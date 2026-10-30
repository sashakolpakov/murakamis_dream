"""Exact sparse formal-Q verification of the canonical joint source identity.

Monomials are indexed by (Q power,U power,T power); integer coefficients
are retained throughout. The proof is the finite-degree argument in the
note; this checks its precise polynomial conventions independently.
"""
from functools import lru_cache


def add(*ps):
    out={}
    for p in ps:
        for k,v in p.items():out[k]=out.get(k,0)+v
    return {k:v for k,v in out.items() if v}


def mul(a,b):
    out={}
    for x,v in a.items():
        for y,w in b.items():
            k=tuple(xi+yi for xi,yi in zip(x,y));out[k]=out.get(k,0)+v*w
    return {k:v for k,v in out.items() if v}


def shift(p,dq=0,du=0,dt=0,scalar=1):
    return {(q+dq,u+du,t+dt):scalar*v for (q,u,t),v in p.items()}


def u_shift(p,power):
    return {(q+power*u,u,t):v for (q,u,t),v in p.items()}


@lru_cache(None)
def gaussian(n,k):
    if k<0 or k>n:return {}
    if k==0 or k==n:return {(0,0,0):1}
    return add(gaussian(n-1,k),shift(gaussian(n-1,k-1),dq=n-k))


def joint_S(j):
    total={}
    for a in range(j+1):
        term=shift(mul(gaussian(j,a),gaussian(j,a)),dq=a*(a+1)//2,dt=a,scalar=(-1)**a)
        for r in range(a):term=mul(term,{(0,1,0):1,(r,0,0):-1})
        for r in range(j-a):term=mul(term,{(0,0,1):1,(r,1,0):-1})
        total=add(total,term)
    return total


def audit_formal_joint_casimir(channels=range(2,7)):
    rows=[]
    for j in channels:
        S=joint_S(j)
        assert max(k[1] for k in S)<=j and max(k[2] for k in S)<=j
        S0={(q,u,0):v for (q,u,t),v in S.items() if t==0}
        assert S0=={(j*(j-1)//2,j,0):(-1)**j}
        first=shift(mul(mul({(0,1,0):1,(0,0,1):-1},
                            {(0,0,0):1,(1,1,0):-1}),u_shift(S,1)),dq=-j,scalar=-1)
        second=shift(mul(mul({(0,1,0):1,(1,0,1):-1},
                             {(0,0,0):1,(0,1,0):-1}),u_shift(S,-1)),dq=j,scalar=-1)
        diagonal={(0,1,0):2,(1,1,1):2,(0,2,0):-1,(1,2,0):-1,
                  (j+1,0,1):-1,(-j,0,1):-1}
        residual=add(first,second,mul(diagonal,S))
        assert not residual,(j,residual)
        rows.append({'channel':j,'exact_source_monomials':len(S),
                     'formal_Q_Casimir_residual_zero':True,
                     'T_zero_monomial_checked':True})
    return {'status':'PASS','formal_joint_channels':rows,
            'scope':'Sparse integer Laurent-polynomial verification in formal Q,U,T, not a root-only test.'}


# The source identity above is formal. These checks independently compare the
# resulting recurrence, determinant and all retained finite prefactors.
import json
from pathlib import Path
import mpmath as mp
import numpy as np
from audit_actual_two_cut_ports import balanced_data


def scalar_gaussian(Q, n, k, p=None):
    out = 1
    for r in range(1, k+1):
        if p:
            out = out*(1-pow(Q,n-k+r,p))*pow(1-pow(Q,r,p),-1,p) % p
        else:
            out *= (1-Q**(n-k+r))/(1-Q**r)
    return out


def exact_checks():
    counts = dict(coefficient_recurrences=0, determinant_values=0,
                  positive_minor_formulas=0, nonphysical_source_values=0)
    for N in range(3, 24):
        p, eta, q, *_ = balanced_data(N)
        Q = q*q % p
        ii = pow(eta, N, p)
        inv2 = pow(2,-1,p)
        sine = lambda r: (pow(q,r,p)-pow(q,-r,p))*pow(2*ii,-1,p) % p
        cosine = lambda r: (pow(q,r,p)+pow(q,-r,p))*inv2 % p
        J = (N-1)//2
        B = {n:sine(n)**2*pow(cosine(n)**2*sine(2*n-1)*sine(2*n+1)%p,-1,p)%p
             for n in range(1,J)}
        def coeff(j,c):
            out=[1]
            for k in range(1,j+1):
                v=2*c*sine(j+1-k)**2*out[k-1]
                if k>=2:v+=sine(j+2-k)*sine(j+1-k)*out[k-2]
                out.append(v*pow(sine(k)*sine(2*j+1-k)%p,-1,p)%p)
            return out
        for c in (0,1,3,17):
            polys=[coeff(j,c) for j in range(J+1)]
            for n in range(1,J):
                a=c*pow(cosine(n)*cosine(n+1)%p,-1,p)%p
                b=B[n]*(cosine(n)**2-c*c)%p
                for k,target in enumerate(polys[n+1]):
                    actual=(polys[n][k] if k<len(polys[n]) else 0)
                    if k:actual+=a*polys[n][k-1]
                    if k>=2:actual+=b*polys[n-1][k-2]
                    assert actual%p==target
                counts['coefficient_recurrences']+=1
            for z in (2,7):
                dets=[1]
                for j in range(1,J+1):
                    diagonal=(z+c*pow(cosine(j-1)*cosine(j)%p,-1,p))%p
                    determinant=diagonal*dets[-1]
                    if j>1:determinant-=B[j-1]*(c*c-cosine(j-1)**2)*dets[-2]
                    dets.append(determinant%p)
                    value=sum(a*pow(z,j-k,p) for k,a in enumerate(polys[j]))%p
                    assert value==dets[-1]
                    counts['determinant_values']+=1
        previous=[1]
        for j in range(1,J+1):
            value=pow(cosine(j-1)*cosine(j)%p,-1,p)*previous[-1]
            if j>1:value-=B[j-1]*previous[-2]
            previous.append(value%p)
            closed=pow(2,j,p)
            for r in range(1,j+1):closed=closed*sine(r)*pow(sine(j+r),-1,p)%p
            assert previous[-1]==closed
            counts['positive_minor_formulas']+=1
        for j in sorted(set((1,J))):
            for w,U in ((37,19),(41,23)):
                T=w*w%p
                c=-(q*w+pow(q*w%p,-1,p))*inv2%p
                P=coeff(j,c)
                S=0
                for a in range(j+1):
                    term=(-1)**a*pow(Q,a*(a+1)//2,p)*scalar_gaussian(Q,j,a,p)**2*pow(T,a,p)
                    for r in range(a):term=term*(U-pow(Q,r,p))%p
                    for r in range(j-a):term=term*(T-U*pow(Q,r,p))%p
                    S=(S+term)%p
                predicted=pow(T,j,p)*scalar_gaussian(Q,2*j,j,p)*sum(v*pow(U*pow(w,-1,p)%p,k,p) for k,v in enumerate(P))%p
                assert S==predicted
                counts['nonphysical_source_values']+=1
    return counts


def mp_coeff(N,j,c):
    s=lambda r:mp.sin(mp.pi*r/N)
    out=[mp.mpf(1)]
    for k in range(1,j+1):
        out.append((2*c*s(j+1-k)**2*out[k-1]+(s(j+2-k)*s(j+1-k)*out[k-2] if k>=2 else 0))/(s(k)*s(2*j+1-k)))
    return out


def mp_matrices(N,j):
    s=lambda r:mp.sin(mp.pi*r/N)
    cs=lambda r:mp.cos(mp.pi*r/N)
    D=mp.matrix(j);K=mp.matrix(j)
    for n in range(j):D[n,n]=1/(cs(n)*cs(n+1))
    for n in range(1,j):
        b=s(n)**2/(cs(n)**2*s(2*n-1)*s(2*n+1))
        D[n-1,n]=D[n,n-1]=mp.sqrt(b)
        K[n-1,n]=mp.sqrt(b)*cs(n)
        K[n,n-1]=-K[n-1,n]
    return D,K


def numerical_checks():
    mp.mp.dps=100
    cases=[]; maxerr=mp.mpf(0); center=0
    for N in (7,12,31):
        j=(N-1)//2;q=mp.exp(mp.pi*1j/N);Q=q*q;d=N-1
        D,K=mp_matrices(N,j)
        eig=np.linalg.eigvalsh(np.array(D.tolist(),dtype=float))
        assert eig[0]>0
        for tau,nu in ((mp.mpc('.72','.12'),mp.mpc('.36','-.13')),
                       (mp.mpc('.81','-.09'),mp.mpc('.45','.17')),
                       (mp.mpc('.62','.04'),mp.mpc('.19','.02'))):
            t=N*tau;u=N*nu;U=Q**u;V=Q**(t-u)
            c=-mp.cos(mp.pi*(tau+mp.mpf(1)/N));z=mp.exp(mp.pi*1j*(tau-2*nu))
            assert mp.re(c)>0 and mp.re(z)>0
            A=z*mp.eye(j)+c*D+K
            determinant=mp.det(A)
            P=mp_coeff(N,j,c)
            R=sum(a*z**(j-k) for k,a in enumerate(P))
            H=0
            for a in range(j+1):
                term=scalar_gaussian(Q,j,a)**2*q**(a*(a-d))*V**a
                for r in range(a):term*=U-Q**r
                for r in range(j-a):term*=V-Q**r
                H+=term
            denominator=mp.fprod(Q**t-Q**r for r in range(j))
            actual=mp.exp(mp.pi*1j*d*u/N)*H/denominator
            predicted=mp.exp(mp.pi*1j*d*u/N)*q**(j*t)*scalar_gaussian(Q,2*j,j)*determinant/denominator
            err=max(abs(R/determinant-1),abs(actual/predicted-1))
            assert err<mp.mpf('1e-65');maxerr=max(maxerr,err)
            inv=A**-1
            dz=sum(inv[a,a] for a in range(j))
            dc=sum((inv*D)[a,a] for a in range(j))
            assert abs(dz)<=j/mp.re(z)*(1+mp.mpf('1e-80'))
            assert abs(dc)<=j/mp.re(c)*(1+mp.mpf('1e-80'))
            cases.append(dict(N=N,j=j,min_eigenvalue_D=float(eig[0]),
                              relative_source_determinant_error=float(err),
                              z_derivative_bound_ratio=float(abs(dz)*mp.re(z)/j),
                              c_derivative_bound_ratio=float(abs(dc)*mp.re(c)/j)))
        tau=mp.mpf('.715');t=N*tau;c=-mp.cos(mp.pi*(tau+mp.mpf(1)/N))
        R1=sum(mp_coeff(N,j,c));assert R1>0
        denominator=mp.fprod(Q**t-Q**r for r in range(j))
        source=mp.exp(mp.pi*1j*d*t/(2*N))*q**(j*t)*scalar_gaussian(Q,2*j,j)*R1/denominator
        phase=mp.pi*(d*(t-j)+j*j)/(2*N)
        unit=source*mp.exp(-1j*phase)
        assert mp.re(unit)>0 and abs(mp.im(unit)/mp.re(unit))<mp.mpf('1e-90')
        center+=1
    return dict(precision_digits=mp.mp.dps,joint_noninteger_complex_source_cases=len(cases),
                noninteger_real_center_phases=center,max_relative_error=float(maxerr),cases=cases)


def main():
    result=dict(status='PASS',formal_source=audit_formal_joint_casimir(),
                exact_finite_field=exact_checks(),numerical=numerical_checks(),
                scope='Exact source-defined joint determinant, recurrence and minors; complex noninteger source and accretive derivative checks. No global source-cycle or volume-limit assertion.')
    Path(__file__).with_name('actual_q_hahn_joint_accretive_determinant_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='numerical'}|{'numerical':{k:v for k,v in result['numerical'].items() if k!='cases'}},indent=2))


if __name__=='__main__':main()
