#!/usr/bin/env python3
"""Certify every endpoint face for the two-boundary two-crossing sum.

All decisions use outward python-flint balls. Accepted dyadic rectangles
partition each stated parameter square. No numerical optimizer is used.
"""
import argparse
import json
from fractions import Fraction
from pathlib import Path
from flint import acb, arb, ctx
import certify_terminal_three_central_phase as e


def rat(q):
    return arb(q.numerator) / q.denominator


def ball(lo, hi):
    return rat((lo+hi)/2) + arb(0, rat((hi-lo)/2))


def main():
    if not __debug__:
        raise RuntimeError("Run this certificate with Python assertions enabled.")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    ctx.prec = 140
    pi, I = arb.pi(), acb(0, 1)
    e.pi, e.I = pi, I
    a, b = arb(1)/32, arb(15)/32
    h = arb(3).log()/(4*pi)
    J = lambda z: e.Js(z, 1)
    jp = lambda z: e.jp(z, 1)

    def W(x, y):
        return (J(x+y)+J(2*x)-6*J(x)+J(2*y)-6*J(y)
                +I*pi*((x-y)**2+x+y)/2)

    def derivative(x, y):
        common = jp(x+y)
        return (common+2*jp(2*x)-6*jp(x)+I*pi*(x-y+arb(1)/2),
                common+2*jp(2*y)-6*jp(y)+I*pi*(y-x+arb(1)/2))

    z = acb(arb(1)/4, h)
    M = W(z, z).real
    complete_edge = (-8*J(arb(1)/4)).real
    extreme_wire = (2*(J(2*a)-4*J(a))).real
    wire_gap = M-complete_edge-extreme_wire
    assert wire_gap > arb(1)/32
    results = []
    for kind in ["single", "double"]:
        for ex in [a, b]:
            for ey in ([None] if kind == "single" else [a, b]):
                for sx in [1, -1]:
                    for sy in [1, -1]:
                        gap = arb(1)/(4 if kind == "single" else 2)
                        title = [kind, str(ex), None if ey is None else str(ey), sx, sy]

                        def coordinates(v, w):
                            x = acb(ex, sx*h*v)
                            if kind == "single":
                                y = acb(a+(b-a)*w, sy*h)
                            else:
                                y = acb(ey, sy*h*w)
                            return x, y

                        def penalty(v, w):
                            return 2*pi*h*((v if sx<0 else 0)
                                          +((1 if kind=="single" else w)
                                            if sy<0 else 0))

                        queue = [(Fraction(0),Fraction(1),Fraction(0),Fraction(1))]
                        accepted = []
                        visited = 0
                        while queue:
                            vl, vh, wl, wh = queue.pop()
                            visited += 1
                            assert visited < 2000000, title
                            vm, wm = (vl+vh)/2, (wl+wh)/2
                            vc, wc = rat(vm), rat(wm)
                            x0, y0 = coordinates(vc, wc)
                            center = W(x0,y0).real-penalty(vc,wc)-M
                            xb,yb=coordinates(ball(vl,vh),ball(wl,wh))
                            dx,dy=derivative(xb,yb)
                            gv=(I*sx*h*dx).real-(2*pi*h if sx<0 else 0)
                            if kind=="single":
                                gw=((b-a)*dy).real
                            else:
                                gw=(I*sy*h*dy).real-(2*pi*h if sy<0 else 0)
                            upper=(center+abs(gv)*rat((vh-vl)/2)
                                   +abs(gw)*rat((wh-wl)/2)).upper()
                            if upper < -gap:
                                accepted.append({"box":[str(vl),str(vh),str(wl),str(wh)],
                                                 "upper":str(upper)})
                            elif vh-vl >= wh-wl:
                                assert vh-vl > Fraction(1,2**30), (title,center,upper)
                                queue.extend([(vl,vm,wl,wh),(vm,vh,wl,wh)])
                            else:
                                assert wh-wl > Fraction(1,2**30), (title,center,upper)
                                queue.extend([(vl,vh,wl,wm),(vl,vh,wm,wh)])
                        results.append({"face":title,"gap":str(gap),
                                        "visited":visited,"accepted":accepted})
                        print("Certified",title,"in",visited,"rectangles.",flush=True)
    document={"precision_bits":ctx.prec,"action":str(M),
              "wire_gap":str(wire_gap),
              "height":str(h),"faces":results}
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(json.dumps(document,indent=2)+"\n")
    print("All",len(results),"endpoint faces have strict certified gaps.")


if __name__=="__main__":
    main()
