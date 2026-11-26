#!/usr/bin/env python3
"""Whole ordinary-reference boundary, own-three left cut; saved replay has no proposals."""
import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import sys
import time

import numpy as np
from scipy.optimize import brentq
from flint import arb, acb, ctx

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"experiments"))
import certify_mixed_reduced_disk_conditional_packets as old

ar=old.ar
PROOF=ROOT/"notes/research_mixed_three_left_cut_support.md"
STEM="research-mixed-three-left-cut-support"
GAP=Q(1,2000)
OWN=0
CUT=Q(3,20)
KAPPA=Q(1,2500000)
TARGET_CURVATURE=Q(6,5)-2*KAPPA

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def iv(pair):
    return ar(pair[0]).union(ar(pair[1]))

def parameters(box,types,face):
    """(circle angle, other disk radius, other disk angle); face is circle slot."""
    theta,rho,phi=map(iv,box)
    values=[None,None]
    derivative=[[acb(0) for _ in range(3)] for _ in range(2)]
    for slot,t in enumerate(types):
        center=acb(ar(old.CENTERS[t][0]),ar(old.CENTERS[t][1]))
        if slot==face:
            w=ar(old.RADII[t])*(2*PI*II*theta).exp()
            values[slot]=center+w
            derivative[slot][0]=2*PI*II*w
        else:
            w=ar(old.RADII[t])*(2*PI*II*phi).exp()
            values[slot]=center+rho*w
            derivative[slot][1]=w
            derivative[slot][2]=2*PI*II*rho*w
    return values,derivative


def propose(pp,p0):
    fp=[complex(float(z.real.mid()),float(z.imag.mid())) for z in p0]
    roots,D,res=old.base.block([fp[0].real,fp[0].imag,
                                fp[1].real,fp[1].imag],OWN)
    if res>1e-9:return None
    centers=[old.encode(z) for z in roots]
    _,J0=old.base.evalf(list(map(old.cp,centers)),*p0,2+OWN)
    JJ=np.array([[complex(float(z.real.mid()),float(z.imag.mid())) for z in row]
                 for row in J0])
    Y=np.linalg.inv(JJ)
    witness=dict(centers=centers,
                 inverse=[[old.encode(z) for z in row] for row in Y],
                 affine=[[old.encode(z) for z in row] for row in D])
    *_,bb=old.components(witness,pp,p0,OWN)
    if any(not z.is_finite() for z in bb):return None
    for factor in (Q(5,4),Q(3,2),Q(2)):
        witness["radii"]=[str(Q(max(1,int(np.ceil(float(z.upper())*
                                               float(factor)*2**40))),2**40))
                          for z in bb]
        certificate=old.root_box(witness,pp,p0,OWN)
        if certificate is not None:return witness,certificate
    return None

def g2(z):
    q=(-2*PI*II*z).exp()
    return 2*PI*II*q/(1-q)

def phase(s,a,b,eta):
    return old.phase(s,a,b,OWN)-(1+ar(eta)/2)*old.g(a)-(1+ar(OWN)/2)*old.g(b)

def marginals(s,a,b,eta):
    return [old.gp(s+a)-(1+ar(eta)/2)*old.gp(a)+2*PI*II*s,
            old.gp(s+b)-(1+ar(OWN)/2)*old.gp(b)]

def hessian(s,a,b,eta):
    ss=g2(s+a)+g2(s+b)-(2+OWN)*g2(s)
    assert abs(ss)>0
    off=[g2(s+a)+2*PI*II,g2(s+b)]
    diagonal=[g2(s+a)-(1+ar(eta)/2)*g2(a),
              g2(s+b)-(1+ar(OWN)/2)*g2(b)]
    return [[(diagonal[i] if i==j else acb(0))-off[i]*off[j]/ss
             for j in range(2)] for i in range(2)]

def trial_targets(s,a,b,eta):
    """Floating trial only; outward quadratic bounds handle every target."""
    sf,af,bf=[complex(float(z.real.mid()),float(z.imag.mid())) for z in (s,a,b)]
    gp=lambda z:np.log(1-np.exp(-2j*np.pi*z))
    p=[(gp(sf+af)-(1+eta/2)*gp(af)+2j*np.pi*sf).real,
       (gp(sf+bf)-(1+OWN/2)*gp(bf)).real]
    trial=[]
    for z,lam,marginal in ((af,1+eta/2,p[0]),(bf,1+OWN/2,p[1])):
        def f(x):
            zz=x+1j*z.imag
            return (gp(float(CUT)+zz)-lam*gp(zz)).real-marginal
        if f(.22)<=0:x=.22
        elif f(.45)>=0:x=.45
        else:x=brentq(f,.22,.45,xtol=1e-13)
        trial.append(Q(round(x*10**12),10**12))
    return trial

