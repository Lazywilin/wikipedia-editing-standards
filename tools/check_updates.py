#!/usr/bin/env python3
"""
check_updates.py - detect when Wikipedia's rule pages have changed.

What it does
  1. Resolves a list of core rule shortcuts (WP:NPOV, WP:V, ...) to their real pages.
  2. Optionally also reads the page "Wikipedia:List of policies and guidelines" and
     collects every project-namespace page it links to (--listing).
  3. Fetches the latest revision id and edit time of each page from the MediaWiki API.
  4. Compares with the previous run (rules/revisions.json) and reports what changed.
  5. Optionally rewrites rules-index.md (--write) and saves page text snapshots (--snapshot DIR).

What it does NOT do
  It does not rewrite SKILL.md. A change report tells a human (or an AI-assisted review)
  which pages to re-read; the digest is then updated deliberately.

Usage
  python tools/check_updates.py                       # compare only, print report
  python tools/check_updates.py --listing --write     # full list, update state + index
  python tools/check_updates.py --snapshot snapshots  # also save plain-text copies
  python tools/check_updates.py --report report.md    # write the change report to a file

Exit codes: 0 = no changes (or first run baseline), 10 = changes detected, 2 = error.
Requires Python 3.8+ and internet access. Standard library only.
Wikipedia text is available under CC BY-SA 4.0; keep attribution if you redistribute snapshots.
"""
import argparse, json, os, re, sys, time, urllib.parse, urllib.request
from datetime import datetime, timezone
from html.parser import HTMLParser

API = "https://en.wikipedia.org/w/api.php"
UA = "wikipedia-editing-standards-checker/1.0 (https://github.com/Lazywilin/wikipedia-editing-standards)"
LIST_PAGE = "Wikipedia:List of policies and guidelines"

# (shortcut, label). Shortcuts resolve through MediaWiki redirects.
CORE = [
    ("WP:5P", "Five pillars"), ("WP:POLICY", "Policies and guidelines"), ("WP:LPG", "List of policies and guidelines"),
    ("WP:IAR", "Ignore all rules"),
    ("WP:NPOV", "Neutral point of view"), ("WP:V", "Verifiability"), ("WP:NOR", "No original research"),
    ("WP:BLP", "Biographies of living persons"), ("WP:NOT", "What Wikipedia is not"),
    ("WP:COPYRIGHT", "Copyrights"), ("WP:COPYVIO", "Copyright violations"),
    ("WP:NFCC", "Non-free content criteria"), ("WP:IUP", "Image use policy"), ("WP:AT", "Article titles"),
    ("WP:RS", "Reliable sources"), ("WP:RSP", "Perennial sources"), ("WP:MEDRS", "Medical sources"),
    ("WP:SPS", "Self-published sources"), ("WP:N", "Notability"), ("WP:BIO", "Notability (people)"),
    ("WP:NCORP", "Notability (organizations and companies)"), ("WP:NSPORT", "Notability (sports)"),
    ("WP:NMUSIC", "Notability (music)"), ("WP:NPROF", "Notability (academics)"),
    ("WP:NFILM", "Notability (films)"), ("WP:NBOOK", "Notability (books)"),
    ("WP:GEOLAND", "Notability (geographic features)"), ("WP:FRINGE", "Fringe theories"),
    ("WP:MOS", "Manual of Style"), ("MOS:LEAD", "Lead section"), ("WP:LAYOUT", "Layout"),
    ("WP:CITE", "Citing sources"), ("WP:CITEVAR", "Citation style variation"), ("WP:LINKROT", "Link rot"),
    ("WP:EL", "External links"), ("WP:CAT", "Categorization"), ("WP:DAB", "Disambiguation"),
    ("WP:REDIRECT", "Redirect"), ("WP:INFOBOX", "Infoboxes"), ("WP:SIZE", "Article size"),
    ("WP:MERGE", "Merging"), ("WP:SPLIT", "Splitting"), ("MOS:ENGVAR", "English varieties"),
    ("WP:NEWLLM", "Writing articles with large language models"), ("WP:LLM", "Large language models"),
    ("WP:BOTPOL", "Bot policy"),
    ("WP:CIVIL", "Civility"), ("WP:NPA", "No personal attacks"), ("WP:AGF", "Assume good faith"),
    ("WP:BITE", "Do not bite newcomers"), ("WP:HARASS", "Harassment"), ("WP:OUTING", "Outing"),
    ("WP:NLT", "No legal threats"), ("WP:EW", "Edit warring"), ("WP:3RR", "Three-revert rule"),
    ("WP:OWN", "Ownership of content"), ("WP:CANVASS", "Canvassing"), ("WP:SOCK", "Sockpuppetry"),
    ("WP:COI", "Conflict of interest"), ("WP:PAID", "Paid-contribution disclosure"),
    ("WP:USERNAME", "Username policy"), ("WP:DISRUPT", "Disruptive editing"), ("WP:NOTHERE", "Not here to build an encyclopedia"),
    ("WP:CON", "Consensus"), ("WP:DR", "Dispute resolution"), ("WP:RFC", "Requests for comment"),
    ("WP:3O", "Third opinion"), ("WP:TPG", "Talk page guidelines"), ("WP:CT", "Contentious topics"),
    ("WP:ECR", "Extended confirmed restriction"), ("WP:BLOCK", "Blocking policy"), ("WP:BAN", "Banning policy"),
    ("WP:PROTECT", "Protection policy"), ("WP:VAND", "Vandalism"),
    ("WP:DEL", "Deletion policy"), ("WP:CSD", "Criteria for speedy deletion"), ("WP:PROD", "Proposed deletion"),
    ("WP:BLPPROD", "Proposed deletion of unsourced BLPs"), ("WP:AFD", "Articles for deletion"),
    ("WP:ATD", "Alternatives to deletion"), ("WP:BEFORE", "Before nominating for deletion"),
    ("WP:DRAFTIFY", "Draftification"), ("WP:AFC", "Articles for creation"),
]

