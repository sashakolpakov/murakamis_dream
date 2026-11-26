#!/usr/bin/env python3
"""Fixed two-selected ordinary-lift budgets; no roots, grids or retries.

Consumes a reviewed saved-only projection.  Fixed maxima: 128 cotangents,
one pi/exp, two cosines, three logs, 96 vertices and 192 signed gains.
Pending literal pins deliberately prevent all analytic imports.
"""
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import io
import itertools
import json
from math import isqrt
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
PROOF = 'notes/research_mixed_terminal_two_selected_lift_budget_protocol.md'
SOURCE = 'repro/results/research-mixed-terminal-two-selected-reference-projection.json'
PROJECTOR = 'experiments/extract_mixed_terminal_two_selected_references.py'
SOURCE_PROOF = 'notes/research_mixed_terminal_two_selected_reference_bank_transfer.md'
TERMINAL_AUDIT = 'repro/results/research-mixed-terminal-real-transform-cut-saved-audit.json'
TERMINAL_CHECKER = 'experiments/check_mixed_terminal_real_transform_cut_record.py'
PINNED = {
    PROOF: 'ed08fa18c69c0265a3509e7730b068dc57cad6495b64802841d53a551677b322',
    SOURCE: '98a1e6d33c58074fffface6b3da93cbd4d842f5006a2d2f032c94a73ee81c198',
    PROJECTOR: '32121f3a82827de99c6e762fd821b9343d1fab6d751fc4eeffe45500bb1cde2d',
    SOURCE_PROOF: 'eaf351d6f4bab35fbdec81b6642ba72b5777b582caafced26788d31908bf1223',
    TERMINAL_AUDIT: '29d1edc0a516e44ceac16f3c9fe9868bfee0e8c3268134819f05bbd21067306e',
    TERMINAL_CHECKER: '116f9b00d0580e96273c58a4079623796591d80afdb99d25cbd8b1c1a3c231f7',
    'notes/research_mixed_terminal_two_selected_window.md':
        'bdc5390f4a3a05c517ce1254b54154bc3f1b5bbc5307a7301c9ffc20d4e58e07',
    'notes/research_mixed_terminal_two_selected_budget_composition.md':
        '002cf3eb25520f24745a36ce52ead2105793a6c814796752b6d4fb9a3177a4c8',
    'notes/research_mixed_terminal_shared_index_gain_cancellation.md':
        '8313c7dcca46ec7c95c8ed5e7f34e5eb59400615d8633a197e5429e2dbb68218',
    'notes/research_signed_cubic_gain_with_uncertain_center.md':
        '1a890d4c06ff37a397e3e7732f2d6f5b952f9ffa74858f31a5c837ad871bae6c',
    'notes/research_mixed_terminal_two_selected_reference_reconstruction.md':
        '2d81e3ee8e09c1cddf83a0b0579252d67f2b9a2ffd04f2e6b821dcf2b9d96f5a',
    'notes/research_mixed_terminal_symmetric_pair_costs.md':
        'b4ee1a7bdde317edab0210b20cb8616913984c4f992d1cbed240f6092a8e593f',
    'notes/research_mixed_terminal_cubic_cost_and_response_bounds.md':
        'dfc3f415e742aa9c632707aea7c699bb2ccbdc054c08fc7ba640e943bcdaa741',
    'notes/research_mixed_selected_weight_branch_domains.md':
        '081aa8c7491f0c2aebfe0cb9431ff2b304f592b52b07fa2d0544cd8175981b3d',
    'notes/research_mixed_terminal_uniform_kernel_completion.md':
        '4f37ddd1bb41cef9614aa2f1da2629fa2c8bc8a27fc3b3b8392969075002f195',
}
H, HALF = F(1, 100), F(1, 2)
PRECISION, SQRT_BITS = 256, 240
KEYS = ('b', 'rb', 'sb', 'sa')
COORDINATES = ('r', 'b', 's', 'a')
ZERO = (F(0), F(0))
ANALYTIC_LIMITS = dict(pi=1, exponential=1, cosine=2, logarithm=3, cotangent=128)


class Inconclusive(ArithmeticError):
    pass


def require(condition, message):
    if not condition:
        raise Inconclusive(message)


