#!/usr/bin/env python3
"""Exact incidence and reset budgets for the early/plateau assembly.

The arbitrary-length incidence proof is written in the note. Enumeration
checks short cycles and repeated incidences; it is not an induction proof.
"""
import argparse
import hashlib
import itertools
import json
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT/'notes/research_mixed_early_plateau_clusters.md'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=ROOT/'repro/results/research-mixed-early-plateau-clusters.json')
    args = parser.parse_args()
    ph, sh = sha(PROOF), sha(__file__)
    dependencies = {}
    sources = [
        ('early_transition_support', 'certify'),
        ('early_selected_source_cap', 'certify'),
        ('oriented_height_reset', 'certify'),
        ('full_height_reset', 'certify'),
        ('same_sign_height_reset', 'certify'),
        ('selected_plateau_support', 'certify'),
        ('selected_reset_plateau_support', 'certify'),
        ('selected_low_plateau_clusters', 'check'),
        ('coupled_outer_graph', 'check'),
        ('minimum_neighbor_contour', 'check'),
    ]
    for stem, prefix in sources:
        proof = 'notes/research_mixed_'+stem+'.md'
        script = 'experiments/'+prefix+'_mixed_'+stem+'.py'
        result = 'repro/results/research-mixed-'+stem.replace('_', '-')+'.json'
        for path in (proof, script, result):
            dependencies[path] = sha(ROOT/path)
        rec = json.loads((ROOT/result).read_text())
        assert rec['status'] == 'passed', result
        assert rec['proof_sha256'] == dependencies[proof]
        assert rec['script_sha256'] == dependencies[script]
        for field in ('dependencies', 'dependencies_sha256'):
            assert all(sha(ROOT/p) == h for p, h in rec.get(field, {}).items()), result
    for path in ('notes/research_mixed_partial_selected_heights.md',
                 'notes/research_mixed_early_selected_transport.md'):
        dependencies[path] = sha(ROOT/path)

    q = (F(11, 2), F(151, 20))
    height = {3: F(3, 100), 4: F(57, 1000)}
    fees = {}
    for u, v in itertools.product((3, 4), repeat=2):
        a2, b2 = height[u]**2, height[v]**2
        fee = F(0) if (u, v) == (4, 4) else (10-q[0])*a2+(10-q[1])*b2
        fees[str((u, v))] = str(fee)
    assert fees == {'(3, 3)': '1251/200000', '(3, 4)': '240201/20000000',
                    '(4, 3)': '33651/2000000', '(4, 4)': '0'}
    largest = max(F(v) for v in fees.values())
    reserve = F(1, 100)-largest/2
    assert reserve == F(6349, 4000000) and reserve > F(1, 1000)
    assert F(1, 1000)-F(1, 2000) == F(1, 2000)
    assert F(7, 500)*50 < F(57, 50)
    assert 1+F(57, 50)**2 < F(38, 25)**2

    patterns = 0
    doubles = 0
    for m in range(1, 15):
        for word in itertools.product((0, 1), repeat=m):
            # 0 is early; 1 is plateau. Edges keep cyclic multiplicity.
            early_edges = {i for i in range(m) if word[i] == 0 or word[(i+1) % m] == 0}
            mixed_edges = {i for i in range(m) if word[i] != word[(i+1) % m]}
            paid_by = {}
            double_count = 0
            for i in range(m):
                if not (word[i] == word[(i+1) % m] == 1):
                    continue
                credits = []
                if word[(i-1) % m] == 0:
                    credits.append((i-1) % m)
                if word[(i+2) % m] == 0:
                    credits.append((i+1) % m)
                assert len(set(credits)) == len(credits)
                for edge in credits:
                    assert edge in mixed_edges and edge not in paid_by
                    paid_by[edge] = i
                if len(credits) == 2:
                    double_count += 1
            assert 2*double_count <= len(mixed_edges) <= len(early_edges)
            assert -F(1, 100)*len(early_edges)+largest*double_count <= -reserve*len(early_edges)
            assert bool(early_edges) == (0 in word)
            patterns += 1
            doubles += double_count
    assert patterns == 32766
    assert ph == sha(PROOF) and sh == sha(__file__)
    assert all(sha(ROOT/p) == h for p, h in dependencies.items())
    out = dict(status='passed', source_records=len(sources), region_patterns=patterns,
               doubled_reset_blocks=doubles, exact_fees=fees, per_early_edge_reserve=str(reserve),
               phase_gap='1/1000', finite_gap='1/2000', proof_sha256=ph,
               script_sha256=sh, dependencies=dependencies,
               scope='Exact assembly on ([.1,.12] union [.22,.45])^m for all original Fourier selections; the written incidence proof covers arbitrary fixed m. No intervening-transition, low-endpoint, right-region or knot theorem.')
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(out, indent=2)+'\n')
    print('PASS', patterns, 'cyclic patterns, four exact reset fees,', len(sources), 'source records')


if __name__ == '__main__':
    main()
