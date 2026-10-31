#!/usr/bin/env python3
"""Plot the exact finite figure-eight microscopic main-meridian profiles.

Run from any directory:
    python3 experiments/plot_figure_eight_meridian_profile.py

Dependencies: mpmath, numpy, matplotlib.

The data are computed at 80 decimal digits from the whole Laurent polynomial
    f_N(Y) = sum_{n=0}^{N-1} prod_{r=1}^n
             (Y + Y^{-1} - 2 cos(2*pi*r/N)).
No limiting profile is substituted for finite-level data.

The canonical interpolant has degree at most N-2 and takes the values
f_N(exp(2*pi*i*j/N)) for 1 <= j < N.  Its coefficients are recovered by
the finite Fourier formula with its last coefficient set to zero.
At nonzero resonances t=2*pi*k, rho_N(i*t) is evaluated by
    (g_N'(i*t) - pi_N'(i*t)) / H_N'(i*t).
At t=0 it is 1 - P_ord(1)/f_N(1).

The script writes only the four named outputs.  The JSON includes the finite
data, removable-value diagnostics, and a separate 120-digit recalculation at
selected points.  The figure illustrates convergence; it is not its proof.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.metadata
import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import mpmath as mp
import numpy as np


SCRIPT_DIR = Path(__file__).resolve().parent
ROOT = SCRIPT_DIR.parent
FIGURE_STEM = ROOT / "book" / "figures" / "figure-eight-meridian-profile"
RECORD_PATH = SCRIPT_DIR / "figure_eight_meridian_profile_plot.json"
LEVELS = (24, 47, 80)
CHECKPOINTS = (
    ("zero", 0, 1),
    ("ordinary point", 1, 3),
    ("halfway to first resonance", 1, 1),
    ("first positive resonance", 2, 1),
    ("second positive resonance", 4, 1),
    ("first negative resonance", -2, 1),
)


def decimal(value: mp.mpf, digits: int = 45) -> str:
    return mp.nstr(value, digits, strip_zeros=False)


def complex_record(value: mp.mpc | mp.mpf) -> dict[str, str]:
    return {"real": decimal(mp.re(value)), "imaginary": decimal(mp.im(value))}


class FiniteSource:
    """Finite f_N, its ordinary interpolant, and its centered regular part."""

    def __init__(self, level: int):
        self.level = level
        self.cosines = [2 * mp.cos(2 * mp.pi * r / level)
                        for r in range(level)]
        self.complete, _ = self.whole(mp.mpf("0"))
        self.ordinary = [mp.mpf("0")] * level
        for j in range(1, level):
            # At the root Y=Q^j the first zero occurs at r=min(j,N-j).
            # Stop there exactly rather than retain a roundoff-sized zero.
            term = total = mp.mpf("1")
            for r in range(1, min(j, level - j)):
                term *= self.cosines[j] - self.cosines[r]
                total += term
            self.ordinary[j] = total
        # If P has degree <=N-2, Fourier inversion and [Y^(N-1)]P=0
        # give p_r=N^-1 sum_j C_j (Q^(-jr)-Q^j).  Conjugate root
        # pairs make the coefficients real, yielding this cosine form.
        self.coefficients = [
            mp.fsum(
                self.ordinary[j]
                * (mp.cos(2 * mp.pi * j * r / level)
                   - mp.cos(2 * mp.pi * j / level))
                for j in range(1, level)
            ) / level
            for r in range(level - 1)
        ]

    def whole(self, z: mp.mpc | mp.mpf) -> tuple[mp.mpc, mp.mpc]:
        """Return f_N(exp(z/N)) and its derivative with respect to z."""
        n = self.level
        common = 2 * mp.cosh(z / n)
        common_derivative = 2 * mp.sinh(z / n) / n
        term = total = mp.mpc(1)
        derivative = derivative_total = mp.mpc(0)
        for r in range(1, n):
            factor = common - self.cosines[r]
            derivative = derivative * factor + term * common_derivative
            term *= factor
            total += term
            derivative_total += derivative
        return total, derivative_total

    def interpolant(self, z: mp.mpc | mp.mpf) -> tuple[mp.mpc, mp.mpc]:
        """Return P_ord(exp(z/N)) and its z derivative, using Horner."""
        y = mp.exp(z / self.level)
        value = mp.mpc(self.coefficients[-1])
        derivative_y = mp.mpc(0)
        for coefficient in reversed(self.coefficients[:-1]):
            derivative_y = derivative_y * y + value
            value = value * y + coefficient
        return value, y * derivative_y / self.level

    def profiles(self, t_over_pi: mp.mpf, resonance: int | None = None):
        z = mp.j * mp.pi * t_over_pi
        whole, whole_derivative = self.whole(z)
        interpolant, interpolant_derivative = self.interpolant(z)
        g = whole / self.complete
        pi_value = interpolant / self.complete
        if resonance == 0:
            rho = 1 - pi_value
            method = "value at zero"
        elif resonance is not None:
            k = resonance
            h_derivative = ((-1) ** k
                            / (2 * mp.j * self.level
                               * mp.sin(mp.pi * k / self.level)))
            rho = ((whole_derivative - interpolant_derivative)
                   / self.complete / h_derivative)
            method = "removable derivative quotient"
        else:
            h = mp.sinh(z / 2) / (self.level * mp.sinh(z / (2 * self.level)))
            rho = (g - pi_value) / h
            method = "exact centered quotient"
        return g, rho, {
            "method": method,
            "g": complex_record(g),
            "rho": complex_record(rho),
            "absolute_rho_error": decimal(abs(rho - 1)),
            "pi": complex_record(pi_value),
            "vanishing_numerator_residual": (
                decimal(abs(g - pi_value))
                if resonance not in (None, 0) else None
            ),
        }

    def interpolation_residual(self) -> mp.mpf:
        return max(
            abs(self.interpolant(2 * mp.j * mp.pi * j)[0] - self.ordinary[j])
            for j in range(1, self.level)
        )


def checkpoint_values(source: FiniteSource):
    values = {}
    for label, numerator, denominator in CHECKPOINTS:
        t_over_pi = mp.mpf(numerator) / denominator
        resonance = (numerator // (2 * denominator)
                     if numerator % (2 * denominator) == 0 else None)
        g, rho, details = source.profiles(t_over_pi, resonance)
        values[label] = (g, rho, details)
    return values


def removable_value_checks(source: FiniteSource, checkpoints):
    displacement = mp.mpf("1e-12")
    records = {}
    for label, numerator, denominator in CHECKPOINTS:
        if numerator % (2 * denominator):
            continue
        center = mp.mpf(numerator) / denominator
        left = source.profiles(center - displacement)[1]
        right = source.profiles(center + displacement)[1]
        error = abs((left + right) / 2 - checkpoints[label][1])
        if error > mp.mpf("1e-18"):
            raise ArithmeticError(
                f"removable-value mismatch at N={source.level}, {label}"
            )
        records[label] = {
            "displacement_in_t_over_pi": decimal(displacement),
            "symmetric_average_minus_removable_value": decimal(error),
            "interpretation": "finite displacement error, of second order",
        }
    return records


def next_order_diagnostics(source: FiniteSource):
    """Record finite values against the proved first correction; no fit."""
    records = {}
    for label, z, resonance in (
        ("z=1", mp.mpf(1), None),
        ("z=i", mp.j, None),
        ("z=2*pi*i", 2 * mp.pi * mp.j, 1),
    ):
        _, rho, _ = source.profiles(z / (mp.j * mp.pi), resonance)
        scaled = source.level * (rho - 1)
        predicted = mp.sqrt(3) * z**2 / (4 * mp.pi)
        records[label] = {
            "z": complex_record(z),
            "N_times_rho_minus_one": complex_record(scaled),
            "predicted_limit_sqrt3_z_squared_over_4pi": complex_record(predicted),
            "absolute_difference": decimal(abs(scaled - predicted)),
        }
    return records


def build_data(dps: int, samples: int):
    mp.mp.dps = dps
    records = []
    figure_data = []
    for level in LEVELS:
        source = FiniteSource(level)
        grid = []
        for i in range(samples):
            # This rational grid contains 0, +-2*pi, and +-4*pi exactly.
            numerator = 8 * i - 4 * (samples - 1)
            denominator = samples - 1
            t_over_pi = mp.mpf(numerator) / denominator
            resonance = (numerator // (2 * denominator)
                         if numerator % (2 * denominator) == 0 else None)
            g, rho, _ = source.profiles(t_over_pi, resonance)
            grid.append({
                "t_over_pi": float(t_over_pi),
                "g_real": float(mp.re(g)),
                "g_imaginary": float(mp.im(g)),
                "rho_real": float(mp.re(rho)),
                "rho_imaginary": float(mp.im(rho)),
                "absolute_rho_error": float(abs(rho - 1)),
                "resonance_index": resonance,
            })
        checkpoints = checkpoint_values(source)
        removable_checks = removable_value_checks(source, checkpoints)
        interpolation_error = source.interpolation_residual()
        # Independent working-precision comparison, with all finite source
        # values and interpolant coefficients recomputed from the beginning.
        with mp.workdps(dps + 40):
            fine_source = FiniteSource(level)
            fine = checkpoint_values(fine_source)
            precision_differences = {
                label: {
                    "g": decimal(abs(checkpoints[label][0] - fine[label][0])),
                    "rho": decimal(abs(checkpoints[label][1] - fine[label][1])),
                } for label, _, _ in CHECKPOINTS
            }
        max_precision_error = max(
            mp.mpf(value[field])
            for value in precision_differences.values() for field in ("g", "rho")
        )
        # These checks diagnose evaluation errors, not convergence.
        if interpolation_error > mp.mpf(10) ** (-(dps // 2)):
            raise ArithmeticError(f"interpolant residual too large at N={level}")
        if max_precision_error > mp.mpf(10) ** (-(dps // 2)):
            raise ArithmeticError(f"precision discrepancy too large at N={level}")
        records.append({
            "N": level,
            "K_N": complex_record(source.complete),
            "interpolant_degree_bound": level - 2,
            "interpolation_maximum_absolute_residual": decimal(interpolation_error),
            "checkpoints": {label: value[2] for label, value in checkpoints.items()},
            "removable_value_comparison": removable_checks,
            "next_order_diagnostics": next_order_diagnostics(source),
            "precision_comparison": precision_differences,
            "maximum_sampled_rho_error": max(row["absolute_rho_error"] for row in grid),
            "grid": grid,
        })
        figure_data.append(grid)
        print(f"N={level}: finite source and interpolant computed; "
              f"precision difference {mp.nstr(max_precision_error, 5)}")
    return records, figure_data


def render(data, dps: int):
    plt.rcParams.update({
        "font.family": "DejaVu Sans", "font.size": 10,
        "axes.spines.top": False, "axes.spines.right": False,
        "axes.titlesize": 12, "axes.labelsize": 10.5,
        "pdf.fonttype": 42, "svg.fonttype": "none",
        "svg.hashsalt": "figure-eight-meridian-profile",
    })
    figure, axes = plt.subplots(1, 2, figsize=(12.2, 5.5))
    figure.subplots_adjust(left=0.073, right=0.98, bottom=0.22,
                           top=0.80, wspace=0.27)
    colors = ("#c76816", "#2473a6", "#277c51")
    line_styles = ("-", "--", "-.")
    t = np.array([row["t_over_pi"] for row in data[0]])
    axes[0].plot(t, np.sinc(t / 2), color="#252a30", linewidth=2.0,
                 linestyle=(0, (5, 2)), label=r"$H(it)=\sin(t/2)/(t/2)$", zorder=4)
    for level, rows, color, style in zip(LEVELS, data, colors, line_styles):
        axes[0].plot(t, [row["g_real"] for row in rows],
                     color=color, linestyle=style, linewidth=1.6,
                     label=rf"$N={level}$")
        axes[1].semilogy(t, [row["absolute_rho_error"] for row in rows],
                        color=color, linestyle=style, linewidth=1.6,
                        label=rf"$N={level}$")
        resonance_rows = [row for row in rows if row["resonance_index"] is not None]
        axes[1].scatter(
            [row["t_over_pi"] for row in resonance_rows],
            [row["absolute_rho_error"] for row in resonance_rows],
            color=color, s=20, zorder=5,
        )
    for axis in axes:
        axis.set_xlim(-4, 4)
        axis.set_xticks([-4, -2, 0, 2, 4],
                       [r"$-4\pi$", r"$-2\pi$", "$0$", r"$2\pi$", r"$4\pi$"])
        axis.set_xlabel(r"Imaginary displacement $t$, with $M=e^{it/(2N)}$")
        axis.grid(True, color="#dce1e5", linewidth=0.65, alpha=0.8)
        for resonance in (-2, 2):
            axis.axvline(resonance, color="#9da6af", linewidth=0.7, alpha=0.7)
    axes[0].set_title("The reduced invariant and its limiting profile", pad=12)
    axes[0].set_ylabel(r"$g_N(it)=f_N(e^{it/N})/f_N(1)$")
    axes[0].legend(loc="upper right", frameon=False, fontsize=9)
    axes[1].set_title("Error in the centered regular profile", pad=12)
    axes[1].set_ylabel(r"$|\rho_N(it)-1|$ (logarithmic scale)")
    axes[1].legend(loc="lower right", frameon=False, fontsize=9)
    figure.suptitle("The figure-eight knot: varying the meridian near completeness",
                     x=0.5, y=0.965, fontsize=16, fontweight="medium")
    figure.text(0.5, 0.902,
                "Finite sums and their ordinary-color subtraction",
                ha="center", fontsize=10.5, color="#48515b")
    figure.text(0.073, 0.105,
                r"$f_N(Y)=S_N(Y)R_N^{\rm reg}(Y)+P_N^{\rm ord}(Y)$,  "
                r"$S_N(Y)=1+\cdots+Y^{N-1}$,  "
                r"$\rho_N(it)=e^{(N-1)it/(2N)}\,"
                r"N R_N^{\rm reg}(e^{it/N})/f_N(1)$.",
                fontsize=10)
    figure.text(0.073, 0.045,
                "Dots use removable values at t = 0, ±2π, ±4π.  "
                "The plot illustrates convergence; the estimates are proved separately.",
                fontsize=9.5, color="#48515b")
    FIGURE_STEM.parent.mkdir(parents=True, exist_ok=True)
    for extension in ("pdf", "svg", "png"):
        path = FIGURE_STEM.with_suffix("." + extension)
        metadata = {"Date": None} if extension == "svg" else None
        if extension == "pdf":
            metadata = {"CreationDate": None, "ModDate": None,
                        "Title": "The figure-eight knot: varying the meridian near completeness"}
        figure.savefig(path, dpi=220, metadata=metadata)
    plt.close(figure)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dps", type=int, default=80,
                        help="working decimal digits (minimum 60; default 80)")
    parser.add_argument("--samples", type=int, default=801,
                        help="sample count, 1 modulo 4 (default 801)")
    args = parser.parse_args()
    if args.dps < 60 or args.samples < 33 or (args.samples - 1) % 4:
        parser.error("require dps>=60 and samples>=33 with samples=1 modulo 4")
    records, data = build_data(args.dps, args.samples)
    render(data, args.dps)
    payload = {
        "description": "Exact finite figure-eight microscopic meridian profiles",
        "command": ("python3 experiments/plot_figure_eight_meridian_profile.py"
                    f" --dps {args.dps} --samples {args.samples}"),
        "working_decimal_digits": args.dps,
        "comparison_decimal_digits": args.dps + 40,
        "sample_count": args.samples,
        "source_identity": "notes/figure_eight_whole_source_identity.md, equation (1.1)",
        "regularization": "notes/scaled_meridian_regular_profile.md, equations (1)-(7)",
        "source_code_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "software_versions": {
            package: importlib.metadata.version(package)
            for package in ("mpmath", "numpy", "matplotlib")
        },
        "normalization": {
            "Y": "exp(z/N), z=i*t",
            "M": "exp(z/(2N))",
            "g_N": "f_N(exp(z/N))/f_N(1)",
            "rho_N": "exp((N-1)*z/(2*N))*N*R_reg(exp(z/N))/f_N(1)",
            "ordinary_interpolant": "degree <= N-2; values at Q^j, 1<=j<N",
        },
        "illustration_scope": "Finite data illustrate, but do not prove, convergence.",
        "levels": records,
        "figures": {
            extension: {
                "path": str(FIGURE_STEM.with_suffix("." + extension).relative_to(ROOT)),
                "sha256": hashlib.sha256(
                    FIGURE_STEM.with_suffix("." + extension).read_bytes()
                ).hexdigest(),
            } for extension in ("pdf", "svg", "png")
        },
    }
    RECORD_PATH.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    print(f"Wrote {RECORD_PATH.relative_to(ROOT)} and three figure assets.")


if __name__ == "__main__":
    main()
