#!/usr/bin/env python3
"""Paired right-transition boundary support with a reference barrier."""
from pathlib import Path
from fractions import Fraction as F
import argparse,ast,hashlib,importlib.util,itertools,json,time
import numpy as np
from scipy.optimize import brentq
from flint import arb,acb,acb_mat,ctx
ROOT=Path(__file__).resolve().parents[1];ctx.prec=192
PROOF=ROOT/'notes/research_mixed_paired_right_transition_support.md'
SRC=ROOT/'experiments/certify_mixed_cyclic_window_heights.py'
sp=importlib.util.spec_from_file_location('win',SRC);m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);m.PI=arb.pi();P=m.PI;I=acb(0,1);ar=m.ar
sp=importlib.util.spec_from_file_location('small',ROOT/'experiments/certify_mixed_real_small_support.py');core=importlib.util.module_from_spec(sp);sp.loader.exec_module(core);core.pi=P;core.ii=I
# The midpoint reference has a certified 2^-40 input radius, so the
# original fixed 1e-12 point-root radius is too small for this composition.
# A fresh 1e-10 contraction is checked; no inequality is bypassed.
pfn=next(x for x in ast.parse((ROOT/'experiments/certify_mixed_real_small_support.py').read_text()).body if isinstance(x,ast.FunctionDef)and x.name=='point_root')
class PointRadius(ast.NodeTransformer):
 def visit_Constant(self,node):return ast.copy_location(ast.Constant('1e-10'),node)if node.value=='1e-12'else node
pfn=PointRadius().visit(pfn);ast.fix_missing_locations(pfn);exec(compile(ast.Module(body=[pfn],type_ignores=[]),'[point radius]','exec'),core.__dict__)
RECTS=[['.30','.39','-.03','.02'],['.27','.33','-.057','-.02']];faces=[0,0]
def params(box,ta,tb):
 ans=[]
 for j,t in enumerate((ta,tb)):
  xl,xh,yl,yh=map(F,RECTS[t]);v=ar(box[2*j]).union(ar(box[2*j+1]));f=faces[j]
  ans.append(acb(ar(xl)+ar(xh-xl)*v,ar(yl if f==0 else yh))if f in(0,2)else acb(ar(xh if f==1 else xl),ar(yl)+ar(yh-yl)*v))
 return ans
fn=next(x for x in ast.parse(SRC.read_text()).body if isinstance(x,ast.FunctionDef)and x.name=='certify')
class Capture(ast.NodeTransformer):
 def visit_Return(self,n):return ast.copy_location(ast.Return(ast.Call(ast.Name('locals',ast.Load()),[],[])),n)if isinstance(n.value,ast.List)else n
fn=Capture().visit(fn);ast.fix_missing_locations(fn);ns=dict(m.__dict__);ns['params']=params;exec(compile(ast.Module(body=[fn],type_ignores=[]),str(SRC),'exec'),ns);cert=ns['certify']
def decode(ad,axes):
 b=[F(0),F(1)]*3
 for j,bit in enumerate(ad):
  assert bit in '01';axis=axes[ad[:j]];assert type(axis)is int and 0<=axis<3
  k=2*axis;mid=(b[k]+b[k+1])/2;b[k+1-int(bit)]=mid
 return b

def response(w):
 n=10;rr=[ar(v)for v in w['rad']];ee=w['ee'];rho=max((sum((abs(ee[i,j])*rr[j]for j in range(n)),arb(0))/rr[i]).upper()for i in range(n))
 if not rho<1:return None
 de=acb_mat(n,2);de[0,0]=w['diff'](w['zz'][0]+w['p0'][0],w['hz'][0]+w['dp'][0]);de[n-1,1]=w['diff'](w['zz'][-1]+w['p0'][1],w['hz'][-1]+w['dp'][1])
 residual=w['Y']*((w['J0']*w['D']+w['E0'])+acb_mat(w['dj'])*w['D']+de);cur=residual;su=residual
 for _ in range(4):cur=ee*cur;su=su+cur
 T=w['D']-su
 for j in range(2):
  mu=max((abs(residual[i,j])/rr[i]).upper()for i in range(n));tail=mu*rho**5/(1-rho)
  for i in range(n):T[i,j]+=acb(arb(0,(rr[i]*tail).upper()),arb(0,(rr[i]*tail).upper()))
 return T

def pair(z,word,s0,s1):
 x=core.phase(s0,z[0],z[1],word[1],word[2]);y=core.phase(s1,z[1],z[2],word[2],word[3])
 H=[[acb(0)for _ in range(3)]for _ in range(3)]
 for off,data in((0,x),(1,y)):
  for i in range(2):
   for j in range(2):H[i+off][j+off]+=data[2][i][j]
 return x[0]+y[0],[x[1][0],x[1][1]+y[1][0],y[1][1]],H

