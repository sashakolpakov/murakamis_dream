#!/usr/bin/env python3
"""Outward geometric comparison for right-core support-grid chords.

Verifies every correlated three-window reference boundary and original complex tangent, with both Fourier support alternatives; no entire exterior claim.
"""
from pathlib import Path
import argparse,ast,hashlib,importlib.util,json,itertools,time
import sympy as sy
from fractions import Fraction as R
from flint import arb,acb,acb_mat,ctx
ROOT=Path(__file__).resolve().parents[1]
PROOF=ROOT/'notes/research_mixed_right_core_support.md'
SRC=ROOT/'experiments/certify_mixed_cyclic_window_heights.py'
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--precision',type=int,default=256)
parser.add_argument('--max-visits',type=int,default=50000)
parser.add_argument('--output',type=Path,default=ROOT/'repro/results/research-mixed-right-core-support-reference.json')
args=parser.parse_args();assert args.precision>=160;ctx.prec=args.precision
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
DEPS=[
 'notes/research_mixed_right_half_source_reduction.md',
 'experiments/certify_mixed_right_core_support_grid.py',
 'repro/results/research-mixed-right-core-support-grid.json',
 'notes/research_mixed_two_right_source_bound.md',
 'experiments/certify_mixed_two_right_source_bound.py',
 'repro/results/research-mixed-two-right-source-bound.json',
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
from collections import defaultdict
gridrecord=json.loads((ROOT/'repro/results/research-mixed-right-core-support-grid.json').read_text())
assert gridrecord['status']=='passed'and gridrecord['support_values']==750
assert gridrecord['proof_sha256']==proof_hash
assert gridrecord['script_sha256']==sha(ROOT/'experiments/certify_mixed_right_core_support_grid.py')
for p,v in gridrecord['dependencies_sha256'].items():assert sha(ROOT/p)==v
profiles=gridrecord['profiles']
prof=defaultdict(list)
for p in profiles:prof[p['e'],p['b'],p['c']].append(p)
grid=[R(-1,5)+R(j,20)for j in range(10)]
def chord(p,kb):
 lo=max(kb.lower(),ar(grid[0]));hi=min(kb.upper(),ar(grid[-1]));assert lo<=hi
 i=max([0]+[j for j in range(10)if ar(grid[j])<lo])
 j=min([9]+[j for j in range(10)if ar(grid[j])>hi])
 if i==j:
  if j<9:j+=1
  else:i-=1
 L=R(p['grid'][i]['upper']);U=R(p['grid'][j]['upper']);A=(U-L)/(grid[j]-grid[i]);B=L-A*grid[i]
 return A,B
source=json.load(open(ROOT/'repro/results/research-mixed-geometric-support-slopes.json'))
rows=[];start=time.time();total=0;refinements=0;minall=arb(100);worst=None
for ix,case in enumerate(source['cases']):
 word=tuple(case['word']);ta,tb=case['external_types'];faces[:]=case['faces'];pending=list(case['addresses']);good=[];mn=arb(100)
 while pending:
  ad=pending.pop();total+=1;bnd=decode(ad);w=cert(word,ta,tb,bnd,-R(3,25));assert w
  z=w['boxes'];a,s,b=[z[j]for j in(1,2,3)];e=word[1];eta=word[0]
  rr=[ar(v)for v in w['rad']];ee=w['ee'];rho=max((sum((abs(ee[i,j])*rr[j]for j in range(6)),arb(0))/rr[i]).upper()for i in range(6));assert rho<1
  de=acb_mat(6,2);de[0,0]=w['diff'](w['zz'][0]+w['p0'][0],w['hz'][0]+w['dp'][0]);de[5,1]=w['diff'](w['zz'][-1]+w['p0'][1],w['hz'][-1]+w['dp'][1])
  residual=w['Y']*((w['J0']*w['D']+w['E0'])+acb_mat(w['dj'])*w['D']+de);cur=residual;su=residual
  for kk in range(4):cur=ee*cur;su=su+cur
  T=w['D']-su
  for j in range(2):
   mu=max((abs(residual[i,j])/rr[i]).upper()for i in range(6));tail=mu*rho**5/(1-rho)
   for i in range(6):T[i,j]+=acb(arb(0,(rr[i]*tail).upper()),arb(0,(rr[i]*tail).upper()))
  hss=gpp(s+a)+gpp(s+b)-(2+e)*gpp(s);U=gpp(s+a)+2*P*I;V=gpp(s+b)
  Haa=gpp(s+a)-ar(1+R(eta,2))*gpp(a)-U*U/hss;Hbb=gpp(s+b)-ar(1+R(e,2))*gpp(b)-V*V/hss;Hab=-U*V/hss
  mid=[(bnd[0]+bnd[1])/2,(bnd[2]+bnd[3])/2];wm=cert(word,ta,tb,[mid[0],mid[0],mid[1],mid[1]],-R(3,25));assert wm
  aa,ss,bb=[wm['boxes'][j]for j in(1,2,3)]
  pa=gp(ss+aa)+2*P*I*ss-ar(1+R(eta,2))*gp(aa);pb=gp(ss+bb)-ar(1+R(e,2))*gp(bb)
  FF=g(ss+aa)+g(ss+bb)-(2+e)*g(ss)+2*P*I*aa*ss-ar(1+R(eta,2))*g(aa)-ar(1+R(e,2))*g(bb)
  C=FF-pa*aa-pb*bb
  dp=[];kerr=[arb(0),arb(0)]
  for j in range(2):
   qa=Haa*T[1,j]+Hab*T[3,j];qb=Hab*T[1,j]+Hbb*T[3,j]
   xl,xh,yl,yh=map(R,RECTS[(ta,tb)[j]]);vel=acb(ar(xh-xl),0)if faces[j]in(0,2)else acb(0,ar(yh-yl));rad=ar((bnd[2*j+1]-bnd[2*j])/2)
   dp.append((qa*vel,qb*vel,(-a*qa-b*qb)*vel,rad))
   kerr[0]+=abs((qa*vel).real)*rad;kerr[1]+=abs((qb*vel).real)*rad
  kappas=[pp.real+arb(0,kerr[j].upper())for j,pp in enumerate([pa,pb])]
  gaps=[]
  for orient,key in [(0,(e,e,0)),(1,(e,eta,1))]:
   for p in prof[key]:
    A,B=chord(p,kappas[1-orient]);h=R(p['h']);other=acb(ar(-A),ar(h));x,y=(acb(ar('1/2')),other)if orient==0 else(other,acb(ar('1/2')))
    val=(C+pa*x+pb*y).real
    for qa,qb,qc,rad in dp:val-=abs((qa*x+qb*y+qc).real)*rad
    gap=val-ar(B);gaps.append(gap)
    if gap.lower()<minall:minall=gap.lower();worst=dict(word=word,external=[ta,tb],faces=faces[:],ad=ad,orient=orient,profile={k:v for k,v in p.items()if k!='grid'},gap=str(gap))
  if all(v>ar('1/500')for v in gaps):good.append(ad);mn=min(mn,*[v.lower()for v in gaps]);continue
  assert len(ad)<22,(word,ta,tb,faces,ad,worst)
  pending.extend([ad+'0',ad+'1']);refinements+=1
  assert total<args.max_visits
 rows.append(dict(word=word,external=[ta,tb],faces=faces[:],addresses=good,min_gap=str(mn)))
 if ix%16==15:print('progress',ix+1,total,refinements,str(minall),time.time()-start,flush=True)
expected={(*word,ta,tb,fa,fb)for word in itertools.product((0,1),repeat=3)for ta,tb in itertools.product((0,1),repeat=2)for fa,fb in itertools.product(range(4),repeat=2)}
assert len(rows)==512 and {(*p['word'],*p['external'],*p['faces'])for p in rows}==expected
for p in rows:
 codes=sorted(p['addresses']);assert len(codes)==len(set(codes))
 assert all(not b.startswith(a)for a,b in zip(codes,codes[1:]))
 assert sum((R(1,2**len(a))for a in codes),R(0))==1
assert hashes=={p:sha(ROOT/p)for p in DEPS}
assert proof_hash==sha(PROOF)and script_hash==sha(__file__)
minimum=min(arb(p['min_gap']).lower()for p in rows)
assert minimum>ar('1/500')
record=dict(status='passed',precision_bits=args.precision,boundary_products=512,accepted_cells=sum(len(p['addresses'])for p in rows),visited_cells=total,refinements=refinements,cases=rows,minimum_accepted_gap=str(minimum),strict_support_gap='1/500',finite_partial_source_gap='1/1000',elapsed_seconds=time.time()-start,proof_sha256=proof_hash,script_sha256=script_hash,dependencies_sha256=hashes,scope='All reference products and union-taper right-core profiles, including the raw u=1 profile. High rows at other angles below.13 and the remaining exterior are not disposed of here.')
args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(record,indent=2)+'\n')
print('PASS',len(rows),total,refinements,time.time()-start,flush=True)
