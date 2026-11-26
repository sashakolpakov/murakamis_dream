from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import hashlib,json,urllib.request
root=Path('/private/tmp/murakamis_dream-publication/docs')
base='https://sashakolpakov.github.io/murakamis_dream/'
paths=['index.html','guide/results.html','guide/frontier.html','guide/geometry.html','guide/manuscript.html','guide/audits.html','figures.html',
'notes/actual_all_circle_local_message_volume.html','notes/actual_all_circle_vertexwise_geometry.html','notes/actual_main_meridian_filtered_characteristic.html','notes/exact_tree_messages_and_strip_bounds.html',
'assets/figures/tree-boundary-message.png','assets/figures/tree-boundary-message.svg','assets/figures/manuscript-leaf-pyramid.png','papers/conway-composition.pdf']
def check(name):
 with urllib.request.urlopen(base+name,timeout=30) as r:
  data=r.read();status=r.status
 local=hashlib.sha256((root/name).read_bytes()).hexdigest()
 live=hashlib.sha256(data).hexdigest()
 return {'path':name,'status':status,'local_sha256':local,'live_sha256':live,'match':live==local}
with ThreadPoolExecutor(max_workers=6) as pool: records=list(pool.map(check,paths))
out={'head':'d2e6c156f7af625eb09a3c9815869ad47b0872cc','pages_run':41278370121,'records':records,'failures':[r for r in records if not r['match']]}
Path('/private/tmp/md-local-message-live-deployment.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'checked':len(records),'matches':sum(r['match'] for r in records),'failures':out['failures']},indent=2))
if out['failures']:raise SystemExit(1)
