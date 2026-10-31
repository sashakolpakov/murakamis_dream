#!/usr/bin/env python3
"""Finite spectral-parameter Cauchy identity and original interior coefficients.

Exact checks supplement the analytical uniform theorem; no asymptotic-rate
sampling or shared entropy comparison is asserted.
"""
import argparse
import itertools
import json
from pathlib import Path
import sys

import mpmath as mp
import numpy as np
import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parent))
from audit_actual_nc_morse_graph_first_normal_source_reduction import Local


def eta_checks(counts):
    x,y,lam=sp.symbols('x y lam')
    h=lambda n:sum(x**k*y**(n-k) for k in range(n+1))
    for r in range(9):
        qs=[sp.Integer(1),x+y]
        for n in range(2,r+1):
            qs.append(sp.expand((x+y)*qs[-1]+(lam/sp.Integer(n+1)-1)*x*y*qs[-2]))
        q=qs[r]
        matching=0
        for bits in itertools.product((0,1),repeat=max(0,r-1)):
            chosen=[e+1 for e,b in enumerate(bits) if b]
            if any(b==a+1 for a,b in zip(chosen,chosen[1:])): continue
            removed={v for e in chosen for v in (e-1,e)}
            term=(x*y)**len(chosen)
            for e in chosen: term*=lam/sp.Integer(e+2)
            length=0
            for v in range(r+1):
                if v<r and v not in removed: length+=1
                else:
                    term*=h(length)
                    length=0
            matching+=term
            counts['matching_subsets']+=1
        assert sp.expand(q-matching)==0
        counts['exact_matching_expansions']+=1
        for k in range(r+1):
            a=sp.Poly(q,x,y).coeff_monomial(x**k*y**(r-k))
            assert all(c>=0 for c in sp.Poly(a,lam).all_coeffs())
            counts['nonnegative_parameter_polynomials']+=1
            for value in [sp.Rational(-7,3),sp.Rational(-1),sp.Rational(-1,3),sp.Rational(0),sp.Rational(1,3),sp.Rational(1),sp.Rational(2),sp.Rational(7,3)]:
                at0=a.subs(lam,2)
                assert at0>0
                assert a.subs(lam,value)**2<=at0*a.subs(lam,value**2/2)
                counts['exact_scalar_cauchy_checks']+=1
    theta,j,delta=sp.symbols('theta j delta',real=True)
    expr=2*sp.sin(j*theta)*sp.sin((j-1)*theta)-(sp.cos(theta)-sp.cos((2*j-1)*theta))
    assert sp.trigsimp(expr,method='fu')==0
    expr=4*sp.sin(j*theta)*sp.sin((j-1)*theta)+4*sp.cos((j-sp.Rational(1,2))*theta)**2-4*sp.sin(sp.pi*delta)**2-2*(sp.cos(theta)+sp.cos(2*sp.pi*delta))
    assert sp.trigsimp(expr,method='fu')==0
    u,z=sp.symbols('u z',real=True)
    assert sp.expand((1-u-z)**2+u*(1-u)-(1-z)**2*(1-u)-z*z*u)==0
    counts['symbolic_identities']+=3


