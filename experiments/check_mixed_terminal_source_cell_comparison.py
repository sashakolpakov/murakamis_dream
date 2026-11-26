#!/usr/bin/env python3
"""Recombine saved cell totals only; no gain, primitive or source callbacks."""
import argparse
from fractions import Fraction as F
import gzip
import hashlib
from itertools import combinations, product
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
CELL = 'repro/results/research-mixed-terminal-source-cell-joined-plane.json.gz'
OLD = 'repro/results/research-mixed-terminal-uniform-real-face-comparison.json'
PRIVATE = 'repro/results/research-mixed-terminal-private-left-symmetric-transfer.json'
FACES = 'repro/results/research-mixed-terminal-uniform-face-reserves.json'
PLANE = 'repro/results/research-mixed-terminal-uniform-joined-plane.json'
ALIAS = 'repro/results/research-mixed-terminal-uniform-alias-comparison.json'
CONSTANT = 'repro/results/research-mixed-terminal-uniform-constant-profile.json'
PINNED = {
    CELL: '53fd53494b658f5faa76ab9fb185b9e5c492d61eb8942944d9bd8e48b2fbfbbb',
    OLD: 'ad14e484df33c18560cfa82ae717d93364f25935e71518cead2d09fce4ca833a',
    PRIVATE: 'a6a0c31f8132d7acf5e6037b293564c62dcebb7532e66d553d372d3667f5b3f4',
    FACES: '37fc3676a9919525e16b214db0fedebd3e13b980150f5f01ec0d0b28141a07d3',
    PLANE: '4bfa03e1c61a4e34d9b6d549b5e9d666b15df606078d02258dae340055e3ee88',
    ALIAS: '2bb8973f00571490a8ecb3d219f104ecc7be2ec025918363d95cec830653e4e2',
    CONSTANT: '5931137b18d3b6d1815ed2cf90569425910882f88e637e35391f575fcab12965',
    'notes/research_mixed_terminal_uniform_main_comparison.md':
        '8658da027d6b5c5692a2da7032c657007b163617d2904b3f06b3e3c21d3b92bb',
    'experiments/check_mixed_terminal_source_cell_joined_plane.py':
        'dd4bbdc4411a6bc1a3d5a924e101c7cebf4ee2c697e57d4fd26932251884f586',
    'notes/research_mixed_terminal_source_cell_joined_plane.md':
        '0d5d3d1c38e0423f2ea130fba5fce0a4c08379abcc69edb1d69cebde692d4c8d',
}
H = F(1, 100)
BALL = re.compile(r'\[\s*([^\s]+)\s*\+/-\s*([^\s]+)\s*\]')


