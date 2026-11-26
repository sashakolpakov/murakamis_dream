#!/usr/bin/env python3
"""Complete one missing equal-type face by exact symmetry; no proposals."""
import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import time

from flint import arb, acb, ctx
import certify_mixed_three_left_cut_support as original

ROOT=Path(__file__).resolve().parents[1]
PROOF=ROOT/"notes/research_mixed_three_left_cut_symmetry_completion.md"
PARTIAL=ROOT/"repro/results/research-mixed-three-left-cut-support-partial.json"
OUTPUT=ROOT/"repro/results/research-mixed-three-left-cut-support.json"
PARTIAL_SHA="3fdd788cbd235d72bdba3499111e7901485c807e0f9bea3c80492fdd6a869778"
ORIGINAL_PROOF_SHA="6d7647fe2de235b300dc71575bc4b63739cd849a1503568a89d41f3b6fe87e5a"
ORIGINAL_SCRIPT_SHA="ce8610602f0b5f0359be7cbc077551fbecc9289e82fc36f9a398f79e68d858d6"
CASES=[(a,b,face) for a,b in ((0,0),(0,1),(1,1)) for face in (0,1)]
COMPLETED_LEAVES=[77988,77988,45884,46577,25757]


def sha(path):
    with Path(path).open("rb") as f:
        return hashlib.file_digest(f,"sha256").hexdigest()


def split(box,depth,axis):
    assert axis==depth%3
    lo,hi=box[axis];mid=(lo+hi)/2
    left,right=list(box),list(box)
    left[axis]=(lo,mid);right[axis]=(mid,hi)
    return [(left,depth+1),(right,depth+1)]


def structure(domain):
    """Read tree topology only; do not repeat its source arithmetic."""
    todo=[([(Q(0),Q(1))]*3,0)]
    leaves=0;maximum_depth=0
    for node in domain["tree"]:
        assert todo,"node after exhausted cube"
        box,depth=todo.pop()
        assert len(node)==2
        if node[0]=="S":
            todo.extend(split(box,depth,node[1]))
        else:
            assert node[0]=="L"
            assert set(node[1])=={"witness","targets"}
            assert len(node[1]["targets"])==2
            assert all(len(row)==2 for row in node[1]["targets"])
            leaves+=1;maximum_depth=max(maximum_depth,depth)
    assert not todo,"incomplete purportedly complete face"
    assert leaves==domain["leaves"]
    assert len(domain["tree"])==2*leaves-1
    assert maximum_depth==domain["maximum_depth"]
    return leaves


