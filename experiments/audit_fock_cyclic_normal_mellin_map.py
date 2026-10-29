#!/usr/bin/env python3
"""Whole-normal cyclic carries, Mellin map, relative chain and log residue."""

import json
import math
from pathlib import Path

import sympy as s

from audit_finite_sum_annihilator import field


def cyclic_case(N):
    p,g,q=field(N);Q=q*q%p;length=8;invN=pow(N,-1,p)
    zero=[0]*length
    def padd(a,b):return [(x+y)%p for x,y in zip(a,b)]
    def pscale(a,c):return [v*c%p for v in a]
    def pmul(a,b):
        return [sum(a[j]*b[n-j] for j in range(n+1))%p for n in range(length)]
    def pexp(c):return [pow(c%p,n,p)*pow(math.factorial(n),-1,p)%p for n in range(length)]
    def cadd(a,b):return [padd(x,y) for x,y in zip(a,b)]
    def cscale(a,c):return [pscale(v,c) for v in a]
    def cp(a,poly):return [pmul(v,poly) for v in a]
    def cmul(a,b):
        out=[zero[:] for _ in range(N)];U=pexp(1)
        for i in range(N):
            for j in range(N):
                value=pmul(a[i],b[j])
                if i+j>=N:value=pmul(value,U)
                out[(i+j)%N]=padd(out[(i+j)%N],value)
        return out
    def derivative(a):
        out=[]
        for j,v in enumerate(a):
            d=[(n+1)*v[n+1]%p for n in range(length-1)]+[0]
            out.append(padd(d,pscale(v,j*invN%p)))
        return out
    def same_lower(a,b):return all(x[:-1]==y[:-1] for x,y in zip(a,b))
    one=[zero[:] for _ in range(N)];one[0][0]=1
    eps=[]
    for j in range(N):
        eps.append([pscale(pexp(-ell*invN),invN*pow(Q,-j*ell,p)%p)
                    for ell in range(N)])
    total=[zero[:] for _ in range(N)]
    for e in eps:total=cadd(total,e)
    assert total==one
    for i in range(N):
        assert same_lower(derivative(eps[i]),[zero[:] for _ in range(N)])
        assert eps[i][0]==pscale(pexp(0),invN)
        for j in range(N):
            expected=eps[i] if i==j else [zero[:] for _ in range(N)]
            assert cmul(eps[i],eps[j])==expected
        for r in range(4):
            monomial=zero[:];monomial[r]=pow(math.factorial(r),-1,p)
            image=cp(eps[i],monomial)
            expected=[zero[:] for _ in range(N)]
            if r:
                previous=zero[:];previous[r-1]=pow(math.factorial(r-1),-1,p)
                expected=cp(eps[i],previous)
            assert same_lower(derivative(image),expected)
        for k in (-2,0,1,3):
            character=cp(eps[i],pexp(k))
            assert character[0]==pscale(pexp(k),invN)
    # The reduced root representative and literal clock power have
    # different whole-normal lifts, related by the retained U factor.
    x=-pow(q,-1,p)%p
    pivot=[zero[:] for _ in range(N)]
    pivot[N-1]=pscale(pexp(-1),pow(x,1-N,p))
    inverse=[zero[:] for _ in range(N)];inverse[1]=pscale(pexp(0),pow(x,N-1,p))
    assert cmul(pivot,inverse)==one
    literal=cp(pivot,pexp(1))
    literal_inverse=cp(inverse,pexp(-1))
    assert cmul(literal,literal_inverse)==one
    clock_inverse=[zero[:] for _ in range(N)]
    clock_inverse[1]=pscale(pexp(0),pow(x,-1,p))
    actual_clock_power=one
    for _ in range(N-1):actual_clock_power=cmul(actual_clock_power,clock_inverse)
    assert actual_clock_power==literal
    alpha=pexp(invN)
    for j in range(N):
        moved=cp(cmul(pivot,eps[j]),alpha)
        expected=cscale(eps[j],pow(x,1-N,p)*pow(Q,-j,p)%p)
        assert moved==expected
        literal_moved=cp(cmul(literal,eps[j]),pexp(-(N-1)*invN))
        assert literal_moved==expected
    assert same_lower(derivative(pivot),cscale(pivot,-invN))
    assert same_lower(derivative(inverse),cscale(inverse,invN))
    assert same_lower(derivative(literal),cscale(literal,(N-1)*invN))
    assert same_lower(derivative(literal_inverse),cscale(literal_inverse,(1-N)*invN))
    def coefficient_projector(f):
        out=[zero[:] for _ in range(N)];out[0]=f[0][:]
        return out
    def vacuum_projector(f):
        out=[zero[:] for _ in range(N)];out[0][0]=f[0][0]
        return out
    first_normal=zero[:];first_normal[1]=1
    normal_input=cp(eps[0],first_normal)
    assert coefficient_projector(normal_input)!=vacuum_projector(normal_input)
    assert vacuum_projector(normal_input)==[zero[:] for _ in range(N)]
    assert same_lower(derivative(coefficient_projector(normal_input)),
                      coefficient_projector(derivative(normal_input)))
    left=cadd(derivative(vacuum_projector(normal_input)),
              cscale(vacuum_projector(derivative(normal_input)),-1))
    right=cscale(vacuum_projector(derivative(normal_input)),-1)
    assert left==right and right[0][0]==(-invN)%p
    return {'level':N,'whole_cyclic_carry_idempotents_exact':True,
            'Mellin_Weyl_and_normal_intertwining':True,
            'nonconstant_integer_resonant_characters_retained':True,
            'averaged_cut_preserved':True,'reduced_and_literal_pivot_lifts_retained':True,
            'literal_clock_power_differs_by_U':True,
            'coefficientwise_and_finite_vacuum_projectors_distinct':True,
            'finite_vacuum_normal_cut_row_retained':True}


