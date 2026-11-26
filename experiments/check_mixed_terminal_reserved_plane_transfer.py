#!/usr/bin/env python3
"""Exact saved-endpoint audit of terminal reserved-plane transfer.

Standard library only. The saved centered primitive and logarithmic
increment enclosures are inputs; no analytic function is reevaluated.
"""
import argparse
from fractions import Fraction as F
import hashlib
import itertools
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROOF = 'notes/research_mixed_terminal_reserved_plane_transfer.md'
SOURCE = 'repro/results/research-mixed-terminal-joint-main-budget-diagnostic.json'
REFS = 'repro/results/research-mixed-terminal-horizontal-envelope-diagnostic.json'
REF_AUDIT = 'repro/results/research-mixed-terminal-horizontal-envelope-saved-audit.json'
CURVATURE = 'repro/results/research-mixed-terminal-joint-main-curvature-budget.json'
PINNED = {
    PROOF: '0d4461c5b00e4f68dc00c0c1d6e824156c9c5050327eab70694f3cd21e714c70',
    SOURCE: '2b6e9b17d1a16071c545c0ba9f9bb2502e1f18c5009fafc1212fd326d2a621f9',
    REFS: 'ca58c35640f1e2894f35b0f2c841029ff28b1c4af8411c1a12da012ace09059b',
    REF_AUDIT: 'bedf680b3f57c799980517f7aa6178a7f9c5a0890bac8528947e9018baf7a4de',
    CURVATURE: '12677b1d1b20ece4ffe61c7a370cf54b3c98233fb81f082e0220435b30a89495',
    'experiments/check_mixed_terminal_horizontal_envelope_record.py':
        '23545f9f66ec7ba9e2ddb89410f9c198a64f4d615b95df4d346bc2083936cdcb',
    'experiments/check_mixed_terminal_joint_main_curvature_budget.py':
        '4362cd068f55a15d74afa3530c37631b6ea515e5de76592583152870f28551db',
    'notes/research_mixed_terminal_three_alias_reserve.md':
        '8780ddc96481a15f6b75e54ed7311a7f4e6272c7969056c8f63265f7e5cb6d82',
    'notes/research_mixed_terminal_four_alias_reserve.md':
        '02619c9f58624475deb1b88d39125b907b37e97fa4d6b94a1573a4fe5a965eaa',
    'repro/results/research-mixed-terminal-three-alias-reserve.json':
        '039094505d49f8736485224fceaf280de836bba635301b1fa669e51c2d9fd483',
    'repro/results/research-mixed-terminal-four-alias-reserve.json':
        '6ff887ab81798ea4e237dfaf39cbd99f17cfecda367bc4e551f92ea61da351d0',
}


def sha(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for part in iter(lambda: stream.read(1048576), b''):
            h.update(part)
    return h.hexdigest()


def fragment_sha(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,
                                    separators=(',',':')).encode()).hexdigest()


def interval(value):
    assert value['finite'] is True
    lo, hi = F(value['lower_rational']), F(value['upper_rational'])
    assert lo <= hi
    return lo, hi


def record(value):
    return {'finite':True,'lower_rational':str(value[0]),'upper_rational':str(value[1])}


def contains(outer, inner):
    return outer[0] <= inner[0] <= inner[1] <= outer[1]


def inside(value, lo, hi):
    return F(lo) < value[0] <= value[1] < F(hi)


def add(a, b):
    return a[0]+b[0], a[1]+b[1]


def scale(c, a):
    c = F(c)
    return (c*a[0],c*a[1]) if c >= 0 else (c*a[1],c*a[0])


