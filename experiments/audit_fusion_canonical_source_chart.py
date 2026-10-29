#!/usr/bin/env python3
"""Actual fusion canonical chart, Euler orientation and retained source wall.

The rational chart is checked independently of any assertion of global
semiclassical convergence or geometric-period selection.
"""

import json
from pathlib import Path

import numpy as np
import sympy as sp

from audit_actual_borel_regular_fusion import fusion, inv, physical_cap, right_regular
from audit_actual_fusion_right_euler_clock import factorial_kernel
from audit_actual_two_cut_ports import balanced_data


def symbolic_chart():
    A, J, pa, pj, x = sp.symbols('A J pa pj x', nonzero=True)
    z = x*pj/pa
    K = 1-(1-A)*(1-J)/z
    U, V, pu, pv = A/K, J*K, (1-A)*pa, pj*(1-J*K)/(1-J)
    coords, original = [U, V, pu, pv], [A, J, pa, pj]
    Ki = 1-pu*(1-V)/(x*pv)
    recovered = [U*Ki, V/Ki, pu/(1-U*Ki), pv*(1-V/Ki)/(1-V)]
    assert all(sp.cancel(g-f) == 0 for g, f in zip(recovered, original))

    def bracket(f, g):
        return sp.cancel(A*pa*(sp.diff(f,A)*sp.diff(g,pa)-sp.diff(f,pa)*sp.diff(g,A))
                         +J*pj*(sp.diff(f,J)*sp.diff(g,pj)-sp.diff(f,pj)*sp.diff(g,J)))

    expected = sp.Matrix([[0,0,U*pu,0], [0,0,0,V*pv],
                          [-U*pu,0,0,0], [0,-V*pv,0,0]])
    for i in range(4):
        for j in range(i+1, 4):
            assert sp.cancel(bracket(coords[i],coords[j])-expected[i,j]) == 0

    delta = sp.symbols('delta')
    zz = 1-delta
    Dplus = A-A*J*delta+(J-1)*delta**2
    Dminus = J-A*J*delta+(A-1)*delta**2
    # Actual new-to-physical basis C R_u^{-1}, followed by opposite basis.
    assert sp.limit(A*zz/Dplus, delta, 0) == 1
    assert sp.limit(J*Dplus/zz, delta, 0) == A*J
    assert sp.limit((A*zz*delta**2/Dminus)/delta**2, delta, 0) == A/J
    assert sp.limit((J*Dminus/(zz*delta**2))*delta**2, delta, 0) == J**2
    return {'birational_inverse': True, 'six_log_Poisson_brackets': True,
            'actual_Euler_basis_U_limit': 1,
            'opposite_Euler_basis_U_valuation': 2}


def kernel_case(N, p, Q, root):
    x = 3
    C = factorial_kernel(N, p, Q, x)
    I = np.eye(N*N, dtype=np.int64)
    S = np.zeros((N,N), dtype=np.int64)
    for a in range(N-1):
        S[a+1,a] = 1
    Sa = Su = np.kron(S,np.eye(N,dtype=np.int64))
    Da = np.diag([pow(Q,a,p) for a in range(N) for _ in range(N)])
    Dj = np.diag([pow(Q,j,p) for _ in range(N) for j in range(N)])
    P0 = np.diag([int(a == 0) for a in range(N) for _ in range(N)])
    Ptop = np.diag([int(a == N-1) for a in range(N) for _ in range(N)])
    shift_j = np.kron(np.eye(N,dtype=np.int64),S)
    Fj = shift_j@(I-Q*Dj) % p
    Fv = Fj.copy()
    bottom = P0@C@Sa % p
    normal = (1-pow(Q,N,p))*Su@C@Ptop % p
    assert np.array_equal((C@Sa-Su@C@(I-Q*Da))%p,(bottom-normal)%p)
    assert np.array_equal(C@Fj%p,Fv@C%p)
    assert bottom.any()
    if root:
        assert not normal.any()
    else:
        assert normal.any()
    return {'N':N,'field':p,'root':root,'bottom_wall_nonzero':True,
            'top_normal_wall_nonzero':bool(normal.any())}


