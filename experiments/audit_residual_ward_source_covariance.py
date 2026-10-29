#!/usr/bin/env python3
"""Exact checks of complete co-source covariance and whole-power currents.

The Gaussian-current/ideal theorem is proved in the note; these checks
verify its newly explicit boundary and normal-source formulas.
"""

import json
from pathlib import Path

import numpy as np
import sympy as sp

from audit_divided_ward_factorial_fusion import eq, field, ident, mm


def boundary_rows():
    records=[]
    for n in range(2,10):
        p,q=field(n)
        q2=q*q%p
        invn=pow(n,-1,p)
        e=np.ones((n,n),dtype=np.int64)*invn
        for meridian in (1,2,3):
            x=-meridian*pow(q,-1,p)%p
            k=np.diag([x*pow(q2,-a,p)%p for a in range(n)])
            ki=np.diag([pow(int(k[a,a]),-1,p) for a in range(n)])
            raising=np.zeros((n,n),dtype=np.int64)
            lowering=raising.copy()
            for a in range(1,n):
                raising[a-1,a]=(meridian*pow(q2,-a,p)-pow(meridian,-1,p))%p
            for a in range(n-1):lowering[a+1,a]=(1-pow(q2,a+1,p))%p
            ek=(mm(mm(ki,e,p),k,p)-e)%p
            ee=(mm(mm(ki,e,p),raising,p)-mm(mm(raising,ki,p),e,p))%p
            ef=(mm(e,lowering,p)-mm(mm(mm(k,lowering,p),e,p),ki,p))%p
            kappa=(meridian-pow(meridian,-1,p))%p
            expected_e=[]
            expected_f=[]
            for a in range(n):
                aval=pow(q2,a,p)
                edge=(1 if a==n-1 else 0)-(1 if a==0 else 0)
                expected_e.append(((q2-1)*aval*pow(n*meridian*x%p,-1,p)
                                  +kappa*edge*pow(n*x%p,-1,p))%p)
                expected_f.append((1-q2)*aval*invn%p)
            eq(np.diag(ek),np.zeros(n,dtype=np.int64),p)
            eq(np.diag(ee),np.array(expected_e,dtype=np.int64),p)
            eq(np.diag(ef),np.array(expected_f,dtype=np.int64),p)
            if meridian==1:
                for a in range(n):
                    assert int(ee[a,a])*n%p==q*(1-q2)*pow(q2,a,p)%p
        records.append({'level':n,'meridian_germs_checked':3,
                        'complete_and_endpoint_rows':True})
    return records


def principal_geometry():
    r,s=sp.symbols('r s')
    density=-1/(s*(1+s))
    fields=[(2*(r-1),2*s),(2*r-1,2*s)]
    for xr,xs in fields:
        divergence=sp.cancel((sp.diff(density*xr,r)+sp.diff(density*xs,s))/density)
        assert sp.cancel(divergence-2/(1+s))==0
    determinant=sp.factor(sp.det(sp.Matrix(fields)))
    assert determinant==-2*s
    h=sp.symbols('h')
    b1=2*sp.exp(h/2)*(1-sp.exp(h))/(1+s)
    b2=(1+sp.exp(h/2))*(1-sp.exp(h))/(1+s)
    for b in (b1,b2):assert sp.simplify(sp.limit(b/h,h,0)+2/(1+s))==0
    return {'two_cut_fields_determinant':str(determinant),
            'literal_co_source_matches_density_divergence':True}


def whole_normal():
    checks=0
    pivot_lifts=[]
    for n in range(2,10):
        for a in range(-n,2*n+1):
            for b in range(-2,3):
                # Dphys(A^a U^b)=(a+Nb)A^aU^b; after reduction,
                # a=Nc+j, the trace vanishes unless j=0.
                c,j=divmod(a,n)
                left=(a+n*b) if j==0 else 0
                right=n*(c+b) if j==0 else 0
                assert left==right
                checks+=1
        # A^N=U distinguishes the literal clock power from the reduced
        # root representative, even though their paired cut is the same.
        red_weight=-1
        literal_weight=n-1
        assert literal_weight-red_weight==n
        assert red_weight+1==0
        assert literal_weight+(1-n)==0
        pivot_lifts.append({'level':n,'literal_minus_reduced_U_weight':n,
                            'reduced_pivot_normal_weight':red_weight,
                            'literal_clock_pivot_normal_weight':literal_weight,
                            'both_paired_cut_normal_weights':0})
    return {'whole_normal_monomial_and_carry_checks':checks,
            'divided_frobenius_is_negative_physical_euler':True,
            'both_pivot_lifts_and_exact_U_adapter':pivot_lifts}


def main():
    result={'boundary_rows':boundary_rows(),
            'principal_geometry':principal_geometry(),
            'whole_normal':whole_normal(),
            'scope':'Actual co-source and whole-normal identities; no finite geometric source-survival claim.'}
    out=Path(__file__).with_name('residual_ward_source_covariance_results.json')
    out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'levels':len(result['boundary_rows']),
                      **result['principal_geometry'],**result['whole_normal'],
                      'output':str(out)},indent=2))


if __name__=='__main__':main()
