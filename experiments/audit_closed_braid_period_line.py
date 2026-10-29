#!/usr/bin/env python3
"""Closed-braid Hom lines and their normal deformation equations.

Independent free-word/Fox and matrix linearizations, Artin fixed fibers,
exact metabelian lifts on the Alexander divisor, and actual quantum
cut functionals. No equality of geometric and augmentation periods or
volume estimate is asserted.
"""

from itertools import product
import json
from pathlib import Path
from random import Random

import numpy as np
import sympy as sp

from audit_actual_peripheral_fusion import inverse_mod, matrix_power, tensor_module
from audit_cyclic_steinberg_lattice import determinant, rank
from audit_finite_sum_annihilator import field, cut_matrix_dense
from audit_kashaev_ado_pointing import WORDS, color_matrices
from audit_marked_braid_holonomy import from_holonomies, braid_groups
from audit_regular_holonomy_braiding import (
    regular_module, central, embed, holonomy, mm, chebyshev,
    matrix_series_multiply, sampled_module,
)

t = sp.Symbol('t', nonzero=True)


def burau(strands,word):
    result = sp.eye(strands)
    for j,sign in word:
        step = sp.eye(strands)
        block = sp.Matrix([[1-1/t,1/t],[1,0]]) if sign>0 else sp.Matrix([[0,1],[t,1-t]])
        step[j:j+2,j:j+2] = block
        result = step*result
    return result.applyfunc(sp.expand)


def reduce_word(word):
    result=[]
    for a in word:
        if result and result[-1]==-a:
            result.pop()
        else:
            result.append(a)
    return result


def free_braid(strands,word):
    result=[[i+1] for i in range(strands)]
    inv=lambda w:[-a for a in reversed(w)]
    for j,sign in word:
        a,b=result[j:j+2]
        result[j:j+2] = ([reduce_word(inv(a)+b+a),a] if sign>0
                         else [b,reduce_word(b+a+inv(b))])
    return result


def fox_row(word,strands):
    result=[0]*strands
    degree=0
    for a in word:
        result[abs(a)-1] += t**degree if a>0 else -t**(degree-1)
        degree+=1 if a>0 else -1
    assert degree==1
    return [sp.expand(a) for a in result]


def normalize_laurent(value):
    value=sp.expand(value)
    smallest=min(term.as_powers_dict().get(t,0) for term in sp.Add.make_args(value))
    value=sp.Poly(sp.expand(value/t**smallest),t)
    if value.LC()<0:
        value=-value
    return value.as_expr()


def permutation_is_knot(strands,word):
    values=list(range(strands))
    for j,_ in word:
        values[j],values[j+1]=values[j+1],values[j]
    seen=set();a=0
    while a not in seen:
        seen.add(a);a=values[a]
    return len(seen)==strands


def symbolic_cases():
    rng=Random(268104)
    words=[(3,list(w)) for w in WORDS]+[(2,[(0,1)]*3)]
    while len(words)<24:
        strands=rng.randrange(2,5)
        length=rng.randrange(3,11)
        word=[(rng.randrange(strands-1),rng.choice((-1,1))) for _ in range(length)]
        if permutation_is_knot(strands,word):
            words.append((strands,word))
    records=[]
    for strands,word in words:
        B=burau(strands,word)
        F=sp.Matrix([fox_row(w,strands) for w in free_braid(strands,word)])
        assert B==F
        assert all(sp.expand(sum(B[i,j] for j in range(strands))-1)==0 for i in range(strands))
        minor=(sp.eye(strands)-B)[1:,1:]
        cofactor=sp.expand(minor.det())
        assert abs(cofactor.subs(t,1))==1
        records.append({'strands':strands,'word':word,'Fox_equals_matrix_linearization':True,
                        'unit_cofactor_at_one':int(cofactor.subs(t,1)),
                        'normalized_Alexander_cofactor':str(normalize_laurent(cofactor))})
    assert records[0]['normalized_Alexander_cofactor']=='t**2 - 3*t + 1'
    assert records[3]['normalized_Alexander_cofactor']=='t**2 - t + 1'
    hopf=(sp.eye(2)-burau(2,[(0,1)]*2))[1:,1:].det()
    assert hopf.subs(t,1)==0
    return words,records,{'two_component_exception_at_one_verified':True}


