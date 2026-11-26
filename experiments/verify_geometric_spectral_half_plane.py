#!/usr/bin/env python3
"""Exact rational constants in the geometric spectral half-plane proof.

This verifies only the elementary numerical comparisons in the written
argument. It does not sample solutions or replace the analytic return estimate.
"""
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path


def cosh_upper(x):
    return 1+x*x/2+x**4/(24*(1-x*x/30))


def main():
    comparisons = []

    def lt(name, left, right):
        assert left < right, (name, left, right)
        comparisons.append({"name":name,"left":str(left),"right":str(right),
                            "positive_difference":str(right-left)})

    lt("sqrt3 lower bound squared",F(25,9),F(3))
    lt("sqrt3 upper bound squared",F(3),F(49,16))
    lt("small-height cosh upper bound",cosh_upper(F(1,2)),F(8,7))
    lt("intermediate cosh upper bound",cosh_upper(F(1)),F(8,5))
    lt("global cosh upper bound",cosh_upper(F(23,20)),F(7,4))
    lt("H_c upper bound from Taylor lower bound",F(7,4),1+F(6,5)**2/2+F(6,5)**4/24)
    lt("angle comparison at 2*pi/3+2/15",F(37,60),F(5,8))
    lt("intermediate margin after squaring",F(1125,797)**2,F(2))
    lt("higher-height angle comparison squared",3*F(32249,56000)**2,F(1))
    lt("high-height B lower bound squared",F(8,5)**2,F(8,3))
    lt("small-height final spectral bound",F(38,21),2-F(1,3500))
    lt("high-height final spectral bound",F(133343,70400),F(19,10))
    lt("high-height margin",F(19,10),2-F(1,3500))
    lt("low-angle high-height margin",F(7,4),2-F(1,3500))
    lt("higher-height margin implies target",F(1,3500),F(1,875))
    lt("bootstrap square-root lower bound squared",F(49,25),F(2))
    lt("bootstrap cosh bound squared",F(7,4),F(16,9))
    lt("bootstrap spectral bound",F(26,15),F(7,4))
    lt("uniform Jacobi margin for N at least 16",F(1,5),F(1,4)-F(10,16**2))
    # The strict inequality pi^2<10 is the only transcendental input here.
    assert F(1,3500)-F(10,200**2)==F(1,28000)
    assert F(7,8)*(F(3,35)+F(1,1000))+F(1,2)==F(32249,56000)
    assert F(7,2)*(F(1,2)+F(7,8)*F(207,4400))==F(133343,70400)
    assert F(23,20)*F(9,220)==F(207,4400)
    assert F(4,7)*F(1,2000)==F(1,3500)
    assert F(4,7)*F(1,1000)==F(1,1750)
    here=Path(__file__).resolve();root=here.parents[1]
    paths=[here,root/'notes/research_geometric_spectral_half_plane.md']
    record={"status":"passed","method":"exact Fraction arithmetic",
            "strict_rational_comparisons":comparisons,"exact_normalization_identities":6,
            "scope":"Constants only; the return and angle inequalities have written proofs.",
            "sha256":{str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}}
    out=root/'repro/results/research-geometric-spectral-half-plane.json'
    out.write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({"status":"passed","strict_comparisons":len(comparisons),
                      "exact_identities":6,"output":str(out)}))


if __name__=='__main__':
    main()
