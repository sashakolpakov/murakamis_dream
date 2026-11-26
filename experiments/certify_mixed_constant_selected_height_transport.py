#!/usr/bin/env python3
"""Saved-cover proof of constant-selected-height half-stencil inequalities."""
import argparse,gzip,hashlib,importlib.util,json,time,sys,itertools,math,tempfile
from concurrent.futures import ProcessPoolExecutor,as_completed
from pathlib import Path
from fractions import Fraction as F
from flint import arb,acb,ctx
BASE=Path(__file__).resolve().parents[1]
PROOF=BASE/'notes/research_mixed_constant_selected_height_transport.md'
ROOT_HELPER=BASE/'experiments/certify_mixed_isolated_transition_phase.py'
ROOT_HELPER_SHA=hashlib.sha256(ROOT_HELPER.read_bytes()).hexdigest()
sp=importlib.util.spec_from_file_location('half_root',ROOT_HELPER);m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m)
assert ROOT_HELPER_SHA==hashlib.sha256(ROOT_HELPER.read_bytes()).hexdigest()
ctx.prec=192;pi=arb.pi();ii=acb(0,1);m.pi,m.ii=pi,ii;m.core.pi,m.core.ii=pi,ii
ar=m.ar;n=5
proposal=m.proposal;second=m.second;equation=m.equation;gpp=m.gpp;point_root=m.point_root
def root_box(a, b, a0, b0, eps, witness=None):
    center = proposal(a0, b0, eps) if witness is None else witness["center"]
    if center is None:
        return None
    z0 = acb(ar(center[0]), ar(center[1]))
    H0 = second(z0, a0, b0, eps)
    Y = 1/H0
    E = [gpp(z0+a0)+2*pi*ii, gpp(z0+b0)]
    dp = [a-a0, b-b0]
    if witness is None:
        dd = [[str(float((-Y*e).real.mid())), str(float((-Y*e).imag.mid()))] for e in E]
    else:
        dd = witness["derivatives"]
    deriv = [acb(ar(v[0]), ar(v[1])) for v in dd]
    dz = sum((deriv[j]*dp[j] for j in (0, 1)), acb(0))
    lin = equation(z0, a0, b0, eps)+sum(((H0*deriv[j]+E[j])*dp[j] for j in (0, 1)), acb(0))

    def rem(base, delta):
        w = base+acb(arb(0, abs(delta.real).upper()), arb(0, abs(delta.imag).upper()))
        if not 0 < w.real < 1:
            return arb.pos_inf()
        return pi*pi*abs(1/(pi*w).sin()**2)*abs(delta)**2/2

    err = abs(Y)*(abs(lin)+rem(z0+a0, dz+dp[0])+rem(z0+b0, dz+dp[1])+(2+eps)*rem(z0, dz))
    if not err.is_finite():
        return None
    radius = F(witness["radius"]) if witness is not None else F(max(1, math.ceil(float(err.upper())*4*2**42)), 2**42)
    if radius > F(1, 20):
        return None
    delta = dz+acb(arb(0, ar(radius)), arb(0, ar(radius)))
    z = z0+delta
    S=(pi*z).cot()
    if not (0 < z.real < ar(F(1,2)) and S.real > 0 and abs(S.imag) < 1):
        return None
    if not all(0 < w.real < 1 for w in (z, z+a, z+b)):
        return None

    def dc(base, move):
        return -pi*(pi*move).sin()/((pi*base).sin()*(pi*(base+move)).sin())

    defect = 1-Y*H0-Y*(dc(z0+a0, delta+dp[0])+dc(z0+b0, delta+dp[1])-(2+eps)*dc(z0, delta))
    if not err+abs(defect)*ar(radius) < ar(radius):
        return None
    pr = point_root(a0, b0, eps, center)
    if pr is None:
        return None
    return z, pr[0], {"center": center, "derivatives": dd, "radius": str(radius)}

