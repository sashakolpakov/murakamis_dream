#!/usr/bin/env python3
"""Build the mathematical papers, check their length, and publish the resulting PDFs.

Requires latexmk and PyMuPDF. This command checks typesetting and records
dependencies; it does not verify the mathematics or turn an imported theorem
into a proof. The complete reference manuscript is left unchanged.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[1]


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("papers", nargs="*", help="Directory names; default: all papers in catalog.json.")
    parser.add_argument("--no-publish", action="store_true", help="Build locally without copying PDFs into docs/papers.")
    args = parser.parse_args()
    latexmk = shutil.which("latexmk")
    if not latexmk:
        raise SystemExit("latexmk is required (TeX Live or MacTeX).")
    try:
        import pymupdf
    except ImportError:
        raise SystemExit("PyMuPDF is required to count the PDF pages: python3 -m pip install pymupdf")
    catalog = json.loads((ROOT / "papers/catalog.json").read_text())
    entries = {entry["directory"]: entry for entry in catalog["papers"]}
    unknown = set(args.papers) - entries.keys()
    if unknown:
        raise SystemExit("Unknown paper: " + ", ".join(sorted(unknown)))
    selected = args.papers or list(entries)
    reports = []
    for name in selected:
        entry = entries[name]
        source = ROOT / "papers" / name
        build = source / "build"
        build.mkdir(parents=True, exist_ok=True)
        command = [latexmk, "-pdf", "-interaction=nonstopmode", "-halt-on-error",
                   "-file-line-error", "-outdir=build", "main.tex"]
        result = subprocess.run(command, cwd=source, text=True, stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT)
        (build / "build-console.txt").write_text(result.stdout)
        if result.returncode:
            raise SystemExit(result.stdout[-10000:])
        log = (build / "main.log").read_text(errors="replace")
        if re.search(r"undefined references|undefined citations|(?:Reference|Citation) .+ undefined|multiply defined", log):
            raise SystemExit(f"{name}: unresolved or duplicated reference; see {build / 'main.log'}")
        pdf = build / "main.pdf"
        with pymupdf.open(pdf) as document:
            pages = len(document)
        if not 1 <= pages <= entry["page_limit"]:
            raise SystemExit(f"{name}: {pages} pages exceeds the {entry['page_limit']}-page limit.")
        overfull = [line for line in log.splitlines() if "Overfull" in line]
        if overfull:
            raise SystemExit(f"{name}: overfull boxes need inspection and correction:\n" + "\n".join(overfull))
        inputs = sorted(p for p in source.rglob("*") if p.suffix in {".tex", ".bib"} and build not in p.parents)
        report = {"directory": name, "title": entry["title"], "status": entry["status"],
                  "pages": pages, "page_limit": entry["page_limit"],
                  "imports": entry["imports"], "pdf_sha256": digest(pdf),
                  "source_sha256": {str(p.relative_to(ROOT)): digest(p) for p in inputs},
                  "warnings": [line for line in log.splitlines() if "Warning:" in line],
                  "scope": "Typesetting, page count and declared imports only; not proof verification."}
        (build / "build-manifest.json").write_text(json.dumps(report, indent=2) + "\n")
        reports.append((report, pdf))
        print(f"{name}: {pages} pages; no unresolved references or overfull boxes.")
    # Copy only after every selected paper passes the checks.
    if not args.no_publish:
        destination = ROOT / "docs/papers"
        destination.mkdir(parents=True, exist_ok=True)
        for report, pdf in reports:
            shutil.copyfile(pdf, destination / (report["directory"] + ".pdf"))
            (destination / (report["directory"] + "-build.json")).write_text(json.dumps(report, indent=2) + "\n")


if __name__ == "__main__":
    main()
