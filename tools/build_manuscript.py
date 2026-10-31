#!/usr/bin/env python3
"""Build the authored manuscript without running research or certificate jobs."""
from __future__ import annotations
import argparse
import hashlib
import json
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'manuscript'
BUILD = SOURCE / 'build'

def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build_figures() -> dict[str, str]:
    """Compile reusable native TikZ illustrations; raster previews if gs exists."""
    directory = BUILD / 'figures'
    directory.mkdir(parents=True, exist_ok=True)
    pdflatex = shutil.which('pdflatex')
    if not pdflatex:
        raise SystemExit('pdflatex is required to compile the native figures.')
    preamble = r'''\documentclass[tikz,border=8pt]{standalone}
\usepackage{amsmath,amssymb,lmodern}
\usetikzlibrary{arrows.meta,positioning,calc,fit,intersections}
\newcommand{\ii}{\mathrm i}
\newcommand{\Vol}{\operatorname{Vol}}
\tikzset{box/.style={draw,rounded corners,fill=blue!4,align=center,inner sep=7pt},arr/.style={-{Latex[length=2mm]},thick}}
\begin{document}
'''
    outputs = {}
    for figure in sorted((SOURCE / 'figures').glob('*.tex')):
        wrapper = directory / (figure.stem + '-standalone.tex')
        wrapper.write_text(preamble + r'\input{figures/' + figure.stem + '}\n' + r'\end{document}' + '\n')
        command = [pdflatex, '-interaction=nonstopmode', '-halt-on-error', '-file-line-error',
                   '-jobname=' + figure.stem, '-output-directory=build/figures', str(wrapper.relative_to(SOURCE))]
        result = subprocess.run(command, cwd=SOURCE, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        if result.returncode:
            print(result.stdout[-8000:])
            raise SystemExit(result.returncode)
        pdf = directory / (figure.stem + '.pdf')
        outputs[str(pdf.relative_to(ROOT))] = sha256(pdf)
        gs = shutil.which('gs')
        if gs:
            png = directory / (figure.stem + '.png')
            subprocess.run([gs, '-q', '-dSAFER', '-dBATCH', '-dNOPAUSE', '-sDEVICE=pngalpha',
                            '-r120', '-sOutputFile=' + str(png), str(pdf)], check=True)
            outputs[str(png.relative_to(ROOT))] = sha256(png)
    return outputs

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--clean', action='store_true', help='Remove only manuscript/build before building.')
    args = parser.parse_args()
    latexmk = shutil.which('latexmk')
    if not latexmk:
        raise SystemExit('latexmk is required (TeX Live or MacTeX). No files were changed.')
    if args.clean and BUILD.exists():
        shutil.rmtree(BUILD)
    BUILD.mkdir(parents=True, exist_ok=True)
    figure_outputs = build_figures()
    command = [latexmk, '-pdf', '-interaction=nonstopmode', '-halt-on-error', '-file-line-error', '-outdir=build', 'main.tex']
    result = subprocess.run(command, cwd=SOURCE, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    (BUILD / 'build-console.txt').write_text(result.stdout)
    if result.returncode:
        print(result.stdout[-12000:])
        raise SystemExit(result.returncode)
    log = (BUILD / 'main.log').read_text(errors='replace')
    fatal = ['There were undefined references', 'There were undefined citations', 'Citation `']
    if any(s in log for s in fatal):
        raise SystemExit('LaTeX completed with unresolved references/citations; see manuscript/build/main.log.')
    inputs = sorted(p for p in SOURCE.rglob('*') if p.suffix in {'.tex', '.bib'} and BUILD not in p.parents)
    metadata = {'schema': 1, 'scope': 'Typesetting only; does not replay mathematical certificates.',
                'command': ['latexmk', '-pdf', '-interaction=nonstopmode', '-halt-on-error', '-file-line-error', '-outdir=build', 'main.tex'], 'inputs': {str(p.relative_to(ROOT)): sha256(p) for p in inputs},
                'figures': figure_outputs,
                'pdf': str((BUILD / 'main.pdf').relative_to(ROOT)), 'pdf_sha256': sha256(BUILD / 'main.pdf'),
                'warnings': [line for line in log.splitlines() if 'Warning:' in line or 'Overfull' in line]}
    (BUILD / 'build-manifest.json').write_text(json.dumps(metadata, indent=2) + '\n')
    print(f'Built {BUILD / "main.pdf"}')
    print(f'SHA256 {metadata["pdf_sha256"]}')
    print(f'{len(metadata["warnings"])} typesetting warnings; see build-manifest.json.')

if __name__ == '__main__':
    main()
