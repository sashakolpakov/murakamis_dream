#!/usr/bin/env python3
"""Independent normalization checks for the free pair-edge packet.

Exact symbolic identities and finite Barnes-product sampling are checked.
Finite Newton sums versus the proved asymptotic are diagnostics only.
"""
import argparse
import hashlib
import json
from pathlib import Path

import mpmath as mp
import sympy as sp

from audit_exact_factorial_interpolation import sine_factorial


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def encode(z):
    return {"real": mp.nstr(mp.re(z), 32),
            "imaginary": mp.nstr(mp.im(z), 32)}


def primitive(z):
    return ((mp.polylog(2, mp.exp(2j*mp.pi*z))-mp.pi**2/6)
            *1j/(2*mp.pi)+1j*mp.pi*(z-z*z)/2)


def phase(y, t, u):
    def one(v):
        return (-primitive(mp.mpf(".5")-y+v/(2*mp.pi))
                -primitive(mp.mpf(".5")-y-v/(2*mp.pi))
                -2*primitive(y))
    return one(t)+one(u)


def newton_rows(level, angle):
    z = -2*mp.cos(angle)
    values, normals = [mp.mpc(1)], [mp.mpc(0)]
    for j in range(1, level):
        denominator = 4*mp.sin(mp.pi*j/level)**2
        factor = (2*mp.cos(mp.pi*(2*j-1)/level)-z)/denominator
        normals.append(factor*normals[-1]-values[-1]/denominator)
        values.append(factor*values[-1])
    return values, normals


