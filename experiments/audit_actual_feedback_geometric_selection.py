#!/usr/bin/env python3
"""Exact finite-source Gaussian stabilization and its Hessian/radical."""
import itertools
import json
from pathlib import Path
import sympy as sp

from audit_actual_hardy_cauchy_network import HardyNetwork
from audit_actual_global_charged_bridge_flow import setup
from audit_actual_clock_feedback_normal_form import feedback_metadata,case


def actual_gaussian_cases():
    rows=[]
    words=([1,-2,1,-2],[1,1,1,2,-1,2],[-1,2,-1])
    for N in range(2,10):
        H=HardyNetwork(N,1);p,Q=H.p,H.Q
        g=sum(pow(Q,-u*v,p) for u in range(N) for v in range(N))*pow(N,-1,p)%p
        assert g==1
        for word in words:
            S=setup(H,3,word);_,meta=feedback_metadata(S)
            R=list(meta.values());m=len(word)
            T=[[r['T'].get(j,0) for j in range(m)] for r in R]
            for seed in range(13):
                nu=[(-1)**i*(seed+2*i+1) for i in range(len(R))]
                hh=[(seed+3*j)%N for j in range(m)]
                uu=[(2*seed+j)%N for j in range(m)]
                vv=[(3*seed+2*j)%N for j in range(m)]
                tt=[sum(nu[i]*T[i][j] for i in range(len(R))) for j in range(m)]
                eta=[h+u for h,u in zip(hh,uu)]
                lam=[t+v for t,v in zip(tt,vv)]
                before=-sum(l*e for l,e in zip(lam,eta))+sum(l*h for l,h in zip(lam,hh))
                before+=sum(tt[j]*eta[j] for j in range(m))
                after=sum(tt[j]*hh[j]-vv[j]*uu[j] for j in range(m))
                assert before==after
                assert pow(Q,before,p)==pow(Q,after,p)
                assert pow(g,m,p)==1
            rows.append({'N':N,'word':word,'actual_feedback_rows':len(R),
                         'exact_momentum_shear_cases':13,'normalized_gaussian':g})
    return rows


def nonlinear_hessian_check():
    # Two nonconstant framing variables, two transverse variables, m=2.
    x=sp.symbols('r s z w');u=sp.symbols('u0:2');v=sp.symbols('v0:2')
    eta=sp.symbols('e0:2');lam=sp.symbols('l0:2');alpha=sp.Integer(3)
    r,s,z,w=x;T=sp.Matrix([[0,1],[-1,-1]])
    nu=sp.Matrix([r+z*z,s*w+z]);hh=sp.Matrix([r*z+w,s+w*w])
    act=2*z*z+z*w+3*w*w+z**3
    bare=act-alpha*(nu.T*T*hh)[0]
    ext=bare+alpha*((sp.Matrix(lam).T*(hh-sp.Matrix(eta)))[0]
                    +(nu.T*T*sp.Matrix(eta))[0])
    sub=dict(zip(eta,hh+sp.Matrix(u)))|dict(zip(lam,T.T*nu+sp.Matrix(v)))
    developed=sp.expand(ext.subs(sub,simultaneous=True))
    assert sp.expand(developed-act+alpha*(sp.Matrix(v).T*sp.Matrix(u))[0])==0
    old=list(x)+list(eta)+list(lam);new=list(x)+list(u)+list(v)
    coord=list(x)+list(hh+sp.Matrix(u))+list(T.T*nu+sp.Matrix(v))
    J=sp.Matrix(coord).jacobian(new)
    assert sp.expand(J.det())==1
    origin=dict.fromkeys(new,0);old_origin=dict.fromkeys(old,0)
    Hext=sp.hessian(ext,old).subs(old_origin);J0=J.subs(origin)
    Hact=sp.hessian(act,x).subs(dict.fromkeys(x,0))
    D=sp.zeros(4)
    for j in range(2):D[j,j+2]=D[j+2,j]=-alpha
    target=sp.diag(Hact,D)
    assert J0.T*Hext*J0==target
    assert Hext.rank()==6 and len(Hext.nullspace())==2
    lifted=[]
    for j in range(2):
        unit=sp.zeros(8,1);unit[j]=1
        k=J0*unit;assert Hext*k==sp.zeros(8,1);lifted.append([int(a) for a in k])
    assert D.det()==(-1)**2*alpha**4
    # A genuine transverse slice has no frame coordinates.
    inds=[2,3,4,5,6,7]
    assert target.extract(inds,inds).det()==D.det()*Hact.extract([2,3],[2,3]).det()
    return {'exact_nonlinear_phase_split':True,'full_coordinate_Jacobian':1,
            'extended_Hessian_rank':6,'framing_radical_dimension':2,
            'normalized_hyperbolic_determinant':int(D.det()),
            'lifted_original_framing_vectors':lifted}


def main():
    original=[case(N,3,word) for N,word in
              ((2,[1,-2,1,-2]),(3,[1,-2,1,-2]),(2,[1,1,1,2,-1,2]))]
    # Multiplication by the exact split auxiliary Gaussian changes no
    # coefficient, so the very same original full pivotal source is retained.
    for row in original:
        assert row['feedback_original_scalar']==row['original_matrix_scalar']
        row.pop('metadata',None)
    out={'actual_diagram_Gaussian_stabilizations':actual_gaussian_cases(),
         'original_whole_sources_unchanged':original,
         'nonlinear_Jacobian_and_Hessian':nonlinear_hessian_check(),
         'scope':'exact normalization and preservation of the unresolved original source; '
                 'no selected geometric coefficient or volume bound'}
    Path(__file__).with_name('audit_actual_feedback_geometric_selection_results.json').write_text(
        json.dumps(out,indent=2)+'\n')
    print('PASS 24 actual feedback diagrams / 312 exact shears, three ORIGINAL sources, '
          'nonlinear Jacobian-one split, Hessian determinant and two framing directions')


if __name__=='__main__':main()
