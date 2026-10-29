#!/usr/bin/env python3
"""Exact finite-field checks of divided factorial fusion and marked-edge rows.

The all-level theorems are proved in the notes. These diagnostics compare
q-binomial formulas with independent normal derivatives and test complete
matrix identities, including every matrix-unit cut row at the tested levels.
"""

import json
from pathlib import Path

import numpy as np
import sympy as sp


def field(n):
    m = max(2, 1000 // (2*n))
    while not sp.isprime(2*n*m + 1):
        m += 1
    p = int(2*n*m + 1)
    q = pow(int(sp.primitive_root(p)), (p-1)//(2*n), p)
    assert pow(q, n, p) == p-1
    return p, q


def mm(a, b, p):
    return a @ b % p


def ident(d):
    return np.eye(d, dtype=np.int64)


def powers(a, n, p):
    out = [ident(len(a))]
    for _ in range(n):
        out.append(mm(out[-1], a, p))
    return out


def eq(a, b, p):
    assert not np.any((a-b) % p)


def factorials(q2, n, p):
    out = [1]
    for j in range(1, n):
        out.append(out[-1] * (1-pow(q2, j, p)) % p)
    return out


def color(n, p, q):
    q2 = q*q % p
    e = np.zeros((n, n), dtype=np.int64)
    ed = e.copy()
    f = e.copy()
    kval = []
    kdval = []
    for a in range(n):
        kval.append(pow(q, n-1-2*a, p))
        kdval.append((n-1-2*a)*pow(q, n-2-2*a, p) % p)
        if a:
            e[a-1, a] = (pow(q2, -a, p)-1) % p
            ed[a-1, a] = (n+(n-2*a)*pow(q2, -a, p))*pow(q, -1, p) % p
        if a+1 < n:
            f[a+1, a] = (1-pow(q2, a+1, p)) % p
    return e, np.diag(kval), ed, np.diag(kdval), f


def tensor_color(e, k, ed, kd, b, p):
    c, ct, kt = e, ed, k
    for _ in range(1, b):
        d = len(c)
        ct = (np.kron(ct, k)+np.kron(c, kd)+np.kron(ident(d), ed)) % p
        c = (np.kron(c, k)+np.kron(ident(d), e)) % p
        kt = np.kron(kt, k) % p
    return c, kt, ct


def divided_derivative(c, cd, n, p, q):
    cp = powers(c, n, p)
    eq(cp[n], np.zeros_like(c), p)
    derivative = np.zeros_like(c)
    for j in range(n):
        derivative = (derivative+mm(mm(cp[j], cd, p), cp[n-1-j], p)) % p
    delta_derivative = -2*n*pow(q, -1, p) % p
    return derivative * pow(delta_derivative, -1, p) % p


def ppoly(a, n, fac, p, scale=1):
    ap = powers(a, n-1, p)
    out = np.zeros_like(a)
    for j in range(n):
        out = (out+ap[j]*(pow(scale, j, p)*pow(fac[j], -1, p) % p)) % p
    return out


def expnil(a, bound, p, scale=1):
    out = ident(len(a))
    term = out.copy()
    coefficient = 1
    for j in range(1, bound):
        term = mm(term, a, p)
        coefficient = coefficient*scale*pow(j, -1, p) % p
        out = (out+coefficient*term) % p
    eq(mm(term, a, p), np.zeros_like(a), p)
    return out


def adjoint_divided(t, e, k, jnorm, n, fac, p):
    kp_inv = [ident(len(k))]
    kinv = np.diag([pow(int(k[a,a]), -1, p) for a in range(len(k))])
    for _ in range(n):
        kp_inv.append(mm(kp_inv[-1], kinv, p))
    ep = powers(e, n-1, p)
    rp = powers(mm(e, kinv, p), n-1, p)
    out = mm(mm(jnorm, t, p)-mm(t, jnorm, p), kp_inv[n], p)
    for j in range(1, n):
        l = n-j
        coefficient = n*pow(fac[j]*fac[l] % p, -1, p)*pow(-1, l, p) % p
        term = mm(mm(mm(ep[j], t, p), kp_inv[j], p), rp[l], p)
        out = (out+coefficient*term) % p
    return out


def partial_trace(t, g, n, p):
    out = np.zeros((n,n), dtype=np.int64)
    for a in range(n):
        out = (out+int(g[a,a])*t[a::n,a::n]) % p
    return out


def ward_h(x, z, k, f, n, p):
    out = np.zeros_like(x)
    for a in range(n):
        for b in range(n):
            if a != b:
                out[a,b] = int(x[a,b])*pow(int(k[a,a]-k[b,b]) % p,-1,p) % p
    d = [int(z[r+1,r])*pow(int(f[r+1,r]),-1,p) % p for r in range(n-1)]
    mean = sum((n-1-r)*d[r] for r in range(n-1))*pow(n,-1,p) % p
    for a in range(n):
        out[a,a] = (mean-sum(d[:a])) % p
    return out


def main():
    records = []
    coherence = []
    for n in range(2,9):
        p,q = field(n)
        q2 = q*q % p
        fac = factorials(q2,n,p)
        e,k,ed,kd,f = color(n,p,q)
        a,b = np.kron(e,k)%p, np.kron(ident(n),e)%p
        c,kt,cd = tensor_color(e,k,ed,kd,2,p)
        jp = np.zeros_like(c)
        ap,bp = powers(a,n-1,p),powers(b,n-1,p)
        for j in range(1,n):
            coef = n*pow(fac[j]*fac[n-j]%p,-1,p)%p
            jp = (jp+coef*mm(bp[n-j],ap[j],p))%p
        eq(jp,divided_derivative(c,cd,n,p,q),p)
        eq(mm(jp,jp,p),np.zeros_like(c),p)
        eq(mm(jp,c,p),mm(c,jp,p),p)
        target = np.zeros(n*n,dtype=np.int64)
        target[0] = -n*q % p
        eq(jp[:,(n-1)*n+1],target,p)
        for scale in (1,-3):
            lhs = mm(ppoly(b,n,fac,p,scale),ppoly(a,n,fac,p,scale),p)
            rhs = mm((ident(n*n)+pow(scale,n,p)*pow(n,-1,p)*jp)%p,
                     ppoly(c,n,fac,p,scale),p)
            eq(lhs,rhs,p)
        w = np.zeros((n,n),dtype=np.int64)
        w[n-1,0] = 1
        zero = np.zeros_like(e)
        aa = lambda t: adjoint_divided(t,e,k,zero,n,fac,p)
        u = np.zeros_like(e)
        for l in range(1,n): u[l-1,l] = 1
        eq(aa(w),-n*u,p)
        phi = lambda t: int(t.sum())*pow(n,-1,p)%p
        phid = lambda t: -phi(aa(mm(t,w,p)))*pow(n-1,-1,p)%p
        assert phid(ident(n)) == 1
        for xidx in range(n*n):
            t = np.zeros_like(e)
            t[xidx//n,xidx%n] = 1
            eq(aa(aa(t)),zero,p)
            x = mm(k,t,p)-mm(t,k,p)
            z = mm(f,t,p)-mm(t,f,p)
            ht = ward_h(x,z,k,f,n,p)
            assert (phid(t)-phi(t)-phid(ht)+phi(ht))%p == 0
        g = np.diag([pow(int(k[s,s]),1-n,p) for s in range(n)])
        for seed in range(3):
            t = np.fromfunction(lambda i,j:(i+1)*(j+seed+2)+(i==j)*(seed+3),
                                (n*n,n*n),dtype=int).astype(np.int64)%p
            left = partial_trace(adjoint_divided(t,c,kt,jp,n,fac,p),g,n,p)
            right = aa(partial_trace(t,g,n,p))
            eq(left,right,p)
            direct = phid(partial_trace(t,g,n,p))
            inserted = mm(t,np.kron(w,ident(n))%p,p)
            lifted = partial_trace(adjoint_divided(inserted,c,kt,jp,n,fac,p),g,n,p)
            assert (direct+phi(lifted)*pow(n-1,-1,p))%p == 0
        records.append({'level':n,'prime':p,'two_factor_fusion_and_normal_derivative':True,
                        'explicit_divided_entries':True,'marked_row_matrix_units':n*n,
                        'divided_adjoint_pivotal_chain_map':3})
        if n <= 5:
            c3,k3,cd3 = tensor_color(e,k,ed,kd,3,p)
            j3 = divided_derivative(c3,cd3,n,p,q)
            chi = pow(-1,n-1,p)
            jl = np.kron(jp,ident(n))*chi%p
            jr = np.kron(ident(n),jp)%p
            lm,rm = (j3-jl)%p,(j3-jr)%p
            eq(mm(jl,lm,p),mm(lm,jl,p),p)
            eq(mm(jr,rm,p),mm(rm,jr,p),p)
            invn=pow(n,-1,p)
            left=mm(expnil(jl,3,p,invn),expnil(lm,3,p,invn),p)
            right=mm(expnil(jr,3,p,invn),expnil(rm,3,p,invn),p)
            eq(left,right,p)
            eq(left,expnil(j3,3,p,invn),p)
            coherence.append({'level':n,'even_level_character_retained':int(chi),
                              'three_factor_associativity':True})
    result={'two_factor_and_marked_cut':records,'fusion_coherence':coherence,
            'scope':'Exact diagnostics; no selected geometric-source or volume claim.'}
    out=Path(__file__).with_name('divided_ward_factorial_fusion_results.json')
    out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'levels':len(records),'marked_matrix_units':sum(x['marked_row_matrix_units'] for x in records),
                      'associativity_levels':len(coherence),'output':str(out)},indent=2))


if __name__ == '__main__':
    main()
