#!/usr/bin/env python3
"""Finite product/weighted/root-coefficient checks for the short own proof."""
import itertools
import json
from pathlib import Path

from audit_actual_two_cut_ports import balanced_data
from audit_actual_trivalent_root_fourier_source_certificate import mul, coeff


def factorials(Q, length, p):
    F = [1]
    for k in range(1, length+1):
        F.append(F[-1]*(1-pow(Q, k, p)) % p)
    return F


def euler(Q, start, length, p):
    out = [1]
    for k in range(length):
        out = mul(out, [1, -pow(Q, start+k, p) % p], p)
    return out


def add_shift(out, poly, shift, scale, p):
    for k, v in enumerate(poly):
        out[k+shift] = (out[k+shift]+scale*v) % p


def generic_product():
    p, Q = 1009, 2
    F = factorials(Q, 20, p)
    count = 0
    for m, n in itertools.product(range(11), repeat=2):
        lhs = mul(euler(Q, 0, m, p), euler(Q, 0, n, p), p)
        rhs = [0]*(m+n+1)
        for k in range(min(m, n)+1):
            scale = (-1)**k*pow(Q, k*(k-1)//2, p)*F[m]*F[n]*pow(F[k]*F[m-k]*F[n-k], -1, p) % p
            add_shift(rhs, euler(Q, 0, m+n-k, p), k, scale, p)
        assert lhs == rhs
        count += 1
    return count


def case(N):
    p, eta, q, *_ = balanced_data(N)
    Q, d, m = q*q % p, N-1, (N-1)//2
    F = factorials(Q, d, p)
    weighted = root_coeff = triples = 0
    for c in range(m+1):
        square = mul(euler(Q, 0, c, p), euler(Q, 0, c, p), p)
        for H in range(2*c+1):
            lhs = [square[e]*F[2*c-e]*pow(F[H-e], -1, p) % p for e in range(H+1)]
            rhs = [0]*(H+1)
            for k in range(min(c, H)+1):
                scale = (-1)**k*pow(Q, k*(k-1)//2, p)*F[c]**2*F[2*c-k]*pow(F[k]*F[c-k]**2*F[H-k], -1, p) % p
                add_shift(rhs, euler(Q, 0, H-k, p), k, scale, p)
            assert lhs == rhs
            weighted += 1
    for b in range(m+1):
        square = mul(euler(Q, -b, b, p), euler(Q, -b, b, p), p)
        for n in range(b+1):
            lhs = coeff(mul(square, euler(Q, 0, d-2*b+n, p), p), n)
            rhs = pow(Q, n*(n-1-2*b), p)*F[b]**2*pow(F[n]*F[b-n]**2, -1, p) % p
            assert lhs == rhs
            root_coeff += 1
    for a, b, c in itertools.product(range(m+1), repeat=3):
        delta, H = a+b+c-d, a+c-b
        if delta < 0:
            continue
        square = mul(euler(Q, 0, c, p), euler(Q, 0, c, p), p)
        weighted_poly = [square[e]*F[2*c-e]*pow(F[H-e], -1, p) % p for e in range(H+1)]
        square_b = mul(euler(Q, -b, b, p), euler(Q, -b, b, p), p)
        actual = coeff(mul(square_b, weighted_poly, p), delta)
        T0 = pow(Q, delta*(delta-1-2*b), p)*F[b]**2*F[2*c]*pow(F[H]*F[delta]*F[b-delta]**2, -1, p) % p
        value, term = 1, 1
        for k in range(delta):
            num = Q*(1-pow(Q, k-delta, p))*(1-pow(Q, k-c, p))**2*(1-pow(Q, k-H, p))
            den = (1-pow(Q, k+1, p))*(1-pow(Q, k-2*c, p))*(1-pow(Q, b-delta+k+1, p))**2
            term = term*num*pow(den % p, -1, p) % p
            value = (value+term) % p
        assert actual == T0*value % p
        triples += 1
    return {'N': N, 'prime': p, 'weighted_square_identities': weighted,
            'root_coefficient_cancellations': root_coeff,
            'all_order_supported_source_coefficient_bridges': triples}


if __name__ == '__main__':
    generic = generic_product()
    rows = [case(N) for N in range(2, 17)]
    out = {'status': 'PASS', 'generic_product_linearizations': generic,
           'root_families': rows,
           'scope': 'Supplementary exact checks of the separately proved finite square-linearization source bridge, including every physical denominator. No whole magnetic tensor or graph-volume bound is tested or asserted.'}
    Path(__file__).with_name('actual_trivalent_square_linearization_bridge_results.json').write_text(json.dumps(out, indent=2)+'\n')
    print('PASS', generic, 'generic product identities;', len(rows), 'root families;',
          sum(r['all_order_supported_source_coefficient_bridges'] for r in rows), 'all-order supported bridges')
