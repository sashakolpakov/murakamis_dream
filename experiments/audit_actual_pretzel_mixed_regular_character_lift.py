#!/usr/bin/env python3
"""Independent rational/matrix and finite-source checks of the regular lift."""
from pathlib import Path
import json
import mpmath as mp
import sympy as sp


def zero(expr):
    assert sp.factor(expr) == 0, sp.factor(expr)


def symbolic():
    X, Y, H, w, m = sp.symbols("X Y H w m", nonzero=True)
    T = H + 1 / H
    den = (1 - Y / H) * (1 - H * Y)
    p = -((T * Y**2 + 2) / Y) / den
    q = -(1 - Y**2)**2 / (Y**2 * den**2)
    d = (1 - Y**2) * (1 + Y) / (Y**2 * den)
    xx = Y * m / (m + Y * d)
    quad = (Y + T + 1) * X**2 - (T * Y + 2) * X + Y - 1
    # The cleared source Riccati equation implies precisely the X equation.
    numerator = sp.together(quad.subs(X, xx)).as_numer_denom()[0]
    riccati = sp.together(m*m - p*m - q).as_numer_denom()[0]
    assert sp.rem(numerator, riccati, m) == 0
    zero(xx.subs({H: 1, m: -1/Y}) - (Y-1)/(Y+3))
    zero((1+X)**2*(X-1) - (X-Y)*(1-X/H)*(1-H*X) - quad)

    Yx = (1+2*X-(T+1)*X**2)/(1-T*X+X**2)
    Z = sp.factor((1+Yx**2 - (1-Yx)**3/(1-Yx/X))/Yx)
    L = (H-X)/(1-H*X)
    lam = -1/L
    beta = -(H-X)*(1-H*X)/(sp.sqrt(H)*(H+1)*(1-X**2))
    zero(sp.sqrt(H)*beta*(lam-Yx)-1)
    zero(beta*(1/lam-Yx)/sp.sqrt(H)-1)
    zero(beta*(-L-1/L-2*Yx)-(H+1)/sp.sqrt(H))
    zero(beta**2*(1+(L+1/L)*Yx+Yx**2)-1)
    Zgroup = 2-(lam-1)**2/(lam+1)**2*(2+lam*H+1/(lam*H))
    zero(Zgroup-Z)

    U = (w*Y-1)/(w-Y)
    D = (w-1)**2/(w+1)**2*(U+1/U)+8*w/(w+1)**2
    numerator = sp.together((D+L+1/L).subs(Y,Yx)).as_numer_denom()[0]
    wpoly = sp.together(w*w-Z*w+1).as_numer_denom()[0]
    zero(sp.rem(numerator,wpoly,w))

    # Explicit actual four-parabolic matrices, with an arbitrary independent U.
    V = sp.symbols("V", nonzero=True)
    tw = (w-1)/(w+1)
    a = sp.Matrix([[2*w/(w+1),1],[-tw**2,2/(w+1)]])
    b = sp.diag(w,1/w)*a.inv()
    c = sp.Matrix([[2/(w+1),w*V],[-tw**2/(w*V),2*w/(w+1)]])
    e = (c*b*a).inv()
    for mat in (a,b,c,e):
        zero(mat.det()-1)
        zero(sp.trace(mat)-2)
    zero(sp.trace(b*a)-w-1/w)
    zero(sp.trace(c*b)-tw**2*(V+1/V)-8*w/(w+1)**2)
    # Generic threaded half twist, before any character quotient.
    lm, mm = sp.symbols("lm mm", nonzero=True)
    tt = (lm-1)/(lm+1)
    aa = sp.Matrix([[2*lm/(lm+1),1],[-tt**2,2/(lm+1)]])
    pp = sp.diag(lm,1/lm)
    bb = pp*aa.inv()
    cc = sp.diag(mm,1/mm)
    rr = cc.inv()*bb*cc
    ss = cc.inv()*bb*aa*bb.inv()*cc
    zero(sp.trace(rr.inv()*aa)-(2-tt**2*(2+lm/mm**2+mm**2/lm)))
    for entry in ss*rr-pp:
        zero(entry)
    # Complete color in a bounded, noncentral trace -2 frame.
    yy = sp.symbols("yy", nonzero=True)
    pp0 = sp.Matrix([[-1,1],[0,-1]])
    cc0 = sp.eye(2)-(pp0+sp.eye(2))/(1+yy)
    zero(cc0.det()-1)
    zero(sp.trace(cc0)-2)
    assert cc0 != sp.eye(2)
    return 18


