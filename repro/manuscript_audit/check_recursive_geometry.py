#!/usr/bin/env python3
"""Bounded equation/reference record; not a verification of the geometric proof."""
import hashlib
import json
import re
from pathlib import Path
import sympy as s

import argparse, sys
if sys.flags.optimize:
    raise SystemExit('Run without -O: exact checks use assertions.')
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--output', required=True, help='Write a fresh JSON record here.')
args = parser.parse_args()
Path(args.output).resolve().parent.mkdir(parents=True, exist_ok=True)

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(args.output).resolve()
read_scope = {
    'manuscript/sections/04-geometry.tex': 'Full chapter',
    'manuscript/sections/07-marked-geometry.tex': 'Full chapter',
    'manuscript/sections/D-marked-cell-calibration.tex': 'Full appendix, including the integrated filling-chain paragraph',
    'manuscript/sections/09-reproduction.tex': 'Rate-transfer proposition and geometry/source dependency paragraphs; scope statements',
    'manuscript/sections/01-introduction.tex': 'Completed grammar, main theorem, exclusions, fixed-diagram quantifiers',
    'manuscript/sections/03-entropy.tex': 'Action, strict-domain/barrier input and forced root gate',
    'manuscript/sections/06-packet.tex': 'Selected source branch, local shear, Hessian and nonzero local packet',
    'manuscript/sections/08-filling.tex': 'Filling action and cusp-Hessian conventions only; not a fresh audit of the whole period',
    'notes/actual_conway_single_leaf_geometric_composition.md': 'Sections 4–5',
    'notes/actual_conway_general_strict_mask_geometry.md': 'Sections 3–5',
    'notes/actual_conway_general_mask_marked_filling.md': 'Sections 1–3',
    'notes/positive_conway_geometric_incidence.md': 'Full note; comparison of older broader grammar and its flat annular boundary case',
    'notes/general_source_regulator_hyperbolic_equality.md': 'Sections 1–6 in full',
    'notes/general_peripheral_representation_volume_bound.md': 'Sections 1–3, especially the common conical boundary homotopy',
    'notes/actual_pretzel_marked_regulator_and_filling_action.md': 'Sections 3 and 5; primitive/regulator and same-boundary filling-chain conventions',
}
sources = []
for name, scope in read_scope.items():
    p = ROOT / name
    sources.append({'path': name, 'sha256': hashlib.sha256(p.read_bytes()).hexdigest(), 'reading_scope': scope})

# Exact projective equations used in Appendix D, at independent E and R.
E, R = s.symbols('E R', nonzero=True)
def whites(e, r):
    return [s.Matrix([[1,0],[0,e]]), s.Matrix([[1,e-1],[0,e]]),
            s.Matrix([[e-r,r*(1-e)],[e-1,1-e*r]]), s.Matrix([[r,0],[1-e,e*r]])]
def projectively_equal(P, Q):
    p, q = list(P), list(Q)
    return all(s.cancel(p[i]*q[j]-p[j]*q[i]) == 0
               for i in range(4) for j in range(i+1,4))
W = whites(E,R)
S = s.Matrix([[0,-E*R],[1,-1-E]])
A = s.Matrix([[R,-R],[1,E*R-1-E]])
B = s.Matrix([[R/E-1-1/E,R],[-1,R]])
checks = {}
for i,j in [(0,0),(2,2),(3,1)]:
    checks[f'pure_word_{i}_{j}'] = projectively_equal(W[i]*S, S.subs(E,1/E)*W[j])
for i,j in [(0,2),(2,0),(1,3)]:
    checks[f'odd_word_{i}_{j}'] = projectively_equal(W[i].inv()*B*W[j].inv()*A,s.eye(2))
T = s.Matrix([[0,R-1],[1,-1]])
C = s.Matrix([[1,-R],[1,-1]])
for j in range(4):
    checks[f'turn_{j}'] = projectively_equal(T*W[(j+1)%4], whites(1/E,1-R)[j]*T)
    checks[f'closing_{j}'] = projectively_equal(C*whites(1/E,R)[j], W[(2-j)%4]*C)

