#!/usr/bin/env python3
"""Actual plat endpoint splitting and its original normalized first trace jet."""
import json
from pathlib import Path
import numpy as np
from audit_actual_two_cut_ports import balanced_data
from audit_actual_marked_multiport_chebyshev_source_packet import pair_circle
from audit_actual_trivalent_full_cd_normalization_and_magnetic_growth import physical_columns
from audit_general_augmented_plat_matching_geometry import plat_matching,cubic_dictionary

class Jets:
    def __init__(self,N):
        self.N=N; self.d=N-1; self.p,self.eta,self.q,*_=balanced_data(N)
    def add(self,a,b):return ((a[0]+b[0])%self.p,(a[1]+b[1])%self.p)
    def neg(self,a):return (-a[0]%self.p,-a[1]%self.p)
    def mul(self,a,b):return (a[0]*b[0]%self.p,(a[0]*b[1]+a[1]*b[0])%self.p)
    def inv(self,a):
        v=pow(int(a[0]),-1,self.p);return v,-int(a[1])*v*v%self.p
    def power(self,a):
        v=pow(self.q,a,self.p);return v,a*v%self.p
    def matmul(self,a,b):return a[0]@b[0]%self.p,(a[1]@b[0]+a[0]@b[1])%self.p
    def kron(self,a,b):return np.kron(a[0],b[0])%self.p,(np.kron(a[1],b[0])+np.kron(a[0],b[1]))%self.p
    def scale(self,a,s):return a[0]*s[0]%self.p,(a[1]*s[0]+a[0]*s[1])%self.p
    def operators(self):
        n,d,p=self.N,self.d,self.p
        def zero():return np.zeros((n,n),dtype=np.int64),np.zeros((n,n),dtype=np.int64)
        E,F,K,Ki=zero(),zero(),zero(),zero()
        for u in range(n):
            k=self.power(d-2*u);ki=self.power(-d+2*u)
            for c in range(2):K[c][u,u]=k[c];Ki[c][u,u]=ki[c]
            if u>0:
                e=self.mul(self.power(-n),self.add((1,0),self.neg(self.power(2*(n-u)))))
                f=self.add((1,0),self.neg(self.power(2*u)))
                for c in range(2):E[c][u-1,u]=e[c];F[c][u,u-1]=f[c]
        I=np.eye(n,dtype=np.int64),np.zeros((n,n),dtype=np.int64)
        Ep=self.add(self.kron(E,K),self.kron(I,E))
        Fp=self.add(self.kron(F,I),self.kron(Ki,F))
        Kp=self.kron(K,K);Kpi=self.kron(Ki,Ki)
        O=self.add(self.matmul(Fp,Ep),self.add(self.scale(Kp,self.power(1)),self.scale(Kpi,self.power(-1))))
        ident=np.eye(n*n,dtype=np.int64),np.zeros((n*n,n*n),dtype=np.int64)
        m=d//2;nodes=[self.add(self.power(2*j+1),self.power(-2*j-1)) for j in range(n)]
        P=ident
        for j in range(n):
            if j==m:continue
            factor=self.add(O,self.neg(self.scale(ident,nodes[j])))
            factor=self.scale(factor,self.inv(self.add(nodes[m],self.neg(nodes[j]))))
            P=self.matmul(P,factor)
        fac=[(1,0)]
        for u in range(1,n):fac.append(self.mul(fac[-1],self.add((1,0),self.neg(self.power(2*u)))))
        pv=[]
        for a in range(n):
            z=self.mul((n*(-1)**a,0),self.power(-d*d+a*(d-a-1)))
            z=self.mul(z,self.mul(self.mul(fac[a],fac[d-a]),self.inv(fac[d])))
            pv.append(z)
        cup=np.zeros((n,n),dtype=np.int64),np.zeros((n,n),dtype=np.int64)
        cap=np.zeros((n,n),dtype=np.int64),np.zeros((n,n),dtype=np.int64)
        for a in range(n):
            ell=self.inv(pv[d-a])
            for c in range(2):cup[c][a,d-a]=pv[a][c];cap[c][a,d-a]=ell[c]
        return O,P,cup,cap


def apply_pair(A,state,slot,N,p):
    s=np.moveaxis(state,(slot,slot+1),(0,1));shape=s.shape
    out=(A@s.reshape(N*N,-1))%p
    return np.moveaxis(out.reshape(shape),(0,1),(slot,slot+1))


