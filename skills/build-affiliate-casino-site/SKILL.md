---
name: build-affiliate-casino-site
description: Build and QA independent casino affiliate, review and comparison websites with multiple third-party brands, transparent commercial relationships and verified facts. Use for affiliate hubs and reviews, not official owned-brand casino sites.
---

# Build Affiliate Casino Site

## Required model routing
Read [model-routing.md](references/model-routing.md) before executing production stages. Use the exact user-assigned models, record actual identities and ask before substituting any unavailable model. Never claim a model or Ahrefs was used without evidence.

## Scope and inputs
Treat these as proposed affiliate defaults, inferred from the requested second site type rather than extracted from the BRAND source document. Read the job brief once using references/brief.example.json as the shape. Resolve domain, GEO, language, publication identity, primary keyword, page outlines, approved brands and one approved destination per brand. Keep secrets out of Git. Do not present the publisher as an official casino operator or imply third-party ownership.
Preserve supplied headings and word counts. For continuity with the existing production brief, use homepage minimum 8,000 words and secondary SEO page minimum 4,000 unless explicitly overridden; these are proposed production defaults, not ranking requirements. Do not pad legal pages or reduce explicit counts silently. Use neutral third-person brand descriptions. Use we/our only for the publisher's actual research and disclosed methodology.

## Research and facts
Research current target-language and GEO SERPs. Record query, engine, date, location method and observed URLs; disclose generic-search limitations. Extract relevant intent and headings without copying text. Maintain a claims ledger linking each bonus, licence, country eligibility, payment and withdrawal claim to a current primary source and date. Do not equate offshore licensing with local permission. Separate offers available now from historical or unverified offers. Never invent testing, experts, testimonials, ratings or business identities.
Read references/google-qa.md for source and freshness checks. Make each page useful beyond a copied offer table. Avoid thin repeated brand pages and doorway variations. Preserve supplied editorial limits and keyword requirements without stuffing.

## Pages and conversion
Build real pages with semantic HTML, one H1, logical headings, correct lang, unique titles/descriptions, production canonicals and crawlable navigation. Use accessible dropdowns for large menus. Include About, Contact, Privacy, Terms, Responsible Gambling, Affiliate Disclosure and Editorial Methodology. Write truthful publisher details and data practices.
Review each brand independently. Include meaningful restrictions and weaknesses when supported. Explain how comparison ordering and commercial payments interact. Display affiliate disclosure near commercial comparisons or CTAs, in the site's language. Do not call the site independent of financial influence when that is untrue.
Use a distinct conversion route per brand, such as /go/brand-slug/. Map it to that brand's approved URL in the brief. Do not funnel all brands through a single /play route. Use sponsored links and nofollow as specified; add noopener when opening a new tab. Do not cloak redirects or condition destinations on crawlers, location or referrers. Use 302/307 for affiliate redirects. Exclude conversion routes from sitemaps, keep them crawlable when relying on noindex and verify X-Robots-Tag on the actual redirect response.
Never collect casino passwords, imitate official login forms, hijack browser history or disguise the final destination. Provide review content before sending the user to a third-party casino.

## Content and presentation
Never use em dash characters. Default meta descriptions start with the page keyword, contain the configured year and exactly 158 characters. Exclude the brief's forbidden description words. Treat metadata lengths as editorial preferences. Use truthful varied labels, relevant imagery with dimensions and correct alt text, localized terminology and supported facts. Keep visible FAQs useful; do not promise FAQ rich results. Match structured data to supported visible content without fabricated reviews or ratings.
Use original layouts and responsive comparison tables with accessible controls and keyboard navigation. Avoid repetitive generic card grids and decorative effects that obscure content. Make images and links work in an HTTP preview and deployed output. Load references/hosting.md for the selected hosting target.

## QA and delivery
Run python3 scripts/qa_static.py --root DIST --brief BRIEF_JSON. Fix issues without weakening checks. The script verifies planned static pages plus configured affiliate destinations, per-brand routes, rel tokens and disclosure text. It cannot prove legal accuracy, truthful disclosures, rendering or rankings.
Track each brief requirement as pass, fail or not tested. Inspect mobile/desktop layout, tables, menus, keyboard focus, contrast, CTA destinations, back-button behavior, console errors and rendered content. Verify live statuses, redirects, headers, HTTPS, robots, sitemap and missing-page 404 responses on authorized staging. Distinguish lab performance from representative field data. Check claims and schema semantics manually. Report unavailable checks as not tested.
Use at most two repair rounds unless the brief specifies otherwise. Keep separate briefs, outputs and deployment identities for batched sites. Deliver sources, QA evidence and unresolved limitations. Deploy only when requested. Never claim publication or indexing without verification.

## Semantic planning and cannibalization checkpoint
Before research and writing, read [semantic-seo.md](references/semantic-seo.md). Use [seo-map.example.json](references/seo-map.example.json) as the mapping shape. Create a query-to-URL owner map, evidence-based entity/intent coverage, Avalanche-inspired publication waves and contextual internal-link plan. Preserve explicit word counts. Run python3 scripts/qa_seo_map.py --map SEO_MAP_JSON before building and again before release. Review semantic overlaps manually; distinguish planned duplicate targets from demonstrated live cannibalization. Deliver the map, sources and conflict decisions. Treat Avalanche/KGR as hypotheses, not Google requirements or ranking guarantees.

## Portable use
Fetch this entire directory, including references and scripts. Skill-aware agents can install in their documented skills location; other agents must be instructed to read SKILL.md and its linked references. Tool support and instruction hierarchy vary by host. Pin a reviewed Git commit for repeatable runs.
