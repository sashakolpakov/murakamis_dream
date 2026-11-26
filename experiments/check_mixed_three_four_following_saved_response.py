#!/usr/bin/env python3
"""One saved-only response completion; no root, Hessian or action evaluation."""
from fractions import Fraction as F
import argparse
import hashlib
import json
from pathlib import Path
import traceback

from flint import acb, arb, ctx

ROOT = Path(__file__).resolve().parents[1]
PROTOCOL = "notes/research_mixed_three_four_following_saved_response_protocol.md"
SCRIPT = "experiments/check_mixed_three_four_following_saved_response.py"
MANIFEST = ROOT / "repro/protocols/research-mixed-three-four-following-saved-response.json"
OUTPUT = ROOT / "repro/results/research-mixed-three-four-following-saved-response-attempt01.json"
SAVED_RESULT = "repro/results/research-mixed-three-four-following-boundary-cover-attempt01.json"
SAVED_RESULT_SHA256 = "e2a6f208dd59f9e2d8044619aa70532c7945972b8d499af3e00880f9e580449b"
SAVED_MANIFEST = "repro/protocols/research-mixed-three-four-following-boundary-cover.json"
SAVED_MANIFEST_SHA256 = "d7e9e6a096e4ce5dc77858691a90b257f842a42910603f74f3d15a6e20a46405"
CIRCLES = [
    {"label": "c3", "center": ["7/20", "-1/100"], "radius": "83/1000", "typed_radius": "9/100"},
    {"label": "c4", "center": ["3/10", "-13/250"], "radius": "3/50", "typed_radius": "8/125"},
]
CELLS_PER_CIRCLE = 512
POINT_RADIUS = "1/1073741824"
CELL_RADIUS = "1/256"
REQUIRED = {
    PROTOCOL, SCRIPT, SAVED_RESULT, SAVED_MANIFEST,
    "notes/research_mixed_three_four_following_boundary_diagnostic_protocol.md",
    "experiments/check_mixed_three_four_following_boundary_cover.py",
    "notes/research_mixed_three_four_following_critical_curve.md",
    "notes/research_mixed_transformed_following_four_radial_majorant.md",
    "notes/research_mixed_transformed_real_initial_interval.md",
    "notes/research_mixed_actual_last_row_reference_domains.md",
    "notes/research_mixed_reduced_disk_conditional_packets.md",
}
COUNTS = dict(decoded_real_intervals=0, response_enclosures=0,
              margin_comparisons=0, new_roots=0, new_inclusions=0,
              new_hessians=0, new_matrix_inverses=0,
              new_actions=0, new_dilogarithms=0)



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
    inherit(SAVED_RESULT)
    return expected


def saved_check_names():
    names = ['full parameter enclosure in original typed disk', 'rational inverse invertible']
    for tag in ('midpoint', 'whole_cell'):
        guards = ['original private chamber', 'original auxiliary chamber']
        guards.extend(label+': original Q chamber' for label in ('a', 't', 'z'))
        guards.append('original a typed disk')
        for label in ('t', 'z'):
            guards.extend(label+': '+suffix for suffix in
                          ('original typed disk', 'original reduced output disk', 'original negative output height'))
        guards.extend(['all original primitive arguments regular',
                       'original auxiliary sine and cosine branches', 'outgoing radius in original range'])
        names.extend(tag+': '+name for name in guards)
        for i in range(5):
            names.extend([f'{tag} row {i}: contraction', f'{tag} row {i}: strict complex-disk inclusion'])
    names.append('finite original midpoint action values')
    return names


def fixed_inventory():
    return [dict(id=f'{circle["label"]}:{index:03d}', circle=circle['label'], index=index,
                 theta_start_pi=str(F(2*index, CELLS_PER_CIRCLE)),
                 theta_end_pi=str(F(2*(index+1), CELLS_PER_CIRCLE)),
                 theta_midpoint_pi=str(F(2*index+1, CELLS_PER_CIRCLE)))
            for circle in CIRCLES for index in range(CELLS_PER_CIRCLE)]


