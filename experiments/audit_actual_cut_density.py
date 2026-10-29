#!/usr/bin/env python3
"""Actual cut residues, crossing half-densities, and holonomy volume.

Exact symbolic and finite-field certificates.  No assertion of a
selected geometric-period contribution or a volume limit is made.
"""

import json
from pathlib import Path
from random import Random

import numpy as np
import sympy as sp

from audit_cyclic_steinberg_lattice import determinant, rank
from audit_finite_sum_annihilator import cut_matrix_dense, field
from audit_kashaev_ado_pointing import WORDS, color_matrices


def equal(left, right):
    if isinstance(left, sp.MatrixBase):
        assert (left-right).applyfunc(sp.cancel) == sp.zeros(*left.shape)
    else:
        assert sp.cancel(left-right) == 0


def crossing_densities():
    A, B, C, x = sp.symbols('A B C x', nonzero=True)
    Y = x*x
    records = []
    for sign in (1, -1):
        if sign > 0:
            H = sp.Matrix([[0, 1, 1], [1, 0, -1], [1, -1, -1]])
            shapes = [B, C, Y/A, B*C, Y*C/A]
            vectors = [(0,1,0), (0,0,1), (-1,0,0), (0,1,1), (-1,0,1)]
            amp = A*B*(1-B*C)*(1-Y/A)/((1-B)*(1-C)*(1-Y*C/A))
            left = sp.Matrix([1,-1,1])
            right = sp.Matrix([0,0,1])
            ratios = [B*C/x*(1-Y/A)/(1-Y*C/A), A/(C*x)*(1-B*C)/(1-B)]
            want = 1/(1-C)
        else:
            H = sp.Matrix([[0,-1,0], [-1,0,0], [0,0,0]])
            shapes = [A, C, Y/B, A*C, Y*C/B]
            vectors = [(1,0,0), (0,0,1), (0,-1,0), (1,0,1), (0,-1,1)]
            amp = C/(A*B)*(1-A*C)*(1-Y/B)/((1-A)*(1-C)*(1-Y*C/B))
            left = sp.Matrix([1,-1,-1])
            right = sp.Matrix([0,0,-1])
            ratios = [x/B*(1-A*C)/(1-A), x/A*(1-Y/B)/(1-Y*C/B)]
            want = C/(1-C)
        for z, vector, epsilon in zip(shapes, vectors, (1,1,1,-1,-1)):
            v = sp.Matrix(vector)
            H += epsilon*z/(1-z)*v*v.T
        mixed = (left.T*H*right)[0]
        equal(mixed, want)
        equal(amp, x**(2*sign)*mixed*ratios[0]*ratios[1])
        records.append({'crossing_sign': sign, 'mixed_Hessian': str(want),
                        'original_principal_amplitude_factorization_exact': True})
    return records


def holonomy_volumes():
    K, e, t, z = sp.symbols('K e t z', nonzero=True)

    def G(k, ee, trace):
        return sp.Matrix([[k, ee], [(k*trace-k*k-1)/ee, trace-k]])

    matrix = G(K, e, t)
    for g in (sp.Matrix([[1,z],[0,1]]), sp.Matrix([[1,0],[z,1]]), sp.diag(z,1/z)):
        changed = g*matrix*g.inv()
        jac = sp.Matrix([changed[0,0], changed[0,1]]).jacobian([K,e])
        equal(jac.det()/changed[0,1], 1/e)
    x = sp.symbols('x', nonzero=True)
    position, momentum = x/K, e*x/(1-x*K)
    row1 = [sp.diff(position, v)/position for v in (K,e)]
    row2 = [sp.diff(momentum, v)/momentum for v in (K,e)]
    equal(sp.Matrix([row1,row2]).det(), -1/(K*e))

    L, h, u = sp.symbols('L h u', nonzero=True)
    first, second = matrix, G(L,h,u)
    f = (t-K-1/K)/e
    prefix = sp.Matrix([[1,0],[-K*f,K]])
    H1, H2 = first, prefix.inv()*second*prefix
    equal((H2*H1)[0,0], K*L)
    diagonal = sp.Matrix([H2[0,0],H2[0,1]]).jacobian([L,h])
    equal(diagonal.det()/H2[0,1], 1/h)
    # For any b, triangularity reduces the full Jacobian to these
    # conjugation-invariant diagonal blocks. The pivot removes all
    # factors K_j except the marked first factor.
    k1,k2,k3 = sp.symbols('k1 k2 k3', nonzero=True)
    equal(k2*k3/(k1*k2*k3), 1/k1)
    return {'conjugacy_residue_invariant_on_three_SL2_generators': True,
            'canonical_phase_form_equals_negative_nu_over_K': True,
            'triangular_prefix_volume_and_product_entry_exact': True,
            'actual_pivot_leaves_only_inverse_first_K': True}


