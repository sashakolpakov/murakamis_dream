#!/usr/bin/env python3
"""Exact saved real-face reserves at four original canonical references.

Standard library only. No old module, root, primitive, source, optimizer,
interval package or analytic evaluation is imported or executed.
"""
import argparse
from fractions import Fraction as F
import hashlib
import itertools
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
PROOF = 'notes/research_mixed_terminal_canonical_face_reserve.md'
SOURCE = 'repro/results/research-mixed-terminal-joint-main-budget-diagnostic.json'
AUDIT = 'repro/results/research-mixed-terminal-joint-main-budget-saved-audit.json'
PLANE = 'repro/results/research-mixed-terminal-reserved-plane-transfer.json'
PLANE_CHECKER = 'experiments/check_mixed_terminal_reserved_plane_transfer.py'
ROOT_AUTHOR = 'repro/results/research-mixed-open-word-critical-localization.json'
ROOT_REPLAY = 'repro/results/research-mixed-open-word-critical-localization-replay.json'
REQUIRED = F(11, 200)
NUMBER = r'[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?'
BALL = re.compile(r'\[('+NUMBER+r') \+/- ('+NUMBER+r')\]')
DISKS = ((F(7,20),-F(1,100),F(9,100)),
         (F(3,10),-F(13,250),F(8,125)))
