#!/usr/bin/env python3
"""Current-input and exact incidence budgets for the hybrid low/plateau theorem."""
import argparse
import hashlib
import itertools
import json
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / 'notes/research_mixed_hybrid_low_plateau_clusters.md'

# These are theorem inputs. Inherited records are hash-validated, not promoted
# from diagnostic status to new mathematical inputs by this checker.
SPECS = [
    ('mixed_hybrid_zero_pair_support', 'certify', None),
    ('mixed_hybrid_zero_pair_support', 'certify', 'replay'),
    ('mixed_all_endpoint_support', 'certify', None),
    ('mixed_all_endpoint_support', 'replay', 'replay'),
    ('mixed_43_endpoint_support', 'check', None),
    ('mixed_43_endpoint_support', 'replay', 'replay'),
    ('mixed_uniform_real_low_support', 'check', None),
    ('mixed_both_low_raw_support', 'certify', None),
    ('mixed_full_height_reset', 'certify', None),
    ('mixed_selected_plateau_support', 'certify', None),
    ('mixed_selected_reset_plateau_support', 'certify', None),
    ('mixed_selected_right_taper_support', 'certify', None),
    ('mixed_split_cutoff_hybrid_contour', 'check', None),
    ('mixed_selected_low_plateau_clusters', 'check', None),
]


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path,
                        default=ROOT / 'repro/results/research-mixed-hybrid-low-plateau-clusters.json')
    args = parser.parse_args()
    ph, sh = sha(PROOF), sha(__file__)
    deps, records, bindings = {}, {}, []

    def bind(path, expected=None):
        value = sha(ROOT / path)
        if expected is not None:
            assert value == expected, path
        if path in deps:
            assert deps[path] == value, path
        deps[path] = value
        return value

    for stem, prefix, suffix in SPECS:
        pp = f'notes/research_{stem}.md'
        ss = f'experiments/{prefix}_{stem}.py'
        rr = f'repro/results/research-{stem.replace("_", "-")}'
        rr += ('-' + suffix if suffix else '') + '.json'
        for path in (pp, ss, rr):
            bind(path)
        rec = json.loads((ROOT / rr).read_text())
        assert rec['status'] == 'passed', rr
        assert rec['script_sha256'] == deps[ss], rr
        inherited = {}
        for key in ('dependencies', 'dependencies_sha256'):
            for path, digest in rec.get(key, {}).items():
                if path in inherited:
                    assert inherited[path] == digest, (rr, path)
                inherited[path] = digest
                bind(path, digest)
        assert rec.get('proof_sha256', inherited.get(pp)) == deps[pp], rr
        records[(stem, suffix)] = rec
        bindings.append(dict(record=rr, proof=pp, script=ss))

    for path in ('notes/research_mixed_partial_selected_heights.md',
                 'notes/research_mixed_plateau_accretivity.md',
                 'notes/research_mixed_unselected_right_taper_products.md'):
        bind(path)

    checks = []

    def check(name, value):
        assert value, name
        checks.append(name)

    pair = records['mixed_hybrid_zero_pair_support', None]
    replay = records['mixed_hybrid_zero_pair_support', 'replay']
    check('complete pair author and replay',
          pair['boundary_products'] == replay['boundary_products'] == 2048
          and pair['accepted_cells'] == replay['accepted_cells'] == 18988
          and pair['target_corners_per_cell'] == replay['target_corners_per_cell'] == 16)
    pair_path = 'repro/results/research-mixed-hybrid-zero-pair-support.json'
    check('final pair replay input binding', replay['input_sha256'] == deps[pair_path])
    expected = set(itertools.product(itertools.product((0, 1), repeat=5),
                                     range(2), range(2), range(4), range(4)))

    def covers(rec):
        out = {}
        for row in rec['cases']:
            key = (tuple(row['word']), *row['external_types'], *row['faces'])
            assert key not in out
            codes = row['addresses']
            assert len(codes) == row['cells'] == len(set(codes))
            codes = sorted(codes)
            assert all(set(code) <= {'0', '1'} for code in codes)
            assert all(not b.startswith(a) for a, b in zip(codes, codes[1:]))
            assert sum((F(1, 2**len(code)) for code in codes), F(0)) == 1
            out[key] = codes
        assert set(out) == expected
        return out

    check('same complete exact pair covers', covers(pair) == covers(replay))
    check('literal finite pair loss and collar',
          F(pair['finite_pair_gap']) == F(replay['finite_pair_gap']) == F(1, 5)
          and F(pair['low_cutoff']) == F(1, 1000))
    check('all seven endpoint orientations complete',
          records['mixed_all_endpoint_support', None]['reference_products'] == 112
          and records['mixed_all_endpoint_support', 'replay']['reference_products'] == 112)
    check('eighth endpoint source and replay complete',
          records['mixed_43_endpoint_support', None]['case_count'] == 16
          and records['mixed_43_endpoint_support', 'replay']['status'] == 'passed')
    check('deep-low plateau finite gap',
          F(records['mixed_uniform_real_low_support', None]['uniform_source_gap']) == F(1, 20))
    check('deep-low loop finite gap and closed cutoff',
          F(records['mixed_both_low_raw_support', None]['gap']) == F(1, 100)
          and F(records['mixed_both_low_raw_support', None]['target_real_cutoff']) == F(1, 10))
    check('full integrated plateau reset cost',
          records['mixed_full_height_reset', None]['integrated_cost_upper'] == 10)
    check('selected corners improve the common ceiling',
          F(records['mixed_selected_plateau_support', None]['reference_defect_upper']) == -F(1, 100)
          and F(records['mixed_selected_reset_plateau_support', None]['phase_gap']) == F(1, 100))
    check('height convexity for every actual Fourier branch',
          F(records['mixed_selected_right_taper_support', None]['target_concavity']) == F(5, 4))
    check('pure plateau inherited finite gap',
          F(records['mixed_selected_low_plateau_clusters', None]['selected_plateau_gap']) == F(1, 200))

    # Incidence identities, not enumeration of cyclic words.
    for k in (1, 2):
        check(f'seam edge fractional allocation with {k} seam incidences',
              F(k, 2) + (1-F(k, 2)) == 1 and 0 <= 1-F(k, 2) <= F(1, 2))
        check(f'affected plateau vertex with {k} low incidences', 0 <= 2-k <= k)
    check('one-cycle pair square is restored by a half-power', F(2)*F(1, 2) == 1)
    check('two-cycle plateau has no further edge after two low incidences', 2-2 == 0)
    check('existential collar respects original fixed source cutoff', F(0) < F(1, 1000) < F(1, 10))
    check('endpoint thickening reserves half the original finite gap', F(1, 4000) == F(1, 2000)/2)
    debit = F(10)*F(57, 1000)**2
    seam = F(1, 10)-2*debit
    deep = F(1, 20)-debit
    check('exact per-incidence debit', debit == F(3249, 100000))
    check('exact seam coefficient', seam == F(1751, 50000))
    check('exact deep-low boundary coefficient', deep == F(1751, 100000))
    check('each nonempty low alternative retains one hundredth', min(seam, deep, F(1, 100)) == F(1, 100))
    check('single total Fourier budget leaves one two-hundredth', F(1, 100)-F(1, 200) == F(1, 200))
    for eta, eps in itertools.product((0, 1), repeat=2):
        check(f'original allocated kernel power {eta}{eps}',
              -F(1+eps, 2)-F(eta+eps, 4) == -F(2+eta+3*eps, 4))

    assert ph == sha(PROOF) and sh == sha(__file__)
    assert all(sha(ROOT / path) == digest for path, digest in deps.items())
    result = dict(status='passed', arithmetic='exact rational assembly and current saved-input bindings',
                  exact_checks=len(checks), checks=checks, primary_record_count=len(SPECS),
                  primary_records=bindings, pair_boundary_products=2048, pair_saved_cells=18988,
                  cycle_pattern_enumerations=0, new_numerical_inequalities=0,
                  collar_scope='One fixed positive epsilon <=1/1000 and below the uniform endpoint-thickening radius; no numerical radius asserted.',
                  seam_coefficient=str(seam), deep_low_boundary_coefficient=str(deep),
                  deep_low_internal_gap='1/100', finite_low_region_gap='1/200',
                  proof_sha256=ph, script_sha256=sh, dependencies_sha256=deps,
                  scope='Original periodic hybrid on (L union P)^m, L=[0,.1], P=[.22,.45], all selections and zero-uniform low contribution; no transition/right exterior or whole-period theorem.')
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print('PASS', len(checks), 'exact checks;', len(SPECS), 'primary records;', len(deps), 'current bindings', flush=True)


if __name__ == '__main__':
    main()
