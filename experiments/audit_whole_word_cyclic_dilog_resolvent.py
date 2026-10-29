#!/usr/bin/env python3
"""Exact root-field audit of the original full cyclic-dilogarithm period."""

import json
from pathlib import Path

import numpy as np

from audit_actual_crossing_euler_completion import actual_data
from audit_actual_two_cut_ports import partial, word_matrix


def cyclic_coefficients(N, p, Q, sign):
    """Taylor jet of prod_j (1-Q^j t)^(sign*j/N), directly."""
    out = [1] + [0]*(N-1)
    for j in range(1, N):
        exponent = sign*j*pow(N, -1, p) % p
        local = [1]
        for a in range(1, N):
            local.append(local[-1]*(exponent-a+1)*pow(a, -1, p)*(-pow(Q, j, p)) % p)
        out = [sum(out[a]*local[k-a] for a in range(k+1)) % p for k in range(N)]
    return out


def polynomial(T, coefficients, p):
    out, power = np.zeros_like(T), np.eye(len(T), dtype=np.int64)
    for c in coefficients:
        out = (out+c*power) % p
        power = power@T % p
    assert not power.any()
    return out


def multiply_chronological(factors, p):
    out = np.eye(len(factors[0][1]), dtype=np.int64)
    for _, factor in factors:
        out = factor@out % p
    return out


