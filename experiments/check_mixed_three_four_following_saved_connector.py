#!/usr/bin/env python3
"""One saved-only complete vertical-connector comparison. UNRUN until approved."""
from fractions import Fraction as F
import argparse
import hashlib
import json
from pathlib import Path
import traceback

from flint import arb, ctx

ROOT = Path(__file__).resolve().parents[1]
PROTOCOL = "notes/research_mixed_three_four_following_saved_connector_protocol.md"
SCRIPT = "experiments/check_mixed_three_four_following_saved_connector.py"
MANIFEST = ROOT / "repro/protocols/research-mixed-three-four-following-saved-connector.json"
OUTPUT = ROOT / "repro/results/research-mixed-three-four-following-saved-connector-attempt01.json"
SAVED_RESULT = "repro/results/research-mixed-three-four-following-saved-response-attempt01.json"
SAVED_RESULT_SHA256 = "5bc3e5ff76ab5371e76bddb8d8fc32512ef16d9571d1991fb0c5f57dd39867c3"
SAVED_MANIFEST = "repro/protocols/research-mixed-three-four-following-saved-response.json"
SAVED_MANIFEST_SHA256 = "84fe02e65cb17575f5016e8d70e67c261b93ea4a65d9992c99f9ccd9cfb92859"
CELLS_PER_CIRCLE = 512
REQUIRED = {
 PROTOCOL, SCRIPT, SAVED_RESULT, SAVED_MANIFEST,
 "notes/research_mixed_transformed_vertical_connector.md",
 "notes/research_mixed_three_four_following_remainder_gaps.md",
 "notes/research_mixed_three_four_following_critical_curve.md",
 "notes/research_mixed_three_four_following_saved_response_protocol.md",
 "experiments/check_mixed_three_four_following_saved_response.py",
}
COUNTS = dict(decoded_real_intervals=0, ceiling_evaluations=0, margin_comparisons=0,
 new_roots=0, new_inclusions=0, new_hessians=0, new_matrix_inverses=0,
 new_response_derivatives=0, new_actions=0, new_dilogarithms=0)



CIRCLES = [
    {"label": "c3", "center": ["7/20", "-1/100"], "radius": "83/1000", "typed_radius": "9/100"},
    {"label": "c4", "center": ["3/10", "-13/250"], "radius": "3/50", "typed_radius": "8/125"},
]


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


def real_ball(value):
    return dict(ball=str(value), lower=str(value.lower()), upper=str(value.upper()))


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


def fixed_inventory():
    return [dict(id=f'{circle["label"]}:{index:03d}', circle=circle['label'], index=index,
                 theta_start_pi=str(F(2*index, CELLS_PER_CIRCLE)),
                 theta_end_pi=str(F(2*(index+1), CELLS_PER_CIRCLE)),
                 theta_midpoint_pi=str(F(2*index+1, CELLS_PER_CIRCLE)))
            for circle in CIRCLES for index in range(CELLS_PER_CIRCLE)]


def decode_real(record):
    """Union of both outward endpoint displays, including their printed radii."""
    COUNTS['decoded_real_intervals'] += 1
    assert isinstance(record['lower'], str) and isinstance(record['upper'], str)
    left, right = arb(record['lower']), arb(record['upper'])
    assert left.is_finite() and right.is_finite(), 'nonfinite saved endpoint'
    assert left.lower() <= right.upper(), 'reversed saved endpoint bounds'
    return left.union(right)


def exact_upper(value):
    assert value.is_finite()
    return F(str(value.upper().fmpq()))


def check(cell, name, condition):
    cell['checks'].append(dict(name=name, passed=bool(condition)))
    assert condition, name


def exact_lower(value):
    assert value.is_finite()
    return F(str(value.lower().fmpq()))


def verify_saved_report(bindings):
    assert bindings[SAVED_RESULT] == SAVED_RESULT_SHA256
    assert bindings[SAVED_MANIFEST] == SAVED_MANIFEST_SHA256
    saved = json.loads((ROOT/SAVED_RESULT).read_text())
    old_manifest = json.loads((ROOT/SAVED_MANIFEST).read_text())
    assert saved['status'] == 'completed' and saved['verdict'] == 'both_full_disks_have_positive_margins'
    assert saved['manifest_sha256'] == SAVED_MANIFEST_SHA256
    assert old_manifest['root_reviewed'] is True and old_manifest['peer_reviewed'] is True
    assert saved['files_sha256'] == saved['claimed_files_sha256'] == old_manifest['files_sha256']
    assert not any(saved.get(key) for key in ('error','changed_inputs','manifest_changed'))
    assert saved['precision_bits'] == 256 and saved['circles'] == CIRCLES
    assert saved['cells_per_circle'] == CELLS_PER_CIRCLE
    assert saved['unprocessed_inventory'] == [] and saved['refinements'] == saved['retries'] == 0
    assert saved['inventory'] == fixed_inventory() and len(saved['cells']) == 1024
    assert [v['id'] for v in saved['cells']] == [v['id'] for v in fixed_inventory()]
    assert saved['summary'] == dict(attempted_cells=1024,completed_cells=1024,positive_cells=1024,
                                    failed_cell_ids=[],nonpositive_cell_ids=[])
    assert saved['operation_counts'] == dict(decoded_real_intervals=48128,response_enclosures=1024,
      margin_comparisons=2048,new_roots=0,new_inclusions=0,new_hessians=0,new_matrix_inverses=0,
      new_actions=0,new_dilogarithms=0)
    assert saved['original_result_status'] == 'failed'
    assert saved['original_result_sha256'] == 'e2a6f208dd59f9e2d8044619aa70532c7945972b8d499af3e00880f9e580449b'
    return saved


