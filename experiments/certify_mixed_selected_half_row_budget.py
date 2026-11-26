#!/usr/bin/env python3
"""Bounded scalar attempt for four selected first-four/next-three half rows.

Only explicit rational reference maps and the original dilogarithm primitive
are evaluated. No root solve, finite quantum sum or previous cover is run.
Unresolved cells are preserved and cannot produce a complete proof status.
"""
import argparse
from collections import Counter
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import time

from flint import acb, arb, ctx

import certify_mixed_endpoint_log_budget as base


REPO = Path(__file__).resolve().parents[1]
PROOF = Path("notes/research_mixed_selected_half_row_scalar_certificate.md")
GAP = F(1, 2000)
H = F(7, 625)
KEYS = ("main_factorial", "main_forced", "left_factorial", "left_forced")
DEPENDENCIES = (
    "notes/research_mixed_selected_four_three_half_row_majorant.md",
    "notes/research_mixed_selected_half_row_evaluation_design.md",
    "notes/research_mixed_private_cap_curvature_bound.md",
    "notes/research_mixed_selected_cap_right_rows.md",
    "notes/research_mixed_selected_four_three_finite_reduction.md",
    "notes/research_mixed_first_four_next_three_central_gap.md",
    "notes/research_mixed_endpoint_coupled_log_increments.md",
    "notes/research_mixed_rational_critical_transport.md",
    "notes/research_mixed_open_word_endpoint_rectangles.md",
    "notes/research_mixed_first_four_attached_height_bound.md",
    "notes/research_mixed_reduced_disk_pair_sums.md",
    "notes/research_mixed_open_local_factor_coverage.md",
    "notes/research_mixed_typed_last_row_envelopes.md",
    "notes/research_mixed_endpoint_cap_rectangle.md",
    "experiments/certify_mixed_reduced_disk_conditional_packets.py",
    "experiments/certify_mixed_endpoint_packet_extension.py",
)


class Inconclusive(Exception):
    pass


def rat(q):
    q = F(q)
    return arb(q.numerator) / q.denominator


def lower(q):
    return F(str(q.lower().fmpq()))


def upper(q):
    return F(str(q.upper().fmpq()))


def interval(lo, hi):
    lo, hi = F(lo), F(hi)
    if lo > hi:
        raise Inconclusive("empty containing interval")
    return base.ball(lo, hi)


def real_record(q):
    if not q.is_finite():
        return {"finite": False, "ball": str(q)}
    return {"finite": True, "ball": str(q),
            "lower_rational": str(lower(q)), "upper_rational": str(upper(q))}


def complex_record(q):
    return {"real": real_record(q.real), "imag": real_record(q.imag)}


def clip_interval(q, lo, hi):
    """Image of an interval under the monotone clipping map."""
    if not q.is_finite():
        raise Inconclusive("nonfinite clipping input")
    lo, hi = F(lo), F(hi)
    return interval(min(hi, max(lo, lower(q))),
                    min(hi, max(lo, upper(q))))


def intersect_interval(q, lo, hi):
    """Necessary actual-reference intersection, with boundaries retained."""
    return interval(max(F(lo), lower(q)), min(F(hi), upper(q)))


def quadratic_gain(gradient, trial, lo, hi, mu):
    """Exact rational upper bound for both signed clipped displacements."""
    if not gradient.is_finite() or not trial.is_finite():
        raise Inconclusive("nonfinite quadratic gain")
    mu = F(mu)
    lengths = (upper(trial)-F(lo), F(hi)-lower(trial))
    if min(lengths) < 0:
        raise Inconclusive("trial does not meet the target interval")
    slopes = (max(F(0), -lower(gradient)), max(F(0), upper(gradient)))
    values = []
    for beta, length in zip(slopes, lengths):
        displacement = min(length, beta/mu)
        values.append(beta*displacement-mu*displacement*displacement/2)
    return max(values)


