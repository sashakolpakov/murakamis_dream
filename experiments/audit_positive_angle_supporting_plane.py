#!/usr/bin/env python3
"""Complete-shape edge supporting plane, Gaussian deficit and affine factorial weight."""

import json
import random
from pathlib import Path

import mpmath as mp
import sympy as sp
from flint import acb_poly, arb, ctx


HERE = Path(__file__).parent


def lobachevsky(x):
    if x == 0 or x == 1:
        return mp.mpf(0)
    return mp.im(mp.polylog(2, mp.exp(2j*mp.pi*x)))/2


def setup():
    data = json.loads((HERE/'positive_alias_volume_counterexample_fixture.json').read_text())
    E = sp.Matrix(data['steps'][0]['gluing_rows'][:3])
    A = sp.kronecker_product(sp.eye(3), sp.ones(1, 3))
    C = A.col_join(E)
    rows = list(C.T.rref()[1])
    B = C[rows, :].T
    scalar_rows = list(B.T.rref()[1])
    inverse = B[scalar_rows, :].inv()
    root = next(z for z in mp.polyroots([1, -2, 3, -1]) if mp.im(z) > 0)
    shapes = [root, 2-root+root*root, root]
    angles = []
    for z in shapes:
        angles.extend([mp.arg(z)/mp.pi, mp.arg(1/(1-z))/mp.pi, mp.arg(1-1/z)/mp.pi])
    gradient = [-mp.pi*mp.log(2*mp.sin(mp.pi*x)) for x in angles]
    coefficients = []
    for i in range(len(rows)):
        coefficients.append(mp.fsum(mp.mpf(str(inverse[i, j]))*gradient[scalar_rows[j]]
                                   for j in range(len(rows))))
    recovered = [mp.fsum(mp.mpf(int(B[i, j]))*coefficients[j] for j in range(len(rows)))
                 for i in range(9)]
    error = max(abs(a-b) for a, b in zip(gradient, recovered))
    assert error < mp.mpf('1e-75')
    eta = [mp.mpf(0)]*3
    lam = [mp.mpf(0)]*3
    for row, value in zip(rows, coefficients):
        if row < 3:
            lam[row] = value
        else:
            eta[row-3] = value
    assert max(abs(v) for v in eta) > mp.mpf('.1')
    for row in E.tolist():
        assert abs(mp.fsum(int(v)*x for v, x in zip(row, angles))-2) < mp.mpf('1e-75')
    volume = mp.fsum(lobachevsky(x) for x in angles)
    c = mp.pi**3*min(angles)/64
    ctx.prec = 192
    ar = next(z for z in acb_poly([-1, 3, -2, 1]).roots(tol=1e-48, maxprec=512)
              if z.imag > 0)
    interval_angles = []
    for z in (ar, 2-ar+ar*ar, ar):
        interval_angles.extend([z.arg()/arb.pi(), (1/(1-z)).arg()/arb.pi(),
                                (1-1/z).arg()/arb.pi()])
    assert all(x > arb('.22') for x in interval_angles)
    return E, angles, gradient, eta, volume, c, {
        'row_basis': rows, 'gradient_row_span_residual': str(error),
        'edge_multipliers': list(map(str, eta)), 'volume': str(volume),
        'minimum_angle_certified_above': '.22', 'quadratic_deficit_constant': str(c)}


