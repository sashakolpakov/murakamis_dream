# Unfolding the actual Ward jets gives a marked dilogarithm period

Research proof, 27 October 2026. A product-preserving fixed-N
formalization with reduced scalar symbols is obstructed under the
regularity hypotheses of
[the fixed-root audit](fixed_root_formal_ward_obstruction.md).
Their coherent all-level factorial jets do admit an unfolding. This
note constructs it and identifies its cyclotomic pole, regular part,
norm-root gauge, and local Heisenberg regulator by direct formulas.

This is a theorem about the literal Ward factorial block. It does
not identify the selected full knot contraction with a geometric
period, or prove the volume conjecture. No published asymptotic or
quantum-dilogarithm theorem is a premise of the proof.

## 1. The actual jets and a faithful all-level unfolding

Let Q_N=exp(2pi*i/N), N>=2. The actual nilpotent Ward block has
the finite factorial gauge

    f_N(z)=sum_(j=0)^(N-1) z^j/(Q_N;Q_N)_j,

with z=-t e and e^N=0. Every denominator in this formula is nonzero.
Its constant term is one. The literal relation is

    f_N(Q_N z)=(1-z)f_N(z) mod z^N.               (1)

Consider a proposed unfolding F(Q,z)=sum_j c_j(Q)z^j with each
c_j rational in Q and regular at Q_N for all sufficiently large N.
If its restrictions modulo z^N give these actual jets at every
sufficiently large level, then necessarily

    c_j(Q)=1/(Q;Q)_j.                            (2)

Indeed fix j and use every N>j outside the finite exceptional set.
The rational function c_j(Q)-1/(Q;Q)_j vanishes at infinitely many
distinct Q_N, so is zero. Existence is the displayed series

    F(Q,z)=sum_(j>=0) z^j/(Q;Q)_j.                (3)

Thus all-level rational coefficient data, rather than a chosen
levelwise continuation, determine one formal function. No bound
on the degrees of c_j as j grows was assumed. The same argument
works for any specified family of nilpotent jets with such a
rational coefficient unfolding; it proves uniqueness, not existence
for an arbitrary family or for an unspecified whole knot period.

Coefficient comparison gives the exact equation and normalization

    F(Q,Qz)=(1-z)F(Q,z), F(Q,0)=1.               (4)

Over Q(Q)[[z]], these conditions also determine F uniquely. For
|Q|<1 it agrees with the ordinary convergent quantum factorial

    F(Q,z)=1/(z;Q)_infinity

near z=0. This analytic statement follows directly by iterating
(4), or from the coefficient identity below; it is not used to
justify a root specialization of the infinite product.

The nilpotent jets in (1) do not on their own define a value of
F at a root for nonnilpotent z. The cyclotomic pole must first
be retained. The rational coefficient hypothesis excludes arbitrary
unrelated periodic factors at different levels; it is not a claim
that any transseries or multivalued modular completion is thereby
fixed without additional markings.

## 2. The formal logarithm and its exact cyclotomic pole

Take the z-adic logarithm, with constant term zero. Equation (4)
gives directly

    log F(Q,z)=sum_(m>=1) z^m/[m(1-Q^m)].         (5)

There is no convergence assumption in (5). For fixed m it is a
rational identity in Q. Fix a primitive root zeta of order N and
write Q=zeta exp(h). The expansion is coefficientwise in z, with
one possible h^(-1) term. Put X=z^N. Terms m not divisible by N
are regular in h. For m=kN,

    1/(1-exp(kN h))=-1/(kN h)+1/2+O(h).

Consequently the polar coefficient is exactly

    A_(-1)(X)=[h^(-1)]log F=-Li_2(X)/N^2.        (6)

Here Li_2(X)=sum_(k>=1)X^k/k^2 is first a formal power series.
On a marked punctured curve it has its usual analytic continuation
fixed from this germ. Formula (6) is a coefficient evaluation,
not a limiting assertion about a selected knot sequence.

This gives a useful logarithmic-coordinate interpretation. Passing
to the N-th cyclotomic resonance retains the terms with indices
divisible by N. Their denominators supply a second factor kN,
so the resonant logarithm coefficient is a dilogarithm. Keeping
only a bare nilpotent special fiber would miss exactly this term.

