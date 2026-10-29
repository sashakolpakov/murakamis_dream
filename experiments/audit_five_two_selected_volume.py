#!/usr/bin/env python3
"""Finite diagnostics of the proved marked 5_2 asymptotic and nonzero prefactor.

The proof uses exact source identities and certified contours, not these
finite-N comparisons. This diagnostic checks the assembled normalization.
"""
import json
from pathlib import Path
import mpmath as mp

def main():
    mp.mp.dps=100
    rho=mp.findroot(lambda z:z**3+z*z-1,mp.mpf(".75"))
    v=(1+rho)/2+1j*mp.sqrt(1/rho-(1+rho)**2/4)
    X=1/(1+v*v);Y=-v
    x=1+mp.log(X)/(2j*mp.pi);y=1+mp.log(Y)/(2j*mp.pi)
    def J(z):
        return (mp.polylog(2,1)-mp.polylog(2,mp.exp(2j*mp.pi*z)))/(2j*mp.pi)-.5j*mp.pi*z*z+.5j*mp.pi*z
    S=3*J(x)-J(y)-J(x-y)+1j*mp.pi*(3*x+2*y-x*x-x*y-y*y)
    R=(v*v+v+4)*(v*v+v-1)/(1-v**4)
    Wpp=2j*mp.pi*R
    Syy=-2j*mp.pi*(v*v+1)/(v*(v+1))
    a=mp.sqrt(2)*mp.exp((3*mp.log(mp.sin(mp.pi*x))-mp.log(mp.sin(mp.pi*y))
                      -mp.log(mp.sin(mp.pi*(x-y))))/2-1j*mp.pi*(3*x+2*y))
    C=2*mp.pi*a/(mp.sqrt(-Syy)*mp.sqrt(-Wpp))
    assert Syy.real<0 and Wpp.real<0 and Wpp.imag<0
    rows=[]
    previous=mp.inf
    for N in (12,24,48,96,192):
        Q=mp.exp(2j*mp.pi/N);F=[mp.mpc(1)]
        for k in range(1,N):
            F.append(F[-1]*(1-Q**k))
        value=mp.fsum(Q**(-n*(n+2)-j*(n+1))*F[n]**3/(F[j]*F[n-j])
                     for n in range(N) for j in range(n+1))
        ratio=value/(C*N**mp.mpf("1.5")*mp.exp(N*S))
        error=abs(ratio-1)
        assert error<previous and N*error<7
        previous=error
        rows.append({"N":N,"normalized_ratio_real":mp.nstr(ratio.real,35),
                     "normalized_ratio_imag":mp.nstr(ratio.imag,35),
                     "N_times_relative_error":mp.nstr(N*error,20)})
    result={"status":"PASS","critical_action":[mp.nstr(S.real,65),mp.nstr(S.imag,65)],
            "nonzero_prefactor":[mp.nstr(C.real,65),mp.nstr(C.imag,65)],
            "finite_diagnostics":rows,
            "proof":"notes/five_two_selected_volume_proof.md",
            "scope":"Normalization diagnostics; uniform proof comes from finite identities, exact contour formulas and rigorous Arb certificate."}
    out=Path(__file__).with_name("five_two_selected_volume_results.json")
    out.write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(result,indent=2))
if __name__=="__main__":
    main()

