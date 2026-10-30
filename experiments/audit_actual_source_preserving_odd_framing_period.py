#!/usr/bin/env python3
"""Original odd-band source, genuine normal scope, and physical residue audit."""
import argparse
import json
from pathlib import Path
import mpmath as mp
import sympy as sp
import numpy as np
from audit_actual_braided_residual_framing_current import fixture, rectangular_fixture
from audit_actual_explicit_root_channel_normal_adapter import source_channel, root_diagonal
from audit_actual_nc_morse_graph_first_normal_source_reduction import const
from audit_actual_braided_two_cut_source_adapter import eq


def original_source_checks():
    count=entries=bands=first_normals=eigenjets=defects=0
    rows=[]
    for N in (2,3,4):
     for width,kind in [(2,'braid'),(2,'complete'),(3,'braid')]+([(1,'rectangular')] if N<=3 else []):
      orig=rectangular_fixture(N) if kind=='rectangular' else fixture(N,width,kind)
      for routed in (False,True):
       field,q,g,A,B,U,Ui,b,c=orig
       if not routed:U=Ui=const(np.eye(N**c,dtype=np.int64))
       C=source_channel((field,q,g,A,B,U,Ui,b,c))
       I=np.eye(N,dtype=np.int64);Tp=np.diag(np.ones(N-1,dtype=np.int64),-1);Tm=Tp.T
       t=2*pow(3,-1,field)%field
       beta=np.array([int(sp.binomial(N-1,a))*pow(t,a,field)*pow(1-t,N-1-a,field)%field for a in range(N)],dtype=np.int64)
       e=np.outer(beta,np.ones(N,dtype=np.int64))
       O=(Tp-q*Tm)%field;O1=(-q*Tm)%field
       kappa=int(np.trace(e@O)%field)
       assert kappa!=0
       formula=(1-q-pow(t,N-1,field)+q*pow(1-t,N-1,field))%field
       assert kappa==formula
       whole=C(const(I));z=tuple(int(x[0,0]) for x in whole)
       CO=C((O,O1))
       assert np.array_equal(CO[0],z[0]*O%field);entries+=N*N
       literal=0
       for a in range(N-1):
        for l in range(N-1):
         E=np.zeros_like(I);E[l+1,l]=1
         literal+=int(beta[a])*int(C(const(E))[0][a+1,a]);bands+=1
       for a in range(1,N):
        for l in range(1,N):
         E=np.zeros_like(I);E[l-1,l]=1
         literal-=q*int(beta[a])*int(C(const(E))[0][a-1,a]);bands+=1
       assert literal%field==kappa*z[0]%field
       actual_pair=int(np.trace(e@CO[0])%field)
       nu=int(np.sum(g[1])%field); assert int(np.sum(g[0])%field)==0
       assert nu*actual_pair*pow(kappa,-1,field)%field==nu*z[0]%field;first_normals+=1
       H=root_diagonal(N,q,field);Oh1=(O1+O@H)%field
       E=np.zeros_like(I);E[0,N-1]=1
       CE=C(const(E));lam=tuple(int(x[0,N-1]) for x in CE)
       Ch=C((O,Oh1));assert eq(Ch,(lam[0]*O%field,(lam[1]*O+lam[0]*Oh1)%field));eigenjets+=2*N*N
       defect=int(np.trace(e@(CO[1]-z[1]*O-z[0]*O1))%field)
       defects+=int(defect!=0);count+=1
       rows.append(dict(N=N,width_in=c,width_out=b,kind=kind,routed=routed,kappa=kappa,root_scalar=z[0],normal_defect=defect))
    return dict(actual_sources=count, root_odd_entries=entries,
                literal_bands=bands, whole_first_normals=first_normals,
                generic_eigenkernel_jet_entries=eigenjets,
                nonzero_literal_normal_defects=defects, rows=rows)


