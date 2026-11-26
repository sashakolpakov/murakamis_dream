#!/usr/bin/env python3
"""Check exact cap/Fourier recursion against the full original quotient.

No asymptotic data are used as proof inputs. Negative crossings are
constructed by inversion of the original positive crossing matrix.
"""

import argparse
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path

import mpmath as mp

import check_one_crossing_gaussian_window as original
from check_complete_boundary_coefficient_transport import mul


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=110)
    parser.add_argument("--output", type=Path, default=Path(
        "repro/results/research-positive-cap-fourier-recursion.json"))
    args = parser.parse_args()
    if args.precision < 80:
        parser.error("Use at least 80 decimal digits.")
    mp.mp.dps = args.precision
    tolerance = mp.mpf(10)**(-(args.precision-35))
    records = []

    def check(label, N, sign, actual, expected):
        error = abs(actual-expected)/max(1, abs(actual), abs(expected))
        if error >= tolerance:
            raise AssertionError((label, N, sign, mp.nstr(error, 20)))
        records.append({"identity": label, "N": N, "sign": sign,
                        "relative_error": mp.nstr(error, 16)})

    def matrix_check(label, N, sign, actual, expected):
        for j in range(actual.rows):
            for k in range(actual.cols):
                check(label, N, sign, actual[j, k], expected[j, k])

    for N in range(2, 11):
        M0, q0, kappa0, sine_factorial = original.original_matrix(N)
        identity = mp.eye(N)
        cap = identity[:, 0]
        S = mp.matrix([[int(k == j+1) for k in range(N)]
                       for j in range(N)])
        for sign in (1, -1):
            M = M0 if sign == 1 else M0**-1
            q = q0 if sign == 1 else mp.conj(q0)
            kappa = kappa0 if sign == 1 else mp.conj(kappa0)
            Q, D = q*q, N-1
            H = M.transpose_conj()*M
            factorial = [mp.mpc(1)]
            for j in range(1, N):
                factorial.append(factorial[-1]*(1-Q**j))
            a = [(-q)**j/factorial[j] for j in range(N)]
            b = [q**(j*j)/factorial[j] for j in range(N)]
            Ta = mp.matrix([[a[k-j] if k >= j else 0
                             for k in range(N)] for j in range(N)])
            Tb = mp.matrix([[b[k-j] if k >= j else 0
                             for k in range(N)] for j in range(N)])
            C = mp.diag(a)*Tb
            fourier = mp.matrix([[Q**(j*k)/mp.sqrt(N)
                                  for k in range(N)] for j in range(N)])
            row_phase = mp.diag([kappa*(-q)**j for j in range(N)])
            matrix_check("original Fourier factorization", N, sign,
                         M, mp.sqrt(N)*row_phase*fourier*C)
            matrix_check("positive Gram factorization", N, sign,
                         H, N*C.transpose_conj()*C)
            matrix_check("finite inverse convolutions", N, sign,
                         Ta*Tb, identity)

            factors = []
            for j in range(N):
                polynomial = [mp.mpc(1)]
                for r in range(j):
                    polynomial = mul(polynomial, [1, -Q**(-r)])
                factors.append(polynomial)
            for j in range(N):
                for k in range(N):
                    coefficient = mul(factors[j], factors[k])[j]
                    expected = (N*q**(j*j+k*k)*coefficient
                                /(factorial[j]*factorial[k]))
                    check("single coefficient Gram formula", N, sign,
                          H[j, k], expected)

            X = mp.diag([Q**j for j in range(N)])
            K = S.T*(identity-Q*X)
            Y = (identity+q**-1*S)*X
            clock = Y-q**-1*(K-q*X)*(identity-Q*Y)
            stencil = mp.zeros(N)
            for j in range(N):
                stencil[j, j] = 3*Q**j-(1+Q)*Q**(2*j)
                if j < D:
                    stencil[j, j+1] = q*Q**j*(1-Q**(j+1))
                if j:
                    stencil[j, j-1] = -q**-1*(1-Q**j)**2
            matrix_check("clock stencil", N, sign, clock, stencil)
            matrix_check("original clock intertwining", N, sign,
                         X*H, H*stencil)
            matrix_check("finite oscillator endpoint current", N, sign,
                         Ta*K*Tb, K-q*X+q**-1*b[D]*(S**D))
            matrix_check("endpoint current annihilation", N, sign,
                         (S**D)*(identity-Q*Y), mp.zeros(N))
            first = H*cap
            matrix_check("original cap scale", N, sign,
                         first, N*mp.matrix(a))
            matrix_check("cap Jacobi boundary equation", N, sign,
                         (stencil.transpose_conj()-identity)*first,
                         mp.zeros(N, 1))

            # Iterate scalar convolutions, not C*C or the Gram matrix.
            coefficient = [mp.mpc(int(j == 0)) for j in range(N)]
            literal = cap.copy()
            powers = [identity]
            for _ in range(8):
                powers.append(powers[-1]*H)
            for r in range(4):
                for j in range(N):
                    check("entire original cap vector", N, sign,
                          coefficient[j], literal[j])
                upper = [
                    mp.fsum(b[k-j]*coefficient[k] for k in range(j, N))
                    for j in range(N)]
                even = mp.fsum(abs(z)**2 for z in coefficient)
                odd = N*mp.fsum(
                    abs(upper[j])**2/sine_factorial[j]**2
                    for j in range(N))
                check("positive even cap energy", N, sign,
                      even, powers[2*r][0, 0])
                check("positive odd cap energy", N, sign,
                      odd, powers[2*r+1][0, 0])
                coefficient = [
                    N*mp.fsum(a[j-l]*upper[l]/sine_factorial[l]**2
                              for l in range(j+1))
                    for j in range(N)]
                literal = H*literal

            # Independent polynomial checks include the constant and
            # degree-N currents, using a non-cap test input.
            test = [mp.mpc(j+1, 2*j-1)/(j+2) for j in range(N)]
            shifted = [Q**j*test[j] for j in range(N)]
            upper = [mp.fsum(b[k-j]*test[k] for k in range(j, N))
                     for j in range(N)]
            upper_shifted = [
                mp.fsum(b[k-j]*shifted[k] for k in range(j, N))
                for j in range(N)]
            for j in range(N+1):
                lhs = Q**(j-1)*upper[j-1] if j else 0
                rhs = (upper_shifted[j-1] if j else 0)
                if j < N:
                    rhs += q**-1*upper_shifted[j]
                if j == 0:
                    rhs -= q**-1*upper_shifted[0]
                check("upper projection clock current", N, sign, lhs, rhs)
            lower = mul(a, test)[:N]
            lower_shifted = mul(a, shifted)[:N]
            for j in range(N+1):
                lhs = Q**j*lower[j] if j < N else 0
                rhs = lower_shifted[j] if j < N else 0
                if j:
                    rhs += q*lower_shifted[j-1]
                if j == N:
                    rhs -= q*lower_shifted[D]
                check("lower projection clock current", N, sign, lhs, rhs)
            for j in range(N):
                lhs = (2-Q**j-Q**(-j))*test[j]/sine_factorial[j]**2
                rhs = test[j]/sine_factorial[j-1]**2 if j else 0
                check("coefficient weight clock identity", N, sign, lhs, rhs)

            skew = M-M.T
            W = skew.transpose_conj()*skew
            matrix_check("positive skew crossing reduction", N, sign,
                         W, H+H**-1-2*identity)
            tau = [mp.mpc(1)]
            wp = identity
            for m in range(1, 8):
                wp = wp*W
                tau.append(wp[0, 0])
            for m in range(8):
                expected = mp.fsum(
                    math.comb(m+k, 2*k)*tau[k] for k in range(m+1))
                check("positive triangular moment identity", N, sign,
                      powers[m][0, 0], expected)
            difference = (H-W)*cap
            check("first cap vector error", N, sign,
                  mp.fsum(abs(z)**2 for z in difference), N)

            half = N//2
            plus, minus = mp.zeros(N, N-half), mp.zeros(N, half)
            for j in range(half):
                plus[j, j] = plus[D-j, j] = 1/mp.sqrt(2)
                minus[j, j] = 1/mp.sqrt(2)
                minus[D-j, j] = -1/mp.sqrt(2)
            if N % 2:
                plus[half, half] = 1
            block = plus.T*skew*minus
            explicit = mp.zeros(N-half, half)
            for j in range(half):
                for k in range(half):
                    explicit[j, k] = skew[j, k]+M[D-k, j]
            if N % 2:
                for k in range(half):
                    explicit[half, k] = mp.sqrt(2)*M[half, k]
            matrix_check("original parity crossing block", N, sign,
                         block, explicit)
            Wplus, Wminus = plus.T*W*plus, minus.T*W*minus
            matrix_check("positive parity plus block", N, sign,
                         Wplus, block.conjugate()*block.T)
            matrix_check("positive parity minus block", N, sign,
                         Wminus, block.transpose_conj()*block)
            wp, wm, full = mp.eye(N-half), mp.eye(half), identity
            for m in range(8):
                check("actual plus cap split", N, sign,
                      wp[0, 0], full[0, 0]+full[0, D])
                check("actual minus cap split", N, sign,
                      wm[0, 0], full[0, 0]-full[0, D])
                wp, wm, full = wp*Wplus, wm*Wminus, full*W
            if N >= 3:
                actual = mp.im(H[0, 1]*H[1, 2]*H[2, 0])
                expected = (-sign*N**3*mp.sin(mp.pi/N)
                            /(sine_factorial[1]**4*sine_factorial[2]))
                check("exact low-color Gram cycle", N, sign,
                      actual, expected)

    n0, s0 = Fraction(64), Fraction(1, 10)
    cycle_relative_bound = (
        65/(4*n0)+75*s0**2/(2*n0)+39*s0/n0
        +150*s0**3/n0**2+156*s0**2/n0**2
        +360*s0**4/n0**2+1440*s0**5/n0**3)
    assert cycle_relative_bound < Fraction(1, 3)

    root = Path(__file__).resolve().parents[1]
    paths = [
        Path(__file__).resolve(),
        root/"experiments/check_one_crossing_gaussian_window.py",
        root/"experiments/check_complete_boundary_coefficient_transport.py",
    ]
    result = {
        "status": "passed",
        "scope": "exact full original cap recursion and finite endpoint currents",
        "precision_decimal_digits": args.precision,
        "levels": list(range(2, 11)),
        "signs": [1, -1],
        "checks": len(records),
        "max_relative_error": max(
            (item["relative_error"] for item in records), key=mp.mpf),
        "rational_cycle_bound": {
            "N_at_least": 64,
            "s_at_most": str(s0),
            "relative_correction_upper": str(cycle_relative_bound),
            "strict_threshold": "1/3"},
        "sha256": {
            str(path.relative_to(root)):
                hashlib.sha256(path.read_bytes()).hexdigest()
            for path in paths},
        "records": records,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({key: result[key] for key in
                      ("status", "checks", "max_relative_error")}))
    print(args.output)


if __name__ == "__main__":
    main()
