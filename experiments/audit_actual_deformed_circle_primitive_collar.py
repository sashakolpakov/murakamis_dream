#!/usr/bin/env python3
"""Exact collar algebra and original ordered circle/line maps.

The audit retains the primitive contact pairing, rather than identifying
it with the doubled shaded-reflection word. Global assembly is not tested.
"""
import argparse
import json
from pathlib import Path
import mpmath as mp
import sympy as sp


def symbolic():
    x,y,b,s=sp.symbols('x y b s',positive=True)
    A=x+y;D=A*A-4*x*y*s*s;Tb2=b*A+x*y+b*b*s*s;Bb=A+2*b*s*s
    rx,ry,rb=1/x,1/y,1/b;L2=D/(x*x*y*y)
    uL=(L2+rx*rx-ry*ry)/2;pL=uL+rb*(rx-ry)
    q2=(rx+rb)**2-pL*pL/L2
    num=rx*(rx+rb)-uL*pL/L2
    checks=[Bb*Bb-4*s*s*Tb2-D,
            q2-4*(1-s*s)*Tb2/(b*b*D),
            num-2*(1-s*s)*Bb/(b*D),
            rx*rx-uL*uL/L2-4*s*s*(1-s*s)/D]
    B,T=sp.symbols('B T');E=B+2*s*T;DD=B*B-4*s*s*T*T
    checks += [(B-2*s*T)*E-DD,
               (B-2*s*T)/(B+2*s*T)-DD/E**2,
               (B+2*s*T)/(B-2*s*T)-E**2/DD]
    z,X,Y,t,v=sp.symbols('z X Y t v',real=True)
    # The shaded-circle equation gives the exact centered modulus ratio.
    num0=X*X+(Y-v)**2;den0=X*X+(Y+v)**2
    checks.append(sp.rem(sp.Poly((t+v)*num0-(t-v)*den0,X),
                         sp.Poly(X*X+Y*Y-2*t*Y+v*v,X)).as_expr())
    for value in checks:assert sp.factor(value)==0,value
    # Explicit outer product, selected eigenflag and projective multiplier.
    L,rx,ry,u,v,C,S=sp.symbols('L rx ry u v C S',real=True)
    P=sp.Matrix([[ry*ry-L*L,L*rx*rx],[-L,rx*rx]])/(rx*ry)
    assert sp.factor(P.det()-1)==0
    pminus=u-sp.I*v;J=-C+sp.I*S
    eigen=P*sp.Matrix([pminus,1])-J*sp.Matrix([pminus,1])
    substitutions={u:(L*L+rx*rx-ry*ry)/(2*L),
                   v:rx*ry*S/L,C:(L*L-rx*rx-ry*ry)/(2*rx*ry)}
    for value in eigen:
        value=sp.factor(value.subs(substitutions,simultaneous=True))
        value=value.subs(S*S,1-((L*L-rx*rx-ry*ry)/(2*rx*ry))**2)
        assert sp.factor(value)==0,value
    return {'exact_radius_and_selected_flag_identities':len(checks)+3}


def reflection(X,Y,r,star=False):
    sign=-1 if star else 1
    return mp.matrix([[X+sign*1j*Y,r*r-X*X-Y*Y],[1,-X+sign*1j*Y]])/r


def transform(M,z):
    return (M[0,0]*z+M[0,1])/(M[1,0]*z+M[1,1])


def err(A,B):
    return mp.norm(A-B)/max(1,mp.norm(A),mp.norm(B))


def hmove(pair,direction=1):
    A,B=pair
    return (A**-1*B*A,A) if direction==1 else (B,B*A*B**-1)


def threaded(A,B,aux):
    data=[A,B,aux]
    for j in (2,1,1,2):data[j-1:j+1]=hmove(data[j-1:j+1])
    return data


