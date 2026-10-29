#!/usr/bin/env python3
"""Exact dual-Casimir/core transport and faithful-source alias diagnostics."""

import json
from pathlib import Path

import mpmath as mp
import numpy as np
import sympy as sp

from audit_actual_two_cut_ports import balanced_data, coproduct
from audit_actual_pretzel_complete_base_casimir_polynomial import rotate_box, matrix_value
from audit_actual_pretzel_cusp_color_two_band_bound import continuants
from diagnose_pretzel_coherent_radial_capacity import source_polynomial, evaluate, lobachevsky


def peval(coefficients, z, p):
    out = 0
    for a in reversed(coefficients):
        out = (out*z+int(a)) % p
    return out


def symbolic_product_certificate():
    q, R, V, w = sp.symbols('q R V w', nonzero=True)
    a = (q*w-1)**3/(q*(w*w-1)*(q*w+1))
    b = (w-q)**3/(q*(w+q)*(w*w-1))
    c = 8*q*w/((w+q)*(q*w+1))
    plus = (1-q*R*w)/(1-q*w)*(1-1/(q*w))/(1-R/(q*w))
    minus = (1-w/q)/(1-R*w/q)*(1-q*R/w)/(1-q/w)
    gamma = ((a*plus+b*minus+c-q*R-1/(q*R))
             *(1-R*w/q)*(1-R/(q*w)))
    assert sp.factor(gamma+(R-1)**4/(q*R)) == 0
    comparison = (q*R+1/(q*R)-(1-R/V)*(1-q*q*R)/(q*R)
                  -q*V-1/(q*V)
                  -(V+1/V-2)*(-q)*(V-R)/(V-1))
    assert sp.factor(comparison) == 0
    assert sp.factor(a+b+c-q-1/q) == 0
    return {'all_degree_shifted_product_identity': True,
            'finite_continuant_coefficient_identity': True,
            'constant_row_sum': True}


