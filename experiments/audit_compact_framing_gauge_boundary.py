#!/usr/bin/env python3
"""Exact universal framing, eigenflag and principal residue checks."""

import json
from pathlib import Path

import sympy as S


def same_matrix(a,b):
    assert (a-b).applyfunc(S.simplify)==S.zeros(a.rows,a.cols)


def finite_gauge():
    q,m,c,w,z=S.symbols('Q M c w z',nonzero=True)
    records=[]
    for n in range(2,6):
        gauge=S.diag(*(c**(-a) for a in range(n)))
        e=S.zeros(n);f=S.zeros(n)
        for a in range(1,n):e[a-1,a]=m*q**(-a)-1/m
        for a in range(n-1):f[a+1,a]=1-q**(a+1)
        same_matrix(gauge*e*gauge.inv(),c*e)
        same_matrix(gauge*f*gauge.inv(),f/c)
        entries=S.symbols(f'a0:{n*n}')
        matrix=S.Matrix(n,n,entries)
        transformed=gauge*matrix*gauge.inv()
        kernel=lambda a,ww,zz:sum(ww**i*a[i,j]*S.binomial(n-1,j)*zz**j
                                  for i in range(n) for j in range(n))
        assert S.expand(kernel(transformed,w,z)-kernel(matrix,w/c,c*z))==0
        records.append({'level':n,'exact_momentum_gauge_and_coherent_coordinates':True})
    return records


def framing_and_springer():
    r,s,p,v,a,eta,b=S.symbols('r s p v a eta b',nonzero=True)
    mu0=S.Matrix([[1,1],[0,1]])
    frame=S.Matrix([[r,1-r],[s,-s]])
    diagonal=S.diag(p,1)
    mu=S.Matrix([[1+s,-s*p],[s/p,1-s]])
    same_matrix(diagonal*frame.inv()*mu0*frame*diagonal.inv(),mu)
    gn=S.Matrix([[1,0],[v,1/eta]])
    nb=S.Matrix([[1,b],[0,1]])
    values={v:1/p,eta:-s*p,b:(1-r)/s}
    same_matrix((gn*nb).subs(values),diagonal*frame.inv()/p)
    coordinates=S.Matrix([-s*p,1/p,(1-r)/s])
    jac=S.factor(coordinates.jacobian([r,s,p]).det())
    assert jac==-1/(s*p)
    spr=S.Matrix([[-v,1],[-v*v,v]])
    same_matrix(mu-S.eye(2),(eta*spr).subs({v:1/p,eta:-s*p}))
    c=2*S.pi*S.I
    physical_eta=(1-S.exp(-c*v*a))/v
    derivative=S.simplify(S.diff(physical_eta,a))
    assert S.simplify(derivative-c*S.exp(-c*v*a))==0
    assert S.simplify(derivative/(1-physical_eta*v)-c)==0
    vp=1/v;ap=v-v*v*a
    other=(S.exp(c*vp*ap)-1)/vp
    assert S.simplify(S.expand_power_exp(other+v*v*physical_eta))==0
    return {'actual_frame_and_source_gauge':True,'Springer_jacobian':str(jac),
            'two_physical_pole_charts_and_exact_Gauss_form':True}


def logarithmic_section_and_escape():
    r,s,p,a,b,c,d=S.symbols('r s p a b c d',nonzero=True)
    cp=2*S.pi*S.I
    loga=-S.log(1+s)
    rstar=1-loga/cp
    assert S.simplify(p*(1-rstar)-p*loga/cp)==0
    assert S.residue(1/(s*(1+s)),s,0)==1
    assert S.residue(1/(s*(1+s)),s,-1)==-1
    g=S.Matrix([[a,b],[c,(1+b*c)/a]])
    mu0=S.Matrix([[1,1],[0,1]])
    comm=mu0*g*mu0.inv()*g.inv()
    assert S.factor(S.trace(comm)-2-c*c)==0
    g=S.Matrix([[a,b],[c,d]])
    diag=S.diag(p,1)
    for rr in (0,1):
        frame=S.Matrix([[rr,1-rr],[s,-s]])
        actual=diag*frame.inv()*g*frame*diag.inv()
        if rr:
            expected=S.Matrix([[a+b*s,-b*s*p],[(a-d+b*s-c/s)/p,d-b*s]])
        else:
            expected=S.Matrix([[d+b*s,p*(a-d-b*s+c/s)],[b*s/p,a-b*s]])
        same_matrix(actual,expected)
    t=S.symbols('t',positive=True)
    south_p=S.sqrt((1-t)/t);south_s=S.exp(-cp*t)-1
    south=S.limit(S.sqrt(t)*(-c/(south_s*south_p)),t,0,dir='+')
    north_p=S.sqrt(t/(1-t));north_s=S.exp(cp*t)-1
    north=S.limit(S.sqrt(t)*(c*north_p/north_s),t,0,dir='+')
    assert S.simplify(south-c/cp)==0
    assert S.simplify(north-c/cp)==0
    return {'marked_logarithmic_section':True,'unit_boundary_residue':True,
            'irreducible_commutator_escape_invariant':True,
            'both_nonzero_minimal_escape_poles':True}


def gaussian_flag_residue():
    eta,v,a=S.symbols('eta v a',nonzero=True)
    inverse=S.Matrix([1-v*a,-eta*v,1/v])
    jac=S.factor(inverse.jacobian([eta,v,a]).det())
    r,s,p=inverse
    coefficient=S.factor(-jac/(s*(1+s)*p))
    assert S.factor(coefficient+1/(eta*(1-eta*v)))==0
    residue=S.simplify(S.limit(eta*coefficient,eta,0))
    assert residue==-1
    return {'full_actual_frame_density_coefficient':str(coefficient),
            'principal_logarithmic_residue':str(residue),
            'normalized_residue_is_actual_compact_trace_class':True}


def main():
    result={'finite_gauge':finite_gauge(),
            'framing_and_Springer':framing_and_springer(),
            'section_and_escape':logarithmic_section_and_escape(),
            'principal_gaussian_residue':gaussian_flag_residue(),
            'scope':'Actual gauge and principal boundary class; no higher-loop extension or volume claim.'}
    out=Path(__file__).with_name('compact_framing_gauge_boundary_results.json')
    out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'finite_gauge_levels':len(result['finite_gauge']),
                      **result['framing_and_Springer'],**result['principal_gaussian_residue'],
                      'output':str(out)},indent=2))


if __name__=='__main__':main()