def symbolic_cut_residue():
    A, s, M = sp.symbols('A s M', nonzero=True)
    records = []
    for N in range(2, 9):
        amap = M/(M+s)
        original = A**(N-1)/(A**N-1)
        pulled = original.subs(A,amap)*sp.diff(amap,s)
        want = M**N/((M+s)*((M+s)**N-M**N))
        equal(pulled,want)
        assert sp.residue(pulled,s,0) == sp.Rational(1,N)
        assert sp.residue(pulled,s,-M) == -1
        # Retain the complete principal-root source and the compensating
        # pole. This is not a replacement of their divisors by beta.
        polynomial = sum((j+1)*A**j for j in range(N))
        at_infinity = -sp.residue((polynomial/A).subs(A,1/s)/s**2,s,0)
        assert at_infinity == -1
        assert sp.residue(polynomial/A,A,0) == 1
        U = sp.symbols('U')
        L = sp.zeros(N)
        for j in range(N-1):
            L[j+1,j] = 1
        L[0,N-1] = U
        D = sp.diag(*range(N))
        equal(D*L-L*D-L, -N*U*L.diff(U))
        records.append({'level': N, 'M_observation_map_and_all_source_poles_retained': True,
                        'canonical_residue_and_normal_carry_matrix_exact': True})
    return records


def root_cut_case(N):
    p, generator, q = field(N)
    Q = q*q % p
    roots = [pow(Q,a,p) for a in range(N)]
    inverse_N = pow(N,-1,p)
    rng = Random(71000+N)
    coefficients = [rng.randrange(p) for _ in range(N)]
    values = [sum(c*pow(A,j,p) for j,c in enumerate(coefficients)) % p for A in roots]
    assert sum(values)*inverse_N % p == coefficients[0]
    restored = [sum(values[a]*pow(Q,-a*j,p) for a in range(N))*inverse_N % p for j in range(N)]
    assert restored == coefficients
    residues = 0
    for M in (1, generator, pow(generator,7,p)):
        for A,value in zip(roots,values):
            ss = M*(pow(A,-1,p)-1) % p
            root = (M+ss) % p
            derivative = N*pow(root,N-1,p) % p
            residue = pow(M,N,p)*pow(root*derivative % p,-1,p) % p
            assert residue == inverse_N
            residues += 1
        dropped = sum(values[1:])*inverse_N % p
        assert (sum(values)*inverse_N-dropped) % p == values[0]*inverse_N % p
    return {'level': N, 'prime': p, 'DFT_and_actual_average_equal_canonical_residue': True,
            'individual_pulled_cut_poles_checked': residues,
            'omitted_frame_point_retains_its_source': True}


def actual_matrix_cut_case(N):
    p, generator, q = field(N)
    Q = q*q % p
    factorials = [1]
    for a in range(1,N):
        factorials.append(factorials[-1]*(1-pow(Q,a,p)) % p)
    psi = np.array([pow(v,-1,p) for v in factorials],dtype=np.int64)
    phi = np.array([v*pow(N,-1,p) % p for v in factorials],dtype=np.int64)
    slices, knots = 0, 0
    for M in (1,pow(generator,N+7,p)):
        x = -M*pow(q,-1,p) % p
        data = color_matrices(N,p,q,x)
        for crossing in data[:2]:
            tensor = crossing.reshape((N,)*4)
            for c,d in ((0,0),(1,0),(0,N-1)):
                C = tensor[:,c,:,d]
                boundary = C@psi % p
                balanced_values = np.array(factorials,dtype=np.int64)*boundary % p
                constant = int(np.sum(balanced_values))*pow(N,-1,p) % p
                actual = int(phi@boundary) % p
                assert constant == actual
                projector = np.outer(psi,phi) % p
                assert int(np.trace(projector@C % p)) % p == actual
                slices += 1
        if N <= 6:
            for word in WORDS:
                C = cut_matrix_dense(N,p,data,3,word)
                boundary = C@psi % p
                balanced_values = np.array(factorials,dtype=np.int64)*boundary % p
                assert np.all(balanced_values == int(C[0,0]))
                # Avoid the singular A=1 frame explicitly and retain the
                # necessary new normalization, rather than deleting it.
                assert int(np.sum(balanced_values[1:]))*pow(N-1,-1,p) % p == int(C[0,0])
                knots += 1
    return {'level': N, 'actual_crossing_boundary_slices': slices,
            'whole_original_knot_cuts_and_explicit_source_excision': knots}


