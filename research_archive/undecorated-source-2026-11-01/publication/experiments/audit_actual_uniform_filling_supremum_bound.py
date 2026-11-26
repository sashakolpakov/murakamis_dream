#!/usr/bin/env python3
"""Finite exact identity checks for the uniform filling-norm proof.

The norm inequalities are proved analytically in the companion note. This
runner checks algebraic inputs, not sampled operator norms. Cyclotomic tests
are over Q. Physical matrices use the existing independent original-source
constructors over their explicitly recorded finite fields.
"""

import argparse
import hashlib
import json
import sys
from pathlib import Path

import numpy as np
import sympy as sp


class Cyclotomic:
    def __init__(self, order):
        self.z = sp.Symbol('z')
        self.mod = sp.Poly(sp.cyclotomic_poly(order, self.z), self.z, domain=sp.QQ)
        self.order = order
        self.zero = self.red(0)
        self.one = self.red(1)
        self.powers = [self.red(self.z**k) for k in range(order)]

    def red(self, x):
        return sp.Poly(x, self.z, domain=sp.QQ).rem(self.mod)

    def mul(self, x, y):
        return (x*y).rem(self.mod)

    def inv(self, x):
        return sp.invert(x, self.mod)

    def power(self, k):
        return self.powers[k % self.order]

    def evaluate(self, coefficients, x):
        out = self.zero
        for a in reversed(coefficients):
            out = self.mul(out, x) + self.red(a)
        return out


def riesz_checks():
    rows = []
    for d in range(1, 13):
        field = Cyclotomic(4*d)
        imaginary = field.power(d)
        nodes, weights = [], []
        for r in range(1, 2*d+1):
            node = field.power(2*r-1)
            denominator = d*(field.red(2)-node-field.power(-(2*r-1)))
            closed = (-1)**(r+1)*field.inv(denominator)
            # Independently sum the inverse finite Fourier matrix.
            mode_sum = field.zero
            for j in range(-d+1, d+1):
                mode_sum += sp.Rational(j, 2*d)*field.mul(
                    imaginary, field.power(-(2*r-1)*j))
            assert field.red(closed-mode_sum).is_zero, (d, r, 'weights')
            nodes.append(node)
            weights.append(closed)
        for j in range(-d, d+1):
            actual = field.zero
            for r, weight in enumerate(weights, 1):
                actual += field.mul(weight, field.power((2*r-1)*j))
            assert field.red(actual-j*imaginary).is_zero, (d, j, 'mode')
        # These are the positive magnitudes of the real closed-form weights.
        mass = sum(((-1)**(r+1)*w for r, w in enumerate(weights, 1)), field.zero)
        assert field.red(mass-d).is_zero
        rows.append(dict(degree=d, cyclotomic_order=4*d,
                         inverse_Fourier_weight_identities=2*d,
                         derivative_mode_identities=2*d+1,
                         exact_absolute_weight_mass=d))
    return rows


