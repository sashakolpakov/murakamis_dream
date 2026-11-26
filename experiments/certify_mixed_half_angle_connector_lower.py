#!/usr/bin/env python3
"""Half-angle connector reserve on the complete original five-window cover.

The saved old addresses are starting subdivisions only. Every root, phase,
response and new inequality is reevaluated; old gap values are not used.
"""
import argparse
import hashlib
import importlib.util
import itertools
import json
import time
from fractions import Fraction as F
from pathlib import Path

from flint import acb, arb

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / 'notes/research_mixed_half_angle_connector_lower.md'
HELPER = ROOT / 'experiments/certify_mixed_hybrid_zero_pair_support.py'
HELPER_SHA = hashlib.sha256(HELPER.read_bytes()).hexdigest()
spec = importlib.util.spec_from_file_location('half_angle_frozen_window', HELPER)
h = importlib.util.module_from_spec(spec)
spec.loader.exec_module(h)
assert HELPER_SHA == hashlib.sha256(HELPER.read_bytes()).hexdigest()
p, ar = h.p, h.ar
CEILINGS = (F(291561, 10**6), F(443534, 10**6))
COLLAR = F(1, 50)
RESERVE = F(1, 20)
OLD_RECORD = 'repro/results/research-mixed-hybrid-zero-pair-support.json'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def validate_cover(addresses):
    codes = sorted(addresses)
    assert codes and len(codes) == len(set(codes))
    assert all(set(code) <= {'0', '1'} for code in codes)
    assert all(not b.startswith(a) for a, b in zip(codes, codes[1:]))
    assert sum((F(1, 2**len(code)) for code in codes), F(0)) == 1
    return codes


def validate_inputs():
    dependencies, visited, primary = {}, set(), {}

    def bind(path, expected=None):
        if path not in dependencies:
            dependencies[path] = sha(ROOT / path)
        if expected is not None:
            assert dependencies[path] == expected, path
        return dependencies[path]

    def inherit(path):
        data = (ROOT / path).read_bytes()
        bind(path, hashlib.sha256(data).hexdigest())
        record = json.loads(data)
        if path in visited:
            return record
        visited.add(path)
        bindings = {}
        for field in ('dependencies', 'dependencies_sha256'):
            for name, digest in record.get(field, {}).items():
                if name in bindings:
                    assert bindings[name] == digest, (path, name)
                bindings[name] = digest
                bind(name, digest)
        for name in bindings:
            if name.startswith('repro/results/') and name.endswith('.json'):
                inherit(name)
        return record

    for stem, prefix in (
            ('mixed_hybrid_zero_pair_support', 'certify'),
            ('mixed_half_angle_seam_source', 'check'),
            ('mixed_oriented_height_reset', 'certify')):
        pp = f'notes/research_{stem}.md'
        ss = f'experiments/{prefix}_{stem}.py'
        rp = f'repro/results/research-{stem.replace("_", "-")}.json'
        rec = inherit(rp)
        assert rec['status'] == 'passed', rp
        assert rec['proof_sha256'] == bind(pp), rp
        assert rec['script_sha256'] == bind(ss), rp
        primary[stem] = rec
    for name in (
            'experiments/certify_mixed_paired_right_transition_support.py',
            'experiments/certify_mixed_cyclic_window_heights.py',
            'experiments/certify_mixed_real_small_support.py'):
        bind(name)
    assert bind(str(HELPER.relative_to(ROOT))) == HELPER_SHA
    old = primary['mixed_hybrid_zero_pair_support']
    assert old['boundary_products'] == 2048 and old['accepted_cells'] == 18988
    half = primary['mixed_half_angle_seam_source']
    assert half['exact_checks'] == 23
    for typ in (0, 1):
        assert arb(half['scalar_values'][f'constant_type{typ}']) < ar(CEILINGS[typ])
    assert arb(half['scalar_values']['maximum_collar_cost']) < ar(COLLAR)
    reset = primary['mixed_oriented_height_reset']
    assert list(map(F, reset['integrated_one_height_costs'])) == [F(11, 2), F(151, 20)]
    return dependencies, primary


