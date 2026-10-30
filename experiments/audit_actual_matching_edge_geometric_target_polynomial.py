#!/usr/bin/env python3
"""Actual typed target, generic source polynomial, retained jets, scalar rate.

Finite checks supplement the displayed two-Sears and variational proofs.
No source-network or completed-operator asymptotic is asserted.
"""
import json
import math
from pathlib import Path
import numpy as np
import sympy as sp
import mpmath as mp

from audit_actual_matching_edge_completed_projector_block import omega
from audit_actual_q_hahn_physical_generic_jet_bound import Jet, divide_simple_zero
from audit_high_color_first_normal_r_degree import root_field


def geometry():
    x,y,z,s,t,r=sp.symbols('x y z s t r',nonzero=True)
    def L(x,s):return sp.Matrix([[1,0],[s*(1-x)/x,-1/x]])
    def G(x,s):return sp.Matrix([[-1/x,(1-x)/(x*s)],[-s*(1-x)/x,-2+1/x]])
    heads=[(x,s),(y,t),(1/y,-t),(1/x,-s)]
    prefix=sp.eye(2);raw=[]
    for xx,ss in heads:
        raw.append(sp.simplify(prefix.inv()*G(xx,ss)*prefix))
        prefix=sp.simplify(L(xx,ss)*prefix)
    assert sp.simplify(raw[2]-raw[1].inv())==sp.zeros(2)
    assert sp.simplify(raw[3]-raw[0].inv())==sp.zeros(2)
    assert prefix==sp.eye(2)
    F=s*(1-x)-x*t*(1-y)
    outy=x*y/z;outs=(r*(1-z)-F)/(z*(1-outy))
    assert sp.simplify(L(outy,outs)*L(z,r)-L(y,t)*L(x,s))==sp.zeros(2)
    b,c,eps=sp.symbols('b c eps',nonzero=True)
    A=-sp.Matrix([[1,1],[0,1]]);B=-sp.Matrix([[1,0],[-4,1]])
    H=B*A+sp.eye(2);C=sp.eye(2)+b*H
    assert H*H==sp.zeros(2)
    trace=sp.expand(sp.trace(B.inv()*C*B*C.inv()))
    assert trace==2+16*b*b
    tau=2*sp.I*c/(1-eps*sp.I*c)
    assert sp.simplify(eps/2+1/tau+sp.I/(2*c))==0
    assert sp.simplify(trace.subs(b,-sp.I/(2*c))-(2-4/c**2))==0
    return dict(exact_nested_inverse_meridians=2,exact_total_lower_preservation=1,
                exact_target_trace_and_primitive_shear=3)


def generic_data(d,q,p):
    de=(q-pow(q,-1,p))%p
    ns=[(pow(q,n,p)-pow(q,-n,p))*pow(de,-1,p)%p for n in range(2*d+3)]
    fac=[1]
    for n in range(1,2*d+3):fac.append(fac[-1]*ns[n]%p)
    D=[(-1)**g*ns[d+1]*fac[g]**2*fac[d-g]*pow(fac[d+g+1],-1,p)%p for g in range(d+1)]
    def source(a,g):
        S=0
        for z in range(d+max(a,g),min(2*d,d+a+g)+1):
            den=fac[z-d-a]**2*fac[z-d-g]**2*fac[2*d-z]*fac[d+a+g-z]**2
            S=(S+(-1)**z*fac[z+1]*pow(den,-1,p))%p
        return (-1)**d*S*pow(ns[d+1],-1,p)*D[a]*D[g]%p
    return ns,D,source