## 3. The regular part is the marked cyclic dilogarithm

Define, with the z=0 branch fixed,

    D_N(z)=product_(j=1)^(N-1)(1-zeta^j z)^(j/N).

Its formal logarithm is well defined. The elementary weighted
root sum is

    sum_(j=1)^(N-1) j zeta^(jm)
       =N/(zeta^m-1) for N not dividing m,
       =N(N-1)/2 for N dividing m.

For the first equality, differentiate the finite geometric sum
and evaluate at the nontrivial N-th root zeta^m. This identity
and (5) give the entire constant coefficient:

    [h^0]log F=log D_N(z)-(1/2)Log(1-X).         (7)

Indeed the nonresonant terms give log D_N minus its resonant
part, and the resonant constant term is Li_1(X)/(2N). Combining
them gives precisely (7), with its sign and factor one half.

In a formal exponential line the first two coefficients are
therefore

    F(zeta exp(h),z)
      =exp(-Li_2(X)/(N^2 h))
           D_N(z)(1-X)^(-1/2)(1+O(h)).           (8)

Equation (8) is a coefficientwise formal statement in z and h.
It is not a uniform rootwise asymptotic estimate or a permission
to evaluate a divergent infinite product first. All logarithmic
and square-root branches are continued from z=0 together.

## 4. Identification with the actual normalized norm-root gauge

Use the actual cyclic Ward order near M=1,

    kappa=M-M^(-1), kappa_N=M^N-M^(-N),
    A_N=R[e]/(e^N-(-1)^(N+1)kappa_N),
    sigma(e)=zeta e, z=-t e.

Then X=z^N=-kappa_N t^N, and the full determinant character is

    1-X=1+kappa_Nt^N=Norm(1+t e).                (9)

Mark nu=(1-X)^(1/N) by nu=1 at the nilpotent fiber. The cyclic
product satisfies the exact transport and norm identities

    D_N(zeta z)/D_N(z)=(1-z)/nu,
    Norm D_N(z)=nu^(N(N-1)/2).                  (10)

The first follows by subtracting its two logarithms using the
weighted root sum; the second follows by multiplying all its
deck translates. Both identities hold on the common marked root
cover, not with independent fractional powers chosen per factor.

Define

    g_D=D_N(z)/nu^((N-1)/2).                    (11)

It has Norm g_D=1 and sigma g_D=((1+t e)/nu)g_D.
At kappa=0 it has constant coefficient one and reduces exactly
to the actual finite factorial gauge f_N(-t e): equation (1)
determines that nilpotent unit coefficient by coefficient.

The [norm-root transfer theorem](cyclic_ward_norm_root_period.md)
constructs a meridian-regular norm-one gauge with precisely these
properties. Their ratio is sigma invariant, hence scalar in R;
its N-th power is one and its identity mark is one. Thus the
two gauges agree exactly on the completed marked cover. This
identifies the actual normalized Ward gauge with the defined
cyclic dilogarithm, rather than only comparing their norms.

For even N the half power in (11) has its identity square-root
mark. The disconnected phase sheets are retained, not equated.
Formula (7) may now be written particularly simply as

    [h^0]log F=log g_D-(1/2)Log nu.              (12)

The meridian-regular unit interpretation of (10)--(12) is over
the characteristic-zero cyclotomic coefficient field, retaining
all factorial denominators. No arithmetic integrality at those
denominators is asserted.

## 5. The local Heisenberg regulator is reconstructed

On the marked logarithmic cover of X away from 0,1,infinity put

    U=Log X, V=Log(1-X),
    S=Li_2(X)+UV, R=Li_2(X)+(1/2)UV.

Direct differentiation gives

    dS=U dV, dR=(1/2)(U dV-V dU).              (13)

Thus U/N, V/N and S/N^2 are the coordinates of the usual
Heisenberg period matrix

    Pi_N=[1 U/N S/N^2; 0 1 V/N; 0 0 1].

