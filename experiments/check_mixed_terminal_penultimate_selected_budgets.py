#!/usr/bin/env python3
"""Fixed saved-only penultimate-selection recombination; no analytic imports."""
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SOURCE = 'repro/results/research-mixed-terminal-two-selected-lift-budgets.json.gz'
SOURCE_DRIVER = 'experiments/evaluate_mixed_terminal_two_selected_lift_budgets.py'
AUDIT = 'repro/results/research-mixed-terminal-two-selected-lift-budgets-saved-audit.json'
AUDITOR = 'experiments/check_mixed_terminal_two_selected_lift_budget_record.py'
PROJECTION = 'repro/results/research-mixed-terminal-two-selected-reference-projection.json'
CRITERION = 'notes/research_mixed_terminal_penultimate_selected_criterion.md'
PROTOCOL = 'notes/research_mixed_terminal_penultimate_selected_evaluation.md'
PINNED = {
    SOURCE: '55d8252d1a34bb6ad514cdc77c43376c7b4cbc42fd76617b9b21ef1868c8024d',
    SOURCE_DRIVER: 'a0a18de1a523b61cbd197b18e385ee562187da96a76810924f83c2e287661cf8',
    AUDIT: '126b39c133170b668ab4e5ffe955a7064dd892521830a7c5b9c8e947226944be',
    AUDITOR: '4db86b157936cf53623f0416d7bfabbff25c1595dd996e5a2b6f053d67e87f5b',
    PROJECTION: '98a1e6d33c58074fffface6b3da93cbd4d842f5006a2d2f032c94a73ee81c198',
    CRITERION: 'e3a8f6523524f1a86fed53bea099bc632ba0f0cfb86869746c6041dc4e4762b8',
    PROTOCOL: 'b8d5d3d9bd8bddf822390fd7207d5624ece9adc38c2220c2dfa7903633f5d8e3',
    'notes/research_mixed_second_selected_four_profile_reduction.md':
        'd084b535d83a08e50c4baddc52249c8495d88cde65f8c81e04baff566560d25e',
    'repro/results/research-mixed-second-selected-outgoing-four-left-cut.json':
        'b391e2873a761e0f646f315b91e890822854309d00251141a36fd8960f3e691d',
    'notes/research_mixed_terminal_two_selected_reference_reconstruction.md':
        '2d81e3ee8e09c1cddf83a0b0579252d67f2b9a2ffd04f2e6b821dcf2b9d96f5a',
    'notes/research_mixed_terminal_two_selected_reference_bank_transfer.md':
        'eaf351d6f4bab35fbdec81b6642ba72b5777b582caafced26788d31908bf1223',
    'notes/research_mixed_plateau_window_concave_profiles.md':
        'ba03fd9804c63274b8015532d3c176a044e9b7f0bdd34d69331f420522c88d19',
    'notes/research_mixed_terminal_ordinary_label_completion.md':
        '592b37d691db0359d4440d6ebffb35591ca14f00f71f3f2bffcc27b72beeec3a',
    'notes/research_mixed_second_selected_outgoing_four_left_cut.md':
        'd980491147fc9e2edfbe2e69148e390064215bd37f08f8df565609fd7c4f9a50',
    'notes/research_mixed_second_selected_outgoing_four_half_row_completion.md':
        'ce795f3dbf2cab22244994fa7e881ec3017387e4515f138a41809bfedd72aa75',
    'notes/research_mixed_second_selected_outgoing_last_rows.md':
        'd634f87205e3273ba5845f8f9586df3fe1a197fae8eae765d010278ff1809c91',
    'notes/research_mixed_three_row_source_assembly.md':
        '947fe40bd6125a0bca0f984dc4dde6d55e478ecf0719911829bdb840ef34396c',
    'notes/research_mixed_terminal_full_input_index_barrier.md':
        '45ae03bf28a78df930fc8e7c97054ca40689630423a4d36c0009b6b0bb900ee2',
    'notes/research_mixed_second_selected_horizontal_concavity.md':
        'dac208b242a8dd24f1ce0c29e15775bd343554e0cb0141e2ad84c0fe64312ca8',
    'notes/research_mixed_first_four_next_four_endpoint_budget.md':
        '9a4e089fe3d69f746465ef366eb86ac086272d007d0e669aecc8bfc1340e8903',
    'notes/research_mixed_terminal_symmetric_pair_costs.md':
        'b4ee1a7bdde317edab0210b20cb8616913984c4f992d1cbed240f6092a8e593f',
    'notes/research_mixed_terminal_cubic_cost_and_response_bounds.md':
        'dfc3f415e742aa9c632707aea7c699bb2ccbdc054c08fc7ba640e943bcdaa741',
    'notes/research_mixed_terminal_two_selected_lift_budget_protocol.md':
        'ed08fa18c69c0265a3509e7730b068dc57cad6495b64802841d53a551677b322',
    'notes/research_mixed_terminal_shared_index_gain_cancellation.md':
        '8313c7dcca46ec7c95c8ed5e7f34e5eb59400615d8633a197e5429e2dbb68218',
}
HALF, LEFT, K = F(1, 2), F(11, 50), F(19)
H = F(1, 100)


