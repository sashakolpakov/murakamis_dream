#!/usr/bin/env python3
"""Exact checks of the actual ADO evaluation on Chebyshev-threaded loops.

Constructs Weyl modules without singular Jones--Wenzl projectors, verifies
their exact sequences, and compares actual root R traces with the derived
one-dimensional virtual colors. No volume estimate is asserted.
"""

from itertools import product
import json
from pathlib import Path

import numpy as np
import sympy as sp

from audit_finite_sum_annihilator import field
from audit_actual_peripheral_fusion import (fundamental, module, tensor_module,
                                            inverse_mod, matrix_power)
from audit_cyclic_steinberg_lattice import rank


def integer(n, prime, q):
    return (pow(q,n,prime)-pow(q,-n,prime))*pow((q-pow(q,-1,prime))%prime,-1,prime)%prime


def weyl(m, prime, q):
    E = np.zeros((m+1,m+1),dtype=np.int64)
    F = np.zeros_like(E)
    for j in range(1,m+1):
        E[j-1,j] = integer(m-j+1,prime,q)
        F[j,j-1] = integer(j,prime,q)
    K = np.diag([pow(q,m-2*j,prime) for j in range(m+1)]).astype(np.int64)
    target = np.diag([integer(m-2*j,prime,q) for j in range(m+1)])
    assert np.array_equal((E@F-F@E)%prime,target)
    assert not np.any((K@E-q*q*E@K)%prime)
    assert not np.any((K@F-pow(q,-2,prime)*F@K)%prime)
    return E,F,K


def weyl_sequence_case(level,m):
    prime,_,q = field(level)
    W, D = fundamental(prime,q), weyl(m,prime,q)
    U = tensor_module(W,D,prime)
    injection = np.zeros((2*(m+1),m+2),dtype=np.int64)
    projection = np.zeros((m,2*(m+1)),dtype=np.int64)
    for j in range(m+2):
        if j<=m:
            injection[j,j] = pow(q,-j,prime)
        if j>=1:
            injection[m+j,j] = 1
    for j in range(m+1):
        if j>=1:
            projection[j-1,j] = 1
        if j<m:
            projection[j,m+1+j] = -pow(q,-j-1,prime)%prime
    plus,minus = weyl(m+1,prime,q),weyl(m-1,prime,q)
    for data in (D,plus,minus):
        assert not np.any(matrix_power(data[0],level,prime))
        assert not np.any(matrix_power(data[1],level,prime))
    assert rank(injection,prime)==m+2
    assert rank(projection,prime)==m
    assert not np.any(projection@injection%prime)
    for a,b,c in zip(U,plus,minus):
        assert np.array_equal(a@injection%prime,injection@b%prime)
        assert np.array_equal(projection@a%prime,c@projection%prime)
    return {'level':level,'weyl_highest_weight':m,
            'tensor_fundamental_Weyl_sequence_exact':True}