class D:
 def __init__(self,v,d=None):self.v=v if isinstance(v,arb)else ar(v);self.d=d if d is not None else[arb(0)for _ in range(n)]
 def __add__(a,b):
  if not isinstance(b,D):b=D(b)
  return D(a.v+b.v,[x+y for x,y in zip(a.d,b.d)])
 __radd__=__add__
 def __neg__(a):return D(-a.v,[-x for x in a.d])
 def __sub__(a,b):return a+-b if isinstance(b,D)else a+D(-F(b))
 def __rsub__(a,b):return D(b)+-a
 def __mul__(a,b):
  if not isinstance(b,D):b=D(b)
  return D(a.v*b.v,[x*b.v+a.v*y for x,y in zip(a.d,b.d)])
 __rmul__=__mul__
 def __truediv__(a,b):return a*D(1/F(b))
def minimum(a,b):
 if not isinstance(a,D):a=D(a)
 if not isinstance(b,D):b=D(b)
 if a.v.upper()<b.v.lower():return a
 if b.v.upper()<a.v.lower():return b
 return D(min(a.v.lower(),b.v.lower()).union(min(a.v.upper(),b.v.upper())),[x.union(y)for x,y in zip(a.d,b.d)])
H={0:(F('-.03'),F('.02')),1:(F('-.057'),F('-.02'))}
def params(box,types):
 v=[]
 for j,(lo,hi)in enumerate(box):
  d=[arb(0)for _ in range(n)];d[j]=arb(1);v.append(D(ar(lo).union(ar(hi)),d))
 t=F(3,25)+F(1,10)*v[0];xn=t+(F(9,20)-t)*v[1];rt=(t-F(1,10))/F(3,25)
 tc,tn,to=types[2],types[1],types[0]
 hc=D(0) if tc==2 else H[tc][0]+(H[tc][1]-H[tc][0])*v[3];hn=D(0) if tn==2 else H[tn][0]+(H[tn][1]-H[tn][0])*v[4]
 if to==0:poly=[(t,F('-.03')*rt),(D('.22'),D('-.03')),(D('.45'),D('-.03')),(D('.45'),D('.02')),(D('.22'),D('.02')),(t,F('.02')*rt)]
 elif to==1:poly=[(t,F('-.057')*rt),(D('.22'),D('-.057')),(D('.45'),D('-.057')),(D('.45'),F('-.02')*rt),(t,F('-.02')*rt)]
 if to==2:poly=[(t,D('.014')),(D('.45'),D('.014'))]
 (x0,h0),(x1,h1)=poly[FACE],poly[(FACE+1)%len(poly)]
 xo=x0+v[2]*(x1-x0);ho=h0+v[2]*(h1-h0)
 xx=[xo,xn,t];yy=[ho,D('.014') if tn==2 else hn*rt,D('.014') if tc==2 else hc*rt]
 zz=[acb(x.v,y.v)for x,y in zip(xx,yy)]
 dz=[[acb(x.d[j],y.d[j])for j in range(n)]for x,y in zip(xx,yy)]
 return zz,dz,hc,hn

def gradH(s,a,b,eta,eps):
 gp=m.core.gp;gpp=m.gpp;sa=gpp(s+a)+2*pi*ii;sb=gpp(s+b);ss=m.second(s,a,b,eps)
 G=[gp(s+a)+2*pi*ii*s-(1+ar(F(eta,2)))*gp(a),gp(s+b)-(1+ar(F(eps,2)))*gp(b)]
 Hm=[[gpp(s+a)-(1+ar(F(eta,2)))*gpp(a)-sa*sa/ss,-sa*sb/ss],[-sa*sb/ss,gpp(s+b)-(1+ar(F(eps,2)))*gpp(b)-sb*sb/ss]]
 return G,Hm

