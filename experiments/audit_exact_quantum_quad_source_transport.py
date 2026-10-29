#!/usr/bin/env python3
"""Exact finite quad transport, actual two-head sewing, and retained source."""

import json
from pathlib import Path

import mpmath as mp
import numpy as np
import sympy as sp

from audit_actual_crossing_euler_completion import actual_data
from audit_actual_peripheral_fusion import inverse_mod
from audit_actual_two_cut_ports import partial, word_matrix
from audit_standard_face_gluing import configuration, FaceFrames


def matprod(p, *factors):
    out = np.eye(len(factors[0]), dtype=np.int64)
    for factor in reversed(factors):
        out = factor@out % p
    return out


def omega(N, p, Q, u, v):
    out = [1]
    for n in range(1, N):
        out.append(out[-1]*v*pow(1-u*pow(Q, n, p), -1, p) % p)
    return np.array(out, dtype=np.int64)


def fourier(N, p, q):
    Q, gamma = q*q % p, -q % p
    return np.array([[pow(gamma, n, p)*pow(Q, k*n+n*(n+1)//2, p) % p
                      for n in range(N)] for k in range(N)], dtype=np.int64)


def quad_case(N):
    cfg, B = configuration(N)
    p, Q, q = cfg.p, cfg.Q, cfg.q
    W = fourier(N, p, q)
    Wi = inverse_mod(W, p)
    Z = np.diag([pow(Q, n, p) for n in range(N)]).astype(np.int64)
    S = np.zeros((N, N), dtype=np.int64)
    for n in range(N):
        S[(n+1) % N, n] = 1
    Zi = inverse_mod(Z, p)
    assert np.array_equal(matprod(p, W, Zi, Wi), S)
    assert np.array_equal(matprod(p, W, Zi, S, Wi), (-q)*Z % p)
    cube = matprod(p, W, W, W)
    scalar = N*sum(pow(-q, n, p)*pow(Q, n*(n+1)//2, p) for n in range(N)) % p
    assert scalar and np.array_equal(cube, scalar*np.eye(N, dtype=np.int64) % p)
    frames = FaceFrames(cfg, B)
    sources = []
    for f in ((0, 1, 2), (0, 2, 3), (1, 2, 3), (2, 0, 3)):
        G, u, v, phi = frames.data(f)
        source = omega(N, p, Q, u, v)
        assert np.array_equal(G[:, 0], source)
        original = (u, v)
        coefficient_product = 1
        for _ in range(3):
            u1, v1 = q*v*pow(u, -1, p) % p, pow(u, -1, p)
            assert (pow(u1, N, p)+pow(v1, N, p)) % p == 1
            target = omega(N, p, Q, u1, v1)
            transformed = W@omega(N, p, Q, u, v) % p
            coefficient = int(transformed[0])
            assert coefficient and np.array_equal(transformed, coefficient*target % p)
            coefficient_product = coefficient_product*coefficient % p
            u, v = u1, v1
        assert (u, v) == original and coefficient_product == scalar
        # Actual bilinear cap, with both inverse frames retained.
        M = frames.pairing(f)
        Mt = matprod(p, Wi.T, M, Wi)
        left, right = W@source % p, W@np.arange(1, N+1, dtype=np.int64) % p
        assert int(left@Mt@right) % p == int(source@M@np.arange(1, N+1, dtype=np.int64)) % p
        sources.append(dict(face=list(f), quad_scalar_product=coefficient_product))
    # The actual one-head wall and both original cut normalizations.
    J = S.copy(); J[0, N-1] = 0
    P0 = np.diag([1]+[0]*(N-1)).astype(np.int64)
    P = matprod(p, W, P0, Wi)
    assert np.array_equal(P, np.ones((N, N), dtype=np.int64)*pow(N, -1, p) % p)
    A = matprod(p, W, S, Wi)
    assert np.array_equal(matprod(p, W, J, Wi), (np.eye(N, dtype=np.int64)-P)@A % p)
    pcol = W[:, 0]
    ell = np.ones(N, dtype=np.int64)@Wi % p
    assert int(ell@P@pcol) % p == 1
    E = np.ones((N, N), dtype=np.int64)*pow(N, -1, p) % p
    Et = matprod(p, W, E, Wi)
    assert int(np.trace(Et@P)) % p == pow(N, -1, p)
    return dict(N=N, field=p, faces=sources, exact_original_wall_source=1)


def sewing_case(N):
    data = actual_data(N, 1)
    p, q, x = data[:3]
    Q = q*q % p
    S = np.zeros((N, N), dtype=np.int64)
    for n in range(N):
        S[(n+1) % N, n] = 1
    Jp = S.copy(); Jp[0, N-1] = 0
    Jm = Jp.T
    V0, V1 = np.zeros((N*N, N), dtype=np.int64), np.zeros((N*N, N), dtype=np.int64)
    for k in range(N):
        V0[k, k] = 1
        V1[((k+1) % N)*N+N-1, k] = 1
    F = [1]
    for n in range(1, N):
        F.append(F[-1]*(1-pow(Q, n, p)) % p)
    u = [pow(c, -1, p) for c in F]
    v = [pow(-1, n, p)*pow(Q, n*(n-1)//2, p)*u[n] % p for n in range(N)]
    rows = []
    for phase in (1, pow(Q, -1, p)):
        a = phase*pow(x, -1, p) % p
        A, T = a*np.kron(S, S.T) % p, a*np.kron(Jp, Jm) % p
        Ai = inverse_mod(A, p)
        for t in range(2, min(p, 30)):
            if (pow(t, N, p)-pow(a, N, p)) % p == 0:
                continue
            RA = inverse_mod(t*np.eye(N*N, dtype=np.int64)-A, p)
            RT = inverse_mod(t*np.eye(N*N, dtype=np.int64)-T, p)
            z = a*pow(t, -1, p) % p
            C01 = np.diag([pow(z, N-k-1, p) for k in range(N)])
            C10 = np.diag([pow(z, k+1, p) for k in range(N)])
            rebuilt = (RA-matprod(p, RA, V0, V0.T, A, RA)-matprod(p, RA, V1, V1.T, A, RA)
                       +matprod(p, RA, V0, C01, V1.T, A, RA)+matprod(p, RA, V1, C10, V0.T, A, RA)) % p
            assert np.array_equal(rebuilt, RT)
        # Residue of the TWO cross sectors, computed from the ordinary
        # Taylor series RA=-sum_r t^r A^(-r-1); bulk/diagonal have no pole.
        inverse_powers = [np.eye(N*N, dtype=np.int64)]
        for n in range(1, N+1):
            inverse_powers.append(inverse_powers[-1]@Ai % p)
        for coeff in (u, v):
            residue = np.zeros((N*N, N*N), dtype=np.int64)
            for k in range(N):
                for left, right, degree in ((k, ((k+1) % N)*N+N-1, N-k-1),
                                            (((k+1) % N)*N+N-1, k, k+1)):
                    for d in range(degree):
                        for r in range(degree-d):
                            s = degree-1-d-r
                            value = coeff[d]*pow(a, degree, p) % p
                            residue = (residue+value*np.outer(inverse_powers[r+1][:, left], inverse_powers[s][right, :])) % p
            expected, power = np.zeros_like(T), np.eye(N*N, dtype=np.int64)
            for c in coeff:
                expected = (expected+c*power) % p
                power = power@T % p
            assert np.array_equal(residue, expected)
        rows.append(dict(a=a, cyclic_central_factor=pow(a, N, p), two_cross_periods_checked=True))
    return dict(N=N, field=p, transfers=rows)


def whole_word(N, strands, word):
    data = actual_data(N, 1)
    p, q, _, _, pivot, plus, minus, twist, dimension, _ = data
    W, Wi = fourier(N, p, q), None
    Wi = inverse_mod(W, p)
    H, Hi = np.kron(W, W), np.kron(Wi, Wi)
    rp, rm = matprod(p, H, plus, Hi), matprod(p, H, minus, Hi)
    original = word_matrix(word, plus, minus, strands, N, p)
    transformed = word_matrix(word, rp, rm, strands, N, p)
    G = matprod(p, W, np.diag(pivot), Wi)
    if strands == 2:
        cut = np.einsum('ij,cjai->ca', G, transformed.reshape((N,)*4)) % p
    else:
        cut = np.einsum('ij,kl,cjlaik->ca', G, G, transformed.reshape((N,)*6)) % p
    old_cut = partial(original, pivot, strands, N, p)
    assert np.array_equal(cut, matprod(p, W, old_cut, Wi))
    E = np.ones((N, N), dtype=np.int64)*pow(N, -1, p) % p
    Et = matprod(p, W, E, Wi)
    scalar = int(np.trace(Et@cut)) % p
    assert scalar == int(old_cut.sum())*pow(N, -1, p) % p
    writhe = sum(1 if letter > 0 else -1 for letter in word)
    return dict(N=N, strands=strands, word=list(word),
                original_full_period=scalar*dimension*pow(twist, -writhe, p) % p)


def parameter_obstruction():
    w = sp.symbols('w')
    orbit = [w, 1-1/w, 1/(1-w)]
    expected = [w*w+w-1, w*w-w-1, w*w-3*w+1, 3*w*w-3*w+1]
    numerators = []
    for s in orbit:
        for target in orbit:
            numerator = sp.factor(sp.together(w*(1-s)/(w-1)-target).as_numer_denom()[0])
            remainder = sp.Poly(numerator, w)
            for factor in (w, w-1, *expected):
                while remainder.degree() and sp.rem(remainder, sp.Poly(factor, w)).is_zero:
                    remainder = sp.quo(remainder, sp.Poly(factor, w))
            assert remainder.degree() == 0
            numerators.append(str(numerator))
    return dict(exact_nine_comparisons=numerators, upper_half_plane_exception='1/2+i/(2sqrt(3))')


def actual_cap_pole_witness():
    t, I = sp.symbols('t'), sp.I
    S = sp.Matrix([[0, 1], [1, 0]])
    Jp = sp.Matrix([[0, 0], [1, 0]])
    A, T = I*sp.kronecker_product(S, S), I*sp.kronecker_product(Jp, Jp.T)
    V0, V1 = sp.zeros(4, 2), sp.zeros(4, 2)
    for k in range(2):
        V0[k, k] = 1
        V1[((k+1) % 2)*2+1, k] = 1
    RA, RT = (t*sp.eye(4)-A).inv(), (t*sp.eye(4)-T).inv()
    cross = RA*(V0*sp.diag(I/t, 1)*V1.T+V1*sp.diag(I/t, -1/t**2)*V0.T)*A*RA
    # Exact actual balanced fusion, retaining its factorial diagonal.
    C = sp.Matrix([[1, 0, 0, 0], [0, 1, -2*I, 0], [0, 0, 2, 0], [0, 0, 0, 2]])
    def cap(B):
        B = C*B*C.inv()
        return sp.factor(sum(((-I, I)[k])*B[2*c+k, 2*a+k]
                             for a in range(2) for c in range(2) for k in range(2))/2)
    original, sewn = cap(RT), cap(cross)
    assert sp.simplify(original-2*I/t**2) == 0
    assert sp.simplify(sewn+2*I*(t-1)*(t+1)/(t**2*(t**2+1)**2)) == 0
    poles = []
    for pole in (I, -I):
        regular = sp.cancel((t-pole)**2*sewn)
        coefficient = sp.simplify(regular.subs(t, pole))
        assert coefficient == I
        simple = sp.simplify(sp.diff(regular, t).subs(t, pole))
        residue = sp.simplify(simple/sp.sqrt(1+pole)-coefficient/(2*(1+pole)**sp.Rational(3, 2)))
        expected = ((-9-I)/(4*sp.sqrt(1+I)) if pole == I else (9-I)/(4*sp.sqrt(1-I)))
        assert sp.simplify(residue-expected) == 0 and residue != 0
        poles.append(dict(pole=str(pole), double_pole_coefficient=str(coefficient),
                          full_inverse_D_residue=str(expected)))
    return dict(original_cap=str(original), cross_cap=str(sewn), source_visible_cyclic_poles=poles)


def balancing_audit():
    out = []
    for N in (2, 3, 7, 16):
        for h in range(1, N+1):
            s = mp.mpf('0.7')
            logz = -s/N+mp.mpf('0.4')*1j
            z = mp.exp(logz)
            C = mp.matrix([[1, -mp.exp((N-h)*logz)], [-mp.exp(h*logz), 1]])
            B = mp.diag([mp.exp((N-2*h)*logz/4), mp.exp((2*h-N)*logz/4)])
            balanced = B**-1*C*B
            expected = mp.matrix([[1, -mp.exp(N*logz/2)], [-mp.exp(N*logz/2), 1]])
            assert max(abs(balanced[i,j]-expected[i,j]) for i in range(2) for j in range(2)) < mp.mpf('1e-70')
            cond = max(abs(B[0,0]), abs(B[1,1]))/min(abs(B[0,0]), abs(B[1,1]))
            assert cond <= mp.exp(s/2)*(1+mp.mpf('1e-70'))
        out.append(dict(N=N, all_h_balanced=True, condition_bound=float(mp.exp(s/2))))
    return out


def complex_scalars():
    mp.mp.dps = 85
    out = []
    for N in (12, 24, 48, 96):
        Q, q = mp.exp(2j*mp.pi/N), mp.exp(1j*mp.pi/N)
        z = (1+mp.sqrt(3)*1j)/2
        u, v = mp.exp(mp.log(z)/N), mp.exp(mp.log(1-z)/N)
        def sequence(a, b):
            seq = [mp.mpc(1)]
            for n in range(1, N):
                seq.append(seq[-1]*b/(1-a*Q**n))
            return seq
        f, g = sequence(u, v), sequence(q*v/u, 1/u)
        c = sum((-q)**n*Q**(n*(n+1)//2)*f[n] for n in range(N))/mp.sqrt(N)
        ratio = mp.sqrt(sum(abs(t)**2 for t in f)/sum(abs(t)**2 for t in g))
        assert abs(abs(c)/ratio-1) < mp.mpf('1e-55')
        out.append(dict(N=N, source_coefficient_abs=float(abs(c)), log_abs_over_logN=float(mp.log(abs(c))/mp.log(N))))
    return out


def main():
    mp.mp.dps = 85
    quad = [quad_case(N) for N in (2, 3, 4, 5, 6, 9)]
    sewing = [sewing_case(N) for N in range(2, 8)]
    words = [whole_word(N, strands, word) for N in (2, 3, 4)
             for strands, word in ((2, (1, 1, 1)), (3, (1, -2, 1, -2)))]
    result = dict(status='PASS', quad_cases=quad, sewing_cases=sewing, whole_original_words=words,
                  source_parameter_obstruction=parameter_obstruction(), complex_source_scalars=complex_scalars(),
                  actual_original_cap_pole_witness=actual_cap_pole_witness(), balancing=balancing_audit(),
                  scope='Exact quad/source and two-head cyclic sewing; no original geometric intersection or volume lower bound claimed.')
    Path(__file__).with_name('exact_quantum_quad_source_transport_results.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(dict(status='PASS', quad_levels=len(quad), sewing_levels=len(sewing), original_signed_words=len(words))))


if __name__ == '__main__':
    main()
