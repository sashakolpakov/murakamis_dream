#!/usr/bin/env python3
"""Independent saved-witness replay of the full plateau alias clamp.

No author module or floating root solver is used. Original sine logarithms
validate the rational affine Newton witnesses; real-form cotangent Hessians and
scalar log-modulus marginal formulas test the claimed inequalities.
"""
import argparse
import hashlib
import itertools
import json
import time
from fractions import Fraction as Q
from pathlib import Path
from flint import arb, acb, ctx

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / 'notes/research_mixed_plateau_alias_clamping.md'
AUTHOR = ROOT / 'experiments/certify_mixed_plateau_alias_clamping.py'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def exact_cover(addresses):
    words = sorted(addresses)
    assert len(words) == len(set(words))
    assert all(set(w) <= {'0', '1'} for w in words)
    assert all(not b.startswith(a) for a, b in zip(words, words[1:]))
    assert sum((Q(1, 2**len(w)) for w in words), Q(0)) == 1


def cells(address, dimensions):
    assert dimensions > 0
    intervals = [[Q(0), Q(1)] for _ in range(dimensions)]
    for depth, bit in enumerate(address):
        axis = depth % dimensions
        left, right = intervals[axis]
        intervals[axis][1 - int(bit)] = (left + right) / 2
    return intervals


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--precision', type=int, default=320)
    parser.add_argument('--input', type=Path, default=ROOT / 'repro/results/research-mixed-plateau-alias-clamping.json')
    parser.add_argument('--output', type=Path, default=ROOT / 'repro/results/research-mixed-plateau-alias-clamping-replay.json')
    args = parser.parse_args()
    assert args.precision >= 256
    ctx.prec = args.precision
    pi, ii = arb.pi(), acb(0, 1)
    start = time.time()
    input_hash, script_hash, proof_hash = sha(args.input), sha(__file__), sha(PROOF)
    data = json.loads(args.input.read_text())
    assert data['status'] == 'passed'
    assert data['proof_sha256'] == proof_hash
    assert data['script_sha256'] == sha(AUTHOR)
    for path, digest in data['dependencies'].items():
        assert sha(ROOT / path) == digest, path

    def ar(value):
        value = Q(value)
        return arb(value.numerator) / value.denominator

    def point(pair):
        return acb(ar(pair[0]), ar(pair[1]))

    def interval(bounds, middle=False):
        a, b = bounds
        return ar((a + b)/2) if middle else ar(a).union(ar(b))

    def sine_log(z):
        assert 0 < z.real < 1
        return (2 * (pi*z).sin()).log()

    def gp(z):
        return sine_log(z) + ii*pi*(ar('1/2') - z)

    def real_gp(z):
        # Squared modulus of 1-exp(-2*pi*i*z), retaining its radial factor.
        radius = (2*pi*z.imag).exp()
        return (1+radius*radius-2*radius*(2*pi*z.real).cos()).log()/2

    def gpp(z):
        # Real-coordinate form, independently evaluated from sine/cosh.
        x, y = 2*pi*z.real, 2*pi*z.imag
        denominator = y.cosh()-x.cos()
        return pi*acb(x.sin()/denominator, -y.sinh()/denominator)-pi*ii

    def original_equation(s, a, b, epsilon):
        return (sine_log(s+a) + sine_log(s+b) - (2+epsilon)*sine_log(s)
                + ii*pi*(a-b+epsilon*(s-ar('1/2'))))

    def derivative(s, a, b, epsilon):
        return gpp(s+a) + gpp(s+b) - (2+epsilon)*gpp(s)

    max_newton = arb(0)
    min_cross = None
    marginal_checks = 0

    def validate(witness, epsilon, parameters, middle):
        nonlocal max_newton
        a, b = parameters
        a0, b0 = middle
        center = point(witness['center'])
        D = list(map(point, witness['affine_derivatives']))
        assert len(D) == 2
        radius = ar(witness['remainder_radius'])
        assert 0 < radius <= ar('1/25')
        dp = [a-a0, b-b0]
        dz = D[0]*dp[0] + D[1]*dp[1]
        h0 = derivative(center, a0, b0, epsilon)
        inverse = 1/h0
        f0 = original_equation(center, a0, b0, epsilon)
        external = [gpp(center+a0)+2*pi*ii, gpp(center+b0)]
        linear = f0 + sum(((h0*D[j]+external[j])*dp[j] for j in (0, 1)), acb(0))

        def taylor_remainder(base, delta):
            # Integral Taylor remainder for log(2 sin(pi*z)).
            path = base + acb(arb(0, abs(delta.real).upper()), arb(0, abs(delta.imag).upper()))
            assert 0 < path.real < 1
            return pi*pi*abs(1/(pi*path).sin()**2)*abs(delta)**2/2

        error = abs(inverse)*(abs(linear)
                + taylor_remainder(center+a0, dz+dp[0])
                + taylor_remainder(center+b0, dz+dp[1])
                + (2+epsilon)*taylor_remainder(center, dz))
        delta = dz + acb(arb(0, radius), arb(0, radius))
        root = center + delta
        assert ar('1/5') < root.real < ar('23/50')
        assert abs(root.imag) < ar('17/100')

        def cotangent_increment(base, displacement):
            return -pi*(pi*displacement).sin()/((pi*base).sin()*(pi*(base+displacement)).sin())

        variation = (cotangent_increment(center+a0, delta+dp[0])
                     + cotangent_increment(center+b0, delta+dp[1])
                     - (2+epsilon)*cotangent_increment(center, delta))
        newton_derivative = 1-inverse*h0-inverse*variation
        norm = (error/radius + abs(newton_derivative)).upper()
        assert norm < 1, ('affine Newton', witness['address'], str(norm))
        max_newton = max(max_newton, norm)
        return root

    rectangles = {
        '3': list(map(Q, ['.22', '.45', '-.03', '.02'])),
        '4': list(map(Q, ['.22', '.45', '-.057', '.0141']))}

    def cross_parameters(case, address, middle=False):
        result = []
        for kind, side, bounds in zip(case['kinds'], case['parts'], cells(address, 2)):
            xl, xr, yl, yr = rectangles[kind]
            corners = [acb(ar(xl), ar(yl)), acb(ar(xr), ar(yl)),
                       acb(ar(xr), ar(yr)), acb(ar(xl), ar(yr))]
            result.append(corners[side] + (corners[(side+1) % 4]-corners[side])*interval(bounds, middle))
        return result

    expected_cross = {(e, a, b, i, j)
                      for e, a, b in [(0, '3', '3'), (0, '4', '3'), (1, '3', '4'), (1, '4', '4')]
                      for i, j in itertools.product(range(4), repeat=2)}
    assert len(data['cross_cases']) == 64
    assert {(c['eps'], *c['kinds'], *c['parts']) for c in data['cross_cases']} == expected_cross
    cross_results = []
    cross_count = 0
    for case in data['cross_cases']:
        exact_cover(case['addresses'])
        assert sorted(case['addresses']) == sorted(w['address'] for w in case['witnesses'])
        for w in case['witnesses']:
            parameters = cross_parameters(case, w['address'])
            middle = cross_parameters(case, w['address'], True)
            a, b = parameters
            s = validate(w, case['eps'], parameters, middle)
            mixed = (-(gpp(s+a)+2*pi*ii)*gpp(s+b)/derivative(s, a, b, case['eps'])).real
            assert mixed > ar('1/100'), ('mixed Hessian', case['kinds'], case['parts'], w['address'], str(mixed))
            low = mixed.lower()
            min_cross = low if min_cross is None else min(min_cross, low)
            cross_count += 1
        row = {'epsilon': case['eps'], 'kinds': case['kinds'], 'parts': case['parts'], 'cells': len(case['addresses'])}
        cross_results.append(row)
        print('cross', json.dumps(row), flush=True)

    # Reconstruct every marginal domain and its rational target independently.
    heights = {0: [Q('-.03'), Q('.02')], 1: [Q('-.057'), Q('.014')]}
    configurations = [('lower', 0, heights[0], 0), ('lower', 1, [Q('.014')]*2, 1)]
    configurations += [('lower', 1, [Q('-.057')+j*Q('.037')/4, Q('-.057')+(j+1)*Q('.037')/4], 2+j) for j in range(4)]
    configurations += [('upper4', 1, [Q('-.057'), Q('-.02')], 0), ('upper4', 1, [Q('.014')]*2, 1)]
    configurations += [('upper3', 0, [Q('-.03')+j*Q('.05')/8, Q('-.03')+(j+1)*Q('.05')/8], j) for j in range(8)]
    rational_bounds = [
        ['6483/50000', '1061/10000'], ['-30471/100000', '28503/100000'],
        ['-4487/50000', '11809/100000'], ['-577/5000', '14717/100000'],
        ['-1437/10000', '869/5000'], ['-17473/100000', '19797/100000'],
        ['-1547/2500', '551/3125'], ['-90013/100000', '9431/50000'],
        ['-5653/50000', '10277/100000'], ['-12151/100000', '5371/50000'],
        ['-6517/50000', '11177/100000'], ['-2791/20000', '579/5000'],
        ['-2983/20000', '747/6250'], ['-7957/50000', '6147/50000'],
        ['-16953/100000', '12607/100000'], ['-1127/6250', '1289/10000']]
    expected_faces = []
    for group_index, (mode, own, own_height, group) in enumerate(configurations):
        rho = [Q('.22'), Q('.25')] if mode == 'lower' else [Q('.4'), Q('.45')] if mode == 'upper3' else [Q('.4')]*2
        for side, neighbor in itertools.product((0, 1), repeat=2):
            expected_faces.append({'mode': mode, 'type': own, 'neighbor': neighbor,
                                   'side': side, 'group': group,
                                   'box': [rho, own_height, heights[neighbor]],
                                   'bound': Q(rational_bounds[group_index][side])})
    assert len(expected_faces) == len(data['face_cases']) == 64

    def face_parameters(spec, address, middle=False):
        active = [i for i, (a, b) in enumerate(spec['box']) if a < b]
        fractions = cells(address, len(active))
        vals = [ar(bounds[0]) for bounds in spec['box']]
        for axis, bounds in zip(active, fractions):
            left, right = spec['box'][axis]
            vals[axis] = ar(left) + ar(right-left)*interval(bounds, middle)
        rho, own_height, neighbor_height = vals
        if spec['mode'] == 'lower' or (spec['mode'] == 'upper3' and spec['neighbor'] == 0):
            neighbor_real = rho
        else:
            neighbor_real = ar('.4') if spec['mode'] == 'upper3' else ar('.45')
        target, neighbor = acb(rho, own_height), acb(neighbor_real, neighbor_height)
        return [neighbor, target] if spec['side'] == 0 else [target, neighbor]

    face_results = []
    face_count = 0
    for index, (spec, case) in enumerate(zip(expected_faces, data['face_cases'])):
        for key in ['mode', 'type', 'neighbor', 'side', 'group']:
            assert spec[key] == case[key], (index, key)
        assert spec['box'] == [list(map(Q, v)) for v in case['box']]
        assert spec['bound'] == Q(case['bound'])
        active = [i for i, (a, b) in enumerate(spec['box']) if a < b]
        assert active == case['active_parameters']
        exact_cover(case['addresses'])
        assert sorted(case['addresses']) == sorted(w['address'] for w in case['witnesses'])
        epsilon = spec['type'] if spec['side'] == 0 else spec['neighbor']
        for w in case['witnesses']:
            parameters = face_parameters(spec, w['address'])
            middle = face_parameters(spec, w['address'], True)
            a, b = parameters
            s = validate(w, epsilon, parameters, middle)
            if spec['side'] == 0:
                own = spec['type']
                marginal = real_gp(s+b)-(1+own)*real_gp(b)
            else:
                marginal = real_gp(s+a)-real_gp(a)-2*pi*s.imag
            assert (marginal > ar(spec['bound']) if spec['mode'] == 'lower' else marginal < ar(spec['bound'])), ('marginal', index, w['address'], str(marginal), str(spec['bound']))
            marginal_checks += 1
            face_count += 1
        row = {'index': index, 'mode': spec['mode'], 'side': spec['side'], 'neighbor': spec['neighbor'], 'cells': len(case['addresses'])}
        face_results.append(row)
        print('face', json.dumps(row), flush=True)

    group_checks = []
    for j, (mode, own, own_height, group) in enumerate(configurations):
        bound = sum(map(Q, rational_bounds[j]))
        if mode == 'lower':
            assert bound > (Q(-1, 50) if own == 1 and group == 1 else 0)
        elif mode == 'upper4' and group == 1:
            assert ar(bound) + gp(acb(ar('.4'), ar('.014'))).real < 0
        else:
            assert bound < 0
        group_checks.append({'mode': mode, 'type': own, 'group': group, 'sum': str(bound)})
    assert 2*(ar('.44')*pi).cos() < 1
    assert Q(721, 10000)-Q(25, 2)*Q(71, 1000)**2 == Q(727, 80000)
    assert Q(727, 80000)-Q(3, 5000)-Q(1, 1000)-Q(1, 150) == Q(197, 240000)
    assert cross_count == data['cross_cells'] == 4459
    assert face_count == data['face_cells'] == 54162
    assert sha(args.input) == input_hash and sha(PROOF) == proof_hash and sha(__file__) == script_hash
    assert sha(AUTHOR) == data['script_sha256']
    for path, digest in data['dependencies'].items():
        assert sha(ROOT/path) == digest, path
    output = {'status': 'passed', 'precision_bits': args.precision,
              'cross_products': 64, 'cross_cells': cross_count, 'face_domains': 64,
              'face_cells': face_count, 'refinements': 0, 'affine_witnesses': cross_count+face_count,
              'max_normalized_newton_bound': str(max_newton), 'min_mixed_hessian': str(min_cross),
              'marginal_checks': marginal_checks, 'exact_rational_group_checks': 16,
              'strict_scalar_comparisons': 2, 'exact_budget_identities': 2,
              'cross_cases': cross_results, 'face_cases': face_results, 'gradient_groups': group_checks,
              'scope': data['scope'], 'input_sha256': input_hash, 'author_script_sha256': sha(AUTHOR),
              'script_sha256': script_hash, 'proof_sha256': proof_hash, 'dependencies': data['dependencies'],
              'elapsed_seconds': time.time()-start,
              'independent_method': 'Exact dyadic partition reconstruction and original sine-log affine Newton witnesses; real-coordinate cotangent Hessians and real log-modulus marginals. No author imports, polynomial roots, or numerical optimizers.'}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2)+'\n')
    print('PASS independent plateau aliases', cross_count, face_count, flush=True)


if __name__ == '__main__':
    main()
