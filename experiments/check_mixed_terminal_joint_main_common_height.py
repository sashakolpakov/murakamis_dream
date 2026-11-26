#!/usr/bin/env python3
"""Saved-only exact audit of the common-height terminal main criterion.

Standard library only. No analytic evaluator, root, primitive, parameter
grid, optimizer or finite-source routine is imported or executed.
"""
import argparse
from fractions import Fraction as F
import hashlib
import itertools
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = 'repro/results/research-mixed-terminal-joint-main-budget-diagnostic.json'
AUDIT = 'repro/results/research-mixed-terminal-joint-main-curvature-budget.json'
OLD_CHECKER = 'experiments/check_mixed_terminal_joint_main_curvature_budget.py'
PROOF = 'notes/research_mixed_terminal_joint_main_common_height.md'
PINNED = {
    SOURCE: '2b6e9b17d1a16071c545c0ba9f9bb2502e1f18c5009fafc1212fd326d2a621f9',
    AUDIT: '12677b1d1b20ece4ffe61c7a370cf54b3c98233fb81f082e0220435b30a89495',
    OLD_CHECKER: '4362cd068f55a15d74afa3530c37631b6ea515e5de76592583152870f28551db',
    PROOF: '3c7a3ef14df887676ca8e35c1b9b37957f2e09d0945fcadc15c947f687b9fbab',
    'notes/research_mixed_terminal_joint_main_curvature_budget.md':
        '90b947d752c6ed646b897945ff3eb3b1beffe45074dce80087c87379e1ef04ee',
    'notes/research_mixed_terminal_joint_main_height_monotonicity.md':
        '5e52f94807c21ac0f366b742d4fd0d1eba26e99d29b83c33d33de27dbd41d93e',
}


def sha(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(1048576), b''):
            h.update(chunk)
    return h.hexdigest()


def interval(record):
    assert record['finite'] is True
    lo, hi = F(record['lower_rational']), F(record['upper_rational'])
    assert lo <= hi
    return lo, hi


