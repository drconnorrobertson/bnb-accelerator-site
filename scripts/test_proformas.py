from copy import deepcopy
import json,re
from build_proformas import validate,calculate,render,ROOT
x={'publication_status':'published','slug':'synthetic-fixture','title':'Synthetic fixture only','market':'Test market','address':None,'address_public':False,'verdict':'bad','verdict_reason':'Negative downside cash flow','evidence_type':'projected','period':'Synthetic first year','reviewed_on':'2026-10-08','purchase_price':500000,'annual_revenue':100000,'annual_operating_costs':[{'label':'Operating costs','amount':45000}],'annual_debt_service':30000,'cash_required':[{'label':'Cash including reserve','amount':250000}],'downside_annual_revenue':60000,'downside_annual_operating_costs':[{'label':'Downside costs','amount':40000}],'assumptions':['Synthetic data only'],'strengths':[],'risks':['Revenue decline'],'missing_evidence':['Property documents'],'sources':[{'label':'Synthetic source for test','url':'https://example.com/'}],'editorial_review_complete':True}
validate(x);c=calculate(x);assert c['net']==25000 and c['down']==-10000 and c['coc']==10
s=render(x);assert '$-10,000' in s and 'Pass at these assumptions' in s and 'Projected' in s
for block in re.findall(r'<script type="application/ld\+json">(.*?)</script>',s,re.S):json.loads(block)
for key,value in [('annual_revenue',None),('annual_debt_service',-1),('editorial_review_complete',False),('slug','../private'),('reviewed_on','2099-01-01')]:
 bad=deepcopy(x);bad[key]=value
 try:validate(bad)
 except (ValueError,TypeError):pass
 else:raise AssertionError(key+' accepted invalid value')
bad=deepcopy(x);bad['address']='PRIVATE ADDRESS'
try:validate(bad)
except ValueError:pass
else:raise AssertionError('private address allowed')
z=deepcopy(x);z['cash_required'][0]['amount']=0;assert calculate(z)['coc'] is None
assert not (ROOT/'proformas/synthetic-fixture/index.html').exists()
assert not (ROOT/'public/_gen/proformas/template.json').exists()
print('PASS: financial math, negative downside, zero denominator, missing inputs, private address, draft isolation, JSON-LD')
# Exercise publication, draft exclusion and withdrawal in an isolated directory.
import tempfile
from pathlib import Path
import build_proformas as builder
with tempfile.TemporaryDirectory() as temp:
 root=Path(temp);(root/'_gen/proformas').mkdir(parents=True)
 (root/'sitemap-proof.xml').write_text('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"></urlset>')
 fixture=root/'_gen/proformas/deal.json';fixture.write_text(json.dumps(x))
 builder.ROOT=root;builder.build()
 assert (root/'proformas/synthetic-fixture/index.html').exists()
 assert '/proformas/synthetic-fixture/' in (root/'sitemap-proof.xml').read_text()
 x['publication_status']='draft';fixture.write_text(json.dumps(x));builder.build()
 assert not (root/'proformas/synthetic-fixture/index.html').exists()
 assert '/proformas/synthetic-fixture/' not in (root/'sitemap-proof.xml').read_text()
 builder.ROOT=ROOT
print('PASS: approved publication, crawlable directory/sitemap, draft withdrawal, isolated fixture')
