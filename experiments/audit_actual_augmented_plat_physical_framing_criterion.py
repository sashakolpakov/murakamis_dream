#!/usr/bin/env python3
"""Exact framing identities plus finite argument-regression checks.

This does not search for or assert a favorable frame for any whole plat.
"""
from __future__ import annotations

import cmath
import json
import math
import random
from pathlib import Path

import sympy as sp


def cross(a: complex, b: complex) -> int:
    return int(a.real * b.imag - a.imag * b.real)


def dot(a: complex, b: complex) -> int:
    return int(a.real * b.real + a.imag * b.imag)


def origin_in_triangle(a: complex, b: complex, c: complex) -> bool:
    den = cross(b - a, c - a)
    if den:
        nums = (cross(b, c), cross(c, a), cross(a, b))
        return all(n * den >= 0 for n in nums)
    return any(cross(x, y) == 0 and dot(x, y) <= 0
               for x, y in ((a, b), (b, c), (c, a)))


def central_exact(a: complex, b: complex, c: complex) -> bool:
    """Sign of |c| Re(b conj(a))+|a| Re(b conj(c)), exactly."""
    if cross(a, c) == 0:
        return False
    q, r = dot(b, a), dot(b, c)
    aa, cc = dot(a, a), dot(c, c)
    if q >= 0 and r >= 0:
        return q > 0 or r > 0
    if q <= 0 and r <= 0:
        return False
    if q > 0:
        return cc * q * q > aa * r * r
    return aa * r * r > cc * q * q


def arg_0_2pi(z: complex) -> float:
    return cmath.phase(z) % (2 * math.pi)


def physical_arguments(a: complex, b: complex, c: complex):
    x1, x2 = -a / b, -b / c
    r1, r2 = arg_0_2pi(x1) / (2 * math.pi), arg_0_2pi(x2) / (2 * math.pi)
    s = r1 + r2
    if s < 1:
        tau, u = s, r1
    else:
        tau, u = 2 - s, 1 - r2
    # Exact boundary classification is checked separately; floating comparisons
    # are used only for arguments a fixed distance from a boundary.
    support = (0 < r1 < 1 and 0 < r2 < 1 and .5 < tau < 1 and 0 < u < tau)
    central = support and abs(2 * u - tau) < .5
    margins = [r1, 1-r1, r2, 1-r2, abs(tau-.5), abs(tau-1),
               abs(u), abs(u-tau), abs(abs(2*u-tau)-.5)]
    return support, central, min(margins), (r1, r2, tau, u)


def symbolic_identities():
    r0, r1, r2 = sp.symbols('r0 r1 r2', real=True)
    identity = sp.eye(2)
    A = -sp.Matrix([[1, 1], [0, 1]])
    B = -sp.Matrix([[1, 0], [-4, 1]])
    P = B*A
    assert A.trace() == B.trace() == P.trace() == -2
    pencil = r0*identity+r1*A+r2*P
    assert sp.expand(pencil.det()-(2*(r0*r0+r1*r1+r2*r2)-(r0+r1+r2)**2)) == 0
    assert sp.Matrix.hstack(*[m.reshape(4, 1) for m in (identity, A, P)]).rank() == 3

    z, w = sp.symbols('z w')
    v = sp.Matrix([z, 1])
    ell = sp.Matrix([[1, -w]])/(z-w)
    pi = v*ell
    assert sp.simplify(pi*pi-pi) == sp.zeros(2)
    assert sp.simplify(pi.trace()) == 1 and sp.simplify(pi.det()) == 0
    q00, q01, q10, q11 = sp.symbols('q00 q01 q10 q11')
    Q = sp.Matrix([[q00,q01],[q10,q11]])
    assert sp.simplify((Q*pi).trace()-(ell*Q*v)[0]) == 0

    p0 = pi.subs({z: sp.I, w: -sp.I})
    aa = [(m*p0).trace().expand() for m in (identity,A,P)]
    assert aa == [1, -1+sp.I/2, -1-5*sp.I/2]
    assert sp.expand(aa[0]/2+5*aa[1]/12+aa[2]/12) == 0
    assert sp.expand(aa[0]*aa[1]+aa[1]*aa[2]+aa[0]*aa[2]) == sp.Rational(1,4)
    assert sp.expand(aa[0]+aa[2]+4*aa[1]) == -4-sp.I/2

    x,y = sp.symbols('x y')
    assert sp.expand((x+y)-2*x-(y-x)) == 0
    assert sp.expand((2-x-y)-2*(1-y)-(y-x)) == 0

    h,beta=sp.symbols('h beta', real=True)
    av=(h*h-1)/2
    L=sp.Matrix([[1+av/2+sp.I*h/2,(av-1)/4+sp.I*h/2],
                 [-av-1,-av/2-sp.I*h/2]])
    H=P+identity
    assert sp.simplify(L*L-L) == sp.zeros(2)
    assert sp.simplify(L.trace()) == 1
    assert sp.simplify((P*L).trace()) == 1
    assert sp.simplify((A*L).trace()) == av
    assert sp.simplify(((H*A-A*H)*L).trace()) == -4*sp.I*h
    transported=(identity+beta*H)*A*(identity-beta*H)
    assert sp.simplify((transported*L).trace()-(av-4*sp.I*beta*h-8*beta*beta)) == 0
    return identity,A,P


