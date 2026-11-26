#!/usr/bin/env python3
"""Check the low-coordinate identities and existing source provenance."""
import argparse
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / 'notes/research_mixed_deep_low_half_region.md'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path,
                        default=ROOT / 'repro/results/research-mixed-deep-low-half-region.json')
    args = parser.parse_args()
    ph, sh = sha(PROOF), sha(__file__)
    deps, visited, checks = {}, set(), []

    def check(name, value):
        assert value, name
        checks.append(name)

    def bind(path, expected=None):
        digest = sha(ROOT / path)
        if expected is not None:
            assert digest == expected, path
        if path in deps:
            assert deps[path] == digest, path
        deps[path] = digest
        return digest

    def inherit(path):
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
        for name in bindings:
            if name.startswith('repro/results/') and name.endswith('.json'):
                inherit(name)
        return record

    stems = (
        'mixed_half_endpoint_conditional_packet',
        'mixed_full_nonlow_half_region',
        'mixed_split_cutoff_hybrid_contour',
        'mixed_fourier_weight_continuation',
        'mixed_extracted_plateau_curvature',
    )
    records = {}
    for stem in stems:
        pp = f'notes/research_{stem}.md'
        ss = f'experiments/check_{stem}.py'
        rr = f'repro/results/research-{stem.replace("_", "-")}.json'
        bind(pp)
        bind(ss)
        rec = inherit(rr)
        inherited = {**rec.get('dependencies', {}),
                     **rec.get('dependencies_sha256', {})}
        check(stem + ': completed record with current proof and script',
              rec['status'] == 'passed'
              and rec['script_sha256'] == deps[ss]
              and rec.get('proof_sha256', inherited.get(pp)) == deps[pp])
        records[stem] = rec

    u, v, p, q = sp.symbols('u v p q', real=True)
    S = u+sp.I*v
    U = (S-sp.I)/(S+sp.I)
    A = (p-sp.I)/(p+sp.I)
    B = (q-sp.I)/(q+sp.I)
    identities = {
        'first shifted factorial ratio':
            (1-U*A)/(1-A)-(S+p)/(S+sp.I),
        'second shifted factorial ratio':
            (1-U*B)/(1-B)-(S+q)/(S+sp.I),
        'original chirp changes the first denominator':
            ((1-U*A)/(1-A))/U-(S+p)/(S-sp.I),
        'first squared modulus difference':
            (u+p)**2+v**2-u**2-(v-1)**2
            -(2*u*p+p**2+2*v-1),
        'second squared modulus difference':
            (u+q)**2+v**2-u**2-(v+1)**2
            -(2*u*q+q**2-2*v-1),
        'first positive decomposition':
            (2*u*p+p**2+2*v-1)
            -(2*u*p+(p**2-3)+2*(v+1)),
        'second positive decomposition':
            (2*u*q+q**2-2*v-1)
            -(2*u*q+(q**2-3)+2*(1-v)),
    }
    for name, expr in identities.items():
        check(name, sp.cancel(sp.expand(expr)) == 0)
    check('one-sixth cotangent threshold', sp.cot(sp.pi/6) == sp.sqrt(3))
    check('one-sixth factorial sign threshold', 2*sp.sin(sp.pi/6) == 1)
    check('low raising interval lies strictly below the threshold',
          F(0) < F(1, 1000) < F(1, 10) < F(1, 6))
    check('both row cutoffs vanish up to the raising endpoint',
          F(1, 10) < F(3, 25) < F(11, 50))
    t, w = sp.symbols('t w', nonnegative=True)
    check('a zero low incidence resets either neighboring minimum',
          sp.Min(0, t, w) == 0)
    check('raising below one tenth preserves the plateau clamp',
          max(F(11, 50), F(1, 10)) == F(11, 50))
    check('raising below one tenth cannot change right overshoot',
          F(1, 10) < F(9, 20))

    endpoint = records['mixed_half_endpoint_conditional_packet']
    check('closed half-endpoint source retains both level parities',
          endpoint['exact_even_odd_row_support_checks'] == 54
          and endpoint['exact_physical_half_endpoint_comparisons'] == 30)
    curve = records['mixed_extracted_plateau_curvature']
    check('occupation coefficient is supplied by the existing extraction',
          F(curve['occupation_coefficient']) == F(1, 4000)
          and curve['validated_boundary_products'] == 64
          and curve['validated_saved_cells'] == 36325
          and curve['numerical_cells_recomputed'] == 0)
    check('left off-plateau displacement pays a full unit penalty',
          400*(F(27, 100)-F(11, 50))**2 == 1)
    check('right off-plateau displacement pays a full unit penalty',
          400*(F(9, 20)-F(39, 100))**2 > 1)
    check('total finite-source tolerance leaves the asserted gap',
          F(1, 4000)-F(1, 8000) == F(1, 8000))
    for eta in (0, 1):
        for eps in (0, 1):
            check(f'allocated source power for type pair {eta}{eps}',
                  -F(1+eps, 2)-F(eta+eps, 4)
                  == -F(2+eta+3*eps, 4))

    assert ph == sha(PROOF) and sh == sha(__file__)
    assert all(sha(ROOT / path) == digest for path, digest in deps.items())
    result = dict(
        status='passed', exact_checks=len(checks), checks=checks,
        primary_records=len(stems), current_bindings=len(deps),
        symbolic_identity_count=len(identities), numerical_cells_recomputed=0,
        cyclic_pattern_enumerations=0, monotonicity_threshold='1/6',
        raising_endpoint='1/10', occupation_coefficient='1/4000',
        finite_gap='1/8000', proof_sha256=ph, script_sha256=sh,
        dependencies_sha256=deps,
        scope='Exact identities and existing source provenance for the written arbitrary-length restricted-integral theorem on [rho,1/2]^m with fixed positive hybrid collar rho. No assertion uniform as rho tends to zero, no seam or right-half estimate, and no whole-period or short-filling theorem.')
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print('PASS', len(checks), 'exact checks;', len(stems), 'primary records;',
          len(deps), 'current bindings; no numerical cover', flush=True)


if __name__ == '__main__':
    main()
