#!/usr/bin/env python3
"""Exact checks for the angle-quotient proof, including a flat fiber."""
import json
from pathlib import Path
import sympy as sp


def main():
    ca, cb = sp.symbols('ca cb')
    cc = (1-ca*cb)/(ca+cb)
    matrix = sp.Matrix([[ca+cc, cc], [cc, cb+cc]])
    assert sp.factor(matrix.det()) == 1
    t = sp.symbols('t')
    polynomial = sp.Poly((4*t-1)**3-4*t, t)
    assert polynomial.as_expr() == 64*t**3-48*t**2+8*t-1
    assert polynomial.count_roots(sp.Rational(1,4), 1) == 1
    # A rational interval entirely inside the positive angle branch.
    lo, hi = sp.Rational(1,2), sp.Rational(3,4)
    assert polynomial.count_roots(lo, hi) == 1
    assert polynomial.eval(lo) < 0 < polynomial.eval(hi)
    # First two atoms only: tangent maps in coordinates x,y,z.
    visible = sp.Matrix([[1,0,0], [2,0,0], [-3,0,0],
                         [0,1,0], [0,-1,0], [0,0,0]])
    assert visible.rank() == 2
    assert visible.nullspace() == [sp.Matrix([0,0,1])]
    # On x=1/6 the rational tangent coordinates are y,z.
    boundary_visible = visible[:,1:]
    assert boundary_visible.rank() == 1
    assert boundary_visible.nullspace() == [sp.Matrix([0,1])]
    # At x=1/6 the first atom still increases: sin(x)sin(2x)^2=3/8<1.
    assert sp.sin(sp.pi/6)*sp.sin(sp.pi/3)**2 == sp.Rational(3,8)
    result = {
        'status': 'PASS',
        'hessian_determinant_identity': 1,
        'critical_polynomial': str(polynomial.as_expr()),
        'positive_branch_root_count': 1,
        'isolating_interval': ['1/2','3/4'],
        'visible_tangent_rank': 2,
        'flat_kernel_dimension': 1,
        'boundary_visible_rank': 1,
        'scope': 'Exact algebraic checks supplement the general proof; no geometric gluing claim.'
    }
    path = Path(__file__).with_name('positive_source_algebraic_volume_period_results.json')
    path.write_text(json.dumps(result, indent=2)+'\n')
    print('PASS: Hessian, algebraic critical branch, flat fiber, boundary quotient')


if __name__ == '__main__':
    main()
