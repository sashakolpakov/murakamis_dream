#!/usr/bin/env python3
"""Correlated five-window comparison for two real-right incident raw blocks."""
from pathlib import Path
from fractions import Fraction as F
import argparse,ast,hashlib,importlib.util,itertools,json,time
from flint import arb,acb,acb_mat,ctx
ROOT=Path(__file__).resolve().parents[1];PROOF=ROOT/'notes/research_mixed_right_pair_correlated_support.md';SRC=ROOT/'experiments/certify_mixed_cyclic_window_heights.py'
parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--precision',type=int,default=256);parser.add_argument('--case',nargs=5);parser.add_argument('--max-visits',type=int,default=1000000);parser.add_argument('--output',type=Path,default=ROOT/'repro/results/research-mixed-right-pair-correlated-support.json');args=parser.parse_args();ctx.prec=args.precision;assert args.precision>=160
sp=importlib.util.spec_from_file_location('pair_win',SRC);m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);m.PI=arb.pi();P=m.PI;I=acb(0,1);ar=m.ar
RECTS=[['3/10','39/100','-3/100','1/50'],['27/100','33/100','-57/1000','-1/50']];faces=[0,0]
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
DEPS=['notes/research_mixed_cyclic_critical_height_bounds.md','experiments/certify_mixed_cyclic_window_heights.py','notes/research_mixed_cyclic_critical_localization.md','notes/research_mixed_type_four_height_refinement.md','notes/research_mixed_right_pair_raw_reduction.md','experiments/check_mixed_right_pair_raw_reduction.py','repro/results/research-mixed-right-pair-raw-reduction.json','notes/research_mixed_oriented_height_reset.md','experiments/certify_mixed_oriented_height_reset.py','repro/results/research-mixed-oriented-height-reset.json','notes/research_mixed_conditional_torus_composition.md']
INHERITED=[
 ('cyclic-block-localization','certify_mixed_cyclic_block_localization.py','research_mixed_cyclic_critical_localization.md'),
 ('cyclic-block-boundary-images','certify_mixed_cyclic_block_boundary_images.py','research_mixed_cyclic_critical_height_bounds.md'),
 ('cyclic-window-heights','certify_mixed_cyclic_window_heights.py','research_mixed_cyclic_critical_height_bounds.md'),
 ('type-four-height-refinement','certify_mixed_type_four_height_refinement.py','research_mixed_type_four_height_refinement.md'),
 ('plateau-accretivity','check_mixed_plateau_accretivity.py','research_mixed_plateau_accretivity.md'),
 ('selected-reset-plateau-support','certify_mixed_selected_reset_plateau_support.py','research_mixed_selected_reset_plateau_support.md'),
 ('selected-plateau-support','certify_mixed_selected_plateau_support.py','research_mixed_selected_plateau_support.md')]
for name,script,proof in INHERITED:
 for p in('repro/results/research-mixed-'+name+'.json','experiments/'+script,'notes/'+proof):
  if p not in DEPS:DEPS.append(p)
for p in('notes/research_mixed_coupled_outer_graph.md','notes/research_mixed_uniform_low_plateau_clusters.md'):
 if p not in DEPS:DEPS.append(p)
hashes={p:sha(ROOT/p)for p in DEPS};ph,sh=sha(PROOF),sha(__file__)
for name,script,proof in INHERITED:
 r=json.loads((ROOT/('repro/results/research-mixed-'+name+'.json')).read_text())
 assert r['status']=='passed'and r['script_sha256']==sha(ROOT/'experiments'/script)and r['proof_sha256']==sha(ROOT/'notes'/proof),(name,'binding')
 for key in('dependencies','dependencies_sha256'):
  for p,h in r.get(key,{}).items():assert sha(ROOT/p)==h,(name,p)

for pi,si,ri in((4,5,6),(7,8,9)):
 r=json.loads((ROOT/DEPS[ri]).read_text());assert r['status']=='passed'and r['proof_sha256']==hashes[DEPS[pi]]and r['script_sha256']==hashes[DEPS[si]]
 for key in('dependencies','dependencies_sha256'):
  for p,h in r.get(key,{}).items():assert sha(ROOT/p)==h,p

def params(box,ta,tb):
 out=[]
 for j,t in enumerate((ta,tb)):
  xl,xh,yl,yh=map(F,RECTS[t]);v=ar(box[2*j]).union(ar(box[2*j+1]));f=faces[j]
  out.append(acb(ar(xl)+ar(xh-xl)*v,ar(yl if f==0 else yh))if f in(0,2)else acb(ar(xh if f==1 else xl),ar(yl)+ar(yh-yl)*v))
 return out
