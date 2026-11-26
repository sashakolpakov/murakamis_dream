#!/usr/bin/env python3
"""Two whole-D4 joined-plane ceilings from immutable saved analytic data.

Exact fractions/integer square roots only: 48 force vertices and96gains.
No original evaluator main, analytic callback, new reference or retry.
"""
import argparse
from fractions import Fraction as F
import hashlib
import importlib.util
from itertools import product
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
PROOF = 'notes/research_mixed_terminal_uniform_joined_plane.md'
SOURCE = 'repro/results/research-mixed-terminal-four-input-integral-budget.json'
AUDIT = 'repro/results/research-mixed-terminal-four-input-integral-budget-saved-audit.json'
GAIN = 'experiments/certify_mixed_terminal_four_input_integral_budget.py'
GAIN_CHECKER = 'experiments/check_mixed_terminal_four_input_integral_budget.py'
REFINED = 'repro/results/research-mixed-terminal-quadratic-residual-refinement.json'
REFINED_PROOF = 'notes/research_mixed_terminal_quadratic_residual_refinement.md'
REFINED_CHECKER = 'experiments/check_mixed_terminal_quadratic_residual_refinement.py'
POSTERIOR = 'repro/results/research-mixed-terminal-split-taylor-completion.json'
SPLIT = 'repro/results/research-mixed-terminal-split-taylor-inclusion.json'
AFFINE = 'repro/results/research-mixed-terminal-correlated-affine-family.json'
PINNED = {
    'notes/research_mixed_terminal_uniform_joined_plane.md':
        '12ab4cd4e94a521ac97da4e8f71aa68b2352764cd2d283cf123e9f5f113b11e5',
    'repro/results/research-mixed-terminal-four-input-integral-budget.json':
        '9831e8bdbc884cfc0b0c99dbc7f92245403988ae7dc4bbbba86b5606c5a1575e',
    'repro/results/research-mixed-terminal-four-input-integral-budget-saved-audit.json':
        'cda9eef92856387d0ec0dccca6311512bb980034a07832ab89a99a7bc733d6c3',
    'experiments/certify_mixed_terminal_four_input_integral_budget.py':
        '3b806591d88cd461ab7764a6f9c704a048d9c33edb88834a32dbc59a99c91388',
    'experiments/check_mixed_terminal_four_input_integral_budget.py':
        'd38f41d186bf31d3255861c45cb0500d1a21a4eb1bfd4d366c6a956efc614bf4',
    'repro/results/research-mixed-terminal-quadratic-residual-refinement.json':
        '2834576c2a443c9ffd24032277b5f253d9a85eac17d3f754905812e822a9a331',
    'notes/research_mixed_terminal_quadratic_residual_refinement.md':
        'f012610187e14b824fdfeea730bc71ffde1660687ffbdcc491bc945c6a54d596',
    'experiments/check_mixed_terminal_quadratic_residual_refinement.py':
        '251fc4b3c656201ab5451287577baddb4d4be8122ff34a1318078de0f8501a05',
    'repro/results/research-mixed-terminal-split-taylor-completion.json':
        'e04521450e1973658cbd602aa0a8f54d4c7d40c968b4b90d65374d570981c617',
    'repro/results/research-mixed-terminal-split-taylor-inclusion.json':
        'a25587e526dc753306eb690b76f1f07d0d05410be315c6675023bd87ae42e202',
    'repro/results/research-mixed-terminal-correlated-affine-family.json':
        '51b702aa6ea44aa5891bc1146a7d5c0d22686cd814f9bbe5d9c4c63b9a16f9e1',
    'notes/research_mixed_terminal_reserved_plane_transfer.md':
        '0d4461c5b00e4f68dc00c0c1d6e824156c9c5050327eab70694f3cd21e714c70',
    'notes/research_mixed_terminal_symmetric_pair_costs.md':
        'b4ee1a7bdde317edab0210b20cb8616913984c4f992d1cbed240f6092a8e593f',
    'notes/research_mixed_terminal_shared_force_vertices.md':
        '2134390846790b38b6e6451a010d0660e0b7f21fb913739a339173a9771b4a78',
    'notes/research_mixed_terminal_cubic_cost_and_response_bounds.md':
        'dfc3f415e742aa9c632707aea7c699bb2ccbdc054c08fc7ba640e943bcdaa741',
}
H, R = F(1,100),F(8,125)
Z = (F(0),F(0))