def inside(bounds, lo, hi):
    return F(lo) < bounds[0] <= bounds[1] < F(hi)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    assert not args.output.exists()
    inputs = dict(PINNED)
    own = Path(__file__).resolve().relative_to(ROOT).as_posix()
    inputs[own] = sha(ROOT/own)
    for name, digest in inputs.items():
        assert sha(ROOT/name) == digest, name
    source = json.loads((ROOT/SOURCE).read_text())
    audit = json.loads((ROOT/AUDIT).read_text())
    assert source['status'] == 'complete fixed diagnostic'
    assert source['changed_inputs'] == [] and source['precision_bits'] == 256
    assert F(source['height_rational']) == F(1,100)
    assert audit['status'] == 'passed' and audit['changed_inputs'] == []
    assert audit['source_path'] == SOURCE and audit['source_sha256'] == inputs[SOURCE]
    assert audit['checker_sha256'] == inputs[OLD_CHECKER]
    assert audit['canonical_reference_cases_checked'] == 4
    for parent in (source, audit):
        for name, digest in parent['input_sha256'].items():
            assert name not in inputs or inputs[name] == digest, name
            assert sha(ROOT/name) == digest, name
            inputs[name] = digest
    expected = list(itertools.product((0,1), repeat=2))
    assert [(r['beta'],r['epsilon']) for r in source['cases']] == expected
    assert [(r['beta'],r['epsilon']) for r in audit['canonical_cases']] == expected

    Bs, Bt = F(19881,1587200), F(867,40000)
    B0 = -F(109,1000)+Bs+Bt+F(63,200)*F(17,100)
    B1 = -F(50063,39680000)
    assert B0 == -F(843167,39680000)
    delta, H, C = F(7,2000), F(27,2000), F(1241,300)
    assert H == F(1,100)+delta and H < F(7,500)
    assert F(98,75)*F(22,7)+F(3,100) == C
    assert F(16,25)*F(22,7)+F(19,10) == F(1369,350) < C
    factorial, forced = B1-F(11,10)*delta, B0+C*delta
    assert factorial == -F(202831,39680000)
    assert forced == -F(4030001,595200000)
    assert -factorial-F(1,200) == F(4431,39680000)
    assert -forced-F(1,200) == F(1054001,595200000)
    assert max(factorial,forced) < -F(1,200)

    rows = []
    for row, old in zip(source['cases'], audit['canonical_cases']):
        beta, epsilon = row['beta'], row['epsilon']
        assert (row['source_index'],row['source_case_sha256']) == (
            old['source_index'],old['source_case_sha256'])
        assert row['status'] == 'both main-current bounds enclosed'
        assert row['ordinary_label_reduction_height_verified'] is True
        assert F(row['height_rational']) == F(1,100)
        q = row['actual_coordinate_enclosures']
        for name, saved in old['coordinate_guards'].items():
            assert q[name] == saved
        b, hb = map(F,row['outside_coordinate_rational'])
        assert F(11,50) <= b <= F(9,20)
        assert F(-39,500) <= hb <= F(21,1000)
        s, a, t = (interval(q[n]['real']) for n in ('s','a','t'))
        hs, ha, ht = (interval(q[n]['imag']) for n in ('s','a','t'))
        assert inside(s,'.28','.314') and inside(a,'.22','.314')
        assert inside(t,'.18','.35') and inside(ha,'-.108','-.001')
        assert inside(hs,'-.102','-.001')
        assert max(map(abs,hs)) < F(61,1000)
        assert max(map(abs,ht)) < F(33,500)
        v = 'xi' if epsilon == 0 else 'e'
        hv, vr = interval(q[v]['imag']), interval(q[v]['real'])
        if epsilon == 0:
            assert inside(ht,'-.072','.021') and inside(hv,'.049','.077')
            assert inside(vr,'.1','.4')
        else:
            assert inside(ht,'-.108','-.020') and inside(hv,'-.051','-.019')
            assert inside(vr,'.27','.49')
        assert [br['nu'] for br in row['branches']] == [1,0]
        fac, force = row['branches']
        As, At = interval(row['force_s']), interval(row['force_t'])
        Aa1 = interval(fac['force_a'])
        assert row['force_s'] == old['force_intervals']['s']
        assert row['force_t'] == old['force_intervals']['t']
        assert fac['force_a'] == old['force_intervals']['a']
        assert fac['lifted_reference_value'] == old['factorial_trial_value']
        assert inside(As,0,'.141') and inside(At,'-.255',0)
        assert inside(Aa1,'-.255',0)
        assert interval(fac['lifted_reference_value'])[1] < -F(463,10000)
        assert F(old['factorial_upper_rational']) < B1
        d = F(1,2)-s[1]
        assert d > F(93,500)
        T0, Aa0 = interval(force['lifted_reference_value']), interval(force['force_a'])
        assert T0[1] < -F(109,1000)
        assert 0 < Aa0[0] <= Aa0[1] < F(63,200)
        assert a[0] > F(7,25)
        gains = (15*As[1]**2/(128*d),At[0]**2/3,Aa0[1]*(F(9,20)-a[0]))
        assert gains[0] < Bs and gains[1] < Bt
        assert gains[2] < F(1071,20000)
        saved_B0 = T0[1]+sum(gains)
        assert saved_B0 < B0
        rows.append({
            'beta':beta,'epsilon':epsilon,'source_index':row['source_index'],
            'source_case_sha256':row['source_case_sha256'],
            'all_original_height_and_curvature_guards_verified':True,
            'new_guards':{'T0':force['lifted_reference_value'],'A_a0':force['force_a'],
                          'a_real':q['a']['real']},
            'full_P_forced_gain_uppers_rational':list(map(str,gains)),
            'full_P_forced_upper_at_H0_rational':str(saved_B0),
            'inherited_factorial_upper_at_H0_rational':old['factorial_upper_rational'],
            'common_height_rational':str(H),
            'factorial_coarse_upper_rational':str(factorial),
            'forced_coarse_upper_rational':str(forced),
            'both_full_P_branches_below_minus_1over200':True,
        })
    changed = [name for name,digest in inputs.items() if sha(ROOT/name) != digest]
    assert not changed
    result = {
        'status':'passed','source_path':SOURCE,'source_sha256':inputs[SOURCE],
        'curvature_audit_path':AUDIT,'curvature_audit_sha256':inputs[AUDIT],
        'proof_sha256':inputs[PROOF],'checker_sha256':inputs[own],
        'input_sha256':inputs,'changed_inputs':changed,
        'initial_height_rational':'1/100','common_height_rational':str(H),
        'height_increment_rational':str(delta),'forced_transport_upper_rational':str(C),
        'coarse_initial_upper_rational':{'factorial':str(B1),'forced':str(B0)},
        'coarse_final_upper_rational':{'factorial':str(factorial),'forced':str(forced)},
        'gap_reserves_above_1over200_rational':{
            'factorial':str(-factorial-F(1,200)),'forced':str(-forced-F(1,200))},
        'canonical_cases':rows,'canonical_reference_cases_checked':4,
        'common_main_gap_rational':'1/200','both_branches_bound_on_full_P':True,
        'analytic_evaluations':0,'reference_or_source_replays':0,
        'full_terminal_source_gap_claimed':False,'uniform_reference_domain_claimed':False,
        'finite_word_realization_claimed':False,
    }
    args.output.parent.mkdir(parents=True,exist_ok=True)
    with args.output.open('x') as stream:
        stream.write(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'passed','record_sha256':sha(args.output),
                      'canonical_cases':4,'common_height':str(H),'common_main_gap':'1/200'}))


if __name__ == '__main__':
    main()
