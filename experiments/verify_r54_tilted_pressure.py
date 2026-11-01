#!/usr/bin/env python3
"""Exact upper bound for the tilted original exterior pressure at A/C=17/5.
No stationarity of the proposed rational weights is assumed or needed.
"""
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
from fractions import Fraction as F
from math import isqrt
import json, hashlib, importlib.util, argparse
if not __debug__: raise SystemExit('Assertions must be enabled')

def main():
 ap=argparse.ArgumentParser(description=__doc__)
 ap.add_argument('--repo',type=Path,default=ROOT)
 ap.add_argument('--certificate',type=Path,default=ROOT / 'experiments/r54_tilted_pressure_certificate.json')
 ap.add_argument('--response-result',type=Path,default=Path('r54_response_results.json'))
 ap.add_argument('--output',type=Path,default=Path('r54_tilted_pressure_results.json'))
 args=ap.parse_args();src=args.repo/'experiments/actual_singleton_sector_obstruction_certificate.json'
 original=json.loads(src.read_text());data=json.loads(args.certificate.read_text())
 assert data['source_certificate_sha256']==hashlib.sha256(src.read_bytes()).hexdigest()
 ep=args.repo/'experiments/verify_conway_two_leaf_block_alias_certificate.py'
 spec=importlib.util.spec_from_file_location('tilt_interval',ep);e=importlib.util.module_from_spec(spec);spec.loader.exec_module(e)
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
 A,C=16,0;zero=set(original['source']['protected']);anchor=original['anchor'];ports=original['source']['ports']
 assert anchor==32 and ports[anchor]==[0,50,16,29] and zero=={29,50}
 ordinary=original['ordinary'];free=[v for v in ordinary if v not in (A,C)]
 weights={int(k):F(*v) for k,v in data['weights'].items()};T=F(*data['tilt'])
 assert set(weights)==set(ordinary) and min(weights.values())>0
 assert T==F(17,5) and weights[A]==T and weights[C]==1
 value=I(0);rows=0
 for crossing,(x,b,c,y) in enumerate(ports):
  if crossing==anchor:continue
  for middle in (b,c):
   tri=[v for v in (x,middle,y) if v not in zero];W=[weights[v] for v in tri];rows+=1
   if len(tri)==1:value+=logi(W[0])/2
   else:
    D=sqrt(sum(W[i]*W[j] for i in range(len(W)) for j in range(i+1,len(W))))
    angles=[atan(I(w)/D)/PI for w in W]
    for v,a in zip(tri,angles):value+=-J(a)-J(F(1,2)-a)+a*logi(weights[v])
 for v in free:value-=logi(weights[v])
 assert rows==106
 weighted=value-logi(T)/2
 assert F(weighted.hi,S)<F(16921,250) # 67.684
 # This checks the sharper consequence of the separately replayed response
 # enclosure. Its underlying localization proof remains a named input.
 response=json.loads(args.response_result.read_text())
 assert response['source_certificate_sha256']==hashlib.sha256(src.read_bytes()).hexdigest()
 assert F(response['nu_bounds'][0])>F(27,100)
 assert F(response['nu_bounds'][1])<F(11,40)
 assert F(response['kappa_lower'])>F(11,125)
 nu_hi=F(11,40);kappa_lo=F(11,125)
 assert 1-(1+T)*nu_hi+(T-1)*kappa_lo>0
 result={'scope':'Exact rational trial-pressure upper bound; response tightening uses the separately verified response enclosure.',
 'source_certificate_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),
 'tilted_certificate_sha256':hashlib.sha256(args.certificate.read_bytes()).hexdigest(),
 'response_result_sha256':hashlib.sha256(args.response_result.read_bytes()).hexdigest(),
 'engine_sha256':hashlib.sha256(ep.read_bytes()).hexdigest(),
 'verifier_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'tilt':str(T),'spectator_triangles':rows,'weighted_pressure_bounds':weighted.bounds(),
 'certified_upper':'16921/250','nu_lower':'27/100','nu_upper':'11/40','kappa_lower':'11/125',
 'a_minus_T_b_lower':str(1-(1+T)*nu_hi+(T-1)*kappa_lo),
 'arithmetic':'Outward integer fixed-point intervals; no optimizer or floating-point verification.'}
 args.output.write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps({'tilt':result['tilt'],'weighted_pressure_bounds':result['weighted_pressure_bounds'],'certified_upper':result['certified_upper'],'a_minus_T_b_lower':result['a_minus_T_b_lower'],'output':str(args.output)},indent=2))
if __name__=='__main__':main()
