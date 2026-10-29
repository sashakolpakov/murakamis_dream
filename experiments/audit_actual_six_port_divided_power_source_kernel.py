#!/usr/bin/env python3
"""Actual divided coproducts and six-port source kernel, including all parity signs."""
import functools
import itertools
import json
import math
from pathlib import Path

import numpy as np

from audit_actual_two_cut_ports import balanced_data
from audit_actual_pair_casimir_commutant_and_rotated_trace import rank


@functools.cache
def states(N, r, degree):
    if degree < 0 or degree > r*(N-1):
        return ()
    if r == 0:
        return ((),) if degree == 0 else ()
    return tuple((a,)+tail for a in range(max(0, degree-(r-1)*(N-1)),
                                        min(N-1, degree)+1)
                 for tail in states(N, r-1, degree-a))


class ActualDivided:
    def __init__(self, N, prime, q):
        self.N, self.d, self.p, self.q = N, N-1, prime, q
        self.Q = q*q % prime
        self.rho = (q-pow(q, -1, prime)) % prime
        self.fact = [1]
        self.ff = [1]
        for a in range(1, N):
            self.fact.append(self.fact[-1]*(pow(q, a, prime)-pow(q, -a, prime))
                             *pow(self.rho, -1, prime) % prime)
            self.ff.append(self.ff[-1]*(1-pow(self.Q, a, prime)) % prime)

    @functools.cache
    def local(self, kind, a, n):
        p, q, Q = self.p, self.q, self.Q
        if n < 0 or n >= self.N or (kind == "E" and n > a) or (
                kind == "F" and a+n > self.d):
            return 0
        answer = 1
        if kind == "E":
            for b in range(a-n+1, a+1):
                answer = answer*(pow(q, -self.N, p)
                                 -pow(q, self.N-2*b, p)) % p
        else:
            for b in range(a+1, a+n+1):
                answer = answer*(1-pow(Q, b, p)) % p
        return answer*pow(self.fact[n], -1, p) % p

    def entry(self, kind, a, b):
        p, d = self.p, self.d
        ell = [u-v if kind == "E" else v-u for u, v in zip(a, b)]
        if min(ell) < 0 or max(ell) >= self.N:
            return 0
        cross = sum(ell[i]*ell[j] for i in range(len(a))
                    for j in range(i+1, len(a)))
        if kind == "E":
            exponent = cross+sum(sum(ell[:i])*(d-2*a[i]) for i in range(len(a)))
        else:
            exponent = -cross-sum(sum(ell[i+1:])*(d-2*b[i]) for i in range(len(a)))
        answer = pow(self.q, exponent, p)
        for u, n in zip(a, ell):
            answer = answer*self.local(kind, u, n) % p
        return answer

    def matrix(self, kind, r, degree, n):
        source = states(self.N, r, degree)
        target = states(self.N, r, degree-n if kind == "E" else degree+n)
        return np.array([[self.entry(kind, a, b) for a in source]
                         for b in target], dtype=np.int64).reshape(len(target), len(source))

    def apply(self, kind, vector, n):
        out = {}
        r = len(next(iter(vector)))
        for a, coefficient in vector.items():
            capacities = a if kind == "E" else tuple(self.d-v for v in a)
            for ell in states(self.N, r, n):
                if any(k > c for k, c in zip(ell, capacities)):
                    continue
                b = tuple(u-v if kind == "E" else u+v for u, v in zip(a, ell))
                out[b] = (out.get(b, 0)+coefficient*self.entry(kind, a, b)) % self.p
        return {key: value for key, value in out.items() if value}


