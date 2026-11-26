#!/usr/bin/env python3
"""Exact saved-only audit of the fixed whole-D4 integral budgets.

Analytic cotangent/exp/trigonometric/logarithm endpoints are inherited
from the pinned interval run. This checker makes no analytic calls.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from math import isqrt
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SOURCE = 'repro/results/research-mixed-terminal-four-input-integral-budget.json'
DRIVER = 'experiments/certify_mixed_terminal_four_input_integral_budget.py'
PROOF = 'notes/research_mixed_terminal_four_input_integral_budget.md'
POSTERIOR = 'repro/results/research-mixed-terminal-split-taylor-completion.json'
SPLIT = 'repro/results/research-mixed-terminal-split-taylor-inclusion.json'
AFFINE = 'repro/results/research-mixed-terminal-correlated-affine-family.json'
PINNED = {
    SOURCE: '9831e8bdbc884cfc0b0c99dbc7f92245403988ae7dc4bbbba86b5606c5a1575e',
    DRIVER: '3b806591d88cd461ab7764a6f9c704a048d9c33edb88834a32dbc59a99c91388',
    PROOF: '90ec6c9d4b3641a01e789b64dd0d26053b402c2914b99cafe81eff8ad4265cb9',
    POSTERIOR: 'e04521450e1973658cbd602aa0a8f54d4c7d40c968b4b90d65374d570981c617',
    SPLIT: 'a25587e526dc753306eb690b76f1f07d0d05410be315c6675023bd87ae42e202',
    AFFINE: '51b702aa6ea44aa5891bc1146a7d5c0d22686cd814f9bbe5d9c4c63b9a16f9e1',
}
NAMES = ('e', 'xi', 't', 'a', 's')
H, R = F(1, 100), F(8, 125)
Z, O = (F(0), F(0)), (F(1), F(1))


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
    assert value['finite'] is True
    lo, hi = F(value['lower_rational']), F(value['upper_rational'])
    assert lo <= hi
    return lo, hi


def rec(value):
    return dict(lower_rational=str(value[0]), upper_rational=str(value[1]))


def add(x, y):
    return x[0]+y[0], x[1]+y[1]


def neg(x):
    return -x[1], -x[0]


def sub(x, y):
    return add(x, neg(y))


def mul(x, y):
    v = [a*b for a in x for b in y]
    return min(v), max(v)


def sc(x, a):
    return mul(x, (F(a), F(a)))


def polynomial(coefficients, x):
    value = Z
    for c in reversed(coefficients):
        value = add(mul(value, x), (c, c))
    return value


def sqroot(x):
    assert x >= 0
    n = isqrt((x.numerator << 480)//x.denominator)
    lo = F(n, 1 << 240)
    hi = lo if lo*lo == x else F(n+1, 1 << 240)
    assert lo*lo <= x <= hi*hi
    return lo, hi


def clip(x, lo, hi):
    assert lo <= hi
    return tuple(min(hi, max(lo, t)) for t in x)


def modulus(z, saved):
    assert tuple(map(F, saved['coefficient'])) == z
    square = sum(x*x for x in z)
    assert F(saved['squared_modulus_rational']) == square
    value = sqroot(square)
    assert iv(saved['modulus']) == value
    return value[1]


def check_gain(saved, force, center, target, K):
    assert iv(saved['force']) == force and iv(saved['center']) == center
    assert iv(saved['target']) == target and F(saved['K_rational']) == K
    assert F('.18') <= target[0] <= center[0] <= center[1] <= target[1] <= F('.5')
    d, p, q = F('.5')-center[1], max(F(0), -force[0]), max(F(0), force[1])
    assert d > 0
    assert [F(saved[k]) for k in ('d_rational', 'p_rational', 'q_rational')] == [d, p, q]
    umax, vmax = center[1]-target[0], target[1]-center[0]
    cases = []
    rad = d*d+2*p/K
    root = sqroot(rad)
    cases.append(('negative displacement', (F(0), umax), (F(0), p, -K*d/2, -K/6),
                  rad, root, clip(sub(root, (d, d)), F(0), umax), 'clipped unique maximum'))
    top = min(vmax, d)
    if q >= K*d*d/2:
        cases.append(('positive displacement below d', (F(0), top), (F(0), q, -K*d/2, K/6),
                      None, None, (top, top), 'q >= K*d^2/2: right endpoint'))
    else:
        rad = d*d-2*q/K
        root = sqroot(rad)
        cases.append(('positive displacement below d', (F(0), top), (F(0), q, -K*d/2, K/6),
                      rad, root, clip(sub((d, d), root), F(0), top), 'clipped smaller root'))
    if vmax > d:
        rad = q/K
        root = sqroot(rad)
        cases.append(('positive displacement above d', (d, vmax), (F(0), q, F(0), -K/3),
                      rad, root, clip(root, d, vmax), 'actual d >= displacement: cubic cost K*v^3/3'))
    assert len(saved['branches']) == len(cases)
    upper = F(0)
    for item, (name, domain, coefficients, rad, root, optimizer, decision) in zip(saved['branches'], cases):
        assert item['name'] == name and item['decision'] == decision
        assert iv(item['domain']) == domain
        assert tuple(map(F, item['coefficients_rational'])) == coefficients
        assert item['radicand_rational'] == (None if rad is None else str(rad))
        assert (None if item['square_root'] is None else iv(item['square_root'])) == root
        assert iv(item['optimizer']) == optimizer
        value = polynomial(coefficients, optimizer)
        assert iv(item['value']) == value
        upper = max(upper, value[1])
    assert F(saved['upper_rational']) == upper
    return upper, len(cases)


def verify(inputs):
    source, posterior, split, affine = [json.loads((ROOT/p).read_text())
                                       for p in (SOURCE, POSTERIOR, SPLIT, AFFINE)]
    for data in (source, posterior, split, affine):
        assert data['changed_inputs'] == []
        for key in ('input_sha256', 'dependencies_sha256'):
            for path, digest in data.get(key, {}).items():
                assert path not in inputs or inputs[path] == digest
                assert sha(ROOT/path) == digest, path
                inputs[path] = digest
    assert source['status'] == 'completed fixed protocol' and source['all_four_budgets_enclosed']
    assert source['precision_bits'] == 256 and source['square_root_bits'] == 240
    assert source['proof_sha256'] == inputs[PROOF] and source['source_sha256'] == inputs[POSTERIOR]
    assert source['fallback'] == 'none' and source['uniform_main_phase_gap_proved'] is False
    assert not source['uniform_finite_source_gap_proved'] and not source['global_knot_theorem_proved']
    assert source['counts'] == dict(reference_data_cases=2, height_slabs=32,
        cotangent=96, pi=1, exponential=1, cosine=2, sine=2, logarithm=5, cubic_gains=8,
        roots=0, inverses=0, optimizers=0, original_primitives=0, source_evaluations=0,
        parameter_subdivisions=0, retries=0)
    pi = iv(source['constants']['pi'])
    assert F(157, 50) < pi[0] <= pi[1] < F(22, 7)
    exp_height, log_two = iv(source['constants']['exp_2piH']), iv(source['constants']['log_two'])
    assert exp_height[0] > 1 and log_two[0] > 0
    assert [(c['beta'], c['epsilon']) for c in source['cases']] == [(1, 0), (1, 1)]
    report, all_budgets = [], []
    total_moduli = total_cubics = 0
    for row, p in zip(source['cases'], posterior['posterior_enclosures'][2:]):
        epsilon = row['epsilon']
        assert (p['beta'], p['epsilon']) == (1, epsilon)
        assert row['status'] == 'enclosed both full-P branches'
        assert row['source_entry_canonical_sha256'] == canonical_sha(p)
        ss, oo = split['cases'][2+epsilon], affine['cases'][2+epsilon]
        ss1 = next(c for c in ss['candidates'] if F(c['multiplier_rational']) == 1)
        oo1 = next(c for c in oo['candidates'] if F(c['multiplier_rational']) == 1)
        assert p['source_case_canonical_sha256'] == canonical_sha(ss)
        assert ss['source_case_canonical_sha256'] == canonical_sha(oo)
        assert p['source_candidate_canonical_sha256'] == canonical_sha(ss1)
        assert ss1['source_candidate_canonical_sha256'] == canonical_sha(oo1)
        for key in ('source_case_canonical_sha256', 'source_candidate_canonical_sha256',
                    'center_exact', 'response_exact', 'posterior_radii_rational',
                    'parameter_center', 'parameter_radius_rational'):
            assert row[key] == p[key]
        assert tuple(map(F, p['parameter_center'])) == (F('.30'), -F('.052'))
        assert F(p['parameter_radius_rational']) == R and F(p['multiplier_rational']) == 1
        q0 = dict(zip(NAMES, [tuple(map(F, x)) for x in p['center_exact']]))
        u = dict(zip(NAMES, [tuple(map(F, x)) for x in p['response_exact']]))
        error = dict(zip(NAMES, map(F, p['posterior_radii_rational'])))
        assert all(0 <= x < F(y) for x, y in zip(error.values(), p['original_radii_rational']))
        coordinates, widths = {}, {}
        for name in NAMES:
            saved = row['individual_supports'][name]
            m = modulus(u[name], saved['modulus_witness']); total_moduli += 1
            width = R*m+error[name]
            assert F(saved['error_radius_rational']) == error[name]
            assert F(saved['width_rational']) == width
            widths[name] = width
            coordinates[name] = tuple((x-width, x+width) for x in q0[name])
            assert iv(saved['real']) == coordinates[name][0] and iv(saved['imag']) == coordinates[name][1]
        real = {'a': coordinates['a'][0]}
        for name in ('s', 't'):
            saved = row['shared_real_supports'][name]
            coeff = tuple(u[name][j]+u['a'][j] for j in range(2))
            m = modulus(coeff, saved['modulus_witness']); total_moduli += 1
            width = R*m+error[name]+error['a']
            center = q0[name][0]+q0['a'][0]
            real[name] = center-width, center+width
            assert F(saved['width_rational']) == width and iv(saved['interval']) == real[name]
        def inside(name, k, lo, hi):
            x = coordinates[name][k]
            return F(lo) <= x[0] <= x[1] <= F(hi)
        guards = dict(
            ordinary_real=inside('s',0,'.24','.36'), ordinary_height=inside('s',1,'-.102','-.001'),
            selected_real=inside('a',0,'.22','.45'), selected_height=inside('a',1,'-.108','0'),
            terminal_real=inside('t',0,'.22','.4'), cubic_terminal_height=inside('t',1,'-.108','.108'),
            terminal_original_height=inside('t',1,'-.108' if epsilon else '-.072','-.020' if epsilon else '.021'),
            private_real=inside('e' if epsilon else 'xi',0,'.27' if epsilon else '.1','.49' if epsilon else '.4'),
            private_original_height=inside('e' if epsilon else 'xi',1,'-.051' if epsilon else '.049','-.019' if epsilon else '.077'),
            positive_delta=coordinates['a'][1][1] < H,
            positive_log_sine=F(1,6) < coordinates['a'][0][0] <= coordinates['a'][0][1] < F(1,2),
            external_full_input_barrier=F('-.12') <= F('-.052')-R and F('-.052')+R <= F('.08'),
            external_pair_height=max(abs(F('-.052')-R),abs(F('-.052')+R)) <= F('.12'),
            external_reference_real=F('.22') <= F('.30')-R and F('.30')+R <= F('.45'))
        assert row['domain_guards'] == guards and all(guards.values())
        assert len(row['slabs']) == 16
        totals = {k: Z for k in ('V', 'S', 'T', 'A')}
        means = {k: Z for k in ('a', 's', 't')}
        for j, slab in enumerate(row['slabs']):
            assert slab['index'] == j and iv(slab['theta']) == (F(j,16),F(j+1,16))
            weight, weighted = F(1,16), F(31-2*j,512)
            assert F(slab['weight_rational']) == weight and F(slab['weighted_rational']) == weighted
            assert set(slab['nodes']) == {'a','s','t'}
            C, I = {}, {}
            for name, node in slab['nodes'].items():
                endpoint_images = []
                assert len(node['endpoint_supports']) == 2
                for theta, saved in zip((F(j,16),F(j+1,16)),node['endpoint_supports']):
                    assert saved['node'] == name and F(saved['theta_rational']) == theta
                    if name == 'a':
                        midpoint = (1-theta)*q0['a'][1]+theta*H
                        width = (1-theta)*widths['a']
                        assert saved['modulus_witness'] is None
                    else:
                        coeff = tuple(u[name][k]+(1-theta)*u['a'][k] for k in range(2))
                        m = modulus(coeff,saved['modulus_witness']); total_moduli += 1
                        midpoint = q0[name][1]+(1-theta)*q0['a'][1]+theta*H
                        width = R*m+error[name]+(1-theta)*error['a']
                    image = midpoint-width, midpoint+width
                    assert F(saved['midpoint_rational']) == midpoint and F(saved['width_rational']) == width
                    assert iv(saved['interval']) == image
                    endpoint_images.append(image)
                height = min(x[0] for x in endpoint_images),max(x[1] for x in endpoint_images)
                assert iv(node['real']) == real[name] and iv(node['imag']) == height
                assert 0 < real[name][0] <= real[name][1] < 1
                C[name], I[name] = iv(node['cotangent']['real']),iv(node['cotangent']['imag'])
                means[name] = add(means[name],sc(I[name],weight))
            terms = dict(V=sc(sub(sub(sc(C['a'],3),C['s']),C['t']),weighted),
                S=sc(sub(O,I['s']),weight),T=sc(neg(add(O,I['t'])),weight),
                A=sc(sub(sub(sub(sc(I['a'],3),I['s']),I['t']),O),weight))
            assert {k:iv(v) for k,v in slab['integral_contributions'].items()} == terms
            totals = {k:add(totals[k],terms[k]) for k in totals}
        assert {k:iv(v) for k,v in row['normalized_integrals'].items()} == totals
        delta = sub((H,H),coordinates['a'][1]); pd = mul(pi,delta)
        assert delta[0] > 0 and iv(row['height_displacement']) == delta
        W = mul(mul(pd,delta),totals['V']); assert iv(row['W']) == W
        As,At,Aa1 = [mul(pd,totals[k]) for k in ('S','T','A')]
        forced = row['forced_additions']
        cosine, mod_square, own_force, sine = [iv(forced[k]) for k in
            ('cosine','modulus_square','own_force','sine_at_A_upper')]
        assert -1 <= cosine[0] <= cosine[1] <= 1 and mod_square[0] > 0
        assert sine[0] > 0
        bracket = add(iv(forced['log_sine']),log_two)
        assert iv(forced['bracket']) == bracket and bracket[0] > 0
        Jupper = -(F('.5')-coordinates['a'][0][1])*bracket[0]/2
        assert F(forced['J_upper_rational']) == Jupper
        Aa0 = add(Aa1,own_force)
        assert {k:iv(v) for k,v in row['forces'].items()} == dict(s=As,t=At,a_factorial=Aa1,a_forced=Aa0)
        Gs,n = check_gain(row['shared_gains']['s'],As,coordinates['s'][0],(F('.22'),F('.5')),F(88,5));total_cubics += n
        Gt,n = check_gain(row['shared_gains']['t'],At,coordinates['t'][0],(F('.22'),F('.4')),F((3+epsilon)*22,5));total_cubics += n
        assert [b['nu'] for b in row['branches']] == [1,0]
        branches = []
        for b,force in zip(row['branches'],(Aa1,Aa0)):
            nu = b['nu']
            Ga,n = check_gain(b['selected_gain'],force,coordinates['a'][0],(F('.22'),F('.45')),F((nu+1)*49,5));total_cubics += n
            T = W[1]-2*pi[0]*H if nu else W[1]+Jupper
            budget = T+Gs+Ga+Gt
            assert F(b['trial_upper_rational']) == T and F(b['budget_upper_rational']) == budget
            assert b['strictly_negative'] == (budget < 0)
            threshold = -F(1,400) if epsilon == 0 else (-F(1,150) if nu == 0 else None)
            if threshold is not None:assert budget < threshold
            else:assert budget > 0
            branches.append(dict(nu=nu,trial_upper_rational=str(T),s_gain_upper_rational=str(Gs),
                selected_gain_upper_rational=str(Ga),t_gain_upper_rational=str(Gt),budget_upper_rational=str(budget),
                proved_gap_rational=None if threshold is None else str(-threshold),
                classification='upper bound inconclusive' if threshold is None else 'uniform negative main phase'))
            all_budgets.append(budget)
        report.append(dict(beta=1,epsilon=epsilon,branches=branches,
            normalized_Imcot_means={k:rec(v) for k,v in means.items()},
            normalized_integrals={k:rec(v) for k,v in totals.items()},W=rec(W),kappa=rec(pd)))
    assert max(all_budgets) == F(source['worst_budget_upper_rational'])
    assert source['common_margin_rational'] is None
    return dict(cases=report,verified_cotangent_boxes=96,verified_theta_slabs=32,
        verified_modulus_witness_occurrences=total_moduli,verified_gain_functions=8,
        verified_gain_polynomial_branches=total_cubics,verified_fourier_budgets=4,
        epsilon_zero_both_gap_rational='1/400',epsilon_one_forced_gap_rational='1/150',
        epsilon_one_factorial_sign_proved=False,uniform_all_four_signs_proved=False,
        analytic_endpoint_evaluations_inherited=True,analytic_callbacks=0,
        primitive_or_reference_replays=0,finite_source_theorem_proved=False,global_knot_theorem_proved=False)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    if args.output.exists():raise FileExistsError(args.output)
    if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
    inputs=dict(PINNED)
    own=Path(__file__).resolve().relative_to(ROOT).as_posix()
    inputs[own]=sha(ROOT/own)
    out=dict(status='checking',source_path=SOURCE,source_sha256=PINNED[SOURCE],
        checker_path=own,checker_sha256=inputs[own],input_sha256=inputs)
    error=None
    try:
        for name,digest in inputs.items():assert sha(ROOT/name)==digest,name
        out.update(verify(inputs))
        out['changed_inputs']=[n for n,h in inputs.items() if sha(ROOT/n)!=h]
        assert out['changed_inputs']==[]
        out['status']='passed'
    except Exception as exc:
        error=exc;out['status']='failed saved-data verification'
        out['error']=dict(type=type(exc).__name__,message=str(exc))
    args.output.parent.mkdir(parents=True,exist_ok=True)
    with args.output.open('x',encoding='utf-8') as stream:
        json.dump(out,stream,separators=(',',':'));stream.write('\n')
    print(json.dumps(dict(status=out['status'],bindings=len(inputs),output_sha256=sha(args.output))))
    if error is not None:raise error


if __name__=='__main__':main()
