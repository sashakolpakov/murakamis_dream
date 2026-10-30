#!/usr/bin/env python3
"""Exact local certificates and incidence reconstruction for the Casimir plat.

The finite graph checks are regression tests for the general spanning-tree
proof. The matrix identities are symbolic identities before any Artin
specialization; no numerical Hessian rank is substituted for the theorem.
"""
import json
from collections import deque
from pathlib import Path

import sympy as s


def rat(x):
    return s.factor(x)


def mat(x):
    return x.applyfunc(rat)


def regular_centralizer():
    J, a, k, m = s.symbols('J a k m', nonzero=True)
    P = s.Matrix([[J, 1], [0, 1/J]])
    lower = 2-2*J-J*a+a/J
    A = s.Matrix([[a, -(a+1)**2/lower], [lower, -2-a]])
    B = mat(P*A.inv())
    assert rat(A.det()-1) == 0 and rat(s.trace(A)+2) == 0
    assert rat(B.det()-1) == 0 and rat(s.trace(B)+2) == 0
    Q = P-s.eye(2)/J
    C = s.eye(2)+k*Q
    R = 1+k*(J-1/J)
    assert rat(C.det()-R) == 0
    Ao = mat(C*A*C.inv())
    bracket = Q*A-A*Q
    denominator = rat(s.trace(bracket*(Q*A-Ao*Q)))
    numerator = rat(s.trace(bracket*(Ao-A)))
    assert rat(numerator/denominator-k) == 0
    assert rat(denominator.subs(J, -1)) == 32
    H = P.subs(J, -1)+s.eye(2)
    A0 = mat(A.subs(J, -1))
    assert mat(H*H) == s.zeros(2)
    assert rat(s.trace(H*A0)) == 4
    assert mat(Ao.subs(J, -1)-(A0+k*(H*A0-A0*H)-4*k*k*H)) == s.zeros(2)
    rows = []
    Htwist = P.inv()-s.eye(2)
    hJ = 1/J-1
    for epsilon in (0, 1, -1):
        auxiliary = mat(m*R*hJ**(-epsilon)*C.inv()*Htwist**epsilon)
        assert mat(auxiliary*P-P*auxiliary) == s.zeros(2)
        assert rat(auxiliary[0, 0]-m) == 0
        assert rat(auxiliary.det()-m*m*R*(-J)**epsilon) == 0
        transport = mat(Htwist**epsilon*auxiliary.inv())
        assert mat(transport*A*transport.inv()-Ao) == s.zeros(2)
        assert mat(auxiliary.subs({J: -1, m: 1})
                   -(s.eye(2)+(s.Rational(epsilon, 2)-k)*H)) == s.zeros(2)
        rows.append(dict(epsilon=epsilon, selected_eigenvalue='m',
                         determinant='m^2 R0 (-J)^epsilon',
                         actual_transport_and_endpoint=True))
    return dict(regular_denominator=str(denominator),
                endpoint_denominator=32, signed_auxiliary=rows)


def head(X, S):
    K, F, E = -1/X, S*(1-X), (1/X-1)/S
    L = s.Matrix([[1, 0], [-K*F, K]])
    G = s.Matrix([[K, E], [F*K, F*E+1/K]])
    return G, L


def boundaries_and_adapter():
    X, S = s.symbols('X S', nonzero=True)
    G1, L1 = head(X, S)
    G2, _ = head(1/X, -S)
    assert mat((G1+s.eye(2))*s.Matrix([1, S])) == s.zeros(2, 1)
    assert mat(L1.inv()*G2*L1*G1) == s.eye(2)
    # Exact local canonical one-form modulo degree conservation.
    d, yi, yo, h = s.symbols('d yi yo h')
    ds, du, dv = s.symbols('ds du dv')
    incoming = [h+d+yi, h+d]
    outgoing = [h-yo, h]
    one_form = incoming[0]*dv+incoming[1]*(ds-dv)
    one_form -= outgoing[0]*du+outgoing[1]*(ds-du)
    assert s.expand(one_form-(d*ds+yo*du+yi*dv)) == 0
    # The high adapter is the literal chain rule, independent of xi.
    adapter = s.Matrix([[-1, 0, 0], [-1, 1, 0], [-1, 0, 1]])
    assert adapter.T*s.Matrix([d, yo, yi]) == s.Matrix([-d-yo-yi, yo, yi])
    boundary = []
    for name, incidence, derivatives in (
            ('cup', -1, [s.I*s.pi, 0]),
            ('ordinary_cap', 1, [s.I*s.pi, 0]),
            ('marked_cap', 1, [0, s.I*s.pi])):
        ratio = s.exp(incidence*(derivatives[0]-derivatives[1]))
        assert s.simplify(ratio+1) == 0
        boundary.append(name)
    # A trace-only invariant Artin flag has an extra infinitesimal freedom.
    # The source's exact eigenvalue/kernel condition excludes it.
    e = s.symbols('e')
    nilpotent = s.Matrix([[-1, 1], [0, -1]])
    moving_flag = s.Matrix([1, e])
    residual = nilpotent*moving_flag-(-1+e)*moving_flag
    assert all(s.rem(x, e**2, e) == 0 for x in residual)
    exact_kernel_residual = (nilpotent+s.eye(2))*moving_flag
    assert exact_kernel_residual == s.Matrix([e, 0])
    return dict(boundaries=boundary, inverse_pair_and_exact_kernel=True,
                high_adapter='(-d-yo-yi, yo, yi)',
                trace_only_nilpotent_flag_counterexample_retained=True)


