# The peripheral delta module and the normal derivative of the knot period

Research note, 26 October 2026. This identifies a boundary component
which any positive-volume proof must retain. The ordinary principal-root
colors force polynomial growth if a polynomial annihilator acts
nontrivially on the complete-color delta vector. When that boundary
component is retained, a simple rank condition expresses the actual
complete period as the first normal derivative of a homogeneous kernel
line. The derivative has a polynomially bounded source. Its size is
therefore an inverse-operator and source-coupling problem, in the natural
cyclic trace metric.

The statements below separate a necessary boundary factor from a further
rank condition. The positive volume limit is now proved for the knots of
the [net-twist theorem](actual_conway_net_twist_volume.md). For every such
knot, Section 2 therefore proves the boundary-factor condition for every
polynomial all-level annihilator. The special-fiber rank condition in
Section 4 remains additional; the scalar volume theorem does not prove
it or identify a full quantum module with the geometric regulator.

The subsequent [actual Weyl-descent proof](actual_weyl_descent.md)
constructs P=B*(Y-1) from the primitive minimal normal operator for
every knot and proves its unitary reciprocity. Thus those symmetry
data in Section 6 are available for the canonical actual operator.
Those symmetry statements do not prove special-fiber injectivity or
give direct estimates for the inverse below. Section 2's necessity
test still concerns every polynomial annihilator.

The subsequent [peripheral-fusion proof](actual_peripheral_fusion.md)
derives the regular normal boundary lattice from the actual fundamental
parallel, retaining its pole before changing lattice. Its odd normal
state w_N=(M-M^(-1))F_N has K_N=(1/2)partial_(Log M)w_N at M=1.
The adjacent-color splitting there has a nonzero square-zero Casimir
residue whose pivotal partial trace is identity. These exact quantum
extension data do not establish the root-fiber rank or the regulator norm.

The subsequent [ramified Weyl-fibre theorem](ramified_weyl_fibre.md)
retains this derivative as an ordinary coordinate of a descended
algebraic fibre over s=((U-1)/(U+1))^2. Its - sector generator is
z e_- rather than a vector discarded by setting z=0 first. The
source equation and complete functional then hold in that fibre,
with their original rank qualifications. An explicit dimension
formula gives signatures for which negative-sector injectivity
cannot hold; saturated kernels and further lifting data remain
available. No regulator norm is inferred from this descent.

## 1. Fixed state, ring, and principal-root bound

Use the actual literature state in
[the ADO audit](kashaev_ado_pointing.md), with

    q_N=exp(pi*i/N), Q_N=q_N^2, Y=M^2,
    F_N(Y) Laurent polynomial, K_N=F_N(1)=<K>_N,
    F_N(Q_N^r)=C_r(q_N), 1<=r<N.

The [regular-period theorem](regularized_kashaev_period.md) reconstructs
the positive path trace directly from the actual fundamental crossing.
For any fixed b-strand knot braid it proves

    |C_r(q_N)|<=D_N=sin(pi/N)^(1-b)<= (N/2)^(b-1). (1.1)

Take a specified actual annihilator with denominators cleared and
recorded, in the polynomial quantum torus

    R=C(q)[Y^(+/-1),T^(+/-1); T Y=q^2Y T],
    P=sum_(j=0)^d a_j(q,Y)T^j,
    a_j in C[q^(+/-1),Y^(+/-1)].                 (1.2)

An initial power of T permits the nonnegative shift convention.
The [existence](finite_sum_annihilator.md) and
[squared-meridian descent](even_meridian_norm_descent.md) theorems
supply such an actual operator, but do not yet identify its classical
geometric factors.

## 2. A nonzero complete column forces polynomial growth

For 0<=i<=d put

    r_i(q)=a_i(q,q^(-2i)).                         (2.1)

If r_i is not identically zero, it has finite vanishing order nu_i
at q=1. For all large N,

    |r_i(q_N)|>=c_i N^(-nu_i).

Evaluate the actual equation at Y=Q_N^(-i). Its i-th term is
r_i(q_N)K_N. If N>d, every other term uses a noncomplete orbit
color, and hence has modulus at most C_P D_N by (1.1). The fixed
Laurent coefficients are bounded on the unit torus. Consequently

    |K_N|<=C N^(b-1+nu_i).                        (2.2)

