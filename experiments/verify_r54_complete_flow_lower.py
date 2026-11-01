#!/usr/bin/env python3
"""Verify a complete-flow entropy lower bound with exact rational arithmetic.
No optimizer, floating-point evaluation, or approximate stationary equation
is used here. Geometry is the original marked simple-sphere complete source.
"""
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
from fractions import Fraction as F
import importlib.util,json,hashlib,argparse
if not __debug__:raise SystemExit('Do not run with -O')
def main():
 p=argparse.ArgumentParser(description=__doc__)
 p.add_argument('--repo',type=Path,default=ROOT)
 p.add_argument('--certificate',type=Path,default=ROOT / 'experiments/r54_complete_flow_lower_certificate.json')
 p.add_argument('--output',type=Path,default=Path('r54_complete_flow_lower_results.json'))
 args=p.parse_args()
 src=args.repo/'experiments/actual_singleton_sector_obstruction_certificate.json'
 original=json.loads(src.read_text());data=json.loads(args.certificate.read_text())
 assert data['source_certificate_sha256']==hashlib.sha256(src.read_bytes()).hexdigest()
 engine_path=args.repo/'experiments/verify_conway_two_leaf_block_alias_certificate.py'
 spec=importlib.util.spec_from_file_location('r54_exact_interval_engine',engine_path)
 e=importlib.util.module_from_spec(spec);spec.loader.exec_module(e)
 zero=set(original['source']['protected']);ports=original['source']['ports'];ordinary=original['ordinary']
 assert data['protected']==sorted(zero) and data['ordinary']==ordinary
 assert len(data['rows'])==2*len(ports)==108
 assert len(ordinary)==54
 loads={v:F(0) for v in ordinary};entropy=e.I(0);minimum=F(1)
 for idx,row in enumerate(data['rows']):
  crossing,side=divmod(idx,2);x,b,c,y=ports[crossing]
  assert row['crossing']==crossing and row['side']==side
  faces=[v for v in (x,b if side==0 else c,y) if v not in zero]
  assert row['faces']==faces
  values=[F(*a) for a in row['values']]
  assert len(values)==len(faces) and sum(values)==F(1,2) and min(values)>0
  for v,a in zip(faces,values):
   assert 0<a<=F(1,2);loads[v]+=a;minimum=min(minimum,a)
   entropy+=-e.J(a)-e.J(F(1,2)-a)
 assert all(a==1 for a in loads.values())
 lower=F(entropy.lo,e.S);upper=F(entropy.hi,e.S)
 assert lower>F(67687,1000),entropy.bounds()
 # A readable outward decimal enclosure, computed without binary floats.
 scale=10**12
 lo_dec=lower.numerator*scale//lower.denominator
 hi_dec=-((-upper.numerator*scale)//upper.denominator)
 def dec(n):return f'{n//scale}.{n%scale:012d}'
 result={'status':'certified','scope':'Original complete feasible-flow entropy lower bound only.',
  'source_normalization':'Phi=Vol(original augmented complement)/(2*pi)',
  'rows':108,'ordinary_targets':54,'protected':sorted(zero),
  'minimum_positive_corner':str(minimum),
  'entropy_bounds':entropy.bounds(),'entropy_decimal_enclosure':[dec(lo_dec),dec(hi_dec)],
  'certified_Phi_lower':'67687/1000',
  'arithmetic':'Outward integer fixed-point intervals at 10^40; Euler-product integrated log-sine with exact tail.',
  'optimizer_used_in_verification':False,'floating_point_used_in_verification':False,
  'source_certificate_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),
  'flow_certificate_sha256':hashlib.sha256(args.certificate.read_bytes()).hexdigest(),
  'engine_sha256':hashlib.sha256(engine_path.read_bytes()).hexdigest(),
  'verifier_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
 args.output.write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps({'status':result['status'],'Phi_lower':result['certified_Phi_lower'],
  'entropy_decimal_enclosure':result['entropy_decimal_enclosure'],'output':str(args.output)},indent=2))
if __name__=='__main__':main()
