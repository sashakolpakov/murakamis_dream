from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,subprocess
pub=Path('/private/tmp/murakamis_dream-publication');ws=Path('/Users/sasha/volume-conjecture');tmp=Path('/private/tmp')
archive=ws/'research_archive/trivalent-meridian-2026-11-01';archive.mkdir(parents=True,exist_ok=True)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
records=json.loads((archive/'preservation-manifest.json').read_text())['files'] if (archive/'preservation-manifest.json').exists() else []
def preserve(p,kind):
 if not p.is_file(): return
 data=p.read_bytes();h=hashlib.sha256(data).hexdigest();dest=archive/(kind+'-'+p.stem+'-'+h[:16]+p.suffix)
 if dest.exists(): assert dest.read_bytes()==data
 else: dest.write_bytes(data)
 records.append({'source':str(p),'archive':str(dest.relative_to(ws)),'sha256':h})
paths=json.loads((tmp/'md-trivalent-publication-paths.json').read_text())
for rel in paths:
 preserve(ws/rel,'before');preserve(pub/rel,'published')
 (ws/rel).parent.mkdir(parents=True,exist_ok=True);(ws/rel).write_bytes((pub/rel).read_bytes())
private_names=[p.name for pattern in ['md-*trivalent*.md','md-*trivalent*.py','md-*trivalent*.json','md-*trivalent*.log'] for p in tmp.glob(pattern)]
private_names += ['md-one-high-admissible-hub-trace-exponential-obstruction.md','md-complete-admissible-hub-trace-exponential-obstruction.md','md-old-whole-hub-simultaneous-half-pressure.md']
for name in private_names:preserve(tmp/name,'private')
preserve(tmp/'md-trivalent-browser/report.json','browser');preserve(tmp/'md-trivalent-public-reproduction/summary.json','repro')
book=json.loads((tmp/'md-trivalent-book-check.json').read_text());browser=json.loads((tmp/'md-trivalent-browser/report.json').read_text());assert not book['failures'] and not browser['failures']
repro=json.loads((tmp/'md-trivalent-public-reproduction/summary.json').read_text());assert len(repro['results'])==1 and all(r['returncode']==0 for r in repro['results'])
audit=json.loads((pub/'experiments/trivalent_return_comparison_results.json').read_text())
assert audit['script_sha256']==sha(pub/'experiments/audit_main_meridian_trivalent_components.py')
now=datetime.now(timezone.utc).isoformat();hashes={rel:sha(pub/rel) for rel in paths}
revision={
 'updated_utc':now,
 'base_commit':'f8ad1bf26869de41987719075f53dabef5517ec0',
 'scope':'Moving-meridian volume theorem extended to arbitrary fixed trivalent bare components connected by the original physical turns.',
 'proved':[
  'Joint concavity and the boundary response at the simultaneous half boundary give the old-component pressure comparison.',
  'The exact cubic quotient trace, its disjoint old and additional supports, and a coupled replacement prove a strict gap for every additional pattern in a fixed trivalent component.',
  'The enlarged component class retains the full source bounds, auxiliary-color gap, complex wire packet and joint filling argument.',
  'The resulting uniform volume limit is the filled knot-complement volume, with the exact framing scalar and preferred-cusp first correction.'
 ],
 'limits':'The graph and independently sufficiently long signed twists are fixed before the quantum level tends to infinity. Higher-valence components still require the separate existing component condition. Artificial binary resolutions do not qualify as physical trivalent components. Ordinary-color resonances and a selected classical A-factor are not settled here.',
 'sources':['notes/actual_main_meridian_trivalent_component_bound.md','notes/actual_main_meridian_trivalent_filled_volume.md'],
 'reproduction_commands':['python3 repro/run_research_checks.py trivalent-components'],
 'validation':{'book':book,'browser':{'page_viewport_checks':len(browser['checks']),'failures':browser['failures']},'exact_reproduction':'714 symmetric triples representing 3024 ordered triples at levels 2 through 10; 384 moving metrics; 136 return endpoint checks; six actual currying types and ten compatible products.','reproduction_scope':'Finite algebraic identities and supports; the analytic pressure and asymptotic arguments are supplied by the proofs.','reproduction_records_match':(pub/'experiments/trivalent_return_comparison_results.json').read_bytes()==(tmp/'md-trivalent-return-comparison-results.json').read_bytes(),'new_source_private_paths':0},
 'manuscript_pdf_sha256':sha(pub/'manuscript/build/main.pdf'),
 'pyramid_caption':'Schematic hyperbolic pyramid; quadrilateral gluing face.',
 'pyramid_png_sha256':sha(pub/'docs/assets/figures/manuscript-leaf-pyramid.png')
}
assert revision['validation']['reproduction_records_match']
assert revision['manuscript_pdf_sha256']=='18ccc920523a9df9cb305d01270b9983e9019b418692c0872c780f8101f82c27'
assert revision['pyramid_png_sha256']=='7e2ffa53ae95123be66e22bbc06144c5f0f3340bce27b72dd0ca393c02392e6a'
for name in ['PUBLICATION_MANIFEST.json','PUBLICATION_VALIDATION.json']:
 p=pub/name;preserve(p,'before-metadata');d=json.loads(p.read_text());d['trivalent_meridian_revision']=revision
 if name=='PUBLICATION_MANIFEST.json':
  rows={r['path']:r for r in d['files']}
  for rel,h in hashes.items():rows.setdefault(rel,{'path':rel}).update(source_sha256=h,published_sha256=h)
  d['files']=[rows[k] for k in sorted(rows)];d['generated_public_files']=sorted(p.relative_to(pub).as_posix() for p in (pub/'docs').rglob('*') if p.is_file());d['last_refreshed_utc']=now
 else:d['last_refresh_utc']=now
 p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n');preserve(p,'published-metadata')
manifest=json.loads((pub/'PUBLICATION_MANIFEST.json').read_text())
for row in manifest['files']:assert sha(pub/row['path'])==row['published_sha256'],row['path']
for rel,h in hashes.items():assert sha(ws/rel)==h,rel
(tmp/'md-trivalent-release-whitelist.json').write_text(json.dumps(hashes,indent=2)+'\n')
(tmp/'md-trivalent-publication-validation.json').write_text(json.dumps(revision,indent=2,ensure_ascii=False)+'\n')
(archive/'preservation-manifest.json').write_text(json.dumps({'updated_utc':now,'files':records,'published_paths':paths},indent=2)+'\n')
print(json.dumps({'source_files':len(paths),'manifest_entries_verified':len(manifest['files']),'preserved_versions':len(records),'archive':str(archive)},indent=2))
