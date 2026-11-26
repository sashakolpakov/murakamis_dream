#!/usr/bin/env python3
"""Assemble the exact 108-row terminal ledger; no analytic or gain calls."""
import argparse
from fractions import Fraction as F
import hashlib
from itertools import product
import json
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[1]
PROOF='notes/research_mixed_terminal_three_input_completion_protocol.md'
AUDIT='repro/results/research-mixed-terminal-three-input-budget-saved-audit.json'
SOURCE='repro/results/research-mixed-terminal-three-input-budget.json.gz'
CUT='repro/results/research-mixed-terminal-three-input-terminal-cut.json'
PRIVATE='repro/results/research-mixed-terminal-three-input-private-left-transfer.json'
FACES='repro/results/research-mixed-terminal-uniform-face-reserves.json'
ALIASES='repro/results/research-mixed-terminal-uniform-alias-reserves.json'
PINNED={
    'notes/research_mixed_terminal_three_input_completion_protocol.md': 'e5da41359ece1302c3a642c5303a675feb5f4442b2933e125873fa76f220e94d',
    'repro/results/research-mixed-terminal-three-input-budget-saved-audit.json': '665135dfaa440e31b34281aebb3844845ce7d8e242dc52a9f65aaf31982c2257',
    'repro/results/research-mixed-terminal-three-input-budget.json.gz': '18f5260f3fcd18461d8dd2859d515d9c5180f53127e917debd628ebcf26a0dec',
    'repro/results/research-mixed-terminal-three-input-terminal-cut.json': '4aa9cf123ecd0d0cae3f862bf0110da71e360c939cc6488aa6f2b1479ea5f933',
    'repro/results/research-mixed-terminal-uniform-face-reserves.json': '37fc3676a9919525e16b214db0fedebd3e13b980150f5f01ec0d0b28141a07d3',
    'repro/results/research-mixed-terminal-uniform-alias-reserves.json': '142f424a414174fc8ee8ba0fd4ee69b6c8c6ffd5c954bbba9211771536b9bd87',
    'experiments/check_mixed_terminal_three_input_budget_record.py': 'bc5f15c2cdb558dde4b16d690408f03eb08bbc60d0aefe7c0d906e0db1422539',
    'experiments/check_mixed_terminal_three_input_terminal_cut.py': 'c86c29a6f7c76a8d8b474f2b8aed01c54f909b9bd4ffc617d4fe860097b0de90',
    'notes/research_mixed_terminal_three_input_terminal_cut_transfer.md': 'd8d22b1fc9b08faadefca6cdd6659bf4ab576715493a98aef6693ff9148e0277',
    'experiments/check_mixed_terminal_three_input_private_left_transfer.py': '3e36dc47da849fd9dc8db2d522d3e534a86ef5d66417184327db2b5a8186df99',
    'notes/research_mixed_terminal_three_input_private_left_transfer.md': '58a71a75e4559be27e410703a586e9f62b5a2af8dcd9dd0150c3648667c411a9',
    'notes/research_mixed_terminal_incoming_type_transfer.md': '5c8f8f53c9618a19220289f21b7505358733d8a6764c352688ee0f425bd03173',
    'repro/results/research-mixed-terminal-three-input-private-left-transfer.json': '9ddff909d06f766f8a7a04977db24a49ec5b392d69efa4b8f2bc040f1a8ac470',
}
GAP=F(1,10000)


def sha(path):
    digest=hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda:stream.read(1048576),b''):digest.update(block)
    return digest.hexdigest()


def canonical_sha(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':')).encode()).hexdigest()


