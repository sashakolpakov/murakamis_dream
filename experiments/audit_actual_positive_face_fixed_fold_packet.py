#!/usr/bin/env python3
"""Original Newton source, reflected finite system, refined real diagnostics."""
import argparse
import json
from pathlib import Path

import mpmath as mp
import sympy as sp

from audit_actual_q_hahn_negative_clock_boundary import literal_h
from audit_actual_positive_face_channel_rate import continuants, forced, sine_factorials


def source_z(N,a,x,b,y):
    """Homogenize the ORIGINAL finite H sum, before any recurrence/reflection.

    This literal summand formula also evaluates at zero faces.
    """
    q=mp.exp(1j*mp.pi/N);Q=q*q
    F=[mp.mpc(1)]
    for r in range(1,a+1):F.append(F[-1]*(1-Q**r))
    return mp.fsum(q**(k*k-a*a)*(F[a]/(F[k]*F[a-k]))**2
                  *mp.fprod(x+q**(2*r+1)*b for r in range(k))
                  *mp.fprod(b+q**(2*r+1)*y for r in range(a-k))
                  for k in range(a+1))


def coefficients(N,j,x,b,y):
    th=mp.pi/N;A=x+y
    u=mp.cos((j-1)*th)*mp.sin(j*th)
    v=mp.sin((2*j-1)*th)*(A+2*b*mp.cos(j*th)*mp.cos((j-1)*th))
    w=mp.sin((j-1)*th)*mp.cos(j*th)*(A*A-4*x*y*mp.cos((j-1)*th)**2)
    D=x*x+y*y-2*x*y*mp.cos(2*j*th)
    return u,v,w,D


def system(N,j,x,b,c,y):
    u,vb,w,D=coefficients(N,j,x,b,y)
    _,vc,_,_=coefficients(N,j,x,c,y)
    M=mp.matrix([[vb*vc,-vb*w,-w*vc,w*w],
                 [u*vb,0,-u*w,0],[u*vc,-u*w,0,0],[u*u,0,0,0]])
    return u*u*D,M


def symbolic():
    A,b,x,y,s,c,T=sp.symbols('A b x y s c T', nonzero=True)
    H=b*(x+y)+x*y+b*b*s*s
    Ep=x+y+2*b*s*s+2*s*sp.sqrt(H)
    Em=x+y+2*b*s*s-2*s*sp.sqrt(H)
    assert sp.expand(Ep*Em-((x+y)**2-4*x*y*s*s))==0
    # Derivative of log(c sqrt(H)) under ds/dz=pi c,dc/dz=-pi s.
    J=c*sp.sqrt(H)
    derivative=sp.pi*c*sp.diff(J,s)-sp.pi*s*sp.diff(J,c)
    expected=sp.pi/2*(-s/c+b*b*s*c/H)
    assert sp.simplify(derivative/(2*J)-expected)==0
    gap,gapprime,tan,tanprime=sp.symbols('gap gapprime tan tanprime',nonzero=True)
    a=(gapprime/gap-tanprime/tan)/2
    assert sp.expand(tanprime*gap/2+tan*(a*gap-gapprime/2))==0
    # Product-root quartic: eliminate the two actual quadratic roots.
    e,f,Bb,Bc,D,lam=sp.symbols('e f Bb Bc D lam')
    poly=D*(lam**4+1)-4*Bb*Bc*(lam**3+lam)+(4*Bb**2+4*Bc**2-2*D)*lam**2
    expr=sp.together(poly.subs(lam,e*f/D)*D**3).expand()
    rem=sp.rem(sp.rem(expr,e*e-2*Bb*e+D,e),f*f-2*Bc*f+D,f)
    assert sp.expand(rem)==0
    u,z=sp.symbols('u z')
    tensor=sp.kronecker_product(sp.Matrix([[2*Bb,-D],[1,0]]),sp.Matrix([[2*Bc,-D],[1,0]]))
    assert sp.expand((u*u*D*sp.eye(4)-z*u*u*tensor).det()-u**8*D**3*poly.subs(lam,z))==0
    return {'reflection_first_correction_and_full_characteristic_identities':5}


