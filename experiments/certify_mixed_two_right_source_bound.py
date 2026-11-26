#!/usr/bin/env python3
"""Outward full-source supporting-plane bound on two right outer half-periods.

All original rows and Fourier forcing are retained by the cited analytic
reduction. This checker verifies its exact corner constants and the full
three-window reference comparison, not a global mixed-cycle lower bound.
"""
from pathlib import Path
import argparse,ast,hashlib,importlib.util,json,itertools,time
import sympy as sy
from fractions import Fraction as R
from flint import arb,acb,acb_mat,ctx
ROOT=Path(__file__).resolve().parents[1]
PROOF=ROOT/'notes/research_mixed_two_right_source_bound.md'
SRC=ROOT/'experiments/certify_mixed_cyclic_window_heights.py'
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--precision',type=int,default=256)
parser.add_argument('--max-visits',type=int,default=50000)
parser.add_argument('--output',type=Path,default=ROOT/'repro/results/research-mixed-two-right-source-bound.json')
args=parser.parse_args();assert args.precision>=160;ctx.prec=args.precision
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
DEPS=[
 'notes/research_mixed_right_half_source_reduction.md',
 'experiments/check_mixed_right_half_source_reduction.py',
 'repro/results/research-mixed-right-half-source-reduction.json',
 'notes/research_mixed_geometric_support_slopes.md',
 'experiments/certify_mixed_geometric_support_slopes.py',
 'experiments/replay_mixed_geometric_support_slopes.py',
 'repro/results/research-mixed-geometric-support-slopes.json',
 'repro/results/research-mixed-geometric-support-slopes-replay.json',
 'experiments/certify_mixed_cyclic_window_heights.py',
 'notes/research_mixed_cyclic_critical_height_bounds.md',
 'notes/research_mixed_fourier_weight_continuation.md',
 'notes/research_mixed_boundary_strip_bounds.md',
 'notes/research_mixed_conditional_torus_composition.md',
]
hashes={p:sha(ROOT/p)for p in DEPS};proof_hash=sha(PROOF);script_hash=sha(__file__)
for name,script,proof in[
 ('research-mixed-right-half-source-reduction','check_mixed_right_half_source_reduction.py','research_mixed_right_half_source_reduction.md'),
 ('research-mixed-geometric-support-slopes','certify_mixed_geometric_support_slopes.py','research_mixed_geometric_support_slopes.md')]:
 rec=json.loads((ROOT/f'repro/results/{name}.json').read_text());assert rec['status']=='passed'
 assert rec['script_sha256']==sha(ROOT/'experiments'/script)
 assert rec['proof_sha256']==sha(ROOT/'notes'/proof)
 for key in('dependencies','dependencies_sha256'):
  for dep,dig in rec.get(key,{}).items():assert sha(ROOT/dep)==dig,(name,dep)
review=json.loads((ROOT/'repro/results/research-mixed-geometric-support-slopes-replay.json').read_text())
assert review['status']=='passed'
assert review['script_sha256']==sha(ROOT/'experiments/replay_mixed_geometric_support_slopes.py')
assert review['proof_sha256']==sha(ROOT/'notes/research_mixed_geometric_support_slopes.md')
assert review['input_sha256']==sha(ROOT/'repro/results/research-mixed-geometric-support-slopes.json')
for dep,dig in review['dependencies'].items():assert sha(ROOT/dep)==dig,dep
sp=importlib.util.spec_from_file_location('win',SRC);m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);m.PI=arb.pi();P=m.PI;I=acb(0,1);ar=m.ar
RECTS=[['3/10','39/100','-3/100','1/50'],['27/100','33/100','-57/1000','-1/50']];faces=[0,0]
def params(box,ta,tb):
 out=[]
 for j,t in enumerate((ta,tb)):
  xl,xh,yl,yh=map(R,RECTS[t]);v=ar(box[2*j]).union(ar(box[2*j+1]));f=faces[j]
  out.append(acb(ar(xl)+ar(xh-xl)*v,ar(yl if f==0 else yh))if f in(0,2)else acb(ar(xh if f==1 else xl),ar(yl)+ar(yh-yl)*v))
 return out
fn=next(x for x in ast.parse(SRC.read_text()).body if isinstance(x,ast.FunctionDef)and x.name=='certify')
class Capture(ast.NodeTransformer):
 def visit_Return(self,n):
  return ast.copy_location(ast.Return(ast.Call(ast.Name('locals',ast.Load()),[],[])),n)if isinstance(n.value,ast.List)else n
