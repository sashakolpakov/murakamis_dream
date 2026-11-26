#!/usr/bin/env python3
"""Independent sine-log/rational-exponential replay of left-taper Hessians."""
import argparse,hashlib,itertools,json,time
from fractions import Fraction as R
from pathlib import Path
import sympy as sp
from flint import arb,acb,ctx
ROOT=Path(__file__).resolve().parents[1]
PROOF=ROOT/'notes/research_mixed_left_taper_tilted_hessian.md'
AUTHOR=ROOT/'experiments/certify_mixed_left_taper_tilted_hessian.py'
INPUT=ROOT/'repro/results/research-mixed-left-taper-tilted-hessian.json'
RECTS={0:list(map(R,['.15','.45','-.03','.02'])),1:list(map(R,['.15','.45','-.057','0'])),2:list(map(R,['.24','.45','-.057','-.02']))}
P=arb.pi();I=acb(0,1)
def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def ar(x):
 x=R(x);return arb(x.numerator)/x.denominator
def cover(addresses):
 tree={}
 for address in addresses:
  node=tree
  for bit in address:
   assert bit in'01'and'leaf'not in node
   node=node.setdefault(bit,{})
  assert not node;node['leaf']=1
 def visit(node):
  if 'leaf'in node:
   assert node=={'leaf':1};return 1
  assert set(node)=={'0','1'}
  return visit(node['0'])+visit(node['1'])
 assert visit(tree)==len(addresses)
def decode(address):
 lo=[R(0),R(0)];hi=[R(1),R(1)]
 for j,bit in enumerate(address):
  k=j%2;mid=(lo[k]+hi[k])/2
  if bit=='0':hi[k]=mid
  else:lo[k]=mid
 return lo,hi
def edge(kind,face,lo,hi):
 xl,xh,yl,yh=RECTS[kind]
 cc=[acb(ar(xl),ar(yl)),acb(ar(xh),ar(yl)),acb(ar(xh),ar(yh)),acb(ar(xl),ar(yh))]
 return cc[face]+(cc[(face+1)%4]-cc[face])*ar(lo).union(ar(hi))
def params(eta,faces,address):
 lo,hi=decode(address)
 vals=[edge(k,f,lo[j],hi[j])for j,(k,f)in enumerate(zip((eta,2),faces))]
 mids=[edge(k,f,(lo[j]+hi[j])/2,(lo[j]+hi[j])/2)for j,(k,f)in enumerate(zip((eta,2),faces))]
 return vals,mids
def gp(z):
 assert 0<z.real<1
 return (2*(P*z).sin()).log()+P*I*(1-2*z)/2
def gpp(z):
 E=(-2*P*I*z).exp()
 return 2*P*I*E/(1-E)
def jacdiff(base,delta):
 E=(-2*P*I*base).exp();Z=(-2*P*I*delta).exp()
 return 2*P*I*E*(Z-1)/((1-E*Z)*(1-E))
