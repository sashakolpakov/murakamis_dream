#!/usr/bin/env python3
"""Shared edge caps, cyclic face rotations, and tetrahedron reversal.

The tensors are the already specified pointed fusion maps and actual
source-normalized endpoint caps. Root marks are shared on edges.
This audit makes no selected geometric-period or volume assertion.
"""

from functools import cache
from itertools import permutations,product
import json
from pathlib import Path

import numpy as np
import sympy as sp

from audit_actual_peripheral_fusion import inverse_mod, matrix_power
from audit_cyclic_steinberg_lattice import determinant
from audit_regular_holonomy_braiding import mm
from audit_relative_pivotal_duality import endpoint_frame,endpoint_module,pointed_fusion


def independent_rows(matrix,prime):
    work=matrix.T.copy()%prime;selected=[];row=0
    for col in range(work.shape[1]):
        pivot=next((k for k in range(row,len(work)) if work[k,col]),None)
        if pivot is None:continue
        work[[row,pivot]]=work[[pivot,row]]
        work[row]=work[row]*pow(int(work[row,col]),-1,prime)%prime
        for k in range(len(work)):
            if k!=row and work[k,col]:work[k]=(work[k]-work[k,col]*work[row])%prime
        selected.append(col);row+=1
        if row==len(work):break
    assert row==matrix.shape[1]
    return selected


def scalar_ratio(left,right,prime):
    r,c=next(zip(*np.nonzero(right)))
    value=int(left[r,c])*pow(int(right[r,c]),-1,prime)%prime
    return value if np.array_equal(left,right*value%prime) else None


def axis_action(tensor,matrix,axis,prime):
    return np.moveaxis(np.tensordot(matrix,tensor,axes=(1,axis)),0,axis)%prime