def barnes_sample(level, j, angle):
    plus = mp.mpf(level-1)/2-j+level*angle/(2*mp.pi)
    minus = mp.mpf(level-1)/2-j-level*angle/(2*mp.pi)
    return level/(sine_factorial(level, plus)
                  *sine_factorial(level, minus)*sine_factorial(level, j)**2)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=100)
    parser.add_argument("--output", default="repro/results/research-pair-free-boundary-kernel.json")
    args = parser.parse_args()
    mp.mp.dps = args.precision
    root = Path(__file__).resolve().parents[1]
    tolerance = mp.power(10, -args.precision//2)
    maximum = mp.mpf(0)
    comparisons = 0

    def check(left, right):
        nonlocal maximum, comparisons
        error = abs(left-right)/max(1, abs(left), abs(right))
        maximum = max(maximum, error)
        comparisons += 1
        assert error < tolerance, (left, right, error)

    a, b, v = sp.symbols("a b v", real=True)
    aa = a+sp.I*b
    identity = ((a*a+b*b)*v**4
                -(1-(1-aa)*v)*(1-(1-sp.conjugate(aa))*v)
                -(v-1)*((a*a+b*b)*(v**3+v**2)+(2*a-1)*v+1))
    assert sp.expand(identity) == 0
    c, r = sp.symbols("c r", nonzero=True)
    ratio = (1-(1-c*c)*r*r)/(c*c*r**4)
    tangent = c/(sp.pi*(1+c*c*r*r))
    assert sp.simplify(ratio.subs(r, 1)-1) == 0
    assert sp.simplify((tangent*sp.diff(ratio, r)).subs(r, 1)+2/(sp.pi*c)) == 0
    assert sp.simplify((-2/(sp.pi*c))/(tangent.subs(r, 1)**2)
                       +2*sp.pi*(1+c*c)**2/c**3) == 0
    cc = a+sp.I*b
    quotient = sp.expand(cc*(v+sp.conjugate(cc)**2))
    assert sp.simplify(sp.re(quotient)-a*(v+a*a+b*b)) == 0
    assert sp.simplify(sp.im(quotient)-b*(v-a*a-b*b)) == 0
    symbolic_checks = 6

    # Finite Barnes G product is independent of the Newton recurrence.
    angles = [mp.mpc("1.5", "-.96"), mp.mpc(".01", ".003")]
    for level in (2, 3, 6, 7, 8, 9):
        for angle in angles:
            values, normals = newton_rows(level, angle)
            for j in range(level):
                check(barnes_sample(level, j, angle), values[j])
            for j in sorted({0, level//2, level-1}):
                derivative = mp.diff(lambda z: barnes_sample(level, j, z), angle)
                check(derivative/(2*mp.sin(angle)), normals[j])
            top = mp.mpf(level-1)/2+level*angle/(2*mp.pi)
            check(sine_factorial(level, top)*sine_factorial(level, level-1-top), level)

    examples = [
        (mp.mpc("1.5", "-.96"), mp.mpc(".01", ".003")),
        (mp.mpc("1.2", "-.5"), mp.mpc("-.012", ".004")),
        (mp.mpc(".7", "-.15"), mp.mpc(".008", "-.003")),
    ]
    diagnostics = []
    for index, (t, u) in enumerate(examples):
        C = mp.cos(t/2)
        assert 0 < mp.re(t) < mp.pi/2 and 0 < -mp.im(t) < mp.mpf("1.07")
        assert abs(C) < 1 and mp.re(C*C) > mp.mpf(".5")
        y = mp.acos((1-mp.cos(t)*mp.cos(u))/(2+mp.cos(t)+mp.cos(u)))/(2*mp.pi)
        selected = phase(y, t, u)
        hessian = -mp.pi*(
            mp.tan(mp.pi*y+t/2)+mp.tan(mp.pi*y-t/2)
            +mp.tan(mp.pi*y+u/2)+mp.tan(mp.pi*y-u/2)
            +4/mp.tan(mp.pi*y))
        check(mp.diff(lambda z: phase(z, t, u), y), 0)
        check(mp.diff(lambda z: phase(z, t, u), y, 2), hessian)
        amplitude = mp.sqrt(2*mp.pi)/(4*mp.sin(mp.pi*y)**2*mp.sqrt(-hessian))
        for level in (32, 33, 64, 65, 128, 129):
            first, _ = newton_rows(level, t)
            second, _ = newton_rows(level, u)
            low_end = level-1-level//2
            full = mp.fsum(first[j]*second[j] for j in range(level))
            low = mp.fsum(first[j]*second[j] for j in range(low_end+1))
            predicted = level**(-mp.mpf("1.5"))*amplitude*mp.exp(level*selected)
            diagnostics.append({
                "example": index, "N": level, "t": encode(t), "u": encode(u),
                "saddle": encode(y), "phase": encode(selected),
                "amplitude": encode(amplitude), "full_ratio": encode(full/predicted),
                "low_ratio": encode(low/predicted),
                "N_times_full_relative_error": mp.nstr(level*abs(full/predicted-1), 24),
                "radical_over_packet": encode((full-low)/predicted),
            })

    dependencies = [root/"experiments/audit_exact_factorial_interpolation.py"]
    proof = root/"notes/research_pair_free_boundary_kernel.md"
    record = {
        "status": "passed",
        "precision_decimal": args.precision,
        "symbolic_identities": symbolic_checks,
        "finite_sampling_normal_and_phase_identities": comparisons,
        "maximum_relative_identity_error": mp.nstr(maximum, 32),
        "packet_diagnostics_not_proof": diagnostics,
        "script_sha256": digest(Path(__file__).resolve()),
        "proof_sha256": digest(proof),
        "dependencies": {str(path.relative_to(root)): digest(path) for path in dependencies},
        "versions": {"mpmath": mp.__version__, "sympy": sp.__version__},
        "scope": "Finite identities and normalization diagnostics; the uniform contour proof is in the note.",
    }
    output = Path(args.output)
    if not output.is_absolute():
        output = root/output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(record, indent=2)+"\n")
    print(f"Passed {symbolic_checks} symbolic and {comparisons} finite identities; "
          f"max relative error {mp.nstr(maximum, 8)}.")
    print(f"Recorded {len(diagnostics)} packet diagnostics (not asymptotic proof).")
    print(f"Result: {output}")


if __name__ == "__main__":
    main()