def root_box(a,b,a0,b0,witness,origin=None):
 z0=acb(ar(witness['center'][0]),ar(witness['center'][1]))
 D=[acb(ar(v[0]),ar(v[1]))for v in witness['derivatives']]
 if origin is not None:
  aa,bb=origin;z=z0+D[0]*(a0-aa)+D[1]*(b0-bb)
  z0=acb(z.real.mid(),z.imag.mid())
  for _ in range(4):
   f=gp(z0+a0)+gp(z0+b0)-3*gp(z0)+2*P*I*a0
   h=gpp(z0+a0)+gpp(z0+b0)-3*gpp(z0)
   z=z0-f/h;z0=acb(z.real.mid(),z.imag.mid())
 h0=gpp(z0+a0)+gpp(z0+b0)-3*gpp(z0);Y=1/h0
 f0=gp(z0+a0)+gp(z0+b0)-3*gp(z0)+2*P*I*a0
 ext=[gpp(z0+a0)+2*P*I,gpp(z0+b0)];dp=[a-a0,b-b0]
 dz=sum((D[j]*dp[j]for j in(0,1)),acb(0))
 linear=f0+sum(((h0*D[j]+ext[j])*dp[j]for j in(0,1)),acb(0))
 def remainder(base,delta):
  z=base+acb(arb(0,abs(delta.real).upper()),arb(0,abs(delta.imag).upper()))
  if not 0<z.real<1:return arb.pos_inf()
  E=(-2*P*I*z).exp()
  return 2*P**2*abs(E/(1-E)**2)*abs(delta)**2
 error=abs(Y)*(abs(linear)+remainder(z0+a0,dz+dp[0])+remainder(z0+b0,dz+dp[1])+3*remainder(z0,dz))
 if not error.is_finite():return None
 radius=ar(witness['radius'])if origin is None else max(ar('1e-12').upper(),(2*error).upper())
 if not radius<ar('1/20'):return None
 delta=dz+acb(arb(0,radius),arb(0,radius));z=z0+delta
 if not ar('.19')<z.real<ar('.47')or not -ar('.22')<z.imag<ar('.16'):return None
 E=1-Y*h0-Y*(jacdiff(z0+a0,delta+dp[0])+jacdiff(z0+b0,delta+dp[1])-3*jacdiff(z0,delta))
 if not error+abs(E)*radius<radius:return None
 return z
def test(eta,faces,address,witness,original):
 (a,b),(a0,b0)=params(eta,faces,address)
 origin=None if address==original else params(eta,faces,original)[1]
 s=root_box(a,b,a0,b0,witness,origin)
 if s is None:return False
 p,q=gpp(s+a),gpp(s+b)
 Hss=p+q-3*gpp(s);Hsa=p+2*P*I;Hsb=q
 aa=-(p-ar(1+R(eta,2))*gpp(a)-Hsa**2/Hss)
 ab=Hsa*Hsb/Hss
 bb=-(q-ar('3/2')*gpp(b)-Hsb**2/Hss)
 if not aa.real>0:return False
 for rho in ([R(-13,100),R(13,100)]if eta==0 else[R(-13,50),R(0)]):
  rr=ar(rho)
  A=(1-rr**2)*aa.real-2*rr*aa.imag-ar('1/2')
  B=ab.real-rr*ab.imag
  C=bb.real-ar('1/2')
  if not A>0 or not A*C-B**2>0:return False
 return True
def exact():
 E,Z=sp.symbols('E Z')
 assert sp.cancel(E*Z/(1-E*Z)-E/(1-E)-E*(Z-1)/((1-E*Z)*(1-E)))==0
 rho,a,b,c,d=sp.symbols('rho a b c d',real=True)
 assert sp.expand(sp.re((1+sp.I*rho)**2*(a+sp.I*b))-(1-rho*rho)*a+2*rho*b)==0
 assert sp.expand(sp.re((1+sp.I*rho)*(c+sp.I*d))-c+rho*d)==0
 assert sp.diff((1-rho*rho)*a-2*rho*b,rho,2)==-2*a
 l,x,r3,r4=R('.22'),R('.15'),R('.30'),R('.27')
 assert x*x-2*r4*x+l*l<0
 assert R('.03')*(1-(x/l)**2)/(r3-x)<R('.13')
 assert R('.057')*(1-(x/l)**2)/(r4-x)<R('.26')
 assert (r4-l)**2/4==R(1,1600)
 assert R(1,1600)-R(1,8000)==R(1,2000)
 return 4,5
