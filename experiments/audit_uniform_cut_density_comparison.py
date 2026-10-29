#!/usr/bin/env python3
"""Uniform canonical cut / holonomy determinant-line comparison.

Exact rational and finite-field diagnostics for the general proof.
Includes arbitrary quadratic canonical words, rank-two kernel and
cokernel matching, sourced endpoint torsion, and prefix moment maps.
No selected finite quantum period or volume limit is asserted.
"""

from itertools import combinations
import json
from pathlib import Path
import random

import numpy as np
import sympy as s


def symplectic_form(b):
    return s.zeros(b).row_join(s.eye(b)).col_join(
        (-s.eye(b)).row_join(s.zeros(b)))


def local_map(b,j,L):
    n=2*b;I=s.eye(n);F=I.copy()
    a,bb,p1,p2=I[j,:],I[j+1,:],I[b+j,:],I[b+j+1,:]
    tau=a+bb
    u=(p2-p1-L[0,0]*a-L[0,2]*tau)/L[0,1]
    pp2=p2+L[2,0]*a+L[2,1]*u+L[2,2]*tau
    pp1=pp2+L[1,0]*a+L[1,1]*u+L[1,2]*tau
    F[j,:]=u;F[j+1,:]=tau-u
    F[b+j,:]=pp1;F[b+j+1,:]=pp2
    O=symplectic_form(b)
    assert (F.T*O*F-O).applyfunc(s.cancel)==s.zeros(n)
    return F


def word_data(b,word,local_forms):
    m=len(word);n=b+m;I=s.eye(n);pos=I[:b,:]
    S=s.zeros(n);F=s.eye(2*b);product=1
    local_rows=[]
    for k,((j,sign),L) in enumerate(zip(word,local_forms)):
        a,bb,c=pos[j,:],pos[j+1,:],I[b+k,:]
        U=s.Matrix.vstack(a,bb+sign*c,a+bb)
        local_rows.append(U)
        S+=U.T*L*U
        pos[j,:],pos[j+1,:]=bb+sign*c,a-sign*c
        F=local_map(b,j,L)*F
        product*=L[0,1]
    closure=pos-I[:b,:];C=closure[1:,:]
    cofactor=C[:,1:b]
    assert abs(cofactor.det())==1
    E=s.zeros(n,m+1);E[0,0]=1
    for k in range(m):E[b+k,k+1]=1
    E[1:b,:]=-cofactor.inv()*C*E
    assert C*E==s.zeros(b-1,m+1)
    assert closure*E==s.zeros(b,m+1)
    H=E.T*S*E
    P=pos[:,:b];R=pos[:,b:]
    Jin=(-S[:b,b:]).row_join(P.T).col_join(
        S[b:,b:].row_join(-R.T))
    assert s.cancel(Jin.det()-(-1)**(m*(b-1))*product)==0
    inputs=S[:b,:b].row_join(s.eye(b)).col_join(
        (-S[b:,:b]).row_join(s.zeros(m,b)))
    solution=Jin.inv()*inputs
    Ffrom=(P.row_join(s.zeros(b))+R*solution[:m,:]).col_join(solution[m:,:])
    assert (F-Ffrom).applyfunc(s.cancel)==s.zeros(2*b)
    D=F-s.eye(2*b)
    Lcut=D[1:,:].col_join(s.eye(2*b)[b,:])
    assert s.cancel(H.det()-product*Lcut.det())==0
    return {'S':S,'H':H,'F':F,'D':D,'Lcut':Lcut,'Jin':Jin,
            'E':E,'C':C,'P':P,'R':R,'cofactor':cofactor,
            'product_V':product,'local_rows':local_rows}


def torsion(matrix,kernel,cokernel):
    n=matrix.rows;r=kernel.cols
    chosen=[];current=kernel
    for j in range(n):
        if current.row_join(s.eye(n)[:,j]).rank()>current.cols:
            chosen.append(j);current=current.row_join(s.eye(n)[:,j])
    V=s.eye(n)[:,chosen]
    assert V.cols==n-r
    pivots=cokernel.rref()[1]
    W=s.zeros(n,r)
    inverse=cokernel[:,list(pivots)].inv()
    for i,pivot in enumerate(pivots):W[pivot,:]=inverse[i,:]
    assert cokernel*W==s.eye(r)
    assert matrix*kernel==s.zeros(n,r)
    assert cokernel*matrix==s.zeros(r,n)
    return s.cancel(kernel.row_join(V).det()/(matrix*V).row_join(W).det())


