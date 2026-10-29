#!/usr/bin/env python3
"""Retained physical terminal phase: exact Ward defects and effective coupon."""

import json
from pathlib import Path

import mpmath as mp
import numpy as np
import sympy as s

from audit_actual_two_cut_ports import balanced_data, coproduct


def field_case(N):
    prime,eta,q,E,F,K,pivot,Rp,Rm=balanced_data(N)
    Q,d,x=q*q % prime,N-1,int(K[0,0])
    rho=(q-pow(q,-1,prime)) % prime
    Ec=rho*rho*E % prime
    E2,F2,K2=coproduct(Ec,F,K,2,N,prime)
    Et,Ft,Kt=coproduct(Ec,F,K,3,N,prime)
    I=np.eye(N,dtype=np.int64)
    Ki=np.diag([pow(int(z),-1,prime) for z in np.diag(K)])
    AF=np.kron(Ki,np.kron(F,I)) % prime
    BE=np.kron(I,np.kron(Ec,K)) % prime
    fac=[1]
    for j in range(1,N):fac.append(fac[-1]*(1-pow(Q,j,prime)) % prime)
    ids=[u*N+d-u for u in range(N)]
    high=[i*N for i in ids]
    seed=np.zeros((N*N,N),dtype=np.int64);seed[ids,np.arange(N)]=1
    H=np.zeros((N**3,N),dtype=np.int64);power=seed.copy()
    for c in range(N):
        H[c::N,:]=pow(-x*Q,c,prime)*pow(fac[c],-1,prime)*power % prime
        power=E2@power % prime
    D=H.copy()
    for _ in range(d):D=Ft@D % prime
    D=D*pow(fac[d],-1,prime) % prime
    xi=pow(-1,d,prime)*N % prime
    raised=D.copy()
    for _ in range(d):raised=Et@raised % prime
    assert np.array_equal(raised,xi*H % prime)
    assert not np.any(Ft@D % prime)
    cap=np.zeros(N**3,dtype=np.int64)
    ell=np.array([pow(x,-u,prime)*pow(Q,-u,prime)*pow(N,-1,prime) % prime
                  for u in range(N)],dtype=np.int64)
    cap[[i*N+d for i in ids]]=ell
    Uphys=np.kron(I,Rp@Rp % prime)
    Ured=(Uphys@H % prime)[high,:]
    assert np.array_equal(Uphys@D % prime,D@Ured % prime)
    coupons=[]
    for n in range(N):
        mask=np.array([int((j//N)%N==n) for j in range(N**3)],dtype=np.int64)
        z=mask[:,None]*D % prime
        for _ in range(d):z=Et@z % prime
        Mn=z[high,:]*pow(xi,-1,prime) % prime
        coupons.append(Mn)
        direct=(cap@Uphys % prime)*mask % prime@D % prime
        assert np.array_equal(direct,ell@Ured % prime@Mn % prime)
    assert np.array_equal(sum(coupons)%prime,np.eye(N,dtype=np.int64))
    records=0
    for t in [1,2,pow(Q,1,prime)]:
        diagonal=np.array([pow(t,(j//N)%N,prime) for j in range(N**3)])
        C=np.diag(diagonal)
        assert np.array_equal((Ft@C-C@Ft)%prime,(1-t)*AF@C % prime)
        assert np.array_equal((Et@C-C@Et)%prime,(1-pow(t,-1,prime))*BE@C % prime)
        assert not np.any((Kt@C-C@Kt)%prime)
        M=sum((pow(t,n,prime)*coupons[n] for n in range(N)),np.zeros((N,N),dtype=np.int64)) % prime
        z=diagonal[:,None]*D % prime
        for _ in range(d):z=Et@z % prime
        assert np.array_equal(M,z[high,:]*pow(xi,-1,prime)%prime)
        direct=cap@Uphys % prime@C % prime@D % prime
        assert np.array_equal(direct,ell@Ured % prime@M % prime)
        cup=np.array([N*pow(x,u-d,prime) % prime for u in range(N)],dtype=np.int64)
        if t!=1:assert np.any(Ft@C % prime@D % prime@cup % prime)
        records+=1
    return {'N':N,'all_input_packet_effective_coupons':N,'retained_phases':records,
            'literal_coproduct_and_original_terminal_Cartan':True}


def exact_two_level_coupon():
    q=s.I;Q=-1;x=s.I;I=s.eye(2)
    E=s.Matrix([[0,-2],[0,0]]);F=s.Matrix([[0,0],[2,0]]);K=s.diag(x,-x)
    Et=s.kronecker_product(E,K,K)+s.kronecker_product(I,E,K)+s.kronecker_product(I,I,E)
    Ft=s.kronecker_product(F,I,I)+s.kronecker_product(K.inv(),F,I)+s.kronecker_product(K.inv(),K.inv(),F)
    E2=s.kronecker_product(E,K)+s.kronecker_product(I,E)
    seed=s.zeros(4,2);seed[1,0]=seed[2,1]=1
    H=s.zeros(8,2)
    for a in range(4):
        for j in range(2):H[2*a,j]=seed[a,j];H[2*a+1,j]=s.I*(E2*seed)[a,j]/2
    D=Ft*H/2;t=s.symbols('t')
    C=s.diag(*[t**((j//2)%2) for j in range(8)])
    M=s.simplify(-(Et*C*D)[[2,4],:]/2)
    assert M==s.Matrix([[t,0],[s.I*(t-1),2-t]])
    M0=M.subs(t,0)
    assert M0*M0!=M0 and 3 in M.subs(t,-1).eigenvals()
    return str(M)


def source_norm(N):
    Q=mp.exp(2*mp.pi*mp.j/N)
    t=mp.exp(mp.j*mp.mpf('.37'))
    squared=abs(1-t)**2*N*N*mp.fsum(abs(1-Q**(-u))**2 for u in range(N))
    assert abs(squared/(N**3)-2*abs(1-t)**2)<mp.mpf('1e-65')
    return {'N':N,'relative_lowest_Ward_defect':mp.nstr(mp.sqrt(squared/N**3),18)}


if __name__=='__main__':
    mp.mp.dps=85
    result={'status':'PASS','all_exterior_physical_Ward_and_completion':[field_case(N) for N in range(2,8)],
            'exact_N2_effective_coupon':exact_two_level_coupon(),
            'macroscopic_actual_source_norm':[source_norm(N) for N in [2,3,5,8,17,32,64,129]],
            'scope':'Extra Cartan coupon and exact projected completion; no meridian identification or knot-volume bound.'}
    Path(__file__).with_name('actual_terminal_phase_coupon_ward_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS 6 full physical Ward/terminal-completion levels; exact N2 coupon; 8 uniform source norm checks')
