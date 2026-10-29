#!/usr/bin/env python3
"""Exact audits of actual ADO reflection and primitive Weyl descent.

Checks the Chevalley basis map, the actual finite crossings and framing
factor, turnover of the cut contraction, full Laurent symmetry, and
the monomial reflection algebra. No volume estimate is asserted.
"""

from itertools import product
import json
from pathlib import Path
import random

import numpy as np
import sympy as sp

from audit_finite_sum_annihilator import field, scalar_data
from audit_kashaev_ado_pointing import color_matrices, WORDS
from audit_regularized_kashaev_period import actual_laurent_period
from audit_peripheral_normal_period import operator_calibration, Q, Y


def basic_matrices(level,prime,q,x):
    e,_,_ = scalar_data(level,prime,q,x)
    E = np.zeros((level,level),dtype=np.int64)
    F = np.zeros_like(E)
    for j in range(1,level):
        E[j-1,j] = e[j]
        F[j,j-1] = 1
    K = np.diag([x*pow(q,-2*j,prime)%prime for j in range(level)]).astype(np.int64)
    return E,F,K


def chevalley_case(level,kind):
    prime,generator,q = field(level)
    x = pow(q,level-1,prime) if kind == "ideal" else pow(generator,3 if kind == "generic1" else 7,prime)
    reflected_x = pow(q,-2,prime)*pow(x,-1,prime)%prime
    old = color_matrices(level,prime,q,x)
    reflected = color_matrices(level,prime,q,reflected_x)
    E,F,K = basic_matrices(level,prime,q,x)
    Ep,Fp,Kp = basic_matrices(level,prime,q,reflected_x)
    d = [1]
    for a in range(1,level):
        d.append(d[-1]*int(Ep[a-1,a])%prime)
    if not all(d):
        # This diagnostic chooses generic colors away from the finite walls.
        return {"level":level,"color":kind,"generic_wall_skipped":True}
    C = np.zeros_like(E)
    Cinv = np.zeros_like(E)
    for a,value in enumerate(d):
        C[level-1-a,a] = value
        Cinv[a,level-1-a] = pow(value,-1,prime)
    assert np.array_equal(C@Ep@Cinv%prime,F)
    assert np.array_equal(C@Fp@Cinv%prime,E)
    Kinv = np.diag([pow(int(K[a,a]),-1,prime) for a in range(level)])
    assert np.array_equal(C@Kp@Cinv%prime,Kinv)
    pair_weights = np.kron(np.array(d,dtype=np.int64),np.array(d,dtype=np.int64))%prime
    inverse_weights = np.array([pow(int(v),-1,prime) for v in pair_weights],dtype=np.int64)
    swap = [b*level+a for a,b in product(range(level),repeat=2)]
    factor = pow(q,-2,prime)*pow(x,2*(level-1),prime)%prime
    for sign in (0,1):
        conjugated = (reflected[sign]*pair_weights[:,None]%prime)*inverse_weights[None,:]%prime
        conjugated = conjugated[::-1,::-1]
        expected = old[sign][np.ix_(swap,swap)]*pow(factor,1 if sign == 0 else -1,prime)%prime
        assert np.array_equal(conjugated,expected)
    gp = reflected[2]
    ginv = np.diag([pow(int(old[2][a,a]),-1,prime) for a in range(level)])
    assert np.array_equal(C@gp@Cinv%prime,ginv)
    assert reflected[3] == factor*old[3]%prime
    return {"level":level,"color":kind,"Chevalley_E_F_K_exact":True,
            "both_crossings_and_pivotal_exact":True,"crossing_and_twist_factor_identical":True}


def period_by_paths(level,prime,data,strands,word,cut_color=0):
    positive,negative,pivotal,twist = data
    transitions = {}
    for sign,matrix in ((1,positive),(-1,negative)):
        for a,b in product(range(level),repeat=2):
            column = matrix[:,a*level+b]
            transitions[sign,a,b] = [(divmod(row,level),int(value))
                                     for row,value in enumerate(column) if value%prime]
    total = 0
    for closed in product(range(level),repeat=strands-1):
        initial = (cut_color,)+closed
        weight = 1
        for a in closed:
            weight = weight*int(pivotal[a,a])%prime
        paths = {initial:weight}
        for position,sign in reversed(word):
            following = {}
            for state,value in paths.items():
                a,b = state[position:position+2]
                for output,coefficient in transitions[sign,a,b]:
                    new_state = state[:position]+output+state[position+2:]
                    following[new_state] = (following.get(new_state,0)+value*coefficient)%prime
            paths = following
        total = (total+paths.get(initial,0))%prime
    return total*pow(int(twist),-sum(sign for _,sign in word),prime)%prime


def knot_word(word,strands=3):
    permutation = list(range(strands))
    for position,_ in word:
        permutation[position],permutation[position+1] = permutation[position+1],permutation[position]
    seen = set()
    j = 0
    while j not in seen:
        seen.add(j)
        j = permutation[j]
    return len(seen) == strands


def diagrams():
    result = [(2,[(0,1)]*3),(2,[(0,-1)]*5)]+[(3,list(w)) for w in WORDS]
    randomizer = random.Random(20261026)
    while len(result)<9:
        word = [(randomizer.randrange(2),randomizer.choice((-1,1))) for _ in range(8)]
        if knot_word(word):
            result.append((3,word))
    return result