def finite_sources():
    mp.mp.dps = 100
    worst = mp.mpf(0)
    count = 0
    for N in (9,10,17,18,31,32,33,64,65):
        Q = mp.exp(2j*mp.pi/N)
        F = [mp.mpc(1)]
        for k in range(1,N):
            F.append(F[-1]*(1-Q**k))
        M = (N-1)//2
        for h in sorted({0,1,max(0,N//30)}):
            r = max(h+1,int(mp.ceil(mp.mpf('0.32')*N)))
            if r >= M:
                continue
            terms = [Q**(-v*r)*F[2*v]/(F[v]*F[v-h]*F[v+h]*F[v-r])
                     for v in range(r,M+1)]
            A = sum(terms)
            A1 = sum(Q**(-v*(r+1))*F[2*v]/
                     (F[v]*F[v-h]*F[v+h]*F[v-r-1])
                     for v in range(r+1,M+1))
            moment = sum(t*(Q**(-v)-Q**(-r))
                         for v,t in zip(range(r,M+1),terms))
            err = abs(A1-moment)/max(1,abs(A1),abs(moment))
            worst = max(worst,err)
            assert err < mp.mpf('1e-80')
            # Exact D ratio including every Q shift, before its classical limit.
            D = Q**(-r*r)*F[2*r]/(F[r]*F[r-h]*F[r+h])
            D1 = Q**(-(r+1)**2)*F[2*r+2]/(F[r+1]*F[r+1-h]*F[r+1+h])
            Y,H = Q**r,Q**h
            dratio = Q**(-2*r-1)*(1-Q*Y**2)*(1-Q**2*Y**2)/(
                (1-Q*Y)*(1-Q*Y/H)*(1-Q*Y*H))
            assert abs(D1/D-dratio) < mp.mpf('1e-80')
            count += 1
    return count,mp.nstr(worst,8)


def absolute_cusp():
    mp.mp.dps = 100
    count = 0
    for s in (3,5,7,25,51):
        alpha = mp.pi/s
        c,t = mp.cos(alpha),1/mp.sin(alpha)
        rho = mp.sqrt((1+mp.sin(alpha))/c)
        w,U = -rho**4,mp.exp(2j*alpha)
        Y = mp.exp(2j*mp.atan(1/c))
        def g(z):
            return mp.matrix([[-2*w/(w+1),z],[-t*t/z,-2/(w+1)]])
        for i in (0,1,s-1):
            z = t/rho*mp.exp((2*i+1)*1j*alpha)
            P = g(z)*g(U*z)**-1
            C = mp.eye(2)-(P+mp.eye(2))/(1+Y)
            coord = mp.matrix([[0,1],[U**(-i-1),-rho]])
            PP,CC = coord*P*coord**-1,coord*C*coord**-1
            W = t/rho
            targetP = mp.matrix([[-1,-2j*c*W],[0,-1]])
            targetC = mp.matrix([[1,(1+1j*c)*W],[0,1]])
            assert mp.norm(PP-targetP) < mp.mpf('1e-90')
            assert mp.norm(CC-targetC) < mp.mpf('1e-90')
            count += 1
    return count


def literal_cap_order_and_reversal():
    mp.mp.dps = 90
    count = 0
    for s in (3,5,7):
        w = mp.mpc('-3.2','0.1')
        t2 = ((w-1)/(w+1))**2
        def g(z):
            return mp.matrix([[-2*w/(w+1),z],[-t2/z,-2/(w+1)]])
        def h(z):
            return g(-w*z)
        us = [mp.exp(mp.mpc(str((i+1)/37),str((i+2)/31))) for i in range(s-1)]
        us.append(1/mp.fprod(us))
        incoming = [mp.mpc(0)]*s
        incoming[-1] = 1
        for b in range(s-1,0,-1):
            incoming[b-1] = us[b]*incoming[b]
        outgoing = [us[b]*incoming[b] for b in range(s)]
        for b in range(s):
            nxt = (b+1)%s
            assert abs(incoming[b]-outgoing[nxt]) < mp.mpf('1e-80')
            assert mp.norm(h(incoming[b])**-1*h(outgoing[nxt])-mp.eye(2)) < mp.mpf('1e-80')
            assert mp.norm(g(incoming[b])*g(outgoing[nxt])**-1-mp.eye(2)) < mp.mpf('1e-80')
            count += 1
        # Independent exact geometric cyclic reversal is holomorphic.
        alpha = mp.pi/s
        rho = mp.sqrt(1/mp.cos(alpha)+mp.tan(alpha))
        def Z(k): return rho*mp.exp(2j*k*alpha)
        def Up(k): return mp.exp((2*k+1)*1j*alpha)/rho
        def Um(k): return rho**3*mp.exp((2*k+1)*1j*alpha)
        for k in range(s):
            assert abs(rho*rho/Z(k)-Z(-k)) < mp.mpf('1e-80')
            assert abs(rho*rho/Up(k)-Um(-k-1)) < mp.mpf('1e-80')
            assert abs(rho*rho/Um(k)-Up(-k-1)) < mp.mpf('1e-80')
    return count


if __name__ == "__main__":
    rational = symbolic()
    finite,err = finite_sources()
    cusps = absolute_cusp()
    caps = literal_cap_order_and_reversal()
    result = {"status":"PASS", "cleared_rational_matrix_families":rational,
              "literal_finite_source_moment_families":finite,
              "absolute_original_circle_cusp_matrices":cusps,
              "literal_unequal_port_caps_and_holomorphic_reversal":caps,
              "maximum_relative_source_error":err,
              "scope":"Regular source-selected local lift; global port/cap and longitude markings remain separately typed."}
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
