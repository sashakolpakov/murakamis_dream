#!/usr/bin/env python3
"""Shared face frames for the actual recoupling and standard matrix kernel.

Difference roots are shared on edges. The induced face pairing and
cyclic map are compared with parameter-independent Gaussian matrices;
all their actual scalar lines and ordered Weyl insertions are retained.
No full charged topological invariant or volume theorem is asserted.
"""

from itertools import permutations,product
from functools import cache
import json
from pathlib import Path

import numpy as np
import sympy as sp

from audit_actual_peripheral_fusion import inverse_mod
from audit_cyclic_steinberg_lattice import determinant
from audit_oriented_tetrahedron_source import Configuration,scalar_ratio
from audit_regular_holonomy_braiding import mm
from audit_standard_matrix_dilog_comparison import basic_kernel,evaluation,primitive


def configuration(N):
    for multiple in range(10,1000):
        p=12*N*multiple+1
        if not sp.isprime(p):continue
        roots={pow(a,N,p):a for a in range(1,p)};R=set(roots)
        candidates=sorted(v for v in R if v!=1 and (1-v)%p in R)
        found=None
        for aidx,a in enumerate(candidates):
            compatible=[b for b in candidates[aidx+1:] if (a-b)%p in R]
            for bidx,b in enumerate(compatible):
                c=next((c for c in compatible[bidx+1:] if (b-c)%p in R),None)
                if c is not None:found=[1,a,b,c];break
            if found is not None:break
        if found is None:continue
        cfg=object.__new__(Configuration);cfg.N=N;cfg.p=p
        generator=int(sp.primitive_root(p));cfg.generator=generator
        cfg.q=pow(generator,(p-1)//(2*N),p);cfg.Q=cfg.q*cfg.q%p
        cfg.tau=pow(generator,(p-1)//(3*N),p)
        cfg.points=found;cfg.flags=[roots[v] for v in found];cfg.marks={};B={}
        for i,j in product(range(4),repeat=2):
            if i<j:
                cfg.marks[i,j]=1;cfg.marks[j,i]=pow(cfg.Q,-1,p)
                B[i,j]=roots[(found[i]-found[j])%p];B[j,i]=cfg.q*B[i,j]%p
        cfg.flip=np.zeros((N*N,N*N),dtype=np.int64)
        for i,j in product(range(N),repeat=2):cfg.flip[j*N+i,i*N+j]=1
        return cfg,B
    raise AssertionError('no complete difference-root chart')


class FaceFrames:
    def __init__(self,cfg,B):self.cfg=cfg;self.B=B

    @cache
    def data(self,f):
        i,j,k=f;c=self.cfg;p=c.p
        beta=self.B[i,k]*pow(self.B[j,k],-1,p)%p
        rho=c.flags[j]*pow(c.flags[i],-1,p)*beta%p
        a=c.flags[k]*pow(c.flags[i],-1,p)*self.B[j,i]*pow(self.B[j,k],-1,p)%p
        phi=primitive(c.N,p,c.Q,rho,a)
        H=evaluation(c.N,p,c.Q,beta)
        G=H*np.array([pow(int(v),-1,p) for v in phi],dtype=np.int64)[:,None]%p
        return G,rho,a,phi

    def pairing(self,f):
        G=self.data(f)[0];Gr=self.data(f[::-1])[0];p=self.cfg.p
        return mm(p,inverse_mod(G,p).T,self.cfg.face(f),inverse_mod(Gr,p))

    def cyclic(self,f):
        r=f[1:]+f[:1];p=self.cfg.p
        return mm(p,self.data(r)[0],self.cfg.corrected_rotation(f),inverse_mod(self.data(f)[0],p))


def pure_pairing(cfg,B,f):
    i,j,k=f;N=cfg.N;p=cfg.p;Q=cfg.Q
    edge_ratio=B[k,i]*pow(B[i,k],-1,p)%p
    phase=-pow(edge_ratio,-1,p)%p
    return np.array([[pow(Q,b,p)*pow(phase,(a-b)%N,p)
                      *pow(Q,((a-b)%N)*(((a-b)%N)+1)//2,p)%p
                      for b in range(N)] for a in range(N)],dtype=np.int64)


def pure_cyclic(cfg,B,f):
    i,j,k=f;N=cfg.N;p=cfg.p;Q=cfg.Q
    rik=B[k,i]*pow(B[i,k],-1,p)%p;rjk=B[k,j]*pow(B[j,k],-1,p)%p
    c=-Q*rik%p;d=Q*rik*pow(rjk,-1,p)%p
    return np.array([[pow(d,-a,p)*pow(c,-b,p)*pow(Q,a*b+b*(b+1)//2,p)%p
                      for b in range(N)] for a in range(N)],dtype=np.int64)


def case(N):
    cfg,B=configuration(N);frames=FaceFrames(cfg,B);p=cfg.p;Q=cfg.Q
    roots={pow(Q,j,p):j for j in range(N)};gauss=-cfg.q%p
    faces=[]
    for f in permutations(range(4),3):
        M=frames.pairing(f);V=frames.cyclic(f)
        MG=pure_pairing(cfg,B,f);VG=pure_cyclic(cfg,B,f)
        mu=scalar_ratio(M,MG,p);xi=scalar_ratio(V,VG,p)
        assert mu and xi and determinant(MG,p) and determinant(VG,p)
        # These are full source-normalized scalars, not independently chosen roots.
        faces.append({'face':list(f),'pairing_scalar':mu,'cyclic_scalar':xi})
    tetrahedra=[]
    Z=np.diag([pow(Q,j,p) for j in range(N)]).astype(np.int64)
    S=np.zeros((N,N),dtype=np.int64)
    for j in range(N):S[(j+1)%N,j]=1
    for tet in permutations(range(4)):
        i,j,k,l=tet
        A,Bf,C,D=(i,k,l),(i,j,k),(i,j,l),(j,k,l)
        GA,rhoA,aA,_=frames.data(A);GB,rhoB,aB,phiB=frames.data(Bf)
        GC,alpha,aC,_=frames.data(C);GD,beta,aD,_=frames.data(D)
        assert rhoA==alpha*beta%p
        gamma=aA*pow(aD,-1,p)%p;v=aC*pow(aA,-1,p)%p;u=alpha*pow(gamma,-1,p)%p
        e=roots[gamma*pow(rhoB,-1,p)%p]
        d=roots[-gauss*gamma*beta*v*pow(aB,-1,p)%p]
        rik=B[k,i]*pow(B[i,k],-1,p)%p
        rjk=B[k,j]*pow(B[j,k],-1,p)%p
        assert pow(Q,e,p)==rik*pow(rjk,-1,p)%p
        assert pow(Q,d,p)==cfg.q*pow(rjk,-1,p)%p
        pi,pj,pk,pl=(cfg.points[a] for a in tet)
        geometric_ratio=(pl-pj)*(pk-pi)*pow((pl-pi)*(pk-pj),-1,p)%p
        central_shape=pow(u,N,p)
        assert central_shape==pow(geometric_ratio,-1,p)
        value=1;terms=[1];eta=alpha*beta%p
        for degree in range(1,N):
            value=value*pow(gamma,-1,p)*(1-eta*pow(Q,degree,p))*pow(1-beta*pow(Q,degree,p),-1,p)%p
            terms.append(value)
        kappa=sum(terms)*pow(N,-1,p)%p;assert kappa
        L=basic_kernel(N,p,Q,u,v)
        # The relative input is a marked clock/shift charge.
        diagonal=np.diag([pow(Q,d*r,p) for r in range(N)]).astype(np.int64)
        shift=np.zeros_like(S)
        for r in range(N):shift[(r-e)%N,r]=1
        right=np.kron(mm(p,diagonal,shift),np.eye(N,dtype=np.int64))%p
        expected=mm(p,L,right)*kappa*int(phiB[e])%p
        actual=mm(p,np.kron(GC,GD),cfg.tetrahedron(tet),
                  np.kron(inverse_mod(GA,p),inverse_mod(GB,p)),cfg.flip)
        assert np.array_equal(actual,expected)
        tetrahedra.append({'ordering':list(tet),'relative_mark_shift_e':e,'relative_clock_charge_d':d,
                           'central_standard_shape':central_shape,'oriented_flag_cross_ratio':geometric_ratio,
                           'pointing_scalar_kappa':kappa,'extra_pointing_factor_phi_B_e':int(phiB[e]),
                           'exact_shared_face_standard_kernel_normal_form':True})
    return {'level':N,'prime':p,'flag_points':cfg.points,'face_scalars':faces,
            'all_face_pairings_and_cyclic_maps_are_fixed_gaussians_times_retained_scalars':True,
            'all_24_ordered_tetrahedron_standard_normal_forms':tetrahedra}


def main():
    records=[]
    for N in (2,3,4,5,6,9):
        records.append(case(N));print(f'N={N}: 24 Gaussian face pairings/cyclic maps and 24 ordered kernel normal forms passed',flush=True)
    result={'scope':'One globally shared face frame, actual scalar pairings and explicit Weyl charges for each ordered tetrahedron. This does not assert that vertex orderings define the same uncolored tensor or prove the selected global geometric period/norm.',
            'configurations':records}
    Path(__file__).with_name('standard_face_gluing_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS',flush=True)


if __name__=='__main__':main()