def verify_saved_report(bindings):
    assert bindings[SAVED_RESULT] == SAVED_RESULT_SHA256
    assert bindings[SAVED_MANIFEST] == SAVED_MANIFEST_SHA256
    saved = json.loads((ROOT/SAVED_RESULT).read_text())
    old_manifest = json.loads((ROOT/SAVED_MANIFEST).read_text())
    assert saved['status'] == 'failed' and saved['verdict'] == 'inconclusive'
    assert saved['manifest_sha256'] == SAVED_MANIFEST_SHA256
    assert old_manifest['root_reviewed'] is True and old_manifest['peer_reviewed'] is True
    assert saved['files_sha256'] == saved['claimed_files_sha256'] == old_manifest['files_sha256']
    assert not any(saved.get(key) for key in ('error', 'changed_inputs', 'manifest_changed'))
    assert saved['precision_bits'] == 256 and saved['proposal_iterations_per_cell'] == 24
    assert saved['point_radius'] == POINT_RADIUS and saved['parameter_radius'] == CELL_RADIUS
    assert saved['circles'] == CIRCLES and saved['cells_per_circle'] == CELLS_PER_CIRCLE
    assert saved['adaptive_subdivisions'] == saved['retries'] == 0
    assert saved['unprocessed_inventory'] == []
    assert saved['inventory'] == fixed_inventory()
    assert len(saved['cells']) == 1024
    assert [cell['id'] for cell in saved['cells']] == [item['id'] for item in fixed_inventory()]
    assert saved['operation_counts'] == dict(
        equation_calls=26624, jacobian_calls=27648, dilogarithm_calls=12288,
        proposal_iterations=24576, point_inclusion_tests=1024,
        parameter_inclusion_tests=1024, action_evaluations=1024,
        comparison_evaluations=0, derivative_evaluations=1024)
    assert saved['summary']['attempted_cells'] == 1024
    assert saved['summary']['completed_cells'] == saved['summary']['positive_cells'] == 0
    ids = [item['id'] for item in fixed_inventory()]
    assert saved['summary']['failed_cell_ids'] == saved['summary']['nonpositive_cell_ids'] == ids
    return saved


def decode_real(record):
    """Union of both outward endpoint displays, including their printed radii."""
    COUNTS['decoded_real_intervals'] += 1
    assert isinstance(record['lower'], str) and isinstance(record['upper'], str)
    left, right = arb(record['lower']), arb(record['upper'])
    assert left.is_finite() and right.is_finite(), 'nonfinite saved endpoint'
    assert left.lower() <= right.upper(), 'reversed saved endpoint bounds'
    return left.union(right)


def decode_complex(record):
    return acb(decode_real(record['real']), decode_real(record['imag']))


def exact_upper(value):
    assert value.is_finite()
    return F(str(value.upper().fmpq()))


def check(cell, name, condition):
    cell['checks'].append(dict(name=name, passed=bool(condition)))
    assert condition, name


def classify(value):
    return 'positive' if value > 0 else 'negative' if value < 0 else 'inconclusive'


