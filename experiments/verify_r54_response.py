#!/usr/bin/env python3
"""Exact rational enclosures for the original R54 exterior response.
The proposal file is not a numerical proof: all acceptance tests below use
outward integer interval arithmetic and rational graph inequalities.
"""
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
from fractions import Fraction as F
from collections import deque
from math import isqrt
import json,hashlib,importlib.util,argparse
if not __debug__:raise SystemExit('Assertions must be enabled')

def main():
 ap=argparse.ArgumentParser(description=__doc__)
 ap.add_argument('--repo',type=Path,default=ROOT)
 ap.add_argument('--certificate',type=Path,default=ROOT / 'experiments/r54_response_certificate.json')
 ap.add_argument('--output',type=Path,default=Path('r54_response_results.json'))
 args=ap.parse_args();src=args.repo/'experiments/actual_singleton_sector_obstruction_certificate.json'
 original=json.loads(src.read_text());data=json.loads(args.certificate.read_text())
 assert data['source_certificate_sha256']==hashlib.sha256(src.read_bytes()).hexdigest()
 ep=args.repo/'experiments/verify_conway_two_leaf_block_alias_certificate.py'
 spec=importlib.util.spec_from_file_location('response_interval',ep);e=importlib.util.module_from_spec(spec);spec.loader.exec_module(e)
 I,S,PI,logi=e.I,e.S,e.PI,e.logi
 def sqrt(x):
  x=e.iv(x);assert x.lo>=0
  a=isqrt(x.lo*S);b=isqrt(x.hi*S)
  if b*b<x.hi*S:b+=1
  return I(a,b,raw=True)
 def atan(x):
  x=e.iv(x);assert x.lo>=0;scale=1
  while 2*x.hi>S:x=x/(1+sqrt(1+x*x));scale*=2
  term=x;val=I(0)
  for k in range(80):val+=(-1)**k*term/F(2*k+1);term=term*x*x
  tail=term/F(161)
  return scale*(val+I(-tail.hi,tail.hi,raw=True))
 def J(t):
  t=e.iv(t);assert 0<t.lo<=t.hi<S//2
  out=t*logi(2*PI*t)-t
  for n in range(1,21):out-=e.ZETA[n]*t**(2*n+1)/F(n*(2*n+1))
  tail=2*t**43/(F(21*43)*(1-t*t))
  return out+I(-tail.hi,0,raw=True)
 def boundabs(x):return F(max(abs(x.lo),abs(x.hi)),S)
 def lower(x):return F(x.lo,S)
 def upper(x):return F(x.hi,S)
 A,C=16,0;zero=set(original['source']['protected']);anchor=original['anchor'];ports=original['source']['ports']
 assert anchor==32 and ports[anchor]==[0,50,16,29] and zero=={29,50}
 ordinary=original['ordinary'];free=[v for v in ordinary if v not in (A,C)];n=len(free)
 assert n==52 and n<=64
 weights={int(k):F(*v) for k,v in data['weights'].items()};trial={int(k):F(*v) for k,v in data['potential_trial'].items()}
 assert set(weights)==set(trial)==set(ordinary) and min(weights.values())>0
 assert weights[A]==weights[C]==1 and trial[A]==1 and trial[C]==0
 radius=F(*data['radius']);assert radius==F(1,1000)
 grad={v:I(0) for v in ordinary};res={v:I(0) for v in free};energy=I(0);value=I(0)
 conductance=[];graph={v:set() for v in ordinary};degree_A=0;rows=0
 for crossing,(x,b,c,y) in enumerate(ports):
  if crossing==anchor:continue
  for middle in (b,c):
   tri=[v for v in (x,middle,y) if v not in zero];rows+=1;W=[weights[v] for v in tri]
   if len(tri)==1:
    angles=[I(F(1,2))];value+=logi(W[0])/2
   else:
    D=sqrt(sum(W[i]*W[j] for i in range(len(W)) for j in range(i+1,len(W))))
    angles=[atan(I(w)/D)/PI for w in W]
    for v,a in zip(tri,angles):value+=-J(a)-J(F(1,2)-a)+a*logi(weights[v])
    for i,vi in enumerate(tri):
     for j in range(i+1,len(tri)):
      vj=tri[j];k=I(W[i]*W[j])/(2*PI*D*(W[i]+W[j]));assert lower(k)>0
      conductance.append(lower(k));graph[vi].add(vj);graph[vj].add(vi)
      dh=trial[vi]-trial[vj];energy+=k*dh*dh
      if vi in res:res[vi]+=k*dh
      if vj in res:res[vj]-=k*dh
      if A in (vi,vj):degree_A+=1
   for v,a in zip(tri,angles):grad[v]+=a
 for v in free:grad[v]-=1;value-=logi(weights[v])
 assert rows==106
 dist={A:0,C:0};queue=deque([A,C])
 while queue:
  v=queue.popleft()
  for w in graph[v]:
   if w not in dist:dist[w]=dist[v]+1;queue.append(w)
 assert set(dist)==set(ordinary)
 depth=max(dist.values());lam=min(conductance)/F(n*depth)
 # Every free vertex has a path of at most depth edges to a grounded
 # vertex. Cauchy along these paths gives Hessian >= lam * identity.
 gmax=max(boundabs(grad[v]) for v in free)
 lam_ball=(1-4*radius)*lam
 assert 8*gmax<lam_ball*radius
 # Radial gradient positivity on the Euclidean radius ball puts the
 # unique minimizer inside it. Edge conductances vary by e^(+/-4r).
 rmax=max(boundabs(res[v]) for v in free)
 k0_lower=lower(energy)-n*rmax*rmax/lam
 kappa_lower=(1-4*radius)*k0_lower
 nu_error=radius*degree_A/(4*lower(PI))
 nu_lower=lower(grad[A])-nu_error;nu_upper=upper(grad[A])+nu_error
 assert nu_lower>F(27,100) and nu_upper<F(28,100)
 assert kappa_lower>F(11,125)
 assert upper(value)<F(33947,500) # 67.894
 loss=-logi(F(81,125))/2
 assert lower(loss)>F(27,125) # .216
 result={'status':'certified','scope':'Original exterior pressure and grounded response; no quantum-spectrum extrapolation.',
  'ordinary_vertices':len(ordinary),'free_vertices':n,'spectator_triangles':rows,
  'grounded_path_depth':depth,'hessian_lower_at_trial':str(lam),'gradient_max_bound':str(gmax),
  'radius':str(radius),'localization_test_margin':str(lam_ball*radius-8*gmax),
  'trial_energy_bounds':energy.bounds(),'trial_energy_residual_max_bound':str(rmax),
  'kappa_lower':str(kappa_lower),'nu_bounds':[str(nu_lower),str(nu_upper)],'pressure_trial_bounds':value.bounds(),
  'conservative_certified_bounds':{'nu':["27/100","28/100"],'kappa_lower':"11/125",'M_cap_upper':"33947/500",'squared_factor_R_upper':"81/125",'loss_lower':"27/125"},
  'arithmetic':'Outward integer fixed-point intervals; no optimizer or floating point used in verification.',
  'source_certificate_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),
  'response_certificate_sha256':hashlib.sha256(args.certificate.read_bytes()).hexdigest(),
  'engine_sha256':hashlib.sha256(ep.read_bytes()).hexdigest(),'verifier_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
 args.output.write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps({'status':result['status'],'bounds':result['conservative_certified_bounds'],'grounded_path_depth':depth,'output':str(args.output)},indent=2))
if __name__=='__main__':main()
