#!/usr/bin/env python3
"""Exact symbolic checks for the bounded local mixed-circle port chart.

These checks certify the displayed rational identities and complete
matrices. They do not certify the missing global stack face/periphery map.
"""

import json
from pathlib import Path

import sympy as sp


def zero(expr):
    if isinstance(expr, sp.MatrixBase):
        return all(sp.cancel(x) == 0 for x in expr)
    return sp.cancel(expr) == 0


def main():
    w, y = sp.symbols("w y", nonzero=True)
    eye = sp.eye(2)
    c = w + 1 / w
    u = (w * y - 1) / (w - y)
    a = sp.Matrix([[-1, -1], [0, -1]])
    b = sp.Matrix([[-1, 0], [2 - c, -1]])
    aa = b * a
    bb = w * (y - 1) / ((w - 1) * (w - y))
    al = sp.cancel((u + 1 - bb * c) / 2)
    kt = (al * eye + bb * aa).applyfunc(sp.cancel)
    ki = kt.inv().applyfunc(sp.cancel)
    checks = 0

    def check(condition):
        nonlocal checks
        assert condition
        checks += 1

    check(zero(kt.det() - u))
    check(zero(kt * aa - aa * kt))
    check(zero(bb * (w - 1 / w) - (u - 1)))
    check(zero(al + bb * w - u))
    check(zero(al + bb / w - 1))
    check(zero(kt.subs(w, 1 / w) - kt / u))

    ap = (kt * a * ki).applyfunc(sp.cancel)
    bp = (kt * b * ki).applyfunc(sp.cancel)
    pp = (a * kt * a.inv() * ki).applyfunc(sp.cancel)
    check(zero(pp - b.inv() * kt * b * ki))
    dd = 2 + (w - 1) ** 2 * (y - 1) ** 2 / ((w - y) * (w * y - 1))
    check(zero(sp.trace(pp) - dd))
    old_d = ((w - 1) / (w + 1)) ** 2 * (u + 1 / u) + 8 * w / (w + 1) ** 2
    check(zero(old_d - dd))
    jt = eye - y * pp
    ct = y * eye - pp
    delta = 1 - y * dd + y**2
    check(zero(jt.det() - delta))
    check(zero(ct.det() - delta))
    check(zero(jt * ct + delta * pp))
    check(zero(jt * bp - a * jt))
    # Literal unrotated input=(bp,b^-1), output=(ap^-1,a).
    check(zero(ct.inv() * b.inv() * ct - ap.inv()))
    check(zero(ct.inv() * b.inv() * bp * b * ct - a))
    # Opposite half twist has auxiliary meridian J^-1; scalar drops out.
    check(zero(jt * bp * jt.inv() - a))
    check(zero(jt * bp.inv() * b.inv() * bp * jt.inv() - ap.inv()))

    ii = sp.I
    ae = aa.subs(w, -1)
    ke = eye - ii * (ae + eye) / 2
    pe = (a * ke * a.inv() * ke.inv()).applyfunc(sp.simplify)
    ce = (eye - (pe + eye) / (1 + ii)).applyfunc(sp.simplify)
    je = ((eye - ii * pe) / (1 + ii)).applyfunc(sp.simplify)
    check(zero(kt.subs({w: -1, y: ii}) - ke))
    check(zero(pe - sp.Matrix([[-1 + 2 * ii, -1], [-4, -1 - 2 * ii]])))
    check(zero(sp.trace(pe) + 2))
    check(zero(sp.trace(ce) - 2))
    mm = sp.Matrix([[1, sp.Rational(1, 2)], [1, ii / 2]])
    check(zero(mm * ae * mm.inv() - sp.Matrix([[-1, 0], [2 - 2 * ii, -1]])))
    check(zero(mm * pe * mm.inv() - sp.Matrix([[-1, -2 + 2 * ii], [0, -1]])))
    check(zero(mm * ce * mm.inv() - sp.Matrix([[1, -2 * ii], [0, 1]])))
    check(zero(mm * je * mm.inv() - sp.Matrix([[1, 2], [0, 1]])))
    # Six exact developed flags: outer, inner, a,b,a',b'.
    flags = [
        (sp.Matrix([-sp.Rational(1, 2), 1]), 0),
        (sp.Matrix([-ii / 2, 1]), sp.oo),
        (sp.Matrix([1, 0]), 1),
        (sp.Matrix([0, 1]), -ii),
        (ke * sp.Matrix([1, 0]), ii),
        (ke * sp.Matrix([0, 1]), -1),
    ]
    for vector, target in flags:
        mapped = (mm * vector).applyfunc(sp.simplify)
        check(zero(mapped[1]) if target is sp.oo else zero(mapped[0] - target * mapped[1]))
    check(sp.simplify((2 - 2 * ii) / (-2 * ii)) == 1 + ii)
    check(sp.simplify((2 - 2 * ii) / (-2)) == -1 + ii)

    def projectively_equal(left, right):
        quotient = (left * right.inv()).applyfunc(sp.simplify)
        return zero(quotient[0, 1]) and zero(quotient[1, 0]) and zero(quotient[0, 0] - quotient[1, 1])

    # Antiholomorphic matrices: composition r_i r_j=H_i conjugate(H_j).
    c0 = (1 + ii) / 2
    refs = [
        sp.Matrix([[c0, 0], [1, -sp.conjugate(c0)]]),
        sp.Matrix([[-c0, 0], [1, sp.conjugate(c0)]]),
        sp.Matrix([[ii, 1 - ii], [0, 1]]),
        sp.Matrix([[ii, -1 + ii], [0, 1]]),
    ]
    be = b.subs(w, -1)
    apo = ke * a * ke.inv()
    bpo = ke * be * ke.inv()
    for physical, left, right in [
        (a, 2, 0), (be, 1, 2), (apo, 3, 0), (bpo, 1, 3), (ae, 1, 0)
    ]:
        check(projectively_equal(mm * physical * mm.inv(), refs[left] * sp.conjugate(refs[right])))

    gp = (mm * je * apo * mm.inv()).applyfunc(sp.simplify)
    gm = (mm * bpo * je.inv() * mm.inv()).applyfunc(sp.simplify)
    check(zero(gp - sp.Matrix([[3 * ii, 1 - ii], [1 + ii, -ii]])))
    check(zero(gm - sp.Matrix([[ii, 1 - ii], [-1 - ii, ii]])))
    for gamma, sources, targets in [
        (gp, [sp.oo, -1, -ii], [sp.oo, 1, ii]),
        (gm, [sp.oo, 1, ii], [sp.oo, -1, -ii]),
    ]:
        for source, target in zip(sources, targets):
            source_vector = sp.Matrix([1, 0]) if source is sp.oo else sp.Matrix([source, 1])
            mapped = (gamma * refs[0] * sp.conjugate(source_vector)).applyfunc(sp.simplify)
            check(zero(mapped[1]) if target is sp.oo else zero(mapped[0] - target * mapped[1]))

    # The oriented actual outer-pants boundary, independently of an aux flag.
    tt = sp.Matrix([[c0, -c0], [1, 0]])
    at = (tt * mm * a * mm.inv() * tt.inv()).applyfunc(sp.simplify)
    bt = (tt * mm * be * mm.inv() * tt.inv()).applyfunc(sp.simplify)
    aat = (tt * mm * ae * mm.inv() * tt.inv()).applyfunc(sp.simplify)
    check(zero(at - sp.Matrix([[-1, 0], [-2, -1]])))
    check(zero(bt - sp.Matrix([[-3, 2], [-2, 1]])))
    check(zero(aat - sp.Matrix([[-1, -2], [0, -1]])))
    for horocoordinate, parabolic in [
        (sp.Matrix([[0, -1], [1, 0]]), at),
        (sp.Matrix([[0, -1], [1, -1]]), bt),
    ]:
        check(zero(horocoordinate * parabolic * horocoordinate.inv() - sp.Matrix([[-1, 2], [0, -1]])))
    check(zero(aat.inv() * bt * at - eye))

    result = {
        "status": "PASS",
        "exact_symbolic_identity_checks": checks,
        "arithmetic": "SymPy exact rational functions and Gaussian rationals",
        "scope": "Bounded local signed threaded ports and complete cut-piece geometric anchor: all white and both shaded face maps, flags and inner peripheral matrices.",
        "not_claimed": "Global deformed stack/outer-collar peripheral map or a new filled quantum-volume theorem.",
    }
    out = Path(__file__).with_name("actual_belt_stack_regular_parabolic_port_chart_results.json")
    out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
