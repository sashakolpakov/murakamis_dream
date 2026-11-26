from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from urllib.request import Request,urlopen
import hashlib,json,subprocess
root=Path('/private/tmp/murakamis_dream-publication')
head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=root,text=True).strip()
base='https://sashakolpakov.github.io/murakamis_dream/'
paths=['guide/methods.html','guide/notation.html','guide/frontier.html',
       'assets/figures/methods-proof-map.svg','papers/conway-composition.pdf',
       'notes/actual_morse_geometric_contribution.html','sphinx/mathematics.html']
def check(path):
 req=Request(base+path+'?revision='+head,headers={'Cache-Control':'no-cache'})
 with urlopen(req,timeout=40) as r: data=r.read();status=r.status
 a=hashlib.sha256(data).hexdigest();b=hashlib.sha256((root/'docs'/path).read_bytes()).hexdigest()
 return {'path':path,'http_status':status,'sha256':a,'local_sha256':b,'matches':a==b}
with ThreadPoolExecutor(max_workers=4) as pool:rows=list(pool.map(check,paths))
runs=json.loads(subprocess.check_output(['gh','run','list','--repo','sashakolpakov/murakamis_dream','--limit','3','--json','databaseId,headSha,status,conclusion'],text=True))
run=next(r for r in runs if r['headSha']==head)
report={'commit':head,'pages_run':run['databaseId'],'pages_conclusion':run['conclusion'],'files':rows,'status':'success' if all(r['matches'] for r in rows) and run['conclusion']=='success' else 'pending'}
Path('/private/tmp/md-methods-live-check.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
raise SystemExit(0 if report['status']=='success' else 1)
