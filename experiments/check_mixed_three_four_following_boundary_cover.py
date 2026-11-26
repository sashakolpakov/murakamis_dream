#!/usr/bin/env python3
"""One fixed full-circle cover. UNRUN until protocol/code/manifest approval.

No refinement, alternate seed, restart, automatic replay or output replacement.
"""
from fractions import Fraction as F
import argparse
import hashlib
import json
import math
from pathlib import Path
import traceback

from flint import acb, acb_mat, arb, ctx

ROOT = Path(__file__).resolve().parents[1]
PROTOCOL = "notes/research_mixed_three_four_following_boundary_diagnostic_protocol.md"
SCRIPT = "experiments/check_mixed_three_four_following_boundary_cover.py"
MANIFEST = ROOT / "repro/protocols/research-mixed-three-four-following-boundary-cover.json"
OUTPUT = ROOT / "repro/results/research-mixed-three-four-following-boundary-cover-attempt01.json"
CENTER_RESULT = "repro/results/research-mixed-three-four-following-action-centers-attempt01.json"
CENTER_RESULT_SHA256 = "43e55892e025cc21a88a749b0517102eb35164a98fa0558c8dd7903d238e8958"
CENTER_MANIFEST = "repro/protocols/research-mixed-three-four-following-action-centers.json"
CENTER_MANIFEST_SHA256 = "2011d2340ed544926f59a5ca0960d0453ddfbd9871852d1a13c04814bc52fd87"
POINT_RADIUS = "1/1073741824"
CELL_RADIUS = "1/256"
CIRCLES = [
    {"label": "c3", "center": ["7/20", "-1/100"], "radius": "83/1000", "typed_radius": "9/100"},
    {"label": "c4", "center": ["3/10", "-13/250"], "radius": "3/50", "typed_radius": "8/125"},
]
CELLS_PER_CIRCLE = 512
ITERATIONS = 24
REQUIRED = {
    PROTOCOL, SCRIPT, CENTER_RESULT, CENTER_MANIFEST,
    "notes/research_mixed_three_four_following_action_diagnostic_protocol.md",
    "experiments/check_mixed_three_four_following_action_centers.py",
    "notes/research_mixed_three_four_following_critical_curve.md",
    "notes/research_mixed_alternating_cap_phase_entrance.md",
    "notes/research_mixed_actual_prefix_arbitrary_letter_phase_class.md",
    "notes/research_mixed_three_four_complete_transformed_prefix.md",
    "notes/research_mixed_three_four_next_conditional_attachment.md",
    "notes/research_mixed_three_four_following_action_direction.md",
    "notes/research_mixed_transformed_following_four_radial_majorant.md",
    "notes/research_mixed_transformed_real_initial_interval.md",
    "notes/research_mixed_actual_last_row_reference_domains.md",
    "notes/research_mixed_reduced_disk_conditional_packets.md",
    "notes/research_mixed_open_word_hessian.md",
    "notes/research_mixed_cyclic_critical_height_bounds.md",
    "notes/research_mixed_three_four_half_face_witness_protocol.md",
    "experiments/check_mixed_three_four_half_face_witnesses.py",
}
COUNTS = dict(equation_calls=0, jacobian_calls=0, dilogarithm_calls=0,
              proposal_iterations=0, point_inclusion_tests=0,
              parameter_inclusion_tests=0, action_evaluations=0,
              comparison_evaluations=0, derivative_evaluations=0)



PRIMARY = [
    ("repro/results/research-mixed-open-word-critical-localization.json",
     "repro/results/research-mixed-open-word-critical-localization-replay.json",
     "notes/research_mixed_open_word_critical_localization.md",
     "experiments/certify_mixed_open_word_critical_localization.py",
     "experiments/certify_mixed_open_word_critical_localization.py"),
    ("repro/results/research-mixed-cyclic-block-localization.json",
     "repro/results/research-mixed-cyclic-block-localization-replay.json",
     "notes/research_mixed_cyclic_critical_localization.md",
     "experiments/certify_mixed_cyclic_block_localization.py",
     "experiments/replay_mixed_cyclic_block_localization.py"),
]


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def ar(x):
    x = F(x)
    return arb(x.numerator) / x.denominator


def cp(pair):
    return acb(ar(pair[0]), ar(pair[1]))


def rational_midpoint(z):
    parts = [float(z.real.mid()), float(z.imag.mid())]
    if not all(math.isfinite(v) for v in parts):
        raise ValueError("nonfinite midpoint proposal")
    return [str(F(v)) for v in parts]