def local(N, M):
    data = actual_data(N, M)
    if data is None:
        return None
    p, q, x, _, pivot, plus, minus, twist, dimension, normalization = data
    Q = q*q % p
    fac = [1]
    for a in range(1, N):
        fac.append(fac[-1]*(1-pow(Q, a, p)) % p)
    u = [pow(c, -1, p) for c in fac]
    v = [pow(-1, a, p)*pow(Q, a*(a-1)//2, p)*u[a] % p for a in range(N)]
    du, dv = cyclic_coefficients(N, p, Q, 1), cyclic_coefficients(N, p, Q, -1)
    assert du == u and dv == v
    # All-inverse realization: keep physical Q but orient the auxiliary
    # curve oppositely for every original u or inverse-factorial slot.
    opposite_inverse = cyclic_coefficients(N, p, pow(Q, -1, p), -1)
    all_inverse_u = [pow(Q, -a, p)*opposite_inverse[a] % p for a in range(N)]
    assert all_inverse_u == u
    recovered_fac = [N*pow(Q, -a-1, p)*dv[N-1-a] % p for a in range(N)]
    assert recovered_fac == fac
    S = np.zeros((N, N), dtype=np.int64)
    for a in range(N-1):
        S[a+1, a] = 1
    Tm, Tp = pow(x, -1, p)*np.kron(S.T, S) % p, pow(x, -1, p)*np.kron(S, S.T) % p
    Um, Vm, Up, Vp = (polynomial(T, c, p) for T, c in ((Tm, all_inverse_u), (Tm, dv), (Tp, all_inverse_u), (Tp, dv)))
    eye = np.eye(N, dtype=np.int64)
    F1, F2 = np.kron(np.diag(recovered_fac), eye), np.kron(eye, np.diag(recovered_fac))
    F1i, F2i = np.kron(np.diag(all_inverse_u), eye), np.kron(eye, np.diag(all_inverse_u))
    ds = [pow(-1, a, p)*pow(Q, a*(a-1)//2, p)*pow(x, -2*a, p) % p for a in range(N)]
    D, Di = np.kron(eye, np.diag(ds)), np.kron(eye, np.diag([pow(d, -1, p) for d in ds]))
    # Listed left-to-right as the displayed matrix product; reverse to act.
    common_left = [('F2', F2), ('u-', Um), ('F1', F1), ('F2i', F2i)]
    common_right = [('F2', F2), ('F1i', F1i), ('v-', Vm), ('F2i', F2i)]
    positive = list(reversed(common_left+[('D', D), ('u+', Up)]+common_right))
    negative = list(reversed(common_left+[('v+', Vp), ('Di', Di)]+common_right))
    kappa = int(plus[0, 0])
    assert np.array_equal(kappa*multiply_chronological(positive, p) % p, plus)
    assert np.array_equal(pow(kappa, -1, p)*multiply_chronological(negative, p) % p, minus)
    return dict(N=N, M=M, p=p, x=x, pivot=pivot, plus=plus, minus=minus,
                kappa=kappa, positive=positive, negative=negative, twist=twist,
                dimension=dimension, normalization=normalization)


def source(row, factors, strands):
    W = multiply_chronological(factors, row['p'])
    return int(partial(W, row['pivot'], strands, row['N'], row['p']).sum())*pow(row['N'], -1, row['p']) % row['p']


def word_case(row, strands, word, check_low_powers=False):
    N, p = row['N'], row['p']
    factors = []
    for letter in word:
        slot = abs(letter)-1
        local_factors = row['positive' if letter > 0 else 'negative']
        for name, A in local_factors:
            extended = np.kron(np.kron(np.eye(N**slot, dtype=np.int64), A),
                               np.eye(N**(strands-slot-2), dtype=np.int64))
            factors.append((name, extended))
    w = sum(1 if letter > 0 else -1 for letter in word)
    assert sum(name.startswith(('u', 'v')) for name, _ in factors) == 3*len(word)
    assert sum(name.startswith('F') and not name.endswith('i') for name, _ in factors) == 3*len(word)
    assert sum(name.startswith('F') and name.endswith('i') for name, _ in factors) == 3*len(word)
    assert sum(name.startswith('D') for name, _ in factors) == len(word)
    reconstructed = source(row, factors, strands)*pow(row['kappa'], w, p) % p
    actual_W = word_matrix(word, row['plus'], row['minus'], strands, N, p)
    actual = int(partial(actual_W, row['pivot'], strands, N, p).sum())*pow(N, -1, p) % p
    assert reconstructed == actual
    witnesses = []
    if check_low_powers:
        for j, (name, A) in enumerate(factors):
            if name.startswith('u'):
                modified = factors[:j]+[(name, np.eye(len(A), dtype=np.int64))]+factors[j+1:]
                coefficient = source(row, modified, strands)
                if coefficient:
                    witnesses.append(dict(slot=j, atom=name, constant_transfer_source=coefficient))
        assert witnesses, 'Do not silently discard every u infinity term.'
    full = actual*row['dimension']*pow(row['twist'], -w, p) % p
    return dict(N=N, M=row['M'], strands=strands, word=list(word),
                minimal_curve_factors=3*len(word), full_curve_factors=9*len(word),
                full_source_exterior_polynomial_exponent=strands-1+6*len(word),
                original_full_period=full, retained_u_infinity_witnesses=witnesses)


def main():
    locals_checked, words = [], []
    for N in range(2, 8):
        for M in (1, 3):
            row = local(N, M)
            if row is None:
                continue
            locals_checked.append(dict(N=N, M=M, field=row['p'], normalization=row['normalization']))
            if N <= 4:
                words.append(word_case(row, 3, (1, -2, 1, -2), check_low_powers=True))
            if N <= 3:
                words.append(word_case(row, 4, (1, 2, 3, -2, -1, 3)))
    result = dict(status='PASS', local_cases=locals_checked, word_cases=words,
                  all_inverse_auxiliary_curve_orientation_checked=True,
                  scope='Exact marked 3m/9m cyclic-dilogarithm period, including all-inverse realization, of original words and source; no geometric cycle-selection theorem.')
    Path(__file__).with_name('whole_word_cyclic_dilog_resolvent_results.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(dict(status='PASS', local_cases=len(locals_checked), whole_words=len(words),
                          nonzero_u_infinity_witnesses=sum(len(r['retained_u_infinity_witnesses']) for r in words))))


if __name__ == '__main__':
    main()
