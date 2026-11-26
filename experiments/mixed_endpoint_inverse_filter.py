"""Necessary four/four endpoint-input tests; no roots or source evaluations.

The caller supplies an enclosure of b and of the original attached root
E_4(b), valid on the same whole parameter box. All inconclusive interval
tests retain the box. Exclusion requires separate length-two and
length-at-least-three proofs.
"""
from fractions import Fraction as F

from flint import acb, arb


def rational(value):
    value = F(value)
    return arb(value.numerator)/value.denominator


def disk_test(z, real, imag, radius):
    center = acb(rational(real), rational(imag))
    d = z-center
    separation = d.real**2+d.imag**2-rational(radius)**2
    return dict(squared_distance_minus_radius_squared=str(separation),
                strictly_disjoint=bool(separation > 0))


def evaluate(b, attached):
    """Return sufficient exclusion evidence, never a feasibility assertion.

    Only string reason codes are suitable as saved witnesses: interval
    display strings can change at a different replay precision.
    """
    result = dict(excluded=False, m2_excluded=False, m3_excluded=False,
                  m2_reasons=[], m3_reasons=[], input=str(b),
                  endpoint_attached=str(attached))
    if not (b.is_finite() and attached.is_finite()):
        result["unresolved"] = "nonfinite supplied enclosure"
        return result
    if b.real < rational(F(69, 250)):
        result["m2_reasons"].append("attached_real_floor")
    if abs(b-attached) > 0:
        result["m2_reasons"].append("attached_fixed_point")
    result["m2_excluded"] = bool(result["m2_reasons"])
    pi, ii = arb.pi(), acb(0, 1)
    U, A = (-2*pi*ii*b).exp(), (-2*pi*ii*attached).exp()
    denominator = 1-U*A
    if not all(z.is_finite() for z in (U, A, denominator)):
        result["unresolved"] = "nonfinite exponential enclosure"
        return result
    if not (abs(U) > 0 and abs(denominator) > 0):
        result["unresolved"] = "first denominator not separated from zero"
        return result
    one_minus_UV = A*(1-U)**3/denominator
    if not (one_minus_UV.is_finite() and abs(one_minus_UV) > 0):
        result["unresolved"] = "second denominator not separated from zero"
        return result
    V = (1-one_minus_UV)/U
    W = V+(1-V)**3/one_minus_UV
    if not (V.is_finite() and W.is_finite()):
        result["unresolved"] = "nonfinite inverse enclosure"
        return result
    result.update(inverse_V=str(V), inverse_W=str(W))
    if V.imag >= 0:
        result["m3_reasons"].append("opposite_half_plane")
    if W.imag <= 0:
        result["m3_reasons"].append("external_half_plane")
    if V.imag < 0:
        t = -V.log()/(2*pi*ii)
        if t.is_finite():
            result["ordinary_opposite_leg"] = str(t)
            result["t_P4"] = disk_test(t, F(3, 10), F(-13, 250), F(3, 50))
            if result["t_P4"]["strictly_disjoint"]:
                result["m3_reasons"].append("opposite_outside_P4")
    if W.imag > 0:
        c = W.log()/(2*pi*ii)
        if c.is_finite():
            result["next_external_leg"] = str(c)
            result["c_P3"] = disk_test(c, F(7, 20), F(-1, 100), F(83, 1000))
            result["c_P4"] = disk_test(c, F(3, 10), F(-13, 250), F(3, 50))
            if result["c_P3"]["strictly_disjoint"] and result["c_P4"]["strictly_disjoint"]:
                result["m3_reasons"].append("external_outside_both_P")
    result["m3_excluded"] = bool(result["m3_reasons"])
    result["excluded"] = result["m2_excluded"] and result["m3_excluded"]
    return result


def witness(result):
    """Choose one certified reason for each disjoint word-length case."""
    assert result["excluded"] and result["m2_excluded"] and result["m3_excluded"]
    return dict(m2=result["m2_reasons"][0], m3=result["m3_reasons"][0])


def validate_witness(saved, result):
    """Recheck saved sufficient reasons without comparing decimal displays."""
    assert isinstance(saved, dict) and set(saved) == {"m2", "m3"}
    assert result["excluded"]
    assert saved["m2"] in result["m2_reasons"]
    assert saved["m3"] in result["m3_reasons"]
