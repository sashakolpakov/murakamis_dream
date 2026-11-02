#!/usr/bin/env python3
"""Exact algebra checks for the meridian gauge and formal coefficient argument.
No asymptotic or geometric conclusion is inferred from these finite checks.
"""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output',type=Path,default=Path(__file__).resolve().parent/'build/check')
    args=ap.parse_args();args.output.mkdir(parents=True,exist_ok=True)
    dest=args.output/'summary.json';dest.unlink(missing_ok=True)
    if not __debug__:raise SystemExit('Assertions must be enabled; do not use -O.')
    import sympy as sp
    base=Path(__file__).resolve().parent
    inputs=sorted(base.glob('*.tex'))+sorted((base/'figures').glob('*.tex'))+[Path(__file__).resolve()]
    hashes={str(p.relative_to(base)):hashlib.sha256(p.read_bytes()).hexdigest() for p in inputs}
    q,M,z,h,u,s=sp.symbols('q M z h u s',nonzero=True)
    f=lambda w:w-1/w
    counts={'sine_ratio_identities':0,'root_level_gauge_identities':0,
            'cleared_classical_coefficients':0,'regrading_monomials':0,
            'finite_jet_negative_controls':0}
    # Direct exponential substitutions for both derivatives of K.
    plus=z*M-1/(z*M);minus=z/M-M/z;center=z-1/z
    assert sp.cancel(minus/plus-(M*M-z*z)/(1-M*M*z*z))==0
    counts['sine_ratio_identities']+=1
    assert sp.cancel(center**2/(plus*minus)-(1-z*z)**2/((1-z*z*M*M)*(1-z*z/(M*M))))==0
    counts['sine_ratio_identities']+=1
    # Derive the exact modified-dimension ratio, then reduce its numerator
    # modulo the actual all-level relation q^N=-1, without assuming q=1.
    for N in range(2,13):
        dim=lambda w:f(w)/(w**N-w**(-N))
        for j in range(7):
            expr=sp.together(dim(q**j*M)/dim(M)-(-1)**j*f(q**j*M)/f(M))
            num=sp.fraction(expr)[0].expand()
            assert sp.rem(num,q**N+1,q)==0,(N,j)
            counts['root_level_gauge_identities']+=1
    # Clear the whole operator on the left before taking its classical symbol.
    for r in range(7):
        denominator=sp.prod(f(q**k*M) for k in range(1,r+1))
        for j in range(r+1):
            cleared=sp.cancel(denominator*(-1)**j*f(M)/f(q**j*M))
            assert sp.cancel(cleared.subs(q,1)-(-1)**j*f(M)**r)==0
            counts['cleared_classical_coefficients']+=1
    # Check every monomial of one finite bidegree rectangle, independently
    # expanding the substituted expression with SymPy coefficient extraction.
    polynomial=sum((1+3*a+7*b)*h**a*u**b for a in range(9) for b in range(9))
    substituted=sp.Poly(polynomial.subs(u,h*s),h,s)
    for a in range(9):
        for b in range(9):
            assert substituted.coeff_monomial(h**(a+b)*s**b)==1+3*a+7*b
            counts['regrading_monomials']+=1
    for L in range(9):
        truncated=sum(c*h**n*s**b for (n,b),c in substituted.terms() if n<=L)
        expected=sum((1+3*a+7*b)*h**(a+b)*s**b for a in range(9) for b in range(9) if a+b<=L)
        assert sp.expand(truncated-expected)==0
        # A genuinely nonzero coefficient is invisible at each finite order.
        assert sp.series(h**(L+1),h,0,L+1).removeO()==0
        assert h**(L+1)!=0
        counts['finite_jet_negative_controls']+=1
    assert hashes=={str(p.relative_to(base)):hashlib.sha256(p.read_bytes()).hexdigest() for p in inputs},'inputs changed during check'
    result={'scope':'Exact rational sine and reduced/full gauge identities, and finite formal coefficient recovery. No analytic remainder, operator-existence or geometric assertion is tested.','checks':counts,'source_sha256':hashes}
    dest.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps(counts,sort_keys=True))

if __name__=='__main__':main()
