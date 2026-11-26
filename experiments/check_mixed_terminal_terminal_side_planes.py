#!/usr/bin/env python3
"""Update saved terminal plane trials only; no new gain or analytic calls."""
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import io
from itertools import product
import json
from math import isqrt
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
PROOF = 'notes/research_mixed_terminal_terminal_side_plane_protocol.md'
THEORY = 'notes/research_mixed_terminal_terminal_side_marginal_enclosure.md'
PLANE = 'repro/results/research-mixed-terminal-uniform-joined-plane.json'
CELLS = 'repro/results/research-mixed-terminal-source-cell-joined-plane.json.gz'
FACES = 'repro/results/research-mixed-terminal-uniform-face-reserves.json'
REFINED = 'repro/results/research-mixed-terminal-quadratic-residual-refinement.json'
POSTERIOR = 'repro/results/research-mixed-terminal-split-taylor-completion.json'
SPLIT = 'repro/results/research-mixed-terminal-split-taylor-inclusion.json'
AFFINE = 'repro/results/research-mixed-terminal-correlated-affine-family.json'
INTEGRAL = 'repro/results/research-mixed-terminal-four-input-integral-budget.json'
PRIVATE = 'repro/results/research-mixed-terminal-private-left-symmetric-transfer.json'
PINNED = {
    'notes/research_mixed_terminal_terminal_side_plane_protocol.md': '7eacb8ad316f0b727d593d6c520f493b252f351c0603eeaceed559297ac91135',
    'notes/research_mixed_terminal_terminal_side_marginal_enclosure.md': 'ef21f881e158a39f46d645ec5b639c7b0a01d122b67b2f0b6c1b082798c731b7',
    'repro/results/research-mixed-terminal-uniform-joined-plane.json': '4bfa03e1c61a4e34d9b6d549b5e9d666b15df606078d02258dae340055e3ee88',
    'repro/results/research-mixed-terminal-source-cell-joined-plane.json.gz': '53fd53494b658f5faa76ab9fb185b9e5c492d61eb8942944d9bd8e48b2fbfbbb',
    'repro/results/research-mixed-terminal-uniform-face-reserves.json': '37fc3676a9919525e16b214db0fedebd3e13b980150f5f01ec0d0b28141a07d3',
    'repro/results/research-mixed-terminal-quadratic-residual-refinement.json': '2834576c2a443c9ffd24032277b5f253d9a85eac17d3f754905812e822a9a331',
    'repro/results/research-mixed-terminal-split-taylor-completion.json': 'e04521450e1973658cbd602aa0a8f54d4c7d40c968b4b90d65374d570981c617',
    'repro/results/research-mixed-terminal-split-taylor-inclusion.json': 'a25587e526dc753306eb690b76f1f07d0d05410be315c6675023bd87ae42e202',
    'repro/results/research-mixed-terminal-correlated-affine-family.json': '51b702aa6ea44aa5891bc1146a7d5c0d22686cd814f9bbe5d9c4c63b9a16f9e1',
    'repro/results/research-mixed-terminal-four-input-integral-budget.json': '9831e8bdbc884cfc0b0c99dbc7f92245403988ae7dc4bbbba86b5606c5a1575e',
    'repro/results/research-mixed-terminal-private-left-symmetric-transfer.json': 'a6a0c31f8132d7acf5e6037b293564c62dcebb7532e66d553d372d3667f5b3f4',
    'repro/results/research-mixed-terminal-four-input-integral-budget-saved-audit.json': 'cda9eef92856387d0ec0dccca6311512bb980034a07832ab89a99a7bc733d6c3',
    'repro/results/research-mixed-terminal-source-cell-comparison.json': 'ef6a2b2c45942f69877ec53b6c2c27129f71ece62bf31ae1d596404164f688bf',
    'notes/research_mixed_terminal_uniform_joined_plane.md': '12ab4cd4e94a521ac97da4e8f71aa68b2352764cd2d283cf123e9f5f113b11e5',
    'experiments/check_mixed_terminal_uniform_joined_plane.py': '35fbf2b1a3d2722f1c930cf21704a3121ed0460e621fdfe9420f2b679f39dd16',
    'notes/research_mixed_terminal_source_cell_joined_plane.md': '0d5d3d1c38e0423f2ea130fba5fce0a4c08379abcc69edb1d69cebde692d4c8d',
    'experiments/check_mixed_terminal_source_cell_joined_plane.py': 'dd4bbdc4411a6bc1a3d5a924e101c7cebf4ee2c697e57d4fd26932251884f586',
    'experiments/check_mixed_terminal_source_cell_comparison.py': '68d367fafad7a374d1292f45e771e63ef506c66e36ef09dd1c201d356fc6e6e6',
    'notes/research_mixed_terminal_uniform_face_reserves.md': 'b770a8d3c182c9936367c1f43edd2e74f483ffd5ead2d61fa44b85420109a363',
    'experiments/check_mixed_terminal_uniform_face_reserves.py': 'b631f8d2b23acab944fc8ab900c2a6dfcacd9da1922643f58919d4185ebb7a6d',
    'notes/research_mixed_terminal_quadratic_residual_refinement.md': 'f012610187e14b824fdfeea730bc71ffde1660687ffbdcc491bc945c6a54d596',
    'experiments/check_mixed_terminal_quadratic_residual_refinement.py': '251fc4b3c656201ab5451287577baddb4d4be8122ff34a1318078de0f8501a05',
    'notes/research_mixed_terminal_all_input_affine_enclosures.md': '6412be85ca87c01a0b363191c724dc1e7357c00939ce5c379a7c501f3565215f',
    'experiments/check_mixed_terminal_split_taylor_completion.py': 'bfa49b46454c324d05047352251e6f7aefa68cbec8d53ab5914c935bec502580',
    'notes/research_mixed_terminal_private_left_symmetric_transfer.md': '1c007e90e1fd8057d8b3773fd712fbb331b0d71c4b253664535805b37e9e7199',
    'experiments/check_mixed_terminal_private_left_symmetric_transfer.py': '9fa43a9d0faa0e7331c87d2ba5f35d32b80f23af8c62ed1b5df1fbada0074b01',
    'notes/research_mixed_terminal_canonical_source_domain.md': 'd50929a1a1c02d034feb5ca5f9ebf6e6da70bd6b0a1eb4a67f67fd1108d18d11',
    'notes/research_mixed_terminal_four_input_integral_budget.md': '90ec6c9d4b3641a01e789b64dd0d26053b402c2914b99cafe81eff8ad4265cb9',
    'experiments/check_mixed_terminal_four_input_integral_budget.py': 'd38f41d186bf31d3255861c45cb0500d1a21a4eb1bfd4d366c6a956efc614bf4',
}
H, R = F(1, 100), F(8, 125)
NAMES = ('e', 'xi', 't', 'a', 's')
MESH = 1 << 256