def conjugation_matrix(M,prime):
    Mi=inverse_mod(M,prime)
    columns=[]
    for j in range(4):
        unit=np.zeros((2,2),dtype=np.int64);unit.flat[j]=1
        columns.append(mm(prime,M,unit,Mi).reshape(-1))
    return np.column_stack(columns)


def block_linearization(strands,word,M,prime):
    A=conjugation_matrix(M,prime);Ai=inverse_mod(A,prime)
    I=np.eye(4,dtype=np.int64)
    result=np.eye(4*strands,dtype=np.int64)
    for j,sign in word:
        step=np.eye(4*strands,dtype=np.int64)
        block=(np.block([[I-Ai,Ai],[I,np.zeros_like(I)]]) if sign>0
               else np.block([[np.zeros_like(I),I],[A,I-A]]))%prime
        step[4*j:4*j+8,4*j:4*j+8]=block
        result=mm(prime,step,result)
    return (result-np.eye(4*strands,dtype=np.int64))[4:,4:]%prime


def ms_inverse(a,prime):
    result=[inverse_mod(a[0],prime)]
    for n in range(1,len(a)):
        total=sum(mm(prime,a[j],result[n-j]) for j in range(1,n+1))%prime
        result.append(-mm(prime,result[0],total)%prime)
    return result


def ms_braid(values,word,prime):
    result=[[x.copy() for x in a] for a in values]
    mul=lambda a,b:matrix_series_multiply(a,b,prime)
    for j,sign in word:
        a,b=result[j:j+2]
        result[j:j+2]=([mul(mul(ms_inverse(a,prime),b),a),a] if sign>0
                       else [b,mul(mul(b,a),ms_inverse(b,prime))])
    return result


def artin_case(strands,word,kind):
    prime=1009
    if kind=='identity':
        M0=np.eye(2,dtype=np.int64)
    elif kind=='unipotent':
        M0=np.array([[1,1],[0,1]],dtype=np.int64)
    else:
        for s in range(2,prime):
            M0=np.diag([s,pow(s,-1,prime)]).astype(np.int64)
            if determinant(block_linearization(strands,word,M0,prime),prime):
                break
    J=block_linearization(strands,word,M0,prime)
    Ji=inverse_mod(J,prime)
    # A genuine moving SL_2 meridian, with all three Artin orders retained.
    eye=np.eye(2,dtype=np.int64);zero=np.zeros_like(eye)
    upper=np.array([[0,1],[0,0]],dtype=np.int64)
    lower=2*upper.T
    meridian=[M0.copy(),mm(prime,M0,upper+lower),mm(prime,M0,upper,lower),zero.copy()]
    rng=Random(3141+strands+len(word))
    values=[[x.copy() for x in meridian] for _ in range(strands)]
    for a in values[1:]:
        for r in range(1,4):
            a[r]=(a[r]+np.array([rng.randrange(prime) for _ in range(4)],dtype=np.int64).reshape(2,2))%prime
    for r in range(1,4):
        changed=ms_braid(values,word,prime)
        residual=np.concatenate([mm(prime,(changed[j][r]-values[j][r])%prime,
                                      inverse_mod(M0,prime)).reshape(-1) for j in range(1,strands)])
        correction=-mm(prime,Ji,residual.reshape(-1,1))[:,0]%prime
        for j in range(1,strands):
            values[j][r]=(values[j][r]+mm(prime,correction[4*(j-1):4*j].reshape(2,2),M0))%prime
        changed=ms_braid(values,word,prime)
        assert all(np.array_equal(a[k],b[k]) for a,b in zip(values,changed) for k in range(r+1))
    assert all(all(np.array_equal(a,b) for a,b in zip(v,meridian)) for v in values)
    return {'strands':strands,'word':word,'base':kind,'order':3,
            'normalized_Jacobian_invertible':True,'unique_fixed_jet_is_abelian':True}


