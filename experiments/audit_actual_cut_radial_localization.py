#!/usr/bin/env python3
"""Actual inverse-cyclic-dilog cut endpoint weights and radial bounds."""

import json
from pathlib import Path

import mpmath as mp
import sympy as S


def derivative_identity():
    r, c = S.symbols("r c", real=True)
    den = r*r-2*r*c+1
    actual = (r*r-r*c)/den
    wanted = S.Rational(1,2)+(r*r-1)/(2*den)
    assert S.cancel(actual-wanted) == 0
    return True


def endpoint_log(N, j, epsilon):
    Q = mp.exp(epsilon*2*mp.pi*1j/N)
    return -sum(mp.mpf(k)/N*mp.log(abs(1-Q**(k-j)))
                for k in range(1,N) if k != j)


def actual_g_log(N, j, epsilon, r):
    Q = mp.exp(epsilon*2*mp.pi*1j/N)
    return -sum(mp.mpf(k)/N*mp.log(abs(1-r*Q**(k-j)))
                for k in range(1,N) if k != j)


def exact_product_checks():
    endpoints = radial = 0
    for N in range(2,25):
        logs = [mp.log(2*mp.sin(mp.pi*k/N)) for k in range(1,N)]
        for j in range(1,N):
            u = mp.mpf(j)/N
            expected = sum(logs[:j])-(u+mp.mpf('0.5'))*mp.log(N)
            C = mp.mpf(N-1)/4-u/2
            minimum = mp.mpf((N-1)*(N-2))/(4*N)
            assert C >= minimum-mp.mpf('1e-50') >= -mp.mpf('1e-50')
            for epsilon in (1,-1):
                direct = endpoint_log(N,j,epsilon)
                assert abs(direct-expected) < mp.mpf('1e-48')
                endpoints += 1
                if N <= 12:
                    for r in map(mp.mpf, ('1.001','1.1','2','10')):
                        value = actual_g_log(N,j,epsilon,r)
                        assert value <= direct-C*mp.log(r)+mp.mpf('1e-48')
                        radial += 1
    return endpoints, radial


def actual_integral_checks():
    rows = []
    for N,j,epsilon in ((2,1,1),(3,1,1),(3,2,-1),(5,2,1),(5,3,-1)):
        u = mp.mpf(j)/N
        C = mp.mpf(N-1)/4-u/2
        G = mp.exp(endpoint_log(N,j,epsilon))
        scale = mp.sin(mp.pi*u)/mp.pi
        def integrand(r):
            return mp.exp(actual_g_log(N,j,epsilon,r))*(r-1)**(-u)/r
        mass = scale*mp.quad(integrand,[1,mp.mpf('1.1'),2,mp.inf])
        tail = scale*mp.quad(integrand,[2,mp.inf])
        assert mass <= G*(1+mp.mpf('1e-30'))
        assert tail <= G*2**(-C)*(1+mp.mpf('1e-30'))
        rows.append({"N":N,"j":j,"epsilon":epsilon,
                     "normalized_absolute_mass_over_G":float(mass/G),
                     "tail_R2_over_proved_bound":float(tail/(G*2**(-C)))})
    return rows


def main():
    mp.mp.dps = 60
    derivative_identity()
    endpoints, radial = exact_product_checks()
    integrals = actual_integral_checks()
    lam = -mp.quad(lambda x:mp.log(2*mp.sin(x)),[0,mp.pi/6])
    rate = lam/mp.pi
    rows = []
    for N in (32,64,128,256,512):
        running = mp.mpf(0)
        logweights = []
        for j in range(1,N):
            running += mp.log(2*mp.sin(mp.pi*j/N))
            logweights.append(running-(mp.mpf(j)/N+mp.mpf('.5'))*mp.log(N))
        peak = max(logweights)
        lsum = peak+mp.log(sum(mp.exp(x-peak) for x in logweights))
        rows.append({"N":N,"log_sum_G_over_N":float(lsum/N),
                     "c_N_over_N":float(mp.mpf((N-1)*(N-2))/(4*N*N))})
    result = {"status":"PASS", "algebraic_derivative_identity":True,
              "endpoint_product_checks":endpoints,"radial_product_inequalities":radial,
              "actual_absolute_integrals":integrals,
              "limiting_endpoint_rate_v3_over_2pi":float(rate),
              "scale_diagnostics":rows,
              "scope":"Actual cut radial bounds and original factorial endpoint weights; no angular/source lower bound."}
    Path(__file__).with_name("actual_cut_radial_localization_results.json").write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({k:v for k,v in result.items() if k not in ('actual_absolute_integrals','scale_diagnostics')}))


if __name__ == "__main__":
    main()
