#!/usr/bin/env python3
"""Compare the combined trace identity with the original physical jets."""
from pathlib import Path
import hashlib
import json

import mpmath as mp


def main():
    mp.mp.dps = 100
    root = Path(__file__).resolve().parents[1]
    count = {"trace_identities": 0, "normal_commutators": 0,
             "even_operator_identities": 0, "cardinal_identities": 0,
             "gram_kernel_identities": 0, "integral_normalizations": 0,
             "odd_weighted_trace_identities": 0,
             "odd_weighted_operator_identities": 0,
             "transport_identities": 0, "interpolation_outputs": 0,
             "signed_time_integrals": 0,
             "full_period_identities": 0, "full_period_coercivity": 0}
    worst = mp.mpf(0)

    def check(x, y, group):
        nonlocal worst
        error = abs(x-y)/max(1, abs(x), abs(y))
        worst = max(worst, error)
        assert error < mp.mpf("1e-75"), (group, x, y, error)
        count[group] += 1

    for N in range(2, 19):
        theta, eta, last = mp.pi/N, (-1)**(N-1), (N-1)//2
        size = last+1
        nodes = [2*mp.cos((2*a+1)*theta) for a in range(size)]
        if N % 2:
            nodes[-1] = mp.mpf(-2)
        double = range(size-(N % 2))
        weights = [4-x*x for x in nodes]
        lam = [1/mp.fprod(x-y for b, y in enumerate(nodes) if b != a)
               for a, x in enumerate(nodes)]
        D = mp.matrix(size)
        for a in range(size):
            for b in range(size):
                D[a, b] = (mp.fsum(1/(nodes[a]-nodes[k])
                                    for k in range(size) if k != a)
                           if a == b else
                           lam[b]/(lam[a]*(nodes[a]-nodes[b])))
        factorial = [mp.mpf(1)]
        for k in range(1, size):
            factorial.append(factorial[-1]*2*mp.sin(k*theta))

        def ej(j, z):
            return mp.fprod(nodes[b]-z for b in range(j))/factorial[j]**2

        def low(z):
            return mp.fsum(ej(k, z)*ej(k, -2) for k in range(size))

        F = mp.matrix([low(x) for x in nodes])
        for a in double:
            check(mp.diff(low, nodes[a]), (D*F)[a], "normal_commutators")

        A = mp.diag(weights)
        if N % 2 == 0:
            B = A*D-mp.diag([x/2 for x in nodes])
            sigma = [2*(-1)**a*mp.sin((2*a+1)*theta)
                     for a in range(size)]
            for a in range(size):
                for b in range(size):
                    target = (mp.mpf(0) if a == b else
                              sigma[a]*sigma[b]/(nodes[a]-nodes[b]))
                    check(B[a, b], target, "cardinal_identities")

        for n in (-3, 0, 1, 3, 4):
            const = mp.exp(1j*mp.pi*n*(N-1)**2/(4*N))

            def phase(z):
                return n*N*mp.acos(-z/2)**2/(4*mp.pi)

            def crossing(z):
                return const*mp.exp(1j*phase(z))

            def h(z):
                return crossing(z)*low(z)

            rv = mp.matrix([crossing(x) for x in nodes])
            R = mp.diag(list(rv))
            phase_derivative = [n*N*mp.acos(-x/2)
                                /(4*mp.pi*mp.sqrt(1-x*x/4))
                                if x != -2 else n*N/(4*mp.pi)
                                for x in nodes]
            gamma = (mp.diag([1j*phase_derivative[a]*rv[a]
                              for a in range(size)])+R*D-D*R)
            defects = gamma*F
            hv = R*F
            for a in double:
                check(mp.diff(h, nodes[a])-(D*hv)[a],
                      defects[a], "normal_commutators")

            if N % 2 == 0:
                H = A*mp.diag(phase_derivative)+(B-R.H*B*R)/1j
                for a in range(size):
                    for b in range(size):
                        check(H[a, b], mp.conj(H[b, a]),
                              "even_operator_identities")
                        if a == b:
                            gram = sigma[a]**2*phase_derivative[a]
                        else:
                            diff = phase(nodes[a])-phase(nodes[b])
                            gram = (sigma[a]*sigma[b]
                                    *2*mp.sin(diff/2)/(nodes[a]-nodes[b])
                                    *mp.exp(-1j*diff/2))
                        check(H[a, b], gram, "gram_kernel_identities")

            for j in range(size):
                def p(z):
                    return ej(j, z)

                def product(z):
                    return h(z)*p(z)

                pv = mp.matrix([p(x) for x in nodes])
                original = eta*mp.fsum(
                    weights[a]*mp.diff(product, nodes[a])
                    -nodes[a]*product(nodes[a]) for a in double)
                if N % 2:
                    original += product(-2)
                combined = eta*mp.fsum(
                    weights[a]*defects[a]*pv[a] for a in double)
                if N % 2:
                    combined += (N*N*mp.fsum(lam[a]*hv[a] for a in range(size))
                                 *mp.fsum(lam[a]*pv[a] for a in range(size)))
                check(original, combined, "trace_identities")
                if N % 2 == 0:
                    operator = 1j*eta*(pv.T*R*H*F)[0]
                    check(original, operator, "even_operator_identities")

        if N % 2:
            double_nodes = nodes[:-1]
            dsize = len(double_nodes)
            plus_weights = [(x+2)*(4-x*x) for x in double_nodes]
            plus_lam = [1/mp.fprod(x-y for b, y in enumerate(double_nodes)
                                  if b != a)
                        for a, x in enumerate(double_nodes)]
            plus_sigma = [N*v for v in plus_lam]
            plus_D = mp.matrix(dsize)
            for a in range(dsize):
                check(plus_weights[a], plus_sigma[a]**2,
                      "odd_weighted_operator_identities")
                for b in range(dsize):
                    plus_D[a, b] = (
                        mp.fsum(1/(double_nodes[a]-double_nodes[k])
                                for k in range(dsize) if k != a)
                        if a == b else
                        plus_lam[b]/(plus_lam[a]
                                     *(double_nodes[a]-double_nodes[b])))
            plus_A = mp.diag(plus_weights)
            plus_B = plus_A*plus_D+mp.diag(
                [(4-2*x*x-2*x)/2 for x in double_nodes])
            for a in range(dsize):
                for b in range(dsize):
                    target = (mp.mpf(0) if a == b else
                              plus_sigma[a]*plus_sigma[b]
                              /(double_nodes[a]-double_nodes[b]))
                    check(plus_B[a, b], target,
                          "odd_weighted_operator_identities")

            def plus_l(z):
                return mp.fsum(ej(k, z)*ej(k, -2) for k in range(dsize))

            plus_F = mp.matrix([plus_l(x) for x in double_nodes])
            for n in (-3, 0, 1, 3, 4):
                const = mp.exp(1j*mp.pi*n*(N-1)**2/(4*N))

                def plus_crossing(z):
                    return const*mp.exp(1j*n*N*mp.acos(-z/2)**2/(4*mp.pi))

                plus_R = mp.diag([plus_crossing(x) for x in double_nodes])
                plus_phase_derivative = [
                    n*N*mp.acos(-x/2)/(4*mp.pi*mp.sqrt(1-x*x/4))
                    for x in double_nodes]
                plus_H = (plus_A*mp.diag(plus_phase_derivative)
                          +(plus_B-plus_R.H*plus_B*plus_R)/1j)
                for a in range(dsize):
                    for b in range(dsize):
                        check(plus_H[a, b], mp.conj(plus_H[b, a]),
                              "odd_weighted_operator_identities")
                for j in range(dsize):
                    def weighted_product(z):
                        return (z+2)*plus_crossing(z)*plus_l(z)*ej(j, z)
                    original = mp.fsum(
                        (4-x*x)*mp.diff(weighted_product, x)
                        -x*weighted_product(x) for x in double_nodes)
                    pv = mp.matrix([ej(j, x) for x in double_nodes])
                    operator = 1j*(pv.T*plus_R*plus_H*plus_F)[0]
                    check(original, operator, "odd_weighted_trace_identities")

        # Independent normalization of the positive divided-difference measure.
        for x, y in ((mp.mpf(-2), mp.mpf(-2)),
                     (nodes[0], mp.mpf(-1))):
            # s=2*cosh(u) converts the improper integral into a smooth one.
            integral = mp.quad(
                lambda u: 4*u*mp.sinh(u)
                /((2*mp.cosh(u)-x)*(2*mp.cosh(u)-y)),
                [0, 1, 4, mp.inf])
            expected = (mp.mpf(1) if x == y == -2 else
                        (mp.acos(-x/2)**2-mp.acos(-y/2)**2)/(x-y))
            check(integral, expected, "integral_normalizations")

        # The same observation formula applies to the entire even space
        # and the literal weighted odd space. Keep its carrier in the trace.
        obs_nodes = nodes if N % 2 == 0 else double_nodes
        obs_sigma = sigma if N % 2 == 0 else plus_sigma
        obs_B = B if N % 2 == 0 else plus_B
        obs_A = A if N % 2 == 0 else plus_A
        obs_l = low if N % 2 == 0 else plus_l
        obs_F = mp.matrix([obs_l(x) for x in obs_nodes])
        obs_size = len(obs_nodes)
        times = [N*mp.acos(-x/2)**2/(4*mp.pi) for x in obs_nodes]
        time_derivative = [N*mp.acos(-x/2)/(4*mp.pi*mp.sqrt(1-x*x/4))
                           for x in obs_nodes]
        G = mp.matrix(obs_size)
        for a in range(obs_size):
            for b in range(obs_size):
                G[a, b] = (obs_sigma[a]**2*time_derivative[a] if a == b
                           else obs_sigma[a]*obs_sigma[b]*(times[a]-times[b])
                           /(obs_nodes[a]-obs_nodes[b]))

        def U(t):
            return mp.diag([mp.exp(1j*t*v) for v in times])

        def H(t):
            u = U(t)
            return t*obs_A*mp.diag(time_derivative)+(obs_B-u.H*obs_B*u)/1j

        for n, pwr in ((mp.mpf(1), mp.mpf(2)),
                       (mp.mpf(1)/3, mp.mpf(5)/4)):
            cocycle = H(n)+U(n).H*H(pwr)*U(n)
            for a in range(obs_size):
                for b in range(obs_size):
                    check(H(n+pwr)[a, b], cocycle[a, b], "transport_identities")

        period = N if N % 2 == 0 else 2*N
        full = H(period)
        translated = H(mp.mpf(2)/3+period)
        expected_translate = H(mp.mpf(2)/3)+period*mp.diag(
            [G[a, a] for a in range(obs_size)])
        for a in range(obs_size):
            for b in range(obs_size):
                target = period*G[a, a] if a == b else mp.mpf(0)
                check(full[a, b], target, "full_period_identities")
                check(translated[a, b], expected_translate[a, b],
                      "full_period_identities")
                if a != b:
                    cycles = (times[a]-times[b])*period/(2*mp.pi)
                    check(cycles, mp.nint(cycles), "full_period_identities")
                    assert mp.nint(cycles) != 0
            lower = mp.mpf(2) if N % 2 == 0 else mp.mpf(128)/(N*N)
            assert mp.re(full[a, a]) >= lower-mp.mpf("1e-75")
            count["full_period_coercivity"] += 1

        for t in (mp.mpf(0), mp.mpf(1)/3, mp.mpf(3)):
            z = mp.mpf(13)/4+mp.j/5
            Qz = mp.fprod(z-x for x in obs_nodes)
            interpolated = mp.fsum(
                mp.exp(1j*t*times[a])*obs_F[a]
                *mp.fprod((z-obs_nodes[b])/(obs_nodes[a]-obs_nodes[b])
                          for b in range(obs_size) if b != a)
                for a in range(obs_size))
            observed = mp.fsum(obs_sigma[a]*mp.exp(1j*t*times[a])*obs_F[a]
                              /(z-obs_nodes[a]) for a in range(obs_size))
            check(observed, N*interpolated/Qz, "interpolation_outputs")

        if N in (4, 5, 8, 9):
            for n in (1, 3):
                carrier = mp.exp(1j*mp.pi*n*(N-1)**2/(4*N))
                for j in range(obs_size):
                    pv = [ej(j, x) for x in obs_nodes]

                    def time_integrand(t):
                        return mp.fsum(
                            pv[a]*mp.exp(1j*(n-t)*times[a])*G[a, b]
                            *mp.exp(1j*t*times[b])*obs_F[b]
                            for a in range(obs_size) for b in range(obs_size))

                    convolution = 1j*((-1)**(N-1))*carrier*mp.quad(
                        time_integrand, [0, n/2, n])

                    def original_product(z):
                        crossing_value = carrier*mp.exp(
                            1j*n*N*mp.acos(-z/2)**2/(4*mp.pi))
                        value = crossing_value*obs_l(z)*ej(j, z)
                        return value if N % 2 == 0 else (z+2)*value

                    original = ((-1)**(N-1))*mp.fsum(
                        (4-x*x)*mp.diff(original_product, x)
                        -x*original_product(x) for x in obs_nodes)
                    check(original, convolution, "signed_time_integrals")

    paths = [Path(__file__).resolve(),
             root/"notes/research_trace_normal_defect_positive_form.md",
             root/"notes/research_exact_complete_trace_contour.md",
             root/"notes/research_pair_triangular_normal_region.md"]
    result = {
        "status": "passed",
        "precision_decimal": mp.mp.dps,
        "levels": [2, 18],
        "powers": [-3, 0, 1, 3, 4],
        **count,
        "maximum_relative_error": mp.nstr(worst, 22),
        "scope": "Exact identities at both parities; positivity has a written integral proof.",
        "sha256": {str(path.relative_to(root)): hashlib.sha256(path.read_bytes()).hexdigest()
                   for path in paths},
    }
    output = root/"repro/results/research-trace-normal-defect-positive-form.json"
    output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({key: value for key, value in result.items() if key != "sha256"}))


if __name__ == "__main__":
    main()
