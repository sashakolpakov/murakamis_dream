#!/usr/bin/env python3
"""Saved-cover proof of the unselected minimum-level half-stencil inequalities."""
import argparse,gzip,hashlib,importlib.util,json,time,sys,itertools,math,tempfile
from concurrent.futures import ProcessPoolExecutor,as_completed
from pathlib import Path
from fractions import Fraction as F
from flint import arb,acb,ctx
BASE=Path(__file__).resolve().parents[1]
PROOF=BASE/'notes/research_mixed_minimum_level_half_stencils.md'
sp=importlib.util.spec_from_file_location('half_root',BASE/'experiments/certify_mixed_isolated_transition_phase.py');m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m)
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
H={0:(F('-.03'),F('.02')),1:(F('-.057'),F('-.02'))}
def params(box,types):
 v=[]
 for j,(lo,hi)in enumerate(box):
  d=[arb(0)for _ in range(n)];d[j]=arb(1);v.append(D(ar(lo).union(ar(hi)),d))
 t=F(1,10)+F(3,25)*v[0];xn=t+(F(9,20)-t)*v[1];rt=(t-F(1,10))/F(3,25)
 tc,tn,to=types[2],types[1],types[0]
 hc=H[tc][0]+(H[tc][1]-H[tc][0])*v[3];hn=H[tn][0]+(H[tn][1]-H[tn][0])*v[4]
 if to==0:poly=[(t,F('-.03')*rt),(D('.22'),D('-.03')),(D('.45'),D('-.03')),(D('.45'),D('.02')),(D('.22'),D('.02')),(t,F('.02')*rt)]
 else:poly=[(t,F('-.057')*rt),(D('.22'),D('-.057')),(D('.45'),D('-.057')),(D('.45'),F('-.02')*rt),(t,F('-.02')*rt)]
 (x0,h0),(x1,h1)=poly[FACE],poly[(FACE+1)%len(poly)]
 xo=x0+v[2]*(x1-x0);ho=h0+v[2]*(h1-h0)
 xx=[xo,xn,t];yy=[ho,hn*rt,hc*rt]
 zz=[acb(x.v,y.v)for x,y in zip(xx,yy)]
 dz=[[acb(x.d[j],y.d[j])for j in range(n)]for x,y in zip(xx,yy)]
 return zz,dz,hc,hn

def gradH(s,a,b,eta,eps):
 gp=m.core.gp;gpp=m.gpp;sa=gpp(s+a)+2*pi*ii;sb=gpp(s+b);ss=m.second(s,a,b,eps)
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
 ctx.prec=bits;pi,ii=arb.pi(),acb(0,1);m.pi,m.ii=pi,ii;m.core.pi,m.core.ii=pi,ii

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

DEPS=[
 'experiments/certify_mixed_isolated_transition_phase.py',
 'experiments/certify_mixed_real_small_support.py',
 'notes/research_mixed_global_cotangent_roots.md',
 'experiments/check_mixed_global_cotangent_roots.py',
 'repro/results/research-mixed-global-cotangent-roots.json',
 'notes/research_mixed_minimum_neighbor_contour.md',
 'experiments/check_mixed_minimum_neighbor_contour.py',
 'repro/results/research-mixed-minimum-neighbor-contour.json',
 'notes/research_mixed_minimum_level_transport.md']

