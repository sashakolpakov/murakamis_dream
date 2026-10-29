#!/usr/bin/env python3
"""Exact checks for the boundary delta module and the normal period.

An independently derived telescoping operator supplies a calibration.
Its finite cyclotomic block is compared with actual cut polynomials at
the levels stated in the output; no all-level state comparison or
volume theorem is inferred from those tests.
"""

import json
from pathlib import Path

import numpy as np
import sympy as sp

from audit_finite_sum_annihilator import field
from audit_cyclic_steinberg_lattice import rank
from audit_regularized_kashaev_period import (actual_laurent_period,
                                             multiply_poly, add_poly, evaluate)


Q, Y, Z = sp.symbols("Q Y Z")


def operator_calibration():
    D = Y*(Y+1)*(Q-Y**2)*(Q*Y**2-1)
    middle = Q**2*Y**2-Q*Y**4+Q*Y**3+Q*Y-Q+Y**2
    c = {-1: Y**2*(Q-Y)*(Q*Y**2-1),
         0: -(Y-1)**2*(Y+1)*middle,
         1: Y**2*(Q*Y-1)*(Q-Y**2)}
    denominator = (Y-Z)*(1-Y*Z)
    certificate = (Y-1)**2*Z/denominator
    ratio_up = (Y-1)*(1-Q*Y*Z)/((Y-Z)*(1-Q*Y))
    ratio_down = (Y-Q*Z)*(1-Y)/((Y-Q)*(1-Y*Z))
    ratio_k = Y+1/Y-Q*Z-1/(Q*Z)
    lhs = c[-1]*ratio_down+c[0]+c[1]*ratio_up
    rhs = D*(certificate.subs(Z,Q*Z)*ratio_k-certificate)
    assert sp.cancel(lhs-rhs) == 0
    # C(1)=-1: the finite boundary is -D*(t_N-1)=D*Delta(U).
    raw = {j: sp.Integer(0) for j in range(-1, 3)}
    for j, value in c.items():
        raw[j+1] += D*value.subs(Y,Q*Y)
        raw[j] -= D.subs(Y,Q*Y)*value
    raw = {j+1: sp.expand(value.subs(Y,Q*Y)) for j,value in raw.items()}
    common = sp.gcd_list(list(raw.values()))
    P = {j: sp.factor(value/common) for j,value in raw.items()}
    B = {j: sp.cancel(value/(Q**j*Y-1)) for j,value in P.items()}
    assert all(sp.denom(value) == 1 for value in B.values())
    reciprocity = -Q**12*Y**8
    for j,value in B.items():
        assert sp.cancel(-Q**j*Y*value-reciprocity*B[3-j].subs(Y,Q**-3/Y)) == 0
    assert sp.cancel(reciprocity*reciprocity.subs(Y,Q**-3/Y)-1) == 0
    assert sp.cancel(reciprocity*reciprocity.subs({Q:Q**-1,Y:Y**-1},simultaneous=True)-1) == 0
    for j,value in P.items():
        assert sp.simplify(value.subs(Y,Q**(-j))) == 0
    low = min(min(monom[0] for monom in sp.Poly(value,Y).monoms()) for value in P.values())
    z = sp.symbols("z")
    initial = sp.factor(sum(sp.expand(value).coeff(Y,low)*z**j for j,value in P.items()))
    assert sp.expand(initial-z*(Q-z)) == 0
    classical = sp.factor(sum(value.subs(Q,1)*z**j for j,value in P.items()))
    return P,B,{"telescoping_certificate_exact": True,
                "boundary_column_factors_exact": True,
                "initial_polynomial": str(initial),
                "Weyl_reciprocity_factor": str(reciprocity),
                "Weyl_involutions_and_unit_circle_norm_exact": True,
                "classical_symbol": str(classical),
                "removed_common_factor": str(sp.factor(common))}


def coefficient_terms(operator):
    return {j: [(int(c),eY,eQ) for (eY,eQ),c in sp.Poly(value,Y,Q).terms()]
            for j,value in operator.items()}


def matrix_and_derivative(terms, level, prime, omega):
    A = np.zeros((level,level),dtype=np.int64)
    A1 = np.zeros_like(A)
    inv_level = pow(level,-1,prime)
    for row in range(level):
        y = pow(omega,row,prime)
        for j,coeff in terms.items():
            value = sum(c*pow(y,eY,prime)*pow(omega,eQ,prime) for c,eY,eQ in coeff) % prime
            normal = sum(c*eY*pow(y,eY,prime)*pow(omega,eQ,prime) for c,eY,eQ in coeff) % prime
            column = (row+j)%level
            A[row,column] = (A[row,column]+value)%prime
            A1[row,column] = (A1[row,column]+normal*inv_level)%prime
    return A,A1


