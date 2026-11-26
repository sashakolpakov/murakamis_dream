"""Outward three-gain central budgets on an already enclosed reference.

No execution on import. The caller supplies the frozen Evaluator from
diagnose_mixed_second_selected_central_budget, with its original primitive.
This module does not construct or change reference data.
"""
from fractions import Fraction as F

from flint import acb


def evaluate_reference(e, shapes, coordinates, beta, gap=F(1, 2000)):
    """Return two sufficient central bounds, preserving inconclusive inputs."""
    if beta not in (0, 1):
        raise ValueError("beta must be zero or one")
    gap = F(gap)
    if gap <= 0:
        raise ValueError("the requested strict gap must be positive")
    details = {}
    e.counts["directional_reference_attempts"] += 1
    try:
        f, p = e.f, e.p
        pi, height = p.pi, f.rat(F(1, 100))
        u, z, v = (coordinates[name] for name in ("u", "z", "v"))
        U, Z, V = (shapes[name] for name in ("u", "z", "v"))
        zH = acb(z.real, height)
        lam = e.finite((2*pi*(height-z.imag)).exp(), "radial multiplier")
        if not lam > 0:
            raise f.Inconclusive("radial multiplier not outward positive")
        ell = lam.log()
        A = p.log_abs(1-lam*U*Z)-p.log_abs(1-U*Z)
        B = p.log_abs(1-lam*V*Z)-p.log_abs(1-V*Z)
        C = p.log_abs(1-lam*Z)-p.log_abs(1-Z)
        GH = p.log_abs(1-lam*Z)
        d = ell-B
        gzH = p.g(zH).real
        vertical = (
            (p.g(u+zH)-p.g(u+z)+p.g(v+zH)-p.g(v+z)).real
            -3*gzH+3*p.g(z).real-2*pi*v.real*(height-z.imag)
        )
        scalars = dict(A=A, B=B, C=C, ell=ell, d=d, G_H=GH,
                       radial_multiplier=lam, exact_vertical_cost=vertical,
                       g_zH_real=gzH)
        details["scalars"] = {
            name: f.real_record(e.finite(value, name))
            for name, value in scalars.items()
        }
        if not (A > 0 and d > 0):
            raise f.Inconclusive("directional force signs not outward separated")

        left, left_record = e.conjugate(
            A, u.real, u.imag, F(1), F(11, 50), F(1, 2),
            zero=False, zero_edge=False,
        )
        details["left_index_gain"] = left_record
        q = F(1, 5) if beta == 0 else F(11, 50)
        mu_factor = F(2, 5) if beta == 0 else F(71, 80)
        mu_lower = mu_factor*f.lower(pi)
        d_upper = f.upper(d)
        length_upper = f.upper(v.real)-q
        if min(mu_lower, d_upper, length_upper) <= 0:
            raise f.Inconclusive("invalid right-index quadratic data")
        displacement = min(d_upper/mu_lower, length_upper)
        right_upper = d_upper*displacement-mu_lower*displacement**2/2
        details["right_index_gain"] = {
            "curvature_pi_factor": str(mu_factor),
            "curvature_lower_rational": str(mu_lower),
            "force_upper_rational": str(d_upper),
            "displacement_limit_upper_rational": str(length_upper),
            "maximizing_enlarged_displacement_rational": str(displacement),
            "gain_upper_rational": str(right_upper),
            "target_lower_rational": str(q),
        }
        details["branches"] = {}
        for nu in (0, 1):
            e.counts["directional_branch_attempts"] += 1
            D = A+B-3*C+(1-nu)*GH
            T = vertical+(1-nu)*gzH-2*nu*pi*height
            lo = F(2, 5) if nu == 0 else F(11, 50)
            selected, selected_record = e.conjugate(
                D, z.real, height, F(1+nu), lo, F(9, 20),
                zero=False, zero_edge=False,
            )
            budget = e.finite(T+left+f.rat(right_upper)+selected,
                              "directional central budget")
            upper = f.upper(budget)
            details["branches"]["factorial" if nu else "forced"] = {
                "nu": nu, "D_nu": f.real_record(D), "T_nu": f.real_record(T),
                "selected_gain": selected_record,
                "selected_gain_keeps_its_sign": True,
                "budget": f.real_record(budget),
                "strictly_below_zero": upper < 0,
                "strictly_below_candidate_gap": upper < -gap,
            }
        passed = all(
            branch["strictly_below_zero"]
            for branch in details["branches"].values()
        )
        proved_margin = min(
            -F(branch["budget"]["upper_rational"])
            for branch in details["branches"].values()
        ) if passed else None
        return {
            "status": "accepted" if passed else "inconclusive",
            "reason": ("both restricted branch upper bounds strictly negative"
                       if passed else "strict negativity not certified for both branches"),
            "beta": beta, "candidate_gap": str(gap),
            "proved_margin_lower_rational": str(proved_margin) if passed else None,
            "details": details,
        }
    except e.f.Inconclusive as error:
        return {"status": "inconclusive", "reason": str(error), "beta": beta,
                "candidate_gap": str(gap), "details": details}
