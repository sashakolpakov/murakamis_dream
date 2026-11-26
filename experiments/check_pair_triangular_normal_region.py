#!/usr/bin/env python3
"""Check the exact triangular first normals and their rate comparison."""
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import re

import mpmath as mp
from flint import arb, ctx

from check_physical_row_riccati_transport import direct_rows, relative


def main():
    root = Path(__file__).resolve().parents[1]
    mp.mp.dps = 110
    ctx.prec = 160
    pi_lower = Q(333, 106)
    atan_lower = sum((Q(-1)**k)*Q(1, 5)**(2*k+1)/Q(2*k+1)
                     for k in range(4))
    assert 16*atan_lower-4*Q(1,239)>pi_lower
    assert Q(99,70)**2>2
    groups = 100
    series = sum(Q(1,(8*r+1)**2)+Q(1,(8*r+3)**2)
                 -Q(1,(8*r+5)**2)-Q(1,(8*r+7)**2)
                 for r in range(groups))
    series_upper = series+Q(1,32*(groups-1))
    catalan_upper = sum(Q((-1)**k,(2*k+1)**2) for k in range(21))
    c_upper = (2*Q(99,70)*series_upper+catalan_upper)/pi_lower
    assert c_upper<Q(251,200)
    assert 4*catalan_upper/pi_lower<Q(7,6)
    exponential_lower=Q(1)
    term=Q(1)
    for k in range(1,10):
        term*=Q(13,4)/k
        exponential_lower+=term
    assert exponential_lower>25
    assert Q(7,6)+Q(1,50)*(1+Q(13,4))==Q(751,600)<Q(251,200)
    certificate_path = root/"repro/results/research-internal-pair-three-mixed-packet.json"
    certificate = json.loads(certificate_path.read_text())
    assert certificate["status"]=="certified"
    value = certificate["root"]["selected_action"]
    real_ball = arb(re.match(r"(\[[^\]]+\])",value).group(1))
    assert real_ball>arb(63)/50
    assert Q(63,25)-Q(251,100)==Q(1,100)

    normal_checks = phase_sum_checks = monotonicity_checks = 0
    maximum_error = mp.mpf(0)
    for nlevel in (8,9,16,17,32,33):
        theta, eta = mp.pi/nlevel, (-1)**(nlevel-1)
        last = (nlevel-1)//2
        sine = lambda k: 2*mp.sin(k*theta)
        fac = [mp.mpf(1)]
        for k in range(1, 2*last):
            fac.append(fac[-1]*sine(k))
        frows = direct_rows(nlevel, mp.mpf(-2), last)
        for j in range(1,last+1):
            nodes = [2*mp.cos((2*h+1)*theta) for h in range(j)]
            def newton(z):
                return mp.fprod(c-z for c in nodes)/fac[j]**2
            magnitudes, derivatives = [], []
            for a in range(j):
                actual = mp.diff(newton,nodes[a])
                predicted = ((-1)**(j-a)*fac[j+a]*fac[j-a-1]
                             /(sine(2*a+1)*fac[j]**2))
                error = relative(actual,predicted)
                assert error<mp.mpf("1e-70")
                maximum_error=max(maximum_error,error)
                normal_checks+=1
                derivatives.append(actual)
                magnitudes.append(frows[a]*fac[j+a]*fac[j-a-1]/fac[j]**2)
            for a in range(j-1):
                assert magnitudes[a+1]>magnitudes[a]
                monotonicity_checks+=1
            for power in (3,4,7):
                carrier=mp.exp(1j*mp.pi*power*(nlevel-1)**2/(4*nlevel))
                crossing=[carrier*mp.exp(1j*power*nlevel
                           *(mp.pi-(2*a+1)*theta)**2/(4*mp.pi))
                          for a in range(j)]
                original=eta*mp.fsum(
                    sine(2*a+1)**2*crossing[a]*frows[a]*derivatives[a]
                    for a in range(j))
                formula=eta*mp.fsum(
                    (-1)**(j-a)*crossing[a]*sine(2*a+1)*magnitudes[a]
                    for a in range(j))
                error=relative(original,formula)
                assert error<mp.mpf("1e-70")
                assert abs(original)<=2*j*magnitudes[-1]+mp.mpf("1e-70")
                maximum_error=max(maximum_error,error)
                phase_sum_checks+=1
    dependencies = [
        Path(__file__).resolve(),
        root/"experiments/check_physical_row_riccati_transport.py",
        root/"notes/research_pair_triangular_normal_region.md",
        root/"notes/research_physical_row_riccati_transport.md",
        root/"notes/research_last_physical_row_riccati.md",
        root/"notes/research_edge_cut_energy_comparison.md",
        certificate_path,
    ]
    result = {
        "status":"passed", "precision_decimal":110,
        "normal_identities":normal_checks, "original_phase_sums":phase_sum_checks,
        "strict_magnitude_comparisons":monotonicity_checks,
        "maximum_identity_error":mp.nstr(maximum_error,20),
        "rational_C_upper":str(c_upper),
        "rational_C_upper_decimal_diagnostic":float(c_upper),
        "upper_endpoint_C_bound":"751/600",
        "retained_gap_indices":"j/N<=1/4 or j/N>=49/100",
        "certified_half_action":str(real_ball),
        "rational_rate_upper":"251/100",
        "geometric_rate_lower":"63/25",
        "strict_rate_gap":"1/100",
        "sha256":{str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest()
                  for p in dependencies},
    }
    output=root/"repro/results/research-pair-triangular-normal-region.json"
    output.write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({k:result[k] for k in (
        "status","normal_identities","original_phase_sums",
        "strict_magnitude_comparisons","maximum_identity_error",
        "rational_C_upper_decimal_diagnostic","strict_rate_gap")}))


if __name__=="__main__":
    main()
