#!/usr/bin/env python3
"""Static affiliate checks; browser, live and factual checks remain separate."""
import argparse,json,sys
from urllib.parse import urlsplit
from pathlib import Path
from qa_common import audit as common_audit,Page,resolve

def audit(root,brief):
 r=common_audit(root,brief)
 def fail(path,message):r['issues'].append({'path':path,'message':message})
 brands=brief.get('brands',[]); routes={}; destinations={}
 if not brands:fail('brief','Missing approved brands')
 for brand in brands:
  route=brand.get('route',''); url=brand.get('approved_url','')
  if not route.startswith('/go/') or route in routes:fail('brief','Missing, invalid or duplicate per-brand /go/ route')
  if urlsplit(url).scheme!='https' or not urlsplit(url).netloc:fail('brief','Approved destination must be absolute HTTPS')
  routes[route.rstrip('/')]=url;destinations[url]=route
 phrase=brief.get('disclosure_text','')
 if not phrase:fail('brief','Missing configured localized disclosure text')
 for config in brief.get('pages',[]):
  f=resolve(root,config['path'])
  if not f:continue
  p=Page();p.feed(f.read_text()); commercial=False
  for t,a in p.tags:
   if t!='a':continue
   href=a.get('href','');u=urlsplit(href)
   internal=not u.netloc or u.netloc==urlsplit(brief.get('domain','')).netloc
   if internal and u.path.rstrip('/')=='/play':fail(config['path'],'Single-brand /play route not allowed in affiliate output')
   if internal and u.path.startswith('/go/'):
    commercial=True
    if u.path.rstrip('/') not in routes:fail(config['path'],'Unapproved affiliate route: '+href)
    if not {'sponsored','nofollow'}<=set(a.get('rel','').split()):fail(config['path'],'Affiliate link missing sponsored/nofollow')
   if href in destinations:
    commercial=True
    if not {'sponsored','nofollow'}<=set(a.get('rel','').split()):fail(config['path'],'Direct affiliate link missing sponsored/nofollow')
   if (href in destinations or internal and u.path.startswith('/go/')) and a.get('target')=='_blank' and 'noopener' not in a.get('rel','').split():fail(config['path'],'New-tab affiliate link missing noopener')
  if commercial and phrase and phrase not in ' '.join(p.main):fail(config['path'],'Missing configured disclosure in main content')
 r['status']='FAIL' if r['issues'] or not r['checked_pages'] else 'PASS_STATIC_ONLY'
 r['not_tested']+=['unlisted external affiliate links','redirect mapping and destination identity','disclosure prominence and factual accuracy']
 return r

def main():
 a=argparse.ArgumentParser();a.add_argument('--root',required=True,type=Path);a.add_argument('--brief',required=True,type=Path);v=a.parse_args()
 try:r=audit(v.root,json.loads(v.brief.read_text()))
 except (OSError,ValueError,KeyError) as e:print(json.dumps({'status':'ERROR','message':str(e)}));return 2
 print(json.dumps(r,indent=2));return 1 if r['status']=='FAIL' else 0
if __name__=='__main__':sys.exit(main())
