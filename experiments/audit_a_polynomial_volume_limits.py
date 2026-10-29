#!/usr/bin/env python3
"""A-generated marked polynomial periods, independent of a Jones state.

Symbolic twist-curve and cover certificates; high precision figure-eight
tests of both product constructions. Numerical tests supplement the
general regulator/Riemann-sum proof, not a quantum volume conjecture.
"""

import json
from functools import cache
from itertools import product
from pathlib import Path

import mpmath as mp
import sympy as sp


@cache
def chebyshev(index, z):
    if index == -1:
        return sp.Integer(0)
    if index == 0:
        return sp.Integer(1)
    if index < -1:
        return -chebyshev(-index-2,z)
    return sp.expand(z*chebyshev(index-1,z)-chebyshev(index-2,z))


def twist_certificates():
    z, s, u, M = sp.symbols('z s u M')
    A = sp.Matrix([[M,1],[0,1/M]])
    B = sp.Matrix([[M,0],[-u,1/M]])
    W = A*B.inv()*A.inv()*B
    trace = u*u+(2-M*M-1/M**2)*u+2
    assert sp.cancel(sp.trace(W)-trace) == 0
    assert (A*W-W*B-(M*M+1/M**2-u-1)*(A-B)).applyfunc(sp.cancel) == sp.zeros(2)
    matrix_cases = []
    for k in (-3,-2,-1,1,2,3):
        r = (M*M+1/M**2-u-1)*chebyshev(k-1,trace)-chebyshev(k-2,trace)
        assert (A*W**k-W**k*B-r*(A-B)).applyfunc(sp.cancel) == sp.zeros(2)
        matrix_cases.append(k)
    curves = []
    for k in list(range(-8,0))+list(range(1,9)):
        S,T = chebyshev(k-1,z),chebyshev(k-2,z)
        assert sp.expand(S*S+T*T-z*S*T-1) == 0
        assert sp.gcd(S,T) == 1
        D = sp.expand(S*(S-T))
        ss = z-1/D
        uu = (z-2)*S/(S-T)
        assert sp.cancel((ss-uu-1)*S-T) == 0
        assert sp.cancel(uu*uu+(2-ss)*uu+2-z) == 0
        numerator = sp.fraction(sp.cancel(ss*ss-4))[0]
        factors = sp.factor_list(numerator)[1]
        assert any(multiplicity % 2 for _,multiplicity in factors)
        curves.append({'signed_twist_parameter':k,
                       'rational_trace_chart_and_Chebyshev_identity_exact':True,
                       'squared_meridian_discriminant_not_a_square':True})
    return {'direct_Wirtinger_matrix_relations':matrix_cases,'curves':curves}


def norm_and_cover_certificates():
    L,Z,m,l = sp.symbols('L Z m l')
    # Figure-eight cone samples alpha=0,pi/3 at N=2.
    first = L*L+2*L+1
    second_with_product = Z*Z+4*Z*L+L*L
    resultant = sp.resultant(first,second_with_product,L)
    assert sp.expand(resultant-(Z*Z-4*Z+1)**2) == 0
    selected = 2+sp.sqrt(3)
    assert sp.simplify(resultant.subs(Z,selected)) == 0
    covers = 0
    matrices = [(D,0,0,1) for D in range(1,7)]+[(2,1,1,2),(1,2,0,3),(1,1,-1,1),(2,3,1,2)]
    for a,b,c,d in matrices:
        degree = a*d-b*c
        for aa in range(-3,4):
            for bb in range(-3,4):
                mp_,lp_ = m**a*l**b,m**c*l**d
                ap,bp = a*aa+b*bb,c*aa+d*bb
                ratio = lp_**ap*mp_**(-bp)/(l**aa*m**(-bb))**degree
                assert sp.cancel(ratio) == 1
                covers += 1
    return {'exact_A_resultant':str(sp.factor(resultant)),
            'marked_algebraic_root':str(selected),'exact_peripheral_cover_products':covers}


