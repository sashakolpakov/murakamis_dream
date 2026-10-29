#!/usr/bin/env python3
"""Exact projected Cartan kernel; retain orbital aliases and source normals."""

import json
from pathlib import Path

import mpmath as mp
import numpy as np
import sympy as s

from audit_actual_two_cut_ports import balanced_data, coproduct


def poly_product_linear(coefficients, c, prime):
    out = [0] * (len(coefficients) + 1)
    for k, value in enumerate(coefficients):
        out[k] = (out[k] + value) % prime
        out[k+1] = (out[k+1] - c*value) % prime
    return out


def original_case(N):
    prime, eta, q, E, F, K, pivot, R, Rminus = balanced_data(N)
    d, Q, x = N-1, q*q % prime, int(K[0, 0])
    rho = (q-pow(q, -1, prime)) % prime
    Ec = rho*rho*E % prime
    E2, F2, _ = coproduct(Ec, F, K, 2, N, prime)
    Et, Ft, _ = coproduct(Ec, F, K, 3, N, prime)
    ids = [u*N+d-u for u in range(N)]
    high = [u*N for u in ids]
    fac = [1]
    for a in range(1, N):
        fac.append(fac[-1]*(1-pow(Q, a, prime)) % prime)
    seed = np.zeros((N*N, N), dtype=np.int64)
    seed[ids, np.arange(N)] = 1
    H = np.zeros((N**3, N), dtype=np.int64)
    power = seed.copy()
    for c in range(N):
        H[c::N, :] = pow(-x*Q, c, prime)*pow(fac[c], -1, prime)*power % prime
        power = E2@power % prime
    D = H.copy()
    for _ in range(d):
        D = Ft@D % prime
    D = D*pow(fac[d], -1, prime) % prime
    kappa = int(R[0, 0])
    L = R[np.ix_(ids, ids)]*pow(kappa, -1, prime) % prime

    RR = np.zeros((N, N), dtype=np.int64)
    alias_count = 0
    for i in range(N):
        for j in range(N):
            value = sum(fac[a]**2*pow(fac[a-i]*fac[a-j] % prime, -1, prime)
                        for a in range(max(i, j), N)) % prime
            polynomial = [1]
            for n in range(1-i, 1):
                polynomial = poly_product_linear(polynomial, pow(Q, n, prime), prime)
            for n in range(1-j, 1):
                polynomial = poly_product_linear(polynomial, pow(Q, n, prime), prime)
            alias = polynomial[N] if len(polynomial) > N else 0
            assert value == N*(1+alias) % prime
            if i+j < N:
                assert value == N % prime
            alias_count += bool(alias)
            RR[i, j] = value

    for t in [1, 2, prime-1, Q]:
        C = np.diag([pow(t, j % N, prime) for j in range(N*N)])
        Nt = np.zeros((N, N), dtype=np.int64)
        ep, fp = np.eye(N*N, dtype=np.int64), np.eye(N*N, dtype=np.int64)
        for k in range(N):
            scalar = (pow(x, k, prime)*pow(Q, k*(k+1)//2, prime)
                      *pow(fac[k]**2 % prime, -1, prime)) % prime
            Nt = (Nt+scalar*(ep@C % prime@fp % prime)[np.ix_(ids, ids)]) % prime
            ep, fp = ep@E2 % prime, F2@fp % prime
        # Independent original triple-head definition, before summing pair powers.
        diagonal = np.array([pow(t, (j//N) % N, prime) for j in range(N**3)])
        raised = diagonal[:, None]*D % prime
        for _ in range(d):
            raised = Et@raised % prime
        actual = raised[high, :]*pow(pow(-1, d, prime)*N % prime, -1, prime) % prime
        assert np.array_equal(Nt@L % prime, actual)
        if t == 1:
            assert np.array_equal(actual, np.eye(N, dtype=np.int64))
        factored = np.zeros((N, N), dtype=np.int64)
        for i in range(N):
            for j in range(N):
                SS = sum(pow(t*pow(Q, i+j-d, prime) % prime, a, prime)
                         *fac[d-j+a]**2*pow(fac[a]*fac[a+i-j] % prime, -1, prime)
                         for a in range(max(0, j-i), j+1)) % prime
                scalar = (pow(x, j-i, prime)*pow(Q, i*(i-j), prime)
                          *pow(t, d-j, prime)
                          *pow(fac[j]*fac[d-j]*fac[i]*fac[d-i] % prime, -1, prime)) % prime
                factored[i, j] = scalar*int(RR[i, j])*SS % prime
        assert np.array_equal(Nt, factored)

    # Exact actual prefix source, including both original crossing scalars.
    I = np.eye(N, dtype=np.int64)
    R2 = (np.kron(I, R)@H % prime)[high, :]
    Rm2 = (np.kron(I, Rminus)@H % prime)[high, :]
    cup = np.array([N*pow(x, j-d, prime) % prime for j in range(N)], dtype=np.int64)
    ed = np.zeros(N, dtype=np.int64)
    ed[d] = 1
    assert np.array_equal(Rm2@cup % prime, N*pow(kappa, -1, prime)*ed % prime)
    squared = L@L % prime@ed % prime
    expected = []
    for j in range(N):
        value = sum(pow(-1, v, prime)*pow(Q, v*(v+1)//2-j*v, prime)
                    *pow(fac[j-v]*fac[v]**3 % prime, -1, prime)
                    for v in range(j+1)) % prime
        expected.append(N*N*pow(x, j-d, prime)*fac[j]
                        *pow(fac[d-j], -1, prime)*value % prime)
    assert np.array_equal(squared, np.array(expected, dtype=np.int64))
    ell = np.array([pow(x, -j, prime)*pow(Q, -j, prime)*pow(N, -1, prime) % prime
                    for j in range(N)], dtype=np.int64)
    terminal_row = ell@R2 % prime@R2 % prime
    expected_row = np.array([pow(x*Q % prime, j-d, prime)*pow(N, -1, prime) % prime
                             for j in range(N)], dtype=np.int64)
    assert np.array_equal(terminal_row, expected_row)
    return {'N': N, 'full_input_phases': 4, 'all_orbital_alias_entries': N*N,
            'nonzero_alias_entries': int(alias_count), 'literal_source_and_cap': True}


def rational_graph_checks():
    J, z, t, I, S = s.symbols('J z t I S', nonzero=True)
    jp, zp = J*(1+z)/(t+z), z/t
    jacobian = s.factor(J*z/(jp*zp)*s.det(s.Matrix([[s.diff(jp, J), s.diff(jp, z)],
                                                  [s.diff(zp, J), s.diff(zp, z)]])))
    assert jacobian == 1
    X = -(1-J)**2*(1+z)**2/z
    Y = (J-1)**2*(1+z)/J
    Z = (J-1)**2*(1+z)/(J*z)
    assert s.factor((X+Y+Z)**2+X*Y*Z) == 0
    substitute = {J: jp, z: zp}
    Xp, Yp, Zp = [s.factor(v.subs(substitute, simultaneous=True)) for v in [X, Y, Z]]
    lam = s.factor((X+Y+t*Z)**2/(t*(X+Y+Z)**2))
    assert all(s.factor(a-b) == 0 for a, b in [(Xp, lam*X), (Yp, lam*Y), (Zp, lam*t*Z)])
    assert s.factor((zp/(jp*(1+zp)))-(z/(J*(1+z)))) == 0

    # Exact derivative data of the alias coefficient phase.
    w = (2*I*J-I-J)/(I*J-1)
    assert s.factor((1-w)**2-(1-w/I)*(1-w/J)) == 0
    R = w/J
    V = S*I/J
    pin, pout = (1-S)/(S*(1-R)), V*(1-w/I)/(1-V)
    assert s.factor(pin.subs(S, 1/R)+1) == 0
    assert s.factor(pout.subs(S, 1/R)+1) == 0
    return {'constant_channel_symplectic': True, 'actual_cubic_and_clock': True,
            'alias_saddle_and_phase_one_degeneracy': True}


def exact_source_cap_intersection():
    m, t, a = s.symbols('m t a')
    R = (m**12-3*m**11+5*m**10-9*m**9+9*m**8+2*m**7-9*m**6
         +2*m**5+9*m**4-9*m**3+5*m**2-3*m+1)
    f = (50*m**11-126*m**10+181*m**9-343*m**8+267*m**7+295*m**6
         -332*m**5-88*m**4+397*m**3-214*m**2+69*m-24)/107
    P = (m**3*t**3-3*m**3*t**2+3*m**3*t-m**3-3*m**2*t**3+8*m**2*t**2
         -7*m**2*t+2*m**2+3*m*t**3-5*m*t**2+3*m*t-m-t**3)
    def reduced_numerator(expr):
        return s.rem(s.cancel(expr).as_numer_denom()[0], R, m)
    assert reduced_numerator(P.subs(t, f)) == 0
    assert reduced_numerator(f*f.subs(m, 1/m)-1) == 0
    assert s.gcd(s.together(f-1).as_numer_denom()[0], R) == 1
    A = a**6-3*a**5-a**4+6*a**3-2*a**2+14*a-19
    assert s.Poly(A, a).count_roots(s.Rational(131, 100), s.Rational(33, 25)) == 1
    assert s.rem(m**6*A.subs(a, m+1/m), R, m) == 0
    X = (m-1)**2*(t-1)**2/t
    Y = (m-1)**2*(t-1)*(m*t-m-t)**2/(m*t)
    Z = -(m-1)**2*(t-1)*(m*m*t*t-2*m*m*t+m*m-2*m*t*t+3*m*t-m+t*t)**2/(m*t*t)
    assert reduced_numerator((Y-X*X).subs(t, f)) == 0
    assert reduced_numerator((Z+X).subs(t, f)) == 0
    assert reduced_numerator(((X+Y+Z)**2+X*Y*Z)) == 0

    mp.mp.dps = 80
    aa = mp.findroot(lambda x: x**6-3*x**5-x**4+6*x**3-2*x*x+14*x-19, (mp.mpf('1.31'), mp.mpf('1.32')))
    mm = (aa+mp.j*mp.sqrt(4-aa*aa))/2
    ff = s.lambdify(m, f, 'mpmath')
    tt = ff(mm)
    J = mm/(mm*mm-tt*(1-mm)**2)
    S = mm*J
    RR = (2*J-1)/(J*J)
    pp = (1-S)/(S*(1-RR))
    V0 = J+(1-J)**2/(J*pp)
    assert abs(J*V0**2-3*J*V0+3*J-1) < mp.mpf('1e-65')
    assert abs(abs(mm)-1)+abs(abs(tt)-1) < mp.mpf('1e-65')
    for value in [J, S, pp, V0, V0-J, 1-V0, 1-S, 1-RR]:
        assert abs(value) > mp.mpf('1e-4')
    return {'unit_unit_algebra_exact': True, 'source_saddle_regular': True,
            'm': mp.nstr(mm, 25), 't': mp.nstr(tt, 25),
            'scope': 'Resolved cap-character intersection, not a proved full normal critical lift.'}


def shrinking_phase_escape():
    m, t, w, tau, v = s.symbols('m t w tau v')
    P = (m**3*t**3-3*m**3*t**2+3*m**3*t-m**3-3*m**2*t**3+8*m**2*t**2
         -7*m**2*t+2*m**2+3*m*t**3-5*m*t**2+3*m*t-m-t**3)
    expected = w**3-w**2+2*(1+tau)*w-(1+tau)
    assert s.factor(P.subs({m: 1+w/tau, t: 1+tau})-expected) == 0
    C = w**3-w**2+2*t*w-t
    assert s.discriminant(C.subs(t, 1), w) == -23
    X = (m-1)**2*(t-1)**2/t
    Y = (m-1)**2*(t-1)*(m*t-m-t)**2/(m*t)
    Z = -(m-1)**2*(t-1)*(m*m*t*t-2*m*m*t+m*m-2*m*t*t+3*m*t-m+t*t)**2/(m*t*t)
    shift = {m: 1+w/tau, t: 1+tau}
    XX, YY, ZZ = [s.factor(a.subs(shift)) for a in [X, Y, Z]]
    cc = s.factor(((t-1)*(m+1/m-2)).subs(shift))
    assert s.factor(XX-w*w/(1+tau)) == 0
    assert s.factor(cc-w*w/(w+tau)) == 0
    assert s.rem(s.together(YY-XX*XX).as_numer_denom()[0], expected, w) == 0
    assert s.rem(s.together(ZZ+XX).as_numer_denom()[0], expected, w) == 0
    limiting = v**3-v*v+2*v-1
    assert s.rem(v*(v-1)**2-v**4, limiting, v) == 0
    assert s.rem(-v*(v*v-v+1)**2+v*v, limiting, v) == 0
    return {'exact_escaping_source_branch': str(C), 'simple_limit_discriminant': -23,
            'bounded_characters_unbounded_recorded_ratio': True,
            'scope': 'Arc endpoint escape, with its action and selected normal lift unproved.'}


if __name__ == '__main__':
    result = {'status': 'PASS', 'literal_original_modules': [original_case(N) for N in range(2, 9)],
              'critical_graph_algebra': rational_graph_checks(),
              'resolved_source_cap_intersection': exact_source_cap_intersection(),
              'shrinking_phase_escape': shrinking_phase_escape(),
              'scope': 'All-input exact kernel and two critical channels; no selected-cycle energy estimate.'}
    Path(__file__).with_name('actual_terminal_effective_cartan_kernel_results.json').write_text(json.dumps(result, indent=2)+'\n')
    print('PASS 7 complete original modules, exact orbital aliases/source/cap; symplectic cubic graph and algebraic unit/unit intersection')
