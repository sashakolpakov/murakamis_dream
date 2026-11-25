#!/usr/bin/env python3
"""Check that the current subject papers form one synchronized collection.

Checks source/PDF identity, compiled labels used by the declared graph,
companion links, and the Conway reading route. It does not infer the truth
of a mathematical statement from its label or from a successful build.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
CONWAY_THEOREM = "recursive_strict_volume"
RETIRED = {
    "newton-tangles", "strict-newton-profiles", "conway-geometry",
    "conway-fillings", "local-coefficients", "source-asymptotics",
    "circle-tree-asymptotics", "directed-tree-asymptotics",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        default=ROOT / "repro/results/paper-collection")
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    result_path = args.output / "summary.json"
    result_path.unlink(missing_ok=True)
    catalog_path = ROOT / "papers/catalog.json"
    catalog = json.loads(catalog_path.read_text())
    entries = {p["directory"]: p for p in catalog["papers"]}
    series_path = ROOT / "papers/conway-series.json"
    series = json.loads(series_path.read_text())
    if (series["lead"] != "conway-asymptotics"
            or len(series["papers"]) != len(set(series["papers"]))
            or not set(series["papers"]) <= set(entries)):
        raise ValueError("The Conway series must name distinct current papers and its lead.")
    prior = set()
    for paper in series["papers"]:
        if not set(series["direct_prerequisites"][paper]) <= prior:
            raise ValueError(f"The Conway series prerequisite order fails at {paper}")
        prior.add(paper)
    if len(entries) != len(catalog["papers"]) or not catalog.get("edition"):
        raise ValueError("The collection needs a dated catalog without repeated papers.")
    if set(entries) & RETIRED or any(p.get("edition") == "earlier" for p in entries.values()):
        raise ValueError("An obsolete edition remains in the current catalog.")
    actual = {p.parent.name for p in (ROOT / "papers").glob("*/main.tex")}
    if actual != set(entries):
        raise ValueError(f"Paper folders differ from the catalog: {actual ^ set(entries)}")
    for name in RETIRED:
        if (ROOT / "papers" / name).exists() or (ROOT / "docs/papers" / (name + ".pdf")).exists():
            raise ValueError(f"Superseded paper copy remains: {name}")

    pins = {"papers/catalog.json": digest(catalog_path),
            "papers/conway-series.json": digest(series_path),
            str(Path(__file__).resolve().relative_to(ROOT)): digest(Path(__file__))}
    reports = {}
    labels = {}
    for name, entry in entries.items():
        folder = ROOT / "papers" / name
        readme = folder / "README.md"
        if not readme.is_file():
            raise ValueError(f"Missing current source guide: {name}")
        pins[str(readme.relative_to(ROOT))] = digest(readme)
        build = folder / "build"
        manifest_path = build / "build-manifest.json"
        report = json.loads(manifest_path.read_text())
        if (report["directory"] != name or report.get("edition") != catalog["edition"]
                or report["title"] != entry["title"] or report["status"] != entry["status"]
                or report["imports"] != entry["imports"]):
            raise ValueError(f"Build metadata is out of date: {name}")
        if report["pages"] != entry["pages"] or not 1 <= report["pages"] <= entry["page_limit"]:
            raise ValueError(f"Catalog page count differs from the actual build: {name}")
        for path, expected in report["source_sha256"].items():
            if digest(ROOT / path) != expected:
                raise ValueError(f"Stale source in {name}: {path}")
            pins[path] = expected
        for pdf in [build / "main.pdf", ROOT / "docs/papers" / (name + ".pdf")]:
            if digest(pdf) != report["pdf_sha256"]:
                raise ValueError(f"Stale PDF: {pdf.relative_to(ROOT)}")
        public_manifest = ROOT / "docs/papers" / (name + "-build.json")
        if manifest_path.read_bytes() != public_manifest.read_bytes():
            raise ValueError(f"Public and local build metadata differ: {name}")
        aux = (build / "main.aux").read_text()
        labels[name] = dict(re.findall(r"\\newlabel\{([^}]+)\}\{\{([^}]*)\}", aux))
        if not labels[name]:
            raise ValueError(f"No compiled mathematical labels found: {name}")
        reports[name] = {
            "title": entry["title"], "pages": report["pages"],
            "pdf": str((ROOT / "docs/papers" / (name + ".pdf")).relative_to(ROOT)),
            "pdf_sha256": report["pdf_sha256"],
            "manifest": str(public_manifest.relative_to(ROOT)),
            "manifest_sha256": digest(public_manifest),
            "compiled_labels": len(labels[name]),
        }

    old_paths = re.compile(r"(?:papers/|\.\./)(?:" + "|".join(map(re.escape, RETIRED)) + r")(?:/|\.pdf)")
    companion_links = set()
    for name in entries:
        for path in (ROOT / "papers" / name).rglob("*"):
            if not path.is_file() or "build" in path.parts or path.suffix not in {".tex", ".bib", ".py", ".md"}:
                continue
            content = path.read_text()
            if old_paths.search(content):
                raise ValueError(f"A current paper still refers to a retired path: {path.relative_to(ROOT)}")
            pins[str(path.relative_to(ROOT))] = digest(path)
            targets = re.findall(r"https://sashakolpakov\.github\.io/murakamis_dream/papers/([a-z0-9-]+)\.pdf", content)
            for tag, target in re.findall(
                r"https://github\.com/sashakolpakov/murakamis_dream/blob/([^/]+)/docs/papers/([a-z0-9-]+)\.pdf", content
            ):
                if tag != series["git_tag"] or target not in series["papers"]:
                    raise ValueError(f"Unregistered series edition in {path.relative_to(ROOT)}")
                targets.append(target)
            for target in targets:
                if target not in entries:
                    raise ValueError(f"Unknown companion PDF in {path.relative_to(ROOT)}: {target}")
                companion_links.add((name, target))

    graph_path = ROOT / "papers/dependencies.json"
    graph = json.loads(graph_path.read_text())
    if set(graph["articles"]) != set(entries):
        raise ValueError("The article graph and current paper catalog differ.")
    analysis_path = ROOT / "docs/papers/dependency-analysis.json"
    analysis = json.loads(analysis_path.read_text())
    for path, expected in analysis["source_sha256"].items():
        if digest(ROOT / path) != expected:
            raise ValueError(f"The paper graph is out of date: {path}")
        pins[path] = expected
    checked_labels = {}
    for node in graph["nodes"]:
        for source in node["sources"]:
            parts = Path(source["path"]).parts
            match = re.search(r"\\label\{([^}]+)\}", source["anchor"])
            if len(parts) < 3 or parts[0] != "papers" or parts[1] not in entries or not match:
                continue
            name, label = parts[1], match.group(1)
            if source["path"] not in pins or label not in labels[name]:
                raise ValueError(f"Graph export is not in the compiled paper: {name}:{label}")
            checked_labels[name + ":" + label] = labels[name][label]

    lead_nodes = [n["id"] for n in graph["nodes"] if n["id"] == CONWAY_THEOREM and any(
        s["path"] == "papers/conway-asymptotics/introduction.tex"
        and s["anchor"] in {r"\label{ca:main}", r"\label{ca:volume}"}
        for s in n["sources"])]
    if len(lead_nodes) != 1:
        raise ValueError("The Conway main theorem needs one declared proof route.")
    route = analysis["prerequisite_routes"][lead_nodes[0]]
    if route["unowned_statements"]:
        raise ValueError("A Conway prerequisite has no current paper home.")
    conway_papers = route["articles"]
    if set(conway_papers) != set(series["papers"]):
        raise ValueError("The source series and the mathematical dependency closure differ.")
    supporting = [name for name in conway_papers if name != "conway-asymptotics"]
    result = {
        "scope": "Current collection consistency, actual compiled exports, source/PDF identity and declared reading dependencies; not verification of analytic or geometric proofs.",
        "edition": catalog["edition"], "papers": reports,
        "conway_series_tag": series["git_tag"],
        "total_pages": sum(r["pages"] for r in reports.values()),
        "compiled_graph_exports_checked": checked_labels,
        "companion_links_checked": sorted(companion_links),
        "conway_reading_route": {
            "theorem": lead_nodes[0], "lead": "conway-asymptotics",
            "supporting_papers": supporting,
            "total_pages": sum(reports[name]["pages"] for name in conway_papers),
        },
        "source_sha256": dict(sorted(pins.items())),
    }
    result_path.write_text(json.dumps(result, indent=2) + "\n")
    print(f"Checked {len(entries)} current papers, {len(checked_labels)} compiled graph exports, "
          f"and {len(companion_links)} companion links.")
    print(f"Conway route: the lead paper and {len(supporting)} supporting papers; "
          f"{result['conway_reading_route']['total_pages']} pages in total.")


if __name__ == "__main__":
    main()