def exact_sources():
    counts=dict(original_homogeneous_Newton_values=0,original_nonzero_chart_values=0,
                lower_original_determinants=0,large_source_reflections=0,
                endpoint_safe_scalar_recurrences=0,zero_leading_fold_equations=0,
                literal_terminal_equations=0,finite_vector_rows=0,
                finite_Fourier_equations=0,reflected_cosine_identities=0,
                Laurent_coefficient_evaluations=0)
    worst=mp.mpf(0)
    def check(z,w):
        nonlocal worst
        err=abs(z-w)/max(1,abs(w));worst=max(worst,err)
        assert err<mp.mpf('1e-65'),(z,w,err)
    params=[('1.3','.8','1.1','2.1'),('1.1','0','0','1.7'),
            ('0','0','1.2','1.7'),('1.7','.8','0','0'),
            ('1.4','0','0','1.4')]
    for N in range(3,15):
        d=N-1;M=d//2;q=mp.exp(1j*mp.pi/N);Q=q*q;th=mp.pi/N;S=sine_factorials(N)
        for raw in params:
            x,b,c,y=map(mp.mpf,raw)
            Zb=[source_z(N,a,x,b,y) for a in range(N)]
            Zc=[source_z(N,a,x,c,y) for a in range(N)]
            counts['original_homogeneous_Newton_values']+=2*N
            for middle,Z in ((b,Zb),(c,Zc)):
                if middle and y:
                    for a in range(N):
                        z=(-q)**a*q**(-a*a)*y**a*literal_h(N,a,-x/(q*middle),-middle/(q*y))
                        check(Z[a],z);counts['original_nonzero_chart_values']+=1
                DD=continuants(N,M,x,middle,y)
                for a in range(M+1):
                    beta=S[2*a]/S[a]**2
                    check(Z[a],beta*DD[a]);counts['lower_original_determinants']+=1
                    check(Z[d-a],forced(N,a,x,y)*Z[a]);counts['large_source_reflections']+=1
                z=lambda j:Z[j] if 0<=j<N else mp.mpc(0)
                for j in range(1,N+1):
                    u,v,w,D=coefficients(N,j,x,middle,y)
                    check(u*z(j),v*z(j-1)-w*z(j-2))
                    counts['endpoint_safe_scalar_recurrences']+=1
                    if j<N and abs(u)<mp.mpf('1e-70'):
                        counts['zero_leading_fold_equations']+=1
                    if j==N:counts['literal_terminal_equations']+=1
            # Rational auxiliary components retain the original localization.
            P0=forced(N,0,x,y);Ps=[P0]
            for j in range(1,N):
                _,_,_,D=coefficients(N,j,x,b,y);Ps.append(Ps[-1]/D)
            for eps in (-1,0,1):
                omega=lambda j:mp.exp(1j*th*d*d/2)*(-1)**j*q**(j*(j+1))
                V=[]
                for j in range(N):
                    bm=Zb[j-1] if j else 0;cm=Zc[j-1] if j else 0
                    V.append(omega(j)**eps*Ps[j]*mp.matrix([Zb[j]*Zc[j],Zb[j]*cm,bm*Zc[j],bm*cm]))
                zero=mp.matrix([0]*4)
                for j in range(N+1):
                    L,T=system(N,j,x,b,c,y)
                    left=L*(V[j] if j<N else zero)
                    right=(-Q**j)**eps*T*(V[j-1] if j else zero)
                    for z,w in zip(left,right):check(z,w);counts['finite_vector_rows']+=1
                for zz in (mp.mpc('.8','.2'),mp.mpc('1.1','-.13')):
                    left=mp.matrix([0]*4);right=mp.matrix([0]*4)
                    for j in range(N):
                        L,_=system(N,j,x,b,c,y);_,T=system(N,j+1,x,b,c,y)
                        left+=L*V[j]*zz**j
                        right+=zz*(-Q**(j+1))**eps*T*V[j]*zz**j
                    for z,w in zip(left,right):check(z,w)
                    counts['finite_Fourier_equations']+=1
                chi=mp.mpc('.037','.021')
                lhs=mp.fsum((1 if 2*a==d else 2)*V[a][0]*mp.cos(mp.pi*(d-2*a)*chi) for a in range(M+1))
                rhs=mp.fsum(V[a][0]*mp.exp(1j*mp.pi*(d-2*a)*chi) for a in range(N))
                check(lhs,rhs);counts['reflected_cosine_identities']+=1
            # Independently evaluate the specified Laurent functions.
            for j in range(N+1):
                W=Q**j;sw=(q**-1*W-q/W)/(2j);cw=(q**-1*W+q/W)/2
                u=(sw+mp.sin(th))/2
                v=sw*(x+y+b*(cw+mp.cos(th)))
                w=(sw-mp.sin(th))/2*(x*x+y*y-x*y*(Q**-1*W+Q/W))
                D=x*x+y*y-x*y*(W+1/W)
                for actual,expected in zip((u,v,w,D),coefficients(N,j,x,b,y)):check(actual,expected)
                counts['Laurent_coefficient_evaluations']+=1
    counts['maximum_exact_relative_error']=str(worst)
    return counts


