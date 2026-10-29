#!/usr/bin/env python3
"""Compile the editable TikZ figures to PDF, SVG and PNG.

Requires pdfLaTeX with TikZ and PyMuPDF. TeX intermediates stay temporary.
"""
from pathlib import Path
import shutil
import subprocess
import tempfile


def main():
    import pymupdf
    root = Path(__file__).resolve().parents[1]
    figures = root / "book" / "figures"
    if not shutil.which("pdflatex"):
        raise SystemExit("pdfLaTeX is required to render the TikZ figures.")
    for source in sorted(figures.glob("*.tex")):
        with tempfile.TemporaryDirectory(prefix="murakamis-figure-") as tmp:
            subprocess.run(
                ["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
                 "-output-directory", tmp, str(source)],
                check=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
            )
            pdf = Path(tmp) / (source.stem + ".pdf")
            with pymupdf.open(pdf) as document:
                page = document[0]
                page.get_pixmap(matrix=pymupdf.Matrix(2.4, 2.4), alpha=False).save(
                    figures / (source.stem + ".png")
                )
                (figures / (source.stem + ".svg")).write_text(page.get_svg_image(), encoding="utf-8")
            shutil.copyfile(pdf, figures / (source.stem + ".pdf"))
        print(f"Rendered {source.stem}: PDF, SVG, PNG")


if __name__ == "__main__":
    main()
