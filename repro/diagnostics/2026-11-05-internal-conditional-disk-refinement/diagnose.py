#!/usr/bin/env python3
"""Four fixed contractions of the known old tail obstruction; diagnostic only."""
import hashlib
import json
from pathlib import Path
import numpy as np
from scipy.optimize import root
from flint import acb, arb, ctx

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
ctx.prec=192
PI,II=arb.pi(),acb(0,1)


def g(z):
    return ((-2*PI*II*z).exp().polylog(2)-PI*PI/6)/(2*PI*II)


def cv(z):
    return acb(str(z.real),str(z.imag))


def pair(z):
    return [float(z.real),float(z.imag)]


def solve(a,b):
    def jp(z):return np.log(2*np.sin(np.pi*z))
    def fun(v):
        s,t=v[:2]+1j*v[2:]
        out=np.array([jp(s+t)+jp(s+a)-2*jp(s)+1j*np.pi*(a-t),
                      jp(s+t)+jp(t+b)-2*jp(t)+1j*np.pi*(b-s)])
        return np.r_[out.real,out.imag]
    rr=root(fun,[.405812323751165,.337758049539820,
                 .020538477635504,.017916246413660],tol=1e-11)
    residual=float(np.max(np.abs(fun(rr.x))))
    assert residual<1e-9
    return rr.x[:2]+1j*rr.x[2:],residual


def main():
    a=complex(.3131,-.1146);b=complex(.4028,-.0828)
    c4,c3=complex(.30,-.052),complex(.35,-.01)
    anew=c4+.060*(a-c4)/abs(a-c4)
    bnew=c3+.083*(b-c3)/abs(b-c3)
    rows=[]
    for name,aa,bb in (("old rational point",a,b),
                       ("left radius .060 only",anew,b),
                       ("right radius .083 only",a,bnew),
                       ("both improved disks",anew,bnew)):
        (s,t),residual=solve(aa,bb)
        z,alpha,beta=cv(s),cv(aa),cv(t)
        selected=g(z+alpha)+g(z+beta)-2*g(z)+2*PI*II*alpha*z
        last=(g(alpha)+g(beta)).real+2*PI*(
            max(-alpha.imag,arb(0))+max(beta.imag,arb(0)))
        excess=float((last-selected.real).mid())
        row=dict(name=name,external_a=pair(aa),external_b=pair(bb),
                 root_s=pair(s),root_t=pair(t),residual=residual,
                 last_row_minus_selected=excess)
        rows.append(row);print(row,flush=True)
    paths=["notes/research_mixed_conditional_image_contours.md",
           "notes/research_mixed_cyclic_critical_height_bounds.md",
           "notes/research_mixed_open_word_endpoint_rectangles.md"]
    out=dict(status="diagnostic_only",rows=rows,
             scope="Four fixed type3/ext4,3 points derived only from the old certified "
                   "obstruction. No optimization, circle scan, source theorem, or "
                   "interval verification of the new roots.",
             dependencies_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
                                    for p in paths},
             script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    (HERE/"result.json").write_text(json.dumps(out,indent=2)+"\n")


if __name__=="__main__":main()
