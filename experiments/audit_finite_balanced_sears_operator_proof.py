#!/usr/bin/env python3
"""Exact finite checks of the own polynomial-operator Sears proof."""
import itertools
import json
import random
from pathlib import Path

from audit_actual_two_cut_ports import balanced_data


def poch(a,n,v,p):
    out = 1
    for k in range(n):out = out*(1-a*pow(v,k,p)) % p
    return out


def hyper(n,nums,dens,v,p):
    total = 0
    for k in range(n+1):
        den = poch(v,k,v,p)
        for a in dens:den = den*poch(a,k,v,p) % p
        if not den:raise ZeroDivisionError
        num = pow(v,k,p)
        for a in nums:num = num*poch(a,k,v,p) % p
        total += num*pow(den,-1,p)
    return total % p


def sears(n,a,b,c,d,e,v,p):
    f = a*b*c*pow(v,1-n,p)*pow(d*e,-1,p) % p
    left = hyper(n,[pow(v,-n,p),a,b,c],[d,e,f],v,p)
    num = poch(e*pow(a,-1,p)%p,n,v,p)*poch(d*e*pow(b*c,-1,p)%p,n,v,p) % p
    den = poch(e,n,v,p)*poch(d*e*pow(a*b*c,-1,p)%p,n,v,p) % p
    if not den:raise ZeroDivisionError
    right = hyper(n,[pow(v,-n,p),a,d*pow(b,-1,p)%p,d*pow(c,-1,p)%p],
                  [d,a*pow(v,1-n,p)*pow(e,-1,p)%p,d*e*pow(b*c,-1,p)%p],v,p)
    assert left == num*pow(den,-1,p)*right % p
    return left


def operator_case(v,params,z,k,p):
    A,B,C,D = params
    P = A*B*C*D % p
    def M(r,t):return poch(A*t%p,r,v,p)*poch(A*pow(t,-1,p)%p,r,v,p) % p
    def u(t):
        den = (1-t*t)*(1-v*t*t) % p
        if not den:raise ZeroDivisionError
        num = 1
        for a in params:num = num*(1-a*t) % p
        return num*pow(den,-1,p) % p
    actual = (u(z)*(M(k,v*z%p)-M(k,z))
              +u(pow(z,-1,p))*(M(k,pow(v,-1,p)*z%p)-M(k,z))) % p
    lam = (pow(v,-k,p)-1)*(1-P*pow(v,k-1,p)) % p
    target = lam*M(k,z) % p
    if k:
        mu = 1-pow(v,-k,p)
        for a in (B,C,D):mu = mu*(1-A*a*pow(v,k-1,p)) % p
        target = (target+mu*M(k-1,z)) % p
    assert actual == target


def main():
    rng = random.Random(20261029)
    p,v = 1000003,7
    op_count = sears_count = 0
    for k in range(10):
        for _ in range(20):
            try:
                operator_case(v,[rng.randrange(2,p-1) for _ in range(4)],rng.randrange(2,p-1),k,p)
            except ZeroDivisionError:continue
            op_count += 1
    for n in range(11):
        for _ in range(30):
            try:sears(n,*[rng.randrange(2,p-1) for _ in range(5)],v,p)
            except ZeroDivisionError:continue
            sears_count += 1
    roots = []
    for N in range(2,17):
        pp,eta,q,*_ = balanced_data(N)
        Q,d,count = q*q % pp,N-1,0
        for aa,bb,cc in itertools.product(range(d//2+1),repeat=3):
            if aa<max(bb,cc) or aa>bb+cc or aa+bb+cc<d:continue
            n = bb+cc-aa
            sears(n,pow(Q,-bb,pp),pow(Q,aa+1,pp),pow(Q,-cc,pp),
                  pow(Q,-bb-cc,pp),pow(Q,aa-bb+1,pp),Q,pp)
            count += 1
        roots.append({'N':N,'all_supported_max_chart_root_series':count})
    out = {'status':'PASS','exact_operator_basis_actions':op_count,
           'exact_generic_balanced_Sears_families':sears_count,
           'exact_root_specializations':roots,
           'scope':'Own finite balanced Sears lemma and root parameter specialization; actual source coefficient-to-series identification is separate.'}
    Path(__file__).with_name('finite_balanced_sears_operator_proof_results.json').write_text(json.dumps(out,indent=2)+'\n')
    print(f'PASS {op_count} exact operator actions, {sears_count} generic balanced Sears identities, {len(roots)} full supported root families')


if __name__=='__main__':
    main()
