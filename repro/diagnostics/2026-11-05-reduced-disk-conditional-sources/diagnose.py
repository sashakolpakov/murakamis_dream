#!/usr/bin/env python3
"""Fixed 12x12 reduced-circle pilot, both orientations; not a certificate."""
import hashlib
import json
from pathlib import Path
import numpy as np
from scipy.optimize import root
from flint import acb, arb, ctx

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
ctx.prec=128
PI,II=arb.pi(),acb(0,1)
DISKS=[(complex(.35,-.01),.083),(complex(.30,-.052),.060)]


def g(z):
    return ((-2*PI*II*z).exp().polylog(2)-PI*PI/6)/(2*PI*II)


def cv(z):
    return acb(str(z.real),str(z.imag))


def pair(z):
    return [float(z.real),float(z.imag)]


def phase(s,a,b,eps):
    return g(s+a)+g(s+b)-(2+eps)*g(s)+2*PI*II*a*s


def solve(a,b,eps):
    def jp(z):return np.log(2*np.sin(np.pi*z))
    def fun(v):
        s,t=v[:2]+1j*v[2:]
        out=np.array([jp(s+t)+jp(s+a)-(2+eps)*jp(s)
                      +1j*np.pi*(a-t+eps*(s-.5)),
                      jp(s+t)+jp(t+b)-(2+eps)*jp(t)
                      +1j*np.pi*(b-s+eps*(t-.5))])
        return np.r_[out.real,out.imag]
    center=DISKS[eps][0]
    rr=root(fun,[center.real,center.real,center.imag,center.imag],tol=1e-11)
    residual=float(np.max(np.abs(fun(rr.x))))
    assert residual<1e-9
    return rr.x[:2]+1j*rr.x[2:],residual


def evaluate(a,b,s,eps):
    M=phase(s,a,b,eps).real
    last=(g(a)+g(b)).real+2*PI*(max(-a.imag,arb(0))+max(b.imag,arb(0)))
    cuts=[float((M-phase(acb(str(c)),a,b,eps).real).mid()) for c in (.15,.49)]
    aliases=[]
    for sign in (-1,1):
        aliases.append(min(float((M-phase(acb(arb(3)/20+arb(34)*j/800,
                                             sign*arb(1)/5),a,b,eps).real+2*PI/5).mid())
                           for j in range(9)))
    qa=(2*PI*a.real).sin()/((2*PI*a.imag).cosh()-(2*PI*a.real).cos())
    qb=(2*PI*b.real).sin()/((2*PI*b.imag).cosh()-(2*PI*b.real).cos())
    wl,wr=-1/(49*PI/100).tan(),max(qa,qb)
    ca,sa,cb,sb=(PI*a).cos(),(PI*a).sin(),(PI*b).cos(),(PI*b).sin()
    shape=max(float(((2*PI*(b.imag-a.imag)).exp()/4**eps
                     *abs(ca-(wl+(wr-wl)*j/12)*sa)**2
                     *abs(cb-(wl+(wr-wl)*j/12)*sb)**2
                     *(1+(wl+(wr-wl)*j/12)**2)**eps).mid()) for j in range(13))
    return dict(left_cut_gap=cuts[0],right_cut_gap=cuts[1],
                last_row_gap=float((M-last).mid()),
                lower_alias_grid_gap=aliases[0],upper_alias_grid_gap=aliases[1],
                tail_shape_grid_upper=shape)


def main():
    cases=[]
    for eps in (0,1):
        for ta,tb in ((0,0),(0,1),(1,1)):
            rows=[]
            for i in range(12):
                a=DISKS[ta][0]+DISKS[ta][1]*np.exp(2j*np.pi*i/12)
                for j in range(12):
                    b=DISKS[tb][0]+DISKS[tb][1]*np.exp(2j*np.pi*j/12)
                    (s,t),residual=solve(a,b,eps)
                    orient=[evaluate(cv(a),cv(t),cv(s),eps),
                            evaluate(cv(b),cv(s),cv(t),eps)]
                    rows.append(dict(angles=[i,j],external=[pair(a),pair(b)],
                                     roots=[pair(s),pair(t)],residual=residual,
                                     orientations=orient))
            keys=rows[0]["orientations"][0].keys()
            extrema={key:(max if key.endswith("upper") else min)(
                oo[key] for row in rows for oo in row["orientations"]) for key in keys}
            case=dict(own_epsilon=eps,external_types=[ta,tb],rows=rows,extrema=extrema)
            cases.append(case)
            print(eps,ta,tb,extrema,flush=True)
    paths=["notes/research_mixed_conditional_image_contours.md",
           "notes/research_mixed_cyclic_critical_localization.md",
           "notes/research_mixed_cyclic_critical_height_bounds.md",
           "notes/research_mixed_conditional_critical_images.md"]
    out=dict(status="diagnostic_only",cases=cases,root_proposals=864,
             source_orientations=1728,angle_grid=12,
             scope="Six fixed reduced-circle products, both orientations. No optimization, "
                   "interval root validation, continuous source cover, or packet theorem.",
             dependencies_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
                                    for p in paths},
             script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    (HERE/"result.json").write_text(json.dumps(out,indent=2)+"\n")


if __name__=="__main__":main()
