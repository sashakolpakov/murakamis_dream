#!/usr/bin/env python3
"""Exact source phases, CD measures and the four octahedral tetrahedra.

The Riemann-sum limit and the negative normalized summand action are
proved analytically. This audit does not assert a global gluing identity.
"""
import json
from pathlib import Path

import sympy as sp

from audit_actual_q_hahn_physical_generic_jet_bound import Jet, original
from audit_high_color_first_normal_r_degree import root_field


def main():
    entries = measures = parity_measures = 0
    Jet.order = 1
    for N in range(3, 26):
        p, eta = root_field(N)
        q0 = eta*eta % p
        Jet.p = p
        q, qb = Jet(q0), Jet(pow(q0, -1, p))
        F, Fb = [Jet(1)], [Jet(1)]
        for r in range(1, N):
            F.append(F[-1]*(1-q**(2*r)))
            Fb.append(Fb[-1]*(1-qb**(2*r)))
        imag = pow(eta, N, p)
        ss = [1]
        for r in range(1, N):
            ss.append(ss[-1]*(pow(q0, r, p)-pow(q0, -r, p))*pow(imag, -1, p) % p)
        for j in range((N-1)//2+1):
            ff, fb = [], []
            for u in range(j+1):
                f = original(N, q, j, j, u, F).c[0]
                fc = original(N, qb, j, j, u, Fb).c[0]
                beta = ss[j]*pow(ss[u]*ss[j-u], -1, p) % p
                assert f == pow(q0, j*u, p)*beta % p
                assert f*fc % p == beta*beta % p
                ff.append(f); fb.append(fc); entries += 1
            sigma = sum(a*a for a in ff) % p
            sigmab = sum(a*a for a in fb) % p
            magnitude = ss[2*j]*pow(ss[j]**2, -1, p) % p
            assert sigma*sigmab % p == magnitude*magnitude % p
            measures += 1
        j = (N-1)//2
        magnitude = ss[2*j]*pow(ss[j]**2, -1, p) % p
        expected = 1 if N % 2 else 2*imag*pow(q0-pow(q0, -1, p), -1, p) % p
        assert magnitude == expected
        parity_measures += 1

    t = sp.symbols('t', positive=True)
    zeta = (1+sp.I*t)/(1-sp.I*t)
    upper1 = (-1-1)/(zeta-1)
    upper2 = (1+1)/(1-zeta)
    lower1 = (1-zeta)/(-2*zeta)
    # The second lower simplex uses (0,-1,1,-zeta).
    lower2 = (0-1)*(-1+zeta)/((0+zeta)*(-1-1))
    for value in (upper1, upper2):
        assert sp.simplify(value-(1+sp.I/t)) == 0
    for value in (lower1, lower2):
        assert sp.simplify(value-1/(1-sp.I/t)) == 0

    metric=sp.diag(-1,1,1,1)
    signs=((1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1))
    for eps in signs:
        vertex=sp.Matrix([sp.sqrt(3),*eps])
        normal=sp.Matrix([1,*[-sp.sqrt(3)*e for e in eps]])
        assert (normal.T*metric*normal)[0]==8
        reflected=vertex-2*(vertex.T*metric*normal)[0]*normal/8
        assert sp.simplify(reflected-2*sp.Matrix([sp.sqrt(3),*[-e for e in eps]]))==sp.zeros(4,1)
        for other in signs:
            if other!=eps:
                assert (sp.Matrix([sp.sqrt(3),*other]).T*metric*normal)[0]==0

    result = dict(status='PASS', exact_highest_source_entries=entries,
                  actual_bilinear_measure_checks=measures,
                  even_and_odd_fold_measure_checks=parity_measures,
                  actual_tetrahedron_shape_identities=4,
                  exact_ideal_cube_reflections=4,
                  scope='Local native highest-weight energy, marked phase, octahedral tetrahedra and ideal cube reflections; no global energy or gluing theorem.')
    Path(__file__).with_name('actual_native_magnetic_energy_local_geometry_results.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
