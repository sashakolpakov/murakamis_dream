#!/usr/bin/env python3
"""Fixed saved-only private-left transfer; no analytic or gain callbacks."""
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
PROOF = 'notes/research_mixed_terminal_three_input_private_left_transfer.md'
SOURCE = 'repro/results/research-mixed-terminal-three-input-budget.json.gz'
AUDIT = 'repro/results/research-mixed-terminal-three-input-budget-saved-audit.json'
AUDITOR = 'experiments/check_mixed_terminal_three_input_budget_record.py'
DRIVER = 'experiments/certify_mixed_terminal_three_input_budget.py'
FACES = 'repro/results/research-mixed-terminal-uniform-face-reserves.json'
PINNED = {
    PROOF: '58a71a75e4559be27e410703a586e9f62b5a2af8dcd9dd0150c3648667c411a9',
    SOURCE: '18f5260f3fcd18461d8dd2859d515d9c5180f53127e917debd628ebcf26a0dec',
    AUDIT: '665135dfaa440e31b34281aebb3844845ce7d8e242dc52a9f65aaf31982c2257',
    AUDITOR: 'bc5f15c2cdb558dde4b16d690408f03eb08bbc60d0aefe7c0d906e0db1422539',
    DRIVER: '2cdcccac8295666d120d6db4b53e7862bd7e14e538a7e37f854f1b2177bd6dab',
    FACES: '37fc3676a9919525e16b214db0fedebd3e13b980150f5f01ec0d0b28141a07d3',
    'notes/research_mixed_terminal_three_input_budget_protocol.md':
        '0c37a9813a30cbd964aa0931e13ea1f1f7a2825408f64e071f7400954e4541b6',
    'notes/research_mixed_terminal_private_left_uniform_force.md':
        '20361d2a52affe5273ab4aa056f66b250fa498bb9f87742609f1d9450b9b2ee2',
    'notes/research_mixed_terminal_private_left_symmetric_transfer.md':
        '1c007e90e1fd8057d8b3773fd712fbb331b0d71c4b253664535805b37e9e7199',
    'notes/research_mixed_terminal_private_left_joint_transfer.md':
        '41de4b6ab3197e2180bab6174fe01406d525a551ae470f964d0478e8171075ff',
    'notes/research_mixed_terminal_incoming_type_transfer.md':
        '5c8f8f53c9618a19220289f21b7505358733d8a6764c352688ee0f425bd03173',
}
H, GAP = F(1, 100), F(1, 250)


def sha(path):
    digest = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1048576), b''):
            digest.update(block)
    return digest.hexdigest()


def canonical_sha(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True,
        separators=(',', ':')).encode()).hexdigest()


def iv(value):
    assert value.get('finite', True) is True
    lo, hi = F(value['lower_rational']), F(value['upper_rational'])
    assert lo <= hi
    return lo, hi


def rec(value):
    return dict(lower_rational=str(value[0]), upper_rational=str(value[1]))


def convolution(left, right):
    out = [F(0)]*(len(left)+len(right)-1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i+j] += a*b
    return out


