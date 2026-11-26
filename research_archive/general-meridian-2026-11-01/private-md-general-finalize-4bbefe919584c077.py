from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,subprocess
pub=Path('/private/tmp/murakamis_dream-publication');ws=Path('/Users/sasha/volume-conjecture');tmp=Path('/private/tmp')
archive=ws/'research_archive/general-meridian-2026-11-01';archive.mkdir(parents=True,exist_ok=True)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
recordfile=archive/'preservation-manifest.json'
records=json.loads(recordfile.read_text())['files'] if recordfile.exists() else []
def preserve(p,kind):
 if not p.is_file(): return
 data=p.read_bytes();h=hashlib.sha256(data).hexdigest();dest=archive/(kind+'-'+p.stem+'-'+h[:16]+p.suffix)
 if dest.exists(): assert dest.read_bytes()==data
 else: dest.write_bytes(data)
 records.append({'source':str(p),'archive':str(dest.relative_to(ws)),'sha256':h})
paths=json.loads((tmp/'md-general-publication-paths.json').read_text())
for rel in paths:
 preserve(ws/rel,'before');preserve(pub/rel,'published')
 (ws/rel).parent.mkdir(parents=True,exist_ok=True);(ws/rel).write_bytes((pub/rel).read_bytes())
private_patterns=['md-*general*.md','md-*general*.py','md-*general*.json','md-*general*.log','md-one-high*','md-old-*pressure*','md-old-bare*','md-multiple-high*','md-arbitrary-bare*','md-valence-nine*','md-joint-reflection*','md-higher-hub*','md-published-high-index*','md-main-meridian-*','actual_main_meridian_*','audit_main_meridian_high_fourier_reflection.py','high_fourier_reflection_results.json']
for pattern in private_patterns:
 for p in tmp.glob(pattern):preserve(p,'private')
for folder in ['md-general-browser','md-general-public-reproduction','md-general-guide-validation']:
 for p in (tmp/folder).rglob('*'):preserve(p,folder)
book=json.loads((tmp/'md-general-book-check.json').read_text());browser=json.loads((tmp/'md-general-browser/report.json').read_text())
assert not book['failures'] and not browser['failures']
repro=json.loads((tmp/'md-general-public-reproduction/summary.json').read_text());assert len(repro['results'])==1 and all(r['returncode']==0 for r in repro['results'])
audit=json.loads((pub/'experiments/high_fourier_reflection_results.json').read_text())
assert audit['script_sha256']==sha(pub/'experiments/audit_main_meridian_high_fourier_reflection.py')
now=datetime.now(timezone.utc).isoformat();hashes={rel:sha(pub/rel) for rel in paths}
revision={
 'updated_utc':now,'base_commit':'8dadde29f2a02207a1031b12f4b5031e12b43db5',
 'scope':'Moving-meridian volume and preferred-cusp asymptotics for every fixed strict ordered Conway tree with independently sufficiently long fixed signed twists.',
 'proved':[
  'Exact cancellation of the first Fourier alias bounds a one-high trace difference by the complete tensor with its index reflected, with a strict regular-window loss.',
  'Full Frobenius fusion and sequential turn deletion compare positive pressures while retaining the ordered branches and their correlations.',
  'Simultaneous half-boundary comparison and the half-cardinal identity control several-high correction sectors for arbitrary junction valences.',
  'The general component estimate supplies the original complex packet and joint filling hypotheses without a component valence, size or path restriction.',
  'The resulting uniform volume limit is the original filled knot-complement volume; exact framing and the preferred-cusp correction retain all original physical edges.',
  'The zero-framed Laurent family and intrinsic asymptotics transfer through the existing marked net-twist and arbitrary-closure ambient isotopies.'
 ],
 'limits':'The presentation, parity and sufficiently long signed net twists are fixed before the quantum level tends to infinity. The theorem retains strictness and knot qualifications. It does not cover arbitrary short net twists, continuation through ordinary-color resonances, a fixed meridian disk, or identification of a selected classical geometric A-factor. Deleted turns appear only in upper estimates and do not replace the original knot complement.',
 'sources':['notes/actual_main_meridian_high_fourier_reflection.md','notes/actual_main_meridian_component_pressure.md','notes/actual_main_meridian_general_component_comparison.md','notes/actual_main_meridian_filled_volume.md'],
 'reproduction_commands':['python3 repro/run_research_checks.py general-components'],
 'validation':{'book':book,'browser':{'page_viewport_checks':len(browser['checks']),'failures':browser['failures']},'exact_reproduction':audit['counts'],'reproduction_scope':audit['scope'],'reproduction_records_match':(pub/'experiments/high_fourier_reflection_results.json').read_bytes()==(tmp/'high_fourier_reflection_results.json').read_bytes(),'new_source_private_paths':0},
 'manuscript_pdf_sha256':sha(pub/'manuscript/build/main.pdf'),
 'pyramid_caption':'Schematic hyperbolic pyramid; quadrilateral gluing face.',
 'pyramid_png_sha256':sha(pub/'docs/assets/figures/manuscript-leaf-pyramid.png')
}
assert revision['validation']['reproduction_records_match']
assert revision['manuscript_pdf_sha256']=='18ccc920523a9df9cb305d01270b9983e9019b418692c0872c780f8101f82c27'
assert revision['pyramid_png_sha256']=='7e2ffa53ae95123be66e22bbc06144c5f0f3340bce27b72dd0ca393c02392e6a'
for name in ['PUBLICATION_MANIFEST.json','PUBLICATION_VALIDATION.json']:
 p=pub/name;preserve(p,'before-metadata');d=json.loads(p.read_text());d['general_meridian_revision']=revision
 if name=='PUBLICATION_MANIFEST.json':
  rows={r['path']:r for r in d['files']}
  for rel,h in hashes.items():rows.setdefault(rel,{'path':rel}).update(source_sha256=h,published_sha256=h)
  d['files']=[rows[k] for k in sorted(rows)];d['generated_public_files']=sorted(p.relative_to(pub).as_posix() for p in (pub/'docs').rglob('*') if p.is_file());d['last_refreshed_utc']=now
 else:d['last_refresh_utc']=now
 p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n');preserve(p,'published-metadata')
manifest=json.loads((pub/'PUBLICATION_MANIFEST.json').read_text())
for row in manifest['files']:assert sha(pub/row['path'])==row['published_sha256'],row['path']
for rel,h in hashes.items():assert sha(ws/rel)==h,rel
(tmp/'md-general-release-whitelist.json').write_text(json.dumps(hashes,indent=2)+'\n')
(tmp/'md-general-publication-validation.json').write_text(json.dumps(revision,indent=2,ensure_ascii=False)+'\n')
records=list({(r['source'],r['sha256']):r for r in records}.values())
recordfile.write_text(json.dumps({'updated_utc':now,'files':records,'published_paths':paths},indent=2)+'\n')
print(json.dumps({'source_files':len(paths),'manifest_entries_verified':len(manifest['files']),'preserved_versions':len(records),'archive':str(archive)},indent=2))