def apply_operator(terms, polynomial, prime, omega):
    result = {}
    for j,coeff in terms.items():
        a = {}
        for c,eY,eQ in coeff:
            add_poly(a,{eY:c*pow(omega,eQ,prime)},prime)
        shifted = {e:c*pow(omega,j*e,prime)%prime for e,c in polynomial.items()}
        add_poly(result,multiply_poly(a,shifted,prime),prime)
    return result


def cyclotomic_block(level,prime,omega):
    term = {0:1}
    total = {0:1}
    for k in range(1,level):
        factor = {-1:1,0:-pow(omega,k,prime)-pow(omega,-k,prime),1:1}
        term = multiply_poly(term,factor,prime)
        add_poly(total,term,prime)
    return total


def solve_unique(A,b,prime):
    matrix = np.column_stack((A,b)).copy()%prime
    pivot_row = 0
    pivots = []
    for column in range(A.shape[1]):
        candidates = [r for r in range(pivot_row,len(matrix)) if matrix[r,column]%prime]
        if not candidates:
            continue
        row = candidates[0]
        matrix[[row,pivot_row]] = matrix[[pivot_row,row]]
        matrix[pivot_row] = matrix[pivot_row]*pow(int(matrix[pivot_row,column]),-1,prime)%prime
        for r in range(len(matrix)):
            if r != pivot_row:
                matrix[r] = (matrix[r]-matrix[r,column]*matrix[pivot_row])%prime
        pivots.append(column)
        pivot_row += 1
    assert len(pivots) == A.shape[1]
    assert not np.any(matrix[pivot_row:,-1])
    answer = np.zeros(A.shape[1],dtype=np.int64)
    for row,column in enumerate(pivots):
        answer[column] = matrix[row,-1]
    assert not np.any((A@answer-b)%prime)
    return answer


def independent_columns(matrix,prime):
    chosen = np.zeros((len(matrix),0),dtype=np.int64)
    for column in matrix.T:
        candidate = np.column_stack((chosen,column))
        if rank(candidate,prime) > chosen.shape[1]:
            chosen = candidate
    return chosen


def normal_period_case(level,P_terms,B_terms,actual_cut):
    prime,_,q = field(level)
    omega = q*q%prime
    F = cyclotomic_block(level,prime,omega)
    if actual_cut:
        actual = actual_laurent_period(level,prime,q,3,[(0,1),(1,-1)]*2)
        assert F == actual
    assert not apply_operator(P_terms,F,prime,omega)
    fF = multiply_poly(F,{0:-1,1:1},prime)
    assert not apply_operator(B_terms,fF,prime,omega)
    P0,P1 = matrix_and_derivative(P_terms,level,prime,omega)
    B0,B1 = matrix_and_derivative(B_terms,level,prime,omega)
    roots = np.array([pow(omega,j,prime) for j in range(level)],dtype=np.int64)
    D0 = np.diag((roots-1)%prime)
    D1 = np.diag(roots*pow(level,-1,prime)%prime)
    assert np.array_equal(P0,B0@D0%prime)
    assert np.array_equal(P1,(B1@D0+B0@D1)%prime)
    values = np.array([evaluate(F,int(z),prime) for z in roots],dtype=np.int64)
    v0 = D0@values%prime
    assert not np.any(B0@v0%prime)
    assert v0[0] == 0 and v0[1] != 0
    assert rank(B0,prime) == level-1
    assert rank(P0,prime) == level-2
    anchor_row = np.zeros(level,dtype=np.int64)
    anchor_row[1] = 1
    system = np.vstack((B0,anchor_row))
    source = np.concatenate((-B1@v0%prime,np.array([0],dtype=np.int64)))
    derivative = solve_unique(system,source,prime)
    predicted = level*int(derivative[0])%prime
    assert predicted == int(values[0])
    J = np.zeros_like(B0)
    J_range = np.zeros_like(B0)
    for row,y in enumerate(roots):
        J[row,(-row)%level] = -y%prime
        J_range[row,(-row-3)%level] = -pow(omega,12,prime)*pow(int(y),8,prime)%prime
    identity = np.eye(level,dtype=np.int64)
    assert np.array_equal(J@J%prime,identity)
    assert np.array_equal(J_range@J_range%prime,identity)
    shift = np.zeros_like(B0)
    for row in range(level):
        shift[row,(row+1)%level] = 1
    assert np.array_equal(J@shift@J%prime,omega*shift.T%prime)
    kappa = -pow(q,-1,prime)%prime
    rotation = kappa*shift%prime
    assert np.array_equal(J@rotation@J%prime,pow(kappa,-1,prime)*shift.T%prime)
    rotation_power = identity.copy()
    for _ in range(level):
        rotation_power = rotation_power@rotation%prime
    assert np.array_equal(rotation_power,pow(-1,level-1,prime)*identity%prime)
    assert np.array_equal(B0@J%prime,J_range@B0%prime)
    assert np.array_equal(J@v0%prime,v0)
    normal_source = -B1@v0%prime
    assert np.array_equal(J_range@normal_source%prime,-normal_source%prime)
    minus_basis = independent_columns((identity-J)%prime,prime)
    assert minus_basis.shape[1] == (level+1)//2
    folded = B0@minus_basis%prime
    folded_solution = solve_unique(folded,normal_source,prime)
    assert level*int((minus_basis@folded_solution%prime)[0])%prime == predicted
    # The first obstruction on the two-dimensional special kernel fixes
    # the same coefficient of its complete delta vector.
    delta = np.zeros(level,dtype=np.int64)
    delta[0] = 1
    assert rank(np.column_stack((P0,P1@delta%prime)),prime) == level-1
    semisimple = values.copy()
    semisimple[0] = 0
    obstruction = P1@(semisimple+predicted*delta)%prime
    assert rank(np.column_stack((P0,obstruction)),prime) == level-2
    return {"level":level,"prime":prime,"actual_cut_polynomial_compared":actual_cut,
            "boundary_kernel_dimension":2,"divided_operator_kernel_dimension":1,
            "normal_derivative_recovers_complete_value":True,
            "Weyl_minus_dimension":minus_basis.shape[1],
            "Weyl_folded_period_recovers_same_value":True,
            "signed_dihedral_ADO_character_checked":True,
            "first_Bockstein_selects_same_period":True}


