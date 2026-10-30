#!/usr/bin/env python3
"""Focused checks of the actual root density and its local folded Gaussian.

No global period or mixed-color assertion is tested here.  The proof of
uniformity is in the note; the scalar and whole-source checks independently
retain the actual endpoint offsets and original marked normalization.
"""
import argparse
import json
from pathlib import Path

import mpmath as mp
import sympy as sp

from audit_actual_augmented_plat_phase_compiler import level
from audit_actual_q_hahn_joint_complex_amplitude import Source, selected_packet
from audit_actual_q_hahn_selected_complex_action import J


def symbolic():
    N, tau, alpha, epsilon = sp.symbols('N tau alpha epsilon')
    actual = -sp.pi*sp.I*(N-1)*tau \
        +(epsilon-1)*sp.pi*sp.I*(N*alpha+N*alpha**2+alpha)
    target = N*sp.pi*sp.I*(-tau+(epsilon-1)*(alpha+alpha**2)) \
        +sp.pi*sp.I*(tau+(epsilon-1)*alpha)
    assert sp.expand(actual-target) == 0
    k = sp.symbols('k', integer=True)
    assert sp.expand(k-(k-1)-2) == -1
    s, sm = sp.symbols('s sm')
    aa, am = (N-1-s)/2, (N-1-sm)/2
    # Remaining difference is the integer 2*(a-am), hence exp(pi i *)=1.
    difference = aa-am+(aa*(aa+1)-am*(am+1))/N-(s*s-sm*sm)/(4*N)
    assert sp.expand(difference-2*(aa-am)) == 0
    return dict(literal_coupon_phase=True, original_marked_boundary_power=-1,
                exact_fold_half_twist_phase=True)


def factorials(N):
    sf = [mp.mpf(1)]
    for n in range(1, N):
        sf.append(sf[-1]*2*mp.sin(mp.pi*n/N))
    return sf


def endpoints():
    scalars = twists = 0
    error = mp.mpf(0)
    for N in range(3, 52):
        d, M = N-1, (N-1)//2
        q = mp.exp(mp.pi*1j/N)
        sf = factorials(N)
        km = 1 if N % 2 else 2
        h0 = km*N*sf[2*M]/sf[M]**2
        expected = N if N % 2 else 2*N/mp.sin(mp.pi/N)
        err = abs(h0/expected-1)
        assert err < mp.mpf('1e-125')
        error = max(error, err)
        scalars += 1
        nuM = (-1)**M*q**(M*(M+1))
        sm = d-2*M
        for a in range(M+1):
            s = d-2*a
            ratio = (-1)**a*q**(a*(a+1))/nuM
            answer = mp.exp(mp.pi*1j*(s*s-sm*sm)/(4*N))
            err = abs(ratio/answer-1)
            assert err < mp.mpf('1e-125')
            error = max(error, err)
            twists += 1
    return dict(original_h0_endpoint_scalars=scalars,
                exact_signed_fold_phase_ratios=twists,
                maximum_relative_error=str(error))


