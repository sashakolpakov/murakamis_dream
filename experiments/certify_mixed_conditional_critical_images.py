#!/usr/bin/env python3
"""Full conditional-source certificate on actual cyclic critical images.

Uses the unchanged original affine block Newton test as a verified local
primitive. It covers only the distinguished boundaries of the smaller
circle/rectangle products. Every endpoint, full real-tail shape, and both
horizontal alias signs are checked outward, in both block orientations.
"""
import argparse,ast,hashlib,importlib.util,itertools,json,time,math,sys
from pathlib import Path
from fractions import Fraction as Q
from flint import arb,acb,ctx
ROOT=Path(__file__).resolve().parents[1];SOURCE=ROOT/'experiments/certify_mixed_cyclic_block_localization.py'
PROOF=ROOT/'notes/research_mixed_conditional_critical_images.md'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--precision',type=int,default=192);ap.add_argument('--max-visits',type=int,default=40000);ap.add_argument('--output',type=Path,default=ROOT/'repro/results/research-mixed-conditional-critical-images.json');args=ap.parse_args()
dependencies=['experiments/certify_mixed_cyclic_block_localization.py','notes/research_mixed_cyclic_critical_localization.md','notes/research_mixed_cyclic_critical_height_bounds.md','notes/research_mixed_conditional_image_contours.md','notes/research_mixed_three_canonical_conditional.md','notes/research_mixed_four_conditional_complex_neighbors.md','notes/exact_factorial_interpolation_and_complex_contours.md','repro/results/research-mixed-cyclic-block-localization.json','repro/results/research-mixed-cyclic-block-localization-replay.json','repro/results/research-mixed-cyclic-window-heights.json','repro/results/research-mixed-cyclic-window-heights-replay.json']
initial_hashes={p:sha(ROOT/p)for p in dependencies}
proof_hash=sha(PROOF)
for p in dependencies:
 if p.endswith('.json'):assert json.loads((ROOT/p).read_text())['status']=='passed',p
loc=json.loads((ROOT/'repro/results/research-mixed-cyclic-block-localization.json').read_text());assert loc['script_sha256']==sha(SOURCE) and loc['proof_sha256']==sha(ROOT/'notes/research_mixed_cyclic_critical_localization.md')
spec=importlib.util.spec_from_file_location('frozen',SOURCE);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);ctx.prec=args.precision;m.PI=arb.pi();ar=m.ar;I=m.I;PI=m.PI
T=ast.parse(SOURCE.read_text());fn=next(n for n in T.body if isinstance(n,ast.FunctionDef)and n.name=='certify')
class Capture(ast.NodeTransformer):
 def visit_Return(self,n):
  if isinstance(n.value,ast.Constant)and n.value.value is True:return ast.copy_location(ast.Return(ast.Call(ast.Name('locals',ast.Load()),[],[])),n)
  return n
fn=Capture().visit(fn);ast.fix_missing_locations(fn);ns=dict(m.__dict__)
PARTS=(0,0)
CORNERS=[acb(ar('27/100'),-ar('57/1000')),acb(ar('33/100'),-ar('57/1000')),acb(ar('33/100'),-ar('1/1000')),acb(ar('27/100'),-ar('1/1000'))]
def boundary_value(t,part,theta):
 if t==0:return acb(ar('7/20'),-ar('1/100'))+ar('83/1000')*(2*PI*I*theta).exp()
 return CORNERS[part]+theta*(CORNERS[(part+1)%4]-CORNERS[part])
def boundary_derivative(t,part,p):
 if t==0:return 2*PI*I*(p-acb(ar('7/20'),-ar('1/100')))
 return CORNERS[(part+1)%4]-CORNERS[part]
def arcs(lo,hi,ta,tb):return [boundary_value(t,PARTS[j],ar(lo[k]).union(ar(hi[k])))for j,(k,t)in enumerate([(0,ta),(2,tb)])]
ns['pars']=arcs;exec(compile(ast.Module(body=[fn],type_ignores=[]),str(SOURCE)+'[pilot]', 'exec'),ns);cert=ns['certify']
def decode(ad):
 box=[Q(0),Q(1),Q(0),Q(1)]
 for j,v in enumerate(ad):
  k=2*(j%2);mid=(box[k]+box[k+1])/2;box[k+1-int(v)]=mid
 return box