def iv(value):
    assert value.get('finite',True) is True
    result=F(value['lower_rational']),F(value['upper_rational'])
    assert result[0]<=result[1]
    return result


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    assert PINNED and all(isinstance(v,str) and len(v)==64 for v in PINNED.values()),'successful private-left result not yet pinned'
    if args.output.exists():raise FileExistsError(args.output)
    if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
    inputs=dict(PINNED)
    own=Path(__file__).resolve().relative_to(ROOT).as_posix();inputs[own]=sha(ROOT/own)
    out=dict(status='initializing',proof_path=PROOF,checker_path=own,input_sha256=inputs,
        analytic_calls=0,source_evaluations=0,root_calls=0,new_gain_calls=0,subdivisions=0,retries=0,
        cases=[],replacement_checks=[],raw_gap_rational=str(GAP),finite_gap_rational=str(GAP/2),
        all_108_paid=False,whole_source_theorem_proved=False,knot_theorem_proved=False)
    fatal=None
    try:
        for name,digest in inputs.items():assert sha(ROOT/name)==digest,name
        data={name:json.loads((ROOT/name).read_text()) for name in (AUDIT,CUT,PRIVATE,FACES,ALIASES)}
        audit,cut,private,faces,aliases=(data[n] for n in (AUDIT,CUT,PRIVATE,FACES,ALIASES))
        for record in data.values():
            assert record['changed_inputs']==[]
            for name,digest in record['input_sha256'].items():
                assert name not in inputs or inputs[name]==digest,name
                if name not in inputs:
                    assert sha(ROOT/name)==digest,name
                    inputs[name]=digest
        assert audit['status']=='passed' and audit['source_path']==SOURCE and audit['source_sha256']==inputs[SOURCE]
        assert audit['all_108_comparisons_enclosed'] and audit['checked_counts']['comparisons']==108
        assert audit['checked_counts']['vertices']==528 and audit['checked_counts']['saved_gain_certificates']==1152
        assert audit['negative_comparisons']==audit['target_gap_comparisons']==105 and audit['unresolved_comparisons']==3
        assert len(audit['cases'])==2
        assert faces['all_uniform_bare_bounds_defined'] and aliases['all_uniform_alias_bounds_defined']
        assert not faces['unresolved_family_cases'] and not aliases['unresolved_family_cases']
        base={};unresolved=set();old_paid=0
        for epsilon,row in enumerate(audit['cases']):
            assert (row['beta'],row['epsilon'])==(0,epsilon)
            face,alias=faces['cases'][epsilon],aliases['cases'][epsilon]
            assert (face['beta'],face['epsilon'])==(0,epsilon)==(alias['beta'],alias['epsilon'])
            assert alias['image_cover_case_canonical_sha256']==canonical_sha(face)
            expected_families=([('four',j) for j in list(range(8))+[20]] if epsilon else
                [('three_mixed',j) for j in range(8)]+[('three_half',0)])
            assert [(f['series'],f['family']) for f in face['families']]==expected_families
            labels=['main','constant']+['alias:'+a['t_state']+':'+a['private_state'] for a in alias['alias_labels']]+[
                series+':'+str(family) for series,family in expected_families]
            assert len(labels)==len(set(labels))==27
            expected={(epsilon,label,nu) for label in labels for nu in (1,0)}
            assert len(row['comparisons'])==54
            actual=set()
            for comparison in row['comparisons']:
                key=epsilon,comparison['label'],comparison['nu']
                assert key not in actual;actual.add(key)
                options={name:F(v) for name,v in comparison['upper_options_rational'].items()}
                value=min(options.values())
                assert F(comparison['chosen_upper_rational'])==value
                assert comparison['strictly_negative']==(value<0)
                assert comparison['target_gap_passed']==(value < -GAP)
                base[key]=comparison
                if value < -GAP:old_paid+=1
                else:unresolved.add(key)
            assert actual==expected
        expected_new={(1,'four:0',1),(1,'four:2',1),(1,'four:2',0)}
        assert unresolved==expected_new and old_paid==105 and len(base)==108

        row=audit['cases'][1];face=faces['cases'][1]
        assert cut['status']=='completed fixed saved-only protocol' and cut['target_passed'] and cut['strictly_negative']
        assert cut['source_path']==SOURCE and cut['audit_path']==AUDIT
        assert cut['source_case_canonical_sha256']==row['source_case_canonical_sha256']
        assert F(cut['target_gap_rational'])==GAP
        assert cut['counts']==dict(analytic_evaluations=0,independent_checks=64,rational_gains=64,
            reference_evaluations=0,retries=0,vertices=32)
        old=cut['previous_comparison'];base_old=base[1,'four:0',1]
        for key in base_old:assert old[key]==base_old[key]
        family,=[f for f in face['families'] if (f['series'],f['family'])==('four',0)]
        assert cut['source_family']==family
        assert old['source_association']['source_family']==family
        assert old['source_association']['source_family_canonical_sha256']==canonical_sha(family)
        assert family['complete_finite_coverage'] and not family['null_jobs_unresolved']
        bare=F(family['uniform_bare_upper_rational'])
        assert bare==F(cut['bare_upper_rational'])==F(old['source_association']['bare_upper_rational'])
        assert bare==max(F(j['decoded_upper_rational']) for j in family['contributing_jobs'])
        assert cut['parameter_order']==['kappa','Ia','Is','Icut','ReD']
        parameters=list(map(iv,cut['parameter_intervals']));assert len(parameters)==5
        costs={k:F(v) for k,v in cut['costs_rational'].items()}
        assert costs==dict(s=F(88,5),a=F(49,5)*(1+F(1,2)+F(3,5)))
        trial=F(cut['trial_upper_rational'])
        assert len(cut['vertices'])==32
        totals=[];saved_gain_uppers=0
        for vertex,bits in zip(cut['vertices'],product((0,1),repeat=5)):
            assert vertex['endpoint_bits']==list(bits)
            k,ia,iss,icut,d=[pair[bit] for pair,bit in zip(parameters,bits)]
            forces=dict(s=k*(1-iss),a=d+k*(3*ia-iss-icut-1))
            assert {n:F(v) for n,v in vertex['forces_rational'].items()}==forces
            assert set(vertex['gains'])==set(vertex['checks'])=={'s','a'}
            gain_sum=F(0)
            for name,K in costs.items():
                witness=vertex['gains'][name]
                assert iv(witness['force'])==(forces[name],forces[name]) and F(witness['K_rational'])==K
                center=iv(row['individual_coordinate_intervals'][name]['real'])
                target=(F('.22'),F('.5') if name=='s' else F('.45'))
                assert iv(witness['center'])==center and iv(witness['target'])==target
                assert vertex['checks'][name]==len(witness['branches'])
                upper=max(F(0),*(iv(branch['value'])[1] for branch in witness['branches']))
                assert F(witness['upper_rational'])==upper
                gain_sum+=upper;saved_gain_uppers+=1
            total=trial+gain_sum
            assert F(vertex['budget_upper_rational'])==total
            totals.append(total)
        assert saved_gain_uppers==64
        budget=max(totals)
        new_cut=budget+bare
        assert F(cut['budget_upper_rational'])==budget
        assert F(cut['comparison_upper_rational'])==new_cut and new_cut < -GAP
        replacements={(1,'four:0',1):('terminal_coordinate_cut',new_cut)}
        out['replacement_checks'].append(dict(epsilon=1,label='four:0',nu=1,source_path=CUT,
            source_sha256=inputs[CUT],source_family_sha256=canonical_sha(family),
            vertex_count=32,saved_gain_upper_count=64,trial_upper_rational=str(trial),
            vertex_budget_maximum_rational=str(budget),bare_upper_rational=str(bare),new_upper_rational=str(new_cut)))

        assert private['status']=='passed' and private['private_left_gap_proved']
        assert private['source_path']==SOURCE and private['source_sha256']==inputs[SOURCE]
        assert private['source_audit_path']==AUDIT and private['source_audit_sha256']==inputs[AUDIT]
        assert private['source_case_canonical_sha256']==row['source_case_canonical_sha256']
        assert private['source_face_case_canonical_sha256']==canonical_sha(face)
        assert private['old_private_left_route']==row['private_left_route']
        assert private['old_private_left_route']['available'] is False
        for key in ('analytic_calls','new_gain_calls','root_calls','subdivisions'):assert private[key]==0
        assert F(private['selected_height_rational'])==F(1,100)
        assert F(private['common_raw_gap_rational'])==F(1,250)
        assert private['verified_reference_case_count']==1 and private['verified_branch_count']==2
        assert private['verified_elementary_inequality_count']==5 and private['verified_polynomial_count']==1
        assert not private['pending_nu'] and len(private['branches'])==2
        assert all(F(v)>0 for v in private['elementary_margins_rational'].values())
        assert F(private['force_upper_rational'])==F(1,50)
        debit=F(1,50)*(F(2,5)-F(2987,10000))
        assert F(private['gain_debit_rational'])==debit==F(1013,500000)
        family,=[f for f in face['families'] if (f['series'],f['family'])==('four',2)]
        assert family['complete_finite_coverage'] and not family['null_jobs_unresolved']
        assert private['family_canonical_sha256']==canonical_sha(family)
        bare=F(family['uniform_bare_upper_rational'])
        assert F(private['bare_upper_rational'])==bare<0
        assert bare==max(F(j['decoded_upper_rational']) for j in family['contributing_jobs'])
        for branch,nu in zip(private['branches'],(1,0)):
            assert branch['nu']==nu
            old=base[1,'four:2',nu]
            for key,value in branch['old_plane_comparison'].items():assert value==old[key]
            main,=[b for b in row['budgets'] if (b['kind'],b['nu'])==('main',nu)]
            main_upper=F(main['upper_rational'])
            assert F(branch['main_upper_rational'])==main_upper
            guard=-F(33,5000) if nu else -F(3,200)
            assert F(branch['main_guard_rational'])==guard and main_upper<guard
            assert F(branch['bare_upper_rational'])==bare and F(branch['gain_debit_rational'])==debit
            upper=main_upper+bare+debit
            assert F(branch['revised_upper_rational'])==upper and F(branch['strict_gap_rational'])==-upper
            assert branch['raw_gap_passed'] and upper < -F(1,250)
            replacements[1,'four:2',nu]=('bounded_force_private_left',upper)
            out['replacement_checks'].append(dict(epsilon=1,label='four:2',nu=nu,source_path=PRIVATE,
                source_sha256=inputs[PRIVATE],source_family_sha256=canonical_sha(family),
                main_upper_rational=str(main_upper),bare_upper_rational=str(bare),
                gain_debit_rational=str(debit),new_upper_rational=str(upper)))
        assert set(replacements)==expected_new

        new_paid=0;worst=None
        for epsilon,case in enumerate(audit['cases']):
            output=dict(beta=0,epsilon=epsilon,source_case_canonical_sha256=case['source_case_canonical_sha256'],
                comparisons=[],old_private_left_route=case['private_left_route'])
            out['cases'].append(output)
            for previous in case['comparisons']:
                key=epsilon,previous['label'],previous['nu']
                options={name:F(v) for name,v in previous['upper_options_rational'].items()}
                if key in replacements:
                    name,value=replacements[key];assert name not in options;options[name]=value
                best=min(options.values());assert best < -GAP
                output['comparisons'].append(dict(label=key[1],nu=key[2],previous_comparison=previous,
                    upper_options_rational={n:str(v) for n,v in options.items()},
                    chosen_upper_rational=str(best),strict_gap_rational=str(-best),target_passed=True))
                new_paid+=1;worst=best if worst is None else max(worst,best)
            assert len(output['comparisons'])==54
            output['worst_upper_rational']=str(max(F(v['chosen_upper_rational']) for v in output['comparisons']))
        assert new_paid==108 and len(out['replacement_checks'])==3
        out.update(status='passed',old_paid_count=105,old_unresolved_count=3,new_paid_count=108,
            remaining_count=0,all_108_paid=True,worst_upper_rational=str(worst),
            counts=dict(original_rows=108,replacement_rows=3,cut_vertex_sums=32,saved_gain_uppers=64,private_sums=2),
            source_scope='canonical actual K3, incoming type3 unselected, ordinary own4, terminal type3 or4; outer plateau only')
    except (Exception,KeyboardInterrupt) as exc:
        fatal=exc;out.update(status='failed',all_108_paid=False,error=dict(type=type(exc).__name__,message=str(exc)))
    out['changed_inputs']=[name for name,digest in inputs.items() if not (ROOT/name).is_file() or sha(ROOT/name)!=digest]
    if out['changed_inputs']:out.update(status='changed inputs',all_108_paid=False)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    with args.output.open('x') as stream:json.dump(out,stream,sort_keys=True,indent=2);stream.write('\n')
    print(json.dumps(dict(status=out['status'],all_108_paid=out['all_108_paid'],output_sha256=sha(args.output))),flush=True)
    if fatal is not None:raise fatal
    if out['changed_inputs']:raise SystemExit(1)


if __name__=='__main__':main()
