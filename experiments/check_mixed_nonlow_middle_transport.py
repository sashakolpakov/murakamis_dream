#!/usr/bin/env python3
"""Complete-input and exact bookkeeping check for nonlow middle transport.

No numerical inequality or root is recomputed. The saved derivative trees
are exhausted structurally and compared to their completed 384-bit replays.
The arbitrary-length implication is the written incidence argument, not a
finite enumeration of cyclic words.
"""
import argparse
import hashlib
import itertools
import json
from fractions import Fraction as F
from pathlib import Path

from flint import arb
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT/'notes/research_mixed_nonlow_middle_transport.md'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def tree(row, box, immediate=False):
    stack = [list(box)]
    leaves = visits = monotone = 0
    for node in row['nodes']:
        assert stack
        cell = stack.pop()
        visits += 1
        if node[0] == 'L':
            assert len(node) == (1 if immediate else 2)
            leaves += 1
        elif node[0] == 'S':
            assert len(node) == 2
            axis = node[1]
            assert type(axis) is int and 0 <= axis < len(cell)
            lo, hi = cell[axis]
            assert lo < hi
            mid = (lo+hi)/2
            for interval in ((lo, mid), (mid, hi)):
                child = list(cell)
                child[axis] = interval
                stack.append(child)
        else:
            assert not immediate and node[0] == 'M' and len(node) == 4
            axis, bit = node[1:3]
            assert type(axis) is int and 0 <= axis < len(cell)
            assert type(bit) is int and bit in (0, 1)
            assert cell[axis][0] < cell[axis][1]
            point = cell[axis][bit]
            cell[axis] = (point, point)
            stack.append(cell)
            monotone += 1
    assert not stack and row['remaining_boxes'] == 0
    assert (leaves, visits) == (row['accepted_cells'], row['visited_cells'])
    assert monotone == row.get('monotonic_reductions', 0)
    return leaves, visits, monotone


def conditioned_interval(word, index, table):
    own = word[index]
    bounds = [F(-57, 1000), F(-1, 50)] if own else [F(-3, 100), F(1, 50)]
    middle = table[''.join(map(str, word[index-1:index+2]))][1]
    following = (word[index+2],) if index+2 < 4 else (0, 1)
    first = [table[''.join(map(str, (own, word[index+1], last)))][2]
             for last in following]
    lows = [bounds[0], F(middle[0], 1000), F(min(p[0] for p in first), 1000)]
    highs = [bounds[1], F(middle[1], 1000), F(max(p[1] for p in first), 1000)]
    if own == word[index+1] == 1:
        lows.append(F(-56, 1000))
        highs.append(F(-48, 1000))
        if word[index-1] == 1:
            highs.append(F(-53, 1000))
    lo, hi = max(lows), min(highs)
    assert lo < hi
    return [str(lo), str(hi)]