def initial_dimension_checks():
    # Constant-coefficient operators give independent exact root matrices;
    # repeated initial roots count once, rather than by multiplicity.
    records = []
    for level in (2,3,4,5,6,8,9,10,12,15):
        prime,_,q = field(level)
        omega = q*q%prime
        for exponents in ((0,), (1,), (0,0), (0,1), (0,0,1,1)):
            expected = len({e%level for e in exponents})
            eigenvalues = [pow(omega,e,prime) for e in exponents]
            diagonal = [np.prod([(pow(omega,r,prime)-a)%prime for a in eigenvalues],dtype=object)%prime
                        for r in range(level)]
            actual = level-rank(np.diag(np.array(diagonal,dtype=np.int64)),prime)
            assert actual == expected
            records.append({"level":level,"initial_root_exponents":list(exponents),
                            "distinct_root_bound_attained":actual})
    return records


def ambiguity_checks():
    records = []
    for level in (3,4,5,6,8,10):
        prime,_,q = field(level)
        omega = q*q%prime
        # B=(T-1)(T-Q), P=B*(Y-1). Every root state
        # 1+a*S_N has identical ordinary values but a different target.
        B = {0:omega,1:-(1+omega),2:1}
        P = {}
        for j,c in B.items():
            P[j] = {0:-c,1:c*pow(omega,j,prime)}
        S = {r:1 for r in range(level)}
        complete = []
        for scalar in (0,1,2):
            F = {0:1}
            add_poly(F,S,prime,multiplier=scalar)
            result = {}
            for j,a in P.items():
                shifted = {e:c*pow(omega,j*e,prime)%prime for e,c in F.items()}
                add_poly(result,multiply_poly(a,shifted,prime),prime)
            assert not result
            assert all(evaluate(F,pow(omega,j,prime),prime) == 1 for j in range(1,level))
            complete.append(evaluate(F,1,prime))
        assert len(set(complete)) == 3
        records.append({"level":level,"all_ordinary_values_identical":True,
                        "complete_values_differ":True,"divided_kernel_dimension":2})
    return records


def main():
    P,B,certificate = operator_calibration()
    P_terms,B_terms = coefficient_terms(P),coefficient_terms(B)
    levels = (2,3,4,5,6,7,8,10,12,15,18)
    actual_levels = (2,3,4,5,6,7,8,10)
    normal = [normal_period_case(n,P_terms,B_terms,n in actual_levels) for n in levels]
    initial = initial_dimension_checks()
    ambiguity = ambiguity_checks()
    result = {"scope":"Boundary module and normal derivative; no all-level actual-state identity or volume theorem.",
              "symbolic_certificate":certificate,"normal_period_checks":normal,
              "initial_dimension_checks":initial,"rank_hypothesis_counterexamples":ambiguity}
    Path(__file__).with_name("peripheral_normal_period_results.json").write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({"symbolic_certificate":True,"normal_period_levels":list(levels),
                      "actual_cut_levels":list(actual_levels),"initial_dimension_checks":len(initial),
                      "rank_hypothesis_counterexamples":len(ambiguity),
                      "all_checks_passed":True}),flush=True)


if __name__ == "__main__":
    main()
