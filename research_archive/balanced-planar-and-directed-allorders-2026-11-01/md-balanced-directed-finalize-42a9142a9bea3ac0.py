from pathlib import Path
from datetime import datetime, timezone
import hashlib,json,shutil,subprocess
pub=Path('/private/tmp/murakamis_dream-publication')
ws=Path('/Users/sasha/volume-conjecture')
tmp=Path('/private/tmp')
base='ec4ca87d2472aa5f3bc18a30be93170946771f99'
archive=ws/'research_archive/balanced-planar-and-directed-allorders-2026-11-01'
archive.mkdir(parents=True,exist_ok=True)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def preserve(p):
 if p.is_file():
  dest=archive/(p.stem+'-'+sha(p)[:16]+p.suffix)
  if not dest.exists():shutil.copy2(p,dest)
assert subprocess.check_output(['git','rev-parse','HEAD'],cwd=pub,text=True).strip()==base
paths=sorted(set(subprocess.check_output(['git','diff','HEAD','--name-only'],cwd=pub,text=True).splitlines()+subprocess.check_output(['git','ls-files','--others','--exclude-standard'],cwd=pub,text=True).splitlines())-{'PUBLICATION_MANIFEST.json','PUBLICATION_VALIDATION.json'})
sources=[p for p in paths if not p.startswith('docs/')]
book=json.loads((tmp/'md-balanced-directed-book-check.json').read_text())
browser=json.loads((tmp/'md-balanced-directed-browser/report.json').read_text())
followup=json.loads((tmp/'md-balanced-directed-browser-final/report.json').read_text())
paper=json.loads((pub/'manuscript/build/build-manifest.json').read_text())
repro=json.loads((tmp/'md-balanced-fans-repro-final/summary.json').read_text())
exact=json.loads((pub/'experiments/actual_balanced_terminal_fans_results.json').read_text())
fidelity_l=json.loads((tmp/'md-balanced-fans-appendix-fidelity-final.json').read_text())
fidelity_m=json.loads((tmp/'md-directed-allorders-appendix-fidelity.json').read_text())
assert not book['failures'] and not browser['failures'] and not followup['failures']
assert not paper['warnings']
assert fidelity_l['ordered_displays_identical'] and fidelity_l['ordered_inline_identical'] and not fidelity_l['control_bytes']
assert fidelity_m['displays_preserved'] and fidelity_m['inline_preserved'] and not fidelity_m['controls']
assert sha(pub/'notes/actual_balanced_terminal_fan_volume.md')==fidelity_l['source_sha256']
assert sha(pub/'manuscript/sections/L-balanced-terminal-fans.tex')==fidelity_l['target_sha256']
assert sha(pub/'manuscript/sections/M-directed-all-orders.tex')==fidelity_m['appendix_sha256']
assert repro['status']=='passed' and repro['completed_checks']==1 and not repro['failed_checks']
assert exact['check_count']==134
assert sha(pub/'manuscript/build/main.pdf')==paper['pdf_sha256']==followup['pdf']['source_sha256']==sha(pub/'docs/papers/conway-composition.pdf')
for rel,digest in paper['inputs'].items():assert sha(pub/rel)==digest,rel
for rel,digest in paper['figures'].items():assert sha(pub/rel)==digest,rel
previous_path=tmp/'md-balanced-directed-release-whitelist.json'
previous=json.loads(previous_path.read_text()) if previous_path.exists() else {}
conflicts=[]
for rel in sources:
 dest=ws/rel
 if not dest.is_file() or sha(dest)==sha(pub/rel) or sha(dest)==previous.get(rel):continue
 old=subprocess.run(['git','show',base+':'+rel],cwd=pub,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
 if old.returncode or hashlib.sha256(old.stdout).hexdigest()!=sha(dest):conflicts.append(rel)
if conflicts:raise RuntimeError({'workspace_changes_since_base':conflicts})
now=datetime.now(timezone.utc).isoformat()
revision={
 'updated_utc':now,
 'base_commit':base,
 'volume_scope':'A fixed connected augmented diagram whose white cellulation is a simple triangulated sphere with at least four vertices, its original crossing-disk matching and frames, a marked nonmatching strand edge, and a parity pattern with one main knot. Alternatively any such oriented simple sphere with a chosen perfect matching of its cubic dual supplies a literal diagram in S3 and a knot parity.',
 'geometric_construction':'The positive circle packing and ideal right-angled polyhedron are constructed by a finite Hall/entropy optimization and an injective Euclidean development. A separate supplied metric certificate is not a hypothesis.',
 'new_volume_theorem':'A finite even terminal fan on each side of each original crossing circle makes the complete-radius balance inequality strict at every original and added circle in one shared packing. All original and added filling integers, independently sufficiently long and fixed before N, give the volume equality for the actual reduced Kashaev invariant through all integer levels. The right side is the actual hyperbolic knot-complement volume.',
 'normalization_and_geometry':'The full original finite Morse source retains oriented four-leg frames, cups and caps, normal terms, signed powers, parity, endpoint currents and all nonzero Fourier charges. The primitive filling equations complete the auxiliary cusps by smooth solid tori of angle 2pi while the main cusp stays complete.',
 'decoration_limitation':'The even decorations preserve endpoint pairing and the knot condition but generally change the knot. The threshold and the number of additions depend on the fixed diagram. This is not a theorem for arbitrary short original fillings, an undecorated core, a nonsimple white sphere, or a diagram changing with N.',
 'directed_all_orders_extension':'For every fixed ordered circle-tree directed certificate, the reduced meridian profile has the full polynomially filtered expansion on the disk |s|<1 and every fixed compact in the open upper half-plane, with the exact H_N scalar retained. The leading cusp correction and selected geometric longitude hold throughout this class.',
 'operator_consequence':'Every genuine fixed all-level reduced annihilator has the selected geometric irreducible factor in its first nonzero classical symbol, after the exact reduced/full-state gauge and preferred peripheral normalization. Over rational coefficients use the contracted rational prime.',
 'scope_boundary':'No full A-polynomial equality, operator-ideal equality, multiplicity claim, uniform resonance passage, fixed-M off-complete asymptotic, or moving-meridian extension to the new planar decorated class is asserted. The general conjecture and active research objective remain open.',
 'manuscript':'294-page illustrated manuscript with new Chapters 13 and 14 and complete Appendices L and M. Existing mathematical formulas are retained; scope and exposition are updated.',
 'pdf_sha256':paper['pdf_sha256'],
 'validation':{
   'book':book,'browser_page_checks':browser['page_checks']+followup['page_checks'],
   'browser_failures':[],'manuscript_warnings':paper['warnings'],
   'finite_reproduction_groups':1,'finite_exact_checks':134,
   'finite_check_scope':'Symbolic recurrence identities, rational inequalities, oriented local patch incidences, endpoint pairings and finite even-count examples. These checks do not replace the analytic proof or assert a general theorem from samples.',
   'appendix_L_displays':104,'appendix_L_inline_formulas':457,
   'appendix_M_displays':36,'appendix_M_inline_formulas':204,
   'formula_fidelity':'All display and inline mathematical formulas are preserved in order from the final source notes.',
   'last_prose_correction':'Hall inequalities are strict for every nonempty proper destination subset; the empty cut is equality.'
 },
 'pyramid_caption':'Ideal hyperbolic pyramid. The text names the shaded ideal triangles and quadrilateral gluing face and gives the ideal boundary coordinates.',
 'pyramid_png_sha256':sha(pub/'docs/assets/figures/manuscript-leaf-pyramid.png'),
 'sources':sources
}
for rel in sources:
 p=pub/rel;dest=ws/rel;preserve(p);preserve(dest);dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,dest)
