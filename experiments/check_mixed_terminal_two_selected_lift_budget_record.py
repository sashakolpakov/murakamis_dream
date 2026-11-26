#!/usr/bin/env python3
"""Fixed stdlib-only audit of the saved two-selected lift budgets.

An unset source hash prevents execution. No analytic/provider/gain module is
imported; square-root witnesses are verified only by exact integer squaring.
"""
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SOURCE = 'repro/results/research-mixed-terminal-two-selected-lift-budgets.json.gz'
DRIVER = 'experiments/evaluate_mixed_terminal_two_selected_lift_budgets.py'
PROTOCOL = 'notes/research_mixed_terminal_two_selected_lift_budget_protocol.md'
PROOF = 'notes/research_mixed_terminal_two_selected_lift_budget_saved_check.md'
PROJECTION = 'repro/results/research-mixed-terminal-two-selected-reference-projection.json'
PROJECTOR = 'experiments/extract_mixed_terminal_two_selected_references.py'
PROJECTION_PROOF = 'notes/research_mixed_terminal_two_selected_reference_bank_transfer.md'
TERMINAL = 'repro/results/research-mixed-terminal-real-transform-cut-saved-audit.json'
TERMINAL_CHECKER = 'experiments/check_mixed_terminal_real_transform_cut_record.py'
PINNED = {
    SOURCE: '55d8252d1a34bb6ad514cdc77c43376c7b4cbc42fd76617b9b21ef1868c8024d',
    DRIVER: 'a0a18de1a523b61cbd197b18e385ee562187da96a76810924f83c2e287661cf8',
    PROTOCOL: 'ed08fa18c69c0265a3509e7730b068dc57cad6495b64802841d53a551677b322',
    PROOF: '00b0b1225c327b3fcd0d07fa00603812dc3dacfc55d837e5269a5069c04b63f9',
    PROJECTION: '98a1e6d33c58074fffface6b3da93cbd4d842f5006a2d2f032c94a73ee81c198',
    PROJECTOR: '32121f3a82827de99c6e762fd821b9343d1fab6d751fc4eeffe45500bb1cde2d',
    PROJECTION_PROOF: 'eaf351d6f4bab35fbdec81b6642ba72b5777b582caafced26788d31908bf1223',
    TERMINAL: '29d1edc0a516e44ceac16f3c9fe9868bfee0e8c3268134819f05bbd21067306e',
    TERMINAL_CHECKER: '116f9b00d0580e96273c58a4079623796591d80afdb99d25cbd8b1c1a3c231f7',
    'notes/research_signed_cubic_gain_with_uncertain_center.md':
        '1a890d4c06ff37a397e3e7732f2d6f5b952f9ffa74858f31a5c837ad871bae6c',
    'notes/research_mixed_terminal_two_selected_budget_composition.md':
        '002cf3eb25520f24745a36ce52ead2105793a6c814796752b6d4fb9a3177a4c8',
    'notes/research_mixed_terminal_shared_index_gain_cancellation.md':
        '8313c7dcca46ec7c95c8ed5e7f34e5eb59400615d8633a197e5429e2dbb68218',
}
H, HALF, ZERO = F(1, 100), F(1, 2), (F(0), F(0))
NAMES = ('r', 'b', 's', 'a')
ARGUMENTS = ('b', 'rb', 'sb', 'sa')
CHARTS = {'k3_circle_left', 'k3_circle_right', 'k3_lower_chord',
          'k3_upper_chord', 'k3_oblique_chord', 'k4_circle_left',
          'k4_circle_right', 'k4_lower_chord', 'k4_upper_chord'}


def need(condition, message):
    if not condition:
        raise ValueError(message)


def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1048576), b''):
            h.update(block)
    return h.hexdigest()


def canonical(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True,
        separators=(',', ':')).encode()).hexdigest()


def load(path):
    p = ROOT/path
    with (gzip.open(p, 'rt', encoding='utf-8') if p.suffix == '.gz' else p.open()) as stream:
        return json.load(stream)


def interval(value):
    need(value.get('finite') is True, 'nonfinite saved interval')
    lo, hi = F(value['lower_rational']), F(value['upper_rational'])
    need(lo <= hi, 'reversed saved interval')
    return lo, hi