class OriginalPrimitives:
    """All constants are formed only after the requested precision is set."""
    def __init__(self):
        self.pi, self.ii = arb.pi(), acb(0, 1)
        self.height, self.cut = rat(H), acb(rat("27/100"))
        disc = 1-2*(2*self.pi*self.ii*self.cut).exp()
        if not disc.real > 1:
            raise Inconclusive("fixed canonical discriminant not separated")
        self.cut_u = ((self.ii+disc.sqrt())/2).atan()/self.pi
        self.regular(self.cut_u)
        self.regular(self.cut-self.cut_u)
        if not (self.cut_u.real < rat("1/2")
                and (self.cut-self.cut_u).real < rat("1/2")):
            raise Inconclusive("fixed canonical cut branch not enclosed")
        self.cut_action = self.endpoint_action(self.cut, self.cut_u)

    @staticmethod
    def regular(w):
        if not w.is_finite() or not (w.real > 0 and w.real < 1):
            raise Inconclusive("original primitive strip not certified")

    def g(self, w):
        self.regular(w)
        result = (((-2*self.pi*self.ii*w).exp().polylog(2)
                   -self.pi*self.pi/6)/(2*self.pi*self.ii))
        if not result.is_finite():
            raise Inconclusive("original dilogarithm enclosure not finite")
        return result

    def J(self, w):
        return self.g(w)-self.ii*self.pi*w*(1-w)/2

    def endpoint_action(self, e, u):
        return (-2*self.J(acb(rat("1/2"))-u)-3*self.J(u)-self.J(e-u)
                +self.ii*self.pi*e*u)

    def psi(self, e, z, action):
        return (action+self.J(e+z)-self.J(z)
                -self.ii*self.pi*e*z-self.g(e))

    def q(self, w):
        return self.g(w+rat("1/2"))-self.g(w)

    def Q(self, s, z, b):
        return (self.g(s+z)+self.g(s+b)-2*self.g(s)
                -self.g(z)-self.g(b)+2*self.pi*self.ii*z*s)

    @staticmethod
    def log_abs(w):
        modulus = abs(w)
        if not modulus.is_finite() or not modulus > 0:
            raise Inconclusive("zero not excluded from logarithmic modulus")
        return modulus.log()


def reference(box, primitive):
    pi, ii = primitive.pi, primitive.ii
    auxiliary = acb(base.ball(box[0], box[1]), base.ball(box[2], box[3]))
    U = (2*pi*ii*auxiliary).exp()
    shapes = {name: base.rational_enclosure(factors, U)
              for name, factors in base.MAPS.items()}
    coordinates = {}
    for name, shape in shapes.items():
        coordinate = ii*shape.log()/(2*pi)
        if not coordinate.is_finite():
            return "split", "nonfinite "+name+" coordinate", None
        lo, hi, hlo, hhi = map(F, base.RANGES[name])
        if (upper(coordinate.real) < lo or lower(coordinate.real) > hi
                or upper(coordinate.imag) < hlo
                or lower(coordinate.imag) > hhi):
            return "excluded", name+" range", None
        coordinates[name] = coordinate
    for name in ("s", "b"):
        if base.outside_disk(coordinates[name], ".35", "-.01", ".083"):
            return "excluded", name+" reduced disk", None
    if base.outside_disk(coordinates["z"], ".30", "-.052", ".060"):
        return "excluded", "z reduced disk", None
    for names, lo in ((("z", "s"), ".589"), (("s", "b"), ".635")):
        total = sum((coordinates[name].real for name in names), arb(0))
        if total.upper() < rat(lo) or total.lower() > rat(".77"):
            return "excluded", "+".join(names)+" coupled sum", None
    S, B = shapes["s"], shapes["b"]
    next_shape = (1-S*B)/(B*(1-S*B)+(1-B)**2)
    if next_shape.is_finite() and next_shape.imag.lower() > 0:
        return "excluded", "next external upper half-plane", None
    next_coordinate = ii*next_shape.log()/(2*pi)
    if (next_coordinate.is_finite()
            and base.outside_typed_domain(next_coordinate, 3)
            and base.outside_typed_domain(next_coordinate, 4)):
        return "excluded", "next external typed domains", None
    # Intersect each coordinate with its proved containing rectangle only
    # after the identical necessary filters. Every actual reference is kept.
    for name, w in coordinates.items():
        lo, hi, hlo, hhi = base.RANGES[name]
        coordinates[name] = acb(intersect_interval(w.real, lo, hi),
                                intersect_interval(w.imag, hlo, hhi))
    return "retained", "", (auxiliary, shapes, coordinates)