def test(case, bounds):
    word, ta, tb, fa, fb = case
    p.faces[:] = [fa, fb]
    window = p.cert(word, ta, tb, bounds, -F(3, 25))
    if not window:
        return None, 'reference root'
    z = [window['boxes'][j] for j in (3, 5, 7)]
    response = p.response(window)
    if response is None:
        return None, 'reference response'
    whole = p.pair(z, word, window['boxes'][4], window['boxes'][6])
    mid = [(bounds[k]+bounds[k+1])/2 for k in (0, 2)]
    point = p.cert(word, ta, tb, [mid[0], mid[0], mid[1], mid[1]], -F(3, 25))
    if not point:
        return None, 'midpoint root'
    z0 = [point['boxes'][j] for j in (3, 5, 7)]
    central = p.pair(z0, word, point['boxes'][4], point['boxes'][6])
    half = acb(ar('1/2'))
    gap = (central[0]+central[1][0]*(half-z0[0])
           +central[1][2]*(half-z0[2])).real
    gap -= ar(CEILINGS[word[2]]+CEILINGS[word[3]]+COLLAR)
    gap -= ar('11/2')*(ar('1/2')-z0[0].real)**2
    gap -= ar('151/20')*(ar('1/2')-z0[2].real)**2
    for ell in range(2):
        xl, xh, yl, yh = map(F, p.RECTS[(ta, tb)[ell]])
        velocity = (acb(ar(xh-xl)) if p.faces[ell] in (0, 2)
                    else acb(0, ar(yh-yl)))
        R = [response[j, ell]*velocity for j in (3, 5, 7)]
        dP = p.matvec(whole[2], R)
        derivative = ((half-z[0])*dP[0]+(half-z[2])*dP[2]).real
        derivative += 11*(ar('1/2')-z[0].real)*R[0].real
        derivative += ar('151/10')*(ar('1/2')-z[2].real)*R[2].real
        if not derivative.is_finite():
            return None, 'nonfinite derivative'
        gap -= abs(derivative)*ar((bounds[2*ell+1]-bounds[2*ell])/2)
    if not gap.is_finite():
        return None, 'nonfinite gap'
    if not gap > ar(RESERVE):
        return None, 'new reserve'
    return gap.lower(), None


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--precision', type=int, default=256)
    ap.add_argument('--input', type=Path, help='Reevaluate the final new saved cover without refinements.')
    ap.add_argument('--output', type=Path, default=ROOT /
                    'repro/results/research-mixed-half-angle-connector-lower.json')
    ap.add_argument('--max-seconds', type=float, default=900)
    ap.add_argument('--max-visits', type=int, default=200000)
    args = ap.parse_args()
    assert args.precision >= 160 and 0 < args.max_seconds <= 900
    assert args.max_visits > 0
    start = time.monotonic()
    h.configure(args.precision)
    ph, sh = sha(PROOF), sha(__file__)
    dependencies, primary = validate_inputs()
    cases = [(word, ta, tb, fa, fb)
             for word in itertools.product((0, 1), repeat=5)
             for ta, tb, fa, fb in itertools.product(range(2), range(2), range(4), range(4))]
    assert len(cases) == len(set(cases)) == 2048

    def index(record):
        rows = {(tuple(row['word']), *row['external_types'], *row['faces']): row
                for row in record['cases']}
        assert len(rows) == len(record['cases']) == 2048 and set(rows) == set(cases)
        for row in rows.values():
            assert len(validate_cover(row['addresses'])) == row['cells']
        return rows

    starting = index(primary['mixed_hybrid_zero_pair_support'])
    assert sum(row['cells'] for row in starting.values()) == 18988
    input_hash = None
    if args.input:
        data = args.input.read_bytes()
        input_hash = hashlib.sha256(data).hexdigest()
        saved = json.loads(data)
        assert saved['status'] == 'passed'
        assert saved['proof_sha256'] == ph and saved['script_sha256'] == sh
        assert saved['dependencies_sha256'] == dependencies
        starting = index(saved)
        assert sum(row['cells'] for row in starting.values()) == saved['accepted_cells']
    rows, visits, refinements, worst = [], 0, 0, None
    args.output.parent.mkdir(parents=True, exist_ok=True)
    for number, case in enumerate(cases, 1):
        pending = list(reversed(starting[case]['addresses']))
        accepted, reasons, minimum = [], {}, None
        while pending:
            assert time.monotonic()-start <= args.max_seconds, (case, 'runtime limit')
            address = pending.pop()
            visits += 1
            assert visits <= args.max_visits, (case, 'visit limit')
            value, reason = test(case, h.decode(address))
            if value is None:
                assert args.input is None, (case, address, reason, 'saved new cell failed')
                assert len(address) < 30, (case, address, reason, 'depth limit')
                refinements += 1
                reasons[reason] = reasons.get(reason, 0)+1
                pending.extend([address+'1', address+'0'])
            else:
                accepted.append(address)
                # Both arguments are exact outward endpoints, not overlapping balls.
                minimum = value if minimum is None else min(minimum.lower(), value.lower())
        codes = validate_cover(accepted)
        worst = minimum if worst is None else min(worst.lower(), minimum.lower())
        rows.append(dict(word=case[0], external_types=list(case[1:3]), faces=list(case[3:]),
                         addresses=codes, cells=len(codes), minimum_reserve=str(minimum),
                         split_reasons=reasons))
        Path(str(args.output)+'.partial').write_text(json.dumps(
            dict(status='running', cases=rows), separators=(',', ':'))+'\n')
        if number % 32 == 0 or number == 1:
            print('progress', number, 2048, 'cells', sum(row['cells'] for row in rows),
                  'visits', visits, 'refinements', refinements, 'minimum', worst,
                  'elapsed', time.monotonic()-start, flush=True)
    assert ph == sha(PROOF) and sh == sha(__file__) and HELPER_SHA == sha(HELPER)
    assert all(sha(ROOT/path) == digest for path, digest in dependencies.items())
    if args.input:
        assert input_hash == sha(args.input)
    out = dict(status='passed', precision_bits=args.precision, boundary_products=2048,
               original_starting_cells=18988, accepted_cells=sum(row['cells'] for row in rows),
               visited_cells=visits, refinements=refinements, minimum_reserve=str(worst),
               strict_reserve=str(RESERVE), half_angle_ceilings=list(map(str, CEILINGS)),
               common_collar_ceiling=str(COLLAR), rotated_costs=['11/2', '151/20'],
               primary_records=len(primary), current_bindings=len(dependencies),
               cases=rows, proof_sha256=ph, script_sha256=sh, dependencies_sha256=dependencies,
               elapsed_seconds=time.monotonic()-start, runtime_limit_seconds=args.max_seconds,
               source_cover_recomputed=False,
               scope='New whole-cell geometric half-angle connector reserve on all original '
                     'five-window boundary products, retaining both rotated real costs. '
                     'No general-angle seam sign, arbitrary interface or knot-family conclusion.')
    if args.input:
        out.update(input_path=str(args.input), input_sha256=input_hash)
    args.output.write_text(json.dumps(out, indent=2)+'\n')
    Path(str(args.output)+'.partial').unlink(missing_ok=True)
    print('PASS', 2048, out['accepted_cells'], visits, refinements,
          'minimum', worst, 'elapsed', out['elapsed_seconds'], flush=True)


if __name__ == '__main__':
    main()