def identity(n):
    return acb_mat([[int(i == j) for j in range(n)] for i in range(n)])


def jp(z):
    return (2 * (PI * z).sin()).log()


def cot(z):
    return (PI * z).cot()


def equations(v, outside):
    COUNTS["equation_calls"] += 1
    e, a, u, t, z = v
    values = [
        -jp(e-u)+jp(e+a)+II*PI*(u-a),
        jp(e+a)+jp(a+t)-2*jp(a)+II*PI*(t-e),
        2*(PI*u).cos().log()+(PI*(e-u)).sin().log()
        -3*(PI*u).sin().log()+II*PI*e,
        jp(a+t)+jp(t+z)-3*jp(t)+II*PI*(a-z+t-ar("1/2")),
        jp(t+z)+jp(z+outside)-3*jp(z)
        +II*PI*(outside-t+z-ar("1/2")),
    ]
    return acb_mat([[value] for value in values])


def jacobian(v, outside):
    COUNTS["jacobian_calls"] += 1
    e, a, u, t, z = v
    b, ea, at, tz, zc = [PI*cot(w) for w in
                         (e-u, e+a, a+t, t+z, z+outside)]
    d = PI*(2*(PI*u).tan()+3*cot(u))
    return acb_mat([
        [-b+ea, ea-II*PI, b+II*PI, 0, 0],
        [ea-II*PI, ea+at-2*PI*cot(a), 0, at+II*PI, 0],
        [b+II*PI, 0, -d-b, 0, 0],
        [0, at+II*PI, 0, at+tz-3*PI*cot(t)+II*PI, tz-II*PI],
        [0, 0, 0, tz-II*PI, tz+zc-3*PI*cot(z)+II*PI],
    ])


def J(z):
    COUNTS["dilogarithm_calls"] += 1
    z = acb(z)
    return (PI*PI/6-(2*PI*II*z).exp().polylog(2))/(2*PI*II) \
        + II*PI*z*(1-z)/2


def g(z):
    return J(z)+II*PI*z*(1-z)/2


def actions(v, outside):
    COUNTS["action_evaluations"] += 1
    e, a, u, t, z = v
    endpoint = -2*J(ar("1/2")-u)-3*J(u)-J(e-u) \
        + II*PI*e*u-II*PI*(e-e*e)/2
    bare = endpoint+g(e+a)+g(a+t)+g(t+z) \
        -2*g(a)-3*g(t)-g(z)+2*PI*II*a*t
    gram = g(z+outside)-2*g(z)-2*g(outside)+2*PI*II*z*outside
    return bare, bare+gram, gram


def real_ball(value):
    return dict(ball=str(value), lower=str(value.lower()), upper=str(value.upper()))


def complex_ball(value):
    return dict(real=real_ball(value.real), imag=real_ball(value.imag))


def verify_inputs(manifest):
    expected = manifest["files_sha256"]
    required = set(REQUIRED)
    for row in PRIMARY:
        required.update(row)
    assert required <= expected.keys(), "missing mandatory source binding"
    for path, digest in expected.items():
        assert sha(ROOT/path) == digest, ("changed frozen input", path)
    visited = set()

    def inherit(path):
        if path in visited:
            return
        visited.add(path)
        data = json.loads((ROOT/path).read_text())
        for field in ("dependencies", "dependencies_sha256", "primary_records",
                      "primary_records_sha256", "saved_replays", "saved_replays_sha256",
                      "files_sha256"):
            deps = data.get(field, {})
            if not isinstance(deps, dict):
                continue
            for child, digest in deps.items():
                assert expected.get(child) == digest, ("unbound dependency", child)
                assert sha(ROOT/child) == digest, ("changed dependency", child)
                if child.startswith("repro/results/") and child.endswith(".json"):
                    inherit(child)

    for author_path, replay_path, proof_path, author_script, replay_script in PRIMARY:
        author = json.loads((ROOT/author_path).read_text())
        replay = json.loads((ROOT/replay_path).read_text())
        assert author["status"] == replay["status"] == "passed"
        assert replay["input_sha256"] == expected[author_path]
        ap = author.get("precision_bits", author.get("precision"))
        rp = replay.get("precision_bits", replay.get("precision"))
        assert isinstance(ap, int) and isinstance(rp, int) and rp >= ap
        assert author["proof_sha256"] == replay["proof_sha256"] == expected[proof_path]
        assert author["script_sha256"] == expected[author_script]
        assert replay["script_sha256"] == expected[replay_script]
        if "domains" in author:
            assert author["domains"] == replay["domains"]
            for key in ("domain_count", "one_vertex_count", "leaves", "excluded", "visits"):
                assert author[key] == replay[key], ("changed full coverage", key)
            assert [(v["epsilon"], v["witness"]) for v in author["one_vertex"]] == \
                [(v["epsilon"], v["witness"]) for v in replay["one_vertex"]]
        else:
            assert len(author["cases"]) == len(replay["cases"]) == 6
            for a_case, r_case in zip(author["cases"], replay["cases"]):
                assert a_case["types"] == r_case["types"]
                assert len(a_case["accepted"]) == r_case["original_boxes"]
                assert r_case["replay_boxes"] == r_case["original_boxes"]
                assert r_case["refinements"] == 0
        inherit(author_path)
        inherit(replay_path)
    inherit(CENTER_RESULT)
    return expected