# Source shear, primitive multiplier and action/boundary normalization.
v, eps, t = s.symbols('v eps t')
V = -2*v
checks['half_twist_G_correction'] = s.simplify(2*s.pi*s.I*(-eps*v*v/(4*s.pi*s.I)) + eps*V*V/8) == 0
chi = t-eps*v/(2*s.pi*s.I)
checks['primitive_shear'] = s.simplify(-2*s.pi*s.I*t-eps*V/2+2*s.pi*s.I*chi) == 0
Tphase = s.symbols('Tphase', nonzero=True)
Z = (1+E)/(1+Tphase)
checks['rho_selected_source'] = s.cancel(Z/(1+E-Z)-1/Tphase) == 0
checks['Q_selected_source'] = s.cancel((E-Z)/(Z-1)-(E*Tphase-1)/(E-Tphase)) == 0
checks['volume_primitive_differential'] = s.simplify(s.Rational(1,2)*(-2*v)*(-2*s.pi*s.I)-2*s.pi*s.I*v) == 0
a,b,p = s.symbols('a b p', real=True, nonzero=True)
chi = a+s.I*b
U = -2*s.pi*s.I*chi
V = (-2*s.pi*s.I-U)/p
chirp = s.pi*s.I*(chi-1)**2/(2*p)
checks['filled_boundary_cancellation'] = s.simplify(2*s.pi*s.re(chirp)+s.re(U)*s.im(V)/2) == 0

# Pullback of the tube metric in u=log|d-q|, r=y/|d-q|.
r,dr,du,dtheta = s.symbols('r dr du dtheta', positive=True)
halfspace = dr**2/r**2+2*dr*du/r+(1+r**2)*du**2/r**2+dtheta**2/r**2
tube = dr**2/(r**2*(1+r**2))+(1+r**2)/r**2*(du+r*dr/(1+r**2))**2+dtheta**2/r**2
checks['tube_metric_substitution'] = s.factor(tube-halfspace) == 0
assert all(checks.values()), checks

# Resolve the actual manuscript input tree; do not scan unrelated archived TeX.
seen = set()
def include(path):
    path = path.resolve()
    if path in seen or not path.is_file():
        return
    seen.add(path)
    body = path.read_text()
    for rel in re.findall(r'\\(?:input|include)\{([^}]+)\}',body):
        pth = ROOT/'manuscript'/rel
        if not pth.suffix:
            pth = pth.with_suffix('.tex')
        include(pth)
include(ROOT/'manuscript/main.tex')
labels = {}
for path in seen:
    for lab in re.findall(r'\\label\{([^}]+)\}',path.read_text()):
        labels.setdefault(lab, []).append(str(path.relative_to(ROOT)))
reference_report = {}
for name in list(read_scope)[:4]:
    refs = re.findall(r'\\(?:eqref|ref|autoref|cref|Cref)\{([^}]+)\}',(ROOT/name).read_text())
    bad = {x:labels.get(x,[]) for x in refs if len(labels.get(x,[])) != 1}
    reference_report[name] = {'reference_occurrences':len(refs),'nonunique_or_missing':bad}
    assert not bad, (name,bad)

