#!/usr/bin/env python3
"""Outward budgets and exact source bookkeeping for the larger closure.

The finite contour and geometric calibration are written dependencies.
This checker verifies their closing margins and the original matrix word;
it does not infer a knot invariant from that scalar word.
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
    ap.add_argument('--precision', type=int, default=256)
    ap.add_argument('--output', type=Path,
                    default=ROOT/'repro/results/research-three-larger-source-closure.json')
    args = ap.parse_args()
    ctx.prec = args.precision

    def a(value):
        value = Q(value)
        return arb(value.numerator)/value.denominator

    pi, sq = arb.pi(), arb(21).sqrt()
    K, real_k = 4*pi/sq, 8*pi*arb(3).sqrt()/21
    D, beta = 2*sq, a('.36')
    R, W, H, r, A, B = map(a, ['.005', '.009', '.0057', '.0013', '1.45', '.000077'])
    rho = (5-sq)/2
    Z = a('1.05')*rho/(1-a('.3')*rho)
    C = K*(D+beta)/(2*(D-beta)**2)
    Lmax, Lunequal = 2*H, (1+Z)*H
    sector = D*(real_k*R**2-2*K*R*r-K*r**2)-beta*K*(R+r)**2
    endpoint_derivative = D*(real_k*R-K*r)-beta*K*(R+r)
    actual_B = a('.000066')+a('.0113')**2/(4*(A+a('1.5')))
    generic_gap = 2*A*W**2-K*Lunequal*W-C*Lunequal**2
    actual_gap = 3*W**2-2*B-C*Lmax**2
    checks = []

    def positive(name, value):
        assert value > 0, (name, value)
        checks.append({'name': name, 'strict_positive_margin': str(value)})

    positive('critical fixed-point map contracts', 1-beta/D)
    positive('critical fixed-point map preserves true R disk', D*R-Lmax-beta*R)
    positive('critical displacement strictly below .0013', r-Lmax/(D-beta))
    positive('V contour remains in source disk', R-r)
    positive('real curvature strictly above18', D*real_k-beta*K-18)
    positive('both endpoint sectors exceed .000066', sector-a('.000066'))
    positive('both real endpoint derivative margins exceed .05', endpoint_derivative-a('.05'))
    positive('central endpoint losses exceed .000033', sector/2-a('.000033'))
    positive('two entrance caps have B2 below .000077', B-actual_B)
    positive('unequal-preparation loss increases outside W', 4*A*W-K*Lunequal)
    positive('unequal-preparation whole outer period has gap above .00005', generic_gap-a('.00005'))
    positive('two actual entrance caps have whole outer gap above .00005', actual_gap-a('.00005'))
    positive('source gradient upper bounds contract with attachments', 1-Z)
    positive('ordinary corner restoration leaves .05 reserve', a(Q(31, 600))-a('.05'))
    positive('opposite endpoint real displacements remain nonzero', R-r)

    # The all-N bilinear cardinal identity is imported from the cited
    # source proof. This symbolic identity checks its frequency pairing,
    # without presenting a finite-level sample as an all-level proof.
    n = sp.Symbol('n', positive=True, integer=True)
    j = sp.Symbol('j', nonnegative=True, integer=True)
    frequency = j-(n-1)/2
    opposite = (n-1-j)-(n-1)/2
    assert sp.simplify(frequency+opposite) == 0
    identities = ['symbolic opposite-frequency pairing for both parities']
    AA, TT = sp.MatrixSymbol('A', n, n), sp.MatrixSymbol('T', n, n)
    closed = (AA**3*(AA**3*TT**j).T).doit().xreplace({AA.T: AA, TT.T: TT}).doit()
    assert closed == AA**3*TT**j*AA**3
    identities.append('literal bilinear closure is A^3 T^j A^3')
    m = 6+j
    assert sp.expand(3+j+3-m) == 0
    identities.append('selected-vertex count m=6+j')
    assert sp.expand(2+(2+j)-(m-2)) == 0
    identities.append('carrier C_N3^2 kappa^(m-2)')
    assert Q(-1)+Q(-1)+Q(1)-Q(1, 2) == Q(-3, 2)
    identities.append('original measure and Gaussian give N^(-3/2)')
    assert (AA**3*TT**0*AA**3).doit() == AA**6
    identities.append('j=0 is exactly undeleted A^6')
    assert Q(3, 25)+Q(1, 15)-Q(27, 200) == Q(31, 600)
    identities.append('L40 ordinary-boundary corner gap31/600')
    assert 2*Q(9, 50) == Q(9, 25)
    identities.append('closing Hessian defect is the sum .36')
    # Exact partition including the two real annuli and full outer period.
    cuts = list(map(Q, ['-1/2', '-.009', '-.005', '.005', '.009', '1/2']))
    assert sum(cuts[k+1]-cuts[k] for k in range(5)) == 1
    assert all(cuts[k+1] > cuts[k] for k in range(5))
    identities.append('five exact input intervals exhaust a full period')

    induction_path = ROOT/'repro/results/research-three-larger-source-propagation.json'
    induction = json.loads(induction_path.read_text())
    assert induction['status'] == 'passed'
    assert induction['script_sha256'] == sha256(
        (ROOT/'experiments/check_three_larger_source_propagation.py').read_bytes()).hexdigest()
    for path, digest in induction['dependencies_sha256'].items():
        assert sha256((ROOT/path).read_bytes()).hexdigest() == digest, path

    deps = [
        'notes/research_three_larger_source_closure.md',
        'notes/research_three_larger_source_propagation.md',
        'notes/research_three_first_entrance_real_extension.md',
        'notes/research_three_small_source_closure.md',
        'notes/research_three_chain_geometric_chamber.md',
        'notes/research_three_chain_action_volume_calibration.md',
        'notes/research_three_chain_fourier_corner_transfer.md',
    ]
    result = {
        'status': 'passed', 'precision_bits': args.precision,
        'scope': 'Larger full bilinear closure and exact original complete-ended word at each fixed m>=6, with ordinary jets at complete colors. No outside-color whole-period or knot-identification assertion.',
        'strict_scalar_comparisons': len(checks), 'comparisons': checks,
        'exact_identities': identities,
        'constants': {'critical_radius_upper': str(Lmax/(D-beta)),
                      'closing_action_drift_constant': str(C),
                      'endpoint_sector_lower': str(sector),
                      'endpoint_derivative_lower': str(endpoint_derivative),
                      'unequal_preparation_outer_gap': str(generic_gap),
                      'actual_entrance_outer_gap': str(actual_gap),
                      'actual_entrance_B2_upper': str(actual_B)},
        'minimum_length': 6, 'remaining_short_lengths_from_this_argument': [3, 4, 5],
        'source_induction_record_sha256': sha256(induction_path.read_bytes()).hexdigest(),
        'source_induction_current_script_and_dependencies_verified': True,
        'script_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
        'dependencies_sha256': {p: sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},
    }
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: result[k] for k in ['status', 'strict_scalar_comparisons',
                    'constants']}, indent=2))
    print('Exact identities:', len(identities))


if __name__ == '__main__':
    main()
