#!/usr/bin/env python3
"""Diagnostic, not an asymptotic proof: original terminal phase jets and arc energy."""

import argparse
import json
from pathlib import Path

import mpmath as mp


def evaluate(N, dps, arc_power):
    mp.mp.dps = dps
    d = N-1
    q = mp.exp(mp.j*mp.pi/N)
    Q, x = q*q, q**d
    phases = [Q**j for j in range(N)]
    Qp = lambda n: phases[n % N]
    fac = [mp.mpc(1)]
    for j in range(1, N):
        fac.append(fac[-1]*(1-Qp(j)))
    green = [mp.mpc(1)]
    for j in range(1, N):
        green.append((1-Qp(j))**2*green[-1]+Qp(j))

    # All original complete input columns retained.  For B=R12 R23^-1,
    # Bp=N L e_d, so exact T factorization uses L^2 e_d here.
    low = []
    for j in range(N):
        z = mp.fsum((-1)**v*Qp(v*(v+1)//2-j*v)
                    /(fac[j-v]*fac[v]**3) for v in range(j+1))
        low.append(N*N*x**(j-d)*fac[j]/fac[d-j]*z)
    packet = []
    for n in range(N):
        z = mp.fsum(Qp(-n*t)*fac[n-t]*(fac[n]/fac[t]/fac[n-t])**2
                    *((-1)**t*x**t*Qp(t*(t+1)//2))*green[t]*low[d-t]
                    for t in range(n+1))
        packet.append((-1)**n*Qp(-n*(n+3)//2)*z)
    scalar = mp.fsum(packet)
    jet = mp.fsum(n*packet[n] for n in range(N))
    a = mp.mpf(N)**(-arc_power)
    sinc = [mp.mpf(1)] + [mp.sin(a*j)/(a*j) for j in range(1, N)]
    arc_energy = mp.re(mp.fsum(packet[n]*mp.conj(packet[m])*sinc[abs(n-m)]
                               for n in range(N) for m in range(N)))
    assert arc_energy > 0
    return {'N': N, 'dps': dps, 'arc_power': arc_power,
            'scalar_abs': mp.nstr(abs(scalar), 28),
            'scalar_vs_green_last_relative_error': mp.nstr(abs(scalar-green[-1])/max(1, abs(scalar)), 8),
            'first_jet_abs': mp.nstr(abs(jet), 28),
            'first_jet_log_rate': mp.nstr(mp.log(max(1, abs(jet)))/N, 25),
            'normalized_arc_energy': mp.nstr(arc_energy, 28),
            'arc_half_log_rate': mp.nstr(mp.log(arc_energy)/(2*N), 25)}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--levels', default='8,16,24,32,48,64')
    parser.add_argument('--arc-power', type=int, default=3)
    args = parser.parse_args()
    records = []
    for N in map(int, args.levels.split(',')):
        base = evaluate(N, 100+4*N, args.arc_power)
        check = evaluate(N, 160+4*N, args.arc_power)
        for key in ['scalar_abs', 'first_jet_abs', 'normalized_arc_energy']:
            a, b = mp.mpf(base[key]), mp.mpf(check[key])
            assert abs(a-b)/max(1, abs(b)) < mp.mpf('1e-24')
        check['paired_lower_precision_dps'] = base['dps']
        records.append(check)
        print(N, check['first_jet_log_rate'], check['arc_half_log_rate'], flush=True)
    out = {'status': 'DIAGNOSTIC_PAIRED_PRECISION',
           'original_word': [-2, 1, 2, 2], 'prefix_action': 'R12 R23^-1',
           'packet_definition': 'T_n(Bp), with original complete source and full Cartan',
           'records': records,
           'scope': 'Finite numerical values only. No limiting jet exponent, exact 5_2 transform, or selected-cycle survival is proved.'}
    Path(__file__).with_name('terminal_cartan_jet_and_arc_diagnostics.json').write_text(json.dumps(out, indent=2)+'\n')