def real_and_imag(z):
    return [sp.simplify(sp.re(z)), sp.simplify(sp.im(z))]


def pencil_certificate(identity,A,P,z,w,annihilate=False):
    v = sp.Matrix([z,1])
    cols = [m*v for m in (identity,A,P)]
    if annihilate:
        equations = sp.Matrix.hstack(*cols)
    else:
        coeffs = [(col[0]-w*col[1]).expand() for col in cols]
        equations = sp.Matrix(2,3,lambda i,j: real_and_imag(coeffs[j])[i])
    null = equations.nullspace()
    assert len(null) == 1
    weights = null[0]
    total = sp.simplify(sum(weights))
    assert total != 0
    weights = weights/total
    M = sum((weights[i]*m for i,m in enumerate((identity,A,P))), sp.zeros(2))
    if annihilate:
        assert M*v == sp.zeros(2,1)
        assert M.det() == 0
        assert all(c >= 0 for c in weights)
    else:
        assert sp.simplify((M*v)[0]-w*(M*v)[1]) == 0
        opposite = sp.im(z)*sp.im(w) < 0
        assert M.det() < 0 if opposite else M.det() == 0
        assert all(c > 0 for c in weights) if opposite else all(c >= 0 for c in weights)
        if z != w:
            ell=sp.Matrix([[1,-w]])/(z-w)
            vals=[(ell*m*v)[0] for m in (identity,A,P)]
            assert sp.simplify(sum(weights[i]*vals[i] for i in range(3))) == 0