def relative_checks():
    t,sigma=s.symbols('t sigma');order=7
    trunc=lambda f:s.series(f,t,0,order).removeO().expand()
    backward=trunc(s.exp(-sigma*t));endpoint=trunc(s.exp(-t))
    def L(a,b0,b1):
        return trunc(s.integrate(trunc(backward*a),(sigma,0,1))-endpoint*b1+b0)
    tests=[]
    for f in (1+sigma+t*sigma**2,t*t+sigma**3+t*sigma,1+t+sigma**2*t**3):
        defect=L(s.diff(f,sigma)-t*f,f.subs(sigma,0),f.subs(sigma,1))
        assert defect==0
        # The two coherent differential directions commute exactly.
        first=lambda h:s.diff(h,t)-sigma*h
        second=lambda h:s.diff(h,sigma)-t*h
        assert s.expand(first(second(f))-second(first(f)))==0
        bare=s.expand(s.diff(second(f),t)-second(s.diff(f,t)))
        assert s.expand(bare+f)==0
        tests.append({'relative_coboundary_transgression_zero':True,
                      'normal_sigma_correction_flat':True})
    for coefficient in (1,1+t+t*t):
        assert L(trunc(s.exp(sigma*t))*coefficient,0,0)==trunc(coefficient)
    assert trunc(s.exp(sigma*t)).subs(sigma,1)==trunc(s.exp(t))
    return tests


def obstruction_and_scale_checks():
    U=s.symbols('U');residues=[]
    for degree in (1,2,3,7):
        assert s.residue(degree/U,U,0)==degree
        rational=U**-3+2/U+U/(1-U)
        assert s.residue(s.diff(rational,U),U,0)==0
        residues.append({'finite_cover_degree':degree,'nonzero_logarithmic_residue':degree})
    a,b,N=s.symbols('a b N',nonzero=True);z=a+b
    tau=a*z;A=z*z/(1+z*z)
    density=s.cancel(s.diff(tau,a)*s.diff(A,b)/A-s.diff(tau,b)*s.diff(A,a)/A)
    assert s.cancel(density-2/(1+z*z))==0
    # Physical quantization scale is explicitly distinct from the bare kernel.
    h=2*s.pi*s.I/N;u=N*s.log(A)
    assert s.simplify(tau*s.log(A)/h-tau*u/(2*s.pi*s.I))==0
    return {'finite_cover_residue_obstructions':residues,
            'bare_Darboux_form_exact':True,'physical_two_pi_i_scale_not_suppressed':True}


def main():
    cyclic=[cyclic_case(N) for N in range(2,9)]
    result={'whole_normal_Mellin_cases':cyclic,'strict_relative_chain_cases':relative_checks(),
            'global_obstruction_and_scale':obstruction_and_scale_checks(),
            'scope':'Actual formal/lognormal boundary comparison only; no global geometric period selection.'}
    path=Path(__file__).with_name('fock_cyclic_normal_mellin_map_results.json')
    path.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'whole_normal_levels':len(cyclic),
                      'relative_chain_cases':len(result['strict_relative_chain_cases']),
                      'output':str(path)},indent=2))


if __name__=='__main__':main()
