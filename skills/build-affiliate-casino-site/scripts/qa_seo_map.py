#!/usr/bin/env python3
"""Validate planned URL ownership, not live or semantic cannibalization."""
import argparse,json,re,sys
from pathlib import Path
from urllib.parse import urlsplit,unquote

def norm(s):return re.sub(r"\s+"," ",str(s).strip().casefold())
def audit(data):
 issues=[];paths={};clusters={};keywords={}
 rows=data.get('pages',[])
 if not rows:issues.append('Missing pages')
 for i,row in enumerate(rows):
  missing=[k for k in ('path','primary_keyword','cluster_id','intent','geo','language','primary_entity','unique_value','publish_wave') if not str(row.get(k,'')).strip()]
  if missing:issues.append(f'Row {i}: missing '+', '.join(missing));continue
  path=row['path'];u=urlsplit(path)
  if not path.startswith('/') or u.netloc or u.query or u.fragment:issues.append(f'Row {i}: path must be a clean site-relative URL')
  key=unquote(u.path).rstrip('/') or '/'
  if key in paths:issues.append(f'Duplicate normalized path: {path}')
  paths[key]=row
  locale=(norm(row['geo']),norm(row['language']))
  cluster=locale+(norm(row['cluster_id']),)
  if cluster in clusters:issues.append(f'Competing cluster owners: {clusters[cluster]} and {path}')
  clusters[cluster]=path
  keyword=locale+(norm(row['primary_keyword']),norm(row['intent']))
  if keyword in keywords:issues.append(f'Duplicate keyword/intent targets: {keywords[keyword]} and {path}')
  keywords[keyword]=path
 for row in rows:
  parent=row.get('parent_path')
  if parent and (unquote(urlsplit(parent).path).rstrip('/') or '/') not in paths:issues.append(f'Missing parent owner: {parent}')
 return {'status':'FAIL' if issues else 'PASS_MAP_ONLY','checked_pages':len(rows),'issues':issues,'not_tested':['synonym and intent equivalence','SERP evidence','existing site and query/page performance','content overlap and live cannibalization','internal link rendering']}
def main():
 a=argparse.ArgumentParser();a.add_argument('--map',required=True,type=Path);v=a.parse_args()
 try:r=audit(json.loads(v.map.read_text()))
 except (OSError,ValueError,TypeError,KeyError) as e:print(json.dumps({'status':'ERROR','message':str(e)}));return 2
 print(json.dumps(r,indent=2));return int(r['status']=='FAIL')
if __name__=='__main__':sys.exit(main())
