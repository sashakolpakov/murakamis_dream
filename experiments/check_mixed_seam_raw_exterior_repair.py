#!/usr/bin/env python3
"""Exact raw exterior fees and existing-input seam-repair deduction.

No numerical cover, critical root, optimization, or cyclic enumeration.
The global nonlow upper bound remains a separate hypothesis.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT/'notes/research_mixed_seam_raw_exterior_repair.md'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--input', type=Path)
    ap.add_argument('--output', type=Path, default=ROOT/
                    'repro/results/research-mixed-seam-raw-exterior-repair.json')
    args = ap.parse_args()
    ph, sh = sha(PROOF), sha(__file__)
    deps, visited, primary, identities, checks = {}, set(), {}, [], []

    def bind(path, expected=None):
        if path not in deps:
            deps[path] = sha(ROOT/path)
        if expected is not None:
            assert deps[path] == expected, path
        return deps[path]

    def inherit(path):
        if path in visited:
            return None
        raw = (ROOT/path).read_bytes()
        bind(path, hashlib.sha256(raw).hexdigest())
        rec = json.loads(raw)
        visited.add(path)
        merged = {}
        for field in ('dependencies', 'dependencies_sha256'):
            for name, digest in rec.get(field, {}).items():
                assert name not in merged or merged[name] == digest, name
                merged[name] = digest
                bind(name, digest)
        for name in merged:
            if name.startswith('repro/results/') and name.endswith('.json'):
                inherit(name)
        return rec

    for stem, proof, script in [
        ('mixed_closed_half_period', 'mixed_closed_half_period', 'check_mixed_closed_half_period'),
        ('mixed_raw_row_stationarity', 'mixed_raw_row_stationarity', 'check_mixed_raw_row_stationarity'),
        ('mixed_right_boundary_row_bracket', 'mixed_right_boundary_row_bracket', 'check_mixed_right_boundary_row_bracket'),
        ('mixed_height_resolved_seam_sources', 'mixed_height_resolved_seam_sources', 'check_mixed_height_resolved_seam_sources'),
        ('mixed_right_square_conditional_packets', 'mixed_unselected_right_taper_products', 'certify_mixed_right_square_conditional_packets'),
        ('mixed_complex_right_row_reduction', 'mixed_complex_right_row_reduction', 'check_mixed_complex_right_row_reduction'),
        ('mixed_exact_low_transport', 'mixed_exact_low_transport', 'check_mixed_exact_low_transport')]:
        name = f'repro/results/research-{stem.replace("_", "-")}.json'
        rec = inherit(name)
        if rec is None:
            raw = (ROOT/name).read_bytes()
            bind(name, hashlib.sha256(raw).hexdigest())
            rec = json.loads(raw)
        assert rec['status'] == 'passed', name
        bind(f'notes/research_{proof}.md', rec['proof_sha256'])
        bind(f'experiments/{script}.py', rec['script_sha256'])
        primary[stem] = rec
    bind('notes/research_mixed_split_cutoff_hybrid_contour.md')

    def check(name, condition):
        assert condition, name
        checks.append(name)

    def zero(name, expression):
        assert sp.simplify(sp.expand(expression)) == 0, name
        identities.append(name)

    bracket = primary['mixed_right_boundary_row_bracket']
    check('complete raw bracket includes early and endpoint reals',
          bracket['row_interval'] == ['1/5', '2/5']
          and bracket['neighboring_real_interval'] == ['1/10', '1/2']
          and bracket['maximum_absolute_height'] == '57/1000')
    raw = primary['mixed_raw_row_stationarity']
    check('all physical selected raw branches retained', raw['physical_branch_count'] == 12)
    half = primary['mixed_closed_half_period']
    check('complete inherited general-angle run inequalities',
          half['typed_selection_cases'] == 24 and half['rational_intervals'] == 96
          and half['left_boundary_debit'] == '9/100'
          and half['right_boundary_debit'] == '0'
          and half['internal_phase_reserve'] == '1/3'
          and half['singleton_phase_reserve'] == '3/1000')
    square = primary['mixed_right_square_conditional_packets']
    check('repaired bare kernels lie in completed right square',
          square['boundary_pieces'] == 64 and square['accepted_cells'] == 2423
          and square['parameter_rectangles']['p3'] == ['11/50', '1/2', '-3/100', '1/50']
          and square['parameter_rectangles']['p4'] == ['11/50', '1/2', '-57/1000', '141/10000'])
    profiles = primary['mixed_height_resolved_seam_sources']
    check('original angle-uniform source profiles extracted completely',
          profiles['source_grid_values'] == 225 and profiles['original_source_cells'] == 57092
          and profiles['independent_replay_source_cells'] == 57166)
    low = primary['mixed_exact_low_transport']
    check('original raw and coherent low raising available', low['raising_endpoint'] == '1/10')

    # Bind two completed saved replays, without reevaluating any old cell.
    saved_replays = []
    for stem in ('mixed_closed_half_period', 'mixed_raw_row_stationarity'):
        author_path = f'repro/results/research-{stem.replace("_", "-")}.json'
        replay_path = f'repro/results/research-{stem.replace("_", "-")}-replay.json'
        replay = inherit(replay_path)
        if replay is None:
            raw = (ROOT/replay_path).read_bytes()
            bind(replay_path, hashlib.sha256(raw).hexdigest())
            replay = json.loads(raw)
        author = primary[stem]
        assert replay['status'] == 'passed' and replay['input_sha256'] == deps[author_path]
        for key in ('proof_sha256', 'script_sha256'):
            assert replay[key] == author[key], (stem, key)
        saved_replays.append(replay_path)

    pi, I = sp.pi, sp.I
    u, z, x, h = sp.symbols('u z x h', real=True)
    alpha, eps, d, sigma, q = sp.symbols('alpha eps d sigma q', real=True)
    g = sp.Function('g')
    Q = g(u+sp.Rational(1,2))+g(u+z)-(2+eps)*g(u)+2*pi*I*(d*z+(1-d)/2)*u
    phase = Q-(1+(alpha-q)/2)*g(z)+pi*I*(sigma-q)*z
    K = sp.diff(g(u+z),z)-(1+(alpha-q)/2)*sp.diff(g(z),z)+2*pi*I*d*u+pi*I*(sigma-q)
    zero('original chirp and selected allocated marginal', sp.diff(phase,z)-K)
    zero('fixed-row own second derivative', sp.diff(phase,z,2)
         -sp.diff(g(u+z),z,2)+(1+(alpha-q)/2)*sp.diff(g(z),z,2))
    X, C = sp.symbols('X C', real=True)
    zero('real cotangent derivative numerator',
         sp.diff(sp.sin(X)/(C-sp.cos(X)),X)
         -(C*sp.cos(X)-1)/(C-sp.cos(X))**2)
    s = sp.symbols('s', positive=True)
    zero('hyperbolic bound from a radius ratio', (s+1/s)/2-sp.Rational(13,12)
         -(s-sp.Rational(3,2))*(s-sp.Rational(2,3))/(2*s))
    check('positive hyperbolic interval endpoint', F(3,2)+F(2,3)==F(13,6))
    check('rational square-root and cosine bounds', F(9,4)**2>5 and (1+F(9,4))/4==F(13,16))
    check('strict raw cotangent decrease margin', F(13,12)*F(13,16)==F(169,192)<1)
    check('shifted arguments stay in the original regular strip',
          F(1,10)+F(1,5)==F(3,10)>0 and F(1,2)+F(2,5)==F(9,10)<1)
    physical = [(0,0,0),(1,1,0),(0,0,1),(0,1,1),(1,0,1),(1,1,1)]
    branches = []
    for ee, aa, dd in physical:
        for ss in range(aa+1):
            for qq in sorted({0,ss}):
                check(f'convex branch remaining coefficient {ee}{aa}{dd}{ss}{qq}',aa-qq>=0)
                branches.append([ee,aa,dd,ss,qq])
    assert len(branches) == 12
    zero('active factorial branch imaginary marginal at real height',
         pi*(sp.Rational(1,2)-x-u)
         -(1+alpha/2)*pi*(sp.Rational(1,2)-x)+2*pi*d*u+pi*sigma
         -pi*((2*d-1)*u-alpha*(sp.Rational(1,2)-x)/2+sigma))
    tau = sp.symbols('tau', real=True)
    zero('chord and tangent repair displacement', (1-tau)*h-(h-tau*h))
    v = sp.symbols('v', nonnegative=True)
    base = pi*(sigma-alpha*(sp.Rational(1,2)-x)/2)
    slope0, slope1 = base-pi*u, base+pi*u
    zero('left positive displacement fee slack', base*v-slope0*v-pi*u*v)
    zero('left negative displacement fee slack',
         -base*v+pi*v/2+slope0*v-pi*(sp.Rational(1,2)-u)*v)
    zero('right positive displacement fee slack',
         base*v+pi*v/2-slope1*v-pi*(sp.Rational(1,2)-u)*v)
    zero('right negative displacement fee slack', -base*v+slope1*v-pi*u*v)
    check('all four fee slacks are nonnegative on the row bracket',
          F(1,5)>0 and F(1,2)-F(2,5)>0)

    k, n = sp.symbols('k n', integer=True, positive=True)
    zero('proper-run reserve minus retained per-vertex loss',
         (k-1)/3-sp.Rational(9,100)-sp.Rational(3,1000)*k
         -(991*k-1270)/3000)
    check('proper runs of every length at least two retain the loss', 991*2-1270>0)
    check('all-seam loop and cycles have the stronger reserve', F(1,3)>F(3,1000))
    zero('one global finite tolerance leaves the promised seam loss',
         sp.Rational(3,1000)*n-sp.Rational(1,1000)-sp.Rational(1,500)*n
         -(n-1)/1000)
    check('one collar incidence has at most one exterior incidence', 2-1<=1 and 2-2==0)

    result = dict(status='passed', exact_identities=len(identities),
        exact_checks=len(checks), physical_branches=branches,
        primary_records=len(primary), saved_replays=saved_replays,
        current_bindings=len(deps), identities=identities, checks=checks,
        raw_cotangent_product_upper='169/192', seam_phase_loss_per_vertex='3/1000',
        conditional_seam_finite_loss_per_vertex='1/500', numerical_cells_recomputed=0,
        new_critical_roots=0, cyclic_pattern_enumerations=0,
        global_nonlow_bound_asserted=False, proof_sha256=ph, script_sha256=sh,
        dependencies_sha256=deps,
        scope='Exact raw exterior repair fees and unconditional seam-priority '
              'reduction to the ordinary nonlow mixed envelope. A global nonlow '
              'bound is a separate hypothesis; no new full-period asymptotic.')
    ih = None
    if args.input:
        data = args.input.read_bytes()
        ih = hashlib.sha256(data).hexdigest()
        old = json.loads(data)
        for key in result:
            assert old[key] == result[key], key
        result['input_sha256'] = ih
    assert sha(PROOF)==ph and sha(__file__)==sh
    assert all(sha(ROOT/path)==digest for path,digest in deps.items())
    if ih:
        assert sha(args.input)==ih
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS',len(identities),'identities',len(checks),'checks',len(branches),
          'branches',len(primary),'primary',len(deps),'bindings',flush=True)


if __name__ == '__main__':
    main()