def sha(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(1048576), b''):
            h.update(chunk)
    return h.hexdigest()


def canonical_sha(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True,
        separators=(',', ':')).encode()).hexdigest()


def load(path):
    opener = gzip.open if str(path).endswith('.gz') else open
    with opener(path, 'rt', encoding='utf-8') as stream:
        return json.load(stream)


def iv(v):
    if 'finite' in v:
        assert v['finite'] is True
    a, b = F(v['lower_rational']), F(v['upper_rational'])
    assert a <= b
    return a, b


def rec(v): return dict(lower_rational=str(v[0]), upper_rational=str(v[1]))
def cv(v): return iv(v['real']), iv(v['imag'])
def cr(v): return dict(real=rec(v[0]), imag=rec(v[1]))
def ex(v): return F(v), F(v)
def cx(v): return ex(v[0]), ex(v[1])
def add(x, y): return x[0]+y[0], x[1]+y[1]
def neg(x): return -x[1], -x[0]
def sub(x, y): return add(x, neg(y))
def mul(x, y):
    values = [a*b for a in x for b in y]
    return min(values), max(values)
def sc(x, a): return mul(x, ex(a))
def ca(x, y): return add(x[0], y[0]), add(x[1], y[1])
def cs(x, a): return sc(x[0], a), sc(x[1], a)
def csub(x, y): return sub(x[0], y[0]), sub(x[1], y[1])
def cm(x, y):
    return sub(mul(x[0], y[0]), mul(x[1], y[1])), add(mul(x[0], y[1]), mul(x[1], y[0]))
def quotient(x, y):
    d = y[0]**2+y[1]**2
    assert d > 0
    return (x[0]*y[0]+x[1]*y[1])/d, (x[1]*y[0]-x[0]*y[1])/d
def contained(outer, inner): return outer[0] <= inner[0] <= inner[1] <= outer[1]


