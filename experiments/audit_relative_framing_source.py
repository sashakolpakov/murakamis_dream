#!/usr/bin/env python3
"""Relative meridian framing source, exact projector, and normal carry.

Checks the explicit relative contraction and its literal finite-color
realization. This is a boundary source model; it does not identify an
internal semiclassical pushforward or prove a volume estimate.
"""

import json
from pathlib import Path

import numpy as np
import sympy as s

from audit_finite_sum_annihilator import field,cut_matrix_dense
from audit_kashaev_ado_pointing import color_matrices


A,t,U=s.symbols('A t U')


def canonical(f,N,normal=False):
    relation=A**N-(U if normal else 1)
    return s.rem(s.Poly(s.expand(f),A),s.Poly(relation,A)).as_expr().expand()


def phi(f,N):return canonical(f,N).coeff(A,0)


def delta(h):return (s.diff(h,t),h.subs(t,0),h.subs(t,1))


def transgress(v):
    a,b0,b1=v
    return s.expand(s.integrate(a,(t,0,1))-b1+b0)


def inclusion(f):return (f,s.Integer(0),s.Integer(0))


def homotopy(v):
    a,b0,b1=v;L=transgress(v)
    return s.expand(b0+s.integrate(a-L,t)-s.integrate(a-L,t).subs(t,0))


def relative_complex():
    records=[]
    for N in range(2,13):
        h=sum((j+1)*(1+t+(j+2)*t*t+t**3)*A**j for j in range(N))
        dh=delta(h)
        assert transgress(dh)==0
        assert s.expand(homotopy(dh)-h)==0
        a=sum((j+2)*(1+(j+1)*t+2*t*t)*A**j for j in range(N))
        b0=sum((j*j+1)*A**j for j in range(N))
        b1=sum((2*j+3)*A**j for j in range(N))
        v=(a,b0,b1);L=transgress(v)
        contracted=delta(homotopy(v))
        assert all(s.expand(x-y)==0 for x,y in zip(contracted,(a-L,b0,b1)))
        assert transgress(inclusion(L))==L
        project=lambda v:tuple(phi(x,N) for x in v)
        assert all(s.expand(x-y)==0 for x,y in zip(project(delta(h)),delta(phi(h,N))))
        assert s.expand(phi(transgress(v),N)-transgress(project(v)))==0
        assert s.expand(phi(homotopy(v),N)-homotopy(project(v)))==0
        records.append({'level':N,'relative_deformation_retract_exact':True,
                        'source_projector_is_strict_cochain_map':True,
                        'source_commutes_with_contraction_and_transgression':True})
    return records


def finite_color_model():
    records=[]
    for N in range(2,15):
        p,generic,q=field(N);Q=q*q%p;x=-generic*pow(q,-1,p)%p
        invN=pow(N,-1,p)
        V=np.array([[pow(Q,a*j,p) for j in range(N)] for a in range(N)],dtype=np.int64)
        Vi=np.array([[pow(Q,-a*j,p)*invN%p for a in range(N)] for j in range(N)],dtype=np.int64)
        assert np.array_equal(V@Vi%p,np.eye(N,dtype=np.int64))
        mulA=np.zeros((N,N),dtype=np.int64)
        for j in range(N):mulA[(j+1)%N,j]=1
        ecoef=np.zeros((N,N),dtype=np.int64);ecoef[0,0]=1
        Scoef=np.diag([pow(Q,j,p) for j in range(N)])
        average=np.zeros((N,N),dtype=np.int64);power=np.eye(N,dtype=np.int64)
        for _ in range(N):average=(average+power)%p;power=power@Scoef%p
        assert np.array_equal(average*invN%p,ecoef)
        eeval=V@ecoef@Vi%p
        assert np.array_equal(eeval,np.full((N,N),invN,dtype=np.int64))
        gcoef=pow(x,1-N,p)*mulA.T%p
        invgcoef=pow(x,N-1,p)*mulA%p
        Dcoef=invgcoef@ecoef%p
        Deval=V@Dcoef@Vi%p
        expected=np.array([[pow(x,N-1,p)*pow(Q,a,p)*invN%p for _ in range(N)]
                           for a in range(N)],dtype=np.int64)
        assert np.array_equal(Deval,expected)
        assert not np.any(Dcoef@Dcoef%p)
        assert np.array_equal(gcoef@Dcoef%p,ecoef)
        assert np.array_equal(Dcoef@gcoef@Dcoef%p,Dcoef)
        assert np.trace(gcoef@Dcoef%p)%p==1
        C=np.array([[(i+1)*(j+2)+i*i+3*j for j in range(N)] for i in range(N)],dtype=np.int64)%p
        Ccoef=Vi@C@V%p
        source=int(Ccoef[0,0])
        marked=int(np.trace(gcoef@Dcoef@Ccoef%p)%p)
        assert marked==source
        records.append({'level':N,'prime':p,'literal_eval_basis_projector_and_defect':True,
                        'arbitrary_finite_matrix_cut_retained':True})
    return records


