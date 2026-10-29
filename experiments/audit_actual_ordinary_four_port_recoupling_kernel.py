#!/usr/bin/env python3
"""Unequal typed Clebsch norms, cyclic four-port kernel and root partners."""
import itertools
import json
from pathlib import Path

import numpy as np

from audit_actual_two_cut_ports import balanced_data
from audit_actual_nc_morse_graph_first_normal_source_reduction import module_jet
from audit_actual_trivalent_all_channel_marked_contraction import highest_cup_cap
from audit_actual_trivalent_complete_circle_vertex_kernel import axis_apply


def factorials(q,n,p):
    Q=q*q%p;out=[1]
    for r in range(1,n+1):out.append(out[-1]*(1-pow(Q,r,p))%p)
    return out


def highest(a,b,c,q,p,fac):
    A,B,m=2*a,2*b,a+b-c
    return [(-1)**s*pow(q,s*(A-2*B+2*m-s-1),p)
            *fac[B-m+s]*fac[A-s]*pow(fac[B-m]*fac[A],-1,p)%p
            for s in range(m+1)]


def clebsch(a,b,c,q,p,closed=True):
    A,B,C,m=2*a,2*b,2*c,a+b-c;Q=q*q%p
    fac=factorials(q,max(A,B) if closed else max(A,B,C),p)
    h=highest(a,b,c,q,p,fac)
    out=np.zeros(((A+1)*(B+1),C+1),dtype=np.int64)
    if not closed:
        _,FA,KA=(t[0] for t in module_jet(A,q,p))
        _,FB,_=(t[0] for t in module_jet(B,q,p))
        Ki=np.diag([pow(int(x),-1,p) for x in np.diag(KA)])
        Ft=(np.kron(FA,np.eye(B+1,dtype=np.int64))+np.kron(Ki,FB))%p
        for s,value in enumerate(h):out[s*(B+1)+m-s,0]=value
        for r in range(1,C+1):out[:,r]=Ft@out[:,r-1]%p*pow(1-pow(Q,r,p),-1,p)%p
        return out
    for r in range(C+1):
        for i in range(A+1):
            j=m+r-i
            if not 0<=j<=B:continue
            value=0
            for s in range(m+1):
                t=j-m+s
                if not (0<=t<=j and 0<=r-t<=i):continue
                den=fac[s]*fac[m-s]*fac[t]*fac[r-t]%p
                value+=h[s]*pow(q,-A*t,p)*pow(Q,s*t,p)*pow(den,-1,p)
            out[i*(B+1)+j,r]=fac[i]*fac[j]*value%p
    return out


def norm(a,b,c,q,p):
    A,B,m=2*a,2*b,a+b-c
    fac=factorials(q,a+b+c+1,p)
    return (-1)**m*pow(q,-A*B+m*(m-1),p)*fac[a+b+c+1]*pow(fac[m]*fac[2*c+1],-1,p)%p


def reverse_dual(W,a,b,c,q,p):
    # W is on B,A; the resulting row is on A,B.
    A,B,C=2*a,2*b,2*c
    pc,_=highest_cup_cap(C,q,p)
    _,ca=highest_cup_cap(A,q,p);_,cb=highest_cup_cap(B,q,p)
    P=np.zeros(((B+1)*(A+1),(A+1)*(B+1)),dtype=np.int64)
    for u,v in itertools.product(range(A+1),range(B+1)):
        P[v*(A+1)+u,u*(B+1)+v]=1
    return pc.T@W.T%p@np.kron(cb.T,ca.T)%p@P%p


