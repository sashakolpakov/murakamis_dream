#!/usr/bin/env python3
"""Independent sine-logarithm/rectangle-extremum replay of the half-stencil cover."""
import argparse,gzip,hashlib,importlib.util,json,time,sys,itertools,math,tempfile
from concurrent.futures import ProcessPoolExecutor,as_completed
from pathlib import Path
from fractions import Fraction as F
from flint import arb,acb,ctx
BASE=Path(__file__).resolve().parents[1]
PROOF=BASE/'notes/research_mixed_minimum_level_half_stencils.md'
ctx.prec=192;pi=arb.pi();ii=acb(0,1);n=5

def ar(value):
 value=F(value);return arb(value.numerator)/value.denominator

def sine(z):return acb((pi*z.real).sin()*(pi*z.imag).cosh(),(pi*z.real).cos()*(pi*z.imag).sinh())
def cot(z):
 x,y=2*pi*z.real,2*pi*z.imag;den=y.cosh()-x.cos()
 return acb(x.sin()/den,-y.sinh()/den)
def logsine(z):return (2*sine(z)).log()
def gp(z):
 # Exact extrema of log|1-R exp(-2pi i x)| and its continuous argument
 # on the enclosing real x/R rectangle. Root equations still use logsine.
 xl,xh=z.real.lower(),z.real.upper();yl,yh=z.imag.lower(),z.imag.upper()
 assert xl>0 and xh<1
 rl=(2*pi*yl).exp().lower();rh=(2*pi*yh).exp().upper()
 cc=[(2*pi*x).cos()for x in(xl,xh)]
 clo=arb(-1)if xl<=ar('1/2')<=xh else min(v.lower()for v in cc)
 chi=max(v.upper()for v in cc)
 near=rl-chi if chi<rl else chi-rh if chi>rh else arb(0)
 ml=(1-chi*chi+near*near).lower()
 mh=max((1+r*r-2*r*clo).upper()for r in(rl,rh))
 if not ml>0:return acb(arb.nan(),arb.nan())
 real=(ml.log()/2).union(mh.log()/2)
 angles=[]
 for r in(rl,rh):
  for x in(xl,xh):angles.append(acb(1-r*(2*pi*x).cos(),r*(2*pi*x).sin()).arg())
  if r<1:
   root=r.acos()/(2*pi);angle=r.asin()
   if not(root.upper()<xl or root.lower()>xh):angles.append(angle)
   other=1-root
   if not(other.upper()<xl or other.lower()>xh):angles.append(-angle)
 imag=min(v.lower()for v in angles).union(max(v.upper()for v in angles))
 return acb(real,imag)

def gpp(z):return pi*cot(z)-pi*ii
def second(s,a,b,eps):return pi*(cot(s+a)+cot(s+b)-(2+eps)*cot(s))+eps*pi*ii
def equation(s,a,b,eps):return logsine(s+a)+logsine(s+b)-(2+eps)*logsine(s)+pi*ii*(a-b+eps*(s-ar('1/2')))
def proposal(*args):raise AssertionError('no root proposals in independent replay')
def point_root(a,b,eps,center):
 c=acb(ar(center[0]),ar(center[1]));Y=1/second(c,a,b,eps);r=ar('1e-12');z=c+acb(arb(0,r),arb(0,r))
 if not abs(Y*equation(c,a,b,eps))+abs(1-Y*second(z,a,b,eps))*r<r:return None
 S=cot(z)
 if not(S.real>0 and abs(S.imag)<1 and all(0<w.real<1 for w in(z,z+a,z+b))):return None
 return z,center
