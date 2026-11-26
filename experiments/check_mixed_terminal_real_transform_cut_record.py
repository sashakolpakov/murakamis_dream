#!/usr/bin/env python3
"""Audit the saved direct-cut budgets and merge all 36 real/entropy comparisons.

Only rational recombination and the frozen stdlib check_gain witness checker
are used. No analytic library, gain generator, root or source evaluator runs.
"""
import argparse
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
SOURCE = 'repro/results/research-mixed-terminal-real-transform-cut-budget.json.gz'
DRIVER = 'experiments/certify_mixed_terminal_real_transform_cut_budget.py'
PROOF = 'notes/research_mixed_terminal_real_transform_cut_protocol.md'
THEORY = 'notes/research_mixed_terminal_real_transform_cut_budget.md'
OLD = 'repro/results/research-mixed-terminal-four-input-integral-budget.json'
OLD_AUDIT = 'repro/results/research-mixed-terminal-four-input-integral-budget-saved-audit.json'
GAIN_CHECKER = 'experiments/check_mixed_terminal_four_input_integral_budget.py'
REFINED = 'repro/results/research-mixed-terminal-quadratic-residual-refinement.json'
POSTERIOR = 'repro/results/research-mixed-terminal-split-taylor-completion.json'
SPLIT = 'repro/results/research-mixed-terminal-split-taylor-inclusion.json'
AFFINE = 'repro/results/research-mixed-terminal-correlated-affine-family.json'
FACES = 'repro/results/research-mixed-terminal-uniform-face-reserves.json'
PREVIOUS = 'repro/results/research-mixed-terminal-terminal-side-planes-saved-audit.json'
PREVIOUS_CHECKER = 'experiments/check_mixed_terminal_terminal_side_planes_record.py'
PREVIOUS_SOURCE = 'repro/results/research-mixed-terminal-terminal-side-planes.json.gz'
PINNED = {
    SOURCE: '6f526c7a5b9c5f0f3b23a23a79ada4c5670966b7518959600e0a02b1caeea8cb',
    DRIVER: '47bece384efa09a87d76e8a8b08c14dc9aa480c1c8a880844dc58963fcd58ca9',
    PROOF: '551233df01752ed8c8d333dd2c6d45cb09b60a391dba9d9d09af7a20ca7264eb',
    THEORY: 'ee4ba95733040b87abf9a4f956f076444f505f1ba2502e684cbe2c9dd37ecf92',
    OLD: '9831e8bdbc884cfc0b0c99dbc7f92245403988ae7dc4bbbba86b5606c5a1575e',
    OLD_AUDIT: 'cda9eef92856387d0ec0dccca6311512bb980034a07832ab89a99a7bc733d6c3',
    GAIN_CHECKER: 'd38f41d186bf31d3255861c45cb0500d1a21a4eb1bfd4d366c6a956efc614bf4',
    REFINED: '2834576c2a443c9ffd24032277b5f253d9a85eac17d3f754905812e822a9a331',
    POSTERIOR: 'e04521450e1973658cbd602aa0a8f54d4c7d40c968b4b90d65374d570981c617',
    SPLIT: 'a25587e526dc753306eb690b76f1f07d0d05410be315c6675023bd87ae42e202',
    AFFINE: '51b702aa6ea44aa5891bc1146a7d5c0d22686cd814f9bbe5d9c4c63b9a16f9e1',
    FACES: '37fc3676a9919525e16b214db0fedebd3e13b980150f5f01ec0d0b28141a07d3',
    PREVIOUS: '4f387cabec8dcc511aa28a43ebc6887e63eaffbf48eef104ca8612b68f80ac29',
    PREVIOUS_CHECKER: '5197088188134ef1df8b640d0db037231f9d346d206b10c6277ffafb431202d7',
    PREVIOUS_SOURCE: '29eaf5f622eb74ef21d67d766c974456a5c4cb6103477f42c9f75b11fb9c94a7',
    'notes/research_mixed_terminal_canonical_source_domain.md':
        'd50929a1a1c02d034feb5ca5f9ebf6e6da70bd6b0a1eb4a67f67fd1108d18d11',
    'notes/research_mixed_terminal_symmetric_pair_costs.md':
        'b4ee1a7bdde317edab0210b20cb8616913984c4f992d1cbed240f6092a8e593f',
    'notes/research_mixed_terminal_concave_profile_envelope.md':
        '6d71c0470a9fe1598cdc46459ffcda98f807eb84c1be8bc2810517706a744ddd',
}
H, R, MESH = F(1,100), F(8,125), 1 << 256
Z = F(0), F(0)
NAMES = ('e','xi','t','a','s')


