#!/usr/bin/env python3
"""Saved-only exact audit of the fixed whole-D3 terminal budget.

No Flint import, analytic evaluation, reference solve, or new gain call.
The frozen independent gain checker verifies only already saved witnesses.
"""
import argparse
import ast
from fractions import Fraction as F
import gzip
import hashlib
import importlib.util
from itertools import product
import json
from math import isqrt
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SOURCE = 'repro/results/research-mixed-terminal-three-input-budget.json.gz'
SOURCE_SHA256 = '18f5260f3fcd18461d8dd2859d515d9c5180f53127e917debd628ebcf26a0dec'
DRIVER = 'experiments/certify_mixed_terminal_three_input_budget.py'
PROOF = 'notes/research_mixed_terminal_three_input_budget_protocol.md'
GAIN_CHECKER = 'experiments/check_mixed_terminal_four_input_integral_budget.py'
REFINED = 'repro/results/research-mixed-terminal-quadratic-residual-refinement.json'
POSTERIOR = 'repro/results/research-mixed-terminal-split-taylor-completion.json'
SPLIT = 'repro/results/research-mixed-terminal-split-taylor-inclusion.json'
AFFINE = 'repro/results/research-mixed-terminal-correlated-affine-family.json'
FACES = 'repro/results/research-mixed-terminal-uniform-face-reserves.json'
ALIASES = 'repro/results/research-mixed-terminal-uniform-alias-reserves.json'
PINNED = {
    DRIVER: '2cdcccac8295666d120d6db4b53e7862bd7e14e538a7e37f854f1b2177bd6dab',
    PROOF: '0c37a9813a30cbd964aa0931e13ea1f1f7a2825408f64e071f7400954e4541b6',
    GAIN_CHECKER: 'd38f41d186bf31d3255861c45cb0500d1a21a4eb1bfd4d366c6a956efc614bf4',
}
NAMES = ('e', 'xi', 't', 'a', 's')
NODES = ('a', 's', 't', 'cut_left', 'cut_right')
CUTS = (F(3, 20), F(1, 2))
H, RADIUS, GAP = F(1, 100), F(9, 100), F(1, 10000)
PARAMETER_CENTER = (F(7, 20), -F(1, 100))
Z = (F(0), F(0))
LIMITS = dict(pi=1, exponential=1, cosine=2, sine=10, logarithm=9,
              cotangent=164, vertices=528, scalar_cubic_gains=1152,
              independent_gain_checks=1152, required_comparisons=108,
              direct_alternatives=28, private_left_alternatives=2)


def sha(path):
    result = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1048576), b''):
            result.update(block)
    return result.hexdigest()


def canonical_sha(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True,
        separators=(',', ':')).encode()).hexdigest()


def iv(value):
    if 'finite' in value:
        assert value['finite'] is True
    result = F(value['lower_rational']), F(value['upper_rational'])
    assert result[0] <= result[1]
    return result


def cv(value): return iv(value['real']), iv(value['imag'])
def ex(value): return F(value), F(value)
def cx(value): return ex(value[0]), ex(value[1])
def add(x, y): return x[0]+y[0], x[1]+y[1]
def neg(x): return -x[1], -x[0]
def sub(x, y): return add(x, neg(y))
def mul(x, y):
    products = [a*b for a in x for b in y]
    return min(products), max(products)
def scale(x, a): return mul(x, ex(a))
def ca(x, y): return add(x[0], y[0]), add(x[1], y[1])
def cs(x, a): return scale(x[0], a), scale(x[1], a)
def cn(x): return neg(x[0]), neg(x[1])
def cd(x, y): return ca(x, cn(y))
def cm(x, y):
    return sub(mul(x[0], y[0]), mul(x[1], y[1])), add(mul(x[0], y[1]), mul(x[1], y[0]))
def exact_add(x, y): return x[0]+y[0], x[1]+y[1]
def exact_scale(x, a): return a*x[0], a*x[1]
def contains(outer, inner): return outer[0] <= inner[0] <= inner[1] <= outer[1]
def absmax(x): return max(abs(x[0]), abs(x[1]))
def rec(x): return dict(lower_rational=str(x[0]), upper_rational=str(x[1]))


