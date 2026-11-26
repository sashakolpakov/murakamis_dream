from pathlib import Path
from fractions import Fraction as F
import sys,json,time,hashlib
from flint import arb,acb,ctx
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT/'experiments'))
import certify_mixed_reduced_disk_conditional_packets as c
ctx.prec=320;c.PI,c.II=arb.pi(),acb(0,1);c.base.PI,c.base.I=c.PI,c.II
source_path=ROOT/'repro/results/research-mixed-reduced-disk-conditional-packets.json'
r=json.loads(source_path.read_text())
sha=lambda path:hashlib.sha256(Path(path).read_bytes()).hexdigest()
bindings=dict(r['dependencies_sha256'])
bindings[str(source_path.relative_to(ROOT))]=sha(source_path)
bindings['notes/research_mixed_reduced_disk_conditional_packets.md']=r['proof_sha256']
bindings['experiments/certify_mixed_reduced_disk_conditional_packets.py']=r['script_sha256']
assert all(sha(ROOT/p)==h for p,h in bindings.items())
rows=[]
def quantities(s,t,a,b,eps):
 U,V,L,R=[(-2*c.PI*c.II*z).exp() for z in (s,t,a,b)]
 A=(1-U)*(1-V)/4 if eps==0 else (2-U-V)/4
 B=-((1-L)**2*(1-U))/(4*L*(1-U*L));C=-((1-R)**2*(1-V))/(4*R*(1-V*R))
 q=[1/(c.PI*s).tan()+1/(c.PI*a).tan()-c.II,1/(c.PI*t).tan()+1/(c.PI*b).tan()-c.II]
 out=dict(A_im=A.imag,A_re=A.real,A_unit=1-abs(A),A_lens=1-abs(1-A),B_im=B.imag,C_im=C.imag,q_re=min(x.real.lower() for x in q),q_down=min((-x.imag).lower() for x in q))
 if A.imag>0 and B.imag>0 and C.imag>0:
  Z=(1/A-1).sqrt();ZB=(1/B-1).sqrt();ZC=(1/C-1).sqrt()
  out['cell']=min((q[0].real-(Z.real**2+ZB.real**2).sqrt()).lower(),(q[1].real-(Z.real**2+ZC.real**2).sqrt()).lower())
  tau=(2*A-1).acos();rl=(Z*B.sqrt()).asinh();rr=(Z*C.sqrt()).asinh()
  out['period_error']=abs(rl+rr-c.II*(3+eps)*tau/2+c.PI*c.II)
 return out
for d in r['domains']:
 eps,ta,tb=d['types'];pending=[([(F(0),F(1)),(F(0),F(1))],0)];cursor=0
 result=dict(types=d['types'],whole={},point={})
 while pending:
  box,depth=pending.pop();node=d['tree'][cursor];cursor+=1
  if node[0]=='S':
   lo,hi=c.split(box,node[1]);pending.extend([(lo,depth+1),(hi,depth+1)]);continue
  pp=c.parameter(box,(ta,tb));p0=c.parameter([(sum(x,F(0))/2,)*2 for x in box],(ta,tb));root=c.root_box(node[1],pp,p0,eps);assert root
  for mode,z,p in [('whole',root['root'],pp),('point',root['point'],p0)]:
   vals=quantities(*z,*p,eps)
   for key,value in vals.items():
    item=result[mode].setdefault(key,dict(minimum=None,maximum=None,failures=0,count=0,worst_node=None))
    if not value.is_finite():item['failures']+=1;continue
    lower=float(value.lower());upper=float(value.upper());item['count']+=1
    if item['minimum'] is None or lower<item['minimum']:item['minimum']=lower;item['worst_node']=cursor-1
    if item['maximum'] is None or upper>item['maximum']:item['maximum']=upper
    if (key=='period_error' and not value<c.PI/2) or (key!='period_error' and not value>0):item['failures']+=1
 rows.append(result);print(json.dumps(result),flush=True)
assert all(sha(ROOT/p)==h for p,h in bindings.items())
Path(__file__).with_name('result.json').write_text(json.dumps(dict(scope='Bounded extraction diagnostic on fixed complete reduced-disk witnesses, not a new theorem or cover',domains=rows,dependencies_sha256=bindings,script_sha256=sha(__file__)),indent=2)+'\n')
