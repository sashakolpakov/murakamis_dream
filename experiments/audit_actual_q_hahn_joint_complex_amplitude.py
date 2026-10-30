#!/usr/bin/env python3
"""Exact coproduct plus actual joint amplitude/transport regressions.

The written theorem proves uniformity. These finite checks verify source
normalization, both shifts and the claimed nonzero leading amplitude;
they do not estimate a global plat sum or generic-q normal currents.
"""
import json
from pathlib import Path

import mpmath as mp
import sympy as sp

from audit_actual_two_cut_ports import balanced_data
from audit_actual_q_hahn_uniform_complex_amplitude import chosen_packet, sine_data
from audit_actual_q_hahn_selected_complex_action import energy


def exact_coproduct():
    checks = 0
    for N in range(3, 22):
        p, _, q, *_ = balanced_data(N)
        Q = q*q % p
        poch = [1]
        for n in range(1, N):
            poch.append(poch[-1]*(1-pow(Q, n, p)) % p)
        for j in range((N-1)//2+1):
            choose = [poch[j]*pow(poch[a]*poch[j-a] % p, -1, p) % p
                      for a in range(j+1)]

            def source(U, V):
                H = 0
                for a in range(j+1):
                    term = choose[a]**2*pow(q, a*(a-(N-1)), p)*pow(V, a, p)
                    for r in range(a):
                        term = term*(U-pow(Q, r, p)) % p
                    for r in range(j-a):
                        term = term*(V-pow(Q, r, p)) % p
                    H = (H+term) % p
                den = 1
                for r in range(j):
                    den = den*(U*V-pow(Q, r, p)) % p
                return None if not den else H*pow(den, -1, p) % p

            for U, V in ((2, 3), (5, 7), (11, 13), (17, 19)):
                T = U*V % p
                values = [source(U, Q*V % p),
                          source(U*pow(Q, -1, p) % p, Q*V % p), source(U, V)]
                if any(v is None for v in values):
                    continue
                lhs = (1-Q*T)*values[0]
                rhs = (1-U)*values[1]+(U-Q*T)*values[2]
                assert (lhs-rhs) % p == 0
                checks += 1
    return checks


class Source:
    def __init__(self, N, j):
        self.N, self.j = N, j
        self.h, self.xi = mp.mpf(1)/N, mp.mpf(j)/N
        self.cos = [mp.cos(mp.pi*n/N) for n in range(j+1)]
        self.B = [None]+[mp.sin(mp.pi*n/N)**2 /
                              (self.cos[n]**2*mp.sin(mp.pi*(2*n-1)/N)
                               *mp.sin(mp.pi*(2*n+1)/N)) for n in range(1, j)]
        self.sf = [mp.mpf(1)]
        for n in range(1, 2*j+1):
            self.sf.append(self.sf[-1]*2*mp.sin(mp.pi*n/N))
        self.central_beta = self.sf[2*j]/self.sf[j]**2

    def determinant(self, tau, nu):
        N, j = self.N, self.j
        c = -mp.cos(mp.pi*(tau+self.h))
        z = mp.exp(mp.pi*1j*(tau-2*nu))
        prior, R = mp.mpf(1), z+c/self.cos[1]
        for n in range(1, j):
            prior, R = R, ((z+c/(self.cos[n]*self.cos[n+1]))*R
                           +self.B[n]*(self.cos[n]**2-c*c)*prior)
        den = mp.fprod(2*mp.sin(mp.pi*(tau-mp.mpf(r)/N)) for r in range(j))
        phase = mp.pi*1j*((N-1)*nu+mp.mpf(j*j-(N-1)*j)/(2*N))
        return self.central_beta*mp.exp(phase)*R/den

    def direct(self, tau, nu):
        """Literal terminating sine sum, independent of the determinant."""
        N, j = self.N, self.j

        def seq(scaled):
            values = [mp.mpc(1)]
            for k in range(j):
                values.append(values[-1]*mp.sin(mp.pi*(scaled-mp.mpf(k)/N))
                              /mp.sin(mp.pi*(k+1)/N))
            return values

        bu, bv, bt = seq(nu), seq(tau-nu), seq(tau)
        w = mp.exp(mp.pi*1j*(tau+self.xi-1+self.h))
        terms = [w**a*self.sf[j]/self.sf[a]/self.sf[j-a]*bu[a]*bv[j-a]
                 for a in range(j+1)]
        return mp.exp(mp.pi*1j*(N-j-1)*nu)*mp.fsum(terms)/bt[j]


def selected_packet(tau, xi, nu):
    tr, nr = mp.re(tau), mp.re(nu)
    w0 = mp.exp(mp.pi*1j*(tr+xi-1))
    _, Acal, alpha, _ = chosen_packet(tr, xi, nr, w0)
    _, B, Fs, _ = sine_data(tr, xi, nr, alpha, w0)
    bf_previous = B*Fs

    def C(t, u):
        return (mp.sin(mp.pi*xi)*mp.sqrt(mp.sin(mp.pi*u)*mp.sin(mp.pi*(t-u))
                *mp.sin(mp.pi*(t-xi))/mp.sin(mp.pi*t))/2)

    c_previous = C(tr, nr)
    for k in range(1, 41):
        t = tr+(tau-tr)*k/40
        u = nr+(nu-nr)*k/40
        w = mp.exp(mp.pi*1j*(t+xi-1))
        alpha = mp.findroot(lambda a: sine_data(t, xi, u, a, w)[0]
                            -w*sine_data(t, xi, u, a, w)[1],
                            (alpha, alpha+mp.mpf('1e-6')), tol=mp.mpf('1e-135'))
        _, B, Fs, _ = sine_data(t, xi, u, alpha, w)
        current = B*Fs
        assert abs(mp.arg(current/bf_previous)) < mp.pi/2
        cc = C(t, u)
        Acal *= cc/c_previous*mp.sqrt(bf_previous/current)
        c_previous, bf_previous = cc, current
        assert all(0 < mp.re(v) < 1 for v in
                   (alpha, xi-alpha, u-alpha, t-u-xi+alpha))
    phase = energy(tau, xi, nu, alpha)+alpha*mp.log(w)+mp.pi*1j*nu*(1-xi)
    amplitude = Acal*mp.exp(mp.pi*1j*(alpha-nu))
    return phase, amplitude, alpha


def transport(tau, xi, nu, alpha):
    s = lambda v: mp.sin(mp.pi*v)
    co = lambda v: mp.cos(mp.pi*v)
    cot = lambda v: co(v)/s(v)
    w = mp.exp(mp.pi*1j*(tau+xi-1))
    rr = tau-nu-xi+alpha
    A0, B0, Fs, _ = sine_data(tau, xi, nu, alpha, w)
    anu = mp.pi*(s(alpha)**2*co(rr)+w*s(xi-alpha)**2*co(nu-alpha))/Fs
    atau = -(mp.pi*s(alpha)**2*co(rr)-mp.pi*1j*w*B0)/Fs
    a = (mp.log(2*s(nu))-mp.log(2*s(nu-alpha))-mp.log(2*s(tau-nu))
         +mp.log(2*s(rr))+mp.pi*1j*(1-xi))
    b = (mp.log(2*s(tau-nu))-mp.log(2*s(rr))-mp.log(2*s(tau))
         +mp.log(2*s(tau-xi))+mp.pi*1j*alpha)
    ann = mp.pi*(cot(nu)+cot(tau-nu)-(1-anu)*(cot(nu-alpha)+cot(rr)))
    btt = mp.pi*(cot(tau-nu)-(1+atau)*cot(rr)-cot(tau)+cot(tau-xi))+mp.pi*1j*atau
    U, T, J = [mp.exp(2*mp.pi*1j*v) for v in (nu, tau, xi)]
    ea, eb = mp.exp(a), mp.exp(b)
    A = (U-T)*(1-U)/T
    D = 2*U*(1+T-U)/T
    assert abs(A*(ea+1/ea)+D-(J+1/J)) < mp.mpf('1e-110')
    assert abs((1-T)*eb-(U-1)/ea-U+T) < mp.mpf('1e-110')
    H1 = (-2*mp.pi*1j*U*(U-T)/T*ea-2*mp.pi*1j*U*(1-U)/T/ea
          +2*mp.pi*1j*U*(T-1)/T-mp.pi*1j*(J-1/J))
    r = -(H1+ann*A*(ea+1/ea)/2)/(A*(ea-1/ea))
    ss = ((1-U)/ea*(mp.pi*1j+r-ann/2)+2*mp.pi*1j*T*(eb-1)
          -(1-T)*eb*btt/2)/((1-T)*eb)
    return a, b, r, ss


def numerical():
    mp.mp.dps = 160
    rows = []
    source_max = error_max = derivative_max = 0.0
    gradient_checks = 0
    cases = [('0.8', '0.4'), ('0.8', '0.5'), ('0.9', '0.3333333333333333333333'),
             ('0.7', '0.3')]
    for N in (32, 65, 128, 257):
        for ts, js in cases:
            j = (N-1)//2 if js == '0.5' else int(mp.floor(mp.mpf(js)*N))
            t = N-1-j if ts == '0.7' else int(mp.floor(mp.mpf(ts)*N))
            src = Source(N, j)
            for dt, dn in ((mp.mpc('0.0', '0.035'), mp.mpc('0.0', '-0.025')),
                           (mp.mpc('0.2', '-0.2')/N, mp.mpc('0.17', '0.3')/N)):
                tau = mp.mpf(t)/N+dt
                nu = mp.mpf(t)/(2*N)+dn
                direct = src.direct(tau, nu)
                det = src.determinant(tau, nu)
                source_error = abs(direct/det-1)
                assert source_error < mp.mpf('1e-100')
                source_max = max(source_max, float(source_error))
                phase, amplitude, alpha = selected_packet(tau, src.xi, nu)
                predicted = amplitude*mp.exp(N*phase)/mp.sqrt(N)
                err = N*abs(det/predicted-1)
                assert err < 10
                error_max = max(error_max, float(err))
                row = dict(N=N, j=j, tau=[float(mp.re(tau)), float(mp.im(tau))],
                           nu=[float(mp.re(nu)), float(mp.im(nu))],
                           N_times_relative_error=float(err), amplitude_modulus=float(abs(amplitude)))
                if js == '0.5' and mp.im(dt) > 0:
                    a, b, r, ss = transport(tau, src.xi, nu, alpha)
                    an = mp.diff(lambda v: src.determinant(tau, v), nu)/det/N
                    bn = mp.diff(lambda v: src.determinant(v, nu), tau)/det/N
                    e1, e2 = N*N*abs(an-a-r/N), N*N*abs(bn-b-ss/N)
                    assert max(e1, e2) < 20
                    derivative_max = max(derivative_max, float(e1), float(e2))
                    row.update(N_squared_nu_gradient_remainder=float(e1),
                               N_squared_tau_gradient_remainder=float(e2))
                    gradient_checks += 2
                rows.append(row)
    return dict(precision_digits=mp.mp.dps, joint_amplitude_cases=len(rows),
                independent_source_determinant_comparisons=len(rows),
                maximum_source_relative_error=source_max,
                maximum_N_times_relative_error=error_max,
                actual_gradient_corrections=gradient_checks,
                maximum_N_squared_gradient_remainder=derivative_max, cases=rows)


def sheet_selector():
    """Exact characteristic reduction and independent saddle-sheet checks."""
    z, c, s, root = sp.symbols('z c s root')
    V = 1+2*c*z+z*z
    W = 1+2*c*z+(1-s*s)*z*z
    Y = (s*z+sp.I*root)**2/V
    relation = sp.together(Y+1/Y-2+4*W/V).as_numer_denom()[0]
    assert sp.rem(sp.expand(relation), root*root-W, root) == 0
    recovered = sp.together((V*Y-s*s*z*z+W)/(2*sp.I*s*z)-root)
    assert sp.rem(sp.expand(recovered.as_numer_denom()[0]), root*root-W, root) == 0
    mp.mp.dps = 160
    checks = 0
    maximum = 0.0
    for xi in (mp.mpf('.4'), mp.mpf('.5')):
        for tau, nu in ((mp.mpc('.8', '.035'), mp.mpc('.4', '-.025')),
                         (mp.mpc('.85', '-.04'), mp.mpc('.32', '.03'))):
            _, _, alpha = selected_packet(tau, xi, nu)
            a, _, _, _ = transport(tau, xi, nu, alpha)
            zz = mp.exp(mp.pi*1j*(tau-2*nu))
            cc, ss = -mp.cos(mp.pi*tau), mp.sin(mp.pi*xi)
            ww = 1+2*cc*zz+mp.cos(mp.pi*xi)**2*zz*zz
            vv = 1+2*cc*zz+zz*zz
            target = (ss*zz+1j*mp.sqrt(ww))**2/vv
            error = abs(target/mp.exp(a)-1)
            assert error < mp.mpf('1e-110')
            candidate = (vv*mp.exp(a)-ss*ss*zz*zz+ww)/(2j*ss*zz)
            opposite = (vv*mp.exp(-a)-ss*ss*zz*zz+ww)/(2j*ss*zz)
            assert mp.re(candidate) > 0 and mp.re(opposite) < 0
            maximum = max(maximum, float(error))
            checks += 1
    return dict(exact_characteristic_and_recovery_identities=2,
                complex_selected_sheet_checks=checks, maximum_relative_error=maximum,
                scope='Local principal-sheet selection only; no global common frame or cycle claim.')


def main():
    result = dict(status='PASS', exact_off_lattice_coproduct_checks=exact_coproduct(),
                  numerical=numerical(), sheet_selector=sheet_selector(),
                  scope='Exact original normalized coproduct at nonphysical arguments; independent terminating-sum/determinant comparisons and finite regressions of joint complex amplitudes and both gradient corrections. The written proof supplies uniformity. Integer channel retained; no global cycle, coherent sum, or generic-q normal estimate.')
    Path(__file__).with_name('actual_q_hahn_joint_complex_amplitude_results.json').write_text(
        json.dumps(result, indent=2)+'\n')
    print(json.dumps({**{k: v for k, v in result.items() if k != 'numerical'},
                      **{k: v for k, v in result['numerical'].items() if k != 'cases'}}, indent=2))


if __name__ == '__main__':
    main()