def test(box,case,witness=None):
 types,side,chi,cin=case;to,tn,tc=map(lambda v:int(v>0),types);zz,dz,hc,hn=params(box,types);mid=[((a+b)/2,(a+b)/2)for a,b in box];z0,_,hc0,hn0=params(mid,types)
 if cin==0:
  edges=[(1,2,tn,tc)]if side==0 else[(2,1,tc,tn)];center_edge=0;center_index=1 if side==0 else 0;ng=[];sgn=1 if side==0 else -1
 elif side==0:edges=[(0,1,to,tn),(1,2,tn,tc)];center_edge,center_index=1,1;ng=[(0,1),(1,0)];sgn=1
 else:edges=[(2,1,tc,tn),(1,0,tn,to)];center_edge,center_index=0,0;ng=[(0,1),(1,0)];sgn=-1
 datas=[];wits=[]
 for j,(a,b,eta,eps)in enumerate(edges):
  p=root_box(zz[a],zz[b],z0[a],z0[b],eps,None if witness is None else witness[j])
  if p is None:return None,None,None
  z,zc,w=p;datas.append((gradH(z,zz[a],zz[b],eta,eps),gradH(zc,z0[a],z0[b],eta,eps)));wits.append(w)
 qc=1+ii*chi*hc.v/ar(F(3,25));qn=ii*cin*hn.v/ar(F(3,25));qc0=1+ii*chi*hc0.v/ar(F(3,25));qn0=ii*cin*hn0.v/ar(F(3,25))
 gc=datas[center_edge][0][0][center_index]+sgn*ii*ar(F(3,2));gc0=datas[center_edge][1][0][center_index]+sgn*ii*ar(F(3,2));Gn=sum((datas[k][0][0][l]for k,l in ng),acb(0));Gn0=sum((datas[k][1][0][l]for k,l in ng),acb(0))
 gauge=ar(F(sgn,10)) if types[2]==2 else arb(0)
 fc=(qc0*gc0+qn0*Gn0).real+gauge;fv=(qc*gc+qn*Gn).real+gauge
 grads=[]
 for j in range(n):
  dg=[]
  for (a,b,eta,eps),data in zip(edges,datas):
   HH=data[0][1];dg.append([HH[k][0]*dz[a][j]+HH[k][1]*dz[b][j]for k in(0,1)])
  dgc=dg[center_edge][center_index];dGn=sum((dg[k][l]for k,l in ng),acb(0))
  grads.append((ii*chi*hc.d[j]/ar(F(3,25))*gc+qc*dgc+ii*cin*hn.d[j]/ar(F(3,25))*Gn+qn*dGn).real)
 radii=[ar((b-a)/2)for a,b in box];lower=fc-sum((abs(v)*r for v,r in zip(grads,radii)),arb(0))
 if fv.lower()>lower.lower():lower=fv
 return lower,grads,wits

def choose(box,types,grads):
 if grads is not None:return max(((abs(grads[j]).upper()*ar(b-a)).upper(),j)for j,(a,b)in enumerate(box)if b>a)[1]
 zz,dz,_,_=params([((a+b)/2,(a+b)/2)for a,b in box],types)
 return max(((sum((abs(dz[k][j])for k in ([1,2] if case[3]==0 else [0,1,2])),arb(0)).upper()*ar(b-a)).upper(),j)for j,(a,b)in enumerate(box)if b>a)[1]
def specs():
 cases=[]
 for tc in (0,1,2):
  for side in (0,1):
   for chi in ((0,) if tc==2 else (0,1)):cases.append(([0,2,tc],side,chi,0,0))
 for tn,side in itertools.product((0,1),repeat=2):cases.append(([0,tn,2],side,0,0,0))
 for tn,side in itertools.product((0,1),repeat=2):
  for to in (0,1,2):
   for face in range((6,5,1)[to]):cases.append(([to,tn,2],side,0,1,face))
 for tn,tc,side,chi in itertools.product((0,1),repeat=4):cases.append(([2,tn,tc],side,chi,1,0))
 assert len(cases)==78 and len(set(map(str,cases)))==78
 return [list(v)for v in cases]

