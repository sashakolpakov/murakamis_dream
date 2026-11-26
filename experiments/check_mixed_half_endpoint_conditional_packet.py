#!/usr/bin/env python3
"""Exact closed-half-endpoint root, coefficient, and finite support checks."""
import argparse,hashlib,json
from pathlib import Path
import sympy as sp
ROOT=Path(__file__).resolve().parents[1]
PROOF=ROOT/'notes/research_mixed_half_endpoint_conditional_packet.md'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=ROOT/'repro/results/research-mixed-half-endpoint-conditional-packet.json')
    args=parser.parse_args()
    proof_hash,script_hash=sha(PROOF),sha(__file__)
    deps={}
    stems=['mixed_global_cotangent_roots','mixed_real_conditional_contour_geometry',
           'mixed_negative_height_full_period','lower_half_factorial_continuation',
           'mixed_global_lower_conditional_packet','mixed_all_real_conditional_packet']
    for stem in stems:
        pp=f'notes/research_{stem}.md';ss=f'experiments/check_{stem}.py';rr=f'repro/results/research-{stem.replace("_","-")}.json'
        for path in(pp,ss,rr):deps[path]=sha(ROOT/path)
        rec=json.loads((ROOT/rr).read_text());assert rec['status']=='passed'
        assert rec['proof_sha256']==deps[pp]and rec['script_sha256']==deps[ss]
        assert all(sha(ROOT/p)==h for p,h in rec.get('dependencies_sha256',rec.get('dependencies',{})).items()),stem
    identities=[]
    def zero(name,value):
        assert sp.simplify(sp.expand(value))==0,name
        identities.append(name)
    u,v,p,q,delta,eps,N=sp.symbols('u v p q delta eps N',real=True)
    I=sp.I;S=u+I*v
    F0=lambda z:z*z+(p+q)*z-1+I*(q-p)
    F1=lambda z:(z+I)*(z+p)*(z+q)-2*I*(p-I)*(q+I)
    zero('quadratic upper boundary including q zero',sp.im(sp.expand(F0(u+I)))-(2*u+2*q))
    zero('quadratic lower boundary including p zero',sp.im(sp.expand(F0(u-I)))+2*u+2*p)
    zero('quadratic entire left boundary',sp.re(sp.expand(F0(I*v)))+1+v*v)
    zero('cubic entire left boundary',sp.im(sp.expand(F1(I*v)))-((v-1)*p*q-v*v*(v+1)-2))
    T=u+I;D=(T+I)*(T+q)-2*I*(q+I);Z=2*(q+I)-T*(T+I)*(T+q)
    zero('upper boundary forced denominator',D-u*(u+q+3*I))
    forced=-1-2*(4*q+u*q*(u+q)+u)/(u*((u+q)**2+9))
    zero('upper boundary forced imaginary part',sp.im(sp.expand_complex(Z/D))-forced)
    first=(p+u-I)/(p-I)
    zero('lower first-factor real part including p zero',sp.re(first)-1-u*p/(p*p+1))
    zero('lower first-factor positive imaginary part',sp.im(first)-u/(p*p+1))
    second=(q+u-I)/(q+I)
    zero('lower factor formula at q zero',second.subs(q,0)+1+I*u)
    C=-u/(u*u+v*v)
    H=sp.Matrix([[u-C,-C],[-C,-C]])
    zero('strict half-endpoint triangle determinant',H.det()-u*u/(u*u+v*v))
    zero('half-endpoint inner diagonal',H[0,0]-(u+u/(u*u+v*v)))
    zero('half-endpoint outer diagonal',H[1,1]-u/(u*u+v*v))
    zero('height-circle quadratic at zero outer cotangent',-(2*v+1)*(2*v*v+2*v+1)+(2*v+1)*(2*(v+sp.Rational(1,2))**2+sp.Rational(1,2)))
    x=sp.symbols('x',real=True)
    trig=sp.sin(x+sp.pi/2)**2-sp.sin(x)**2-sp.cos(2*x)
    assert sp.trigsimp(trig)==0;identities.append('half-neighbor strict low-arc sine difference')
    R=sp.symbols('R',real=True)
    zero('half-neighbor integrated mirror margin',R*(1-sp.cos(sp.pi))/(sp.pi*(1+R)**2)-2*R/(sp.pi*(1+R)**2))
    zero('uniform type-four alias reserve',(sp.Rational(1,2)-delta)+sp.Rational(1,2)-(1-delta))
    zero('nonzero Gaussian power at the endpoint',1-eps/2-sp.Rational(1,2)-(1-eps)/2)
    # The half-neighbor factor is 1+r^h at every level.  It vanishes
    # within a period precisely at the even-level physical half index.
    z=sp.symbols('z');support=[];physical=[]
    for level in range(2,11):
        cp=sp.Poly(sp.cyclotomic_poly(level,z),z,domain=sp.QQ)
        def red(e):return sp.rem(sp.Poly(sp.expand(e),z,domain=sp.QQ),cp).as_expr()
        def mul(a,b):return red(a*b)
        def zp(k):return red(z**(k%level))
        prod=sp.Integer(1)
        for j in range(level):
            if j:prod=mul(prod,1+zp(j))
            expected=(level%2==0 and j>=level//2)
            assert (prod==0)==expected,(level,j)
            support.append([level,j,expected])
        full=sp.Integer(1)
        for h in range(1,level+1):full=mul(full,1+zp(h))
        assert full==1-(-1)**level
        if level%2:continue
        aa=level//2;P=[sp.Integer(1)]
        for j in range(1,level):P.append(mul(P[-1],1-zp(j)))
        inv=[sp.invert(sp.Poly(pp,z,domain=sp.QQ),cp).as_expr()for pp in P]
        for bb in range(1,aa+1):
            for ep in(0,1):
                canonical=sp.Integer(0);original=sp.Integer(0)
                na=P[aa];nb=P[bb]
                for j in range(level):
                    if j:na=mul(na,1-zp(aa+j));nb=mul(nb,1-zp(bb+j))
                    wt=mul(zp(-aa*j),red(inv[j]**(2+ep)))
                    canonical=red(canonical+mul(wt,mul(na,nb)))
                    if j+max(aa,bb)<level:original=red(original+mul(wt,mul(P[j+aa],P[j+bb])))
                assert canonical==original
                physical.append([level,aa,bb,ep])
    assert sha(PROOF)==proof_hash and sha(__file__)==script_hash
    assert all(sha(ROOT/p)==h for p,h in deps.items())
    result={'status':'passed','arithmetic':'exact symbolic and cyclotomic polynomial arithmetic',
            'exact_identity_count':len(identities),'exact_identities':identities,
            'exact_even_odd_row_support_checks':len(support),'support_checks':support,
            'exact_physical_half_endpoint_comparisons':len(physical),'physical_cases':physical,
            'proof_sha256':proof_hash,'script_sha256':script_hash,'dependencies_sha256':deps,
            'scope':'Uniform original conditional packet for compact real neighbor sets in (0,1/2]^2. No uniform zero-neighbor or remaining outer-sum assertion.'}
    args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS',len(identities),'exact identities,',len(support),'even/odd support checks,',len(physical),'physical endpoint comparisons')

if __name__=='__main__':main()
