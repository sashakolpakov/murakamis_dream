#!/usr/bin/env python3
"""Compile the formal statements selected by the current volume manuscripts.

The coverage file names the actual modules and their manuscript statements.
This runner checks that no other project modules remain, compiles the selected
code, and audits every public definition and theorem. It does not establish
the written analytic/geometric inputs or infer formal coverage from a hash.
Dependency downloads and mathematical experiments are not part of replay.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import tomllib

ROOT = Path(__file__).resolve().parents[1]
ALLOWED_AXIOMS = {"propext", "Classical.choice", "Quot.sound"}
TOOLCHAIN = "leanprover/lean4:v4.32.2"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def code_without_comments(text: str) -> str:
    """Strip nested Lean comments, preserving strings and line boundaries."""
    out = []
    i = depth = 0
    string = False
    while i < len(text):
        if depth:
            if text.startswith("/-", i):
                depth += 1; i += 2
            elif text.startswith("-/", i):
                depth -= 1; i += 2
                out.append(" ")
            else:
                if text[i] == "\n": out.append("\n")
                i += 1
        elif string:
            out.append(text[i])
            if text[i] == "\\" and i + 1 < len(text):
                i += 1; out.append(text[i])
            elif text[i] == '"':
                string = False
            i += 1
        elif text.startswith("/-", i):
            depth = 1; i += 2; out.append(" ")
        elif text.startswith("--", i):
            end = text.find("\n", i)
            i = len(text) if end < 0 else end
        else:
            if text[i] == '"': string = True
            out.append(text[i]); i += 1
    if depth or string:
        raise ValueError("Unclosed comment or string in a Lean source.")
    return "".join(out)


def declarations(path: Path, namespace: str) -> dict[str, str]:
    code = code_without_comments(path.read_text())
    if re.search(r"\b(?:sorry|admit|sorryAx|skipKernelTC)\b", code):
        raise ValueError(f"Proof placeholder or kernel bypass in {path}")
    if re.search(r"^\s*(?:@\[[^\n]*\]\s*)*(?:(?:private|protected|unsafe|noncomputable)\s+)*(?:axiom|opaque|constant|elab|initialize)\b", code, re.M):
        raise ValueError(f"Unchecked declaration/command in {path}")
    if re.findall(r"^namespace\s+(\S+)", code, re.M) != [namespace]:
        raise ValueError(f"Unexpected namespace layout in {path}")
    pattern = re.compile(
        r"^[ \t]*(?:@\[[^\n]*\][ \t]*)*(private[ \t]+)?"
        r"(?:noncomputable[ \t]+)?(def|abbrev|theorem|lemma)[ \t]+"
        r"(\w+(?:\.\w+)*)", re.M)
    result = {}
    for private, kind, name in pattern.findall(code):
        if private:
            continue
        full = namespace + "." + name
        if full in result:
            raise ValueError(f"Duplicate public declaration: {full}")
        result[full] = "theorem" if kind in {"theorem", "lemma"} else "definition"
    if not result:
        raise ValueError(f"Empty public module inventory: {path}")
    return result


def execute(command: list[str], cwd: Path, log: Path) -> str:
    env = dict(os.environ, LEAN_NUM_THREADS="2")
    run = subprocess.run(command, cwd=cwd, env=env, text=True,
                         stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    log.write_text(run.stdout)
    if run.returncode or re.search(r"\b(?:warning|error)(?:\([^)]*\))?:", run.stdout):
        raise ValueError(f"Compilation failed; see {log}\n" + run.stdout[-3500:])
    return run.stdout


def inventory_controls() -> list[str]:
    """Check concrete failures that compilation alone need not reject."""
    rejected = []
    with tempfile.TemporaryDirectory(prefix='volume-lean-inventory-') as tmp:
        path = Path(tmp) / 'InventoryControl.lean'
        good = 'namespace InventoryControl\n/- outer /- inner -/ -/\ndef witness : Nat := 0\nend InventoryControl\n'
        path.write_text(good)
        if declarations(path, 'InventoryControl') != {'InventoryControl.witness': 'definition'}:
            raise ValueError('Nested comments changed the public inventory.')
        for label, bad in [
            ('unused private axiom', 'private axiom hidden : False'),
            ('unused private opaque', 'private opaque hidden : Nat'),
            ('admitted proof', 'theorem hidden : False := by sorry'),
        ]:
            path.write_text('namespace InventoryControl\ndef witness : Nat := 0\n'+bad+'\nend InventoryControl\n')
            try:
                declarations(path, 'InventoryControl')
            except ValueError:
                rejected.append(label)
            else:
                raise ValueError('An invalid inventory control was accepted: '+label)
    return rejected



def correspondence_inputs(coverage: dict) -> tuple[dict, set[Path]]:
    """Validate the authored semantic map and its expected-type checks.

    The records explain the mathematical dictionary; Lean checks each
    independent contract type. Neither source anchors nor a relation's
    prose are treated as a proof that TeX has been formalized.
    """
    expected = {root: item['module']
                for project in coverage['projects'].values()
                for item in project['modules'] for root in item['roots']}
    local_imports = {item['module'] for project in coverage['projects'].values()
                     for item in project['modules']} | {'VolumeLogic'}
    records, contracts, inputs = {}, {}, set()
    for relative in coverage.get('correspondence', []):
        path = (ROOT / relative).resolve()
        if not path.is_relative_to(ROOT / 'formal/correspondence'):
            raise ValueError('Correspondence records must be in formal/correspondence/.')
        obj = json.loads(path.read_text())
        if obj.get('schema') != 1:
            raise ValueError(f'Unknown correspondence schema: {relative}')
        inputs.add(path)
        for entry in obj['contracts']:
            contract = (ROOT / entry['path']).resolve()
            project = coverage['projects'][entry['project']]
            directory = ROOT / project['directory']
            if not contract.is_relative_to(directory):
                raise ValueError(f'Contract outside its project: {contract}')
            name = str(contract.relative_to(directory))
            if name not in project['infrastructure']:
                raise ValueError(f'Unregistered statement contract: {contract}')
            if contract in contracts:
                raise ValueError(f'Duplicate statement contract: {contract}')
            text = contract.read_text()
            code = code_without_comments(text)
            if re.search(r'\b(?:sorry|admit|sorryAx|skipKernelTC|native_decide|ofReduceBool)\b', code):
                raise ValueError(f'Admitted statement contract: {contract}')
            for line in re.findall(r'^import\s+([^\n]+)', code, re.M):
                for imported in line.split():
                    if imported not in local_imports and not re.fullmatch(
                            r'(?:Mathlib|Std|Lean|Init)(?:\.\w+)*', imported):
                        raise ValueError(f'Unregistered contract import: {imported}')
            if re.search(r'^\s*(?:@\[[^\n]*\]\s*)*'
                         r'(?:(?:private|protected|unsafe|noncomputable|local)\s+)*'
                         r'(?:axiom|opaque|constant|elab|initialize|structure|inductive|'
                         r'class|def|abbrev|theorem|lemma|instance)\b', code, re.M):
                raise ValueError(f'Contracts must contain anonymous type checks, not declarations: {contract}')
            markers = re.findall(r'^\s*--\s*manuscript-contract:\s*(\S+)\s*$', text, re.M)
            if len(markers) != len(set(markers)) or set(markers) != set(entry['roots']):
                raise ValueError(f'Contract root markers differ from their record: {contract}')
            if not re.search(r'^\s*example\b', code, re.M):
                raise ValueError(f'No independent expected-type examples in {contract}')
            contracts[contract] = entry
            inputs.add(contract)
        for relation in obj['relations']:
            root = relation['root']
            if root not in expected or relation['module'] != expected[root] or root in records:
                raise ValueError(f'Duplicate or unregistered semantic proof root: {root}')
            if relation['kind'] not in {'exact', 'specialization', 'component', 'conditional'}:
                raise ValueError(f'Unknown logical relation: {root}')
            for field in ['symbol_dictionary', 'hypotheses', 'conclusion', 'unformalized', 'notes']:
                if field not in relation:
                    raise ValueError(f'Missing semantic field {field}: {root}')
            if not relation['symbol_dictionary'] or not relation['conclusion']:
                raise ValueError(f'Empty statement dictionary or conclusion: {root}')
            if relation['kind'] == 'exact' and relation['unformalized']:
                raise ValueError(f'An exact match cannot omit part of its statement: {root}')
            contract = (ROOT / relation['contract']).resolve()
            if contract not in contracts or root not in contracts[contract]['roots']:
                raise ValueError(f'No compiled expected-type contract for {root}')
            if not relation['manuscript']:
                raise ValueError(f'No written counterpart for {root}')
            for source in relation['manuscript']:
                manuscript = (ROOT / source['path']).resolve()
                if (not manuscript.is_relative_to(ROOT) or manuscript.suffix != '.tex'
                        or source['anchor'] not in manuscript.read_text()):
                    raise ValueError(f'Missing precise manuscript anchor: {source}')
                inputs.add(manuscript)
            records[root] = relation
    if set(records) != set(expected):
        raise ValueError('The semantic map must cover every selected proof root: '
                         + str(set(expected) ^ set(records)))
    return {'relations': records, 'contracts': contracts}, inputs


def contract_controls(lake: str, key: str, project: dict,
                      controls: list[dict], target: Path, output: Path) -> list[dict]:
    """Compile valid contracts and reject specified changes of their types."""
    directory = ROOT / project['directory']
    results = []
    for item in controls:
        if item['project'] != key:
            continue
        if (not re.fullmatch(r'[a-z0-9_-]+', item['id']) or not item['reason']
                or item['positive'] == item['negative']):
            raise ValueError('A signature control needs a name, reason and distinct types.')
        for source in [item['positive'], item['negative']]:
            code = code_without_comments(source)
            if re.search(r'\b(?:sorry|admit|sorryAx|skipKernelTC|native_decide|ofReduceBool)\b', code):
                raise ValueError('A signature control may not contain an admission or bypass.')
            if re.search(r'^\s*(?:(?:private|unsafe|noncomputable)\s+)*'
                         r'(?:axiom|opaque|constant|elab|initialize)\b', code, re.M):
                raise ValueError('An unchecked declaration entered a signature control.')
        with tempfile.TemporaryDirectory(prefix='statement-control-',
                                          dir=directory / '.lake/build') as temporary:
            temporary = Path(temporary)
            positive, negative = temporary / 'Positive.lean', temporary / 'Negative.lean'
            positive.write_text(item['positive'])
            negative.write_text(item['negative'])
            good_log = target / (item['id'] + '-positive.txt')
            bad_log = target / (item['id'] + '-negative.txt')
            execute([lake, 'env', 'lean', str(positive)], directory, good_log)
            run = subprocess.run([lake, 'env', 'lean', str(negative)], cwd=directory,
                                 env=dict(os.environ, LEAN_NUM_THREADS='2'), text=True,
                                 stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            bad_log.write_text(run.stdout)
            if not run.returncode or not re.search(item['expected_error'], run.stdout):
                raise ValueError('The intended type error was not detected: ' + item['id'])
        results.append({'id': item['id'], 'reason': item['reason'],
                        'positive_log': str(good_log.relative_to(output)),
                        'negative_log': str(bad_log.relative_to(output))})
    return results

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    output = args.output.resolve(); output.mkdir(parents=True, exist_ok=True)
    (output / "summary.json").unlink(missing_ok=True)
    lake = shutil.which("lake")
    if not lake:
        raise SystemExit("Lake is required; install the pinned toolchain.")
    coverage_file = ROOT / "formal/coverage.json"
    coverage = json.loads(coverage_file.read_text())
    dependencies = json.loads((ROOT / "formal/dependency-pins.json").read_text())
    projects = coverage["projects"]
    semantic, semantic_files = correspondence_inputs(coverage)
    type_control_path = ROOT / coverage['contract_controls']
    type_controls = json.loads(type_control_path.read_text())
    if type_controls.get('schema') != 1 or not type_controls.get('controls'):
        raise ValueError('Expected nonempty typed statement controls.')
    if len({c['id'] for c in type_controls['controls']}) != len(type_controls['controls']):
        raise ValueError('Duplicate statement controls.')
    controls = inventory_controls()
    inputs = {coverage_file, ROOT / "formal/dependency-pins.json", Path(__file__).resolve()}
    inputs |= semantic_files
    inputs.add(type_control_path)
    active_modules = {item['module'] for p in projects.values() for item in p['modules']}
    for project in projects.values():
        directory = ROOT / project['directory']
        inputs |= {directory / item['path'] for item in project['modules']}
        inputs |= {directory / name for name in project['infrastructure']}
        inputs |= {directory / name for name in ['lakefile.toml', 'lake-manifest.json', 'lean-toolchain']}
        inputs |= {ROOT / source['path'] for item in project['modules'] for source in item['manuscript']}
    source_pins = {str(p.relative_to(ROOT)): digest(p) for p in inputs}
    reports = {}
    # Only generated local artifacts are removed. Shared pinned packages are
    # left intact; imports can never be satisfied by a retired local .olean.
    for project in projects.values():
        build = ROOT / project['directory'] / '.lake/build'
        if build.is_symlink():
            raise ValueError(f'Refusing to clean a symlinked local build: {build}')
        if build.exists():
            shutil.rmtree(build)
    for key in ["std", "mathlib"]:
        project = projects[key]; directory = ROOT / project["directory"]
        target = output / key; target.mkdir(parents=True, exist_ok=True)
        if (directory / "lean-toolchain").read_text().strip() != TOOLCHAIN:
            raise ValueError(f"Wrong toolchain in {directory}")
        config = tomllib.loads((directory / 'lakefile.toml').read_text())
        configured = [x['name'] for x in config.get('lean_lib', [])]
        expected_targets = project['defaultTargets']
        if configured != expected_targets or config.get('defaultTargets') != expected_targets:
            raise ValueError(f'Lake targets differ from selected coverage: {directory}')
        expected_files = {directory / item["path"] for item in project["modules"]}
        actual_files = {p for p in directory.rglob("*.lean") if ".lake" not in p.parts}
        extra_files = {directory / name for name in project["infrastructure"]}
        if actual_files != expected_files | extra_files:
            raise ValueError(f"Active modules differ from coverage map: {actual_files ^ (expected_files | extra_files)}")
        if key == 'std':
            manifest = json.loads((directory / 'lake-manifest.json').read_text())
            if config.get('require', []) or manifest.get('packages', []):
                raise ValueError('The Std project must have no external packages.')
            umbrella = [line.strip() for line in code_without_comments((directory/'VolumeLogic.lean').read_text()).splitlines() if line.strip()]
            wanted = ['import '+item['module'] for item in project['modules']]
            if len(umbrella) != len(wanted) or set(umbrella) != set(wanted):
                raise ValueError('The Std aggregator must contain exactly the selected imports.')
        names = {}
        by_module = {}
        import_graph = {}
        for item in project["modules"]:
            path = directory / item["path"]
            imports = []
            for line in re.findall(r'^import\s+([^\n]+)', code_without_comments(path.read_text()), re.M):
                imports.extend(line.split())
            for imported in imports:
                if imported not in active_modules and not re.fullmatch(r'(?:Mathlib|Std|Lean|Init)(?:\.\w+)*', imported):
                    raise ValueError(f'Unregistered or retired local import in {path}: {imported}')
                if key == 'std' and (imported.startswith('Mathlib') or
                    imported in {x['module'] for x in projects['mathlib']['modules']}):
                    raise ValueError(f'The Std project cannot depend on Mathlib: {path}')
            import_graph[item['module']] = set(imports) & {x['module'] for x in project['modules']}
            for source in item["manuscript"]:
                text = (ROOT / source["path"]).read_text()
                if source["anchor"] not in text:
                    raise ValueError(f"Missing manuscript statement: {source}")
                inputs.add(ROOT / source["path"])
            current = declarations(path, item["namespace"])
            if names.keys() & current.keys():
                raise ValueError("A public declaration was inventoried twice.")
            if not item['roots']:
                raise ValueError(f'No manuscript-facing proof root selected in {path}')
            for root in item["roots"]:
                if root not in current:
                    raise ValueError(f"Missing selected proof root: {root}")
            names.update(current); by_module[item["module"]] = current
        audit = directory / "AxiomAudit.lean"
        wanted_audit = ["import " + item["module"] for item in project["modules"]]
        wanted_audit += ["", *["#print axioms " + name for name in names], ""]
        if audit.read_text() != "\n".join(wanted_audit):
            raise ValueError(f"Axiom audit differs from the full public inventory: {audit}")
        inputs |= expected_files | extra_files
        inputs |= {directory / n for n in ["lakefile.toml", "lake-manifest.json", "lean-toolchain"]}
        if key == "mathlib":
            manifest = json.loads((directory / "lake-manifest.json").read_text())
            packages = {p["name"]: p for p in manifest["packages"]}
            if len(packages) != len(manifest["packages"]) or set(packages) != set(dependencies) | {"volumeLogic"}:
                raise ValueError("Unexpected dependency set.")
            local = packages["volumeLogic"]
            if local.get("type") != "path" or local.get("dir") != "../formal":
                raise ValueError("The Std dependency must remain relative.")
            direct = {p['name']: p for p in config['require']}
            if len(config['require']) != 2 or direct != {'volumeLogic': {'name': 'volumeLogic', 'path': '../formal'},
                'mathlib': {'name': 'mathlib', 'git': dependencies['mathlib']['url'],
                            'rev': dependencies['mathlib']['rev']}}:
                raise ValueError('Direct dependency configuration changed.')
            for name, pin in dependencies.items():
                p = packages[name]
                if p.get("type") != "git" or (p.get("url"), p.get("rev")) != (pin["url"], pin["rev"]):
                    raise ValueError(f"Changed dependency pin: {name}")
                checkout = directory / manifest["packagesDir"] / name
                revision = execute(["git", "rev-parse", "HEAD"], checkout, target / (name + "-revision.txt")).strip()
                clean = execute(["git", "status", "--porcelain", "--untracked-files=no"], checkout, target / (name + "-tracked.txt")).strip()
                if revision != pin["rev"] or clean:
                    raise ValueError(f"Changed dependency checkout: {name}")
        for p in inputs:
            name, sha = str(p.relative_to(ROOT)), digest(p)
            if name in source_pins and source_pins[name] != sha:
                raise ValueError(f'An earlier project input changed: {name}')
            source_pins[name] = sha
        version = execute([lake, 'env', 'lean', '--version'], directory, target / 'version.txt')
        if not re.search(r'Lean \(version 4\.32\.2(?:,|\))', version):
            raise ValueError('Executed Lean does not match the toolchain pin.')
        if key == "std":
            execute([lake, "build"], directory, target / "build.txt")
        else:
            pending = {item['module']: item for item in project['modules']}
            done = set()
            while pending:
                ready = [name for name in pending if import_graph[name] <= done]
                if not ready:
                    raise ValueError('A cycle exists in the active local import graph.')
                name = ready[0]
                item = pending.pop(name)
                destination = directory / ".lake/build/lib/lean" / (item["module"] + ".olean")
                destination.parent.mkdir(parents=True, exist_ok=True)
                execute([lake, "env", "lean", "-o", str(destination), item["path"]],
                        directory, target / (item["module"] + ".txt"))
                done.add(name)
        # These examples state the expected mathematical types independently
        # of the theorem declaration being applied. A signature mismatch is a
        # kernel-checked type error, rather than a stale source-hash warning.
        contract_logs = []
        for contract, specification in semantic['contracts'].items():
            if specification['project'] != key:
                continue
            relative = str(contract.relative_to(directory))
            log_path = target / (contract.stem + '.txt')
            execute([lake, 'env', 'lean', relative], directory, log_path)
            contract_logs.append(str(log_path.relative_to(output)))
        rejected_types = contract_controls(lake, key, project, type_controls['controls'],
                                           target, output)
        log = execute([lake, "env", "lean", "AxiomAudit.lean"], directory, target / "axioms.txt")
        axioms = {}
        entries = re.findall(r"'([^']+)' depends on axioms:\s*\[([^\]]*)\]", log)
        entries += [(name, '') for name in re.findall(r"'([^']+)' does not depend on any axioms", log)]
        if len(entries) != len(names):
            raise ValueError('Missing or duplicated compiler axiom output.')
        for name, atoms in entries:
            axioms[name] = [a.strip() for a in atoms.split(",") if a.strip()]
        if set(axioms) != set(names):
            raise ValueError("Incomplete compiler axiom report.")
        if any(set(values) - ALLOWED_AXIOMS for values in axioms.values()):
            raise ValueError("An admitted proof or additional axiom entered the proof chain.")
        if any(digest(ROOT / name) != sha for name, sha in source_pins.items()):
            raise ValueError("An input changed during replay.")
        reports[key] = {"modules": list(by_module), "declarations": names, "axioms": axioms,
                        "statement_contracts": contract_logs,
                        "invalid_type_contracts_rejected": rejected_types}
        print(f"{key}: {len(by_module)} modules compiled; {len(names)} public declarations audited.", flush=True)
    for project in projects.values():
        directory = ROOT / project['directory']
        wanted = {directory / item['path'] for item in project['modules']}
        wanted |= {directory / name for name in project['infrastructure']}
        actual = {p for p in directory.rglob('*.lean') if '.lake' not in p.parts}
        if actual != wanted:
            raise ValueError('The active Lean source inventory changed during replay.')
    if any(digest(ROOT / name) != sha for name, sha in source_pins.items()):
        raise ValueError('An input changed before the combined replay completed.')
    result = {"scope": "Actual compilation and axiom checks of the retained manuscript-facing statements. Written analytic/geometric inputs remain those stated in the manuscripts.",
              "toolchain": TOOLCHAIN, "projects": reports, "inventory_controls_rejected": controls,
              "statement_correspondence": {
                  "scope": "Authored statement dictionaries and anonymous independently stated Lean type contracts; no automatic inference of TeX semantics.",
                  "selected_roots": len(semantic['relations']),
                  "relation_kinds": {kind: sum(r['kind'] == kind for r in semantic['relations'].values())
                                     for kind in ['exact', 'specialization', 'component', 'conditional']},
                  "contract_files": [str(p.relative_to(ROOT)) for p in semantic['contracts']],
              },
              "source_sha256": dict(sorted(source_pins.items()))}
    (output / "summary.json").write_text(json.dumps(result, indent=2) + "\n")


if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError) as error:
        raise SystemExit(str(error))
