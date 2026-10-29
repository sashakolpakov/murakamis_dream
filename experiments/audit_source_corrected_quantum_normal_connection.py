"""Actual factorial lift, central obstructions and Jordan exceptions.

Exact rational identities and finite-field root tests supplement the
characteristic-zero proof. No knot semisimplicity or volume law is tested.
"""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

from audit_first_quantum_normal_connection import field, assert_zero, modpoly


Q,Y,U,eps=sp.symbols('Q Y U eps')


def actual_factorial_source():
    records=[]
    central=[1+U, 1+(U-1)**2, (U+1/U)/2]
    for N in range(2,8):
        p,z=field(N)
        G=sp.prod(1-Q**j*Y for j in range(N))
        # Literal denominator-cleared SAME whole source equation.
        residual=(1-Y)*G.subs(Y,Q*Y)-(1-Q**N*Y)*G
        assert sp.cancel(residual)==0
        F=1-U
        corrected=lambda f:sp.cancel(U*sp.diff(f,U)+U/(1-U)*f)
        assert corrected(F)==0
        for h in central:
            candidate=h.subs(U,Y**N)*G
            defect=(1-Y)*candidate.subs(Y,Q*Y)-(1-Q**N*Y)*candidate
            first=sp.together(z*sp.diff(defect,Q).subs(Q,z))
            expected=((1-Y)*N*U*sp.diff(h,U)*F).subs(U,Y**N)
            assert_zero(first-expected,p)
            obstruction=corrected(h*F)
            assert sp.cancel(obstruction-U*sp.diff(h,U)*F)==0
            assert obstruction!=0
            assert modpoly(sp.together(first).as_numer_denom()[0],p)!=0
            records.append({'N':N,'central_multiplier':str(h),
                            'same_whole_factorial_source_detects_nonconstant_multiplier':True})
    return records


def jordan_exception():
    records=[]
    f=1+2*U+3*U**2
    A=sp.Matrix([[0,1],[-1,2]])
    J=A-sp.eye(2)
    assert J*J==sp.zeros(2)
    v=sp.Matrix([1,1])
    for N in range(2,9):
        Z=(1+eps)**N
        # Literal central form of (S-1)(S-Z); it has no first
        # normal constraint, and the second one keeps two solutions.
        defect=sp.expand(f.subs(U,Z*Z*U)-(1+Z)*f.subs(U,Z*U)+Z*f)
        assert sp.diff(defect,eps).subs(eps,0)==0
        second=sp.diff(defect,eps,2).subs(eps,0)/2
        DU=lambda x:U*sp.diff(x,U)
        assert sp.expand(second-N*N*(DU(DU(f))-DU(f)))==0
        assert second!=0
        for linear in (1+U,3-U):
            full=sp.expand(linear.subs(U,Z*Z*U)-(1+Z)*linear.subs(U,Z*U)+Z*linear)
            assert full==0
        L0=A**(-N)-sp.eye(2)
        assert L0.rank()==1 and L0*v==sp.zeros(2,1)
        assert L0.row_join(v).rank()==L0.rank()
        ratio=(3-U)/(1+U)
        assert ratio.subs(U,1)==1 and sp.diff(ratio,U)!=0
        records.append({'N':N,'kernel_to_cokernel_symbol_on_selected_line':0,
                        'first_normal_constraint':0,'second_normal_operator':'N^2 D_U(D_U-1)',
                        'nonconstant_ratio_of_exact_same_operator_lifts':str(ratio)})
    return records


def hidden_order_reduction():
    records=[]
    S=sp.symbols('S')
    for m in (2,4,7):
        quotient,remainder=sp.div(S**m,S-1,S)
        assert remainder==1
        assert sp.expand(S**m-quotient*(S-1)-remainder)==0
        for N in range(2,7):
            p,z=field(N)
            G=Y**(-N)
            # This polynomial preoperator has root order1 but full
            # orderm: S-1+(Z-1)S^m. Its first-order lift and
            # source-corrected rank-one connection are both exact.
            defect=G.subs(Y,Q*Y)-G+(Q**N-1)*G.subs(Y,Q**m*Y)
            first=z*sp.diff(defect,Q).subs(Q,z)
            assert_zero(first,p)
            F=1/U
            assert sp.cancel(U*sp.diff(F,U)+F)==0
            records.append({'N':N,'literal_full_order':m,'root_effective_order':1,
                            'source_corrected_connection':'D_U+1',
                            'first_order_lift_of_Y^-N':True})
    return records


def main():
    result={'actual_factorial_central_source':actual_factorial_source(),
            'essential_Jordan_exception':jordan_exception(),
            'hidden_order_effective_companion':hidden_order_reduction(),
            'scope':'specified whole preoperator and source rule; actual-knot nonzero symbol not assumed'}
    target=Path(__file__).with_name('source_corrected_quantum_normal_connection_results.json')
    target.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'pass','factorial_cases':len(result['actual_factorial_central_source']),
                      'Jordan_cases':len(result['essential_Jordan_exception']),
                      'hidden_order_cases':len(result['hidden_order_effective_companion']),
                      'results':str(target)},indent=2))


if __name__=='__main__':
    main()
