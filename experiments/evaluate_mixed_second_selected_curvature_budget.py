"""Optional rational improvements of the frozen directional upper bounds.

No parameter, interval, primitive or source work occurs on import.
evaluate_reference calls the frozen helper once; refine_saved_result is
pure rational postprocessing. Neither function proves reference existence.
"""
from fractions import Fraction as F
import hashlib
import importlib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FROZEN = "experiments/evaluate_mixed_second_selected_directional_budget.py"
PINNED = {
    FROZEN: "650a2a1319853df03430c267f28a5ffdc67b4bf7c7576e392cb3f22fbbe4c541",
    "notes/research_mixed_second_selected_directional_budget.md":
        "f74ddbea9c59685e7c6d343c7b41490c1c81520d09016664f274ff003331efd2",
    "notes/research_mixed_second_selected_local_curvature_gains.md":
        "cb149020a95c582a8c686522c37bda3771a731201600be4c195f1e550ce443bd",
    "notes/research_mixed_second_selected_central_budget.md":
        "c839f134024ccd2ad0a95ce81ed8cd16fb0bcefb9d508a347c9278c84bd3f21d",
}
HEIGHT = F(1, 100)


def interval(record):
    if record.get("finite") is not True:
        raise ValueError("a rational refinement requires finite saved endpoints")
    lo, hi = F(record["lower_rational"]), F(record["upper_rational"])
    if lo > hi:
        raise ValueError("reversed saved endpoints")
    return lo, hi


def candidate(method, upper, witness=None):
    return {"method": method, "upper_rational": str(F(upper)),
            "witness": {} if witness is None else witness}


def minimum(candidates):
    if not candidates:
        raise ValueError("empty upper-bound inventory")
    winner = min(range(len(candidates)),
                 key=lambda i: F(candidates[i]["upper_rational"]))
    return {"candidates": candidates, "selected_candidate_index": winner,
            "upper_rational": candidates[winner]["upper_rational"]}


def complete_pair(result):
    branches = result.get("details", {}).get("branches", {})
    try:
        for label in ("forced", "factorial"):
            interval(branches[label]["budget"])
    except (KeyError, TypeError, ValueError, ZeroDivisionError):
        return False
    return True


