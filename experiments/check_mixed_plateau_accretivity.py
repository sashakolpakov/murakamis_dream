#!/usr/bin/env python3
"""Exact pair-Hessian algebra and outward scalar reserves for the full plateau.

Root holomorphy and original finite-source packets are established inputs;
this checker does not replace their contour proofs or assert a full-word VC.
"""
import argparse,hashlib,json
from pathlib import Path
from fractions import Fraction as R
import sympy as sy
from flint import arb,ctx
ROOT=Path(__file__).resolve().parents[1]
PROOF=ROOT/'notes/research_mixed_plateau_accretivity.md'
ap=argparse.ArgumentParser(description=__doc__)
ap.add_argument('--precision',type=int,default=256)
ap.add_argument('--output',type=Path,default=ROOT/'repro/results/research-mixed-plateau-accretivity.json')
args=ap.parse_args();assert args.precision>=160;ctx.prec=args.precision
P=arb.pi()
def ar(x):
 x=R(x);return arb(x.numerator)/x.denominator
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
DEPS=[
 'notes/research_mixed_transition_conditional_rectangles.md',
 'experiments/certify_mixed_transition_conditional_rectangles.py',
 'repro/results/research-mixed-transition-conditional-rectangles.json',
 'notes/research_mixed_asymmetric_low_conditional_packets.md',
 'experiments/certify_mixed_asymmetric_low_conditional_packets.py',
 'repro/results/research-mixed-asymmetric-low-conditional-packets.json',
 'notes/research_mixed_boundary_strip_bounds.md',
 'notes/research_mixed_central_outer_integral.md',
 'notes/research_mixed_local_outer_contribution.md',
 'notes/research_mixed_fourier_weight_continuation.md',
 'notes/research_mixed_outer_graph_contours.md',
 'notes/research_mixed_conditional_torus_composition.md',
]
hashes={p:sha(ROOT/p)for p in DEPS};ph=sha(PROOF);sh=sha(__file__)
for name in ['transition_conditional_rectangles','asymmetric_low_conditional_packets']:
 rec=json.loads((ROOT/('repro/results/research-mixed-'+name.replace('_','-')+'.json')).read_text())
 assert rec['status']=='passed'
 assert rec['script_sha256']==sha(ROOT/f'experiments/certify_mixed_{name}.py')
 assert rec['proof_sha256']==sha(ROOT/f'notes/research_mixed_{name}.md')
 for p,h in rec['dependencies'].items():assert sha(ROOT/p)==h,(name,p)
 assert rec['boundary_pieces']==(64 if name.startswith('transition') else 32)
u,p,v,q=sy.symbols('u p v q',real=True)
den=(u+p)**2+(v+q)**2
C=((u*p-v*q-1)*(u+p)+(u*q+p*v)*(v+q))/den
target=((u+p)**2-(p*v-u*q)**2)/den
assert sy.factor(u*p-(u+p)*C-target)==0
identities=['exact complex pair determinant']
checks={}
def positive(name,x):
 assert x>0,(name,str(x));checks[name]=str(x)
positive('inner cotangent cone',(-ar('.34')*P).exp()-(ar('.4')*P).cos())
positive('outer cotangent cone',(-ar('.114')*P).exp()-(ar('.44')*P).cos())
positive('asymmetric inner cone',(-ar('.42')*P).exp()-(ar('.48')*P).cos())
positive('asymmetric low outer cone',(-ar('.114')*P).exp()-(ar('.30')*P).cos())
def cr(x,h):return(2*P*ar(x)).sin()/((2*P*ar(h)).cosh()-(2*P*ar(x)).cos())
def ci(x,h):return(2*P*ar(h)).sinh()/((2*P*ar(h)).cosh()-(2*P*ar(x)).cos())
for x in ['.20','.46']:positive('inner real lower '+x,cr(x,'.17')-ar('.09'))
for x in ['.22','.45']:positive('outer real lower '+x,cr(x,'.057')-ar('.15'))
positive('inner real upper',ar('1.4')-(P*ar('.20')).cos()/(P*ar('.20')).sin())
positive('outer real upper',ar('1.21')-(P*ar('.22')).cos()/(P*ar('.22')).sin())
positive('inner imaginary upper',ar('.98')-ci('.20','.17'))
positive('outer imaginary upper',ar('.42')-ci('.22','.057'))
positive('inner imaginary height monotonicity',1-(P*ar('.4')).cos()*(P*ar('.34')).cosh())
positive('outer imaginary height monotonicity',1-(P*ar('.44')).cos()*(P*ar('.114')).cosh())
positive('shifted real cotangent lower',(P*ar('.91')).cos()/(P*ar('.91')).sin()+ar('3.5'))
positive('pair trace upper',ar(10)-ar('1.4')-ar('1.21')-7)
det=(1-ar('.98')**2)*ar('.24')**2/(ar('.24')**2+ar('1.4')**2)
positive('explicit pair eigenvalue reserve',P*det/10-ar('1/4000'))
positive('graph Jacobian reserve',ar('2.49')**2-1-ar('2.28')**2)
positive('graph left cotangent cone',P-ar('.057')/ar('.22')**2)
assert hashes=={p:sha(ROOT/p)for p in DEPS}
assert ph==sha(PROOF)and sh==sha(__file__)
record=dict(status='passed',precision_bits=args.precision,exact_identities=identities,scalar_margins=checks,scalar_comparisons=len(checks),pair_accretivity='1/4000',effective_cyclic_accretivity='1/2000',proof_sha256=ph,script_sha256=sh,dependencies_sha256=hashes,scope='Exact triangle determinant and scalar reserves for established holomorphic conditional roots. Supports the written unaliased constant-height plateau theorem; no selected-alias, curved-graph, or whole-period estimate.')
args.output.parent.mkdir(parents=True,exist_ok=True)
args.output.write_text(json.dumps(record,indent=2)+'\n')
print('PASS',len(identities),'exact identity and',len(checks),'strict scalar comparisons')
