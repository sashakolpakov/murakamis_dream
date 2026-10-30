#!/usr/bin/env python3
"""Original Newton coefficients, polynomial source system, and character map."""
import argparse
import json
import sympy as sp
import sys
from pathlib import Path
import numpy as np

from audit_actual_two_cut_ports import balanced_data


def rank(A,p):
    A=np.array(A,dtype=np.int64).copy()%p
    m,n=A.shape;r=0
    for c in range(n):
        pivot=next((j for j in range(r,m) if A[j,c]),None)
        if pivot is None:continue
        A[[r,pivot]]=A[[pivot,r]]
        A[r]=A[r]*pow(int(A[r,c]),-1,p)%p
        for j in range(m):
            if j!=r and A[j,c]:A[j]=(A[j]-int(A[j,c])*A[r])%p
        r+=1
        if r==m:break
    return r


def fold_selection():
    out=[];values=jumps=rows=0
    for N in range(3,19):
        p,eta,q,*_=balanced_data(N);d=N-1;M=d//2;s0=d-2*M
        Q=q*q%p;ii=pow(eta,N,p);inv2=pow(2,-1,p)
        sin=lambda n:(pow(q,n,p)-pow(q,-n,p))*pow(2*ii,-1,p)%p
        cos=lambda n:(pow(q,n,p)+pow(q,-n,p))*inv2%p
        x,b,c,y=3,5,7,11
        D=lambda j:(x-pow(Q,j,p)*y)*(x-pow(Q,-j,p)*y)%p
        while any(D(j)==0 for j in range(N)):y+=2
        F=[1]
        for j in range(1,N):F.append(F[-1]*(1-pow(Q,j,p))%p)
        def Z(a,middle):
            total=0
            for k in range(a+1):
                v=pow(q,k*k-a*a,p)*pow(F[a]*pow(F[k]*F[a-k],-1,p)%p,2,p)%p
                for r in range(k):v=v*(x+pow(q,2*r+1,p)*middle)%p
                for r in range(a-k):v=v*(middle+pow(q,2*r+1,p)*y)%p
                total=(total+v)%p
            return total
        Zb=[Z(a,b) for a in range(N)];Zc=[Z(a,c) for a in range(N)];values+=2*N
        P0=1
        for r in range(1,N):P0=P0*(x-pow(Q,r,p)*y)%p
        Ps=[P0]
        for j in range(1,N):Ps.append(Ps[-1]*pow(D(j),-1,p)%p)
        omega=lambda j:pow(eta,d*d,p)*(-1)**j*pow(q,j*(j+1),p)%p
        def coefficients(j):
            uj=cos(j-1)*sin(j)%p
            vb=sin(2*j-1)*(x+y+2*b*cos(j)*cos(j-1))%p
            vc=sin(2*j-1)*(x+y+2*c*cos(j)*cos(j-1))%p
            bar=sin(j-1)*cos(j)%p;wj=bar*D(j-1)%p
            mat=np.array([[vb*vc,-vb*wj,-wj*vc,bar*bar*D(j-1)],
                          [uj*vb,0,-uj*wj,0],[uj*vc,-uj*wj,0,0],
                          [D(j)*uj*uj,0,0,0]],dtype=np.int64)%p
            return uj*uj*D(j)%p,mat
        for eps in (-1,0,1):
            U=[]
            for j in range(N):
                bp=Zb[j-1] if j else 0;cp=Zc[j-1] if j else 0
                Y=np.array([Zb[j]*Zc[j],Zb[j]*cp,bp*Zc[j],D(j)*bp*cp],dtype=np.int64)%p
                U.append(Y*(pow(omega(j),eps,p)*Ps[j]%p)%p)
            zero=np.zeros(4,dtype=np.int64)
            for j in range(N+1):
                L,T=coefficients(j);factor=pow(-pow(Q,j,p)%p,eps,p)
                lhs=L*(U[j] if j<N else zero)%p
                rhs=factor*(T@(U[j-1] if j else zero)%p)%p
                assert np.array_equal(lhs,rhs),(N,eps,j,lhs,rhs)
                rows+=4
            hi=M+s0+1
            assert np.array_equal(U[hi],pow(q,(s0+1)*eps,p)*U[M][::-1]%p)
            jumps+=1
            # Homogeneous differences of finite-polynomial solutions with the
            # SAME prescribed initial vector have U0=0.
            blocks=[]
            for j in range(N+1):
                L,T=coefficients(j);block=np.zeros((4,4*N),dtype=np.int64)
                if j<N:block[:,4*j:4*j+4]=L*np.eye(4,dtype=np.int64)
                if j:block[:,4*(j-1):4*j]=(-pow(-pow(Q,j,p)%p,eps,p)*T)%p
                blocks.append(block%p)
            initial=np.zeros((4,4*N),dtype=np.int64);initial[:,:4]=np.eye(4,dtype=np.int64)
            A=np.vstack(blocks+[initial])%p
            nullity=4*N-rank(A,p)
            assert nullity==(3 if N%2==0 else 0),(N,eps,nullity)
            jump=np.zeros((4,4*N),dtype=np.int64)
            jump[:,4*hi:4*hi+4]=np.eye(4,dtype=np.int64)
            jump[:,4*M:4*M+4]=-pow(q,(s0+1)*eps,p)*np.eye(4,dtype=np.int64)[::-1]
            augmented=4*N-rank(np.vstack([A,jump%p]),p)
            assert augmented==0
            bridge=None
            if N%2==0:
                H=N//2
                assert rank(coefficients(H)[1],p)==1
                assert coefficients(H)[0]!=0
                assert rank(coefficients(H+1)[1],p)==1
                assert coefficients(H+1)[0]==0
                assert all(rank(coefficients(j)[1],p)==4 for j in range(H+2,N))
                assert rank(coefficients(N)[1],p)==1
                bridge=[1,1]
            out.append({'N':N,'epsilon':eps,'field':p,'face_values':[x,b,c,y],
                        'unaugmented_kernel_dimension':nullity,
                        'with_actual_reflection_kernel_dimension':augmented,
                        'even_bridge_ranks':bridge})
    return {'status':'PASS','original_Newton_values':values,'canonical_fold_jumps':jumps,
            'actual_polynomial_system_rows':rows,'finite_system_dimension_checks':len(out),
            'cases':out,'scope':'Exact localized finite external-polynomial system. Three-dimensional freedom is an operator solution-space statement, not three original-source choices. Literal Newton source and its reflected jump fix the unique source solution.'}



