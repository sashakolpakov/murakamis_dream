#!/usr/bin/env python3
"""Join saved terminal planes to their original 70 source-cell reserves.

Standard-library arithmetic only. No analytic replay, new cell, source root,
target search, alternate input, or retry. Every cell and all nine families
remain in the output, irrespective of the resulting signs.
"""
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import importlib.util
import io
from itertools import combinations, product
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
PROOF = 'notes/research_mixed_terminal_source_cell_joined_plane.md'
PLANE = 'repro/results/research-mixed-terminal-uniform-joined-plane.json'
PLANE_PROOF = 'notes/research_mixed_terminal_uniform_joined_plane.md'
PLANE_CHECKER = 'experiments/check_mixed_terminal_uniform_joined_plane.py'
FACES = 'repro/results/research-mixed-terminal-uniform-face-reserves.json'
FACE_PROOF = 'notes/research_mixed_terminal_uniform_face_reserves.md'
FACE_CHECKER = 'experiments/check_mixed_terminal_uniform_face_reserves.py'
REFINED = 'repro/results/research-mixed-terminal-quadratic-residual-refinement.json'
REFINED_PROOF = 'notes/research_mixed_terminal_quadratic_residual_refinement.md'
REFINED_CHECKER = 'experiments/check_mixed_terminal_quadratic_residual_refinement.py'
SOURCE = 'repro/results/research-mixed-terminal-four-input-integral-budget.json'
AUDIT = 'repro/results/research-mixed-terminal-four-input-integral-budget-saved-audit.json'
GAIN = 'experiments/certify_mixed_terminal_four_input_integral_budget.py'
GAIN_CHECKER = 'experiments/check_mixed_terminal_four_input_integral_budget.py'
PINNED = {
    PROOF: '0d5d3d1c38e0423f2ea130fba5fce0a4c08379abcc69edb1d69cebde692d4c8d',
    PLANE: '4bfa03e1c61a4e34d9b6d549b5e9d666b15df606078d02258dae340055e3ee88',
    PLANE_PROOF: '12ab4cd4e94a521ac97da4e8f71aa68b2352764cd2d283cf123e9f5f113b11e5',
    PLANE_CHECKER: '35fbf2b1a3d2722f1c930cf21704a3121ed0460e621fdfe9420f2b679f39dd16',
    FACES: '37fc3676a9919525e16b214db0fedebd3e13b980150f5f01ec0d0b28141a07d3',
    FACE_PROOF: 'b770a8d3c182c9936367c1f43edd2e74f483ffd5ead2d61fa44b85420109a363',
    FACE_CHECKER: 'b631f8d2b23acab944fc8ab900c2a6dfcacd9da1922643f58919d4185ebb7a6d',
    REFINED: '2834576c2a443c9ffd24032277b5f253d9a85eac17d3f754905812e822a9a331',
    REFINED_PROOF: 'f012610187e14b824fdfeea730bc71ffde1660687ffbdcc491bc945c6a54d596',
    REFINED_CHECKER: '251fc4b3c656201ab5451287577baddb4d4be8122ff34a1318078de0f8501a05',
    SOURCE: '9831e8bdbc884cfc0b0c99dbc7f92245403988ae7dc4bbbba86b5606c5a1575e',
    AUDIT: 'cda9eef92856387d0ec0dccca6311512bb980034a07832ab89a99a7bc733d6c3',
    GAIN: '3b806591d88cd461ab7764a6f9c704a048d9c33edb88834a32dbc59a99c91388',
    GAIN_CHECKER: 'd38f41d186bf31d3255861c45cb0500d1a21a4eb1bfd4d366c6a956efc614bf4',
    'notes/research_mixed_terminal_shared_force_vertices.md':
        '2134390846790b38b6e6451a010d0660e0b7f21fb913739a339173a9771b4a78',
    'notes/research_mixed_terminal_symmetric_pair_costs.md':
        'b4ee1a7bdde317edab0210b20cb8616913984c4f992d1cbed240f6092a8e593f',
    'notes/research_mixed_terminal_canonical_source_domain.md':
        'd50929a1a1c02d034feb5ca5f9ebf6e6da70bd6b0a1eb4a67f67fd1108d18d11',
}
H, R = F(1, 100), F(8, 125)
NAMES = ('e', 'xi', 't', 'a', 's')
BALL = re.compile(r'\[([^\[\]]+) \+/- ([^\[\]]+)\]')


def sha(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(1048576), b''):
            h.update(chunk)
    return h.hexdigest()


def canonical_sha(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True,
        separators=(',', ':')).encode()).hexdigest()


