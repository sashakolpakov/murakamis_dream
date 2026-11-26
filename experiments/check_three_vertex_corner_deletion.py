#!/usr/bin/env python3
"""Exact scalar bounds and original-matrix checks for the corner deletion.

The matrix checks use the defining sine-factorial M, not a positive H
construction. They test all cutoff sizes at small levels; the uniform
asymptotic estimates are proved in the linked note.
"""
from fractions import Fraction as F
from hashlib import sha256
import json
from math import factorial
from pathlib import Path

import mpmath as mp
import sympy as sp


def main():
    comparisons = []
    def positive(name, x):
        assert x > 0, (name, x)
        comparisons.append({'name': name, 'margin': str(x)})
    def cos_poly(x, degree):
        return sum(((-1)**k*x**(2*k)/factorial(2*k)
                    for k in range(degree//2+1)), F(0))

    positive('exp(5)>100 from positive Taylor terms',
             sum((F(5)**k/factorial(k) for k in range(7)), F(0))-100)
    positive('cos(7/16)>9/10', cos_poly(F(7,16),6)-F(9,10))
    positive('cos(7/8)>5/8', cos_poly(F(7,8),6)-F(5,8))
    positive('cos(3/10)>20/21', cos_poly(F(3,10),6)-F(20,21))
    positive('sqrt(13)>3', F(13)-9)
    positive('sqrt(13)<15/4', F(15,4)**2-13)
    positive('cosh(H)^2>9/4', (F(11)+9)/8-F(9,4))
    positive('cosh(H)^2<49/16', F(49,16)-(F(11)+3*F(15,4))/8)
    positive('cos(17/10)>-1/7', cos_poly(F(17,10),6)+F(1,7))
    positive('cos(7/4)<-1/6', -F(1,6)-cos_poly(F(7,4),8))
    positive('arcsin(1/6)<17/100', F(17,100)-F(17,100)**3/6-F(1,6))
    positive('lower angle bound', F(25,16)+F(1,7)-F(17,10))
    positive('upper angle bound', F(7,4)-F(11,7)-F(17,100))
    positive('attaching second coordinate<3/20', F(3,20)-(F(44,7)-F(51,10))/8)
    first=F(7,16)**2/24*(5+6*F(10,9)+F(8,5))
    second=F(1,2)*F(3,20)**2*F(21,20)
    assert first+second == F(270991,2304000)
    positive('attaching square energy<1/8', F(1,8)-first-second)
    positive('corner exponent<2c', 2*F(8,25)-F(3,25))
    assert F(29,25)-F(1,3)-F(16,25)-F(3,25)==F(1,15)

    exp_half=sum((F(1,2)**k/factorial(k) for k in range(5)), F(0))+F(1,2)**5/factorial(5)/(1-F(1,12))
    positive('exp(1/2)<33/20', F(33,20)-exp_half)
    positive('pi exp(2)<25', F(25)-F(22,7)*F(33,20)**4)
    positive('log(2)<7/10', sum((F(7,10)**k/factorial(k) for k in range(5)),F(0))-2)
    positive('cut-face derivative is negative', F(1,2)-F(22,175))
    positive('dilog(1/2)<3/5', F(3,5)-F(1,2)-F(1,16)-F(1,36))
    positive('top-edge entropy below retained saddle', F(4,15)-F(3,50))
    positive('axis critical entropy below retained saddle',3*F(8,25)-F(7,10))

    algebra=[]
    def zero(name, expression):
        assert sp.simplify(expression)==0,(name,expression)
        algebra.append(name)
    I=sp.I; rt=sp.sqrt(3); X=(1+I*rt)/4
    U=(-1-I*rt)/2; W=sp.simplify(U*U)
    zero('complex stationary ratio',X*(1-W)/(1-X*U)-1)
    diagonal=sp.simplify(2*I*(W/(1-W)-X*U/(1-X*U)))
    off=sp.simplify(2*I*W/(1-W))
    zero('normalized Hessian diagonal',diagonal+rt+I)
    zero('normalized Hessian offdiagonal',off+1/rt+I)
    det=sp.simplify(diagonal**2-off**2)
    zero('normalized Hessian determinant',det-sp.Rational(4,3)*(2+I*rt))
    zero('Fourier coefficient fourth power',16*sp.Rational(8,3)/(det*sp.conjugate(det))-sp.Rational(24,7))
    zero('denominator amplitude', (1-X)*(1-X*U)-sp.Rational(3,4))
    zero('outside numerator phase',X*(1-I*rt)/2-sp.Rational(1,2))

    mp.mp.dps=80
    count=0
    worst=mp.mpf(0)
    def check(name,a,b):
        nonlocal count,worst
        if hasattr(a,'rows'):
            err=mp.norm(a-b)/max(1,mp.norm(a),mp.norm(b))
        else:
            err=abs(a-b)/max(1,abs(a),abs(b))
        assert err<mp.mpf('1e-65'),(name,err)
        count+=1; worst=max(worst,err)

    for N in range(2,13):
        D=N-1; q=mp.exp(mp.pi*1j/N); Q=q*q
        kap=mp.exp(mp.pi*1j*D*D/(2*N))
        S=[mp.mpf(1)]
        for j in range(1,N): S.append(S[-1]*2*mp.sin(mp.pi*j/N))
        M=mp.matrix(N); J=mp.matrix(N)
        for j in range(N):
            J[j,D-j]=1
            for k in range(j+1):
                M[j,k]=kap*(-1)**j*q**(j*(k+1))*S[j]/(S[k]*S[j-k])
        Minv=M**-1; A=J*M**3
        x=mp.mpc('0.173','0.092'); y=mp.mpc('0.217','0.063')
        X=mp.exp(2*mp.pi*1j*x); Y=mp.exp(2*mp.pi*1j*y)
        hx=mp.matrix([mp.sin(mp.pi*N*(x-mp.mpf(j)/N))/(N*mp.sin(mp.pi*(x-mp.mpf(j)/N))) for j in range(N)])
        hy=mp.matrix([mp.sin(mp.pi*N*(y-mp.mpf(j)/N))/(N*mp.sin(mp.pi*(y-mp.mpf(j)/N))) for j in range(N)])
        cx=mp.exp(-mp.pi*1j*D*x)*(1-X**N)/N
        cy=mp.exp(-mp.pi*1j*D*y)*(1-Y**N)/N
        def poch(a,k):
            return mp.fprod(1-a*Q**(-r) for r in range(k))
        for L in range((D//2)+1):
            P=mp.diag([int(j<=L) for j in range(N)])
            E=M.T*P*J*M*P*M
            check(f'similarity {N}/{L}',M*E*Minv,kap*J*Minv*P*J*M*P)
            corner=kap*cx*cy*sum((X**i*Y**j*poch(Q**-1,i+j)/(poch(X,i+1)*poch(Y,j+1))
                                       for i in range(L+1) for j in range(L+1)),mp.mpc(0))
            check(f'original Fourier corner {N}/{L}',(hx.T*E*hy)[0],corner)
            T=A-E
            check(f'noncommutative telescope {N}/{L}',A**3-T**3,A**2*E+A*E*T+E*T**2)
            check(f'corner symmetry {N}/{L}',E,E.T)
        actual_L=N//50
        assert 2*actual_L<=D

    root=Path(__file__).resolve().parents[1]
    proof=root/'notes/research_traced_three_vertex_endpoint.md'
    deps=['notes/research_homogeneous_three_action_calibration.md',
          'notes/research_root_pochhammer_interpolation.md',
          'notes/exact_factorial_interpolation_and_complex_contours.md',
          'notes/research_positive_three_crossing_cycle.md',
          'notes/research_one_crossing_gaussian_window.md',
          'notes/research_radical_path_sector_gap.md',
          'notes/research_edge_cut_energy_comparison.md']
    out=root/'repro/results/research-three-vertex-corner-deletion.json'
    result={'status':'passed','exact_rational_comparisons':len(comparisons),
            'exact_rational_identities':2,'comparisons':comparisons,
            'exact_saddle_identities':len(algebra),'saddle_identities':algebra,
            'finite_diagnostics':count,'decimal_digits':80,'levels':[2,12],
            'worst_relative_error':str(worst),
            'scope':'Scalar proof bounds and literal original matrix/Fourier corner normalization; no inferred large-level asymptotic.',
            'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
            'proof_sha256':sha256(proof.read_bytes()).hexdigest(),
            'dependencies_sha256':{p:sha256((root/p).read_bytes()).hexdigest() for p in deps}}
    out.write_text(json.dumps(result,indent=2)+'\n')
    print(f'Passed {len(comparisons)} rational comparisons, 2 identities, {len(algebra)} saddle identities, {count} original finite diagnostics.\n{out}')

if __name__=='__main__': main()