def sha(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda:stream.read(1048576),b''): h.update(block)
    return h.hexdigest()


def canonical(x):
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()


def load(name):
    with (gzip.open(ROOT/name,'rt') if name.endswith('.gz') else (ROOT/name).open()) as stream:
        return json.load(stream)


def iv(x):
    assert x.get('finite',True) is True
    v = F(x['lower_rational']),F(x['upper_rational']); assert v[0] <= v[1]
    return v


def cv(x): return iv(x['real']),iv(x['imag'])
def pt(x): return x,x
def cp(x): return pt(x[0]),pt(x[1])
def add(x,y): return x[0]+y[0],x[1]+y[1]
def sub(x,y): return x[0]-y[1],x[1]-y[0]
def mul(x,y):
    p = [a*b for a in x for b in y]; return min(p),max(p)
def sc(x,a): return mul(x,pt(a))
def ca(x,y): return add(x[0],y[0]),add(x[1],y[1])
def cd(x,y): return sub(x[0],y[0]),sub(x[1],y[1])
def cs(x,a): return sc(x[0],a),sc(x[1],a)
def cm(x,y): return sub(mul(x[0],y[0]),mul(x[1],y[1])),add(mul(x[0],y[1]),mul(x[1],y[0]))
def contains(outer,inner): return outer[0] <= inner[0] <= inner[1] <= outer[1]


