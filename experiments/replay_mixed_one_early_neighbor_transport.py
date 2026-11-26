#!/usr/bin/env python3
"""Independent saved-cover replay of all one-early-neighbor half stencils.

Every original sine-log root witness and complete split/monotonicity tree
is verified; no root proposal or sampled minimum is an acceptance test.
"""
import argparse,gzip,hashlib,importlib.util,itertools,json,math,time,tempfile
from concurrent.futures import ProcessPoolExecutor,as_completed
from pathlib import Path
from fractions import Fraction as F
from flint import arb,acb,ctx
BASE=Path(__file__).resolve().parents[1]
PROOF=BASE/'notes/research_mixed_one_early_neighbor_transport.md'
LIB=BASE/'experiments/replay_mixed_constant_selected_height_transport.py'
LIB_SHA=hashlib.sha256(LIB.read_bytes()).hexdigest()
sp=importlib.util.spec_from_file_location('one_early_independent_arithmetic',LIB);m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m)
assert LIB_SHA==hashlib.sha256(LIB.read_bytes()).hexdigest()
ar=m.ar;n=5
H={0:(F('-.03'),F('.02')),1:(F('-.057'),F('-.02'))}
SMALL={0:(F('-.005'),F(1,300)),1:(F('-.0095'),F('.014'))}
EARLY={0:(F('-.25'),F(1,6)),1:(F('-.475'),F('.7'))}
CIM={'000':('-.01','.01'),'001':('-.017','-.002'),'010':('-.049','-.03'),'011':('-.057','-.043'),'100':('-.017','.002'),'101':('-.025','-.011'),'110':('-.054','-.036'),'111':('-.062','-.049')}

def coefficient_interval(center,neighbor,outer,side):
 word=(outer,neighbor,center)if side==0 else(center,neighbor,outer)
 lo,hi=map(F,CIM[''.join(map(str,word))]);lo=max(H[neighbor][0],lo);hi=min(H[neighbor][1],hi)
 if neighbor==1 and((side==0 and center==1)or(side==1 and outer==1)):hi=min(hi,F('-.048'))
 if center==neighbor==outer==1:hi=min(hi,F('-.053'))
 assert lo<hi
 return lo,hi

def center_interval(kind,center,side,sign):
 lo,hi=EARLY[1]if kind==0 and center==1 and side==1 else SMALL[center]
 if sign<0:hi=F(0)
 if sign>0:lo=F(0)
 return lo,hi

def parameter(value,derivative=None):
 return m.Parameter(value,derivative if derivative is not None else[arb(0)for _ in range(n)])

def polygon(typ,t,rt,lower=None):
 low=H[typ][0]if lower is None else lower
 bottom=acb(t,ar(low)*rt);db=acb(ar('.1'),ar(low)*ar('5/6'))
 if typ==0:
  z=[bottom,acb(ar('.22'),ar(low)),acb(ar('.45'),ar(low)),acb(ar('.45'),ar('.02')),acb(ar('.22'),ar('.02')),acb(t,ar('.02')*rt)]
  d=[db,acb(0),acb(0),acb(0),acb(0),acb(ar('.1'),ar('.02')*ar('5/6'))]
 else:
  z=[bottom,acb(ar('.22'),ar(low)),acb(ar('.45'),ar(low)),acb(ar('.45'),ar('.014')),acb(t,ar('.014'))]
  d=[db,acb(0),acb(0),acb(0),acb(ar('.1'))]
 return z,d

