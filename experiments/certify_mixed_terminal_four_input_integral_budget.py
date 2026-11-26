#!/usr/bin/env python3
"""Fixed whole-D4 height-integral test: two cases, 16 slabs, no fallback.

Only elementary interval cotangent/exp/trigonometric/logarithm calls.
No original primitive, root, source, optimizer, inverse or subdivision.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from math import isqrt
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
PROOF = 'notes/research_mixed_terminal_four_input_integral_budget.md'
SOURCE = 'repro/results/research-mixed-terminal-split-taylor-completion.json'
SOURCE_PROOF = 'notes/research_mixed_terminal_all_input_affine_enclosures.md'
SOURCE_CHECKER = 'experiments/check_mixed_terminal_split_taylor_completion.py'
SPLIT = 'repro/results/research-mixed-terminal-split-taylor-inclusion.json'
AFFINE = 'repro/results/research-mixed-terminal-correlated-affine-family.json'
COST_PROOF = 'notes/research_mixed_terminal_symmetric_pair_costs.md'
COST_CHECKER = 'experiments/check_mixed_terminal_symmetric_pair_costs.py'
COST_AUDIT = 'repro/results/research-mixed-terminal-symmetric-pair-costs.json'
PINNED = {
    'notes/research_mixed_terminal_four_input_integral_budget.md':
        '90ec6c9d4b3641a01e789b64dd0d26053b402c2914b99cafe81eff8ad4265cb9',
    'repro/results/research-mixed-terminal-split-taylor-completion.json':
        'e04521450e1973658cbd602aa0a8f54d4c7d40c968b4b90d65374d570981c617',
    'notes/research_mixed_terminal_all_input_affine_enclosures.md':
        '6412be85ca87c01a0b363191c724dc1e7357c00939ce5c379a7c501f3565215f',
    'experiments/check_mixed_terminal_split_taylor_completion.py':
        'bfa49b46454c324d05047352251e6f7aefa68cbec8d53ab5914c935bec502580',
    'repro/results/research-mixed-terminal-split-taylor-inclusion.json':
        'a25587e526dc753306eb690b76f1f07d0d05410be315c6675023bd87ae42e202',
    'repro/results/research-mixed-terminal-correlated-affine-family.json':
        '51b702aa6ea44aa5891bc1146a7d5c0d22686cd814f9bbe5d9c4c63b9a16f9e1',
    'repro/results/research-mixed-terminal-correlated-affine-family-saved-audit.json':
        '2638c47a2b0216f04bb4f31e4f6bdd86d9c2b17cdfd00ea880835dcf80d97959',
    'notes/research_mixed_terminal_symmetric_pair_costs.md':
        'b4ee1a7bdde317edab0210b20cb8616913984c4f992d1cbed240f6092a8e593f',
    'experiments/check_mixed_terminal_symmetric_pair_costs.py':
        'fba012dc5e5fd238521c4bfdbab5805ce6027f31dcb0652d1b84e4369960cf9a',
    'repro/results/research-mixed-terminal-symmetric-pair-costs.json':
        '3069d85deea24cb747feacf233bcd4bca15dd6b2bda4ace68547c68135bbcc08',
    'notes/research_mixed_terminal_one_parameter_transport.md':
        '1fdc3b445ea4a43319f16eeee20e739d608d7133b5471ccb40042174affefddd',
    'notes/research_mixed_terminal_joint_main_budget.md':
        '5c3e23f070d27628b3843030cd4bced887fcc7e76e25b15ed8d73a6816369baa',
    'notes/research_mixed_terminal_cubic_cost_and_response_bounds.md':
        'dfc3f415e742aa9c632707aea7c699bb2ccbdc054c08fc7ba640e943bcdaa741',
    'notes/research_mixed_terminal_main_optimizer_localization.md':
        '6e88ab6d8635255877ae6ba570d6d8e434880f8a01c710452ed48b4cde482295',
    'notes/research_mixed_terminal_full_input_index_barrier.md':
        '45ae03bf28a78df930fc8e7c97054ca40689630423a4d36c0009b6b0bb900ee2',
    'notes/research_mixed_terminal_joint_main_curvature_budget.md':
        '90b947d752c6ed646b897945ff3eb3b1beffe45074dce80087c87379e1ef04ee',
    'notes/research_mixed_terminal_correlated_affine_family_certificate.md':
        '0ba6a11f26a17e3642a41c6bd97cf93a01c1c7a5c4dd2437d3ee23435dfb8957',
    'notes/research_mixed_terminal_correlated_affine_family_completion.md':
        '5b814d6eadb78eb8636d6144505dc826898a8956f73aab28f03af36873946b3e',
    'notes/research_mixed_terminal_split_taylor_inclusion.md':
        '461c0fe2eb943a791d91b94ce1627e4c650fcaf80623873cd0b53f963e05bd17',
}
NAMES = ('e', 'xi', 't', 'a', 's')
H, RADIUS = F(1, 100), F(8, 125)
PARAMETER_CENTER = (F(3, 10), -F(13, 250))
PRECISION = 256
SQRT_BITS = 240
ZERO, ONE = (F(0), F(0)), (F(1), F(1))


class Inconclusive(ArithmeticError):
    pass


def sha(path):
    digest = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1048576), b''):
            digest.update(block)
    return digest.hexdigest()


def canonical_sha(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True,
        separators=(',', ':')).encode()).hexdigest()


def require(condition, message):
    if not condition:
        raise Inconclusive(message)


def interval_record(value):
    lo, hi = value
    assert lo <= hi
    return dict(finite=True, lower_rational=str(lo), upper_rational=str(hi))


def exact(value):
    return F(value), F(value)


def add(x, y):
    return x[0]+y[0], x[1]+y[1]


def neg(x):
    return -x[1], -x[0]


def sub(x, y):
    return add(x, neg(y))


def mul(x, y):
    values = [a*b for a in x for b in y]
    return min(values), max(values)


def scale(x, y):
    return mul(x, exact(y))


def poly(coefficients, x):
    out = ZERO
    for coefficient in reversed(coefficients):
        out = add(mul(out, x), exact(coefficient))
    return out


def clip_interval(x, lo, hi):
    assert lo <= hi
    return tuple(min(hi, max(lo, endpoint)) for endpoint in x)


def sqrt_interval(value):
    """An exact dyadic enclosure, with no floating square root."""
    value = F(value)
    assert value >= 0
    scale_int = 1 << SQRT_BITS
    n = isqrt((value.numerator << (2*SQRT_BITS))//value.denominator)
    low = F(n, scale_int)
    high = low if low*low == value else F(n+1, scale_int)
    assert low*low <= value <= high*high
    return low, high


def modulus_witness(z):
    square = z[0]*z[0]+z[1]*z[1]
    bounds = sqrt_interval(square)
    return bounds[1], dict(coefficient=[str(x) for x in z],
        squared_modulus_rational=str(square), modulus=interval_record(bounds))


def gain(force, center, target, K):
    """Equations (15)--(18), retaining every displacement branch."""
    c_lo, c_hi = center
    L, R = target
    assert F('0.18') <= L <= c_lo <= c_hi <= R <= F('0.5')
    d, p, q = F('0.5')-c_hi, max(F(0), -force[0]), max(F(0), force[1])
    assert d > 0 and K > 0
    minus_max, plus_max = c_hi-L, R-c_lo
    branches = []

    def save(name, domain, coefficients, radicand, root, chosen, decision):
        value = poly(coefficients, chosen)
        branches.append(dict(name=name, domain=interval_record(domain),
            coefficients_rational=list(map(str, coefficients)),
            radicand_rational=None if radicand is None else str(radicand),
            square_root=None if root is None else interval_record(root),
            optimizer=interval_record(chosen), value=interval_record(value),
            decision=decision))

    radicand = d*d+2*p/K
    root = sqrt_interval(radicand)
    point = clip_interval(sub(root, exact(d)), F(0), minus_max)
    save('negative displacement', (F(0), minus_max),
         (F(0), p, -K*d/2, -K/6), radicand, root, point, 'clipped unique maximum')
    upper = min(plus_max, d)
    if q >= K*d*d/2:
        save('positive displacement below d', (F(0), upper),
             (F(0), q, -K*d/2, K/6), None, None, exact(upper),
             'q >= K*d^2/2: right endpoint')
    else:
        radicand = d*d-2*q/K
        root = sqrt_interval(radicand)
        point = clip_interval(sub(exact(d), root), F(0), upper)
        save('positive displacement below d', (F(0), upper),
             (F(0), q, -K*d/2, K/6), radicand, root, point, 'clipped smaller root')
    if plus_max > d:
        radicand = q/K
        root = sqrt_interval(radicand)
        point = clip_interval(root, d, plus_max)
        save('positive displacement above d', (d, plus_max),
             (F(0), q, F(0), -K/3), radicand, root, point,
             'actual d >= displacement: cubic cost K*v^3/3')
    upper_value = max(F(0), *(F(b['value']['upper_rational']) for b in branches))
    return upper_value, dict(force=interval_record(force), center=interval_record(center),
        target=interval_record(target), K_rational=str(K), d_rational=str(d),
        p_rational=str(p), q_rational=str(q), branches=branches,
        upper_rational=str(upper_value))


def supports(source, row):
    centers = dict(zip(NAMES, [tuple(map(F, z)) for z in source['center_exact']]))
    responses = dict(zip(NAMES, [tuple(map(F, z)) for z in source['response_exact']]))
    errors = dict(zip(NAMES, map(F, source['posterior_radii_rational'])))
    assert len(centers) == len(responses) == len(errors) == 5
    individual, widths = {}, {}
    for name in NAMES:
        mod, witness = modulus_witness(responses[name])
        width = RADIUS*mod+errors[name]
        widths[name] = width
        individual[name] = tuple((c-width, c+width) for c in centers[name])
        row['individual_supports'][name] = dict(modulus_witness=witness,
            error_radius_rational=str(errors[name]), width_rational=str(width),
            real=interval_record(individual[name][0]),
            imag=interval_record(individual[name][1]))
    real, theta_cache = {}, {}
    real['a'] = individual['a'][0]
    for name in ('s', 't'):
        coefficient = tuple(responses[name][i]+responses['a'][i] for i in range(2))
        mod, witness = modulus_witness(coefficient)
        width = RADIUS*mod+errors[name]+errors['a']
        midpoint = centers[name][0]+centers['a'][0]
        real[name] = midpoint-width, midpoint+width
        row['shared_real_supports'][name] = dict(modulus_witness=witness,
            width_rational=str(width), interval=interval_record(real[name]))

    def imaginary(name, theta):
        key = name, theta
        if key not in theta_cache:
            weight = 1-theta
            if name == 'a':
                midpoint = weight*centers['a'][1]+theta*H
                width = weight*widths['a']
                witness = None
            else:
                coefficient = tuple(responses[name][i]+weight*responses['a'][i]
                                    for i in range(2))
                mod, witness = modulus_witness(coefficient)
                midpoint = centers[name][1]+weight*centers['a'][1]+theta*H
                width = RADIUS*mod+errors[name]+weight*errors['a']
            value = midpoint-width, midpoint+width
            theta_cache[key] = value, dict(node=name, theta_rational=str(theta),
                midpoint_rational=str(midpoint), width_rational=str(width),
                modulus_witness=witness, interval=interval_record(value))
        return theta_cache[key]

    return individual, real, imaginary


def domain_guards(individual, epsilon):
    def inside(name, component, lo, hi):
        a, b = individual[name][component]
        return F(lo) <= a <= b <= F(hi)
    tests = {
        'ordinary_real': inside('s', 0, '.24', '.36'),
        'ordinary_height': inside('s', 1, '-.102', '-.001'),
        'selected_real': inside('a', 0, '.22', '.45'),
        'selected_height': inside('a', 1, '-.108', '0'),
        'terminal_real': inside('t', 0, '.22', '.4'),
        'cubic_terminal_height': inside('t', 1, '-.108', '.108'),
        'terminal_original_height': inside('t', 1, '-.108' if epsilon else '-.072',
                                          '-.020' if epsilon else '.021'),
        'private_real': inside('e' if epsilon else 'xi', 0,
                               '.27' if epsilon else '.1', '.49' if epsilon else '.4'),
        'private_original_height': inside('e' if epsilon else 'xi', 1,
                                          '-.051' if epsilon else '.049',
                                          '-.019' if epsilon else '.077'),
        'positive_delta': individual['a'][1][1] < H,
        'positive_log_sine': F(1, 6) < individual['a'][0][0]
                             <= individual['a'][0][1] < F(1, 2),
        'external_full_input_barrier': -F('.12') <= PARAMETER_CENTER[1]-RADIUS
            and PARAMETER_CENTER[1]+RADIUS <= F('.08'),
        'external_pair_height': max(abs(PARAMETER_CENTER[1]-RADIUS),
                                    abs(PARAMETER_CENTER[1]+RADIUS)) <= F('.12'),
        'external_reference_real': F('.22') <= PARAMETER_CENTER[0]-RADIUS
            and PARAMETER_CENTER[0]+RADIUS <= F('.45'),
    }
    return tests


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    if hasattr(sys, 'set_int_max_str_digits'):
        sys.set_int_max_str_digits(0)
    inputs = {}
    counts = dict(reference_data_cases=0, height_slabs=0, cotangent=0, pi=0,
                  exponential=0, cosine=0, sine=0, logarithm=0, cubic_gains=0,
                  roots=0, inverses=0, optimizers=0, original_primitives=0,
                  source_evaluations=0, parameter_subdivisions=0, retries=0)
    result = dict(status='initializing', proof_path=PROOF, source_path=SOURCE,
        precision_bits=PRECISION, square_root_bits=SQRT_BITS, input_sha256=inputs,
        counts=counts, cases=[], fallback='none', uniform_main_phase_gap_proved=False,
        uniform_finite_source_gap_proved=False, global_knot_theorem_proved=False)
    fatal = None
    try:
        assert PINNED and all(isinstance(d, str) and len(d) == 64 for d in PINNED.values())

        def bind(name, digest):
            assert name not in inputs or inputs[name] == digest, name
            assert sha(ROOT/name) == digest, name
            inputs[name] = digest

        for name, digest in PINNED.items():
            bind(name, digest)
        own = Path(__file__).resolve().relative_to(ROOT).as_posix()
        bind(own, sha(ROOT/own))
        posterior, split, affine, cost_audit = [json.loads((ROOT/name).read_text())
                                       for name in (SOURCE, SPLIT, AFFINE, COST_AUDIT)]
        for record in (posterior, split, affine, cost_audit):
            for key in ('input_sha256', 'dependencies_sha256'):
                for name, digest in record.get(key, {}).items():
                    bind(name, digest)
            assert record['changed_inputs'] == []
        assert posterior['status'] == 'passed'
        assert posterior['all_four_input_disks_certified'] is True
        assert posterior['checker_sha256'] == inputs[SOURCE_CHECKER]
        assert posterior['proof_sha256'] == inputs[SOURCE_PROOF]
        assert posterior['source_path'] == SPLIT and posterior['source_sha256'] == inputs[SPLIT]
        assert split['status'] == 'completed fixed saved-only protocol'
        assert split['all_four_input_families_certified'] is True
        assert split['source_path'] == AFFINE and split['source_sha256'] == inputs[AFFINE]
        assert cost_audit['status'] == 'passed'
        assert cost_audit['checker_sha256'] == inputs[COST_CHECKER]
        assert cost_audit['proof_sha256'] == inputs[COST_PROOF]
        chosen = [p for p in posterior['posterior_enclosures'] if p['beta'] == 1]
        assert [(p['beta'], p['epsilon']) for p in chosen] == [(1, 0), (1, 1)]
        for p in chosen:
            assert F(p['multiplier_rational']) == 1
            assert p['exact_linear_system_verified'] is True
            assert tuple(map(F, p['parameter_center'])) == PARAMETER_CENTER
            assert F(p['parameter_radius_rational']) == RADIUS
            split_case = split['cases'][2+p['epsilon']]
            original = affine['cases'][2+p['epsilon']]
            assert (split_case['beta'], split_case['epsilon']) == (1, p['epsilon'])
            assert (original['beta'], original['epsilon']) == (1, p['epsilon'])
            assert p['source_case_canonical_sha256'] == canonical_sha(split_case)
            assert split_case['source_case_canonical_sha256'] == canonical_sha(original)
            assert p['center_exact'] == split_case['original_center'] == original['center']
            assert p['response_exact'] == split_case['original_response'] == original['response_exact']
            split_candidate = [c for c in split_case['candidates']
                               if F(c['multiplier_rational']) == 1]
            candidate = [c for c in original['candidates']
                         if F(c['multiplier_rational']) == 1]
            assert len(split_candidate) == len(candidate) == 1
            assert split_candidate[0]['criterion_pass'] is True
            assert p['source_candidate_canonical_sha256'] == canonical_sha(split_candidate[0])
            assert split_candidate[0]['source_candidate_canonical_sha256'] == canonical_sha(candidate[0])
            assert all(F(0) <= F(x) < F(y) for x, y in zip(
                p['posterior_radii_rational'], p['original_radii_rational']))

        # No analytic library is loaded until all direct/inherited inputs are verified.
        from flint import arb, acb, ctx
        ctx.prec = PRECISION

        def ar(value):
            value = F(value)
            return arb(value.numerator)/arb(value.denominator)

        def ends(value):
            require(value.is_finite(), 'nonfinite elementary enclosure')
            return F(str(value.lower().fmpq())), F(str(value.upper().fmpq()))

        def ball(value):
            lo, hi = value
            out = arb(ar((lo+hi)/2), ar((hi-lo)/2).upper())
            blo, bhi = ends(out)
            require(blo <= lo <= hi <= bhi, 'outward ball conversion failed')
            return out

        def elementary(kind, value=None):
            maxima = dict(pi=1, exponential=1, cosine=2, sine=2, logarithm=5, cotangent=96)
            counts[kind] += 1
            assert counts[kind] <= maxima[kind], kind
            if kind == 'pi':
                out = arb.pi()
            else:
                method = dict(exponential='exp', cosine='cos', sine='sin',
                              logarithm='log', cotangent='cot')[kind]
                out = getattr(value, method)()
            require(out.is_finite(), 'nonfinite '+kind+' enclosure')
            return out

        pi = elementary('pi')
        pi_bounds = ends(pi)
        exp_height = elementary('exponential', 2*pi*ar(H))
        log_two = elementary('logarithm', arb(2))
        result['constants'] = dict(pi=interval_record(pi_bounds),
            exp_2piH=interval_record(ends(exp_height)), log_two=interval_record(ends(log_two)))
        for p in chosen:
            counts['reference_data_cases'] += 1
            epsilon = p['epsilon']
            row = dict(beta=1, epsilon=epsilon, status='initializing',
                source_entry_canonical_sha256=canonical_sha(p),
                source_case_canonical_sha256=p['source_case_canonical_sha256'],
                source_candidate_canonical_sha256=p['source_candidate_canonical_sha256'],
                center_exact=p['center_exact'], response_exact=p['response_exact'],
                posterior_radii_rational=p['posterior_radii_rational'],
                parameter_center=p['parameter_center'],
                parameter_radius_rational=p['parameter_radius_rational'],
                individual_supports={}, shared_real_supports={}, slabs=[], branches=[])
            result['cases'].append(row)
            try:
                individual, real, imaginary = supports(p, row)
                row['domain_guards'] = domain_guards(individual, epsilon)
                require(all(row['domain_guards'].values()), 'original domain/height guard failed')
                totals = dict(V=ZERO, S=ZERO, T=ZERO, A=ZERO)
                for index in range(16):
                    left, right = F(index, 16), F(index+1, 16)
                    weight, weighted = F(1, 16), F(31-2*index, 512)
                    slab = dict(index=index, theta=interval_record((left, right)),
                        weight_rational=str(weight), weighted_rational=str(weighted), nodes={})
                    row['slabs'].append(slab)
                    counts['height_slabs'] += 1
                    C, I = {}, {}
                    for name in ('a', 's', 't'):
                        low_value, low_witness = imaginary(name, left)
                        high_value, high_witness = imaginary(name, right)
                        height = min(low_value[0], high_value[0]), max(low_value[1], high_value[1])
                        node = dict(real=interval_record(real[name]), imag=interval_record(height),
                                    endpoint_supports=[low_witness, high_witness])
                        slab['nodes'][name] = node
                        require(0 < real[name][0] <= real[name][1] < 1,
                                'original cotangent argument left strip')
                        input_value = acb(ball(real[name]), ball(height))
                        require(input_value.real > 0 and input_value.real < 1,
                                'rounded cotangent argument left strip')
                        output = elementary('cotangent', pi*input_value)
                        C[name], I[name] = ends(output.real), ends(output.imag)
                        node['cotangent'] = dict(real=interval_record(C[name]), imag=interval_record(I[name]))
                    terms = dict(V=scale(sub(sub(scale(C['a'], 3), C['s']), C['t']), weighted),
                        S=scale(sub(ONE, I['s']), weight),
                        T=scale(neg(add(ONE, I['t'])), weight),
                        A=scale(sub(sub(sub(scale(I['a'], 3), I['s']), I['t']), ONE), weight))
                    slab['integral_contributions'] = {k: interval_record(v) for k, v in terms.items()}
                    totals = {k: add(totals[k], terms[k]) for k in totals}
                row['normalized_integrals'] = {k: interval_record(v) for k, v in totals.items()}
                delta = sub(exact(H), individual['a'][1])
                require(delta[0] > 0, 'nonpositive height displacement')
                pi_delta = mul(pi_bounds, delta)
                W = mul(mul(pi_delta, delta), totals['V'])
                As, At, Aa1 = (mul(pi_delta, totals[k]) for k in ('S', 'T', 'A'))
                row['height_displacement'] = interval_record(delta)
                row['W'] = interval_record(W)
                cosine = elementary('cosine', 2*pi*ball(individual['a'][0]))
                modulus_square = 1+exp_height*exp_height-2*exp_height*cosine
                require(modulus_square > 0, 'forced-force logarithm is not positive')
                own_force = ends(elementary('logarithm', modulus_square)/2)
                sine = elementary('sine', pi*ar(individual['a'][0][1]))
                require(sine > 0, 'log-sine argument is not positive')
                log_sine = elementary('logarithm', 2*sine)
                bracket = add(ends(log_sine), ends(log_two))
                require(bracket[0] > 0, 'J chord logarithmic bracket is not positive')
                G_H = -(F(1, 2)-individual['a'][0][1])*bracket[0]/2
                Aa0 = add(Aa1, own_force)
                row['forced_additions'] = dict(cosine=interval_record(ends(cosine)),
                    modulus_square=interval_record(ends(modulus_square)),
                    own_force=interval_record(own_force), sine_at_A_upper=interval_record(ends(sine)),
                    log_sine=interval_record(ends(log_sine)), bracket=interval_record(bracket),
                    J_upper_rational=str(G_H))
                row['forces'] = {k: interval_record(v) for k, v in
                                 dict(s=As, t=At, a_factorial=Aa1, a_forced=Aa0).items()}
                Gs, gs_record = gain(As, individual['s'][0], (F('.22'), F('.5')), F(88, 5))
                Gt, gt_record = gain(At, individual['t'][0], (F('.22'), F('.4')), F((3+epsilon)*22, 5))
                counts['cubic_gains'] += 2
                row['shared_gains'] = dict(s=gs_record, t=gt_record)
                for nu, force in ((1, Aa1), (0, Aa0)):
                    Ga, ga_record = gain(force, individual['a'][0], (F('.22'), F('.45')), F((nu+1)*49, 5))
                    counts['cubic_gains'] += 1
                    trial_upper = W[1]-2*pi_bounds[0]*H if nu else W[1]+G_H
                    budget = trial_upper+Gs+Ga+Gt
                    row['branches'].append(dict(nu=nu, selected_gain=ga_record,
                        trial_upper_rational=str(trial_upper),
                        budget_upper_rational=str(budget), strictly_negative=budget < 0))
                row['status'] = 'enclosed both full-P branches'
            except Inconclusive as exc:
                row['status'] = 'inconclusive'
                row['error'] = dict(type=type(exc).__name__, message=str(exc))
            except Exception as exc:
                row['status'] = 'unexpected error'
                row['error'] = dict(type=type(exc).__name__, message=str(exc))
                fatal = exc
        complete = all(c['status'] == 'enclosed both full-P branches' for c in result['cases'])
        assert len(result['cases']) == 2
        result['status'] = 'completed fixed protocol' if fatal is None else 'unexpected error'
        result['all_four_budgets_enclosed'] = complete
        if complete:
            assert counts['height_slabs'] == 32 and counts['cotangent'] == 96
            assert counts['cosine'] == counts['sine'] == 2 and counts['logarithm'] == 5
            assert counts['cubic_gains'] == 8
            worst = max(F(b['budget_upper_rational']) for c in result['cases'] for b in c['branches'])
            result['worst_budget_upper_rational'] = str(worst)
            result['uniform_main_phase_gap_proved'] = worst < 0
            result['common_margin_rational'] = str(-worst) if worst < 0 else None
    except Exception as exc:
        fatal = exc
        result['status'] = 'unexpected error'
        result['error'] = dict(type=type(exc).__name__, message=str(exc))
    result['changed_inputs'] = [name for name, digest in inputs.items() if sha(ROOT/name) != digest]
    if result['changed_inputs']:
        result['uniform_main_phase_gap_proved'] = False
        result['status'] = 'changed inputs'
    result['proof_sha256'] = inputs.get(PROOF)
    result['source_sha256'] = inputs.get(SOURCE)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open('x', encoding='utf-8') as stream:
        json.dump(result, stream, separators=(',', ':'))
        stream.write('\n')
    print(json.dumps(dict(status=result['status'], counts=counts,
        uniform_main_phase_gap_proved=result['uniform_main_phase_gap_proved'],
        worst_budget_upper_rational=result.get('worst_budget_upper_rational'),
        output_sha256=sha(args.output))))
    if fatal is not None:
        raise fatal


if __name__ == '__main__':
    main()
