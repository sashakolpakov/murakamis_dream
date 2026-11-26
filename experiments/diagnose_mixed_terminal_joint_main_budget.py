#!/usr/bin/env python3
"""Eight joint-main affine supports from four already certified suffixes.

No reference proposal, root solve, target optimization, transport, subdivision,
alternate height, or retry. Positive upper bounds are not source obstructions.
"""
import argparse
from fractions import Fraction as F
import hashlib
import itertools
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROOF = 'notes/research_mixed_terminal_joint_main_budget.md'
SOURCE = 'repro/results/research-mixed-terminal-horizontal-envelope-diagnostic.json'
AUDIT = 'repro/results/research-mixed-terminal-horizontal-envelope-saved-audit.json'
CHECKER = 'experiments/check_mixed_terminal_horizontal_envelope_record.py'
PINNED = {'experiments/check_mixed_terminal_horizontal_envelope_record.py': '23545f9f66ec7ba9e2ddb89410f9c198a64f4d615b95df4d346bc2083936cdcb',
 'notes/research_mixed_plateau_window_concave_profiles.md': 'ba03fd9804c63274b8015532d3c176a044e9b7f0bdd34d69331f420522c88d19',
 'notes/research_mixed_second_selected_four_profile_reduction.md': 'd084b535d83a08e50c4baddc52249c8495d88cde65f8c81e04baff566560d25e',
 'notes/research_mixed_selected_weight_branch_domains.md': '081aa8c7491f0c2aebfe0cb9431ff2b304f592b52b07fa2d0544cd8175981b3d',
 'notes/research_mixed_terminal_concave_profile_envelope.md': '6d71c0470a9fe1598cdc46459ffcda98f807eb84c1be8bc2810517706a744ddd',
 'notes/research_mixed_terminal_four_reduced_currents.md': 'cc4dfa641fdbeab421edf9e450e8ed7ac9c55daff46e0a8153d9e5a65656666c',
 'notes/research_mixed_terminal_horizontal_envelope_diagnostic.md': 'ea1e6d1daf4b8e3822a198de1f63f4f211061761af8bdd01d641b4d8f930ad72',
 'notes/research_mixed_terminal_horizontal_envelope_obstruction.md': '71377253981b2448cc8f69650f25ac231d8f16ee17ced054aa7499895e7ca5de',
 'notes/research_mixed_terminal_joint_main_budget.md': '5c3e23f070d27628b3843030cd4bced887fcc7e76e25b15ed8d73a6816369baa',
 'notes/research_mixed_terminal_three_critical_curve.md': 'bc279f1acb8751c752ebd630f765b9e43d76e6a7f59f979d713b194feb93dfda',
 'repro/results/research-mixed-terminal-horizontal-envelope-diagnostic.json': 'ca58c35640f1e2894f35b0f2c841029ff28b1c4af8411c1a12da012ace09059b',
 'repro/results/research-mixed-terminal-horizontal-envelope-saved-audit.json': 'bedf680b3f57c799980517f7aa6178a7f9c5a0890bac8528947e9018baf7a4de'}
HEIGHT = F(1, 100)
NAMES = ('e', 'xi', 't', 'a', 's')
CENTERS = ((F(7, 20), -F(1, 100)), (F(3, 10), -F(13, 250)))
ARGUMENT_NAMES = ('a', 'sa', 'ta', 'aH', 'saH', 'taH')


def sha(path):
    digest = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1048576), b''):
            digest.update(block)
    return digest.hexdigest()


def fragment_sha(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True,
                                    separators=(',', ':')).encode()).hexdigest()


def interval(value):
    if value['finite'] is not True:
        raise ValueError('nonfinite saved interval')
    lo, hi = F(value['lower_rational']), F(value['upper_rational'])
    if lo > hi:
        raise ValueError('reversed saved interval')
    return lo, hi


def pair_record(lo, hi):
    return {'finite': True, 'lower_rational': str(lo), 'upper_rational': str(hi)}


def inputs_and_source():
    if not PINNED:
        raise ValueError('unfinished protocol pins')
    inputs = dict(PINNED)
    for name, digest in inputs.items():
        if sha(ROOT / name) != digest:
            raise ValueError('changed direct input: ' + name)
    source = json.loads((ROOT / SOURCE).read_text())
    audit = json.loads((ROOT / AUDIT).read_text())
    if not (audit['status'] == 'passed' and audit['source_path'] == SOURCE
            and audit['source_sha256'] == inputs[SOURCE]
            and audit['checker_sha256'] == inputs[CHECKER]
            and audit['canonical_references_checked'] == 4):
        raise ValueError('saved reference audit association failed')
    if not (source['status'] == 'complete fixed diagnostic'
            and source['changed_inputs'] == []
            and source['precision_bits'] == 256):
        raise ValueError('source reference certificate incomplete')
    for name, digest in source['input_sha256'].items():
        if name in inputs and inputs[name] != digest:
            raise ValueError('conflicting inherited pin: ' + name)
        if sha(ROOT / name) != digest:
            raise ValueError('changed inherited reference input: ' + name)
        inputs[name] = digest
    expected = list(itertools.product((0, 1), repeat=2))
    if [(c['beta'], c['epsilon']) for c in source['cases']] != expected:
        raise ValueError('wrong four-case reference inventory')
    own = Path(__file__).resolve().relative_to(ROOT).as_posix()
    inputs[own] = sha(ROOT / own)
    return inputs, source