def need(condition, message):
    if not condition:
        raise ValueError(message)


def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for chunk in iter(lambda: stream.read(1048576), b''):
            h.update(chunk)
    return h.hexdigest()


def canonical(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True,
        separators=(',', ':')).encode()).hexdigest()


def load(name):
    path = ROOT/name
    with (gzip.open(path, 'rt', encoding='utf-8') if path.suffix == '.gz'
          else path.open(encoding='utf-8')) as stream:
        return json.load(stream)


def interval(record):
    need(record.get('finite') is True, 'nonfinite saved interval')
    lo, hi = F(record['lower_rational']), F(record['upper_rational'])
    need(lo <= hi, 'reversed saved interval')
    return lo, hi


def clipped_upper(A, m, D):
    """One fixed rational bracket; no optimizer or root is evaluated."""
    need(m > 0 and D > 0, 'nonpositive quadratic domain')
    if A <= 0:
        branch, dquad, Q, dhi, dlo = 'nonpositive extension', F(0), F(0), F(0), F(0)
    else:
        if A <= m*D:
            branch, dquad, Q = 'quadratic interior', A/m, A*A/(2*m)
        else:
            branch, dquad, Q = 'quadratic right endpoint', D, A*D-m*D*D/2
        dhi = min(D, A/m)
        dlo = min(D, A/(m+K*dhi/2))
    debit = K*dlo**3/6
    R = Q-debit
    need(0 <= dlo <= dhi <= D and 0 <= R <= Q, 'invalid cubic bracket/upper')
    need(Q == A*dquad-m*dquad*dquad/2, 'quadratic support mismatch')
    return R, Q, dict(A_rational=str(A), positive_A_rational=str(max(F(0), A)),
        m_rational=str(m), D_rational=str(D), K_rational=str(K),
        transition_rational=str(m*D), branch=branch,
        quadratic_maximizing_displacement_rational=str(dquad),
        quadratic_upper_rational=str(Q), d_hi_rational=str(dhi), d_lo_rational=str(dlo),
        cubic_debit_rational=str(debit), corrected_upper_rational=str(R))


def check_records(source, audit, projection):
    need(source['schema'] == 'mixed-terminal-two-selected-lift-budgets-v1'
         and source['status'] == 'completed fixed protocol', 'source did not complete')
    need(source['changed_inputs'] == [] and source['unvisited_cases'] == []
         and source['all_four_budgets_enclosed'] is True, 'incomplete/changed source')
    need(source['source_path'] == PROJECTION and source['source_sha256'] == PINNED[PROJECTION],
         'source/projection association')
    need(audit['status'] == 'passed exact saved two-lift arithmetic audit'
         and audit['changed_inputs'] == [], 'saved audit did not pass')
    need(audit['source'] == SOURCE and audit['source_sha256'] == PINNED[SOURCE]
         and audit['checker'] == AUDITOR and audit['checker_sha256'] == PINNED[AUDITOR],
         'audit/source/checker association')
    need(audit['input_sha256'][SOURCE] == PINNED[SOURCE]
         and audit['input_sha256'][SOURCE_DRIVER] == PINNED[SOURCE_DRIVER],
         'audit producer bindings')
    need(source['counts'] == audit['verified_source_counts'], 'audited call counts differ')
    counts = source['counts']
    need(counts['cotangent'] == 128 and counts['vertices'] == 96 and counts['signed_gains'] == 192,
         'wrong fixed source inventory')
    need(projection['status'] == 'passed' and projection['changed_inputs'] == []
         and projection['all_boundaries_complete'] is True
         and projection['reference_counts'] == {'0': 637, '1': 646}, 'incomplete reference projection')
    need(source['reference_counts'] == projection['reference_counts']
         and source['all_boundaries_complete'] is True, 'source reference inventory')
    need(source['projection_case_hashes'] == [canonical(c) for c in projection['cases']],
         'projection case hash list')
    for record in (source, audit, projection):
        need([c['epsilon'] for c in record['cases']] == [0, 1], 'case ordering/count')
    need(len(audit['vertices']) == 96, 'audited vertex count')
    indexed = {}
    for row in audit['vertices']:
        key = row['epsilon'], row['mu'], tuple(row['flags'])
        need(key not in indexed, 'duplicate audited vertex')
        indexed[key] = row
    return indexed


