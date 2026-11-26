#!/usr/bin/env python3
"""Check the isolated-gap obstruction and endpoint incidence identities.

This does not certify the open derivative hypothesis for the other vertices.
"""
import argparse
import hashlib
import importlib.util
import itertools
import json
from fractions import Fraction as F
from pathlib import Path
from flint import acb, arb, ctx

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT/'notes/research_mixed_frozen_early_transport.md'
HELPER = ROOT/'experiments/certify_mixed_real_small_support.py'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--precision', type=int, default=256)
    p.add_argument('--output', type=Path, default=ROOT/'repro/results/research-mixed-frozen-early-transport.json')
    args = p.parse_args()
    assert args.precision >= 128
    ctx.prec = args.precision
    spec = importlib.util.spec_from_file_location('frozen_early_roots', HELPER)
    core = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(core)
    core.pi, core.ii = arb.pi(), acb(0, 1)
    ph, sh = sha(PROOF), sha(__file__)
    dependencies = {str(HELPER.relative_to(ROOT)): sha(HELPER)}
    for stem, prefix in [('early_plateau_clusters', 'check'),
                         ('early_selected_source_cap', 'certify'),
                         ('selected_minimum_flow_obstruction', 'check')]:
        proof = 'notes/research_mixed_'+stem+'.md'
        script = 'experiments/'+prefix+'_mixed_'+stem+'.py'
        result = 'repro/results/research-mixed-'+stem.replace('_', '-')+'.json'
        for path in (proof, script, result):
            dependencies[path] = sha(ROOT/path)
        rec = json.loads((ROOT/result).read_text())
        assert rec['status'] == 'passed'
        assert rec['proof_sha256'] == dependencies[proof]
        assert rec['script_sha256'] == dependencies[script]
        for field in ('dependencies', 'dependencies_sha256'):
            assert all(sha(ROOT/path) == h for path, h in rec.get(field, {}).items())
    path = 'notes/research_mixed_early_selected_transport.md'
    dependencies[path] = sha(ROOT/path)
    low, middle = acb(core.ar(F(1, 10))), acb(core.ar(F(219, 1000)))
    left = core.point_root(low, middle, 1)
    right = core.point_root(middle, low, 0)
    assert left is not None and right is not None
    derivative = (core.phase(left[0], low, middle, 0, 1)[1][1]
                  +core.phase(right[0], middle, low, 1, 0)[1][0]).real
    assert derivative < core.ar(F(-3, 20))
    assert core.ar('-.158611') < derivative < core.ar('-.158610')
    assert core.g(middle).real < 0
    slow = lambda x: min(F(1), max(F(0), (x-F(1, 10))/F(3, 25)))
    fast = lambda x: min(F(1), max(F(0), (x-F(1, 10))/F(1, 50)))
    x = [F(1, 10), F(219, 1000), F(1, 10)]
    for j in range(3):
        near = [(j-1) % 3, j, (j+1) % 3]
        assert min(slow(x[k]) for k in near) == min(fast(x[k]) for k in near) == 0

    patterns = 0
    for m in range(1, 15):
        N = lambda j: {(j-1) % m, j, (j+1) % m}
        for bits in itertools.product((0, 1), repeat=m):
            B = {j for j in range(m) if bits[j] == 0}
            if not B:
                continue
            I = {j for j in range(m) if j not in B and (j-1) % m in B and (j+1) % m in B}
            A = set(range(m))-B-I
            for j in range(m):
                if not N(j) & B:
                    assert not N(j) & I
                if j not in B and (j+1) % m not in B:
                    assert j in A and (j+1) % m in A
            for j in A:
                assert not ((j-1) % m in B and (j+1) % m in B)
            patterns += 1
    assert patterns == 32752
    assert ph == sha(PROOF) and sh == sha(__file__)
    assert all(sha(ROOT/path) == h for path, h in dependencies.items())
    out = dict(status='passed', precision_bits=args.precision,
               obstruction_derivative=str(derivative), root_centers=[left[1], right[1]],
               incidence_patterns=patterns, proof_sha256=ph, script_sha256=sh,
               dependencies=dependencies,
               scope='Real3-4-3 obstruction to unrestricted raising, and exact isolated-position incidence identities. The Dirichlet derivative hypothesis remains open; no complete mixed-transition theorem.')
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(out, indent=2)+'\n')
    print('PASS', patterns, 'incidence patterns; isolated-gap derivative', derivative)


if __name__ == '__main__':
    main()