Thus a positive exponential volume rate requires

    a_i(q,q^(-2i))=0 for every i.                 (2.3)

Equivalently every coefficient is divisible in the Laurent ring by
q^(2i)Y-1. Polynomial division at its nonzero root proves this
equivalence. Hence the required factorization is exactly

    P=B*(Y-1), B in R with Laurent coefficients.  (2.4)

This is right multiplication: its i-th coefficient is
b_i(q,Y)*(q^(2i)Y-1). A monic operator over C(q,Y) can have poles
on those divisors; an ordinary evaluation of that localized operator
cannot replace the cleared equation used above.

The result is a dichotomy for an arbitrary knot. For the knots covered
by the strict-tree and net-twist volume theorems, their positive volume
limit rules out (2.2), so every polynomial annihilator satisfies (2.3).
For a hyperbolic knot outside the proved class, this remains a necessary
condition for its conjectured positive-volume limit. Conversely, the
boundary factor alone supplies no exponential lower bound.

The [nearby-zero theorem](actual_ado_complete_meridian_zero_accumulation.md)
gives another consequence of the same ordinary-color values: zeros of
the actual reduced state approach the complete meridian at distance
$O(1/N)$. Its final section also records the two-sign version of the
boundary factor for operators in the unsquared coordinate $M$.

## 3. The missing component is a fixed boundary module

At generic q define

    Delta=R/R*(Y-1), delta=class of 1.

It has C(q)-basis T^j delta, j in Z, and

    Y T^j delta=q^(-2j)T^j delta.

Therefore P delta=0 is exactly (2.3). The module is simple at
indeterminate q: polynomial interpolation in Y isolates one term
of any nonzero finite combination of these distinct eigenvectors,
and powers of T then generate all of them. Every vector is killed
by a nonzero polynomial in Y. Localizing the meridian to C(q,Y)
therefore kills Delta completely.

For a polynomial annihilator ideal I, positive exponential growth
would imply I is contained in R*(Y-1). Its cyclic module would have
Delta as a quotient. For one specified P satisfying (2.4), this quotient
already follows without a volume assumption. The generic norm torsor
over C(q,Y) needs a meridian lattice to retain this boundary datum.

At the actual root, impose T^N=1 as well. The resulting Delta_N is
the N-dimensional clock-and-shift module with Y^N=T^N=1, at every
parity and composite level. It is irreducible because the N distinct
Y-eigenvalues and their cyclic shift generate all matrix units.
On functions of the root orbit the complete delta vector is

    e_0=(1,0,...,0),
    e_0(Y)=S_N(Y)/N modulo Y^N-1.

Thus P annihilates this vector on the central fiber when (2.4) holds.
If c_N=(0,C_1,...,C_(N-1)), the actual state there is

    F_bar_N=c_N+K_N e_0.                          (3.1)

Every vector in this affine line satisfies the same special operator
equation and has the same ordinary-color pointing. The complete
coefficient is fixed by extension away from the central fiber.
This affine ambiguity is not permission to change the actual state.

At q=1, (2.4) also gives the vertical factor Y-1 in the classical
polynomial symbol. Removing vertical factors to state an A-curve
equation discards this specific boundary-module datum. The marked
integral/meridian extension must therefore accompany that curve.

## 4. The actual full period is a normal derivative

Assume (2.4) for the specified operator. Work near U=Y^N=1, with
t=U-1 and the fixed root germs

    Y_r(t)=Q_N^r*(1+t)^(1/N), 0<=r<N.

Represent B by the cyclic matrix B_N(t): its row r, column r+j
modulo N receives b_j(q_N,Y_r(t)). Write

    B_N(t)=B_0+t B_1+O(t^2),
    (B_1)_(r,r+j)=(1/N)(Y*d/dY)b_j(q_N,Q_N^r).    (4.1)

Retain the full vector of the actual state and put

    v_N(t)_r=(Y_r(t)-1)F_N(Y_r(t)),
    v_N(t)=v_0+t v_1+O(t^2).

