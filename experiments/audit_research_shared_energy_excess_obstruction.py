#!/usr/bin/env python3
"""Verify the registered rational original-source energy excess certificate.

No optimizer, numerical builder, or private fixture is imported. The exact
source/flow checks and Arb bounds are the reviewed certificate algorithm.
"""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import argparse
import json
import sys
from flint import arb, ctx

sys.path.insert(0, str(Path(__file__).resolve().parent))
from audit_actual_original_marked_face_coefficient import morse_faces

def verify(data,M=8192):
 ctx.prec=192;ports=data['ports'];zero=set(data['protected']);ordinary=data['ordinary'];chart=morse_faces(3,data['word'],0)
 assert chart['circles']==list(map(tuple,ports)) and (0,chart['v'])==tuple(data['protected']);assert ordinary==[f for f in range(chart['faces']) if f not in zero]
 tris=[t for x,b,c,y in ports for t in [(x,b,y),(x,c,y)]];assert len({tuple(sorted(t)) for t in tris})==14 and all(len(set(t))==3 for t in tris)
 edges=Counter(tuple(sorted((t[j],t[(j+1)%3]))) for t in tris for j in range(3));assert len(edges)==21 and set(edges.values())=={2}
 assert tuple(ports[2])==(0,1,6,4) and data['fixed_half_face']==1
 assert [(r['port'],r['side']) for r in data['rows']]==[(e,s) for e in range(7) for s in (0,1) if (e,s)!=(2,1)]
 qs=[F(*r['value']) for r in data['variables']];assert min(qs)>=0;assert sorted(i for r in data['rows'] for i in r['variables'])==list(range(len(qs)))
 loads={f:F(0) for f in ordinary};loads[1]=F(1,2);coupons=[{f:F(0) for f in p} for p in ports];coupons[2][1]=F(1,2)
 for row in data['rows']:
  e,s=row['port'],row['side'];tri=tris[2*e+s];fs=[f for f in tri if f not in zero];assert fs==row['faces'] and len(fs)==len(row['variables']);assert sum((qs[i] for i in row['variables']),F(0))==F(1,2)
  for f,i in zip(fs,row['variables']):assert data['variables'][i]['name']==[e,s,f];loads[f]+=qs[i];coupons[e][f]+=qs[i]
 assert all(v==1 for v in loads.values())
 for e,(x,b,c,y) in enumerate(ports):
  assert sum(coupons[e].values())==1 and all(coupons[e].get(f,F(0))==0 for f in zero)
  if e==2:assert coupons[e][b]>F(1,2) and coupons[e][c]==0 and coupons[e][x]==0
  else:assert coupons[e][b]<F(1,2) and coupons[e][c]<F(1,2)
 def ab(q):return arb(q.numerator)/q.denominator
 def lob(a):
  t=arb(0)
  for n in range(1,M+1):t+=(2*n*a).sin()/(2*n*n)
  return t+arb(0,arb(1)/(2*M))
 cache={}
 def f(q):
  if q in (0,F(1,2)):return arb(0)
  if q not in cache:cache[q]=(lob(arb.pi()*ab(q))+lob(arb.pi()*ab(F(1,2)-q)))/arb.pi()
  return cache[q]
 entropy=sum((f(q) for q in qs),arb(0));L=data['complete_curvatures'];assert L==[0,16,9,25,1,4,0,1,9]
 qc={}
 def Q(tri):
  key=tuple(sorted(L[f] for f in tri))
  if key in qc:return qc[key]
  w=[arb(v) for v in key if v]
  if len(w)==1:v=w[0].log()/2
  else:
   D=sum(w[i]*w[j] for i in range(len(w)) for j in range(i+1,len(w))).sqrt();v=arb(0)
   for a in w:
    t=(a/D).atan();v+=(lob(t)+lob(arb.pi()/2-t))/arb.pi()+t/arb.pi()*a.log()
  qc[key]=v;return v
 upper=sum((Q(t) for t in tris),arb(0))-sum((arb(L[f]).log() for f in ordinary),arb(0));gap=entropy-upper;assert gap>arb('.50'),gap
 result={'status':'PASS','scope':'Exact feasible ORIGINAL shared flow proves the actual even-level conditioned spectral energy exceeds completePhi. This disproves only the stronger E<=exp(N Phi+o(N)) proposal, not its mass-gap budget or joint-score criterion, and not a quantum-rate bound.','counts':{'ports':7,'triangle_rows':len(data['rows']),'rational_variables':len(qs),'ordinary_targets':len(loads),'strict_cross_ports':6,'protected_outer_one_sided_port':1},'energy_entropy_lower':str(entropy.lower()),'complete_potential_upper':str(upper.upper()),'excess_lower':str(gap.lower()),'certified_excess':'.50','precision_bits':ctx.prec,'fourier_terms':M,'coupon_exponents':[{str(f):[q.numerator,q.denominator] for f,q in row.items()} for row in coupons]}
 return result

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--certificate', type=Path,
        default=Path(__file__).with_name('research_shared_energy_excess_obstruction_certificate.json'))
    parser.add_argument('--output', type=Path,
        default=Path(__file__).with_name('research_shared_energy_excess_obstruction_results.json'))
    args = parser.parse_args()
    result = verify(json.loads(args.certificate.read_text()))
    args.output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({k:v for k,v in result.items() if k != 'coupon_exponents'}, indent=2))

if __name__ == '__main__':
    main()
