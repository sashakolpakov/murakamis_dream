"""Boundary responses from certified prefix coordinates and derivatives.

The first endpoint flag is one. No roots, inverse matrices, reference
maps or scalar budgets are evaluated here. Inputs are never clipped.
The caller certifies the common canonical reference and dq*/dc.
"""
from fractions import Fraction as F

from flint import acb, arb


NAMES = ("e", "xi", "a", "u", "z", "v", "b")
HEIGHT_BOUNDS = {
    "u": (F(-51, 500), F(-1, 1000)),
    "a": (F(-39, 500), F(21, 1000)),
}


class Inconclusive(Exception):
    pass


def endpoints(value):
    if not value.is_finite():
        raise Inconclusive("nonfinite real enclosure")
    lo = F(str(value.lower().fmpq()))
    hi = F(str(value.upper().fmpq()))
    if lo > hi:
        raise Inconclusive("reversed real enclosure")
    return lo, hi


def real_record(value):
    lo, hi = endpoints(value)
    return {"finite": True, "lower_rational": str(lo), "upper_rational": str(hi)}


def complex_record(value):
    return {"real": real_record(value.real), "imag": real_record(value.imag)}


def rectangle_record(value, limits, strict=False):
    x, h = endpoints(value.real), endpoints(value.imag)
    lo, hi, bottom, top = map(F, limits)
    if strict:
        contained = lo < x[0] <= x[1] < hi and bottom < h[0] <= h[1] < top
    else:
        contained = lo <= x[0] <= x[1] <= hi and bottom <= h[0] <= h[1] <= top
    return {"bounds": list(map(str, (lo, hi, bottom, top))),
            "strict": strict, "whole_box_contained": contained}


def disk_record(value, kind):
    a, b, radius = ((F(7, 20), F(-1, 100), F(83, 1000)) if kind == 3
                    else (F(3, 10), F(-13, 250), F(3, 50)))
    x, h = endpoints(value.real), endpoints(value.imag)
    maximum = max((x[0]-a)**2, (x[1]-a)**2)+max((h[0]-b)**2, (h[1]-b)**2)
    dx, dy = max(F(0), x[0]-a, a-x[1]), max(F(0), h[0]-b, b-h[1])
    minimum = dx*dx+dy*dy
    return {"kind": kind, "center_real_rational": str(a), "center_imag_rational": str(b),
            "radius_rational": str(radius), "rectangle_distance_squared_upper_rational": str(maximum),
            "rectangle_distance_squared_lower_rational": str(minimum),
            "whole_box_contained": maximum <= radius**2,
            "strictly_disjoint": minimum > radius**2}


def domain_records(coordinates, beta):
    """Only report tests; never intersect an input with these domains."""
    common = {}
    for name in NAMES:
        limits = (".33", ".47", "-.09", ".08") if name == "e" else (
            (".21", ".25", ".01", ".10") if name == "xi"
            else (".23", ".45", "-.12", ".12"))
        common[name] = rectangle_record(coordinates[name], limits)
    heights = {}
    for name in ("a", "u", "v", "b"):
        lo, hi = (HEIGHT_BOUNDS[name] if name in HEIGHT_BOUNDS else
                  ((F(-13, 200), F(17, 250)) if beta == 0 else
                   (F(-51, 500), F(-1, 1000))))
        lower, upper = endpoints(coordinates[name].imag)
        heights[name] = {"necessary_open_interval": [str(lo), str(hi)],
                         "whole_box_strictly_contained": lo < lower <= upper < hi}
    ordinary = (".267", ".433", "-.065", ".068") if beta == 0 else (
        ".24", ".36", "-.102", "-.001")
    ranges = {
        "e": (".333", ".363", "-.051", "-.019"),
        "xi": (".217", ".234", ".027", ".045"),
        "a": (".246", ".350", "-.078", "-.020"),
        "u": (".24", ".36", "-.102", "-.001"),
        "z": (".24", ".36", "-.102", "-.001"), "v": ordinary, "b": ordinary,
    }
    necessary = {}
    for name, limits in ranges.items():
        necessary[name] = {"rectangle": rectangle_record(coordinates[name], limits)}
        if name not in ("e", "xi"):
            necessary[name]["disk"] = disk_record(
                coordinates[name], 3+beta if name in ("v", "b") else 4)
    outside = coordinates["c"]
    x, h = endpoints(outside.real), endpoints(outside.imag)
    external = {}
    for kind, lo, hi in ((3, F(-9, 125), F(17, 250)), (4, F(-27, 250), F(-1, 1000))):
        disk = disk_record(outside, kind)
        oblique_hi, oblique_lo = x[1]-3*h[0], x[0]-3*h[1]
        contained = disk["whole_box_contained"] and lo <= h[0] <= h[1] <= hi
        disjoint = disk["strictly_disjoint"] or h[1] < lo or h[0] > hi
        if kind == 3:
            contained = contained and oblique_hi <= F(76, 125)
            disjoint = disjoint or oblique_lo > F(76, 125)
        external[str(kind)] = {
            "disk": disk, "height_interval": [str(lo), str(hi)],
            "oblique_upper_rational": str(oblique_hi) if kind == 3 else None,
            "oblique_lower_rational": str(oblique_lo) if kind == 3 else None,
            "whole_box_contained": contained, "necessarily_disjoint": disjoint,
        }
    return {
        "common_prefix_product": common,
        "common_prefix_product_contains_full_boxes": all(x["whole_box_contained"] for x in common.values()),
        "boundary_extension_height_conditions": heights,
        "boundary_extension_height_conditions_verified": all(
            x["whole_box_strictly_contained"] for x in heights.values()),
        "necessary_reference_domain_containments": necessary,
        "external_typed_domains": external,
        "external_scope": "canonical references at c in supplied box intersected with K3 or K4",
        "no_coordinate_intersections_performed": True,
    }


