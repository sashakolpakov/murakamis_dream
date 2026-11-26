from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,subprocess
pub=Path('/private/tmp/murakamis_dream-publication');ws=Path('/Users/sasha/volume-conjecture');tmp=Path('/private/tmp')
base='d2e6c156f7af625eb09a3c9815869ad47b0872cc'
archive=ws/'research_archive/geometric-characteristic-2026-11-01';archive.mkdir(parents=True,exist_ok=True)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def preserve(p):
 if p.is_file():
  dest=archive/(p.stem+'-'+sha(p)[:16]+p.suffix)
  if not dest.exists():shutil.copy2(p,dest)
paths=sorted(set(subprocess.check_output(['git','diff','--name-only'],cwd=pub,text=True).splitlines()+subprocess.check_output(['git','ls-files','--others','--exclude-standard'],cwd=pub,text=True).splitlines())-{'PUBLICATION_MANIFEST.json','PUBLICATION_VALIDATION.json'})
sources=[x for x in paths if not x.startswith('docs/')]
book=json.loads((tmp/'md-geometric-book-check.json').read_text());browser=json.loads((tmp/'md-geometric-browser/report.json').read_text());paper=json.loads((pub/'manuscript/build/build-manifest.json').read_text());repro=json.loads((tmp/'md-geometric-characteristic-repro/summary.json').read_text());fidelity=json.loads((tmp/'md-geometric-appendix-fidelity.json').read_text())
assert not book['failures'] and not browser['failures'] and not paper['warnings']
assert not fidelity['missing_displays'] and not fidelity['control_bytes']
assert repro['status']=='passed' and repro['completed_checks']==4 and not repro['failed_checks']
assert sha(pub/'manuscript/build/main.pdf')==paper['pdf_sha256']==browser['pdf']['source_sha256']
conflicts=[]
for rel in sources:
 dest=ws/rel
 if not dest.is_file() or sha(dest)==sha(pub/rel):continue
 old=subprocess.run(['git','show',base+':'+rel],cwd=pub,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
 if old.returncode or hashlib.sha256(old.stdout).hexdigest()!=sha(dest):conflicts.append(rel)
if conflicts:raise RuntimeError({'workspace_changes_since_base':conflicts})
now=datetime.now(timezone.utc).isoformat()
revision={
 'updated_utc':now,
 'scope':'Fixed literal ordered trees with a crossing-circle tangle at every vertex, at least one edge, actual quarter-turn attachments, original endpoint frames and primitive slopes, one main knot and no internally closed extra component.',
 'geometric_conclusion':'The entire preferred geometric longitude germ is L=-M^a product_e (M^2-X_e)/(1-M^2 X_e), a=-w(D)-sum n_v, on the actual regular complete hyperbolic filled branch. Filling descent explicitly requires Q_v^2!=1.',
 'proof':'Explicit nonparabolic native and four-puncture character representations, ordered page and full Hurwitz gluing, boundary isotropy, geometric integrality and constants field, regular reconstruction at every nonzero M, original surgery framing and Seifert-surface longitude sign.',
 'quantum_hypotheses':'Actual all-order source classes: independently sufficiently long signed powers in covered strict all-circle presentations, or sum d/(d^2+n^2)<=2^-25, or max d/(d^2+n^2)<=2^-120. Graph and integers fixed before N.',
 'operator_conclusion':'The selected complex geometric irreducible factor divides the first nonzero classical symbol of every genuine fixed all-level reduced ADO annihilator. Rational coefficients give the contracted rational prime factor. Exact peripheral gauge retained before formal-domain cancellation.',
 'volume_scope':'All previously proved volume classes and numerical thresholds remain unchanged. This revision closes the geometric characteristic identification for covered circle trees; it does not add arbitrary short-twist cases.',
 'still_open':'Full A-polynomial or operator-ideal equality; multiplicities; geometric characteristic identification for arbitrary strict trees with bare junctions; ordinary-color resonance continuation; arbitrary short twists, general hyperbolic knots and growing diagrams. Global research objective remains active.',
 'manuscript':'New geometric longitude chapter, full filtered-characteristic Appendix H and full geometric/annihilator Appendix I, with native vector illustrations.',
 'manuscript_pdf_sha256':paper['pdf_sha256'],
 'validation':{'book':book,'browser_page_checks':len(browser['checks']),'browser_failures':browser['failures'],'manuscript_warnings':paper['warnings'],'reproduction_checks':4,'reproduction_failures':0,'appendix_source_displays':fidelity['source_displays'],'appendix_converted_displays':fidelity['appendix_displays']},
 'finite_check_scope':'Four symbolic programs check local matrices, character matching, full Hurwitz line transport and algebraic ratio identities. The written global proofs are separate.',
 'pyramid_caption':'Schematic hyperbolic pyramid. All five vertices are ideal. Quadrilateral gluing face.',
 'pyramid_png_sha256':sha(pub/'docs/assets/figures/manuscript-leaf-pyramid.png'),
 'sources':sources}
assert revision['pyramid_png_sha256']=='7e2ffa53ae95123be66e22bbc06144c5f0f3340bce27b72dd0ca393c02392e6a'
for rel in sources:
 p=pub/rel;dest=ws/rel;preserve(p);preserve(dest);dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,dest)
for name in ['PUBLICATION_MANIFEST.json','PUBLICATION_VALIDATION.json']:
 p=pub/name;preserve(p);d=json.loads(p.read_text());d['geometric_characteristic_revision']=revision
 if name=='PUBLICATION_MANIFEST.json':
  rows={x['path']:x for x in d['files']}
  for rel in sources:rows.setdefault(rel,{'path':rel}).update(source_sha256=sha(pub/rel),published_sha256=sha(pub/rel))
  d['files']=[rows[k] for k in sorted(rows)];d['generated_public_files']=sorted(x.relative_to(pub).as_posix() for x in (pub/'docs').rglob('*') if x.is_file());d['last_refreshed_utc']=now
 else:d['last_refresh_utc']=now
 p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n');preserve(p);shutil.copy2(p,ws/name)
m=json.loads((pub/'PUBLICATION_MANIFEST.json').read_text());bad=[x['path'] for x in m['files'] if sha(pub/x['path'])!=x['published_sha256']];assert not bad,bad
for pat in ['md-geometric*','md-all-circle*','md-all-main*','md-nonparabolic*','md-peripheral-ratio*','md-preferred-longitude*','md-global-all-circle*','md-decorated-hurwitz*','md-filtered-appendix*','md-local-message-current-handoff.json']:
 for p in tmp.glob(pat):
  if p.is_file():preserve(p)
for folder in ['md-geometric-browser','md-geometric-characteristic-repro']:
 for p in (tmp/folder).rglob('*'):preserve(p)
(tmp/'md-geometric-publication-validation.json').write_text(json.dumps(revision,indent=2)+'\n')
whitelist=paths+['PUBLICATION_MANIFEST.json','PUBLICATION_VALIDATION.json'];(tmp/'md-geometric-release-whitelist.json').write_text(json.dumps({p:sha(pub/p) for p in whitelist},indent=2)+'\n')
print(json.dumps({'sources_synced':len(sources),'release_files':len(whitelist),'manifest_files':len(m['files']),'failures':[]},indent=2))
