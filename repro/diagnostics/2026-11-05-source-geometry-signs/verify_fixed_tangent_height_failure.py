"""One saved independent-domain root defeats the uniform tangent-height shortcut."""
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
pending=[([(F(0),F(1)),(F(0),F(1))],0)];cursor=0;fixed=None
while pending:
 box,depth=pending.pop();node=d['tree'][cursor];index=cursor;cursor+=1
 if node[0]=='S':
  assert node[1]==depth%2
  a,b=c.split(box,node[1]);pending.extend([(a,depth+1),(b,depth+1)]);continue
 if index!=2218:continue
 angles=[sum(v,F(0))/2 for v in box];assert angles==[F(9,64),F(9,64)]
 pp=c.parameter(box,(0,0));p0=c.parameter([(v,v) for v in angles],(0,0))
 root=c.root_box(node[1],pp,p0,0);assert root
 s,t=root['point'];U=(-2*c.PI*c.II*s).exp();V=(-2*c.PI*c.II*t).exp();A=(1-U)*(1-V)/4
 a,b=A.real,A.imag;polynomial=4*a*(a*a+b*b)-b*b
 assert a>0 and b>0 and polynomial < -c.ar('1/100')
 fixed=dict(types=[0,0,0],node=index,angle_midpoints=list(map(str,angles)),parameters=list(map(str,p0)),root=list(map(str,root['point'])),A=str(A),polynomial='4 Re(A)|A|^2 - Im(A)^2',outward_value=str(polynomial),outward_upper=str(polynomial.upper().fmpq()),strict_upper='-1/100')
assert cursor==len(d['tree']) and fixed is not None
assert sha(p)==ih and all(sha(ROOT/q)==h for q,h in bindings.items())
result=dict(status='passed',precision_bits=320,fixed_case=fixed,input_sha256=ih,dependencies_sha256=bindings,script_sha256=sha(__file__),new_root_proposals=0,new_cover_cells=0,scope='Only the independent type3/type3,type3 reduced-disk map: the inferred tangent cannot have imaginary part strictly between minus one and zero at this saved midpoint. This is not an actual coupled open-word or positive unit-geometry counterexample.')
Path(__file__).with_name('fixed-tangent-height-failure.json').write_text(json.dumps(result,indent=2)+'\n')
print('PASS fixed tangent-height shortcut obstruction; no coupled-word claim')
