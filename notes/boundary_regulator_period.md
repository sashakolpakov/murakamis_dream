# The boundary period line has an exact volume norm

Research note, 25 October 2026. This constructs the continuous boundary
period and its norm directly from the audited symplectic boundary formula.
It is the classical Chern--Simons/regulator framework, not a new quantum
definition. No global theorem identifying a published quantum state is
assumed. The last section states the exact remaining quantum comparison.

Use a nondegenerate one-cusped gluing chart, full peripheral rows with
pairing -2, and the oriented tetrahedral Bloch lift beta. Flat real
shapes other than 0 and 1 are allowed. All logarithms below live on
their matched continuation cover; constants from their branches remain.

## 1. The peripheral line and its invariant norm

On the logarithmic cover of (C^*)^2 use U=Log m, V=Log l. Define a
line by the deck action

    (U,V,p) -> (U+2pi i a,V+2pi i b,exp(bU-aV)p),
    a,b in Z.                                          (1.1)

This is an actual action: composing two multipliers introduces only
exp(2pi i(bc-ad))=1. The form

    A=-(U dV-V dU)/(2pi i)                              (1.2)

transforms to A+d(bU-aV), so d-A defines a connection on the line.
Its curvature form dA is -dU wedge dV/(pi i). On a peripheral
Lagrangian curve, in particular a smooth geometric A-polynomial
branch, its pullback is flat.

Set B(U,V)=Re U Im V-Re V Im U. The norm

    log||p||=log|p|-B(U,V)/(2pi)                         (1.3)

is invariant under (1.1): B changes by
2pi(b Re U-a Re V), precisely the change of log|p| times 2pi.
No choice of a logarithm branch is being hidden in this norm.

## 2. A branch-compatible tetrahedron primitive

For a tetrahedron choose u=Log z and v=Log z'', where z''=1-z^(-1).
Write w=Log(1-z)=u+v+pi i k with a fixed odd integer k on the
chosen logarithmic sheet. Continue Li_2 so that dLi_2(z)=-w du.
Put

    T(z)=Li_2(z)+(1/2)u w+(pi i k/2)u.                 (2.1)

Direct differentiation gives

    dT=(1/2)(u dv-v du).                               (2.2)

The compatible branch of the Bloch--Wigner identity gives exactly

    Im T=D(z)-(1/2)(Re u Im v-Re v Im u).              (2.3)

Indeed D=Im Li_2+Re u Im w; substitute w=u+v+pi i k in (2.1).
The k terms cancel in (2.3). The branch identity for D continues
because its derivative is single valued and its continuation constants
are real: a loop about zero changes u by 2pi i and leaves Li_2 fixed;
a loop about one changes w by 2pi i and Li_2 by -2pi i u.
Their commutators add multiples of (2pi i)^2. Thus (2.3) does not
discard flattening terms by taking an
unmatched principal branch.

## 3. Centering the affine gluing equations

Collect x=(u_j,v_j), with the orientation signs in

    Omega(x,y)=sum_j epsilon_j(u_j y_vj-v_j y_uj).

The logarithmic edge equations are affine with purely imaginary
constants. Choose a purely imaginary vector x_0=i a_0 satisfying
those equations and the chosen complete peripheral logarithms. It need
not be a shape point. Such a vector is obtained by taking the imaginary
part of a complete logarithmic shape point; equivalently one can use
the rational angle reference already constructed in the state notes.
This existence is asserted for a chart with that complete point.

Subtract its peripheral values in defining U,V, so U=V=0 at the
chosen complete lift. Then xi=x-x_0 satisfies the homogeneous edge
equations, xi in E^perp. The audited coisotropic boundary identity is

    Omega(xi,eta)=-(1/2)(U(xi)V(eta)-V(xi)U(eta)),
    xi,eta in E^perp.                                 (3.1)

This is the same pairing calculation that gives
delta beta=-(1/2)m wedge l. Define

    R_X=sum_j epsilon_j T(z_j)-(1/2)Omega(x_0,x)+C,
    C real.                                           (3.2)

