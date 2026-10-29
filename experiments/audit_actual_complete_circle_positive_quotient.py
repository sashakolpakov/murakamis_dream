#!/usr/bin/env python3
"""Actual Hopf quotient, angle metric, circle sewing and whole-source caps."""

import json
from pathlib import Path

import mpmath as mp
import numpy as np

from audit_actual_two_cut_ports import balanced_data, coproduct
from audit_actual_complete_source_multiplicity_module import rank_mod
from audit_actual_half_clock_source_dilation import original_factorial_R


def circle(O, N):
    a, b = mp.eye(O.rows), O.copy()
    for _ in range(2, N):
        a, b = b, O*b-a
    return (-1)**(N-1)*b


def field_case(N):
    p, eta, q, E, F, K, pivot, Rp, Rm = balanced_data(N)
    d, Q, rho = N-1, q*q % p, (q-pow(q, -1, p)) % p
    Et, Ft, Kt = coproduct(rho*rho*E % p, F, K, 2, N, p)
    I = np.eye(N*N, dtype=np.int64)
    Ki = np.diag([pow(int(z), -1, p) for z in np.diag(Kt)])
    O = (Ft@Et+q*Kt+pow(q, -1, p)*Ki) % p
    a, b = I, O
    for _ in range(2, N):
        a, b = b, (O@b-a) % p
    L = pow(-1, d, p)*b % p
    nodes = [(pow(q, 2*j+1, p)+pow(q, -2*j-1, p)) % p for j in range(d//2+1)]
    fac = [1]
    for r in range(1, N):
        fac.append(fac[-1]*(1-pow(Q, r, p)) % p)
    images, labels = [], []
    for j, c in enumerate(nodes):
        projector = I.copy()
        for ell, other in enumerate(nodes):
            if ell != j:
                projector = (O-other*I)@projector % p
                projector = projector*pow(c-other, -1, p) % p
        w = projector[:, d-j].copy()  # physical |0,d-j>
        y = L@w % p
        assert np.any(y) and not np.any(Et@y % p)
        n = 2*j
        previous = None
        for r in range(n+1):
            current = L@w % p
            assert np.any(current)
            assert np.array_equal(Kt@current % p,pow(q, n-2*r, p)*current % p)
            assert np.array_equal(O@current % p,c*current % p)
            if r:
                coefficient = (pow(q, -n-1, p)*(1-pow(Q, n+1-r, p))) % p
                assert np.array_equal(Et@current % p,coefficient*previous % p)
            else:
                assert not np.any(Et@current % p)
            nu = pow(-1, j, p)*pow(q, j*(j+1), p) % p
            assert np.array_equal(Rp@current % p,int(Rp[0, 0])*nu*current % p)
            value = N if 2*j==d else 0
            assert np.array_equal(L@current % p,value*current % p)
            images.append(current); labels.append((j, r))
            previous = current
            if r<n:
                w = Ft@w % p
                w = w*pow(1-pow(Q, r+1, p), -1, p) % p
            else:
                assert not np.any(Ft@current % p)
    expected = ((N+1)//2)**2
    assert rank_mod(np.column_stack(images), p)==expected==rank_mod(L, p)
    # COMPLETE source highest spaces after a circle, including both leg orders.
    Ec = rho*rho*E % p
    E3 = (np.kron(Et, K)+np.kron(I, Ec)) % p
    lookup = dict(zip(labels, images))
    highest_left, highest_right = [], []
    for j in range(d//2+1):
        hl = np.zeros(N**3, dtype=np.int64); hr = hl.copy()
        for r in range(j+1):
            alpha = (pow(Q, j*r, p)*fac[j]*fac[2*j-r]
                     *pow(fac[j-r]*fac[2*j] % p, -1, p)) % p
            head = np.zeros(N, dtype=np.int64); head[j-r] = 1
            hl = (hl+alpha*np.kron(lookup[j,r], head)) % p
            hr = (hr+alpha*pow(int(K[0,0]), -r, p)*np.kron(head, lookup[j,r])) % p
        assert np.any(hl) and np.any(hr)
        assert not np.any(E3@hl % p) and not np.any(E3@hr % p)
        highest_left.append(hl); highest_right.append(hr)
    assert rank_mod(np.column_stack(highest_left), p)==d//2+1
    assert rank_mod(np.column_stack(highest_right), p)==d//2+1
    # Exact entire-block braiding; no split-pair quotient is asserted.
    if N<=5:
        eye = np.eye(N, dtype=np.int64)
        block = np.kron(Rp, eye)@np.kron(eye, Rp) % p
        assert np.array_equal(block@np.kron(L, eye) % p,
                              np.kron(eye, L)@block % p)
    return {'N': N, 'complete_ordinary_Hopf_quotient_dimension': expected,
            'all_ladder_endpoints_and_full_Cartan_twists': True,
            'both_complete_source_Hom_dimensions': d//2+1,
            'whole_block_naturality_tested': N<=5}


def complex_case(N):
    mp.mp.dps = 85
    d = N-1
    q = mp.exp(mp.j*mp.pi/N); Q = q*q; x = q**d
    fac, s = [mp.mpc(1)], [mp.mpf(1)]
    for r in range(1, N):
        fac.append(fac[-1]*(1-Q**r)); s.append(abs(fac[-1]))
    ids = {T: list(range(max(0, T-d), min(d, T)+1)) for T in range(2*d+1)}
    O, L, C, P, E, F = {}, {}, {}, {}, {}, {}
    for T, aa in ids.items():
        index = {a: j for j, a in enumerate(aa)}
        omega = mp.matrix(len(aa)); swap = mp.matrix(len(aa))
        for j, a in enumerate(aa):
            b = T-a
            omega[j, j] = ((Q**(-a)-1)*x*Q**(-b)*(1-Q**a)
                +(Q**(-b)-1)/x*Q**a*(1-Q**b)
                +q*x*x*Q**(-T)+q**(-1)*x**(-2)*Q**T)
            if a+1 in index:
                val = Q**(-b)*(1-Q**b)*(1-Q**(a+1))
                omega[j, index[a+1]] = omega[index[a+1], j] = val
            swap[j, index[b]] = 1
        O[T], P[T] = omega, swap
        L[T] = circle(omega, N); C[T] = swap*L[T]
        if T<2*d:
            nxt = {a: j for j, a in enumerate(ids[T+1])}
            f = mp.matrix(len(nxt), len(aa))
            for col, a in enumerate(aa):
                b = T-a
                if a<d: f[nxt[a+1], col] += 1-Q**(a+1)
                if b<d: f[nxt[a], col] += Q**a/x*(1-Q**(b+1))
            F[T] = f
        if T:
            prev = {a: j for j, a in enumerate(ids[T-1])}
            e = mp.matrix(len(prev), len(aa))
            for col, a in enumerate(aa):
                b = T-a
                if a: e[prev[a-1], col] += (Q**(-a)-1)*x*Q**(-b)
                if b: e[prev[a], col] += Q**(-b)-1
            E[T] = e
    err = lambda A: max((abs(z) for z in A), default=mp.mpf(0))
    for T in F:
        assert err(E[T+1].H*C[T]+C[T+1]*F[T])<mp.mpf('1e-55')*max(1,err(C[T]),err(C[T+1]))
    nodes = [q**(2*j+1)+q**(-2*j-1) for j in range(d//2+1)]
    vectors = {T: [] for T in ids}; labels = {T: [] for T in ids}
    grams = {T: [] for T in ids}
    for j, c in enumerate(nodes):
        T = d-j
        proj = mp.eye(len(ids[T]))
        for ell, other in enumerate(nodes):
            if ell != j:
                proj = (O[T]-other*mp.eye(O[T].rows))*proj/(c-other)
        w = proj[:, 0]
        gj = N if 2*j==d else 2*N*s[2*j]/s[j]**2
        for r in range(2*j+1):
            vectors[T].append(w); labels[T].append((j, r))
            grams[T].append(gj*s[2*j]/(s[r]*s[2*j-r]))
            if r<2*j:
                w = F[T]*w/(1-Q**(r+1)); T += 1
    B = {}
    for T in ids:
        count = len(vectors[T])
        if not count:
            assert err(C[T])<mp.mpf('1e-55')
            continue
        W = mp.matrix(O[T].rows, count)
        for col, v in enumerate(vectors[T]): W[:, col] = v
        actual = W.H*C[T]*W
        expected = mp.diag(grams[T])
        assert err(actual-expected)<mp.mpf('1e-50')*max(1,err(expected))
        B[T] = mp.diag([1/mp.sqrt(g) for g in grams[T]])*W.H*C[T]
        assert err(B[T].H*B[T]-C[T])<mp.mpf('1e-50')*max(1,err(C[T]))
        sewn = B[T]*P[T]*B[T].H
        eigen = mp.diag([N if 2*j==d else 0 for j, r in labels[T]])
        assert err(sewn-eigen)<mp.mpf('1e-50')*max(1,err(C[T]))
    for T in F:
        if T not in B or T+1 not in B: continue
        fq = mp.matrix(len(labels[T+1]), len(labels[T]))
        for col, (j, r) in enumerate(labels[T]):
            if (j, r+1) in labels[T+1]:
                row = labels[T+1].index((j, r+1))
                fq[row, col] = (1-Q**(r+1))*mp.sqrt(grams[T+1][row]/grams[T][col])
                assert abs(fq[row, col])<=2*(1+mp.mpf('1e-60'))
        assert err(B[T+1]*F[T]-fq*B[T])<mp.mpf('1e-50')*max(1,err(C[T]),err(C[T+1]))
    row0 = labels[d].index((0, 0))
    ell = mp.matrix([[x**a/N for a in range(N)]])
    marked = mp.matrix([[x**(d-a)/N**2 for a in range(N)]])
    cup = mp.matrix([N*x**(a-d) for a in range(N)])
    assert err(B[d][row0, :]-mp.sqrt(2*N**3)*ell)<mp.mpf('1e-50')
    assert err((B[d]*P[d])[row0, :]-mp.sqrt(2*N**5)*marked)<mp.mpf('1e-50')
    assert err(B[d]*cup)<mp.mpf('1e-50')
    # First split-pair face, with the normalized original trivial channel.
    snake = mp.matrix(N)
    for a in range(N):
        for b in range(N):
            # I tensor pi_0 after iota_0 tensor I; complementary physical color.
            if a==b:
                snake[a,b] = mp.sqrt(2*N**3)*ell[0,d-a]*mp.sqrt(mp.mpf(2)/N)*cup[a]
    assert err(snake-2*N*mp.eye(N))<mp.mpf('1e-50')
    # Supply all physical blocks for separate whole-source positive tests.
    full = np.zeros((N*N, N*N), complex)
    all_labels = [(j,r) for j in range(d//2+1) for r in range(2*j+1)]
    pi_full = np.zeros((len(all_labels), N*N), complex)
    lift_full = np.zeros((N*N, len(all_labels)), complex)
    for T, aa in ids.items():
        indices = [a*N+T-a for a in aa]
        full[np.ix_(indices, indices)] = np.array(C[T].tolist(), complex)
        if T in B:
            rows = [all_labels.index(label) for label in labels[T]]
            pi_full[np.ix_(rows, indices)] = np.array(B[T].tolist(), complex)
            for local, global_index in enumerate(rows):
                lift_full[indices, global_index] = np.array(
                    [z/mp.sqrt(grams[T][local]) for z in vectors[T][local]], complex)
    return {'N': N, 'orthogonal_once_power_angle_metric': True,
            'full_circle_sewing_not_identity': True,
            'ordinary_and_marked_source_rows_with_leg_flip': True}, {
                'C':full,'pi':pi_full,'lift':lift_full,'labels':all_labels}


def mixed_block_case(N, data):
    q = np.exp(1j*np.pi/N); Q = q*q; d = N-1
    pi, lift, labels = data['pi'], data['lift'], data['labels']
    R = original_factorial_R(N)
    physical = np.kron(R,np.eye(N))@np.kron(np.eye(N),R)
    induced = np.kron(np.eye(N),pi)@physical@np.kron(lift,np.eye(N))
    fac = [1.+0j]
    for r in range(1,N):fac.append(fac[-1]*(1-Q**r))
    maximum_error = 0.
    for j in range(d//2+1):
        n, ell = 2*j, 2*j+1
        source = [labels.index((j,r))*N+a for r in range(ell) for a in range(N)]
        target = [a*len(labels)+labels.index((j,r)) for a in range(N) for r in range(ell)]
        observed = induced[np.ix_(target,source)]
        fq = np.zeros((ell,ell),complex); fn = np.zeros((N,N),complex)
        s = [abs(z)for z in fac]
        beta = lambda r:s[n]/(s[r]*s[n-r])
        for r in range(ell-1):fq[r+1,r]=(1-Q**(r+1))*np.sqrt(beta(r+1)/beta(r))
        for a in range(N-1):fn[a+1,a]=1-Q**(a+1)
        eq = -fq.conj().T
        nilpotent = np.eye(ell*N,dtype=complex)
        ep,fp=np.eye(ell,dtype=complex),np.eye(N,dtype=complex)
        for r in range(1,ell):
            ep=ep@eq;fp=fp@fn
            nilpotent+=(-1)**r*q**(r*r)/fac[r]*np.kron(ep,fp)
        cartan=np.diag([q**((n-2*r)*(d-2*a)/2)for r in range(ell)for a in range(N)])
        before=cartan@nilpotent
        expected=np.empty_like(before)
        for r in range(ell):
            for a in range(N):expected[a*ell+r,:]=before[r*N+a,:]
        error=np.linalg.norm(observed-expected)/max(1,np.linalg.norm(expected))
        assert error<2e-6
        maximum_error=max(maximum_error,error)
        bound=sum(4.**r/s[r]for r in range(ell))
        assert np.linalg.norm(observed,2)<=bound*(1+1e-7)
        assert np.linalg.norm(np.linalg.inv(observed),2)<=bound*(1+1e-7)
    return {'N':N,'every_ordinary_channel_full_mixed_Cartan':True,
            'maximum_relative_actual_block_error':maximum_error,
            'both_signed_finite_norm_bounds':True}


def apply_pair(v, A, slot, N, width):
    shape = (N,)*width
    order = [slot, slot+1]+[j for j in range(width) if j not in (slot, slot+1)]
    moved = np.transpose(v.reshape(shape), order)
    moved = (A@moved.reshape(N*N, -1)).reshape(shape)
    return np.transpose(moved, np.argsort(order)).reshape(-1)


def source_case(N, pairs, C):
    width, d = 2*pairs, N-1
    q = np.exp(1j*np.pi/N); x = q**d
    P = np.zeros((N*N, N*N), complex)
    cup = np.zeros(N*N, complex); ell = np.zeros(N*N, complex)
    marked = np.zeros(N*N, complex); unrestricted = np.zeros(N*N, complex)
    for a in range(N):
        for b in range(N):
            P[a*N+b, b*N+a] = 1
            unrestricted[a*N+b] = x**b/N**2
        cup[a*N+d-a] = N*x**(a-d)
        ell[a*N+d-a] = x**a/N
        marked[a*N+d-a] = x**(d-a)/N**2
    H = P@C@P
    state = cup.copy(); row = marked.copy(); rawrow = unrestricted.copy()
    for _ in range(pairs-1):
        state = np.kron(cup, state)
        row = np.kron(ell, row); rawrow = np.kron(ell, rawrow)
    R = original_factorial_R(N); Rm = np.linalg.inv(R)
    word = ([1] if pairs==1 else [2*j for j in range(1, pairs)])
    word += [-1, 1]  # literal inverse normalization retained before comparison
    for letter in word:
        state = apply_pair(state, R if letter>0 else Rm, abs(letter)-1, N, width)
    scalar = row@state
    assert abs(scalar-rawrow@state)<1e-7*max(1,abs(scalar))
    output = state.copy()
    for j in range(pairs):
        output = apply_pair(output, H if j==pairs-1 else C, 2*j, N, width)
    energy = float(np.real(np.vdot(state, output)))
    cost = 2.**(-pairs)*N**(-(3*pairs+2))
    assert abs(scalar)**2<=cost*energy+1e-6*max(1,abs(scalar)**2,abs(cost*energy))
    return {'N': N, 'pairs': pairs, 'actual_signed_word': word,
            'whole_marked_degree_restriction': True,
            'positive_C_H_source_budget': cost}


if __name__ == '__main__':
    field = [field_case(N) for N in range(2, 9)]
    positive, matrices = [], {}
    for N in range(2, 9):
        result, data = complex_case(N); positive.append(result); matrices[N] = data
    mixed = [mixed_block_case(N, matrices[N])for N in range(2,7)]
    sources = [source_case(N, pairs, matrices[N]['C']) for N in (2, 3, 4) for pairs in (1, 2, 3)]
    result = {'status': 'PASS', 'exact_original_Hopf_quotients': field,
              'positive_angle_channel_and_sewing_checks': positive,
              'actual_whole_block_mixed_braiding_and_both_norm_bounds':mixed,
              'whole_original_source_inequalities': sources,
              'scope': 'Exact positive circle channel/source theorem; no unrestricted split-pair or sharp geometric-energy claim.'}
    Path(__file__).with_name('actual_complete_circle_positive_quotient_results.json').write_text(
        json.dumps(result, indent=2)+'\n')
    print('PASS 7 Hopf quotient/source spaces; 7 angle-metric/sewing levels; 5 actual mixed-block braidings; 9 original source bounds')
