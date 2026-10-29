#!/usr/bin/env python3
"""Exact algebraic checks of the resolved complete Newton cut.

These check universal rational identities, an arbitrary odd cusp germ,
and the finite-root normal adapter. They do not test a selected knot
asymptotic or assert geometric support of an unspecified operator.
"""

import json
from pathlib import Path

import sympy as s


Y, L, u, e, r, x = s.symbols('Y L u e r x')


def rational_geometry():
    uu = (Y * L + 1) / (Y + L)
    ee = Y * (Y + L) * (Y * L + 1) / (L * (Y**2 - 1)**2)
    xx = 1 / e + u + 1 / u
    ss = u + 1 / u + (u - 1 / u)**2 * e
    zz = u * (xx + ss) - 2
    fricke = xx**2 + ss**2 + zz**2 - xx * ss * zz - 4
    assert s.cancel(fricke) == 0
    assert s.cancel((zz + 2) / (xx + ss) - u) == 0
    assert s.cancel(1 / (xx - u - 1 / u) - e) == 0
    substitutions = {u: uu, e: ee}
    for actual, expected in ((xx, Y + 1/Y), (ss, L + 1/L),
                             (zz, Y*L + 1/(Y*L))):
        assert s.cancel(actual.subs(substitutions) - expected) == 0
    area = (s.diff(uu, Y)*s.diff(ee, L)
            - s.diff(uu, L)*s.diff(ee, Y)) / (uu * ee)
    assert s.cancel(area - 1/(Y*L)) == 0
    assert s.cancel(uu.subs({Y: 1/Y, L: 1/L}, simultaneous=True)-uu) == 0
    assert s.cancel(ee.subs({Y: 1/Y, L: 1/L}, simultaneous=True)-ee) == 0
    g = 2-u-1/u
    assert s.cancel(1-e*g-e*(xx-2)) == 0
    ec = -u/(u-1)**2
    assert s.cancel(xx.subs(e, ec)-2) == 0
    assert s.cancel(ss.subs(e, ec)+2) == 0
    assert s.cancel(zz.subs(e, ec)+2) == 0
    er = (1-r)/g
    assert s.cancel(s.diff(er, r)/(u*er)+1/(u*(1-r))) == 0
    return {'fricke_and_inverse': True, 'full_torus_substitution': True,
            'symplectic_jacobian': True, 'weighted_weyl_invariance': True,
            'exceptional_curve_and_regular_normal': True}


def arbitrary_cusp():
    # Use rational odd germs in q=(Y-1)/(Y+1). This gives exact
    # Weyl covariance without expensive exponential series.
    q, tau, beta = s.symbols('q tau beta')
    # lambda=2atanh(tau*q+beta*q^3), so d lambda/d logY=tau.
    zeta = tau*q + beta*q**3
    yy = (1+q)/(1-q)
    ll = -(1+zeta)/(1-zeta)
    uu = s.cancel((yy*ll+1)/(yy+ll))
    ee = s.cancel(yy*(yy+ll)*(yy*ll+1)/(ll*(yy**2-1)**2))
    assert s.cancel(uu.subs(q, -q)-uu) == 0
    assert s.cancel(ee.subs(q, -q)-ee) == 0
    u0 = s.cancel(uu.subs(q, 0))
    e0 = s.cancel(ee.subs(q, 0))
    assert s.cancel(u0-(tau+1)/(tau-1)) == 0
    assert s.cancel(e0-(1-tau**2)/4) == 0
    assert s.cancel(e0+u0/(u0-1)**2) == 0
    ww = s.cancel(yy+1/yy-2)
    rr = s.cancel(1-ee*(2-uu-1/uu))
    assert s.cancel(rr-ee*ww) == 0
    assert s.limit(s.cancel(rr/ww), q, 0) == e0
    p, imaginary = s.symbols('p imaginary', real=True)
    uc = ((p+s.I*imaginary)+1)/((p+s.I*imaginary)-1)
    im = s.simplify(s.im(s.expand_complex(uc)))
    assert s.cancel(im+2*imaginary/((p-1)**2+imaginary**2)) == 0
    return {'arbitrary_odd_cusp_parameters': ['tau','beta'],
            'even_descent_to_quotient': True, 'algebraic_complete_limits': True,
            'exact_r_equals_e_w': True, 'transverse_normal_derivative': str(e0),
            'orientation_half_plane': True}


def kernel_differentials():
    xx = Y+1/Y
    ratio = xx-u-1/u
    longitude = (u*Y-1)/(Y-u)
    # Exponentiating the derivatives of (16) fixes their algebraic
    # arguments independently of logarithmic sheet conventions.
    exp_dU = -(1-u*Y)*(1-u/Y)/u
    exp_dy = (1-1/Y)*(1-u*Y)/((1-Y)*(1-u/Y))
    assert s.cancel(exp_dU-ratio) == 0
    assert s.cancel(exp_dy-longitude) == 0
    cross_Uy = Y*s.diff(ratio,Y)/ratio
    cross_yU = u*s.diff(longitude,u)/longitude
    assert s.cancel(cross_Uy-cross_yU) == 0
    assert s.cancel((1-e*(2-u-1/u))-e*(1/e+u+1/u-2)) == 0
    assert s.cancel(longitude.subs(Y,1)+1) == 0
    return {'dilogarithm_derivative_arguments': True,
            'mixed_derivative_integrability': True,
            'stationary_cut_is_exceptional_curve': True,
            'interior_complete_longitude': -1}


def central_normal_projectors():
    records=[]
    cprev, ccur=s.Integer(2),x
    for level in range(2,19):
        cnext=s.expand(x*ccur-cprev)
        cprev,ccur=ccur,cnext
        polynomial=s.Poly(ccur-2,x)
        quotient,rem=s.div(polynomial,s.Poly(x-2,x))
        assert rem.is_zero
        hn=quotient.as_expr()
        assert hn.subs(x,2)==level**2
        projector=hn/level**2
        assert s.rem(projector**2-projector,polynomial.as_expr(),x)==0
        assert s.rem((x-2)*projector,polynomial.as_expr(),x)==0
        # The trace normal adapter agrees with the exact finite-root
        # power relation, without setting U_c to one first.
        exact=s.cancel(ccur.subs(x,Y+1/Y)-Y**level-Y**(-level))
        assert exact==0
        records.append({'level':level, 'trace_normal_multiplier':level**2,
                        'idempotent_and_eigenspace':True,
                        'unmodified_power_relation':True})
    return records


def main():
    result={'universal_rational_geometry':rational_geometry(),
            'arbitrary_odd_cusp':arbitrary_cusp(),
            'kernel_generating_differential':kernel_differentials(),
            'central_normal_projectors':central_normal_projectors(),
            'scope':'Resolved marked geometric target and universal cut; '
                    'no actual geometric-symbol or selected-volume claim.'}
    output=Path(__file__).with_name('newton_resolution_and_regulator_cut_results.json')
    output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'universal_rational_geometry':result['universal_rational_geometry'],
                      'arbitrary_odd_cusp':result['arbitrary_odd_cusp'],
                      'kernel_generating_differential':result['kernel_generating_differential'],
                      'central_normal_projectors':len(result['central_normal_projectors']),
                      'output':str(output)},indent=2))


if __name__=='__main__':
    main()
