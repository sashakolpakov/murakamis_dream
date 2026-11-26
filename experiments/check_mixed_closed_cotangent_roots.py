#!/usr/bin/env python3
"""Exact closed-cotangent boundary and triangle identities."""
import argparse
import hashlib
import json
from pathlib import Path

import sympy as sp

ROOT=Path(__file__).resolve().parents[1]
PROOF=ROOT/'notes/research_mixed_closed_cotangent_roots.md'


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=ROOT/'repro/results/research-mixed-closed-cotangent-roots.json')
    args=parser.parse_args()
    ph,sh=sha(PROOF),sha(__file__)
    deps={}
    for stem in ('mixed_global_cotangent_roots','mixed_real_outer_support'):
        pp=f'notes/research_{stem}.md';ss=f'experiments/check_{stem}.py';rr=f'repro/results/research-{stem.replace("_","-")}.json'
        for path in(pp,ss,rr):deps[path]=sha(ROOT/path)
        rec=json.loads((ROOT/rr).read_text())
        assert rec['status']=='passed'
        assert rec['proof_sha256']==deps[pp] and rec['script_sha256']==deps[ss]
        for key in ('dependencies','dependencies_sha256'):
            assert all(sha(ROOT/p)==h for p,h in rec.get(key,{}).items())
    p,q,u,v,aa,bb=sp.symbols('p q u v aa bb',real=True)
    I=sp.I;P=p+I*aa;Q=q+I*bb;S=u+I*v
    exact=[]
    def zero(name,value):
        assert sp.cancel(sp.expand(value))==0,name
        exact.append(name)
    f0=lambda z:z*z+(P+Q)*z-1+I*(Q-P)
    f1=lambda z:(z+I)*(z+P)*(z+Q)-2*I*(P-I)*(Q+I)
    zero('quadratic upper boundary',sp.im(sp.expand(f0(u+I)))-u*(2+aa+bb)-2*q)
    zero('quadratic lower boundary',sp.im(sp.expand(f0(u-I)))-u*(-2+aa+bb)+2*p)
    zero('quadratic left boundary',sp.re(sp.expand(f0(I*v)))+1+v*v-aa*(1-v)+bb*(1+v))
    zero('cubic left boundary',sp.im(sp.expand(f1(I*v)))-((v-1)*p*q+2*(aa-1)*(bb+1)-(v+1)*(aa+v)*(bb+v)))
    top=u+I
    den=(top+I)*(top+Q)-2*I*(Q+I)
    num=2*(Q+I)-top*(top+I)*(top+Q)
    zero('upper denominator nonzero on closed quadrant',den-u*(u+Q+3*I))
    forced=-1-2*(4*q+u*q*(u+q)+u*(bb+1)**2)/(u*((u+q)**2+(bb+3)**2))
    zero('upper forced imaginary cotangent',sp.im(sp.expand_complex(num/den))-forced)
    first=(P+u-I)/(P-I)
    zero('lower first factor real part',sp.re(first)-1-u*p/(p*p+(aa-1)**2))
    zero('lower first factor positive imaginary part',sp.im(first)-u*(1-aa)/(p*p+(aa-1)**2))
    ratio=(P+I)/(P-I)
    zero('outer inverse quotient imaginary part',sp.im(ratio)-2*p/(p*p+(aa-1)**2))
    zero('outer inverse quotient on closed face',ratio.subs(p,0)-(aa+1)/(aa-1))
    C=sp.re(sp.expand_complex((P*S-1)/(S+P)))
    denT=(u+p)**2+(v+aa)**2
    det=u*p-(u+p)*C
    zero('general triangle determinant',det-((u+p)**2-(p*v-u*aa)**2)/denT)
    Cface=u*(aa*aa-1)/(u*u+(v+aa)**2)
    zero('closed-face pair cotangent',C.subs(p,0)-Cface)
    zero('closed-face triangle determinant',det.subs(p,0)-u*u*(1-aa*aa)/(u*u+(v+aa)**2))
    assert ph==sha(PROOF) and sh==sha(__file__)
    assert all(sha(ROOT/p)==h for p,h in deps.items())
    result={'status':'passed','arithmetic':'exact symbolic rational identities',
            'exact_identity_count':len(exact),'exact_identities':exact,
            'proof_sha256':ph,'script_sha256':sh,'dependencies_sha256':deps,
            'scope':'Unique simple original zero-lift roots and positive ambient Schur curvature on closed outer cotangent quadrant. No finite-source extension or varying-height graph concavity.'}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS',len(exact),'exact identities; inherited input records current')


if __name__=='__main__':
    main()
