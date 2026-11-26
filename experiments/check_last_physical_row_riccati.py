#!/usr/bin/env python3
"""Original finite-row checks for Riccati transport to the physical endpoint."""
import argparse
import hashlib
import json
from pathlib import Path

import mpmath as mp

from check_physical_row_riccati_transport import direct_rows, relative


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=120)
    args = parser.parse_args()
    assert args.precision >= 100
    mp.mp.dps = args.precision
    tol = mp.power(10, -args.precision//3)
    rows = []
    counts = {"original_recurrence": 0, "coefficient_identity": 0,
              "barrier": 0, "odd_complete_identity": 0}
    max_error = mp.mpf(0)
    for n in (16, 17, 32, 33, 64, 65, 128, 129):
        theta, last, start = mp.pi/n, (n-1)//2, n//4
        sine = lambda r: 2*mp.sin(r*theta)
        c0 = 2*mp.cos(theta)
        aa = [sine(r+1)**4/(sine(2*r+1)*sine(2*r+2))
              for r in range(last)]
        qq = [None]+[mp.cos(r*theta)/mp.sin(r*theta)**3
                     for r in range(1, last+1)]
        for w in (mp.mpc(-2), mp.mpc("-0.7", "0.9"),
                  mp.mpc("1.7", "0.3"), mp.mpc("0.5", "-2.598076211353316")):
            values = direct_rows(n, w, last)
            ratios = [None]+[values[r]/values[r-1] for r in range(1, last+1)]
            error = relative(ratios[1], 1+(c0-w)/aa[0])
            lower_b = mp.sin(start*theta)**4/2
            barrier_c = min(
                mp.sqrt((c0-w.real)*lower_b)/2,
                (ratios[start].real-1)/(2*qq[start]))
            assert barrier_c > 0
            largest_h_error = mp.mpf(0)
            largest_defect = mp.mpf(0)
            for r in range(1, last):
                cc = sine(r)**4/(sine(2*r)*sine(2*r+1))
                q, d = cc/aa[r], (c0-w)/aa[r]
                predicted = 1+d+q*(1-1/ratios[r])
                error = max(error, relative(predicted, ratios[r+1]))
                counts["original_recurrence"] += 1
                if r >= start:
                    b = mp.sin(r*theta)**3*mp.sin((2*r+1)*theta)/(2*mp.cos(r*theta))
                    error = max(error, relative(q, qq[r+1]/qq[r]),
                                relative(1/aa[r], b*qq[r]*qq[r+1]))
                    assert lower_b-tol <= b <= 1+tol
                    assert ratios[r+1].real-1 >= barrier_c*qq[r+1]-tol
                    counts["coefficient_identity"] += 2
                    counts["barrier"] += 1
                    lam = mp.exp(2*mp.asinh(mp.sqrt(2-w)*mp.cot(r*theta)/2))
                    nxt = mp.exp(2*mp.asinh(mp.sqrt(2-w)*mp.cot((r+1)*theta)/2))
                    largest_h_error = max(
                        largest_h_error, (mp.mpf(n)/2-r)*abs(ratios[r]-lam))
                    largest_defect = max(
                        largest_defect, n*abs(1+d+q*(1-1/lam)-nxt))
            logarithm = mp.fsum(mp.log(v) for v in ratios[1:])
            endpoint = mp.mpf(last)/n
            def regularized(x):
                if x == 0:
                    return mp.log(2-w)-2*mp.log(mp.pi)
                return 2*mp.asinh(mp.sqrt(2-w)*mp.cot(mp.pi*x)/2)+2*mp.log(x)
            action = (mp.quad(regularized, [0, endpoint])
                      -2*endpoint*(mp.log(endpoint)-1))
            error = max(error, relative(mp.exp(logarithm), values[last]))
            if n % 2:
                ew = em = mp.mpf(1)
                terms = [mp.mpf(1)]
                for j in range(1, last+1):
                    node = 2*mp.cos((2*j-1)*theta)
                    ew *= (node-w)/sine(j)**2
                    em *= (node+2)/sine(j)**2
                    terms.append(ew*em)
                complete = mp.fsum(terms)  # All higher terms are exactly zero.
                error = max(error, relative(complete, values[last]))
                counts["odd_complete_identity"] += 1
            assert error < tol, (n, w, error)
            max_error = max(max_error, error)
            rows.append({
                "N": n, "w": [mp.nstr(w.real, 18), mp.nstr(w.imag, 18)],
                "last_physical_row": last,
                "maximum_identity_error": mp.nstr(error, 20),
                "positive_barrier_constant": mp.nstr(barrier_c, 20),
                "h_times_ratio_error_diagnostic": mp.nstr(largest_h_error, 20),
                "N_times_local_defect_diagnostic": mp.nstr(largest_defect, 20),
                "logarithmic_error_over_log_N_diagnostic": [
                    mp.nstr((logarithm-n*action).real/mp.log(n), 20),
                    mp.nstr((logarithm-n*action).imag/mp.log(n), 20)],
            })
    here = Path(__file__).resolve()
    root = here.parents[1]
    dependencies = [
        here,
        here.with_name("check_physical_row_riccati_transport.py"),
        root/"notes/research_last_physical_row_riccati.md",
        root/"notes/research_physical_row_riccati_transport.md",
    ]
    result = {
        "status": "passed", "precision_decimal": args.precision,
        "counts": counts, "source_cases": len(rows),
        "maximum_identity_error": mp.nstr(max_error, 20),
        "sha256": {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
                   for p in dependencies},
        "records": rows,
        "scope": "Finite identities and barriers; asymptotic columns are diagnostics.",
    }
    output = root/"repro/results/research-last-physical-row-riccati.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({k: result[k] for k in (
        "status", "precision_decimal", "counts", "source_cases", "maximum_identity_error")}))


if __name__ == "__main__":
    main()
