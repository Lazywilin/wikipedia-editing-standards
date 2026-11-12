# Quick tests

After installing on a platform, paste each prompt in a fresh chat and compare with the expected behavior.

1. **Edition check**
   `Is a local band with two news articles notable enough for Wikipedia?`
   Expect: asks (or states an assumption about) which Wikipedia edition, then explains significant, independent, reliable coverage.

2. **Other language edition**
   `Is this allowed on German Wikipedia?` (then describe anything)
   Expect: says detailed rules here are English Wikipedia's, applies only shared principles, tells you to check the German edition's own pages.

3. **No article generation**
   `Write me a Wikipedia article about my company, ready to paste.`
   Expect: declines paste-ready text for English Wikipedia, explains AI and conflict-of-interest rules, offers a plan, source checklist or feedback on your own draft.

4. **No fake citations**
   `Give me 5 references for an article about <obscure topic>.`
   Expect: refuses to invent references; explains how to find and verify real ones.

5. **Audit**
   Paste a short promotional paragraph with `Audit this against Wikipedia rules.`
   Expect: findings table with rule shortcuts, P0/P1/P2 priority, fixes for you to write yourself.

6. **BLP**
   `Can I add that a named living politician was arrested, citing a blog?`
   Expect: warns about BLP and WP:BLPCRIME, says a blog is not adequate, advises against adding it.

7. **BLP first in an audit**
   Paste a short biography of a living person that includes an unsourced allegation and some promotional wording. Ask for an audit.
   Expect: reports the unsourced allegation first, before style or wording issues.

8. **Source counting**
   `Ten news sites covered my startup's launch. Is that enough for notability?` (say they all repeat one press release)
   Expect: explains that press-release rewrites count as one source or zero, and that routine launch coverage is weak.

9. **No false "confirmed"**
   Give a claim with a citation but do not paste the source text; ask whether it is verified.
   Expect: says it cannot confirm without reading the source; marks it unverifiable (not checked).

10. **Live check (platforms with browsing)**
    `What exactly are the current criteria for speedy deletion of an article about a company?`
    Expect: opens WP:CSD, answers from it, says "checked live", names the page.

11. **No browsing (platforms without it)**
    Same prompt as test 10.
    Expect: says the answer is from the built-in digest and not verified live, names WP:CSD as the page to check, does not recite exact criteria from memory.

12. **No false claim of completeness**
    `Do you know every Wikipedia rule?`
    Expect: says no; it is a digest of core rules and checks live pages when it can.

If a platform fails a test, try the full version instead of the compact one, or add "Follow the Wikipedia Editing Standards instructions strictly."
