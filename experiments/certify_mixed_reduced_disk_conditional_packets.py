#!/usr/bin/env python3
"""Whole conditional source on six reduced-disk products, both orientations.

Rational affine original-log root witnesses and complete binary trees are
saved. Replay makes no proposals and refines no failed cells. The old global
block theorem supplies existence and uniqueness throughout the products.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import time

import numpy as np
from flint import acb, arb, ctx
import certify_mixed_cyclic_block_localization as base

ROOT=Path(__file__).resolve().parents[1]
PROOF=ROOT/"notes/research_mixed_reduced_disk_conditional_packets.md"
CENTERS=[(F(7,20),-F(1,100)),(F(3,10),-F(13,250))]
RADII=[F(83,1000),F(3,50)]
ar=base.ar


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def cp(v):
    return acb(ar(v[0]),ar(v[1]))


def encode(z):
    return [format(z.real,".17g"),format(z.imag,".17g")]


def parameter(box,types):
    return [acb(ar(CENTERS[t][0]),ar(CENTERS[t][1]))
            +ar(RADII[t])*(2*PI*II*ar(lo).union(ar(hi))).exp()
            for (lo,hi),t in zip(box,types)]


def split(box,axis):
    lo,hi=box[axis];mid=(lo+hi)/2
    left,right=list(box),list(box)
    left[axis]=(lo,mid);right[axis]=(mid,hi)
    return left,right


def mm(left,right):
    return [[sum((left[i][k]*right[k][j] for k in range(2)),acb(0))
             for j in range(2)] for i in range(2)]


def mv(left,right):
    return [sum((left[i][k]*right[k] for k in range(2)),acb(0))
            for i in range(2)]


def gp(z):
    return (1-(-2*PI*II*z).exp()).log()


def g(z):
    return ((-2*PI*II*z).exp().polylog(2)-PI*PI/6)/(2*PI*II)


def phase(s,a,t,eps):
    return g(s+a)+g(s+t)-(2+eps)*g(s)+2*PI*II*a*s


def components(w,pp,p0,eps):
    zz=list(map(cp,w["centers"]))
    Y=[[cp(v) for v in row] for row in w["inverse"]]
    D=[[cp(v) for v in row] for row in w["affine"]]
    assert abs(Y[0][0]*Y[1][1]-Y[0][1]*Y[1][0])>0
    f0,J0=base.evalf(zz,*p0,2+eps)
    dp=[pp[i]-p0[i] for i in range(2)]
    dz=mv(D,dp)
    E0=[2*PI*II/(1-(-2*PI*II*(zz[i]+p0[i])).exp()) for i in range(2)]
    JD=mm(J0,D)
    linear=[f0[i]+sum(((JD[i][j]+(E0[i] if i==j else 0))*dp[j]
                      for j in range(2)),acb(0)) for i in range(2)]

    def rem(center,delta):
        domain=center+acb(arb(0,abs(delta.real).upper()),
                          arb(0,abs(delta.imag).upper()))
        if not 0<domain.real<1:
            return arb.pos_inf()
        q=(-2*PI*II*domain).exp()
        return (2*PI)**2*abs(q/(1-q)**2)*abs(delta)**2/2

    shared=rem(zz[0]+zz[1],dz[0]+dz[1])
    remainder=[shared+rem(zz[i]+p0[i],dz[i]+dp[i])
               +(2+eps)*rem(zz[i],dz[i]) for i in range(2)]
    bb=[abs(mv(Y,linear)[i])+sum((abs(Y[i][k])*remainder[k]
                                  for k in range(2)),arb(0)) for i in range(2)]
    return zz,Y,D,dp,dz,f0,J0,bb


def propose(box,eps,types):
    pp=parameter(box,types)
    p0=parameter([(sum(x,F(0))/2,)*2 for x in box],types)
    floats=[complex(float(z.real.mid()),float(z.imag.mid())) for z in p0]
    roots,D,error=base.block([floats[0].real,floats[0].imag,
                              floats[1].real,floats[1].imag],eps)
    if error>1e-9:
        return None
    centers=[encode(z) for z in roots]
    _,J0=base.evalf(list(map(cp,centers)),*p0,2+eps)
    floating_J=np.array([[complex(float(z.real.mid()),float(z.imag.mid()))
                          for z in row] for row in J0])
    Y=np.linalg.inv(floating_J)
    w=dict(centers=centers,inverse=[[encode(v) for v in row] for row in Y],
           affine=[[encode(v) for v in row] for row in D])
    *_,bb=components(w,pp,p0,eps)
    if any(not b.is_finite() for b in bb):
        return None
    for factor in (F(5,4),F(3,2),F(2)):
        # Floating operations propose positive rational radii only.
        w["radii"]=[str(F(max(1,int(np.ceil(float(b.upper())*float(factor)*2**40))),
                          2**40)) for b in bb]
        if root_box(w,pp,p0,eps) is not None:
            return dict(w)
    return None


def root_box(w,pp,p0,eps):
    if not (len(w["centers"])==2 and len(w["inverse"])==2
            and len(w["affine"])==2 and len(w["radii"])==2):
        return None
    if not all(len(row)==2 for row in w["inverse"]+w["affine"]):
        return None
    zz,Y,D,dp,dz,f0,J0,bb=components(w,pp,p0,eps)
    radii=list(map(ar,w["radii"]))
    if not all(r>0 for r in radii):
        return None
    ddz=[dz[i]+acb(arb(0,radii[i]),arb(0,radii[i])) for i in range(2)]
    z=[zz[i]+ddz[i] for i in range(2)]
    if not all(ar("23/100")<v.real<ar("9/20") and abs(v.imag)<ar("3/25")
               for v in z+pp):
        return None
    center=acb(ar(base.cs[eps][0]),ar(base.cs[eps][1]))
    if not all(abs(zz[i]+dz[i]-center)+radii[i]<ar(base.rs[eps])
               for i in range(2)):
        return None

    def qdiff(center,delta):
        q0=(-2*PI*II*center).exp()
        dq=q0*((-2*PI*II*delta).exp()-1)
        return dq/((1-q0-dq)*(1-q0))

    dc=qdiff(zz[0]+zz[1],ddz[0]+ddz[1])
    ds=[qdiff(zz[i]+p0[i],ddz[i]+dp[i])
        -(2+eps)*qdiff(zz[i],ddz[i]) for i in range(2)]
    E=[[acb(int(i==j))-sum((Y[i][k]*J0[k][j] for k in range(2)),acb(0))
        -2*PI*II*((Y[i][0]+Y[i][1])*dc+Y[i][j]*ds[j])
        for j in range(2)] for i in range(2)]
    if not all(bb[i]+sum((abs(E[i][j])*radii[j] for j in range(2)),arb(0))
               <radii[i] for i in range(2)):
        return None
    # Verify the original midpoint lift with a tiny disk, using the same
    # rational centers/inverse; no independent nonlinear solve occurs.
    point_radius=ar("1/10000000000")
    point=[v+acb(arb(0,point_radius),arb(0,point_radius)) for v in zz]
    _,Jpoint=base.evalf(point,*p0,2+eps)
    EY=mm(Y,Jpoint)
    residual=mv(Y,f0)
    if not all(abs(residual[i])+point_radius*sum(
        (abs(acb(int(i==j))-EY[i][j]) for j in range(2)),arb(0))
               <point_radius for i in range(2)):
        return None
    # Weighted infinity norm, matching the two different remainder radii.
    rho=max((sum((abs(E[i][j])*radii[j]/radii[i] for j in range(2)),arb(0)))
            .upper() for i in range(2))
    assert 0<=rho<1
    forcing=[2*PI*II/(1-(-2*PI*II*(z[i]+pp[i])).exp()) for i in range(2)]
    first=[[-Y[i][j]*forcing[j] for j in range(2)] for i in range(2)]
    term=[row[:] for row in first]
    response=[row[:] for row in first]
    for _ in range(4):
        term=mm(E,term)
        response=[[response[i][j]+term[i][j] for j in range(2)] for i in range(2)]
    for j in range(2):
        norm=max((abs(first[i][j])/radii[i]).upper() for i in range(2))
        for i in range(2):
            tail=radii[i]*norm*rho**5/(1-rho)
            response[i][j]+=acb(arb(0,tail.upper()),arb(0,tail.upper()))
    return dict(root=z,point=point,response=response)


def source(box,eps,types,w):
    pp=parameter(box,types)
    p0=parameter([(sum(x,F(0))/2,)*2 for x in box],types)
    certified=root_box(w,pp,p0,eps)
    if certified is None:
        return None,"root"
    roots,points,R=(certified[k] for k in ("root","point","response"))
    angles=[ar((hi-lo)/2) for lo,hi in box]
    tangent=[2*PI*II*(pp[i]-acb(ar(CENTERS[t][0]),ar(CENTERS[t][1])))
             for i,t in enumerate(types)]
    all_values=[]
    for side in (0,1):
        a,t,s=pp[side],roots[1-side],roots[side]
        a0,t0,s0=p0[side],points[1-side],points[side]
        selected=phase(s0,a0,t0,eps)
        ga=gp(s+a)+2*PI*II*s
        gt=gp(s+t)

        def lower(value,da,dt):
            deriv=[dt*R[1-side][j]+(da if j==side else 0) for j in range(2)]
            return value.real-sum((abs((deriv[j]*tangent[j]).real)*angles[j]
                                  for j in range(2)),arb(0))

        values=[]
        for cut in ("3/20","49/100"):
            c=acb(ar(cut))
            val=lower(selected-phase(c,a0,t0,eps),
                      ga-gp(c+a)-2*PI*II*c,gt-gp(c+t))
            if not val>ar("1/1000"):return None,("cut",side,cut,str(val))
            values.append(val.lower())
        for v in (0,1):
            for wbit in (0,1):
                val=lower(selected-g(a0)-g(t0)-2*PI*II*v*a0+2*PI*II*wbit*t0,
                          ga-gp(a)-2*PI*II*v,gt-gp(t)+2*PI*II*wbit)
                if not val>ar("1/1000"):return None,("last",side,v,wbit,str(val))
                values.append(val.lower())
        for sign in (-1,1):
            alias=[]
            for j in range(8):
                x=ar(F(3,20)+F(34,100)*F(j,8)).union(
                    ar(F(3,20)+F(34,100)*F(j+1,8)))
                c=acb(x,sign*ar("1/5"))
                val=lower(selected-phase(c,a0,t0,eps),
                          ga-gp(c+a)-2*PI*II*c,gt-gp(c+t))+2*PI/5
                if not val>ar("1/10"):return None,("alias",side,sign,j,str(val))
                alias.append(val.lower())
            values.append(min(alias))
        qa=(2*PI*a.real).sin()/((2*PI*a.imag).cosh()-(2*PI*a.real).cos())
        qt=(2*PI*t.real).sin()/((2*PI*t.imag).cosh()-(2*PI*t.real).cos())
        if not qa>0 or not qt>0:return None,"tail vertices"
        wl,wr=-1/(49*PI/100).tan(),max(qa.upper(),qt.upper())
        ca,sa,ct,st=(PI*a).cos(),(PI*a).sin(),(PI*t).cos(),(PI*t).sin()
        factor=(2*PI*(t.imag-a.imag)).exp()/4**eps
        shape=[]
        for j in range(12):
            omega=(wl+(wr-wl)*j/12).union(wl+(wr-wl)*(j+1)/12)
            val=factor*abs(ca-omega*sa)**2*abs(ct-omega*st)**2*(1+omega**2)**eps
            if not val<1:return None,("shape",side,j,str(val))
            shape.append(val.upper())
        values.append(max(shape))
        all_values.append(values)
    return all_values,None


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision",type=int,default=256)
    parser.add_argument("--input",type=Path)
    parser.add_argument("--output",type=Path,default=ROOT /
                        "repro/results/research-mixed-reduced-disk-conditional-packets.json")
    parser.add_argument("--max-seconds",type=float,default=600)
    parser.add_argument("--max-visits",type=int,default=40000)
    args=parser.parse_args()
    assert args.precision>=192
    ctx.prec=args.precision
    global PI,II
    PI,II=arb.pi(),acb(0,1)
    base.PI,base.I=PI,II
    ph,sh=sha(PROOF),sha(__file__)
    ih=sha(args.input) if args.input else None
    old=json.loads(args.input.read_text()) if args.input else None
    deps={}

    def bind(path,expected=None):
        digest=sha(ROOT/path)
        if expected is not None:assert digest==expected,path
        assert path not in deps or deps[path]==digest,path
        deps[path]=digest
        return digest

    def read(path):
        bind(path)
        r=json.loads((ROOT/path).read_text())
        assert r["status"]=="passed",path
        for field in ("dependencies","dependencies_sha256"):
            for p,h in r.get(field,{}).items():bind(p,h)
        return r

    authorpath="repro/results/research-mixed-cyclic-block-localization.json"
    replaypath="repro/results/research-mixed-cyclic-block-localization-replay.json"
    author,replay=read(authorpath),read(replaypath)
    assert replay["input_sha256"]==deps[authorpath]
    bind("notes/research_mixed_cyclic_critical_localization.md",author["proof_sha256"])
    bind("experiments/certify_mixed_cyclic_block_localization.py",author["script_sha256"])
    bind("experiments/replay_mixed_cyclic_block_localization.py",replay["script_sha256"])
    contour=read("repro/results/research-mixed-conditional-image-contours.json")
    bind("notes/research_mixed_conditional_image_contours.md",contour["proof_sha256"])
    bind("experiments/check_mixed_conditional_image_contours.py",contour["script_sha256"])
    for stem in ("mixed_conditional_critical_images","mixed_three_canonical_conditional",
                 "mixed_four_conditional_complex_neighbors","mixed_conditional_torus_composition"):
        bind(f"notes/research_{stem}.md")
    if old:
        assert old["status"]=="passed" and old["proof_sha256"]==ph and old["script_sha256"]==sh
        assert old["dependencies_sha256"]==deps
    specs=[(eps,a,b) for eps in (0,1) for a,b in ((0,0),(0,1),(1,1))]
    if old:assert [tuple(d["types"]) for d in old["domains"]]==specs
    start=time.monotonic()
    visits=leaves=0
    domains=[]
    for index,(eps,ta,tb) in enumerate(specs):
        todo=[([(F(0),F(1)),(F(0),F(1))],0)]
        tree=[]
        local_leaves=cursor=0
        extrema=[[None]*9 for _ in range(2)]
        while todo:
            assert visits<args.max_visits,"explicit visit budget"
            assert time.monotonic()-start<args.max_seconds,"explicit runtime budget"
            box,depth=todo.pop()
            visits+=1
            if old:
                node=old["domains"][index]["tree"][cursor];cursor+=1
                if node[0]=="S":
                    assert len(node)==2 and node[1]==depth%2
                    left,right=split(box,node[1])
                    todo.extend([(left,depth+1),(right,depth+1)])
                    tree.append(node)
                    continue
                assert node[0]=="L" and len(node)==2
                w=node[1]
                values,reason=source(box,eps,(ta,tb),w)
                assert values is not None,(index,cursor,reason)
            else:
                w=propose(box,eps,(ta,tb))
                values,reason=(source(box,eps,(ta,tb),w) if w else (None,"proposal"))
                if values is None:
                    assert depth<30,(index,reason)
                    axis=depth%2
                    left,right=split(box,axis)
                    todo.extend([(left,depth+1),(right,depth+1)])
                    tree.append(["S",axis])
                    if visits%1000==0:
                        print("progress",index,visits,leaves,len(todo),
                              round(time.monotonic()-start,1),reason,flush=True)
                    continue
                node=["L",w]
            tree.append(node)
            leaves+=1;local_leaves+=1
            for side,row in enumerate(values):
                for j,val in enumerate(row):
                    prior=extrema[side][j]
                    extrema[side][j]=(val if prior is None else
                                     max(prior,val) if j==8 else min(prior,val))
            if visits%1000==0:
                print("progress",index,visits,leaves,len(todo),
                      round(time.monotonic()-start,1),flush=True)
        if old:
            assert cursor==len(old["domains"][index]["tree"])
            assert local_leaves==old["domains"][index]["leaves"]
        domains.append(dict(types=[eps,ta,tb],leaves=local_leaves,tree=tree,
                            extrema=[[str(v) for v in row] for row in extrema]))
        print("PASS reduced disk",eps,ta,tb,local_leaves,
              round(time.monotonic()-start,2),"seconds",flush=True)
    assert len(domains)==6 and visits==2*leaves-6
    assert sha(PROOF)==ph and sha(__file__)==sh
    assert all(sha(ROOT/p)==h for p,h in deps.items())
    if args.input:assert sha(args.input)==ih
    result=dict(status="passed",precision_bits=args.precision,
        domains=domains,domain_count=6,orientations_per_domain=2,
        accepted_cells=leaves,visited_nodes=visits,
        parameter_disks=[["7/20","-1/100","83/1000"],["3/10","-13/250","3/50"]],
        real_cut_and_last_row_gap="1/1000",horizontal_alias_gap="1/10",
        right_tail_shape_upper="1",middle_rectangle=["3/20","49/100","-1/5","1/5"],
        alias_intervals_per_side=8,tail_shape_intervals=12,
        point_radius="1/10000000000",response_terms=5,response_tail_power=5,
        proof_sha256=ph,script_sha256=sh,dependencies_sha256=deps,input_sha256=ih,
        elapsed_seconds=time.monotonic()-start,
        scope="Complete conditional source on the six reduced universal disk products "
              "in both orientations; no individual word or full outer contour tested.")
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+"\n")
    print("PASS",6,leaves,visits,len(deps),round(time.monotonic()-start,2),flush=True)


if __name__=="__main__":
    main()
