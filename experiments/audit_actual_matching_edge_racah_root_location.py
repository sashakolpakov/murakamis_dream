#!/usr/bin/env python3
"""Exact source values and recurrence; positive shift and action diagnostics."""
import json
from pathlib import Path

import mpmath as mp
import sympy as sp

from audit_actual_two_cut_ports import balanced_data


def symbolic():
    u,v,z=sp.symbols('u v z',nonzero=True)
    sn=lambda t:(t-1/t)/(2*sp.I)
    cs=lambda t:(t+1/t)/2
    A=-4*sn(u*z)**4/(sn(u*u*z)*sn(u*u*z*z))
    B=2/(cs(u)*cs(u*z))
    C=-4*sn(u)**4/(sn(u*u)*sn(u*u*z))
    residual=z*v*v+1/(z*v*v)-4*sn(v)**4/(sn(u*v)*sn(u*z/v))
    residual-=A*sn(u*v*z)/sn(u*z/v)+B+C*sn(u/v)/sn(u*v)
    assert sp.factor(residual)==0
    # z here is exp(i theta/2), u is exp(i n theta).
    assert sp.factor(sn(u*z)**2+sn(z)**2-(1-cs(u)*cs(u*z*z)))==0
    assert sp.factor(sn(u/z)*sn(u*z)+sn(z)**2-sn(u)**2)==0
    return 3


def exact():
    counts=dict(original_root_values=0,all_polynomial_recurrence_coefficients=0,
                leading_normalizations=0)
    for N in range(3,35):
        p,eta,q,*_=balanced_data(N);d=N-1;M=d//2;imag=pow(eta,N,p)
        sn=lambda n:(pow(q,n,p)-pow(q,-n,p))*pow(2*imag,-1,p)%p
        cs=lambda n:(pow(q,n,p)+pow(q,-n,p))*pow(2,-1,p)%p
        sf=[1]
        for n in range(1,N):sf.append(sf[-1]*2*sn(n)%p)
        lam=lambda n:2*cs(2*n+1)%p
        polys=[]
        for a in range(M+1):
            coeff=[0]*(a+1);basis=[1]
            for k in range(a+1):
                c=sf[a+k]*pow(sf[a-k]*sf[k]**4,-1,p)%p
                for r,value in enumerate(basis):coeff[r]=(coeff[r]+c*value)%p
                nxt=[0]*(len(basis)+1)
                for r,value in enumerate(basis):
                    nxt[r]=(nxt[r]+lam(k)*value)%p
                    nxt[r+1]=(nxt[r+1]-value)%p
                basis=nxt
            assert coeff[a]==(-1)**a*sf[2*a]*pow(sf[a],-4,p)%p
            counts['leading_normalizations']+=1;polys.append(coeff)
            for g in range(d+1):
                actual=0
                for r in range(max(0,a-g),min(a,d-g)+1):
                    term=sf[g+r]*pow(sf[g+r-a]*sf[r]*sf[a-r],-1,p)%p
                    actual=(actual+term*term)%p
                value=sum(v*pow(lam(g),r,p) for r,v in enumerate(coeff))%p
                assert value==actual
                counts['original_root_values']+=1
        for n in range(M):
            A=-4*sn(n+1)**4*pow(sn(2*n+1)*sn(2*n+2),-1,p)%p
            B=2*pow(cs(n)*cs(n+1),-1,p)%p
            C=0 if n==0 else -4*sn(n)**4*pow(sn(2*n)*sn(2*n+1),-1,p)%p
            for k in range(n+2):
                left=polys[n][k-1] if k else 0
                right=A*polys[n+1][k]
                if k<=n:right+=B*polys[n][k]
                if k<n:right+=C*polys[n-1][k]
                assert (left-right)%p==0
                counts['all_polynomial_recurrence_coefficients']+=1
    return counts


