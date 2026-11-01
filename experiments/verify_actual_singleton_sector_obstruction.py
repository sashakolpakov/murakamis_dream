#!/usr/bin/env python3
"""Exact rational fixed-sector obstruction. No optimizer or floating point is used.

The input is a literal oriented sphere/matching/mark plus rational feasible
loads for ONE LEFT sector with CROSS at every other crossing. Elementary
sphere moves, all face targets, and a rational complete-action upper witness
are checked before outward rational entropy bounds are evaluated.
"""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict,Counter
from math import isqrt
import argparse,importlib.util,json,hashlib
if not __debug__:raise SystemExit('Do not run with -O')

def load_engine(repo):
 p=Path(repo)/'experiments/verify_conway_two_leaf_block_alias_certificate.py'
 spec=importlib.util.spec_from_file_location('singleton_interval_engine',p);e=importlib.util.module_from_spec(spec);spec.loader.exec_module(e)
 return e,p

def edges(fs):
 out=defaultdict(list)
 for i,t in enumerate(fs):
  assert len(set(t))==3
  for j in range(3):out[tuple(sorted((t[j],t[(j+1)%3])))].append((i,t[j],t[(j+1)%3],t[(j+2)%3]))
 assert len({tuple(sorted(t)) for t in fs})==len(fs)
 for rr in out.values():assert len(rr)==2 and rr[0][1]==rr[1][2] and rr[0][2]==rr[1][1]
 return out

def cyc(a,b):return any(tuple(a)==tuple(b[k:]+b[:k]) for k in range(3))

