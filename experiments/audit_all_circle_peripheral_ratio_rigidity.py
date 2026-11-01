#!/usr/bin/env python3
"""Exact local identities used by the peripheral-ratio rigidity argument.

The geometric integrality and all-fiber representation arguments are
written proofs; these checks verify their displayed algebraic formulas.
"""
import argparse
import hashlib
import json
from pathlib import Path
import sympy as s


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    M,E,Q,P,X,Y,t = s.symbols('M E Q P X Y t', nonzero=True)
    records = []
    def check(name, expression):
        value = s.cancel(expression)
        if value != 0:
            raise AssertionError((name,value))
        records.append(name)
    def ld(value,var):
        return s.cancel(var*s.diff(value,var)/value)

    quotient = ((E+Q)*(E+1/Q)*(E+P)*(E+1/P)
                /((E-1)**2*(1-E*M**2)*(1-E/M**2)))
    f=(M**2-E)/(1-M**2*E)
    rhoq=(Q+E)/(1+Q*E)
    rhop=(P+E)/(1+P*E)
    Fu,Fq,Fp,Fz=[ld(quotient,var) for var in [M,Q,P,E]]
    check('main derivative of edge relation', Fu-2*ld(f,E))
    check('first auxiliary derivative', Fq+ld(rhoq,E))
    check('second auxiliary derivative', Fp+ld(rhop,E))
    # Eliminate dz using dF=0 and check all coefficients of the
    # alternating two-form, rather than evaluating a numerical sample.
    Ez=[-Fu/Fz,-Fq/Fz,-Fp/Fz]
    vars=[M,Q,P]
    df=[ld(f,v)+ld(f,E)*Ez[i] for i,v in enumerate(vars)]
    drq=[ld(rhoq,v)+ld(rhoq,E)*Ez[i] for i,v in enumerate(vars)]
    drp=[ld(rhop,v)+ld(rhop,E)*Ez[i] for i,v in enumerate(vars)]
    check('closed form du wedge dq',df[1]+drq[0]/2)
    check('closed form du wedge dp',df[2]+drp[0]/2)
    check('closed form dq wedge dp',-drq[2]/2+drp[1]/2)

    beta,gamma,D=Q+1/Q,P+1/P,M**2+M**-2
    S=beta+gamma+D+2
    numerator=2*D-beta*gamma
    H=(Q-1)**2*(P-1)**2-4*(M+1/M)**2*Q*P
    check('edge quadratic discriminant squareclass',
          numerator**2-4*S**2-((Q+1)*(P+1)/(Q*P))**2*H)
    Hxy=(X-1)**2*(Y-1)**2-4*t*X*Y
    check('discriminant proving prime edge divisor',
          s.discriminant(Hxy,Y)-16*t*X*(X**2+(t-2)*X+1))
    check('simple valuation at X zero',
          s.diff(s.discriminant(Hxy,Y),X).subs(X,0)-16*t)
    check('primitive coefficients at X one',Hxy.subs(X,1)+4*t*Y)
    check('trace-zero split fiber',H.subs(M,s.I)-(Q-1)**2*(P-1)**2)
    check('main factors at unipotent eigenvalues',f.subs(M,1)-1)
    check('main factor at trace zero',f.subs(M,s.I)+1)
    result={
        'scope':'Exact local rational and discriminant identities; geometric gluing and unit regularity require their written proofs.',
        'count':len(records),'checks':records,'all_exact':True,
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'count':len(records),'all_exact':True}))


if __name__=='__main__':
    main()
