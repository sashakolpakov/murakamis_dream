"""Validated first-type-three references over one external-coordinate box.

Import-safe. initialize() checks pinned inputs; evaluate() makes one
bounded floating proposal and validates it by original residuals only.
All conclusions are conditional on actual c in cbox intersect (K3 union K4).
"""
from collections import Counter
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

from flint import acb, arb, ctx


ROOT = Path(__file__).resolve().parents[1]
ALPHA = 0
PINNED = {
    'experiments/mixed_second_selected_external_reference.py': 'bf665fcaef589bb4370a172a3db6ea6e917a385cf6dd9daae84bc3d263b37dc4',
    'notes/research_mixed_second_selected_first_three_extension.md': 'd488ff98e01cfd5cd077de664c7e3bee3bfeeb735009f8c78f7c0ac60c7ad0e2',
    'notes/research_mixed_second_selected_first_three_external_reference_evaluation.md': '564710c4b10719fb0e81312e94289242cdc3857273d9d83b3dd1c965b490394f',
    'notes/research_mixed_prefix_residual_localization.md': '5590b49394d112be5f5d23e7f20c31225bce8f1c19e6d3fd1dc3aa1ce40f0434',
    'notes/research_mixed_open_word_hessian.md': '21556711a3ac410ce7d3e4dda0d3a6395cd7ee2a69993d82f5f8325c6e7dad23',
    'notes/research_mixed_open_word_endpoint_rectangles.md': 'ac5603badc00d42e98d17a1c5948cae011a6abd991d5249fa61d4224a829ad07',
    'notes/research_mixed_open_word_critical_localization.md': 'a3f8a0f781abd43f8ca17321171081ba37c91b284f83f22a4f7ae34e270424fa',
    'notes/research_mixed_cyclic_critical_localization.md': 'ccb8b144e6068c434059b707cd13d9aed8bb88a40e7fa0cf0e6bc655bff7fa71',
    'notes/research_mixed_stationary_reference_boundary_extension.md': '86ca000c2778c1908e4428224692f883742f432083728307bc9e6a415a45514f',
    'notes/research_mixed_second_selected_reference_curve.md': '4a591366418d251cbcfaad5705ff439747a8745cc8e75f64561e70aec3ef5bd5',
    'notes/research_mixed_second_selected_external_reference_evaluation.md': '0b2e5a3cece17d5db4a1d35536fef33ff5239a218cb88fffe8338148009b1f83',
}
NAMES = ("e", "xi", "a", "u", "z", "v", "b")
NEGATIVE_NAMES = ("e", "a", "u", "z", "v", "b", "c")
PRECISION = 256
COMMON = {
    "e": tuple(map(F, (".33", ".47", "-.09", ".08"))),
    "xi": tuple(map(F, (".21", ".25", ".01", ".10"))),
}
Q = tuple(map(F, (".23", ".45", "-.12", ".12")))
FORMS = {
    "e-xi": (F(0), (1, -1, 0, 0, 0, 0, 0, 0)),
    "e+a": (F(0), (1, 0, 1, 0, 0, 0, 0, 0)),
    "e": (F(0), (1, 0, 0, 0, 0, 0, 0, 0)),
    "half-xi": (F(1, 2), (0, -1, 0, 0, 0, 0, 0, 0)),
    "xi": (F(0), (0, 1, 0, 0, 0, 0, 0, 0)),
    "a+u": (F(0), (0, 0, 1, 1, 0, 0, 0, 0)),
    "a": (F(0), (0, 0, 1, 0, 0, 0, 0, 0)),
    "u+z": (F(0), (0, 0, 0, 1, 1, 0, 0, 0)),
    "u": (F(0), (0, 0, 0, 1, 0, 0, 0, 0)),
    "z+v": (F(0), (0, 0, 0, 0, 1, 1, 0, 0)),
    "z": (F(0), (0, 0, 0, 0, 1, 0, 0, 0)),
    "v+b": (F(0), (0, 0, 0, 0, 0, 1, 1, 0)),
    "v": (F(0), (0, 0, 0, 0, 0, 1, 0, 0)),
    "b+c": (F(0), (0, 0, 0, 0, 0, 0, 1, 1)),
    "b": (F(0), (0, 0, 0, 0, 0, 0, 1, 0)),
}
_STATE = None


