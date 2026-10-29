#!/usr/bin/env python3
"""Exact ordinary open columns and original supported/unsaturated seam normals."""
import json
import math
from pathlib import Path

import numpy as np

from audit_actual_nc_morse_graph_first_normal_source_reduction import (
    Local, mul, inv, graph_case, exposed_mark, ordered_dipole_graph, module_jet,
)
from audit_actual_trivalent_complete_circle_vertex_kernel import (
    theta_graph, ordered_cube_graph, matching, noncrossing, axis_apply,
)
from audit_actual_six_port_divided_power_source_kernel import ActualDivided, states


def open_contract(tensors, output, p):
    tensors=[((A[0].copy(),A[1].copy()),tuple(labels)) for A,labels in tensors]
    while len(tensors)>1:
        choices=[]
        for i,(A,left) in enumerate(tensors):
            for j in range(i+1,len(tensors)):
                B,right=tensors[j];common=set(left)&set(right)
                size=math.prod(A[0].shape[k] for k,x in enumerate(left) if x not in common)
                size*=math.prod(B[0].shape[k] for k,x in enumerate(right) if x not in common)
                choices.append((not bool(common),size,-len(common),i,j,common))
        _,_,_,i,j,common=min(choices,key=lambda z:z[:5])
        A,left=tensors[i];B,right=tensors[j];shared=sorted(common)
        axes=([left.index(x) for x in shared],[right.index(x) for x in shared])
        out=(np.tensordot(A[0],B[0],axes=axes)%p,
             (np.tensordot(A[1],B[0],axes=axes)+np.tensordot(A[0],B[1],axes=axes))%p)
        labels=tuple(x for x in left if x not in common)+tuple(x for x in right if x not in common)
        tensors=[z for k,z in enumerate(tensors) if k not in (i,j)]+[(out,labels)]
    A,labels=tensors[0]
    assert set(labels)==set(output)
    if not output:return int(A[0])%p,int(A[1])%p
    return tuple(a.transpose(tuple(labels.index(x) for x in output)) for a in A)


def packet(local, graph, labels, powers, omit_white=None):
    ports,black,marked=graph;p=local.p
    tensors=[];S=(1,0)
    for v,edges in ports.items():
        if v==omit_white:continue
        js=tuple(labels[e] for e in edges)
        ordered=js if v in black else js[::-1]
        V=local.vertex(ordered)
        assert V['theta'] is not None
        S=mul(S,V['s'],p)
        tensor=V['theta'] if v in black else local.dual(V['theta'],ordered)
        tensors.append((tensor,edges))
    out=() if omit_white is None else ports[omit_white]
    Xi=open_contract(tensors,out,p)
    C=1
    for e,j in enumerate(labels):
        C=C*local.h0[j]*local.gamma[j]*pow(local.omega[j],powers[e],p)%p
    return Xi,S,C


def graft(A,B,u,w,labelsA,labelsB,powersA,powersB):
    pa,ba,ma=A;pb,bb,mb=B
    assert u in ba and w not in bb
    interval=pa[u];outer=pb[w]
    assert interval==tuple(range(interval[0],interval[0]+3))
    assert outer[0]==0 and outer[-1]==len(labelsB)-1
    assert tuple(labelsA[e] for e in interval)==tuple(labelsB[e] for e in outer)
    start=interval[0];shift=len(labelsB)-3
    def old(e):
        if e<start:return e
        if e>start+2:return e+shift
        return start+outer[e-start]
    ports={v:tuple(old(e) for e in es) for v,es in pa.items() if v!=u}
    black=set(ba)-{u};offset=max(pa)+1
    for v,es in pb.items():
        if v==w:continue
        ports[offset+v]=tuple(start+e for e in es)
        if v in bb:black.add(offset+v)
    labels=[None]*(len(labelsA)+shift);powers=[0]*len(labels)
    for e,j in enumerate(labelsB):labels[start+e]=j;powers[start+e]=powersB[e]
    for e,j in enumerate(labelsA):
        labels[old(e)]=j
        if e in interval:powers[old(e)]+=powersA[e]
        else:powers[old(e)]=powersA[e]
    result=(ports,black,ma)
    assert noncrossing([es for v,es in ports.items() if v in black])
    assert noncrossing([es for v,es in ports.items() if v not in black])
    matching([es for v,es in ports.items() if v in black])
    matching([es for v,es in ports.items() if v not in black])
    assert exposed_mark(A) and exposed_mark(B) and exposed_mark(result)
    return result,labels,powers