def symbolic_character():
    T,U,V,J,Z,W,e=sp.symbols('T U V J Z W e')
    P=lambda X,Y:T*(J-Y)**2*(X-Y)+(Y-1)**2*(T*Y-X*J)
    ee=lambda X,Y:-Y*(J-1)**2*(T*Y-X*J)/(J*X*(J-Y)**2)
    rr=(J+1)**2/(4*J);Bb=T+1-2*T*rr/U;D=(T+1)**2-4*T*rr
    K=(J**3*U*(J-T)+(J*T*(1-J**2)+2*J**2*U*(T-1))*Z
       +(U*(1-J*T)+2*T*(J-1))*Z*Z)
    assert sp.factor(ee(U,Z)**2-2*Bb*ee(U,Z)+D+P(U,Z)*K/(J*U**2*(J-Z)**4))==0
    result=sp.resultant(P(U,Z),J*U*(J-Z)**2*e+Z*(J-1)**2*(T*Z-U*J),Z)
    assert sp.factor(result-J**4*U**2*(J-1)**4*(T-U)**2*(e*e-2*Bb*e+D))==0
    R0=Z*W*(J-1)**4*(T*Z-U*J)*(T*W-V*J)/(J*U*V*(J-Z)**2*(J-W)**2*(T-J)*(T*J-1))
    assert sp.factor(R0-ee(U,Z)*ee(V,W)/D)==0
    p1=lambda X,Y:Y*(X-1)/(X-Y)
    p2=lambda X,Y:J*Y*(T/X-1)/(T*Y/X-J)
    oldY=(1-U)*(T*Z-U*J)/(J*(U-Z)*(T-U))
    assert sp.factor(-p1(U,Z)/p2(U,Z)-oldY)==0
    oldTotal=J*Z*W*(T-J)*(T-U)*(T-V)/((T*J-1)*(T*Z-U*J)*(T*W-V*J))
    assert sp.factor((T-J)/(J*(T*J-1))*p2(U,Z)*p2(V,W)-oldTotal)==0
    u,vb,vc,bar,D0,D1=sp.symbols('u vb vc bar D0 D1')
    w=bar*D0
    M=sp.Matrix([[vb*vc,-vb*w,-w*vc,w*w],[u*vb,0,-u*w,0],
                 [u*vc,-u*w,0,0],[u*u,0,0,0]])
    G1=sp.diag(1,1,1,D1);G0=sp.diag(1,1,1,D0)
    NN=sp.Matrix([[vb*vc,-vb*w,-w*vc,bar*bar*D0],[u*vb,0,-u*w,0],
                 [u*vc,-u*w,0,0],[D1*u*u,0,0,0]])
    assert sp.simplify(NN-G1*M*G0.inv())==sp.zeros(4)
    assert sp.factor(NN.det()-(D1/D0)*(u*w)**4)==0
    return {'exact_gauge_and_ordered_character_certificates':7}


