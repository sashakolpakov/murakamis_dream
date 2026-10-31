"""Exact fixed-slope endpoint certificate using the reviewed rational engine."""
from pathlib import Path
from fractions import Fraction as F
import runpy,json
base=runpy.run_path(str(Path(__file__).with_name('verify_conway_two_leaf_block_alias_certificate.py')))
I,S,g,k,m,gm,logi,sinpi,L2=[base[s] for s in ['I','S','g','k','m','grad_m','logi','sinpi','LOG2']]
p=[F(a,10**6) for a in [352416,352416,647584]]
v=[F(a,10**6) for a in [570352,246081,753919]]
assert base['feasible'](p) and p[0]<F(1,2)
assert base['feasible'](v)
mu=lam=-2*L2
P=g(p[0])+m(p)+mu*p[1]-lam*p[2]
H=k(v[0])+m(v)
grad=gm(v);grad[0]+=-logi(2*sinpi(v[0]/2))
records=[]
for w in base['VERTICES'][2]:
 gap=P-H-sum((grad[j]*(w[j]-v[j]) for j in range(3)),I(0))-mu*w[1]+lam*w[2]
 assert gap.lo*50>S*3
 records.append({'vertex':list(map(str,w)),'gap_lower':str(F(gap.lo,S))})
res={'status':'PASS','exact_rational_arithmetic':True,'lambda_mu':'-2log2',
     'certified_gap':'3/50','pure':list(map(str,p)),'alias':list(map(str,v)),
     'minimum_lower':str(min(F(r['gap_lower']) for r in records)),'vertices':records}
import argparse
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--output',type=Path)
args=parser.parse_args()
if args.output:
 args.output.write_text(json.dumps(res,indent=2)+'\n')
print(json.dumps(res,indent=2))
