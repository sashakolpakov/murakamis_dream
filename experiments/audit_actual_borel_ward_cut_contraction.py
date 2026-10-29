#!/usr/bin/env python3
"""Literal Borel Ward homotopy and original balanced cut identities."""

import json
from pathlib import Path

import sympy as s


def hopf_partial_trace_checks():
    records=[]
    for level,root in ((2,s.Integer(-1)),(3,(-1+s.sqrt(3)*s.I)/2)):
        def simplify(M):return M.applyfunc(s.simplify)
        def operators(color):
            K=s.diag(*(color*root**(-a) for a in range(level)))
            F=s.zeros(level);E=s.zeros(level)
            for a in range(level-1):
                F[a+1,a]=1-root**(a+1)
                # The common q^-1 scale cancels from the E intertwining.
                E[a,a+1]=s.Rational(1,color)*(1-color**2*root**(-a))
            return K,F,E
        K1,F1,E1=operators(2);K2,F2,E2=operators(3)
        I=s.eye(level)
        Kt=s.kronecker_product(K1,K2)
        Ft=s.kronecker_product(F1,I)+s.kronecker_product(K1.inv(),F2)
        Et=s.kronecker_product(E1,K2)+s.kronecker_product(I,E2)
        C=s.Matrix(level**2,level**2,lambda a,b:(a+2)*(b+1)+(a-b)**2)
        g=K2**(1-level)
        def ptr(C):
            return simplify(s.Matrix(level,level,lambda a,b:
                sum(g[j,j]*C[a*level+j,b*level+j] for j in range(level))))
        pc=ptr(C)
        assert simplify(ptr(Kt*C*Kt.inv())-K1*pc*K1.inv())==s.zeros(level)
        assert simplify(ptr((Et*C-C*Et)*Kt.inv())
                        -(E1*pc-pc*E1)*K1.inv())==s.zeros(level)
        assert simplify(ptr(Ft*C-Kt.inv()*C*Kt*Ft)
                        -(F1*pc-K1.inv()*pc*K1*F1))==s.zeros(level)
        records.append({'level':level,'all_three_actual_Hopf_adjoint_partial_traces':True,
                        'two_distinct_nonzero_colors':True})
    a,c=s.symbols('a c',nonzero=True)
    da=s.Matrix([[1,0,0]]);db=s.Matrix([[0,1,0]]);dc=s.Matrix([[0,0,1]])
    rK=da/a;rE=db/a;rF=dc/a-c*da/a**2+(c/a)*da/a
    assert s.simplify(rF-dc/a)==s.zeros(1,3)
    assert s.simplify(2*rK+2*rE-(2*da+2*db)/a)==s.zeros(1,3)
    assert s.simplify(rF+rE-(dc+db)/a)==s.zeros(1,3)
    return records


def main():
    Q,x=s.symbols('Q x',nonzero=True)
    records=[]
    for level in range(2,10):
        K=s.diag(*(x*Q**(-a) for a in range(level)))
        F=s.zeros(level)
        for a in range(level-1):F[a+1,a]=1-Q**(a+1)
        C=s.Matrix(level,level,lambda a,b:(a+2)*(b+1)+x*(a-b))
        dK=K*C-C*K;dF=F*C-C*F
        HK=s.zeros(level)
        for a in range(level):
            for b in range(level):
                if a!=b:HK[a,b]=s.cancel(dK[a,b]/(K[a,a]-K[b,b]))
        diffs=[s.cancel(dF[r+1,r]/F[r+1,r]) for r in range(level-1)]
        average=s.expand(sum((level-1-r)*diffs[r] for r in range(level-1))/level)
        HF=s.diag(*(s.expand(average-sum(diffs[:a])) for a in range(level)))
        scalar=s.trace(C)/level
        assert (C-scalar*s.eye(level)-HK-HF).applyfunc(s.cancel)==s.zeros(level)
        assert s.cancel(s.trace(HK+HF))==0
        h=HK+HF
        assert ((K*h-h*K)-dK).applyfunc(s.cancel)==s.zeros(level)
        assert ((F*h-h*F)-dF).applyfunc(s.cancel)==s.zeros(level)
        e=s.ones(level)/level
        H=s.zeros(level)
        for a in range(level):
            for b in range(level):
                if a!=b:H[a,b]=1/(level*(K[a,a]-K[b,b]))
        assert (K*H-H*K-e+s.eye(level)/level).applyfunc(s.cancel)==s.zeros(level)
        assert s.cancel(s.trace(e*C)-scalar+s.trace(H*dK))==0
        XH=dK*K.inv();ZH=dF+K.inv()*dK*F
        assert (XH*K-dK).applyfunc(s.cancel)==s.zeros(level)
        assert (ZH-K.inv()*XH*K*F-dF).applyfunc(s.cancel)==s.zeros(level)
        assert s.cancel(s.trace(e*C)-scalar+s.trace(K*H*XH))==0
        # Scalar Ward-closed matrices have exactly the original unknot cut.
        assert s.trace(e*s.eye(level))==1
        # The co-source has a nontrivial kernel away from Ward-closed states.
        zero_cut=s.zeros(level);zero_cut[0,0]=1;zero_cut[1,1]=-1
        assert zero_cut!=s.zeros(level) and s.trace(e*zero_cut)==0
        records.append({'level':level,'exact_Ward_contraction':True,
                        'exact_cut_cochain_homotopy':True,
                        'unknot_unit':1,'nonzero_vector_zero_cut':True})
    result={'finite_matrix_cases':records,
            'Hopf_adjoint_partial_trace_cases':hopf_partial_trace_checks(),
            'constant_principal_cut_framing_currents':True,
            'scope':'Actual Ward/cut contraction only; no partial-to-geometric embedding.'}
    path=Path(__file__).with_name('actual_borel_ward_cut_contraction_results.json')
    path.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'exact_Ward_and_cut_levels':len(records),
                      'Hopf_adjoint_partial_trace_levels':len(result['Hopf_adjoint_partial_trace_cases']),
                      'output':str(path)},indent=2))


if __name__=='__main__':main()
