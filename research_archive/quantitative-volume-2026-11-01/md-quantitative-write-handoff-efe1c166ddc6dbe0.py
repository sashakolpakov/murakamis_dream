from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,shutil,subprocess
tmp=Path('/private/tmp');pub=tmp/'murakamis_dream-publication'
archive=Path('/Users/sasha/volume-conjecture/research_archive/quantitative-volume-2026-11-01')
def preserve(p):
 if p.is_file():
  h=hashlib.sha256(p.read_bytes()).hexdigest()
  out=archive/(p.stem+'-'+h[:16]+p.suffix)
  if not out.exists():shutil.copy2(p,out)
head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=pub,text=True).strip()
live=json.loads((tmp/'md-quantitative-live-deployment.json').read_text())
assert live['commit']==head and all(row['equal'] for row in live['checks'])
assert not subprocess.check_output(['git','status','--porcelain'],cwd=pub,text=True).strip()
revision=json.loads((tmp/'md-quantitative-publication-validation.json').read_text())
now=datetime.now(timezone.utc).isoformat()
state={
 'updated_utc':now,
 'goal':'get the most general equality AND show that it is indeed the hyperbolic volume involved',
 'goal_status':'active',
 'current_turn':'progress: explicit degree-and-twist criterion upgraded from analytic limit to actual knot-volume theorem; full geometry, preferred cusp, operator corollary and detailed manuscript published',
 'public_checkout':str(pub),'public_head':head,'pushed':True,
 'pages_run':live['pages_run'],'live_verified':len(live['checks']),
 'latest_user_caption':'Schematic hyperbolic pyramid. All five vertices are ideal. Quadrilateral gluing face. Remains correct in source, live image and manuscript.',
 'previous_broader_volume_result':'Every fixed strict ordered Conway tree with independently sufficiently long fixed signed twists, arbitrary bare-component size/valence/adjacency. Uniform microscopic meridian profile and preferred cusp; intrinsic formulas transfer through the proved net-twist and closure reductions. Do not narrow these older theorems to circle-only trees.',
 'new_published_volume_theorem':{
  'class':'Any fixed literal ordered circle tree with at least one edge. Every vertex has an original crossing circle; main strands must form one knot with no internal extra component. Original endpoint frames, order, half turns and disk slopes are retained.',
  'definition':'Choose terminal root0. W_v=(prod_{w in Iminus}T W_w)R^n_v(prod_{w in Iplus}T W_w); close R^n0 T W_w cylindrically. Products ordered; physical T² half-turn retained.',
  'criterion':'S=sum_v d_v/(d_v²+n_v²)<=2^-25',
  'automatic_strictness':'One unturned circle H with turned child factors L yields H; terminal closure H/L is strict. No extra strict-angle test for this literal class. Two-vertex allodd case excluded by knot test.',
  'conclusion':'Actual knot complement hyperbolic; (2pi/N)log|K_N| -> its volume. F_N(q^s)/[F_N(1) A_N(s) H_N(s)]=1+O(N^-1) uniformly |s|<=R<1, eventually nonzero, both parities/composites. Graph/powers fixed beforeN.',
  'scalar':'q=e^{pi i/N};H_N=sin(pi s)/(Nsin(pi s/N));A_N=q^{a(D)s²/2},a(D)=-w(D)-sum n_v.',
  'preferred_cusp':'tauK=a(D)+2i sum_physical_edges cot(pi x_e*);F_N(e^{z/(2N)})/[F_N(1)Hcal_N(z)]=1+tauK*z²/(8pi iN)+O(N^-2), |z|<=2piR. Exact s-independent base/insertion rule proves the remainder under the same criterion.',
  'operator_period':'Any fixed genuine all-level quantum A-operator with finite initial ordinary-color data and singular-step Laurent/jet treatment gives exact P_N(P,c0)=K_N and hence the same volume limit. No classical geometric-factor identification asserted.',
  'explicit_bounds':['all |n_v|>=8192sqrt(E) suffices','add B terminal circles per original vertex of any m-vertex tree; new |n|>=B gives S<2m/B, so B>=2^26m suffices subject to knot/parity. This changes the knot.','R0 insertion preserves filled diagram, changes augmented exterior, contributes1/d to S; high-degree bare junctions may qualify.'],
  'normalized_length':'L_v²=(d_v²+n_v²)/(2d_v);S=.5 sum L_v^-2.',
 },
 'geometric_proof':{
  'topology':'Actual labeled ribbon insertion attaches one octahedron per edge per projection half; correct left/right order and terminal root half-turn. Each circle has d_v sectors, exactly one original signed seam. All primitive curves retained.',
  'local_chart':'Eight positive tetrahedra per edge, all shapes i atzero; |tau_v|<=.01 chart with exact full complex pants ratios and odd return matrices. C composed with T placement retained.',
  'path':'Psi_tau+i n tau/(2pi)=ic,0<=c<=1; |tau_v(c)|<=2pi c/[.98sqrt(d_v²+n_v²)]<.00111, Imtau<0.',
  'periods':'U=-2pi Psi_tau-i eps tau;V=2i tau;n=eps-2p;U+pV=-2piic.',
  'completion':'Invariant vector field on compact similarity torus rules out second fixed point in developing image. Log development gives complete flat torus. Fixed initial generator periods tend to0 as second fixed point goes toinfinity, fixing integer lifts without a small-global-log assumption. Primitive tube angle2pi c; at1 smooth original surgery; main cusp complete.',
  'volume':'G=2pi i(Psi-sum tauPsi_tau)+.5sum eps tau²;dG=.5sum VdU;Vol=ImG-.5sum ReU ImV=2pi Re C(c);completeanchor2E v8. Core lambda length=-2Imtau; Schlaefli sign/factor agree.',
  'cusp':'Compare actual representations nearzero on new positive triangulation via mixed main-meridian/aux-longitude marked gluing rigidity. Exact Legendre equations identify physical x_e; intrinsic main translation continues holomorphically along chart. Fixed surgery word is preferred at smooth endpoint.',
 },
 'publication':{
  'master':'notes/actual_all_circle_quantitative_volume.md',
  'proofs':['notes/actual_all_circle_curvature_filling_limit.md','notes/all_circle_uniform_newton_bounds.md','notes/actual_all_circle_octahedral_decomposition.md','notes/actual_all_circle_angular_octahedra.md','notes/actual_all_circle_geometric_completion.md','notes/actual_all_circle_preferred_cusp.md'],
  'manuscript':'130 pages, Chapter9 and full AppendicesE/F, exact A-period corollary; zero warnings. All130 source displays and510 inline formulas preserved in appendices.',
  'manuscript_pdf_sha256':revision['manuscript_pdf_sha256'],
  'guide':'README, guide/results/frontier/geometry/manuscript/audits/index, gallery, current-status notes and reproduction map updated. Sphinx redirects to the same guide.',
  'illustration':'book/figures/octahedral-page-attachment nativeTeX+SVG+PNG+PDF; manuscript shares nativefragment. Complete endpoint/face labels and gluing orientation explained.',
  'reproduction':'python3 repro/run_research_checks.py curvature-fillings',
  'checks':'3/3 programs;4 symbolic+990 numerical cases;46 rational+7bounds;128trees/448attachments/28algebra. Finite scope explicit, no general proof inferred from tests.',
  'validation':revision['validation'],
 },
 'remaining_general_problem':['Arbitrary short twists outside S criterion; other knot constructions, cyclic interaction graphs and growing diagrams.','The selected classical geometric A-factor and its exact marked regulator module remain open. Microscopic finite jets alone do not force that identification.'],
 'private_A_factor_report':'/private/tmp/md-main-meridian-marked-a-factor-interface-and-jet-obstruction.md: finite resultant criterion ord>P bidegree bound for supplied classical factor; root multipliers invisible at any fixed microscopic order. They change ordinary-color pointing, so are not counterexamples for actual knot state.',
 'next_steps':['Do not repeat completed caption/publication or reopen the proved circle-tree completion as an outstanding gap.','Build further structural extension or actual classical-A selection argument without confusing complete geometric source, actual signed invariant and selected recurrence period.','Keep all earlier methods and failed routes archived; preserve broad old strict-tree theorem. General goal remains active.'],
 'archive':str(archive),
}
for n in ['murakamis-current-research-handoff.json','murakamis-current-turn-status.json','md-curvature-current-handoff.json','md-quantitative-current-handoff.json']:
 p=tmp/n;preserve(p);p.write_text(json.dumps(state,indent=2)+'\n');preserve(p)
for p in tmp.glob('md-*quantitative*.*'):preserve(p)
print(json.dumps({'head':head,'goal_status':'active','live_matches':len(live['checks']),'manuscript_pages':130},indent=2))
