#!/usr/bin/env python3
"""Exact bookkeeping and scalar budgets for complete-ended chain growth.

The proved source induction is checked as a current dependency, not
replaced by the scalar and word identities in this script.
"""
import argparse
from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path

import sympy as sp
from flint import arb, ctx

ROOT = Path(__file__).resolve().parents[1]


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--precision', type=int, default=192)
    ap.add_argument('--output', type=Path,
                    default=ROOT/'repro/results/research-three-chain-after-entrance.json')
    args = ap.parse_args()
    ctx.prec = args.precision

    def rat(value):
        value = Q(value)
        return arb(value.numerator)/value.denominator

    root = arb(21).sqrt()
    rho = (5-root)/2
    Z = rat('1.05')*rho/(1-rat('.3')*rho)
    modulus = 4*arb.pi()/root
    H, small = rat('.0057'), rat('.0004')
    comparisons = []

    def positive(name, value):
        assert value > 0, (name, value)
        comparisons.append({'name': name, 'positive_margin': str(value)})

    positive('two broader steps give H below .000312', rat('.000312')-Z*Z*H)
    positive('two broader steps enter H below .0004', small-Z*Z*H)
    positive('one-step certified upper bound is not below .0004', Z*H-small)
    positive('capped envelope decreases past .01', 2*rat('1.45')*rat('.01')-modulus*small)
    positive('Z contracts certified H', 1-Z)
    positive('ordinary corner reserve above .05', rat(Q(31, 600))-rat('.05'))

    n = sp.symbols('n', positive=True, integer=True)
    j, k = sp.symbols('j k', nonnegative=True, integer=True)
    A, T = sp.MatrixSymbol('A', n, n), sp.MatrixSymbol('T', n, n)
    left, right = A**3*T**(j+2), A**3*T**(k+2)
    closed = (left*right.T).doit().xreplace({A.T: A, T.T: T}).doit()
    expected = A**3*T**(j+k+4)*A**3
    assert closed == expected, (closed, expected)
    identities = ['bilinear right-word transpose and retained-factor order']
    m = 10+j+k
    assert sp.expand(3+(4+j+k)+3-m) == 0
    identities.append('selected-vertex count m=10+j+k')
    assert sp.expand((4+j)+(4+k)-(m-2)) == 0
    identities.append('carrier exponent kappa^(m-2) with two C_N3 factors')
    assert Q(-1)+Q(-1)+Q(1)-Q(1, 2) == Q(-3, 2)
    identities.append('closing power N^(-3/2)')
    assert Q(-1)+Q(-1, 2)+Q(1)-Q(1, 2) == Q(-1)
    identities.append('attachment preserves cap power N^(-1)')
    assert Q(3, 25)+Q(1, 15)-Q(27, 200) == Q(31, 600)
    identities.append('ordinary-boundary L40 reserve 31/600')
    assert 5+5 == 10
    identities.append('minimum length supplied by two five-vertex caps')

    deps = [
        'notes/research_three_chain_after_entrance.md',
        'notes/research_three_larger_source_propagation.md',
        'notes/research_three_first_entrance_real_extension.md',
        'notes/research_three_larger_phase_class.md',
        'notes/research_three_source_tail_propagation.md',
        'notes/research_three_small_source_closure.md',
        'notes/research_three_chain_fourier_corner_transfer.md',
        'notes/research_three_chain_geometric_chamber.md',
        'notes/research_three_chain_action_volume_calibration.md',
    ]
    induction_path = ROOT/'repro/results/research-three-larger-source-propagation.json'
    induction = json.loads(induction_path.read_text())
    assert induction['status'] == 'passed'
    assert induction['script_sha256'] == sha256(
        (ROOT/'experiments/check_three_larger_source_propagation.py').read_bytes()).hexdigest()
    for path, digest in induction['dependencies_sha256'].items():
        assert sha256((ROOT/path).read_bytes()).hexdigest() == digest, path
    result = {
        'status': 'passed', 'precision_bits': args.precision,
        'scope': 'Exact assembly checks for the proved original complete-ended scalar-source theorem at fixed m>=10, including complete-color ordinary jets. The analytic source induction and volume calibration are cited proofs; no knot identification or outside-color whole-period bound is inferred.',
        'scalar_comparisons': comparisons, 'exact_identities': identities,
        'one_step_H_bound': str(Z*H), 'two_step_H_bound': str(Z*Z*H),
        'minimum_length_from_this_preparation': 10,
        'remaining_short_lengths_from_this_argument': list(range(3, 10)),
        'passed_source_induction': {
            'record': str(induction_path.relative_to(ROOT)),
            'sha256': sha256(induction_path.read_bytes()).hexdigest(),
            'current_script_and_dependencies_verified': True,
            'scope': 'Passed record reused; its analytic component checks are not rerun here.',
        },
        'script_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
        'dependencies_sha256': {f: sha256((ROOT/f).read_bytes()).hexdigest() for f in deps},
    }
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