def params(box,case):
 kind,center,neighbor,outer,side,sign,face=case
 v=[ar(a).union(ar(b))for a,b in box]
 lo,hi=center_interval(kind,center,side,sign);hv=ar(lo)+ar(hi-lo)*v[3]
 dh=[arb(0)for _ in range(n)];dh[3]=ar(hi-lo)
 cn=parameter(arb(0));dz=[[acb(0)for _ in range(n)]for _ in range(3)]
 if kind==0:
  u=ar('.02')*v[0];el,eh=EARLY[neighbor];ce=ar(el)+ar(eh-el)*v[1]
  he=ce*u;zz=[acb(ar('.45')),acb(ar('.1')+u,he),acb(ar('.22'),hv)]
  dz[1][0]=acb(ar('.02'),ce*ar('.02'));dz[1][1]=acb(0,ar(eh-el)*u)
  if center==1 and side==1:
   hv=hv*u;dh[0]=(ar(lo)+ar(hi-lo)*v[3])*ar('.02');dh[3]=ar(hi-lo)*u
   zz[2]=acb(ar('.22'),hv)
  for j in range(n):dz[2][j]=acb(0,dh[j])
 else:
  t=ar('.12')+ar('.1')*v[0];rt=ar('1/6')+ar('5/6')*v[0]
  zz=[acb(ar('.45')),acb(0),acb(t,hv)];dz[2][0]=acb(ar('.1'));dz[2][3]=acb(0,dh[3])
  if kind==1:
   z,p=polygon(neighbor,t,rt);j=(face+1)%len(z)
   zz[1]=z[face]+v[2]*(z[j]-z[face])
   dz[1][0]=p[face]+v[2]*(p[j]-p[face]);dz[1][2]=z[j]-z[face]
  else:
   nl,nh=coefficient_interval(center,neighbor,outer,side);cv=ar(nl)+ar(nh-nl)*v[4]
   cd=[arb(0)for _ in range(n)];cd[4]=ar(nh-nl);cn=parameter(cv,cd)
   xn=t+(ar('.45')-t)*v[1];zz[1]=acb(xn,cv*rt)
   dz[1][0]=acb(ar('.1')*(1-v[1]),cv*ar('5/6'));dz[1][1]=acb(ar('.45')-t);dz[1][4]=acb(0,ar(nh-nl)*rt)
   low=F('-.025')if outer==0 and neighbor==1 else None
   z,p=polygon(outer,t,rt,low);j=(face+1)%len(z)
   zz[0]=z[face]+v[2]*(z[j]-z[face])
   dz[0][0]=p[face]+v[2]*(p[j]-p[face]);dz[0][2]=z[j]-z[face]
 if center==0:gauge=parameter(arb(0))
 elif(kind==0 and side==0)or(kind!=0 and side==1):gauge=parameter(ar('.2'if kind==0 else'-.2'))
 else:
  assert sign in(-1,1);sgn=-1 if kind==0 else 1
  gauge=parameter((4*sign*hv-ar('.053'))*sgn,[4*sign*sgn*d for d in dh])
 return zz,dz,cn,gauge

def macro_specs():
 return([[0,c,e,0,s]for e,c,s in itertools.product((0,1),repeat=3)]+
         [[1,c,n,0,s]for c,n,s in itertools.product((0,1),repeat=3)]+
         [[2,c,n,o,s]for c,n,o,s in itertools.product((0,1),repeat=4)])
def specs():
 out=[]
 for kind,center,neighbor,outer,side in macro_specs():
  signs=(-1,1)if center==1 and((kind==0 and side==1)or(kind!=0 and side==0))else(0,)
  faces=range(1 if kind==0 else(6 if(neighbor if kind==1 else outer)==0 else 5))
  for sign,face in itertools.product(signs,faces):out.append([kind,center,neighbor,outer,side,sign,face])
 assert len(out)==175 and len(set(map(str,out)))==175
 return out

def configure(bits):
 global pi,ii
 m.configure(bits);pi=arb.pi();ii=acb(0,1)

def test(box,case,witness=None):
 kind,center,neighbor,outer,side,sign,face=case
 zz,dz,cn,gauge=params(box,case);mid=[((a+b)/2,(a+b)/2)for a,b in box];z0,_,cn0,gauge0=params(mid,case)
 if kind<2:
  edges=[(1,2,neighbor,center)]if side==0 else[(2,1,center,neighbor)]
  ci,ck=0,1 if side==0 else 0;ng=[]
 elif side==0:edges=[(0,1,outer,neighbor),(1,2,neighbor,center)];ci,ck=1,1;ng=[(0,1),(1,0)]
 else:edges=[(2,1,center,neighbor),(1,0,neighbor,outer)];ci,ck=0,0;ng=[(0,1),(1,0)]
 datas=[];wits=[]
 for j,(a,b,eta,eps)in enumerate(edges):
  p=m.root_box(zz[a],zz[b],z0[a],z0[b],eps,None if witness is None else witness[j])
  if p is None:return None,None,None
  z,zc,w=p;datas.append((m.gradH(z,zz[a],zz[b],eta,eps),m.gradH(zc,z0[a],z0[b],eta,eps)));wits.append(w)
 gc=datas[ci][0][0][ck];gc0=datas[ci][1][0][ck]
 Gn=sum((datas[k][0][0][l]for k,l in ng),acb(0));Gn0=sum((datas[k][1][0][l]for k,l in ng),acb(0))
 qn=ii*cn.v/ar('.12');qn0=ii*cn0.v/ar('.12')
 fc=(gc0+qn0*Gn0).real+gauge0.v;fv=(gc+qn*Gn).real+gauge.v
 grads=[]
 for j in range(n):
  dg=[]
  for(a,b,eta,eps),data in zip(edges,datas):
   HH=data[0][1];dg.append([HH[k][0]*dz[a][j]+HH[k][1]*dz[b][j]for k in(0,1)])
  dgc=dg[ci][ck];dGn=sum((dg[k][l]for k,l in ng),acb(0))
  grads.append((dgc+ii*cn.d[j]/ar('.12')*Gn+qn*dGn).real+gauge.d[j])
 radii=[ar((b-a)/2)for a,b in box];lower=fc-sum((abs(v)*r for v,r in zip(grads,radii)),arb(0))
 if fv.lower()>lower.lower():lower=fv
 return lower,grads,wits

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def exact_checks():
 assert len(macro_specs())==32 and len(specs())==175
 assert [sum(c[0]==kind for c in specs())for kind in range(3)]==[10,55,110]
 assert F('.475')*F('.02')==F('.0095')and F('.7')*F('.02')==F('.014')
 for case in specs():
  z,dz,cn,g=params([(F(1,2),F(1,2))]*n,case)
  assert cn.v==0 if case[0]<2 else cn.v.is_finite()
 return {'exact_checks':4}