def cube_corner(local,labels):
    graph=ordered_cube_graph();ports,black,w=graph;p=local.p
    a,b,c=labels[0],labels[10],labels[11];r=b+c-a
    B0=labels[1]+labels[2]-a
    B1=labels[3]+labels[4]+c
    B2=labels[5]+labels[9]+a-c
    vtx={}
    for v,es in ports.items():
        if v==w:continue
        js=tuple(labels[e] for e in es);ordered=js if v in black else js[::-1]
        T=local.vertex(ordered)['theta'];assert T is not None
        vtx[v]=T if v in black else local.dual(T,ordered)
    result=(0,0)
    for u in range(2*labels[1]+1):
        for v in range(2*labels[3]+1):
            for z in range(2*labels[5]+1):
                color={0:2*a,10:r,11:0,1:u,2:B0-u,3:v,4:B1-v,5:z,9:B2-z,
                       8:sum(labels[e] for e in (1,8,9))-B2-u+z,
                       7:sum(labels[e] for e in (2,3,7))-B0+u-v,
                       6:sum(labels[e] for e in (4,5,6))-B1+v-z}
                if any(not 0<=color[e]<=2*labels[e] for e in range(12)):continue
                term=(1,0)
                for vertex,es in ports.items():
                    if vertex==w:continue
                    at=tuple(color[e] for e in es);T=vtx[vertex]
                    term=mul(term,(int(T[0][at]),int(T[1][at])),p)
                result=(result[0]+term[0])%p,(result[1]+term[1])%p
    return result


def physical_before_boundary_circles(local, graph, labels, powers, white):
    """Literal physical six-head source; no source projection is inserted."""
    p=local.p;ports,black,_=graph;boundary=set(ports[white])
    tensors=[];constant=1
    for e,j in enumerate(labels):
        if e not in boundary:
            constant=constant*local.h0[j]*pow(local.omega[j],powers[e],p)%p
    for v,edges in ports.items():
        if v==white:continue
        if v in black:
            value=local.J[0].copy()
            for axis,e in enumerate(edges):
                if e not in boundary:value=axis_apply(local.pi[labels[e]][0],value,axis,p)
        else:
            value=local.ellS[0].copy()
            for axis,e in enumerate(edges):
                assert e not in boundary
                value=axis_apply(local.W[labels[e]][0].T,value,axis,p)
        tensors.append(((value,np.zeros_like(value)),edges))
    Y=open_contract(tensors,ports[white],p)[0]
    return constant*Y%p


def ward_current(local, Y, kind):
    N,p=local.N,local.p
    value=Y.reshape((N,)*6)
    E,F,K=(A[0] for A in module_jet(N-1,local.q,p))
    Ki=np.diag([pow(int(z),-1,p) for z in np.diag(K)])
    result=np.zeros_like(value)
    for active in range(6):
        term=axis_apply(E if kind=='E' else F,value,active,p)
        for axis in (range(active+1,6) if kind=='E' else range(active)):
            term=axis_apply(K if kind=='E' else Ki,term,axis,p)
        result=(result+term)%p
    return result


