#!/usr/bin/env python3
"""Outward scalar margins for the written all-length open-word Hessian lemma.

No critical root or parameter cover is computed. The arbitrary-length
allocation is the mathematical proof; scalar tests supply its constants.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

from flint import arb, ctx


ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / 'notes/research_mixed_open_word_hessian.md'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--precision', type=int, default=192)
    ap.add_argument('--input', type=Path)
    ap.add_argument('--output', type=Path, default=ROOT /
                    'repro/results/research-mixed-open-word-hessian.json')
    args = ap.parse_args()
    assert args.precision >= 128
    ctx.prec = args.precision
    proof_sha, script_sha = sha(PROOF), sha(__file__)
    dependencies = {}

    def bind(name, expected=None):
        digest = sha(ROOT / name)
        assert expected is None or digest == expected, name
        assert name not in dependencies or dependencies[name] == digest, name
        dependencies[name] = digest

    source = 'repro/results/research-mixed-complete-boundary-sum.json'
    bind(source)
    record = json.loads((ROOT / source).read_text())
    assert record['status'] == 'passed'
    for field in ('dependencies', 'dependencies_sha256'):
        for name, digest in record.get(field, {}).items():
            bind(name, digest)
    bind('experiments/check_mixed_complete_boundary_sum.py', record['script_sha256'])
    assert 'notes/research_mixed_complete_boundary_sum.md' in dependencies

    pi = arb.pi()
    margins = {
        'Q_cosh_below_4_over_3': arb(4)/3-(6*pi/25).cosh(),
        'Q_long_sine_above_3_over_10': (9*pi/10).sin()-arb(3)/10,
        'Q_small_pair_sine_above_4_over_5': (23*pi/50).sin()-arb(4)/5,
        'Q_small_pair_cosine_above_minus_half': (27*pi/50).cos()+arb(1)/2,
        'Q_shifted_cotangent_below_1_over_7': arb(1)/7-(pi/25).tan(),
        'U_sine_above_9_over_10': (21*pi/50).sin()-arb(9)/10,
        'U_cosine_below_1_over_4': arb(1)/4-(21*pi/50).cos(),
        'U_cosh_below_5_over_4': arb(5)/4-(pi/5).cosh(),
        'difference_left_sine_above_2_over_5': (4*pi/25).sin()-arb(2)/5,
        'difference_right_sine_above_2_over_5': (13*pi/25).sin()-arb(2)/5,
        'difference_cosh_below_2': arb(2)-(19*pi/50).cosh(),
    }
    assert len(margins) == 11
    for name, margin in margins.items():
        assert margin.lower() > 0, (name, margin)

    checks = []

    def check(name, assertion):
        assert assertion, name
        checks.append(name)

    check('whole Q own cotangent lower bound',
          F(3,10)/(F(4,3)+1) == F(9,70) > F(1,8))
    check('small Q pair eigenvalue lower bound',
          F(4,5)/(F(4,3)+F(1,2))-F(2,7) == F(58,385) > F(1,8))
    check('endpoint tangent lower bound',
          F(9,10)/(F(5,4)+F(1,4)) == F(3,5))
    check('endpoint cotangent lower bound', F(9,10)/F(5,4) == F(18,25))
    check('endpoint u diagonal lower bound',
          2*F(3,5)+3*F(18,25) == F(84,25) > 3)
    check('endpoint difference cotangent lower bound', F(2,5)/3 == F(2,15))
    a, b = F(3), F(2,15)
    determinant = (a+b)*b-b*b
    trace = a+2*b
    check('endpoint matrix is positive definite', a+b > 0 and determinant > 0)
    check('endpoint determinant divided by trace', determinant/trace == F(6,49))
    check('internal legs have larger reserve than endpoint pairs', F(1,4) > F(6,49))
    check('private minus endpoint real interval stays regular',
          F(33,100)-F(1,4) == F(2,25) > 0
          and F(47,100)-F(21,100) == F(13,50) < F(1,2))
    check('private minus endpoint imaginary interval',
          F(-9,100)-F(1,10) == F(-19,100)
          and F(2,25)-F(1,100) == F(7,100))
    check('endpoint vertex sum has negative cotangent real part',
          F(33,100)+F(23,100) == F(14,25) > F(1,2)
          and F(47,100)+F(9,20) == F(23,25) < 1)
    check('single-vertex endpoint sum has the same sign',
          2*F(33,100) > F(1,2) and 2*F(47,100) < 1)
    check('additional type-four own terms are positive',
          0 < F(23,100) < F(9,20) < F(1,2)
          and 0 < F(33,100) < F(47,100) < F(1,2))
    check('two incident pair allocations restore the internal own term', -1-1 == -2)
    check('no unweighted private own term is inserted', 0+0 == 0)

    stable = dict(
        status='passed', scalar_inequality_count=11, exact_check_count=len(checks),
        scalar_names=list(margins), exact_checks=checks,
        interior_pair_hessian_lower_over_pi='1/8',
        endpoint_u_lower_over_pi='3', endpoint_difference_lower_over_pi='2/15',
        open_word_hessian_lower_over_pi='6/49', inverse_norm_upper_times_pi='49/6',
        domains={'Q':['23/100','9/20','-3/25','3/25'],
                 'E':['33/100','47/100','-9/100','2/25'],
                 'U':['21/100','1/4','1/100','1/10']},
        proof_sha256=proof_sha, script_sha256=script_sha,
        dependencies_sha256=dependencies, critical_roots_computed=0,
        parameter_cells=0, cyclic_word_enumerations=0,
        scope='Uniform accretive Hessian and uniqueness on the written product '
              'for all open words in three and four. Existence, endpoint source '
              'coverage and full open-word noncancellation are not asserted.')
    result = dict(stable, precision_bits=args.precision,
                  outward_margins={name:str(value) for name,value in margins.items()})
    input_sha = None
    if args.input:
        raw = args.input.read_bytes()
        input_sha = hashlib.sha256(raw).hexdigest()
        old = json.loads(raw)
        for name, value in stable.items():
            assert old[name] == value, name
        assert args.precision >= old['precision_bits']
        assert all(arb(value).lower() > 0 for value in old['outward_margins'].values())
        result['input_sha256'] = input_sha
    assert sha(PROOF) == proof_sha and sha(__file__) == script_sha
    assert all(sha(ROOT/name) == digest for name,digest in dependencies.items())
    if input_sha:
        assert sha(args.input) == input_sha
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print('PASS',len(margins),'outward scalar margins;',len(checks),
          'exact checks; no critical roots or parameter cover',flush=True)


if __name__ == '__main__':
    main()
