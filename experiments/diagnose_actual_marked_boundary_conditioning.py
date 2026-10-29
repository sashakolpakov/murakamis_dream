#!/usr/bin/env python3
"""High-precision original boundary moments via a finite generic cluster sum.

Diagnostic only: the finite formulas are independently proved from the
actual Clebsch/duality source; growing-level samples do not prove a bound.
"""
import argparse
import itertools
import json
from pathlib import Path

import mpmath as mp


def ring_mul(a,b):
    out=[mp.mpc(0) for _ in a]
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            if not i&j:out[i|j]+=x*y
    return out


class GenericPacket:
    def __init__(self,N,t):
        self.N,self.d=N,N-1
        self.zeta=mp.exp(mp.pi*1j/N+t)
        self.cache={0:mp.mpc(1)}
        self.f=[mp.mpc(0)]+[1-self.power(2*k) for k in range(1,3*self.d+2)]
        self.F=[mp.mpc(1)]
        for k in range(1,len(self.f)):self.F.append(self.F[-1]*self.f[k])
        self.cV=N*self.power(-self.d*self.d)
        self.pV=[self.cV*(-1)**u*self.power(u*(self.d-u-1))*self.F[u]*self.F[self.d-u]/self.F[self.d]
                 for u in range(N)]
        self.hs={};self.sources={};self.norms={};self.middles={}

    def power(self,k):
        if k not in self.cache:self.cache[k]=self.zeta**k
        return self.cache[k]

    def highest(self,j):
        if j not in self.hs:
            t=self.d-j
            h=[mp.mpc(1)]
            for u in range(t):h.append(-self.power(-self.d+2*(t-1-u))*self.f[j+1+u]/self.f[self.d-u]*h[-1])
            self.hs[j]=h
        return self.hs[j]

    def cupQ(self,j,r):
        return (-1)**r*self.power(r*(2*j-r-1))*self.F[r]*self.F[2*j-r]/self.F[2*j]

    def middle(self,j,r,A,B):
        key=(j,r,A,B)
        if key not in self.middles:
            t=self.d-j
            assert A+B==t+r and 0<=A<=self.d and 0<=B<=self.d
            h=self.highest(j)
            val=mp.mpc(0)
            for z in range(max(0,A-t,r-B),min(r,A)+1):
                u=A-z;v=r-z
                val+=h[u]*self.power(-self.d*v+2*u*v)/(self.F[z]*self.F[v]*self.F[u]*self.F[t-u])
            self.middles[key]=self.F[A]*self.F[B]*val
        return self.middles[key]

    def source(self,a,b,c):
        key=(a,b,c)
        if key not in self.sources:
            r1=a+b-c
            assert min(r1,a+c-b,b+c-a)>=0
            ha,hc=self.highest(a),self.highest(c)
            value=mp.mpc(0)
            for k in range(self.d-max(a,c)+1):
                u=self.d-a-k;v=self.d-c-k
                value+=ha[u]*hc[v]*self.middle(b,r1,v,a+k)/(self.pV[u]*self.pV[k]*self.pV[v])
            self.sources[key]=self.power(c*(self.d-2*c)-2*c)*self.cupQ(b,r1)*value
        return self.sources[key]

    def norm(self,j):
        if j not in self.norms:
            self.norms[j]=(-1)**(self.d+j)*self.power(j*(j+1)-self.d*(2*j+1))*self.F[self.d+j+1]
            self.norms[j]/=self.cV**2*self.F[self.d-j]*self.F[2*j+1]
        return self.norms[j]

    def theta(self,a,b,c):
        J=a+b+c;r=b+c-a;r1=a+b-c;r2=a+c-b
        return ((-1)**r1*self.power(2*c-r1*(r-1))*self.F[2*b]*self.F[r2]*self.F[J+1]
                /(self.f[1]*self.F[r]*self.F[2*a]*self.F[r1]*self.F[2*c]))

    def closed_branch(self,js):
        a,b,c=js
        if min(b+c-a,a+c-b,a+b-c)<0:return mp.mpc(0)
        return self.source(a,b,c)*self.source(c,b,a)*self.theta(a,b,c)/(self.norm(a)*self.norm(b)*self.norm(c))

    def circle(self,j):
        z=self.power(2*j+1)+self.power(-2*j-1)
        u,v=mp.mpc(1),z
        if self.N==2:return -v
        for _ in range(2,self.N):u,v=v,z*v-u
        return (-1)**self.d*v

    def moments_closed(self,labels):
        active=[i for i,j in enumerate(labels) if 2*j<self.d]
        choices=[(j,) if 2*j==self.d else (j,self.d-j) for j in labels]
        values=[mp.mpc(0) for _ in range(1<<len(active))]
        for js in itertools.product(*choices):
            branch=self.closed_branch(js)
            currents=[self.circle(js[axis]) for axis in active]
            for mask in range(len(values)):
                coefficient=mp.mpc(1)
                for k,current in enumerate(currents):
                    if mask>>k&1:coefficient*=current
                values[mask]+=coefficient*branch
        return values