def nullvector(matrix,prime):
    work=matrix.copy()%prime
    row=0;pivots=[]
    for col in range(work.shape[1]):
        candidates=[j for j in range(row,len(work)) if work[j,col]]
        if not candidates:
            continue
        j=candidates[0];work[[row,j]]=work[[j,row]]
        work[row]=work[row]*pow(int(work[row,col]),-1,prime)%prime
        for j in range(len(work)):
            if j!=row:
                work[j]=(work[j]-work[j,col]*work[row])%prime
        pivots.append(col);row+=1
    free=next(j for j in range(work.shape[1]) if j not in pivots)
    answer=np.zeros(work.shape[1],dtype=np.int64);answer[free]=1
    for j,col in enumerate(pivots):answer[col]=-work[j,free]%prime
    assert not np.any(matrix@answer%prime)
    return answer


def metabelian_case(strands,word):
    B=burau(strands,word)
    cofactor=normalize_laurent((sp.eye(strands)-B)[1:,1:].det())
    for prime in list(sp.primerange(101,1000)):
        candidates=[s for s in range(2,prime) if s*s%prime!=1 and int(cofactor.subs(t,s*s%prime))%prime==0]
        if candidates:
            s=candidates[0];break
    else:raise AssertionError('no diagnostic split root')
    J=np.array((B-sp.eye(strands)).subs(t,s*s%prime).applyfunc(
        lambda a:int(sp.numer(a))*pow(int(sp.denom(a)),-1,prime)%prime),dtype=np.int64)%prime
    vector=np.concatenate((np.array([0]),nullvector(J[1:,1:],prime)))
    assert not np.any(J@vector%prime)
    matrices=[(s,int(a)*pow(s,-1,prime)%prime,0,pow(s,-1,prime)) for a in vector]
    assert braid_groups(matrices,word,prime)==matrices
    def mult(a,b):return np.array(a).reshape(2,2)@np.array(b).reshape(2,2)%prime
    assert any(np.any((mult(matrices[0],m)-mult(m,matrices[0]))%prime) for m in matrices[1:])
    return {'strands':strands,'word':word,'prime':int(prime),'meridian_eigenvalue':s,
            'Alexander_root':s*s%prime,'exact_nonabelian_reducible_fixed_tuple':True}


def checked_frame(left,right,params_left,params_right,level,prime,q):
    # Pullback of the checked braiding: source order is swapped before r.
    source=(right,left)
    A,B=embed(source,0),embed(source,1)
    Ap,Bp=holonomy(A,B,prime,q)
    target=(embed((left,right),0),embed((left,right),1))
    assert central(Ap,level,prime,q)==central(left,level,prime,q)
    assert central(Bp,level,prime,q)==central(right,level,prime,q)
    size=level*level;I=np.eye(size,dtype=np.int64)
    projector=I.copy()
    for K,x in ((Ap[2],params_left),(Bp[2],params_right)):
        power=I.copy();total=np.zeros_like(I)
        for _ in range(level):
            total=(total+power)%prime
            power=mm(prime,power,K*pow(x,-1,prime)%prime)
        projector=mm(prime,projector,total*pow(level,-1,prime)%prime)
    v=projector[:,0]
    columns=[mm(prime,matrix_power(Ap[1],r,prime),matrix_power(Bp[1],s,prime),v.reshape(-1,1))[:,0]
             for r,s in product(range(level),repeat=2)]
    frame=np.column_stack(columns)
    if not determinant(frame,prime):raise ValueError('outside explicit Hom-frame chart')
    for old,new in zip((Ap,Bp),target):
        assert all(np.array_equal(mm(prime,a,frame),mm(prime,frame,b)) for a,b in zip(old,new))
    swap=[b*level+a for a,b in product(range(level),repeat=2)]
    checked=frame[swap,:]
    for a in tensor_module(left,right,prime):
        assert not np.any((mm(prime,a,checked)-mm(prime,checked,a))%prime)
    return checked


def cut_operator(matrices,frames,word,level,prime):
    count=len(matrices)
    result=np.eye(level**count,dtype=np.int64)
    for j,sign in word:
        local=frames[j] if sign>0 else inverse_mod(frames[j],prime)
        full=np.kron(np.kron(np.eye(level**j,dtype=np.int64),local),
                     np.eye(level**(count-j-2),dtype=np.int64))
        result=mm(prime,result,full)
    return partial_cut(matrices,result,level,prime)