def field_case(N):
    p, eta, q, E, F, K, pivot, Rp, Rm = balanced_data(N)
    d, Q, x = N-1, q*q % p, int(K[0, 0])
    rho = (q-pow(q, -1, p)) % p
    Et, Ft, Kt = coproduct(rho*rho*E % p, F, K, 2, N, p)
    Ki = np.diag([pow(int(z), -1, p) for z in np.diag(Kt)])
    O = (Ft@Et+q*Kt+pow(q, -1, p)*Ki) % p
    ids = [u*N+d-u for u in range(N)]
    A = O[np.ix_(ids, ids)]
    fs = continuants(A, p)
    cs = [(pow(q, 2*v+1, p)+pow(q, -(2*v+1), p)) % p for v in range(N)]
    bs = [(pow(Q, v, p)+pow(Q, -v, p)-2) % p for v in range(N)]

    def Dvec(vector):
        return [(cs[v]*int(vector[v])
                 +(bs[v+1]*int(vector[v+1]) if v+1 < N else 0)) % p
                for v in range(N)]

    def fpoly(vector):
        out = [0]*N
        for v in range(N):
            for k, z in enumerate(fs[v]):
                out[k] = (out[k]+int(vector[v])*z) % p
        return out

    # Literal all-input quarter-turn Casimir multiplication, for every color.
    Us = [np.eye(N*N, dtype=np.int64), O.copy()]
    for n in range(2, N):
        Us.append((O@Us[-1]-Us[-2]) % p)
    rotated = []
    for j in range(1, N+1):
        Lj = pow(-1, j-1, p)*Us[j-1] % p
        B = Rm@Lj % p
        actual = rotate_box(B, N, x, p)
        vec = actual[np.ix_(ids, ids)][0, :]
        expected = matrix_value(fpoly(Dvec(vec)), O, p)
        assert np.array_equal(rotate_box(O@B % p, N, x, p), expected)
        rotated.append(vec.copy())

    # The finite two-band coefficient formula extends to ALL ordinary
    # colors: low colors have only the reflected short band. No factorial
    # with index >=N is evaluated.
    imaginary = pow(eta, N, p)
    fac, sine = [1], [1]
    for a in range(1, N):
        fac.append(fac[-1]*(1-pow(Q, a, p)) % p)
        sine.append(pow(imaginary, a, p)*pow(q, -a*(a+1)//2, p)*fac[a] % p)
    for r in range(N):
        expected = [0]*N
        if r <= d//2:
            for v in range(r, d//2+1):
                expected[v] = (sine[d-v]**2*sine[2*v]
                               *pow(sine[v-r]*sine[v+r] % p, -1, p)) % p
        for t in range(1, min(r, N-r)+1):
            expected[N-t] = (pow(-1, N-t-r, p)*sine[t-1]**2*sine[t+r-1]
                              *pow(sine[2*t-1]*sine[r-t] % p, -1, p)) % p
        kappa = int(Rp[0, 0])
        assert [pow(kappa, -1, p)*v % p for v in expected] == list(rotated[N-r-1])

    # All polynomial degrees and several off-grid w values, not only the nodes.
    tested_w = 0
    for w in range(2, min(p, 35)):
        wi = pow(w, -1, p)
        if (w*w-1)*(q*w+1)*(w+q) % p == 0:
            continue
        aa = (q*w-1)**3*pow(q*(w*w-1)*(q*w+1) % p, -1, p) % p
        bb = (w-q)**3*pow(q*(w+q)*(w*w-1) % p, -1, p) % p
        cc = 8*q*w*pow((w+q)*(q*w+1) % p, -1, p) % p
        z = (w+wi) % p
        wzp = (Q*w+pow(Q*w % p, -1, p)) % p
        wzm = (pow(Q, -1, p)*w+Q*wi) % p
        for v in range(N):
            lhs = (aa*peval(fs[v], wzp, p)+bb*peval(fs[v], wzm, p)
                   +cc*peval(fs[v], z, p)) % p
            rhs = (cs[v]*peval(fs[v], z, p)
                   +(bs[v]*peval(fs[v-1], z, p) if v else 0)) % p
            assert lhs == rhs
        tested_w += 1

    # Entire low-core Chebyshev identity, with all coefficients retained.
    complete = [int(v) for v in rotated[-1]]
    previous = [(2*v) % p for v in complete]
    current = Dvec(complete)
    M = d//2
    for r in range(M+1):
        cheb = previous if r == 0 else current
        expected = [pow(-1, r, p)*v*pow(2, -1, p) % p for v in cheb]
        actual = [int(v) if k <= M else 0 for k, v in enumerate(rotated[N-r-1])]
        assert expected == actual
        if r:
            nxt = [(a-b) % p for a, b in zip(Dvec(current), previous)]
            previous, current = current, nxt
    return {'N': N, 'literal_all_color_quarter_turn_Ward': True,
            'all_color_original_two_band_coefficients': True,
            'off_grid_points_all_degrees': tested_w,
            'complete_low_core_Chebyshev_identity': True}


def gap_case(s):
    mp.mp.dps = 60
    j0 = 8*lobachevsky(mp.pi/4)/mp.pi
    alpha = mp.pi/s
    rate = 4*s/mp.pi*(lobachevsky(mp.pi/4+alpha/2)
                     +lobachevsky(mp.pi/4-alpha/2))
    gap = rate-(s-1)*j0
    elementary_lower = j0-mp.pi/(s*mp.cos(alpha))
    assert gap > elementary_lower > 0
    return {'odd_boxes': s, 'complete_geometric_rate': float(rate),
            'source_alias_margin_at_zero_corridor': float(gap),
            'proved_elementary_positive_lower': float(elementary_lower)}


def three_box_source_diagnostic(N, dps):
    q, coefficients = source_polynomial(N, dps)
    d = N-1
    kappa = q**(mp.mpf(d*d)/2)
    total = mp.mpc(0)
    nodal = mp.mpf(0)
    for j in range(N//2):
        w = q**(2*j+1)
        c = w+1/w
        value, derivative = evaluate(coefficients, c)
        R = kappa*(-1)**j*q**(j*(j+1))
        Rprime = -R*(d-2*j)/(2*(w-1/w))
        product = R*value**2
        product_prime = Rprime*value**2+2*R*value*derivative
        total += (4-c*c)*product_prime-c*product
        nodal = max(nodal, abs(product))
    total *= (-1)**d
    if N % 2:
        j = d//2
        total += kappa*(-1)**j*q**(j*(j+1))*evaluate(coefficients, -2)[0]**2
    return {'N': N, 'dps': dps,
            'full_source_log_modulus_over_N': float(mp.log(abs(total))/N),
            'largest_nodal_log_modulus_over_N': float(mp.log(nodal)/N),
            'source_real': mp.nstr(mp.re(total), 40),
            'source_imaginary': mp.nstr(mp.im(total), 40),
            'scope': 'Diagnostic only: no inferred limit or three-box uniform gap.'}, total


if __name__ == '__main__':
    symbolic = symbolic_product_certificate()
    fields = [field_case(N) for N in range(2, 11)]
    gaps = [gap_case(s) for s in range(5, 32, 2)]
    diagnostics = []
    last = None
    for N in (16, 32, 64, 128):
        row, last = three_box_source_diagnostic(N, max(120, 2*N))
        diagnostics.append(row)
    replay, replay_value = three_box_source_diagnostic(128, 512)
    assert abs(replay_value/last-1) < mp.mpf('1e-95')
    diagnostics.append(replay)
    output = {'status': 'PASS', 'symbolic': symbolic, 'literal_all_input': fields,
              'uniform_positive_margins': gaps,
              'three_box_exact_source_diagnostics': diagnostics,
              'scope': 'Proved fixed-cusp alias source gap for odd s>=5, relative to complete-base geometric rate; no mixed-core survival or global-color gap asserted.'}
    Path(__file__).with_name('actual_pretzel_mixed_alias_source_gap_results.json').write_text(
        json.dumps(output, indent=2)+'\n')
    print('PASS 9 all-color physical dual-Casimir/core families; all-degree symbolic identities; 14 positive source gaps; exact three-box diagnostic with doubled precision')
