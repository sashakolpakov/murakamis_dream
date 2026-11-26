#!/usr/bin/env python3
"""Check exact forgetting constants and completed source provenance; no cover."""
import argparse
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / 'notes/research_mixed_plateau_boundary_forgetting.md'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path,
                        default=ROOT / 'repro/results/research-mixed-plateau-boundary-forgetting.json')
    args = parser.parse_args()
    ph, sh = sha(PROOF), sha(__file__)
    dependencies, visited = {}, set()
    checks = []

    def check(name, value):
        assert value, name
        checks.append(name)

    def bind(path, expected=None):
        digest = sha(ROOT / path)
        if expected is not None:
            assert digest == expected, path
        if path in dependencies:
            assert dependencies[path] == digest, path
        dependencies[path] = digest
        return digest

    def inherited(path):
        bind(path)
        record = json.loads((ROOT / path).read_text())
        if path in visited:
            return record
        visited.add(path)
        bindings = {}
        for key in ('dependencies', 'dependencies_sha256'):
            for name, digest in record.get(key, {}).items():
                if name in bindings:
                    assert bindings[name] == digest, (path, name)
                bindings[name] = digest
                bind(name, digest)
        # Recursive validation is of provenance, not a new theorem-status
        # assertion about every archived diagnostic in those manifests.
        for name in bindings:
            if name.startswith('repro/results/') and name.endswith('.json'):
                inherited(name)
        return record

    specs = [
        ('mixed_extracted_plateau_curvature', 'check', ''),
        ('mixed_type_four_height_refinement', 'certify', ''),
        ('mixed_type_four_height_refinement', 'replay', '-replay'),
    ]
    records = {}
    for stem, prefix, suffix in specs:
        pp = f'notes/research_{stem}.md'
        ss = f'experiments/{prefix}_{stem}.py'
        rr = f'repro/results/research-{stem.replace("_", "-")}{suffix}.json'
        bind(pp)
        bind(ss)
        record = inherited(rr)
        check(stem + suffix + ' passed with current proof and code',
              record['status'] == 'passed'
              and record['proof_sha256'] == dependencies[pp]
              and record['script_sha256'] == dependencies[ss])
        records[stem, suffix] = record

    curvature = records['mixed_extracted_plateau_curvature', '']
    author = records['mixed_type_four_height_refinement', '']
    replay = records['mixed_type_four_height_refinement', '-replay']
    check('curvature extraction retains the complete saved certificate',
          curvature['validated_boundary_products'] == 64
          and curvature['validated_saved_cells'] == 36325
          and curvature['numerical_cells_recomputed'] == 0)
    check('both extracted whole-cell lower endpoints exceed one fifth',
          F(curvature['recorded_author_lower']) > F(1, 5)
          and F(curvature['recorded_replay_lower']) > F(1, 5)
          and F(curvature['local_hessian_lower']) == F(1, 5))
    reset = json.loads((ROOT / curvature['author_record']).read_text())
    check('unchanged local upper Hessian input is20',
          reset['status'] == 'passed' and reset['matrix_cost_upper'] == 20)
    check('reference geometry includes both completed48-product records',
          author['case_count'] == replay['case_count'] == 48
          and author['accepted_cells'] == replay['accepted_cells'] == 249
          and replay['refinements'] == 0)
    geometry_author = 'repro/results/research-mixed-type-four-height-refinement.json'
    check('independent geometry replay binds its author record',
          replay['input_sha256'] == dependencies[geometry_author])
    check('typed reference rectangles and refined negative fourth height',
          author['rectangles'] == replay['rectangles'] == [
              ['3/10', '39/100', '-3/100', '1/50'],
              ['27/100', '33/100', '-57/1000', '-1/1000']]
          and F(author['upper_height']) == F(replay['upper_height']) == -F(1, 50))

    local, L = F(1, 5), F(20)
    mu, Lambda = 2*local, 2*L
    alpha = 2/(Lambda+mu)
    q = (Lambda-mu)/(Lambda+mu)
    q0 = 1-mu/Lambda
    check('two original incidences give the interior lower and upper bounds',
          mu == F(2, 5) and Lambda == 40)
    check('optimal projected-gradient step', alpha == F(5, 101))
    check('optimal Euclidean contraction factor', q == F(99, 101) and 0 < q < 1)
    check('both extremal Hessian directions have that contraction',
          1-alpha*mu == q and 1-alpha*Lambda == -q)
    check('objective-contraction step has factor99/100', q0 == F(99, 100))
    check('quadratic comparison cancels the squared-distance remainder',
          Lambda*(mu/Lambda)**2-mu*(mu/Lambda) == 0)
    lo, hi, alo, ahi = F('.22'), F('.45'), F('.27'), F('.39')
    margin = min(alo-lo, hi-ahi)
    displacement = max(hi-alo, ahi-lo)
    check('all reference real coordinates have uniform margin1/20', margin == F(1, 20))
    check('one endpoint displacement is at most9/50', displacement == F(9, 50))
    C = F(9, 5)
    check('reference-energy initial norm bound is9/5',
          (L/mu)*2*displacement**2 == C**2)
    check('the variational initial norm bound remains valid separately',
          L*2*displacement/mu == 18)
    coefficient = Lambda*C**2/2
    check('inactive-tail action coefficient is324/5', coefficient == F(324, 5))
    check('depth295 is beyond the uniform inactive-tail threshold', C*q**295 < margin)
    check('depth295 action error is less than1/2000', coefficient*q**590 < F(1, 2000))
    check('depth315 is beyond the same inactive-tail threshold', C*q**315 < margin)
    check('depth315 action error is less than1/4000', coefficient*q**630 < F(1, 4000))
    check('two boundary windows have590 or630 free coordinates',
          2*295 == 590 and 2*315 == 630)
    check('cross-end interaction coefficient is1000', L**2/mu == 1000)

    assert ph == sha(PROOF) and sh == sha(__file__)
    assert all(sha(ROOT/name) == digest for name, digest in dependencies.items())
    result = dict(
        status='passed', exact_checks=len(checks), checks=checks,
        primary_records=len(specs), current_bindings=len(dependencies),
        numerical_cells_recomputed=0, chain_lengths_enumerated=0,
        local_lower=str(local), local_upper=str(L),
        interior_lower=str(mu), interior_upper=str(Lambda),
        optimal_step=str(alpha), norm_contraction=str(q),
        objective_contraction=str(q0), uniform_initial_norm=str(C),
        uniform_inactive_tail_coefficient=str(coefficient),
        certified_windows=[dict(depth=295, total_free_coordinates=590,
                                action_error_less_than='1/2000'),
                           dict(depth=315, total_free_coordinates=630,
                                action_error_less_than='1/4000')],
        cross_end_coefficient='1000',
        proof_sha256=ph, script_sha256=sh, dependencies_sha256=dependencies,
        scope='Exact constants and completed input provenance for the written arbitrary-length fixed-height unselected plateau variational theorem. No fresh Hessian cover, finite-source asymptotic, selected-height or changed-contour assertion.')
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print('PASS', len(checks), 'exact checks;', len(specs), 'primary records;',
          len(dependencies), 'current bindings; no numerical cover', flush=True)


if __name__ == '__main__':
    main()
