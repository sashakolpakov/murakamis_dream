#!/usr/bin/env python3
"""One fixed original-log witness; no proposals, search, or subdivisions."""
import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path

from flint import arb, acb, ctx
import certify_mixed_reduced_disk_conditional_packets as source

ROOT=Path(__file__).resolve().parents[1]
PROOF=ROOT/"notes/research_mixed_left_cut_independent_reference_obstruction.md"
STEM="research-mixed-left-cut-independent-reference-obstruction"
POINT="repro/diagnostics/2026-11-05-left-cut-weak-reference/local-result.json"
ANGLES=["382614753601/1000000000000","121984810683/200000000000"]
TARGET=["11/50","22252624287/50000000000"]

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--precision",type=int,default=256)
    ap.add_argument("--input",type=Path)
    ap.add_argument("--output",type=Path,default=ROOT/"repro/results"/(STEM+".json"))
    args=ap.parse_args()
    assert args.precision>=192
    ctx.prec=args.precision
    source.PI=arb.pi();source.II=acb(0,1)
    source.base.PI=arb.pi();source.base.I=acb(0,1)
    deps={}
    def bind(name,expected=None):
        h=sha(ROOT/name)
        if expected is not None:assert h==expected,name
        if name in deps:assert deps[name]==h,name
        deps[name]=h
        return h
    def read(name):
        bind(name)
        obj=json.loads((ROOT/name).read_text())
        assert obj.get("status")=="passed",name
        for p,h in obj.get("dependencies_sha256",{}).items():bind(p,h)
        return obj
    author_name="repro/results/research-mixed-reduced-disk-conditional-packets.json"
    replay_name="repro/results/research-mixed-reduced-disk-conditional-packets-replay.json"
    author=read(author_name);replay=read(replay_name)
    assert replay["input_sha256"]==deps[author_name]
    for obj in (author,replay):
        bind("notes/research_mixed_reduced_disk_conditional_packets.md",obj["proof_sha256"])
        bind("experiments/certify_mixed_reduced_disk_conditional_packets.py",obj["script_sha256"])
    assert author["domains"]==replay["domains"] or all(
        a["types"]==b["types"] and a["tree"]==b["tree"]
        and a["leaves"]==b["leaves"]
        for a,b in zip(author["domains"],replay["domains"]))
    assert author["domain_count"]==replay["domain_count"]==6
    bind(POINT)
    point=json.loads((ROOT/POINT).read_text())
    assert point["source_sha256"]==deps[author_name]
    assert point["helper_sha256"]==deps["experiments/certify_mixed_reduced_disk_conditional_packets.py"]
    assert point["angles"]==ANGLES and point["target"]==TARGET
    witness=point["point_witness"]
    ph,sh=sha(PROOF),sha(__file__)
    old=None;ih=None
    if args.input:
        ih=sha(args.input);old=json.loads(args.input.read_text())
        assert old["status"]=="passed"
        assert old["proof_sha256"]==ph and old["script_sha256"]==sh
        assert old["dependencies_sha256"]==deps
        assert old["angles"]==ANGLES and old["target"]==TARGET
        assert old["point_witness"]==witness
        witness=old["point_witness"]

    box=[(Q(t),Q(t)) for t in ANGLES]
    pp=source.parameter(box,(0,1))
    certificate=source.root_box(witness,pp,pp,1)
    assert certificate is not None,"original zero-lift root witness"
    s,b=certificate["point"];a,c=pp
    ar=source.ar
    assert Q("11/50")<=Q(TARGET[0])<=Q("9/20")
    assert Q("11/50")<=Q(TARGET[1])<=Q("9/20")
    for z,rl,ru,il,iu in (
        (a,"288/1000","289/1000","45/1000","46/1000"),
        (c,"253/1000","254/1000","-91/1000","-90/1000"),
        (s,"267/1000","268/1000","-88/1000","-87/1000"),
        (b,"332/1000","333/1000","-58/1000","-57/1000")):
        assert ar(rl)<z.real<ar(ru) and ar(il)<z.imag<ar(iu)
        assert abs(z.imag)<ar("27/250")
    aa=acb(ar(TARGET[0]),a.imag)
    bb=acb(ar(TARGET[1]),b.imag)
    cut=acb(ar("3/20"))
    for z in (s,a,b,s+a,s+b,cut,aa,bb,cut+aa,cut+bb):
        assert 0<z.real<1
    assert bb.imag<0
    lam=ar("3/2")
    F=source.phase(s,a,b,1)-source.g(a)-lam*source.g(b)
    pa=(source.gp(s+a)-source.gp(a)+2*source.PI*source.II*s).real
    pb=(source.gp(s+b)-lam*source.gp(b)).real
    row=(source.phase(cut,aa,bb,1)-source.g(aa)-lam*source.g(bb)).real
    excess=row-F.real-pa*(aa.real-a.real)-pb*(bb.real-b.real)
    assert excess>ar("1/1000"),"strict allocated affine-plane excess"
    assert sha(PROOF)==ph and sha(__file__)==sh
    assert all(sha(ROOT/p)==h for p,h in deps.items())
    if args.input:assert sha(args.input)==ih
    result=dict(
        status="passed",precision_bits=args.precision,
        angles=ANGLES,target=TARGET,own_type=4,external_types=[3,4],
        point_witness=witness,root_witness_count=1,parameter_subdivisions=0,
        proof_sha256=ph,script_sha256=sh,dependencies_sha256=deps,input_sha256=ih,
        reference_enclosures=dict(a=str(a),external_c=str(c),s=str(s),b=str(b)),
        allocated_reference_rate=str(F.real),marginals=[str(pa),str(pb)],
        allocated_cut_rate=str(row),excess=str(excess),strict_excess_floor="1/1000",
        scope="A single auxiliary independent-reference fixed-left-cut obstruction; "
              "no actual-word realization or complete finite-source lower bound.")
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+"\n")
    print("PASS one original-log point witness, zero subdivisions,",len(deps),
          "current bindings, excess",excess,"> 1/1000")

if __name__=="__main__":
    main()