fn=Capture().visit(fn);ast.fix_missing_locations(fn);ns=dict(m.__dict__);ns['params']=params;exec(compile(ast.Module(body=[fn],type_ignores=[]),str(SRC)+'[two-right]','exec'),ns);cert=ns['certify']
def decode(ad):
 b=[R(0),R(1),R(0),R(1)]
 for j,v in enumerate(ad):k=2*(j%2);mid=(b[k]+b[k+1])/2;b[k+1-int(v)]=mid
 return b

def gp(z):return(1-(-2*P*I*z).exp()).log()
def gpp(z):return P*(P*z).cot()-P*I
def g(z):return ((-2*P*I*z).exp().polylog(2)-P*P/6)/(2*P*I)
def gamma(z,e,eta,x,y):
 a,s,b=[z[j]for j in(1,2,3)];pa=gp(s+a)+2*P*I*s-ar(1+R(eta,2))*gp(a);pb=gp(s+b)-ar(1+R(e,2))*gp(b)
 F=g(s+a)+g(s+b)-(2+e)*g(s)+2*P*I*a*s-ar(1+R(eta,2))*g(a)-ar(1+R(e,2))*g(b)
 return F+pa*(x-a)+pb*(y-b)
# Exact algebra fixes the positive sine roots, before outward evaluation.
v,t,k,eps=sy.symbols('v t k eps',positive=True)
identities=[]
def exact(name,expr):
 assert sy.simplify(expr)==0,name;identities.append(name)
w=(sy.sqrt(17)-1)/8
exact('mixed-corner four-type positive sine equation',1-w-4*w*w)
exact('double-half four-type cubic equation',1-v*v-2*v**3+(2*v**3+v*v-1))
exact('row curvature identity',k*t+(k+eps)/t-2*k-k*(t-1)**2/t-eps/t)
exact('zero-type quarter-row critical equation',1-sy.Rational(1,2)-sy.Rational(1,2))
assert 2*R(1,2)**3+R(1,2)**2-1<0<2*R(3,4)**3+R(3,4)**2-1
const={};cubic_bracket=None
for e in(0,1):
 const[e,0]=arb(0)if not e else -g(acb(ar('1/6'))).real
 for n in(1,2):
  if not e:u=ar('1/4')
  elif n==1:u=(((arb(17).sqrt()-1)/8).sqrt()).asin()/P
  else:
   # Outward bracket for the positive cubic root.
   lo,hi=R(1,2),R(3,4)
   for _ in range(180):
    md=(lo+hi)/2
    if 2*md**3+md**2-1>0:hi=md
    else:lo=md
   ss=ar(lo).union(ar(hi));u=ss.asin()/P;cubic_bracket=[str(lo),str(hi)]
   assert 2*lo**3+lo**2-1<0<2*hi**3+hi**2-1
  const[e,n]=(n*g(acb(ar('1/2')+u))-(n+e)*g(acb(u))).real
minimum_row_derivative=(2*(P/5).cos()).log()-2*(2*(P/5).sin()).log()
assert minimum_row_derivative>ar('1/10')
assert P>3
print('constants',{str(k):str(v)for k,v in const.items()},flush=True)
source=json.load(open(ROOT/'repro/results/research-mixed-geometric-support-slopes.json'))
assert source['status']=='passed' and source['full_family']
expected={(*word,ta,tb,fa,fb)for word in itertools.product((0,1),repeat=3)for ta,tb in itertools.product((0,1),repeat=2)for fa,fb in itertools.product(range(4),repeat=2)}
actual={(*c['word'],*c['external_types'],*c['faces'])for c in source['cases']}
assert expected==actual and len(source['cases'])==len(actual)==512
assert source['rectangles']==RECTS and source['slope_bounds']==['-1/5','1/4']
for c in source['cases']:
 codes=sorted(c['addresses']);assert len(codes)==len(set(codes))==c['accepted']
 assert all(not b.startswith(a)for a,b in zip(codes,codes[1:]))
 assert sum((R(1,2**len(a))for a in codes),R(0))==1
