#!/usr/bin/env python3
"""Stdlib-only exact audit of the frozen eight-center third-selection test."""
import argparse
from fractions import Fraction as F
import hashlib
import itertools
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = 'repro/results/research-mixed-third-selected-eight-center-diagnostic.json'
PINNED = {
    SOURCE:'69ea662427dd1499aea1451df25da519d0249dc3604b55afd0bdd55c7da4812a',
    'experiments/diagnose_mixed_third_selected_profiles.py':'4edf2a5f7946d35968acc9492757e69c09a87320fbf2d40fdf883d0f852760e8',
    'notes/research_mixed_third_selected_two_vertex_diagnostic.md':'8c4b1d1af57b2fe416267c7759af32d7ec9ffd7957628169749f8fa5157c9515',
}
CENTERS = ((F(7,20),-F(1,100)),(F(3,10),-F(13,250)))
NAMES = ('a','u','z','v','b')


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify(bindings):
    for name,digest in bindings.items():
        assert isinstance(digest,str) and len(digest)==64
        assert sha(ROOT/name)==digest,name


def interval(row):
    assert row['finite'] is True
    lo,hi=F(row['lower_rational']),F(row['upper_rational'])
    assert lo<=hi
    return lo,hi


def target_box(beta,left,right):
    p=(F(11,50),F(9,20))
    box=[p,(F(1,8),F(1,2)),p,(F(3,20) if beta==0 else F(1,8),F(1,2)),p]
    if left!='main':
        x=F(1,8) if left=='left' else F(1,2)
        box[1]=(x,x)
    if right=='half':box[3]=(F(1,2),F(1,2))
    return box


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    if args.output.exists():raise FileExistsError(args.output)
    verify(PINNED)
    source=json.loads((ROOT/SOURCE).read_text())
    verify(source['input_sha256'])
    assert source['script_sha256']==PINNED['experiments/diagnose_mixed_third_selected_profiles.py']
    assert source['status']=='fixed eight-center diagnostic completed'
    assert source['diagnostic'] is True and source['unexpected_error'] is None
    assert source['whole_domain_claimed'] is False and source['finite_word_realization_claimed'] is False
    assert source['precision_bits']==192 and source['proposal_decimal_digits']==50
    assert source['proposal_max_steps']==20 and source['target_proposal_max_iterations']==200
    assert F(source['height_rational'])==F(1,100)
    assert source['counts']=={'reference_proposals':8,'reference_residual_certificates':8,
        'target_proposals':72,'profile_interval_bounds':72,'finite_quantum_sums':0,
        'parameter_subdivisions':0,'alternate_seeds':0}
    rows=source['references']
    keys=list(itertools.product((0,1),repeat=3))
    assert [(r['alpha'],r['beta'],r['external_right_type_flag']) for r in rows]==keys
    uppers,lowers,summaries=[],[],[]
    support_count=0
    for row,(alpha,beta,sigma) in zip(rows,keys):
        assert row['status']=='fixed canonical reference certified'
        assert tuple(map(F,row['external_a']))==CENTERS[alpha]
        assert tuple(map(F,row['external_c']))==CENTERS[sigma]
        assert len(row['proposal_trace'])<=20
        q0={k:tuple(map(F,v)) for k,v in row['proposal_centers'].items()}
        assert set(q0)==set(NAMES[1:])
        assert all(F(23,100)<=x<=F(9,20) and -F(3,25)<=y<=F(3,25) for x,y in q0.values())
        cert=row['reference_certificate'];rho=F(cert['root_coordinate_radius_rational'])
        assert cert['residual_primitive_calls']=={'g':0,'gp':12}
        moduli=[interval(r)[1] for r in cert['residual_moduli']]
        assert len(moduli)==len(cert['residual'])==4 and all(x>=0 for x in moduli)
        assert F(cert['residual_max_upper_rational'])==max(moduli)
        # Original accretivity gives 4||residual||/pi. This rational test
        # verifies the saved radius independently using pi>157/50.
        squared_bound=F(200,157)**2*sum(x*x for x in moduli)
        assert rho*rho>squared_bound
        for name,q in cert['coordinates'].items():
            real,imag=interval(q['real']),interval(q['imag'])
            center=CENTERS[alpha] if name=='a' else q0[name]
            r=F(0) if name=='a' else rho
            assert real[0]<=center[0]-r<=center[0]+r<=real[1]
            assert imag[0]<=center[1]-r<=center[1]+r<=imag[1]
            if name!='a':
                own=1 if name in('u','z') else beta
                rb=(F(6,25),F(9,25)) if own else (F(267,1000),F(433,1000))
                hb=(-F(51,500),-F(1,1000)) if own else (-F(13,200),F(17,250))
                assert rb[0]<real[0]<=real[1]<rb[1] and hb[0]<imag[0]<=imag[1]<hb[1]
        expected=list(itertools.product(('main','left','half'),('main','half') if beta==0 else('main',),(0,1)))
        assert [(p['incoming_profile'],p['outgoing_profile'],p['nu']) for p in row['profiles']]==expected
        row_uppers=[]
        for profile,(left,right,nu) in zip(row['profiles'],expected):
            trial=list(map(F,profile['trial']));box=target_box(beta,left,right)
            assert len(trial)==len(profile['support_terms'])==5
            support=[]
            for name,x,(lo,hi),term in zip(NAMES,trial,box,profile['support_terms']):
                assert lo<=x<=hi and term['name']==name
                assert (F(term['lower']),F(term['upper']),F(term['trial']))==(lo,hi,x)
                gl,gh=interval(term['gradient'])
                products=[gl*(lo-x),gh*(lo-x),gl*(hi-x),gh*(hi-x)]
                assert products==list(map(F,term['corner_products']))
                assert F(term['upper_rational'])==max(products)>=0
                support.append(max(products));support_count+=1
            low,high=interval(profile['trial_defect'])
            upper=high+sum(support,F(0))
            assert F(profile['upper_rational'])==upper<-F(1,30)
            assert profile['primitive_calls']=={'g':27,'gp':35}
            uppers.append(upper);lowers.append(low);row_uppers.append(upper)
        index=max(range(len(row_uppers)),key=row_uppers.__getitem__)
        worst=row['profiles'][index]
        assert (worst['incoming_profile'],worst['outgoing_profile'],worst['nu'])==('main','main',1)
        summaries.append({'alpha':alpha,'beta':beta,'external_right_type_flag':sigma,
            'profile_count':len(expected),'maximum_upper_rational':str(row_uppers[index]),
            'maximum_upper_decimal_display':float(row_uppers[index]),
            'worst_label':['main','main',1], 'root_radius_rational':str(rho),
            'residual_radius_squared_margin_rational':str(rho*rho-squared_bound)})
    assert len(uppers)==72 and support_count==360
    assert F(source['largest_support_upper_rational'])==max(uppers)
    assert F(source['largest_trial_lower_rational'])==max(lowers)
    verify(PINNED);verify(source['input_sha256'])
    result={'status':'exact saved eight-center third-selection audit passed',
        'source':SOURCE,'source_sha256':PINNED[SOURCE],'checker_sha256':sha(Path(__file__)),
        'input_bindings_checked':len(source['input_sha256']), 'canonical_centers_checked':8,
        'profiles_checked':72,'support_terms_checked':360,'common_gap_rational':'1/30',
        'common_gap_scope':'remaining concave labels at eight prescribed external input pairs only',
        'squared_residual_radius_checked_with_pi_lower_rational':'157/50',
        'summaries':summaries,'largest_support_upper_rational':str(max(uppers)),
        'new_root_source_primitive_or_interval_evaluations':0,
        'whole_domain_or_actual_word_realization_claimed':False}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    with args.output.open('x') as stream:
        json.dump(result,stream,sort_keys=True,indent=2);stream.write('\n')
    print(json.dumps({'status':result['status'],'profiles':72,'supports':360,
                     'common_gap':'1/30','audit_sha256':sha(args.output)}))


if __name__=='__main__':main()