def one_sided_quadratic(slope,length):
    """sup_{0<=d<=length} slope*d-curvature*d^2/2, outward."""
    if length==0 or slope<=0:return arb(0)
    beta=max(slope.upper(),arb(0))
    if beta>=ar(TARGET_CURVATURE*length):
        return beta*ar(length)-ar(TARGET_CURVATURE*length*length)/2
    return beta*beta/(2*ar(TARGET_CURVATURE))

def quadratic_gain(beta,trial):
    # The sign-separated intervals also cover an uncertain sign at zero.
    plus=one_sided_quadratic(beta.upper(),Q(9,20)-trial)
    minus=one_sided_quadratic((-beta).upper(),trial-Q(11,50))
    return max(arb(0),plus.upper(),minus.upper())

def check_source(box,pp,p0,dp,certificate,types,targets=None):
    roots=certificate["root"]
    points=certificate["point"]
    response=certificate["response"]
    halfwidth=[ar((hi-lo)/2) for lo,hi in box]
    rows=[]
    for side in (0,1):
        eta=types[side]
        a,s,b=pp[side],roots[side],roots[1-side]
        a0,s0,b0=p0[side],points[side],points[1-side]
        trial=(trial_targets(s0,a0,b0,eta) if targets is None
               else list(map(Q,targets[side])))
        assert len(trial)==2 and all(Q(11,50)<=v<=Q(9,20) for v in trial)
        aa=acb(ar(trial[0]),a.imag);bb=acb(ar(trial[1]),b.imag)
        aa0=acb(ar(trial[0]),a0.imag);bb0=acb(ar(trial[1]),b0.imag)
        cut=acb(ar(CUT))
        P=marginals(s,a,b,eta)
        P0=marginals(s0,a0,b0,eta)
        Pc=marginals(cut,aa,bb,eta)
        H=hessian(s,a,b,eta)
        delta=[aa.real-a.real,bb.real-b.real]
        delta0=[aa0.real-a0.real,bb0.real-b0.real]
        midpoint=(phase(cut,aa0,bb0,eta)-phase(s0,a0,b0,eta)).real
        midpoint-=sum((P0[i].real*delta0[i] for i in range(2)),arb(0))
        midpoint+=ar(KAPPA)*sum((v*v for v in delta0),arb(0))
        HD=[sum((H[i][j]*delta[j] for j in range(2)),acb(0)) for i in range(2)]
        DU=[-HD[i].real-2*ar(KAPPA)*delta[i] for i in range(2)]
        DH=[(P[i]-Pc[i]+HD[i]).imag for i in range(2)]
        Zder=[dp[side],
              [sum((response[1-side][j]*dp[j][axis] for j in range(2)),acb(0))
               for axis in range(3)]]
        parameter_derivative=[
            sum((DU[i]*Zder[i][axis].real+DH[i]*Zder[i][axis].imag
                 for i in range(2)),arb(0)) for axis in range(3)]
        meanvalue=sum((abs(parameter_derivative[i])*halfwidth[i]
                       for i in range(3)),arb(0))
        slopes=[Pc[i].real-P[i].real+2*ar(KAPPA)*delta[i] for i in range(2)]
        gains=[quadratic_gain(slopes[i],trial[i]) for i in range(2)]
        bound=midpoint+meanvalue+sum(gains,arb(0))
        rows.append(dict(side=side,trial=[str(v) for v in trial],
                         midpoint=str(midpoint),meanvalue=str(meanvalue),
                         gains=[str(v) for v in gains],upper_bound=bound.upper().str(70)))
        if midpoint>-ar(GAP):
            return None,dict(reason="point exceeds requested gap",rows=rows)
        if not bound<-ar(GAP):return None,dict(reason="interval bound",rows=rows)
    return rows,dict(reason="passed",rows=rows)


