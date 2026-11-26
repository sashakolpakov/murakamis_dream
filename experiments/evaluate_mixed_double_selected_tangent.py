#!/usr/bin/env python3
"""Outward tangent-plane bounds for the original double-selection profiles.

The proposal optimizer is optional proof input: any rational point in the
fixed target box is valid. All accepted inequalities use Arb evaluations
and exact rational support functions, never the optimizer's reported value.
"""
from fractions import Fraction as F
from flint import acb, arb

NAMES = ("e", "a", "u", "z", "v", "b")
H = F(1, 100)


def rat(x):
    x = F(x)
    return arb(x.numerator)/arb(x.denominator)


def fraction(x):
    return F(str(x.fmpq()))


def endpoints(x):
    if not x.is_finite():
        raise ValueError("nonfinite real interval")
    return fraction(x.lower()), fraction(x.upper())


def real_record(x):
    lo, hi = endpoints(x)
    return {"finite": True, "lower_rational": str(lo), "upper_rational": str(hi)}


def ball(lo, hi):
    lo, hi = F(lo), F(hi)
    if lo > hi:
        raise ValueError("reversed interval")
    return arb(rat((lo+hi)/2), rat((hi-lo)/2))


def read_real(x):
    return ball(x["lower_rational"], x["upper_rational"])


def read_complex(x):
    return acb(read_real(x["real"]), read_real(x["imag"]))


def complex_record(x):
    return {"real": real_record(x.real), "imag": real_record(x.imag)}


class Primitive:
    def __init__(self):
        self.pi, self.ii = arb.pi(), acb(0, 1)
        self.calls = {"g": 0, "gp": 0, "auxiliary": 0}

    @staticmethod
    def regular(z):
        if not z.is_finite() or not (z.real > 0 and z.real < 1):
            raise ValueError("original logarithmic strip not enclosed")

    def g(self, z):
        self.regular(z)
        self.calls["g"] += 1
        result = ((-2*self.pi*self.ii*z).exp().polylog(2)-self.pi*self.pi/6)/(2*self.pi*self.ii)
        if not result.is_finite():
            raise ValueError("nonfinite original primitive")
        return result

    def gp(self, z):
        self.regular(z)
        self.calls["gp"] += 1
        result = (1-(-2*self.pi*self.ii*z).exp()).log()
        if not result.is_finite():
            raise ValueError("nonfinite original logarithm")
        return result

    def J(self, z):
        return self.g(z)-self.ii*self.pi*z*(1-z)/2

    def jp(self, z):
        return self.gp(z)-self.ii*self.pi*(1-2*z)/2

    def auxiliary(self, e):
        self.calls["auxiliary"] += 1
        disc = 1-2*(2*self.pi*self.ii*e).exp()
        # On the original cap rectangle the discriminant stays in the
        # right half-plane, so the printed principal root is unambiguous.
        if not disc.real > 0:
            raise ValueError("cap discriminant not in the right half-plane")
        xi = ((self.ii+disc.sqrt())/2).atan()/self.pi
        self.regular(xi)
        self.regular(e-xi)
        self.regular(acb(rat(F(1, 2)))-xi)
        return xi

    def cap(self, e, a):
        xi = self.auxiliary(e)
        action = (-2*self.J(acb(rat(F(1, 2)))-xi)-3*self.J(xi)
                  -self.J(e-xi)+self.ii*self.pi*e*xi)
        value = action+self.J(e+a)-self.J(a)-self.ii*self.pi*e*a-self.g(e)
        de = -self.jp(e-xi)+self.ii*self.pi*xi+self.jp(e+a)-self.ii*self.pi*a-self.gp(e)
        da = self.jp(e+a)-self.jp(a)-self.ii*self.pi*e
        return value, de, da

    def ordinary(self, s, a, b, beta):
        value = (self.g(s+a)+self.g(s+b)-(2+beta)*self.g(s)
                 -self.g(a)-self.g(b)+2*self.ii*self.pi*a*s)
        ds = self.gp(s+a)+self.gp(s+b)-(2+beta)*self.gp(s)+2*self.ii*self.pi*a
        da = self.gp(s+a)-self.gp(a)+2*self.ii*self.pi*s
        db = self.gp(s+b)-self.gp(b)
        return value, ds, da, db

    def phase(self, q, beta):
        e, a, u, z, v, b = q
        ce, q2, q3 = self.cap(e, a), self.ordinary(u, a, z, 1), self.ordinary(v, z, b, beta)
        value = ce[0]+q2[0]+q3[0]-self.g(a)-self.g(z)-beta*self.g(b)/2
        gradient = [
            ce[1], ce[2]+q2[2]-self.gp(a), q2[1],
            q2[3]+q3[2]-self.gp(z), q3[1], q3[3]-beta*self.gp(b)/2,
        ]
        return value, gradient


