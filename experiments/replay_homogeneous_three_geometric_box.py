#!/usr/bin/env python3
"""Independent outward replay of the geometric neighbor-map certificate.

No author module is imported. Exact rational rectangles and the neighbor
mesh are read from the completed artifact, then all analytic enclosures
and strict inequalities are recomputed. A horizontal sweep checks the
t-domain partition independently of the author's adaptive splitting.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import time

from flint import acb, arb, ctx


F = Fraction
DOMAIN = (F(13, 10), F(91, 50), F(41, 50), F(121, 100))


def scalar(value):
    value = F(value)
    return arb(value.numerator)/value.denominator


def closed_interval(left, right):
    return scalar((left+right)/2)+arb(0, scalar((right-left)/2))


def complex_rectangle(bounds):
    left, right, low, high = bounds
    return acb(closed_interval(left, right), -closed_interval(low, high))


def exact_center(bounds):
    left, right, low, high = bounds
    return acb(scalar((left+right)/2), -scalar((low+high)/2))


def horizontal_cover(rectangles):
    """Every open horizontal slab must be covered exactly once."""
    left, right, low, high = DOMAIN
    events = {}
    for index, box in enumerate(rectangles):
        x0, x1, h0, h1 = box
        assert left <= x0 < x1 <= right and low <= h0 < h1 <= high
        events.setdefault(h0, []).append((1, index, x0, x1))
        events.setdefault(h1, []).append((-1, index, x0, x1))
    heights = sorted(events)
    assert heights[0] == low and heights[-1] == high
    active = {}
    for height in heights:
        for direction, index, x0, x1 in events[height]:
            if direction > 0:
                assert index not in active
                active[index] = (x0, x1)
            else:
                assert active.pop(index) == (x0, x1)
        if height == high:
            assert not active
            continue
        position = left
        for x0, x1 in sorted(active.values()):
            assert x0 == position, (height, position, x0)
            position = x1
        assert position == right
    return len(heights)-1


def point_jet(t, u):
    """The return and its two first derivatives, evaluated directly."""
    tangent = (t/2).tan()
    cosine, sine = (u/2).cos(), (u/2).sin()
    square_root = (1+(tangent*cosine)**2).sqrt()
    return ((tangent*cosine).asinh(),
            cosine*(1+tangent*tangent)/(2*square_root),
            -tangent*sine/(2*square_root))


def mean_value_jet(t_box, u_box):
    """Integrate the holomorphic derivatives on a convex product box.

    r_tt = c v(1+v²)/(2s) - c³ v(1+v²)²/(4s³),
    r_tu = -sin(u/2)(1+v²)/(4s³),
    r_uu = -v c(1+v²)/(4s³).
    """
    t, u = complex_rectangle(t_box), complex_rectangle(u_box)
    center_t, center_u = exact_center(t_box), exact_center(u_box)
    offset_t, offset_u = t-center_t, u-center_u
    value0, dt0, du0 = point_jet(center_t, center_u)
    _, dt, du = point_jet(t, u)
    v = (t/2).tan()
    c, sn = (u/2).cos(), (u/2).sin()
    sq = (1+v*v*c*c).sqrt()
    square = 1+v*v
    # Powers retain the exact dependency of a repeated complex interval;
    # multiplying independent copies would needlessly widen this bound.
    dtt = c*v*square/(2*sq)-c**3*v*square**2/(4*sq**3)
    dtu = -sn*square/(4*sq**3)
    duu = -v*c*square/(4*sq**3)
    # All line segments used for these integrals lie in the boxes.
    return (value0+dt*offset_t+du*offset_u,
            dt0+dtt*offset_t+dtu*offset_u,
            du0+dtu*offset_t+duu*offset_u)


def neighbor_grid(mesh):
    left, right, low, high = DOMAIN
    return [(left+(right-left)*i/mesh, left+(right-left)*(i+1)/mesh,
             low+(high-low)*j/mesh, low+(high-low)*(j+1)/mesh)
            for j in range(mesh) for i in range(mesh)]


def check_rectangle(t_box, neighbors):
    ii = acb(0, 1)
    samples = [mean_value_jet(t_box, u_box) for u_box in neighbors]
    hull = samples[0][1]
    for _, dt, _ in samples[1:]:
        hull = acb(hull.real.union(dt.real), hull.imag.union(dt.imag))
    complete = mean_value_jet(t_box, (F(0), F(0), F(0), F(0)))[1]
    minima = {}

    def require(label, margin):
        assert margin > 0, (tuple(map(str, t_box)), label, str(margin))
        bound = margin.lower()
        if label not in minima or bound < minima[label]:
            minima[label] = bound

    for value, dt, du in samples:
        require("return real part", value.real)
        require("return imaginary lower", value.imag+scalar(F(3, 5)))
        require("return imaginary upper", -value.imag)
        for name, other in (("finite", hull), ("complete", complete)):
            denominator = 3+2*ii*(dt+other)
            derivative = (-2*ii*du)/denominator
            require(name+" denominator real part", denominator.real)
            require(name+" derivative real lower", derivative.real)
            require(name+" derivative real upper", scalar(F(1, 4))-derivative.real)
            require(name+" derivative imaginary lower", scalar(F(1, 16))+derivative.imag)
            require(name+" derivative imaginary upper", scalar(F(1, 16))-derivative.imag)
    return minima


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=160)
    parser.add_argument("--input", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--smoke", action="store_true")
    args = parser.parse_args()
    ctx.prec = args.precision
    root = Path(__file__).resolve().parents[1]
    if args.smoke:
        assert horizontal_cover([DOMAIN]) == 1
        try:
            horizontal_cover([DOMAIN, DOMAIN])
        except AssertionError:
            pass
        else:
            raise AssertionError("The exact-cover check accepted a doubled domain")
        a = (DOMAIN[0]+DOMAIN[1])/2
        h = (DOMAIN[2]+DOMAIN[3])/2
        check_rectangle((a, a, h, h), neighbor_grid(32))
        print("Smoke passed: exact-cover rejection and midpoint 32x32 neighbor checks. No full certificate replay.")
        return

    input_path = args.input or root/"repro/results/research-homogeneous-three-geometric-box.json"
    output_path = args.output or root/"repro/results/research-homogeneous-three-geometric-box-review.json"
    source = root/"experiments/certify_homogeneous_three_geometric_box.py"
    artifact = json.loads(input_path.read_text())
    assert artifact["status"] == "passed"
    assert tuple(F(v) for v in artifact["domain_real_angle_height"]) == DOMAIN
    assert artifact["sha256"][source.name] == hashlib.sha256(source.read_bytes()).hexdigest()
    mesh = artifact["neighbor_mesh"]
    assert isinstance(mesh, int) and mesh == 32
    rectangles = [tuple(F(v) for v in entry["box"]) for entry in artifact["accepted"]]
    assert rectangles
    slabs = horizontal_cover(rectangles)
    neighbors = neighbor_grid(mesh)
    started = time.monotonic()
    global_minima = {}
    checked = []
    for index, box in enumerate(rectangles, 1):
        margins = check_rectangle(box, neighbors)
        for name, value in margins.items():
            if name not in global_minima or value < global_minima[name]:
                global_minima[name] = value
        checked.append({"author_rectangle": index-1, "positive_margins": {k: str(v) for k, v in margins.items()}})
        if index % 100 == 0:
            print(f"replayed {index}/{len(rectangles)} rectangles in {time.monotonic()-started:.1f}s", flush=True)
    dependencies = [Path(__file__).resolve(), source, input_path]
    proof = root/"notes/research_homogeneous_three_geometric_contraction.md"
    if proof.exists():
        dependencies.append(proof)
    result = {
        "status": "passed", "precision_bits": ctx.prec,
        "scope": "Independent recomputation of every analytic derivative/return bound, without importing the author module. Exact rational horizontal sweep proves multiplicity-one coverage. Baseline roots, no-exit arithmetic and Banach/geometric identification have a separate written proof and checker. No quantum coefficient conclusion.",
        "domain_real_angle_height": [str(v) for v in DOMAIN],
        "neighbor_mesh": mesh, "parameter_rectangles": len(rectangles),
        "neighbor_rectangles_per_parameter": len(neighbors),
        "horizontal_cover_slabs": slabs,
        "extra_refinement": 0,
        "positive_minima": {k: str(v) for k, v in global_minima.items()},
        "checked": checked, "wall_seconds": time.monotonic()-started,
        "sha256": {str(p.relative_to(root)) if p.is_relative_to(root) else str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in dependencies},
    }
    output_path.write_text(json.dumps(result, indent=2)+"\n")
    print(f"Passed independent replay of {len(rectangles)} rectangles at {ctx.prec} bits. {output_path}", flush=True)


if __name__ == "__main__":
    main()
