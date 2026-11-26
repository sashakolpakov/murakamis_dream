#!/usr/bin/env python3
"""One saved-only correlated selected-force test for beta=epsilon=1.

Analytic endpoints, original canonical existence and zero lifts are inherited.
Only exact interval arithmetic, 32 cotangent vertices and integer square roots
are used. The frozen standard-library audit helper is imported without main().
"""
import argparse
from fractions import Fraction as F
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
PROOF = 'notes/research_mixed_terminal_stationary_force_transport.md'
INTEGRAL = 'repro/results/research-mixed-terminal-four-input-integral-budget.json'
AUDIT = 'repro/results/research-mixed-terminal-four-input-integral-budget-saved-audit.json'
HELPER = 'experiments/check_mixed_terminal_four_input_integral_budget.py'
REFINED = 'repro/results/research-mixed-terminal-quadratic-residual-refinement.json'
POSTERIOR = 'repro/results/research-mixed-terminal-split-taylor-completion.json'
SPLIT = 'repro/results/research-mixed-terminal-split-taylor-inclusion.json'
AFFINE = 'repro/results/research-mixed-terminal-correlated-affine-family.json'
CENTER = 'repro/results/research-mixed-terminal-horizontal-envelope-diagnostic.json'
CENTER_AUDIT = 'repro/results/research-mixed-terminal-horizontal-envelope-saved-audit.json'
FORCES = 'repro/results/research-mixed-terminal-joint-main-budget-diagnostic.json'
FORCE_AUDIT = 'repro/results/research-mixed-terminal-joint-main-budget-saved-audit.json'
PINNED = {
    PROOF: '3a04a594cf8a81c4ceb9225e5e37262c0f24dc7ccbb2183f5b64d94d3d1531ce',
    INTEGRAL: '9831e8bdbc884cfc0b0c99dbc7f92245403988ae7dc4bbbba86b5606c5a1575e',
    AUDIT: 'cda9eef92856387d0ec0dccca6311512bb980034a07832ab89a99a7bc733d6c3',
    HELPER: 'd38f41d186bf31d3255861c45cb0500d1a21a4eb1bfd4d366c6a956efc614bf4',
    REFINED: '2834576c2a443c9ffd24032277b5f253d9a85eac17d3f754905812e822a9a331',
    POSTERIOR: 'e04521450e1973658cbd602aa0a8f54d4c7d40c968b4b90d65374d570981c617',
    SPLIT: 'a25587e526dc753306eb690b76f1f07d0d05410be315c6675023bd87ae42e202',
    AFFINE: '51b702aa6ea44aa5891bc1146a7d5c0d22686cd814f9bbe5d9c4c63b9a16f9e1',
    CENTER: 'ca58c35640f1e2894f35b0f2c841029ff28b1c4af8411c1a12da012ace09059b',
    CENTER_AUDIT: 'bedf680b3f57c799980517f7aa6178a7f9c5a0890bac8528947e9018baf7a4de',
    FORCES: '2b6e9b17d1a16071c545c0ba9f9bb2502e1f18c5009fafc1212fd326d2a621f9',
    FORCE_AUDIT: 'fceffb2a2bfe677579bb6ff94087b5129c9db0daf8f85674b94ee6de7fa3dda6',
    'notes/research_mixed_terminal_quadratic_residual_refinement.md':
        'f012610187e14b824fdfeea730bc71ffde1660687ffbdcc491bc945c6a54d596',
    'experiments/check_mixed_terminal_quadratic_residual_refinement.py':
        '251fc4b3c656201ab5451287577baddb4d4be8122ff34a1318078de0f8501a05',
}
NAMES = ('e', 'xi', 't', 'a', 's')
H, R = F(1, 100), F(8, 125)


def sha(path):
    digest = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1048576), b''):
            digest.update(block)
    return digest.hexdigest()


def canonical_sha(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True,
        separators=(',', ':')).encode()).hexdigest()


def ir(value):
    assert value[0] <= value[1]
    return dict(finite=True, lower_rational=str(value[0]), upper_rational=str(value[1]))


def ca(x, y):
    return x[0]+y[0], x[1]+y[1]


