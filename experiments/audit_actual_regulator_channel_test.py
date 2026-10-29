#!/usr/bin/env python3
"""Actual regular 4_1 affine A connection: CP/polar/regulator test."""

import json
from pathlib import Path

import mpmath as mp
import sympy as sp

from audit_actual_regulator_weighted_a_transfer import coeff, eig


def exact():
    Q, Y, L = sp.symbols('Q Y L', nonzero=True)
    g = Q**2*Y**2-Q*Y**4+Q*Y**3+Q*Y-Q+Y**2
    cm = Y**2*(Q-Y)*(Q*Y**2-1)
    c0 = -(Y-1)**2*(Y+1)*g
    cp = Y**2*(Q*Y-1)*(Q-Y**2)
    source = Y*(Y+1)*(Q-Y**2)*(Q*Y**2-1)/cp
    for z in [-c0/cp, -cm/cp, source]:
        assert sp.factor(z-z.subs({Q: 1/Q, Y: 1/Y}, simultaneous=True)) == 0
    P = Y**2+Y**-2-Y-Y**-1-2
    aa, pd = Y/(Y**2-1), Y*sp.diff(P, Y)
    V = sp.Matrix([[L, 1/L], [1, 1]])
    ld = pd*L**2/(L**2-1)
    Vdot = sp.Matrix([[ld, -ld/L**2], [0, 0]])
    B = V.inv()*sp.Matrix([[-aa*(L+1/L), 2*aa], [0, 0]])*V-V.inv()*Vdot*sp.diag(L, 1/L)
    lam, s = -2-sp.sqrt(3), sp.sqrt(3)
    E0 = sp.simplify((sp.I*sp.diag(1/L, L)*B).subs({Y: sp.I, L: lam}))
    ratio = -lam
    ltheta = 2*lam**2/(lam**2-1)
    dn1 = -lam*ltheta/(lam**2+1)
    dn2 = ltheta/lam+dn1
    E = sp.simplify(sp.diag(1, ratio).inv()*E0*sp.diag(1, ratio)-sp.diag(dn1, dn2))
    target = sp.Matrix([[-sp.Rational(5, 12), (s-1)/6],
                        [-(s+1)/6, -sp.Rational(5, 12)]])
    assert all(sp.simplify(x) == 0 for x in E-target)
    skew = sp.simplify((E-E.T)/2)
    assert skew == sp.Matrix([[0, s/6], [-s/6, 0]])
    assert sp.simplify((E+E.T)[0, 1]) == -sp.Rational(1, 3)
    return {'normalized_connection_generator': str(E),
            'exact_unit_circle_reality': True,
            'polar_rotation_generator': str(skew)}


def normalized_frame(Y):
    L, V = eig(Y)
    n1 = 1/mp.sqrt(abs(L)**2+1)
    n2 = 1/mp.sqrt(abs(1/L)**2+1)
    return L, V*mp.diag([n1, n2])


def finite(N, sign):
    tau = 2*mp.pi/N
    Q, Y = mp.exp(1j*tau), sign*mp.j
    T, f = coeff(Q, Y)
    lam, S = normalized_frame(Y)
    _, Snext = normalized_frame(Q*Y)
    Lambda = mp.diag([lam, 1/lam])
    C = Lambda**-1*Snext**-1*T*S
    source = Snext**-1*f
    E = sign*mp.matrix([[-mp.mpf(5)/12, (mp.sqrt(3)-1)/6],
                        [-(mp.sqrt(3)+1)/6, -mp.mpf(5)/12]])
    error = mp.norm((C-mp.eye(2))/tau-E)
    assert N*error < 100
    gram = C.H*C
    # A common scalar cannot remove this off-diagonal Gram entry.
    if N >= 256:
        assert abs(gram[0, 1])/tau > mp.mpf('.12')
    U = C*(mp.sqrtm(gram)**-1)
    assert mp.norm(U.H*U-mp.eye(2)) < mp.mpf('1e-60')
    assert N*abs(U[0, 1]/tau-sign*mp.sqrt(3)/6) < 50
    R = mp.diag([1, -1])
    defect = U.H*R*U-R
    assert N*abs(defect[0, 1]/tau-sign*mp.sqrt(3)/3) < 50
    if N >= 256:
        assert abs(defect[0, 1])/tau > mp.mpf('.2')
    assert min(abs(source[0]), abs(source[1])) > mp.mpf('.1')
    J = mp.matrix([[0, mp.j], [-mp.j, 0]])
    assert mp.norm(T.H*J*T-mp.det(T)*J) < mp.mpf('1e-60')
    assert mp.norm(U.H*J*U-J) < mp.mpf('1e-60')
    real_vector = mp.matrix([mp.mpf('.7'), mp.mpf('-.4')])
    assert abs((real_vector.H*J*real_vector)[0]) < mp.mpf('1e-60')
    return {'N': N, 'Y': 'i' if sign > 0 else '-i',
            'actual_color_fraction': '.25' if sign > 0 else '.75',
            'normalized_generator_error': mp.nstr(error, 10),
            'polar_mix_per_tau': mp.nstr(mp.re(U[0, 1]/tau), 18),
            'regulator_defect_per_tau': mp.nstr(mp.re(defect[0, 1]/tau), 18),
            'source_both_channels_nonzero': True,
            'exact_indefinite_flux': True}


def main():
    mp.mp.dps = 80
    result = {'status': 'PASS', 'exact': exact(),
              'actual_packets': [finite(N, sign) for N in [32, 64, 128, 256, 512, 1024, 2048]
                                 for sign in [1, -1]],
              'scope': ('Actual regular instantaneous classical eigenframe only; '
                        'does not exclude superadiabatic or global original-source transport.')}
    Path(__file__).with_name('actual_regulator_channel_test_results.json').write_text(
        json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
