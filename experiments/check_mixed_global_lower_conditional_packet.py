#!/usr/bin/env python3
"""Exact finite normalization and contour algebra for the full lower packet."""
import argparse
import hashlib
import json
from pathlib import Path
import sympy as sp

ROOT=Path(__file__).resolve().parents[1]
PROOF=ROOT/'notes/research_mixed_global_lower_conditional_packet.md'

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=ROOT/'repro/results/research-mixed-global-lower-conditional-packet.json')
    args=parser.parse_args()
    proof_hash,script_hash=sha(PROOF),sha(__file__)
    stems=['mixed_global_cotangent_roots','mixed_real_conditional_contour_geometry',
           'mixed_negative_height_full_period','lower_half_factorial_continuation']
    deps={}
    for stem in stems:
        pp=f'notes/research_{stem}.md';ss=f'experiments/check_{stem}.py'
        rr=f'repro/results/research-{stem.replace("_","-")}.json'
        for p in(pp,ss,rr):deps[p]=sha(ROOT/p)
        rec=json.loads((ROOT/rr).read_text())
        assert rec['status']=='passed'
        assert rec['proof_sha256']==deps[pp] and rec['script_sha256']==deps[ss]
        inherited=rec.get('dependencies_sha256',rec.get('dependencies',{}))
        assert all(sha(ROOT/p)==h for p,h in inherited.items()),stem
    deps['notes/exact_factorial_interpolation_and_complex_contours.md']=sha(ROOT/'notes/exact_factorial_interpolation_and_complex_contours.md')
    identities=[]
    def zero(name,expr):
        assert sp.simplify(sp.expand(expr))==0,name
        identities.append(name)
    N,x,y,a,b,eps,t=sp.symbols('N x y a b eps t',real=True)
    I=sp.I;pi=sp.pi
    E=lambda w:-I*pi*w*(w+1)/(2*N)+I*pi*w/2
    row=lambda s:2*pi*I*N*a*s+E(N*(s+a))+E(N*(s+b))-(2+eps)*E(N*s)
    zero('row reflection across every shifted wall',sp.re(row(x-I*y)-row(x+I*y))-(2*pi*N*y*(a-b+eps*(x-sp.Rational(1,2)))+eps*pi*y))
    zero('left midpoint reflection has no hidden constant',sp.re(row(-1/(2*N)-I*y)-row(-1/(2*N)+I*y))-2*pi*N*y*(a-b-eps/2))
    zero('literal cotangent residue is one',N/(2*I)*(2*pi*I)/(pi*N)-1)
    B,U=sp.symbols('B U')
    # Upper and lower Cauchy identities make their non-real boundary sums
    # respectively -B and +B, with B the left-to-right real segment.
    zero('two constant modes give positive N',N/(2*I)*((-I)*(-B)+I*B)-N*B)
    zero('upper midpoint cotangent remainder',1-(t-1)/(t+1)-2/(t+1))
    zero('lower midpoint cotangent remainder',1+(1-t)/(1+t)-2/(1+t))
    theta=sp.symbols('theta',real=True)
    zero('all-real full-period multiplier inequality',(1+t)**2-(1+t*t+2*t*sp.cos(theta))-2*t*(1-sp.cos(theta)))
    zero('original Gaussian amplitude phase',-pi*((x+a)+(x+b)-(2+eps)*x)/2-pi*(eps*x-a-b)/2)
    zero('full source power',1-eps/2-sp.Rational(1,2)-(1-eps)/2)
    zero('midpoint vertical power',1-(2+eps)/2+eps/2)
    finite=[]
    z=sp.symbols('z')
    for level in(2,3,4,5,6):
        cyclo=sp.Poly(sp.cyclotomic_poly(level,z),z,domain=sp.QQ)
        def red(expr):
            return sp.rem(sp.Poly(sp.expand(expr),z,domain=sp.QQ),cyclo).as_expr()
        def mul(f,g):return red(f*g)
        def zp(k):return red(z**(k%level))
        factorial=[sp.Integer(1)]
        for j in range(1,level):factorial.append(mul(factorial[-1],1-zp(j)))
        inverse=[sp.invert(sp.Poly(p,z,domain=sp.QQ),cyclo).as_expr() for p in factorial]
        for aa in range(level):
            for bb in range(level):
                numer_a=[factorial[aa]];numer_b=[factorial[bb]]
                for j in range(1,level):
                    numer_a.append(mul(numer_a[-1],1-zp(aa+j)))
                    numer_b.append(mul(numer_b[-1],1-zp(bb+j)))
                for ep in(0,1):
                    full=sp.Integer(0);physical=sp.Integer(0)
                    for j in range(level):
                        weight=mul(zp(-aa*j),red(inverse[j]**(2+ep)))
                        full=red(full+mul(weight,mul(numer_a[j],numer_b[j])))
                        if j+max(aa,bb)<level:
                            physical=red(physical+mul(weight,mul(factorial[j+aa],factorial[j+bb])))
                        else:
                            assert mul(numer_a[j],numer_b[j])==0
                    assert red(full-physical)==0,(level,aa,bb,ep)
                    finite.append([level,aa,bb,ep])
    assert sha(PROOF)==proof_hash and sha(__file__)==script_hash
    assert all(sha(ROOT/p)==h for p,h in deps.items())
    result={'status':'passed','arithmetic':'exact symbolic and rational cyclotomic polynomial arithmetic',
            'exact_identity_count':len(identities),'exact_identities':identities,
            'exact_finite_source_comparisons':len(finite),'finite_cases':finite,
            'levels':[2,3,4,5,6],'proof_sha256':proof_hash,'script_sha256':script_hash,
            'dependencies_sha256':deps,
            'scope':'Exact all-row canonical/physical reduction, residue and reflection normalization. The full compact lower-height source theorem follows from the written global contour proof and its validated analytic dependencies, not finite-level extrapolation.'}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS',len(identities),'exact identities,',len(finite),'exact finite source comparisons')

if __name__=='__main__':main()