def verify_saved_seeds(manifest, bindings):
    assert bindings[CENTER_RESULT] == CENTER_RESULT_SHA256
    assert bindings[CENTER_MANIFEST] == CENTER_MANIFEST_SHA256
    saved = json.loads((ROOT/CENTER_RESULT).read_text())
    saved_manifest = json.loads((ROOT/CENTER_MANIFEST).read_text())
    assert saved['manifest_sha256'] == CENTER_MANIFEST_SHA256
    assert saved['status'] == 'completed'
    assert saved['verdict'] == 'both_centers_have_positive_margins'
    assert saved['precision_bits'] == 256
    assert saved['proposal_iterations_per_case'] == ITERATIONS
    assert saved['disk_radius'] == POINT_RADIUS
    assert saved['unprocessed_inventory'] == []
    assert saved['parameter_subdivisions'] == saved['retries'] == 0
    assert saved['source_cover_evaluations'] == 0
    assert not any(saved.get(key) for key in ('error', 'changed_inputs', 'manifest_changed'))
    assert saved['files_sha256'] == saved['claimed_files_sha256'] == saved_manifest['files_sha256']
    assert saved_manifest['root_reviewed'] is True and saved_manifest['peer_reviewed'] is True
    assert len(saved['cases']) == 2
    seeds = {}
    inventory = []
    for circle, case in zip(CIRCLES, saved['cases']):
        assert case['label'] == circle['label']
        assert case['external'] == circle['center']
        assert case['status'] == 'completed' and case['verdict'] == 'both_margins_positive'
        assert len(case['proposal_history']) == ITERATIONS
        assert [row['iteration'] for row in case['proposal_history']] == list(range(1, ITERATIONS+1))
        assert len(case['checks']) == 29 and all(check['passed'] is True for check in case['checks'])
        assert [item['label'] for item in case['comparisons']] == ['real_initial', 'complete_complement']
        assert all(item['verdict'] == 'positive' for item in case['comparisons'])
        assert case['proposal_history'][-1]['centers'] == case['final_center']
        center = case['final_center']
        assert len(center) == 5 and all(len(pair) == 2 for pair in center)
        for pair in center:
            for coordinate in pair:
                F(coordinate)  # Syntax validation of the exact saved rational only.
        seeds[circle['label']] = center
        inventory.append(dict(label=circle['label'], center=center))
    assert manifest['seed_center_inventory'] == inventory
    return seeds


def require(cell, name, condition):
    cell['checks'].append(dict(name=name, passed=bool(condition)))
    assert condition, name


def guarded_box(cell, tag, center, radius, outside):
    box = [v+acb(arb(0, radius), arb(0, radius)) for v in center]
    e, a, u, t, z = box
    def check(name, condition):
        require(cell, tag+': '+name, condition)
    check('original private chamber', ar('33/100') < e.real < ar('47/100')
          and ar('-9/100') < e.imag < ar('2/25'))
    check('original auxiliary chamber', ar('21/100') < u.real < ar('1/4')
          and ar('1/100') < u.imag < ar('1/10'))
    for label, w in (('a', a), ('t', t), ('z', z)):
        check(label+': original Q chamber', ar('23/100') < w.real < ar('9/20')
              and ar('-3/25') < w.imag < ar('3/25'))
    check('original a typed disk', abs(center[1]-cp(['7/20', '-1/100']))+radius < ar('9/100'))
    for index, label in ((3, 't'), (4, 'z')):
        check(label+': original typed disk', abs(center[index]-cp(['3/10', '-13/250']))+radius < ar('8/125'))
        check(label+': original reduced output disk', abs(center[index]-cp(['3/10', '-13/250']))+radius < ar('3/50'))
        check(label+': original negative output height', ar('-51/500') < box[index].imag < ar('-1/1000'))
    arguments = [e, a, u, t, z, outside, ar('1/2')-u,
                 e-u, e+a, a+t, t+z, z+outside]
    check('all original primitive arguments regular', all(0 < w.real < 1 for w in arguments))
    check('original auxiliary sine and cosine branches', 0 < u.real < ar('1/2')
          and 0 < (e-u).real < ar('1/2'))
    outgoing_radius = (2*PI*z.imag).exp()
    check('outgoing radius in original range', ar('1/2') < outgoing_radius < 1)
    return box


