#!/usr/bin/env python3
"""Full physical CD Kraus factorization and original pretzel source.

All ports remain open in the tested box identity. Full-network tests use
the unrestricted original marked cap and actual cup matching directly.
An exact N=3 test independently reconstructs the half-twist certificate.
"""

import itertools
import json
from pathlib import Path

import numpy as np
import sympy as sy

from audit_actual_half_clock_source_dilation import generators, original_factorial_R


def close(a, b, label, tol=2e-7):
    error = float(np.max(np.abs(np.asarray(a)-np.asarray(b))))
    scale = max(1., float(np.max(np.abs(np.asarray(b)))))
    assert error < tol*scale, (label, error, scale)


def physical_data(N):
    q, Q, x, _, K, E, F, _ = generators(N, 1)
    d, I, rho = N-1, np.eye(N), q-1/q
    Et = np.kron(E*rho*rho, K)+np.kron(I, E*rho*rho)
    Ft = np.kron(F, I)+np.kron(np.linalg.inv(K), F)
    Kt = np.kron(K, K)
    O = Ft@Et+q*Kt+1/q*np.linalg.inv(Kt)
    a, b = np.eye(N*N), O.copy()
    for _ in range(2, N):
        a, b = b, O@b-a
    L = (-1)**d*b
    P = np.zeros((N*N, N*N), complex)
    for u, v in itertools.product(range(N), repeat=2):
        P[v*N+u, u*N+v] = 1
    H = L@P
    R = original_factorial_R(N)
    kappa = q**(d*d/2)
    s = [1.]
    for j in range(1, N):
        s.append(s[-1]*abs(1-Q**j))
    columns, phases, labels = [], [], []
    for T in range(2*d+1):
        low = min(T, 2*d-T)
        offset = max(0, T-d)
        ids = [(offset+u)*N+T-offset-u for u in range(low+1)]
        J = O[np.ix_(ids, ids)]
        for j in range(low+1):
            partner = d-j
            if j > partner or partner > low:
                continue
            c = q**(2*j+1)+q**(-2*j-1)
            v = np.zeros(low+1, complex)
            v[0] = 1
            if low:
                v[1] = (c-J[0, 0])/J[0, 1]
            for u in range(1, low):
                v[u+1] = ((c-J[u, u])*v[u]-J[u, u-1]*v[u-1])/J[u, u+1]
            h = (2*s[low]**2/(s[low-j]*s[low+j-d]) if j < partner
                 else s[low]**2/s[low-j]**2)
            col = np.zeros(N*N, complex)
            col[ids] = np.sqrt(h)*v
            nu = (-1)**j*q**(j*(j+1))
            close(R@col, kappa*nu*col, 'actual R on each full physical CD image')
            columns.append(col)
            phases.append(kappa*nu)
            labels.append((T, j))
    C = np.array(columns).T
    phases = np.array(phases)
    close(C@C.conj().T, H, 'full CD positive factor')
    for e in (-3, -1, 0, 1, 2):
        close(np.linalg.matrix_power(R, e)@L,
              (C*phases**e)@C.conj().T@P, 'all-input coherent box factor')
    return {'N': N, 'original_pair_dimension': N*N, 'CD_image_dimension': C.shape[1],
            'all_degree_CD_and_all_input_signed_box_factor': True}, (q, Q, x, R, L, P, C, phases)


def apply_boxes(matrices, tensor):
    value = tensor
    for axis, matrix in enumerate(matrices):
        value = np.moveaxis(np.tensordot(matrix, value, axes=(1, axis)), 0, axis)
    return value


