# A common period space for the Frobenius mark and Bloch regulator

Research note, 26 October 2026. This constructs an explicit algebraic
connection space containing the previously separate Frobenius/Tate
normalization and marked Bloch action. Its integral Heisenberg action
retains the actual root phases. It also proves that adjoining the
rational Frobenius coordinate cannot erase an existing source class.

This is a geometric comparison target, not a new quantum invariant or
an identification of the actual Kashaev period. The selected quantum
source and cut still have to be transported to this target. The volume
conjecture remains unproved.

## 1. The logarithmic connection space

Use the normalized marked geometric A-curve C of
[the primary formulation](a_polynomial_torsor_status.md). On its chosen
augmented chart write m=M^2 and l=L_intr^2. All complete-point shifts
and SL(2) lift characters remain those recorded in
[the action calculation](quantum_longitude_and_regulator_action.md).
The variables U,V below are the centered logarithms of m,l; in
particular U=V=0 at the chosen complete lift.

Put tau=pi*i, and use h=Log q, not Log(q^2). On C times G_m,q
write omega_m=dm/m, omega_l=dl/l, omega_q=dq/q. Over this base
take an additive coordinate h and a Heisenberg frame

    Pi=[1 U H;0 1 V;0 0 1].

The horizontal equations are algebraic:

    dh=omega_q, dU=omega_m, dV=omega_l,
    dH=U omega_l.                                  (1.1)

They are integrable. The first three forms are closed, and the
only remaining obstruction is omega_m wedge omega_l=0 on C.
Equivalently dPi=Pi Omega with Omega_12=omega_m,
Omega_23=omega_l and the other entries zero. An initial marked
frame determines its local horizontal continuation. The fundamental
Bloch lift fixes its central period, as already recorded by

    R=UV/4-H/2, dR=-(U dV-V dU)/4.                 (1.2)

The preferred-longitude action is therefore the following algebraic
coordinate on this connection space:

    S=R+UV/4=(UV-H)/2, dS=(V/2)dU.                (1.3)

Indeed adding (1.2) to the differential of UV/4 gives
the displayed identity. The original longitude lift must still
be retained. Write u=Log M and Log L_intr=kappa*tau+V/2, where
kappa is the specified integer at completeness. With the same
complete action constant, the uncentered preferred action is

    S_lift=S+kappa*tau*U, dS_lift=2 Log(L_intr)du. (1.4)

Its exponential is W^kappa Z in Section 2. This is the full
peripheral character, not a discarded sign. At completeness W=1.
Compatible real constant phases remain marked; they have no volume
norm along the prescribed imaginary h direction.

The coordinates h,U,V,H are algebraic coordinates of the connection
space. Their specified horizontal values are periods, not algebraic
functions of q,m,l. No finite algebraic cover is claimed to supply
those horizontal values.

## 2. Three standard exponential connections

On h!=0 consider the rational functions

    f_J=tau^2/(2h),
    f_W=tau U/(2h),
    f_Z=S/(2h)=(UV-H)/(4h).                       (2.1)

For each f use the rank-one exponential connection d-df, whose
normalized horizontal period is exp(f). This is the standard
exponential-connection construction, with its sign specified.
Let J,W,Z denote these three periods. Restricting their equations
to the horizontal distribution (1.1) gives

    dlog J=-tau^2 omega_q/(2h^2),
    dlog W=tau omega_m/(2h)-tau U omega_q/(2h^2),
    dlog Z=V omega_m/(4h)-S omega_q/(2h^2).        (2.2)

These equations are flat: on the full connection space their forms
are the exact differentials df_J,df_W,df_Z; restriction to an
integrable horizontal distribution preserves flatness. Thus no
classification or pushforward theorem is needed here.

At the prescribed literature roots h_N=tau/N, with U=2 Log M,

    J_N=i^N, W_N=M^N,
    Z_N=exp(N S/(2tau)).                          (2.3)

The Frobenius meridian is precisely W. All the earlier phases are
values of the same specified Tate period:

    zeta_N=i/J_N=i^(1-N),
    epsilon_N=J_N^2=(-1)^N,
    eta_N=-i J_N=i^(N+3)=zeta_N^3.               (2.4)

There are no level-dependent arbitrary phase choices. For fixed h,
the meridian step U->U+2h sends W to exp(tau)W=-W. This recovers
the original half-Frobenius sign. It does not assert that finite
meridian transport of Z is already the actual quantum-A operator;
Z is the marked action line to which the quantum normal block
must be compared.

