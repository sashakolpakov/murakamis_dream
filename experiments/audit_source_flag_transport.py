#!/usr/bin/env python3
"""Auxiliary source flags, exact adapters, and their first normal jet.

The quantum objects are the existing pointed cyclic endpoint modules.
We test moving-source projective covariance, the full scalar source
cocycle, an explicit anchor correction, and a nonzero normal shear.
No global ADO/geometric period identification is asserted.
"""

from functools import cache
from itertools import permutations, product
import json
from pathlib import Path

import numpy as np
import sympy as sp

from audit_actual_peripheral_fusion import inverse_mod
from audit_oriented_tetrahedron_source import Configuration, scalar_ratio
from audit_regular_holonomy_braiding import mm
from audit_relative_pivotal_duality import endpoint_module
from audit_standard_face_gluing import FaceFrames
from audit_standard_matrix_dilog_comparison import evaluation


def symbolic_certificate():
    pi,pj,pk,s,a,b,c,d=sp.symbols('pi pj pk s a b c d')
    F=lambda x:(a*x+b)/(c*x+d)
    t=lambda x,y,z,o:(y-o)*(x-z)/((x-o)*(y-z))
    assert sp.cancel(t(F(pi),F(pj),F(pk),F(s))-t(pi,pj,pk,s))==0
    assert sp.cancel(1-t(pi,pj,pk,s)
                     -(pk-s)*(pj-pi)/((pi-s)*(pj-pk)))==0
    epsilon,base,di,dj,dk,source=sp.symbols('epsilon base di dj dk source')
    assert sp.cancel(t(base+epsilon*di,base+epsilon*dj,base+epsilon*dk,
                       base+epsilon*source)-t(di,dj,dk,source))==0
    tau=epsilon/(s-base)
    assert sp.cancel((base+epsilon*di-s)/(base+epsilon*dj-s)
                     -(1-tau*di)/(1-tau*dj))==0
    return {'source_aware_Steinberg_parameter_is_projectively_invariant':True,
            'complement_identity_is_exact':True,
            'normal_source_flag_and_infinity_chart_are_exact_algebraic_identities':True}


def five_clique(vertices, powers, prime):
    """Five flags with differences and distances to source 0,1 all split."""
    n=len(vertices)
    adjacency=[]
    for i,x in enumerate(vertices):
        bits=0
        for j in range(i+1,n):
            if (x-vertices[j])%prime in powers:bits|=1<<j
        adjacency.append(bits)

    def search(bits,needed):
        if not needed:return []
        while bits.bit_count()>=needed:
            bit=bits&-bits;bits^=bit;i=bit.bit_length()-1
            found=search(bits&adjacency[i],needed-1)
            if found is not None:return [vertices[i],*found]
        return None
    return search((1<<n)-1,5)


