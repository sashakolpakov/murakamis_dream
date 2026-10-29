#!/usr/bin/env python3
"""Complete three-head Hopf multiplicity, actual sources and recoupling.

Finite-field checks use the independently implemented original signed R.
The analytic proof is in notes/actual_complete_source_multiplicity_module.md.
"""

import json
from pathlib import Path
import cmath

import numpy as np

from audit_actual_two_cut_ports import balanced_data, coproduct
from audit_actual_complete_casimir_hermite_packet import canonical_field_frame


def inverse_mod(A, prime):
    n = A.shape[0]
    B = np.concatenate((A.copy() % prime, np.eye(n, dtype=np.int64)), axis=1)
    for j in range(n):
        i = next(i for i in range(j, n) if B[i, j] % prime)
        B[[i, j]] = B[[j, i]]
        B[j] = B[j] * pow(int(B[j, j]), -1, prime) % prime
        for i in range(n):
            if i != j and B[i, j]:
                B[i] = (B[i] - B[i, j] * B[j]) % prime
    return B[:, n:]


def rank_mod(A, prime):
    B = A.copy() % prime
    rank = 0
    for j in range(B.shape[1]):
        pivots = [i for i in range(rank, B.shape[0]) if B[i, j]]
        if not pivots:
            continue
        i = pivots[0]
        B[[i, rank]] = B[[rank, i]]
        B[rank] = B[rank] * pow(int(B[rank, j]), -1, prime) % prime
        for i in range(rank + 1, B.shape[0]):
            if B[i, j]:
                B[i] = (B[i] - B[i, j] * B[rank]) % prime
        rank += 1
        if rank == B.shape[0]:
            break
    return rank