def complete_cell(saved, circle, cell):
    for key in ('id', 'circle', 'index', 'theta_start_pi', 'theta_end_pi', 'theta_midpoint_pi'):
        check(cell, 'saved inventory '+key, saved[key] == cell[key])
    check(cell, 'original failed status preserved', saved['status'] == 'failed' and saved['verdict'] == 'inconclusive')
    check(cell, 'only the prescribed interval-inverse failure',
          saved['error'] == 'ZeroDivisionError: matrix is singular'
          and 'inverse_cell = cell_jac.inv()' in saved['traceback'])
    check(cell, 'all original checks present and passed',
          [v['name'] for v in saved['checks']] == saved_check_names()
          and all(v['passed'] is True for v in saved['checks']))
    check(cell, 'original proposal inventory retained',
          len(saved['proposal_history']) == 24
          and [v['iteration'] for v in saved['proposal_history']] == list(range(1,25))
          and saved['final_center'] == saved['proposal_history'][-1]['centers'])
    check(cell, 'no old comparison or derivative enclosure promoted',
          saved['comparisons'] == [] and 'derivative_enclosures' not in saved)
    check(cell, 'both complete original inclusion inventories',
          set(saved['inclusions']) == {'midpoint', 'whole_cell'}
          and all(len(saved['inclusions'][tag]['rows']) == 5
                  and len(saved['inclusions'][tag]['coordinate_boxes']) == 5
                  for tag in ('midpoint', 'whole_cell')))
    check(cell, 'original operation counts', saved['operation_counts'] == dict(
        equation_calls=26, jacobian_calls=27, dilogarithm_calls=12,
        proposal_iterations=24, point_inclusion_tests=1,
        parameter_inclusion_tests=1, action_evaluations=1,
        comparison_evaluations=0, derivative_evaluations=1))

    row_bounds = {}
    decoded_inclusions = {}
    for tag, radius in (('midpoint', POINT_RADIUS), ('whole_cell', CELL_RADIUS)):
        check(cell, tag+': original fixed radius', F(saved['inclusions'][tag]['radius']) == F(radius))
        rows = []
        upper_bounds = []
        for i, original in enumerate(saved['inclusions'][tag]['rows']):
            derivative = decode_real(original['derivative_row'])
            image = decode_real(original['image_radius'])
            residual = decode_real(original['residual'])
            k_i = exact_upper(derivative)
            check(cell, f'{tag} row {i}: decoded contraction', 0 <= k_i < 1)
            check(cell, f'{tag} row {i}: decoded strict inclusion', exact_upper(image) < F(radius))
            rows.append(dict(derivative_row=real_ball(derivative),
                             image_radius=real_ball(image), residual=real_ball(residual),
                             exact_row_upper=str(k_i)))
            upper_bounds.append(k_i)
        row_bounds[tag] = upper_bounds
        decoded_inclusions[tag] = rows
    cell['decoded_inclusions'] = decoded_inclusions
    k_rows = row_bounds['whole_cell']
    k = max(k_rows)
    k_last = k_rows[4]

    uniform_box = [decode_complex(v) for v in saved['inclusions']['whole_cell']['coordinate_boxes']]
    outside = decode_complex(saved['external_cell'])
    t, z = uniform_box[3], uniform_box[4]
    check(cell, 'decoded original derivative logarithm strips',
          0 < z.real < 1 and 0 < (t+z).real < 1)
    check(cell, 'decoded original mixed derivative strip', 0 < (z+outside).real < 1)
    Y = saved['rational_inverse']
    check(cell, 'complete exact rational inverse', len(Y) == 5 and all(len(row) == 5 for row in Y)
          and all(len(entry) == 2 for row in Y for entry in row))
    last_column = [cp(Y[j][4]) for j in range(5)]
    m = max(exact_upper(abs(value)) for value in last_column)
    check(cell, 'positive finite saved inverse column bound', m > 0)
    center_c = cp(circle['center'])
    ctheta = II*(outside-center_c)
    halfwidth = decode_real(saved['theta_halfwidth'])
    check(cell, 'positive decoded angular halfwidth', halfwidth > 0)
    Q = (-2*PI*II*z).exp()
    C = (-2*PI*II*outside).exp()
    denominator = 1-Q*C
    check(cell, 'original mixed derivative denominator nonzero', abs(denominator) > 0)
    gamma = 2*PI*II/denominator
    response_center = -gamma*last_column[4]
    response_error = abs(gamma)*ar(k_last)*ar(m)/(1-ar(k))
    pprime = (2*(PI*(t+z)).sin()).log()-(2*(PI*z).sin()).log()-II*PI*t
    outgoing_radius = (2*PI*z.imag).exp()
    check(cell, 'decoded uniform outgoing radius', ar('1/2') < outgoing_radius < 1)
    beta = (2/(1+outgoing_radius*outgoing_radius)).log()/2
    ceiling_h = (-ar('6/25')+beta/10)*(-2*PI*outgoing_radius*outgoing_radius/(1+outgoing_radius*outgoing_radius))
    COUNTS['response_enclosures'] += 1
    check(cell, 'finite saved-response enclosure',
          all(v.real.is_finite() and v.imag.is_finite() for v in (gamma,response_center,pprime,ctheta))
          and response_error.is_finite() and ceiling_h.is_finite())
    cell['decoded_uniform_box'] = [complex_ball(v) for v in uniform_box]
    cell['decoded_external_cell'] = complex_ball(outside)
    cell['response'] = dict(row_upper_bounds=[str(v) for v in k_rows],
        k=str(k), k_last=str(k_last), m=str(m),
        exact_last_inverse_entry=Y[4][4], exact_last_inverse_column=[Y[j][4] for j in range(5)],
        gamma=complex_ball(gamma), center=complex_ball(response_center),
        error_radius=real_ball(response_error), pprime=complex_ball(pprime),
        parameter_angular_derivative=complex_ball(ctheta),
        uniform_outgoing_radius=real_ball(outgoing_radius), radial_beta=real_ball(beta),
        ceiling_height_derivative=real_ball(ceiling_h))

    bare = decode_complex(saved['bare_prefix_action_midpoint'])
    midpoint_radius = decode_real(saved['outgoing_radius_midpoint'])
    midpoint_beta = decode_real(saved['radial_beta_midpoint'])
    check(cell, 'decoded midpoint radius and beta domain',
          ar('1/2') < midpoint_radius < 1 and 0 < midpoint_beta < ar('7/20'))
    ceiling_mid = ar('17539/9600')-ar('23/64000')-ar('6/25')*midpoint_beta+midpoint_beta*midpoint_beta/20
    cell['decoded_midpoint_values'] = dict(bare_prefix_action=complex_ball(bare),
        outgoing_radius=real_ball(midpoint_radius), radial_beta=real_ball(midpoint_beta),
        angular_halfwidth=real_ball(halfwidth))
    for label, coefficient, bound in (
            ('real_initial', pprime, ar('7/4')),
            ('complete_complement', pprime+II*ceiling_h, ceiling_mid)):
        COUNTS['margin_comparisons'] += 1
        central_derivative = (coefficient*response_center*ctheta).real
        derivative_error = abs(coefficient)*abs(ctheta)*response_error
        derivative = central_derivative+arb(0,derivative_error.upper())
        debit = halfwidth*abs(derivative)
        midpoint_margin = bare.real-bound
        margin = midpoint_margin+arb(0,debit.upper())
        check(cell, label+': finite transported margin',
              derivative.is_finite() and debit.is_finite() and margin.is_finite())
        cell['comparisons'].append(dict(label=label,
            midpoint_ceiling=real_ball(bound), midpoint_margin=real_ball(midpoint_margin),
            midpoint_verdict=classify(midpoint_margin),
            central_real_derivative=real_ball(central_derivative),
            derivative_error_radius=real_ball(derivative_error),
            real_derivative=real_ball(derivative), transport_debit=real_ball(debit),
            whole_cell_margin=real_ball(margin), verdict=classify(margin)))
    signs = [v['verdict'] for v in cell['comparisons']]
    cell['verdict'] = ('both_cell_margins_positive' if all(v=='positive' for v in signs)
                       else 'a_cell_comparison_is_negative' if 'negative' in signs else 'inconclusive')
    cell['status'] = 'completed'