Since P F_N=0, B_N(t)v_N(t)=0. At the special fiber,

    (v_0)_0=0,
    (v_0)_r=(Q_N^r-1)C_r(q_N), 1<=r<N,
    B_0 v_0=0,
    B_0 v_1=-B_1 v_0,
    (v_1)_0=K_N/N.                               (4.2)

The last identity keeps the zero of Y-1 until differentiation:
Y_0'(0)=1/N. In particular the complete full ADO value is exactly

    N_N(1)=eta_N (v_1)_0, eta_N=i^(N+3).           (4.3)

Indeed the full state, before specialization, is

    N_N(M)=eta_N M^(N-1)*(Y-1)F_N(Y)/(U-1).

Its poles, its sign character, and its phase have all been retained.
The normal derivative realizes their cancelled whole germ.

Suppose now that

    rank B_0=N-1.                                 (4.4)

The known nonzero vector v_0 spans its kernel; the reference
component is Q_N-1 because C_1=1. The solutions of the inhomogeneous
normal equation in (4.2) form a genuine affine torsor under C*v_0.
Since (v_0)_0=0, its complete-coordinate functional is constant.
Thus (4.2) determines K_N exactly, without choosing the derivative
of a central normalization unit.

More explicitly replacing v_N(t) by c(1+t)v_N(t), c(1)=1, adds
c'(1)v_0 to v_1. The complete value in (4.3) does not change.
This is the anchored normal-period comparison, with its specified
root germs. The rank condition is additional to the existence of
the actual operator; it is not assumed for every knot.

The regular complete scalar of the preceding note is

    R_N(1)=(v_1)_0-p_N(1), |p_N(1)|<=D_N.          (4.5)

So the normal derivative and that regularized field-trace period
give the same positive-volume target.

## 5. The first obstruction selects a point of the delta torsor

Let D(t)=diag(Y_r(t)-1), so P_N(t)=B_N(t)D(t). At zero,
Im D(0) is the hyperplane of vectors with zero complete coordinate.
Its kernel is C*e_0. Since ker B_0=C*v_0 is inside this hyperplane,

    rank P_0=N-2, ker P_0=span(e_0,c_N).           (5.1)

The first lifting obstruction is the linear map

    kappa:ker P_0 -> coker P_0,
    x -> [P_1 x].                                 (5.2)

This is the usual first Bockstein: a lift x+t x_1 solves the equation
through first order exactly when P_0 x_1+P_1 x=0. In particular

    P_1 e_0=(1/N)B_0 e_0.

This is not in Im P_0. Otherwise e_0 would differ from a vector in
Im D(0) by a member of ker B_0, also in Im D(0), a contradiction.
The actual vector c_N+K_N e_0 lifts. Hence kappa has rank one on
the two-dimensional kernel, and its kernel selects that exact line.

Choose any left null vector ell of P_0 with ell P_1 e_0 nonzero.
The period is the exact ratio

    K_N=-ell P_1 c_N/(ell P_1 e_0).                (5.3)

Changing ell subject to this condition gives the same answer,
because the actual lift exists. This derivative pairing records
the boundary extension that the ordinary special kernel omits.
Under (4.4) the rank loss in P is exactly one simple Smith factor;
no unverified higher-order lift is being used. More singular cases
need the higher jets retained in the
[bounded-jet construction](bounded_meridian_jets.md).

## 6. A bounded source and the exact inverse-matrix period

Use the Hermitian norm on the orbit coming from the cyclic trace;
the unnormalized Euclidean version differs only by the common
factor N^(1/2). The fixed Laurent coefficients give

    ||B_1||<=C_B/N,
    ||v_0||<=2D_N*sqrt(N).                         (6.1)

For the first inequality write B_1 as a finite sum of diagonal
coefficient matrices times unitary cyclic shifts, and bound each
Y-derivative on the unit torus. Thus the normal equation has a
polynomially bounded, explicitly specified source.

Let B_0^+ be the Moore--Penrose inverse. Since e_0 is perpendicular
to ker B_0, every solution of (4.2) has the same complete coordinate,
and exactly

    K_N=-N*e_0^* B_0^+ B_1 v_0.                  (6.2)