DEPS=[
 'experiments/certify_mixed_isolated_transition_phase.py',
 'experiments/certify_mixed_real_small_support.py',
 'notes/research_mixed_closed_cotangent_roots.md',
 'experiments/check_mixed_closed_cotangent_roots.py',
 'repro/results/research-mixed-closed-cotangent-roots.json',
 'notes/research_mixed_minimum_neighbor_contour.md',
 'experiments/check_mixed_minimum_neighbor_contour.py',
 'repro/results/research-mixed-minimum-neighbor-contour.json']
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def configure(bits):
 global pi,ii
 ctx.prec=bits;pi,ii=arb.pi(),acb(0,1);m.pi,m.ii=pi,ii;m.core.pi,m.core.ii=pi,ii

def check_record(stem,prefix):
 p=BASE/f'repro/results/research-{stem.replace("_","-")}.json';r=json.loads(p.read_text())
 assert r['status']=='passed'
 assert r['proof_sha256']==sha(BASE/f'notes/research_{stem}.md')
 assert r['script_sha256']==sha(BASE/f'experiments/{prefix}_{stem}.py')
 for key in ('dependencies','dependencies_sha256'):
  for q,h in r.get(key,{}).items():assert sha(BASE/q)==h,q

def exact_checks():
 import sympy as sy
 v,w,b,c,k,chi,xi,g=sy.symbols('v w b c k chi xi g',real=True)
 L=(1+sy.I*chi*b)*(v+sy.I*k)+sy.I*xi*c*w+g
 R=(1+sy.I*chi*b)*(w-sy.I*k)-g
 assert sy.expand(L+R-((1+sy.I*chi*b)*(v+w)+sy.I*xi*c*w))==0
 assert F(1,50)*50==1 and F(7,500)*50<F(57,1000)*20
 assert len(specs())==78 and len(set(map(str,specs())))==78
 assert sum(e[3]==0 for e in specs())==14
 assert sum(e[3]==1 and e[0][2]==2 for e in specs())==48
 assert sum(e[3]==1 and e[0][2]!=2 for e in specs())==16
 cot=(2*pi*ar('.014')).sinh()/((2*pi*ar('.014')).cosh()-(2*pi*ar('.12')).cos())
 assert cot<ar('1/2')
 # Selected actual heights stay H even though the coefficient of d rho is 0.
 global FACE
 FACE=0
 box=[(F(1,2),F(1,2))]*5
 zz,dz,hc,hn=params(box,[2,2,2])
 assert all(z.imag.contains(ar('.014')) for z in zz)
 assert hc.v==0 and hn.v==0 and all(d.imag.contains(0) for row in dz for d in row)
 return dict(exact_checks=7,scalar_checks=1,selected_cotangent_bound=str(cot.upper()))

