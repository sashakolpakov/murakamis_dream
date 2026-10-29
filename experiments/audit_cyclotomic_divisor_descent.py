#!/usr/bin/env python3
"""Finite divisor-flow gauges and all-level cyclic transports.

Tests a restricted uniform rank-one descent theorem. No comparison
line for the original knot period is assumed or inferred.
"""

import json
from pathlib import Path

import sympy as s


def cumulative_flow(charges):
    answer={}
    for c in sorted({c for c,u in charges}):
        indices=[u for label,u in charges if label == c]
        current=0
        for u in range(min(indices),max(indices)+1):
            current-=charges.get((c,u),0)
            if current:
                answer[c,u]=current
        assert current == 0
    return answer


def symbolic_gauge():
    q,Y=s.symbols('q Y',nonzero=True)
    charges={(1,-1):1,(1,1):-1,(2,0):-2,(2,1):2}
    flow=cumulative_flow(charges);k=-1
    a=q**(2*k)*s.prod((1-c*q**(2*u)*Y)**n for (c,u),n in charges.items())
    f=Y**k*s.prod((1-c*q**(2*u)*Y)**n for (c,u),n in flow.items())
    assert s.cancel(f.subs(Y,q*q*Y)/f-a) == 0
    anchored=s.cancel(f/f.subs(Y,3))
    assert s.cancel(anchored.subs(Y,3)-1) == 0
    assert s.cancel(anchored.subs(Y,q*q*Y)/anchored-a) == 0
    return {'generic_gauge_and_pointing_exact':True,
            'input_charges':[[c,u,n] for (c,u),n in charges.items()],
            'finite_cumulative_flow':[[c,u,n] for (c,u),n in flow.items()],
            'scalar_character_k':k}