If s_N is the smallest nonzero singular value of B_0, then

    |K_N|<=2 C_B D_N sqrt(N)/s_N.                 (6.3)

Consequently positive volume growth would force an exponentially
large inverse norm in this specified boundary problem. The source
itself cannot supply that positive exponent. Small singular values
alone are insufficient: (6.2) also retains the source and the
complete-coordinate pairing. In a singular-vector decomposition
it is the sum of their two overlaps divided by the corresponding
singular values. No largest-eigenvalue prescription is being used.

The geometric action already has imaginary value Vol at completeness,
by the [actual action proof](quantum_longitude_and_regulator_action.md).
For a knot covered by the net-twist theorem, whenever the stated rank
condition holds, (6.2) is an exact expression for its invariant and
therefore has the scalar volume growth proved there. Deriving this
growth directly from the inverse and identifying the geometric
regulator at the module level remain additional tasks. Neither (6.3)
nor a geometric critical point by itself controls the two overlaps.
Extra left operator factors can create small singular values with
zero relevant overlap.

### A Weyl symmetry isolates the relevant inverse

There is a stronger reduction when the *actual operator* has a checked
reciprocity. Write R h(Y)=h(Y^(-1)), Q=q^2, and suppose

    J=-Y R, J'=c(q,Y)T^d R,
    B J=J' B,
    c(q,Y)c(q,Q^(-d)Y^(-1))=1,
    |c(q,Y)|=1 on the unit torus.                 (6.4)

Both give unitary involutions on the root orbit; B_0 intertwines
them. Their -1 eigenspaces are orthogonal to the +1 eigenspaces,
and e_0 has J-eigenvalue -1. The factor Y-1 is the squared-meridian
form of the Weyl denominator, up to the retained monomial M.

If J v_0=v_0, differentiating the operator identity at U=1 proves
J' B_1 v_0=-B_1 v_0. Explicitly inversion sends t to -t+O(t^2),
and the domain involution has derivative J/N. Applying the
differentiated identity to v_0 kills the terms containing B_0 v_0
and leaves exactly this source parity. Thus only the -1 symmetry
sector enters the complete normal period.

Under (4.4) this source parity is automatic whenever K_N is nonzero.
Indeed the one-dimensional kernel makes J v_0=epsilon*v_0.
If epsilon=-1, the same differentiation gives source parity +1.
The -1 part of v_1 would then be a multiple of v_0 and have zero
complete coordinate, forcing K_N=0.

More generally (4.4) can be weakened in this symmetry setting:
it suffices that J v_0=v_0 and B_0 is injective on the -1 domain.
The actual derivative places the source in its image. Extra +1
kernel vectors do not affect the value. Writing the restricted
Moore--Penrose inverse as B_-^+, the exact period is

    K_N=-N e_0^* B_-^+ B_1 v_0.                  (6.5)

It is this inverse and its specified source that need a regulator
norm theorem. Small singular values in the other symmetry sector
make no contribution. Reciprocity is additional quantum data;
it is not assumed merely from the classical A-curve's inversion
symmetry. The subsequent [actual-state proof](actual_weyl_descent.md)
now derives this reciprocity for the primitive minimal normal
operator of every knot, and also proves J v_0=v_0 directly. An
arbitrary nonprimitive or left-multiplied operator still needs its
own checked intertwiner and lattice.

There is an explicit Hilbert-90 descent of the reflected kernel frame.
If its generic rational kernel is a C(U)-line, reciprocity gives

    J v=gamma(U)v, gamma(U)gamma(U^(-1))=1.

When J v_0=v_0, gamma is a unit at U=1 with gamma(1)=1. Set
g(U)=(1+gamma(U))/2. Direct division gives g(U)/g(U^(-1))=gamma(U).
Thus g*v is J-invariant and g(1)=1. This is an explicit frame change
of the same pointed line, not a replacement knot state. Its derivative
adds g'(1)v_0 and leaves the complete normal period unchanged. Zeros
or poles of this frame elsewhere remain part of the lattice data.
This is quadratic Hilbert 90 on the central involution, after the
normal pointing has already fixed the value at the branch point.

