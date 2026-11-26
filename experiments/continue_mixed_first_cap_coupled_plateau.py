#!/usr/bin/env python3
"""Preserve four first-cap stages and add necessary coupled exclusions only."""
import argparse
import copy
import gzip
import json
from pathlib import Path
import signal
import time

from flint import acb, arb, ctx
import certify_mixed_first_cap_plateau as stage1
import certify_mixed_first_cap_actual_plateau as stage2
import certify_mixed_first_cap_typed_plateau as stage3
import certify_mixed_first_cap_oriented_plateau as base
import mixed_endpoint_inverse_filter as coupling

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT/'notes/research_mixed_first_cap_coupled_plateau_certificate.md'
SEED_NAME = 'repro/results/research-mixed-first-cap-oriented-plateau-attempt01.json'
SEED_SHA = 'fb21ee2dc6ec496b1b890fd8d26cc471da9d845075565b05179d1abf7086e507'
BASE_PROOF = 'notes/research_mixed_first_cap_oriented_plateau_certificate.md'
BASE_PROOF_SHA = 'f0dfa839d839b05dd7deea535bae40f5cfee65b3500d4ef785085e0d4ae34178'
BASE_SCRIPT = 'experiments/certify_mixed_first_cap_oriented_plateau.py'
BASE_SCRIPT_SHA = 'c7a04d02202896bb7ffb8af94e0c7d8e59182e1ff6bb3d5c6e1c772a673698fa'
FILTER_NAME = 'experiments/mixed_endpoint_inverse_filter.py'
FILTER_SHA = '62cfcc5a35182d2356a12da6df8a59d1761ecce1ba4453bbcdb048d4070f46b5'
FILTER_PROOF = 'notes/research_mixed_endpoint_inverse_filter.md'
FILTER_PROOF_SHA = '20a73200b9180b0e69a3307e338a4b841c3a9ff6c583ce63b23d2426859c83da'
MODULES = [stage1, stage2, stage3, base, base]
RULES = ['original_full_disk_v1', 'lower_height_v1', 'typed_disk_v1',
         'adjacent_four_v1', 'coupled_actual_v1']
M2_REASONS = {'attached_real_floor', 'attached_fixed_point'}
M3_REASONS = {'opposite_half_plane', 'external_half_plane',
              'opposite_outside_P4', 'external_outside_both_P'}


def prefix_tree(record, job):
    if job < len(record['completed']):
        return record['completed'][job]
    active = record['active']
    if active is not None and active['job'] == job:
        return active['tree']
    return []


def assert_extends(record, previous):
    assert len(record['completed']) >= len(previous['completed'])
    assert record['completed'][:len(previous['completed'])] == previous['completed']
    if previous['active'] is not None:
        j, before = previous['active']['job'], previous['active']['tree']
        after = prefix_tree(record, j)
        assert after[:len(before)] == before
        assert j < len(record['completed']) or record['active'] is not None


def filter_witness_shape(witness):
    assert isinstance(witness, dict) and set(witness) == {'m2', 'm3'}
    assert witness['m2'] in M2_REASONS and witness['m3'] in M3_REASONS


def geometric_node(box, cell):
    if base.old.excluded(box):
        return ['X']
    if base.height_excluded(box, cell['neighbor']):
        return ['H']
    if base.radial_excluded(box, cell['neighbor']):
        return ['R']
    if base.upper_height_excluded(box, cell['neighbor']):
        return ['U']
    if base.adjacent_four_excluded(box, cell['own'], cell['neighbor']):
        return ['A']
    return None


def filter_box(cell, context, box):
    assert (cell['own'], cell['neighbor']) == (1, 1)
    b = base.old.parameter(box, 1)
    root = base.enclosing_root(context, b, 12)
    return coupling.evaluate(b, root[1])