def original_checks(counts):
    z=sp.symbols('z')
    for N in range(3,10):
        loc=Local(N)
        p,q,Q,d=loc.p,loc.q,loc.Q,loc.d
        K=loc.Kpair[0]
        Ki=np.diag([pow(int(v),-1,p) for v in np.diag(K)])
        omega=(loc.Fpair[0]@loc.Epair[0]+q*K+pow(q,-1,p)*Ki)%p
        powers=[np.eye(N*N,dtype=np.int64)]
        for _ in range(d):powers.append(powers[-1]@omega%p)
        cc=[int(a)%p for a in sp.Poly(2*sp.chebyshevt(N,z/2)+2,z).all_coeffs()]
        nodes=[(q*pow(Q,j,p)+pow(q,-1,p)*pow(Q,-j,p))%p for j in range(N)]
        bs=[(2-pow(Q,j,p)-pow(Q,-j,p))%p for j in range(N)]
        ss=[0]+[-(pow(q,j,p)-pow(q,-j,p))*(pow(q,j-1,p)-pow(q,1-j,p))%p for j in range(1,N)]

        def operator(sigma,derivative=False):
            op=np.zeros_like(omega)
            for pos,a in enumerate(cc[:-1]):
                degree=N-pos
                for r in range(degree):
                    exponent=degree-1-r
                    if derivative:
                        if exponent==0:continue
                        value=a*exponent*pow(sigma,exponent-1,p)%p
                    else:value=a*pow(sigma,exponent,p)%p
                    op=(op+value*powers[r])%p
            return op

        def grid(op):
            values=[]
            for u in range(N):
                x=-q*pow(Q,u,p)%p
                for v in range(N):
                    y=-pow(q,-1,p)*pow(Q,-v,p)%p
                    for r in range(N):
                        s=(u+v-r)%N
                        actual_delta=r-u
                        c=pow(Q,-actual_delta,p)
                        value=N*pow(q,d*actual_delta,p)*pow(c,d,p)*int(op[r*N+s,u*N+v])%p
                        values.append((x,y,c,value))
                        counts['original_grid_entries']+=1
                        if r+s!=u+v:
                            assert int(op[r*N+s,u*N+v])==0
                            counts['wrong_total_entries']+=1
            return values

        def extract(values,i,j,k):
            r=j-i
            total=sum(value*pow(x,-k,p)*pow(y,k-r,p)*pow(c,j-d,p) for x,y,c,value in values)%p
            return total*pow(N,-3,p)%p

        def tail(sigma,i,j):
            # Coefficients of x^k y^(j-i-k), computed independently of Omega.
            arr0=[1]
            if i==j:return arr0
            arr1=[bs[i+1],bs[i+1]]
            for row in range(i+2,j+1):
                cur=[0]*(row-i+1)
                for k,a in enumerate(arr1):
                    cur[k]=(cur[k]+bs[row]*a)%p
                    cur[k+1]=(cur[k+1]+bs[row]*a)%p
                for k,a in enumerate(arr0):
                    cur[k+1]=(cur[k+1]+ss[row]*(nodes[row-1]-sigma)*a)%p
                arr0,arr1=arr1,cur
            return arr1

        values=list(dict.fromkeys([(-2)%p,0,2,nodes[0],nodes[N//2-1]]))
        for sigma in values:
            physical=grid(operator(sigma))
            for j in range(N//2):
                for i in range(j+1):
                    outside=pow(-1,j-i,p)
                    for a in range(N):
                        if a<i or a>j:outside=outside*(sigma-nodes[a])%p
                    for k,coefficient in enumerate(tail(sigma,i,j)):
                        assert extract(physical,i,j,k)==outside*coefficient%p,(N,sigma,i,j,k)
                        counts['original_one_sided_coefficients']+=1
                        if 0<k<j-i:counts['original_two_outer_coefficients']+=1
            counts['spectral_values']+=1
        ref=(-operator(-2%p))%p if N%2==0 else (operator(-2%p)-pow(N,-2,p)*operator(-2%p,True))%p
        physical=grid(ref)
        for j in range(N//2):
            for i in range(j+1):
                outside=1
                for a in range(N):
                    if (a<i or a>j) and not (N%2 and a==N//2):outside=outside*(2+nodes[a])%p
                if N%2:outside=outside*pow(N,-2,p)%p
                for k,coefficient in enumerate(tail(-2%p,i,j)):
                    assert extract(physical,i,j,k)==outside*coefficient%p
                    counts['odd_reference_coefficients' if N%2 else 'even_reference_coefficients']+=1
        counts['levels']+=1


def rearrangement_checks(counts):
    mp.mp.dps=75
    worst=mp.mpf(0)
    for delta in [mp.mpf(0),mp.mpf(1)/12,mp.mpf(1)/4,mp.mpf(2)/5,mp.mpf(1)/2]:
        a=mp.cos(2*mp.pi*delta)
        for radius in [mp.mpf(1)/5,mp.mpf(1),mp.mpf(7)]:
            phi=mp.atan(radius)
            correction=mp.asin(a*mp.sin(phi))
            theta1,theta2=phi+correction,mp.pi-phi+correction
            worst=max(worst,abs(theta2-theta1-(mp.pi-2*phi)))
            for theta in [theta1,theta2]:
                if abs(mp.cos(theta)+a)>mp.mpf('1e-65'):
                    worst=max(worst,abs(abs(mp.sin(theta)/(mp.cos(theta)+a))-radius))
            counts['level_set_identities']+=1
        for x,y in [(mp.mpf(1),mp.mpf(2)),(mp.mpf(3),mp.mpf(1)),(mp.mpf(1),mp.mpf(0))]:
            A=x+y;rho=4*x*y/A**2;z=mp.sin(mp.pi*delta)**2
            B=lambda v:(1+mp.sqrt(1-rho+rho*v*v))/2
            for t in [mp.mpf(1)/11,mp.mpf(2)/9,mp.mpf(4)/9]:
                s,c=mp.sin(mp.pi*t),mp.cos(mp.pi*t)
                if abs(c*c-z)<mp.mpf('1e-60'):continue
                root=2*s*(A*s+mp.sqrt((x-y)**2*s*s+4*x*y*(1-z)**2))
                energy=root*4*c*c/(4*(c*c-z))**2
                R=s*c/(c*c-z)
                compact=A*R*R*B((1-z)/s)
                tp=mp.atan(abs(R))/mp.pi
                upper=A*mp.tan(mp.pi*tp)**2*B(1/mp.sin(mp.pi*tp))
                worst=max(worst,abs(energy-compact))
                assert compact<=upper+mp.mpf('1e-65')
                counts['weighted_kernel_identities']+=1
                counts['pointwise_rearrangement_bounds']+=1
    assert worst<mp.mpf('1e-65')
    return str(worst)


def run():
    counts={name:0 for name in ['matching_subsets','exact_matching_expansions',
        'nonnegative_parameter_polynomials','exact_scalar_cauchy_checks','symbolic_identities',
        'levels','spectral_values','original_grid_entries','wrong_total_entries',
        'original_one_sided_coefficients','original_two_outer_coefficients',
        'odd_reference_coefficients','even_reference_coefficients','level_set_identities',
        'weighted_kernel_identities','pointwise_rearrangement_bounds']}
    eta_checks(counts)
    original_checks(counts)
    error=rearrangement_checks(counts)
    return {'status':'PASS','counts':counts,'max_identity_error':error,
        'scope':'Exact parameter-matching expansion and rational Cauchy inequalities; original coproduct/DFT coefficients at both parities with all unused rows and reference derivatives; symbolic and fixed high-precision rearrangement identities. No asymptotic-rate sampling or global shared-entropy claim.'}


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,default=Path(__file__).with_name('actual_one_sided_relative_spectral_energy_results.json'))
    args=parser.parse_args()
    result=run()
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
