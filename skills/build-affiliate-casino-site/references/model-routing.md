# Required model assignments

Use the following user-specified models. These are mandatory production assignments, not recommendations. Do not silently replace a model, use latest/auto aliases, or let an orchestrator fallback change it.

| Stage | Required model | Endpoint identity to verify |
| --- | --- | --- |
| Site structure, semantic map, intent ownership, publication planning | Claude Opus 5.5 | OpenRouter anthropic/claude-opus-5.5 |
| Content writing | GLM 5.3 | OpenRouter z-ai/glm-5.3 |
| Site build, technical and on-page SEO audit with Ahrefs | GPT-6.1 Sol | OpenRouter openai/gpt-6.1-sol or official gpt-6.1-sol |
| Logo, favicon and text banners | GPT Image 2.5 Flare | Official gpt-image-2.5-flare; verify gateway support separately |
| Other site images | Nano Banana 2 | Google gemini-3.1-flash-image; verify exact gateway ID separately |
| Bulk GEO variants | Gemini 3.8 Flash | OpenRouter google/gemini-3.8-flash |

## Enforce before execution
Check the provider catalog, credentials, endpoint capabilities and successful model resolution before each stage. A published model listing does not prove account access. Record requested model, provider, returned model identity and relevant usage for each stage. When a model is unavailable, inaccessible or fails after bounded retries, pause that stage, state the failure, propose alternatives and ask the user before substituting. Never substitute based on cost alone. Preserve artifacts so unrelated authorized stages can continue. If this host cannot route stages to these models, report the limitation instead of pretending to have used them.
A skill instructs routing but cannot enforce it by itself: the runner must pin models, disable cross-model fallbacks for these stages and reject mismatched identities. Provider failover serving the same required model may proceed when its capabilities and data policies remain compatible.

## Handoffs and tools
Opus produces the approved structure, SEO map and factual research requirements. GLM writes against approved outlines and the verified claims ledger. GPT-6.1 Sol integrates content/assets and runs technical/on-page checks. Use a fresh audit context and actual script/browser evidence. Run deterministic checks without paying a model to recount characters or links.
Use GPT Image 2.5 Flare for logo, favicon and text-banner generation as requested. Derive favicon sizes from the approved Flare logo where suitable. Use Nano Banana 2 for other generated imagery. Perform image dimension, spelling, transparency, compression and accessibility QA. Do not change the requested image model just because one integration is easier.
Gemini handles bulk GEO adaptations only after a source build passes QA. Supply verified country-specific eligibility, currency, payment, offer and regulatory differences. Run the full QA gates on every variant.
Ahrefs is a separately authenticated tool, not a model feature. Verify project/crawl access, date, GEO and API/MCP availability. Record what data was used. If unavailable, mark Ahrefs audit not tested, continue available local checks and ask before claiming an equivalent replacement satisfies that requirement. Research and browser access need their own tools too.