The ambient cyclic orbit also retains a precise signed dihedral
relation. Direct multiplication gives J T J=Q*T^(-1). With the
actual ADO character kappa=-q^(-1), put T_tilde=kappa*T. Then

    J T_tilde J=T_tilde^(-1),
    T_tilde^N=kappa^N=(-1)^(N-1).                 (6.6)

Thus the uniform half-root lambda=-q, lambda^2=Q, is compatible with
the Weyl action and with the full even-level sign. This is an action
on the ambient orbit module. It does not assert that the scalar
operator's rational solution line is stable under T; only its
checked reflection intertwiner and central frame descent are used.
Neither Hilbert-90 descent nor this finite symmetry supplies the
missing regulator norm.

## 7. A fixed initial form bounds the rational root period rank

There is a simple separate certificate for generic rational rank.
For any Laurent polynomial operator L, let r be the least Y-exponent
in its coefficients and define

    I_0(q,z)=sum_j [Y^r]a_j(q,Y)*z^j.              (7.1)

At q_N, suppose this initial form is nonzero. On E=C(Y) over
C(U), U=Y^N, represent Y^(-r)L in the monomial basis
1,Y,...,Y^(N-1). Its matrix is integral over C[U]. Modulo U it
is lower triangular: positive powers of Y either increase the
basis exponent or wrap with a positive power of U. Its diagonal
entries are I_0(q_N,Q_N^k). The principal submatrix on their
nonzero indices has nonzero determinant. Therefore

    dim_(C(U)) ker L
       <=#{0<=k<N : I_0(q_N,Q_N^k)=0}.             (7.2)

This counts distinct lattice roots, not their multiplicities.
If I_0=g(q)*z^a*(z-q^(2s))^m, with g(q_N) nonzero and m>=1,
the bound is one at every such level. Any known nonzero rational
period then proves generic rank one. The same applies at infinity.
This is a condition on the actual quantum initial form, not on
the commutative A-polynomial alone. Terms vanishing at q=1 can
change the extremal Y-coefficient.

The bound certifies the generic line used in Hilbert 90. It does
not replace (4.4), which concerns its special fiber and the normal
derivative. A rational kernel line may acquire extra special
solutions; that possibility is exactly what the lattice retains.

The subsequent [torsion initial-rank theorem](torsion_initial_rank.md)
extends the pure-binomial test: rational-coefficient initial forms
have only finitely many isolated torsion-grid exceptions outside
their contained binomial torsion curves. Their eventual root count
is given by finite periodic congruences. A single occupied curve
therefore gives generic rank one even in the presence of non-toric
initial factors. The proof keeps the q half-root and provides an
explicit exceptional-level bound. It does not establish the special
negative-sector injectivity or regulator norm.

## 8. The rank hypothesis cannot be suppressed

For a manufactured root family let

    F_N(Y)=1+a_N S_N(Y),
    B=(T-1)(T-Q), P=B*(Y-1).

Then P F_N=0 because (Y-1)F_N=Y-1+a_N(U-1), and B kills 1,Y.
All ordinary orbit values are one, while K_N=1+N*a_N is arbitrary.
Here B_0 has a two-dimensional kernel. Its complete-coordinate
functional does not vanish on that kernel, so the first normal
equation leaves this freedom. The quantum initial form also has
two distinct lattice roots, consistent with (7.2).

These are not knot states. In particular choosing a_N to change
the complete value violates the coherent all-level color data,
whose recovery is proved in [the all-level theorem](all_level_a_period.md).
The example only explains the rank requirement for the simpler
normal equation (6.2), not a new ambiguity in the actual invariant.

## 9. Independent operator and actual-state calibration

The audit derives a telescoping operator for the finite block

    H_N(Y)=sum_(k=0)^(N-1) t_k(Y),
    t_k=product_(r=1)^k(Y+Y^(-1)-Q^r-Q^(-r)).