def sha(path):
    digest = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1048576), b''):
            digest.update(block)
    return digest.hexdigest()


def canonical_sha(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True,
        separators=(',', ':')).encode()).hexdigest()


def rec(value):
    lo, hi = value
    assert lo <= hi
    return dict(finite=True, lower_rational=str(lo), upper_rational=str(hi))


def read_interval(value):
    assert value['finite'] is True
    result = F(value['lower_rational']), F(value['upper_rational'])
    assert result[0] <= result[1]
    return result


def point(value):
    return F(value), F(value)


def add(x, y):
    return x[0]+y[0], x[1]+y[1]


def neg(x):
    return -x[1], -x[0]


def sub(x, y):
    return add(x, neg(y))


def mul(x, y):
    products = [a*b for a in x for b in y]
    return min(products), max(products)


def scale(x, value):
    return mul(x, point(value))


def polynomial(coefficients, x):
    value = ZERO
    for coefficient in reversed(coefficients):
        value = add(mul(value, x), point(coefficient))
    return value


def root_interval(value):
    """Exactly squared dyadic endpoints, at the sole prescribed precision."""
    assert value >= 0
    denominator = 1 << SQRT_BITS
    n = isqrt((value.numerator << (2*SQRT_BITS))//value.denominator)
    lo = F(n, denominator)
    hi = lo if lo*lo == value else F(n+1, denominator)
    assert lo*lo <= value <= hi*hi
    return lo, hi


def h(x):
    return x*x/4-x*x*x/6


def hp(x):
    return x/2-x*x/2


def signed_gain(q, center, target, K, counts):
    """Exact two-edge candidate enclosure; no zero cap or point optimization."""
    counts['signed_gains'] += 1
    assert counts['signed_gains'] <= 192
    A, B = center
    L, R = target
    assert F('.18') <= A <= B <= HALF
    assert F('.18') <= L <= R <= HALF and K > 0
    # Both polynomials are expanded in their one free edge coordinate.
    coefficients = (
        (K*(h(B)-B*hp(B))-q*B, q+K*hp(B), -K/4, K/6),
        (q*R-K*h(R), -q+K*R/2, -K*(F(1, 4)+R/2), K/3),
    )
    domains = target, center
    radicands = (HALF-B)**2-2*q/K, (R-HALF)**2+4*q/K
    record = dict(force_rational=str(q), center=rec(center), target=rec(target),
                  K_rational=str(K), square_root_bits=SQRT_BITS, edges=[])
    values = []
    for index in range(2):
        coeff, domain, discriminant = coefficients[index], domains[index], radicands[index]
        edge = dict(fixed='center_upper' if index == 0 else 'target_upper',
            fixed_rational=str(B if index == 0 else R), domain=rec(domain),
            coefficients_rational=list(map(str, coeff)),
            discriminant_rational=str(discriminant), candidates=[], discarded_roots=[])
        record['edges'].append(edge)

        def save(kind, interval, raw=None):
            counts['gain_candidates'] += 1
            assert counts['gain_candidates'] <= 1536
            value = polynomial(coeff, interval)
            row = dict(kind=kind, argument=rec(interval), value=rec(value))
            if raw is not None:
                row['unclipped_root'] = rec(raw)
            edge['candidates'].append(row)
            values.append(value[1])

        for endpoint, name in zip(domain, ('left_endpoint', 'right_endpoint')):
            save(name, point(endpoint))
        if discriminant < 0:
            edge['square_root'] = None
            edge['discarded_roots'] = ['negative discriminant: both roots nonreal']
            continue
        counts['gain_square_roots'] += 1
        assert counts['gain_square_roots'] <= 384
        square_root = root_interval(discriminant)
        edge['square_root'] = rec(square_root)
        for sign in (-1, 1):
            if index == 0:
                raw = add(point(HALF), scale(square_root, sign))
            else:
                raw = scale(add(point(R+HALF), scale(square_root, sign)), F(1, 2))
            clipped = max(raw[0], domain[0]), min(raw[1], domain[1])
            if clipped[0] > clipped[1]:
                edge['discarded_roots'].append(dict(sign=sign,
                    untruncated=rec(raw), reason='whole root enclosure misses edge'))
            else:
                save('critical_minus' if sign < 0 else 'critical_plus', clipped, raw)
    assert values
    upper = max(values)
    record['upper_rational'] = str(upper)
    record['zero_cap_used'] = False
    return upper, record


def validate_projection(source, inputs):
    assert source['status'] == 'passed' and source['changed_inputs'] == []
    assert source['proof_path'] == SOURCE_PROOF
    assert source['proof_sha256'] == inputs[SOURCE_PROOF]
    assert source['checker_path'] == PROJECTOR
    assert source['checker_sha256'] == inputs[PROJECTOR]
    assert source['all_boundaries_complete'] is True
    assert source['reference_counts'] == {'0': 637, '1': 646}
    assert [case['epsilon'] for case in source['cases']] == [0, 1]
    for case in source['cases']:
        assert set(case['coordinates']) == set(COORDINATES)
        for coordinate in case['coordinates'].values():
            read_interval(coordinate['real'])
            read_interval(coordinate['imag'])
        assert len(case['slabs']) == 16
        for j, slab in enumerate(case['slabs']):
            assert slab['index'] == j
            assert tuple(map(F, slab['theta_rational'])) == (F(j, 16), F(j+1, 16))
            assert set(slab['arguments']) == set(KEYS)
            for argument in slab['arguments'].values():
                read_interval(argument['real'])
                read_interval(argument['imag'])


def guards(coordinates):
    out = {}
    for name in COORDINATES:
        x, y = coordinates[name]
        out[name+'_real'] = F('.24') <= x[0] <= x[1] <= F('.36')
        out[name+'_height'] = F('-.102') <= y[0] <= y[1] <= F('-.001')
    out['forced_targets_right_of_centers'] = coordinates['b'][0][1] < F('.4')
    out['shared_reflection'] = coordinates['s'][0][1] <= F('.36')
    out['positive_displacements'] = max(coordinates[n][1][1] for n in ('a', 'b')) < H
    return out


def ceiling_decimal(value):
    denominator = 10**12
    n = -((-value.numerator*denominator)//value.denominator)
    sign = '-' if n < 0 else ''
    q, r = divmod(abs(n), denominator)
    return sign+str(q)+'.'+str(r).zfill(12)


def write_record(path, result):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('xb') as raw:
        with gzip.GzipFile(filename='', mode='wb', compresslevel=1,
                           mtime=0, fileobj=raw) as compressed:
            with io.TextIOWrapper(compressed, encoding='utf-8') as stream:
                json.dump(result, stream, separators=(',', ':'))
                stream.write('\n')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if not str(args.output).endswith('.json.gz'):
        parser.error('output must be a new .json.gz file')
    if args.output.exists():
        raise FileExistsError(args.output)
    if hasattr(sys, 'set_int_max_str_digits'):
        sys.set_int_max_str_digits(0)
    inputs, fatal = {}, None
    counts = dict(pi=0, exponential=0, cosine=0, logarithm=0, cotangent=0,
        cases=0, slabs=0, vertices=0, signed_gains=0, gain_candidates=0,
        gain_square_roots=0, reference_calls=0, root_proposals=0,
        source_evaluations=0, original_primitives=0, optimizers=0,
        parameter_subdivisions=0, retries=0)
    result = dict(schema='mixed-terminal-two-selected-lift-budgets-v1',
        status='initializing', proof_path=PROOF, source_path=SOURCE,
        precision_bits=PRECISION, square_root_bits=SQRT_BITS,
        counts=counts, input_sha256=inputs, cases=[], fallback='none',
        all_four_budgets_enclosed=False, all_added_budgets_nonpositive=False,
        two_selected_terminal_raw_gap_rational=None, finite_source_gap_rational=None,
        whole_word_theorem_proved=False, knot_volume_theorem_proved=False)
    try:
        assert PINNED and all(isinstance(v, str) and len(v) == 64 for v in PINNED.values()), \
            'reviewed projection pins are not finalized'

        def bind(name, digest):
            assert isinstance(digest, str) and len(digest) == 64
            assert name not in inputs or inputs[name] == digest, name
            assert sha(ROOT/name) == digest, name
            inputs[name] = digest

        for name, digest in PINNED.items():
            bind(name, digest)
        own = Path(__file__).resolve().relative_to(ROOT).as_posix()
        bind(own, sha(ROOT/own))
        source = json.loads((ROOT/SOURCE).read_text())
        inherited_terminal = json.loads((ROOT/TERMINAL_AUDIT).read_text())
        for record in (source, inherited_terminal):
            assert record['changed_inputs'] == []
            for name, digest in record['input_sha256'].items():
                bind(name, digest)
        validate_projection(source, inputs)
        assert inherited_terminal['status'] == 'passed exact saved direct-cut and all-profile audit'
        assert inherited_terminal['all_27_terminal_profile_bounds_paid'] is True
        assert inherited_terminal['paid_real_entropy_branches'] == 36
        assert F(inherited_terminal['complete_profile_raw_floor_rational']) == F(1, 2600)
        assert inherited_terminal['input_sha256'][TERMINAL_CHECKER] == inputs[TERMINAL_CHECKER]
        result['projection_case_hashes'] = [canonical_sha(c) for c in source['cases']]
        result['reference_counts'] = source['reference_counts']
        result['all_boundaries_complete'] = source['all_boundaries_complete']

        # No analytic import, and no old provider/helper import, before all pins.
        from flint import arb, acb, ctx
        ctx.prec = PRECISION

        def ar(value):
            value = F(value)
            return arb(value.numerator)/arb(value.denominator)

        def ends(value):
            require(value.is_finite(), 'nonfinite elementary interval')
            return F(str(value.lower().fmpq())), F(str(value.upper().fmpq()))

        def ball(interval):
            lo, hi = interval
            out = arb(ar((lo+hi)/2), ar((hi-lo)/2).upper())
            low, high = ends(out)
            require(low <= lo <= hi <= high, 'outward interval conversion failed')
            return out

        def elementary(kind, argument=None):
            counts[kind] += 1
            assert counts[kind] <= ANALYTIC_LIMITS[kind]
            out = arb.pi() if kind == 'pi' else getattr(argument,
                dict(exponential='exp', cosine='cos', logarithm='log', cotangent='cot')[kind])()
            require(out.is_finite(), 'nonfinite '+kind)
            return out

        pi = elementary('pi')
        pi_interval = ends(pi)
        require(pi_interval[0] > 0, 'nonpositive pi bound')
        result['constants'] = dict(pi=rec(pi_interval))
        exponential_argument = 2*pi*ar(H)
        result['constants']['exponential_argument'] = rec(ends(exponential_argument))
        exponential = elementary('exponential', exponential_argument)
        result['constants']['exp_2piH'] = rec(ends(exponential))
        half_argument = 1+exponential
        result['constants']['half_log_argument'] = rec(ends(half_argument))
        require(half_argument > 0, 'half endpoint logarithm argument not separated')
        qhalf = elementary('logarithm', half_argument)
        half_lower = ends(qhalf)[0]
        result['constants']['q_half'] = rec(ends(qhalf))

        for original in source['cases']:
            counts['cases'] += 1
            row = dict(epsilon=original['epsilon'], status='initializing',
                projection_case_canonical_sha256=canonical_sha(original),
                coordinates=original['coordinates'], slabs=[], branches=[])
            result['cases'].append(row)
            try:
                coordinates = {name: (read_interval(original['coordinates'][name]['real']),
                    read_interval(original['coordinates'][name]['imag'])) for name in COORDINATES}
                row['domain_guards'] = guards(coordinates)
                require(all(row['domain_guards'].values()), 'ordinary reference domain guard failed')
                means, V = {key: ZERO for key in KEYS}, ZERO
                for j, source_slab in enumerate(original['slabs']):
                    counts['slabs'] += 1
                    assert counts['slabs'] <= 32
                    weight, weighted = F(1, 16), F(31-2*j, 512)
                    slab = dict(index=j, theta_rational=source_slab['theta_rational'],
                        projection_slab_canonical_sha256=canonical_sha(source_slab),
                        weight_rational=str(weight), weighted_rational=str(weighted), arguments={})
                    row['slabs'].append(slab)
                    real, imaginary = {}, {}
                    for key in KEYS:
                        source_argument = source_slab['arguments'][key]
                        x, y = read_interval(source_argument['real']), read_interval(source_argument['imag'])
                        witness = dict(real=rec(x), imag=rec(y))
                        slab['arguments'][key] = witness
                        require(0 < x[0] <= x[1] < 1, 'cotangent input outside original strip')
                        z = acb(ball(x), ball(y))
                        require(z.real > 0 and z.real < 1, 'outward cotangent input leaves strip')
                        witness['outward_argument'] = dict(real=rec(ends(z.real)), imag=rec(ends(z.imag)))
                        cot = elementary('cotangent', pi*z)
                        real[key], imaginary[key] = ends(cot.real), ends(cot.imag)
                        witness['cotangent'] = dict(real=rec(real[key]), imag=rec(imaginary[key]))
                    contributions = {key: scale(imaginary[key], weight) for key in KEYS}
                    vertical = scale(sub(sub(scale(real['b'], 3), real['rb']), real['sb']), weighted)
                    slab['mean_contributions'] = {key: rec(v) for key, v in contributions.items()}
                    slab['vertical_contribution'] = rec(vertical)
                    means = {key: add(means[key], contributions[key]) for key in KEYS}
                    V = add(V, vertical)
                row['normalized_means'] = {key: rec(value) for key, value in means.items()}
                row['normalized_vertical'] = rec(V)
                delta_b = sub(point(H), coordinates['b'][1])
                delta_a = sub(point(H), coordinates['a'][1])
                kappa = mul(pi_interval, delta_b)
                require(kappa[0] > 0 and delta_a[0] > 0, 'nonpositive lift')
                Vplus = max(F(0), V[1])
                v_lower = pi_interval[0]*delta_a[0]*max(F(0), 1-means['sa'][1])
                d_s = HALF-coordinates['s'][0][0]
                Bupper = coordinates['b'][0][1]
                row['lift_data'] = dict(delta_b=rec(delta_b), delta_a=rec(delta_a),
                    kappa=rec(kappa), V_positive_upper_rational=str(Vplus),
                    v_lower_rational=str(v_lower), shared_s_displacement_upper_rational=str(d_s))
                cosine_argument = 2*pi*ar(Bupper)
                row['forced_endpoint'] = dict(B_upper_rational=str(Bupper),
                    cosine_argument=rec(ends(cosine_argument)),
                    q_half_lower_rational=str(half_lower), chord_factor_rational=str((HALF-Bupper)/2))
                cosine = elementary('cosine', cosine_argument)
                row['forced_endpoint']['cosine'] = rec(ends(cosine))
                norm_square = 1+exponential*exponential-2*exponential*cosine
                row['forced_endpoint']['modulus_square'] = rec(ends(norm_square))
                require(norm_square > 0, 'forced endpoint logarithm argument not separated')
                qend_ball = elementary('logarithm', norm_square)/2
                qend = ends(qend_ball)
                row['forced_endpoint']['q_end'] = rec(qend)
                for mu in (1, 0):
                    intervals = [kappa, means['b'], means['rb'], means['sb']]
                    names = ['kappa', 'I_b', 'I_rb', 'I_sb']
                    if mu == 0:
                        intervals.append(qend)
                        names.append('q_end')
                    branch = dict(mu=mu, target=rec((F('.22'), F('.45')) if mu else (F('.4'), F('.45'))),
                        variable_order=names, variable_intervals=[rec(v) for v in intervals], vertices=[])
                    row['branches'].append(branch)
                    for flags in itertools.product((0, 1), repeat=len(intervals)):
                        counts['vertices'] += 1
                        assert counts['vertices'] <= 96
                        values = [interval[index] for interval, index in zip(intervals, flags)]
                        k, ib, irb, isb = values[:4]
                        ar_force = k*(1-irb)
                        ab_factorial = k*(3*ib-irb-isb-1)
                        ab_force = ab_factorial if mu else ab_factorial+values[4]
                        vertical_upper = k*k*Vplus/pi_interval[0]
                        selected_upper = -2*pi_interval[0]*H if mu else \
                            -(HALF-Bupper)*(values[4]+half_lower)/2
                        shared_expression = k*(1+isb)-2*v_lower
                        debit = d_s*max(F(0), shared_expression)
                        vertex = dict(flags=list(flags), values_rational=list(map(str, values)),
                            forces_rational=dict(r=str(ar_force), b_factorial=str(ab_factorial), b=str(ab_force)),
                            vertical_upper_rational=str(vertical_upper),
                            selected_trial_upper_rational=str(selected_upper),
                            shared_expression_rational=str(shared_expression),
                            shared_debit_upper_rational=str(debit), gains={})
                        branch['vertices'].append(vertex)
                        r_upper, r_gain = signed_gain(ar_force, coordinates['r'][0],
                            (F('.22'), HALF), F(88, 5), counts)
                        vertex['gains']['r'] = r_gain
                        b_upper, b_gain = signed_gain(ab_force, coordinates['b'][0],
                            (F('.22'), F('.45')) if mu else (F('.4'), F('.45')),
                            F((mu+1)*49, 5), counts)
                        vertex['gains']['b'] = b_gain
                        upper = vertical_upper+selected_upper+debit+r_upper+b_upper
                        vertex['upper_rational'] = str(upper)
                    assert len(branch['vertices']) == (16 if mu else 32)
                    worst = max(F(v['upper_rational']) for v in branch['vertices'])
                    branch['upper_rational'] = str(worst)
                    branch['nonpositive'] = worst <= 0
                    branch['maximizing_flags'] = [v['flags'] for v in branch['vertices']
                                                  if F(v['upper_rational']) == worst]
                row['status'] = 'enclosed both added budgets'
            except Inconclusive as exc:
                row['status'] = 'inconclusive'
                row['error'] = dict(type=type(exc).__name__, message=str(exc))
            except BaseException as exc:
                row['status'] = 'unexpected error'
                row['error'] = dict(type=type(exc).__name__, message=str(exc))
                fatal = exc
                break
        complete = len(result['cases']) == 2 and all(
            row['status'] == 'enclosed both added budgets' for row in result['cases'])
        result['all_four_budgets_enclosed'] = complete
        result['status'] = 'completed fixed protocol' if fatal is None else 'unexpected error'
        if complete:
            assert all(counts[key] == value for key, value in ANALYTIC_LIMITS.items())
            assert counts['slabs'] == 32 and counts['vertices'] == 96 and counts['signed_gains'] == 192
            worst = max(F(branch['upper_rational']) for case in result['cases'] for branch in case['branches'])
            result['worst_budget_upper_rational'] = str(worst)
            result['all_added_budgets_nonpositive'] = worst <= 0
            if worst <= 0:
                result['two_selected_terminal_raw_gap_rational'] = '1/2600'
                result['finite_source_gap_rational'] = '1/5200'
    except BaseException as exc:
        fatal = exc
        result['status'] = 'unexpected error'
        result['error'] = dict(type=type(exc).__name__, message=str(exc))
    changed = []
    for name, digest in inputs.items():
        try:
            if sha(ROOT/name) != digest:
                changed.append(name)
        except OSError:
            changed.append(name)
    result['changed_inputs'] = changed
    if changed or fatal is not None:
        result['all_added_budgets_nonpositive'] = False
        result['two_selected_terminal_raw_gap_rational'] = None
        result['finite_source_gap_rational'] = None
    if changed:
        result['status'] = 'changed inputs'
    result['unvisited_cases'] = [epsilon for epsilon in (0, 1)
                                if epsilon not in [row['epsilon'] for row in result['cases']]]
    result['proof_sha256'] = inputs.get(PROOF)
    result['source_sha256'] = inputs.get(SOURCE)
    result['checker_sha256'] = inputs.get(PROJECTOR)
    write_record(args.output, result)
    worst = result.get('worst_budget_upper_rational')
    print(json.dumps(dict(status=result['status'], counts=counts, bindings=len(inputs),
        all_added_budgets_nonpositive=result['all_added_budgets_nonpositive'],
        worst_upper_decimal_ceiling=None if worst is None else ceiling_decimal(F(worst)),
        output_sha256=sha(args.output))))
    if fatal is not None:
        raise fatal


if __name__ == '__main__':
    main()
