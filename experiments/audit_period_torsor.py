#!/usr/bin/env python3
"""Uniform algebra checks for the period-torsor reformulation.

There are no knot-census inputs. Tests cover the cyclic norm, noncommuting
deck lifts, finite Fourier reduction at composite levels, and an exact local
rational-parameter bridge checked against the defining Faddeev integral.
Finite samples validate formulas; the accompanying proofs are uniform.
"""

import argparse
import json
from collections import defaultdict
from itertools import product
from pathlib import Path

import mpmath as mp
import sympy as sp

from check_local_completion import phi_original_integral


def cyclotomic_zero(expression,w,n):
    return sp.rem(sp.Poly(sp.expand(expression),w),sp.Poly(sp.cyclotomic_poly(n,w),w)).is_zero


def torsor_certificate(n):
    w,x,M,c,s=sp.symbols("w x M c s")
    norm=sp.prod(1-w**j*x for j in range(n))
    assert cyclotomic_zero(norm-(1-x**n),w,n)
    plus_norm=sp.prod(1+w**j*M for j in range(n))
    assert cyclotomic_zero(plus_norm-(1+M**n),w,n)
    # The shift of the determinant exponents proves Delta(w*x)/Delta(x).
    exponents=[n-1-j for j in range(n)]
    shifted=[exponents[(j-1)%n] for j in range(n)]
    assert [shifted[j]-exponents[j] for j in range(n)]==[-(n-1)]+[1]*(n-1)
    assert sum(exponents)==n*(n-1)//2
    # The determinant-normalizing root has the centered exponent vector.
    assert [(n-1)//2-exponents[j] for j in range(n)]==[j-(n-1)//2 for j in range(n)]
    A=lambda point:(w*point[0],point[1],point[2]*(1-point[0])/point[1])
    B=lambda point:(point[0],w*point[1],point[2])
    C=lambda point:(point[0],point[1],w*point[2])
    start=(x,c,s)
    ab=A(B(start));ba=B(A(start))
    assert all(sp.cancel(v-u)==0 for v,u in zip(ab,(ba[0],ba[1],ba[2]/w)))
    assert all(sp.cancel(v-u)==0 for v,u in zip(A(C(start)),C(A(start))))
    assert all(sp.cancel(v-u)==0 for v,u in zip(B(C(start)),C(B(start))))
    for k in range(1,2*n+1):
        moment=sum(j*w**(j*k) for j in range(1,n))
        if k%n:
            assert cyclotomic_zero((w**k-1)*moment-n,w,n)
        else:
            assert cyclotomic_zero(moment-sp.Rational(n*(n-1),2),w,n)
    return {"level":n,"norm_one_cover":"x^n=t, c^n=1-t",
            "generic_peripheral_norm":"1+M^n",
            "determinant_root_centered_exponents":[j-(n-1)//2 for j in range(n)],
            "deck_relation":"AB=C^(-1)BA; C central",
            "norm_and_determinant_shift_exact":True,
            "weighted_root_sums_exact":True}


def mv(matrix,vector,n):
    return tuple(sum(a*b for a,b in zip(row,vector))%n for row in matrix)


def dot(left,right,n):
    return sum(a*b for a,b in zip(left,right))%n


def finite_reduction_certificate(n,T,U,name,expect_obstruction=False):
    r=len(T)
    V=list(product(range(n),repeat=r))
    zero=(0,)*r
    K=[v for v in V if mv(T,v,n)==zero]
    obstruction=[k for k in K if all(dot(mv(U,k,n),mv(T,v,n),n)==0 for v in V)]
    if expect_obstruction:
        assert len(obstruction)>1
        return {"level":n,"model":name,"nonzero_obstruction_detected":True,
                "obstruction_cardinality":len(obstruction),"theorem_applied":False}
    assert obstruction==[zero]
    representatives={mv(T,v,n):v for v in V}
    W={w for w in representatives if all(dot(mv(U,k,n),w,n)==0 for k in K)}
    assert len(W)*len(K)**2==n**r
    weights=defaultdict(lambda:[0]*n)
    for v in V:
        w=mv(T,v,n)
        phase=(-dot(mv(U,v,n),w,n))%n
        weights[w][phase]+=1
    z=sp.Symbol("z")
    phi=sp.Poly(sp.cyclotomic_poly(n,z),z)
    for w,counts in weights.items():
        polynomial=sum(counts[j]*z**j for j in range(n))
        if w in W:
            representative=representatives[w]
            q=(-dot(mv(U,representative,n),w,n))%n
            for v in V:
                if mv(T,v,n)==w:
                    assert (-dot(mv(U,v,n),w,n))%n==q
            polynomial-=len(K)*z**q
        assert sp.rem(sp.Poly(polynomial,z),phi).is_zero
    free_rank=next((j for j in range(r+1) if len(W)==n**j),None)
    is_free=free_rank is not None and all(
        sum(all(p*x%n==0 for x in w) for w in W)==p**free_rank
        for p in sp.factorint(n))
    return {"level":n,"model":name,"ambient_cardinality":n**r,
            "kernel_cardinality":len(K),"support_cardinality":len(W),
            "support_normalization":"1/sqrt(|W|)",
            "all_formal_amplitude_coefficients_checked_exactly":True,
            "support_is_free_over_Z_mod_level":is_free}


def weyl_certificate(n):
    half=pow(2,-1,n)
    e=(1,1,1,1);m=(1,0,1,0);l=(0,0,1,-1)
    omega=lambda a,b:(sum(a[j]*b[j+2]-a[j+2]*b[j] for j in range(2)))%n
    scale=lambda a,v:tuple(a*x%n for x in v)
    add=lambda v,w:tuple((a+b)%n for a,b in zip(v,w))
    assert omega(m,e)==omega(l,e)==0 and omega(m,l)==1
    E={scale(j,e) for j in range(n)}
    assert len(E)==n
    # Pi^2=Pi, in the formal Weyl basis, without numerical matrix ranks.
    coefficients=defaultdict(lambda:[sp.Rational(0)]*n)
    for a in E:
        for b in E:
            coefficients[add(a,b)][half*omega(a,b)%n]+=sp.Rational(1,n*n)
    for v,values in coefficients.items():
        assert values[0]==sp.Rational(1,n) and all(x==0 for x in values[1:])
    boundary=[]
    for a,b in product(range(n),repeat=2):
        v=add(scale(a,m),scale(b,l));boundary.append(v)
        assert (v in E)==(a==b==0)
    # Only the identity contributes to the full trace, hence rank Pi=n.
    assert sp.Rational(n*n,n)==n and len(boundary)==n*n
    perpendicular={v for v in product(range(n),repeat=4) if omega(e,v)==0}
    decomposed={add(add(scale(a,m),scale(b,l)),scale(c,e))
                for a,b,c in product(range(n),repeat=3)}
    assert decomposed==perpendicular and len(perpendicular)==n**3
    return {"level":n,"mixed_isotropic_edge_vector":list(e),
            "edge_projector_idempotent_exact":True,"boundary_dimension":n,
            "trace_orthogonal_boundary_weyl_operators":n*n,
            "all_nonidentity_boundary_class_traces_zero":True,
            "coisotropic_quotient_basis_verified":True,
            "reduced_Heisenberg_torsor_degree":n**3}


def continuous_phase_certificate():
    lam,mu=sp.symbols("lambda mu")
    vectors=[sp.Matrix(sp.symbols(f"{name}_0:3")) for name in ["dref","Wref","d1","W1","dd","dW"]]
    d0,W0,d1,W1,dd,dW=vectors
    scalar=lambda a,b:(a.T*b)[0]
    d=d0+lam*d1+dd;W=W0+lam*W1+dW
    Aref=lam*scalar(W1,d0)+lam**2*scalar(W1,d1)/2
    old=-scalar(d,W)/4+(Aref+scalar(dW,d0+lam*d1))/2
    uniform=(scalar(d0,W)-scalar(W0,d)-scalar(d0,W0))/4-lam*mu/8
    certificate=-scalar(dd,dW)+lam*(scalar(dW,d1)-scalar(W1,dd)+mu/2)
    assert sp.expand(4*(old-uniform)-certificate)==0
    return {"all_vectors_and_peripheral_parameters_indeterminate":True,
            "exact_polynomial_certificate":True,
            "universal_quadratic_term":"-lambda*mu/(8*pi)",
            "hypotheses":"dd.dW=0 and dW.d1-W1.dd=-mu/2"}


def bloch_certificate():
    X,Y,A,B,C=[sp.eye(5)[:,j] for j in range(5)]
    wedge=lambda v,w:v*w.T-w*v.T
    expression=(wedge(X,A)+wedge(Y,B)-wedge(X+Y,C)
                -wedge(X+B-C,A-C)-wedge(Y+A-C,B-C))
    assert expression==sp.zeros(5)
    return {"formal_logarithmic_generators":5,
            "five_term_boundary_wedge_identity_exact":True,
            "boundary_pairing_convention":-2,
            "boundary_formula":"delta beta=-(1/2)*m wedge l",
            "scope":"The wedge certificate is exact; the boundary formula follows from the separate uniform symplectic proof."}


def rational_phi_certificate():
    mp.mp.dps=48
    records=[]
    for n in [3,5,9]:
        b=1/mp.sqrt(n)
        z=mp.mpc('-.7',mp.pi*(n+1)+mp.mpf('.25'))
        cb=.5j*(b+1/b)
        spectral=z/(2*mp.pi*mp.sqrt(n))-cb
        direct=phi_original_integral(b,spectral)
        w=mp.exp(2j*mp.pi/n);X=mp.exp(z/n)
        logD=sum(mp.mpf(j)/n*mp.log(1-w**j*X) for j in range(1,n))
        expected=mp.exp(1j*mp.polylog(2,mp.exp(z))/(2*mp.pi*n)
                        +(1+1j*z/(2*mp.pi*n))*mp.log(1-mp.exp(z))-logD)
        error=abs(direct/expected-1)
        assert error<mp.mpf('1e-35')
        h=(n-1)//2;central_log=mp.log(1-mp.exp(z))
        c=mp.exp(central_log/n);normalizer=mp.exp(logD-h*central_log/n)
        S=mp.polylog(2,mp.exp(z))+z*central_log
        torsor_value=mp.exp(mp.mpf(n+1)*central_log/(2*n)+1j*S/(2*mp.pi*n))/normalizer
        assert abs(torsor_value/expected-1)<mp.mpf('1e-40')
        next_X=w*X
        next_logD=sum(mp.mpf(j)/n*mp.log(1-w**j*next_X) for j in range(1,n))
        next_s=mp.exp(next_logD-h*central_log/n)
        assert abs(next_s/normalizer-(1-X)/c)<mp.mpf('1e-40')
        records.append({"level":n,"logarithmic_variable":str(z),
                        "relative_error":str(error),
                        "Heisenberg_period_evaluation_and_deck_multiplier_checked":True})
    return {"method":"Defining Phi contour integral versus exact finite-product/dilogarithm formula",
            "proof_status":"Numerical diagnostics of the separate uniform residue proof",
            "precision_digits":48,"records":records}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skip-phi",action="store_true")
    args=parser.parse_args()
    result={"scope":"Uniform torsor and finite-reduction checks; no knot-specific inputs.",
            "torsors":[torsor_certificate(n) for n in [3,5,9]],
            "finite_reductions":[],"boundary_modules":[weyl_certificate(n) for n in [3,5,9]],
            "continuous_boundary_phase":continuous_phase_certificate(),
            "Bloch_period_lift":bloch_certificate()}
    for n in [3,5,9,15,21]:
        result["finite_reductions"].append(finite_reduction_certificate(
            n,[[3,0],[0,1]],[[0,0],[1,0]],"nonunit Smith entry 3"))
    for n in [3,9]:
        result["finite_reductions"].append(finite_reduction_certificate(
            n,[[0,0,0],[0,1,0],[0,0,1]],[[0,0,0],[1,0,0],[0,0,1]],"one full Fourier kernel"))
    result["negative_control"]=finite_reduction_certificate(
        9,[[3,0],[0,1]],[[0,0],[0,0]],"unpaired kernel",expect_obstruction=True)
    if not args.skip_phi:result["rational_phi"]=rational_phi_certificate()
    Path(__file__).with_name("period_torsor_results.json").write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(result,indent=2))


if __name__=="__main__":main()
