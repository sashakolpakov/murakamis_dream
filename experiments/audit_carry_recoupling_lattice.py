#!/usr/bin/env python3
"""Uniform carry lattice, local recoupling moves and the actual cut period.

All degeneration calculations use valuations and leading coefficients,
not a small numerical parameter. Cyclic wrap terms are retained in the
specialized carry operator. The auxiliary crossing lift is not asserted
to satisfy a generic Yang--Baxter relation.
"""

from collections import Counter
from functools import cache
from itertools import product
import json
from math import comb
from pathlib import Path

import numpy as np
import sympy as sp

from audit_actual_peripheral_fusion import inverse_mod
from audit_cyclic_steinberg_lattice import cyclic_matrices, determinant
from audit_factorial_source_torsor import primitive
from audit_finite_sum_annihilator import field, scalar_data
from audit_kashaev_ado_pointing import WORDS, color_matrices, reduced_period
from audit_regular_holonomy_braiding import mm


@cache
def trees(start,count):
    if count==1:return (start,)
    return tuple((left,right) for size in range(1,count)
                 for left in trees(start,size) for right in trees(start+size,count-size))


def leaves(tree):
    return (tree,) if isinstance(tree,int) else leaves(tree[0])+leaves(tree[1])


def nodes(tree):
    if isinstance(tree,int):return []
    return [(leaves(tree[0]),leaves(tree[1]))]+nodes(tree[0])+nodes(tree[1])


def right_rotations(tree):
    if isinstance(tree,int):return []
    left,right=tree;result=[]
    if not isinstance(left,int):
        A,B=left;C=right
        result.append(((A,(B,C)),(leaves(A),leaves(B),leaves(C))))
    for changed,triple in right_rotations(left):result.append(((changed,right),triple))
    for changed,triple in right_rotations(right):result.append(((left,changed),triple))
    return result


def row_matrix(level,prime,Q,directions,tree):
    b=len(directions);indices=list(product(range(level),repeat=b));internal=nodes(tree)
    assert len(internal)==b-1
    rows=[];carries=[];minimum=0
    for state in indices:
        carry=sum(state)//level;carries.append(carry);residue=sum(state)%level
        coeff=np.array([pow(Q,residue*a,prime) for a in range(level)],dtype=np.int64)
        valuation=np.zeros(level,dtype=np.int64)
        for L,R in internal:
            I=L+R;ri=sum(state[j] for j in I)%level;rr=sum(state[j] for j in R)%level
            local_carry=(sum(state[j] for j in L)%level+rr)//level
            def factors(subset,res):
                values=[1];v=[0]
                for d in range(1,level):
                    phase=pow(Q,d+res,prime)
                    unit=sum(directions[j] for j in subset)%prime if phase==1 else (1-phase)%prime
                    assert unit
                    values.append(values[-1]*unit%prime);v.append(v[-1]+int(phase==1))
                return values,v
            numerator,vn=factors(I,ri);denominator,vd=factors(R,rr)
            vv=np.array([a-b for a,b in zip(vn,vd)],dtype=np.int64)
            assert np.all(vv+local_carry>=0)
            cc=np.array([a*pow(d,-1,prime)%prime for a,d in zip(numerator,denominator)],dtype=np.int64)
            coeff=np.kron(coeff,cc)%prime
            valuation=(valuation[:,None]+vv[None,:]).reshape(-1)
        assert np.all(valuation+carry>=0)
        minimum=min(minimum,int(np.min(valuation)))
        rows.append(np.where(valuation+carry==0,coeff,0))
    M=np.vstack(rows);det=determinant(M,prime);assert det
    assert np.array_equal(M[:,0],np.array([int(k==0) for k in carries],dtype=np.int64))
    expected=(b-1)*(level-1)*level**(b-1)//2
    assert sum(carries)==expected
    return M,np.array(carries,dtype=np.int64),det,minimum


@cache
def clebsch(level,prime,Q,s,t):
    X1,Y1,_,_=cyclic_matrices(level,prime,Q,s)
    X2,Y2,_,_=cyclic_matrices(level,prime,Q,t)
    I=np.eye(level,dtype=np.int64);XT=np.kron(X1,X2)%prime
    D=(np.kron(X1,I)+np.kron(Y1,inverse_mod(Y2,prime)))%prime
    vacuum=np.zeros(level*level,dtype=np.int64);vacuum[0]=1
    relative=[];v=vacuum.copy()
    for j in range(level):relative.append(v);v=mm(prime,D,v[:,None])[:,0]
    columns=[]
    for a in range(level):
        for j in range(level):
            v=relative[j].copy()
            for _ in range(a):v=mm(prime,XT,v[:,None])[:,0]
            columns.append(v)
    C=np.column_stack(columns)
    assert determinant(C,prime) and np.array_equal(C[:,0],vacuum)
    return C


