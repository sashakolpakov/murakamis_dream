#!/usr/bin/env python3
"""Actual generic Casimir, original polynomial, and four retained q jets."""
import json
import math
from pathlib import Path
from audit_actual_q_hahn_physical_generic_jet_bound import Jet, matrix, forward
from audit_high_color_first_normal_r_degree import root_field


def apply(diag,up,low,v):
    out=[]
    for u,x in enumerate(v):
        value=diag[u]*x
        if u:value+=low[u-1]*v[u-1]
        if u+1<len(v):value+=up[u]*v[u+1]
        out.append(value)
    return out


def source_polynomial(N,q,a,diag,up,low,v,z):
    d=N-1;delta=q-q**-1
    unit=lambda n:(q**n-q**(-n))/delta
    term=v[:];out=v[:];scalar_term=Jet(1);scalar=Jet(1);lead=Jet(1)
    for k in range(a):
        lam=q**(2*k+1)+q**(-2*k-1)
        coef=-unit(a-k)*unit(a+k+1)/(unit(k+1)**2*unit(d-k)*unit(d+k+2)*delta**2)
        jterm=apply(diag,up,low,term)
        term=[coef*(new-lam*old) for new,old in zip(jterm,term)]
        out=[old+new for old,new in zip(out,term)]
        scalar_term*=coef*(z-lam);scalar+=scalar_term;lead*=coef
    return out,scalar,lead


def audit():
    counts=dict(actual_forward_backward_continuants=0,
                original_polynomial_safe_row_four_jets=0,
                sharp_first_boundary_defects=0,endpoint_residual_determinants=0,
                retained_jet_coefficients=0)
    for N in range(3,11):
        p,eta=root_field(N);Jet.p=p;Jet.order=4;q0=eta*eta%p
        q=Jet([q0*pow(math.factorial(k),-1,p)%p for k in range(4)])
        for t in range(N):
            D,U,L=matrix(N,q,t)
            roots={(pow(q0,2*m+1,p)+pow(q0,-2*m-1,p))%p for m in range(t+1)}
            value=3
            while value%p in roots:value+=1
            z=Jet(value)
            for reverse in (False,True):
                diag,up,low=(D,U,L) if not reverse else (D[::-1],L[::-1],U[::-1])
                C=forward(diag,up,low,z)
                residual=[v-z*c for v,c in zip(apply(diag,up,low,C),C)]
                assert all(v==0 for v in residual[:-1])
                assert residual[-1].c[0]!=0
                chi_prev=Jet(1);chi=(z-diag[0]);prod=Jet(1)
                for r in range(t):
                    nxt=(z-diag[r+1])*chi-low[r]*up[r]*chi_prev
                    chi_prev,chi=chi,nxt;prod*=up[r]
                assert residual[-1]==-chi/prod
                counts['actual_forward_backward_continuants']+=1
                counts['endpoint_residual_determinants']+=1
                for a in range((N-1)//2+1):
                    out,scalar,lead=source_polynomial(N,q,a,diag,up,low,C,z)
                    defect=[v-scalar*c for v,c in zip(out,C)]
                    for u in range(max(0,t-a+1)):
                        assert defect[u]==0
                        counts['original_polynomial_safe_row_four_jets']+=1
                        counts['retained_jet_coefficients']+=4
                    if a and t>=a-1:
                        first=t-a+1;pred=residual[-1]*lead
                        for r in range(first,t):pred*=up[r]
                        assert defect[first]==pred and pred.c[0]!=0
                        counts['sharp_first_boundary_defects']+=1
    return counts


def main():
    result=dict(status='PASS',checks=audit(),scope='Exact actual generic four-jets and polynomial action windows; no coherent environment or complex magnetic continuation assumed.')
    Path(__file__).with_name('actual_matching_edge_polynomial_finite_propagation_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