def mul(a, b):
    corners = [x*y for x in a for y in b]
    return min(corners),max(corners)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args = parser.parse_args()
    assert not args.output.exists()
    inputs = dict(PINNED)
    own = Path(__file__).resolve().relative_to(ROOT).as_posix()
    inputs[own] = sha(ROOT/own)
    for name,digest in inputs.items():
        assert sha(ROOT/name) == digest,name
    source = json.loads((ROOT/SOURCE).read_text())
    refs = json.loads((ROOT/REFS).read_text())
    ref_audit = json.loads((ROOT/REF_AUDIT).read_text())
    curvature = json.loads((ROOT/CURVATURE).read_text())
    assert source['status'] == refs['status'] == 'complete fixed diagnostic'
    assert source['changed_inputs'] == refs['changed_inputs'] == []
    assert ref_audit['status'] == curvature['status'] == 'passed'
    assert ref_audit['source_path'] == REFS and ref_audit['source_sha256'] == inputs[REFS]
    assert ref_audit['checker_sha256'] == inputs[
        'experiments/check_mixed_terminal_horizontal_envelope_record.py']
    assert ref_audit['canonical_references_checked'] == 4
    assert curvature['source_path'] == SOURCE and curvature['source_sha256'] == inputs[SOURCE]
    assert curvature['checker_sha256'] == inputs[
        'experiments/check_mixed_terminal_joint_main_curvature_budget.py']
    assert curvature['canonical_reference_cases_checked'] == 4
    assert curvature['changed_inputs'] == []
    for parent in (source,refs,curvature):
        for name,digest in parent['input_sha256'].items():
            assert name not in inputs or inputs[name] == digest,name
            assert sha(ROOT/name) == digest,name
            inputs[name] = digest
    H = F(1,100)
    assert F(source['height_rational']) == H
    assert source['precision_bits'] == refs['precision_bits'] == 256
    pi = interval(source['pi'])
    assert inside(pi,F(157,50),F(22,7))
    expected = list(itertools.product((0,1),repeat=2))
    for rows in (source['cases'],refs['cases'],curvature['canonical_cases']):
        assert [(row['beta'],row['epsilon']) for row in rows] == expected
    s_coarse = F(19881,1587200)
    E1_coarse = F(19,500)+s_coarse+F(16129,4000000)
    E0_coarse = F(3,500)+s_coarse+F(561,20000)
    assert E1_coarse < F(11,200) and E0_coarse < F(11,200)
    assert F(59,1000)-F(11,200) == F(1,250)
    assert F(63,1000)-F(11,200) == F(1,125)
    summaries = []
    for index,(row,ref,old) in enumerate(zip(
            source['cases'],refs['cases'],curvature['canonical_cases'])):
        beta,epsilon = row['beta'],row['epsilon']
        assert row['source_index'] == old['source_index'] == index
        assert row['source_case_sha256'] == old['source_case_sha256'] == fragment_sha(ref)
        assert ref['canonical_reference_certified'] is True
        assert ref['status'] == 'canonical reference and lower tests certified'
        assert row['status'] == 'both main-current bounds enclosed'
        assert row['ordinary_label_reduction_height_verified'] is True
        assert F(row['height_rational']) == H
        assert row['saved_coordinate_enclosures'] == ref['coordinate_enclosures']
        assert row['outside_coordinate_rational'] == ref['outside_coordinate']
        q = row['actual_coordinate_enclosures']
        for name,saved in old['coordinate_guards'].items():
            assert q[name] == saved
        for name in ('e','xi','t','a','s'):
            assert ref['domain_checks'][name]['common_product_verified']
            assert ref['domain_checks'][name]['typed_rectangle_verified']
            for part in ('real','imag'):
                assert contains(interval(q[name][part]),interval(ref['coordinate_enclosures'][name][part]))
        for name in ('a','t'):
            for part in ('real','imag'):
                assert contains(interval(ref['actual_marginal_input_enclosures'][name][part]),
                                interval(ref['coordinate_enclosures'][name][part]))
        for name in ('a','s'):
            guard = ref['domain_checks'][name]
            assert F(guard['typed_disk_radius_squared_rational']) == F(9,2500)
            assert F(guard['typed_disk_squared_distance_upper_rational']) < F(9,2500)
        if epsilon:
            guard = ref['domain_checks']['a']
            assert F(guard['oriented_real_floor_rational']) > F(259,1000)
            assert F(guard['oriented_threshold_rational']) == F(259,1000)
        b,hb = map(F,row['outside_coordinate_rational'])
        assert (b,hb) == ((F(7,20),-F(1,100)) if beta == 0 else
                          (F(3,10),-F(13,250)))
        assert F(11,50) <= b <= F(9,20)
        assert F(-39,500) <= hb <= F(21,1000)
        s,a,t = (interval(q[name]['real']) for name in ('s','a','t'))
        hs,ha,ht = (interval(q[name]['imag']) for name in ('s','a','t'))
        assert inside(s,'.28','.314') and inside(a,'.28','.314')
        assert inside(hs,'-.102','-.001') and max(map(abs,hs)) < F(61,1000)
        assert inside(ha,'-.108','-.001') and inside(t,'.18','.35')
        assert max(map(abs,ht)) < F(33,500)
        v = 'xi' if epsilon == 0 else 'e'
        if epsilon == 0:
            assert inside(ht,'-.072','.021') and inside(interval(q[v]['imag']),'.049','.077')
            assert inside(interval(q[v]['real']),'.1','.4')
        else:
            assert inside(ht,'-.108','-.020') and inside(interval(q[v]['imag']),'-.051','-.019')
            assert inside(interval(q[v]['real']),'.27','.49')
        delta = interval(row['delta'])
        saved_ha = interval(ref['coordinate_enclosures']['a']['imag'])
        assert contains(delta,(H-saved_ha[1],H-saved_ha[0])) and delta[0] > 0
        p_im = interval(ref['allocated_terminal_marginal']['imag'])
        Bg_a = interval(row['centered_primitives']['a']['real'])
        Bg_sa = interval(row['centered_primitives']['sa']['real'])
        L_a = interval(row['log_increments']['a']['real'])
        L_sa = interval(row['log_increments']['sa']['real'])
        aH = row['original_values']['aH']
        assert aH['original_strip_and_cuts_verified']
        assert contains(interval(aH['argument']['real']),interval(ref['coordinate_enclosures']['a']['real']))
        assert contains(interval(aH['argument']['imag']),(H,H))
        gaH, gpaH = interval(aH['g']['real']),interval(aH['g_prime']['real'])
        fee = mul(delta,p_im)
        J1 = add(add(add(fee,Bg_sa),scale(-F(3,2),Bg_a)),scale(-H,pi))
        J0 = add(add(J1,scale(F(1,2),gaH)),scale(H,pi))
        Gs = L_sa
        G1 = add(L_sa,scale(-F(3,2),L_a))
        G0 = add(G1,scale(F(1,2),gpaH))
        assert inside(Gs,0,'.141') and inside(G1,'-.127',0) and inside(G0,0,'.165')
        assert J1[1] < F(19,500) and J0[1] < F(3,500)
        d = F(1,2)-s[1]
        assert d > F(93,500)
        s_gain = 15*Gs[1]**2/(128*d)
        a1_gain = G1[0]**2/4
        a0_gain = G0[1]*(F(9,20)-a[0])
        assert s_gain < s_coarse
        assert a1_gain < F(16129,4000000) and a0_gain < F(561,20000)
        E1, E0 = J1[1]+s_gain+a1_gain,J0[1]+s_gain+a0_gain
        assert E1 < E1_coarse < F(11,200)
        assert E0 < E0_coarse < F(11,200)
        summaries.append({
            'beta':beta,'epsilon':epsilon,'source_index':index,
            'source_case_sha256':row['source_case_sha256'],
            'original_height_and_source_guards_verified':True,
            'selected_height_rational':str(H),
            'saved_inputs':{'delta':record(delta),'pT_imag':record(p_im),
                           'Bg_a_real':record(Bg_a),'Bg_sa_real':record(Bg_sa),
                           'L_a_real':record(L_a),'L_sa_real':record(L_sa),
                           'g_aH_real':record(gaH),'gprime_aH_real':record(gpaH)},
            'positive_terminal_fee':record(fee),
            'J1':record(J1),'J0':record(J0),'Gs':record(Gs),
            'G_a1':record(G1),'G_a0':record(G0),
            's_gain_upper_rational':str(s_gain),
            'selected_gain_upper_rational':{'factorial':str(a1_gain),'forced':str(a0_gain)},
            'joined_plane_upper_rational':{'factorial':str(E1),'forced':str(E0)},
            'both_plane_budgets_below_11over200':True,
        })
    changed = [name for name,digest in inputs.items() if sha(ROOT/name) != digest]
    assert not changed
    result = {
        'status':'passed','source_path':SOURCE,'source_sha256':inputs[SOURCE],
        'marginal_source_path':REFS,'marginal_source_sha256':inputs[REFS],
        'reference_audit_sha256':inputs[REF_AUDIT],'curvature_audit_sha256':inputs[CURVATURE],
        'proof_sha256':inputs[PROOF],'checker_sha256':inputs[own],
        'input_sha256':inputs,'changed_inputs':changed,'selected_height_rational':str(H),
        'canonical_reference_cases_checked':4,'joined_plane_alternatives_checked':8,
        'coarse_plane_upper_rational':{'factorial':str(E1_coarse),'forced':str(E0_coarse)},
        'common_plane_upper_rational':'11/200',
        'coarse_upper_reserve_rational':{'factorial':str(F(11,200)-E1_coarse),
                                        'forced':str(F(11,200)-E0_coarse)},
        'alias_endpoint_gap_rational':'1/250','constant_profile_gap_rational':'1/125',
        'canonical_cases':summaries,'analytic_evaluations':0,'reference_or_source_replays':0,
        'entire_alias_integral_suppressed_claimed':False,
        'full_terminal_source_gap_claimed':False,'uniform_reference_domain_claimed':False,
        'finite_word_realization_claimed':False,
    }
    args.output.parent.mkdir(parents=True,exist_ok=True)
    with args.output.open('x') as stream:
        stream.write(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'passed','record_sha256':sha(args.output),
                      'canonical_cases':4,'common_plane_upper':'11/200'}))


if __name__ == '__main__':
    main()