def case(N,k):
    j=Jets(N);p,q,d=j.p,j.q,N-1;m=d//2
    O,E,cup,cap=j.operators()
    _,_,_,_,_,_,_,Rp,Rm=balanced_data(N)
    L=pair_circle(O[0],N,p)
    assert np.array_equal(L@L%p*pow(N*N,-1,p)%p,E[0])
    assert np.array_equal(L@E[0]%p,N*E[0]%p)
    W,*_=physical_columns(N,q,p);Wbar,*_=physical_columns(N,pow(q,-1,p),p)
    reverse=np.zeros((N*N,N*N),dtype=np.int64)
    for a in range(N):
        for b in range(N):reverse[b*N+a,a*N+b]=1
    pi=Wbar[m].T@reverse%p
    assert np.array_equal(pi@W[m]%p,np.eye(N,dtype=np.int64))
    assert np.array_equal(W[m]@pi%p,E[0])
    odd=list(range(1,2*k-2,2));even=list(range(0,2*k-1,2))
    boxes=odd+even+odd
    matching,free=plat_matching(k,boxes);assert free==0
    graph=cubic_dictionary(len(boxes),matching)
    state=(np.array([1],dtype=np.int64),np.array([0],dtype=np.int64))
    row=(np.array([1],dtype=np.int64),np.array([0],dtype=np.int64))
    mark=np.array([[pow(pow(q,d,p),b,p)*pow(N*N,-1,p)%p for b in range(N)] for a in range(N)],dtype=np.int64)
    marked=np.array([1],dtype=np.int64)
    for h in range(k):
        state=j.kron(state,(cup[0].reshape(-1),cup[1].reshape(-1)))
        row=j.kron(row,(cap[0].reshape(-1),cap[1].reshape(-1)))
        marked=np.kron(marked,(mark if h==k-1 else cap[0]).reshape(-1))%p
    s0=state[0].reshape((N,)*(2*k));s1=state[1].reshape((N,)*(2*k))
    split=s0.copy()
    for slot in boxes:
        s1=(apply_pair(E[0],s1,slot,N,p)+apply_pair(E[1],s0,slot,N,p))%p
        s0=apply_pair(E[0],s0,slot,N,p)
        # An independent open matching-edge sum, not projector lookup.
        work=np.moveaxis(split,(slot,slot+1),(0,1));shape=work.shape
        channel=pi@work.reshape(N*N,-1)%p
        split=np.moveaxis((W[m]@channel%p).reshape(shape),(0,1),(slot,slot+1))
    assert np.array_equal(s0,split)
    value=int(marked@s0.reshape(-1)%p)
    F0=int(row[0]@s0.reshape(-1)%p)
    F1=int((row[1]@s0.reshape(-1)+row[0]@s1.reshape(-1))%p)
    nu=2*N*(-1)**N*pow((q-pow(q,-1,p))%p,-1,p)%p
    assert F0==0 and F1==nu*value%p
    omega=int(Rp[0,0])*pow(-1,m,p)*pow(q,m*(m+1),p)%p
    signs=[(-1,0,1)[i%3] for i in range(len(boxes))]
    actual=state[0].reshape((N,)*(2*k))
    for slot,sign in zip(boxes,signs):
        B=L@E[0]%p
        if sign:B=(Rp if sign>0 else Rm)@B%p
        actual=apply_pair(B,actual,slot,N,p)
    physical=int(marked@actual.reshape(-1)%p)
    predicted=pow(N,len(boxes),p)*pow(omega,sum(signs),p)*value%p
    assert physical==predicted
    return {'N':N,'plat_width':k,'crossing_disks':len(boxes),
            'all_oriented_Delta_faces_match':graph['all_oriented_medial_faces_match'],
            'split_endpoint_graph':True,'original_first_normal':True,
            'signed_original_endpoint_scalar':physical}

if __name__=='__main__':
    rows=[case(N,k) for N,k in [(3,2),(3,3),(3,4),(5,2),(5,3),(7,2)]]
    result={'status':'PASS','cases':rows,'scope':'Odd endpoint contribution only; original mark, generic first derivative and matching graph retained. No positivity/dominance or even-level claim.'}
    Path(__file__).with_name('general_odd_endpoint_matching_network_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS6 original odd endpoint plat contractions, full matching-edge split and normalized first trace jets')