def api_get(params, retries=3):
    params = dict(params, format="json", formatversion="2")
    url = API + "?" + urllib.parse.urlencode(params)
    last = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.loads(r.read().decode("utf-8"))
        except Exception as e:  # network or JSON problems
            last = e
            time.sleep(1.5 * (attempt + 1))
    raise RuntimeError(f"API request failed: {last}")

def chunks(seq, n):
    for i in range(0, len(seq), n):
        yield seq[i:i + n]

def fetch_revisions(titles):
    """Return {resolved_title: {revid, timestamp, requested}} and a list of missing requests."""
    out, missing = {}, []
    for group in chunks(titles, 40):
        data = api_get({"action": "query", "titles": "|".join(group), "redirects": "1",
                        "prop": "revisions", "rvprop": "ids|timestamp"})
        q = data.get("query", {})
        # map: requested title -> resolved title (via normalized + redirects)
        mapping = {t: t for t in group}
        for n in q.get("normalized", []):
            for k, v in list(mapping.items()):
                if v == n["from"]: mapping[k] = n["to"]
        for rd in q.get("redirects", []):
            for k, v in list(mapping.items()):
                if v == rd["from"]: mapping[k] = rd["to"]
        pages = {p["title"]: p for p in q.get("pages", [])}
        for req, res in mapping.items():
            p = pages.get(res)
            if not p or p.get("missing") or not p.get("revisions"):
                missing.append(req); continue
            rev = p["revisions"][0]
            out[res] = {"revid": rev["revid"], "timestamp": rev["timestamp"], "requested": req}
        time.sleep(0.3)
    return out, missing

def fetch_listing_titles():
    data = api_get({"action": "parse", "page": LIST_PAGE, "prop": "links", "redirects": "1"})
    titles = []
    for l in data.get("parse", {}).get("links", []):
        if l.get("ns") == 4 and l.get("exists", True):   # ns 4 = Wikipedia: project namespace
            titles.append(l["title"])
    return sorted(set(titles))

class _Text(HTMLParser):
    SKIP = {"script", "style", "table", "sup"}
    def __init__(self):
        super().__init__(); self.buf, self.skip = [], 0
    def handle_starttag(self, tag, attrs):
        if tag in self.SKIP: self.skip += 1
        if tag in ("p", "li", "h1", "h2", "h3", "h4", "br", "div"): self.buf.append("\n")
    def handle_endtag(self, tag):
        if tag in self.SKIP and self.skip: self.skip -= 1
    def handle_data(self, d):
        if not self.skip: self.buf.append(d)

def html_to_text(html):
    p = _Text(); p.feed(html)
    text = "".join(p.buf)
    text = re.sub(r"[ \t\r\f\v]+", " ", text)
    return re.sub(r"\n\s*\n+", "\n\n", text).strip()

def save_snapshot(directory, title, info):
    os.makedirs(directory, exist_ok=True)
    data = api_get({"action": "parse", "page": title, "prop": "text", "redirects": "1"})
    text = html_to_text(data["parse"]["text"])
    slug = re.sub(r"[^A-Za-z0-9._-]+", "_", title)[:120]
    url = page_url(title)
    header = (f"Title: {title}\nSource: {url}\nRevision: {info['revid']} ({info['timestamp']})\n"
              f"License: CC BY-SA 4.0 (Wikipedia contributors)\n\n")
    with open(os.path.join(directory, slug + ".txt"), "w", encoding="utf-8") as f:
        f.write(header + text + "\n")
    time.sleep(0.3)