def partial_cut(matrices,result,level,prime):
    count=len(matrices)
    weights=np.array([1],dtype=np.int64)
    for _,_,K in matrices[1:]:
        weights=np.kron(weights,np.diag(matrix_power(inverse_mod(K,prime),level-1,prime)))%prime
    block=level**(count-1)
    cut=np.zeros((level,level),dtype=np.int64)
    for i,j in product(range(level),repeat=2):
        cut[i,j]=sum(int(result[i*block+r,j*block+r])*int(weights[r]) for r in range(block))%prime
    assert np.array_equal(cut,int(cut[0,0])*np.eye(level,dtype=np.int64)%prime)
    return cut


def semicyclic_transport(left,right,x,level,prime,q):
    """A changing-center checked map, with anchor one before normalization."""
    A,B=embed((right,left),0),embed((right,left),1)
    Ap,Bp=holonomy(A,B,prime,q)
    ca,cb=central(Ap,level,prime,q),central(Bp,level,prime,q)
    targets=[regular_module(level,prime,q,x,c[3],c[1],c[2]) for c in (ca,cb)]
    size=level*level;I=np.eye(size,dtype=np.int64)
    projector=I.copy()
    for K in (Ap[2],Bp[2]):
        power=I.copy();total=np.zeros_like(I)
        for _ in range(level):
            total=(total+power)%prime
            power=mm(prime,power,K*pow(x,-1,prime)%prime)
        projector=mm(prime,projector,total*pow(level,-1,prime)%prime)
    v=projector[:,0]
    frame=np.column_stack([mm(prime,matrix_power(Ap[1],r,prime),matrix_power(Bp[1],s,prime),
                              v.reshape(-1,1))[:,0] for r,s in product(range(level),repeat=2)])
    assert determinant(frame,prime)
    for old,new in zip((Ap,Bp),(embed(targets,0),embed(targets,1))):
        assert all(np.array_equal(mm(prime,a,frame),mm(prime,frame,b)) for a,b in zip(old,new))
    swap=[b*level+a for a,b in product(range(level),repeat=2)]
    return frame[swap,:],targets