def complete_cell(saved, cell):
    for key in ('id','circle','index','theta_start_pi','theta_end_pi','theta_midpoint_pi'):
        check(cell,'saved inventory '+key,saved[key] == cell[key])
    check(cell,'original completed positive result',saved['status']=='completed'
          and saved['verdict']=='both_cell_margins_positive')
    check(cell,'all original checks retained',len(saved['checks'])==46
          and len({v['name'] for v in saved['checks']})==46
          and all(v['passed'] is True for v in saved['checks']))
    check(cell,'both original positive comparisons retained',
          [v['label'] for v in saved['comparisons']]==['real_initial','complete_complement']
          and all(v['verdict']==v['midpoint_verdict']=='positive' for v in saved['comparisons']))
    check(cell,'full saved coordinate inventory',len(saved['decoded_uniform_box'])==5)
    check(cell,'saved operation scope',saved['operation_counts']==dict(
        decoded_real_intervals=47,response_enclosures=1,margin_comparisons=2,new_roots=0,
        new_inclusions=0,new_hessians=0,new_matrix_inverses=0,new_actions=0,new_dilogarithms=0))
    ah = decode_real(saved['decoded_uniform_box'][1]['imag'])
    qh = decode_real(saved['decoded_uniform_box'][4]['imag'])
    initial_margin = decode_real(saved['comparisons'][0]['whole_cell_margin'])
    complement_margin = decode_real(saved['comparisons'][1]['whole_cell_margin'])
    check(cell,'decoded original margins remain positive',initial_margin>0 and complement_margin>0)
    a_lower,a_upper = exact_lower(ah),exact_upper(ah)
    q_upper = exact_upper(qh)
    cell['decoded_values']=dict(incoming_height=real_ball(ah),outgoing_height=real_ball(qh),
        original_initial_margin=real_ball(initial_margin),original_complement_margin=real_ball(complement_margin),
        incoming_height_lower=str(a_lower),incoming_height_upper=str(a_upper),outgoing_height_upper=str(q_upper))
    check(cell,'whole-cell incoming height strictly negative',a_upper<0)
    delta_from_height = -2*PI*ar(a_lower)
    delta = max(F(11,50),exact_upper(delta_from_height))
    check(cell,'whole-cell connector depth below one half',delta<F(1,2))
    radius_enclosure = (2*PI*ar(q_upper)).exp()
    radius = exact_upper(radius_enclosure)
    check(cell,'whole-cell outgoing radius in range',F(1,2)<radius<1)
    D,R = ar(delta),ar(radius)
    beta = (2/(1+R*R)).log()/2
    u = D/2-beta
    check(cell,'admitted beta and increasing-convex range',0<=beta<ar('7/20')
          and -ar('7/20')<=u<=ar('1/4'))
    square0=u*u
    square1=(u-ar('1/10'))*(u-ar('1/10'))
    square_upper=max(exact_upper(square0),exact_upper(square1))
    hyperbolic=arb(3).sqrt()*(D/2).sinh()**2/(2*PI)
    B0=ar('1549/1500')
    d0=ar('7/40')-ar('3/512')+ar('73/125')
    lower_rows=B0+d0+u/4+ar(square_upper)/20+hyperbolic
    upper_rows=B0+D+ar('1/3')
    COUNTS['ceiling_evaluations']+=1
    check(cell,'finite elementary connector bounds',all(v.is_finite() for v in
          (beta,u,square0,square1,hyperbolic,lower_rows,upper_rows)))
    ceiling_upper=max(exact_upper(lower_rows),exact_upper(upper_rows))
    action_enclosure=initial_margin+ar('7/4')
    action_lower=exact_lower(action_enclosure)
    margin=action_lower-ceiling_upper
    COUNTS['margin_comparisons']+=1
    cell['connector']=dict(delta_from_height=real_ball(delta_from_height),delta_upper=str(delta),
        radius_enclosure=real_ball(radius_enclosure),radius_upper=str(radius),
        beta=real_ball(beta),u=real_ball(u),square_u=real_ball(square0),square_u_minus_tenth=real_ball(square1),
        square_max_upper=str(square_upper),hyperbolic_term=real_ball(hyperbolic),
        lower_row_ceiling=real_ball(lower_rows),upper_row_ceiling=real_ball(upper_rows),
        exact_ceiling_upper=str(ceiling_upper))
    cell['comparison']=dict(saved_full_cell_action=real_ball(action_enclosure),
        exact_action_lower=str(action_lower),exact_ceiling_upper=str(ceiling_upper),
        exact_margin_lower=str(margin),margin_lower_display=real_ball(ar(margin)),
        verdict='positive' if margin>0 else 'inconclusive')
    cell['status']='completed'
    cell['verdict']='connector_margin_positive' if margin>0 else 'inconclusive'