class Inconclusive(Exception):
    pass


class Excluded(Exception):
    pass


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_hash(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def initialize():
    """Verify pinned files; return fixed proposal seeds without numerical work."""
    global _STATE
    bindings = dict(PINNED)
    for name, expected in bindings.items():
        if sha(ROOT/name) != expected:
            raise ValueError("first-type-three reference input mismatch: "+name)
    bindings[str(Path(__file__).resolve().relative_to(ROOT))] = sha(Path(__file__))
    common_seed = ((".407", ".009"), (".230", ".063"),
                   (".3345", "-.0255"), (".30", "-.052"), (".30", "-.052"))
    seeds = {}
    for beta in (0, 1):
        right = (".35", "-.01") if beta == 0 else (".30", "-.052")
        seeds[beta] = tuple(tuple(F(q) for q in row) for row in common_seed+(right, right))
    _STATE = {"bindings": dict(bindings), "seeds": seeds}
    return {"bindings": dict(bindings), "alpha": ALPHA,
            "seeds": {beta: [list(row) for row in seed] for beta, seed in seeds.items()},
            "seed_role": "fixed rational proposal only; not a certified canonical reference",
            "seed_canonical_certification_required": False,
            "precision_bits": PRECISION}


def gradient(values, outside, beta, xp, log, sin, cos, pi, ii):
    """The seven original, unscaled alpha-zero gradient rows."""
    e, xi, a, u, z, v, b = values
    half = xp(1)/2
    def j(w):
        return log(2*sin(pi*w))
    return [
        -j(e-xi)+j(e+a)+ii*pi*(xi-a),
        2*log(cos(pi*xi))+log(sin(pi*(e-xi)))-3*log(sin(pi*xi))+ii*pi*e,
        j(e+a)+j(a+u)-2*j(a)+ii*pi*(u-e),
        j(u+z)+j(a+u)-3*j(u)+ii*pi*(a-z+u-half),
        j(u+z)+j(z+v)-3*j(z)+ii*pi*(v-u+z-half),
        j(v+b)+j(z+v)-(2+beta)*j(v)+ii*pi*(z-b+beta*(v-half)),
        j(v+b)+j(b+outside)-(2+beta)*j(b)+ii*pi*(outside-v+beta*(b-half)),
    ]


def rat(q):
    q = F(q)
    return arb(q.numerator)/q.denominator


def finite(value, label):
    if not value.is_finite():
        raise Inconclusive("nonfinite "+label)
    return value


def ends(value):
    finite(value, "real interval")
    return F(str(value.lower().fmpq())), F(str(value.upper().fmpq()))


def real_record(value):
    lo, hi = ends(value)
    return {"finite": True, "lower_rational": str(lo), "upper_rational": str(hi)}


def complex_record(value):
    finite(value, "complex interval")
    return {"real": real_record(value.real), "imag": real_record(value.imag)}


def matrix_record(matrix):
    return [[complex_record(value) for value in row] for row in matrix]


def interval(lo, hi):
    lo, hi = F(lo), F(hi)
    if lo > hi:
        raise Excluded("empty necessary coordinate intersection")
    mid, radius = rat((lo+hi)/2), rat((hi-lo)/2)
    value = arb(mid, radius.upper())
    if ends(value)[0] > lo or ends(value)[1] < hi:
        raise Inconclusive("failed outward interval reconstruction")
    return value


def rectangle(box):
    return acb(interval(box[0], box[1]), interval(box[2], box[3]))


def cp(pair):
    return acb(rat(pair[0]), rat(pair[1]))


def pair_record(pair):
    return [str(q) for q in pair]


def sqrt_upper(q):
    q = F(q)
    if q < 0:
        raise ValueError("negative squared norm")
    return ends(rat(q).sqrt())[1] if q else F(0)


def squared_modulus_upper(z):
    x, y = ends(z.real), ends(z.imag)
    return max(abs(x[0]), abs(x[1]))**2+max(abs(y[0]), abs(y[1]))**2


def modulus_upper(z):
    return sqrt_upper(squared_modulus_upper(z))


def norm_upper(vector):
    square = sum((squared_modulus_upper(z) for z in vector), F(0))
    return sqrt_upper(square), square


def matvec(matrix, vector):
    return [sum((entry*x for entry, x in zip(row, vector)), acb(0)) for row in matrix]


def jacobian_from_k(k, beta, pi, ii):
    """Exact symmetric Jacobian of the original alpha=0 gradient."""
    H = [[0 for _ in NAMES] for _ in NAMES]
    H[0][0] = -k["e-xi"]+k["e+a"]
    H[1][1] = -2*k["half-xi"]-3*k["xi"]-k["e-xi"]
    H[2][2] = k["e+a"]+k["a+u"]-2*k["a"]
    H[3][3] = k["u+z"]+k["a+u"]-3*k["u"]+ii*pi
    H[4][4] = k["u+z"]+k["z+v"]-3*k["z"]+ii*pi
    H[5][5] = k["v+b"]+k["z+v"]-(2+beta)*k["v"]+ii*pi*beta
    H[6][6] = k["v+b"]+k["b+c"]-(2+beta)*k["b"]+ii*pi*beta
    for i, j, value in ((0, 1, k["e-xi"]+ii*pi), (0, 2, k["e+a"]-ii*pi),
                        (2, 3, k["a+u"]+ii*pi), (3, 4, k["u+z"]-ii*pi),
                        (4, 5, k["z+v"]+ii*pi), (5, 6, k["v+b"]-ii*pi)):
        H[i][j] = H[j][i] = value
    return H, [0, 0, 0, 0, 0, 0, k["b+c"]+ii*pi]


def terms(beta):
    return [((-1, "e-xi"), (1, "e+a")),
            ((2, "half-xi"), (-3, "xi"), (1, "e-xi")),
            ((1, "e+a"), (1, "a+u"), (-2, "a")),
            ((1, "u+z"), (1, "a+u"), (-3, "u")),
            ((1, "u+z"), (1, "z+v"), (-3, "z")),
            ((1, "v+b"), (1, "z+v"), (-(2+beta), "v")),
            ((1, "v+b"), (1, "b+c"), (-(2+beta), "b"))]


def propose(cmid, beta, seed, counts):
    import mpmath as mp
    counts["proposal_calls"] += 1
    with mp.workdps(50):
        def mr(q):
            return mp.mpf(q.numerator)/q.denominator
        def mc(pair):
            return mp.mpc(mr(pair[0]), mr(pair[1]))
        def forms(values, outside):
            values = list(values)+[outside]
            return {name: mr(constant)+sum(a*x for a, x in zip(row, values))
                    for name, (constant, row) in FORMS.items()}
        def matrix(values, outside):
            k = {name: mp.pi*mp.cot(mp.pi*w) for name, w in forms(values, outside).items()}
            H, s = jacobian_from_k(k, beta, mp.pi, mp.j)
            return mp.matrix(H), mp.matrix(s)
        q, outside = [mc(pair) for pair in seed], mc(cmid)
        stopped_small, last_residual = False, None
        for _ in range(20):
            residual = gradient(q, outside, beta, mp.mpf, mp.log, mp.sin, mp.cos, mp.pi, mp.j)
            counts["floating_gradient_evaluations"] += 1
            if not all(mp.isfinite(x) for x in residual):
                raise Inconclusive("nonfinite floating original-gradient proposal")
            last_residual = max(abs(x) for x in residual)
            if last_residual < mp.mpf("1e-42"):
                stopped_small = True
                break
            try:
                H, _ = matrix(q, outside)
                correction = mp.lu_solve(H, mp.matrix(residual))
            except ZeroDivisionError as error:
                raise Inconclusive("singular floating Newton proposal: "+str(error)) from error
            if not all(mp.isfinite(x) for x in correction):
                raise Inconclusive("nonfinite floating Newton correction")
            counts["newton_steps"] += 1
            q = [x-correction[j] for j, x in enumerate(q)]
        scale = 10**40
        def rounded(value):
            if not (mp.isfinite(value.real) and mp.isfinite(value.imag)):
                raise Inconclusive("nonfinite floating predictor component")
            return [F(int(mp.nint(value.real*scale)), scale), F(int(mp.nint(value.imag*scale)), scale)]
        q0 = [rounded(value) for value in q]
        try:
            H, s = matrix([mc(pair) for pair in q0], outside)
            approximate_inverse = H**-1
        except ZeroDivisionError as error:
            raise Inconclusive("singular floating predictor preconditioner: "+str(error)) from error
        counts["floating_preconditioner_inversions"] += 1
        response = -approximate_inverse*s
        P = [[rounded(approximate_inverse[i, j]) for j in range(7)] for i in range(7)]
        T = [rounded(response[i]) for i in range(7)]
        proposal = {"precision_decimal_digits": 50, "maximum_newton_steps": 20,
                    "rounding_decimal_places": 40, "stopped_below_proposal_tolerance": stopped_small,
                    "proposal_tolerance": "1e-42", "last_proposal_residual_max": mp.nstr(last_residual, 25),
                    "floating_convergence_used_as_certificate": False}
    return q0, T, P, proposal


class Encloser:
    def __init__(self, beta, details, counts):
        self.beta, self.details, self.counts = beta, details, counts
        self.pi, self.ii = arb.pi(), acb(0, 1)

    def common_domain(self, values, outside, label):
        records = {}
        for name, value in list(zip(NAMES, values))+[("c", outside)]:
            box = COMMON.get(name, Q)
            x, y = ends(value.real), ends(value.imag)
            passed = box[0] <= x[0] <= x[1] <= box[1] and box[2] <= y[0] <= y[1] <= box[3]
            records[name] = {"coordinate": complex_record(value), "necessary_bounds": list(map(str, box)), "contained": passed}
            if not passed:
                self.details.setdefault("common_domain_checks", {})[label] = records
                raise Inconclusive(label+" not contained in common product: "+name)
        self.details.setdefault("common_domain_checks", {})[label] = records

    def arguments(self, values, outside, label):
        full = list(values)+[outside]
        args, records = {}, {}
        for name, (constant, row) in FORMS.items():
            value = acb(rat(constant))+sum((a*x for a, x in zip(row, full)), acb(0))
            x = ends(value.real)
            passed = F(0) < x[0] <= x[1] < F(1)
            records[name] = {"argument": complex_record(value), "original_regular_strip": passed}
            if not passed:
                self.details.setdefault("branch_checks", {})[label] = records
                raise Inconclusive(label+" original strip failed: "+name)
            args[name] = value
        self.details.setdefault("branch_checks", {})[label] = records
        return args

    def sine(self, value, label):
        sine = finite((self.pi*value).sin(), label+" sine")
        x, y = ends(sine.real), ends(sine.imag)
        distance = max(F(0), x[0], -x[1], y[0], -y[1])
        self.details.setdefault("sine_denominator_checks", []).append({
            "label": label, "sine": complex_record(sine), "cartesian_distance_lower_rational": str(distance)})
        if distance <= 0:
            raise Inconclusive("sine rectangle does not exclude zero: "+label)
        return sine

    def jacobian(self, values, outside, label):
        self.counts["interval_jacobians"] += 1
        args = self.arguments(values, outside, label)
        k = {}
        for name, w in args.items():
            k[name] = finite(self.pi*(self.pi*w).cos()/self.sine(w, label+" "+name), "cotangent")
            self.counts["cotangent_enclosures"] += 1
        H, s = jacobian_from_k(k, self.beta, self.pi, self.ii)
        return [[acb(value) for value in row] for row in H], [acb(value) for value in s]

    def remainder(self, affine, outside, T):
        args = self.arguments(affine, outside, "full affine Taylor")
        derivative_bounds, directional_squares = {}, {}
        full_direction = T+[[F(1), F(0)]]
        witnesses = {}
        for name, w in args.items():
            third = finite(-self.pi*self.pi/self.sine(w, "Taylor "+name)**2, "third derivative")
            bound = modulus_upper(third)
            coefficients = FORMS[name][1]
            direction = [sum((a*pair[j] for a, pair in zip(coefficients, full_direction)), F(0)) for j in (0, 1)]
            square = direction[0]**2+direction[1]**2
            derivative_bounds[name], directional_squares[name] = bound, square
            witnesses[name] = {"third_derivative": complex_record(third), "absolute_upper_rational": str(bound),
                               "direction": pair_record(direction), "direction_squared_modulus_rational": str(square)}
            self.counts["third_derivative_enclosures"] += 1
        rho = [sum((abs(coefficient)*derivative_bounds[name]*directional_squares[name]
                    for coefficient, name in row), F(0)) for row in terms(self.beta)]
        square = sum((value*value for value in rho), F(0))
        self.details["Taylor_remainder"] = {"term_witnesses": witnesses,
            "gradient_terms": [[{"coefficient": a, "argument": name} for a, name in row] for row in terms(self.beta)],
            "rho_component_upper_rationals": list(map(str, rho)),
            "rho_squared_norm_upper_rational": str(square), "rho_norm_upper_rational": str(sqrt_upper(square))}
        return sqrt_upper(square)


def external_types(box, details):
    survivors, records = [], {}
    for kind, a, b, radius, floor, ceiling in (
            (3, F(7, 20), F(-1, 100), F(83, 1000), F(-9, 125), F(17, 250)),
            (4, F(3, 10), F(-13, 250), F(3, 50), F(-27, 250), F(-1, 1000))):
        dx, dy = max(F(0), box[0]-a, a-box[1]), max(F(0), box[2]-b, b-box[3])
        excess = dx*dx+dy*dy-radius*radius
        excluded = excess > 0 or box[3] < floor or box[2] > ceiling or (kind == 3 and box[0]-3*box[3] > F(76, 125))
        records[str(kind)] = {"squared_disk_distance_excess_rational": str(excess),
            "height_interval": [str(floor), str(ceiling)], "excluded": excluded}
        if not excluded:
            survivors.append(kind)
    details["external_typed_necessary_tests"] = records
    details["possible_external_types"] = survivors
    if not survivors:
        raise Excluded("external rectangle excludes both typed domains")
    return survivors


def clip_actual(raw, outside, beta, types, details):
    ordinary = (".267", ".433", "-.065", ".068") if beta == 0 else (".24", ".36", "-.102", "-.001")
    typed = {"e": (".376", ".438", "-.019", ".037"),
             "xi": (".218", ".242", ".049", ".077"),
             "a": (".278", ".391", "-.072", ".021"),
             "u": (".24", ".36", "-.102", "-.001"),
             "z": (".24", ".36", "-.102", "-.001"), "v": ordinary, "b": ordinary}
    external = {3: tuple(map(F, (".267", ".433", "-.072", ".068"))),
                4: tuple(map(F, (".24", ".36", "-.108", "-.001")))}
    typed["c"] = (min(external[t][0] for t in types), max(external[t][1] for t in types),
                  min(external[t][2] for t in types), max(external[t][3] for t in types))
    result, records = {}, {}
    details["actual_reference_intersections"] = records
    for name, value in list(zip(NAMES, raw))+[("c", outside)]:
        bounds, common = tuple(map(F, typed[name])), COMMON.get(name, Q)
        x, y = ends(value.real), ends(value.imag)
        clipped = (max(x[0], bounds[0], common[0]), min(x[1], bounds[1], common[1]),
                   max(y[0], bounds[2], common[2]), min(y[1], bounds[3], common[3]))
        records[name] = {"raw_coordinate": complex_record(value), "necessary_bounds": list(map(str, bounds)),
                         "common_bounds": list(map(str, common)), "intersection_endpoints": list(map(str, clipped))}
        if clipped[0] > clipped[1] or clipped[2] > clipped[3]:
            raise Excluded("localized canonical coordinate misses necessary rectangle: "+name)
        result[name] = rectangle(clipped)
        records[name]["outward_intersection"] = complex_record(result[name])
    return result


def evaluate(cbox, cmid, beta, seed_centers=None):
    """Return a pointwise canonical certificate on actual typed points of cbox."""
    if _STATE is None:
        initialize()
    if ctx.prec != PRECISION:
        raise ValueError("external-reference precision must be 256 bits")
    if beta not in (0, 1):
        raise ValueError("beta must be zero or one")
    box, midpoint = tuple(map(F, cbox)), tuple(map(F, cmid))
    if (len(box) != 4 or len(midpoint) != 2 or box[0] > box[1] or box[2] > box[3]
            or not (box[0] <= midpoint[0] <= box[1] and box[2] <= midpoint[1] <= box[3])):
        raise ValueError("prescribed exact expansion point is outside external box")
    seed = _STATE["seeds"][beta]
    if seed_centers is not None and tuple(tuple(F(q) for q in row) for row in seed_centers) != seed:
        raise ValueError("only the fixed rational proposal seed is permitted")
    counts = Counter()
    details = {"alpha": ALPHA, "beta": beta, "cbox": list(map(str, box)), "cmid": list(map(str, midpoint)),
               "seed_centers": [[str(q) for q in row] for row in seed],
               "seed_role": "fixed rational proposal only; not a certified canonical reference",
               "seed_canonical_certification_required": False,
               "seed_centers_sha256": canonical_hash([[str(q) for q in row] for row in seed]),
               "certificate_scope": "actual canonical references with c in cbox intersect (K3 union K4)",
               "precision_bits": PRECISION}
    output = {"status": "inconclusive", "alpha": ALPHA, "beta": beta,
              "coordinates": {}, "shapes": {}, "derivatives": {},
              "H": None, "inverse": None, "details": details, "witness": details, "counts": counts}
    try:
        if not (Q[0] <= box[0] <= box[1] <= Q[1] and Q[2] <= box[2] <= box[3] <= Q[3]):
            raise Inconclusive("full external rectangle overhangs common Q")
        types = external_types(box, details)
        q0, T, P, proposal = propose(midpoint, beta, seed, counts)
        details.update({"proposal": proposal, "q0": [pair_record(x) for x in q0],
                        "T": [pair_record(x) for x in T], "P": [[pair_record(x) for x in row] for row in P]})
        cert = Encloser(beta, details, counts)
        qpoint, cpoint, outside = list(map(cp, q0)), cp(midpoint), rectangle(box)
        delta = outside-cpoint
        affine = [x+cp(t)*delta for x, t in zip(qpoint, T)]
        details["raw_affine_coordinates"] = {name: complex_record(x) for name, x in zip(NAMES, affine)}
        cert.common_domain(affine, outside, "full affine predictor")
        cert.common_domain(qpoint, cpoint, "rational midpoint")
        H0, s0 = cert.jacobian(qpoint, cpoint, "rational midpoint")
        residual = gradient(qpoint, cpoint, beta, arb, lambda w: w.log(),
                                      lambda w: w.sin(), lambda w: w.cos(), cert.pi, cert.ii)
        counts["original_point_residual_evaluations"] += 1
        residual = [finite(x, "original midpoint gradient") for x in residual]
        tball = list(map(cp, T))
        linear = [x+y for x, y in zip(matvec(H0, tball), s0)]
        rnorm, rsquare = norm_upper(residual)
        lnorm, lsquare = norm_upper(linear)
        rho = cert.remainder(affine, outside, T)
        delta_square = max(abs(box[0]-midpoint[0]), abs(box[1]-midpoint[0]))**2
        delta_square += max(abs(box[2]-midpoint[1]), abs(box[3]-midpoint[1]))**2
        d = sqrt_upper(delta_square)
        mu = F(6, 49)*ends(cert.pi)[0]
        error = (rnorm+lnorm*d+rho*d*d/2)/mu
        details["residual_localization"] = {"r0": [complex_record(x) for x in residual],
            "H0": matrix_record(H0), "fc0": [complex_record(x) for x in s0],
            "linear_defect": [complex_record(x) for x in linear],
            "r0_squared_norm_upper_rational": str(rsquare), "r0_norm_upper_rational": str(rnorm),
            "linear_squared_norm_upper_rational": str(lsquare), "linear_norm_upper_rational": str(lnorm),
            "delta_squared_modulus_upper_rational": str(delta_square), "delta_modulus_upper_rational": str(d),
            "rho_norm_upper_rational": str(rho), "mu_lower_rational": str(mu),
            "coordinate_error_modulus_upper_rational": str(error),
            "no_clipped_value_used_in_Taylor_bound": True}
        raw = [acb(interval(ends(x.real)[0]-error, ends(x.real)[1]+error),
                   interval(ends(x.imag)[0]-error, ends(x.imag)[1]+error)) for x in affine]
        details["raw_localized_coordinates"] = {name: complex_record(x) for name, x in zip(NAMES, raw)}
        coordinates = clip_actual(raw, outside, beta, types, details)
        output["coordinates"] = coordinates
        details["actual_coordinate_enclosures"] = {name: complex_record(x) for name, x in coordinates.items()}
        qactual = [coordinates[name] for name in NAMES]
        # No domain-clipping operation is differentiated: H is evaluated
        # on a set known to contain the actual canonical point.
        H, s = cert.jacobian(qactual, coordinates["c"], "actual canonical enclosure")
        output["H"] = H
        pball = [[cp(value) for value in row] for row in P]
        E = [[acb(int(i == j))-sum((pball[i][k]*H[k][j] for k in range(7)), acb(0))
              for j in range(7)] for i in range(7)]
        eta = max(sum((modulus_upper(x) for x in row), F(0)) for row in E)
        pnorm = max(sum((modulus_upper(x) for x in row), F(0)) for row in pball)
        response = details["response_verification"] = {"H": matrix_record(H), "fc": [complex_record(x) for x in s],
            "P": matrix_record(pball), "I_minus_PH": matrix_record(E),
            "eta_upper_rational": str(eta), "P_norm_infinity_upper_rational": str(pnorm), "neumann_passed": eta < 1}
        counts["neumann_verifications"] += 1
        if eta >= 1:
            raise Inconclusive("Neumann row-sum bound is not below one")
        inverse_error = eta*pnorm/(1-eta)
        inverse = [[acb(interval(pair[0]-inverse_error, pair[0]+inverse_error),
                        interval(pair[1]-inverse_error, pair[1]+inverse_error)) for pair in row] for row in P]
        defect = [x+y for x, y in zip(matvec(H, tball), s)]
        preconditioned = matvec(pball, defect)
        defect_norm = max(modulus_upper(x) for x in preconditioned)
        derivative_error = defect_norm/(1-eta)
        derivatives = {name: acb(interval(t[0]-derivative_error, t[0]+derivative_error),
                                 interval(t[1]-derivative_error, t[1]+derivative_error)) for name, t in zip(NAMES, T)}
        response.update({"inverse_error_modulus_upper_rational": str(inverse_error), "inverse_enclosure": matrix_record(inverse),
            "HT_plus_fc": [complex_record(x) for x in defect],
            "preconditioned_response_residual": [complex_record(x) for x in preconditioned],
            "response_residual_norm_infinity_upper_rational": str(defect_norm),
            "derivative_error_modulus_upper_rational": str(derivative_error),
            "derivative_enclosures": {name: complex_record(x) for name, x in derivatives.items()}})
        shapes = {}
        for name in NEGATIVE_NAMES:
            shapes[name] = finite((-2*cert.pi*cert.ii*coordinates[name]).exp(), "negative reference shape "+name)
            counts["negative_shape_exponentials"] += 1
        details["negative_shapes"] = {name: complex_record(x) for name, x in shapes.items()}
        output.update({"status": "enclosed", "reason": "original residual and implicit response certified",
                       "shapes": shapes, "derivatives": derivatives, "inverse": inverse})
    except Excluded as error:
        output.update({"status": "excluded", "reason": str(error)})
    except Inconclusive as error:
        output.update({"status": "inconclusive", "reason": str(error)})
    except Exception as error:
        output.update({"status": "error", "reason": type(error).__name__+": "+str(error),
                       "unexpected_error": repr(error)})
    output["counts"] = dict(counts)
    limits = {"proposal_calls": 1, "newton_steps": 20, "floating_gradient_evaluations": 20,
              "floating_preconditioner_inversions": 1, "original_point_residual_evaluations": 1,
              "interval_jacobians": 2, "cotangent_enclosures": 30,
              "third_derivative_enclosures": 15, "neumann_verifications": 1,
              "negative_shape_exponentials": 7}
    if any(counts[name] > limit for name, limit in limits.items()):
        output.update({"status": "error", "reason": "bounded provider operation cap exceeded",
                       "unexpected_error": "bounded provider operation cap exceeded"})
    details["operation_limits"] = limits
    details["counts"] = dict(counts)
    details["status"], details["reason"] = output["status"], output["reason"]
    if "unexpected_error" in output:
        details["unexpected_error"] = output["unexpected_error"]
    details.update({"alternative_seed_or_midpoint_calls": 0, "proposal_retries": 0,
                    "finite_source_evaluations": 0, "scalar_budget_evaluations": 0,
                    "suffix_realization_claimed": False, "nonempty_parameter_intersection_claimed": False})
    return output