def point(a):return complex(float(a.real.mid()),float(a.imag.mid()))
def fgrad(a,b,eta,e):
 pp,qq=1/np.tan(np.pi*a),1/np.tan(np.pi*b)
 co=[1,pp+qq,-1+1j*(qq-pp)]if not e else[1,pp+qq+1j,pp*qq+1j*(pp+qq),1j*pp*qq-2j*(pp-1j)*(qq+1j)]
 rt=[z for z in np.roots(co)if z.real>0 and abs(z.imag)<1]
 if len(rt)!=1:raise ValueError('floating root')
 s=np.log((rt[0]+1j)/(rt[0]-1j))/(2j*np.pi)
 gp=lambda z:np.log(1-np.exp(-2j*np.pi*z))
 return [gp(s+a)+2j*np.pi*s-(1+eta/2)*gp(a),gp(s+b)-(1+e/2)*gp(b)]

def support(z0,g0,t0,word):
 refs=list(map(point,z0));tt=float(t0.mid());tau=20*(.5-tt);height=[tau*z.imag for z in refs];p=[]
 for j in(0,2):
  if j==0:fun=lambda x:fgrad(x+1j*height[0],tt+1j*height[1],word[1],word[2])[0].real-float(g0[0].real.mid())
  else:fun=lambda x:fgrad(tt+1j*height[1],x+1j*height[2],word[2],word[3])[1].real-float(g0[2].real.mid())
  if fun(.22)<=0:c=.22
  elif fun(.45)>=0:c=.45
  else:c=brentq(fun,.22,.45,xtol=1e-10)
  p.append(F(round(c*10**8),10**8))
 return p

