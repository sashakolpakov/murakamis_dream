#!/usr/bin/env python3
"""Exact original-matrix and finite-binomial checks for the power-four sum.

The general identities are proved in the note. These finite checks use
exact number-field arithmetic, not fitted numerical matrix entries.
No saddle dominance or source remainder is checked here.
"""
import argparse
from hashlib import sha256
import json
from pathlib import Path
import sympy as sp

ROOT=Path(__file__).resolve().parents[1]


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=ROOT/'repro/results/research-power-four-finite-source.json')
    args=parser.parse_args()
    identities=[]
    def exact(name,expr):
        assert sp.cancel(expr)==0,name
        identities.append(name)
    r,a,K=sp.symbols('r a K')
    def symbolic_poch(z,q,n):
        return sp.prod(1-z*q**j for j in range(n))
    for d in range(7):
        lhs=sum(symbolic_poch(r**(-d),r,l)*a**l/symbolic_poch(r,r,l) for l in range(d+1))
        exact(f'generic finite binomial degree {d}',lhs-symbolic_poch(a*r**(-d),r,d))
    U=(1-K)/(2*K)
    exact('diagonal stationary exponent',K*(1-U**2)-(1-U)*(1-K*U))

    field=sp.QQ.algebraic_field(sp.I,sp.sqrt(2),sp.sqrt(3))
    one,zero=field.one,field.zero
    def cv(x):return field.from_sympy(sp.sympify(x))
    def prod(seq):
        out=one
        for value in seq:out*=value
        return out
    def poch(z,q,n):return prod(1-z*q**j for j in range(n))
    def checked(name,value):
        assert value==zero,name
        identities.append(name)
    def mm(A,B):
        n=len(A)
        return [[sum((A[i][k]*B[k][j] for k in range(n)),zero) for j in range(n)] for i in range(n)]
    def polynomial_product(factors):
        out=[one]
        for value in factors:
            new=[zero]*(len(out)+1)
            for j,c in enumerate(out):
                new[j]+=c
                new[j+1]-=value*c
            out=new
        return out

    levels=[]
    for N,qs in [(2,sp.I),(3,(1+sp.I*sp.sqrt(3))/2),
                 (4,(1+sp.I)/sp.sqrt(2)),(6,(sp.sqrt(3)+sp.I)/2)]:
        q=cv(qs);Q=q*q;r=one/Q
        checked(f'N{N} primitive-root scalar',Q**N-one)
        checked(f'N{N} full root product',poch(r,r,N-1)-N)
        for j in range(N):
            P=polynomial_product(Q**a for a in range(j+1,N))
            for k in range(N):
                value=sum((c*Q**(k*(N-1-d)) for d,c in enumerate(P)),zero)
                claimed=zero if k>j else Q**(-k)*poch(Q,Q,N-1-k)/poch(Q,Q,j-k)
                checked(f'N{N} coefficient support j{j} k{k}',value-claimed)
        for i in range(N):
            for k in range(N-i):
                d=N-1-i-k
                lhs=sum((poch(r,r,i+k+l)*r**(-k*l)/poch(r,r,l) for l in range(d+1)),zero)
                rhs=poch(r,r,i+k)*poch(r,r,N-1-k)/poch(r,r,i)
                checked(f'N{N} root-binomial collapse i{i} k{k}',lhs-rhs)
        M0=[[zero]*N for _ in range(N)]
        for j in range(N):
            for k in range(j+1):
                gauss=poch(Q,Q,j)/(poch(Q,Q,k)*poch(Q,Q,j-k))
                M0[j][k]=(-1)**j*q**(j+k*k)*gauss
        square=mm(M0,M0);fourth=mm(square,square)
        for case,(xs,ys) in enumerate([
            (sp.Rational(1,3)+sp.I/5,sp.Rational(1,4)+sp.I/7),
            (sp.Rational(2,5)-sp.I/6,sp.Rational(1,5)+sp.I/3)]):
            X,Y=cv(xs),cv(ys)
            dx=[(-one/q)**i/(1-X*r**i) for i in range(N)]
            dy=[(-one/q)**i/(1-Y*r**i) for i in range(N)]
            # M=kappa*M0. Dividing literal JM^4 by kappa^2 leaves
            # kappa^2=q^(N-1)^2, so no fourth-root representation is needed.
            literal=q**((N-1)**2)*sum((dx[i]*fourth[N-1-i][j]*dy[j] for i in range(N) for j in range(N)),zero)
            triple=sum(((-1)**j*Q**(j*(j+1)//2)*X**i*Y**k*poch(r,r,i+j)
                        /(poch(X,r,i+1)*poch(Y,r,k+1)*poch(Q,Q,j-k))
                        for i in range(N) for j in range(N-i) for k in range(j+1)),zero)
            double=N*sum((X**i*Y**k*poch(r,r,i+k)
                          /(poch(r,r,i)*poch(r,r,k)*poch(X,r,i+1)*poch(Y,r,k+1))
                          for i in range(N) for k in range(N-i)),zero)
            checked(f'N{N} case{case} literal original matrix vs triple',literal-triple)
            checked(f'N{N} case{case} literal original matrix vs double',literal-double)
        levels.append(N)

    deps=[
        'notes/research_power_four_finite_source.md',
        'notes/research_three_four_source_interface.md',
        'notes/research_crossing_cauchy_transport.md',
        'notes/research_exterior_crossing_phase.md',
        'notes/research_traced_three_vertex_endpoint.md',
    ]
    result={
        'status':'passed',
        'scope':'Exact generic finite-binomial identities, root-of-unity coefficient support and collapse, and literal original JM^4 comparisons at two rational complex inputs per finite level. The written proof gives the all-level identity; no full-source asymptotic or contour dominance is checked.',
        'arithmetic':'Exact rational functions and Q(i,sqrt(2),sqrt(3)) number-field arithmetic',
        'exact_identity_count':len(identities),'exact_identities':identities,'finite_levels':levels,
        'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
        'dependencies_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},
    }
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['status','exact_identity_count','finite_levels']},indent=2))


if __name__=='__main__':
    main()
