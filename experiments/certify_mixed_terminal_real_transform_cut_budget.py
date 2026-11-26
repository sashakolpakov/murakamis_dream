#!/usr/bin/env python3
"""Fixed two-case direct-cut budget: 34 cot, 4 sine, 2 log enclosures.

No roots, private primitives, source replay, parameter grid or retry.
"""
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import importlib.util
import io
from itertools import product
import json
from math import isqrt
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
PROOF = 'notes/research_mixed_terminal_real_transform_cut_protocol.md'
THEORY = 'notes/research_mixed_terminal_real_transform_cut_budget.md'
SOURCE = 'repro/results/research-mixed-terminal-four-input-integral-budget.json'
AUDIT = 'repro/results/research-mixed-terminal-four-input-integral-budget-saved-audit.json'
GAIN = 'experiments/certify_mixed_terminal_four_input_integral_budget.py'
GAIN_CHECKER = 'experiments/check_mixed_terminal_four_input_integral_budget.py'
REFINED = 'repro/results/research-mixed-terminal-quadratic-residual-refinement.json'
POSTERIOR = 'repro/results/research-mixed-terminal-split-taylor-completion.json'
SPLIT = 'repro/results/research-mixed-terminal-split-taylor-inclusion.json'
AFFINE = 'repro/results/research-mixed-terminal-correlated-affine-family.json'
FACES = 'repro/results/research-mixed-terminal-uniform-face-reserves.json'
PINNED = {
    'notes/research_mixed_terminal_real_transform_cut_protocol.md': '551233df01752ed8c8d333dd2c6d45cb09b60a391dba9d9d09af7a20ca7264eb',
    'notes/research_mixed_terminal_real_transform_cut_budget.md': 'ee4ba95733040b87abf9a4f956f076444f505f1ba2502e684cbe2c9dd37ecf92',
    'repro/results/research-mixed-terminal-four-input-integral-budget.json': '9831e8bdbc884cfc0b0c99dbc7f92245403988ae7dc4bbbba86b5606c5a1575e',
    'repro/results/research-mixed-terminal-four-input-integral-budget-saved-audit.json': 'cda9eef92856387d0ec0dccca6311512bb980034a07832ab89a99a7bc733d6c3',
    'experiments/certify_mixed_terminal_four_input_integral_budget.py': '3b806591d88cd461ab7764a6f9c704a048d9c33edb88834a32dbc59a99c91388',
    'experiments/check_mixed_terminal_four_input_integral_budget.py': 'd38f41d186bf31d3255861c45cb0500d1a21a4eb1bfd4d366c6a956efc614bf4',
    'repro/results/research-mixed-terminal-quadratic-residual-refinement.json': '2834576c2a443c9ffd24032277b5f253d9a85eac17d3f754905812e822a9a331',
    'repro/results/research-mixed-terminal-split-taylor-completion.json': 'e04521450e1973658cbd602aa0a8f54d4c7d40c968b4b90d65374d570981c617',
    'repro/results/research-mixed-terminal-split-taylor-inclusion.json': 'a25587e526dc753306eb690b76f1f07d0d05410be315c6675023bd87ae42e202',
    'repro/results/research-mixed-terminal-correlated-affine-family.json': '51b702aa6ea44aa5891bc1146a7d5c0d22686cd814f9bbe5d9c4c63b9a16f9e1',
    'repro/results/research-mixed-terminal-uniform-face-reserves.json': '37fc3676a9919525e16b214db0fedebd3e13b980150f5f01ec0d0b28141a07d3',
    'notes/research_mixed_terminal_uniform_face_reserves.md': 'b770a8d3c182c9936367c1f43edd2e74f483ffd5ead2d61fa44b85420109a363',
    'experiments/check_mixed_terminal_uniform_face_reserves.py': 'b631f8d2b23acab944fc8ab900c2a6dfcacd9da1922643f58919d4185ebb7a6d',
    'notes/research_mixed_terminal_quadratic_residual_refinement.md': 'f012610187e14b824fdfeea730bc71ffde1660687ffbdcc491bc945c6a54d596',
    'experiments/check_mixed_terminal_quadratic_residual_refinement.py': '251fc4b3c656201ab5451287577baddb4d4be8122ff34a1318078de0f8501a05',
    'notes/research_mixed_terminal_all_input_affine_enclosures.md': '6412be85ca87c01a0b363191c724dc1e7357c00939ce5c379a7c501f3565215f',
    'notes/research_mixed_terminal_canonical_source_domain.md': 'd50929a1a1c02d034feb5ca5f9ebf6e6da70bd6b0a1eb4a67f67fd1108d18d11',
    'notes/research_mixed_terminal_symmetric_pair_costs.md': 'b4ee1a7bdde317edab0210b20cb8616913984c4f992d1cbed240f6092a8e593f',
    'notes/research_mixed_terminal_cubic_cost_and_response_bounds.md': 'dfc3f415e742aa9c632707aea7c699bb2ccbdc054c08fc7ba640e943bcdaa741',
    'notes/research_mixed_terminal_full_input_index_barrier.md': '45ae03bf28a78df930fc8e7c97054ca40689630423a4d36c0009b6b0bb900ee2',
    'notes/research_mixed_terminal_joint_main_budget.md': '5c3e23f070d27628b3843030cd4bced887fcc7e76e25b15ed8d73a6816369baa',
    'notes/research_mixed_terminal_concave_profile_envelope.md': '6d71c0470a9fe1598cdc46459ffcda98f807eb84c1be8bc2810517706a744ddd',
    'notes/research_mixed_terminal_four_input_integral_budget.md': '90ec6c9d4b3641a01e789b64dd0d26053b402c2914b99cafe81eff8ad4265cb9',
    'notes/research_mixed_terminal_shared_force_vertices.md': '2134390846790b38b6e6451a010d0660e0b7f21fb913739a339173a9771b4a78',
    'notes/research_mixed_terminal_terminal_side_marginal_enclosure.md': 'ef21f881e158a39f46d645ec5b639c7b0a01d122b67b2f0b6c1b082798c731b7',
}
NAMES = ('e', 'xi', 't', 'a', 's')
H, RADIUS = F(1, 100), F(8, 125)
PARAMETER_CENTER = (F('.30'), -F('.052'))
PRECISION, MESH_BITS = 256, 256
ZERO = (F(0), F(0))
LIMITS = dict(center_cotangents=2, slab_cotangents=32,
              center_complex_sines=2, curvature_real_sines=2, center_logarithms=2)