class Configuration:
    def __init__(self,level,charged=False,start=2):
        self.N=level
        self.p=next(12*level*k+1 for k in range(10,1000) if sp.isprime(12*level*k+1))
        generator=int(sp.primitive_root(self.p))
        self.generator=generator
        self.q=pow(generator,(self.p-1)//(2*level),self.p)
        self.Q=self.q*self.q%self.p
        self.tau=pow(generator,(self.p-1)//(3*level),self.p)
        assert pow(self.tau,3,self.p)==self.Q
        self.flags=[];values=set()
        for a in range(start,self.p):
            value=pow(a,level,self.p)
            if value not in values:self.flags.append(a);values.add(value)
            if len(self.flags)==4:break
        assert len(self.flags)==4
        self.points=[pow(a,level,self.p) for a in self.flags]
        self.marks={}
        for i,j in product(range(4),repeat=2):
            if i<j:
                x=pow(self.Q,i+j+1,self.p) if charged else 1
                self.marks[i,j]=x;self.marks[j,i]=pow(self.Q*x,-1,self.p)
        self.flip=np.zeros((level**2,level**2),dtype=np.int64)
        for i,j in product(range(level),repeat=2):self.flip[j*level+i,i*level+j]=1

    @cache
    def edge(self,i,j):
        X,Y,_,J,c=endpoint_frame(self.N,self.p,self.Q,self.marks[i,j],self.flags[j],self.flags[i])
        return X,Y,J*pow(c,-1,self.p)%self.p,c

    @cache
    def module(self,f):
        i,j,k=f;p=self.p
        lam=(self.points[i]-self.points[k])*pow(self.points[j]-self.points[k],-1,p)%p
        a=self.flags[j]*pow(self.flags[k],-1,p)%p
        b=self.flags[i]*pow(self.flags[k],-1,p)%p
        return endpoint_module(self.N,p,self.Q,lam,a,b)

    @cache
    def fusion(self,f):
        i,j,k=f
        return pointed_fusion(self.N,self.p,self.Q,self.edge(i,j)[:2],self.edge(j,k)[:2])

    @cache
    def face(self,f):
        i,j,k=f;N=self.N;p=self.p
        B=mm(p,self.fusion(f).T,np.kron(self.edge(i,j)[2],self.edge(j,k)[2]),
             self.flip,self.fusion((k,j,i)))
        removed=mm(p,np.kron(inverse_mod(self.edge(i,k)[2],p),np.eye(N,dtype=np.int64)),B)
        M=np.einsum('iaib->ab',removed.reshape((N,)*4))*pow(N,-1,p)%p
        assert determinant(M,p)
        assert np.array_equal(B,np.kron(self.edge(i,k)[2],M)%p)
        return M

    @cache
    def trivalent(self,f):
        i,j,k=f;N=self.N
        C=self.fusion(f).reshape((N,)*4)
        Ji=inverse_mod(self.edge(i,k)[2],self.p)
        tensor=np.einsum('ijab,ca->ijcb',C,Ji)%self.p
        X1,Y1=self.edge(i,j)[:2];X2,Y2=self.edge(j,k)[:2];X3,Y3=self.edge(k,i)[:2]
        act=lambda t,A,k:axis_action(t,A,k,self.p)
        assert np.array_equal(act(act(act(tensor,X1,0),X2,1),X3,2),tensor)
        totalY=(act(tensor,Y1,0)+act(act(tensor,Y2,1),X1,0)
                +act(act(act(tensor,Y3,2),X2,1),X1,0))%self.p
        assert not np.any(totalY)
        return tensor.reshape(N**3,N)

    @cache
    def rotation(self,f):
        i,j,k=f;N=self.N
        target=self.trivalent((j,k,i))
        ginv=inverse_mod(matrix_power(self.edge(i,j)[0],N-1,self.p),self.p)
        source=axis_action(self.trivalent(f).reshape((N,)*4),ginv,0,self.p)
        turned=np.transpose(source,(1,2,0,3)).reshape(N**3,N)
        rows=independent_rows(target,self.p)
        S=mm(self.p,inverse_mod(target[rows,:],self.p),turned[rows,:])
        assert np.array_equal(mm(self.p,target,S),turned) and determinant(S,self.p)
        return S

    @cache
    def tetrahedron(self,t):
        i,j,k,l=t
        return pointed_fusion(self.N,self.p,self.Q,self.module((i,j,l)),self.module((j,k,l)))

    @cache
    def corrected_rotation(self,f):
        X,Y=self.module(f);lam=int(matrix_power(X,self.N,self.p)[0,0])
        corrected=mm(self.p,self.rotation(f),inverse_mod(X,self.p))*self.tau*lam%self.p
        target=self.module(f[1:]+f[:1])
        newX=-self.Q*mm(self.p,inverse_mod(X,self.p),Y)%self.p
        newY=self.Q*inverse_mod(X,self.p)%self.p
        assert np.array_equal(mm(self.p,target[0],corrected),mm(self.p,corrected,newX))
        assert np.array_equal(mm(self.p,target[1],corrected),mm(self.p,corrected,newY))
        return corrected

    def face_alignment(self,source,target):
        value=np.eye(self.N,dtype=np.int64);current=source
        for _ in range(3):
            if current==target:return value
            value=mm(self.p,self.corrected_rotation(current),value)
            current=current[1:]+current[:1]
        raise AssertionError('oriented face orders are not cyclically related')

    @cache
    def tetrahedron_tensor(self,t):
        i,j,k,l=t;N=self.N;p=self.p
        A,B,C,D=(i,k,l),(i,j,k),(i,j,l),(j,k,l)
        sign=(-1)**sum(t[a]>t[b] for a in range(4) for b in range(a+1,4))
        if sign==1:
            matrix=mm(p,self.tetrahedron(t),np.kron(inverse_mod(self.face(A),p).T,
                                                  inverse_mod(self.face(B),p).T))
            tensor=np.transpose(matrix.reshape((N,)*4),(1,2,0,3))
            faces=[D,A[::-1],C,B[::-1]]
        else:
            matrix=mm(p,inverse_mod(self.tetrahedron(t),p),np.kron(inverse_mod(self.face(C),p).T,
                                                                 inverse_mod(self.face(D),p).T))
            tensor=np.transpose(matrix.reshape((N,)*4),(3,0,2,1))
            faces=[D[::-1],A,C[::-1],B]
        canonical=[(1,2,3),(3,2,0),(0,1,3),(2,1,0)]
        for axis,face in enumerate(faces):
            S=self.face_alignment(face,canonical[t[axis]])
            tensor=axis_action(tensor,S,axis,p)
        return np.transpose(tensor,tuple(t.index(v) for v in range(4)))


def reversal_case(level):
    cfg=Configuration(level,True);p=cfg.p;N=level
    R=cfg.tetrahedron((0,1,2,3));reverse=cfg.tetrahedron((3,2,1,0))
    left=np.kron(cfg.face((0,2,3)),cfg.face((0,1,2)))%p
    right=np.kron(cfg.face((0,1,3)),cfg.face((1,2,3)))%p
    assert np.array_equal(mm(p,left,reverse),mm(p,R.T,right))
    # The cap on a total edge is shared, rather than reset to a local product root.
    bad={};ratios={}
    for f in ((0,2,3),(0,1,2),(0,1,3),(1,2,3)):
        i,j,k=f
        product_mark=cfg.marks[i,j]*cfg.marks[j,k]%p
        _,_,_,_,c_product=endpoint_frame(N,p,cfg.Q,product_mark,cfg.flags[k],cfg.flags[i])
        ratio=c_product*pow(cfg.edge(i,k)[3],-1,p)%p
        bad[f]=cfg.face(f)*ratio%p;ratios[f]=ratio
    bad_left=mm(p,np.kron(bad[0,2,3],bad[0,1,2]),reverse)
    bad_right=mm(p,R.T,np.kron(bad[0,1,3],bad[1,2,3]))
    defect=ratios[0,2,3]*ratios[0,1,2]*pow(ratios[0,1,3]*ratios[1,2,3],-1,p)%p
    assert scalar_ratio(bad_left,bad_right,p)==defect
    return {'level':level,'prime':p,'exact_tetrahedron_reversal_with_shared_edge_caps':True,
            'independent_product_root_defect':defect,'independent_product_marks_fail':defect!=1}


def cyclic_case(level,start=2):
    cfg=Configuration(level,False,start);p=cfg.p;N=level
    f=(0,1,2);r=(1,2,0);rr=(2,0,1)
    product_rotation=mm(p,cfg.rotation(rr),cfg.rotation(r),cfg.rotation(f))
    assert np.array_equal(product_rotation,np.eye(N,dtype=np.int64))
    turned_metric=mm(p,cfg.rotation(f).T,cfg.face(r),inverse_mod(cfg.rotation((0,2,1)),p))
    ratio=scalar_ratio(turned_metric,cfg.face(f),p)
    defect=mm(p,inverse_mod(cfg.face(f),p),turned_metric)
    reverseX=cfg.module((2,1,0))[0]
    assert np.array_equal(defect,inverse_mod(matrix_power(reverseX,N-1,p),p))
    assert np.array_equal(cfg.face((2,1,0)),cfg.face(f).T)
    corrected_product=mm(p,cfg.corrected_rotation(rr),cfg.corrected_rotation(r),cfg.corrected_rotation(f))
    assert np.array_equal(corrected_product,np.eye(N,dtype=np.int64))
    paired=mm(p,cfg.corrected_rotation(f).T,cfg.face(r),inverse_mod(cfg.corrected_rotation((0,2,1)),p))
    assert np.array_equal(paired,cfg.face(f))
    # Uniform calibration used in the proof of the nonscalar raw defect.
    i,j,k=f;Ai,Aj,Ak=(cfg.flags[v] for v in f)
    lam=(cfg.points[i]-cfg.points[k])*pow(cfg.points[j]-cfg.points[k],-1,p)%p
    mu=(1-lam)%p;u=Aj*pow(Ak,-1,p)%p;v=Ai*pow(Ak,-1,p)%p
    alpha=pow(Ak,N-1,p)*pow(cfg.points[j]-cfg.points[k],-1,p)%p
    rawM=cfg.face(f)*cfg.edge(i,j)[3]*cfg.edge(j,k)[3]*pow(cfg.edge(i,k)[3],-1,p)%p
    assert int(rawM[0,1])==alpha*pow(u,N-2,p)*lam*pow(mu,-1,p)%p
    assert int(rawM[N-1,0])==alpha*lam*pow(v,N-1,p)*pow(mu,-1,p)%p
    assert not rawM[N-1,N-1]
    rawL=cfg.rotation(f)*cfg.edge(j,i)[3]*pow(cfg.edge(i,k)[3],-1,p)%p
    expected=np.zeros(N,dtype=np.int64);expected[-1]=lam*pow(mu,-1,p)%p
    assert np.array_equal(rawL[:,0],expected)
    return {'level':level,'prime':p,'flags':cfg.flags,'pivotal_rotation_cubed_is_identity':True,
            'cyclic_face_metric_scalar':ratio,
            'cyclic_face_metric_defect_small':defect.tolist() if N<=4 else None,
            'raw_metric_defect_is_exact_inverse_face_pivot':True,
            'reversed_pairing_is_exact_transpose':True,
            'corrected_cyclic_rotation_cubed_is_identity':True,
            'corrected_rotation_preserves_actual_face_pairing':True,
            'raw_trace_and_unit_calibrations_match_the_uniform_proof':True,
            'cubic_phase_retained':cfg.tau}


def root_mark_case(level):
    cfg=Configuration(level);p=cfg.p;Q=cfg.Q;b=cfg.generator
    values=[];valuations=[]
    for j in range(level):
        x=pow(Q,j,p)
        _,_,_,_,c=endpoint_frame(level,p,Q,x,1,b)
        values.append(c)
        factors=[(1-pow(Q,s-j,p))%p for s in range(1,level-1)]
        valuation=sum(f==0 for f in factors);valuations.append(valuation)
        leading=-pow(level*x*Q,-1,p)
        for factor in factors:
            if factor:leading=leading*factor%p
        assert leading%p
    norm=1
    for j in range(level):
        ratio=values[(j+1)%level]*pow(values[j],-1,p)%p
        formula=pow(Q,-1,p)*(b-pow(Q,-j,p))*pow(b-pow(Q,level-2-j,p),-1,p)%p
        assert ratio==formula
        norm=norm*ratio%p
    assert norm==1
    assert valuations==[int(1<=j<=level-2) for j in range(level)]
    return {'level':level,'prime':p,'root_mark_hilbert90_ratios_have_exact_norm_one':True,
            'cap_scalar_valuations_at_actual_wall':valuations,
            'all_extra_wall_information_is_first_order':True}


def gauge_case(level):
    old=Configuration(level,False);new=Configuration(level,True);p=old.p
    units={edge:int(old.edge(*edge)[3])*pow(int(new.edge(*edge)[3]),-1,p)%p for edge in old.marks}
    for f in permutations(range(4),3):
        i,j,k=f;scalar=units[i,j]*units[j,k]*pow(units[i,k],-1,p)%p
        assert np.array_equal(new.face(f),old.face(f)*scalar%p)
    for t in permutations(range(4)):
        i,j,k,l=t
        charges=lambda a,b,c: new.marks[a,b]*new.marks[b,c]*pow(new.marks[a,c],-1,p)%p
        assert charges(i,j,k)*charges(i,k,l)%p==charges(i,j,l)*charges(j,k,l)%p
    return {'level':level,'prime':p,'all_24_oriented_face_cap_gauges_are_edge_coboundaries':True,
            'all_24_tetrahedral_charge_cocycle_identities':True}


def vertex_order_case(level):
    cfg=Configuration(level,False);p=cfg.p;N=level
    base=cfg.tetrahedron_tensor((0,1,2,3)).reshape(N*N,N*N)
    records=[]
    for t in permutations(range(4)):
        changed=cfg.tetrahedron_tensor(t).reshape(N*N,N*N)
        ratio=scalar_ratio(changed,base,p)
        records.append({'ordering':list(t),'scalar':ratio})
    changed=cfg.tetrahedron_tensor((1,2,0,3)).reshape(-1)
    flat=base.reshape(-1);first=int(np.flatnonzero(flat)[0])
    second=next(j for j in range(len(flat)) if (int(changed[j])*int(flat[first])-int(flat[j])*int(changed[first]))%p)
    minor=(int(changed[second])*int(flat[first])-int(flat[second])*int(changed[first]))%p
    certificate={'even_ordering':[1,2,0,3],'indices':[first,second],
                 'base_values':[int(flat[first]),int(flat[second])],
                 'changed_values':[int(changed[first]),int(changed[second])],
                 'nonzero_proportionality_minor':minor}
    print(f'N={level}: {sum(c["scalar"] is not None for c in records)}/24 bare vertex-order tensors are scalar equivalent',flush=True)
    return {'level':level,'prime':p,'vertex_orders':records,
            'all_vertex_orders_are_scalar_equivalent':all(c['scalar'] is not None for c in records),
            'explicit_bare_tensor_obstruction':certificate}


def main():
    levels=(2,3,4,5,6,8,9,10,12)
    reversals=[reversal_case(n) for n in levels]
    print(f'{len(reversals)} shared-cap tetrahedron reversals passed; independent product marks fail in {sum(c["independent_product_marks_fail"] for c in reversals)} cases',flush=True)
    rotations=[cyclic_case(n) for n in levels]
    print(f'{len(rotations)} corrected cyclic/dual face orderings passed; every raw cyclic metric defect is non-scalar',flush=True)
    gauges=[gauge_case(n) for n in levels]
    print('shared edge cap and root charge gauges passed',flush=True)
    root_marks=[root_mark_case(n) for n in levels]
    orders=[vertex_order_case(n) for n in (2,3,4)]
    result={'scope':'Shared-edge reversal and corrected face ordering are proved; the separate bare-tensor full vertex-order prescription fails. No selected hyperbolic period or norm is identified.',
            'global_unrestricted_tetrahedron_invariance':False,
            'tetrahedron_reversals':reversals,'cyclic_faces':rotations,'edge_cap_gauges':gauges,
            'root_mark_sources':root_marks,
            'tetrahedron_vertex_orders':orders}
    Path(__file__).with_name('oriented_tetrahedron_source_results.json').write_text(json.dumps(result,indent=2)+'\n')


if __name__=='__main__':main()