DEFAULT_BITS=320
DEFAULT_OUTPUT="repro/results/research-mixed-one-early-neighbor-transport-replay.json"
FINAL_SCOPE="Independent sine-log and explicit-parameter replay of all one-early-neighbor half stencils; no source or whole-cycle assertion."

def check_record(stem,prefix):
 path=BASE/f'repro/results/research-{stem.replace("_","-")}.json';rr=json.loads(path.read_text())
 assert rr['status']=='passed'
 assert rr['proof_sha256']==sha(BASE/f'notes/research_{stem}.md')
 assert rr['script_sha256']==sha(BASE/f'experiments/{prefix}_{stem}.py')
 for key in ('dependencies','dependencies_sha256'):
  for p,h in rr.get(key,{}).items():assert sha(BASE/p)==h,p
 if 'cover_path'in rr:
  cp=Path(rr['cover_path']);cp=cp if cp.is_absolute()else BASE/cp
  assert sha(cp)==rr['cover_sha256']
 return rr

GEOMETRY=[('mixed_neighbor_conditioned_critical_boxes','certify'),('mixed_four_before_four_height','certify'),('mixed_three_consecutive_four_height','check')]
DEPS=list(dict.fromkeys(m.DEPS+['experiments/certify_mixed_constant_selected_height_transport.py','experiments/replay_mixed_constant_selected_height_transport.py','notes/research_mixed_constant_selected_height_transport.md','repro/results/research-mixed-constant-selected-height-transport.json']+[p for stem,prefix in GEOMETRY+[('mixed_early_selected_source_cap','certify')]for p in[f'notes/research_{stem}.md',f'experiments/{prefix}_{stem}.py',f'repro/results/research-{stem.replace("_","-")}.json']]))

def inherited_checks():
 for stem in ('mixed_closed_cotangent_roots','mixed_minimum_neighbor_contour'):check_record(stem,'check')
 check_record('mixed_constant_selected_height_transport','certify')
 check_record('mixed_early_selected_source_cap','certify')
 geom=[check_record(stem,prefix)for stem,prefix in GEOMETRY]
 for word,limits in geom[0]['limits_in_thousandths'].items():assert list(map(F,CIM[word]))==[F(v,1000)for v in limits[1]],word
 assert geom[0]['boundary_products']==512 and geom[1]['boundary_products']==512 and geom[2]['boundary_products']==256
 assert arb(geom[2]['maximum_height_upper'])<ar('-.053')
 assert arb(geom[1]['maximum_height_upper'])<ar('-.048')
 return {'bound_geometry_records':3,'bound_geometry_intervals':8}

def verify_domain(case,data):
 assert data['case']==case
 nodes=iter(data['nodes']);stack=[[(F(0),F(1))for _ in range(n)]];vis=acc=mon=0;lo=None
 while stack:
  box=stack.pop();vis+=1;node=next(nodes)
  if node[0]=='S':
   assert len(node)==2 and type(node[1])is int and 0<=node[1]<n
   j=node[1];a,b=box[j];assert a<b;mid=(a+b)/2
   for pair in((a,mid),(mid,b)):
    bb=list(box);bb[j]=pair;stack.append(bb)
   continue
  assert node[0]in('L','M')
  w=node[-1];assert isinstance(w,list)and len(w)==(1 if case[0]<2 else 2)
  assert all(isinstance(v,dict)and set(v)=={'center','derivatives','radius'}for v in w)
  lower,grads,checked=test(box,case,w);assert lower is not None,(case,vis,'root witness')
  if node[0]=='L':
   assert len(node)==2 and lower>0,(case,vis,lower)
   acc+=1;lo=lower.lower()if lo is None else min(lo,lower.lower())
  else:
   assert len(node)==4;j,bit=node[1:3]
   assert type(j)is int and 0<=j<n and bit in(0,1)and box[j][0]<box[j][1]
   assert(grads[j]>0 if bit==0 else grads[j]<0),(case,vis,'monotonicity',j,grads[j])
   bb=list(box);end=box[j][bit];bb[j]=(end,end);stack.append(bb);mon+=1
 assert next(nodes,None)is None,(case,'unused tree nodes')
 assert(vis,acc,mon)==(data['visits'],data['accepted'],data['monotonic_reductions'])
 return dict(case=case,accepted=acc,visits=vis,monotonic_reductions=mon,minimum=str(lo))

