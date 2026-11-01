#!/usr/bin/env python3
"""Exact rational identities for the marked pure two-octahedron chart.

These identities verify the displayed local matrices. They do not replace
the ribbon-cut identification or the oriented global marking argument.
No files are changed unless --output is explicitly supplied.
"""
import argparse
import json
import sympy as s


def run_checks():
    E, m, Q, P = s.symbols('E m Q P', nonzero=True)
    A = (m*E+Q)/(m+Q)
    B = P*(1-m*E)/(P+m)
    Rv = (m*E+Q)*(m*E*Q+1)/(E*m*(Q**2+1)+2*E*Q*m**2+Q*(1-m**2))
    Rw = -P*(m*E-1)**2/(E*m**2*(P**2+1)+2*E*P*m+P*(m**2-1))
    G = s.factor(s.together(Rv-Rw)).as_numer_denom()[0]/(E*m**2)
    G = s.Poly(s.cancel(G), E).as_expr()
    X = (E*Q**2*m+E*Q*m**2+E*Q*m+E*m-Q*m+Q)/(E*Q*m**2-E*Q*m+Q**2*m+Q*m+Q+m)
    Xw = -(E*P**2*m+E*P*m+E*P+E*m+P*m-P)/(E*P*m-E*P-P**2-P*m-P-1)
    results = []

    def check(name, expression, locus=False):
        num = s.cancel(expression).as_numer_denom()[0]
        if locus and num != 0:
            num = s.rem(s.Poly(num, E), s.Poly(G, E)).as_expr()
        assert s.cancel(num) == 0, name
        results.append(name)

    def maps(R):
        S = s.factor(m**2*R/(1+(m**2-1)*R))
        L = 1/E
        l1, l2, l3 = L/m, L/m**2, L*m
        c2 = s.cancel((l2*(R-1)/(S-1)-1)/(R-1))
        c3 = s.cancel((l3*R/S-1)/R)
        W = [s.diag(L, 1), s.Matrix([[l1,1-l1],[0,1]]),
             s.Matrix([[c2+l2,1-c2-l2],[c2,1-c2]]),
             s.Matrix([[l3,0],[c3,1]])]
        return S, [C.applyfunc(s.factor) for C in W]

    def mob(C,z):
        return s.cancel((C[0,0]*z+C[0,1])/(C[1,0]*z+C[1,1]))

    def derivative(C,z):
        C=C.applyfunc(s.factor)
        return s.factor(det2(C)/(C[1,0]*z+C[1,1])**2)

    def det2(C):
        return s.factor(C[0,0]*C[1,1]-C[0,1]*C[1,0])

    def sv(a,r):
        return s.Matrix([[0,r*a*(1-a)],[a-r,r-a*a]]).applyfunc(s.factor)

    def sw(b,r):
        return s.Matrix([[b*(b-1),-r*b*(b-1)],[b-r,r-b]]).applyfunc(s.factor)

    def projective_equal(name,C,D):
        C=C.applyfunc(s.factor)
        D=D.applyfunc(s.factor)
        Z = C*D.adjugate()
        for label,value in [('01',Z[0,1]),('10',Z[1,0]),('diag',Z[0,0]-Z[1,1])]:
            check(name+' '+label,value)

    # Each endpoint identity holds on its own local apex locus.
    Sv, Wv = maps(Rv)
    a=A/E
    bv=1+(B-1)/(E*m)
    check('v apex W0',mob(Wv[0],A)-a)
    check('v apex W2',mob(Wv[2],A)-a)
    check('w apex W1',mob(Wv[1],B)-bv)
    vp,vm=sv(A,Rv),sv(a,Sv)
    for name,j,k in [('v return0',0,0),('v return2',2,2),('v cross-return',3,1)]:
        projective_equal(name,Wv[j]*vp,vm*Wv[k])
    Sw,Ww=maps(Rw)
    b=1+(B-1)/(E*m)
    check('w apex W3',mob(Ww[3],B)-b)
    wp,wm=sw(B,Rw),sw(b,Sw)
    for name,j,k in [('w return1',1,1),('w return3',3,3),('w cross-return',0,2)]:
        projective_equal(name,Ww[j]*wp,wm*Ww[k])

    # Four native main derivatives, infinity measured in 1/z.
    corners=[0,s.oo,1,Rv]
    for j,z in enumerate(corners):
        C=(Wv[(j-1)%4].adjugate()*Wv[j]).applyfunc(s.factor)
        if z is s.oo:
            check('main corner infinity fixes infinity',C[1,0])
            value=s.factor(det2(C)/C[0,0]**2)
        else:
            check('main corner '+str(j)+' fixed',mob(C,z)-z)
            value=derivative(C,z)
        check('main corner '+str(j)+' multiplier',value-[1/m,m,1/m,m][j])

    Uv=(E*m+Q)*(Q*m+1)/((Q+m)*(E*Q*m+1))
    Uw=(E+P)*(P+m)/((E*P+1)*(P*m+1))
    check('v meridian',derivative(vp,A)-Uv)
    check('w meridian',derivative(wp,B)-Uw)
    check('v longitude',derivative(Wv[2],A)*E-Q**2)
    check('w longitude',(1/(E*m))/derivative(Ww[3],B)-P**2)
    check('v source coordinate',Uv-(Q+X)/(1+Q*X))
    check('w source coordinate',Uw-(P+Xw)/(1+P*Xw))
    check('common source coordinate',X-Xw,True)
    edge=(X+Q)*(X+1/Q)*(X+P)*(X+1/P)-(X-1)**2*(1-X*m)*(1-X/m)
    check('source edge equation',edge,True)
    check('complete wire coordinate',X.subs(m,1)-E)

    # The doubled pants seam includes its shear, not only puncture traces.
    D1=E
    D2=mob(Wv[1].adjugate(),a)
    D3=s.cancel(Wv[2].adjugate()[0,0]/Wv[2].adjugate()[1,0])
    D4=mob(Wv[2].adjugate(),0)
    D5=mob(Wv[3].adjugate(),a)
    D6=E*Sv
    ratios=[(A-1)/(A-D1),(1-D2)/(1-A),(A-D3)/(1-D3),
            A*(Rv-D4)/((A-D4)*Rv),(Rv-A)*D5/((Rv-D5)*A),
            Rv*(A-D6)/(D6*(A-Rv))]
    targets=[-m/Q,-Q,-1/(m*Q),-m*Q,-1/Q,-Q/m]
    for i,(r,t) in enumerate(zip(ratios,targets)):
        check('pants seam '+str(i),r-t)
    for i in range(3):
        check('reversed pants cancellation '+str(i),targets[3+i]*targets[2-i]-1)

    # Other endpoint has the same local table with m inverted.
    def inv(C,z):
        D=C.adjugate()
        if z is s.oo:
            return s.factor(D[0,0]/D[1,0])
        return mob(D,z)
    d0,d1,d2=inv(Ww[3],1),inv(Ww[2],b),inv(Ww[1],Sw)
    d3,d4,d5=inv(Ww[1],0),inv(Ww[0],b),inv(Ww[3],s.oo)
    wratios=[(B-1)*(Rw-d0)/((B-d0)*(Rw-1)),
             (Rw-B)*(1-d1)/((Rw-d1)*(1-B)),
             (1-Rw)*(B-d2)/((1-d2)*(B-Rw)),
             B/(B-d3),d4/B,(B-d5)/(-d5)]
    for i,(r,t) in enumerate(zip(wratios,[-1/(P*m),-P,-m/P,-P/m,-1/P,-P*m])):
        check('other endpoint seam '+str(i),r-t)

    # A naive odd three-point swap in the fixed white chart is NOT an edge return.
    Ao=s.Matrix([[Sv,-Sv],[1,Sv*(A-1)/a-A]]).applyfunc(s.factor)
    Bo=s.Matrix([[(a*(A-Rv)+Rv)/A,-Rv],[1,-Rv]]).applyfunc(s.factor)
    defect=(Wv[0].adjugate()*Bo).applyfunc(s.factor)
    defect=(defect*Wv[2].adjugate()).applyfunc(s.factor)
    defect=(defect*Ao).applyfunc(s.factor)
    check('fixed-white odd defect lower entry',defect[1,0])
    check('fixed-white odd defect dilation',defect[0,0]/defect[1,1]-m**-2)
    check('fixed-white odd defect translation',defect[0,1]/defect[1,1]-(1-m**-2)*A)

    # At m=1 the regular Hurwitz meridian is the original positive odd word.
    W0c=Wv[0].subs(m,1)
    W2c=Wv[2].subs(m,1)
    Pc=(W2c.inv()*W0c).applyfunc(s.factor)
    Hc=(Pc.inv()-s.eye(2)).applyfunc(s.factor)
    old_positive=(W0c.inv()*Bo.subs(m,1)).applyfunc(s.factor)
    continued_positive=(vp.subs(m,1).inv()*Hc).applyfunc(s.factor)
    projective_equal('positive odd collar calibration',old_positive,continued_positive)

    # Literal four-segment main word. Its commutator lift has determinant one.
    p=sv(A,Rv); w=sw(B,Rv)
    Lam=(w*p.adjugate()).applyfunc(s.factor)
    Lam=(Lam*w.adjugate()).applyfunc(s.factor)
    Lam=(Lam*p).applyfunc(s.factor)
    Lam=(Lam/(det2(p)*det2(w))).applyfunc(s.factor)
    f=(m-X)/(1-m*X)
    check('main word fixes infinity',Lam[1,0])
    check('main word selected diagonal',Lam[0,0]+1/f,True)
    check('main word opposite diagonal',Lam[1,1]+f,True)
    complete=Lam.subs({m:1,Q:1,P:1,E:s.I}).applyfunc(s.simplify)
    assert complete==s.Matrix([[-1,2+2*s.I],[0,-1]])
    results.append('complete main word and central sign')

    return {'purpose':'Exact local marked face/peripheral identities; no substitute for the global cut proof',
            'checks':len(results),'identities':results,'all_exact':True,
            'complete_main_word':str(complete)}


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--output')
    args=parser.parse_args()
    result=run_checks()
    encoded=json.dumps(result,indent=2)+'\n'
    if args.output:
        with open(args.output,'w',encoding='utf8') as handle:
            handle.write(encoded)
    print(encoded)
