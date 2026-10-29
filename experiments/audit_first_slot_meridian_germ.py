#!/usr/bin/env python3
"""Exact first-slot marked-meridian momentum and split density pole."""

import json
from pathlib import Path

import sympy as sp


def main():
    M, c, beta, r, s, p = sp.symbols("M c beta r s p", nonzero=True)
    kappa = M-1/M
    U = sp.Matrix([[M-c*beta, kappa*beta-c*beta**2], [c, 1/M+c*beta]])
    F = sp.Matrix([[r, 1-r], [s, -kappa-s]])
    D = U-sp.eye(2)/M
    assert sp.cancel(U.det()-1) == 0
    assert sp.cancel(sp.trace(U)-M-1/M) == 0
    assert sp.cancel(D.det()) == 0
    current = F.inv()*D*F
    raw = -current[0, 1]/current[0, 0]
    predicted = 1-(1-kappa*beta)/(r+beta*s)
    assert sp.cancel(raw-predicted) == 0
    inverse = (1-kappa*beta)/(1-p)-beta*s
    assert sp.cancel(predicted.subs(r, inverse)-p) == 0
    Delta = s+kappa*inverse
    density = -p*sp.diff(inverse, p)/Delta
    predicted_density = -p/((1-p)*(s*(1-p)+kappa))
    assert sp.cancel(density-predicted_density) == 0
    complete = predicted_density.subs(M, 1)
    assert sp.cancel(complete+p/(s*(1-p)**2)) == 0
    # The original complete inverse-Hurwitz bubble atoms, not a coordinate guess.
    h = sp.symbols("h", integer=True, nonnegative=True)
    t = r+beta*s
    a_h, a_next = 1+h*s, 1+(h+1)*s
    b_h = a_h+c*(1-t)*(t+h*s)/s
    b_next = a_next+c*(1-t)*(t+(h+1)*s)/s
    C = a_next*b_h/(b_next*a_h)
    assert sp.cancel(C-1+c*(1-t)**2/(b_next*a_h)) == 0
    # The residue-normalized scalar density has only the declared pole coalescence.
    z = 1+kappa/s
    partial = (1/(p-1)-z/(p-z))/kappa
    assert sp.cancel(partial-predicted_density) == 0
    out = Path(__file__).with_name("first_slot_meridian_germ_results.json")
    out.write_text(json.dumps({"status": "pass", "raw_F_M_conjugation": True,
                              "complete_bubble_transfer_atoms": True,
                              "generic_marked_meridian_momentum_Mobius": True,
                              "universal_momentum_pole": "p=1",
                              "density_poles": ["p=1", "p=1+(M-M^-1)/s"],
                              "complete_density": "-p/[s(1-p)^2]",
                              "scope": "Exact classical chart and admissibility checks; no selected source or Gaussian cycle identification."}, indent=2)+"\n")
    print(json.dumps({"status": "pass", "results": str(out)}, indent=2))


if __name__ == "__main__":
    main()
