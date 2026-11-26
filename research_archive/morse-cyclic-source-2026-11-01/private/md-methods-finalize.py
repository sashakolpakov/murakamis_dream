from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,subprocess,shutil
tmp=Path('/private/tmp');pub=tmp/'murakamis_dream-publication'
archive=Path('/Users/sasha/volume-conjecture/research_archive/morse-cyclic-source-2026-11-01')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=pub,text=True).strip()
assert not subprocess.check_output(['git','status','--porcelain'],cwd=pub,text=True).strip()
assert subprocess.check_output(['git','rev-parse','origin/main'],cwd=pub,text=True).strip()==head
live=json.loads((tmp/'md-methods-live-check.json').read_text())
assert live['status']=='success' and live['commit']==head
for name in ['murakamis-current-research-handoff.json','murakamis-current-turn-status.json']:
 p=tmp/name
 if p.exists():
  dst=archive/'previous-handoffs'/f'{p.stem}-{sha(p)[:16]}.json';dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,dst)
data={
 'updated_utc':datetime.now(timezone.utc).isoformat(),
 'goal':'get the most general equality AND show that it is indeed the hyperbolic volume involved',
 'goal_status':'active; not complete or blocked',
 'latest_user_request':'Manuscript completed proofs only, including limited results; detailed illustrated guide covering all approaches with notation and literature; retire duplicate Sphinx exposition; correct TeX rendering.',
 'documentation_task':'Complete and published. Main guide, notation, manuscript scope, sources and rendered artifacts updated; no separate Sphinx build, eight legacy redirects retained.',
 'public_checkout':str(pub),'workspace':'/Users/sasha/volume-conjecture',
 'public_head':head,'public_clean':True,'pushed':True,
 'previous_head':'09cd63c5c5c1b1c8ce8805a7536e0f33e56a9d19',
 'paper_pages':322,'paper_pdf_sha256':sha(pub/'docs/papers/conway-composition.pdf'),
 'deployment':live,
 'published':{
  'methods':'book/chapters/methods.md',
  'notation':'book/chapters/notation.md',
  'scope':'manuscript/sections/01-introduction.tex',
  'geometric_sector':['notes/actual_morse_cross_filling_period.md','notes/actual_morse_geometric_contribution.md','manuscript/sections/O-morse-geometric-contribution.tex'],
  'scope_of_new_theorem':'The all-CROSS contribution of the literal matched simple-sphere Morse source has a nonzero whole-period asymptotic for independently long fixed signed fillings, both level parities. Original primitive peripheral words, regulator anchor and smooth metric completion identify its rate with the actual filled knot-complement volume. It is a selected contribution, not a new invariant or full-invariant theorem.'
 },
 'editorial_changes':'Removed unsuccessful odd face-map detour from manuscript I while retaining B_o and the working physical calibration; replaced stale proposed-comparison text in H by completed proof dependencies. Failed ideas remain in original technical notes. Added precise scope table, primary literature context, definitions, geometric-sign normalization, method diagram and clearer homogeneous face figure. Corrected eight pre-existing manuscript web links.',
 'validation':{
  'manuscript':'322 pages; no unresolved references/citations or overfull boxes; six underfull spacing messages. 67 new display formulas and 284 inline formulas retained. Scope/context PDF pages visually checked.',
  'guide':'1065 HTML pages; 28915 local links; 1045 indexed notes; no checker failures. Guide raw-TeX scan clear. 14 desktop/mobile page checks plus four final method/notation checks, all clean. Sphinx redirects tested.',
  'reports':['md-morse-publication-handoff.json','md-methods-manuscript-web-links.json','md-methods-guide-raw-tex-check.json','md-methods-browser-validation/report.json','md-methods-browser-final/report.json'],
  'figure_pdf_cleanup':'Seven unchanged figure PDFs were pixel/text/link-identical to baseline. Regenerated copies preserved; original bytes restored. Manifest hashes correct.'
 },
 'research_archive':str(archive),
 'private_results':{
  'endpoint':'md-cyclic-signed-plus-two-coefficient-bound.md: local coefficients <=2N^3 at +2, <=2N^4 on [2cos(pi/N),2]. Shared D_N <=2^(r+1)N^(6r) at all+2, <=2^(r+1)N^(7r) on shrinking cube. This does not bound the fixed full spectral cube.',
  'pair_current':'md-cyclic-signed-protected-pair-current.md: actual exterior loads, four interior bands and both endpoints. Sewn current does NOT vanish: exact N3,m6 example value -2051892 retained and independently reproduced.',
  'face_operator':'md-root-face-operator-factorization-and-shifted-pairing.md: D preserves root quotient; C=c0-D(Z+x)(Z+y)D; bilinear coefficient pairing/self-adjointness; q-Leibniz shifts spectators. D,Z generate full matrix algebra despite separate nilpotence. No positive norm/gap conclusion. 6688 exact checks N2..12.',
  'diagnostics':'md-undecorated-cancellation-bipyramid-diagnostic-report.md: signed original targets and constraints, N3..32 selected diagnostics, high precision replays and exact low levels. No asymptotic inference.',
  'support':'Protected-position odd one-exception identity holds, but arbitrary-position version fails. N3,m6 position3 D=2*9^5*(sigma-1)*(sigma+2), derivative at -2=-354294. Exact two-monomial proof retained.'
 },
 'critical_path':[
  'General-Morse all-CROSS applicability and actual-volume identification are now published; do not re-open as an unperformed task.',
  'For unchanged simple-sphere diagrams outside existing comparison criteria, prove a strict bound for D_N=full-CROSS on the entire shared fixed spectral cube, or an equally strong bound after original filling functionals. Preserve signs, face targets and repeated-root derivatives.',
  'The finite filling norm transfers a strict augmented gap to independently long fixed fillings; a bound only at augmented volume without a strict gap does not imply the smaller filled rate.',
  'Full volume theorem remains proved only in the previously covered Conway/tree/decorated planar classes. No additional full-invariant family claimed this turn.',
  'Next research should combine actual cyclic transfer/grade blocks and shifted face identities to control the signed remainder. Endpoint-only polynomial bounds and the nonzero sewn current are constraints, not the missing theorem.'
 ]
}
for name in ['murakamis-current-research-handoff.json','murakamis-current-turn-status.json','md-methods-current-handoff.json']:
 (tmp/name).write_text(json.dumps(data,indent=2)+'\n')
(archive/'current-handoff.json').write_text(json.dumps(data,indent=2)+'\n')
manifest={str(p.relative_to(archive)):{'bytes':p.stat().st_size,'sha256':sha(p)} for p in archive.rglob('*') if p.is_file() and p.name!='manifest.json'}
(archive/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps({'head':head,'paper_sha256':data['paper_pdf_sha256'],'archive':str(archive),'goal_status':'active'},indent=2))
