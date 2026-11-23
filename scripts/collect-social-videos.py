import urllib.request,json,re,time,concurrent.futures
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def get(url,data=None):
 req=urllib.request.Request(url,data=json.dumps(data).encode() if data else None,headers={'User-Agent':'Mozilla/5.0','Content-Type':'application/json'})
 return urllib.request.urlopen(req,timeout=35).read().decode()
def walk(x):
 if isinstance(x,dict):
  yield x
  for v in x.values():yield from walk(v)
 elif isinstance(x,list):
  for v in x:yield from walk(v)
def channel(handle,tab):
 url=f'https://www.youtube.com/@{handle}/{tab}';s=get(url);m=re.search(r'var ytInitialData = (.*?);</script>',s)
 if not m:return [],{'url':url,'error':'No initial data'}
 d=json.loads(m.group(1));rows={};seen=set();pages=0
 while True:
  pages+=1
  for x in walk(d):
   if 'lockupViewModel' in x:
    v=x['lockupViewModel'];i=v.get('contentId','');t=v.get('metadata',{}).get('lockupMetadataViewModel',{}).get('title',{}).get('content','')
    if len(i)==11 and t: rows[i]={'id':i,'title':t,'platform':'youtube','channel':handle,'tab':tab,'url':'https://www.youtube.com/watch?v='+i}
   if 'videoRenderer' in x:
    v=x['videoRenderer'];i=v['videoId'];t=''.join(z.get('text','') for z in v.get('title',{}).get('runs',[]));rows[i]={'id':i,'title':t,'platform':'youtube','channel':handle,'tab':tab,'url':'https://www.youtube.com/watch?v='+i}
   if 'shortsLockupViewModel' in x:
    v=x['shortsLockupViewModel'];i=v.get('onTap',{}).get('innertubeCommand',{}).get('reelWatchEndpoint',{}).get('videoId');t=v.get('overlayMetadata',{}).get('primaryText',{}).get('content','')
    if i:rows[i]={'id':i,'title':t,'platform':'youtube','channel':handle,'tab':tab,'url':'https://www.youtube.com/shorts/'+i}
  cs=[x['continuationItemRenderer'].get('continuationEndpoint',{}).get('continuationCommand',{}).get('token') for x in walk(d) if 'continuationItemRenderer' in x];cs=[v for v in cs if v and v not in seen]
  if not cs:break
  token=cs[0];seen.add(token)
  try:d=json.loads(get('https://www.youtube.com/youtubei/v1/browse',{'context':{'client':{'clientName':'WEB','clientVersion':'2.20261119.07.00'}},'continuation':token}))
  except Exception as e:return list(rows.values()),{'url':url,'pages':pages,'error':str(e),'count':len(rows)}
  if pages>100:raise RuntimeError('Pagination bound exceeded')
 return list(rows.values()),{'url':url,'pages':pages,'exhausted':True,'count':len(rows)}
allrows={};logs=[]
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
 fs=[pool.submit(channel,h,t) for h in ['mybnbaccelerator','mybnbacceleratortestimonials'] for t in ['videos','shorts','streams']]
 for f in concurrent.futures.as_completed(fs):
  try:
   rows,log=f.result();logs.append(log)
   for r in rows:allrows[r['id']]=r
   print(log,flush=True)
  except Exception as e:logs.append({'error':str(e)});print(str(e),flush=True)
out={'retrievedAt':__import__('datetime').datetime.now(__import__('datetime').timezone.utc).isoformat(),'channels':logs,'videos':list(allrows.values())}
(ROOT/'_gen/social-video-channel-refresh.json').write_text(json.dumps(out,indent=2))
print('TOTAL',len(allrows),flush=True)