SERIES = {
    'three_mixed': {
        'epsilon':0, 'families':8, 'cells':3347,
        'author':'repro/results/research-mixed-terminal-three-mixed-faces-attempt01.json',
        'replay':'repro/results/research-mixed-terminal-three-mixed-faces-replay.json',
        'proof':'notes/research_mixed_terminal_three_mixed_face_certificate.md',
        'script':'experiments/certify_mixed_terminal_three_mixed_faces.py'},
    'three_half': {
        'epsilon':0, 'families':1, 'cells':3347,
        'author':'repro/results/research-mixed-terminal-three-right-face-attempt01.json',
        'replay':'repro/results/research-mixed-terminal-three-right-face-replay.json',
        'proof':'notes/research_mixed_terminal_three_right_face_certificate.md',
        'script':'experiments/certify_mixed_terminal_three_right_face.py'},
    'four': {
        'epsilon':1, 'families':21, 'cells':1911,
        'author':'repro/results/research-mixed-terminal-four-source-stage4-attempt01.json',
        'replay':'repro/results/research-mixed-terminal-four-source-replay.json',
        'proof':'notes/research_mixed_terminal_four_coupled_source_continuation.md',
        'script':'experiments/continue_mixed_terminal_four_source_coupled.py'},
}
PINNED = {'experiments/certify_mixed_open_word_critical_localization.py': '49704425b4f1a0fc7613284080e9d50e56afa087b518a51bd9c49d079ca47e00',
 'experiments/certify_mixed_terminal_four_source.py': 'ded3dc6dfca6ed6206251b32139a7e0d7051b85a1e53306b297671f00b706ccf',
 'experiments/certify_mixed_terminal_three_mixed_faces.py': '23df5797e35340e5a5537ee3ce811e0da61e3517cbb6dc9adbf4ec1f43574267',
 'experiments/certify_mixed_terminal_three_right_face.py': '689596824317a198f082b5c4db3825ec616654d9f65ccedc1b1e039814b1e707',
 'experiments/check_mixed_terminal_joint_main_budget_record.py': '80dc2c9e9dae3cdf55696a2cf92b5f9587be1af7c7b225743f8353bb8343d57b',
 'experiments/check_mixed_terminal_reserved_plane_transfer.py': 'b471d62e1f672d6ce15959de609ddd5e06d9372d5c394a2d1960332fe3294c36',
 'experiments/continue_mixed_terminal_four_source_coupled.py': '08b6f5b2eab5abc5ad2a4ab424034256f55c0211b08c04f2f1eda4fe4cc5de9d',
 'notes/research_mixed_open_word_critical_localization.md': 'a3f8a0f781abd43f8ca17321171081ba37c91b284f83f22a4f7ae34e270424fa',
 'notes/research_mixed_open_word_endpoint_rectangles.md': 'ac5603badc00d42e98d17a1c5948cae011a6abd991d5249fa61d4224a829ad07',
 'notes/research_mixed_terminal_canonical_face_reserve.md': '45d3def413d15478b3fe968409f98b3730f686a9124195b1e718b5afe027ed8e',
 'notes/research_mixed_terminal_four_alias_reserve.md': '02619c9f58624475deb1b88d39125b907b37e97fa4d6b94a1573a4fe5a965eaa',
 'notes/research_mixed_terminal_four_coupled_source_continuation.md': 'ee52ddb19be76ed0147a2e23309f2feafd812b4f8758eecabdd3096b8f0b0830',
 'notes/research_mixed_terminal_four_right_triangle.md': '66457f4789fa5898066cc693dd98d2ece1e34c48af65798603bd65d1d6f03920',
 'notes/research_mixed_terminal_four_selected_height_completion.md': '5b688d2adf67895f430a2fef77a5d98fcb8ac74846ebc2bbe1027cd6e3414127',
 'notes/research_mixed_terminal_four_source_certificate.md': '3166c5343b4a079f07e80beb80bc3e25f3107343fe079cab07a5ff682029ebe3',
 'notes/research_mixed_terminal_horizontal_envelope_diagnostic.md': 'ea1e6d1daf4b8e3822a198de1f63f4f211061761af8bdd01d641b4d8f930ad72',
 'notes/research_mixed_terminal_reserved_plane_transfer.md': '0d4461c5b00e4f68dc00c0c1d6e824156c9c5050327eab70694f3cd21e714c70',
 'notes/research_mixed_terminal_selected_height_rows.md': 'f282382e106a7669592ae5bf2755c307613a72780b957e3966e5b21ba9bb03e3',
 'notes/research_mixed_terminal_three_alias_reserve.md': '8780ddc96481a15f6b75e54ed7311a7f4e6272c7969056c8f63265f7e5cb6d82',
 'notes/research_mixed_terminal_three_critical_curve.md': 'bc279f1acb8751c752ebd630f765b9e43d76e6a7f59f979d713b194feb93dfda',
 'notes/research_mixed_terminal_three_full_completion.md': 'c1374b63ad8fb5d71fcb717a1d90961b683e8b1ec4415fe772469e8a5d28cfb5',
 'notes/research_mixed_terminal_three_mixed_face_certificate.md': 'c44701087a66f5c6397561b641a47a772175d0dc03749d4679144df0b5e57246',
 'notes/research_mixed_terminal_three_right_face_certificate.md': '36b811d4f9d414abea264f280f3719778bacdf47a57faefe4f60be50f79b1d4f',
 'notes/research_mixed_terminal_three_right_triangle.md': '034a79e2f3406e4aebcb01a62ac4f3ba9817b97dfb4974666c87169e941fb81c',
 'notes/research_mixed_terminal_three_selected_height_completion.md': 'e3fea31226612be459f23e8cec8773503e562799cced20b36efcc0e4cd70e186',
 'repro/results/research-mixed-open-word-critical-localization-replay.json': '2b5d91f8fbfa860d978f7b2076270b33bbe40d7410d39e91c9733e41b03ec247',
 'repro/results/research-mixed-open-word-critical-localization.json': 'ac2991d4cd5b7a78d202a237efebf98a9ad7ab77b6bacc4ab82568b8aa3cdad5',
 'repro/results/research-mixed-terminal-four-source-replay.json': '3b38c1f62ee63f537db1ec2209bb9e278cc273b477dec03b7e0f15fb7f57cf79',
 'repro/results/research-mixed-terminal-four-source-stage4-attempt01.json': 'e3651c4ec370625b6be4b8a93ab000730926c33d4062162c7188d0712d56f5d3',
 'repro/results/research-mixed-terminal-joint-main-budget-diagnostic.json': '2b6e9b17d1a16071c545c0ba9f9bb2502e1f18c5009fafc1212fd326d2a621f9',
 'repro/results/research-mixed-terminal-joint-main-budget-saved-audit.json': 'fceffb2a2bfe677579bb6ff94087b5129c9db0daf8f85674b94ee6de7fa3dda6',
 'repro/results/research-mixed-terminal-reserved-plane-transfer.json': 'b9ce042d50911acbd5e87fa755a5b9a50393845035b3dba984c07f7e6d759ffe',
 'repro/results/research-mixed-terminal-three-mixed-faces-attempt01.json': '2ab91d18d9f89ca76d1af6e617ea0460b3b87627d845ffc4fda4d1598a626032',
 'repro/results/research-mixed-terminal-three-mixed-faces-replay.json': '8fdb997394efeb5fc87b224cbd848e3706521d25a55adc6599fb3820e2ba75aa',
 'repro/results/research-mixed-terminal-three-right-face-attempt01.json': 'e3dfac0bfb95122cff5db4e75b3c71798ef2a76a9b62161a27d5fd4c77abc15b',
 'repro/results/research-mixed-terminal-three-right-face-replay.json': '2d3f6b86bbdc3e714cf346ae32c302a35cbb09d9b55740a054df54af6c13c33a'}