def semicyclic_period_case(level,action_word):
    strands=1+max(j+1 for j,_ in action_word)
    B=burau(strands,action_word)
    Delta=normalize_laurent((sp.eye(strands)-B)[1:,1:].det())
    chosen=None
    for multiplier in range(6,400):
        prime=4*level*multiplier+1
        if not sp.isprime(prime):continue
        candidates=[M for M in range(2,prime) if int(Delta.subs(t,pow(M,2*level,prime)))%prime==0]
        if candidates:
            chosen=(prime,candidates[0]);break
    assert chosen is not None,(level,action_word)
    prime,M=chosen
    generator=int(sp.primitive_root(prime));q=pow(generator,(prime-1)//(2*level),prime)
    qhalf=pow(generator,(prime-1)//(4*level),prime)
    rho=(q-pow(q,-1,prime))%prime
    s=pow(M,level,prime);delta=pow(-1,level-1,prime)
    x=pow(q,level-1,prime)*M%prime
    omega=(q*x+pow(q*x,-1,prime))%prime
    linear=np.array((B-sp.eye(strands)).subs(t,s*s%prime).applyfunc(
        lambda a:int(sp.numer(a))*pow(int(sp.denom(a)),-1,prime)%prime),dtype=np.int64)%prime
    coefficients=np.concatenate((np.array([0]),nullvector(linear[1:,1:],prime)))
    groups=[(s,int(a)*pow(s,-1,prime)%prime,0,pow(s,-1,prime)) for a in coefficients]
    assert braid_groups(groups,action_word,prime)==groups
    states=from_holonomies([tuple(delta*a%prime for a in g) for g in groups],prime)
    assert all(k==pow(x,level,prime) and f==0 for k,e,f in states)
    epsilons=[e*pow(rho,-level,prime)%prime for _,e,_ in states]
    assert epsilons[0]==0 and any(epsilons)
    # Operators multiply in the reverse of the classical action order.
    operator_word=list(reversed(action_word))
    a=level-1
    scalar=pow(x,a,prime)*pow(qhalf,-a*a,prime)%prime
    theta=pow(qhalf,-a*a,prime)
    periods=[];frames_seen=0
    for scale in (0,1,2,5):
        initial=[regular_module(level,prime,q,x,omega,scale*e%prime,0) for e in epsilons]
        current=list(initial)
        result=np.eye(level**strands,dtype=np.int64)
        for j,sign in operator_word:
            left,right=current[j:j+2]
            if sign>0:
                frame,target=semicyclic_transport(left,right,x,level,prime,q)
                frame=frame*scalar%prime
            else:
                ca,cb=central(left,level,prime,q),central(right,level,prime,q)
                k=pow(x,level,prime)
                ea=(ca[1]*(1-pow(k,-2,prime))+cb[1]*pow(k,-1,prime))%prime
                eb=ca[1]*pow(k,-1,prime)%prime
                target=[regular_module(level,prime,q,x,omega,e,0) for e in (ea,eb)]
                forward,recovered=semicyclic_transport(*target,x,level,prime,q)
                assert all(np.array_equal(a,b) for old,new in zip((left,right),recovered) for a,b in zip(old,new))
                frame=inverse_mod(forward*scalar%prime,prime)
            full=np.kron(np.kron(np.eye(level**j,dtype=np.int64),frame),
                         np.eye(level**(strands-j-2),dtype=np.int64))
            result=mm(prime,result,full)
            current[j:j+2]=target
            frames_seen+=1
        assert all(np.array_equal(a,b) for old,new in zip(initial,current) for a,b in zip(old,new))
        cut=partial_cut(initial,result,level,prime)
        cut=cut*pow(theta,-sum(sign for _,sign in operator_word),prime)%prime
        actual=cut_matrix_dense(level,prime,color_matrices(level,prime,q,x),strands,operator_word)
        assert np.array_equal(cut,actual)
        periods.append(int(cut[0,0]))
    assert len(set(periods))==1
    return {'level':level,'prime':prime,'action_word':action_word,'operator_word':operator_word,
            'squared_central_meridian':s*s%prime,'exact_Alexander_root':True,
            'nonabelian_reducible_semicyclic_family':True,'parameter_values':[0,1,2,5],
            'changing_central_characters_closed_exactly':True,'intertwiner_steps':frames_seen,
            'all_four_cut_matrices_equal_actual_ADO':True,'period_values':periods}


def weight_case(level,seed):
    prime,_,q=field(level)
    rng=Random(932*level+seed)
    for _ in range(100):
        left,pl=sampled_module(level,prime,q,rng)
        right,pr=sampled_module(level,prime,q,rng)
        z=rng.randrange(1,prime)
        D=np.diag([pow(z,-j,prime) for j in range(level)]).astype(np.int64)
        Di=inverse_mod(D,prime)
        changed=[]
        for data,params in ((left,pl),(right,pr)):
            x,omega,e,f=params
            target=regular_module(level,prime,q,x,omega,e*pow(z,level,prime)%prime,
                                  f*pow(z,-level,prime)%prime)
            assert all(np.array_equal(a,mm(prime,Di,b*factor%prime,D))
                       for a,b,factor in zip(target,data,(z,pow(z,-1,prime),1)))
            changed.append(target)
        try:
            original=holonomy(embed((left,right),0),embed((left,right),1),prime,q)
            scaled=holonomy(embed(changed,0),embed(changed,1),prime,q)
        except StopIteration:continue
        DD=np.kron(D,D);DDi=inverse_mod(DD,prime)
        assert all(np.array_equal(a,mm(prime,DDi,b*factor%prime,DD))
                   for target,source in zip(scaled,original)
                   for a,b,factor in zip(target,source,(z,pow(z,-1,prime),1)))
        return {'level':level,'seed':seed,'both_wrap_weights_exact':True,
                'all_six_transformed_generator_weights_exact':True}
    raise AssertionError('no regular graded chart')


def quantum_abelian_case(level,strands):
    prime,generator,q=field(level)
    rho=(q-pow(q,-1,prime))%prime
    roots={pow(a,level,prime):a for a in range(1,prime)}
    rng=Random(6719*level+strands)
    delta=pow(-1,level-1,prime)
    for attempt in range(30000):
        omega=rng.randrange(1,prime)
        trace=-delta*chebyshev(level,omega,prime)%prime
        a,b=rng.randrange(1,prime),rng.randrange(1,prime)
        c=(a*(trace-a)-1)*pow(b,-1,prime)%prime
        group=(a,b,c,(trace-a)%prime)
        if not c:continue
        groups=[tuple(delta*x%prime for x in group)]*strands
        try:
            states=from_holonomies(groups,prime)
            if any(k not in roots or not e or not f for k,e,f in states):continue
            xs=[roots[k] for k,_,_ in states]
            modules=[regular_module(level,prime,q,x,omega,e*pow(rho,-level,prime)%prime,
                                    -f*pow(rho,-level,prime)%prime)
                     for x,(_,e,f) in zip(xs,states)]
            frames=[checked_frame(modules[j],modules[j+1],xs[j],xs[j+1],level,prime,q)
                    for j in range(strands-1)]
        except (ValueError,StopIteration):continue
        break
    else:raise AssertionError(('no cyclic abelian Hom chart',level,strands))
    words=WORDS if strands==3 else ([(0,1)]*3,[(0,-1)]*3)
    scalars=[]
    for word in words:
        assert permutation_is_knot(strands,word)
        scalars.append(int(cut_operator(modules,frames,word,level,prime)[0,0]))
    return {'level':level,'strands':strands,'attempts':attempt+1,
            'both_central_powers_nonzero':True,'all_crossing_intertwinings_exact':True,
            'closed_cut_functionals_scalar':True,'cut_values_in_chosen_frames':scalars}


def actual_restriction_case(level,kind):
    prime,generator,q=field(level)
    x=pow(q,level-1,prime) if kind=='ideal' else generator
    omega=(q*x+pow(q*x,-1,prime))%prime
    V=regular_module(level,prime,q,x,omega,0,0)
    frame=checked_frame(V,V,x,x,level,prime,q)
    # Here the raw projector anchor is one, so this is exactly checked R^0.
    qhalf=pow(generator,(prime-1)//(4*level),prime)
    multiplier=pow(x,level-1,prime)*pow(qhalf,-(level-1)**2,prime)%prime
    frame=frame*multiplier%prime
    theta=pow(qhalf,-(level-1)**2,prime)
    actual=color_matrices(level,prime,q,x)
    for word in WORDS:
        cut=cut_operator([V]*3,[frame]*2,word,level,prime)
        cut=cut*pow(theta,-sum(s for _,s in word),prime)%prime
        assert np.array_equal(cut,cut_matrix_dense(level,prime,actual,3,word))
    return {'level':level,'color':kind,'three_original_cut_periods_recovered_exactly':True}


def main():
    words,symbolic,scope=symbolic_cases()
    print(f'Fox and braid linearizations: {len(symbolic)} passed',flush=True)
    artin=[artin_case(n,w,kind) for n,w in words[:8] for kind in ('identity','unipotent','diagonal')]
    print(f'complete fixed fibers through Artin order three: {len(artin)} passed',flush=True)
    special=[metabelian_case(n,w) for n,w in (words[0],words[3])]
    print(f'exact nonabelian reducible lifts: {len(special)} passed',flush=True)
    quantum=[quantum_abelian_case(n,b) for n in (2,3,4,5,6) for b in (2,3)]
    print(f'generic cyclic closed-braid cut functionals: {len(quantum)} passed',flush=True)
    actual=[actual_restriction_case(n,kind) for n in (2,3,4,5,6) for kind in ('generic','ideal')]
    print(f'original ADO restrictions: {len(actual)} passed',flush=True)
    semicyclic=[semicyclic_period_case(n,w) for n in (2,3,4,5,6,8) for w in (list(WORDS[0]),[(0,1)]*3)]
    print(f'nonabelian reducible period anchors: {len(semicyclic)} passed',flush=True)
    weights=[weight_case(n,seed) for n in (2,3,4,5,6,8,10) for seed in (1,2)]
    print(f'two-sided central weights: {len(weights)} passed',flush=True)
    result={'scope':'Exact closed-braid Hom-line and normal-deformation checks; no geometric period comparison or volume theorem.',
            'Fox_and_braid':symbolic,'Artin_fixed_fibers':artin,'Alexander_divisor_lifts':special,
            'generic_cyclic_cut_functionals':quantum,'actual_ADO_restrictions':actual,
            'nonabelian_reducible_period_anchors':semicyclic,'central_weight_covariance':weights,**scope}
    Path(__file__).with_name('closed_braid_period_line_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS',flush=True)


if __name__=='__main__':main()
