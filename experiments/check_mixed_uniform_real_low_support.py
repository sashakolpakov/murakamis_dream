#!/usr/bin/env python3
"""Exact source-domain gluing and one oriented reset reserve."""
import argparse
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / 'notes/research_mixed_uniform_real_low_support.md'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=ROOT / 'repro/results/research-mixed-uniform-real-low-support.json')
    args = parser.parse_args()
    ph, sh = sha(PROOF), sha(__file__)
    specs = [
        ('mixed_real_zero_collar_extension', 'certify'),
        ('mixed_real_one_small_support', 'certify'),
        ('mixed_real_outer_support', 'check'),
        ('mixed_oriented_height_reset', 'certify'),
        ('mixed_fourier_weight_continuation', 'check'),
    ]
    deps, records = {}, {}
    for stem, prefix in specs:
        pp = f'notes/research_{stem}.md'
        ss = f'experiments/{prefix}_{stem}.py'
        rr = f'repro/results/research-{stem.replace("_", "-")}.json'
        for path in (pp, ss, rr):
            deps[path] = sha(ROOT / path)
        rec = json.loads((ROOT / rr).read_text())
        assert rec['status'] == 'passed', stem
        assert rec['script_sha256'] == deps[ss], stem
        inherited = rec.get('dependencies_sha256', rec.get('dependencies', {}))
        assert rec.get('proof_sha256', inherited.get(pp)) == deps[pp], stem
        for key in ('dependencies', 'dependencies_sha256'):
            for path, digest in rec.get(key, {}).items():
                assert sha(ROOT / path) == digest, (stem, path)
                if path in deps:
                    assert deps[path] == digest
                deps[path] = digest
        records[stem] = rec

    checks = []
    def check(name, condition):
        assert condition, name
        checks.append(name)

    collar = records['mixed_real_zero_collar_extension']
    compact = records['mixed_real_one_small_support']
    reset = records['mixed_oriented_height_reset']
    ell, cutoff, ylow, yhigh = F(1,1000), F(1,10), F(1,10), F(9,20)
    check('complete closed collar source', collar['reference_products'] == 64 and collar['reference_cells'] == 975)
    check('exact collar endpoint', F(collar['cutoff']) == ell)
    check('other interval is inside extended collar',
          F(collar['other_interval'][0]) <= ylow <= yhigh <= F(collar['other_interval'][1]))
    check('two low pieces cover the closed interval', F(0) < ell < cutoff)
    check('compact piece is strictly inside the real half-square',
          F(0) < ell <= cutoff < F(1,2) and F(0) < ylow <= yhigh < F(1,2))
    check('compact one-small cutoff matches', F(compact['cutoff']) == cutoff and compact['reference_products'] == 64)
    check('compact phase reserve', F(compact['phase_gap']) == F(11,200) > F(1,20))
    check('collar reserve dominates the joined gap', F(3,50) > F(1,20))
    for eta in (0,1):
        for eps in (0,1):
            check(f'original allocated power {eta}{eps}',
                  -F(1+eps,2)-F(eta+eps,4) == -F(2+eta+3*eps,4))
    check('both oriented reset costs retained',
          list(map(F, reset['integrated_one_height_costs'])) == [F(11,2), F(151,20)])
    debit = F(151,20)*F(57,1000)**2
    check('exact maximum debit', debit == F(490599,20000000))
    check('full debit is below three hundredths', debit < F(3,100))
    check('exact remaining gap', F(1,20)-debit == F(509401,20000000))
    check('reserved gap exceeds one fiftieth', F(1,20)-debit > F(1,50))
    check('adjacent plateau avoids the forcing tie', F(0) < F(11,50) <= F(9,20) < F(1,2))
    assert ph == sha(PROOF) and sh == sha(__file__)
    assert all(sha(ROOT / path) == digest for path, digest in deps.items())
    result = dict(status='passed', arithmetic='exact rational domain and normalization checks',
                  exact_checks=len(checks), checks=checks, source_records=len(specs),
                  low_interval=['0','1/10'], other_interval=['1/10','9/20'],
                  uniform_source_gap='1/20', maximum_reserved_reset=str(debit),
                  reserved_source_gap='1/50', proof_sha256=ph, script_sha256=sh,
                  dependencies_sha256=deps,
                  scope='Zero-uniform original real-target one-low kernel bound, all types/orientations/selections, with one complete oriented plateau-reset rate reserved. No zero-root transport, nonzero packet, incidence assembly or whole-period assertion.')
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print('PASS',len(checks),'exact checks +',len(specs),'current source records',flush=True)


if __name__ == '__main__':
    main()
