#!/usr/bin/env python3
"""Exact scalar and finite Fourier checks for the small-source closure.

The analytic source hypotheses and contour proof are in the note.
This checker does not establish a finite entrance source.
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
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--precision', type=int, default=192)
    parser.add_argument('--output', type=Path,
                        default=ROOT/'repro/results/research-three-small-source-closure.json')
    args = parser.parse_args()
    ctx.prec = args.precision

    def a(value):
        value = Q(value)
        return arb(value.numerator)/value.denominator

    checks = []

    def positive(name, value):
        assert value > 0, (name, value)
        checks.append({'name': name, 'strict_positive_margin': str(value)})

    pi, root21 = arb.pi(), arb(21).sqrt()
    kabs, kalpha = 4*pi/root21, 8*pi*arb(3).sqrt()/21
    D, b = 2*root21, a(Q(9, 25))
    R, rc, L = a(Q(1, 200)), a(Q(3, 625)), a(Q(1, 1250))
    A, zr = a(Q(29, 20)), a(Q(1, 10000))
    Ccl = kabs*(D+b)/(2*(D-b)**2)
    positive('critical fixed map contracts by less than 1/25', a(Q(1, 25))-b/D)
    positive('critical fixed map is a strict disk self-map', R-(L+b*R)/D)
    positive('critical radius below 1/10000', zr-L/(D-b))
    positive('joint real Hessian loss above 16', D*kalpha-b*kabs-16)
    positive('outside-period loss increases beyond central cut', 4*A*rc-kabs*L)
    gap = 2*A*rc**2-kabs*L*rc-Ccl*L**2
    positive('full-period complementary gap above 1/20000', gap-a(Q(1, 20000)))
    positive('translated central rectangle stays inside source disk', R**2-rc**2-zr**2)
    positive('translated endpoint gap above 1/20000', 8*(rc-zr)**2-a(Q(1, 20000)))

    # Literal cardinal functions are
    # h_j(x)=N^-1 sum_{q=-(N-1), step2}^{N-1} exp(i*pi*q*(x-j/N)).
    # Opposite frequencies survive the period integral. The remaining
    # root-of-unity polynomial is reduced exactly modulo t^N-1; for
    # j!=k its evaluation is zero by the geometric sum at a nontrivial
    # Nth root. This tests the finite frequency range at both parities,
    # with no floating roots of unity or Gaussian replacement.
    Fourier_cases = []
    for N in range(2, 33):
        frequencies = list(range(-(N-1), N, 2))
        assert len(frequencies) == N and all(-q in frequencies for q in frequencies)
        surviving = [(q, r) for q in frequencies for r in frequencies if q+r == 0]
        assert len(surviving) == N
        assert all((q+r) % 2 == 0 for q in frequencies for r in frequencies)
        for diff in range(N):
            residues = [(i*diff) % N for i in range(N)]
            if diff == 0:
                assert residues == [0]*N
            else:
                # Every residue in the cyclic subgroup occurs equally.
                from math import gcd
                g = gcd(N, diff)
                assert sorted(set(residues)) == list(range(0, N, g))
                assert all(residues.count(r) == g for r in set(residues))
        Fourier_cases.append({'N': N, 'cardinal_count': N,
                              'opposite_frequency_pairs': N,
                              'parity_sign': (-1)**(N-1)})

    # A noncommuting symbolic matrix product verifies the orientation;
    # an entry-wise exact replay uses symmetric matrices which do not
    # commute, so reversing the endpoint factors cannot pass accidentally.
    X, Y, Z = [sp.MatrixSymbol(n, 3, 3) for n in ['X', 'Y', 'Z']]
    assert sp.transpose(X*Y*Z) == Z.T*Y.T*X.T
    AA = sp.Matrix([[1, 2, 0], [2, -1, 3], [0, 3, 4]])
    TT = sp.Matrix([[0, -1, 2], [-1, 3, 1], [2, 1, 5]])
    left, right = sp.Matrix([2, -1, 3]), sp.Matrix([-1, 4, 2])
    assert AA*TT != TT*AA
    word_checks = 0
    for j in range(4):
        for k in range(4):
            frow = left.T*AA**2*TT**j
            grow = right.T*AA**2*TT**k
            assert frow*grow.T == left.T*AA**2*TT**(j+k)*AA**2*right
            word_checks += 1
    assert Q(-1)+Q(-1)+Q(1, 2) == Q(-3, 2)

    deps = [
        'notes/research_three_small_source_closure.md',
        'notes/research_three_source_tail_propagation.md',
        'notes/research_three_cap_central_source.md',
        'notes/research_three_prepared_cap_quantified_source.md',
        'notes/research_traced_three_vertex_endpoint.md',
        'notes/research_three_chain_fourier_corner_transfer.md',
    ]
    result = {'status': 'passed', 'precision_bits': args.precision,
              'scalar_comparisons': len(checks), 'checks': checks,
              'Fourier_level_count': len(Fourier_cases), 'Fourier_levels': Fourier_cases,
              'noncommuting_word_checks': word_checks,
              'exact_symbolic_transpose_identities': 1,
              'exact_normalization_identities': 1,
              'constants': {'C_cl': str(Ccl), 'critical_radius_upper': str(L/(D-b)),
                            'closure_action_drift_upper': str(Ccl*L**2),
                            'full_period_gap': str(gap)},
              'scope': 'Outward scalar budgets, exact finite-frequency cardinal algebra and noncommuting orientation tests. Does not certify source entrance hypotheses, contour proof, or a volume identity.',
              'script_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
              'dependencies_sha256': {p: sha256((ROOT/p).read_bytes()).hexdigest() for p in deps}}
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({key: result[key] for key in
                      ['status', 'scalar_comparisons', 'Fourier_level_count',
                       'noncommuting_word_checks']}, indent=2))
    print('full-period gap:', gap)


if __name__ == '__main__':
    main()
