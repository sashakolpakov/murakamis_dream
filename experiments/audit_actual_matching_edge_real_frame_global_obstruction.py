#!/usr/bin/env python3
"""Audit the new local interface; global contradiction is a proved input."""
import argparse
import json
from pathlib import Path

import mpmath as mp
import sympy as sp


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path(__file__).with_name(
        "audit_actual_matching_edge_real_frame_global_obstruction_results.json"))
    args = parser.parse_args()
    count = {"exact_matrix_and_trace_identities": 0, "actual_inverse_turn_frames": 0,
             "original_selected_strip_flags": 0, "normalized_original_factors": 0}

    def zero(x):
        assert sp.factor(x) == 0, sp.factor(x)
        count["exact_matrix_and_trace_identities"] += 1

    A = sp.Matrix([[-1, -1], [0, -1]])
    B = sp.Matrix([[-1, 0], [4, -1]])
    F = sp.Matrix([[0, 1], [2, 1]])
    H, z, w = sp.symbols("H z w")
    Ae = F*A*F.inv()
    Pe = F*B*A*F.inv()
    C = sp.eye(2)-sp.I*H*(B*A+sp.eye(2))/2
    Ao = C*A*C.inv()
    Aoe = F*Ao*F.inv()
    for actual, expected in ((Ae, sp.Matrix([[-1, 0], [-2, -1]])),
                             (Pe, sp.Matrix([[-1, -2], [0, -1]])),
                             (Aoe, sp.Matrix([[-1-2*sp.I*H, -2*H*H],
                                              [-2, -1+2*sp.I*H]]))):
        for x in actual-expected:
            zero(x)
    Pi = sp.Matrix([[z, -z*w], [1, -w]])/(z-w)
    zero(sp.trace(Pe*Pi)+1+2/(z-w))
    zero(sp.trace(Ae*Pi)+1-2*z*w/(z-w))
    zero(sp.trace((Aoe-Ae)*Pi)-(-2*H*H-2*sp.I*H*(z+w))/(z-w))
    q = sp.symbols("q", nonzero=True)
    rho = (q+1/q)/2
    zero(-2/(1+q**-2)+q/rho)
    ee = sp.symbols("e", nonzero=True)
    delta = -q/rho
    total = sp.I*H+(1/ee-ee)/(2*sp.I*H*rho)
    zero((-2*H*H-2*sp.I*H*total)/delta-(1/ee-ee)/q)

    mp.mp.dps = 75
    tol = mp.mpf("1e-63")
    worst = mp.mpf(0)

    def close(x, y=0):
        nonlocal worst
        er = abs(x-y)
        worst = max(worst, er)
        assert er < tol, er

    def trace(M):
        return M[0, 0]+M[1, 1]

    A = mp.matrix([[-1, -1], [0, -1]])
    B = mp.matrix([[-1, 0], [4, -1]])
    F = mp.matrix([[0, 1], [2, 1]])
    for S in (mp.mpf(".1"), mp.mpf(".4"), mp.mpf(".8"),
              mp.mpf("1.2"), mp.mpf(2), mp.mpf(4)):
        k = S*S
        H = mp.sqrt(1+k)
        C = mp.eye(2)-1j*H*(B*A+mp.eye(2))/2
        Ao, Bo = C*A*C**-1, C*B*C**-1
        T = B**-1*Bo
        lower = -1/mp.sqrt(k+2)
        upper = min(mp.mpf(1), k+1-mp.sqrt(k+2))
        for fraction in (mp.mpf(".2"), mp.mpf(".5"), mp.mpf(".8")):
            c0 = lower+fraction*(upper-lower)
            tau = mp.acos(-c0)/mp.pi
            rho = (-mp.sqrt(k+2)-c0)/(1+k)
            alpha = mp.acos(rho)
            distance = 1-alpha/mp.pi
            u, v = (tau-distance)/2, (tau+distance)/2
            original_total = 1-distance
            assert mp.mpf(".5") < original_total < 1
            assert 0 < u < v < tau < 1
            assert 0 < u < original_total and 0 < 1-v < original_total
            for order in (-1, 1):
                q = mp.exp(order*1j*alpha)
                for adapter in (-1, 1):
                    e = mp.exp(adapter*1j*mp.pi*tau)
                    difference = -q/rho
                    total = 1j*H+(1/e-e)/(2j*H*rho)
                    z, w = (total+difference)/2, (total-difference)/2
                    assert 0 < mp.im(z) < H and 0 < mp.im(w) < H
                    close(mp.im(z)+mp.im(w), H)
                    count["original_selected_strip_flags"] += 2
                    proj_eta = mp.matrix([[z, -z*w], [1, -w]])/(z-w)
                    proj = F**-1*proj_eta*F
                    close(trace(proj), 1)
                    close(mp.det(proj), 0)
                    close(trace(A*proj), e/q)
                    close(trace(Ao*proj), 1/(e*q))
                    close(trace(B*A*proj), q**-2)
                    target = Ao*proj/trace(Ao*proj)
                    close(trace(T*target), e*e)
                    close(trace(Ao**-1*target)/e, q)
                    close(trace(Bo*target)/e, 1/q)
                    count["actual_inverse_turn_frames"] += 1

                    # Test the ORIGINAL physical coordinates, and only
                    # then apply their low/high adapter. Both target
                    # adapters and both input/output orientations occur.
                    phys_total = q*q
                    for value in (-q/e, -q*e):
                        normalized_u = value if order == 1 else value/phys_total
                        normalized_t = phys_total if order == 1 else 1/phys_total
                        close(normalized_t, mp.exp(2j*mp.pi*original_total))
                        err = min(abs(normalized_u-mp.exp(2j*mp.pi*u)),
                                  abs(normalized_u-mp.exp(2j*mp.pi*(1-v))))
                        close(err)
                        count["normalized_original_factors"] += 1

    result = {"status": "PASS", **count, "max_numeric_error": str(worst),
              "scope": "new actual local strip/adapter interface; global polar obstruction is an independently proved input"}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