def analytic_functions(x,b,y):
    A=x+y;T2=b*A+x*y
    def E(z):
        if T2==0:return A
        si=mp.sin(mp.pi*z)
        return A+2*b*si*si+2*si*mp.sqrt(T2+b*b*si*si)
    def J(z):
        if T2==0:return mp.mpf(1)
        return mp.cos(mp.pi*z)*mp.sqrt(T2+b*b*mp.sin(mp.pi*z)**2)/mp.sqrt(T2)
    def corr(z):
        if T2==0:return mp.mpf(0)
        si,co=mp.sin(mp.pi*z),mp.cos(mp.pi*z)
        return mp.pi/2*(-si/co+b*b*si*co/(T2+b*b*si*si))
    return E,J,corr


def diagnostics():
    profiles=[];worst_res=worst_pivot=worst_packet=mp.mpf(0);pivots=0;complex_res=0
    patterns=[('222','1.3','.7','1.9','2.1'),('202','1.1','0','0','1.7'),
              ('022_002','0','0','1.2','1.7'),('220_200','1.7','.8','0','0')]
    for N in (48,49,96,97,192,193):
        M=(N-1)//2;s0=N-1-2*M;h=1/mp.mpf(N);th=mp.pi/N
        S=sine_factorials(N);beta=[S[2*a]/S[a]**2 for a in range(M+1)]
        for name,*raw in patterns:
            x,b,c,y=map(mp.mpf,raw);A=x+y
            Dfun=lambda z:A*A-4*x*y*mp.sin(mp.pi*z)**2
            allD=[];funcs=[]
            for middle in (b,c):
                D=continuants(N,M,x,middle,y);allD.append(D)
                E,J,corr=analytic_functions(x,middle,y);funcs.append((E,J,corr))
                app=lambda z:E(z)*mp.exp(h*corr(z))
                for a in range(M-int(N*.1),M+1):
                    z=(mp.mpf(N)/2-a)/N
                    actual=beta[a]*D[a]/(beta[a-1]*D[a-1])
                    err=N*N*abs(actual/app(z)-1);worst_pivot=max(worst_pivot,err);pivots+=1
                for z in (mp.mpc('.03','.02'),mp.mpc('-.04','.013'),mp.mpf('.5')/N):
                    tau=mp.tan(mp.pi*z)/mp.tan(mp.pi*(z+h))
                    rhs=(1+tau)*(A+2*middle*mp.sin(mp.pi*z)*mp.sin(mp.pi*(z+h)))-tau*Dfun(z+h)/app(z+h)
                    val=abs(app(z)-rhs)/(h*h*abs(z));worst_res=max(worst_res,val);complex_res+=1
            (Eb,Jb,_),(Ec,Jc,_)=funcs;Db,Dc=allD
            def action(z):
                return mp.quad(lambda v:mp.log(Eb(v)*Ec(v)/Dfun(v)),[0,z])
            d0=mp.mpf(s0)/(2*N)
            for target in (mp.mpf('.025'),mp.mpf('.06'),mp.mpf('.1')):
                t=max(1,int(N*target));a=M-t;delta=mp.mpf(s0+2*t)/(2*N)
                actual=(beta[a]**2*Db[a]*Dc[a]*forced(N,a,x,y)
                        /(beta[M]**2*Db[M]*Dc[M]*forced(N,M,x,y)))
                model=mp.exp(-N*(action(delta)-action(d0)))*mp.sqrt(Jb(d0)*Jc(d0)/(Jb(delta)*Jc(delta)))
                error=actual/model-1;worst_packet=max(worst_packet,N*abs(error))
                profiles.append({'N':N,'pattern':name,'delta':str(delta),'N_relative_error':str(N*error)})
    assert worst_res<100 and worst_pivot<100 and worst_packet<100
    return {'scope':'Refined fixed-real packet and complex residual diagnostics only; no actual complex degree continuation or exponential Fourier error is asserted.',
            'original_refined_pivots':pivots,'complex_analytic_residual_samples':complex_res,
            'fixed_real_packet_profiles':len(profiles),'maximum_N2_pivot_error':str(worst_pivot),
            'maximum_scaled_complex_residual':str(worst_res),'maximum_N_packet_error':str(worst_packet),'profiles':profiles}


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',default='experiments/actual_positive_face_fixed_fold_packet_results.json');args=ap.parse_args()
    mp.mp.dps=90
    data={'status':'PASS','precision_digits':90,'symbolic':symbolic(),'source':exact_sources(),'diagnostics':diagnostics(),
          'scope':'Literal original Newton polynomials at every small and large channel, zero-face limits, actual finite recurrences and Fourier endpoints, reflected source phases and principal symbol. Asymptotic samples are diagnostics; the fixed-real relative theorem is proved analytically. No actual complex-color packet or alias gap is inferred.'}
    Path(args.output).write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps({k:v for k,v in data.items() if k!='diagnostics'},indent=2))
    print(json.dumps({k:v for k,v in data['diagnostics'].items() if k!='profiles'},indent=2))


if __name__=='__main__':main()
