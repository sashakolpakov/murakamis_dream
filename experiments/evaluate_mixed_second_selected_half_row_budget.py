"""Two half-row scalar upper bounds on an already certified reference.

Import-safe: only standard-library definitions are loaded here. There is
no root, reference, source, parameter-cover or command-line execution.
The caller supplies the frozen original evaluator and centered primitive.
"""
from fractions import Fraction as F
import hashlib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OLD = "experiments/diagnose_mixed_second_selected_central_budget.py"
FOUR = "experiments/diagnose_mixed_four_four_half_row_budget.py"
FROZEN = "experiments/certify_mixed_selected_half_row_budget.py"
SPEC = "notes/research_mixed_second_selected_half_row_evaluation.md"
PINNED = {
    SPEC: "4ed8584c2ee32c2f31d24a3e8b1dca73fc6edaff0fa2e078bfda9af6f6ca134f",
    "notes/research_mixed_second_selected_half_row_budget.md":
        "784c71292d450c201c1b591f977eec424f4ec92ee90d2bee4465ec47c2685788",
    OLD: "fa99e0b8de2a9b2bb4bf999f6057024dcf4500c35b5173638961ad226251e9ce",
    FOUR: "cc1d86c233ef74f343796b6ad64967ca8a86c8dd315546b1de7c440cd9f9f82f",
    FROZEN: "c3fcced82e6677c65f7f76242e9ca7b00712e236d50a3608bca589e5456f0f34",
    "notes/research_mixed_centered_primitive_enclosure.md":
        "ce2bebcca5ff53ca466948517f4324123b09bb7c92c6736409ff47ece9aac956",
    "notes/research_mixed_second_selected_reference_curve.md":
        "4a591366418d251cbcfaad5705ff439747a8745cc8e75f64561e70aec3ef5bd5",
    "notes/research_mixed_second_selected_horizontal_concavity.md":
        "dac208b242a8dd24f1ce0c29e15775bd343554e0cb0141e2ad84c0fe64312ca8",
}
HEIGHT = F(1, 100)
PLATEAU = (F(11, 50), F(9, 20))
MU_SELECTED = (F(32, 5), F(69, 10))
MU_OUTGOING = (F(57, 10), F(41, 10))
CALL_CAPS = {
    "half_row_branch_attempts": 2,
    "half_row_direct_log_abs_calls": 6,
    "half_row_direct_primitive_calls": 9,
    "half_row_quadratic_calculations": 3,
    "node_conjugates": 1,
    "centered_primitive_calls": 11,
}


def initialize():
    """Verify metadata only; merge inherited provider bindings in the caller."""
    bindings = dict(PINNED)
    for name, expected in bindings.items():
        if hashlib.sha256((ROOT/name).read_bytes()).hexdigest() != expected:
            raise ValueError("half-row input mismatch: "+name)
    path = Path(__file__).resolve()
    bindings[str(path.relative_to(ROOT))] = hashlib.sha256(path.read_bytes()).hexdigest()
    return {
        "bindings": bindings, "alpha": 1, "beta_cases": [0, 1],
        "height_rational": str(HEIGHT),
        "target_interval": [str(q) for q in PLATEAU],
        "call_caps": dict(CALL_CAPS),
        "reference_calls": 0, "source_calls": 0,
    }


def _method_file(method):
    return Path(method.__func__.__code__.co_filename).resolve()


def _check_provider(e):
    if _method_file(e.conjugate) != (ROOT/OLD).resolve():
        raise ValueError("unexpected original conjugate provider")
    if _method_file(e.p.g) != (ROOT/OLD).resolve():
        raise ValueError("use old.make_primitive_class(four) as the primitive")
    if Path(e.f.__file__).resolve() != (ROOT/FROZEN).resolve():
        raise ValueError("unexpected original interval provider")
    mro_files = {
        Path(cls.__dict__["g"].__code__.co_filename).resolve()
        for cls in type(e.p).__mro__ if "g" in cls.__dict__
    }
    if not {(ROOT/OLD).resolve(), (ROOT/FOUR).resolve(),
            (ROOT/FROZEN).resolve()}.issubset(mro_files):
        raise ValueError("centered primitive inheritance differs from frozen providers")
    if not hasattr(e.p, "counts"):
        raise ValueError("counted original centered primitive is required")


