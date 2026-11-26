#!/usr/bin/env python3
"""Check original even-run backward equations and endpoint normalization.

Exact matrix/moment identities are tested numerically. Gaussian-mode
errors are recorded as finite diagnostics, not used as an asymptotic
certificate or a spectral-dominance test.
"""

import argparse
import hashlib
import json
from pathlib import Path

import mpmath as mp

from check_twist_period_insertion import original_matrices
from check_two_run_source_transfer import run_states


def relative(a, b):
    return mp.norm(a-b)/max(mp.mpf(1), mp.norm(a), mp.norm(b))


def channel(k, r, q):
    out = (r+1/r)*mp.eye(k)
    for j in range(k-1):
        out[j, j+1] = out[j+1, j] = -1
    out[0, 0] -= r
    out[k-1, k-1] -= 1/q
    return out


def run(precision):
    mp.mp.dps = precision
    tolerance = mp.power(10, -precision//2)
    records = []
    for level in (16, 17, 32, 33):
        d = level-1
        q = mp.exp(mp.pi*1j/level)
        qq = q*q
        kappa = mp.exp(mp.pi*1j*d*d/(2*level))
        crossing, _, _ = original_matrices(level)
        first = mp.eye(level)[:, 0]
        for k in (2, 3, 4):
            power = 2*k
            original = crossing**power*first
            states, _ = run_states(level, power)
            endpoint = states[d]
            current = endpoint.copy()
            sine_square = mp.mpf(1)
            error = mp.mpf(0)
            observations = mp.matrix(k)
            limiting = mp.matrix(k)
            moments = mp.matrix(k, 1)
            row = mp.eye(k)[k-1, :]
            prefix = mp.eye(k)
            laplacian = channel(k, mp.mpf(1), mp.mpf(1))
            lap_power = mp.eye(k)
            for h in range(level):
                if h:
                    sine_square *= (2*mp.sin(mp.pi*h/level))**2
                    current = channel(k, q*qq**(-h), q)*current
                error = max(error, relative(
                    current, sine_square*states[d-h]))
                error = max(error, relative(
                    kappa**power*current[k-1]/sine_square,
                    original[d-h]))
                if h < k:
                    if h:
                        prefix = channel(k, q*qq**(-h), q)*prefix
                        lap_power = laplacian*lap_power
                    observations[h, :] = row*prefix
                    limiting[h, :] = row*lap_power
                    moments[h] = sine_square*original[d-h]/kappa**power
            error = max(error, relative(observations*endpoint, moments))
            recovered = observations**-1*moments
            error = max(error, relative(recovered, endpoint),
                        abs(mp.det(limiting)-1),
                        abs(mp.det(observations)-1))

            frame = mp.matrix(k)
            eigenvalues = []
            for j in range(k):
                eigenvalues.append(4*mp.sin(mp.pi*j/(2*k))**2)
                for h in range(k):
                    frame[h, j] = (1/mp.sqrt(k) if j == 0 else
                        mp.sqrt(mp.mpf(2)/k)
                        *mp.cos(mp.pi*j*(mp.mpf(h)+mp.mpf("0.5"))/k))
            error = max(error, relative(
                laplacian*frame, frame*mp.diag(eigenvalues)))
            error = max(error, relative(frame.T*frame, mp.eye(k)))
            cphase = ((-1)**level*mp.exp(-mp.pi*1j*power/(4*level))
                      *(-1j*mp.sqrt(power)/2)*mp.exp(mp.pi*1j/4))
            predicted = mp.matrix(k, 1)
            predicted_modes = mp.matrix(k, 1)
            for j in range(1, k):
                weight = (2*(-1)**j*(1-mp.mpf(j)/k)*mp.sin(mp.pi*j/k)
                          *mp.exp(-mp.pi*1j*level*j*j/(2*k)))
                coefficient = weight/frame[k-1, j]
                predicted_modes[j] = coefficient
                predicted += coefficient*frame[:, j]
            normalized = endpoint/(cphase*level**mp.mpf("1.5"))
            norm_constant = 4*mp.fsum(
                r*r*mp.cos(mp.pi*r/(2*k))**2 for r in range(1, k))
            error = max(error, relative(
                abs(cphase)**2*mp.norm(predicted)**2, norm_constant))
            assert error < tolerance, (level, k, error)
            records.append({
                "N": level, "power": power, "channels": k,
                "colors_checked": level, "fixed_endpoint_moments": k,
                "exact_identity_maximum_relative_error": mp.nstr(error, 20),
                "gaussian_mode_error_not_a_certificate":
                    mp.nstr(mp.norm(normalized-predicted), 20),
                "scaled_gaussian_error_not_a_certificate":
                    mp.nstr(mp.sqrt(level)*mp.norm(normalized-predicted), 20),
                "normalized_dominant_projection_modulus":
                    mp.nstr(abs((frame.T*normalized)[k-1]), 20),
                "predicted_dominant_projection_modulus":
                    mp.nstr(abs(predicted_modes[k-1]), 20),
                "endpoint_norm_squared_over_N_cubed":
                    mp.nstr(mp.norm(endpoint)**2/level**3, 20),
                "proved_endpoint_norm_limit": mp.nstr(norm_constant, 20),
            })
    return records


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=110)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    records = run(args.precision)
    here = Path(__file__)
    dependencies = ("check_twist_period_insertion.py",
                    "check_two_run_source_transfer.py")
    result = {
        "status": "pass", "precision_decimal_digits": args.precision,
        "scope": "Original crossing columns, every backward color equation, "
                 "fixed endpoint observation/moment identities, exact Laplacian "
                 "modes and phase/norm constants. Gaussian errors are recorded "
                 "only; no finite test proves an asymptotic.",
        "script_sha256": hashlib.sha256(here.read_bytes()).hexdigest(),
        "dependencies_sha256": {
            name: hashlib.sha256(here.with_name(name).read_bytes()).hexdigest()
            for name in dependencies},
        "checks": records,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({
        "status": "pass", "cases": len(records),
        "colors": sum(r["colors_checked"] for r in records),
        "endpoint_moments": sum(r["fixed_endpoint_moments"] for r in records),
        "maximum_relative_error": mp.nstr(max(
            mp.mpf(r["exact_identity_maximum_relative_error"])
            for r in records), 12),
        "output": str(args.output)}))


if __name__ == "__main__":
    main()
