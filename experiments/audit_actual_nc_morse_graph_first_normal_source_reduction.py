#!/usr/bin/env python3
"""Exact first jets of the original NC/Morse graph, including its marked normal.

Arithmetic is in cyclotomic-root finite fields with epsilon^2=0. No
finite-difference derivative, Hermitian white replacement, or reconstructed
unrestricted mark is used.
"""
import itertools
import json
import math
from pathlib import Path

import numpy as np

from audit_actual_two_cut_ports import balanced_data
from audit_actual_trivalent_complete_circle_vertex_kernel import (
    axis_apply, contract, sources, noncrossing, matching,
    theta_graph, ordered_cube_graph,
)


def mul(a, b, p):
    return a[0]*b[0] % p, (a[1]*b[0]+a[0]*b[1]) % p


def inv(a, p):
    z = pow(int(a[0]), -1, p)
    return z, -int(a[1])*z*z % p


def mm(a, b, p):
    return a[0]@b[0] % p, (a[1]@b[0]+a[0]@b[1]) % p


def kron(a, b, p):
    return (np.kron(a[0], b[0]) % p,
            (np.kron(a[1], b[0])+np.kron(a[0], b[1])) % p)


def add(a, b, p):
    return (a[0]+b[0]) % p, (a[1]+b[1]) % p


def const(a):
    return a, np.zeros_like(a)


def trans(a):
    return a[0].T, a[1].T


def ordered_dipole_graph():
    return {0:(0,1,2),1:(3,4,5),2:(0,1,5),3:(2,3,4)}, {0,1}, 2


def exposed_mark(graph):
    ports, black, marked = graph
    if marked in black or any(tuple(sorted(es)) != es for es in ports.values()):
        return False
    a, _, c = ports[marked]
    left, right = 2*a, 2*c+1
    top = matching([ports[v] for v in ports if v not in black])
    return not any(u < left < right < v for u, v in top)


def axis_jet(A, v, index, p):
    return (axis_apply(A[0], v[0], index, p),
            (axis_apply(A[1], v[0], index, p)
             + axis_apply(A[0], v[1], index, p)) % p)


def contract_jet(tensors, p):
    tensors = [((A[0].copy(), A[1].copy()), tuple(labels))
               for A, labels in tensors]
    while len(tensors) > 1:
        choices = []
        for i, (A, left) in enumerate(tensors):
            for j in range(i+1, len(tensors)):
                B, right = tensors[j]
                common = set(left) & set(right)
                if not common:
                    continue
                size = math.prod(A[0].shape[k] for k, x in enumerate(left) if x not in common)
                size *= math.prod(B[0].shape[k] for k, x in enumerate(right) if x not in common)
                choices.append((size, -len(common), i, j, common))
        assert choices
        _, _, i, j, common = min(choices, key=lambda z: z[:4])
        A, left = tensors[i]
        B, right = tensors[j]
        shared = sorted(common)
        axes = ([left.index(x) for x in shared], [right.index(x) for x in shared])
        out = (np.tensordot(A[0], B[0], axes=axes) % p,
               (np.tensordot(A[1], B[0], axes=axes)
                + np.tensordot(A[0], B[1], axes=axes)) % p)
        labels = tuple(x for x in left if x not in common)+tuple(x for x in right if x not in common)
        tensors = [z for k, z in enumerate(tensors) if k not in (i, j)]+[(out, labels)]
    A, labels = tensors[0]
    assert not labels
    return int(A[0]) % p, int(A[1]) % p


def module_jet(L, q, p):
    Q, n = q*q % p, L+1
    E = [np.zeros((n, n), dtype=np.int64) for _ in range(2)]
    F = [np.zeros((n, n), dtype=np.int64) for _ in range(2)]
    K = [np.zeros((n, n), dtype=np.int64) for _ in range(2)]
    for r in range(n):
        K[0][r, r] = pow(q, L-2*r, p)
        K[1][r, r] = (L-2*r)*int(K[0][r, r]) % p
    for r in range(1, n):
        E[0][r-1, r] = pow(q, -L-1, p)*(1-pow(Q, L+1-r, p)) % p
        E[1][r-1, r] = ((-L-1)*int(E[0][r-1, r])
            - 2*(L+1-r)*pow(q, -L-1, p)*pow(Q, L+1-r, p)) % p
        F[0][r, r-1] = (1-pow(Q, r, p)) % p
        F[1][r, r-1] = -2*r*pow(Q, r, p) % p
    return tuple(E), tuple(F), tuple(K)