def packets():
    records = []
    max_measure = max_coupon = max_source = mp.mpf(0)
    for N in (40, 41, 80, 81, 128, 129):
        d, a = N-1, (N-1)//2
        t, u, v = int(mp.floor(mp.mpf('.79')*N)), \
            int(mp.floor(mp.mpf('.29')*N)), int(mp.floor(mp.mpf('.43')*N))
        tau, alpha = mp.mpf(t)/N, mp.mpf(a)/N
        eta, zeta = tau+alpha-1, tau-alpha
        sf, source = factorials(N), Source(N, a)
        k = 1 if 2*a == d else 2
        h = k*sf[t]**2/(sf[t-a]*sf[t+a-d])
        H = 2*J(tau)-J(zeta)-J(eta)
        bh = mp.sin(mp.pi*tau)/(2*mp.sin(mp.pi*eta)
              *mp.sqrt(mp.sin(mp.pi*zeta)*mp.sin(mp.pi*eta)))
        measure_error = N*abs(h/(k*bh*mp.exp(N*H))-1)
        assert measure_error < 20
        max_measure = max(max_measure, measure_error)
        phases, amplitudes, values = [], [], []
        for row in (u, v):
            nu = mp.mpf(row)/N
            phi, amp, _ = selected_packet(tau, alpha, nu)
            value = source.direct(tau, nu)
            source_error = abs(value/source.determinant(tau, nu)-1)
            assert source_error < mp.mpf('1e-105')
            max_source = max(max_source, source_error)
            phases.append(phi); amplitudes.append(amp); values.append(value)
        q = mp.exp(mp.pi*1j/N)
        nua = (-1)**a*q**(a*(a+1))
        row = dict(N=N, actual_channel=a, h0=str(k*N*sf[2*a]/sf[a]**2),
                   measure_N_relative_error=str(measure_error), signed=[])
        for eps in (-1, 0, 1):
            # The known head-independent kappa^epsilon is left on both sides.
            literal = q**(-d*t)*nua**(eps-1)*h*values[0]*values[1]
            theta = H+sum(phases)+mp.pi*1j*(-tau+(eps-1)*(alpha+alpha*alpha))
            amplitude = bh*amplitudes[0]*amplitudes[1] \
                *mp.exp(mp.pi*1j*(tau+(eps-1)*alpha))
            predicted = k/N*amplitude*mp.exp(N*theta)
            err = N*abs(literal/predicted-1)
            assert err < 30
            max_coupon = max(max_coupon, err)
            row['signed'].append(dict(epsilon=eps, N_relative_error=str(err)))
        records.append(row)
    return dict(precision_digits=mp.mp.dps, actual_signed_coupon_packets=18,
                original_terminating_determinant_comparisons=12,
                scalar_CD_packets=6, records=records,
                maximum_N_measure_relative_error=str(max_measure),
                maximum_N_coupon_relative_error=str(max_coupon),
                maximum_literal_source_relative_error=str(max_source))


def folded_gaussians():
    records = []
    for H in (mp.mpc(-2), mp.mpc(-3, 2), mp.mpc(-1, -4)):
        for N in (127, 128, 511, 512, 2047, 2048):
            M = (N-1)//2
            # A fixed small local channel neighborhood; the discarded part
            # is exponentially small, with the same Gaussian coefficient.
            width = mp.mpf('.12')
            total = mp.mpc(0)
            for a in range(max(0, int(mp.ceil(N*(mp.mpf('.5')-width)))), M+1):
                w = mp.mpf(N)/2-a
                k = 1 if 2*a == N-1 else 2
                # Include a nonconstant amplitude and a genuine cubic term.
                displacement = -w/N
                amp = mp.exp(mp.mpc('.3','.2')*displacement)
                phase = H*w*w/(2*N)+mp.mpc('.2','.1')*N*displacement**3
                total += k*amp*mp.exp(phase)
            target = mp.sqrt(N)*mp.sqrt(2*mp.pi)/mp.sqrt(-H)
            error = abs(total/target-1)
            assert error < 1
            records.append(dict(N=N, H=[str(mp.re(H)),str(mp.im(H))],
                                relative_error=str(error),
                                sqrt_N_relative_error=str(mp.sqrt(N)*error)))
        assert mp.mpf(records[-1]['relative_error']) < mp.mpf('.08')
        assert mp.mpf(records[-2]['relative_error']) < mp.mpf('.08')
    return dict(actual_parity_lattice_gaussians=len(records), records=records,
                scope='Analytical Gaussian lemma calibration; no global source period.')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    mp.mp.dps = 140
    # Original matrices and unrestricted root marked contractions, independently
    # reconstructed by the frozen source compiler, not a proposed local model.
    original = [level(N) for N in (3, 4)]
    result = dict(status='PASS', symbolic=symbolic(), endpoints=endpoints(),
                  original_source=original, packets=packets(),
                  folded=folded_gaussians(),
                  scope='Complete-color local marked density and local folded Gaussian; '
                        'no global cycle, framing integral, mixed-color or filling theorem.')
    output = args.output or Path(__file__).with_name(
        'actual_augmented_plat_local_marked_density_results.json')
    output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(dict(status='PASS', endpoint_scalars=49,
                          fold_phase_ratios=result['endpoints']['exact_signed_fold_phase_ratios'],
                          original_marked_plats=sum(len(x['whole_plats']) for x in original),
                          actual_coupon_packets=18, gaussian_calibrations=18,
                          maximum_N_coupon_relative_error=result['packets']['maximum_N_coupon_relative_error']),
                     indent=2))


if __name__ == '__main__':
    main()
