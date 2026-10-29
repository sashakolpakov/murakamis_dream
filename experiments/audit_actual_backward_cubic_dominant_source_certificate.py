#!/usr/bin/env python3
"""Exact rational/Sturm certificate for the actual backward cubic's dominant root.

No sampled root plot is used for the conclusion.  The printed decimal
approximations only label the two exact isolating intervals.
"""
import json
from dataclasses import dataclass
from fractions import Fraction as F
from pathlib import Path

import sympy as s


@dataclass(frozen=True)
class Interval:
    lo: F
    hi: F

    @staticmethod
    def point(x):
        x = F(x)
        return Interval(x, x)

    def __add__(self, other):
        other = as_interval(other)
        return Interval(self.lo + other.lo, self.hi + other.hi)

    __radd__ = __add__

    def __neg__(self):
        return Interval(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + (-as_interval(other))

    def __rsub__(self, other):
        return as_interval(other) + (-self)

    def __mul__(self, other):
        other = as_interval(other)
        values = [a*b for a in (self.lo, self.hi)
                  for b in (other.lo, other.hi)]
        return Interval(min(values), max(values))

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = as_interval(other)
        assert other.lo > 0 or other.hi < 0
        return self * Interval(1/other.hi, 1/other.lo)

    def __pow__(self, n):
        assert n >= 0
        result = Interval.point(1)
        for _ in range(n):
            result *= self
        return result

    def abs_upper(self):
        return max(abs(self.lo), abs(self.hi))

    def abs_lower(self):
        return F(0) if self.lo <= 0 <= self.hi else min(abs(self.lo), abs(self.hi))


def as_interval(x):
    return x if isinstance(x, Interval) else Interval.point(x)


def cpoint(re, im=0):
    return Interval.point(re), Interval.point(im)


def cadd(a, b):
    return a[0]+b[0], a[1]+b[1]


def cscale(a, b):
    return a[0]*b, a[1]*b


def cmul(a, b):
    return a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0]


def cpow(a, n):
    result = cpoint(1)
    for _ in range(n):
        result = cmul(result, a)
    return result


def cupper(a):
    return a[0].abs_upper()+a[1].abs_upper()


def clower(a):
    return max(a[0].abs_lower(), a[1].abs_lower())


def polynomial_interval(poly, symbol, domain):
    coefficients = s.Poly(poly, symbol).all_coeffs()
    result = Interval.point(0)
    for coefficient in coefficients:
        result = result*domain + F(int(s.numer(coefficient)), int(s.denom(coefficient)))
    return result