def same_interval(record, expected, context):
    got = interval(record)
    need(got == expected, context+': '+str(got)+' != '+str(expected))


def encloses(outer, inner):
    return outer[0] <= inner[0] <= inner[1] <= outer[1]


def add(x, y):
    return x[0]+y[0], x[1]+y[1]


def scale(x, q):
    return (q*x[0], q*x[1]) if q >= 0 else (q*x[1], q*x[0])


def subtract(x, y):
    return x[0]-y[1], x[1]-y[0]


def product(x, y):
    candidates = [a*b for a in x for b in y]
    return min(candidates), max(candidates)


def point(q):
    return q, q


def horner(coefficients, x):
    out = ZERO
    for coefficient in reversed(coefficients):
        out = add(product(out, x), point(coefficient))
    return out


def dyadic_sqrt_witness(record, radicand):
    lo, hi = interval(record)
    unit = F(1, 2**240)
    need(0 <= lo <= hi, 'negative square-root endpoint')
    need((lo/unit).denominator == 1, 'sqrt lower not a 240-bit dyadic')
    need(lo*lo <= radicand <= hi*hi, 'sqrt endpoint squares do not enclose discriminant')
    if lo*lo == radicand:
        need(hi == lo, 'exact dyadic root must be a singleton')
    else:
        need(hi == lo+unit and radicand < hi*hi,
             'sqrt interval is not the prescribed adjacent dyadic enclosure')
    return lo, hi


def check_gain(record, q, center, target, K, counters):
    """Verify the mandatory saved candidate set, without selecting a new gain."""
    counters['signed_gains'] += 1
    A, B = center
    L, R = target
    need(F('.18') <= A <= B <= HALF and F('.18') <= L <= R <= HALF,
         'cubic domain')
    need(K > 0 and F(record['force_rational']) == q
         and F(record['K_rational']) == K, 'gain force/coefficient association')
    same_interval(record['center'], center, 'gain center')
    same_interval(record['target'], target, 'gain target')
    need(record['square_root_bits'] == 240 and record['zero_cap_used'] is False,
         'gain precision or zero truncation')
    # Expand q(x-c)-K B_h(x,c) independently on its two boundary edges.
    coefficients = [
        (-q*B-K*B*B/4+K*B**3/3, q+K*(B-B*B)/2, -K/4, K/6),
        (q*R-K*R*R/4+K*R**3/6, -q+K*R/2, -K/4-K*R/2, K/3),
    ]
    discriminants = [(HALF-B)**2-2*q/K, (R-HALF)**2+4*q/K]
    need(len(record['edges']) == 2, 'gain must contain both edges')
    upper_values = []
    for edge_index, edge in enumerate(record['edges']):
        domain = target if edge_index == 0 else center
        fixed = B if edge_index == 0 else R
        label = 'center_upper' if edge_index == 0 else 'target_upper'
        need(edge['fixed'] == label and F(edge['fixed_rational']) == fixed, 'edge identity')
        same_interval(edge['domain'], domain, 'edge domain')
        coeff = tuple(map(F, edge['coefficients_rational']))
        need(coeff == coefficients[edge_index], 'expanded edge polynomial')
        disc = discriminants[edge_index]
        need(F(edge['discriminant_rational']) == disc, 'critical discriminant')
        expected = [('left_endpoint', point(domain[0]), None),
                    ('right_endpoint', point(domain[1]), None)]
        discarded = []
        if disc < 0:
            need(edge['square_root'] is None, 'nonreal roots have square-root witness')
            discarded = ['negative discriminant: both roots nonreal']
        else:
            counters['gain_square_roots'] += 1
            root = dyadic_sqrt_witness(edge['square_root'], disc)
            for sign in (-1, 1):
                raw = add(point(HALF), scale(root, sign)) if edge_index == 0 else \
                    scale(add(point(R+HALF), scale(root, sign)), HALF)
                clipped = max(domain[0], raw[0]), min(domain[1], raw[1])
                if clipped[0] > clipped[1]:
                    discarded.append((sign, raw))
                else:
                    expected.append(('critical_minus' if sign == -1 else 'critical_plus', clipped, raw))
        actual_discarded = edge['discarded_roots']
        need(len(actual_discarded) == len(discarded), 'missing/extra discarded critical root')
        for got, wanted in zip(actual_discarded, discarded):
            if isinstance(wanted, str):
                need(got == wanted, 'wrong nonreal-root reason')
            else:
                sign, raw = wanted
                need(got['sign'] == sign and got['reason'] == 'whole root enclosure misses edge',
                     'wrong disjoint-root reason')
                same_interval(got['untruncated'], raw, 'discarded root interval')
        need(len(edge['candidates']) == len(expected), 'missing/extra edge endpoint or critical root')
        for candidate, (kind, argument, raw) in zip(edge['candidates'], expected):
            counters['gain_candidates'] += 1
            need(candidate['kind'] == kind, 'candidate ordering/identity')
            same_interval(candidate['argument'], argument, 'candidate argument')
            if raw is None:
                need('unclipped_root' not in candidate, 'endpoint marked as root')
            else:
                same_interval(candidate['unclipped_root'], raw, 'unclipped root')
            value = horner(coeff, argument)
            same_interval(candidate['value'], value, 'candidate rational Horner enclosure')
            upper_values.append(value[1])
    upper = max(upper_values)
    need(F(record['upper_rational']) == upper, 'signed gain maximum')
    return upper


