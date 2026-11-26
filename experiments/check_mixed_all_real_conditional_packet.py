#!/usr/bin/env python3
"""Exact upper-half calibration and all-real conditional source normalization."""
import argparse
import hashlib
import json
from pathlib import Path
import sympy as sp

ROOT=Path(__file__).resolve().parents[1]
PROOF=ROOT/'notes/research_mixed_all_real_conditional_packet.md'
def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=ROOT/'repro/results/research-mixed-all-real-conditional-packet.json')
    args=parser.parse_args()
    proof_hash,script_hash=sha(PROOF),sha(__file__)
    stems=['mixed_global_cotangent_roots','mixed_real_conditional_contour_geometry',
           'mixed_negative_height_full_period','lower_half_factorial_continuation',
           'mixed_global_lower_conditional_packet']
    deps={}
    for stem in stems:
        pp=f'notes/research_{stem}.md';ss=f'experiments/check_{stem}.py'
        rr=f'repro/results/research-{stem.replace("_","-")}.json'
        for p in(pp,ss,rr):deps[p]=sha(ROOT/p)
        rec=json.loads((ROOT/rr).read_text())
        assert rec['status']=='passed'
        assert rec['proof_sha256']==deps[pp] and rec['script_sha256']==deps[ss]
        assert all(sha(ROOT/p)==h for p,h in rec.get('dependencies_sha256',rec.get('dependencies',{})).items()),stem
    exact=[]
    def zero(name,value):
        assert sp.simplify(sp.expand(value))==0,name
        exact.append(name)
    I=sp.I;pi=sp.pi
    N,x,y,a,b,eps,u,v,p,q=sp.symbols('N x y a b eps u v p q',real=True)
    z,w=sp.symbols('z w')
    E=lambda w:-I*pi*w*(w+1)/(2*N)+I*pi*w/2
    zero('exact complex marked reflection',2*E(w)-(-I*pi*w*(w+1)/N+I*pi*w))
    zero('upper primitive and symbol exponents',2*E(N*z)-(I*pi*N*(z-z*z)-I*pi*z))
    zero('upper primitive full-period shift',I*pi*((z+1)-(z+1)**2)-I*pi*(z-z*z)+2*pi*I*z)
    zero('upper symbol is antiperiodic',sp.exp(-I*pi*(z+1))+sp.exp(-I*pi*z))
    poly=(z+a)-(z+a)**2+(z+b)-(z+b)**2-(2+eps)*(z-z*z)+4*a*z
    target=a*(1-a)+b*(1-b)+2*z*(a-b)+eps*(z*z-z)
    zero('upper conditional phase including original chirp',poly-target)
    zero('real upper rate relative to lower reflection',sp.re(I*pi*target.subs(z,x+I*y))+2*pi*y*(a-b+eps*(x-sp.Rational(1,2))))
    L=lambda xx:a-b+eps*(xx-sp.Rational(1,2))
    zero('upper mirror has additional positive term',-2*pi*y*(L(x)-L(1-x))-2*pi*eps*y*(1-2*x))
    zero('upper final endpoint loses two pi epsilon height',-2*pi*y*(L(1)-L(0))+2*pi*eps*y)
    row=lambda s,aa,bb,ee:2*pi*I*N*aa*s+E(N*(s+aa))+E(N*(s+bb))-(2+ee)*E(N*s)
    refl=sp.re(row(x-I*y,a,b,eps)-row(x+I*y,a,b,eps))
    zero('exact finite row reflection',refl-(2*pi*N*y*L(x)+eps*pi*y))
    zero('midpoint correction cancels exactly',refl.subs(x,-1/(2*N))-2*pi*N*y*(a-b-eps/2))
    omega=I*pi*N*(a*(1-a)+b*(1-b))-I*pi*(a+b)
    zero('type-three constant permutation Schwarz carrier',row(x+I*y,a,b,0)-sp.conjugate(row(x-I*y,b,a,0))-omega)
    zero('type-four residual is an index-dependent chirp',row(x+I*y,a,b,1)-sp.conjugate(row(x-I*y,b,a,1))-omega+2*E(N*(x+I*y)))
    S=u+I*v
    F0=S*S+(p+q)*S-1+I*(q-p)
    zero('quadratic root height sign',sp.im(sp.expand(F0))-(v*(2*u+p+q)+q-p))
    zero('original local amplitude exponent',-I*pi*((z+a)+(z+b)-(2+eps)*z)/2-I*pi*(eps*z-a-b)/2)
    zero('unchanged N Gaussian normalization',1-eps/2-sp.Rational(1,2)-(1-eps)/2)
    finite=[]
    r=sp.symbols('r')
    for level in(2,3,4,5,6):
        cp=sp.Poly(sp.cyclotomic_poly(level,r),r,domain=sp.QQ)
        def red(expr):return sp.rem(sp.Poly(sp.expand(expr),r,domain=sp.QQ),cp).as_expr()
        def mul(f,g):return red(f*g)
        def rp(k):return red(r**(k%level))
        def conjugate(f):
            pp=sp.Poly(f,r,domain=sp.QQ)
            return red(sum(cc*rp(-mon[0])for mon,cc in pp.terms()))
        P=[sp.Integer(1)]
        for j in range(1,level):P.append(mul(P[-1],1-rp(j)))
        inv=[sp.invert(sp.Poly(pp,r,domain=sp.QQ),cp).as_expr()for pp in P]
        def L(aa,bb):
            return red(sum(mul(rp(-aa*j),mul(P[j+aa]*P[j+bb],inv[j]**2))for j in range(level-max(aa,bb))))
        for aa in range(level):
            for bb in range(level):
                carrier=(-1)**(aa+bb)*rp((aa*(aa+1)+bb*(bb+1))//2)
                assert red(L(aa,bb)-mul(carrier,conjugate(L(bb,aa))))==0,(level,aa,bb)
                finite.append([level,aa,bb])
    assert sha(PROOF)==proof_hash and sha(__file__)==script_hash
    assert all(sha(ROOT/p)==h for p,h in deps.items())
    result={'status':'passed','arithmetic':'exact symbolic and rational cyclotomic polynomial arithmetic',
            'exact_identity_count':len(exact),'exact_identities':exact,
            'exact_finite_symmetry_comparisons':len(finite),'finite_cases':finite,
            'proof_sha256':proof_hash,'script_sha256':script_hash,'dependencies_sha256':deps,
            'scope':'Upper-half original interpolation calibration and complete all-real conditional packet normalization. No complex-taper or remaining outer-sum theorem.'}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS',len(exact),'exact identities,',len(finite),'exact finite symmetry comparisons')

if __name__=='__main__':main()
