#!/usr/bin/env python3
"""Render a boundary schematic, not a complete periodic circle packing.

The opposite-protected-outer convention is
    F1=(u,A,v,C), F2=(v,B,u,D), boundary u-A-C-v-B-D-u.
Only the two equal-radius boundary pairs and one translated pair are drawn.
Run from any directory; outputs are native SVG and a PNG inspection copy.
"""

from pathlib import Path
import math

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon


def main():
    root = Path(__file__).resolve().parents[1]
    output = root / "book" / "figures" / "two-cap-cylindrical-boundary"
    output.parent.mkdir(parents=True, exist_ok=True)
    plt.rcParams.update({
        "font.family": "DejaVu Sans",
        "svg.fonttype": "none",
        "svg.hashsalt": "two-cap-cylindrical-boundary-v1",
    })

    h, radius, period = 3.0, 1.0, 8.0
    horizontal = math.sqrt(3.0)
    centers = {
        "A": (0.0, 1.0), "C": (horizontal, 2.0),
        "D": (4.0, 1.0), "B": (4.0 + horizontal, 2.0),
    }
    assert math.isclose(math.dist(centers["A"], centers["C"]), 2 * radius)
    assert math.isclose(math.dist(centers["D"], centers["B"]), 2 * radius)
    assert math.dist(centers["C"], centers["D"]) > 2 * radius
    assert math.dist(centers["B"], (period, 1.0)) > 2 * radius

    fig = plt.figure(figsize=(14, 6.4), facecolor="#ffffff")
    ax = fig.add_axes([0.045, 0.235, 0.93, 0.60])
    ax.set_aspect("equal")
    ax.set_xlim(-1.7, 11.0)
    ax.set_ylim(-0.65, 3.95)
    ax.axis("off")

    ink, muted = "#163449", "#546777"
    cut, outline = "#bc4d39", "#366884"
    ax.add_patch(Polygon(
        [(0, 0), (4, 0), (4 + horizontal, h), (horizontal, h)],
        closed=True, facecolor="#e5f0e6", edgecolor="none", zorder=0,
    ))
    for y, label in [(0, "u"), (h, "v")]:
        ax.plot([-1.15, 10.85], [y, y], color=ink, lw=1.8, zorder=1)
        ax.text(-1.32, y, label, fontsize=17, fontstyle="italic",
                color=ink, ha="center", va="center")

    # The ghost copy makes the deck translation visible without drawing
    # any purported interior packing or asserting additional contacts.
    for label in ["A", "C"]:
        x, y = centers[label]
        ax.add_patch(Circle((x + period, y), radius, facecolor="#fafafa",
                            edgecolor="#9ba7b0", lw=1.4,
                            linestyle=(0, (4, 3)), zorder=2))
        ax.text(x + period, y, f"{label} + T", ha="center", va="center",
                fontsize=13, color="#778792", zorder=5)
    for label, (x, y) in centers.items():
        ax.add_patch(Circle((x, y), radius, facecolor="#f3f7fa",
                            edgecolor=outline, lw=1.8, zorder=2))
        ax.text(x, y, label, ha="center", va="center", fontsize=18,
                color=ink, zorder=5)

    for index, offset in enumerate([0.0, 4.0], start=1):
        ax.plot([offset, offset + horizontal], [0, h], color=cut,
                lw=2.2, zorder=4)
        points = [(offset, 0), (offset + horizontal / 2, h / 2),
                  (offset + horizontal, h)]
        ax.scatter(*zip(*points), s=27, facecolor=cut, edgecolor="white",
                   linewidth=0.7, zorder=6)
        ax.text(offset + 0.55, -0.39, f"cap cut {index}", color=cut,
                fontsize=12, ha="center", va="center")

    ax.text(2.9, 1.5, r"$\mathcal{D}$", fontsize=26,
            ha="center", va="center", color="#386547", zorder=6)
    ax.annotate("", xy=(period, 3.67), xytext=(0, 3.67),
                arrowprops={"arrowstyle": "<->", "color": muted, "lw": 1.4})
    for x in [0, period]:
        ax.plot([x, x], [3.54, 3.79], color=muted, lw=1.1)
    ax.text(period / 2, 3.78, "one translation period  T = 8",
            color=muted, fontsize=12, ha="center", va="bottom")

    fig.text(0.055, 0.94, "Two-cap cylindrical exterior", fontsize=21,
             weight="semibold", color=ink, ha="left")
    fig.text(0.055, 0.885, "Equal-radius boundary pairs between the parallel marked lines",
             fontsize=13, color=muted, ha="left")
    fig.text(0.055, 0.165, "Boundary schematic; interior packing omitted",
             fontsize=14, weight="semibold", color=ink, ha="left")
    fig.text(0.055, 0.112,
             r"r = 1, H = 3, ν₁ = ν₂ = 1/3.  Green shading marks the chosen exterior $\mathcal{D}$; gray circles are translates.",
             fontsize=11.5, color=muted, ha="left")
    fig.text(0.055, 0.063,
             "Recorded boundary order: u–A–C–v–B–D–u.  Each red cut joins its pair’s three contact points.",
             fontsize=11.5, color=muted, ha="left")

    fig.savefig(output.with_suffix(".svg"), metadata={
        "Date": None,
        "Title": "Two-cap cylindrical exterior: boundary schematic",
        "Description": "Boundary schematic; interior packing omitted. "
            "Two disjoint contact cuts, parallel marked lines, and one translation period.",
    })
    fig.savefig(output.with_suffix(".png"), dpi=150)
    plt.close(fig)
    print(output.with_suffix(".svg"))
    print(output.with_suffix(".png"))


if __name__ == "__main__":
    main()
