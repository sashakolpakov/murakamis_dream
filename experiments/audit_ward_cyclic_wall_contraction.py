#!/usr/bin/env python3
"""Original dual cup, full marker, Ward/sewing cocycle and cyclic contraction."""

import json
from pathlib import Path

import mpmath as mp
import numpy as np
import sympy as sp

from audit_actual_rogers_bridge_transport import MixedEntries, crossing, field, fusion


def inverse(A, prime):
    return np.array(sp.Matrix(A.tolist()).inv_mod(prime)).astype(np.int64)


def local_case(N, complete):
    prime, generic, q = field(N)
    E = MixedEntries(N, prime, q)
    Q, d = E.Q, N-1
    x = -pow(q, -1, prime) % prime if complete else generic
    y = pow(x, -1, prime)*pow(Q, -1, prime) % prime
    a = pow(x, -1, prime)
    first_frame = fusion(N, prime, x, E.F)
    second_frame = fusion(N, prime, y, E.F)
    literal = crossing(E, x, y, 1)
    cup = first_frame[:, d*N]
    assert np.array_equal(literal@cup % prime, second_frame[:, d*N])
    cap = np.array([pow(y, v, prime)*pow(N, -2, prime) % prime
                    for u in range(N) for v in range(N)], dtype=np.int64)
    assert int(cap@literal@cup % prime) == 1

    mu = np.array([pow(y, d-r, prime)*pow(-1, r, prime)
                   *pow(Q, -r*(r+1)//2, prime)*int(E.F[r])**2
                   *pow(N, -2, prime) % prime for r in range(N)], dtype=np.int64)
    assert all(int((cap@second_frame)[r*N+d-r] % prime) == int(mu[r])
               for r in range(N))
    assert int(mu[d]) == 1
    ell = np.zeros(N, dtype=np.int64)
    ell[d] = 1
    unit = ell.copy()
    raising = np.zeros((N, N), dtype=np.int64)
    for r in range(d):
        raising[r+1, r] = 1
    cyclic = raising.copy()
    cyclic[0, d] = 1
    nu = np.zeros(N, dtype=np.int64)
    nu[1:] = mu[:-1]
    assert np.array_equal((mu-ell) % prime, nu@raising % prime)
    gaussian = [pow(-1, b, prime)*pow(Q, b*(b+1)//2, prime) % prime
                for b in range(N)]
    Din = np.diag([gaussian[d-r] for r in range(N)]).astype(np.int64)
    Dout = np.diag([gaussian[(-r) % N] for r in range(N)]).astype(np.int64)
    assert np.array_equal(raising@Din % prime, Dout@raising % prime)
    A = a*cyclic % prime
    Tin = a*raising % prime
    Tout = Tin.copy()
    Tout[1, 0] = 0
    assert np.array_equal(raising@Tin % prime, Tout@raising % prime)
    defect = (raising@A-A@raising) % prime
    sparse = np.zeros((N, N), dtype=np.int64)
    sparse[1, d] = a
    sparse[0, d-1] = -a % prime
    assert np.array_equal(defect, sparse)
    eye = np.eye(N, dtype=np.int64)
    checked = 0
    for t in range(2, 18):
        if (pow(t, N, prime)-pow(a, N, prime)) % prime == 0:
            continue
        RA = inverse((t*eye-A) % prime, prime)
        RTin = inverse((t*eye-Tin) % prime, prime)
        RTout = inverse((t*eye-Tout) % prime, prime)
        Ein, Eout = (RTin-RA) % prime, (RTout-RA) % prime
        assert not np.any((raising@Ein-Eout@raising+RA@defect@RA) % prime)
        gmu = int(mu@Din@RA@unit % prime)
        gcorner = int(ell@RA@unit % prime)
        current = int(nu@Dout@RA@defect@RA@unit % prime)
        assert (gmu-gcorner-current) % prime == 0
        assert int(mu@Din@RTin@unit % prime) == pow(t, -1, prime)
        expected = pow(t, N-1, prime)*pow((pow(t, N, prime)-pow(a, N, prime)) % prime, -1, prime) % prime
        assert gcorner == expected
        checked += 1
    assert checked
    powers = [unit]
    for r in range(1, N):
        powers.append(cyclic@powers[-1] % prime)
    coefficients = [int(mu@Din@v % prime) for v in powers]
    assert coefficients[0] == 1
    residues, primitive = [], []
    for j in range(N):
        residues.append(sum(coefficients[r]*pow(Q, -j*r, prime)
                            for r in range(N))*pow(N, -1, prime) % prime)
        primitive.append(sum(coefficients[r]*pow(Q, -j*r, prime)
                             *pow((pow(Q, -r, prime)-1) % prime, -1, prime)
                             for r in range(1, N))*pow(N, -1, prime) % prime)
    assert sum(residues) % prime == 1
    assert sum(primitive) % prime == 0
    for j in range(N):
        assert (primitive[(j+1) % N]-primitive[j]
                -residues[j]+pow(N, -1, prime)) % prime == 0
    return {"N": N, "meridian": "complete" if complete else "generic",
            "original_cup_and_marker": True,
            "rational_resolvent_parameters": checked,
            "pointwise_Ward_sewing_cocycle": True,
            "exact_residue_augmentation": 1,
            "explicit_cyclic_chain_primitive": True}


def norm_cases():
    rows = []
    for N in (2, 3, 4, 7, 12, 25, 64, 127):
        # The unique zero-mean inverse of forward difference.
        S = np.zeros((N, N))
        for j in range(N):
            S[j, (j+1) % N] = 1
        P = np.ones((N, N))/N
        D = S-np.eye(N)
        H = np.linalg.inv(D+P)-P
        assert np.max(np.abs(D@H-(np.eye(N)-P))) < 2e-12
        assert np.max(np.abs(H@D-(np.eye(N)-P))) < 2e-12
        l2 = np.linalg.norm(H, 2)
        linf = np.linalg.norm(H, np.inf)
        assert abs(l2-1/(2*np.sin(np.pi/N))) < 2e-11
        assert l2 <= N/4+2e-12 and linf <= N+2e-12
        rows.append({"N": N, "ell2_norm": float(l2), "ell_infinity_norm": float(linf)})
    return rows


def whole_current_case(N, length):
    """Assembled literal dual-pair Euler word, with every cyclic sector retained."""
    prime, x, q = field(N)
    E = MixedEntries(N, prime, q)
    Q, d = E.Q, N-1
    y = pow(x, -1, prime)*pow(Q, -1, prime) % prime
    last_color = y if length % 2 else x
    mu = np.array([pow(last_color, d-r, prime)*pow(-1, r, prime)
                   *pow(Q, -r*(r+1)//2, prime)*int(E.F[r])**2
                   *pow(N, -2, prime) % prime for r in range(N)], dtype=np.int64)
    ell = np.zeros(N, dtype=np.int64)
    ell[d] = 1
    nu = np.zeros(N, dtype=np.int64)
    nu[1:] = mu[:-1]
    F = np.zeros((N, N), dtype=np.int64)
    for r in range(d):
        F[r+1, r] = 1
    S = F.copy()
    S[0, d] = 1
    eye = np.eye(N, dtype=np.int64)
    gaussian = [pow(-1, b, prime)*pow(Q, b*(b+1)//2, prime) % prime
                for b in range(N)]
    Din = np.diag([gaussian[d-r] for r in range(N)]).astype(np.int64)
    Dout = np.diag([gaussian[(-r) % N] for r in range(N)]).astype(np.int64)
    options, denominators = [], []
    for j in range(length):
        a = pow(x if j % 2 == 0 else y, -1, prime)
        t = next(value for value in range(2+j, 40)
                 if (pow(value, N, prime)-pow(a, N, prime)) % prime)
        A, Tin = a*S % prime, a*F % prime
        Tout = Tin.copy()
        Tout[1, 0] = 0
        RA = inverse((t*eye-A) % prime, prime)
        RTin = inverse((t*eye-Tin) % prime, prime)
        RTout = inverse((t*eye-Tout) % prime, prime)
        options.append(((Din@RA % prime, Dout@RA % prime),
                        (Din@(RTin-RA) % prime, Dout@(RTout-RA) % prime)))
        denominators.append(t)

    nonzero_separate_changes = 0
    summed_change = 0
    summed_original = 0
    for code in range(1 << length):
        factors = [options[j][(code >> j) & 1] for j in range(length)]
        prefix = [eye]
        for Ain, _ in factors:
            prefix.append(Ain@prefix[-1] % prime)
        total = prefix[-1]
        rhs = np.zeros((N, N), dtype=np.int64)
        for j, (Ain, Aout) in enumerate(factors):
            tail = eye
            for _, later_out in factors[j+1:]:
                tail = later_out@tail % prime
            defect = (F@Ain-Aout@F) % prime
            rhs = (rhs+tail@defect@prefix[j]) % prime
        whole_out = eye
        for _, Aout in factors:
            whole_out = Aout@whole_out % prime
        assert np.array_equal((F@total-whole_out@F) % prime, rhs)
        change = int((mu-ell)@total@ell % prime)
        assert change == int(nu@rhs@ell % prime)
        nonzero_separate_changes += int(change != 0)
        summed_change = (summed_change+change) % prime
        summed_original = (summed_original+int(mu@total@ell % prime)) % prime
    assert summed_change == 0
    expected = 1
    for t in denominators:
        expected = expected*pow(t, -1, prime) % prime
    assert summed_original == expected
    assert nonzero_separate_changes
    return {"N": N, "Euler_slots": length, "retained_cyclic_sectors": 1 << length,
            "nonzero_sectorwise_marker_changes": nonzero_separate_changes,
            "total_Ward_current": summed_change,
            "original_unit_cup_resolvent_source_retained": True}


def scale_cases():
    mp.mp.dps = 60
    v3 = mp.im(mp.polylog(2, mp.exp(mp.pi*1j/3)))
    target = float(v3/mp.pi)
    rows = []
    for N in (40, 80, 160, 320, 640, 1280):
        logF = np.zeros(N)
        for r in range(1, N):
            logF[r] = logF[r-1]+np.log(2*np.sin(np.pi*r/N))
        log_weights = 2*logF[:-1]-2*np.log(N)
        logscale = max(0., float(np.max(log_weights)))
        c = np.zeros(N, dtype=np.complex128)
        c[0] = np.exp(-logscale)
        for r in range(1, N):
            c[r] = (np.exp(log_weights[r-1]-logscale)
                    *np.exp(1j*np.pi*(N-r)**2/N))
        residues = np.fft.fft(c)/N
        maximum = float(np.max(np.abs(residues)))
        maxc = float(np.max(np.abs(c)))
        assert maximum <= maxc*(1+1e-12)
        assert maximum >= maxc/N*(1-1e-12)
        rows.append({"N": N,
                     "log_max_original_cyclic_residue_over_N": float((logscale+np.log(maximum))/N),
                     "proved_limit_Vol_figure_eight_over_2pi": target,
                     "full_augmentation_is_exactly_one_by_field_and_symbolic_proof": True})
    return rows


if __name__ == "__main__":
    result = {"status": "PASS",
              "scope": "Original full-marker cup, rational Ward/sewing current and retained augmentation; no positive-chart or volume-selection assertion.",
              "original_root_families": [local_case(N, complete)
                                         for N in range(2, 9) for complete in (False, True)],
              "assembled_original_Ward_cocycle_cases": [whole_current_case(N, length)
                                                        for N in range(2, 8) for length in (2, 3)],
              "polynomial_chain_contraction_norms": norm_cases(),
              "source_anchored_large_residue_scale": scale_cases()}
    out = Path(__file__).with_name("ward_cyclic_wall_contraction_results.json")
    out.write_text(json.dumps(result, indent=2)+"\n")
    print("PASS", len(result["original_root_families"]), "original cup families;",
          len(result["assembled_original_Ward_cocycle_cases"]), "assembled sector words;",
          len(result["polynomial_chain_contraction_norms"]), "chain norms;",
          len(result["source_anchored_large_residue_scale"]), "source scale diagnostics")
