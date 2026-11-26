#!/usr/bin/env python3
"""Exact conditional Fourier/Gram identities and original cyclic traces.

The general finite proofs are in the note. These exact checks verify
normalization and endpoint forcing, not an asymptotic lower bound.
"""
import argparse,json
from pathlib import Path
from hashlib import sha256
import sympy as sp

ROOT=Path(__file__).resolve().parents[1]

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output',type=Path,default=ROOT/'repro/results/research-mixed-conditional-leg-sum.json')
    args=ap.parse_args();identities=[]
    field=sp.QQ.algebraic_field(sp.I,sp.sqrt(2),sp.sqrt(3));one,zero=field.one,field.zero
    cv=lambda x:field.from_sympy(sp.sympify(x))
    def conj(x):return cv(sp.conjugate(field.to_sympy(x)))
    def prod(values):
        out=one
        for v in values:out*=v
        return out
    def check(name,value):
        assert value==zero,(name,field.to_sympy(value));identities.append(name)
    def multiply(A,B):
        n=len(A);return [[sum((A[a][i]*B[i][b]for i in range(n)),zero)for b in range(n)]for a in range(n)]
    def polprod(a,b):
        out=[zero]*(len(a)+len(b)-1)
        for j,x in enumerate(a):
            for k,y in enumerate(b):out[j+k]+=x*y
        return out
    def evalpoly(c,x):
        out=zero
        for v in reversed(c):out=out*x+v
        return out
    for N,qs in [(2,sp.I),(3,(1+sp.I*sp.sqrt(3))/2),(4,(1+sp.I)/sp.sqrt(2)),(6,(sp.sqrt(3)+sp.I)/2)]:
        q=cv(qs);ii=cv(sp.I);r=q**-2;Q=q*q;D=N-1
        P=[prod(1-r**h for h in range(1,a+1))for a in range(N)]
        S=[prod((q**h-q**(-h))/ii for h in range(1,a+1))for a in range(N)]
        delta=[ii**a*q**(-a*(a+1)//2)for a in range(N)];tau=[d*d for d in delta]
        check(f'N{N} full nonzero root product',P[-1]-N)
        polynomials=[]
        for a in range(N):
            poly=[one]
            for h in range(1,a+1):poly=polprod(poly,[one,-r**h])
            polynomials.append(poly)
            assert poly[-1]!=zero
            check(f'N{N} original phase a{a}',P[a]-delta[a]*S[a])
            for j,c in enumerate(poly):
                target=(-1)**j*q**(-j*(a+1))*S[a]/(S[j]*S[a-j])
                check(f'N{N} sine-binomial coefficient a{a} j{j}',c-target)
        values=[[evalpoly(polynomials[a],r**i)for i in range(N)]for a in range(N)]
        for a in range(N):
            for i in range(N):
                expected=P[i+a]/P[i]if i+a<N else zero
                check(f'N{N} exact conditional zero/support a{a} i{i}',values[a][i]-expected)
                check(f'N{N} node conjugation a{a} i{i}',r**(-a*i)*values[a][i]-tau[a]*conj(values[a][i]))
        moments=[sum((r**(d*i)/P[i]for i in range(N)),zero)for d in range(N)]
        for d in range(-N-2,N+3):
            check(f'N{N} forced Laurent moment d{d}',(r**d-1)*moments[d%N]+moments[(d+1)%N]-one/N)
        check(f'N{N} exact first moment',moments[1]-one/N)
        for d in range(1,N+1):
            check(f'N{N} explicit forced moment d{d}',moments[d%N]-P[d-1]*sum((one/P[j]for j in range(d)),zero)/N)
        for d in range(N+1):
            left=r**d/P[d]if d<N else zero
            right=(one/P[d]if d<N else zero)-(one/P[d-1]if d>=1 else zero)+(one/N if d==N else zero)
            check(f'N{N} entire q-exponential polynomial coefficient d{d}',left-right)
        T=[[[zero for b in range(N)]for a in range(N)]for eps in range(2)]
        for a in range(N):
            for b in range(N):
                F=polprod(polynomials[a],polynomials[b])
                L=[sum((r**(-a*i)*P[i+a]*P[i+b]/P[i]**(2+eps)for i in range(N-max(a,b))),zero)for eps in range(2)]
                for eps in range(2):
                    extension=sum((r**(-a*i)*values[a][i]*values[b][i]/P[i]**eps for i in range(N)),zero)
                    check(f'N{N} full-period conditional eps{eps} a{a} b{b}',L[eps]-extension)
                    T[eps][a][b]=L[eps]/(P[a]**2*P[b]**eps)
                check(f'N{N} no-alias coefficient a{a} b{b}',L[0]-N*F[a])
                gram=sum((conj(polynomials[a][j])*polynomials[b][j]for j in range(min(a,b)+1)),zero)
                check(f'N{N} positive circle Gram a{a} b{b}',L[0]-N*tau[a]*gram)
                sinegram=sum((q**(j*(a-b))*S[a]*S[b]/(S[j]**2*S[a-j]*S[b-j])for j in range(min(a,b)+1)),zero)
                check(f'N{N} residual linear Fourier phase a{a} b{b}',L[0]-N*tau[a]*sinegram)
                weighted=sum((conj(values[a][i])*values[b][i]/P[i]for i in range(N)),zero)
                check(f'N{N} original four weighted Gram a{a} b{b}',L[1]-tau[a]*weighted)
                check(f'N{N} forced moment expansion a{a} b{b}',L[1]-sum((c*moments[(d-a)%N]for d,c in enumerate(F)),zero))
        for a in range(N):
            for b in range(N):check(f'N{N} exact positive metric a{a} b{b}',S[a]**2*T[0][a][b]-S[b]**2*conj(T[0][b][a]))
        # Literal original crossing, with scalar kappa removed.
        C=[prod(1-Q**h for h in range(1,a+1))for a in range(N)]
        M=[[(-1)**a*q**(a+b*b)*C[a]/(C[b]*C[a-b])if b<=a else zero for b in range(N)]for a in range(N)]
        M2=multiply(M,M);M3=multiply(M2,M);M4=multiply(M2,M2)
        original={3:[[q**(D*D)*M3[D-a][b]for b in range(N)]for a in range(N)],
                  4:[[q**(D*D)*M4[D-a][b]/N for b in range(N)]for a in range(N)]}
        for word in [(3,),(4,),(3,4),(3,4,3),(4,3,4,3)]:
            left=original[word[0]];right=T[word[0]-3]
            for n in word[1:]:left=multiply(left,original[n]);right=multiply(right,T[n-3])
            check(f'N{N} full original normalized cyclic word {word}',sum((left[j][j]-right[j][j]for j in range(N)),zero))
    deps=['notes/research_mixed_conditional_leg_sum.md','notes/research_mixed_wire_exact_contraction.md',
          'notes/research_mixed_three_four_operator_obstruction.md','notes/research_three_four_source_interface.md']
    result={'status':'passed','exact_identity_count':len(identities),'exact_identities':identities,
            'levels':[2,3,4,6],'arithmetic':'Exact Q(i,sqrt(2),sqrt(3)) coefficient and matrix algebra',
            'scope':'Original conditional support/scalars, no-alias coefficient, positive and weighted Grams, forced finite moments, and original cyclic word traces. No asymptotic lower bound.',
            'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
            'dependencies_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest()for p in deps}}
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k]for k in ['status','exact_identity_count','levels']}))

if __name__=='__main__':main()