The subsequent [whole-source four-plat proof](figure_eight_whole_source_identity.md)
identifies H_N with the actual figure-eight ADO state at every level,
with all peripheral factors retained. The derivation here does not
take that equality as a premise. Put Z=Q^k and

    C(Y,Z)=(Y-1)^2 Z/((Y-Z)(1-YZ)),
    D(Y)=Y(Y+1)(Q-Y^2)(QY^2-1),
    g=Q^2Y^2-QY^4+QY^3+QY-Q+Y^2,
    c_-=Y^2(Q-Y)(QY^2-1),
    c_0=-(Y-1)^2(Y+1)g,
    c_+=Y^2(QY-1)(Q-Y^2).

The finite products give the two Y-shift ratios and the k-ratio
directly. Substitution proves the exact rational certificate

    sum_(j=-1)^1 c_j(Y)*t_k(Q^jY)/t_k(Y)
      =D(Y)*(C(Y,QZ)*t_(k+1)/t_k-C(Y,Z)).          (9.1)

At a root Q^N=1, C(Y,1)=-1 and
t_N=Y^N+Y^(-N)-2. Telescoping therefore gives

    (c_-T^(-1)+c_0+c_+T)H_N
                   =D(Y)*(3-U-U^(-1)).           (9.2)

The central factor is retained. Applying D(Y)T-D(QY) kills the
source. Left multiplication by T removes the negative shift.
The common coefficient factor removed in the audit is exactly
Q^3Y(Q^3Y^2-1)^2, recorded before any specialization. The resulting
polynomial P has every boundary column factor, initial form
z(Q-z), and classical symbol

    (Y-1)^2(Y+1)^2*(z-1)*Y^2*A_geo(Y,z),
    A_geo=z^2-(Y^2-Y-2-Y^(-1)+Y^(-2))*z+1.         (9.3)

This checks the familiar geometric peripheral polynomial and the
additional boundary factors in fixed conventions. It does not prove
an AJ theorem for arbitrary knot operators or identify root central
curves with A_geo.

For this calibrated operator the exact reciprocity in (6.4) is
c(Q,Y)=-Q^12 Y^8 and d=3. Substituting its coefficients verifies

    -Q^j Y b_j(Y)=c(Q,Y)b_(3-j)(Q^(-3)/Y).

The two involution and unit-norm identities follow by multiplication.
The -1 domain has dimension ceil(N/2), including every parity.
The audit verifies the source parity and recovers the same period
using only that folded inverse. This removes an irrelevant symmetry
sector before any asymptotic estimate; it is not such an estimate.

[The audit](../experiments/audit_peripheral_normal_period.py) verifies
the certificate symbolically. At levels 2,3,4,5,6,7,8,10 it proves
coefficientwise equality of H_N with independently computed actual
figure-eight cut Laurent polynomials over the stated finite fields,
and verifies their annihilation. At eleven levels through 18 it
checks both matrix ranks, the derivative product rule, and exact
recovery of the complete block period by (4.2), (5.2), and the
Weyl-folded inverse (6.5). It also
checks 50 initial-root dimension examples and six explicit rank-
ambiguity examples. All checks passed. The larger block tests do
not extend the actual-state comparison beyond its stated levels.
That all-level comparison is now supplied by the independent
four-plat proof, which also proves the selected volume limit and
leading coefficient for the actual figure-eight invariant.
Results are in [the output](../experiments/peripheral_normal_period_results.json).

    python3 experiments/audit_peripheral_normal_period.py

The boundary delta module, first lifting obstruction, Moore--Penrose
inverse and initial-form argument use standard module and linear
algebra. Their proofs above specify their role in the actual marked
period; no novelty claim or imported analytic theorem is made.
The quantum-torus Weyl involution already has explicit coverage in
[Le's lectures, Section 5.9](https://letu.math.gatech.edu/Papers/Lectures_Luminy_2014_new.pdf).
Only its scope is used for coverage; no AJ, state-comparison or
analytic conclusion from that source is a premise. The weighted
involutions and source parity above were obtained by direct operator
identities, with all monomial phases retained.
The [geometric triangulation bridge](triangulation_regulator_bridge.md)
supplies the marked Bloch action for the comparison with this normal
period. The scalar volume equality is established for the stated
strict and net-twist knot classes. The survival and identification of
the actual geometric factor, the additional rank conditions in this
note, and the volume conjecture outside the established classes remain
open.
