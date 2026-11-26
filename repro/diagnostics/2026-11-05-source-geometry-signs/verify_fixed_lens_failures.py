"""Two fixed independent-domain lens failures; not a coupled-word obstruction."""
from pathlib import Path
from fractions import Fraction as F
import sys,json,hashlib
from flint import arb,acb,ctx
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'experiments'))
import certify_mixed_reduced_disk_conditional_packets as c
ctx.prec=320;c.PI,c.II=arb.pi(),acb(0,1);c.base.PI,c.base.I=c.PI,c.II
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
p=ROOT/'repro/results/research-mixed-reduced-disk-conditional-packets.json'
r=json.loads(p.read_text());ih=sha(p)
bindings=dict(r['dependencies_sha256'])
bindings['notes/research_mixed_reduced_disk_conditional_packets.md']=r['proof_sha256']
bindings['experiments/certify_mixed_reduced_disk_conditional_packets.py']=r['script_sha256']
assert all(sha(ROOT/q)==h for q,h in bindings.items())
d=r['domains'][0];assert d['types']==[0,0,0]
checks={92:('abs(A)',F(51,50)),2312:('abs(1-A)',F(28,25))}
rows=[];pending=[([(F(0),F(1)),(F(0),F(1))],0)];cursor=0
while pending:
 box,depth=pending.pop();node=d['tree'][cursor];index=cursor;cursor+=1
 if node[0]=='S':
  assert node[1]==depth%2
  a,b=c.split(box,node[1]);pending.extend([(a,depth+1),(b,depth+1)]);continue
 if index not in checks:continue
 pp=c.parameter(box,(0,0));p0=c.parameter([(sum(v,F(0))/2,)*2 for v in box],(0,0))
 root=c.root_box(node[1],pp,p0,0);assert root
 s,t=root['point'];U=(-2*c.PI*c.II*s).exp();V=(-2*c.PI*c.II*t).exp();A=(1-U)*(1-V)/4
 name,floor=checks[index];value=abs(A if name=='abs(A)' else 1-A)
 assert value>c.ar(floor)
 rows.append(dict(types=[0,0,0],node=index,angle_midpoints=[str(sum(v,F(0))/2) for v in box],parameters=list(map(str,p0)),root=list(map(str,root['point'])),A=str(A),quantity=name,strict_lower=str(floor),outward_lower=str(value.lower().fmpq())))
assert cursor==len(d['tree']) and len(rows)==2
assert sha(p)==ih and all(sha(ROOT/q)==h for q,h in bindings.items())
result=dict(status='passed',precision_bits=320,cases=rows,input_sha256=ih,dependencies_sha256=bindings,script_sha256=sha(__file__),new_root_proposals=0,new_cover_cells=0,scope='Two existing certified midpoint roots on independent reduced type-three external disks violate geometric lens conditions. No coupled open-word source critical point, positive geometric period solution, or invariant is contradicted.')
Path(__file__).with_name('fixed-lens-failures.json').write_text(json.dumps(result,indent=2)+'\n')
print('PASS two fixed lens failures; no actual coupled-word assertion')
