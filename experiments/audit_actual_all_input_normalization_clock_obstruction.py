#!/usr/bin/env python3
"""Original all-input clock operator, exact Ward jets and obstruction."""

import json
from pathlib import Path

import mpmath as mp
import numpy as np

from audit_actual_two_cut_ports import balanced_data


def fac_field(Q, N, prime):
    out = [1]
    for j in range(1, N):
        out.append(out[-1]*(1-pow(Q, j, prime)) % prime)
    return out


def D_field(i, s, Q, fac, prime, derivative=False):
    return fac[i]**2*sum((b if derivative else pow(s, b, prime))
        *pow(Q, b*b, prime)*pow(fac[i-b]*fac[b]**2 % prime, -1, prime)
        for b in range(i+1)) % prime


def original_field_case(N):
    prime, eta, q, E, F, K, pivot, R, Rminus = balanced_data(N)
    d, Q, x = N-1, q*q % prime, int(K[0, 0])
    fac = fac_field(Q, N, prime)
    Qm = pow(Q, -1, prime)
    facm = fac_field(Qm, N, prime)
    kappa = int(R[0, 0])
    ids = [j*N+d-j for j in range(N)]
    L = pow(kappa, -1, prime)*R[np.ix_(ids, ids)] % prime
    Linverse = kappa*Rminus[np.ix_(ids, ids)] % prime
    assert np.array_equal(L@Linverse % prime, np.eye(N, dtype=np.int64))
    Rphysical_squared = R@R % prime
    clock_checks = 0
    for t in (1, 2, 5):
        # Direct complete physical cup/R^2/cap contraction on EVERY input.
        physical = np.zeros((N, N), dtype=np.int64)
        for a in range(N):
            cap = pow(x, -a, prime)*pow(Q, -a, prime)*pow(N, -1, prime) % prime
            for n in range(N):
                cup = N*pow(x, n-d, prime) % prime
                for c in range(N):
                    physical[c, a] += (cap*int(Rphysical_squared[(d-a)*N+c, n*N+d-n])
                                       *cup*pow(t, n, prime)) % prime
            physical[:, a] %= prime
        u = np.array([pow(x*t, j, prime) for j in range(N)], dtype=np.int64)
        one = L@u % prime
        for i in range(N):
            rhs = pow(x, i, prime)*pow(t, d, prime)*D_field(i, pow(t, -1, prime), Qm, facm, prime) % prime
            assert int(one[i]) == rhs
        two = L@one % prime
        closed = np.array([pow(x, a, prime)*int(two[d-a]) % prime for a in range(N)])
        assert np.array_equal(physical, np.diag(closed))
        if t == 1:
            assert np.array_equal(closed, np.full(N, kappa*kappa % prime, dtype=np.int64))
        for i in range(2, N):
            rhs = ((1+Q-2*pow(Q, i, prime)+pow(Q, 2*i-1, prime)*t)
                   *D_field(i-1, t, Q, fac, prime)
                   -Q*(1-pow(Q, i-1, prime))**2*D_field(i-2, t, Q, fac, prime)) % prime
            assert D_field(i, t, Q, fac, prime) == rhs
        clock_checks += N

    P, Pm = [1], [1]
    for i in range(1, N):
        P.append(((1-pow(Q, i, prime))**2*P[-1]+pow(Q, i, prime)) % prime)
        Pm.append(((1-pow(Qm, i, prime))**2*Pm[-1]+pow(Qm, i, prime)) % prime)
    derivatives = [D_field(i, 1, Q, fac, prime, derivative=True) for i in range(N)]
    ujet = np.array([j*pow(x, j, prime) % prime for j in range(N)], dtype=np.int64)
    w, v = L@ujet % prime, L@L % prime@ujet % prime
    for i in range(N):
        Dmprime = D_field(i, 1, Qm, facm, prime, derivative=True)
        assert int(w[i]) == pow(x, i, prime)*(d-Dmprime) % prime
        if i:
            assert (derivatives[i]-derivatives[i-1]) % prime == pow(Q, i, prime)*P[i-1] % prime
            difference = (pow(x, -i, prime)*int(w[i])-pow(x, 1-i, prime)*int(w[i-1])) % prime
            assert difference == -pow(Qm, i, prime)*Pm[i-1] % prime
    Cprime = np.array([pow(x, a, prime)*int(v[d-a]) % prime for a in range(N)])
    assert int(Cprime[d]) == pow(x, -d, prime)*Q*(Pm[d]-1) % prime
    physical_jet = np.zeros((N, N), dtype=np.int64)
    for a in range(N):
        cap = pow(x, -a, prime)*pow(Q, -a, prime)*pow(N, -1, prime) % prime
        for n in range(N):
            cup = N*pow(x, n-d, prime) % prime
            for c in range(N):
                physical_jet[c, a] += cap*int(Rphysical_squared[(d-a)*N+c, n*N+d-n])*cup*n % prime
        physical_jet[:, a] %= prime
    assert np.array_equal(physical_jet, np.diag(Cprime))
    commutator = (F@physical_jet-physical_jet@F) % prime
    expected = np.zeros((N, N), dtype=np.int64)
    for a in range(d):
        expected[a+1, a] = (1-pow(Q, a+1, prime))*(int(Cprime[a])-int(Cprime[a+1])) % prime
    assert np.array_equal(commutator, expected)
    # The retained Ward insertion passes through the ACTUAL pair d+/-1
    # sectors, rather than a recording-register shift in its degree-d block.
    JF, JE = np.zeros((N, N), dtype=np.int64), np.zeros((N, N), dtype=np.int64)
    rho = (q-pow(q, -1, prime)) % prime
    Ecal = rho*rho*E % prime
    for a in range(N):
        cap = pow(x, -a, prime)*pow(Q, -a, prime)*pow(N, -1, prime) % prime
        if a < d:
            for n in range(d):
                cup = N*pow(x, n-d, prime) % prime
                JF[a+1, a] += (cap*int(Rphysical_squared[(d-a)*N+a+1, (n+1)*N+d-n])
                                *pow(int(K[a, a]), -1, prime)*int(F[n+1, n])*cup) % prime
        if a:
            for n in range(1, N):
                cup = N*pow(x, n-d, prime) % prime
                JE[a-1, a] += (cap*int(Rphysical_squared[(d-a)*N+a-1, (n-1)*N+d-n])
                                *int(Ecal[n-1, n])*int(K[d-n, d-n])*cup) % prime
    assert np.array_equal(JF % prime, -commutator % prime)
    assert np.array_equal(JE % prime, (Ecal@physical_jet-physical_jet@Ecal) % prime)
    return {'N': N, 'all_original_physical_clock_columns': clock_checks,
            'both_root_D_recursions_and_exact_normal_current': True,
            'original_selected_endpoint_jet': True,
            'full_physical_Hopf_commutator': True,
            'retained_degree_d_plus_minus_one_Ward_insertions': True}