fn=next(x for x in ast.parse(SRC.read_text()).body if isinstance(x,ast.FunctionDef)and x.name=='certify')
class Capture(ast.NodeTransformer):
 def visit_Return(self,n):return ast.copy_location(ast.Return(ast.Call(ast.Name('locals',ast.Load()),[],[])),n)if isinstance(n.value,ast.List)else n
fn=Capture().visit(fn);ast.fix_missing_locations(fn);ns=dict(m.__dict__);ns['params']=params;exec(compile(ast.Module(body=[fn],type_ignores=[]),str(SRC)+'[right-pair]','exec'),ns);cert=ns['certify']
def decode(ad):
 b=[F(0),F(1),F(0),F(1)]
 for j,v in enumerate(ad):k=2*(j%2);mid=(b[k]+b[k+1])/2;b[k+1-int(v)]=mid
 return b

def gp(z):return(1-(-2*P*I*z).exp()).log()
def gpp(z):return P*(P*z).cot()-P*I
def g(z):return ((-2*P*I*z).exp().polylog(2)-P*P/6)/(2*P*I)
def local(a,s,b,eta,e):
 pa=gp(s+a)+2*P*I*s-ar(1+F(eta,2))*gp(a);pb=gp(s+b)-ar(1+F(e,2))*gp(b)
 val=g(s+a)+g(s+b)-(2+e)*g(s)+2*P*I*a*s-ar(1+F(eta,2))*g(a)-ar(1+F(e,2))*g(b)
 hss=gpp(s+a)+gpp(s+b)-(2+e)*gpp(s);U=gpp(s+a)+2*P*I;V=gpp(s+b)
 aa=gpp(s+a)-ar(1+F(eta,2))*gpp(a)-U*U/hss;bb=gpp(s+b)-ar(1+F(e,2))*gpp(b)-V*V/hss;ab=-U*V/hss
 return val,pa,pb,aa,ab,bb
src=json.loads((ROOT/DEPS[6]).read_text());grid=[F(-1,5)+F(j,40)for j in range(19)];profiles={(p['epsilon'],p['other_halfweight']):p['grid']for p in src['profiles']}
def chord(key,kb):
 if not(kb>ar(grid[0])and kb<ar(grid[-1])):return None
 lo,hi=kb.lower(),kb.upper();i=max([0]+[j for j in range(19)if ar(grid[j])<lo]);j=min([18]+[j for j in range(19)if ar(grid[j])>hi])
 if i==j:
  if j<18:j+=1
  else:i-=1
 L,U=[F(profiles[key][t]['upper'])for t in(i,j)];A=(U-L)/(grid[j]-grid[i]);B=L-A*grid[i];return A,B

def test(word,ta,tb,bnd):
 w=cert(word,ta,tb,bnd,-F(3,25))
 if not w:return None
 n=10;z=w['boxes'];a,b,c=[z[k]for k in(3,5,7)];aa=local(a,z[4],b,word[1],word[2]);bb=local(b,z[6],c,word[2],word[3])
 rr=[ar(v)for v in w['rad']];ee=w['ee'];rho=max((sum((abs(ee[i,j])*rr[j]for j in range(n)),arb(0))/rr[i]).upper()for i in range(n));assert rho<1
 de=acb_mat(n,2);de[0,0]=w['diff'](w['zz'][0]+w['p0'][0],w['hz'][0]+w['dp'][0]);de[n-1,1]=w['diff'](w['zz'][-1]+w['p0'][1],w['hz'][-1]+w['dp'][1])
 residual=w['Y']*((w['J0']*w['D']+w['E0'])+acb_mat(w['dj'])*w['D']+de);cur=residual;su=residual
 for _ in range(4):cur=ee*cur;su=su+cur
 T=w['D']-su
 for j in range(2):
  mu=max((abs(residual[i,j])/rr[i]).upper()for i in range(n));tail=mu*rho**5/(1-rho)
  for i in range(n):T[i,j]+=acb(arb(0,(rr[i]*tail).upper()),arb(0,(rr[i]*tail).upper()))
 mids=[(bnd[0]+bnd[1])/2,(bnd[2]+bnd[3])/2];wm=cert(word,ta,tb,[mids[0],mids[0],mids[1],mids[1]],-F(3,25));assert wm
 zm=wm['boxes'];am,bm,cm=[zm[k]for k in(3,5,7)];amv=local(am,zm[4],bm,word[1],word[2]);bmv=local(bm,zm[6],cm,word[2],word[3]);pa,pb=amv[1],bmv[2];C=amv[0]+bmv[0]-pa*am-pb*cm
 grads=[];ke=[arb(0),arb(0)]
 for j in range(2):
  dpa=aa[3]*T[3,j]+aa[4]*T[5,j];dpb=bb[4]*T[5,j]+bb[5]*T[7,j]
  xl,xh,yl,yh=map(F,RECTS[(ta,tb)[j]]);vel=acb(ar(xh-xl),0)if faces[j]in(0,2)else acb(0,ar(yh-yl));rad=ar((bnd[2*j+1]-bnd[2*j])/2)
  dpa*=vel;dpb*=vel;da=T[3,j]*vel;dc=T[7,j]*vel
  grads.append((dpa,dpb,da,dc,rad));ke[0]+=abs(dpa.real)*rad;ke[1]+=abs(dpb.real)*rad
 cs=[chord(key,p.real+arb(0,k.upper()))for key,p,k in(( (word[2],word[1]),pa,ke[0]),((word[3],word[3]),pb,ke[1]))]
 if any(v is None for v in cs):return None
 A0,B0=cs[0];A1,B1=cs[1];p,q=-ar(A0),-ar(A1);cost=ar(F(151,20))*am.imag**2+ar(F(11,2))*cm.imag**2
 gap=(C+pa*p+pb*q).real-ar(B0+B1)-cost
 for dpa,dpb,da,dc,rad in grads:
  der=((p-a)*dpa+(q-c)*dpb).real-ar(F(151,10))*a.imag*da.imag-11*c.imag*dc.imag
  gap-=abs(der)*rad
 if not gap>ar(F(1,5000)):return None
 return gap.lower()

