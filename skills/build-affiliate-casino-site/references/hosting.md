# Hosting targets

## Apache/cPanel
Confirm Apache-compatible .htaccess support, document root and HTTPS availability. Configure clean URLs, a true ErrorDocument 404, and a 403 document when relevant. Set the approved /go/brand-slug/ redirect and its X-Robots-Tag response header with compatible server directives. Check that headers are attached to the redirect response, not just an HTML page. Test syntax on the target; do not assume every cPanel host uses identical modules. Do not ship credentials.

## Cloudflare Pages
Use static output plus Pages _redirects and _headers where applicable; .htaccess has no effect. Configure /go/brand-slug/ 302 to the approved destination. Verify whether _headers attaches to that redirect response on the chosen deployment path. If not, use a Pages Function/Worker response with explicit Location and X-Robots-Tag headers, or record the limitation. Static rule headers do not automatically apply to Function-generated responses. Use 404.html and verify the missing-path status; avoid unintended SPA fallback. Keep routing consistent with canonicals and slash conventions. Verify current official Cloudflare documentation before implementation.

## Both
Serve /robots.txt and /sitemap.xml from the root. Include only canonical, indexable, successful content URLs in the sitemap. Do not Disallow URLs whose noindex must be read. Use identical destinations for users and crawlers. Verify target URLs without collecting login credentials. Test live headers using an authorised HTTP client; local file previews cannot verify server behavior.
