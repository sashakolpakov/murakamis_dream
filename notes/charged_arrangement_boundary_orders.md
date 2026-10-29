# Boundary orders of the actual charged gain arrangement

28 October 2026. The fixed-diagram charged polynomial has an additional
restriction absent from arbitrary unit-root coefficient examples: it
has a bounded number of root-INTERVAL blocks. Each block has distinct
roots, even though its length grows with N. This bounds the order of
every noncoordinate collision at a generic linear flat independently
of N. A zero logarithmic residue at such a boundary can therefore
involve only a bounded coordinate cut deficit.

The following statements concern actual fixed-clock binary products,
before or after unit-factor-preserving fusions. They do not identify
the full coupled clock phase or establish its volume bound.

## 1. Exact classification of the linear flats

Write the source, with extracted scalars retained in gamma, as

    P=gamma product_e product_(r=0)^(L_e-1)
                       (X_(u_e)-a_e Q^r X_(v_e)),
    f=P/product_i X_i^(q_i), sum_i q_i=sum_e L_e.

There are B block slots, bounded by the fixed original diagram, with
L_e<=N and a_e in the actual 2Nth roots of unity. Loops are first
evaluated as their exact scalar monomial and their source charge
adjusted by the proved source identity. A zero scalar kills the state.
Thus genuine remaining factors have two distinct endpoints. The
coordinate hyperplanes X_i=0 are included in the arrangement.

Every intersection flat F has the following form. Some coordinates
are identically zero; call their set Z. The others are partitioned
into classes, with relations X_i=zeta_i T_class and |zeta_i|=1,
where the T_class are independent. Indeed follow the gain equations
X_i=g X_j along a connected component. A nontrivial cycle gain or
one coordinate-zero equation forces that whole component to zero;
otherwise path gains give precisely these proportional coordinates.

Put

    m_Z=number of factors with both endpoints in Z,
    e_Z=q(Z)-m_Z,
    c_F=number of OTHER factor hyperplanes containing F.

Every one of these c_F factors joins a pair in the SAME nonzero
class and has its particular matching gain zeta_i/zeta_j. Each
root-interval block contributes AT MOST ONE such factor, since its
Q-roots are distinct. Consequently

    0<=c_F<=B.                                      (1)

If F has codimension c, then

    c=|Z|+sum_nonzero_classes (class_size-1).          (2)

The common origin is omitted after the usual common-scale quotient;
it does not supply an additional projective boundary divisor.

## 2. Its masterfunction and source-form orders are explicit

Blow up the linear flat F and take a generic point of its exceptional
divisor, away from smaller intersections. Every linear factor whose
hyperplane contains F has order one in the normal scale t; the other
factors are units. A coordinate X_i vanishes there exactly when i is
in Z. Therefore the EXACT logarithmic residue/order of f is

    a_F=ord_F(f)=m_Z+c_F-q(Z)=c_F-e_Z.             (3)

In particular a_F=0 forces e_Z<=B. A macroscopic coordinate deficit
cannot be neutralized by bounded noncoordinate multiplicity. If Z is
empty, a proper arrangement flat has a_F=c_F>0, and f tends to zero
rather than a finite nonzero value.

The actual coefficient form is

    Omega=P dX_1...dX_k/product_i X_i^(q_i+1).

The normal blow-up Jacobian has order c-1. Its exact normal order is

    ord_F(Omega)=a_F+c-|Z|-1.                      (4)

This counts the extra one in each coordinate pole; it must not be
confused with only the phase order (3). At ZERO phase order, a
noncoordinate flat c>|Z| produces NO pole of the original form.
The only possible logarithmic source poles with zero phase order
are pure coordinate flats: c=|Z|, c_F=0 and e_Z=0. These are the
already proved exact tight-cut factorizations. Equation (4) does
not declare stationary values of a holomorphic boundary extension
irrelevant; it distinguishes those from an original residue pole.

For example (4) follows in explicit local coordinates: choose a basis
of F and c normal vectors, put the normal displacement equal to
t times a nonzero normal direction, and use its remaining c-1
direction ratios. The wedge Jacobian contributes t^(c-1), numerator
factors contribute t^(m_Z+c_F), and coordinate denominators contribute
t^(q(Z)+|Z|). This proves the formula with no quantum asymptotic.

## 3. Linear chart changes have polynomial conditioning

Normalize the factor and coordinate rows to

    e_i-g e_j, g in mu_(2N), or e_i.