def main():
    global PI, II
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--manifest',type=Path,default=MANIFEST)
    args=parser.parse_args()
    if OUTPUT.exists():
        raise FileExistsError('the saved-only output already exists; no overwrite')
    inventory=fixed_inventory()
    result=dict(status='failed',verdict='inconclusive',precision_bits=256,
                original_result=SAVED_RESULT,original_result_sha256=SAVED_RESULT_SHA256,
                original_result_status='failed',circles=CIRCLES,cells_per_circle=CELLS_PER_CIRCLE,
                inventory=inventory,cells=[],unprocessed_inventory=[v['id'] for v in inventory],
                operation_counts=COUNTS,refinements=0,retries=0,
                scope='Saved-only completion of two source-piece margins on two full disks; old failed run unchanged; no whole-prefix or next-attachment conclusion.')
    frozen=None;manifest_hash=None
    try:
        manifest_hash=sha(args.manifest)
        result['manifest_sha256']=manifest_hash
        manifest=json.loads(args.manifest.read_text())
        result['claimed_files_sha256']=manifest.get('files_sha256',{})
        assert manifest['root_reviewed'] is True and manifest['peer_reviewed'] is True
        assert manifest['precision_bits']==256
        assert manifest['circle_inventory']==CIRCLES and manifest['cells_per_circle']==CELLS_PER_CIRCLE
        assert manifest['saved_result_sha256']==SAVED_RESULT_SHA256
        assert manifest['response_method']=='last_row_neumann_disk'
        assert manifest['output']==str(OUTPUT.relative_to(ROOT))
        frozen=verify_inputs(manifest)
        saved=verify_saved_report(frozen)
        result['files_sha256']=frozen
        ctx.prec=256
        PI,II=arb.pi(),acb(0,1)
        for position,item in enumerate(inventory):
            circle=CIRCLES[position//CELLS_PER_CIRCLE]
            cell=dict(item,status='failed',verdict='inconclusive',checks=[],comparisons=[])
            result['cells'].append(cell)
            before=dict(COUNTS)
            try:
                complete_cell(saved['cells'][position],circle,cell)
            except Exception as exc:
                cell['error']=f'{type(exc).__name__}: {exc}'
                cell['traceback']=traceback.format_exc()
            finally:
                cell['operation_counts']={key:COUNTS[key]-before[key] for key in COUNTS}
                result['unprocessed_inventory'].remove(cell['id'])
        assert [v['id'] for v in result['cells']]==[v['id'] for v in inventory]
        result['summary']=dict(attempted_cells=len(result['cells']),
            completed_cells=sum(v['status']=='completed' for v in result['cells']),
            positive_cells=sum(v['verdict']=='both_cell_margins_positive' for v in result['cells']),
            failed_cell_ids=[v['id'] for v in result['cells'] if v['status']!='completed'],
            nonpositive_cell_ids=[v['id'] for v in result['cells'] if v['verdict']!='both_cell_margins_positive'])
        if all(v['status']=='completed' for v in result['cells']):
            result['status']='completed'
            result['verdict']=('both_full_disks_have_positive_margins'
                if all(v['verdict']=='both_cell_margins_positive' for v in result['cells'])
                else 'complete_saved_inventory_recorded_no_full_disk_conclusion')
    except Exception as exc:
        result['error']=f'{type(exc).__name__}: {exc}'
        result['traceback']=traceback.format_exc()
    finally:
        def changed_or_missing(path,digest):
            try:return sha(path)!=digest
            except OSError:return True
        if frozen is not None:
            changed=[path for path,h in frozen.items() if changed_or_missing(ROOT/path,h)]
            if changed:
                result['changed_inputs']=changed;result['status']='failed';result['verdict']='inconclusive'
        if manifest_hash is not None and changed_or_missing(args.manifest,manifest_hash):
            result['manifest_changed']=True;result['status']='failed';result['verdict']='inconclusive'
        OUTPUT.parent.mkdir(parents=True,exist_ok=True)
        with OUTPUT.open('x') as stream:
            json.dump(result,stream,indent=2);stream.write('\n')
    print(json.dumps(dict(status=result['status'],verdict=result['verdict'],
                         summary=result.get('summary'),counts=COUNTS,output=str(OUTPUT))))
    if result['status']!='completed':raise SystemExit(1)


if __name__=='__main__':
    main()