class Local:
    def __init__(self, N):
        self.N, self.d = N, N-1
        self.p, self.eta, self.q, *_ = balanced_data(N)
        p, q, d = self.p, self.q, self.d
        self.Q, self.x = q*q % p, pow(q, d, p)
        Q = self.Q
        self.fac, self.logfac = [1], [0]
        for r in range(1, N):
            self.fac.append(self.fac[-1]*(1-pow(Q, r, p)) % p)
            self.logfac.append((self.logfac[-1]-2*r*pow(Q, r, p)
                                * pow(1-pow(Q, r, p), -1, p)) % p)
        self.cup, self.cap = self.cup_jet(d, N*pow(q, -d*d, p) % p, -d*d)
        self.P = const(np.eye(N*N, dtype=np.int64).reshape((N,)*4)
            .transpose(1, 0, 2, 3).reshape(N*N, N*N))
        E, F, K = module_jet(d, q, p)
        I = const(np.eye(N, dtype=np.int64))
        Ki0 = np.diag([pow(int(z), -1, p) for z in np.diag(K[0])])
        Ki = (Ki0, -Ki0@K[1]@Ki0 % p)
        self.Epair = add(kron(E, K, p), kron(I, E, p), p)
        self.Fpair = add(kron(F, I, p), kron(Ki, F, p), p)
        self.Kpair = kron(K, K, p)
        self.W, self.pi, self.ordinary, self.qcups = {}, {}, {}, {}
        self.h0, self.gamma, self.omega = {}, {}, {}
        imag = pow(self.eta, N, p)
        sine = [pow(imag, r, p)*pow(q, -r*(r+1)//2, p)*self.fac[r] % p
                for r in range(N)]
        for j in range(d//2+1):
            self.ordinary[j] = module_jet(2*j, q, p)
            self.qcups[j] = self.cup_jet(2*j)
            self.gamma[j] = pow(q, 2-j*j, p)*pow(N, -2, p) % p
            self.h0[j] = N if 2*j == d else 2*N*sine[2*j]*pow(sine[j]**2, -1, p) % p
            self.omega[j] = pow(self.eta, d*d, p)*(-1)**j*pow(q, j*(j+1), p) % p
            l, n = d-j, 2*j+1
            W = [np.zeros((N*N, n), dtype=np.int64) for _ in range(2)]
            for u in range(l+1):
                h = ((-1)**u*pow(q, -d*u, p)
                    * pow(Q, u*(l-1)-u*(u-1)//2, p)
                    * self.fac[j+u]*self.fac[d-u]
                    * pow(self.fac[j]*self.fac[d], -1, p)) % p
                logh = (u*(2*l-d-u-1)+self.logfac[j+u]-self.logfac[j]
                        + self.logfac[d-u]-self.logfac[d]) % p
                W[0][u*N+l-u, 0], W[1][u*N+l-u, 0] = h, h*logh % p
            for r in range(1, n):
                denom = ((1-pow(Q, r, p)) % p, -2*r*pow(Q, r, p) % p)
                v = mm(self.Fpair, (W[0][:, r-1], W[1][:, r-1]), p)
                di = inv(denom, p)
                W[0][:, r] = v[0]*di[0] % p
                W[1][:, r] = (v[1]*di[0]+v[0]*di[1]) % p
            self.W[j] = tuple(W)
            for physical, ordinary in zip((self.Epair, self.Fpair, self.Kpair), self.ordinary[j]):
                left, right = mm(physical, self.W[j], p), mm(self.W[j], ordinary, p)
                assert all(np.array_equal(a, b) for a, b in zip(left, right))
            DW = mm(mm(mm(trans(self.qcups[j][0]), trans(self.W[j]), p),
                          kron(trans(self.cap), trans(self.cap), p), p), self.P, p)
            self.pi[j] = tuple(a*pow(self.gamma[j], -1, p) % p for a in DW)
        D = N*N
        self.J = tuple(np.zeros((D,)*3, dtype=np.int64) for _ in range(2))
        self.ellS = tuple(np.zeros((D,)*3, dtype=np.int64) for _ in range(2))
        for a, b, c in itertools.product(range(N), repeat=3):
            ids = (a*N+b, (d-b)*N+c, (d-c)*N+d-a)
            for source, dualmap in ((self.J, self.cup), (self.ellS, self.cap)):
                value = (1, 0)
                for u in (a, b, c):
                    value = mul(value, (int(dualmap[0][u, d-u]), int(dualmap[1][u, d-u])), p)
                source[0][ids], source[1][ids] = value
        _, rootell, self.marker = sources(N, self.x, p)
        assert np.array_equal(rootell, self.ellS[0])
        D0 = mm(self.cap, trans(self.cup), p)
        self.nu = 2*N*(-1)**N*pow(q-pow(q, -1, p), -1, p) % p
        assert int(np.trace(D0[0]) % p) == 0
        assert int(np.trace(D0[1]) % p) == self.nu
        self.cache = {}

    def cup_jet(self, L, scale=1, scale_log=0):
        p, q = self.p, self.q
        out = [np.zeros((L+1, L+1), dtype=np.int64) for _ in range(2)]
        for u in range(L+1):
            value = (scale*(-1)**u*pow(q, u*(L-u-1), p)
                * self.fac[u]*self.fac[L-u]*pow(self.fac[L], -1, p)) % p
            log = (scale_log+u*(L-u-1)+self.logfac[u]
                   + self.logfac[L-u]-self.logfac[L]) % p
            out[0][u, L-u], out[1][u, L-u] = value, value*log % p
        cap0 = np.zeros_like(out[0])
        for u in range(L+1):
            cap0[L-u, u] = pow(int(out[0][u, L-u]), -1, p)
        cap1 = -cap0@out[1]@cap0 % p
        return tuple(out), (cap0, cap1)

    def theta(self, js):
        a, b, c = js
        J, r, r1 = sum(js), b+c-a, a+b-c
        if min(r, r1, a+c-b) < 0:
            return None
        p, q = self.p, self.q
        out = [np.zeros(tuple(2*j+1 for j in js), dtype=np.int64) for _ in range(2)]
        for k in range(r1+1):
            value = ((-1)**k*pow(q, k*(2*a+1-k), p)
                * self.fac[r+k]*self.fac[2*a-k]
                * pow(self.fac[r]*self.fac[2*a], -1, p)) % p
            log = (k*(2*a+1-k)+self.logfac[r+k]+self.logfac[2*a-k]
                   - self.logfac[r]-self.logfac[2*a]) % p
            out[0][2*a-k, r+k, 0], out[1][2*a-k, r+k, 0] = value, value*log % p
        E1, _, K1 = self.ordinary[a]
        E2, _, K2 = self.ordinary[b]
        E3, _, K3 = self.ordinary[c]
        E12 = add(kron(E1, K2, p), kron(const(np.eye(2*a+1, dtype=np.int64)), E2, p), p)
        for u in range(1, 2*c+1):
            coefficient = mul((-int(K3[0][u-1, u-1]) % p, -int(K3[1][u-1, u-1]) % p),
                              inv((int(E3[0][u-1, u]), int(E3[1][u-1, u])), p), p)
            v = mm(E12, (out[0][:, :, u-1].reshape(-1), out[1][:, :, u-1].reshape(-1)), p)
            out[0][:, :, u] = (coefficient[0]*v[0] % p).reshape(2*a+1, 2*b+1)
            out[1][:, :, u] = ((coefficient[1]*v[0]+coefficient[0]*v[1]) % p).reshape(2*a+1, 2*b+1)
        return tuple(out)

    def dual(self, value, js):
        p = self.p
        for axis, j in enumerate(js):
            value = axis_jet(self.qcups[j][1], value, axis, p)
        return tuple(v.transpose(2, 1, 0) for v in value)

    def vertex(self, js):
        js = tuple(js)
        if js in self.cache:
            return self.cache[js]
        p = self.p
        U, ordinary = self.J, self.ellS
        marked = self.marker
        for axis, j in enumerate(js):
            U = axis_jet(self.pi[j], U, axis, p)
            ordinary = axis_jet(trans(self.W[j]), ordinary, axis, p)
            marked = axis_apply(self.W[j][0].T, marked, axis, p)
        theta = self.theta(js)
        if theta is None:
            assert not any(np.any(v) for v in U)
            scalar = (0, 0)
        else:
            corner = (2*js[0], js[1]+js[2]-js[0], 0)
            scalar = int(U[0][corner]), int(U[1][corner])
            assert np.array_equal(U[0], scalar[0]*theta[0] % p)
            assert np.array_equal(U[1], (scalar[1]*theta[0]+scalar[0]*theta[1]) % p)
        self.cache[js] = {'U': U, 'ordinary': ordinary, 'marked': marked,
                          's': scalar, 'theta': theta}
        return self.cache[js]


def graph_case(local, name, graph, labels, powers):
    p, N = local.p, local.N
    ports, black, marked_vertex = graph
    assert exposed_mark(graph), 'A bare marked row requires an exposed cap; nested cuts need pivotal transport'
    assert noncrossing([ports[v] for v in ports if v in black])
    assert noncrossing([ports[v] for v in ports if v not in black])
    matching([ports[v] for v in ports if v in black])
    matching([ports[v] for v in ports if v not in black])
    actual_tensors, ordinary_jets, spin_jets = [], [], []
    Cedges, Cgamma, S = 1, 1, (1, 0)
    nontriangle, zeros, source_jets = [], [], {}
    for e, j in enumerate(labels):
        Cedges = Cedges*local.h0[j]*pow(local.omega[j], powers[e], p) % p
        Cgamma = Cgamma*local.gamma[j] % p
    for v, edges in ports.items():
        js = tuple(labels[e] for e in edges)
        vertex = local.vertex(js)
        ordinary_jets.append((vertex['U'] if v in black else vertex['ordinary'], edges))
        actual_tensors.append((vertex['U'][0] if v in black else
                               vertex['marked'] if v == marked_vertex else vertex['ordinary'][0], edges))
        ordered = js if v in black else tuple(reversed(js))
        source = local.vertex(ordered)
        source_jets[v] = list(source['s'])
        if source['theta'] is None:
            nontriangle.append(v)
            continue
        if source['s'][0] == 0:
            zeros.append(v)
        S = mul(S, source['s'], p)
        tensor = source['theta'] if v in black else local.dual(source['theta'], ordered)
        spin_jets.append((tensor, edges))
        if v not in black:
            reverse_U = local.dual(source['U'], ordered)
            gammas = math.prod(local.gamma[j] for j in js) % p
            for actual, target in zip(vertex['ordinary'], reverse_U):
                assert np.array_equal(actual, gammas*target % p)
    actual = Cedges*contract(actual_tensors, p) % p
    Fphysical = contract_jet(ordinary_jets, p)
    assert Fphysical[0] == 0
    assert actual == Cedges*Fphysical[1]*pow(local.nu, -1, p) % p
    Xi = None
    if nontriangle:
        assert actual == 0
    else:
        Xi = contract_jet(spin_jets, p)
        factor = Cgamma*mul(S, Xi, p)[1] % p
        assert Fphysical[1] == factor
        expected = Cedges*factor*pow(local.nu, -1, p) % p
        assert actual == expected
        if not zeros:
            assert Xi[0] == 0
            assert actual == Cedges*Cgamma*S[0]*Xi[1]*pow(local.nu, -1, p) % p
        elif len(zeros) >= 2:
            assert actual == 0
        elif zeros == [marked_vertex]:
            assert actual == Cedges*Cgamma*S[1]*Xi[0]*pow(local.nu, -1, p) % p
        else:
            assert actual == 0 and S[1]*Xi[0] % p == 0
    return {'N': N, 'prime': p, 'graph': name, 'edges': len(labels),
            'labels': list(labels), 'signed_powers': list(powers),
            'nontriangle_vertices': nontriangle, 'zero_source_vertices': zeros,
            'marked_vertex': marked_vertex, 'original_marked_scalar': actual,
            'ordered_local_source_first_jets': source_jets,
            'ordinary_spin_root_and_first_normal': list(Xi) if Xi else None,
            'original_physical_mark_vs_exact_first_normal': True}


def nested_mark_rejection():
    local = Local(3)
    graph = ordered_cube_graph()
    ports, black, _ = graph
    p = local.p
    actual = []
    for marked in (4,5):
        tensors = []
        for v, es in ports.items():
            vertex = local.vertex((1,1,1))
            value = vertex['U'][0] if v in black else vertex['marked'] if v==marked else vertex['ordinary'][0]
            tensors.append((value,es))
        actual.append(pow(local.h0[1],12,p)*contract(tensors,p)%p)
    assert local.q==375 and p==1009
    assert actual==[155,620]
    assert exposed_mark((ports,black,4))
    assert not exposed_mark((ports,black,5))
    return {'N':3,'prime':p,'q_image':local.q,
            'exposed_white_ports':[0,10,11],'nested_white_ports':[1,8,9],
            'bare_mark_scalar_images':actual,
            'same_ordinary_first_normal_cannot_equal_both':True,
            'nested_bare_mark_is_not_a_pivotal_cut_without_transport':True}


if __name__ == '__main__':
    locals = {N: Local(N) for N in range(2, 7)}
    local_rows = []
    for N, local in locals.items():
        count = 0
        for js in itertools.product(range((N-1)//2+1), repeat=3):
            v = local.vertex(js)
            if v['theta'] is not None:
                count += 1
        local_rows.append({'N': N, 'all_triangle_source_and_canonical_first_jets': count,
                           'first_jet_E_F_K_covariance_and_trace_clock': True})
    rows = []
    for N in range(2, 7):
        M = (N-1)//2
        rows.append(graph_case(locals[N], 'theta', theta_graph(), (M,)*3, (1,-2,3)))
    for N in (3,4,5):
        M = (N-1)//2
        rows.append(graph_case(locals[N], 'genuine_ordered_dipole', ordered_dipole_graph(),
                               (M,)*6, (0,1,-1,2,0,-2)))
        rows.append(graph_case(locals[N], 'genuine_ordered_cube', ordered_cube_graph(),
                               (M,)*12, tuple((e % 5)-2 for e in range(12))))
    cube = ordered_cube_graph()
    configurations = {}
    configurations['sole_marked_white_unsaturated'] = [2]*12
    for e in cube[0][cube[2]]:
        configurations['sole_marked_white_unsaturated'][e] = 1
    configurations['sole_black_unsaturated'] = [2]*12
    for e in cube[0][0]:
        configurations['sole_black_unsaturated'][e] = 1
    configurations['sole_ordinary_white_unsaturated'] = [2]*12
    for e in cube[0][5]:
        configurations['sole_ordinary_white_unsaturated'][e] = 1
    configurations['two_white_zeros'] = configurations['sole_marked_white_unsaturated'].copy()
    for e in cube[0][5]:
        configurations['two_white_zeros'][e] = 1
    configurations['marked_nontriangle'] = [2]*12
    for e, j in zip(cube[0][cube[2]], (0,1,2)):
        configurations['marked_nontriangle'][e] = j
    for name, labels in configurations.items():
        rows.append(graph_case(locals[5], name, cube, labels, (0,)*12))
    result = {'status': 'PASS', 'exact_local_first_jets': local_rows,
              'literal_NC_graph_source_normal_cases': rows,
              'negative_nested_mark_test':nested_mark_rejection(),
              'scope': 'Exact original NC/Morse graph source reduction with an exposed bare mark and retained marked-white boundary normal. A nested bare mark is explicitly rejected. No norm, noncancellation, geometric-volume, or arbitrary untyped planar-graph assertion.'}
    Path(__file__).with_name('actual_nc_morse_graph_first_normal_source_reduction_results.json').write_text(json.dumps(result, indent=2)+'\n')
    print(f'PASS {len(local_rows)} exact local first-jet families; {len(rows)} exposed theta/dipole/cube sources; negative nested-mark rejection')
