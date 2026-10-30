#!/usr/bin/env python3
"""Exact original paired phases and centered shared-cycle convolutions."""
import itertools
import json
from pathlib import Path

from audit_actual_matching_graph_positive_fourier_partition import data, graph
from audit_actual_matching_graph_shared_cycle_fourier_compiler import convolution
from audit_actual_two_cut_ports import balanced_data


def endpoint_phases():
    count=0
    for N in range(2,18):
        p,eta,q,*_=balanced_data(N);D=data(N,q,pow(eta,N,p),p,eta);d=N-1;s=D['sf']
        for a,cols in D['W'].items():
            for r,col in enumerate(cols):
                w=abs(r-a);t=d-w;T=d-a+r;b=max(0,T-d);index=b*N+T-b
                ct=pow(q,a*(t+a-d),p)*pow(D['fac'][a],-1,p)%p
                actual=D['h0'][a]*col[index]*D['pi'][a][r][index]*ct*ct%p
                ka=1 if 2*a==d else 2
                scalar=ka*N*s[a+w]*pow(s[a]**2*s[w]**2*s[a-w],-1,p)%p
                assert actual==scalar*pow(q,(2*a-d)*t,p)%p
                count+=1
    return count


def cycle_phases(N,width,all_states=True):
    p,eta,q,*_=balanced_data(N);D=data(N,q,pow(eta,N,p),p,eta);d=N-1;s=D['sf']
    assert eta*eta%p==q
    nodes,cycles,boxes=graph(width);R=len(boxes)
    labels=[(a,w) for a in D['W'] for w in range(-a,a+1)]
    states=itertools.product(labels,repeat=R) if all_states else (
        tuple(((i+shift)%(d//2+1),0) for i in range(R)) for shift in range(d//2+1))
    counts=dict(flow_states=0,cycle_coefficients=0,marked_coefficients=0,
                full_scalar_cancellations=0,integer_phase_checks=0,base_shift_checks=0)
    for lab in states:
        defects=[sum((1 if nodes[v][0]=='W' else -1)*lab[nodes[v][1]][1]
                     for v,_ in order if nodes[v][0] in ('W','pi')) for order in cycles]
        if any(defects):continue
        counts['flow_states']+=1;constant=1;actual_marked=centered_marked=1;parity=0
        for ci,order in enumerate(cycles):
            actual=[1]+[0]*(2*N-1);centered=[1]+[0]*(2*N-1);translated=[1]+[0]*(2*N-1)
            eps,shift=1,0;local_constant=1
            for v,entry in order:
                kind,i=nodes[v];T=d+(lab[i][1] if i is not None else 0)
                se=eps if entry==0 else -eps;sb=shift if entry==0 else T-shift
                twice_delta=2*sb-T
                aa=[0]*(2*N);cc=[0]*(2*N);dd=[0]*(2*N)
                if i is not None:
                    a,w=lab[i];r=a+w;t=d-abs(w);b=max(0,w)
                    src=D['W'][a][r] if kind=='W' else D['pi'][a][r]
                    cv=src[b*N+T-b];ct=pow(q,a*(t+a-d),p)*pow(D['fac'][a],-1,p)%p
                    local_constant=local_constant*cv*ct*pow(eta,(d-2*a)*t,p)%p
                    for h,pc in enumerate(D['polys'][t,a]):
                        gamma=d-2*a+2*h;index=gamma*se%(2*N)
                        aa[index]=(aa[index]+cv*ct*pc*pow(q,gamma*(sb-b)-t*h,p))%p
                        cc[index]=(cc[index]+pc*pow(eta,gamma*twice_delta,p))%p
                        dd[index]=(dd[index]+pc*pow(eta,gamma*(twice_delta+2*se),p))%p
                    parity+=d*T
                else:
                    scale=N*pow(q,-d*d,p)%p if kind=='cup' else pow(N,-1,p)
                    local_constant=local_constant*scale*pow(eta,d*d,p)%p
                    aa[d*se%(2*N)]=scale*pow(q,d*sb,p)%p
                    cc[d*se%(2*N)]=pow(eta,d*twice_delta,p)
                    dd[d*se%(2*N)]=pow(eta,d*(twice_delta+2*se),p)
                    parity+=d*d
                actual=convolution(actual,aa,p);centered=convolution(centered,cc,p)
                translated=convolution(translated,dd,p)
                eps,shift=-eps,T-shift
            assert eps==1 and shift==0
            assert all(actual[h]==local_constant*centered[h]%p for h in range(2*N))
            assert all(translated[h]==pow(q,h,p)*centered[h]%p for h in range(2*N))
            assert all(actual[h]==centered[h]==0 for h in range(1,2*N,2))
            counts['cycle_coefficients']+=2*N
            if ci:
                # A unit integer base-coordinate translation is immaterial at charge zero.
                assert centered[0]==translated[0]
                counts['base_shift_checks']+=1
            charge=1 if ci==0 else 0
            actual_marked=actual_marked*actual[2*charge]%p
            centered_marked=centered_marked*centered[2*charge]%p
            constant=constant*local_constant%p
        assert parity%2==0
        counts['integer_phase_checks']+=1
        hprod=scalar=1
        for a,w in lab:
            hprod=hprod*D['h0'][a]%p;w=abs(w);ka=1 if 2*a==d else 2
            scalar=scalar*ka*N*s[a+w]*pow(s[a]**2*s[w]**2*s[a-w],-1,p)%p
        assert hprod*constant%p==scalar
        assert hprod*actual_marked%p==scalar*centered_marked%p
        counts['full_scalar_cancellations']+=1;counts['marked_coefficients']+=1
    return dict(N=N,width=width,**counts)


def main():
    rows=[cycle_phases(N,2) for N in range(2,7)]
    rows += [cycle_phases(N,k,False) for N,k in [(3,3),(4,3),(3,4),(4,4)]]
    result=dict(status='PASS',original_paired_endpoint_phases=endpoint_phases(),
                exact_shared_cycles=rows,
                scope='Original complex endpoint phases, whole centered cycle polynomials, global scalar cancellation and marked extraction; no stationary-cycle contribution or volume theorem.')
    Path(__file__).with_name('actual_matching_graph_centered_fourier_phase_results.json').write_text(json.dumps(result,indent=2)+'\n')
    totals={key:sum(row[key] for row in rows) for key in rows[0] if key not in ('N','width')}
    print(json.dumps(dict(status='PASS',original_paired_endpoint_phases=result['original_paired_endpoint_phases'],**totals),indent=2))


if __name__=='__main__':main()
