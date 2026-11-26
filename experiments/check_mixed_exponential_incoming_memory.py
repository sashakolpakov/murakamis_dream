#!/usr/bin/env python3
"""Check exponential incoming-memory arithmetic and current proved inputs."""
import argparse
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / 'notes/research_mixed_exponential_incoming_memory.md'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output', type=Path, default=ROOT /
                    'repro/results/research-mixed-exponential-incoming-memory.json')
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
        for name in bindings:
            if name.startswith('repro/results/') and name.endswith('.json'):
                inherit(name)
        return record

    primary = []
    for stem in ('mixed_finite_depth_subaction',
                 'mixed_seam_boundary_potential_reduction'):
        pp = f'notes/research_{stem}.md'
        ss = f'experiments/check_{stem}.py'
        rp = 'repro/results/research-' + stem.replace('_', '-') + '.json'
        record = inherit(rp)
        bind(pp)
        bind(ss)
        check(stem + ' has current completed proof and code',
              record['status'] == 'passed'
              and record['proof_sha256'] == dependencies[pp]
              and record['script_sha256'] == dependencies[ss])
        primary.append(record)
    check('relative closure constants retained',
          primary[0]['local_closure_ratio'] == 200
          and primary[0]['global_closure_ratio_per_K'] == 24000)
    check('the prior result does not assert a numerical depth or interface sign',
          primary[0]['numerical_depth_evaluated'] is False
          and primary[0]['interface_sign_certified'] is False)

    a, C, eps, Psi = sp.symbols('a C eps Psi', positive=True)
    P, Q = sp.symbols('P Q', nonnegative=True)
    lam = 1-a/C
    check('backward recurrence is exactly the closed-prefix inequality',
          sp.simplify(a*P-C*(P-Q)-eps
                      -C*(Q-lam*P-eps/C)) == 0)
    check('geometric error denominator is a over C',
          sp.simplify(1-lam-a/C) == 0)
    check('occupation discrepancy bound at the terminal state',
          sp.simplify((C*Psi+eps)/a-(C*Psi/a+eps/a)) == 0)

    z = sp.symbols('z', nonnegative=True)  # Represents lambda**k.
    Rk = C*z*Psi/a+eps/a
    Rnext = C*lam*z*Psi/a+eps/a
    check('inductive exponential occupation estimate includes every epsilon term',
          sp.simplify(lam*Rk+eps/C-Rnext) == 0)
    check('geometric epsilon sum collapses exactly',
          sp.simplify(z*eps/a+(eps/C)*(1-z)/(1-lam)-eps/a) == 0)
    check('prefix replacement cost yields the claimed relative exponential bound',
          sp.expand(eps+C*Rk-(C*C*z*Psi/a+(1+C/a)*eps)) == 0)
    check('k zero bound is weaker than the direct closure bound',
          sp.simplify(C*C/a-C-C*(C-a)/a) == 0)

    T, k = sp.symbols('T k', integer=True)
    j, h = T-3*k, 3*k+3
    check('replacement starts at the exact required baseline layer',
          sp.expand((j-3)-(T-h)) == 0)
    check('three entry steps and unchanged suffix give exactly h steps',
          sp.expand(3+(T-j)-h) == 0)
    check('padding to T at least h leaves at least three prefix symbols',
          sp.expand(j.subs(T, h)-3) == 0)
    m, ell = sp.symbols('m ell', integer=True)
    check('phase-aligned prefix replacement preserves the terminal layer',
          sp.expand((j+m*ell)+(T-j)-T-m*ell) == 0)
    omega0, omega1, omega2, earlier = sp.symbols('omega0 omega1 omega2 earlier')
    check('three-symbol occupation is cumulative occupation difference',
          sp.expand((earlier+omega0+omega1+omega2)-earlier
                    -(omega0+omega1+omega2)) == 0)

    u = sp.symbols('u', positive=True)
    check('logarithmic depth inequality has positive derivative on zero to one',
          sp.simplify(sp.diff(-sp.log(1-u)-u, u)-u/(1-u)) == 0)
    check('depth logarithm targets exactly the requested relative error',
          sp.simplify(C*C/a * (a*sp.Symbol('e', positive=True)/(C*C))
                      -sp.Symbol('e', positive=True)) == 0)
    theta, x, y, zeta = sp.symbols('theta x y zeta', positive=True)
    Bprev = theta*(x/6+y/3)
    Bnext = theta*(y/6+zeta/3)
    check('same gauge distributes occupation across the whole output triple',
          sp.expand(theta*(x+y)/2+Bnext-Bprev-theta*(x+y+zeta)/3) == 0)
    check('relative error theta over six leaves theta over six local loss',
          sp.simplify(theta/3-theta/6-theta/6) == 0)
    check('uniform maximum occupation stays unchanged on enlarged alphabet',
          3*(F(1, 4000)+F(1, 200)) == F(63, 4000))
    check('terminal triple maximum equals63 times kappa',
          F(63, 4000)/F(1, 4000) == 63)
    check('uniform layer threshold gives one half kappa before epsilon',
          sp.simplify((C/a)*(a/(126*C))*63-sp.Rational(1, 2)) == 0)
    check('near-optimal epsilon allowance adds the other half kappa',
          sp.simplify((a*sp.Rational(1, 4000)/2)/a
                      -sp.Rational(1, 8000)) == 0)
    check('clamped distance one twentieth saturates the occupation penalty',
          400*F(1, 20)**2 == 1
          and F(27, 100)-F(22, 100) == F(1, 20)
          and F(45, 100)-F(39, 100) > F(1, 20))
    for period in (1, 2):
        w = sp.symbols('w0:'+str(period))
        check(f'period {period} counts literal occupation incidences',
              sp.expand(sum(w[(i-2) % period]+w[(i-1) % period]+w[i]
                            for i in range(period))-3*sum(w)) == 0)

    assert ph == sha(PROOF) and sh == sha(__file__)
    assert all(sha(ROOT/p) == digest for p, digest in dependencies.items())
    result = dict(
        status='passed', exact_checks=len(checks), checks=checks,
        primary_records=len(primary), current_bindings=len(dependencies),
        numerical_cells_recomputed=0, sampled_histories=0,
        contraction='1-(1-theta)/C_theta',
        cumulative_occupation='C_theta/(1-theta)*lambda**k*Psi+epsilon/(1-theta)',
        depth='3*k+3',
        relative_error='C_theta**2/(1-theta)*lambda**k*Psi',
        terminal_transition_layer='3*(1+ceil(C_theta/(1-theta)*log(126*C_theta/(1-theta))))',
        transition_layer_epsilon_upper='(1-theta)/8000',
        prescribed_error_depth='3*ceil(C_theta/(1-theta)*max(0,log(C_theta**2/((1-theta)*e))))+3',
        numerical_depth_evaluated=False, interface_sign_certified=False,
        proof_sha256=ph, script_sha256=sh, dependencies_sha256=dependencies,
        scope='Exact recurrence, layer alignment, geometric error and gauge identities with current written inputs. Prefix optimality and cycle closure remain written proofs. No numerical interface sign, full-period asymptotic or new knot theorem.')
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print('PASS', len(checks), 'exact checks;', len(primary), 'primary records;',
          len(dependencies), 'current bindings; no numerical cover', flush=True)


if __name__ == '__main__':
    main()
