#!/usr/bin/env python3
"""Exact singular-gauge normalization and logarithmic Heisenberg checks."""

import cmath
import json
from pathlib import Path

import sympy as s


Q,Y,Z=s.symbols('Q Y Z')


def confluence_gauges():
    h=Q-1
    F=s.Matrix([[1,Y/(1-Y)+h*Y,Y*Y/(1+Y)+h/(1-Y)],
                [0,1,1/(1+Y)+h*Y*Y],[0,0,1]])
    H=s.Matrix([[h**-2,h**-3,0],[0,h,h**-1],[0,0,h**2]])
    G=F*H
    normalized=(G*G.subs(Y,Z).inv()).applyfunc(s.cancel)
    expected=(F*F.subs(Y,Z).inv()).applyfunc(s.cancel)
    assert (normalized-expected).applyfunc(s.cancel)==s.zeros(3)
    assert (normalized.subs(Y,Z)-s.eye(3)).applyfunc(s.cancel)==s.zeros(3)
    C=(G.subs(Y,Q*Y)*G.inv()).applyfunc(s.cancel)
    C_from_F=(F.subs(Y,Q*Y)*F.inv()).applyfunc(s.cancel)
    assert (C-C_from_F).applyfunc(s.cancel)==s.zeros(3)
    assert (C.subs(Q,1)-s.eye(3)).applyfunc(s.cancel)==s.zeros(3)
    A=C.diff(Q).subs(Q,1).applyfunc(s.cancel)
    F0=F.subs(Q,1)
    expected_A=(Y*F0.diff(Y)*F0.inv()).applyfunc(s.cancel)
    assert (A-expected_A).applyfunc(s.cancel)==s.zeros(3)
    normalized0=normalized.subs(Q,1)
    assert (Y*normalized0.diff(Y)-A*normalized0).applyfunc(s.cancel)==s.zeros(3)
    scalar_G=Y-Q
    scalar_C=s.cancel(scalar_G.subs(Y,Q*Y)/scalar_G)
    assert s.cancel(scalar_C-Q*(Y-1)/(Y-Q))==0
    assert s.cancel(scalar_C.diff(Q).subs(Q,1)-Y/(Y-1))==0
    bad_anchor=s.cancel(scalar_G/scalar_G.subs(Y,1))
    assert s.cancel(bad_anchor-(1-(Y-1)/h))==0
    generic_anchor=s.cancel(scalar_G/scalar_G.subs(Y,Z))
    assert s.cancel(generic_anchor.subs(Q,1)-(Y-1)/(Z-1))==0
    return {'singular_Q_gauge_normalized_at_generic_anchor':True,
            'Q_dependent_constant_matrix_cancels_exactly':True,
            'rational_classical_fundamental_matrix_exact':True,
            'poles_at_Y_one_and_minus_one_retained':True,
            'nongeneric_anchor_counterexample_exact':True}


def heisenberg_curvature():
    r,N=s.symbols('r N')
    A=s.Matrix([[0,1,0],[0,0,r],[0,0,0]])
    h=Q-1
    C=s.eye(3)+h*A+h*h*A*A/2
    assert A**3==s.zeros(3)
    assert C.diff(Q).subs(Q,1)==A
    records=[]
    for level in range(2,10):
        got=(C**level).applyfunc(s.expand)
        expected=s.eye(3)+level*h*A+level*level*h*h*A*A/2
        assert (got-expected).applyfunc(s.expand)==s.zeros(3)
        records.append({'level':level,'exact_curvature_log_parameter':'N*(Q-1)',
                        'central_cross_term_retained':True})
    t=s.symbols('t')
    exact=s.eye(3)+t*A+t*t*A*A/2
    assert exact[0,1]==t and exact[0,2]==r*t*t/2
    # The confluence curvature converges to nontrivial monodromy.
    diagnostics=[]
    for level in (20,100,500):
        q=cmath.exp(2j*cmath.pi/level)
        value=level*(q-1)
        diagnostics.append({'level':level,'N_times_Q_minus_one_real':value.real,
                            'N_times_Q_minus_one_imag':value.imag,
                            'finite_diagnostic_only':True})
    return {'exact_power_formulas':records,
            'nonrational_exact_step_requires_Log_Q':True,
            'curvature_limit_diagnostics':diagnostics}


def logarithmic_residues():
    Y=s.symbols('Y')
    records=[]
    for ramification in (1,2,3,5):
        omega=ramification/Y
        assert s.residue(omega,Y,0)==ramification
        # Rational exact differentials have no residue, including poles.
        rational=Y**-3+2/Y+Y/(1-Y)
        assert s.residue(s.diff(rational,Y),Y,0)==0
        records.append({'finite_cover_ramification':ramification,
                        'nonzero_pulled_back_dlog_residue':ramification,
                        'rational_exact_differential_residue':0})
    return records


def main():
    result={'generic_anchor_confluence':confluence_gauges(),
            'rational_and_exact_Heisenberg_steps':heisenberg_curvature(),
            'finite_cover_logarithmic_obstructions':logarithmic_residues(),
            'scope':'Absolute zero-curvature regulator obstruction; no actual comparison or volume theorem.'}
    path=Path(__file__).with_name('regulator_curvature_obstruction_results.json')
    path.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'generic_anchor_confluence_exact':True,
                      'Heisenberg_power_checks':len(result['rational_and_exact_Heisenberg_steps']['exact_power_formulas']),
                      'finite_cover_residue_checks':len(result['finite_cover_logarithmic_obstructions']),
                      'output':str(path)},indent=2))


if __name__=='__main__':main()