def check_projection(projection):
    need(projection['status'] == 'passed' and projection['changed_inputs'] == [], 'projection did not pass')
    need(projection['proof_path'] == PROJECTION_PROOF
         and projection['proof_sha256'] == PINNED[PROJECTION_PROOF], 'projection proof association')
    need(projection['checker_path'] == PROJECTOR
         and projection['checker_sha256'] == PINNED[PROJECTOR], 'projector association')
    need(projection['all_boundaries_complete'] is True
         and projection['reference_counts'] == {'0': 637, '1': 646}, 'projection coverage flags')
    need(projection['coordinate_mapping_new_to_old'] == {'r': 'b', 'b': 'v', 's': 'z', 'a': 'u'},
         'original coordinate permutation')
    need([c['epsilon'] for c in projection['cases']] == [0, 1], 'projection case inventory')
    need(len(projection['coverage']) == 18, 'projection chart count')
    seen = set()
    for tree in projection['coverage']:
        key = tree['epsilon'], tree['chart']
        need(key not in seen and key[0] in (0, 1) and key[1] in CHARTS, 'duplicate/unknown tree')
        seen.add(key)
        addresses = tree['addresses']
        need(addresses == sorted(set(addresses)), 'tree addresses not ordered and unique')
        need(all(not set(a)-{'0', '1'} for a in addresses), 'invalid binary address')
        need(not any(b.startswith(a) for a, b in zip(addresses, addresses[1:])), 'non-prefix-free tree')
        need(sum((F(1, 2**len(a)) for a in addresses), F(0)) == 1, 'incomplete tree mass')
        need(tree['leaf_count'] == len(addresses) and F(tree['normalized_mass_rational']) == 1,
             'tree summary mismatch')
    need(seen == {(e, c) for e in (0, 1) for c in CHARTS}, 'missing chart case')
    refs = projection['reference_associations']
    leaves = projection['terminal_geometry']
    need(len(refs) == 1283 and len(leaves) == 1394, 'projection terminal/reference counts')
    keys = {(r['epsilon'], r['source_node_index']): r for r in refs}
    need(len(keys) == len(refs), 'duplicate projected reference')
    associated, leaf_keys, exclusions = set(), set(), {0: 0, 1: 0}
    for leaf in leaves:
        tree_key = leaf['epsilon'], leaf['chart'], leaf['address']
        need(tree_key not in leaf_keys, 'duplicate terminal geometry')
        leaf_keys.add(tree_key)
        need(leaf['beta'] == 1, 'unselected beta in projection')
        if leaf['status'] == 'accepted boundary estimate':
            key = leaf['epsilon'], leaf['source_node_index']
            need(key in keys and key not in associated, 'reference/geometry association')
            associated.add(key)
            for field in ('chart', 'address', 'external_domain', 'parameter_interval',
                          'external_coordinate_box', 'source_node_canonical_sha256'):
                need(keys[key][field] == leaf[field], 'reference geometry field: '+field)
        else:
            need(leaf['status'] == 'excluded', 'reference exclusion or unresolved leaf')
            witness = leaf['source_exclusion']
            need(witness['criterion'] in ('outside_typed_disk', 'below_lower_height',
                 'above_upper_height', 'above_oblique_halfplane'), 'non-geometric exclusion')
            need(F(witness['strict_margin_rational']) > 0, 'non-strict geometric exclusion')
            exclusions[leaf['epsilon']] += 1
    need(associated == set(keys) and exclusions == {0: 55, 1: 56}, 'selected inventory mismatch')
    need(leaf_keys == {(t['epsilon'], t['chart'], a) for t in projection['coverage']
                      for a in t['addresses']}, 'geometry/tree inventory mismatch')
    for case in projection['cases']:
        need(projection['case_canonical_sha256'][str(case['epsilon'])] == canonical(case),
             'projection case canonical hash')


