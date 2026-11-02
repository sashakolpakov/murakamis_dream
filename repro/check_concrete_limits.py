#!/usr/bin/env python3
"""Check optional Mathlib transfer, variational estimates and triangle calculus.

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
MODULE_NAMESPACES = {
    "RealTransfer": "VolumeLogic.RealModel",
    "WeightedGraph": "VolumeLogic.WeightedGraph",
    "Flattening": "VolumeLogic.Flattening",
    "TransportCoercivity": "VolumeLogic.TransportCoercivity",
    "GroundedConvexity": "VolumeLogic.GroundedConvexity",
    "GroundedLaplacian": "VolumeLogic.GroundedLaplacian",
    "TriangleLoads": "VolumeLogic.TriangleLoads",
    "TrianglePotential": "VolumeLogic.TrianglePotential",
    "TriangleMinimizer": "VolumeLogic.TriangleMinimizer",
    "TriangleBalance": "VolumeLogic.TriangleBalance",
    "HallRecession": "VolumeLogic.HallRecession",
    "TriangleHall": "VolumeLogic.TriangleHall",
}
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


# Compiled counterexamples delimit mathematical strengthening, not just metadata.
BALANCE_BOUNDARY_CONTROLS = r'''
import TriangleBalance

open scoped BigOperators
open VolumeLogic
open TriangleBalance TriangleMinimizer TrianglePotential TriangleLoads
namespace VolumeLogic.TriangleBalanceControls

-- Wrong half-mass normalization is rejected by an actual supported row.
theorem half_mass : ¬ ((∑ v : Unit,
    vertexLoad (fun (_ : Unit) (_ : Fin 3) => ()) (fun _ => ![1,0,0])
      (fun _ => 0) v) = 1) := by
  have he := sum_vertexLoad (fun (_ : Unit) (_ : Fin 3) => ())
    (fun _ => ![1,0,0]) (fun _ => 0)
    (by intro t i; fin_cases i <;> norm_num)
    (by intro t; exact ⟨0, by norm_num⟩)
  norm_num at he
  simp only [Fintype.sum_unique]
  rw [he]
  norm_num

-- Repeated active destinations keep both corner loads, not one of them.
theorem repeated_destination : vertexLoad (fun (_ : Unit) (_ : Fin 3) => (1 : Fin 2))
    (fun _ => ![1,1,0]) (fun _ => 0) 1 = 1/2 := by
  have he := sum_vertexLoad (fun (_ : Unit) (_ : Fin 3) => (1 : Fin 2))
    (fun _ => ![1,1,0]) (fun _ => 0)
    (by intro t i; fin_cases i <;> norm_num)
    (by intro t; exact ⟨0, by norm_num⟩)
  simpa [Fin.sum_univ_two, vertexLoad, column, aggregate] using he

-- The one-vertex grounded problem has a minimum but no zero root residual
-- when the chosen root demand is zero.
theorem arbitrary_root :
    (∀ p : Unit → ℝ, p () = 0 →
      summedPotential (fun (_ : Unit) (_ : Fin 3) => ()) (fun _ => ![1,0,0])
        (fun _ => 0) (fun _ => 0) ≤
      summedPotential (fun (_ : Unit) (_ : Fin 3) => ()) (fun _ => ![1,0,0])
        (fun _ => 0) p) ∧
    residual (fun (_ : Unit) (_ : Fin 3) => ()) (fun _ => ![1,0,0])
      (fun _ => 0) (fun _ => 0) () ≠ 0 := by
  constructor
  · intro p hp
    have he : p = fun _ => (0 : ℝ) := by funext v; cases v; exact hp
    rw [he]
  · have he := root_residual (fun (_ : Unit) (_ : Fin 3) => ())
      (fun _ => ![1,0,0]) (fun _ => 0) (fun _ => 0)
      (by intro t i; fin_cases i <;> norm_num)
      (by intro t; exact ⟨0, by norm_num⟩) ()
      (by intro v hv; cases v; exact False.elim (hv rfl))
    norm_num at he
    rw [he]
    norm_num

-- Without connected support, a free unused vertex admits distinct solutions.
theorem disconnected_support : ∃ q p : Fin 2 → ℝ, q ≠ p ∧ q 0 = 0 ∧ p 0 = 0 ∧
    (∀ v, v ≠ 0 → vertexLoad (fun (_ : Unit) (_ : Fin 3) => (0 : Fin 2))
      (fun _ => ![1,0,0]) q v = 0) ∧
    (∀ v, v ≠ 0 → vertexLoad (fun (_ : Unit) (_ : Fin 3) => (0 : Fin 2))
      (fun _ => ![1,0,0]) p v = 0) := by
  refine ⟨![0,0], ![0,1], ?_, by norm_num, by norm_num, ?_, ?_⟩
  · intro he
    have hh := congrFun he 1
    norm_num at hh
  all_goals
    intro v hv
    fin_cases v
    · exact False.elim (hv rfl)
    · simp [vertexLoad, column, aggregate]

end VolumeLogic.TriangleBalanceControls
#print axioms VolumeLogic.TriangleBalanceControls.half_mass
#print axioms VolumeLogic.TriangleBalanceControls.repeated_destination
#print axioms VolumeLogic.TriangleBalanceControls.arbitrary_root
#print axioms VolumeLogic.TriangleBalanceControls.disconnected_support
'''

BALANCE_CONTROL_NAMES = ['half_mass', 'repeated_destination', 'arbitrary_root', 'disconnected_support']
HALL_CONTROL_SOURCE = ROOT / 'repro/lean/hall-controls.lean'
HALL_CONTROL_NAMES = ['strict_cut_balance', 'weak_cuts_no_balance', 'incompatible_total']

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
    if len(paths) != len(MODULE_NAMESPACES) or {p.name for p in paths} != {
        module + ".lean" for module in MODULE_NAMESPACES
    }:
        raise ValueError("Every registered optional module must be present exactly once.")
    result = {}
    pattern = re.compile(r"^\s*(?:noncomputable\s+)?(def|theorem)\s+(\w+)", re.M)
    unsupported = re.compile(r"^\s*(?:private\s+|protected\s+)?(?:lemma|instance|abbrev|opaque|axiom|structure|class|inductive|constant|example)\b", re.M)
    for path in paths:
        namespace = MODULE_NAMESPACES[path.stem]
        code = uncomment_lean(path.read_text())
        if re.search(r"\b(?:sorry|admit)\b", code) or unsupported.search(code):
            raise ValueError(f"Unsupported or unchecked declaration in {path.name}; extend the explicit inventory first.")
        if re.findall(r"^namespace\s+(\S+)", code, re.M) != [namespace]:
            raise ValueError(f"Unexpected namespace layout in {path.name}.")
        for kind, name in pattern.findall(code):
            full_name = namespace + "." + name
            if full_name in result:
                raise ValueError("Duplicate declaration: " + full_name)
            result[full_name] = kind
    if not result:
        raise ValueError("No concrete-limit declarations found.")
    return result


def validate_audit(names: dict[str, str], source: str) -> None:
    code = uncomment_lean(source)
    imports = re.findall(r"^import (\S+)$", code, re.M)
    if len(imports) != len(set(imports)) or set(imports) != set(MODULE_NAMESPACES):
        raise ValueError("AxiomAudit.lean must import every registered optional module exactly once.")
    inspected = re.findall(r"^#print axioms (\S+)$", code, re.M)
    if len(inspected) != len(set(inspected)) or sorted(inspected) != sorted(names):
        raise ValueError("AxiomAudit.lean must inspect every definition and theorem exactly once.")
    if any(line.strip() and line.strip() not in {"import " + m for m in MODULE_NAMESPACES} and
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
    reject("omitted_weighted_graph_module", declaration_inventory,
           [PACKAGE / (m + ".lean") for m in MODULE_NAMESPACES if m != "WeightedGraph"])
    graph_name = "VolumeLogic.WeightedGraph.grounded_energy_pos"
    if graph_name not in names:
        raise ValueError("The registered grounded-energy theorem is missing.")
    reject("omitted_grounded_energy_audit", validate_audit, names,
           audit.replace("#print axioms " + graph_name, ""))
    reject("omitted_flattening_module", declaration_inventory,
           [PACKAGE / (m + ".lean") for m in MODULE_NAMESPACES if m != "Flattening"])
    cost_name = "VolumeLogic.Flattening.stationary_quadratic_cost"
    if cost_name not in names:
        raise ValueError("The registered quadratic-cost theorem is missing.")
    reject("omitted_quadratic_cost_audit", validate_audit, names,
           audit.replace("#print axioms " + cost_name, ""))
    reject("omitted_transport_coercivity_module", declaration_inventory,
           [PACKAGE / (m + ".lean") for m in MODULE_NAMESPACES if m != "TransportCoercivity"])
    coercivity_name = "VolumeLogic.TransportCoercivity.grounded_recession_coercive"
    if coercivity_name not in names:
        raise ValueError("The registered transport-coercivity theorem is missing.")
    reject("omitted_grounded_coercivity_audit", validate_audit, names,
           audit.replace("#print axioms " + coercivity_name, ""))
    reject("omitted_grounded_convexity_module", declaration_inventory,
           [PACKAGE / (m + ".lean") for m in MODULE_NAMESPACES if m != "GroundedConvexity"])
    uniqueness_name = "VolumeLogic.GroundedConvexity.exists_unique_grounded_minimizer"
    if uniqueness_name not in names:
        raise ValueError("The registered unique grounded-minimum theorem is missing.")
    reject("omitted_unique_grounded_minimum_audit", validate_audit, names,
           audit.replace("#print axioms " + uniqueness_name, ""))
    reject("omitted_grounded_laplacian_module", declaration_inventory,
           [PACKAGE / (m + ".lean") for m in MODULE_NAMESPACES if m != "GroundedLaplacian"])
    inversion_name = "VolumeLogic.GroundedLaplacian.exists_unique_grounded_solution"
    if inversion_name not in names:
        raise ValueError("The registered grounded linear-equation theorem is missing.")
    reject("omitted_unique_grounded_solution_audit", validate_audit, names,
           audit.replace("#print axioms " + inversion_name, ""))
    reject("omitted_triangle_loads_module", declaration_inventory,
           [PACKAGE / (m + ".lean") for m in MODULE_NAMESPACES if m != "TriangleLoads"])
    loads_name = "VolumeLogic.TriangleLoads.sum_load_pairing_hasDerivAt"
    if loads_name not in names:
        raise ValueError("The registered shared triangle-load derivative theorem is missing.")
    reject("omitted_shared_triangle_derivative_audit", validate_audit, names,
           audit.replace("#print axioms " + loads_name, ""))
    reject("omitted_triangle_potential_module", declaration_inventory,
           [PACKAGE / (m + ".lean") for m in MODULE_NAMESPACES if m != "TrianglePotential"])
    potential_name = "VolumeLogic.TrianglePotential.potential_hasDerivAt"
    if potential_name not in names:
        raise ValueError("The registered actual supremum-gradient theorem is missing.")
    reject("omitted_supremum_gradient_audit", validate_audit, names,
           audit.replace("#print axioms " + potential_name, ""))
    reject("omitted_triangle_minimizer_module", declaration_inventory,
           [PACKAGE / (m + ".lean") for m in MODULE_NAMESPACES if m != "TriangleMinimizer"])
    minimum_name = "VolumeLogic.TriangleMinimizer.exists_unique_prescribed_minimizer"
    if minimum_name not in names:
        raise ValueError("The registered actual triangle-minimum theorem is missing.")
    reject("omitted_actual_triangle_minimum_audit", validate_audit, names,
           audit.replace("#print axioms " + minimum_name, ""))
    reject("omitted_triangle_balance_module", declaration_inventory,
           [PACKAGE / (m + ".lean") for m in MODULE_NAMESPACES if m != "TriangleBalance"])
    balance_name = "VolumeLogic.TriangleBalance.exists_unique_balance"
    if balance_name not in names:
        raise ValueError("The registered actual triangle-balance theorem is missing.")
    reject("omitted_actual_triangle_balance_audit", validate_audit, names,
           audit.replace("#print axioms " + balance_name, ""))
    for module, theorem in (("HallRecession", "grounded_coercive"),
                            ("TriangleHall", "exists_unique_balance")):
        reject("omitted_" + module + "_module", declaration_inventory,
               [PACKAGE / (m + ".lean") for m in MODULE_NAMESPACES if m != module])
        name = MODULE_NAMESPACES[module] + "." + theorem
        if name not in names:
            raise ValueError("Missing cut-inequality theorem: " + name)
        reject("omitted_" + module + "_theorem_audit", validate_audit, names,
               audit.replace("#print axioms " + name, ""))
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
            libraries = [item.get("name") for item in config.get("lean_lib", [])]
            targets = config.get("defaultTargets", [])
            if (len(libraries) != len(MODULE_NAMESPACES) or set(libraries) != set(MODULE_NAMESPACES)
                    or len(targets) != len(MODULE_NAMESPACES) or set(targets) != set(MODULE_NAMESPACES)):
                raise ValueError("Lake must register and build every optional module.")
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
            inputs = source_files + [HALL_CONTROL_SOURCE] + [PACKAGE / name for name in ("AxiomAudit.lean", "lakefile.toml", "lean-toolchain", "lake-manifest.json", "README.md", ".gitignore")]
            inputs += sorted((FORMAL / "VolumeLogic").glob("*.lean"))
            inputs += [FORMAL / name for name in ("VolumeLogic.lean", "lakefile.toml", "lean-toolchain", "lake-manifest.json")]
            inputs.append(Path(__file__).resolve())
            hashes = {str(p.relative_to(ROOT)): sha256(p) for p in sorted(inputs)}
            version = checked_run([args.lake, "env", "lean", "--version"], PACKAGE).strip()
            if not re.search(r"Lean \(version 4\.32\.2(?:,|\))", version):
                raise ValueError("The executed Lean version does not match the pin: " + version)
            (PACKAGE / ".lake/build/lib/lean").mkdir(parents=True, exist_ok=True)
            commands = [(["build", "VolumeLogic"], "std-build.txt")]
            commands += [(["env", "lean", "-o", f".lake/build/lib/lean/{module}.olean", module + ".lean"],
                          module + ".txt") for module in MODULE_NAMESPACES]
            commands += [(["env", "lean", "AxiomAudit.lean"], "axioms.txt")]
            logs = {}
            for command, filename in commands:
                result = subprocess.run([args.lake, *command], cwd=PACKAGE, text=True,
                                        stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                logs[filename] = result.stdout
                (output / filename).write_text(result.stdout)
                if result.returncode or re.search(r"\b(?:warning|error)(?:\([^)]*\))?:", result.stdout):
                    raise ValueError(result.stdout + "\nLean did not compile without warnings.")
            axioms = parse_axioms(names, logs["axioms.txt"])
            boundary_source = output / "triangle-balance-controls.lean"
            boundary_source.write_text(BALANCE_BOUNDARY_CONTROLS)
            boundary_run = subprocess.run([args.lake, "env", "lean", str(boundary_source)],
                cwd=PACKAGE, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            (output / "triangle-balance-controls.txt").write_text(boundary_run.stdout)
            if boundary_run.returncode or re.search(r"\b(?:warning|error)(?:\([^)]*\))?:", boundary_run.stdout):
                raise ValueError(boundary_run.stdout + "\nTriangle-balance boundary controls failed.")
            boundary_axioms = parse_axioms(
                {"VolumeLogic.TriangleBalanceControls." + n: "theorem" for n in BALANCE_CONTROL_NAMES},
                boundary_run.stdout)
            hall_source = output / "hall-controls.lean"
            hall_source.write_text(HALL_CONTROL_SOURCE.read_text())
            hall_run = subprocess.run([args.lake, "env", "lean", str(hall_source)],
                cwd=PACKAGE, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            (output / "hall-controls.txt").write_text(hall_run.stdout)
            if hall_run.returncode or re.search(r"\b(?:warning|error)(?:\([^)]*\))?:", hall_run.stdout):
                raise ValueError(hall_run.stdout + "\nHall boundary controls failed.")
            hall_axioms = parse_axioms(
                {"VolumeLogic.HallControls." + n: "theorem" for n in HALL_CONTROL_NAMES},
                hall_run.stdout)
            if any(sha256(ROOT / path) != digest for path, digest in hashes.items()):
                raise ValueError("A recorded source changed during this replay; rerun on stable inputs.")
            report = {
                "scope": "Concrete complex modulus and real logarithmic level scale; finite-residue packet assembly, whole-remainder noncancellation and conditional volume transfer; actual finite real weighted graph energy, positive-edge paths, constant kernel, grounded strict positivity and the explicit Laplacian quadratic identity; actual one-variable derivative bounds imply stationary quadratic cost, convex supporting-tangent gains and a strict two-branch sector margin; an actual positive finite corner table and connected co-occurrence paths give a uniform grounded max-minus-linear recession bound, coercivity of its vertex-bounded potential, compact sublevels and an attained minimum; actual segment derivatives with second derivative equal to connected graph energy imply strict convexity and uniqueness of that same grounded minimum; the actual reduced principal graph Laplacian has its constructed bilinear form, trivial kernel, nonzero determinant and a linear inverse, yielding a unique solution of every grounded linear equation; actual exponential triangle weights, square roots and arctangent loads have the proved directional conductance Jacobian, and their finite shared-vertex pairing is the explicit graph energy, including a zero corner; the literal Lobachevsky integral defines a continuous concave triangle entropy, the supported supremum is attained at the explicit arctangent loads, its actual affine-path first derivative is their pairing, and the actual shared-potential second derivative at every path point is the graph energy; the same supported supremum gives singleton affine rows, which are retained together with nonsingletons in a mixed-row shared-sum theorem; actual pure-corner lower bounds and fixed-support multivariate Lipschitz continuity, exact corner-table aggregation, and row-to-conductance paths give a unique grounded minimum of this explicit potential, including fixed boundary coefficients and physical demands matched only away from the root; the aggregate actual maximizing loads are the coordinate derivatives, grounded minimization is equivalent to all free-vertex load equations, and the explicit positive table and connected support yield a unique grounded balance solution; the unforced root residual is exactly the total mass discrepancy; strict finite cut inequalities and total half-mass compatibility now derive the grounded recession margin, connectivity, an actual minimum, a positive supported corner table and unique full load balance without assuming any table.",
                "explicit_inputs_remaining": ["the actual invariant's exact finite source identity", "the nonzero packet coefficient and finite-action convergence (a common limit, or a limit on every residue class with equal real action)", "a strict bound for the whole complementary remainder", "the actual geometric action-volume equality", "identification of the geometric/source potential with the proved supported entropy supremum and its incidence graph; application-specific nonnegative corner coefficients and identification of the actual supported incidence", "identification of the shared-weight path and its stationary point, directional second-derivative bound, additional entropy sign inequalities for the sector criterion, and the actual source envelopes", "verification of the finite strict cut inequalities and total half-mass compatibility for the actual geometric incidence and prescribed demands; transport-table feasibility and connectivity now follow from these cuts, and the triangle vertex bound and fixed-coefficient continuity are proved", "identification of the geometric potential with the finite shared sum and its fixed boundary corner coefficients; the explicit table gives nonempty support and the fixed row partition, and row paths give conductance connectivity; no support-changing minimizer limit or nonlinear geometric development is claimed"],
                "residue_assembly": {"period": "any fixed positive natural number", "denominator": "original level N, including on N=p*n+r", "amplitudes": "each residue limit is nonzero; the complex limits may differ", "actions": "the complex residue limits may differ; their real parts agree", "unit_character": "may depend arbitrarily on N and need not converge", "conclusion": "ordinary all-integer-level convergence and eventual nonvanishing"},
                "toolchain": TOOLCHAIN,
                "dependency_pins": materialized,
                "local_dependency": {"name": "volumeLogic", "path": "../formal", "sources_copied": False},
                "commands": [["lake", *command] for command, _ in commands],
                "modules": {module: {"namespace": namespace,
                    "definitions": sum(kind == "def" and name.startswith(namespace + ".") for name, kind in names.items()),
                    "theorems": sum(kind == "theorem" and name.startswith(namespace + ".") for name, kind in names.items())}
                    for module, namespace in MODULE_NAMESPACES.items()},
                "definitions": sorted(n for n, kind in names.items() if kind == "def"),
                "theorems": sorted(n for n, kind in names.items() if kind == "theorem"),
                "axioms": dict(sorted(axioms.items())),
                "negative_controls": controls,
                "mathematical_boundary_controls": {
                    "cases": BALANCE_CONTROL_NAMES,
                    "source": "triangle-balance-controls.lean",
                    "source_sha256": sha256(boundary_source),
                    "axioms": boundary_axioms,
                    "scope": "Compiled exact checks of half mass, repeated incidence, arbitrary grounded root demand, and nonuniqueness without connected support.",
                },
                "source_sha256": hashes,
                "hall_boundary_controls": {
                    "cases": HALL_CONTROL_NAMES,
                    "source": "hall-controls.lean",
                    "source_sha256": sha256(hall_source),
                    "axioms": hall_axioms,
                    "scope": "An actual strict-cut balance with a zero corner and repeated destinations; weak cuts with unattainable finite-height boundary demand; strict proper cuts without total compatibility.",
                },
                "result": "All optional declarations compiled; every definition and theorem has only the permitted foundational axioms.",
            }
            (output / "summary.json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
        except (ValueError, OSError, KeyError) as error:
            raise SystemExit(str(error)) from error
        print(f"Checked {len(report['definitions'])} definitions and {len(report['theorems'])} optional concrete theorems.")
        print(f"Validated all {len(EXPECTED_GIT)} Git dependency pins and {len(controls)} negative controls.")
        print("The exact source, uniform analytic estimates and geometric calibration remain explicit inputs.")
        print("The supported entropy supremum gradient is proved; geometric/source identification and flattening application remain written inputs.")
        print("Strict finite cuts and total mass now imply transport feasibility, connectivity and unique actual balance; checking those cuts for the geometric incidence remains written.")
        print("Actual integral entropy, supported maximization, its gradient and shared-potential second derivatives are proved; packing and source identification remain written.")
        print("Actual grounded load balance and unique solution are proved; the root equation additionally requires total demand compatibility.")
        print("Grounded finite graph inversion is proved; geometric Hessian identification, quantitative inverse bounds and nonlinear deformation remain outside this theorem.")
        if args.output:
            print(f"Report: {output / 'summary.json'}")


if __name__ == "__main__":
    main()
