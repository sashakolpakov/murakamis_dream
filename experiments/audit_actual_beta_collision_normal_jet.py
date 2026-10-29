"""Audit the COMPLETE original beta collision jet, with no residue replacement.

The asymptotic proof is in notes/actual_beta_collision_normal_jet_obstruction.md.
Finite tests independently compare the Newton polynomial, its differentiated
products, the factorial sum, and the full actual three-star derivative.
"""
from pathlib import Path
import json
import mpmath as mp


def beta(u, v, n, q):
    p = mp.mpc(1)
    result = p
    for a in range(1, n):
        p *= u - q ** (a - 1) * v
        result += p
    return result


def beta_du(u, v, n, q):
    p, dp = mp.mpc(1), mp.mpc(0)
    result = dp
    for a in range(1, n):
        factor = u - q ** (a - 1) * v
        dp = dp * factor + p
        p *= factor
        result += dp
    return result


def jet(v, n, q):
    f = mp.mpc(1)
    result = f
    for k in range(1, n - 1):
        f *= 1 - q ** k
        result += f * v ** k
    return result


def close(x, y, tol=mp.mpf("1e-65")):
    err = abs(x-y) / max(1, abs(x), abs(y))
    assert err < tol, (mp.nstr(x, 30), mp.nstr(y, 30), mp.nstr(err, 10))


def main():
    mp.mp.dps = 100
    c0 = mp.exp(-mp.j * mp.pi / 3)
    gamma = mp.im(mp.polylog(2, mp.exp(mp.j * mp.pi / 3))) / (2 * mp.pi)
    finite = []
    for n in (2, 3, 4, 5, 6, 7, 8, 11, 16, 23, 32):
        q = mp.exp(2 * mp.j * mp.pi / n)
        for c in (c0, mp.mpc("0.7", "0.2"), mp.mpc("-0.3", "0.8")):
            close(beta(c, c, n, q), 1)
            close(beta_du(c, c, n, q), jet(c, n, q))
            close(mp.diff(lambda v: beta(c, v, n, q), c), -jet(c, n, q))
            a, b = mp.mpc("0.23", "0.17"), mp.mpc("0.31", "-0.11")
            base = beta(1, a, n, q) * beta(1, b, n, q)
            lhs = mp.diff(lambda u: beta(u, a, n, q) * beta(1, b, n, q)
                          * beta(c, c*u, n, q), mp.mpf(1)) / base
            rhs = beta_du(1, a, n, q) / beta(1, a, n, q) - c*jet(c, n, q)
            close(lhs, rhs)
        finite.append(n)

    # Exact Plancherel formula by a mesh exceeding twice the polynomial degree.
    parseval = []
    for n in (2, 3, 5, 8, 13):
        q = mp.exp(2 * mp.j * mp.pi / n)
        a = mp.mpc("0.4", "-0.2")
        lhs = mp.fsum(abs(a - (z := mp.exp(2*mp.j*mp.pi*k/(2*n+1)))
                          * jet(z, n, q))**2 for k in range(2*n+1)) / (2*n+1)
        f = mp.mpc(1)
        rhs = abs(a)**2 + 1
        for k in range(1, n-1):
            f *= 1-q**k
            rhs += abs(f)**2
        close(lhs, rhs)
        parseval.append(n)

    # Both parities and nonmultiples of six: no hidden root/parity anchor.
    saddle = []
    for n in (48, 65, 96, 127, 192, 257, 384, 513, 768):
        q = mp.exp(2 * mp.j * mp.pi / n)
        actual = jet(c0, n, q)
        ref = mp.j*n*mp.exp(n*gamma - 25*mp.j*mp.pi*n/72)
        ratio = actual/ref
        assert abs(ratio-1) < mp.mpf("1.0")/n, (n, ratio)
        theta = 6*mp.pi/5
        shifted = jet(c0*mp.exp(mp.j*theta/n), n, q)/actual
        assert abs(shifted+1) < mp.mpf("12.0")/n, (n, shifted)
        factorial, energy = mp.mpc(1), mp.mpf(1)
        for k in range(1, n-1):
            factorial *= 1-q**k
            energy += abs(factorial)**2
        energy_ref = n**mp.mpf("1.5")/mp.root(3, 4)*mp.exp(2*n*gamma)
        energy_ratio = energy/energy_ref
        assert abs(energy_ratio-1) < mp.mpf("1.0")/n, (n, energy_ratio)
        saddle.append({"N":n, "ratio_re":float(mp.re(ratio)),
                       "ratio_im":float(mp.im(ratio)),
                       "N_scaled_error":float(n*abs(ratio-1)),
                       "two_point_flip_error":float(abs(shifted+1)),
                       "positive_energy_ratio":float(energy_ratio),
                       "log_rate":float(mp.log(abs(actual))/n)})
    result = {"status":"PASS", "finite_levels":finite,
              "parseval_levels":parseval, "gamma":str(gamma), "saddle":saddle}
    target = Path(__file__).with_suffix(".json")
    target.write_text(json.dumps(result, indent=2)+"\n")
    print("PASS: 33 exact beta jets/three-star derivatives; 5 Plancherel identities; "
          "9 mixed-parity saddle, normal-shift, and positive-energy tests")
    print("gamma =", mp.nstr(gamma, 25))
    print("results:", target)


if __name__ == "__main__":
    main()