if args.case:cases=[(tuple(map(int,args.case[0])),*map(int,args.case[1:]))]
else:cases=[(word,ta,tb,fa,fb)for word in itertools.product((0,1),repeat=5)for ta,tb in itertools.product((0,1),repeat=2)for fa,fb in itertools.product(range(4),repeat=2)]
rows=[];start=time.time();vis=0;worst=arb(100)
for case in cases:
 word,ta,tb,fa,fb=case;faces[:]=[fa,fb];pending=[''];good=[];mn=arb(100)
 while pending:
  ad=pending.pop();vis+=1;gap=test(word,ta,tb,decode(ad))
  if gap is None:
   assert len(ad)<30,(case,ad)
   pending.extend([ad+'0',ad+'1'])
  else:good.append(ad);mn=min(mn,gap)
  assert vis<args.max_visits,(case,ad,vis)
 codes=sorted(good);assert all(not b.startswith(a)for a,b in zip(codes,codes[1:]));assert sum((F(1,2**len(x))for x in codes),F(0))==1
 rows.append(dict(word=word,external_types=[ta,tb],faces=[fa,fb],addresses=good,min_gap=str(mn)));worst=min(worst,mn);print('progress',len(rows),case,len(good),vis,str(mn),time.time()-start,flush=True)
 partial=dict(status='running',cases=rows);Path(str(args.output)+'.partial').write_text(json.dumps(partial,separators=(',',':'))+'\n')
assert hashes=={p:sha(ROOT/p)for p in DEPS}and ph==sha(PROOF)and sh==sha(__file__)
if not args.case:assert len(rows)==2048
patterns=0
for length in range(4,13):
 for bits in itertools.product((0,1),repeat=length):
  centers=[j for j,b in enumerate(bits)if b]
  if not centers:continue
  if any((centers[(k+1)%len(centers)]-j)%length not in range(4,length)and not(len(centers)==1 and length>=4)for k,j in enumerate(centers)):continue
  groups=[{(j+d)%length for d in(-2,-1,0,1)}for j in centers]
  assert all(len(g)==4 for g in groups)and sum(map(len,groups))==len(set().union(*groups))
  zero=[bool(bits[j]or bits[(j-1)%length]or bits[(j+1)%length])for j in range(length)]
  used=set().union(*groups)
  for j in centers:
   assert all(zero[(j+d)%length]for d in(-1,0,1))and all(not zero[(j+d)%length]for d in(-2,2))
  for j in set(range(length))-used:assert not zero[j]and not zero[(j+1)%length]
  patterns+=1
result=dict(status='passed'if not args.case else'partial-case-passed',precision_bits=args.precision,boundary_products=len(rows),cyclic_star_bookkeeping_diagnostics=patterns,accepted_cells=sum(len(r['addresses'])for r in rows),visited_cells=vis,minimum_gap=str(worst),strict_gap='1/5000',cases=rows,proof_sha256=ph,script_sha256=sh,dependencies=hashes,elapsed_seconds=time.time()-start,scope='Five-window correlated pair raw support pays oriented adjacent reset costs. Full isolated-right four-block gap and separated-right P/R contribution for every selected subset; no adjacent-right or arbitrary exterior theorem.'if not args.case else'Single boundary-product pilot, no general certificate.')
args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(result,indent=2)+'\n');Path(str(args.output)+'.partial').unlink(missing_ok=True);print('PASS',len(rows),vis,time.time()-start,flush=True)