def actual_euler_case(N):
    p,eta,q,_,F,K,_,plus,minus = balanced_data(N)
    Q, x = q*q%p, int(K[0,0])
    C,Ci,phi,_,ftot,Ks,_ = fusion(N,p,Q,[x,x],[0,0])
    assert not phi
    size=N*N
    I=np.eye(size,dtype=np.int64)
    f=np.zeros(size,dtype=np.int64); f[N:2*N]=1
    Rf=right_regular(f,N,0,p)
    z=x*Rf%p
    fac=[1]
    for a in range(1,N):
        fac.append(fac[-1]*(1-pow(Q,a,p))%p)
    Tu,Tv,power=I.copy(),I.copy(),I.copy()
    for a in range(1,N):
        power=power@z%p
        Tu=(Tu+power*pow(fac[a],-1,p))%p
        Tv=(Tv+power*(pow(-1,a,p)*pow(Q,a*(a-1)//2,p)*pow(fac[a],-1,p)%p))%p
    assert np.array_equal(Tu@Tv%p,I)
    A=np.diag([pow(Q,a,p) for a in range(N) for _ in range(N)])
    J=np.diag([pow(Q,j,p) for _ in range(N) for j in range(N)])
    delta=(I-z)%p
    delta_q=(I-pow(Q,-1,p)*z)%p
    assert np.array_equal(Tu@A@Tv%p,inv(delta,p)@A%p)
    assert np.array_equal(Tu@J@Tv%p,delta_q@J%p)
    assert np.array_equal(Tv@A@Tu%p,delta@A%p)
    assert np.array_equal(Tv@J@Tu%p,inv(delta_q,p)@J%p)
    # This is the basis dictated by b=u^{-1} a u in the RIGHT algebra.
    T,Ti=C@Tv%p,Tu@Ci%p
    P=np.zeros((N,N),dtype=np.int64);P[0,:]=1
    g=np.diag([pow(int(K[a,a]),1-N,p) for a in range(N)])
    Dphys=np.kron(P,g)%p
    Dnew=Ti@Dphys@T%p
    boundary=pow(x,-1,p)*np.kron(np.diag([1]+[0]*(N-1)),F)%p
    witnesses=[]
    for W in (plus,minus,plus@plus@plus%p):
        rel=Ci@W@C%p
        dressed=Tu@rel@Tv%p
        assert np.array_equal(Ti@W@T%p,dressed)
        original=physical_cap(W,Ks,N,p)
        assert int(np.trace(Dphys@W))%p == original
        assert int(np.trace(Dnew@dressed))%p == original
        value=physical_cap(W@boundary%p,Ks,N,p)
        assert value
        witnesses.append(int(value))
    return {'N':N,'field':p,'exact_Euler_clock_and_source_orientation':True,
            'original_signed_word_bottom_wall_periods':witnesses}


def main():
    symbolic=symbolic_chart()
    kernels=[]
    eulers=[]
    for N in range(2,8):
        p,_,q,*_=balanced_data(N)
        kernels.append(kernel_case(N,p,q*q%p,True))
        kernels.append(kernel_case(N,1009,2,False))
        eulers.append(actual_euler_case(N))
    result={'status':'PASS','symbolic_chart':symbolic,'kernel_cases':kernels,
            'actual_Euler_source_cases':eulers,
            'scope':'Local rational symplectic fusion graph, exact finite wall/source relations and Euler basis orientation. No global semiclassical or geometric-period selection claim.'}
    Path(__file__).with_name('fusion_canonical_source_chart_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'PASS','kernel_cases':len(kernels),
                      'Euler_source_cases':len(eulers),'symbolic_chart':symbolic}))


if __name__=='__main__':
    main()
