#!/usr/bin/env python3
"""Exact rational critical-phase / original ordered-character certificate.

The four generic centralizer identities are checked by polynomial ideal
reduction over Q(T,U,V,J), not by a finite set of numerical samples.
No quantum cycle selection or absolute regulator comparison is inferred.
"""
import json
from pathlib import Path
import sympy as s
from sympy.combinatorics.free_groups import free_group


def certificate():
    T,U,V,J,Z,W=s.symbols('T U V J Z W')
    polynomial=lambda x,z:s.expand(T*(J-z)**2*(x-z)+(z-1)**2*(T*z-x*J))
    momentum=lambda x,z:(1-x)*(T*z-x*J)/(J*(x-z)*(T-x))
    D=J*Z*W*(T-J)*(T-U)*(T-V)/((T*J-1)*(T*Z-U*J)*(T*W-V*J))
    R=Z*W*(J-1)**4*(T*Z-U*J)*(T*W-V*J)/(J*U*V*(J-Z)**2*(J-W)**2*(T-J)*(T*J-1))
    y=momentum(U,Z)
    aa=(U-T)*(1-U)/T; dd=2*U*(1+T-U)/T
    residual=-U*(J-T)*polynomial(U,Z)/(J*T*(U-Z)*(J*U-T*Z))
    assert s.cancel(aa*(y+1/y)+dd-J-1/J-residual)==0
    yy=s.symbols('y')
    inverse=U*J*(yy*(T-U)+(1-U))/(yy*J*(T-U)+T*(1-U))
    assert s.cancel(momentum(U,inverse)-yy)==0
    f=(1-V)*momentum(V,W)+T-V
    fout=(1-U)/momentum(U,Z)+T-U
    f_residual=V*Z*(J-T)*(T-U)*polynomial(V,W)/((V-W)*(J*T-1)*(J*U-T*Z)*(J*V-T*W))
    assert s.cancel(fout-D*f-f_residual)==0
    def head(x,shift):
        return s.Matrix([[-1/x,(1-x)/(x*shift)],[-shift*(1-x)/x,-2+1/x]])
    c=J+1/J
    P=s.Matrix([[1/T,(c-T-1/T)/f],[f/T,c-1/T]])
    ain=head(V,momentum(V,W)); aout=head(U,1/(D*momentum(U,Z)))
    assert s.cancel(P.det()-1)==0
    assert s.cancel(ain.det()-1)==0 and s.trace(ain)==-2
    Ctilde=(J-R/J)*s.eye(2)+(R-1)*P
    domain=s.QQ.frac_field(T,U,V,J)
    ideal=s.groebner([polynomial(U,Z),polynomial(V,W)],Z,W,domain=domain)
    zero_entries=[]
    for i in range(2):
        for j in range(2):
            numerator=s.together((Ctilde*ain-aout*Ctilde)[i,j]).as_numer_denom()[0]
            assert ideal.reduce(numerator)[1]==0
            zero_entries.append([i,j])
    # Literal high-degree index translation. These are PHYSICAL head
    # coordinates, not the low coordinates relabeled as actual meridians.
    Dhigh=1/(D*momentum(U,Z)*momentum(V,W))
    fhigh=(1-V/T)*momentum(V,W)+(1-V)/T
    Phigh=s.Matrix([[T,(c-T-1/T)/fhigh],[fhigh*T,c-T]])
    ainhigh=head(V/T,momentum(V,W))
    aouthigh=head(U/T,1/(Dhigh*momentum(U,Z)))
    Chigh=(J-R/J)*s.eye(2)+(R-1)*Phigh
    high_zero_entries=[]
    for i in range(2):
        for j in range(2):
            numerator=s.together((Chigh*ainhigh-aouthigh*Chigh)[i,j]).as_numer_denom()[0]
            assert ideal.reduce(numerator)[1]==0
            high_zero_entries.append([i,j])
    endpoint=s.groebner([polynomial(U,Z).subs(J,-1),polynomial(V,W).subs(J,-1)],
                       Z,W,domain=s.QQ.frac_field(T,U,V))
    numerator=s.together((R-1).subs(J,-1)).as_numer_denom()[0]
    assert endpoint.reduce(numerator)[1]==0
    # At the endpoint use a literal Jordan frame. All common-trace pairs
    # have lower-left entry four after P+I is normalized to E_12.
    a,b=s.symbols('a b')
    H=s.Matrix([[0,1],[0,0]])
    A=s.Matrix([[a,-(a+1)**2/4],[4,-2-a]])
    C=s.eye(2)+b*H; Aprime=s.simplify(C*A*C.inv())
    comm=H*A-A*H
    assert s.trace(H*A)==4
    assert s.trace(comm*comm)==32
    assert s.simplify(s.trace(comm*Aprime)/32-b)==0
    # Source cap relations in the ORIGINAL complete principal chart.
    X,S=s.symbols('X S',nonzero=True)
    k1=-1/X;k2=-X
    f1=-S*(1-X);f2=S*(1-1/X)
    e1=(1/X-1)/(-S);e2=(X-1)/S
    assert s.simplify(f1+f2/k1)==0
    assert s.simplify(e1*k2+e2)==0
    assert k1*k2==1
    # The critical-value envelope derivative is entirely from the original
    # centered Fourier color term, once an actual stationary branch exists.
    xi,chi,sign=s.symbols('xi chi sigma')
    color_phase=sign*s.pi*s.I*(1-2*xi)*chi
    Vlong=sign*4*s.pi*s.I*(xi-s.Rational(1,2))
    assert s.simplify(-2*s.diff(color_phase,chi)-Vlong)==0
    assert s.simplify(2*s.pi*s.I*s.diff(color_phase,chi)
                      -s.Rational(1,2)*Vlong*(-2*s.pi*s.I))==0
    # Literal chronological mixed-loop word, before imposing auxiliary closure.
    group,Aword,Bword,Cword=free_group('A B C')
    words=[Aword,Bword,Cword]
    for index in (1,0,0,1):
        first,second=words[index:index+2]
        words[index:index+2]=[first**-1*second*first,first]
    Pword=Bword*Aword; Kword=Pword**-1*Cword*Pword
    assert words==[Kword**-1*Aword*Kword,Kword**-1*Bword*Kword,Kword]
    return {
        'status':'PASS',
        'generic_casimir_residual':'exact polynomial multiple of P(U,Z)',
        'magnetic_inverse':'exact rational identity',
        'full_normalized_F_transport':'exact polynomial multiple of P(V,W)',
        'centralizer_matrix_entries_reduced_to_zero':zero_entries,
        'physical_high_chamber_conjugator_entries_reduced_to_zero':high_zero_entries,
        'coefficient_field':'Q(T,U,V,J)',
        'endpoint_R0_equals_one':'exact reduction modulo both endpoint quadratics',
        'parabolic_normal':'Tr([H,A] Aout)/32=b',
        'original_cap_principal_product':'identity',
        'conditional_stationary_action_differential':'d(2pi i phi)=1/2 sum V dU from original centered Fourier coupling',
        'literal_mixed_loop_word':'[2,1,1,2] gives (K^-1 A K,K^-1 B K,K), K=P^-1 C P',
        'scope':'Local actual critical-phase character transport only. Global marked logarithmic lift, absolute regulator, cycle selection, and source gap remain unproved.'
    }


if __name__=='__main__':
    result=certificate()
    Path(__file__).with_name('actual_augmented_plat_local_critical_character_map_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
