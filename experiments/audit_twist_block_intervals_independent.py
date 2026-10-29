#!/usr/bin/env python3
"""Independent all-angle stress of physical twist-frame interval products.

Tests the exact separated collision factor and every retained M power;
does not replace the all-level factorial proof by finite estimates.
"""

import json
from pathlib import Path

import mpmath as mp


def main():
    mp.mp.dps = 100
    records = []
    for N in (2, 3, 4, 5, 8, 16, 32, 64):
        q = mp.exp(mp.pi*1j/N)
        Q = q*q
        d = N-1
        intervals = sorted({(0, d), (0, d//2), (d//2, d), (d//3, 2*d//3)})
        for ell in (0, 1, -7, 10**6):
            delta = mp.mpf(1)/(8*N**3*(1+abs(ell)))
            for angle in (0, mp.pi/2, mp.pi, 3*mp.pi/2):
                M = 1+delta*mp.exp(1j*angle)
                assert abs(1-M**4) >= 3*delta
                worst_product_error = mp.mpf(0)
                worst_log_bound_ratio = mp.mpf(0)
                collisions, self_omitted = 0, 0
                for r, s in intervals:
                    choices = {r, s, (r+s)//2}
                    if r <= d//2 <= s:
                        choices.add(d//2)
                    for k in choices:
                        ls = [l for l in range(r, s+1) if l != k]
                        zeros = [l for l in ls if (k+l+1) % N == 0]
                        assert len(zeros) <= 1
                        collisions += bool(zeros)
                        self_omitted += (2*k+1) % N == 0
                        base_nonzero = mp.mpc(1)
                        continued_nonzero = mp.mpc(1)
                        error_sum = mp.mpf(0)
                        for l in ls:
                            m = k+l+1
                            if m % N == 0:
                                continue
                            root = Q**(-m)
                            base_nonzero *= 1-root
                            continued_nonzero *= 1-M**4*root
                            err = abs(M**4-1)/abs(1-root)
                            assert err < mp.mpf('.1')
                            error_sum += 2*err
                        logchange = abs(mp.log(abs(continued_nonzero/base_nonzero)))
                        assert logchange <= error_sum+mp.mpf('1e-80')
                        if error_sum:
                            worst_log_bound_ratio = max(worst_log_bound_ratio, logchange/error_sum)
                        def c(j):
                            return q**-1*M*M*Q**(-j)+q*M**-2*Q**j
                        literal = mp.fprod(c(k)-c(l) for l in ls)
                        factored = ((q*M**-2)**len(ls)
                                    *mp.fprod(Q**k-Q**l for l in ls)
                                    *(1-M**4)**len(zeros)*continued_nonzero)
                        error = abs(literal-factored)/max(abs(literal), mp.mpf('1e-90'))
                        assert error < mp.mpf('1e-75')
                        worst_product_error = max(worst_product_error, error)
                        # First numerator interval: the M^-1 normalization is
                        # explicitly retained before harmonic comparison.
                        continued = mp.fprod(M*Q**(-l)-M**-1 for l in range(r+1, s+1))
                        root_product = mp.fprod(Q**(-l)-1 for l in range(r+1, s+1))
                        err = mp.fsum(2*abs(M*M-1)/abs(Q**(-l)-1)
                                      for l in range(r+1, s+1))
                        if s > r:
                            change = abs(mp.log(abs(continued/(M**(-(s-r))*root_product))))
                            assert change <= err+mp.mpf('1e-80')
                        # The second numerator interval touches both physical
                        # total-degree endpoints in these two valid choices.
                        for T in {s, d+r}:
                            indices = [T-l+1 for l in range(r+1, s+1)]
                            assert all(1 <= j <= d for j in indices)
                alpha = d+mp.log(M)/(mp.pi*1j/N)
                original_cartan = mp.exp((mp.pi*1j/N)*(alpha*alpha-d*d)/2)
                explicit_cartan = M**d*mp.exp(mp.log(M)**2/(2*mp.pi*1j/N))
                assert abs(original_cartan/explicit_cartan-1) < mp.mpf('1e-85')
                assert abs(explicit_cartan**ell) < 2
                records.append({'N': N, 'signed_power': ell, 'circle_angle': str(angle),
                                'intervals_checked': intervals,
                                'actual_collision_cases': collisions,
                                'omitted_self_collision_cases': self_omitted,
                                'max_factored_denominator_relative_error': float(worst_product_error),
                                'max_log_perturbation_bound_ratio': float(worst_log_bound_ratio),
                                'full_original_Cartan_power_abs': float(abs(explicit_cartan**ell))})
    data = {'status': 'PASS', 'families': records,
            'scope': ('Physical interval identities and uniform collision perturbations; '
                      'the analytic source-preserving norm proof is in the factorial-frame note.')}
    Path(__file__).with_name('twist_block_intervals_independent_results.json').write_text(
        json.dumps(data, indent=2)+'\n')
    print(f'PASS {len(records)} independent all-angle/signed-power interval and full-Cartan families')


if __name__ == '__main__':
    main()
