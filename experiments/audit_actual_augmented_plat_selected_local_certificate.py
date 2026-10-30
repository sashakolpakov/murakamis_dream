#!/usr/bin/env python3
"""Original-head endpoint sheet identities, with both actual adapters.

The algebraic checks do not assert whole-plat certificate existence or a
contributing original summation cycle.
"""
from __future__ import annotations

import cmath
import json
import math
import random
from pathlib import Path

import sympy as sp


def main():
    z,w,b=sp.symbols('z w b')
    I=sp.eye(2)
    A=-sp.Matrix([[1,1],[0,1]])
    B=-sp.Matrix([[1,0],[-4,1]])
    P=B*A
    H=P+I
    g=sp.Matrix([[1,-w],[1,-z]])
    Ag=sp.simplify(g*A*g.inv())
    Bg=sp.simplify(g*B*g.inv())
    Pg=sp.simplify(g*P*g.inv())
    bm=sp.Matrix([[1,0],[-Ag[1,0],Ag[0,0]]])
    G2=sp.simplify(bm*Bg*bm.inv())
    S1=sp.factor(Ag[1,0]/(Ag[0,0]+1))
    S2=sp.factor(G2[1,0]/(G2[0,0]+1))
    Up=sp.factor(-1/Ag[0,0])
    Tp=sp.factor(1/Pg[0,0])
    y=sp.factor(S1/S2)
    assert sp.factor(Up-(z-w)/(z-w+1)) == 0
    assert sp.factor(Tp-(z-w)/(4*w*z+3*w+z+1)) == 0
    assert sp.factor(y+w/(z+1)) == 0
    expected={
        ('low','input'):(2*w+1)/(2*w-1),
        ('low','output'):(2*z+1)/(2*z+3),
        ('high','input'):-(2*z+1)/(2*z+3),
        ('high','output'):-(2*w+1)/(2*w-1),
    }
    for adapter in ('low','high'):
        U,T=(Up,Tp) if adapter=='low' else (Up/Tp,1/Tp)
        for side,yy in [('input',y),('output',1/y)]:
            root=-U*(yy*(T-U)+(1-U))/(-yy*(T-U)+T*(1-U))
            assert sp.factor(root-expected[adapter,side]) == 0
    # The two local pairs over the same physical magnetic parameters.
    involution={z:-w-1,w:-z-1}
    assert sp.factor(Up.subs(involution,simultaneous=True)-Up)==0
    assert sp.factor(Tp.subs(involution,simultaneous=True)-Tp)==0
    assert sp.factor(y.subs(involution,simultaneous=True)-1/y)==0

    C=I+b*H
    Cz=sp.factor((C[0,0]*z+C[0,1])/(C[1,0]*z+C[1,1]))
    assert sp.factor(1/(2*Cz+1)-(1/(2*z+1)-2*b))==0
    p,q=sp.symbols('p q')
    eta_sub={z:(1/p-1)/2,w:(1/q-1)/2}
    assert sp.factor(Tp.subs(eta_sub,simultaneous=True)+(p-q)/(p-q+2))==0

    # Both algebraic selected-root reconstruction signs are retained.
    zz,cc,rr=sp.symbols('zeta c r')
    W=1+2*cc*zz
    V=W+zz**2
    Y=(zz+sp.I*rr)**2/V
    recover=(V*Y-zz**2+W)/(2*sp.I*zz)
    assert sp.rem(sp.together(recover-rr).as_numer_denom()[0],rr**2-W,rr)==0
    yy=sp.symbols('Y')
    rgeo=(V*yy-zz**2+W)/(2*sp.I*zz)
    # Characteristic in these centered variables has roots Y and 1/Y.
    char=V*yy**2-2*(zz**2-W)*yy+V
    assert sp.factor((rgeo**2-W)/char+V/(4*zz**2))==0

    # Finite regressions compare the algebraic source selector against the
    # oriented disk side, for both physical degree adapters and both factors.
    rng=random.Random(301020267)
    checks={f'{a}_{s}':0 for a in ('low','high') for s in ('input','output')}
    central_frames=0
    for _ in range(50000):
        zv=complex(rng.uniform(-3,3),rng.uniform(-3,3))
        wv=complex(rng.uniform(-3,3),rng.uniform(-3,3))
        if abs(zv-wv)<1e-5 or abs(zv+1)<1e-5 or abs(wv)<1e-5:
            continue
        Uv=(zv-wv)/(zv-wv+1)
        Tv=(zv-wv)/(4*wv*zv+3*wv+zv+1)
        l1=math.log(abs(Uv))+1j*(cmath.phase(Uv)%(2*math.pi))
        X2=Tv/Uv
        l2=math.log(abs(X2))+1j*(cmath.phase(X2)%(2*math.pi))
        x1=l1/(2j*math.pi)
        x2=l2/(2j*math.pi)
        degree=x1+x2
        if abs(x1.real-.5)+abs(x2.real-.5)>=.4999 or abs(degree.real-1)<1e-4:
            continue
        adapter='low' if degree.real<1 else 'high'
        tau,nu=(degree,x1) if adapter=='low' else (2-degree,1-x2)
        zeta=cmath.exp(1j*math.pi*(tau-2*nu))
        cv=-cmath.cos(math.pi*tau)
        assert cv.real>0 and zeta.real>0
        Ws=1+2*cv*zeta
        Vs=Ws+zeta*zeta
        physical_y=-wv/(zv+1)
        assert zv.imag*wv.imag>0
        central_frames += 1
        for side,Yv in [('input',physical_y),('output',1/physical_y)]:
            rg=(Vs*Yv-zeta*zeta+Ws)/(2j*zeta)
            # The phase-coordinate characteristic is unchanged by high adapter.
            assert abs(rg*rg-Ws)<2e-8*max(1,abs(Ws))
            expect=wv.imag<0 if side=='input' else wv.imag>0
            assert (rg.real>0)==expect, (adapter,side,zv,wv,rg)
            checks[f'{adapter}_{side}'] += 1
        if central_frames>=1000 and all(v>=100 for v in checks.values()):
            break
    assert central_frames>=1000 and all(v>=100 for v in checks.values())

    result={
        'status':'PASS',
        'exact_original_head_and_prefix_formulas':3,
        'exact_low_high_input_output_roots':4,
        'exact_two_sheet_involution_checks':3,
        'exact_centralizer_strip_translation':True,
        'exact_selector_characteristic_and_recovery':True,
        'central_frame_regressions':central_frames,
        'selector_vs_oriented_side_regressions':checks,
        'scope':'Actual endpoint local sheet certificate and strip reduction. '
                'No whole-plat feasibility, normal-current estimate, discrete-channel '
                'continuation or contributing-cycle claim.'
    }
    Path(__file__).with_name('actual_augmented_plat_selected_local_certificate_results.json').write_text(
        json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