def domain_job(job):
 number,case,path,digest,bits=job;configure(bits);assert sha(path)==digest
 data=json.loads(Path(path).read_text());row=verify_domain(case,data);assert sha(path)==digest
 return number,row

def replay_cover(source,bits,jobs,start):
 rows=[None]*175
 if jobs==1:
  with gzip.open(source,'rt')as stream:
   for number,case in enumerate(specs()):
    line=stream.readline();assert line,(number,'missing chart')
    rows[number]=verify_domain(case,json.loads(line))
    print('PASS chart',number+1,175,rows[number]['accepted'],rows[number]['monotonic_reductions'],'min',rows[number]['minimum'],'elapsed',time.time()-start,flush=True)
   assert not stream.read().strip(),'extra charts'
 else:
  with tempfile.TemporaryDirectory(prefix='one-early-saved-cover-')as tmp:
   with ProcessPoolExecutor(max_workers=jobs)as pool:
    pending={}
    with gzip.open(source,'rt')as stream:
     for number,case in enumerate(specs()):
      line=stream.readline();assert line,(number,'missing chart')
      path=Path(tmp)/f'{number:03d}.json';path.write_text(line)
      future=pool.submit(domain_job,(number,case,str(path),sha(path),bits));pending[future]=path
     assert not stream.read().strip(),'extra charts'
    for future in as_completed(pending):
     number,row=future.result();assert rows[number]is None and row['case']==specs()[number]
     rows[number]=row;pending[future].unlink()
     print('PASS chart',number+1,175,row['accepted'],row['monotonic_reductions'],'min',row['minimum'],'elapsed',time.time()-start,flush=True)
 assert all(r is not None for r in rows)
 return rows

def main():
 ap=argparse.ArgumentParser(description=__doc__)
 group=ap.add_mutually_exclusive_group();group.add_argument('--input',type=Path);group.add_argument('--witnesses',type=Path)
 ap.add_argument('--precision',type=int,default=DEFAULT_BITS);ap.add_argument('--jobs',type=int,default=1)
 ap.add_argument('--output',type=Path,default=BASE/DEFAULT_OUTPUT)
 args=ap.parse_args();assert args.precision>=192 and 1<=args.jobs<=16;configure(args.precision)
 if args.input is None and args.witnesses is None:args.input=BASE/'repro/results/research-mixed-one-early-neighbor-transport.json'
 ph,sh=sha(PROOF),sha(__file__);author=BASE/'experiments/certify_mixed_one_early_neighbor_transport.py';ash=sha(author)
 deps={p:sha(BASE/p)for p in DEPS};assert sha(LIB)==LIB_SHA
 checks=exact_checks();checks.update(inherited_checks());ih=None
 if args.input:
  ih=sha(args.input);saved=json.loads(args.input.read_text());assert saved['status']=='passed'
  assert saved['proof_sha256']==ph and saved['script_sha256']==ash and saved['dependencies_sha256']==deps
  source=Path(saved['cover_path']);source=source if source.is_absolute()else BASE/source
  assert sha(source)==saved['cover_sha256']
 else:source=args.witnesses
 cover_hash=sha(source);start=time.time();rows=replay_cover(source,args.precision,args.jobs,start)
 assert ph==sha(PROOF)and sh==sha(__file__)and ash==sha(author)and deps=={p:sha(BASE/p)for p in DEPS}and cover_hash==sha(source)
 if args.input:assert ih==sha(args.input)
 try:sourcepath=str(source.resolve().relative_to(BASE))
 except ValueError:sourcepath=str(source.resolve())
 result=dict(status='passed',precision_bits=args.precision,jobs=args.jobs,macro_domains=32,charts=175,cells=sum(r['accepted']for r in rows),visits=sum(r['visits']for r in rows),monotonic_reductions=sum(r['monotonic_reductions']for r in rows),minimum_half=str(min(arb(r['minimum']).lower()for r in rows)),cases=rows,proof_sha256=ph,script_sha256=sh,author_script_sha256=ash,dependencies_sha256=deps,cover_path=sourcepath,cover_sha256=cover_hash,input_source_kind='bound_author_record'if args.input else'untrusted_complete_cover',elapsed_seconds=time.time()-start,scope=FINAL_SCOPE,**checks)
 if args.input:result.update(input_path=str(args.input),input_sha256=ih)
 args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(result,indent=2)+'\n')
 print('FULL PASS',32,175,result['cells'],result['monotonic_reductions'],checks,flush=True)
if __name__=='__main__':main()