nodes = [
 {'id':'scope','claim':'Literal completed grammar, both root children completed; endpoint test gives one knot','inputs':[],'status':'stated hypothesis and finite topology test'},
 {'id':'strict','claim':'Selected complete source has strict unique stationary angles','inputs':['scope'],'status':'imported entropy/response theorem; not fully reproved in this bounded audit'},
 {'id':'cells','claim':'Ordered leaf/prism faces and derivative identities fit isometrically','inputs':['strict'],'status':'read explicit formulas and ordered gluing argument'},
 {'id':'incidence','claim':'Convex assembly and labeled projection cuts recover original S3 augmented exterior','inputs':['scope','cells'],'status':'read geometric incidence and finite cut argument, including completed-grammar restriction'},
 {'id':'complete','claim':'Complete oriented augmented metric; volume 2 pi F0','inputs':['incidence'],'status':'read edge return and cusp decoration construction'},
 {'id':'source_germ','claim':'Actual finite source selects the stated holomorphic action/shear','inputs':['strict'],'status':'imported exact recurrence/packet theorem; no independent full asymptotic audit here'},
 {'id':'representation','claim':'Full local face/edge words define nearby representation of same augmented group; main cusps parabolic','inputs':['complete','source_germ'],'status':'read full construction; exact checks of fourteen pure/odd/turn/closing relations; nine prism identities read but not independently expanded here'},
 {'id':'marking','claim':'Original primitive U=-2 pi i chi, V=-2 partial Phi, power epsilon-2p','inputs':['representation','scope'],'status':'read original collar and two-rectangle lattice; exact normalization checks'},
 {'id':'regulator','claim':'Vol(rho)=Im G-(1/2)sum ReU ImV, G=2 pi i Phi','inputs':['complete','marking'],'status':'read same fundamental-chain boundary calculation and constant anchor'},
 {'id':'saddle','claim':'Reciprocal-slope IFT selects a nearby solution for independently long signed p','inputs':['source_germ','marking'],'status':'read nondegenerate diagonal cusp Jacobian and fixed polydisk argument'},
 {'id':'log_link','claim':'Actual log-link periods are U,V before multiplying slopes','inputs':['representation','saddle'],'status':'read bounded generator paths, q escape and rank-two Euclidean development'},
 {'id':'metric','claim':'Primitive angular period -2 pi i gives smooth solid torus; unfilled main cusp remains complete','inputs':['scope','log_link'],'status':'read entire-tube construction and descent; exact tube metric check'},
 {'id':'filling_chain','claim':'Representation volume equals completed metric volume with unchanged chain normalization','inputs':['regulator','metric'],'status':'missing explanation found and now integrated in the manuscript; matching §6 hypotheses verified'},
 {'id':'action_volume','claim':'2 pi Re S equals actual original filled knot-complement volume','inputs':['saddle','filling_chain'],'status':'exact chirp/boundary cancellation checked'},
 {'id':'quantum_remainder','claim':'Entire finite invariant has nonzero contribution and smaller full remainder','inputs':['source_germ'],'status':'separate source/alias/period inputs; not supplied by geometry and not newly reproved here'},
 {'id':'limit','claim':'Full invariant volume limit','inputs':['action_volume','quantum_remainder'],'status':'rate-transfer proposition checked; geometric identity and global remainder remain distinct inputs'},
]
done=set()
for node in nodes:
    assert set(node['inputs']) <= done, node
    done.add(node['id'])
record = {
 'scope':'Bounded read of chapters 04/07 and Appendix D, plus relevant dependencies and section 09 rate transfer. No full-manuscript proof certification.',
 'correction':{'file':'manuscript/sections/D-marked-cell-calibration.tex','pre_correction_sha256':'6750ec335d346ef3f8e28e85b4434e35f7791c5461fcf0e33a13d38a79a7f932','state':'integrated before this record','description':'Explicit same-boundary-triangulation axis comparison and zero-volume solid-torus extension'},
 'sources':sources,'exact_checks':checks,'reference_resolution':reference_report,'dependency_nodes':nodes,
 'omissions':['No new verification of rational inequality certificates','No full re-audit of complex Fourier contour/charge domination','No independent full expansion of nine prism compatibility matrices','No formal verification of metric completeness or fundamental-chain arguments']
}
OUT.write_text(json.dumps(record,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'record':str(OUT),'exact_checks':len(checks),'dependency_nodes':len(nodes),'references':reference_report,'source_count':len(sources)},indent=2))
