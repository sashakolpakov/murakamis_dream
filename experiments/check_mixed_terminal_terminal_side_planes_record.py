#!/usr/bin/env python3
"""Audit saved terminal-side shifts and maxima; no numerical helper imports."""
import argparse
from fractions import Fraction as F
import gzip
import hashlib
from itertools import product
import json
from math import isqrt
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SOURCE = 'repro/results/research-mixed-terminal-terminal-side-planes.json.gz'
CELLS = 'repro/results/research-mixed-terminal-source-cell-joined-plane.json.gz'
PLANE = 'repro/results/research-mixed-terminal-uniform-joined-plane.json'
FACES = 'repro/results/research-mixed-terminal-uniform-face-reserves.json'
REFINED = 'repro/results/research-mixed-terminal-quadratic-residual-refinement.json'
AFFINE = 'repro/results/research-mixed-terminal-correlated-affine-family.json'
OLD = 'repro/results/research-mixed-terminal-source-cell-comparison.json'
PRIVATE = 'repro/results/research-mixed-terminal-private-left-symmetric-transfer.json'
ALIAS = 'repro/results/research-mixed-terminal-uniform-alias-comparison.json'
CONSTANT = 'repro/results/research-mixed-terminal-uniform-constant-profile.json'
PINNED = {
    SOURCE: '29eaf5f622eb74ef21d67d766c974456a5c4cb6103477f42c9f75b11fb9c94a7',
    CELLS: '53fd53494b658f5faa76ab9fb185b9e5c492d61eb8942944d9bd8e48b2fbfbbb',
    PLANE: '4bfa03e1c61a4e34d9b6d549b5e9d666b15df606078d02258dae340055e3ee88',
    FACES: '37fc3676a9919525e16b214db0fedebd3e13b980150f5f01ec0d0b28141a07d3',
    REFINED: '2834576c2a443c9ffd24032277b5f253d9a85eac17d3f754905812e822a9a331',
    AFFINE: '51b702aa6ea44aa5891bc1146a7d5c0d22686cd814f9bbe5d9c4c63b9a16f9e1',
    OLD: 'ef6a2b2c45942f69877ec53b6c2c27129f71ece62bf31ae1d596404164f688bf',
    PRIVATE: 'a6a0c31f8132d7acf5e6037b293564c62dcebb7532e66d553d372d3667f5b3f4',
    ALIAS: '2bb8973f00571490a8ecb3d219f104ecc7be2ec025918363d95cec830653e4e2',
    CONSTANT: '5931137b18d3b6d1815ed2cf90569425910882f88e637e35391f575fcab12965',
    'experiments/check_mixed_terminal_terminal_side_planes.py':
        '6b38c04c4f0026c2764ce8920bbe8cda6fe89f4645c5b936fabf47820d64d02c',
    'notes/research_mixed_terminal_terminal_side_plane_protocol.md':
        '7eacb8ad316f0b727d593d6c520f493b252f351c0603eeaceed559297ac91135',
    'notes/research_mixed_terminal_terminal_side_marginal_enclosure.md':
        'ef21f881e158a39f46d645ec5b639c7b0a01d122b67b2f0b6c1b082798c731b7',
    'experiments/check_mixed_terminal_source_cell_comparison.py':
        '68d367fafad7a374d1292f45e771e63ef506c66e36ef09dd1c201d356fc6e6e6',
    'notes/research_mixed_terminal_uniform_main_comparison.md':
        '8658da027d6b5c5692a2da7032c657007b163617d2904b3f06b3e3c21d3b92bb',
}
H, R, MESH = F(1, 100), F(8, 125), 1 << 256
NAMES = ('e', 'xi', 't', 'a', 's')