def main():
 global P
 parser=argparse.ArgumentParser(description=__doc__)
 parser.add_argument('--precision',type=int,default=320)
 parser.add_argument('--output',type=Path,default=ROOT/'repro/results/research-mixed-left-taper-tilted-hessian-replay.json')
 args=parser.parse_args();assert args.precision>=192;ctx.prec=args.precision;P=arb.pi()
 raw=INPUT.read_bytes();data=json.loads(raw);assert data['status']=='passed'
 assert data['script_sha256']==sha(AUTHOR)and data['proof_sha256']==sha(PROOF)
 assert data['rectangles']=={str(k):[str(v)for v in vs]for k,vs in RECTS.items()}
 assert data['tilt_intervals']=={'0':['-13/100','13/100'],'1':['-13/50','0']}
 assert data['strict_hessian_lower']=='1/2'and data['action_gap']=='1/1600'and data['finite_source_gap']=='1/2000'
 deps=dict(data['dependencies']);deps[str(PROOF.relative_to(ROOT))]=sha(PROOF);deps[str(AUTHOR.relative_to(ROOT))]=sha(AUTHOR)
 for path,digest in list(deps.items()):
  assert sha(ROOT/path)==digest
  if path.endswith('.json'):
   rr=json.loads((ROOT/path).read_text());assert rr['status']=='passed'
   for p,h in rr.get('dependencies',rr.get('dependencies_sha256',{})).items():
    assert sha(ROOT/p)==h;deps[p]=h
 for stem in ('asymmetric_wide_conditional_packets','transition_conditional_rectangles'):
  rr=json.loads((ROOT/('repro/results/research-mixed-'+stem.replace('_','-')+'.json')).read_text())
  assert rr['script_sha256']==sha(ROOT/('experiments/certify_mixed_'+stem+'.py'))
  assert rr['proof_sha256']==sha(ROOT/('notes/research_mixed_'+stem+'.md'))
 cases=data['cases'];assert len(cases)==32
 assert {(c['eta'],*c['faces'])for c in cases}==set(itertools.product((0,1),range(4),range(4)))
 start=time.time();selfhash=sha(__file__);ni,nr=exact();results=[];total=0;refinements=0
 for case in cases:
  addresses=case['addresses'];cover(addresses)
  witnesses={w['address']:w for w in case['witnesses']}
  assert len(witnesses)==len(addresses)and set(witnesses)==set(addresses)
  accepted=[];refined=0
  for original in addresses:
   todo=[original]
   while todo:
    ad=todo.pop()
    try:ok=test(case['eta'],case['faces'],ad,witnesses[original],original)
    except(ValueError,ZeroDivisionError,AssertionError):ok=False
    if ok:accepted.append(ad)
    else:
     assert len(ad)<len(original)+14,(case['eta'],case['faces'],original,ad)
     refined+=1;todo.extend([ad+'1',ad+'0'])
  cover(accepted);total+=len(accepted);refinements+=refined
  row={'eta':case['eta'],'faces':case['faces'],'original_cells':len(addresses),'replay_cells':len(accepted),'refinements':refined}
  results.append(row);print(json.dumps(row),flush=True)
 assert sum(r['original_cells']for r in results)==data['accepted_cells']
 assert raw==INPUT.read_bytes()and selfhash==sha(__file__)
 assert all(sha(ROOT/p)==h for p,h in deps.items())
 output={'status':'passed','precision_bits':args.precision,'boundary_products':32,'original_cells':data['accepted_cells'],
         'replay_cells':total,'refinements':refinements,'cases':results,
         'exact_identity_count':ni,'exact_rational_checks':nr,'elapsed_seconds':time.time()-start,
         'input_sha256':hashlib.sha256(raw).hexdigest(),'proof_sha256':sha(PROOF),'script_sha256':selfhash,'dependencies':deps,
         'analytic_independence':'Sine logarithms, rational-exponential Hessians and Jacobian differences, explicit real tilted matrices, exact complete-tree coverage; stored witnesses only, no author import/root proposal.',
         'scope':data['scope']}
 args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(output,indent=2)+'\n')
 print('PASS',total,'cells,',refinements,'refinements',flush=True)
if __name__=='__main__':main()
