#!/usr/bin/env python3
"""Replay the retained-boundary identities for a run of powers minus two.

The general proof is Section 11 of research_negative_two_chain_original_periods.
Symbolic and high-precision checks below supplement that proof. They do not
assert positivity of the original cells or a quantum asymptotic.
"""

import argparse
import hashlib
import json
from pathlib import Path
import platform

import mpmath as mp
import sympy as sp


def exact_checks():
    lam, a, b = sp.symbols("lambda A B")
    count = 0
    for length in range(2, 21):
        u = sp.chebyshevu(length - 1, lam)
        v = sp.chebyshevu(length - 2, lam)
        t = sp.chebyshevt(length, lam)
        assert sp.expand(u*u + v*v - 2*lam*u*v - 1) == 0
        assert sp.expand(lam*u - v - t) == 0
        initial_conic_times_u2 = (
            lam*lam*u*u - 2*lam*a*(b+a*v)*u
            + a*a*u*u + (b+a*v)**2
        )
        eliminated = lam*lam*u*u + a*a + b*b - 2*a*b*t
        assert sp.expand(initial_conic_times_u2 - eliminated) == 0
        for j in range(1, length):
            def numerator(k):
                left = sp.chebyshevu(length-k-1, lam) if k < length else 0
                right = sp.chebyshevu(k-1, lam) if k else 0
                return a*left + b*right
            assert sp.expand(
                numerator(j+1)-2*lam*numerator(j)+numerator(j-1)
            ) == 0
        count += 1
    return count


def numerical_checks(precision):
    mp.mp.dps = precision
    tolerance = mp.power(10, -precision + 20)
    records = []
    left_angle = mp.mpc("-0.025", "-0.006")
    right_angle = mp.mpc("-0.018", "-0.004")
    a, b = mp.cos(left_angle/2), mp.cos(right_angle/2)

    def text(z):
        return mp.nstr(z, 35)

    for length in (2, 3, 4, 6, 9, 16):
        initial = mp.pi*(length-2j)/(length*length+4)
        beta0 = mp.findroot(
            lambda z: 2*mp.asinh(mp.tan(z))-1j*length*z+1j*mp.pi,
            initial, tol=tolerance/100,
        )
        beta = mp.findroot(
            lambda z: mp.asinh(a*mp.tan(z))+mp.asinh(b*mp.tan(z))
            -1j*length*z+1j*mp.pi,
            beta0, tol=tolerance/100,
        )
        lam = mp.cos(beta)
        u = mp.chebyu(length-1, lam)

        def U(index):
            return mp.chebyu(index, lam) if index >= 0 else mp.mpc(0)

        c = [(a*U(length-j-1)+b*U(j-1))/u for j in range(length+1)]
        angles = [left_angle] + [
            -2*mp.acos(c[j]) for j in range(1, length)
        ] + [right_angle]
        residuals = [
            abs(lam*lam*u*u+a*a+b*b-2*a*b*mp.chebyt(length, lam)),
            abs(c[0]-a), abs(c[-1]-b),
        ]
        edge_returns = []
        for j in range(length):
            q = 1j*(1-lam/(c[j]*c[j+1]))
            assert q.real > 0
            assert (q*c[j]).real > 0 and (q*c[j+1]).real > 0
            rv = mp.asinh(mp.tan(angles[j]/2)*c[j+1])
            rw = mp.asinh(mp.tan(angles[j+1]/2)*c[j])
            residuals.extend((
                abs(mp.cosh(rv)-q*c[j+1]),
                abs(mp.cosh(rw)-q*c[j]),
            ))
            edge_returns.append((rv, rw))
        for j in range(1, length):
            residuals.append(abs(
                edge_returns[j-1][1]+edge_returns[j][0]
                +1j*angles[j]+1j*mp.pi
            ))
        residuals.extend((
            abs(edge_returns[0][0]
                -mp.asinh(mp.tan(left_angle/2)*lam)+1j*left_angle/2),
            abs(edge_returns[-1][1]
                -mp.asinh(mp.tan(right_angle/2)*lam)+1j*right_angle/2),
        ))
        weighted = mp.fsum(mp.sin(mp.pi*j/length)*c[j]
                           for j in range(1, length))
        residuals.append(abs(
            2*(lam-mp.cos(mp.pi/length))*weighted
            -mp.sin(mp.pi/length)*(a+b)
        ))
        assert all(z.real > 0 and z.imag < 0 for z in c)
        assert lam.real > mp.cos(mp.pi/length)
        assert max(residuals) < tolerance
        records.append({
            "L": length,
            "left_angle": text(left_angle),
            "right_angle": text(right_angle),
            "selected_reduced_beta": text(beta),
            "lambda": text(lam),
            "maximum_period_and_return_residual": text(max(residuals)),
            "gap_from_largest_Dirichlet_eigenvalue":
                text(lam.real-mp.cos(mp.pi/length)),
        })

    # Exact degenerate reduced center: the old run remains regular.
    length = 5
    c = [mp.mpc(1, -j) for j in range(length+1)]
    angles = [-2*mp.acos(z) for z in c]
    returns = []
    for j in range(length):
        q = 1j*(1-1/(c[j]*c[j+1]))
        assert q.real > 0 and (q*c[j]).real > 0 and (q*c[j+1]).real > 0
        returns.append((
            mp.asinh(mp.tan(angles[j]/2)*c[j+1]),
            mp.asinh(mp.tan(angles[j+1]/2)*c[j]),
        ))
    exceptional_residual = max(abs(
        returns[j-1][1]+returns[j][0]+1j*angles[j]+1j*mp.pi
    ) for j in range(1, length))
    assert exceptional_residual < tolerance
    return records, {
        "lambda": "1",
        "C_j": "1-i*j",
        "L_checked": length,
        "original_period_residual": text(exceptional_residual),
        "reduced_angle": "0",
        "principal_reduced_charge_residual": "pi",
        "meaning": (
            "The original run is regular, but this reduced zero angle is "
            "not the selected primitive-charge-one isolated saddle."
        ),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=90)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    symbolic_count = exact_checks()
    records, exception = numerical_checks(args.precision)
    result = {
        "status": "passed",
        "scope": (
            "Checks of exact retained-boundary algebra and calibrated original "
            "periods. No original-cell positivity or quantum asymptotic claim."
        ),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "versions": {
            "python": platform.python_version(),
            "mpmath": mp.__version__,
            "sympy": sp.__version__,
        },
        "symbolic_lengths_checked": symbolic_count,
        "symbolic_L_range": [2, 20],
        "precision_decimal_digits": args.precision,
        "selected_branch_checks": records,
        "reduced_chart_exception": exception,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print(f"Verified {symbolic_count} symbolic lengths and {len(records)} boundary germs.")
    print(f"Saved {args.output}")


if __name__ == "__main__":
    main()