def local_move(level,prime,Q,directions,old,new,triple,oldM,newM):
    A,B,C=triple;all_leaves=A+B+C
    key_old=(A+B,C);key_child=(A,B);key_new=(A,B+C);key_newchild=(B,C)
    no=nodes(old);nn=nodes(new);b=len(directions)
    oldkeys=no.index(key_old)+1,no.index(key_child)+1
    newkeys=nn.index(key_new)+1,nn.index(key_newchild)+1
    common=set(no)&set(nn)
    ao=sum(directions[j] for j in all_leaves)%prime
    bc=sum(directions[j] for j in B+C)%prime;cc=sum(directions[j] for j in C)%prime
    s=ao*pow(bc,-1,prime)%prime;t=bc*pow(cc,-1,prime)%prime
    small=clebsch(level,prime,Q,s,t)
    states=list(product(range(level),repeat=b));expected=np.zeros_like(oldM)
    for column,source in enumerate(states):
        oldlocal=source[oldkeys[0]]*level+source[oldkeys[1]]
        for row,target in enumerate(states):
            if target[0]!=source[0]:continue
            if any(source[no.index(key)+1]!=target[nn.index(key)+1] for key in common):continue
            expected[row,column]=small[target[newkeys[0]]*level+target[newkeys[1]],oldlocal]
    assert np.array_equal(mm(prime,newM,expected),oldM)
    return {'level':level,'leaves':b,'old':str(old),'new':str(new),
            'local_pointed_Clebsch_with_exact_spectators_matches':True}


def carry_crossings(level,prime,q,x,direction_right):
    Q=q*q%prime;e,c,ci=scalar_data(level,prime,q,x)
    pos=np.zeros((level*level,level*level),dtype=np.int64);neg=np.zeros_like(pos)
    for a,b in product(range(level),repeat=2):
        ecoef=1
        for k in range(a+1):
            if k:ecoef=ecoef*e[a-k+1]%prime
            u,v=a-k,(b+k)%level;wrap=level*direction_right if b+k>=level else 1
            value=c[k]*ecoef*wrap*pow(x,-u-v,prime)*pow(Q,u*v,prime)%prime
            pos[v*level+u,a*level+b]=value
        ecoef=1
        for k in range(b+1):
            if k:ecoef=ecoef*e[b-k+1]%prime
            u,v=b-k,(a+k)%level;wrap=level*direction_right if a+k>=level else 1
            neg[u*level+v,a*level+b]=ci[k]*ecoef*wrap*pow(x,a+b,prime)*pow(Q,-a*b,prime)%prime
    assert np.array_equal(mm(prime,pos,neg),np.eye(level*level,dtype=np.int64))
    return pos,neg