def matrix_data(N,a):
    theta=mp.pi/N
    B=[2/(mp.cos(n*theta)*mp.cos((n+1)*theta)) for n in range(a)]
    beta=[mp.mpf(0)]+[mp.sin(n*theta)**2/(mp.cos(n*theta)**2*mp.sin((2*n-1)*theta)*mp.sin((2*n+1)*theta)) for n in range(1,a)]
    e=[2*mp.sin(n*theta)**2*mp.sqrt(beta[n]) for n in range(a)]
    D=mp.diag([b/2 for b in B]);J=mp.diag(B)
    for n in range(1,a):D[n,n-1]=D[n-1,n]=mp.sqrt(beta[n]);J[n,n-1]=J[n-1,n]=e[n]
    return B,e,D,J


def log_polynomial(N,a,x):
    B,e,_,_=matrix_data(N,a);theta=mp.pi/N
    logsf=lambda k:mp.fsum(mp.log(2*mp.sin(r*theta)) for r in range(1,k+1))
    value=logsf(2*a)-4*logsf(a)
    pivot=None
    for n in range(a):
        pivot=B[n]-x-(e[n]**2/pivot if n else 0)
        assert pivot>0
        value+=mp.log(pivot)
    return value


def integral_J(x):
    if x==0 or x==1:return mp.mpf(0)
    return -mp.im(mp.polylog(2,mp.exp(2j*mp.pi*x)))/(2*mp.pi)


def limiting_action(alpha,x):
    A=mp.sin(mp.pi*alpha)**2;v=2-x
    t=mp.asin(mp.sqrt(A*v/(v+4*A)))/mp.pi
    return integral_J(alpha+t)-integral_J(alpha-t)-4*integral_J(t)+mp.quad(lambda u:mp.log(2*mp.cos(2*mp.pi*u)-x),[0,t])


def diagnostics():
    mp.mp.dps=90;factorizations=roots=0;minimum_gap=mp.inf
    for N in range(3,28):
        a=(N-1)//2;B,e,D,J=matrix_data(N,a);theta=mp.pi/N
        H=mp.diag([mp.sin((n+mp.mpf('.5'))*theta) for n in range(a)])
        difference=J-2*mp.eye(a)-2*H*D*H-2*mp.sin(theta/2)**2*D
        assert mp.norm(difference)<mp.mpf('1e-75')
        eig=mp.eigsy(J,eigvals_only=True)
        assert min(eig)>2
        assert all(eig[k+1]>eig[k] for k in range(a-1))
        minimum_gap=min(minimum_gap,min(eig)-2)
        factorizations+=1;roots+=a
    rows=[];largest=mp.mpf(0)
    for N in (40,81,160):
        for a in sorted(set((N//5,(N-1)//2))):
            alpha=mp.mpf(a)/N
            for x in map(mp.mpf,('-5','-2','0','1.5')):
                actual=log_polynomial(N,a,x)
                predicted=N*limiting_action(alpha,x)
                error=abs(actual-predicted)/mp.log(N)
                assert error<5
                largest=max(largest,error)
                rows.append(dict(N=N,a=a,x=float(x),log_scaled_error=float(error)))
    return dict(positive_shift_factorizations=factorizations,simple_roots_above_two=roots,
                smallest_checked_root_gap=mp.nstr(minimum_gap,20),
                continued_actual_log_rates=len(rows),largest_log_scaled_error=float(largest),rates=rows)


def main():
    result=dict(status='PASS',symbolic_identities=symbolic(),exact=exact(),diagnostics=diagnostics(),
                scope='Exact original root polynomial, own Jacobi recurrence and positive shift. Finite action diagnostics accompany the analytic continuation proof; no relative amplitude, moving-q normal or global contraction estimate.')
    Path(__file__).with_name('actual_matching_edge_racah_root_location_results.json').write_text(json.dumps(result,indent=2)+'\n')
    short=dict(result);short['diagnostics']={k:v for k,v in result['diagnostics'].items() if k!='rates'}
    print(json.dumps(short,indent=2))


if __name__=='__main__':main()
