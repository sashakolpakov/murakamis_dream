#!/usr/bin/env python3
"""Actual pure-braid jets and a genuine braided source groupoid.

The spectral test uses the literal ADO crossing and its actual pivot.
The groupoid test updates semicyclic centers and uses the full source
frames, including the source-at-infinity line orders. It is not a
global triangulation-state or volume theorem.
"""

from functools import cache
from itertools import product
import json
from pathlib import Path

import numpy as np

from audit_actual_peripheral_fusion import inverse_mod,module
from audit_casimir_braiding import highest_matrices,hermite_polynomials,solve,evaluate,chebyshev
from audit_cyclic_steinberg_lattice import rank,determinant
from audit_finite_sum_annihilator import field
from audit_kashaev_ado_pointing import color_matrices,reduced_period,WORDS
from audit_kashaev_crossing import quantum_group
from audit_regular_holonomy_braiding import mm
from audit_semicyclic_carry_braiding import positive,negative,transported
from audit_source_flag_carry_extension import branch_infinity_kernel
from audit_carry_recoupling_lattice import trees


def projector_zero(N,p,q,O):
    rows=[];values=[]
    for k in range((N+1)//2):
        c=(pow(q,2*k+1,p)+pow(q,-2*k-1,p))%p
        rows.append([pow(c,j,p) for j in range(N)]);values.append(int(k==0))
        if 2*k+1<N:
            rows.append([0]+[j*pow(c,j-1,p)%p for j in range(1,N)])
            values.append(0)
    coefficients=solve(np.array(rows,dtype=np.int64),np.array(values,dtype=np.int64),p)
    return evaluate(coefficients,O,p)


def spectral_case(N):
    p,generator,q=field(N);Q=q*q%p;rho=(q-pow(q,-1,p))%p
    E,F,K,Ki,_=highest_matrices(N,p,q)
    eye=np.eye(N,dtype=np.int64);big=np.eye(N*N,dtype=np.int64)
    Et=(np.kron(E,K)+np.kron(eye,E))%p
    Ft=(np.kron(F,eye)+np.kron(Ki,F))%p
    O=(mm(p,Ft,Et)*rho*rho+q*np.kron(K,K)+pow(q,-1,p)*np.kron(Ki,Ki))%p
    actual=color_matrices(N,p,q,pow(q,N-1,p));B=actual[0];pivot=actual[2]
    r,_,_=hermite_polynomials(N,p,q)
    assert np.array_equal(B,evaluate(r,O,p))
    mu=pow(generator,(p-1)//(4*N),p);lam=pow(mu,(N-1)**2,p)
    Rq,_=quantum_group(N,p,mu)
    swap=np.zeros_like(big)
    for a,b in product(range(N),repeat=2):swap[b*N+a,a*N+b]=1
    assert np.array_equal(mm(p,swap,Rq),B*lam%p)
    e0=projector_zero(N,p,q,O)
    c0=(q+pow(q,-1,p))%p;J=mm(p,(O-c0*big)%p,e0)
    assert np.array_equal(mm(p,e0,e0),e0)
    assert not np.any(mm(p,J,J)) and np.any(J)
    # This is the actual self-dual cup/cap, with its pivot retained.
    duality=np.zeros((N,N),dtype=np.int64)
    for a in range(N):duality[N-1-a,a]=pow(q,a*a,p)
    cup=inverse_mod(duality,p).T.reshape(N*N,1)
    cap=mm(p,pivot,duality).reshape(1,N*N)
    Pi=mm(p,cup,cap)
    assert not np.any(mm(p,Pi,Pi)) and rank(Pi,p)==1
    assert np.array_equal(J,Pi*pow(-1,N,p)*rho*rho%p)
    coefficient=pow(-1,N+1,p)*(N-1)*rho%p
    loop=mm(p,B,B)
    assert np.array_equal(mm(p,e0,(loop-big)%p),Pi*coefficient%p)
    localized=(big+Pi*coefficient)%p
    assert determinant(localized,p)==1
    assert np.array_equal(mm(p,localized,cup),cup)
    assert rank(J,p)==1 and rank(e0,p)==2*N
    powers=[]
    value=big.copy()
    for m in range(1,8):
        value=mm(p,loop,value)
        assert np.array_equal(mm(p,e0,(value-big)%p),Pi*(m*coefficient%p)%p)
        if m in (1,2,3,7):powers.append({'winding':m,'retained_nilpotent_coefficient':m*coefficient%p})
    partial=np.einsum('abcb->ac',mm(p,mm(p,e0,(loop-big)%p),np.kron(eye,pivot)).reshape((N,)*4))%p
    assert np.array_equal(partial,coefficient*eye%p) and coefficient
    assert np.array_equal(np.einsum('abcb->ac',mm(p,Pi,np.kron(eye,pivot)).reshape((N,)*4))%p,eye)
    # The actual meridian color splits the coincident pair. This is its
    # exact first coefficient, not a numerical small-parameter test.
    numerator=big.copy();denominator=4*rho%p
    for j in range(N-1):
        node=(pow(q,2*j+1,p)+pow(q,-2*j-1,p))%p
        numerator=mm(p,numerator,(O-node*big)%p)
        if j:denominator=denominator*(c0-node)%p
    residue=numerator*pow(denominator,-1,p)%p
    assert np.array_equal(residue,J*pow(4*rho,-1,p)%p)
    source_residue=residue*(4*N)%p
    assert np.array_equal(source_residue,Pi*pow(-1,N,p)*N*rho%p)
    return {'level':N,'prime':p,'actual_ADO_crossing_is_exact_normalized_Casimir_polynomial':True,
            'quantum_group_R_scalar_lambda0':lam,'original_ADO_zero_framing_twist':actual[3],
            'rank_of_complete_Casimir_projector':rank(e0,p),'rank_of_its_nilpotent':rank(J,p),
            'nilpotent_is_actual_cup_cap_with_full_pivot':True,
            'localized_holonomy_has_determinant_one_and_fixes_the_cup':True,
            'full_twist_source_coefficient':coefficient,'pivotal_closing_detects_it':True,
            'actual_meridian_projector_first_coefficient_is_exact':True,
            'full_affine_source_residue_in_U_minus_one':pow(-1,N,p)*N*rho%p,
            'nontrivial_pure_braid_powers':powers}


def meridian_case(N):
    p,generator,q=field(N);Q=q*q%p;M=generator;Y=M*M%p;U=pow(Y,N,p)
    eye=np.eye(N,dtype=np.int64);big=np.eye(N*N,dtype=np.int64)
    rho=(q-pow(q,-1,p))%p

    def decomposition(meridian):
        x=-meridian*pow(q,-1,p)%p
        E,F,K=module(N,p,q,x);Ki=inverse_mod(K,p)
        Et=(np.kron(E,K)+np.kron(eye,E))%p
        Ft=(np.kron(F,eye)+np.kron(Ki,F))%p
        Kt=np.kron(K,K)%p
        O=(mm(p,Ft,Et)*rho*rho+q*Kt+pow(q,-1,p)*np.kron(Ki,Ki))%p
        columns=[]
        for j in range(N):
            vector=np.zeros(N*N,dtype=np.int64);coefficient=1
            vector[j]=1
            for a in range(j):
                coefficient=-coefficient*int(E[j-a-1,j-a])*pow(int(E[a,a+1])*x*pow(Q,-(j-a-1),p),-1,p)%p
                vector[(a+1)*N+j-a-1]=coefficient
            assert not np.any(mm(p,Et,vector[:,None]))
            for r in range(N):
                columns.append(vector.copy());vector=mm(p,Ft,vector[:,None])[:,0]
            assert not np.any(vector)
        H=np.column_stack(columns);assert determinant(H,p)
        B=color_matrices(N,p,q,x)[0]
        y=meridian*meridian%p
        nodes=[(pow(q,-2*j-1,p)*y+pow(q,2*j+1,p)*pow(y,-1,p))%p for j in range(N)]
        values=[pow(-1,j,p)*pow(q,j*(j+1),p)*pow(y,-j,p)%p for j in range(N)]
        assert len(set(nodes))==N
        assert np.array_equal(mm(p,O,H),H*np.repeat(nodes,N)[None,:]%p)
        assert np.array_equal(mm(p,B,H),H*np.repeat(values,N)[None,:]%p)
        return H,B,O,(Et,Ft,Kt),nodes,values

    H,B,O,ops,nodes,values=decomposition(M)
    Hs,Bs,Os,opss,_,_=decomposition(q*M%p)
    shift=np.zeros_like(big)
    for j,r in product(range(N),repeat=2):shift[((j+1)%N)*N+r,j*N+r]=1
    G=mm(p,Hs,shift,inverse_mod(H,p));Gi=inverse_mod(G,p)
    for old,new in zip(ops,opss):assert np.array_equal(mm(p,G,old),mm(p,new,G))
    last=np.zeros(N*N,dtype=np.int64);last[-N:]=1
    E_last=mm(p,H*last[None,:],inverse_mod(H,p))
    source=(1+pow(U,-1,p))%p
    assert np.array_equal(mm(p,Gi,Bs,G),(-pow(Y,-1,p)*B+source*E_last)%p)
    assert rank(E_last,p)==N
    assert not np.any((chebyshev(O,N,p)+(U+pow(U,-1,p))*big)%p)
    V=np.array([[pow(node,j,p) for j in range(N)] for node in nodes],dtype=np.int64)
    coefficients=solve(V,np.array(values,dtype=np.int64),p)
    assert np.array_equal(evaluate(coefficients,O,p),B)
    norm=1
    for j in range(N):norm=-norm*pow(Y*pow(Q,j,p)%p,-1,p)%p
    assert norm==-pow(U,-1,p)%p
    norm_r=1
    for value in values:norm_r=norm_r*value%p
    assert determinant(B,p)==pow(norm_r,N,p)
    Hminus,_,_,_,_,_=decomposition(-M%p)
    parity=np.kron(eye,np.diag([pow(-1,j,p) for j in range(N)]).astype(np.int64))
    labels=np.repeat([pow(-1,j,p) for j in range(N)],N)
    assert np.array_equal(Hminus,mm(p,parity,H)*labels[None,:]%p)
    return {'level':N,'prime':p,'meridian_M':M,'U_M_to_2N':U,
            'actual_tensor_meridian_shift_intertwines_E_F_K':True,
            'crossing_affine_source_equation_exact':True,
            'retained_source_coefficient_one_plus_U_inverse':source,
            'homogeneous_cyclic_norm_minus_U_inverse':norm,
            'source_projector_rank':N,'Casimir_chebyshev_base_and_spectral_norm_exact':True,
            'N_step_meridian_transport_retains_parity_and_spectral_sign':True}


def groupoid_case(N,kind):
    p,generator,q=field(N);Q=q*q%p;x=generator if kind=='generic' else pow(q,N-1,p)
    k=pow(x,N,p);size=N**3;eye=np.eye(N,dtype=np.int64)
    states=list(product(range(N),repeat=3));kappa=np.array([sum(s)//N for s in states])
    # These inverse endpoint factors make the normalized total Y
    # precisely the original iterated coproduct of F.
    scale=np.array([pow(x,-sum(j*s[j] for j in range(3)),p) for s in states],dtype=np.int64)
    scaleinv=np.array([pow(int(v),-1,p) for v in scale],dtype=np.int64)
    zero=(0,0,0,0);alternate=(0,1,0,1)
    TL,TR=trees(0,3)
    def flags(a):
        result=[0]
        for j,value in enumerate(a):result.append((result[-1]-pow(k,-j,p)*value)%p)
        return tuple(result)
    words=([(0,1),(1,1),(0,1)],[(1,1),(0,1),(1,1)],
           [(0,1),(0,-1)],[(1,1),(1,-1)])
    def valid(a):
        for word in words:
            now=list(a)
            if len(set(flags(now)))<4:return False
            for j,sign in word:
                now[j:j+2]=transported(N,p,q,x,*now[j:j+2],sign)
                if len(set(flags(now)))<4:return False
        return True
    initial=next((1,a,b) for a,b in product(range(2,30),repeat=2) if valid((1,a,b)))
    @cache
    def frame(a,tree,branch):
        return branch_infinity_kernel(N,p,Q,flags(a),tree,branch)
    def leafarrow(a,j,sign):
        local=(positive if sign>0 else negative)(N,p,q,x,*a[j:j+2])
        matrix=np.kron(local,eye) if j==0 else np.kron(eye,local)
        return scaleinv[:,None]*matrix*scale[None,:]%p
    actual=color_matrices(N,p,q,x)
    def nilarrow(j,sign):
        local=actual[0 if sign>0 else 1]
        matrix=np.kron(local,eye) if j==0 else np.kron(eye,local)
        return scaleinv[:,None]*matrix*scale[None,:]%p
    source_image=(kappa==0).astype(np.int64)
    def path(word,charts):
        a=tuple(initial);value=np.eye(size,dtype=np.int64);lineorder=0;checks=0
        oldM,oldw=frame(a,*charts[0])
        for index,(j,sign) in enumerate(word):
            new=list(a);new[j:j+2]=transported(N,p,q,x,*new[j:j+2],sign);new=tuple(new)
            newM,neww=frame(new,*charts[index+1])
            assert flags(a)[-1]==flags(new)[-1]
            leaf=leafarrow(a,j,sign)
            row,col=np.nonzero(leaf)
            assert all(kappa[r]<=kappa[c] for r,c in zip(row,col))
            assert np.array_equal(np.where(kappa[:,None]==kappa[None,:],leaf,0),nilarrow(j,sign))
            arrow=mm(p,inverse_mod(newM,p),leaf,oldM)
            relative=np.einsum('iaib->ab',arrow.reshape(N,N*N,N,N*N))*pow(N,-1,p)%p
            assert np.array_equal(arrow,np.kron(eye,relative)%p)
            Aold=inverse_mod(oldM,p)*source_image[None,:]%p
            Anew=inverse_mod(newM,p)*source_image[None,:]%p
            assert np.array_equal(mm(p,arrow,Aold),mm(p,Anew,nilarrow(j,sign)))
            value=mm(p,arrow,value);lineorder+=neww-oldw
            a=new;oldM,oldw=newM,neww;checks+=1
        return a,value,lineorder,checks
    A=path(words[0],[(TL,zero),(TR,alternate),(TL,alternate),(TR,alternate)])
    B=path(words[1],[(TL,zero),(TL,alternate),(TR,zero),(TR,alternate)])
    assert A[0]==B[0] and A[2]==B[2]==1 and np.array_equal(A[1],B[1])
    for word in words[2:]:
        back=path(word,[(TL,zero),(TR,alternate),(TL,zero)])
        assert back[0]==initial and back[2]==0 and np.array_equal(back[1],np.eye(size,dtype=np.int64))

    # A closed center line, with genuine braids and both source lines.
    fixed=tuple(pow(k,-j,p) for j in range(3))
    for j in (0,1):
        for sign in (1,-1):
            assert transported(N,p,q,x,*fixed[j:j+2],sign)==fixed[j:j+2]
    matrices=[frame(fixed,TL,zero)[0],frame(fixed,TR,alternate)[0]]
    pivot=np.diag(actual[2])
    cut=np.array([int(a==0)*int(pivot[b])*int(pivot[c])%p for a,b,c in states],dtype=np.int64)
    period_records=[]
    for word in WORDS:
        value=np.eye(size,dtype=np.int64)
        for j,sign in word:value=mm(p,value,leafarrow(fixed,j,sign))
        twist=pow(actual[3],-sum(sign for _,sign in word),p)
        target=reduced_period(N,p,*actual,word)
        closed=np.einsum('abcdbc,b,c->ad',value.reshape((N,)*6),pivot,pivot)%p
        assert np.array_equal(closed*twist%p,target*eye%p)
        for M in matrices:
            rec=mm(p,inverse_mod(M,p),cut[:,None]*value%p,M)
            assert int(np.trace(rec))*twist%p==target
        period_records.append({'word':word,'actual_cut_value':target,'both_source_lines_keep_original_whole_cut':True})
    return {'level':N,'color':kind,'prime':p,'initial_variable_centers':initial,
            'raw_K_N_root_k':k,'actual_meridian_norm_U':k*k%p,
            'mixed_braid_tree_source_relation_exact':True,'total_source_line_order_on_both_paths':1,
            'inverse_endpoint_factors_preserve_actual_total_F_and_all_arrows_factor_on_relatives':True,
            'inverse_paths_keep_source_lattice_and_close_exactly':True,
            'actual_specialization_image_naturality_on_every_arrow':True,
            'ordinary_source_image_rank':int(np.count_nonzero(kappa==0)),
            'retained_Tor_directions':int(np.count_nonzero(kappa>0)),
            'original_periods':period_records}


def main():
    spectral=[];groupoids=[];meridians=[]
    for N in (2,3,4,5,6,8,9,10,12,15):
        spectral.append(spectral_case(N));print(f'N={N}: actual pure-braid cup/cap jet and closing scalar passed',flush=True)
    for N in (2,3,4,5,6,9):
        meridians.append(meridian_case(N));print(f'N={N}: actual meridian shift and full affine Casimir source passed',flush=True)
    for N in (2,3,4,5,6):
        for kind in ('generic','Kashaev'):
            groupoids.append(groupoid_case(N,kind));print(f'N={N}, {kind}: genuine braided source groupoid passed',flush=True)
    result={'scope':'Actual nontrivial pure-braid spectral jet and genuine recoupling/source transport with moving centers. This does not disprove a differently decorated tetrahedral symmetry or prove the global geometric quantum-A/volume comparison.',
            'actual_pure_braid_jets':spectral,'actual_meridian_Casimir_sources':meridians,
            'braided_source_groupoids':groupoids}
    Path(__file__).with_name('braided_source_groupoid_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS',flush=True)


if __name__=='__main__':main()