def inclusion(cell, tag, center, Y, radius, outside):
    key = 'point_inclusion_tests' if tag == 'midpoint' else 'parameter_inclusion_tests'
    COUNTS[key] += 1
    box = guarded_box(cell, tag, center, radius, outside)
    gradient = equations(center, outside)
    residual = Y*gradient
    jac = jacobian(box, outside)
    error = identity(5)-Y*jac
    rows = [sum(abs(error[i, j]) for j in range(5)) for i in range(5)]
    record = dict(radius=str(radius), coordinate_boxes=[complex_ball(v) for v in box],
                  original_center_gradient=[complex_ball(gradient[i, 0]) for i in range(5)],
                  rows=[dict(residual=real_ball(abs(residual[i, 0])),
                             derivative_row=real_ball(rows[i]),
                             image_radius=real_ball(abs(residual[i, 0])+radius*rows[i])) for i in range(5)])
    cell['inclusions'][tag] = record
    for i in range(5):
        require(cell, f'{tag} row {i}: contraction', rows[i] < 1)
        require(cell, f'{tag} row {i}: strict complex-disk inclusion',
                abs(residual[i, 0])+radius*rows[i] < radius)
    return box, jac


def classify(interval):
    return 'positive' if interval > 0 else 'negative' if interval < 0 else 'inconclusive'


