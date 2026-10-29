#!/usr/bin/env python3
"""Exact source-flat carry deformation, retained Euler factor and flat norm."""

import itertools,json,math
from pathlib import Path

import numpy as np

from audit_actual_hardy_cauchy_network import HardyNetwork
from audit_actual_crossing_euler_completion import completion
from audit_actual_borel_regular_fusion import fusion,right_regular
from audit_actual_two_cut_ports import word_matrix,partial
from audit_whole_fermat_toric_residue_and_wire_source import sources


def local_fields():
    rows=[]
    for N in range(2,10):
        H=HardyNetwork(N,1);p,Q=H.p,H.Q
        T,Ti=completion(N,p,Q,H.x,H.plus,H.minus)
        Dp=(T-H.plus)%p;Dm=(Ti-H.minus)%p
        C,Ci,*_=fusion(N,p,Q,[H.x,H.x],[0,0])
        degree=np.array([a+b for a,b in itertools.product(range(N),repeat=2)])
        for radius in (2,3):
            z=pow(radius,N,p)
            L=np.array([pow(radius,int(d),p) for d in degree],dtype=np.int64)
            Li=np.array([pow(int(a),-1,p) for a in L],dtype=np.int64)
            P=(H.plus+z*Dp)%p;M=(H.minus+z*Dm)%p
            assert np.array_equal(P@M%p,np.eye(N*N,dtype=np.int64))
            assert np.array_equal(P,T*L[:,None]*Li[None,:]%p)
            assert np.array_equal(M,Ti*L[:,None]*Li[None,:]%p)
            coeff=np.zeros(N*N,dtype=np.int64)
            for a,k in itertools.product(range(N),repeat=2):
                coeff[a*N+k]=(H.kappa*pow(-1,k,p)*pow(Q,k*(k-1)//2,p)
                    *pow(H.x,-a-2*k,p)*pow(H.fac[a],-1,p)*(1 if a+k<N else z))%p
            assert np.array_equal((C@right_regular(coeff,N,0,p)%p)@Ci%p,P)
            fz=np.zeros(N*N,dtype=np.int64)
            for k in range(N):fz[N+k]=z if k==N-1 else 1
            Rf=right_regular(fz,N,0,p)
            U=np.eye(N*N,dtype=np.int64);power=U.copy()
            for a in range(1,N):
                power=Rf@power%p
                U=(U+pow(H.x,-a,p)*pow(H.fac[a],-1,p)*power)%p
            assert not np.any(Rf@power%p)
            diag=np.zeros(N*N,dtype=np.int64)
            for k in range(N):diag[k]=pow(-1,k,p)*pow(Q,k*(k-1)//2,p)*pow(H.x,-2*k,p)%p
            Euler=(C@right_regular(diag,N,0,p)%p)@U%p@Ci%p*H.kappa%p
            assert np.array_equal(Euler,P)
        rows.append({'N':N,'both_signs_literal_inverse':True,
                     'degree_gauge_equals_z_carry_weight':True,
                     'actual_weighted_Euler_argument_and_Gaussian_retained':True})
    return rows


def whole_sources():
    rows=[]
    for N in (2,3,4):
        H=HardyNetwork(N,1);p=H.p
        T,Ti=completion(N,p,H.Q,H.x,H.plus,H.minus)
        for z in (2,5):
            plus=(H.plus+z*(T-H.plus))%p
            minus=(H.minus+z*(Ti-H.minus))%p
            for width,word in ((2,[1,1,1]),(3,[1,-2,1,-2]),
                               (3,[-1,2,1,-2,1]),(4,[1,-2,3,1,-2,3])):
                W=word_matrix(word,H.plus,H.minus,width,N,p)
                Wz=word_matrix(word,plus,minus,width,N,p)
                assert np.array_equal(partial(W,H.pivot,width,N,p),partial(Wz,H.pivot,width,N,p))
                if width==4:
                    cup,cap,mark=sources(H)
                    source_in=np.kron(cup,cup)%p
                    source_out=np.kron(cap,mark)%p
                    assert int(source_out@((Wz-W)@source_in%p))%p==0
                rows.append({'N':N,'width':width,'word':word,'carry_parameter':z,
                             'whole_original_pivotal_cut_preserved':True,
                             'full_original_marked_plat_preserved_when_width4':width==4})
    return rows


def complex_bounds():
    rows=[]
    A=3+3*math.log(2)
    for N in range(2,13):
        Q=np.exp(2j*np.pi/N);x=-np.exp(-1j*np.pi/N);d=N-1
        F=np.ones(N,dtype=complex)
        for k in range(1,N):F[k]=F[k-1]*(1-Q**k)
        assert sum(1/abs(F))<=math.exp(N/2)*(1+1e-12)
        max_C,max_Ci=0.,0.
        for total in range(2*d+1):
            indices=list(range(max(0,total-d),min(d,total)+1));n=len(indices)
            M=np.array([[1/F[a-u] if u<=a else 0 for a in indices] for u in indices])
            Mi=np.array([[(-1)**(a-u)*Q**((a-u)*(a-u-1)/2)/F[a-u] if u<=a else 0
                          for a in indices] for u in indices])
            assert np.linalg.norm(M@Mi-np.eye(n))<1e-7
            left=np.array([x**u*F[total-u] for u in indices])
            right=np.array([x**(-a)*F[a]/F[total-a] for a in indices])
            C=left[:,None]*M*right[None,:]
            Ci=(1/right)[:,None]*Mi*(1/left)[None,:]
            assert np.linalg.norm(C@Ci-np.eye(n))<1e-6
            max_C=max(max_C,np.linalg.norm(C,2));max_Ci=max(max_Ci,np.linalg.norm(Ci,2))
        assert max_C<=math.exp((1+2*math.log(2))*N)
        assert max_Ci<=math.exp((1.5+math.log(2))*N)
        rows.append({'N':N,'original_fusion_norm':max_C,'original_inverse_norm':max_Ci,
                     'all_weight_block_factorizations_checked':2*d+1,
                     'uniform_complete_crossing_exponent_bound':A})
    return rows


def main():
    result={'status':'PASS','actual_local_Rees_Euler_identity':local_fields(),
            'whole_original_signed_sources':whole_sources(),
            'independent_original_complex_norm_bounds':complex_bounds(),
            'scope':'Arbitrarily exponential suppression of this source-null positive-N carry extension. No bound for the genuine degree-zero word, its geometric critical coefficient or arbitrary scalar cycle boundaries.'}
    Path(__file__).with_name('actual_exponentially_tame_carry_completion_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS source-flat carry deformation, literal Euler/Gaussian signed words and original flat norm bounds')


if __name__=='__main__':main()