The right connection Pi_N^(-1)dPi_N has entries dU/N and dV/N
on the first superdiagonal and zero central entry, by (13);
equivalently dPi_N=Pi_N Omega_N. More explicitly,

    U/N=Log z, V/N=Log nu,
    S/N^2=-A_(-1)+Log z Log nu,
    R/N^2=-A_(-1)+(1/2)Log z Log nu.             (14)

Equations (6), (9), and the actual norm-root mark therefore
reconstruct the full local flat period from the unfolded Ward
factorial and its source. Its real regulator is

    D(X)=Im Li_2(X)+Re(U) Im(V),
    dD=Re(U)d Im(V)-Re(V)d Im(U).               (15)

This is the Bloch--Wigner local regulator, with the same marked
logs. Individual Li_2 pole coefficients alone omit the displayed
logarithmic metric term. No knot fundamental-class constant or
orientation is supplied merely by this local calculation.

These logarithmic formulas live on the generic marked punctured
cover. They do not assign Log(0) to the nilpotent special fiber;
there the regular jet and its divided source are kept instead.

The actual divided cyclic source is tied to the pole by an
explicit first-normal identity. Since kappa_N=N kappa+O(kappa^2),
formula (6), with X=-kappa_Nt^N, gives

    partial_kappa A_(-1)|_(kappa=0)=t^N/N.

The literal polynomial source from the cyclic Ward block obeys

    [(sigma f_N(-t e)-(1+t e)f_N(-t e))/kappa]_(kappa=0)
         =-t^N=-N partial_kappa A_(-1)|_(kappa=0). (16)

This directly compares the actual normal source with the
unfolded cyclotomic period coefficient. The same scalar t^N
is the first-normal group-transfer character B_0(1+t e).
The source, norm-root transfer, and period pole are three
specified realizations of this one local normal datum.

### 5.1 The resonant pole is an exact divided-power tensor correction

There is also an operator realization of this pole on the genuine
integral complete-color lift. It is important to use that lift here,
rather than suppose that a fixed-root typical color is a generic-q
quantum-group module. On b factors let C(Q) be the total actual
raising operator. Its individual factors have N-th power zero for
every generic Q. The q-multinomial formula then shows that

    J_b(Q)=C(Q)^N/(1-Q^N)

is regular at Q_N. Denote its root value by J_b. It lowers total
integer position by N, so J_b^b=0. The
[divided Ward fusion proof](divided_ward_factorial_fusion.md) gives
the matrix definitions, all root characters, and arbitrary-block
associativity. The following derivation identifies its correction
directly with the whole function (3).

Since C(Q) is nilpotent for generic Q, evaluating (5) at -t C(Q)
involves only finitely many terms. For m<N its root value is the
corresponding coefficient of log f_N(-t C). For m>=N not divisible
by N, C(Q)^m has a factor 1-Q^N while its denominator is a unit,
so the term vanishes at the root. For m=kN with k>=2 the numerator
has k such factors and the denominator only one, so it also
vanishes. The remaining term, m=N, is exactly (-t)^N J_b/N.
Consequently

    [F(Q,-t C(Q))]_root
       =exp[(-t)^N J_b/N] f_N(-t C).             (16a)

Here the exponential terminates before its b-th power. Equivalently,
if A_i are the individual raising operators dressed by all later
K factors, q-binomial expansion gives

    product_(i=b,...,1) f_N(-t A_i)
       =exp[(-t)^N J_b/N] f_N(-t C).             (16b)

Thus the exact finite tensor defect is the evaluated resonant
logarithm of the all-level function. In the coordinate of (6),
C(Q)^N=(1-Q^N)J_b(Q)=-N h J_b+O(h^2). Substituting this into
-Li_2((-t C(Q))^N)/(N^2 h) gives the same (-t)^N J_b/N;
all its higher dilogarithm powers vanish after specialization.
This comparison uses the moving representation and retains its
first normal. Substituting C^N=0 before taking the quotient would
delete the entire correction.

This is a general tensor theorem, with a nilpotence bound independent
of N for fixed b. It is not a scalar growth theorem. Ordinary pivotal
closure kills a degree-N lowering insertion. A marked missing-edge
insertion can compensate that degree, and its divided Hopf-adjoint
pairing with the literal cut is computed in the fusion note. A source
comparison must retain that relative pairing before contraction.

