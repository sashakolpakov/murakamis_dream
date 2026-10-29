#!/usr/bin/env python3
"""Finite exact-root images of an UNPROVED 64-partner value symmetry.

No high-partner normal, completed source frame or asymptotic is estimated.
"""
import itertools
import json
from pathlib import Path

from audit_actual_supported_racah_common_phase_and_normal_metric import forms, value_case
from audit_high_color_first_normal_r_degree import root_field


def level(N):
    p,eta=root_field(N);q=eta*eta%p;D=N-1;M=D//2;sine=[1]
    for r in range(1,N):
        sine.append(sine[-1]*(pow(q,r,p)-pow(q,-r,p))*pow(pow(eta,N,p),-1,p)%p)
    supported=[spins for spins in itertools.product(range(M+1),repeat=6)
               if min(forms(spins)[1])>=D]
    bases=sorted(set([supported[0],supported[len(supported)//2],supported[-1]]))
    rows=[]
    for base in bases:
        _,reference=value_case(N,base,q,p,sine);failures=[];partners=set()
        for bits in itertools.product((0,1),repeat=6):
            partner=tuple(D-spin if bit else spin for bit,spin in zip(bits,base))
            partners.add(partner)
            _,value=value_case(N,partner,q,p,sine)
            if value!=reference:failures.append({'bits':bits,'partner':partner,'W_squared_residue':value})
        rows.append({'folded_base':base,'all_64_bit_patterns_tested':True,
                     'distinct_partner_tuples':len(partners),
                     'reference_W_squared_residue':reference,'failures':failures})
    return {'N':N,'prime':p,'eta_order':4*N,'q_residue':q,'q_order':2*N,
            'normalized_metric':'W_squared=R_root_squared*product_face_d_face',
            'bases':rows}


if __name__=='__main__':
    rows=[level(N) for N in range(3,11)]
    failures=sum(len(base['failures']) for row in rows for base in row['bases'])
    count=64*sum(len(row['bases']) for row in rows)
    result={'status':'DIAGNOSTIC','finite_root_levels':rows,
            'bit_pattern_comparisons':count,'observed_failures':failures,
            'provenance':'Exact computations in specified finite cyclotomic-root images; not a uniform identity proof.',
            'research_lead':'Positive face-normalized W_squared may be invariant under every ell->N-1-ell complement choice.',
            'limits':'No all-level symmetry theorem. The retained [2N] partner tail and its normal derivatives are NOT controlled; value symmetry does not imply a common generic germ, positive completed physical Gram, source transport, or volume limit.'}
    Path(__file__).with_name('supported_racah_partner_value_reflection_diagnostic_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print('DIAGNOSTIC',len(rows),'root levels /',count,'bit patterns /',failures,'observed failures; normals unestimated')