def target_box(beta, cap_kind, right_kind):
    box = [(F(".27"), F(".49")), (F(".22"), F(".45")),
           (F(".125"), F(".5")), (F(".22"), F(".45")),
           (F(".15") if beta == 0 else F(".125"), F(".5")),
           (F(".22"), F(".45"))]
    if cap_kind == "left":
        box[0] = (F(".27"), F(".27"))
    if right_kind == "half":
        box[4] = (F(".5"), F(".5"))
    return box


def evaluate(row, cap_kind, right_kind, nu1, nu2, trial):
    beta = row["beta"]
    if beta not in (0, 1) or cap_kind not in ("main", "left"):
        raise ValueError("unsupported profile")
    if right_kind not in ("main", "half") or (beta == 1 and right_kind != "main"):
        raise ValueError("unsupported outgoing profile")
    if nu1 not in (0, 1) or nu2 not in (0, 1):
        raise ValueError("unsupported Fourier alternative")
    box = target_box(beta, cap_kind, right_kind)
    trial = tuple(F(x) for x in trial)
    if len(trial) != 6 or not all(lo <= x <= hi for x, (lo, hi) in zip(trial, box)):
        raise ValueError("trial lies outside original target box")
    p = Primitive()
    r = [read_complex(row["coordinates"][name]) for name in NAMES]
    q = [acb(rat(x), z.imag) for x, z in zip(trial, r)]
    q[1], q[3] = acb(rat(trial[1]), rat(H)), acb(rat(trial[3]), rat(H))
    if cap_kind == "left":
        q[0] = acb(rat(F(".27")))
    if right_kind == "half":
        q[4] = acb(rat(F(".5")))
    ref, ref_gradient = p.phase(r, beta)
    value, gradient = p.phase(q, beta)
    marginal = ref_gradient[-1]
    value -= ref+marginal*(q[-1]-r[-1])
    gradient[-1] -= marginal
    for index, nu in ((1, nu1), (3, nu2)):
        value += (1-nu)*p.g(q[index])-2*p.pi*rat(H)*nu
        gradient[index] += (1-nu)*p.gp(q[index])
    support = []
    for index, (x, (lo, hi), slope) in enumerate(zip(trial, box, gradient)):
        lower, upper = endpoints(slope.real)
        products = [lower*(lo-x), upper*(lo-x), lower*(hi-x), upper*(hi-x)]
        support.append({
            "name": NAMES[index], "trial": str(x), "lower": str(lo), "upper": str(hi),
            "gradient": real_record(slope.real), "corner_products": list(map(str, products)),
            "upper_rational": str(max(products)),
        })
    upper = endpoints(value.real)[1]+sum(F(s["upper_rational"]) for s in support)
    return {
        "cap": cap_kind, "right": right_kind, "nu1": nu1, "nu2": nu2,
        "trial": list(map(str, trial)), "trial_defect": real_record(value.real),
        "outgoing_marginal": complex_record(marginal),
        "support_terms": support, "upper_rational": str(upper),
        "upper_decimal_display": float(upper), "primitive_calls": p.calls,
    }
