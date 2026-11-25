#!/usr/bin/env python3
"""Prepare and compile source-only Conway-series archives, entirely offline.

The TeX recorder supplies each article's dependency closure. Repository-local
inputs must be TeX, bibliography sources, or figure assets. Dependencies outside
the article directory are copied under _vendor, and references are rewritten
only in the temporary package. The ZIP is extracted and compiled separately.
No credential is read, no network request is made, and no submission occurs.

Requires latexmk, kpsewhich, and PyMuPDF. Run after the series sources freeze:
    .venv/bin/python tools/prepare_conway_submission.py
The default output is ignored build/submission/conway-series-<edition>/.
Metadata are drafts, not a claim that the platform has validated a request.
"""
from __future__ import annotations

import argparse
from datetime import date
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import zipfile


ROOT = Path(__file__).resolve().parents[1]
SERIES = ROOT / "papers/conway-series.json"
POLICY = ROOT / "hexagon_parameters.local"
ALLOWED_PAPERS = (
    "filling-bounds", "newton-calculus", "conway-source-bounds",
    "marked-fillings", "strict-conway-geometry", "oscillatory-fillings",
    "conway-asymptotics",
)
SOURCE_SUFFIXES = {".tex", ".bib"}
FIGURE_SUFFIXES = {".pdf", ".png", ".jpg", ".jpeg", ".eps", ".svg"}
ALLOWED_SUFFIXES = SOURCE_SUFFIXES | FIGURE_SUFFIXES
MAX_ARCHIVE_BYTES = 100 * 1024**2
MAX_COMBINED_BYTES = 250 * 1024**2
# These classifications concern the articles themselves. They are not copied
# from the unrelated example work recorded in hexagon_parameters.local.
CLASSIFICATIONS = {
    "filling-bounds": ("math.GT", ["math.QA"], ["57K16", "57K10"],
                       "Finite quantum tangle evaluations and knot invariants."),
    "newton-calculus": ("math.GT", ["math.QA"], ["57K16", "57K10"],
                        "Root-of-unity tangle calculus and its variational profiles."),
    "conway-source-bounds": ("math.GT", ["math.QA"], ["57K16"],
                            "Spectral estimates for quantum tangle evaluations."),
    "marked-fillings": ("math.GT", ["math.MG"], ["57K32", "57K10"],
                        "Marked hyperbolic link exteriors and Dehn fillings."),
    "strict-conway-geometry": ("math.GT", ["math.MG"], ["57K32", "57K10"],
                               "Hyperbolic geometry of augmented tangle compositions."),
    "oscillatory-fillings": ("math.CA", ["math.GT"], ["41A60"],
                             "Asymptotics of finite oscillatory sums."),
    "conway-asymptotics": ("math.GT", ["math.QA"], ["57K16", "57K32"],
                           "Quantum invariant asymptotics and hyperbolic volume."),
}
PATH_COMMAND = re.compile(
    r"(\\(?:input|include|includegraphics\*?|bibliography|addbibresource)"
    r"\s*(?:\[[^\]]*\]\s*)?\{)([^{}]+)(\})")


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def json_write(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False,
                               sort_keys=True) + "\n")