WORDS=[(2,[(0,1)]),(2,[(0,1)]*3),
       (3,[(0,1),(1,-1)]*2),(3,[(0,1),(1,1)]),
       (4,[(0,1),(1,1),(2,-1)]),
       (5,[(0,1),(1,-1),(2,1),(3,-1)]),
       (6,[(0,1),(1,1),(2,-1),(3,1),(4,1)])]


def regular_words():
    records=[]
    for b,word in WORDS:
        forms=[s.Matrix([[k+2,k+3,2],[k+3,k+5,1],[2,1,k+7]])
               for k in range(len(word))]
        data=word_data(b,word,forms)
        assert data['H'].det()!=0
        records.append({'strands':b,'crossings':len(word),
                        'exact_canonical_maps_and_determinants':True,
                        'det_H_over_product_V_det_Lcut':str(s.cancel(
                            data['H'].det()/data['product_V']/data['Lcut'].det()))})
    return records


def degenerate_word():
    b=3;word=[(0,1),(1,-1)]*2;m=len(word);d=m+1
    variables=s.symbols('u:24')
    forms=[]
    for k in range(m):
        a,v,c,uu,t,tt=variables[6*k:6*k+6]
        forms.append(s.Matrix([[a,v,c],[v,uu,t],[c,t,tt]]))
    # Only build the linear position Hessian before imposing mixed units.
    I=s.eye(b+m);pos=I[:b,:];S=s.zeros(b+m)
    for k,((j,sign),L) in enumerate(zip(word,forms)):
        a,bb,c=pos[j,:],pos[j+1,:],I[b+k,:]
        U=s.Matrix.vstack(a,bb+sign*c,a+bb);S+=U.T*L*U
        pos[j,:],pos[j+1,:]=bb+sign*c,a-sign*c
    C=(pos-I[:b,:])[1:,:];E=s.zeros(b+m,d);E[0,0]=1
    for k in range(m):E[b+k,k+1]=1
    E[1:b,:]=-C[:,1:b].inv()*C*E
    H=E.T*S*E
    B=s.Matrix([[1,0],[0,1],[1,1],[2,-1],[-1,2]])
    equations=list(H*B)
    A,_=s.linear_eq_to_matrix(equations,variables)
    basis=A.nullspace();rng=random.Random(271027)
    data=None
    for attempt in range(40):
        value=sum((rng.randint(-3,3)*v for v in basis),s.zeros(len(variables),1))
        sub=dict(zip(variables,value));Fs=[L.subs(sub) for L in forms]
        if any(L[0,1]==0 for L in Fs):continue
        candidate=word_data(b,word,Fs)
        if candidate['H'].rank()==d-2:
            data=candidate;break
    assert data is not None
    S,H,E,C=data['S'],data['H'],data['E'],data['C']
    assert H*B==s.zeros(d,2)
    rho=C[:,1:b].T.inv()*(S*E*B)[1:b,:]
    assert C.T*rho==S*E*B
    p=s.zeros(b,2);p[1:,:]=rho
    Kend=(E*B)[:b,:].col_join(p)
    assert data['Lcut']*Kend==s.zeros(2*b,2)
    Ecan=s.zeros(2*b,2*b-1)
    for j in range(1,b):Ecan[j,j-1]=1;Ecan[0,j-1]=-1
    Ecan[b:,b-1:]=s.eye(b)
    O=symplectic_form(b)
    coker=(Kend.T*O*Ecan).row_join(s.zeros(2,1))
    TH=torsion(H,B,B.T)
    Tcut=-torsion(data['Lcut'],Kend,coker)
    assert s.cancel(data['product_V']*TH+Tcut)==0
    # Explicit first variation checks the same cokernel pairing.
    chi=next(pair for pair in combinations(range(d),2) if B[list(pair),:].det()!=0)
    selector=s.zeros(2,b+m)
    free_indices=[0]+list(range(b,b+m))
    for row,column in enumerate(chi):selector[row,free_indices[column]]=1
    perturbation=selector.T*selector
    rhs=(perturbation[:b,:]*E*B).col_join(-perturbation[b:,:]*E*B)
    motion=data['Jin'].inv()*rhs
    deltaF=(data['R']*motion[:m,:]).col_join(motion[m:,:])
    pairing=Kend.T*O*deltaF
    expected=B.T*E.T*perturbation*E*B
    assert (pairing-expected).applyfunc(s.cancel)==s.zeros(2)
    assert expected.det()!=0
    return {'strands':b,'crossings':m,'phase_dimension':d,'kernel_dimension':2,
            'closed_flow_kernel_maps_to_endpoint_kernel':True,
            'canonical_selfdual_cokernel_and_epsilon_pairing_exact':True,
            'product_V_T_H_equals_minus_T_cut':True,
            'phase_torsion':str(TH),'endpoint_torsion':str(Tcut)}