def evaluate_response(coordinates, qprime, beta, *, pi=None):
    """Enclose pL', pR' and B for alpha=1 from full certified input boxes.

    coordinates has e,xi,a,u,z,v,b,c; qprime has exactly the first
    seven names and encloses derivatives with respect to the same c.
    Neither existence nor derivative validity is established here.
    """
    if beta not in (0, 1) or set(coordinates) != set(NAMES+("c",)) or set(qprime) != set(NAMES):
        raise ValueError("wrong flag or canonical coordinate/derivative inventory")
    result = {
        "status": "inconclusive", "alpha": 1, "beta": beta,
        "derivative_order": list(NAMES), "derivative_variable": "c",
        "canonical_existence_certified_here": False,
        "qprime_certified_here": False,
        "requires_certified_common_canonical_reference_and_qprime": True,
        "coordinate_clipping_performed": False,
        "reference_root_evaluations": 0, "matrix_inverse_evaluations": 0,
        "scalar_budget_evaluations": 0, "details": {}, "counts": {},
    }
    details, counts = result["details"], result["counts"]
    try:
        details["coordinates"] = {name: complex_record(coordinates[name]) for name in NAMES+("c",)}
        details["qprime"] = {name: complex_record(qprime[name]) for name in NAMES}
        details["domain_checks"] = domain_records(coordinates, beta)
        if pi is None:
            pi = arb.pi()
            counts["pi_enclosures"] = 1
        else:
            counts["pi_enclosures"] = 0
        pi_lo, pi_hi = endpoints(pi)
        if not F(157, 50) < pi_lo <= pi_hi < F(22, 7):
            raise Inconclusive("pi enclosure lacks the required rational witnesses")
        details["pi"] = real_record(pi)
        ii = acb(0, 1)
        a, u, v, b = (coordinates[name] for name in ("a", "u", "v", "b"))
        ap, up, vp, bp = (qprime[name] for name in ("a", "u", "v", "b"))
        arguments = {"a": a, "a+u": a+u, "b": b, "v+b": v+b}
        curvatures = {}
        details["original_J_second_derivatives"] = {}
        for name, w in arguments.items():
            x_lo, x_hi = endpoints(w.real)
            if not 0 < x_lo <= x_hi < 1:
                raise Inconclusive("whole cotangent argument leaves original strip: "+name)
            angle = pi*w
            sine, cosine = angle.sin(), angle.cos()
            counts["sine_calls"] = counts.get("sine_calls", 0)+1
            counts["cosine_calls"] = counts.get("cosine_calls", 0)+1
            sx, sy = endpoints(sine.real), endpoints(sine.imag)
            separated = sx[0] > 0 or sx[1] < 0 or sy[0] > 0 or sy[1] < 0
            saved = {"argument": complex_record(w), "sine": complex_record(sine),
                     "cosine": complex_record(cosine), "cartesian_sine_separation": separated}
            details["original_J_second_derivatives"][name] = saved
            if not separated:
                raise Inconclusive("cotangent denominator not separated on whole box: "+name)
            value = pi*cosine/sine
            saved["pi_cotangent"] = complex_record(value)
            curvatures[name] = value
        K_a, K_au, K_b, K_vb = (curvatures[name] for name in ("a", "a+u", "b", "v+b"))
        # g''=J''-i*pi. These include the original chirp and both allocated halfweights.
        L_a = K_au-(arb(3)/2)*K_a+ii*pi/2
        L_u = K_au+ii*pi
        R_v = K_vb-ii*pi
        R_b = K_vb-(1+arb(beta)/2)*K_b+ii*pi*beta/2
        pLprime, pRprime = L_a*ap+L_u*up, R_v*vp+R_b*bp
        left, right = pLprime*ap, pRprime*bp
        details["marginal_response_coefficients"] = {
            name: complex_record(value) for name, value in
            (("L_a", L_a), ("L_u", L_u), ("R_v", R_v), ("R_b", R_b))}
        details["pLprime"], details["pRprime"] = complex_record(pLprime), complex_record(pRprime)
        details["left_product"], details["right_product"] = complex_record(left), complex_record(right)
        left_modulus, right_modulus = abs(left), abs(right)
        counts["complex_modulus_calls"] = 2
        left_lower, left_upper = endpoints(left_modulus)
        right_lower, right_upper = endpoints(right_modulus)
        if min(left_upper, right_upper) < 0:
            raise Inconclusive("negative upper modulus endpoint")
        details["left_product_modulus"], details["right_product_modulus"] = (
            real_record(left_modulus), real_record(right_modulus))
        height_ok = details["domain_checks"]["boundary_extension_height_conditions_verified"]
        product_ok = details["domain_checks"]["common_prefix_product_contains_full_boxes"]
        result.update({
            "status": "enclosed" if height_ok and product_ok else "inconclusive",
            "B": {"finite": True,
                  "lower_rational": str(max(F(0), left_lower)+max(F(0), right_lower)),
                  "upper_rational": str(left_upper+right_upper)},
            "B_upper_rational": str(left_upper+right_upper),
            "B_upper_components_rational": [str(left_upper), str(right_upper)],
            "height_conditions_verified": height_ok,
            "common_prefix_product_verified": product_ok,
            "reason": ("response and whole-image height/product conditions enclosed; canonical existence and derivative validity remain caller obligations"
                       if height_ok and product_ok else
                       "finite response, but a required whole-image height/product condition is unresolved"),
        })
    except Inconclusive as error:
        result["reason"] = str(error)
    return result


evaluate = evaluate_response
