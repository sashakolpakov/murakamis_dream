#!/usr/bin/env python3
"""Exact checks of the rational holonomy automorphism and its actual wall.

The unrestricted root modules, algebra automorphism, matrix-unit
intertwiners, and regular deformation are constructed independently of
any published holonomy R formula. No knot period comparison or volume
asymptotic is inferred.
"""

from itertools import product
import json
from pathlib import Path
from random import Random

import numpy as np
import sympy as sp

from audit_finite_sum_annihilator import field
from audit_actual_peripheral_fusion import inverse_mod, matrix_power, raw_mixed_R, module
from audit_cyclic_steinberg_lattice import determinant, rank
from audit_kashaev_ado_pointing import color_matrices, WORDS
from audit_actual_weyl_descent import period_by_paths


def mm(prime,*matrices):
    result = matrices[0]%prime
    for matrix in matrices[1:]:
        result = result@matrix%prime
    return result


def chebyshev(n,z,prime):
    a,b = 2,z%prime
    if n==0:
        return a
    for _ in range(1,n):
        a,b = b,(z*b-a)%prime
    return b


def scalar(matrix,prime):
    value = int(matrix[0,0])%prime
    assert np.array_equal(matrix%prime,value*np.eye(len(matrix),dtype=np.int64)%prime)
    return value


def central(data,level,prime,q):
    E,F,K = data
    rho = (q-pow(q,-1,prime))%prime
    k,e,f = (scalar(matrix_power(matrix,level,prime),prime) for matrix in (K,E,F))
    omega = scalar((rho*rho*mm(prime,F,E)+q*K+pow(q,-1,prime)*inverse_mod(K,prime))%prime,prime)
    assert chebyshev(level,omega,prime)==(pow(rho,2*level,prime)*e*f-k-pow(k,-1,prime))%prime
    return k,e,f,omega


def regular_module(level,prime,q,x,omega,epsilon,phi):
    rho = (q-pow(q,-1,prime))%prime
    Q = q*q%prime
    E = np.zeros((level,level),dtype=np.int64)
    F = np.zeros_like(E)
    K = np.diag([x*pow(Q,-j,prime)%prime for j in range(level)]).astype(np.int64)
    rest = 1
    for j in range(1,level):
        value = (omega-q*int(K[j,j])-pow(q,-1,prime)*pow(int(K[j,j]),-1,prime))*pow(rho,-2,prime)%prime
        if not value:
            raise ValueError('outside the selected regular matrix-unit chart')
        E[j-1,j] = value
        F[j,j-1] = 1
        rest = rest*value%prime
    E[level-1,0] = epsilon*pow(rest,-1,prime)%prime
    F[0,level-1] = phi%prime
    assert central((E,F,K),level,prime,q)==(pow(x,level,prime),epsilon%prime,phi%prime,omega%prime)
    return E,F,K


def sampled_module(level,prime,q,randomizer):
    rho = (q-pow(q,-1,prime))%prime
    while True:
        x,omega,phi = [randomizer.randrange(1,prime) for _ in range(3)]
        k = pow(x,level,prime)
        epsilon = (chebyshev(level,omega,prime)+k+pow(k,-1,prime))*pow(pow(rho,2*level,prime)*phi%prime,-1,prime)%prime
        try:
            data = regular_module(level,prime,q,x,omega,epsilon,phi)
        except ValueError:
            continue
        if epsilon:
            return data,(x,omega,epsilon,phi)


def embed(factors,position):
    result = []
    for matrix in factors[position]:
        full = np.array([[1]],dtype=np.int64)
        for j,data in enumerate(factors):
            full = np.kron(full,matrix if j==position else np.eye(len(data[0]),dtype=np.int64))
        result.append(full)
    return tuple(result)


def holonomy(left,right,prime,q):
    E,F,K = left
    e,f,k = right
    size = len(E)
    I = np.eye(size,dtype=np.int64)
    rho = (q-pow(q,-1,prime))%prime
    Q = q*q%prime
    Ki,ki = inverse_mod(K,prime),inverse_mod(k,prime)
    u = (q*rho*rho%prime)*mm(prime,E,Ki,k,f)%prime
    H = inverse_mod((I-u)%prime,prime)
    G = inverse_mod((I-pow(Q,-1,prime)*u)%prime,prime)
    transformed_left = (mm(prime,E,k),
        (f+mm(prime,F,ki)-mm(prime,G,Ki,Ki,f))%prime,
        mm(prime,K,(I-pow(Q,-1,prime)*u)%prime))
    transformed_right = ((mm(prime,K,e)+E-mm(prime,E,k,k,H))%prime,
        mm(prime,Ki,f),mm(prime,k,H))
    return transformed_left,transformed_right


