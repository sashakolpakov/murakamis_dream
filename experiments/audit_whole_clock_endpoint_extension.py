"""Integral whole Jackson endpoint tower and actual spectral defect."""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


def main():
    x,Z,c,delta=sp.symbols('x Z c delta',nonzero=True)
    tower=[]
    for L in range(1,9):
        P=sp.prod(x-c*Z**r for r in range(L+1))
        Pold=sp.prod(x-c*Z**r for r in range(L))
        D=sp.cancel((P-P.subs(x,Z*x))/(1-Z))
        quotient,remainder=sp.div(D,Pold,x)
        assert sp.expand(remainder)==0
        assert sp.cancel(quotient).as_numer_denom()[1]==1
        assert sp.expand(D.subs(Z,1)-x*sp.diff(P.subs(Z,1),x))==0
        for power in (-3,-1,0,1,L,L+2):
            g=x**power
            Dg=sp.cancel((g-g.subs(x,Z*x))/(1-Z))
            assert sp.cancel(Dg.subs(Z,1)-x*sp.diff(g,x))==0
        tower.append({'L':L,'integral_monic_divisibility':True,
                      'root_confluent_Euler_map':True})
    defects=[]
    for N in range(2,10):
        P=sp.prod(x-c*Z**r for r in range(N+1))
        top=sp.expand(P.subs(x,c*Z**(N+1)))
        expected=c**(N+1)*Z**(N*(N+1)//2)*sp.prod(Z**j-1 for j in range(1,N+2))
        assert sp.expand(top-expected)==0
        current=sp.cancel(-top/(1-Z))
        leading=sp.limit(current/(1-Z)**N,Z,1)
        assert leading==(-1)**N*c**(N+1)*sp.factorial(N+1)
        e_lengths=[sp.Rational(1,(k+1)*(N-k)) for k in range(N)]
        f_lengths=[sp.Rational(1,k*(N-k+1)) for k in range(1,N+1)]
        assert max(e_lengths)==max(f_lengths)==sp.Rational(1,N)
        defects.append({'N':N,'actual_top_endpoint_order':N,
                        'leading_sign':(-1)**N,
                        'inverse_arrow_norm_squared':str(sp.Rational(1,N))})
    result={'status':'pass','integral_tower':tower,'actual_spectral_defects':defects,
            'scope':'Whole function extension and root primitive metric; no tensor/Hopf/Gaussian current identification.'}
    path=Path(__file__).with_name('whole_clock_endpoint_extension_results.json')
    path.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'pass','tower_levels':len(tower),
                      'actual_spectral_levels':len(defects),'results':str(path)},indent=2))


if __name__=='__main__':main()
