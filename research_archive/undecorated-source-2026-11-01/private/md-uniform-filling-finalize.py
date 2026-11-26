from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,subprocess

tmp=Path('/private/tmp')
pub=tmp/'murakamis_dream-publication'
work=Path('/Users/sasha/volume-conjecture')
archive=work/'research_archive/undecorated-source-2026-11-01'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=pub,text=True).strip()
assert head=='09cd63c5c5c1b1c8ce8805a7536e0f33e56a9d19'
assert not subprocess.check_output(['git','status','--porcelain'],cwd=pub,text=True).strip()
assert subprocess.check_output(['git','rev-parse','origin/main'],cwd=pub,text=True).strip()==head
for name in ['murakamis-current-research-handoff.json','murakamis-current-turn-status.json']:
    p=tmp/name
    if p.exists():
        dst=archive/'previous-handoffs'/f'{p.stem}-{sha(p)[:16]}.json'
        dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,dst)
pdf=pub/'docs/papers/conway-composition.pdf'
data={
 'updated_utc':datetime.now(timezone.utc).isoformat(),
 'goal':'get the most general equality AND show that it is indeed the hyperbolic volume involved',
 'goal_status':'active; not complete or blocked',
 'current_turn':'Published finite filling-supremum theorem; preserved exact cyclic transfer, grade-block algebra and geometric obstructions. No new volume family.',
 'public_checkout':str(pub),'workspace':str(work),'public_head':head,
 'public_clean':True,'pushed':True,'pages_run':41292433740,'pages_conclusion':'success',
 'live_files_verified':5,'paper_pages':302,'paper_pdf_sha256':sha(pdf),
 'latest_user_request':'Pyramid caption corrected and live-verified: Ideal hyperbolic pyramid; all five vertices ideal; shaded triangles named; quadrilateral gluing face. No Euclidean disclaimer.',
 'published_note':'notes/actual_uniform_filling_supremum_bound.md',
 'published_manuscript':'manuscript/sections/N-uniform-filling-bound.tex',
 'reproduce':'python3 repro/run_research_checks.py filling-supremum',
 'finite_theorem':{
  'single':'For deg H<=N-1, |L_N^n H|<=(1+|n|/2)||H|| on [-2,2]. If H vanishes at every distinct spectral node, cost improves to (N-1)/N independently of n; double-node derivatives retained.',
  'shared':'Apply tensor product functionals after the original common-face coefficient. One-sided factors have node vanishing. The unsplit full-minus-CROSS polynomial vanishes on the product node grid.',
  'unsplit_cost':'product_e(1+|n_e|/2)-product_e(1/N+|n_e|/2)',
  'proof':'Exact midpoint residues from Chebyshev ODE and elementary Riesz finite interpolation; complex/vector trigonometric derivative bound. Fixed twist costs are level independent.',
  'scope':'Original connected flat-plat and matched simple-sphere Morse source identities with original mark/targets/framing. No source exponential estimate or new volume theorem is inferred.',
  'prior_coverage':'Earlier Fourier-Hermite Gram theorem already has a level-uniform dual cost in another Hilbert norm. New direct original-numerator supremum and node-vanishing improvements are distinguished.'
 },
 'validation':{
  'finite':'168 cyclotomic derivative modes; 11 Chebyshev levels; 33 original monomial, 60 signed crossing-power and 36 compressed-block identities.',
  'manuscript':'30 displays and 113 inline formulas preserved; 0 typesetting warnings; pages visually checked.',
  'guide':'1062 pages checked, no broken local resources; new note/frontier/reproduction checked in browser at desktop and mobile sizes.',
  'reports':['/private/tmp/md-uniform-filling-appendix-fidelity.json','/private/tmp/md-uniform-filling-book-check.json','/private/tmp/md-uniform-filling-browser-check.json','/private/tmp/md-uniform-filling-live-check.json']
 },
 'previous_public_baseline':{
  'commit':'bb6d98a0e523dc0ee622398c4d10d439ff9af57b',
  'scope':'Balanced two-sided terminal decoration of any oriented simple triangulated sphere with chosen dual matching gives long fixed filling volume limits, with knot parity and all original/added fillings long. Added tangles generally change the knot. Directed circle-tree certificates have all-orders microscopic expansion and selected geometric-factor consequence.',
  'handoff':'/private/tmp/md-balanced-planar-and-directed-allorders-handoff.json'
 },
 'private_continuation':{
  'archive':str(archive),
  'cyclic_transfer':'md-undecorated-bipyramid-exact-cyclic-transfer.md: actual opposite-offset bipyramid source is a trace on two pending degrees. One marked grade increase d, north grade preservation, south drops totaling d. Common S^d extraction is automatic by homogeneity; generic exact coefficient/trace checks pass.',
  'grade_blocks':'md-undecorated-bipyramid-signed-grade-blocks.md, SHA f87406f16980db5d56ba0c2f173fb709d4c17cbca4903af7ca74c9937a7a7dd1. North blocks f(C_g)J_g, actual south coefficient blocks, full nonincreasing grade paths. O_m(N^(m/2)) grade patterns for fixed m. Full-grade conjugate Gram pairing and indefinite J-unitarity are limited statements; arbitrary even rows are not conjugate partners.',
  'telescope':'Exact aligned two-row boundary specialization has uniform bound 2N^4, retaining both endpoints. Checked directly from original resolvent coefficients at N3..12. It does not estimate the opposite-offset closed cyclic source.',
  'geometry':'Even bipyramids m>=6 with either matching offset fail local complete-radius balance at every legal mark: r=4cos^2(pi/m)>=3, strict gap<-1/10. The optimized unconditioned envelope also exceeds the complete value. Not a volume-conjecture counterexample. Native inversion figure and exact checks retained.',
  'fractional_flow':'Comparison polytope is integral but entropy is concave; a fractional maximizer need not be integral. Completing fractional rows changes loads; local positive-volume boundary obstruction is not a closed-source counterexample.',
  'terminal_tangles':'Turned long factors with opposite powers do not cancel relative to endpoints. Branched-cover amalgam and torsion certify this local claim; no universal claim about external closures.',
  'half_charge':'One-sided normals reduce to exact value projectors/half-charge combs with original peripheral logarithms. Half-charge alone does not give an orbifold filling representation.'
 },
 'remaining_tasks':[
  'For the actual unchanged opposite-offset bipyramid prove ||D_N||_infty <= exp(N(Vol(Y)/(2pi)-eta+o(1))), D_N=full-CROSS, eta>0, both parities, shared constraints and signs retained.',
  'Separately verify applicability of the nonzero all-CROSS long-filling asymptotic and primitive geometric identification to this literal general-Morse diagram. Existing public all-CROSS theorem is stated for certified flat plats. Finite source identity alone is not this verification.',
  'General arbitrary short fillings and arbitrary hyperbolic knots remain open. No new equality class has been established in this continuation.'
 ],
 'next_steps':[
  'Start from the frozen cyclic transfer and signed grade blocks. Do not repeat publication/caption/norm proof work.',
  'Parallelize the signed-product inequality and precise general-Morse all-CROSS applicability proof. Retain all endpoint degree states and avoid independently optimized local radii.',
  'Do not confuse a full-source bound at augmented volume with the smaller filled volume: need a strict complementary gap plus a nonzero geometric term.',
  'Preserve every private result in the archive; only the finite supremum theorem was promoted this turn.'
 ]
}
for name in ['murakamis-current-research-handoff.json','murakamis-current-turn-status.json','md-uniform-filling-current-handoff.json']:
    (tmp/name).write_text(json.dumps(data,indent=2)+'\n')
(archive/'current-handoff.json').write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps({'head':head,'goal_status':'active','paper_pages':302,'archive':str(archive)},indent=2))
