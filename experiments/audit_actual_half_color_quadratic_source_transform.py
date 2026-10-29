#!/usr/bin/env python3
"""Finite odd-root quadratic collapse and ORIGINAL 4_1 simple channel."""

import json
from pathlib import Path

import numpy as np
import sympy as sp

from audit_finite_sum_annihilator import field
from audit_actual_two_cut_ports import balanced_data,coproduct
from audit_actual_complete_casimir_hermite_packet import canonical_field_frame


def finite_transform_checks():
    rows=[]
    for N in range(3,52,2):
        p,g,q=field(N);Q=q*q % p;m=(N-1)//2
        F=[1]
        for r in range(1,N):F.append(F[-1]*(1-pow(Q,r,p)) % p)
        def poch(a,k):
            out=1
            for j in range(k):out=out*(1-a*pow(Q,j,p)) % p
            return out
        def choose(n,k):return F[n]*pow(F[k]*F[n-k] % p,-1,p) % p
        chu=0
        for n in range(m+1):
            b=pow(g,3,p);c=pow(g,5,p)
            # Keep generic denominator outside the cyclic root subgroup.
            while any((1-c*pow(Q,j,p)) % p==0 for j in range(n)):
                c=c*g % p
            direct=sum(poch(pow(Q,-n,p),j)*poch(b,j)*pow(Q,j,p)
                       *pow(F[j]*poch(c,j) % p,-1,p) for j in range(n+1)) % p
            target=pow(b,n,p)*poch(c*pow(b,-1,p) % p,n)*pow(poch(c,n),-1,p) % p
            assert direct==target
            durfee=sum(pow(Q,r*r,p)*pow(F[r]*F[r]*F[n-r] % p,-1,p)
                       for r in range(n+1)) % p
            assert durfee==pow(F[n]*F[n] % p,-1,p)
            chu+=1
        a=pow(Q,-m,p)
        assert a==pow(Q,m+1,p)
        U=sum(pow(Q,t,p)*pow(poch(a,t),3,p)*pow(F[t]*F[t] % p,-1,p)
              for t in range(m+1)) % p
        S=sum(pow(Q,-k*(m-k),p)*choose(m,k)**2 for k in range(m+1)) % p
        expected=pow(-1,m,p)*pow(Q,-m*(3*m+1)//2,p)*S % p
        assert U==expected
        C=pow(-1,m,p)*pow(pow(q,N-1,p),-m,p)*pow(Q,m*(m+1)//2+1,p) % p
        raw=C*sum(pow(Q,m+t,p)*F[m+t]**3*pow(F[t]*F[t] % p,-1,p)
                  for t in range(m+1)) % p
        assert raw==F[m]**3*S % p
        rows.append({'N':N,'finite_qChu_and_Durfee_checks':chu,
                     'exact_odd_root_quadratic_and_all_phases':True})
    return rows


def actual_original_channel_checks():
    rows=[]
    for N in range(3,16,2):
        p,eta,q,E,F,K,pivot,Rp,Rm=balanced_data(N)
        Q,d,m,x,rho=q*q % p,N-1,(N-1)//2,int(K[0,0]),(q-pow(q,-1,p)) % p
        fac=[1]
        for j in range(1,N):fac.append(fac[-1]*(1-pow(Q,j,p)) % p)
        def choose(n,k):return fac[n]*pow(fac[k]*fac[n-k] % p,-1,p) % p
        E2,F2,K2=coproduct(rho*rho*E % p,F,K,2,N,p)
        K2i=np.diag([pow(int(z),-1,p) for z in np.diag(K2)])
        O=(F2@E2+q*K2+pow(q,-1,p)*K2i) % p
        ids=[a*N+d-a for a in range(N)]
        V,Vi,meta,blocks=canonical_field_frame(O[np.ix_(ids,ids)],N,d,p,q)
        simple=meta.index((m,'value'));f=V[:,simple]
        seed=np.zeros((N*N,N),dtype=np.int64);seed[ids,np.arange(N)]=1
        power=seed.copy();J=np.zeros((N,N),dtype=np.int64)
        for c in range(N):
            i=d-c
            J[i,:]=pow(-x*Q,c,p)*pow(fac[c],-1,p)*power[i,:] % p
            power=E2@power % p
        assert np.array_equal(J,J.T)
        Ji=np.array(sp.Matrix(J.tolist()).inv_mod(p)).astype(np.int64)
        R1=Rp[np.ix_(ids,ids)];R1i=Rm[np.ix_(ids,ids)]
        R2=Ji@R1 % p@J % p;kappa=int(Rp[0,0])
        assert kappa*kappa % p==pow(x,d,p)
        cup=np.array([N*pow(x,a-d,p) % p for a in range(N)],dtype=np.int64)
        ell=np.array([pow(x,-a,p)*pow(Q,-a,p)*pow(N,-1,p) % p for a in range(N)])
        h=R2@cup % p
        assert np.array_equal(h,np.array([kappa*int(cup[a])*fac[d-a] % p for a in range(N)]))
        v=R1i@h % p;y=J@f % p
        expected_y=[0]*m+[pow(Q,-r*(m-r),p)*choose(m,r)**2 % p for r in range(m+1)]
        assert np.array_equal(y,np.array(expected_y))
        for i in range(N):
            explicit=(pow(x,i-d,p)*pow(-1,i,p)*pow(Q,i*(i+1)//2-d,p)
                      *fac[d-i]*pow(fac[i],-1,p)
                      *sum(pow(Q,b,p)*fac[b]**3*pow(fac[b-i],-1,p) for b in range(i,d+1))) % p
            assert int(v[i])==explicit
        S=sum(expected_y) % p
        nu=pow(-1,m,p)*pow(q,m*(m+1),p) % p
        assert fac[m]*fac[m] % p==N*nu % p
        assert int(y@v) % p==N*nu*fac[m]*S % p
        W=R2@R2 % p@R1i % p@R2 % p
        z=Vi@J % p@W % p@cup % p
        target=N*pow(Q,m*(m+1),p)*fac[m]*S % p
        assert int(z[simple])==target
        positive_original=sum(pow(-1,n,p)*pow(Q,-n*(n+1)//2,p)*fac[n]**2 for n in range(N)) % p
        assert int(ell@W % p@cup) % p==positive_original
        rows.append({'N':N,'literal_original_positive_negative_R_and_coproduct_J':True,
                     'TRUE_fourplat_word':[2,-1,2,2],
                     'complete_simple_channel':int(z[simple]),'proved_formula':target,
                     'original_full_scalar_also_checked':True})
    return rows


if __name__=='__main__':
    result={'status':'PASS','finite_transforms':finite_transform_checks(),
            'complete_original_source_channel':actual_original_channel_checks()}
    Path(__file__).with_name('actual_half_color_quadratic_source_transform_results.json').write_text(
        json.dumps(result,indent=2)+'\n')
    print('PASS: 25 odd-root quadratic families, 7 complete ORIGINAL fourplat simple-channel families')
