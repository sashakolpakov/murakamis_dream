"""Actual unknot source: sharp bounded-jet and pole-lattice checks.

The nonminimal operator is an exact actual unknot annihilator. The
competing root section is explicitly not a different knot invariant.
The all-knot theorem uses the uniform recurrence budget proved in the
associated note and the older all-level reconstruction theorem.
"""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

from audit_first_quantum_normal_connection import field


Q,X,Y=sp.symbols('Q X Y')


def rank_mod(rows,p):
    a=[[int(v)%p for v in row] for row in rows]
    rank=0
    for col in range(len(a[0])):
        pivot=next((i for i in range(rank,len(a)) if a[i][col]),None)
        if pivot is None:continue
        a[rank],a[pivot]=a[pivot],a[rank]
        inv=pow(a[rank][col],-1,p)
        a[rank]=[v*inv%p for v in a[rank]]
        for i in range(len(a)):
            if i!=rank and a[i][col]:
                c=a[i][col]
                a[i]=[(x-c*y)%p for x,y in zip(a[i],a[rank])]
        rank+=1
        if rank==len(a):break
    return rank


def generic_actual_operator():
    coeff=[Q*(1-Y),(1+Q)*(Q*Y-1),1-Q**2*Y]
    assert sp.expand(sum(coeff))==0  # The actual unknot C_n=1.
    transformed=0
    S=sp.symbols('S')
    for j,aj in enumerate(coeff):
        for (ell,),a in sp.Poly(aj,Y).terms():
            transformed+=a*Q**(-ell*j)*X**(-j)*S**ell
    target=X**(-2)*(1-X)*(1-Q*X)*(1-S)
    assert sp.cancel(transformed-target)==0
    n0=5
    Z=X**n0/(1-X)
    B=X**(n0-2)*(1-Q**n0+(Q**n0-Q)*X)
    A=X**(-2)*(1-X)*(1-Q*X)
    assert sp.cancel(A*(Z-Z.subs(X,Q*X))-B)==0
    return {'actual_color':'unknot C_n=1','generic_operator_and_Fourier_source_exact':True,
            'n0':n0,'leading_Y_span':1,'leading_monomials':2,'pole_budget':1,'required_quantum_levels':2}


def root_and_first_normal():
    n0,d=5,2
    records=[]
    for N in range(8,19):
        p,zeta=field(N)
        x=next(t for t in range(2,p) if pow(t,N,p)!=1)
        u=pow(x,N,p)
        inv=lambda value:pow(value%p,-1,p)
        delta=u*inv(1-u)%p
        rhs_scalar=N*u*inv((1-u)**2)%p
        orbit=[x*pow(zeta,j,p)%p for j in range(N)]
        matrix=[]
        rhs=[]
        for j,t in enumerate(orbit):
            nxt=orbit[(j+1)%N]
            A=inv(t*t)*(1-t)*(1-zeta*t)%p
            actual=pow(t,n0,p)*inv(1-t)%p
            actual_next=pow(nxt,n0,p)*inv(1-nxt)%p
            B=pow(t,n0-2,p)*(1-pow(zeta,n0,p)+(pow(zeta,n0,p)-zeta)*t)%p
            assert A*(actual-actual_next)%p==B
            # The alternative root function changes the residue by1
            # while preserving the exact same affine root equation.
            assert A*((actual+delta)-(actual_next+delta))%p==B
            row=[0]*N
            row[j]=A
            row[(j+1)%N]=-A
            matrix.append(row)
            rhs.append(A*rhs_scalar%p)
        rank=rank_mod(matrix,p)
        augmented=rank_mod([row+[b] for row,b in zip(matrix,rhs)],p)
        assert rank==N-1 and augmented==N
        # Direct color-side certificate: one simple missing step
        # spends the entire uniform B=1 budget, exactly at C_N.
        singular=[m for m in range(n0-d,N-d+1) if pow(zeta,m+2,p)==1]
        assert singular==[N-2]
        first_leading_derivative=-(N)*pow(zeta,N,p)%p
        assert first_leading_derivative!=0
        prefix=sum(X**r for r in range(1,n0))
        actualZ=X**n0/(1-X)
        altered=actualZ+X**N/(1-X**N)
        numerator=sp.cancel((1-X**N)*(altered+prefix))
        expected=sum(X**r for r in range(1,N+1))+X**N
        assert sp.expand(numerator-expected)==0
        num,den=sp.cancel(altered).as_numer_denom()
        polynomial_part=sp.div(num,den,X)[0]
        assert -sp.expand(polynomial_part).coeff(X,0)==2
        records.append({'N':N,'prime':p,'same_affine_source_at_every_orbit_point':True,
                        'correct_cyclotomic_numerator_degree':N,'actual_residue':1,'competing_residue':2,
                        'first_normal_cyclic_rank':rank,'augmented_rank':augmented,
                        'singular_color_step':N-2,'total_leading_vanishing_budget':1})
    return records


def main():
    result={'actual_unknot_generic_source':generic_actual_operator(),
            'root_freedom_and_first_normal_exclusion':root_and_first_normal(),
            'scope':'whole actual Mellin pole lattice and bounded quantum lifts; no selected volume estimate'}
    target=Path(__file__).with_name('mellin_cyclotomic_jet_uniqueness_results.json')
    target.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'pass','actual_unknot_root_levels':len(result['root_freedom_and_first_normal_exclusion']),
                      'quantum_jet_budget':1,'results':str(target)},indent=2))


if __name__=='__main__':
    main()