def sha(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1048576), b''):
            h.update(block)
    return h.hexdigest()


def canonical_sha(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True,
        separators=(',', ':')).encode()).hexdigest()


def iv(v):
    if 'finite' in v:
        assert v['finite'] is True
    result = F(v['lower_rational']), F(v['upper_rational'])
    assert result[0] <= result[1]
    return result


def rec(v): return dict(finite=True, lower_rational=str(v[0]), upper_rational=str(v[1]))
def cv(v): return iv(v['real']), iv(v['imag'])
def cr(v): return dict(real=rec(v[0]), imag=rec(v[1]))
def ex(v): return F(v), F(v)
def cx(v): return ex(v[0]), ex(v[1])
def add(x, y): return x[0]+y[0], x[1]+y[1]
def neg(x): return -x[1], -x[0]
def sub(x, y): return add(x, neg(y))
def mul(x, y):
    candidates = [a*b for a in x for b in y]
    return min(candidates), max(candidates)
def sc(x, a): return mul(x, ex(a))
def ca(x, y): return add(x[0], y[0]), add(x[1], y[1])
def csub(x, y): return sub(x[0], y[0]), sub(x[1], y[1])
def cs(x, a): return sc(x[0], a), sc(x[1], a)
def cm(x, y):
    return sub(mul(x[0], y[0]), mul(x[1], y[1])), add(mul(x[0], y[1]), mul(x[1], y[0]))
def contains(outer, inner): return outer[0] <= inner[0] <= inner[1] <= outer[1]


