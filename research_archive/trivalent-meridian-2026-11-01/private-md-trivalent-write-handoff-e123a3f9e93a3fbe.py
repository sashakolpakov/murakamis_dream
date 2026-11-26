from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,subprocess
ws=Path('/Users/sasha/volume-conjecture');tmp=Path('/private/tmp');pub=tmp/'murakamis_dream-publication';arc=ws/'research_archive/trivalent-meridian-2026-11-01'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
record=json.loads((arc/'preservation-manifest.json').read_text())
def preserve(p,tag='private'):
 if not p.is_file():return
 h=sha(p);dest=arc/(tag+'-'+p.stem+'-'+h[:16]+p.suffix)
 if dest.exists():assert dest.read_bytes()==p.read_bytes()
 else:dest.write_bytes(p.read_bytes())
 record['files'].append({'source':str(p),'archive':str(dest.relative_to(ws)),'sha256':h})
for pattern in ['md-*trivalent*.md','md-*trivalent*.py','md-*trivalent*.json','md-*trivalent*.log']:
 for p in tmp.glob(pattern):preserve(p)
for name in ['md-one-high-admissible-hub-trace-exponential-obstruction.md','md-complete-admissible-hub-trace-exponential-obstruction.md','md-old-whole-hub-simultaneous-half-pressure.md','md-higher-hub-independent-cross-checks.md','md-published-high-index-dependency-audit.md']:
 preserve(tmp/name)
for p in (tmp/'md-trivalent-browser').glob('*.png'):preserve(p,'browser')
for p in (tmp/'md-trivalent-public-reproduction').glob('*'):preserve(p,'repro')
validation=json.loads((tmp/'md-trivalent-publication-validation.json').read_text())
live=json.loads((tmp/'md-trivalent-live-deployment.json').read_text())
assert all(c['equal'] for c in live['checks'])
head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=pub,text=True).strip()
assert live['commit']==head
assert not subprocess.check_output(['git','status','--porcelain'],cwd=pub,text=True)
now=datetime.now(timezone.utc).isoformat()
handoff={
 'updated_utc':now,'goal':'get the most general equality AND show that it is indeed the hyperbolic volume involved','goal_status':'active',
 'public_checkout':str(pub),'public_head':head,'pushed':True,'pages_run':live['pages_run'],'live_verified':len(live['checks']),
 'latest_user_caption':'Schematic hyperbolic pyramid; quadrilateral gluing face. Compiled PDF and live figure remain corrected and hash-verified.',
 'published_result':'The filled moving-meridian volume limit, exact scalar, normalized profile and preferred-cusp first correction now cover arbitrary fixed trivalent bare components on physical turn edges, in addition to singleton and path-qualified components.',
 'published_notes':validation['sources'],
 'scope_limits':['The complete-value theorem remains broader than this moving-meridian theorem.','A component with more than one bare junction and at least one junction of valence greater than three still requires the existing path criterion. Artificial unturned binary resolutions do not qualify.','The knot presentation and sufficiently long signed filling integers are fixed before N tends to infinity. The lower twist threshold is independent of their ratios and of R<1.','Ordinary-color resonances, a fixed M disk and a selected classical geometric A-factor remain open.'],
 'validation':validation['validation'],
 'next_critical_path':{
  'old_pressure_lemma':str(tmp/'md-old-whole-hub-simultaneous-half-pressure.md'),
  'old_pressure_status':'The simultaneous half-boundary comparison extends to arbitrary-valence old hubs with at most one marked incidence per hub. Full cross-reads passed; this alone does not control the moving additional trace terms.',
  'pointwise_obstruction':str(tmp/'md-one-high-admissible-hub-trace-exponential-obstruction.md'),
  'independent_proof':str(tmp/'md-complete-admissible-hub-trace-exponential-obstruction.md'),
  'obstruction':'For N=5a+1, phi_s(e_(4a)e_a^8)/phi_0 has exponentially growing absolute value at each fixed Delta_s nonzero, through both parities. The complete tuple is admissible with one high index, but lies on pair-equality boundary faces.',
  'scope':'This refutes an unweighted pointwise polynomial or subexponential whole-trace comparison. It does not refute the volume conjecture, the trivalent theorem, the all-low comparison or a strict-window comparison.',
  'remaining_work':'Compare the bad boundary configurations with the actual neighboring coefficient profiles and the coupled geometric pressure. Cluster and geometry are investigating. The saved dependency audit confirms that the published singleton/path/regular-window estimates use only the all-low comparison and separate full-norm bounds, not the refuted one-high comparison.'
 },
 'archive':str(arc),'release_whitelist':str(tmp/'md-trivalent-release-whitelist.json'),'live_record':str(tmp/'md-trivalent-live-deployment.json')}
for name in ['md-trivalent-current-handoff.json','murakamis-current-research-handoff.json','murakamis-current-turn-status.json']:
 p=tmp/name;preserve(p,'previous-handoff');p.write_text(json.dumps(handoff,indent=2,ensure_ascii=False)+'\n')
(arc/'current-handoff.json').write_text(json.dumps(handoff,indent=2,ensure_ascii=False)+'\n')
record['files']=list({(r['source'],r['sha256']):r for r in record['files']}.values());record['updated_utc']=now
(arc/'preservation-manifest.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'public_head':head,'live_artifacts':len(live['checks']),'preserved_versions':len(record['files'])}))