def source_case(N, s, powers, data):
    q, Q, x, R, L, P, C, phases = data
    d, rank = N-1, C.shape[1]
    shape = [N]*(2*s)
    p = np.zeros(shape, complex)
    for colors in itertools.product(range(N), repeat=s):
        indices = [0]*(2*s)
        indices[0], indices[-1] = colors[0], d-colors[0]
        for t in range(1, s):
            indices[2*t-1], indices[2*t] = colors[t], d-colors[t]
        second = [2*s-1]+list(range(2, 2*s-1, 2))
        p[tuple(indices)] = N**s*x**(-sum(indices[j] for j in second))
    row = np.zeros(shape, complex)
    for indices in np.ndindex(*shape):
        if all(indices[2*t-1]+indices[2*t] == d for t in range(1, s)):
            row[indices] = (x**(indices[-1]+sum(indices[2*t-1] for t in range(1, s)))
                            /N**(s+1))
    box_order, ordinary_order = list(range(2*s)), list(range(2*s))
    for t in range(s):
        box_order[2*t:2*t+2] = [2*t+1, 2*t]
    for t in range(1, s):
        ordinary_order[2*t-1:2*t+1] = [2*t, 2*t-1]
    p_box = p.transpose(box_order).reshape([N*N]*s)
    p_ordinary = p.transpose(ordinary_order).reshape([N*N]*s)
    u = apply_boxes([C.conj().T]*s, p_box)
    v = apply_boxes([C.conj().T]*s, p_ordinary)
    phase = np.ones([rank]*s, complex)
    for t, e in enumerate(powers):
        axis_shape = [1]*s
        axis_shape[t] = rank
        phase *= (phases**e).reshape(axis_shape)
    coherent = N**(-2*s-1)*np.vdot(v, phase*u)
    literal = apply_boxes([np.linalg.matrix_power(R, e)@L for e in powers],
                          p.reshape([N*N]*s)).reshape(shape)
    original = np.sum(row*literal)
    close(original, coherent, 'original unrestricted marked source vs coherent packet')
    top_from_cup = np.conj(p_ordinary.reshape(shape))/N**(2*s+1)
    # Actual total-degree restriction, without local marked replacement.
    for indices in np.ndindex(*shape):
        if sum(indices) == s*d:
            close(row[indices], top_from_cup[indices], 'whole original marked-degree row')
    energy_u, energy_v = float(np.vdot(u, u).real), float(np.vdot(v, v).real)
    bound = N**(-4*s-2)*energy_u*energy_v
    assert abs(original)**2 <= bound+1e-6*max(1, bound)
    return {'N': N, 'boxes': s, 'signed_half_twist_powers': list(powers),
            'raw_scalar_real': float(original.real), 'raw_scalar_imag': float(original.imag),
            'original_marked_source_exact': True, 'coherent_positive_Cauchy_bound': bound,
            'norm_u_squared': energy_u, 'norm_v_squared': energy_v}