def run_cell(circle, index, seed, cell):
    theta_mid = PI*ar(F(2*index+1, CELLS_PER_CIRCLE))
    halfwidth = PI/CELLS_PER_CIRCLE
    theta_cell = theta_mid+arb(0, halfwidth.upper())
    center_c = cp(circle['center'])
    rho = ar(circle['radius'])
    midpoint_exp = (II*theta_mid).exp()
    cell_exp = (II*theta_cell).exp()
    outside_mid = center_c+rho*midpoint_exp
    outside_cell = center_c+rho*cell_exp
    ctheta = II*rho*cell_exp
    cell['external_midpoint'] = complex_ball(outside_mid)
    cell['external_cell'] = complex_ball(outside_cell)
    cell['theta_cell'] = real_ball(theta_cell)
    cell['theta_halfwidth'] = real_ball(halfwidth)
    require(cell, 'full parameter enclosure in original typed disk',
            abs(outside_cell-center_c) < ar(circle['typed_radius']))
    proposals = [list(pair) for pair in seed]
    for iteration in range(ITERATIONS):
        v = list(map(cp, proposals))
        step = jacobian(v, outside_mid).inv()*equations(v, outside_mid)
        proposals = [rational_midpoint(v[j]-step[j, 0]) for j in range(5)]
        COUNTS['proposal_iterations'] += 1
        cell['proposal_history'].append(dict(iteration=iteration+1, centers=proposals))
    v0 = list(map(cp, proposals))
    inverse_mid = jacobian(v0, outside_mid).inv()
    inverse_exact = [[rational_midpoint(inverse_mid[i, j]) for j in range(5)] for i in range(5)]
    Y = acb_mat([[cp(pair) for pair in row] for row in inverse_exact])
    cell['final_center'] = proposals
    cell['rational_inverse'] = inverse_exact
    require(cell, 'rational inverse invertible', abs(Y.det()) > 0)
    point_box, _ = inclusion(cell, 'midpoint', v0, Y, ar(POINT_RADIUS), outside_mid)
    cell_box, cell_jac = inclusion(cell, 'whole_cell', v0, Y, ar(CELL_RADIUS), outside_cell)

    bare, whole, gram = actions(point_box, outside_mid)
    require(cell, 'finite original midpoint action values',
            all(v.real.is_finite() and v.imag.is_finite() for v in (bare, whole, gram)))
    cell['bare_prefix_action_midpoint'] = complex_ball(bare)
    cell['whole_half_chain_action_midpoint'] = complex_ball(whole)
    cell['removed_gram_action_midpoint'] = complex_ball(gram)
    r_mid = (2*PI*point_box[4].imag).exp()
    beta_mid = (2/(1+r_mid*r_mid)).log()/2
    ceiling_mid = ar('17539/9600')-ar('23/64000')-ar('6/25')*beta_mid+beta_mid*beta_mid/20
    cell['outgoing_radius_midpoint'] = real_ball(r_mid)
    cell['radial_beta_midpoint'] = real_ball(beta_mid)

    COUNTS['derivative_evaluations'] += 1
    inverse_cell = cell_jac.inv()
    require(cell, 'finite uniform Hessian inverse',
            all(inverse_cell[i, j].real.is_finite() and inverse_cell[i, j].imag.is_finite()
                for i in range(5) for j in range(5)))
    z = cell_box[4]
    t = cell_box[3]
    Q = (-2*PI*II*z).exp()
    C = (-2*PI*II*outside_cell).exp()
    denominator = 1-Q*C
    require(cell, 'original mixed derivative denominator nonzero', abs(denominator) > 0)
    qprime = -inverse_cell[4, 4]*(2*PI*II/denominator)
    pprime = jp(t+z)-jp(z)-II*PI*t
    r_cell = (2*PI*z.imag).exp()
    beta_cell = (2/(1+r_cell*r_cell)).log()/2
    ceiling_h = (-ar('6/25')+beta_cell/10)*(-2*PI*r_cell*r_cell/(1+r_cell*r_cell))
    response = qprime*ctheta
    derivatives = ((pprime*response).real, ((pprime+II*ceiling_h)*response).real)
    require(cell, 'finite uniform margin derivatives', all(value.is_finite() for value in derivatives))
    cell['derivative_enclosures'] = dict(
        inverse_last_entry=complex_ball(inverse_cell[4, 4]),
        original_mixed_derivative=complex_ball(2*PI*II/denominator),
        last_leg_response=complex_ball(qprime),
        bare_action_last_derivative=complex_ball(pprime),
        parameter_angular_derivative=complex_ball(ctheta),
        radial_ceiling_height_derivative=real_ball(ceiling_h),
        outgoing_radius=real_ball(r_cell), radial_beta=real_ball(beta_cell))
    for (label, bound), derivative in zip(
            (('real_initial', ar('7/4')), ('complete_complement', ceiling_mid)), derivatives):
        COUNTS['comparison_evaluations'] += 1
        midpoint_margin = bare.real-bound
        derivative_abs = abs(derivative)
        debit = halfwidth*derivative_abs
        whole_margin = midpoint_margin+arb(0, debit.upper())
        require(cell, label+': finite midpoint and transported margins',
                midpoint_margin.is_finite() and debit.is_finite() and whole_margin.is_finite())
        cell['comparisons'].append(dict(label=label,
            midpoint_ceiling=real_ball(bound), midpoint_margin=real_ball(midpoint_margin),
            midpoint_verdict=classify(midpoint_margin),
            real_derivative=real_ball(derivative), derivative_absolute_bound=real_ball(derivative_abs),
            transport_debit=real_ball(debit), whole_cell_margin=real_ball(whole_margin),
            verdict=classify(whole_margin)))
    verdicts = [item['verdict'] for item in cell['comparisons']]
    cell['verdict'] = ('both_cell_margins_positive' if all(v == 'positive' for v in verdicts)
                       else 'a_cell_comparison_is_negative' if 'negative' in verdicts else 'inconclusive')
    cell['status'] = 'completed'