def root_box(a, b, a0, b0, eps, witness=None):
    assert witness is not None
    center = witness["center"]
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
        return pi*pi*abs(1/sine(w)**2)*abs(delta)**2/2

    err = abs(Y)*(abs(lin)+rem(z0+a0, dz+dp[0])+rem(z0+b0, dz+dp[1])+(2+eps)*rem(z0, dz))
    if not err.is_finite():
        return None
    radius = F(witness["radius"]) if witness is not None else F(max(1, math.ceil(float(err.upper())*4*2**42)), 2**42)
    if radius > F(1, 20):
        return None
    delta = dz+acb(arb(0, ar(radius)), arb(0, ar(radius)))
    z = z0+delta
    # On 0<x<1/2, Re cot(pi*(x+iy))>0. Its imaginary part has
    # modulus<1 iff cos(2*pi*x)<exp(-2*pi*abs(y)). This exact
    # scalar criterion avoids dependency inflation in sinh/denominator.
    height=max(abs(z.imag.lower()),abs(z.imag.upper()))
    cone=(2*pi*z.real.lower()).cos() < (-2*pi*height).exp()
    if not (0 < z.real < ar(F(1,2)) and cone):
        return None
    if not all(0 < w.real < 1 for w in (z, z+a, z+b)):
        return None

    def dc(base, move):
        return -pi*sine(move)/(sine(base)*sine(base+move))

    defect = 1-Y*H0-Y*(dc(z0+a0, delta+dp[0])+dc(z0+b0, delta+dp[1])-(2+eps)*dc(z0, delta))
    if not err+abs(defect)*ar(radius) < ar(radius):
        return None
    pr = point_root(a0, b0, eps, center)
    if pr is None:
        return None
    return z, pr[0], {"center": center, "derivatives": dd, "radius": str(radius)}

class Parameter:
 def __init__(self,value,derivatives):self.v=value;self.d=derivatives
H={0:(F('-.03'),F('.02')),1:(F('-.057'),F('-.02'))}
def params(box,types):
 v=[ar(a).union(ar(b))for a,b in box];to,tn,tc=types
 t=ar('.1')+ar('.12')*v[0];x=t+(ar('.45')-t)*v[1]
 hc=ar(H[tc][0])+ar(H[tc][1]-H[tc][0])*v[3];hn=ar(H[tn][0])+ar(H[tn][1]-H[tn][0])*v[4]
 if to==0:
  bases=[acb(ar('.1')),acb(ar('.22'),ar('-.03')),acb(ar('.45'),ar('-.03')),acb(ar('.45'),ar('.02')),acb(ar('.22'),ar('.02')),acb(ar('.1'))]
  slopes=[acb(ar('.12'),ar('-.03')),acb(0),acb(0),acb(0),acb(0),acb(ar('.12'),ar('.02'))]
 else:
  bases=[acb(ar('.1')),acb(ar('.22'),ar('-.057')),acb(ar('.45'),ar('-.057')),acb(ar('.45')),acb(ar('.1'))]
  slopes=[acb(ar('.12'),ar('-.057')),acb(0),acb(0),acb(0,ar('-.02')),acb(ar('.12'),ar('-.02'))]
 j=FACE;k=(j+1)%len(bases);start=bases[j]+slopes[j]*v[0];end=bases[k]+slopes[k]*v[0]
 zo=start+v[2]*(end-start);zn=acb(x,hn*v[0]);zc=acb(t,hc*v[0])
 dz=[[acb(0)for _ in range(5)]for _ in range(3)]
 dz[0][0]=slopes[j]+v[2]*(slopes[k]-slopes[j]);dz[0][2]=(bases[k]-bases[j])+(slopes[k]-slopes[j])*v[0]
 dz[1][0]=acb(ar('.12')*(1-v[1]),hn);dz[1][1]=acb(ar('.45')-t);dz[1][4]=acb(0,ar(H[tn][1]-H[tn][0])*v[0])
 dz[2][0]=acb(ar('.12'),hc);dz[2][3]=acb(0,ar(H[tc][1]-H[tc][0])*v[0])
 dhc=[arb(0)for _ in range(5)];dhn=dhc.copy();dhc[3]=ar(H[tc][1]-H[tc][0]);dhn[4]=ar(H[tn][1]-H[tn][0])
 return [zo,zn,zc],dz,Parameter(hc,dhc),Parameter(hn,dhn)

def gradH(s,a,b,eta,eps):
 sa=gpp(s+a)+2*pi*ii;sb=gpp(s+b);ss=second(s,a,b,eps)
 G=[gp(s+a)+2*pi*ii*s-(1+ar(F(eta,2)))*gp(a),gp(s+b)-(1+ar(F(eps,2)))*gp(b)]
 Hm=[[gpp(s+a)-(1+ar(F(eta,2)))*gpp(a)-sa*sa/ss,-sa*sb/ss],[-sa*sb/ss,gpp(s+b)-(1+ar(F(eps,2)))*gpp(b)-sb*sb/ss]]
 return G,Hm

