#!/usr/bin/env python3
"""Complete terminal-C source tests on four existing endpoint-map graphs.

Only old accepted rectangles intersecting the input disk boundary are used.
Every such original logarithmic root witness is revalidated; no root or
parameter subdivision is proposed.  Source gaps and complete contour
intervals are evaluated anew, retaining every revived endpoint branch.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import time

from flint import acb, acb_mat, arb, ctx
import certify_mixed_open_word_critical_localization as base

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / "notes/research_mixed_terminal_conditional_source_reduction.md"
ar, cp = base.ar, base.cp


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def g(z):
    return ((-2*PI*II*z).exp().polylog(2)-PI*PI/6)/(2*PI*II)


def gp(z):
    return (1-(-2*PI*II*z).exp()).log()


def phase(t, a, e, eps):
    return g(t+a)+g(t+e)-(2+eps)*g(t)+2*PI*II*a*t


def uppermax(values):
    return max(value.upper() for value in values)


def response(z, a, eps, witness):
    """Validated e'(a), using the original inverse proposal and Neumann tail."""
    J = base.jacobian(z, a, eps)
    Y = acb_mat([[cp(v) for v in row] for row in witness["inverse"]])
    E = base.ident(3)-Y*J
    rho = uppermax([sum((abs(E[i,j]) for j in range(3)), arb(0))
                    for i in range(3)])
    assert 0 <= rho < 1, ("response contraction", rho)
    forcing = acb_mat([[0], [PI*(PI*(z[1]+a)).cot()+II*PI], [0]])
    term = -(Y*forcing)
    result = acb_mat(term)
    residual_norm = uppermax([abs(term[j,0]) for j in range(3)])
    for _ in range(4):
        term = E*term
        result += term
    tail = residual_norm*rho**5/(1-rho)
    return result[0,0]+acb(arb(0,tail.upper()),arb(0,tail.upper()))


