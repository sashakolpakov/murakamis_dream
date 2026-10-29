#!/usr/bin/env python3
"""Six-leaf original Newton source: exact stationary certificate and diagnostics.

The symbolic calculation certifies the complete critical point, Hessian,
Gaussian amplitude and D=N-1 offset. Finite-level source ratios are numerical
diagnostics only; they do not prove an asymptotic or complex uniformity.
"""
import json
from pathlib import Path

import mpmath as mp
import sympy as sp


def exact_stationary_certificate():
    xs = sp.symbols('x1:6', real=True)
    ts = sp.symbols('t2:6', real=True)
    coordinates = xs + ts
    cot_a = sp.sqrt(3)/2
    cots = [cot_a]*5 + [sp.sqrt(3)/6, 0, -sp.sqrt(3)/6, -cot_a]
    sine = [sp.simplify(1/sp.sqrt(1+b*b)) for b in cots]
    cosine = [sp.simplify(b*s) for b, s in zip(cots, sine)]

    def trig(argument):
        """Exact sine/cosine of pi times an integral affine wire form."""
        argument = sp.expand(argument)
        constant = argument.subs(dict.fromkeys(coordinates, 0))
        assert constant.is_integer
        result = sp.Integer((-1)**int(constant))
        for variable, s, c in zip(coordinates, sine, cosine):
            degree = sp.diff(argument, variable)
            assert degree.is_integer
            result *= (c+sp.I*s)**int(degree)
        result = sp.expand_complex(sp.expand(result))
        s, c = sp.simplify(sp.im(result)), sp.simplify(sp.re(result))
        assert s.is_positive
        return s, sp.simplify(c/s)

    # Every tuple is an actual factorial argument, multiplicity and offset.
    # The final product is forced flat: its coefficient is exactly one.
    leaves = list(xs) + [1-ts[-1]]
    offsets = [0]*5 + [-1]
    rows = []
    for leaf, offset in zip(leaves, offsets):
        rows.extend([(2*leaf, 1, 2*offset), (leaf, -4, offset)])
    gates = []
    for j in range(2, 6):
        left = xs[0] if j == 2 else ts[j-3]
        right, output = xs[j-1], ts[j-2]
        gate = [(left+right, 1, 0), (output, 1, 0),
                (left, -1, 0), (right, -1, 0),
                (output-left, -1, 0), (output-right, -1, 0),
                (left+right-output, -1, 0)]
        rows.extend(gate)
        gates.append((left, right, output))

    hessian = sp.zeros(9)
    gradient_exponentials = [sp.Integer(1)]*9
    # Six leaves and four gates each have the factor 2^(-3/2).
    amplitude = sp.Rational(1, 2**15)
    offset = sp.Integer(1)
    for argument, multiplicity, shift in rows:
        s, cotangent = trig(argument)
        vector = sp.Matrix([sp.diff(argument, v) for v in coordinates])
        hessian += multiplicity*cotangent*(vector*vector.T)
        amplitude *= s**sp.Rational(multiplicity, 2)
        offset *= (2*s)**(multiplicity*shift)
        for i in range(9):
            gradient_exponentials[i] *= (2*s)**(multiplicity*vector[i])
    gradient_exponentials = [sp.simplify(g) for g in gradient_exponentials]
    assert gradient_exponentials == [1]*9
    negative_hessian_over_pi = sp.simplify(-hessian)
    # Exact LDL pivots certify positive definiteness without numeric eigenvalues.
    _, diagonal = negative_hessian_over_pi.LDLdecomposition(hermitian=False)
    pivots = [sp.simplify(diagonal[i, i]) for i in range(9)]
    assert all(p.is_positive for p in pivots)
    determinant = sp.factor(negative_hessian_over_pi.det())
    offset = sp.simplify(offset)
    assert offset == sp.Rational(4, 3)
    amplitude = sp.simplify(amplitude*offset)
    gaussian = sp.simplify(2**sp.Rational(9, 2)*amplitude/sp.sqrt(determinant))
    assert gaussian == 3*sp.root(3, 4)/32768
    return {
        'coordinates': [str(c) for c in coordinates],
        'primitive_lattice': 'Z^9; r6=N-t5-1, all other wire offsets zero',
        'common_leaf_cotangent': str(cot_a),
        'partial_output_cotangents_j_2_to_5': [str(c) for c in cots[5:]],
        'gradient_exponentials': [str(g) for g in gradient_exponentials],
        'negative_hessian_over_pi': [[str(v) for v in row] for row in negative_hessian_over_pi.tolist()],
        'positive_LDL_pivots_over_pi': [str(p) for p in pivots],
        'determinant_over_pi_to_nine': str(determinant),
        'integer_offset_multiplier': str(offset),
        'summand_amplitude': str(amplitude),
        'gaussian_amplitude': str(gaussian),
        'N_power': '6/2-3*4/2+9/2 = 3/2',
    }, gaussian