def check_norm(w,z):
    assert cv(w['rectangle']) == z and w['mesh_bits'] == 256
    square = sum(max(abs(lo),abs(hi))**2 for lo,hi in z)
    assert F(w['squared_radius_rational']) == square
    n = isqrt(square.numerator*MESH*MESH//square.denominator)
    lo = F(n,MESH); hi = lo if lo*lo == square else F(n+1,MESH)
    assert iv(w['sqrt_interval']) == (lo,hi) and lo*lo <= square <= hi*hi
    return hi


def ceiling(q,digits=12):
    n = -((-q.numerator*10**digits)//q.denominator)
    a,b = divmod(abs(n),10**digits)
    return ('-' if n<0 else '')+f'{a}.{b:0{digits}d}'


def forbidden(*args,**kwargs):
    raise AssertionError('forbidden numerical, source, or prior-audit entry point')


def check_association(row,old,oa,new,prior,sp,aff,face,eps):
    assert all((x['beta'],x['epsilon']) == (1,eps) for x in (row,old,oa,new,prior,sp,aff,face))
    for name,value in (('source_case',old),('audit_case',oa),('refinement_case',new),
                       ('affine_case',aff),('face_case',face)):
        assert row[name+'_canonical_sha256'] == canonical(value)
    assert old['source_entry_canonical_sha256'] == new['source_posterior_canonical_sha256'] == canonical(prior)
    assert prior['source_case_canonical_sha256'] == canonical(sp) and sp['source_case_canonical_sha256'] == canonical(aff)
    assert new['affine_case_canonical_sha256'] == canonical(aff)
    assert face['refinement_case_canonical_sha256'] == canonical(new) and face['source_posterior_canonical_sha256'] == canonical(prior)
    assert new['exact_linear_system_verified'] and prior['exact_linear_system_verified'] and sp['family_certified']
    for key in ('center_exact','response_exact','parameter_center','parameter_radius_rational'):
        assert new[key] == prior[key] == old[key]
    assert new['center_exact'] == sp['original_center'] == aff['center']
    assert new['response_exact'] == sp['original_response'] == aff['response_exact']
    assert tuple(map(F,new['parameter_center'])) == (F(3,10),-F(13,250))
    assert F(new['parameter_radius_rational']) == R
    assert all(0 <= F(x) <= F(y) for x,y in zip(new['posterior_radii_rational'],prior['posterior_radii_rational']))
    for key in ('center_exact','response_exact','posterior_radii_rational','coordinate_enclosures'):
        assert row[key] == new[key]
    assert row['inherited_domain_guards'] == old['domain_guards'] and all(old['domain_guards'].values())
    for name in NAMES:
        for part in ('real','imag'):
            assert contains(iv(old['individual_supports'][name][part]),iv(new['coordinate_enclosures'][name][part]))
    ac = [c for c in aff['candidates'] if F(c['multiplier_rational']) == 1]
    ss = [c for c in sp['candidates'] if F(c['multiplier_rational']) == 1]
    assert len(ac) == len(ss) == 1
    assert prior['source_candidate_canonical_sha256'] == canonical(ss[0])
    assert ss[0]['source_candidate_canonical_sha256'] == canonical(ac[0]) and ss[0]['criterion_pass']
    assert ac[0]['criterion_verified'] and ac[0]['saved_central_root_contained'] and ac[0]['all_full_original_log_disks_regular']
    assert face['all_nine_uniform_bare_bounds_defined']
    assert tuple(map(F,face['physical_a_box_rational'][0])) == iv(new['coordinate_enclosures']['a']['real'])
    assert tuple(map(F,face['physical_a_box_rational'][1])) == iv(new['coordinate_enclosures']['a']['imag'])
    return ac[0]


def check_difference(row,new,aff,candidate,pi,tau):
    q = dict(zip(NAMES,(tuple(map(F,x)) for x in new['center_exact'])))
    u = dict(zip(NAMES,(tuple(map(F,x)) for x in new['response_exact'])))
    eta = dict(zip(NAMES,map(F,new['posterior_radii_rational'])))
    a0,t0,ua,ut = q['a'],q['t'],u['a'],u['t']
    uta = tuple(ua[j]+ut[j] for j in range(2))
    nd,od = row['new_cut_disk'],row['old_ta_disk']
    nua = check_norm(nd['ua_modulus'],cp(ua)); nuta = check_norm(od['uta_modulus'],cp(uta))
    wa,wta = R*nua+eta['a'],R*nuta+eta['a']+eta['t']
    cut = a0[0]+tau,a0[1]; ta = tuple(a0[j]+t0[j] for j in range(2))
    dist = min(cut[0]-wa,1-cut[0]-wa)
    assert tuple(map(F,nd['center_exact'])) == cut and F(nd['radius_rational']) == wa
    assert F(nd['strip_distance_rational']) == dist and 0 < dist <= F(1,2)
    assert iv(nd['real_interval']) == (cut[0]-wa,cut[0]+wa)
    assert nd['regular'] is True
    z = cv(nd['center_input'])
    assert all(contains(a,pt(b)) for a,b in zip(z,cut)) and 0 < z[0][0] <= z[0][1] < 1
    assert cv(nd['center_sine'])[0][0] > 0 and iv(nd['curvature_sine'])[0] > 0
    # These are inherited composite elementary enclosures, not re-evaluated.
    for key in ('center_j','center_j_prime','center_cotangent'): cv(nd[key])
    mtau = F(nd['curvature_upper_rational'])
    assert mtau == iv(nd['curvature_bound'])[1] and mtau > 0
    term = next(x for x in aff['primitive_terms'] if x['name'] == 't+a')
    disk = next(x['full_curvature'] for x in candidate['full_primitive_terms'] if x['name'] == 't+a')
    assert od['primitive_canonical_sha256'] == canonical(term) and od['full_disk_canonical_sha256'] == canonical(disk)
    assert od['full_disk'] == disk and od['center_j'] == term['center_j'] and od['center_j_prime'] == term['center_j_prime']
    assert tuple(map(F,term['center_exact'])) == tuple(map(F,disk['center_exact'])) == ta
    assert disk['regular'] is True and disk['stage'] == 'full'
    radius = F(disk['radius_upper_rational'])
    assert F(od['new_radius_rational']) == wta <= radius
    assert tuple(map(F,disk['real_interval_rational'])) == (ta[0]-radius,ta[0]+radius)
    assert 0 < ta[0]-radius < ta[0]+radius < 1
    mta = F(disk['curvature_upper_rational']); assert mta >= iv(disk['curvature_bound'])[1] and mta > 0
    jtau,jptau,jta,jpta = cv(nd['center_j']),cv(nd['center_j_prime']),cv(term['center_j']),cv(term['center_j_prime'])
    ipi = Z,pi
    D0 = ca(cd(jtau,jta),cm(ipi,cp((tau-t0[0],-t0[1]))))
    Dt = cd(cs(jpta,-1),ipi); Da = cd(jptau,jpta)
    L = ca(cm(Dt,cp(ut)),cm(Da,cp(ua)))
    w = row['difference_enclosure']
    for key,z in (('D0',D0),('Dt',Dt),('Da',Da),('L',L)): assert cv(w[key]) == z
    p0,rho0 = sum(D0[1])/2,(D0[1][1]-D0[1][0])/2
    L0 = tuple(sum(v)/2 for v in L)
    assert F(w['p0_rational']) == p0 and F(w['rho0_rational']) == rho0
    assert tuple(map(F,w['L0_exact'])) == L0
    rL = check_norm(w['rhoL'],cd(L,cp(L0)))
    ndt = check_norm(w['Dt_modulus'],Dt); nda = check_norm(w['Da_modulus'],Da)
    nL = check_norm(w['L_modulus'],L); nL0 = check_norm(w['L0_modulus'],cp(L0))
    remainder = (mtau*wa*wa+mta*wta*wta)/2
    tail = eta['t']*ndt+eta['a']*nda+remainder
    rho = rho0+R*rL+tail
    assert F(w['Taylor_remainder_rational']) == remainder and F(w['posterior_and_Taylor_error_rational']) == tail
    assert F(w['rho_rational']) == rho
    realD = add(D0[0],(-R*nL-tail,R*nL+tail)); assert iv(w['real']) == realD
    height = iv(new['coordinate_enclosures']['a']['imag'])
    delta = H-height[1],H-height[0]; delta0 = H-a0[1]
    assert iv(w['delta']) == delta and F(w['delta0_rational']) == delta0 and delta[0] > 0
    combined = tuple(delta0*L0[j]-p0*ua[j] for j in range(2))
    ncombined = check_norm(w['combined_linear_modulus'],cp(combined))
    dot = sum(ua[j]*L0[j] for j in range(2))
    assert F(w['dot_ua_conjugateL0_rational']) == dot
    # The PLUS sign belongs to the support of +Im(ua*d)Im(L0*d).
    quadratic = R*R*(nua*nL0+dot)/2; assert quadratic >= 0
    terms = (-delta0*p0,R*ncombined,quadratic,delta[1]*rho,eta['a']*(abs(p0)+R*nL0))
    assert tuple(map(F,w['negative_height_product_terms_rational'])) == terms
    UD = sum(terms)
    assert F(w['negative_height_product_upper_rational']) == UD and w['product_zero_cap_applied'] is False
    return a0,wa,realD,delta,UD


def check_integrals(row,old,oa,pi,a0,wa,tau,delta,realD,count):
    assert len(row['slabs']) == len(old['slabs']) == 16
    means = dict(a=Z,s=Z,cut=Z); V = Z; weights = weighted = F(0)
    real = a0[0]+tau-wa,a0[0]+tau+wa
    assert 0 < real[0] <= real[1] < 1
    for j,(slab,prior) in enumerate(zip(row['slabs'],old['slabs'])):
        theta = F(j,16),F(j+1,16); w = F(1,16); ww = F(31-2*j,512)
        assert slab['index'] == prior['index'] == j and iv(slab['theta']) == iv(prior['theta']) == theta
        assert F(slab['weight_rational']) == F(prior['weight_rational']) == w
        assert F(slab['weighted_rational']) == F(prior['weighted_rational']) == ww
        assert slab['old_slab_canonical_sha256'] == canonical(prior)
        node = slab['new_cut_node']; assert len(node['endpoint_supports']) == 2
        heights = []
        for point,end in zip(theta,node['endpoint_supports']):
            midpoint,width = (1-point)*a0[1]+point*H,(1-point)*wa
            interval = midpoint-width,midpoint+width
            assert F(end['theta_rational']) == point and F(end['midpoint_rational']) == midpoint
            assert F(end['width_rational']) == width and iv(end['interval']) == interval
            heights.append(interval)
        imag = min(z[0] for z in heights),max(z[1] for z in heights)
        assert iv(node['real']) == real and iv(node['imag']) == imag
        outward = cv(node['outward_input'])
        assert contains(outward[0],real) and contains(outward[1],imag)
        assert 0 < outward[0][0] <= outward[0][1] < 1
        cut = cv(node['cotangent'])
        C,I = {},{}
        for name in ('a','s'):
            saved = prior['nodes'][name]['cotangent']
            assert slab['old_'+name+'_cotangent'] == saved
            C[name],I[name] = cv(saved)
            means[name] = add(means[name],sc(I[name],w))
        means['cut'] = add(means['cut'],sc(cut[1],w))
        v = sc(sub(sub(sc(C['a'],3),C['s']),cut[0]),ww)
        assert iv(slab['V_contribution']) == v and iv(slab['Icut_contribution']) == sc(cut[1],w)
        V = add(V,v); weights += w; weighted += ww
        count['slabs'] += 1; count['new_cotangent_associations'] += 1; count['inherited_cotangent_associations'] += 2
    assert weights == 1 and weighted == F(1,2)
    assert all(means[name] == iv(oa['normalized_Imcot_means'][name]) for name in ('a','s'))
    kappa = mul(pi,delta); W = mul(mul(kappa,delta),V)
    Q = iv(old['forced_additions']['own_force']); GH = F(old['forced_additions']['J_upper_rational'])
    shared = row['shared_integrals']
    for key,value in (('pi',pi),('delta',delta),('kappa',kappa),('normalized_V',V),('W',W),
                      ('Ia',means['a']),('Is',means['s']),('Icut',means['cut']),('ReD',realD),('Q',Q)):
        assert iv(shared[key]) == value
    assert shared['old_forced_additions_canonical_sha256'] == canonical(old['forced_additions'])
    assert F(shared['GH_upper_rational']) == GH
    return kappa,means,W,Q,GH


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',required=True,type=Path)
    args = parser.parse_args(); assert not args.output.exists()
    if hasattr(sys,'set_int_max_str_digits'): sys.set_int_max_str_digits(0)
    inputs = dict(PINNED); own = Path(__file__).resolve().relative_to(ROOT).as_posix()
    inputs[own] = sha(ROOT/own)
    for name,digest in inputs.items(): assert sha(ROOT/name) == digest,name
    paths = (SOURCE,OLD,OLD_AUDIT,REFINED,POSTERIOR,SPLIT,AFFINE,FACES,PREVIOUS)
    data = {name:load(name) for name in paths}
    for record in data.values():
        assert record.get('changed_inputs',[]) == []
        for key in ('input_sha256','dependencies_sha256','dependencies'):
            if isinstance(record.get(key),dict):
                for name,digest in record[key].items():
                    assert isinstance(digest,str) and len(digest) == 64
                    assert name not in inputs or inputs[name] == digest,name
                    inputs[name] = digest
    for name,digest in inputs.items(): assert sha(ROOT/name) == digest,name
    source,old,audit,refined,posterior,split,affine,faces,previous = (data[p] for p in paths)
    assert source['status'] == 'completed fixed protocol' and len(source['input_sha256']) == 528
    assert source['precision_bits'] == 256 and F(source['selected_height_rational']) == H
    assert source['all_six_comparisons_enclosed'] and source['all_six_signs_proved'] and not source['pending_cases']
    assert not source['complete_terminal_kernel_proved'] and not source['knot_theorem_proved']
    assert source['proof_sha256'] == PINNED[PROOF] and source['driver_sha256'] == PINNED[DRIVER]
    assert old['status'] == 'completed fixed protocol' and old['all_four_budgets_enclosed']
    assert audit['status'] == 'passed' and audit['source_path'] == OLD and audit['source_sha256'] == PINNED[OLD]
    assert audit['checker_sha256'] == PINNED[GAIN_CHECKER] and audit['verified_cotangent_boxes'] == 96 and audit['verified_theta_slabs'] == 32
    assert refined['source_path'] == POSTERIOR and refined['source_sha256'] == PINNED[POSTERIOR]
    assert posterior['status'] == 'passed' and posterior['all_four_input_disks_certified']
    assert posterior['source_path'] == SPLIT and posterior['source_sha256'] == PINNED[SPLIT]
    assert split['all_four_input_families_certified'] and split['source_path'] == AFFINE and split['source_sha256'] == PINNED[AFFINE]
    assert affine['status'] == 'completed fixed protocol'
    assert faces['all_uniform_bare_bounds_defined'] and not faces['unresolved_family_cases']
    assert previous['status'] == 'passed exact saved terminal-side audit'
    assert previous['source_path'] == PREVIOUS_SOURCE and previous['source_sha256'] == PINNED[PREVIOUS_SOURCE]
    assert previous['input_sha256'][PREVIOUS_CHECKER] == PINNED[PREVIOUS_CHECKER]
    assert previous['paid_real_entropy_branches'] == 32 and previous['unresolved_real_entropy_branches'] == 4
    assert len(previous['input_sha256']) == 557 and F(previous['common_paid_raw_floor_rational']) == F(1,2600)
    pi = iv(old['constants']['pi'])
    assert iv(source['constants']['pi']) == pi and source['constants']['pi_source_sha256'] == PINNED[OLD]
    assert F(157,50) < pi[0] <= pi[1] < F(22,7)
    assert contains(iv(source['constants']['outward_reconstructed_pi']),pi)
    # Read and hash-verified stdlib module; its main/record replay is disabled.
    spec = importlib.util.spec_from_file_location('saved_direct_cut_gain_checker',ROOT/GAIN_CHECKER)
    helper = importlib.util.module_from_spec(spec); spec.loader.exec_module(helper)
    helper.main = forbidden; helper.verify = forbidden
    count = dict(cases=0,center_enclosure_associations=0,slabs=0,new_cotangent_associations=0,
        inherited_cotangent_associations=0,vertices=0,saved_gain_checks=0,comparisons=0,merged_comparisons=0)
    reports,comparisons,updates = [],[],{}
    assert [(c['beta'],c['epsilon'],F(c['tau_rational'])) for c in source['cases']] == [(1,0,F(1,2)),(1,1,F(3,20))]
    for eps,row in enumerate(source['cases']):
        tau,sigma = (F(1,2),F(5,3)) if eps == 0 else (F(3,20),F(3,5))
        assert F(row['sigma_rational']) == sigma
        oldcase,oa,new,prior,sp,aff,face = old['cases'][eps],audit['cases'][eps],refined['cases'][2+eps],posterior['posterior_enclosures'][2+eps],split['cases'][2+eps],affine['cases'][2+eps],faces['cases'][2+eps]
        candidate = check_association(row,oldcase,oa,new,prior,sp,aff,face,eps)
        a0,wa,realD,delta,UD = check_difference(row,new,aff,candidate,pi,tau)
        assert contains(iv(oldcase['height_displacement']),delta)
        kappa,means,W,Q,GH = check_integrals(row,oldcase,oa,pi,a0,wa,tau,delta,realD,count)
        centers = {name:iv(new['coordinate_enclosures'][name]['real']) for name in ('s','a')}
        targets = dict(s=(F(11,50),F(1,2)),a=(F(11,50),F(9,20)))
        assert all(contains(targets[name],centers[name]) for name in centers)
        branchbounds,branchreports = {},[]
        assert [b['nu'] for b in row['branches']] == [1,0]
        for branch in row['branches']:
            nu = branch['nu']; Ka = F(49,5)*(nu+F(1,2)+sigma)
            trial = UD+W[1]+(-2*pi[0]*H if nu else GH)
            assert F(branch['trial_upper_rational']) == trial and F(branch['selected_K_rational']) == Ka
            params = [kappa,means['a'],means['s'],means['cut'],realD]+([] if nu else [Q])
            order = ['kappa','Ia','Is','Icut','ReD']+([] if nu else ['Q'])
            assert branch['parameter_order'] == order and list(map(iv,branch['parameter_intervals'])) == params
            bitslist = list(product((0,1),repeat=len(params)))
            assert [v['endpoint_bits'] for v in branch['vertices']] == [list(b) for b in bitslist]
            uppers = []
            for bits,v in zip(bitslist,branch['vertices']):
                vals = [x[bit] for x,bit in zip(params,bits)]
                assert list(map(F,v['parameters_rational'])) == vals
                k,ia,iss,icut,dr = vals[:5]
                forces = dict(s=k*(1-iss),a=dr+k*(3*ia-iss-icut-1)+(vals[5] if not nu else 0))
                assert {name:F(value) for name,value in v['forces_rational'].items()} == forces
                assert set(v['gains']) == set(v['independent_gain_checks']) == {'s','a'}
                gains = []
                for name,K in (('s',F(88,5)),('a',Ka)):
                    upper,polys = helper.check_gain(v['gains'][name],pt(forces[name]),centers[name],targets[name],K)
                    check = v['independent_gain_checks'][name]
                    assert F(check['upper_rational']) == upper and check['check'] == polys
                    gains.append(upper); count['saved_gain_checks'] += 1
                assert F(v['gain_sum_upper_rational']) == sum(gains)
                total = trial+sum(gains)
                assert F(v['phase_upper_before_bare_rational']) == total
                uppers.append(total); count['vertices'] += 1
            maximum = max(uppers); branchbounds[nu] = maximum
            assert F(branch['phase_upper_before_bare_rational']) == maximum
            assert branch['attaining_vertices'] == [list(b) for b,v in zip(bitslist,uppers) if v == maximum]
            branchreports.append(dict(nu=nu,source_branch_canonical_sha256=canonical(branch),trial_upper_rational=str(trial),
                phase_upper_before_bare_rational=str(maximum),attaining_vertices=branch['attaining_vertices']))
        desired = [('three_mixed',1),('three_half',0)] if eps == 0 else [('four',0)]
        expected = [(s,f,nu) for s,f in desired for nu in (1,0)]
        assert [(x['series'],x['family'],x['nu']) for x in row['comparisons']] == expected
        for x in row['comparisons']:
            series,family,nu = x['series'],x['family'],x['nu']
            fs = [f for f in face['families'] if (f['series'],f['family']) == (series,family)]
            assert len(fs) == 1; f = fs[0]
            assert f['complete_finite_coverage'] and not f['null_jobs_unresolved']
            assert x['source_family_canonical_sha256'] == canonical(f)
            assert x['source_job_count'] == len(f['contributing_jobs']) == (45 if eps == 0 else 25)
            bare = max(F(j['decoded_upper_rational']) for j in f['contributing_jobs'])
            assert F(f['uniform_bare_upper_rational']) == F(x['bare_upper_rational']) == bare
            assert F(x['phase_upper_before_bare_rational']) == branchbounds[nu]
            total = bare+branchbounds[nu]
            assert F(x['joined_upper_rational']) == total and F(x['gap_rational']) == -total
            assert x['strictly_negative'] is True and total < -F(1,160) and x['source_scope'] == 'actual K4'
            profile = 8 if series == 'three_half' else family
            record = dict(epsilon=eps,profile_index=profile,series=series,family=family,nu=nu,
                source_comparison=x,source_comparison_canonical_sha256=canonical(x),
                joined_upper_rational=str(total),upper_decimal_ceiling=ceiling(total),gap_exceeds_1_over_160=True)
            assert (eps,profile,nu) not in updates
            updates[eps,profile,nu] = record; comparisons.append(record); count['comparisons'] += 1
        assert row['status'] == 'enclosed both full-P branches and all assigned source comparisons'
        reports.append(dict(epsilon=eps,tau_rational=str(tau),source_case_canonical_sha256=canonical(row),
            negative_height_product_upper_rational=str(UD),branches=branchreports))
        count['cases'] += 1; count['center_enclosure_associations'] += 1
    assert count == dict(cases=2,center_enclosure_associations=2,slabs=32,new_cotangent_associations=32,
        inherited_cotangent_associations=64,vertices=192,saved_gain_checks=384,comparisons=6,merged_comparisons=0)
    assert source['counts'] == dict(cases=2,completed_cases=2,height_slabs=32,center_cotangents=2,slab_cotangents=32,
        center_complex_sines=2,curvature_real_sines=2,center_logarithms=2,vertices=192,scalar_cubic_gains=384,
        independent_gain_checks=384,source_comparisons=6,new_pi_evaluations=0,private_actions=0,dilogarithms=0,
        roots=0,source_evaluations=0,subdivisions=0,retries=0)
    worst = max(F(r['joined_upper_rational']) for r in comparisons)
    assert F(source['worst_joined_upper_rational']) == worst and F(source['common_six_margin_rational']) == -worst > F(1,160)
    assert {(r['epsilon'],r['profile_index'],r['nu']) for r in previous['unresolved']} == {(0,1,1),(0,8,1),(1,0,1),(1,0,0)}
    merged,seen = [],set()
    for oldrow in previous['comparisons']:
        key = oldrow['epsilon'],oldrow['profile_index'],oldrow['nu']
        assert key not in seen; seen.add(key)
        prior = F(oldrow['proved_upper_rational'])
        update = updates.get(key)
        best = min(prior,F(update['joined_upper_rational'])) if update else prior
        assert best < -F(1,2600)
        merged.append(dict(epsilon=key[0],profile_index=key[1],nu=key[2],label=oldrow['label'],
            prior_comparison=oldrow,direct_cut_comparison=update,proved_upper_rational=str(best),
            proved_upper_decimal_ceiling=ceiling(best),gap_rational=str(-best),strictly_negative=True,
            gap_exceeds_1_over_2600=True))
        count['merged_comparisons'] += 1
    assert seen == {(eps,profile,nu) for eps in (0,1) for profile in range(9) for nu in (0,1)}
    assert len(merged) == 36 and set(updates) <= seen
    smallest = min(-F(r['proved_upper_rational']) for r in merged)
    assert smallest == F(previous['smallest_paid_real_entropy_gap_rational']) > F(1,2600)
    assert F(previous['separate_main_gap_rational']) == F(1,400)
    assert F(previous['separate_alias_gap_rational']) == F(1,20)
    assert F(previous['separate_constant_gap_rational']) == F(1,100)
    assert F(previous['separate_private_left_gap_rational']) == F(51,20000)
    changed = [name for name,digest in inputs.items() if sha(ROOT/name) != digest]; assert not changed
    out = dict(status='passed exact saved direct-cut and all-profile audit',input_sha256=inputs,changed_inputs=changed,
        source_path=SOURCE,source_sha256=PINNED[SOURCE],driver_sha256=PINNED[DRIVER],proof_sha256=PINNED[PROOF],
        previous_audit_sha256=PINNED[PREVIOUS],gain_checker_sha256=PINNED[GAIN_CHECKER],counts=count,
        cases=reports,direct_cut_comparisons=comparisons,common_six_gap_rational=str(-worst),
        common_six_gap_exceeds_1_over_160=True,merged_comparisons=merged,paid_real_entropy_branches=36,
        unresolved_real_entropy_branches=0,smallest_real_entropy_gap_rational=str(smallest),
        complete_profile_raw_floor_rational='1/2600',inherited_finite_source_gap_rational='1/5200',
        direct_private_left_kept_separate=True,old_positive_plane_uppers_preserved=True,
        inherited_analytic_endpoints='Original center sine/log/cotangent, their composite derivative and curvature intervals, and new slab cotangent endpoints are inherited from the pinned reviewed run. All displayed D/product/slab/vertex/gain polynomial and source-sum arithmetic is rechecked.',
        original_source_scope='Actual canonical K4, beta=1, epsilon=0/1, H=1/100; complete original targets and both alternatives. Analytic containing-disk statements do not extend the finite source domain.',
        all_27_terminal_profile_bounds_paid=True,local_two_factor_kernel_gap_supported=True,
        new_analytic_calls=0,new_gain_generations=0,roots=0,source_replays=0,subdivisions=0,
        whole_word_theorem_proved=False,knot_theorem_proved=False,finite_exceptions_theorem_proved=False)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    with args.output.open('x') as stream: json.dump(out,stream,separators=(',',':')); stream.write('\n')
    print(json.dumps(dict(status=out['status'],counts=count,bindings=len(inputs),paid=36,remaining=0,
        largest_direct_upper_decimal_ceiling=ceiling(worst),common_raw_floor='1/2600',
        output_sha256=sha(args.output))))


if __name__ == '__main__':
    main()