def modulus(value, saved=None):
    squared = sum(absmax(component)**2 for component in value)
    mesh = 1 << 256
    n = isqrt(squared.numerator*mesh*mesh//squared.denominator)
    lower = F(n, mesh)
    upper = lower if lower*lower == squared else F(n+1, mesh)
    assert lower*lower <= squared <= upper*upper
    if saved is not None:
        assert cv(saved['rectangle']) == value
        assert F(saved['squared_radius_rational']) == squared
        assert iv(saved['modulus']) == (lower, upper) and saved['mesh_bits'] == 256
    return upper


def intersection(x, y, saved):
    value = max(x[0], y[0]), min(x[1], y[1])
    assert value[0] <= value[1]
    assert iv(saved['raw']) == x and iv(saved['necessary']) == y
    assert tuple(map(F, saved['intersection_rational'])) == value
    return value


def typed_ranges(epsilon):
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


def verify_associations(row, new, prior, splitcase, affine, face, alias, epsilon):
    for entry in (row, new, prior, splitcase, affine, face, alias):
        assert (entry['beta'], entry['epsilon']) == (0, epsilon)
    for name, value in (('refinement', new), ('posterior', prior), ('split', splitcase),
                        ('affine', affine), ('face', face), ('alias', alias)):
        assert row['source_associations'][name] == canonical_sha(value)
    assert new['source_posterior_canonical_sha256'] == canonical_sha(prior)
    assert new['split_case_canonical_sha256'] == canonical_sha(splitcase)
    assert new['affine_case_canonical_sha256'] == canonical_sha(affine)
    assert prior['source_case_canonical_sha256'] == canonical_sha(splitcase)
    assert splitcase['source_case_canonical_sha256'] == canonical_sha(affine)
    assert face['refinement_case_canonical_sha256'] == alias['refinement_case_canonical_sha256'] == canonical_sha(new)
    assert face['source_posterior_canonical_sha256'] == canonical_sha(prior)
    assert alias['image_cover_case_canonical_sha256'] == canonical_sha(face)
    for name in ('center_exact', 'response_exact', 'parameter_center', 'parameter_radius_rational'):
        assert row[name] == new[name] == prior[name]
    assert row['posterior_radii_rational'] == new['posterior_radii_rational']
    assert new['center_exact'] == splitcase['original_center'] == affine['center']
    assert new['response_exact'] == splitcase['original_response'] == affine['response_exact']
    assert tuple(map(F, new['parameter_center'])) == PARAMETER_CENTER
    assert F(new['parameter_radius_rational']) == RADIUS
    assert new['exact_linear_system_verified'] and prior['exact_linear_system_verified']
    assert len(new['posterior_radii_rational']) == len(prior['posterior_radii_rational']) == 5
    assert all(0 <= F(a) <= F(b) for a, b in zip(new['posterior_radii_rational'], prior['posterior_radii_rational']))
    assert F(new['multiplier_rational']) == F(prior['multiplier_rational']) == 2
    split_candidates = [x for x in splitcase['candidates'] if F(x['multiplier_rational']) == 2]
    old_candidates = [x for x in affine['candidates'] if F(x['multiplier_rational']) == 2]
    assert len(split_candidates) == len(old_candidates) == 1
    scandidate, old = split_candidates[0], old_candidates[0]
    assert prior['source_candidate_canonical_sha256'] == canonical_sha(scandidate)
    assert scandidate['source_candidate_canonical_sha256'] == canonical_sha(old)
    assert splitcase['family_certified'] and scandidate['criterion_pass']
    assert old['saved_central_root_contained'] and old['all_full_original_log_disks_regular']
    assert face['all_nine_uniform_bare_bounds_defined'] and alias['all_twelve_bare_bounds_defined']
    assert face['physical_a_box_rational'] == alias['physical_a_box_rational']
    assert face['intersecting_original_cells'] == alias['intersecting_original_cells']
    for j, part in enumerate(('real', 'imag')):
        assert tuple(map(F, face['physical_a_box_rational'][j])) == iv(new['coordinate_enclosures']['a'][part])
    assert len(face['families']) == 9 and len(alias['families']) == 12 and len(alias['alias_labels']) == 16
    return old


def verify_supports(row, new, epsilon):
    centers = dict(zip(NAMES, (tuple(map(F, x)) for x in new['center_exact'])))
    responses = dict(zip(NAMES, (tuple(map(F, x)) for x in new['response_exact'])))
    eta = dict(zip(NAMES, map(F, new['posterior_radii_rational'])))
    assert len(centers) == len(responses) == len(eta) == 5
    typed, widths, individual = typed_ranges(epsilon), {}, {}
    assert set(row['individual_supports']) == set(NAMES)
    for name in NAMES:
        saved = row['individual_supports'][name]
        width = RADIUS*modulus(cx(responses[name]), saved['modulus_witness'])+eta[name]
        assert F(saved['width_rational']) == width
        widths[name] = width
        result = []
        for j, part in enumerate(('real', 'imag')):
            raw = centers[name][j]-width, centers[name][j]+width
            first = intersection(raw, typed[name][j], saved['necessary_intersections'][part])
            value = intersection(first, iv(new['coordinate_enclosures'][name][part]),
                                 saved['necessary_intersections'][part+'_saved'])
            assert iv(saved[part]) == value
            result.append(value)
        individual[name] = tuple(result)
    return centers, responses, eta, widths, individual


def verify_endpoint(saved, name, theta, centers, responses, eta, widths, individual):
    assert saved['node'] == name and F(saved['theta_rational']) == theta
    weight = 1-theta
    if name in ('s', 't'):
        coefficient = exact_add(responses[name], responses['a'])
        width_real = RADIUS*modulus(cx(coefficient), saved['real_coefficient_modulus'])+eta[name]+eta['a']
        midpoint_real = centers[name][0]+centers['a'][0]
        real = midpoint_real-width_real, midpoint_real+width_real
        necessary_real = add(individual[name][0], individual['a'][0])
        coefficient = exact_add(responses[name], exact_scale(responses['a'], weight))
        width = RADIUS*modulus(cx(coefficient), saved['imaginary_coefficient_modulus'])+eta[name]+weight*eta['a']
        mid = centers[name][1]+weight*centers['a'][1]+theta*H
        necessary_imag = add(individual[name][1], add(scale(individual['a'][1], weight), ex(theta*H)))
    else:
        tau = {'cut_left': CUTS[0], 'cut_right': CUTS[1]}.get(name, F(0))
        real = centers['a'][0]+tau-widths['a'], centers['a'][0]+tau+widths['a']
        necessary_real = add(individual['a'][0], ex(tau))
        mid, width = weight*centers['a'][1]+theta*H, weight*widths['a']
        necessary_imag = add(scale(individual['a'][1], weight), ex(theta*H))
        assert saved['imaginary_coefficient_modulus'] is None
    assert F(saved['imaginary_midpoint_rational']) == mid
    assert F(saved['imaginary_width_rational']) == width
    return (intersection(real, necessary_real, saved['real_intersection']),
            intersection((mid-width, mid+width), necessary_imag, saved['imaginary_intersection']))


def verify_integrals(row, support):
    means, weighted = {name:Z for name in NODES}, {name:Z for name in NODES}
    assert len(row['slabs']) == 16 and not row['pending_height_nodes']
    for j, slab in enumerate(row['slabs']):
        left, right = F(j, 16), F(j+1, 16)
        weight, omega = F(1, 16), F(31-2*j, 512)
        assert slab['index'] == j and iv(slab['theta']) == (left, right)
        assert F(slab['weight_rational']) == weight and F(slab['weighted_rational']) == omega
        assert set(slab['nodes']) == set(NODES)
        for name in NODES:
            node = slab['nodes'][name]
            assert len(node['endpoint_supports']) == 2
            lr, li = verify_endpoint(node['endpoint_supports'][0], name, left, *support)
            rr, ri = verify_endpoint(node['endpoint_supports'][1], name, right, *support)
            assert lr == rr and 0 < lr[0] <= lr[1] < 1
            height = min(li[0], ri[0]), max(li[1], ri[1])
            assert iv(node['real']) == lr and iv(node['imag']) == height
            C, I = cv(node['cotangent'])  # Source-bound analytic inputs, never reevaluated.
            assert iv(node['mean_contribution']) == scale(I, weight)
            assert iv(node['weighted_contribution']) == scale(C, omega)
            means[name] = add(means[name], scale(I, weight))
            weighted[name] = add(weighted[name], scale(C, omega))
    assert {name:iv(x) for name,x in row['normalized_Imcot_means'].items()} == means
    assert {name:iv(x) for name,x in row['weighted_Recot_means'].items()} == weighted
    return means, weighted


def verify_signed(saved, F0, L, error, ua, eta_a, delta0, delta, sign):
    assert saved['sign'] == sign and saved['full_center_interval_used'] is True
    assert cv(saved['F0']) == F0 and cv(saved['L']) == L
    assert F(saved['error_radius_rational']) == error
    assert tuple(map(F,saved['ua_exact'])) == ua
    assert F(saved['delta0_rational']) == delta0 and iv(saved['delta']) == delta
    p = F0[1]
    ua_upper = modulus(cx(ua), saved['ua_modulus'])
    L_upper = modulus(L, saved['L_modulus'])
    linear = cd(cs(L,delta0),cm(cx(ua),(p,Z)))
    linear_upper = modulus(linear,saved['linear_modulus'])
    dot = add(scale(L[0],ua[0]),scale(L[1],ua[1]))
    assert iv(saved['dot_interval']) == dot
    quad = RADIUS**2*(ua_upper*L_upper+(-dot[0] if sign==1 else dot[1]))/2
    assert quad >= 0
    terms = (scale(p,sign*delta0)[1],RADIUS*linear_upper,quad,
             delta[1]*error,eta_a*(absmax(p)+RADIUS*L_upper))
    assert tuple(map(F,saved['terms_rational'])) == terms
    assert F(saved['upper_rational']) == sum(terms)
    return sum(terms)


def verify_taylor(row, affine, candidate, support, pi, delta):
    centers, responses, eta, widths, individual = support
    old_terms = {x['name']:x for x in affine['primitive_terms']}
    full = {x['name']:x['full_curvature'] for x in candidate['full_primitive_terms']}
    ipi, gp, gpp, curvature = (Z,pi), {}, {}, {}
    wa = widths['a']
    wsa = RADIUS*modulus(cx(exact_add(responses['a'],responses['s'])))+eta['a']+eta['s']
    for name, center, width in (('a',centers['a'],wa),
            ('a+s',exact_add(centers['a'],centers['s']),wsa)):
        saved, old, guard = row['saved_center_data'][name], old_terms[name], full[name]
        assert tuple(map(F,old['center_exact'])) == tuple(map(F,guard['center_exact'])) == center
        assert tuple(map(F,saved['center_exact'])) == center
        assert saved['center_j'] == old['center_j'] and saved['center_j_prime'] == old['center_j_prime']
        assert saved['full_curvature'] == guard
        assert saved['full_curvature_canonical_sha256'] == canonical_sha(guard)
        assert guard['regular'] is True and guard['stage']=='full'
        assert width <= F(guard['radius_upper_rational'])
        lo,hi = map(F,guard['real_interval_rational'])
        assert 0 < lo < hi < 1
        m = F(guard['curvature_upper_rational'])
        assert m >= iv(guard['curvature_bound'])[1] > 0
        gp[name] = ca(cv(old['center_j']),cm(ipi,cx((F(1,2)-center[0],-center[1]))))
        gpp[name] = cd(cv(old['center_j_prime']),ipi)
        curvature[name] = m
        assert cv(saved['gprime']) == gp[name] and cv(saved['gsecond']) == gpp[name]
        assert F(saved['argument_radius_rational']) == width
    P0 = cd(cs(gp['a'],F(3,2)),gp['a+s'])
    Ps,Pa = cn(gpp['a+s']),cd(cs(gpp['a'],F(3,2)),gpp['a+s'])
    LP = ca(cm(Ps,cx(responses['s'])),cm(Pa,cx(responses['a'])))
    errorP = modulus(Ps)*eta['s']+modulus(Pa)*eta['a']+(
        F(3,2)*curvature['a']*wa*wa+curvature['a+s']*wsa*wsa)/2
    saved = row['plane_marginal']
    assert cv(saved['P0']) == P0 and cv(saved['Ds']) == Ps and cv(saved['Da']) == Pa
    assert cv(saved['L']) == LP and F(saved['rho_rational']) == errorP
    UP = verify_signed(saved['signed_product'],P0,LP,errorP,responses['a'],eta['a'],
                       H-centers['a'][1],delta,1)
    assert len(row['cuts']) == 2 and not row['pending_cuts']
    cuts = {}
    for saved,tau,name in zip(row['cuts'],CUTS,('cut_left','cut_right')):
        center = centers['a'][0]+tau,centers['a'][1]
        distance = min(center[0]-wa,1-center[0]-wa)
        assert saved['name']==name and F(saved['tau_rational'])==tau
        assert tuple(map(F,saved['center_exact']))==center
        assert F(saved['full_argument_radius_rational'])==wa
        assert F(saved['distance_rational'])==distance and 0<distance<=F(1,2)
        assert cv(saved['center_sine'])[0][0]>0
        # These original-branch elementary enclosures remain immutable inputs.
        jcut,cot = cv(saved['center_j']),cv(saved['center_cotangent'])
        sine = iv(saved['curvature_sine'])
        assert sine[0]>0
        curvature_ball = iv(saved['curvature_bound'])
        m = F(saved['curvature_upper_rational'])
        assert m==curvature_ball[1]>0
        # Arb evaluates pi^2/sin^2 directly. Serialized operands can give a
        # slightly wider quotient; the immutable analytic result is retained.
        gpcut = ca(jcut,cm(ipi,cx((F(1,2)-center[0],-center[1]))))
        gppcut = cd((mul(pi,cot[0]),mul(pi,cot[1])),ipi)
        assert cv(saved['gprime'])==gpcut and cv(saved['gsecond'])==gppcut
        D0 = ca(cd(ca(gpcut,gp['a+s']),cs(gp['a'],3)),cs(ipi,2*tau))
        Ds = gpp['a+s']
        Da = cd(ca(gppcut,gpp['a+s']),cs(gpp['a'],3))
        LD = ca(cm(Ds,cx(responses['s'])),cm(Da,cx(responses['a'])))
        error = modulus(Ds)*eta['s']+modulus(Da)*eta['a']+(
            m*wa*wa+curvature['a+s']*wsa*wsa+3*curvature['a']*wa*wa)/2
        assert cv(saved['D0'])==D0 and cv(saved['Ds'])==Ds and cv(saved['Da'])==Da
        assert cv(saved['L'])==LD and F(saved['rho_rational'])==error
        UD = verify_signed(saved['signed_product'],D0,LD,error,responses['a'],eta['a'],
                           H-centers['a'][1],delta,-1)
        width = RADIUS*modulus(LD)+error
        Dreal = D0[0][0]-width,D0[0][1]+width
        assert F(saved['ReD_width_rational'])==width and iv(saved['ReD'])==Dreal
        cuts[name]=dict(UD=UD,Dreal=Dreal,sigma=F(3,5) if tau==CUTS[0] else F(5,3))
    return UP,cuts


def verify_selected(row, individual, constants):
    saved = row['selected_primitives']
    A = individual['a'][0]
    assert iv(saved['A'])==A
    cosine,square,Q,sine,logsine = (iv(saved[name]) for name in
        ('cosine','modulus_square','Q','sine','log_sine'))
    assert -1<=cosine[0]<=cosine[1]<=1 and square[0]>0 and sine[0]>0
    # square,Q,sine,logsine are original analytic enclosures, not reevaluated.
    bracket=add(logsine,iv(constants['log_two']))
    assert iv(saved['bracket'])==bracket
    assert bracket[0]>0 and F(1,6)<A[0]<=A[1]<F(1,2)
    GH=-(F(1,2)-A[1])*bracket[0]/2
    assert F(saved['GH_upper_rational'])==GH
    return Q,GH


def verify_budgets(row, epsilon, individual, means, weighted, delta, pi, UP, cuts, Q, GH, gain_checker, counts):
    kappa=mul(pi,delta)
    assert iv(row['kappa'])==kappa and iv(row['height_displacement'])==delta and delta[0]>0
    factor=mul(mul(pi,delta),delta)
    Vmain=sub(sub(scale(weighted['a'],3),weighted['s']),weighted['t'])
    Vplane=sub(scale(weighted['a'],F(3,2)),weighted['s'])
    Wmain,Wplane=mul(factor,Vmain),mul(factor,Vplane)
    saved=row['integrated_values']
    assert iv(saved['pi_delta_squared'])==factor and iv(saved['main_normalized'])==Vmain
    assert iv(saved['plane_normalized'])==Vplane and iv(saved['main_W'])==Wmain and iv(saved['plane_W'])==Wplane
    expected=[(kind,nu) for kind in ('main','plane','cut_left','cut_right') for nu in (1,0)]
    assert [(b['kind'],b['nu']) for b in row['budgets']]==expected and not row['pending_budgets']
    values={}
    for branch,(kind,nu) in zip(row['budgets'],expected):
        order=['kappa','Ia','Is']; parameters=[kappa,means['a'],means['s']]
        if kind=='main':
            order+=['It'];parameters+=[means['t']]
            trial=Wmain[1]+(-2*pi[0]*H if nu else GH)
            costs=dict(s=F(88,5),a=F(49,5)*(nu+1),t=F(22,5)*(3+epsilon))
        elif kind=='plane':
            trial=UP+Wplane[1]+(-pi[0]*H if nu else GH/2)
            costs=dict(s=F(88,5),a=F(49,10)*(nu+1))
        else:
            item=cuts[kind]
            order+=['Icut','ReD'];parameters+=[means[kind],item['Dreal']]
            Vcut=sub(sub(scale(weighted['a'],3),weighted['s']),weighted[kind])
            trial=item['UD']+mul(factor,Vcut)[1]+(-2*pi[0]*H if nu else GH)
            costs=dict(s=F(88,5),a=F(49,5)*(nu+F(1,2)+item['sigma']))
        if not nu:
            order.append('Q');parameters.append(Q)
        assert branch['parameter_order']==order
        assert list(map(iv,branch['parameter_intervals']))==parameters
        assert {k:F(v) for k,v in branch['costs_rational'].items()}==costs
        assert F(branch['trial_upper_rational'])==trial
        bitsets=list(product((0,1),repeat=len(parameters)))
        assert len(branch['vertices'])==len(bitsets)
        totals=[]
        for vertex,bits in zip(branch['vertices'],bitsets):
            assert vertex['endpoint_bits']==list(bits)
            point=dict(zip(order,(interval[bit] for interval,bit in zip(parameters,bits))))
            assert {k:F(v) for k,v in vertex['parameters_rational'].items()}==point
            k,ia,iss=point['kappa'],point['Ia'],point['Is']
            forces=dict(s=k*(1-iss))
            if kind=='main':
                forces.update(a=k*(3*ia-iss-point['It']-1)+point.get('Q',F(0)),t=-k*(1+point['It']))
            elif kind=='plane':
                forces['a']=k*(F(3,2)*ia-iss-F(1,2))+point.get('Q',F(0))/2
            else:
                forces['a']=point['ReD']+k*(3*ia-iss-point['Icut']-1)+point.get('Q',F(0))
            assert {k:F(v) for k,v in vertex['forces_rational'].items()}==forces
            assert set(vertex['gains'])==set(vertex['independent_checks'])==set(costs)
            gain_sum=F(0)
            for name,K in costs.items():
                center=individual[name][0]
                target=(F('.22'),F('.5') if name=='s' else F('.4') if name=='t' else F('.45'))
                assert contains(target,center)
                upper,nchecks=gain_checker.check_gain(vertex['gains'][name],ex(forces[name]),center,target,K)
                assert F(vertex['independent_checks'][name]['upper_rational'])==upper
                assert vertex['independent_checks'][name]['check']==nchecks
                gain_sum+=upper;counts['saved_gain_certificates']+=1
            assert F(vertex['gain_sum_upper_rational'])==gain_sum
            assert F(vertex['budget_upper_rational'])==trial+gain_sum
            totals.append(trial+gain_sum);counts['vertices']+=1
        maximum=max(totals)
        assert F(branch['budget_upper_rational'])==maximum
        assert branch['attaining_vertices']==[list(bits) for bits,value in zip(bitsets,totals) if value==maximum]
        values[kind,nu]=maximum
    return values


def verify_comparisons(row, epsilon, individual, face, alias, values, counts):
    expected=[('four',j) for j in list(range(8))+[20]] if epsilon else [('three_mixed',j) for j in range(8)]+[('three_half',0)]
    assert [(f['series'],f['family']) for f in face['families']]==expected
    labels=['main','constant']+['alias:'+x['t_state']+':'+x['private_state'] for x in alias['alias_labels']]+[
        series+':'+str(family) for series,family in expected]
    assert row['required_label_inventory']==labels and len(labels)==len(set(labels))==27
    assert row['expected_required_comparisons']==54 and not row['pending_comparisons']
    if epsilon:
        a,t,e=individual['a'],individual['t'],individual['e']
        guards=dict(A_above_299=a[0][0]>F('.299'),A_at_most_36=a[0][1]<=F('.36'),
            t_above_302=t[0][0]>F('.302'),t_at_most_350=t[0][1]<=F('.350'),
            ht_above_minus071=t[1][0]>F('-.071'),ht_at_most_minus020=t[1][1]<=F('-.020'),
            e_original_real=F('.333')<=e[0][0]<=e[0][1]<=F('.363'),
            e_original_height=F('-.051')<=e[1][0]<=e[1][1]<=F('-.019'))
        assert row['private_left_route']['guards']==guards
        private_left=all(guards.values())
        assert row['private_left_route']['available']==private_left
        assert row['private_left_route']['original_open_endpoint_bounds_retained'] is True
        assert row['private_left_route']['proof']=='notes/research_mixed_terminal_four_input_private_left_force.md'
    else:
        assert row['private_left_route']==dict(available=False,reason='terminal type3')
        private_left=False
    reserve=F(111,1000)+F(11,25)*individual['a'][1][0]
    assert F(row['constant_reserve_rational'])==reserve
    desired=[]
    for nu in (1,0):
        desired.append(('main',nu,dict(main=values['main',nu]),None))
        desired.append(('constant',nu,dict(plane=values['plane',nu]-reserve),None))
    for label in alias['alias_labels']:
        assert label['complete_finite_coverage']
        reserve=F(label['allocated_reserve_rational'])
        assert reserve==-F(label['uniform_bare_upper_rational'])-F(41,1000)
        for nu in (1,0):
            desired.append(('alias:'+label['t_state']+':'+label['private_state'],nu,
                dict(plane=values['plane',nu]-reserve),
                dict(source_label_canonical_sha256=canonical_sha(label),label=label)))
    for family in face['families']:
        assert family['complete_finite_coverage'] and not family['null_jobs_unresolved']
        bare=F(family['uniform_bare_upper_rational'])
        assert bare==max(F(x['decoded_upper_rational']) for x in family['contributing_jobs'])
        f=family['family']
        kind=('cut_right' if family['series']=='three_half' or f==20 else
              'cut_left' if f in (0,4,5) else 'cut_right' if f in (1,6,7) else None)
        for nu in (1,0):
            options=dict(plane=values['plane',nu]+bare)
            if kind:
                options['direct']=values[kind,nu]+bare;counts['direct_alternatives']+=1
            if epsilon and f==2 and private_left:
                options['private_left_transfer']=values['main',nu]+bare;counts['private_left_alternatives']+=1
            desired.append((family['series']+':'+str(f),nu,options,
                dict(source_family_canonical_sha256=canonical_sha(family),bare_upper_rational=str(bare),source_family=family)))
    assert len(desired)==len(row['comparisons'])==54
    compact=[]
    for saved,(label,nu,options,association) in zip(row['comparisons'],desired):
        assert (saved['label'],saved['nu'])==(label,nu)
        assert {k:F(v) for k,v in saved['upper_options_rational'].items()}==options
        assert saved['source_association']==association
        best=min(options.values())
        assert F(saved['chosen_upper_rational'])==best
        assert saved['strictly_negative']==(best<0) and saved['target_gap_passed']==(best < -GAP)
        compact.append(dict(label=label,nu=nu,upper_options_rational={k:str(v) for k,v in options.items()},
            chosen_upper_rational=str(best),strictly_negative=best<0,target_gap_passed=best < -GAP))
    assert F(row['worst_upper_rational'])==max(F(x['chosen_upper_rational']) for x in compact)
    counts['comparisons']+=54
    return compact


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    assert SOURCE_SHA256 is not None,'completed analytic source SHA has not been pinned'
    if args.output.exists(): raise FileExistsError(args.output)
    if hasattr(sys,'set_int_max_str_digits'): sys.set_int_max_str_digits(0)
    inputs=dict(PINNED);inputs[SOURCE]=SOURCE_SHA256
    own=Path(__file__).resolve().relative_to(ROOT).as_posix()
    inputs[own]=sha(ROOT/own)
    out=dict(status='initializing',source_path=SOURCE,source_sha256=SOURCE_SHA256,
        checker_path=own,proof_path=PROOF,input_sha256=inputs,cases=[],
        analytic_evaluations=0,root_evaluations=0,new_gain_evaluations=0,
        whole_source_theorem_proved=False,knot_theorem_proved=False)
    fatal=None
    try:
        for name,digest in inputs.items(): assert sha(ROOT/name)==digest,name
        with gzip.open(ROOT/SOURCE,'rt',encoding='utf-8') as stream: source=json.load(stream)
        tree=ast.parse((ROOT/DRIVER).read_text())
        literal=next(ast.literal_eval(n.value) for n in tree.body if isinstance(n,ast.Assign)
            and any(isinstance(t,ast.Name) and t.id=='PINNED' for t in n.targets))
        expected_inputs=dict(literal);expected_inputs[DRIVER]=PINNED[DRIVER]
        paths=(REFINED,POSTERIOR,SPLIT,AFFINE,FACES,ALIASES)
        data={name:json.loads((ROOT/name).read_text()) for name in paths}
        for record in data.values():
            assert record.get('changed_inputs',[])==[]
            for key in ('input_sha256','dependencies_sha256','dependencies'):
                if isinstance(record.get(key),dict):
                    for name,digest in record[key].items():
                        assert name not in expected_inputs or expected_inputs[name]==digest,name
                        expected_inputs[name]=digest
        assert source['input_sha256']==expected_inputs
        for name,digest in expected_inputs.items():
            assert name not in inputs or inputs[name]==digest,name
            assert sha(ROOT/name)==digest,name
            inputs[name]=digest
        assert source['changed_inputs']==[] and source['driver_path']==DRIVER
        assert source['proof_path']==PROOF and source['proof_sha256']==PINNED[PROOF]
        assert source['driver_sha256']==PINNED[DRIVER]
        assert source['precision_bits']==256 and F(source['delta_rational'])==GAP
        assert source['limits']==LIMITS
        assert source['phase_scope']=='entire canonical D3; full independent fixed-height targets'
        assert source['source_scope']=='canonical actual K3; incoming unselected type3, ordinary own4'
        assert not source['whole_source_theorem_proved'] and not source['knot_theorem_proved']
        assert source['status']=='completed fixed protocol' and source['all_108_comparisons_enclosed'] is True
        assert not source['pending_cases'] and len(source['cases'])==2
        refined,posterior,split,affine,faces,aliases=(data[p] for p in paths)
        assert refined['status']=='completed fixed saved-only protocol'
        assert refined['source_path']==POSTERIOR and refined['source_sha256']==inputs[POSTERIOR]
        assert posterior['status']=='passed' and posterior['all_four_input_disks_certified']
        assert posterior['source_path']==SPLIT and posterior['source_sha256']==inputs[SPLIT]
        assert split['all_four_input_families_certified'] and split['source_sha256']==inputs[AFFINE]
        assert affine['status']=='completed fixed protocol'
        assert faces['all_uniform_bare_bounds_defined'] and not faces['unresolved_family_cases']
        assert aliases['all_uniform_alias_bounds_defined'] and not aliases['unresolved_family_cases']
        assert aliases['image_cover_sha256']==inputs[FACES] and F(aliases['height_debit_rational'])==F(41,1000)
        spec=importlib.util.spec_from_file_location('saved_three_input_gain_checker',ROOT/GAIN_CHECKER)
        checker=importlib.util.module_from_spec(spec);spec.loader.exec_module(checker)
        constants=source['constants'];pi=iv(constants['pi'])
        assert F(157,50)<pi[0]<=pi[1]<F(22,7)
        assert iv(constants['exp_2piH'])[0]>1 and iv(constants['log_two'])[0]>0
        counts=dict(vertices=0,saved_gain_certificates=0,comparisons=0,direct_alternatives=0,private_left_alternatives=0)
        for epsilon,row in enumerate(source['cases']):
            assert row['status']=='all fixed comparisons enclosed'
            new,prior=refined['cases'][epsilon],posterior['posterior_enclosures'][epsilon]
            sp,aff,face,alias=(record['cases'][epsilon] for record in (split,affine,faces,aliases))
            candidate=verify_associations(row,new,prior,sp,aff,face,alias,epsilon)
            support=verify_supports(row,new,epsilon)
            individual=support[-1]
            means,weighted=verify_integrals(row,support)
            delta=H-individual['a'][1][1],H-individual['a'][1][0]
            assert delta[0]>0
            UP,cuts=verify_taylor(row,aff,candidate,support,pi,delta)
            Q,GH=verify_selected(row,individual,constants)
            values=verify_budgets(row,epsilon,individual,means,weighted,delta,pi,UP,cuts,Q,GH,checker,counts)
            comparisons=verify_comparisons(row,epsilon,individual,face,alias,values,counts)
            out['cases'].append(dict(beta=0,epsilon=epsilon,source_case_canonical_sha256=canonical_sha(row),
                checked_height_slabs=16,checked_cotangent_components=164,
                individual_coordinate_intervals={name:{'real':rec(z[0]),'imag':rec(z[1])} for name,z in individual.items()},
                budgets=[dict(kind=kind,nu=nu,upper_rational=str(value)) for (kind,nu),value in values.items()],
                private_left_route=row['private_left_route'],comparisons=comparisons,
                worst_upper_rational=row['worst_upper_rational']))
        assert counts['vertices']==528 and counts['saved_gain_certificates']==1152
        assert counts['comparisons']==108 and counts['direct_alternatives']==28
        for key,value in LIMITS.items():
            assert source['counts'][key]==(counts['private_left_alternatives'] if key=='private_left_alternatives' else value)
        for key,value in dict(cases=2,completed_cases=2,height_slabs=32,roots=0,source_evaluations=0,
            target_optimizers=0,private_actions=0,dilogarithms=0,subdivisions=0,retries=0).items():
            assert source['counts'][key]==value
        comparisons=[x for row in out['cases'] for x in row['comparisons']]
        worst=max(F(x['chosen_upper_rational']) for x in comparisons)
        assert source['all_108_negative']==(worst<0) and source['target_gap_proved']==(worst < -GAP)
        assert F(source['worst_upper_rational'])==worst
        assert source['common_margin_rational']==(str(-worst) if worst<0 else None)
        out.update(status='passed',source_input_binding_count=len(expected_inputs),checked_counts=counts,
            all_108_comparisons_enclosed=True,all_108_negative=worst<0,target_gap_proved=worst < -GAP,
            target_gap_rational=str(GAP),worst_upper_rational=str(worst),
            negative_comparisons=sum(x['strictly_negative'] for x in comparisons),
            unresolved_comparisons=sum(not x['strictly_negative'] for x in comparisons),
            target_gap_comparisons=sum(x['target_gap_passed'] for x in comparisons),
            analytic_inputs_policy='Frozen original analytic endpoints; all subsequent exact rational operations recombined.')
    except (Exception,KeyboardInterrupt) as exc:
        fatal=exc;out.update(status='failed',error=dict(type=type(exc).__name__,message=str(exc)))
    out['changed_inputs']=[name for name,digest in inputs.items() if not (ROOT/name).is_file() or sha(ROOT/name)!=digest]
    if out['changed_inputs']: out['status']='changed inputs'
    args.output.parent.mkdir(parents=True,exist_ok=True)
    with args.output.open('x') as stream: json.dump(out,stream,sort_keys=True,indent=2);stream.write('\n')
    print(json.dumps(dict(status=out['status'],negative_comparisons=out.get('negative_comparisons'),
        unresolved_comparisons=out.get('unresolved_comparisons'),output_sha256=sha(args.output))),flush=True)
    if fatal is not None: raise fatal
    if out['changed_inputs']: raise SystemExit(1)


if __name__=='__main__': main()
