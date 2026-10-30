#!/usr/bin/env python3
"""Exact new flag identities used by the selected-factor corollary.

The global continuation, side exclusion and prescribed-pair geometry are
analytical consequences of separately audited inputs. These identities
do not constitute another amplitude or global-frame numerical test.
"""
import json
from pathlib import Path

import sympy as sp


def main():
    U, T, S = sp.symbols("U T S")
    Delta = U * (T + 1 - U) / T
    W = 1 - (T + 1) / U
    A = sp.Matrix([[-1, -1], [0, -1]])
    P = sp.Matrix([[1, 1], [-4, -3]])
    counts = dict(adapter_cases=0, root_branches=0,
                  exact_original_head_identities=0,
                  exact_prefix_trace_identities=0,
                  exact_discriminant_identities=0,
                  exact_sheet_involutions=0)

    def zero(expr):
        numerator = sp.cancel(expr).as_numer_denom()[0]
        remainder = sp.rem(sp.Poly(numerator, S), sp.Poly(S*S-Delta, S))
        assert sp.cancel(remainder.as_expr()) == 0

    zero(Delta + U*U*W/T)
    counts["exact_discriminant_identities"] += 1
    low_triple = sp.Matrix([1, -1/U, 1/T])
    high_triple = sp.Matrix([1, -T/U, T])
    assert sp.simplify(high_triple-T*sp.Matrix(list(reversed(low_triple)))) == sp.zeros(3, 1)

    for up, tp in ((U, T), (U/T, 1/T)):
        zero(up*(tp+1-up)/tp-Delta)
        counts["exact_discriminant_identities"] += 1
        branches = []
        for sign in (-1, 1):
            w = (-1+sign*S)/(2*(1-up))
            z = w+up/(1-up)
            zero((z-w)/(z-w+1)-up)
            zero((z-w)/(4*w*z+3*w+z+1)-tp)
            counts["exact_original_head_identities"] += 2
            frame = sp.Matrix([[z, -z*w], [1, -w]])/(z-w)
            for actual, expected in ((sp.trace(frame), 1),
                                     (sp.trace(A*frame), -1/up),
                                     (sp.trace(P*frame), 1/tp)):
                zero(actual-expected)
                counts["exact_prefix_trace_identities"] += 1
            zero(frame.det())
            zero(4*(1-up)*w*w+4*w+1-up/tp)
            branches.append((z, w))
            counts["root_branches"] += 1
        zm, wm = branches[0]
        zp, wp = branches[1]
        zero(zm+wp+1)
        zero(wm+zp+1)
        counts["exact_sheet_involutions"] += 2
        counts["adapter_cases"] += 1

    result = dict(status="PASS", exact=counts,
                  scope="Exact low/high original-head, prefix-trace, discriminant and sheet identities. Continuation and prescribed-pair localization are analytical; no new amplitude or cycle test.")
    destination = Path(__file__).with_name("actual_augmented_plat_selected_factor_localization_results.json")
    destination.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