def frontier(cell, tree, face, job, seeds, replay_leaf=None, replay_filter=None):
    prefixes = [prefix_tree(seed, job) for seed in seeds]
    for previous, later in zip(prefixes, prefixes[1:]):
        assert later[:len(previous)] == previous
    assert tree[:len(prefixes[-1])] == prefixes[-1]
    pending = [(cell['box'], 0)]
    counts = dict(leaves_by_tier=[0]*5, exclusions={key: 0 for key in 'XHRUAF'}, nodes=len(tree))
    for index, node in enumerate(tree):
        assert pending
        box, depth = pending.pop()
        tier = next((j for j, old in enumerate(prefixes) if index < len(old)), 4)
        kind = node[0]
        allowed = ({'S', 'X', 'L'}, {'S', 'X', 'H', 'L'},
                   {'S', 'X', 'H', 'R', 'U', 'L'},
                   {'S', 'X', 'H', 'R', 'U', 'A', 'L'},
                   {'S', 'X', 'H', 'R', 'U', 'A', 'F', 'L'})[tier]
        assert kind in allowed
        if kind == 'S':
            assert len(node) == 2 and node[1] in (0, 1)
            left, right = base.old.split(box, node[1])
            pending.extend([(left, depth+1), (right, depth+1)])
        elif kind == 'L':
            assert len(node) == 2 and not base.old.excluded(box)
            MODULES[tier].validate_trial(node[1], face)
            if replay_leaf is not None:
                replay_leaf(box, node[1], tier)
            counts['leaves_by_tier'][tier] += 1
        elif kind == 'F':
            assert tier == 4 and len(node) == 2
            assert (cell['own'], cell['neighbor']) == (1, 1)
            assert geometric_node(box, cell) is None
            filter_witness_shape(node[1])
            if replay_filter is not None:
                replay_filter(box, node[1])
            counts['exclusions']['F'] += 1
        else:
            assert len(node) == 1 and geometric_node(box, cell) == node
            counts['exclusions'][kind] += 1
    return pending, counts


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--precision', type=int, default=256)
    parser.add_argument('--input', type=Path)
    parser.add_argument('--resume', type=Path)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--max-nodes', type=int, default=600000)
    parser.add_argument('--max-seconds', type=float, default=600)
    parser.add_argument('--max-depth', type=int, default=30)
    args = parser.parse_args()
    assert args.precision >= 192 and not (args.input and args.resume)
    assert not args.output.exists(), 'output must be a fresh immutable path'
    assert 0 < args.max_nodes <= 600000 and 0 < args.max_seconds <= 600
    assert 0 <= args.max_depth <= 45
    source_path = args.input or args.resume
    assert all(args.output.resolve() != p.resolve()
               for p in [ROOT/SEED_NAME]+([source_path] if source_path else []))
    ctx.prec = args.precision
    pi, ii = arb.pi(), acb(0, 1)
    for module in MODULES:
        module.PI, module.II = pi, ii
        module.primitive.PI, module.primitive.II = pi, ii
        module.old.propose = base.original_root_proposals_forbidden
        if args.input:
            module.propose_targets = base.target_proposals_forbidden
    assert base.ar('3.14')/200-2*base.ar(base.KAPPA) > base.ar(base.MU)
    proof_hash, script_hash = base.sha(PROOF), base.sha(__file__)
    dependencies, records = {}, {}

    def bind(name, expected=None):
        digest = base.sha(ROOT/name)
        if expected is not None:
            assert digest == expected, name
        assert name not in dependencies or dependencies[name] == digest
        dependencies[name] = digest
        return digest

    def inherit(name):
        bind(name)
        if name in records:
            return records[name]
        record = json.loads((ROOT/name).read_text())
        records[name] = record
        for key in ('dependencies_sha256', 'dependencies'):
            for path, digest in record.get(key, {}).items():
                bind(path, digest)
                if path.startswith('repro/results/') and path.endswith('.json'):
                    inherit(path)
        return record

    bind(SEED_NAME, SEED_SHA)
    bind(BASE_PROOF, BASE_PROOF_SHA)
    bind(BASE_SCRIPT, BASE_SCRIPT_SHA)
    seed = inherit(SEED_NAME)
    assert seed['format_version'] == 4 and seed['status'] == 'incomplete'
    assert seed['fatal_error'] is None and seed['final_bindings_verified']
    assert seed['proof_sha256'] == BASE_PROOF_SHA and seed['script_sha256'] == BASE_SCRIPT_SHA
    assert seed['reference_domains'] == base.domain_metadata()
    assert seed['gap'] == str(base.GAP) and seed['target_curvature'] == str(base.MU)
    assert seed['families'] == base.family_metadata() and seed['job_count'] == 21032
    assert len(seed['completed']) == 19996 and seed['active']['job'] == 19996
    assert len(seed['active']['tree']) == 306 and len(seed['active']['pending']) == 9
    assert sum(map(len, seed['completed']))+len(seed['active']['tree']) == 24564
    seeds, provenance = [], []
    for j in range(1, 4):
        meta = seed[f'stage{j}_provenance']
        bind(meta['record'], meta['record_sha256'])
        bind(meta['proof'], meta['proof_sha256'])
        bind(meta['script'], meta['script_sha256'])
        record = inherit(meta['record'])
        assert record['status'] == 'incomplete' and record['fatal_error'] is None
        assert record['proof_sha256'] == meta['proof_sha256']
        assert record['script_sha256'] == meta['script_sha256']
        assert len(record['completed']) == meta['completed_jobs']
        assert record['active']['job'] == meta['active_job']
        assert len(record['active']['tree']) == meta['active_tree_nodes']
        assert len(record['active']['pending']) == meta['pending_boxes']
        assert record['gap'] == str(MODULES[j-1].GAP)
        assert record['target_curvature'] == str(MODULES[j-1].MU)
        assert record['families'] == base.family_metadata()
        seeds.append(record)
        provenance.append(meta)
    seeds.append(seed)
    provenance.append(dict(record=SEED_NAME, record_sha256=SEED_SHA,
                           proof=BASE_PROOF, proof_sha256=BASE_PROOF_SHA,
                           script=BASE_SCRIPT, script_sha256=BASE_SCRIPT_SHA,
                           gap=str(base.GAP), completed_jobs=19996,
                           active_job=19996, active_tree_nodes=306, pending_boxes=9))
    for before, after in zip(seeds, seeds[1:]):
        assert_extends(after, before)
    bind(FILTER_NAME, FILTER_SHA)
    bind(FILTER_PROOF, FILTER_PROOF_SHA)
    bind('notes/research_terminal_coupling_barriers.md')
    bind('notes/research_mixed_open_local_factor_coverage.md')
    roots, root_replay = inherit(base.ROOT_AUTHOR), inherit(base.ROOT_REPLAY)
    assert roots['status'] == root_replay['status'] == 'passed'
    assert root_replay['input_sha256'] == dependencies[base.ROOT_AUTHOR]
    assert roots['domains'] == root_replay['domains']
    # Recheck the two exact geometry facts independently of cap source status.
    bind(base.IMAGE_RECORD, base.IMAGE_HASH)
    images = json.loads(gzip.decompress((ROOT/base.IMAGE_RECORD).read_bytes()))
    image_author_name = 'repro/results/research-mixed-cyclic-block-localization.json'
    image_replay_name = 'repro/results/research-mixed-cyclic-block-localization-replay.json'
    image_author, image_replay = inherit(image_author_name), inherit(image_replay_name)
    assert image_author['status'] == image_replay['status'] == 'passed'
    assert image_replay['input_sha256'] == dependencies[image_author_name]
    bind(image_author_name, images['author_record_sha256'])
    bind('experiments/certify_mixed_cyclic_block_localization.py', images['source_sha256'])
    bind('experiments/extract_mixed_cyclic_block_images.py', images['script_sha256'])
    bind('notes/research_mixed_cyclic_critical_localization.md', images['proof_sha256'])
    oriented = base.oriented_real_floor(images, image_author)
    attached = base.attached_four_four_floor(roots)
    assert oriented == seed['oriented_input_extraction']
    assert attached == seed['attached_four_four_extraction']
    cells = base.original_cells(roots)
    jobs = [(ci, fi) for ci in range(len(cells)) for fi in range(len(base.FACES))]
    assert len(cells) == 5258 and len(jobs) == 21032
    domain = dict(base.domain_metadata(), coupled_own_four_neighbor_four=True,
                  coupled_scope='union of m2 attached fixed points and m>=3 adjacent ordinary feasible set',
                  necessary_only=True)
    source_hash = base.sha(source_path) if source_path else None
    saved = json.loads(source_path.read_text()) if source_path else None
    if saved:
        assert saved['format_version'] == 5
        assert saved['proof_sha256'] == proof_hash and saved['script_sha256'] == script_hash
        assert saved['dependencies_sha256'] == dependencies
        assert saved['seed_sha256'] == SEED_SHA and saved['stage_provenance'] == provenance
        assert saved['acceptance_rules'] == RULES and saved['reference_domains'] == domain
        assert saved['oriented_input_extraction'] == oriented and saved['attached_four_four_extraction'] == attached
        assert saved['gap'] == str(base.GAP) and saved['target_curvature'] == str(base.MU)
        assert saved['families'] == base.family_metadata() and saved['job_count'] == len(jobs)
        assert saved['status'] == ('passed' if args.input else 'incomplete')
        assert_extends(saved, seed)
    initial = saved or seed
    completed, active = copy.deepcopy(initial['completed']), copy.deepcopy(initial['active'])
    if active is not None:
        active.pop('failure', None)

    def validate_partition():
        assert len(completed) <= len(jobs)
        for ji, tree in enumerate(completed):
            ci, fi = jobs[ji]
            pending, _ = frontier(cells[ci], tree, base.FACES[fi], ji, seeds)
            assert not pending
        if active is not None:
            assert active['job'] == len(completed) < len(jobs)
            ci, fi = jobs[active['job']]
            pending, _ = frontier(cells[ci], active['tree'], base.FACES[fi], active['job'], seeds)
            assert pending and base.serialize_pending(pending) == active['pending']
        assert_extends(dict(completed=completed, active=active), initial)

    validate_partition()
    contexts = {}
    root_checks = proposals = refinements = attempted = nodes = filter_checks = 0
    fatal_error = None

    def context(ci, tier=3):
        nonlocal root_checks
        key = (ci, min(tier, 3))
        if key not in contexts:
            contexts[key] = MODULES[key[1]].root_context(cells[ci])
            root_checks += 1
        return contexts[key]

    def validate_bindings():
        assert base.sha(PROOF) == proof_hash and base.sha(__file__) == script_hash
        assert all(base.sha(ROOT/name) == digest for name, digest in dependencies.items())
        if source_path:
            assert base.sha(source_path) == source_hash

    def result(status, reason, summaries):
        return dict(format_version=5, status=status, stop_reason=reason,
                    precision_bits=args.precision, proof_sha256=proof_hash, script_sha256=script_hash,
                    dependencies_sha256=dependencies, seed_sha256=SEED_SHA,
                    stage_provenance=provenance, acceptance_rules=RULES,
                    input_sha256=source_hash if args.input else None,
                    resume_sha256=source_hash if args.resume else None,
                    reference_domains=domain, gap=str(base.GAP), target_curvature=str(base.MU),
                    oriented_input_extraction=oriented, attached_four_four_extraction=attached,
                    original_endpoint_cells=5258, face_families_per_cell=4,
                    families=base.family_metadata(), own_types=[0, 1], one_vertex_included=False,
                    job_count=len(jobs), completed=completed, active=active,
                    additional_nodes=nodes, attempted_nodes=attempted,
                    revalidated_original_root_contexts=root_checks,
                    root_proposals=0, target_proposals=proposals, refinements=refinements,
                    coupled_filter_checks=filter_checks, fatal_error=fatal_error,
                    attempt_limits=None if args.input else dict(additional_nodes=args.max_nodes,
                        seconds=args.max_seconds, depth_from_inherited_cell=args.max_depth),
                    replay_summaries=summaries, final_bindings_verified=True,
                    scope='All four cap comparisons on the prior geometric domains with necessary '
                          'coupled exclusions only for own4/input4. Actual m>=2 inputs retained; '
                          'no comparison asserted at discarded auxiliary points. Complete author '
                          'and saved replay required; all prior arithmetic tiers retained.')

    if args.input:
        assert active is None and len(completed) == len(jobs)
        summaries, checked, filtered = [], 0, 0
        for ji, tree in enumerate(completed):
            ci, fi = jobs[ji]
            maximum = None

            def replay_leaf(box, targets, tier):
                nonlocal checked, maximum
                module = MODULES[tier]
                passed, trial, info, _ = module.check_face(cells[ci], context(ci, tier), box, base.FACES[fi], targets)
                assert passed and trial == targets, (ji, tier, box, info)
                checked += 1
                upper = arb(info['upper']).upper()
                maximum = upper if maximum is None else max(maximum, upper)

            def replay_filter(box, witness):
                nonlocal filtered, filter_checks
                evidence = filter_box(cells[ci], context(ci), box)
                coupling.validate_witness(witness, evidence)
                filtered += 1
                filter_checks += 1

            pending, counts = frontier(cells[ci], tree, base.FACES[fi], ji, seeds, replay_leaf, replay_filter)
            assert not pending
            summaries.append(dict(job=ji, **counts, maximum_upper=None if maximum is None else str(maximum)))
            if ji % 128 == 0:
                print('REPLAY', ji, '/', len(jobs), 'leaves', checked, 'coupled exclusions', filtered, flush=True)
        assert attempted == nodes == proposals == refinements == 0
        validate_bindings()
        validate_partition()
        base.write_atomic(args.output, result('passed', 'all source tiers and coupled exclusions replayed', summaries))
        print('PASS', len(jobs), 'jobs', checked, 'leaves', filtered, 'coupled exclusions', flush=True)
        return 0

    start = checkpoint = time.monotonic()
    reason = 'all actual coupled cap comparisons verified'
    signal.signal(signal.SIGALRM, base.alarm_handler)
    signal.setitimer(signal.ITIMER_REAL, args.max_seconds)
    try:
        while len(completed) < len(jobs):
            if nodes >= args.max_nodes or time.monotonic()-start >= args.max_seconds:
                raise base.BudgetStop('author additional-node/time cap')
            ji = len(completed)
            ci, fi = jobs[ji]
            if active is None:
                with base.atomic_state():
                    active = dict(job=ji, tree=[], pending=base.serialize_pending([(cells[ci]['box'], 0)]))
            box_strings, depth = active['pending'][-1]
            box = base.decode_box(box_strings)
            attempted += 1
            new_node = geometric_node(box, cells[ci])
            replacement = []
            if new_node is None and (cells[ci]['own'], cells[ci]['neighbor']) == (1, 1):
                evidence = filter_box(cells[ci], context(ci), box)
                filter_checks += 1
                if evidence['excluded']:
                    new_node = ['F', coupling.witness(evidence)]
            if new_node is None:
                passed, trial, info, axis = base.check_face(cells[ci], context(ci), box, base.FACES[fi])
                proposals += 1
                if passed:
                    new_node = ['L', trial]
                elif depth >= args.max_depth:
                    reason = 'maximum depth; unresolved coupled cap face'
                    active['failure'] = dict(box=box_strings, targets=trial, bounds=info)
                    break
                else:
                    left, right = base.old.split(box, axis)
                    new_node = ['S', axis]
                    replacement = base.serialize_pending([(left, depth+1), (right, depth+1)])
            with base.atomic_state():
                active['pending'].pop()
                active['tree'].append(new_node)
                active['pending'].extend(replacement)
                nodes += 1
                refinements += int(new_node[0] == 'S')
                if not active['pending']:
                    completed.append(active['tree'])
                    active = None
            if time.monotonic()-checkpoint >= 10:
                validate_bindings()
                validate_partition()
                base.write_atomic(args.output, result('incomplete', 'atomic checkpoint', []))
                print('CHECKPOINT', len(completed), '/', len(jobs), 'additional nodes', nodes, flush=True)
                checkpoint = time.monotonic()
    except base.BudgetStop as exc:
        reason = str(exc)
    except Exception as exc:
        fatal_error = dict(type=type(exc).__name__, message=str(exc))
        reason = 'unresolved arithmetic/inherited-input failure'
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
    validate_bindings()
    validate_partition()
    status = 'passed' if len(completed) == len(jobs) and active is None else 'incomplete'
    base.write_atomic(args.output, result(status, reason, []))
    print(status.upper(), len(completed), '/', len(jobs), 'additional nodes', nodes,
          'seconds', time.monotonic()-start, flush=True)
    return 0 if status == 'passed' else 3 if fatal_error else 2


if __name__ == '__main__':
    raise SystemExit(main())
