#!/usr/bin/env python3
"""Exact classification identities and actual inverse-turn frame checks."""
import argparse
import json
from pathlib import Path

import mpmath as mp
import sympy as sp


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path(__file__).with_name(
        "audit_actual_matching_edge_real_target_frames_results.json"))
    args = parser.parse_args()
    count = {"formal_identities": 0, "actual_local_frames": 0,
             "both_adapter_rows": 0, "nonconjugate_support_failures": 0,
             "exact_generic_bandwidth_entries": 0}

    def zero(x):
        assert sp.factor(x) == 0, sp.factor(x)
        count["formal_identities"] += 1

    J, e = sp.symbols("J e", nonzero=True)
    p = (e**2-1/J)/(J-1/J)
    kap = -(J-1)**2/(J+1)**2
    a, d = -2*J/(J+1), -2/(J+1)
    k, c = -(J+1)**2/(4*J), -(e+1/e)/2
    zero((a*p+d*(1-p))/e+c/k)
    zero(kap*p*(1-p)/e**2-(c*c+k)/(4*k*k))

    k, c, M = sp.symbols("k c M", positive=True)
    L2 = (c*c+k)/k**2
    a2 = c*c*M*(1+k)/(c*c+k)
    norm = c*c/k**2-2*c*c*M/k**2 + L2*(
        M*(a2+k*(1-a2))/(1+k)
        +(M-1)*((1-a2)+k*a2)/(1+k))
    M0 = k/(1-c*c)+1/(1+k)
    zero(norm-(1-c*c)*(M*k+M-1)/(k*(1+k)))
    zero((norm-1).subs(M, M0))
    delta = 1-c*c*(k+2)
    zero((1-a2).subs(M, M0)-k*delta/((1-c*c)*(c*c+k)))
    mean = c*(M-1)/k
    half2 = L2*M*(1-a2)*k/(1+k)
    bracket = c**4*(k+2)-2*c*c+k*k+k+1
    zero(((c-mean)**2-half2).subs(M, M0)
         +delta*bracket/((1-c*c)**2*(1+k)**2))
    rho = sp.symbols("rho", real=True)
    anti_norm = rho*rho+k*(rho+c/k)**2-L2*k/(1+k)
    zero((1+k)*(anti_norm-1)-((1+k)*rho+c)**2+k+2)

    # Check (5) before applying the second-branch constraint. Rational
    # parametrizations enforce both circle and hyperbola identities.
    x, y, z, L, d0 = sp.symbols("x y z L d0", real=True)
    ca, sa = (1-x*x)/(1+x*x), 2*x/(1+x*x)
    cb, sb = (1-y*y)/(1+y*y), 2*y/(1+y*y)
    ch, sh = (z+1/z)/2, (z-1/z)/2
    re1, re2 = d0+L*ch*(ca*cb+sa*sb), d0+L*ch*(ca*cb-sa*sb)
    im1, im2 = L*sh*(sa*cb-ca*sb), L*sh*(sa*cb+ca*sb)
    zero(re1**2+im1**2-re2**2-im2**2-4*L*sa*sb*(d0*ch+L*cb*ca))

    # Exact generic tridiagonal polynomial band; this also certifies
    # every retained jet of the identically zero entries.
    h = sp.symbols("h")
    for t in range(2, 8):
        mat = sp.zeros(t+1)
        for i in range(t+1):
            mat[i, i] = i+1+h*(i+2)
            if i < t:
                mat[i, i+1] = 2+i+h
                mat[i+1, i] = 1+i-h
        for deg in range(1, min(4, t)):
            pol = sp.eye(t+1)
            for n in range(1, deg+1):
                pol += (1+h)**n * mat**n
            for u in range(t+1):
                for v in range(t+1):
                    if abs(u-v) > deg:
                        assert pol[u, v] == 0
                        count["exact_generic_bandwidth_entries"] += 1

    mp.mp.dps = 70
    tol = mp.mpf("1e-60")
    maxerr = mp.mpf(0)

    def close(x, y=0):
        nonlocal maxerr
        er = abs(x-y)
        maxerr = max(maxerr, er)
        assert er < tol, er

    def tr(m):
        return m[0, 0]+m[1, 1]

    def mclose(m, n):
        for i in range(2):
            for j in range(2):
                close(m[i, j], n[i, j])

    I = mp.eye(2)
    old_a = mp.matrix([[-1, -1], [0, -1]])
    old_b = mp.matrix([[-1, 0], [4, -1]])
    for s in (mp.mpf(".1"), mp.mpf(".4"), mp.mpf(".8"),
              mp.mpf("1.2"), mp.mpf(2), mp.mpf(4)):
        kk = s*s
        eta = mp.asinh(s)
        jj = -mp.exp(-2*eta)
        rr = (1+1j*s)/(1-1j*s)
        collar_b = -1j*mp.sqrt(1+kk)/2
        collar = I+collar_b*(old_b*old_a+I)
        old_ao = collar*old_a*collar**-1
        old_bo = collar*old_b*collar**-1
        target_t = old_b**-1*old_bo
        actual_in, actual_out = old_ao**-1, old_bo
        basis = mp.matrix([[target_t[0, 1], target_t[0, 1]],
                           [jj-target_t[0, 0], 1/jj-target_t[0, 0]]])
        first = basis**-1*actual_in*basis
        basis = basis*mp.matrix([[first[0, 1], 0], [0, 1]])
        kap = -(jj-1)**2/(jj+1)**2
        aa, dd = -2*jj/(jj+1), -2/(jj+1)
        canonical = mp.matrix([[aa, 1], [kap, dd]])
        mclose(basis**-1*actual_in*basis, canonical)
        mclose(basis**-1*actual_out*basis,
               mp.matrix([[aa, rr], [kap/rr, dd]]))
        low = -1/mp.sqrt(kk+2)
        high = min(mp.mpf(1), kk+1-mp.sqrt(kk+2))
        for frac in (mp.mpf(".2"), mp.mpf(".5"), mp.mpf(".8")):
            cc = low+frac*(high-low)
            tau = mp.acos(-cc)/mp.pi
            rho = (-mp.sqrt(kk+2)-cc)/(1+kk)
            assert -1 < rho < cc
            zin = rho+1j*mp.sqrt(1-rho*rho)
            zout = mp.conj(zin)
            rhs1, rhs2 = zin+cc/kk, zout+cc/kk
            xx = (rhs2-rhs1/rr)/(rr-1/rr)
            yy = rhs1-xx
            close(xx*yy, (cc*cc+kk)/(4*kk*kk))
            nu = (tau-1)/2+mp.acos(rho)/(2*mp.pi)
            omega = tau-nu
            assert 0 < nu < tau/2 < omega < tau
            assert 0 < omega-nu < mp.mpf(".5")
            for adapter in (-1, 1):
                ee = mp.exp(adapter*1j*mp.pi*tau)
                pp = (ee*ee-1/jj)/(jj-1/jj)
                proj = mp.matrix([[pp, ee*yy/kap], [ee*xx, 1-pp]])
                mclose(proj*proj, proj)
                actual_proj = basis*proj*basis**-1
                close(tr(actual_in*actual_proj)/ee, zin)
                close(tr(actual_out*actual_proj)/ee, zout)
                old_proj = old_ao**-1*actual_proj/tr(old_ao**-1*actual_proj)
                pulled = old_ao*old_proj/tr(old_ao*old_proj)
                mclose(pulled, actual_proj)
                for val, expected in ((zin, omega), (zout, nu)):
                    # The physical high-to-low adapter reverses the
                    # total, but the normalized exponent is identical.
                    u_phys = -1/(ee*val)
                    u_low = u_phys if adapter == -1 else u_phys*ee**2
                    close(u_low, mp.exp(2j*mp.pi*expected))
                    count["both_adapter_rows"] += 1
                count["actual_local_frames"] += 1

        # Explicit other-branch points: actual unit rows exist, but
        # cannot BOTH satisfy the strict physical real-part test.
        for ratio in (mp.mpf("-.8"), mp.mpf("-.3"), mp.mpf(0),
                      mp.mpf(".3"), mp.mpf(".8")):
            cc = ratio/mp.sqrt(kk+2)
            mm = kk/(1-cc*cc)+1/(1+kk)
            coschi = cc*mp.sqrt(mm*(1+kk)/(cc*cc+kk))
            chi = mp.acos(coschi)
            sigma = mp.acosh(mp.sqrt(mm))
            beta = mp.atan(s)
            ll = mp.sqrt(cc*cc+kk)/kk
            z1 = -cc/kk+ll*(mp.cosh(sigma)*mp.cos(chi-beta)
                              +1j*mp.sinh(sigma)*mp.sin(chi-beta))
            z2 = -cc/kk+ll*(mp.cosh(sigma)*mp.cos(chi+beta)
                              +1j*mp.sinh(sigma)*mp.sin(chi+beta))
            close(abs(z1), 1)
            close(abs(z2), 1)
            assert (cc-mp.re(z1))*(cc-mp.re(z2)) < 0
            count["nonconjugate_support_failures"] += 1

    result = {"status": "PASS", **count, "max_numeric_error": str(maxerr),
              "scope": "local actual real target frames; no global selected-frame claim"}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