def endpoint_sources():
    records=[]
    h=s.Matrix([1,0,0]);ee=s.Matrix([0,1,0]);ff=s.Matrix([0,0,1])
    K=(h+2*ff).row_join(ee+ff);u=ee;ell=s.Matrix([[2,1,-1]])
    for n in (6,8,10):
        Cdom=s.Matrix(n,n,lambda i,j:(i+2 if i==j else (i+j+1 if j>i else 0)))
        Ctar=s.Matrix(n,n,lambda i,j:(i+3 if i==j else (i-j+2 if i>j else 0)))
        A=Cdom[:,:3];Vc=Cdom[:,3:];W=Ctar[:,n-3:]
        M=s.zeros(3,n);M[:,n-3:]=s.eye(3);M=M*Ctar.inv()
        D=Ctar[:,:n-3]*Cdom.inv()[3:,:]
        lam=ell.row_join(s.Matrix([[j+1 for j in range(n-3)]]))*Cdom.inv()
        p=s.Rational(2,3);b0=s.Matrix([[-1,-p,0]])
        Z=(ee-p*h).row_join(ff);z0=-h
        beta=b0*M
        Efull=(D*Vc).row_join(W*Z).row_join(W*z0)
        assert beta*Efull==s.Matrix([[0]*(n-1)+[1]])
        Lcut=(Efull.inv()*D)[:n-1,:].col_join(lam)
        coker=(M*Efull[:,:n-1])[1:,:].row_join(s.zeros(2,1))
        Tcut=torsion(Lcut,A*K,coker)/Efull.det()
        Tbeta=s.cancel(Cdom.det()/Ctar.det())
        assert s.cancel(Tcut+Tbeta)==0
        coefficients=s.Matrix([j+1 for j in range(n-3)])
        Rf=Vc*coefficients;f=D*Rf;c=s.Rational(7,3)
        solution=Rf+A*u*(c-(lam*Rf)[0])
        assert D*solution==f and (lam*solution)[0]==c
        eta=s.Matrix([[j*j+2 for j in range(n)]])
        dual=(eta*Rf)[0]+(eta*A*u)[0]*(c-(lam*Rf)[0])
        assert s.cancel((eta*solution)[0]-dual)==0
        records.append({'middle_dimension':n,'cut_torsion_over_holonomy_torsion':'-1',
                        'source_and_affine_dual_retained':True})
    return records


