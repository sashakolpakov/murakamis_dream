#!/usr/bin/env python3
"""Outward original-phase derivative on independent right-clamp domains.

All four real parameters are covered. Neighbor harmonic reduction precedes
the cover. Saved trees retain both root witnesses and every monotone face.
"""
import argparse,gzip,hashlib,importlib.util,itertools,json,math,tempfile,time
from concurrent.futures import ProcessPoolExecutor,as_completed
from fractions import Fraction as F
from pathlib import Path
import sympy as sy
from flint import arb,acb,ctx

ROOT=Path(__file__).resolve().parents[1]
PROOF=ROOT/'notes/research_mixed_unselected_right_clamping.md'
HELPER=ROOT/'experiments/certify_mixed_minimum_level_half_stencils.py'
spec=importlib.util.spec_from_file_location('right_clamp_original_arithmetic',HELPER)
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
ar=m.ar
OMEGA={0:[('.1','0'),('.22','-.03'),('.45','-.03'),('.5','0'),('.45','.02'),('.22','.02')],
       1:[('.1','0'),('.22','-.057'),('.45','-.057'),('.5','0'),('.45','.014'),('.12','.014')]}
K={0:(F('-.03'),F('.02')),1:(F('-.057'),F(0))}
RECORDS=[
 ('mixed_closed_cotangent_roots','check'),
 ('mixed_early_selected_source_cap','certify'),
 ('mixed_left_right_interface_source','certify'),
 ('mixed_right_guard_conditional_packets','certify'),
 ('mixed_right_square_conditional_packets','certify','mixed_unselected_right_taper_products'),
 ('mixed_fourier_weight_continuation','check'),
 ('mixed_split_cutoff_hybrid_contour','check'),
]
HELPERS=['experiments/certify_mixed_minimum_level_half_stencils.py',
 'experiments/certify_mixed_isolated_transition_phase.py',
 'experiments/certify_mixed_real_small_support.py']

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def configure(bits):
 global pi,ii
 m.configure(bits);pi,ii=m.pi,m.ii
def specifications():
 return [list(v) for v in itertools.product((0,1),(0,1),(0,1),range(6),range(6))]
def edge(ty,face,lo,hi):
 aa,bb=OMEGA[ty][face],OMEGA[ty][(face+1)%6]
 start=acb(ar(aa[0]),ar(aa[1]));vel=acb(ar(F(bb[0])-F(aa[0])),ar(F(bb[1])-F(aa[1])))
 return start+vel*ar(lo).union(ar(hi)),vel
def params(box,case):
 eta,beta,gamma,ia,ic=case
 a,da=edge(eta,ia,*box[0]);c,dc=edge(gamma,ic,*box[1])
 t=ar('.45')+ar('.05')*ar(box[2][0]).union(ar(box[2][1]))
 kl,kh=K[beta];dk=ar(kh-kl);k=ar(kl)+dk*ar(box[3][0]).union(ar(box[3][1]))
 r=400*(ar('.5')-t)**2;rp=-800*(ar('.5')-t);q=1+ii*k*rp
 b=acb(t,k*r)
 dz=[[da,acb(0),acb(0),acb(0)],
     [acb(0),acb(0),ar('.05')*q,ii*dk*r],
     [acb(0),dc,acb(0),acb(0)]]
 dq=[acb(0),acb(0),ii*40*k,ii*dk*rp]
 return [a,b,c],dz,q,dq

def test(box,case,witness=None):
 zz,dz,q,dq=params(box,case);mid=[((lo+hi)/2,(lo+hi)/2)for lo,hi in box]
 z0,_,q0,_=params(mid,case);eta,beta,gamma,_,_=case
 datas=[];wits=[]
 for j,(left,right,et,ep)in enumerate(((0,1,eta,beta),(1,2,beta,gamma))):
  old=None if witness is None else witness[j]
  if old is not None:assert F(0)<F(old['radius'])<=F(1,20)
  packet=m.root_box(zz[left],zz[right],z0[left],z0[right],ep,old)
  if packet is None:return None,None,None
  s,sc,wit=packet;assert F(0)<F(wit['radius'])<=F(1,20)
  full=m.gradH(s,zz[left],zz[right],et,ep);point=m.gradH(sc,z0[left],z0[right],et,ep)
  # A valid correlated Newton enclosure does not imply that a direct interval
  # Schur denominator excludes zero. Such inflation must trigger subdivision.
  if not all(v.is_finite()for pair in(full,point)for v in(pair[0]+[v for row in pair[1]for v in row])):
   return None,None,None
  datas.append((full,point))
  wits.append(wit)
 left,right=datas
 G=left[0][0][1]+right[0][0][0];G0=left[1][0][1]+right[1][0][0]
 fc=(q0*G0).real;fv=(q*G).real;grads=[]
 for j in range(4):
  dg=left[0][1][1][0]*dz[0][j]+(left[0][1][1][1]+right[0][1][0][0])*dz[1][j]+right[0][1][0][1]*dz[2][j]
  grads.append((q*dg+dq[j]*G).real)
 if not all(v.is_finite()for v in[fc,fv]+grads):return None,None,None
 upper=fc+sum((abs(v)*ar((hi-lo)/2)for v,(lo,hi)in zip(grads,box)),arb(0))
 # Each independently valid upper endpoint can be used; no Arb max/min ambiguity.
 if fv.upper()<upper.upper():upper=fv
 return upper,grads,wits

