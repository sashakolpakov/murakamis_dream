#!/usr/bin/env python3
"""Literal full-degree trivalent CD vertices and typed graph contractions.

The primary comparisons are exact in cyclotomic-root finite fields. They
compare full original pair boxes/turns with the explicit one-color kernels,
not an inferred volume or a dephased normal replacement.
"""
import itertools
import json
import math
from pathlib import Path

import numpy as np

from audit_actual_two_cut_ports import balanced_data, coproduct


def axis_apply(A, v, axis, p):
    moved = np.moveaxis(v, axis, 0)
    out = np.tensordot(A, moved, axes=(1, 0)) % p
    return np.moveaxis(out, 0, axis)


def matrix_power(A, n, inverse, p):
    B = A if n >= 0 else inverse
    out = np.eye(len(A), dtype=np.int64)
    for _ in range(abs(n)):
        out = out @ B % p
    return out


def contract(tensors, p):
    """Pairwise exact graph contraction, reducing mod p after each dot."""
    tensors = [(A.copy(), tuple(labels)) for A, labels in tensors]
    while len(tensors) > 1:
        choices = []
        for i, (A, left) in enumerate(tensors):
            for j in range(i+1, len(tensors)):
                B, right = tensors[j]
                common = set(left) & set(right)
                if not common:
                    continue
                size = math.prod(A.shape[a] for a, x in enumerate(left) if x not in common)
                size *= math.prod(B.shape[a] for a, x in enumerate(right) if x not in common)
                choices.append((size, -len(common), i, j, common))
        assert choices, 'The audited graph is connected'
        _, _, i, j, common = min(choices, key=lambda x: x[:4])
        A, left = tensors[i]
        B, right = tensors[j]
        shared = sorted(common)
        axes = ([left.index(x) for x in shared], [right.index(x) for x in shared])
        out = np.tensordot(A, B, axes=axes) % p
        labels = tuple(x for x in left if x not in common) + tuple(x for x in right if x not in common)
        tensors = [z for k, z in enumerate(tensors) if k not in (i, j)] + [(out, labels)]
    A, labels = tensors[0]
    assert not labels
    return int(A) % p