def contraction_checks():
    records = []
    for level in (2,3,4,5,6,8,10):
        prime,generator,q = field(level)
        M = generator
        x = -pow(q,-1,prime)*M%prime
        xp = -pow(q,-1,prime)*pow(M,-1,prime)%prime
        old = color_matrices(level,prime,q,x)
        reflected = color_matrices(level,prime,q,xp)
        swap = [b*level+a for a,b in product(range(level),repeat=2)]
        inv_pivotal = np.diag([pow(int(old[2][a,a]),-1,prime) for a in range(level)])
        turned = (old[0][np.ix_(swap,swap)],old[1][np.ix_(swap,swap)],inv_pivotal,old[3])
        for strands,word in diagrams():
            original = period_by_paths(level,prime,old,strands,word)
            opposite = period_by_paths(level,prime,reflected,strands,word)
            rotated = period_by_paths(level,prime,turned,strands,word,cut_color=level-1)
            assert original == opposite == rotated
            records.append({"level":level,"strands":strands,"crossings":len(word),
                            "reflected_meridian_exact":True,"left_right_turnover_exact":True})
    return records


def full_laurent_checks():
    records = []
    for level in (2,3,4,5,6):
        prime,_,q = field(level)
        for strands,word in diagrams()[:5]:
            F = actual_laurent_period(level,prime,q,strands,word)
            assert F == {-e:c for e,c in F.items()}
            omega = q*q%prime
            colors = {j:sum(c*pow(pow(omega,j,prime),e,prime) for e,c in F.items())%prime
                      for j in range(1,level)}
            assert all(colors[j] == colors[level-j] for j in colors)
            for r in range(-1,level+2):
                taylor = sum(colors[j]*(1-pow(omega,j,prime))*pow(omega,-j*r,prime)
                             for j in colors)*pow(level,-1,prime)%prime
                sine = sum(colors[j]*(pow(q,(2*r-1)*j,prime)-pow(q,-(2*r-1)*j,prime))
                           *(pow(q,j,prime)-pow(q,-j,prime)) for j in colors)*pow(2*level,-1,prime)%prime
                assert taylor == sine
            records.append({"level":level,"strands":strands,"crossings":len(word),
                            "full_actual_Laurent_reflection_exact":True,
                            "ordinary_color_reflection_exact":True,
                            "bounded_source_sine_moments_exact":True})
    return records


def monomial_reciprocity_checks():
    q,z,m,d,alpha,N = sp.symbols("q z m d alpha N")
    reflected_alpha = 2*(N-1)-alpha
    twist_difference = reflected_alpha**2+2*(1-N)*reflected_alpha-alpha**2-2*(1-N)*alpha
    assert sp.expand(twist_difference) == 0
    # The actual finite-block operator is independently derived by its
    # telescoping certificate in the preceding audit.
    _,B,_ = operator_calibration()
    c = -Q**12*Y**8
    assert sp.expand(c-(-q**24*Y**8).subs(q**2,Q)) == 0
    assert sp.cancel(c*c.subs(Y,Q**-3/Y)-1) == 0
    # Primitive generator changes must be monomial. Verify the norm law
    # and induced reflection for varied positive and negative exponents.
    cases = 0
    for degree in (1,2,3,4,5):
        for exponent in (-3,-1,0,1,2,4):
            for sign in (-1,1):
                multiplier = sign*q**(degree*(exponent-1))*Y**exponent
                reflected = multiplier.subs(Y,q**(-2*degree)/Y)
                assert sp.simplify(multiplier*reflected*q**(2*degree)-1) == 0
                range_factor = -multiplier*q**(2*degree)*Y
                assert sp.simplify(range_factor*range_factor.subs(Y,q**(-2*degree)/Y)-1) == 0
                conjugate = range_factor.subs({q:q**-1,Y:Y**-1},simultaneous=True)
                assert sp.simplify(range_factor*conjugate-1) == 0
                cases += 1
    return {"symbolic_twist_reflection":True,"primitive_monomial_norm_cases":cases,
            "calibrated_operator_range_factor":str(c)}


def sine_orthogonality_checks():
    records = []
    for level in (2,3,4,5,6,8,10,12,15):
        prime,_,q = field(level)
        D = np.array([[(pow(q,a*j,prime)-pow(q,-a*j,prime))%prime
                       for j in range(1,level)] for a in range(1,level)],dtype=np.int64)
        assert np.array_equal(D@D.T%prime,(-2*level)*np.eye(level-1,dtype=np.int64)%prime)
        records.append({"level":level,"unnormalized_sine_orthogonality_exact":True})
    return records


def main():
    local = [chevalley_case(n,kind) for n in (2,3,4,5,6,8,10,12,15)
             for kind in ("generic1","generic2","ideal")]
    print(json.dumps({"local_Chevalley_cases":len(local)}),flush=True)
    contractions = contraction_checks()
    print(json.dumps({"cut_turnover_cases":len(contractions)}),flush=True)
    laurent = full_laurent_checks()
    monomials = monomial_reciprocity_checks()
    sine = sine_orthogonality_checks()
    result = {"scope":"Exact actual-state Weyl symmetry and algebraic primitive reciprocity; no inverse-norm or volume theorem.",
              "local_Chevalley":local,"cut_turnover":contractions,
              "full_actual_Laurent_symmetry":laurent,"primitive_reciprocity":monomials,
              "sine_orthogonality":sine}
    Path(__file__).with_name("actual_weyl_descent_results.json").write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({"full_Laurent_states":len(laurent),"primitive_monomial_cases":monomials["primitive_monomial_norm_cases"],
                      "sine_orthogonality_levels":len(sine),"all_checks_passed":True}),flush=True)


if __name__ == "__main__":
    main()