def choose(box,case,grads):
 if grads is not None:
  return max(((abs(grads[j])*ar(hi-lo)).upper(),j)for j,(lo,hi)in enumerate(box)if hi>lo)[1]
 _,dz,_,_=params([((lo+hi)/2,(lo+hi)/2)for lo,hi in box],case)
 return max(((sum((abs(row[j])for row in dz),arb(0))*ar(hi-lo)).upper(),j)for j,(lo,hi)in enumerate(box)if hi>lo)[1]

def work(job):
 index,case,bits,source,dest,budget=job;configure(bits)
 source_hash=sha(source)if source else None
 saved=json.loads(Path(source).read_text())if source else None
 if saved:assert saved['index']==index and saved['case']==case
 todo=[[(F(0),F(1))for _ in range(4)]];nodes=[];cursor=0;leaves=monotone=visits=0;worst=None
 while todo:
  box=todo.pop();visits+=1;assert visits<=budget,(index,'node budget',visits)
  if saved:
   assert cursor<len(saved['nodes']);node=saved['nodes'][cursor];cursor+=1
   if node[0]=='S':
    j=node[1];assert type(j)is int and 0<=j<4 and box[j][0]<box[j][1]
    mid=sum(box[j])/2;lo=list(box);hi=list(box);lo[j]=(box[j][0],mid);hi[j]=(mid,box[j][1]);todo.extend((lo,hi));nodes.append(node);continue
   assert node[0]in('L','M')
   upper,grads,wits=test(box,case,node[-1]);assert upper is not None,(index,'saved root failure',box)
   if node[0]=='L':
    assert upper<-ar('1/10'),(index,'saved inequality',box,str(upper));leaves+=1
    worst=upper.upper()if worst is None else max(worst,upper.upper())
   else:
    _,j,bit,_=node;assert type(j)is int and 0<=j<4 and bit in(0,1)and box[j][0]<box[j][1]
    assert(grads[j]>0 if bit else grads[j]<0),(index,'saved monotonicity',j,box)
    value=box[j][bit];reduced=list(box);reduced[j]=(value,value);todo.append(reduced);monotone+=1
   nodes.append(node);continue
  upper,grads,wits=test(box,case)
  if upper is not None and upper<-ar('1/10'):
   nodes.append(['L',wits]);leaves+=1;worst=upper.upper()if worst is None else max(worst,upper.upper());continue
  signed=[]
  if grads is not None:
   for j,(lo,hi)in enumerate(box):
    if hi>lo and(grads[j]>0 or grads[j]<0):signed.append(((abs(grads[j])*ar(hi-lo)).upper(),j,int(grads[j]>0)))
  if signed:
   _,j,bit=max(signed);nodes.append(['M',j,bit,wits]);reduced=list(box);value=box[j][bit];reduced[j]=(value,value);todo.append(reduced);monotone+=1;continue
  assert any(lo<hi for lo,hi in box),(index,'point not negative',box,str(upper))
  j=choose(box,case,grads);lo=list(box);hi=list(box);mid=sum(box[j])/2;lo[j]=(box[j][0],mid);hi[j]=(mid,box[j][1]);nodes.append(['S',j]);todo.extend((lo,hi))
  assert max((x.denominator.bit_length()for pair in box for x in pair))<65,(index,'depth limit',box)
 if saved:
  assert cursor==len(saved['nodes'])
  assert(leaves,visits,monotone)==(saved['leaves'],saved['visits'],saved['monotone'])
  assert sha(source)==source_hash
 result=dict(index=index,case=case,nodes=nodes,leaves=leaves,visits=visits,monotone=monotone,maximum_derivative_upper=str(worst))
 Path(dest).write_text(json.dumps(result,separators=(',',':'))+'\n')
 return index,leaves,visits,monotone,str(worst),sha(dest)

def bindings():
 deps={p:sha(ROOT/p)for p in HELPERS};records=[]
 for item in RECORDS:
  stem,prefix=item[:2];proof=item[2]if len(item)>2 else stem
  rp=f'repro/results/research-{stem.replace("_","-")}.json';pp=f'notes/research_{proof}.md';ss=f'experiments/{prefix}_{stem}.py'
  rec=json.loads((ROOT/rp).read_text());assert rec['status']=='passed'
  inherited={**rec.get('dependencies',{}),**rec.get('dependencies_sha256',{})}
  assert rec.get('proof_sha256',inherited.get(pp))==sha(ROOT/pp)and rec['script_sha256']==sha(ROOT/ss)
  for field in('dependencies','dependencies_sha256'):
   for path,digest in rec.get(field,{}).items():assert sha(ROOT/path)==digest,path;deps[path]=digest
  for path in(rp,pp,ss):deps[path]=sha(ROOT/path)
  records.append(rp)
 return deps,records