def generic():
    count=matrices=entries=0;p=1000003
    for q in (2,3,5):
        for d in range(1,16):
            ns,Ds,source=generic_data(d,q,p)
            for a in range(d+1):
                for g in range(d+1):
                    val=term=1
                    for k in range(a):
                        if k>=g:break
                        term=-term*ns[a-k]*ns[a+k+1]*ns[g-k]*ns[g+k+1]*pow(ns[k+1]**2*ns[d-k]*ns[d+k+2],-1,p)%p
                        val=(val+term)%p
                    assert source(a,g)==val
                    count+=1
            if q!=2 or d>5:continue
            N=d+1;O=omega(d,q,p);I=np.eye(N*N,dtype=np.int64)
            lams=[(pow(q,2*g+1,p)+pow(q,-2*g-1,p))%p for g in range(N)]
            Ps=[]
            for g in range(N):
                M=I.copy()
                for h in range(N):
                    if h!=g:M=M@(O-lams[h]*I)%p*pow(lams[g]-lams[h],-1,p)%p
                Ps.append(M)
            delta2=(q-pow(q,-1,p))**2%p
            for a in range(d//2+1):
                direct=I.copy();term=I.copy()
                for k in range(a):
                    scalar=-ns[a-k]*ns[a+k+1]*pow(ns[k+1]**2*ns[d-k]*ns[d+k+2]*delta2,-1,p)%p
                    term=term@(O-lams[k]*I)%p*scalar%p
                    direct=(direct+term)%p
                spectral=sum((source(a,g)*Ps[g]%p for g in range(N)),np.zeros_like(I))%p
                assert np.array_equal(direct,spectral)
                matrices+=1;entries+=N**4
    return dict(original_generic_seven_factorial_values=count,
                original_Casimir_polynomial_matrices=matrices,operator_entries=entries)


def root_jets():
    counts=hermite=0
    for N in range(3,15):
        d=N-1;p,eta=root_field(N);root=eta*eta%p
        Jet.p=p;Jet.order=4
        q=Jet([root*pow(math.factorial(k),-1,p)%p for k in range(4)])
        delta=q-q**-1
        nums=[(q**n-q**(-n))/delta for n in range(2*N)]
        regular=[Jet(1)];noN=[Jet(1)]
        for n in range(1,2*N):
            regular.append(regular[-1]*nums[n])
            noN.append(noN[-1] if n==N else noN[-1]*nums[n])
        D=[(-1)**g*regular[g]**2*regular[d-g]/noN[d+g+1] for g in range(N)]
        lams=[q**(2*g+1)+q**(-2*g-1) for g in range(N)]
        for a in range(d//2+1):
            values=[];derivatives=[]
            for g in range(N):
                original=Jet(0)
                for z in range(d+max(a,g),min(2*d,d+a+g)+1):
                    den=regular[z-d-a]**2*regular[z-d-g]**2*regular[2*d-z]*regular[d+a+g-z]**2
                    original+=(-1)**(d+z)*noN[z+1]/den
                value=term=Jet(1);dv=dt=Jet(0)
                for k in range(a):
                    coef=-nums[a-k]*nums[a+k+1]/(nums[k+1]**2*nums[d-k]*nums[d+k+2]*delta**2)
                    factor=coef*(lams[g]-lams[k])
                    dt=dt*factor+term*coef
                    term=term*factor
                    value+=term;dv+=dt
                assert value==original*D[a]*D[g]
                values.append(original*D[g]);derivatives.append(dv/D[a]);counts+=1
            for g in range(N//2):
                gp=d-g
                actual=divide_simple_zero(values[g]-values[gp],lams[g]-lams[gp])
                assert actual[0]==derivatives[g].c[0]
                hermite+=1
    return dict(original_generic_root_four_jets=counts,
                original_normal_equals_spectral_derivative=hermite)


def rates():
    mp.mp.dps=80;rows=[]
    for N in (40,81,160,321):
        for xi0,c in [(mp.mpf('.3'),mp.mpf('.7')),(mp.mpf('.5'),mp.mpf('.5')),(mp.mpf('.5'),mp.mpf('.85'))]:
            a=min(int(mp.floor(N*xi0)),(N-1)//2);xi=mp.mpf(a)/N
            z=2-4/c**2;theta=mp.pi/N
            lam=lambda r:2*mp.cos((2*r+1)*theta)
            term=mp.mpf(1);value=term;terms=[term]
            for k in range(a):
                term*=((lam(k)-lam(a))*(lam(k)-z))/(2*mp.sin((k+1)*theta))**4
                assert term>0
                value+=term;terms.append(term)
            A=mp.sin(mp.pi*xi)**2;kappa=c**-2
            star=mp.asin(mp.sqrt(A*kappa/(A+kappa)))/mp.pi
            action=mp.quad(lambda u:mp.log((A-mp.sin(mp.pi*u)**2)*(kappa-mp.sin(mp.pi*u)**2)/mp.sin(mp.pi*u)**4),[0,star])
            residual=mp.log(value)-N*action
            assert abs(residual)<10*mp.log(N)
            mode=max(range(len(terms)),key=terms.__getitem__)
            assert abs(mp.mpf(mode)/N-star)<3/mp.sqrt(N)
            rows.append(dict(N=N,a=a,c=str(c),selected_mode=mode,
                             actual_log_value=str(mp.log(value)),action=str(action),
                             log_residual=str(residual)))
    return dict(precision_digits=80,positive_actual_scalar_rate_cases=len(rows),rows=rows,
                max_log_residual_over_logN=str(max(abs(mp.mpf(r['log_residual']))/mp.log(r['N']) for r in rows)))


def main():
    result=dict(status='PASS',geometry=geometry(),generic=generic(),normals=root_jets(),scalar_rates=rates(),
                scope='Exact typed geometric target, original generic Casimir polynomial and retained Hermite normal; positive scalar evaluation only. No completed-operator or whole-source asymptotic.')
    Path(__file__).with_name('actual_matching_edge_geometric_target_polynomial_results.json').write_text(json.dumps(result,indent=2)+'\n')
    small={**result,'scalar_rates':{k:v for k,v in result['scalar_rates'].items() if k!='rows'}}
    print(json.dumps(small,indent=2))

if __name__=='__main__':main()
