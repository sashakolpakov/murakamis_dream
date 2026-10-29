#!/usr/bin/env python3
"""Archive eleven existing all-high tail observations, not a theorem.

Only mpmath is needed. This evaluates the actual omitted-zero terms;
normal derivatives are not obtained by differentiating the conjecture.
"""
import json
from pathlib import Path

import mpmath as mp


CHECKED_M=(1,2,3,4,6,8,12,16,24,32,48)


def one_level(m):
    N=3*m+1
    with mp.workdps(3*N+60):
        theta=mp.pi/N
        sine=[mp.mpf(1)]
        for j in range(1,N):
            sine.append(sine[-1]*2*mp.sin(j*theta))
        log1=[mp.mpf(0)];log2=[mp.mpf(0)]
        for j in range(1,3*N):
            # These are log derivatives of the actual regular factorial,
            # with BOTH numerator zeros omitted before specialization.
            L1=j*mp.cot(j*theta)-mp.cot(theta) if j%N else 0
            L2=j*j/mp.sin(j*theta)**2-1/mp.sin(theta)**2 if j%N else 0
            log1.append(log1[-1]+L1);log2.append(log2[-1]+L2)

        C=N*N/sine[2*m]**3
        assert abs(C/(sine[m]**3/N)-1)<mp.mpf('1e-50')
        terms=[];first=[];second=[]
        for k in range(2*m):
            z=2*N-1+k
            indices=[k+1]*4+[2*m-1-k]*3
            term=-2*mp.sin(theta)*N*N*(-1)**k*sine[k]/mp.fprod(sine[j]for j in indices)
            L1=log1[z+1]-mp.fsum(log1[j]for j in indices)
            L2=log2[z+1]-mp.fsum(log2[j]for j in indices)
            terms.append(term)
            # i*T' = sum(term*L1), while T'' = sum(term*(L2-L1^2)).
            first.append(term*L1)
            second.append(term*(L2-L1*L1))
        coherent=mp.fsum(terms)/C
        proposed=-3*mp.sin(theta)*mp.fsum(mp.cot(u*theta)for u in range(1,m+1))
        error=abs(coherent-proposed)
        assert error<mp.mpf('1e-40')
        absolute=mp.fsum(abs(v)for v in terms)/C
        fmt=lambda v:mp.nstr(v,45)
        return {
            'm':m,'N':N,'decimal_working_precision':3*N+60,
            'folded_spins':[m]*6,'all_high_partner_spins':[2*m]*6,
            'true_z_range':[6*m,8*m],'core_z':6*m,
            'tail_z_range':[6*m+1,8*m],
            'coherent_T_over_C':fmt(coherent),
            'proposed_cotangent_expression':fmt(proposed),
            'absolute_numerical_residual':fmt(error),
            'i_D_log_zeta_T_over_C':fmt(mp.fsum(first)/C),
            'D_log_zeta_squared_T_over_C':fmt(mp.fsum(second)/C),
            'absolute_tail_over_C':fmt(absolute),
            'log_absolute_tail_over_C_divided_by_N':fmt(mp.log(absolute)/N),
            'scope':'Numerical comparison only; no finite identity or uniform jet bound inferred.',
        }


if __name__=='__main__':
    levels=[one_level(m)for m in CHECKED_M]
    result={
        'status':'PASS_DIAGNOSTIC',
        'proposed_identity':'T(q)/C(q) = -3 sin(pi/N) sum_{u=1}^m cot(pi*u/N), N=3m+1',
        'root_convention':'q=exp(pi*i/N), Q=q^2, symmetric quantum integers; t=log(zeta/q)',
        'checked_m':list(CHECKED_M),'levels':levels,
        'provenance':'Portable archival version of the previously run eleven-level scratch probe; no larger numerical campaign.',
        'limitations':['No exact proof of the proposed identity.','No certified numerical error bound.','No general nonempty-tail or higher-normal transport theorem.'],
    }
    output=Path(__file__).with_name('all_high_racah_tail_cotangent_diagnostic_results.json')
    output.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    print('PASS_DIAGNOSTIC',len(levels),'previously probed levels; finite cotangent identity remains unproved')
