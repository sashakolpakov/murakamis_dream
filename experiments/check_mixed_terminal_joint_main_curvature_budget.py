#!/usr/bin/env python3
"""Exact saved-data and rational-constant audit of terminal node-cost bounds.

Standard library only. No primitive, logarithm, root, parameter, source or
old evaluator is imported or evaluated. Analytic hypotheses are proved in
the pinned note; this checks their explicit rational witnesses and inputs.
"""
import argparse
from fractions import Fraction as F
import hashlib
import itertools
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROOF = 'notes/research_mixed_terminal_joint_main_curvature_budget.md'
SOURCE = 'repro/results/research-mixed-terminal-joint-main-budget-diagnostic.json'
AUDIT = 'repro/results/research-mixed-terminal-joint-main-budget-saved-audit.json'
CHECKER = 'experiments/check_mixed_terminal_joint_main_budget_record.py'
PINNED = {'experiments/check_mixed_terminal_joint_main_budget_record.py': '80dc2c9e9dae3cdf55696a2cf92b5f9587be1af7c7b225743f8353bb8343d57b',
 'notes/research_mixed_first_cap_plateau_phase.md': '159a1b89eebcb72fa9ac3395435086f066b3e648c389e2417e0b61fb490ff612',
 'notes/research_mixed_pair_curvature_composition.md': 'b0ee9b836af171147647b6c93f0a3c1651c909867fb828184a7afdc4251a1f73',
 'notes/research_mixed_reference_shape_half_plane.md': '28c1d35c39ac2290733d6cada8e4ae1d1e6fd58ebf641c0aef9168f962e7a143',
 'notes/research_mixed_second_selected_horizontal_concavity.md': 'dac208b242a8dd24f1ce0c29e15775bd343554e0cb0141e2ad84c0fe64312ca8',
 'notes/research_mixed_selected_four_four_left_main_majorant.md': 'fffa8b11516d5ca95364e7c8823dd9323e8b09ca259bc7caaa93a8371f1006ed',
 'notes/research_mixed_terminal_four_selected_height_completion.md': '5b688d2adf67895f430a2fef77a5d98fcb8ac74846ebc2bbe1027cd6e3414127',
 'notes/research_mixed_terminal_joint_main_budget.md': '5c3e23f070d27628b3843030cd4bced887fcc7e76e25b15ed8d73a6816369baa',
 'notes/research_mixed_terminal_joint_main_curvature_budget.md': '90b947d752c6ed646b897945ff3eb3b1beffe45074dce80087c87379e1ef04ee',
 'notes/research_mixed_terminal_three_selected_height_completion.md': 'e3fea31226612be459f23e8cec8773503e562799cced20b36efcc0e4cd70e186',
 'repro/results/research-mixed-terminal-joint-main-budget-diagnostic.json': '2b6e9b17d1a16071c545c0ba9f9bb2502e1f18c5009fafc1212fd326d2a621f9',
 'repro/results/research-mixed-terminal-joint-main-budget-saved-audit.json': 'fceffb2a2bfe677579bb6ff94087b5129c9db0daf8f85674b94ee6de7fa3dda6'}


def sha(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1048576), b''):
            h.update(block)
    return h.hexdigest()


def interval(v):
    assert v['finite'] is True
    lo, hi = F(v['lower_rational']), F(v['upper_rational'])
    assert lo <= hi
    return lo, hi


def strict_inside(bounds, lo, hi):
    return F(lo) < bounds[0] <= bounds[1] < F(hi)


def cosh_upper(x):
    assert F(0) <= x < 1
    return 1 + (x*x/2)/(1-x*x/12)


def sin_lower(x):
    return x-x**3/6


def sin_upper(x):
    return x-x**3/6+x**5/120


def cos_upper(x):
    return 1-x*x/2+x**4/24


