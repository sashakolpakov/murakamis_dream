#!/usr/bin/env python3
"""Untruncated continuous vacuum positivity and original colored-plat scale.

No root quotient or high-color derivative estimate is imported. The
endpoint-inclusive theorem is in the companion note; finite scalar
continuity is checked instead of differentiating a singular path basis.
"""
from pathlib import Path
import functools
import json
import math
import numpy as np
import mpmath as mp
import sympy as sp


@functools.lru_cache(None)
def paths(length, endpoint=0):
    result=[(0,)]
    for _ in range(length):
        result=[p+(h,) for p in result for h in (p[-1]-1,p[-1]+1) if h>=0]
    return tuple(p for p in result if endpoint is None or p[-1]==endpoint)


class VacuumTL:
    def __init__(self,k,j,theta):
        self.k,self.j,self.m=k,j,j-1
        self.n=2*k*self.m
        self.theta,self.q=theta,np.exp(1j*theta)
        self.delta=2*math.cos(theta)
        self.rows=paths(self.n)
        self.index={p:i for i,p in enumerate(self.rows)}
        self.mu=[math.sin((a+1)*theta)/math.sin(theta) for a in range(k*self.m+1)]
        assert min(self.mu)>0
        self.identity=np.eye(len(self.rows),dtype=complex)
        self.generators={}

    def E(self,i):
        if i in self.generators:return self.generators[i]
        result=np.zeros_like(self.identity)
        for col,p in enumerate(self.rows):
            if p[i-1]!=p[i+1]:continue
            a=p[i-1]
            for b in (a-1,a+1):
                candidate=p[:i]+(b,)+p[i+1:]
                if candidate in self.index:
                    result[self.index[candidate],col]=math.sqrt(self.mu[p[i]]*self.mu[b])/self.mu[a]
        self.generators[i]=result
        return result

    def B(self,i,sign=1):
        positive=self.q**.5*self.identity-self.q**(-.5)*self.E(i)
        return positive if sign>0 else positive.conj().T

    def source(self):
        p=(0,)
        for _ in range(self.k):
            p+=tuple(range(1,self.m+1))+tuple(range(self.m-1,-1,-1))
        u=np.zeros(len(self.rows),complex)
        dim=math.sin(self.j*self.theta)/math.sin(self.theta)
        u[self.index[p]]=dim**(self.k/2)
        return u

    def colored_generator(self,letter):
        offset=(abs(letter)-1)*self.m
        tile=[offset+self.m+r-j for r in range(self.m) for j in range(self.m)]
        signed=tile if letter>0 else [-i for i in reversed(tile)]
        result=self.identity.copy()
        for i in signed:result=self.B(abs(i),1 if i>0 else -1)@result
        return result


def direct_crossing(j,theta):
    q=mp.exp(mp.j*theta);rho=q-1/q;m=j-1
    qi=lambda a:(q**a-q**(-a))/rho
    fac=[mp.mpc(1)]
    for a in range(1,j):fac.append(fac[-1]*qi(a))
    result=mp.matrix(j*j,j*j)
    for a in range(j):
        for b in range(j):
            ec=mp.mpc(1)
            for h in range(min(a,m-b)+1):
                if h:ec*=qi(a-h+1)*qi(j-a+h-1)
                c,d=a-h,b+h
                value=q**(mp.mpf(h*(h-1))/2)*rho**h/fac[h]*ec
                value*=q**(mp.mpf((m-2*c)*(m-2*d))/2)
                result[d*j+c,a*j+b]=value
    return result


def actual_trefoil_cut(j,theta):
    q=mp.exp(mp.j*theta);m=j-1
    r=direct_crossing(j,theta);cube=r*r*r
    dim=mp.sin(j*theta)/mp.sin(theta)
    trace=mp.fsum(q**(2*m-2*a-2*b)*cube[a*j+b,a*j+b]
                 for a in range(j) for b in range(j))
    twist=q**(mp.mpf(m*(m+2))/2)
    return trace/dim/twist**3


def vacuum_checks():
    rows=[]
    for k,j in ((1,2),(1,4),(1,6),(2,2),(2,3),(2,4),(3,2),(3,3),(4,2)):
        nlevel=k*(j-1)+1 # INCLUSIVE endpoint in theorem.
        if nlevel<2:continue
        for fraction in (.5,.73,.95,.9999):
            theta=math.pi/nlevel*fraction
            model=VacuumTL(k,j,theta)
            assert max(max(p) for p in model.rows)==k*(j-1)
            u=model.source();dim=math.sin(j*theta)/math.sin(theta)
            assert abs(np.vdot(u,u)-dim**k)<1e-10*max(1,dim**k)
            worst=0.
            for i in range(1,model.n):
                e=model.E(i);b=model.B(i)
                worst=max(worst,np.linalg.norm(e-e.conj().T),
                          np.linalg.norm(e@e-model.delta*e),
                          np.linalg.norm(b.conj().T@b-model.identity))
                if (i%model.m)!=0:
                    assert np.linalg.norm(e@u)<1e-10*max(1,np.linalg.norm(u))
            assert worst<1e-9,(k,j,fraction,worst)
            # An actual signed colored plat word; all factors retain the
            # original elementary Cartan normalization.
            letter=min(2,2*k-1)
            bplus=model.colored_generator(letter)
            bminus=model.colored_generator(-letter)
            assert np.linalg.norm(bminus@bplus-model.identity)<1e-8
            scalar=np.vdot(u,(bplus@bminus@bplus)@u)/dim
            assert abs(scalar)<=dim**(k-1)*(1+1e-8)
            rows.append({"bridges":k,"color":j,"level":nlevel,
                         "inclusive_endpoint":True,"theta_fraction":fraction,
                         "vacuum_paths":len(model.rows),"max_height":k*(j-1),
                         "max_TL_unitarity_error":float(worst),
                         "original_reduced_plat_bound":float(dim**(k-1))})
    return rows


