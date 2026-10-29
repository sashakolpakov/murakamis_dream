#!/usr/bin/env python3
"""Independent finite-sum audit of the refined normalization-clock disk bound.

Uses no primary proof/audit helpers. Numerical samples supplement the
all-complex-disk proof; they do not certify a supremum by sampling.
"""

import json
from pathlib import Path

import mpmath as mp


def disk_bound(N, c):
    return 2*mp.exp(2*c)*N*N*mp.exp(c/4*mp.log1p(2*mp.mpf(N)/(3*c)))


def case(N):
    with mp.workdps(N+90):
        Q = mp.exp(2*mp.j*mp.pi/N)
        factors = [mp.mpc(1)]
        for j in range(1, N):
            factors.append(factors[-1]*(1-Q**j))
        k = N//6
        sk = abs(factors[k])
        assert abs(sk/min(abs(a) for a in factors)-1)<mp.mpf('1e-65')
        assert abs(max(abs(a) for a in factors)*sk/N-1)<mp.mpf('1e-65')

        def G(z):
            powers = [mp.mpc(1)]
            for j in range(1, N):
                powers.append(powers[-1]*z)
            return mp.fsum(factors[j]*powers[j] for j in range(N))

        c_values = sorted(set((mp.mpf('0.125'), mp.mpf('0.5'),
                               min(mp.mpf(2), mp.mpf(N)/2), mp.sqrt(N)/2,
                               mp.mpf(N)/2)))
        largest_ratio = mp.mpf(0)
        max_recurrence_error = mp.mpf(0)
        samples = 0
        for c in c_values:
            assert 0<c<=mp.mpf(N)/2
            b = c/4
            if k:
                summand = mp.fsum(mp.log1p(b/j) for j in range(1, k+1))
                integral = k*mp.log1p(b/k)+b*mp.log1p(k/b)
                simplified = b*(1+mp.log1p(2*mp.mpf(N)/(3*c)))
                assert summand<=integral*(1+mp.mpf('1e-65'))
                assert integral<=simplified*(1+mp.mpf('1e-65'))
            for radius in (mp.mpf(0), mp.mpf('0.5'), mp.mpf(1)):
                for angular in range(8):
                    t = 1+radius*c/N*mp.exp(mp.j*mp.pi*angular/4)
                    actual = G(t)
                    recurrence = (1-t)*actual+t*Q*G(Q*t)-1
                    relative = abs(recurrence)/max(1, abs(actual), abs(G(Q*t)))
                    assert relative<mp.mpf('1e-60')
                    max_recurrence_error = max(max_recurrence_error, relative)
                    # Exact backward reconstruction, including all complex phases.
                    start = G(t*Q**(-k))
                    forcing, multiplier = mp.mpc(0), mp.mpc(1)
                    for j in range(k, 0, -1):
                        alpha = -(1-t*Q**(-j))/(t*Q**(1-j))
                        beta = 1/(t*Q**(1-j))
                        forcing = beta+alpha*forcing
                        multiplier *= alpha
                    reconstructed = forcing+multiplier*start
                    assert abs(reconstructed-actual)<mp.mpf('1e-55')*max(1, abs(actual))
                    assert abs(start)<=mp.exp(c)*N*N/sk*(1+mp.mpf('1e-60'))
                    if k:
                        product = mp.fprod(abs(1-t*Q**(-j)) for j in range(1, k+1))
                        assert product<=sk*mp.exp(integral)*(1+mp.mpf('1e-60'))
                        assert abs(forcing)<=2*k*mp.exp(2*c/3)*(1+mp.mpf('1e-60'))
                    bound = disk_bound(N, c)
                    assert abs(actual)<=bound
                    largest_ratio = max(largest_ratio, abs(actual)/bound)
                    samples += 1
        return {'N': N, 'k': k, 'complex_disk_samples': samples,
                'largest_sample_modulus_over_bound': float(largest_ratio),
                'maximum_relative_recurrence_residual': mp.nstr(max_recurrence_error, 8),
                'principal_root_minimum_reflection_and_backward_phases': True}


