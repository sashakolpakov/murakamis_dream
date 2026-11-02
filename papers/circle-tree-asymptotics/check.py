#!/usr/bin/env python3
"""Finite algebra and outward rational budgets for circle-tree asymptotics.

Reuses the existing exact edge/finite strip checker. Additional inequalities
use Fraction arithmetic and rigorous series bounds, not floating sampling.
This does not prove the contour estimates, uniform asymptotics, finite
diagram adapter, or hyperbolic geometry.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile


def atan_bounds(x, terms=12):
    partial = sum(((-1)**j*x**(2*j+1)/F(2*j+1)
                   for j in range(terms)), F(0))
    next_term = (-1)**terms*x**(2*terms+1)/F(2*terms+1)
    return min(partial, partial+next_term), max(partial, partial+next_term)


def positive_series_upper(x, parity, terms=10):
    """Upper bound for sinh(x), or cosh(x)-1, for positive rational x."""
    first = 1 if parity else 2
    factorial = 1
    for i in range(1, first+1):
        factorial *= i
    term, total = x**first/F(factorial), F(0)
    degree = first
    for _ in range(terms):
        total += term
        term *= x*x/F((degree+1)*(degree+2))
        degree += 2
    ratio = x*x/F((degree+1)*(degree+2))
    assert 0 < ratio < 1
    return total + term/(1-ratio)


def encoded(q):
    return {"rational": str(q), "decimal_for_orientation": float(q)}


def rational_budgets():
    # tan(4 atan(1/5) - atan(1/239)) = 1, with the angle in (0,pi/2).
    t = F(1, 5)
    twice = 2*t/(1-t*t)
    four = 2*twice/(1-twice*twice)
    assert (four-F(1, 239))/(1+four/F(239)) == 1
    a, b = atan_bounds(F(1, 5)), atan_bounds(F(1, 239))
    pi_lo, pi_hi = 16*a[0]-4*b[1], 16*a[1]-4*b[0]
    assert 3 < pi_lo < pi_hi < F(22, 7)
    delta, eps, a0, t0 = F(1, 50), F(1, 25), F(1, 400), F(1, 16)
    gamma = (1+delta)/(1-delta)**2
    beta_upper = pi_hi*gamma/F(2**25)
    half_eta_lower = 1/(1638400*pi_hi)
    connector = gamma*max((1+eps)/2, 2/(3-4*eps))
    endpoint_cost_upper = pi_hi*a0*t0+a0*t0*t0+70*a0*a0*t0*t0
    endpoint_half_loss_lower = a0*pi_lo*pi_lo/2
    sigma = positive_series_upper(F(1, 8), 1)
    k = positive_series_upper(F(1, 8), 0)
    # 1/sqrt(1-sigma^4) <= 1/(1-sigma^4).
    c_upper = 1/(1-sigma**4)
    diagonal_upper = 2*k*c_upper/(1-k)+c_upper-1
    row_upper = diagonal_upper+sigma*sigma*c_upper
    tangent_upper = sigma/(1-k)
    cosine_upper = tangent_upper**2/(1-tangent_upper**2)
    # arcsin(z) <= z/sqrt(1-z^2) <= z/(1-z^2) for 0<=z<1.
    wire_distance_upper = cosine_upper/(1-cosine_upper**2)/(2*pi_lo)
    vertical = -6*F(47, 1000)**2+44*F(47, 1000)*F(5, 1000)+22*F(5, 1000)**2
    margins = {
        "critical_drop_below_half_fixed_loss": half_eta_lower-beta_upper,
        "connector_coefficient_below_three_quarters": F(3, 4)-connector,
        "endpoint_cost_below_half_loss": endpoint_half_loss_lower-endpoint_cost_upper,
        "tail_quadratic_cost_below_half": a0/2-100*a0*a0,
        "raw_real_constant": 1/(80*pi_hi)-F(1, 400),
        "raw_imaginary_constant": 70-8*pi_hi,
        "diagonal_error_below_delta": delta-diagonal_upper,
        "row_error_below_epsilon": eps-row_upper,
        "tan_bound": F(128, 1000)-tangent_upper,
        "critical_cosine_bound": F(17, 1000)-cosine_upper,
        "critical_wire_distance": F(3, 1000)-wire_distance_upper,
        "vertical_current_loss": -F(2, 1000)-vertical,
        "nonconstant_cotangent_loss": 2*pi_lo/F(500)-F(77, 30000),
        "nonempty_charge_cutoff_squared": F(2**25)-(64*pi_hi)**2,
        "geometric_chart_squared": (1-delta)**2*2**25-(200*pi_hi)**2,
    }
    assert all(value > 0 for value in margins.values()), margins
    # Negative controls: these altered budgets would not be certified.
    assert 2*beta_upper > half_eta_lower
    assert F(1, 2) < connector
    return {
        "method": "exact rational arithmetic; alternating arctangent and positive hyperbolic series tails",
        "pi_interval": [str(pi_lo), str(pi_hi)],
        "critical_drop_upper": encoded(beta_upper),
        "half_fixed_loss_lower": encoded(half_eta_lower),
        "connector_coefficient": encoded(connector),
        "strict_margin_lower_bounds": {k: encoded(v) for k, v in margins.items()},
        "negative_controls": [
            "doubling the allowed summed bound fails this beta-versus-eta/2 comparison",
            "replacing the connector threshold by one half fails",
        ],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.unlink(missing_ok=True)
    if not __debug__:
        raise RuntimeError("Run with assertions enabled, without -O.")
    here = Path(__file__).resolve().parent
    repo = here.parents[1]
    old_script = repo/"experiments/audit_all_circle_curvature_packet.py"
    sources = sorted(here.rglob("*.tex")) + [Path(__file__).resolve(), old_script]
    sources += [
        repo/"papers/conway-asymptotics/factorial.tex",
        repo/"papers/meridian-tangles/main.tex",
        repo/"papers/circle-tree-geometry/main.tex",
    ]
    def hashes():
        return {str(p.relative_to(repo)): hashlib.sha256(p.read_bytes()).hexdigest()
                for p in sources}
    before = hashes()
    budgets = rational_budgets()
    with tempfile.TemporaryDirectory(prefix="circle-tree-edge-") as tmp:
        child = Path(tmp)/"edge.json"
        subprocess.run([sys.executable, "-I", str(old_script), "--output", str(child)],
                       cwd=repo, check=True, capture_output=True, text=True)
        edge = json.loads(child.read_text())
    if hashes() != before:
        raise RuntimeError("A source changed while the checker ran.")
    record = {
        "scope": "exact edge identities, outward rational constant budgets, and explicitly finite product samples",
        "not_proved": [
            "uniform complex product or contour estimates",
            "charge-tail convergence or Gaussian asymptotics",
            "original finite diagram normalization",
            "hyperbolic metric or volume identification",
        ],
        "source_sha256": before,
        "rational_budgets": budgets,
        "existing_edge_checker": edge,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(record, indent=2, sort_keys=True)+"\n")
    print(json.dumps({"output": str(args.output),
                      "exact_edge_identities": edge["exact_symbolic_identities"],
                      "rational_budgets": len(budgets["strict_margin_lower_bounds"]),
                      "finite_product_samples": edge["finite_complex_gaussian_cases"]}))


if __name__ == "__main__":
    main()