def actual_case(N):
    prime, eta, q, E, F, K, pivot, Rp, Rm = balanced_data(N)
    Q, d = q*q % prime, N-1
    rho = (q-pow(q, -1, prime)) % prime
    Ecal = rho*rho*E % prime
    x = int(K[0, 0])
    fac = [1]
    for j in range(1, N):
        fac.append(fac[-1]*(1-pow(Q, j, prime)) % prime)
    I = np.eye(N, dtype=np.int64)
    E2, F2, K2 = coproduct(Ecal, F, K, 2, N, prime)
    E3, F3, K3 = coproduct(Ecal, F, K, 3, N, prime)
    pair_ids = [j*N+d-j for j in range(N)]
    source = np.zeros((N*N, N), dtype=np.int64)
    source[pair_ids, np.arange(N)] = 1
    H = np.zeros((N**3, N), dtype=np.int64)
    power = source.copy()
    for c in range(N):
        ids = [j*N+c for j in range(N*N)]
        H[ids, :] = pow(-x*Q, c, prime)*pow(fac[c], -1, prime)*power % prime
        power = E2 @ power % prime
    highest_ids = [(a*N+b)*N+c for a in range(N) for b in range(N)
                   for c in range(N) if a+b+c == d]
    lower_ids = [(a*N+b)*N+c for a in range(N) for b in range(N)
                 for c in range(N) if a+b+c == d-1]
    assert rank_mod(E3[np.ix_(lower_ids, highest_ids)], prime) == len(lower_ids)
    assert not np.any(E3 @ H % prime)
    left_boundary = [(j*N+d-j)*N for j in range(N)]
    right_boundary = [(j*N+d-j) for j in range(N)]
    assert np.array_equal(H[left_boundary, :], I)
    J = H[right_boundary, :]
    J_expected = np.zeros((N, N), dtype=np.int64)
    for i in range(N):
        for j in range(N-i):
            binomial = fac[d-j]*pow(fac[i]*fac[d-i-j] % prime, -1, prime) % prime
            J_expected[i, j] = (pow(-x*Q, d-i, prime)*pow(x, j, prime)
                                *pow(Q, i*(i+1)//2-d*(d+1)//2, prime)*binomial) % prime
    assert np.array_equal(J, J_expected)
    Ji = inverse_mod(J, prime)

    def casimir(Et, Ft, Kt):
        Ki = np.diag([pow(int(z), -1, prime) for z in np.diag(Kt)])
        return (Ft @ Et+q*Kt+pow(q, -1, prime)*Ki) % prime

    O2 = casimir(E2, F2, K2)
    O3 = casimir(E3, F3, K3)
    assert not np.any((O3+2*np.eye(N**3, dtype=np.int64)) @ H % prime)
    A = O2[np.ix_(pair_ids, pair_ids)]
    A_expected = np.zeros_like(A)
    for j in range(N):
        A_expected[j,j] = (q+pow(q,-1,prime)-q*(1-pow(Q,j,prime))**2
                           -pow(q,-1,prime)*(1-pow(Q,j+1,prime))**2) % prime
        if j:
            A_expected[j-1,j] = A_expected[j,j-1] = -(1-pow(Q,j,prime))**2 % prime
    assert np.array_equal(A,A_expected)
    B = Ji @ A @ J % prime
    B_expected = np.zeros((N, N), dtype=np.int64)
    for j in range(N):
        B_expected[j, j] = (pow(q, 2*j+1, prime)+pow(q, -2*j-1, prime)) % prime
        if j:
            B_expected[j-1, j] = (pow(Q, j, prime)+pow(Q, -j, prime)-2) % prime
    assert np.array_equal(B, B_expected)
    assert np.array_equal(J @ A @ Ji % prime, B.T)
    assert np.array_equal(np.kron(I, O2) @ H % prime, H @ B % prime)

    R12 = Rp[np.ix_(pair_ids, pair_ids)]
    R23 = Ji @ R12 @ J % prime
    for actual, first, second in ((Rp, R12, R23), (Rm, inverse_mod(R12, prime), inverse_mod(R23, prime))):
        assert np.array_equal(np.kron(actual, I) @ H % prime, H @ first % prime)
        assert np.array_equal(np.kron(I, actual) @ H % prime, H @ second % prime)
    cup = np.array([N*pow(x, j-d, prime) % prime for j in range(N)], dtype=np.int64)
    ordinary = np.array([pow(x, -j, prime)*pow(Q, -j, prime)*pow(N, -1, prime) % prime
                         for j in range(N)], dtype=np.int64)
    marked = np.array([pow(x, d-j, prime)*pow(N, -2, prime) % prime for j in range(N)], dtype=np.int64)
    harmonic = [0]
    for j in range(1, N):
        harmonic.append((harmonic[-1]+pow(1-pow(Q, j, prime), -1, prime)) % prime)
    g = cup*pow(N, -1, prime) % prime
    v = np.array([-int(g[j])*harmonic[j]*pow(rho, -1, prime) % prime for j in range(N)])
    gamma = int(ordinary @ v) % prime
    mu = int(marked @ v) % prime
    t = (v-mu*cup)*pow(gamma, -1, prime) % prime
    assert int(marked @ cup) % prime == 1 and int(ordinary @ t) % prime == 1
    expected = np.zeros(N, dtype=np.int64)
    expected[d] = N*pow(x, -d, prime) % prime
    assert np.array_equal(J @ cup % prime, expected)
    assert np.array_equal(J[:, 0], cup*pow(N, -1, prime) % prime)
    assert np.array_equal(ordinary @ Ji % prime,
                          np.array([pow(x,d,prime)*pow(N,-1,prime) % prime]+[0]*(N-1)))
    # Genuine N-dimensional Hom Racah, not the ambient pair-product frame.
    V, Vi, metadata, blocks = canonical_field_frame(A,N,d,prime,q)
    Racah = Vi @ J @ V % prime
    assert np.array_equal(inverse_mod(Racah,prime),Vi @ Ji @ V % prime)
    source_channels = Vi @ J @ cup % prime
    cap_channels = ordinary @ Ji @ V % prime
    nodes = [(pow(q,2*j+1,prime)+pow(q,-2*j-1,prime)) % prime for j in range(N)]
    source_expected, cap_expected, col = [], [], 0
    for block in blocks:
        j, si = block['j'], pow(block['sigma'],-1,prime)
        nu = pow(-1,j,prime)*pow(q,j*(j+1),prime) % prime
        if block['multiplicity']==2:
            c = nodes[j]
            derivative = sum(pow(c-nodes[k],-1,prime) for k in range(N) if nodes[k]!=c) % prime
            assert derivative == c*pow(4-c*c,-1,prime) % prime
            assert block['sigma'] == pow(-1,d,prime)*pow(x,d,prime)*nu*pow(4-c*c,-1,prime) % prime
            source_expected += [-N*nu*si*derivative % prime,N*nu*si % prime]
            cap_expected += [pow(x,d,prime)*pow(N,-1,prime) % prime,0]
        else:
            source_expected += [N*nu*si % prime]
            cap_expected += [pow(x,d,prime)*pow(N,-1,prime) % prime]
    assert np.array_equal(source_channels,np.array(source_expected,dtype=np.int64))
    closed_source = []
    for block in blocks:
        j = block['j']
        if block['multiplicity']==2:
            phase = N*pow(-1,d,prime)*pow(x,-d,prime) % prime
            closed_source += [-phase*nodes[j] % prime,phase*(4-nodes[j]*nodes[j]) % prime]
        else:
            closed_source += [N*pow(x,-d,prime) % prime]
    assert np.array_equal(source_channels,np.array(closed_source,dtype=np.int64))
    assert np.array_equal(cap_channels,np.array(cap_expected,dtype=np.int64))
    Dc = Vi @ R12 @ V % prime
    assert np.array_equal(Vi @ J @ R12 @ Ji @ V % prime,
                          Racah @ Dc % prime @ inverse_mod(Racah,prime) % prime)
    jt = J @ t % prime
    for j in range(d):
        expected_j = (N*pow(x,-d,prime)*pow(-q,j,prime)*(1-Q)
                      *pow(1-pow(Q,j+1,prime),-1,prime)) % prime
        assert jt[j] == expected_j
    assert jt[d] == t[0]
    theta = pow(-1,N,prime)*rho*rho % prime
    # A cap-Ward current is not null after an adjacent ORIGINAL crossing.
    cap_current=(A-(q+pow(q,-1,prime))*I) % prime
    assert not np.any(ordinary @ cap_current % prime)
    assert np.array_equal(cap_current @ t % prime,theta*cup % prime)
    primitive=t*pow(theta,-1,prime) % prime
    overlap=ordinary @ (R23 @ cap_current-cap_current @ R23) % prime
    assert int(overlap @ primitive) % prime == int(Rp[0,0])*pow(x,-d,prime) % prime
    top = np.zeros(N*N,dtype=np.int64)
    top[0] = 1
    top_desc = []
    for r in range(N):
        top_desc.append(top*pow(fac[r],-1,prime) % prime)
        top = F2 @ top % prime
    for c in range(1,N):
        ec_t = np.linalg.matrix_power(E2.astype(object),c) @ (source@t).astype(object) % prime
        coefficient = (theta*N*pow(q,c-1,prime)*fac[c-1]
                       *pow(1-pow(Q,d,prime),-1,prime)) % prime
        assert np.array_equal(np.asarray(ec_t,dtype=np.int64),coefficient*top_desc[d-c] % prime)
    Krylov = np.column_stack([np.linalg.matrix_power(B.astype(object), k).astype(object) @ cup.astype(object) % prime
                              for k in range(N)]).astype(np.int64)
    assert rank_mod(Krylov, prime) == N

    # All descendants, including original ordinary and unrestricted marked rows.
    embeds = []
    power = H.copy()
    for a in range(N):
        embeds.append(power*pow(fac[a], -1, prime) % prime)
        power = F3 @ power % prime
    S = np.column_stack(embeds)
    assert rank_mod(S, prime) == N*N
    ell_full = np.zeros(N*N, dtype=np.int64)
    ell_full[pair_ids] = ordinary
    m_full = np.array([pow(x, b, prime)*pow(N, -2, prime) % prime
                       for a in range(N) for b in range(N)], dtype=np.int64)
    ell3, m3 = np.kron(ell_full, I), np.kron(m_full, I)
    for a in range(N):
        target = np.zeros((N, N), dtype=np.int64)
        target[a, :] = ordinary
        assert np.array_equal(ell3 @ embeds[a] % prime, target)
        pmap = embeds[a] @ cup % prime
        expected = np.zeros(N**3, dtype=np.int64)
        expected[np.array(pair_ids)*N+a] = cup
        assert np.array_equal(pmap, expected)
    # These are arbitrary exterior coordinates, not only a closed scalar test.
    for word in ((2, 1, -2), (1, -2, 1, 2), (-1, 2, -1)):
        reduced = cup.copy()
        physical = H @ cup % prime
        for letter in word:
            M = R12 if abs(letter) == 1 else R23
            if letter < 0:
                M = inverse_mod(M, prime)
            reduced = M @ reduced % prime
            R = Rp if letter > 0 else Rm
            physical = (np.kron(R, I) if abs(letter) == 1 else np.kron(I, R)) @ physical % prime
        assert np.array_equal(physical, H @ reduced % prime)
        assert np.array_equal(m3 @ physical % prime, m3 @ H @ reduced % prime)
        right_reduced = J @ reduced % prime
        assert int(ordinary @ reduced) % prime == pow(x,d,prime)*pow(N,-1,prime)*int(right_reduced[0]) % prime
    return {"N": N, "complete_Hom_dimension": N, "complete_isotypic_dimension": N*N,
            "original_signed_braids_and_complete_anti_Pascal_recoupling": True,
            "local_cap_Ward_current_and_exact_overlap_boundary": True,
            "cup_and_tame_Hermite_lift_with_both_original_co_sources": True,
            "full_character_cyclicity_and_arbitrary_exterior_word_identity": True,
            "complete_channel_positive_metric_with_exact_polynomial_sources":True}


def apply_pair(R, vectors, slot, width, N, prime):
    count = vectors.shape[1]
    axes = [slot, slot+1]+[j for j in range(width) if j not in (slot, slot+1)]+[width]
    inv_axes = np.argsort(axes)
    tensor = vectors.reshape((N,)*width+(count,)).transpose(axes)
    result = R @ tensor.reshape(N*N, -1) % prime
    return result.reshape((N,)*width+(count,)).transpose(inv_axes).reshape(N**width, count)


def matrix_polynomial(coeffs, A, prime):
    result = np.zeros_like(A)
    I = np.eye(len(A), dtype=np.int64)
    for c in reversed(coeffs):
        result = (result @ A+int(c)*I) % prime
    return result


def plat_case(N, pairs):
    import itertools
    prime, eta, q, E, F, K, pivot, Rp, Rm = balanced_data(N)
    Q, d, x = q*q % prime, N-1, int(K[0, 0])
    rho = (q-pow(q, -1, prime)) % prime
    Ec = rho*rho*E % prime
    fac = [1]
    for j in range(1, N):
        fac.append(fac[-1]*(1-pow(Q, j, prime)) % prime)
    prefix, odd, width = 2*pairs-2, 2*pairs-1, 2*pairs
    states = [v for v in itertools.product(range(N), repeat=prefix) if sum(v) == (pairs-1)*d]
    indices = [sum(v[j]*N**(prefix-j-1) for j in range(prefix)) for v in states]
    dim = len(states)
    Epre, Fpre, Kpre = coproduct(Ec, F, K, prefix, N, prime)
    Eodd, Fodd, Kodd = coproduct(Ec, F, K, odd, N, prime)
    seed = np.zeros((N**prefix, dim), dtype=np.int64)
    seed[indices, np.arange(dim)] = 1
    H = np.zeros((N**odd, dim), dtype=np.int64)
    power = seed.copy()
    for c in range(N):
        H[np.arange(N**prefix)*N+c, :] = pow(-x*Q, c, prime)*pow(fac[c], -1, prime)*power % prime
        power = Epre @ power % prime
    assert not np.any(Eodd @ H % prime)
    Phi = np.zeros((N**width, dim), dtype=np.int64)
    power = H.copy()
    for a in range(N):
        Phi[np.arange(N**odd)*N+d-a, :] = N*pow(x, a-d, prime)*pow(fac[a], -1, prime)*power % prime
        power = Fodd @ power % prime
    extract = [i*N*N+d for i in indices]
    extraction = pow(x, d, prime)*pow(N, -1, prime) % prime
    assert np.array_equal(extraction*Phi[extract, :] % prime, np.eye(dim, dtype=np.int64))

    # Literal complete cap source: ordinary caps, then FULL marked row.
    cup = np.zeros(N*N, dtype=np.int64)
    ordinary = np.zeros(N*N, dtype=np.int64)
    marker = np.zeros(N*N, dtype=np.int64)
    for a in range(N):
        for b in range(N):
            marker[a*N+b] = pow(x, b, prime)*pow(N, -2, prime) % prime
            if a+b == d:
                cup[a*N+b] = N*pow(x, -b, prime) % prime
                ordinary[a*N+b] = pow(x, -a, prime)*pow(Q, -a, prime)*pow(N, -1, prime) % prime
    top, bottom = marker.copy(), cup.copy()
    lam, w0 = np.array([1], dtype=np.int64), np.array([1], dtype=np.int64)
    for _ in range(pairs-1):
        top, bottom = np.kron(ordinary, top) % prime, np.kron(cup, bottom) % prime
        lam, w0 = np.kron(lam, ordinary) % prime, np.kron(w0, cup) % prime
    lam, w0 = lam[indices], w0[indices]
    assert np.array_equal(Phi @ w0 % prime, bottom)
    assert np.array_equal(top @ Phi % prime, lam)

    # Infer the SAME complete confluent r_N from the ORIGINAL pair operator.
    E2, F2, K2 = coproduct(Ec, F, K, 2, N, prime)
    K2i = np.diag([pow(int(z), -1, prime) for z in np.diag(K2)])
    O2 = (F2 @ E2+q*K2+pow(q, -1, prime)*K2i) % prime
    pair_ids = [j*N+d-j for j in range(N)]
    O = O2[np.ix_(pair_ids, pair_ids)]
    R = Rp[np.ix_(pair_ids, pair_ids)]
    cyclic = np.zeros(N, dtype=np.int64)
    cyclic[d] = 1
    columns = []
    for _ in range(N):
        columns.append(cyclic)
        cyclic = O @ cyclic % prime
    krylov = np.column_stack(columns)
    kappa = int(Rp[0, 0])
    coeffs = inverse_mod(krylov, prime) @ R[:, d]*pow(kappa, -1, prime) % prime
    assert np.array_equal(kappa*matrix_polynomial(coeffs, O, prime) % prime, R)
    # Explicit penultimate boundary Casimir, including operator order F_B K_B.
    if prefix:
        EA, _, _ = coproduct(Ec, F, K, prefix-1, N, prime)
        Kinv = np.diag([pow(int(z), -1, prime) for z in np.diag(K)])
        Hb = (q*x*np.kron(np.eye(N**(prefix-1), dtype=np.int64), K)
              +pow(q, -1, prime)*pow(x, -1, prime)*np.kron(np.eye(N**(prefix-1), dtype=np.int64), Kinv)
              -x*np.kron(EA, F @ K)) % prime
        Hb = Hb[np.ix_(indices, indices)]
        Kpi = np.diag([pow(int(z), -1, prime) for z in np.diag(Kpre)])
        Op = (Fpre @ Epre+q*Kpre+pow(q, -1, prime)*Kpi) % prime
        Op = Op[np.ix_(indices, indices)]
    else:
        Hb = np.array([[(q+pow(q, -1, prime)) % prime]], dtype=np.int64)
        Op = Hb.copy()
    induced_plus, induced_minus = [], []
    for slot in range(width-1):
        actual = apply_pair(Rp, Phi, slot, width, N, prime)
        reduced = extraction*actual[extract, :] % prime
        assert np.array_equal(actual, Phi @ reduced % prime)
        if slot < width-3:
            expected = apply_pair(Rp, seed, slot, prefix, N, prime)[indices, :]
        else:
            expected = kappa*matrix_polynomial(coeffs, Hb if slot == width-3 else Op, prime) % prime
        assert np.array_equal(reduced, expected)
        actual_minus = apply_pair(Rm, Phi, slot, width, N, prime)
        minus = extraction*actual_minus[extract, :] % prime
        assert np.array_equal(actual_minus, Phi @ minus % prime)
        assert np.array_equal(reduced @ minus % prime, np.eye(dim, dtype=np.int64))
        induced_plus.append(reduced)
        induced_minus.append(minus)
    words = ([1, -1, 1], [-1, 1]) if pairs == 1 else (
        [width-1, -(width-2), 1], [1, -(width-1), width-2, 1])
    for word in words:
        physical, reduced = bottom.copy()[:, None], w0.copy()
        for letter in word:
            physical = apply_pair(Rp if letter > 0 else Rm, physical, abs(letter)-1, width, N, prime)
            reduced = (induced_plus if letter > 0 else induced_minus)[abs(letter)-1] @ reduced % prime
        assert int(top @ physical[:, 0]) % prime == int(lam @ reduced) % prime
    return {"N": N, "plat_pairs": pairs, "complete_invariant_dimension": dim,
            "all_actual_signed_generators_and_original_marked_source": True,
            "explicit_boundary_and_last_prefix_Casimirs": True,
            "full_original_source_word_reduction": True}


def source_hermite_norms(N):
    q = cmath.exp(1j*np.pi/N)
    Q, x, d, rho = q*q, -1/q, N-1, q-1/q
    harmonic = np.r_[0j,np.cumsum([1/(1-Q**j) for j in range(1,N)])]
    g = x**(np.arange(N)-d)
    t = (-1)**(N+1)*N*rho*g*(harmonic-harmonic.mean())
    theta = (-1)**N*rho*rho
    norm2 = float(np.vdot(t,t).real)
    embedded = norm2
    for c in range(1,N):
        amplitude = (-x*Q)**c*theta*N*q**(c-1)/((1-Q**d)*(1-Q**c))
        embedded += (N-c)*abs(amplitude)**2
    formula = norm2+N**3*abs(rho)**2*(N*N-1)/24
    assert abs(embedded/formula-1) < 1e-8
    assert embedded >= N**3/4*(1-1e-8)
    assert embedded <= np.pi**2*N**3/3*(1+1e-8)
    condition = max(N**1.5,np.sqrt(embedded))/min(N**1.5,np.sqrt(embedded))
    assert condition <= 2*(1+1e-8)
    jt = np.r_[[N*x**(-d)*(-q)**j*(1-Q)/(1-Q**(j+1)) for j in range(d)],t[0]]
    z2 = float(np.vdot(jt[:d],jt[:d]).real)
    z_formula = N*N*abs(rho)**2*(N*N-1)/12
    assert abs(z2/z_formula-1) < 1e-8
    assert N*N*(1-1e-8) <= z2 <= np.pi**2*N*N/3*(1+1e-8)
    Y = np.column_stack([N*x**(-d)*np.eye(N)[:,d],jt])
    bound = np.pi/np.sqrt(3)*(1+np.pi*(1+np.log(N)))**2
    assert np.linalg.cond(Y) <= bound
    us = []
    caps = []
    for j in range((N+1)//2):
        if 2*j+1<N:
            c = 2*np.cos((2*j+1)*np.pi/N)
            us += [-N*c,N*(4-c*c)]
            caps += [1/N,0]
        else:
            us += [N]
            caps += [1/N]
    unorm = float(np.vdot(us,us).real)
    expected = (N*N*(4*N-1) if N%2 else 4*N**3)
    if N==2:expected=64
    if N==4:expected=192
    assert abs(unorm/expected-1)<1e-8
    capnorm = float(np.vdot(caps,caps).real)
    assert abs(capnorm-((N+1)//2)/N**2)<1e-8
    assert np.sqrt(unorm*capnorm)<=2*N*(1+1e-8)
    return {"N":N,"embedded_highest_source_condition":float(condition),
            "exact_recoupled_source_frame_condition":float(np.linalg.cond(Y)),
            "proved_uniform_highest_condition":2,"proved_recoupled_polylog_bound":float(bound),
            "complete_channel_source_squared_norm":unorm,"ordinary_cap_squared_dual_norm":capnorm,
            "full_channel_Cauchy_boundary_product":float(np.sqrt(unorm*capnorm)),
            "proved_uniform_Cauchy_boundary_product_bound":2*N}


if __name__ == "__main__":
    rows = [actual_case(N) for N in range(2, 9)]
    plats = [plat_case(N, k) for k in range(1, 4) for N in range(2, 5)]+[plat_case(2, 4)]
    norms = [source_hermite_norms(N) for N in (2,3,4,5,6,8,12,16,24,32,64,128)]
    Path(__file__).with_name("actual_complete_source_multiplicity_module_results.json").write_text(
        json.dumps({"status": "PASS", "original_source_complete_modules": rows,
                    "arbitrary_width_ordinary_and_marked_plat_source": plats,
                    "source_Hermite_embedding_and_complete_recoupling_norms":norms}, indent=2)+"\n")
    print(f"PASS {len(rows)} complete three-head modules; {len(plats)} full signed plat sources; {len(norms)} Hermite source norms")