def refine_saved_result(original, enclosures, beta, gap=F(1, 2000)):
    """Refine a complete pair using only exact rational endpoint arithmetic.

    enclosures contains coordinates u,z,v, negative-sign shape v, and pi.
    Each real interval has finite/lower_rational/upper_rational fields.
    Its caller must bind the original result and common-reference enclosures.
    """
    gap = F(gap)
    if beta not in (0, 1) or gap <= 0 or original.get("beta") != beta:
        raise ValueError("invalid beta, gap or frozen-result association")
    output = {
        "status": "inconclusive", "beta": beta, "candidate_gap": str(gap),
        "fully_evaluated_pair": False, "proved_margin_lower_rational": None,
        "reference_existence_certified": False,
        "geometric_admissibility_checked": False,
        "scope": "upper bounds only for actual original references in the supplied enclosures",
        "details": {"frozen_result": original, "input_enclosures": enclosures,
                    "branches": {}, "hypothesis_checks": {}},
    }
    if not complete_pair(original):
        output["reason"] = "frozen pair arithmetically incomplete; no extra branch attempted"
        return output
    saved = original["details"]
    scalars, old_branches = saved["scalars"], saved["branches"]
    coords = enclosures["coordinates"]
    u, z, v = {axis: interval(coords["u"][axis]) for axis in ("real", "imag")}, \
              {axis: interval(coords["z"][axis]) for axis in ("real", "imag")}, \
              {axis: interval(coords["v"][axis]) for axis in ("real", "imag")}
    pi_lo, pi_hi = interval(enclosures["pi"])
    if not (F(157, 50) < pi_lo <= pi_hi < F(22, 7)):
        raise ValueError("the supplied pi enclosure lacks the stated rational witnesses")
    A_lo, A_hi = interval(scalars["A"])
    d_lo, d_hi = interval(scalars["d"])
    if A_lo <= 0 or d_lo <= 0:
        raise ValueError("a complete frozen pair must have separated directional signs")
    checks = output["details"]["hypothesis_checks"]

    left = [candidate("frozen left conjugate",
                      interval(saved["left_index_gain"]["value"])[1])]
    local_u = (F(5, 16) < u["real"][0] <= u["real"][1] < F(63, 200)
               and -F(9, 200) < u["imag"][0] <= u["imag"][1] < F(9, 200)
               and A_hi < F(33, 200))
    checks["local_left_cubic"] = local_u
    if local_u:
        left.append(candidate("local left cubic", F(2691, 204800),
                              {"A_upper_rational": str(A_hi),
                               "center_curvature_lower_rational": "39/20",
                               "third_derivative_absolute_upper_rational": "15",
                               "enlarged_displacement_upper_rational": "3/16"}))

    right = [candidate("frozen right quadratic",
                       F(saved["right_index_gain"]["gain_upper_rational"]))]
    local_v = (beta == 0
               and F(1, 3) < v["real"][0] <= v["real"][1] < F(3, 8)
               and -F(1, 50) < v["imag"][0] <= v["imag"][1] < F(1, 50))
    checks["local_right_curvature"] = local_v
    if local_v:
        right.append(candidate("local right curvature", d_hi*d_hi/(2*F(471, 265)),
                               {"force_upper_rational": str(d_hi),
                                "curvature_lower_rational": "471/265"}))
    checks["negative_shape_cotangent"] = False
    if beta == 0:
        shape = enclosures["negative_shapes"]["v"]
        x_lo, x_hi = interval(shape["real"])
        y_lo, y_hi = interval(shape["imag"])
        if y_hi < 0:
            denominator = max((1-x_lo)**2, (1-x_hi)**2)+max(y_lo*y_lo, y_hi*y_hi)
            cot_lower = -2*y_hi/denominator
            delta_lower = max(F(1, 5), min(cot_lower, F(15, 53)))
            mu_lower = 2*pi_lo*delta_lower
            length = v["real"][1]-F(1, 5)
            if length < 0:
                raise ValueError("negative right-index displacement limit")
            displacement = min(d_hi/mu_lower, length)
            gain = d_hi*displacement-mu_lower*displacement**2/2
            checks["negative_shape_cotangent"] = True
            right.append(candidate("negative-shape cotangent curvature", gain, {
                "numerator_lower_rational": str(-2*y_hi),
                "denominator_upper_rational": str(denominator),
                "cotangent_lower_rational": str(cot_lower),
                "delta_lower_rational": str(delta_lower),
                "pi_lower_rational": str(pi_lo),
                "curvature_lower_rational": str(mu_lower),
                "force_upper_rational": str(d_hi),
                "displacement_limit_upper_rational": str(length),
                "maximizing_enlarged_displacement_rational": str(displacement),
            }))

    vertical = [candidate("frozen exact vertical enclosure",
                          interval(scalars["exact_vertical_cost"])[1])]
    real_v_limits = (F(267, 1000), F(433, 1000)) if beta == 0 else (F(6, 25), F(9, 25))
    vertical_guard = (
        F(6, 25) <= u["real"][0] <= u["real"][1] <= F(9, 25)
        and F(6, 25) <= z["real"][0] <= z["real"][1] <= F(9, 25)
        and real_v_limits[0] <= v["real"][0] <= v["real"][1] <= real_v_limits[1]
        and z["imag"][1] < HEIGHT)
    checks["stationary_reference_vertical_bound"] = vertical_guard
    if vertical_guard:
        delta_hi = HEIGHT-z["imag"][0]
        coefficient = F(33, 5) if beta == 0 else F(429, 70)
        vertical.append(candidate("stationary reference curvature", coefficient*delta_hi**2,
                                  {"height_displacement_upper_rational": str(delta_hi),
                                   "quadratic_coefficient_upper_rational": str(coefficient),
                                   "requires_original_stationary_reference": True}))
    component = {"left": minimum(left), "right": minimum(right), "vertical": minimum(vertical)}
    output["details"]["component_bounds"] = component
    left_hi, right_hi, vertical_hi = (F(component[name]["upper_rational"])
                                     for name in ("left", "right", "vertical"))
    gz_hi = interval(scalars["g_zH_real"])[1]

    for label, nu in (("forced", 0), ("factorial", 1)):
        old = old_branches[label]
        selected = [candidate("frozen signed selected conjugate",
                              interval(old["selected_gain"]["value"])[1])]
        D_lo, D_hi = interval(old["D_nu"])
        local_z = (nu == 1 and D_hi < 0
                   and F(11, 50) < z["real"][0] <= z["real"][1] < F(7, 25))
        checks[label+"_local_selected_curvature"] = local_z
        if local_z:
            selected.append(candidate("downward factorial curvature", D_lo**2/10,
                                      {"force_lower_rational": str(D_lo),
                                       "curvature_lower_rational": "5"}))
        selected_bound = minimum(selected)
        trial = minimum([
            candidate("frozen trial enclosure", interval(old["T_nu"])[1]),
            candidate("selected vertical bound and literal Fourier term",
                      vertical_hi+gz_hi if nu == 0 else vertical_hi-pi_lo/50),
        ])
        sum_upper = F(trial["upper_rational"])+left_hi+right_hi+F(selected_bound["upper_rational"])
        final = minimum([
            candidate("frozen complete branch upper", interval(old["budget"])[1]),
            candidate("sum of four component upper bounds", sum_upper,
                      {"components": ["trial", "left", "right", "selected"],
                       "each_component_counted_once": True}),
        ])
        upper = F(final["upper_rational"])
        output["details"]["branches"][label] = {
            "nu": nu, "trial_bound": trial, "selected_bound": selected_bound,
            "selected_gain_keeps_its_sign": True, "final_bound": final,
            "budget": {"finite": True, "lower_rational": str(upper),
                       "upper_rational": str(upper),
                       "meaning": "exact rational upper majorant, not an enclosure of the phase value"},
            "strictly_below_zero": upper < 0,
            "strictly_below_candidate_gap": upper < -gap,
        }
    branches = output["details"]["branches"]
    passed = all(branch["strictly_below_zero"] for branch in branches.values())
    output.update({
        "status": "accepted" if passed else "inconclusive",
        "reason": ("both refined upper majorants strictly negative" if passed
                   else "both refined majorants finite; strict negativity not certified"),
        "fully_evaluated_pair": True,
        "proved_margin_lower_rational": str(min(
            -F(branch["budget"]["upper_rational"]) for branch in branches.values())) if passed else None,
        "additional_primitive_calls": 0, "additional_conjugate_calls": 0,
        "additional_reference_calls": 0,
    })
    return output


