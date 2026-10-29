#!/usr/bin/env python3
"""Exact source-to-monodromy chain maps and the retained normal cut."""

import json
from pathlib import Path

import sympy as s

Q,Y,U=s.symbols('Q Y U')


def simp(x):
    return s.cancel(s.expand(x))


def mat_simp(M):
    return M.applyfunc(simp)


def shift(v,power=1):
    return v.subs(Y,Q**power*Y)


def companion_checks():
    records=[]
    # A rational gauge is used only as an exact check, not as a knot model.
    g=1+Q*Y
    a=simp(shift(g)/g)
    for level,root in ((2,s.Integer(-1)),(3,(-1+s.sqrt(3)*s.I)/2)):
        for degree in (1,2):
            if degree==1:
                coeff=[-a,s.Integer(1)]
            else:
                coeff=[2*a,-shift(a)-2,s.Integer(1)]
            A=s.zeros(degree)
            for j in range(degree-1):A[j,j+1]=1
            for j in range(degree):A[degree-1,j]=-coeff[j]/coeff[-1]
            B=mat_simp(A.inv())
            e=s.zeros(degree,1);e[-1]=1
            r=mat_simp(B*e/coeff[-1])
            def T(v):return mat_simp(B*shift(v))
            def J(f):return s.Matrix([shift(f,j) for j in range(degree)])
            def P(f):return simp(sum(coeff[j]*shift(f,j) for j in range(degree+1)))
            f=g*(1-Y**level)
            v=J(f)
            assert mat_simp(T(v)-v-r*P(f))==s.zeros(degree,1)
            term=r*P(f);source=term
            for _ in range(1,level):
                term=T(term);source=mat_simp(source+term)
            transport=v
            for _ in range(level):transport=T(transport)
            assert mat_simp(transport-v-source)==s.zeros(degree,1)
            # Source from the actual supplied Q-germ, not an assumed flat lift.
            h1=simp((Q*s.diff(P(f),Q)).subs(Q,root))
            aroot=A.subs(Q,root).applyfunc(simp)
            broot=B.subs(Q,root).applyfunc(simp)
            rroot=r.subs(Q,root).applyfunc(simp)
            def T0(v):return mat_simp(broot*v.subs(Y,root*Y))
            term=rroot*h1;sourced=term
            for _ in range(1,level):
                term=T0(term);sourced=mat_simp(sourced+term)
            H=s.eye(degree)
            for j in range(level):H=mat_simp(H*shift(B,j))
            H0=H.subs(Q,root).applyfunc(simp)
            H1=(Q*H.diff(Q)).subs(Q,root).applyfunc(simp)
            v0=v.subs(Q,root).applyfunc(simp)
            L1v0=mat_simp(H1*v0+level*H0*(Y*v0.diff(Y)))
            left=(H0-s.eye(degree)).T.nullspace()
            assert len(left)==1
            for ell in left:
                assert simp((ell.T*(L1v0-sourced))[0])==0
            # Direct normal chain identity, with scalar f0 held fixed in Q.
            f0=f.subs(Q,root)
            P1f0=simp((Q*s.diff(P(f0),Q)).subs(Q,root))
            term=rroot*P1f0;normal_rhs=term
            for _ in range(1,level):
                term=T0(term);normal_rhs=mat_simp(normal_rhs+term)
            J0f0=J(f0).subs(Q,root).applyfunc(simp)
            normal_lhs=mat_simp(H1*J0f0+level*H0*(Y*J0f0.diff(Y)))
            for ell in left:assert simp((ell.T*(normal_lhs-normal_rhs))[0])==0
            assert h1!=0
            records.append({'level':level,'scalar_order':degree,
                            'generic_chain_identity':True,
                            'actual_nonzero_source':True,
                            'normal_chain_identity_mod_monodromy_image':True})
    return records


def reduce_power(f,level):
    out=[s.Integer(0)]*level
    f=s.expand(f)
    for term in s.Add.make_args(f):
        power=int(term.as_powers_dict().get(Y,0))
        coeff=term/Y**power
        quotient,remainder=divmod(power,level)
        out[remainder]+=coeff*U**quotient
    return [simp(c) for c in out]


def cut_and_cyclic_checks():
    records=[]
    X=Y+1/Y
    # The monomial basis (1-Y)X^n spans the same lattice as Newton v_n
    # and avoids any algebraic-number simplification in envelope checks.
    for level in range(2,12):
        basis=[s.expand((1-Y)*X**n) for n in range(level)]
        matrix=s.Matrix.hstack(*(s.Matrix(reduce_power(f,level)) for f in basis))
        ideals=[]
        for j in range(level):
            row=[s.expand(U**level*matrix[j,n]) for n in range(level)]
            gcd=s.Poly(0,U)
            for entry in row:gcd=s.gcd(gcd,s.Poly(entry,U))
            factors=s.factor(gcd.as_expr())
            # Remove powers of U, which are units in A=k[U,U^-1].
            while factors!=0 and factors.subs(U,0)==0:
                factors=s.cancel(factors/U)
            factors=s.Poly(factors,U).monic().as_expr()
            expected=U-1 if level%2 and j==(level+1)//2 else s.Integer(1)
            assert s.expand(factors-expected)==0
            ideals.append(str(expected))
        # e2(X)v0 in physical coordinates and its exact Bockstein cut.
        C0=s.Integer(2);C1=X
        for _ in range(1,level):C0,C1=C1,s.expand(X*C1-C0)
        generator=simp((1-Y)*(C1-2)/(level**2*(X-2)))
        expected=-Y*(Y**level-1)*sum(Y**j for j in range(level))/(level**2*Y**level)
        assert simp(generator-expected)==0
        assert simp(-s.diff(generator,Y).subs(Y,1)-1)==0
        normal=simp(generator/(Y**level-1))
        assert simp(normal.subs(Y,1)+s.Rational(1,level))==0
        # X-2 kills this abstract fiber class: its product lies in wL.
        quotient=simp((X-2)*generator/(Y**level-1))
        # quotient=(1-Y)(U-1)/(N^2 U) is visibly in L.
        assert simp(quotient-(1-Y)*(Y**level-1)/(level**2*Y**level))==0
        records.append({'level':level,'cyclic_character_ideals':ideals,
                        'normal_X_two_cut':1,'divided_normal_value':f'-1/{level}'})
    zeta=(-1+s.sqrt(3)*s.I)/2
    assert simp((1+zeta)+zeta**2)==0
    assert simp(2*zeta**2-(-zeta**2))!=0
    return records


def main():
    result={'scalar_companion_source_maps':companion_checks(),
            'normal_cut_and_parity_envelope':cut_and_cyclic_checks(),
            'scope':'Actual-source structural maps, no regulator comparison or norm identity.'}
    path=Path(__file__).with_name('source_lattice_monodromy_chainmap_results.json')
    path.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'scalar_companion_normal_cases':len(result['scalar_companion_source_maps']),
                      'normal_cut_and_envelope_levels':len(result['normal_cut_and_parity_envelope']),
                      'output':str(path)},indent=2))


if __name__=='__main__':main()