def J(t):
    return -mp.im(mp.polylog(2, mp.exp(2j*mp.pi*t)))/(2*mp.pi)


def complete_phase():
    a = mp.atan(2/mp.sqrt(3))/mp.pi
    z = [None] + [mp.atan2(1, mp.sin(mp.pi/6)*mp.cot(j*mp.pi/6))/mp.pi
                  for j in range(1, 6)]
    g = J(2*a)-4*J(a)
    value = 6*g
    for j in range(2, 6):
        x, y, t = z[j-1], a, z[j]
        assert max(x, y) < t < x+y < 1
        value += J(x+y)+J(t)-J(x)-J(y)-J(t-x)-J(t-y)-J(x+y-t)
    assert abs(z[1]-a) < mp.mpf('1e-90')
    assert abs(z[5]+a-1) < mp.mpf('1e-90')
    return a, value


class NewtonSource:
    def __init__(self, N):
        self.N, self.D, self.M = N, N-1, (N-1)//2
        self.q = mp.exp(mp.j*mp.pi/N)
        self.kappa = mp.exp(mp.j*mp.pi*self.D*self.D/(2*N))
        self.s = [mp.mpf(1)]
        for r in range(1, N):
            self.s.append(self.s[-1]*2*mp.sin(mp.pi*r/N))
        s = self.s
        self.table = []
        for i in range(N):
            for j in range(i, N-i):
                for r in range(max(i, j), i+j+1):
                    mu = s[i+j]*s[r]/(s[i]*s[j]*s[r-i]*s[r-j]*s[i+j-r])
                    assert mu > 0
                    self.table.append((i, j, r, mu))

    def multiply(self, a, b):
        result = [mp.mpc(0)]*self.N
        for i, j, r, mu in self.table:
            product = a[i]*b[j]
            if i != j:
                product += a[j]*b[i]
            result[r] += product*mu
        return result

    def closed_flat(self, a, b):
        # mu(i,j,D)=1 for i+j=D, zero for every other pair.
        return mp.fsum(a[i]*b[self.D-i] for i in range(self.N))

    def leaves(self, h=0, include_alias=True):
        N, s = self.N, self.s
        pure = [mp.mpc(0)]*N
        for v in range(h, self.M+1):
            pure[v] = N*N*s[2*v]/(s[v]**2*s[v-h]*s[v+h])
        if include_alias and h:
            for r in range(h):
                pure[self.D-r] += (-1)**(N+h-1+r)*s[r]**2*s[h+r]/(s[2*r+1]*s[h-r-1])
        minus = []
        for r in range(N):
            minus.append(mp.fsum(pure[v]/self.kappa*(-1)**v*self.q**(-v*(r+1))
                                 *s[v]/(s[r]*s[v-r]) for v in range(r, N)))
        return {0: pure, -1: minus, 1: [mp.conj(v) for v in minus]}

    def evaluate(self, pattern, leaves):
        # Literal C((h h h)(h h h)); associative left chain checked separately.
        left = self.multiply(self.multiply(leaves[pattern[0]], leaves[pattern[1]]), leaves[pattern[2]])
        right = self.multiply(self.multiply(leaves[pattern[3]], leaves[pattern[4]]), leaves[pattern[5]])
        return self.closed_flat(left, right)


PATTERNS = [(0, 0, 0, 0, 0, 0), (-1, -1, -1, -1, -1, -1),
            (1, 1, 1, 1, 1, 1), (-1, 1, 0, -1, 1, 0),
            (-1, 0, 0, 0, 0, 0), (-1, -1, -1, 1, 1, 1)]


