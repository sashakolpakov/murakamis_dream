#!/usr/bin/env python3
"""Actual even paired-normal trivalent anchor and coherent weighted quartic.

Finite exact root fields retain the repeated eigenvector and Jordan chain;
separate principal-complex tests check the componentwise normal envelope.
"""
import itertools
import json
from pathlib import Path

import mpmath as mp
import numpy as np

from audit_actual_two_cut_ports import balanced_data,coproduct
from audit_actual_trivalent_complete_circle_vertex_kernel import vertex_formula


def factorials(N,q,p):
    Q=q*q%p;F=[1]
    for a in range(1,N):F.append(F[-1]*(1-pow(Q,a,p))%p)
    return F


def closed(N,q,p):
    m,j=N//2,N//2-1;d=N-1;Q=q*q%p;x=pow(q,d,p);F=factorials(N,q,p)
    W=np.zeros((N*N,2*j+1),dtype=np.int64)
    for r in range(2*j+1):
        for a in range(N):
            b=m+r-a
            if not 0<=b<N:continue
            z=0
            for s in range(max(0,a-r),min(m,a)+1):
                den=F[s]**2*F[m-s]**2*F[a-s]*F[r-a+s]%p
                z+=pow(q,s*s,p)*pow(x,-r+a-s,p)*pow(Q,s*(r-a+s),p)*pow(den,-1,p)
            W[a*N+b,r]=F[a]*F[b]*F[m]*z%p
    return W,F