def positive_tau(N,labels):
    d=N-1;J=sum(labels);delta=J-d
    s=[mp.mpf(1)]
    for k in range(1,N):s.append(s[-1]*2*mp.sin(mp.pi*k/N))
    R=mp.fsum(s[t]*s[J-t]/mp.fprod(s[t-j]*s[J-j-t] for j in labels)
              for t in range(max(labels),J-max(labels)+1))
    r=sum(2*j<d for j in labels)
    Z=N*N*2**r*mp.fprod(s[J-2*j] for j in labels)/s[delta]*R*R
    return Z/N**(3-r)


def measure(N,labels,dps,shrink=1):
    with mp.workdps(dps):
        h=mp.mpf(N)**-8/shrink
        plus=GenericPacket(N,h).moments_closed(labels)
        minus=GenericPacket(N,-h).moments_closed(labels)
        rho=2j*mp.sin(mp.pi/N)
        nu=2*N*(-1)**N/rho
        moments=[(p-m)/(2*h*nu) for p,m in zip(plus,minus)]
        tau=positive_tau(N,labels)
        errors=abs(moments[-1]/tau-1)
        qpoly=[moments[len(moments)-1-i]/tau for i in range(len(moments))]
        qpoly[0]=mp.mpc(1)
        n=qpoly.copy();n[0]=mp.mpc(0)
        power=[mp.mpc(1)]+[mp.mpc(0)]*(len(n)-1)
        root=[mp.mpc(0)]*len(n)
        r=(len(n)-1).bit_length()
        for k in range(r+1):
            coefficient=mp.binomial(mp.mpf('.5'),k)
            root=[x+coefficient*y for x,y in zip(root,power)]
            power=ring_mul(power,n)
        K=mp.fsum(abs(a)**2 for a in root)
        return {'N':N,'labels':list(labels),'dps':dps,'normal_step':mp.nstr(h,20),
                'top_moment_relative_error':mp.nstr(errors,20),'K':mp.nstr(K,40),
                'log_K_over_N':mp.nstr(mp.log(K)/N,25),
                'normalized_moments':[[mp.nstr(mp.re(v/tau),30),mp.nstr(mp.im(v/tau),30)] for v in moments]}


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--levels',default='8,12,16,24,32')
    parser.add_argument('--dps',type=int,default=140)
    parser.add_argument('--deficit',type=int,default=0,help='additional deficit below nearest paired center')
    parser.add_argument('--output',default='actual_marked_boundary_conditioning_diagnostic.json')
    args=parser.parse_args()
    rows=[]
    for N in map(int,args.levels.split(',')):
        j=(N-2)//2-args.deficit
        row=measure(N,(j,j,j),max(args.dps,N+80))
        rows.append(row)
        print(json.dumps(row),flush=True)
        Path(args.output).write_text(json.dumps({'status':'DIAGNOSTIC','rows':rows,'scope':'Original finite generic cluster confluence; finite precision/normal steps, no uniform conditioning theorem.'},indent=2)+'\n')