def complex_case(N, record_disk=True):
    with mp.workdps(3*N+80):
        d = N-1
        q = mp.exp(mp.j*mp.pi/N)
        Q, x = q*q, q**d
        fac, P = [mp.mpc(1)], [mp.mpc(1)]
        for j in range(1, N):
            fac.append(fac[-1]*(1-Q**j))
            P.append((1-Q**j)**2*P[-1]+Q**j)
        L, Linverse = mp.matrix(N), mp.matrix(N)
        for j in range(N):
            for i in range(d-j, N):
                k = i+j-d
                L[i, j] = x**(-d+k)*Q**((d-j)*(d-i))*fac[i]*fac[j]/(fac[k]*fac[d-j]*fac[d-i])
            # Literal negative crossing with its inverse common scalar removed.
            b, poch = d-j, mp.mpc(1)
            for k in range(b+1):
                if k:
                    poch *= 1-Q**(-b+k-1)
                Linverse[b-k, j] = x**(d-k)*Q**(-j*b)*fac[j+k]/(fac[k]*fac[j])*poch
        if N <= 16:
            ident = Linverse*L
            assert max(abs(ident[i, j]-(i == j)) for i in range(N) for j in range(N)) < mp.mpf('1e-40')
        ujet = mp.matrix([j*x**j for j in range(N)])
        w, v = L*ujet, L*(L*ujet)
        for i in range(1, N):
            assert abs(x**(-i)*w[i]-x**(1-i)*w[i-1]+Q**(-i)*mp.conj(P[i-1])) < mp.mpf('1e-35')*max(1, abs(P[i-1]))
        B = []
        for i in range(N):
            direct = sum(abs(Linverse[i, j]) for j in range(N))
            factorial = sum(N*N/(abs(fac[i])**2*abs(fac[j])**2*abs(fac[d-i-j])) for j in range(d-i+1))
            assert abs(direct-factorial) < mp.mpf('1e-35')*max(1, factorial)
            B.append(direct)
        i = min(d, max(1, 5*N//6))
        lower = abs(P[i-1])/(B[i]+B[i-1])
        actual = max(abs(v[j]) for j in range(d-i+2))
        assert actual >= lower*(1-mp.mpf('1e-35'))
        Cprime = [x**a*v[d-a] for a in range(N)]
        full_max = max(abs(z) for z in Cprime)
        endpoint = x**(-d)*Q*mp.conj(P[d]-1)
        assert abs(Cprime[d]-endpoint) < mp.mpf('1e-35')*max(1, abs(endpoint))
        defect = max(abs((1-Q**(a+1))*(Cprime[a]-Cprime[a+1])) for a in range(d))
        assert defect >= max(0, 4*(full_max-abs(endpoint))/N**2)*(1-mp.mpf('1e-30'))
        disk_rate, disk_endpoint = None, None
        if record_disk:
            t = 1+mp.mpf(1)/N
            result = L*(L*mp.matrix([(x*t)**j for j in range(N)]))
            disk_rate = float(mp.log(max(abs(z) for z in result))/N)
            disk_endpoint = float(abs(result[0]))
        return {'N': N, 'literal_inverse_and_finite_current_inequality': True,
                'witness_input_minimum': i-1,
                'finite_current_lower_lograte': float(mp.log(lower)/N),
                'actual_first_jet_max_lograte_diagnostic': float(mp.log(full_max)/N),
                'actual_F_Ward_defect_lograte_diagnostic': float(mp.log(defect)/N),
                'one_disk_point_operator_lograte_diagnostic': disk_rate,
                'same_disk_point_selected_endpoint_modulus': disk_endpoint}


if __name__ == '__main__':
    fields = [original_field_case(N) for N in range(2, 13)]
    fields.append(original_field_case(14))
    complex_rows = [complex_case(N) for N in (2, 3, 4, 6, 8, 12, 16, 24, 48, 96)]
    output = {'status': 'PASS', 'all_original_physical_input_columns': fields,
              'complete_complex_currents_and_finite_lower_bound': complex_rows,
              'scope': 'All-input clock-disk operator obstruction; selected scalar cancellation and global source scope retained.'}
    Path(__file__).with_name('actual_all_input_normalization_clock_obstruction_results.json').write_text(
        json.dumps(output, indent=2)+'\n')
    print('PASS 12 all-input original normalization operators; exact Ward jets/physical commutators; 10 complete complex current bounds')
