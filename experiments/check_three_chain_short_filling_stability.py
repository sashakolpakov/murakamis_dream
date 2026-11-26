#!/usr/bin/env python3
"""Exact diagnostics/bookkeeping for marked short-chain stability.

All-N trace and mirror identities have cited algebraic proofs. Exact
finite quotient calculations here diagnose normalization and first-normal
retention at one even and one odd level, not an all-level theorem.
"""
import argparse
from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--precision', type=int, default=256,
                    help='Recorded downstream replay precision; all new calculations are exact.')
    ap.add_argument('--output', type=Path,
                    default=ROOT/'repro/results/research-three-chain-short-filling-stability.json')
    args = ap.parse_args()
    z = sp.Symbol('z', real=True)
    diagnostics = []

    def zero(label, expression, level):
        difference = sp.simplify(sp.expand(expression))
        assert difference == 0, (label, level, difference)
        diagnostics.append({'identity': label, 'level': level})

    for N in (2, 3):
        D = N-1
        q = sp.cos(sp.pi/N)+sp.I*sp.sin(sp.pi/N)
        kappa = sp.cos(sp.pi*D*D/(2*N))+sp.I*sp.sin(sp.pi*D*D/(2*N))
        roots = [2*sp.cos(sp.pi*(2*j+1)/N) for j in range(N)]
        factorial = [sp.Integer(1)]
        for j in range(1, N):
            factorial.append(sp.simplify(factorial[-1]*2*sp.sin(sp.pi*j/N)))
        basis = []
        product = sp.Integer(1)
        for j in range(N):
            basis.append(sp.expand(product/factorial[j]**2))
            product *= roots[j]-z
        P = sp.Poly(2*(sp.chebyshevt(N, z/2)+1), z)

        def reduced(expression):
            rem = sp.rem(sp.Poly(sp.expand(expression), z, domain='EX'), P)
            return sp.Poly.from_dict(
                {monomial: sp.simplify(value) for monomial, value in rem.terms()}, z,
                domain='EX').as_expr()

        def trace(expression):
            return sp.simplify((-1)**D*N**2*sp.Poly(reduced(expression), z).coeff_monomial(z**D))

        M = sp.Matrix(N, N, lambda i, j: sp.simplify(
            kappa*(-1)**i*q**(i*(j+1))*factorial[i]/(factorial[j]*factorial[i-j]))
            if j <= i else 0)
        J = sp.Matrix(N, N, lambda i, j: int(i+j == D))
        R = sp.expand(sum(M[i, 0]*basis[i] for i in range(N)))
        Rminus = sp.conjugate(R)
        zero('original crossing and conjugate are quotient inverses', reduced(R*Rminus)-1, N)
        for j in range(N):
            zero('original crossing multiplication column',
                 reduced(R*basis[j])-sum(M[i, j]*basis[i] for i in range(N)), N)
        for i in range(N):
            for j in range(N):
                zero('full quotient trace Gram is J', trace(basis[i]*basis[j])-J[i, j], N)
                zero('original matrix conjugation is inverse', (M*sp.conjugate(M))[i, j]-int(i == j), N)
                zero('bilinear self-adjointness', (M.T*J-J*M)[i, j], N)
        Aplus = (J*M**3).applyfunc(sp.simplify)
        Aminus = (J*sp.conjugate(M)**3).applyfunc(sp.simplify)
        for sign, crossing, AA in ((1, R, Aplus), (-1, Rminus, Aminus)):
            crossing3 = reduced(crossing**3)
            for i in range(N):
                for j in range(N):
                    zero('literal signed power-three trace equals JM^(3sigma)',
                         trace(crossing3*basis[i]*basis[j])-AA[i, j], N)
        for i in range(N):
            for j in range(N):
                zero('uniform path mirror matrix identity', Aminus[i, j]-sp.conjugate(Aplus[i, j]), N)
        # The exact quotient is nonreduced in both cases, so the trace
        # diagnostics above genuinely include double-root normal data.
        gcd_degree = sp.gcd(P, P.diff()).degree()
        assert gcd_degree == N//2

    exact = []
    m, k, boundary, remaining = sp.symbols('m k boundary remaining', integer=True, positive=True)
    assert sp.simplify(sp.Rational(3, 2)*(m-(m+1))+sp.Rational(3, 2)) == 0
    exact.append('m degree-two selected vertices and m+1 edges give N^(-3/2)')
    # Exponents of the two independent unit symbols C and kappa.
    assert (m-(m-2), m-2) == (2, m-2)
    exact.append('C^m (kappa/C)^(m-2)=C^2 kappa^(m-2)')
    assert sp.simplify(sp.Rational(3, 2)*(k-(k-1+boundary))
                       -sp.Rational(3, 2)*(1-boundary)) == 0
    exact.append('component edge/vertex count includes every boundary incidence')
    selected, total = sp.symbols('selected total', integer=True, positive=True)
    prefactor = -sp.Rational(3, 2)*((total-1)-selected)
    assert sp.simplify(prefactor.subs(total, selected+remaining)
                       +sp.Rational(3, 2)*remaining-sp.Rational(3, 2)) == 0
    exact.append('all remaining original traces produce final N^(3/2)')
    eta, sigma = sp.symbols('eta sigma', real=True)
    p = (eta-3*sigma)/2
    assert sp.expand(eta-2*p-3*sigma) == 0
    exact.append('selected power uses original p=(eta-3sigma)/2')
    t, rr = sp.symbols('t rr')
    positive_period = 3*t+2*sp.I*rr
    negative_period = -3*(-sp.conjugate(t))+2*sp.I*(-sp.conjugate(rr))
    assert sp.expand(negative_period-sp.conjugate(positive_period)) == 0
    exact.append('negative original unit-charge period is conjugate of positive period')
    positive_fill = 3*sp.I*t**2/(4*sp.pi)-sp.I*t
    negative_fill = -3*sp.I*(-sp.conjugate(t))**2/(4*sp.pi)-sp.I*(-sp.conjugate(t))
    assert sp.expand(negative_fill-sp.conjugate(positive_fill)) == 0
    exact.append('original signed filling action is conjugated exactly')

    # A concrete tree with length-three, four, five and six paths
    # sharing one free vertex, plus another selected component. This checks raw
    # degrees when several component polynomials meet one free color.
    path_a = [('a', j) for j in range(3)]
    path_b = [('b', j) for j in range(4)]
    path_c = [('c', j) for j in range(5)]
    path_d = [('d', j) for j in range(6)]
    left, middle, right, upper, outer, branch, leaf = 'left', 'middle', 'right', 'upper', 'outer', 'branch', 'leaf'
    edges = [(left, path_a[0]), *zip(path_a, path_a[1:]), (path_a[-1], middle),
             (middle, path_b[0]), *zip(path_b, path_b[1:]), (path_b[-1], right),
             (middle, path_c[0]), *zip(path_c, path_c[1:]), (path_c[-1], upper),
             (middle, path_d[0]), *zip(path_d, path_d[1:]), (path_d[-1], outer),
             (middle, branch), (branch, leaf)]
    vertices = {v for e in edges for v in e}
    components = [set(path_a), set(path_b), set(path_c), set(path_d), {branch}]
    S = set().union(*components)
    free = vertices-S
    degree = {v: sum(v in e for e in edges) for v in vertices}
    assert len(edges) == len(vertices)-1
    covered = set()
    component_free_incidence = {v: 0 for v in free}
    component_power = Q(0)
    for C in components:
        incident = {i for i, e in enumerate(edges) if any(v in C for v in e)}
        assert not (covered & incident)
        covered |= incident
        boundary_edges = [edges[i] for i in incident if not all(v in C for v in edges[i])]
        assert len(incident) == len(C)-1+len(boundary_edges)
        component_power += Q(3, 2)*(len(C)-len(incident))
        outside = [v for e in boundary_edges for v in e if v not in C]
        assert len(outside) == len(set(outside))
        for v in outside:
            component_free_incidence[v] += 1
        if len(C) in (3, 4, 5, 6):
            assert all(degree[v] == 2 for v in C)
            assert len(boundary_edges) == 2
    untouched = [i for i in range(len(edges)) if i not in covered]
    for v in free:
        original_degree = component_free_incidence[v]+sum(v in edges[i] for i in untouched)
        assert original_degree == degree[v]
    assert component_power-Q(3, 2)*len(untouched)+Q(3, 2)*len(free) == Q(3, 2)
    exact.append('shared free vertices retain all original polynomial-degree incidences')
    exact.append('mixed-component tree partition has no duplicate or omitted edge')

    record_paths = [
        ('research-three-larger-source-closure', 'check_three_larger_source_closure.py'),
        ('research-three-chain-outside-boundary-decay', 'check_three_chain_outside_boundary_decay.py'),
        ('research-three-chain-five-closure', 'certify_three_chain_five_closure.py'),
        ('research-three-chain-five-closure-replay', 'replay_three_chain_five_closure.py'),
        ('research-three-chain-four-closure', 'certify_three_chain_four_closure.py'),
        ('research-three-chain-four-closure-replay', 'replay_three_chain_four_closure.py'),
        ('research-three-chain-three-central-currents', 'check_three_chain_three_central_currents.py'),
        ('research-three-chain-three-central-currents-replay', 'replay_three_chain_three_central_currents.py'),
        ('research-three-chain-three-complements', 'certify_three_chain_three_complements.py'),
        ('research-three-chain-three-complements-replay', 'replay_three_chain_three_complements.py'),
    ]
    provenance = []
    for stem, script in record_paths:
        path = ROOT/'repro/results'/(stem+'.json')
        record = json.loads(path.read_text())
        assert record['status'] == 'passed'
        assert record['script_sha256'] == sha256((ROOT/'experiments'/script).read_bytes()).hexdigest()
        for dep, digest in record.get('dependencies_sha256', {}).items():
            assert sha256((ROOT/dep).read_bytes()).hexdigest() == digest, (stem, dep)
        if stem.endswith('-replay'):
            author_path = ROOT/'repro/results'/(stem.removesuffix('-replay')+'.json')
            assert record['artifact_sha256'] == sha256(author_path.read_bytes()).hexdigest()
        provenance.append({'path': str(path.relative_to(ROOT)),
                           'sha256': sha256(path.read_bytes()).hexdigest(),
                           'current_script_and_dependencies_verified': True})
    deps = [
        'notes/research_three_chain_short_filling_stability.md',
        'notes/research_three_larger_source_closure.md',
        'notes/research_three_chain_outside_boundary_decay.md',
        'notes/research_three_chain_five_closure.md',
        'notes/research_three_chain_four_closure.md',
        'notes/research_three_chain_three_closure.md',
        'notes/research_three_chain_three_central_currents.md',
        'notes/research_componentwise_short_filling_stability.md',
        'notes/research_positive_three_crossing_cycle.md',
        'notes/research_quantum_cap_primitive_source.md',
        'notes/research_three_chain_geometric_chamber.md',
        'notes/research_three_chain_action_volume_calibration.md',
        'notes/research_homogeneous_wire_complete_cap.md',
        'notes/research_positive_point_marked_completion.md',
        'notes/research_long_fillings_complex_boundary_phase.md',
    ]
    result = {
        'status': 'passed', 'downstream_precision_bits': args.precision,
        'arithmetic': 'New finite quotient and bookkeeping calculations are exact SymPy algebra.',
        'scope': 'Normalization diagnostics at N=2,3, plus exact algebraic/graph bookkeeping and passed source provenance. The all-level identities, analytic source estimates, marked completion and knot-component hypotheses are the cited written proofs.',
        'finite_normalization_diagnostics': diagnostics,
        'finite_levels': [2, 3], 'exact_bookkeeping_identities': exact,
        'original_tree_example': {'vertices': len(vertices), 'edges': len(edges),
                                 'selected_vertices': len(S), 'free_vertices': len(free),
                                 'component_sizes': [len(C) for C in components],
                                 'shared_free_vertex_original_degree': degree[middle]},
        'passed_source_records': provenance,
        'script_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
        'dependencies_sha256': {p: sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},
    }
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'status': 'passed', 'exact_finite_diagnostics': len(diagnostics),
                      'exact_bookkeeping_identities': len(exact),
                      'source_records': len(provenance)}, indent=2))


if __name__ == '__main__':
    main()