def verify(data,repo):
 engine,engine_path=load_engine(repo);I,S,PI,ZETA,logi=engine.I,engine.S,engine.PI,engine.ZETA,engine.logi
 def sqrt(x):
  x=engine.iv(x);assert x.lo>=0;lo=isqrt(x.lo*S);hi=isqrt(x.hi*S)
  if hi*hi<x.hi*S:hi+=1
  return I(lo,hi,raw=True)
 def atan(x):
  x=engine.iv(x);assert x.lo>=0;mul=1
  while 2*x.hi>S:x=x/(1+sqrt(1+x*x));mul*=2
  term=x;out=I(0)
  for j in range(80):out+=(-1)**j*term/F(2*j+1);term=term*x*x
  tail=term/F(161)
  return mul*(out+I(-tail.hi,tail.hi,raw=True))
 def J(t):
  t=engine.iv(t);assert 0<t.lo<=t.hi<S//2
  out=t*logi(2*PI*t)-t
  for n in range(1,21):out-=ZETA[n]*t**(2*n+1)/F(n*(2*n+1))
  tail=2*t**43/(F(21*43)*(1-t*t))
  return out+I(-tail.hi,0,raw=True)
 cache={}
 def f(a):
  assert 0<=a<=F(1,2)
  if a in (0,F(1,2)):return I(0)
  if a not in cache:cache[a]=-J(a)-J(F(1,2)-a)
  return cache[a]
 def Q(weights):
  weights=sorted(weights);assert weights[0]>=0 and weights[-1]>0
  pos=[w for w in weights if w]
  if len(pos)==1:return logi(pos[0])/2
  D=sqrt(sum(weights[i]*weights[j] for i in range(3) for j in range(i+1,3)));out=I(0)
  for w in pos:
   a=atan(I(w)/D)/PI
   out+=-J(a)-J(F(1,2)-a)+a*logi(w)
  return out
 # Exact reconstruction: stellar subdivision and legal diagonal flips.
 fs=[(0,1,2),(0,3,1),(1,3,2),(0,2,3)];nv=4
 for op in data['sphere_history']:
  if op['kind']=='stellar':
   j=op['index'];assert tuple(op['old'])==fs[j] and op['new']==nv;a,b,c=fs.pop(j);fs.extend([(a,b,nv),(b,c,nv),(c,a,nv)]);nv+=1
  else:
   assert op['kind']=='flip';i,j=op['i'],op['j'];a,b,c,d=[op[x] for x in 'abcd'];ed=edges(fs)
   assert cyc(fs[i],(a,b,c)) and cyc(fs[j],(b,a,d)) and c!=d and tuple(sorted((c,d))) not in ed
   fs[i]=(c,a,d);fs[j]=(d,b,c)
  edges(fs)
 s=data['source'];assert nv==s['vertices'] and fs==list(map(tuple,s['faces']))
 ed=edges(fs);matching=list(map(tuple,s['matching_faces']));assert sorted(i for pair in matching for i in pair)==list(range(len(fs)))
 ports=[];matching_edges=[]
 for i,j in matching:
  assert i<j;common=set(fs[i])&set(fs[j]);assert len(common)==2;t=fs[i]
  k=next(k for k in range(3) if {t[k],t[(k+1)%3]}==common)
  y,x,b=t[k],t[(k+1)%3],t[(k+2)%3];c=next(v for v in fs[j] if v not in common)
  ports.append((x,b,c,y));matching_edges.append(tuple(sorted((x,y))))
 assert ports==list(map(tuple,s['ports'])) and len(set(matching_edges))==len(ports)
 R=len(ports);assert len(fs)==2*R and nv==R+2 and len(ed)==3*R
 zero=set(s['protected']);mark=tuple(sorted(zero));assert len(zero)==2 and mark in ed and mark not in matching_edges
 ordinary=sorted(set(range(nv))-zero);assert ordinary==data['ordinary']
 a=data['anchor'];tags=data['tags'];assert len(tags)==R and tags[a]=='L' and all(v=='C' for i,v in enumerate(tags) if i!=a)
 overloaded=ports[a][2];assert overloaded==data['overloaded_face'] and overloaded not in zero
 # Literal row incidence and original unit target equations.
 vals=[F(*v['value']) for v in data['variables']];names=[tuple(v['name']) for v in data['variables']]
 assert len(set(names))==len(names) and min(vals)>=0
 li=data['lambda_variable'];assert names[li]==('lambda',);lam=vals[li];assert 0<lam<1
 expected=[(e,side) for e in range(R) for side in (0,1) if not (e==a and side==1)]
 assert [(r['crossing'],r['side']) for r in data['rows']]==expected
 used=[];loads={f:F(0) for f in ordinary};entropy=I(0)
 for row in data['rows']:
  e,side=row['crossing'],row['side'];x,b,c,y=ports[e];tri=(x,b if side==0 else c,y);active=[f for f in tri if f not in zero]
  assert row['faces']==active and row['fractional']==(e==a)
  ids=row['variables'];assert len(ids)==len(active);used.extend(ids);mass=lam if e==a else F(1)
  assert sum((vals[i] for i in ids),F(0))==mass/2
  for face,i in zip(active,ids):assert names[i]==('corner',e,side,face);loads[face]+=vals[i]
  entropy+=mass*sum((f(vals[i]/mass) for i in ids),I(0))
 assert sorted(used+[li])==list(range(len(vals)))
 loads[overloaded]+=1-lam/2
 assert all(v==1 for v in loads.values())
 # Exact support data used in the all-large-even-level proof.
 cross_rows=[row for row in data['rows'] if not row['fractional']]
 graph={face:set() for face in ordinary}
 for row in cross_rows:
  for face in row['faces']:graph[face].update(set(row['faces'])-{face})
 seen={ordinary[0]};queue=list(seen)
 while queue:
  for face in graph[queue.pop()]-seen:seen.add(face);queue.append(face)
 assert seen==set(ordinary)
 assert ports[a]==(0,50,16,29) and zero=={29,50}
 assert data['rows'][2*a]['faces']==[0]
 minimum_cross_corner=min(vals[i] for row in cross_rows for i in row['variables'])
 assert minimum_cross_corner>0
 chosen_outer=[]
 for e,(x,b,c,y) in enumerate(ports):
  if e!=a:
   choices=[face for face in (x,y) if face not in zero];assert choices
   chosen_outer.append(choices[0])
 assert len(chosen_outer)==R-1
 load_correction_bound=(R-1)*(2*R+2)
 even_half_level=load_correction_bound//(2*minimum_cross_corner)+2
 support={'ordinary_cross_triangle_graph_connected':True,'ordinary_vertices':R,
  'minimum_cross_corner_load':str(minimum_cross_corner),'selected_outer_faces':chosen_outer,
  'per_corner_correction_bound':load_correction_bound,
  'nonzero_sector_for_all_even_levels_at_least':2*even_half_level,
  'scope':'Exact incidence and rational-load checks for the support proof in the note; not a lower exponential-rate estimate.'}
 weights={int(k):F(*v) for k,v in data['complete_upper_radii'].items()};assert sorted(weights)==ordinary and min(weights.values())>0
 weights.update({f:F(0) for f in zero})
 upper=sum((Q([weights[x],weights[mid],weights[y]]) for x,b,c,y in ports for mid in (b,c)),I(0))-sum((logi(weights[f]) for f in ordinary),I(0))
 gap=entropy-upper;assert F(gap.lo,S)>F(1,5),(entropy.bounds(),upper.bounds(),gap.bounds())
 return {'status':'certified','scope':'One genuine fixed LEFT/CROSS string has convex weighted-envelope capacity above the actual complete action. This is not a lower bound on a signed source coefficient or on the quantum invariant.','counts':{'crossings':R,'white_vertices':nv,'triangles':len(fs),'sphere_edges':len(ed),'elementary_sphere_moves':len(data['sphere_history']),'dual_variables':len(vals),'exact_face_targets':len(loads),'one_sided_crossings':1,'mixed_spectator_crossings':0},'protected':sorted(zero),'anchor':a,'anchor_quartet':ports[a],'lambda':str(lam),'dual_entropy_lower_and_upper':entropy.bounds(),'complete_action_upper_witness_bounds':upper.bounds(),'strict_excess_bounds':gap.bounds(),'certified_strict_excess':'1/5','arithmetic':'integer outward-rounded rational intervals; sqrt by isqrt; atan alternating series with half-angle reduction; integrated log sine from Euler product with exact tail','engine_path':str(engine_path.relative_to(Path(repo))),'engine_sha256':hashlib.sha256(engine_path.read_bytes()).hexdigest(),'optimizer_used_in_verification':False,'nonzero_sector_support':support}

def main():
 repo_default=Path(__file__).resolve().parents[1]
 parser=argparse.ArgumentParser(description=__doc__)
 parser.add_argument('--repo',type=Path,default=repo_default)
 parser.add_argument('--certificate',type=Path,default=repo_default/'experiments/actual_singleton_sector_obstruction_certificate.json')
 parser.add_argument('--output',type=Path,default=repo_default/'experiments/actual_singleton_sector_obstruction_results.json')
 args=parser.parse_args()
 result=verify(json.loads(args.certificate.read_text()),args.repo)
 result['certificate_sha256']=hashlib.sha256(args.certificate.read_bytes()).hexdigest()
 result['verifier_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
 args.output.parent.mkdir(parents=True,exist_ok=True)
 args.output.write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps({'status':result['status'],'strict_excess':result['certified_strict_excess'],'crossings':result['counts']['crossings'],'output':str(args.output)},indent=2))
if __name__=='__main__':main()