def check_case(case, projected, pi, half_lower, counters, output):
    eps = projected['epsilon']
    need(case['epsilon'] == eps and case['status'] == 'enclosed both added budgets', 'incomplete case')
    need(case['projection_case_canonical_sha256'] == canonical(projected), 'case projection hash')
    need(case['coordinates'] == projected['coordinates'], 'coordinate projection equality')
    need(set(case['coordinates']) == set(NAMES), 'coordinate inventory')
    coords = {n: (interval(case['coordinates'][n]['real']),
                  interval(case['coordinates'][n]['imag'])) for n in NAMES}
    guards = {}
    for n, (x, y) in coords.items():
        guards[n+'_real'] = F('.24') <= x[0] <= x[1] <= F('.36')
        guards[n+'_height'] = F('-.102') <= y[0] <= y[1] <= F('-.001')
    guards.update(forced_targets_right_of_centers=coords['b'][0][1] < F('.4'),
                  shared_reflection=coords['s'][0][1] <= F('.36'),
                  positive_displacements=max(coords[n][1][1] for n in ('a', 'b')) < H)
    need(all(guards.values()) and case['domain_guards'] == guards, 'reference domain guards')
    need(len(case['slabs']) == len(projected['slabs']) == 16, 'slab count')
    means, vertical = {key: ZERO for key in ARGUMENTS}, ZERO
    for j, (slab, original) in enumerate(zip(case['slabs'], projected['slabs'])):
        counters['slabs'] += 1
        need(slab['index'] == original['index'] == j, 'slab index')
        theta = (F(j, 16), F(j+1, 16))
        need(tuple(map(F, slab['theta_rational'])) == tuple(map(F, original['theta_rational'])) == theta,
             'theta slab endpoints')
        need(slab['projection_slab_canonical_sha256'] == canonical(original), 'slab projection hash')
        w, v = F(1, 16), F(31-2*j, 512)
        need(F(slab['weight_rational']) == w and F(slab['weighted_rational']) == v, 'integral weights')
        need(set(slab['arguments']) == set(original['arguments']) == set(ARGUMENTS), 'argument inventory')
        real = {}
        for key in ARGUMENTS:
            saved, projected_argument = slab['arguments'][key], original['arguments'][key]
            x, y = interval(projected_argument['real']), interval(projected_argument['imag'])
            same_interval(saved['real'], x, 'projected argument real')
            same_interval(saved['imag'], y, 'projected argument height')
            ox, oy = interval(saved['outward_argument']['real']), interval(saved['outward_argument']['imag'])
            need(encloses(ox, x) and encloses(oy, y) and 0 < ox[0] <= ox[1] < 1,
                 'outward cotangent argument/domain')
            real[key] = interval(saved['cotangent']['real'])
            imaginary = interval(saved['cotangent']['imag'])
            contribution = scale(imaginary, w)
            same_interval(slab['mean_contributions'][key], contribution, 'weighted imaginary cotangent')
            means[key] = add(means[key], contribution)
            counters['cotangent'] += 1
        contribution = scale(subtract(subtract(scale(real['b'], F(3)), real['rb']), real['sb']), v)
        same_interval(slab['vertical_contribution'], contribution, 'weighted vertical cotangent')
        vertical = add(vertical, contribution)
    for key in ARGUMENTS:
        same_interval(case['normalized_means'][key], means[key], 'normalized mean')
    same_interval(case['normalized_vertical'], vertical, 'normalized vertical')
    db, da = subtract(point(H), coords['b'][1]), subtract(point(H), coords['a'][1])
    kappa = product(pi, db)
    vp = max(F(0), vertical[1])
    lower_v = pi[0]*da[0]*max(F(0), 1-means['sa'][1])
    ds, bu = HALF-coords['s'][0][0], coords['b'][0][1]
    need(kappa[0] > 0 and da[0] > 0, 'positive lift guard')
    lift = case['lift_data']
    for name, value in (('delta_b', db), ('delta_a', da), ('kappa', kappa)):
        same_interval(lift[name], value, 'lift '+name)
    for name, value in (('V_positive_upper_rational', vp), ('v_lower_rational', lower_v),
                        ('shared_s_displacement_upper_rational', ds)):
        need(F(lift[name]) == value, 'lift scalar '+name)
    endpoint = case['forced_endpoint']
    need(F(endpoint['B_upper_rational']) == bu and F(endpoint['q_half_lower_rational']) == half_lower
         and F(endpoint['chord_factor_rational']) == (HALF-bu)/2, 'forced endpoint association')
    # These are reviewed analytic witnesses, not independent analytic evaluations.
    interval(endpoint['cosine_argument'])
    interval(endpoint['cosine'])
    need(interval(endpoint['modulus_square'])[0] > 0, 'forced logarithm guard')
    qe = interval(endpoint['q_end'])
    need([b['mu'] for b in case['branches']] == [1, 0], 'branch inventory')
    summaries = []
    for branch in case['branches']:
        mu = branch['mu']
        target = (F('.22'), F('.45')) if mu else (F('.4'), F('.45'))
        same_interval(branch['target'], target, 'full branch target')
        names = ['kappa', 'I_b', 'I_rb', 'I_sb']+([] if mu else ['q_end'])
        boxes = [kappa, means['b'], means['rb'], means['sb']]+([] if mu else [qe])
        need(branch['variable_order'] == names and len(branch['variable_intervals']) == len(boxes),
             'vertex variable inventory')
        for saved, box in zip(branch['variable_intervals'], boxes):
            same_interval(saved, box, 'vertex variable interval')
        nv = 2**len(boxes)
        need(len(branch['vertices']) == nv, 'vertex count')
        uppers, flags_all = [], []
        for index, vertex in enumerate(branch['vertices']):
            flags = [(index >> (len(boxes)-1-j)) & 1 for j in range(len(boxes))]
            need(vertex['flags'] == flags, 'vertex binary ordering/completeness')
            values = [box[flag] for box, flag in zip(boxes, flags)]
            need(list(map(F, vertex['values_rational'])) == values, 'vertex endpoint values')
            k, ib, irb, isb = values[:4]
            r_force = k*(1-irb)
            bf = k*(3*ib-irb-isb-1)
            b_force = bf+(F(0) if mu else values[4])
            need({key: F(value) for key, value in vertex['forces_rational'].items()}
                 == {'r': r_force, 'b_factorial': bf, 'b': b_force}, 'vertex forces')
            w = k*k*vp/pi[0]
            selected = -2*pi[0]*H if mu else -(HALF-bu)*(values[4]+half_lower)/2
            expression = k*(1+isb)-2*lower_v
            debit = ds*max(F(0), expression)
            for name, value in (('vertical_upper_rational', w), ('selected_trial_upper_rational', selected),
                                ('shared_expression_rational', expression), ('shared_debit_upper_rational', debit)):
                need(F(vertex[name]) == value, 'vertex component '+name)
            need(set(vertex['gains']) == {'r', 'b'}, 'gain node inventory')
            gr = check_gain(vertex['gains']['r'], r_force, coords['r'][0], (F('.22'), HALF), F(88, 5), counters)
            gb = check_gain(vertex['gains']['b'], b_force, coords['b'][0], target, F((mu+1)*49, 5), counters)
            upper = w+selected+debit+gr+gb
            need(F(vertex['upper_rational']) == upper, 'vertex total')
            uppers.append(upper)
            flags_all.append(flags)
            counters['vertices'] += 1
            output['vertices'].append({'epsilon': eps, 'mu': mu, 'flags': flags,
                'r_gain_canonical_sha256': canonical(vertex['gains']['r']),
                'b_gain_canonical_sha256': canonical(vertex['gains']['b']),
                'recombined_upper_rational': str(upper)})
        worst = max(uppers)
        need(F(branch['upper_rational']) == worst and branch['nonpositive'] == (worst <= 0), 'budget maximum/sign')
        maximizing = [flags for flags, value in zip(flags_all, uppers) if value == worst]
        need(branch['maximizing_flags'] == maximizing, 'maximizing vertex inventory')
        summaries.append({'mu': mu, 'upper_rational': str(worst), 'nonpositive': worst <= 0,
                          'strictly_below_minus_1_104': worst < -F(1, 104),
                          'maximizing_flags': maximizing})
    return {'epsilon': eps, 'projection_case_canonical_sha256': canonical(projected), 'branches': summaries}


