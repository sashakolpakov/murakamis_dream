#!/usr/bin/env python3
"""Bordered Hessians and the exact prefix momentum polarization.

Finite-field cases test universal rational identities, not discreteness
or the selected geometric cycle. Those hypotheses/proofs are in the note.
"""

from itertools import product
import json
from pathlib import Path

import sympy as sp


PRIME=1009


def mm(a,b):
    return tuple(sum(a[2*i+k]*b[2*k+j] for k in range(2))%PRIME
                 for i in range(2) for j in range(2))


def inv(a):
    di=pow((a[0]*a[3]-a[1]*a[2])%PRIME,-1,PRIME)
    return tuple(di*x%PRIME for x in (a[3],-a[1],-a[2],a[0]))


def add(*matrices):
    return tuple(sum(values)%PRIME for values in zip(*matrices))


def mul(c,a):return tuple(c*x%PRIME for x in a)


def ell(a,r,s):
    return (a[3]+(a[0]-a[3])*r+a[1]*s
            +a[2]*r*(1-r)*pow(s,-1,PRIME))%PRIME


def ell_prime(a,r,s):
    return (a[0]-a[3]+a[2]*(1-2*r)*pow(s,-1,PRIME))%PRIME


def local_data(U,V,r,s,sigma):
    ev=ell(V,r,s)
    if not ev:return None
    k=ell(U,r,s)*pow(ev,-1,PRIME)%PRIME
    if not k or k==1:return None
    C=add(U,mul(-k,V))
    F=(r%PRIME,(1-r)%PRIME,s%PRIME,-s%PRIME)
    Fi=inv(F)
    Ccur=mm(mm(Fi,C),F)
    assert Ccur[0]==0
    p=sigma*Ccur[1]*pow(k-1,-1,PRIME)%PRIME
    if not p:return None
    kp=(ell_prime(U,r,s)*ev-ell(U,r,s)*ell_prime(V,r,s))*pow(ev,-2,PRIME)%PRIME
    Fr=(1,-1,0,0)
    Fir=mul(-1,mm(mm(Fi,Fr),Fi))
    Ccurr=add(mm(mm(Fir,C),F),mm(mm(Fi,mul(-kp,V)),F),mm(mm(Fi,C),Fr))
    pp=sigma*(Ccurr[1]*(k-1)-Ccur[1]*kp)*pow(k-1,-2,PRIME)%PRIME
    return k,p,C,ev,kp,pp


def inverse_map(U,V,s,p,sigma):
    u=(p+pow(p,-1,PRIME))%PRIME
    vv=(pow(p,-1,PRIME)-p)%PRIME
    A0=(U[2]+s*(U[0]+U[3]))%PRIME
    A1=(V[2]+s*(V[0]+V[3]))%PRIME
    denominator=(s*u+sigma*A1)%PRIME
    if not denominator:return None
    k=(s*u+sigma*A0)*pow(denominator,-1,PRIME)%PRIME
    C=add(U,mul(-k,V))
    if not k or k==1 or not C[2]:return None
    D=-sigma*s*(k-1)*vv%PRIME
    r=(C[2]+s*(C[0]-C[3])-D)*pow(2*C[2],-1,PRIME)%PRIME
    return r,k,C,A0,A1,D


def rational_polarization():
    regular=caustics=density=0
    for vi,mi in product(range(3),repeat=2):
        a,b,c=2+vi,1+vi,2+vi
        V=(a,b,c,(1+b*c)*pow(a,-1,PRIME)%PRIME)
        u,v=1+mi,2+mi
        meridian=((1+u*v)%PRIME,-u*u%PRIME,v*v%PRIME,(1-u*v)%PRIME)
        U=mm(meridian,V)
        assert (meridian[0]+meridian[3])%PRIME==2
        for r,s,sigma in product(range(2,10),range(1,5),(-1,1)):
            original=local_data(U,V,r,s,sigma)
            if original is None:continue
            k,p,C,ev,kp,pp=original
            recovered=inverse_map(U,V,s,p,sigma)
            if recovered is None:continue
            rr,kk,CC,A0,A1,D=recovered
            assert rr==r and kk==k and CC==C
            actual_D=(C[2]+s*(C[0]-C[3])-2*C[2]*r)%PRIME
            assert actual_D==D
            regular+=1
            if pp and (A1-A0)%PRIME:
                left=p*pow(pp,-1,PRIME)*pow(s,-1,PRIME)%PRIME
                right=ev*(k-1)*pow((A1-A0)%PRIME,-1,PRIME)%PRIME
                assert left==right
                density+=1
        for s,p,sigma in product(range(1,5),(1,PRIME-1),(-1,1)):
            recovered=inverse_map(U,V,s,p,sigma)
            if recovered is None:continue
            r,k,C,_,_,D=recovered
            original=local_data(U,V,r,s,sigma)
            if original is None:continue
            kk,pp,CC,_,kp,pprime=original
            assert kk==k and pp==p and CC==C and D==0 and kp==0
            expected=-C[2]*pow(sigma*s*(k-1)%PRIME,-1,PRIME)%PRIME
            assert pprime==expected and pprime
            caustics+=1
    assert regular and caustics and density
    return {"prime":PRIME,"birational_forward_inverse_cases":regular,
            "exact_new_density_Jacobians":density,
            "old_caustics_resolved_with_nonzero_new_derivative":caustics,
            "both_original_prefix_parities_checked":True}


def bordered_hessians():
    mu,gamma=sp.symbols("mu gamma")
    records=[]
    for rank in range(4):
        B=sp.Matrix(rank,rank,lambda i,j:(i+3 if i==j else 1))
        w=sp.Matrix(sp.symbols(f"w0:{rank}"))
        H0=sp.zeros(rank+1)
        for i,j in product(range(rank),repeat=2):H0[i+1,j+1]=B[i,j]
        c=sp.Matrix([mu]+list(w))
        H=H0.row_join(c).col_join(c.T.row_join(sp.Matrix([[gamma]])))
        want=-mu**2*B.det()
        assert sp.expand(H.det()-want)==0
        records.append({"old_transverse_rank":rank,
                        "new_internal_dimension":rank+2,
                        "determinant":str(want),
                        "independent_of_gamma_and_transverse_mixed_terms":True})
    H,N=sp.symbols("H N",nonzero=True)
    assert sp.simplify((1/N)/H**2-1/(2*sp.pi*sp.I*H)).subs(H,2*sp.pi*sp.I/N)==0
    return records


def main():
    result={"status":"PASS","bordered_hessian_identities":bordered_hessians(),
            "universal_prefix_polarization":rational_polarization(),
            "Fourier_normalization":"N^-1 H_N^-2=(2pi*i*H_N)^-1",
            "scope":"Exact rational geometry and formal nondegenerate block. "
                    "No actual selected global cycle or off-root Fourier/Vandermonde equivalence."}
    output=Path(__file__).with_name("actual_fourier_polarized_normal_block_results.json")
    output.write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({"status":"PASS","bordered_hessians":4,
                      **result["universal_prefix_polarization"],"output":str(output)},indent=2))


if __name__=="__main__":main()