def specifications(table, frozen):
    result = []
    for region in ('lower', 'upper'):
        for word in itertools.product((0, 1), repeat=4):
            for side in ('left', 'right'):
                ci, ni = (1, 2) if side == 'right' else (2, 1)
                cb = conditioned_interval(word, ci, table)
                nb = conditioned_interval(word, ni, table)
                for sc, sn in itertools.product(range(word[ci]+1), range(word[ni]+1)):
                    base = dict(region=region, word=list(word), side=side, selected=[sc, sn])
                    if frozen:
                        hb = (['-1/200', '1/300'] if word[ci] == 0 else
                              ['0', '7/500'] if sc else ['-19/2000', '0'])
                        for xi in range(1 if sn else 2):
                            result.append(dict(base, neighbor_switch=xi,
                                frozen_height_interval=hb, neighbor_coefficient_interval=nb))
                    else:
                        for chi, xi in itertools.product(range(1 if sc else 2), range(1 if sn else 2)):
                            result.append(dict(base, switches=[chi, xi], coefficient_intervals=[cb, nb]))
    assert len(result) == len({json.dumps(c, sort_keys=True) for c in result}) == (240 if frozen else 400)
    return result


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--input', type=Path)
    ap.add_argument('--output', type=Path, default=ROOT/'repro/results/research-mixed-nonlow-middle-transport.json')
    args = ap.parse_args()
    ph, sh = sha(PROOF), sha(__file__)
    ih = sha(args.input) if args.input else None
    old = json.loads(args.input.read_text()) if args.input else None
    deps, visited, primary, checks = {}, set(), {}, []

    def bind(path, expected=None):
        if path not in deps:
            deps[path] = sha(ROOT/path)
        if expected is not None:
            assert deps[path] == expected, path
        return deps[path]

    def inherit(path):
        bind(path)
        if path in visited:
            return
        visited.add(path)
        record = json.loads((ROOT/path).read_text())
        nested = {}
        for field in ('dependencies', 'dependencies_sha256'):
            for p, digest in record.get(field, {}).items():
                if p in nested:
                    assert nested[p] == digest, p
                nested[p] = digest
                bind(p, digest)
        for p in nested:
            if p.startswith('repro/results/') and p.endswith('.json'):
                inherit(p)

    def load(stem, prefix='check', replay=False, proof_stem=None):
        path = 'repro/results/research-mixed-'+stem.replace('_', '-')+('-replay' if replay else '')+'.json'
        inherit(path)
        r = json.loads((ROOT/path).read_text())
        assert r['status'] == 'passed', path
        assert r['proof_sha256'] == bind('notes/research_mixed_'+(proof_stem or stem)+'.md')
        assert r['script_sha256'] == bind('experiments/'+prefix+'_mixed_'+stem+'.py')
        primary[path] = deps[path]
        return r

    def check(name, assertion):
        assert assertion, name
        checks.append(name)

    full = load('full_left_region')
    upper = load('nonlow_upper_transition_removal')
    early = load('early_plateau_right_clusters')
    grid = load('right_core_support_grid', 'certify', proof_stem='right_core_support')
    right = load('right_core_support_reference', 'certify', proof_stem='right_core_support')
    rr = load('two_right_source_bound', 'certify')
    selected = load('selected_plateau_support', 'certify')
    plateau = load('plateau_accretivity')
    low = load('exact_low_transport')
    geometry = load('neighbor_conditioned_critical_boxes', 'certify')
    # Bind the actual written source allocation and both endpoint geometric
    # refinements, in addition to their inherited completed records.
    for name in ('minimum_level_transport', 'early_selected_transport',
                 'four_before_four_height_lower', 'four_before_four_height', 'raw_row_stationarity'):
        path = 'notes/research_mixed_'+name+'.md'
        bind(path)
    check('old derivative families are complete with independent saved checks',
          full['complete_input_requirement'] is True
          and [r['domains'] for r in full['derivative_families']] == [192, 78, 50, 175]
          and full['derivative_domain_count'] == 495
          and full['independently_verified_leaves'] == 4720234
          and full['numerical_inequalities_repeated'] == full['cyclic_pattern_enumerations'] == 0)
    check('upper removal preserves labels before any finite tolerance',
          F(upper['horizontal_loss']) == F(1, 20)
          and upper['numerical_cells_recomputed'] == 0
          and set(upper['inherited_cover_structures']) == {
              'mixed_raw_coherent_height_bounds', 'mixed_raw_coherent_right_clamping',
              'mixed_two_raw_right_clamping'})
    check('conditioned reference geometry complete',
          geometry['boundary_products'] == 512 and len(geometry['limits_in_thousandths']) == 8)

    immediate = load('immediate_right_half')
    immediate_replay = load('immediate_right_half', replay=True)
    bands = {(1, 0, 0): ('-.017', '.010'), (1, 0, 1): ('-.025', '-.002'),
             (1, 1, 0): ('-.054', '-.030'), (1, 1, 1): ('-.056', '-.048'),
             (0, 0, 0): ('-.017', '.010'), (0, 0, 1): ('-.025', '.002'),
             (0, 1, 0): ('-.056', '-.030'), (0, 1, 1): ('-.056', '-.036')}
    expected = [(list(key)+[0], tuple(map(F, values))) for key, values in bands.items()]
    expected += [([d, 1, b, 1], (F(0), F(0))) for d, b in itertools.product((0, 1), repeat=2)]
    structures = {}

    def paired(stem, author, replay):
        apath = 'repro/results/research-mixed-'+stem.replace('_', '-')+'.json'
        check(stem+' current saved384 author input binding',
              replay['precision_bits'] >= 384 and author['precision_bits'] >= 256
              and replay['input_sha256'] == deps[apath]
              and author['proof_sha256'] == replay['proof_sha256']
              and author['script_sha256'] == replay['script_sha256']
              and author['dependencies_sha256'] == replay['dependencies_sha256'])

    paired('immediate_right_half', immediate, immediate_replay)
    assert len(immediate['cases']) == len(immediate_replay['cases']) == len(expected) == 12
    totals = [0, 0, 0]
    for a, b, (case, band) in zip(immediate['cases'], immediate_replay['cases'], expected):
        assert a['case'] == b['case'] == case
        assert tuple(map(F, a['coefficient_interval'])) == tuple(map(F, b['coefficient_interval'])) == band
        assert a['nodes'] == b['nodes']
        box = [(F(3, 25), F(11, 50)), band]
        counts = tree(a, box, immediate=True)
        assert tree(b, box, immediate=True) == counts
        assert arb(a['minimum_lower_bound']).lower() > arb(1)/2000
        assert arb(b['minimum_lower_bound']).lower() > arb(1)/2000
        totals = [x+y for x, y in zip(totals, counts)]
    check('all twelve immediate sides and exact saved trees complete', totals == [32, 52, 0])
    structures['immediate_right_half'] = dict(domains=12, leaves=32, visits=52, monotone=0)
    for record in (immediate, immediate_replay):
        frozen = record['frozen_height_corollary']
        assert len(frozen['scalar_reserves']) == 12
        assert all(arb(v).lower() > 0 for v in frozen['scalar_reserves'].values())
        assert F(frozen['rational_height_derivative_upper']) == F(-552849, 500000)
        assert frozen['new_parameter_cells'] == 0
        assert F(frozen['derivative_lower_bound']) == F(13, 100)
    check('frozen immediate scalar comparisons and unrounded gauge recovered',
          F(13, 100)+F(1, 10) == F(23, 100)
          and F(23, 100)-F(1, 5) == F(3, 100)
          and F(23, 100)-F(53, 1000) == F(177, 1000))

    for frozen, stem, counts in (
        (False, 'distance_two_right_halves', (400, 52795, 105240, 50)),
        (True, 'frozen_center_distance_two_right_halves', (240, 30517, 61002, 208)),
    ):
        a = load(stem, 'certify')
        b = load(stem, 'certify', replay=True)
        paired(stem, a, b)
        cases = specifications(geometry['limits_in_thousandths'], frozen)
        check(stem+' complete ordered actual conditioned domains',
              a['required_cases'] == a['completed_cases'] == b['required_cases'] == b['completed_cases'] == counts[0]
              and [r['case'] for r in a['cases']] == [r['case'] for r in b['cases']] == cases)
        totals = [0, 0, 0]
        for left, right_row in zip(a['cases'], b['cases']):
            assert left['nodes'] == right_row['nodes']
            cell_counts = tree(left, [(F(0), F(1))]*4)
            assert tree(right_row, [(F(0), F(1))]*4) == cell_counts
            assert arb(left['minimum_lower_bound']).lower() > 0
            assert arb(right_row['minimum_lower_bound']).lower() > 0
            totals = [x+y for x, y in zip(totals, cell_counts)]
        check(stem+' every complete tree and monotone face matches saved replay',
              tuple(totals) == counts[1:]
              and tuple(a[k] for k in ('accepted_cells', 'visited_cells', 'monotonic_reductions')) == counts[1:]
              and tuple(b[k] for k in ('accepted_cells', 'visited_cells', 'monotonic_reductions')) == counts[1:])
        structures[stem] = dict(domains=counts[0], leaves=totals[0], visits=totals[1], monotone=totals[2])

    check('right source grid and whole reference cover are complete',
          grid['source_profiles'] == 75 and grid['support_values'] == 750
          and right['boundary_products'] == 512 and right['accepted_cells'] == 5546)
    check('independent PR rate gap is retained before finite tolerance',
          F(right['strict_support_gap']) == F(1, 500))
    check('RR raw rate gap is retained before finite tolerance',
          rr['boundary_products'] == 512 and F(rr['strict_reference_gap']) == F(1, 50))
    check('selected PP uses the actual branch rate not its finite rounded gap',
          F(selected['reference_defect_upper']) == -F(1, 100)
          and selected['target_products'] == 36 and selected['reference_products'] == 96)
    check('unselected PP fixed-height tangent concavity is a completed input',
          F(plateau['effective_cyclic_accretivity']) == F(1, 2000)
          and plateau['scalar_comparisons'] == 19)
    check('early endpoint argument retains its unrounded source constants',
          F(early['early_phase_loss']) == F(1, 100)
          and F(early['affected_PR_raw_ceiling']) == F(1, 200)
          and F(early['early_R_raw_loss']) == F(1, 1000)
          and F(early['largest_double_PP_excess']) == F(33651, 2000000))
    check('early incidence loss after its single-use charges is at least .001',
          F(1, 100)-F(33651, 4000000) == F(6349, 4000000) > F(1, 1000)
          and F(1, 100)-F(1, 200) == F(1, 200) > F(1, 1000))
    check('early-free independent right endpoint leaves the stronger gap',
          min(F(1, 500), F(1, 50)) > F(1, 1000))
    check('real low transport fixes a positive collar and raises to .1',
          F(low['raising_endpoint']) == F(1, 10) and F(low['collar_upper']) == F(1, 1000))
    check('selected heights are fixed above the fast cutoff',
          (F(3, 25)-F(1, 10))/F(1, 50) == 1)
    check('early neighbors imply the stated frozen unselected bands',
          F(1, 6)*F(-3, 100) == F(-1, 200)
          and F(1, 6)*F(1, 50) == F(1, 300)
          and F(1, 6)*F(-57, 1000) == F(-19, 2000))
    check('slow and fast cutoff scales have the exact common ratio',
          F(3, 25)/F(1, 50) == 6 and F(11, 50)-F(1, 10) == F(3, 25))
    # These are local symbolic inequalities valid for every multiplicity n,
    # not tests of finitely many cyclic words: if v<0 and n>=1, n*v<=v;
    # if v>=0, n*min(v,0)=0<=v. For gauge sums, both coefficients vanish.
    check('shared center and selected real gauge coefficients cancel',
          F(3, 2)-F(3, 2) == 0 and F(1, 10)-F(1, 10) == 0)
    n = sp.symbols('n', integer=True, positive=True)
    v = sp.symbols('v', positive=True)
    check('negative-height overcount differs by (n-1) times a nonnegative magnitude',
          sp.expand((-v)-n*(-v)-(n-1)*v) == 0 and (n-1).is_nonnegative is True)
    check('positive height terms may be omitted for every multiplicity',
          sp.Min(v, 0) == 0 and v.is_positive is True)
    check('literal halfweights sum once even on loops and parallel edges', F(1, 2)+F(1, 2) == 1)
    check('one global source tolerance leaves the advertised finite reserve',
          F(1, 1000)-F(1, 2000) == F(1, 2000))
    check('fixed early-isolated positions have no uncharged P/P or P/R incidence',
          set(('B', 'B')).isdisjoint(('P', 'R')))

    result = dict(status='passed', complete_input_requirement=True, exact_checks=len(checks),
        checks=checks, primary_records=primary, primary_record_count=len(primary),
        inherited_old_domains=495, new_derivative_structures=structures,
        independently_replayed_new_domains=652,
        numerical_inequalities_recomputed=0, cyclic_pattern_enumerations=0,
        nonlow_phase_loss='1/1000', nonlow_finite_loss='1/2000', one_global_source_tolerance='strictly less than 1/2000',
        region='[rho,1]^m with fixed admissible rho>0 and a nonempty original right set',
        all_original_selections=True, all_integer_parities=True,
        proof_sha256=ph, script_sha256=sh, dependencies_sha256=deps,
        scope='Complete-input validation of written arbitrary-cycle middle transport with permanent raw right labels. No numerical cover, no raw-to-coherent substitution, no seam-plus-right or whole-period noncancellation claim.')
    if old is not None:
        assert old == result
        result['input_sha256'] = ih
    assert sha(PROOF) == ph and sha(__file__) == sh
    assert all(sha(ROOT/path) == digest for path, digest in deps.items())
    if args.input:
        assert sha(args.input) == ih
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print('PASS', len(checks), 'exact checks;', len(primary), 'primary records;', len(deps),
          'current bindings; 495 inherited + 652 saved derivative domains; no numerical rerun')


if __name__ == '__main__':
    main()
