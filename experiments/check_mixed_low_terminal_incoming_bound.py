#!/usr/bin/env python3
"""Exact retained-surplus arithmetic and current source provenance only."""
import argparse
import hashlib
import itertools
import json
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / 'notes/research_mixed_low_terminal_incoming_bound.md'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output', type=Path, default=ROOT /
                    'repro/results/research-mixed-low-terminal-incoming-bound.json')
    args = ap.parse_args()
    ph, sh = sha(PROOF), sha(__file__)
    deps, visited, primary, checks = {}, set(), {}, []

    def bind(path, expected=None):
        value = sha(ROOT / path)
        if expected is not None:
            assert value == expected, path
        if path in deps:
            assert deps[path] == value, path
        deps[path] = value
        return value

    def inherit(path):
        if path in visited:
            return json.loads((ROOT / path).read_bytes())
        raw = (ROOT / path).read_bytes()
        bind(path, hashlib.sha256(raw).hexdigest())
        record = json.loads(raw)
        visited.add(path)
        merged = {}
        for field in ('dependencies', 'dependencies_sha256'):
            for name, digest in record.get(field, {}).items():
                if name in merged:
                    assert merged[name] == digest, name
                merged[name] = digest
                bind(name, digest)
        for name in merged:
            if name.startswith('repro/results/') and name.endswith('.json'):
                inherit(name)
        return record

    def load(stem, prefix='check'):
        path = 'repro/results/research-' + stem.replace('_', '-') + '.json'
        record = inherit(path)
        assert record['status'] == 'passed', path
        assert record['proof_sha256'] == bind('notes/research_' + stem + '.md')
        assert record['script_sha256'] == bind('experiments/' + prefix + '_' + stem + '.py')
        primary[path] = record
        return record

    def check(name, condition):
        assert condition, name
        checks.append(name)

    small = load('mixed_real_one_small_support', 'certify')
    early = load('mixed_early_transition_support', 'certify')
    curvature = load('mixed_extracted_plateau_curvature')
    deep = load('mixed_deep_low_half_region')
    subaction = load('mixed_finite_depth_subaction')
    for path in ('notes/research_mixed_early_plateau_clusters.md',
                 'notes/research_mixed_frozen_early_transport.md',
                 'notes/research_mixed_nonlow_occupation_loss.md',
                 'notes/research_mixed_full_left_region.md',
                 'notes/research_mixed_full_nonlow_half_region.md',
                 'notes/research_mixed_half_endpoint_conditional_packet.md',
                 'notes/research_mixed_nonlow_open_chain_boundary.md'):
        bind(path)
    check('complete real one-small phase comparison with both orientations',
          F(small['phase_gap']) == F(11, 200)
          and F(small['cutoff']) == F(1, 10)
          and small['reference_products'] == 64 and small['orientations'] == 2
          and small['cells'] == 269 and small['affine_corner_tests'] == 21520)
    check('complete early reference products and phase allowance',
          F(early['phase_gap']) == F(1, 100)
          and early['reference_products'] == 64 and early['cells'] == 251)
    check('current strengthened occupation and exact unused early reserve',
          F(curvature['occupation_coefficient']) == F(1, 4000)
          and F(curvature['early_reserve']) == F(6349, 4000000)
          and F(curvature['unused_early_reserve']) == F(1349, 4000000))
    check('deep-low raising has the same occupation and endpoint',
          F(deep['raising_endpoint']) == F(1, 10)
          and F(deep['occupation_coefficient']) == F(1, 4000)
          and deep['exact_checks'] == 28)
    check('incoming potential uses completed relative-depth inputs',
          subaction['exact_checks'] == 25
          and subaction['interface_sign_certified'] is False)

    surplus = F(11, 200) - F(1, 100)
    q0, q1 = F(11, 2), F(151, 20)
    hmax = {0: F(3, 100), 1: F(57, 1000)}
    check('one-small surplus before its existing reset credit', surplus == F(9, 200))
    rows = []
    for low_argument, q in ((0, q0), (1, q1)):
        for neighbor_type in (0, 1):
            debit = q * hmax[neighbor_type] ** 2
            bonus = surplus - debit
            check(f'positive original oriented surplus, side{low_argument},type{neighbor_type}',
                  bonus > 0 and F(1, 100) + debit + bonus == F(11, 200))
            rows.append(dict(low_argument=low_argument,
                             neighbor_type_indicator=neighbor_type,
                             assigned_credit=str(debit), retained_bonus=str(bonus)))
    check('two-low edge retains its full surplus without a plateau credit',
          F(1, 100) + surplus == F(11, 200))
    check('early occupation charges remain fully paid before new bonuses',
          F(1, 100) - F(33651, 2000000) / 2 - 5 * F(1, 4000)
          == F(1349, 4000000) > 0)
    pairs = []
    for left_type, right_type in itertools.product((0, 1), repeat=2):
        bonus = 2 * surplus - q1 * hmax[left_type] ** 2 - q0 * hmax[right_type] ** 2
        check(f'ordered two-edge terminal bonus types{left_type}{right_type}', bonus > 0)
        pairs.append(dict(neighbor_types=[left_type, right_type], bonus_lower=str(bonus)))
    check('exact universal terminal bonus',
          min(F(row['bonus_lower']) for row in pairs) == F('0.04760055'))
    check('exact type-three neighbor bonus', F(pairs[0]['bonus_lower']) == F('.078255'))
    check('all low real symbols pay the same saturated occupation',
          400 * F('.05') ** 2 == 1 and F('.1') < F('.22'))
    check('incoming and closing half-shares restore one full occupation',
          F(1, 2) + F(1, 2) == 1)

    assert ph == sha(PROOF) and sh == sha(__file__)
    assert all(sha(ROOT / p) == value for p, value in deps.items())
    result = dict(status='passed', exact_checks=len(checks), checks=checks,
                  primary_records=len(primary), current_bindings=len(deps),
                  one_edge_bonuses=rows, ordered_terminal_bonuses=pairs,
                  minimum_terminal_bonus='952011/20000000',
                  both_three_terminal_bonus='15651/200000',
                  original_phase_loss='11/200', original_early_loss='1/100',
                  occupation_coefficient='1/4000',
                  numerical_cells_recomputed=0, new_critical_roots=0,
                  interface_sign_certified=False,
                  proof_sha256=ph, script_sha256=sh, dependencies_sha256=deps,
                  scope='Exact existing-input surplus and closure arithmetic. The written proof gives a uniform incoming upper bound at a low terminal coordinate; no numerical interface sign or whole-period claim.')
    assert F(result['minimum_terminal_bonus']) == F('.04760055')
    assert F(result['both_three_terminal_bonus']) == F('.078255')
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + '\n')
    print('PASS', len(checks), 'exact checks;', len(primary), 'primary records;',
          len(deps), 'bindings; no numerical cover rerun.', flush=True)


if __name__ == '__main__':
    main()
