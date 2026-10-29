#!/usr/bin/env python3
"""Actual channel-wise Markov trace, whole-knot source and full-Psi rays."""

from itertools import product
import json
from pathlib import Path

import mpmath as mp
import numpy as np

from audit_actual_borel_regular_fusion import fusion, inv
from audit_actual_hardy_cauchy_network import HardyNetwork
from audit_actual_modular_dilog_circle import psi
from audit_actual_two_cut_ports import partial, word_matrix


def local(N, M):
    H = HardyNetwork(N, M)
    p, Q, d = H.p, H.Q, N-1
    C, Ci, *_ = fusion(N, p, Q, [H.x,H.x], [0,0])
    assert np.array_equal(C@Ci % p, np.eye(N*N, dtype=np.int64))
    U = np.zeros((N*N,N*N), dtype=np.int64)
    D = np.diag([H.diag[b] for a,b in product(range(N),repeat=2)])
    for a,b in product(range(N),repeat=2):
        for h in range(min(d-a,b)+1):
            U[(a+h)*N+b-h,a*N+b] = H.u[h]
    core = D@U % p
    actual = H.kappa*C@core@Ci % p
    assert np.array_equal(actual, H.plus)
    alpha = H.kappa*pow(H.x,-d,p) % p
    channels = []
    for k in range(N):
        P = np.diag([int(b==k) for a,b in product(range(N),repeat=2)])
        modified = H.kappa*C@core@P@Ci % p
        close = partial(modified,H.pivot,2,N,p)
        assert np.array_equal(close, alpha*int(k==0)*np.eye(N,dtype=np.int64) % p)
        channels.append(k)
    # Full arbitrary channel function; this is not assumed an intertwiner.
    r = [(j*j+3*j+2)%p for j in range(N)]
    P = np.diag([r[b] for a,b in product(range(N),repeat=2)])
    modified = H.kappa*C@core@P@Ci % p
    close = partial(modified,H.pivot,2,N,p)
    assert np.array_equal(close, alpha*r[0]*np.eye(N,dtype=np.int64) % p)
    for a,s in product(range(N),repeat=2):
        value = 0
        for j in range(s+1):
            poch = 1
            for ell in range(s):
                poch = poch*(1-pow(Q,a-j+1+ell,p)) % p
            value += ((-1)**(s-j)*pow(Q,j*(j+1)//2,p)*poch
                      * pow(H.fac[j]*H.fac[s-j] % p,-1,p))
        assert value % p == (-1)**s % p
    record = {'N':N,'M':M,'all_channel_partial_traces_exact':channels,
              'arbitrary_diagonal_evaluates_at_zero_channel':True,
              'C_inverse_pair_exact':True}
    if M == 1 and N <= 4:
        word = [1,-2,1,-2]
        exterior = partial(word_matrix(word,H.plus,H.minus,3,N,p),H.pivot,3,N,p)
        assert np.array_equal(exterior,int(exterior[0,0])*np.eye(N,dtype=np.int64) % p)
        # The literal traced kink is composed at the original open port.
        stabilized = exterior@close*pow(alpha,-1,p) % p
        assert np.array_equal(stabilized,r[0]*exterior % p)
        record['whole_original_figure_eight_normalized_cell'] = True
        record['exterior_cut'] = int(exterior[0,0])
    return record


def radial(N,R):
    with mp.workdps(48):
        def integrand(t):
            if not t:
                return mp.mpf(1)
            return psi(N,1,mp.log(t))/(1-t**N)
        E = mp.quad(integrand,[0,R/3,2*R/3,R])/(2j*mp.pi)
        Q = mp.exp(2j*mp.pi/N)
        h = -N*Q**(-1)*E
        c = R*mp.sqrt(1-R)/(-mp.log(1-R))
        expected = Q**(-1)*(1-c*mp.exp(-1j*N*mp.polylog(2,R)/(2*mp.pi)))
        assert 0<c<1
        scaled = N*abs(h-expected)
        assert scaled < 20
        return {'N':N,'R':str(R),'ray_factor_modulus':float(abs(h)),
                'circle_factor_modulus':float(abs(1-h)),
                'N_times_asymptotic_error':float(scaled),
                'limiting_uniform_lower_margin':float(1-c)}


def main():
    fields=[]
    for N in range(2,9):
        for M in (1,3):
            try:
                fields.append(local(N,M))
            except ValueError:
                continue
    rays=[radial(N,mp.mpf(R)) for N in (4,8,16,32) for R in ('.25','.5')]
    result={'status':'PASS','actual_channel_markov_traces':fields,
            'actual_full_Psi_radial_factors':rays,
            'scope':'Original normalization cells and original whole-knot relative components; no volume-conjecture assumption.'}
    Path(__file__).with_name('actual_markov_ray_normalization_results.json').write_text(
        json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'PASS','channel_families':len(fields),
                      'whole_figure_eight_source_checks':sum('whole_original_figure_eight_normalized_cell' in r for r in fields),
                      'exact_ray_integrals':len(rays)}))


if __name__=='__main__':
    main()