def test(box,case,witness=None):
 types,side,chi,cin=case;to,tn,tc=types;zz,dz,hc,hn=params(box,types);mid=[((a+b)/2,(a+b)/2)for a,b in box];z0,_,hc0,hn0=params(mid,types)
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
 fc=(qc0*gc0+qn0*Gn0).real;fv=(qc*gc+qn*Gn).real
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
 if grads is not None:return max((abs(grads[j]).upper()*ar(b-a),j)for j,(a,b)in enumerate(box)if b>a)[1]
 zz,dz,_,_=params([((a+b)/2,(a+b)/2)for a,b in box],types)
 return max((sum((abs(dz[k][j])for k in ([1,2] if case[3]==0 else [0,1,2])),arb(0)).upper()*ar(b-a),j)for j,(a,b)in enumerate(box)if b>a)[1]

def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def configure(bits):
 global pi,ii
 ctx.prec=bits;pi,ii=arb.pi(),acb(0,1)

def specs():
 ans=[]
 for tn,tc,side,chi in itertools.product((0,1),repeat=4):ans.append([[0,tn,tc],side,chi,0,0])
 for to,tn,tc,side,chi in itertools.product((0,1),repeat=5):
  for face in range(6 if to==0 else 5):ans.append([[to,tn,tc],side,chi,1,face])
 assert len(ans)==192
 return ans

def unpack_cover(row):
 if 'witness_pool'not in row:return row
 assert row.get('cover_schema')==2
 pool=row['witness_pool'];used=set();nodes=[]
 for node in row['nodes']:
  if node[0]=='S':nodes.append(node);continue
  ids=node[-1];assert len(ids)==(1 if row['case'][3]==0 else 2)
  assert all(type(j)is int and 0<=j<len(pool)for j in ids)
  used.update(ids);nodes.append(node[:-1]+[[pool[j]for j in ids]])
 assert used==set(range(len(pool)))
 return dict(row,nodes=nodes)

def pack_cover(row):
 pool=[];lookup={};nodes=[]
 for node in row['nodes']:
  if node[0]=='S':nodes.append(node);continue
  ids=[]
  for witness in node[-1]:
   key=json.dumps(witness,sort_keys=True,separators=(',',':'))
   if key not in lookup:lookup[key]=len(pool);pool.append(witness)
   ids.append(lookup[key])
  nodes.append(node[:-1]+[ids])
 return dict(row,nodes=nodes,witness_pool=pool,cover_schema=2)

