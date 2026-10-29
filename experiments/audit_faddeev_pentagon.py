#!/usr/bin/env python3
"""Independent scalar, Fourier and charged-pentagon normalization checks.

Numerics use the convergent modular-double product, whose identification
with the defining integral was checked separately. The identity being tested
is not used to evaluate any integral. These are diagnostics, not proofs.
"""

import json
from pathlib import Path

import mpmath as mp
import sympy as sp

from check_local_completion import phi_compact_quotient


def exact_charge_certificate():
    a0, a2, a4, c0, c4, C, Y, Z, t = sp.symbols("a0 a2 a4 c0 c4 C Y Z t")
    half = sp.Rational(1, 2)
    a = {0: a0, 2: a2, 4: a4, 1: a0 + a2, 3: a2 + a4}
    c = {0: c0, 4: c4, 1: c0 + a4, 3: a0 + c4, 2: c0 + a4 + a0 + c4}
    beta = {j: half - a[j] - c[j] for j in range(5)}

    def exponent(j, x):
        return -sp.Rational(1, 12) - C**2 * (4 * (c[j] - beta[j]) + 1) / 6 - 4 * C * c[j] * (x - C * (c[j] + beta[j]))

    uncharged_exponent = -(1 - 4 * C**2) / 12
    shift = -2 * C * a2
    Ybar, Zbar = Y + 2 * C * a[3], Z + 2 * C * a[1]
    difference = sp.expand(
        exponent(4, Y - t - shift) + exponent(2, t + shift) + exponent(0, Z - t - shift)
        + 2 * (Y - t - shift) * (Z - t - shift)
        - 3 * uncharged_exponent - 2 * (Ybar - t) * (Zbar - t))
    assert sp.diff(difference, t) == 0
    phase = sp.simplify(difference + 2 * uncharged_exponent - exponent(1, Z) - exponent(3, Y))
    Pe = 2 * (c0 + a2 + c4) - half
    assert sp.simplify(phase - C**2 * Pe / 3) == 0
    for j in range(5):
        assert sp.simplify(a[j] + c[j] + beta[j] - half) == 0
    return {"all_boundary_variables_symbolic": True,
            "integrand_ratio_independent_of_internal_variable": True,
            "phase_exponent_over_pi_i_cb_squared": str(Pe / 3)}


def main():
    mp.mp.dps = 38
    b = mp.mpc(".8", ".3")
    cb = 1j * (b + 1 / b) / 2
    zeta_o = mp.exp(mp.pi * 1j * (1 - 4 * cb**2) / 12)
    phi = lambda z: phi_compact_quotient(b, z)
    records = []
    probes = [
        (mp.mpc(".2", ".35"), mp.mpc("-.3", "-.25"), mp.mpc(".17", "-.2")),
        (mp.mpc("-.1", ".4"), mp.mpc(".14", "-.3"), mp.mpc("-.11", "-.26")),
        (mp.mpc(".08", ".3"), mp.mpc("-.19", "-.28"), mp.mpc(".08", "-.18")),
    ]
    for u, v, w in probes:
        assert mp.im(v + cb) > 0 and mp.im(cb - u) > 0
        assert mp.im(v - u) < mp.im(w) < 0
        integral = mp.quad(lambda x: phi(x + u) / phi(x + v) * mp.exp(2j * mp.pi * w * x),
                           [-42, -12, -4, 0, 4, 12, 42])
        expected = zeta_o * phi(u - v - cb) * phi(w + cb) / phi(u - v + w - cb) * mp.exp(-2j * mp.pi * w * (v + cb))
        error = abs(integral / expected - 1)
        assert error < mp.mpf("2e-16")
        records.append({"u": str(u), "v": str(v), "w": str(w), "relative_error": str(error)})

    def psi(a, c, x):
        nu = mp.exp(-mp.pi * 1j * cb**2 * (4 * (a - c) + 1) / 6)
        return nu * mp.exp(-4j * mp.pi * cb * a * (x - cb * (a + c))) / phi(x - 2 * cb * (a + c))

    def charged_kernel(a, c, x):
        beta = mp.mpf(".5") - a - c
        return mp.exp(-mp.pi * 1j / 12) * psi(c, beta, x)

    a_probe, c_probe, t_probe = mp.mpf(".12"), mp.mpf(".1"), mp.mpf(".21")
    fourier = mp.exp(-mp.pi * 1j * t_probe**2) * mp.quad(
        lambda x: psi(a_probe, c_probe, x) * mp.exp(-2j * mp.pi * t_probe * x),
        list(range(-42, 43, 3)))
    fourier_error = abs(fourier / charged_kernel(a_probe, c_probe, t_probe) - 1)
    assert fourier_error < mp.mpf("2e-16")

    a0, a2, a4 = map(mp.mpf, [".04", ".06", ".05"])
    c0, c4 = map(mp.mpf, [".07", ".08"])
    a = {0: a0, 2: a2, 4: a4, 1: a0 + a2, 3: a2 + a4}
    c = {0: c0, 4: c4, 1: c0 + a4, 3: a0 + c4, 2: c0 + a4 + a0 + c4}
    assert all(a[j] > 0 and c[j] > 0 and a[j] + c[j] < mp.mpf(".5") for j in range(5))
    Pe = 2 * (c0 + a2 + c4) - mp.mpf(".5")
    phase = mp.exp(mp.pi * 1j * cb**2 * Pe / 3)
    pentagon_records = []
    for Y, Z in [(mp.mpf(".23"), mp.mpf("-.18")), (mp.mpf("-.31"), mp.mpf(".27"))]:
        integral = mp.quad(
            lambda t: charged_kernel(a[4], c[4], Y - t) * charged_kernel(a[2], c[2], t)
            * charged_kernel(a[0], c[0], Z - t) * mp.exp(2j * mp.pi * (Y - t) * (Z - t)),
            [-18, -6, -2, 0, 2, 6, 18])
        expected = phase * charged_kernel(a[1], c[1], Z) * charged_kernel(a[3], c[3], Y)
        error = abs(integral / expected - 1)
        assert error < mp.mpf("2e-16")
        pentagon_records.append({"Y": str(Y), "Z": str(Z), "relative_error": str(error)})

    payload = {
        "source": "Andersen--Kashaev arXiv:1109.6295v2, equations (18), (20), (54), (56)",
        "b": str(b), "scope": "Finite numerical diagnostics and exact phase certificates for the independent proof.",
        "generic_ramanujan_integrals": records,
        "charged_fourier_relative_error": str(fourier_error),
        "charged_pentagon_generic_boundary_checks": pentagon_records,
        "exact_charge_certificate": exact_charge_certificate(),
    }
    destination = Path(__file__).with_name("faddeev_pentagon_results.json")
    destination.write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps({"ramanujan_cases": len(records), "charged_pentagon_cases": len(pentagon_records),
                      "max_relative_error": str(max([mp.mpf(r["relative_error"]) for r in records + pentagon_records]
                                                   + [fourier_error])),
                      "exact_phase_certificate_passed": True, "results": str(destination)}, indent=2))


if __name__ == "__main__":
    main()
