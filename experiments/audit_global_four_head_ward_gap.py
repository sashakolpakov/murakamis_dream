#!/usr/bin/env python3
"""Diagnostic only: simultaneous physical F/E Ward gap on four actual heads."""

import argparse
import json
from pathlib import Path

import numpy as np


def states(heads, N, degree):
    if heads == 1:
        return [(degree,)] if 0 <= degree < N else []
    return [(a,)+tail
            for a in range(max(0, degree-(heads-1)*(N-1)), min(N-1, degree)+1)
            for tail in states(heads-1, N, degree-a)]


def current(heads, N, degree):
    source = states(heads, N, degree)
    above = states(heads, N, degree+1)
    below = states(heads, N, degree-1)
    row_above = {state: i for i, state in enumerate(above)}
    row_below = {state: i for i, state in enumerate(below)}
    Q = np.exp(2j*np.pi/N)
    color = -np.exp(-1j*np.pi/N)
    F = np.zeros((len(above), len(source)), dtype=complex)
    E = np.zeros((len(below), len(source)), dtype=complex)
    for column, state in enumerate(source):
        prefix = 1
        for j, a in enumerate(state):
            if a < N-1:
                out = state[:j]+(a+1,)+state[j+1:]
                F[row_above[out], column] = prefix*(1-Q**(a+1))
            prefix *= color**(-1)*Q**a
        suffix = 1
        for j in range(heads-1, -1, -1):
            a = state[j]
            if a:
                out = state[:j]+(a-1,)+state[j+1:]
                E[row_below[out], column] = -suffix*(1-Q**(-a))
            suffix *= color*Q**(-a)
    return source, above, below, F, E


def case(N):
    heads, degree = 4, 2*(N-1)
    source, above, below, F, E = current(heads, N, degree)
    previous, _, _, Fprevious, _ = current(heads, N, degree-1)
    index_source = {state: j for j, state in enumerate(source)}
    index_below = {state: j for j, state in enumerate(below)}
    source_reversal = [index_source[state[::-1]] for state in source]
    below_reversal = [index_below[state[::-1]] for state in below]
    predicted = -Fprevious.conj().T[np.ix_(below_reversal, source_reversal)]
    error = float(np.max(np.abs(E-predicted)))
    assert error < 2e-12
    gram = F.conj().T@F+E.conj().T@E
    explicit = np.zeros_like(gram)
    q = np.exp(1j*np.pi/N)
    phi = np.pi-np.pi/N
    for column, state in enumerate(source):
        explicit[column, column] = 4*sum(np.sin(np.pi*(a+1)/N)**2
                                        +np.sin(np.pi*a/N)**2 for a in state)
        for i in range(heads):
            for j in range(i+1, heads):
                if state[i] == N-1 or state[j] == 0:
                    continue
                out = list(state)
                out[i] += 1
                out[j] -= 1
                row = index_source[tuple(out)]
                middle = sum(state[i+1:j])
                value = (8/q*np.sin(np.pi*(state[i]+1)/N)*np.sin(np.pi*state[j]/N)
                         *np.cos((j-i)*phi-np.pi*(state[i]+state[j]+2*middle)/N))
                explicit[row, column] = value
                explicit[column, row] = np.conj(value)
    gram_error = float(np.max(np.abs(gram-explicit)))
    assert gram_error < 1e-11
    conjugation_error = float(np.max(np.abs(gram[np.ix_(source_reversal, source_reversal)]
                                            -gram.conj())))
    assert conjugation_error < 1e-11
    realified = gram.real-gram.imag[source_reversal, :]
    direct_unitary = (.5*gram-.5j*gram[:, source_reversal]
                      +.5j*gram[source_reversal, :]
                      +.5*gram[np.ix_(source_reversal, source_reversal)])
    realification_error = float(np.max(np.abs(realified-direct_unitary)))
    assert realification_error < 1e-11
    assert np.max(np.abs(realified-realified.T)) < 1e-11
    triangle = None
    if N == 5:
        ia, ib, ic = [index_source[state] for state in
                      ((1, 1, 2, 4), (2, 0, 2, 4), (2, 1, 1, 4))]
        product = gram[ib, ia]*gram[ic, ib]*gram[ia, ic]
        golden = (5-np.sqrt(5))/2
        expected = -np.sqrt(5)*golden**2/q
        assert abs(product-expected) < 1e-12
        assert abs(product.imag) > 1
        triangle = {"product_real": float(product.real), "product_imag": float(product.imag),
                    "diagonal_unitary_gauge_invariant_nonreal": True}

    # Exact rank of F follows from all full N-strings in the actual
    # graded regular Borel fusion. The joint rank is NOT asserted proved here.
    F_rank = len(source)-len(states(heads-1, N, degree-(N-1)))
    F_values = np.linalg.svd(F, compute_uv=False)
    positive_F = float(F_values[F_rank-1])
    next_F = float(F_values[F_rank]) if F_rank < len(F_values) else 0.
    assert next_F < 1e-10
    both = np.linalg.svd(np.vstack([F, E]), compute_uv=False)
    observed_positive = both[both > 1e-10]
    joint_gap = float(observed_positive[-1])
    observed_kernel = len(source)-len(observed_positive)
    assert joint_gap > 1e-5
    return {"N": N, "head_count": heads, "actual_total_degree": degree,
            "physical_source_dimension": len(source),
            "proved_F_rank": F_rank,
            "smallest_nonzero_F_singular_value": positive_F,
            "next_F_value_in_exact_zero_cluster": next_F,
            "observed_joint_F_E_kernel_dimension": observed_kernel,
            "smallest_observed_nonzero_joint_Ward_value": joint_gap,
            "actual_E_reversal_identity_error": error,
            "explicit_all_entry_Gram_error": gram_error,
            "reversal_real_structure_error": conjugation_error,
            "condition_one_realification_error": realification_error,
            "actual_K_one_triangle": triangle}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--larger", action="store_true", help="also test N=14,16")
    args = parser.parse_args()
    levels = [3, 4, 5, 6, 8, 10, 12]+([14, 16] if args.larger else [])
    result = {"status": "PASS",
              "scope": "Actual physical Ward matrices and verified reversal identity; numerical spectral diagnostic, not an asymptotic theorem or a counterexample to polynomial bounds.",
              "cases": [case(N) for N in levels]}
    output = Path(__file__).with_name("global_four_head_ward_gap_results.json")
    output.write_text(json.dumps(result, indent=2)+"\n")
    print("PASS", len(levels), "actual four-head Ward spectra; numerical diagnostic only")