def inverse_holonomy(left,right,prime,q):
    E1,F1,K1 = left
    E2,F2,K2 = right
    I = np.eye(len(E1),dtype=np.int64)
    rho = (q-pow(q,-1,prime))%prime
    Q = q*q%prime
    u = (q*rho*rho%prime)*mm(prime,E1,F2)%prime
    H = inverse_mod((I-u)%prime,prime)
    G = inverse_mod((I-pow(Q,-1,prime)*u)%prime,prime)
    K = mm(prime,K1,G)
    k = mm(prime,K2,(I-u)%prime)
    Ki,ki = inverse_mod(K,prime),inverse_mod(k,prime)
    E = mm(prime,E1,ki)
    f = mm(prime,K,F2)
    e = mm(prime,Ki,(E2-E+mm(prime,E,k,k,H))%prime)
    F = mm(prime,(F1-f+mm(prime,G,Ki,Ki,f))%prime,k)
    return (E,F,K),(e,f,k)


def check_relations(left,right,prime,q):
    rho = (q-pow(q,-1,prime))%prime
    Q = q*q%prime
    for E,F,K in (left,right):
        Ki = inverse_mod(K,prime)
        assert not np.any((E@F-F@E-(K-Ki)*pow(rho,-1,prime))%prime)
        assert not np.any((K@E-Q*E@K)%prime)
        assert not np.any((K@F-pow(Q,-1,prime)*F@K)%prime)
    assert all(not np.any((a@b-b@a)%prime) for a in left for b in right)


def transformed_centres(a,b,level,prime,q):
    k,e,f,omega = a
    l,g,h,omega2 = b
    rho = (q-pow(q,-1,prime))%prime
    D = (1+pow(rho,2*level,prime)*e*h*l*pow(k,-1,prime))%prime
    if not D:
        raise ValueError('central divisor D=0')
    Di = pow(D,-1,prime)
    return ((k*D%prime,e*l%prime,(h+f*pow(l,-1,prime)-h*pow(k,-2,prime)*Di)%prime,omega),
            (l*Di%prime,(k*g+e-e*l*l*Di)%prime,h*pow(k,-1,prime)%prime,omega2),D)


def automorphism_case(level,seed):
    prime,_,q = field(level)
    randomizer = Random(4100*level+seed)
    for attempt in range(100):
        a,_ = sampled_module(level,prime,q,randomizer)
        b,_ = sampled_module(level,prime,q,randomizer)
        A,B = embed((a,b),0),embed((a,b),1)
        ca,cb = central(a,level,prime,q),central(b,level,prime,q)
        try:
            ea,eb,D = transformed_centres(ca,cb,level,prime,q)
            Ap,Bp = holonomy(A,B,prime,q)
        except (ValueError,StopIteration):
            continue
        check_relations(Ap,Bp,prime,q)
        assert central(Ap,level,prime,q)==ea
        assert central(Bp,level,prime,q)==eb
        recovered = inverse_holonomy(Ap,Bp,prime,q)
        assert all(np.array_equal(x,y) for x,y in zip(A+B,recovered[0]+recovered[1]))
        E,F,K = A;e,f,k = B
        Ep,Fp,Kp = Ap;ep,fp,kp = Bp
        assert not np.any((mm(prime,Ep,kp)+ep-mm(prime,K,e)-E)%prime)
        assert not np.any((Fp+mm(prime,inverse_mod(Kp,prime),fp)-f-mm(prime,F,inverse_mod(k,prime)))%prime)
        return {'level':level,'seed':seed,'generic_cyclic_relations_and_cross_commutators_exact':True,
                'rational_inverse_exact':True,'root_central_map_and_Casimir_exact':True,
                'coproduct_intertwining_exact':True,'retained_central_factor_D':D}
    raise AssertionError('no regular sampled chart')