def iv(value):
    if 'finite' in value:
        assert value['finite'] is True
    lo, hi = F(value['lower_rational']), F(value['upper_rational'])
    assert lo <= hi
    return lo, hi


def rec(x): return dict(lower_rational=str(x[0]), upper_rational=str(x[1]))
def cv(x): return iv(x['real']), iv(x['imag'])
def cr(x): return dict(real=rec(x[0]), imag=rec(x[1]))
def ex(x): return F(x), F(x)
def cx(x): return ex(x[0]), ex(x[1])
def add(x, y): return x[0]+y[0], x[1]+y[1]
def neg(x): return -x[1], -x[0]
def sub(x, y): return add(x, neg(y))
def mul(x, y):
    values = [a*b for a in x for b in y]
    return min(values), max(values)
def sc(x, a): return mul(x, ex(a))
def ca(x, y): return add(x[0], y[0]), add(x[1], y[1])
def cm(x, y):
    return sub(mul(x[0], y[0]), mul(x[1], y[1])), add(mul(x[0], y[1]), mul(x[1], y[0]))
def csub(x, y): return sub(x[0], y[0]), sub(x[1], y[1])
def contained(outer, inner): return outer[0] <= inner[0] <= inner[1] <= outer[1]
def box(value):
    result = tuple(tuple(map(F, x)) for x in value)
    assert len(result) == 2 and all(len(x) == 2 and x[0] <= x[1] for x in result)
    return result
def encoded(value): return [[str(lo), str(hi)] for lo, hi in value]
def intersect(x, y):
    result = tuple((max(a[0], b[0]), min(a[1], b[1])) for a, b in zip(x, y))
    return None if any(lo > hi for lo, hi in result) else result
def area(value): return (value[0][1]-value[0][0])*(value[1][1]-value[1][0])
def quotient(x, y):
    denominator = y[0]**2+y[1]**2
    assert denominator > 0
    return ((x[0]*y[0]+x[1]*y[1])/denominator,
            (x[1]*y[0]-x[0]*y[1])/denominator)
def K0(x): return F(49, 10)*(x-x*x)


def address_box(address):
    result = [(-F(1), F(1)), (-F(1), F(1))]
    for depth, bit in enumerate(address):
        assert bit in '01'
        axis = depth % 2
        lo, hi = result[axis]
        middle = (lo+hi)/2
        result[axis] = (lo, middle) if bit == '0' else (middle, hi)
    return tuple(result)


def outward_saved_upper(value):
    # Exactly the inherited Arb-ball display convention; bare decimals fail.
    match = BALL.fullmatch(value)
    assert match is not None, ('not an outward saved ball', value)
    middle, radius = map(F, match.groups())
    assert radius >= 0
    return middle+radius


def cell_quadratic(A, c, a0, lam, p0):
    bA = p0-lam[0]*a0[1]+lam[1]*(A-a0[0])
    coefficients = (H*bA, H*lam[0]-bA, -lam[0])
    def value(x): return coefficients[0]+coefficients[1]*x+coefficients[2]*x*x
    witness = dict(A_endpoint_rational=str(A), c_interval=rec(c), b_A_rational=str(bA),
        coefficients_ascending_rational=list(map(str, coefficients)),
        derivative_coefficients_ascending_rational=list(map(str, (coefficients[1], 2*coefficients[2]))),
        endpoint_values_rational=[str(value(x)) for x in c])
    if lam[0] > 0:
        critical = (H*lam[0]-bA)/(2*lam[0])
        chosen = min(c[1], max(c[0], critical))
        candidates = [chosen]
        witness.update(mode='concave quadratic with clipped critical point',
            critical_point_rational=str(critical), clipped_maximizer_rational=str(chosen))
    else:
        candidates = list(c)
        witness['mode'] = 'convex or linear polynomial: both endpoints'
    maximum = max(value(x) for x in candidates)
    witness['candidate_points_rational'] = list(map(str, candidates))
    witness['candidate_values_rational'] = [str(value(x)) for x in candidates]
    witness['attaining_points_rational'] = [str(x) for x in candidates if value(x) == maximum]
    witness['maximum_rational'] = str(maximum)
    return maximum, witness