def exact_three():
    N, d = 3, 2
    z = sy.sqrt(3)*sy.I
    q = (1+z)/2
    Q, x, kappa = sy.expand(q*q), sy.expand(q*q), sy.expand(q*q)
    simplify = lambda t: sy.simplify(sy.expand_complex(t))
    f = [sy.Integer(1)]
    for a in range(1, N):
        f.append(simplify(f[-1]*(1-Q**a)))
    E, F = sy.zeros(N), sy.zeros(N)
    K = sy.diag(*[simplify(x*Q**(-a)) for a in range(N)])
    for a in range(1, N):
        E[a-1, a] = simplify(Q**(-a)-1)
        F[a, a-1] = simplify(1-Q**a)
    I = sy.eye(N)
    Et = sy.kronecker_product(E, K)+sy.kronecker_product(I, E)
    Ft = sy.kronecker_product(F, I)+sy.kronecker_product(K.inv(), F)
    Kt = sy.kronecker_product(K, K)
    O = (Ft*Et+q*Kt+Kt.inv()/q).applyfunc(simplify)
    L = (O*O-sy.eye(N*N)).applyfunc(simplify)
    R = sy.zeros(N*N)
    for a, b in itertools.product(range(N), repeat=2):
        for k in range(min(a, d-b)+1):
            R[(b+k)*N+a-k, a*N+b] = simplify(
                kappa*x**(-a-b+k)*Q**(b*(a-k))*f[b+k]*f[a]
                /(f[k]*f[b]*f[a-k]))
    values = {}
    for name, B in [('retained_half_twist', (R.inv()*L).applyfunc(simplify)),
                    ('genuinely_untwisted', L)]:
        total = 0
        for h in range(-d, d+1):
            ids = list(range(max(0, h), min(d, d+h)+1))
            M = sy.Matrix([[simplify(x**(-2*a+h)*B[(a-h)*N+d-ap+h, a*N+d-ap])
                            for ap in ids] for a in ids])
            D = sy.diag(*[simplify(x**(2*a)) for a in ids])
            total += sy.trace(D*M**3)
        values[name] = simplify(x**(2*d)*total/N)
    assert simplify(values['retained_half_twist']-(-189+81*z)) == 0
    assert values['genuinely_untwisted'] == 270
    ratio = simplify(values['retained_half_twist']/sy.conjugate(values['retained_half_twist']))
    assert simplify(ratio-(11-21*z)/38) == 0
    assert simplify(ratio+sy.conjugate(ratio)) == sy.Rational(11, 19)

    # A separate UNTWiSTED check of the actual two boundary packets.  Compute
    # their Gram directly from H=L P, without choosing or fitting CD columns.
    # The quadratic-field domain keeps every original cup phase exact.
    flip = sy.zeros(N*N)
    for a, b in itertools.product(range(N), repeat=2):
        flip[b*N+a, a*N+b] = 1
    H = (L*flip).applyfunc(simplify)
    field = sy.QQ.algebraic_field(z)
    exact = lambda a: field.from_sympy(simplify(a))
    h = [[exact(H[a, b]) for b in range(N*N)] for a in range(N*N)]
    states = []
    for a, b, c in itertools.product(range(N), repeat=3):
        ports = [a, b, d-b, c, d-c, d-a]
        amplitude = exact(N**3*x**(-sum(ports[j] for j in (5, 2, 4))))
        conjugate = exact(sy.conjugate(N**3*x**(-sum(ports[j] for j in (5, 2, 4)))))
        box = [ports[j] for j in (1, 0, 3, 2, 5, 4)]
        ordinary = [ports[j] for j in (0, 2, 1, 4, 3, 5)]
        states.append((amplitude, conjugate,
                       [box[2*j]*N+box[2*j+1] for j in range(3)],
                       [ordinary[2*j]*N+ordinary[2*j+1] for j in range(3)]))
    gram = [[field.zero for _ in range(2)] for _ in range(2)]
    for left in states:
        for right in states:
            for row in range(2):
                for col in range(2):
                    term = left[1]*right[0]
                    for box in range(3):
                        term *= h[left[2+row][box]][right[2+col][box]]
                    gram[row][col] += term
    gram = sy.Matrix([[field.to_sympy(a) for a in row] for row in gram])
    assert gram == 3**10*sy.Matrix([[18, 10], [10, 119]])
    assert gram.det() == 2042*3**20
    assert gram[1, 0]/3**7 == values['genuinely_untwisted']
    return {'N': 3, 'odd_boxes': 3, 'exact_original_half_twisted_scalar': str(values['retained_half_twist']),
            'exact_genuinely_untwisted_scalar': '270',
            'nonintegral_rational_trace_of_scalar_phase_ratio': '11/19',
            'no_unit_root_phase_can_make_the_half_twisted_scalar_real': True,
            'untwisted_actual_packet_Gram': '3^10 [[18,10],[10,119]]',
            'untwisted_packet_Gram_determinant': '2042*3^20',
            'untwisted_original_source_is_neither_canonical_packet_norm': True}


if __name__ == '__main__':
    frames, data = [], {}
    for N in range(2, 8):
        record, data[N] = physical_data(N)
        frames.append(record)
    sources = [source_case(N, 3, powers, data[N]) for N in range(2, 6)
               for powers in ((-1, -1, -1), (0, 0, 0), (-1, 0, 2))]
    sources += [source_case(N, 5, (-1,)*5, data[N]) for N in (2, 3)]
    results = {'status': 'PASS', 'full_physical_CD_Kraus_boxes': frames,
               'complete_original_pretzel_sources': sources,
               'exact_original_level_three_certificate': exact_three(),
               'scope': 'All-exterior box factor and arbitrary-width marked-source Cauchy theorem; no sharp geometric energy or general untwisted reflection theorem.'}
    Path(__file__).with_name('actual_pretzel_circle_coherent_reflection_results.json').write_text(
        json.dumps(results, indent=2)+'\n')
    print('PASS 6 full physical Kraus frames; 14 complete original marked sources; exact N=3 half-twist phase and untwisted quotient-Gram certificates')
