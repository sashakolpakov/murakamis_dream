#!/usr/bin/env python3
"""Original full-channel sources and positive/CD-weighted Cauchy Grams."""

import json
from pathlib import Path

import mpmath as mp
import numpy as np
import sympy as sp

from audit_actual_two_cut_ports import balanced_data,coproduct,word_matrix
from audit_actual_complete_casimir_hermite_packet import canonical_field_frame


def exact_original_source():
    rows=[]
    for N in range(2,10):
        p,eta,q,E,F,K,pivot,Rp,Rm=balanced_data(N)
        Q,d,x,rho=q*q % p,N-1,int(K[0,0]),(q-pow(q,-1,p)) % p
        Ecal=rho*rho*E % p
        E2,F2,K2=coproduct(Ecal,F,K,2,N,p)
        K2i=np.diag([pow(int(z),-1,p) for z in np.diag(K2)])
        O=(F2@E2+q*K2+pow(q,-1,p)*K2i) % p
        ids=[u*N+d-u for u in range(N)]
        V,Vi,meta,blocks=canonical_field_frame(O[np.ix_(ids,ids)],N,d,p,q)
        fac=[1]
        for j in range(1,N):fac.append(fac[-1]*(1-pow(Q,j,p)) % p)
        seed=np.zeros((N*N,N),dtype=np.int64)
        seed[ids,np.arange(N)]=1
        power=seed.copy();J=np.zeros((N,N),dtype=np.int64)
        for c in range(N):
            i=d-c
            J[i,:]=pow(-x*Q,c,p)*pow(fac[c],-1,p)*power[i,:] % p
            power=E2@power % p
        Ji=np.array(sp.Matrix(J.tolist()).inv_mod(p)).astype(np.int64)
        cup=np.array([N*pow(x,u-d,p) % p for u in range(N)],dtype=np.int64)
        ell=np.array([pow(x,-u,p)*pow(Q,-u,p)*pow(N,-1,p) % p for u in range(N)])
        endpoint=np.zeros(N,dtype=np.int64);endpoint[d]=N*pow(x,-d,p) % p
        assert np.array_equal(J@cup % p,endpoint)
        leftendpoint=np.zeros(N,dtype=np.int64);leftendpoint[0]=pow(x,d,p)*pow(N,-1,p) % p
        assert np.array_equal(ell@Ji % p,leftendpoint)
        incoming=Vi@J % p@cup % p
        outgoing=ell@Ji % p@V % p
        expect_in=[];expect_out=[]
        for block in blocks:
            j=block['j'];c=(pow(q,2*j+1,p)+pow(q,-2*j-1,p)) % p
            if block['multiplicity']==2:
                phase=N*pow(-1,d,p)*pow(x,-d,p) % p
                expect_in += [-phase*c % p,phase*(4-c*c) % p]
                expect_out += [pow(x,d,p)*pow(N,-1,p) % p,0]
            else:
                expect_in += [N*pow(x,-d,p) % p]
                expect_out += [pow(x,d,p)*pow(N,-1,p) % p]
        assert np.array_equal(incoming,np.array(expect_in,dtype=np.int64))
        assert np.array_equal(outgoing,np.array(expect_out,dtype=np.int64))
        assert int(outgoing@incoming) % p == 0
        words=[]
        if N<=5:
            cup_physical=np.zeros(N*N,dtype=np.int64);cup_physical[ids]=cup
            cap_physical=np.zeros(N*N,dtype=np.int64);cap_physical[ids]=ell
            R12=Rp[np.ix_(ids,ids)];I12=Rm[np.ix_(ids,ids)]
            R23=Ji@R12 % p@J % p;I23=Ji@I12 % p@J % p
            for word in ([2,-1,2,2],[2,2,2],[1,2,-1,-2,2]):
                W=np.eye(N,dtype=np.int64)
                for a in word:
                    W=({1:R12,-1:I12,2:R23,-2:I23}[a])@W % p
                cut=(np.kron(cap_physical.reshape(1,-1),np.eye(N,dtype=np.int64))
                     @word_matrix(word,Rp,Rm,3,N,p) % p
                     @np.kron(cup_physical.reshape(-1,1),np.eye(N,dtype=np.int64))) % p
                scalar=int(ell@W % p@cup) % p
                assert np.array_equal(cut,scalar*np.eye(N,dtype=np.int64) % p)
                Wch=Vi@J % p@W % p@Ji % p@V % p
                assert int(outgoing@Wch % p@incoming) % p == scalar
                if word==[2,-1,2,2]:
                    figure=sum(pow(-1,n,p)*pow(Q,-n*(n+1)//2,p)*fac[n]**2 for n in range(N)) % p
                    assert scalar==figure
                words.append({'chronological_word':word,'original_full_Cartan_open_cut':True})
        rows.append({'N':N,'actual_coproduct_J_endpoints_and_full_CD_source':True,
                     'both_Hermite_types_and_odd_simple_channel':True,'full_original_words':words})
    return rows


def norm_source(N):
    q=mp.e**(mp.j*mp.pi/N);d=N-1;x=q**d
    source=[];cap=[];weights=[]
    for j in range(N//2):
        c=2*mp.cos((2*j+1)*mp.pi/N);a2=4-c*c
        phase=N*(-1)**d*x**(-d)
        source.extend([-phase*c,phase*a2]);cap.extend([x**d/N,mp.mpc(0)])
        weights.extend([1/a2,1/a2])
    if N%2:
        source.append(N*x**(-d));cap.append(x**d/N);weights.append(mp.mpf(1))
    assert len(source)==N
    SI=mp.fsum(abs(a)**2 for a in source);TI=mp.fsum(abs(a)**2 for a in cap)
    SD=mp.fsum(t*abs(a)**2 for t,a in zip(weights,source))
    TD=mp.fsum(abs(a)**2/t for t,a in zip(weights,cap))
    return source,cap,weights,SI,TI,SD,TD


def positive_norm_checks():
    mp.mp.dps=85;rows=[]
    for N in list(range(2,33))+[48,64,96,128,192,256]:
        u,b,D,SI,TI,SD,TD=norm_source(N)
        SIexpected=(64 if N==2 else 192 if N==4 else
                    N*N*(4*N-1) if N%2 else 4*N**3)
        SDexpected=(mp.mpf(16) if N==2 else mp.mpf(N*N)*(N*N+3*N+8)/6 if N%2
                    else mp.mpf(N**4)/4+mp.mpf(N**3)/2)
        TDexpected=mp.mpf(1) if N==2 else mp.mpf(N+1)/(N*N) if N%2 else mp.mpf(1)/N
        assert abs(SI/SIexpected-1)<mp.mpf('1e-65')
        assert abs(TI/(mp.mpf((N+1)//2)/(N*N))-1)<mp.mpf('1e-65')
        assert abs(SD/SDexpected-1)<mp.mpf('1e-65')
        assert abs(TD/TDexpected-1)<mp.mpf('1e-65')
        assert SI*TI<=4*N*N*(1+mp.mpf('1e-65'))
        assert SD*TD<=2*N**3*(1+mp.mpf('1e-65'))
        assert abs(mp.fsum(a*c for a,c in zip(u,b)))<mp.mpf('1e-60')
        assert min(D)>=mp.mpf(1)/4*(1-mp.mpf('1e-65'))
        assert max(D)<=max(1,mp.mpf(N*N)/16)*(1+mp.mpf('1e-65'))
        rows.append({'N':N,'unweighted_source_squared_norm':float(SI),
                     'unweighted_cap_squared_dual_norm':float(TI),
                     'CD_source_squared_norm':float(SD),'CD_cap_squared_dual_norm':float(TD),
                     'balanced_unweighted_exact_cap_factor':float(N*TI),
                     'balanced_CD_exact_cap_factor':float(N*TD)})
    return rows


def explicit_positive_Grams():
    mp.mp.dps=85;rows=[]
    for N in (2,3,4,6,9,12):
        q=mp.e**(mp.j*mp.pi/N);Q=q*q;d=N-1;x=q**d
        F=[mp.mpc(1)]
        for j in range(1,N):F.append(F[-1]*(1-Q**j))
        A=mp.zeros(N)
        for u in range(N):
            A[u,u]=q+1/q-q*(1-Q**u)**2-(1-Q**(u+1))**2/q
            if u<d:A[u,u+1]=A[u+1,u]=-(1-Q**(u+1))**2
        columns=[]
        for j in range((N+1)//2):
            c=2*mp.cos((2*j+1)*mp.pi/N)
            f=[mp.mpc(1)];df=[mp.mpc(0)]
            for u in range(d):
                f.append(((c-A[u,u])*f[u]-(A[u-1,u]*f[u-1] if u else 0))/A[u,u+1])
                df.append((f[u]+(c-A[u,u])*df[u]-(A[u-1,u]*df[u-1] if u else 0))/A[u,u+1])
            columns.append(f)
            if j!=d-j:columns.append(df)
        V=mp.matrix([[columns[j][i] for j in range(N)] for i in range(N)])
        Vi=V**-1
        J=mp.zeros(N)
        for i in range(N):
            for j in range(N-i):
                choose=F[d-j]/(F[i]*F[d-i-j])
                J[i,j]=(-x*Q)**(d-i)*x**j*Q**(i*(i+1)//2-d*(d+1)//2)*choose
        Ji=J**-1;S=Vi*J
        cup=mp.matrix([N*x**(u-d) for u in range(N)])
        ell=mp.matrix([[x**(-u)*Q**(-u)/N for u in range(N)]])
        uu,bb,weights,SI,TI,SD,TD=norm_source(N)
        assert mp.norm(S*cup-mp.matrix(uu))<mp.mpf('1e-55')*max(1,mp.sqrt(SI))
        assert mp.norm(ell*Ji*V-mp.matrix([bb]))<mp.mpf('1e-55')
        for kind,D,src,cap in (('unweighted',mp.eye(N),SI,TI),('CD',mp.diag(weights),SD,TD)):
            G=S.H*D*S/N
            Gi=N*Ji*V*(D**-1)*V.H*Ji.H
            mp.cholesky((G+G.H)/2)
            actualsrc=(cup.H*G*cup)[0];actualcap=(ell*Gi*ell.H)[0]
            assert abs(actualsrc/(src/N)-1)<mp.mpf('1e-50')
            assert abs(actualcap/(N*cap)-1)<mp.mpf('1e-50')
        rows.append({'N':N,'two_full_rank_positive_Grams':True,
                     'physical_right_channel_coordinates_checked':True,
                     'original_balanced_source_and_cap_norms':True})
    return rows


if __name__=='__main__':
    result={'status':'PASS','original_coproduct_sources':exact_original_source(),
            'closed_source_norms':positive_norm_checks(),'explicit_positive_Grams':explicit_positive_Grams()}
    Path(__file__).with_name('actual_complete_channel_positive_gram_results.json').write_text(
        json.dumps(result,indent=2)+'\n')
    print('PASS: 8 actual source levels/12 original cut words,37 all-N norm profiles,6 pairs of full positive Grams')