def supporting_plane_checks(E, angles, gradient, eta, volume, c):
    rng = random.Random(28102026)
    points = []
    for _ in range(120):
        x = []
        for _j in range(3):
            a = rng.randrange(101)
            b = rng.randrange(101-a)
            x.extend([mp.mpf(a)/100, mp.mpf(b)/100, mp.mpf(100-a-b)/100])
        points.append(x)
    for eps in map(mp.mpf, ('1e-2', '1e-4', '1e-6')):
        x = list(angles)
        x[0] += eps
        x[1] -= eps
        points.append(x)
    worst_ratio = mp.inf
    for x in points:
        delta = [a-b for a, b in zip(x, angles)]
        squared = mp.fsum(v*v for v in delta)
        V = mp.fsum(lobachevsky(v) for v in x)
        direct_plane = mp.fsum(g*v for g, v in zip(gradient, delta))
        edge_defect = [mp.fsum(int(v)*a for v, a in zip(row, x))-2 for row in E.tolist()]
        edge_plane = mp.fsum(a*b for a, b in zip(eta, edge_defect))
        assert abs(direct_plane-edge_plane) < mp.mpf('1e-73')
        deficit = volume+edge_plane-V
        assert deficit >= c*squared-mp.mpf('1e-70')
        if squared:
            worst_ratio = min(worst_ratio, deficit/squared)
    return {'local_angle_points_including_boundary': len(points),
            'smallest_observed_deficit_over_squared_distance': str(worst_ratio),
            'proved_global_constant': str(c)}


def factorial_and_affine_checks(E, angles, eta, volume, c):
    rng = random.Random(6132026)
    checks = 0
    for N in (8, 16, 31, 64, 127):
        logs = [mp.mpf(0)]
        for k in range(1, N):
            logs.append(logs[-1]+mp.log(2*mp.sin(mp.pi*k/N)))
        for charge in (N, N-1):
            for _ in range(20):
                k = []
                for _j in range(3):
                    while True:
                        a = rng.randrange(charge+1)
                        b = rng.randrange(charge-a+1)
                        tri = [a, b, charge-a-b]
                        if max(tri) < N:
                            break
                    k.extend(tri)
                y = [mp.mpf(v)/charge for v in k]
                defect = [sum(int(v)*a for v, a in zip(row, k))-2*charge for row in E.tolist()]
                squared = mp.fsum((a-b)**2 for a, b in zip(y, angles))
                plane = volume+mp.fsum(a*b for a, b in zip(eta, defect))/charge-c*squared
                assert mp.fsum(lobachevsky(a) for a in y) <= plane+mp.mpf('1e-70')
                logw = -mp.fsum(logs[v] for v in k)
                # Fixed coarse allowance tests the uniform O(logN) factorial
                # estimate and, in the affine case, the radial modulus term.
                rhs = N*plane/mp.pi+100*mp.log(N)
                assert logw <= rhs
                checks += 1
    local = []
    for N in (4, 7, 10, 31, 64, 127):
        d = N-1
        s = [mp.mpf(1)]
        for k in range(1, N):
            s.append(s[-1]*2*mp.sin(mp.pi*k/N))
        for a in range(N):
            b = (d-a)//2
            cc = d-a-b
            w = 1/(s[a]*s[b]*s[cc])
            binomial = s[a+b]/(s[a]*s[b])
            assert abs(w-binomial/N) < mp.mpf('1e-65')*max(1, abs(w))
        a = b = d//3
        cc = d-a-b
        if cc == a:
            binomial = s[a+b]/(s[a]*s[b])
            ratio = mp.sqrt(N*binomial)
            local.append({'N': N, 'log_full_star_over_one_tetra_amplitude_per_N': str(mp.log(ratio)/N)})
    return {'integer_factorial_defect_packages': checks,
            'exact_affine_binomial_weight_identity': True,
            'full_scalar_vs_square_root_warning': local}


def main():
    mp.mp.dps = 90
    E, angles, gradient, eta, volume, c, certificate = setup()
    out = {'status': 'PASS', 'irregular_complete_geometric_certificate': certificate,
           'supporting_plane_and_quadratic_deficit': supporting_plane_checks(E, angles, gradient, eta, volume, c),
           'quantum_weights_and_affine_normalization': factorial_and_affine_checks(E, angles, eta, volume, c),
           'scope': 'General positive angle upper comparison with bounded/sublinear defects; '
                    'no source-preserving map from the original full Kashaev period asserted.'}
    Path(__file__).with_name('positive_angle_supporting_plane_results.json').write_text(
        json.dumps(out, indent=2)+'\n')
    print('PASS complete irregular supporting-plane certificate,123 global deficit points,200 factorial defect packages and affine binomial identity')


if __name__ == '__main__':
    main()