def run(command: list[str], cwd: Path, *, env: dict[str, str] | None = None) -> str:
    result = subprocess.run(command, cwd=cwd, env=env, text=True,
                            stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    if result.returncode:
        raise RuntimeError(f"Command failed in {cwd}: {command[0]}\n"
                           + result.stdout[-7000:])
    return result.stdout


def tex_environment(*, isolated: bool) -> dict[str, str]:
    env = os.environ.copy()
    # A user TEXINPUTS pointing into the repository could hide a missing file.
    for name in ("TEXINPUTS", "BIBINPUTS", "BSTINPUTS", "TEXMFOUTPUT"):
        env.pop(name, None)
    # The reviewed repository sources may use ../ for shared figures.
    # The extracted package has no reason to read above its own root.
    env["openin_any"] = "p" if isolated else "r"
    env["openout_any"] = "p"
    return env


def compile_article(directory: Path, build_name: str, *, isolated: bool = False) -> dict:
    command = ["latexmk", "-pdf", "-recorder", "-interaction=nonstopmode",
               "-halt-on-error", "-file-line-error", f"-outdir={build_name}",
               "-pdflatex=pdflatex -no-shell-escape %O %S", "main.tex"]
    output = run(command, directory, env=tex_environment(isolated=isolated))
    build = directory / build_name
    (build / "preflight-build.txt").write_text(output)
    log = (build / "main.log").read_text(errors="replace")
    bad = re.search(r"undefined references|undefined citations|"
                    r"(?:Reference|Citation) .+ undefined|multiply defined|Overfull", log)
    if bad:
        raise RuntimeError(f"Unresolved reference or overfull box: {build / 'main.log'}")
    import pymupdf
    with pymupdf.open(build / "main.pdf") as document:
        pages = len(document)
    return {"pages": pages, "pdf": build / "main.pdf", "fls": build / "main.fls",
            "warnings": [line for line in log.splitlines() if "Warning:" in line]}


def system_tex_roots() -> tuple[Path, ...]:
    roots = []
    for variable in ("TEXMFDIST", "TEXMFLOCAL", "TEXMFSYSVAR", "TEXMFSYSCONFIG"):
        value = run(["kpsewhich", f"-var-value={variable}"], ROOT).strip()
        if value and "$" not in value and "{" not in value:
            roots.append(Path(value).expanduser().resolve())
    if not roots:
        raise RuntimeError("Could not locate the installed TeX distribution.")
    return tuple(roots)


def recorder_inputs(fls: Path, cwd: Path) -> set[Path]:
    inputs = set()
    for line in fls.read_text().splitlines():
        if line.startswith("INPUT "):
            path = Path(line[6:])
            candidate = path if path.is_absolute() else cwd / path
            if candidate.is_file():
                inputs.add(candidate.resolve())
    return inputs


def allowed_file(path: Path) -> bool:
    return (path.suffix.lower() in ALLOWED_SUFFIXES
            and not any(part.startswith(".") for part in path.parts)
            and ".." not in path.parts)


def bibliography_inputs(directory: Path, tex_inputs: set[Path]) -> set[Path]:
    # BibTeX/Biber do not write their reads to pdflatex's .fls. Their input
    # declarations supplement the recorder for articles with external .bib files.
    found = set()
    for path in tex_inputs:
        if path.suffix == ".tex":
            text = path.read_text()
            for match in PATH_COMMAND.finditer(text):
                if "bibliography" not in match[1] and "addbibresource" not in match[1]:
                    continue
                for name in match[2].split(","):
                    source = directory / name.strip()
                    if not source.suffix:
                        source = source.with_suffix(".bib")
                    if not source.is_file():
                        raise RuntimeError(f"Unresolved bibliography: {source}")
                    found.add(source.resolve())
    return found


def source_closure(directory: Path, fls: Path,
                   system_roots: tuple[Path, ...]) -> set[Path]:
    found = set()
    for path in recorder_inputs(fls, directory):
        if any(path.is_relative_to(base) for base in system_roots):
            continue
        if path.is_relative_to(directory / "build"):
            # Auxiliary files are generated on the standalone replay.
            continue
        if not path.is_relative_to(ROOT):
            raise RuntimeError(f"Input outside the repository and installed TeX: {path}")
        if not allowed_file(path.relative_to(ROOT)):
            raise RuntimeError(f"Repository input is not an allowed manuscript/figure: {path}")
        found.add(path)
    found |= bibliography_inputs(directory, found)
    if directory / "main.tex" not in found:
        raise RuntimeError("Recorder did not include the article's main.tex.")
    for path in found:
        if not path.is_relative_to(ROOT) or not allowed_file(path.relative_to(ROOT)):
            raise RuntimeError(f"Disallowed source dependency: {path}")
    return found


def destination(path: Path, directory: Path) -> Path:
    if path.is_relative_to(directory):
        return path.relative_to(directory)
    return Path("_vendor") / path.relative_to(ROOT)


def rewrite_references(text: str, directory: Path, mapping: dict[Path, Path]) -> str:
    def replace(match: re.Match) -> str:
        names = []
        for original in match[2].split(","):
            name = original.strip()
            base = directory / name
            candidates = [base]
            if not base.suffix:
                candidates += [base.with_suffix(ext) for ext in sorted(ALLOWED_SUFFIXES)]
            resolved = next((candidate.resolve() for candidate in candidates
                             if candidate.resolve() in mapping), None)
            if resolved is None:
                names.append(original)
                continue
            target = mapping[resolved]
            # All TeX input paths are resolved from the article's compilation
            # directory, including commands inside a nested input file.
            if not resolved.is_relative_to(directory):
                if (re.search(r"\\include\s*\{", match[1])
                        or "bibliography" in match[1]):
                    target = target.with_suffix("")
                names.append(target.as_posix())
            else:
                names.append(original)
        return match[1] + ",".join(names) + match[3]
    return PATH_COMMAND.sub(replace, text)


def braced_command(text: str, command: str) -> str:
    match = re.search(r"\\" + re.escape(command) + r"\s*\{", text)
    if not match:
        raise RuntimeError(f"Missing \\{command} in main.tex")
    depth, start = 1, match.end()
    for index in range(start, len(text)):
        if text[index] in "{}" and (index == 0 or text[index - 1] != "\\"):
            depth += 1 if text[index] == "{" else -1
            if depth == 0:
                return text[start:index].strip()
    raise RuntimeError(f"Unclosed \\{command} argument")


def pdf_content(path: Path) -> list:
    """Compare visible text and link targets, ignoring PDF IDs and xrefs."""
    import pymupdf
    result = []
    with pymupdf.open(path) as document:
        for page in document:
            links = []
            for link in page.get_links():
                target = {key: link[key] for key in ("kind", "uri", "file", "page", "nameddest")
                          if key in link}
                if "to" in link:
                    point = link["to"]
                    target["to"] = ([round(point.x, 4), round(point.y, 4)]
                                    if hasattr(point, "x") else str(point))
                links.append(target)
            result.append([page.get_text(), links])
    return result


def metadata(slug: str, source: Path, pages: int, policy: dict,
             series: dict) -> dict:
    text = source.read_text()
    abstract = re.search(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", text, re.S)
    if not abstract:
        raise RuntimeError(f"No abstract in {source}")
    fixed = policy["fixed_administrative_parameters"]
    required = ("authors", "submittingContributorIndex", "sponsorName",
                "submittingOrganizationId", "license", "authorshipMode",
                "humanUnderstanding", "provenance", "correctnessConfirmed",
                "communityInterestConfirmed", "citationsConfirmed", "rightsConfirmed")
    draft = {key: fixed[key] for key in required}
    subject, cross_lists, msc, rationale = CLASSIFICATIONS[slug]
    title = braced_command(text, "title").replace(r"\\", " ")
    title = re.sub(r"\\(?:newline|linebreak)(?:\[[^\]]*\])?", " ", title)
    draft.update({
        "title": " ".join(title.split()),
        "abstract": " ".join(abstract[1].split()),
        "subject": subject, "crossListSubjects": cross_lists,
        "mscCodes": msc, "tags": [], "pageCount": pages,
        "comments": f"{pages} pages. Part of the Conway series, edition "
                    f"{series['edition']}. Companion proof dependencies are "
                    "stated in the manuscript.",
        "formalizations": [],
    })
    author = braced_command(text, "author")
    return {"draft": draft, "classification_rationale": rationale,
            "abstract_encoding": "TeX from this article's abstract, whitespace normalized",
            "manuscript_author_matches": all(a["name"] in author for a in fixed["authors"]),
            "edition_git_tag": series["git_tag"],
            "notes": ["Offline draft only; not checked against a live API schema.",
                      "Fixed administrative declarations reuse the user's standing policy.",
                      "No formalization artifact or code is included in the source archive."]}


def prepare(slug: str, output: Path, series: dict, policy: dict,
            system_roots: tuple[Path, ...], page_limit: int) -> dict:
    directory = ROOT / "papers" / slug
    # Keep the official build/main.pdf and its build manifest untouched.
    compiled = compile_article(directory, "build/submission-read")
    closure = source_closure(directory, compiled["fls"], system_roots)
    before = {str(path.relative_to(ROOT)): digest(path) for path in sorted(closure)}
    mapping = {path: destination(path, directory) for path in closure}
    if len(set(mapping.values())) != len(mapping):
        raise RuntimeError(f"{slug}: vendored and article-local paths collide.")
    article_output = output / slug
    article_output.mkdir(parents=True, exist_ok=True)
    archive = article_output / f"{slug}-source.zip"
    # A failed rerun cannot leave an old report that appears to describe it.
    (article_output / "preflight.json").unlink(missing_ok=True)
    archive.unlink(missing_ok=True)
    with tempfile.TemporaryDirectory(prefix=f"conway-submit-{slug}-") as temporary:
        temporary_root = Path(temporary).resolve()
        package = temporary_root / "package"
        package.mkdir()
        rewrites = []
        for path, target in sorted(mapping.items()):
            copied = package / target
            copied.parent.mkdir(parents=True, exist_ok=True)
            if path.suffix == ".tex":
                original = path.read_text()
                revised = rewrite_references(original, directory, mapping)
                copied.write_text(revised)
                if original != revised:
                    rewrites.append(str(target))
            else:
                shutil.copyfile(path, copied)
        members = sorted(path for path in package.rglob("*") if path.is_file())
        if not all(allowed_file(path.relative_to(package)) for path in members):
            raise RuntimeError("Package contains a disallowed file.")
        expanded_bytes = sum(path.stat().st_size for path in members)
        if expanded_bytes > MAX_COMBINED_BYTES:
            raise RuntimeError("Expanded source exceeds the 250 MiB combined limit.")
        edition_date = date.fromisoformat(str(series["edition"]))
        timestamp = (edition_date.year, edition_date.month, edition_date.day, 0, 0, 0)
        temporary_archive = temporary_root / "source.zip"
        with zipfile.ZipFile(temporary_archive, "w", zipfile.ZIP_DEFLATED) as zipped:
            for path in members:
                info = zipfile.ZipInfo(path.relative_to(package).as_posix(), timestamp)
                info.create_system = 3
                info.external_attr = 0o100644 << 16
                zipped.writestr(info, path.read_bytes(), compress_type=zipfile.ZIP_DEFLATED)
        archive_bytes = temporary_archive.stat().st_size
        if (archive_bytes > MAX_ARCHIVE_BYTES
                or archive_bytes + expanded_bytes > MAX_COMBINED_BYTES):
            raise RuntimeError("Source ZIP exceeds the 100 MiB archive or 250 MiB combined limit.")
        extracted = temporary_root / "extracted"
        extracted.mkdir()
        with zipfile.ZipFile(temporary_archive) as zipped:
            if any(not allowed_file(Path(name)) or Path(name).is_absolute()
                   for name in zipped.namelist()):
                raise RuntimeError("Unsafe archive member.")
            zipped.extractall(extracted)
        replay = compile_article(extracted, "_build", isolated=True)
        for path in recorder_inputs(replay["fls"], extracted):
            if not path.is_relative_to(extracted) and not any(
                    path.is_relative_to(base) for base in system_roots):
                raise RuntimeError(f"Standalone compile read an unbundled input: {path}")
        if not 1 <= replay["pages"] <= page_limit:
            raise RuntimeError(f"{slug}: standalone PDF is {replay['pages']} pages; "
                               f"limit is {page_limit}.")
        if compiled["pages"] != replay["pages"]:
            raise RuntimeError(f"{slug}: repository and standalone page counts differ.")
        canonical = directory / "build/main.pdf"
        if not canonical.is_file():
            raise RuntimeError(f"Run tools/build_papers.py for {slug} before packaging.")
        if pdf_content(canonical) != pdf_content(replay["pdf"]):
            raise RuntimeError(f"{slug}: standalone PDF text or link targets differ from "
                               "the canonical PDF; rebuild the current sources first.")
        pdf = article_output / f"{slug}.pdf"
        shutil.copyfile(replay["pdf"], pdf)
        shutil.copyfile(temporary_archive, archive)
        archive_members = {str(path.relative_to(extracted)): digest(path)
                           for path in sorted(extracted.rglob("*"))
                           if path.is_file() and "_build" not in path.relative_to(extracted).parts}
    for relative, expected in before.items():
        if digest(ROOT / relative) != expected:
            raise RuntimeError(f"Source changed during preparation: {relative}")
    draft = metadata(slug, directory / "main.tex", replay["pages"], policy, series)
    json_write(article_output / "metadata-draft.json", draft)
    report = {
        "paper": slug, "edition": series["edition"], "git_tag": series["git_tag"],
        "pages": replay["pages"], "page_limit": page_limit,
        "source_sha256": before, "archive_members_sha256": archive_members,
        "archive_sha256": digest(archive), "pdf_sha256": digest(pdf),
        "archive_bytes": archive_bytes, "expanded_source_bytes": expanded_bytes,
        "combined_source_bytes": archive_bytes + expanded_bytes,
        "canonical_pdf_text_and_link_targets_match": True,
        "rewritten_files_in_package_only": rewrites,
        "warnings": replay["warnings"], "standalone_compile": "passed",
        "credential_read": False, "network_requests": False,
        "archive_policy": "Only recorder-selected TeX/bibliography sources and figure assets.",
        "scope": "Dependency closure, standalone typesetting and metadata draft only; "
                 "not mathematical proof verification or remote submission.",
    }
    json_write(article_output / "preflight.json", report)
    print(f"{slug}: source ZIP compiles independently; {replay['pages']} pages; "
          f"{len(archive_members)} archive files.", flush=True)
    return report


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("papers", nargs="*", metavar="PAPER",
                        help="Default: the seven papers in the series manifest.")
    parser.add_argument("--output", type=Path,
                        help="Output directory, confined to ignored build/submission/.")
    args = parser.parse_args()
    if set(args.papers) - set(ALLOWED_PAPERS) or len(args.papers) != len(set(args.papers)):
        parser.error("Choose each paper at most once from: " + ", ".join(ALLOWED_PAPERS))
    if not SERIES.is_file():
        raise SystemExit(f"Missing series manifest: {SERIES}")
    series = json.loads(SERIES.read_text())
    listed = [entry if isinstance(entry, str) else entry["directory"]
              for entry in series["papers"]]
    if set(listed) != set(ALLOWED_PAPERS) or len(listed) != len(ALLOWED_PAPERS):
        raise SystemExit("Series manifest must list exactly the seven allowed papers once.")
    edition_name = str(series["edition"])
    if not re.fullmatch(r"[0-9A-Za-z._-]+", edition_name):
        raise SystemExit("Unsafe edition name.")
    base = ROOT / "build/submission"
    output = (args.output or base / f"conway-series-{edition_name}").resolve()
    if not output.is_relative_to(base.resolve()):
        raise SystemExit("Generated submission files must remain under build/submission/.")
    output.mkdir(parents=True, exist_ok=True)
    (output / "summary.json").unlink(missing_ok=True)
    policy = json.loads(POLICY.read_text())  # Public metadata; never read a credential.
    if policy["schema"] != "hexagon-fixed-submission-parameters-v1":
        raise SystemExit("Unknown public submission-parameter schema.")
    catalog = json.loads((ROOT / "papers/catalog.json").read_text())
    limits = {entry["directory"]: entry["page_limit"] for entry in catalog["papers"]}
    roots = system_tex_roots()
    reports = [prepare(slug, output, series, policy, roots, limits[slug])
               for slug in (args.papers or listed)]
    # Detect changes to an earlier article while a later archive was compiling.
    for report in reports:
        for relative, expected in report["source_sha256"].items():
            if digest(ROOT / relative) != expected:
                raise SystemExit(f"Source changed during collection preparation: {relative}")
    json_write(output / "summary.json", {
        "edition": series, "papers": reports, "tool_sha256": digest(Path(__file__)),
        "scope": "Offline publication preparation; no credentials, network, or submission.",
        "limitations": [
            "The recorder describes files read on this TeX build, not every dormant macro branch.",
            "Bibliography declarations supplement pdflatex's recorder for BibTeX/Biber inputs.",
            "Reference rewriting supports ordinary braced input/graphics/bibliography commands; "
            "the isolated compile rejects missing or unbundled dependencies.",
            "Installed TeX packages are build prerequisites, not bundled source files.",
            "Bibliography links do not define the mathematical dependency graph.",
            "A successful compile checks neither mathematical correctness nor live API compatibility.",
        ],
    })
    print(f"Offline preparation complete: {output / 'summary.json'}")


if __name__ == "__main__":
    main()