def norm(z):
    square = sum(max(abs(lo), abs(hi))**2 for lo, hi in z)
    n = isqrt((square.numerator*MESH*MESH)//square.denominator)
    lo = F(n, MESH)
    hi = lo if lo*lo == square else F(n+1, MESH)
    assert 0 <= lo <= hi and lo*lo <= square <= hi*hi
    return hi, dict(rectangle=cr(z), squared_radius_rational=str(square),
        sqrt_interval=rec((lo, hi)), mesh_bits=256)


def quadratic(A, c, a0, lam, p0):
    b = p0-lam[0]*a0[1]+lam[1]*(A-a0[0])
    coeff = H*b, H*lam[0]-b, -lam[0]
    def value(x): return coeff[0]+coeff[1]*x+coeff[2]*x*x
    if lam[0] > 0:
        critical = (H*lam[0]-b)/(2*lam[0])
        candidates = [min(c[1], max(c[0], critical))]
        mode = 'clipped concave vertex'
    else:
        critical, candidates, mode = None, list(c), 'both endpoints'
    values = list(map(value, candidates))
    return max(values), dict(A_endpoint_rational=str(A), c_interval=rec(c),
        coefficients_ascending_rational=list(map(str, coeff)), mode=mode,
        critical_point_rational=None if critical is None else str(critical),
        candidates_rational=list(map(str, candidates)), values_rational=list(map(str, values)),
        maximum_rational=str(max(values)))


def terminal_marginal(aff, new, candidate, pi):
    center = dict(zip(NAMES, [tuple(map(F, x)) for x in new['center_exact']]))
    response = dict(zip(NAMES, [tuple(map(F, x)) for x in new['response_exact']]))
    eta = dict(zip(NAMES, map(F, new['posterior_radii_rational'])))
    assert len(center) == len(response) == len(eta) == 5
    assert all(x >= 0 for x in eta.values())
    ua, ut = response['a'], response['t']
    uta = ua[0]+ut[0], ua[1]+ut[1]
    nua, wua = norm(cx(ua))
    nuta, wuta = norm(cx(uta))
    wa, wta = R*nua+eta['a'], R*nuta+eta['t']+eta['a']
    terms = {t['name']: t for t in aff['primitive_terms']}
    full = {t['name']: t['full_curvature'] for t in candidate['full_primitive_terms']}
    zta = center['t'][0]+center['a'][0], center['t'][1]+center['a'][1]
    values, derivatives, curvature, witnesses = {}, {}, {}, {}
    for name, z, width in (('a', center['a'], wa), ('t+a', zta, wta)):
        term, disk = terms[name], full[name]
        assert tuple(map(F, term['center_exact'])) == tuple(map(F, disk['center_exact'])) == z
        assert disk['regular'] is True and disk['stage'] == 'full'
        radius = F(disk['radius_upper_rational'])
        assert 0 <= width <= radius
        lo, hi = map(F, disk['real_interval_rational'])
        assert 0 < lo == z[0]-radius < hi == z[0]+radius < 1
        m = F(disk['curvature_upper_rational'])
        assert m >= iv(disk['curvature_bound'])[1] and m > 0
        values[name], derivatives[name] = cv(term['center_j']), cv(term['center_j_prime'])
        curvature[name] = m
        witnesses[name] = dict(center_exact=list(map(str, z)),
            center_j=term['center_j'], center_j_prime=term['center_j_prime'],
            primitive_term_canonical_sha256=canonical_sha(term),
            full_disk_canonical_sha256=canonical_sha(disk),
            new_radius_rational=str(width), saved_radius_rational=str(radius),
            real_strip_rational=[str(lo), str(hi)], gthird_upper_rational=str(m))
    ipi = (ex(0), pi)
    zlinear = (center['t'][0]+center['a'][0]/2-F(1, 4),
               center['t'][1]+center['a'][1]/2)
    P0 = ca(csub(values['t+a'], cs(values['a'], F(3, 2))), cm(ipi, cx(zlinear)))
    Dt = ca(derivatives['t+a'], ipi)
    Da = ca(csub(derivatives['t+a'], cs(derivatives['a'], F(3, 2))), cs(ipi, F(1, 2)))
    L = ca(cm(Dt, cx(ut)), cm(Da, cx(ua)))
    p0, rho0 = sum(P0[1])/2, (P0[1][1]-P0[1][0])/2
    L0 = tuple(sum(x)/2 for x in L)
    rhoL, wrhoL = norm(csub(L, cx(L0)))
    ndt, wdt = norm(Dt)
    nda, wda = norm(Da)
    remainder = (curvature['t+a']*wta*wta+F(3, 2)*curvature['a']*wa*wa)/2
    rho = rho0+R*rhoL+eta['t']*ndt+eta['a']*nda+remainder
    height = iv(new['coordinate_enclosures']['a']['imag'])
    delta = H-height[1], H-height[0]
    assert delta[0] > 0
    delta0 = H-center['a'][1]
    nL, wL = norm(cx(L0))
    lin = tuple(delta0*L0[j]-p0*ua[j] for j in range(2))
    nlin, wlin = norm(cx(lin))
    dot = sum(ua[j]*L0[j] for j in range(2))
    qsupport = R*R*(nua*nL-dot)/2
    assert qsupport >= 0
    parts = (delta0*p0, R*nlin, qsupport, delta[1]*rho, eta['a']*(abs(p0)+R*nL))
    UP = sum(parts)
    lam = quotient(L0, ua)
    nlam, wlam = norm(cx(lam))
    nadj, wadj = norm(csub(Da, cx(lam)))
    rho4 = rho+eta['a']*nlam
    rho5 = rho0+R*rhoL+eta['t']*ndt+eta['a']*nadj+remainder
    witness = dict(primitive_disks=witnesses, center_exact=new['center_exact'],
        response_exact=new['response_exact'], posterior_radii_rational=new['posterior_radii_rational'],
        P0=cr(P0), Dt=cr(Dt), Da=cr(Da), L=cr(L),
        p0_rational=str(p0), rho0_rational=str(rho0), L0_exact=list(map(str, L0)),
        ua_modulus=wua, uta_modulus=wuta, rhoL=wrhoL, Dt_modulus=wdt, Da_modulus=wda,
        Taylor_remainder_rational=str(remainder), rho_terminal_rational=str(rho),
        delta=rec(delta), delta0_rational=str(delta0), L0_modulus=wL,
        combined_linear_modulus=wlin, dot_ua_conjugateL0_rational=str(dot),
        whole_disk_terms_rational=list(map(str, parts)), whole_disk_UP_rational=str(UP),
        lambda_exact=list(map(str, lam)), lambda_modulus=wlam, Da_minus_lambda_modulus=wadj,
        rho4_rational=str(rho4), rho5_rational=str(rho5), rho_star_rational=str(min(rho4, rho5)),
        selected_error_equations=[i for i, x in ((4, rho4), (5, rho5)) if x == min(rho4, rho5)])
    return witness, dict(a0=center['a'], lam=lam, p0=p0, rho=min(rho4, rho5), UP=UP)


def update_branch(old, UPold, UPnew, parameters, centers, counts, cell=False):
    """Recombine inherited witnesses; never invoke a scalar gain routine."""
    nu = old['nu']
    bounds = [parameters['kappa'], parameters['Ia'], parameters['Is']]
    if not nu:
        bounds.append(parameters['Q'])
    expected = list(product((0, 1), repeat=len(bounds)))
    assert [v['endpoint_bits'] for v in old['vertices']] == [list(x) for x in expected]
    shift = UPnew-UPold
    assert shift <= 0
    trial = F(old['trial_upper_rational'])
    result = dict(nu=nu, source_branch_canonical_sha256=canonical_sha(old),
        old_trial_upper_rational=str(trial), UP_change_rational=str(shift),
        new_trial_upper_rational=str(trial+shift), vertices=[])
    old_totals, new_totals = [], []
    for vertex, bits in zip(old['vertices'], expected):
        vals = [bound[bit] for bound, bit in zip(bounds, bits)]
        assert list(map(F, vertex['parameters_rational'])) == vals
        k, ia, iss = vals[:3]
        forces = k*(1-iss), k*(F(3, 2)*ia-iss-F(1, 2))+(vals[3]/2 if not nu else 0)
        assert tuple(map(F, vertex['forces_rational'])) == forces
        gain_sum, gains = F(0), {}
        for name, force, target, K in zip(('s', 'a'), forces,
                ((F('.22'), F('.5')), (F('.22'), F('.45'))),
                (F(88, 5), F((1+nu)*49, 10))):
            gain = vertex['gains'][name]
            assert iv(gain['force']) == (force, force)
            assert iv(gain['center']) == centers[name]
            assert iv(gain['target']) == target and F(gain['K_rational']) == K
            upper = max(F(0), *(iv(b['value'])[1] for b in gain['branches']))
            assert upper == F(gain['upper_rational'])
            if cell:
                assert F(vertex['independent_gain_checks'][name]['upper_rational']) == upper
            gains[name] = dict(source_witness_canonical_sha256=canonical_sha(gain),
                unchanged_force_rational=str(force), unchanged_center=rec(centers[name]),
                unchanged_target=rec(target), K_rational=str(K), upper_rational=str(upper))
            gain_sum += upper
            counts['saved_gain_witness_recombinations'] += 1
        assert gain_sum == F(vertex['gain_sum_upper_rational'])
        total = trial+gain_sum
        assert total == F(vertex['plane_upper_rational'])
        old_totals.append(total)
        new_totals.append(total+shift)
        result['vertices'].append(dict(endpoint_bits=list(bits), parameters_rational=list(map(str, vals)),
            source_vertex_canonical_sha256=canonical_sha(vertex), gains=gains,
            unchanged_gain_sum_rational=str(gain_sum), old_plane_upper_rational=str(total),
            new_plane_upper_rational=str(total+shift)))
        counts['saved_vertex_recombinations'] += 1
    key = 'cell_plane_upper_rational' if cell else 'uniform_plane_upper_rational'
    assert max(old_totals) == F(old[key])
    assert old['attaining_vertices'] == [list(b) for b, v in zip(expected, old_totals) if v == max(old_totals)]
    result.update(old_plane_upper_rational=str(max(old_totals)),
        new_plane_upper_rational=str(max(new_totals)),
        attaining_vertices=[list(b) for b, v in zip(expected, new_totals) if v == max(new_totals)])
    assert max(new_totals) <= max(old_totals)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    if not str(args.output).endswith('.json.gz'):
        raise ValueError('a fresh deterministic .json.gz output is required')
    if hasattr(sys, 'set_int_max_str_digits'):
        sys.set_int_max_str_digits(0)
    assert PINNED
    inputs = dict(PINNED)
    own = Path(__file__).resolve().relative_to(ROOT).as_posix()
    inputs[own] = sha(ROOT/own)
    counts = dict(cases=0, completed_cells=0, quadratic_endpoint_maximizations=0,
        saved_vertex_recombinations=0, saved_gain_witness_recombinations=0,
        cell_family_branch_comparisons=0, uniform_family_branch_summaries=0,
        gain_calls=0, analytic_calls=0, roots=0, source_evaluations=0,
        subdivisions=0, retries=0)
    out = dict(status='initializing', proof_path=PROOF, checker_path=own, input_sha256=inputs,
        counts=counts, cases=[], pending_cells=[], all_updated_bounds_enclosed=False,
        complete_terminal_kernel_proved=False, knot_theorem_proved=False,
        source_scope='canonical actual K4; phase planes on D4; full original targets',
        old_private_left_plane_outcomes_retained=True)
    active, fatal = None, None
    try:
        def bind(name, digest):
            assert isinstance(digest, str) and len(digest) == 64
            assert name not in inputs or inputs[name] == digest
            assert sha(ROOT/name) == digest, name
            inputs[name] = digest
        for name, digest in list(inputs.items()):
            bind(name, digest)
        data = {p: load(ROOT/p) for p in
            (PLANE, CELLS, FACES, REFINED, POSTERIOR, SPLIT, AFFINE, INTEGRAL, PRIVATE)}
        for d in data.values():
            assert d.get('changed_inputs', []) == []
            for key in ('input_sha256', 'dependencies_sha256', 'dependencies'):
                if isinstance(d.get(key), dict):
                    for name, digest in d[key].items():
                        bind(name, digest)
        plane, cells, faces, refined, posterior, split, affine, integral, private = (
            data[p] for p in (PLANE, CELLS, FACES, REFINED, POSTERIOR, SPLIT, AFFINE, INTEGRAL, PRIVATE))
        assert plane['status'] == cells['status'] == refined['status'] == 'completed fixed saved-only protocol'
        assert posterior['status'] == 'passed'
        assert split['status'] == 'completed fixed saved-only protocol'
        assert affine['status'] == 'completed fixed protocol'
        assert plane['uniform_plane_ceilings_proved'] is True
        assert cells['uniform_cellwise_plane_ceilings_proved'] is True and cells['pending_cells'] == []
        assert cells['counts']['completed_cells'] == cells['counts']['enclosed_cells'] == 70
        assert cells['counts']['source_null_comparisons'] == cells['counts']['no_reference_cells'] == 0
        assert cells['counts']['scalar_cubic_gains'] == cells['counts']['independent_gain_checks'] == 3360
        assert faces['status'] == 'completed fixed saved-only extraction' and faces['all_uniform_bare_bounds_defined']
        assert integral['status'] == 'completed fixed protocol' and integral['all_four_budgets_enclosed']
        assert private['status'] == 'passed' and private['rational_barrier_witnesses_verified']
        assert F(private['scoped_raw_face_gap_rational']) == F(51, 20000)
        assert refined['source_path'] == POSTERIOR and refined['source_sha256'] == inputs[POSTERIOR]
        assert posterior['source_path'] == SPLIT and posterior['source_sha256'] == inputs[SPLIT]
        assert split['source_path'] == AFFINE and split['source_sha256'] == inputs[AFFINE]
        assert cells['plane_sha256'] == inputs[PLANE] and cells['faces_sha256'] == inputs[FACES]
        assert cells['refinement_sha256'] == inputs[REFINED]
        assert plane['source_sha256'] == inputs[INTEGRAL]
        assert [(c['beta'], c['epsilon']) for c in plane['cases']] == [(1, 0), (1, 1)]
        assert [(c['beta'], c['epsilon']) for c in cells['cases']] == [(1, 0), (1, 1)]
        for eps, face in enumerate(faces['cases'][2:]):
            assert (face['beta'], face['epsilon']) == (1, eps)
            out['pending_cells'].extend(dict(epsilon=eps, original_cell_index=c['index'])
                for c in face['intersecting_original_cells'])
        assert len(out['pending_cells']) == 70
        pi = iv(integral['constants']['pi'])
        assert F(157, 50) < pi[0] <= pi[1] < F(22, 7)
        for eps in (0, 1):
            p, oldcells, face, new, prior, sp, aff, original = (
                plane['cases'][eps], cells['cases'][eps], faces['cases'][2+eps],
                refined['cases'][2+eps], posterior['posterior_enclosures'][2+eps],
                split['cases'][2+eps], affine['cases'][2+eps], integral['cases'][eps])
            assert all((x['beta'], x['epsilon']) == (1, eps)
                for x in (p, oldcells, face, new, prior, sp, aff, original))
            assert new['source_posterior_canonical_sha256'] == canonical_sha(prior)
            assert prior['source_case_canonical_sha256'] == canonical_sha(sp)
            assert sp['source_case_canonical_sha256'] == canonical_sha(aff)
            assert new['affine_case_canonical_sha256'] == canonical_sha(aff)
            assert oldcells['plane_case_canonical_sha256'] == canonical_sha(p)
            assert oldcells['face_case_canonical_sha256'] == canonical_sha(face)
            assert oldcells['refinement_case_canonical_sha256'] == p['refinement_case_canonical_sha256'] == canonical_sha(new)
            assert oldcells['original_integral_case_canonical_sha256'] == p['source_case_canonical_sha256'] == canonical_sha(original)
            assert face['refinement_case_canonical_sha256'] == canonical_sha(new)
            assert new['exact_linear_system_verified'] and prior['exact_linear_system_verified']
            assert all(original['domain_guards'].values())
            assert sp['family_certified'] is True
            for key in ('center_exact', 'response_exact', 'parameter_center', 'parameter_radius_rational'):
                assert new[key] == prior[key] == original[key]
            assert new['center_exact'] == aff['center'] and new['response_exact'] == aff['response_exact']
            assert p['center_exact'] == new['center_exact'] and p['response_exact'] == new['response_exact']
            assert p['posterior_radii_rational'] == new['posterior_radii_rational']
            assert tuple(map(F, new['parameter_center'])) == (F('.30'), -F('.052'))
            assert F(new['parameter_radius_rational']) == R
            assert all(0 <= F(x) <= F(y) for x, y in
                zip(new['posterior_radii_rational'], prior['posterior_radii_rational']))
            candidate = next(c for c in aff['candidates'] if F(c['multiplier_rational']) == 1)
            scandidate = next(c for c in sp['candidates'] if F(c['multiplier_rational']) == 1)
            assert prior['source_candidate_canonical_sha256'] == canonical_sha(scandidate)
            assert scandidate['source_candidate_canonical_sha256'] == canonical_sha(candidate)
            assert scandidate['criterion_pass'] is True
            assert scandidate['status'] == 'uniform original canonical enclosure certified'
            assert candidate['criterion_verified'] is True and candidate['saved_central_root_contained'] is True
            assert candidate['all_full_original_log_disks_regular'] is True
            marginal, values = terminal_marginal(aff, new, candidate, pi)
            oldUP = F(p['marginal']['UP_upper_rational'])
            bestUP = min(oldUP, values['UP'])
            row = dict(beta=1, epsilon=eps, status='initializing',
                old_plane_case_canonical_sha256=canonical_sha(p),
                old_cell_case_canonical_sha256=canonical_sha(oldcells),
                refinement_case_canonical_sha256=canonical_sha(new),
                affine_case_canonical_sha256=canonical_sha(aff),
                terminal_marginal=marginal, old_global_UP_rational=str(oldUP),
                new_global_UP_rational=str(values['UP']), best_global_UP_rational=str(bestUP),
                global_UP_minimizers=[name for name, v in (('old', oldUP), ('terminal', values['UP'])) if v == bestUP],
                global_branches=[], cells=[], families=[],
                inherited_coverage=oldcells['coverage'],
                independent_private_left_raw_gap_rational='51/20000' if eps else None)
            out['cases'].append(row)
            counts['cases'] += 1
            pv = p['plane_value']
            assert iv(pv['pi']) == pi
            parameters = {key: iv(pv[key]) for key in ('kappa', 'Ia', 'Is', 'Q')}
            centers = {name: iv(new['coordinate_enclosures'][name]['real']) for name in ('s', 'a')}
            assert [b['nu'] for b in p['branches']] == [1, 0]
            for b in p['branches']:
                extra = -pi[0]*H if b['nu'] else F(pv['old_GH_upper_rational'])/2
                assert F(b['trial_upper_rational']) == oldUP+iv(pv['WP'])[1]+extra
                row['global_branches'].append(update_branch(b, oldUP, bestUP, parameters, centers, counts))
            assert oldcells['coverage']['exact_full_image_coverage'] is True
            originals = face['intersecting_original_cells']
            assert len(originals) == len(oldcells['cells']) == (45 if eps == 0 else 25)
            expected_families = ([('three_mixed', i) for i in range(8)]+[('three_half', 0)] if not eps
                                 else [('four', i) for i in range(8)]+[('four', 20)])
            assert [(f['series'], f['family']) for f in face['families']] == expected_families
            facejobs = {}
            for f in face['families']:
                assert f['complete_finite_coverage'] and not f['null_jobs_unresolved']
                for job in f['contributing_jobs']:
                    facejobs[(job['original_cell_index'], f['series'], f['family'])] = job
            for oldc, original_cell in zip(oldcells['cells'], originals):
                assert oldc['original_cell'] == original_cell
                assert oldc['original_cell_canonical_sha256'] == canonical_sha(original_cell)
                assert oldc['status'] == 'enclosed both joined-plane alternatives'
                A, c = tuple(map(F, original_cell['intersection'][0])), tuple(map(F, original_cell['intersection'][1]))
                assert A == iv(oldc['reference_A_interval']) and c == iv(oldc['reference_c_interval'])
                assert A[0] <= A[1] and c[0] <= c[1] < H
                active = dict(original_cell=original_cell,
                    source_cell_canonical_sha256=canonical_sha(oldc), status='initializing',
                    quadratic_endpoint_maximizations=[], branches=[], family_comparisons=[])
                row['cells'].append(active)
                polys = [quadratic(x, c, values['a0'], values['lam'], values['p0']) for x in A]
                counts['quadratic_endpoint_maximizations'] += 2
                terminalUP = max(x[0] for x in polys)+(H-c[0])*values['rho']
                oldcellUP = F(oldc['UP_upper_rational'])
                best = min(oldcellUP, terminalUP)
                active.update(
                    quadratic_endpoint_maximizations=[x[1] for x in polys],
                    marginal_error_rational=str((H-c[0])*values['rho']),
                    old_UP_rational=str(oldcellUP), terminal_UP_rational=str(terminalUP), best_UP_rational=str(best),
                    UP_minimizers=[name for name, v in (('old', oldcellUP), ('terminal', terminalUP)) if v == best],
                    unchanged_plane_values=oldc['plane_values'], unchanged_s_center=oldc['s_real_intersection_endpoints_rational'])
                parameters = dict(kappa=iv(oldc['plane_values']['kappa']),
                    Ia=iv(oldcells['shared_data']['Ia']), Is=iv(oldcells['shared_data']['Is']),
                    Q=iv(oldc['plane_values']['Q']))
                centers = dict(s=tuple(map(F, oldc['s_real_intersection_endpoints_rational'])), a=A)
                assert centers['s'][0] <= centers['s'][1]
                assert [b['nu'] for b in oldc['branches']] == [1, 0]
                for b in oldc['branches']:
                    cpv = oldc['plane_values']
                    extra = -pi[0]*H if b['nu'] else F(cpv['GH_cell_upper_rational'])/2
                    assert F(b['trial_upper_rational']) == oldcellUP+iv(cpv['WP'])[1]+extra
                    trial_key = 'factorial_trial_upper_rational' if b['nu'] else 'forced_trial_upper_rational'
                    assert F(cpv[trial_key]) == F(b['trial_upper_rational'])
                    active['branches'].append(update_branch(b, oldcellUP, best, parameters, centers, counts, cell=True))
                assert [(j['series'], j['family']) for j in oldc['source_jobs']] == expected_families
                assert len(oldc['family_comparisons']) == 18
                for job in oldc['source_jobs']:
                    key = (original_cell['index'], job['series'], job['family'])
                    savedjob = facejobs[key]
                    for name, value in savedjob.items():
                        assert job[name] == value
                    assert job['decoded_upper_rational'] is not None
                    src = F(job['decoded_upper_rational'])
                    for branch in active['branches']:
                        nu = branch['nu']
                        oldcomp = next(x for x in oldc['family_comparisons']
                            if (x['series'], x['family'], x['nu']) == (job['series'], job['family'], nu))
                        assert oldcomp['status'] == 'enclosed'
                        assert oldcomp['job'] == job['job']
                        assert F(oldcomp['source_upper_rational']) == src
                        assert F(oldcomp['joined_upper_rational']) == F(branch['old_plane_upper_rational'])+src
                        joined = F(branch['new_plane_upper_rational'])+src
                        active['family_comparisons'].append(dict(series=job['series'], family=job['family'],
                            job=job['job'], nu=nu, source_upper_rational=str(src),
                            old_comparison_canonical_sha256=canonical_sha(oldcomp),
                            old_joined_upper_rational=oldcomp['joined_upper_rational'],
                            new_joined_upper_rational=str(joined), strictly_negative=joined < 0,
                            gap_rational=str(-joined)))
                        counts['cell_family_branch_comparisons'] += 1
                active['status'] = 'completed unchanged-gain update'
                counts['completed_cells'] += 1
                out['pending_cells'].remove(dict(epsilon=eps, original_cell_index=original_cell['index']))
                active = None
                if counts['completed_cells'] % 10 == 0:
                    print(json.dumps(dict(completed_cells=counts['completed_cells'], pending=len(out['pending_cells']))), flush=True)
            for family in face['families']:
                summary = dict(series=family['series'], family=family['family'], branches=[])
                for nu in (1, 0):
                    values_joined = [(c['original_cell']['index'], x) for c in row['cells'] for x in c['family_comparisons']
                        if (x['series'], x['family'], x['nu']) == (family['series'], family['family'], nu)]
                    assert len(values_joined) == len(originals)
                    cellupper = max(F(x['new_joined_upper_rational']) for _, x in values_joined)
                    globalbranch = next(x for x in row['global_branches'] if x['nu'] == nu)
                    globalupper = F(globalbranch['new_plane_upper_rational'])+F(family['uniform_bare_upper_rational'])
                    best = min(cellupper, globalupper)
                    summary['branches'].append(dict(nu=nu, updated_global_joined_upper_rational=str(globalupper),
                        updated_cellwise_joined_upper_rational=str(cellupper),
                        best_complete_upper_rational=str(best), strictly_negative=best < 0,
                        gap_rational=str(-best), selected_routes=[k for k, v in
                            (('global', globalupper), ('cellwise', cellupper)) if v == best],
                        attaining_cells=[i for i, x in values_joined if F(x['new_joined_upper_rational']) == cellupper]))
                    counts['uniform_family_branch_summaries'] += 1
                row['families'].append(summary)
            row['status'] = 'completed both whole-family and all original-cell updates'
        assert counts['cases'] == 2 and counts['completed_cells'] == 70 and not out['pending_cells']
        assert counts['quadratic_endpoint_maximizations'] == 140
        assert counts['saved_vertex_recombinations'] == 1728 and counts['saved_gain_witness_recombinations'] == 3456
        assert counts['cell_family_branch_comparisons'] == 1260 and counts['uniform_family_branch_summaries'] == 36
        out['all_updated_bounds_enclosed'] = True
        out['status'] = 'completed fixed saved-only protocol'
    except (Exception, KeyboardInterrupt) as exc:
        fatal = exc
        out['status'] = 'failed saved-only protocol'
        out['error'] = dict(type=type(exc).__name__, message=str(exc))
        if active is not None:
            active['status'] = 'failed saved-only protocol'
            active['error'] = out['error']
    out['changed_inputs'] = [p for p, h in inputs.items() if not (ROOT/p).is_file() or sha(ROOT/p) != h]
    if out['changed_inputs']:
        out['status'] = 'changed inputs'
        out['all_updated_bounds_enclosed'] = False
    out['proof_sha256'], out['checker_sha256'] = inputs[PROOF], inputs[own]
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open('xb') as raw:
        with gzip.GzipFile(filename='', fileobj=raw, mode='wb', compresslevel=1, mtime=0) as gz:
            with io.TextIOWrapper(gz, encoding='utf-8', newline='\n') as stream:
                json.dump(out, stream, separators=(',', ':'))
                stream.write('\n')
    print(json.dumps(dict(status=out['status'], counts=counts, output_sha256=sha(args.output))), flush=True)
    if fatal is not None:
        raise fatal
    if out['changed_inputs']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