def sha(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for b in iter(lambda: stream.read(1048576), b''):
            h.update(b)
    return h.hexdigest()


def canonical(x):
    return hashlib.sha256(json.dumps(x, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def load(name):
    with (gzip.open(ROOT/name, 'rt') if name.endswith('.gz') else (ROOT/name).open()) as stream:
        return json.load(stream)


def iv(x):
    assert x.get('finite', True) is True
    z = F(x['lower_rational']), F(x['upper_rational'])
    assert z[0] <= z[1]
    return z


def cv(x): return iv(x['real']), iv(x['imag'])
def pt(x): return x, x
def cp(z): return pt(z[0]), pt(z[1])
def add(x, y): return x[0]+y[0], x[1]+y[1]
def sub(x, y): return x[0]-y[1], x[1]-y[0]
def mul(x, y):
    p = [a*b for a in x for b in y]
    return min(p), max(p)
def scale(x, a): return mul(x, pt(a))
def ca(x, y): return add(x[0], y[0]), add(x[1], y[1])
def cd(x, y): return sub(x[0], y[0]), sub(x[1], y[1])
def cs(x, a): return scale(x[0], a), scale(x[1], a)
def cm(x, y): return sub(mul(x[0], y[0]), mul(x[1], y[1])), add(mul(x[0], y[1]), mul(x[1], y[0]))


def check_norm(record, rectangle):
    """Integer-square-root audit, not a new analytic enclosure."""
    assert cv(record['rectangle']) == rectangle and record['mesh_bits'] == 256
    square = sum(max(abs(lo), abs(hi))**2 for lo, hi in rectangle)
    assert F(record['squared_radius_rational']) == square
    n = isqrt(square.numerator*MESH*MESH//square.denominator)
    lo = F(n, MESH); hi = lo if lo*lo == square else F(n+1, MESH)
    assert iv(record['sqrt_interval']) == (lo, hi)
    assert lo*lo <= square <= hi*hi
    return hi


def check_marginal(m, refined, affine, pi):
    q = dict(zip(NAMES, (tuple(map(F, x)) for x in refined['center_exact'])))
    u = dict(zip(NAMES, (tuple(map(F, x)) for x in refined['response_exact'])))
    eta = dict(zip(NAMES, map(F, refined['posterior_radii_rational'])))
    assert all(x >= 0 for x in eta.values())
    for key in ('center_exact', 'response_exact', 'posterior_radii_rational'):
        assert m[key] == refined[key]
    assert refined['center_exact'] == affine['center'] and refined['response_exact'] == affine['response_exact']
    assert refined['exact_linear_system_verified'] and refined['affine_case_canonical_sha256'] == canonical(affine)
    ua, ut = u['a'], u['t']; uta = tuple(ua[j]+ut[j] for j in range(2))
    ma = check_norm(m['ua_modulus'], cp(ua)); mta = check_norm(m['uta_modulus'], cp(uta))
    wa, wta = R*ma+eta['a'], R*mta+eta['t']+eta['a']
    candidate = next(c for c in affine['candidates'] if F(c['multiplier_rational']) == 1)
    assert candidate['criterion_verified'] and candidate['saved_central_root_contained']
    assert candidate['all_full_original_log_disks_regular']
    terms = {x['name']: x for x in affine['primitive_terms']}
    disks = {x['name']: x['full_curvature'] for x in candidate['full_primitive_terms']}
    values, derivatives, curvatures = {}, {}, {}
    assert set(m['primitive_disks']) == {'a', 't+a'}
    for name, center, width in (('a', q['a'], wa), ('t+a', tuple(q['t'][j]+q['a'][j] for j in range(2)), wta)):
        w, t, d = m['primitive_disks'][name], terms[name], disks[name]
        assert w['primitive_term_canonical_sha256'] == canonical(t) and w['full_disk_canonical_sha256'] == canonical(d)
        assert w['center_j'] == t['center_j'] and w['center_j_prime'] == t['center_j_prime']
        assert tuple(map(F, w['center_exact'])) == tuple(map(F, t['center_exact'])) == tuple(map(F, d['center_exact'])) == center
        assert d['regular'] is True and d['stage'] == 'full'
        radius = F(d['radius_upper_rational'])
        assert F(w['new_radius_rational']) == width <= radius == F(w['saved_radius_rational'])
        strip = center[0]-radius, center[0]+radius
        assert tuple(map(F, d['real_interval_rational'])) == tuple(map(F, w['real_strip_rational'])) == strip
        assert 0 < strip[0] < strip[1] < 1
        curvature = F(d['curvature_upper_rational'])
        assert F(w['gthird_upper_rational']) == curvature >= iv(d['curvature_bound'])[1] > 0
        values[name], derivatives[name], curvatures[name] = cv(t['center_j']), cv(t['center_j_prime']), curvature
    ipi = pt(F(0)), pi
    linear = (q['t'][0]+q['a'][0]/2-F(1,4), q['t'][1]+q['a'][1]/2)
    P0 = ca(cd(values['t+a'], cs(values['a'], F(3,2))), cm(ipi, cp(linear)))
    Dt = ca(derivatives['t+a'], ipi)
    Da = ca(cd(derivatives['t+a'], cs(derivatives['a'], F(3,2))), cs(ipi, F(1,2)))
    L = ca(cm(Dt, cp(ut)), cm(Da, cp(ua)))
    for name, z in (('P0', P0), ('Dt', Dt), ('Da', Da), ('L', L)):
        assert cv(m[name]) == z
    p0, rho0 = sum(P0[1])/2, (P0[1][1]-P0[1][0])/2
    L0 = tuple(sum(x)/2 for x in L)
    assert F(m['p0_rational']) == p0 and F(m['rho0_rational']) == rho0
    assert tuple(map(F, m['L0_exact'])) == L0
    rL = check_norm(m['rhoL'], cd(L, cp(L0)))
    ndt = check_norm(m['Dt_modulus'], Dt); nda = check_norm(m['Da_modulus'], Da)
    remainder = (curvatures['t+a']*wta*wta+F(3,2)*curvatures['a']*wa*wa)/2
    rho = rho0+R*rL+eta['t']*ndt+eta['a']*nda+remainder
    assert F(m['Taylor_remainder_rational']) == remainder and F(m['rho_terminal_rational']) == rho
    height = iv(refined['coordinate_enclosures']['a']['imag'])
    delta = H-height[1], H-height[0]; d0 = H-q['a'][1]
    assert iv(m['delta']) == delta and delta[0] > 0 and F(m['delta0_rational']) == d0
    nL = check_norm(m['L0_modulus'], cp(L0))
    linear = tuple(d0*L0[j]-p0*ua[j] for j in range(2))
    nlinear = check_norm(m['combined_linear_modulus'], cp(linear))
    dot = sum(ua[j]*L0[j] for j in range(2))
    assert F(m['dot_ua_conjugateL0_rational']) == dot
    parts = (d0*p0, R*nlinear, R*R*(ma*nL-dot)/2, delta[1]*rho, eta['a']*(abs(p0)+R*nL))
    assert parts[2] >= 0 and tuple(map(F, m['whole_disk_terms_rational'])) == parts
    assert F(m['whole_disk_UP_rational']) == sum(parts)
    den = ua[0]*ua[0]+ua[1]*ua[1]; assert den > 0
    lam = (L0[0]*ua[0]+L0[1]*ua[1])/den, (L0[1]*ua[0]-L0[0]*ua[1])/den
    assert tuple(map(F, m['lambda_exact'])) == lam
    nlam = check_norm(m['lambda_modulus'], cp(lam))
    nadj = check_norm(m['Da_minus_lambda_modulus'], cd(Da, cp(lam)))
    r4, r5 = rho+eta['a']*nlam, rho0+R*rL+eta['t']*ndt+eta['a']*nadj+remainder
    assert F(m['rho4_rational']) == r4 and F(m['rho5_rational']) == r5
    assert F(m['rho_star_rational']) == min(r4, r5)
    assert m['selected_error_equations'] == [j for j, value in ((4,r4),(5,r5)) if value == min(r4,r5)]
    return q['a'], p0, lam, min(r4, r5), sum(parts)


def check_quadratic(w, A, height, a0, p0, lam):
    b = p0-lam[0]*a0[1]+lam[1]*(A-a0[0])
    coeff = H*b, H*lam[0]-b, -lam[0]
    assert F(w['A_endpoint_rational']) == A and iv(w['c_interval']) == height
    assert tuple(map(F, w['coefficients_ascending_rational'])) == coeff
    if lam[0] > 0:
        critical = coeff[1]/(2*lam[0]); points = [max(height[0], min(height[1], critical))]
        assert w['mode'] == 'clipped concave vertex' and F(w['critical_point_rational']) == critical
    else:
        points = list(height)
        assert w['mode'] == 'both endpoints' and w['critical_point_rational'] is None
    vals = [coeff[0]+coeff[1]*x+coeff[2]*x*x for x in points]
    assert list(map(F, w['candidates_rational'])) == points and list(map(F, w['values_rational'])) == vals
    assert F(w['maximum_rational']) == max(vals)
    return max(vals)


def check_branch(new, old, oldup, bestup, params, centers, count, cell=False):
    nu = old['nu']; shift = bestup-oldup; assert nu in (0,1) and shift <= 0
    assert new['nu'] == nu and new['source_branch_canonical_sha256'] == canonical(old)
    trial = F(old['trial_upper_rational'])
    assert F(new['old_trial_upper_rational']) == trial and F(new['UP_change_rational']) == shift
    assert F(new['new_trial_upper_rational']) == trial+shift
    bounds = [params[k] for k in ('kappa','Ia','Is')]+([] if nu else [params['Q']])
    bitslist = list(product((0,1), repeat=len(bounds)))
    assert [v['endpoint_bits'] for v in new['vertices']] == [v['endpoint_bits'] for v in old['vertices']] == [list(x) for x in bitslist]
    totals = []
    for nv, ov, bits in zip(new['vertices'], old['vertices'], bitslist):
        assert nv['source_vertex_canonical_sha256'] == canonical(ov)
        vals = [bound[bit] for bound, bit in zip(bounds, bits)]
        assert list(map(F, nv['parameters_rational'])) == list(map(F, ov['parameters_rational'])) == vals
        k, ia, iss = vals[:3]
        forces = (k*(1-iss), k*(F(3,2)*ia-iss-F(1,2))+(vals[3]/2 if not nu else 0))
        assert tuple(map(F, ov['forces_rational'])) == forces
        sums = []
        assert set(nv['gains']) == set(ov['gains']) == {'s','a'}
        for name, force, target, K in zip(('s','a'), forces, ((F(11,50),F(1,2)),(F(11,50),F(9,20))), (F(88,5),F((1+nu)*49,10))):
            ng, og = nv['gains'][name], ov['gains'][name]
            assert ng['source_witness_canonical_sha256'] == canonical(og)
            assert F(ng['unchanged_force_rational']) == force and iv(og['force']) == (force,force)
            assert iv(ng['unchanged_center']) == iv(og['center']) == centers[name]
            assert iv(ng['unchanged_target']) == iv(og['target']) == target
            assert F(ng['K_rational']) == F(og['K_rational']) == K
            upper = max([F(0)]+[iv(b['value'])[1] for b in og['branches']])
            assert F(ng['upper_rational']) == F(og['upper_rational']) == upper
            if cell: assert F(ov['independent_gain_checks'][name]['upper_rational']) == upper
            sums.append(upper); count['gain_upper_associations'] += 1
        total = trial+sum(sums)
        assert F(ov['gain_sum_upper_rational']) == F(nv['unchanged_gain_sum_rational']) == sum(sums)
        assert F(ov['plane_upper_rational']) == F(nv['old_plane_upper_rational']) == total
        assert F(nv['new_plane_upper_rational']) == total+shift
        totals.append(total); count['vertices'] += 1
    key = 'cell_plane_upper_rational' if cell else 'uniform_plane_upper_rational'
    assert F(old[key]) == F(new['old_plane_upper_rational']) == max(totals)
    assert F(new['new_plane_upper_rational']) == max(totals)+shift
    attaining = [list(b) for b,x in zip(bitslist,totals) if x == max(totals)]
    assert old['attaining_vertices'] == new['attaining_vertices'] == attaining
    return max(totals)+shift


def upward(q, digits=12):
    n = -((-q.numerator*10**digits)//q.denominator)
    sign = '-' if n < 0 else ''; a,b = divmod(abs(n),10**digits)
    return f'{sign}{a}.{b:0{digits}d}'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args(); assert not args.output.exists()
    if hasattr(sys, 'set_int_max_str_digits'): sys.set_int_max_str_digits(0)
    inputs = dict(PINNED); own = Path(__file__).resolve().relative_to(ROOT).as_posix()
    inputs[own] = sha(ROOT/own)
    for name,digest in inputs.items(): assert sha(ROOT/name) == digest, name
    data = {name:load(name) for name in (SOURCE,CELLS,PLANE,FACES,REFINED,AFFINE,OLD,PRIVATE,ALIAS,CONSTANT)}
    for d in data.values():
        assert d.get('changed_inputs',[]) == []
        for key in ('input_sha256','dependencies_sha256','dependencies'):
            if isinstance(d.get(key),dict):
                for name,digest in d[key].items():
                    assert isinstance(digest,str) and len(digest) == 64
                    assert name not in inputs or inputs[name] == digest
                    inputs[name] = digest
    for name,digest in inputs.items(): assert sha(ROOT/name) == digest, name
    source, cells, plane, faces, refined, affine, old, private, alias, constant = (data[p] for p in (SOURCE,CELLS,PLANE,FACES,REFINED,AFFINE,OLD,PRIVATE,ALIAS,CONSTANT))
    assert source['status'] == 'completed fixed saved-only protocol' and len(source['input_sha256']) == 545
    assert source['all_updated_bounds_enclosed'] and not source['pending_cells']
    assert not source['complete_terminal_kernel_proved'] and not source['knot_theorem_proved']
    assert source['old_private_left_plane_outcomes_retained']
    assert source['checker_sha256'] == PINNED['experiments/check_mixed_terminal_terminal_side_planes.py']
    assert source['proof_sha256'] == PINNED['notes/research_mixed_terminal_terminal_side_plane_protocol.md']
    assert old['status'] == 'passed exact saved comparison' and old['source_record_sha256'] == PINNED[CELLS]
    assert old['paid_real_entropy_branches'] == 31 and old['unresolved_real_entropy_branches'] == 5
    assert cells['uniform_cellwise_plane_ceilings_proved'] and not cells['pending_cells']
    assert cells['counts']['no_reference_cells'] == cells['counts']['source_null_comparisons'] == 0
    assert private['status'] == 'passed' and private['rational_barrier_witnesses_verified']
    privategap = F(private['scoped_raw_face_gap_rational']); assert privategap == F(51,20000)
    assert private['domain']['beta'] == private['domain']['epsilon'] == 1
    assert F(private['domain']['transfer_selected_height_rational']) == H
    assert alias['all_joined_endpoint_gaps_exceed_1_over_20'] and F(alias['common_gap_lower_rational']) > F(1,20)
    assert constant['uniform_constant_profile_gap_proved'] and F(constant['common_raw_gap_rational']) == F(1,100)
    assert F(constant['common_exact_deficit_lower_rational']) > F(1,100)
    assert F(old['separate_main_gap_rational']) == F(1,400)
    assert [(c['beta'],c['epsilon']) for c in source['cases']] == [(1,0),(1,1)]
    count = dict(cases=0,cells=0,quadratics=0,vertices=0,gain_upper_associations=0,pairings=0,summaries=0)
    rows, inventory, marginal_inventory = [], [], []
    oldrows = {(r['epsilon'],r['series'],r['family'],r['nu']):r for r in old['comparisons']}
    assert len(oldrows) == 36
    for eps, case in enumerate(source['cases']):
        oc, op, face, ref, aff = cells['cases'][eps], plane['cases'][eps], faces['cases'][2+eps], refined['cases'][2+eps], affine['cases'][2+eps]
        assert all((x['beta'],x['epsilon']) == (1,eps) for x in (case,oc,op,face,ref,aff))
        assert case['old_plane_case_canonical_sha256'] == canonical(op)
        assert case['old_cell_case_canonical_sha256'] == canonical(oc)
        assert case['refinement_case_canonical_sha256'] == canonical(ref) and case['affine_case_canonical_sha256'] == canonical(aff)
        assert oc['face_case_canonical_sha256'] == canonical(face) and oc['plane_case_canonical_sha256'] == canonical(op)
        assert face['refinement_case_canonical_sha256'] == op['refinement_case_canonical_sha256'] == canonical(ref)
        assert case['inherited_coverage'] == oc['coverage'] and oc['coverage']['exact_full_image_coverage']
        pi = iv(op['plane_value']['pi']); assert F(157,50) < pi[0] <= pi[1] < F(22,7)
        a0,p0,lam,rho,up = check_marginal(case['terminal_marginal'],ref,aff,pi)
        oldup = F(op['marginal']['UP_upper_rational']); bestup = min(oldup,up)
        assert F(case['old_global_UP_rational']) == oldup and F(case['new_global_UP_rational']) == up
        assert F(case['best_global_UP_rational']) == bestup
        assert case['global_UP_minimizers'] == [k for k,v in (('old',oldup),('terminal',up)) if v == bestup]
        assert case['independent_private_left_raw_gap_rational'] == ('51/20000' if eps else None)
        params = {k:iv(op['plane_value'][k]) for k in ('kappa','Ia','Is','Q')}
        centers = {k:iv(ref['coordinate_enclosures'][k]['real']) for k in ('s','a')}
        assert [b['nu'] for b in case['global_branches']] == [b['nu'] for b in op['branches']] == [1,0]
        globalplanes = {}
        for nb,ob in zip(case['global_branches'],op['branches']):
            nu = ob['nu']; extra = -pi[0]*H if nu else F(op['plane_value']['old_GH_upper_rational'])/2
            assert F(ob['trial_upper_rational']) == oldup+iv(op['plane_value']['WP'])[1]+extra
            globalplanes[nu] = check_branch(nb,ob,oldup,bestup,params,centers,count)
        originals = face['intersecting_original_cells']
        assert [c['original_cell'] for c in case['cells']] == [c['original_cell'] for c in oc['cells']] == originals
        assert len(originals) == (45 if eps == 0 else 25)
        expected = ([('three_mixed',i) for i in range(8)]+[('three_half',0)] if eps == 0 else [('four',i) for i in range(8)]+[('four',20)])
        assert [(f['series'],f['family']) for f in case['families']] == [(f['series'],f['family']) for f in face['families']] == expected
        jobs = {(j['original_cell_index'],f['series'],f['family']):j for f in face['families'] for j in f['contributing_jobs']}
        assert len(jobs) == 9*len(originals)
        assert all(f['complete_finite_coverage'] and not f['null_jobs_unresolved'] for f in face['families'])
        for f in face['families']: assert F(f['uniform_bare_upper_rational']) == max(F(j['decoded_upper_rational']) for j in f['contributing_jobs'])
        local = {}
        for c,oldc in zip(case['cells'],oc['cells']):
            orig = c['original_cell']; idx = orig['index']
            assert c['status'] == 'completed unchanged-gain update' and c['source_cell_canonical_sha256'] == canonical(oldc)
            assert oldc['original_cell_canonical_sha256'] == canonical(orig)
            A,height = (tuple(map(F,z)) for z in orig['intersection'])
            assert A == iv(oldc['reference_A_interval']) and height == iv(oldc['reference_c_interval'])
            assert A[0] <= A[1] and height[0] <= height[1] < H
            assert len(c['quadratic_endpoint_maximizations']) == 2
            maxima = [check_quadratic(w,x,height,a0,p0,lam) for w,x in zip(c['quadratic_endpoint_maximizations'],A)]
            count['quadratics'] += 2
            error = (H-height[0])*rho; terminalup = max(maxima)+error
            cou = F(oldc['UP_upper_rational']); cbest = min(cou,terminalup)
            assert F(c['marginal_error_rational']) == error and F(c['terminal_UP_rational']) == terminalup
            assert F(c['old_UP_rational']) == cou and F(c['best_UP_rational']) == cbest
            assert c['UP_minimizers'] == [k for k,v in (('old',cou),('terminal',terminalup)) if v == cbest]
            assert c['unchanged_plane_values'] == oldc['plane_values'] and c['unchanged_s_center'] == oldc['s_real_intersection_endpoints_rational']
            pv = oldc['plane_values']; params = {k:iv(oc['shared_data'][k]) for k in ('Ia','Is')}
            params.update(kappa=iv(pv['kappa']),Q=iv(pv['Q']))
            centers = dict(s=tuple(map(F,c['unchanged_s_center'])),a=A)
            planes = {}
            assert [b['nu'] for b in c['branches']] == [b['nu'] for b in oldc['branches']] == [1,0]
            for nb,ob in zip(c['branches'],oldc['branches']):
                nu = ob['nu']; extra = -pi[0]*H if nu else F(pv['GH_cell_upper_rational'])/2
                assert F(ob['trial_upper_rational']) == cou+iv(pv['WP'])[1]+extra
                assert F(pv['factorial_trial_upper_rational' if nu else 'forced_trial_upper_rational']) == F(ob['trial_upper_rational'])
                planes[nu] = check_branch(nb,ob,cou,cbest,params,centers,count,cell=True)
            assert len(c['family_comparisons']) == 18
            seen = set()
            oldcomparisons = {(x['series'],x['family'],x['nu']):x for x in oldc['family_comparisons']}
            for x in c['family_comparisons']:
                key = (x['series'],x['family'],x['nu']); assert key not in seen; seen.add(key)
                job = jobs[idx,*key[:2]]; prior = oldcomparisons[key]
                assert x['old_comparison_canonical_sha256'] == canonical(prior)
                assert x['job'] == prior['job'] == job['job']
                src = F(job['decoded_upper_rational'])
                assert F(x['source_upper_rational']) == F(prior['source_upper_rational']) == src
                assert F(x['old_joined_upper_rational']) == F(prior['joined_upper_rational'])
                assert F(prior['joined_upper_rational']) == F(prior['plane_upper_rational'])+src
                value = planes[key[2]]+src
                assert F(x['new_joined_upper_rational']) == value and F(x['gap_rational']) == -value
                assert x['strictly_negative'] == (value < 0)
                local.setdefault(key,[]).append((idx,value)); count['pairings'] += 1
            assert seen == {(series,family,nu) for series,family in expected for nu in (1,0)}
            inventory.append(dict(epsilon=eps,original_cell_index=idx,source_cell_canonical_sha256=canonical(c),
                old_UP_rational=str(cou),terminal_UP_rational=str(terminalup),best_UP_rational=str(cbest),
                plane_uppers_rational={str(k):str(v) for k,v in planes.items()}))
            count['cells'] += 1
        for fam,ff in zip(case['families'],face['families']):
            assert [b['nu'] for b in fam['branches']] == [1,0]
            for b in fam['branches']:
                nu = b['nu']; key = fam['series'],fam['family'],nu
                values = local[key]; assert len(values) == len(originals)
                cu = max(v for _,v in values); gu = globalplanes[nu]+F(ff['uniform_bare_upper_rational']); best = min(cu,gu)
                assert F(b['updated_global_joined_upper_rational']) == gu and F(b['updated_cellwise_joined_upper_rational']) == cu
                assert F(b['best_complete_upper_rational']) == best and F(b['gap_rational']) == -best
                assert b['strictly_negative'] == (best < 0)
                assert b['attaining_cells'] == [i for i,v in values if v == cu]
                assert b['selected_routes'] == [name for name,v in (('global',gu),('cellwise',cu)) if v == best]
                prior = oldrows[eps,*key]; direct = eps == 1 and prior['profile_index'] == 2
                assert prior['source_family_canonical_sha256'] == canonical(ff)
                assert gu <= F(prior['old_global_upper_rational']) and cu <= F(prior['new_same_cell_upper_rational'])
                assert F(prior['best_plane_upper_rational']) == min(F(prior['old_global_upper_rational']),F(prior['new_same_cell_upper_rational']))
                effective = min(best,-privategap) if direct else best
                rows.append(dict(epsilon=eps,series=key[0],family=key[1],profile_index=prior['profile_index'],label=prior['label'],nu=nu,
                    previous_comparison=prior,terminal_global_upper_rational=str(gu),terminal_cell_upper_rational=str(cu),
                    best_plane_upper_rational=str(best),direct_private_left_upper_rational=str(-privategap) if direct else None,
                    proved_upper_rational=str(effective),proved_upper_decimal_ceiling=upward(effective),strictly_negative=effective<0,
                    gap_rational=str(-effective),attaining_cells=b['attaining_cells'],selected_routes=b['selected_routes']))
                count['summaries'] += 1
        marginal_inventory.append(dict(epsilon=eps,source_case_canonical_sha256=canonical(case),
            old_global_UP_rational=str(oldup),terminal_global_UP_rational=str(up),best_global_UP_rational=str(bestup),
            global_plane_uppers_rational={str(k):str(v) for k,v in globalplanes.items()}))
        assert case['status'] == 'completed both whole-family and all original-cell updates'; count['cases'] += 1
    assert count == dict(cases=2,cells=70,quadratics=140,vertices=1728,gain_upper_associations=3456,pairings=1260,summaries=36)
    assert source['counts'] == dict(cases=2,completed_cells=70,quadratic_endpoint_maximizations=140,saved_vertex_recombinations=1728,
        saved_gain_witness_recombinations=3456,cell_family_branch_comparisons=1260,uniform_family_branch_summaries=36,
        gain_calls=0,analytic_calls=0,roots=0,source_evaluations=0,subdivisions=0,retries=0)
    paid = [r for r in rows if r['strictly_negative']]; remaining = [r for r in rows if not r['strictly_negative']]
    assert len(paid) == 32 and {(r['epsilon'],r['profile_index'],r['nu']) for r in remaining} == {(0,1,1),(0,8,1),(1,0,1),(1,0,0)}
    newpaid = [r for r in paid if not r['previous_comparison']['strictly_negative']]
    assert len(newpaid) == 1 and (newpaid[0]['epsilon'],newpaid[0]['profile_index'],newpaid[0]['nu']) == (1,8,1)
    assert F(newpaid[0]['proved_upper_rational']) < -F(1978,5000000)
    remaining_ceilings = {(0,1,1):F('0.004806'),(0,8,1):F('0.007611'),
                          (1,0,1):F('0.011871'),(1,0,0):F('0.008978')}
    for r in remaining:
        assert 0 < F(r['proved_upper_rational']) <= remaining_ceilings[r['epsilon'],r['profile_index'],r['nu']]
    assert all(F(r['proved_upper_rational']) < -F(1,2600) for r in paid)
    smallest = min(-F(r['proved_upper_rational']) for r in paid)
    assert smallest == -F(newpaid[0]['proved_upper_rational']) > F(1,2600)
    changed = [name for name,digest in inputs.items() if sha(ROOT/name) != digest]; assert not changed
    output = dict(status='passed exact saved terminal-side audit',input_sha256=inputs,changed_inputs=changed,
        source_path=SOURCE,source_sha256=PINNED[SOURCE],previous_audit_sha256=PINNED[OLD],counts=count,
        inherited_analytic_endpoints='Original logarithms and curvature disks, certified reference family, and scalar gain certificates are inherited from the pinned reviewed records; only rational recombinations and integer-square-root witnesses are checked here.',
        marginal_cases=marginal_inventory,cell_inventory=inventory,comparisons=rows,newly_paid_comparisons=newpaid,
        paid_real_entropy_branches=32,unresolved_real_entropy_branches=4,unresolved=remaining,
        smallest_paid_real_entropy_gap_rational=str(smallest),common_paid_raw_floor_rational='1/2600',
        separate_main_gap_rational='1/400',separate_alias_gap_rational='1/20',separate_constant_gap_rational='1/100',
        separate_private_left_gap_rational='51/20000',conditional_remaining_gap_name='gamma4',
        conditional_complete_raw_gap='min(gamma4,1/2600)',conditional_complete_finite_gap='min(gamma4,1/2600)/2',
        new_gain_evaluations=0,analytic_callbacks=0,roots=0,source_replays=0,subdivisions=0,
        complete_terminal_kernel_proved=False,full_source_proved=False,knot_theorem_proved=False,
        scope='Canonical actual K4, H=1/100, independent original targets and both complete selected-weight alternatives. Positive upper bounds remain inconclusive; private-left is a separate direct theorem.')
    args.output.parent.mkdir(parents=True,exist_ok=True)
    with args.output.open('x') as stream: json.dump(output,stream,separators=(',',':')); stream.write('\n')
    print(json.dumps(dict(status=output['status'],counts=count,bindings=len(inputs),paid=32,remaining=4,
        largest_paid_upper_decimal_ceiling=upward(-smallest),output_sha256=sha(args.output))))


if __name__ == '__main__':
    main()
