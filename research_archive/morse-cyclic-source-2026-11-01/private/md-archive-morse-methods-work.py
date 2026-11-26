from pathlib import Path
import hashlib,json,shutil,subprocess

tmp=Path('/private/tmp')
pub=tmp/'murakamis_dream-publication'
work=Path('/Users/sasha/volume-conjecture')
archive=work/'research_archive/morse-cyclic-source-2026-11-01'
archive.mkdir(parents=True,exist_ok=True)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()

def retain(src,dst):
    dst.parent.mkdir(parents=True,exist_ok=True)
    if dst.exists() and dst.read_bytes()!=src.read_bytes():
        old=dst.with_name(dst.stem+'-'+sha(dst)[:16]+dst.suffix)
        if not old.exists():shutil.copy2(dst,old)
    shutil.copy2(src,dst)

patterns=['md-morse-*','md-cyclic-signed-*','md-undecorated-cancellation-bipyramid-*',
          'md-root-face-*','md-audit-root-face-*','md-guide-primary-*','md-notation-*',
          'md-methods-*','md-insert-guide-method-references.py','md-archive-morse-methods-work.py']
for pattern in patterns:
    for src in tmp.glob(pattern):
        if src.is_file():retain(src,archive/'private'/src.name)
        elif src.is_dir():
            for p in src.rglob('*'):
                if p.is_file():retain(p,archive/'private'/src.name/p.relative_to(src))
retain(tmp/'md-morse-cyclic-progress.md',archive/'README.md')

if '--sync' in __import__('sys').argv:
    rows=json.loads((tmp/'md-methods-workspace-plan.json').read_text())
    for row in rows:
        if row['workspace_state'] not in {'new','current','base','historical'}:
            raise RuntimeError('Unresolved workspace file: '+row['path'])
        name=row['path'];src=pub/name;dst=work/name
        if dst.exists() and dst.read_bytes()!=src.read_bytes():
            retain(dst,archive/'workspace-before'/name)
        retain(src,dst)
        if not name.startswith('docs/'):
            retain(src,archive/'publication'/name)
    for name in ['manuscript/build/build-manifest.json','docs/build-info.json']:
        retain(pub/name,work/name);retain(pub/name,archive/'publication'/name)

manifest={str(p.relative_to(archive)):{'bytes':p.stat().st_size,'sha256':sha(p)}
          for p in archive.rglob('*') if p.is_file() and p.name!='manifest.json'}
(archive/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps({'archive':str(archive),'files':len(manifest),'synced':'--sync' in __import__('sys').argv},indent=2))