def norm(z):
    squared = sum(max(abs(lo), abs(hi))**2 for lo, hi in z)
    mesh = 1 << MESH_BITS
    n = isqrt((squared.numerator*mesh*mesh)//squared.denominator)
    low = F(n, mesh)
    high = low if low*low == squared else F(n+1, mesh)
    assert 0 <= low <= high and low*low <= squared <= high*high
    return high, dict(rectangle=cr(z), squared_radius_rational=str(squared),
        sqrt_interval=rec((low, high)), mesh_bits=MESH_BITS)


def forbidden(*args, **kwargs):
    raise AssertionError('forbidden original evaluator/checker entry point')


def verify_case(old, saved, new, prior, splitcase, aff, face, epsilon):
    for value in (old, saved, new, prior, splitcase, aff, face):
        assert (value['beta'], value['epsilon']) == (1, epsilon)
    assert old['source_entry_canonical_sha256'] == canonical_sha(prior)
    assert new['source_posterior_canonical_sha256'] == canonical_sha(prior)
    assert prior['source_case_canonical_sha256'] == canonical_sha(splitcase)
    assert splitcase['source_case_canonical_sha256'] == canonical_sha(aff)
    assert new['affine_case_canonical_sha256'] == canonical_sha(aff)
    assert face['refinement_case_canonical_sha256'] == canonical_sha(new)
    assert face['source_posterior_canonical_sha256'] == canonical_sha(prior)
    assert prior['exact_linear_system_verified'] is True and new['exact_linear_system_verified'] is True
    assert splitcase['family_certified'] is True
    for key in ('center_exact', 'response_exact', 'parameter_center', 'parameter_radius_rational'):
        assert new[key] == prior[key] == old[key]
    assert new['center_exact'] == splitcase['original_center'] == aff['center']
    assert new['response_exact'] == splitcase['original_response'] == aff['response_exact']
    assert tuple(map(F, new['parameter_center'])) == PARAMETER_CENTER
    assert F(new['parameter_radius_rational']) == RADIUS
    assert all(0 <= F(a) <= F(b) for a, b in
        zip(new['posterior_radii_rational'], prior['posterior_radii_rational']))
    assert all(old['domain_guards'].values())
    for name in NAMES:
        for part in ('real', 'imag'):
            assert contains(iv(old['individual_supports'][name][part]),
                            iv(new['coordinate_enclosures'][name][part]))
    splitcandidates = [c for c in splitcase['candidates'] if F(c['multiplier_rational']) == 1]
    candidates = [c for c in aff['candidates'] if F(c['multiplier_rational']) == 1]
    assert len(splitcandidates) == len(candidates) == 1
    splitcandidate, candidate = splitcandidates[0], candidates[0]
    assert prior['source_candidate_canonical_sha256'] == canonical_sha(splitcandidate)
    assert splitcandidate['source_candidate_canonical_sha256'] == canonical_sha(candidate)
    assert splitcandidate['criterion_pass'] is True
    assert candidate['criterion_verified'] is True
    assert candidate['saved_central_root_contained'] is True
    assert candidate['all_full_original_log_disks_regular'] is True
    assert face['all_nine_uniform_bare_bounds_defined'] is True
    a = new['coordinate_enclosures']['a']
    assert list(map(F, face['physical_a_box_rational'][0])) == list(iv(a['real']))
    assert list(map(F, face['physical_a_box_rational'][1])) == list(iv(a['imag']))
    return candidate


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    if not str(args.output).endswith('.json.gz'):
        raise ValueError('a fresh .json.gz output is required')
    if hasattr(sys, 'set_int_max_str_digits'):
        sys.set_int_max_str_digits(0)
    assert PINNED
    inputs = dict(PINNED)
    own = Path(__file__).resolve().relative_to(ROOT).as_posix()
    inputs[own] = sha(ROOT/own)
    counts = dict(cases=0, completed_cases=0, height_slabs=0,
        center_cotangents=0, slab_cotangents=0, center_complex_sines=0,
        curvature_real_sines=0, center_logarithms=0, vertices=0,
        scalar_cubic_gains=0, independent_gain_checks=0, source_comparisons=0,
        new_pi_evaluations=0, private_actions=0, dilogarithms=0,
        roots=0, source_evaluations=0, subdivisions=0, retries=0)
    out = dict(status='initializing', proof_path=PROOF, theory_path=THEORY,
        driver_path=own, input_sha256=inputs, precision_bits=PRECISION,
        selected_height_rational=str(H), counts=counts, cases=[],
        pending_cases=[dict(beta=1, epsilon=0, tau_rational='1/2'),
                       dict(beta=1, epsilon=1, tau_rational='3/20')],
        all_six_comparisons_enclosed=False, all_six_signs_proved=False,
        complete_terminal_kernel_proved=False, knot_theorem_proved=False,
        phase_scope='whole D4 canonical family; original independent full-P targets',
        source_scope='actual K4, with original oriented and inverse-feasible hypotheses')
    fatal, active = None, None
    try:
        def bind(name, digest):
            assert isinstance(digest, str) and len(digest) == 64
            assert name not in inputs or inputs[name] == digest, name
            assert sha(ROOT/name) == digest, name
            inputs[name] = digest
        for name, digest in list(inputs.items()):
            bind(name, digest)
        paths = (SOURCE, AUDIT, REFINED, POSTERIOR, SPLIT, AFFINE, FACES)
        data = {p: json.loads((ROOT/p).read_text()) for p in paths}
        for record in data.values():
            assert record.get('changed_inputs', []) == []
            for key in ('input_sha256', 'dependencies_sha256', 'dependencies'):
                if isinstance(record.get(key), dict):
                    for name, digest in record[key].items():
                        bind(name, digest)
        source, audit, refined, posterior, split, affine, faces = (data[p] for p in paths)
        assert source['status'] == 'completed fixed protocol' and source['all_four_budgets_enclosed']
        assert audit['status'] == 'passed' and audit['source_path'] == SOURCE
        assert audit['source_sha256'] == inputs[SOURCE] and audit['checker_sha256'] == inputs[GAIN_CHECKER]
        assert audit['verified_cotangent_boxes'] == 96 and audit['verified_theta_slabs'] == 32
        assert refined['status'] == 'completed fixed saved-only protocol'
        assert refined['source_path'] == POSTERIOR and refined['source_sha256'] == inputs[POSTERIOR]
        assert posterior['status'] == 'passed' and posterior['all_four_input_disks_certified']
        assert posterior['source_path'] == SPLIT and posterior['source_sha256'] == inputs[SPLIT]
        assert split['status'] == 'completed fixed saved-only protocol'
        assert split['all_four_input_families_certified'] and split['source_path'] == AFFINE
        assert split['source_sha256'] == inputs[AFFINE]
        assert affine['status'] == 'completed fixed protocol'
        assert faces['status'] == 'completed fixed saved-only extraction'
        assert faces['all_uniform_bare_bounds_defined'] and not faces['unresolved_family_cases']
        pi_bounds = iv(source['constants']['pi'])
        assert F(157, 50) < pi_bounds[0] <= pi_bounds[1] < F(22, 7)
        out['constants'] = dict(pi=rec(pi_bounds), pi_source_sha256=inputs[SOURCE])
        # Imported modules have only stdlib definitions at module scope. Only the
        # exact gain and independent witness checker are permitted below.
        modules = []
        for label, path in (('fixed_direct_cut_gain', GAIN), ('fixed_direct_cut_gain_check', GAIN_CHECKER)):
            spec = importlib.util.spec_from_file_location(label, ROOT/path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            module.main = forbidden
            modules.append(module)
        gain_module, check_module = modules

        # No elementary library is imported until all saved input hashes pass.
        from flint import arb, acb, ctx
        ctx.prec = PRECISION

        def ar(value):
            value = F(value)
            return arb(value.numerator)/arb(value.denominator)

        def ends(value):
            if not value.is_finite():
                raise ArithmeticError('nonfinite elementary interval')
            return F(str(value.lower().fmpq())), F(str(value.upper().fmpq()))

        def ball(value):
            lo, hi = value
            assert lo <= hi
            result = arb(ar((lo+hi)/2), ar((hi-lo)/2).upper())
            assert contains(ends(result), value), 'outward ball conversion failed'
            return result

        def cc(value):
            return acb(ball(value[0]), ball(value[1]))

        def elementary(kind, value):
            counts[kind] += 1
            assert counts[kind] <= LIMITS[kind]
            method = 'cot' if 'cotangent' in kind else 'sin' if 'sine' in kind else 'log'
            result = getattr(value, method)()
            if not result.is_finite():
                raise ArithmeticError('nonfinite '+kind)
            return result

        def complex_record(value):
            return cr((ends(value.real), ends(value.imag)))

        pi = ball(pi_bounds)
        out['constants']['outward_reconstructed_pi'] = rec(ends(pi))
        for epsilon, tau, sigma in ((0, F(1, 2), F(5, 3)), (1, F(3, 20), F(3, 5))):
            old, saved, new, prior, sp, aff, face = (
                source['cases'][epsilon], audit['cases'][epsilon], refined['cases'][2+epsilon],
                posterior['posterior_enclosures'][2+epsilon], split['cases'][2+epsilon],
                affine['cases'][2+epsilon], faces['cases'][2+epsilon])
            active = dict(beta=1, epsilon=epsilon, tau_rational=str(tau), sigma_rational=str(sigma),
                status='initializing', source_case_canonical_sha256=canonical_sha(old),
                audit_case_canonical_sha256=canonical_sha(saved),
                refinement_case_canonical_sha256=canonical_sha(new),
                affine_case_canonical_sha256=canonical_sha(aff),
                face_case_canonical_sha256=canonical_sha(face), slabs=[], branches=[], comparisons=[])
            out['cases'].append(active)
            counts['cases'] += 1
            candidate = verify_case(old, saved, new, prior, sp, aff, face, epsilon)
            active['inherited_domain_guards'] = old['domain_guards']
            active['center_exact'], active['response_exact'] = new['center_exact'], new['response_exact']
            active['posterior_radii_rational'] = new['posterior_radii_rational']
            active['coordinate_enclosures'] = new['coordinate_enclosures']
            center = dict(zip(NAMES, [tuple(map(F, z)) for z in new['center_exact']]))
            response = dict(zip(NAMES, [tuple(map(F, z)) for z in new['response_exact']]))
            errors = dict(zip(NAMES, map(F, new['posterior_radii_rational'])))
            ua, ut = response['a'], response['t']
            uta = tuple(ua[j]+ut[j] for j in range(2))
            nua, wua = norm(cx(ua))
            nuta, wuta = norm(cx(uta))
            wa, wta = RADIUS*nua+errors['a'], RADIUS*nuta+errors['a']+errors['t']
            a0, t0 = center['a'], center['t']
            cut0 = a0[0]+tau, a0[1]
            ta0 = a0[0]+t0[0], a0[1]+t0[1]
            distance = min(cut0[0]-wa, 1-cut0[0]-wa)
            assert 0 < distance <= F(1, 2)
            active['new_cut_disk'] = dict(center_exact=list(map(str, cut0)),
                radius_rational=str(wa), strip_distance_rational=str(distance),
                real_interval=rec((cut0[0]-wa, cut0[0]+wa)), ua_modulus=wua)
            terms = {term['name']: term for term in aff['primitive_terms']}
            full = {term['name']: term['full_curvature'] for term in candidate['full_primitive_terms']}
            oldta, disk = terms['t+a'], full['t+a']
            assert tuple(map(F, oldta['center_exact'])) == tuple(map(F, disk['center_exact'])) == ta0
            assert disk['regular'] is True and disk['stage'] == 'full'
            oldradius = F(disk['radius_upper_rational'])
            assert 0 <= wta <= oldradius
            assert tuple(map(F, disk['real_interval_rational'])) == (ta0[0]-oldradius, ta0[0]+oldradius)
            assert 0 < ta0[0]-oldradius < ta0[0]+oldradius < 1
            mta = F(disk['curvature_upper_rational'])
            assert mta > 0 and mta >= iv(disk['curvature_bound'])[1]
            active['old_ta_disk'] = dict(primitive_canonical_sha256=canonical_sha(oldta),
                full_disk_canonical_sha256=canonical_sha(disk), center_j=oldta['center_j'],
                center_j_prime=oldta['center_j_prime'], full_disk=disk,
                new_radius_rational=str(wta), uta_modulus=wuta)

            # Exactly one new center sine/log/cot and one real disk sine per case.
            zcenter = cc(cx(cut0))
            assert zcenter.real > 0 and zcenter.real < 1
            sine = elementary('center_complex_sines', pi*zcenter)
            assert sine.real > 0, 'original center logarithm branch not separated'
            jcut = elementary('center_logarithms', 2*sine)
            cotcenter = elementary('center_cotangents', pi*zcenter)
            jpcut = pi*cotcenter
            disk_sine = elementary('curvature_real_sines', pi*ar(distance))
            assert disk_sine > 0
            mvalue = pi*pi/(disk_sine*disk_sine)
            mtau = ends(mvalue)[1]
            assert mtau > 0
            active['new_cut_disk'].update(regular=True, center_input=complex_record(zcenter),
                center_sine=complex_record(sine), center_j=complex_record(jcut),
                center_cotangent=complex_record(cotcenter), center_j_prime=complex_record(jpcut),
                curvature_sine=rec(ends(disk_sine)), curvature_bound=rec(ends(mvalue)),
                curvature_upper_rational=str(mtau))
            jtau, jptau = cv(complex_record(jcut)), cv(complex_record(jpcut))
            jta, jpta = cv(oldta['center_j']), cv(oldta['center_j_prime'])
            ipi = (ZERO, pi_bounds)
            D0 = ca(csub(jtau, jta), cm(ipi, cx((tau-t0[0], -t0[1]))))
            Dt = csub(cs(jpta, -1), ipi)
            Da = csub(jptau, jpta)
            linear = ca(cm(Dt, cx(ut)), cm(Da, cx(ua)))
            p0, rho0 = sum(D0[1])/2, (D0[1][1]-D0[1][0])/2
            L0 = tuple(sum(v)/2 for v in linear)
            rhoL, wrhoL = norm(csub(linear, cx(L0)))
            ndt, wdt = norm(Dt)
            nda, wda = norm(Da)
            nlinear, wlinear = norm(linear)
            nL0, wL0 = norm(cx(L0))
            remainder = (mtau*wa*wa+mta*wta*wta)/2
            tail = errors['t']*ndt+errors['a']*nda+remainder
            rho = rho0+RADIUS*rhoL+tail
            Dreal = add(D0[0], (-RADIUS*nlinear-tail, RADIUS*nlinear+tail))
            height = iv(new['coordinate_enclosures']['a']['imag'])
            delta = H-height[1], H-height[0]
            assert delta[0] > 0 and contains(iv(old['height_displacement']), delta)
            delta0 = H-a0[1]
            combined = tuple(delta0*L0[j]-p0*ua[j] for j in range(2))
            ncombined, wcombined = norm(cx(combined))
            dot = sum(ua[j]*L0[j] for j in range(2))
            quadratic = RADIUS*RADIUS*(nua*nL0+dot)/2
            assert quadratic >= 0
            product_terms = (-delta0*p0, RADIUS*ncombined, quadratic,
                             delta[1]*rho, errors['a']*(abs(p0)+RADIUS*nL0))
            UD = sum(product_terms)
            active['difference_enclosure'] = dict(D0=cr(D0), Dt=cr(Dt), Da=cr(Da), L=cr(linear),
                p0_rational=str(p0), rho0_rational=str(rho0), L0_exact=list(map(str, L0)),
                rhoL=wrhoL, Dt_modulus=wdt, Da_modulus=wda, L_modulus=wlinear,
                L0_modulus=wL0, Taylor_remainder_rational=str(remainder),
                posterior_and_Taylor_error_rational=str(tail), rho_rational=str(rho),
                real=rec(Dreal), delta=rec(delta), delta0_rational=str(delta0),
                combined_linear_modulus=wcombined, dot_ua_conjugateL0_rational=str(dot),
                negative_height_product_terms_rational=list(map(str, product_terms)),
                negative_height_product_upper_rational=str(UD), product_zero_cap_applied=False)

            # Old a,s enclosures retain their original whole disk/slab scope.
            means = dict(a=ZERO, s=ZERO, cut=ZERO)
            V = ZERO
            real_cut = cut0[0]-wa, cut0[0]+wa
            assert 0 < real_cut[0] <= real_cut[1] < 1
            assert len(old['slabs']) == 16
            for index, oldslab in enumerate(old['slabs']):
                left, right = F(index, 16), F(index+1, 16)
                weight, weighted = F(1, 16), F(31-2*index, 512)
                assert oldslab['index'] == index and iv(oldslab['theta']) == (left, right)
                assert F(oldslab['weight_rational']) == weight and F(oldslab['weighted_rational']) == weighted
                heights, endpoint_supports = [], []
                for theta in (left, right):
                    midpoint, width = (1-theta)*a0[1]+theta*H, (1-theta)*wa
                    interval = midpoint-width, midpoint+width
                    heights.append(interval)
                    endpoint_supports.append(dict(theta_rational=str(theta), midpoint_rational=str(midpoint),
                        width_rational=str(width), interval=rec(interval)))
                imag_cut = min(x[0] for x in heights), max(x[1] for x in heights)
                slab = dict(index=index, theta=rec((left, right)), weight_rational=str(weight),
                    weighted_rational=str(weighted), old_slab_canonical_sha256=canonical_sha(oldslab),
                    new_cut_node=dict(real=rec(real_cut), imag=rec(imag_cut), endpoint_supports=endpoint_supports))
                active['slabs'].append(slab)
                counts['height_slabs'] += 1
                zslab = cc((real_cut, imag_cut))
                assert zslab.real > 0 and zslab.real < 1
                cot = elementary('slab_cotangents', pi*zslab)
                cutcot = (ends(cot.real), ends(cot.imag))
                slab['new_cut_node'].update(outward_input=complex_record(zslab), cotangent=cr(cutcot))
                C, I = {}, {}
                for name in ('a', 's'):
                    cotold = oldslab['nodes'][name]['cotangent']
                    C[name], I[name] = iv(cotold['real']), iv(cotold['imag'])
                    slab['old_'+name+'_cotangent'] = cotold
                    means[name] = add(means[name], sc(I[name], weight))
                means['cut'] = add(means['cut'], sc(cutcot[1], weight))
                contribution = sc(sub(sub(sc(C['a'], 3), C['s']), cutcot[0]), weighted)
                V = add(V, contribution)
                slab['V_contribution'] = rec(contribution)
                slab['Icut_contribution'] = rec(sc(cutcot[1], weight))
            for name in ('a', 's'):
                assert means[name] == iv(saved['normalized_Imcot_means'][name])
            kappa = mul(pi_bounds, delta)
            W = mul(mul(kappa, delta), V)
            Q = iv(old['forced_additions']['own_force'])
            GH = F(old['forced_additions']['J_upper_rational'])
            centers = {name: iv(new['coordinate_enclosures'][name]['real']) for name in ('s', 'a')}
            targets = {'s': (F('.22'), F('.5')), 'a': (F('.22'), F('.45'))}
            for name in centers:
                assert contains(targets[name], centers[name])
            active['shared_integrals'] = dict(pi=rec(pi_bounds), delta=rec(delta), kappa=rec(kappa),
                normalized_V=rec(V), W=rec(W), Ia=rec(means['a']), Is=rec(means['s']),
                Icut=rec(means['cut']), ReD=rec(Dreal), Q=rec(Q), GH_upper_rational=str(GH),
                old_forced_additions_canonical_sha256=canonical_sha(old['forced_additions']))
            for nu in (1, 0):
                trial = UD+W[1]+(-2*pi_bounds[0]*H if nu else GH)
                Ka = F(49, 5)*(nu+F(1, 2)+sigma)
                parameters = [kappa, means['a'], means['s'], means['cut'], Dreal]
                if not nu:
                    parameters.append(Q)
                branch = dict(nu=nu, trial_upper_rational=str(trial), selected_K_rational=str(Ka),
                    parameter_order=['kappa', 'Ia', 'Is', 'Icut', 'ReD']+(['Q'] if not nu else []),
                    parameter_intervals=list(map(rec, parameters)), vertices=[])
                active['branches'].append(branch)
                for bits in product((0, 1), repeat=len(parameters)):
                    point = [value[bit] for value, bit in zip(parameters, bits)]
                    k, ia, iss, itau, dr = point[:5]
                    forces = dict(s=k*(1-iss), a=dr+k*(3*ia-iss-itau-1)+(point[5] if not nu else 0))
                    vertex = dict(endpoint_bits=list(bits), parameters_rational=list(map(str, point)),
                        forces_rational={n:str(v) for n,v in forces.items()}, gains={}, independent_gain_checks={})
                    branch['vertices'].append(vertex)
                    counts['vertices'] += 1
                    total = F(0)
                    for name, K in (('s', F(88, 5)), ('a', Ka)):
                        upper, witness = gain_module.gain(ex(forces[name]), centers[name], targets[name], K)
                        counts['scalar_cubic_gains'] += 1
                        verified, check = check_module.check_gain(witness, ex(forces[name]), centers[name], targets[name], K)
                        counts['independent_gain_checks'] += 1
                        assert upper == verified
                        vertex['gains'][name] = witness
                        vertex['independent_gain_checks'][name] = dict(upper_rational=str(verified), check=check)
                        total += upper
                    vertex['gain_sum_upper_rational'] = str(total)
                    vertex['phase_upper_before_bare_rational'] = str(trial+total)
                assert len(branch['vertices']) == (32 if nu else 64)
                maximum = max(F(v['phase_upper_before_bare_rational']) for v in branch['vertices'])
                branch['phase_upper_before_bare_rational'] = str(maximum)
                branch['attaining_vertices'] = [v['endpoint_bits'] for v in branch['vertices']
                    if F(v['phase_upper_before_bare_rational']) == maximum]
            desired = [('three_mixed', 1), ('three_half', 0)] if not epsilon else [('four', 0)]
            for series, family in desired:
                found = [f for f in face['families'] if (f['series'], f['family']) == (series, family)]
                assert len(found) == 1
                family_data = found[0]
                assert family_data['complete_finite_coverage'] and not family_data['null_jobs_unresolved']
                bare = F(family_data['uniform_bare_upper_rational'])
                assert bare == max(F(j['decoded_upper_rational']) for j in family_data['contributing_jobs'])
                for branch in active['branches']:
                    upper = bare+F(branch['phase_upper_before_bare_rational'])
                    active['comparisons'].append(dict(series=series, family=family, nu=branch['nu'],
                        source_family_canonical_sha256=canonical_sha(family_data),
                        source_job_count=len(family_data['contributing_jobs']), bare_upper_rational=str(bare),
                        phase_upper_before_bare_rational=branch['phase_upper_before_bare_rational'],
                        joined_upper_rational=str(upper), strictly_negative=upper < 0,
                        gap_rational=str(-upper), source_scope='actual K4'))
                    counts['source_comparisons'] += 1
            active['status'] = 'enclosed both full-P branches and all assigned source comparisons'
            counts['completed_cases'] += 1
            out['pending_cases'].remove(dict(beta=1, epsilon=epsilon, tau_rational=str(tau)))
            print(json.dumps(dict(epsilon=epsilon, status=active['status'],
                branch_uppers=[float(F(b['phase_upper_before_bare_rational'])) for b in active['branches']])), flush=True)
            active = None
        assert counts['cases'] == counts['completed_cases'] == 2 and not out['pending_cases']
        assert counts['height_slabs'] == 32 and all(counts[k] == v for k, v in LIMITS.items())
        assert counts['vertices'] == 192
        assert counts['scalar_cubic_gains'] == counts['independent_gain_checks'] == 384
        assert counts['source_comparisons'] == 6
        comparisons = [x for case in out['cases'] for x in case['comparisons']]
        worst = max(F(x['joined_upper_rational']) for x in comparisons)
        out.update(status='completed fixed protocol', all_six_comparisons_enclosed=True,
            all_six_signs_proved=worst < 0, worst_joined_upper_rational=str(worst),
            common_six_margin_rational=str(-worst) if worst < 0 else None)
    except (Exception, KeyboardInterrupt) as exc:
        fatal = exc
        out['status'] = 'failed fixed protocol'
        out['error'] = dict(type=type(exc).__name__, message=str(exc))
        if active is not None:
            active['status'] = 'failed fixed protocol'
            active['error'] = out['error']
    out['changed_inputs'] = [name for name, digest in inputs.items()
        if not (ROOT/name).is_file() or sha(ROOT/name) != digest]
    if out['changed_inputs']:
        out['status'] = 'changed inputs'
        out['all_six_comparisons_enclosed'] = out['all_six_signs_proved'] = False
    out['proof_sha256'], out['driver_sha256'] = inputs[PROOF], inputs[own]
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open('xb') as raw:
        with gzip.GzipFile(filename='', fileobj=raw, mode='wb', compresslevel=1, mtime=0) as gz:
            with io.TextIOWrapper(gz, encoding='utf-8', newline='\n') as stream:
                json.dump(out, stream, separators=(',', ':'))
                stream.write('\n')
    print(json.dumps(dict(status=out['status'], counts=counts, all_six_signs_proved=out['all_six_signs_proved'],
        output_sha256=sha(args.output))), flush=True)
    if fatal is not None:
        raise fatal
    if out['changed_inputs']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
