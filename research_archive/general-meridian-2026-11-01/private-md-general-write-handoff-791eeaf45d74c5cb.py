from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,subprocess
ws=Path('/Users/sasha/volume-conjecture');tmp=Path('/private/tmp');pub=tmp/'murakamis_dream-publication';arc=ws/'research_archive/general-meridian-2026-11-01'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
record=json.loads((arc/'preservation-manifest.json').read_text())
def preserve(p,tag='private'):
 if not p.is_file():return
 h=sha(p);dest=arc/(tag+'-'+p.stem+'-'+h[:16]+p.suffix)
 if dest.exists():assert dest.read_bytes()==p.read_bytes()
 else:dest.write_bytes(p.read_bytes())
 record['files'].append({'source':str(p),'archive':str(dest.relative_to(ws)),'sha256':h})
for pattern in ['md-*general*','md-*component*','md-*pressure*','md-one-high*','md-complete-admissible*','actual_main_meridian_same_index*']:
 for p in tmp.glob(pattern):preserve(p)
validation=json.loads((tmp/'md-general-publication-validation.json').read_text())
live=json.loads((tmp/'md-general-live-deployment.json').read_text())
assert all(c['equal'] for c in live['checks'])
head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=pub,text=True).strip()
assert live['commit']==head
assert not subprocess.check_output(['git','status','--porcelain'],cwd=pub,text=True)
now=datetime.now(timezone.utc).isoformat()
handoff={
 'updated_utc':now,'goal':'get the most general equality AND show that it is indeed the hyperbolic volume involved','goal_status':'active',
 'current_turn':'progress: arbitrary bare-component moving-meridian theorem published and live verified',
 'public_checkout':str(pub),'public_head':head,'pushed':True,'pages_run':live['pages_run'],'live_verified':len(live['checks']),
 'latest_user_caption':'Schematic hyperbolic pyramid; quadrilateral gluing face. Compiled PDF and live figure remain corrected and hash-verified.',
 'published_result':'The moving-meridian volume limit, exact scalar, nonzero normalized profile and preferred-cusp correction now cover every fixed strict ordered Conway tree with independently sufficiently long fixed signed twists. No remaining bare-component adjacency, valence, size or path restriction. The marked ambient-isotopy reductions transfer the intrinsic conclusions to their stated net-twist and closure classes.',
 'published_notes':validation['sources']+['notes/actual_main_meridian_same_index_obstruction.md'],
 'proof':validation['proved'],
 'scope_limits':['The presentation and sufficiently long signed filling integers are fixed before N tends to infinity; the threshold is independent of their ratios and the later R<1.','Strictness, orientation, knot and two-leaf qualifications remain. Arbitrary short surviving net twists and general hyperbolic knots are not proved.','Ordinary-color resonances, a fixed meridian disk, and the selected classical geometric A-factor remain open.','The comparison deletes turns only in upper estimates. All original physical edges, peripheral markings, normalization and original knot-complement volume stay in the retained packet.'],
 'validation':validation['validation'],
 'preserved_obstruction':{'public_note':'notes/actual_main_meridian_same_index_obstruction.md','meaning':'A fixed-valence-nine, one-high, complete-admissible tuple has an exponentially large moving/complete ratio. This refutes same-index pointwise comparison, not the volume conjecture. The general theorem instead bounds the trace difference by a reflected complete tensor and controls the full coupled pressure.'},
 'next_critical_path':['Do not reimpose removed trivalent/path restrictions. The general component argument and its original packet/filling dependency reads are complete.','Any broader knot theorem must address short surviving net twists or a topological representation beyond the stated fixed strict/net-twist classes.','For the A-polynomial objective, the exact pointed quantum period and moving family are available, but selecting the classical geometric factor remains separate.','A generic profile through ordinary-color resonances needs a further estimate for the subtracted state. The figure-eight result remains broader in this parameter direction.'],
 'archive':str(arc),'release_whitelist':str(tmp/'md-general-release-whitelist.json'),'live_record':str(tmp/'md-general-live-deployment.json')}
for name in ['md-general-current-handoff.json','md-general-meridian-current-handoff.json','murakamis-current-research-handoff.json','murakamis-current-turn-status.json']:
 p=tmp/name;preserve(p,'previous-handoff');p.write_text(json.dumps(handoff,indent=2,ensure_ascii=False)+'\n')
(arc/'current-handoff.json').write_text(json.dumps(handoff,indent=2,ensure_ascii=False)+'\n')
record['files']=list({(r['source'],r['sha256']):r for r in record['files']}.values());record['updated_utc']=now
(arc/'preservation-manifest.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'public_head':head,'live_artifacts':len(live['checks']),'preserved_versions':len(record['files'])}))