def sha(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for part in iter(lambda: stream.read(1048576), b''):
            h.update(part)
    return h.hexdigest()


def canonical_sha(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',',':')).encode()).hexdigest()


def interval(value):
    assert value['finite'] is True
    lo, hi = F(value['lower_rational']), F(value['upper_rational'])
    assert lo <= hi
    return lo, hi


def encoded(box):
    return [[str(lo),str(hi)] for lo,hi in box]


def split(box, axis):
    lo, hi = box[axis]
    mid = (lo+hi)/2
    left, right = list(box), list(box)
    left[axis], right[axis] = (lo,mid), (mid,hi)
    return tuple(left), tuple(right)


def excluded_disk(box):
    return sum(min(lo*lo,hi*hi) if lo*hi > 0 else F(0)
               for lo,hi in box) > 1


def intersect(a, b):
    result = tuple((max(x[0],y[0]), min(x[1],y[1])) for x,y in zip(a,b))
    return None if any(lo > hi for lo,hi in result) else result


def area(box):
    return (box[0][1]-box[0][0])*(box[1][1]-box[1][0])


def physical(box, neighbor):
    x,y,r = DISKS[neighbor]
    return ((x+r*box[0][0],x+r*box[0][1]),
            (y+r*box[1][0],y+r*box[1][1]))


def rectangle_in_disk(box, center, radius):
    return sum(max((lo-c)**2,(hi-c)**2)
               for (lo,hi),c in zip(box,center)) < radius**2


def outward_saved_upper(value):
    assert isinstance(value, str)
    m = BALL.fullmatch(value)
    if m:
        midpoint, radius = map(F,m.groups())
        assert radius >= 0
        return midpoint+radius
    raise AssertionError(('not an outward Arb ball display',value))


def root_cells(author, replay):
    assert author['domains'] == replay['domains']
    assert replay['input_sha256'] == PINNED[ROOT_AUTHOR]
    assert author['domain_count'] == replay['domain_count'] == 4
    assert [(d['epsilon'],d['neighbor_epsilon']) for d in author['domains']] == list(itertools.product((0,1),repeat=2))
    cells = {0:[],1:[]}
    excluded = {0:[],1:[]}
    counts = []
    total_nodes = 0
    for di, domain in enumerate(author['domains']):
        stack = [(((F(-1),F(1)),(F(-1),F(1))),0,'')]
        leaves = omissions = 0
        terminal_mass = F(0)
        eps, neighbor = domain['epsilon'],domain['neighbor_epsilon']
        for ni,node in enumerate(domain['tree']):
            assert stack
            box,depth,address = stack.pop()
            total_nodes += 1
            if node[0] == 'S':
                assert len(node) == 2 and node[1] == depth%2
                left,right = split(box,node[1])
                stack.extend([(left,depth+1,address+'0'),(right,depth+1,address+'1')])
            else:
                terminal_mass += F(1,2**depth)
                if node[0] == 'X':
                    assert len(node) == 1 and excluded_disk(box)
                    omissions += 1
                    if neighbor == 1:
                        excluded[eps].append(physical(box,neighbor))
                else:
                    assert node[0] == 'L' and len(node) == 2 and not excluded_disk(box)
                    leaves += 1
                    cells[eps].append({'index':len(cells[eps]),'domain':di,'node':ni,
                        'neighbor':neighbor,'address':address,'depth':depth,'box':box,
                        'physical':physical(box,neighbor),
                        'original_node_canonical_sha256':canonical_sha(node)})
        assert not stack and terminal_mass == 1
        assert (leaves,omissions) == (domain['leaves'],domain['excluded'])
        counts.append({'epsilon':eps,'neighbor_epsilon':neighbor,'leaves':leaves,
                       'excluded':omissions,'terminal_mass_rational':str(terminal_mass)})
    assert [v['leaves'] for v in counts] == [1645,1702,1002,909]
    assert (total_nodes,sum(v['leaves'] for v in counts),sum(v['excluded'] for v in counts)) == (10978,5258,233)
    assert (len(cells[0]),len(cells[1])) == (3347,1911)
    return cells,excluded,counts


