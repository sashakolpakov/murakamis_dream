from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,subprocess
ws=Path('/Users/sasha/volume-conjecture');tmp=Path('/private/tmp');pub=tmp/'murakamis_dream-publication';arc=ws/'research_archive/preferred-cusp-2026-11-01'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
records=json.loads((arc/'preservation-manifest.json').read_text())
def preserve(p,tag='private'):
 if not p.is_file():return
 h=sha(p);dest=arc/(tag+'-'+p.stem+'-'+h[:16]+p.suffix)
 if dest.exists():assert dest.read_bytes()==p.read_bytes()
 else:dest.write_bytes(p.read_bytes())
 entry={'source':str(p),'archive':str(dest.relative_to(ws)),'sha256':h}
 if entry not in records['files']:records['files'].append(entry)
for pattern in ['md-*trivalent*.md','md-*trivalent*.py','md-*trivalent*.json','md-cusp-*.*']:
 for p in tmp.glob(pattern):preserve(p)
for p in (tmp/'md-cusp-browser').glob('*.png'):preserve(p,'browser')
for name in ['md-bare-component-full-label-gram-and-clamping.md','md-general-main-longitude-independent-ledger-review.md']:preserve(tmp/name)
validation=json.loads((tmp/'md-cusp-publication-validation.json').read_text());live=json.loads((tmp/'md-cusp-live-deployment.json').read_text());assert all(c['equal'] for c in live['checks'])
head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=pub,text=True).strip();assert head=='f8ad1bf26869de41987719075f53dabef5517ec0';assert not subprocess.check_output(['git','status','--porcelain'],cwd=pub,text=True)
now=datetime.now(timezone.utc).isoformat()
handoff={
 'updated_utc':now,'goal':'get the most general equality AND show that it is indeed the hyperbolic volume involved','goal_status':'active','public_checkout':str(pub),'public_head':head,'pushed':True,'pages_run':41265629403,'live_verified':len(live['checks']),
 'latest_user_caption':'Schematic hyperbolic pyramid; quadrilateral gluing face. The compiled PDF and live figure remain corrected and hash-verified.',
 'published_result':'Exact scalar A_N(s)=q_N^((-w-sum n)s^2/2), independent preferred-cusp identity tau=-w-sum n+2i sum cot(pi x_e^fill), and first correction pi i s^2 tau/(2N) in the existing filled moving-meridian class.',
 'published_notes':['notes/actual_main_meridian_exact_scalar.md','notes/actual_main_meridian_preferred_cusp.md','notes/actual_main_meridian_filled_volume.md'],
 'scope_limits':['The complete-value volume theorem remains broader than the moving-meridian theorem.','The geometric preferred-cusp identity covers every stated strict marked tree; this release does not enlarge the moving analytic class.','Ordinary-color resonance continuation and the selected classical geometric A-factor remain open.','Twist numbers and the finite presentation are fixed before N tends to infinity.'],
 'validation':validation['validation'],
 'next_critical_path':{
  'private_component_proof':str(tmp/'md-trivalent-bare-component-simultaneous-clamp.md'),
  'sha256':sha(tmp/'md-trivalent-bare-component-simultaneous-clamp.md'),
  'result':'Simultaneous high-boundary clamping yields an absolute return gap for arbitrary-size trivalent bare components on physical quarter-turn edges. Full internal labels are retained.',
  'root_read':'Root read the full initial proof and checked the two subsequent precisions; geometry and coherent supplied independent full reads.',
  'precisions':['Use i/(N-1) for finite closed entropy comparison; using i/N makes return complements exceed one at total 2N-1. Uniform rate error is O(log N).','Ordinary terminal profiles enter directly as L; completed products are proper A, and only those internal outputs are turned.','A low return arm receives one new g(x) profile in its adjacent old region, then reassembles as old(.5,.5,x); the contribution is counted once.'],
  'remaining_work':'Cluster is drafting a separate global extension through source induction, auxiliary-color gap, full strict wire window, small complex tubes and joint filling contours. Geometry and coherent should review it before promotion.',
  'limits':'Higher-valence hubs resolved with unturned complementary-label edges are not covered. The current published moving theorem has not yet been enlarged.'
 },
 'archive':str(arc),'release_whitelist':str(tmp/'md-cusp-release-whitelist.json'),'live_record':str(tmp/'md-cusp-live-deployment.json')}
for name in ['md-cusp-current-handoff.json','murakamis-current-research-handoff.json','murakamis-current-turn-status.json']:
 p=tmp/name;preserve(p,'previous-handoff');p.write_text(json.dumps(handoff,indent=2,ensure_ascii=False)+'\n')
(arc/'current-handoff.json').write_text(json.dumps(handoff,indent=2,ensure_ascii=False)+'\n');records['updated_utc']=now;(arc/'preservation-manifest.json').write_text(json.dumps(records,indent=2)+'\n')
print(json.dumps({'public_head':head,'live_artifacts':len(live['checks']),'preserved_versions':len(records['files']),'private_component_sha256':handoff['next_critical_path']['sha256']}))
