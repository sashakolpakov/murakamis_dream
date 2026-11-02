#!/usr/bin/env python3
"""Bounded finite checks for the directed circle-tree theorem.

Exact rational budgets and original endpoint pairings are replayed separately
from high-precision finite quotient/root-grid identities. Neither kind of
check proves the uniform analytic induction or the geometric volume theorem.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile


def rectangle_budgets():
    k, b, R, r, t, alpha = F(1, 2**16), F(1, 2**11), F(1, 8), F(1, 16), F(1, 2**14), F(1, 160)
    # Alternating Taylor lower bound for sin(r); 3<pi<22/7 suffices below.
    sin_lower = r-r**3/6
    margins = {
        "complementary_kernel_half_gap": F(3, 400)-(2*b+(R*R+b*b)/10+2*k),
        "far_real_angle_absorbs_parent_imaginary_cost": alpha*sin_lower**2/2-6*b*b,
        "remaining_angular_decay": alpha/2-2*k,
        "phase_class_closes": F(1, 20)-(F(1, 50)+F(20, 19*2500)),
        "conditional_saddle_stays_in_small_disk": b-t-b/20,
        "connector_bound": F(7, 8)-F(300, 361),
        "restored_angles_in_geometric_chart": F(1, 100)-F(20, 19*2**15),
        "mixed_threshold_denominator": F(2**57)-(F(2**56)+F(2**54)),
        "local_condition_implies_mixed_alternative": F(1, 2**57)-F(1, 2**120),
    }
    if not all(x>0 for x in margins.values()):
        raise AssertionError(margins)
    return {name:{"strict_margin":str(x),"decimal_for_orientation":float(x)}
            for name,x in margins.items()}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    args.output.unlink(missing_ok=True)
    if not __debug__:
        raise RuntimeError('Run with assertions enabled, without -O.')
    here=Path(__file__).resolve().parent
    repo=here.parents[1]
    arithmetic=repo/'experiments/audit_actual_all_circle_directed_volume.py'
    messages=repo/'experiments/audit_all_circle_local_message_recursion.py'
    finite=repo/'experiments/audit_main_meridian_direct_fillings.py'
    sources=sorted(here.rglob('*.tex'))+[Path(__file__).resolve(),arithmetic,messages,finite]
    sources += [repo/'notes/actual_all_circle_directed_volume.md',
                repo/'papers/meridian-tangles/main.tex',
                repo/'papers/circle-tree-geometry/main.tex',
                repo/'papers/conway-asymptotics/factorial.tex']
    sources += sorted((repo/'papers/circle-tree-asymptotics').glob('*.tex'))
    def hashes():
        return {str(p.relative_to(repo)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sources}
    before=hashes()
    budgets=rectangle_budgets()
    with tempfile.TemporaryDirectory(prefix='directed-tree-check-') as tmp:
        results=[]
        for name,script in [('arithmetic',arithmetic),('messages',messages)]:
            output=Path(tmp)/(name+'.json')
            subprocess.run([sys.executable,'-I',str(script),'--output',str(output)],
                           cwd=repo,check=True,capture_output=True,text=True)
            results.append(json.loads(output.read_text()))
    arithmetic_result,message_result=results
    assert message_result['all_degree_checks']
    assert message_result['all_identities_within_tolerance']
    # These are deliberately false strengthened requirements, not new theorems.
    root_control=next(x for x in arithmetic_result['rational_checks']
                      if x['name']=='center cannot pay any outgoing patch')
    assert F(root_control['left']) < F(root_control['right'])
    assert not F(root_control['right']) < F(root_control['left'])
    odd_stack=next(x for x in arithmetic_result['pairing_checks']
                   if x['name']=='through pairing before an odd leaf')['obtained']
    assert odd_stack != [[[0,3],[1,2]],0]
    if hashes()!=before:
        raise RuntimeError('A source changed during the checker run.')
    record={
        'scope':'Finite rational inequalities and endpoint pairings, plus explicitly high-precision finite quotient/root-grid comparisons.',
        'not_proved':['uniform complex kernel estimates','recursive Gaussian asymptotics or charge tails',
                      'topological knot identification for arbitrary inputs','hyperbolic metric and volume calibration'],
        'source_sha256':before,
        'rectangle_budgets':budgets,
        'negative_controls':['Imposing an outgoing patch on the final root rejects the certified star.',
                             'One odd inserted leaf does not have the through pairing of an even stack.'],
        'directed_arithmetic_and_pairings':arithmetic_result,
        'finite_message_comparison':message_result,
    }
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(record,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'output':str(args.output),'extra_rational_budgets':len(budgets),
                      'original_rational_checks':len(arithmetic_result['rational_checks']),
                      'endpoint_pairings':len(arithmetic_result['pairing_checks']),
                      'finite_cases':message_result['cases'],
                      'root_choices':message_result['root_choices']}))


if __name__=='__main__':
    main()