def recombine(source, audit, projection, output):
    audited_vertices = check_records(source, audit, projection)
    used = set()
    pi_lo = interval(source['constants']['pi'])[0]
    need(pi_lo > 0, 'pi lower nonpositive')
    half_log_lo = interval(source['constants']['q_half'])[0]
    counts = output['counts']
    for case, saved_case, projected in zip(source['cases'], audit['cases'], projection['cases']):
        eps = case['epsilon']
        output['active_case'] = eps
        need(case['status'] == 'enclosed both added budgets', 'case incomplete')
        case_hash = canonical(projected)
        need(case['projection_case_canonical_sha256'] == saved_case['projection_case_canonical_sha256']
             == case_hash and case['coordinates'] == projected['coordinates'], 'case/reference association')
        coords = case['coordinates']
        need(set(coords) == {'r', 'b', 's', 'a'}, 'reference coordinate inventory')
        sx, sh = interval(coords['s']['real']), interval(coords['s']['imag'])
        guards = dict(center_in_original_domain=F('.24') <= sx[0] <= sx[1] <= F('.36'),
            strict_height=F('-.061') < sh[0] <= sh[1] < F('.061'))
        need(all(guards.values()), 'new shared-index curvature guard')
        m, D = K*(HALF-sx[1]), sx[1]-LEFT
        need(m > 0 and D > 0, 'shared-index domain empty')
        result = dict(epsilon=eps, source_case_canonical_sha256=canonical(case),
            projection_case_canonical_sha256=case_hash, coordinates=coords,
            new_guards=guards, m_rational=str(m), D_rational=str(D),
            K_rational=str(K), branches=[])
        output['cases'].append(result)
        need([b['mu'] for b in case['branches']] == [1, 0]
             and [b['mu'] for b in saved_case['branches']] == [1, 0], 'branch inventory')
        for branch, audited_branch in zip(case['branches'], saved_case['branches']):
            mu = branch['mu']
            output['active_branch'] = mu
            target = (LEFT, F('.45')) if mu else (F('.4'), F('.45'))
            need(interval(branch['target']) == target, 'changed selected target')
            names = ['kappa', 'I_b', 'I_rb', 'I_sb']+([] if mu else ['q_end'])
            need(branch['variable_order'] == names, 'force variable ordering')
            boxes = list(map(interval, branch['variable_intervals']))
            need(len(boxes) == len(names) and len(branch['vertices']) == 2**len(names),
                 'force box/vertex inventory')
            original_old, corrected, quadratic, flags_list = [], [], [], []
            branch_out = dict(mu=mu, target=branch['target'], variable_order=names,
                variable_intervals=branch['variable_intervals'], vertices=[])
            result['branches'].append(branch_out)
            for index, vertex in enumerate(branch['vertices']):
                flags = [(index >> (len(names)-1-j)) & 1 for j in range(len(names))]
                output['active_vertex'] = flags
                need(vertex['flags'] == flags, 'missing/reordered binary vertex')
                values = [box[flag] for box, flag in zip(boxes, flags)]
                need(list(map(F, vertex['values_rational'])) == values, 'vertex endpoint mismatch')
                key = eps, mu, tuple(flags)
                need(key in audited_vertices and key not in used, 'missing/reused audited vertex')
                used.add(key)
                audited = audited_vertices[key]
                kappa, ib, irb, isb = values[:4]
                A = kappa*(1+isb)
                ar = kappa*(1-irb)
                bf = kappa*(3*ib-irb-isb-1)
                ab = bf+(F(0) if mu else values[4])
                need({k: F(v) for k, v in vertex['forces_rational'].items()}
                     == {'r': ar, 'b_factorial': bf, 'b': ab}, 'original force identity')
                gains = vertex['gains']
                need(set(gains) == {'r', 'b'}, 'original gain inventory')
                for name, force, coefficient, domain in (
                    ('r', ar, F(88, 5), (LEFT, HALF)),
                    ('b', ab, F((mu+1)*49, 5), target)):
                    gain = gains[name]
                    need(canonical(gain) == audited[name+'_gain_canonical_sha256'],
                         'gain differs from audited certificate')
                    need(F(gain['force_rational']) == force and F(gain['K_rational']) == coefficient
                         and interval(gain['center']) == interval(coords[name]['real'])
                         and interval(gain['target']) == domain and gain['zero_cap_used'] is False,
                         'gain force/domain/center association')
                    counts['old_gain_certificates_associated'] += 1
                gr, gb = F(gains['r']['upper_rational']), F(gains['b']['upper_rational'])
                vertical = kappa*kappa*F(case['lift_data']['V_positive_upper_rational'])/pi_lo
                b_upper = interval(coords['b']['real'])[1]
                trial = -2*pi_lo*H if mu else -(HALF-b_upper)*(values[4]+half_log_lo)/2
                expression = A-2*F(case['lift_data']['v_lower_rational'])
                old_debit = F(case['lift_data']['shared_s_displacement_upper_rational'])*max(F(0), expression)
                need(F(vertex['vertical_upper_rational']) == vertical
                     and F(vertex['selected_trial_upper_rational']) == trial
                     and F(vertex['shared_expression_rational']) == expression
                     and F(vertex['shared_debit_upper_rational']) == old_debit, 'old additive components')
                old = vertical+trial+gr+gb+old_debit
                need(F(vertex['upper_rational']) == F(audited['recombined_upper_rational']) == old,
                     'old vertex/audit sum')
                R, Q, witness = clipped_upper(A, m, D)
                new, weaker = old-old_debit+R, old-old_debit+Q
                need(new == vertical+trial+gr+gb+R and new <= weaker, 'new additive recombination')
                branch_out['vertices'].append(dict(flags=flags, values_rational=vertex['values_rational'],
                    source_vertex_canonical_sha256=canonical(vertex),
                    r_gain_canonical_sha256=audited['r_gain_canonical_sha256'],
                    b_gain_canonical_sha256=audited['b_gain_canonical_sha256'],
                    original_forces_rational=vertex['forces_rational'],
                    original_vertical_upper_rational=str(vertical),
                    original_selected_trial_upper_rational=str(trial),
                    original_r_gain_upper_rational=str(gr), original_b_gain_upper_rational=str(gb),
                    original_upper_rational=str(old), removed_shared_debit_rational=str(old_debit),
                    negative_force_majorant=witness,
                    quadratic_only_upper_rational=str(weaker), new_upper_rational=str(new)))
                original_old.append(old)
                corrected.append(new)
                quadratic.append(weaker)
                flags_list.append(flags)
                counts['vertices'] += 1
                counts['quadratic_evaluations'] += 1
                counts['single_cubic_brackets'] += 1
                output['active_vertex'] = None
            old_max, new_max, q_max = max(original_old), max(corrected), max(quadratic)
            need(F(branch['upper_rational']) == F(audited_branch['upper_rational']) == old_max,
                 'old branch/audit maximum')
            need(branch['maximizing_flags'] == audited_branch['maximizing_flags']
                 == [f for f, v in zip(flags_list, original_old) if v == old_max],
                 'old maximizing flags')
            branch_out.update(original_upper_rational=str(old_max), new_upper_rational=str(new_max),
                quadratic_only_upper_rational=str(q_max),
                maximizing_flags=[f for f, v in zip(flags_list, corrected) if v == new_max],
                strict_negative=new_max < 0)
            counts['branches'] += 1
            output['active_branch'] = None
        counts['cases'] += 1
        output['active_case'] = None
    need(used == set(audited_vertices), 'unvisited audited vertex')
    need(counts['cases'] == 2 and counts['branches'] == 4 and counts['vertices'] == 96
         and counts['old_gain_certificates_associated'] == 192
         and counts['quadratic_evaluations'] == counts['single_cubic_brackets'] == 96,
         'fixed recombination count')
    worst = max(F(b['new_upper_rational']) for c in output['cases'] for b in c['branches'])
    profile = max(-F(1, 400), worst)
    positive_gap = profile < 0
    output.update(worst_main_upper_rational=str(worst), independent_nonmain_upper_rational='-1/400',
        complete_profile_upper_rational=str(profile), all_main_budgets_strictly_negative=worst < 0,
        complete_local_gap_proved=positive_gap,
        raw_local_gap_rational=str(-profile) if positive_gap else None,
        finite_source_gap_rational=str(-profile/2) if positive_gap else None)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    if hasattr(sys, 'set_int_max_str_digits'):
        sys.set_int_max_str_digits(0)
    own = Path(__file__).resolve().relative_to(ROOT).as_posix()
    bindings = {}
    output = dict(schema='mixed-terminal-penultimate-selected-budgets-v1', status='not completed',
        checker=own, checker_sha256=sha(ROOT/own), protocol=PROTOCOL, criterion=CRITERION,
        source=SOURCE, source_audit=AUDIT, input_sha256=bindings, changed_inputs=[], cases=[],
        active_case=None, active_branch=None, active_vertex=None, fallback='none',
        counts=dict(cases=0, branches=0, vertices=0, quadratic_evaluations=0, single_cubic_brackets=0,
            old_gain_certificates_associated=0, new_cubic_gains=0, analytic_evaluations=0,
            root_evaluations=0, optimizers=0, new_parameter_cells=0, retries=0),
        all_main_budgets_strictly_negative=False, complete_local_gap_proved=False,
        raw_local_gap_rational=None, finite_source_gap_rational=None,
        whole_word_theorem_proved=False, knot_volume_theorem_proved=False)
    try:
        need(PINNED and all(isinstance(h, str) and len(h) == 64 for h in PINNED.values()),
             'reviewed bindings are not finalized')

        def bind(name, digest):
            need(isinstance(digest, str) and len(digest) == 64, 'invalid input digest')
            need(name not in bindings or bindings[name] == digest, 'conflicting binding '+name)
            need(sha(ROOT/name) == digest, 'changed input '+name)
            bindings[name] = digest

        for name, digest in PINNED.items():
            bind(name, digest)
        bind(own, output['checker_sha256'])
        source, audit, projection = load(SOURCE), load(AUDIT), load(PROJECTION)
        for record in (source, audit, projection):
            need(record['changed_inputs'] == [], 'inherited changed input')
            for name, digest in record['input_sha256'].items():
                bind(name, digest)
        output.update(source_sha256=PINNED[SOURCE], source_audit_sha256=PINNED[AUDIT],
            criterion_sha256=PINNED[CRITERION], protocol_sha256=PINNED[PROTOCOL])
        recombine(source, audit, projection, output)
        output['status'] = 'completed fixed saved-vertex recombination'
    except BaseException as exc:
        output['status'] = 'failed'
        output['error'] = dict(type=type(exc).__name__, message=str(exc))
    for name, digest in bindings.items():
        if not (ROOT/name).exists() or sha(ROOT/name) != digest:
            output['changed_inputs'].append(name)
    if output['changed_inputs']:
        output['status'] = 'failed'
        output['error'] = dict(type='InputChanged', message='bound input changed during computation')
    if output['status'] == 'failed':
        output.update(all_main_budgets_strictly_negative=False, complete_local_gap_proved=False,
            raw_local_gap_rational=None, finite_source_gap_rational=None)
    output['input_sha256'] = dict(sorted(bindings.items()))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open('x', encoding='utf-8') as stream:
        json.dump(output, stream, sort_keys=True, separators=(',', ':'))
        stream.write('\n')
    print(json.dumps(dict(status=output['status'], completed_cases=len(output['cases']),
        vertices=output['counts']['vertices'], input_bindings=len(bindings),
        complete_local_gap_proved=output['complete_local_gap_proved'],
        output_sha256=sha(args.output))))
    return 0 if output['status'].startswith('completed') else 1


if __name__ == '__main__':
    raise SystemExit(main())