def actual_normalization_checks():
    rows=[]
    for j in (2,3,4):
        n=2*(j-1)+1
        for fraction in (.5,.85,.99):
            theta=math.pi/n*fraction
            model=VacuumTL(2,j,theta)
            u=model.source();dim=math.sin(j*theta)/math.sin(theta)
            braid=model.colored_generator(2)
            twist=model.q**((j-1)*(j+1)/2)
            pathscalar=np.vdot(u,(braid@braid@braid)@u)/dim/twist**3
            defining=actual_trefoil_cut(j,mp.mpf(theta))
            err=abs(complex(defining)-pathscalar)
            assert err<1e-8,(j,fraction,err,pathscalar,defining)
            rows.append({"color":j,"level":n,"theta_fraction":fraction,
                         "defining_full_Cartan_vs_plat_error":float(err)})
    # At j2,N3 the top path weight is zero. Evaluate the original scalar
    # Laurent polynomial AT the endpoint, not the singular path derivatives.
    qn=mp.exp(mp.j*mp.pi/3)
    p=lambda q:q**(-2)+q**(-6)-q**(-8)
    assert abs(actual_trefoil_cut(2,mp.pi/3)-p(qn))<mp.mpf('1e-60')
    assert abs(p(qn))<=1+mp.mpf('1e-60')
    jets=[]
    for r in (1,2,3,4):
        value=mp.diff(lambda s:p(qn*(1+s/3)),0,r)
        delta=mp.diff(lambda d:p(qn*(1-d)**(mp.mpf(1)/6)),0,r)
        assert mp.isfinite(abs(value)) and mp.isfinite(abs(delta))
        jets.append({"order":r,"endpoint_scaled_q_jet":float(abs(value)),
                     "endpoint_Delta_jet":float(abs(delta))})
    return rows,jets


def exact_chebyshev_checks():
    x=sp.Symbol('x');count=0
    for n in range(31):
        p=sp.chebyshevt(n,x)
        value=sp.Integer(1)
        for r in range(5):
            assert sp.diff(p,x,r).subs(x,1)==value
            value=sp.cancel(value*(n*n-r*r)/(2*r+1))
            count+=1
    return count


def complex_packet_checks():
    rows=[]
    A=5
    for j in (2,3,4):
        n=2*(j-1)+1 # inclusive two-bridge endpoint
        for direction in (1,mp.j,-1,-mp.j):
            s=2*mp.mpf(n)**(-A)*direction
            theta=mp.pi/n-mp.j*s/n
            actual=actual_trefoil_cut(j,theta)
            assert abs(actual)<n**3
            t=-mp.j*mp.tanh(s/(4*n))
            ratio=(1+mp.j*t)/(1-mp.j*t)
            assert abs(ratio/mp.exp(s/(2*n))-1)<mp.mpf('1e-70')
            rows.append({"color":j,"level":n,"disk_exponent":A,
                         "s_real":float(mp.re(s)),"s_imag":float(mp.im(s)),
                         "actual_whole_scalar_modulus":float(abs(actual))})
    for delta in (mp.mpf('1e-3'),mp.mpf('1e-6'),mp.mpf('1e-12')):
        for direction in (1,mp.j,-1,-mp.j):
            x=1+delta*direction
            for ell in (1,2,7,16,64):
                value=mp.chebyt(ell,x)
                assert abs(value)<=mp.exp(4*ell*mp.sqrt(delta))
    return rows


def main():
    mp.mp.dps=80
    vacuum=vacuum_checks()
    actual,jets=actual_normalization_checks()
    cheb=exact_chebyshev_checks()
    complex_rows=complex_packet_checks()
    result={"status":"PASS","continuous_untruncated_vacuum_cases":vacuum,
            "actual_generic_colored_source_normalizations":actual,
            "endpoint_scalar_normal_jets":jets,"exact_Chebyshev_endpoint_checks":cheb,
            "entire_complex_normal_packet":complex_rows,
            "scope":"Macroscopic ordinary quantum-normal window, inclusive endpoint. No fixed-q meridian derivative or complete high-color bound."}
    target=Path(__file__).with_suffix('.json')
    target.write_text(json.dumps(result,indent=2)+'\n')
    print(f'PASS:{len(vacuum)} continuous vacuum windows;{len(actual)} defining R/plat comparisons;'
          f'{len(jets)} endpoint normal jets;{cheb} exact Chebyshev derivative identities')
    print(f'{len(complex_rows)} actual entire complex packet tests, including endpoint colors')
    print(target)


if __name__=='__main__':main()