def chebyshev_checks():
    x = sp.Symbol('x')
    rows = []
    for N in range(2, 13):
        field = Cyclotomic(2*N)
        chi = sp.Poly(2*sp.chebyshevt(N, x/2)+2, x)
        coeff = [chi.nth(k) for k in range(N+1)]
        derivatives = [[sp.diff(chi.as_expr(), x, j).expand().coeff(x, k)
                        for k in range(N+1-j)] for j in range(4)]
        distinct = []
        for a in range(N//2):
            c = field.power(2*a+1)+field.power(-2*a-1)
            values = [field.evaluate(cs, c) for cs in derivatives]
            assert values[0].is_zero and values[1].is_zero
            gap = field.red(4)-field.mul(c, c)
            assert field.red(field.mul(values[2]/2, gap)-N*N).is_zero
            assert field.red(field.mul(values[3]/6, field.mul(gap, gap))
                             -N*N*c).is_zero
            distinct.append(c)
        # Multiply the full repeated-node polynomial independently of T_N.
        product = [field.one]
        factors = [c for c in distinct for _ in range(2)]
        if N % 2:
            factors.append(field.red(-2))
            assert chi.eval(-2) == 0 and chi.diff().eval(-2) == N*N
        for c in factors:
            new = [field.zero for _ in range(len(product)+1)]
            for k, value in enumerate(product):
                new[k] -= field.mul(c, value)
                new[k+1] += value
            product = [field.red(v) for v in new]
        assert all(field.red(a-b).is_zero for a, b in zip(product, coeff))
        rows.append(dict(N=N, cyclotomic_order=2*N, double_nodes=N//2,
                         simple_minus_two_node=bool(N % 2),
                         full_multiplicity_factorization=True,
                         double_residue_and_derivative_identities=2*(N//2)))
    return rows


def physical_and_compressed(repo):
    experiments = repo/'experiments'
    if not experiments.is_dir():
        raise RuntimeError('Pass --repo with the research checkout containing experiments/')
    sys.path.insert(0, str(experiments))
    from audit_actual_spectral_total_derivative_source import original_matrices
    from audit_actual_small_circle_polynomial_face_insertion import Local

    # This routine builds Omega from E,F,K and R,+/- from the signed transfer
    # formula, then compares the full midpoint reconstruction entry by entry.
    original = original_matrices()
    x = sp.Symbol('x')
    compressed = []
    for N in range(3, 9):
        loc = Local(N)
        p, q, d = loc.p, loc.q, N-1
        im = pow(loc.eta, N, p)
        sine = [(pow(q, j, p)-pow(q, -j, p))*pow(im, -1, p) % p
                for j in range(N)]
        O = np.zeros((N, N), dtype=np.int64)
        for j in range(N):
            O[j, j] = (pow(q, 2*j+1, p)+pow(q, -2*j-1, p)) % p
            if j >= 1:
                O[j-1, j] = -sine[j]**2*5 % p  # x=2, y=3
            if j >= 2:
                O[j-2, j] = -sine[j]*sine[j-1]*6 % p
        I = np.eye(N, dtype=np.int64)
        powers = [I]
        for j in range(N):
            powers.append(powers[-1]@O % p)
        chi = sp.Poly(2*sp.chebyshevt(N, x/2)+2, x)
        coeff = [int(chi.nth(k)) % p for k in range(N+1)]
        assert np.array_equal(sum((c*A for c, A in zip(coeff, powers)),
                                 np.zeros_like(I)) % p, np.zeros_like(I))
        numerators = []
        for a in range(N):
            c = int(O[a, a])
            V, Vp = np.zeros_like(I), np.zeros_like(I)
            for degree in range(1, N+1):
                for j in range(degree):
                    e = degree-1-j
                    V = (V+coeff[degree]*pow(c, e, p)*powers[j]) % p
                    if e:
                        Vp = (Vp+coeff[degree]*e*pow(c, e-1, p)*powers[j]) % p
            numerators.append((c, V, Vp))
        size = N//2
        low = O[:size, :size]
        lowI = np.eye(size, dtype=np.int64)
        projectors = []
        for a in range(size):
            c = int(O[a, a])
            projector = lowI.copy()
            for b in range(size):
                if a != b:
                    cb = int(O[b, b])
                    projector = projector@(low-cb*lowI) % p
                    projector = projector*pow((c-cb) % p, -1, p) % p
            projectors.append(projector)
            for c0, V, Vp in numerators:
                assert np.array_equal(V[:size, :size], np.zeros_like(lowI))
            c0, V, Vp = numerators[a]
            expected = ((4-c0*c0)*pow(N*N, -1, p))*Vp[:size, :size] % p
            assert np.array_equal(expected, projector), (N, a, 'normal projector')
        for n in (-3, -1, 0, 1, 2, 3):
            full = np.zeros_like(I)
            semisimple = np.zeros_like(lowI)
            for a, (c, V, Vp) in enumerate(numerators):
                root = pow(loc.eta, d*d, p)*pow(-1, a, p)*pow(q, a*(a+1), p) % p
                f = pow(root, n, p)
                h = 2*a+1
                gamma = (-(N-h)*pow(2*(pow(q, h, p)-pow(q, -h, p)) % p,
                                     -1, p)) % p if h != N else 0
                fp = n*gamma*f % p
                full = (full+(4-c*c)*(f*Vp+fp*V)-c*f*V) % p
                if a < size:
                    semisimple = (semisimple+f*projectors[a]) % p
            full = full*pow(2*N*N, -1, p) % p
            assert np.array_equal(full[:size, :size], semisimple), (N, n)
            assert int(full[0, 0]) == pow(pow(loc.eta, d*d, p), n, p)
        compressed.append(dict(N=N, prime=p, block_size=size,
                               signed_powers=[-3, -1, 0, 1, 2, 3],
                               full_node_vanishing=True,
                               original_numerator_normals_equal_projectors=True,
                               lower_full_Hermite_equals_value_block=True,
                               retained_diagonal_unit_phase=True))
    return original, compressed


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--output', type=Path,
                        default=Path(__file__).with_name(
                            'actual_uniform_filling_supremum_bound_results.json'))
    args = parser.parse_args()
    riesz = riesz_checks()
    chebyshev = chebyshev_checks()
    original, compressed = physical_and_compressed(args.repo.resolve())
    imports = ['audit_actual_spectral_total_derivative_source.py',
               'audit_actual_small_circle_polynomial_face_insertion.py',
               'audit_actual_braided_two_cut_source_adapter.py',
               'audit_actual_nc_morse_graph_first_normal_source_reduction.py']
    result = dict(status='passed', arithmetic=dict(cyclotomic='Exact rational quotient fields',
                  physical='Exact finite fields; primes recorded for each level'),
                  riesz=riesz, chebyshev=chebyshev,
                  original_physical_matrices=original, compressed_original_source=compressed,
                  dependencies={name:hashlib.sha256((args.repo/'experiments'/name).read_bytes()).hexdigest()
                                for name in imports},
                  scope=['Finite algebraic identities, both parities, original signed crossings.',
                         'No sampled norm ratios or numerical claim of an all-level inequality.',
                         'No shared-spectral exponential bound, saddle selection, or volume theorem.'])
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(dict(status=result['status'], riesz_degrees=len(riesz),
                         riesz_modes=sum(r['derivative_mode_identities'] for r in riesz),
                         chebyshev_levels=len(chebyshev), physical=original,
                         compressed_power_identities=6*len(compressed)), indent=2))


if __name__ == '__main__':
    main()
