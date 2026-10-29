#!/usr/bin/env python3
"""Original repeated-R diagonal sector and its exact endpoint numerator."""

import json
from pathlib import Path

import mpmath as mp
import numpy as np

from audit_actual_borel_regular_fusion import fusion
from audit_actual_two_cut_ports import balanced_data


def main():
    mp.mp.dps = 65
    matrix_cases = []
    for N in (2, 3, 4, 5, 6, 8, 9):
        prime, _, q, _, _, K, _, positive, negative = balanced_data(N)
        Q = q*q % prime
        x = int(K[0, 0])
        C, Ci, *_ = fusion(N, prime, Q, [x, x], [0, 0])
        scalar = int(positive[0, 0])
        literal = np.eye(N*N, dtype=np.int64)
        for exponent in range(1, 6):
            literal = positive@literal % prime
            relative = Ci@literal@C % prime
            for k in range(N):
                d = pow(-1, k, prime)*pow(Q, k*(k+1)//2, prime) % prime
                assert int(relative[k, k]) == pow(scalar*d, exponent, prime)
            inverse = np.eye(N*N, dtype=np.int64)
            for _ in range(exponent):
                inverse = negative@inverse % prime
            relative_inverse = Ci@inverse@C % prime
            for k in range(N):
                d = pow(-1, k, prime)*pow(Q, k*(k+1)//2, prime) % prime
                assert int(relative_inverse[k, k]) == pow(scalar*d, -exponent, prime)
            matrix_cases.append({"N": N, "p": exponent, "both_signs": True})

    endpoint_cases = 0
    lattice_cases = 0
    for N in (3, 4, 7, 12):
        n = N-1
        Q = mp.exp(2j*mp.pi/N)
        for exponent in (-5, -3, -1, 1, 3, 5):
            for ell in (-2, -1, 0, 1, 2):
                def B(z):
                    return mp.exp(1j*mp.pi*exponent*z*(z-n)/N+2j*mp.pi*ell*z)

                for k in range(N):
                    d = (-1)**k * Q**(k*(k+1)//2)
                    assert abs(B(k)-d**exponent) < mp.mpf("1e-58")
                    lattice_cases += 1
                for t in (mp.mpf(".17"), mp.mpf("1.3"), mp.mpf("5.4")):
                    actual = B(1j*t)-B(-1j*t)-B(n+1j*t)+B(n-1j*t)
                    expected = (4*mp.exp(-1j*mp.pi*exponent*t*t/N)
                                *mp.sinh(mp.pi*exponent*n*t/N)
                                *mp.cosh(2*mp.pi*ell*t))
                    assert abs(actual-expected) <= mp.mpf("1e-55")*max(1, abs(expected))
                    endpoint_cases += 1
                endpoint_slopes = [exponent*(2*a-n)/N+2*ell for a in (0, n)]
                maximum = max(abs(value) for value in endpoint_slopes)
                predicted = abs(exponent)*n/N+2*abs(ell)
                assert abs(maximum-predicted) < 1e-14

    packet_cases = []
    for N, exponent in ((4, 3), (4, -3), (7, 5), (7, -5),
                        (9, 4), (9, -4), (13, 3), (13, 6)):
        n = N-1
        cutoff = abs(exponent)//2
        c = mp.mpf(abs(exponent))*n/N
        gap = 2*(cutoff+1)-c
        assert gap >= 1
        quadratic = mp.pi*exponent/N

        def B(z):
            return mp.exp(1j*quadratic*z*(z-n))

        def mode(k):
            linear = 2*mp.pi*k-quadratic*n
            scale = mp.sqrt(-1j*quadratic)
            shift = linear/(2*quadratic)
            return (mp.exp(-1j*linear*linear/(4*quadratic))*mp.sqrt(mp.pi)
                    /(2*scale)*(mp.erf(scale*(n+shift))-mp.erf(scale*shift)))

        def correction(t):
            if t == 0:
                return 2j*exponent*n/N
            return (4j*mp.exp(-1j*quadratic*t*t)*mp.sinh(mp.pi*exponent*n*t/N)
                    *mp.exp(-2*mp.pi*cutoff*t)/mp.expm1(2*mp.pi*t))

        height = mp.mpf(48)
        remainder = mp.quad(correction, list(range(49)))
        source_sum = mp.fsum(B(j) for j in range(N))
        packet_sum = 1+mp.fsum(mode(k) for k in range(-cutoff, cutoff+1))+remainder
        residual = abs(packet_sum-source_sum)
        tail_bound = (2/(mp.pi*gap*(1-mp.exp(-2*mp.pi)))
                      *mp.exp(-mp.pi*gap*height))
        assert residual < mp.mpf("1e-48")+tail_bound, (N, exponent, residual)
        # Closed digamma form of the positive absolute remainder bound.
        start = cutoff+1
        positive_bound = (mp.digamma(start+c/2)-mp.digamma(start-c/2))/mp.pi
        assert abs(remainder) <= positive_bound+mp.mpf("1e-48")
        packet_cases.append({"N": N, "p": exponent,
                             "mode_cutoff": cutoff, "mode_count": 2*cutoff+1,
                             "strict_type_gap": float(gap),
                             "exact_residue_identity_residual": float(residual),
                             "remainder_absolute_value": float(abs(remainder)),
                             "proven_absolute_bound": float(positive_bound)})

    marked_cases = []
    for N, exponent, spectral, meridian in (
            (5, 1, mp.mpc(".8", ".3"), mp.mpc("1.1", ".1")),
            (5, -1, mp.mpc("1.2", "-.2"), mp.mpc(".9", ".1")),
            (8, 3, mp.mpc(".7", ".2"), mp.mpc("1.05", ".03")),
            (8, -3, mp.mpc("1.1", ".1"), mp.mpc(".95", "-.04"))):
        n = N-1
        cutoff = (abs(exponent)+1)//2
        logarg = mp.log(spectral*meridian**(-2*exponent))
        quadratic = mp.pi*exponent/N

        def f(z):
            return mp.exp(1j*quadratic*z*(z-n)+logarg*z)

        def mode(k):
            linear = 2*mp.pi*k-quadratic*n-1j*logarg
            scale = mp.sqrt(-1j*quadratic)
            shift = linear/(2*quadratic)
            return (mp.exp(-1j*linear*linear/(4*quadratic))*mp.sqrt(mp.pi)
                    /(2*scale)*(mp.erf(scale*(n+shift))-mp.erf(scale*shift)))

        def correction(t):
            if t == 0:
                derivative0 = -1j*quadratic*n+logarg
                derivativen = (1j*quadratic*n+logarg)*f(n)
                return -(derivative0-derivativen)/mp.pi
            numerator = f(1j*t)-f(-1j*t)-f(n+1j*t)+f(n-1j*t)
            return 1j*mp.exp(-2*mp.pi*cutoff*t)*numerator/mp.expm1(2*mp.pi*t)

        Q = mp.exp(2j*mp.pi/N)
        literal = mp.fsum(((-1)**j*Q**(j*(j+1)//2)*meridian**(-2*j))**exponent
                         *spectral**j for j in range(N))
        remainder = mp.quad(correction, list(range(49)))
        presented = ((f(0)+f(n))/2
                     +mp.fsum(mode(k) for k in range(-cutoff, cutoff+1))+remainder)
        residual = abs(literal-presented)
        assert residual < mp.mpf("1e-48"), (N, exponent, residual)
        marked_cases.append({"N": N, "p": exponent,
                             "original_marked_kernel_residual": float(residual)})

    result = {
        "status": "PASS",
        "literal_repeated_crossing_matrix_cases": len(matrix_cases),
        "both_positive_and_negative_powers": True,
        "literal_clock_values_checked": lattice_cases,
        "endpoint_numerator_identities": endpoint_cases,
        "exact_finite_mode_source_identities": packet_cases,
        "whole_marked_gaussian_kernel_identities": marked_cases,
        "scope": "Exact actual local matrix sector and all linear lattice gauges; no assertion that this sector alone is a whole knot period.",
    }
    output = Path(__file__).with_name("twist_vertical_type_obstruction_results.json")
    output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(result))


if __name__ == "__main__":
    main()
