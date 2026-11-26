#!/usr/bin/env python3
"""Exploratory maxima for the remaining two-selection profile functions.

This uses midpoints of eight previously certified reference enclosures.
The midpoints need not themselves solve the original stationary equations.
Double precision optimization is diagnostic only: neither a uniform bound
nor a new certificate for the quantum source is asserted.
"""
import argparse
from fractions import Fraction
import hashlib
import itertools
import json
from pathlib import Path

import numpy as np
from scipy.optimize import minimize
from scipy.special import spence

ROOT = Path(__file__).resolve().parents[1]
BANK = ROOT / "repro/results/research-mixed-second-selected-boundary-reference-bank.json"
BANK_SHA = "3e6e227ac78afcf214844376f7f0069259a4c3f0e7a9a755a6a57a8081a24bbb"
H = .01
P = (.22, .45)
NAMES = ("e", "a", "u", "z", "v", "b")


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def bounds(item):
    return tuple(float(Fraction(item[k])) for k in ("lower_rational", "upper_rational"))


def coordinate(item):
    return complex(sum(bounds(item["real"]))/2, sum(bounds(item["imag"]))/2)


def width(row):
    return max(hi-lo for item in row["coordinates"].values()
               for part in ("real", "imag") for lo, hi in [bounds(item[part])])


def g(z):
    return (spence(1-np.exp(-2j*np.pi*z))-np.pi**2/6)/(2j*np.pi)


def gp(z):
    return np.log(1-np.exp(-2j*np.pi*z))


def J(z):
    return g(z)-.5j*np.pi*z*(1-z)


def jp(z):
    return gp(z)-.5j*np.pi*(1-2*z)


def auxiliary(e):
    return np.arctan((1j+np.sqrt(1-2*np.exp(2j*np.pi*e)))/2)/np.pi


def cap(e, a):
    xi = auxiliary(e)
    action = -2*J(.5-xi)-3*J(xi)-J(e-xi)+1j*np.pi*e*xi
    value = action+J(e+a)-J(a)-1j*np.pi*e*a-g(e)
    derivative_e = -jp(e-xi)+1j*np.pi*xi+jp(e+a)-1j*np.pi*a-gp(e)
    derivative_a = jp(e+a)-jp(a)-1j*np.pi*e
    return value, derivative_e, derivative_a


def ordinary(s, a, b, beta):
    value = g(s+a)+g(s+b)-(2+beta)*g(s)-g(a)-g(b)+2j*np.pi*a*s
    return (value, gp(s+a)+gp(s+b)-(2+beta)*gp(s)+2j*np.pi*a,
            gp(s+a)-gp(a)+2j*np.pi*s, gp(s+b)-gp(b))


def original_phase(q, beta):
    e, a, u, z, v, b = q
    ce, q2, q3 = cap(e, a), ordinary(u, a, z, 1), ordinary(v, z, b, beta)
    value = ce[0]+q2[0]+q3[0]-g(a)-g(z)-beta*g(b)/2
    gradient = np.array((ce[1], ce[2]+q2[2]-gp(a), q2[1],
                         q2[3]+q3[2]-gp(z), q3[1], q3[3]-beta*gp(b)/2))
    return value, gradient


