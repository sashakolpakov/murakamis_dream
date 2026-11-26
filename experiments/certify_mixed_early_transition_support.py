#!/usr/bin/env python3
"""Early transition blocks: height corners, real tangents and reference boundaries.

Every acceptance is outward. Floating roots only propose rational witnesses;
the saved-cover mode admits no new proposals or subdivisions.
"""
import argparse
import hashlib
import importlib.util
import itertools
import json
import time
from fractions import Fraction as F
from pathlib import Path
from flint import acb, arb, ctx

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT/'notes/research_mixed_early_transition_support.md'
HELPER = ROOT/'experiments/certify_mixed_real_small_support.py'
spec = importlib.util.spec_from_file_location('early_original_log', HELPER)
core = importlib.util.module_from_spec(spec)
spec.loader.exec_module(core)
ar = core.ar
HEIGHTS = {(0, 0): (F(-1, 200), F(1, 300)),
           (1, 0): (F(-19, 2000), F(0)),
           (1, 1): (F(0), F(7, 500))}
INTERVALS = [(F(1, 10)+F(7*j, 320), F(1, 10)+F(7*(j+1), 320))
             for j in range(16)]
GAP = F(1, 100)
DEPS = core.DEPS + [
    'notes/research_mixed_real_small_support.md',
    'experiments/certify_mixed_real_small_support.py',
    'repro/results/research-mixed-real-small-support.json',
    'notes/research_mixed_early_selected_source_cap.md',
    'experiments/certify_mixed_early_selected_source_cap.py',
    'repro/results/research-mixed-early-selected-source-cap.json',
    'notes/research_mixed_oriented_height_reset.md',
]


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def validate_record(record_path, proof, script):
    rec = json.loads((ROOT/record_path).read_text())
    assert rec['status'] == 'passed'
    assert rec['proof_sha256'] == sha(ROOT/proof)
    assert rec['script_sha256'] == sha(ROOT/script)
    for field in ('dependencies', 'dependencies_sha256'):
        assert all(sha(ROOT/p) == h for p, h in rec.get(field, {}).items())


def tangent_data(source):
    old = {} if source is None else {tuple(r['key']): r['center'] for r in source['tangent_roots']}
    roots, cached = {}, {}
    data = {(eta, eps): [] for eta, eps in itertools.product((0, 1), repeat=2)}
    for eta, eps in itertools.product((0, 1), repeat=2):
        for sa, sb in itertools.product(range(eta+1), range(eps+1)):
            for fa, fb in itertools.product(range(sa+1), range(sb+1)):
                for h0, h1 in itertools.product(HEIGHTS[eta, sa], HEIGHTS[eps, sb]):
                    for side, j in itertools.product((0, 1), range(len(INTERVALS))):
                        lo, hi = INTERVALS[j]
                        real = (F(3, 25), (lo+hi)/2) if side == 0 else ((lo+hi)/2, F(3, 25))
                        c = [acb(ar(real[k]), ar((h0, h1)[k])) for k in (0, 1)]
                        key = (eps, str(h0), str(h1), side, j)
                        if key not in cached:
                            if source is not None:
                                assert key in old
                            root = core.point_root(*c, eps, old.get(key))
                            assert root is not None, key
                            cached[key] = root[0]
                            roots[key] = root[1]
                        s = cached[key]
                        value, grad, _ = core.phase(s, *c, eta, eps)
                        grad = list(grad)
                        for k, (selected, forcing) in enumerate(((sa, fa), (sb, fb))):
                            value += ar(F(forcing, 2))*core.g(c[k])+core.pi*core.ii*(selected-forcing)*c[k]
                            grad[k] += ar(F(forcing, 2))*core.gp(c[k])+core.pi*core.ii*(selected-forcing)
                        corners = itertools.product((F(1, 10), F(3, 25)), (lo, hi)) if side == 0 else itertools.product((lo, hi), (F(1, 10), F(3, 25)))
                        for x in corners:
                            target = [acb(ar(x[k]), ar((h0, h1)[k])) for k in (0, 1)]
                            bound = (value+sum((grad[k]*ar(x[k]-real[k]) for k in (0, 1)), acb(0))).real
                            exact_key = (x[0], x[1], h0, h1, side)
                            data[eta, eps].append((target, bound, side, exact_key))
    if source is not None:
        assert set(old) == set(roots) and len(old) == len(source['tangent_roots'])
    # For identical target/charge pairs only the largest tangent bound matters.
    # Taking upper endpoints makes this simplification an outward enlargement.
    counts = {}
    for types, rows in data.items():
        merged = {}
        for target, bound, side, key in rows:
            if key not in merged or bound.upper() > merged[key][1]:
                merged[key] = (target, bound.upper(), side)
        counts[str(types)] = [len(rows), len(merged)]
        data[types] = list(merged.values())
    return data, [{'key': list(key), 'center': center} for key, center in sorted(roots.items())], counts


