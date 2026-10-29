"""Exact source/word checks for the compact coherent period construction."""

from __future__ import annotations

from fractions import Fraction as F
from math import comb, factorial, prod
from pathlib import Path
import json

import mpmath as mp
import sympy as sp


def multiply(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(a)))
             for j in range(len(a))] for i in range(len(a))]


def subtract(a, b):
    return [[x-y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def symbol(a, w, z):
    n = len(a)-1
    return sum(w**i * a[i][j] * comb(n, j) * z**j
               for i in range(n+1) for j in range(n+1)) / (1+w*z)**n


def centered_coefficient(n, j, r, z, w):
    return sum(F(comb(j, k)*comb(n-j, r-k)) * z**(j-k) * (-w)**(r-k)
               for k in range(max(0, r-(n-j)), min(j, r)+1))


def star_at(a, b, w, z):
    n = len(a)-1
    answer = F(0)
    for r in range(n+1):
        p = sum(w**i * a[i][j] * comb(n, j)
                * centered_coefficient(n, j, r, z, w)
                for i in range(n+1) for j in range(n+1)) / (1+w*z)**n
        q = sum(b[i][j] * comb(n, j) * z**j
                * centered_coefficient(n, i, r, w, z)
                for i in range(n+1) for j in range(n+1)) / (1+w*z)**n
        answer += p*q / comb(n, r)
    return answer


def differential_symbol(a, w, z, direction):
    n = len(a)-1
    k = sum(w**i*a[i][j]*comb(n,j)*z**j
            for i in range(n+1) for j in range(n+1))
    kw = sum(i*w**(i-1)*a[i][j]*comb(n,j)*z**j
             for i in range(1,n+1) for j in range(n+1))
    kz = sum(j*w**i*a[i][j]*comb(n,j)*z**(j-1)
             for i in range(n+1) for j in range(1,n+1))
    d = 1+w*z
    sw, sz = kw/d**n-n*z*k/d**(n+1), kz/d**n-n*w*k/d**(n+1)
    return w*sw-z*sz if direction == 0 else sw+z*z*sz


def exact_matrix_checks():
    results=[]
    mp.mp.dps=50
    def coherent_norm(a):
        n=len(a)-1
        matrix=mp.matrix([[mp.mpf(value.numerator)/value.denominator
                           *mp.sqrt(mp.mpf(comb(n,j))/comb(n,i))
                           for j,value in enumerate(row)]
                          for i,row in enumerate(a)])
        return max(mp.svd(matrix,compute_uv=False))
    for N in range(2,10):
        n=N-1
        a=[[F(((i+2)*(j+3)+i*i-2*j)%13-6, i+j+1)
            for j in range(N)] for i in range(N)]
        b=[[F(((i+1)*(j+4)+j*j)%11-5, i+j+2)
            for j in range(N)] for i in range(N)]
        w,z=F(2,7),F(3,11)
        assert star_at(a,b,w,z)==symbol(multiply(a,b),w,z)
        tau=sum(a[j][j] for j in range(N))/N
        off=[[a[i][j]/(i-j) if i!=j else F(0)
              for j in range(N)] for i in range(N)]
        diagonal=[[F(0) for _ in range(N)] for _ in range(N)]
        for j in range(n):
            diagonal[j+1][j]=sum(a[k][k]-tau for k in range(j+1))/(j+1)
        j0=[[F(i==j)*j for j in range(N)] for i in range(N)]
        jm=[[F(j if i==j-1 else 0) for j in range(N)] for i in range(N)]
        co=subtract(multiply(j0,off),multiply(off,j0))
        cd=subtract(multiply(jm,diagonal),multiply(diagonal,jm))
        assert all(co[i][j]+cd[i][j]==a[i][j]-(tau if i==j else 0)
                   for i in range(N) for j in range(N))
        assert symbol(co,w,z)==differential_symbol(off,w,z,0)
        assert symbol(cd,w,z)==differential_symbol(diagonal,w,z,1)
        norm=coherent_norm(a)
        off_ratio=coherent_norm(off)/norm
        diag_ratio=coherent_norm(diagonal)/norm
        assert off_ratio<=mp.pi/2 and diag_ratio<=2
        # Exact compact beta pairing of every matrix unit.
        for j in range(N):
            beta=F(factorial(j)*factorial(n-j),factorial(N))
            assert comb(n,j)*beta==F(1,N)
        # Actual off-root head: both terms must be retained.
        q,M=F(3,5),F(4,3)
        Q=q*q
        e=[[F(0) for _ in range(N)] for _ in range(N)]
        f=[[F(0) for _ in range(N)] for _ in range(N)]
        k=[[F(0) for _ in range(N)] for _ in range(N)]
        for j in range(N):
            k[j][j]=-M/q*Q**(-j)
            if j:
                e[j-1][j]=M*Q**(-j)-1/M
            if j<n:
                f[j+1][j]=1-Q**(j+1)
        t=w*z/(1+w*z)
        rp,rm=(1+(Q-1)*t)**n,(1+(1/Q-1)*t)**n
        assert symbol(k,w,z)==-M/q*rm
        assert symbol(e,w,z)==(M*rm-1/M-(M-1/M)*(1-t)**n)/w
        assert symbol(f,w,z)==w*(1-Q*rp-(1-Q**N)*t**n)
        for h in range(9):
            beta0=F(N*factorial(h)*factorial(n),factorial(N+h))
            assert beta0==F(factorial(h),prod(range(N+1,N+h+1)))
            assert F(N,n+h+1)==F(N,N+h)
        results.append({'level':N,'exact_centered_star_product':True,
                        'global_primitive_matrix_and_vector_fields':True,
                        'compact_beta_trace':True,'both_actual_off_root_walls':True,
                        'coherent_off_primitive_norm_ratio':float(off_ratio),
                        'coherent_diagonal_primitive_norm_ratio':float(diag_ratio)})
    # A literal root clock illustrates why its ordinary symbol power is wrong.
    d=[[F(1),F(0)],[F(0),F(-1)]]
    assert star_at(d,d,F(2,7),F(3,11))==1
    assert symbol(d,F(2,7),F(3,11))**2!=1
    return results


def geometric_checks():
    w,z,A,p,x=sp.symbols('w z A p x',nonzero=True)
    t=w*z/(1+w*z)
    assert sp.simplify(sp.diff(t,z)/w-1/(1+w*z)**2)==0
    K=x/A
    E=(1/x-K)*p
    Ff=(1-A)/p
    def bracket(f,g):
        return sp.simplify(-A*p*(sp.diff(f,A)*sp.diff(g,p)-sp.diff(f,p)*sp.diff(g,A)))
    assert sp.simplify(bracket(K,E)-K*E)==0
    assert sp.simplify(bracket(K,Ff)+K*Ff)==0
    assert sp.simplify(bracket(E,Ff)-K+1/K)==0
    assert sp.simplify(E*Ff+K+1/K-x-1/x)==0
    h=(1-w*z)/(1+w*z)
    e=2*z/(1+w*z)
    f=2*w/(1+w*z)
    assert sp.simplify(h*h+e*f-1)==0
    mp.mp.dps=60
    bounds=[]
    for N in (32,64,128,256):
        Q=mp.exp(2j*mp.pi/N)
        error=max(abs((1+(Q-1)*mp.mpf(t0))**(N-1)-mp.exp(2j*mp.pi*mp.mpf(t0)))
                  for t0 in ('0.2','0.5','0.8'))
        assert N*error<10
        bounds.append({'level':N,'N_times_clock_error':float(N*error)})
    return {'fixed_affine_quadric':True,
            'physical_Gauss_symplectic_form':True,'all_three_physical_brackets':True,
            'Casimir':True,'clock_removable_germ_diagnostics':bounds,
            'literal_clock_star_power_retained':True}


def fixed_rank_a_period_checks():
    """An actual constant-color recurrence with one apparent root pole.

    Operator [(1-q^4 Y)T-1](T-1), TY=q²YT, annihilates C_j=1.
    The selected source is kept while the left companion frame has a pole.
    """
    cases=[]
    source=[[F(0),F(1)],[F(0),F(1)]]
    for N in range(3,11):
        q=F(2,3)
        H=[[F(1),F(0)],[F(0),F(1)]]
        for j in range(1,N-1):
            p=1-q**(2*j+4)
            H=multiply([[F(0),F(1)],[-1/p,(1+p)/p]],H)
        left,right=multiply(source,H),multiply(H,source)
        assert sum(left[j][j] for j in range(2))==1
        assert right==source
        assert star_at(source,H,F(2,7),F(3,11))==symbol(left,F(2,7),F(3,11))

        prime=next(p for p in range(2*N+1,20000,2*N) if sp.isprime(p))
        q0=pow(int(sp.primitive_root(prime)),(prime-1)//(2*N),prime)
        def matmul_mod(a,b):
            return [[sum(a[i][k]*b[k][j] for k in range(2))%prime
                     for j in range(2)] for i in range(2)]
        before=[[1,0],[0,1]]
        for j in range(1,N-2):
            p=(1-pow(q0,2*j+4,prime))%prime
            inv=pow(p,-1,prime)
            before=matmul_mod([[0,1],[-inv,(1+p)*inv]],before)
        c=pow(2*N,-1,prime)
        pole=matmul_mod([[0,0],[c,-c]],before)
        sm=[[0,1],[0,1]]
        lp,rp=matmul_mod(sm,pole),matmul_mod(pole,sm)
        assert any(lp[i][j] for i in range(2) for j in range(2))
        assert (lp[0][0]+lp[1][1])%prime==0
        assert rp==[[0,0],[0,0]]
        cases.append({'level':N,'fixed_companion_rank':2,
                      'exact_actual_period':1,
                      'nonzero_traceless_left_pole':True,
                      'right_source_frame_removes_pole':True})
    return cases


def main():
    result={'exact_finite_source':exact_matrix_checks(),'geometry':geometric_checks(),
            'fixed_rank_actual_a_period':fixed_rank_a_period_checks()}
    output=Path(__file__).with_name('compact_coherent_source_results.json')
    output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
