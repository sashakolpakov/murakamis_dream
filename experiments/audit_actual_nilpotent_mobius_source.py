#!/usr/bin/env python3
"""Source Jacobian and actual-R obstruction to ordinary nilpotent Mobius."""
import json
import math
from pathlib import Path
import numpy as np
import sympy as sp

from audit_actual_hardy_cauchy_network import HardyNetwork
from audit_actual_two_cut_ports import balanced_data,coproduct


def truncated(f,X,N):
    return sp.series(f,X,0,N).removeO().expand()


def source_checks():
    X=sp.Symbol('X');rows=[]
    for N in range(2,11):
        d=N-1;a,c=sp.Integer(3),sp.Integer(2)
        f=a*X/(1+c*X);inverse=X/(a-c*X)
        assert truncated(f.subs(X,inverse),X,N)==X
        assert truncated(inverse.subs(X,f),X,N)==X
        J=a*(a-c*X)**(N-2)
        for n in range(N):
            direct=truncated(f**n,X,N).coeff(X,d)
            assert direct==sp.expand(X**n*J).coeff(X,d)
            invariant=truncated(a**(-d)*(1+c*X)**(N-2)*f**n,X,N).coeff(X,d)
            assert invariant==int(n==d)
            coherent=truncated((1+c*X)**d*(X/(1+c*X))**n,X,N).coeff(X,d)
            assert coherent==c**(d-n)
        L=sp.zeros(N);D=sp.zeros(N);Lcoh=sp.zeros(N)
        for j in range(N-1):
            L[j+1,j]=N-2-j;D[j+1,j]=-j;Lcoh[j+1,j]=d-j
        assert L**max(1,N-1)==sp.zeros(N)
        assert D**max(1,N-1)==sp.zeros(N)
        if N>=3:
            assert L**(N-2)!=sp.zeros(N) and D**(N-2)!=sp.zeros(N)
        assert Lcoh**N==sp.zeros(N) and Lcoh**(N-1)!=sp.zeros(N)
        assert sum(abs(int(sp.expand((1-X)**(N-2)).coeff(X,j))) for j in range(N))==2**(N-2)
        rows.append({'N':N,'original_source_Jacobian':str(J),
                     'source_preserving_and_unweighted_Jordan_blocks':[N-1,1],
                     'coherent_generator_nilpotent_index':N,
                     'unit_c_source_multiplier_l1':2**(N-2)})
    return rows


def original_operator_checks():
    rows=[]
    for N in range(2,14):
        H=HardyNetwork(N,1);p=H.p
        p0,eta,q,E,F,K,pivot,plus,minus=balanced_data(N)
        assert p==p0 and np.array_equal(plus,H.plus)
        assert not np.any(np.linalg.matrix_power(F,N)%p)
        # Modular powering avoids unbounded intermediary integer growth.
        def power(A,n):
            out=np.eye(len(A),dtype=np.int64)
            for _ in range(n):out=out@A%p
            return out
        assert not np.any(power(F,N)) and np.any(power(F,N-1))
        assert not np.any(power(E,N)) and np.any(power(E,N-1))
        _,Ft,_=coproduct(E,F,K,2,N,p)
        assert not np.any(power(Ft,N))
        if N>=3:
            D=np.zeros((N,N),dtype=np.int64)
            for j in range(1,N-1):D[j+1,j]=-j
            Dt=np.kron(D,np.eye(N,dtype=np.int64))+np.kron(np.eye(N,dtype=np.int64),D)
            C=(H.plus@Dt-Dt@H.plus)%p
            witness=int(C[2,N]);expected=H.kappa*(pow(H.x,-1,p)-pow(H.x,-2,p))%p
            assert witness==expected and witness
        else:witness=0
        rows.append({'N':N,'original_E_F_nilpotent_index':N,
                     'actual_F_coproduct_Nth_power_zero':True,
                     'full_Cartan_Mobius_crossing_defect':witness,
                     'defect_expected_nonzero':N>=3})
    return rows


def main():
    out={'exact_source_and_Jordan_checks':source_checks(),
         'original_quantum_operator_checks':original_operator_checks(),
         'scope':'ordinary common nilpotent Mobius does not implement actual framing Ward transport; '
                 'no obstruction to a separately proved coupled quantum source transformation'}
    Path(__file__).with_name('audit_actual_nilpotent_mobius_source_results.json').write_text(
        json.dumps(out,indent=2)+'\n')
    print('PASS nine exact source Jacobians/lifts, Jordan types and source norms; '
          '12 ORIGINAL Hopf modules and all-N crossing-defect witnesses')


if __name__=='__main__':main()
