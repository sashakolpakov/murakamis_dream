#!/usr/bin/env python3
"""Generic all-channel factorial source versus literal physical matrices.

Includes both members j,d-j before root specialization. No conjugate or
root factorial reflection is used in these generic source comparisons.
"""
import itertools
import json
from pathlib import Path

import numpy as np

from audit_actual_two_cut_ports import coproduct
from audit_actual_two_cut_ports import balanced_data
from audit_actual_trivalent_complete_circle_vertex_kernel import axis_apply, sources


class Generic:
    def __init__(self, N, q=2, p=1000003):
        self.N, self.d, self.q, self.p = N, N-1, q, p
        self.Q = q*q % p
        d, Q = self.d, self.Q
        self.fac = [1]
        for k in range(1, 3*N+2):
            self.fac.append(self.fac[-1]*(1-pow(Q, k, p)) % p)
        assert all(self.fac)
        self.scale = N*pow(q, -d*d, p) % p
        self.pv = [self.cup(d, u, self.scale) for u in range(N)]
        self.PV = np.fliplr(np.diag(self.pv)).copy()
        self.E = np.diag([pow(q, -d-1, p)*(1-pow(Q, d+1-u, p)) % p
                          for u in range(1, N)], 1)
        self.F = np.diag([(1-pow(Q, u, p)) % p for u in range(1, N)], -1)
        self.K = np.diag([pow(q, d-2*u, p) for u in range(N)])
        self.Epair, self.Fpair, self.Kpair = coproduct(self.E, self.F, self.K, 2, N, p)
        self.W, self.DW, self.norm, self.projector = {}, {}, {}, {}
        for j in range(N):
            l = d-j
            W = np.zeros((N*N, 2*j+1), dtype=np.int64)
            for u in range(l+1): W[u*N+l-u, 0] = self.high(j, u)
            for r in range(1, 2*j+1):
                W[:, r] = self.Fpair@W[:, r-1] % p * pow(1-pow(Q, r, p), -1, p) % p
            self.W[j] = W
            DW = np.zeros((2*j+1, N*N), dtype=np.int64)
            for r, u, v in itertools.product(range(2*j+1), range(N), range(N)):
                DW[r, u*N+v] = (self.cup(2*j, 2*j-r)
                    * int(W[(d-v)*N+d-u, 2*j-r])
                    * pow(self.pv[d-v]*self.pv[d-u], -1, p)) % p
            self.DW[j] = DW
            value = int((DW@W % p)[0, 0])
            self.norm[j] = value
            self.projector[j] = W@DW % p * pow(value, -1, p) % p

    def cup(self, L, u, scale=1):
        q, p, f = self.q, self.p, self.fac
        return (scale*(-1)**u*pow(q, u*(L-u-1), p)
                * f[u]*f[L-u]*pow(f[L], -1, p)) % p

    def high(self, j, u):
        if not 0 <= u <= self.d-j: return 0
        d, q, Q, p, f = self.d, self.q, self.Q, self.p, self.fac
        return ((-1)**u*pow(q, -d*u, p)
                * pow(Q, u*(d-j-1)-u*(u-1)//2, p)
                * f[j+u]*f[d-u]*pow(f[j]*f[d], -1, p)) % p

    def w_factorial(self, j, r, A, B):
        d, q, Q, p, f = self.d, self.q, self.Q, self.p, self.fac
        l = d-j
        if not (0 <= A <= d and 0 <= B <= d and 0 <= r <= 2*j
                and A+B == l+r): return 0
        value = 0
        for u in range(max(0, l-B), min(l, A)+1):
            t = B-l+u
            if not 0 <= t <= r: continue
            value += (self.high(j, u)*pow(q, -d*t, p)*pow(Q, u*t, p)
                      * pow(f[u]*f[l-u]*f[t]*f[r-t], -1, p))
        return f[A]*f[B]*value % p

    def norm_factorial(self, j):
        d, q, p, f = self.d, self.q, self.p, self.fac
        return ((-1)**(d+j)*pow(self.scale, -2, p)
                * pow(q, j*(j+1)-d*(2*j+1), p)
                * f[d+j+1]*pow(f[d-j]*f[2*j+1], -1, p)) % p

    def source_corner_direct(self, js):
        a, b, c = js
        r = b+c-a
        if min(r, a+b-c, a+c-b) < 0: return 0
        N, d, p = self.N, self.d, self.p
        value = 0
        for u, v, w in itertools.product(range(N), repeat=3):
            value += (self.pv[u]*self.pv[v]*self.pv[w]
                      * int(self.DW[a][2*a, u*N+v])
                      * int(self.DW[b][r, (d-v)*N+w])
                      * int(self.DW[c][0, (d-w)*N+d-u]))
        return value % p

    def source_corner_factorial(self, js):
        a, b, c = js
        r1 = a+b-c
        if min(b+c-a, r1, a+c-b) < 0: return 0
        d, q, p = self.d, self.q, self.p
        value = 0
        for k in range(d-max(a, c)+1):
            u, v = d-a-k, d-c-k
            value += (self.high(a, u)*self.high(c, v)
                      * self.w_factorial(b, r1, v, a+k)
                      * pow(self.pv[u]*self.pv[k]*self.pv[v], -1, p))
        return (pow(q, c*(d-2*c)-2*c, p)*self.cup(2*b, r1)*value) % p

    def regular_corner_sum(self, js):
        """Analytic at the root, including all high partner channels."""
        a, b, c = js
        r1 = a+b-c
        if min(b+c-a, r1, a+c-b) < 0: return 0
        d, p = self.d, self.p
        value = 0
        for k in range(d-max(a, c)+1):
            u, v = d-a-k, d-c-k
            value += (self.high(a, u)*self.high(c, v)
                      * self.w_factorial(b, r1, v, a+k)
                      * pow(self.cup(d, u)*self.cup(d, k)*self.cup(d, v), -1, p))
        return value % p

    def theta_factorial(self, js):
        a, b, c = js
        J, r, r1, r2 = sum(js), b+c-a, a+b-c, a+c-b
        if min(r, r1, r2) < 0: return 0
        q, Q, p, f = self.q, self.Q, self.p, self.fac
        return ((-1)**r1*pow(q, 2*c-r1*(r-1), p)
                * f[2*b]*f[r2]*f[J+1]
                * pow((1-Q)*f[r]*f[2*a]*f[r1]*f[2*c], -1, p)) % p

    def closed_factorial(self, js):
        if min(js[1]+js[2]-js[0], js[0]+js[1]-js[2], js[0]+js[2]-js[1]) < 0:
            return 0
        numerator = (self.source_corner_factorial(js)
                     * self.source_corner_factorial(tuple(reversed(js)))
                     * self.theta_factorial(js))
        denominator = np.prod([self.norm_factorial(j) for j in js], dtype=object)
        return numerator*pow(int(denominator), -1, self.p) % self.p

    def closed_regular_factorial(self, js):
        a, b, c = js
        J, r, r1, r2 = sum(js), b+c-a, a+b-c, a+c-b
        if min(r, r1, r2) < 0: return 0
        d, q, Q, p, f = self.d, self.q, self.Q, self.p, self.fac
        exponent = d*(3*a+2*b+3*c+3)-4*a*a-4*c*c+2*a*c-2*J
        numerator = ((-1)**d*pow(q, exponent, p)*f[r]*f[r1]*f[r2]*f[J+1]
                     * self.regular_corner_sum(js)
                     * self.regular_corner_sum(tuple(reversed(js))))
        denominator = 1-Q
        for j in js:
            numerator *= f[d-j]*(1-pow(Q, 2*j+1, p))
            denominator *= f[d+j+1]
        return numerator*pow(denominator, -1, p) % p

    def physical_sources(self):
        N, d, p = self.N, self.d, self.p
        J = np.zeros((N*N,)*3, dtype=np.int64)
        cap = J.copy()
        for u, v, w in itertools.product(range(N), repeat=3):
            ids = (u*N+v, (d-v)*N+w, (d-w)*N+d-u)
            J[ids] = self.pv[u]*self.pv[v]*self.pv[w] % p
            cap[ids] = pow(self.pv[d-u]*self.pv[d-v]*self.pv[d-w], -1, p)
        return J, cap


def generic_level(N, q=2, p=1000003, closed=False):
    g = Generic(N, q, p)
    identity = np.eye(N*N, dtype=np.int64)
    total = np.zeros_like(identity)
    entries = endpoints = 0
    for j in range(N):
        W, DW = g.W[j], g.DW[j]
        assert np.array_equal(DW@W % p, g.norm_factorial(j)*np.eye(2*j+1, dtype=np.int64) % p)
        assert np.array_equal(g.projector[j]@g.projector[j] % p, g.projector[j])
        total = (total+g.projector[j]) % p
        for u in range(g.d-j+1):
            assert W[(j+u)*N+g.d-u, 2*j] == pow(q, j*(g.d-2*j), p)*g.high(j, u) % p
            endpoints += 1
        for r in range(2*j+1):
            for A in range(N):
                B = g.d-j+r-A
                if 0 <= B < N:
                    assert W[A*N+B, r] == g.w_factorial(j, r, A, B)
                    entries += 1
    assert np.array_equal(total, identity)
    triples = physical = 0
    if closed: J, cap = g.physical_sources()
    for js in itertools.product(range(N), repeat=3):
        a, b, c = js
        if min(b+c-a, a+b-c, a+c-b) < 0:
            if not closed: continue
        else:
            assert g.source_corner_direct(js) == g.source_corner_factorial(js), (N, js, 'corner')
            assert g.closed_factorial(js) == g.closed_regular_factorial(js), (N, js, 'combined')
            triples += 1
        if closed:
            current = J
            for axis, j in enumerate(js): current = axis_apply(g.projector[j], current, axis, p)
            actual = int(np.sum(cap*current) % p)
            assert actual == g.closed_factorial(js), (N, js, actual, g.closed_factorial(js))
            physical += 1
    return {'N': N, 'generic_zeta': q, 'prime': p,
            'all_low_and_high_pair_channels': N,
            'finite_coproduct_entry_checks': entries,
            'generic_lowest_endpoint_checks': endpoints,
            'literal_nested_source_corners': triples,
            'full_physical_closed_triples': physical,
            'all_projector_norms_and_complete_resolution': True}


class RootJet:
    """Exact Z-jets, with zeta=q*(1-Z)^(1/(2N))."""
    def __init__(self, N, order):
        self.N, self.d, self.order = N, N-1, order
        self.p, _, self.q, *_ = balanced_data(N)
        self.Q = self.q*self.q % self.p
        self.zero = (0,)*(order+1)
        self.one = (1,)+(0,)*order
        self.z = (0, 1)+(0,)*(order-1)
        self.fac, self.normunit = [self.one], {}
        unit = self.one
        for k in range(1, 3*N+2):
            factor = self.add(self.one, self.scale(self.zpower(2*k), -1))
            self.fac.append(self.mul(self.fac[-1], factor))
            if k != N: unit = self.mul(unit, factor)
            if N <= k < 2*N: self.normunit[k] = unit
        self.highs = {}
        self.wcache = {}
        self.bcache = {}

    def add(self, a, b): return tuple((x+y) % self.p for x, y in zip(a, b))
    def scale(self, a, c): return tuple(x*c % self.p for x in a)
    def mul(self, a, b):
        out = [0]*(self.order+1)
        for i, x in enumerate(a):
            for j, y in enumerate(b[:self.order+1-i]): out[i+j] += x*y
        return tuple(x % self.p for x in out)
    def product(self, *values):
        out = self.one
        for value in values: out = self.mul(out, value)
        return out
    def inv(self, a):
        inverse = pow(a[0], -1, self.p)
        out = [inverse]
        for k in range(1, self.order+1):
            out.append(-inverse*sum(a[j]*out[k-j] for j in range(1, k+1)) % self.p)
        return tuple(out)
    def zpower(self, exponent):
        p = self.p
        alpha = exponent*pow(2*self.N, -1, p) % p
        value = pow(self.q, exponent, p)
        out = [value]
        for k in range(1, self.order+1):
            value = -value*(alpha-k+1)*pow(k, -1, p) % p
            out.append(value)
        return tuple(out)
    def cup(self, u):
        d, f = self.d, self.fac
        return self.scale(self.product(self.zpower(u*(d-u-1)), f[u], f[d-u], self.inv(f[d])), (-1)**u)
    def high(self, j, u):
        key = j, u
        if key not in self.highs:
            d, l, f = self.d, self.d-j, self.fac
            self.highs[key] = self.scale(self.product(
                self.zpower(u*(2*l-d-u-1)), f[j+u], f[d-u], self.inv(f[j]), self.inv(f[d])), (-1)**u)
        return self.highs[key]
    def w(self, j, r, A, B):
        key = j, r, A, B
        if key not in self.wcache:
            d, l, f = self.d, self.d-j, self.fac
            assert 0 <= A <= d and 0 <= B <= d and A+B == l+r
            total = self.zero
            for u in range(max(0, l-B), min(l, A)+1):
                t = B-l+u
                if not 0 <= t <= r: continue
                term = self.product(self.high(j, u), self.zpower((2*u-d)*t),
                    self.inv(self.product(f[u], f[l-u], f[t], f[r-t])))
                total = self.add(total, term)
            self.wcache[key] = self.product(f[A], f[B], total)
        return self.wcache[key]
    def B(self, js):
        if js not in self.bcache:
            a, b, c = js
            total = self.zero
            for k in range(self.d-max(a, c)+1):
                u, v = self.d-a-k, self.d-c-k
                term = self.product(self.high(a, u), self.high(c, v), self.w(b, a+b-c, v, a+k),
                                    self.inv(self.product(self.cup(u), self.cup(k), self.cup(v))))
                total = self.add(total, term)
            self.bcache[js] = total
        return self.bcache[js]
    def regular_trace(self, js):
        a, b, c = js
        J, r, r1, r2 = sum(js), b+c-a, a+b-c, a+c-b
        if min(r, r1, r2) < 0: return self.zero
        d, f = self.d, self.fac
        exponent = d*(3*a+2*b+3*c+3)-4*a*a-4*c*c+2*a*c-2*J
        value = self.scale(self.product(self.zpower(exponent), f[r], f[r1], f[r2], f[J+1],
                         self.B(js), self.B(tuple(reversed(js))), self.inv(self.add(self.one, self.scale(self.zpower(2), -1)))), (-1)**d)
        for j in js:
            gamma = self.one if 2*j == d else self.add(self.one, self.scale(self.zpower(4*j+2), -1))
            value = self.product(value, f[d-j], gamma, self.inv(self.normunit[self.N+j]))
        return value
    def circle(self, j):
        c = self.add(self.zpower(2*j+1), self.zpower(-2*j-1))
        previous, value = self.one, c
        if self.d == 0: return self.one
        for _ in range(2, self.N): previous, value = value, self.add(self.mul(c, value), self.scale(previous, -1))
        return self.scale(value, (-1)**self.d)
    def circle_factored(self, j):
        assert 2*j != self.d
        step = self.add(self.one, self.scale(self.z, -1))
        value, term = self.zero, self.one
        for _ in range(2*j+1):
            value = self.add(value, term)
            term = self.mul(term, step)
        return self.scale(self.product(self.zpower(-self.d*(2*j+1)), value,
            self.inv(self.add(self.one, self.scale(self.zpower(4*j+2), -1)))), (-1)**self.d)


def root_moment_level(N, labels):
    p, _, q, E, F, K, *_ = balanced_data(N)
    d, Q, x = N-1, q*q % p, pow(q, N-1, p)
    rho = (q-pow(q, -1, p)) % p
    Et, Ft, Kt = coproduct(rho*rho*E % p, F, K, 2, N, p)
    Ki = np.diag([pow(int(v), -1, p) for v in np.diag(Kt)])
    O = (Ft@Et+q*Kt+pow(q, -1, p)*Ki) % p
    identity = np.eye(N*N, dtype=np.int64)
    previous, circle = identity, O
    for _ in range(2, N): previous, circle = circle, (O@circle-previous) % p
    circle = (-1)**d*circle % p
    nodes = [(pow(q, 2*j+1, p)+pow(q, -2*j-1, p)) % p for j in range(d//2+1)]
    projectors = {}
    for j in set(labels):
        value, derivative = identity.copy(), 0
        for k, ck in enumerate(nodes):
            if j == k: continue
            multiplicity = 1 if 2*k == d else 2
            for _ in range(multiplicity): value = value@(O-ck*identity) % p * pow(nodes[j]-ck, -1, p) % p
            derivative = (derivative+multiplicity*pow(nodes[j]-ck, -1, p)) % p
        if 2*j < d: value = value@(identity-derivative*(O-nodes[j]*identity)) % p
        projectors[j] = value
    source, _, mark = sources(N, x, p)
    value = source
    for axis, j in enumerate(labels): value = axis_apply(projectors[j], value, axis, p)
    active = [axis for axis, j in enumerate(labels) if 2*j < d]
    rank = len(active)
    jet = RootJet(N, rank+1)
    branches = [((j,) if 2*j == d else (j, d-j)) for j in labels]
    sums = [jet.zero]*(1 << rank)
    factored_sums = [jet.zero]*(1 << rank)
    for js in itertools.product(*branches):
        regular = jet.regular_trace(js)
        for axis in active:
            assert jet.circle(js[axis]) == jet.mul(jet.z, jet.circle_factored(js[axis]))
        for mask in range(1 << rank):
            term = regular
            factored = regular
            for bit, axis in enumerate(active):
                if mask >> bit & 1:
                    term = jet.mul(term, jet.circle(js[axis]))
                    factored = jet.mul(factored, jet.circle_factored(js[axis]))
            sums[mask] = jet.add(sums[mask], term)
            factored_sums[mask] = jet.add(factored_sums[mask], factored)
    moments = []
    for mask in range(1 << rank):
        current = value
        for bit, axis in enumerate(active):
            if mask >> bit & 1: current = axis_apply(circle, current, axis, p)
        actual = int(np.sum(mark*current) % p)
        predicted = (-1)**d*rho*sums[mask][rank+1] % p
        degree = rank+1-mask.bit_count()
        assert predicted == (-1)**d*rho*factored_sums[mask][degree] % p
        assert not any(factored_sums[mask][:degree])
        assert actual == predicted, (N, labels, mask, actual, predicted)
        assert not any(sums[mask][:rank+1]), (N, labels, mask, 'uncancelled pole/trace constant')
        moments.append(actual)
    return {'N': N, 'folded_labels': list(labels), 'paired_axes': rank,
            'generic_singleton_branches': 1 << rank, 'jet_order': rank+1,
            'all_original_marked_moments': moments,
            'paired_circle_factors_reduce_required_jet_order': True,
            'all_poles_and_ordinary_trace_constant_cancel_exactly': True}


if __name__ == '__main__':
    rows = [generic_level(N, closed=N <= 4) for N in range(2, 9)]
    rows += [generic_level(N, q=3, p=1000033, closed=N <= 3) for N in range(2, 6)]
    roots = [root_moment_level(N, (j,)*3) for N in range(2, 8) for j in {0, (N-1)//2}]
    roots += [root_moment_level(5, js) for js in ((1, 2, 2), (0, 1, 2), (0, 1, 1))]
    out = {'status': 'PASS', 'generic_original_source_families': rows,
           'complete_root_cluster_marked_jet_families': roots,
           'scope': 'Exact generic finite-field comparisons including high partner channels. Finite audits supplement the factorial derivations; no conditioning or general graph asymptotic is asserted.'}
    Path(__file__).with_name('actual_generic_six_head_tetrahedral_source_results.json').write_text(json.dumps(out, indent=2)+'\n')
    print('PASS', len(rows), 'generic all-channel families;',
          sum(x['literal_nested_source_corners'] for x in rows), 'literal corners;',
          sum(x['full_physical_closed_triples'] for x in rows), 'full physical contractions;',
          len(roots), 'all-moment root cluster jet families')
