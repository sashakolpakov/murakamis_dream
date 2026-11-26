#!/usr/bin/env python3
"""Exact real-parameter conditional height and left-contour identities."""
import argparse
import hashlib
import json
from pathlib import Path
import sympy as sp

ROOT=Path(__file__).resolve().parents[1]
PROOF=ROOT/'notes/research_mixed_real_conditional_contour_geometry.md'

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--precision',type=int,default=256)
    parser.add_argument('--output',type=Path,default=ROOT/'repro/results/research-mixed-real-conditional-contour-geometry.json')
    args=parser.parse_args()
    assert args.precision>=128
    initial_script,initial_proof=sha(__file__),sha(PROOF)
    paths=['notes/research_mixed_global_cotangent_roots.md',
           'experiments/check_mixed_global_cotangent_roots.py',
           'repro/results/research-mixed-global-cotangent-roots.json',
           'notes/research_mixed_plateau_accretivity.md']
    deps={p:sha(ROOT/p) for p in paths}
    inherited=json.loads((ROOT/paths[2]).read_text())
    assert inherited['status']=='passed'
    assert inherited['proof_sha256']==deps[paths[0]]
    assert inherited['script_sha256']==deps[paths[1]]
    assert all(sha(ROOT/p)==h for p,h in inherited['dependencies'].items())
    exact=[]
    def zero(name,value):
        assert sp.cancel(sp.expand(value))==0,name
        exact.append(name)
    u,v,p,q,t,w=sp.symbols('u v p q t w',real=True)
    I=sp.I;S=u+I*v
    F=(S+I)*(S+p)*(S+q)-2*I*(p-I)*(q+I)
    circle=-v*v-6*v-1
    imag=(3*v+1)*u*u-v*v*(v+1)-2+u*(p+q)*(2*v+1)+p*q*(v-1)
    zero('original cubic imaginary part',sp.im(sp.expand(F))-imag)
    C=-4*v**3-20*v*v-9*v-3
    zero('circle imaginary reduction',imag.subs(u*u,circle)-(C+u*(p+q)*(2*v+1)+p*q*(v-1)))
    zero('lower semicircle sign polynomial',C.subs(v,-sp.Rational(1,2)-t)-(4*t**3-14*t*t-8*t-3))
    D=(S+I)*(S+p)-2*I*(p-I)
    Z=-S*(S+I)*(S+p)-2*(p-I)
    zero('cubic linear equation for second real parameter',F-(D*q-Z))
    A=v*(v+2);B=u*(2*v+1)*(v+1);C2=-(2*v+1)*(2*v*v+2*v+1)
    lhs=sp.rem(sp.Poly(sp.expand(sp.im(Z*sp.conjugate(D))/8),u),sp.Poly(u*u-circle,u)).as_expr()
    zero('circle imaginary numerator quadratic',lhs-(A*p*p+B*p+C2))
    T=2*v**5+9*v**4+12*v**3+10*v*v+2*v+1
    disc=sp.expand(B*B-4*A*C2).subs(u*u,circle)
    zero('negative discriminant factorization',disc+(2*v+1)*T)
    shifted=2*w**5+4*w**4+(3*w*w-w**3)+(sp.Rational(3,2)-23*w/8)
    zero('positive discriminant polynomial after shift',T.subs(v,w-sp.Rational(1,2))-shifted)
    zero('height circle identity',2*(u*u+(v+1)**2)-(u*u+(v-1)**2)-(u*u+v*v+6*v+1))
    x,a,b,y,eps=sp.symbols('x a b y eps',real=True)
    trig=sp.sin(x+a)**2-sp.sin(x)**2-sp.sin(a)*sp.sin(2*x+a)
    assert sp.trigsimp(sp.expand_trig(trig))==0
    exact.append('low-arc sine difference')
    R,c=sp.symbols('R c',real=True)
    norm=1+R*R-2*R*c
    zero('negative-height low-arc denominator',norm.subs(c,R)-(1-R*R))
    zero('positive-height low-arc denominator',norm.subs(c,1/R)-(R*R-1))
    phi=lambda z:sp.pi*(z-z*z)/2
    chirp=phi(S+a)+phi(S+b)-(2+eps)*phi(S)+2*sp.pi*a*S
    target=phi(a)+phi(b)+sp.pi*S*(a-b)+eps*sp.pi*(S*S-S)/2
    zero('original sine-log chirp',chirp-target)
    chirp_s=lambda z:phi(a)+phi(b)+sp.pi*z*(a-b)+eps*sp.pi*(z*z-z)/2
    reflection=sp.re(I*chirp_s(x-I*y))-sp.re(I*chirp_s(x+I*y))
    zero('exact two-height reflection',reflection-2*sp.pi*y*(a-b+eps*(x-sp.Rational(1,2))))
    zero('left upper derivative reserve',(2+eps)*sp.pi-2*sp.pi*a-(sp.pi-2*sp.pi*a)-(sp.pi-2*sp.pi*b)-(eps*sp.pi+2*sp.pi*b))
    rational=[
        ('discriminant remainder on w in [0,1/2]',sp.Rational(3,2)-sp.Rational(23,8)*sp.Rational(1,2)),
        ('3-w positive on [0,1/2]',3-sp.Rational(1,2)),
        ('14-4t positive on [0,1/2]',14-4*sp.Rational(1,2)),
        ('base Rouche imaginary lower bound',sp.Rational(1,3)-sp.Rational(1,20)),
    ]
    assert all(value>0 for _,value in rational)
    assert initial_script==sha(__file__) and initial_proof==sha(PROOF)
    assert all(sha(ROOT/p)==h for p,h in deps.items())
    result={'status':'passed','precision_bits':args.precision,
            'exact_identity_count':len(exact),'exact_identities':exact,
            'rational_sign_margins':[{'name':n,'margin':str(vv)}for n,vv in rational],
            'proof_sha256':initial_proof,'script_sha256':initial_script,
            'dependencies_sha256':deps,
            'scope':'Exact real-outer type-four height exclusion, left-half horizontal maximum, left endpoint and alias phase geometry. No complete conditional sum or high-half source theorem.'}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS',len(exact),'exact identities,',len(rational),'rational sign margins')

if __name__=='__main__':
    main()