def data(x,b,c,y,delta):
    s=mp.sin(mp.pi*delta);co=mp.cos(mp.pi*delta);A=x+y
    D=A*A-4*x*y*s*s;rootD=mp.sqrt(D);L=rootD/(x*y)
    rx,ry,rb,rc=1/x,1/y,1/b,1/c
    u=(L*L+rx*rx-ry*ry)/(2*L);v=2*s*co/rootD
    Tb=mp.sqrt(b*A+x*y+b*b*s*s);Tc=mp.sqrt(c*A+x*y+c*c*s*s)
    Eb=A+2*b*s*s+2*s*Tb;Ec=A+2*c*s*s+2*s*Tc
    pb=u+rb*(rx-ry)/L;pc=u+rc*(rx-ry)/L
    qb=2*co*Tb/(b*rootD);qc=-2*co*Tc/(c*rootD)
    X=reflection(0,0,rx);Xs=reflection(0,0,rx,True)
    Y=reflection(L,0,ry);Ys=reflection(L,0,ry,True)
    B=reflection(pb,qb,rb);Bs=reflection(pb,qb,rb,True)
    C=reflection(pc,qc,rc);Cs=reflection(pc,qc,rc,True)
    Ain=B*Xs;Bin=Y*Bs;Ao=C*Xs;Bo=Y*Cs;P=Bin*Ain
    J=-mp.exp(-2j*mp.pi*delta);R=Eb*Ec/D
    transport=mp.eye(2)+(R-1)/(J-1/J)*(P-mp.eye(2)/J)
    corners=[rx*(pb+1j*qb)/(rx+rb),
             L+ry*(pb+1j*qb-L)/(ry+rb),
             rx*(pc+1j*qc)/(rx+rc),
             L+ry*(pc+1j*qc-L)/(ry+rc)]
    return locals()


def finite_patterns():
    count=contact=threads=half=0;worst=mp.mpf(0);double=0
    radii=[('1.3','.7','1.9','2.1'),('1','1','1','1'),('.9','2.2','.8','1.7')]
    deltas=[mp.mpf('.012'),mp.mpf('.037'),mp.mpf('-.021'),mp.mpc('.015','.006')]
    for row in radii:
        x,b,c,y=map(mp.mpf,row)
        for de in deltas:
            d=data(x,b,c,y,de);P=d['P'];J=d['J'];R=d['R'];C=d['transport']
            for U,V in [(C*d['Ain']*C**-1,d['Ao']),(C*d['Bin']*C**-1,d['Bo']),
                        (P,d['Y']*d['Xs'])]:
                ee=err(U,V);assert ee<mp.mpf('1e-65');worst=max(worst,ee);count+=1
            vec=mp.matrix([d['u']-1j*d['v'],1])
            assert err(P*vec,J*vec)<mp.mpf('1e-65')
            assert err(C*vec,R*vec)<mp.mpf('1e-65');count+=2
            for source,target in zip(d['corners'][:2],d['corners'][2:]):
                ee=abs(transform(C,source)-target)/max(1,abs(target))
                assert ee<mp.mpf('1e-65');worst=max(worst,ee);contact+=1
            rb2=d['D']/d['Eb']**2;rc2=d['Ec']**2/d['D']
            assert abs(rc2/rb2-R*R)<mp.mpf('1e-65');double+=1
            H=P**-1-mp.eye(2)
            for eps in (-1,0,1):
                pure=C*H**(-eps)
                aux=(-1)**eps*mp.sqrt(mp.det(pure))*pure**-1
                actual=threaded(d['Ain'],d['Bin'],aux)
                assert err(actual[2],aux)<mp.mpf('1e-65')
                pair=actual[:2]
                if eps:pair=hmove(pair,eps)
                assert err(pair[0],d['Ao'])<mp.mpf('1e-65')
                assert err(pair[1],d['Bo'])<mp.mpf('1e-65');threads+=1
                ev=(aux*vec)[1]/vec[1]
                assert abs(ev**-2/(R*(-J)**eps)-1)<mp.mpf('1e-65');half+=1
    return {'ordered_pair_and_selected_flag_checks':count,'literal_contact_pairings':contact,
            'primitive_vs_double_reflection_checks':double,
            'actual_threading_and_half_twist_words':threads,'primitive_eigenvalue_checks':half,
            'maximum_relative_error':str(worst)}


def hermitian_circle(X,Y,r):
    return mp.matrix([[1,-X-1j*Y],[-X+1j*Y,X*X+Y*Y-r*r]])/r


