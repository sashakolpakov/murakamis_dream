#!/usr/bin/env python3
"""Rational certificates for the scalar full-Psi moment-cycle radii.

No finite matrix source is used in the graph. The literal cup/cap K_N
polynomials are bounded-capacity edges; every other geometric kernel is
an untruncated Hardy edge. All capacities and source charges are scaled
by d=N-1, so the certificates hold for every N simultaneously.
"""

from fractions import Fraction
import json
from pathlib import Path

import numpy as np
from scipy.optimize import linprog

from audit_actual_cyclic_hardy_dilog_network import elementary_gates


class ScalarFlowGraph:
    def __init__(self, heads, letters):
        assert heads % 2 == 0
        self.heads, self.letters = heads, letters
        self.gamma = []
        self.edges = []
        self.caps = []
        self.current = self.nodes()
        self.initial = self.current[:]
        for i in range(0, heads, 2):
            self.gamma[self.current[i+1]] += 1
            self.caps.append((self.current[i+1], self.current[i], 'cup'))
        for gate in elementary_gates(letters):
            self.gate(gate)
            self.reset()
        for i in range(0, heads, 2):
            self.gamma[self.current[i+1]] -= 1
            self.caps.append((self.current[i], self.current[i+1], 'cap'))
        self.final = self.current[:]
        n = len(self.gamma)
        self.V = np.zeros((n, len(self.edges)+len(self.caps)), dtype=np.int64)
        for j, (a, b, *_) in enumerate(self.edges+self.caps):
            self.V[a, j] -= 1
            self.V[b, j] += 1
        self.gamma = np.array(self.gamma, dtype=np.int64)
        self.atom_ids = [j for j, edge in enumerate(self.edges) if edge[2] == 'atom']
        self.bounds = [(0, None)]*len(self.edges)+[(0, 1)]*len(self.caps)

    def nodes(self):
        out = list(range(len(self.gamma), len(self.gamma)+self.heads))
        self.gamma += [0]*self.heads
        return out

    def edge(self, a, b, kind='Hardy'):
        self.edges.append((a, b, kind))

    def reset(self):
        out = self.nodes()
        for a, b in zip(self.current, out):
            self.edge(a, b)
        self.current = out

    def gate(self, gate):
        old, out = self.current, self.nodes()
        if gate[0] == 'transfer':
            numerator, denominator = gate[1:]
            self.edge(old[denominator], old[numerator], 'atom')
        for i, (a, b) in enumerate(zip(old, out)):
            if gate[0] == 'Udiag' and i == gate[1]:
                self.edge(a, b, 'atom')
            elif gate[0] == 'Fdiag' and i == gate[1]:
                self.gamma[a] -= 1
                self.gamma[b] += 1
                self.edge(b, a, 'atom')
            elif gate[0] == 'Gaussian' and i == gate[1]:
                self.edge(a, b, 'Gaussian')
            else:
                self.edge(a, b)
        self.current = out

    def flow_optimum(self, costs):
        result = linprog(-np.array([float(c) for c in costs]),
                         A_eq=self.V, b_eq=-self.gamma,
                         bounds=self.bounds, method='highs')
        assert result.success, result.message
        flow = np.rint(result.x).astype(np.int64)
        # Integral incidence/capacity vertex: exact checks after rational recovery.
        assert np.max(np.abs(flow-result.x)) < 1e-7
        assert np.array_equal(self.V@flow, -self.gamma)
        assert min(flow) >= 0
        assert max(flow[len(self.edges):]) <= 1
        return result, flow

    def radius_certificate(self, taus, eta=Fraction(1, 10)):
        assert len(taus) == len(self.atom_ids)
        ell = [Fraction(0)]*self.V.shape[1]
        for j, tau in zip(self.atom_ids, taus):
            ell[j] = tau
        # Fixed arbitrary log-modulus costs emulate color and Gaussian dilations.
        for j, edge in enumerate(self.edges):
            if edge[2] == 'Gaussian':
                ell[j] += Fraction((-1)**j*(j % 7), 5)
        costs = [ell[j]+(eta if j < len(self.edges) else 0)
                 for j in range(self.V.shape[1])]
        result, flow = self.flow_optimum(costs)
        # TU dual potentials with denominator dividing the rational cost denominator.
        radius = [Fraction(float(v)).limit_denominator(10000)
                  for v in result.eqlin.marginals]
        active = [sum(Fraction(int(self.V[i, j]))*radius[i]
                      for i in range(len(radius)))+ell[j]
                  for j in range(self.V.shape[1])]
        assert all(v <= -eta for v in active[:len(self.edges)])
        source_bound = sum(Fraction(int(g))*r for g, r in zip(self.gamma, radius))
        source_bound += sum(max(Fraction(0), v) for v in active[len(self.edges):])
        dual_value = sum(c*int(f) for c, f in zip(costs, flow))
        assert source_bound == dual_value
        assert all(flow[j] <= 1 for j in self.atom_ids)
        assert max(flow[:len(self.edges)]) <= self.heads//2
        rough_bound = sum(taus)+sum(abs(ell[j]) for j in range(len(ell))
                                    if j not in self.atom_ids)*self.heads//2
        rough_bound += eta*len(self.edges)*self.heads//2
        assert source_bound <= rough_bound
        return {'atom_radius_logs': [str(t) for t in taus],
                'rational_source_log_bound': str(source_bound),
                'exact_primal_dual_agreement': True,
                'all_geometric_kernel_radius_margins': str(eta),
                'maximum_atom_flow': int(max(flow[j] for j in self.atom_ids)),
                'maximum_internal_head_flow': int(max(flow[:len(self.edges)])),
                'torus_log_radii': [str(r) for r in radius]}

    def all_atom_capacity_certificates(self):
        for selected in self.atom_ids:
            costs = [Fraction(0)]*self.V.shape[1]
            costs[selected] = Fraction(1)
            result, flow = self.flow_optimum(costs)
            assert int(flow[selected]) <= 1
            radius = [Fraction(float(v)).limit_denominator(1000)
                      for v in result.eqlin.marginals]
            reduced = [sum(Fraction(int(self.V[i, j]))*radius[i]
                           for i in range(len(radius)))+costs[j]
                       for j in range(self.V.shape[1])]
            assert all(v <= 0 for v in reduced[:len(self.edges)])
            upper = sum(Fraction(int(g))*r for g, r in zip(self.gamma, radius))
            upper += sum(max(Fraction(0), v) for v in reduced[len(self.edges):])
            assert upper == int(flow[selected]) <= 1
        return len(self.atom_ids)