def main():
    identity,A,P=symbolic_identities()
    rng=random.Random(30102026)
    rational_certificates=0
    for side in (-1,1):
        for j in range(40):
            z=sp.Rational(rng.randrange(-9,10),3)+side*sp.I*sp.Rational(rng.randrange(1,10),4)
            w=sp.Rational(rng.randrange(-9,10),5)-side*sp.I*sp.Rational(rng.randrange(1,10),6)
            pencil_certificate(identity,A,P,z,w)
            rational_certificates += 1
    for j in range(-8,9):
        pencil_certificate(identity,A,P,sp.Rational(j,3),0,True)
        pencil_certificate(identity,A,P,sp.Rational(j,3)+sp.I,sp.Rational(j+1,4))
        rational_certificates += 2

    # A constructive simultaneous central frame for finitely many transports
    # of one product, including nonidentity shared prefixes.
    hv=sp.Integer(200)
    av=(hv*hv-1)/2
    L=sp.Matrix([[1+av/2+sp.I*hv/2,(av-1)/4+sp.I*hv/2],
                 [-av-1,-av/2-sp.I*hv/2]])
    perturb=sp.Matrix([[1,1/hv**4],[0,1]])
    L=sp.simplify(perturb*L*perturb.inv())
    H=P+identity
    prefixes=[identity,sp.Matrix([[1,1+sp.I],[0,1]]),
              sp.Matrix([[1,0],[2-sp.I,1]]),sp.Matrix([[0,-1],[1,1+sp.I]])]
    local_feasibility_checks=0
    for W in prefixes:
        denom=sp.simplify((W.inv()*L).trace())
        assert denom != 0
        projector=sp.simplify(W.inv()*L/denom)
        assert sp.simplify(projector*projector-projector) == sp.zeros(2)
        assert sp.simplify(projector.trace()) == 1
        for br in range(-2,3):
            for bi in range(-2,3):
                b=sp.Integer(br)+sp.I*bi
                Ab=(identity+b*H)*A*(identity-b*H)
                vals=[sp.simplify((m*W*projector).trace()) for m in (identity,Ab,P)]
                base=[sp.simplify((m*L).trace()) for m in (identity,Ab,P)]
                assert all(sp.simplify(vals[i]-base[i]/denom)==0 for i in range(3))
                assert sp.im(base[0]*sp.conjugate(base[2])) != 0
                # Both scalar products are positive, an exact sufficient
                # certificate for the central inequality (no square root).
                assert sp.re(base[1]*sp.conjugate(base[0])) > 0
                assert sp.re(base[1]*sp.conjugate(base[2])) > 0
                local_feasibility_checks += 1

    trials=support_checks=central_checks=boundary_skips=0
    for _ in range(10000):
        vals=[complex(rng.randrange(-8,9),rng.randrange(-8,9)) for i in range(3)]
        if any(z==0 for z in vals):
            continue
        trials += 1
        a,b,c=vals
        # The exact central test always implies the exact strict-support test.
        support_exact=cross(a,c)!=0 and not origin_in_triangle(a,b,c)
        cent_exact=central_exact(a,b,c)
        assert not cent_exact or support_exact
        support,central,margin,coords=physical_arguments(a,b,c)
        if margin < 1e-10 or cross(a,c)==0:
            boundary_skips += 1
            continue
        assert support == support_exact, (vals,coords,support,support_exact)
        assert central == cent_exact, (vals,coords,central,cent_exact)
        support_checks += 1
        central_checks += 1
    # Cup/cap reciprocal logarithms use the actual +1 affine degree.
    cup_checks=0
    for _ in range(300):
        a=complex(rng.randrange(-8,9),rng.randrange(-8,9))
        b=complex(rng.randrange(-8,9),rng.randrange(-8,9))
        if not a or not b or cross(a,b)==0:
            continue
        r1=arg_0_2pi(-a/b)/(2*math.pi)
        r2=arg_0_2pi(-b/a)/(2*math.pi)
        assert abs(r1+r2-1)<2e-15
        cup_checks += 1

    result={
        'status':'PASS',
        'exact_symbolic': ['projector quotient and prefix coefficient',
                           'canonical pair traces and determinant pencil',
                           'both degree adapters have tau-2u=x2-x1',
                           'exact regular bad-frame positive convex relation',
                           'constructive common-product projector and transport formula'],
        'exact_rational_disk_certificates':rational_certificates,
        'exact_shared_product_central_feasibility_checks':local_feasibility_checks,
        'random_gaussian_integer_triples':trials,
        'argument_regression_support_checks':support_checks,
        'argument_regression_central_checks':central_checks,
        'argument_boundary_cases_skipped':boundary_skips,
        'cup_cap_canonical_log_checks':cup_checks,
        'scope':'Finite exact framing/support criterion and necessary disk-side obstruction. '
                'No favorable whole-plat frame, source branch comparison, normal-current estimate '
                'or contributing-cycle theorem is asserted.'
    }
    out=Path(__file__).with_name('actual_augmented_plat_physical_framing_criterion_results.json')
    out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
