from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,subprocess
pub=Path('/private/tmp/murakamis_dream-publication')
ws=Path('/Users/sasha/volume-conjecture')
tmp=Path('/private/tmp')
base='3d0f2a8ebe4e8f71340582b18097fa4f298005b1'
archive=ws/'research_archive/directed-and-strict-geometry-2026-11-01'
archive.mkdir(parents=True,exist_ok=True)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def preserve(p):
 if p.is_file():
  dest=archive/(p.stem+'-'+sha(p)[:16]+p.suffix)
  if not dest.exists():shutil.copy2(p,dest)
paths=sorted(set(subprocess.check_output(['git','diff','HEAD','--name-only'],cwd=pub,text=True).splitlines()+subprocess.check_output(['git','ls-files','--others','--exclude-standard'],cwd=pub,text=True).splitlines())-{'PUBLICATION_MANIFEST.json','PUBLICATION_VALIDATION.json'})
sources=[p for p in paths if not p.startswith('docs/')]
book=json.loads((tmp/'md-directed-strict-book-check.json').read_text())
browser=json.loads((tmp/'md-directed-strict-browser/report.json').read_text())
followup=json.loads((tmp/'md-directed-strict-browser-followup/report.json').read_text())
paper=json.loads((pub/'manuscript/build/build-manifest.json').read_text())
repro=json.loads((tmp/'md-directed-strict-repro-final/summary.json').read_text())
fidelity_j=json.loads((tmp/'md-strict-geometric-appendix-fidelity.json').read_text())
fidelity_k=json.loads((tmp/'md-directed-appendix-fidelity.json').read_text())
assert not book['failures'] and not browser['failures'] and not followup['failures']
assert not paper['warnings']
assert fidelity_j['ordered_displays_identical'] and not fidelity_j['control_bytes']
assert fidelity_k['display_math_identical_in_order'] and fidelity_k['inline_math_preserved_in_order'] and not fidelity_k['control_bytes']
assert sha(pub/'manuscript/sections/J-strict-tree-geometric-characteristic.tex')==fidelity_j['appendix_sha256']
assert sha(pub/'manuscript/sections/K-directed-circle-messages.tex')==fidelity_k['appendix_sha256']
assert repro['status']=='passed' and repro['completed_checks']==2 and not repro['failed_checks']
assert sha(pub/'manuscript/build/main.pdf')==paper['pdf_sha256']==followup['pdf']['source_sha256']
assert sha(pub/'experiments/audit_actual_all_circle_directed_volume.py')==json.loads((pub/'experiments/actual_all_circle_directed_volume_results.json').read_text())['sources']['experiments/audit_actual_all_circle_directed_volume.py']
previous_path=tmp/'md-directed-strict-release-whitelist.json'
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
 'volume_scope':'Fixed literal ordered circle trees with at least one physical quarter-turn edge, original strand frames and disk slopes, one main knot and no internally closed extra component. All integers and the whole finite diagram are fixed before the level tends to infinity.',
 'new_volume_theorem':'Directed finite criterion with a separately chosen outgoing decay constant at every nonroot vertex and no outgoing condition at the final evaluation root. The actual invariant has nonzero leading contribution and the stated microscopic profile; its rate is the actual hyperbolic knot-complement volume.',
 'simple_sufficient_condition':'At every vertex independently: |n_v|>=2^27 OR d_v>=2^28. In particular |n_v|>=2^27 at every vertex works independently of tree size.',
 'core_extension':'At every vertex of any fixed knot-paired ordered circle-tree core, insert an even B>=2^28 stack of terminal tangles in one specified product slot; each new power is odd with magnitude>=2^27+1. This preserves the endpoint pairing, generally changes the knot, and yields the actual hyperbolic volume equality.',
 'geometric_factor_extension':'Zero-power-circle insertion, exact stationary elimination with its additive constant, full based boundary-map comparison and regular folded reconstruction extend the preferred geometric longitude from circle trees to all covered strict Conway presentations. Marked net-twist and closure isotopies transfer the intrinsic result.',
 'operator_hypotheses':'All-orders sources already proved: strict independently long fillings, summed circle-tree bound sum d/(d^2+n^2)<=2^-25, or old-local bound max d/(d^2+n^2)<=2^-120. Every genuine fixed all-level reduced ADO annihilator has the selected geometric irreducible factor in its first nonzero classical symbol; rational coefficients use the contracted rational prime.',
 'scope_boundary':'Additional directed cases have volume equality and first-order profile here; their all-orders shifted-chart theorem is not asserted. No full A-polynomial equality, operator-ideal equality, multiplicity statement, arbitrary short-twist theorem, resonance continuation, or growing-diagram limit. Research objective remains active.',
 'manuscript':'243-page illustrated manuscript; new directed chapter and full Appendices J and K; existing source/math preserved, current scope paragraphs updated.',
 'pdf_sha256':paper['pdf_sha256'],
 'validation':{'book':book,'browser_page_checks':browser['page_checks']+followup['page_checks'],'browser_failures':[],'manuscript_warnings':paper['warnings'],'reproduction_groups':2,'rational_directed_inequalities':25,'endpoint_pairing_identities':8,'local_zero_circle_identities':26,'appendix_J_displays':46,'appendix_K_displays':69,'appendix_K_inline_formulas':176},
 'pyramid_caption':'Schematic hyperbolic pyramid. All five vertices are ideal. Quadrilateral gluing face.',
 'pyramid_png_sha256':sha(pub/'docs/assets/figures/manuscript-leaf-pyramid.png'),
 'sources':sources}
assert revision['pyramid_png_sha256']=='7e2ffa53ae95123be66e22bbc06144c5f0f3340bce27b72dd0ca393c02392e6a'
for rel in sources:
 p=pub/rel;dest=ws/rel;preserve(p);preserve(dest);dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,dest)
for name in ['PUBLICATION_MANIFEST.json','PUBLICATION_VALIDATION.json']:
 p=pub/name;preserve(p);d=json.loads(p.read_text());d['directed_and_strict_geometry_revision']=revision
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
for pat in ['md-directed*','md-strict*','md-variable-local-volume*','md-bare*','md-vertex-scaled*']:
 for p in tmp.glob(pat):
  if p.is_file():preserve(p)
for folder in ['md-directed-strict-browser','md-directed-strict-browser-followup','md-directed-strict-repro-final','md-directed-strict-guide-final-20261101']:
 for p in (tmp/folder).rglob('*'):preserve(p)
(tmp/'md-directed-strict-publication-validation.json').write_text(json.dumps(revision,indent=2)+'\n')
whitelist=paths+['PUBLICATION_MANIFEST.json','PUBLICATION_VALIDATION.json']
(tmp/'md-directed-strict-release-whitelist.json').write_text(json.dumps({p:sha(pub/p) for p in whitelist},indent=2)+'\n')
print(json.dumps({'sources_synced':len(sources),'release_files':len(whitelist),'manifest_files':len(m['files']),'failures':[]},indent=2))