Equations (2.2) and (3.1) prove

    dR_X=-(1/4)(U dV-V dU).                            (3.3)

The centering term in (3.2) is necessary because the edge equations
are affine. Applying a homogeneous symplectic formula without it
would lose a branch-dependent linear term.

There is also an exact norm identity. Since Re x is in E^perp,
and Im x-a_0 is in E^perp, (2.3) and (3.1) give

    Im R_X=D(beta)-(1/2)Omega(Re x,Im x-a_0)
          =D(beta)+(1/4)B(U,V).                        (3.4)

No angle positivity, saddle estimate or limit is used here.

Changing the purely imaginary reference within the same affine edge
and complete peripheral constraints changes x_0 by an element of E.
Its pairing with x-x_0 vanishes. The change in R_X is consequently
a real constant, since both references are purely imaginary. Thus
this reference choice affects only the unitary phase of P_X below.

## 4. The regulator is a norm of a parallel period

Define on the logarithmic continuation cover

    P_X=exp(2R_X/(pi i)).                              (4.1)

Equations (3.3)--(3.4) say exactly

    d log P_X=A,
    log||P_X||=2D(beta)/pi.                            (4.2)

At the geometric complete point the last value is 2Vol(W)/pi.
Thus volume is already the norm of a continuous period section.
This identity is uniform on the stated nondegenerate gluing charts.

Two compatible chart presentations of the same marked Bloch lift
have the same boundary connection and norm. Their parallel sections
therefore differ by a constant of absolute value one on a connected
overlap. Under a logarithmic deck change the comparison with the
multiplier in (1.1) can likewise retain a constant unitary character.
This records a flat phase twist of the pullback line. The calculation
does not silently trivialize it or identify it with a particular
published Chern--Simons phase. That identification requires the global
lift and phase calibration, alongside the finite scalar data of
`equivariant_roots_and_phase_descent.md`.

The exact five-term invariance of D(beta) already proved in the Bloch
note makes the norm in (4.2) independent of its tetrahedral presentation.
Its complex phase contains the additional period datum. The boundary
symbol alone does not fix the value of that section.

The action (1.1) and connection (1.2) have the same ordered-coordinate
form as the classical line described in Baseilhac--Benedetti,
[Analytic families of quantum hyperbolic invariants](https://arxiv.org/abs/1212.4261v3),
Section 4.4, equations (56)--(57). Their ordered coordinates are
(lambda,mu)=(longitude,meridian), whereas ours were (m,l). Exchanging
the ordered coordinates dualizes this line. A literal comparison must
therefore retain the peripheral orientation/inversion convention as well
as the phase calibration. The connection and volume norm above were
derived from the local primitive and coisotropic reduction, without
assuming that source's global identification theorem or a same-order
identification of its marked line with ours.

## 5. The remaining quantum comparison is now a precise norm statement

Let J_n be the prescribed, fully normalized literature meridian state
at b^2=1/n, evaluated at the complete peripheral point. The conventions
in the state notes give h_n=n/(n+1)^2, not 1/n. The requested volume law

    -2pi h_n log|J_n| -> Vol(W)

is exactly equivalent to

    4h_n log|J_n|+log||P_hyp|| -> 0.                   (5.1)

The equality log||P_hyp||=2Vol(W)/pi proves this equivalence with all
constants fixed. Establishing (5.1) is still a quantum theorem. It
requires identifying the selected global period/cycle and controlling
its comparison across levels; no finite-level phase normalization
proves it. In the actual Faddeev chart the finite central character
is t_n=exp((n+1)y), as independently derived in the rational bridge.
The map of parameters must therefore remain part of this comparison.

The work here supplies the exact classical target and its norm. It
does not replace the all-alternating goal by a theorem about the
existence of that target, or assert an unproved quantum comparison.

The subsequent `rational_period_pushforward.md` constructs an exact
folded period for the specified source realization and identifies its
local gluing/regulator summands with all measures retained. It also
shows why boundary specialization can preserve a residue even when
the open special gluing fiber has lost its point. Transport and
localization of that cycle, followed by (5.1), remain necessary.