## 6. A controlled norm theorem on an actual cyclic gauge chart

The local reconstruction also admits an analytic norm estimate.
This is a different parameter direction from the fixed-root h
in (6)--(8): now N varies, Q_N=exp(2pi*i/N), and
hbar_N=2pi*i/N. Fix 0<r<1 and use the branches continued from z=0.
Uniformly for |z|<=r,

    Log g_(D,N)(z)
       =-Li_2(z)/hbar_N-(1/2)Log(1-z)+O_r(1/N). (17)

To prove it, put f_z(x)=x Log(1-z exp(2pi*i*x)). The function
and its first two x derivatives are uniformly bounded on this
compact chart. The finite product is

    Log D_N(z)=sum_(j=1)^(N-1) f_z(j/N).

Trapezoidal Euler summation therefore gives

    Log D_N=N integral_0^1 f_z(x)dx
                         -(1/2)Log(1-z)+O_r(1/N).

Termwise integration of the absolutely convergent logarithmic
series gives integral_0^1 f_z=-Li_2(z)/(2pi*i). The normalization
in (11) changes this by O_r(r^N), since
Log nu_N=Log(1-z^N)/N. This proves (17), with both upper and
lower norm control. It is an estimate of the specific marked
cyclic gauge already identified in Section 4, not a choice of
a new quantum state.

For example an explicit bound for the absolute remainder in (17)
is

    B_r/(12N)+r^N/[2(1-r^N)],
    B_r=4pi r/(1-r)+4pi^2 r/(1-r)^2.

The displayed B_r bounds |f_z''|. The ordinary composite
trapezoidal remainder, multiplied by N, gives its first term;
|Log(1-z^N)|<=r^N/(1-r^N) gives the second. Thus no interchange
of a divergent infinite root product and a limit is used.

In particular its inverse has rate

    (2pi/N)log|g_(D,N)(z)^(-1)| -> Im Li_2(z).    (18)

The full local regulator uses the logarithmic metric term in
(15). On a marked chart define the metrized inverse gauge by

    ||g_(D,N)^(-1)(z)||_reg
      =|g_(D,N)^(-1)(z)|
         exp[(N/(2pi))Log|z| Arg(1-z)].           (19)

Then

    (2pi/N)log||g_(D,N)^(-1)(z)||_reg -> D(z),    (20)

with O_r(1/N) error on fixed compact marked subcharts. At z=0
the metric extends by continuity if needed. Formula (19) is the
explicit metric on the local Heisenberg period line determined
by (15); it is not an additional factor inserted into the actual
Kashaev invariant. A global knot comparison must still show that
its quantum period carries this metric with the prescribed signs
and logarithmic transition functions.

## 7. What the local identification does not imply globally

This replaces the obstructed fixed-N multiplicative comparison
by an explicit coherent all-level function and its marked
cyclotomic period. It proves an exact local source/gauge/regulator
identification for a block built from the actual quantum matrices.

To use it for the knot, the local transfer currents and their
inserted moments must still be transported through the full
source-preserving contraction. The selected cycle and cross-level
metric cannot be inferred from agreement of local factors.
For example, ordinary finite factorial ratios are regular at
their roots because their polar terms cancel; extracting a pole
from an individual infinite factor and forgetting that cancellation
would not be a valid knot-period argument.

The actual Newton period, the partially summed geometric block,
and its marked knot Bloch action already exist in the other
notes. Their remaining comparison must use the unfolded source
complex, retaining the normal edge and all peripheral factors.
Neither global source survival nor the general volume conjecture
is asserted here.

[Exact coefficient audit](../experiments/audit_unfolded_ward_factorial_regulator.py).
[Results](../experiments/unfolded_ward_factorial_regulator_results.json).
[Independent proof audit](unfolded_ward_factorial_independent_audit.md).
[Independent moving-representation and cut audit](divided_ward_bridge_independent_audit.md).
The [global function/source audit](global_period_rigidity_function_audit.md)
records the extra selected-period information still required beyond
this exact local function reconstruction.