def inspect(box, primitive):
    details = {}
    try:
        state, reason, ref = reference(box, primitive)
        if state != "retained":
            return state, reason, details
        auxiliary, shapes, coordinates = ref
        details["reference_coordinates"] = {
            name: complex_record(w) for name, w in coordinates.items()}
        pi, ii = primitive.pi, primitive.ii
        e, z, s, b = (coordinates[name] for name in ("e", "z", "s", "b"))
        E, Z, S, B = (shapes[name] for name in ("e", "z", "s", "b"))
        zH = acb(z.real, primitive.height)
        lam = (2*pi*primitive.height).exp()/abs(Z)
        if not lam.is_finite():
            raise Inconclusive("nonfinite shared radial multiplier")

        # Exact outgoing maximum, including both clipping transitions.
        pR = primitive.log_abs(1-S*B)-primitive.log_abs(1-B)
        rb = abs(B)
        zeta = (rb+1/rb)*pR.tanh()/2
        acos_input = clip_interval(zeta, -1, 1)
        vhat = clip_interval(acos_input.acos()/(2*pi), ".22", ".45")
        outgoing = (primitive.q(acb(vhat, b.imag)).real
                    -pR*(vhat-b.real))
        details["outgoing"] = {
            "p_real": real_record(pR), "zeta": real_record(zeta),
            "maximizer": real_record(vhat), "value": real_record(outgoing)}

        gz, gzH = primitive.g(z), primitive.g(zH)
        common = (primitive.q(zH).real-pi*primitive.height+outgoing
                  -primitive.Q(s, z, b).real+gz.real)
        main_increment = (primitive.g(e+zH)-primitive.g(e+z)-gzH+gz).real
        actual_action = primitive.endpoint_action(e, auxiliary)
        left_increment = (primitive.psi(primitive.cut, zH, primitive.cut_action)
                          -primitive.psi(e, z, actual_action)).real
        A = primitive.log_abs(1-lam*E*Z)-primitive.log_abs(1-E*Z)
        private_gain = quadratic_gain(A, e.real, ".3", ".4", F(28, 5))
        details["common"] = real_record(common)
        details["main_increment"] = real_record(main_increment)
        details["left_increment"] = real_record(left_increment)
        details["private_gradient"] = real_record(A)
        details["private_gain_rational"] = str(private_gain)
        majorants = {}
        for where, ep, increment in (
                ("main", E, main_increment),
                ("left", (-2*pi*ii*primitive.cut).exp(), left_increment)):
            for nu, label in ((1, "factorial"), (0, "forced")):
                gradient = (primitive.log_abs(1-lam*ep*Z)
                            +primitive.log_abs(1+lam*Z)
                            -(2+nu)*primitive.log_abs(1-lam*Z))
                mu = ((F(7) if nu else F(33, 5)) if where == "main"
                      else (F(69, 10) if nu else F(13, 2)))
                incoming_gain = quadratic_gain(gradient, z.real, ".22", ".45", mu)
                fourier = -nu*gzH.real-2*nu*pi*primitive.height
                point = increment+common+fourier
                total = point+rat(incoming_gain)
                if where == "main":
                    total += rat(private_gain)
                if not total.is_finite():
                    raise Inconclusive("nonfinite "+where+" "+label+" majorant")
                key = where+"_"+label
                majorants[key] = {
                    "value": real_record(total), "point": real_record(point),
                    "incoming_gradient": real_record(gradient),
                    "incoming_curvature": str(mu),
                    "incoming_gain_rational": str(incoming_gain),
                    "accepted": bool(total < -rat(GAP)),
                }
        details["majorants"] = majorants
        if all(majorants[key]["accepted"] for key in KEYS):
            return "accepted", "four strict half-row tests", details
        return "split", "half-row majorants not certified", details
    except Inconclusive as error:
        return "split", str(error), details


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify_partition(leaves, unresolved):
    addresses = [item["address"] for item in leaves+unresolved]
    ordered = sorted(addresses)
    assert len(set(addresses)) == len(addresses)
    assert all(not set(a)-set("01") for a in addresses)
    assert not any(b.startswith(a) for a, b in zip(ordered, ordered[1:]))
    assert sum((F(1, 2**len(a)) for a in addresses), F(0)) == 1


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--bits", type=int, default=160)
    parser.add_argument("--max-cells", type=int, default=4000)
    parser.add_argument("--max-depth", type=int, default=20)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    if args.bits != 160 or not 1 <= args.max_cells <= 4000 or not 0 <= args.max_depth <= 20:
        parser.error("this single bounded attempt uses160bits, at most4000cells/depth20")
    ctx.prec = args.bits
    paths = [Path(__file__).resolve(), Path(base.__file__).resolve(),
             REPO/PROOF]+[REPO/name for name in DEPENDENCIES]
    bindings = {str(path.relative_to(REPO)): sha(path) for path in paths}
    started = time.monotonic()
    primitive = OriginalPrimitives()
    stack = [("", base.ROOT)]
    leaves, unresolved, counts, visited = [], [], Counter(), 0
    while stack and visited < args.max_cells:
        address, box = stack.pop()
        kind, reason, details = inspect(box, primitive)
        visited += 1
        if kind in ("accepted", "excluded"):
            counts[kind] += 1
            item = {"address": address, "status": kind, "reason": reason}
            if kind == "accepted":
                item["certificate"] = details
            leaves.append(item)
        elif len(address) >= args.max_depth:
            unresolved.append({"address": address, "box": list(map(str, box)),
                               "reason": reason, "enclosures": details})
        else:
            children = base.split(box, len(address))
            stack.extend([(address+"1", children[1]), (address+"0", children[0])])
        if visited % 250 == 0:
            print(json.dumps({"visited": visited, "terminal_counts": dict(counts),
                              "pending": len(stack), "depth_unresolved": len(unresolved)}),
                  flush=True)
    unresolved.extend({"address": address, "box": list(map(str, box)),
                       "reason": "cell budget; box not inspected", "enclosures": None}
                      for address, box in stack)
    verify_partition(leaves, unresolved)
    for name, expected in bindings.items():
        if sha(REPO/name) != expected:
            raise RuntimeError("input changed during attempt: "+name)
    maxima = {}
    for key in KEYS:
        values = [F(leaf["certificate"]["majorants"][key]["value"]["upper_rational"])
                  for leaf in leaves if leaf["status"] == "accepted"]
        maxima[key] = str(max(values)) if values else None
    record = {
        "status": "proved" if not unresolved else "unresolved",
        "scope": "Four strengthened main/left-cut half-row scalar upper bounds only",
        "precision_bits": args.bits, "gap": str(GAP), "height": str(H),
        "initial_auxiliary_rectangle": list(map(str, base.ROOT)),
        "necessary_reference_ranges": base.RANGES,
        "main_private_curvature": "28/5",
        "independent_tests": list(KEYS),
        "branch": "Original principal Li2 on0<Re(w)<1; canonical fixed left-cut action",
        "root_proposals": 0, "finite_source_evaluations": 0,
        "split_rule": "alternate real/imaginary dyadic subdivision, real first",
        "visited_cells": visited, "terminal_counts": dict(counts),
        "unresolved_count": len(unresolved),
        "unresolved_dyadic_fraction": str(sum(
            (F(1, 2**len(item["address"])) for item in unresolved), F(0))),
        "max_cells": args.max_cells, "max_depth": args.max_depth,
        "terminal_partition_verified": True,
        "accepted_maximum_upper_rational": maxima,
        "elapsed_seconds": time.monotonic()-started,
        "input_sha256": bindings, "leaves": leaves, "unresolved": unresolved,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(record, indent=2)+"\n")
    print(json.dumps({key: record[key] for key in (
        "status", "visited_cells", "terminal_counts", "unresolved_count",
        "unresolved_dyadic_fraction", "elapsed_seconds")}), flush=True)


if __name__ == "__main__":
    main()