def finite_field(level):
    quotient=(10000+2*level-1)//(2*level)
    while not s.isprime(2*level*quotient+1):
        quotient+=1
    p=int(2*level*quotient+1)
    g=int(s.primitive_root(p));q=pow(g,(p-1)//(2*level),p)
    assert pow(q,level,p) == p-1
    return p,g,q


def cyclic_transports():
    gauges=[(-2,{(1,-2):1,(1,0):-1,(2,0):-2,(2,3):2}),
            (0,{(1,-3):-2,(1,-1):1,(1,2):1,(3,-1):2,(3,1):-2}),
            (3,{(2,-2):2,(2,1):-2,(3,0):-1,(3,4):1})]
    records=[]
    for k,charges in gauges:
        flow=cumulative_flow(charges)
        labels={c for c,u in charges}
        for c in labels:
            positions={u for label,u in charges if label == c}
            positions.update(u for label,u in flow if label == c)
            for u in range(min(positions)-1,max(positions)+2):
                assert charges.get((c,u),0) == flow.get((c,u-1),0)-flow.get((c,u),0)
        for N in range(2,18):
            p,g,q=finite_field(N);Q=q*q%p
            def value(Y, use_flow=False):
                data=flow if use_flow else charges
                result=pow(Y,k,p) if use_flow else pow(q,2*k,p)
                for (c,u),n in data.items():
                    factor=(1-c*pow(Q,u,p)*Y)%p
                    if factor == 0:return None
                    result=result*pow(factor,n,p)%p
                return result
            chosen=None
            for exponent in range(1,300):
                Y=pow(g,exponent,p)
                orbit=[value(Y*pow(Q,j,p)%p) for j in range(N)]
                f=value(Y,True);shifted=value(Q*Y%p,True)
                if None not in orbit and f is not None and shifted is not None:
                    chosen=Y;break
            assert chosen is not None
            norm=1
            for item in orbit:norm=norm*item%p
            assert norm == 1
            assert shifted*pow(f,-1,p)%p == value(chosen)
            records.append({'level':N,'prime':p,'character_k':k,
                            'full_orbit_norm':norm,'fixed_gauge_intertwines':True})
    return records


def parity_and_halfstep():
    records=[]
    for N in range(2,18):
        p,g,q=finite_field(N);Q=q*q%p
        chosen=None
        for power in range(1,300):
            Y=pow(g,power,p);U=pow(Y,N,p)
            orbit=[Y*pow(Q,j,p)%p for j in range(N)]
            if all((1-x*x)%p and (1-x)%p and (1-q*x)%p and (1+q*x)%p
                   for x in orbit) and (1-U)%p and (1+U)%p:
                chosen=Y;break
        assert chosen is not None
        square_norm=1;half_norm=1;alias_norm=1;other_root_norm=1
        for x in orbit:
            square_norm=square_norm*(1-Q*x*x)*pow((1-x*x)%p,-1,p)%p
            half_norm=half_norm*(1-q*x)*pow((1-x)%p,-1,p)%p
            alias_norm=alias_norm*(1-x)*(1-q*x)*pow(((1+x)*(1+q*x))%p,-1,p)%p
            other_root_norm=other_root_norm*(1-x)*(1+q*x)*pow(((1+x)*(1-q*x))%p,-1,p)%p
        half=(1+U)*pow((1-U)%p,-1,p)%p
        assert half_norm == half
        assert square_norm == (1 if N%2 else half*half%p)
        assert alias_norm == 1
        if N%2:
            inverse_half=(1-U)*pow((1+U)%p,-1,p)%p
            assert other_root_norm == inverse_half*inverse_half%p
            assert other_root_norm != 1
        else:
            assert other_root_norm == 1
        assert pow(-1,N,p) == (1 if N%2 == 0 else p-1)
        records.append({'level':N,'quadratic_orbit_transport':square_norm,
                        'odd_only_descent_countercheck':N%2 == 1,
                        'all_selected_halfroots_hide_generic_divisor_obstruction':True,
                        'missing_odd_order_place_detects_it':N%2 == 1,
                        'halfstep_peripheral_ratio_retained':True})
    return records


def moving_algebraic_divisors():
    q,Y=s.symbols('q Y',nonzero=True)
    root=s.sqrt(1+q)
    betas=[3+root,3-root]
    alphas=[q*q*b for b in betas]
    polynomial=1-6*Y+(8-q)*Y*Y
    gauge=Y*Y*polynomial
    reconstructed=Y*Y*s.prod(1-b*Y for b in betas)
    assert s.simplify(s.expand(reconstructed-gauge)) == 0
    shifts=[]
    for a,b in zip(alphas,betas):
        ki=s.simplify((s.diff(a,q)/a-s.diff(b,q)/b).subs(q,1)/2)
        assert ki == 1
        assert s.simplify(a/(q**(2*ki)*b)-1) == 0
        shifts.append(int(ki))
    limits=[b.subs(q,1) for b in betas]
    assert all(c.is_positive for c in limits)
    assert all(s.simplify(limits[0]**k-limits[1]**k) != 0 for k in (1,2))
    assert s.simplify(polynomial.subs(Y,q*q*Y)/polynomial
                      -s.prod(1-a*Y for a in alphas)/s.prod(1-b*Y for b in betas)) == 0
    A=2+q;B=3+q*q
    moving_gauge=Y**-1*(1-A*Y)/(1-B*Y)
    moving_coefficient=s.cancel(moving_gauge.subs(Y,q*q*Y)/moving_gauge)
    expected=q**-2*(1-q*q*A*Y)*(1-B*Y)/((1-A*Y)*(1-q*q*B*Y))
    assert s.cancel(moving_coefficient-expected) == 0
    moving_shifts=[]
    for a,b in ((q*q*A,A),(B,q*q*B)):
        ki=s.simplify((s.diff(a,q)/a-s.diff(b,q)/b).subs(q,1)/2)
        moving_shifts.append(int(ki))
    assert moving_shifts == [1,-1]
    records=[]
    for N in range(2,18):
        p,g,q0=finite_field(N);Q=q0*q0%p
        def f(Y,kind):
            if kind == 'quadratic':
                return Y*Y*(1-6*Y+(8-q0)*Y*Y)%p
            denominator=(1-(3+q0*q0)*Y)%p
            if not denominator:return None
            return pow(Y,-1,p)*(1-(2+q0)*Y)*pow(denominator,-1,p)%p
        for kind in ('quadratic','linear_moving'):
            chosen=None
            for power in range(1,300):
                Y0=pow(g,power,p)
                values=[f(Y0*pow(Q,j,p)%p,kind) for j in range(N+1)]
                if all(v is not None and v != 0 for v in values):
                    chosen=Y0;break
            assert chosen is not None
            total=1
            for j in range(N):
                total=total*values[j+1]*pow(values[j],-1,p)%p
            assert total == 1
            records.append({'level':N,'kind':kind,'all_level_transport':total})
    return {'algebraic_splitting_field_gauge_descends_exactly':True,
            'unramified_positive_distinct_limiting_roots':True,
            'algebraic_branch_shifts_from_first_q_derivatives':shifts,
            'moving_rational_seed_shifts':moving_shifts,
            'independent_transports':records}


def main():
    result={'symbolic_fixed_gauge':symbolic_gauge(),
            'independent_cyclic_transport_checks':cyclic_transports(),
            'parity_and_halfstep_checks':parity_and_halfstep(),
            'unramified_moving_divisors':moving_algebraic_divisors(),
            'scope':'Rank-one descent under explicit split or unramified nonresonant divisor hypotheses; no actual knot comparison line or volume theorem.'}
    output=Path(__file__).with_name('cyclotomic_divisor_descent_results.json')
    output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'fixed_gauge_exact':True,
                      'independent_cyclic_transports':len(result['independent_cyclic_transport_checks']),
                      'parity_and_halfstep_checks':len(result['parity_and_halfstep_checks']),
                      'moving_algebraic_divisor_transports':len(result['unramified_moving_divisors']['independent_transports']),
                      'output':str(output)},indent=2))


if __name__ == '__main__':
    main()
