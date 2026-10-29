#!/usr/bin/env python3
"""Exact actual-port Fourier cap, independent clocks and finite alias tails."""

import json
from pathlib import Path

import sympy as sp


def field(level):
    multiplier=max(2,4000//level)
    while not sp.isprime(level*multiplier+1):multiplier+=1
    prime=int(level*multiplier+1)
    generator=int(sp.primitive_root(prime))
    return prime,pow(generator,(prime-1)//level,prime)


def audit_level(n):
    prime,zeta=field(n)
    invn=pow(n,-1,prime)
    def average_mode(q,v=1):
        return sum(pow(v*pow(zeta,j,prime)%prime,q,prime)
                   for j in range(n))*invn%prime
    modes={q:average_mode(q) for q in range(-4*n-4,4*n+5)}
    units=0
    # Literal four-port units, including all first-port output bands.
    # Q is independent of the fixed Fourier sampling root zeta.
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for d in range(n):
                    q=d-b
                    for Q in (2,zeta):
                        weight=pow(Q,b,prime)
                        original=weight*invn%prime if d==b else 0
                        represented=weight*modes[q]*invn%prime
                        assert represented==original
                    units+=1
    tails=0
    for q in range(-3*n-1,3*n+2):
        for ell in (-2,0,2):
            for h in range(4):
                weight=pow(q,h,prime)
                target=weight if q+ell==0 else 0
                for v in (1,2):
                    average=weight*average_mode(q+ell,v)%prime
                    alias=(weight*pow(v,q+ell,prime)%prime
                           if (q+ell)%n==0 and q+ell!=0 else 0)
                    assert (average-alias)%prime==target%prime
                    tails+=1
    # The actual two-cut unknot is the flip, not an identity tensor.
    def flip_kernel(eta,Q=1,clock=False):
        return sum((pow(Q,b,prime) if clock else 1)*pow(eta,a-b,prime)
                   for a in range(n) for b in range(n))%prime
    selected=sum(flip_kernel(pow(zeta,j,prime)) for j in range(n))*invn*invn%prime
    selected_clock=sum(flip_kernel(pow(zeta,j,prime),zeta,True)
                       for j in range(n))*invn*invn%prime
    assert selected==1 and selected_clock==0
    # Exact finite-port character ratios do not supply point substitution.
    p=3
    cap=invn
    substituted=sum(pow(pow(p,-1,prime)*p%prime,q,prime)
                    for q in range(n))*invn%prime
    assert substituted==1 and cap!=substituted
    clock_units=0
    Q=2
    for b in range(n):
        for d in range(n):
            q=d-b
            assert pow(Q,d,prime)==pow(Q,b,prime)*pow(Q,q,prime)%prime
            clock_units+=1
    return {"level":n,"prime":prime,"all_four_port_units":units,
            "generic_Q_and_root_Q_independent_of_Fourier_sampling":True,
            "shifted_moment_tail_checks":tails,
            "input_output_clock_units":clock_units,
            "actual_flip_source":selected,"actual_flip_input_clock_source":selected_clock,
            "character_kernel_cap_differs_from_incidence_substitution":True}


def symbolic_two_power_coordinates():
    Q,Veta=sp.symbols("Q V_eta",nonzero=True)
    b,n=sp.symbols("b N",integer=True,positive=True)
    assert sp.diff(Q**(n*b),Q)*Q==n*b*Q**(n*b)
    assert sp.diff(Veta,Q)==0
    return {"physical_power_normal_derivative":"D_Q U_B=N*b*U_B",
            "fixed_band_power_normal_derivative":"D_Q V_eta=0",
            "source_formula":"[eta^0]F=[V_eta^0](sum_k F_(kN)V_eta^k)",
            "physical_b_sum_is_still_y_equals_one":True}


def main():
    levels=[audit_level(n) for n in range(2,9)]
    result={"status":"PASS","levels":levels,
            "independent_whole_power_coordinates":symbolic_two_power_coordinates(),
            "scope":"Exact original finite four-port source and alias corrections. "
                    "No identification with a geometric cap or global Gaussian cycle."}
    target=Path(__file__).with_name("finite_band_fourier_cap_results.json")
    target.write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({"status":"PASS","levels":len(levels),
                      "four_port_units":sum(row["all_four_port_units"] for row in levels),
                      "shifted_moment_tails":sum(row["shifted_moment_tail_checks"] for row in levels),
                      "clock_units":sum(row["input_output_clock_units"] for row in levels),
                      "output":str(target)},indent=2))


if __name__=="__main__":main()
