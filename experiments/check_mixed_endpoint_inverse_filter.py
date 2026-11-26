#!/usr/bin/env python3
"""Exactly two prescribed endpoint-inverse tests; no proposals or refinement."""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

from flint import acb, arb, ctx
import certify_mixed_first_cap_oriented_plateau as cap

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT/'notes/research_mixed_endpoint_inverse_filter.md'
TESTS = [
    dict(name='first_cap', record='repro/results/research-mixed-first-cap-oriented-plateau-attempt01.json',
         sha='fb21ee2dc6ec496b1b890fd8d26cc471da9d845075565b05179d1abf7086e507',
         proof='notes/research_mixed_first_cap_oriented_plateau_certificate.md',
         script='experiments/certify_mixed_first_cap_oriented_plateau.py',
         job=19996, families=4, own_four_only=False,
         box=[['-212243/524288', '-106121/262144'], ['-1/2', '-262143/524288']]),
    dict(name='terminal_four', record='repro/results/research-mixed-terminal-four-source-stage3-attempt01.json',
         sha='151200a014e548445543a2aba66210c38714d0904305cdb3a73d665f60429738',
         proof='notes/research_mixed_terminal_four_oriented_source_continuation.md',
         script='experiments/continue_mixed_terminal_four_source_oriented.py',
         job=39335, families=21, own_four_only=True,
         box=[['-146935/262144', '-587739/1048576'], ['-3/4', '-393215/524288']])
]


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def disk_test(z, center, radius):
    dz = z-cap.cp(center)
    distance = dz.real**2+dz.imag**2-cap.ar(radius)**2
    return dict(squared_distance_minus_radius_squared=str(distance),
                strictly_disjoint=bool(distance > 0))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--precision', type=int, default=256)
    ap.add_argument('--output', type=Path, required=True)
    args = ap.parse_args()
    assert args.precision >= 192 and not args.output.exists()
    ctx.prec = args.precision
    dependencies = {}

    def bind(name, expected=None):
        digest = sha(ROOT/name)
        if expected is not None:
            assert digest == expected, name
        assert name not in dependencies or dependencies[name] == digest
        dependencies[name] = digest
        return digest

    records = []
    for test in TESTS:
        bind(test['record'], test['sha'])
        record = json.loads((ROOT/test['record']).read_text())
        assert record['status'] == 'incomplete' and record['fatal_error'] is None
        assert len(record['completed']) == test['job']
        assert record['active']['job'] == test['job']
        assert record['active']['failure']['box'] == test['box']
        assert record['active']['pending'][-1] == [test['box'], 30]
        assert record['face_families_per_cell'] == test['families']
        for name, digest in record['dependencies_sha256'].items():
            bind(name, digest)
        bind(test['proof'], record['proof_sha256'])
        bind(test['script'], record['script_sha256'])
        records.append(record)
    bind(str(PROOF.relative_to(ROOT)))
    bind(str(Path(__file__).resolve().relative_to(ROOT)))
    bind('notes/research_terminal_coupling_barriers.md')
    bind('notes/research_mixed_open_local_factor_coverage.md')
    roots = json.loads((ROOT/cap.ROOT_AUTHOR).read_text())
    replay = json.loads((ROOT/cap.ROOT_REPLAY).read_text())
    assert roots['status'] == replay['status'] == 'passed'
    assert replay['input_sha256'] == sha(ROOT/cap.ROOT_AUTHOR)
    assert roots['domains'] == replay['domains']
    cells = cap.original_cells(roots)
    cap.old.propose = cap.original_root_proposals_forbidden
    cap.propose_targets = cap.target_proposals_forbidden
    pi, ii = arb.pi(), acb(0, 1)
    cap.PI, cap.II = pi, ii
    cap.primitive.PI, cap.primitive.II = pi, ii
    centers = [['7/20', '-1/100'], ['3/10', '-13/250']]
    results = []
    for test in TESTS:
        eligible = [c for c in cells if c['own'] == 1] if test['own_four_only'] else cells
        ci = test['job']//test['families']
        cell = eligible[ci]
        assert (cell['own'], cell['neighbor']) == (1, 1)
        box = cap.decode_box(test['box'])
        assert all(lo <= x <= y <= hi for (lo, hi), (x, y) in zip(cell['box'], box))
        context = cap.root_context(cell)
        b = cap.old.parameter(box, 1)
        root = cap.enclosing_root(context, b, 12)
        a = root[1]
        U, A = (-2*pi*ii*b).exp(), (-2*pi*ii*a).exp()
        denom = 1-U*A
        assert abs(U) > 0 and abs(A) > 0 and abs(denom) > 0
        one_minus_UV = A*(1-U)**3/denom
        assert abs(one_minus_UV) > 0
        V = (1-one_minus_UV)/U
        W = V+(1-V)**3/one_minus_UV
        assert all(z.is_finite() for z in (b, a, U, A, V, W))
        result = dict(name=test['name'], status='unresolved', job=test['job'],
                      original_typed_cell=ci, original_node=cell['node'], box=test['box'],
                      input=str(b), endpoint_attached=str(a), inverse_V=str(V), inverse_W=str(W),
                      inherited_root_validated=True, same_inverse_intersections=12,
                      root_proposals=0, new_cells=0, source_comparisons=0,
                      m2_excluded_by_attached_real_floor=bool(b.real < cap.ar('69/250')))
        reasons = []
        if V.imag >= 0:
            reasons.append('V has nonnegative imaginary part')
        if W.imag <= 0:
            reasons.append('W has nonpositive imaginary part')
        if V.imag < 0:
            t = -V.log()/(2*pi*ii)
            assert t.is_finite() and 0 < t.real < cap.ar('1/2')
            result['ordinary_opposite_leg'] = str(t)
            result['t_D4'] = disk_test(t, centers[1], F(8, 125))
            result['t_P4'] = disk_test(t, centers[1], F(3, 50))
            if result['t_P4']['strictly_disjoint']:
                reasons.append('opposite ordinary leg is outside P4')
        if W.imag > 0:
            c = W.log()/(2*pi*ii)
            assert c.is_finite() and 0 < c.real < cap.ar('1/2')
            result['next_external_leg'] = str(c)
            result['c_D'] = [disk_test(c, centers[j], r) for j, r in enumerate((F(9, 100), F(8, 125)))]
            result['c_P'] = [disk_test(c, centers[j], r) for j, r in enumerate((F(83, 1000), F(3, 50)))]
            if all(item['strictly_disjoint'] for item in result['c_P']):
                reasons.append('next external leg is outside both smaller typed disks')
        result['exclusion_reasons'] = reasons
        if reasons:
            assert result['m2_excluded_by_attached_real_floor']
            result['status'] = 'excluded'
        results.append(result)
    for name, digest in dependencies.items():
        assert sha(ROOT/name) == digest, name
    output = dict(status='diagnostic_completed', precision_bits=args.precision,
                  dependencies_sha256=dependencies, results=results,
                  final_bindings_verified=True,
                  scope='Only two prescribed boxes; neither source attempt is promoted.')
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2)+'\n')
    print(json.dumps([dict(name=r['name'], status=r['status'], reasons=r['exclusion_reasons']) for r in results]))


if __name__ == '__main__':
    main()