def g(z):return ((-2*PI*I*z).exp().polylog(2)-PI*PI/6)/(2*PI*I)
def gp(z):return (1-(-2*PI*I*z).exp()).log()
def ph(s,a,t,d):return g(s+a)+g(s+t)-d*g(s)+2*PI*I*a*s

def check(adr,eps,ta,tb):
 al,ah,bl,bh=decode(adr);w=cert((al,Q(0),bl,Q(0)),(ah,Q(0),bh,Q(0)),eps,ta,tb)
 if not w:return None,'block'
 pp=w['pp'];zz=w['zz'];p0=w['p0'];zbox=[zz[i]+w['dz'][i]+acb(arb(0,ar(w['rad'][i])),arb(0,ar(w['rad'][i])))for i in(0,1)]
 # Point Newton enclosure, independent of the finite output radii.
 rr=ar('1e-11');zp=[v+acb(arb(0,rr),arb(0,rr))for v in zz];f0,j0=m.evalf(zz,*p0,2+eps);_,jp=m.evalf(zp,*p0,2+eps)
 Y=w['yy'];err=max(abs(sum(Y[i][k]*f0[k]for k in(0,1)))for i in(0,1));con=max(sum(abs(acb(int(i==j))-sum(Y[i][k]*jp[k][j]for k in(0,1)))for j in(0,1))for i in(0,1))
 if not(err+con*rr<rr):return None,'point'
 off=PI*(PI*(zbox[0]+zbox[1])).cot()-PI*I
 J=[[off+PI*(PI*(zbox[i]+pp[i])).cot()-(2+eps)*PI*(PI*zbox[i]).cot()+(1+eps)*PI*I if i==j else off for j in(0,1)]for i in(0,1)]
 det=J[0][0]*J[1][1]-J[0][1]*J[1][0]
 E=[PI*(PI*(zbox[i]+pp[i])).cot()+PI*I for i in(0,1)]
 D=[[-J[1][1]*E[0]/det,J[0][1]*E[1]/det],[J[1][0]*E[0]/det,-J[0][0]*E[1]/det]]
 dt=[ar((ah-al)/2),ar((bh-bl)/2)];tangent=[boundary_derivative(t,PARTS[i],pp[i])for i,t in enumerate((ta,tb))]
 out=[]
 for side in(0,1):
  a=pp[side];s=zbox[side];t=zbox[1-side];a0=p0[side];s0=zp[side];t0=zp[1-side];d=2+eps
  selected=ph(s0,a0,t0,d)
  def lower(v,ga,gt):
   deriv=[gt*D[1-side][j]+(ga if j==side else 0)for j in(0,1)]
   return v.real-sum(abs((deriv[j]*tangent[j]).real)*dt[j]for j in(0,1))
  ga=gp(s+a)+2*PI*I*s;gt=gp(s+t)
  gaps=[]
  for cut in('3/20','49/100'):
   c=acb(ar(cut));gaps.append(lower(selected-ph(c,a0,t0,d),ga-gp(c+a)-2*PI*I*c,gt-gp(c+t)))
  for u in(0,1):
   for v in(0,1):gaps.append(lower(selected-g(a0)-g(t0)-2*PI*I*u*a0+2*PI*I*v*t0,ga-gp(a)-2*PI*I*u,gt-gp(t)+2*PI*I*v))
  if not all(x>ar('1/10000')for x in gaps):return None,('gap',side,[str(x)for x in gaps])
  # H'(s)<0 until w=-cot(pi s) reaches both quadratic vertices.
  qa=(2*PI*a.real).sin()/((2*PI*a.imag).cosh()-(2*PI*a.real).cos());qt=(2*PI*t.real).sin()/((2*PI*t.imag).cosh()-(2*PI*t.real).cos())
  wr=max(qa.upper(),qt.upper());wl=-1/(49*PI/100).tan();ca,sa=(PI*a).cos(),(PI*a).sin();ct,st=(PI*t).cos(),(PI*t).sin();fac=(2*PI*(t.imag-a.imag)).exp()/4**eps
  worst=arb(0)
  for j in range(12):
   ww=(wl+(wr-wl)*j/12).union(wl+(wr-wl)*(j+1)/12)
   val=fac*abs(ca-ww*sa)**2*abs(ct-ww*st)**2*(1+ww**2)**eps;worst=max(worst,val.upper())
  if not worst<1:return None,('shape',side,str(worst))
  alias=[]
  for sign in(-1,1):
   for jj in range(8):
    xx=ar(Q(3,20)+Q(34,100)*Q(jj,8)).union(ar(Q(3,20)+Q(34,100)*Q(jj+1,8)))
    cc=acb(xx,sign*ar('1/5'))
    bb=lower(selected-ph(cc,a0,t0,d),ga-gp(cc+a)-2*PI*I*cc,gt-gp(cc+t))+2*PI/5
    if not bb>ar('1/1000'):return None,('alias',side,sign,jj,str(bb))
    alias.append(bb)
  out.append({'gaps':gaps,'shape':worst,'alias':alias})
 return {'orientations':out,'root_centers':[[str(v.real),str(v.imag)]for v in w['z']],'affine_matrix':[[[str(v.real),str(v.imag)]for v in row]for row in w['D']],'affine_radii':[str(v)for v in w['rad']]},None

