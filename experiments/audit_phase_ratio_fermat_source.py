#!/usr/bin/env python3
"""Pointed cyclic reflection, actual source double and phase-ratio basis."""

import json
from itertools import product
from pathlib import Path

import mpmath as mp
import numpy as np

from audit_actual_half_clock_source_dilation import original_factorial_R, word_matrix


def bar(A):
    return mp.matrix([[mp.conj(A[i, j]) for j in range(A.cols)] for i in range(A.rows)])


def frames(N, sigma, u, v):
    q = mp.exp(mp.pi*1j/N)
    qs, Qs = q**sigma, q**(2*sigma)
    D = mp.diag([Qs**a for a in range(N)])
    S = mp.zeros(N)
    for a in range(N):
        S[(a+1) % N, a] = 1
    A = mp.diag([(-qs)**a*Qs**(a*(a+1)//2) for a in range(N)])
    J = A**-1
    W = mp.matrix([[Qs**(k*a)/mp.sqrt(N) for a in range(N)] for k in range(N)])*A
    P, L = mp.zeros(N, 1), mp.zeros(1, N)
    factorial = mp.mpc(1)
    previous = mp.mpc(1)
    for a in range(N):
        if a:
            factorial *= 1-u*Qs**a
            previous *= 1-u*Qs**(a-1)
        P[a] = v**a/factorial
        L[0, a] = v**(-a)*previous
    X, Y = u*D, v*S
    Z = [X, Y**-1, -X**-1*Y]
    return qs, D, S, J, W, P, L, factorial, X, Y, Z


def near(A, B, label):
    err = mp.norm(A-B)/max(1, mp.norm(B))
    assert err < mp.mpf('1e-60'), (label, err)


def local_case(N, sigma, kind):
    q = mp.exp(mp.pi*1j/N)
    if kind == 'fixed_central_fermat':
        U = mp.mpc('.3', '.8')
        u, v = mp.exp(mp.log(U)/N), mp.exp(mp.log(1-U)/N)
    elif kind == 'fixed_radius_fermat':
        u = mp.mpf('1.17')*mp.exp(mp.mpf('.31')*1j)
        v = mp.exp(mp.log(1-u**N)/N)
    else:
        u = mp.mpf('.81')*mp.exp(mp.mpf('.23')*1j)
        v = mp.mpf('1.07')*mp.exp(-mp.mpf('.17')*1j)
    qs, D, S, J, W, P, L, Fd, X, Y, Z = frames(N, sigma, u, v)
    up, vp = 1/mp.conj(u), qs**-1*mp.conj(v)/mp.conj(u)
    _, Dp, Sp, Jp, Wp, Pp, Lp, Fdp, Xp, Yp, Zp = frames(N, sigma, up, vp)
    B, Bp = mp.eye(N)-X-Y, mp.eye(N)-Xp-Yp
    near(J*bar(J), mp.eye(N), 'antiinvolution')
    near(Pp, J*bar(P), 'right source including root normalizer')
    near(Lp, bar(L)*D**-1*J**-1, 'left source clock')
    near(Bp*J, -J*bar(X)**-1*bar(B), 'cleared operator reflection')
    near(J*bar(W)*bar(J), W**-1, 'pointed dihedral identity')
    near(Pp.H*Pp, P.H*P, 'right norm')
    near(Lp*Lp.H, L*L.H, 'left norm')
    Delta, Deltap = 1-u**N-v**N, 1-up**N-vp**N
    assert abs(Deltap+mp.conj(Delta)/mp.conj(u)**N) < mp.mpf('1e-60')*max(1, abs(Deltap))
    e0 = mp.zeros(N, 1)
    e0[0] = 1
    near(B*(Fd*P), Delta*e0, 'full polynomial source')
    near(Fdp*Pp, mp.conj(u)**(-(N-1))*J*bar(Fd*P), 'polynomial Gamma')
    for a, b in [(0, 0), (1, 2), (2, 1)]:
        near(Zp[a], J*bar(Z[b])**-1*J**-1, 'inverse reflected face')
    C = mp.matrix([[mp.mpc(i+1, j-1)/(N+1) for j in range(N)] for i in range(N)])
    near(bar(L*C*P), Lp*D*(J*bar(C)*J**-1)*Pp, 'paired scalar/co-source')
    f = mp.matrix([mp.mpc(a+1, 1-a)/(N+1) for a in range(N)])
    eta = B*f
    near(Bp*J*bar(f), -J*bar(X)**-1*bar(eta), 'full inhomogeneous packet')
    assert abs(J[N-1, N-1]+qs) < mp.mpf('1e-60')
    if kind != 'off_fermat':
        rho_u, rho_v = qs*v/u, 1/u
        _, _, _, _, _, Pr, _, _, _, _, _ = frames(N, sigma, rho_u, rho_v)
        c = (W*P)[0]
        near(W*P, c*Pr, 'actual pointed quad source')
        hr_u, hr_v = 1/mp.conj(rho_u), qs**-1*mp.conj(rho_v)/mp.conj(rho_u)
        _, _, _, _, _, Phr, _, _, _, _, _ = frames(N, sigma, hr_u, hr_v)
        ch = (W*Phr)[0]
        assert abs(ch*mp.conj(c)-1) < mp.mpf('1e-60')
    return {'N': N, 'sigma': sigma, 'parameter_scope': kind,
            'source_cosource_Gamma_and_current': True, 'pointed_dihedral': True}


def bell_case(N):
    q, Q = mp.exp(mp.pi*1j/N), mp.exp(2*mp.pi*1j/N)
    U = mp.mpc('.3', '.8')  # A Frobenius center, not a fixed geometric radius.
    u, v = mp.exp(mp.log(U)/N), mp.exp(mp.log(1-U)/N)
    _, _, _, _, _, P, _, _, _, _, _ = frames(N, -1, u, v)
    c = [[mp.fsum(Q**(-r*a)*P[a]*mp.conj(P[(s-a) % N]) for a in range(N))/mp.sqrt(N)
          for r in range(N)] for s in range(N)]
    worst, minimum = mp.mpf(0), mp.inf
    spin = {'q_to_d': mp.mpf(0), 'opposite': mp.mpf(0)}
    counts = {0: 0, N: 0, 2*N: 0}
    for s, r in product(range(N), repeat=2):
        num = 1-(v/mp.conj(v))*Q**(-r)
        den = u-(v/mp.conj(v))*mp.conj(u)*Q**(s-r)
        err = abs(den*c[s][(r+1) % N]-num*c[s][r])/max(1, abs(c[s][r]), abs(c[s][(r+1) % N]))
        assert err < mp.mpf('1e-60')
        assert abs(c[s][r]) > mp.mpf('1e-65')
        minimum, worst = min(minimum, abs(c[s][r])), max(worst, err)
        total = ((-s) % N)+r+((s-r) % N)
        counts[total] += 1
        key = 'opposite' if total == N else 'q_to_d'
        spin[key] += abs(c[s][r])**2
    source_norm = mp.fsum(abs(P[a])**2 for a in range(N))**2
    assert abs(sum(spin.values())-source_norm)/source_norm < mp.mpf('1e-60')
    assert all(value > 0 for value in spin.values())
    assert counts[0] == 1
    assert counts[2*N] == (N-1)*(N-2)//2
    return {'N': N, 'all_joint_source_coefficients_nonzero': True,
            'minimum_coefficient_modulus': mp.nstr(minimum, 12),
            'cyclic_source_recurrence_error': mp.nstr(worst, 8),
            'positive_halfphase_counts': {str(k): value for k, value in counts.items()},
            'opposite_halfcharge_source_fraction': mp.nstr(spin['opposite']/source_norm, 18)}


def fusion(N):
    q, Q = np.exp(np.pi*1j/N), np.exp(2*np.pi*1j/N)
    x = q**(N-1)
    F = [1+0j]
    for a in range(1, N):
        F.append(F[-1]*(1-Q**a))
    C = np.zeros((N*N, N*N), complex)
    for a, k in product(range(N), repeat=2):
        for u in range(a+1):
            v = a+k-u
            if v < N:
                C[u*N+v, a*N+k] = x**(u-a)*F[a]*F[v]/(F[a-u]*F[k])
    return C


def actual_plat(N, bridges, word):
    q, Q = np.exp(np.pi*1j/N), np.exp(2*np.pi*1j/N)
    d, x = N-1, q**(N-1)
    C = fusion(N)
    G = np.array([[1+0j]])
    Gi = G.copy()
    for _ in range(bridges):
        G, Gi = np.kron(G, C), np.kron(Gi, np.linalg.inv(C))
    width = 2*bridges
    indices = list(product(range(N), repeat=width))
    incoming = (d, 0)*bridges
    outgoing = (d, 0)+(0, d)*(bridges-1)
    col, row = indices.index(incoming), indices.index(outgoing)
    W = word_matrix(original_factorial_R(N), N, word, width)
    B = Gi@W@G
    e = np.zeros(N**width, complex)
    e[col] = 1
    covector = np.zeros(N**width, complex)
    for j, index in enumerate(indices):
        weight = x**index[1]/N**2
        for pair in range(1, bridges):
            a, b = index[2*pair:2*pair+2]
            weight *= x**a/N if a+b == d else 0
        covector[j] = weight
    physical = covector@W@G@e
    fused = N**(1-bridges)*B[row, col]
    assert abs(physical-fused) < 2e-7*max(1, abs(physical))
    jdiag = np.array([np.prod([(-q)**(-a)*Q**(-a*(a+1)//2) for a in index])
                      for index in indices])
    assert abs(jdiag[row]-jdiag[col]) < 1e-10
    reflected = jdiag[:, None]*B.conjugate()/jdiag[None, :]
    scalar_reflected = N**(1-bridges)*reflected[row, col]
    assert abs(scalar_reflected-physical.conjugate()) < 2e-7*max(1, abs(physical))
    return {'N': N, 'bridges': bridges, 'signed_word': word,
            'original_full_marked_scalar': [float(physical.real), float(physical.imag)],
            'full_Cartan_source_and_reflected_double': True}


def main():
    mp.mp.dps = 90
    data = {'status': 'PASS',
            'local_packets': [local_case(N, sigma, kind) for N in [2, 3, 4, 5, 7, 8]
                              for sigma in [1, -1]
                              for kind in ['fixed_central_fermat', 'fixed_radius_fermat', 'off_fermat']],
            'joint_spectral_source': [bell_case(N) for N in range(2, 13)],
            'original_plats': [actual_plat(N, 2, word) for N in [2, 3, 4]
                               for word in [[2], [2, 2, 2], [2, -2, 2], [-2, -2, -2]]]
                              +[actual_plat(2, 3, [2, 4])],
            'scope': ('Source-exact reflection and explicit phase-ratio source; '
                      'no geometric edge character or positive-angle majorant is asserted.')}
    Path(__file__).with_name('phase_ratio_fermat_source_results.json').write_text(
        json.dumps(data, indent=2)+'\n')
    print('PASS',len(data['local_packets']),'reflected source/current packets;',
          len(data['joint_spectral_source']),'joint spectral sources;',
          len(data['original_plats']),'original full-marked signed plats')


if __name__ == '__main__':
    main()