def data(N):
    p, eta, q, E, F, K, pivot, R, Ri = balanced_data(N)
    d, Q, x = N-1, q*q % p, pow(q, N-1, p)
    rho = (q-pow(q, -1, p)) % p
    Et, Ft, Kt = coproduct(rho*rho*E % p, F, K, 2, N, p)
    Ki = np.diag([pow(int(z), -1, p) for z in np.diag(Kt)])
    O = (Ft@Et+q*Kt+pow(q, -1, p)*Ki) % p
    # A separately reconstructed conjugate physical Casimir.
    qb, Qb, xb = pow(q, -1, p), pow(Q, -1, p), pow(x, -1, p)
    Eb = np.diag([(pow(Qb, -a, p)-1) % p for a in range(1, N)], 1)
    Fb = np.diag([(1-pow(Qb, a, p)) % p for a in range(1, N)], -1)
    Kb = np.diag([xb*pow(Qb, -a, p) % p for a in range(N)])
    Ebt, Fbt, Kbt = coproduct(Eb, Fb, Kb, 2, N, p)
    Kbi = np.diag([pow(int(z), -1, p) for z in np.diag(Kbt)])
    Ob = (Fbt@Ebt+qb*Kbt+q*Kbi) % p
    I = np.eye(N*N, dtype=np.int64)
    u, L = I, O.copy()
    for _ in range(2, N):
        u, L = L, (O@L-u) % p
    L = (-1)**d*L % p
    P = np.zeros_like(L)
    for a, b in itertools.product(range(N), repeat=2):
        P[b*N+a, a*N+b] = 1
    factorial, s = [1], [1]
    imag = pow(eta, N, p)
    for r in range(1, N):
        factorial.append(factorial[-1]*(1-pow(Q, r, p)) % p)
        s.append(pow(imag, r, p)*pow(q, -r*(r+1)//2, p)*factorial[-1] % p)
    labels, cols, bars, weights, phase = [], [], [], [], []
    for T in range(2*d+1):
        low, offset = min(T, 2*d-T), max(0, T-d)
        ids = [(offset+a)*N+T-offset-a for a in range(low+1)]
        for j in range(low+1):
            if not j <= d-j <= low:
                continue
            node = (pow(q, 2*j+1, p)+pow(q, -2*j-1, p)) % p
            pair = []
            for A in (O, Ob):
                v = np.zeros(N*N, dtype=np.int64)
                v[ids[0]] = 1
                prev, current = 0, 1
                for a in range(low):
                    backward = int(A[ids[a], ids[a-1]]) if a else 0
                    forward = int(A[ids[a], ids[a+1]])
                    nxt = ((node-int(A[ids[a], ids[a]]))*current-backward*prev)*pow(forward, -1, p) % p
                    v[ids[a+1]] = nxt
                    prev, current = current, nxt
                assert np.array_equal(A@v % p, node*v % p)
                pair.append(v)
            h = s[low]**2*pow(s[low-j]**2, -1, p) % p if j == d-j else 2*s[low]**2*pow(s[low-j]*s[low+j-d], -1, p) % p
            a, b, c = low-j, low+j-d, d-low
            assert a+b+2*c == d
            angle = (N*N*(1 if j == d-j else 2)*pow(s[a]*s[b]*s[c]**2, -1, p)) % p
            assert h == angle
            omega = pow(eta, d*d, p)*(-1)**j*pow(q, j*(j+1), p) % p
            assert np.array_equal(R@pair[0] % p, omega*pair[0] % p)
            labels.append((T, j))
            cols.append(pair[0]); bars.append(pair[1]); weights.append(h); phase.append(omega)
    V, Vb = np.array(cols).T, np.array(bars).T
    h, phase = np.array(weights, dtype=np.int64), np.array(phase, dtype=np.int64)
    assert np.array_equal((V*h)@Vb.T % p, L@P % p)
    for e in (-3, -1, 0, 1, 2):
        actual = matrix_power(R, e, Ri, p) @ L % p
        target = (V*(h*np.array([pow(int(z), e, p) for z in phase]) % p))@Vb.T % p@P % p
        assert np.array_equal(actual, target)
    return p, q, x, R, Ri, L, P, labels, V, Vb, h, phase


def sources(N, x, p):
    d, D = N-1, N*N
    J = np.zeros((D,)*3, dtype=np.int64)
    ell = np.zeros_like(J)
    marker = np.zeros_like(J)
    for a, b, c in itertools.product(range(N), repeat=3):
        physical = (a, b, d-b, c, d-c, d-a)
        indices = tuple(physical[2*k]*N+physical[2*k+1] for k in range(3))
        J[indices] = N**3*pow(x, a+b+c-3*d, p) % p
        ell[indices] = pow(N, -3, p)*pow(x, a+b+c, p) % p
    for physical in itertools.product(range(N), repeat=6):
        if physical[1]+physical[2] == d and physical[3]+physical[4] == d:
            indices = tuple(physical[2*k]*N+physical[2*k+1] for k in range(3))
            marker[indices] = pow(N, -4, p)*pow(x, physical[5]+physical[1]+physical[3], p) % p
    return J, ell, marker


def vertex_formula(N, x, p, labels, Vb):
    d, r = N-1, len(labels)
    result = [np.zeros((r,)*3, dtype=np.int64) for _ in range(3)]
    for i, j, k in itertools.product(range(r), repeat=3):
        T, S, U = labels[i][0], labels[j][0], labels[k][0]
        if T+S+U != 3*d:
            continue
        lo, hi = max(0, T-d, T+S-2*d), min(d, T, T+S-d)
        values = [0, 0, 0]
        for a in range(lo, hi+1):
            b, c = T-a, T+S-d-a
            black = int(Vb[b*N+a, i])*int(Vb[c*N+d-b, j])*int(Vb[(d-a)*N+d-c, k])
            white = int(Vb[a*N+b, i])*int(Vb[(d-b)*N+c, j])*int(Vb[(d-c)*N+d-a, k])
            values[0] += pow(x, a+b+c-3*d, p)*black
            values[1] += pow(x, -a-b-c, p)*white
            values[2] += pow(x, -d+a-b-c, p)*white
        for A, v in zip(result, values):
            A[i, j, k] = N**3*v % p
    return result


def vertex_case(N):
    values = data(N)
    p, q, x, R, Ri, L, P, labels, V, Vb, h, phase = values
    J, ell, marker = sources(N, x, p)
    shape = (N,)*6
    permutations = [(1,0,3,2,5,4), (5,2,1,4,3,0), (0,2,1,4,3,5)]
    direct = []
    for perm in permutations:
        A = J.reshape(shape).transpose(perm).reshape((N*N,)*3)
        for axis in range(3):
            A = axis_apply(Vb.T, A, axis, p)
        direct.append(A)
    formula = vertex_formula(N, x, p, labels, Vb)
    for A, B in zip(direct, formula):
        assert np.array_equal(A, B)
    # Check unrestricted marker restriction only in total degree 3d.
    Jbar, _, _ = sources(N, pow(x, -1, p), p)
    target_ell = pow(N, -6, p)*Jbar.reshape(shape).transpose(permutations[1]).reshape(J.shape) % p
    target_marker = pow(N, -7, p)*Jbar.reshape(shape).transpose(permutations[2]).reshape(J.shape) % p
    assert np.array_equal(target_ell, ell)
    for physical in itertools.product(range(N), repeat=6):
        if sum(physical) == 3*(N-1):
            indices = tuple(physical[2*k]*N+physical[2*k+1] for k in range(3))
            assert marker[indices] == target_marker[indices]
    # The exact middle-degree nested source polynomial has marked corner one.
    middle = [a*N+N-1-a for a in range(N)]
    c0 = 0
    for a in range(N):
        c0 += N**3*pow(x, -(N-1)-a, p)*pow(x, a, p)**2*pow(x, -a, p)
    assert pow(x, N-1, p)*pow(N, -4, p)*c0 % p == 1
    return {'N':N, 'CD_channels':len(labels), 'all_full_degree_one_color_vertices':True,
            'exact_affine_CD_angle_weights':True, 'unrestricted_marked_degree_scope':True}, values, formula


def theta_graph():
    return {0:(0,1,2), 1:(0,1,2)}, {0}, 1


def cube_graph():
    xy = {0:(-2,-2),1:(2,-2),2:(2,2),3:(-2,2),
          4:(-1,-1),5:(1,-1),6:(1,1),7:(-1,1)}
    edges = [(0,1),(1,2),(2,3),(3,0),(4,5),(5,6),(6,7),(7,4),
             (0,4),(1,5),(2,6),(3,7)]
    ports = {}
    for v in xy:
        adjacent = [e for e, ab in enumerate(edges) if v in ab]
        def angle(e):
            a,b = edges[e]; w = b if a == v else a
            return math.atan2(xy[w][1]-xy[v][1], xy[w][0]-xy[v][0])
        ports[v] = tuple(sorted(adjacent, key=angle))
    return ports, {0,2,5,7}, 1


def progressive_graph():
    return {0:(0,1,2), 1:(3,4,5), 2:(0,1,3), 3:(4,5,2)}, {0,1}, 2


def ordered_cube_graph():
    return {0:(0,1,2),1:(3,4,11),2:(5,9,10),3:(6,7,8),
            4:(0,10,11),5:(1,8,9),6:(2,3,7),7:(4,5,6)}, {0,1,2,3}, 4


def noncrossing(partition):
    for i, A in enumerate(partition):
        for B in partition[i+1:]:
            for a, c in itertools.combinations(A, 2):
                for b, d in itertools.combinations(B, 2):
                    if a < b < c < d or b < a < d < c:
                        return False
    return True


def matching(partition):
    out = []
    for a,b,c in partition:
        out.extend([(2*a,2*c+1), (2*a+1,2*b), (2*b+1,2*c)])
    assert noncrossing(out)
    return out


def primitive_morse_case(N, graph, powers, values, tensor_scalar):
    """Ungrouped original p/ell/m and four-index boxes on the full Morse cut."""
    p, q, x, R, Ri, L, P, labels, V, Vb, h, phase = values
    ports, black, marked = graph
    B = [ports[v] for v in ports if v in black]
    W = [ports[v] for v in ports if v not in black]
    assert noncrossing(B) and noncrossing(W)
    bottom, top = matching(B), matching(W)
    E = len(powers)
    assert sorted(sum((list(z) for z in B),[])) == list(range(E))
    assert sorted(sum((list(z) for z in W),[])) == list(range(E))
    cup = np.zeros((N,N),dtype=np.int64)
    cap = cup.copy();mark = cup.copy()
    for a,b in itertools.product(range(N),repeat=2):
        mark[a,b] = pow(N,-2,p)*pow(x,b,p) % p
        if a+b == N-1:
            cup[a,b] = N*pow(x,-b,p) % p
            cap[a,b] = pow(N,-1,p)*pow(x,a,p) % p
    tensors = []
    for e in range(E):
        box = matrix_power(R,powers[e],Ri,p)@L % p
        tensors.append((box.reshape((N,)*4),(2*e,2*e+1,2*E+2*e,2*E+2*e+1)))
    tensors.extend((cup,(2*E+a,2*E+b)) for a,b in bottom)
    am,bm,cm = ports[marked]
    marked_arc = (2*am,2*cm+1)
    marked_tensors = tensors + [(mark if (a,b)==marked_arc else cap,(a,b)) for a,b in top]
    ordinary_tensors = tensors + [(cap,(a,b)) for a,b in top]
    actual = contract(marked_tensors,p)
    ordinary = contract(ordinary_tensors,p)
    assert actual == tensor_scalar
    assert ordinary == 0
    return {'N':N,'physical_heads':2*E,'prime':p,
            'bottom_original_cup_matching_1based':[[a+1,b+1] for a,b in bottom],
            'top_original_cap_matching_1based':[[a+1,b+1] for a,b in top],
            'unrestricted_marker_1based':[marked_arc[0]+1,marked_arc[1]+1],
            'marked_original_scalar':actual,'all_ordinary_scalar':ordinary,
            'independent_ungrouped_original_Morse_contraction':True}


def graph_case(N, graph, powers, values, formula):
    p, q, x, R, Ri, L, P, labels, V, Vb, h, phase = values
    ports, black, marked = graph
    J, ell, marker = sources(N, x, p)
    U, white, mark = formula
    _, whitebar, markbar = vertex_formula(N, pow(x,-1,p), p, labels, V)
    direct, coherent = [], []
    for v, edges in ports.items():
        if v in black:
            A, B = J.copy(), U.copy()
            for axis, e in enumerate(edges):
                actual = matrix_power(R, powers[e], Ri, p)@L % p
                A = axis_apply(actual, A, axis, p)
                w = h*np.array([pow(int(z), powers[e], p) for z in phase]) % p
                shape = [1,1,1];shape[axis] = len(labels)
                B = B*w.reshape(shape) % p
        else:
            A = marker if v == marked else ell
            B = markbar if v == marked else whitebar
        direct.append((A, edges)); coherent.append((B, edges))
    a = contract(direct, p)
    b = pow(N, -6*len(black)-1, p)*contract(coherent, p) % p
    assert a == b, (N, powers, a, b)
    return {'N':N, 'vertices':len(ports), 'edges':len(powers), 'signed_powers':powers,
            'exact_fixed_tensor_unrestricted_marker_vs_channel_partition':True,
            'raw_cyclotomic_image':a, 'prime':p}


def ordinary_contraction(N, graph, values):
    p, q, x, R, Ri, L, P, labels, V, Vb, h, phase = values
    ports, black, marked = graph
    J, ell, marker = sources(N, x, p)
    tensors = []
    for v, edges in ports.items():
        A = J.copy() if v in black else ell
        if v in black:
            for axis in range(3):
                A = axis_apply(L, A, axis, p)
        tensors.append((A, edges))
    return contract(tensors, p)


def direct_morse_case(N, powers, values, tensor_scalar):
    """Independent ORIGINAL twelve-head nested-cup, full-marker evaluation."""
    p, q, x, R, Ri, L, P, labels, V, Vb, h, phase = values
    matching = [(0,11),(1,2),(3,10),(4,9),(5,6),(7,8)]
    v = np.zeros((N,)*12, dtype=np.int64)
    for colors in itertools.product(range(N), repeat=6):
        physical = [0]*12
        for a, (left, right) in zip(colors, matching):
            physical[left], physical[right] = a, N-1-a
        v[tuple(physical)] = N**6*pow(x, -sum(physical[right] for _, right in matching), p) % p
    v = v.reshape((N*N,)*6)
    top_order = [0,1,3,4,5,2]
    for axis, edge in enumerate(top_order):
        B = matrix_power(R, powers[edge], Ri, p)@L % p
        v = axis_apply(B, v, axis, p)
    _, ell, marker = sources(N, x, p)
    marked = int(np.sum(v*np.tensordot(marker, ell, axes=0)) % p)
    ordinary = int(np.sum(v*np.tensordot(ell, ell, axes=0)) % p)
    assert ordinary == 0
    assert marked == tensor_scalar
    return {'N':N, 'physical_heads':12, 'original_noncrossing_bottom_matching_1based':[[a+1,b+1] for a,b in matching],
            'signed_powers':powers, 'unrestricted_original_marked_scalar':marked,
            'ordinary_complete_source_scalar':ordinary, 'prime':p,
            'independent_physical_Morse_source_matches_partition':True}


def dipole_case(N, values, formula):
    p,q,x,R,Ri,L,P,labels,V,Vb,h,phase = values
    J,ell,marker = sources(N,x,p)
    U,white,marked = formula
    _,whitebar,_ = vertex_formula(N,pow(x,-1,p),p,labels,V)
    _,_,_,E,F,K,_,_,_ = balanced_data(N)
    rho = (q-pow(q,-1,p)) % p
    Et,Ft,Kt = coproduct(rho*rho*E % p,F,K,2,N,p)
    families = []
    for left,right in ((0,0),(-1,2),(3,-2)):
        A=axis_apply(matrix_power(R,left,Ri,p)@L%p,J,0,p)
        A=axis_apply(matrix_power(R,right,Ri,p)@L%p,A,1,p)
        transmission=np.tensordot(A,ell,axes=([0,1],[1,2]))%p
        for generator in (Et,Ft,Kt):
            assert not np.any((transmission@generator-generator@transmission)%p)
        channel=Vb.T@P%p@transmission%p@V%p
        weights=[h*np.array([pow(int(z),n,p) for z in phase])%p for n in (left,right)]
        explicit=U*weights[0][:,None,None]%p*weights[1][None,:,None]%p
        explicit=pow(N,-6,p)*np.tensordot(explicit,whitebar,axes=([0,1],[1,2]))%p
        assert np.array_equal(explicit,channel)
        neck=L@transmission%p@L%p
        if N%2 == 0:
            assert not np.any(neck)
        else:
            # The complete squared circle retains only the genuine Steinberg value.
            simple=np.array([int(j==(N-1)//2) for T,j in labels],dtype=np.int64)
            assert np.array_equal(channel,channel*simple[:,None]*simple[None,:]%p)
        families.append({'interior_signed_powers':[left,right],
                         'all_input_Hopf_transmission':True,
                         'full_coherent_CD_double_vertex_kernel':True,
                         'external_two_belt_neck_zero':bool(not np.any(neck))})
    return {'N':N,'families':families}


if __name__ == '__main__':
    levels, graphs, morse, cubes, qdim, primitive, dipoles = [], [], [], [], [], [], []
    for N in range(2,9):
        row, values, formula = vertex_case(N)
        levels.append(row)
        dipoles.append(dipole_case(N,values,formula))
        if N <= 5:
            for powers in ([0,0,0], [-1,-1,-1], [1,-2,3]):
                graphs.append(graph_case(N, theta_graph(), powers, values, formula))
            for powers in ([0]*6, [-1]*6, [1,-2,3,0,-1,2]):
                result = graph_case(N, progressive_graph(), powers, values, formula)
                graphs.append(result)
                if N <= 3:
                    morse.append(direct_morse_case(N, powers, values, result['raw_cyclotomic_image']))
            ordinary = ordinary_contraction(N, progressive_graph(), values)
            assert ordinary == 0
            qdim.append({'N':N, 'actual_progressive_ordinary_closure':ordinary})
        if N <= 4:
            for powers in ([0]*12, [-1]*12, [(-1)**k*(k%3) for k in range(12)]):
                actual_cube = graph_case(N, ordered_cube_graph(), powers, values, formula)
                graphs.append(actual_cube)
                primitive.append(primitive_morse_case(N,ordered_cube_graph(),powers,values,actual_cube['raw_cyclotomic_image']))
            actual_ordinary = ordinary_contraction(N,ordered_cube_graph(),values)
            assert actual_ordinary == 0
            for powers in ([0]*12, [-1]*12, [(-1)**k*(k%3) for k in range(12)]):
                cubes.append(graph_case(N, cube_graph(), powers, values, formula))
            rejected = ordinary_contraction(N, cube_graph(), values)
            cubes[-1]['naive_all_ordinary_cube_diagnostic'] = rejected
            if N == 3:
                assert rejected == 174
                assert next(z for z in graphs if z['N']==3 and z['vertices']==4 and z['signed_powers']==[0]*6)['raw_cyclotomic_image'] == 242
                assert next(z for z in graphs if z['N']==3 and z['vertices']==8 and z['signed_powers']==[0]*12)['raw_cyclotomic_image'] == 730
    out = {'status':'PASS', 'full_physical_vertex_levels':levels,
           'literal_typed_port_graph_sources':graphs,
           'independent_full_physical_Morse_sources':morse,
           'corrected_cube_ungrouped_twenty_four_head_Morse_sources':primitive,
           'all_input_two_belt_neck_and_full_normal_dipole_kernels':dipoles,
           'actual_ordinary_qdim_tests':qdim,
           'formal_cube_partitions_WITH_SOURCE_REJECTION':cubes,
           'scope':'Exact full-degree vertices; actual noncrossing ordered theta/progressive/cube sources; the naive cyclic cube is explicitly NOT an original ribbon source. The corrected cube has independent ungrouped 24-head Morse contractions. No geometric maximum or sharp asymptotic inferred.'}
    Path(__file__).with_name('actual_trivalent_complete_circle_vertex_kernel_results.json').write_text(json.dumps(out,indent=2)+'\n')
    print(f'PASS {len(levels)} all-degree vertices/normal angle weights; {len(graphs)} ordered marked sources; {len(morse)} twelve-head/{len(primitive)} twenty-four-head Morse words; {3*len(dipoles)} all-input dipoles; naive-cube rejection')