def normal_source_and_carry():
    records=[]
    for N in range(2,13):
        f=sum((j+1+U*U)*A**j for j in range(N))
        carried=canonical(A*f,N,normal=True)
        assert s.expand(A*f-carried-(N+U*U)*(A**N-U))==0
        assert s.expand(carried.coeff(A,0)-U*(N+U*U))==0
        multiplication=s.zeros(N)
        for j in range(N-1):multiplication[j+1,j]=1
        multiplication[0,N-1]=U
        matrix=sum(((j+1+U*U)*multiplication**j for j in range(N)),s.zeros(N))
        assert s.expand(s.trace(matrix)/N-(1+U*U))==0
        assert s.residue((1+U*U)/(U-1),U,1)==2
        eps=sum(A**j for j in range(N))/N
        assert canonical(eps*eps-eps,N)==0
        assert canonical((A-1)*eps,N)==0
        assert phi(eps,N)==s.Rational(1,N)
        # Canonical zero residue and naive unreduced representatives differ.
        assert phi(A**N,N)==1
        assert s.residue(A**N/A,A,0)==0
        assert s.residue(s.Integer(1)/A,A,0)==1
        # The original logarithmic root kernel gives the same constant term
        # at infinity for the degree<N representative.
        tilde=sum((j+1)*A**j for j in range(N))
        omega=A**(N-1)/(A**N-1)
        z=s.Symbol('z')
        assert -s.residue((tilde*omega).subs(A,1/z)/z**2,z,0)==-1
        records.append({'level':N,'full_U_trace_and_residue_exact':True,
                        'normal_carry_preserved':True,
                        'deleted_root_idempotent_source_weight':str(s.Rational(1,N)),
                        'canonical_representative_condition_essential':True})
    return records


def actual_cut_matrices():
    records=[]
    diagrams=[(2,[(0,1)]*3),(3,[(0,1),(1,-1)]*2)]
    for N in (2,3,4,5):
        p,generic,q=field(N);Q=q*q%p;x=-generic*pow(q,-1,p)%p
        invN=pow(N,-1,p)
        e=np.full((N,N),invN,dtype=np.int64)
        gg=np.diag([pow(x,1-N,p)*pow(Q,-a,p)%p for a in range(N)])
        D=np.array([[pow(x,N-1,p)*pow(Q,a,p)*invN%p for _ in range(N)]
                    for a in range(N)],dtype=np.int64)
        for strands,word in diagrams:
            C=cut_matrix_dense(N,p,color_matrices(N,p,q,x),strands,word)
            source=int(np.sum(C,dtype=np.int64)*invN%p)
            assert int(np.trace(e@C%p)%p)==source
            assert int(np.trace(gg@D@C%p)%p)==source
            records.append({'level':N,'strands':strands,'crossings':len(word),
                            'original_finite_cut_matches_relative_source':True})
    return records


def main():
    result={'relative_cochain_model':relative_complex(),
            'finite_color_projector':finite_color_model(),
            'normal_source_and_canonical_carry':normal_source_and_carry(),
            'original_cut_matrix_checks':actual_cut_matrices(),
            'scope':'Exact boundary relative realization; internal Gaussian comparison and selected volume norm remain unproved.'}
    output=Path(__file__).with_name('relative_framing_source_results.json')
    output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'relative_complex_cases':len(result['relative_cochain_model']),
                      'literal_finite_projectors':len(result['finite_color_projector']),
                      'normal_source_and_carry_cases':len(result['normal_source_and_canonical_carry']),
                      'actual_cut_matrices':len(result['original_cut_matrix_checks']),
                      'output':str(output)},indent=2))


if __name__=='__main__':main()
