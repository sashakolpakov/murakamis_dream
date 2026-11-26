#!/usr/bin/env python3
"""Fixed whole-D3 terminal budgets; original saved references, no adaptivity.

Only main() imports Flint. The two imported frozen helpers are used solely
for exact rational cubic gains and independent checks of their witnesses.
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
PROOF = 'notes/research_mixed_terminal_three_input_budget_protocol.md'
THEORY = 'notes/research_mixed_terminal_incoming_type_transfer.md'
REFINED = 'repro/results/research-mixed-terminal-quadratic-residual-refinement.json'
POSTERIOR = 'repro/results/research-mixed-terminal-split-taylor-completion.json'
SPLIT = 'repro/results/research-mixed-terminal-split-taylor-inclusion.json'
AFFINE = 'repro/results/research-mixed-terminal-correlated-affine-family.json'
FACES = 'repro/results/research-mixed-terminal-uniform-face-reserves.json'
ALIASES = 'repro/results/research-mixed-terminal-uniform-alias-reserves.json'
GAIN = 'experiments/certify_mixed_terminal_four_input_integral_budget.py'
GAIN_CHECKER = 'experiments/check_mixed_terminal_four_input_integral_budget.py'
PINNED = {
    'notes/research_mixed_terminal_real_transform_cut_budget.md': 'ee4ba95733040b87abf9a4f956f076444f505f1ba2502e684cbe2c9dd37ecf92',
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
    'notes/research_mixed_terminal_three_input_budget_protocol.md': '0c37a9813a30cbd964aa0931e13ea1f1f7a2825408f64e071f7400954e4541b6',
    'notes/research_mixed_terminal_incoming_type_transfer.md': '5c8f8f53c9618a19220289f21b7505358733d8a6764c352688ee0f425bd03173',
    'repro/results/research-mixed-terminal-uniform-alias-reserves.json': '142f424a414174fc8ee8ba0fd4ee69b6c8c6ffd5c954bbba9211771536b9bd87',
    'notes/research_mixed_terminal_uniform_alias_reserves.md': 'c942ce53d48079e1a2aa0c9d087b7eb0c92c70de13685ba9b0d0f08a0b1bda8a',
    'experiments/check_mixed_terminal_uniform_alias_reserves.py': '3b831a9cc4dd742e0e235e2c769b3d8dbd236c25f9267ea7d1afd59c46b63abd',
    'notes/research_mixed_terminal_uniform_constant_profile.md': '1aff3730e96efe0f62e00a44247150de54ac4d5f93eeed436a94952d89a60c96',
    'notes/research_mixed_terminal_uniform_joined_plane.md': '12ab4cd4e94a521ac97da4e8f71aa68b2352764cd2d283cf123e9f5f113b11e5',
    'notes/research_mixed_terminal_reserved_plane_transfer.md': '0d4461c5b00e4f68dc00c0c1d6e824156c9c5050327eab70694f3cd21e714c70',
    'notes/research_mixed_terminal_private_left_symmetric_transfer.md': '1c007e90e1fd8057d8b3773fd712fbb331b0d71c4b253664535805b37e9e7199',
    'notes/research_mixed_terminal_four_input_private_left_force.md': '28fd9890765e9b4f666d7fe11bc0364c4e1b6c9de4ae45506251c0ec27679f3b',
    'notes/research_mixed_terminal_private_left_uniform_force.md': '20361d2a52affe5273ab4aa056f66b250fa498bb9f87742609f1d9450b9b2ee2',
    'notes/research_mixed_terminal_horizontal_envelope_diagnostic.md': 'ea1e6d1daf4b8e3822a198de1f63f4f211061761af8bdd01d641b4d8f930ad72',
    'experiments/diagnose_mixed_terminal_horizontal_envelope.py': 'c8e45e240f8b1ec51c0da612b2e75256204b5b57df8f0bdf0ffa565b6b2286f9',
    'experiments/check_mixed_terminal_horizontal_envelope_record.py': '23545f9f66ec7ba9e2ddb89410f9c198a64f4d615b95df4d346bc2083936cdcb',
    'notes/research_mixed_terminal_main_optimizer_localization.md': '6e88ab6d8635255877ae6ba570d6d8e434880f8a01c710452ed48b4cde482295',
    'notes/research_mixed_open_word_critical_localization.md': 'a3f8a0f781abd43f8ca17321171081ba37c91b284f83f22a4f7ae34e270424fa',
    'notes/research_mixed_cyclic_critical_localization.md': 'ccb8b144e6068c434059b707cd13d9aed8bb88a40e7fa0cf0e6bc655bff7fa71',
}
NAMES = ('e', 'xi', 't', 'a', 's')
H, RADIUS, GAP = F(1, 100), F(9, 100), F(1, 10000)
PARAMETER_CENTER = (F(7, 20), -F(1, 100))
PRECISION = MESH_BITS = 256
Z = (F(0), F(0))
CUTS = (F(3, 20), F(1, 2))
NODES = ('a', 's', 't', 'cut_left', 'cut_right')
LIMITS = dict(pi=1, exponential=1, cosine=2, sine=10, logarithm=9,
              cotangent=164, vertices=528, scalar_cubic_gains=1152,
              independent_gain_checks=1152, required_comparisons=108,
              direct_alternatives=28, private_left_alternatives=2)


class Inconclusive(Exception):
    def __init__(self, message, operands=None):
        super().__init__(message)
        self.operands = operands


def require(test, message, operands=None):
    if not test:
        raise Inconclusive(message, operands)


def sha(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1048576), b''):
            h.update(block)
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


def rec(value):
    return dict(finite=True, lower_rational=str(value[0]), upper_rational=str(value[1]))


def cv(value): return iv(value['real']), iv(value['imag'])
def cr(value): return dict(real=rec(value[0]), imag=rec(value[1]))
def ex(value): return F(value), F(value)
def cx(value): return ex(value[0]), ex(value[1])
def add(x, y): return x[0]+y[0], x[1]+y[1]
def neg(x): return -x[1], -x[0]
def sub(x, y): return add(x, neg(y))
def mul(x, y):
    products = [a*b for a in x for b in y]
    return min(products), max(products)
def sc(x, value): return mul(x, ex(value))
def ca(x, y): return add(x[0], y[0]), add(x[1], y[1])
def cs(x, value): return sc(x[0], value), sc(x[1], value)
def cn(x): return neg(x[0]), neg(x[1])
def csub(x, y): return ca(x, cn(y))
def cm(x, y):
    return sub(mul(x[0], y[0]), mul(x[1], y[1])), add(mul(x[0], y[1]), mul(x[1], y[0]))
def contained(outer, inner): return outer[0] <= inner[0] <= inner[1] <= outer[1]
def absmax(x): return max(abs(x[0]), abs(x[1]))
def exact_sum(x, y): return x[0]+y[0], x[1]+y[1]
def exact_scale(x, a): return a*x[0], a*x[1]


def norm(value):
    squared = sum(absmax(component)**2 for component in value)
    mesh = 1 << MESH_BITS
    root = isqrt(squared.numerator*mesh*mesh//squared.denominator)
    lo = F(root, mesh)
    hi = lo if lo*lo == squared else F(root+1, mesh)
    assert lo*lo <= squared <= hi*hi
    return hi, dict(rectangle=cr(value), squared_radius_rational=str(squared),
                    modulus=rec((lo, hi)), mesh_bits=MESH_BITS)


def intersect(x, y, witness):
    value = max(x[0], y[0]), min(x[1], y[1])
    witness.update(raw=rec(x), necessary=rec(y),
                   intersection_rational=list(map(str, value)))
    require(value[0] <= value[1], 'empty necessary reference-image intersection', witness)
    return value


def typed_ranges(epsilon):
    # Original strong image bounds; never used to clip a Taylor tube.
    result = dict(a=((F('.24'), F('.36')), (F('-.102'), F('-.001'))),
                  s=((F('.24'), F('.36')), (F('-.102'), F('-.001'))))
    if epsilon:
        result.update(e=((F('.333'), F('.363')), (F('-.051'), F('-.019'))),
                      xi=((F('.21'), F('.25')), (F('.01'), F('.10'))),
                      t=((F('.246'), F('.350')), (F('-.108'), F('-.020'))))
    else:
        result.update(e=((F('.33'), F('.47')), (F('-.09'), F('.08'))),
                      xi=((F('.218'), F('.242')), (F('.049'), F('.077'))),
                      t=((F('.278'), F('.391')), (F('-.072'), F('.021'))))
    return result


def verify_case(new, prior, splitcase, affine, face, aliases, epsilon):
    for entry in (new, prior, splitcase, affine, face, aliases):
        assert (entry['beta'], entry['epsilon']) == (0, epsilon)
    assert new['source_posterior_canonical_sha256'] == canonical_sha(prior)
    assert new['split_case_canonical_sha256'] == canonical_sha(splitcase)
    assert new['affine_case_canonical_sha256'] == canonical_sha(affine)
    assert prior['source_case_canonical_sha256'] == canonical_sha(splitcase)
    assert splitcase['source_case_canonical_sha256'] == canonical_sha(affine)
    assert face['refinement_case_canonical_sha256'] == canonical_sha(new)
    assert face['source_posterior_canonical_sha256'] == canonical_sha(prior)
    assert aliases['refinement_case_canonical_sha256'] == canonical_sha(new)
    assert aliases['image_cover_case_canonical_sha256'] == canonical_sha(face)
    for key in ('center_exact', 'response_exact', 'parameter_center', 'parameter_radius_rational'):
        assert new[key] == prior[key]
    assert new['center_exact'] == splitcase['original_center'] == affine['center']
    assert new['response_exact'] == splitcase['original_response'] == affine['response_exact']
    assert tuple(map(F, new['parameter_center'])) == PARAMETER_CENTER
    assert F(new['parameter_radius_rational']) == RADIUS
    assert new['exact_linear_system_verified'] and prior['exact_linear_system_verified']
    assert all(0 <= F(a) <= F(b) for a, b in
               zip(new['posterior_radii_rational'], prior['posterior_radii_rational']))
    assert F(new['multiplier_rational']) == F(prior['multiplier_rational']) == 2
    scandidates = [c for c in splitcase['candidates'] if F(c['multiplier_rational']) == 2]
    candidates = [c for c in affine['candidates'] if F(c['multiplier_rational']) == 2]
    assert len(scandidates) == len(candidates) == 1
    scandidate, candidate = scandidates[0], candidates[0]
    assert prior['source_candidate_canonical_sha256'] == canonical_sha(scandidate)
    assert scandidate['source_candidate_canonical_sha256'] == canonical_sha(candidate)
    assert scandidate['criterion_pass'] and splitcase['family_certified']
    # The original unsplit D3 inclusion failed. Its full-tube data remain
    # valid inputs to the subsequently successful split-Taylor certificate.
    assert candidate['saved_central_root_contained']
    assert candidate['all_full_original_log_disks_regular']
    assert face['all_nine_uniform_bare_bounds_defined'] and aliases['all_twelve_bare_bounds_defined']
    assert face['physical_a_box_rational'] == aliases['physical_a_box_rational']
    assert face['intersecting_original_cells'] == aliases['intersecting_original_cells']
    for j, part in enumerate(('real', 'imag')):
        assert tuple(map(F, face['physical_a_box_rational'][j])) == iv(new['coordinate_enclosures']['a'][part])
    assert len(face['families']) == 9 and len(aliases['families']) == 12
    assert len(aliases['alias_labels']) == 16
    return candidate


def supports(new, epsilon, row):
    centers = dict(zip(NAMES, (tuple(map(F, p)) for p in new['center_exact'])))
    responses = dict(zip(NAMES, (tuple(map(F, p)) for p in new['response_exact'])))
    errors = dict(zip(NAMES, map(F, new['posterior_radii_rational'])))
    typed, individual, widths = typed_ranges(epsilon), {}, {}
    row['individual_supports'] = {}
    row['typed_range_source'] = 'original endpoint rectangles and full-bidisk own-four image theorem'
    for name in NAMES:
        modulus, witness = norm(cx(responses[name]))
        widths[name] = RADIUS*modulus+errors[name]
        item = dict(modulus_witness=witness, width_rational=str(widths[name]),
                    necessary_intersections={})
        row['individual_supports'][name] = item
        pieces = []
        for j, part in enumerate(('real', 'imag')):
            raw = centers[name][j]-widths[name], centers[name][j]+widths[name]
            w = {}
            item['necessary_intersections'][part] = w
            bounded = intersect(raw, typed[name][j], w)
            # Both independently established reference enclosures may be used.
            w2 = {}
            item['necessary_intersections'][part+'_saved'] = w2
            bounded = intersect(bounded, iv(new['coordinate_enclosures'][name][part]), w2)
            pieces.append(bounded)
        individual[name] = tuple(pieces)
        item.update(real=rec(pieces[0]), imag=rec(pieces[1]))

    def argument(name, theta):
        base = name if name in ('s', 't') else None
        tau = {'cut_left': CUTS[0], 'cut_right': CUTS[1]}.get(name, F(0))
        weight = 1-theta
        if base is None:
            raw_real = centers['a'][0]+tau-widths['a'], centers['a'][0]+tau+widths['a']
            real_necessary = add(individual['a'][0], ex(tau))
            mid = weight*centers['a'][1]+theta*H
            width = weight*widths['a']
            imaginary_necessary = add(sc(individual['a'][1], weight), ex(theta*H))
            modulus_witness = None
        else:
            real_coefficient = exact_sum(responses[base], responses['a'])
            modulus, real_witness = norm(cx(real_coefficient))
            rw = RADIUS*modulus+errors[base]+errors['a']
            rm = centers[base][0]+centers['a'][0]
            raw_real = rm-rw, rm+rw
            real_necessary = add(individual[base][0], individual['a'][0])
            coefficient = exact_sum(responses[base], exact_scale(responses['a'], weight))
            modulus, modulus_witness = norm(cx(coefficient))
            mid = centers[base][1]+weight*centers['a'][1]+theta*H
            width = RADIUS*modulus+errors[base]+weight*errors['a']
            imaginary_necessary = add(individual[base][1],
                                      add(sc(individual['a'][1], weight), ex(theta*H)))
        w = dict(node=name, theta_rational=str(theta),
                 imaginary_midpoint_rational=str(mid), imaginary_width_rational=str(width),
                 imaginary_coefficient_modulus=modulus_witness,
                 real_intersection={}, imaginary_intersection={})
        if base is not None:
            w['real_coefficient_modulus'] = real_witness
        real = intersect(raw_real, real_necessary, w['real_intersection'])
        imaginary = intersect((mid-width, mid+width), imaginary_necessary, w['imaginary_intersection'])
        return real, imaginary, w
    return centers, responses, errors, widths, individual, argument


def signed_product(F0, L, derivative_error, ua, eta_a, delta0, delta, sign):
    """Upper sign*Delta*Im(F), retaining all center coefficient intervals."""
    p = F0[1]
    nu, wu = norm(cx(ua))
    nl, wl = norm(L)
    linear = csub(cs(L, delta0), cm(cx(ua), (p, Z)))
    nlinear, wlinear = norm(linear)
    dot = add(sc(L[0], ua[0]), sc(L[1], ua[1]))
    # sign=+1 has minus dot; sign=-1 has plus dot.
    quad = RADIUS**2*(nu*nl+(-dot[0] if sign == 1 else dot[1]))/2
    require(quad >= 0, 'negative quadratic upper witness',
            dict(sign=sign, ua_exact=list(map(str, ua)), L=cr(L),
                 dot_interval=rec(dot), quadratic_upper_rational=str(quad)))
    terms = (sc(p, sign*delta0)[1], RADIUS*nlinear, quad,
             delta[1]*derivative_error, eta_a*(absmax(p)+RADIUS*nl))
    return sum(terms), dict(sign=sign, F0=cr(F0), L=cr(L),
        full_center_interval_used=True, error_radius_rational=str(derivative_error),
        ua_exact=list(map(str, ua)), delta0_rational=str(delta0), delta=rec(delta),
        ua_modulus=wu, L_modulus=wl, linear_modulus=wlinear, dot_interval=rec(dot),
        terms_rational=list(map(str, terms)), upper_rational=str(sum(terms)))


def private_left_guards(individual):
    a, t, e = individual['a'], individual['t'], individual['e']
    guards = dict(A_above_299=a[0][0] > F('.299'), A_at_most_36=a[0][1] <= F('.36'),
        t_above_302=t[0][0] > F('.302'), t_at_most_350=t[0][1] <= F('.350'),
        ht_above_minus071=t[1][0] > F('-.071'), ht_at_most_minus020=t[1][1] <= F('-.020'),
        e_original_real=F('.333') <= e[0][0] <= e[0][1] <= F('.363'),
        e_original_height=F('-.051') <= e[1][0] <= e[1][1] <= F('-.019'))
    return dict(guards=guards, available=all(guards.values()),
        original_open_endpoint_bounds_retained=True,
        proof='notes/research_mixed_terminal_four_input_private_left_force.md')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    if not str(args.output).endswith('.json.gz'):
        raise ValueError('fresh .json.gz output required')
    if hasattr(sys, 'set_int_max_str_digits'):
        sys.set_int_max_str_digits(0)
    inputs = dict(PINNED)
    own = Path(__file__).resolve().relative_to(ROOT).as_posix()
    inputs[own] = sha(ROOT/own)
    counts = dict.fromkeys(LIMITS, 0)
    counts.update(cases=0, completed_cases=0, height_slabs=0, roots=0,
                  source_evaluations=0, target_optimizers=0, private_actions=0,
                  dilogarithms=0, subdivisions=0, retries=0)
    out = dict(status='initializing', proof_path=PROOF, theory_path=THEORY,
        driver_path=own, precision_bits=PRECISION, delta_rational=str(GAP),
        input_sha256=inputs, counts=counts, limits=LIMITS, cases=[],
        pending_cases=[dict(beta=0, epsilon=e) for e in (0, 1)],
        phase_scope='entire canonical D3; full independent fixed-height targets',
        source_scope='canonical actual K3; incoming unselected type3, ordinary own4',
        all_108_comparisons_enclosed=False, all_108_negative=False,
        target_gap_proved=False, whole_source_theorem_proved=False,
        knot_theorem_proved=False)
    fatal, active = None, None
    try:
        assert PINNED
        def bind(name, digest):
            assert isinstance(digest, str) and len(digest) == 64
            assert name not in inputs or inputs[name] == digest, name
            assert sha(ROOT/name) == digest, name
            inputs[name] = digest
        for name, digest in list(inputs.items()):
            bind(name, digest)
        paths = (REFINED, POSTERIOR, SPLIT, AFFINE, FACES, ALIASES)
        data = {path: json.loads((ROOT/path).read_text()) for path in paths}
        for entry in data.values():
            assert entry.get('changed_inputs', []) == []
            for key in ('input_sha256', 'dependencies_sha256', 'dependencies'):
                if isinstance(entry.get(key), dict):
                    for name, digest in entry[key].items():
                        bind(name, digest)
        refined, posterior, split, affine, faces, aliases = (data[p] for p in paths)
        assert refined['status'] == 'completed fixed saved-only protocol'
        assert refined['source_path'] == POSTERIOR and refined['source_sha256'] == inputs[POSTERIOR]
        assert posterior['status'] == 'passed' and posterior['all_four_input_disks_certified']
        assert posterior['source_path'] == SPLIT and posterior['source_sha256'] == inputs[SPLIT]
        assert split['all_four_input_families_certified'] and split['source_sha256'] == inputs[AFFINE]
        assert affine['status'] == 'completed fixed protocol'
        assert faces['all_uniform_bare_bounds_defined'] and not faces['unresolved_family_cases']
        assert aliases['all_uniform_alias_bounds_defined'] and not aliases['unresolved_family_cases']
        assert aliases['image_cover_sha256'] == inputs[FACES]
        assert F(aliases['height_debit_rational']) == F(41, 1000)
        modules = []
        for name, path in (('three_input_exact_gain', GAIN), ('three_input_gain_checker', GAIN_CHECKER)):
            spec = importlib.util.spec_from_file_location(name, ROOT/path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            modules.append(module)
        gain, checker = modules
        from flint import arb, acb, ctx
        ctx.prec = PRECISION
        def ar(value):
            value = F(value)
            return arb(value.numerator)/arb(value.denominator)
        def fraction(value):
            p, q = value.fmpq().p, value.fmpq().q
            return F(int(p), int(q))
        def ends(value):
            require(value.is_finite(), 'nonfinite analytic interval',dict(display=str(value)))
            return fraction(value.lower()), fraction(value.upper())
        def ball(value):
            lo, hi = value
            result = arb(ar((lo+hi)/2), ar((hi-lo)/2).upper())
            require(contained(ends(result), value), 'rounded input does not contain rational rectangle',
                    dict(exact=rec(value),rounded=rec(ends(result))))
            return result
        def complex_ball(value):
            result = acb(ball(value[0]), ball(value[1]))
            require(contained(ends(result.real), value[0]) and contained(ends(result.imag), value[1]),
                    'rounded complex input does not contain rational rectangle',
                    dict(exact=cr(value),rounded=cr((ends(result.real),ends(result.imag)))))
            return result
        def elementary(kind, value=None):
            counts[kind] += 1
            assert counts[kind] <= LIMITS[kind], kind
            operand = None if value is None else (cr((ends(value.real),ends(value.imag)))
                if isinstance(value,acb) else rec(ends(value)))
            out['last_analytic_operation'] = dict(kind=kind,ordinal=counts[kind],input=operand)
            result = arb.pi() if kind == 'pi' else getattr(value,
                dict(exponential='exp', sine='sin', cosine='cos',
                     logarithm='log', cotangent='cot')[kind])()
            require(result.is_finite(), 'nonfinite '+kind,out['last_analytic_operation'])
            return result
        pi = elementary('pi')
        pi_bounds = ends(pi)
        require(F(157, 50) < pi_bounds[0] <= pi_bounds[1] < F(22, 7), 'pi range',rec(pi_bounds))
        ipi = (Z, pi_bounds)
        exp_height = elementary('exponential', 2*pi*ar(H))
        log_two = elementary('logarithm', arb(2))
        out['constants'] = dict(pi=rec(pi_bounds), exp_2piH=rec(ends(exp_height)), log_two=rec(ends(log_two)))

        for epsilon in (0, 1):
            counts['cases'] += 1
            active = dict(beta=0, epsilon=epsilon, status='initializing', comparisons=[],
                slabs=[], cuts=[], budgets=[], pending_height_nodes=[[j,n] for j in range(16) for n in NODES],
                pending_cuts=list(map(str, CUTS)),
                pending_budgets=[[kind,nu] for kind in ('main','plane','cut_left','cut_right') for nu in (1,0)],
                expected_required_comparisons=54)
            out['cases'].append(active)
            try:
                new = refined['cases'][epsilon]
                prior = posterior['posterior_enclosures'][epsilon]
                sp, aff, face, alias = (entry['cases'][epsilon] for entry in (split, affine, faces, aliases))
                candidate = verify_case(new, prior, sp, aff, face, alias, epsilon)
                expected = ([('four',j) for j in list(range(8))+[20]] if epsilon else
                            [('three_mixed',j) for j in range(8)]+[('three_half',0)])
                assert [(f['series'],f['family']) for f in face['families']] == expected
                labels = ['main','constant']+[
                    'alias:'+v['t_state']+':'+v['private_state'] for v in alias['alias_labels']]+[
                    series+':'+str(family) for series,family in expected]
                assert len(labels) == len(set(labels)) == 27
                active['required_label_inventory'] = labels
                active['pending_comparisons'] = [[label,nu] for label in labels for nu in (1,0)]
                active['source_associations'] = {name:canonical_sha(entry) for name,entry in
                    (('refinement',new),('posterior',prior),('split',sp),('affine',aff),('face',face),('alias',alias))}
                active.update(center_exact=new['center_exact'], response_exact=new['response_exact'],
                    posterior_radii_rational=new['posterior_radii_rational'],
                    parameter_center=new['parameter_center'], parameter_radius_rational=new['parameter_radius_rational'])
                centers, responses, eta, widths, individual, argument = supports(new, epsilon, active)
                delta = H-individual['a'][1][1], H-individual['a'][1][0]
                require(delta[0] > 0, 'nonpositive selected height displacement',
                        dict(H_rational=str(H),a_height=rec(individual['a'][1]),delta=rec(delta)))
                kappa = mul(pi_bounds, delta)
                active['height_displacement'], active['kappa'] = rec(delta), rec(kappa)
                means = {name:Z for name in NODES}
                weighted = {name:Z for name in NODES}
                for j in range(16):
                    left, right = F(j,16), F(j+1,16)
                    weight, omega = F(1,16), F(31-2*j,512)
                    slab = dict(index=j, theta=rec((left,right)), weight_rational=str(weight),
                                weighted_rational=str(omega), nodes={})
                    active['slabs'].append(slab)
                    counts['height_slabs'] += 1
                    for name in NODES:
                        lr, li, lw = argument(name,left)
                        rr, ri, rw = argument(name,right)
                        assert lr == rr
                        height = min(li[0],ri[0]), max(li[1],ri[1])
                        node = dict(real=rec(lr), imag=rec(height), endpoint_supports=[lw,rw])
                        slab['nodes'][name] = node
                        require(0 < lr[0] <= lr[1] < 1, 'cotangent original strip: '+name,
                                dict(slab=j,node=name,rectangle=cr((lr,height))))
                        value = complex_ball((lr,height))
                        require(value.real > 0 and value.real < 1, 'rounded cotangent strip',
                                dict(slab=j,node=name,rounded=cr((ends(value.real),ends(value.imag)))))
                        cot = elementary('cotangent', pi*value)
                        C, I = ends(cot.real), ends(cot.imag)
                        node['cotangent'] = dict(real=rec(C),imag=rec(I))
                        node['mean_contribution'], node['weighted_contribution'] = rec(sc(I,weight)),rec(sc(C,omega))
                        means[name] = add(means[name],sc(I,weight))
                        weighted[name] = add(weighted[name],sc(C,omega))
                        active['pending_height_nodes'].remove([j,name])
                active['normalized_Imcot_means'] = {n:rec(v) for n,v in means.items()}
                active['weighted_Recot_means'] = {n:rec(v) for n,v in weighted.items()}
                A = individual['a'][0]
                cosine = elementary('cosine',2*pi*ball(A))
                square = 1+exp_height*exp_height-2*exp_height*cosine
                require(square > 0,'nonpositive selected-force logarithm',
                        dict(A=rec(A),exp_height=rec(ends(exp_height)),cosine=rec(ends(cosine)),square=rec(ends(square))))
                Q = ends(elementary('logarithm',square)/2)
                sine = elementary('sine',pi*ar(A[1]))
                require(sine > 0,'nonpositive chord sine',dict(A=rec(A),sine=rec(ends(sine))))
                log_sine = elementary('logarithm',2*sine)
                bracket = add(ends(log_sine),ends(log_two))
                require(bracket[0] > 0 and F(1,6) < A[0] <= A[1] < F(1,2),'chord domain',
                        dict(A=rec(A),bracket=rec(bracket)))
                GH = -(F(1,2)-A[1])*bracket[0]/2
                active['selected_primitives'] = dict(A=rec(A),cosine=rec(ends(cosine)),
                    modulus_square=rec(ends(square)),Q=rec(Q),sine=rec(ends(sine)),
                    log_sine=rec(ends(log_sine)),bracket=rec(bracket),GH_upper_rational=str(GH))

                terms = {term['name']:term for term in aff['primitive_terms']}
                full = {term['name']:term['full_curvature'] for term in candidate['full_primitive_terms']}
                gp, gpp, curvature, old_witnesses = {}, {}, {}, {}
                for name, center, width in (
                    ('a',centers['a'],widths['a']),
                    ('a+s',exact_sum(centers['a'],centers['s']),
                     RADIUS*norm(cx(exact_sum(responses['a'],responses['s'])))[0]+eta['a']+eta['s'])):
                    old, guard = terms[name], full[name]
                    assert tuple(map(F,old['center_exact'])) == tuple(map(F,guard['center_exact'])) == center
                    require(guard['regular'] is True and guard['stage']=='full','saved full tube not regular',guard)
                    require(width <= F(guard['radius_upper_rational']),'refined full tube not contained',
                            dict(name=name,refined_radius_rational=str(width),saved_full_curvature=guard))
                    lo,hi = map(F,guard['real_interval_rational'])
                    require(0 < lo < hi < 1,'saved derivative strip',dict(name=name,full_curvature=guard))
                    m = F(guard['curvature_upper_rational'])
                    assert m >= iv(guard['curvature_bound'])[1] > 0
                    gp[name] = ca(cv(old['center_j']),cm(ipi,cx((F(1,2)-center[0],-center[1]))))
                    gpp[name] = csub(cv(old['center_j_prime']),ipi)
                    curvature[name] = m
                    old_witnesses[name] = dict(center_exact=list(map(str,center)),center_j=old['center_j'],
                        center_j_prime=old['center_j_prime'],gprime=cr(gp[name]),gsecond=cr(gpp[name]),
                        argument_radius_rational=str(width),full_curvature=guard,
                        full_curvature_canonical_sha256=canonical_sha(guard))
                active['saved_center_data'] = old_witnesses
                wa = widths['a']
                wsa = F(old_witnesses['a+s']['argument_radius_rational'])
                P0 = csub(cs(gp['a'],F(3,2)),gp['a+s'])
                Ps, Pa = cn(gpp['a+s']), csub(cs(gpp['a'],F(3,2)),gpp['a+s'])
                LP = ca(cm(Ps,cx(responses['s'])),cm(Pa,cx(responses['a'])))
                rhoP = norm(Ps)[0]*eta['s']+norm(Pa)[0]*eta['a']+(F(3,2)*curvature['a']*wa*wa+curvature['a+s']*wsa*wsa)/2
                UP, PW = signed_product(P0,LP,rhoP,responses['a'],eta['a'],
                                         H-centers['a'][1],delta,1)
                active['plane_marginal'] = dict(P0=cr(P0),Ds=cr(Ps),Da=cr(Pa),L=cr(LP),
                    rho_rational=str(rhoP),signed_product=PW)
                cut_data = {}
                for tau, name in zip(CUTS,('cut_left','cut_right')):
                    center = centers['a'][0]+tau, centers['a'][1]
                    distance = min(center[0]-wa,1-center[0]-wa)
                    cut = dict(name=name,tau_rational=str(tau),center_exact=list(map(str,center)),
                        full_argument_radius_rational=str(wa),distance_rational=str(distance))
                    active['cuts'].append(cut)
                    require(0 < distance <= F(1,2),'cut full correlated tube left original strip',dict(cut))
                    value = complex_ball(cx(center))
                    require(value.real > 0 and value.real < 1,'cut center strip',
                            dict(name=name,center=cr((ends(value.real),ends(value.imag)))))
                    sine_center = elementary('sine',pi*value)
                    require(sine_center.real > 0,'center log-sine original branch',
                            dict(name=name,center_exact=list(map(str,center)),sine=cr((ends(sine_center.real),ends(sine_center.imag)))))
                    jcut = elementary('logarithm',2*sine_center)
                    cot_center = elementary('cotangent',pi*value)
                    sine_distance = elementary('sine',pi*ar(distance))
                    require(sine_distance > 0,'cut curvature sine not positive',
                            dict(name=name,distance_rational=str(distance),sine=rec(ends(sine_distance))))
                    mball = pi*pi/(sine_distance*sine_distance)
                    m = ends(mball)[1]
                    gp_cut = ca((ends(jcut.real),ends(jcut.imag)),cm(ipi,cx((F(1,2)-center[0],-center[1]))))
                    gpp_cut = csub((mul(pi_bounds,ends(cot_center.real)),
                                    mul(pi_bounds,ends(cot_center.imag))),ipi)
                    D0 = ca(csub(ca(gp_cut,gp['a+s']),cs(gp['a'],3)),cs(ipi,2*tau))
                    Ds = gpp['a+s']
                    Da = csub(ca(gpp_cut,gpp['a+s']),cs(gpp['a'],3))
                    LD = ca(cm(Ds,cx(responses['s'])),cm(Da,cx(responses['a'])))
                    rhoD = norm(Ds)[0]*eta['s']+norm(Da)[0]*eta['a']+(
                        m*wa*wa+curvature['a+s']*wsa*wsa+3*curvature['a']*wa*wa)/2
                    UD, DW = signed_product(D0,LD,rhoD,responses['a'],eta['a'],
                                             H-centers['a'][1],delta,-1)
                    Dreal_width = RADIUS*norm(LD)[0]+rhoD
                    Dreal = D0[0][0]-Dreal_width,D0[0][1]+Dreal_width
                    cut.update(center_sine=dict(real=rec(ends(sine_center.real)),imag=rec(ends(sine_center.imag))),
                        center_j=dict(real=rec(ends(jcut.real)),imag=rec(ends(jcut.imag))),
                        center_cotangent=dict(real=rec(ends(cot_center.real)),imag=rec(ends(cot_center.imag))),
                        curvature_sine=rec(ends(sine_distance)),curvature_bound=rec(ends(mball)),
                        curvature_upper_rational=str(m),gprime=cr(gp_cut),gsecond=cr(gpp_cut),
                        D0=cr(D0),Ds=cr(Ds),Da=cr(Da),L=cr(LD),rho_rational=str(rhoD),
                        signed_product=DW,ReD=rec(Dreal),ReD_width_rational=str(Dreal_width))
                    cut_data[name] = dict(UD=UD,Dreal=Dreal,sigma=F(3,5) if tau==CUTS[0] else F(5,3))
                    active['pending_cuts'].remove(str(tau))

                Wfactor = mul(mul(pi_bounds,delta),delta)
                VW = sub(sub(sc(weighted['a'],3),weighted['s']),weighted['t'])
                VP = sub(sc(weighted['a'],F(3,2)),weighted['s'])
                mainW, planeW = mul(Wfactor,VW),mul(Wfactor,VP)
                active['integrated_values'] = dict(pi_delta_squared=rec(Wfactor),main_normalized=rec(VW),
                    main_W=rec(mainW),plane_normalized=rec(VP),plane_W=rec(planeW))
                budget_values = {}
                for kind in ('main','plane','cut_left','cut_right'):
                    for nu in (1,0):
                        order = ['kappa','Ia','Is']
                        parameters = [kappa,means['a'],means['s']]
                        if kind=='main':
                            order += ['It'];parameters += [means['t']]
                            trial = mainW[1]+(-2*pi_bounds[0]*H if nu else GH)
                            costs = dict(s=F(88,5),a=F(49,5)*(nu+1),t=F(22,5)*(3+epsilon))
                        elif kind=='plane':
                            trial = UP+planeW[1]+(-pi_bounds[0]*H if nu else GH/2)
                            costs = dict(s=F(88,5),a=F(49,10)*(nu+1))
                        else:
                            item = cut_data[kind]
                            order += ['Icut','ReD'];parameters += [means[kind],item['Dreal']]
                            Vcut = sub(sub(sc(weighted['a'],3),weighted['s']),weighted[kind])
                            Wcut = mul(Wfactor,Vcut)
                            trial = item['UD']+Wcut[1]+(-2*pi_bounds[0]*H if nu else GH)
                            costs = dict(s=F(88,5),a=F(49,5)*(nu+F(1,2)+item['sigma']))
                        if not nu:
                            order.append('Q');parameters.append(Q)
                        branch = dict(kind=kind,nu=nu,trial_upper_rational=str(trial),
                            parameter_order=order,parameter_intervals=list(map(rec,parameters)),
                            costs_rational={n:str(v) for n,v in costs.items()},vertices=[])
                        active['budgets'].append(branch)
                        for bits in product((0,1),repeat=len(parameters)):
                            point = dict(zip(order,(v[bit] for v,bit in zip(parameters,bits))))
                            k,ia,iss = point['kappa'],point['Ia'],point['Is']
                            forces = dict(s=k*(1-iss))
                            if kind=='main':
                                forces.update(a=k*(3*ia-iss-point['It']-1)+point.get('Q',F(0)),
                                              t=-k*(1+point['It']))
                            elif kind=='plane':
                                forces['a'] = k*(F(3,2)*ia-iss-F(1,2))+point.get('Q',F(0))/2
                            else:
                                forces['a'] = point['ReD']+k*(3*ia-iss-point['Icut']-1)+point.get('Q',F(0))
                            vertex = dict(endpoint_bits=list(bits),parameters_rational={n:str(v) for n,v in point.items()},
                                forces_rational={n:str(v) for n,v in forces.items()},gains={},independent_checks={})
                            branch['vertices'].append(vertex);counts['vertices'] += 1
                            total = F(0)
                            for name,K in costs.items():
                                center_interval = individual[name][0]
                                target = (F('.22'),F('.5') if name=='s' else F('.4') if name=='t' else F('.45'))
                                require(contained(target,center_interval),'gain reference center outside full target',
                                    dict(kind=kind,nu=nu,node=name,endpoint_bits=list(bits),
                                         force=rec(ex(forces[name])),center=rec(center_interval),
                                         target=rec(target),K_rational=str(K)))
                                upper,witness = gain.gain(ex(forces[name]),center_interval,target,K)
                                counts['scalar_cubic_gains'] += 1
                                verified,check = checker.check_gain(witness,ex(forces[name]),center_interval,target,K)
                                counts['independent_gain_checks'] += 1
                                assert verified == upper
                                vertex['gains'][name] = witness
                                vertex['independent_checks'][name] = dict(upper_rational=str(verified),check=check)
                                total += upper
                            vertex['gain_sum_upper_rational'] = str(total)
                            vertex['budget_upper_rational'] = str(trial+total)
                        maximum = max(F(v['budget_upper_rational']) for v in branch['vertices'])
                        branch['budget_upper_rational'] = str(maximum)
                        branch['attaining_vertices'] = [v['endpoint_bits'] for v in branch['vertices'] if F(v['budget_upper_rational'])==maximum]
                        budget_values[kind,nu] = maximum
                        active['pending_budgets'].remove([kind,nu])

                active['private_left_route'] = private_left_guards(individual) if epsilon else dict(available=False,reason='terminal type3')
                active['constant_reserve_rational'] = str(F(111,1000)+F(11,25)*individual['a'][1][0])
                def comparison(label,nu,options,association):
                    best = min(options.values())
                    active['comparisons'].append(dict(label=label,nu=nu,
                        upper_options_rational={n:str(v) for n,v in options.items()},
                        chosen_upper_rational=str(best),strictly_negative=best<0,
                        target_gap_passed=best < -GAP,source_association=association))
                    counts['required_comparisons'] += 1
                    active['pending_comparisons'].remove([label,nu])
                for nu in (1,0):
                    comparison('main',nu,dict(main=budget_values['main',nu]),None)
                    comparison('constant',nu,dict(plane=budget_values['plane',nu]-F(active['constant_reserve_rational'])),None)
                for label in alias['alias_labels']:
                    assert label['complete_finite_coverage']
                    reserve = F(label['allocated_reserve_rational'])
                    assert reserve == -F(label['uniform_bare_upper_rational'])-F(41,1000)
                    for nu in (1,0):
                        comparison('alias:'+label['t_state']+':'+label['private_state'],nu,
                            dict(plane=budget_values['plane',nu]-reserve),
                            dict(source_label_canonical_sha256=canonical_sha(label),label=label))
                for family in face['families']:
                    assert family['complete_finite_coverage'] and not family['null_jobs_unresolved']
                    bare = F(family['uniform_bare_upper_rational'])
                    assert bare == max(F(j['decoded_upper_rational']) for j in family['contributing_jobs'])
                    f = family['family']
                    cut_kind = ('cut_right' if family['series']=='three_half' or f==20 else
                                'cut_left' if f in (0,4,5) else 'cut_right' if f in (1,6,7) else None)
                    for nu in (1,0):
                        options = dict(plane=budget_values['plane',nu]+bare)
                        if cut_kind:
                            options['direct'] = budget_values[cut_kind,nu]+bare
                            counts['direct_alternatives'] += 1
                        if epsilon and f==2 and active['private_left_route']['available']:
                            options['private_left_transfer'] = budget_values['main',nu]+bare
                            counts['private_left_alternatives'] += 1
                        comparison(family['series']+':'+str(f),nu,options,
                            dict(source_family_canonical_sha256=canonical_sha(family),
                                 bare_upper_rational=str(bare),source_family=family))
                assert len(active['comparisons']) == 54
                assert not active['pending_height_nodes'] and not active['pending_cuts'] and not active['pending_budgets']
                assert not active['pending_comparisons']
                active['status'] = 'all fixed comparisons enclosed'
                active['worst_upper_rational'] = str(max(F(c['chosen_upper_rational']) for c in active['comparisons']))
                counts['completed_cases'] += 1
                out['pending_cases'].remove(dict(beta=0,epsilon=epsilon))
            except Inconclusive as exc:
                active['status'] = 'inconclusive fixed protocol'
                active['error'] = dict(type=type(exc).__name__,message=str(exc),operands=exc.operands)
                out['pending_cases'].remove(dict(beta=0,epsilon=epsilon))
            print(json.dumps(dict(epsilon=epsilon,status=active['status'],
                comparisons=len(active['comparisons']))),flush=True)
            active = None
        for key,maximum in LIMITS.items():
            assert counts[key] <= maximum,(key,counts[key],maximum)
        complete = counts['completed_cases']==2
        out['status'] = 'completed fixed protocol' if complete else 'completed with inconclusive cases'
        out['all_108_comparisons_enclosed'] = complete
        if complete:
            for key in LIMITS:
                if key != 'private_left_alternatives':
                    assert counts[key] == LIMITS[key],(key,counts[key],LIMITS[key])
            assert counts['height_slabs'] == 32
            comparisons = [c for row in out['cases'] for c in row['comparisons']]
            worst = max(F(c['chosen_upper_rational']) for c in comparisons)
            out.update(all_108_negative=worst<0,target_gap_proved=worst < -GAP,
                       worst_upper_rational=str(worst),common_margin_rational=str(-worst) if worst<0 else None)
    except (Exception,KeyboardInterrupt) as exc:
        fatal = exc
        out['status'] = 'failed fixed protocol'
        out['error'] = dict(type=type(exc).__name__,message=str(exc),
                            operands=getattr(exc,'operands',None))
        if active is not None:
            active['status'] = out['status'];active['error'] = out['error']
    out['changed_inputs'] = [name for name,digest in inputs.items()
        if not (ROOT/name).is_file() or sha(ROOT/name)!=digest]
    if out['changed_inputs'] or fatal is not None:
        out['all_108_comparisons_enclosed'] = out['all_108_negative'] = out['target_gap_proved'] = False
    if out['changed_inputs']:
        out['status'] = 'changed inputs'
    out['proof_sha256'],out['driver_sha256'] = inputs.get(PROOF),inputs[own]
    args.output.parent.mkdir(parents=True,exist_ok=True)
    with args.output.open('xb') as raw:
        with gzip.GzipFile(filename='',fileobj=raw,mode='wb',compresslevel=1,mtime=0) as gz:
            with io.TextIOWrapper(gz,encoding='utf-8',newline='\n') as stream:
                json.dump(out,stream,separators=(',',':'));stream.write('\n')
    print(json.dumps(dict(status=out['status'],counts=counts,target_gap_proved=out['target_gap_proved'],
                         output_sha256=sha(args.output))),flush=True)
    if fatal is not None:
        raise fatal
    if out['changed_inputs']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
