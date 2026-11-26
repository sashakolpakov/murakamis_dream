#!/usr/bin/env python3
"""Exact algebra and connected-branch premises for three-chain calibration.

This does not compare numerical dilogarithms or certify a quantum contour.
The action constant is fixed by the cited exact homogeneous identity.
"""

from __future__ import annotations

import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path

from flint import arb, acb, ctx
import sympy as sp


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=192)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    ctx.prec = args.precision
    root = Path(__file__).resolve().parents[1]
    pi, ii = arb.pi(), acb(0, 1)

    def rat(v):
        v = Q(v)
        return arb(v.numerator) / v.denominator

    def interval(a, b):
        return rat((a+b)/2) + arb(0, rat((b-a)/2))

    def square(z, radius):
        return acb(z.real + arb(0, radius), z.imag + arb(0, radius))

    def upper_acos(w):
        # Principal acos on the upper half-plane, with an explicit
        # holomorphic radical factorization for a tighter enclosure.
        return -ii * (w + (w-1).sqrt() * (w+1).sqrt()).log()

    def chart_checks(box):
        a, b, c, d = [interval(*ab) for ab in box]
        U, V = acb(-a, -b), acb(-c, -d)
        X, Y = 1/(1+U-U*V), 1/(1+V-U*V)
        x, y = X.log()/(2*pi*ii), Y.log()/(2*pi*ii)
        W = (U*V-U-V-1)/2
        tau = upper_acos(W)
        margins = [X.real, X.imag, Y.real, Y.imag,
                   1-abs(X), 1-abs(Y), 1-abs(X*U), 1-abs(Y*V),
                   W.imag, tau.real, pi-tau.real, -tau.imag]
        for wire in (x, y):
            margins.extend((wire.real, arb(1)/4-wire.real, wire.imag))
            for arg in (wire, arb(1)/2-wire+tau/(2*pi),
                        arb(1)/2-wire-tau/(2*pi)):
                margins.extend((arg.real, 1-arg.real))
        return margins

    initial = [(Q(2,5), Q(13,20)), (Q(3,4), Q(1)),
               (Q(2,5), Q(13,20)), (Q(3,4), Q(1))]
    pending = [(initial, "")]
    accepted = []
    visited = 0
    while pending:
        box, address = pending.pop()
        visited += 1
        if visited > 20000:
            raise RuntimeError("explicit connected-chart budget exceeded")
        margins = chart_checks(box)
        if all(v > 0 for v in margins):
            accepted.append({"address": address,
                             "box": [[str(a), str(b)] for a,b in box],
                             "minimum_margin": str(min(margins, key=lambda v: float(v.lower())))})
            continue
        axis = len(address) % 4
        a, b = box[axis]
        mid = (a+b)/2
        for digit, ab in (("0", (a,mid)), ("1", (mid,b))):
            child = list(box)
            child[axis] = ab
            pending.append((child, address+digit))

    # Reconstruct every leaf from its binary address; then collapse the
    # complete prefix tree. This checks the rational cover without floats.
    addresses = set()
    for item in accepted:
        address = item["address"]
        assert address not in addresses
        addresses.add(address)
        box = list(initial)
        for depth, digit in enumerate(address):
            axis = depth % 4
            a,b = box[axis]
            mid = (a+b)/2
            box[axis] = (a,mid) if digit == "0" else (mid,b)
        assert [[str(a),str(b)] for a,b in box] == item["box"]
    while addresses != {""}:
        address = max(addresses, key=len)
        assert address
        parent = address[:-1]
        assert parent+"0" in addresses and parent+"1" in addresses
        addresses.remove(parent+"0")
        addresses.remove(parent+"1")
        assert parent not in addresses
        addresses.add(parent)
    assert addresses == {""}

    source_path = root/"repro/results/research-three-chain-geometric-chamber.json"
    source = json.loads(source_path.read_text())
    assert source["status"] == "passed"
    assert source["reference_length"] == 24 and source["bulk_depth"] == 9
    epsilon = rat(Q(8, 3*10**25))
    index_tests = []

    def wire(t,u):
        ct,cu = t.cos(),u.cos()
        C = (1-ct*cu)/(2+ct+cu)
        assert C.imag < 0
        return upper_acos(C.conjugate()).conjugate()/(2*pi)

    def verify_indices(label,x,y):
        X,Y = (2*pi*ii*x).exp(),(2*pi*ii*y).exp()
        a,b = 1/X-1,1/Y-1
        delta = 1-2*(a+b)+(a-b)**2
        assert delta.imag > 0
        U,V = (1+a-b-delta.sqrt())/2,(1-a+b-delta.sqrt())/2
        for k,z in enumerate((U,V)):
            margins = [-z.real-rat(Q(2,5)), rat(Q(13,20))+z.real,
                       -z.imag-rat(Q(3,4)), 1+z.imag]
            assert all(v > 0 for v in margins), (label,k,list(map(str,margins)))
            index_tests.append({"label":label,"coordinate":k,
                                "enclosure":str(z),"margins":list(map(str,margins))})

    reference24 = None
    for ref in source["references"]:
        m = ref["length"]
        centers = [acb(rat(a),rat(b)) for a,b in ref["centers"]]
        assert len(centers) == m
        angles = [square(z,epsilon) for z in centers]
        wires = [wire(t,u) for t,u in zip(angles,angles[1:])]
        for v in range(1,m-1):
            verify_indices(f"reference length {m}, vertex {v+1}",wires[v-1],wires[v])
        if m == 24:
            reference24 = centers
    assert reference24 is not None
    near = [square(reference24[j-1],epsilon+rat(Q(13,25))*rat(Q(9,25))**(24-j))
            for j in range(1,11)]
    near_wires = [wire(t,u) for t,u in zip(near,near[1:])]
    for v in range(1,9):
        verify_indices(f"all-length near-end vertex {v+1}",near_wires[v-1],near_wires[v])
    star = upper_acos(acb(-arb(1)/4,3*arb(3).sqrt()/4))
    bulk_angle = square(star,rat(Q(9,25))**8)
    bulk_wire = wire(bulk_angle,bulk_angle)
    verify_indices("all-length bulk",bulk_wire,bulk_wire)

    # All identities hold as rational functions; no sampled equality is used.
    U,V,z = sp.symbols("U V z")
    X,Y = 1/(1+U-U*V),1/(1+V-U*V)
    W = U*V-U-V-1
    exact = []
    def identity(name, expr):
        assert sp.cancel(expr) == 0, name
        exact.append(name)
    identity("index equation 1",1/X-1-U*(1-V))
    identity("index equation 2",1/Y-1-V*(1-U))
    identity("geometric inverse U",U-(1-X)/(1+X+X*W))
    identity("geometric inverse V",V-(1-Y)/(1+Y+Y*W))
    identity("vertex quadratic",X*Y*W**2+(X*Y+X+Y)*W+1+X+Y-X*Y)
    C=(X+1/X)/2
    identity("wire derivative exponential",(X*U-1)/(U*(1-X))-(C+W/2)/(1-C))
    period=z**3*(1+X*z)*(1+Y*z)-(X+z)*(Y+z)
    numerator,_=sp.fraction(sp.cancel(period))
    assert sp.rem(numerator,z*z-W*z+1,z) == 0
    exact.append("original exponentiated vertex period")
    jac=sp.Matrix([X,Y]).jacobian([U,V]).det()
    identity("critical chart Jacobian",jac-(1-U-V)*X**2*Y**2)

    proof = root/"notes/research_three_chain_action_volume_calibration.md"
    deps = [Path(__file__).resolve(),source_path,
            root/"notes/research_three_chain_geometric_chamber.md",
            root/"notes/research_three_vertex_central_index_chart.md",
            root/"notes/research_homogeneous_three_action_calibration.md",
            root/"notes/research_three_vertex_local_composition.md",
            root/"notes/research_unsummed_network_phase_coercivity.md",
            root/"notes/research_positive_edge_volume_identity.md",
            root/"notes/research_positive_point_marked_completion.md"]
    if proof.exists(): deps.append(proof)
    result = {"status":"passed","precision_bits":ctx.prec,
              "scope":"Exact rational identities, connected branch-domain coverage, and inclusion of all-length geometric index enclosures. No numerical dilogarithm calibration, quantum coefficient, or complementary contour is checked.",
              "chart_root_box":[[str(a),str(b)] for a,b in initial],
              "accepted_chart_boxes":len(accepted),"visited_chart_boxes":visited,
              "exact_binary_cover":True,"chart_boxes":accepted,
              "actual_index_coordinates":len(index_tests),"index_tests":index_tests,
              "exact_identities":exact,
              "sha256":{str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in deps}}
    output=args.output or root/"repro/results/research-three-chain-action-volume-calibration.json"
    output.write_text(json.dumps(result,indent=2)+"\n")
    print(f"Passed {len(accepted)} connected-chart boxes, {len(index_tests)} actual index coordinates, {len(exact)} exact identities. {output}")


if __name__ == "__main__":
    main()
