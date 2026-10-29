#!/usr/bin/env python3
"""Paired-precision actual moments and quarantined finite Racah checks.

This is a diagnostic audit, NOT a uniform conditioning theorem or a
proof of the finite generic source/Racah transformation.
"""
import itertools
import json
from pathlib import Path

import mpmath as mp

from audit_actual_generic_six_head_tetrahedral_source import Generic
from diagnose_actual_marked_boundary_conditioning import measure


def finite_racah_candidate(N,q=2,p=1000003):
    g=Generic(N,q,p)
    qfac=[pow(q,-n*(n-1)//2,p)*g.fac[n]*pow(1-g.Q,-n,p)%p for n in range(3*N+1)]
    count=0
    for a,b,c in itertools.product(range(N),repeat=3):
        J=a+b+c
        if min(b+c-a,a+b-c,a+c-b)<0:continue
        S=0
        for t in range(max(a,b,c,J-g.d),min(a+b,a+c,b+c)+1):
            den=qfac[g.d+t-J]
            for j in (a,b,c):den=den*qfac[t-j]*qfac[J-j-t]%p
            S=(S+(-1)**(g.d+t)*qfac[N+t]*pow(den,-1,p))%p
        exponent=a*a-b*b+c*c-a*b-a*c+b*c-c*g.d
        proposed=(-1)**J*pow(q,exponent,p)*qfac[a]*qfac[b]*qfac[c]*pow(qfac[J+1],-1,p)*S%p
        assert proposed==g.regular_corner_sum((a,b,c))
        count+=1
    return {'N':N,'generic_parameter':q,'prime':p,'all_triangle_candidate_checks':count,
            'scope':'Finite checks only; the generic finite transformation is not proved by this audit.'}


def paired(N,labels,dps):
    first=measure(N,labels,dps,1)
    second=measure(N,labels,dps+70,2)
    with mp.workdps(80):
        a=[mp.mpc(*v) for v in first['normalized_moments']]
        b=[mp.mpc(*v) for v in second['normalized_moments']]
        delta=max(abs(x-y) for x,y in zip(a,b))
        assert delta<mp.mpf(N)**-7
        assert mp.mpf(second['top_moment_relative_error'])<mp.mpf(N)**-7
        Kdelta=abs(mp.mpf(first['K'])-mp.mpf(second['K']))
        assert Kdelta<mp.mpf(N)**-7
    return {'N':N,'labels':list(labels),'first_precision':dps,'second_precision':dps+70,
            'normal_step_ratio':2,'maximum_normalized_moment_difference':mp.nstr(delta,20),
            'K_difference':mp.nstr(Kdelta,20),'refined_actual_source_measurement':second}


if __name__=='__main__':
    checks=[finite_racah_candidate(N,2) for N in range(2,9)]
    checks += [finite_racah_candidate(N,3) for N in range(2,7)]
    rows=[paired(16,(7,7,7),150),paired(64,(31,31,31),180),
          paired(128,(51,51,51),240),paired(129,(32,32,64),260),
          paired(256,(127,127,127),360)]
    out={'status':'PASS_DIAGNOSTIC','finite_generic_Racah_candidate':checks,
         'paired_precision_actual_moments':rows,
         'scope':'Actual source moments from proved generic Clebsch/trace formulas, measured with two normal steps and two precisions. No finite-source identity or uniform K bound follows from the finite samples.'}
    Path(__file__).with_name('actual_marked_boundary_conditioning_diagnostic_results.json').write_text(json.dumps(out,indent=2)+'\n')
    print('PASS_DIAGNOSTIC 12 generic finite candidate families;5 paired-precision actual boundary moment profiles')
