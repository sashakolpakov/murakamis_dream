#!/usr/bin/env python3
"""Actual Cartan port currents, root cyclic source and whole carry guard."""

import json
from pathlib import Path

import numpy as np
import sympy as sp

from audit_finite_band_fourier_cap import field


def cyclic_shift(f):return f[1:]+f[:1]


def level_case(n):
    prime,Q=field(n)
    invn=pow(n,-1,prime);iq=pow((Q-1)%prime,-1,prime)
    def D(f):return [(a-b)*iq%prime for a,b in zip(cyclic_shift(f),f)]
    def h(f):
        mean=sum(f)*invn%prime
        g=[(a-mean)%prime for a in f]
        prefix=[0]
        for a in g[:-1]:prefix.append((prefix[-1]+a)%prime)
        center=sum(prefix)*invn%prime
        return [(Q-1)*(a-center)%prime for a in prefix]
    for j in range(n):
        f=[int(i==j) for i in range(n)]
        expected=[(a-invn)%prime for a in f]
        assert D(h(f))==expected and h(D(f))==expected
        assert sum(h(f))%prime==0
        # Lift every centered basis sequence to a literal one-sided
        # highest-input port tensor, then apply the actual Cartan row.
        coefficients={}
        for b in range(1,n):
            fourier=sum(expected[k]*pow(Q,k*b,prime) for k in range(n))%prime
            qinteger=(pow(Q,-b,prime)-1)*iq%prime
            coefficients[b]=fourier*pow(qinteger,-1,prime)%prime
        reconstructed=[invn*sum(coefficients[b]*(pow(Q,-b,prime)-1)*iq
                                  *pow(Q,-k*b,prime) for b in range(1,n))%prime
                       for k in range(n)]
        assert reconstructed==expected
    units=highest=0
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for d in range(n):
                    q=d-b
                    J=[invn*pow(Q,j*q,prime)%prime for j in range(n)]
                    factor=(pow(Q,q,prime)-1)*iq%prime
                    JW=[factor*x%prime for x in J]
                    assert D(J)==JW and sum(JW)%prime==0
                    # The whole second partial trace selects d=b, at which
                    # the literal port multiplier vanishes identically.
                    if d==b:assert factor==0
                    if a==0 and c+d==b:
                        assert q==-c and q<=0
                        highest+=1
                    units+=1
    unknot=[1]+[0]*(n-1)
    current=D(unknot)
    assert any(current) and sum(current)%prime==0
    return {"level":n,"prime":prime,"port_units":units,
            "highest_conserving_one_sided_units":highest,
            "cyclic_homotopy_basis_vectors":n,
            "literal_highest_port_primitives":n,
            "actual_highest_unknot_current_nonzero_source_zero":True}


def root_metric(n):
    Q=np.exp(2j*np.pi/n)
    U=np.array([[Q**(j*k)/np.sqrt(n) for k in range(n)] for j in range(n)])
    multipliers=np.array([0]+[(Q-1)/(Q**k-1) for k in range(1,n)])
    h=(U*multipliers[None,:])@U.conj().T
    S=np.zeros((n,n),dtype=complex)
    for j in range(n):S[j,(j+1)%n]=1
    D=(S-np.eye(n))/(Q-1);P=np.ones((n,n))/n
    assert np.linalg.norm(h@D-(np.eye(n)-P))<1e-10
    assert np.linalg.norm(D@h-(np.eye(n)-P))<1e-10
    norm=np.linalg.norm(h,2)
    assert norm<=1+1e-12
    g=np.arange(1,n+1,dtype=float)+1j*np.arange(n,dtype=float)**2
    distance=np.linalg.norm(P@g)
    assert abs(abs(sum(g))-np.sqrt(n)*distance)<1e-8
    return {"N":n,"cyclic_source_inverse_norm":float(norm),
            "exact_theorem_bound":1,"distance_to_zero_source_space_checked":True}