def Jmatrix(N,q,p):
    d=N-1;Q=q*q%p;x=pow(q,d,p);F=factorials(N,q,p)
    out=np.zeros((N,N),dtype=np.int64)
    for a in range(N):
        for b in range(N-a):
            out[a,b]=pow(-x*Q,d-a,p)*pow(x,b,p)*pow(Q,(a*(a+1)-d*(d+1))//2,p)*F[d-b]*pow(F[a]*F[d-a-b],-1,p)%p
    return out


def circle(O,N,p):
    a,b=np.eye(len(O),dtype=np.int64),O.copy()
    for _ in range(2,N):a,b=b,(O@b-a)%p
    return (-1)**(N-1)*b%p


def axis(A,v,i,p):
    u=np.moveaxis(v,i,0)
    z=np.tensordot(A,u,axes=(1,0))%p
    return np.moveaxis(z,0,i)


def triple_action(v,kind,E,F,K,p):
    n=len(E);I=np.eye(n,dtype=np.int64)
    Ki=np.diag([pow(int(z),-1,p) for z in np.diag(K)])
    out=np.zeros_like(v)
    for k in range(3):
        z=v.copy()
        for i in range(3):
            A=(E if i==k else K if i>k else I) if kind=='E' else (F if i==k else Ki if i<k else I)
            z=axis(A,z,i,p)
        out=(out+z)%p
    return out


def field_case(N):
    p,eta,q,E,F,K,pivot,R,Ri=balanced_data(N)
    m,j,d=N//2,N//2-1,N-1;Q=q*q%p;x=pow(q,d,p)
    imag=pow(eta,N,p);half=pow(2,-1,p);rho=(q-pow(q,-1,p))%p
    sine=lambda a:(pow(q,a,p)-pow(q,-a,p))*pow(2*imag,-1,p)%p
    cosine=lambda a:(pow(q,a,p)+pow(q,-a,p))*half%p
    W,fac=closed(N,q,p);Wb,facb=closed(N,pow(q,-1,p),p)
    Ec=rho*rho*E%p;Et,Ft,Kt=coproduct(Ec,F,K,2,N,p)
    w=np.zeros(N*N,dtype=np.int64)
    for a in range(m+1):w[a*N+m-a]=pow(q,a*a,p)*fac[m]*pow(fac[a]*fac[m-a],-1,p)%p
    assert np.array_equal(W[:,0],w)
    for r in range(1,2*j+1):w=Ft@w%p*pow(1-pow(Q,r,p),-1,p)%p;assert np.array_equal(w,W[:,r])
    l=2*j+1
    EQ=np.zeros((l,l),dtype=np.int64);FQ=EQ.copy()
    KQ=np.diag([pow(q,2*j,p)*pow(Q,-r,p)%p for r in range(l)])
    for r in range(1,l):
        EQ[r-1,r]=pow(q,-2*j-1,p)*(1-pow(Q,2*j+1-r,p))%p
        FQ[r,r-1]=(1-pow(Q,r,p))%p
    for A,B in ((Et,EQ),(Ft,FQ),(Kt,KQ)):assert np.array_equal(A@W%p,W@B%p)
    P=np.zeros((N*N,N*N),dtype=np.int64)
    for a,b in itertools.product(range(N),repeat=2):P[a*N+b,b*N+a]=1
    assert not np.any(Wb.T@P%p@W%p)
    beta=np.array([sine(r+1)*pow(sine(1),-1,p)%p for r in range(l)],dtype=np.int64)
    h0=2*N*pow(sine(1),-1,p)%p # 4N/|1-Q| with |1-Q|=2sin(theta).
    for t in range(m+1):assert W[(j+t)*N+d-t,2*j]==pow(q,j,p)*W[t*N+m-t,0]%p
    assert W[d,j]==pow(q,-j*j,p)
    # Actual complete-circle first normal on EVERY degree of this image.
    nodes=(q+pow(q,-1,p))%p;c=-nodes%p
    for r in range(l):
        T=m+r;lo=max(0,T-d);hi=min(d,T);ids=[a*N+T-a for a in range(lo,hi+1)]
        O=(Ft[np.ix_(ids,range(N*N))]@Et[np.ix_(range(N*N),ids)]
           +q*Kt[np.ix_(ids,ids)]+pow(q,-1,p)*np.diag([pow(int(Kt[a,a]),-1,p) for a in ids]))%p
        Pb=np.eye(len(ids),dtype=np.int64)[::-1]
        L=circle(O,N,p)
        central=h0*pow(int(beta[r]),-1,p)*np.outer(W[ids,r],Wb[ids,r])%p
        # Other folded channels may be present. Extract the c cluster by values
        # only AFTER its actual full L. This keeps its derivative source.
        distinct=[(pow(q,2*a+1,p)+pow(q,-2*a-1,p))%p for a in range(j+1)]
        proj=np.eye(len(ids),dtype=np.int64)
        for b in distinct:
            if b!=c:proj=proj@(O-b*np.eye(len(ids),dtype=np.int64))%p*pow(c-b,-1,p)%p
        observed=proj@L%p@Pb%p
        assert np.array_equal(observed,central)
    # Lowest complete Jordan chain and its retained source current.
    ids=[a*N+m-a for a in range(m+1)]
    O=(Ft[np.ix_(ids,range(N*N))]@Et[np.ix_(range(N*N),ids)]
       +q*Kt[np.ix_(ids,ids)]+pow(q,-1,p)*np.diag([pow(int(Kt[a,a]),-1,p) for a in ids]))%p
    h=W[ids,0];hb=Wb[ids,0];v=np.zeros(m+1,dtype=np.int64);v[0]=1
    dv=np.zeros(m+1,dtype=np.int64)
    for a in range(m):
        back=int(O[a,a-1]) if a else 0;front=int(O[a,a+1]);prev=int(v[a-1]) if a else 0;dp=int(dv[a-1]) if a else 0
        v[a+1]=((c-int(O[a,a]))*int(v[a])-back*prev)*pow(front,-1,p)%p
        dv[a+1]=(int(v[a])+(c-int(O[a,a]))*int(dv[a])-back*dp)*pow(front,-1,p)%p
    assert np.array_equal(v,h)
    Lprime=-2*N*pow(4-c*c,-1,p)%p
    normal=dv*pow(Lprime,-1,p)%p;L=circle(O,N,p)
    assert np.array_equal(L@normal%p,h)
    assert np.array_equal((O-c*np.eye(m+1,dtype=np.int64))@normal%p,h*pow(Lprime,-1,p)%p)
    assert int(hb@normal[::-1]%p)==pow(h0,-1,p)
    assert int(sum(int(a)**2 for a in h)%p)==0
    nf=np.zeros(N*N,dtype=np.int64);nf[ids]=normal
    previous=np.zeros(N*N,dtype=np.int64)
    for a in range(m):previous[a*N+m-1-a]=pow(q,a*a,p)*fac[m-1]*pow(fac[a]*fac[m-1-a],-1,p)%p
    assert np.array_equal(Et@nf%p,x*pow(2*Lprime,-1,p)*previous%p)
    # Actual trivalent scalar and both white kernels remain explicitly open.
    labels=[(m+r,j) for r in range(l)]
    U,V,Vm=vertex_formula(N,x,p,labels,Wb)
    A=pow(q,-j,p)*sum(pow(x,k-N,p)*int(Wb[k*N+m-k,0])**2*int(Wb[(j+k)*N+m-k,j]) for k in range(m+1))%p
    assert int(U[2*j,j,0])==N**3*A%p
    b=np.array([pow(Q,-k*(m-k),p)*(fac[m]*pow(fac[k]*fac[m-k],-1,p)%p)**2%p for k in range(m+1)],dtype=np.int64)
    S=sum(sine(k)*cosine(k)*int(b[k])**2 for k in range(1,m))%p
    assert A==pow(q,1-m*(m-1),p)*S%p
    balanced=U.copy()
    for a in range(3):
        shape=[1,1,1];shape[a]=l
        balanced=balanced*np.array([pow(int(z),-1,p) for z in beta]).reshape(shape)%p
    assert not np.any(triple_action(balanced,'E',EQ,FQ,KQ,p))
    assert not np.any(triple_action(balanced,'F',EQ,FQ,KQ,p))
    # Independent canonical 3j: lowest pair slice, then the actual E recurrence.
    EQ2,FQ2,KQ2=coproduct(EQ,FQ,KQ,2,l,p)
    current=np.zeros(l*l,dtype=np.int64);current[2*j*l+j]=1
    for a in range(2*j-1,j-1,-1):
        ratio=-int(KQ[a+1,a+1])*(1-pow(Q,a+1,p))*pow(1-pow(Q,3*j-a,p),-1,p)%p
        current[a*l+3*j-a]=int(current[(a+1)*l+3*j-a-1])*pow(ratio,-1,p)%p
    Theta=np.zeros((l,l,l),dtype=np.int64);Theta[:,:,0]=current.reshape(l,l)
    for r in range(1,l):
        current=(-int(KQ[r-1,r-1])*pow(int(EQ[r-1,r]),-1,p))*(EQ2@current%p)%p
        Theta[:,:,r]=current.reshape(l,l)
    assert np.array_equal(balanced,N**3*A*pow(int(beta[j]),-1,p)*Theta%p)
    assert not np.any(triple_action(Theta,'E',EQ,FQ,KQ,p))
    assert not np.any(triple_action(Theta,'F',EQ,FQ,KQ,p))
    # Full recoupling/contiguous coefficient identity, with endpoint zeros kept.
    JJ,Jb=Jmatrix(N,q,p),Jmatrix(N,pow(q,-1,p),p);rev=np.eye(N,dtype=np.int64)[::-1]
    assert np.array_equal(Jb@rev%p@JJ%p,rev)
    f=pow(q,j*j,p)*W[[a*N+d-a for a in range(N)],j]%p
    y=JJ@f%p;want=np.zeros(N,dtype=np.int64)
    for k in range(m):
        betaj=pow(Q,-k*(j-k),p)*(fac[j]*pow(fac[k]*fac[j-k],-1,p)%p)**2%p
        want[m+k]=betaj*pow(sine(k+1),-1,p)%p
    assert np.array_equal(y,want)
    transforms=[]
    for k in range(m+1):
        values=[]
        for arg in (1,pow(Q,-1,p)):
            z=0
            for i in range(k,m+1):z+=int(b[i])*(-1)**i*pow(arg,i,p)*facb[i]*pow(facb[k]*facb[i-k],-1,p)
            values.append(z%p)
        if k==0:assert values[0]==0
        else:
            expected=(-1)**k*pow(q,(m-k)**2,p)*sine(k)*int(b[k])%p
            assert values[0]==expected
            ratio=(1+3*pow(Q,-k,p))*pow(1-pow(Q,-k,p),-1,p)%p
            assert values[1]==ratio*values[0]%p
        transforms.append(values)
    return {'N':N,'prime':p,'all_actual_even_Clebsch_and_endpoint_phases':True,
            'paired_normal_CD_factor_all_degrees':True,
            'actual_Jordan_preimage_and_nonzero_E_current':True,
            'entire_balanced_black_tensor_independent_canonical_3j':True,
            'full_repeated_Casimir_and_contiguous_transform':True,
            'original_black_scalar_weighted_quartic':True,'scalar_image':int(A),
            'marked_white_kernel_retained_separately':True}


def complex_normal_and_profile(N):
    mp.mp.dps=85;m=N//2;j=m-1;q=mp.exp(mp.pi*1j/N);Q=q*q;x=q**(N-1);theta=mp.pi/N
    fac=[mp.mpc(1)];s=[mp.mpf(1)]
    for a in range(1,N):fac.append(fac[-1]*(1-Q**a));s.append(s[-1]*abs(1-Q**a))
    h=[q**(a*a)*fac[m]/fac[a]/fac[m-a] for a in range(m+1)]
    Lprime=-N/(2*mp.sin(theta)**2);H=[mp.mpc(0)]
    partial=mp.mpc(0)
    for a in range(m):
        partial+=h[a]**2
        t=Q**(-m+a)*(1-Q**(m-a))*(1-Q**(a+1))
        H.append(H[-1]+partial/(t*h[a]*h[a+1]))
    ratio=max(abs(z/Lprime) for z in H)
    assert ratio<=mp.pi**2/8
    value=sum(mp.sin(k*theta)*mp.cos(k*theta)*(s[m]/s[k]/s[m-k])**4 for k in range(1,m))
    normalized=4*N**mp.mpf('1.5')*mp.exp(-N*4*mp.catalan/mp.pi)*value
    if N>=32:assert abs(normalized-1)<3/N
    return {'N':N,'max_componentwise_normal_over_highest_envelope':float(ratio),
            'proved_uniform_bound':float(mp.pi**2/8),
            'positive_weighted_quartic':bool(value>0),
            'normalized_even_Laplace_prefactor':float(normalized)}


if __name__=='__main__':
    rows=[field_case(N) for N in range(2,18,2)]
    complex_rows=[complex_normal_and_profile(N) for N in (4,6,8,16,32,64,128,256)]
    out={'status':'PASS','actual_even_source_and_normals':rows,
         'principal_complex_normal_envelopes_and_scalar_profiles':complex_rows,
         'scope':'Exact paired-normal central source identities and positive scalar asymptotic. No odd-source replacement, even semisimplification, complex joint-color packet, marked-vertex norm or global survival assertion.'}
    Path(__file__).with_name('actual_trivalent_even_central_normal_packet_results.json').write_text(json.dumps(out,indent=2)+'\n')
    print('PASS 8 actual even Clebsch/CD/Jordan/source/quartic levels; 8 complex normal-envelope and scalar calibrations')