def coefficient_checks():
    counts=dict(literal_Newton_face_polynomials=0,canceled_source_component_identities=0,
                polynomial_system_rows=0,source_component_degree_checks=0,
                literal_core_cosine_polynomials=0,shared_face_coupled_rows=0,
                shared_face_coefficient_equalities=0,marked_K4_core_coefficients=0)
    z0=(0,0,0,0)
    for N in range(3,8):
        p,eta,q,*_=balanced_data(N);Q=q*q%p;d=N-1;M=d//2
        ii=pow(eta,N,p);inv2=pow(2,-1,p)
        sin=lambda j:(pow(q,j,p)-pow(q,-j,p))*pow(2*ii,-1,p)%p
        cos=lambda j:(pow(q,j,p)+pow(q,-j,p))*inv2%p
        def scale(a,c):return {k:v*c%p for k,v in a.items() if v*c%p}
        def add(*args):
            out={}
            for a in args:
                for k,v in a.items():out[k]=(out.get(k,0)+v)%p
            return {k:v for k,v in out.items() if v}
        def mul(a,b):
            out={}
            for ka,va in a.items():
                for kb,vb in b.items():
                    k=tuple(x+y for x,y in zip(ka,kb));out[k]=(out.get(k,0)+va*vb)%p
            return {k:v for k,v in out.items() if v}
        def product(*args):
            v={z0:1}
            for a in args:v=mul(v,a)
            return v
        def var(j):return {tuple(1 if k==j else 0 for k in range(4)):1}
        x,b,c,y=[var(j) for j in range(4)]
        Delta=lambda j:add(product(x,x),scale(product(x,y),-pow(Q,j,p)-pow(Q,-j,p)),product(y,y))
        def forced(a):return product(*(add(x,scale(y,-pow(Q,r,p))) for r in range(a+1,N-a)))
        F=[1]
        for j in range(1,N):F.append(F[-1]*(1-pow(Q,j,p))%p)
        def source(a,middle):
            terms=[]
            for k in range(a+1):
                coeff=pow(q,k*k-a*a,p)*pow(F[a]*pow(F[k]*F[a-k],-1,p)%p,2,p)%p
                term=product(*(add(x,scale(middle,pow(q,2*r+1,p))) for r in range(k)),
                             *(add(middle,scale(y,pow(q,2*r+1,p))) for r in range(a-k)))
                terms.append(scale(term,coeff))
            return add(*terms)
        Zb=[source(j,b) for j in range(N)];Zc=[source(j,c) for j in range(N)]
        counts['literal_Newton_face_polynomials']+=2*N
        P0=forced(0)
        B=[product(forced(j),Zb[j],Zc[j]) for j in range(M+1)]
        Bext=[B[min(j,d-j)] for j in range(N)]
        omega=lambda j:pow(eta,d*d,p)*(-1)**j*pow(q,j*(j+1),p)%p
        def mat(j):
            uj=cos(j-1)*sin(j)%p
            vb=scale(add(x,y,scale(b,2*cos(j)*cos(j-1))),sin(2*j-1))
            vc=scale(add(x,y,scale(c,2*cos(j)*cos(j-1))),sin(2*j-1))
            bar=sin(j-1)*cos(j)%p;wj=scale(Delta(j-1),bar)
            NN=[[mul(vb,vc),scale(mul(vb,wj),-1),scale(mul(wj,vc),-1),scale(Delta(j-1),bar*bar)],
                [scale(vb,uj),{},scale(wj,-uj),{}],
                [scale(vc,uj),scale(wj,-uj),{},{}],
                [scale(Delta(j),uj*uj),{},{},{}]]
            return scale(Delta(j),uj*uj),NN
        def matvec(A,v):return [add(*(mul(a,b) for a,b in zip(row,v))) for row in A]
        def perm(poly):
            # Actual K4 shared-face pattern: (x,b,c,y)->(b,x,y,c).
            return {(k[1],k[0],k[3],k[2]):v for k,v in poly.items()}
        for eps in (-1,0,1):
            UU=[]
            for j in range(N):
                if j<=M:
                    crossb=product(forced(j),Zb[j],Zc[j-1]) if j else {}
                    crossc=product(forced(j),Zb[j-1],Zc[j]) if j else {}
                else:
                    r=d-j;s=d-2*r
                    if s==1:crossb=crossc=mul(Zb[M],Zc[M])
                    else:
                        crossb=product(forced(r+1),Zb[r],Zc[r+1])
                        crossc=product(forced(r+1),Zb[r+1],Zc[r])
                v=[Bext[j],crossb,crossc,Bext[j-1] if j else {}]
                v=[scale(w,pow(omega(j),eps,p)) for w in v];UU.append(v)
                # Compare the POLYNOMIAL gauge against uncanceled original H.
                denom=product(*(Delta(r) for r in range(1,j+1)))
                bp=Zb[j-1] if j else {};cp=Zc[j-1] if j else {}
                literal=[mul(Zb[j],Zc[j]),mul(Zb[j],cp),mul(bp,Zc[j]),product(Delta(j),bp,cp)]
                for k in range(4):
                    assert mul(denom,v[k])==scale(mul(P0,literal[k]),pow(omega(j),eps,p))
                    counts['canceled_source_component_identities']+=1
                    expected=d-(1 if k in(1,2) else 0)
                    assert all(sum(m)==expected for m in v[k]);counts['source_component_degree_checks']+=1
            for j in range(N+1):
                L,NN=mat(j);left=[mul(L,v) for v in (UU[j] if j<N else [{}]*4)]
                right=[scale(v,pow(-pow(Q,j,p)%p,eps,p)) for v in matvec(NN,UU[j-1] if j else [{}]*4)]
                assert left==right;counts['polynomial_system_rows']+=4
            tt=3;zz=pow(tt,-2,p)
            full=add(*(scale(UU[j][0],pow(tt,d,p)*pow(zz,j,p)) for j in range(N)))
            folded=add(*(scale(B[a],(1 if 2*a==d else 2)*pow(omega(a),eps,p)
                              *(pow(tt,d-2*a,p)+pow(tt,-d+2*a,p))*inv2) for a in range(M+1)))
            assert full==folded;counts['literal_core_cosine_polynomials']+=1
            # Tensor with an overlapping actual K4 face register and extract
            # every face coefficient, rather than testing only point values.
            if N<=6:
                z2=5
                other=[add(*(scale(perm(UU[j][k]),pow(z2,j,p)) for j in range(N))) for k in range(4)]
                left=[{} for _ in range(4)];right=[{} for _ in range(4)]
                for j in range(N):
                    L,_=mat(j);_,NN=mat(j+1)
                    for k in range(4):left[k]=add(left[k],scale(mul(L,UU[j][k]),pow(zz,j,p)))
                    rv=matvec(NN,UU[j])
                    for k in range(4):right[k]=add(right[k],scale(rv[k],pow(zz,j+1,p)*pow(-pow(Q,j+1,p)%p,eps,p)))
                for a in range(4):
                    for bb in range(4):
                        ll=mul(left[a],other[bb]);rr=mul(right[a],other[bb])
                        assert ll==rr;counts['shared_face_coupled_rows']+=1
                        counts['shared_face_coefficient_equalities']+=len(ll)
                first=add(*(scale(UU[j][0],pow(zz,j,p)) for j in range(N)))
                target=(0,d,0,d)
                coeff=mul(first,other[0]).get(target,0)
                independent=0
                for j in range(N):
                    for k in range(N):
                        independent=(independent+pow(zz,j,p)*pow(z2,k,p)*mul(UU[j][0],perm(UU[k][0])).get(target,0))%p
                assert coeff==independent;counts['marked_K4_core_coefficients']+=1
    return counts


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',default='experiments/actual_whole_source_coupled_face_difference_system_results.json');args=ap.parse_args()
    data={'status':'PASS','symbolic':symbolic_character(),'polynomial_coefficients':coefficient_checks(),
          'fold_selection':fold_selection(),
          'scope':'Literal homogenized Newton source, polynomial face gauge, finite shared-face coefficient system, canonical fold state and original ordered-character identities. No scalar A-polynomial elimination, selected complex asymptotic or small-color-subset gap is inferred.'}
    Path(args.output).write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps({k:v for k,v in data.items() if k!='fold_selection'},indent=2))
    print(json.dumps({k:v for k,v in data['fold_selection'].items() if k!='cases'},indent=2))


if __name__=='__main__':main()