start=time.time();total=0;refinements=0;minall=arb(100);rows=[]
for ix,c in enumerate(source['cases']):
 word=tuple(c['word']);ta,tb=c['external_types'];faces[:]=c['faces'];pending=list(c['addresses']);good=[];mn=arb(100)
 while pending:
  ad=pending.pop();total+=1;bnd=decode(ad);w=cert(word,ta,tb,bnd,-R(3,25))
  if not w:why='selfmap'
  else:
   z=w['boxes'];a,s,b=[z[j]for j in(1,2,3)];e=word[1];eta=word[0]
   ne=6;rr=[ar(v)for v in w['rad']];ee=w['ee'];rho=max((sum((abs(ee[i,j])*rr[j]for j in range(ne)),arb(0))/rr[i]).upper()for i in range(ne));assert rho<1
   de=acb_mat(ne,2);de[0,0]=w['diff'](w['zz'][0]+w['p0'][0],w['hz'][0]+w['dp'][0]);de[ne-1,1]=w['diff'](w['zz'][-1]+w['p0'][1],w['hz'][-1]+w['dp'][1])
   residual=w['Y']*((w['J0']*w['D']+w['E0'])+acb_mat(w['dj'])*w['D']+de);cur=residual;su=residual
   for kk in range(4):cur=ee*cur;su=su+cur
   T=w['D']-su
   for j in range(2):
    mu=max((abs(residual[i,j])/rr[i]).upper()for i in range(ne));tail=mu*rho**5/(1-rho)
    for i in range(ne):T[i,j]+=acb(arb(0,(rr[i]*tail).upper()),arb(0,(rr[i]*tail).upper()))
   hss=gpp(s+a)+gpp(s+b)-(2+e)*gpp(s);U=gpp(s+a)+2*P*I;V=gpp(s+b)
   Haa=gpp(s+a)-ar(1+R(eta,2))*gpp(a)-U*U/hss;Hbb=gpp(s+b)-ar(1+R(e,2))*gpp(b)-V*V/hss;Hab=-U*V/hss
   mid=[(bnd[0]+bnd[1])/2,(bnd[2]+bnd[3])/2];wm=cert(word,ta,tb,[mid[0],mid[0],mid[1],mid[1]],-R(3,25));assert wm
   gaps=[]
   for x,y in itertools.product((ar('1/2'),arb(1)),repeat=2):
    v=gamma(wm['boxes'],e,eta,x,y).real
    ga=Haa*(x-a)+Hab*(y-b);gb=Hab*(x-a)+Hbb*(y-b)
    for j in range(2):
     deriv=ga*T[1,j]+gb*T[3,j];xl,xh,yl,yh=map(R,RECTS[(ta,tb)[j]]);velocity=acb(ar(xh-xl),0)if faces[j]in(0,2)else acb(0,ar(yh-yl));v-=abs((deriv*velocity).real)*ar((bnd[2*j+1]-bnd[2*j])/2)
    n=int(x==ar('1/2'))+int(y==ar('1/2'));gaps.append(v-const[e,n])
   if all(v>ar('1/50')for v in gaps):
    good.append(ad);mn=min(mn,*[v.lower()for v in gaps]);continue
   why=[str(v)for v in gaps]
  assert len(ad)<24,(word,faces,ad,why)
  pending.extend([ad+'0',ad+'1']);refinements+=1
  assert total<args.max_visits
 rows.append({'word':list(word),'external_types':[ta,tb],'faces':c['faces'],'addresses':good,'min_gap':str(mn)});minall=min(minall,mn)
 if ix%16==15:print('progress',ix+1,total,refinements,'min',str(minall),time.time()-start,flush=True)
for c in rows:
 codes=sorted(c['addresses']);assert len(codes)==len(set(codes))
 assert all(not b.startswith(a)for a,b in zip(codes,codes[1:]))
 assert sum((R(1,2**len(a))for a in codes),R(0))==1
assert {(*c['word'],*c['external_types'],*c['faces'])for c in rows}==expected
assert len(rows)==512
assert hashes=={p:sha(ROOT/p)for p in DEPS}
assert proof_hash==sha(PROOF)and script_hash==sha(__file__)
record={
 'status':'passed','precision_bits':args.precision,
 'scope':'Full original conditional source on both right target half-periods at height zero, including all rows and true Fourier weights; no entire exterior-complement or mixed-cycle lower bound.',
 'boundary_products':512,'accepted_cells':sum(len(c['addresses'])for c in rows),
 'visited_cells':total,'refinements':refinements,'cases':rows,
 'strict_reference_gap':'1/50','finite_source_gap':'1/100',
 'minimum_certified_reference_gap':str(minall),
 'source_corner_constants':{f'epsilon{e}_halfcount{n}':str(val)for(e,n),val in const.items()},
 'positive_cubic_root_bracket':cubic_bracket,
 'exact_algebraic_checks':identities,
 'strict_scalar_margins':{'minimum_row_derivative_minus_1/10':str(minimum_row_derivative-ar('1/10')),'pi_minus_three':str(P-3)},
 'proof_sha256':proof_hash,'script_sha256':script_hash,'dependencies_sha256':hashes,
 'elapsed_seconds':time.time()-start,
 'summary_scope':'All acceptances use exact rational thresholds and outward intervals; printed decimal summaries are informational only.',
}
args.output.parent.mkdir(parents=True,exist_ok=True)
args.output.write_text(json.dumps(record,indent=2)+'\n')
print('PASS',record['boundary_products'],'products,',record['accepted_cells'],'cells,',refinements,'refinements,4 exact identities+2 scalar margins',flush=True)
