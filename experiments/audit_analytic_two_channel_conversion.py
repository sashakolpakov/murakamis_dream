#!/usr/bin/env python3
"""Exact-model audit: analytic conversion versus marked branch actions.

This is NOT an actual knot quantum recurrence or its source.
"""

import json
from pathlib import Path

import mpmath as mp


def norm(A):
    return mp.svd(A, compute_uv=False)[0]


def case(N, a, theta, power):
    with mp.workdps(max(90, N//2)):
        a, theta = mp.mpf(a), mp.mpf(theta)
        b = mp.mpf(N)**(-power)
        P = mp.eye(2)
        largest_condition = mp.mpf(0)
        for j in range(N):
            x = mp.mpf(j)/N
            alpha = mp.exp(a*(x-mp.mpf('.5')))
            beta = mp.exp(-a*(x-mp.mpf('.5'))+1j*theta)
            T = mp.matrix([[alpha, b], [0, beta]])
            S = mp.matrix([[1, b/(beta-alpha)], [0, 1]])
            Sinv = mp.matrix([[1, -b/(beta-alpha)], [0, 1]])
            assert norm(T*S-S*mp.diag([alpha, beta])) < mp.mpf('1e-70')
            largest_condition = max(largest_condition, norm(S)*norm(Sinv))
            P = T*P

        finite = b*mp.fsum(mp.exp(a*k*(N-k)/N+1j*theta*k)
                            for k in range(N))
        assert abs(P[0, 1]-finite)/max(1, abs(finite)) < mp.mpf('1e-68')
        assert abs(P[0, 0]-mp.exp(-a/2)) < mp.mpf('1e-68')
        assert abs(P[1, 1]-mp.exp(a/2+1j*N*theta)) < mp.mpf('1e-68')

        # Independent scalar second-order companion realization with
        # its literal initial source (0,b), retaining the O(1/N) shift.
        u0, u1 = mp.mpc(0), mp.mpc(b)
        for j in range(N-1):
            x = mp.mpf(j)/N
            alpha_next = mp.exp(a*(x+mp.mpf(1)/N-mp.mpf('.5')))
            beta = mp.exp(-a*(x-mp.mpf('.5'))+1j*theta)
            u0, u1 = u1, (alpha_next+beta)*u1-mp.exp(1j*theta)*u0
        assert abs(u1-finite)/max(1, abs(finite)) < mp.mpf('1e-65')

        # Integer Gaussian terms outside the physical finite interval.
        tail = b*(mp.fsum(mp.exp(a*k*(N-k)/N+1j*theta*k)
                          for k in range(-2*N, 0))
                  +mp.fsum(mp.exp(a*k*(N-k)/N+1j*theta*k)
                           for k in range(N, 3*N+1)))
        bound = b*mp.coth(a/2)
        assert abs(tail) <= bound

        fourier = (b*mp.sqrt(mp.pi*N/a)*mp.exp(a*N/4+1j*theta*N/2)
                   *mp.fsum((-1)**(m*N)
                            *mp.exp(-N*(theta-2*mp.pi*m)**2/(4*a))
                            for m in range(-8, 9)))
        assert abs(finite+tail-fourier)/max(1, abs(fourier)) < mp.mpf('1e-65')

        gamma = a/4-theta**2/(4*a)
        leading = b*mp.sqrt(mp.pi*N/a)*mp.exp(N*gamma+1j*N*theta/2)
        ratio_error = abs(finite/leading-1)
        # Complete asymptotic error includes BOTH the other Fourier
        # modes and the omitted O(1) finite-interval tails.
        kappa = mp.pi*(mp.pi-theta)/a
        assert ratio_error < (10*mp.exp(-kappa*N)
                              +2*bound/abs(leading))
        assert abs(norm(P*mp.matrix([1, 0]))-mp.exp(-a/2)) < mp.mpf('1e-68')

        # The scalar unit phase makes the 2 by 2 family determinant one.
        sample = mp.matrix([[mp.exp(a/6), b],
                            [0, mp.exp(-a/6+1j*theta)]])
        sample *= mp.exp(-1j*theta/2)
        assert abs(mp.det(sample)-1) < mp.mpf('1e-68')

        # Exact reciprocal-conjugate 4-channel extension and its
        # indefinite Hermitian metric.
        c = a
        B = mp.exp(c)*sample
        A = mp.zeros(4)
        other = (B.H)**(-1)
        for i in range(2):
            for j in range(2):
                A[i, j], A[i+2, j+2] = B[i, j], other[i, j]
        J = mp.matrix([[0, 0, 1, 0], [0, 0, 0, 1],
                       [1, 0, 0, 0], [0, 1, 0, 0]])
        assert norm(A.H*J*A-J) < mp.mpf('1e-65')

        return {"N": N, "a": str(a), "theta": str(theta),
                "coupling_power": power,
                "marked_branch_action_maximum": 0,
                "pointwise_radius_integral": mp.nstr(a/4, 16),
                "proved_product_exponent": mp.nstr(gamma, 22),
                "finite_product_rate": mp.nstr(mp.log(norm(P))/N, 22),
                "relative_leading_asymptotic_error": mp.nstr(ratio_error, 8),
                "largest_eigenbasis_condition": mp.nstr(largest_condition, 10),
                "preserved_e1_source_log_norm": mp.nstr(-a/2, 12)}


def main():
    mp.mp.dps = 100
    rows = [case(N, a, theta, power)
            for a, theta in [('2', '1'), ('3', mp.pi/2)]
            for power in [0, 1]
            for N in [31, 32, 63, 64, 127, 128, 255, 256]]
    result = {"status": "PASS", "cases": len(rows), "rows": rows,
              "scope": ("General analytic two-channel recurrence only. "
                        "Not a quantum operator or source for a knot.")}
    path = Path(__file__).with_name('analytic_two_channel_conversion_results.json')
    path.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({"status": "PASS", "cases": len(rows),
                      "last_four": rows[-4:]}, indent=2))


if __name__ == '__main__':
    main()