def matvec(H,v):return [sum((a*b for a,b in zip(row,v)),acb(0))for row in H]
def dot(a,b):return sum((x*y for x,y in zip(a,b)),acb(0))
def test(case,bnd):
 word,ta,tb,fa,fb=case;faces[:]=[fa,fb];w=cert(word,ta,tb,bnd[:4],-F(3,25))
 if not w:return None,'reference'
 z=[w['boxes'][i]for i in(3,5,7)]
 if not all(ar('.24')<v.real<ar('.40')and abs(v.imag)<ar('.063')for v in z):return None,'image'
 T=response(w)
 if T is None:return None,'response'
 rf=pair(z,word,w['boxes'][4],w['boxes'][6]);B=[]
 for ell in range(2):
  q=[T[i,ell]for i in(3,5,7)];B.append(sum((abs(q[i]*q[j]*rf[2][i][j])for i in range(3)for j in range(3)),arb(0)))
 if not all(v<ar('.2')for v in B):return None,'barrier'
 mid=[(bnd[k]+bnd[k+1])/2 for k in(0,2,4)];wm=cert(word,ta,tb,[mid[0],mid[0],mid[1],mid[1]],-F(3,25))
 if not wm:return None,'reference midpoint'
 z0=[wm['boxes'][i]for i in(3,5,7)];r0=pair(z0,word,wm['boxes'][4],wm['boxes'][6]);t=ar('.45')+ar('.05')*ar(bnd[4]).union(ar(bnd[5]));t0=ar('.45')+ar('.05')*ar(mid[2]);tau=20*(ar('.5')-t);tau0=20*(ar('.5')-t0)
 try:pp,qq=support(z0,r0[1],t0,word);assert F('.22')<=pp<=F('.45')and F('.22')<=qq<=F('.45')
 except(ValueError,OverflowError):return None,'support proposal'
 target=[acb(ar(pp),tau*z[0].imag),acb(t,tau*z[1].imag),acb(ar(qq),tau*z[2].imag)]
 target0=[acb(ar(pp),tau0*z0[0].imag),acb(t0,tau0*z0[1].imag),acb(ar(qq),tau0*z0[2].imag)]
 rt=[];rt0=[]
 for j in(0,1):
  p=core.root_box(target[j],target[j+1],target0[j],target0[j+1],word[j+2])
  if p is None:return None,'target'
  rt.append(p[0]);rt0.append(p[1])
 tf=pair(target,word,*rt);tf0=pair(target0,word,*rt0)
 fee=lambda zs:ar('7.55')*zs[0].imag**2+ar('5.5')*zs[2].imag**2
 DD=(tf0[0]-r0[0]-dot(r0[1],[a-b for a,b in zip(target0,z0)])).real+(1-tau0)**2*fee(z0)
 gg=[tf0[1][j]-r0[1][j]for j in(0,2)];ge=[arb(0),arb(0)];radii=[ar((bnd[k+1]-bnd[k])/2)for k in(0,2,4)]
 for ell in range(3):
  if ell<2:
   ty=(ta,tb)[ell];xl,xh,yl,yh=map(F,RECTS[ty]);vel=acb(ar(xh-xl),0)if faces[ell]in(0,2)else acb(0,ar(yh-yl));R=[T[j,ell]*vel for j in(3,5,7)];W=[I*tau*v.imag for v in R]
   derivative=(dot([a-b for a,b in zip(tf[1],rf[1])],W)-dot(matvec(rf[2],R),[a-b for a,b in zip(target,z)])).real+2*(1-tau)**2*(ar('7.55')*z[0].imag*R[0].imag+ar('5.5')*z[2].imag*R[2].imag)
  else:
   R=[acb(0)]*3;W=[-I*z[0].imag,acb(ar('.05'),-z[1].imag),-I*z[2].imag]
   derivative=dot([a-b for a,b in zip(tf[1],rf[1])],W).real+2*(1-tau)*fee(z)
  DD+=abs(derivative)*radii[ell]
  dh=[a-b for a,b in zip(matvec(tf[2],W),matvec(rf[2],R))]
  for k,j in enumerate((0,2)):ge[k]+=abs(dh[j].real)*radii[ell]
 for k,c in enumerate((pp,qq)):
  gb=gg[k].real+arb(0,ge[k].upper());DD+=max((gb*ar(v-c)).upper()for v in(F('.22'),F('.45')))
 if not DD<ar('-.01'):return None,'gap'
 return [DD.upper(),*[v.upper()for v in B]],None

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main():
 global P,I
 ap=argparse.ArgumentParser(description=__doc__)
 ap.add_argument('--precision',type=int,default=256)
 ap.add_argument('--case',nargs=5)
 ap.add_argument('--input',type=Path)
 ap.add_argument('--output',type=Path,default=ROOT/'repro/results/research-mixed-paired-right-transition-support.json')
 ap.add_argument('--max-visits',type=int,default=3000000)
 args=ap.parse_args();assert args.precision>=160;ctx.prec=args.precision;P=arb.pi();I=acb(0,1);m.PI=P;ns['PI']=P;core.pi=P;core.ii=I
 deps=['experiments/certify_mixed_cyclic_window_heights.py',
       'experiments/certify_mixed_real_small_support.py',
       'notes/research_mixed_cyclic_critical_height_bounds.md',
       'notes/research_mixed_height_coupled_reference_extension.md',
       'experiments/check_mixed_height_coupled_reference_extension.py',
       'repro/results/research-mixed-height-coupled-reference-extension.json']
 records=[
 ('cyclic-block-localization','certify_mixed_cyclic_block_localization.py','research_mixed_cyclic_critical_localization.md'),
 ('cyclic-window-heights','certify_mixed_cyclic_window_heights.py','research_mixed_cyclic_critical_height_bounds.md'),
 ('type-four-height-refinement','certify_mixed_type_four_height_refinement.py','research_mixed_type_four_height_refinement.md'),
 ('type-three-window-strip','certify_mixed_type_three_window_strip.py','research_mixed_type_three_window_strip.md'),
 ('closed-cotangent-roots','check_mixed_closed_cotangent_roots.py','research_mixed_closed_cotangent_roots.md'),
 ('right-square-conditional-packets','certify_mixed_right_square_conditional_packets.py','research_mixed_unselected_right_taper_products.md'),
 ('oriented-height-reset','certify_mixed_oriented_height_reset.py','research_mixed_oriented_height_reset.md')]
 for stem,script,proof in records:
  record='repro/results/research-mixed-'+stem+'.json'
  for p in(record,'experiments/'+script,'notes/'+proof):
   if p not in deps:deps.append(p)
  d=json.loads((ROOT/record).read_text());assert d['status']=='passed'
  assert d['script_sha256']==sha(ROOT/'experiments'/script)and d['proof_sha256']==sha(ROOT/'notes'/proof)
  for key in('dependencies','dependencies_sha256'):
   for p,h in d.get(key,{}).items():assert sha(ROOT/p)==h,(stem,p)
 er=json.loads((ROOT/deps[5]).read_text());assert er['status']=='passed'and er['proof_sha256']==sha(ROOT/deps[3])and er['script_sha256']==sha(ROOT/deps[4])
 hashes={p:sha(ROOT/p)for p in deps};ph,sh=sha(PROOF),sha(__file__)
 cot=(2*P*ar('.063')).sinh()/((2*P*ar('.063')).cosh()-(2*P*ar('.22')).cos())
 assert cot<ar('.5')and (2*P*ar('.063')).cosh()*(2*P*ar('.22')).cos()<1
 assert F(1,5)*2*F(1,20)**2/4==F(1,4000)
 assert F(1,100)-F(1,4000)>F(1,125)>F(1,250)
 ih=None;old=None
 if args.input:
  ih=sha(args.input);saved=json.loads(args.input.read_text());assert saved['status']=='passed'
  assert saved['proof_sha256']==ph and saved['script_sha256']==sh and saved['dependencies']==hashes
  old={tuple([tuple(r['word']),*r['external_types'],*r['faces']]):r for r in saved['cases']}
  assert len(old)==len(saved['cases'])==2048
 if args.case:cases=[(tuple(map(int,args.case[0])),*map(int,args.case[1:]))]
 else:cases=[(word,ta,tb,fa,fb)for word in itertools.product((0,1),repeat=5)for ta,tb,fa,fb in itertools.product(range(2),range(2),range(4),range(4))]
 assert len(set(cases))==len(cases)
 if not args.case:assert len(cases)==2048
 rows=[];visits=0;start=time.time();maximum=None;barriers=[arb(0),arb(0)]
 for case in cases:
  pending=list(reversed(old[case]['addresses']))if old is not None else[''];axes=dict(old[case]['split_axes'])if old is not None else{};good=[];why={};mx=None;bv=[arb(0),arb(0)]
  while pending:
   ad=pending.pop();visits+=1;assert visits<=args.max_visits,(case,visits);box=decode(ad,axes);ans,reason=test(case,box)
   if ans is None:
    assert old is None,(case,ad,reason,'saved cell failed')
    why[reason]=why.get(reason,0)+1;assert len(ad)<30,(case,ad,why)
    candidates=range(2)if reason in('reference','image','response','barrier','reference midpoint')else range(3)
    weights=[]
    for j in candidates:
     if j==2:scale=F('.1')
     else:
      xl,xh,yl,yh=map(F,RECTS[case[1+j]]);scale=xh-xl if case[3+j]in(0,2)else yh-yl
     weights.append((scale*(box[2*j+1]-box[2*j]),j))
    axes[ad]=max(weights)[1];pending.extend([ad+'1',ad+'0'])
   else:
    good.append(ad);mx=ans[0]if mx is None else max(mx,ans[0]);bv=[max(bv[j],ans[j+1])for j in range(2)]
  codes=sorted(good);assert len(codes)==len(set(codes))and all(not b.startswith(a)for a,b in zip(codes,codes[1:]))
  assert sum((F(1,2**len(a))for a in codes),F(0))==1
  assert set(axes)=={a[:j]for a in codes for j in range(len(a))}
  maximum=mx if maximum is None else max(maximum,mx);barriers=[max(barriers[j],bv[j])for j in range(2)]
  row=dict(word=case[0],external_types=list(case[1:3]),faces=list(case[3:5]),addresses=codes,split_axes=axes,accepted=len(codes),boundary_defect_upper=str(mx),response_bounds=list(map(str,bv)),split_reasons=why);rows.append(row)
  print('progress',len(rows),len(cases),case,len(codes),visits,str(mx),time.time()-start,flush=True)
  Path(str(args.output)+'.partial').write_text(json.dumps(dict(status='running',cases=rows),separators=(',',':'))+'\n')
 assert hashes=={p:sha(ROOT/p)for p in deps}and ph==sha(PROOF)and sh==sha(__file__)
 if args.input:assert ih==sha(args.input)
 out=dict(status='partial-case-passed'if args.case else'passed',precision_bits=args.precision,boundary_products=len(rows),accepted_cells=sum(r['accepted']for r in rows),visited_cells=visits,cases=rows,maximum_boundary_defect=str(maximum),maximum_response_bounds=list(map(str,barriers)),target_cotangent_bound=str(cot.upper()),exact_budgets=2,scalar_checks=2,proof_sha256=ph,script_sha256=sh,dependencies=hashes,elapsed_seconds=time.time()-start,scope='Paired unselected right-transition phase support on actual cyclic references, including two oriented outside reset debits; original finite-source consequence and isolated four-block stars only. No arbitrary transition-cluster or full-period theorem.'if not args.case else'Single boundary-product pilot only.')
 if args.input:out.update(input_path=str(args.input),input_sha256=ih)
 args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(out,indent=2)+'\n');Path(str(args.output)+'.partial').unlink(missing_ok=True)
 print('PASS',len(rows),out['accepted_cells'],visits,flush=True)
if __name__=='__main__':main()
