#!/usr/bin/env python3
"""Exact block phase gauge and quantitative unbalanced positive capacity.

The synthetic triangle tests a proved charged block theorem, not a knot
realization. Original knot metadata is tested separately for its failure
to satisfy the hypothesis; no curved sector is erased.
"""
import itertools,json,math
from pathlib import Path
import numpy as np
import mpmath as mp

from audit_actual_hardy_cauchy_network import HardyNetwork
from audit_actual_global_charged_bridge_flow import setup,graph_blocks


def positive_binomial(N,L):
    c=[mp.mpf(1)]
    for j in range(L):
        c.append(c[-1]*mp.sin(mp.pi*(L-j)/N)/mp.sin(mp.pi*(j+1)/N))
    return c


def flat_potentials(k,edges,modulus):
    eta={0:0};todo=[0]
    for u in todo:
        for a,b,w in edges:
            if a==u:v=b;pred=(eta[u]+w)%modulus
            elif b==u:v=a;pred=(eta[u]-w)%modulus
            else:continue
            if v in eta and eta[v]!=pred:return None
            if v not in eta:eta[v]=pred;todo.append(v)
    return eta if len(eta)==k else None


def triangle_case(r):
    N=4*r+1;k=3;lengths=[3*r,2*r,2*r];target=(2*r,3*r,2*r)
    endpoints=[(0,1),(1,2),(2,0)];q=mp.exp(mp.pi*1j/N);Q=q*q
    eta_exponents=[0,3,-2]
    cs=[positive_binomial(N,L) for L in lengths]
    # Exact source cut inequalities, with nonzero macroscopic defect.
    for mask in range(1,2**k-1):
        I={i for i in range(k) if mask>>i&1}
        inner=sum(L for (u,v),L in zip(endpoints,lengths) if u in I and v in I)
        cut=sum(L for (u,v),L in zip(endpoints,lengths) if (u in I)!=(v in I))
        assert 0<sum(target[i] for i in I)-inner<cut
    incident=[sum(L for (u,v),L in zip(endpoints,lengths) if i in (u,v)) for i in range(k)]
    assert any(incident[i]!=2*target[i] for i in range(k))
    # Actual root-Pochhammer product, preserving its complete unit phase.
    terms={(0,0,0):mp.mpc(1)}
    positive={(0,0,0):mp.mpf(1)}
    edges=[]
    for (u,v),L,c in zip(endpoints,lengths,cs):
        wexp=(eta_exponents[v]-eta_exponents[u])%(2*N)
        edges.append((u,v,wexp))
        beta=-q**(wexp-(L-1))
        actual=[mp.mpc(1)]
        for a in range(L):
            nxt=[mp.mpc(0)]*(len(actual)+1)
            for j,z in enumerate(actual):
                nxt[j]+=z;nxt[j+1]-=z*beta*Q**a
            actual=nxt
        assert max(abs(actual[j]-c[j]*q**(wexp*j)) for j in range(L+1))<mp.mpf('1e-60')
        def expand(P,coeff):
            out={}
            for powers,z in P.items():
                for j,cj in enumerate(coeff):
                    e=list(powers);e[u]+=L-j;e[v]+=j;e=tuple(e)
                    out[e]=out.get(e,0)+z*cj
            return out
        terms=expand(terms,actual);positive=expand(positive,c)
    assert flat_potentials(k,edges,2*N) is not None
    common=sum(eta_exponents[i]*target[i] for i in range(k))
    common-=sum(eta_exponents[u]*L for (u,v),L in zip(endpoints,lengths))
    original=terms[target];selected=positive[target]
    assert abs(original-q**common*selected)<mp.mpf('1e-53')*selected

    # Unique positive critical radii; the equations are derived from the
    # same block distributions rather than a guessed source scalar.
    def moments(a,b,need_hessian=False):
        rho=[a,b,mp.mpf(0)];g=mp.mpf(0);grad=[-mp.mpf(t) for t in target]
        for (u,v),L,c in zip(endpoints,lengths,cs):
            weights=[c[j]*mp.exp((L-j)*rho[u]+j*rho[v]) for j in range(L+1)]
            Z=sum(weights);mean=sum(j*weights[j] for j in range(L+1))/Z
            grad[u]+=L-mean;grad[v]+=mean;g+=mp.log(Z)
        return g-sum(target[i]*rho[i] for i in range(k)),grad
    sol=mp.findroot(lambda a,b:tuple(moments(a,b)[1][:2]),(mp.mpf(0),mp.mpf(0)),tol=mp.mpf('1e-65'))
    g,grad=moments(sol[0],sol[1]);capacity=mp.exp(g)
    assert max(abs(x) for x in grad)<mp.mpf('1e-60')
    probability=selected/capacity;bound=mp.mpf(1)/math.prod(L+1 for L in lengths)
    assert bound<=probability<=1
    # Directly check the exact whole flow probability, not only inequality.
    rho=[sol[0],sol[1],mp.mpf(0)];probs=[]
    for (u,v),L,c in zip(endpoints,lengths,cs):
        a=[c[j]*mp.exp((L-j)*rho[u]+j*rho[v]) for j in range(L+1)];Z=sum(a)
        probs.append([x/Z for x in a])
    event=mp.mpf(0)
    for j0 in range(lengths[0]+1):
        j1=j0-r;j2=j1
        if 0<=j1<=lengths[1] and 0<=j2<=lengths[2]:
            event+=probs[0][j0]*probs[1][j1]*probs[2][j2]
    assert abs(event-probability)<mp.mpf('1e-60')
    return {'N':N,'lengths':lengths,'source_charges':target,'unbalanced':True,
            'radii':[float(mp.exp(x)) for x in rho],
            'source_over_capacity':float(probability),'proved_lower_factor':float(bound),
            'whole_complex_phase_preserved':True,'not_claimed_as_knot_realization':True}


def actual_curved_source():
    rows=[]
    for N in (3,5,7,9):
        H=HardyNetwork(N,1);r=(N-1)//2
        S=setup(H,3,[1,-2,1,1,-2,-2]);G=graph_blocks(H,S,[0,r,r,r,0,r])
        E=G['blocks'];edges=[(b['tail'],b['head'],b['w_exp']) for b in E]
        assert flat_potentials(G['anchor_count'],edges,2*N) is None
        phase=(E[2]['w_exp']+E[4]['w_exp']+E[6]['w_exp']-E[7]['w_exp'])%(2*N)
        assert phase==r
        rows.append({'N':N,'original_six_three_sector':[0,r,r,r,0,r],
                     'nonflat_actual_bulk_cycle_retained':True,'phase_exponent':phase})
    return rows


def main():
    mp.mp.dps=85
    result={'status':'PASS','unbalanced_strict_block_capacity':[triangle_case(r) for r in range(1,7)],
            'actual_knot_scope_checks':actual_curved_source(),
            'scope':'Exact conditional block-phase theorem, original normalizers unchanged. No uniform actual-knot clock-flatness or volume theorem claimed.'}
    Path(__file__).with_name('actual_flat_block_sublevel_transport_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS six unbalanced root-block source/capacity cases and four retained original curved sectors')


if __name__=='__main__':main()