def exact_geometry():
    r,s,b,c,q,R=sp.symbols('r s b c q R', nonzero=True)
    F=sp.Matrix([[r,1-r],[s,-s]])
    mu=sp.eye(2)+c*sp.Matrix([[b,-b*b],[1,-b]])
    RR=r-s*b; p=(RR-1)/RR; k=1+c/s*RR*(1-RR)
    physical=sp.Matrix([[k,(1-k)*p],[(k-1)/p,2-k]])
    assert all(sp.cancel(x)==0 for x in F.inv()*mu*F-physical)
    odd=R/(R-1)-q*(R-1)/R
    decomposition=(1+q)/2*(R/(R-1)-(R-1)/R)+(1-q)/2*(R/(R-1)+(R-1)/R)
    assert sp.cancel(odd-decomposition)==0
    assert sp.cancel(odd-((1-q)+1/(R-1)+q/R))==0
    prim=(1-q)*r+sp.log(RR-1)+q*sp.log(RR)
    assert sp.cancel(sp.diff(prim,r)-odd.subs(R,RR))==0
    assert sp.residue(odd,R,1)==1
    assert sp.residue(odd,R,0)==q
    w=sp.symbols('w',nonzero=True)
    assert sp.residue(-odd.subs(R,1/w)/w**2,w,0)==-1-q
    # ds wedge dr coefficients, keeping the actual orientation.
    s2=c/s*RR*(1-RR)
    lhs=odd.subs({q:1,R:RR})/(s*(1+s))
    rhs=sp.diff(s2,r)/(s*(1+s)*s2)
    assert sp.cancel(lhs-rhs)==0
    y=sp.symbols('s2',nonzero=True)
    assert sp.residue(sp.residue(1/((1+s)*s*y),y,0),s,0)==1
    # The resonant limit is a check of the rational form, not a quantum packet.
    h,rho=sp.symbols('h rho',nonzero=True)
    inner=odd.subs({R:rho/h-s*b,q:sp.exp(sp.pi*sp.I*h)})
    assert sp.simplify(sp.limit(inner/h,h,0)-(2/rho-sp.pi*sp.I))==0
    assert sp.simplify(sp.limit(inner/(1-sp.exp(sp.pi*sp.I*h)),h,0)-(1+2*sp.I/(sp.pi*rho)))==0
    assert sp.cancel(R/(1-R)+(1/R)/(1-1/R)+1)==0
    # The all-N modulus identity is algebraic in its real endpoint weights.
    a0,b0,cc,ss=sp.symbols('a0 b0 cc ss',real=True)
    square=(a0-b0*cc)**2+(b0*ss)**2
    formula=(a0-b0)**2*(1+cc)/2+(a0+b0)**2*(1-cc)/2
    assert sp.rem(sp.expand(square-formula),sp.Poly(cc**2+ss**2-1,ss),ss)==0
    return dict(physical_gauss_entries=4, exact_odd_and_primitive_identities=3,
                exact_one_form_residues=3, oriented_doublelog_identities=2,
                classical_resonant_limits=2, exact_modulus_identity=1, inverse_clock_residue_identity=1)


def numerical_normalization():
    mp.mp.dps=80
    checks=residue_checks=symmetric_checks=0; minimum=mp.inf; maximum_error=mp.mpf('0'); residue_error=mp.mpf('0')
    for N in range(2,65):
        q=mp.e**(mp.pi*1j/N)
        for t in (mp.mpf('0'),mp.mpf(1)/3,mp.mpf(1)/2,mp.mpf(2)/3,mp.mpf('1')):
            a=1-t**(N-1);b=1-(1-t)**(N-1);kap=a-q*b
            bound=mp.sin(mp.pi/(2*N))
            assert abs(kap)>=bound*(1-mp.mpf('1e-75'))
            square=(a-b)**2*mp.cos(mp.pi/(2*N))**2+(a+b)**2*mp.sin(mp.pi/(2*N))**2
            maximum_error=max(maximum_error,abs(abs(kap)**2-square))
            minimum=min(minimum,N*abs(kap));checks+=1
            beta=[mp.binomial(N-1,j)*t**j*(1-t)**(N-1-j) for j in range(N)]
            G=sum(beta[j]/((q*q**(2*j))**-1-1) for j in range(N))
            err=abs(mp.re(G)+mp.mpf('0.5')); residue_error=max(residue_error,err)
            assert err<mp.mpf('1e-75')
            sample=-(1+q)*G/kap
            direct=sum(N*beta[j]/kap*(-(1+q))/((q*q**(2*j))**-1-1) for j in range(N))/N
            assert abs(sample-direct)<mp.mpf('1e-72')
            assert abs(sample)>0;residue_checks+=1
            if t==mp.mpf('0.5'):
                assert abs(G+mp.mpf('0.5'))<mp.mpf('1e-75');symmetric_checks+=1
    return dict(both_parity_normalization_checks=checks,
                specified_coherent_residue_samples=residue_checks,
                exact_symmetric_sample_checks=symmetric_checks,
                max_sample_realpart_error=mp.nstr(residue_error,8),
                minimum_N_times_modulus=mp.nstr(minimum,22),
                max_modulus_identity_error=mp.nstr(maximum_error,8),digits=80)


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,default=Path(__file__).with_name('actual_source_preserving_odd_framing_period_results.json'))
    args=parser.parse_args()
    result=dict(status='PASS',source=original_source_checks(),geometry=exact_geometry(),
                normalization=numerical_normalization(),
                scope='Exact original root odd source and first-trace normal; local physical leading-form residues. No global winding, mixed-color packet, or uniform quantum resonant limit inferred.')
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='source'},indent=2))
    print(json.dumps({k:v for k,v in result['source'].items() if k!='rows'},indent=2))

if __name__=='__main__':
    main()