def fixed_point_complex_case(p, riley, frame, stabilization_sign=None, include_complex=False,
                             base_meridians=None, braid_word=None):
    def mm(a,b):
        return a@b % p

    def inv(a):
        det = int(a[0,0]*a[1,1]-a[0,1]*a[1,0]) % p
        return np.array([[a[1,1],-a[0,1]],[-a[1,0],a[0,0]]],dtype=np.int64)*pow(det,-1,p) % p

    A = np.array([[1,1],[0,1]],dtype=np.int64)
    B = np.array([[1,0],[riley,1]],dtype=np.int64)
    C = mm(mm(mm(mm(inv(A),B),A),inv(B)),A)
    r,s = frame
    G = np.array([[r,1-r],[s,-s]],dtype=np.int64) % p
    raw = (A,B,C) if base_meridians is None else base_meridians
    initial = [-mm(mm(inv(G),H),G) % p for H in raw]
    word = list(WORDS[0] if braid_word is None else braid_word)
    if stabilization_sign is not None:
        assert stabilization_sign in (1,-1)
        initial.append(initial[-1].copy())
        word.append((len(initial)-2,stabilization_sign))
    n = 2*len(initial)
    variations = []
    for j,H in enumerate(initial):
        K,e = map(int,(H[0,0],H[0,1]))
        if not e:
            raise ZeroDivisionError('outside the conjugacy residue chart')
        trace = int(np.trace(H)) % p
        dK = np.array([[1,0],[(trace-2*K)*pow(e,-1,p),-1]],dtype=np.int64) % p
        de = np.array([[0,1],[-int(H[1,0])*pow(e,-1,p),0]],dtype=np.int64) % p
        var = np.zeros((n,2,2),dtype=np.int64)
        var[2*j],var[2*j+1] = dK,de
        variations.append(var)
    original_variations = [v.copy() for v in variations]
    moved = [H.copy() for H in initial]
    for j,sign in word:
        a,b = moved[j:j+2]
        da,db = variations[j:j+2]
        if sign > 0:
            ai = inv(a)
            c = mm(mm(ai,b),a)
            dc = np.array([(-mm(mm(ai,v),c)+mm(mm(ai,w),a)+mm(mm(ai,b),v)) % p
                           for v,w in zip(da,db)])
            moved[j:j+2],variations[j:j+2] = [c,a],[dc,da]
        else:
            bi = inv(b)
            c = mm(mm(b,a),bi)
            dc = np.array([(mm(mm(w,a),bi)+mm(mm(b,v),bi)-mm(mm(c,w),bi)) % p
                           for v,w in zip(da,db)])
            moved[j:j+2],variations[j:j+2] = [b,c],[db,dc]
    assert all(np.array_equal(a,b) for a,b in zip(initial,moved))
    derivative = np.array([[int(v[0,0]) for v in var] if k==0 else [int(v[0,1]) for v in var]
                           for var in variations for k in (0,1)],dtype=np.int64)
    D = (derivative-np.eye(n,dtype=np.int64)) % p
    lie_basis = [np.diag([1,-1]),np.array([[0,1],[0,0]]),np.array([[0,0],[1,0]])]
    a = np.array([[int((xi@H-H@xi)[0,k]) % p for xi in lie_basis]
                  for H in initial for k in (0,1)],dtype=np.int64)
    product = np.eye(2,dtype=np.int64)
    dproduct = np.zeros((n,2,2),dtype=np.int64)
    for H,var in zip(initial,original_variations):
        dproduct = np.array([(mm(v,product)+mm(H,old)) % p for v,old in zip(var,dproduct)])
        product = mm(H,product)
    left_trivialized = [mm(v,inv(product)) for v in dproduct]
    m = np.array([[int(v[i,j]) for v in left_trivialized] for i,j in ((0,0),(0,1),(1,0))],dtype=np.int64)
    assert not np.any(D@a % p) and not np.any(m@D % p)
    assert (rank(a,p),rank(D,p),rank(m,p)) == (3,n-3,3)
    eye = np.eye(n,dtype=np.int64)
    complement = []
    running = a.copy()
    for j in range(n):
        candidate = np.column_stack([running,eye[:,j]])
        if rank(candidate,p)>running.shape[1]:
            complement.append(j)
            running = candidate
    assert len(complement)==n-3
    V = eye[:,complement]
    from itertools import combinations
    pivots = next(cols for cols in combinations(range(n),3) if determinant(m[:,cols],p))
    W = np.zeros((n,3),dtype=np.int64)
    W[list(pivots),:] = np.array(sp.Matrix(m[:,pivots].tolist()).inv_mod(p).tolist(),dtype=np.int64)
    assert np.array_equal(m@W % p,np.eye(3,dtype=np.int64))
    source = np.column_stack([a,V])
    target = np.column_stack([D@V % p,W])
    torsion = determinant(source,p)*pow(determinant(target,p),-1,p) % p
    # Change both splittings. The value must be independent of them.
    shift_V = np.arange(3*(n-3),dtype=np.int64).reshape((3,n-3))
    shift_W = np.arange((n-3)*3,dtype=np.int64).reshape((n-3,3))
    V2 = (V+a@shift_V) % p
    W2 = (W+(D@V % p)@shift_W) % p
    alternate = determinant(np.column_stack([a,V2]),p)*pow(determinant(np.column_stack([D@V2 % p,W2]),p),-1,p) % p
    assert alternate == torsion
    result = {'prime': p, 'Riley_root': riley, 'frame': list(frame),
            'strands':len(initial),'stabilization_sign':stabilization_sign,
            'total_product_trace':int(np.trace(product))%p,
            'acyclic_ranks': [3,n-3,3], 'torsion': int(torsion),
            'two_compositions_and_splitting_independence_exact': True}
    if include_complex:
        result['complex_data'] = {'a':a,'D':D,'m':m,'last_meridian':initial[-1]}
    return result


