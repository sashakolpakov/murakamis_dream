#!/usr/bin/env python3
"""Actual cap Fourier resolution, Nakayama line and cyclic transport.

No sector is identified with a geometric period. Exact finite fields
check explicit algebra and original signed-word sources.
"""
import json
import math
from pathlib import Path

import numpy as np

from audit_actual_borel_regular_fusion import (
    alg_product, fusion, inv, physical_cap, right_regular,
)
from audit_actual_two_cut_ports import balanced_data, word_matrix, coproduct
from audit_all_strand_cauchy_cap import tail_blocks


def algebra(N, p, Q, x):
    one = np.zeros(N*N, dtype=np.int64)
    one[:N] = 1
    f = np.zeros_like(one)
    f[N:2*N] = 1
    H = one.copy()
    H[:N] = [pow(Q, -j, p) for j in range(N)]
    fac = [1]
    for a in range(1, N):
        fac.append(fac[-1]*(1-pow(Q, a, p)) % p)
    u, v, J = (one.copy() for _ in range(3))
    for a in range(1, N):
        u[a*N:(a+1)*N] = pow(x, a, p)*pow(fac[a], -1, p) % p
        v[a*N:(a+1)*N] = (pow(-1, a, p)*pow(Q, a*(a-1)//2, p)
                              *pow(x, a, p)*pow(fac[a], -1, p)) % p
        J[a*N:(a+1)*N] = (pow(x, a, p)*(1-pow(Q, a+1, p))
                              *pow(1-Q, -1, p)) % p
    def mul(a, b):
        return alg_product(a, b, N, 0, p)
    def power(a, k):
        out = one.copy()
        for _ in range(k):
            out = mul(out, a)
        return out
    def inverse_unit(a):
        n = (one-a) % p
        out, term = one.copy(), one.copy()
        for _ in range(1, N):
            term = mul(term, n)
            out = (out+term) % p
        assert np.array_equal(mul(a, out), one)
        return out
    def nu(a):
        return np.roll(a.reshape(N, N), 1, axis=1).reshape(N*N)
    def tau(a):
        return int(a[(N-1)*N:].sum()) % p
    return one, f, H, u, v, J, mul, power, inverse_unit, nu, tau


def local_case(N):
    p, _, q, _, _, K, _, plus, _ = balanced_data(N)
    Q, x = q*q % p, int(K[0, 0])
    one, f, H, u, v, J, mul, power, inverse_unit, nu, tau = algebra(N, p, Q, x)
    e = np.zeros_like(one)
    e[N-1] = 1
    E = mul(e, J)
    s = np.zeros_like(one)
    s[(N-1)*N] = 1
    Ffusion, Ffusion_i, _, _, _, _, _ = fusion(N, p, Q, [x, x], [0, 0])
    cword = Ffusion_i@plus@Ffusion % p@one % p
    cdiag_inverse = np.zeros_like(one)
    cdiag_inverse[:N] = [pow(int(t), -1, p) for t in cword[:N]]
    cword_i = mul(inverse_unit(mul(cdiag_inverse, cword)), cdiag_inverse)
    assert np.array_equal(mul(cword, cword_i), one)
    assert np.array_equal(mul(E, E), E) and tau(E) == 0
    line_units = 0
    for i in range(N*N):
        a = np.eye(N*N, dtype=np.int64)[:, i]
        compressed = mul(mul(E, a), nu(E))
        value = int(mul(J, a)[(N-1)*N])
        assert np.array_equal(compressed, value*s % p)
        assert not np.any(mul(mul(E, a), E)) or tau(mul(mul(E, a), E)) == 0
        line_units += 1
    resolution = np.zeros_like(one)
    transport = []
    for k in range(N):
        C = mul(power(H, k), J)
        Ci = mul(inverse_unit(J), power(H, (N-k) % N))
        assert np.array_equal(mul(C, Ci), one)
        resolution = (resolution+pow(Q, (N-1)*k, p)*C) % p
        def theta(a):
            return mul(mul(C, nu(a)), Ci)
        # Exact twisted cyclic identities on deterministic basis pairs.
        for i in range(N*N):
            a = np.eye(N*N, dtype=np.int64)[:, i]
            b = np.eye(N*N, dtype=np.int64)[:, (3*i+1) % (N*N)]
            assert tau(mul(C, mul(a, b))) == tau(mul(C, mul(b, theta(a))))
        g, d = math.gcd(k, N), N//math.gcd(k, N)
        zd = power(x*f % p, d)
        den1 = (one-zd) % p
        den2 = (one-pow(Q, d, p)*zd) % p
        G = power(mul(inverse_unit(den1), inverse_unit(den2)), g)
        assert np.array_equal(power(C, N), G)
        Gi = inverse_unit(G)
        columns = []
        for i in range(N*N):
            a = np.eye(N*N, dtype=np.int64)[:, i]
            columns.append((mul(mul(G, a), Gi)-a) % p)
        delta = np.column_stack(columns)
        term = np.eye(N*N, dtype=np.int64)
        for _ in range(g):
            term = term@delta % p
        assert not np.any(term)
        if g <= 2:
            assert not np.any(delta)
            logarithm = np.zeros_like(one)
            for a in range(1, N):
                denominator = (pow(Q, k*a, p)-1) % p
                numerator = (1+pow(Q, a, p)) % p
                if not denominator:
                    assert not numerator
                    continue
                logarithm[a*N:(a+1)*N] = (pow(x, a, p)*numerator
                    *pow(a*denominator, -1, p)) % p
            gauge, logpower, factorial = one.copy(), one.copy(), 1
            for a in range(1, N):
                logpower = mul(logpower, logarithm)
                factorial = factorial*a % p
                gauge = (gauge+logpower*pow(factorial, -1, p)) % p
            shifted_gauge = np.concatenate([gauge[a*N:(a+1)*N]
                        *pow(Q, k*a, p) % p for a in range(N)])
            assert np.array_equal(shifted_gauge, mul(J, gauge))
            if k == 1:
                vshift = np.concatenate([v[a*N:(a+1)*N]*pow(Q, a, p) % p
                                         for a in range(N)])
                assert np.array_equal(gauge, mul(v, vshift))
        else:
            term = H.copy()
            for _ in range(g-1):
                term = delta@term % p
            assert np.any(term), (N, k, "nilpotence index must equal gcd")
        for generator in (H, f):
            result = generator.copy()
            for _ in range(N):
                result = theta(result)
            assert np.array_equal(result, mul(mul(G, generator), Gi))
        h = mul(cword, theta(cword_i))
        hnorm, shifted = one.copy(), h.copy()
        for _ in range(N):
            hnorm = mul(hnorm, shifted)
            shifted = theta(shifted)
        assert np.array_equal(hnorm, mul(mul(mul(cword, G), cword_i), Gi))
        test_word = (H+f) % p
        conjugate = mul(mul(cword_i, test_word), cword)
        assert tau(mul(C, conjugate)) == tau(mul(C, mul(test_word, h)))
        if k == 0 and N > 2:
            term = H.copy()
            for _ in range(N-1):
                term = delta@term % p
            assert np.any(term), (N, "zero-sector index must be exactly N")
        transport.append({"k": k, "gcd": g, "nilpotence_bound": g,
                          "primitive_finite_order": bool(g == 1),
                          "finite_order_when_gcd_at_most_two": bool(g <= 2),
                          "cyclic_nilpotence_index": 1 if g <= 2 else g,
                          "zero_sector_index_exact_N": bool(k == 0 and N > 2)})
    assert np.array_equal(resolution*pow(N, -1, p) % p, E)
    return {"N": N, "field": p, "relative_line_basis_cases": line_units,
            "transport": transport}


def word_case(N, strands, word):
    p, _, q, _, _, K, _, plus, minus = balanced_data(N)
    Q, x = q*q % p, int(K[0, 0])
    one, _, H, u, v, J, mul, power, _, nu, tau = algebra(N, p, Q, x)
    S, ys = tail_blocks(N, p, Q, [x]*(strands-1))
    r = len(ys)
    tail_frame = np.kron(np.eye(N, dtype=np.int64), S)
    C, _, _, _, _, _, _ = fusion(N, p, Q, [x, ys[0]], [0, 0])
    common = np.zeros((N**strands, N**strands), dtype=np.int64)
    labels = [0] if strands == 2 else [lam % N for lam in range(r)]
    for lam, j in enumerate(labels):
        for a in range(N):
            for k in range(N):
                physical = C[:, a*N+(k-j) % N].reshape(N, N)
                for uhead in range(N):
                    common[uhead*r*N+lam*N:uhead*r*N+(lam+1)*N,
                           lam*N*N+a*N+k] = physical[uhead, :]
    common = tail_frame@common % p
    common_i = inv(common, p)
    W = word_matrix(word, plus, minus, strands, N, p)
    relative = common_i@W@common % p
    gamma0 = N*pow(x, strands*(1-N), p)*Q % p
    sectors = np.zeros(N, dtype=np.int64)
    for target in range(r):
        for source in range(r):
            block = relative[target*N*N:(target+1)*N*N,
                             source*N*N:(source+1)*N*N]
            a = block@one % p
            assert np.array_equal(block, right_regular(a, N, 0, p))
            if target != source:
                continue
            b = mul(mul(v, a), u)
            j = labels[target]
            for k in range(N):
                Ck = mul(power(H, k), J)
                phase = pow(Q, -j+(j-1)*k, p)
                sectors[k] = (int(sectors[k])+phase*tau(mul(Ck, b))) % p
    source = int(sectors.sum())*pow(N, -1, p) % p
    literal = physical_cap(W, [K]*strands, N, p)
    assert gamma0*source % p == literal
    return {"N": N, "strands": strands, "word": list(word), "field": p,
            "unit_source_sector_values": sectors.tolist(),
            "average_source": source, "original_physical_cap": literal,
            "common_frame_full_matrix_blocks": r*r}


def e_commutation_witness():
    N = 2
    p, _, q, Ephysical, Fphysical, Kphysical, _, plus, _ = balanced_data(N)
    Q, x = q*q % p, int(Kphysical[0, 0])
    one, _, H, u, v, J, mul, _, inverse_unit, nu, _ = algebra(N, p, Q, x)
    C, Ci, _, _, _, _, _ = fusion(N, p, Q, [x, x], [0, 0])
    a = Ci@plus@C % p@one % p
    b = mul(mul(v, a), u)
    transformed = mul(mul(u, mul(mul(J, nu(b)), inverse_unit(J))), v)
    Wprime = C@right_regular(transformed, N, 0, p)@Ci % p
    Etotal, _, _ = coproduct(Ephysical, Fphysical, Kphysical, 2, N, p)
    assert not np.any((Etotal@plus-plus@Etotal) % p)
    residual = (Etotal@Wprime-Wprime@Etotal) % p
    assert np.any(residual)
    return {"N": N, "field": p, "actual_positive_crossing_is_E_linear": True,
            "sector_zero_transformed_word_is_E_linear": False,
            "exact_nonzero_E_commutator": residual.tolist()}


def main():
    local = [local_case(N) for N in range(2, 9)]
    words = [word_case(3, 2, (1,)), word_case(3, 2, (1, 1, 1)),
             word_case(3, 3, (1, -2, 1, -2)),
             word_case(3, 3, (1, 1, -2, 1, -2, -1)),
             word_case(4, 3, (1, -2, 1, -2)),
             word_case(3, 4, (1, -2, 3, 1, -2, 3))]
    assert len(set(words[0]["unit_source_sector_values"])) > 1
    p = words[0]["field"]
    left = [x*pow(words[0]["average_source"], -1, p) % p
            for x in words[0]["unit_source_sector_values"]]
    right = [x*pow(words[1]["average_source"], -1, p) % p
             for x in words[1]["unit_source_sector_values"]]
    assert left != right
    assert words[2]["average_source"] == words[3]["average_source"]
    assert words[2]["unit_source_sector_values"] != words[3]["unit_source_sector_values"]
    result = {"status": "PASS", "local": local, "actual_words": words,
              "E_commutation_obstruction": e_commutation_witness(),
              "scope": "Exact original-source Fourier resolution on a common whole-word matrix algebra, relative Nakayama line and sharp growing nilpotence; no geometric selected-period or volume assertion."}
    Path(__file__).with_name("actual_source_fourier_twisted_traces_results.json").write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"status": result["status"], "levels": len(local),
                      "actual_words": len(words), "sector_witnesses": words[:2]}))


if __name__ == "__main__":
    main()
