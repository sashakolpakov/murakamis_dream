#!/usr/bin/env python3
"""Finite diagnostics for the complete first-normal/first-normal sector.

These data are not an asymptotic proof or a certificate of a contributing
complex saddle. Every finite source value uses the exact formula (5).
"""
import hashlib
import json
from pathlib import Path

import mpmath as mp

from check_physical_row_riccati_transport import direct_rows


def main():
    mp.mp.dps=140
    root=Path(__file__).resolve().parents[1]
    rows=[]
    for level in (33,65,129,257):
        last=(level-1)//2
        theta=mp.pi/level
        sine=lambda k:2*mp.sin(k*theta)
        fac=[mp.mpf(1)]
        for k in range(1,level):
            fac.append(fac[-1]*sine(k))
        physical=direct_rows(level,mp.mpf(-2),last)
        carrier=mp.exp(3j*mp.pi*(level-1)**2/(4*level))
        crossing=[carrier*mp.exp(3j*level
                  *(mp.pi-(2*a+1)*theta)**2/(4*mp.pi))
                  for a in range(last)]
        terms=[]
        endpoint_terms=[]
        for j in range(1,last+1):
            positive=[sine(2*a+1)*physical[a]*fac[j+a]*fac[j-a-1]/fac[j]**2
                      for a in range(j)]
            exact=mp.fsum((-1)**(j-a)*crossing[a]*positive[a] for a in range(j))
            endpoint=-crossing[j-1]*positive[-1]
            terms.append(exact*exact)
            endpoint_terms.append(endpoint*endpoint)
        full=mp.fsum(terms)
        separated=mp.fsum(v for j,v in enumerate(terms,1)
                         if 4*j<=level or 100*j>=49*level)
        middle=full-separated
        rows.append({
            "N":level,
            "exact_normal_normal_log_modulus_over_N":mp.nstr(mp.log(abs(full))/level,30),
            "separated_index_regions_log_modulus_over_N":mp.nstr(mp.log(abs(separated))/level,30),
            "remaining_index_band_log_modulus_over_N":mp.nstr(mp.log(abs(middle))/level,30),
            "endpoint_approximation_log_modulus_over_N_diagnostic":
                mp.nstr(mp.log(abs(mp.fsum(endpoint_terms)))/level,30),
        })
    # Formal phase only: no claim about its coefficient in the finite source.
    power=6
    equation=lambda t:mp.log(2*mp.sin(t/2))+mp.asinh(mp.tan(t/2))-1j*power*t/4
    t=mp.findroot(equation,mp.mpc(".45",".28"))
    x=(mp.pi-t)/(2*mp.pi)
    primitive=lambda z:(-1j*mp.pi*(z*z-z)/2
        +1j*mp.polylog(2,mp.exp(2j*mp.pi*z))/(2*mp.pi)-1j*mp.pi/12)
    psi=-4*(primitive(mp.mpf(1)/4+t/(4*mp.pi))
            +primitive(mp.mpf(1)/4-t/(4*mp.pi)))
    c=primitive(2*x)-2*primitive(x)+psi
    phase=2*c+1j*power*t*t/(4*mp.pi)
    result={
        "status":"diagnostic",
        "precision_decimal":140,
        "scope":"Exact finite normal-normal sums; no limiting rate or saddle contribution asserted.",
        "records":rows,
        "formal_chirp":{
            "combined_power":power,
            "angle":[mp.nstr(t.real,30),mp.nstr(t.imag,30)],
            "stationary_equation_residual":mp.nstr(abs(equation(t)),12),
            "real_phase":mp.nstr(phase.real,30),
            "scope":"Formal analytic stationary point only; omitted finite tails and cycle coefficient unproved.",
        },
        "sha256":{str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest()
            for p in (Path(__file__).resolve(),
                      root/"experiments/check_physical_row_riccati_transport.py",
                      root/"notes/research_pair_triangular_normal_region.md")},
    }
    output=root/"repro/results/research-pair-triangular-cancellation-diagnostic.json"
    output.write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(result["records"],indent=2))


if __name__=="__main__":
    main()
