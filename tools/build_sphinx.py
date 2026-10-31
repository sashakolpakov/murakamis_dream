#!/usr/bin/env python3
"""Build the manuscript reading site in docs/sphinx; no proof jobs run."""
from __future__ import annotations
import argparse
import hashlib
import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'docs' / 'site'
OUTPUT = ROOT / 'docs' / 'sphinx'

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--sphinx-build', help='Explicit sphinx-build executable.')
    args = parser.parse_args()
    executable = args.sphinx_build or shutil.which('sphinx-build')
    command = [executable] if executable else [sys.executable, '-m', 'sphinx']
    pdf = ROOT / 'manuscript' / 'build' / 'main.pdf'
    if not pdf.is_file():
        raise SystemExit('Build the manuscript first: python3 tools/build_manuscript.py')
    command += ['-b', 'html', '-W', '--keep-going', str(SOURCE), str(OUTPUT)]
    subprocess.run(command, cwd=ROOT, check=True)
    metadata = {'schema': 1, 'scope': 'Sphinx typesetting only.', 'command': ['python3', '-m', 'sphinx', '-b', 'html', '-W', '--keep-going', 'docs/site', 'docs/sphinx'],
                'pdf_sha256': hashlib.sha256(pdf.read_bytes()).hexdigest(),
                'sources': {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
                            for p in sorted(SOURCE.rglob('*')) if p.is_file() and p.suffix in {'.rst', '.py', '.css'}}}
    (OUTPUT / 'build-manifest.json').write_text(json.dumps(metadata, indent=2) + '\n')
    print(f'Built {OUTPUT / "index.html"}')

if __name__ == '__main__':
    main()
