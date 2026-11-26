from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,subprocess

tmp=Path('/private/tmp')
ws=Path('/Users/sasha/volume-conjecture')
pub=tmp/'murakamis_dream-publication'
archive=ws/'research_archive/curvature-filling-2026-11-01'
archive.mkdir(parents=True,exist_ok=True)
def preserve(path):
 if path.is_file():
  digest=hashlib.sha256(path.read_bytes()).hexdigest()
  dest=archive/(path.stem+'-'+digest[:16]+path.suffix)
  if not dest.exists():shutil.copy2(path,dest)
  return {'source':str(path),'archive':str(dest),'sha256':digest}
rows=[]
for pattern in ['md-*curvature*.*','md-*octahedron-angular*.*','md-all-circle-*.*',
                'md-short-filling-*.*','md-main-meridian-marked-a-factor-*.*']:
 for path in tmp.glob(pattern):
  item=preserve(path)
  if item:rows.append(item)
for name in ['murakamis-current-research-handoff.json','murakamis-current-turn-status.json']:
 preserve(tmp/name)
head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=pub,text=True).strip()
live=json.loads((tmp/'md-curvature-live-deployment.json').read_text())
assert live['commit']==head and all(row['equal'] for row in live['checks'])
current={
 'updated_utc':datetime.now(timezone.utc).isoformat(),
 'goal':'get the most general equality AND show that it is indeed the hyperbolic volume involved',
 'goal_status':'active',
 'current_turn':'progress: explicit quantitative analytic extension published; local geometric blocks proved privately; global ordered assembly being audited',
 'public_checkout':str(pub),'public_head':head,'pushed':True,
 'pages_run':live['pages_run'],'live_verified':len(live['checks']),
 'latest_user_caption':'Schematic hyperbolic pyramid. All five vertices are ideal. Quadrilateral gluing face. Correct source, compiled figure and manuscript remain live hash-verified.',
 'previous_volume_theorem':'Every fixed strict ordered Conway tree, arbitrary bare-component size/valence/adjacency, with independently sufficiently long fixed signed twists. Uniform shrinking-meridian profile, exact scalar and preferred-cusp correction. Intrinsic conclusions transfer through proved marked net-twist and closure isotopies. Do not reimpose removed component restrictions.',
 'new_published_analytic_theorem':{
  'class':'Fixed strict ordered all-circle trees: every junction carries an original crossing circle; retain the knot/parity conditions.',
  'criterion':'S=sum_v d_v/(d_v^2+n_v^2)<=2^-25',
  'conclusion':'Nonzero first joint charge; actual reduced F_N(q^s)/F_N(1)=A_N(s)H_N(s)(1+O(N^-1)); log-rate2*pi*Re C(1), uniformly |s|<=R<1, both parities.',
  'scope':'This permits fixed short or zero powers at high-degree circles; graph and powers stay fixed before N. No new short-twist complement-volume conclusion is published.',
  'notes':['notes/actual_all_circle_curvature_filling_limit.md','notes/all_circle_uniform_newton_bounds.md'],
  'reproduction':'python3 repro/run_research_checks.py curvature-fillings',
  'checks':'4 exact symbolic identities,990 complex Gaussian samples at70 digits, both parities160..256; finite checks only.',
  'guide':'book/chapters/frontier.md explicitly distinguishes the proved analytic limit from unresolved volume identification.',
 },
 'validation':json.loads((tmp/'md-curvature-publication-validation.json').read_text())['validation'],
 'private_geometry':{
  'local_chart':'/private/tmp/md-two-octahedron-angular-edge-block.md',
  'local_audit':'/private/tmp/md-two-octahedron-angular-edge-block-independent-audit.md',
  'local_reproduction':'/private/tmp/md-audit-two-octahedron-angular-edge-block.py',
  'local_scope':'Actual two-leaf cut, C composed with T apex placement, two octahedra, eight positive tetrahedra on |tau|,|upsilon|<=.01; six complex pants seam ratios, local logarithmic increment. Independently audited; global topology remains separate.',
  'first_charge_size':'|tau_v|<=2*pi*sqrt(S)/(1-1/50)<.00111, so the analytic path c*1 for0<=c<=1 fits the local positive chart.',
  'global_work':'cluster_source_transport is writing literal bowtie ribbon insertion / ordered tree decomposition and primitive-path concatenation; coherent_partner_currents is assigned its independent audit. conway_reduced_geometry is writing completion and Schlaefli along charge path, conditional on that topology.',
  'required_primitive_logs':'U_v=-2*pi*sum_edges psi_tau-i*epsilon_v*tau_v;V_v=2i*tau_v;U_v+p_vV_v=-2*pi*i*c,n_v=epsilon_v-2p_v. Every retained half twist stays at its original distinguished seam.',
  'completion_route':'Positive nonsingular similarity tori for c>0; Re V>0. At small c fixed-tree old near-complete proof fixes actual log periods; integer differences remain constant through positive chart. At c1 primitive period-2*pi*i gives smooth tube. Core length=-2Im tau; Schlaefli derivative2*pi*sum Im tau equals derivative2*pi*Re C(c); anchor actual augmentedVol2*pi*F0.',
  'obstruction_report':'/private/tmp/md-short-filling-geometric-certificate-and-real-chamber-obstruction.md: small angular coordinates alone do not mean small primitive meridian logs; original real pyramid chamber has no smooth primitive filling.',
 },
 'private_A_factor':{
  'report':'/private/tmp/md-main-meridian-marked-a-factor-interface-and-jet-obstruction.md',
  'content':'Marked classical elimination from existing source charts; finite geometric-factor test ord P0(M,Lgeom(M))>ad+bc using resultant; exact both-parity root multipliers invisible to any prescribed finite microscopic order but with different classical curve.',
  'limit':'Multipliers change ordinary-color pointing. Actual scalar framing endpoint/carry comparison and relative formal functional remain missing. Do not promote microscopic profile to classical A-factor.',
 },
 'next_steps':[
  'Do not repeat publication or caption work; current checkout is clean and deployed.',
  'Finish and independently audit literal global ordered edge-block topology, actual seam orientation and primitive word. Local chart/volume factorization alone is not a topology proof.',
  'If topology and charge-path completion verify, integrate Schlaefli with original volume anchor to upgrade S criterion to actual short-twist knot-volume theorem; then update manuscript, illustrated guide and public status with real geometric pictures.',
  'Preserve all drafts, failures and scope boundaries. General hyperbolic knots and selected classical A-factor remain unresolved; keep goal active.'
 ],
 'archive':str(archive),
}
for name in ['murakamis-current-research-handoff.json','murakamis-current-turn-status.json','md-curvature-current-handoff.json']:
 (tmp/name).write_text(json.dumps(current,indent=2)+'\n')
 preserve(tmp/name)
(archive/'preservation-manifest.json').write_text(json.dumps({'files':rows,'updated_utc':current['updated_utc']},indent=2)+'\n')
print(json.dumps({'head':head,'goal_status':'active','preserved_files':len(rows),'live_matches':len(live['checks'])},indent=2))
