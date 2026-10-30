#!/usr/bin/env python3
"""Actual inverse turn, ordered transport and selected scalar action.

The tests make no operator-symbol substitution and retain the distinction
between scalar asymptotics and an assembled source contribution.
"""
import json
from pathlib import Path
import sympy as sp
import mpmath as mp


def exact():
    b,z=sp.symbols('b z',nonzero=True);I=sp.eye(2)
    A=-sp.Matrix([[1,1],[0,1]]);B=-sp.Matrix([[1,0],[-4,1]])
    H=B*A+I;C=I+b*H
    Ao=sp.simplify(C*A*C.inv());Bo=sp.simplify(C*B*C.inv())
    T=sp.simplify(B.inv()*Bo);alpha=8*b*b-4*b+1;D=T-alpha*I
    assert sp.simplify(T-A*Ao.inv())==sp.zeros(2)
    assert sp.simplify(D*A-B.inv()*D)==sp.zeros(2)
    assert sp.simplify(D*Ao.inv()-Bo*D)==sp.zeros(2)
    assert sp.factor(D.det())==-64*b**4
    raw=[Ao,Bo,B.inv(),A.inv()]
    total=I;lowers=[];locals=[]
    for G in raw:
        prev=sp.Matrix([[1,0],[-total[1,0],total[0,0]]])
        locals.append(sp.simplify(prev*G*prev.inv()))
        total=sp.simplify(G*total)
        after=sp.Matrix([[1,0],[-total[1,0],total[0,0]]])
        lowers.append(sp.simplify(after*prev.inv()))
    assert total==I
    prefix=I
    for index in [1,2,3,0]:
        actual=sp.simplify(prefix.inv()*locals[index]*prefix)
        expected=sp.simplify(lowers[0]*raw[index]*lowers[0].inv())
        assert sp.simplify(actual-expected)==sp.zeros(2)
        prefix=sp.simplify(lowers[index]*prefix)
    assert prefix==I
    J=-z**-2;bb=-sp.I*(z+z**-1)/4
    ratio=sp.cancel((J-alpha.subs(b,bb))/(1/J-alpha.subs(b,bb)))
    target=(1+sp.I*(z-z**-1)/2)/(1-sp.I*(z-z**-1)/2)
    assert sp.cancel(ratio-target)==0
    atzero=sp.simplify((D/(-2*sp.I)).subs(b,-sp.I/2))
    assert sp.simplify(atzero-I-sp.I*(T.subs(b,-sp.I/2)+I)/2)==sp.zeros(2)
    # exp(-partial_xi Psi) follows from d eta/d xi=-pi i:
    # 2 atan(sinh eta) is represented by the rational Cayley ratio.
    ss=sp.symbols('s',real=True)
    assert sp.simplify((1+sp.I*ss)/(1-sp.I*ss)-(1+sp.I*ss)**2/(1+ss**2))==0
    J,R=sp.symbols('J R',nonzero=True)
    Bt=sp.Matrix([[-2*J/(J+1),1],[-(J-1)**2/(J+1)**2,-2/(J+1)]])
    Tt=sp.diag(J,1/J);Dt=sp.diag(R,1)
    assert sp.factor(Bt.det())==1
    assert sp.factor(sp.trace(Bt))==-2
    assert sp.factor(sp.trace(Bt.inv()*Tt))==-2
    source=sp.trace(Dt*Bt.inv()*Dt.inv()*Bt)
    proposed=2-(J-1)**2/(J+1)**2*(2-R-1/R)
    assert sp.cancel(source-proposed)==0
    zz=J+1/J
    assert sp.cancel((J-1)**2/(J+1)**2-(zz-2)/(zz+2))==0
    return dict(ordered_target_matrix_identities=4,actual_cyclic_prefix_identities=4,
                exact_eigenratio_and_parabolic_limit=2,exact_Cayley_identity=1,
                exact_general_input_character_identities=5)


def polynomial(N,eta,a=None):
    if a is None:a=(N-1)//2
    theta=mp.pi/N;z=-2*mp.cosh(2*eta)
    lam=lambda r:2*mp.cos((2*r+1)*theta)
    term=value=mp.mpf(1);dt=dv=mp.mpf(0)
    for k in range(a):
        coeff=(lam(k)-lam(a))/(2*mp.sin((k+1)*theta))**4
        factor=coeff*(lam(k)-z)
        dt=dt*factor-term*coeff
        term*=factor;value+=term;dv+=dt
    return value,dv


