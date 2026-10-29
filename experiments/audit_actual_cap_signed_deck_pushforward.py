#!/usr/bin/env python3
"""All four ORIGINAL cap channels: exact signed-deck source kernels."""

import json
from pathlib import Path

import mpmath as mp

from audit_cap_wall_fermat_quad_residue import affine_points, data, frames


def finite_product(index, delta, Q, N, epsilon, prime):
    quotient, residue = divmod(index, N)
    result = pow(epsilon, quotient, prime)
    for j in range(residue):
        result = result*(1-delta*pow(Q, j, prime)) % prime
    return result


def exact_cases():
    checked = 0
    families = []
    for N in range(2, 12):
        prime, _, _, Q, *_ = data(N)
        for delta, a, w in affine_points(N, prime)[:5]:
            assert w == 1
            epsilon = pow(a, N, prime)
            assert epsilon == (1-pow(delta, N, prime)) % prime
            for source in (0, N-1):
                sigma = int(source != 0)
                us = delta*pow(Q, sigma, prime) % prime
                P, _ = frames(N, prime, Q, us, a, 1)
                alpha = (1-Q) % prime if sigma else 1
                for target in (0, N-1):
                    tau = target
                    ut = delta*pow(Q, int(target != 0), prime) % prime
                    _, L = frames(N, prime, Q, ut, a, 1)
                    beta = N if target else 1
                    D = sigma+tau
                    B = epsilon*pow(N, -1, prime) % prime if target else (1-delta) % prime
                    R = (1-Q*delta)*pow((1-Q) % prime, -1, prime) % prime
                    for ell in range(-4, 5):
                        for n in range(N):
                            m = (n+target-source+ell) % N
                            actual = (pow(a, D+ell, prime)*int(L[m])*int(P[n])
                                      *pow(alpha*beta % prime, -1, prime)) % prime
                            h = n+sigma
                            expected = (B*pow(R, sigma, prime)
                                        *finite_product(h+ell, delta, Q, N, epsilon, prime)
                                        *pow(finite_product(h+1, delta, Q, N, epsilon, prime), -1, prime)) % prime
                            assert actual == expected, (N, source, target, ell, n)
                            checked += 1
            families.append({"N": N, "exact_Fermat_point": [int(delta), int(a)],
                             "all_four_original_channels_and_signed_characters": True})
    return families, checked


def uniform_bounds():
    mp.mp.dps = 65
    rho = mp.mpf(1)/16
    rows = []
    for N in (5, 8, 13, 32, 64):
        Q = mp.exp(2j*mp.pi/N)
        maxima = {ell: mp.mpf(0) for ell in range(-3, 4)}
        for angle in range(16):
            epsilon = rho*mp.exp(2j*mp.pi*angle/16)
            delta = mp.exp(mp.log(1-epsilon)/N)
            R = (1-Q*delta)/(1-Q)
            for source in (0, N-1):
                sigma = int(source != 0)
                for target in (0, N-1):
                    B = epsilon/N if target else 1-delta
                    for ell in range(-3, 4):
                        for n in range(N):
                            h = n+sigma
                            if ell >= 1:
                                ratio = mp.fprod(1-delta*Q**j for j in range(h+1, h+ell))
                            else:
                                ratio = 1/mp.fprod(1-delta*Q**j for j in range(h+ell, h+1))
                            actual = abs(B*R**sigma*ratio)
                            maxima[ell] = max(maxima[ell], actual)
                            if ell >= 1:
                                bound = 4*rho*3**(ell-1)/N
                            elif ell == 0:
                                bound = mp.mpf(2)
                            else:
                                bound = 2*(1+rho)*(mp.mpf(N)/3)**(-ell)
                            assert actual <= bound, (N, ell, n, actual, bound)
        rows.append({"N": N, "sampled_circle_maxima": {str(k): float(v) for k, v in maxima.items()},
                     "all_proven_signed_character_bounds_hold_on_grid": True})
    return rows


def bulk_scope_cases():
    exact = []
    for N in range(7, 40):
        prime, _, _, Q, *_ = data(N)
        L = (N+5)//6
        U = (5*N)//6
        n, m = L-2, U
        r = m-n
        assert 0 <= n < N and 0 <= m < N and 1 <= r < N
        F = [1]
        for j in range(1, N):
            F.append(F[-1]*(1-pow(Q, j, prime)) % prime)
        # Literal normalized cap leading coefficients, not an assigned kernel.
        literal = F[m]*pow(N*F[n+1] % prime, -1, prime) % prime
        product = pow(N, -1, prime)
        for j in range(L, U+1):
            product = product*(1-pow(Q, j, prime)) % prime
        assert literal == product and product
        exact.append({"N": N, "source_index": n, "target_index": m,
                      "bulk_deck_character": r, "central_pole_order": 1,
                      "exact_original_cap_coefficient_matches_product": True})
    rho = mp.mpf(1)/16
    scales = []
    v3 = mp.im(mp.polylog(2, mp.exp(mp.pi*1j/3)))
    for N in (24, 48, 96, 192, 384, 768, 1536):
        L, U = (N+5)//6, (5*N)//6
        r = U-L+2
        rate = (mp.fsum(mp.log(2*mp.sin(mp.pi*j/N)) for j in range(L, U+1))-mp.log(N))/N
        norm = rho**(mp.mpf(r)/N-1)
        assert 1 <= norm <= 1/rho
        scales.append({"N": N, "log_exact_cap_coefficient_over_N": float(rate),
                       "proved_Riemann_sum_limit_Vol_figure_eight_over_2pi": float(v3/mp.pi),
                       "inserted_coupon_norm_on_fixed_central_circle": float(norm)})
    return {"exact_literal_cap_cases": exact, "rate_diagnostics": scales,
            "scope": "Inserted non-degree-intertwining coupon on the ORIGINAL single-head cap; not a knot or paired-charge counterexample."}


if __name__ == "__main__":
    families, count = exact_cases()
    result = {"status": "PASS",
              "scope": "Literal normalized source/co-source entries at every original 0/d cap channel; no assertion that all singular Pachner factors have bounded deck characters.",
              "exact_root_families": families,
              "exact_signed_deck_kernel_identities": count,
              "uniform_bound_diagnostics": uniform_bounds(),
              "bulk_character_sharp_scope": bulk_scope_cases()}
    output = Path(__file__).with_name("actual_cap_signed_deck_pushforward_results.json")
    output.write_text(json.dumps(result, indent=2)+"\n")
    print("PASS", len(families), "actual root/Fermat families;", count,
          "four-channel signed-deck identities;", len(result["uniform_bound_diagnostics"]), "bound grids")