def objective(x, r, beta, cap_kind, right_kind, nu1, nu2):
    q = np.array(x, dtype=complex)+1j*r.imag
    q[1], q[3] = x[1]+1j*H, x[3]+1j*H
    if cap_kind == "left":
        q[0] = .27+0j
    if right_kind == "half":
        q[4] = .5+0j
    value, gradient = original_phase(q, beta)
    ref, ref_gradient = original_phase(r, beta)
    p = ref_gradient[-1]
    value -= ref+p*(q[-1]-r[-1])
    gradient[-1] -= p
    for index, nu in ((1, nu1), (3, nu2)):
        value += (1-nu)*g(q[index])-2*np.pi*H*nu
        gradient[index] += (1-nu)*gp(q[index])
    if cap_kind == "left":
        gradient[0] = 0
    if right_kind == "half":
        gradient[4] = 0
    return -float(value.real), -gradient.real


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    if sha(BANK) != BANK_SHA:
        raise ValueError("changed certified bank")
    rows = json.loads(BANK.read_text())["accepted_references"]
    picked = []
    for beta, domain in itertools.product((0, 1), ("k3", "k4")):
        group = [r for r in rows if r["beta"] == beta and r["external_domain"] == domain]
        picked.extend((("smallest enclosure", min(group, key=width)),
                       ("smallest saved single-selection gap",
                        min(group, key=lambda r: Fraction(r["certified_central_gap_lower_rational"])))))
    results = []
    for selection, row in picked:
        beta = row["beta"]
        r = np.array([coordinate(row["coordinates"][name]) for name in NAMES])
        ref, gradient = original_phase(r, beta)
        source = {
            "selection": selection, "beta": beta, "external_domain": row["external_domain"],
            "source_node_index": row["source_node_index"],
            "source_payload_sha256": row["compact_payload_canonical_sha256"],
            "max_coordinate_enclosure_width": width(row),
            "reference_midpoints": {name: [float(z.real), float(z.imag)] for name, z in zip(NAMES, r)},
            "internal_stationary_residual_max": float(np.max(np.abs(gradient[:-1]))),
            "reference_action_real": float(ref.real), "profiles": [],
        }
        for cap_kind, right_kind, nu1, nu2 in itertools.product(
                ("main", "left"), ("main", "half") if beta == 0 else ("main",), (0, 1), (0, 1)):
            box = [(.27, .49), P, (.125, .5), P, ((.15 if beta == 0 else .125), .5), P]
            if cap_kind == "left":
                box[0] = (.27, .27)
            if right_kind == "half":
                box[4] = (.5, .5)
            x0 = np.clip(r.real, [x[0] for x in box], [x[1] for x in box])
            fixed = (r, beta, cap_kind, right_kind, nu1, nu2)
            opt = minimize(objective, x0, args=fixed, jac=True, bounds=box, method="L-BFGS-B",
                           options={"ftol": 1e-14, "gtol": 1e-10, "maxiter": 200, "maxls": 40})
            # Compare the implemented gradient with centered differences at a
            # fixed interior test, not merely at a possibly constrained optimum.
            test = np.array([(lo+hi)/2 for lo, hi in box])
            grad = objective(test, *fixed)[1]
            errors = []
            for j, (lo, hi) in enumerate(box):
                if lo == hi:
                    continue
                step = np.zeros(6)
                step[j] = 1e-6
                diff = (objective(test+step, *fixed)[0]-objective(test-step, *fixed)[0])/2e-6
                errors.append(abs(float(diff-grad[j])))
            source["profiles"].append({
                "cap": cap_kind, "right": right_kind, "nu1": nu1, "nu2": nu2,
                "optimizer_success": bool(opt.success), "optimizer_message": str(opt.message),
                "iterations": int(opt.nit), "evaluations": int(opt.nfev),
                "candidate_maximum": float(-opt.fun), "candidate_targets": opt.x.tolist(),
                "gradient_difference_error_max": max(errors),
            })
        results.append(source)
    result = {
        "status": "exploratory midpoint optimizations; no certified inequalities",
        "scope": "original D16/D8 remaining profiles at eight prescribed enclosure midpoints",
        "bank_sha256": BANK_SHA, "script_sha256": sha(Path(__file__)),
        "height": H, "new_roots": 0, "finite_quantum_sums": 0,
        "warning": "Midpoints are not asserted stationary; numerical maxima are not upper bounds.",
        "references": results,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    profiles = [p for row in results for p in row["profiles"]]
    print(json.dumps({"references": len(results), "profiles": len(profiles),
                      "all_optimizers_successful": all(p["optimizer_success"] for p in profiles),
                      "largest_candidate": max(p["candidate_maximum"] for p in profiles),
                      "max_gradient_error": max(p["gradient_difference_error_max"] for p in profiles)}))


if __name__ == "__main__":
    main()