def main():
    global PI,II
    ap=argparse.ArgumentParser()
    ap.add_argument("--precision",type=int,default=256)
    ap.add_argument("--max-nodes",type=int,default=600000)
    ap.add_argument("--max-seconds",type=float,default=600)
    ap.add_argument("--max-depth",type=int,default=45)
    ap.add_argument("--pilot",action="store_true")
    ap.add_argument("--input",type=Path)
    ap.add_argument("--output",type=Path,default=ROOT/"repro/results"/(STEM+".json"))
    args=ap.parse_args()
    assert args.precision>=192 and args.max_nodes>0 and args.max_seconds>0
    if args.pilot:
        assert args.input is None
        args.max_nodes=min(args.max_nodes,511)
        args.max_seconds=min(args.max_seconds,60)
    ctx.prec=args.precision
    PI=arb.pi();II=acb(0,1)
    old.PI=PI;old.II=II;old.base.PI=PI;old.base.I=II
    assert Q(27,67)*Q(3)>Q(6,5)
    assert Q(11,18)<1
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
        assert obj["status"]=="passed",name
        for p,h in obj.get("dependencies_sha256",{}).items():bind(p,h)
        return obj
    source_name="repro/results/research-mixed-reduced-disk-conditional-packets.json"
    replay_name="repro/results/research-mixed-reduced-disk-conditional-packets-replay.json"
    author,previous=read(source_name),read(replay_name)
    assert previous["input_sha256"]==deps[source_name]
    assert author["domain_count"]==previous["domain_count"]==6
    assert len(author["domains"])==len(previous["domains"])==6
    for a,b in zip(author["domains"],previous["domains"]):
        assert a["types"]==b["types"] and a["tree"]==b["tree"]
        assert a["leaves"]==b["leaves"]
    for rec in (author,previous):
        bind("notes/research_mixed_reduced_disk_conditional_packets.md",rec["proof_sha256"])
        bind("experiments/certify_mixed_reduced_disk_conditional_packets.py",rec["script_sha256"])
    for name in (
        "research_mixed_four_left_cut_support",
        "research_mixed_horizontal_tail_reference_boundary",
        "research_mixed_half_index_contour",
        "research_mixed_horizontal_zero_mode_support",
        "research_mixed_horizontal_asymmetric_contour",
        "research_mixed_horizontal_real_cut_optimization"):
        bind("notes/"+name+".md")
    ph,sh=sha(PROOF),sha(__file__)
    source_input=None;ih=None
    if args.input:
        ih=sha(args.input)
        source_input=json.loads(args.input.read_text())
        assert source_input["status"]=="passed"
        assert source_input["proof_sha256"]==ph and source_input["script_sha256"]==sh
        assert source_input["dependencies_sha256"]==deps
        assert source_input["strict_gap"]==str(GAP)
    specs=[(ta,tb,face) for ta,tb in ((0,0),(0,1),(1,1)) for face in (0,1)]
    if args.pilot:specs=[(0,0,0)]
    if source_input:
        assert [tuple(d["case"]) for d in source_input["domains"]]==specs
    start=time.monotonic();last_log=start
    visits=leaves=0
    domains=[]
    failure_counts={"root":0,"source":0}
    def snapshot(status,active=None,reason=None):
        assert sha(PROOF)==ph and sha(__file__)==sh
        assert all(sha(ROOT/p)==h for p,h in deps.items())
        if args.input:assert sha(args.input)==ih
        result=dict(status=status,precision_bits=args.precision,
                    strict_gap=str(GAP),left_cut=str(CUT),own_type=3+OWN,
                    pilot=args.pilot,kappa=str(KAPPA),
                    target_curvature=str(TARGET_CURVATURE),
                    parameter_domain="circle times closed disk",
                    domains=domains,domain_count=len(domains),
                    conditional_orientations=2,visited_nodes=visits,
                    proposals_enabled=args.input is None,
                    accepted_cells=leaves,failure_counts=failure_counts,
                    proof_sha256=ph,script_sha256=sh,
                    dependencies_sha256=deps,input_sha256=ih,
                    elapsed_seconds=time.monotonic()-start,
                    scope="All own-three ordinary reduced reference families only; "
                          "formal auxiliary allocation and actual physical subset distinguished.")
        if active is not None:result["incomplete_domain"]=active
        if reason is not None:result["stop_reason"]=reason
        path=(args.output if status=="passed" else
              args.output.with_name(args.output.stem+"-partial.json"))
        path.parent.mkdir(parents=True,exist_ok=True)
        path.write_text(json.dumps(result,indent=2)+"\n")
        return path
    for case_index,(ta,tb,face) in enumerate(specs):
        types=(ta,tb)
        todo=[([(Q(0),Q(1))]*3,0)]
        tree=[];cursor=local_leaves=0
        maximum=None;max_depth=0
        old_domain=source_input["domains"][case_index] if source_input else None
        while todo:
            if visits>=args.max_nodes or time.monotonic()-start>=args.max_seconds:
                active=dict(case=[ta,tb,face],tree=tree,leaves=local_leaves,
                            pending=[[[[str(v) for v in p] for p in box],depth]
                                     for box,depth in todo],input_cursor=cursor)
                path=snapshot("incomplete",active,"explicit node or time budget")
                print("INCOMPLETE",visits,leaves,"saved",path,flush=True)
                return 2
            box,depth=todo.pop();visits+=1
            pp,dp=parameters(box,types,face)
            p0,_=parameters([((lo+hi)/2,)*2 for lo,hi in box],types,face)
            if old_domain:
                assert cursor<len(old_domain["tree"])
                node=old_domain["tree"][cursor];cursor+=1
                if node[0]=="S":
                    assert len(node)==2 and node[1]==depth%3
                    axis=node[1];lo,hi=box[axis];mid=(lo+hi)/2
                    left,right=list(box),list(box)
                    left[axis]=(lo,mid);right[axis]=(mid,hi)
                    todo.extend([(left,depth+1),(right,depth+1)])
                    tree.append(node)
                    continue
                assert node[0]=="L" and len(node)==2
                w=node[1]["witness"];targets=node[1]["targets"]
                assert len(targets)==2
                certificate=old.root_box(w,pp,p0,OWN)
                assert certificate is not None,("saved root",case_index,cursor)
                rows,detail=check_source(box,pp,p0,dp,certificate,types,targets)
                assert rows is not None,("saved source",case_index,cursor,detail)
            else:
                proposed=propose(pp,p0)
                rows=None
                if proposed is None:
                    reason="root";detail=dict(reason="root")
                else:
                    w,certificate=proposed
                    try:
                        rows,detail=check_source(box,pp,p0,dp,certificate,types)
                    except (AssertionError,ValueError,ZeroDivisionError) as exc:
                        detail=dict(reason="nonfinite interval or uncertain division",
                                    exception=type(exc).__name__)
                    reason="source"
                if rows is None:
                    if depth>=args.max_depth or detail["reason"]=="point exceeds requested gap":
                        active=dict(case=[ta,tb,face],tree=tree,leaves=local_leaves,
                                    failing_box=[[str(v) for v in p] for p in box],
                                    failing_depth=depth,detail=detail,
                                    witness=w if proposed else None,
                                    pending=[[[[str(v) for v in p] for p in pending],dd]
                                             for pending,dd in todo])
                        path=snapshot("incomplete",active,detail["reason"])
                        print("INCOMPLETE",case_index,visits,leaves,detail,path,flush=True)
                        return 2
                    failure_counts[reason]+=1
                    axis=depth%3;lo,hi=box[axis];mid=(lo+hi)/2
                    left,right=list(box),list(box)
                    left[axis]=(lo,mid);right[axis]=(mid,hi)
                    todo.extend([(left,depth+1),(right,depth+1)])
                    tree.append(["S",axis])
                    continue
                node=["L",dict(witness=w,targets=[row["trial"] for row in rows])]
            tree.append(node)
            leaves+=1;local_leaves+=1;max_depth=max(max_depth,depth)
            for row in rows:
                val=arb(row["upper_bound"])
                maximum=val.upper() if maximum is None else max(maximum,val.upper())
            now=time.monotonic()
            if now-last_log>=10:
                print("progress",case_index,visits,leaves,len(todo),
                      round(now-start,2),"seconds",flush=True)
                last_log=now
        if old_domain:
            assert cursor==len(old_domain["tree"]) and local_leaves==old_domain["leaves"]
            assert tree==old_domain["tree"]
        assert len(tree)==2*local_leaves-1
        domains.append(dict(case=[ta,tb,face],leaves=local_leaves,tree=tree,
                            maximum_upper=str(maximum),maximum_depth=max_depth))
        print("PASS face",ta,tb,face,local_leaves,str(maximum),
              round(time.monotonic()-start,2),"seconds",flush=True)
    assert len(domains)==len(specs) and visits==2*leaves-len(specs)
    path=snapshot("pilot_complete" if args.pilot else "passed")
    print("PILOT" if args.pilot else "PASS",len(specs),leaves,visits,len(deps),round(time.monotonic()-start,2),
          "seconds",path,flush=True)
    return 0

if __name__=="__main__":
    raise SystemExit(main())