def braid_case(level,seed):
    prime,_,q = field(level)
    randomizer = Random(9100*level+seed)
    for attempt in range(100):
        factors = [sampled_module(level,prime,q,randomizer)[0] for _ in range(3)]
        original = [embed(factors,j) for j in range(3)]
        answers = []
        try:
            for word in (((0,1),(0,2),(1,2)),((1,2),(0,2),(0,1))):
                data = list(original)
                for a,b in word:
                    data[a],data[b] = holonomy(data[a],data[b],prime,q)
                answers.append(data)
        except StopIteration:
            continue
        assert all(np.array_equal(x,y) for a,b in zip(*answers) for x,y in zip(a,b))
        return {'level':level,'seed':seed,'quantum_automorphism_Yang_Baxter_exact':True}
    raise AssertionError('no regular triple chart')


def intertwiner_case(level):
    prime,generator,q = field(level)
    randomizer = Random(1100*level)
    roots = {pow(value,level,prime):value for value in range(1,prime)}
    qhalf = pow(generator,(prime-1)//(4*level),prime)
    anchor = pow(qhalf,(level-1)**2,prime)
    for attempt in range(1000):
        a,pa = sampled_module(level,prime,q,randomizer)
        b,pb = sampled_module(level,prime,q,randomizer)
        ca,cb = central(a,level,prime,q),central(b,level,prime,q)
        try:
            ea,eb,D = transformed_centres(ca,cb,level,prime,q)
        except ValueError:
            continue
        if D not in roots:
            continue
        droot = roots[D]
        xa,xb = pa[0]*droot%prime,pb[0]*pow(droot,-1,prime)%prime
        try:
            ta = regular_module(level,prime,q,xa,ea[3],ea[1],ea[2])
            tb = regular_module(level,prime,q,xb,eb[3],eb[1],eb[2])
        except ValueError:
            continue
        A,B = embed((a,b),0),embed((a,b),1)
        Ap,Bp = holonomy(A,B,prime,q)
        size = level*level
        I = np.eye(size,dtype=np.int64)
        projectors = []
        for K,x in ((Ap[2],xa),(Bp[2],xb)):
            power = I.copy();projector = np.zeros_like(I)
            normalized = K*pow(x,-1,prime)%prime
            for _ in range(level):
                projector = (projector+power)%prime
                power = mm(prime,power,normalized)
            projectors.append(projector*pow(level,-1,prime)%prime)
        P = mm(prime,*projectors)
        assert rank(P,prime)==1
        v = anchor*P[:,0]%prime
        if not np.any(v):
            continue
        columns = []
        for r,s in product(range(level),repeat=2):
            columns.append(mm(prime,matrix_power(Ap[1],r,prime),
                               matrix_power(Bp[1],s,prime),v.reshape(-1,1))[:,0])
        intertwiner = np.column_stack(columns)
        assert determinant(intertwiner,prime)!=0
        targets = (embed((ta,tb),0),embed((ta,tb),1))
        for old,new in zip((Ap,Bp),targets):
            assert all(np.array_equal(mm(prime,x,intertwiner),mm(prime,intertwiner,y))
                       for x,y in zip(old,new))
        return {'level':level,'attempts':attempt+1,'matrix_unit_intertwiner_constructed':True,
                'all_six_generator_intertwinings_exact':True,
                'no_roots_of_E_or_F_central_parameters_used':True}
    raise AssertionError('no regular splitting chart found')


def actual_wall_case(level,kind):
    prime,generator,q = field(level)
    x = pow(q,level-1,prime) if kind=='ideal' else generator
    a = module(level,prime,q,x)
    A,B = embed((a,a),0),embed((a,a),1)
    Ap,Bp = holonomy(A,B,prime,q)
    R = raw_mixed_R(level,prime,q,a,x,list(range(level)),a,x,list(range(level)))
    Ri = inverse_mod(R,prime)
    assert all(np.array_equal(mm(prime,R,old,Ri),new)
               for old,new in zip(A+B,Ap+Bp))
    qhalf = pow(generator,(prime-1)//(4*level),prime)
    multiplier = pow(x,level-1,prime)*pow(qhalf,-(level-1)**2,prime)%prime
    Rbar = multiplier*R%prime
    assert determinant(Rbar,prime)==1
    size = level*level
    I = np.eye(size,dtype=np.int64)
    P = I.copy()
    for K in (Ap[2],Bp[2]):
        normalized = K*pow(x,-1,prime)%prime
        term = I.copy();projection = np.zeros_like(I)
        for _ in range(level):
            projection = (projection+term)%prime
            term = mm(prime,term,normalized)
        P = mm(prime,P,projection*pow(level,-1,prime)%prime)
    anchor = pow(qhalf,(level-1)**2,prime)
    v = anchor*P[:,0]%prime
    columns = [mm(prime,matrix_power(Ap[1],r,prime),matrix_power(Bp[1],s,prime),
                  v.reshape(-1,1))[:,0] for r,s in product(range(level),repeat=2)]
    anchored_intertwiner = np.column_stack(columns)
    assert np.array_equal(anchored_intertwiner,anchor*R%prime)
    determinant_root = pow(q,(level-1)**2,prime)*pow(x,1-level,prime)%prime
    assert pow(determinant_root,size,prime)==determinant(anchored_intertwiner,prime)
    assert np.array_equal(anchored_intertwiner*pow(determinant_root,-1,prime)%prime,Rbar)
    if kind=='ideal':
        full = pow(qhalf,(level-1)**2,prime)*R%prime
        assert np.array_equal(full,Rbar)
    comparisons = 0
    if level<=6:
        actual = color_matrices(level,prime,q,x)
        normalized = (actual[0]*multiplier%prime,
                      actual[1]*pow(multiplier,-1,prime)%prime,
                      actual[2],pow(qhalf,-(level-1)**2,prime))
        for word in WORDS:
            assert period_by_paths(level,prime,actual,3,word)==period_by_paths(level,prime,normalized,3,word)
            comparisons+=1
    return {'level':level,'color':kind,'conjugation_equals_actual_R_exact':True,
            'determinant_one_frame_exact':True,'matrix_unit_frame_has_exact_actual_wall_value':True,
            'actual_zero_framed_cut_comparisons':comparisons}


def series_multiply(a,b,prime):
    return [sum(a[j]*b[n-j] for j in range(n+1))%prime for n in range(len(a))]


def series_inverse(a,prime):
    result = [pow(a[0],-1,prime)]
    for n in range(1,len(a)):
        result.append(-result[0]*sum(a[j]*result[n-j] for j in range(1,n+1))%prime)
    return result


def series_power(a,n,prime):
    if n<0:
        return series_power(series_inverse(a,prime),-n,prime)
    result = [1]+[0]*(len(a)-1)
    while n:
        if n%2:
            result = series_multiply(result,a,prime)
        a = series_multiply(a,a,prime)
        n//=2
    return result


def chebyshev_series(n,a,prime):
    previous = [2]+[0]*(len(a)-1)
    if not n:
        return previous
    current = a
    for _ in range(1,n):
        previous,current = current,[(x-y)%prime for x,y in zip(series_multiply(a,current,prime),previous)]
    return current


def matrix_series_multiply(a,b,prime):
    return [sum(mm(prime,a[j],b[n-j]) for j in range(n+1))%prime for n in range(len(a))]


def matrix_series_power(a,n,prime):
    result = [np.eye(len(a[0]),dtype=np.int64)]+[np.zeros_like(a[0]) for _ in range(len(a)-1)]
    for _ in range(n):
        result = matrix_series_multiply(result,a,prime)
    return result


def regular_deformation_case(level):
    prime,_,q = field(level)
    Q = q*q%prime
    rho = (q-pow(q,-1,prime))%prime
    order = 3
    x0 = pow(q,level-1,prime)
    x = [x0,2*x0%prime,0,0]
    xi = series_inverse(x,prime)
    epsilon,phi = [0,3,0,0],[0,5,0,0]
    target = [(pow(rho,2*level,prime)*a-b-c)%prime for a,b,c in zip(
        series_multiply(epsilon,phi,prime),series_power(x,level,prime),series_power(x,-level,prime))]
    omega = [-2%prime,0,0,0]
    derivative = pow(-1,level-1,prime)*level*level%prime
    for k in range(1,order+1):
        value = chebyshev_series(level,omega,prime)
        omega[k] = (target[k]-value[k])*pow(derivative,-1,prime)%prime
    assert chebyshev_series(level,omega,prime)==target
    rest = [1,0,0,0]
    entries = {}
    for a in range(1,level):
        entries[a] = [(w-q*pow(Q,-a,prime)*b-pow(q,-1,prime)*pow(Q,a,prime)*c)
                       *pow(rho,-2,prime)%prime for w,b,c in zip(omega,x,xi)]
        assert entries[a][0]!=0
        rest = series_multiply(rest,entries[a],prime)
    entries[0] = series_multiply(epsilon,series_inverse(rest,prime),prime)
    E = [np.zeros((level,level),dtype=np.int64) for _ in range(order+1)]
    F = [np.zeros_like(E[0]) for _ in range(order+1)]
    K = [np.zeros_like(E[0]) for _ in range(order+1)]
    Ki = [np.zeros_like(E[0]) for _ in range(order+1)]
    for k in range(order+1):
        for a in range(1,level):
            E[k][a-1,a] = entries[a][k]
            if not k:
                F[k][a,a-1] = 1
        E[k][level-1,0] = entries[0][k]
        F[k][0,level-1] = phi[k]
        K[k] = np.diag([x[k]*pow(Q,-a,prime)%prime for a in range(level)])
        Ki[k] = np.diag([xi[k]*pow(Q,a,prime)%prime for a in range(level)])
    for k,(ef,fe) in enumerate(zip(matrix_series_multiply(E,F,prime),matrix_series_multiply(F,E,prime))):
        assert not np.any((ef-fe-(K[k]-Ki[k])*pow(rho,-1,prime))%prime)
    for left,right,constant in ((K,E,Q),(K,F,pow(Q,-1,prime))):
        assert all(not np.any((a-constant*b)%prime) for a,b in zip(
            matrix_series_multiply(left,right,prime),matrix_series_multiply(right,left,prime)))
    for data,expected in ((E,epsilon),(F,phi)):
        assert all(np.array_equal(a,b*np.eye(level,dtype=np.int64)%prime)
                   for a,b in zip(matrix_series_power(data,level,prime),expected))
    base = module(level,prime,q,x0)
    assert all(np.array_equal(a[0],b) for a,b in zip((E,F,K),base))
    return {'level':level,'order':order,'regular_three_parameter_module_jet_exact':True,
            'central_E_and_F_powers_exact':True,'base_is_actual_Steinberg_color':True,
            'Casimir_Hensel_derivative_unit':int(derivative)}


def symbolic_centre_check():
    k,l,e,f,g,h = sp.symbols('k l e f g h',nonzero=True)
    def uncheck(a,b):
        k,e,f=a;l,g,h=b;D=1-e*h*l/k
        return ((k*D,e*l,h+f/l-h/(k*k*D)),
                (l/D,k*g+e-e*l*l/D,h/k))
    checked = uncheck((l,g,h),(k,e,f))
    c = 1-k*g*f/l
    expected = ((l*c,k*g,f+h/k-f/(l*l*c)),
                (k/c,l*e+g-k*k*g/c,f/l))
    assert all(sp.cancel(x-y)==0 for x,y in zip(checked[0]+checked[1],expected[0]+expected[1]))
    casimir = lambda x:x[0]+1/x[0]+x[1]*x[2]
    output = uncheck((k,e,f),(l,g,h))
    assert sp.cancel(casimir(output[0])-casimir((k,e,f)))==0
    assert sp.cancel(casimir(output[1])-casimir((l,g,h)))==0
    return {'balanced_centre_Casimir_exact':True,
            'checked_centre_map_equals_previous_inverse_holonomy_map':True,
            'sign_conversion':'e=rho^N E^N; f=-rho^N F^N'}


def main():
    automorphisms = [automorphism_case(n,seed) for n in (2,3,4,5,6,8,10) for seed in (1,2)]
    print(f'generic root algebra automorphisms: {len(automorphisms)} passed',flush=True)
    braids = [braid_case(n,seed) for n in (2,3,4) for seed in (1,2)]
    print(f'quantum three-factor Yang--Baxter maps: {len(braids)} passed',flush=True)
    intertwiners = [intertwiner_case(n) for n in (2,3,4,5,6,8)]
    print(f'actual matrix-unit holonomy intertwiners: {len(intertwiners)} passed',flush=True)
    walls = [actual_wall_case(n,kind) for n in (2,3,4,5,6,8,10)
             for kind in ('generic','ideal')]
    print(f'actual ADO wall and determinant frames: {len(walls)} passed',flush=True)
    deformations = [regular_deformation_case(n) for n in (2,3,4,5,6,8,10,12,15)]
    print(f'regular Steinberg deformations through order three: {len(deformations)} passed',flush=True)
    result = {'scope':'Exact local holonomy-braiding diagnostics; no global period or volume theorem.',
              'root_automorphisms':automorphisms,'quantum_Yang_Baxter':braids,
              'regular_matrix_unit_intertwiners':intertwiners,'actual_ADO_wall':walls,
              'regular_deformation_jets':deformations,
              'symbolic_centre':symbolic_centre_check()}
    Path(__file__).with_name('regular_holonomy_braiding_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS',flush=True)


if __name__=='__main__':
    main()