def test(case, address, tangent, witness):
    eta, eps, fa, fb = case
    al, ah, bl, bh = core.box(address)
    r = [core.edge(eta, fa, al, ah), core.edge(eps, fb, bl, bh)]
    r0 = [core.edge(eta, fa, (al+ah)/2, (al+ah)/2), core.edge(eps, fb, (bl+bh)/2, (bl+bh)/2)]
    roots = core.root_box(*r, *r0, eps, witness)
    if roots is None:
        return None
    s, s0, wit = roots
    value, grad, _ = core.phase(s0, *r0, eta, eps)
    _, _, H = core.phase(s, *r, eta, eps)
    velocity = [core.velocity(eta, fa), core.velocity(eps, fb)]
    radius = [ar((ah-al)/2), ar((bh-bl)/2)]
    worst = None
    for target, tang, side in tangent[eta, eps]:
        other = 1-side
        q = ar(F(11, 2) if side == 0 else F(151, 20))
        plane = value+sum((grad[k]*(target[k]-r0[k]) for k in (0, 1)), acb(0))
        upper = tang-plane.real+q*r0[other].imag**2
        for k in (0, 1):
            derivative = -sum((H[l][k]*(target[l]-r[l]) for l in (0, 1)), acb(0))*velocity[k]
            real_derivative = derivative.real
            if k == other:
                real_derivative += 2*q*r[other].imag*velocity[k].imag
            upper += abs(real_derivative)*radius[k]
        if not upper < -ar(GAP):
            return None
        worst = upper.upper() if worst is None else max(worst, upper.upper())
    return wit, worst


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--precision', type=int, default=256)
    parser.add_argument('--max-visits', type=int, default=200000)
    parser.add_argument('--input', type=Path)
    parser.add_argument('--output', type=Path, default=ROOT/'repro/results/research-mixed-early-transition-support.json')
    args = parser.parse_args()
    assert args.precision >= 128
    ctx.prec = args.precision
    core.pi, core.ii = arb.pi(), acb(0, 1)
    initial = {p: sha(ROOT/p) for p in DEPS}
    ph, sh = sha(PROOF), sha(__file__)
    for j in (0, 3, 8):
        validate_record(core.DEPS[j+2], core.DEPS[j], core.DEPS[j+1])
    for j in (len(core.DEPS), len(core.DEPS)+3):
        validate_record(DEPS[j+2], DEPS[j], DEPS[j+1])
    cot_margin = ar(F(1, 2))-(2*core.pi*ar(F(7, 500))).sinh()/(2*(core.pi*ar(F(1, 10))).sin()**2)
    assert cot_margin > 0
    ih = sha(args.input) if args.input else None
    source = json.loads(args.input.read_text()) if args.input else None
    if source is not None:
        assert source['status'] == 'passed' and source['reference_products'] == 64
        assert source['proof_sha256'] == ph and source['script_sha256'] == sh
        assert source['dependencies'] == initial and source['phase_gap'] == str(GAP)
    tangent, roots, counts = tangent_data(source)
    print('tangents', len(roots), counts, flush=True)
    expected = list(itertools.product((0, 1), (0, 1), range(4), range(4)))
    if source is not None:
        assert [tuple(row['case']) for row in source['cases']] == expected
    rows, visits, cells, worst = [], 0, 0, None
    start = time.time()
    for index, case in enumerate(expected):
        pending = [('', None)] if source is None else [(r['address'], r['witness']) for r in source['cases'][index]['leaves']]
        if source is not None:
            core.cover([address for address, _ in pending])
        leaves = []
        while pending:
            address, witness = pending.pop()
            visits += 1
            assert visits <= args.max_visits
            result = test(case, address, tangent, witness)
            if result is None:
                assert source is None and len(address) < 28, (case, address)
                pending.extend([(address+'0', None), (address+'1', None)])
                continue
            wit, upper = result
            worst = upper if worst is None else max(worst, upper)
            leaves.append({'address': address, 'witness': wit})
        leaves.sort(key=lambda r: r['address'])
        core.cover([r['address'] for r in leaves])
        cells += len(leaves)
        rows.append({'case': list(case), 'leaves': leaves})
        print('case', index+1, case, 'cells', len(leaves), 'visits', visits, 'elapsed', round(time.time()-start, 2), flush=True)
    assert initial == {p: sha(ROOT/p) for p in DEPS}
    assert ph == sha(PROOF) and sh == sha(__file__)
    if args.input:
        assert ih == sha(args.input)
    record = dict(status='passed', precision_bits=args.precision, phase_gap=str(GAP),
                  reference_products=64, cells=cells, visits=visits, worst_defect_upper=str(worst),
                  cotangent_margin=str(cot_margin), tangent_roots=roots, tangent_counts=counts,
                  cases=rows, proof_sha256=ph, script_sha256=sh, dependencies=initial,
                  input_sha256=ih, elapsed_seconds=time.time()-start,
                  scope='One early-transition coordinate, other real coordinate in [.1,.45], independent typed small heights, and full oriented neighboring reset allowance; all selections and forcing branches. No global transition assembly.')
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(record, indent=2)+'\n')
    print('PASS', len(rows), cells, visits, 'worst', worst, flush=True)


if __name__ == '__main__':
    main()