class ReducedScalarFlowGraph(ScalarFlowGraph):
    """Contract the head-Hardy forest, without retaining its positivity constraints."""

    def __init__(self, original):
        self.heads, self.letters = original.heads, original.letters
        parent = list(range(len(original.gamma)))
        def root(a):
            while parent[a] != a:
                parent[a] = parent[parent[a]]
                a = parent[a]
            return a
        forest_edges = []
        for a, b, kind in original.edges:
            if kind != 'atom':
                assert root(a) != root(b), 'Head-Hardy graph must be a forest'
                parent[root(b)] = root(a)
                forest_edges.append((a, b))
        roots = sorted({root(a) for a in range(len(parent))})
        labels = {a: j for j, a in enumerate(roots)}
        self.node_map = [labels[root(a)] for a in range(len(parent))]
        self.gamma = np.zeros(len(roots), dtype=np.int64)
        for a, value in enumerate(original.gamma):
            self.gamma[self.node_map[a]] += value
        self.edges = [(self.node_map[a], self.node_map[b], kind)
                      for a, b, kind in original.edges if kind == 'atom']
        self.caps = [(self.node_map[a], self.node_map[b], kind)
                     for a, b, kind in original.caps]
        self.V = np.zeros((len(roots), len(self.edges)+len(self.caps)), dtype=np.int64)
        for j, (a, b, *_) in enumerate(self.edges+self.caps):
            self.V[a, j] -= 1
            self.V[b, j] += 1
        self.atom_ids = list(range(len(self.edges)))
        self.bounds = [(0, None)]*len(self.edges)+[(0, 1)]*len(self.caps)
        self.original = original
        self.original_atom_ids = original.atom_ids
        self.forest_ids = [j for j, e in enumerate(original.edges) if e[2] != 'atom']

    def flow_optimum(self, costs):
        result, flow = super().flow_optimum(costs)
        old = self.original
        full = np.zeros(old.V.shape[1], dtype=np.float64)
        for j, original_j in enumerate(self.original_atom_ids):
            full[original_j] = flow[j]
        full[len(old.edges):] = flow[len(self.edges):]
        remainder = -old.gamma-old.V@full
        forest_matrix = old.V[:, self.forest_ids]
        missing, *_ = np.linalg.lstsq(forest_matrix, remainder, rcond=None)
        integer_missing = np.rint(missing).astype(np.int64)
        assert np.max(np.abs(missing-integer_missing)) < 1e-7
        full[self.forest_ids] = integer_missing
        exact = np.rint(full).astype(np.int64)
        assert np.array_equal(old.V@exact, -old.gamma)
        assert min(integer_missing) >= 0, 'A negative omitted head current must not reenter'
        assert max(integer_missing) <= self.heads//2
        return result, flow


