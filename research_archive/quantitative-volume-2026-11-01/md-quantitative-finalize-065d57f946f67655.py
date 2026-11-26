from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,subprocess
pub=Path('/private/tmp/murakamis_dream-publication')
ws=Path('/Users/sasha/volume-conjecture')
tmp=Path('/private/tmp')
archive=ws/'research_archive/quantitative-volume-2026-11-01'
archive.mkdir(parents=True,exist_ok=True)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def preserve(p):
 if not p.is_file():return
 dest=archive/(p.stem+'-'+sha(p)[:16]+p.suffix)
 if not dest.exists():shutil.copy2(p,dest)
changed=subprocess.check_output(['git','diff','--name-only'],cwd=pub,text=True).splitlines()
new=subprocess.check_output(['git','ls-files','--others','--exclude-standard'],cwd=pub,text=True).splitlines()
paths=sorted(set(changed+new)-{'PUBLICATION_MANIFEST.json','PUBLICATION_VALIDATION.json'})
sources=[p for p in paths if not p.startswith('docs/')]
book=json.loads((tmp/'md-quantitative-book-check.json').read_text())
browser=json.loads((tmp/'md-quantitative-browser/report.json').read_text())
manuscript=json.loads((pub/'manuscript/build/build-manifest.json').read_text())
assert not book['failures'] and not browser['failures']
assert not manuscript['warnings']
assert sha(pub/'manuscript/build/main.pdf')==manuscript['pdf_sha256']
assert browser['pdf']['source_sha256']==manuscript['pdf_sha256']
repros={}
for name,script in [('all_circle_curvature_packet','audit_all_circle_curvature_packet'),
 ('two_octahedron_angular_edge_block','audit_two_octahedron_angular_edge_block'),
 ('ordered_octahedron_pages','audit_ordered_octahedron_pages')]:
 d=json.loads((pub/'experiments'/(name+'_results.json')).read_text())
 assert d['script_sha256']==sha(pub/'experiments'/(script+'.py'))
 repros[name]={'script_sha256':d['script_sha256'],'results_sha256':sha(pub/'experiments'/(name+'_results.json'))}
now=datetime.now(timezone.utc).isoformat()
revision={
 'updated_utc':now,
 'scope':'Every fixed literal ordered tree of two-string tangle compositions with a crossing circle at each vertex, at least one edge, original frames and the actual one-component knot test.',
 'criterion':'S=sum_v d_v/(d_v^2+n_v^2)<=2^-25',
 'conclusion':'The original knot complement is hyperbolic and the actual reduced Kashaev invariant has its volume limit through all integer levels. The same fixed diagram has a nonzero uniform microscopic ADO meridian profile on |s|<=R<1 and the preferred-cusp first correction.',
 'operator_corollary':'The exact pointed quantum A-period reconstructs the same Kashaev invariant and therefore has the same volume limit, with finite initial data and singular-step derivatives retained. No classical geometric-factor identity is assumed.',
 'geometric_identification':'The literal ordered projection cut gives two octahedra per edge. Positive tetrahedra and the full primitive logarithmic periods complete the original auxiliary surgeries at cone angle2*pi. The regulator and complete volume anchor identify the first-charge action with this knot-complement volume.',
 'explicit_corollaries':['Every |n_v|>=8192*sqrt(E) suffices for E edges.','Attach B terminal circles per vertex to an m-vertex tree, with new powers of magnitude>=B. Then B>=2^26*m suffices subject to the actual knot/parity test. The additions change the knot.','Literal R^0 insertion preserves the filled diagram but changes the augmented exterior and contributes1/d to S.'],
 'limits':'No optimality or priority claim. The construction and powers remain fixed before N. Arbitrary short twists, graphs with cycles, all hyperbolic knots and the selected classical geometric A-factor remain outside this result. Previous broader strict-tree long-net-twist and closure theorems are preserved.',
 'sources':sources,
 'validation':{
  'book':book,'browser_page_checks':len(browser['checks']),'browser_failures':browser['failures'],
  'manuscript_warnings':manuscript['warnings'],'reproduction':repros,
  'finite_check_scope':'4 exact edge identities and990 finite complex samples;46 local rational identities and7 bounds;128 tree cases with448 attachments and28 algebra identities. These supplement the written uniform, topological and geometric proofs.',
 },
 'pyramid_caption':'Schematic hyperbolic pyramid. All five vertices are ideal. Quadrilateral gluing face.',
 'pyramid_png_sha256':sha(pub/'docs/assets/figures/manuscript-leaf-pyramid.png'),
 'manuscript_pdf_sha256':manuscript['pdf_sha256'],
}
assert revision['pyramid_png_sha256']=='7e2ffa53ae95123be66e22bbc06144c5f0f3340bce27b72dd0ca393c02392e6a'
for rel in sources:
 p=pub/rel;preserve(p)
 dest=ws/rel
 if dest.is_file():preserve(dest)
 dest.parent.mkdir(exist_ok=True,parents=True);shutil.copy2(p,dest)
for name in ['PUBLICATION_MANIFEST.json','PUBLICATION_VALIDATION.json']:
 p=pub/name;preserve(p);d=json.loads(p.read_text())
 d['quantitative_volume_revision']=revision
 d['curvature_filling_revision']['historical_status']='Analytic-only stage, superseded for the stated circle-tree criterion by quantitative_volume_revision.'
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
mismatches=[x['path'] for x in m['files'] if sha(pub/x['path'])!=x['published_sha256']]
assert not mismatches,mismatches
for pat in ['md-*quantitative*.*','md-all-circle-*.*','md-*octahedron*.*','md-*angular*.*','md-ordered-*.*','md-curvature-repro-*.*']:
 for p in tmp.glob(pat):preserve(p)
for folder in ['md-quantitative-browser','md-all-circle-volume-publication','md-quantitative-appendices']:
 for p in (tmp/folder).rglob('*'):preserve(p)
(tmp/'md-quantitative-publication-validation.json').write_text(json.dumps(revision,indent=2)+'\n')
whitelist=paths+['PUBLICATION_MANIFEST.json','PUBLICATION_VALIDATION.json']
(tmp/'md-quantitative-release-whitelist.json').write_text(json.dumps({p:sha(pub/p) for p in whitelist},indent=2)+'\n')
print(json.dumps({'sources_synced':len(sources),'release_files':len(whitelist),'manifest_files':len(m['files']),'failures':[]},indent=2))