def certify_domain(job):
 global case,FACE
 number,entry,source,dest,max_visits=job;case=entry[:4];FACE=entry[4]
 assert source is not None
 ih=sha(source)if source else None
 if source:
  with gzip.open(source,'rt')as stream:saved=unpack_cover(json.load(stream))
  assert saved['case']==entry
  supplied=iter(saved['nodes'])
 else:supplied=None
 stack=[[(F(0),F(1))for _ in range(n)]];nodes=[];visits=accepted=monotonic=0;minimum=None
 while stack:
  box=stack.pop();visits+=1;assert visits<=max_visits,(number,visits)
  node=next(supplied)if supplied is not None else None
  if node is not None and node[0]=='S':
   assert len(node)==2 and type(node[1])is int and 0<=node[1]<n
   j=node[1];a,b=box[j];assert a<b;mid=(a+b)/2
   for pair in((a,mid),(mid,b)):
    child=list(box);child[j]=pair;stack.append(child)
   nodes.append(node);continue
  witness=None if node is None else node[-1]
  lower,grads,wit=test(box,case,witness)
  if node is not None:
   assert lower is not None,(number,visits,'root witness')
   if node[0]=='L':
    assert len(node)==2 and lower>0,(number,visits,'leaf lower bound',lower)
    accepted+=1;minimum=lower.lower()if minimum is None else min(minimum,lower.lower());nodes.append(node)
   else:
    assert node[0]=='M'and len(node)==4
    j,bit=node[1:3];assert type(j)is int and 0<=j<n and bit in(0,1)
    assert box[j][0]<box[j][1]and (grads[j]>0 if bit==0 else grads[j]<0),(number,visits,'monotonic derivative')
    child=list(box);end=box[j][bit];child[j]=(end,end);stack.append(child);nodes.append(node);monotonic+=1
   continue
  if lower is not None and lower>0:
   accepted+=1;minimum=lower.lower()if minimum is None else min(minimum,lower.lower());nodes.append(['L',wit]);continue
  options=[]
  if grads is not None:
   for j,((a,b),v)in enumerate(zip(box,grads)):
    if a==b:continue
    if v>0:options.append(((abs(v).lower()*ar(b-a)).lower(),j,0))
    elif v<0:options.append(((abs(v).lower()*ar(b-a)).lower(),j,1))
  if options:
   _,j,bit=max(options);end=box[j][bit];child=list(box);child[j]=(end,end);stack.append(child);nodes.append(['M',j,bit,wit]);monotonic+=1
  else:
   j=choose(box,case[0],grads);a,b=box[j];assert b-a>F(1,2**24);mid=(a+b)/2;nodes.append(['S',j])
   for pair in((a,mid),(mid,b)):
    child=list(box);child[j]=pair;stack.append(child)
 if supplied is not None:
  assert next(supplied,None)is None,'unconsumed tree nodes'
  assert ih==sha(source),'input changed'
 row=dict(case=entry,accepted=accepted,visits=visits,monotonic_reductions=monotonic,minimum=str(minimum))
 with gzip.open(dest,'wt')as stream:json.dump(pack_cover(dict(**row,nodes=nodes)),stream,separators=(',',':'))
 return number,row


def exact_range_identities():
 import sympy as sy
 r,c,t=sy.symbols('r c t',real=True);z=1-r*c+sy.I*r*t
 radial=sy.expand(sy.im((-c+sy.I*t)*sy.conjugate(z)))
 angular=sy.expand(sy.im((r*t+sy.I*r*c)*sy.conjugate(z)))
 assert sy.expand(radial-t)==0
 assert sy.expand(angular-r*(c-r)+r*r*(c*c+t*t-1))==0
 y=sy.symbols('y',real=True)
 assert sy.simplify(sy.cosh(y)-sy.sinh(y)-sy.exp(-y))==0
 return 3