def postprocess(e, original, shapes, coordinates, beta, gap=F(1, 2000)):
    """Read existing endpoints only; never call the frozen helper or primitive."""
    if not complete_pair(original):
        return refine_saved_result(original, {}, beta, gap)
    def real(value):
        if not value.is_finite():
            raise ValueError("nonfinite common-reference enclosure")
        return {"finite": True, "lower_rational": str(e.f.lower(value)),
                "upper_rational": str(e.f.upper(value))}
    def complex_record(value):
        return {"real": real(value.real), "imag": real(value.imag)}
    enclosures = {
        "coordinates": {name: complex_record(coordinates[name]) for name in ("u", "z", "v")},
        "negative_shapes": {"v": complex_record(shapes["v"])}, "pi": real(e.p.pi),
    }
    result = refine_saved_result(original, enclosures, beta, gap)
    result["postprocessing_only"] = True
    return result


def evaluate_reference(e, shapes, coordinates, beta, gap=F(1, 2000)):
    """Call the unchanged frozen helper once, then refine its complete pair."""
    def verify():
        for name, expected in PINNED.items():
            if hashlib.sha256((ROOT/name).read_bytes()).hexdigest() != expected:
                raise ValueError("curvature-wrapper dependency mismatch: "+name)
    verify()
    frozen = importlib.import_module("evaluate_mixed_second_selected_directional_budget")
    if Path(frozen.__file__).resolve() != (ROOT/FROZEN).resolve():
        raise ValueError("unexpected frozen-helper module location")
    original = frozen.evaluate_reference(e, shapes, coordinates, beta, gap)
    result = postprocess(e, original, shapes, coordinates, beta, gap)
    verify()
    result["input_sha256"] = dict(PINNED)
    result["frozen_helper_calls"] = 1
    return result
