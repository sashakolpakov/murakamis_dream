#!/usr/bin/env python3
"""Exact algebra and dependency checks for the bounded Appendix O/P audit.
This is not a proof assistant or a certification of the analytic theorems.
"""
from pathlib import Path
import json,hashlib,re
import sympy as s
import argparse, sys
if sys.flags.optimize:
    raise SystemExit('Run without -O: exact checks use assertions.')
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--output', required=True, help='Write a fresh JSON record here.')
args = parser.parse_args()
Path(args.output).resolve().parent.mkdir(parents=True, exist_ok=True)

repo=Path(__file__).resolve().parents[2]
files=[
'manuscript/sections/O-morse-geometric-contribution.tex',
'manuscript/sections/P-weak-balance.tex',
'manuscript/sections/N-uniform-filling-bound.tex',
'manuscript/sections/L-balanced-terminal-fans.tex',
'notes/actual_morse_geometric_contribution.md',
'notes/actual_morse_cross_filling_period.md',
'notes/general_weak_balance_volume.md',
'notes/research_matched_sphere_morse_source.md',
'notes/actual_balanced_terminal_fan_volume.md',
'notes/actual_marked_deformed_circle_pattern.md',
'notes/actual_deformed_circle_primitive_collar.md',
'notes/actual_complete_core_geometric_deformation.md',
'notes/actual_augmented_plat_critical_scheme.md',
'notes/actual_original_boundary_stationary_character.md',
'notes/general_source_regulator_hyperbolic_equality.md',
'notes/general_peripheral_representation_volume_bound.md',
'notes/actual_pretzel_marked_regulator_and_filling_action.md',
'notes/bloch_lift_and_boundary_torsor.md',
'notes/general_marked_multicusp_gluing_rigidity.md']
manifest={f:hashlib.sha256((repo/f).read_bytes()).hexdigest() for f in files}
nodes=[
('input',[], 'Finite oriented simple triangulated sphere; dual perfect matching; nonmatching marked edge; retained cyclic frames and epsilon; original component test.'),
('topology',['input'],'Inverse cut gives the original S3 augmented diagram, primitive disk bases and n=epsilon-2p.'),
('packing',['input'],'Strict Hall feasibility, interior entropy maximizer, injective center development and support halfspaces give positive ideal right-angled cut polyhedron.'),
('complete_metric',['topology','packing'],'Original face pairings and cusp links give complete Y with Vol(Y)=2Vol(Q).'),
('finite_source',['topology'],'Exact homogeneous Morse coefficient, original degree d targets, protected zeros, full Hermite and raw scalars.'),
('complete_action',['packing','complete_metric','finite_source'],'Original endpoint determinant calibration and facet coning give P(q*)=Phi=Vol(Y)/(2pi), gradient0.'),
('circle_germ',['packing','complete_action'],'Marked line-circle Jacobian invertible; analytic common pattern and source stationary radii agree.'),
('group_germ',['topology','circle_germ'],'Full reflection prefixes, cup/cap identities, threading and signed Hurwitz maps give actual framed rho_delta near rho0.'),
('peripheral',['group_germ'],'Primitive logs U=-Log R0-epsilon Log(-J), V=2Log(-J); actual main groups remain parabolic.'),
('regulator',['complete_action','peripheral'],'Fixed oriented fundamental-chain volume differential gives absolute corrected action identity.'),
('critical_point',['circle_germ','peripheral'],'Multivariate reciprocal-slope IFT gives first charge; U+pV=-2pi i and Im delta>0.'),
('metric_completion',['complete_metric','group_germ','peripheral','critical_point'],'Actual small log periods, nonunit auxiliary multiplier and primitive angle2pi fill smooth solid tori; main cusps remain complete.'),
('filled_action',['regulator','metric_completion'],'Same boundary triangulation axis comparison identifies 2pi Re S with actual filled metric volume.'),
('central_asymptotic',['finite_source','complete_action','critical_point'],'O analytic part: H1/H2, first Gaussian and all charge currents give nonzero central period at both parities.'),
('central_volume',['filled_action','central_asymptotic'],'Central contribution rate equals actual original filled complement volume.'),
('weak_balance',['complete_action'],'Additional actual complete-radius inequalities, with fixed finite data.'),
('remainder',['finite_source','complete_action','weak_balance'],'P power flattening and one shared torus give full-minus-central real-cube gap.'),
('hermite_bound',['finite_source'],'N finite operator norm transfers the remainder at subexponential cost for fixed powers.'),
('full_volume',['topology','central_volume','remainder','hermite_bound'],'Increase fixed long-twist threshold; central rate dominates, hence original normalized invariant volume limit.')]
node_map={k:{'requires':req,'claim':claim} for k,req,claim in nodes}
done=set();order=[]
while len(done)<len(nodes):
 ready=[k for k,_,_ in nodes if k not in done and set(node_map[k]['requires'])<=done]
 assert ready,'Dependency cycle'
 for k in ready:done.add(k);order.append(k)
