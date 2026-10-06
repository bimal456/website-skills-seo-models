---
name: build-brand-casino-site
description: Build and QA a real multi-page casino or other owned-brand website from a brief, preserving supplied outlines and word counts. Use for BRAND site builds, cPanel or Cloudflare Pages packaging, and repairs. Do not use for independent affiliate comparison sites or third-party official-site impersonation.
---

# Build Brand Casino Site

## Required model routing
Read [model-routing.md](references/model-routing.md) before executing production stages. Use the exact user-assigned models, record actual identities and ask before substituting any unavailable model. Never claim a model or Ahrefs was used without evidence.

## Inputs and scope
Read the job brief once. Use [brief.example.json](references/brief.example.json) as the input shape; accept equivalent natural-language instructions. Resolve required brand, domain, GEO, language, keyword, approved tracking URL, hosting target and page outline. Keep secrets out of briefs and Git. Establish brand ownership/operation before using official first-person voice; do not imply ownership of third-party brands. If facts or ownership are missing, report the gap rather than invent it.
Preserve explicit headings, keywords, CTAs and word counts. Default casino homepage minimum: 8,000 words; each secondary SEO page minimum: 4,000 words. Adjust only when the user or supplied outline specifies otherwise. These are production requirements, not Google ranking requirements. Avoid filler and repeated paragraphs; report any depth conflict without silently reducing length. Do not apply SEO page minimums blindly to concise legal utility pages.

## Research checkpoint
Research current SERPs for the target GEO and language. Record engine, query, date, location method and observed URLs. Do not label a generic search as a verified local SERP. If local access is unavailable, disclose that limitation. Extract competitor title, H2s, Conclusion, FAQs and H3 FAQ questions; estimate paragraph/point proportions and explain the estimate. Recommend content depth and additional intent-driven pages without copying. Do not create pages merely because a competitor has them.
Verify bonus terms, licence identity and jurisdiction eligibility with current primary sources. Record URL, date and supported claim in a claims ledger. Do not equate offshore licensing with local authorisation. Keep uncertainties visible in research and avoid unsupported published claims.

## Build checkpoint
Build a real multi-page site: one detailed homepage plus secondary SEO pages, casino default 10. Clarify whether a supplied page count includes utility pages. Make all secondary pages reachable through header navigation, using accessible grouped dropdowns where needed. Include localized About, Contact, Privacy, Terms and Responsible Gambling for casino sites. Describe actual data handling, identity and contact details; do not invent a business address or legal terms.
Use first-person we/our for an owned brand. Feature providers and payment methods rather than rival casinos. Do not add developer credits or KAP Digital credits. Do not fabricate people, reviews, testimonials, teams or experience.
Build /login as information/transition only with no credential collection or official-login imitation. Route Login/Register and all conversion CTAs to /play; use /play/ for Tower Rush. Vary truthful anchor text. Use rel="nofollow sponsored noopener" and target="_blank" only where appropriate. Show a truthful commercial relationship disclosure where applicable.
Use 302 or 307 for the approved /play destination, with no user-agent, referrer or crawler-dependent destination. Never use 301 except genuine migration. Do not block /play in robots.txt when relying on noindex. Add X-Robots-Tag: noindex to the redirect response where supported; verify it on the actual response and do not promise immediate deindexing of a redirect URL. Exclude /play from sitemaps. Optional informational /login noindex must remain crawlable. Never apply production-wide noindex.
Follow [hosting.md](references/hosting.md) for the selected target. Do not deploy a website unless the user requests deployment; deliver cPanel-ready or Cloudflare Pages-ready ZIP when requested.

## Content and design checkpoint
Never use the em dash character in website text. Meta descriptions: focus keyword first, exactly 158 characters, current year, varied original wording; exclude listicle wording, learn, discover and ontdek. Treat character limits as editorial rules, not Google requirements. Add per-page titles; use brief limits when specified.
Use one H1, semantic header/nav/main/footer, logical headings, breadcrumbs, absolute production canonicals, OG/Twitter metadata, correct lang and only genuine multilingual hreflang. Match structured data to visible, supported content. Do not invent ratings or claim FAQ rich-result eligibility; keep useful visible FAQs.
Build original, GEO-specific content with concrete evidence and limitations. Follow [google-qa.md](references/google-qa.md) for freshness and source review.
Use intentional varied layouts and relevant imagery. Avoid generic SaaS styling, repetitive gradients/card grids, glassmorphism, blobs, glow and excessive animation. Use descriptive alt for informative images and empty alt for decorative ones; declare dimensions. Lazy-load below-fold imagery, not the main LCP image. Use consistent logo/favicon. Keep assets working locally and after upload; for a static file:// delivery use compatible relative assets, and also test an HTTP preview for routes and headers.

## QA and release checkpoint
Run python3 scripts/qa_static.py --root DIST --brief BRIEF_JSON. The script checks static output only; it does not certify rendering, legal accuracy, ranking or full SEO compliance. Fix failures; do not edit checks to hide failures. Add automated checks required by the particular brief, including word counts using main editorial content only. Track requirements in a pass/fail/not-tested matrix.
Read [google-qa.md](references/google-qa.md), then inspect mobile/desktop navigation, keyboard access, overflow, CTA destinations, initial and rendered content, forms and normal browser back behavior. Never trap history, inject deceptive redirects or hijack the back button. Check JS console, broken assets, structured-data validity and unsupported claims. Use real browser QA when available; label unavailable checks not tested.
On an authorised staging deployment verify HTTP status, canonical host, HTTPS, headers, redirects, robots, sitemap and a genuinely missing URL. A custom 404 file alone is not proof of a 404 status. Protect staging separately from production and verify production is indexable. Measure performance; aim for LCP <=2.5s, INP <=200ms, CLS <=0.1 where representative field data is available; label lab data separately.
Allow at most the brief's repair rounds, default two; checkpoint work and stop retry loops with a specific unresolved report. For batches keep one brief, directory and deployment identity per site. Reuse scripts rather than restating them in prompts.
Return completed pages, sources, QA evidence, failed/not-tested checks and delivery location. Never claim deployment, GitHub publication or indexing without verification.

## Semantic planning and cannibalization checkpoint
Before research and writing, read [semantic-seo.md](references/semantic-seo.md). Use [seo-map.example.json](references/seo-map.example.json) as the mapping shape. Create a query-to-URL owner map, evidence-based entity/intent coverage, Avalanche-inspired publication waves and contextual internal-link plan. Preserve explicit word counts. Run python3 scripts/qa_seo_map.py --map SEO_MAP_JSON before building and again before release. Review semantic overlaps manually; distinguish planned duplicate targets from demonstrated live cannibalization. Deliver the map, sources and conflict decisions. Treat Avalanche/KGR as hypotheses, not Google requirements or ranking guarantees.

## Portable agent use
Keep this skill and its relative references/scripts together. Fetch the complete directory from a trusted Git repository; reading only a raw SKILL.md URL does not fetch supporting files. On skill-aware agents install in their documented skill path; otherwise explicitly instruct the agent to read this file and follow linked references. Tool availability and instruction hierarchy remain host-specific. Do not assume every LLM has browsing, shell or deployment tools.