def quadratic_upper(force_bounds, center_bounds, curvature,
                    target=PLATEAU):
    """Exact upper endpoint for both signed clipped quadratic displacements."""
    p_lo, p_hi = map(F, force_bounds)
    c_lo, c_hi = map(F, center_bounds)
    lo, hi = map(F, target)
    mu = F(curvature)
    if not (p_lo <= p_hi and lo <= c_lo <= c_hi <= hi and mu > 0):
        raise ValueError("invalid quadratic data")
    sides = {}
    for label, force, length in (
        ("negative", max(F(0), -p_lo), c_hi-lo),
        ("positive", max(F(0), p_hi), hi-c_lo),
    ):
        displacement = min(length, force/mu)
        upper = force*displacement-mu*displacement**2/2
        sides[label] = {
            "nonnegative_force_upper_rational": str(force),
            "displacement_length_upper_rational": str(length),
            "clipped_displacement_rational": str(displacement),
            "gain_upper_rational": str(upper),
        }
    clipped = max(F(item["gain_upper_rational"]) for item in sides.values())
    unrestricted = max(p_lo*p_lo, p_hi*p_hi)/(2*mu)
    upper = min(clipped, unrestricted)
    return upper, {
        "force_interval": [str(p_lo), str(p_hi)],
        "center_interval": [str(c_lo), str(c_hi)],
        "target_interval": [str(lo), str(hi)],
        "curvature_lower_rational": str(mu),
        "sides": sides,
        "clipped_upper_rational": str(clipped),
        "unrestricted_upper_rational": str(unrestricted),
        "selected_method": ("clipped" if clipped <= unrestricted else "unrestricted"),
        "upper_rational": str(upper),
        "meaning": "exact rational upper majorant, not a phase enclosure",
    }