def physical_sector(local,j):
    N,p,q=local.N,local.p,local.q;D=N*N
    K=local.Kpair[0]
    Ki=np.diag([pow(int(z),-1,p) for z in np.diag(K)])
    O=(local.Fpair[0]@local.Epair[0]+q*K+pow(q,-1,p)*Ki)%p
    eye=np.eye(D,dtype=np.int64);a,b=eye,O.copy()
    for _ in range(2,N):a,b=b,(O@b-a)%p
    value=(-1)**(N-1)*b%p
    cj=(pow(q,2*j+1,p)+pow(q,-2*j-1,p))%p
    for k in range((N-1)//2+1):
        if k==j:continue
        ck=(pow(q,2*k+1,p)+pow(q,-2*k-1,p))%p
        value=value@(O-ck*eye)%p*pow(cj-ck,-1,p)%p
    assert np.array_equal(value,local.h0[j]*local.W[j][0]%p@local.pi[j][0]%p)
    return value


def physical_pruning(N):
    local=Local(N);p=local.p;M=(N-1)//2;B=ordered_cube_graph()
    labels=[M]*12;powers=[0]*12
    Y=physical_before_boundary_circles(local,B,labels,powers,4)
    nonzero=np.any(Y)
    assert not np.any(ward_current(local,Y,'E'))
    assert not np.any(ward_current(local,Y,'F'))
    Y6=Y.reshape((N,)*6);d=N-1
    assert all(sum(a)==3*d for a in np.argwhere(Y6))
    data=ActualDivided(N,p,local.q)
    prefix=np.array([int(Y6[a+(0,d)])*pow(local.x,d,p)*pow(N,-1,p)%p
                     for a in states(N,4,2*d)],dtype=np.int64)
    assert not np.any(data.matrix('E',4,2*d,N)@prefix%p)
    # Boundary labels do not enter Y; their coupons were genuinely omitted.
    boundary=(1,1,1) if N>=5 else (0,0,0)
    observed=Y.copy()
    for axis,j in enumerate(boundary):
        observed=axis_apply(physical_sector(local,j),observed,axis,p)
    assert sum(boundary)<d and not np.any(observed)
    if N==5:assert nonzero
    nested=None
    if N==3:
        Yinner=physical_before_boundary_circles(local,B,labels,powers,5)
        Einner=ward_current(local,Yinner,'E');Finner=ward_current(local,Yinner,'F')
        assert np.any(Einner) or np.any(Finner)
        nested={'bare_nested_six_head_array_has_nonzero_ordinary_Ward_current':True}
    return {'N':N,'prime':p,'nonzero_physical_source_before_boundary_circles':bool(nonzero),
            'ordinary_E_F_and_integer_H_source_equations':True,
            'actual_extracted_Nth_divided_source_current_zero':True,
            'unsaturated_boundary_labels':list(boundary),
            'full_polynomial_circle_product_annihilates_before_mark':True,
            'nested_cut_countercurrent':nested}


def exact_order_two_certificate():
    """QQ(q), Phi_10 certificate; a zero prime-field image alone is NOT used."""
    from functools import lru_cache
    from flint import fmpq_poly
    modulus=fmpq_poly([1,-1,1,-1,1])
    class K:
        def __init__(self,a=0):
            self.a=(a.a if isinstance(a,K) else a if isinstance(a,fmpq_poly)
                    else fmpq_poly([a]))%modulus
        def __add__(self,other):return K(self.a+K(other).a)
        __radd__=__add__
        def __neg__(self):return K(-self.a)
        def __sub__(self,other):return self+-K(other)
        def __rsub__(self,other):return K(other)+-self
        def __mul__(self,other):return K(self.a*K(other).a)
        __rmul__=__mul__
        def inverse(self):
            g,u,_=self.a.xgcd(modulus)
            assert g==1
            return K(u)
        def __truediv__(self,other):return self*K(other).inverse()
        def __pow__(self,n):
            if n<0:return self.inverse()**(-n)
            out=K(1);a=self
            while n:
                if n&1:out*=a
                a*=a;n//=2
            return out
        def __bool__(self):return bool(self.a)
    q=K(fmpq_poly([0,1]));Q=q*q;fac=[K(1)]
    for r in range(1,5):fac.append(fac[-1]*(1-Q**r))
    @lru_cache(None)
    def theta(js):
        a,b,c=js;r=b+c-a;r1=a+b-c;out={}
        for k in range(r1+1):
            out[2*a-k,r+k,0]=(-1)**k*q**(k*(2*a+1-k))*fac[r+k]*fac[2*a-k]/fac[r]/fac[2*a]
        for t in range(1,2*c+1):
            co=-q**(2*c-2*(t-1))/(q**(-2*c-1)*(1-Q**(2*c+1-t)))
            for A in range(2*a+1):
                for B in range(2*b+1):
                    z=K(0)
                    if A<2*a:
                        z+=q**(-2*a-1)*(1-Q**(2*a-A))*q**(2*b-2*B)*out.get((A+1,B,t-1),K(0))
                    if B<2*b:
                        z+=q**(-2*b-1)*(1-Q**(2*b-B))*out.get((A,B+1,t-1),K(0))
                    if z:out[A,B,t]=co*z
        return out
    @lru_cache(None)
    def cup(j,u):
        return (-1)**u*q**(u*(2*j-u-1))*fac[u]*fac[2*j-u]/fac[2*j]
    def entry(js,rs,white):
        if not white:return theta(js).get(rs,K(0))
        a,b,c=js;u,v,w=rs
        return (theta((c,b,a)).get((2*c-w,2*b-v,2*a-u),K(0))
                /cup(c,2*c-w)/cup(b,2*b-v)/cup(a,2*a-u))
    B=ordered_cube_graph();labels=[2]*12
    for e in B[0][4]:labels[e]=1
    grouped=[K(0) for _ in range(4)];term_count=0
    for u in range(4):
        for v in range(5):
            for w in range(5):
                rs={0:2,10:1,11:0,1:u,2:3-u,3:v,4:5-v,5:w,9:4-w,
                    8:2-u+w,7:3+u-v,6:1+v-w}
                if any(not 0<=rs[e]<=2*labels[e] for e in rs):continue
                term=K(1)
                for vertex,es in B[0].items():
                    if vertex==4:continue
                    term*=entry(tuple(labels[e] for e in es),tuple(rs[e] for e in es),vertex not in B[1])
                if term:term_count+=1
                grouped[u]+=term
    rows=[]
    for value in grouped:
        coeff=[]
        for k in range(4):
            assert value.a[k]==int(value.a[k])
            coeff.append(int(value.a[k]))
        rows.append(coeff)
    assert term_count==50
    assert rows==[[58,-58,0,-92],[-386,236,-92,476],
                  [476,-234,150,-528],[-148,56,-58,144]]
    assert not sum(grouped,K(0))
    local=Local(5);A=ordered_cube_graph();labelsA=[2]*12
    for e in A[0][0]:labelsA[e]=1
    XiA,_,_=packet(local,A,labelsA,[0]*12)
    alphaB=cube_corner(local,labels)
    assert local.p==1021 and local.q==432
    assert XiA==(0,775) and alphaB==(0,909)
    new,labelsNew,powersNew=graft(A,B,0,4,labelsA,labels,[0]*12,[0]*12)
    assert all(sum(labelsNew[e] for e in es)>=4 for es in new[0].values())
    assert exposed_mark(new)
    return {'cyclotomic_modulus_coefficients':[1,-1,1,-1,1],
            'exact_nonzero_cube_terms':term_count,
            'four_grouped_coefficients_in_basis_1_q_q2_q3':rows,
            'exact_cube_alpha_root_zero_in_QQq':True,
            'nonzero_derivative_reduction':{'prime':1021,'q_image':432,
                'Xi_A_prime':775,'alpha_B_prime':909,
                'Xi_new_second_Taylor_coefficient':775*909%1021},
            'new_graph_edges':len(labelsNew),'new_vertices':len(new[0]),
            'all_new_vertex_triples_supported_but_unsaturated_three_cut':True,
            'exact_Xi_new_order':2,
            'original_fixed_first_normal_sector_zero':True}


def level(N,boundary,block_name):
    local=Local(N);p=local.p;M=(N-1)//2
    A=ordered_cube_graph()
    B={'theta':theta_graph(),'dipole':ordered_dipole_graph(),'cube':ordered_cube_graph()}[block_name]
    w=B[2];E_B=max(e for es in B[0].values() for e in es)+1
    labelsA=[M]*12;labelsB=[M]*E_B
    for e,j in zip(A[0][0],boundary):labelsA[e]=j
    for e,j in zip(B[0][w],boundary):labelsB[e]=j
    powersA=[(e%3)-1 for e in range(12)]
    powersB=[(-1)**e*(e%2) for e in range(E_B)]
    new,labelsNew,powersNew=graft(A,B,0,w,labelsA,labelsB,powersA,powersB)
    XiA,SA,CA=packet(local,A,labelsA,powersA)
    XiB,SB,CB=packet(local,B,labelsB,powersB)
    XiNew,SNew,CNew=packet(local,new,labelsNew,powersNew)
    Y,_,_=packet(local,B,labelsB,powersB,omit_white=w)
    a,b,c=boundary;corner=(2*a,b+c-a,0)
    alpha=int(Y[0][corner]),int(Y[1][corner])
    theta=local.theta(boundary)
    assert np.array_equal(Y[0],alpha[0]*theta[0]%p)
    assert np.array_equal(Y[1],(alpha[1]*theta[0]+alpha[0]*theta[1])%p)
    XiTheta,ST,CT=packet(local,theta_graph(),list(boundary),(0,0,0))
    assert XiB==mul(alpha,XiTheta,p)
    assert XiNew==mul(alpha,XiA,p)
    assert CNew==CA*CB*pow(CT,-1,p)%p
    assert mul(SNew,ST,p)==mul(SA,SB,p)
    literalA=graph_case(local,'A_cube',A,labelsA,powersA)
    literalB=graph_case(local,'B_'+block_name,B,labelsB,powersB)
    literalNew=graph_case(local,'typed_three_port_graft',new,labelsNew,powersNew)
    predicted=CNew*mul(SNew,mul(alpha,XiA,p),p)[1]*pow(local.nu,-1,p)%p
    assert literalNew['original_marked_scalar']==predicted
    supported=sum(boundary)>=N-1
    if supported:
        literalTheta=graph_case(local,'boundary_theta',theta_graph(),list(boundary),(0,0,0))
        zT=literalTheta['original_marked_scalar']
        assert predicted*zT%p==literalA['original_marked_scalar']*literalB['original_marked_scalar']%p
        assert XiTheta[0]==0 and XiTheta[1]!=0
    else:
        zT=0
        assert XiTheta[0]!=0
    if block_name=='cube':assert alpha==cube_corner(local,labelsB)
    return {'N':N,'prime':p,'boundary_labels':list(boundary),'B_block':block_name,
            'new_edges':len(labelsNew),'full_open_column_root_and_first_jet':True,
            'alpha_root_and_first_normal':list(alpha),
            'supported_positive_theta_seam':supported,
            'literal_marked_A_B_new':[literalA['original_marked_scalar'],literalB['original_marked_scalar'],predicted],
            'boundary_theta_marked_image':zT,
            'all_source_factors_and_signed_Cartan_sewing':True,
            'independent_cube_threefold_sum':block_name=='cube'}


if __name__=='__main__':
    rows=[]
    for N in range(3,8):
        M=(N-1)//2
        for name in ('theta','dipole','cube'):
            rows.append(level(N,(M,M,M),name))
    for N in (5,6,7):
        M=(N-1)//2
        rows.append(level(N,(M,M,M-1),'cube'))
    rows.append(level(5,(1,1,1),'cube'))
    out={'status':'PASS','actual_generic_and_fixed_normal_three_port_sewings':rows,
         'actual_six_physical_head_source_pruning':[physical_pruning(N) for N in range(3,8)],
         'exact_cyclotomic_order_two_counterexample':exact_order_two_certificate(),
         'scope':'Exact typed NC three-port sewing with exposed physical marks, full high-fold channels and source normals. The actual saturated six-head source kills unsaturated complete-circle seams before the mark; generic open jets are retained. No all-N cube positivity, geometry, or arbitrary six-pants operator claim.'}
    Path(__file__).with_name('actual_nc_three_port_source_sewing_results.json').write_text(json.dumps(out,indent=2)+'\n')
    print(f'PASS {len(rows)} all-entry/source sewings; 5 six-head divided-current/prunings; nested Ward current; exact QQ(q) order-two certificate')
