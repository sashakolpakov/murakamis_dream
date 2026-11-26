#!/usr/bin/env python3
"""Focused exact/scalar check of the uniform reduced raw-row bracket."""
import argparse
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path

from flint import arb, ctx

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT/'notes/research_mixed_right_boundary_row_bracket.md'
SOURCE = ROOT/'repro/results/research-mixed-complex-right-row-reduction.json'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def ar(x):
    x = F(x)
    return arb(x.numerator)/x.denominator


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--precision', type=int, default=256)
    ap.add_argument('--input', type=Path)
    ap.add_argument('--output', type=Path, default=ROOT/
        'repro/results/research-mixed-right-boundary-row-bracket.json')
    args = ap.parse_args(); ctx.prec = args.precision
    ph, sh = sha(PROOF), sha(__file__)
    raw = SOURCE.read_bytes(); source_hash = hashlib.sha256(raw).hexdigest()
    source = json.loads(raw)
    assert source['status'] == 'passed'
    deps = {str(SOURCE.relative_to(ROOT)): source_hash}
    for field in ('dependencies', 'dependencies_sha256'):
        for path, digest in source.get(field, {}).items():
            assert path not in deps or deps[path] == digest
            assert sha(ROOT/path) == digest
            deps[path] = digest
    for path, digest in [
        ('notes/research_mixed_complex_right_row_reduction.md', source['proof_sha256']),
        ('experiments/check_mixed_complex_right_row_reduction.py', source['script_sha256'])]:
        assert sha(ROOT/path) == digest; deps[path] = digest
    checks = []
    def check(name, assertion):
        assert assertion, name
        checks.append(name)
    check('original two orientations and height signs',
        len(source['height_cases']) == 4 and
        sorted((c['height_sign'], c['complex_target_first'], c['lambda_over_2piH'])
               for c in source['height_cases']) == [(-1,0,0),(-1,1,1),(1,0,1),(1,1,0)])
    check('strict square-root enclosure', F(11,5)**2 < 5 < F(9,4)**2)
    check('first cosine threshold from strict square-root lower',
          (1+F(11,5))/2 == F(8,5))
    check('first pentagon sine bounds', 1 < (5-F(9,4))/2
          and (5-F(11,5))/2 < F(6,5)**2)
    check('second pentagon cosine upper', (F(9,4)-1)/2 < F(2,3))
    check('second pentagon sine lower', (5+F(11,5))/2 > F(9,5)**2)
    check('whole angular cosine lies strictly negative',
          F(1,4) < F(1,10)+F(1,5) == F(3,10)
          and F(1,2)+F(1,5) == F(7,10) < F(3,4))
    check('height exponential argument', 2*F(22,7)*F(57,1000) < F(9,25))
    x = F(9,25)
    check('geometric exponential majorant',
          1+x+x*x/(2*(1-x/3)) == F(1577,1100) < F(3,2))
    check('lower endpoint constant squared',
          (F(8,5)/3/F(6,5)**3)**2*13 == F(8125,6561) > 1)
    check('upper endpoint constant', F(2,3)*2/F(9,5)**2 == F(100,243)
          and F(100,243)*F(3,2) == F(50,81) < 1)
    scalars = [
        ('pi below 22/7', ar(F(22,7))-arb.pi()),
        ('positive lower derivative reserve', (25*arb(13).sqrt()/81).log()),
        ('positive upper derivative reserve', -(ar(F(50,81))).log()),
    ]
    for name, value in scalars:
        assert value.lower() > 0, name
    input_hash = None
    if args.input:
        old_raw = args.input.read_bytes(); input_hash = hashlib.sha256(old_raw).hexdigest()
        old = json.loads(old_raw)
        assert old['status'] == 'passed'
        assert old['proof_sha256'] == ph and old['script_sha256'] == sh
        assert old['dependencies_sha256'] == deps and old['checks'] == checks
        assert old['row_interval'] == ['1/5', '2/5']
    assert sha(PROOF) == ph and sha(__file__) == sh
    assert all(sha(ROOT/path) == digest for path,digest in deps.items())
    if args.input: assert sha(args.input) == input_hash
    result = dict(status='passed', precision_bits=args.precision,
        exact_checks=len(checks), checks=checks, scalar_comparisons=len(scalars),
        scalar_reserves=[dict(name=name, outward_value=str(value)) for name,value in scalars],
        primary_records=1, current_bindings=len(deps),
        row_interval=['1/5','2/5'], neighboring_real_interval=['1/10','1/2'],
        maximum_absolute_height='57/1000', new_critical_roots=0,
        new_parameter_cells=0, cyclic_word_enumerations=0,
        proof_sha256=ph, script_sha256=sh, dependencies_sha256=deps,
        scope='Uniform interior bracket for the unique continuous raw row maximum. No mixed minimum-flow sign, finite-kernel lower bound or full-period asymptotic.')
    if input_hash: result['input_sha256'] = input_hash
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print('PASS',len(checks),'exact checks;',len(scalars),'outward scalars;',len(deps),'bindings')


if __name__ == '__main__':
    main()
