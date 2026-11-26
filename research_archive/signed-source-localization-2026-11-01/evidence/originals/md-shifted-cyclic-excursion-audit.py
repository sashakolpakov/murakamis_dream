#!/usr/bin/env python3
"""Finite exact checks of the original bipyramid excursion reduction.

This is a bounded algebra audit, not a proof of a norm or spectral gap.
Local numerator coefficients are built from powers of the original
upper-band Casimir, independently of the continuant and transfer.
Only the Python standard library is required.
"""
from __future__ import annotations

import argparse
from collections import defaultdict, deque
import hashlib
import json
from math import lcm
from pathlib import Path
import time


def prime(n):
    if n < 2:
        return False
    k = 2
    while k * k <= n:
        if n % k == 0:
            return False
        k += 1
    return True


def finite_field(N, lower):
    step = lcm(4, 2 * N)
    p = ((lower + step - 2) // step) * step + 1
    while not prime(p):
        p += step
    order = 2 * N
    proper = [k for k in range(1, order) if order % k == 0]
    for q in range(2, p):
        if pow(q, order, p) == 1 and all(pow(q, k, p) != 1 for k in proper):
            return p, q
    raise AssertionError("missing finite-field root")


def chi_coefficients(N):
    p0, p1 = [2], [0, 1]
    for _ in range(2, N + 1):
        nxt = [0] + p1
        for k, a in enumerate(p0):
            nxt[k] -= a
        p0, p1 = p1, nxt
    out = p1[:]
    out[0] += 2
    return out


def reduce_value(x, modulus):
    return x % modulus if modulus else x


def add_to(out, key, value, modulus):
    value = reduce_value(out.get(key, 0) + value, modulus)
    if value:
        out[key] = value
    else:
        out.pop(key, None)


def polynomial_matrix_product(A, B, modulus):
    """Sparse matrices whose entries are polynomials in independent x,y."""
    by_row = defaultdict(list)
    for (k, j), poly in B.items():
        by_row[k].append((j, poly))
    result = {}
    for (i, k), ap in A.items():
        for j, bp in by_row.get(k, []):
            target = result.setdefault((i, j), {})
            for (x, y), a in ap.items():
                for (u, v), b in bp.items():
                    add_to(target, (x + u, y + v), a * b, modulus)
    return {key: val for key, val in result.items() if val}


def numerator_from_matrix(N, sigma, modulus=None, q=None, identity=False):
    """Return (i,j,x_degree,y_degree) coefficients by literal matrix powers."""
    d = N - 1
    if modulus is None:
        assert N == 3
        diagonal, single, double = [1, -2, 1], [0, 3, 3], [0, 0, 3]
    else:
        qp = lambda k: pow(q, k % (2 * N), modulus)
        diagonal = [reduce_value(qp(2*r+1)+qp(-2*r-1), modulus)
                    for r in range(N)]
        single = [reduce_value(2-qp(2*r)-qp(-2*r), modulus)
                  for r in range(N)]
        double = [reduce_value(qp(1)+qp(-1)-qp(2*r-1)-qp(-2*r+1), modulus)
                  for r in range(N)]
    C = {}
    for j in range(N):
        C[j, j] = {(0, 0): diagonal[j]}
        if j:
            C[j-1, j] = {(1, 0): -single[j], (0, 1): -single[j]}
        if j >= 2:
            C[j-2, j] = {(1, 1): -double[j]}
    powers = {(i, i): {(0, 0): 1} for i in range(N)}
    result = {}
    coefficients = chi_coefficients(N)
    for r in range(N):
        weight = (int(r == 0) if identity else
                  sum(coefficients[k] * sigma ** (k-1-r)
                      for k in range(r+1, N+1)))
        weight = reduce_value(weight, modulus)
        for (i, j), poly in powers.items():
            for (x, y), value in poly.items():
                add_to(result, (i, j, x, y), weight * value, modulus)
        if r != d:
            powers = polynomial_matrix_product(C, powers, modulus)
    if not identity:
        vm = {}
        for (i,j,x,y), value in result.items():
            vm.setdefault((i,j),{})[x,y] = value
        defect = polynomial_matrix_product(C,vm,modulus)
        for key, poly in vm.items():
            target=defect.setdefault(key,{})
            for exponent,value in poly.items():
                add_to(target,exponent,-sigma*value,modulus)
        scalar=sum(a*sigma**k for k,a in enumerate(coefficients))
        for i in range(N):
            add_to(defect.setdefault((i,i),{}),(0,0),scalar,modulus)
        assert not any(defect.values()), "full polynomial resolvent equation failed"
    return result


def local_coefficients(N, j, kernel):
    """Keep the actual reversed middle order in every south coupon."""
    d = N - 1
    out = {}
    for (i, r, x, y), value in kernel.items():
        if j % 2:
            if x:
                continue
            a, b, c, pole = i, y, d-r, 0
        else:
            a, b, c, pole = d-r, y, i, x
        assert a+b+c+pole == d
        key = (a, b, c, pole)
        assert key not in out
        out[key] = value
    return out


def literal_source(N, locals_, modulus, cross=False, targets=None):
    """Direct homogeneous monomial multiplication with the original targets."""
    m, d, h = len(locals_), N-1, (N-1)//2
    targets=tuple(targets) if targets is not None else (d,)*m
    result = {(0,)*m: 1}
    for j, local in enumerate(locals_):
        terms = {}
        for (a, b, c, pole), value in local.items():
            if cross and (a > h or c > h):
                continue
            exps = [0]*m
            exps[0] = pole
            legal = True
            for face, power in (((j-1) % m, a), (j, b), ((j+1) % m, c)):
                if face == 0:
                    if power:
                        legal = False
                        break
                else:
                    exps[face] += power
            if legal:
                add_to(terms, tuple(exps), value, modulus)
        new = {}
        for alpha, a in result.items():
            for beta, b in terms.items():
                gamma = tuple(x+y for x, y in zip(alpha, beta))
                if all(a<=b for a,b in zip(gamma,targets)):
                    add_to(new, gamma, a*b, modulus)
        result = new
    return result.get(targets, 0)


def identity_matrix(n):
    return {(i, i): 1 for i in range(n)}


def matrix_product(A, B, modulus):
    rows = defaultdict(list)
    for (k, j), value in B.items():
        rows[k].append((j, value))
    out = {}
    for (i, k), a in A.items():
        for j, b in rows.get(k, []):
            add_to(out, (i, j), a*b, modulus)
    return out


def matrix_sum(A, B, modulus):
    out = dict(A)
    for key, value in B.items():
        add_to(out, key, value, modulus)
    return out


def trace(A, modulus):
    return reduce_value(sum(v for (i, j), v in A.items() if i == j), modulus)


def transfer(N, j, local, modulus, cross=False, clocks=None, q=None,
             u_max=None, rim_targets=None):
    d, h = N-1, (N-1)//2
    u_max=d if u_max is None else u_max
    target = (0 if j == 1 else d) if rim_targets is None else rim_targets[j-1]
    out = {}
    for u in range(u_max+1):
        a = target-u
        if a < 0:
            continue
        for v in range(N):
            for (aa, b, c, pole), value in local.items():
                if aa != a or b+v > u_max:
                    continue
                if cross and (a > h or c > h):
                    continue
                if clocks is not None:
                    alpha, beta, gamma, mu = clocks
                    exponent = alpha*a+beta*b+gamma*c+mu*pole
                    value = value * pow(q, exponent % (2*N), modulus)
                add_to(out, (u*N+v, (v+b)*N+c), value, modulus)
    return out


def transfer_trace(N, transfers, modulus, u_max=None):
    product = identity_matrix(((N-1 if u_max is None else u_max)+1)*N)
    for T in transfers:
        product = matrix_product(product, T, modulus)
    return trace(product, modulus)


def blocks(N, transfers):
    m, d, h, width = len(transfers), N-1, (N-1)//2, N*N
    good, bad = [], []
    for j in range(m):
        target = 0 if j == 1 else d
        for u in range(N):
            for v in range(N):
                index = j*width+u*N+v
                (good if v <= h and 0 <= target-u <= h else bad).append(index)
    good_map, bad_map = {v:i for i,v in enumerate(good)}, {v:i for i,v in enumerate(bad)}
    matrices = ({}, {}, {}, {})
    for j, T in enumerate(transfers):
        for (i, k), value in T.items():
            row, col = j*width+i, ((j+1) % m)*width+k
            row_good, col_good = row in good_map, col in good_map
            number = (0 if row_good else 2)+(0 if col_good else 1)
            rm, cm = (good_map if row_good else bad_map), (good_map if col_good else bad_map)
            matrices[number][rm[row], cm[col]] = value
    return matrices, len(good), len(bad)


def schur_coefficient(N, transfers, modulus):
    m = len(transfers)
    (A, B, C, D), np, nq = blocks(N, transfers)
    ap, dp = [identity_matrix(np)], [identity_matrix(nq)]
    for _ in range(m):
        ap.append(matrix_product(ap[-1], A, modulus))
        dp.append(matrix_product(dp[-1], D, modulus))
    cross_trace = trace(ap[m], modulus)*pow(m, -1, modulus) % modulus
    excursion = [matrix_product(matrix_product(B, dp[j], modulus), C, modulus)
                 for j in range(m-1)]
    W = {}
    for degree in range(2, m+1):
        coefficient = {}
        for i in range(degree-1):
            coefficient = matrix_sum(coefficient,
                matrix_product(ap[i], excursion[degree-2-i], modulus), modulus)
        W[degree] = coefficient
    power, answer = W, 0
    for ell in range(1, m//2+1):
        answer += trace(power.get(m, {}), modulus)*pow(ell, -1, modulus)
        answer %= modulus
        nxt = {}
        for i, a in power.items():
            for j, b in W.items():
                if i+j <= m:
                    nxt[i+j] = matrix_sum(nxt.get(i+j, {}),
                                        matrix_product(a, b, modulus), modulus)
        power = nxt
    return answer, cross_trace


def check_clocks(N, j, local, T, modulus, q):
    d = N-1
    target = 0 if j == 1 else d
    alpha, beta, gamma, mu = j+1, 2*j-1, j*j+2, j % 3-1
    direct = transfer(N, j, local, modulus, clocks=(alpha,beta,gamma,mu), q=q)
    predicted = {}
    for (row, col), value in T.items():
        u,v = divmod(row,N)
        uu,vv = divmod(col,N)
        exponent = (alpha*target+mu*(d-target)
                    +(mu-alpha)*u+(mu-beta)*v
                    +(beta-mu)*uu+(gamma-mu)*vv)
        predicted[row,col] = value*pow(q, exponent % (2*N), modulus) % modulus
    assert direct == predicted


def support_longest_bad_path(N, m):
    """All homogeneous support, without evaluating any spectral coefficients."""
    d,h,width = N-1,(N-1)//2,N*N
    nodes = []
    good = set()
    for j in range(m):
        target = 0 if j == 1 else d
        for u in range(N):
            for v in range(N):
                k=j*width+u*N+v
                if v <= h and 0 <= target-u <= h:
                    good.add(k)
                else:
                    nodes.append(k)
    edges = {k:set() for k in nodes}
    for j in range(m):
        target = 0 if j == 1 else d
        for u in range(N):
            a=target-u
            if a < 0:
                continue
            for v in range(N):
                row=j*width+u*N+v
                if row in good:
                    continue
                for b in range(d-a+1):
                    if v+b > d:
                        continue
                    cs = [d-a-b] if j % 2 else range(d-a-b+1)
                    for c in cs:
                        col=((j+1) % m)*width+(v+b)*N+c
                        if col not in good:
                            edges[row].add(col)
    indegree={k:0 for k in nodes}
    for targets in edges.values():
        for k in targets:
            indegree[k]+=1
    queue=deque(k for k in nodes if indegree[k]==0)
    length={k:0 for k in nodes}
    visited=0
    while queue:
        row=queue.popleft()
        visited+=1
        for col in edges[row]:
            length[col]=max(length[col],length[row]+1)
            indegree[col]-=1
            if indegree[col]==0:
                queue.append(col)
    assert visited == len(nodes), "bad support has a directed cycle"
    longest=max(length.values(),default=0)
    assert longest < 3*m
    return {"N":N,"m":m,"bad_states":len(nodes),
            "bad_edges":sum(map(len,edges.values())),
            "longest_bad_path_edges":longest,"nilpotence_bound":3*m}


def integer_counterexamples():
    N,m=3,6
    spectra=[2,0,2,2,2,2]
    def local_list(values, replaced=None):
        return [local_coefficients(N,j,numerator_from_matrix(
            N,sigma,identity=(j==replaced))) for j,sigma in enumerate(values)]
    full=literal_source(N,local_list(spectra),None)
    north=literal_source(N,local_list(spectra,1),None)
    south=literal_source(N,local_list(spectra,2),None)
    assert (full,north,south)==(910845,115587,243)
    current=-2*full-2*north+4*south
    assert current == -2051892
    values=[-2,-2,-2,2,-2,-2]
    local=local_list(values)
    difference=literal_source(N,local,None)-literal_source(N,local,None,True)
    assert difference == 472392
    return {"N":3,"m":6,"full":full,"north_identity":north,
            "south_identity":south,"unshifted_current":current,
            "one_exception_difference":difference}


def shifted_target_checks():
    result=[]
    for N in (3,4):
        d=N-1
        p,q=finite_field(N,1009)
        spectra=[2,0,2,2,2,2]
        local=[local_coefficients(N,j,numerator_from_matrix(N,sigma,p,q))
               for j,sigma in enumerate(spectra)]
        target=[d]*6
        target[1]+=1
        target[2]-=1
        rim=[0]+target[1:]
        literal=literal_source(N,local,p,targets=target)
        enlarged=[transfer(N,j,h,p,u_max=2*d,rim_targets=rim)
                  for j,h in enumerate(local)]
        restricted=[transfer(N,j,h,p,rim_targets=rim)
                    for j,h in enumerate(local)]
        extended_value=transfer_trace(N,enlarged,p,u_max=2*d)
        assert extended_value==literal
        result.append({"N":N,"prime":p,"q":q,"targets_S_then_rim":target,
                       "direct_residue":literal,"enlarged_transfer_residue":extended_value,
                       "original_box_transfer_residue":transfer_trace(N,restricted,p)})
    return result


def run():
    started=time.time()
    cases=[]
    for N in range(2,6):
        for lower in (1009,5003):
            p,q=finite_field(N,lower)
            for spectra in ([2,0,2,2,2,2],[-2,1,-1,2,0,-2]):
                local=[local_coefficients(N,j,numerator_from_matrix(N,sigma,p,q))
                       for j,sigma in enumerate(spectra)]
                full=literal_source(N,local,p)
                cross=literal_source(N,local,p,True)
                Ts=[transfer(N,j,h,p) for j,h in enumerate(local)]
                Cs=[transfer(N,j,h,p,True) for j,h in enumerate(local)]
                assert transfer_trace(N,Ts,p)==full
                assert transfer_trace(N,Cs,p)==cross
                excursion,cross_mask=schur_coefficient(N,Ts,p)
                assert cross_mask==cross
                assert excursion==(full-cross)%p
                for j in range(6):
                    check_clocks(N,j,local[j],Ts[j],p,q)
                cases.append({"N":N,"m":6,"prime":p,"q":q,
                              "spectra":spectra,"full_residue":full,
                              "cross_residue":cross,"difference_residue":excursion})
    support=[support_longest_bad_path(N,m) for N in range(2,7) for m in (6,8)]
    return {
        "status":"passed",
        "scope":{
            "local_source":"Literal Casimir matrix powers with two independent outer variables.",
            "source_comparison":"Direct original-target monomial extraction versus full/CROSS transfer.",
            "schur":"Exact finite-field trace coefficient of the excursion formula.",
            "clock":"Independent incidence monomial phase versus diagonal clock formula.",
            "support":"Directed homogeneous-support DAG; no evaluated spectral cancellations.",
            "integer":"Original N=3 sewn-current and one-exception counterexamples retained.",
            "limitations":"Finite checks do not prove nilpotence for all levels, norm estimates, or a spectral gap."
        },
        "counts":{"finite_field_cases":len(cases),"local_clock_checks":6*len(cases),
                  "support_graphs":len(support),"integer_counterexamples":2,
                  "shifted_target_cases":2},
        "finite_field_cases":cases,"support_graphs":support,
        "shifted_target_checks":shifted_target_checks(),
        "integer_checks":integer_counterexamples(),
        "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "elapsed_seconds":round(time.time()-started,3)
    }


if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output",type=Path,
                        default=Path(__file__).with_name("md-shifted-cyclic-excursion-results.json"))
    args=parser.parse_args()
    result=run()
    args.output.write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({"status":result["status"],"counts":result["counts"],
                      "output":str(args.output),"elapsed_seconds":result["elapsed_seconds"]}))
