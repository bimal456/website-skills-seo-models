# Google and manual QA

Reviewed: 2026-10-06. Recheck official guidance before future builds; this date is not a promise that all ranking updates have been audited.

## Sources
- Noindex and crawl access: https://developers.google.com/search/docs/crawling-indexing/block-indexing
- JavaScript and crawlable links: https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics
- Spam policies: https://developers.google.com/search/docs/essentials/spam-policies
- Back-button hijacking: https://developers.google.com/search/blog/2026/04/back-button-hijacking
- Helpful content: https://developers.google.com/search/docs/fundamentals/creating-helpful-content
- Documentation changes: https://developers.google.com/search/updates
- AI content: https://developers.google.com/search/docs/fundamentals/using-gen-ai-content

## Required review
1. Inspect current official updates and spam policies. Record only applicable changes and dated primary sources; do not invent special AI-class-name penalties or ranking guarantees.
2. Verify original value and page intent. Preserve user word counts while removing repetition; never treat volume, keyword density, E-E-A-T labels or an AI detector score as a ranking guarantee.
3. Check factual ownership, contact, licence scope, bonus wagering/expiry/eligibility and responsible gambling information against primary sources. Block unsupported material claims. Never create fake first-hand testing.
4. Check initial HTML and rendered content, crawlable href links, successful canonical pages, real 404 status, robots/noindex interactions, sitemap coverage and hreflang reciprocity only for real translations.
5. Inspect navigation and back behavior manually. Check no deceptive redirects, cloaking, doorway variants, scaled low-value pages, fabricated schema or keyword stuffing. Flag suspicious history/pushState usage for review; normal client routing is not automatically abuse.
6. Test at 360px, 768px and desktop widths; inspect overflow, accessible dropdowns, focus, buttons, image loading and console errors. Do not assert these passed from static source alone.
7. Validate production headers and redirect destination after authorised deployment. Use Search Console URL Inspection when access is provided. Indexing and ranking cannot be certified from a successful build.
8. Keep every requirement as pass/fail/not-tested with evidence. Automated success is necessary for covered checks but does not replace editorial, legal or browser review.

## Source-document changes
Preserved homepage minimum 8,000 and secondary SEO page minimum 4,000 words, outlined content, metadata formatting, navigation, design and delivery rules. Corrected contradictory /play noindex plus Disallow. Separated Apache and Pages configuration. Added rendering, mobile/keyboard QA, redirect-response verification, browser-back checks, current source ledger and honest release evidence. Excluded utility legal pages from unrequested SEO padding. Brand only: second site type absent from supplied document.