def main():
 global FACE,case
 ap=argparse.ArgumentParser(description=__doc__)
 group=ap.add_mutually_exclusive_group(required=True)
 group.add_argument('--input',type=Path,help='Current canonical record binding the exact saved cover.')
 group.add_argument('--witnesses',type=Path,help='Untrusted proposal cover; all nodes are checked.')
 ap.add_argument('--precision',type=int,default=256)
 ap.add_argument('--output',type=Path,default=BASE/'repro/results/research-mixed-constant-selected-height-transport.json')
 args=ap.parse_args();assert args.precision>=160;configure(args.precision)
 ph,sh=sha(PROOF),sha(__file__);deps={p:sha(BASE/p)for p in DEPS}
 assert deps['experiments/certify_mixed_isolated_transition_phase.py']==ROOT_HELPER_SHA
 assert deps['experiments/certify_mixed_real_small_support.py']==m.HELPER_SHA
 for stem in ('mixed_closed_cotangent_roots','mixed_minimum_neighbor_contour'):check_record(stem,'check')
 checks=exact_checks();ih=None;saved=None
 if args.input:
  ih=sha(args.input);saved=json.loads(args.input.read_text());assert saved['status']=='passed'
  assert saved['proof_sha256']==ph and saved['script_sha256']==sh and saved['dependencies_sha256']==deps
  source=Path(saved['cover_path']);source=source if source.is_absolute()else BASE/source
  assert sha(source)==saved['cover_sha256']
 else:source=args.witnesses
 cover_hash=sha(source);start=time.time();rows=[];totalvis=totalaccepted=totalmonotonic=0;minimum=None
 with gzip.open(source,'rt')as stream:
  for number,entry in enumerate(specs()):
   line=stream.readline();assert line,(number,'missing domain')
   data=json.loads(line);assert data['case']==entry
   case=entry[:4];FACE=entry[4];nodes=iter(data['nodes']);stack=[[(F(0),F(1))for _ in range(n)]]
   visits=accepted=monotonic=0;lo=None
   while stack:
    box=stack.pop();visits+=1;node=next(nodes)
    if node[0]=='S':
     assert len(node)==2 and type(node[1])is int and 0<=node[1]<n
     j=node[1];a,b=box[j];assert a<b;mid=(a+b)/2
     for pair in ((a,mid),(mid,b)):
      bb=list(box);bb[j]=pair;stack.append(bb)
     continue
    assert node[0]in('L','M')
    supplied=node[-1]
    assert isinstance(supplied,list)and len(supplied)==(1 if case[3]==0 else 2)
    assert all(isinstance(w,dict)and set(w)=={'center','derivatives','radius'}for w in supplied)
    lower,grads,wits=test(box,case,supplied)
    assert lower is not None,(number,visits,'root witness')
    if node[0]=='L':
     assert len(node)==2 and lower>0,(number,visits,'positive half',lower)
     accepted+=1;lo=lower.lower()if lo is None else min(lo,lower.lower())
    else:
     assert len(node)==4
     j,bit=node[1:3];assert type(j)is int and 0<=j<n and bit in(0,1)
     assert box[j][0]<box[j][1]and (grads[j]>0 if bit==0 else grads[j]<0),(number,visits,'monotonicity')
     bb=list(box);end=box[j][bit];bb[j]=(end,end);stack.append(bb);monotonic+=1
   assert next(nodes,None)is None,(number,'unused tree nodes')
   assert visits==data['visits']and accepted==data['accepted']and monotonic==data['monotonic_reductions']
   totalvis+=visits;totalaccepted+=accepted;totalmonotonic+=monotonic
   minimum=lo if minimum is None else min(minimum,lo)
   rows.append(dict(case=entry,accepted=accepted,visits=visits,monotonic_reductions=monotonic,minimum=str(lo)))
   print('PASS domain',number+1,78,'leaves',accepted,'monotonic',monotonic,'minimum',lo,'elapsed',time.time()-start,flush=True)
  assert not stream.read().strip(),'extra domains'
 assert ph==sha(PROOF)and sh==sha(__file__)and deps=={p:sha(BASE/p)for p in DEPS}and cover_hash==sha(source)
 if args.input:assert ih==sha(args.input)
 try:sourcepath=str(source.resolve().relative_to(BASE))
 except ValueError:sourcepath=str(source.resolve())
 out=dict(status='passed',precision_bits=args.precision,domains=78,cells=totalaccepted,visits=totalvis,monotonic_reductions=totalmonotonic,minimum_half=str(minimum),cases=rows,proof_sha256=ph,script_sha256=sh,dependencies_sha256=deps,cover_path=sourcepath,cover_sha256=cover_hash,elapsed_seconds=time.time()-start,**checks,scope='78 new constant-selected-height phase-derivative half stencils; no new finite source or whole-period selected bound.')
 if args.input:out.update(input_path=str(args.input),input_sha256=ih)
 args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(out,indent=2)+'\n')
 print('FULL PASS',78,totalaccepted,totalmonotonic,checks,flush=True)
if __name__=='__main__':main()