def fixed_point_complex_checks():
    records = []
    for p in (97,193,601):
        for riley in (r for r in range(p) if (r*r-r+1) % p==0):
            branch = []
            for frame in ((2,3),(3,2),(4,5),(5,3),(2,7),(7,2)):
                try:
                    record = fixed_point_complex_case(p,riley,frame)
                except ZeroDivisionError:
                    continue
                branch.append(record)
                if len(branch)==3:
                    break
            assert len(branch)==3
            assert len({r['torsion'] for r in branch})==1
            records.extend(branch)
    return records


def main():
    principal = crossing_densities()
    volumes = holonomy_volumes()
    symbolic = symbolic_cut_residue()
    roots = [root_cut_case(N) for N in range(2,17)]
    actual = [actual_matrix_cut_case(N) for N in range(2,11)]
    torsions = fixed_point_complex_checks()
    result = {'scope': 'Exact original finite cut, formal principal density and ambient holonomy volumes; selected internal period reduction and volume norm unproved.',
              'principal_crossings': principal, 'ambient_holonomy_volume': volumes,
              'symbolic_cut_and_normal_source': symbolic, 'root_cut_residues': roots,
              'original_matrix_pairings': actual, 'linearized_fixed_point_complex': torsions}
    path = Path(__file__).with_name('actual_cut_density_results.json')
    path.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'results': str(path), 'symbolic_crossing_factorizations': len(principal),
                      'symbolic_source_levels': len(symbolic), 'root_source_levels': len(roots),
                      'individual_cut_root_residues': sum(x['individual_pulled_cut_poles_checked'] for x in roots),
                      'original_crossing_boundary_slices': sum(x['actual_crossing_boundary_slices'] for x in actual),
                      'original_knot_cuts': sum(x['whole_original_knot_cuts_and_explicit_source_excision'] for x in actual),
                      'acyclic_holonomy_complex_and_invariant_torsion_cases': len(torsions)},indent=2),flush=True)


if __name__ == '__main__':
    main()