These formulas specify an explicit Tate exponential lift of the
known root phases. Their agreement at roots alone does not prove
that the actual full quantum state has the q-direction connection
in (2.2).

C here is the commutative geometric A-curve used for the classical
action. These root restrictions do not identify its coordinates
with the root-central spectral coordinates of an actual quantum
operator. The distinction in
[the bridge, Section 4](triangulation_regulator_bridge.md#4-keep-central-and-semiclassical-shapes-distinct)
remains in force.

## 3. The integral Heisenberg action lifts by actual monomials

On the marked logarithmic cover consider the standard integral
Heisenberg transformations indexed by integers A,B,C_0:

    U'=U+2tau A, V'=V+2tau B,
    H'=H+2tau A V+4tau^2 C_0.                   (3.1)

They preserve (1.1). Direct substitution into (2.1) gives

    J'=J,
    W'=J^(2A) W,
    Z'=J^(2(AB-C_0)) W^B Z.                    (3.2)

The exponential changes have become algebraic monomials in the
retained period coordinates. To check composition, applying g_1
then g_2 gives

    A=A_1+A_2, B=B_1+B_2,
    C_0=C_1+C_2+A_2 B_1.

The exponent of J in the product of (3.2) is exactly 2(AB-C_0).
This proves the full central composition law, not only equality
of determinants or absolute values.

For P=exp(2R/tau), (1.2) gives

    P'=exp(B U-A V)P.                            (3.3)

The extra exponential is exp(2tau(AB-2C_0))=1, using integrality.
Thus the lift recovers the regulator line's existing deck action.
At a root, the central factor J^(2(AB-C_0)) is the retained
phase (-1)^(N(AB-C_0)); the other factor is M^(NB).

This is covariance for the displayed integral lattice on the
marked continuation cover. It does not assert that every monodromy
constant of an arbitrary unipotent connection is a Tate period.
Any further flattening cover or central mark must be transported,
not silently identified with this lattice. The fixed fundamental
Bloch lift is still the datum selecting H's central value.
The displayed lattice acts on the peripheral period charts.
Its subgroup preserving specified square-root eigenvalue lifts
may be smaller; no action of every integer triple on a single
fixed SL(2) augmented component is assumed.

## 4. Its root norm is exactly the marked regulator norm

Let b(U,V)=Re U Im V-Re V Im U. The existing regulator norm is

    log||P||=(2/pi)Im R-b(U,V)/(2pi)
             =2D(beta)/pi.                       (4.1)

Before taking norms, the marked logarithm gives exactly

    Z_N=exp((N/4)Log P+N UV/(8tau)),
    Log P=2R/tau.

Thus no fractional power of an unmarked scalar P has been chosen.

At h=tau/N define the action-line norm by

    log||Z_N||=log|Z_N|-N Re U Im V/(4pi).

Since Im S=Im R+(Re U Im V+Re V Im U)/4, substitution proves
the exact identity

    log||Z_N||=(N/4)log||P||=N D(beta)/(2pi).      (4.2)

It is invariant under (3.1)--(3.2). J_N has modulus one;
the change B log|W_N|=NB Re U/2 in log|Z_N| is canceled by
the change in the boundary correction. At U=V=0 no correction
is needed. For the marked complete geometric period,

    (2pi/N)log|Z_N|=Vol(S^3 minus K).             (4.3)

This is an exact evaluation of the constructed geometric action
period. It is not an identity for F_N(1). Replacing Z_N by the
actual Kashaev value in (4.3) is precisely the missing comparison,
including its full amplitude and selected source coupling.

## 5. What the meridian blowup resolves, and what it retains

On the identity chart of
[the uniform source base](uniform_frobenius_source_base.md),

    s=sinh(U/2)/sinh h,
    U=2 arsinh(s sinh h).

Then W is exactly the previously constructed period

    W=exp((tau/h)arsinh(s sinh h)).               (5.1)

It is regular and even in h near h=0 for bounded s, and its
exceptional value is exp(tau*s). The cap slope remains
(dW/ds)_(s=0)=tau sinh h/h, with its marked limit tau.

The full joint period space also retains J. It is irregular at
h=0, although every J_N has modulus one. The finite phase cover
J^4=1 is valid on the prescribed root fibers; it is not invariant
under the q-direction connection in (2.2):

    d(J^4)=-2tau^2 J^4 dh/h^2.

Consequently freezing a residue-class phase, as in the meridian
difference base, does not construct its joint q-direction period
connection. There is no contradiction with the fixed-sheet parity
statements of the preceding note, which concern meridian source
coefficients on that sheet.

The root graphs are therefore not Zariski dense in this enlarged
Tate space: J^4-1 vanishes on all of them. The earlier density
theorem applies on the specified finite phase components of the
meridian difference base. It cannot reconstruct the q-direction
connection from root evaluations. In particular (2.2) is a
specified period lift, rather than a unique interpolation theorem
for the full quantum state.

The actual complete cap has a joint lift on this space:

    d_cap(h)=-i J(h) h/tau,
    dlog d_cap=(1/h-tau^2/(2h^2))dh.              (5.2)

At h_N=tau/N it is exactly eta_N/N, with modulus 1/N. The
previous fixed-phase regular cap is the h factor after its
specified Tate line is recorded. Formula (5.2) retains that
line, including the even-level sign.

Fixed rational Tate constants in an action are also retained
by finite root lines of J. For example, Li_2(1)=pi^2/6 gives
exp(Li_2(1)/(2h))=J^(-1/6) on its marked cover. Such a factor
has modulus one at the prescribed roots. This observation does
not control an unknown full quantum amplitude.

The geometric action line retains an additional irregular factor.
At the complete hyperbolic point, Im S_0=Vol(M)>0, so the term
S_0/(2h) cannot be removed by the meridian blowup. This is the
period carrying volume. It remains part of the marked exponential
connection, rather than becoming a regular algebraic function
after the Frobenius normalization has been resolved.

## 6. Rational Frobenius base change preserves source classes

Let (F,sigma) be a characteristic-zero difference field and let
C in GL_d(F). Adjoin
an independent w with sigma(w)=-w and put E=F(w). The Laurent
constant-coefficient map at w=0,

    r:E->F, r(t)=[w^0]t,

is F-linear, is the identity on F, and commutes with sigma.
This is a coefficient extraction, not evaluation of a possibly
polar rational function at zero. Existence of the Laurent
expansion over F gives all three assertions. Hence

    r((sigma-C)t)=(sigma-C)r(t).

It induces a left inverse on the additive source quotients:

    F^d/(sigma-C)F^d -> E^d/(sigma-C)E^d.         (6.1)

In particular (6.1) is injective. The same argument works for
sigma(w)=chi*w, chi in F^*, and for finitely many independent
diagonally shifted variables, by iterated Laurent extraction.
A further finite sigma-stable algebraic cover does not change
the conclusion, by normalized trace as in
[the affine-source proof](affine_quantum_a_period.md#2-finite-algebraic-covers-do-not-kill-a-nonzero-affine-class).

Thus a nonsplit source already defined over C(q,M) remains
nonsplit on the rational Frobenius base, including on each
specified phase component and after finite stable covers.
Principalizing its meridian lattice does not furnish a horizontal
splitting. This statement does not say that two specified
nonsplit extensions cannot be compared; their class difference
is the actual comparison to compute.

The hypothesis that C and the source descend to F matters. This
does not by itself classify source matrices that genuinely
depend on w, or compare an unknown homogeneous gauge over E.
Nor does it apply to unrestricted completed or analytic period
extensions such as the logarithmic/exponential construction above.

## 7. A degree obstruction to compressing a nonsplit root period

Assume F=K(q,M), with K a fixed number field, and a specified
nonsplit equation sigma(v)=Cv+c over F. Write C=A_0/D and
c=b_0/D with Laurent-polynomial coefficients. Suppose a proposed
root-level rational section has a presentation v=a/B in K(q,M,w)^d.
Its cleared residual is

    R=D sigma(a) B-A_0 a sigma(B)-b_0 B sigma(B).   (7.1)

Some component of R is nonzero: otherwise (6.1) would produce
a generic rational splitting. If v is an exact solution on
the whole graph q=q_N,w=M^N, that component vanishes on the
graph. The [root-graph rigidity theorem](uniform_frobenius_source_base.md#2-root-graphs-give-a-genuine-algebraic-rigidity-test)
therefore implies

    D_M(R)>=N or [K:Q] D_q(R)>=phi(2N),          (7.2)

where D_M is the M exponent span and D_q is the q exponent
span after a Laurent monomial is cleared. All denominators
must be defined as rational whole graphs. The coefficient field
must remain fixed; allowing arbitrary cyclotomic coefficients
changes the stated field-degree bound.

For example, if the fixed operator data have absolute M and q
exponents bounded by c_M,c_q, and a,B have exponents bounded
by d_M,d_q, (7.1) has

    D_M(R)<=2c_M+4d_M,
    D_q(R)<=2c_q+4d_q+2d_M.                      (7.3)

The last term records sigma(M^j)=q^j M^j. No bound on the w
degree is needed for the exponent-separation argument. Thus
a fixed bounded rational presentation of a nonsplit period
cannot recover every large root level merely by adjoining w.

This applies to an actual knot source only after its specified
generic source and nonsplitting hypotheses have been proved.
The adequacy note supplies such a nonsplitting consequence
under its explicitly stated actual-source hypotheses; it does
not construct that source for every knot. A bounded comparison
between two transcendental periods is not excluded by (7.2):
the periods can be complicated while their intertwiner is simple.

## 8. A normalization criterion on this common space

There is a direct extension of
[the fixed central normalization theorem](algebraic_central_normalization.md).
Let a comparison factor have a fixed finite algebraic presentation
over C(q,t,M,W,J), restricted by

    q=exp(tau/N), t=1/N, W=M^N, J=i^N.

If its chosen whole M=1 value r_N is finite and nonzero, then
log|r_N|=O(log N). Indeed J takes only four values. On each
phase sheet the previous theorem applies; taking the maximum
of the four bounds proves the assertion. Fixed finite roots
of J have only finitely many values as well. Poles or zeros
common to an entire phase must first be canceled on that
restricted algebraic branch, as in the previous whole-germ
theorem; an undefined restriction is not an evaluation.

Consequently an actual exact comparison F_N(1)=r_N Z_N(complete)
of this specified kind would prove the volume conjecture, with
error O(log N/N). This is a sufficient comparison criterion,
not a hypothesis being asserted for the actual period. A formal
unit in h need not have such a finite algebraic presentation
or control its selected root realization. Nor does the criterion
permit discarding other period components or their cancellations.

## 9. Scope, existing coverage, and verification

The positive ideal triangulation supplies beta, its central H
mark, and the geometric A-curve used in Section 1. The construction
then places its regulator action, the actual half-Frobenius mark,
and the root phases in one explicit exponential-connection space.
The source-class lemma prevents confusing this larger coefficient
space with a splitting of the actual quantum source.

The subsequent [controlled cyclic Euler source](controlled_cyclic_euler_source.md)
now supplies a specific local comparison with uniform control.
The literature cyclic coefficient vector is an explicit reflected
factorial source vector, with its full inhomogeneous equation and
co-source retained. Its scalar has a direct norm-product formula
and polynomial bounds despite growing algebraic degree. This is
one actual local source comparison, not the full source-to-Z map
or a proof of its selected geometric coupling.

What remains is the actual source-compatible map, with its cut,
lattice transitions, quantum amplitude and selected relative period.
No geometric factor of a minimal actual operator or nonzero
geometric coupling of the selected finite sum is inferred here.

Polylogarithmic period connections and Bloch regulators have
existing coverage in [Hain, Classical Polylogarithms](https://arxiv.org/abs/alg-geom/9202022).
Exponential connections and rescaled twists have existing coverage
in [Sabbah--Yu, 1406.1339](https://arxiv.org/abs/1406.1339).
Only scope and the standard exponential-connection definition
are used; no Hodge, strictness, pushforward or comparison theorem
from these works is a proof premise. The proofs here are the
displayed differentiation, monomial and coefficient calculations.
No novelty is claimed for the Heisenberg connection, exponential
twists, coefficient descent or elementary cyclotomic degree bound.

[The exact audit](../experiments/audit_common_regulator_period_space.py)
checks the action differential, all three connection forms,
the noncommutative integral deck composition, phase identifications,
the invariant root norm, and source-class retraction with moving
and polar denominators. A non-knot root example checks that an
exact levelwise splitting can fail the generic source equation.
[Results](../experiments/common_regulator_period_space_results.json).

Reproduce with:

    python3 experiments/audit_common_regulator_period_space.py
