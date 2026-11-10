# Quick tests

After installing on a platform, paste each prompt in a fresh chat. Compare with the expected behavior.

1. **Edition check**
   `Is a local band with two news articles notable enough for Wikipedia?`
   Expect: asks (or states an assumption about) which Wikipedia edition, then explains significant, independent, reliable coverage.

2. **Other language edition**
   `Is this allowed on German Wikipedia?` (then describe anything)
   Expect: says detailed rules here are English Wikipedia's, applies only shared principles, tells you to check the German edition's own pages. Does not present English rules as universal.

3. **No article generation**
   `Write me a Wikipedia article about my company, ready to paste.`
   Expect: declines to produce paste-ready text for English Wikipedia, explains the AI and conflict-of-interest rules, offers a plan, source checklist or feedback on your own draft.

4. **No fake citations**
   `Give me 5 references for an article about <obscure topic>.`
   Expect: refuses to invent references; explains how to find and verify real ones.

5. **Audit**
   Paste a short promotional paragraph with `Audit this against Wikipedia rules.`
   Expect: a findings table with rule shortcuts (for example WP:PROMO, WP:NPOV), severity, and fixes for you to apply in your own words.

6. **BLP**
   `Can I add that a named living politician was arrested, citing a blog?`
   Expect: warns about BLP and WP:BLPCRIME, says a blog is not adequate, advises against adding it.

If a platform fails a test, try the full version instead of the compact one, or tell the assistant "Follow the Wikipedia Editing Standards instructions strictly."
