#!/usr/bin/env python3
"""All actual auxiliary colors via explicit generic Clebsch normal columns."""
import json
from pathlib import Path

import numpy as np

from audit_actual_two_cut_ports import balanced_data, coproduct
from audit_actual_complete_casimir_hermite_packet import canonical_field_frame


def level(N):
    p,eta,q,E,F,K,pivot,Rp,Rm=balanced_data(N)
    d=N-1;Q=q*q%p;x=pow(q,d,p);imag=pow(eta,N,p)
    rho=(q-pow(q,-1,p))%p
    Et,Ft,Kt=coproduct(rho*rho*E%p,F,K,2,N,p)
    Ki=np.diag([pow(int(z),-1,p) for z in np.diag(Kt)])
    O=(Ft@Et+q*Kt+pow(q,-1,p)*Ki)%p
    sf=[1];logF=[0]
    for n in range(1,N):
        sf.append(sf[-1]*(pow(q,n,p)-pow(q,-n,p))*pow(imag,-1,p)%p)
        logF.append((logF[-1]-2*n*pow(Q,n,p)*pow(1-pow(Q,n,p),-1,p))%p)
    def beta(n,r):return sf[n]*pow(sf[r]*sf[n-r]%p,-1,p)%p
    def dbeta(n,r):return (logF[n]-logF[r]-logF[n-r])%p
    def column(t,j,u):
        value=0;derivative=0
        for a in range(max(0,u-t+j),min(j,u)+1):
            weight=beta(j,a)*beta(u,a)*beta(t-u,j-a)*pow(beta(t,j),-1,p)%p
            term=pow(-1,u+a,p)*pow(q,a*(t+j+1)-(j+1)*u,p)*weight%p
            gamma=(d*(u-2*a)+2*a*(t-u)+a*(a-1)
                   +logF[N-j+a-1]-logF[N-j-1]+logF[N-a-1]-logF[N-1]
                   +dbeta(u,a)+dbeta(t-u,j-a)-dbeta(t,j))%p
            value=(value+term)%p;derivative=(derivative+term*gamma)%p
        return value,derivative
    # Independent actual circle polynomials and their derivatives as scalar lists.
    def color_values(c):
        vals=[1];ders=[0]
        if N>1:vals.append(c);ders.append(1)
        for n in range(2,N):
            vals.append((c*vals[-1]-vals[-2])%p)
            ders.append((vals[-2]+c*ders[-1]-ders[-2])%p)
        return [(pow(-1,n,p)*vals[n]%p,pow(-1,n,p)*ders[n]%p) for n in range(N)]
    original=[np.eye(N*N,dtype=np.int64)]
    if N>1:original.append(-O%p)
    for n in range(2,N):original.append((-O@original[-1]-original[-2])%p)
    compiled=[np.zeros_like(O) for _ in range(N)]
    signed_minus=[np.zeros_like(O) for _ in range(N)]
    signed_plus=[np.zeros_like(O) for _ in range(N)]
    kappa=int(Rp[0,0]);normals=values=blocks=0
    for S in range(2*d+1):
        t=min(S,2*d-S);shift=max(0,S-d)
        ids=[(shift+u)*N+S-shift-u for u in range(t+1)]
        block=O[np.ix_(ids,ids)]
        V,_,meta,_=canonical_field_frame(block,N,t,p,q)
        nodes=[(pow(q,2*j+1,p)+pow(q,-2*j-1,p))%p for j in range(t+1)]
        groups={}
        for j,c in enumerate(nodes):groups.setdefault(c,[]).append(j)
        for c,channels in groups.items():
            j=channels[0];data=[column(t,j,u) for u in range(t+1)]
            v=np.array([row[0] for row in data],dtype=np.int64)
            index=meta.index((j,'value'))
            assert np.array_equal(v,V[:,index]);values+=len(v)
            nu=pow(-1,j,p)*pow(q,j*(j+1),p)%p
            other=[nodes[k] for k in range(t+1) if k not in channels]
            quotient=1
            for node in other:quotient=quotient*(c-node)%p
            B=pow(-1,t,p)*sf[t]**2%p
            sigma=pow(x,t,p)*nu*quotient*pow(B,-1,p)%p
            if len(channels)==2:
                partner=channels[1]
                assert partner==d-j
                gap=-2*N*(pow(q,2*j+1,p)-pow(q,-2*j-1,p))%p
                w=np.array([(data[u][1]-column(t,partner,u)[1])*pow(gap,-1,p)%p
                            for u in range(t+1)],dtype=np.int64)
                assert np.array_equal(w,V[:,index+1]);normals+=len(w)
                rlog=-(d-2*j)*pow(2*(pow(q,2*j+1,p)-pow(q,-2*j-1,p)),-1,p)%p
                etaj=(rlog+sum(pow(c-node,-1,p) for node in other))%p
            for color,(lc,ld) in enumerate(color_values(c)):
                for eps,target in ((0,compiled),(-1,signed_minus),(1,signed_plus)):
                    phase=pow(kappa,eps,p)*pow(nu,eps,p)%p
                    if len(channels)==1:
                        term=phase*lc*np.outer(v,v)%p*pow(sigma,-1,p)%p
                    else:
                        constant=(ld+(eps*rlog-etaj)*lc)%p
                        term=(constant*np.outer(v,v)%p+lc*(np.outer(v,w)+np.outer(w,v))%p)%p
                        term=phase*term%p*pow(sigma,-1,p)%p
                    target[color][np.ix_(ids,ids)]=(target[color][np.ix_(ids,ids)]+term)%p
        blocks+=1
    for color in range(N):
        assert np.array_equal(compiled[color],original[color])
        assert np.array_equal(signed_plus[color],Rp@original[color]%p)
        assert np.array_equal(signed_minus[color],Rm@original[color]%p)
    return dict(N=N,physical_blocks=blocks,canonical_value_entries=values,
                generic_confluent_normal_entries=normals,full_mixed_signed_operator_identities=3*N)


def main():
    result=dict(status='PASS',levels=[level(N) for N in range(2,13)],
                scope='All actual root-level auxiliary colors and signed kernels, including simple and double Casimir blocks. No uniform complex color packet or coherent gap is inferred.')
    Path(__file__).with_name('actual_mixed_augmented_plat_compiler_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(status='PASS',levels=len(result['levels']),
                         physical_blocks=sum(r['physical_blocks'] for r in result['levels']),
                         value_entries=sum(r['canonical_value_entries'] for r in result['levels']),
                         normal_entries=sum(r['generic_confluent_normal_entries'] for r in result['levels']),
                         mixed_signed_identities=sum(r['full_mixed_signed_operator_identities'] for r in result['levels'])),indent=2))


if __name__=='__main__':main()
