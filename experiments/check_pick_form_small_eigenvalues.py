#!/usr/bin/env python3
"""Check constants and finite moment cancellation for the crossing Pick form.

The exponential eigenvalue bound is proved in the accompanying note.
These checks do not infer an asymptotic from numerical eigenvalues.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

import mpmath as mp


def main():
    root = Path(__file__).resolve().parents[1]
    mp.mp.dps = 100
    constants = []

    def less(name, left, right):
        assert left < right, name
        constants.append({"name": name, "left": str(left), "right": str(right)})

    # Classical 3 < pi < 22/7, and e < 3, suffice for these comparisons.
    less("Taylor radius ratio", F(22, 7)**2/F(256), F(1, 16))
    less("analytic derivative bound", 1/(1-F(1, 4096)), F(2))
    less("quadratic-form prefactor", F(16, 15)**2/F(3), F(1))
    less("positive exponential correction", F(1, 3), F(1))
    less("logarithmic decay: e squared < 16", F(9), F(16))

    cases = []
    worst = mp.mpf(0)
    moment_checks = 0
    for N, k in ((64, 3), (128, 5), (256, 8)):
        m = N//2
        indices = list(range(m-k, m))
        nodes = [2*mp.cos((2*a+1)*mp.pi/N) for a in indices]
        shifted = [x+2 for x in nodes]
        sigma = [2*(-1)**a*mp.sin((2*a+1)*mp.pi/N) for a in indices]
        vector = [1/(sigma[a]*mp.fprod(shifted[a]-shifted[b]
                                      for b in range(k) if b != a))
                  for a in range(k)]
        norm = mp.sqrt(mp.fsum(abs(v)**2 for v in vector))
        vector = [(-1)**(m-k)*v/norm for v in vector]
        assert all(v > 0 for v in vector)
        for j in range(k-1):
            moment = mp.fsum(vector[a]*sigma[a]*shifted[a]**j for a in range(k))
            scale = mp.fsum(abs(vector[a]*sigma[a])*shifted[a]**j
                           for a in range(k))
            error = abs(moment)/scale
            worst = max(worst, error)
            assert error < mp.mpf("1e-85")
            moment_checks += 1

        radius = mp.mpf(1)/2
        height = max(shifted)
        ratio = height/radius
        assert ratio < 1
        for n in (1, 3, 10):
            kappa = n*N/(4*mp.pi)
            phase = [kappa*mp.acos(-x/2)**2 for x in nodes]
            matrix = mp.matrix(k)
            for a in range(k):
                for b in range(k):
                    if a == b:
                        core = (kappa*mp.acos(-nodes[a]/2)
                                /mp.sqrt(1-nodes[a]**2/4))
                    else:
                        core = (1-mp.exp(1j*(phase[b]-phase[a])))/(1j*(nodes[a]-nodes[b]))
                    matrix[a, b] = sigma[a]*sigma[b]*core
            vv = mp.matrix(vector)
            raw_rayleigh = (vv.T*matrix*vv)[0]
            assert abs(mp.im(raw_rayleigh)) < mp.mpf("1e-85")
            rayleigh = mp.re(raw_rayleigh)
            bound = (8*k*kappa*mp.exp(4*kappa*radius)
                     *ratio**(2*k-2)/(1-ratio)**2)
            assert 0 < rayleigh <= bound
            cases.append({
                "N": N, "power": n, "number_of_nodes": k,
                "rayleigh_quotient": mp.nstr(rayleigh, 35),
                "analytic_tail_bound": mp.nstr(bound, 35),
                "scope": "finite moment construction; not an eigenvalue asymptotic",
            })

    # The floor inequality used in the proof, including every fractional case
    # on this rational grid. Its general proof is floor(x) >= x-1 for x >= 4.
    for denominator in range(1, 18):
        for numerator in range(4*denominator, 20*denominator):
            x = F(numerator, denominator)
            assert 2*(numerator//denominator)-2 >= x

    dependencies = (
        "experiments/check_pick_form_small_eigenvalues.py",
        "notes/research_pick_form_small_eigenvalues.md",
        "notes/research_trace_normal_defect_positive_form.md",
    )
    record = {
        "status": "passed", "precision_digits": mp.mp.dps,
        "scope": "Exact scalar comparisons and finite weighted-moment cancellation",
        "rational_comparisons": constants, "moment_checks": moment_checks,
        "maximum_relative_moment_error": mp.nstr(worst, 35),
        "finite_rayleigh_checks": cases,
        "sha256": {name: hashlib.sha256((root/name).read_bytes()).hexdigest()
                   for name in dependencies},
    }
    output = root/"repro/results/research-pick-form-small-eigenvalues.json"
    output.write_text(json.dumps(record, indent=2)+"\n")
    print(json.dumps({"status": "passed", "moment_checks": moment_checks,
                      "rayleigh_checks": len(cases),
                      "maximum_relative_moment_error": record["maximum_relative_moment_error"],
                      "record": str(output.relative_to(root))}))


if __name__ == "__main__":
    main()