def main():
    cases = [(2, [1]), (2, [-1, 1]), (4, [1, -2, 3, 2]),
             (4, [2, -1, 3, 2, -2, 1]),
             (6, [1, -2, 3, -4, 5, 2, -3, 4])]
    rows, capacity_count, reduced_count = [], 0, 0
    for heads, word in cases:
        graph = ScalarFlowGraph(heads, word)
        capacity_count += graph.all_atom_capacity_certificates()
        radii = []
        for kind in range(3):
            taus = ([Fraction(0)]*len(graph.atom_ids) if kind == 0 else
                    [Fraction((j*(kind+2)+kind) % 11, 2) for j in range(len(graph.atom_ids))])
            radii.append(graph.radius_certificate(taus))
        rows.append({'heads': heads, 'word': word, 'head_variables': len(graph.gamma),
                     'untruncated_scalar_Hardy_edges': len(graph.edges),
                     'full_Psi_moment_atoms': len(graph.atom_ids),
                     'literal_bounded_cap_edges': len(graph.caps),
                     'all_atom_capacities_certified_at_every_N': True,
                     'radius_certificates': radii})
        reduced = ReducedScalarFlowGraph(graph)
        reduced_count += reduced.all_atom_capacity_certificates()
        reduced_radii = [reduced.radius_certificate(
            [Fraction((j*5+kind) % 9, 2) for j in reduced.atom_ids]) for kind in range(2)]
        assert len(reduced.gamma) == heads+6*len(word)
        rows[-1]['exact_Hardy_forest_contraction'] = {
            'head_variables': len(reduced.gamma), 'remaining_head_Hardy_kernels': 0,
            'all_omitted_head_flow_constraints_reconstructed_nonnegative': True,
            'all_reduced_atom_capacity_certificates': len(reduced.atom_ids),
            'radius_certificates': reduced_radii}
    output = {'status': 'PASS', 'all_N_atom_capacity_certificates': capacity_count,
              'reduced_all_N_atom_capacity_certificates': reduced_count,
              'scalar_relative_cycle_radius_cases': rows,
              'scope': 'Exact rational toric-flow certificates for scalar full-Psi cycle convergence; no geometric intersection or global noncancellation claim.'}
    Path(__file__).with_name('actual_full_psi_scalar_flow_cycle_results.json').write_text(json.dumps(output, indent=2)+'\n')
    print(f'PASS {capacity_count} original + {reduced_count} reduced all-N atomic capacity certificates, '
          f'{3*len(rows)} original + {2*len(rows)} reduced rational full-cycle radius certificates')


if __name__ == '__main__':
    main()
