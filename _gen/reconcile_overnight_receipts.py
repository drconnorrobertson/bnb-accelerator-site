"""Read-only bounded overnight receipt pairing. Prints evidence, never submits."""
import json,re,subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
BASE='6820e04e7e1be4606900e6efbb48dafc9557ee5b'
END='4135d6245a016f23cebed69f93455f24f49ba96d'
HOST='https://www.bnbaccelerator.com'

def git(*args):return subprocess.check_output(['git',*args],cwd=ROOT,text=True)
def body(s):
 m=re.search(r'<article class="article">(.*?)</article>',s,re.S)
 return m[1] if m else ''

def main():
 existing=[];new=[]
 for p in git('diff','--name-only',BASE,END,'--','blog').splitlines():
  if not re.fullmatch(r'blog/[^/]+/index.html',p) or 'buy-str-high-income-large-tax-bill' in p:continue
  a=subprocess.run(['git','show',BASE+':'+p],cwd=ROOT,text=True,capture_output=True)
  b=git('show',END+':'+p)
  if a.returncode:new.append(HOST+'/'+p.removesuffix('index.html'))
  elif body(a.stdout)!=body(b):existing.append(HOST+'/'+p.removesuffix('index.html'))
 assert len(existing)==103 and len(new)==8
 records={}
 def add(url,source,detail):
  if url in existing+new:records.setdefault(url,[]).append({'source':source,'record':detail})
 for p in sorted((ROOT/'_gen').glob('*.json')):
  if p.name.startswith('oct7-overnight') or p.name=='overnight-receipt-pairing.json':continue
  try:x=json.loads(p.read_text())
  except (ValueError,OSError):continue
  source=str(p.relative_to(ROOT))
  def visit(v):
   if isinstance(v,dict):
    u=v.get('url',v.get('inspectionUrl',''))
    for key in ['indexnow_status','submission','submission_record']:
     d=v.get(key)
     if u and isinstance(d,str) and re.search(r'HTTP\s*200',d,re.I) and (key=='indexnow_status' or 'indexnow' in d.lower()):add(u,source+'#'+key,d)
    idx=v.get('indexnow')
    if isinstance(idx,dict):
     status=idx.get('accepted_http_status',idx.get('http_status'))
     if status==200:
      urls=idx.get('canonical_urls',idx.get('urls',[]))
      for url in urls:add(url,source+'#indexnow',{'http_status':status,'live_key_verified':idx.get('live_key_verified'),'time_basis':idx.get('submitted_at_minute',idx.get('time_basis'))})
     elif u and isinstance(idx.get('status'),str) and re.search(r'HTTP\s*200',idx['status'],re.I):add(u,source+'#indexnow',idx)
    for w in v.values():visit(w)
   elif isinstance(v,list):
    for w in v:visit(w)
  visit(x)
 # Supplement only unambiguous saved editorial sections. These are narrative
 # release records, not an independently authenticated IndexNow server log.
 ledger=(ROOT/'_gen/investor-coverage-ledger.md').read_text()
 for section in re.split(r'(?m)^## ',ledger)[1:]:
  routes=set(re.findall(r'/blog/[a-z0-9-]+/',section))
  if len(routes)!=1 or not re.search(r'IndexNow.*HTTP\s*200',section,re.I):continue
  url=HOST+next(iter(routes));title=section.splitlines()[0]
  sentences=[s.strip() for s in re.split(r'(?<=[.!?])\s+',section) if 'indexnow' in s.lower() and re.search(r'HTTP\s*200',s,re.I)]
  if sentences:add(url,'_gen/investor-coverage-ledger.md#'+title,' '.join(sentences))
 # Pairing establishes a saved acceptance statement for a URL, not that the
 # most recent revision was submitted; compare dates/commits independently.
 output={'window':'October6 18:00 to October7 08:00 America/New_York','baseline_commit':BASE,'window_end_commit':END,'existing_changed':len(existing),'new_articles':len(new),'existing_urls_with_saved_acceptance_statement':sum(u in records for u in existing),'new_urls_with_saved_acceptance_statement':sum(u in records for u in new),'records':[{'url':u,'kind':'existing refresh' if u in existing else 'new guide','saved_acceptance_evidence':records.get(u,[]),'status':'saved acceptance statement paired' if u in records else 'no unambiguous receipt paired'} for u in sorted(existing+new)],'limits':'Historical saved narrative/structured acceptance evidence is not confirmed indexing or independent server logs. Missing evidence does not prove non-submission. Does not prove latest revision submission; dates/commits need individual reconciliation. No network calls or resubmissions.'}
 print(json.dumps(output,indent=2))

if __name__=='__main__':main()
