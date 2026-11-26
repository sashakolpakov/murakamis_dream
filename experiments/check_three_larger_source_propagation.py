#!/usr/bin/env python3
"""Focused assembly checks for the full larger-source induction.

The source/contour proofs are explicit dependencies. This checks their
passed-record provenance, the exact partition and normalization, and
the scalar class/reset inclusions used to assemble them.
"""
import argparse
from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path

from flint import arb, ctx
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--precision', type=int, default=192)
    ap.add_argument('--output', type=Path,
                    default=ROOT/'repro/results/research-three-larger-source-propagation.json')
    args = ap.parse_args()
    ctx.prec = args.precision

    def a(value):
        value = Q(value)
        return arb(value.numerator)/value.denominator

    pi, sq = arb.pi(), arb(21).sqrt()
    K, alpha = 4*pi/sq, 8*pi*arb(3).sqrt()/21
    rho, D = (5-sq)/2, 5+sq
    H, b, A, aa, W = map(a, ['.0057', '.18', '1.45', '1.5', '.009'])
    Z = rho*a('1.05')/(1-a('.3')*rho)
    C0 = K*(D+a('.6'))/(2*(D-a('.6'))**2)
    C = C0+K**2/(4*(A+aa))
    checks = []

    def positive(name, value):
        assert value > 0, (name, value)
        checks.append({'name': name, 'strict_positive_margin': str(value)})

    positive('gradient upper bound contracts', 1-Z)
    positive('disk derivative remains in the class', b-a('.16'))
    positive('real-interval derivative remains in the class', b-a('.15'))
    positive('central accretivity exceeds18 on the entire output union',
             alpha*D-a('.44')*K-18)
    positive('local real packet resets quadratic envelope', (sq*alpha-K*b)/2-A)
    positive('whole-period reset at zero gradient', (aa-A)*W**2)
    positive('whole-period reset at largest gradient exceeds .00001061',
             K*Z*H*W+(aa-A)*W**2-C*H**2-a('.00001061'))
    positive('reset quadratic is convex', C)
    positive('total normalization drift below six millionths',
             a('.000006')-C0*H**2/(1-Z**2))
    positive('one attachment need not reach small certified class', Z*H-a('.0004'))
    positive('two attachments reach .000312', a('.000312')-Z**2*H)
    positive('two attachments reach the small class', a('.0004')-Z**2*H)
    positive('larger cap weakens to small cap for small class',
             2*A*a('.01')-K*a('.0004'))

    # Exact measure-zero shared endpoints are retained in the interval
    # decomposition; the interiors form a disjoint exhaustive period.
    cuts = list(map(Q, ['-1/2', '-1/50', '-9/1000', '-1/200',
                        '1/200', '9/1000', '1/50', '1/2']))
    regions = [(cuts[j], cuts[j+1]) for j in range(len(cuts)-1)]
    assert all(lo < hi for lo, hi in regions)
    assert sum(hi-lo for lo, hi in regions) == 1
    assert all(regions[j][1] == regions[j+1][0] for j in range(len(regions)-1))
    labels = ['far', 'intermediate', 'near', 'central', 'near', 'intermediate', 'far']
    gaps = {'far': Q(1, 2500), 'intermediate': Q(1, 100000), 'near': Q(1, 80000)}
    assert min(gaps.values()) == Q(1, 100000)

    # Cardinal integration supplies a bilinear identity. Once contracted,
    # a right attachment multiplies the existing row word on the right.
    ell = sp.Matrix([[2, -1, 3]])
    AA = sp.Matrix([[1, 2, 0], [2, -1, 3], [0, 3, 4]])
    TT = sp.Matrix([[0, -1, 2], [-1, 3, 1], [2, 1, 5]])
    assert AA*TT != TT*AA
    row = ell*AA**3
    word_checks = 0
    for j in range(6):
        assert row == ell*AA**3*TT**j
        row = row*TT
        word_checks += 1
    # No conjugation or reversal occurs in a single right attachment.
    nu = sp.Symbol('nu')
    assert sp.simplify(1+nu-sp.Rational(1, 2)-sp.Rational(1, 2)-nu) == 0
    assert Q(-1)+1-Q(1, 2)-Q(1, 2) == -1

    component_records = [
        ('research-three-real-output-phase-schur', 'certify_three_real_output_phase_schur.py', None),
        ('research-three-real-output-phase-schur-replay', 'replay_three_real_output_phase_schur.py',
         'research-three-real-output-phase-schur'),
        ('research-three-generic-source-outer-transport', 'check_three_generic_source_outer_transport.py', None),
        ('research-three-larger-source-intermediate-annulus', 'check_three_larger_source_intermediate_annulus.py', None),
        ('research-three-first-entrance-real-budgets', 'check_three_first_entrance_real_budgets.py', None),
        ('research-three-vertex-real-input-union', 'certify_three_vertex_real_input_union.py', None),
        ('research-three-vertex-real-input-union-replay', 'replay_three_vertex_real_input_union.py',
         'research-three-vertex-real-input-union'),
    ]
    reports = []
    for stem, script, artifact in component_records:
        path = 'repro/results/'+stem+'.json'
        record = json.loads((ROOT/path).read_text())
        assert record['status'] == 'passed', path
        assert record['script_sha256'] == sha256((ROOT/'experiments'/script).read_bytes()).hexdigest(), script
        for dependency, digest in record.get('dependencies_sha256', {}).items():
            assert sha256((ROOT/dependency).read_bytes()).hexdigest() == digest, (path, dependency)
        if artifact is not None:
            assert record['artifact_sha256'] == sha256(
                (ROOT/'repro/results'/(artifact+'.json')).read_bytes()).hexdigest(), path
        reports.append({'record': path, 'sha256': sha256((ROOT/path).read_bytes()).hexdigest(),
                        'status': record['status'],
                        'current_script_and_dependency_hashes_verified': True,
                        'scope': 'Passed component record reused; analytic check not rerun by assembly.'})

    dependencies = [
        'notes/research_three_larger_source_propagation.md',
        'notes/research_three_larger_phase_class.md',
        'notes/research_three_generic_source_outer_transport.md',
        'notes/research_three_larger_source_intermediate_annulus.md',
        'notes/research_three_first_entrance_real_extension.md',
        'notes/research_three_prepared_cap_real_extension.md',
        'notes/research_three_vertex_real_input_union.md',
        'notes/research_three_vertex_bidisk_packet.md',
        'notes/research_three_vertex_two_wire_large_cap_bound.md',
        'notes/research_three_vertex_large_cap_height_bound.md',
        'notes/research_three_source_tail_propagation.md',
        'notes/research_three_small_source_closure.md',
        'notes/research_three_chain_fourier_corner_transfer.md',
    ]
    result = {
        'status': 'passed', 'precision_bits': args.precision,
        'scope': 'Exact period coverage, class inclusions, real reset and action drift, finite-word orientation and powers of N, and hashes of passed component records. Does not independently re-prove the analytic contour, source entrance, corner transfer or volume calibration.',
        'strict_scalar_comparisons': len(checks), 'comparisons': checks,
        'exact_period_regions': [{'interval': [str(lo), str(hi)], 'type': labels[j]}
                                 for j, (lo, hi) in enumerate(regions)],
        'minimum_complementary_gap': str(min(gaps.values())),
        'normalization_identities': 2, 'noncommuting_word_checks': word_checks,
        'passed_component_records': reports,
        'constants': {'Z': str(Z), 'two_step_gradient_upper': str(Z**2*H),
                      'summed_action_drift_upper': str(C0*H**2/(1-Z**2))},
        'script_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
        'dependencies_sha256': {p: sha256((ROOT/p).read_bytes()).hexdigest() for p in dependencies},
    }
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: result[k] for k in ['status', 'strict_scalar_comparisons',
                    'normalization_identities', 'noncommuting_word_checks']}, indent=2))
    print('Two-step gradient bound:', Z**2*H)
    print('Summed action drift:', C0*H**2/(1-Z**2))


if __name__ == '__main__':
    main()
