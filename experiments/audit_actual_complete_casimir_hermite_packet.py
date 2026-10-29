#!/usr/bin/env python3
"""Complete actual Casimir/Hermite frames, inverse measure and q-Hahn sums."""

import json
from pathlib import Path

import mpmath as mp
import numpy as np

from audit_actual_two_cut_ports import balanced_data


def canonical_field_frame(O,N,T,p,q):
    Q,d,x = q*q % p,N-1,pow(q,N-1,p)
    D = [int(O[u,u]) for u in range(T+1)]
    A = [int(O[u,u+1]) for u in range(T)]
    assert all(A)
    B = 1
    for a in A:B=B*a % p
    fac=[1]
    for u in range(1,N):fac.append(fac[-1]*(1-pow(Q,u,p)) % p)
    # Independent literal product identity B=Q^{-T(T+1)/2}F_T^2.
    assert B == pow(Q,-T*(T+1)//2,p)*fac[T]*fac[T] % p
    nodes=[(pow(q,2*j+1,p)+pow(q,-2*j-1,p)) % p for j in range(T+1)]
    groups={}
    for j,c in enumerate(nodes):groups.setdefault(c,[]).append(j)
    columns=[];gram=np.zeros((T+1,T+1),dtype=np.int64)
    meta=[];blocks=[]
    for c,indices in groups.items():
        vals=[1];ders=[0];prod=1
        old,cur,do,dc=0,1,0,0
        for u in range(T):
            nxt=((c-D[u])*cur-(A[u-1]**2*old if u else 0)) % p
            dn=(cur+(c-D[u])*dc-(A[u-1]**2*do if u else 0)) % p
            prod=prod*A[u] % p
            vals.append(nxt*pow(prod,-1,p) % p)
            ders.append(dn*pow(prod,-1,p) % p)
            old,cur,do,dc=cur,nxt,dc,dn
        residual=((c-D[T])*cur-(A[T-1]**2*old if T else 0)) % p
        dr=(cur+(c-D[T])*dc-(A[T-1]**2*do if T else 0)) % p
        assert residual==0
        if len(indices)==2:assert dr==0
        j=indices[0]
        nu=pow(-1,j,p)*pow(q,j*(j+1),p) % p
        others=[nodes[k] for k in range(T+1) if k not in indices]
        quotient=1
        for a in others:quotient=quotient*(c-a) % p
        sigma=pow(x,T,p)*nu*quotient*pow(B,-1,p) % p
        k=len(columns)
        columns.append(vals);meta.append((j,'value'))
        if len(indices)==1:
            gram[k,k]=sigma
            blocks.append({'j':j,'multiplicity':1,'sigma':sigma,'eta':None})
        else:
            h=2*j+1
            jet=(-nu*(d-2*j)*pow(2*(pow(q,h,p)-pow(q,-h,p)) % p,-1,p)) % p
            eta=(jet*pow(nu,-1,p)+sum(pow(c-a,-1,p) for a in others)) % p
            columns.append(ders);meta.append((j,'derivative'))
            gram[k,k+1]=gram[k+1,k]=sigma
            gram[k+1,k+1]=sigma*eta % p
            blocks.append({'j':j,'multiplicity':2,'sigma':sigma,'eta':eta})
    V=np.array(columns,dtype=np.int64).T
    assert np.array_equal(V.T@V % p,gram)
    Ki=np.zeros_like(gram);col=0
    for b in blocks:
        si=pow(b['sigma'],-1,p)
        if b['multiplicity']==1:
            Ki[col,col]=si;col+=1
        else:
            Ki[col,col]=-b['eta']*si % p
            Ki[col,col+1]=Ki[col+1,col]=si
            col+=2
    Vi=Ki@V.T % p
    assert np.array_equal(Vi@V % p,np.eye(T+1,dtype=np.int64))
    assert np.array_equal(V@Vi % p,np.eye(T+1,dtype=np.int64))
    return V,Vi,meta,blocks


def root_qhahn(fac,p,Q,x,T,j,u):
    def binom(n,k):
        if min(k,n-k)<0:return 0
        return fac[n]*pow(fac[k]*fac[n-k] % p,-1,p) % p
    r=T-j
    total=0
    for a in range(max(0,u-r),min(j,u)+1):
        total+=(pow(-1,a,p)*pow(x,-(r-u+2*a),p)
                *pow(Q,a*(a-1)//2+a*(r-u+a),p)
                *binom(j,a)*binom(u,a)*binom(T-u,j-a))
    return pow(x,r,p)*pow(binom(T,j),-1,p)*total % p


def literal_complete_checks():
    rows=[];small=[]
    for N in range(2,13):
        p,eta,q,E,F,K,pivot,Rp,Rm=balanced_data(N)
        Q,d,x,rho=q*q % p,N-1,int(K[0,0]),(q-pow(q,-1,p)) % p
        fac=[1]
        for u in range(1,N):fac.append(fac[-1]*(1-pow(Q,u,p)) % p)
        I=np.eye(N,dtype=np.int64)
        Ki=np.diag([pow(int(z),-1,p) for z in np.diag(K)])
        Ft=(np.kron(F,I)+np.kron(Ki,F)) % p
        Et=(np.kron(rho*rho*E % p,K)+np.kron(I,rho*rho*E % p)) % p
        Kt=np.kron(K,K) % p
        O=(Ft@Et+q*Kt+pow(q,-1,p)*np.diag([pow(int(z),-1,p) for z in np.diag(Kt)])) % p
        frames={};count=0
        for T in range(d+1):
            ids=[u*N+T-u for u in range(T+1)]
            block=O[np.ix_(ids,ids)]
            assert np.array_equal(block,block.T)
            for u in range(T):
                v=T-u
                assert int(block[u,u+1])==pow(Q,-v,p)*(1-pow(Q,v,p))*(1-pow(Q,u+1,p)) % p
            V,Vi,meta,blocks=canonical_field_frame(block,N,T,p,q)
            for col,(j,kind) in enumerate(meta):
                if kind=='value':
                    for u in range(T+1):
                        assert int(V[u,col])==root_qhahn(fac,p,Q,x,T,j,u)
                        count+=1
            expected=np.zeros((T+1,T+1),dtype=np.int64);col=0
            for b in blocks:
                j=b['j'];nu=pow(-1,j,p)*pow(q,j*(j+1),p) % p
                expected[col,col]=nu
                if b['multiplicity']==2:
                    h=2*j+1
                    jet=-nu*(d-2*j)*pow(2*(pow(q,h,p)-pow(q,-h,p)) % p,-1,p) % p
                    expected[col,col+1]=jet;expected[col+1,col+1]=nu;col+=2
                else:col+=1
            kappa=int(Rp[0,0])
            assert np.array_equal(Vi@Rp[np.ix_(ids,ids)] % p@V % p,kappa*expected % p)
            neg=Vi@Rm[np.ix_(ids,ids)] % p@V % p
            assert np.array_equal(neg@(kappa*expected % p) % p,np.eye(T+1,dtype=np.int64))
            frames[T]=(V,Vi,meta)
            high=2*d-T
            highids=[(d-T+u)*N+d-u for u in range(T+1)]
            assert np.array_equal(O[np.ix_(highids,highids)],block)
            assert np.array_equal(Rp[np.ix_(highids,highids)],Rp[np.ix_(ids,ids)])
        # Every physical total degree retained in full pair frame.
        Vfull=np.zeros((N*N,N*N),dtype=np.int64);Ifull=np.zeros_like(Vfull)
        records=[];offset=0
        for T in range(2*d+1):
            low=min(T,2*d-T);shift=max(0,T-d)
            V,Vi,meta=frames[low]
            ids=[(shift+u)*N+T-shift-u for u in range(low+1)]
            cols=list(range(offset,offset+low+1))
            Vfull[np.ix_(ids,cols)]=V
            Ifull[np.ix_(cols,ids)]=Vi
            records.extend((T,j,kind) for j,kind in meta)
            offset+=low+1
        assert offset==N*N
        assert np.array_equal(Ifull@Vfull % p,np.eye(N*N,dtype=np.int64))
        cup=np.zeros(N*N,dtype=np.int64)
        ordinary=np.zeros(N*N,dtype=np.int64)
        marked=np.array([pow(x,b,p)*pow(N,-2,p) % p for a in range(N) for b in range(N)])
        for u in range(N):
            cup[u*N+d-u]=N*pow(x,u-d,p) % p
            ordinary[u*N+d-u]=pow(x,-u,p)*pow(Q,-u,p)*pow(N,-1,p) % p
        cupcoords=Ifull@cup % p
        ordinarycoords=ordinary@Vfull % p
        selected=[idx for idx,(T,j,kind) in enumerate(records) if T==d and j==0]
        assert len(selected)==2
        assert int(cupcoords[selected[0]])==N*pow(x,-d,p) % p
        assert all(not int(cupcoords[idx]) for idx in range(N*N) if idx!=selected[0])
        assert all(not int(ordinarycoords[idx]) for idx in range(N*N) if idx!=selected[1])
        assert int(ordinarycoords[selected[1]])
        assert np.array_equal((marked@Vfull % p)@Ifull % p,marked)
        if N<=5:
            actual=np.kron(np.eye(N,dtype=np.int64),Ifull)@np.kron(Vfull,np.eye(N,dtype=np.int64)) % p
            expected=np.zeros_like(actual)
            lookup={}
            for idx,(T,j,kind) in enumerate(records):lookup.setdefault(T,[]).append(idx)
            for pin,(T,j,kind) in enumerate(records):
                low=min(T,2*d-T);shift=max(0,T-d)
                for c in range(N):
                    for u in range(shift,shift+low+1):
                        b=T-u;Tp=b+c
                        value=int(Vfull[u*N+b,pin])
                        for pout in lookup[Tp]:
                            expected[u*N*N+pout,pin*N+c]=value*int(Ifull[pout,b*N+c]) % p
            assert np.array_equal(actual,expected)
            small.append({'N':N,'entire_adjacent_complete_channel_matrix':True})
        rows.append({'N':N,'all_low_blocks':d+1,'all_high_blocks_mirrored':True,
                     'complete_original_signed_R_and_derivative_blocks':True,
                     'literal_finite_Clebsch_entries':count})
    return rows,small


def positive_measure_checks():
    mp.mp.dps=80
    rows=[]
    for N in range(2,19):
        q=mp.e**(mp.j*mp.pi/N);Q=q*q;d=N-1
        s=[mp.mpf(1)]
        for a in range(1,N):s.append(s[-1]*2*mp.sin(mp.pi*a/N))
        count=0
        for T in range(d+1):
            nodes=[q**(2*j+1)+q**(-2*j-1) for j in range(T+1)]
            seen=set()
            for j,c in enumerate(nodes):
                if j in seen:continue
                l=d-j
                indices={j,l} if l!=j and 0<=l<=T else {j}
                seen.update(indices)
                direct=mp.fprod(abs(c-nodes[k]) for k in range(T+1) if k not in indices)/s[T]**2
                aj=abs(1-Q**(2*j+1))
                if len(indices)==2:
                    formula=N*s[T-j]*s[T+j-d]/(s[T]**2*aj**2)
                elif 2*j==d:
                    formula=N*s[T-j]**2/s[T]**2
                else:
                    assert j<d-T
                    formula=s[T-j]*s[T+j+1]/(s[T]**2*aj)
                assert abs(direct/formula-1)<mp.mpf('1e-60')
                if T==d:
                    special=1/aj**2 if len(indices)==2 else mp.mpf(1)
                    assert abs(formula/special-1)<mp.mpf('1e-60')
                count+=1
        rows.append({'N':N,'all_simple_double_selfpaired_measure_profiles':count,
                     'degree_d_polynomial_measure':True})
    return rows


def generic_clebsch(N,T,j,z):
    Q,x,d=z*z,z**(N-1),N-1
    F=[mp.mpc(1)]
    for a in range(1,N):F.append(F[-1]*(1-Q**a))
    def choose(n,k):
        if min(k,n-k)<0:return mp.mpc(0)
        return F[n]/(F[k]*F[n-k])
    highest=[]
    for a in range(j+1):
        highest.append((-1)**a*x**(-a)*Q**(a*(j-1)-a*(a-1)//2)
                       *F[N-j+a-1]/F[N-j-1]*F[d-a]/F[d])
    r=T-j;out=[]
    for u in range(T+1):
        total=mp.mpc(0)
        for a in range(max(0,u-r),min(j,u)+1):
            b=r-u+a
            total+=highest[a]*x**(-b)*Q**(a*b)*choose(u,a)*choose(T-u,j-a)
        out.append(total/(x**(-r)*choose(T,j)))
    return mp.matrix(out)


def generic_omega(N,T,z):
    d,Q,x=N-1,z*z,z**(N-1)
    M=-z**N;e=lambda a:M*Q**(-a)-1/M
    O=mp.zeros(T+1)
    for u in range(T+1):
        v=T-u
        O[u,u]=(e(u)*x*Q**(-v)*(1-Q**u)+e(v)/x*Q**u*(1-Q**v)
                 +z*x*x*Q**(-T)+1/z/x**2*Q**T)
        if u<T:O[u+1,u]=e(v)*(1-Q**(u+1))
        if u:O[u-1,u]=e(u)*Q**(u-v-1)*(1-Q**(v+1))
    return O


def generic_confluence_checks():
    mp.mp.dps=85
    rows=[]
    for N in (2,3,4,6,8):
        q=mp.e**(mp.j*mp.pi/N);d=N-1
        z=q*mp.exp(mp.mpf('.00013')+mp.j*mp.mpf('.00007'))
        count=0;pairs=0
        for T in range(d+1):
            O=generic_omega(N,T,z)
            for j in range(T+1):
                V=generic_clebsch(N,T,j,z)
                lam=z**(2*N-1-2*j)+z**(-2*N+1+2*j)
                assert mp.norm(O*V-lam*V)<mp.mpf('1e-55')*max(1,mp.norm(V))
                count+=1
            rootO=generic_omega(N,T,q)
            for j in range(T+1):
                l=d-j
                if not j<l<=T:continue
                c=q**(2*j+1)+q**(-2*j-1)
                val=[mp.mpc(1)];der=[mp.mpc(0)]
                for u in range(T):
                    A=rootO[u,u+1]
                    nxt=((c-rootO[u,u])*val[u]-(rootO[u-1,u]*val[u-1] if u else 0))/A
                    dn=(val[u]+(c-rootO[u,u])*der[u]-(rootO[u-1,u]*der[u-1] if u else 0))/A
                    val.append(nxt);der.append(dn)
                zz=q*mp.exp(mp.mpf('1e-18'))
                vj,vl=generic_clebsch(N,T,j,zz),generic_clebsch(N,T,l,zz)
                lj=zz**(2*N-1-2*j)+zz**(-2*N+1+2*j)
                ll=zz**(2*N-1-2*l)+zz**(-2*N+1+2*l)
                got=(vl-vj)/(ll-lj)
                want=mp.matrix(der)
                assert mp.norm(got-want)<mp.mpf('1e-9')*max(1,mp.norm(want))
                pairs+=1
        rows.append({'N':N,'generic_actual_Clebsch_eigenvectors':count,
                     'all_colliding_pairs_divided_differences':pairs})
    return rows


if __name__=='__main__':
    exact,adjacent=literal_complete_checks()
    result={'status':'PASS','original_complete_frames':exact,
            'full_adjacent_channels':adjacent,'positive_factorial_measures':positive_measure_checks(),
            'source_preserving_generic_q_confluence':generic_confluence_checks()}
    Path(__file__).with_name('actual_complete_casimir_hermite_packet_results.json').write_text(
        json.dumps(result,indent=2)+'\n')
    print('PASS: 11 complete frame/R/source levels, 4 FULL adjacent matrices, 17 measures, 5 all-pair q-confluences')
