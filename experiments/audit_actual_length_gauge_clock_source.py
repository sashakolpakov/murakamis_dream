#!/usr/bin/env python3
"""Original singleton clock source and exact compressed Riesz budgets."""

import itertools
import json
from pathlib import Path

import mpmath as mp
import numpy as np

import audit_actual_global_charged_bridge_flow as flow
from audit_actual_hardy_cauchy_network import HardyNetwork
from audit_actual_signed_overbridge_unwinding import inv
from audit_actual_two_cut_ports import partial, word_matrix


def singleton_setup(H, width, word):
    S = flow.setup(H, width, word)
    records = S["records"]
    S["paths"] = [[j] for j in range(len(records))]
    S["events"] = [
        {"kind": "bridge", "path": [j],
         "input": R["invars"][R["over_in"]],
         "output": R["outvars"][R["over_out"]]}
        for j, R in enumerate(records)
    ] + [{"kind": "closure", "head": i,
          "input": S["ov"][i], "output": S["iv"][i]}
         for i in range(width)]
    S["expected"] = (set(S["iv"]) | set(S["ov"])
                     | {v for R in records for v in R["vars"]})
    return S


def original_source_case(N, width, word):
    H = HardyNetwork(N, 1)
    S = singleton_setup(H, width, word)
    total, count = 0, 0
    k = len(S["events"])
    for h in itertools.product(range(N), repeat=len(word)):
        forms, weight, mapping, roots = flow.charged_data(H, S, h)
        # All singleton weights are ORIGINAL Cartan/pivot/root phases.
        assert pow(weight, 4 * N, H.p) == 1
        graph = flow.graph_blocks(H, S, h)
        for j in range(len(word)):
            lengths = [e["length"] for e in graph["blocks"] if e["event"] == j]
            assert sorted(lengths) == sorted(v for v in [N - 1 - h[j], h[j]] if v)
        coefficient = flow.charged_coefficient(forms, k, N - 1, H.p)
        total = (total + weight * coefficient) % H.p
        count += 1
    assert count == N**len(word)
    core = total * inv(N, H.p) % H.p
    W = word_matrix(word, H.plus, H.minus, width, N, H.p)
    cut = partial(W, H.pivot, width, N, H.p)
    assert np.array_equal(cut, np.diag(np.diag(cut)))
    expected = int(cut.sum()) * inv(N, H.p) % H.p
    assert core == expected
    chi = H.dimension * pow(H.twist, -sum(1 if j > 0 else -1 for j in word), H.p) % H.p
    return {"N": N, "width": width, "word": word,
            "exact_singleton_clock_states": count,
            "original_core": core, "full_original_scalar": core * chi % H.p}


def compositions(d, r):
    if r == 1:
        yield (d,)
        return
    for a in range(d + 1):
        for rest in compositions(d - a, r - 1):
            yield (a,) + rest


def metric_case(N, r):
    mp.mp.dps = 60
    Q = mp.exp(2j * mp.pi / N)
    F = [mp.mpc(1)]
    for a in range(1, N):
        F.append(F[-1] * (1 - Q**a))
    s = [abs(z) for z in F]
    D = [mp.sqrt(z) / mp.root(N, 4) for z in s]
    for a in range(N):
        assert abs(D[a] * D[N - 1 - a] - 1) < mp.mpf("1e-50")
    norm_from_original_Gamma = mp.mpf(0)
    positive_partition = mp.mpf(0)
    states = 0
    for ns in compositions(N - 1, r):
        hs = [sum(ns[j:]) for j in range(1, r)]
        gamma = F[hs[0]] / (F[hs[-1]] * mp.fprod(F[a] for a in ns[1:-1]))
        transformed = abs(gamma) * mp.fprod(D[a] for a in ns)
        predicted = N**(mp.mpf(1) - mp.mpf(r) / 4) / mp.sqrt(mp.fprod(s[a] for a in ns))
        assert abs(transformed / predicted - 1) < mp.mpf("1e-50")
        norm_from_original_Gamma += transformed**2
        positive_partition += 1 / mp.fprod(s[a] for a in ns)
        states += 1
    predicted_norm = N**(mp.mpf(2) - mp.mpf(r) / 2) * positive_partition
    assert abs(norm_from_original_Gamma / predicted_norm - 1) < mp.mpf("1e-50")
    if r == 2:
        assert abs(positive_partition - 1) < mp.mpf("1e-50")
        assert abs(norm_from_original_Gamma - N) < mp.mpf("1e-50")
    return {"N": N, "composition_length": r, "states": states,
            "exact_source_norm_squared": float(norm_from_original_Gamma)}


def main():
    original = [original_source_case(N, width, word) for N, width, word in [
        (2, 2, [1, 1, 1]), (3, 2, [1, 1, 1]), (4, 2, [1, -1, 1]),
        (2, 3, [1, -2]), (3, 3, [1, -2]),
        (2, 3, [1, -2, 1, -2]), (3, 3, [1, -2, 1, -2]),
        (2, 4, [1, -2, 3]), (3, 4, [1, 2, 3]),
    ]]
    metrics = [metric_case(N, r) for N in range(2, 13) for r in range(2, 6)]
    result = {"status": "PASS", "original_signed_sources": original,
              "length_metric_and_original_Gamma": metrics,
              "total_original_clock_states": sum(c["exact_singleton_clock_states"] for c in original),
              "scope": "source norms only; no geometric energy bound inferred"}
    Path(__file__).with_name("actual_length_gauge_clock_source_results.json").write_text(
        json.dumps(result, indent=2) + "\n")
    print(f"PASS {len(original)} original signed sources / "
          f"{result['total_original_clock_states']} clock states; "
          f"{len(metrics)} exact Gamma/Riesz composition families")


if __name__ == "__main__":
    main()
