#!/usr/bin/env python3
"""Exact enclosure, coverage, and scalar premises for a geometric contraction.

The derivative certificate is a separate outward calculation. This
checker verifies its exact covering and provenance, the two endpoint
period roots, and the rational bounds used for no-exit continuation.
It does not infer a quantum coefficient from geometric contraction.
"""

from __future__ import annotations

from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path

from flint import acb, arb, ctx


def rat(v):
    v = Q(v)
    return arb(v.numerator)/v.denominator


def main():
    ctx.prec = 192
    root = Path(__file__).resolve().parents[1]
    proof = root/"notes/research_homogeneous_three_geometric_contraction.md"
    source = root/"experiments/certify_homogeneous_three_geometric_box.py"
    record_path = root/"repro/results/research-homogeneous-three-geometric-box.json"
    record = json.loads(record_path.read_text())
    assert record["status"] == "passed"
    assert record["neighbor_mesh"] == 32
    assert record["sha256"][source.name] == hashlib.sha256(source.read_bytes()).hexdigest()
    domain = tuple(map(Q, record["domain_real_angle_height"]))
    assert domain == (Q(13,10),Q(91,50),Q(41,50),Q(121,100))
    a,b,c,d = domain
    events = {}
    area = Q(0)
    for i,entry in enumerate(record["accepted"]):
        x0,x1,h0,h1 = map(Q,entry["box"])
        assert a<=x0<x1<=b and c<=h0<h1<=d
        events.setdefault(x0,[]).append((1,i,h0,h1))
        events.setdefault(x1,[]).append((-1,i,h0,h1))
        area += (x1-x0)*(h1-h0)
    active = {}
    endpoints = sorted(events)
    assert endpoints[0]==a and endpoints[-1]==b
    for x in endpoints:
        for sign,i,h0,h1 in events[x]:
            if sign==1:
                assert i not in active
                active[i]=(h0,h1)
            else:
                assert active.pop(i)==(h0,h1)
        if x==b:
            assert not active
            continue
        at=c
        for h0,h1 in sorted(active.values()):
            assert h0==at
            at=h1
        assert at==d
    assert area==(b-a)*(d-c)

    ii=acb(0,1)
    pi=arb.pi()
    star=acb(-arb(1)/4,3*arb(3).sqrt()/4).acos()
    checks=[]
    def positive(name,v):
        assert v>0,(name,v)
        checks.append({"name":name,"positive_margin":str(v)})

    positive("homogeneous angle above 1722/1000",star.real-rat(Q(1722,1000)))
    positive("homogeneous angle below 1723/1000",rat(Q(1723,1000))-star.real)
    positive("homogeneous height above 1087/1000",-star.imag-rat(Q(1087,1000)))
    positive("homogeneous height below 1088/1000",rat(Q(1088,1000))+star.imag)

    def returns(t,u):
        v=(t/2).tan()
        cu=(u/2).cos()
        s=(1+v*v*cu*cu).sqrt()
        first=cu*(1+v*v)/(2*s)
        second=cu*v*(1+v*v)/(2*s)-cu**3*v*(1+v*v)**2/(4*s**3)
        return (v*cu).asinh(),first,second

    roots=[]
    cases=[
        ("two complete neighbors",acb(rat(Q(1381983397031137455,10**18)),-rat(Q(883007686999445322,10**18))),acb(0),acb(0),(Q(1381,1000),Q(1383,1000),Q(882,1000),Q(884,1000))),
        ("one complete neighbor",acb(rat(Q(1539056826670160188,10**18)),-rat(Q(982192219812633070,10**18))),acb(0),star,(Q(1539,1000),Q(1540,1000),Q(982,1000),Q(983,1000))),
    ]
    for label,center,u,w,enclosure in cases:
        radius=rat(Q(1,10**9))
        disk=acb(center.real+arb(0,radius),center.imag+arb(0,radius))
        ru,du,_=returns(center,u)
        rw,dw,_=returns(center,w)
        residual=3*center+2*ii*(ru+rw)-2*pi
        first=3+2*ii*(du+dw)
        second=2*ii*(returns(disk,u)[2]+returns(disk,w)[2])
        margin=abs(first)*radius-abs(residual)-abs(second)*radius**2/2
        positive(label+": Rouche margin",margin)
        x0,x1,h0,h1=enclosure
        positive(label+": angle lower",disk.real-rat(x0))
        positive(label+": angle upper",rat(x1)-disk.real)
        positive(label+": height lower",-disk.imag-rat(h0))
        positive(label+": height upper",rat(h1)+disk.imag)
        roots.append({"name":label,"center":str(center),"radius":str(radius),"enclosing_box":str(disk)})

    # Bounds on changes from one finite neighbor's homogeneous value.
    da_minus=a-Q(1723,1000)
    da_plus=b-Q(1722,1000)
    dh_minus=c-Q(1088,1000)
    dh_plus=d-Q(1087,1000)
    abs_da=max(-da_minus,da_plus)
    abs_dh=max(-dh_minus,dh_plus)
    images=[]
    for number,base in [
        (2,(Q(1722,1000),Q(1723,1000),Q(1087,1000),Q(1088,1000))),
        (1,(Q(1539,1000),Q(1540,1000),Q(982,1000),Q(983,1000))),
    ]:
        x0,x1,h0,h1=base
        image=(
            x0+number*(da_minus/4-abs_dh/16),
            x1+number*(da_plus/4+abs_dh/16),
            h0+number*(dh_minus/4-abs_da/16),
            h1+number*(dh_plus/4+abs_da/16),
        )
        assert a<image[0]<image[1]<b and c<image[2]<image[3]<d
        images.append({"finite_neighbors":number,"strict_image_box":[str(v) for v in image]})
    assert 2*(Q(1,4)+Q(1,16))==Q(5,8)<1
    assert Q(91,50)+2*Q(3,5)<Q(25,8)
    positive("selected-selected angle inequality",pi-rat(Q(91,50)+2*Q(3,5)))
    rho=(8-arb(39).sqrt())/5
    positive("decay factor positive",rho)
    positive("decay factor below 9/25",rat(Q(9,25))-rho)
    assert Q(5,16)*(Q(16,5))==1
    dependencies=[Path(__file__).resolve(),source,record_path]
    if proof.exists():
        dependencies.append(proof)
    result={
        "status":"passed",
        "scope":"Exact multiplicity-one coverage and source hash of the outward derivative certificate; Rouche disks for endpoint period roots; rational no-exit images, contraction and positivity constants. The global continuation, Banach argument and source identification remain written. No quantum asymptotic assertion.",
        "precision_bits":ctx.prec,
        "covered_area":str(area),
        "parameter_boxes":len(record["accepted"]),
        "scalar_checks":checks,
        "endpoint_roots":roots,
        "strict_image_boxes":images,
        "contraction":"5/8",
        "interior_decay":str(rho),
        "sha256":{str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in dependencies},
    }
    output=root/"repro/results/research-homogeneous-three-geometric-contraction.json"
    output.write_text(json.dumps(result,indent=2)+"\n")
    print(f"Passed exact coverage of {len(record['accepted'])} boxes and {len(checks)} scalar comparisons. {output}")


if __name__=="__main__":
    main()
