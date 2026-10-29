#!/usr/bin/env python3
"""Exact cusp/quad/source tests, independent of source-normalization limits.

Finite fields use the unnormalized Fourier matrix W0=sqrt(N) W,
so every identity is checked without choosing a finite-field square root.
The all-N proofs are in cap_wall_fermat_quad_residue_transport.md.
"""

from itertools import product
import json
from pathlib import Path

import numpy as np
import sympy as sp
import mpmath as mp

from audit_actual_borel_regular_fusion import inv
from audit_cyclic_steinberg_lattice import rank
from audit_finite_sum_annihilator import field


def data(N,p_override=None):
    if p_override is None:p,g,q=field(N)
    else:
        p=p_override;g=int(sp.primitive_root(p));q=pow(g,(p-1)//(2*N),p)
    Q=q*q%p;gamma=-q%p
    Z=np.diag([pow(Q,n,p) for n in range(N)]).astype(np.int64)
    S=np.zeros((N,N),dtype=np.int64)
    for n in range(N):S[(n+1)%N,n]=1
    W=np.array([[pow(gamma,n,p)*pow(Q,k*n+n*(n+1)//2,p)%p
                 for n in range(N)] for k in range(N)],dtype=np.int64)
    F=[1]
    for n in range(1,N):F.append(F[-1]*(1-pow(Q,n,p))%p)
    return p,g,q,Q,gamma,Z,S,W,inv(W,p),F


def B(N,p,Z,S,u,v,w):
    return (w*np.eye(N,dtype=np.int64)-u*Z-v*S)%p


def frames(N,p,Q,u,v,w):
    col=[1];row=[1]
    for n in range(1,N):
        col.append(col[-1]*v*pow((w-u*pow(Q,n,p))%p,-1,p)%p)
        row.append(row[-1]*(w-u*pow(Q,n-1,p))*pow(v,-1,p)%p)
    return np.array(col,dtype=np.int64),np.array(row,dtype=np.int64)


def affine_points(N,p,maximum=24):
    powers={}
    for v in range(1,p):powers.setdefault(pow(v,N,p),[]).append(v)
    points=[]
    for u in range(1,p):
        for v in powers.get((1-pow(u,N,p))%p,[]):
            points.append((u,v,1))
            if len(points)>=maximum:return points
    return points


def generic_case(N):
    p,g,q,Q,gamma,Z,S,W,Wi,F=data(N);I=np.eye(N,dtype=np.int64)
    points=affine_points(N,p)
    # A small split field can have only cusps on a high-genus Fermat curve.
    while not points:
        p=int(sp.nextprime(p))
        while (p-1)%(2*N):p=int(sp.nextprime(p))
        p,g,q,Q,gamma,Z,S,W,Wi,F=data(N,p)
        points=affine_points(N,p)
    Zi=inv(Z,p)
    for u,v,w in points:
        target=(q*v%p,w,u)
        old=B(N,p,Z,S,u,v,w);new=B(N,p,Z,S,*target)
        assert rank(old,p)==N-1
        assert np.array_equal(new@W%p,-W@Zi@old%p)
        P,L=frames(N,p,Q,u,v,w);Pt,Lt=frames(N,p,Q,*target)
        assert not np.any(old@P%p)
        assert not np.any(L@old%p)
        A=int((W@P)[0])%p
        D=int((L@Z@Wi)[0])%p
        assert A and D
        assert np.array_equal(W@P%p,A*Pt%p)
        assert np.array_equal(L@Wi%p,D*Lt@S%p)
        # A non-factorized exterior tensor sees exactly the transported pairing.
        T=(Z+S+Z@S+np.outer(np.eye(N,dtype=np.int64)[:,0],
                           np.eye(N,dtype=np.int64)[-1,:]))%p
        old_pair=int(L@T@P)%p
        transported=int(D*Lt@S@(W@T@Wi%p)@(A*Pt%p))%p
        assert old_pair==transported
        lhs=A*D%p
        rhs=(w-u)*pow(w,N,p)*pow(pow(v,N,p)*(u-q*v)%p,-1,p)%p
        assert lhs==rhs
        power=1
        for j in range(1,N):
            factor=(1-pow(Q,j,p))*(u-q*v*pow(Q,j,p))\
                *pow((w-u*pow(Q,j,p))%p,-1,p)%p
            power=power*pow(factor,N-j,p)%p
        assert pow(A,N,p)==power,(N,u,v,pow(A,N,p),power)
        # The co-source is not generally the unshifted target left kernel.
        if not np.array_equal(L@Wi%p,D*Lt%p):
            assert np.any(L@Wi@new%p)
    return {'N':N,'prime':p,'generic_points':len(points),
            'polynomial_intertwining':True,'dual_shift':True,
            'whole_paired_scalar':True,'exact_Nth_power':True}


def cusp_case(N):
    p,g,q,Q,gamma,Z,S,W,Wi,F=data(N);d=N-1;Zi=inv(Z,p)
    corners=[]
    for j in range(N):
        u=pow(Q,-j,p)
        e=np.zeros(N,dtype=np.int64);e[j]=1
        old=B(N,p,Z,S,u,0,1)
        assert rank(old,p)==d
        assert not np.any(old@e%p) and not np.any(e@old%p)
        target=(0,1,u)
        new=B(N,p,Z,S,*target)
        assert np.array_equal(new@W%p,-W@Zi@old%p)
        targetP=np.array([pow(Q,j*n,p) for n in range(N)],dtype=np.int64)
        targetL=np.array([pow(Q,-j*n,p) for n in range(N)],dtype=np.int64)
        aj=pow(gamma,j,p)*pow(Q,j*(j+1)//2,p)%p
        assert np.array_equal(W@e%p,aj*targetP%p)
        assert np.array_equal(e@Wi%p,pow(N*aj%p,-1,p)*targetL%p)
        assert np.array_equal(e@Wi%p,
            (pow(Q,j,p)*pow(N*aj%p,-1,p))*targetL@S%p)
        alpha=beta=1
        if j:
            alpha=N*pow(-1,j-1,p)*pow(Q,j*(j-1)//2,p)*pow(F[j-1],-1,p)%p
            beta=pow(-1,j,p)*pow(Q,-j*(j+1)//2,p)*F[j]%p
            assert alpha*beta%p==N*(1-pow(Q,-j,p))%p
        # Exact leading orders follow from delta(v)=1-v^N/N+O(v^(2N)).
        # Multiplying by the stated residue monomial leaves only component j.
        colres=np.zeros(N,dtype=np.int64);rowres=np.zeros(N,dtype=np.int64)
        for n in range(N):
            cp=rp=1
            czero=(j>=1 and n>=j)
            rzero=(n>j)
            for a in range(1,n+1):
                if a!=j:cp=cp*(1-pow(Q,a-j,p))%p
            for a in range(n):
                if a!=j:rp=rp*(1-pow(Q,a-j,p))%p
            cord=n-N*czero
            rord=-n+N*rzero
            clead=(N if czero else 1)*pow(cp,-1,p)%p
            rlead=rp*(pow(N,-1,p) if rzero else 1)%p
            cpow=N-j-1 if j else -1
            rpow=j-1 if j else -1
            assert cord+cpow>=-1 and rord+rpow>=-1
            if cord+cpow==-1:colres[n]=clead
            if rord+rpow==-1:rowres[n]=rlead
        assert np.array_equal(colres%p,alpha*e%p)
        assert np.array_equal(rowres%p,beta*e%p)
        corners.append({'j':j,'column_residue_normalization':int(alpha),
                        'row_residue_normalization':int(beta)})
    assert corners[d]['column_residue_normalization']==(1-Q)%p
    assert corners[d]['row_residue_normalization']==N%p
    # All 3N cusps, including the points at infinity, have exactly corank one.
    for j in range(N):
        for u,v,w in ((0,pow(Q,j,p),1),(q*pow(Q,j,p)%p,1,0)):
            old=B(N,p,Z,S,u,v,w)
            new=B(N,p,Z,S,q*v%p,w,u)
            assert rank(old,p)==d
            assert np.array_equal(new@W%p,-W@Zi@old%p)
    return {'N':N,'all_projective_cusps':3*N,'even_level':N%2==0,
            'all_corner_residues':corners,'cap_alpha_is_one_minus_Q':True,
            'cap_beta_is_N':True}


def tensor_residue_case(N,k):
    """The independently proved head residues select every tensor entry."""
    p,*_=data(N);d=N-1
    # A generic non-factorized tensor, evaluated by coefficient contraction.
    # Normalized residues are the exact basis rows/columns established above.
    incoming=(d,0)*k
    outgoing=(d,0)+(0,d)*(k-1)
    def coefficient(row,col):
        value=7
        for j,(a,b) in enumerate(zip(row,col)):
            value=(value+(j+1)*(a+2)*(b+3)+a*b*b)%p
        return value
    literal=coefficient(outgoing,incoming)
    # Every head residue has support only at its specified corner.
    column=[np.eye(N,dtype=np.int64)[:,j] for j in incoming]
    row=[np.eye(N,dtype=np.int64)[j,:] for j in outgoing]
    result=0
    for a in product(range(N),repeat=2*k):
        ca=1
        for vec,n in zip(column,a):ca*=int(vec[n])
        if not ca:continue
        for b in product(range(N),repeat=2*k):
            cb=1
            for vec,n in zip(row,b):cb*=int(vec[n])
            if cb:result=(result+ca*cb*coefficient(b,a))%p
    assert literal==result
    return {'N':N,'bridges':k,'number_of_independent_residues':4*k,
            'generic_tensor_corner':literal,'residue_contraction':result}


def micro_collar_cases():
    mp.mp.dps=70
    results=[]
    for N in (2,3,4,8,16,32,64):
        Q=mp.exp(2j*mp.pi/N);q=mp.exp(1j*mp.pi/N);gamma=-q
        v=mp.exp(mp.mpf('.37')*1j)/(16*N)
        # Preserve the tiny zero factor explicitly, without subtractive loss.
        h=-mp.expm1(mp.log1p(-v**N)/N);delta=1-h
        for j in sorted({0,N//2,N-1}):
            u=Q**(-j)*delta
            P=[mp.mpc(1)];L=[mp.mpc(1)]
            for n in range(1,N):
                denominator=h if j>=1 and n==j else 1-delta*Q**(n-j)
                numerator=h if n-1==j else 1-delta*Q**(n-1-j)
                P.append(P[-1]*v/denominator)
                L.append(L[-1]*numerator/v)
            if j:
                alpha=N/mp.fprod(1-Q**(r-j) for r in range(1,j))
                beta=mp.fprod(1-Q**(r-j) for r in range(j))
                P=[v**(N-j)*a/alpha for a in P]
                L=[v**j*a/beta for a in L]
            pn=mp.sqrt(mp.fsum(abs(a)**2 for a in P))
            ln=mp.sqrt(mp.fsum(abs(a)**2 for a in L))
            chirp=[gamma**n*Q**(n*(n+1)//2) for n in range(N)]
            c=mp.fsum(chirp[n]*P[n] for n in range(N))/mp.sqrt(N)
            e=mp.fsum(mp.conj(chirp[n])*L[n] for n in range(N))\
                /(mp.sqrt(N)*(u-q*v))
            cs=abs(c)*mp.sqrt(N);es=abs(e)*mp.sqrt(N)
            assert mp.mpf('.25')<min(pn,ln,cs,es)
            assert max(pn,ln,cs,es)<4
            results.append({'N':N,'cusp':j,'normalized_column_norm':float(pn),
                'normalized_row_norm':float(ln),'sqrt_N_times_c':float(cs),
                'sqrt_N_times_dual_coefficient':float(es)})
    return results


if __name__=='__main__':
    result={'scope':'exact projective cyclic source and all actual corner boundaries; '
                    'no geometric crossing factorization or volume claim',
            'generic':[generic_case(N) for N in range(2,12)],
            'cusps':[cusp_case(N) for N in range(2,12)],
            'tensor_sources':[tensor_residue_case(N,k) for N in (2,3,4) for k in (1,2,3)],
            'micro_collar_norm_diagnostics':micro_collar_cases()}
    path=Path(__file__).with_name('cap_wall_fermat_quad_residue_results.json')
    path.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS',sum(x['generic_points'] for x in result['generic']),
          'generic Fermat points;',sum(x['all_projective_cusps'] for x in result['cusps']),
          'projective cusps;',len(result['tensor_sources']),'full tensor sources;',
          len(result['micro_collar_norm_diagnostics']),'source norm diagnostics')
