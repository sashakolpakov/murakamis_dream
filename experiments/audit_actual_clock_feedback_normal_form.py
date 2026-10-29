#!/usr/bin/env python3
"""Exact actual underclock feedback, independent beta atoms, and socle source."""
import itertools
import json
from pathlib import Path
import numpy as np

from audit_actual_hardy_cauchy_network import HardyNetwork
from audit_actual_global_charged_bridge_flow import (
    setup,segment_coordinates,charged_data,charged_coefficient,evaluate_forms)
from audit_actual_two_cut_ports import word_matrix,partial


def feedback_metadata(S):
    """No clock values enter: history and integer T are diagram data."""
    ports={};anchors=len(S['events'])
    for a,event in enumerate(S['events']):
        v=event['output'];signed=0;history=[]
        while True:
            assert v not in ports
            ports[v]={'anchor':a,'signed':signed,'history':history.copy()}
            if v not in S['under']:break
            v,j=S['under'][v];sig=S['records'][j]['sign']
            signed+=sig;history.append(j)
    assert set(ports)==S['expected']
    primitive={}
    for j,rec in enumerate(S['records']):
        ui=rec['invars'][1-rec['over_in']];data=ports[ui];sig=rec['sign']
        T={l:S['records'][l]['sign'] for l in data['history']}
        if sig<0:T[j]=T.get(j,0)-1
        assert all(l<=j for l in T)
        assert T.get(j,0)==-(1-sig)//2
        primitive[('a',j)]={'anchor':data['anchor'],'power':-1,
            'q':(1+sig)//2,'x':-data['signed'],'T':T}
    for v in sorted({w for event in S['events'] for w in (event['input'],event['output'])}):
        data=ports[v]
        primitive[('z',v)]={'anchor':data['anchor'],'power':1,
            'q':0,'x':data['signed'],
            'T':{l:-S['records'][l]['sign'] for l in data['history']}}
    return ports,primitive


def own_charged_data(H,S,clocks,feedback=True):
    N,p,Q,q,x,d=H.N,H.p,H.Q,H.q,H.x,H.N-1
    ports,primitive=feedback_metadata(S);k=len(S['events'])
    def mono(key):
        r=primitive[key];coef=pow(Q,r['q'],p)*pow(x,r['x'],p)%p
        if feedback:coef=coef*pow(Q,sum(t*clocks[j] for j,t in r['T'].items()),p)%p
        v=[0]*k;v[r['anchor']]=r['power'];return coef,tuple(v)
    def mul(a,b):return a[0]*b[0]%p,tuple(x+y for x,y in zip(a[1],b[1]))
    def inv(a):return pow(a[0],-1,p),tuple(-x for x in a[1])
    def scale(c,a):return c*a[0]%p,a[1]
    def ratio(a,b):return mul(a,inv(b))
    forms=[];weight=1;powers=[0]*k
    def linear(tail,head,z):
        v={tail:1};v[head]=(v.get(head,0)-z)%p
        return {a:b for a,b in v.items() if b}
    for event in S['events']:
        zin,zout=mono(('z',event['input'])),mono(('z',event['output']))
        ai=ports[event['input']]['anchor'];ao=ports[event['output']]['anchor']
        if event['kind']=='closure':
            eta,t=(1,1) if event['head']==0 else (x*pow(pow(x,N,p),-1,p)%p,pow(Q,-1,p))
            zz=ratio(zout,zin)
            for r in range(1,N):forms.append(linear(ai,ao,pow(Q,r,p)*t*zz[0]%p))
            powers[ai]-=d;weight=weight*eta%p
            continue
        path=event['path'];hs=[clocks[j] for j in path]
        assert all(a>=b for a,b in zip(hs,hs[1:]))
        aa=[mono(('a',j)) for j in path]
        au=[primitive[('a',j)]['anchor'] for j in path]
        ns=[d-hs[0]]+[a-b for a,b in zip(hs,hs[1:])]+[hs[-1]]
        z=[scale(Q*Q*x%p,inv(mul(aa[0],zin)))]
        z += [scale(pow(x,-1,p),ratio(a,b)) for a,b in zip(aa,aa[1:])]
        z += [mul(aa[-1],zout)]
        ts=[(1,(0,)*k)];w=0
        for r,(j,a) in enumerate(zip(path,aa),1):
            w+=S['records'][j]['sign']
            ts.append(scale((-1)**r*pow(q,2+w,p)%p,inv(mul(zin,a))))
        tails=[ai]+au;heads=au+[ao]
        weight=weight*N*pow(H.kappa,w,p)%p
        for n,zz,tt,tail,head in zip(ns,z,ts,tails,heads):
            expected=[0]*k;expected[head]+=1;expected[tail]-=1
            assert zz[1]==tuple(expected)
            for r in range(n):forms.append(linear(tail,head,pow(Q,r,p)*zz[0]%p))
            weight=weight*H.inv[n]*pow(tt[0],n,p)%p
            for a,power in enumerate(tt[1]):powers[a]+=n*power
            powers[tail]-=n
    assert powers==[-d]*k
    assert len(forms)==k*d
    return forms,weight,ports,primitive


def case(N,width,word):
    H=HardyNetwork(N,1);p,d=H.p,N-1;S=setup(H,width,word)
    ports,primitive=feedback_metadata(S);k=len(S['events'])
    total=naive=0;count=0;phase_checks=0
    for clocks in itertools.product(range(N),repeat=len(word)):
        if any(any(clocks[a]<clocks[b] for a,b in zip(path,path[1:])) for path in S['paths']):continue
        F,w,_,_=own_charged_data(H,S,clocks)
        oldF,oldw,mapping,_=charged_data(H,S,clocks)
        coef=charged_coefficient(F,k,d,p);oldcoef=charged_coefficient(oldF,k,d,p)
        assert w*coef%p==oldw*oldcoef%p
        # Entire polynomial, not merely a chosen local observable.
        vals=list(range(11,11+k))
        assert w*evaluate_forms(F,vals,p)%p==oldw*evaluate_forms(oldF,vals,p)%p
        # Original port transport and the new explicit a-row formula.
        for key,r in primitive.items():
            base=pow(H.Q,r['q'],p)*pow(H.x,r['x'],p)*pow(vals[r['anchor']],r['power'],p)%p
            new=base*pow(H.Q,sum(t*clocks[j] for j,t in r['T'].items()),p)%p
            if key[0]=='z':
                a,zeta,_=mapping[key[1]];old=zeta*vals[a]%p
            else:
                j=key[1];rec=S['records'][j];uo=rec['outvars'][1-rec['over_out']]
                a,zeta,_=mapping[uo];u=zeta*vals[a]%p
                alpha=pow(H.Q,-clocks[j],p)*pow(H.x,-1,p)%p if rec['sign']>0 else H.Q*H.x%p
                old=alpha*pow(u,-1,p)%p
            assert new==old
            phase_checks+=1
        total=(total+w*coef)%p
        NF,nw,_,_=own_charged_data(H,S,clocks,feedback=False)
        naive=(naive+nw*charged_coefficient(NF,k,d,p))%p
        count+=1
    core=total*pow(N,-1,p)%p;naive=naive*pow(N,-1,p)%p
    original=word_matrix(word,H.plus,H.minus,width,N,p)
    cut=partial(original,H.pivot,width,N,p)
    expected=int(cut.sum())*pow(N,-1,p)%p
    assert core==expected
    external=H.dimension*pow(H.twist,-sum(1 if j>0 else -1 for j in word),p)%p
    nonzero=[(key,j,t) for key,r in primitive.items() for j,t in r['T'].items() if t%N]
    assert nonzero
    key,j,t=nonzero[0]
    # G_T((Y_j-1)R_key)|Y1 !=0 although the original Y1 restriction is0.
    assert (pow(H.Q,t,p)-1)%p
    return {'N':N,'width':width,'word':word,'clock_assignments':count,
            'primitive_variables':len(primitive),'anchors':k,'exact_feedback_rows_checked':phase_checks,
            'feedback_original_scalar':core,'original_matrix_scalar':expected,
            'naively_evaluated_independent_scalar':naive,'naive_feedback_omission_changes_source':naive!=core,
            'full_original_dimension_framing_Cartan_normalization':external*core%p,
            'fugacity_evaluation_kernel_not_preserved':True,
            'metadata':[{'name':str(key),**r} for key,r in primitive.items()]}


def finite_Fourier_identity():
    rows=[]
    for N in range(2,10):
        H=HardyNetwork(N,1);p,Q=H.p,H.Q
        # Independent exact Fourier delta for a nontrivial feedback matrix.
        T=[[0,1],[-1,-1],[1,0]]
        for nu in ((1,-2,3),(N+1,-1,2)):
            for hh in itertools.product(range(N),repeat=2):
                lhs=pow(Q,sum(n*T[i][j]*hh[j] for i,n in enumerate(nu) for j in range(2)),p)
                rhs=0
                for eta in itertools.product(range(N),repeat=2):
                    for lam in itertools.product(range(N),repeat=2):
                        expn=sum(lam[j]*(hh[j]-eta[j]) for j in range(2))
                        expn+=sum(n*T[i][j]*eta[j] for i,n in enumerate(nu) for j in range(2))
                        rhs=(rhs+pow(Q,expn,p))%p
                rhs=rhs*pow(N,-2,p)%p
                assert lhs==rhs
        rows.append({'N':N,'exact_normalized_feedback_Fourier_delta':True})
    return rows


def twisted_bridge_telescope():
    """Actual finite binomial ratio with EVERY charge fugacity retained."""
    rows=[]
    for N in range(2,10):
        H=HardyNetwork(N,1);p,Q,d=H.p,H.Q,N-1
        def prod(a,b):
            out=[0]*N
            for i,x in enumerate(a):
                for j,y in enumerate(b[:N-i]):out[i+j]=(out[i+j]+x*y)%p
            return out
        def inverse(a):
            out=[pow(a[0],-1,p)]+[0]*d
            for i in range(1,N):out[i]=-sum(a[j]*out[i-j] for j in range(1,i+1))*out[0]%p
            return out
        def poch(w,n):
            out=[1]+[0]*d
            for j in range(n):out=prod(out,[1,-w*pow(Q,j,p)%p]+[0]*(N-2))
            return out
        def U(z,t):
            out=[];zz=1
            for n in range(N):
                out.append(zz*H.inv[n]*pow(t,n,p)%p)
                zz=zz*(1-z*pow(Q,n,p))%p
            return out
        count=0
        for signs in ((1,),(1,-1),(-1,1,-1),(1,1,-1,1)):
            m=len(signs);ts=[1]+list(range(11,11+m));end=29
            zs=[pow(Q,(1-signs[r])//2,p)*ts[r+1]*pow(ts[r],-1,p)%p for r in range(m)]
            zs.append(end*pow(ts[-1],-1,p)%p)
            for lambdas in (tuple([0]*m),tuple([(j+1)%N for j in range(m)]),tuple([d]*m)):
                pref=[1]
                for lam in lambdas:pref.append(pref[-1]*pow(Q,lam,p)%p)
                lhs=[1]+[0]*d
                for z,t,y in zip(zs,ts,pref):lhs=prod(lhs,U(z,t*y%p))
                rhs=U(end*pref[-1]%p,1)
                for r,(sig,lam) in enumerate(zip(signs,lambdas),1):
                    w=ts[r]*pref[r-1]%p
                    rhs=prod(rhs,prod(poch(w,lam),inverse(poch(w,(1-sig)//2))))
                assert lhs==rhs
                count+=1
        rows.append({'N':N,'full_fugacity_bridge_telescope_cases':count})
    return rows


def main():
    cases=[case(N,w,word) for N,w,word in
        [(2,3,[1,-2,1,-2]),(3,3,[1,-2,1,-2]),
         (2,3,[1,1,1,2,-1,2]),(3,3,[1,2,-1]),(3,3,[-1,-2,1])]]
    assert any(c['naive_feedback_omission_changes_source'] for c in cases)
    out={'actual_whole_source_feedback_cases':cases,'finite_Fourier_feedback_kernel':finite_Fourier_identity(),
         'twisted_bridge_charge_elimination':twisted_bridge_telescope(),
         'scope':'exact all-word feedback normal form with original socle source; '
                 'independent-parameter telescoping cannot precede feedback; no volume lower bound'}
    Path(__file__).with_name('audit_actual_clock_feedback_normal_form_results.json').write_text(json.dumps(out,indent=2)+'\n')
    print('PASS five ORIGINAL whole feedback/socle source states, all primitive clock histories, '
          'eight normalized Fourier feedback kernels; 96 full-fugacity bridge telescopes; '
          'naive independent telescoping changes actual source')


if __name__=='__main__':main()