def spectator_case(N):
    with mp.workdps(N+90):
        Q = mp.exp(2*mp.j*mp.pi/N)
        D = max(1, int(mp.sqrt(N)/4))
        c = mp.mpf(1)
        exposed_c = c+2*mp.pi*D
        assert exposed_c<N/2
        fac = [mp.mpc(1)]
        for j in range(1, N):
            fac.append(fac[-1]*(1-Q**j))
        coefficients = {r: mp.matrix([[r+2, 2*r+1], [r*r+3, 1-r]])/(1+abs(r))
                        for r in range(-D, D+1)}
        assert mp.norm(coefficients[0]*coefficients[1]-coefficients[1]*coefficients[0])>0
        t = 1+mp.exp(mp.j*mp.mpf('0.7'))/N
        direct = mp.matrix(2)
        modes = mp.matrix(2)
        for j in range(N):
            A = sum((coefficients[r]*Q**(r*j) for r in coefficients), mp.matrix(2))
            direct += fac[j]*t**j*A
        for r, A in coefficients.items():
            argument = t*Q**r
            assert abs(argument-1)*N<=exposed_c*(1+mp.mpf('1e-60'))
            value = mp.fsum(fac[j]*argument**j for j in range(N))
            modes += value*A
        assert mp.norm(direct-modes)<mp.mpf('1e-55')*max(1, mp.norm(direct))
        mass = mp.fsum(mp.norm(A) for A in coefficients.values())
        assert mp.norm(direct)<=mass*disk_bound(N, exposed_c)
        return {'N': N, 'retained_Fourier_bandwidth': D,
                'noncommuting_operator_spectators_and_exact_modes': True,
                'effective_disk_constant': float(exposed_c)}


def root_profile_case(N):
    with mp.workdps(N+90):
        q = mp.exp(mp.j*mp.pi/N); Q = q*q; x = q**(N-1)
        fac = [mp.mpc(1)]
        for j in range(1, N):
            fac.append(fac[-1]*(1-Q**j))
        s = [abs(z) for z in fac]
        phases = [Q**j for j in range(N)]
        H = [mp.fsum(fac[j]*phases[(r*j) % N] for j in range(N))
             for r in range(N)]
        m = N//6
        assert abs(H[1]-Q**(-1))<mp.mpf('1e-60')
        assert abs(H[0])<=N*N+m
        for k in range(1, m+2):
            assert abs(H[k])<=k*(1+mp.mpf('1e-60'))
        for k in range(m+1, N):
            tail_min = min(s[k:])
            assert tail_min>=min(s[k-1], N)*(1-mp.mpf('1e-60'))
            exact_backward_majorant = s[k-1]*(abs(H[0])/N+
                                               mp.fsum(1/s[r] for r in range(k, N)))
            assert abs(H[k])<=exact_backward_majorant*(1+mp.mpf('1e-60'))
            assert exact_backward_majorant<=N+2*N*s[k-1]
        packet = [x**(1-N)*Q**(-j)*mp.conj(fac[j]) for j in range(N)]
        samples = [mp.fsum(packet[j]*phases[(r*j) % N] for j in range(N))
                   for r in range(N)]
        assert abs(samples[0]-x**(1-N)*Q)<mp.mpf('1e-60')
        largest_ratio = mp.mpf(0)
        for r in range(1, N):
            original_relation = x**(1-N)*Q*((1-Q**(-r))*mp.conj(H[N-r])+Q**(-r))
            assert abs(samples[r]-original_relation)<mp.mpf('1e-55')*max(1, abs(samples[r]))
            bound = 1+2*N+4*N*N/s[r]
            assert abs(samples[r])<=bound
            largest_ratio = max(largest_ratio, abs(samples[r])/bound)
        total = mp.fsum(abs(z)**2 for z in samples)
        parseval = N*mp.fsum(z*z for z in s)
        assert abs(total/parseval-1)<mp.mpf('1e-60')
        concentration = []
        for radius in (mp.mpf(1)/24, mp.mpf(1)/12):
            outside = [r for r in range(N) if abs(mp.mpf(r)/N-mp.mpf(1)/6)>=radius]
            mass = mp.fsum(abs(samples[r])**2 for r in outside)
            majorant = mp.fsum((1 if r==0 else 1+2*N+4*N*N/s[r])**2 for r in outside)
            assert mass<=majorant
            concentration.append({'fixed_neighborhood_radius': float(radius),
                                  'fraction_of_discrete_energy_outside': float(mass/total)})
        return {'N': N, 'all_original_root_samples': N,
                'forward_backward_profile_and_factorial_tail': True,
                'largest_sample_over_stated_profile': float(largest_ratio),
                'positive_Fourier_energy_relative_error': mp.nstr(abs(total/parseval-1), 8),
                'discrete_concentration_diagnostics': concentration,
                'no_continuum_concentration_inference': True}


if __name__ == '__main__':
    rows = [case(N) for N in (2, 3, 5, 6, 7, 12, 24, 48, 96, 192)]
    spectators = [spectator_case(N) for N in (48, 96, 192)]
    profiles = [root_profile_case(N) for N in (2, 3, 5, 6, 12, 24, 48, 96, 192)]
    result = {'status': 'PASS', 'independent_uniform_disk_checks': rows,
              'exposed_operator_valued_clock_modes': spectators,
              'original_normalization_root_sample_profiles': profiles,
              'scope': 'Numerical samples supplement the all-disk proof; no general original-braid bandwidth claim.'}
    Path(__file__).with_name('normalization_clock_disk_independent_results.json').write_text(
        json.dumps(result, indent=2)+'\n')
    print('PASS 10 disk/product/backward levels; 3 noncommuting spectator packets; 9 complete root-sample/positive-energy profiles')
