#!/usr/bin/env python3
"""Literal mixed-R longitude, full Cartan density, pivot spin and disk word."""

import json
from pathlib import Path

import numpy as np
import sympy as sp
from sympy.combinatorics.free_groups import free_group

from audit_actual_two_cut_ports import balanced_data
from audit_actual_crossing_circle_source_and_filling import ordinary_module, mixed_check


def factorials(N, Q, p):
    out = [1]
    for a in range(1, N):
        out.append(out[-1]*(1-pow(Q, a, p)) % p)
    return out


def coefficient(alpha, beta, a, b, k, N, eta, q, p):
    Q, x1, x2 = q*q % p, pow(q, alpha, p), pow(q, beta, p)
    F = factorials(N, Q, p)
    poch = 1
    for t in range(k):
        poch = poch*(1-pow(Q, 1-a+t, p)*x1*x1) % p
    return (pow(eta, alpha*beta, p)*pow(-1, k, p)*pow(q, k*k-k, p)
            *pow(x1, -b-2*k, p)*pow(x2, -a+k, p)
            *pow(Q, (a-k)*(b+k), p)*F[b+k]
            *pow(F[b]*F[k] % p, -1, p)*poch) % p


def balanced_ordinary(j, q, N, p):
    A = ordinary_module(j, q, p)
    fac = factorials(N, q*q % p, p)[:j]
    frame = np.array(fac, dtype=np.int64)[:, None]*np.array(
        [pow(a, -1, p) for a in fac], dtype=np.int64)[None, :] % p
    return dict(A, E=A['E']*frame % p, F=A['F']*frame % p)


def quantum_case(N):
    p, eta, q, E, F, K, pivot, Rp, Rm = balanced_data(N)
    d, Q = N-1, q*q % p
    target = {'dim': N, 'E': E, 'F': F, 'K': K, 'H': [d-2*a for a in range(N)]}
    literal_count = color_count = path_count = 0
    for j in range(1, N+1):
        auxiliary = balanced_ordinary(j, q, N, p)
        for A, B, alpha, beta in ((target, auxiliary, d, j-1),
                                 (auxiliary, target, j-1, d)):
            literal = mixed_check(A, B, q, eta, p)
            for a in range(A['dim']):
                for b in range(B['dim']):
                    for k in range(min(a, B['dim']-1-b)+1):
                        r = coefficient(alpha, beta, a, b, k, N, eta, q, p)
                        assert literal[(b+k)*A['dim']+a-k, a*B['dim']+b] == r
                        literal_count += 1
        if j == N:
            continue
        # Two INDEPENDENT ordinary color shifts, including zero coefficients.
        for a in range(j):
            for b in range(N):
                for k in range(min(a, N-1-b)+1):
                    r = coefficient(j-1, d, a, b, k, N, eta, q, p)
                    rs = coefficient(j, d, a, b, k, N, eta, q, p)
                    z, C, BC = pow(Q, j-a, p), pow(Q, k, p), pow(Q, b+k, p)
                    root = pow(eta, -(d-2*b), p)
                    assert ((1-z)*rs-root*pow(q, d, p)*pow(BC, -1, p)*(1-z*C)*r) % p == 0
                    color_count += 1
        for a in range(N):
            for b in range(j):
                for k in range(min(a, j-1-b)+1):
                    r = coefficient(d, j-1, a, b, k, N, eta, q, p)
                    rs = coefficient(d, j, a, b, k, N, eta, q, p)
                    assert (rs-pow(eta, d-2*(a-k), p)*r) % p == 0
                    color_count += 1
        if N > 6:
            continue
        for a in range(N):
            for b in range(N):
                for t in range(j):
                    for k1 in range(min(b, j-1-t)+1):
                        for k2 in range(min(a, j-1-t-k1)+1):
                            for k3 in range(k1+k2+1):
                                k4 = k1+k2-k3
                                if a-k2+k3 >= N or b-k1+k4 >= N:
                                    continue
                                ports = ((d, j-1, b, t, k1),
                                         (d, j-1, a, t+k1, k2),
                                         (j-1, d, t+k1+k2, a-k2, k3),
                                         (j-1, d, t+k1+k2-k3, b-k1, k4))
                                before = pow(q, (j-1-2*t)*(1-N), p)
                                shifted = pow(q, (j-2*t)*(1-N), p)
                                for alpha, beta, u, v, k in ports:
                                    before = before*coefficient(alpha, beta, u, v, k, N, eta, q, p) % p
                                for ix, (alpha, beta, u, v, k) in enumerate(ports):
                                    shifted = shifted*coefficient(alpha+(ix >= 2), beta+(ix < 2),
                                                                    u, v, k, N, eta, q, p) % p
                                lhs, rhs = shifted, before*pow(q, 1-N, p) % p
                                for alpha, beta, u, v, k in ports[2:]:
                                    z, C = pow(Q, 1+alpha-u, p), pow(Q, k, p)
                                    tau0 = pow(Q, v+k, p)*pow(q, -beta, p) % p
                                    lhs = lhs*tau0*(1-z) % p
                                    rhs = rhs*(1-z*C) % p
                                assert lhs == rhs
                                path_count += 1
    return {'N': N, 'literal_full_Cartan_coefficients': literal_count,
            'independent_color_contiguities': color_count,
            'closed_typed_loop_common_paths_with_actual_pivot': path_count}