def period_case(level,directions,matrices):
    prime,generator,q=field(level);Q=q*q%prime;b=3;size=level**b
    states=list(product(range(level),repeat=b));kappa=np.array([sum(a)//level for a in states])
    F=primitive(level,Q,1,prime)
    gauge=np.array([int(F[a[0]])*int(F[a[1]])*int(F[a[2]])%prime for a in states],dtype=np.int64)
    inverses={tree:inverse_mod(M* np.array([pow(int(g),-1,prime) for g in gauge])[:,None]%prime,prime)
              for tree,M in matrices.items()}
    I=np.eye(level,dtype=np.int64);records=[]
    for kind,x in [('generic',generator),('Kashaev',pow(q,level-1,prime))]:
        actual=color_matrices(level,prime,q,x);pairs=[carry_crossings(level,prime,q,x,directions[j+1]) for j in range(2)]
        embedded={}
        for j in range(2):
            for sign in (1,-1):
                local=pairs[j][0 if sign>0 else 1]
                value=np.kron(local,I) if j==0 else np.kron(I,local)
                rows,cols=np.nonzero(value)
                assert all(kappa[r]<=kappa[c] for r,c in zip(rows,cols))
                embedded[j,sign]=value
        pivotal=np.diag(actual[2]);cut=np.array([int(a[0]==0)*int(pivotal[a[1]])*int(pivotal[a[2]])%prime for a in states],dtype=np.int64)
        for word in WORDS:
            B=np.eye(size,dtype=np.int64)
            for j,sign in word:B=mm(prime,B,embedded[j,sign])
            value=int(np.dot(cut,np.diag(B)))%prime
            value=value*pow(actual[3],-sum(sign for _,sign in word),prime)%prime
            target=reduced_period(level,prime,*actual,word)
            assert value==target
            sectors={int(k):int(np.dot(cut*(kappa==k),np.diag(B)))
                     *pow(actual[3],-sum(sign for _,sign in word),prime)%prime
                     for k in range(int(max(kappa))+1)}
            assert sum(sectors.values())%prime==target
            for tree,M in matrices.items():
                Mv=M*np.array([pow(int(g),-1,prime) for g in gauge])[:,None]%prime
                inv=inverses[tree]
                transported=mm(prime,inv,cut[:,None]*B%prime,Mv)
                trace=int(np.trace(transported))%prime
                trace=trace*pow(actual[3],-sum(sign for _,sign in word),prime)%prime
                assert trace==target
            records.append({'level':level,'color':kind,'word':word,'directions':directions,
                            'actual_cut_value':target,'all_trees_same_actual_period':True,
                            'selected_trace_by_carry_sector':sectors,
                            'full_framing_and_pivotal_factor_retained':True})
    # A genuine wrap is present even though it cannot close a cut trace.
    pos=pairs[0][0];rows,cols=np.nonzero(pos)
    assert any((r//level+r%level)<(c//level+c%level) for r,c in zip(rows,cols))
    return records


def exact_lost_source_example():
    E=sp.Matrix([[0,1],[0,0]]);F=E.T
    D=sp.diag(1,-sp.I,-sp.I,1);P=sp.zeros(4)
    for a,b in product(range(2),repeat=2):P[2*b+a,2*a+b]=1
    plus=P*D*(sp.eye(4)+2*sp.I*sp.kronecker_product(E,F))
    minus=(sp.eye(4)-2*sp.I*sp.kronecker_product(E,F))*D.inv()*P
    B=sp.eye(8)
    for j,sign in WORDS[0]:
        local=plus if sign>0 else minus
        B=B*(sp.kronecker_product(local,sp.eye(2)) if j==0
             else sp.kronecker_product(sp.eye(2),local))
    pivot=[-sp.I,sp.I]
    values=[sp.simplify(sum(B[4*a+2*b+c,4*a+2*b+c]*pivot[b]*pivot[c]
                           for a,b,c in product(range(2),repeat=3)
                           if a==0 and (a+b+c)//2==k)) for k in (0,1)]
    assert values==[3,2]
    return {'knot':'figure_eight','level':2,'field':'Q(i)',
            'carry_zero_image_contribution':3,'retained_Tor_source_contribution':2,
            'actual_Kashaev_value':5,'discarding_the_source_changes_the_period':True}


def main():
    lattices=[];moves=[];periods=[]
    cases=[(2,b) for b in range(2,7)]+[(3,b) for b in range(2,5)]+[(4,2),(4,3),(5,3),(6,3),(8,2),(9,2),(10,2),(12,2)]
    for level,b in cases:
        prime,_,q=field(level);Q=q*q%prime;directions=list(range(1,b+1));all_trees=trees(0,b);matrices={}
        for tree in all_trees:
            M,kappa,det,pole=row_matrix(level,prime,Q,directions,tree);matrices[tree]=M
            assert -pole==int(max(kappa))
            assert int(np.count_nonzero(kappa==0))==comb(level+b-1,b)
            lattices.append({'level':level,'leaves':b,'tree':str(tree),'prime':prime,
                             'row_scaled_leading_determinant':det,'Smith_pole_multiplicities':dict(Counter(map(int,kappa))),
                             'largest_entry_pole':-pole,
                             'bounded_source_normal_jet_order':int(max(kappa)),
                             'specialization_image_rank':int(np.count_nonzero(kappa==0)),
                             'Tor_source_dimension':int(np.count_nonzero(kappa>0)),
                             'common_carry_image_lattice_exact':True,'unit_pointing_lies_in_actual_sublattice':True})
        for old in all_trees:
            for new,triple in right_rotations(old):
                moves.append(local_move(level,prime,Q,directions,old,new,triple,matrices[old],matrices[new]))
        if b==3 and level<=6:periods.extend(period_case(level,directions,matrices))
        print(f'N={level}, leaves={b}: {len(all_trees)} integral tree frames passed',flush=True)
    result={'scope':'Common integral recoupling lattice, exact local moves and original ADO cut trace; no geometric knot-character or selected regulator-norm identification.',
            'tree_lattices':lattices,'local_recoupling_moves':moves,'actual_cut_periods':periods,
            'exact_source_loss_example':exact_lost_source_example()}
    Path(__file__).with_name('carry_recoupling_lattice_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(f'PASS: {len(lattices)} trees, {len(moves)} local moves, {len(periods)} actual periods',flush=True)


if __name__=='__main__':main()
