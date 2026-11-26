#!/usr/bin/env python3
"""Full parameter enclosures for an immediate raw right half.

Real row roots are enclosed by their original derivative and its proved
strict negative slope. Complex critical-root solves are not used.
"""
import argparse
from fractions import Fraction as F
import hashlib
import itertools
import json
from pathlib import Path
import time

from flint import acb, arb, ctx

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT/'notes/research_mixed_immediate_right_half.md'
BANDS = {
    (1, 0, 0): ('-.017', '.010'), (1, 0, 1): ('-.025', '-.002'),
    (1, 1, 0): ('-.054', '-.030'), (1, 1, 1): ('-.056', '-.048'),
    (0, 0, 0): ('-.017', '.010'), (0, 0, 1): ('-.025', '.002'),
    (0, 1, 0): ('-.056', '-.030'), (0, 1, 1): ('-.056', '-.036'),
}
CASES = [(d, a, b, 0, F(lo), F(hi))
         for (d, a, b), (lo, hi) in BANDS.items()]
CASES += [(d, 1, b, 1, F(0), F(0))
          for d, b in itertools.product((0, 1), repeat=2)]


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def ar(value):
    value = F(value)
    return arb(value.numerator)/value.denominator


def gp(z):
    return (1-(-2*arb.pi()*acb(0, 1)*z).exp()).log()


def gpp(z):
    return arb.pi()*(arb.pi()*z).cot()-arb.pi()*acb(0, 1)


def target(parameters, selected):
    t, c = parameters
    rho = (t-ar('.1'))/ar('.12')
    ii = acb(0, 1)
    if selected:
        return acb(t, ar('.014')), [acb(1), acb(0)]
    return acb(t, c*rho), [1+ii*c/ar('.12'), ii*rho]


def row_derivative(u, z, epsilon, d):
    return (gp(acb(u+ar('.5')))+gp(z+u)
            -(2+epsilon)*gp(acb(u))
            +2*arb.pi()*acb(0, 1)*(d*z+ar(F(1-d, 2)))).real


def row_enclosure(parameters, middle, selected, epsilon, d):
    zm, _ = target(middle, selected)
    lo, hi = F(1, 5), F(2, 5)
    for _ in range(30):
        trial = (lo+hi)/2
        value = row_derivative(ar(trial), zm, epsilon, d)
        if value > 0:
            lo = trial
        elif value < 0:
            hi = trial
        else:
            break
    u0 = ar((lo+hi)/2)
    z, _ = target(parameters, selected)
    radius = (abs(row_derivative(u0, z, epsilon, d))/(2*arb.pi())).upper()
    return (u0+arb(0, radius)).intersection(ar(F(1, 5)).union(ar(F(2, 5))))


def values(box, d, alpha, beta, selected):
    pars = [ar(lo).union(ar(hi)) for lo, hi in box]
    middle = [ar((lo+hi)/2) for lo, hi in box]
    epsilon = beta if d else alpha
    row = row_enclosure(pars, middle, selected, epsilon, d)
    rowmid = row_enclosure(middle, middle, selected, epsilon, d)
    ii, pi = acb(0, 1), arb.pi()

    def at(parameters, u, chi, q):
        z, zp = target(parameters, selected)
        c = parameters[1]
        v = acb(1) if selected else 1+ii*chi*c/ar('.12')
        vp = [acb(0), acb(0) if selected else ii*chi/ar('.12')]
        coefficient = ar(1+F(alpha, 2)-F(q, 2))
        K = gp(z+u)-coefficient*gp(z)+2*pi*ii*d*u+pi*ii*(selected-q)
        gauged = K+ii*ar(F(3, 2)*(1-2*d))
        val = (v*gauged).real+ar(F(selected*(1-2*d), 10))
        Kz = gpp(z+u)-coefficient*gpp(z)
        Ku = gpp(z+u)+2*pi*ii*d
        T_u = (gpp(acb(u+ar('.5')))+gpp(z+u)
               -(2+epsilon)*gpp(acb(u))).real
        # Intersect with the separately proved whole-domain bound T_u<=-2pi.
        if not T_u.is_finite():
            return None, None
        T_u = T_u.intersection(T_u.lower().union((-2*pi).upper()))
        assert T_u < 0
        up = [-(Ku*zz).real/T_u for zz in zp]
        grad = [(vv*gauged+v*(Kz*zz+Ku*uu)).real
                for vv, zz, uu in zip(vp, zp, up)]
        return val, grad

    lowers, gradients = [], []
    for chi in ((0,) if selected else (0, 1)):
        for q in ((0, 1) if selected else (0,)):
            direct, grad = at(pars, row, chi, q)
            center, _ = at(middle, rowmid, chi, q)
            if direct is None or center is None or not all(
                    x.is_finite() for x in [direct, center, *grad]):
                return None, None
            mean = center-sum((abs(g)*ar((hi-lo)/2)
                               for g, (lo, hi) in zip(grad, box)), arb(0))
            lowers.append(max(direct.lower(), mean.lower()))
            gradients.append(grad)
    return min(lowers), gradients