def sha(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()


def canonical(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def load(name):
    with (gzip.open(ROOT / name, 'rt') if name.endswith('.gz') else (ROOT / name).open()) as f:
        return json.load(f)


def iv(x):
    a, b = F(x['lower_rational']), F(x['upper_rational'])
    assert a <= b
    return a, b


def mul(x, y):
    v = [a * b for a in x for b in y]
    return min(v), max(v)


def box(x):
    ans = tuple(tuple(map(F, v)) for v in x)
    assert len(ans) == 2 and all(len(v) == 2 and v[0] <= v[1] for v in ans)
    return ans


def area(x):
    return (x[0][1]-x[0][0])*(x[1][1]-x[1][0])


def intersection(x, y):
    out = tuple((max(a[0], b[0]), min(a[1], b[1])) for a, b in zip(x, y))
    return None if any(a > b for a, b in out) else out


def upward_decimal(q, digits=12):
    n = -((-q.numerator * 10**digits) // q.denominator)
    sign = '-' if n < 0 else ''
    a, b = divmod(abs(n), 10**digits)
    return f'{sign}{a}.{b:0{digits}d}'


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output', type=Path, required=True)
    args = ap.parse_args()
    assert not args.output.exists()
    if hasattr(sys, 'set_int_max_str_digits'):
        sys.set_int_max_str_digits(0)
    inputs = dict(PINNED)
    own = Path(__file__).resolve().relative_to(ROOT).as_posix()
    inputs[own] = sha(ROOT / own)
    for name, digest in inputs.items():
        assert sha(ROOT / name) == digest, name
    cell, old, private, faces, plane, alias, constant = [load(p) for p in (CELL, OLD, PRIVATE, FACES, PLANE, ALIAS, CONSTANT)]
    for data in (cell, old, private, faces, plane, alias, constant):
        assert data['changed_inputs'] == []
        for name, digest in data['input_sha256'].items():
            assert name not in inputs or inputs[name] == digest, name
            inputs[name] = digest
    for name, digest in inputs.items():
        assert sha(ROOT / name) == digest, name
    assert cell['status'] == 'completed fixed saved-only protocol'
    assert cell['uniform_cellwise_plane_ceilings_proved'] and not cell['pending_cells']
    assert not cell['whole_finite_kernel_proved'] and not cell['private_left_independent_theorem_applied']
    assert len(cell['input_sha256']) == 529
    assert private['status'] == 'passed'
    private_gap = F(private['scoped_raw_face_gap_rational'])
    assert private_gap == F(51, 20000)
    assert private['domain']['beta'] == private['domain']['epsilon'] == 1
    assert F(private['domain']['transfer_selected_height_rational']) == H
    assert old['branches_paid_including_private_left'] == 29 and old['unresolved_branches'] == 7
    assert alias['all_joined_endpoint_gaps_exceed_1_over_20']
    assert F(alias['common_gap_lower_rational']) > F(1,20)
    assert constant['uniform_constant_profile_gap_proved']
    assert F(constant['common_raw_gap_rational']) == F(1,100)
    assert F(constant['common_exact_deficit_lower_rational']) > F(1,100)
    assert F(old['separate_main_gap_rational']) == F(1,400)
    count = dict(cells=0, quadratics=0, vertices=0, saved_gain_upper_associations=0,
                 same_cell_jobs=0, same_cell_branch_sums=0, family_branch_maxima=0)
    rows, cell_inventory = [], []
    assert [(c['beta'], c['epsilon']) for c in cell['cases']] == [(1, 0), (1, 1)]
    for case in cell['cases']:
        eps = case['epsilon']
        face = next(c for c in faces['cases'] if (c['beta'], c['epsilon']) == (1, eps))
        pl = next(c for c in plane['cases'] if (c['beta'], c['epsilon']) == (1, eps))
        assert canonical(face) == case['face_case_canonical_sha256']
        assert canonical(pl) == case['plane_case_canonical_sha256']
        original_cells = face['intersecting_original_cells']
        assert [c['original_cell'] for c in case['cells']] == original_cells
        assert len(original_cells) == (45 if eps == 0 else 25)
        image = box(face['physical_a_box_rational'])
        pieces = []
        jobs = {}
        for fam in face['families']:
            series, family = fam['series'], fam['family']
            multiplier = {'three_mixed': 8, 'three_half': 1, 'four': 21}[series]
            assert len(fam['contributing_jobs']) == len(original_cells)
            assert {j['original_cell_index'] for j in fam['contributing_jobs']} == {c['index'] for c in original_cells}
            uppers = []
            for job in fam['contributing_jobs']:
                assert job['job'] == multiplier*job['original_cell_index']+family
                match = BALL.fullmatch(job['saved_maximum_upper'])
                assert match and F(match[2]) >= 0
                assert F(job['decoded_upper_rational']) == F(match[1])+F(match[2])
                jobs[job['original_cell_index'], series, family] = dict(series=series, family=family, **job)
                uppers.append(F(job['decoded_upper_rational']))
            assert not fam['null_jobs_unresolved'] and fam['complete_finite_coverage']
            assert max(uppers) == F(fam['uniform_bare_upper_rational'])
        shared = case['shared_data']
        pi, ia, iss, vp = (iv(shared[k]) for k in ('pi', 'Ia', 'Is', 'normalized_VP'))
        lam = tuple(map(F, shared['lambda_exact']))
        a0 = tuple(map(F, shared['center_exact'][3]))
        p0 = F(shared['p0_rational'])
        rho = F(shared['rho_star_rational'])
        assert rho == min(F(shared['rho4_rational']), F(shared['rho5_rational']))
        local_sums = {}
        planes = []
        for c in case['cells']:
            orig = c['original_cell']; idx = orig['index']
            assert c['original_cell_canonical_sha256'] == canonical(orig)
            assert c['status'] == 'enclosed both joined-plane alternatives'
            assert orig['neighbor'] == 1 and orig['domain'] == 1+2*eps
            norm = [(-F(1), F(1)), (-F(1), F(1))]
            assert orig['depth'] == len(orig['address'])
            for depth, bit in enumerate(orig['address']):
                assert bit in '01'
                ax = depth % 2; lo, hi = norm[ax]; mid = (lo+hi)/2
                norm[ax] = (lo, mid) if bit == '0' else (mid, hi)
            assert tuple(norm) == box(orig['normalized_box'])
            physical = tuple(tuple(center+F(8,125)*x for x in pair)
                             for center, pair in zip((F(3,10), -F(13,250)), norm))
            assert physical == box(orig['physical_box'])
            piece = intersection(image, physical)
            assert piece is not None and piece == box(orig['intersection'])
            pieces.append(piece)
            A, height = piece
            assert iv(c['reference_A_interval']) == A and iv(c['reference_c_interval']) == height
            delta = (H-height[1], H-height[0]); assert iv(c['delta']) == delta and delta[0] > 0
            maxima = []
            for endpoint, q in zip(A, c['quadratic_endpoint_polynomials']):
                bA = p0-lam[0]*a0[1]+lam[1]*(endpoint-a0[0])
                coeff = (H*bA, H*lam[0]-bA, -lam[0])
                assert F(q['A_endpoint_rational']) == endpoint and iv(q['c_interval']) == height
                assert list(map(F, q['coefficients_ascending_rational'])) == list(coeff)
                def poly(x): return coeff[0]+coeff[1]*x+coeff[2]*x*x
                candidates = [min(height[1], max(height[0], coeff[1]/(2*lam[0])))] if lam[0] > 0 else list(height)
                assert list(map(F, q['candidate_points_rational'])) == candidates
                assert list(map(F, q['candidate_values_rational'])) == [poly(x) for x in candidates]
                maximum = max(map(poly, candidates)); assert F(q['maximum_rational']) == maximum
                maxima.append(maximum); count['quadratics'] += 1
            assert len(maxima) == 2
            up = max(maxima)+delta[1]*rho
            assert F(c['quadratic_maximum_rational']) == max(maxima)
            assert F(c['marginal_error_upper_rational']) == delta[1]*rho
            assert F(c['UP_upper_rational']) == up
            pv = c['plane_values']; kappa = mul(pi, delta)
            wp = mul(mul(pi, (delta[0]**2, delta[1]**2)), vp)
            assert iv(pv['kappa']) == kappa and iv(pv['WP']) == wp
            trials = {1:up+wp[1]-pi[0]*H, 0:up+wp[1]+F(pv['GH_cell_upper_rational'])/2}
            branch_max = {}
            assert [b['nu'] for b in c['branches']] == [1, 0]
            for branch in c['branches']:
                nu = branch['nu']; bounds = [kappa, ia, iss]+([] if nu else [iv(pv['Q'])])
                assert F(branch['trial_upper_rational']) == trials[nu]
                assert [v['endpoint_bits'] for v in branch['vertices']] == [list(b) for b in product((0,1), repeat=len(bounds))]
                values = []
                for v in branch['vertices']:
                    parameters = [b[bit] for b, bit in zip(bounds, v['endpoint_bits'])]
                    assert list(map(F, v['parameters_rational'])) == parameters
                    k, ca, cs = parameters[:3]
                    forces = [k*(1-cs), k*(F(3,2)*ca-cs-F(1,2))+(parameters[3]/2 if not nu else 0)]
                    assert list(map(F, v['forces_rational'])) == forces
                    gains = []
                    for name, force, target, K in zip(('s','a'), forces,
                            ((F(11,50), F(1,2)), (F(11,50), F(9,20))), (F(88,5), F((1+nu)*49,10))):
                        g = v['gains'][name]
                        assert iv(g['force']) == (force, force) and iv(g['target']) == target
                        assert F(g['K_rational']) == K
                        cent = tuple(map(F, c['s_real_intersection_endpoints_rational'])) if name == 's' else A
                        assert iv(g['center']) == cent
                        upper = F(g['upper_rational'])
                        assert upper == max([F(0)]+[iv(b['value'])[1] for b in g['branches']])
                        assert F(v['independent_gain_checks'][name]['upper_rational']) == upper
                        gains.append(upper); count['saved_gain_upper_associations'] += 1
                    assert F(v['gain_sum_upper_rational']) == sum(gains)
                    total = trials[nu]+sum(gains)
                    assert F(v['plane_upper_rational']) == total
                    values.append(total); count['vertices'] += 1
                maximum = max(values); branch_max[nu] = maximum
                assert F(branch['cell_plane_upper_rational']) == maximum
                assert branch['attaining_vertices'] == [v['endpoint_bits'] for v, x in zip(branch['vertices'], values) if x == maximum]
                planes.append((idx, nu, maximum))
            assert len(c['source_jobs']) == 9
            for job in c['source_jobs']:
                assert job == jobs[idx, job['series'], job['family']]
                count['same_cell_jobs'] += 1
            assert len(c['family_comparisons']) == 18
            seen = set()
            for x in c['family_comparisons']:
                key = (x['series'], x['family'], x['nu']); assert key not in seen; seen.add(key)
                job = jobs[idx, x['series'], x['family']]
                assert x['status'] == 'enclosed' and x['job'] == job['job']
                assert F(x['plane_upper_rational']) == branch_max[x['nu']]
                assert x['source_upper_rational'] == job['decoded_upper_rational']
                joined = branch_max[x['nu']]+F(job['decoded_upper_rational'])
                assert F(x['joined_upper_rational']) == joined and F(x['gap_rational']) == -joined
                assert x['strictly_negative'] == (joined < 0)
                local_sums.setdefault(key, []).append((idx, job['job'], joined))
                count['same_cell_branch_sums'] += 1
            cell_inventory.append(dict(epsilon=eps, original_cell_index=idx, original_cell_sha256=canonical(orig),
                plane_uppers_rational={str(k):str(v) for k,v in branch_max.items()}))
            count['cells'] += 1
        assert all((p := intersection(a,b)) is None or area(p) == 0 for a,b in combinations(pieces,2))
        assert sum(map(area,pieces)) == area(image) > 0
        assert F(case['coverage']['covered_area_rational']) == area(image)
        assert max(p[2] for p in planes) == F(case['uniform_plane_upper_rational'])
        assert case['attaining_plane_cells'] == [dict(original_cell_index=i,nu=nu) for i,nu,v in planes if v == max(p[2] for p in planes)]
        all_joined = [v for values in local_sums.values() for _,_,v in values]
        assert max(all_joined) == F(case['observed_joined_maximum_rational']) == F(case['uniform_all_family_upper_rational'])
        assert case['all_family_comparisons_complete']
        for family in case['families']:
            of = next(r for r in old['cases'] if (r['epsilon'],r['series'],r['family']) == (eps,family['series'],family['family']))
            assert of['face_case_sha256'] == canonical(face) and of['plane_case_sha256'] == canonical(pl)
            assert family['both_branches_complete']
            assert F(family['uniform_both_branch_upper_rational']) == max(F(b['uniform_joined_upper_rational']) for b in family['branches'])
            assert family['both_branches_strictly_negative'] == all(F(b['uniform_joined_upper_rational']) < 0 for b in family['branches'])
            for b in family['branches']:
                nu = b['nu']; key = (family['series'],family['family'],nu)
                candidates = local_sums[key]
                assert len(candidates) == len(original_cells)
                new_upper = max(v for _,_,v in candidates)
                assert b['complete'] and not b['unresolved_original_cell_indices'] and not b['no_canonical_references']
                assert F(b['observed_maximum_rational']) == F(b['uniform_joined_upper_rational']) == new_upper
                assert b['strictly_negative'] == (new_upper < 0)
                attaining = [dict(original_cell_index=i, job=j) for i,j,v in candidates if v == new_upper]
                assert b['attaining'] == attaining
                old_upper = F(of['joined_plane_uppers_rational'][str(nu)])
                assert old_upper == F(of['plane_uppers_rational'][str(nu)])+F(of['raw_bare_upper_rational'])
                assert F(of['raw_bare_upper_rational']) == F(next(f for f in face['families'] if (f['series'],f['family']) == key[:2])['uniform_bare_upper_rational'])
                best = min(old_upper,new_upper)
                direct = eps == 1 and of['profile_index'] == 2
                effective = min(best,-private_gap) if direct else best
                rows.append(dict(epsilon=eps, profile_index=of['profile_index'], label=of['label'],
                    series=key[0], family=key[1], nu=nu,
                    old_global_upper_rational=str(old_upper), new_same_cell_upper_rational=str(new_upper),
                    best_plane_upper_rational=str(best), direct_private_left_upper_rational=str(-private_gap) if direct else None,
                    proved_upper_rational=str(effective), proved_upper_decimal_ceiling=upward_decimal(effective),
                    strictly_negative=effective<0, paid_gap_exceeds_1_over_400=effective<-F(1,400),
                    attaining_new_cells=attaining, source_family_canonical_sha256=of['face_family_sha256']))
                count['family_branch_maxima'] += 1
    assert count == dict(cells=70, quadratics=140, vertices=1680, saved_gain_upper_associations=3360,
                         same_cell_jobs=630, same_cell_branch_sums=1260, family_branch_maxima=36)
    unresolved = [r for r in rows if not r['strictly_negative']]
    assert {(r['epsilon'],r['profile_index'],r['nu']) for r in unresolved} == {(0,1,1),(0,8,1),(1,0,0),(1,0,1),(1,8,1)}
    paid = [r for r in rows if r['strictly_negative']]
    assert len(paid) == 31 and all(r['paid_gap_exceeds_1_over_400'] for r in paid)
    smallest = min(-F(r['proved_upper_rational']) for r in paid)
    assert smallest == private_gap
    changed = [name for name,digest in inputs.items() if sha(ROOT/name) != digest]
    assert not changed
    out = dict(status='passed exact saved comparison', input_sha256=inputs, changed_inputs=changed,
        source_record_sha256=PINNED[CELL], old_comparison_sha256=PINNED[OLD], private_left_sha256=PINNED[PRIVATE],
        counts=count, original_cell_inventory=cell_inventory, comparisons=rows,
        paid_real_entropy_branches=31, unresolved_real_entropy_branches=5,
        unresolved=[{k:r[k] for k in ('epsilon','profile_index','label','nu','old_global_upper_rational','new_same_cell_upper_rational','best_plane_upper_rational')} for r in unresolved],
        smallest_paid_real_entropy_gap_rational=str(smallest), separate_main_gap_rational='1/400',
        separate_alias_gap_rational='1/20', separate_constant_gap_rational='1/100',
        all_previously_paid_profiles_common_raw_floor_rational='1/400',
        conditional_remaining_gap_name='gamma5', conditional_complete_raw_gap='min(gamma5,1/400)',
        conditional_complete_finite_gap='min(gamma5,1/400)/2',
        new_gain_evaluations=0, analytic_callbacks=0, roots=0, source_replays=0, subdivisions=0,
        complete_terminal_kernel_proved=False, full_source_proved=False, knot_theorem_proved=False,
        scope='Same original canonical K4 family, H=1/100, independent full targets and both complete-weight alternatives; positive upper bounds are inconclusive.')
    args.output.parent.mkdir(parents=True,exist_ok=True)
    with args.output.open('x') as f:
        json.dump(out,f,indent=2);f.write('\n')
    print(json.dumps(dict(status=out['status'],counts=count,input_bindings=len(inputs),paid=31,remaining=5,
        output_sha256=sha(args.output),smallest_paid_gap=str(smallest))))


if __name__ == '__main__':
    main()
