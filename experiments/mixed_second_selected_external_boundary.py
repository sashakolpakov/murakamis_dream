"""Exact boundary charts for the second-selection external-coordinate route.

Only rational geometry and finite address bookkeeping occur here.  No root,
primitive, source, interval library, or scalar comparison is evaluated.
An exclusion removes a whole chart interval only when a necessary defining
inequality of its typed external domain fails strictly.  Equality is retained.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from types import MappingProxyType
from typing import Mapping, Sequence


@dataclass(frozen=True)
class Domain:
    name: str
    cx: F
    cy: F
    radius: F
    height_lower: F
    height_upper: F
    oblique_upper: F | None = None


@dataclass(frozen=True)
class Chart:
    name: str
    domain: str
    kind: str
    sign: int = 0
    x0: F = F(0)
    y0: F = F(0)
    dx: F = F(0)
    dy: F = F(0)


DOMAINS = MappingProxyType({
    "k3": Domain("k3", F(7, 20), -F(1, 100), F(83, 1000),
                 -F(9, 125), F(17, 250), F(76, 125)),
    "k4": Domain("k4", F(3, 10), -F(13, 250), F(3, 50),
                 -F(27, 250), -F(1, 1000)),
})

_CHARTS = (
    Chart("k3_circle_right", "k3", "circle", sign=1),
    Chart("k3_circle_left", "k3", "circle", sign=-1),
    Chart("k3_lower_chord", "k3", "line", x0=F(7, 20),
          y0=-F(9, 125), dx=F(83, 1000)),
    Chart("k3_upper_chord", "k3", "line", x0=F(7, 20),
          y0=F(17, 250), dx=F(83, 1000)),
    Chart("k3_oblique_chord", "k3", "line", x0=F(301, 500),
          y0=-F(1, 500), dx=F(21, 100), dy=F(7, 100)),
    Chart("k4_circle_right", "k4", "circle", sign=1),
    Chart("k4_circle_left", "k4", "circle", sign=-1),
    Chart("k4_lower_chord", "k4", "line", x0=F(3, 10),
          y0=-F(27, 250), dx=F(3, 50)),
    Chart("k4_upper_chord", "k4", "line", x0=F(3, 10),
          y0=-F(1, 1000), dx=F(3, 50)),
)
_BY_NAME = MappingProxyType({chart.name: chart for chart in _CHARTS})


def chartlist():
    """Nine immutable chart descriptors, each with parameter interval [-1,1]."""
    return _CHARTS


def case_list():
    """The exact 18 beta/chart cases for one fixed first flag."""
    return tuple({"beta": beta, "chart": chart.name}
                 for beta in (0, 1) for chart in _CHARTS)


def _chart(chart):
    if isinstance(chart, str):
        if chart not in _BY_NAME:
            raise ValueError("unknown external boundary chart")
        return _BY_NAME[chart]
    if not isinstance(chart, Chart) or _BY_NAME.get(chart.name) != chart:
        raise ValueError("chart differs from the fixed exact inventory")
    return chart


def _fraction(value):
    if isinstance(value, float):
        raise TypeError("boundary parameters must be exact rationals")
    return F(value)


def _parameter(interval):
    if len(interval) != 2:
        raise ValueError("a parameter interval has two endpoints")
    lo, hi = map(_fraction, interval)
    if not -1 <= lo <= hi <= 1:
        raise ValueError("parameter interval outside [-1,1]")
    return lo, hi


def _affine_range(center, slope, interval):
    lo, hi = interval
    values = (center+slope*lo, center+slope*hi)
    return min(values), max(values)


def paramimage(chart, interval):
    """Full exact Cartesian image hull (xlo,xhi,ylo,yhi), as Fractions.

    A semicircle is center + sign*r*(1+i*t)/(1-i*t).  The two
    scalar extrema below are exact on every closed subinterval of [-1,1].
    """
    chart = _chart(chart)
    lo, hi = _parameter(interval)
    if chart.kind == "line":
        return (*_affine_range(chart.x0, chart.dx, (lo, hi)),
                *_affine_range(chart.y0, chart.dy, (lo, hi)))
    domain = DOMAINS[chart.domain]
    near = F(0) if lo <= 0 <= hi else min(abs(lo), abs(hi))
    far = max(abs(lo), abs(hi))
    real_lo = (1-far*far)/(1+far*far)
    real_hi = (1-near*near)/(1+near*near)
    imag_lo = 2*lo/(1+lo*lo)
    imag_hi = 2*hi/(1+hi*hi)
    scale = chart.sign*domain.radius
    return (*_affine_range(domain.cx, scale, (real_lo, real_hi)),
            *_affine_range(domain.cy, scale, (imag_lo, imag_hi)))


def _line_disk_minimum(chart, interval, domain):
    lo, hi = interval
    x0, y0 = chart.x0-domain.cx, chart.y0-domain.cy
    quadratic = chart.dx*chart.dx+chart.dy*chart.dy
    linear = 2*(x0*chart.dx+y0*chart.dy)
    if quadratic == 0:
        trial = lo
    else:
        trial = min(hi, max(lo, -linear/(2*quadratic)))
    distance = (x0+chart.dx*trial)**2+(y0+chart.dy*trial)**2
    return distance, trial


def exactsourceexclusionwitness(chart, interval):
    """Return a JSON-safe strict whole-interval exclusion, or None.

    None means only that these necessary tests did not exclude the chart
    interval.  It does not assert source feasibility or any scalar sign.
    """
    chart = _chart(chart)
    interval = _parameter(interval)
    domain = DOMAINS[chart.domain]
    box = paramimage(chart, interval)
    xlo, xhi, ylo, yhi = box

    def witness(criterion, margin, **details):
        if margin <= 0:
            raise ValueError("an exclusion must have strictly positive margin")
        return {"chart": chart.name, "domain": domain.name,
                "parameter_interval": list(map(str, interval)),
                "coordinate_box": list(map(str, box)),
                "criterion": criterion, "strict_margin_rational": str(margin),
                "details": {key: str(value) for key, value in details.items()}}

    if yhi < domain.height_lower:
        return witness("below_lower_height", domain.height_lower-yhi,
                       image_upper=yhi, required_lower=domain.height_lower)
    if ylo > domain.height_upper:
        return witness("above_upper_height", ylo-domain.height_upper,
                       image_lower=ylo, required_upper=domain.height_upper)
    if domain.oblique_upper is not None:
        if chart.kind == "line":
            lower, _ = _affine_range(chart.x0-3*chart.y0,
                                     chart.dx-3*chart.dy, interval)
            method = "exact_line_linear_range"
        else:
            lower = xlo-3*yhi
            method = "cartesian_image_lower_bound"
        if lower > domain.oblique_upper:
            return witness("above_oblique_halfplane", lower-domain.oblique_upper,
                           image_lower=lower, required_upper=domain.oblique_upper,
                           bound_method=method)
    if chart.kind == "line":
        minimum, trial = _line_disk_minimum(chart, interval, domain)
        radius_squared = domain.radius**2
        if minimum > radius_squared:
            return witness("outside_typed_disk", minimum-radius_squared,
                           squared_distance_minimum=minimum,
                           radius_squared=radius_squared,
                           minimizing_parameter=trial,
                           bound_method="exact_line_quadratic_minimum")
    # Every semicircle point has exact squared distance radius**2.
    return None


def split(interval):
    """Two closed rational halves; their common midpoint is retained in both."""
    lo, hi = _parameter(interval)
    if lo == hi:
        raise ValueError("cannot split a point interval")
    mid = (lo+hi)/2
    return (lo, mid), (mid, hi)


def parameter_interval(address):
    """Decode a binary tree address from the exact root [-1,1]."""
    if not isinstance(address, str) or any(bit not in "01" for bit in address):
        raise ValueError("invalid binary address")
    interval = (-F(1), F(1))
    for bit in address:
        interval = split(interval)[int(bit)]
    return interval


def validate_partition(addresses: Sequence[str]):
    """Check a complete frontier, including every unresolved/pending leaf.

    This validates parameter coverage only.  It does not validate any
    acceptance, exclusion, reference, or scalar witness carried by a leaf.
    """
    addresses = list(addresses)
    if not addresses:
        raise ValueError("empty interval frontier")
    for address in addresses:
        parameter_interval(address)
    ordered = sorted(addresses)
    for left, right in zip(ordered, ordered[1:]):
        if right.startswith(left):
            raise ValueError("duplicate or overlapping binary leaves")
    mass = sum((F(1, 2**len(address)) for address in addresses), F(0))
    if mass != 1:
        raise ValueError("incomplete parameter interval cover")
    return {"leaf_count": len(addresses), "normalized_mass_rational": "1",
            "full_tree_node_count": 2*len(addresses)-1,
            "maximum_depth": max(map(len, addresses))}


def validate_coverage(frontiers: Mapping[tuple[int, str], Sequence[str]]):
    """Check exactly all 18 (beta,chart) frontiers for one first flag."""
    for key in frontiers:
        if (not isinstance(key, tuple) or len(key) != 2
                or type(key[0]) is not int or not isinstance(key[1], str)):
            raise ValueError("invalid beta/chart association")
    required = {(case["beta"], case["chart"]) for case in case_list()}
    if set(frontiers) != required:
        raise ValueError("missing, duplicate-associated, or extra beta/chart cases")
    cases = []
    for beta, name in sorted(required):
        summary = validate_partition(frontiers[(beta, name)])
        cases.append({"beta": beta, "chart": name, **summary})
    return {"case_count": 18, "chart_count": 9, "cases": cases,
            "total_frontier_leaves": sum(row["leaf_count"] for row in cases)}