def transport_leaf(leaf):
    """(z,p)->(Sz,Sp), with both output and input matrix slots swapped."""
    w=leaf["witness"]
    assert set(w)=={"centers","inverse","affine","radii"}
    assert all(len(w[k])==2 for k in w)
    assert all(len(row)==2 for k in ("inverse","affine") for row in w[k])
    swapped=dict(
        centers=list(reversed(w["centers"])),
        radii=list(reversed(w["radii"])),
        inverse=[[w["inverse"][1-i][1-j] for j in range(2)] for i in range(2)],
        affine=[[w["affine"][1-i][1-j] for j in range(2)] for i in range(2)])
    targets=list(reversed(leaf["targets"]))
    return dict(witness=swapped,targets=targets)


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--precision",type=int,default=256)
    ap.add_argument("--input",type=Path,default=PARTIAL)
    ap.add_argument("--output",type=Path,default=OUTPUT)
    args=ap.parse_args()
    assert args.precision==256,"This author completion is specified at 256 bits."
    assert not args.output.exists(),"Do not overwrite a completed canonical record."
    start=time.monotonic()
    ih=sha(args.input)
    assert ih==PARTIAL_SHA
    source=json.loads(args.input.read_text())
    assert source["status"]=="incomplete" and source["pilot"] is False
    assert source["stop_reason"]=="explicit node or time budget"
    assert source["precision_bits"]==256 and source["own_type"]==3
    assert source["left_cut"]=="3/20" and source["strict_gap"]=="1/2000"
    assert source["kappa"]==str(original.KAPPA)
    assert source["target_curvature"]==str(original.TARGET_CURVATURE)
    assert source["proof_sha256"]==ORIGINAL_PROOF_SHA==sha(original.PROOF)
    assert source["script_sha256"]==ORIGINAL_SCRIPT_SHA==sha(original.__file__)
    deps=source["dependencies_sha256"]
    assert len(deps)==24
    assert all(sha(ROOT/p)==h for p,h in deps.items())
    ph,sh=sha(PROOF),sha(__file__)

    domains=source["domains"]
    assert source["domain_count"]==len(domains)==5
    assert [tuple(d["case"]) for d in domains]==CASES[:5]
    assert [structure(d) for d in domains]==COMPLETED_LEAVES
    active=source["incomplete_domain"]
    assert active["case"]==[1,1,1] and active["leaves"]==18527
    assert source["accepted_cells"]==sum(COMPLETED_LEAVES)+active["leaves"]==292721
    assert source["visited_nodes"]==585445
    assert sum(len(d["tree"]) for d in domains)+len(active["tree"])==585445
    assert sum(n[0]=="L" for n in active["tree"])==active["leaves"]
    # The partial sixth tree remains solely in the immutable input record.
    # Its leaves are not imported into the complete canonical output.
    template=domains[4]
    assert template["case"]==[1,1,0] and template["leaves"]==25757
    print("PASS structure",5,sum(COMPLETED_LEAVES),"completed leaves; transport begins",flush=True)

    ctx.prec=args.precision
    original.PI=arb.pi();original.II=acb(0,1)
    original.old.PI=original.PI;original.old.II=original.II
    original.old.base.PI=original.PI;original.old.base.I=original.II
    todo=[([(Q(0),Q(1))]*3,0)]
    tree=[];leaves=0;maximum_depth=0;maximum=None
    last_log=time.monotonic()
    for node in template["tree"]:
        assert todo
        box,depth=todo.pop()
        if node[0]=="S":
            todo.extend(split(box,depth,node[1]))
            tree.append(node)
            continue
        assert node[0]=="L"
        leaf=transport_leaf(node[1])
        pp,dp=original.parameters(box,(1,1),1)
        p0,_=original.parameters([((lo+hi)/2,)*2 for lo,hi in box],(1,1),1)
        certificate=original.old.root_box(leaf["witness"],pp,p0,0)
        assert certificate is not None,("transported original root",leaves,box)
        rows,detail=original.check_source(
            box,pp,p0,dp,certificate,(1,1),leaf["targets"])
        assert rows is not None,("transported source",leaves,box,detail)
        tree.append(["L",leaf])
        leaves+=1;maximum_depth=max(maximum_depth,depth)
        for row in rows:
            value=arb(row["upper_bound"]).upper()
            maximum=value if maximum is None else max(maximum,value)
        now=time.monotonic()
        if now-last_log>=10:
            print("transport",leaves,"of",25757,round(now-start,2),"seconds",flush=True)
            last_log=now
    assert not todo
    assert leaves==25757 and len(tree)==2*leaves-1
    transported=dict(case=[1,1,1],leaves=leaves,tree=tree,
                     maximum_upper=str(maximum),maximum_depth=maximum_depth)
    assert structure(transported)==leaves
    complete=domains+[transported]
    assert [tuple(d["case"]) for d in complete]==CASES
    total=sum(d["leaves"] for d in complete)
    assert total==299951
    assert sum(len(d["tree"]) for d in complete)==2*total-6==599896

    assert sha(args.input)==ih
    assert sha(original.PROOF)==ORIGINAL_PROOF_SHA
    assert sha(original.__file__)==ORIGINAL_SCRIPT_SHA
    assert sha(PROOF)==ph and sha(__file__)==sh
    assert all(sha(ROOT/p)==h for p,h in deps.items())
    elapsed=time.monotonic()-start
    result={k:v for k,v in source.items()
            if k not in ("incomplete_domain","stop_reason")}
    result.update(status="passed",domains=complete,domain_count=6,
                  accepted_cells=total,visited_nodes=2*total-6,
                  elapsed_seconds=source["elapsed_seconds"]+elapsed,
                  input_sha256=ih,
                  symmetry_completion=dict(
                      proof_path=str(PROOF.relative_to(ROOT)),proof_sha256=ph,
                      helper_path=str(Path(__file__).resolve().relative_to(ROOT)),
                      helper_sha256=sh,
                      partial_input_path=str(args.input.resolve().relative_to(ROOT)),
                      partial_input_sha256=ih,
                      source_face=[1,1,0],target_face=[1,1,1],
                      completed_input_faces=5,completed_input_leaves=COMPLETED_LEAVES,
                      transported_leaves=leaves,transported_nodes=len(tree),
                      proposals_enabled=False,refinements=0,
                      prior_source_arithmetic_repeated=False,
                      transport_precision_bits=args.precision,
                      original_author_elapsed_seconds=source["elapsed_seconds"],
                      validation_elapsed_seconds=elapsed))
    # Preserve exactly the original dependency dictionary and verifier hashes,
    # so the original saved-replay path checks all six faces without changes.
    assert result["dependencies_sha256"]==deps
    assert result["proof_sha256"]==ORIGINAL_PROOF_SHA
    assert result["script_sha256"]==ORIGINAL_SCRIPT_SHA
    args.output.parent.mkdir(parents=True,exist_ok=True)
    tmp=args.output.with_name(args.output.name+".tmp")
    with tmp.open("w") as f:
        json.dump(result,f,indent=2)
        f.write("\n")
    assert sha(args.input)==ih and sha(PROOF)==ph and sha(__file__)==sh
    assert sha(original.PROOF)==ORIGINAL_PROOF_SHA
    assert sha(original.__file__)==ORIGINAL_SCRIPT_SHA
    assert all(sha(ROOT/p)==h for p,h in deps.items())
    tmp.replace(args.output)
    print("PASS symmetry completion",6,total,2*total-6,len(deps),
          round(elapsed,2),"seconds",flush=True)
    print("OUTPUT",args.output,"SHA256",sha(args.output),flush=True)
    return 0


if __name__=="__main__":
    raise SystemExit(main())