def four_inventory():
    ts, es = ('3/20','1/2'), ('27/100','49/100')
    ans = [['flat_t',t,None,'0','0','0','1'] for t in ts]
    ans += [['flat_e',None,e,'0','0','1','0'] for e in es]
    ans += [['corner',t,e,'0','0','0','0'] for t in ts for e in es]
    ans += [['t_alias',None,None,h,'0','0',keep] for h in ('-3/25','3/25') for keep in ('0','1')]
    ans += [['e_alias',None,None,'0',h,keep,'0'] for h in ('-11/200','1/25') for keep in ('0','1')]
    ans += [['double_alias',None,None,t,e,'0','0'] for t in ('-3/25','3/25') for e in ('-11/200','1/25')]
    ans += [['raw_half','1/2',None,'0','0','0','0']]
    return ans


def target_intervals(key, family):
    a,t = (F(11,50),F(9,20)),(F(3,20),F(1,2))
    private = (F(1,10),F(2,5)) if key != 'four' else (F(27,100),F(49,100))
    if key == 'three_half':
        return [a,private]
    if key == 'four' and family == 20:
        return [a,private,(F(1,10),F(269,1000))]
    if family < 2:
        return [a,private]
    if family < 4:
        return [a,t]
    if family < 8:
        return [a]
    return [a,t,private]