def main():
 parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--precision',type=int,default=320);parser.add_argument('--jobs',type=int,default=4)
 parser.add_argument('--input',type=Path,default=BASE/'repro/results/research-mixed-minimum-level-half-stencils.json')
 parser.add_argument('--output',type=Path,default=BASE/'repro/results/research-mixed-minimum-level-half-stencils-replay.json')
 parser.add_argument('--resume',type=Path,help='Explicit hash-bound partial results of the original independent worker; omitted domains are freshly replayed.')
 args=parser.parse_args();assert args.precision>=256 and 1<=args.jobs<=8;configure(args.precision)
 identities=exact_range_identities()
 ph,sh,ih=sha(PROOF),sha(__file__),sha(args.input);author=BASE/'experiments/certify_mixed_minimum_level_half_stencils.py';ah=sha(author)
 previous=json.loads(args.input.read_text());assert previous['status']=='passed'and previous['domains']==192
 assert previous['proof_sha256']==ph and previous['script_sha256']==ah
 deps=dict(previous['dependencies_sha256'])
 for p,h in deps.items():assert sha(BASE/p)==h,p
 cover=BASE/previous['cover_path'];ch=sha(cover);assert ch==previous['cover_sha256']
 for p in(author,args.input,PROOF):
  try:deps[str(p.relative_to(BASE))]=sha(p)
  except ValueError:pass
 specifications=specs();start=time.time();resumed={};resume_hash=None
 if args.resume is not None:
  resume_hash=sha(args.resume);partial=json.loads(args.resume.read_text())
  assert partial['status']=='passed_partial'and partial['precision_bits']>=args.precision and partial['expected_domains']==192
  assert partial['author_record_sha256']==ih and partial['proof_sha256']==ph and partial['cover_sha256']==ch
  capture=BASE/'experiments/capture_mixed_half_stencil_partial_replay.py'
  assert partial['script_sha256']==sha(capture)
  snapshot=BASE/partial['numerical_script_path'];assert partial['numerical_script_sha256']==sha(snapshot)
  for p,h in partial['dependencies_sha256'].items():assert sha(BASE/p)==h,p
  for row in partial['cases']:
   j=row['index'];assert type(j)is int and 0<=j<192 and j not in resumed
   assert row['case']==specifications[j]and arb(row['minimum'])>0
   assert all(row[k]==previous['cases'][j][k]for k in ('accepted','visits','monotonic_reductions'))
   resumed[j]=row
  assert len(resumed)==partial['domains']
  assert all(sum(v[k]for v in resumed.values())==partial[k if k!='visits'else'visited']for k in ('accepted','visits','monotonic_reductions'))
  for p in (capture,snapshot,args.resume):
   try:deps[str(p.relative_to(BASE))]=sha(p)
   except ValueError:pass
  print('RESUME',len(resumed),'original-code domains;',192-len(resumed),'domains require refined-cone numerical replay',flush=True)
 with tempfile.TemporaryDirectory(prefix='mixed-half-independent-')as work:
  work=Path(work)
  with gzip.open(cover,'rt')as stream:
   for j,entry in enumerate(specifications):
    row=json.loads(next(stream));assert row['case']==entry
    if j in resumed:
     digest=hashlib.sha256(json.dumps(row,sort_keys=True,separators=(',',':')).encode()).hexdigest()
     assert digest==resumed[j]['canonical_tree_sha256']
     continue
    with gzip.open(work/f'{j:03d}.json.gz','wt')as out:json.dump(row,out,separators=(',',':'))
   assert next(stream,None)is None
  jobs=[(j,entry,str(work/f'{j:03d}.json.gz'),str(work/f'{j:03d}-checked.json.gz'),2000000)for j,entry in enumerate(specifications)if j not in resumed];rows={j:dict(row,method='original_independent_cone')for j,row in resumed.items()}
  with ProcessPoolExecutor(max_workers=args.jobs,initializer=configure,initargs=(args.precision,))as pool:
   futures={pool.submit(certify_domain,job):job[0]for job in jobs}
   for future in as_completed(futures):
    try:j,row=future.result()
    except BaseException:
     print('FAILED DOMAIN',futures[future]+1,flush=True)
     raise
    rows[j]=dict(row,method='refined_exact_cone');print('REPLAY',j+1,'completed',len(rows),'/192','leaves',row['accepted'],'seconds',round(time.time()-start,2),flush=True)
  assert set(rows)==set(range(192))
 assert ph==sha(PROOF)and sh==sha(__file__)and ah==sha(author)and ih==sha(args.input)and ch==sha(cover)
 for p,h in deps.items():assert sha(BASE/p)==h,p
 if args.resume is not None:assert resume_hash==sha(args.resume)
 assert all(sum(v[k]for v in rows.values())==previous[k if k!='visits'else'visited']for k in ('accepted','visits','monotonic_reductions'))
 out=dict(status='passed',precision_bits=args.precision,exact_range_identities=identities,domains=192,accepted=sum(v['accepted']for v in rows.values()),visited=sum(v['visits']for v in rows.values()),
  monotonic_reductions=sum(v['monotonic_reductions']for v in rows.values()),cases=[rows[j]for j in range(192)],proof_sha256=ph,script_sha256=sh,input_sha256=ih,cover_sha256=ch,dependencies_sha256=deps,elapsed_seconds=time.time()-start,
  resumed_domains=len(resumed),fresh_domains=192-len(resumed),resume_record_sha256=resume_hash,
  scope='Independent original sine-logarithm roots, real cotangents and exact scalar log/argument extrema, explicit parameter derivatives, complete saved split/monotonic trees. Optional original-code domain results are separately hash-bound; every remaining domain uses the exact scalar cotangent-cone refinement. No root proposals, author imports or selected-height assertion.')
 args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(out,indent=2)+'\n');print('PASS192',out['accepted'],out['visited'],flush=True)
if __name__=='__main__':main()