def unequal_generic():
    p,q=1009,11;count=0
    for a,b in itertools.product(range(4),repeat=2):
        for c in range(abs(a-b),a+b+1):
            W=clebsch(a,b,c,q,p);Wdesc=clebsch(a,b,c,q,p,False)
            assert np.array_equal(W,Wdesc)
            opposite=clebsch(b,a,c,q,p)
            dual=reverse_dual(opposite,a,b,c,q,p)
            n=norm(a,b,c,q,p)
            assert np.array_equal(dual@W%p,n*np.eye(2*c+1,dtype=np.int64)%p)
            # Independent lowest-slice endpoint from the ordinary F equation.
            A,B,m=2*a,2*b,a+b-c;fac=factorials(q,max(A,B),p)
            ell=pow(q,-A*B+3*A*m-2*m*m,p)*fac[A-m]*fac[B]*pow(fac[B-m]*fac[A],-1,p)%p
            h=highest(b,a,c,q,p,fac)
            for s in range(m+1):
                assert W[(A-m+s)*(B+1)+B-s,2*c]==ell*pow(q,(A-B)*s,p)*h[s]%p
            count+=1
    return {'generic_channels':count,'independent_coproduct_closed_entries_and_ordered_norms':True}


def S(a,b,c,d,e,q,p):
    w1,w2=clebsch(a,b,e,q,p),clebsch(c,d,e,q,p)
    cup,_=highest_cup_cap(2*e,q,p)
    return (w1@cup%p@w2.T%p).reshape(2*a+1,2*b+1,2*c+1,2*d+1)


def dual_vector(v,spins,q,p):
    for axis,j in enumerate(spins):v=axis_apply(highest_cup_cap(2*j,q,p)[1],v,axis,p)
    return v.transpose(3,2,1,0)


def T(a,b,c,d,f,q,p):
    value=S(b,c,d,a,f,q,p).transpose(3,0,1,2)
    weights=np.array([pow(q,2*a-2*r,p) for r in range(2*a+1)],dtype=np.int64)
    return weights[:,None,None,None]*value%p


def four_port_generic():
    p,q=1009,11;count=entries=0
    for a,b,c,d in itertools.product(range(3),repeat=4):
        es=list(range(max(abs(a-b),abs(c-d)),min(a+b,c+d)+1))
        fs=list(range(max(abs(b-c),abs(d-a)),min(b+c,d+a)+1))
        assert len(es)==len(fs)
        if not es:continue
        columns={e:S(a,b,c,d,e,q,p) for e in es}
        rows={e:dual_vector(S(d,c,b,a,e,q,p),(d,c,b,a),q,p) for e in es}
        norms={}
        for e in es:
            qdim=(pow(q,2*e+1,p)-pow(q,-2*e-1,p))*pow(q-pow(q,-1,p),-1,p)%p
            norms[e]=norm(a,b,e,q,p)*norm(c,d,e,q,p)*qdim%p
            for g in es:
                assert int(np.sum(rows[e]*columns[g])%p)==(norms[e] if e==g else 0)
        for f in fs:
            actual=T(a,b,c,d,f,q,p);target=np.zeros_like(actual)
            for e in es:
                coefficient=int(np.sum(rows[e]*actual)%p)*pow(norms[e],-1,p)%p
                target=(target+coefficient*columns[e])%p;entries+=1
            assert np.array_equal(actual,target)
        count+=1
    return {'generic_external_spin_families':count,'all_recoupling_entries':entries,
            'actual_cyclic_K_clock_and_full_bilinear_norm':True}