def symbolic_transport():
    A, B, p1, p2, x1, x2 = sp.symbols('A B p1 p2 x1 x2', nonzero=True)
    z = (x1/A, (1/x1-x1/A)*p1, (1-A)/p1)
    w = (x2/B, (1/x2-x2/B)*p2, (1-B)/p2)
    def crossing(z, w, sign):
        K,e,f = z
        L,g,h = w
        if sign > 0:
            d = 1-e*h
            return ((L*d,(d*g+e*(d*L-1/L))/K,K*h/d),
                    (K/d,e/(L*d),L*(d*f+h*(d/K-K))))
        c = 1-K*g*f/L
        return ((L*c,K*g,f+h/K-f/(L*L*c)),
                (K/c,L*e+g-K*K*g/c,f/L))
    lower = lambda z: sp.Matrix([[1,0],[-z[0]*z[2],z[0]]])
    G = lambda z: sp.Matrix([[z[0],z[1]],[z[0]*z[2],1/z[0]+z[1]*z[2]]])
    vector = lambda z,x: sp.Matrix([z[1]/(1/x-z[0]),1])
    v1, v2 = vector(z,x1), lower(z).inv()*vector(w,x2)
    H1,H2 = G(z),lower(z).inv()*G(w)*lower(z)
    assert (H1*v1-v1/x1).applyfunc(sp.factor) == sp.zeros(2,1)
    assert (H2*v2-v2/x2).applyfunc(sp.factor) == sp.zeros(2,1)
    for sign in (1,-1):
        zp,wp = crossing(z,w,sign)
        out1,out2 = vector(zp,x2),lower(zp).inv()*vector(wp,x1)
        if sign > 0:
            tau = 1/(w[0]*(1-p1*w[2]/x1))
            differences = (out1-H1.inv()*v2,out2-tau*v1)
        else:
            tau = z[0]/(1+z[0]*z[2]*p2)
            differences = (out1-tau*v2,out2-H2*v1)
        assert all(v.applyfunc(sp.factor) == sp.zeros(2,1) for v in differences)
    return {'unequal_meridian_colors_retained': True,
            'positive_and_negative_flag_transport': True,
            'cut_flag_is_M_inverse_positive_flag_is_dual': True}


def disk_word():
    group,A,B,C = free_group('A B C')
    state = [A,B,C]
    roles = []
    labels = ['A','B','C']
    under_word = group.identity
    self_writhe = 0
    for slot in (1,0,0,1):
        over,under = state[slot:slot+2]
        if labels[slot+1] == 'C':
            roles.append('under')
            under_word = over**-1*under_word
        elif labels[slot] == 'C':
            roles.append('over')
        if labels[slot] == labels[slot+1] == 'C':
            self_writhe += 1
        state[slot:slot+2] = [over**-1*under*over,over]
        labels[slot],labels[slot+1] = labels[slot+1],labels[slot]
    P = B*A
    assert state[2] == P**-1*C*P
    assert state[0] == state[2]**-1*A*state[2]
    assert state[1] == state[2]**-1*B*state[2]
    assert under_word == P**-1
    assert roles == ['under','under','over','over'] and self_writhe == 0
    return {'chronological_loop': [2,1,1,2], 'auxiliary_roles': roles,
            'auxiliary_self_writhe': self_writhe, 'preferred_disk_word': str(P),
            'under_vector_transport_is_inverse_preferred_word': True}


def regulator_algebra():
    x,y,a,b,Gim,p,m = sp.symbols('x y a b Gim p m',real=True)
    z,l = x+sp.I*y,a+sp.I*b
    u,v = -z/2,sp.pi*sp.I-l
    marked = sp.simplify(sp.im(Gim*sp.I-sp.pi*sp.I*z)-2*sp.re(u)*sp.im(v))
    assert sp.simplify(marked-(Gim-x*b)) == 0
    critical_z = 2*sp.pi*sp.I*m-2*p*l
    filled = sp.simplify(sp.im(Gim*sp.I+(critical_z-2*sp.pi*sp.I*m)**2/(4*p)))
    assert sp.simplify(filled-(Gim-sp.re(critical_z)*b)) == 0
    dx,dy,da,db = sp.symbols('dx dy da db',real=True)
    geometric_differential = 2*(sp.re(v)*(-dy/2)-sp.re(u)*(-db))
    assert sp.simplify(geometric_differential-(a*dy-x*db)) == 0
    zz,ll,pp,mm,GG = sp.symbols('zz ll pp mm GG',nonzero=True)
    chi,frequency = zz/(2*sp.I),-ll/(2*sp.pi*sp.I)
    action = GG/(2*sp.pi*sp.I)+2*sp.I*chi*frequency-2*sp.pi*sp.I*(pp*frequency**2+mm*frequency)
    difference = (2*sp.pi*sp.I*action-GG-pp*ll**2).subs(zz,2*sp.pi*sp.I*mm-2*pp*ll)
    assert sp.factor(difference) == 0
    return {'preferred_spin_regulator_cancels_exactly': True,
            'filled_stationary_action_is_marked_regulator': True,
            'preferred_boundary_differential_with_half_step_factor_two': True,
            'actual_Fourier_source_action_equals_chirp_action': True}


if __name__ == '__main__':
    quantum = [quantum_case(N) for N in range(2,8)]
    symbolic = symbolic_transport()
    word = disk_word()
    regulator = regulator_algebra()
    result = {'status':'PASS','literal_mixed_R_and_closing_sources':quantum,
              'independent_mixed_vector_transport':symbolic,'actual_disk_word':word,
              'spin_and_filling_regulator':regulator,
              'scope':'Actual local peripheral/framing certificate; geometric branch lift and regulator identification use their separately proved source hypotheses.'}
    Path(__file__).with_name('actual_mixed_crossing_circle_preferred_longitude_results.json').write_text(
        json.dumps(result,indent=2)+'\n')
    print(f'PASS {len(quantum)} original mixed-color levels; full unequal-color vector transport; literal disk word and marked-spin regulator')