def test(box, eps, neighbor, witness):
    a = base.parameter(box, neighbor)
    assert base.test(witness, a, eps) is not None, "old whole-cell root witness"
    a0 = base.parameter([(sum(interval,F(0))/2,)*2 for interval in box], neighbor)
    z0 = list(map(cp, witness["centers"]))
    radius = ar(witness["radius"])
    z = [v+acb(arb(0,radius),arb(0,radius)) for v in z0]
    e,t,u = z
    assert all(ar(".23")<v.real<ar(".45") and ar("-.12")<v.imag<ar(".12")
               for v in (a,e)), "old universal curvature domain"
    assert ar(".24")<t.real<ar(".40") and abs(t.imag)<ar(".12")
    # The existing rational center and inverse are also tested at the
    # parameter midpoint with a new, tiny radius; this is not a root proposal.
    point = dict(witness, radius="1/10000000000")
    assert base.test(point, a0, eps) is not None, "original midpoint lift"
    point_radius = ar(point["radius"])
    ep,tp,up = [v+acb(arb(0,point_radius),arb(0,point_radius)) for v in z0]
    eprime = response(z,a,eps,witness)
    external_radius = base.DISKS[neighbor][2]
    halfwidths = [ar(external_radius*(hi-lo)/2) for lo,hi in box]
    selected = phase(tp,a0,ep,eps)
    ga = gp(t+a)+2*PI*II*t
    ge = gp(t+e)

    def lower(value, da, de):
        derivative = da+de*eprime
        return (value.real-abs(derivative.real)*halfwidths[0]
                -abs(derivative.imag)*halfwidths[1])

    cuts = []
    for c in (acb(ar("3/20")),acb(ar("49/100"))):
        bound = lower(selected-phase(c,a0,ep,eps),
                      ga-gp(c+a)-2*PI*II*c,ge-gp(c+e))
        assert bound>ar("1/1000"), ("real cut", eps, neighbor, c, bound)
        cuts.append(bound.lower())
    revived = []
    for v in (0,1):
        for w in (0,1):
            bound = lower(selected-g(a0)-g(ep)-2*PI*II*v*a0+2*PI*II*w*ep,
                          ga-gp(a)-2*PI*II*v,ge-gp(e)+2*PI*II*w)
            assert bound>ar("1/1000"), ("last row",eps,neighbor,v,w,bound)
            revived.append(bound.lower())
    aliases = []
    for sign in (-1,1):
        one_side = []
        for j in range(8):
            x = ar(F(3,20)+F(34,100)*F(j,8)).union(
                ar(F(3,20)+F(34,100)*F(j+1,8)))
            c = acb(x,sign*ar("1/5"))
            bound = lower(selected-phase(c,a0,ep,eps),
                          ga-gp(c+a)-2*PI*II*c,ge-gp(c+e))+2*PI/5
            assert bound>ar("1/10"), ("whole alias",eps,neighbor,sign,j,bound)
            one_side.append(bound.lower())
        aliases.append(min(one_side))

    qa = (2*PI*a.real).sin()/((2*PI*a.imag).cosh()-(2*PI*a.real).cos())
    qe = (2*PI*e.real).sin()/((2*PI*e.imag).cosh()-(2*PI*e.real).cos())
    assert qa>0 and qe>0
    wl,wr = -1/(49*PI/100).tan(),uppermax([qa,qe])
    ca,sa,ce,se = (PI*a).cos(),(PI*a).sin(),(PI*e).cos(),(PI*e).sin()
    factor = (2*PI*(e.imag-a.imag)).exp()/4**eps
    shapes = []
    for j in range(12):
        w = (wl+(wr-wl)*j/12).union(wl+(wr-wl)*(j+1)/12)
        value = factor*abs(ca-w*sa)**2*abs(ce-w*se)**2*(1+w*w)**eps
        assert value<1, ("right-tail shape",eps,neighbor,j,value)
        shapes.append(value.upper())
    return cuts+revived+aliases+[max(shapes)]


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision",type=int,default=256)
    parser.add_argument("--input",type=Path)
    parser.add_argument("--output",type=Path,default=ROOT /
                        "repro/results/research-mixed-terminal-conditional-source.json")
    parser.add_argument("--max-seconds",type=float,default=300)
    args=parser.parse_args()
    assert args.precision>=192
    ctx.prec=args.precision
    global PI,II
    PI,II=arb.pi(),acb(0,1)
    ph,sh=sha(PROOF),sha(__file__)
    ih=sha(args.input) if args.input else None
    old=json.loads(args.input.read_text()) if args.input else None
    deps={}

    def bind(path, expected=None):
        digest=sha(ROOT/path)
        if expected is not None:assert digest==expected,path
        assert path not in deps or deps[path]==digest,path
        deps[path]=digest
        return digest

    def read(path):
        bind(path)
        r=json.loads((ROOT/path).read_text())
        assert r["status"]=="passed",path
        for name in ("dependencies","dependencies_sha256"):
            for p,h in r.get(name,{}).items():bind(p,h)
        return r

    rp="repro/results/research-mixed-open-word-critical-localization.json"
    rr="repro/results/research-mixed-open-word-critical-localization-replay.json"
    roots,replay=read(rp),read(rr)
    assert replay["input_sha256"]==deps[rp]
    assert replay["domains"]==roots["domains"]
    for record in (roots,replay):
        bind("notes/research_mixed_open_word_critical_localization.md",record["proof_sha256"])
        bind("experiments/certify_mixed_open_word_critical_localization.py",record["script_sha256"])
    image=read("repro/results/research-mixed-open-word-endpoint-rectangles.json")
    bind("notes/research_mixed_open_word_endpoint_rectangles.md",image["proof_sha256"])
    bind("experiments/check_mixed_open_word_endpoint_rectangles.py",image["script_sha256"])
    old_source=read("repro/results/research-mixed-conditional-image-contours.json")
    bind("notes/research_mixed_conditional_image_contours.md",old_source["proof_sha256"])
    bind("experiments/check_mixed_conditional_image_contours.py",old_source["script_sha256"])
    for name in ("mixed_conditional_critical_images","mixed_three_canonical_conditional",
                 "mixed_four_conditional_complex_neighbors","mixed_conditional_torus_composition"):
        bind(f"notes/research_{name}.md")
    if old:
        assert old["status"]=="passed" and old["proof_sha256"]==ph and old["script_sha256"]==sh
        assert old["dependencies_sha256"]==deps
    specs=[(e,n) for e in (0,1) for n in (0,1)]
    assert [(d["epsilon"],d["neighbor_epsilon"]) for d in roots["domains"]]==specs
    start=time.monotonic()
    domains=[]
    total_boundary=total_inside=total_outside=total_nodes=0
    for index,domain in enumerate(roots["domains"]):
        eps,neighbor=specs[index]
        pending=[([(F(-1),F(1)),(F(-1),F(1))],0)]
        counts=dict(boundary=0,inside=0,outside=0)
        checked=[]
        extrema=[None]*9
        for number,node in enumerate(domain["tree"]):
            assert pending,"extra source-tree nodes"
            box,depth=pending.pop()
            total_nodes+=1
            assert time.monotonic()-start<args.max_seconds,"runtime cap"
            if node[0]=="S":
                assert len(node)==2 and node[1]==depth%2
                left,right=base.split(box,node[1])
                pending.extend([(left,depth+1),(right,depth+1)])
                continue
            if node[0]=="X":
                assert len(node)==1 and base.excluded(box)
                counts["outside"]+=1
                continue
            assert node[0]=="L" and len(node)==2 and not base.excluded(box)
            if sum(max(lo*lo,hi*hi) for lo,hi in box)<1:
                counts["inside"]+=1
                continue
            values=test(box,eps,neighbor,node[1])
            checked.append(number)
            counts["boundary"]+=1
            for j,value in enumerate(values):
                if extrema[j] is None:extrema[j]=value
                elif j==8:extrema[j]=max(extrema[j],value)
                else:extrema[j]=min(extrema[j],value)
        assert not pending
        assert counts["boundary"]+counts["inside"]==domain["leaves"]
        assert counts["outside"]==domain["excluded"]
        expected=[177,180,142,133][index]
        assert counts["boundary"]==expected,(index,counts)
        row=dict(epsilon=eps,neighbor_epsilon=neighbor,counts=counts,
                 original_leaf_node_indices=checked,extrema=list(map(str,extrema)))
        if old:
            prior=old["domains"][index]
            for key in ("epsilon","neighbor_epsilon","counts","original_leaf_node_indices"):
                assert row[key]==prior[key],key
        domains.append(row)
        total_boundary+=counts["boundary"]
        total_inside+=counts["inside"]
        total_outside+=counts["outside"]
        print("PASS terminal source",eps,neighbor,counts,"seconds",
              round(time.monotonic()-start,2),flush=True)
    assert (total_boundary,total_inside,total_outside,total_nodes)==(632,4626,233,10978)
    assert sha(PROOF)==ph and sha(__file__)==sh
    assert all(sha(ROOT/p)==h for p,h in deps.items())
    if args.input:assert sha(args.input)==ih
    result=dict(status="passed",precision_bits=args.precision,domains=domains,
        boundary_witnesses=total_boundary,interior_witnesses_omitted=total_inside,
        original_outside_exclusions=total_outside,validated_original_tree_nodes=total_nodes,
        original_endpoint_witnesses=5258,new_parameter_subdivisions=0,new_root_proposals=0,
        real_cut_and_last_row_gap="1/1000",horizontal_alias_gap="1/10",
        right_tail_shape_upper="1",middle_rectangle=["3/20","49/100","-1/5","1/5"],
        alias_intervals_per_side=8,tail_shape_intervals=12,point_radius="1/10000000000",
        response_terms=5,response_tail_power=5,
        proof_sha256=ph,script_sha256=sh,dependencies_sha256=deps,input_sha256=ih,
        elapsed_seconds=time.monotonic()-start,
        scope="New whole-cell finite-source inequalities on the four correlated endpoint "
              "graphs, using original endpoint witnesses and complete tree validation. "
              "All rows/aliases retained; no remaining open-word contour bound.")
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+"\n")
    print("PASS",total_boundary,"existing boundary witnesses",total_nodes,
          "tree nodes",len(deps),"bindings",round(time.monotonic()-start,2),"seconds",flush=True)


if __name__=="__main__":
    main()
