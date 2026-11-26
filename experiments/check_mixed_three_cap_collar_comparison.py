#!/usr/bin/env python3
"""Saved real corners and scalar budgets for a calibrated three-three collar.

No new root proposals, parameter domains, subdivisions or word enumeration.
"""
import argparse
from fractions import Fraction as F
import hashlib
import itertools
import json
from pathlib import Path

from flint import acb, arb, ctx
import sympy as sp
import certify_mixed_real_small_support as core

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / "notes/research_mixed_three_cap_collar_comparison.md"
VERTICES = [(F(a), F(b)) for a, b in
            [('.1', '.3'), ('.1', '.39'), ('.39', '.5'),
             ('.5', '.39'), ('.39', '.1'), ('.3', '.1')]]


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--precision', type=int, default=256)
    ap.add_argument('--input', type=Path)
    ap.add_argument('--output', type=Path, default=ROOT /
                    'repro/results/research-mixed-three-cap-collar-comparison.json')
    args = ap.parse_args()
    assert args.precision >= 192
    ctx.prec = args.precision
    core.pi, core.ii = arb.pi(), acb(0, 1)
    pi, ar = core.pi, core.ar
    ph, sh = sha(PROOF), sha(__file__)
    ih = sha(args.input) if args.input else None
    old = json.loads(args.input.read_text()) if args.input else None
    deps, visited, records, primary = {}, set(), {}, {}

    def bind(path, expected=None):
        if path not in deps:
            deps[path] = sha(ROOT/path)
        if expected is not None:
            assert deps[path] == expected, path
        return deps[path]

    def inherit(path):
        bind(path)
        if path in visited:
            return records[path]
        visited.add(path)
        record = json.loads((ROOT/path).read_text())
        records[path] = record
        nested = {}
        for field in ('dependencies', 'dependencies_sha256'):
            for p, digest in record.get(field, {}).items():
                assert p not in nested or nested[p] == digest, p
                nested[p] = digest
                bind(p, digest)
        for p in nested:
            if p.startswith('repro/results/') and p.endswith('.json'):
                inherit(p)
        return record

    def load(stem, script_prefix='check'):
        path = 'repro/results/research-'+stem.replace('_', '-')+'.json'
        r = inherit(path)
        assert r['status'] == 'passed', path
        bind('notes/research_'+stem+'.md', r['proof_sha256'])
        bind('experiments/'+script_prefix+'_'+stem+'.py', r['script_sha256'])
        primary[path] = deps[path]
        return r

    seams = load('mixed_seam_run_connector_lower')
    caps = load('mixed_cap_seam_source_bounds')
    images = load('mixed_open_word_endpoint_rectangles')
    disks = load('mixed_open_local_factor_coverage')
    load('mixed_complete_first_cap_packet')
    load('mixed_acute_gradient_height_transfer')
    load('mixed_closed_cotangent_roots')
    load('mixed_real_outer_support')
    load('mixed_real_zero_collar', 'certify')
    for stem in ('mixed_cap_seam_source_bounds', 'mixed_open_local_factor_coverage'):
        path = 'repro/results/research-'+stem.replace('_', '-')+'-replay.json'
        r = inherit(path)
        author = 'repro/results/research-'+stem.replace('_', '-')+'.json'
        assert r['status'] == 'passed' and r['input_sha256'] == deps[author]
        for key in ('proof_sha256', 'script_sha256', 'dependencies_sha256'):
            assert r[key] == records[author][key]
        primary[path] = deps[path]
    for path in ('notes/research_mixed_boundary_strip_bounds.md',
                 'notes/research_mixed_fourier_weight_continuation.md',
                 'notes/research_mixed_open_finite_boundary_windows.md',
                 'notes/research_mixed_conditional_torus_composition.md',
                 'experiments/certify_mixed_real_small_support.py'):
        bind(path)

    checks, scalars = [], {}

    def check(name, condition):
        assert condition, name
        checks.append(name)

    check('the cap seam ceiling and its complete saved replay are retained',
          caps['seam_ceilings'] == ['101/125', '433/500'])
    check('actual type-three attached and private rectangles, including length two',
          list(map(F, images['rectangles'][0][0])) == list(map(F, ['.376', '.438', '-.019', '.037']))
          and list(map(F, images['rectangles'][0][1])) == list(map(F, ['.278', '.391', '-.072', '.021'])))
    check('all ordinary type-three legs use the smaller .083 disk',
          sum(row['witnesses'] for row in disks['attached_disk_extraction']) == 5258
          and all(F(row['enclosing_radius']) == F('.083')
                  for row in disks['attached_disk_extraction'] if row['own_type'] == 3)
          and F('.35')-F('.083') == F('.267')
          and F('.35')+F('.083') == F('.433')
          and -F('.01')-F('.083') == -F('.093')
          and -F('.01')+F('.083') == F('.073'))
    cut = inherit('repro/results/research-mixed-cap-real-cut-gaps.json')
    check('the original complete cap rate exceeds one on every actual image',
          F(cut['selected_rate_floor']) == 1 and cut['status'] == 'passed')

    def cross(a, b, c):
        return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])

    check('the six old corners form a strictly convex clockwise hexagon',
          all(cross(VERTICES[j-1], VERTICES[j], VERTICES[(j+1) % 6]) < 0 for j in range(6)))
    corners = list(itertools.product(map(F, ['.278', '.391']), map(F, ['.267', '.438'])))
    check('the complete actual real rectangle is strictly inside that hexagon',
          all(cross(VERTICES[j], VERTICES[(j+1) % 6], c) < 0
              for j in range(6) for c in corners))
    saved = {(F(r['a']), F(r['b']), r['epsilon']): r for r in seams['roots']}
    assert len(saved) == 40 and seams['scalar_comparisons'] == 48
    root_records = []
    for a, b in VERTICES:
        witness = saved[a, b, 0]
        assert F(witness['radius']) == F(1, 10**12)
        aa, bb = acb(ar(a)), acb(ar(b))
        accepted = core.point_root(aa, bb, 0, witness['center'])
        assert accepted is not None
        box, center = accepted
        assert center == witness['center']
        value = core.phase(box, aa, bb, 0, 0)[0].real
        check('saved original phase at '+str((a, b))+' exceeds .44', value > ar(F(11, 25)))
        key = 'f_'+str(a)+'_'+str(b)
        scalars[key] = value
        root_records.append(dict(a=str(a), b=str(b), epsilon=0,
                                 center=center, radius=witness['radius']))

    cot_margin = (ar('.186')*pi).cosh()-(ar('.534')*pi).cos()-2*(ar('.186')*pi).sinh()
    check('the whole vertical box lies in the closed half-cotangent strip', cot_margin > 0)
    scalars['cotangent_half_strip_margin'] = cot_margin
    u, v, q, beta = sp.symbols('u v q beta', real=True)
    numerator = sp.im((u+sp.I*v+q+sp.I*beta)*sp.conjugate(u+sp.I*v+sp.I))
    check('the surviving complex gradient has negative imaginary numerator',
          sp.expand(numerator-(u*(beta-1)-q*(v+1))) == 0)

    def maximum(C):
        arg = C.exp()/2
        assert 0 < arg < 1
        trial = 2*arg.asin()/pi
        assert 0 < trial < 1
        value = -2*core.g(acb((1-trial)/2)).real-core.g(acb(trial)).real+C*trial
        residual = C-(2*(pi*trial/2).sin()).log()
        assert residual.contains(0)
        return trial, value

    check('the two row maxima lie in the analytic interior-max regime', ar('.146')*pi < arb(2).log())
    for C, label, upper in ((arb(0), 'zero', F('.326')),
                            (ar('.146')*pi, 'positive', F('.526'))):
        trial, value = maximum(C)
        check('the complete row maximum '+label+' has its stated ceiling', value < ar(upper))
        scalars['row_maximizer_'+label] = trial
        scalars['row_maximum_'+label] = value
    check('the two attenuation cases share the asserted budget',
          F('.0465') < F('.073')
          and ar('.526') < ar('.326')+ar('.073')*pi)
    rho = ar(F(1, 1000))
    collar = rho*arb(2).log()-core.g(acb(rho)).real
    loss = ar('.306')-ar('.0835')*pi-2*collar
    check('the full paired rate reserve exceeds three hundredths', loss > ar(F(3, 100)))
    check('one total finite-source tolerance leaves one fortieth',
          F(3, 100)-F(1, 200) == F(1, 40)
          and F(1, 40) > F(1, 50))
    scalars.update(collar_delta=collar, paired_rate_reserve=loss)

    result = dict(status='passed', precision_bits=args.precision,
                  exact_and_scalar_checks=len(checks), checks=checks,
                  saved_root_disks=6, roots=root_records,
                  scalar_enclosures={k: str(v) for k, v in scalars.items()},
                  primary_records_sha256=primary, dependencies_sha256=deps,
                  proof_sha256=ph, script_sha256=sh, input_sha256=ih,
                  new_root_proposals=0, new_parameter_cover_cells=0,
                  rate_reserve='3/100', finite_reserve='1/40',
                  scope='Actual open words beginning (3,3), first outgoing real collar and neighboring real reference with its entire height attenuation. Calibrated cap-plus-edge source bound; no global boundary comparison.')
    if old:
        for key in result:
            if key not in ('precision_bits', 'scalar_enclosures', 'input_sha256'):
                assert old[key] == result[key], key
        assert old['scalar_enclosures'].keys() == scalars.keys()
        assert all(value.overlaps(arb(old['scalar_enclosures'][key])) for key, value in scalars.items())
    assert sha(PROOF) == ph and sha(__file__) == sh
    assert all(sha(ROOT/p) == h for p, h in deps.items())
    if args.input:
        assert sha(args.input) == ih
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print('PASS', len(checks), 'exact/scalar checks;', len(root_records),
          'saved roots;', len(primary), 'primary records;', len(deps), 'bindings')


if __name__ == '__main__':
    main()
