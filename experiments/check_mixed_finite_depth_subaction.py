#!/usr/bin/env python3
"""Exact relative-potential/gauge identities and current inputs; no cover."""
import argparse
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / 'notes/research_mixed_finite_depth_subaction.md'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output', type=Path, default=ROOT /
                    'repro/results/research-mixed-finite-depth-subaction.json')
    args = ap.parse_args()
    ph, sh = sha(PROOF), sha(__file__)
    dependencies, visited, checks = {}, set(), []

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

    def inherit(path):
        bind(path)
        record = json.loads((ROOT / path).read_text())
        if path in visited:
            return record
        visited.add(path)
        bindings = {}
        for field in ('dependencies', 'dependencies_sha256'):
            for name, digest in record.get(field, {}).items():
                if name in bindings:
                    assert bindings[name] == digest, (path, name)
                bindings[name] = digest
                bind(name, digest)
        # Recursion validates provenance only, including any archived
        # diagnostic bindings. No diagnostic is promoted to a theorem.
        for name in bindings:
            if name.startswith('repro/results/') and name.endswith('.json'):
                inherit(name)
        return record

    primary = []
    for stem in ('mixed_finite_depth_boundary_potential',
                 'mixed_extracted_plateau_curvature'):
        pp, ss = f'notes/research_{stem}.md', f'experiments/check_{stem}.py'
        rp = f'repro/results/research-{stem.replace("_", "-")}.json'
        r = inherit(rp)
        bind(pp)
        bind(ss)
        check(stem+' passed with current proof and code',
              r['status'] == 'passed' and r['proof_sha256'] == dependencies[pp]
              and r['script_sha256'] == dependencies[ss])
        primary.append((rp, r))
    potential, curvature = primary[0][1], primary[1][1]
    check('completed quadratic cut theorem retains all needed coefficients',
          potential['exact_checks'] == 31
          and potential['numerical_cells_recomputed'] == 0
          and F(potential['occupation_coefficient']) == F(1, 4000)
          and potential['prefix_quadratic_coefficient'] == 30
          and potential['suffix_quadratic_coefficient'] == 10
          and potential['total_quadratic_coefficient'] == 40)
    check('source lower and upper constants are unchanged',
          F(potential['local_lower']) == F(curvature['local_hessian_lower']) == F(1, 5)
          and F(potential['local_upper']) == 20
          and curvature['validated_boundary_products'] == 64
          and curvature['validated_saved_cells'] == 36325)
    for stem in ('mixed_nonlow_interface_reduction',
                 'mixed_nonlow_open_chain_boundary',
                 'mixed_nonlow_occupation_loss'):
        bind(f'notes/research_{stem}.md')

    theta, a, b, c, K, Psi, e = sp.symbols('theta a b c K Psi e', positive=True)
    d0, d1, d2 = sp.symbols('d0 d1 d2', real=True)
    Bprev = theta*(a/6+b/3)
    Bnext = theta*(b/6+c/3)
    symshare = theta*(a+b)/2
    check('gauge changes symmetric shares to the entire output triple',
          sp.expand(symshare+Bnext-Bprev-theta*(a+b+c)/3) == 0)
    Vh, Vh1, B = sp.symbols('Vh Vh1 B', real=True)
    check('the gauge leaves successive incoming-depth increments unchanged',
          sp.expand((Vh1+B)-(Vh+B)-(Vh1-Vh)) == 0)
    check('three cyclic occupation incidences preserve the original total share',
          3*sp.Rational(1, 3) == 1)
    for m in (1, 2):
        z = sp.symbols('z0:'+str(m))
        lhs = sum(z[(j-1) % m]+z[j]+z[(j+1) % m] for j in range(m))
        check(f'literal period{m} output incidences count each occupation three times',
              sp.expand(lhs-3*sum(z)) == 0)

    kappa = F(1, 4000)
    check('near-reference occupation coefficient is one tenth', 400*kappa == F(1, 10))
    entry = 10*(2*d0*d0+d1*d1)
    exit_ = 10*(d1*d1+2*d2*d2)
    check('entry and exit use every displacement twice',
          sp.expand(entry+exit_-20*(d0*d0+d1*d1+d2*d2)) == 0)
    check('near-baseline closure-to-occupation ratio is200', F(20)/F(1, 10) == 200)
    check('large-occupation closure-to-occupation ratio is24000K', F(6)/kappa == 24000)
    check('maximum occupation of a triple is63/4000',
          3*(kappa+F(1, 200)) == F(63, 4000))
    check('relative good radius stays below1/40',
          F(63, 4000)/40 == F(63, 160000) < F(1, 1600))
    check('a bad symbol costs e times terminal occupation over400',
          sp.simplify((e*Psi/40)/10-e*Psi/400) == 0)
    C = sp.symbols('C', positive=True)
    check('terminal occupation cancels from the bad-count bound',
          sp.simplify(((C+1)*Psi/(1-theta))/(e*Psi/400)
                      -400*(C+1)/((1-theta)*e)) == 0)
    check('quadratic cut has exactly the desired relative error',
          sp.expand(40*(e*Psi/40)-e*Psi) == 0)

    M, k = sp.symbols('M k', integer=True, positive=True)
    first, last, h = -5*M-2, -3, 5*M+3
    cut = first+5*k+2
    check('five-good search excludes the final triple and uses exactly5M positions',
          sp.expand(last-first+1-5*M) == 0
          and sp.expand(first-(-h+1)) == 0)
    check('cut after third retains between5 and5M appended suffix symbols',
          sp.simplify((-cut).subs(k, 0)-5*M) == 0
          and sp.simplify((-cut).subs(k, M-1)-5) == 0)
    check('theta/6 error leaves theta/6 original local loss',
          sp.simplify(theta/3-theta/6-theta/6) == 0)
    check('cyclic local loss is theta/2 times original occupation',
          sp.simplify(3*theta/6-theta/2) == 0)
    check('theta one half has exact error and retained share one twelfth',
          F(1, 2)/6 == F(1, 12))
    check('theta one half bad-count factor is9600',
          F(400)/((1-F(1, 2))*F(1, 12)) == 9600)
    check('theta one half cyclic retained fraction is one quarter',
          3*F(1, 12) == F(1, 4))

    assert ph == sha(PROOF) and sh == sha(__file__)
    assert all(sha(ROOT/p) == digest for p, digest in dependencies.items())
    result = dict(
        status='passed', exact_checks=len(checks), checks=checks,
        primary_records=len(primary), current_bindings=len(dependencies),
        numerical_cells_recomputed=0, cyclic_word_samples=0,
        local_closure_ratio=200, global_closure_ratio_per_K=24000,
        state_relative_bad_count='400*(C_theta+1)/((1-theta)*e)',
        depth='5*(floor(state_relative_bad_count)+1)+3',
        relative_error='e*Psi', gauge='theta*(omega_second/6+omega_third/3)',
        exact_original_local_loss='theta*Psi_output/6',
        exact_original_cyclic_fraction='theta/2',
        numerical_depth_evaluated=False, interface_sign_certified=False,
        proof_sha256=ph, script_sha256=sh, dependencies_sha256=dependencies,
        scope='Exact gauge, relative-depth and incidence identities with current proved inputs. No numerical optimization, new cover, evaluated interface sign, full-period asymptotic or knot claim.')
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print('PASS', len(checks), 'exact checks;', len(primary), 'primary records;',
          len(dependencies), 'current bindings; no numerical cover', flush=True)


if __name__ == '__main__':
    main()
