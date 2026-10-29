"""Exact N-orbit norms of the actual signed crossing shift ratios."""
from __future__ import annotations

import json
import random
from pathlib import Path

from audit_finite_sum_annihilator import field


def case(N):
    p,_,q=field(N)
    Q=q*q%p
    rng=random.Random(743+N)
    checks=0
    examples=0
    while examples<7:
        A,B,C,x=[rng.randrange(1,p) for _ in range(4)]
        Y=Q*x*x%p
        U,V,W,P,X=[pow(z,N,p) for z in (A,B,C,Y,x)]
        if not all(z%p for z in (1-V,1-U,1-W,U-P*W,V-P*W)):
            continue
        def div(a,b):return a*pow(b%p,-1,p)%p
        def positive(a,b,c):
            return [div(b*c,x)*div(1-div(Y,Q*a),1-div(Y*c,Q*a))%p,
                    div(a,c*x)*div(1-Q*b*c,1-Q*b)%p,
                    div(-a,Q*b*c*x)*div((1-Q*b*c)*(1-div(Y*c,a)),1-Q*c)%p]
        def negative(a,b,c):
            return [div(x,b)*div(1-Q*a*c,1-Q*a)%p,
                    div(x,a)*div(1-div(Y,Q*b),1-div(Y*c,Q*b))%p,
                    div(1,x)*div((1-Q*a*c)*(1-div(Y*c,b)),1-Q*c)%p]
        try:
            got=[]
            for ratio in (positive,negative):
                norms=[]
                for axis in range(3):
                    total=1
                    for j in range(N):
                        args=[A,B,C]
                        args[axis]=args[axis]*pow(Q,j,p)%p
                        total=total*ratio(*args)[axis]%p
                    norms.append(total)
                got.append(norms)
            expected=[
                [div(V*W,X)*div(1-div(P,U),1-div(P*W,U))%p,
                 div(U,W*X)*div(1-V*W,1-V)%p,
                 div(-U,V*W*X)*div((1-V*W)*(1-div(P*W,U)),1-W)%p],
                [div(X,V)*div(1-U*W,1-U)%p,
                 div(X,U)*div(1-div(P,V),1-div(P*W,V))%p,
                 div(1,X)*div((1-U*W)*(1-div(P*W,V)),1-W)%p]]
        except ValueError:
            continue
        assert got==expected,(N,got,expected)
        assert X*X%p==P
        checks+=6
        examples+=1
    return {'N':N,'prime':p,'actual_signed_norm_checks':checks,
            'even_level_phase_retained':N%2==0}


def main():
    cases=[case(N) for N in range(2,13)]
    result={'status':'pass','cases':cases,
            'checks':sum(c['actual_signed_norm_checks'] for c in cases),
            'scope':'Exact local crossing norm table only; no source projection or volume asymptotic inferred.'}
    path=Path(__file__).with_name('actual_signed_crossing_norms_results.json')
    path.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'pass','levels':len(cases),'checks':result['checks'],
                      'results':str(path)},indent=2))


if __name__=='__main__':main()