def verify_cells(face, refined):
    abox = cv(refined['coordinate_enclosures']['a'])
    assert all(lo < hi for lo, hi in abox)
    assert box(face['physical_a_box_rational']) == abox
    assert F(face['enclosure_area_rational']) == area(abox) > 0
    assert F(face['covered_area_rational']) == area(abox)
    cells = face['intersecting_original_cells']
    assert len(cells) == (45 if face['epsilon'] == 0 else 25)
    assert len({c['index'] for c in cells}) == len(cells)
    pieces = []
    for cell in cells:
        assert cell['neighbor'] == 1 and cell['domain'] == 1+2*face['epsilon']
        assert cell['depth'] == len(cell['address'])
        normalized = address_box(cell['address'])
        assert normalized == box(cell['normalized_box'])
        physical = (add(ex(F('.30')), sc(normalized[0], R)),
                    add(ex(-F('.052')), sc(normalized[1], R)))
        assert physical == box(cell['physical_box'])
        piece = intersect(physical, abox)
        assert piece is not None and piece == box(cell['intersection'])
        assert isinstance(cell['original_node_canonical_sha256'], str)
        assert len(cell['original_node_canonical_sha256']) == 64
        pieces.append(piece)
    for a, b in combinations(pieces, 2):
        overlap = intersect(a, b)
        assert overlap is None or area(overlap) == 0
    assert sum(map(area, pieces)) == area(abox)
    # Positive area, closed rectangles and disjoint interiors also cover the
    # boundaries. Original leaf/node identities remain bound by the extraction.
    return dict(positive_widths=True, closed_original_cells=True,
        disjoint_interiors=True, covered_area_rational=str(sum(map(area, pieces))),
        image_area_rational=str(area(abox)), exact_full_image_coverage=True)


def verify_jobs(face, counts):
    eps = face['epsilon']
    expected = ([('three_mixed', f) for f in range(8)]+[('three_half', 0)] if eps == 0
                else [('four', f) for f in range(8)]+[('four', 20)])
    assert [(f['series'], f['family']) for f in face['families']] == expected
    indices = {c['index'] for c in face['intersecting_original_cells']}
    result = {i: [] for i in indices}
    for family in face['families']:
        series, number = family['series'], family['family']
        multiplier = {'three_mixed': 8, 'three_half': 1, 'four': 21}[series]
        jobs = family['contributing_jobs']
        assert len(jobs) == len(indices)
        assert {j['original_cell_index'] for j in jobs} == indices
        nulls = []
        finite = []
        for job in jobs:
            index = job['original_cell_index']
            assert job['job'] == multiplier*index+number
            assert len(job['summary_canonical_sha256']) == 64
            upper = job['decoded_upper_rational']
            if upper is None:
                assert job['saved_maximum_upper'] is None
                nulls.append(job)
            else:
                assert F(upper) == outward_saved_upper(job['saved_maximum_upper'])
                finite.append(F(upper))
            result[index].append(dict(series=series, family=number, **job))
            counts['source_job_associations'] += 1
        assert len(nulls) == len(family['null_jobs_unresolved'])
        assert [j['job'] for j in nulls] == family['null_jobs_unresolved']
        assert family['complete_finite_coverage'] == (not nulls)
        if not nulls:
            assert F(family['uniform_bare_upper_rational']) == max(finite)
        else:
            assert family['uniform_bare_upper_rational'] is None
    return result


