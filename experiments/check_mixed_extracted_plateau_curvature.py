#!/usr/bin/env python3
"""Extract rigorous whole-cell minima from completed reset records; no rerun."""
import argparse
import hashlib
import itertools
import json
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT/'notes/research_mixed_extracted_plateau_curvature.md'
SOURCE_PROOF = 'notes/research_mixed_full_height_reset.md'
SOURCE_SCRIPT = 'experiments/certify_mixed_full_height_reset.py'
AUTHOR = 'repro/results/research-mixed-full-height-reset.json'
REPLAY = 'repro/results/research-mixed-full-height-reset-replay.json'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def cover(codes):
    assert codes == sorted(codes) and len(codes) == len(set(codes))
    assert all(set(c) <= {'0', '1'} for c in codes)
    assert all(not b.startswith(a) for a, b in zip(codes, codes[1:]))
    assert sum((F(1, 2**len(c)) for c in codes), F(0)) == 1


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path,
                        default=ROOT/'repro/results/research-mixed-extracted-plateau-curvature.json')
    args = parser.parse_args()
    ph, sh = sha(PROOF), sha(__file__)
    deps, traversed = {}, set()

    def bind(path, expected=None):
        digest = sha(ROOT/path)
        if expected is not None:
            assert digest == expected, path
        if path in deps:
            assert deps[path] == digest, path
        deps[path] = digest
        return digest

    def inherited(path):
        bind(path)
        record = json.loads((ROOT/path).read_text())
        if path in traversed:
            return record
        traversed.add(path)
        bindings = {}
        for key in ('dependencies', 'dependencies_sha256'):
            for p, digest in record.get(key, {}).items():
                if p in bindings:
                    assert bindings[p] == digest, (path, p)
                bindings[p] = digest
                bind(p, digest)
        # Traversal checks provenance only, not theorem status of diagnostics.
        for p in bindings:
            if p.startswith('repro/results/') and p.endswith('.json'):
                inherited(p)
        return record

    for p in (SOURCE_PROOF, SOURCE_SCRIPT,
              'notes/research_mixed_nonlow_occupation_loss.md',
              'notes/research_mixed_nonlow_weighted_transfer.md',
              'notes/research_mixed_nonlow_open_chain_boundary.md',
              'notes/research_mixed_early_plateau_clusters.md'):
        bind(p)
    author, replay = inherited(AUTHOR), inherited(REPLAY)
    expected = list(itertools.product((0, 1), (0, 1), range(4), range(4)))
    checks = []

    def check(name, value):
        assert value, name
        checks.append(name)

    for name, rec in (('author', author), ('independent saved replay', replay)):
        check(name+' passed with current proof and script',
              rec['status'] == 'passed'
              and rec['proof_sha256'] == deps[SOURCE_PROOF]
              and rec['script_sha256'] == deps[SOURCE_SCRIPT])
        check(name+' has all ordered typed boundary domains',
              [tuple(row['case']) for row in rec['cases']] == expected
              and rec['domains'] == 64)
        check(name+' uses the full unselected rectangles',
              rec['parameter_rectangles'] == {
                  '0': ['.22', '.50', '-.03', '.02'],
                  '1': ['.22', '.50', '-.057', '0']})
        for row in rec['cases']:
            cover([leaf['address'] for leaf in row['leaves']])
            for leaf in row['leaves']:
                w = leaf['witness']
                assert len(w['center']) == len(w['derivatives']) == 2
                assert all(len(d) == 2 for d in w['derivatives'])
                assert F(w['radius']) > 0
                for v in w['center']+[q for d in w['derivatives'] for q in d]:
                    F(v)
        check(name+' has exactly36325 complete leaves',
              sum(len(row['leaves']) for row in rec['cases']) == rec['cells'] == 36325)
    check('independent320 binds the immutable author record',
          author['precision_bits'] == 256 and replay['precision_bits'] == 320
          and replay['input_sha256'] == deps[AUTHOR])
    check('same exact rational witness and coverage list in both computations',
          all(a['leaves'] == b['leaves'] for a, b in zip(author['cases'], replay['cases'])))

    d256 = F(author['min_negative_real_hessian_eigenvalue'])
    d320 = F(replay['min_negative_real_hessian_eigenvalue'])
    check('exact recorded outward author minimum', d256 == F('0.20212584175169467926025390625'))
    check('exact recorded outward replay minimum', d320 == F('0.2021258436143398284912109375'))
    local, cyclic, occupation = F(1, 5), F(2, 5), F(1, 4000)
    check('both whole-cell minima exceed one fifth', min(d256, d320) > local)
    check('two original cyclic incidences give two fifths', 2*local == cyclic)
    check('real Taylor loss per endpoint is one tenth', local/2 == F(1, 10))
    check('clean unselected curvature pays the new penalty', F(1, 10)/400 == occupation)
    check('selected clean edge pays the new penalty', F(1, 100) > occupation)
    check('removed right selection still pays its original unit penalty', F(6, 100)**2/10 > occupation)
    reserve = F(1, 100)-F(33651, 2000000)/2
    check('retain the exact unrounded early reserve', reserve == F(6349, 4000000))
    check('at most five early-neighborhood penalties are paid',
          reserve-5*occupation == F(1349, 4000000) > 0)
    check('both curvature and occupation improve by factor800',
          cyclic/F(1, 2000) == occupation/F(1, 3200000) == 800)
    check('old cost estimate remains unchanged',
          author['matrix_cost_upper'] == replay['matrix_cost_upper'] == 20
          and author['integrated_cost_upper'] == replay['integrated_cost_upper'] == 10)

    assert ph == sha(PROOF) and sh == sha(__file__)
    assert all(sha(ROOT/p) == digest for p, digest in deps.items())
    result = dict(status='passed', exact_checks=len(checks), checks=checks,
                  author_record=AUTHOR, independent_replay_record=REPLAY,
                  validated_boundary_products=64, validated_saved_cells=36325,
                  numerical_cells_recomputed=0,
                  recorded_author_lower=str(d256), recorded_replay_lower=str(d320),
                  local_hessian_lower=str(local), cyclic_hessian_lower=str(cyclic),
                  local_taylor_coefficient='1/10', occupation_coefficient=str(occupation),
                  early_reserve=str(reserve), unused_early_reserve='1349/4000000',
                  source_scope='Whole accepted boxes, original logarithmic root, same complete saved witnesses at256 and320 bits; extraction is not a fresh numerical replay.',
                  proof_sha256=ph, script_sha256=sh, dependencies_sha256=deps,
                  scope='Unselected U3/U4 Hessian and stronger occupation/weighted-support corollaries on the previously proved hybrid domain; no whole-invariant or lower-bound claim.')
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print('PASS', len(checks), 'exact checks;', 64, 'products;', 36325,
          'existing cells;', len(deps), 'current bindings; no numerical rerun', flush=True)


if __name__ == '__main__':
    main()