def affine_support(force, center, bounds):
    """Outward exact-rational max of the two endpoint products; no zero cap."""
    fl, fh = interval(force)
    cl, ch = interval(center)
    records = []
    for target in bounds:
        dl, dh = target - ch, target - cl
        corners = [x * y for x in (fl, fh) for y in (dl, dh)]
        records.append({'target_rational': str(target),
                        'displacement': pair_record(dl, dh),
                        'product_corners_rational': list(map(str, corners)),
                        'value': pair_record(min(corners), max(corners))})
    lo = max(interval(r['value'])[0] for r in records)
    hi = max(interval(r['value'])[1] for r in records)
    return {'force': force, 'center': center,
            'target_interval_rational': list(map(str, bounds)),
            'endpoint_products': records, 'value': pair_record(lo, hi),
            'truncated_at_zero': False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    inputs, source = inputs_and_source()
    # Only the direct outward primitive library is loaded, after all bindings.
    from flint import acb, arb, ctx
    ctx.prec = 256
    pi, ii = arb.pi(), acb(0, 1)
    counts = {'saved_reference_cases': 0, 'primitive_evaluations': 0,
              'log_derivative_evaluations': 0, 'branch_bounds': 0,
              'reference_proposals': 0, 'root_solves': 0,
              'reference_transport_evaluations': 0, 'target_optimizations': 0,
              'subdivisions': 0, 'precision_retries': 0,
              'terminal_private_action_evaluations': 0,
              'finite_quantum_source_evaluations': 0}

    def rat(value):
        value = F(value)
        return arb(value.numerator) / arb(value.denominator)

    def ends(value):
        if not value.is_finite():
            raise ArithmeticError('nonfinite outward value')
        return F(str(value.lower().fmpq())), F(str(value.upper().fmpq()))

    def record(value):
        return pair_record(*ends(value))

    def crecord(value):
        return {'real': record(value.real), 'imag': record(value.imag)}

    def ball(saved):
        lo, hi = interval(saved)
        result = arb(rat((lo + hi) / 2), rat((hi - lo) / 2).upper())
        actual_lo, actual_hi = ends(result)
        if not actual_lo <= lo <= hi <= actual_hi:
            raise ArithmeticError('outward coordinate conversion failed')
        return result

    def read_coordinate(saved):
        return acb(ball(saved['real']), ball(saved['imag']))

    def original_values(z):
        if not (z.is_finite() and z.real > 0 and z.real < 1):
            raise ArithmeticError('argument outside original regular strip')
        exponential = (-2 * pi * ii * z).exp()
        if not (exponential.imag > 0 or exponential.imag < 0 or exponential.real < 1):
            raise ArithmeticError('original dilogarithm cut not separated')
        counts['primitive_evaluations'] += 1
        g = (exponential.polylog(2) - pi * pi / 6) / (2 * pi * ii)
        log_argument = 1 - exponential
        if not (log_argument.imag > 0 or log_argument.imag < 0 or log_argument.real > 0):
            raise ArithmeticError('original logarithm cut not separated')
        counts['log_derivative_evaluations'] += 1
        gp = log_argument.log()
        if not (g.is_finite() and gp.is_finite()):
            raise ArithmeticError('nonfinite original primitive')
        return g, gp, {'argument': crecord(z), 'exponential': crecord(exponential),
                       'g': crecord(g), 'g_prime': crecord(gp),
                       'original_strip_and_cuts_verified': True}

    cases = []
    for source_index, saved in enumerate(source['cases']):
        beta, epsilon = saved['beta'], saved['epsilon']
        row = {'source_index': source_index, 'beta': beta, 'epsilon': epsilon,
               'source_case_sha256': fragment_sha(saved), 'status': 'inconclusive',
               'branches': [], 'finite_word_realization_claimed': False}
        try:
            counts['saved_reference_cases'] += 1
            if not (saved['canonical_reference_certified'] is True
                    and saved['status'] == 'canonical reference and lower tests certified'
                    and list(map(F, saved['outside_coordinate'])) == list(CENTERS[beta])):
                raise ValueError('saved canonical case not certified or wrongly associated')
            q = {name: read_coordinate(saved['coordinate_enclosures'][name]) for name in NAMES}
            row['saved_coordinate_enclosures'] = saved['coordinate_enclosures']
            row['actual_coordinate_enclosures'] = {name: crecord(z) for name, z in q.items()}
            row['outside_coordinate_rational'] = saved['outside_coordinate']
            # Pointwise reference enclosures stay in the exact strong images.
            for name in ('a', 's'):
                if not (q[name].real > rat(F(6, 25)) and q[name].real < rat(F(9, 25))
                        and q[name].imag > rat(F(-51, 500))
                        and q[name].imag < rat(F(-1, 1000))):
                    raise ValueError('saved ordinary coordinate left its certified strong image')
            t_bounds = ((F(139, 500), F(391, 1000), F(-9, 125), F(21, 1000))
                        if epsilon == 0 else
                        (F(123, 500), F(7, 20), F(-27, 250), F(-1, 50)))
            if not (q['t'].real > rat(t_bounds[0]) and q['t'].real < rat(t_bounds[1])
                    and q['t'].imag > rat(t_bounds[2]) and q['t'].imag < rat(t_bounds[3])):
                raise ValueError('saved terminal index left its certified strong image')
            row['ordinary_label_reduction_height_verified'] = (
                F(-39, 500) <= CENTERS[beta][1] <= F(21, 1000))
            delta = rat(HEIGHT) - q['a'].imag
            ah = acb(q['a'].real, rat(HEIGHT))
            arguments = {'a': q['a'], 'sa': q['s'] + q['a'], 'ta': q['t'] + q['a'],
                         'aH': ah, 'saH': q['s'] + ah, 'taH': q['t'] + ah}
            values = {name: original_values(arguments[name]) for name in ARGUMENT_NAMES}
            row['original_values'] = {name: values[name][2] for name in ARGUMENT_NAMES}
            row['height_rational'] = str(HEIGHT)
            row['delta'] = record(delta)
            centered = {name: values[name + 'H'][0] - values[name][0]
                        - ii * delta * values[name][1] for name in ('a', 'sa', 'ta')}
            increments = {name: values[name + 'H'][1] - values[name][1]
                          for name in ('a', 'sa', 'ta')}
            W = (centered['sa'] + centered['ta'] - 3 * centered['a']).real
            force_s = increments['sa'].real
            force_t = increments['ta'].real - 2 * pi * delta
            row['centered_primitives'] = {name: crecord(z) for name, z in centered.items()}
            row['log_increments'] = {name: crecord(z) for name, z in increments.items()}
            row['stationary_height_cost'] = record(W)
            row['force_s'] = record(force_s)
            row['force_t'] = record(force_t)
            row['force_signs_theoretically_proved'] = True
            row['outward_force_signs_verified'] = (
                ends(force_s)[0] > 0 and ends(force_t)[1] < 0)
            for nu in (1, 0):
                target = (F(11, 50), F(9, 20)) if nu == 1 else (F(2, 5), F(9, 20))
                T = W + (1 - nu) * values['aH'][0].real - 2 * pi * nu * rat(HEIGHT)
                force_a = (increments['sa'] + increments['ta'] - 3 * increments['a']
                           + (1 - nu) * values['aH'][1]).real
                supports = {
                    's': affine_support(record(force_s), record(q['s'].real), (F(1, 8), F(1, 2))),
                    'a': affine_support(record(force_a), record(q['a'].real), target),
                    't': affine_support(record(force_t), record(q['t'].real), (F(3, 20), F(1, 2))),
                }
                t_record = record(T)
                upper = interval(t_record)[1] + sum(interval(v['value'])[1] for v in supports.values())
                row['branches'].append({
                    'nu': nu, 'label': 'factorial' if nu else 'forced',
                    'selected_target_interval_rational': list(map(str, target)),
                    'lifted_reference_value': t_record, 'force_a': record(force_a),
                    'supports': supports, 'total_upper_rational': str(upper),
                    'main_profile_negative_proved': upper < 0,
                    'factorial_positive_trial_proved': nu == 1 and interval(t_record)[0] > 0,
                    'forced_trial_lower_bound_claimed': False,
                    'whole_source_sign_claimed': False,
                })
                counts['branch_bounds'] += 1
            row['status'] = 'both main-current bounds enclosed'
        except Exception as error:
            row['error'] = type(error).__name__ + ': ' + str(error)
        cases.append(row)
        print(json.dumps({'beta': beta, 'epsilon': epsilon, 'status': row['status'],
                          'upper_bounds': [v['total_upper_rational'] for v in row['branches']],
                          'error': row.get('error')}), flush=True)
    changed = [name for name, digest in inputs.items() if sha(ROOT / name) != digest]
    complete = (not changed and len(cases) == 4 and counts['branch_bounds'] == 8
                and all(row['status'] == 'both main-current bounds enclosed' for row in cases))
    result = {'status': 'complete fixed diagnostic' if complete else 'inconclusive fixed diagnostic',
              'height_rational': str(HEIGHT), 'precision_bits': 256, 'pi': record(pi),
              'counts': counts, 'cases': cases, 'input_sha256': inputs, 'changed_inputs': changed,
              'all_eight_main_bounds_negative': complete and all(
                  branch['main_profile_negative_proved'] for row in cases for branch in row['branches']),
              'whole_source_sign_claimed': False, 'uniform_reference_domain_claimed': False,
              'finite_word_realization_claimed': False, 'complete_54_profile_pass_performed': False}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open('x') as stream:
        stream.write(json.dumps(result, indent=2) + '\n')
    print(json.dumps({'status': result['status'], 'record_sha256': sha(args.output),
                      'all_eight_main_bounds_negative': result['all_eight_main_bounds_negative']}), flush=True)


if __name__ == '__main__':
    main()
