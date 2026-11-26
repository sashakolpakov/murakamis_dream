from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import shutil

pub=Path('/private/tmp/murakamis_dream-publication')
ws=Path('/Users/sasha/volume-conjecture')
tmp=Path('/private/tmp')
record=json.loads((tmp/'md-curvature-publication-paths.json').read_text())
archive=Path(record['archive'])
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def preserve(p):
    if not p.is_file(): return
    target=archive/(p.stem+'-'+sha(p)[:16]+p.suffix)
    if not target.exists(): shutil.copy2(p,target)

for pattern in ['md-*curvature*.*','md-*octahedron-angular*.*',
                'md-all-circle-*.*','md-short-filling-*.*',
                'md-main-meridian-marked-a-factor-*.*']:
    for p in tmp.glob(pattern): preserve(p)
for folder in ['md-curvature-browser','md-curvature-reproduction-final']:
    for p in (tmp/folder).rglob('*'): preserve(p)
hashes={}
for rel in record['source_paths']:
    path=pub/rel
    hashes[rel]=sha(path)
    dest=ws/rel
    dest.parent.mkdir(parents=True,exist_ok=True)
    shutil.copy2(path,dest)
    preserve(path)

book=json.loads((tmp/'md-curvature-book-check.json').read_text())
browser=json.loads((tmp/'md-curvature-browser/report.json').read_text())
checks=json.loads((pub/'experiments/all_circle_curvature_packet_results.json').read_text())
assert not book['failures'] and not browser['failures']
assert checks['script_sha256']==sha(pub/'experiments/audit_all_circle_curvature_packet.py')
now=datetime.now(timezone.utc).isoformat()
revision={
 'updated_utc':now,
 'scope':'A fixed strict Conway operation tree with an original crossing-circle operator at every junction, retaining its knot and parity qualifications. The graph and signed powers are fixed before N tends to infinity.',
 'hypothesis':'sum_v d_v/(d_v^2+n_v^2) <= 2^-25',
 'conclusion':'The actual reduced invariant has a nonzero first-charge asymptotic, a uniform microscopic profile for |s|<=R<1, and logarithmic limit 2*pi*Re C(1).',
 'geometric_limit':'Identifying this action with the original knot-complement volume outside the previously proved long-filling cases remains an unproved geometric completion step. This revision does not claim a new short-twist volume theorem.',
 'proof_inputs':['Uniform full-normal scalar source gap','Exact two-variable edge action','Uniform complex finite-sum expansion','Degree-weighted nonlinear contraction and charge comparison','Absolute tail and connector errors below the first charge'],
 'sources':record['source_paths'],
 'validation':{'book':book,'browser_checks':len(browser['checks']),'browser_failures':browser['failures'],'reproduction':checks},
 'pyramid_caption':'Schematic hyperbolic pyramid. All five vertices are ideal. Quadrilateral gluing face.',
 'pyramid_png_sha256':sha(pub/'docs/assets/figures/manuscript-leaf-pyramid.png'),
 'manuscript_pdf_sha256':sha(pub/'docs/papers/conway-composition.pdf'),
}
for name in ['PUBLICATION_MANIFEST.json','PUBLICATION_VALIDATION.json']:
    path=pub/name
    preserve(path)
    data=json.loads(path.read_text())
    data['curvature_filling_revision']=revision
    if name=='PUBLICATION_MANIFEST.json':
        rows={r['path']:r for r in data['files']}
        for rel,h in hashes.items():
            rows.setdefault(rel,{'path':rel}).update(source_sha256=h,published_sha256=h)
        data['files']=[rows[k] for k in sorted(rows)]
        data['generated_public_files']=sorted(p.relative_to(pub).as_posix() for p in (pub/'docs').rglob('*') if p.is_file())
        data['last_refreshed_utc']=now
    else:
        data['last_refresh_utc']=now
    path.write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n')
    preserve(path)
manifest=json.loads((pub/'PUBLICATION_MANIFEST.json').read_text())
for row in manifest['files']:
    assert sha(pub/row['path'])==row['published_sha256'],row['path']
for rel,h in hashes.items(): assert sha(ws/rel)==h
(tmp/'md-curvature-publication-validation.json').write_text(json.dumps(revision,indent=2)+'\n')
(tmp/'md-curvature-release-whitelist.json').write_text(json.dumps(hashes,indent=2)+'\n')
print(json.dumps({'sources':len(hashes),'manifest_entries':len(manifest['files']),
                  'archive':str(archive),'book_failures':book['failures'],'browser_failures':browser['failures']},indent=2))