Every nonzero s-by-s minor A of such a matrix obeys

    (2/N)^s <= |det A| <=2^s.                     (5)

Here s is bounded by the fixed number of anchors. To prove this,
restrict each chosen row to the chosen columns. A two-entry row is
a gain edge; a one-entry row is a unit ground row. Permuting connected
components splits the minor. A nonzero square block must have equal
numbers of rows and vertices. Each connected block is either a tree
with one ground row, or an ungrounded unicycle. Leaf elimination gives
a unit determinant in the first case and a unit times (1-holonomy)
in the second. An unbalanced count or trivial cycle holonomy gives
zero. All gains and holonomies are 2Nth roots of unity, whose nonzero
differences from one have modulus at least 2 sin(pi/(2N))>=2/N.
Multiplying component factors proves (5).

Thus inverse normal-coordinate matrices obtained from independent
rows have entries at most a fixed-dimensional polynomial in N by
Cramer's rule. No uncontrolled exponential condition number is
hidden in THIS linear arrangement-coordinate step. This is not
yet a bound for a global Morse-flow Jacobian.

## 4. Mixed-sign monomial corners create no new finite critical value

Blowing up all linear intersection flats in increasing dimension
gives local normal-crossing charts whose boundary divisors are labelled
by the original flats. One can see this directly by induction: the
intersection of two incomparable flat transforms has already been
blown up, so only nested flat labels can meet; a basis adapted to
that flag gives the successive normal ratios. Each arrangement
factor is a monomial in these normal coordinates times a unit.

Accordingly a local masterfunction is

    f=u(t,y) product_i t_i^(a_i),                  (6)

where u is a nonvanishing holomorphic unit and the a_i are the
orders (3). If at least one VANISHING normal coordinate t_j has
a_j!=0, choose a local holomorphic a_j-th root of u and change

    t'_j=t_j u^(1/a_j).

The Jacobian at the boundary is nonzero and the coordinate divisors
are preserved. This absorbs the unit EXACTLY: (6) becomes a monomial,
not merely its first-order approximation.

Resolve its mixed-sign indeterminacy by the toric subdivision of the
normal cone along a dot w=0. On an orbit mapping to a finite nonzero
value, its cone sigma lies in this kernel. The nonzero character a
therefore descends to a NONCONSTANT character of that orbit's torus:
it annihilates sigma but is not the zero character. Its derivative
in a toric-ratio direction is nonzero. Thus a new zero-order exceptional
divisor from cancellation of positive and negative weights is NOT
a critical stratum over C*. No assumption that the weights have one
sign is needed.

Possible finite nonzero boundary critical strata must instead meet
a normal-crossing stratum where EVERY vanishing original-flat order
is zero. By (1)--(3), every associated nonempty coordinate cut then
has bounded deficit e_Z<=B. In particular the sufficient condition

    e_Z>B for all nonempty proper coordinate subsets Z

excludes ALL nonzero finite boundary critical values of this fixed
anchor masterfunction. This is a qualitative boundary-tameness
statement. It still requires a separately controlled cycle construction
to give a uniform quantum upper estimate.

## 5. What is left for the FULL phase

The existing cut-jet source theorem controls the normal coefficient
cost of the bounded deficits isolated here. It retains the lower
dimensional periods and does not bound them by a regulator. Similarly
the gain-minor estimate controls linear charts, not arbitrary nonlinear
transport. The
[polynomial logarithmic-mass lemma](actual_coefficient_minimax_upper.md)
specifies what a controlled sublevel representative would accomplish.

There is also an N-dependent saturation issue: an O(1) normal order
is O(1/N) in the normalized log action. Quantum critical points may
approach such a divisor in a 1/N boundary layer even when the limiting
interior critical equations lose a normal constraint. They cannot be
declared points of the SATURATED classical critical closure without
an additional actual source or connection argument. The known sharp
critical-regulator bound covers that closure, not every restricted
boundary stationary equation.

Finally all the preceding critical statements fix the integer clocks.
Complex clock deformation changes the unit-gain interpretation and
must retain the exact feedback and factorial interpolants. No bound
for the complete knot scalar or its nonzero geometric coefficient
is claimed from these anchor results alone.

[Audit](../experiments/audit_charged_arrangement_boundary_orders.py):
actual source flats, complete gain-class/zero-class bookkeeping,
bounded noncoordinate multiplicities, exact normal orders, and
root-of-unity minor/conditioning bounds.