for name in ['PUBLICATION_MANIFEST.json','PUBLICATION_VALIDATION.json']:
 p=pub/name;preserve(p);d=json.loads(p.read_text());d['balanced_planar_and_directed_allorders_revision']=revision
 if name=='PUBLICATION_MANIFEST.json':
  rows={x['path']:x for x in d['files']}
  for rel in sources:rows.setdefault(rel,{'path':rel}).update(source_sha256=sha(pub/rel),published_sha256=sha(pub/rel))
  d['files']=[rows[k] for k in sorted(rows)]
  d['generated_public_files']=sorted(x.relative_to(pub).as_posix() for x in (pub/'docs').rglob('*') if x.is_file())
  d['last_refreshed_utc']=now
 else:d['last_refresh_utc']=now
 p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n');preserve(p);shutil.copy2(p,ws/name)
m=json.loads((pub/'PUBLICATION_MANIFEST.json').read_text())
bad=[x['path'] for x in m['files'] if sha(pub/x['path'])!=x['published_sha256']]
assert not bad,bad
for pat in ['md-balanced*','md-directed-allorders*','md-cyclic*','md-convert-balanced*','actual_all_circle_directed_all_orders.md','08f-directed-all-orders.tex','M-directed-all-orders.tex','audit_actual_balanced_terminal_fans.py','actual_balanced_terminal_fans_results.json','balanced-terminal-fans.*']:
 for p in tmp.glob(pat):
  if p.is_file():preserve(p)
for folder in ['md-balanced-directed-browser','md-balanced-directed-browser-followup','md-balanced-directed-browser-final','md-balanced-fans-repro-final','md-balanced-directed-pdf-render']:
 for p in (tmp/folder).rglob('*'):preserve(p)
for rel in ['manuscript/build/build-manifest.json','manuscript/build/build-console.txt']:
 p=pub/rel;preserve(p);(ws/rel).parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,ws/rel)
(tmp/'md-balanced-directed-publication-validation.json').write_text(json.dumps(revision,indent=2)+'\n')
whitelist=paths+['PUBLICATION_MANIFEST.json','PUBLICATION_VALIDATION.json']
(tmp/'md-balanced-directed-release-whitelist.json').write_text(json.dumps({p:sha(pub/p) for p in whitelist},indent=2)+'\n')
print(json.dumps({'sources_synced':len(sources),'release_files':len(whitelist),'manifest_files':len(m['files']),'pdf_sha256':paper['pdf_sha256'],'failures':[]},indent=2))