def cs(x, a):
    return x[0]*a, x[1]*a


def times_i(x):
    return -x[1], x[0]


def square_norm(x):
    return x[0]*x[0]+x[1]*x[1]


def gain(h, force, center):
    """The unchanged three-piece moving-center enclosure, selected node only."""
    L, R = F('.22'), F('.45')
    K = F(98, 5)
    assert L <= center[0] <= center[1] <= R
    d, p, q = F('.5')-center[1], max(F(0), -force[0]), max(F(0), force[1])
    assert d > 0
    lower_length, upper_length = center[1]-L, R-center[0]
    branches = []

    def save(name, domain, coeff, radicand, root, optimizer, decision):
        branches.append(dict(name=name, domain=ir(domain), coefficients_rational=list(map(str, coeff)),
            radicand_rational=None if radicand is None else str(radicand),
            square_root=None if root is None else ir(root), optimizer=ir(optimizer),
            value=ir(h.polynomial(coeff, optimizer)), decision=decision))

    radicand = d*d+2*p/K
    root = h.sqroot(radicand)
    point = h.clip(h.sub(root, (d, d)), F(0), lower_length)
    save('negative displacement', (F(0), lower_length), (F(0), p, -K*d/2, -K/6),
         radicand, root, point, 'clipped unique maximum')
    top = min(upper_length, d)
    if q >= K*d*d/2:
        save('positive displacement below d', (F(0), top), (F(0), q, -K*d/2, K/6),
             None, None, (top, top), 'q >= K*d^2/2: right endpoint')
    else:
        radicand = d*d-2*q/K
        root = h.sqroot(radicand)
        point = h.clip(h.sub((d, d), root), F(0), top)
        save('positive displacement below d', (F(0), top), (F(0), q, -K*d/2, K/6),
             radicand, root, point, 'clipped smaller root')
    if upper_length > d:
        radicand = q/K
        root = h.sqroot(radicand)
        point = h.clip(root, d, upper_length)
        save('positive displacement above d', (d, upper_length), (F(0), q, F(0), -K/3),
             radicand, root, point, 'actual d >= displacement: cubic cost K*v^3/3')
    upper = max(F(0), *(F(b['value']['upper_rational']) for b in branches))
    result = dict(force=ir(force), center=ir(center), target=ir((L, R)), K_rational=str(K),
        d_rational=str(d), p_rational=str(p), q_rational=str(q), branches=branches,
        upper_rational=str(upper))
    assert h.check_gain(result, force, center, (L, R), K)[0] == upper
    return upper, result


