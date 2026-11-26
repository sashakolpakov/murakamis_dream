from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,subprocess
pub=Path('/private/tmp/murakamis_dream-publication');ws=Path('/Users/sasha/volume-conjecture');tmp=Path('/private/tmp')
archive=ws/'research_archive/preferred-cusp-2026-11-01';archive.mkdir(parents=True,exist_ok=True)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
records=[]
def preserve(p,kind):
 if not p.is_file(): return
 data=p.read_bytes();h=hashlib.sha256(data).hexdigest();dest=archive/(kind+'-'+p.stem+'-'+h[:16]+p.suffix)
 if dest.exists(): assert dest.read_bytes()==data
 else: dest.write_bytes(data)
 records.append({'source':str(p),'archive':str(dest.relative_to(ws)),'sha256':h})
paths=json.loads((tmp/'md-cusp-publication-paths.json').read_text())
for rel in paths:
 preserve(ws/rel,'before');preserve(pub/rel,'published')
 (ws/rel).parent.mkdir(parents=True,exist_ok=True);(ws/rel).write_bytes((pub/rel).read_bytes())
private_names=['md-general-conway-preferred-main-longitude-translation.md','md-general-conway-longitude-audit.py','md-general-conway-longitude-audit-results.json','md-filled-main-meridian-exact-global-scalar-ledger.md','md-filled-main-meridian-exact-global-scalar-ledger-inputs.json','md-general-main-longitude-independent-ledger-review.md','md-publish-main-meridian-scalar.md','md-publish-main-meridian-preferred-cusp.md','md-main-meridian-preferred-cusp-publication-manifest.json','md-bare-component-full-label-gram-and-clamping.md','md-trivalent-bare-component-simultaneous-clamp.md','md-return-prism-signed-face-obstruction.md','md-cusp-update-public.py','md-cusp-install-public.py','md-cusp-browser-check.py','md-cusp-book-check.json','md-cusp-build.log']
for name in private_names:preserve(tmp/name,'private')
preserve(tmp/'md-cusp-browser/report.json','browser');preserve(tmp/'md-cusp-public-reproduction/summary.json','repro')
book=json.loads((tmp/'md-cusp-book-check.json').read_text());browser=json.loads((tmp/'md-cusp-browser/report.json').read_text());assert not book['failures'] and not browser['failures']
repro=json.loads((tmp/'md-cusp-public-reproduction/summary.json').read_text());assert len(repro['results'])==2 and all(r['returncode']==0 for r in repro['results'])
scalar=json.loads((pub/'experiments/main_meridian_exact_scalar_results.json').read_text());geom=json.loads((pub/'experiments/main_meridian_preferred_cusp_results.json').read_text())
now=datetime.now(timezone.utc).isoformat();hashes={rel:sha(pub/rel) for rel in paths}
revision={'updated_utc':now,'base_commit':'b6fe800900946d4c4e101d1459ebb280017f72dc','scope':'Exact main-meridian scalar and preferred-cusp identity for marked Conway constructions; geometric first correction for the existing long-twist moving-meridian class.','proved':['The prescribed crossing, turn and zero-framing scalars combine exactly to q_N^((-w(D)-sum_i n_i)s^2/2).','Original meridian-normalized face maps and the homology of disk fillings give the preferred cusp shape tau=-w(D)-sum_i n_i+2i sum_e cot(pi x_e^fill).','For the existing moving-meridian class, the first correction after the exact sine quotient is pi i s^2 tau/(2N), uniformly on |s|<=R<1.','The normalized reduced profile tends to sin(pi s)/(pi s); the normalized full modified-trace profile tends to one.'],'limits':'The geometric identity has broader strict-tree scope than the moving asymptotic. This release does not enlarge that asymptotic class, cross ordinary-color resonances, or identify a classical geometric A-factor.','sources':['notes/actual_main_meridian_exact_scalar.md','notes/actual_main_meridian_preferred_cusp.md','notes/actual_main_meridian_filled_volume.md'],'reproduction_commands':['python3 repro/run_research_checks.py meridian-cusp'],'validation':{'book':book,'browser':{'page_viewport_checks':len(browser['checks']),'failures':browser['failures']},'scalar_counts':scalar['counts'],'geometric_exact_identities':geom['count'],'reproduction_records_match':True,'new_source_private_paths':0},'manuscript_pdf_sha256':sha(pub/'manuscript/build/main.pdf'),'pyramid_caption':'Schematic hyperbolic pyramid; quadrilateral gluing face.','pyramid_png_sha256':sha(pub/'docs/assets/figures/manuscript-leaf-pyramid.png')}
assert revision['manuscript_pdf_sha256']=='18ccc920523a9df9cb305d01270b9983e9019b418692c0872c780f8101f82c27'
assert revision['pyramid_png_sha256']=='7e2ffa53ae95123be66e22bbc06144c5f0f3340bce27b72dd0ca393c02392e6a'
for name in ['PUBLICATION_MANIFEST.json','PUBLICATION_VALIDATION.json']:
 p=pub/name;preserve(p,'before-metadata');d=json.loads(p.read_text());d['preferred_cusp_revision']=revision
 if name=='PUBLICATION_MANIFEST.json':
  rows={r['path']:r for r in d['files']}
  for rel,h in hashes.items():rows.setdefault(rel,{'path':rel}).update(source_sha256=h,published_sha256=h)
  d['files']=[rows[k] for k in sorted(rows)];d['generated_public_files']=sorted(p.relative_to(pub).as_posix() for p in (pub/'docs').rglob('*') if p.is_file());d['last_refreshed_utc']=now
 else:d['last_refresh_utc']=now
 p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n');preserve(p,'published-metadata')
manifest=json.loads((pub/'PUBLICATION_MANIFEST.json').read_text())
for row in manifest['files']:assert sha(pub/row['path'])==row['published_sha256'],row['path']
for rel,h in hashes.items():assert sha(ws/rel)==h,rel
(tmp/'md-cusp-release-whitelist.json').write_text(json.dumps(hashes,indent=2)+'\n')
(tmp/'md-cusp-publication-validation.json').write_text(json.dumps(revision,indent=2,ensure_ascii=False)+'\n')
(archive/'preservation-manifest.json').write_text(json.dumps({'updated_utc':now,'files':records,'published_paths':paths},indent=2)+'\n')
print(json.dumps({'source_files':len(paths),'manifest_entries_verified':len(manifest['files']),'preserved_versions':len(records),'archive':str(archive)},indent=2))