@cache
def field_chart(N):
    for start in (10,20,40,80,160,320,640,1280,2560,5120):
        multiple=next(k for k in range(start,start+100)
                      if sp.isprime(12*N*k+1))
        p=12*N*multiple+1
        roots={pow(x,N,p):x for x in range(1,p)}
        powers=set(roots)
        candidates=sorted(x for x in powers if x!=1 and (x-1)%p in powers)
        points=five_clique(candidates,powers,p)
        if points is not None:
            generator=int(sp.primitive_root(p))
            q=pow(generator,(p-1)//(2*N),p)
            differences={}
            for i,j in product(range(5),repeat=2):
                if i<j:
                    differences[i,j]=roots[(points[i]-points[j])%p]
                    differences[j,i]=q*differences[i,j]%p
            return p,generator,q,points,roots,differences
    raise AssertionError('no split five-flag/two-source chart')


def config(N,p,generator,q,points,flags):
    cfg=object.__new__(Configuration)
    cfg.N=N;cfg.p=p;cfg.generator=generator;cfg.q=q;cfg.Q=q*q%p
    cfg.tau=pow(generator,(p-1)//(3*N),p)
    cfg.points=list(points);cfg.flags=list(flags)
    cfg.marks={(i,j):(1 if i<j else pow(cfg.Q,-1,p))
               for i,j in permutations(range(5),2)}
    cfg.flip=np.zeros((N*N,N*N),dtype=np.int64)
    for i,j in product(range(N),repeat=2):cfg.flip[j*N+i,i*N+j]=1
    return cfg


@cache
def pointing(frames,tet):
    cfg=frames.cfg;N=cfg.N;p=cfg.p;Q=cfg.Q
    i,j,k,l=tet
    _,eta,aA,_=frames.data((i,k,l))
    _,rhoB,aB,phiB=frames.data((i,j,k))
    _,alpha,aC,_=frames.data((i,j,l))
    _,beta,aD,_=frames.data((j,k,l))
    gamma=aA*pow(aD,-1,p)%p
    rootlogs={pow(Q,r,p):r for r in range(N)}
    e=rootlogs[gamma*pow(rhoB,-1,p)%p]
    value=1;total=1
    for r in range(1,N):
        value=value*pow(gamma,-1,p)*(1-eta*pow(Q,r,p))*pow(1-beta*pow(Q,r,p),-1,p)%p
        total=(total+value)%p
    kappa=total*pow(N,-1,p)%p
    assert kappa
    return kappa*int(phiB[e])%p


def case(N):
    p,generator,q,points,roots,B=field_chart(N);Q=q*q%p
    configurations=[
        config(N,p,generator,q,points,[roots[x] for x in points]),
        config(N,p,generator,q,points,[roots[(x-1)%p] for x in points]),
        config(N,p,generator,q,points,[1]*5),
    ]
    frames=[FaceFrames(cfg,B) for cfg in configurations]
    eye=np.eye(N,dtype=np.int64)

    @cache
    def adapter(target,source,f):
        return mm(p,inverse_mod(frames[target].data(f)[0],p),frames[source].data(f)[0])

    @cache
    def ratio(target,source,tet):
        return pointing(frames[target],tet)*pow(pointing(frames[source],tet),-1,p)%p

    @cache
    def edge_adapter(i,j):
        old,new=configurations[:2]
        if i<j:
            alpha=old.marks[i,j]
            H=evaluation(N,p,Q,alpha)
            values=[1];value=1
            for r in range(1,N):
                root=alpha*pow(Q,r,p)%p
                numerator=(new.flags[i]-new.flags[j]*root)%p
                denominator=(old.flags[i]-old.flags[j]*root)%p
                value=value*numerator*pow(denominator,-1,p)%p
                values.append(value)
            T=mm(p,inverse_mod(H,p),np.diag(values).astype(np.int64),H)
        else:
            forward=edge_adapter(j,i)
            T=mm(p,inverse_mod(new.edge(j,i)[2],p),inverse_mod(forward,p).T,old.edge(j,i)[2])
        X0,Y0=old.edge(i,j)[:2];X1,Y1=new.edge(i,j)[:2]
        assert np.array_equal(mm(p,T,X0),mm(p,X1,T))
        assert np.array_equal(mm(p,T,Y0),mm(p,Y1,T))
        return T

    @cache
    def pivotal_adapter(f):
        i,j,k=f;old,new=configurations[:2]
        removed=mm(p,np.kron(inverse_mod(edge_adapter(i,k),p),eye),
                   inverse_mod(new.fusion(f),p),np.kron(edge_adapter(i,j),edge_adapter(j,k)),old.fusion(f))
        S=np.einsum('iaib->ab',removed.reshape((N,)*4))*pow(N,-1,p)%p
        assert np.array_equal(removed,np.kron(eye,S)%p)
        return S

    changed_units=0
    for f in permutations(range(5),3):
        assert np.array_equal(mm(p,adapter(2,1,f),adapter(1,0,f)),adapter(2,0,f))
        assert np.array_equal(mm(p,adapter(0,1,f),adapter(1,0,f)),eye)
        assert np.any(adapter(1,0,f)[1:,0])
        changed_units+=1

    pivotal_weights={}
    for f in permutations(range(5),3):
        S=pivotal_adapter(f)
        theta=scalar_ratio(S,adapter(1,0,f),p)
        assert theta
        pivotal_weights[f]=theta
        assert np.array_equal(mm(p,S.T,configurations[1].face(f),pivotal_adapter(f[::-1])),
                              configurations[0].face(f))
        rotate=f[1:]+f[:1]
        assert np.array_equal(mm(p,configurations[1].corrected_rotation(f),S),
                              mm(p,pivotal_adapter(rotate),configurations[0].corrected_rotation(f)))

    # A moving source: inversion sends source 0 to infinity.
    A0=configurations[0].flags
    newpoints=[pow(x,-1,p) for x in points]
    newB={(i,j):q*value*pow(A0[i]*A0[j],-1,p)%p for (i,j),value in B.items()}
    moved=config(N,p,generator,q,newpoints,[1]*5)
    movedframes=FaceFrames(moved,newB)
    Ks={}
    for f in permutations(range(5),3):
        i,j,k=f
        scale=A0[j]*pow(A0[i],-1,p)%p
        K=np.diag([pow(scale,-r,p) for r in range(N)]).astype(np.int64)
        Ks[f]=K
        assert np.array_equal(mm(p,movedframes.data(f)[0],K),frames[0].data(f)[0])
        assert np.array_equal(K[:,0],eye[:,0])

    ordered=[]
    for tet in permutations(range(1,5)):
        i,j,k,l=tet
        A,Bf,C,D=(i,k,l),(i,j,k),(i,j,l),(j,k,l)
        R0=configurations[0].tetrahedron(tet)
        R1=configurations[1].tetrahedron(tet)
        raw_left=mm(p,R1,np.kron(adapter(1,0,A),adapter(1,0,Bf)))
        raw_right=mm(p,np.kron(adapter(1,0,C),adapter(1,0,D)),R0)
        c_t=ratio(1,0,tet)
        assert np.array_equal(raw_left,raw_right*c_t%p)

        # The cone/anchor cochain removes the full source-change scalar.
        face_weights={f:ratio(1,0,(0,*f)) for f in (A,Bf,C,D)}
        boundary=face_weights[C]*face_weights[D]*pow(face_weights[A]*face_weights[Bf],-1,p)%p
        assert c_t==boundary
        corrected=lambda f:adapter(1,0,f)*face_weights[f]%p
        assert np.array_equal(mm(p,R1,np.kron(corrected(A),corrected(Bf))),
                              mm(p,np.kron(corrected(C),corrected(D)),R0))
        assert np.array_equal(mm(p,R1,np.kron(pivotal_adapter(A),pivotal_adapter(Bf))),
                              mm(p,np.kron(pivotal_adapter(C),pivotal_adapter(D)),R0))
        assert c_t==pivotal_weights[C]*pivotal_weights[D]*pow(pivotal_weights[A]*pivotal_weights[Bf],-1,p)%p

        moved_left=mm(p,moved.tetrahedron(tet),np.kron(Ks[A],Ks[Bf]))
        moved_right=mm(p,np.kron(Ks[C],Ks[D]),R0)
        assert np.array_equal(moved_left,moved_right)
        ordered.append({'ordering':list(tet),'raw_source_change_scalar':c_t,
                        'anchor_face_scalars':{str(f):face_weights[f] for f in (A,Bf,C,D)},
                        'exact_anchor_corrected_source_transport':True,
                        'exact_unit_preserving_moving_source_inversion':True})

    five=(0,1,2,3,4)
    scalar_boundary=1
    for omitted in range(5):
        tet=five[:omitted]+five[omitted+1:]
        value=ratio(1,0,tet)
        scalar_boundary=scalar_boundary*(value if omitted%2==0 else pow(value,-1,p))%p
    assert scalar_boundary==1

    cap_turn_defects=[]
    for f in permutations(range(1,5),3):
        reverse=f[::-1];rotate=f[1:]+f[:1]
        weight=lambda face:ratio(1,0,(0,*face))
        corrected=lambda face:adapter(1,0,face)*weight(face)%p
        mu0=int(frames[0].pairing(f)[0,0]);mu1=int(frames[1].pairing(f)[0,0])
        xi0=int(frames[0].cyclic(f)[0,0]);xi1=int(frames[1].cyclic(f)[0,0])
        cap_defect=weight(f)*weight(reverse)*mu1*pow(mu0,-1,p)%p
        turn_defect=weight(f)*pow(weight(rotate),-1,p)*xi1*pow(xi0,-1,p)%p
        assert np.array_equal(mm(p,corrected(f).T,configurations[1].face(f),corrected(reverse)),
                              configurations[0].face(f)*cap_defect%p)
        assert np.array_equal(mm(p,configurations[1].corrected_rotation(f),corrected(f)),
                              mm(p,corrected(rotate),configurations[0].corrected_rotation(f))*turn_defect%p)
        cap_turn_defects.append({'face':list(f),'actual_cap_scalar_defect':cap_defect,
                                 'actual_cyclic_map_scalar_defect':turn_defect,
                                 'edge_induced_face_scalar_theta':pivotal_weights[f],
                                 'pivotal_repair_factor_theta_over_anchor':pivotal_weights[f]*pow(weight(f),-1,p)%p,
                                 'actual_pivotal_adapter_preserves_caps_and_turns_exactly':True})

    # Changing the cone vertex changes the face correction by an edge coboundary.
    anchor_changes=0
    for f in permutations((2,3,4)):
        i,j,k=f
        change=ratio(1,0,(1,*f))*pow(ratio(1,0,(0,*f)),-1,p)%p
        edge=lambda a,b:ratio(1,0,(0,1,a,b))
        expected=edge(i,k)*pow(edge(j,k)*edge(i,j),-1,p)%p
        assert change==expected
        anchor_changes+=1

    # First normal jet p_i=2+epsilon*delta_i. Sources 0 and 1
    # have weights 1/2 and 1; infinity has weight zero.
    delta_weight=(1-pow(2,-1,p))%p
    first_jets=[]
    for f in permutations(range(5),3):
        i,j,k=f;di,dj,dk=(points[v] for v in f)
        beta=B[i,k]*pow(B[j,k],-1,p)%p
        J=[0];total=0
        for r in range(1,N):
            value=beta*pow(Q,r,p)%p
            total=(total+value*pow(1-value,-1,p))%p
            J.append((-(dj-di)*total-r*(dk-di))%p)
        H=evaluation(N,p,Q,beta)
        first=mm(p,inverse_mod(H,p),np.diag(J).astype(np.int64),H)*delta_weight*pow(N,-1,p)%p
        lam=pow(beta,N,p)
        X,Y0=endpoint_module(N,p,Q,lam,1,1)
        _,Ydot=endpoint_module(N,p,Q,lam,(dj-dk)*pow(N,-1,p)%p,
                              (di-dk)*pow(N,-1,p)%p)
        assert np.array_equal(mm(p,first,X),mm(p,X,first))
        assert np.array_equal((mm(p,first,Y0)-mm(p,Y0,first))%p,Ydot*delta_weight%p)
        assert np.any(first[1:,0])
        first_jets.append({'face':list(f),'nonconstant_unit_shear':True})

    return {'level':N,'prime':p,'flag_points':points,
            'source_flags':['0','1','infinity'],
            'strict_source_adapter_compositions':60,
            'edge_induced_pivotal_face_adapters_and_cap_turn_naturality':60,
            'nonconstant_transported_units':changed_units,
            'ordered_kernel_comparisons':ordered,
            'five_flag_source_scalar_cocycle':True,
            'retained_actual_cap_and_turn_defects':cap_turn_defects,
            'anchor_changes_are_retained_edge_coboundaries':anchor_changes,
            'first_normal_jet_intertwining_and_nonzero_unit_shears':first_jets}


def main():
    records=[]
    for N in (2,3,4,5,6,9):
        records.append(case(N))
        print(f'N={N}: source adapters, moving-source covariance, anchor correction, and 60 normal shears passed',flush=True)
    result={'scope':'Existing pointed cyclic modules with an auxiliary source flag. Local projective/source transport and retained first normal data; no global selected knot-period/regulator norm theorem.',
            'generic_certificate':symbolic_certificate(),'configurations':records}
    Path(__file__).with_name('source_flag_transport_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS',flush=True)


if __name__=='__main__':main()
