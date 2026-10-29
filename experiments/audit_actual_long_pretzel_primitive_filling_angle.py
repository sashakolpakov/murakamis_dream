#!/usr/bin/env python3
"""Primitive-angle calibration, signed cores and small geometric log lifts."""

import json
from pathlib import Path

import mpmath as mp
import sympy as sp


def symbolic_calibration():
    a,b,p,m=sp.symbols('a b p m',real=True,nonzero=True)
    tau=a+sp.I*b
    U=-2*sp.pi*sp.I*m/(1+p*tau)
    V=tau*U
    core=sp.simplify(sp.re(V))
    expected=2*sp.pi*m*b/((1+p*a)**2+p*p*b*b)
    assert sp.factor(core-expected)==0
    assert sp.simplify(U+p*V+2*sp.pi*sp.I*m)==0
    assert sp.simplify(sp.im(sp.conjugate(U)*V)-2*sp.pi*m*core)==0
    u,v=U/2,sp.pi*sp.I+V/2
    assert sp.simplify(u+p*v-sp.pi*sp.I*(p-m))==0
    assert sp.simplify(2*u+p*(2*v-2*sp.pi*sp.I)+2*sp.pi*sp.I*m)==0
    return {'exact_signed_core_length':True,'positive_log_lattice_orientation':True,
            'projective_angle_is_twice_centered_eigenlog':True,
            'uncentered_SL_spin_is_not_cone_angle':True}


def core_case(s,p,m):
    mp.mp.dps=90
    c=mp.cos(mp.pi/s)
    tau=2j*c/(1+1j*c)
    ustar=mp.atan(1/c)
    assert abs(tau-(1+mp.exp(2j*ustar)))<mp.mpf('1e-80')
    U=-2j*mp.pi*m/(1+p*tau)
    V=tau*U
    predicted=2*mp.pi*m*mp.im(tau)/abs(1+p*tau)**2
    assert abs(mp.re(V)-predicted)<mp.mpf('1e-75')
    assert mp.sign(mp.re(V))==mp.sign(m)
    assert mp.im(mp.conj(U)*V)>0
    assert abs(mp.im(mp.conj(U)*V)-2*mp.pi*m*mp.re(V))<mp.mpf('1e-70')
    # Literal preferred SL longitude retains its central minus.
    M,longitude=mp.exp(U/2),-mp.exp(V/2)
    assert abs(M*longitude**p-(-1)**(p+m))<mp.mpf('1e-65')
    angle=mp.im(U+p*V)
    assert abs(angle+2*mp.pi*m)<mp.mpf('1e-75')
    if abs(m)==1:
        assert abs((-m)*angle-2*mp.pi)<mp.mpf('1e-75')
        assert m*mp.re(V)>0 and (-m)*m==-1
    return {'odd_boxes':s,'signed_slope':p,'charge':m,
            'core_length':float(abs(mp.re(V))),'unwrapped_angle':float(angle),
            'smooth_primitive_angle':abs(m)==1,
            'unit_charge_oriented_tube_attachment':abs(m)==1,
            'positive_oriented_lattice':True}


def affine_increment_case(s,p,m):
    mp.mp.dps=100
    c=mp.cos(mp.pi/s)
    tau=2j*c/(1+1j*c)
    U=-2j*mp.pi*m/(1+p*tau)
    V=tau*U
    A=(1+1j*c)*(1+mp.mpf('.05')*U+mp.mpf('.03')*V)
    k=A/(-mp.expm1(U))
    B=k*(-mp.expm1(V))
    start=mp.mpc('-.6','.2')
    for log,mult,translation in ((U,mp.exp(U),A),(V,mp.exp(V),B)):
        end=mult*start+translation
        path=[start,start+(end-start)/3+mp.mpc('.1','.07'),
              start+2*(end-start)/3-mp.mpc('.05','.08'),end]
        increments=[]
        length=0
        for w0,w1 in zip(path[:-1],path[1:]):
            ratio=(w1-w0)/(w0-k)
            assert abs(ratio)<mp.mpf('.25')
            increments.append(mp.log1p(ratio))
            length+=abs(w1-w0)
        actual=mp.fsum(increments)
        R=max(abs(z) for z in path)
        assert abs(k)>2*R
        assert abs(actual)<=length/(abs(k)-R)*(1+mp.mpf('1e-80'))
        assert abs(actual-log)<mp.mpf('1e-80')
        assert abs(actual-(log+2j*mp.pi))>6
    return {'odd_boxes':s,'signed_slope':p,'charge':m,
            'finite_affine_fixed_point_modulus':float(abs(k)),
            'both_primitive_geometric_logs_match_small_source_logs':True,
            'extra_full_turn_excluded':True}


def fermi_case(r):
    mp.mp.dps=80
    r,t,theta=mp.mpf(r),mp.mpf('.3'),mp.mpf('1.2')
    def coordinates(rr,ang,tt):
        return mp.matrix([mp.exp(tt)*mp.tanh(rr)*mp.cos(ang),
                          mp.exp(tt)*mp.tanh(rr)*mp.sin(ang),
                          mp.exp(tt)/mp.cosh(rr)])
    vec=coordinates(r,theta,t)
    J=mp.matrix(3,3)
    for col in range(3):
        def one(value):
            args=[r,theta,t]
            args[col]=value
            return coordinates(*args)
        deriv=mp.diff(one,[r,theta,t][col])
        for row in range(3):
            J[row,col]=deriv[row]
    metric=J.T*J/vec[2]**2
    expected=mp.diag([1,mp.sinh(r)**2,mp.cosh(r)**2])
    assert mp.norm(metric-expected)<mp.mpf('1e-65')
    assert mp.det(J)>0
    assert abs(mp.det(J)/vec[2]**3-mp.sinh(r)*mp.cosh(r))<mp.mpf('1e-65')
    return {'radius':float(r),'exact_cylindrical_hyperbolic_metric':True,
            'ambient_orientation_positive':True,
            'unit_charge_normal_circumference':float(2*mp.pi*mp.sinh(r)),
            'double_charge_normal_circumference':float(4*mp.pi*mp.sinh(r))}


if __name__=='__main__':
    symbolic=symbolic_calibration()
    cores=[core_case(s,p,m) for s in (3,5,7,25,51)
           for p in (-1000000,-101,-7,7,101,1000000) for m in (-2,-1,1,2)]
    increments=[affine_increment_case(s,p,m) for s in (3,5,25,51)
                for p in (-1000000,-101,101,1000000) for m in (-1,1)]
    metrics=[fermi_case(r) for r in ('.0001','.03','.2','.7','1.2')]
    result={'status':'PASS','exact_symbolic_spin_and_angle':symbolic,
            'signed_independent_core_and_angle_families':cores,
            'geometric_small_log_increment_checks':increments,
            'hyperbolic_tube_metric_calibration':metrics,
            'scope':'Peripheral primitive-angle theorem; positive core deformation and whole tube completion are separate geometric inputs.'}
    Path(__file__).with_name('actual_long_pretzel_primitive_filling_angle_results.json').write_text(
        json.dumps(result,indent=2)+'\n')
    print(f'PASS exact spin/angle algebra; {len(cores)} signed core families; {len(increments)} small-log calibrations; {len(metrics)} tube metrics')