def evaluate_reference(e, shapes, coordinates, beta, gap=F(1, 2000)):
    """Evaluate both full-P half-row branches once, with no reference callback."""
    if beta not in (0, 1):
        raise ValueError("beta must be zero or one")
    gap = F(gap)
    if gap <= 0:
        raise ValueError("the candidate gap must be positive")
    _check_provider(e)
    from flint import acb, ctx

    f, p = e.f, e.p
    before_e, before_p = dict(e.counts), dict(p.counts)
    e.counts["half_row_reference_attempts"] += 1
    details = {"branches": {}, "coordinate_checks": {}, "logarithms": {},
               "primitive_values": {}}
    output = {
        "status": "inconclusive", "alpha": 1, "beta": beta,
        "candidate_gap": str(gap), "height_rational": str(HEIGHT),
        "both_branches_use_full_plateau": True,
        "fully_evaluated_pair": False, "proved_margin_lower_rational": None,
        "reference_existence_certified": False,
        "scope": "upper bounds for the same supplied original stationary reference",
        "precision_bits": int(ctx.prec), "details": details,
        "additional_reference_calls": 0, "additional_source_calls": 0,
    }

    def finish():
        counts = {name: e.counts.get(name, 0)-before_e.get(name, 0)
                  for name in set(e.counts) | set(before_e)}
        counts = {name: value for name, value in counts.items() if value}
        counts["centered_primitive_calls"] = (
            p.counts.get("centered_primitive_calls", 0)
            -before_p.get("centered_primitive_calls", 0))
        if any(counts.get(name, 0) > limit for name, limit in CALL_CAPS.items()):
            raise RuntimeError("half-row evaluator exceeded its fixed arithmetic call caps")
        if any(value < 0 for value in counts.values()):
            raise RuntimeError("provider counter moved backwards")
        output["counts"], output["call_caps"] = counts, dict(CALL_CAPS)
        return output

    def bounds(w):
        e.finite(w, "half-row real input")
        return f.lower(w), f.upper(w)

    def quadratic(force, center, curvature):
        e.counts["half_row_quadratic_calculations"] += 1
        return quadratic_upper(bounds(force), bounds(center), curvature)

    try:
        pi, ii, height = p.pi, p.ii, f.rat(HEIGHT)
        details["pi"] = f.real_record(e.finite(pi, "pi"))
        right_range = (F(267, 1000), F(433, 1000), -F(13, 200), F(17, 250)) \
            if beta == 0 else (F(6, 25), F(9, 25), -F(51, 500), -F(1, 1000))
        ranges = {
            "a": (*PLATEAU, -F(39, 500), F(21, 1000)),
            "u": (F(6, 25), F(9, 25), -F(51, 500), -F(1, 1000)),
            "z": (F(6, 25), F(9, 25), -F(51, 500), -F(1, 1000)),
            "v": right_range, "b": right_range,
        }
        details["coordinates"] = {
            name: f.complex_record(coordinates[name]) for name in ranges}
        details["negative_shapes"] = {
            name: f.complex_record(shapes[name]) for name in ("u", "z", "v", "b")}
        for name, (lo, hi, hlo, hhi) in ranges.items():
            w = e.finite(coordinates[name], name+" coordinate")
            real, imag = bounds(w.real), bounds(w.imag)
            contained = (lo <= real[0] <= real[1] <= hi
                         and hlo <= imag[0] <= imag[1] <= hhi)
            details["coordinate_checks"][name] = {
                "required_rectangle": [str(q) for q in (lo, hi, hlo, hhi)],
                "whole_box_contained": contained,
            }
            if not contained:
                raise f.Inconclusive("containing reference range not certified: "+name)
        for name in ("u", "z", "v", "b"):
            e.finite(shapes[name], name+" negative shape")
        u, z, v, b = (coordinates[name] for name in ("u", "z", "v", "b"))
        U, Z, V, B = (shapes[name] for name in ("u", "z", "v", "b"))
        zH = acb(z.real, height)
        half = f.rat(F(1, 2))
        lam = e.finite((2*pi*(height-z.imag)).exp(), "radial multiplier")
        details["radial_multiplier"] = f.real_record(lam)
        if not lam > 0:
            raise f.Inconclusive("radial multiplier not outward positive")
        log_arguments = {
            "L1": 1-lam*U*Z, "L0": 1-U*Z, "Lplus": 1+lam*Z,
            "Lminus": 1-lam*Z, "Lb": 1+B, "Lvb": 1-V*B,
        }
        logs = {}
        for name, argument in log_arguments.items():
            e.counts["half_row_direct_log_abs_calls"] += 1
            details["logarithms"][name] = {"argument": f.complex_record(argument)}
            logs[name] = e.finite(p.log_abs(argument), name+" logarithmic modulus")
            details["logarithms"][name]["value"] = f.real_record(logs[name])
        A, Db = logs["L1"]-logs["L0"], logs["Lb"]-logs["Lvb"]
        details["common_forces"] = {"A": f.real_record(A), "D_b": f.real_record(Db)}
        if not A > 0:
            raise f.Inconclusive("positive left-index force not outward certified")

        arguments = {
            "u_plus_zH": u+zH, "u_plus_z": u+z,
            "half_plus_zH": half+zH, "v_plus_z": v+z,
            "half_plus_b": half+b, "v_plus_b": v+b,
            "v": v, "z": z, "zH": zH,
        }
        values = {}
        for name, argument in arguments.items():
            details["primitive_values"][name] = {"argument": f.complex_record(argument)}
            p.regular(argument)
            e.counts["half_row_direct_primitive_calls"] += 1
            values[name] = e.finite(p.g(argument), "original g at "+name)
            details["primitive_values"][name]["value"] = f.complex_record(values[name])
        ghalf = ii*pi/8
        chirp = 2*pi*ii*(half*zH-z*v)
        common_trial = (
            values["u_plus_zH"]-values["u_plus_z"]
            +values["half_plus_zH"]-values["v_plus_z"]
            +values["half_plus_b"]-values["v_plus_b"]
            -(2+beta)*(ghalf-values["v"])
            +3*values["z"]-2*values["zH"]+chirp
        )
        details["trial"] = {
            "g_half_exact_formula": "i*pi/8",
            "g_half": f.complex_record(ghalf),
            "original_chirp": f.complex_record(chirp),
            "common_complex_trial_before_nu": f.complex_record(common_trial),
        }
        left, left_record = e.conjugate(
            A, u.real, u.imag, F(1), F(11, 50), F(1, 2),
            zero=False, zero_edge=False,
        )
        e.finite(left, "left-index conjugate")
        details["left_index_gain"] = left_record
        outgoing, outgoing_record = quadratic(Db, b.real, MU_OUTGOING[beta])
        details["outgoing_gain"] = outgoing_record
        for nu, label in ((0, "forced"), (1, "factorial")):
            e.counts["half_row_branch_attempts"] += 1
            Pnu = e.finite(logs["L1"]+logs["Lplus"]-(2+nu)*logs["Lminus"],
                          "selected half-row force")
            Tnu = e.finite((common_trial-nu*values["zH"]).real-2*nu*pi*height,
                          "literal relative half-row trial")
            selected, selected_record = quadratic(Pnu, z.real, MU_SELECTED[nu])
            components = (f.upper(Tnu), f.upper(left), selected, outgoing)
            upper = sum(components, F(0))
            details["branches"][label] = {
                "nu": nu, "selected_target_interval": [str(q) for q in PLATEAU],
                "P_nu": f.real_record(Pnu), "T_nu": f.real_record(Tnu),
                "selected_gain": selected_record,
                "component_upper_rationals": {
                    name: str(value) for name, value in
                    zip(("trial", "left", "selected", "outgoing"), components)},
                "budget": {
                    "finite": True, "lower_rational": str(upper),
                    "upper_rational": str(upper),
                    "meaning": "exact rational upper majorant, not a phase enclosure",
                },
                "strictly_below_zero": upper < 0,
                "strictly_below_candidate_gap": upper < -gap,
            }
        passed = all(branch["strictly_below_zero"] for branch in details["branches"].values())
        output.update({
            "status": "accepted" if passed else "inconclusive",
            "reason": ("both full-P half-row upper bounds strictly negative" if passed
                       else "both half-row majorants finite; negativity not certified"),
            "fully_evaluated_pair": True,
            "proved_margin_lower_rational": str(min(
                -F(branch["budget"]["upper_rational"])
                for branch in details["branches"].values())) if passed else None,
        })
        return finish()
    except f.Inconclusive as error:
        output["reason"] = str(error)
        return finish()
