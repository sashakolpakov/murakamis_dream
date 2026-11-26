#!/usr/bin/env python3
"""Exact root isolation and chart identities for the (-3,-3) pendant.

The geometric existence theorem and full logarithmic period arguments
are written separately. This script checks only rational root bounds,
the selected chart's sign and the displayed algebraic identities.
"""

from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import platform

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "notes/research_three_crossing_pendant_geometric_branch.md"


class Interval:
    def __init__(self, lo, hi=None):
        self.lo, self.hi = F(lo), F(lo if hi is None else hi)
        assert self.lo <= self.hi

    def __add__(self, other):
        other = other if isinstance(other, Interval) else Interval(other)
        return Interval(self.lo + other.lo, self.hi + other.hi)

    __radd__ = __add__

    def __neg__(self):
        return Interval(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + (-other if isinstance(other, Interval) else -F(other))

    def __rsub__(self, other):
        return -self + other

    def __mul__(self, other):
        other = other if isinstance(other, Interval) else Interval(other)
        values = [self.lo * other.lo, self.lo * other.hi,
                  self.hi * other.lo, self.hi * other.hi]
        return Interval(min(values), max(values))

    __rmul__ = __mul__

    def inverse(self):
        assert self.lo * self.hi > 0
        return Interval(1 / self.hi, 1 / self.lo)

    def record(self):
        return [str(self.lo), str(self.hi)]


class ComplexRectangle:
    def __init__(self, real, imag=0):
        self.real = real if isinstance(real, Interval) else Interval(real)
        self.imag = imag if isinstance(imag, Interval) else Interval(imag)

    def __add__(self, other):
        other = other if isinstance(other, ComplexRectangle) else ComplexRectangle(other)
        return ComplexRectangle(self.real + other.real, self.imag + other.imag)

    __radd__ = __add__

    def __neg__(self):
        return ComplexRectangle(-self.real, -self.imag)

    def __sub__(self, other):
        return self + (-other if isinstance(other, ComplexRectangle) else -F(other))

    def __rsub__(self, other):
        return -self + other

    def __mul__(self, other):
        other = other if isinstance(other, ComplexRectangle) else ComplexRectangle(other)
        return ComplexRectangle(
            self.real * other.real - self.imag * other.imag,
            self.real * other.imag + self.imag * other.real,
        )

    __rmul__ = __mul__

    def inverse(self):
        reciprocal = (self.real * self.real + self.imag * self.imag).inverse()
        return ComplexRectangle(self.real * reciprocal, -self.imag * reciprocal)

    def __truediv__(self, other):
        return self * other.inverse()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output", type=Path,
        default=ROOT / "repro/results/research-three-crossing-geometric-branch.json",
    )
    args = parser.parse_args()

    tau, x, w = sp.symbols("tau x w")
    z = 4 - 5*tau + 4*tau**2 - tau**3
    r = tau**2 - 3*tau + 3
    v = (tau - 2)**2 * (tau**2 - 2*tau + 2)
    polynomial = sp.expand(v - 2*sp.I)
    centers = [(2610, 416), (624, -683), (1822, -1037), (944, 1303)]
    expected = [3702643231, 1874713022, 932436308, 2635665116]
    radius = sp.Rational(1, 1000)
    root_records = []
    for (a, b), expected_numerator in zip(centers, expected):
        center = sp.Rational(a, 1000) + sp.I*sp.Rational(b, 1000)
        coefficients = [
            sp.expand(sp.diff(polynomial, tau, j).subs(tau, center)/sp.factorial(j))
            for j in range(5)
        ]
        l1 = lambda value: abs(sp.re(value)) + abs(sp.im(value))
        linf = lambda value: max(abs(sp.re(value)), abs(sp.im(value)))
        margin = (
            radius*linf(coefficients[1]) - l1(coefficients[0])
            - sum(radius**j*l1(coefficients[j]) for j in range(2, 5))
        )
        assert margin == sp.Rational(expected_numerator, 10**12) > 0
        root_records.append({"center": [a, b], "denominator": 1000,
                             "radius": "1/1000", "rouche_margin": str(margin)})
    for i, (a, b) in enumerate(centers):
        for c, d in centers[i+1:]:
            assert (a-c)**2 + (b-d)**2 > 4

    # The second and third disks are strictly below the real axis.
    assert centers[1][1] + 1 < 0 and centers[2][1] + 1 < 0
    # The first disk cannot have a positive-real-part outer half cosine.
    assert F(611, 1000)**2 + F(417, 1000)**2 < F(3, 4)**2
    assert 2*F(2609, 1000) - 3 > F(3, 4)
    assert F(945, 1000) < F(3, 2)

    X = r/(z*r - 1)
    E = -(tau-2)**3*(tau**2-2*tau+2)**2/(tau-1)**2
    dclock = 2-X-1/X
    C = X+1/X-dclock*E
    L = X+1/X-dclock/E
    identities = {
        "terminal_trace": 2+(1-tau)**2*(2-tau)-z,
        "last_return": (2-tau)*(tau-z)+v,
        "source_C": C-2-v**2,
        "source_L": L-z,
        "retained_wire_E": E*(2-z)+v**2,
    }
    wire_E = -(x+w)*(x+1/w)/(x-1)**2
    wire_L = x+1/x-(2-x-1/x)/wire_E
    d2 = -(1-x)**2*(1+w)**2/(4*(x+w)*(1+w*x))
    multiplier = (1+w*x)/(x+w)
    identities["wire_half_cosine"] = (2-wire_L)/4-d2
    identities["primitive_multiplier"] = (
        (multiplier-1)**2/(4*multiplier)
        + d2*(w-1)**2/(w+1)**2
    )
    for name, expression in identities.items():
        assert sp.cancel(expression) == 0, name

    # Interval chart sign on the rectangle containing the selected disk.
    tbox = ComplexRectangle(
        Interval(F(943, 1000), F(945, 1000)),
        Interval(F(1302, 1000), F(1304, 1000)),
    )
    rbox = tbox*tbox-3*tbox+3
    zbox = 4-5*tbox+4*tbox*tbox-tbox*tbox*tbox
    denominator_box = zbox*rbox-1
    denominator_norm_square = (
        denominator_box.real*denominator_box.real
        + denominator_box.imag*denominator_box.imag
    )
    assert F(187, 100) < denominator_box.real.lo
    assert denominator_box.real.hi < F(206, 100)
    assert -F(144, 100) < denominator_box.imag.lo
    assert denominator_box.imag.hi < -F(5, 4)
    assert denominator_norm_square.lo > 5
    xbox = rbox/denominator_box
    assert F(1, 50) < xbox.real.lo < xbox.real.hi < F(1, 4)
    assert -F(4, 5) < xbox.imag.lo < xbox.imag.hi < -F(1, 2)

    # No other displayed cap or chart denominator vanishes at any root.
    denominators = [
        tau-1, tau-2, tau**2-2*tau+2, r, z*r-1,
        (z+1)*r-1,
    ]
    for denominator in denominators:
        assert sp.degree(sp.gcd(polynomial, denominator, extension=sp.I), tau) == 0

    source = Path(__file__).resolve()
    result = {
        "status": "pass",
        "scope": (
            "Exact rational root isolation and source/primitive-period identities. "
            "Geometric existence, marking and logarithmic branch selection use "
            "the separate written proof; no quantum asymptotic is tested."
        ),
        "python_version": platform.python_version(),
        "sympy_version": sp.__version__,
        "script_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "note_sha256": hashlib.sha256(NOTE.read_bytes()).hexdigest(),
        "root_disks": root_records,
        "selected_disk_index": 3,
        "selected_clock_real_interval": xbox.real.record(),
        "selected_clock_imaginary_interval": xbox.imag.record(),
        "clock_denominator_real_interval": denominator_box.real.record(),
        "clock_denominator_imaginary_interval": denominator_box.imag.record(),
        "clock_denominator_norm_squared_interval": denominator_norm_square.record(),
        "exact_identities": list(identities),
        "nonvanishing_denominator_checks": len(denominators),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"status": "pass", "root_disks": len(root_records),
                      "exact_identities": len(identities),
                      "output": str(args.output),
                      "script_sha256": result["script_sha256"]}))


if __name__ == "__main__":
    main()