def root_sequence_case(level):
    prime,generator,q = field(level)
    D,sub = weyl(level,prime,q),weyl(level-2,prime,q)
    injection = np.zeros((level+1,level-1),dtype=np.int64)
    for j in range(level-1):
        injection[j+1,j] = integer(j+1,prime,q)
    projection = np.zeros((2,level+1),dtype=np.int64)
    projection[0,0],projection[1,level] = 1,1
    quotient = (np.zeros((2,2),dtype=np.int64),np.zeros((2,2),dtype=np.int64),
                -np.eye(2,dtype=np.int64)%prime)
    assert rank(injection,prime)==level-1
    assert rank(projection,prime)==2
    for a,b,c in zip(D,sub,quotient):
        assert np.array_equal(a@injection%prime,injection@b%prime)
        assert np.array_equal(projection@a%prime,c@projection%prime)
    qhalf = pow(generator,(prime-1)//(4*level),prime)
    fourth_root = pow(qhalf,level,prime)
    delta = pow(-1,level-1,prime)
    for h in (level,-level,2*level,-2*level):
        pivotal = pow(q,(1-level)*h,prime)
        twist = pow(qhalf,h*h+2*(1-level)*h,prime)
        if abs(h)==level:
            assert pivotal==delta and twist==delta*pow(fourth_root,level,prime)%prime
        else:
            assert pivotal==twist==1
    return {'level':level,'Weyl_N_subquotient_sequence_exact':True,
            'one_dimensional_pivots_and_twists_exact':True}


def nilpotent_series(level,prime,q,A,B):
    rho = (q-pow(q,-1,prime))%prime
    size = len(A)*len(B)
    power = np.eye(size,dtype=np.int64)
    result = np.zeros_like(power)
    factorial = 1
    nilpotent = np.kron(A,B)%prime
    for k in range(level):
        if k:
            factorial = factorial*integer(k,prime,q)%prime
        coefficient = pow(q,k*(k-1)//2,prime)*pow(rho,k,prime)*pow(factorial,-1,prime)%prime
        result = (result+coefficient*power)%prime
        power = power@nilpotent%prime
    assert not np.any(power)
    return result


def linked_loop_operator(level,m,prime,q,core,root_x,heights,linking):
    D = weyl(m,prime,q)
    dimension,aux = len(core[0]),m+1
    diagonal = np.diag([pow(root_x,m-2*j,prime)*pow(q,-a*(m-2*j),prime)%prime
                        for a,j in product(heights,range(aux))])
    R = diagonal@nilpotent_series(level,prime,q,core[0],D[1])%prime
    R21 = diagonal@nilpotent_series(level,prime,q,core[1],D[0])%prime
    double = matrix_power(R21@R%prime,linking,prime)
    pivotal = [pow(int(D[2][j,j]),1-level,prime) for j in range(aux)]
    result = np.zeros((dimension,dimension),dtype=np.int64)
    for j in range(aux):
        result = (result+pivotal[j]*double[j::aux,j::aux])%prime
    return result


def linked_thread_case(level,kind,degree,linking,framing):
    prime,generator,q = field(level)
    qhalf = pow(generator,(prime-1)//(4*level),prime)
    root_x = generator
    x = root_x*root_x%prime
    core = module(level,prime,q,x)
    heights = list(range(level))
    if kind=='core_and_fundamental':
        core = tensor_module(fundamental(prime,q),core,prime)
        heights = [b+j for b,j in product(range(2),range(level))]
        root_x = root_x*qhalf%prime
    terms = []
    for m in (degree,degree-2):
        value = linked_loop_operator(level,m,prime,q,core,root_x,heights,linking)
        twist = pow(qhalf,m*m+2*(1-level)*m,prime)
        terms.append(value*pow(twist,framing,prime)%prime)
    actual = (terms[0]-terms[1])%prime
    original_x = x
    expected = (pow(original_x,degree*linking,prime)+pow(original_x,-degree*linking,prime))%prime
    if degree==level:
        expected = expected*pow(-1,level-1,prime)%prime
        twist = pow(-1,level-1,prime)*pow(qhalf,level*level,prime)%prime
        expected = expected*pow(twist,framing,prime)%prime
        if kind=='core_and_fundamental':
            expected = expected*pow(-1,linking,prime)%prime
    assert np.array_equal(actual,expected*np.eye(len(core[0]),dtype=np.int64)%prime)
    return {'level':level,'core':kind,'thread_degree':degree,'linking_number':linking,'framing':framing,
            'actual_heterogeneous_R_trace_matches_virtual_colors':True}


def zero_framed_aux_knot(level,m,prime,q,exponent):
    D = weyl(m,prime,q)
    dimension = m+1
    qhalf = pow(int(sp.primitive_root(prime)),(prime-1)//(4*level),prime)
    diagonal = np.diag([pow(qhalf,(m-2*a)*(m-2*b),prime)
                        for a,b in product(range(dimension),repeat=2)])
    R = diagonal@nilpotent_series(level,prime,q,D[0],D[1])%prime
    swap = [b*dimension+a for a,b in product(range(dimension),repeat=2)]
    crossing = R[swap,:]
    pivotal = np.array([pow(int(D[2][j,j]),1-level,prime) for j in range(dimension)],dtype=np.int64)
    twist = pow(qhalf,m*m+2*(1-level)*m,prime)
    curl = np.einsum('abcb,b->ac',crossing.reshape((dimension,)*4),pivotal)%prime
    assert np.array_equal(curl,twist*np.eye(dimension,dtype=np.int64)%prime)
    braid = matrix_power(crossing,exponent,prime)
    value = sum(int(braid[j,j])*int(w) for j,w in enumerate(np.kron(pivotal,pivotal)))%prime
    return value*pow(twist,-exponent,prime)%prime


def knotted_thread_case(level,degree,exponent):
    prime,_,q = field(level)
    actual = (zero_framed_aux_knot(level,degree,prime,q,exponent)
              -zero_framed_aux_knot(level,degree-2,prime,q,exponent))%prime
    expected = 2*pow(-1,level-1,prime)%prime if degree==level else 2
    assert actual==expected
    return {'level':level,'thread_degree':degree,'two_strand_knot_writhe':exponent,
            'actual_knotted_auxiliary_trace_exact':True}


def commutator_witness():
    a,s = sp.symbols('a s')
    P = sp.Matrix([[1,a],[0,1]])
    Q = sp.Matrix([[1,0],[s,1]])
    trace = sp.expand(sp.trace(P*Q*P.inv()*Q.inv()))
    assert trace==2+a*a*s*s
    defects = [sp.factor((trace**2-4).subs(a,k)) for k in (1,2)]
    assert sp.monic(sp.gcd(*defects),s)==s*s
    return {'commutator_trace':str(trace),'two_squared_trace_defects':[str(v) for v in defects],
            'only_common_zero_is_degenerate_parabolic_parameter':True}


def separating_observable_projector():
    g,a,c,sc = sp.symbols('g a c sc')
    source = (sc-a*c)/(2-g)
    A = sp.Matrix([[a,source],[0,1]])
    X = sp.Matrix([[g,c],[0,2]])
    sigmaX = sp.Matrix([[g,sc],[0,2]])
    assert sp.simplify(sigmaX*A-A*X)==sp.zeros(2)
    P = (X-g*sp.eye(2))/(2-g)
    assert sp.simplify(P*P-P)==sp.zeros(2)
    selected = sp.Matrix([c/(2-g),1])
    assert sp.simplify(X*selected-2*selected)==sp.zeros(2,1)
    assert sp.simplify(A*selected-sp.Matrix([sc/(2-g),1]))==sp.zeros(2,1)
    return {'central_spectral_projector_exact':True,
            'unique_source_eigenvector_is_horizontal':True,
            'selected_period':'c/(2-g)'}


def main():
    levels = (2,3,4,5,6,7,8,10,12,15,18)
    sequences = [weyl_sequence_case(n,m) for n in levels
                 for m in sorted({1,max(1,n-2),n-1,n,2*n-1})]
    roots = [root_sequence_case(n) for n in levels]
    print(f'exact Weyl sequences: {len(sequences)}; root subquotients: {len(roots)} passed',flush=True)
    links = [linked_thread_case(n,kind,degree,lk,fr)
             for n in (2,3,4,5) for kind in ('core','core_and_fundamental')
             for degree in (n,2*n) for lk in (-1,0,1,2) for fr in (-1,0,1)]
    print(f'actual heterogeneous threaded-loop traces: {len(links)} passed',flush=True)
    knots = [knotted_thread_case(n,degree,w) for n in (2,3,4,5)
             for degree in (n,2*n) for w in (3,-5)]
    print(f'actual knotted auxiliary threads: {len(knots)} passed',flush=True)
    result = {'scope':'Exact actual-ADO threading diagnostics; no geometric period identification or volume assertion.',
              'Weyl_sequences':sequences,'root_subquotients':roots,
              'actual_linked_threads':links,'actual_knotted_threads':knots,
              'hyperbolic_character_witness':commutator_witness(),
              'separating_observable_projector':separating_observable_projector()}
    Path(__file__).with_name('ado_threaded_shadow_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS',flush=True)


if __name__=='__main__':
    main()