def sha(path):
    h=hashlib.sha256()
    with path.open('rb') as f:
        for b in iter(lambda:f.read(1048576),b''):h.update(b)
    return h.hexdigest()


def canonical_sha(x):
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()


def iv(x):
    if 'finite' in x:assert x['finite'] is True
    lo,hi=F(x['lower_rational']),F(x['upper_rational'])
    assert lo<=hi
    return lo,hi


def rec(x):return dict(lower_rational=str(x[0]),upper_rational=str(x[1]))
def cv(x):return iv(x['real']),iv(x['imag'])
def cr(x):return dict(real=rec(x[0]),imag=rec(x[1]))
def ex(x):return F(x),F(x)
def cx(x):return ex(x[0]),ex(x[1])
def add(x,y):return x[0]+y[0],x[1]+y[1]
def neg(x):return -x[1],-x[0]
def sub(x,y):return add(x,neg(y))
def mul(x,y):
    v=[a*b for a in x for b in y]
    return min(v),max(v)
def sc(x,a):return mul(x,ex(a))
def ca(x,y):return add(x[0],y[0]),add(x[1],y[1])
def cn(x):return neg(x[0]),neg(x[1])
def cs(x,a):return sc(x[0],a),sc(x[1],a)
def cm(x,y):return sub(mul(x[0],y[0]),mul(x[1],y[1])),add(mul(x[0],y[1]),mul(x[1],y[0]))
def csub(x,y):return ca(x,cn(y))
def contained(outer,inner):return outer[0]<=inner[0]<=inner[1]<=outer[1]
def exact_sum(x,y):return x[0]+y[0],x[1]+y[1]
def exact_scale(x,a):return x[0]*a,x[1]*a


