#!/usr/bin/env python3
"""Original full physical endpoint matrices and exact half-block identities."""
import json
from pathlib import Path
import mpmath as mp
from audit_actual_q_hahn_physical_generic_jet_bound import matrix


def main():
    mp.mp.dps=80
    counts=dict(original_full_blocks=0,ground_congruence_entries=0,
                half_inverse_bounds=0,positive_determinant_bounds=0,
                harmonic_trace_formulas=0,full_characteristic_products=0,
                exact_schur_determinants=0)
    max_full=mp.mpf(0);max_half=mp.mpf(0)
    for N in range(3,20):
        theta=mp.pi/N;q=mp.exp(1j*theta);delta=2-q-1/q
        delta=mp.re(delta)
        for t in range(N):
            di,up,low=matrix(N,q,t)
            J=mp.diag(di)
            for r in range(t):J[r,r+1]=up[r];J[r+1,r]=low[r]
            E=J-2*mp.eye(t+1)
            detfull=mp.det(E)
            chi=mp.fprod((2*mp.sin((r+mp.mpf('.5'))*theta))**2 for r in range(t+1))
            assert abs((-1)**(t+1)*detfull/chi-1)<mp.mpf('1e-60')
            sf=mp.fprod(2*mp.sin(r*theta) for r in range(1,t+1))
            assert chi/sf**2>=mp.mpf(4)/N**2-mp.mpf('1e-60')
            counts['full_characteristic_products']+=1
            # Frobenius is an upper bound for the required operator norm.
            full_norm=mp.norm(E**-1)
            assert full_norm<100*N**17
            max_full=max(max_full,full_norm/N**3)
            counts['original_full_blocks']+=1
            if not t:continue
            a=[4*mp.sin((t-r)*theta)*mp.sin((r+1)*theta) for r in range(t)]
            halves=sorted(set(((t+1)//2,(t+2)//2)))
            for m in halves:
                F=mp.diag([(-1/q)**r for r in range(m)])
                L=mp.zeros(m)
                for r in range(m):
                    L[r,r]=a[r]+(a[r-1] if r else 0)
                    if r<m-1:L[r,r+1]=L[r+1,r]=-a[r]
                    assert a[r]>=4*mp.mpf(r+1)**2/N**2-mp.mpf('1e-60')
                V=mp.diag([q**(t-2*r) for r in range(m)])
                prefix=E[:m,:m]
                assert mp.norm(F*prefix*F+q**(-t)*(L+delta*V))<mp.mpf('1e-60')
                counts['ground_congruence_entries']+=m*m
                trace=mp.fsum((r+1)/a[r] for r in range(m))
                Linv=L**-1
                assert abs(mp.fsum(Linv[r,r] for r in range(m))-trace)<mp.mpf('1e-60')
                counts['harmonic_trace_formulas']+=1
                product=mp.fprod(a[:m])
                assert abs(mp.det(L)/product-1)<mp.mpf('1e-60')
                assert abs(mp.det(prefix))<=mp.det(L+delta*mp.eye(m))+mp.mpf('1e-60')
                assert abs(mp.det(prefix))/product<=mp.exp(delta*trace)+mp.mpf('1e-60')
                counts['positive_determinant_bounds']+=1
                # Singular values through the Hermitian Gram matrix.
                inverse=prefix**-1
                op=mp.sqrt(max(mp.eighe(inverse.H*inverse,eigvals_only=True)))
                assert op<=mp.mpf(N)**3/4+mp.mpf('1e-60')
                max_half=max(max_half,op/N**3)
                counts['half_inverse_bounds']+=1
            m=(t+1)//2;B=E[:m,:m];C=E[m:,m:]
            Bi=B**-1;Ci=C**-1;A=up[m-1]
            bridge=1-A*A*Bi[m-1,m-1]*Ci[0,0]
            assert abs(bridge-detfull/(mp.det(B)*mp.det(C)))<mp.mpf('1e-55')
            counts['exact_schur_determinants']+=1
    result=dict(status='PASS',counts=counts,
                largest_checked_full_frobenius_over_N_cubed=float(max_full),
                largest_checked_half_operator_over_N_cubed=float(max_half),
                scope='Exact original root matrices, ground congruence, positive half determinants and full Schur denominators. Polynomial uniform bounds and genuine generic-jet extension are proved in the note; no contour dominance asserted.')
    Path(__file__).with_name('actual_casimir_endpoint_resolvent_bound_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