def polynomial(coefficients, x):
    value = F(0)
    for coefficient in reversed(coefficients):
        value = value*x+coefficient
    return value


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    assert all(isinstance(v, str) and len(v) == 64 for v in PINNED.values()), \
        'completed independent audit must be pinned before execution'
    if hasattr(sys, 'set_int_max_str_digits'):
        sys.set_int_max_str_digits(0)
    inputs = dict(PINNED)
    own = Path(__file__).resolve().relative_to(ROOT).as_posix()
    inputs[own] = sha(ROOT/own)
    out = dict(status='initializing', source_path=SOURCE,
        source_sha256=inputs[SOURCE], source_audit_path=AUDIT,
        source_audit_sha256=inputs[AUDIT], proof_path=PROOF,
        proof_sha256=inputs[PROOF], checker_path=own, input_sha256=inputs,
        arithmetic_policy='New rational guards and transfer only; original analytic and gain witnesses inherited from the pinned complete audit.',
        analytic_calls=0, new_gain_calls=0, root_calls=0, subdivisions=0,
        branches=[], pending_nu=[1, 0], reference_guards={},
        private_left_gap_proved=False, full_terminal_kernel_proved=False,
        whole_source_theorem_proved=False, knot_theorem_proved=False)
    fatal = None
    try:
        for name, digest in inputs.items():
            assert sha(ROOT/name) == digest, name
        audit = json.loads((ROOT/AUDIT).read_text())
        with gzip.open(ROOT/SOURCE, 'rt', encoding='utf-8') as stream:
            source = json.load(stream)
        faces = json.loads((ROOT/FACES).read_text())
        for record in (audit, source, faces):
            assert record['changed_inputs'] == []
            for name, digest in record['input_sha256'].items():
                assert name not in inputs or inputs[name] == digest, name
                if name not in inputs:
                    assert sha(ROOT/name) == digest, name
                    inputs[name] = digest
        assert audit['status'] == 'passed'
        assert audit['source_path'] == SOURCE and audit['source_sha256'] == inputs[SOURCE]
        assert audit['checker_path'] == AUDITOR
        assert audit['all_108_comparisons_enclosed'] is True
        assert audit['checked_counts']['vertices'] == 528
        assert audit['checked_counts']['saved_gain_certificates'] == 1152
        assert audit['checked_counts']['comparisons'] == 108
        assert source['status'] == 'completed fixed protocol'
        assert source['driver_path'] == DRIVER and source['driver_sha256'] == inputs[DRIVER]
        assert not source['pending_cases'] and source['all_108_comparisons_enclosed']
        assert source['phase_scope'] == 'entire canonical D3; full independent fixed-height targets'
        assert source['source_scope'] == 'canonical actual K3; incoming unselected type3, ordinary own4'
        assert not source['whole_source_theorem_proved'] and not source['knot_theorem_proved']
        row, checked, face = source['cases'][1], audit['cases'][1], faces['cases'][1]
        for item in (row, checked, face):
            assert (item['beta'], item['epsilon']) == (0, 1)
        assert checked['source_case_canonical_sha256'] == canonical_sha(row)
        assert row['source_associations']['face'] == canonical_sha(face)
        assert face['refinement_case_canonical_sha256'] == row['source_associations']['refinement']
        assert face['all_nine_uniform_bare_bounds_defined']
        assert row['status'] == 'all fixed comparisons enclosed'
        assert tuple(map(F, row['parameter_center'])) == (F(7, 20), -F(1, 100))
        assert F(row['parameter_radius_rational']) == F(9, 100)
        assert row['private_left_route']['available'] is False
        assert checked['private_left_route'] == row['private_left_route']
        out['old_private_left_route'] = row['private_left_route']
        out['source_case_canonical_sha256'] = canonical_sha(row)
        out['source_face_case_canonical_sha256'] = canonical_sha(face)
        coordinates = {}
        for name, value in row['individual_supports'].items():
            coordinates[name] = {part: iv(value[part]) for part in ('real', 'imag')}
            for part in ('real', 'imag'):
                assert coordinates[name][part] == iv(checked['individual_coordinate_intervals'][name][part])
        for name, part, bounds in (
            ('t', 'real', (F(2987,10000), F(7,20))),
            ('t', 'imag', (-F(713,10000), -F(1,50))),
            ('a', 'real', (F(603,2000), F(9,25))),
            ('e', 'real', (F(333,1000), F(363,1000))),
            ('e', 'imag', (-F(51,1000), -F(19,1000))),
            ('a', 'imag', (-F(102,1000), -F(1,1000))),
            ('s', 'real', (F(24,100), F(36,100))),
            ('s', 'imag', (-F(102,1000), -F(1,1000)))):
            value = coordinates[name][part]
            out['reference_guards'][name+'_'+part] = dict(saved=rec(value), required=rec(bounds))
            assert bounds[0] <= value[0] <= value[1] <= bounds[1]
        delta = iv(row['height_displacement'])
        assert delta[0]+coordinates['a']['imag'][1] == H
        assert delta[1]+coordinates['a']['imag'][0] == H and delta[0] > 0
        assert F(1,100) <= H <= F(7,500)
        pi = iv(source['constants']['pi'])
        assert F(157,50) < pi[0] <= pi[1] < F(22,7)
        out['selected_height_rational'] = str(H)

        X, Y, Z, W, z = F(76459,250000), F(78657,125000), F(107859,250000), F(7843,17500), F(157,2500)
        assert X == (2*F(2987,10000)-F(1,2))*F(157,50)
        assert Y == (2*(F(2987,10000)+F(603,2000))-1)*F(157,50)
        assert Z == (2*(F(2987,10000)+F(27,100))-1)*F(157,50)
        assert W == 2*F(713,10000)*F(22,7) and 0 < W < 3
        margins = dict(
            sine_lower=X-X**3/6-F(3,10),
            sum_cosine_upper=F(81,100)-(1-Y**2/2+Y**4/24),
            private_cosine_upper=F(91,100)-(1-Z**2/2+Z**4/24),
            radius_lower=F(100,63)-(1+W+W**2/(2*(1-W/3))),
            selected_radius_upper=1+z+z*z/2-F(50,47))
        out['elementary_margins_rational'] = {k:str(v) for k,v in margins.items()}
        assert len(margins) == 5 and all(v > 0 for v in margins.values())
        base = [F(1),F(3,5),F(1)]
        D = convolution(convolution(base,base),base)
        N = convolution([F(2209,2500),F(3807,2500),F(1)],[F(1),F(91,50),F(1)])
        P = [F(26,25)*v-(N[i] if i<len(N) else 0) for i,v in enumerate(D)]
        expected = list(map(F,('.1564','-1.258952','-.411896','.62584','3.2432','1.872','1.04')))
        assert P == expected
        assert P[1] > -F(63,50) and 2*P[2] > -F(21,25)
        assert 3*P[3] > F(9,5) and 4*P[4] > 12
        assert P[5] > 0 and P[6] > 0
        derivative_lower = -F(63,50)-F(21,25)+F(9,5)*F(3,5)**2+12*F(3,5)**3
        assert derivative_lower == F(57,50) > 0
        at_left = polynomial(P,F(63,100))
        assert at_left == F(1474709079737,12500000000000) > F(1,10)
        assert (F(26,25)-1)/2 == F(1,50)
        debit = F(1,50)*(F(2,5)-F(2987,10000))
        assert debit == F(1013,500000)
        out['polynomial'] = dict(coefficients_rational=list(map(str,P)),
            derivative_lower_rational=str(derivative_lower), value_at_63over100_rational=str(at_left))
        out['force_upper_rational'], out['gain_debit_rational'] = str(F(1,50)), str(debit)

        families = [v for v in face['families'] if (v['series'],v['family']) == ('four',2)]
        assert len(families) == 1
        family = families[0]
        assert family['complete_finite_coverage'] and not family['null_jobs_unresolved']
        bare = F(family['uniform_bare_upper_rational'])
        assert bare == max(F(j['decoded_upper_rational']) for j in family['contributing_jobs'])
        assert bare < 0
        out['bare_upper_rational'] = str(bare)
        out['family_canonical_sha256'] = canonical_sha(family)
        for nu in (1,0):
            budget = [v for v in row['budgets'] if (v['kind'],v['nu']) == ('main',nu)]
            verified = [v for v in checked['budgets'] if (v['kind'],v['nu']) == ('main',nu)]
            old = [v for v in row['comparisons'] if (v['label'],v['nu']) == ('four:2',nu)]
            assert len(budget) == len(verified) == len(old) == 1
            budget,verified,old = budget[0],verified[0],old[0]
            main_upper = F(budget['budget_upper_rational'])
            assert main_upper == F(verified['upper_rational'])
            assert main_upper == max(F(v['budget_upper_rational']) for v in budget['vertices'])
            assert old['source_association']['source_family_canonical_sha256'] == canonical_sha(family)
            assert old['source_association']['source_family'] == family
            assert F(old['source_association']['bare_upper_rational']) == bare
            main_guard = -F(33,5000) if nu else -F(3,200)
            assert main_upper < main_guard
            upper = main_upper+bare+debit
            out['branches'].append(dict(nu=nu, main_budget_canonical_sha256=canonical_sha(budget),
                main_upper_rational=str(main_upper), main_guard_rational=str(main_guard),
                bare_upper_rational=str(bare), gain_debit_rational=str(debit),
                revised_upper_rational=str(upper), strict_gap_rational=str(-upper),
                old_plane_comparison={key:old[key] for key in
                    ('label','nu','upper_options_rational','chosen_upper_rational','strictly_negative')},
                old_comparison_canonical_sha256=canonical_sha(old), raw_gap_passed=upper < -GAP))
            assert upper < -GAP
            out['pending_nu'].remove(nu)
        assert len(out['branches']) == 2 and not out['pending_nu']
        out.update(status='passed',private_left_gap_proved=True,
            common_raw_gap_rational=str(GAP), verified_reference_case_count=1,
            verified_elementary_inequality_count=5, verified_polynomial_count=1,
            verified_branch_count=2)
    except (Exception,KeyboardInterrupt) as exc:
        fatal=exc
        out.update(status='failed',private_left_gap_proved=False,
                   error=dict(type=type(exc).__name__,message=str(exc)))
    out['changed_inputs'] = [name for name,digest in inputs.items()
                            if not (ROOT/name).is_file() or sha(ROOT/name)!=digest]
    if out['changed_inputs']:
        out.update(status='changed inputs',private_left_gap_proved=False)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    with args.output.open('x') as stream:
        json.dump(out,stream,sort_keys=True,indent=2);stream.write('\n')
    print(json.dumps(dict(status=out['status'],private_left_gap_proved=out['private_left_gap_proved'],
                         output_sha256=sha(args.output))),flush=True)
    if fatal is not None:
        raise fatal
    if out['changed_inputs']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