def highest_chart_generic():
    p,q=1009,11;Q=q*q%p;count=entries=0
    fac=factorials(q,30,p)
    for a,b,c,d in itertools.product(range(3),repeat=4):
        es=list(range(max(abs(a-b),abs(c-d)),min(a+b,c+d)+1))
        fs=list(range(max(abs(b-c),abs(d-a)),min(b+c,d+a)+1))
        if not es:continue
        H=a+b+c-d;lo=max(0,H-2*b);hi=min(2*a,H)
        diagonal=lambda i:(pow(q,2*d-2*a+1,p)*pow(Q,i,p)
            +pow(q,-2*d+2*a-1,p)*pow(Q,-i,p))%p
        off=lambda i:(-pow(q,2*b+2*c-2*a-1,p)*pow(Q,i-H,p)
            *(1-pow(Q,2*a+1-i,p))*(1-pow(Q,H-i+1,p)))%p
        right={f:T(a,b,c,d,f,q,p) for f in fs}
        for e in es:
            u=c+e-d;mcd=c+d-e;rd=d-c+e
            chi=(-1)**u*pow(q,u*(2*e-u-1)-2*c*rd,p)*fac[u]*fac[2*d]
            chi=chi*pow(fac[mcd]*fac[2*e],-1,p)%p
            column=clebsch(a,b,e,q,p)[:,u].reshape(2*a+1,2*b+1)
            source=S(a,b,c,d,e,q,p)
            for i in range(lo,hi+1):
                assert source[i,H-i,0,2*d]==chi*int(column[i,H-i])%p
            output=np.zeros_like(source)
            for f in fs:
                i0=a+f-d;mbc=b+c-f;mda=d+a-f
                h_end=highest(b,c,f,q,p,fac)[mbc]
                low=(-1)**mda*pow(q,-4*d*a+4*d*mda-mda*(mda+1),p)%p
                beta=pow(q,2*a-2*i0,p)*h_end*low%p
                assert right[f][i0,H-i0,0,2*d]==beta
                row={i0:1}
                for i in range(i0+1,hi+1):
                    row[i]=row[i-1]*(-off(i))*pow(diagonal(i)-diagonal(i0),-1,p)%p
                coefficient=chi*sum(value*int(column[i,H-i]) for i,value in row.items())
                coefficient=coefficient*pow(beta,-1,p)%p
                output=(output+coefficient*right[f])%p
                entries+=1
            assert np.array_equal(output,source)
        count+=1
    return {'highest_source_chart_families':count,'finite_two_sum_inverse_entries':entries,
            'exact_middle_Casimir_eigenrow_and_endpoint_normalizations':True,
            'all_entry_inverse_recoupling_identity':True}


def root_partners(N):
    p,_,q,*_=balanced_data(N);M=(N-1)//2;Q=q*q%p
    count=high=normzeros=0
    for a,b in itertools.product(range(M+1),repeat=2):
        A,B=2*a,2*b
        EA,FA,KA=(t[0] for t in module_jet(A,q,p))
        EB,FB,KB=(t[0] for t in module_jet(B,q,p))
        Ki=np.diag([pow(int(x),-1,p) for x in np.diag(KA)])
        pair=(np.kron(EA,KB)+np.kron(np.eye(A+1,dtype=np.int64),EB),
              np.kron(FA,np.eye(B+1,dtype=np.int64))+np.kron(Ki,FB),np.kron(KA,KB))
        for c in range(abs(a-b),a+b+1):
            W=clebsch(a,b,c,q,p)
            target=tuple(t[0] for t in module_jet(2*c,q,p))
            for X,Y in zip(pair,target):assert np.array_equal(X@W%p,W@Y%p)
            m=a+b-c
            # Count root zeros in the UNCANCELED finite norm formula, then
            # compare to the independently stated partner admissibility.
            valuation=(a+b+c+1)//N-m//N-(2*c+1)//N
            expected=int(2*c<N-1 and abs(a-b)<=N-1-c<=a+b)
            assert valuation==expected
            normzeros+=valuation
            high+=int(2*c>=N)
            count+=1
    return {'N':N,'prime':p,'all_generic_channels_retained_at_root':count,
            'high_partner_maps_with_canceled_Nth_descendants':high,
            'ordered_norm_simple_zero_channels':normzeros,
            'all_E_F_K_covariances_and_exact_partner_zero_orders':True}


if __name__=='__main__':
    generic=unequal_generic();four=four_port_generic();chart=highest_chart_generic()
    roots=[root_partners(N) for N in range(2,10)]
    out={'status':'PASS','unequal_generic_Clebsch_and_norm':generic,
         'generic_four_port_kernel':four,'root_partners_and_source_zeros':roots,
         'explicit_two_sum_highest_chart_kernel':chart,
         'scope':'Exact generic typed four-port kernel, all root partner maps, and norm-zero orders. No Hermitian/unitary recoupling claim, polynomial conditioning, termwise-root truncation or primitive-core asymptotic.'}
    Path(__file__).with_name('actual_ordinary_four_port_recoupling_kernel_results.json').write_text(json.dumps(out,indent=2)+'\n')
    print(f"PASS{generic['generic_channels']} unequalCG/norms; {four['generic_external_spin_families']} fourportfamilies/{four['all_recoupling_entries']} entries and inverse2sum; 8 fullpartner/rootnormal families")
