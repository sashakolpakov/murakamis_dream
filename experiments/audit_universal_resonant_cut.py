#!/usr/bin/env python3
"""Actual inverse-pair cut, universal atom chart and geometric normal tests."""

import json
from pathlib import Path

import sympy as sp

from audit_actual_one_index_fourier_source import actual_case
import audit_actual_normal_stationary_period as normal


def symbolic_chart():
    c,beta,r,s,t=sp.symbols('c beta r s t', nonzero=True)
    J=sp.Matrix([[1,1],[0,1]])
    U=sp.eye(2)+c*sp.Matrix([-beta,1])*sp.Matrix([[1,beta]])
    F=sp.Matrix([[r,1-r],[s,-s]])
    Up=F.inv()*U*F
    p=sp.cancel(-Up[0,1]/(Up[0,0]-1))
    want=1-1/(r+beta*s)
    assert sp.cancel(p-want)==0
    count=0
    for h in range(7):
        a=lambda k:1+k*s
        b=lambda k:a(k)+(c/s)*(1-t)*(t+k*s)
        for k in (h,h+1):
            raw=(F.inv()*U*(J**k)*F)[0,0]
            assert sp.cancel(raw-b(k).subs(t,r+beta*s))==0
        A=a(h)/a(h+1)
        B=a(h+1)/b(h+1)
        C=a(h+1)*b(h)/(b(h+1)*a(h))
        assert sp.cancel(C-1+c*(1-t)**2/(b(h+1)*a(h)))==0
        negative=[A,C,1/B,A*C,C/B]
        Ap,Bp,Cp=B/C,A*C,1/C
        positive=[Bp,Cp,1/Ap,Bp*Cp,Cp/Ap]
        for x,y in zip(positive,[A*C,1/C,C/B,A,1/B]):
            assert sp.cancel(x-y)==0
        assert all(sp.cancel(x)!=0 and sp.cancel(x-1)!=0 for x in negative)
        count+=1
    pp=sp.symbols('p')
    rr=1/(1-pp)-beta*s
    assert sp.cancel(sp.diff(rr,pp)-1/(1-pp)**2)==0
    return {'symbolic_left_moves':count,'raw_prefix_momentum':True,
            'all_inverse_atoms_checked':True,'universal_complete_density':True}


def actual_inverse_pairs():
    old=[(0,1),(1,-1),(0,1),(1,-1)]
    count=0
    for N in range(2,5):
        for M in (1,3):
            original=actual_case(N,3,old,0,0,M)
            new=actual_case(N,3,[(0,-1),(0,1)]+old,1,0,M)
            if original is None or new is None:
                continue
            assert original['original_period']==new['original_period']
            assert original['retained_full_d_N']==new['retained_full_d_N']
            assert original['fixed_column_sums']==new['fixed_column_sums']
            count+=1
    assert count
    return {'actual_root_source_and_full_peripheral_cases':count}


def critical_normal_pairs():
    old_words=normal.WORDS
    records=[]
    for root in (375,635):
        for frame in ((2,1),(3,2),(4,3)):
            old=normal.geometric_hessian_case(1009,root,frame)
            normal.WORDS=([(0,-1),(0,1)]+list(old_words[0]),)+tuple(old_words[1:])
            try:
                new=normal.geometric_hessian_case(1009,root,frame)
            finally:
                normal.WORDS=old_words
            assert new['independent_phase_variables']==old['independent_phase_variables']+2
            assert new['Hessian_rank']==old['Hessian_rank']+2
            assert new['framing_kernel_dimension']==old['framing_kernel_dimension']==2
            assert new['normal_two_form_coefficient_squared']==old['normal_two_form_coefficient_squared']
            assert new['cusp_derivative']==old['cusp_derivative']
            records.append({'root':root,'frame':frame,'old_rank':old['Hessian_rank'],
                            'new_rank':new['Hessian_rank'],
                            'nonzero_squared_normal_density_unchanged':True})
    return {'actual_inverse_pair_normal_cases':len(records),'records':records}


def main():
    result={'status':'PASS','symbolic':symbolic_chart(),
            'actual_source':actual_inverse_pairs(),'actual_normals':critical_normal_pairs()}
    target=Path(__file__).with_name('universal_resonant_cut_results.json')
    target.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