def verify_source_tree(tree, summary, box, key, family):
    stack = [box]
    kinds = {'S':0,'L':0,'X':0,'F':0}
    for node in tree:
        assert stack
        current = stack.pop()
        kind = node[0]
        assert kind in kinds and (key == 'four' or kind != 'F')
        kinds[kind] += 1
        if kind == 'S':
            assert len(node) == 2 and node[1] in (0,1)
            left,right = split(current,node[1])
            stack.extend([left,right])
        elif kind == 'L':
            assert len(node) == 2
            trial = list(map(F,node[1]))
            if family < 8 or key == 'three_half' or family == 20:
                bounds = target_intervals(key,family)
                assert len(trial) == len(bounds)
                assert all(lo <= x <= hi for x,(lo,hi) in zip(trial,bounds))
            else:
                # All alias families have the same full three-real target product;
                # their exact order is (a,t,e), as in the original target_box().
                assert len(trial) == 3
                assert F(11,50) <= trial[0] <= F(9,20)
                assert F(3,20) <= trial[1] <= F(1,2)
                assert F(27,100) <= trial[2] <= F(49,100)
        elif kind == 'X':
            assert len(node) == 1
            if key != 'four':
                assert excluded_disk(current)
        else:
            assert len(node) == 2 and set(node[1]) == {'m2','m3'}
            assert node[1]['m2'] in ('attached_real_floor','attached_fixed_point')
            assert node[1]['m3'] in ('opposite_half_plane','external_half_plane',
                                    'opposite_outside_P4','external_outside_both_P')
    assert not stack and kinds['L']+kinds['X']+kinds['F'] == kinds['S']+1
    if key == 'four':
        tiers = ('first_stage','second_stage','third_stage','new')
        assert len(tree) == summary['nodes']
        assert kinds['L'] == sum(summary[t+'_leaves'] for t in tiers)
        assert kinds['X'] == sum(summary[t+'_exclusions'] for t in tiers)
        assert kinds['F'] == summary['inverse_exclusions']
    else:
        assert (kinds['L'],kinds['X']) == (summary['leaves'],summary['exclusions'])
    value = summary['maximum_upper']
    if kinds['L']:
        assert value is not None
        upper = outward_saved_upper(value)
        assert upper < 0  # Only the new exact threshold test decides the reserve.
        return upper
    assert value is None and kinds['X']+kinds['F'] > 0
    return None


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args = parser.parse_args()
    assert not args.output.exists(), 'use a fresh immutable output path'
    assert PINNED and PROOF in PINNED
    inputs = dict(PINNED)
    own = Path(__file__).resolve().relative_to(ROOT).as_posix()
    inputs[own] = sha(ROOT/own)

    def bind(name,digest):
        assert isinstance(digest,str) and len(digest) == 64
        assert name not in inputs or inputs[name] == digest, name
        assert sha(ROOT/name) == digest, name
        inputs[name] = digest

    def inherited(record):
        for key in ('input_sha256','dependencies_sha256','dependencies'):
            values = record.get(key)
            if isinstance(values,dict):
                for name,digest in values.items():
                    bind(name,digest)

    for name,digest in list(inputs.items()):
        bind(name,digest)
    source = json.loads((ROOT/SOURCE).read_text())
    audit = json.loads((ROOT/AUDIT).read_text())
    assert source['status'] == 'complete fixed diagnostic' and source['changed_inputs'] == []
    assert source['precision_bits'] == 256 and F(source['height_rational']) == F(1,100)
    assert audit['status'] == 'passed' and audit['source_path'] == SOURCE
    assert audit['source_sha256'] == inputs[SOURCE]
    assert audit['checker_sha256'] == inputs['experiments/check_mixed_terminal_joint_main_budget_record.py']
    assert audit['branch_bounds_checked'] == 8 and audit['certified_reference_associations_checked'] == 4
    inherited(source); inherited(audit)
    assert [(r['beta'],r['epsilon']) for r in source['cases']] == list(itertools.product((0,1),repeat=2))
    plane = json.loads((ROOT/PLANE).read_text())
    assert plane['status'] == 'passed' and plane['changed_inputs'] == []
    assert plane['source_path'] == SOURCE and plane['source_sha256'] == inputs[SOURCE]
    assert plane['checker_sha256'] == inputs[PLANE_CHECKER]
    assert plane['proof_sha256'] == inputs['notes/research_mixed_terminal_reserved_plane_transfer.md']
    assert plane['canonical_reference_cases_checked'] == 4 and plane['joined_plane_alternatives_checked'] == 8
    assert F(plane['selected_height_rational']) == F(1,100)
    assert F(plane['common_plane_upper_rational']) == REQUIRED
    assert [(r['beta'],r['epsilon']) for r in plane['canonical_cases']] == list(itertools.product((0,1),repeat=2))
    inherited(plane)
    roots,replay = [json.loads((ROOT/n).read_text()) for n in (ROOT_AUTHOR,ROOT_REPLAY)]
    for record in (roots,replay):
        assert record['status'] == 'passed'
        bind('notes/research_mixed_open_word_critical_localization.md',record['proof_sha256'])
        bind('experiments/certify_mixed_open_word_critical_localization.py',record['script_sha256'])
        inherited(record)
    cells,excluded,partition = root_cells(roots,replay)
    decoded = {}
    source_summary_counts = {}
    for key,spec in SERIES.items():
        author,saved = [json.loads((ROOT/spec[n]).read_text()) for n in ('author','replay')]
        assert saved['input_sha256'] == inputs[spec['author']]
        for record in (author,saved):
            assert record['status'] == 'passed' and record['active'] is None
            assert record['fatal_error'] is None and record['final_bindings_verified'] is True
            assert record['original_own_'+('three' if spec['epsilon']==0 else 'four')+'_cells'] == spec['cells']
            assert record['face_families_per_cell'] == spec['families']
            assert record['job_count'] == spec['cells']*spec['families']
            bind(spec['proof'],record['proof_sha256']); bind(spec['script'],record['script_sha256'])
            inherited(record)
            if key == 'four':
                assert record['family_inventory'] == four_inventory()
            if key == 'three_half':
                assert record['family'] == {'t':'1/2','t_height':'0','u_height':'0','alias_penalty':'0'}
        assert author['completed'] == saved['completed']
        assert saved['precision_bits'] == 320
        zero_fields = ('additional_nodes','attempted_nodes','root_proposals','target_proposals','refinements') if key=='four' else ('new_nodes','root_proposals','target_proposals','refinements')
        assert all(saved[k] == 0 for k in zero_fields)
        assert len(saved['completed']) == len(saved['replay_summaries']) == spec['cells']*spec['families']
        bounds = []
        for job,(tree,summary) in enumerate(zip(saved['completed'],saved['replay_summaries'])):
            assert summary['job'] == job
            ci,fi = divmod(job,spec['families'])
            value = verify_source_tree(tree,summary,cells[spec['epsilon']][ci]['box'],key,fi)
            bounds.append((value,summary))
        decoded[key] = bounds
        source_summary_counts[key] = {'all_jobs_checked':len(bounds),
            'finite_jobs':sum(v is not None for v,_ in bounds),
            'null_jobs':sum(v is None for v,_ in bounds),
            'family_count':spec['families'],'original_cell_count':spec['cells']}

    cases = []
    for row,plane_row in zip(source['cases'],plane['canonical_cases']):
        eps,beta = row['epsilon'],row['beta']
        assert (plane_row['beta'],plane_row['epsilon'],plane_row['source_index'],plane_row['source_case_sha256']) == (
            beta,eps,row['source_index'],row['source_case_sha256'])
        assert plane_row['original_height_and_source_guards_verified']
        assert F(plane_row['selected_height_rational']) == F(1,100)
        plane_bounds = {name:F(value) for name,value in plane_row['joined_plane_upper_rational'].items()}
        assert set(plane_bounds) == {'factorial','forced'}
        plane_upper = max(plane_bounds.values())
        assert plane_upper < REQUIRED
        assert row['status'] == 'both main-current bounds enclosed'
        q = row['actual_coordinate_enclosures']
        abox = (interval(q['a']['real']),interval(q['a']['imag']))
        assert all(lo < hi for lo,hi in abox), 'positive enclosure widths required'
        assert F(11,50) < abox[0][0] <= abox[0][1] < F(9,20)
        assert -F(27,250) < abox[1][0] <= abox[1][1] < -F(1,1000)
        scope_guards = {'actual_negative_type_four_input':True}
        if eps == 1:
            assert abox[0][0] > F(259,1000)
            assert rectangle_in_disk(abox,(F(3,10),-F(13,250)),F(3,50))
            sbox = (interval(q['s']['real']),interval(q['s']['imag']))
            assert F(6,25) < sbox[0][0] <= sbox[0][1] < F(9,25)
            assert -F(51,500) < sbox[1][0] <= sbox[1][1] < -F(1,1000)
            assert rectangle_in_disk(sbox,(F(3,10),-F(13,250)),F(3,50))
            b = tuple(map(F,row['outside_coordinate_rational']))
            assert b == DISKS[beta][:2]
            b_radius = F(83,1000) if beta == 0 else F(3,50)
            assert rectangle_in_disk(tuple((x,x) for x in b),DISKS[beta][:2],b_radius)
            scope_guards.update(oriented_real_floor=True,reduced_input_disk=True,
                inverse_preceding_ordinary_four_leg=True,
                inverse_external_typed_disk=True,
                inverse_identity_source='original certified canonical ordinary equations')
        cr,ci,r = DISKS[1]
        normalized = (((abox[0][0]-cr)/r,(abox[0][1]-cr)/r),
                      ((abox[1][0]-ci)/r,(abox[1][1]-ci)/r))
        maximum_norm_squared = sum(max(lo*lo,hi*hi) for lo,hi in normalized)
        assert maximum_norm_squared < 1
        assert all(intersect(abox,box) is None for box in excluded[eps])
        selected = [cell for cell in cells[eps] if cell['neighbor']==1 and intersect(abox,cell['physical']) is not None]
        assert selected
        pieces = [intersect(abox,cell['physical']) for cell in selected]
        assert sum(map(area,pieces)) == area(abox)
        # The reconstructed disjoint-interior closed partition, with every
        # intersecting leaf retained, also covers edges and degenerate contacts.
        requests = [('three_mixed',i) for i in range(8)]+[('three_half',0)] if eps==0 else [('four',i) for i in range(8)]+[('four',20)]
        families = []
        for key,fi in requests:
            contributions = []
            nulls = []
            for cell in selected:
                job = SERIES[key]['families']*cell['index']+fi
                value,summary = decoded[key][job]
                item = {'job':job,'original_cell_index':cell['index'],
                    'summary_canonical_sha256':canonical_sha(summary),
                    'saved_maximum_upper':summary['maximum_upper'],
                    'decoded_upper_rational':None if value is None else str(value)}
                contributions.append(item)
                if value is None:
                    nulls.append(job)
            finite = [F(v['decoded_upper_rational']) for v in contributions if v['decoded_upper_rational'] is not None]
            upper = max(finite) if finite else None
            complete = not nulls and upper is not None
            passed = complete and upper < -REQUIRED
            families.append({'series':key,'family':fi,'contributing_jobs':contributions,
                'null_jobs_unresolved':nulls,'complete_finite_coverage':complete,
                'maximum_upper_rational':None if upper is None else str(upper),
                'attaining_jobs':[] if upper is None else [v['job'] for v in contributions if v['decoded_upper_rational'] is not None and F(v['decoded_upper_rational'])==upper],
                'signed_excess_over_threshold_rational':None if upper is None else str(upper+REQUIRED),
                'gap_after_plane_ceiling_rational':None if not complete else str(-upper-REQUIRED),
                'strictly_pays_11over200':passed,
                'case_joined_upper_rational':None if not complete else str(upper+plane_upper),
                'case_branch_joined_uppers_rational':None if not complete else {
                    name:str(upper+value) for name,value in plane_bounds.items()},
                'case_joined_gap_rational':None if not complete else str(-upper-plane_upper),
                'strictly_pays_case_plane':complete and upper+plane_upper < 0})
        cases.append({'beta':beta,'epsilon':eps,'endpoint_neighbor_epsilon':1,
            'source_index':row['source_index'],'source_case_sha256':row['source_case_sha256'],
            'diagnostic_row_canonical_sha256':canonical_sha(row),
            'original_source_scope_guards':scope_guards,
            'joined_plane_record_path':PLANE,
            'joined_plane_case_canonical_sha256':canonical_sha(plane_row),
            'joined_plane_upper_rational':{name:str(value) for name,value in plane_bounds.items()},
            'largest_case_plane_upper_rational':str(plane_upper),
            'a_coordinate_enclosure':q['a'],'physical_a_box_rational':encoded(abox),
            'normalized_a_box_rational':encoded(normalized),
            'maximum_normalized_radius_squared':str(maximum_norm_squared),
            'covered_area_rational':str(sum(map(area,pieces))),
            'enclosure_area_rational':str(area(abox)),
            'intersecting_original_cells':[{
                **{k:cell[k] for k in ('index','domain','node','neighbor','address','depth','original_node_canonical_sha256')},
                'normalized_box':encoded(cell['box']),'physical_box':encoded(cell['physical']),
                'intersection':encoded(intersect(abox,cell['physical']))} for cell in selected],
            'families':families,'all_nine_families_pay':all(v['strictly_pays_11over200'] for v in families),
            'all_nine_families_pay_case_plane':all(v['strictly_pays_case_plane'] for v in families)})
    assert len(cases)==4 and all(len(c['families'])==9 for c in cases)
    changed = [name for name,digest in inputs.items() if sha(ROOT/name)!=digest]
    assert not changed
    all_pass = all(c['all_nine_families_pay'] for c in cases)
    all_case_pass = all(c['all_nine_families_pay_case_plane'] for c in cases)
    unresolved = sum(not f['complete_finite_coverage'] for c in cases for f in c['families'])
    result = {'status':'completed saved-only extraction','all_required_reserves_pass':all_pass,
        'all_case_plane_comparisons_pass':all_case_pass,
        'required_bare_reserve_rational':str(REQUIRED),'unresolved_family_cases':unresolved,
        'insufficient_reserve_family_cases':sum(f['complete_finite_coverage'] and not f['strictly_pays_11over200'] for c in cases for f in c['families']),
        'insufficient_case_plane_family_cases':sum(f['complete_finite_coverage'] and not f['strictly_pays_case_plane'] for c in cases for f in c['families']),
        'source_path':SOURCE,'source_sha256':inputs[SOURCE],
        'proof_sha256':inputs[PROOF],'checker_sha256':inputs[own],
        'input_sha256':inputs,'changed_inputs':changed,'original_partition':partition,
        'source_summary_counts':source_summary_counts,'canonical_cases':cases,
        'canonical_reference_cases_checked':4,'required_family_cases_checked':36,
        'analytic_evaluations':0,'root_or_source_replays':0,'new_parameter_cells':0,
        'finite_word_realization_claimed':False,'uniform_reference_domain_claimed':False,
        'whole_finite_source_claimed':False,
        'scope':'Saved bare face reserves only; any joined conclusion retains the original plane guards and common height.'}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    with args.output.open('x') as stream:
        stream.write(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':result['status'],'all_required_reserves_pass':all_pass,
        'all_case_plane_comparisons_pass':all_case_pass,
        'unresolved_family_cases':unresolved,'insufficient_reserve_family_cases':result['insufficient_reserve_family_cases'],
        'record_sha256':sha(args.output)}))


if __name__ == '__main__':
    main()