def marked_line_limits():
    linechecks=regchecks=flipped=0;worst=mp.mpf(0);wrong_unsigned=[]
    for r,rc in [(mp.mpf('.7'),mp.mpf('.9')),(mp.mpf('.6'),mp.mpf('1.2'))]:
        for de in [mp.mpf('.014'),mp.mpf('.043'),mp.mpc('.018','.007')]:
            psi=2*mp.pi*de;H=r*(1+mp.cos(psi))
            p=mp.sqrt(r*r*mp.sin(psi)**2+2*r*rc*(1+mp.cos(psi)));cy=H-rc
            Xs=reflection(0,r,r,True)
            low=-1j*mp.eye(2);lows=1j*mp.eye(2)
            upper=1j*mp.matrix([[1,2j*H],[0,1]])
            output=reflection(p,cy,rc);outputs=reflection(p,cy,rc,True)
            P=upper*Xs;Ain=low*Xs;Bin=upper*lows
            Ao=output*Xs;Bo=upper*outputs
            x,c=1/r,1/rc;s=mp.sin(mp.pi*de);T=mp.sqrt(c*x+c*c*s*s)
            R=(x+2*c*s*s+2*s*T)/x;J=-mp.exp(-1j*psi)
            C=mp.eye(2)+(R-1)/(J-1/J)*(P-mp.eye(2)/J)
            for U,V in [(C*Ain*C**-1,Ao),(C*Bin*C**-1,Bo)]:
                ee=err(U,V);assert ee<mp.mpf('1e-65');worst=max(worst,ee);linechecks+=1
            flag=mp.matrix([r*mp.sin(psi)+1j*H,1])
            assert err(P*flag,J*flag)<mp.mpf('1e-65');linechecks+=1
            if mp.im(de):continue
            forms=[hermitian_circle(0,r,r),mp.matrix([[0,1j],[-1j,0]]),
                   hermitian_circle(p,cy,rc),mp.matrix([[0,-1j],[1j,2*H]])]
            for t in map(mp.mpf,['.07','.025','.008','-.07','-.025','-.008']):
                g=mp.matrix([[1,0],[-t,1+1j*H*t/2]]);g/=mp.sqrt(mp.det(g));ig=g**-1
                moved=[ig.transpose_conj()*form*ig for form in forms]
                curv=[mp.re(form[0,0]) for form in moved]
                assert min(curv)>0
                centers=[-form[0,1]/form[0,0] for form in moved]
                xx,bb,cc,yy=curv;AA=xx+yy;DD=AA*AA-4*xx*yy*s*s
                Eb=AA+2*bb*s*s+2*s*mp.sqrt(bb*AA+xx*yy+bb*bb*s*s)
                Ec=AA+2*cc*s*s+2*s*mp.sqrt(cc*AA+xx*yy+cc*cc*s*s)
                direction=centers[3]-centers[0]
                sigb=int(mp.sign(mp.im((centers[1]-centers[0])*mp.conj(direction))))
                sigc=int(mp.sign(mp.im((centers[2]-centers[0])*mp.conj(direction))))
                assert sigb and sigc
                Rp=(Eb/mp.sqrt(DD))**sigb*(Ec/mp.sqrt(DD))**(-sigc)
                ee=abs(Rp/R-1);assert ee<mp.mpf('1e-65');worst=max(worst,ee)
                if (sigb,sigc)!=(1,-1):
                    assert sigb==-1 and sigc==-1
                    bad=abs(Eb*Ec/DD/R-1);assert bad>mp.mpf('1e-8')
                    wrong_unsigned.append(float(bad));flipped+=1
                Pp=g*P*ig
                Cp=mp.eye(2)+(Rp-1)/(J-1/J)*(Pp-mp.eye(2)/J)
                assert err(ig*Cp*g,C)<mp.mpf('1e-65');regchecks+=1
    return {'literal_marked_200_maps_and_flags':linechecks,
            'common_positive_circle_regularizations':regchecks,
            'genuinely_flipped_compactifications':flipped,
            'minimum_wrong_unsigned_relative_error':min(wrong_unsigned),
            'maximum_relative_error':str(worst)}


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',default='experiments/actual_deformed_circle_primitive_collar_results.json');args=ap.parse_args()
    mp.mp.dps=80
    result={'status':'PASS','precision_digits':80,'symbolic':symbolic(),
            'finite_circles':finite_patterns(),'marked_lines':marked_line_limits(),
            'scope':'Original ordered white-reflection products, literal even contact pairing, selected eigenflag, actual threading/Hurwitz words and common marked-line conjugation. The doubled shaded-reflection multiplier is retained separately. Global group assembly, regulator and filled-source bounds are not inferred from these checks.'}
    Path(args.output).write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))


if __name__=='__main__':main()
