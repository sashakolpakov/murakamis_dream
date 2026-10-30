#!/usr/bin/env python3
"""Original PSD torus contraction and a finite marked-tetrahedral coefficient.

Uniform global estimates are proved in the note. Gaussian sample errors are
finite diagnostics, not proofs of a source identification or a volume limit.
"""
import argparse
import json
from pathlib import Path
import mpmath as mp
import numpy as np
from audit_actual_q_hahn_complementary_hard_edge import matrices
from audit_actual_complete_circle_positive_face_polynomial import determinant_coefficients


def contraction():
    count=pair_checks=0;worst=0.;largest_log_excess=-float('inf')
    for N in (9,10,17,18,33,34,65,66):
        for a in sorted({max(1,N//3),(N-1)//2}):
            Hp,Hm=matrices(N,a)
            for x,b,y in ((1.3,.8,2.1),(1.3,.8,0.),(0.,.8,2.1),(1.3,0.,2.1)):
                all_X=[x*Hm/2,b*np.eye(a),y*Hp/2]
                X=[z for z in all_X if np.linalg.norm(z)>0]
                M=sum(X);ev,vec=np.linalg.eigh(M)
                inv=(vec/np.sqrt(ev))@vec.conj().T
                A=[inv@z@inv for z in X]
                assert np.linalg.norm(sum(A)-np.eye(a))<1e-9
                for step in range(1,5):
                    theta=np.array([.47*step*(j+1)+.13*j*j for j in range(len(X))])
                    B=sum(np.exp(1j*t)*z for t,z in zip(theta,A))
                    direct=np.trace(np.eye(a)-B.conj().T@B).real
                    expected=sum(abs(np.exp(1j*theta[j])-np.exp(1j*theta[k]))**2*np.trace(A[j]@A[k]).real for j in range(len(A)) for k in range(j+1,len(A)))
                    err=abs(direct-expected);worst=max(worst,err)
                    singular_values=np.linalg.svd(B,compute_uv=False)
                    assert err<2e-8*N and singular_values[0]<=1+2e-9
                    logdet=float(np.log(singular_values).sum()) if np.all(singular_values>0) else -float('inf')
                    excess=float(logdet+expected/2);largest_log_excess=max(largest_log_excess,excess)
                    assert excess<2e-8*N
                    count+=1
                for j in range(len(A)):
                    for k in range(j+1,len(A)):
                        val=float(np.trace(A[j]@A[k]).real)
                        assert val>=-1e-10;pair_checks+=1
    return {'original_determinant_torus_cases':count,'PSD_pair_traces':pair_checks,
            'maximum_trace_identity_error':worst,'largest_log_bound_excess':largest_log_excess}


def multiply1(p,q):
    out=[mp.mpf(0)]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q):out[i+j]+=a*b
    return out


def actual_k4():
    count=0;profiles=[];max_gauss=mp.mpf(0);max_cauchy=mp.mpf(0)
    for N in (9,10,17,18,33,34,65,66):
        d=N-1;M=d//2
        for a1,a2 in ((M,M),(M,max(1,M-1))):
            dc1=determinant_coefficients(N,a1);dc2=determinant_coefficients(N,a2)
            # Actual tetrahedral white graph matching01,23; marked main02.
            # L0=L2=0, L1=z,L3=1. Remove exact monomial z^(d-a1)
            # and the positive one-variable determinant scalars on triangles012/023.
            p1=[dc1[(0,a1-k,k)] for k in range(a1+1)]  # D_a1(0,1,z)
            p2=[dc2[(0,k,a2-k)] for k in range(a2+1)]  # D_a2(0,z,1)
            p=multiply1(p1,p2);target=a1
            assert all(c>0 for c in p)
            def moments(t):
                w=[c*mp.exp(j*t) for j,c in enumerate(p)];mass=mp.fsum(w)
                mean=mp.fsum(j*v for j,v in enumerate(w))/mass
                var=mp.fsum((j-mean)**2*v for j,v in enumerate(w))/mass
                return mass,mean,var
            t=mp.mpf(0)
            for _ in range(30):
                mass,mean,var=moments(t);dt=(mean-target)/var;t-=dt
                if abs(dt)<mp.mpf('1e-65'):break
            mass,mean,var=moments(t)
            assert abs(mean-target)<mp.mpf('1e-55') and var>0
            actual=p[target];gauss=mass*mp.exp(-target*t)/mp.sqrt(2*mp.pi*var)
            rel=actual/gauss-1;max_gauss=max(max_gauss,N*abs(rel))
            assert N*abs(rel)<10
            # A degree+1 torus quadrature is exact for this literal polynomial.
            nodes=len(p)+2
            integral=mp.fsum(mp.fsum(c*mp.exp(j*t)*mp.exp(2j*mp.pi*h*(j-target)/nodes) for j,c in enumerate(p)) for h in range(nodes))/nodes*mp.exp(-target*t)
            err=abs(integral/actual-1);max_cauchy=max(max_cauchy,err)
            assert err<mp.mpf('1e-55')
            profiles.append({'N':N,'labels':[a1,a2],'log_critical_radius':str(t),'variance_over_N':str(var/N),'N_relative_Gaussian_error':str(N*rel)})
            count+=1
    return {'literal_tetrahedral_positive_coefficients':count,'exact_torus_coefficient_checks':count,
            'maximum_Cauchy_relative_error':str(max_cauchy),'maximum_N_Gaussian_error_diagnostic':str(max_gauss),'profiles':profiles}


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',default='experiments/actual_positive_face_coefficient_saddle_results.json');args=ap.parse_args()
    mp.mp.dps=85
    data={'status':'PASS','precision_digits':85,'contraction':contraction(),'coefficient':actual_k4(),
          'scope':'Finite original-matrix global torus inequalities and actual tetrahedral polynomial coefficient/measure checks. Gaussian profiles are diagnostics; the graph-wide theorem is proved analytically. Original marked source equality and volume anchor have separate audits.'}
    Path(args.output).write_text(json.dumps(data,indent=2)+'\n');print(json.dumps(data,indent=2))
if __name__=='__main__':main()