def certificate():
    Z, lam, w, v, t, a, b, c = s.symbols('Z lam w v t a b c')
    p = lam**3+a*lam**2+b*lam+c
    T = (a**3*c*(t+2)-a**2*b**2-a*b*c*(t*t+5*t+4)
         +b**3*(t+2)+c**2*(t+1)**3)/c**2
    ratio = s.cancel(s.resultant(p, w**3*p.subs(lam, lam/w), lam)/(w-1)**3)
    assert s.factor(ratio-c**3*w**3*T.subs(t, w+1/w)) == 0

    az, bz, cz = 5*Z-3, (3-7*Z+3*Z**2)*(1-Z), -(1-Z)**5
    f = p.subs({a: az, b: bz, c: cz})
    assert s.factor(s.discriminant(f, lam)+Z**6*(Z-1)**2*(27*Z**2-54*Z+23)) == 0
    Tz = s.factor(T.subs({a: az, b: bz, c: cz}))

    R2 = (2*(v-2)**4*t**3
          +(-3*v**4+39*v**3-166*v**2+292*v-184)*t**2
          +(15*v**4-72*v**3+141*v**2-181*v+134)*t
          -7*v**4+62*v**3-87*v**2-132*v+220)
    I = ((9*v**3-57*v**2+120*v-84)*t**2
         +(-9*v**3+120*v**2-373*v+339)*t
         +9*v**3-66*v**2+235*v-288)
    R = R2/2
    assert s.factor((Tz+Tz.subs(Z, 1/Z))/2
                    -R.subs(v, Z+1/Z)/(Z+1/Z-2)**4) == 0
    assert s.factor((Tz-Tz.subs(Z, 1/Z))/(Z-1/Z)
                    -I.subs(v, Z+1/Z)/(Z+1/Z-2)**4) == 0

    P = (19683*v**13-275562*v**12+1388745*v**11-1804275*v**10
         -10052343*v**9+44382411*v**8-41161510*v**7-136024030*v**6
         +409871548*v**5-286814789*v**4-449999851*v**3
         +1045577541*v**2-804786993*v+230409954)
    A = (486*v**6-3807*v**5+8973*v**4+4038*v**3
         -51728*v**2+82608*v-43461)
    C = (-243*v**6+3240*v**5-12492*v**4+6666*v**3
         +61295*v**2-138366*v+89982)
    assert s.factor(s.resultant(R, I, t)-(v-2)**4*P) == 0
    assert s.factor(s.subresultants(R, I, t)[-2]-(v-2)**4*(A*t+C)) == 0

    negative = Interval(F(-1761026772, 10**9), F(-1761026771, 10**9))
    positive = Interval(F(1314531712, 10**9), F(1314531713, 10**9))
    poly = s.Poly(P, v)
    assert poly.count_roots(-2, 2) == 2
    for domain in (negative, positive):
        assert poly.count_roots(s.Rational(domain.lo), s.Rational(domain.hi)) == 1
    candidate_t = []
    for domain in (negative, positive):
        value = -polynomial_interval(C, v, domain)/polynomial_interval(A, v, domain)
        candidate_t.append(value)
    assert 1 < candidate_t[0].lo < candidate_t[0].hi < 2
    assert 4 < candidate_t[1].lo < candidate_t[1].hi < 5

    # Exact rectangle containing Z=v/2-i sqrt(1-v^2/4) at the
    # only admissible interior equimodulus candidate.
    z_re = negative/F(2)
    abs_im_lo, abs_im_hi = F(474021281, 10**9), F(474021285, 10**9)
    assert abs_im_lo**2 < 1-negative.lo**2/4
    assert abs_im_hi**2 > 1-negative.hi**2/4
    z = z_re, Interval(-abs_im_hi, -abs_im_lo)
    one_minus_z = cadd(cpoint(1), cscale(z, -1))
    ca = cadd(cscale(z, 5), cpoint(-3))
    cb = cmul(cadd(cadd(cpoint(3), cscale(z, -7)), cscale(cpow(z, 2), 3)),
              one_minus_z)
    cc = cscale(cpow(one_minus_z, 5), -1)
    centers = [(F(1168965, 10**6), F(2383072, 10**6)),
               (F(2467958, 10**6), F(977085, 10**6)),
               (F(3765644, 10**6), F(-990050, 10**6))]
    radius = F(1, 1000)
    disks = []
    for index, center in enumerate(centers):
        z0 = cpoint(*center)
        value = cadd(cadd(cadd(cpow(z0, 3), cmul(ca, cpow(z0, 2))), cmul(cb, z0)), cc)
        derivative = cadd(cadd(cscale(cpow(z0, 2), 3), cscale(cmul(ca, z0), 2)), cb)
        quadratic = cadd(cscale(z0, 3), ca)
        assert cupper(value) < F(1, 50000)
        assert clower(derivative) > 1
        assert cupper(quadratic) < 20
        assert (cupper(value)+cupper(quadratic)*radius**2+radius**3
                < clower(derivative)*radius)
        norm_square = center[0]**2+center[1]**2
        if index < 2:
            assert norm_square < (3-radius)**2
        else:
            assert norm_square > (3+radius)**2
        disks.append({'center': [str(q) for q in center], 'radius': str(radius),
                      'root_count': 1, 'modulus_side_of_3': '<' if index < 2 else '>'})
    for i in range(3):
        for j in range(i):
            distance_square = sum((centers[i][k]-centers[j][k])**2 for k in range(2))
            assert distance_square > 4*radius**2

    return {'status': 'PASS', 'general_ratio_and_discriminant_identities': True,
            'real_imaginary_resultant_and_linear_subresultant': True,
            'exact_sturm_roots_in_minus2_plus2': 2,
            'candidate_intervals': [[str(q.lo), str(q.hi)] for q in (negative, positive)],
            'candidate_ratio_t_intervals': [[str(q.lo), str(q.hi)] for q in candidate_t],
            'exact_rouche_disks_at_only_admissible_candidate': disks,
            'scope': 'Unique dominant eigenvalue on 0<=u<pi/2, uniform gap on strict prefixes; no source projection or whole-source norm inferred.'}


if __name__ == '__main__':
    result = certificate()
    Path(__file__).with_name('actual_backward_cubic_dominant_source_certificate_results.json').write_text(
        json.dumps(result, indent=2)+'\n')
    print('PASS exact ratio/resultant/discriminant identities; 2 Sturm candidates; '
          '3 rational Rouche root disks; backward dominant gap on every strict half-prefix')