def main():
    global PI
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--manifest',type=Path,default=MANIFEST)
    args=parser.parse_args()
    if OUTPUT.exists():raise FileExistsError('the single saved-only connector output exists; no overwrite')
    inventory=fixed_inventory()
    result=dict(status='failed',verdict='inconclusive',precision_bits=256,
        original_result=SAVED_RESULT,original_result_sha256=SAVED_RESULT_SHA256,
        circles=CIRCLES,cells_per_circle=CELLS_PER_CIRCLE,inventory=inventory,
        cells=[],unprocessed_inventory=[v['id'] for v in inventory],operation_counts=COUNTS,
        refinements=0,retries=0,
        scope='One complete vertical connector comparison using saved full-cell data. No new roots/actions or next Fourier observation.')
    frozen=None;manifest_hash=None
    try:
        manifest_hash=sha(args.manifest);result['manifest_sha256']=manifest_hash
        manifest=json.loads(args.manifest.read_text())
        result['claimed_files_sha256']=manifest.get('files_sha256',{})
        assert manifest['root_reviewed'] is True and manifest['peer_reviewed'] is True
        assert manifest['precision_bits']==256 and manifest['circle_inventory']==CIRCLES
        assert manifest['cells_per_circle']==CELLS_PER_CIRCLE
        assert manifest['saved_result_sha256']==SAVED_RESULT_SHA256
        assert manifest['comparison_method']=='vertical_ceiling_whole_cell'
        assert manifest['output']==str(OUTPUT.relative_to(ROOT))
        frozen=verify_inputs(manifest);saved=verify_saved_report(frozen)
        result['files_sha256']=frozen
        ctx.prec=256;PI=arb.pi()
        for position,item in enumerate(inventory):
            cell=dict(item,status='failed',verdict='inconclusive',checks=[])
            result['cells'].append(cell);before=dict(COUNTS)
            try:complete_cell(saved['cells'][position],cell)
            except Exception as exc:
                cell['error']=f'{type(exc).__name__}: {exc}';cell['traceback']=traceback.format_exc()
            finally:
                cell['operation_counts']={key:COUNTS[key]-before[key] for key in COUNTS}
                result['unprocessed_inventory'].remove(cell['id'])
        assert [v['id'] for v in result['cells']]==[v['id'] for v in inventory]
        result['summary']=dict(attempted_cells=len(result['cells']),
            completed_cells=sum(v['status']=='completed' for v in result['cells']),
            positive_cells=sum(v['verdict']=='connector_margin_positive' for v in result['cells']),
            failed_cell_ids=[v['id'] for v in result['cells'] if v['status']!='completed'],
            nonpositive_cell_ids=[v['id'] for v in result['cells'] if v['verdict']!='connector_margin_positive'])
        if all(v['status']=='completed' for v in result['cells']):
            result['status']='completed'
            result['verdict']=('both_full_disks_have_positive_connector_margins'
                if all(v['verdict']=='connector_margin_positive' for v in result['cells'])
                else 'complete_saved_inventory_recorded_no_full_disk_connector_conclusion')
    except Exception as exc:
        result['error']=f'{type(exc).__name__}: {exc}';result['traceback']=traceback.format_exc()
    finally:
        def changed_or_missing(path,digest):
            try:return sha(path)!=digest
            except OSError:return True
        if frozen is not None:
            changed=[p for p,h in frozen.items() if changed_or_missing(ROOT/p,h)]
            if changed:result['changed_inputs']=changed;result['status']='failed';result['verdict']='inconclusive'
        if manifest_hash is not None and changed_or_missing(args.manifest,manifest_hash):
            result['manifest_changed']=True;result['status']='failed';result['verdict']='inconclusive'
        OUTPUT.parent.mkdir(parents=True,exist_ok=True)
        with OUTPUT.open('x') as stream:json.dump(result,stream,indent=2);stream.write('\n')
    print(json.dumps(dict(status=result['status'],verdict=result['verdict'],summary=result.get('summary'),
                         counts=COUNTS,output=str(OUTPUT))))
    if result['status']!='completed':raise SystemExit(1)


if __name__=='__main__':main()
