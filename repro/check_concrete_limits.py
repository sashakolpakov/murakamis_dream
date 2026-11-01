#!/usr/bin/env python3
"""Check the optional Mathlib realization of complex-modulus volume transfer.

The Std-only package is a path dependency and remains independently usable.
This checker never downloads dependencies or updates the manifest. Provision
exactly the pinned packages/cache as described in formal-real/README.md first.
The source, saddle/remainder estimates and geometric calibration are still
explicit inputs, not claims made by this optional check.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import tomllib

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "formal-real"
FORMAL = ROOT / "formal"
TOOLCHAIN = "leanprover/lean4:v4.32.2"
NAMESPACE = "VolumeLogic.RealModel."
ALLOWED_AXIOMS = {"propext", "Classical.choice", "Quot.sound"}
# The complete expected Git dependency set, not merely the direct Mathlib pin.
EXPECTED_GIT = {
    "mathlib": ("https://github.com/leanprover-community/mathlib4.git", "905b95818eb32af7874a58b427f50c1711a5e96c"),
    "plausible": ("https://github.com/leanprover-community/plausible", "e12c1910fe855cbfc38803cd4e55543906d5fa62"),
    "LeanSearchClient": ("https://github.com/leanprover-community/LeanSearchClient", "c5d5b8fe6e5158def25cd28eb94e4141ad97c843"),
    "importGraph": ("https://github.com/leanprover-community/import-graph", "7e9612bf0b9ee66db3cb5b9988a35afc706f5a12"),
    "proofwidgets": ("https://github.com/leanprover-community/ProofWidgets4", "6e311e2a844da9b2cc3971187df2fe0066947b93"),
    "aesop": ("https://github.com/leanprover-community/aesop", "a7dbf0c63b694e47f425f3dcddbc0e178bb432d3"),
    "Qq": ("https://github.com/leanprover-community/quote4", "38d591e778f100aec9762bb582f9c7f55f50e9dc"),
    "batteries": ("https://github.com/leanprover-community/batteries", "023ce7d62a0531e22a5331e20b587817a80d49ff"),
    "Cli": ("https://github.com/leanprover/lean4-cli", "88679d088c9720c27ebdf2ba4dafe17341747f94"),
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate_manifest(manifest: dict) -> dict:
    if manifest.get("name") != "volumeReal" or manifest.get("packagesDir") != ".lake/packages":
        raise ValueError("Unexpected optional package name or packages directory.")
    packages = manifest.get("packages", [])
    by_name = {p.get("name"): p for p in packages}
    if len(by_name) != len(packages) or set(by_name) != set(EXPECTED_GIT) | {"volumeLogic"}:
        raise ValueError("Manifest must contain every expected dependency exactly once.")
    local = by_name["volumeLogic"]
    if local.get("type") != "path" or local.get("dir") != "../formal":
        raise ValueError("volumeLogic must be the relative ../formal path dependency.")
    for name, (url, rev) in EXPECTED_GIT.items():
        package = by_name[name]
        if (package.get("type"), package.get("url"), package.get("rev")) != ("git", url, rev):
            raise ValueError(f"Unexpected URL/revision for dependency {name}.")
        if package.get("subDir") is not None:
            raise ValueError(f"Unexpected subdirectory for dependency {name}.")
    return by_name


def uncomment_lean(text: str) -> str:
    """Remove nested block and line comments, retaining line boundaries."""
    out = []
    depth = 0
    index = 0
    while index < len(text):
        if text.startswith("/-", index):
            depth += 1
            index += 2
        elif depth and text.startswith("-/", index):
            depth -= 1
            index += 2
        elif not depth and text.startswith("--", index):
            end = text.find("\n", index)
            index = len(text) if end < 0 else end
        else:
            char = text[index]
            out.append(char if not depth or char == "\n" else " ")
            index += 1
    if depth:
        raise ValueError("Unclosed Lean comment.")
    return "".join(out)


def declaration_inventory(paths: list[Path]) -> dict[str, str]:
    result = {}
    pattern = re.compile(r"^\s*(?:noncomputable\s+)?(def|theorem)\s+(\w+)", re.M)
    unsupported = re.compile(r"^\s*(?:private\s+|protected\s+)?(?:lemma|instance|abbrev|opaque|axiom|structure|class|inductive|constant|example)\b", re.M)
    for path in paths:
        code = uncomment_lean(path.read_text())
        if re.search(r"\b(?:sorry|admit)\b", code) or unsupported.search(code):
            raise ValueError(f"Unsupported or unchecked declaration in {path.name}; extend the explicit inventory first.")
        if re.findall(r"^namespace\s+(\S+)", code, re.M) != [NAMESPACE[:-1]]:
            raise ValueError(f"Unexpected namespace layout in {path.name}.")
        for kind, name in pattern.findall(code):
            full_name = NAMESPACE + name
            if full_name in result:
                raise ValueError("Duplicate declaration: " + full_name)
            result[full_name] = kind
    if not result:
        raise ValueError("No concrete-limit declarations found.")
    return result


def validate_audit(names: dict[str, str], source: str) -> None:
    code = uncomment_lean(source)
    inspected = re.findall(r"^#print axioms (\S+)$", code, re.M)
    if len(inspected) != len(set(inspected)) or sorted(inspected) != sorted(names):
        raise ValueError("AxiomAudit.lean must inspect every definition and theorem exactly once.")
    if any(line.strip() and line.strip() != "import RealTransfer" and
           not re.fullmatch(r"#print axioms \S+", line.strip()) for line in code.splitlines()):
        raise ValueError("Unexpected command in the axiom audit.")


def parse_axioms(names: dict[str, str], log: str) -> dict[str, list[str]]:
    entries = re.findall(r"'([^']+)' depends on axioms:\s*\[([^\]]*)\]", log)
    entries += [(name, "") for name in re.findall(r"'([^']+)' does not depend on any axioms", log)]
    if len(entries) != len(names) or sorted(n for n, _ in entries) != sorted(names):
        raise ValueError("Compiler axiom output must report every expected declaration exactly once.")
    result = {name: sorted(a.strip() for a in atoms.split(",") if a.strip()) for name, atoms in entries}
    for name, atoms in result.items():
        if set(atoms) - ALLOWED_AXIOMS:
            raise ValueError(f"Unexpected axioms in {name}: {atoms}")
    return result


def negative_controls(manifest: dict, names: dict[str, str], audit: str) -> list[str]:
    checks = []
    def reject(label, function, *args):
        try:
            function(*args)
        except ValueError:
            checks.append(label)
        else:
            raise ValueError("Negative control was accepted: " + label)
    for dependency in ("mathlib", "batteries"):
        changed = copy.deepcopy(manifest)
        next(p for p in changed["packages"] if p["name"] == dependency)["rev"] = "0" * 40
        reject("changed_" + dependency + "_revision", validate_manifest, changed)
    changed = copy.deepcopy(manifest)
    changed["packages"].pop()
    reject("missing_transitive_dependency", validate_manifest, changed)
    changed = copy.deepcopy(manifest)
    changed["packages"].append(copy.deepcopy(changed["packages"][0]))
    reject("duplicate_dependency", validate_manifest, changed)
    changed = copy.deepcopy(manifest)
    next(p for p in changed["packages"] if p["name"] == "volumeLogic")["dir"] = "/formal"
    reject("absolute_local_dependency", validate_manifest, changed)
    first = next(iter(names))
    reject("omitted_definition_audit", validate_audit, names, audit.replace("#print axioms " + first, ""))
    reject("duplicate_declaration_audit", validate_audit, names, audit + "\n#print axioms " + first + "\n")
    reject("unexpected_logical_axiom", parse_axioms, {first: names[first]},
           f"'{first}' depends on axioms: [sorryAx]\n")
    return checks


def checked_run(command: list[str], cwd: Path) -> str:
    result = subprocess.run(command, cwd=cwd, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    if result.returncode:
        raise ValueError(result.stdout or f"Command failed: {command[0]}")
    return result.stdout


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lake", default=shutil.which("lake"), help="Lake executable; the package pins Lean 4.32.2.")
    parser.add_argument("--output", type=Path, help="Write fresh logs and deterministic summary here; default is a temporary directory.")
    args = parser.parse_args()
    if not args.lake:
        raise SystemExit("Lake not found. See formal-real/README.md for setup.")
    with tempfile.TemporaryDirectory(prefix="volume-concrete-limits-") as temporary:
        output = args.output.resolve() if args.output else Path(temporary)
        output.mkdir(parents=True, exist_ok=True)
        # A failed replay cannot leave an old success summary behind.
        (output / "summary.json").unlink(missing_ok=True)
        try:
            if (PACKAGE / "lean-toolchain").read_text().strip() != TOOLCHAIN or (FORMAL / "lean-toolchain").read_text().strip() != TOOLCHAIN:
                raise ValueError("Both packages must use the pinned Lean toolchain.")
            config = tomllib.loads((PACKAGE / "lakefile.toml").read_text())
            requires = {entry["name"]: entry for entry in config.get("require", [])}
            if set(requires) != {"volumeLogic", "mathlib"} or len(config["require"]) != 2:
                raise ValueError("Unexpected direct dependency set.")
            if requires["volumeLogic"] != {"name": "volumeLogic", "path": "../formal"}:
                raise ValueError("Use the original relative Std-only package, without copied sources.")
            if requires["mathlib"] != {"name": "mathlib", "git": EXPECTED_GIT["mathlib"][0], "rev": EXPECTED_GIT["mathlib"][1]}:
                raise ValueError("The direct Mathlib dependency is not exactly pinned.")
            manifest = json.loads((PACKAGE / "lake-manifest.json").read_text())
            packages = validate_manifest(manifest)
            materialized = {}
            for name, (_, expected_rev) in sorted(EXPECTED_GIT.items()):
                directory = PACKAGE / manifest["packagesDir"] / name
                if not directory.is_dir():
                    raise ValueError(f"Missing dependency {name}; follow formal-real/README.md. This checker does not download it.")
                actual = checked_run(["git", "rev-parse", "HEAD"], directory).strip()
                if actual != expected_rev:
                    raise ValueError(f"Cached {name} revision differs from its expected pin.")
                if checked_run(["git", "status", "--porcelain", "--untracked-files=no"], directory).strip():
                    raise ValueError(f"Tracked dependency sources are modified: {name}.")
                materialized[name] = {"url": packages[name]["url"], "rev": actual, "tracked_sources_clean": True}
            mathlib = PACKAGE / manifest["packagesDir"] / "mathlib"
            if (mathlib / "lean-toolchain").read_text().strip() != TOOLCHAIN:
                raise ValueError("Mathlib's toolchain does not match the optional package.")
            source_files = sorted(p for p in PACKAGE.glob("*.lean") if p.name != "AxiomAudit.lean")
            names = declaration_inventory(source_files)
            audit = (PACKAGE / "AxiomAudit.lean").read_text()
            validate_audit(names, audit)
            controls = negative_controls(manifest, names, audit)
            inputs = source_files + [PACKAGE / name for name in ("AxiomAudit.lean", "lakefile.toml", "lean-toolchain", "lake-manifest.json", "README.md", ".gitignore")]
            inputs += sorted((FORMAL / "VolumeLogic").glob("*.lean"))
            inputs += [FORMAL / name for name in ("VolumeLogic.lean", "lakefile.toml", "lean-toolchain", "lake-manifest.json")]
            inputs.append(Path(__file__).resolve())
            hashes = {str(p.relative_to(ROOT)): sha256(p) for p in sorted(inputs)}
            version = checked_run([args.lake, "env", "lean", "--version"], PACKAGE).strip()
            if not re.search(r"Lean \(version 4\.32\.2(?:,|\))", version):
                raise ValueError("The executed Lean version does not match the pin: " + version)
            compiled = PACKAGE / ".lake/build/lib/lean/RealTransfer.olean"
            compiled.parent.mkdir(parents=True, exist_ok=True)
            commands = [(["build", "VolumeLogic"], "std-build.txt"),
                        (["env", "lean", "-o", ".lake/build/lib/lean/RealTransfer.olean", "RealTransfer.lean"], "bridge.txt"),
                        (["env", "lean", "AxiomAudit.lean"], "axioms.txt")]
            logs = {}
            for command, filename in commands:
                result = subprocess.run([args.lake, *command], cwd=PACKAGE, text=True,
                                        stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                logs[filename] = result.stdout
                (output / filename).write_text(result.stdout)
                if result.returncode or re.search(r"\b(?:warning|error)(?:\([^)]*\))?:", result.stdout):
                    raise ValueError(result.stdout + "\nLean did not compile without warnings.")
            axioms = parse_axioms(names, logs["axioms.txt"])
            if any(sha256(ROOT / path) != digest for path, digest in hashes.items()):
                raise ValueError("A recorded source changed during this replay; rerun on stable inputs.")
            report = {
                "scope": "Concrete complex modulus and real logarithmic level scale; equivalence with ordinary real convergence; unit phases, nonzero limiting amplitudes, finite complex actions and fixed real level powers; strict whole-remainder noncancellation and conditional 2*pi-scaled volume transfer.",
                "explicit_inputs_remaining": ["the actual invariant's exact finite source identity", "the nonzero packet coefficient and finite-action convergence", "a strict bound for the whole complementary remainder", "the actual geometric action-volume equality"],
                "toolchain": TOOLCHAIN,
                "dependency_pins": materialized,
                "local_dependency": {"name": "volumeLogic", "path": "../formal", "sources_copied": False},
                "commands": [["lake", *command] for command, _ in commands],
                "definitions": sorted(n for n, kind in names.items() if kind == "def"),
                "theorems": sorted(n for n, kind in names.items() if kind == "theorem"),
                "axioms": dict(sorted(axioms.items())),
                "negative_controls": controls,
                "source_sha256": hashes,
                "result": "All optional declarations compiled; every definition and theorem has only the permitted foundational axioms.",
            }
            (output / "summary.json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
        except (ValueError, OSError, KeyError) as error:
            raise SystemExit(str(error)) from error
        print(f"Checked {len(report['definitions'])} definitions and {len(report['theorems'])} concrete-limit theorems.")
        print(f"Validated all {len(EXPECTED_GIT)} Git dependency pins and {len(controls)} negative controls.")
        print("The exact source, uniform analytic estimates and geometric calibration remain explicit inputs.")
        if args.output:
            print(f"Report: {output / 'summary.json'}")


if __name__ == "__main__":
    main()