checks=[]
J,R,m=s.symbols('J R m',nonzero=True)
for eps in (-1,0,1):
 pref=m*R*(J**-1-1)**(-eps)
 selected=s.cancel(pref/R*(J**-1-1)**eps)
 other=s.cancel(pref*(J-1)**eps)
 assert s.cancel(selected-m)==0
 assert s.cancel(other-m*R*(-J)**eps)==0
 checks.append(f'primitive meridian eigenvalues and determinant, epsilon={eps}')
a,b,p=s.symbols('a b p',real=True)
delta=a+s.I*b;V=-4*s.pi*s.I*delta;U=-2*s.pi*s.I-p*V
lhs=s.re(-2*s.pi*s.I*p*delta**2+2*s.pi*s.I*delta)
rhs=s.im(U)*s.re(V)/(4*s.pi)
assert s.expand(lhs-rhs)==0
checks.append('O(mcgeq24) exact real boundary cancellation for either sign of p')
ua,ub,va,vb,dua,dub,dva,dvb=s.symbols('ua ub va vb dua dub dva dvb',real=True)
dvol=(va*dub-ua*dvb)/2
dcorr=(va*dub+ub*dva)/2
daction=(-ua*dvb-ub*dva)/2
assert s.expand(dvol-dcorr-daction)==0
checks.append('O(mcgeq18-20) exact differential after boundary correction')
R_t,X=s.symbols('R_t X',real=True)
rad=s.exp(X)*s.tanh(R_t);height=s.exp(X)/s.cosh(R_t)
rr=s.simplify((s.diff(rad,R_t)**2+s.diff(height,R_t)**2)/height**2)
xx=s.simplify((s.diff(rad,X)**2+s.diff(height,X)**2)/height**2)
rx=s.simplify((s.diff(rad,R_t)*s.diff(rad,X)+s.diff(height,R_t)*s.diff(height,X))/height**2)
tt=s.simplify(rad**2/height**2)
assert s.simplify(rr-1)==0 and s.simplify(xx-s.cosh(R_t)**2)==0 and rx==0 and s.simplify(tt-s.sinh(R_t)**2)==0
checks.append('O(mcgeq28) exact hyperbolic tube metric pullback')
# Internal references in O/P must have a source label, and labels must be unique.
texfiles=list((repo/'manuscript').rglob('*.tex'))
labels={}
for file in texfiles:
 if 'build' in file.parts:continue
 for lab in re.findall(r'\\label\{([^}]+)\}',file.read_text()):
  labels.setdefault(lab,[]).append(str(file.relative_to(repo)))
refs={}
for f in files[:2]:
 txt=(repo/f).read_text()
 found=re.findall(r'\\(?:eqref|ref|hyperref)\{([^}]+)\}',txt)
 found+=re.findall(r'\\hyperref\[([^]]+)\]',txt)
 missing=[lab for lab in found if lab not in labels]
 assert not missing,(f,missing)
 duplicate_targets={lab:labels[lab] for lab in set(found) if len(labels[lab])!=1}
 assert not duplicate_targets,duplicate_targets
 refs[f]={'references':len(found),'distinct_targets':len(set(found)),'missing':[],'duplicate_targets':[]}
out={'scope':'Bounded geometry interface audit, not full theorem formalization.',
 'source_hashes':manifest,'dependency_nodes':node_map,'topological_order':order,
 'dependency_cycle':False,'exact_checks':checks,'internal_reference_checks':refs,
 'limitations':['No reproof or rerun of analytic H1/H2 constants and Fourier tails.',
 'No proof-assistant verification of Hall packing, fundamental-chain differential, or metric completion.',
 'Full invariant conclusion requires weak balance/quantified remainder and fixed sufficiently long powers.']}
dest=Path(args.output).resolve()
dest.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'dependency_nodes':len(nodes),'exact_checks':len(checks),'reference_checks':refs,'output':str(dest)},indent=2))