def event_graph(width, positions):
    types = ['cup']*width
    active = [v for v in range(width) for _ in range(2)]
    edges = []
    for slot in positions:
        vertex = len(types)
        types.append('coupon')
        for strand in (slot, slot+1):
            edges.append((active[strand], vertex))
            active[strand] = vertex
    for pair in range(width):
        vertex = len(types)
        types.append('cap')
        for strand in (2*pair, 2*pair+1):
            edges.append((active[strand], vertex))
    return types, edges


def recover_potentials(vertices, edges, c):
    adjacent = [[] for _ in range(vertices)]
    for e, (tail, head) in enumerate(edges):
        adjacent[tail].append((head, e, True))
        adjacent[head].append((tail, e, False))
    values = [None]*vertices
    roots = []
    for start in range(vertices):
        if values[start] is not None:
            continue
        roots.append(start)
        values[start] = s.Integer(1)
        queue = deque([start])
        while queue:
            vertex = queue.popleft()
            for other, e, forward in adjacent[vertex]:
                expected = values[vertex]/c[e] if forward else values[vertex]*c[e]
                if values[other] is None:
                    values[other] = expected
                    queue.append(other)
                else:
                    assert values[other] == expected
    return values, roots


def incidence_case(width, positions):
    types, edges = event_graph(width, positions)
    nv, ne = len(types), len(edges)
    B = s.zeros(nv, ne)
    for e, (tail, head) in enumerate(edges):
        B[tail, e], B[head, e] = -1, 1
    wire_momenta = [s.Rational(e+3, e+2) for e in range(ne)]
    vertex_scales = [s.Rational(v+5, v+3) for v in range(nv)]
    local = {}
    c = []
    for e, (tail, head) in enumerate(edges):
        for v in (tail, head):
            local[v, e] = (wire_momenta[e]/vertex_scales[v])**B[v, e]
        c.append(local[tail, e]*local[head, e])
    cycles = B.nullspace()
    for cycle in cycles:
        assert all(x.q == 1 for x in cycle)
        assert s.prod(c[e]**cycle[e] for e in range(ne)) == 1
    reconstructed, roots = recover_potentials(nv, edges, c)
    assert B.rank() == nv-len(roots)
    assert len(cycles) == ne-nv+len(roots)
    for e, (tail, head) in enumerate(edges):
        left = reconstructed[tail]*local[tail, e]**B[tail, e]
        right = reconstructed[head]*local[head, e]**B[head, e]
        assert left == right
        assert left/wire_momenta[e] == reconstructed[tail]/vertex_scales[tail]
    b = s.Matrix([-1 if t == 'cup' else 1 if t == 'cap' else 0 for t in types])
    for component_indicator in B.T.nullspace():
        assert (component_indicator.T*b)[0] == 0
    # Every cycle gives a genuine omitted-edge obstruction, including parallel wires.
    if cycles:
        index = next(e for e in range(ne) if cycles[0][e])
        changed = c[:]
        changed[index] *= 2
        assert s.prod(changed[e]**cycles[0][e] for e in range(ne)) != 1
    return dict(width=width, coupons=len(positions), vertices=nv, wires=ne,
                components=len(roots), primitive_cycle_rank=len(cycles),
                exact_shared_momenta=True)


def main():
    cases = []
    for width in range(2, 8):
        odd = list(range(1, 2*width-2, 2))
        even = list(range(0, 2*width-1, 2))
        for positions in ([], odd, odd+even+odd, odd+even+odd+even+odd):
            cases.append(incidence_case(width, positions))
    out = dict(status='PASS', centralizer=regular_centralizer(),
               physical_boundaries=boundaries_and_adapter(), event_graphs=cases,
               scope='Formal actual Casimir critical/representation equivalence. '
                     'No physical support, selected Poisson cycle, amplitude or asymptotic assertion.')
    Path(__file__).with_name('actual_augmented_plat_critical_scheme_results.json').write_text(
        json.dumps(out, indent=2)+'\n')
    print('PASS regular parabolic inverse and 3 signed auxiliary meridians; '
          'actual cups/caps and high adapter; 24 exact event-graph reconstructions')


if __name__ == '__main__':
    main()