def verify(bindings):
    paths = (INTEGRAL, AUDIT, REFINED, POSTERIOR, SPLIT, AFFINE,
             CENTER, CENTER_AUDIT, FORCES, FORCE_AUDIT)
    for path, digest in bindings.items():
        assert sha(ROOT/path) == digest, path
    records = {p: json.loads((ROOT/p).read_text()) for p in paths}
    for data in records.values():
        if 'changed_inputs' in data:
            assert data['changed_inputs'] == []
        for key in ('input_sha256', 'dependencies_sha256'):
            for path, digest in data.get(key, {}).items():
                assert path not in bindings or bindings[path] == digest, path
                assert sha(ROOT/path) == digest, path
                bindings[path] = digest
    integral, audit, refined, posterior, split, affine, center, center_audit, forces, force_audit = [
        records[p] for p in paths]
    assert integral['status'] == 'completed fixed protocol' and integral['all_four_budgets_enclosed']
    assert audit['status'] == 'passed' and audit['source_path'] == INTEGRAL
    assert audit['source_sha256'] == bindings[INTEGRAL] and audit['checker_sha256'] == bindings[HELPER]
    assert refined['status'] == 'completed fixed saved-only protocol'
    assert refined['source_path'] == POSTERIOR and refined['source_sha256'] == bindings[POSTERIOR]
    assert refined['checker_sha256'] == bindings['experiments/check_mixed_terminal_quadratic_residual_refinement.py']
    assert posterior['status'] == 'passed' and posterior['all_four_input_disks_certified']
    assert posterior['source_path'] == SPLIT and posterior['source_sha256'] == bindings[SPLIT]
    assert split['source_path'] == AFFINE and split['source_sha256'] == bindings[AFFINE]
    assert center_audit['status'] == force_audit['status'] == 'passed'
    assert center_audit['source_path'] == CENTER and center_audit['source_sha256'] == bindings[CENTER]
    assert force_audit['source_path'] == FORCES and force_audit['source_sha256'] == bindings[FORCES]
    assert force_audit['certified_reference_associations_checked'] == 4

    row, old, new = integral['cases'][1], posterior['posterior_enclosures'][3], refined['cases'][3]
    scase, acase, anchor, fcase = split['cases'][3], affine['cases'][3], center['cases'][3], forces['cases'][3]
    for case in (row, old, new, scase, acase, anchor, fcase):
        assert (case['beta'], case['epsilon']) == (1, 1)
    assert row['source_entry_canonical_sha256'] == new['source_posterior_canonical_sha256'] == canonical_sha(old)
    assert old['source_case_canonical_sha256'] == new['split_case_canonical_sha256'] == canonical_sha(scase)
    assert scase['source_case_canonical_sha256'] == new['affine_case_canonical_sha256'] == canonical_sha(acase)
    scandidate = next(c for c in scase['candidates'] if F(c['multiplier_rational']) == 1)
    acandidate = next(c for c in acase['candidates'] if F(c['multiplier_rational']) == 1)
    assert old['source_candidate_canonical_sha256'] == canonical_sha(scandidate)
    assert scandidate['source_candidate_canonical_sha256'] == canonical_sha(acandidate)
    assert scandidate['criterion_pass'] is True
    assert acase['canonical_reference_case_sha256'] == fcase['source_case_sha256'] == canonical_sha(anchor)
    assert fcase['source_index'] == 3 and anchor['canonical_reference_certified'] is True
    assert F(forces['height_rational']) == F(fcase['height_rational']) == H
    assert old['exact_linear_system_verified'] and new['exact_linear_system_verified']
    assert F(old['multiplier_rational']) == F(new['multiplier_rational']) == 1
    for key in ('center_exact', 'response_exact', 'parameter_center', 'parameter_radius_rational'):
        assert row[key] == new[key] == old[key]
    assert old['center_exact'] == scase['original_center'] == acase['center']
    assert old['response_exact'] == scase['original_response'] == acase['response_exact']
    assert tuple(map(F, old['parameter_center'])) == (F('.30'), -F('.052'))
    assert F(old['parameter_radius_rational']) == R
    assert row['posterior_radii_rational'] == new['old_posterior_radii_rational'] == old['posterior_radii_rational']

    spec = importlib.util.spec_from_file_location('frozen_saved_integral_arithmetic', ROOT/HELPER)
    h = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(h)  # Standard-library definitions only; no main().
    q0 = dict(zip(NAMES, [tuple(map(F, z)) for z in old['center_exact']]))
    u = dict(zip(NAMES, [tuple(map(F, z)) for z in old['response_exact']]))
    eta_old = dict(zip(NAMES, map(F, old['posterior_radii_rational'])))
    eta = dict(zip(NAMES, map(F, new['posterior_radii_rational'])))
    assert all(0 <= eta[n] <= eta_old[n] for n in NAMES)
    assert all(tuple(map(F, anchor['proposed_centers'][n])) == q0[n] for n in NAMES)
    assert fcase['saved_coordinate_enclosures'] == anchor['coordinate_enclosures']
    anchor_errors, anchor_boxes = {}, {}
    for name in NAMES:
        box = anchor['coordinate_enclosures'][name]
        displacements = [max(abs(x-q0[name][j]) for x in h.iv(box[part]))
                         for j, part in enumerate(('real', 'imag'))]
        squared = sum(x*x for x in displacements)
        norm = h.sqroot(squared)
        assert norm[1] <= eta_old[name]
        anchor_errors[name] = displacements[0] if name == 'a' else norm[1]
        anchor_boxes[name] = dict(box=box, center_exact=list(map(str, q0[name])),
            component_displacement_bounds_rational=list(map(str, displacements)),
            squared_complex_displacement_rational=str(squared), complex_displacement=ir(norm),
            used_force_error_rational=str(anchor_errors[name]))

    assert row['status'] == 'enclosed both full-P branches' and all(row['domain_guards'].values())
    slab = row['slabs'][15]
    assert slab['index'] == 15 and h.iv(slab['theta']) == (F(15, 16), F(1))
    # Explicitly verify that the saved last slab contains the entire OLD
    # lifted affine/error tube at theta=1; the new errors are smaller.
    lifted_supports = {}
    for name in ('a', 's', 't'):
        if name == 'a':
            width = R*h.sqroot(square_norm(u['a']))[1]+eta_old['a']
            real = q0['a'][0]-width, q0['a'][0]+width
            imag = H, H
        else:
            coefficient = ca(u[name], u['a'])
            width = R*h.sqroot(square_norm(coefficient))[1]+eta_old[name]+eta_old['a']
            mid = q0[name][0]+q0['a'][0]
            real = mid-width, mid+width
            iwidth = R*h.sqroot(square_norm(u[name]))[1]+eta_old[name]
            imag = q0[name][1]+H-iwidth, q0[name][1]+H+iwidth
        node = slab['nodes'][name]
        for part, value in (('real', real), ('imag', imag)):
            outer = h.iv(node[part])
            assert outer[0] <= value[0] <= value[1] <= outer[1]
        assert 0 < real[0] <= real[1] < 1
        lifted_supports[name] = dict(real=ir(real), imag=ir(imag))
    cot = {name: {part: h.iv(node['cotangent'][part]) for part in ('real', 'imag')}
           for name, node in slab['nodes'].items()}
    variable_intervals = (cot['s']['real'], cot['s']['imag'], cot['t']['real'],
                          cot['t']['imag'], cot['a']['real'])
    vertices = []
    for bits in itertools.product((0, 1), repeat=5):
        Cs, Is, Ct, It, Ca = [x[b] for x, b in zip(variable_intervals, bits)]
        value = ca(cs(ca(u['s'], u['a']), Cs), cs(times_i(u['s']), Is))
        value = ca(value, ca(cs(ca(u['t'], u['a']), Ct), cs(times_i(u['t']), It)))
        value = ca(value, ca(cs(u['a'], -3*Ca), times_i(ca(u['t'], cs(u['s'], -1)))))
        vertices.append(dict(bits=list(bits), cot_components_rational=list(map(str, (Cs, Is, Ct, It, Ca))),
            P_over_pi_exact=list(map(str, value)), squared_modulus_rational=str(square_norm(value))))
    assert len(vertices) == 32
    P_square = max(F(v['squared_modulus_rational']) for v in vertices)
    P = h.sqroot(P_square)
    S_square = max(x*x+(y-1)**2 for x in cot['s']['real'] for y in cot['s']['imag'])
    T_square = max(x*x+(y+1)**2 for x in cot['t']['real'] for y in cot['t']['imag'])
    S, T = h.sqroot(S_square), h.sqroot(T_square)
    A = max(abs(x+y-3*z) for x in cot['s']['real'] for y in cot['t']['real'] for z in cot['a']['real'])
    pi = h.iv(integral['constants']['pi'])
    assert F(157, 50) < pi[0] <= pi[1] < F(22, 7)
    affine_cost = R*P[1]
    posterior_cost = eta['s']*S[1]+eta['t']*T[1]+eta['a']*A
    anchor_cost = anchor_errors['s']*S[1]+anchor_errors['t']*T[1]+anchor_errors['a']*A
    B = pi[1]*(affine_cost+posterior_cost+anchor_cost)
    assert [b['nu'] for b in fcase['branches']] == [1, 0]
    F0 = h.iv(fcase['branches'][0]['force_a'])
    transported = F0[0]-B, F0[1]+B
    old_force = h.iv(row['forces']['a_factorial'])
    chosen = max(transported[0], old_force[0]), min(transported[1], old_force[1])
    assert chosen[0] <= chosen[1], 'inconsistent force enclosures'
    assert [b['nu'] for b in row['branches']] == [1, 0]
    branch = row['branches'][0]
    center_interval = h.iv(row['individual_supports']['a']['real'])
    old_Ga, _ = h.check_gain(branch['selected_gain'], old_force, center_interval,
                             (F('.22'), F('.45')), F(98, 5))
    new_Ga, gain_record = gain(h, chosen, center_interval)
    Gs = F(row['shared_gains']['s']['upper_rational'])
    Gt = F(row['shared_gains']['t']['upper_rational'])
    trial = F(branch['trial_upper_rational'])
    old_budget = trial+Gs+Gt+old_Ga
    assert old_budget == F(branch['budget_upper_rational'])
    audit_branch = audit['cases'][1]['branches'][0]
    assert audit_branch['nu'] == 1 and F(audit_branch['budget_upper_rational']) == old_budget
    new_budget = trial+Gs+Gt+new_Ga
    selected_budget = min(old_budget, new_budget)
    return dict(beta=1, epsilon=1, nu=1, source_posterior_entry_sha256=canonical_sha(old),
        refined_case_sha256=canonical_sha(new), integral_case_sha256=canonical_sha(row),
        original_force_case_sha256=canonical_sha(fcase), original_reference_case_sha256=canonical_sha(anchor),
        original_root_anchor=anchor_boxes, old_lifted_tube_supports=lifted_supports,
        smaller_errors_contained_in_old_tube=True, saved_last_slab_cotangents=slab['nodes'],
        vertices=vertices, vertex_count=32, P_squared_max_rational=str(P_square), P_over_pi=ir(P),
        S_squared_max_rational=str(S_square), S_over_pi=ir(S),
        T_squared_max_rational=str(T_square), T_over_pi=ir(T), A_over_pi_upper_rational=str(A),
        affine_cost_over_pi_rational=str(affine_cost), posterior_cost_over_pi_rational=str(posterior_cost),
        anchor_cost_over_pi_rational=str(anchor_cost), total_force_radius_rational=str(B),
        anchor_force=ir(F0), transported_force=ir(transported), old_integral_force=ir(old_force),
        intersected_force=ir(chosen), selected_gain=gain_record,
        unchanged_trial_upper_rational=str(trial), unchanged_s_gain_upper_rational=str(Gs),
        unchanged_t_gain_upper_rational=str(Gt), old_selected_gain_upper_rational=str(old_Ga),
        new_selected_gain_upper_rational=str(new_Ga), old_budget_upper_rational=str(old_budget),
        new_budget_upper_rational=str(new_budget), retained_budget_upper_rational=str(selected_budget),
        strict_improvement=new_budget < old_budget, remaining_factorial_sign_proved=selected_budget < 0)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    if hasattr(sys, 'set_int_max_str_digits'):
        sys.set_int_max_str_digits(0)
    bindings = dict(PINNED)
    own = Path(__file__).resolve().relative_to(ROOT).as_posix()
    bindings[own] = sha(ROOT/own)
    result = dict(status='checking', proof_path=PROOF, proof_sha256=bindings[PROOF],
        checker_sha256=bindings[own], input_sha256=bindings, analytic_callbacks=0,
        original_primitives=0, root_solves=0, parameter_subdivisions=0, retries=0,
        original_reference_certification_inherited=True, existing_cotangent_enclosures_inherited=True,
        finite_source_theorem_proved=False, global_knot_theorem_proved=False)
    error = None
    try:
        result['case'] = verify(bindings)
        result['changed_inputs'] = [n for n, d in bindings.items() if sha(ROOT/n) != d]
        assert result['changed_inputs'] == []
        result['status'] = 'completed fixed saved-only protocol'
    except Exception as exc:
        error = exc
        result['status'] = 'failed saved-data verification'
        result['error'] = dict(type=type(exc).__name__, message=str(exc))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open('x', encoding='utf-8') as stream:
        json.dump(result, stream, separators=(',', ':'))
        stream.write('\n')
    print(json.dumps(dict(status=result['status'], bindings=len(bindings),
        remaining_factorial_sign_proved=result.get('case', {}).get('remaining_factorial_sign_proved'),
        output_sha256=sha(args.output))))
    if error is not None:
        raise error


if __name__ == '__main__':
    main()
