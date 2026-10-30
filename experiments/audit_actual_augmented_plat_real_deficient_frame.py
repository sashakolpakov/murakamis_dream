#!/usr/bin/env python3
"""Exact circle/branch algebra and original marked disk-frame checks."""
import argparse
import json
from pathlib import Path
import mpmath as mp
import sympy as sp


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path(__file__).with_name(
        "audit_actual_augmented_plat_real_deficient_frame_results.json"))
    args = parser.parse_args()
    counts = {"exact_circle_and_branch_identities": 0,
              "actual_marked_disk_frames": 0, "actual_geometric_characteristics": 0}

    def zero(f):
        assert sp.simplify(sp.factor(f)) == 0, sp.factor(f)
        counts["exact_circle_and_branch_identities"] += 1

    X, r, d, a, b, R = sp.symbols("X r d a b R", real=True)
    w = X+sp.I*(r-d/2)
    w0bar = 1-X-sp.I*(r+d/2)
    real = -X*X+X+a*a-a+(r-b)**2-d*d/4-R*R
    imag = (r-b)*(1-2*X)+(a-sp.Rational(1, 2))*d
    zero((w-a-sp.I*b)*(w0bar-a+sp.I*b)-R*R-real-sp.I*imag)
    a2, b2, R2 = sp.symbols("a2 b2 R2", real=True)
    real2 = real.subs({a: a2, b: b2, R: R2})
    imag2 = imag.subs({a: a2, b: b2, R: R2})
    polar = sp.expand(imag*real2-real*imag2)
    zero(polar.coeff(X, 3)-2*(b2-b))
    zero(sp.expand(polar.subs(b2, b)).coeff(X, 2)-d*(a2-a))
    zero(polar.subs({b2: b, a2: a})-(R*R-R2*R2)*imag)
    zero(sp.im((1-sp.I*d)*sp.conjugate(1+sp.I*d))+2*d)

    # Local ORIGINAL traces and determinant coordinates, with output
    # disk normalization retained separately.
    H = sp.symbols("H", real=True)
    A = sp.Matrix([[-1, 0], [-2, -1]])
    P = sp.Matrix([[-1, -2], [0, -1]])
    C = sp.Matrix([[1, sp.I*H], [0, 1]])
    Ao = C*A*C.inv()
    z = X-1+sp.I*(r+d/2)
    Pi = sp.Matrix([[z, -z*w], [1, -w]])/(z-w)
    a1, aout, p = sp.trace(A*Pi), sp.trace(Ao*Pi), sp.trace(P*Pi)
    zero(p-(1+sp.I*d)/(1-sp.I*d))
    L = 2*X-1
    n = (L*L+1+d*d-4*r*r)/2+2*sp.I*r*L
    no = n.subs(r, r-H)
    zero(a1-n/(-1+sp.I*d))
    zero(aout-no/(-1+sp.I*d))
    zero(1-2*n/(1+d*d)+(L+2*sp.I*r)**2/(1+d*d))
    zero(1-2*no/(1+d*d)+(L+2*sp.I*(r-H))**2/(1+d*d))

    aa = sp.symbols("aa")
    T = (1+sp.I*d)/(1-sp.I*d)
    U = 2*(1+sp.I*d)/(aa*aa+1+d*d)
    for zz, sign in ((-1/(aa+sp.I*d), -1), (1/(aa-sp.I*d), 1)):
        Y = -(1-U)*(T*zz+U)/((U-zz)*(T-U))
        expected = (aa*aa+1+d*d+sign*2*aa)/(aa*aa+1+d*d-sign*2*aa)
        zero(Y-expected)
        crit = T*(-1-zz)**2*(U-zz)+(zz-1)**2*(T*zz+U)
        zero(crit)

    mp.mp.dps = 75
    dd = 1/mp.sqrt(3)
    sigma = mp.mpf(1)/6
    cc = mp.cos(mp.pi*sigma)
    worst = mp.mpf(0)

    def close(x, y=0):
        nonlocal worst
        err = abs(x-y)
        worst = max(worst, err)
        assert err < mp.mpf("1e-62"), err

    def tr(m):
        return m[0, 0]+m[1, 1]

    A = mp.matrix([[-1, 0], [-2, -1]])
    P = mp.matrix([[-1, -2], [0, -1]])
    for height in (mp.mpf(1), mp.mpf("1.5"), mp.mpf(3)):
        C = mp.matrix([[1, 1j*height], [0, 1]])
        Ao = C*A*C**-1
        for fraction in (mp.mpf(".2"), mp.mpf(".5"), mp.mpf(".8")):
            mid = dd/2+fraction*(height-dd)
            for xx in (mp.mpf(100), mp.mpf(300)):
                ww = xx+1j*(mid-dd/2)
                zz = xx-1+1j*(mid+dd/2)
                proj = mp.matrix([[zz, -zz*ww], [1, -ww]])/(zz-ww)
                p = tr(P*proj)
                close(abs(p), 1)
                close(p, mp.exp(2j*mp.pi*sigma))
                ain, aout = tr(A*proj), tr(Ao*proj)
                Uin, Uout = -p/ain, -p/aout
                rin, rout = mp.log(Uin)/(2j*mp.pi), mp.log(Uout)/(2j*mp.pi)
                assert 0 < mp.re(rin) < sigma and 0 < mp.re(rout) < sigma
                assert mp.im(rin) > 1 and mp.im(rout) > 1
                assert mp.re(rout-rin) > 0
                ell = 2*xx-1
                for u, midpoint, root, mode in (
                    (Uin, mid, -1/(ell+2j*(mid+dd/2)), -1),
                    (Uout, mid-height, 1/(ell+2j*(mid-height-dd/2)), 1)):
                    zd = mp.exp(1j*mp.pi*sigma)/u
                    expected = cc*((ell*ell+1+dd*dd-4*midpoint*midpoint)/2
                                   +2j*midpoint*ell)
                    close(zd, expected)
                    assert (-mode)*mp.im(zd) > 0
                    sq = (-1j if mode == -1 else 1j)*cc*(ell+2j*midpoint)
                    close(sq*sq, 1-2*cc*zd)
                    assert mp.re(sq) > 0
                    Ygeo = -(1-u)*(p*root+u)/((u-root)*(p-u))
                    Ycontinued = (zd-1j*sq)**2/(1-2*cc*zd+zd*zd)
                    close(Ygeo, Ycontinued)
                    counts["actual_geometric_characteristics"] += 1
                counts["actual_marked_disk_frames"] += 1

    result = {"status": "PASS", **counts, "max_numeric_error": str(worst),
              "scope": "exact circle regularity and actual marked branch interface; global convex-cut existence is proved in text; no finite second-chamber asymptotic"}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
