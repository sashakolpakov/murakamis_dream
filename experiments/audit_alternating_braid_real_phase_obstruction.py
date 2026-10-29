#!/usr/bin/env python3
"""Original-source all-level alternating phase obstruction diagnostics."""

from itertools import combinations
import json
from pathlib import Path

import mpmath as mp
import numpy as np
import sympy as sp

from audit_kashaev_crossing import original


def field_case(n):
    prime = next(4*n*k+1 for k in range(1, 1000) if sp.isprime(4*n*k+1))
    Q = pow(int(sp.primitive_root(prime)), (prime-1)//n, prime)
    r, ri, _ = original(n, prime, Q)
    swap = np.zeros_like(r)
    for a in range(n):
        for b in range(n):
            swap[b*n+a, a*n+b] = 1
    positive = swap @ r.T % prime
    negative = ri.T @ swap * pow(Q, -1, prime) % prime
    assert np.array_equal(positive @ negative % prime,
                          np.eye(n*n, dtype=np.int64))

    def weight(B, D, E, F, epsilon):
        first, second = ((positive, negative) if epsilon == 1
                         else (negative, positive))
        return (int(first[D, 1])*int(second[E*n+F, D*n+B+1])
                *int(first[0, E])*int(second[B, F])) % prime

    checks = 0
    for F, E, D, B in combinations(range(1, n-1), 4):
        u, v, t, h = B-D, D-E, E-F, n+F-B-1
        for epsilon in (1, -1):
            w, shifted = weight(B, D, E, F, epsilon), weight(B, D+1, E, F, epsilon)
            assert w and shifted
            if epsilon == 1:
                ratio = (pow(Q, -(t+h), prime)*(1-pow(Q, -u, prime))
                         *pow((1-pow(Q, v+1, prime)) % prime, -1, prime)) % prime
            else:
                ratio = (pow(Q, t+h, prime)*(1-pow(Q, u, prime))
                         *pow((1-pow(Q, -(v+1), prime)) % prime, -1, prime)) % prime
            assert shifted == w*ratio % prime
            checks += 1
    return {"N": n, "prime": prime, "exact_whole_source_ratios": checks}


def complex_cases():
    mp.mp.dps = 60
    results = []
    for n in (10, 15, 20, 40, 80):
        Q = mp.e**(2j*mp.pi/n)
        fs = [mp.mpc(1)]
        for j in range(1, n):
            fs.append(fs[-1]*(1-Q**j))

        def crossing(a, b, c, d, sign):
            u, v, t, h = (b-a-1) % n, (a-c) % n, (c-d) % n, (d-b) % n
            if u+v+t+h != n-1:
                return mp.mpc(0)
            z = n*Q**(1-(t+h)*(u+h))/(fs[u]*mp.conj(fs[v])*fs[t]*mp.conj(fs[h]))
            return z if sign == 1 else Q**(c+d-a-b)*mp.conj(z)

        def weight(B, D, E, F, epsilon):
            return (crossing(0, 1, 0, D, epsilon)
                    *crossing(D, B+1, E, F, -epsilon)
                    *crossing(0, E, 0, 0, epsilon)
                    *crossing(0, F, 0, B, -epsilon))

        B, D, E, F = 4*n//5, 3*n//5, 2*n//5, n//5
        u, v, t, h = B-D, D-E, E-F, n+F-B-1
        for epsilon in (1, -1):
            actual = weight(B, D+1, E, F, epsilon)/weight(B, D, E, F, epsilon)
            target = (mp.sin(mp.pi*u/n)/mp.sin(mp.pi*(v+1)/n)
                      *mp.e**(-epsilon*mp.pi*1j*(t+h)/n))
            assert abs(actual-target) < mp.mpf('1e-50')
            results.append({"N": n, "epsilon": epsilon,
                            "phase_over_pi": float(mp.arg(actual)/mp.pi),
                            "exact_error": float(abs(actual-target))})
    return results


def symbolic_phase():
    B, D, E, F = sp.symbols('B D E F', real=True)
    corners = [(0, 0, 1-D, D), (B-D, D-E, E-F, 1+F-B),
               (E, 0, 0, 1-E), (F, 0, 1-B, B-F)]

    def local(angles):
        u, v, t, h = angles
        return (-2*(t+h)*(u+h)-sp.Rational(1, 2)*(u*u+t*t-v*v-h*h)
                +sp.Rational(1, 2)*(u+t-v-h))

    full = sp.expand(sum(sign*local(angles)
                         for sign, angles in zip((1, -1, 1, -1), corners)))
    selected = B*D-2*B*F-D*E-D+E*F+E+F
    assert sp.expand(full-selected) == -2*D+2*E
    assert sp.diff(selected, D) == B-E-1
    optimum = {B: sp.Rational(4, 5), D: sp.Rational(3, 5),
               E: sp.Rational(2, 5), F: sp.Rational(1, 5)}
    gradient = [sp.diff(selected, z).subs(optimum) for z in (B, D, E, F)]
    assert gradient == [sp.Rational(1, 5), -sp.Rational(3, 5),
                        sp.Rational(3, 5), -sp.Rational(1, 5)]

    mp.mp.dps = 50
    lob = lambda x: mp.im(mp.polylog(2, mp.e**(2j*mp.pi*x)))/2
    entropy = lambda vals: sum(lob(mp.mpf(a)) for a in vals)/mp.pi
    for s in (mp.mpf('0.1'), mp.mpf('0.4'), mp.mpf('0.6'), mp.mpf('0.8')):
        # The derivative has its sole zero at s=3/5 by sin/cos monotonicity.
        derivative = mp.log(mp.cos(mp.pi*s/2)/mp.sin(mp.pi*s/3))
        if s < mp.mpf('0.6'):
            assert derivative > 0
        elif s > mp.mpf('0.6'):
            assert derivative < 0
        else:
            assert abs(derivative) < mp.mpf('1e-45')
    action = entropy([mp.mpf(1)/5]*5)
    assert abs(action-mp.mpf('0.793669645759747693179389532447')) < mp.mpf('1e-29')
    return {"full_phase_over_pi": str(full),
            "phase_gradient_over_pi": [str(g) for g in gradient],
            "absolute_action_at_unique_chamber_maximum": float(action),
            "scope": "actual real-source chamber; not a geometric cycle or knot-volume assertion"}


def main():
    result = {"exact_fields": [field_case(n) for n in (6, 7, 8, 9, 10, 12)],
              "complex_exact_ratios": complex_cases(), "symbolic": symbolic_phase()}
    path = Path(__file__).with_name('alternating_braid_real_phase_obstruction_results.json')
    path.write_text(json.dumps(result, indent=2)+'\n')
    print('PASS original-source alternating phase flux: '
          f"{sum(c['exact_whole_source_ratios'] for c in result['exact_fields'])} exact field ratios, "
          f"{len(result['complex_exact_ratios'])} complex ratios, symbolic full phase and entropy maximum")


if __name__ == '__main__':
    main()
