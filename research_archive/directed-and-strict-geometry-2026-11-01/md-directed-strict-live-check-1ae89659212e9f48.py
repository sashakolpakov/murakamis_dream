from pathlib import Path
from urllib.request import Request,urlopen
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime,timezone
import argparse,hashlib,json
parser=argparse.ArgumentParser();parser.add_argument('--run',type=int,required=True);args=parser.parse_args()
pub=Path('/private/tmp/murakamis_dream-publication')
base='https://sashakolpakov.github.io/murakamis_dream/'
paths=['index.html','guide/results.html','guide/frontier.html','guide/manuscript.html','guide/mechanism.html','guide/geometry.html','guide/audits.html','notes/actual_all_circle_directed_volume.html','notes/actual_strict_tree_geometric_characteristic.html','notes/actual_all_circle_geometric_characteristic.html','notes/actual_main_meridian_filtered_characteristic.html','notes/actual_conway_pointed_quantum_a_volume.html','papers/conway-composition.pdf','assets/figures/directed-tree-volume.svg','assets/figures/zero-circle-junction.svg','assets/figures/manuscript-leaf-pyramid.png','sphinx/mathematics.html']
def one(rel):
 req=Request(base+rel,headers={'Cache-Control':'no-cache','User-Agent':'murakamis-dream-publication-check'})
 with urlopen(req,timeout=45) as response:data=response.read();status=response.status
 sha=lambda b:hashlib.sha256(b).hexdigest()
 actual=sha(data);expected=sha((pub/'docs'/rel).read_bytes())
 return {'path':rel,'status':status,'actual_sha256':actual,'expected_sha256':expected,'matches':actual==expected}
with ThreadPoolExecutor(max_workers=6) as pool:rows=list(pool.map(one,paths))
report={'checked_utc':datetime.now(timezone.utc).isoformat(),'base':base,'commit':'9e289a77c9c238341e053e76fe708056820203e2','pages_run':args.run,'checks':rows,'failures':[r for r in rows if not r['matches']]}
Path('/private/tmp/md-directed-strict-live-validation.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'checks':len(rows),'failures':report['failures']},indent=2))
raise SystemExit(bool(report['failures']))