def main():
    global PI, II
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--manifest', type=Path, default=MANIFEST)
    args = parser.parse_args()
    if OUTPUT.exists():
        raise FileExistsError('the single-run output already exists; no overwrite')
    inventory = [dict(id=f'{circle["label"]}:{index:03d}', circle=circle['label'], index=index,
                      theta_start_pi=str(F(2*index, CELLS_PER_CIRCLE)),
                      theta_end_pi=str(F(2*(index+1), CELLS_PER_CIRCLE)),
                      theta_midpoint_pi=str(F(2*index+1, CELLS_PER_CIRCLE)))
                 for circle in CIRCLES for index in range(CELLS_PER_CIRCLE)]
    result = dict(status='failed', verdict='inconclusive', precision_bits=256,
                  circles=CIRCLES, cells_per_circle=CELLS_PER_CIRCLE,
                  proposal_iterations_per_cell=ITERATIONS, point_radius=POINT_RADIUS,
                  parameter_radius=CELL_RADIUS, center_result_sha256=CENTER_RESULT_SHA256,
                  inventory=inventory, cells=[], unprocessed_inventory=[item['id'] for item in inventory],
                  operation_counts=COUNTS, adaptive_subdivisions=0, retries=0,
                  scope='Two complete reduced disks; only the original initial and complementary prefix remainders. No whole-prefix or next-attachment conclusion.')
    frozen = None
    manifest_hash = None
    try:
        manifest_hash = sha(args.manifest)
        result['manifest_sha256'] = manifest_hash
        manifest = json.loads(args.manifest.read_text())
        result['claimed_files_sha256'] = manifest.get('files_sha256', {})
        assert manifest['root_reviewed'] is True and manifest['peer_reviewed'] is True
        assert manifest['precision_bits'] == 256
        assert manifest['proposal_iterations_per_cell'] == ITERATIONS
        assert manifest['cells_per_circle'] == CELLS_PER_CIRCLE
        assert manifest['point_radius'] == POINT_RADIUS and manifest['parameter_radius'] == CELL_RADIUS
        assert manifest['circle_inventory'] == CIRCLES
        assert manifest['output'] == str(OUTPUT.relative_to(ROOT))
        frozen = verify_inputs(manifest)
        seeds = verify_saved_seeds(manifest, frozen)
        result['files_sha256'] = frozen
        result['seed_center_inventory'] = manifest['seed_center_inventory']
        ctx.prec = 256
        PI, II = arb.pi(), acb(0, 1)
        position = 0
        for circle in CIRCLES:
            for index in range(CELLS_PER_CIRCLE):
                cell = dict(inventory[position], status='failed', verdict='inconclusive',
                            proposal_history=[], checks=[], inclusions={}, comparisons=[])
                position += 1
                result['cells'].append(cell)
                before = dict(COUNTS)
                try:
                    run_cell(circle, index, seeds[circle['label']], cell)
                except Exception as exc:
                    cell['error'] = f'{type(exc).__name__}: {exc}'
                    cell['traceback'] = traceback.format_exc()
                finally:
                    cell['operation_counts'] = {key: COUNTS[key]-before[key] for key in COUNTS}
                    result['unprocessed_inventory'].remove(cell['id'])
        assert [item['id'] for item in result['cells']] == [item['id'] for item in inventory]
        result['summary'] = {
            'attempted_cells':len(result['cells']),
            'completed_cells':sum(item['status'] == 'completed' for item in result['cells']),
            'positive_cells':sum(item['verdict'] == 'both_cell_margins_positive' for item in result['cells']),
            'failed_cell_ids':[item['id'] for item in result['cells'] if item['status'] != 'completed'],
            'nonpositive_cell_ids':[item['id'] for item in result['cells'] if item['verdict'] != 'both_cell_margins_positive'],
        }
        if all(cell['status'] == 'completed' for cell in result['cells']):
            result['status'] = 'completed'
            result['verdict'] = ('both_full_disks_have_positive_margins'
                if all(cell['verdict'] == 'both_cell_margins_positive' for cell in result['cells'])
                else 'complete_cell_inventory_recorded_no_full_disk_conclusion')
    except Exception as exc:
        result['error'] = f'{type(exc).__name__}: {exc}'
        result['traceback'] = traceback.format_exc()
    finally:
        def changed_or_missing(path, digest):
            try:
                return sha(path) != digest
            except OSError:
                return True
        if frozen is not None:
            changed = [path for path, digest in frozen.items() if changed_or_missing(ROOT/path, digest)]
            if changed:
                result['changed_inputs'] = changed
                result['status'] = 'failed'
                result['verdict'] = 'inconclusive'
        if manifest_hash is not None and changed_or_missing(args.manifest, manifest_hash):
            result['manifest_changed'] = True
            result['status'] = 'failed'
            result['verdict'] = 'inconclusive'
        OUTPUT.parent.mkdir(parents=True, exist_ok=True)
        with OUTPUT.open('x') as stream:
            json.dump(result, stream, indent=2)
            stream.write('\n')
    print(json.dumps(dict(status=result['status'], verdict=result['verdict'],
                          summary=result.get('summary'), counts=COUNTS, output=str(OUTPUT))))
    if result['status'] != 'completed':
        raise SystemExit(1)


if __name__ == '__main__':
    main()