def numeric():
    mp.mp.dps=90
    G=mp.catalan;anchor=4*G/mp.pi;rows=[]
    for eta in [mp.mpf('.25'),mp.mpf('1'),mp.mpf('2')]:
        target=anchor+2/mp.pi*mp.quad(lambda x:mp.atan(mp.sinh(x)),[0,eta])
        mode=mp.atan(mp.cosh(eta))/mp.pi
        integral=mp.quad(lambda x:mp.log(mp.cos(mp.pi*x)**2*(mp.cosh(eta)**2-mp.sin(mp.pi*x)**2)/mp.sin(mp.pi*x)**4),[0,mode])
        assert abs(integral-target)<mp.mpf('1e-85')
        derivative=2/mp.pi*mp.atan(mp.sinh(eta))
        for N in [40,81,160,321]:
            value,dvalue=polynomial(N,eta)
            lograte=mp.log(value)/N
            actual_derivative=-4*mp.sinh(2*eta)*dvalue/(N*value)
            assert abs(lograte-target)<5*mp.log(N)/N
            assert abs(actual_derivative-derivative)<10/N
            rows.append(dict(N=N,eta=str(eta),actual_rate=str(lograte),selected_action=str(target),
                             actual_derivative=str(actual_derivative),selected_derivative=str(derivative)))
    endpoint=[]
    for N in [40,81,160,321]:
        value,dvalue=polynomial(N,mp.mpf(0))
        second=-8*dvalue/(N*value)
        assert abs(second-2/mp.pi)<10/N
        endpoint.append(dict(N=N,actual_second_derivative=str(second),limit=str(2/mp.pi)))
    general=[]
    for alpha0 in [mp.mpf('.2'),mp.mpf('.35')]:
        for eta in [mp.mpf('.4'),mp.mpf('1.5')]:
            for N in [80,161,320]:
                a=int(mp.floor(alpha0*N));alpha=mp.mpf(a)/N
                s=mp.sin(mp.pi*alpha);A=s*s;kappa=mp.cosh(eta)**2
                vstar=mp.asin(mp.sqrt(A*kappa/(A+kappa)))/mp.pi
                direct=2*mp.cosh(eta)*mp.sinh(eta)*mp.quad(
                    lambda v:1/(kappa-mp.sin(mp.pi*v)**2),[0,vstar])
                target=2/mp.pi*mp.asin(s*mp.tanh(eta))
                assert abs(direct-target)<mp.mpf('1e-85')
                value,dvalue=polynomial(N,eta,a)
                actual=-4*mp.sinh(2*eta)*dvalue/(N*value)
                assert abs(actual-target)<10/N
                ratio=mp.exp(2j*mp.asin(s*mp.tanh(eta)))
                zz=-2*mp.cosh(2*eta);input_trace=2*mp.cos(2*mp.pi*alpha)
                assert abs(ratio+1/ratio-(2-(2-input_trace)*(zz+2)/(zz-2)))<mp.mpf('1e-85')
                general.append(dict(N=N,a=a,eta=str(eta),actual_derivative=str(actual),
                                    selected_derivative=str(target)))
    return dict(precision_digits=90,independent_real_action_integrals=3,
                actual_scalar_action_and_first_derivative_cases=len(rows),
                actual_parabolic_second_derivative_cases=len(endpoint),
                general_input_selected_derivative_cases=len(general),
                rows=rows,endpoint=endpoint,general=general)


def main():
    result=dict(status='PASS',exact=exact(),scalar=numeric(),
                scope='Actual inverse-turn ordered transport and canonical scalar generating derivative/anchor. No complex-channel column amplitude, polynomial-operator or whole-source asymptotic.')
    Path(__file__).with_name('actual_matching_edge_polynomial_geometric_action_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({**result,'scalar':{k:v for k,v in result['scalar'].items() if k not in ('rows','endpoint','general')}},indent=2))

if __name__=='__main__':main()