def original_kashaev_calibration():
    # Literal N=2 original W-symbol and enhancement; no Jones evaluation.
    def symbol(i,j,k,l,a,b,c,d):
        u,v,t,h = (j-i-a)%2,(i-l-d)%2,(l-k-c)%2,(k-j-b)%2
        if u+t>=2 or v+h>=2:
            return sp.Integer(0)
        exponent = a-k-j+(v+t)*(t+h)
        return sp.Rational(2*(-1)**(exponent%2),2**(u+v+t+h))

    R,printed_inverse = sp.zeros(4),sp.zeros(4)
    for i,j,k,l in product(range(2),repeat=4):
        R[2*i+j,2*k+l] = symbol(i,j,k,l,1,0,0,0)*(-1)**((k+l)%2)
        printed_inverse[2*i+l,2*k+j] = symbol(i,j,k,l,0,0,0,1)*(-1)**((j+k)%2)
    swap = sp.zeros(4)
    for a,b in product(range(2),repeat=2):
        swap[2*b+a,2*a+b] = 1
    positive = swap*R.T
    negative = -printed_inverse.T*swap
    assert positive*negative == sp.eye(4)
    eye = sp.eye(2)
    value = sp.eye(8)
    for position,sign in ((0,1),(1,-1),(0,1),(1,-1)):
        crossing = positive if sign>0 else negative
        value *= sp.kronecker_product(crossing,eye) if position==0 else sp.kronecker_product(eye,crossing)
    pivot = -sp.I*sp.Matrix([[0,1],[1,0]])
    value *= sp.kronecker_product(eye,pivot,pivot)
    cut = sp.Matrix(2,2,lambda a,b:sum(value[4*a+2*c+d,4*b+2*c+d] for c,d in product(range(2),repeat=2)))
    assert cut == 5*sp.eye(2)
    classical = 2+sp.sqrt(3)
    assert classical != 5
    return {'level':2,'knot':'figure-eight','original_Kashaev_cut':5,
            'classical_cone_A_product':str(classical),'literal_finite_equality':False,
            'scope':'Finite calibration; a suitable quantum A-construction and source could still recover Kashaev.'}


def figure_eight_limits():
    mp.mp.dps = 55
    Theta = 2*mp.pi/3
    target = 2*mp.im(mp.polylog(2,mp.e**(mp.pi*1j/3)))

    def logarithm(alpha):
        a = 2+2*mp.cos(alpha)-2*mp.cos(2*alpha)
        if a < 2 and 2-a < mp.mpf('1e-45'):
            a = mp.mpf(2)
        assert a >= 2
        return mp.acosh(a/2)

    cone = []
    for N in (100,200,400,800,1600,3200):
        value = Theta/N*sum(logarithm(Theta*j/N) for j in range(N))
        cone.append({'N':N,'scaled_log_product':mp.nstr(value,28),
                     'error':mp.nstr(value-target,12)})
    assert abs(mp.mpf(cone[-1]['error'])) < mp.mpf('0.0001')

    rounded = []
    for N in (100,400,1600,6400,25600,102400):
        r = mp.isqrt(N) if hasattr(mp,'isqrt') else int(N**0.5)
        angle = lambda t: Theta*mp.sin(mp.pi*t)**2
        step = 2*mp.pi/N
        total = mp.mpf(0)
        max_residual = mp.mpf(0)
        for j in range(r):
            t0,t1 = mp.mpf(j)/r,mp.mpf(j+1)/r
            midpoint = (t0+t1)/2
            aa = int(mp.nint((angle(t1)-angle(t0))/step))
            # The sampled meridian is an exact root of unity, specified
            # by the integer exponent and denominator N^4.
            exponent = int(mp.nint(N**4*angle(midpoint)/(2*mp.pi)))
            alpha = 2*mp.pi*exponent/N**4
            log_lambda = logarithm(alpha)
            log_l = (2 if midpoint < mp.mpf('0.5') else -2)*log_lambda
            total += aa*log_l
            meridian = mp.e**(1j*alpha)
            longitude = mp.e**log_l
            trace = meridian**2-meridian-2-1/meridian+1/meridian**2
            residual = longitude**2-(trace**2-2)*longitude+1
            max_residual = max(max_residual,abs(residual))
        value = mp.pi/(2*N)*total
        assert max_residual < mp.mpf('1e-45')
        rounded.append({'N':N,'algebraic_sample_count':r,'root_of_unity_denominator':N**4,
                        'scaled_log_marked_polynomial_root':mp.nstr(value,28),
                        'error':mp.nstr(value-target,12),'squared_A_equation_residual':mp.nstr(max_residual,6)})
    assert abs(mp.mpf(rounded[-1]['error'])) < mp.mpf('0.02')
    assert abs(mp.mpf(rounded[-1]['error'])) < abs(mp.mpf(rounded[0]['error']))
    return {'target_two_regular_ideal_tetrahedra':mp.nstr(target,35),
            'cone_A_root_products':cone,'rounded_relative_A_norm_roots':rounded}


def main():
    twists = twist_certificates()
    norm = norm_and_cover_certificates()
    original = original_kashaev_calibration()
    limits = figure_eight_limits()
    result = {'scope':'Classical marked A-generated polynomial-period limit; no equivalence to a standard quantum invariant asserted.',
              'twist_character_connectedness_certificates':twists,
              'polynomial_norm_and_cover_certificates':norm,'figure_eight_limits':limits,
              'direct_original_Kashaev_calibration':original}
    path = Path(__file__).with_name('a_polynomial_volume_limits_results.json')
    path.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'results':str(path),'exact_twist_matrix_relations':len(twists['direct_Wirtinger_matrix_relations']),
                      'twist_curve_certificates':len(twists['curves']),
                      'exact_cover_products':norm['exact_peripheral_cover_products'],
                      'last_cone_error':limits['cone_A_root_products'][-1]['error'],
                      'last_marked_norm_root_error':limits['rounded_relative_A_norm_roots'][-1]['error']},indent=2),flush=True)


if __name__ == '__main__':
    main()