def audit(source, projection, terminal, output):
    need(source['schema'] == 'mixed-terminal-two-selected-lift-budgets-v1'
         and source['status'] == 'completed fixed protocol', 'incomplete source status/schema')
    need(source['changed_inputs'] == [] and source['unvisited_cases'] == [], 'source changed or unvisited cases')
    need(source['precision_bits'] == 256 and source['square_root_bits'] == 240 and source['fallback'] == 'none',
         'source fixed precision/protocol')
    need(source['proof_path'] == PROTOCOL and source['proof_sha256'] == PINNED[PROTOCOL]
         and source['source_path'] == PROJECTION and source['source_sha256'] == PINNED[PROJECTION]
         and source['checker_sha256'] == PINNED[PROJECTOR], 'source provenance')
    check_projection(projection)
    need(source['projection_case_hashes'] == [canonical(c) for c in projection['cases']], 'projection hashes')
    need(source['reference_counts'] == projection['reference_counts']
         and source['all_boundaries_complete'] is True, 'source reference coverage')
    need(terminal['status'] == 'passed exact saved direct-cut and all-profile audit'
         and terminal['changed_inputs'] == [], 'terminal audit did not pass')
    need(terminal['all_27_terminal_profile_bounds_paid'] is True
         and terminal['paid_real_entropy_branches'] == 36
         and F(terminal['complete_profile_raw_floor_rational']) == F(1, 2600), 'terminal comparison premise')
    need(terminal['input_sha256'][TERMINAL_CHECKER] == PINNED[TERMINAL_CHECKER], 'terminal auditor binding')
    constants = source['constants']
    pi = interval(constants['pi'])
    need(pi[0] > 0, 'pi positivity')
    interval(constants['exponential_argument'])
    need(interval(constants['exp_2piH'])[0] > 0 and interval(constants['half_log_argument'])[0] > 0,
         'exponential/half logarithm guard')
    half_lower = interval(constants['q_half'])[0]
    counters = dict(cotangent=0, slabs=0, vertices=0, signed_gains=0, gain_candidates=0, gain_square_roots=0)
    need([c['epsilon'] for c in source['cases']] == [0, 1], 'source case inventory')
    for case, projected in zip(source['cases'], projection['cases']):
        output['active_case'] = case['epsilon']
        output['cases'].append(check_case(case, projected, pi, half_lower, counters, output))
        output['active_case'] = None
    expected = dict(pi=1, exponential=1, cosine=2, logarithm=3, cases=2,
                    reference_calls=0, root_proposals=0, source_evaluations=0,
                    original_primitives=0, optimizers=0, parameter_subdivisions=0, retries=0, **counters)
    need(source['counts'] == expected, 'source call/candidate inventory')
    need(counters['cotangent'] == 128 and counters['slabs'] == 32 and counters['vertices'] == 96
         and counters['signed_gains'] == 192 and counters['gain_candidates'] <= 1536
         and counters['gain_square_roots'] <= 384, 'fixed arithmetic inventory')
    worst = max(F(b['upper_rational']) for c in output['cases'] for b in c['branches'])
    success = worst <= 0
    stronger = worst < -F(1, 104)
    need(F(1, 104)+F(1, 2600) == F(1, 100), 'stronger gap arithmetic')
    need(F(source['worst_budget_upper_rational']) == worst and source['all_four_budgets_enclosed'] is True
         and source['all_added_budgets_nonpositive'] == success, 'global sign/max flags')
    need(source['two_selected_terminal_raw_gap_rational'] == ('1/2600' if success else None)
         and source['finite_source_gap_rational'] == ('1/5200' if success else None), 'conditional local gaps')
    need(source['whole_word_theorem_proved'] is False and source['knot_volume_theorem_proved'] is False,
         'source scope exceeds local comparison')
    output.update(verified_source_counts=expected, worst_budget_upper_rational=str(worst),
        all_added_budgets_nonpositive=success,
        two_selected_terminal_raw_gap_rational='1/2600' if success else None,
        finite_source_gap_rational='1/5200' if success else None,
        inherited_terminal_profile_floor_rational='1/2600',
        all_added_budgets_strictly_below_minus_1_104=stronger,
        enhanced_terminal_raw_gap_rational='1/100' if stronger else None,
        enhanced_finite_source_gap_rational='1/200' if stronger else None)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    if hasattr(sys, 'set_int_max_str_digits'):
        sys.set_int_max_str_digits(0)
    bindings = {}
    own = Path(__file__).resolve().relative_to(ROOT).as_posix()
    output = dict(status='not completed', source=SOURCE, source_sha256=PINNED[SOURCE],
        checker=own, checker_sha256=sha(ROOT/own), proof=PROOF, cases=[], vertices=[], active_case=None,
        all_added_budgets_nonpositive=False, input_sha256=bindings, changed_inputs=[],
        analytic_evaluations=0, root_evaluations=0, new_gain_evaluations=0,
        analytic_enclosures_recomputed=False, whole_word_theorem_proved=False, knot_volume_theorem_proved=False)
    try:
        need(all(isinstance(h, str) and len(h) == 64 for h in PINNED.values()), 'source-result pin not finalized')
        def bind(name, digest):
            need(isinstance(digest, str) and len(digest) == 64, 'invalid binding '+name)
            need(name not in bindings or bindings[name] == digest, 'conflicting binding '+name)
            need(sha(ROOT/name) == digest, 'changed input '+name)
            bindings[name] = digest
        for name, digest in PINNED.items():
            bind(name, digest)
        bind(own, output['checker_sha256'])
        source, projection, terminal = load(SOURCE), load(PROJECTION), load(TERMINAL)
        for record in (source, projection, terminal):
            need(record['changed_inputs'] == [], 'inherited changed inputs')
            for name, digest in record['input_sha256'].items():
                bind(name, digest)
        for name in (DRIVER, PROTOCOL, PROJECTION, PROJECTOR, PROJECTION_PROOF, TERMINAL, TERMINAL_CHECKER):
            need(source['input_sha256'][name] == PINNED[name], 'missing direct source association '+name)
        audit(source, projection, terminal, output)
        output['status'] = 'passed exact saved two-lift arithmetic audit'
    except BaseException as exc:
        output['status'] = 'failed'
        output['error'] = {'type': type(exc).__name__, 'message': str(exc)}
    for name, digest in bindings.items():
        if not (ROOT/name).exists() or sha(ROOT/name) != digest:
            output['changed_inputs'].append(name)
    if output['changed_inputs']:
        output['status'] = 'failed'
        output['error'] = {'type': 'InputChanged', 'message': 'bound input changed during audit'}
    if output['status'] == 'failed':
        output['all_added_budgets_nonpositive'] = False
        output['two_selected_terminal_raw_gap_rational'] = None
        output['finite_source_gap_rational'] = None
        output['all_added_budgets_strictly_below_minus_1_104'] = False
        output['enhanced_terminal_raw_gap_rational'] = None
        output['enhanced_finite_source_gap_rational'] = None
    output['input_sha256'] = dict(sorted(bindings.items()))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open('x') as stream:
        json.dump(output, stream, sort_keys=True, separators=(',', ':'))
        stream.write('\n')
    print(json.dumps({'status': output['status'], 'completed_cases': len(output['cases']),
        'input_bindings': len(bindings), 'all_added_budgets_nonpositive': output['all_added_budgets_nonpositive'],
        'output_sha256': sha(args.output)}))
    return 0 if output['status'].startswith('passed') else 1


if __name__ == '__main__':
    raise SystemExit(main())