def exact_checks():
 t,k,dt,dk=sy.symbols('t k dt dk',real=True);R=400*(sy.Rational(1,2)-t)**2;q=1+sy.I*k*sy.diff(R,t)
 checks={
  'quadratic baseline':R.subs(t,sy.Rational(9,20))-1,
  'quadratic endpoint':R.subs(t,sy.Rational(1,2)),
  'R second derivative':sy.diff(R,t,2)-800,
  'center differential':sy.diff(t+sy.I*k*R,t)*dt+sy.diff(t+sy.I*k*R,k)*dk-q*dt-sy.I*R*dk,
  'direction differential':sy.diff(q,t)*dt+sy.diff(q,k)*dk-sy.I*(sy.diff(R,t)*dk+800*k*dt),
 }
 for name,v in checks.items():assert sy.simplify(v)==0,name
 return list(checks)

def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--precision',type=int,default=256);ap.add_argument('--workers',type=int,default=2);ap.add_argument('--max-nodes',type=int,default=500000)
 ap.add_argument('--input',type=Path);ap.add_argument('--first',type=int,default=0);ap.add_argument('--last',type=int,default=288)
 ap.add_argument('--output',type=Path,default=ROOT/'repro/results/research-mixed-unselected-right-clamping.json');ap.add_argument('--cover',type=Path);args=ap.parse_args()
 if args.cover is None:args.cover=args.output.with_name(args.output.stem+'-cover.jsonl.gz')
 assert args.precision>=128 and 0<=args.first<args.last<=288
 configure(args.precision);ph,sh=sha(PROOF),sha(__file__);deps,records=bindings();exact=exact_checks();specs=specifications();assert len(specs)==288
 ih=sha(args.input)if args.input else None;saved=json.loads(args.input.read_text())if args.input else None
 if saved:
  assert saved['status']=='passed'and saved['products']==288
  assert saved['proof_sha256']==ph and saved['script_sha256']==sh and saved['dependencies_sha256']==deps
  cp=Path(saved['cover_path']);cp=cp if cp.is_absolute()else ROOT/cp;ch=sha(cp);assert ch==saved['cover_sha256']
 start=time.time();summaries={}
 with tempfile.TemporaryDirectory(prefix='right-clamp-')as tmp:
  tmp=Path(tmp);sources={}
  if saved:
   with gzip.open(cp,'rt')as handle:
    for idx,line in enumerate(handle):
     row=json.loads(line);assert row['index']==idx and row['case']==specs[idx]
     path=tmp/f'input-{idx}.json';path.write_text(line);sources[idx]=path
   assert len(sources)==288
  jobs=[(idx,specs[idx],args.precision,sources.get(idx),tmp/f'output-{idx}.json',args.max_nodes)for idx in range(args.first,args.last)]
  with ProcessPoolExecutor(max_workers=args.workers)as pool:
   futures={pool.submit(work,job):job[0]for job in jobs}
   for future in as_completed(futures):
    result=future.result();idx=result[0];assert idx==futures[future]and idx not in summaries;summaries[idx]=result
    print('product',idx+1,'completed',len(summaries),'/',len(jobs),'leaves',result[1],'nodes',result[2],'M',result[3],'seconds',round(time.time()-start,1),flush=True)
  assert set(summaries)==set(range(args.first,args.last));args.cover.parent.mkdir(parents=True,exist_ok=True)
  with gzip.open(args.cover,'wt')as out:
   for idx in range(args.first,args.last):
    path=tmp/f'output-{idx}.json';assert sha(path)==summaries[idx][-1];out.write(path.read_text())
 assert ph==sha(PROOF)and sh==sha(__file__)
 assert all(sha(ROOT/path)==digest for path,digest in deps.items())
 if saved:assert sha(args.input)==ih and sha(cp)==ch
 try:cover_path=str(args.cover.relative_to(ROOT))
 except ValueError:cover_path=str(args.cover.resolve())
 result=dict(status='passed'if(args.first,args.last)==(0,288)else'passed_subset',precision_bits=args.precision,products=len(summaries),product_range=[args.first,args.last],leaves=sum(x[1]for x in summaries.values()),visits=sum(x[2]for x in summaries.values()),monotone_reductions=sum(x[3]for x in summaries.values()),case_summaries=[dict(index=i,case=specs[i],leaves=summaries[i][1],visits=summaries[i][2],monotone=summaries[i][3],maximum_derivative_upper=summaries[i][4])for i in sorted(summaries)],exact_identity_count=len(exact),exact_identities=exact,primary_records=records,proof_sha256=ph,script_sha256=sh,dependencies_sha256=deps,cover_path=cover_path,cover_sha256=sha(args.cover),input_sha256=ih,elapsed_seconds=time.time()-start,scope='Independent neighbor polygons, all eight physical type triples, complete t and unselected k intervals; original two-incident phase derivative < -1/10. No selected-center clamp, neighbor beyond half, or whole-period estimate.')
 args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(result,indent=2)+'\n')
 print('PASS',result['status'],result['products'],'products',result['leaves'],'leaves',result['visits'],'nodes',result['monotone_reductions'],'monotone reductions',flush=True)

if __name__=='__main__':main()