def rational_constants():
    values = {}
    def positive(name, value):
        assert value > 0, name
        values[name] = str(value)
        return value
    k, z = F(31, 10), F(8, 5)
    P = -3*k*z**3+35*z*z-19*k*z+51
    assert P == F(5167, 625)
    positive('private_Schur_numerator', P)
    positive('negative_discriminant_reserve', 4*F(279,10)*F(589,10)-70**2)
    positive('cotangent_018_witness', 8*sin_lower(F(1413,2500))-5*cos_upper(F(1413,2500)))
    positive('cotangent_010_witness', 31*sin_lower(F(157,500))-10*cos_upper(F(157,500)))
    assert F(values['cotangent_018_witness']) == F(3639318425413,62500000000000)
    assert F(values['cotangent_010_witness']) == F(3148696733,50000000000)
    for name, x, cap, expected in (
        ('private_cosh', F(121,250), F(9,8), F(32591,5882872)),
        ('s_cosh', F(671,1750), F(27,25), F(5063368,907493975)),
        ('t_cosh', F(363,875), F(109,100), F(813393,301857700)),
        ('selected_cosh', F(11,175), F(101,100), F(294779,36737900)),
    ):
        value = positive(name, cap-cosh_upper(x))
        assert value == expected
    # Elementary fifth-root trigonometric witnesses used in the proof.
    low_sqrt5, high_sqrt5 = F(111,50), F(9,4)
    positive('sqrt5_lower', 5-low_sqrt5**2)
    positive('sqrt5_upper', high_sqrt5**2-5)
    positive('sin_02pi_above_058_squared', (5-high_sqrt5)/8-F(29,50)**2)
    positive('cos_02pi_above_08', (1+low_sqrt5)/4-F(4,5))
    assert (5+low_sqrt5)/8 == F(19,20)**2  # strict sqrt5 lower gives strict sine bound
    positive('cos_04pi_above_03', (low_sqrt5-1)/4-F(3,10))
    positive('sin_064pi_above_09', 1-F(11,25)**2/2-F(9,10))
    positive('q_small_left', F(29,50)/(F(9,8)-F(4,5))-1)
    positive('q_small_right', F(19,20)/(F(9,8)-F(3,10))-1)
    positive('q_middle_right', F(9,10)/(F(9,8)+F(11,25))-F(1,2))
    positive('sqrt2_below_3over2', F(3,2)**2-2)
    assert (1+low_sqrt5)/4 == F(161,200)
    positive('sin_02pi_below_059_squared', F(59,100)**2-(5-low_sqrt5)/8)
    positive('t_cotangent_decreasing', 1-F(109,100)*F(11,25))
    positive('t_curvature_above_3over2', F(161,336)*F(157,50)-F(3,2))
    positive('sin_044pi_above_098', 1-F(33,175)**2/2-F(49,50))
    positive('s_linear_curvature_above_32over5', F(1225,572)*F(157,50)-F(32,5))
    selected = positive('selected_sine_upper', F(2,5)-sin_upper(F(352,875)))
    assert selected == F(65219373927746,7693634033203125)
    positive('selected_sine_lower', 1-F(352,875)**2/2-F(9,10))
    positive('selected_curvature_above_2', F(157,50)*F(9,10)/F(141,100)-2)
    U = 15*F(141,1000)**2/(128*F(93,500))
    T = F(51,200)**2/3
    A = F(51,200)**2/6
    assert (U,T,A) == (F(19881,1587200),F(867,40000),F(867,80000))
    gap = F(463,10000)-U-T-A
    assert gap == F(50063,39680000)
    assert gap-F(1,800) == F(463,39680000)
    positive('common_gap_reserve', gap-F(1,800))
    return values, (U,T,A), gap


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    assert not args.output.exists()
    assert PINNED, 'unfinished fixed pins'
    inputs = dict(PINNED)
    for name, digest in inputs.items():
        assert sha(ROOT/name) == digest, name
    data = json.loads((ROOT/SOURCE).read_text())
    audit = json.loads((ROOT/AUDIT).read_text())
    assert audit['status'] == 'passed' and audit['source_path'] == SOURCE
    assert audit['source_sha256'] == inputs[SOURCE]
    assert audit['checker_sha256'] == inputs[CHECKER]
    assert audit['branch_bounds_checked'] == 8 and audit['certified_reference_associations_checked'] == 4
    assert data['status'] == 'complete fixed diagnostic' and data['changed_inputs'] == []
    assert data['precision_bits'] == 256 and F(data['height_rational']) == F(1,100)
    for name, digest in data['input_sha256'].items():
        assert name not in inputs or inputs[name] == digest, name
        assert sha(ROOT/name) == digest, name
        inputs[name] = digest
    constants, coarse_gains, gap = rational_constants()
    expected = list(itertools.product((0,1), repeat=2))
    assert [(r['beta'],r['epsilon']) for r in data['cases']] == expected
    summaries = []
    for row in data['cases']:
        beta, epsilon = row['beta'], row['epsilon']
        assert row['status'] == 'both main-current bounds enclosed'
        assert F(row['height_rational']) == F(1,100)
        assert row['ordinary_label_reduction_height_verified']
        q = row['actual_coordinate_enclosures']
        s, a, t = (interval(q[n]['real']) for n in ('s','a','t'))
        hs, ht = interval(q['s']['imag']), interval(q['t']['imag'])
        v = 'xi' if epsilon == 0 else 'e'
        hv = interval(q[v]['imag'])
        b_real = F(row['outside_coordinate_rational'][0])
        hb = F(row['outside_coordinate_rational'][1])
        assert F(11,50) <= b_real <= F(9,20)
        assert strict_inside(interval(q['a']['imag']), '-.108', '-.001')
        assert F(-39,500) <= hb <= F(21,1000)
        assert strict_inside(hs, '-.102', '-.001')
        if epsilon == 0:
            assert strict_inside(ht, '-.072', '.021')
            assert strict_inside(hv, '.049', '.077')
            assert strict_inside(interval(q[v]['real']), '.1', '.4')
        else:
            assert strict_inside(ht, '-.108', '-.020')
            assert strict_inside(hv, '-.051', '-.019')
            assert strict_inside(interval(q[v]['real']), '.27', '.49')
        assert strict_inside(s, '.28', '.314')
        assert strict_inside(a, '.22', '.314')
        assert strict_inside(t, '.18', '.35')
        assert max(map(abs,hs)) < F(61,1000)
        assert max(map(abs,ht)) < F(33,500)
        assert [b['nu'] for b in row['branches']] == [1,0]
        factorial, forced = row['branches']
        As, At, Aa = interval(row['force_s']), interval(row['force_t']), interval(factorial['force_a'])
        T1 = interval(factorial['lifted_reference_value'])
        assert strict_inside(As, 0, '.141')
        assert strict_inside(At, '-.255', 0) and strict_inside(Aa, '-.255', 0)
        assert T1[1] < -F(463,10000)
        d_lower = F(1,2)-s[1]
        assert d_lower > F(93,500)
        saved_gains = (15*As[1]**2/(128*d_lower), At[0]**2/3, Aa[0]**2/6)
        assert all(g < coarse for g,coarse in zip(saved_gains,coarse_gains))
        upper = T1[1]+sum(saved_gains)
        assert upper < -gap < -F(1,800)
        assert F(forced['total_upper_rational']) < -F(1,400)
        summaries.append({'beta':beta,'epsilon':epsilon,
                          'source_index':row['source_index'],
                          'source_case_sha256':row['source_case_sha256'],
                          'coordinate_guards':{n:q[n] for n in ('s','a','t',v)},
                          'force_intervals':{'s':row['force_s'],'t':row['force_t'],'a':factorial['force_a']},
                          'factorial_trial_value':factorial['lifted_reference_value'],
                          's_remaining_length_lower_rational':str(d_lower),
                          'saved_input_gain_uppers_rational':list(map(str,saved_gains)),
                          'factorial_upper_rational':str(upper),
                          'factorial_gap_above_1over800':True,
                          'inherited_forced_upper_rational':forced['total_upper_rational']})
    own = Path(__file__).resolve().relative_to(ROOT).as_posix()
    inputs[own] = sha(ROOT/own)
    changed = [name for name,digest in inputs.items() if sha(ROOT/name) != digest]
    assert not changed
    output = {'status':'passed','source_path':SOURCE,'source_sha256':inputs[SOURCE],
              'previous_saved_audit_sha256':inputs[AUDIT],
              'proof_sha256':inputs[PROOF],'checker_sha256':inputs[own],
              'input_sha256':inputs,'changed_inputs':changed,
              'rational_witnesses':constants,'rational_witness_count':len(constants),
              'coarse_gain_uppers_rational':list(map(str,coarse_gains)),
              'coarse_factorial_gap_lower_rational':str(gap),
              'common_main_gap_rational':'1/800','canonical_cases':summaries,
              'canonical_reference_cases_checked':4,
              'analytic_evaluations':0,'reference_or_source_replays':0,
              'full_terminal_source_gap_claimed':False,
              'uniform_reference_domain_claimed':False,'finite_word_realization_claimed':False}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    with args.output.open('x') as stream:
        stream.write(json.dumps(output,indent=2)+'\n')
    print(json.dumps({'status':'passed','record_sha256':sha(args.output),
                      'canonical_cases':4,'common_main_gap':'1/800'}))


if __name__ == '__main__':
    main()