import itertools
fails=[];count=0;start=time.time();summ=[];allaccepted=[]
for eps,ta,tb in [(e,a,b)for e in(0,1)for a,b in((0,0),(0,1),(1,1))]:
 for pa,pb in itertools.product(range(1 if ta==0 else 4),range(1 if tb==0 else 4)):
  PARTS=(pa,pb);good=0;mn=1.;mf=0;ma=100.;accepted=[];witnesses=[];pending=[''.join(x)for x in itertools.product('01',repeat=4)]
  while pending:
   adr=pending.pop();ret,why=check(adr,eps,ta,tb);count+=1
   if ret:
    witness=ret;ret=ret['orientations'];witnesses.append({'address':adr,'root_centers':witness['root_centers'],'affine_matrix':witness['affine_matrix'],'affine_radii':witness['affine_radii']})
    good+=1;mn=min(mn,*[float(x.lower())for row in ret for x in row['gaps']]);mf=max(mf,*[float(row['shape'].upper())for row in ret]);ma=min(ma,*[float(x.lower())for row in ret for x in row['alias']]);accepted.append(adr)
   elif len(adr)<26:pending.extend([adr+'0',adr+'1'])
   else:
    print('UNRESOLVED',[eps,ta,tb],PARTS,adr,why,flush=True);raise RuntimeError('unresolved at fixed depth budget')
   if count%500==0:print('progress',count,'accepted',good,'pending',len(pending),'seconds',round(time.time()-start,1),flush=True)
   if count>args.max_visits:raise RuntimeError('explicit visit budget')
  row={'types':[eps,ta,tb],'parts':[pa,pb],'good':good,'min_gap':mn,'shape_upper':mf,'alias_gap':ma};summ.append(row);allaccepted.append({'types':[eps,ta,tb],'parts':[pa,pb],'addresses':accepted,'witnesses':witnesses});print(json.dumps(row),flush=True)
# Exact prefix-free binary coverage, independently of the analytic predicates.
for case in allaccepted:
 codes=set(case['addresses']);assert len(codes)==len(case['addresses'])
 assert sum((Q(1,2**len(v))for v in codes),Q(0))==1
 prefixes={a[:j]for a in codes for j in range(len(a))}
 assert not(codes&prefixes)
 for p in prefixes:assert all(p+b in codes or p+b in prefixes for b in'01')
assert len(allaccepted)==42
assert initial_hashes=={p:sha(ROOT/p)for p in dependencies}
assert proof_hash==sha(PROOF)
out={'status':'passed','scope':'Canonical complete conditional packets on correlated actual-critical image domains; not the remaining outer integral.','precision_bits':args.precision,'visited_cells':count,'accepted_cells':sum(len(c['addresses'])for c in allaccepted),'boundary_pieces':42,'conditional_orientations_per_piece':2,'real_endpoint_gap':'1/10000','horizontal_alias_gap':'1/1000','right_tail_shape_upper':'1','middle_rectangle':['3/20','49/100','-1/5','1/5'],'point_newton_radius':'1e-11','summaries':summ,'cases':allaccepted,'elapsed_seconds':time.time()-start,'script_sha256':sha(__file__),'proof_sha256':proof_hash,'dependencies':initial_hashes,'summary_float_scope':'The decimal extrema in summaries are diagnostics only; acceptance uses the stated strict Arb thresholds.'}
args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(out,indent=2)+'\n')
print('PASS',out['boundary_pieces'],'boundary pieces,',out['accepted_cells'],'accepted cells,',count,'visited',time.time()-start,flush=True)