def forbidden(*args, **kwargs):
    raise AssertionError('frozen execution entry points are forbidden')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    if not str(args.output).endswith('.json.gz'):
        raise ValueError('retain the complete witness payload in a fresh .json.gz file')
    if hasattr(sys, 'set_int_max_str_digits'):
        sys.set_int_max_str_digits(0)
    own = Path(__file__).resolve().relative_to(ROOT).as_posix()
    inputs = dict(PINNED)
    inputs[own] = sha(ROOT/own)
    counts = dict(cases=0, original_cells=0, visited_cells=0, enclosed_cells=0,
        no_reference_cells=0, completed_cells=0, quadratic_endpoint_polynomials=0,
        force_vertices=0, scalar_cubic_gains=0, independent_gain_checks=0,
        source_job_associations=0, family_branch_comparisons=0, source_null_comparisons=0,
        analytic_callbacks=0, original_primitives=0, roots=0, reference_evaluations=0,
        source_replays=0, new_parameter_cells=0, subdivisions=0, retries=0)
    out = dict(status='initializing', proof_path=PROOF, checker_path=own,
        plane_path=PLANE, faces_path=FACES, refinement_path=REFINED,
        input_sha256=inputs, counts=counts, cases=[], pending_cells=[],
        uniform_cellwise_plane_ceilings_proved=False,
        all_nine_source_families_suppressed=False, whole_finite_kernel_proved=False,
        knot_theorem_proved=False, source_scope='canonical family restricted to actual K4',
        target_scope='full original target intervals; cells restrict reference a only',
        private_left_independent_theorem_applied=False)
    fatal = None
    active_cell = None
    try:
        def bind(name, digest):
            assert isinstance(digest, str) and len(digest) == 64
            assert name not in inputs or inputs[name] == digest, name
            assert sha(ROOT/name) == digest, name
            inputs[name] = digest
        for name, digest in list(inputs.items()):
            bind(name, digest)
        plane, faces, refined, source, audit = [json.loads((ROOT/p).read_text())
            for p in (PLANE, FACES, REFINED, SOURCE, AUDIT)]
        for data in (plane, faces, refined, source, audit):
            assert data['changed_inputs'] == []
            for key in ('input_sha256', 'dependencies_sha256', 'dependencies'):
                values = data.get(key)
                if isinstance(values, dict):
                    for name, digest in values.items():
                        bind(name, digest)
        assert plane['status'] == 'completed fixed saved-only protocol'
        assert plane['uniform_plane_ceilings_proved'] is True
        assert plane['proof_sha256'] == inputs[PLANE_PROOF]
        assert plane['checker_sha256'] == inputs[PLANE_CHECKER]
        assert plane['source_sha256'] == inputs[SOURCE]
        assert faces['status'] == 'completed fixed saved-only extraction'
        assert faces['all_uniform_bare_bounds_defined'] is True
        assert faces['proof_sha256'] == inputs[FACE_PROOF]
        assert faces['checker_sha256'] == inputs[FACE_CHECKER]
        assert faces['source_path'] == REFINED and faces['source_sha256'] == inputs[REFINED]
        assert refined['status'] == 'completed fixed saved-only protocol'
        assert refined['proof_sha256'] == inputs[REFINED_PROOF]
        assert refined['checker_sha256'] == inputs[REFINED_CHECKER]
        assert source['status'] == 'completed fixed protocol' and source['all_four_budgets_enclosed']
        assert audit['status'] == 'passed' and audit['source_sha256'] == inputs[SOURCE]
        assert audit['checker_sha256'] == inputs[GAIN_CHECKER]
        assert audit['verified_cotangent_boxes'] == 96
        assert [(r['beta'], r['epsilon']) for r in plane['cases']] == [(1, 0), (1, 1)]
        assert [(r['beta'], r['epsilon']) for r in faces['cases']] == list(product((0, 1), repeat=2))
        assert [(r['beta'], r['epsilon']) for r in refined['cases']] == list(product((0, 1), repeat=2))
        out['original_partition'] = faces['original_partition']
        for epsilon in (0, 1):
            face = faces['cases'][2+epsilon]
            out['pending_cells'].extend(dict(epsilon=epsilon, original_cell_index=c['index'])
                for c in face['intersecting_original_cells'])
        counts['original_cells'] = len(out['pending_cells'])
        assert counts['original_cells'] == 70

        # These two frozen modules have only stdlib imports/definitions at
        # import time. Invoke only their rational gain and square-root helpers.
        modules = []
        for name, path in (('cell_plane_gain', GAIN), ('cell_plane_gain_check', GAIN_CHECKER)):
            spec = importlib.util.spec_from_file_location(name, ROOT/path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            module.main = forbidden
            modules.append(module)
        gain, checker = modules
        def norm(value):
            squared = sum(max(abs(a), abs(b))**2 for a, b in value)
            roots = gain.sqrt_interval(squared)
            assert 0 <= roots[0] <= roots[1] and roots[0]**2 <= squared <= roots[1]**2
            return roots[1], dict(rectangle=cr(value), squared_radius_rational=str(squared), modulus=rec(roots))
        pi = iv(source['constants']['pi'])
        assert F(157, 50) < pi[0] <= pi[1] < F(22, 7)
        for epsilon in (0, 1):
            old = source['cases'][epsilon]
            p = plane['cases'][epsilon]
            face = faces['cases'][2+epsilon]
            new = refined['cases'][2+epsilon]
            saved = audit['cases'][epsilon]
            assert all((r['beta'], r['epsilon']) == (1, epsilon) for r in (old, p, face, new, saved))
            assert p['source_case_canonical_sha256'] == canonical_sha(old)
            assert p['refinement_case_canonical_sha256'] == face['refinement_case_canonical_sha256'] == canonical_sha(new)
            assert face['source_posterior_canonical_sha256'] == new['source_posterior_canonical_sha256']
            assert p['affine_case_canonical_sha256'] == new['affine_case_canonical_sha256']
            assert new['exact_linear_system_verified'] is True
            for key in ('center_exact', 'response_exact', 'posterior_radii_rational'):
                assert p[key] == new[key]
            assert new['center_exact'] == old['center_exact'] and new['response_exact'] == old['response_exact']
            assert tuple(map(F, new['parameter_center'])) == (F('.30'), -F('.052'))
            assert F(new['parameter_radius_rational']) == R
            assert all(old['domain_guards'].values())
            for name in NAMES:
                for part in ('real', 'imag'):
                    assert contained(iv(old['individual_supports'][name][part]), iv(new['coordinate_enclosures'][name][part]))
            row = dict(beta=1, epsilon=epsilon, status='initializing',
                plane_case_canonical_sha256=canonical_sha(p), face_case_canonical_sha256=canonical_sha(face),
                refinement_case_canonical_sha256=canonical_sha(new),
                original_integral_case_canonical_sha256=canonical_sha(old),
                coverage=verify_cells(face, new), cells=[], families=[])
            out['cases'].append(row)
            counts['cases'] += 1
            jobs = verify_jobs(face, counts)
            center = dict(zip(NAMES, [tuple(map(F, x)) for x in new['center_exact']]))
            response = dict(zip(NAMES, [tuple(map(F, x)) for x in new['response_exact']]))
            eta = dict(zip(NAMES, map(F, new['posterior_radii_rational'])))
            marginal, pv = p['marginal'], p['plane_value']
            assert iv(pv['pi']) == pi
            p0, rho0 = F(marginal['p0_rational']), F(marginal['rho0_rational'])
            L0 = tuple(map(F, marginal['L0_exact']))
            lam, v = quotient(L0, response['a']), quotient(response['s'], response['a'])
            nlam, wlam = norm(cx(lam))
            nv, wv = norm(cx(v))
            Ds = cv(marginal['Ds_modulus']['rectangle'])
            Da = cv(marginal['Da_modulus']['rectangle'])
            # Verify the saved midpoint/Taylor error association before its
            # two alternative substitution bounds; analytic values are inherited.
            P0, L = cv(marginal['P0']), cv(marginal['L'])
            assert p0 == sum(P0[1])/2 and rho0 == (P0[1][1]-P0[1][0])/2
            assert L0 == tuple(sum(x)/2 for x in L)
            rhoL, wrhoL = norm(csub(L, cx(L0)))
            nds, wds = norm(Ds)
            nda, wda = norm(Da)
            assert iv(marginal['rhoL']['modulus'])[1] == rhoL
            assert iv(marginal['Ds_modulus']['modulus'])[1] == nds
            assert iv(marginal['Da_modulus']['modulus'])[1] == nda
            assert F(marginal['eta_s_rational']) == eta['s']
            assert F(marginal['eta_a_rational']) == eta['a']
            remainder = F(marginal['Taylor_remainder_rational'])
            assert remainder >= 0
            rhoP = rho0+R*rhoL+eta['s']*nds+eta['a']*nda+remainder
            assert rhoP == F(marginal['rhoP_rational'])
            adjusted, wadjusted = norm(csub(Da, cx(lam)))
            rho4 = rhoP+eta['a']*nlam
            rho5 = rho0+R*rhoL+eta['s']*nds+eta['a']*adjusted+remainder
            rho = min(rho4, rho5)
            serror = eta['s']+nv*eta['a']
            oldA = iv(old['individual_supports']['a']['real'])
            oldQ = iv(old['forced_additions']['own_force'])
            GH = F(old['forced_additions']['J_upper_rational'])
            assert oldQ[0] > 0 and oldQ == iv(pv['Q'])
            assert GH == F(pv['old_GH_upper_rational'])
            Ia, Is = iv(pv['Ia']), iv(pv['Is'])
            assert Ia == iv(saved['normalized_Imcot_means']['a'])
            assert Is == iv(saved['normalized_Imcot_means']['s'])
            VP = iv(pv['normalized_VP'])
            assert len(p['plane_slabs']) == 16
            recombined = (F(0), F(0))
            for slab in p['plane_slabs']:
                contribution = sc(sub(sc(iv(slab['Ca']), F(3, 2)), iv(slab['Cs'])), F(slab['weighted_rational']))
                assert contribution == iv(slab['contribution'])
                recombined = add(recombined, contribution)
            assert recombined == VP
            row['shared_data'] = dict(center_exact=new['center_exact'], response_exact=new['response_exact'],
                posterior_radii_rational=new['posterior_radii_rational'],
                lambda_exact=list(map(str, lam)), v_exact=list(map(str, v)),
                lambda_modulus=wlam, v_modulus=wv, p0_rational=str(p0),
                rho0_rational=str(rho0), rhoL=wrhoL, Ds_modulus=wds, Da_modulus=wda,
                Da_minus_lambda_modulus=wadjusted, Taylor_remainder_rational=str(remainder),
                rhoP_rational=str(rhoP), rho4_rational=str(rho4), rho5_rational=str(rho5),
                rho_star_rational=str(rho), selected_error_equations=[n for n, x in ((4, rho4), (5, rho5)) if x == rho],
                s_substitution_radius_rational=str(serror), old_A_interval=rec(oldA), old_Q_interval=rec(oldQ),
                old_GH_endpoint_upper_rational=str(GH), pi=rec(pi), Ia=rec(Ia), Is=rec(Is), normalized_VP=rec(VP))
            global_s = iv(new['coordinate_enclosures']['s']['real'])
            for original in face['intersecting_original_cells']:
                active_cell = dict(original_cell=original, original_cell_canonical_sha256=canonical_sha(original),
                    status='initializing', source_jobs=jobs[original['index']], branches=[], family_comparisons=[])
                row['cells'].append(active_cell)
                counts['visited_cells'] += 1
                A, c = box(original['intersection'])
                assert contained(oldA, A)
                delta = (H-c[1], H-c[0])
                assert delta[0] > 0
                polynomials = [cell_quadratic(endpoint, c, center['a'], lam, p0) for endpoint in A]
                counts['quadratic_endpoint_polynomials'] += 2
                polynomial_max = max(x[0] for x in polynomials)
                UP = polynomial_max+delta[1]*rho
                affine_s = ca(cx(center['s']), cm(cx(v), csub((A, c), cx(center['a']))))
                raw_s = tuple((x[0]-serror, x[1]+serror) for x in affine_s)
                narrow_s = (max(raw_s[0][0], global_s[0]), min(raw_s[0][1], global_s[1]))
                active_cell.update(dict(reference_A_interval=rec(A), reference_c_interval=rec(c),
                    delta=rec(delta), quadratic_endpoint_polynomials=[x[1] for x in polynomials],
                    quadratic_maximum_rational=str(polynomial_max),
                    marginal_error_upper_rational=str(delta[1]*rho), UP_upper_rational=str(UP),
                    s_affine_rectangle=cr(affine_s), s_substitution_rectangle=cr(raw_s),
                    s_global_real_interval=rec(global_s),
                    s_real_intersection_endpoints_rational=list(map(str, narrow_s))))
                if narrow_s[0] > narrow_s[1]:
                    active_cell.update(status='no canonical reference: disjoint s-center enclosures',
                        no_reference_witness=dict(substitution_interval=rec(raw_s[0]), global_interval=rec(global_s),
                            intersection_lower_rational=str(narrow_s[0]), intersection_upper_rational=str(narrow_s[1])))
                    counts['no_reference_cells'] += 1
                    for job in active_cell['source_jobs']:
                        for nu in (1, 0):
                            active_cell['family_comparisons'].append(dict(series=job['series'], family=job['family'],
                                job=job['job'], nu=nu, status='vacuous: no canonical reference',
                                source_upper_rational=job['decoded_upper_rational']))
                else:
                    assert contained((F('.22'), F('.5')), narrow_s)
                    assert contained((F('.22'), F('.45')), A)
                    Q = (max(oldQ[0], oldQ[0]+K0(A[0])-K0(oldA[0])),
                         min(oldQ[1], oldQ[1]-K0(oldA[1])+K0(A[1])))
                    active_cell['Q_narrowing'] = dict(old_interval=rec(oldQ),
                        K0_cell_endpoints_rational=[str(K0(x)) for x in A],
                        K0_old_endpoints_rational=[str(K0(x)) for x in oldA],
                        narrowed_endpoints_rational=list(map(str, Q)))
                    # Q is a scalar function on a nonempty real interval,
                    # regardless of canonical feasibility: emptiness is a BUG.
                    assert Q[0] <= Q[1], 'empty Q interval is a calculation error, not a source exclusion'
                    GHcell = GH-oldQ[0]*(oldA[1]-A[1])
                    kappa = mul(pi, delta)
                    WP = mul(mul(pi, (delta[0]**2, delta[1]**2)), VP)
                    trials = {1: UP+WP[1]-pi[0]*H, 0: UP+WP[1]+GHcell/2}
                    active_cell['plane_values'] = dict(Q=rec(Q), GH_cell_upper_rational=str(GHcell),
                        kappa=rec(kappa), WP=rec(WP),
                        factorial_trial_upper_rational=str(trials[1]), forced_trial_upper_rational=str(trials[0]))
                    for nu in (1, 0):
                        branch = dict(nu=nu, trial_upper_rational=str(trials[nu]), vertices=[])
                        active_cell['branches'].append(branch)
                        bounds = [kappa, Ia, Is]+([] if nu else [Q])
                        for bits in product((0, 1), repeat=len(bounds)):
                            values = [x[bit] for x, bit in zip(bounds, bits)]
                            k, ia, iss = values[:3]
                            forces = (k*(1-iss), k*(F(3, 2)*ia-iss-F(1, 2))+(values[3]/2 if not nu else 0))
                            vertex = dict(endpoint_bits=list(bits), parameters_rational=list(map(str, values)),
                                forces_rational=list(map(str, forces)), gains={})
                            branch['vertices'].append(vertex)
                            counts['force_vertices'] += 1
                            total = F(0)
                            for name, force, cent, target, K in zip(('s', 'a'), forces, (narrow_s, A),
                                ((F('.22'), F('.5')), (F('.22'), F('.45'))), (F(88, 5), F((1+nu)*49, 10))):
                                upper, witness = gain.gain((force, force), cent, target, K)
                                counts['scalar_cubic_gains'] += 1
                                checked, checked_branches = checker.check_gain(witness, (force, force), cent, target, K)
                                counts['independent_gain_checks'] += 1
                                assert checked == upper
                                vertex['gains'][name] = witness
                                vertex.setdefault('independent_gain_checks', {})[name] = dict(
                                    upper_rational=str(checked), polynomial_branches=checked_branches)
                                total += upper
                            vertex['gain_sum_upper_rational'] = str(total)
                            vertex['plane_upper_rational'] = str(trials[nu]+total)
                        assert len(branch['vertices']) == (8 if nu else 16)
                        maximum = max(F(v['plane_upper_rational']) for v in branch['vertices'])
                        branch['cell_plane_upper_rational'] = str(maximum)
                        branch['attaining_vertices'] = [v['endpoint_bits'] for v in branch['vertices']
                            if F(v['plane_upper_rational']) == maximum]
                        for job in active_cell['source_jobs']:
                            comparison = dict(series=job['series'], family=job['family'], job=job['job'], nu=nu,
                                plane_upper_rational=str(maximum), source_upper_rational=job['decoded_upper_rational'])
                            active_cell['family_comparisons'].append(comparison)
                            if job['decoded_upper_rational'] is None:
                                comparison['status'] = 'unresolved source-null job'
                                counts['source_null_comparisons'] += 1
                            else:
                                joined = maximum+F(job['decoded_upper_rational'])
                                comparison.update(status='enclosed', joined_upper_rational=str(joined),
                                    strictly_negative=(joined < 0), gap_rational=str(-joined))
                            counts['family_branch_comparisons'] += 1
                    active_cell['status'] = 'enclosed both joined-plane alternatives'
                    counts['enclosed_cells'] += 1
                counts['completed_cells'] += 1
                out['pending_cells'].remove(dict(epsilon=epsilon, original_cell_index=original['index']))
                active_cell = None
                if counts['completed_cells'] % 10 == 0:
                    print(json.dumps(dict(completed_cells=counts['completed_cells'], pending_cells=len(out['pending_cells']),
                        gain_calls=counts['scalar_cubic_gains'])), flush=True)
            for family in face['families']:
                summary = dict(series=family['series'], family=family['family'], branches=[])
                row['families'].append(summary)
                for nu in (1, 0):
                    candidates = [(c['original_cell']['index'], x) for c in row['cells'] for x in c['family_comparisons']
                        if (x['series'], x['family'], x['nu']) == (family['series'], family['family'], nu)
                        and x['status'] != 'vacuous: no canonical reference']
                    unresolved = [index for index, x in candidates if x['status'] != 'enclosed']
                    finite = [(index, x) for index, x in candidates if x['status'] == 'enclosed']
                    maximum = max((F(x['joined_upper_rational']) for _, x in finite), default=None)
                    complete = not unresolved
                    summary['branches'].append(dict(nu=nu, complete=complete, unresolved_original_cell_indices=unresolved,
                        observed_maximum_rational=None if maximum is None else str(maximum),
                        uniform_joined_upper_rational=str(maximum) if complete and maximum is not None else None,
                        no_canonical_references=(not candidates),
                        strictly_negative=complete and (maximum is None or maximum < 0),
                        attaining=[dict(original_cell_index=i, job=x['job']) for i, x in finite
                            if F(x['joined_upper_rational']) == maximum]))
                values = [F(b['uniform_joined_upper_rational']) for b in summary['branches']
                    if b['uniform_joined_upper_rational'] is not None]
                complete = all(b['complete'] for b in summary['branches'])
                summary['both_branches_complete'] = complete
                summary['both_branches_strictly_negative'] = all(b['strictly_negative'] for b in summary['branches'])
                summary['uniform_both_branch_upper_rational'] = str(max(values)) if complete and values else None
                summary['attaining_branches'] = [b['nu'] for b in summary['branches']
                    if values and b['uniform_joined_upper_rational'] == str(max(values))]
            planes = [(c['original_cell']['index'], b['nu'], F(b['cell_plane_upper_rational']))
                for c in row['cells'] for b in c['branches']]
            maximum = max((x[2] for x in planes), default=None)
            row.update(status='completed all original cells',
                uniform_plane_upper_rational=None if maximum is None else str(maximum),
                attaining_plane_cells=[dict(original_cell_index=i, nu=nu) for i, nu, x in planes if x == maximum],
                all_nine_source_families_suppressed=all(f['both_branches_strictly_negative'] for f in row['families']))
            joined = [(c['original_cell']['index'], x) for c in row['cells'] for x in c['family_comparisons']
                if x['status'] == 'enclosed']
            joined_maximum = max((F(x['joined_upper_rational']) for _, x in joined), default=None)
            all_complete = all(f['both_branches_complete'] for f in row['families'])
            row['all_family_comparisons_complete'] = all_complete
            row['observed_joined_maximum_rational'] = None if joined_maximum is None else str(joined_maximum)
            row['uniform_all_family_upper_rational'] = str(joined_maximum) if all_complete and joined_maximum is not None else None
            row['attaining_joined_comparisons'] = [dict(original_cell_index=i, series=x['series'],
                family=x['family'], job=x['job'], nu=x['nu']) for i, x in joined
                if F(x['joined_upper_rational']) == joined_maximum]
        assert counts['cases'] == 2 and counts['completed_cells'] == counts['visited_cells'] == 70
        assert not out['pending_cells']
        assert counts['quadratic_endpoint_polynomials'] == 140
        assert counts['source_job_associations'] == 630
        assert counts['enclosed_cells']+counts['no_reference_cells'] == 70
        assert counts['force_vertices'] == 24*counts['enclosed_cells'] <= 1680
        assert counts['scalar_cubic_gains'] == counts['independent_gain_checks'] == 48*counts['enclosed_cells'] <= 3360
        assert counts['family_branch_comparisons'] == 18*counts['enclosed_cells']
        out['uniform_cellwise_plane_ceilings_proved'] = True
        out['all_nine_source_families_suppressed'] = all(c['all_nine_source_families_suppressed'] for c in out['cases'])
        out['status'] = 'completed fixed saved-only protocol'
    except (Exception, KeyboardInterrupt) as exc:
        fatal = exc
        out['status'] = 'failed saved-data calculation'
        out['error'] = dict(type=type(exc).__name__, message=str(exc))
        if active_cell is not None:
            active_cell['status'] = 'failed saved-data calculation'
            active_cell['error'] = out['error']
    out['changed_inputs'] = []
    for name, digest in inputs.items():
        if not (ROOT/name).is_file() or sha(ROOT/name) != digest:
            out['changed_inputs'].append(name)
    if out['changed_inputs']:
        out['status'] = 'changed inputs'
        out['uniform_cellwise_plane_ceilings_proved'] = False
        out['all_nine_source_families_suppressed'] = False
    out['proof_sha256'] = inputs.get(PROOF)
    out['checker_sha256'] = inputs[own]
    out['plane_sha256'], out['faces_sha256'], out['refinement_sha256'] = inputs.get(PLANE), inputs.get(FACES), inputs.get(REFINED)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    # Exclusive creation, reproducible gzip header, complete JSON witness.
    with args.output.open('xb') as raw:
        with gzip.GzipFile(filename='', mode='wb', compresslevel=1, fileobj=raw, mtime=0) as compressed:
            with io.TextIOWrapper(compressed, encoding='utf-8', newline='\n') as stream:
                json.dump(out, stream, separators=(',', ':'))
                stream.write('\n')
    print(json.dumps(dict(status=out['status'], counts=counts,
        all_nine_source_families_suppressed=out['all_nine_source_families_suppressed'],
        output_sha256=sha(args.output))), flush=True)
    if fatal is not None:
        raise fatal


if __name__ == '__main__':
    main()
