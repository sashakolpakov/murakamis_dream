from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
import hashlib, json, urllib.request

root=Path('/private/tmp/murakamis_dream-publication/docs')
head=__import__('subprocess').check_output(['git','rev-parse','HEAD'],cwd=root.parent,text=True).strip()
paths=[
'index.html','guide/results.html','guide/frontier.html','guide/audits.html','figures.html',
'notes/actual_main_meridian_trivalent_component_bound.html','notes/actual_main_meridian_trivalent_filled_volume.html',
'notes/actual_main_meridian_grouped_wire_packet.html','notes/actual_main_meridian_preferred_cusp.html',
'notes/actual_main_meridian_filled_volume.html','assets/figures/trivalent-bare-components.svg',
'assets/figures/manuscript-leaf-pyramid.png','papers/conway-composition.pdf',
]

def check(path):
    expected=hashlib.sha256((root/path).read_bytes()).hexdigest()
    request=urllib.request.Request('https://sashakolpakov.github.io/murakamis_dream/'+path+'?revision='+head,headers={'User-Agent':'Publication verification'})
    with urllib.request.urlopen(request,timeout=30) as response:
        live=hashlib.sha256(response.read()).hexdigest()
    return {'path':path,'expected':expected,'live':live,'equal':live==expected}
with ThreadPoolExecutor(max_workers=6) as pool:
    checks=list(pool.map(check,paths))
record={'checked_utc':datetime.now(timezone.utc).isoformat(),'commit':head,'pages_run':json.loads(Path('/private/tmp/md-trivalent-pages-run.json').read_text())['databaseId'],'checks':checks}
Path('/private/tmp/md-trivalent-live-deployment.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'checked':len(checks),'matching':sum(r['equal'] for r in checks),'mismatches':[r['path'] for r in checks if not r['equal']]},indent=2))
assert all(r['equal'] for r in checks)
