"""Checks of the marked Gauss-wall period and actual polar character.

These supplement the proofs in gauss_wall_flux_and_actual_peripheral_character.md;
they do not test a selected regular-sector volume estimate.
"""

from __future__ import annotations

import json
from pathlib import Path

import mpmath as mp
import sympy as sp


def rational_forms():
    v,a,eta=sp.symbols('v a eta',nonzero=True)
    F=1-eta*v
    B=(1-2*v*a)/(2*F)
    assert sp.simplify(sp.diff(B,a)+v/F)==0
    V,ap,etap=1/v,v-v*v*a,-v*v*eta
    Bs=(2*V*ap-1)/(2*(1+etap*V))
    assert sp.simplify(Bs-B)==0
    # Res_D B=(a-1/(2v))dv; its exterior derivative is -Omega.
    assert sp.diff(a-1/(2*v),a)==1
    c=2*sp.pi*sp.I
    etaphys=(1-sp.exp(-c*v*a))/v
    assert sp.simplify(sp.diff(etaphys,a)/(1-v*etaphys)-c)==0
    T,l=sp.symbols('T l',real=True)
    Fl=(1-l)+l*sp.exp(-c*T)
    assert sp.simplify(Fl.subs({l:sp.Rational(1,2),T:sp.Rational(1,2)}))==0
    assert sp.simplify(sp.diff(Fl,l).subs({l:sp.Rational(1,2),T:sp.Rational(1,2)})+2)==0
    assert sp.simplify(sp.diff(Fl,T).subs({l:sp.Rational(1,2),T:sp.Rational(1,2)})-sp.pi*sp.I)==0
    H=sp.symbols('H',nonzero=True)
    for N in range(2,15):
        assert sp.simplify((2*c*c/H**2).subs(H,c/N)-2*N*N)==0
    return {'global_rational_adapter_primitive':True,
            'south_clutch_and_D_residue_sign':True,
            'physical_Gauss_flux_and_wall_intersection':True,
            'marked_deck_first_quantum_jet':True}


def whole_periods():
    mp.mp.dps=85
    c=2j*mp.pi
    def chord(T):
        return -c*T if T<mp.mpf('0.5') else c*(1-T)
    ordinary=-c*mp.quad(chord,[0,mp.mpf('0.5'),1])
    marked=-c*mp.quad(lambda T:-c*T,[0,1])
    assert abs(ordinary)<mp.mpf('1e-70')
    assert abs(marked-c*c/2)<mp.mpf('1e-70')
    u=mp.mpc('0.13','0.17')
    for H in (mp.mpc('0.41','0.73'),mp.mpc('0.08','0.29')):
        chi=lambda uu:mp.exp(-2*c*uu/H)
        half=lambda uu:mp.exp(-c*uu/H)
        assert abs(chi(u+H/2)/chi(u)-1)<mp.mpf('1e-70')
        assert abs(half(u+H/2)/half(u)+1)<mp.mpf('1e-70')
    return {'ordinary_radial_difference_period':mp.nstr(ordinary,8),
            'marked_relative_difference_period':mp.nstr(marked,24),
            'generic_half_step_character_and_sign':True}


def actual_root_factors():
    mp.mp.dps=85
    c=2j*mp.pi
    u=mp.mpc('0.13','0.17')
    M=mp.exp(u)
    cases=[]
    total_residues=0
    for N in range(2,15):
        H=c/N
        q=mp.exp(H/2)
        phase=(1j)**(N+3)
        kappa=lambda m:m-1/m
        actual=lambda m:phase*kappa(m)/(m**N-m**(-N))
        chi=mp.exp(-2*c*u/H)
        half=mp.exp(-c*u/H)
        factor=phase*kappa(M)*half/(1-chi)
        assert abs(factor-actual(M))<mp.mpf('1e-70')
        assert abs(chi-M**(-2*N))<mp.mpf('1e-70')
        assert abs(actual(q*M)/actual(M)+kappa(q*M)/kappa(M))<mp.mpf('1e-70')
        assert abs(actual(1/M)-actual(M))<mp.mpf('1e-70')
        assert abs(mp.exp((c*c/2)/H)-(-1)**N)<mp.mpf('1e-70')
        # Cauchy extraction checks the genuine polar scalar and its phase.
        contour_points=64
        radius=mp.mpf(1)/(8*N)
        residue_norm=mp.mpf(0)
        max_error=mp.mpf(0)
        for k in range(1,N):
            center=mp.mpf(k)/N
            expected=phase*(-1)**k*mp.sin(mp.pi*k/N)/(mp.pi*N)
            value=mp.mpc(0)
            for j in range(contour_points):
                e=mp.exp(c*j/contour_points)
                z=center+radius*e
                f=phase*mp.sin(mp.pi*z)/mp.sin(mp.pi*N*z)
                value+=radius*e*f/contour_points
            error=abs(value-expected)
            assert error<mp.mpf('1e-50'),(N,k,error)
            max_error=max(max_error,error)
            residue_norm+=2*mp.pi*abs(expected)
            total_residues+=1
        assert residue_norm<=2
        cases.append({'level':N,'Frobenius_flux_and_full_factor':True,
                      'retained_half_step_and_inverse_characters':True,
                      'marked_radial_phase':(-1)**N,
                      'wall_residues_checked':N-1,
                      'max_Cauchy_residue_error':mp.nstr(max_error,6),
                      'unit_color_total_indentation_budget':float(residue_norm)})
    return {'cases':cases,'residue_count':total_residues}


def main():
    result={'rational_geometry':rational_forms(),'whole_marked_period':whole_periods(),
            'actual_root_source':actual_root_factors(),
            'scope':'Marked geometric flux and actual polar adapter; no regular-sector norm claim.'}
    Path(__file__).with_name('gauss_wall_peripheral_character_results.json').write_text(
        json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