def frozen_height_checks():
    pi = arb.pi()
    scalar = {}

    def positive(name, value):
        assert value > 0, (name, str(value))
        scalar[name] = str(value)

    for fraction in (F(6, 25), F(11, 25)):
        angle = pi*ar(fraction)
        positive('sine plus cosine at '+str(fraction),
                 angle.sin()+angle.cos()-ar(F(23, 20)))
    positive('small-height cosh ceiling', ar(F(101, 100))-(pi*ar(F(7, 250))).cosh())
    positive('radius lower bound', (-pi*ar(F(19, 1000))).exp()-ar(F(47, 50)))
    positive('radius upper bound', ar(F(11, 10))-(pi*ar(F(7, 250))).exp())
    c0, c1 = (pi*ar(F(11, 25))).cos(), (pi*ar(F(31, 25))).cos()
    positive('first cosine lower', c0-ar('.18'))
    positive('first cosine upper', ar('.19')-c0)
    positive('second cosine lower', c1-ar('-.74'))
    positive('second cosine upper', ar('-.72')-c1)
    numerator = F('.93')*(1-F('.94')**2)-F(1, 2)*(F('.94')-F('.19'))*(
        1+F('.94')**2+2*F('.94')*F('.72'))
    assert numerator < 0
    for name, coefficient, height, gauge, lower in (
        ('type three endpoint', F(1), F('-.005'), F(0), F('.37')),
        ('unselected four endpoint', F(3, 2), F(0), F(0), F('.25')),
        ('selected four endpoint including real gauge', F(3, 2), F('.014'), F('-.1'), F('.13')),
    ):
        value = gp(acb(ar('.62'), ar(height))).real \
            -ar(coefficient)*gp(acb(ar('.22'), ar(height))).real+ar(gauge)
        positive(name, value-ar(lower))
    return dict(scalar_reserves=scalar, rational_height_derivative_upper=str(numerator),
                derivative_lower_bound='13/100', new_parameter_cells=0)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--precision', type=int, default=256)
    ap.add_argument('--input', type=Path)
    ap.add_argument('--output', type=Path, default=ROOT/
                    'repro/results/research-mixed-immediate-right-half.json')
    ap.add_argument('--max-visits', type=int, default=8191)
    ap.add_argument('--seconds', type=float, default=45)
    args = ap.parse_args()
    assert args.precision >= 160
    ctx.prec = args.precision
    ph, sh = sha(PROOF), sha(__file__)
    deps, primaries = {}, {}

    def bind(path, digest=None):
        actual = sha(ROOT/path)
        if digest is not None:
            assert actual == digest, path
        if path in deps:
            assert deps[path] == actual, path
        deps[path] = actual

    for stem, prefix in [
        ('mixed_neighbor_conditioned_critical_boxes', 'certify'),
        ('mixed_four_before_four_height_lower', 'certify'),
        ('mixed_right_boundary_row_bracket', 'check'),
        ('mixed_algebraic_right_row', 'check'),
    ]:
        path = 'repro/results/research-'+stem.replace('_', '-')+'.json'
        bind(path)
        data = json.loads((ROOT/path).read_text())
        assert data['status'] == 'passed'
        bind('notes/research_'+stem+'.md', data['proof_sha256'])
        bind('experiments/'+prefix+'_'+stem+'.py', data['script_sha256'])
        for field in ('dependencies_sha256', 'dependencies'):
            for name, digest in data.get(field, {}).items():
                bind(name, digest)
        primaries[stem] = data
    height = primaries['mixed_four_before_four_height_lower']
    assert height['lower_height'] == '-7/125' and height['upper_height'] == '-6/125'
    bracket = primaries['mixed_right_boundary_row_bracket']
    assert bracket['row_interval'] == ['1/5', '2/5']
    assert bracket['neighboring_real_interval'] == ['1/10', '1/2']
    assert bracket['maximum_absolute_height'] == '57/1000'
    bind('notes/research_mixed_minimum_level_half_stencils.md')
    bind('notes/research_mixed_constant_selected_height_transport.md')
    bind('notes/research_mixed_frozen_outer_half_stencils.md')
    table = primaries['mixed_neighbor_conditioned_critical_boxes']['limits_in_thousandths']
    for (d, alpha, beta), strings in BANDS.items():
        intervals = []
        for outer in (0, 1):
            types = (outer, alpha, beta) if d else (beta, alpha, outer)
            interval = [F(x, 1000) for x in table[''.join(map(str, types))][1]]
            original = (F('-.057'), F('-.02')) if alpha else (F('-.03'), F('.02'))
            interval = [max(interval[0], original[0]), min(interval[1], original[1])]
            if types[1:] == (1, 1):
                interval = [max(interval[0], F('-.056')), min(interval[1], F('-.048'))]
            assert interval[0] < interval[1]
            intervals.append(interval)
        hull = (min(p[0] for p in intervals), max(p[1] for p in intervals))
        assert hull == tuple(map(F, strings)), (d, alpha, beta, hull)
    old, ih = None, None
    if args.input:
        ih = sha(args.input)
        old = json.loads(args.input.read_text())
        assert old['status'] == 'passed'
        assert old['proof_sha256'] == ph and old['script_sha256'] == sh
        assert old['dependencies_sha256'] == deps
        assert len(old['cases']) == len(CASES)
    frozen = frozen_height_checks()
    start = time.monotonic()
    records, status = [], 'passed'
    for index, (d, alpha, beta, selected, clo, chi) in enumerate(CASES):
        stack = [[(F('.12'), F('.22')), (clo, chi)]]
        saved = None if old is None else old['cases'][index]
        identity = [d, alpha, beta, selected]
        if saved is not None:
            assert saved['case'] == identity
            assert saved['coefficient_interval'] == [str(clo), str(chi)]
        nodes, minimum = [], None
        leaves = visits = cursor = 0
        while stack:
            if old is None and (visits >= args.max_visits or time.monotonic()-start > args.seconds):
                status = 'incomplete'
                break
            box = stack.pop()
            visits += 1
            node = None if saved is None else saved['nodes'][cursor]
            cursor += saved is not None
            if node is not None and node[0] == 'S':
                axis = node[1]
                assert axis in (0, 1)
            else:
                assert node is None or node == ['L']
                lower, gradients = values(box, d, alpha, beta, selected)
                if lower is not None and lower > ar(F(1, 2000)):
                    leaves += 1
                    minimum = lower if minimum is None else min(minimum, lower)
                    nodes.append(['L'])
                    continue
                assert saved is None, ('saved leaf failed', index, cursor, str(lower))
                if gradients is None:
                    axis = max((hi-lo, j) for j, (lo, hi) in enumerate(box))[1]
                else:
                    axis = max((max((abs(g[j])*ar(hi-lo)).upper() for g in gradients), j)
                               for j, (lo, hi) in enumerate(box))[1]
            lo, hi = box[axis]
            assert hi-lo > F(1, 2**26)
            mid = (lo+hi)/2
            nodes.append(['S', axis])
            for pair in ((lo, mid), (mid, hi)):
                child = list(box)
                child[axis] = pair
                stack.append(child)
        if saved is not None:
            assert not stack and cursor == len(saved['nodes'])
            assert leaves == saved['accepted_cells'] and visits == saved['visited_cells']
        records.append(dict(case=identity, coefficient_interval=[str(clo), str(chi)],
                            accepted_cells=leaves, visited_cells=visits,
                            remaining_boxes=len(stack), minimum_lower_bound=str(minimum), nodes=nodes))
        print(identity, leaves, visits, minimum, flush=True)
        if status != 'passed':
            break
    assert ph == sha(PROOF) and sh == sha(__file__)
    assert all(sha(ROOT/path) == digest for path, digest in deps.items())
    if args.input:
        assert ih == sha(args.input)
    data = dict(status=status, precision_bits=args.precision, cases=records,
                derivative_lower_bound='1/2000', geometric_interval_count=len(BANDS),
                frozen_height_corollary=frozen,
                elapsed_seconds=time.monotonic()-start, complex_critical_root_solves=0,
                proof_sha256=ph, script_sha256=sh, dependencies_sha256=deps,
                scope='Immediate right-neighbor half derivative with original kappa=3/2 and selected real gauge 1/10. Actual conditioned reference heights, all local types and Fourier choices. No distance-two or upper-taper opposite-half claim; no full-period or knot consequence.')
    if ih:
        data['input_sha256'] = ih
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, indent=2)+'\n')
    print(status.upper(), len(records), 'cases', flush=True)


if __name__ == '__main__':
    main()