def forbidden(*args,**kwargs):raise AssertionError('forbidden evaluator/checker main')


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path,required=True)
    args=p.parse_args()
    if args.output.exists():raise FileExistsError(args.output)
    if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
    inputs=dict(PINNED);own=Path(__file__).resolve().relative_to(ROOT).as_posix();inputs[own]=sha(ROOT/own)
    counts=dict(cases=0,center_marginal_bounds=0,saved_slab_recombinations=0,force_vertices=0,
        scalar_cubic_gains=0,independent_gain_checks=0,analytic_callbacks=0,original_primitives=0,
        roots=0,reference_evaluations=0,subdivisions=0,retries=0)
    out=dict(status='initializing',proof_path=PROOF,source_path=SOURCE,checker_path=own,
        input_sha256=inputs,counts=counts,cases=[],uniform_plane_ceilings_proved=False,
        profile_suppression_proved=False,finite_source_theorem_proved=False,knot_theorem_proved=False)
    fatal=None
    try:
        assert PINNED
        def bind(name,digest):
            assert name not in inputs or inputs[name]==digest,name
            assert sha(ROOT/name)==digest,name
            inputs[name]=digest
        for name,digest in list(inputs.items()):bind(name,digest)
        source,audit,refinement,posterior,split,affine=[json.loads((ROOT/n).read_text())
            for n in (SOURCE,AUDIT,REFINED,POSTERIOR,SPLIT,AFFINE)]
        for d in (source,audit,refinement,posterior,split,affine):
            assert d['changed_inputs']==[]
            for key in ('input_sha256','dependencies_sha256'):
                for name,digest in d.get(key,{}).items():bind(name,digest)
        assert source['status']=='completed fixed protocol' and source['all_four_budgets_enclosed']
        assert audit['status']=='passed' and audit['source_sha256']==inputs[SOURCE]
        assert audit['checker_sha256']==inputs[GAIN_CHECKER] and audit['verified_cotangent_boxes']==96
        assert refinement['status']=='completed fixed saved-only protocol'
        assert refinement['source_path']==POSTERIOR and refinement['source_sha256']==inputs[POSTERIOR]
        assert refinement['proof_sha256']==inputs[REFINED_PROOF] and refinement['checker_sha256']==inputs[REFINED_CHECKER]
        assert posterior['source_path']==SPLIT and posterior['source_sha256']==inputs[SPLIT]
        assert split['source_path']==AFFINE and split['source_sha256']==inputs[AFFINE]
        modules=[]
        for name,path in (('frozen_plane_gain',GAIN),('frozen_plane_gain_check',GAIN_CHECKER)):
            spec=importlib.util.spec_from_file_location(name,ROOT/path);m=importlib.util.module_from_spec(spec)
            spec.loader.exec_module(m);m.main=forbidden;modules.append(m)
        g,check=modules
        def norm(x):
            square=sum(max(abs(a),abs(b))**2 for a,b in x)
            bounds=g.sqrt_interval(square)
            return bounds[1],dict(rectangle=cr(x),squared_radius_rational=str(square),modulus=rec(bounds))
        def exact_norm(x):return norm(cx(x))
        pi=iv(source['constants']['pi']);assert F(157,50)<pi[0]<=pi[1]<F(22,7)
        ipi=(Z,pi)
        for epsilon in (0,1):
            counts['cases']+=1
            old=source['cases'][epsilon];saved=audit['cases'][epsilon]
            new=refinement['cases'][2+epsilon];prior=posterior['posterior_enclosures'][2+epsilon]
            sp=split['cases'][2+epsilon];aff=affine['cases'][2+epsilon]
            row=dict(beta=1,epsilon=epsilon,status='initializing',source_case_canonical_sha256=canonical_sha(old),
                refinement_case_canonical_sha256=canonical_sha(new),affine_case_canonical_sha256=canonical_sha(aff),
                marginal={},plane_slabs=[],branches=[])
            out['cases'].append(row)
            try:
                for x in (old,saved,new,prior,sp,aff):assert (x['beta'],x['epsilon'])==(1,epsilon)
                assert new['source_posterior_canonical_sha256']==canonical_sha(prior)
                assert old['source_entry_canonical_sha256']==canonical_sha(prior)
                assert prior['source_case_canonical_sha256']==canonical_sha(sp)
                assert sp['source_case_canonical_sha256']==canonical_sha(aff)
                assert new['affine_case_canonical_sha256']==canonical_sha(aff)
                assert new['exact_linear_system_verified'] is True
                for key in ('center_exact','response_exact','parameter_center','parameter_radius_rational'):
                    assert new[key]==prior[key]==old[key]
                assert new['center_exact']==aff['center'] and new['response_exact']==aff['response_exact']
                assert tuple(map(F,new['parameter_center']))==(F('.30'),-F('.052'))
                assert F(new['parameter_radius_rational'])==R
                assert all(0<=F(x)<=F(y) for x,y in zip(new['posterior_radii_rational'],prior['posterior_radii_rational']))
                assert all(old['domain_guards'].values())
                for name in ('e','xi','t','a','s'):
                    for part in ('real','imag'):
                        assert contained(iv(old['individual_supports'][name][part]),iv(new['coordinate_enclosures'][name][part]))
                names=('e','xi','t','a','s')
                row['center_exact']=new['center_exact']
                row['response_exact']=new['response_exact']
                row['posterior_radii_rational']=new['posterior_radii_rational']
                center=dict(zip(names,[tuple(map(F,x)) for x in new['center_exact']]))
                response=dict(zip(names,[tuple(map(F,x)) for x in new['response_exact']]))
                eta=dict(zip(names,map(F,new['posterior_radii_rational'])))
                height=iv(new['coordinate_enclosures']['a']['imag']);delta=(H-height[1],H-height[0])
                assert delta[0]>0
                kappa=mul(pi,delta)
                delta0=H-center['a'][1]
                ua,usa=response['a'],exact_sum(response['s'],response['a'])
                nua,wua=exact_norm(ua);nusa,wusa=exact_norm(usa)
                wa,wsa=R*nua+eta['a'],R*nusa+eta['s']+eta['a']
                candidate=next(c for c in aff['candidates'] if F(c['multiplier_rational'])==1)
                split_candidate=next(c for c in sp['candidates'] if F(c['multiplier_rational'])==1)
                assert prior['source_candidate_canonical_sha256']==canonical_sha(split_candidate)
                assert split_candidate['source_candidate_canonical_sha256']==canonical_sha(candidate)
                assert candidate['all_full_original_log_disks_regular'] is True
                terms={t['name']:t for t in aff['primitive_terms']}
                full={t['name']:t['full_curvature'] for t in candidate['full_primitive_terms']}
                ka,kbr={},{}
                gp={}
                for name,z,width in (('a',center['a'],wa),('a+s',exact_sum(center['a'],center['s']),wsa)):
                    t=terms[name];f=full[name]
                    assert tuple(map(F,t['center_exact']))==tuple(map(F,f['center_exact']))==z
                    assert f['regular'] is True and f['stage']=='full'
                    assert width<=F(f['radius_upper_rational'])
                    lo,hi=map(F,f['real_interval_rational']);assert 0<lo<hi<1
                    assert lo==z[0]-F(f['radius_upper_rational']) and hi==z[0]+F(f['radius_upper_rational'])
                    m=F(f['curvature_upper_rational']);assert m>0 and m>=iv(f['curvature_bound'])[1]
                    kbr[name]=m
                    ka[name]=csub(cv(t['center_j_prime']),ipi)
                    gp[name]=ca(cv(t['center_j']),cm(ipi,cx((F('.5')-z[0],-z[1]))))
                    row['marginal'][name]=dict(center_exact=list(map(str,z)),center_j=t['center_j'],
                        center_j_prime=t['center_j_prime'],gprime=cr(gp[name]),gsecond=cr(ka[name]),
                        argument_radius_rational=str(width),saved_full_radius_rational=f['radius_upper_rational'],
                        curvature_upper_rational=str(m),full_curvature_source_canonical_sha256=canonical_sha(f))
                P0=csub(cs(gp['a'],F(3,2)),gp['a+s'])
                Ds=cn(ka['a+s']);Da=csub(cs(ka['a'],F(3,2)),ka['a+s'])
                L=csub(cm(cs(ka['a'],F(3,2)),cx(ua)),cm(ka['a+s'],cx(usa)))
                p0=sum(P0[1])/2;rho0=(P0[1][1]-P0[1][0])/2
                L0=tuple(sum(x)/2 for x in L)
                rhoL,wrhoL=norm(csub(L,cx(L0)))
                nds,wds=norm(Ds);nda,wda=norm(Da);nL,wL=exact_norm(L0)
                remainder=(F(3,2)*kbr['a']*wa*wa+kbr['a+s']*wsa*wsa)/2
                rhoP=rho0+R*rhoL+eta['s']*nds+eta['a']*nda+remainder
                linear=exact_sum(exact_scale(L0,delta0),exact_scale(ua,-p0))
                nlinear,wlinear=exact_norm(linear)
                dot=ua[0]*L0[0]+ua[1]*L0[1]
                quadratic=R*R*(nua*nL-dot)/2;assert quadratic>=0
                parts=(delta0*p0,R*nlinear,quadratic,delta[1]*rhoP,
                       eta['a']*(abs(p0)+R*nL))
                UP=sum(parts)
                row['marginal'].update(dict(P0=cr(P0),p0_rational=str(p0),rho0_rational=str(rho0),
                    L=cr(L),L0_exact=list(map(str,L0)),rhoL=wrhoL,Ds_modulus=wds,Da_modulus=wda,
                    ua_modulus=wua,usa_modulus=wusa,L0_modulus=wL,linear_modulus=wlinear,
                    eta_s_rational=str(eta['s']),eta_a_rational=str(eta['a']),
                    Taylor_remainder_rational=str(remainder),rhoP_rational=str(rhoP),
                    delta0_rational=str(delta0),delta=rec(delta),
                    dot_ua_conjugateL0_rational=str(dot),UP_terms_rational=list(map(str,parts)),
                    UP_upper_rational=str(UP)))
                counts['center_marginal_bounds']+=1
                VP=Z;means={name:Z for name in ('a','s')}
                assert len(old['slabs'])==16
                for j,slab in enumerate(old['slabs']):
                    assert slab['index']==j
                    weight,weighted=F(1,16),F(31-2*j,512)
                    assert F(slab['weight_rational'])==weight and F(slab['weighted_rational'])==weighted
                    caa=iv(slab['nodes']['a']['cotangent']['real']);css=iv(slab['nodes']['s']['cotangent']['real'])
                    term=sc(sub(sc(caa,F(3,2)),css),weighted);VP=add(VP,term)
                    row['plane_slabs'].append(dict(index=j,weighted_rational=str(weighted),
                        Ca=rec(caa),Cs=rec(css),contribution=rec(term)))
                    for name in means:
                        means[name]=add(means[name],sc(iv(slab['nodes'][name]['cotangent']['imag']),weight))
                    counts['saved_slab_recombinations']+=1
                assert all(means[n]==iv(saved['normalized_Imcot_means'][n]) for n in means)
                WP=mul(mul(kappa,delta),VP)
                Q=iv(old['forced_additions']['own_force'])
                GH=F(old['forced_additions']['J_upper_rational'])
                trials={1:UP+WP[1]-pi[0]*H,0:UP+WP[1]+GH/2}
                row['plane_value']=dict(pi=rec(pi),kappa=rec(kappa),normalized_VP=rec(VP),WP=rec(WP),
                    old_GH_upper_rational=str(GH),Q=rec(Q),Ia=rec(means['a']),Is=rec(means['s']))
                for nu in (1,0):
                    branch=dict(nu=nu,trial_upper_rational=str(trials[nu]),vertices=[])
                    row['branches'].append(branch)
                    bounds=[kappa,means['a'],means['s']]+([] if nu else [Q])
                    for bits in product((0,1),repeat=len(bounds)):
                        values=[x[bit] for x,bit in zip(bounds,bits)];k,ia,iss=values[:3]
                        forces=(k*(1-iss),k*(F(3,2)*ia-iss-F(1,2))+(values[3]/2 if not nu else 0))
                        vertex=dict(endpoint_bits=list(bits),parameters_rational=list(map(str,values)),
                                    forces_rational=list(map(str,forces)),gains={})
                        branch['vertices'].append(vertex);counts['force_vertices']+=1
                        total=F(0)
                        for name,force,target,K in zip(('s','a'),forces,((F('.22'),F('.5')),(F('.22'),F('.45'))),
                                                       (F(88,5),F((1+nu)*49,10))):
                            cent=iv(new['coordinate_enclosures'][name]['real'])
                            upper,witness=g.gain((force,force),cent,target,K);counts['scalar_cubic_gains']+=1
                            checked,_=check.check_gain(witness,(force,force),cent,target,K)
                            counts['independent_gain_checks']+=1;assert checked==upper
                            vertex['gains'][name]=witness;total+=upper
                        vertex['gain_sum_upper_rational']=str(total)
                        vertex['plane_upper_rational']=str(trials[nu]+total)
                    assert len(branch['vertices'])==(8 if nu else 16)
                    maximum=max(F(v['plane_upper_rational']) for v in branch['vertices'])
                    branch['uniform_plane_upper_rational']=str(maximum)
                    branch['attaining_vertices']=[v['endpoint_bits'] for v in branch['vertices']
                                                 if F(v['plane_upper_rational'])==maximum]
                row['status']='enclosed both joined-plane alternatives'
            except Exception as exc:
                row['status']='failed saved-data calculation';row['error']=dict(type=type(exc).__name__,message=str(exc))
                fatal=exc
        if fatal is None:
            assert counts['cases']==counts['center_marginal_bounds']==2
            assert counts['saved_slab_recombinations']==32 and counts['force_vertices']==48
            assert counts['scalar_cubic_gains']==counts['independent_gain_checks']==96
            out['common_plane_upper_rational']=str(max(F(b['uniform_plane_upper_rational'])
                for c in out['cases'] for b in c['branches']))
            out['uniform_plane_ceilings_proved']=True;out['status']='completed fixed saved-only protocol'
        else:out['status']='failed saved-data calculation'
    except Exception as exc:
        fatal=exc;out['status']='failed saved-data calculation';out['error']=dict(type=type(exc).__name__,message=str(exc))
    out['changed_inputs']=[n for n,h in inputs.items() if sha(ROOT/n)!=h]
    if out['changed_inputs']:out['uniform_plane_ceilings_proved']=False;out['status']='changed inputs'
    out['proof_sha256']=inputs.get(PROOF);out['source_sha256']=inputs.get(SOURCE);out['checker_sha256']=inputs[own]
    args.output.parent.mkdir(parents=True,exist_ok=True)
    with args.output.open('x',encoding='utf-8') as f:json.dump(out,f,separators=(',',':'));f.write('\n')
    print(json.dumps(dict(status=out['status'],counts=counts,common_plane_upper_rational=out.get('common_plane_upper_rational'),
                         output_sha256=sha(args.output))))
    if fatal is not None:raise fatal


if __name__=='__main__':main()
