#!/usr/bin/env python3
"""Original three-crossing Fourier/shift checks and finite diagnostics.

Positive and negative columns use original multiplication and triangular
solves, respectively. Exact checks concern the parity seam and Fourier
transport. Finite asymptotic ratios are recorded, never used as proofs.
"""

import argparse
import hashlib
import json
from pathlib import Path

import mpmath as mp

from check_even_reflected_casimir_insertions import (
    apply_power, norm, original_crossing,
)


ROOT = Path(__file__).resolve().parents[1]


def fourier(vector, mode):
    N = len(vector)
    return mp.fsum(vector[j]*mp.exp(-2j*mp.pi*mode*j/N)
                   for j in range(N))/mp.sqrt(N)


def shift(vector):
    return [vector[-1]] + vector[:-1]


def encode(value):
    return {"real":mp.nstr(mp.re(value),30),
            "imag":mp.nstr(mp.im(value),30)}


def relative(left, right):
    return abs(left-right)/max(1,abs(left),abs(right))


def run(precision):
    mp.mp.dps = precision
    threshold = mp.mpf(10)**(-precision//2)
    records = []
    worst = mp.mpf(0)
    exact_checks = 0
    a = mp.pi*mp.sqrt(3)
    constant = (2/mp.sqrt(3))**mp.mpf(".25")
    # J(5/6) = Im Li_2(exp(pi i/3))/(2 pi).
    J0 = mp.im(mp.polylog(2,mp.exp(mp.pi*1j/3)))/(2*mp.pi)
    for N in (2,3,6,7,32,33,64,65,128,129):
        q = mp.exp(mp.pi*1j/N)
        Q = q*q
        kappa = mp.exp(mp.pi*1j*(N-1)**2/(2*N))
        omega = mp.exp(mp.pi*1j*(mp.mpf(1)/4+mp.mpf(1)/(4*N)-mp.mpf(N)/12))
        M = original_crossing(N)
        unit = [mp.mpc(1)] + [mp.mpc(0)]*(N-1)
        g = [mp.mpf(1)]
        for j in range(1,N):
            g.append(g[-1]*4*mp.sin(mp.pi*j/N)**2)
        ng = norm(g)
        u = [z/ng for z in g]
        modes = sorted(set([0,1,-1]+[int(mp.nint(t*mp.sqrt(N)))
                                    for t in (mp.mpf("-.75"),mp.mpf("-.25"),
                                              mp.mpf(".25"),mp.mpf(".75"))]))
        for sign in (1,-1):
            alpha = apply_power(M,unit,3*sign)
            chirp = [q**(sign*j*(j+2)) for j in range(N)]
            beta = [alpha[j]/(kappa**(3*sign)*chirp[j]) for j in range(N)]
            nbeta = norm(beta)
            v = [z/(omega**sign*nbeta) for z in beta]
            # Independent expressions for the literal dechirped turn.
            turned = [chirp[N-1-j]*v[N-1-j]/chirp[j] for j in range(N)]
            turned_expected = [
                (-1)**N*q**(-sign)*Q**(-sign*j)*v[N-1-j]
                for j in range(N)
            ]
            for actual, expected in zip(turned,turned_expected):
                err = relative(actual,expected)
                worst = max(worst,err)
                exact_checks += 1
                assert err < threshold
            # The conjugated cyclic shift has a distinct odd-level wrap.
            physical = [chirp[j]*v[j] for j in range(N)]
            conjugated = [chirp[j]*shift(v)[j] for j in range(N)]
            explicit = [(-1)**N*q**sign*physical[-1]]
            explicit += [q**(sign*(2*j+1))*physical[j-1] for j in range(1,N)]
            for actual, expected in zip(conjugated,explicit):
                err = relative(actual,expected)
                worst = max(worst,err)
                exact_checks += 1
                assert err < threshold
            err = relative(norm(conjugated),norm(physical))
            worst = max(worst,err)
            exact_checks += 1
            assert err < threshold

            mode_rows = []
            for m in modes:
                fv = fourier(v,m)
                ft = fourier(turned,m)
                ft_expected = ((-1)**N*q**(-sign)*Q**(m+sign)
                               *fourier(v,-m-sign))
                err = relative(ft,ft_expected)
                worst = max(worst,err)
                exact_checks += 1
                assert err < threshold
                predicted = (constant*N**(-mp.mpf(1)/4)
                             *mp.exp(-5*mp.pi*1j*m/3)
                             *mp.exp(-mp.pi*m*m/(mp.sqrt(3)*N)))
                raw_predicted = (omega**sign*3**(-mp.mpf(1)/4)*mp.sqrt(N)
                                 *mp.exp(2*N*J0)*mp.exp(-5*mp.pi*1j*m/3)
                                 *mp.exp(-mp.pi*m*m/(mp.sqrt(3)*N)))
                mode_rows.append({
                    "m":m,
                    "m_over_sqrt_N":mp.nstr(m/mp.sqrt(N),20),
                    "normalized_actual":encode(fv),
                    "relative_gaussian_error_diagnostic":
                        mp.nstr(abs(fv/predicted-1),30),
                    "raw_relative_gaussian_error_diagnostic":
                        mp.nstr(abs(fourier(beta,m)/raw_predicted-1),30),
                })
            actual_residual = norm([x-y for x,y in zip(shift(v),v)])
            envelope_residual = norm([x-y for x,y in zip(shift(u),u)])
            records.append({
                "N":N,"power":3*sign,
                "profile_distance_diagnostic":mp.nstr(norm([x-y for x,y in zip(v,u)]),30),
                "sqrt_N_shift_residual_diagnostic":mp.nstr(mp.sqrt(N)*actual_residual,30),
                "sqrt_N_envelope_shift_residual_diagnostic":mp.nstr(mp.sqrt(N)*envelope_residual,30),
                "predicted_shift_constant":mp.nstr(mp.sqrt(a),30),
                "scaled_DC_overlap_diagnostic":encode(N**mp.mpf(".25")*fourier(v,0)),
                "predicted_DC_constant":mp.nstr(constant,30),
                "original_closing_modulus":mp.nstr(abs(alpha[-1]),30),
                "dechirped_DC_modulus":mp.nstr(abs(fourier(beta,0)),30),
                "modes":mode_rows,
            })
        print(f"Checked both original three-crossing signs at N={N}.",flush=True)
    here = Path(__file__).resolve()
    dependency = here.with_name("check_even_reflected_casimir_insertions.py")
    return {
        "status":"passed",
        "precision_decimal_digits":precision,
        "mpmath_version":mp.__version__,
        "script_sha256":hashlib.sha256(here.read_bytes()).hexdigest(),
        "dependency_sha256":{
            str(dependency.relative_to(ROOT)):
                hashlib.sha256(dependency.read_bytes()).hexdigest()
        },
        "exact_checks":exact_checks,
        "maximum_relative_identity_error":mp.nstr(worst,35),
        "scope":"Original-column signed phase, parity seam, and Fourier turn identities. "
                "Every finite asymptotic ratio is a diagnostic, not a proof.",
        "records":records,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision",type=int,default=140)
    parser.add_argument("--output",type=Path,
                        default=ROOT/"repro/results/research-three-crossing-fourier-packet.json")
    args = parser.parse_args()
    if args.precision < 100:
        parser.error("Use at least 100 decimal digits for the original column calculations.")
    result = run(args.precision)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({
        "status":result["status"],
        "signed_level_cases":len(result["records"]),
        "exact_checks":result["exact_checks"],
        "maximum_relative_identity_error":result["maximum_relative_identity_error"],
        "output":str(args.output),
    },indent=2))
