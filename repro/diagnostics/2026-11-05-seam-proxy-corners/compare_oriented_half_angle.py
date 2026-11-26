#!/usr/bin/env python3
"""Fixed-reference scalar comparison using inherited oriented lower bounds."""
import argparse,hashlib,json
from fractions import Fraction as F
from pathlib import Path
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2]
SOURCE=ROOT/'repro/diagnostics/2026-11-05-seam-boundary/real-seam-half-pair-diagnostic.json'

def main():
 ap=argparse.ArgumentParser(description=__doc__)
 ap.add_argument('--output',type=Path,required=True)
 args=ap.parse_args();assert not args.output.exists(),'choose a fresh output'
 data=json.loads(SOURCE.read_text());r4=data['actual_reference'][1][0]
 dx=.5-r4;cost0=float(F(11,2))*dx**2;cost1=float(F(151,20))*dx**2
 plane=data['actual_pair_plane_real'];collar=data['collar_rate_cost_2Delta'];occupation=float(F(63,8000))
 c0,c1=[r['explicit_algebraic_value'] for r in data['profiles']]
 ceilings={'height_resolved':float(F('.386681')+F('.515591')),'exact_half_angle':c0+c1,'rational_half_angle_upper':float(F('.291561')+F('.443534'))}
 rows={k:dict(source_ceiling=s,collar=collar,resulting_upper=cost0+cost1+s+collar-plane-occupation) for k,s in ceilings.items()}
 result=dict(scope='Fixed preserved alternating reference only. Floating reference/action data and exact inherited rational coefficients; no optimizer, new phase evaluation, outward certificate or universal reference claim.',reference_four_real=r4,real_displacement=dx,first_coordinate_lower_cost=cost0,second_coordinate_lower_cost=cost1,total_connector_lower_cost=cost0+cost1,actual_pair_plane=plane,retained_occupation=occupation,comparisons=rows,input_sha256=hashlib.sha256(SOURCE.read_bytes()).hexdigest(),script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
 args.output.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(rows,indent=2))
if __name__=='__main__':main()
