from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,subprocess
pub=Path('/private/tmp/murakamis_dream-publication')
ws=Path('/Users/sasha/volume-conjecture')
tmp=Path('/private/tmp')
base='d8ff75be41f307c34867046445c530a6251ec5cf'
archive=ws/'research_archive/local-tree-volume-2026-11-01'
archive.mkdir(parents=True,exist_ok=True)
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def preserve(p):
 if not p.is_file(): return
 dest=archive/(p.stem+'-'+sha(p)[:16]+p.suffix)
 if not dest.exists(): shutil.copy2(p,dest)
changed=subprocess.check_output(['git','diff','--name-only'],cwd=pub,text=True).splitlines()
new=subprocess.check_output(['git','ls-files','--others','--exclude-standard'],cwd=pub,text=True).splitlines()
paths=sorted(set(changed+new)-{'PUBLICATION_MANIFEST.json','PUBLICATION_VALIDATION.json'})
sources=[x for x in paths if not x.startswith('docs/')]
book=json.loads((tmp/'md-local-message-book-check.json').read_text())
browser=json.loads((tmp/'md-local-message-browser/report.json').read_text())
paper=json.loads((pub/'manuscript/build/build-manifest.json').read_text())
assert not book['failures'] and not browser['failures'] and not paper['warnings']
assert sha(pub/'manuscript/build/main.pdf')==paper['pdf_sha256']==browser['pdf']['source_sha256']
repros={}
for script,result,key in [
 ('audit_all_circle_local_message_constants','all_circle_local_message_constants_results','script_sha256'),
 ('audit_all_circle_vertexwise_geometry','all_circle_vertexwise_geometry_results','script_sha256'),
 ('audit_all_circle_local_message_recursion','actual_local_tree_message_recursion_results','runner_sha256')]:
 s=pub/'experiments'/(script+'.py');r=pub/'experiments'/(result+'.json')
 d=json.loads(r.read_text());assert d[key]==sha(s),(script,'stale result')
 repros[script]={'script_sha256':sha(s),'results_sha256':sha(r)}
# Compare each workspace destination with the public base before copying.
conflicts=[]
for rel in sources:
 dest=ws/rel
 if not dest.is_file() or sha(dest)==sha(pub/rel): continue
 old=subprocess.run(['git','show',base+':'+rel],cwd=pub,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
 if old.returncode or hashlib.sha256(old.stdout).hexdigest()!=sha(dest):
  conflicts.append(rel)
if conflicts: raise RuntimeError({'workspace_files_changed_since_public_base':conflicts})
now=datetime.now(timezone.utc).isoformat()
revision={
 'updated_utc':now,
 'scope':'Any fixed literal ordered tree of integer two-string braids with a crossing circle at every vertex, at least one edge, original endpoint frames, and a one-component/no-internal-component knot test.',
 'local_quantum_criterion':'max_v d_v/(d_v^2+n_v^2)<=2^-120',
 'size_independent_corollary':'Every |n_v|>=2^119 suffices independently of tree size, degree and depth. Graph and powers remain fixed before N.',
 'conclusion':'The actual knot complement is hyperbolic; the reduced Kashaev logarithmic growth is its volume through both parities and composite levels. The uniform reduced ADO microscopic profile holds on |s|<=R<1, with exact scalar factors retained.',
 'geometry_only_criterion':'sqrt(d_v^2+n_v^2)>=630 at each vertex gives a positive primitive filling path and smooth actual hyperbolic completion. This weaker condition alone is not a quantum volume theorem.',
 'proof':'Exact full-index subtree polynomial, degree<=N-1 in each parent angle, nonzero normalized local expansion, conditional trace tails and primitive metric completion. All repeated-root normals and peripheral factors retained.',
 'prior_results_preserved':'Summed S<=2^-25 theorem, previous strict-tree long-net-twist and closure theorems remain separate sufficient results.',
 'classical_characteristic':'All-order source expansion on shifted nonreal charts determines a reciprocal irreducible characteristic factor of every specified genuine all-level annihilator. Explicit rational E,Q,M critical equations and L_eff are provided. The geometric cusp tangent is identified.',
 'still_open':'Identification of the full selected characteristic with the geometric eigenvalue germ; arbitrary short twists and arbitrary hyperbolic knots; graphs with cycles or growing diagrams. No global goal completion is claimed.',
 'manuscript':'149 pages; new Chapter10 and full AppendixG. All66 proof displays preserved. New native tree-boundary figure visually inspected.',
 'manuscript_pdf_sha256':paper['pdf_sha256'],
 'validation':{'book':book,'browser_page_checks':len(browser['checks']),'browser_failures':browser['failures'],'manuscript_warnings':paper['warnings'],'reproduction':repros,
 'finite_check_scope':'21 analytic and8 geometric strict rational comparisons;48 numerical finite recursion cases at80digits,180 roots. These supplement, not replace, written proofs.'},
 'pyramid_caption':'Schematic hyperbolic pyramid. All five vertices are ideal. Quadrilateral gluing face.',
 'pyramid_png_sha256':sha(pub/'docs/assets/figures/manuscript-leaf-pyramid.png'),
 'sources':sources
}
assert revision['pyramid_png_sha256']=='7e2ffa53ae95123be66e22bbc06144c5f0f3340bce27b72dd0ca393c02392e6a'
for rel in sources:
 p=pub/rel;dest=ws/rel;preserve(p);preserve(dest)
 dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,dest)
for name in ['PUBLICATION_MANIFEST.json','PUBLICATION_VALIDATION.json']:
 p=pub/name;preserve(p);d=json.loads(p.read_text());d['local_tree_volume_revision']=revision
 if name=='PUBLICATION_MANIFEST.json':
  rows={x['path']:x for x in d['files']}
  for rel in sources:
   rows.setdefault(rel,{'path':rel}).update(source_sha256=sha(pub/rel),published_sha256=sha(pub/rel))
  d['files']=[rows[k] for k in sorted(rows)]
  d['generated_public_files']=sorted(x.relative_to(pub).as_posix() for x in (pub/'docs').rglob('*') if x.is_file())
  d['last_refreshed_utc']=now
 else:d['last_refresh_utc']=now
 p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
 preserve(p);shutil.copy2(p,ws/name)
m=json.loads((pub/'PUBLICATION_MANIFEST.json').read_text())
bad=[x['path'] for x in m['files'] if sha(pub/x['path'])!=x['published_sha256']]
assert not bad,bad
for pat in ['md-local-message*','md-local-tree-message*','md-local-manuscript*','md-filtered-main-meridian*','md-main-meridian-all-order*','md-main-meridian-flat*','md-all-circle-rational-effective*','md-isolated-zero-power*','md-tree-boundary-message*','actual_main_meridian_filtered_characteristic.md']:
 for p in tmp.glob(pat):
  if p.is_file():preserve(p)
for folder in ['md-local-message-browser','md-local-message-repro','md-local-message-repro-with-deps']:
 for p in (tmp/folder).rglob('*'):preserve(p)
(tmp/'md-local-message-publication-validation.json').write_text(json.dumps(revision,indent=2)+'\n')
whitelist=paths+['PUBLICATION_MANIFEST.json','PUBLICATION_VALIDATION.json']
(tmp/'md-local-message-release-whitelist.json').write_text(json.dumps({p:sha(pub/p) for p in whitelist},indent=2)+'\n')
print(json.dumps({'sources_synced':len(sources),'release_files':len(whitelist),'manifest_files':len(m['files']),'failures':[]},indent=2))
