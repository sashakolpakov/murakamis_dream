#!/usr/bin/env python3
"""Exact three-coefficient source certificate; no numerical inequality fit."""
import json
import math
from pathlib import Path

import sympy as sp
from sympy import QQ


def main():
    N=7;D=N-1;order=3;x=sp.symbols('x')
    field=QQ.alg_field_from_poly(sp.Poly(sp.cyclotomic_poly(14,x),x),'q',root_index=3)
    q=field([1,0]);zero=field.zero;one=field.one
    assert q**7==-one and q**14==one
    r=q+q**-1
    assert r**3-r*r-2*r+one==zero
    def mul(a,b):
        return [sum((a[j]*b[k-j] for j in range(k+1)),zero) for k in range(order)]
    def divide(a,b):
        assert b[0]!=zero
        out=[]
        for k,v in enumerate(a):
            out.append((v-sum((b[j]*out[k-j] for j in range(1,k+1)),zero))/b[0])
        return out
    def power(u):
        return [q**u*field.convert(sp.Rational(u**k,math.factorial(k))) for k in range(order)]
    rho=[a-b for a,b in zip(power(1),power(-1))]
    units=[divide([a-b for a,b in zip(power(u),power(-u))],rho) for u in range(3*N+1)]
    unit=[one,zero,zero];fac=[unit];noN=[unit]
    for u in range(1,len(units)):
        fac.append(mul(fac[-1],units[u]))
        noN.append(noN[-1] if u==N else mul(noN[-1],units[u]))
    def metric_jet(labels):
        a,b,c,d,e,f=labels
        faces=[(a,b,e),(c,d,e),(a,d,f),(b,c,f)]
        F=list(map(sum,faces));Q=[a+b+c+d,a+c+e+f,b+d+e+f]
        assert min(Q)<=2*D
        G=[zero]*order;U=unit
        for z in range(max(F),min(Q)+1):
            den=unit
            for n in [z-u for u in F]+[u-z for u in Q]:
                assert 0<=n<=D
                den=mul(den,fac[n])
            term=divide(noN[z+1],den)
            G=[a+(-1)**(D+z)*b for a,b in zip(G,term)]
        for triangle,Fv in zip(faces,F):
            numerator=unit
            for j in triangle:
                numerator=mul(numerator,fac[Fv-2*j])
            df=divide(numerator,noN[Fv+1])
            U=mul(U,[(-1)**(Fv-D)*v for v in df])
        return mul(mul(G,G),U)
    total=[zero]*order;records=[]
    for e in (2,4):
        for f in (2,4):
            jet=metric_jet((2,2,2,2,e,f))
            assert jet[0]==(one+r)**2
            weighted=mul(mul(units[2*e+1],units[2*f+1]),jet)
            total=[a+b for a,b in zip(total,weighted)]
            records.append({'e':e,'f':f,'K_Taylor_coefficients':[str(field.to_sympy(v)) for v in jet]})
    assert total[0]==total[1]==zero
    expected_coefficient=3444-5180*r-6440*r*r
    assert total[2]==expected_coefficient
    cN2=units[N][1]**2
    assert cN2==-28-28*r-56*r*r
    trace=total[2]/cN2
    assert trace==24*r*r+20*r-11
    # Exact ordinary cyclotomic polynomial check, independent of the jet code.
    polynomial=sp.expand((-28-28*x-56*x*x)*(24*x*x+20*x-11)-(3444-5180*x-6440*x*x))
    assert sp.rem(polynomial,x**3-x*x-2*x+1,x)==0
    result={
        'status':'PASS',
        'N':N,'external_spins':[2,2,2,2],
        'selected_cluster_channels':[2,4],
        'ordinary_invariant_dimension':5,'cluster_ranks':[2,2],
        'coefficient_field':'Q[q]/(q^6-q^5+q^4-q^3+q^2-q+1), q=exp(pi i/7)',
        'real_parameter':'r=q+q^-1=2cos(pi/7)',
        'real_minimal_polynomial':'r^3-r^2-2r+1',
        'shared_root_W_squared':'(1+r)^2',
        'weighted_Ward_Taylor_coefficients':['0','0','3444-5180r-6440r^2'],
        'leading_N_quantum_integer_coefficient_squared':'-28-28r-56r^2',
        'exact_cluster_overlap':'24r^2+20r-11',
        'strict_inequality_proof':'r>1 since pi/7<pi/3, so overlap>33>2',
        'individual_source_germs':records,
        'conclusion':'No common positive Hermitian form makes both actual complete selected cluster projectors orthogonal.',
        'limitations':['Not a counterexample to higher scalar normal bounds.',
                       'Does not exclude weighted nonorthogonal transport metrics.',
                       'No asymptotic growth claim is inferred from this finite example.'],
    }
    path=Path(__file__).with_name('actual_cluster_projector_positive_metric_obstruction_results.json')
    path.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS exact N7 source jets: rank2/rank2 cluster overlap=24r^2+20r-11>33>2')

if __name__=='__main__':
    main()
