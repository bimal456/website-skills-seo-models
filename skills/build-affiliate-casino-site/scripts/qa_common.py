#!/usr/bin/env python3
"""Bounded static HTML checks. Browser and live-server checks are separate."""
import argparse,json,re,sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit,unquote
class Page(HTMLParser):
 def __init__(self):
  super().__init__(convert_charrefs=True); self.tags=[]; self.main=[]; self.title=[]; self.headings=[]; self.in_main=0; self.in_title=0; self.skip=0; self.heading=None
 def handle_starttag(self,t,a):
  a=dict(a); self.tags.append((t,a))
  if t=='main': self.in_main+=1
  if t=='title': self.in_title+=1
  if t in ('script','style'): self.skip+=1
  if re.fullmatch('h[1-6]',t): self.heading=[]
 def handle_endtag(self,t):
  if t=='main': self.in_main=max(0,self.in_main-1)
  if t=='title': self.in_title=max(0,self.in_title-1)
  if t in ('script','style'): self.skip=max(0,self.skip-1)
  if re.fullmatch('h[1-6]',t) and self.heading is not None: self.headings.append(' '.join(self.heading).strip()); self.heading=None
 def handle_data(self,s):
  if self.skip:return
  if self.in_main:self.main.append(s)
  if self.in_title:self.title.append(s)
  if self.heading is not None:self.heading.append(s)
def resolve(root,path):
 path=unquote(urlsplit(path).path).lstrip('/'); p=root/path
 candidates=[p,p/'index.html',p.with_suffix('.html')] if path else [root/'index.html']
 for c in candidates:
  if c.resolve().is_relative_to(root.resolve()) and c.is_file():return c
 return None
def audit(root,brief):
 issues=[]; checked=0
 def fail(path,msg):issues.append({'path':path,'message':msg})
 domain=brief.get('domain','').rstrip('/')
 for name in ('robots.txt','sitemap.xml'):
  if not (root/name).is_file():fail('/',f'Missing {name}')
 robots=(root/'robots.txt').read_text() if (root/'robots.txt').exists() else ''
 if re.search(r'^\s*Disallow:\s*/go(?:/.*)?\s*$',robots,re.M|re.I):fail('/play','Disallow conflicts with intended crawl-visible noindex')
 if re.search(r'^\s*Disallow:\s*/\s*$',robots,re.M|re.I):fail('/','Root crawl block requires review')
 for u in brief.get('utility_pages',[]):
  if not resolve(root,u):fail(u,'Missing required utility page')
 seen_titles=set(); seen_desc=set()
 for config in brief.get('pages',[]):
  path=config['path']; f=resolve(root,path)
  if not f:fail(path,'Missing planned page');continue
  checked+=1; raw=f.read_text(); p=Page(); p.feed(raw)
  title=''.join(p.title).strip(); main=' '.join(p.main)
  desc=[a.get('content','') for t,a in p.tags if t=='meta' and a.get('name','').lower()=='description']
  canonical=[a.get('href','') for t,a in p.tags if t=='link' and 'canonical' in a.get('rel','').split()]
  if sum(t=='h1' for t,a in p.tags)!=1:fail(path,'Expected exactly one H1')
  if not any(t=='html' and a.get('lang')==brief.get('language') for t,a in p.tags):fail(path,'Missing or incorrect lang')
  if not p.main:fail(path,'Missing static main content; inspect rendering')
  if len(re.findall(r"\b\w+(?:['’-]\w+)*\b",main))<config.get('min_words',0):fail(path,'Main-content word minimum not met')
  if len(canonical)!=1 or canonical[0]!=domain+path:fail(path,'Canonical does not match planned production URL')
  if not brief.get('title_min',0)<=len(title)<=brief.get('title_max',10000):fail(path,'Title length outside configured range')
  if not title or title in seen_titles:fail(path,'Missing or duplicate title')
  seen_titles.add(title)
  if len(desc)!=1:fail(path,'Expected one meta description');d=''
  else:d=desc[0]
  if len(d)!=brief.get('meta_description_length',158):fail(path,'Description length mismatch')
  if not d.startswith(config.get('keyword',brief.get('primary_keyword',''))):fail(path,'Description must start with focus keyword')
  if str(brief.get('year','')) not in d:fail(path,'Description missing configured current year')
  if d in seen_desc:fail(path,'Duplicate description')
  seen_desc.add(d)
  for word in brief.get('forbidden_words',[]):
   if re.search(r'\b'+re.escape(word)+r'\b',d,re.I):fail(path,'Forbidden description wording: '+word)
  if '\u2014' in raw:fail(path,'Em dash present')
  for h in config.get('required_headings',[]):
   if h not in p.headings:fail(path,'Missing required heading: '+h)
  for t,a in p.tags:
   if t=='input' and a.get('type','').lower()=='password':fail(path,'Credential capture prohibited')
   if t=='meta' and a.get('name','').lower() in ('robots','googlebot') and 'noindex' in a.get('content','').lower():fail(path,'Planned SEO page is noindex')
   if t=='img' and ('alt' not in a or not a.get('width') or not a.get('height')):fail(path,'Image missing alt attribute or dimensions')
   if t=='a':
    href=a.get('href',''); url=urlsplit(href)
    if url.scheme in ('mailto','tel') or href.startswith('#'):continue
    if href.startswith('javascript:'):fail(path,'Noncrawlable JavaScript link');continue
    if url.path.rstrip('/')=='/play' and (not url.netloc or url.netloc==urlsplit(domain).netloc):
     if not {'nofollow','sponsored','noopener'}<=set(a.get('rel','').split()):fail(path,'Conversion link missing required rel tokens')
    elif href and not url.path.startswith('/go/') and (not url.netloc or url.netloc==urlsplit(domain).netloc) and not resolve(root,url.path):fail(path,'Broken local link: '+href)
  for payload in re.findall(r'<script[^>]*type=[\"\']application/ld\+json[\"\'][^>]*>(.*?)</script>',raw,re.S|re.I):
   try:json.loads(payload)
   except ValueError:fail(path,'Invalid JSON-LD')
 return {'checked_pages':checked,'status':'FAIL' if issues or not checked else 'PASS_STATIC_ONLY','issues':issues,'not_tested':['browser layout and navigation','live status and redirect headers','source truth and legal accuracy','Search Console indexing','performance field data','image aspect ratio and originality','schema semantic correctness']}
def main():
 a=argparse.ArgumentParser();a.add_argument('--root',required=True,type=Path);a.add_argument('--brief',required=True,type=Path);v=a.parse_args()
 try:r=audit(v.root,json.loads(v.brief.read_text()))
 except (OSError,ValueError,KeyError) as e:print(json.dumps({'status':'ERROR','message':str(e)}));return 2
 print(json.dumps(r,indent=2));return 1 if r['status']=='FAIL' else 0
if __name__=='__main__':sys.exit(main())