def diff_state(old, new):
    changed, added, removed = [], [], []
    for t, v in new.items():
        if t not in old: added.append(t)
        elif old[t]["revid"] != v["revid"]: changed.append(t)
    for t in old:
        if t not in new: removed.append(t)
    return sorted(changed), sorted(added), sorted(removed)

def page_url(title):
    return "https://en.wikipedia.org/wiki/" + urllib.parse.quote(title.replace(" ", "_"), safe=":/()")

def build_report(old, new, changed, added, removed, missing, first_run):
    lines = [f"# Wikipedia rules check ({datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')})", ""]
    if first_run:
        lines += [f"Baseline created for {len(new)} pages. Nothing to compare yet.", ""]
    else:
        lines += [f"Pages checked: {len(new)}. Changed: {len(changed)}. New: {len(added)}. Removed: {len(removed)}.", ""]
    if changed:
        lines += ["## Changed since last check", ""]
        for t in changed:
            o, n = old[t]["revid"], new[t]["revid"]
            lines.append(f"- [{t}]({page_url(t)}), edited {new[t]['timestamp']}: "
                         f"[view diff](https://en.wikipedia.org/w/index.php?diff={n}&oldid={o})")
        lines.append("")
    if added:
        lines += ["## New pages in the list", ""] + [f"- [{t}]({page_url(t)})" for t in added] + [""]
    if removed:
        lines += ["## No longer in the list", ""] + [f"- {t}" for t in removed] + [""]
    if missing:
        lines += ["## Shortcuts that did not resolve (renamed or removed?)", ""] + [f"- {t}" for t in missing] + [""]
    if changed or added:
        lines += ["## Next step", "",
                  "Read the changed pages, then update `SKILL.md`, `system-prompt-full.md` and "
                  "`system-prompt-compact.txt` where the digest is now out of date. Bump the version and `last_updated`.", ""]
    return "\n".join(lines)

def write_index(path, new, labels):
    rows = ["# Rule index", "",
            "Generated by `tools/check_updates.py`. Revision ids and edit times come from the MediaWiki API.", "",
            "| Page | Label | Last revision | Last edited (UTC) |", "|---|---|---|---|"]
    for t in sorted(new):
        info = new[t]
        label = labels.get(info.get("requested", ""), "")
        rows.append(f"| [{t}]({page_url(t)}) | {label} | {info['revid']} | {info['timestamp']} |")
    rows += ["", "Complete official list: https://en.wikipedia.org/wiki/Wikipedia:List_of_policies_and_guidelines", ""]
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(rows))

def main(argv=None):
    ap = argparse.ArgumentParser(description="Detect changes in Wikipedia policy and guideline pages.")
    ap.add_argument("--listing", action="store_true", help="also include every page linked from the official list")
    ap.add_argument("--write", action="store_true", help="update the state file and rules-index.md")
    ap.add_argument("--snapshot", metavar="DIR", help="save plain-text copies of every page into DIR")
    ap.add_argument("--state", default="rules/revisions.json")
    ap.add_argument("--index", default="rules-index.md")
    ap.add_argument("--report", metavar="FILE", help="write the change report to FILE")
    a = ap.parse_args(argv)

    try:
        labels = {s: l for s, l in CORE}
        titles = [s for s, _ in CORE]
        if a.listing:
            titles += [t for t in fetch_listing_titles() if t not in titles]
        new, missing = fetch_revisions(titles)
    except Exception as e:
        print("ERROR:", e, file=sys.stderr); return 2

    old, first_run = {}, True
    if os.path.exists(a.state):
        with open(a.state, encoding="utf-8") as f:
            old = json.load(f).get("pages", {}); first_run = False
    changed, added, removed = ([], [], []) if first_run else diff_state(old, new)
    report = build_report(old, new, changed, added, removed, missing, first_run)
    print(report)
    if a.report:
        with open(a.report, "w", encoding="utf-8") as f: f.write(report)
    if a.snapshot:
        try:
            for t, info in new.items(): save_snapshot(a.snapshot, t, info)
        except Exception as e:
            print("ERROR while saving snapshots:", e, file=sys.stderr); return 2
    if a.write:
        os.makedirs(os.path.dirname(a.state) or ".", exist_ok=True)
        with open(a.state, "w", encoding="utf-8") as f:
            json.dump({"generated": datetime.now(timezone.utc).isoformat(), "pages": new}, f, indent=1, sort_keys=True)
        write_index(a.index, new, labels)
    return 10 if (changed or added) else 0

if __name__ == "__main__":
    sys.exit(main())