def moment_map():
    records=[];p=1009;Mmer=2;x=-Mmer%p;t=(x+pow(x,-1,p))%p
    inv=lambda a:pow(int(a)%p,-1,p)
    for b in range(1,9):
        n=2*b;Omega=np.zeros((n,n),dtype=np.int64)
        A=np.zeros((n,3),dtype=np.int64)
        av,bv,cv=1,0,0;da=np.zeros(n,dtype=np.int64);db=da.copy();dc=da.copy()
        for j in range(b):
            k=(j+3)%p;e=(2*j+5)%p;f=(t-k-inv(k))*inv(e)%p
            G=np.array([[k,e],[k*f%p,(t-k)%p]],dtype=np.int64)
            prefix=np.array([[av,bv],[cv,(1+bv*cv)*inv(av)%p]],dtype=np.int64)
            for index,(hu,ev,fw) in enumerate(((1,0,0),(0,1,0),(0,0,1))):
                H=(hu+(ev*cv+fw*bv)*inv(2*av))%p
                zeta=np.array([[H,ev*inv(av)%p],[fw*inv(av)%p,-H]],dtype=np.int64)
                delta=(zeta@G-G@zeta)%p
                A[2*j,index]=delta[0,0];A[2*j+1,index]=delta[0,1]
            Omega[2*j,2*j+1]=-inv(k*e)%p
            Omega[2*j+1,2*j]=inv(k*e)
            dk=np.zeros(n,dtype=np.int64);de=dk.copy();dk[2*j]=1;de[2*j+1]=1
            df=((inv(k*k)-1)*inv(e)*dk-f*inv(e)*de)%p
            anew=k*av%p;bnew=(k*bv+e)%p;cnew=k*(cv+f)%p
            dan=(k*da+av*dk)%p;dbn=(k*db+bv*dk+de)%p
            dcn=(k*(dc+df)+(cv+f)*dk)%p
            av,bv,cv,da,db,dc=anew,bnew,cnew,dan,dbn,dcn
        dv=(1+bv*cv)*inv(av)%p
        dd=((cv*db+bv*dc)*inv(av)-(1+bv*cv)*inv(av*av)*da)%p
        Pinv=np.array([[dv,-bv],[-cv,av]],dtype=np.int64)%p
        product_diff=np.zeros((3,n),dtype=np.int64)
        for j in range(n):
            deltaP=np.array([[da[j],db[j]],[dc[j],dd[j]]],dtype=np.int64)
            v=deltaP@Pinv%p
            product_diff[:,j]=[v[0,0],v[0,1],v[1,0]]
        R=np.array([[2,2*cv*inv(av),0],[-cv*inv(av),0,1],
                    [bv*inv(av),dv*inv(av),0]],dtype=np.int64)%p
        assert not np.any((A.T@Omega-R@product_diff)%p)
        records.append({'strands':b,'prime':p,'full_prefix_moment_map_exact':True})
    a,bv,cv,d=s.symbols('a b c d',nonzero=True)
    R=s.Matrix([[2,2*cv/a,0],[-cv/a,0,1],[bv/a,d/a,0]])
    assert s.factor(R.det()+2*(a*d-bv*cv)/a**2)==0
    K=s.Matrix([[1,0],[0,1],[2,1]])
    Z=s.Matrix([[-cv/a,0],[1,0],[0,1]])
    pairing=K.T*R*Z
    assert s.factor(pairing.det()-2*(a*d-bv*cv)/a**2)==0
    r,z,kappa=s.symbols('r s kappa');F=s.Matrix([[r,1-r],[z,-kappa-z]])
    cols=[]
    for variable in (r,z):
        X=-F.inv()*F.diff(variable);X-=s.trace(X)*s.eye(2)/2
        cols.append(s.Matrix([X[0,0],X[0,1],X[1,0]]))
    tangents=s.Matrix.hstack(*cols)
    Cframe=tangents[:2,:]
    assert (tangents-K*Cframe).applyfunc(s.cancel)==s.zeros(3,2)
    assert s.cancel(Cframe.det()+1/(2*(z+kappa*r)))==0
    return {'prefix_cases':records,'universal_R_determinant_exact':True,
            'canonical_cokernel_pairing_determinant_exact':True,
            'full_framing_Maurer_determinant_exact':True}


def main():
    result={'regular_quadratic_words':regular_words(),
            'rank_two_gaussian_and_endpoint':degenerate_word(),
            'endpoint_source_and_torsion':endpoint_sources(),
            'uniform_moment_map_and_framing':moment_map(),
            'scope':'Uniform variable principal-density line; no selected finite-period or volume theorem.'}
    output=Path(__file__).with_name('uniform_cut_density_comparison_results.json')
    output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'quadratic_words':len(result['regular_quadratic_words']),
                      'rank_two_kernel_and_cokernel_checked':True,
                      'sourced_endpoint_complexes':len(result['endpoint_source_and_torsion']),
                      'prefix_moment_map_cases':len(result['uniform_moment_map_and_framing']['prefix_cases']),
                      'output':str(output)},indent=2))


if __name__=='__main__':main()