def whole_two_color_guard():
    Q=sp.symbols('Q',nonzero=True)
    B=sp.diag(1,Q);V=sp.Matrix([[1,1],[1,Q]])
    T=sp.Matrix([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]])
    bigB=sp.kronecker_product(sp.eye(2),B)
    W=(bigB*T*bigB.inv()-T)/(Q-1)
    ptr=lambda M:sp.Matrix(2,2,lambda c,a:sum(M[2*c+b,2*a+b] for b in range(2)))
    assert ptr(T)==sp.eye(2) and ptr(W)==sp.zeros(2)
    bigV=sp.kronecker_product(sp.eye(2),V)
    TV=bigV*T*bigV.inv();WV=bigV*W*bigV.inv()
    raw=lambda M:[sp.cancel(sum(M[2*c+j,j] for c in range(2))) for j in range(2)]
    J,JW=raw(TV),raw(WV)
    assert J==[1,0]
    assert all(sp.cancel(a-b)==0 for a,b in zip(JW,[1/(Q*(Q-1)),-1/(Q*(Q-1))]))
    uncorrected=[-1/(Q-1),1/(Q-1)]
    residual=[sp.cancel(a-b) for a,b in zip(JW,uncorrected)]
    assert all(sp.cancel(x.subs(Q,-1))==0 for x in residual)
    assert any(x for x in residual)
    assert sp.cancel(sum(JW))==0
    return {"actual_tensor":"two-cut unknot flip, highest first input",
            "whole_second_partial_trace_of_current":0,
            "whole_Fourier_current":list(map(str,JW)),
            "uncorrected_cyclic_difference_residual":list(map(str,residual)),
            "root_cyclic_identity_only_after_Q_minus_one":True}


def formal_geometric_current():
    v,H=sp.symbols('v H');A=sp.Function('A');B=sp.Function('B')
    numerator=A(v+H)-A(v)+H*(B(v+H)-B(v))
    coefficient=sp.series(numerator/(sp.exp(H)-1),H,0,2).removeO().doit().expand()
    assert sp.simplify(coefficient.coeff(H,0)-sp.diff(A(v),v))==0
    assert sp.simplify(coefficient.coeff(H,1)
                       -sp.diff(B(v),v)-sp.diff(A(v),v,2)/2+sp.diff(A(v),v)/2)==0
    eta=sp.symbols('eta')
    r=(2+3*eta)/(5+7*eta)
    leading=eta*sp.diff(r,eta)
    assert sp.cancel(eta*sp.diff(leading,eta))!=0
    return {"current_leading_amplitude":"partial_v A0",
            "next_amplitude":"partial_v A1 + partial_v^2 A0/2 - partial_v A0/2",
            "rational_Mobius_density_derivative_nonzero":True,
            "same_formal_regulator_action":True,
            "highest_A_equals_one_geometric_extension_not_assumed":True}


def main():
    levels=[level_case(n) for n in range(2,9)]
    result={"status":"PASS","root_port_and_source":levels,
            "root_norm_checks":[root_metric(n) for n in (2,3,4,5,8,16,32,64)],
            "whole_endpoint_guard":whole_two_color_guard(),
            "formal_geometric_current":formal_geometric_current(),
            "scope":"Actual zero-source Ward currents and their formal block; "
                    "no selected geometric survival or actual exponential norm claim."}
    output=Path(__file__).with_name('zero_source_fourier_current_results.json')
    output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({"status":"PASS","levels":len(levels),
                      "port_units":sum(x['port_units'] for x in levels),
                      "highest_one_sided_units":sum(x['highest_conserving_one_sided_units'] for x in levels),
                      "cyclic_homotopy_basis_vectors":sum(x['cyclic_homotopy_basis_vectors'] for x in levels),
                      "root_norm_levels":8,"whole_actual_two_color_guard":True,
                      "output":str(output)},indent=2))


if __name__=='__main__':main()
