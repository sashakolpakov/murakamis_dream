"""Full generic large-channel source on the polynomial q circle.

This audit checks source preservation and all formerly singular recurrence
interfaces. Samples do not prove the uniform corridor estimate; the note
proves it by exact scalar cancellation and Cauchy's inequality.
"""
import json
from pathlib import Path
import mpmath as mp
from audit_actual_q_hahn_small_channel_generic_normals import (
    Dual, source_S, scalar_K, determinant, original_column,
    det_column, complex_original, poch, prod)
from explore_actual_partner_normal_complex_growth import original_column_and_normal


def exact_all_degree_checks():
    counts = dict(all_degree_source_recurrences=0,
                  original_large_generic_values_and_normals=0,
                  exact_scalar_ratio_values_and_normals=0)
    Dual.p = 1000000007
    for N in range(3,16):
        for qval in (2,5):
            q = Dual(qval,qval)
            Q,B = q*q,q**(-2*N)
            for m in range(1,N):
                sigma,U = Dual(17),Dual(11)
                T,z = sigma*sigma,sigma/U
                assert source_S(N,q,m,U,T)*z**m == (
                    sigma**(2*m)*scalar_K(N,q,m)*determinant(N,q,sigma,m,z))
                counts['all_degree_source_recurrences'] += 1
                if m>(N-1)//2:
                    for t in sorted(set((m,N-1))):
                        for u in sorted(set((0,t//2,t))):
                            assert original_column(N,q,t,m,u) == det_column(N,q,t,m,u)
                            counts['original_large_generic_values_and_normals'] += 1
            for j in range((N-2)//2+1):
                l = N-1-j
                ratio = (prod(1-B*B*Q**r for r in range(2*j+1,2*l+1))
                         /prod(1-B*B*Q**r for r in range(j+1,l+1))
                         /prod(1-B*Q**r for r in range(j+1,l+1)))
                assert ratio == scalar_K(N,q,l)/scalar_K(N,q,j)
                counts['exact_scalar_ratio_values_and_normals'] += 1
    return counts


def B_jet_phi(m,Q,X,T):
    """Partial B derivative at fixed Q,X,T, including the surviving tail."""
    def pj(a,k,power):
        value,derivative = mp.mpc(1),mp.mpc(0)
        for r in range(k):
            z = a*Q**r
            value,derivative = value*(1-z),derivative*(1-z)-value*power*z
        return value,derivative
    values,derivatives = [],[]
    for k in range(m+1):
        n,dn = pj(Q**(m+1),k,2)
        den,dd = pj(Q,k,1)
        factor = (poch(Q**(-m),Q,k)*poch(X,Q,k)*Q**k
                  /poch(1/T,Q,k)/poch(Q,Q,k))
        values.append(factor*n/den)
        derivatives.append(factor*(dn*den-n*dd)/den**2)
    return mp.fsum(values),mp.fsum(derivatives)


def complex_checks():
    mp.mp.dps = 220
    counts = dict(nonphysical_actual_large_q_circle_comparisons=0,
                  resonant_circle_gap_checks=0,
                  original_paired_vs_transverse_complex_normals=0,
                  retained_scalar_circle_identities=0,
                  bounded_and_growing_separation_cases=0)
    max_source_error,max_normal_error,max_scalar_error = [mp.mpf(0)]*3
    min_gap_over_radius = mp.inf
    max_base_inverse_cofactor = mp.mpf(0)
    profiles = []
    for N in (16,17,32,33,64,65):
        base = 1 if N%2==0 else 2
        large_s = int(mp.sqrt(N))
        if (large_s-base)%2:
            large_s -= 1
        separations = sorted(set((base,base+2,large_s)))
        for separation in separations:
            assert separation <= mp.mpf('.24')*N
            j,l = (N-1-separation)//2,(N-1+separation)//2
            for tau,nu in ((mp.mpc('.8','.03'),mp.mpc('.4','.12')),
                           (mp.mpc('.83','-.025'),mp.mpc('.3','-.08'))):
                t,u = N*tau,N*nu
                q0 = mp.exp(mp.pi*1j/N)
                Q0 = q0*q0
                cj,dj = original_column_and_normal(N,t,j,u)
                cl,dl = original_column_and_normal(N,t,l,u)
                assert abs(cl/cj-1)<mp.mpf('1e-170')
                delta = q0**(2*j+1)-q0**(-2*j-1)
                actual_normal = (dj-dl)/(-2*N*delta)
                X,T = q0**(-2*u),q0**(2*t)
                _,bj = B_jet_phi(j,Q0,X,T)
                _,bl = B_jet_phi(l,Q0,X,T)
                transverse = q0**((N-1)*u)*(bj-bl)/(2*delta)
                normal_error = abs(actual_normal-transverse)/max(abs(cj),abs(actual_normal))
                assert normal_error < mp.mpf('1e-160')
                max_normal_error = max(max_normal_error,normal_error)
                counts['original_paired_vs_transverse_complex_normals'] += 1
                rho = mp.mpf('.1')/N**8
                for phase in (0,mp.pi/2,mp.pi,3*mp.pi/2):
                    epsilon = rho*mp.exp(1j*phase)
                    q = q0*mp.exp(epsilon)
                    Q,B,A = q*q,q**(-2*N),q**(2*N)
                    sigma,z = q**t,q**(t-2*u)
                    original = complex_original(N,q,t,l,u)
                    det_value = det_column(N,q,t,l,u)
                    error = abs(original/det_value-1)
                    assert error<mp.mpf('1e-150')
                    max_source_error = max(max_source_error,error)
                    counts['nonphysical_actual_large_q_circle_comparisons'] += 1
                    lam = lambda n:A*Q**(-n)+B*Q**(n+1)
                    for n in range(1,l+1):
                        for step in range(1,min(2,n)+1):
                            ratio = abs(lam(n)-lam(n-step))/rho
                            assert ratio > mp.mpf('.1')
                            min_gap_over_radius = min(min_gap_over_radius,ratio)
                            counts['resonant_circle_gap_checks'] += 1
                    base_ratio = abs(determinant(N,q,sigma,j-1,z)
                                     /determinant(N,q,sigma,j,z))
                    max_base_inverse_cofactor = max(max_base_inverse_cofactor,base_ratio)
                    scalar_ratio = (prod(1-B*B*Q**r for r in range(2*j+1,2*l+1))
                                    /prod(1-B*B*Q**r for r in range(j+1,l+1))
                                    /prod(1-B*Q**r for r in range(j+1,l+1)))
                    scalar_error = abs(scalar_ratio/(scalar_K(N,q,l)/scalar_K(N,q,j))-1)
                    assert scalar_error<mp.mpf('1e-180')
                    max_scalar_error = max(max_scalar_error,scalar_error)
                    counts['retained_scalar_circle_identities'] += 1
                counts['bounded_and_growing_separation_cases'] += 1
                profiles.append(dict(level=N,separation=separation,
                                     tau=str(tau),nu=str(nu),
                                     actual_normal_relative_size=mp.nstr(abs(actual_normal/cj),25)))
    return dict(**counts,precision_digits=mp.mp.dps,
                max_original_source_relative_error=mp.nstr(max_source_error,35),
                max_original_normal_relative_error=mp.nstr(max_normal_error,35),
                max_scalar_ratio_relative_error=mp.nstr(max_scalar_error,35),
                minimum_spectral_gap_over_circle_radius=mp.nstr(min_gap_over_radius,30),
                maximum_small_inverse_cofactor=mp.nstr(max_base_inverse_cofactor,30),
                profiles=profiles)


if __name__=='__main__':
    result = dict(status='PASS',exact=exact_all_degree_checks(),complex=complex_checks(),
                  scope=('Full original generic large source and paired normal on fixed '
                         'complex magnetic corridors, including resonant monic rows. '
                         'The proved subexponential conclusion requires s log N=o(N); '
                         'no fixed nonzero scaled-channel, relative amplitude or global claim.'))
    target = Path(__file__).with_name('actual_q_hahn_near_fold_complex_partner_bound_results.json')
    target.write_text(json.dumps(result,indent=2)+'\n')
    summary = dict(result)
    summary['complex'] = {k:v for k,v in result['complex'].items() if k!='profiles'}
    print(json.dumps(summary,indent=2))
