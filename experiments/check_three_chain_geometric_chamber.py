#!/usr/bin/env python3
"""Certify the finite premises of a chamber enclosure for every chain length.

Approximate solves only choose rational centers. One-vertex Rouche
estimates and the previously proved 5/8 contraction enclose each
whole finite reference solution. The written comparison argument
extends the finite reference enclosures to all longer chains.
"""

from __future__ import annotations

import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path

import mpmath as mp
import sympy as sp
from flint import arb, acb, ctx


REFERENCE = 24
DEPTH = 9


def rat(v):
    v=Q(v)
    return arb(v.numerator)/v.denominator


def centered(z, radius):
    return acb(z.real+arb(0,radius),z.imag+arb(0,radius))


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision",type=int,default=192)
    parser.add_argument("--output",type=Path)
    args=parser.parse_args()
    ctx.prec=args.precision
    mp.mp.dps=65
    root=Path(__file__).resolve().parents[1]
    pi,ii=arb.pi(),acb(0,1)
    star=acb(-arb(1)/4,3*arb(3).sqrt()/4).acos()
    mp_star=mp.acos(mp.mpc(-mp.mpf(1)/4,3*mp.sqrt(3)/4))
    root_radius=rat(Q(1,10**25))
    fixed_error=8*root_radius/3
    checks=[]

    def positive(name,v):
        assert v>0,(name,str(v))
        checks.append({"name":name,"positive_margin":str(v)})

    def in_omega(name,z):
        for label,v in (
            ("angle lower",z.real-rat(Q(13,10))),
            ("angle upper",rat(Q(91,50))-z.real),
            ("height lower",-z.imag-rat(Q(41,50))),
            ("height upper",rat(Q(121,100))+z.imag),
        ):
            positive(name+" "+label,v)

    def ret(t,u):
        v=(t/2).tan()
        c=(u/2).cos()
        s=(1+v*v*c*c).sqrt()
        r=(v*c).asinh()
        first=c*(1+v*v)/(2*s)
        second=c*v*(1+v*v)/(2*s)-c**3*v*(1+v*v)**2/(4*s**3)
        return r,first,second

    def local_root(name,t,u,w):
        disk=centered(t,root_radius)
        ru,du,_=ret(t,u);rw,dw,_=ret(t,w)
        residual=3*t+2*ii*(ru+rw)-2*pi
        first=3+2*ii*(du+dw)
        second=2*ii*(ret(disk,u)[2]+ret(disk,w)[2])
        positive(name+" Rouche",
                 abs(first)*root_radius-abs(residual)-abs(second)*root_radius**2/2)
        in_omega(name,disk)

    def wire(t,u):
        ct,cu=t.cos(),u.cos()
        C=(1-ct*cu)/(2+ct+cu)
        positive("wire cosine in lower half-plane",-C.imag)
        return C.acos()/(2*pi)

    def wire_chamber(name,x):
        for label,v in (
            ("real lower",x.real-rat(Q(7,50))),
            ("real upper",rat(Q(1,5))-x.real),
            ("height lower",x.imag-rat(Q(9,100))),
            ("height upper",rat(Q(3,25))-x.imag),
        ):
            positive(name+" "+label,v)

    def directed(name,x):
        r=x.real-arb(1)/6
        s=x.imag-arb(2).log()/(2*pi)+4*r/5
        for label,v in (
            ("directed real lower",r),
            ("directed real upper",rat(Q(13,1000))-r),
            ("directed height lower",s+rat(Q(3,2000))),
            ("directed height upper",rat(Q(1,1000))-s),
        ):
            positive(name+" "+label,v)

    def cap_chamber(name,t):
        for label,v in (
            ("cap angle lower",t.real-rat(Q(38,25))),
            ("cap angle upper",pi/2-t.real),
            ("cap height lower",-t.imag-rat(Q(97,100))),
            ("cap height upper",1+t.imag),
            ("cap cosine inside unit disk",1-abs((t/2).cos())),
        ):
            positive(name+" "+label,v)

    def geometric_gradient(name,x,t):
        cp=(pi*x+t/2).cos()
        cm=(pi*x-t/2).cos()
        sx=(pi*x).sin()
        positive(name+" cosine plus",cp.real)
        positive(name+" cosine minus",cm.real)
        positive(name+" sine",sx.real)
        bx=cp.log()+cm.log()-2*sx.log()
        positive(name+" logarithmic lift",pi-abs(bx.imag))
        return bx

    def indices(name,x,y,vertex_angle):
        X,Y=(2*pi*ii*x).exp(),(2*pi*ii*y).exp()
        a,b=1/X-1,1/Y-1
        delta=1-2*(a+b)+(a-b)**2
        positive(name+" discriminant branch",delta.imag)
        R=delta.sqrt()
        U,V=(1+a-b-R)/2,(1-a+b-R)/2
        out=[]
        for k,z in enumerate((U,V)):
            positive(name+f" index{k} algebraic real quadrant",-z.real)
            positive(name+f" index{k} algebraic imaginary quadrant",-z.imag)
            s=ii*z.log()/(2*pi)
            positive(name+f" index{k} real lower",s.real-arb(1)/4)
            positive(name+f" index{k} real upper",arb(9)/20-s.real)
            positive(name+f" index{k} height",arb(1)/50-abs(s.imag))
            out.append(str(s))
        # The geometric vertex period supplies the exact quadratic relation.
        # These are branch/lift enclosures, not approximate equality tests.
        for k,wire_value in enumerate((x,y)):
            Z=(2*pi*ii*wire_value).exp()
            Ug=(1-Z)/(1+Z+2*Z*vertex_angle.cos())
            positive(name+f" geometric index{k} real quadrant",-Ug.real)
            positive(name+f" geometric index{k} imaginary quadrant",-Ug.imag)
            phi_derivative=-Ug.log()+(1-Z*Ug).log()-(1-Z).log()-pi*ii
            geometric_gradient(name+f" geometric gradient{k}",wire_value,vertex_angle)
            positive(name+f" retained logarithmic lift{k}",pi-abs(phi_derivative.imag))
        return out

    references=[]
    reference_centers=None
    for m in range(3,REFERENCE+1):
        def period_system(*angles):
            ts=[mp.mpc(0),*angles,mp.mpc(0)]
            return tuple(
                3*ts[j]+2j*(mp.asinh(mp.tan(ts[j]/2)*mp.cos(ts[j-1]/2))
                           +mp.asinh(mp.tan(ts[j]/2)*mp.cos(ts[j+1]/2)))-2*mp.pi
                for j in range(1,m+1))
        approx=mp.findroot(period_system,[mp_star]*m,tol=mp.mpf("1e-55"))
        rational_centers=[
            (Q(mp.nstr(z.real,55)),Q(mp.nstr(z.imag,55))) for z in approx]
        centers=[acb(rat(a),rat(b)) for a,b in rational_centers]
        neighbors=[acb(0),*centers,acb(0)]
        for j,t in enumerate(centers,1):
            local_root(f"length{m} vertex{j}",t,neighbors[j-1],neighbors[j+1])
        actual=[centered(t,fixed_error) for t in centers]
        wires=[wire(t,u) for t,u in zip(actual,actual[1:])]
        for j,x in enumerate(wires,1):
            wire_chamber(f"length{m} wire{j}",x)
        selected_indices=[indices(f"length{m} retained vertex{j}",wires[j-2],wires[j-1],actual[j-1])
                          for j in range(2,m)]
        cap_chamber(f"length{m} left cap",actual[0])
        cap_chamber(f"length{m} right cap",actual[-1])
        directed(f"length{m} left attachment",wires[0])
        directed(f"length{m} right attachment",wires[-1])
        geometric_gradient(f"length{m} left cap",wires[0],actual[0])
        geometric_gradient(f"length{m} right cap",wires[-1],actual[-1])
        references.append({
            "length":m,
            "centers":[[str(a),str(b)] for a,b in rational_centers],
            "wire_enclosures":list(map(str,wires)),
            "index_enclosures":selected_indices,
        })
        if m==REFERENCE:reference_centers=centers
        print(f"Certified reference length {m}.",flush=True)

    # All interior vertices at distance at least DEPTH from each end.
    bulk_error=rat(Q(9,25)**(DEPTH-1))
    bulk_angle=centered(star,bulk_error)
    bulk_wire=wire(bulk_angle,bulk_angle)
    wire_chamber("all-length bulk",bulk_wire)
    bulk_indices=indices("all-length bulk",bulk_wire,bulk_wire,bulk_angle)

    # For m>=REFERENCE, compare the near-end vertices with this fixed path.
    near=[]
    for j in range(1,DEPTH+2):
        comparison=rat(Q(13,25)*Q(9,25)**(REFERENCE-j))
        near.append(centered(reference_centers[j-1],fixed_error+comparison))
    near_wires=[wire(t,u) for t,u in zip(near,near[1:])]
    for j,x in enumerate(near_wires,1):
        wire_chamber(f"all-length near-end wire{j}",x)
    near_indices=[indices(f"all-length near-end retained vertex{j}",
                          near_wires[j-2],near_wires[j-1],near[j-1])
                  for j in range(2,DEPTH+1)]
    cap_chamber("all-length cap",near[0])
    directed("all-length first attachment",near_wires[0])
    geometric_gradient("all-length cap",near_wires[0],near[0])

    X,Y,z,W=sp.symbols("X Y z W")
    period=z**3*(1+X*z)*(1+Y*z)-(X+z)*(Y+z)
    quadratic=X*Y*W**2+(X*Y+X+Y)*W+1+X+Y-X*Y
    assert sp.factor(period-(z-1)*z**2*quadratic.subs(W,z+1/z))==0
    Ug=(1-X)/(1+X+X*W);Vg=(1-Y)/(1+Y+Y*W)
    for residual in (1/X-1-Ug*(1-Vg),1/Y-1-Vg*(1-Ug)):
        numerator,_=sp.fraction(sp.factor(residual))
        assert sp.rem(numerator,quadratic,W)==0
    C=(X+1/X)/2
    assert sp.factor((X*Ug-1)/(Ug*(1-X))-(C+W/2)/(1-C))==0
    a,b,C=sp.symbols("a b C")
    assert sp.factor(((C+a)*(C+b)-(1-C)**2).subs(C,(1-a*b)/(2+a+b)))==0

    dependencies=[
        Path(__file__).resolve(),
        root/"notes/research_homogeneous_three_geometric_contraction.md",
        root/"repro/results/research-homogeneous-three-geometric-contraction.json",
        root/"repro/results/research-homogeneous-three-geometric-box-review.json",
        root/"notes/research_three_vertex_central_index_chart.md",
        root/"notes/research_three_vertex_joint_concavity.md",
    ]
    proof=root/"notes/research_three_chain_geometric_chamber.md"
    if proof.exists():dependencies.append(proof)
    result={
        "status":"passed",
        "precision_bits":ctx.prec,
        "scope":"Rouche enclosures for finite reference lengths3..24, the global 5/8-contraction residual bound, and interval chamber tests for the explicit bulk and near-end comparison boxes. The all-length extension is a written discrete comparison argument. No quantum coefficient or complementary-contour assertion.",
        "reference_length":REFERENCE,"bulk_depth":DEPTH,
        "local_root_radius":"1/10000000000000000000000000",
        "whole_solution_error":"8/(3*10^25)",
        "references":references,
        "bulk_angle_box":str(bulk_angle),"bulk_wire_box":str(bulk_wire),
        "bulk_index_boxes":bulk_indices,
        "near_end_angle_boxes":list(map(str,near)),
        "near_end_wire_boxes":list(map(str,near_wires)),
        "near_end_index_boxes":near_indices,
        "positive_checks":checks,
        "exact_matching_identities":5,
        "sha256":{str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest()
                  for p in dependencies},
    }
    output=args.output or root/"repro/results/research-three-chain-geometric-chamber.json"
    output.write_text(json.dumps(result,indent=2)+"\n")
    print(f"Passed {len(checks)} positive comparisons. {output}",flush=True)


if __name__=="__main__":
    main()
