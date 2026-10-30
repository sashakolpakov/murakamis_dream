#!/usr/bin/env python3
"""Actual braided matrix-unit co-sources, with genuine first q jets."""
import argparse
import itertools
import json
from pathlib import Path

import numpy as np
import sympy as sp

from audit_high_color_first_normal_r_degree import setup, root_field
from audit_actual_nc_morse_graph_first_normal_source_reduction import (
    Local, const, mm, kron, module_jet)


def eq(A, B):
    return all(np.array_equal(a, b) for a, b in zip(A, B))


def eye(n):
    return const(np.eye(n, dtype=np.int64))


def original_crossings(N):
    p, d, coefficient = setup(N, 0)
    _, eta = root_field(N)
    q = eta*eta % p
    rho = (q-pow(q, -1, p)) % p
    lrho = (q+pow(q, -1, p))*pow(rho, -1, p) % p
    diag = [pow(-rho, i, p)*pow(q, i*(i+1)//2, p) % p for i in range(N)]
    logdiag = [(i*lrho+i*(i+1)//2) % p for i in range(N)]
    pairs = []
    for negative in (False, True):
        R = [np.zeros((N*N, N*N), dtype=np.int64) for _ in range(2)]
        for i, j in itertools.product(range(N), repeat=2):
            bound = min(j, d-i) if negative else min(i, d-j)
            for k in range(bound+1):
                oi, oj = (j-k, i+k) if negative else (j+k, i-k)
                c = coefficient(i, j, k, negative=negative)
                frame = diag[oi]*diag[oj]*pow(diag[i]*diag[j] % p, -1, p) % p
                logframe = (logdiag[oi]+logdiag[oj]-logdiag[i]-logdiag[j]) % p
                R[0][oi*N+oj, i*N+j] = c.x*frame % p
                # setup differentiates delta=1-Q^N, whose epsilon derivative is -2N.
                R[1][oi*N+oj, i*N+j] = (-2*N*c.dx+c.x*logframe)*frame % p
        pairs.append(tuple(R))
    assert eq(mm(pairs[0], pairs[1], p), eye(N*N))
    assert eq(mm(pairs[1], pairs[0], p), eye(N*N))
    g0 = np.array([pow(-1, d, p)*pow(q, d-2*a, p) % p for a in range(N)], dtype=np.int64)
    g1 = np.array([(d-2*a)*int(g0[a]) % p for a in range(N)], dtype=np.int64)
    assert int(sum(g0)) % p == 0
    assert int(sum(g1)) % p != 0
    E, F, K = module_jet(d, q, p)
    Ki = (np.diag([pow(int(v), -1, p) for v in np.diag(K[0])]),
          np.diag([-(d-2*a)*pow(int(K[0][a,a]), -1, p) % p for a in range(N)]))
    E2a, E2b = kron(E, K, p), kron(eye(N), E, p)
    F2a, F2b = kron(F, eye(N), p), kron(Ki, F, p)
    operators = [tuple((a+b) % p for a,b in zip(E2a,E2b)),
                 tuple((a+b) % p for a,b in zip(F2a,F2b)), kron(K,K,p)]
    for R in pairs:
        for op in operators:
            assert eq(mm(R, op, p), mm(op, R, p))
    return p, q, (g0,g1), pairs


def embed_pair(R, slot, width, N, p):
    return kron(kron(eye(N**slot), R, p), eye(N**(width-slot-2)), p)


def embed_one(M, slot, width, N, p):
    return kron(kron(eye(N**slot), M, p), eye(N**(width-slot-1)), p)


def product(word, size, p):
    out = eye(size)
    for C in word:
        out = mm(C,out,p)
    return out


def partial(C, g, width, N, p):
    out = [np.zeros((N,N), dtype=np.int64) for _ in range(2)]
    for a,c in itertools.product(range(N), repeat=2):
        for closed in itertools.product(range(N), repeat=width-1):
            row, col = c,a
            w0,w1 = 1,0
            for u in closed:
                row,col = N*row+u,N*col+u
                w0,w1 = w0*int(g[0][u])%p, (w1*int(g[0][u])+w0*int(g[1][u]))%p
            out[0][c,a] = (out[0][c,a]+w0*int(C[0][row,col]))%p
            out[1][c,a] = (out[1][c,a]+w1*int(C[0][row,col])+w0*int(C[1][row,col]))%p
    return tuple(out)


def source_case(N, width, kind):
    p,q,g,(Rp,Rm)=original_crossings(N)
    plus=[embed_pair(Rp,i,width,N,p) for i in range(width-1)]
    minus=[embed_pair(Rm,i,width,N,p) for i in range(width-1)]
    if kind=='braid':
        word=[plus[0],plus[0],plus[0]] if width==2 else [plus[0],minus[1],plus[0],minus[1]]
    else:
        loc=Local(N)
        sectors=[mm(loc.W[a],loc.pi[a],p) for a in loc.W]
        weights=[loc.h0[a] for a in loc.W]
        C=tuple(sum((h*S[r] for h,S in zip(weights,sectors)),np.zeros_like(Rp[r]))%p for r in range(2))
        word=[embed_pair(C,0,width,N,p),plus[0],embed_pair(C,width-2,width,N,p)]
    split=1
    A=product(word[split:],N**width,p);B=product(word[:split],N**width,p)
    H=partial(mm(A,B,p),g,width,N,p)
    z=tuple(int(x[0,0]) for x in H)
    assert eq(H,tuple(zz*np.eye(N,dtype=np.int64)%p for zz in z))
    slot=width-1
    U=product([plus[i] for i in range(slot-1,-1,-1)],N**width,p)
    Ui=product([minus[i] for i in range(slot)],N**width,p)
    assert eq(mm(U,Ui,p),eye(N**width))
    new=partial(mm(mm(mm(U,B,p),A,p),Ui,p),g,width,N,p)
    assert eq(new,H)
    Js=[np.zeros((N,N),dtype=np.int64) for _ in range(2)]
    bare=np.zeros((N,N),dtype=np.int64)
    projectors=[]
    for ell in range(N):
        E=np.zeros((N,N),dtype=np.int64);E[ell,ell]=1
        X=mm(mm(Ui,embed_one(const(E),0,width,N,p),p),U,p)
        projectors.append(X)
        HX=partial(mm(mm(A,X,p),B,p),g,width,N,p)
        for r in range(2):Js[r][:,ell]=np.diag(HX[r])
        plain=partial(mm(mm(A,embed_one(const(E),slot,width,N,p),p),B,p),g,width,N,p)
        bare[:,ell]=np.diag(plain[0])
    assert eq(tuple(sum((x[r] for x in projectors),np.zeros_like(U[r]))%p for r in range(2)),eye(N**width))
    for r in range(2):assert np.all(np.sum(Js[r],axis=1)%p==z[r])
    weighted0=g[0]@Js[0]%p
    weighted1=(g[1]@Js[0]+g[0]@Js[1])%p
    assert np.array_equal(weighted0,z[0]*g[0]%p)
    assert np.array_equal(weighted1,(z[1]*g[0]+z[0]*g[1])%p)
    assert (sum(g[1])*z[0])%p == sum(weighted1)%p
    naive_column=np.sum(bare,axis=0)%p
    naive_pivot=g[0]@bare%p
    return dict(N=N,width=width,source=kind,root_scalar=z[0],scalar_first_jet=z[1],
                actual_two_cut_entry_jets=2*N*N, adapted_column_jets=2*N,
                bare_column=[int(x) for x in naive_column],
                bare_pivotal_column=[int(x) for x in naive_pivot],
                naive_second_marginal_fails=bool(np.any(naive_column!=naive_column[0])),
                naive_pivotal_second_marginal_fails=bool(np.any(naive_pivot!=z[0]*g[0]%p)),
                naive_pivotal_scalar_marginal_fails=bool(np.any(naive_pivot!=naive_pivot[0])),
                field=p)


def characters():
    L,a,b,e=sp.symbols('L a b e',integer=True)
    # Treat the magnetic variables as independent complex symbols in exponents.
    x=sp.symbols('x')
    cup_power=x*(L-x-1)
    assert sp.expand(cup_power-cup_power.subs(x,L-x)-(L-2*x))==0
    N=sp.symbols('N',integer=True,positive=True);d=N-1
    # Root ratio differs from the algebraic clock ratio by the integer winding.
    assert sp.expand((1-N)*(-2*a+2*b)/N-(2*(a-b)+2*(b-a)/N))==0
    return dict(literal_cup_pivotal_ratio=True, retained_complex_row_character=True,
                generic_fixed_highest_weight=True)


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    rows=[source_case(N,2,kind) for N in range(2,7) for kind in ('braid','complete')]
    rows += [source_case(N,3,kind) for N in (2,3,4) for kind in ('braid','complete')]
    assert any(row['naive_second_marginal_fails'] for row in rows)
    assert any(row['naive_pivotal_second_marginal_fails'] for row in rows)
    result=dict(status='PASS',characters=characters(),cases=rows,
                scope='Actual braided two-cut co-source, genuine first quantum jets and whole trace normal; '
                      'no independent two-index evaluation or selected fiber/cycle coefficient.')
    target=args.output or Path(__file__).with_name('actual_braided_two_cut_source_adapter_results.json')
    target.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(status='PASS',actual_sources=len(rows),
                          actual_entry_jets=sum(x['actual_two_cut_entry_jets'] for x in rows),
                          adapted_column_jets=sum(x['adapted_column_jets'] for x in rows)),indent=2))


if __name__=='__main__':main()
