#!/usr/bin/env python3
"""Independent exact sewing, balancing, and ORIGINAL source-pole audit."""

import json
from pathlib import Path

import numpy as np
import sympy as S

from audit_finite_sum_annihilator import field


def fiber_cases():
    count = overlap = 0
    for N in range(2,19):
        p, _, q = field(N)
        Q = q*q % p
        cycle = np.zeros((N,N),dtype=np.int64)
        for n in range(N):cycle[(n+1)%N,n] = 1
        for a in (-q % p, -q*pow(Q,-1,p) % p):
            for t in (2,3):
                z = a*pow(t,-1,p) % p
                if pow(z,N,p) == 1:continue
                RA, power = np.zeros_like(cycle),np.eye(N,dtype=np.int64)
                for n in range(N):
                    RA = (RA+pow(z,n,p)*power) % p
                    power = cycle@power % p
                RA = RA*pow(t*(1-pow(z,N,p)),-1,p) % p
                for h in range(1,N+1):
                    J = cycle.copy()
                    J[0,N-1] = 0
                    J[h%N,h-1] = 0
                    RT,power = np.zeros_like(cycle),np.eye(N,dtype=np.int64)
                    for n in range(N):
                        RT = (RT+pow(z,n,p)*power) % p
                        power = J@power % p
                    assert not power.any()
                    RT = RT*pow(t,-1,p) % p
                    U = np.zeros((N,2),dtype=np.int64)
                    U[0,0]=1;U[h%N,1]=1
                    C = np.array([[1,-pow(z,N-h,p)],[-pow(z,h,p),1]],dtype=np.int64)%p
                    sewn = (RA-RA@U@C@U.T@(a*cycle)%p@RA)%p
                    assert np.array_equal(sewn,RT)
                    if h==N:
                        expected=np.zeros_like(cycle);expected[0,0]=(1-pow(z,N,p))%p
                        assert np.array_equal(U@C@U.T%p,expected)
                        overlap+=1
                    count+=1
    return count,overlap


def balancing_cases():
    count=0
    for N in range(2,19):
        for h in range(1,N+1):
            for ss in (.001,.1,1.,5.):
                r=np.exp(ss/N)
                # The cut phase has z^N=(-1)^(N+1) r^-N.
                z=np.exp(1j*np.pi*(N+1)/N)/r
                ell=1j*np.pi*(N+1)/N-np.log(r)
                D=np.diag([1,np.exp((h-N/2)*ell)])
                C=np.array([[1,-z**(N-h)],[-z**h,1]],complex)
                balanced=np.linalg.inv(D)@C@D
                w=np.exp(N*ell/2)
                assert np.max(np.abs(balanced-np.array([[1,-w],[-w,1]])))<1e-10
                herm=(balanced+balanced.conj().T)/2
                values=np.linalg.eigvalsh(herm)
                if N%2:assert values[0]>0
                else:assert np.max(np.abs(herm-np.eye(2)))<1e-10
                assert np.linalg.cond(D)<=np.exp(ss/2)*(1+1e-10)
                count+=1
    return count


def actual_source_witness():
    t=S.symbols('t');i=S.I;a=i
    cyc=S.Matrix([[0,1],[1,0]])
    up=S.Matrix([[0,0],[1,0]]);down=up.T
    F=S.diag(1,2)
    F1=S.kronecker_product(F,S.eye(2));F2=S.kronecker_product(S.eye(2),F)
    C=F2*(S.eye(4)-i*S.kronecker_product(down,up)/2)*F1*F2.inv()
    A=a*S.kronecker_product(cyc,cyc)
    RA=(t*S.eye(4)-A).inv()
    V0,V1=S.zeros(4,2),S.zeros(4,2)
    for k in range(2):V0[k,k]=1;V1[((k+1)%2)*2+1,k]=1
    cross=(RA*V0*S.diag(a/t,1)*V1.T*A*RA
           +RA*V1*S.diag(a/t,(a/t)**2)*V0.T*A*RA)
    def phi(W):
        pivot=(-i,i)
        return S.simplify(sum(pivot[k]*W[c*2+k,b*2+k]
                             for b in range(2) for c in range(2) for k in range(2))/2)
    actual=S.factor(phi(C*(t*S.eye(4)-a*S.kronecker_product(up,down)).inv()*C.inv()))
    sewn=S.factor(phi(C*cross*C.inv()))
    assert S.simplify(actual-2*i/t**2)==0
    assert S.simplify(sewn+2*i*(t-1)*(t+1)/(t*t*(t*t+1)**2))==0
    for pole in (i,-i):assert S.simplify(S.limit((t-pole)**2*sewn,t,pole)-i)==0
    f=(1+t)**(-S.Rational(1,2))
    assert S.residue(f*actual,t,0)==-i
    assert S.residue(f*sewn,t,0)==-i
    residues=[]
    for pole, expected in ((i,(-9-i)/(4*S.sqrt(1+i))),
                           (-i,(9-i)/(4*S.sqrt(1-i)))):
        b2=S.limit((t-pole)**2*sewn,t,pole)
        b1=S.limit(S.diff(S.cancel((t-pole)**2*sewn),t),t,pole)
        residue=S.simplify(f.subs(t,pole)*b1+S.diff(f,t).subs(t,pole)*b2)
        assert S.simplify(residue-expected)==0
        residues.append(str(expected))
    return {"N":2,"M":1,"actual_source_resolvent":str(actual),
            "sewn_source_resolvent":str(sewn),"both_cyclic_double_pole_coefficients":"I",
            "both_original_small_circle_periods":"-I",
            "retained_unbranched_pole_residues":residues,
            "old_cut_without_added_poles_has_opposite_imaginary_sign":True}


def main():
    count,overlap=fiber_cases()
    result={"status":"PASS","exact_fiber_cases":count,"coincident_wall_cases":overlap,
            "scaled_balancing_cases":balancing_cases(),"actual_source_poles":actual_source_witness(),
            "scope":"Exact original small-circle sewing; cyclic poles and source corrections must remain in cut transport."}
    Path(__file__).with_name('two_head_cyclic_sewing_independent_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))


if __name__=='__main__':main()