def finite_calibration(N, gaussian, a, F0):
    source = NewtonSource(N)
    leaves = source.leaves()
    # Independent finite Pochhammer presentation, not the same triangular sum.
    from audit_actual_odd_conway_newton_transport import complete_coefficients
    _, independent = complete_coefficients(N)
    for sign in (-1, 0, 1):
        for r, expected in enumerate(independent[sign]):
            assert abs(leaves[sign][r]-expected) <= mp.mpf('1e-65')*max(1, abs(expected))
    leading = gaussian*N**mp.mpf('1.5')*mp.exp(N*F0)
    values, rows = {}, []
    for pattern in PATTERNS:
        actual = source.evaluate(pattern, leaves)
        values[pattern] = actual
        eta = mp.exp(mp.j*mp.pi*source.D*sum(pattern)/4)
        odd_amplitude = mp.fprod(mp.sqrt(mp.sin(mp.pi*a))*mp.exp(-mp.j*sign*mp.pi*a/2)
                                for sign in pattern if sign)
        ratio = actual/(eta*odd_amplitude*leading)
        rows.append({'pattern': list(pattern),
                     'ratio_real': mp.nstr(mp.re(ratio), 24),
                     'ratio_imag': mp.nstr(mp.im(ratio), 24),
                     'N_times_absolute_relative_error': mp.nstr(N*abs(ratio-1), 24)})
    assert abs(values[PATTERNS[2]]-mp.conj(values[PATTERNS[1]])) < mp.mpf('1e-65')*abs(values[PATTERNS[1]])
    # The Hessian uses the equivalent left-associated tree, with exact closure.
    pattern = PATTERNS[3]
    chain = leaves[pattern[0]]
    for sign in pattern[1:5]:
        chain = source.multiply(chain, leaves[sign])
    chain_value = source.closed_flat(chain, leaves[pattern[5]])
    assert abs(chain_value-values[pattern]) < mp.mpf('1e-65')*abs(values[pattern])

    # Exact h=1 physical source versus transported core, retaining every alias.
    full_h1, core_h1 = source.leaves(h=1), source.leaves(h=1, include_alias=False)
    mixed_rows = []
    for pattern in (PATTERNS[0], PATTERNS[3], PATTERNS[4]):
        full, core = source.evaluate(pattern, full_h1), source.evaluate(pattern, core_h1)
        mixed_rows.append({'pattern': list(pattern), 'all_six_deficits': 1,
                           'absolute_alias_difference_over_complete_leading': mp.nstr(abs(full-core)/leading, 24),
                           'full_over_core_real': mp.nstr(mp.re(full/core), 24),
                           'full_over_core_imag': mp.nstr(mp.im(full/core), 24)})
    return {'N': N, 'precision_decimal_digits': mp.mp.dps,
            'literal_tree': 'C((h h h)(h h h))',
            'left_associated_closure_agreement': True,
            'full_leaf_Pochhammer_crosscheck': True,
            'complete_source_ratios': rows,
            'mixed_h1_alias_diagnostics': mixed_rows,
            'scope': 'Finite principal-root diagnostics only; no asymptotic inference.'}


def precision_replay():
    """Recompute actual signed sources, not rounded stored ratios."""
    values = []
    for digits in (100, 170):
        with mp.workdps(digits):
            source = NewtonSource(41)
            complete = source.leaves()
            full_h1, core_h1 = source.leaves(h=1), source.leaves(h=1, include_alias=False)
            values.append([
                source.evaluate(PATTERNS[1], complete),
                source.evaluate(PATTERNS[3], complete),
                source.evaluate(PATTERNS[4], full_h1),
                source.evaluate(PATTERNS[4], full_h1)-source.evaluate(PATTERNS[4], core_h1),
            ])
    with mp.workdps(170):
        errors = [abs(lo-hi)/abs(hi) for lo, hi in zip(*values)]
        assert max(errors) < mp.mpf('1e-65')
        return {'N': 41, 'decimal_precisions': [100, 170],
                'quantities': ['all-negative complete source', 'mixed-sign complete source',
                               'one-negative whole h=1 source', 'one-negative h=1 alias difference'],
                'relative_disagreements': [mp.nstr(error, 10) for error in errors],
                'relative_tolerance': '1e-65',
                'scope': 'Numerical cancellation/stability check, not an exact identity proof.'}


def main():
    certificate, exact_amplitude = exact_stationary_certificate()
    with mp.workdps(130):
        a, F0 = complete_phase()
        amplitude = mp.mpf(str(sp.N(exact_amplitude, 125)))
        diagnostics = []
        for N in (16, 17, 24, 25, 40, 41):
            diagnostics.append(finite_calibration(N, amplitude, a, F0))
            print(f'PASS six-leaf exact Newton checks N={N}', flush=True)
        result = {
            'status': 'PASS', 'exact_symbolic_certificate': certificate,
            'phase_and_amplitude': {'leaf_coordinate': mp.nstr(a, 55),
                                    'F0': mp.nstr(F0, 55),
                                    'pure_leading_amplitude': mp.nstr(amplitude, 55)},
            'finite_source_diagnostics': diagnostics,
            'independent_precision_replay': precision_replay(),
            'scope': 'Exact nine-dimensional stationary/Hessian/amplitude certificate; finite principal-root full-source comparisons at both parities are diagnostics, not proofs of convergence, global gap, or complex uniformity.',
        }
    Path(__file__).with_name('actual_odd_conway_six_leaf_calibration_results.json').write_text(json.dumps(result, indent=2)+'\n')
    print('PASS six-leaf symbolic certificate, 36 complete source and 18 whole mixed-source diagnostics')


if __name__ == '__main__':
    main()
