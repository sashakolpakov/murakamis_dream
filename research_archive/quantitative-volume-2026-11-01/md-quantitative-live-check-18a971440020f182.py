from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from urllib.request import Request,urlopen
import hashlib,json,subprocess
root=Path('/private/tmp/murakamis_dream-publication')
head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=root,text=True).strip()
run=json.loads(subprocess.check_output(['gh','run','view','41275478378','--repo','sashakolpakov/murakamis_dream','--json','headSha,status,conclusion'],text=True))
assert run['headSha']==head and run['conclusion']=='success',run
paths=['guide/results.html','guide/frontier.html','guide/audits.html',
 'notes/actual_all_circle_quantitative_volume.html',
 'notes/actual_all_circle_octahedral_decomposition.html',
 'notes/actual_all_circle_angular_octahedra.html',
 'notes/actual_all_circle_geometric_completion.html',
 'notes/actual_all_circle_preferred_cusp.html',
 'notes/actual_conway_pointed_quantum_a_volume.html',
 'assets/figures/octahedral-page-attachment.svg',
 'assets/figures/manuscript-leaf-pyramid.png','papers/conway-composition.pdf']
def check(path):
 expected=hashlib.sha256((root/'docs'/path).read_bytes()).hexdigest()
 url='https://sashakolpakov.github.io/murakamis_dream/'+path+'?revision='+head
 with urlopen(Request(url,headers={'Cache-Control':'no-cache'}),timeout=60) as response:
  data=response.read();status=response.status
 actual=hashlib.sha256(data).hexdigest()
 return {'path':path,'status':status,'local_sha256':expected,'remote_sha256':actual,'equal':actual==expected}
with ThreadPoolExecutor(max_workers=4) as pool:rows=list(pool.map(check,paths))
record={'commit':head,'pages_run':41275478378,'conclusion':'success','checks':rows}
Path('/private/tmp/md-quantitative-live-deployment.json').write_text(json.dumps(record,indent=2)+'\n')
assert all(x['equal'] for x in rows),rows
print(json.dumps({'commit':head,'pages_run':41275478378,'live_matches':len(rows),'failures':[]},indent=2))