def main():
 parser=argparse.ArgumentParser(description=__doc__)
 parser.add_argument('--precision',type=int,default=256);parser.add_argument('--jobs',type=int,default=4)
 parser.add_argument('--input',type=Path);parser.add_argument('--seed-directory',type=Path)
 parser.add_argument('--max-visits',type=int,default=2000000)
 parser.add_argument('--output',type=Path,default=BASE/'repro/results/research-mixed-minimum-level-half-stencils.json')
 parser.add_argument('--limit',type=int,default=192)
 args=parser.parse_args();assert args.precision>=160 and 1<=args.jobs<=8 and 1<=args.limit<=192
 assert not(args.input and args.seed_directory)
 configure(args.precision);ph,sh=sha(PROOF),sha(__file__);dependencies={p:sha(BASE/p)for p in DEPS}
 for stem in('global_cotangent_roots','minimum_neighbor_contour'):
  pp=f'notes/research_mixed_{stem}.md';ss=f'experiments/check_mixed_{stem}.py';rr=f'repro/results/research-mixed-{stem.replace("_","-")}.json'
  rec=json.loads((BASE/rr).read_text());assert rec['status']=='passed'and rec['proof_sha256']==dependencies[pp]and rec['script_sha256']==dependencies[ss]
  for key in('dependencies','dependencies_sha256'):
   for path,digest in rec.get(key,{}).items():assert sha(BASE/path)==digest,(stem,path)
 start=time.time();all_specs=specs();specifications=all_specs[:args.limit];ih=sha(args.input)if args.input else None
 args.output.parent.mkdir(parents=True,exist_ok=True)
 with tempfile.TemporaryDirectory(prefix='mixed-half-stencils-')as work:
  work=Path(work);seed=args.seed_directory
  if args.input:
   previous=json.loads(args.input.read_text());assert previous['status']=='passed'and previous['domains']==192
   assert previous['proof_sha256']==ph and previous['script_sha256']==sh
   cover=BASE/previous['cover_path'];assert sha(cover)==previous['cover_sha256']
   assert previous['dependencies_sha256']==dict(dependencies,**{str(cover.relative_to(BASE)):sha(cover)})
   seed=work/'input';seed.mkdir()
   with gzip.open(cover,'rt')as stream:
    for j,entry in enumerate(all_specs):
     row=json.loads(next(stream));assert row['case']==entry
     with gzip.open(seed/f'{j:03d}.json.gz','wt')as out:json.dump(row,out,separators=(',',':'))
    assert next(stream,None)is None
  rows={};jobs=[(j,entry,str(seed/f'{j:03d}.json.gz')if seed else None,str(work/f'{j:03d}.json.gz'),args.max_visits)for j,entry in enumerate(specifications)]
  with ProcessPoolExecutor(max_workers=args.jobs,initializer=configure,initargs=(args.precision,))as pool:
   for future in as_completed([pool.submit(certify_domain,job)for job in jobs]):
    j,row=future.result();rows[j]=row
    print('PASS domain',j+1,'completed',len(rows),'/',len(jobs),'leaves',row['accepted'],'visits',row['visits'],'seconds',round(time.time()-start,2),flush=True)
  assert set(rows)==set(range(args.limit))
  if not args.input:
   cover=args.output.with_name(args.output.stem+'-cover.jsonl.gz')
   with gzip.open(cover,'wt')as out:
    for j in range(args.limit):
     with gzip.open(work/f'{j:03d}.json.gz','rt')as inp:out.write(inp.read());out.write('\n')
  ch=sha(cover)
  try:cp=str(cover.relative_to(BASE));dependencies[cp]=ch
  except ValueError:cp=str(cover)
  if args.input:assert ih==sha(args.input)and ch==previous['cover_sha256']
  assert ph==sha(PROOF)and sh==sha(__file__)
  for path,digest in dependencies.items():assert sha(BASE/path)==digest,path
  result=dict(status='passed'if args.limit==192 else'partial-domain-passed',precision_bits=args.precision,domains=args.limit,
   accepted=sum(r['accepted']for r in rows.values()),visited=sum(r['visits']for r in rows.values()),monotonic_reductions=sum(r['monotonic_reductions']for r in rows.values()),
   cases=[rows[j]for j in range(args.limit)],cover_path=cp,cover_sha256=ch,proof_sha256=ph,script_sha256=sh,dependencies_sha256=dependencies,
   elapsed_seconds=time.time()-start,input_sha256=ih,scope='Original unselected minimum-level local derivative inequalities via192 exact half-stencil domains. No selected-height or full finite-source inference.')
  args.output.write_text(json.dumps(result,indent=2)+'\n')
  print('FULL PASS'if args.limit==192 else'PARTIAL PASS',args.limit,result['accepted'],result['visited'],flush=True)
if __name__=='__main__':main()