def root_case(N):
    p, eta, q, E, F, K, pivot, Rp, Rm = balanced_data(N)
    data = ActualDivided(N, p, q)
    d, x = N-1, pow(q, N-1, p)
    En = data.matrix("E", 4, 2*d, N)
    Fn = data.matrix("F", 4, N-2, N)
    nlow, nsource = En.shape
    constant = 2*(-1)**N*pow(data.rho, 2*N, p) % p
    assert np.array_equal(En@Fn % p, constant*np.eye(nlow, dtype=np.int64) % p)
    alpha = (N*pow(q, -N*(N-1)//2, p)
             *pow(pow(1-data.Q, N, p), -1, p)) % p
    JE, JF = alpha*En % p, alpha*Fn % p
    assert np.array_equal(JE@JF % p, (-2*N*N)*np.eye(nlow, dtype=np.int64) % p)
    assert rank(JE, p) == math.comb(N+1, 3)
    assert nsource-nlow == (N**3+N)//2
    P = (np.eye(nsource, dtype=np.int64)
         +pow(2*N*N, -1, p)*(JF@JE % p)) % p
    assert not np.any(JE@P % p)
    if N <= 6:
        assert np.array_equal(P@P % p, P)
    # Original two-cup prefix, not an arbitrary invariant vector.
    w0 = np.array([N*N*pow(x, -a[1]-a[3], p) % p
                   if a[0]+a[1] == d and a[2]+a[3] == d else 0
                   for a in states(N, 4, 2*d)], dtype=np.int64)
    assert not np.any(JE@w0 % p)
    assert np.array_equal(P@w0 % p, w0)
    # Full physical two-head divided intertwiners including N-th normals.
    pair = {}
    for kind in ("E", "F"):
        A = np.zeros((N*N, N*N), dtype=np.int64)
        for T in range(2*d+1):
            source = states(N, 2, T)
            target = states(N, 2, T-N if kind == "E" else T+N)
            block = data.matrix(kind, 2, T, N)
            for i, b in enumerate(target):
                for j, a in enumerate(source):
                    A[b[0]*N+b[1], a[0]*N+a[1]] = block[i, j]
        for crossing in (Rp, Rm):
            assert not np.any((A@crossing-crossing@A) % p)
        pair[kind] = A
    return {"N": N, "target_rank": nlow, "source_kernel_dimension": nsource-nlow,
            "exact_all_parity_right_inverse_and_projection": True,
            "original_cup_source_and_both_signed_divided_intertwiners": True}, data


def generic_commutation(N):
    p, q = 1000003, 2
    data = ActualDivided(N, p, q)
    En = data.matrix("E", 4, 2*N-2, N)
    Fn = data.matrix("F", 4, N-2, N)
    direct = En@Fn % p
    rhs = np.zeros_like(direct)
    coefficient = 1
    for t in range(1, N+1):
        coefficient = (coefficient*(pow(q, 2*N-t+1, p)-pow(q, -(2*N-t+1), p))
                       *pow(pow(q, t, p)-pow(q, -t, p), -1, p)) % p
        a = N-t
        Ea = data.matrix("E", 4, N-2, a)
        Fa = data.matrix("F", 4, N-2-a, a)
        rhs = (rhs+pow(data.rho, 2*t, p)*coefficient*(Fa@Ea % p)) % p
    assert np.array_equal(direct, rhs)
    return {"N": N, "generic_q_divided_commutation_before_root": True}


def extraction_case(N, data):
    p, x, Q, d = data.p, pow(data.q, N-1, data.p), data.Q, N-1
    source, target = states(N, 4, 2*d), states(N, 4, N-2)
    expected = data.matrix("E", 4, 2*d, N)
    actual = np.zeros_like(expected)
    for j, w in enumerate(source):
        current = {w: 1}
        for c in range(N):
            coefficient = pow(-x*Q, c, p)*pow(data.ff[c], -1, p) % p
            # True six-head N-divided matrix entry, last two outputs(0,d).
            for a4, value in current.items():
                a6 = a4+(c, d)
                for i, b4 in enumerate(target):
                    actual[i, j] = (actual[i, j]+coefficient*value
                                    *data.entry("E", a6, b4+(0, d))) % p
            current = data.apply("E", current, 1) if current else {}
    assert np.array_equal(actual, expected)
    return {"N": N, "all_original_H2_input_columns": len(source),
            "full_six_head_extraction_identity": True}


def full_source_case(N, data):
    p, eta, q, E, F, K, pivot, Rp, Rm = balanced_data(N)
    d, x = N-1, pow(q, N-1, p)
    v = {a: N**3*pow(x, -a[1]-a[3]-a[5], p) % p
         for a in states(N, 6, 3*d)
         if all(a[2*j]+a[2*j+1] == d for j in range(3))}
    assert not data.apply("E", v, N)
    assert not data.apply("F", v, N)
    word = [1, -2, 4, 3, -5, 2]
    for letter in word:
        slot, crossing = abs(letter)-1, Rp if letter > 0 else Rm
        out = {}
        for a, value in v.items():
            col = a[slot]*N+a[slot+1]
            for row in np.flatnonzero(crossing[:, col]):
                b = a[:slot]+(int(row)//N, int(row) % N)+a[slot+2:]
                out[b] = (out.get(b, 0)+value*int(crossing[row, col])) % p
        v = {key: value for key, value in out.items() if value}
    assert not data.apply("E", v, N)
    assert not data.apply("F", v, N)
    w = np.array([int(v.get(a+(0, d), 0))*pow(x, d, p)*pow(N, -1, p) % p
                  for a in states(N, 4, 2*d)], dtype=np.int64)
    assert not np.any(data.matrix("E", 4, 2*d, N)@w % p)
    return {"N": N, "literal_original_six_head_word": word,
            "both_full_divided_source_equations_and_extracted_kernel": True}


if __name__ == "__main__":
    roots, all_data = [], {}
    for N in range(2, 11):
        row, all_data[N] = root_case(N)
        roots.append(row)
    generic = [generic_commutation(N) for N in range(2, 7)]
    extraction = [extraction_case(N, all_data[N]) for N in range(2, 6)]
    source = [full_source_case(N, all_data[N]) for N in range(2, 5)]
    output = {"status": "PASS", "all_root_right_inverses_and_pair_intertwiners": roots,
              "generic_divided_commutation": generic,
              "all_input_six_head_extraction": extraction,
              "full_original_six_head_source_words": source,
              "scope": "Exact saturated-source kernel and algebraic projection; "
                       "no tame oblique-frame norm or geometric energy estimate."}
    Path(__file__).with_name("actual_six_port_divided_power_source_kernel_results.json").write_text(
        json.dumps(output, indent=2)+"\n")
    print("PASS 9 all-parity right inverses/pair intertwiners; "
          "5 generic commutations; 4 all-input extractions; 3 full six-head source words")
