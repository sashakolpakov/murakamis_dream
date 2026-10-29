# An explicit global Legendre contour and its source-preserving radial homotopy

28 October 2026. Every supplied positive complete ideal triangulation
with the marked full-rank Lagrangian gluing rows has an explicit global
contour on its positive angle polytope. On this contour the WHOLE
imaginary action equals Rivin volume, including off-critical points.
Its complex Jacobian is everywhere invertible. An explicit radial
homotopy from the geometric fixed-radii chain preserves the leading
period, with every boundary prism exponentially smaller. Gaussian
Schur complements preserve the same positive half-plane structure.

These are general contour constructions, not assumptions of
noncancellation. They do not assert that the ORIGINAL quantum
source has already been changed into this positive chart. The
original figure-eight indefinite chart and the five-crossing
bent-source calculation show why that last transport is substantive.
No new knot invariant is defined here.

## 1. The marked positive chart and its explicit angle polytope

Use the [positive quad-chart theorem](positive_quad_chart_and_actual_torus_signature.md).
After its positive rotations, the marked gluing equations are

    A x+B y=c, B invertible, AB^t=BA^t,
    x_j=Log z_j, y_j=Log(1-1/z_j), Im z_j>0.

Put C=B^(-1)A=C^t. At the complete meridian the retained
constant c is purely imaginary. Write B^(-1)c=i kappa,
with kappa real, and retain exactly the potential

    W(x)=sum_j Li_2(exp x_j)+(1/2)x^t(I-C)x
                                  +i(kappa-pi*1)^t x.   (1)

No imaginary constant is added. This is the marked potential
whose complete critical value was calibrated in the quad-chart
theorem. Put x=rho+i theta and

    gamma(theta)=kappa-C theta,
    beta(theta)=pi*1-theta-gamma(theta),
    P={theta:theta>0, beta(theta)>0, gamma(theta)>0}.        (2)

This is a convex bounded open polytope. It is the positive
angle domain with the marked edge and meridian ANGLE equations
imposed. The three angles in tetrahedron j are theta_j,beta_j,
gamma_j. The supplied complete point theta_* belongs to P.

Let F(rho,theta)=Im W(rho+i theta). Directly from (1),

    F(rho,theta)=sum_j Im Li_2(exp(rho_j+i theta_j))
                                             -rho^t beta(theta). (3)

In particular F is separable in its radial variables, even
though the affine angle constraints couple its angle variables.

## 2. A unique radial minimum constructs the contour globally

For every theta in P,

    partial_(rho_j)F=-Arg(1-exp(rho_j+i theta_j))-beta_j,
    partial_(rho_j)^2 F
       =Im[z_j/(1-z_j)]>0.                       (4)

As rho_j tends to -infinity the first derivative tends to
-beta_j<0; at +infinity it tends to gamma_j>0. Hence F has
a UNIQUE global radial minimum, with the explicit solution

    rho_L,j(theta)=log[sin beta_j(theta)/sin gamma_j(theta)],
    x_L(theta)=rho_L(theta)+i theta.              (5)

The equality follows from the ordinary sine rule: its positive
shape has argument theta and Arg(1-z)=-beta. Existence and
uniqueness also follow from (4), without assuming an optimizer
or a contour intersection. On every compact angle subpolytope
the radial objective is uniformly coercive.

On this graph the OFF-CRITICAL identity is exactly

    F(rho_L(theta),theta)
       =sum_j [Im Li_2(z_j)-rho_L,j beta_j]
       =sum_j D(z_j)
       =V(theta).                               (6)

Here D is Bloch--Wigner and V is the ordinary sum of ideal
tetrahedron volumes. Thus the original discrepancy between
off-critical dilogarithm action and volume disappears on this
specified nonlinear contour. This is stronger than comparing
only their critical values.

Rivin strict concavity makes theta_* the unique global maximum
of (6). Its value is the marked hyperbolic volume. The volume
extends continuously to the compact closure of P, and every
other point of that closure has strictly smaller volume. In
particular its boundary has a strict uniform volume gap.
The noncompact radial behavior of (5) at some faces is recorded;
it has not been declared harmless for an arbitrary quantum
amplitude.

## 3. The contour is an algebraic phase graph on a finite cover

Set p_j=exp(2i theta_j), q_j=exp(2i gamma_j). Then (5) gives
the WHOLE rational identity

    z_j=(1-p_j q_j)/(1-q_j),
    q_j=exp(2i kappa_j) product_k p_k^(-C_jk).     (7)

On the positive real phase locus,

    z_j/conjugate(z_j)=p_j,
    z_j''/conjugate(z_j'')=q_j,
    z_j''=1-1/z_j.

Since C is rational, one fixed finite cover of the phase torus
makes all the monomials in (7) ordinary Laurent monomials. For
the actual integral logarithmic gluing marks kappa/pi is also
rational, so its constants are roots of unity. The contour is
therefore the positive real locus of a rational algebraic graph
on that marked finite cover. It is not primarily a collection
of asymptotic jets. Formula (7) retains the sign and winding
marks through kappa and C.

The graph also glues explicitly across the POSITIVE quad atlas.
The cyclic rotation x'=y, y'=-x-y+i pi permutes the angles
and acts on their squared phases by the monomial map

    p'=q, q'=(pq)^(-1).

Substituting these into (7) gives

    z'=(1-p'q')/(1-q')
                  =q(1-p)/(1-pq)=1-1/z.

Thus these reference contours are the same positive
angle-to-shape construction in different quad coordinates,
not unrelated local saddles. This is a classical algebraic
atlas identity; the corresponding EXACT finite quantum
quad/source transformation is not inferred from it.

## 4. A positive Hessian structure controls its Jacobian and all Schur reductions

Let H=W_xx and write

    H=K+iD,
    D=diag_j Im[z_j/(1-z_j)]>0,
    K=I-C+diag_j Re[z_j/(1-z_j)]=K^t.            (8)

This holds throughout the positive product of half-planes,
not just on the contour or at its maximum. The real Hessian
of F in radial/angle coordinates is

    Hess F=[[D,K],[K,-D]].                       (9)

Differentiating its radial minimum gives

    R:=d rho_L/d theta=-D^(-1)K,
    Hess V=-G, G=D+K D^(-1)K>0.                 (10)

These formulas prove strict concavity directly in the selected
angle coordinates. The complex contour Jacobian is

    J_L=R+iI=-D^(-1)conjugate(H),
    H J_L=-G.                                   (11)

It is invertible EVERYWHERE on P. Indeed H has positive
imaginary part, so Hu=0 would imply u^*D u=0. Thus the
contour is a totally real immersion with no vanishing
holomorphic volume Jacobian. Its determinant and Gaussian
half-density have continuous nonzero marks on the convex P.
There is no local Maslov obstruction or a zero Jacobian to
be overcome by a limit.

This structure survives arbitrary successive Gaussian
eliminations. If a complex symmetric matrix H has Im H>0,
partition it as [[E,F],[F^t,G_0]]. The principal block E is
invertible and its Schur complement S=G_0-F^t E^(-1)F obeys

    Im S>0.                                     (12)

For a vector v put w=(-E^(-1)Fv,v). Then
v^*S v=w^*H w, whose imaginary part is w^*(Im H)w>0.
This proves (12) without a diagonalization or a scalar-root
argument. It is the all-rank version of the positive-half-plane
phenomenon checked explicitly in the five-crossing reduction.

Real full-rank linear restrictions also preserve the condition,
since Im(L^t H L)=L^t(Im H)L>0. Conversely a same-dimensional
REAL symplectic Gaussian change cannot repair an indefinite
imaginary Hessian. If H'=(E+F H)(A+B H)^(-1) is its usual
fractional action, the symplectic identities give

    Im H'=(A+B H)^(-*) (Im H)(A+B H)^(-1).

Hermitian inertia is unchanged. This distinguishes a positive
chart construction from an unproved Gaussian repair of the
original indefinite flow chart. Controlled elimination or a
nonlinear Euler/quad transform requires its own source map.

## 5. An exact radial homotopy with automatically lower boundary prisms

Put rho_*=Re x_* at the complete point. Let Q be ANY compact
convex angle polytope contained in P with theta_* in its
interior. Compare the two ACTUAL chains

    Gamma_0(theta)=rho_*+i theta,
    Gamma_1(theta)=rho_L(theta)+i theta, theta in Q,
    Gamma_s(theta)=[(1-s)rho_*+s rho_L(theta)]+i theta. (13)

The fixed-radii theorem makes F(rho_*,theta) strictly concave
with its unique maximum V_* at theta_*. The Legendre chain
has the same property by (6). Convexity in rho gives the
WHOLE homotopy inequality

    F(Gamma_s(theta))
       <=(1-s)F(rho_*,theta)+sV(theta)<=V_*.       (14)

Equality is possible only at theta_*. On the ENTIRE boundary
prism [0,1] times boundary(Q), compactness yields

    F<=V_*-delta_Q, delta_Q>0.                  (15)

Thus this contour deformation comes with a proof of its
boundary gap; a boundary estimate is not appended as an
unverified condition. Its whole image is compact for fixed Q,
and stays in the original positive holomorphic chamber.

For any holomorphic top form omega_N on that image, Stokes
gives the EXACT period difference as the oriented boundary-prism
period. In particular if its actual uniform finite-level form is

    omega_N=N^mu exp[NW/(2pi i)]
                              (a_0(x)+O(1/N)) dx_1...dx_t,

with its original base line retained, then (15) proves that
the two selected periods differ by
O(N^B exp[N(V_*-delta_Q)/(2pi)]). No coefficient is set to
one by normalization. If a_0(x_*) is a unit, each chain has
one selected oriented saddle (multiplicity one), with its
nonzero ORIGINAL density, contour Jacobian and Gaussian
determinant retained. The numerical coefficient is their
specified product, not the number one. Nonvanishing follows
directly from the unique maximum, (11), and the negative
real Gaussian Hessian; its power is N^(mu-t/2). It is not
an assumption that an unspecified thimble intersects a
quantum source.

The statement is for these explicit chains and their retained
prism. Applying it to an original knot state requires an exact
source-preserving positive-chart realization of that state.
It does not assert that realization merely from classical
gluing or from a nonzero local normal density.

## 6. Every nonzero integer alias has an explicit radial escape direction

For an integer vector m, the logarithmic alias is

    W_m(x)=W(x)+2pi i m^t x,
    F_m=F+2pi m^t rho.

For theta in P, (4) has the global range

    -beta_j<partial_(rho_j)F<gamma_j,
    beta_j,gamma_j in (0,pi).

Consequently, whenever m_j!=0,

    sign(m_j) partial_(rho_j)F_m
                        >=2pi|m_j|-pi>=pi|m_j|. (16)

There is NO critical point of any nonzero alias anywhere in
this marked positive chamber. Moreover the explicit flow

    rho_j(s)=rho_j(0)-s sign(m_j), m_j!=0,
    rho_j(s)=rho_j(0), m_j=0

obeys the uniform whole-function inequality

    dF_m/ds<=-pi ||m||_1.                       (17)

For example start at constant rho_*. After a fixed displacement
S>2||rho_*||_infinity one has

    F_m(S,theta)<=V_*
                  -pi(S-2||rho_*||_infinity)||m||_1. (18)

Thus all translated alias BULK chains have explicit exponential
loss, uniformly even in the infinitely many alias labels.
Only finitely many translation directions are used, but no
claim that finitely many Stokes branches exhaust the problem
is made. The decay in ||m|| controls the remaining labels.

The exact radial homotopy also retains its boundary face
periods. Unlike (15), those alias prisms need NOT automatically
be below V_*: their initial phases include 2pi m^t rho_*.
They cannot be erased because their interiors have no critical
point. This construction therefore reduces positive-chamber
alias competition to explicit face sources; it does not prove
those face sources vanish or have smaller rate in every knot.
The original finite-mode or finite-height quadrature remains
the way to carry those sources into a genuine comparison.

### Topology separates positive peripheral aliases from degenerate edge walls

For the actual one-cusped triangulation there is a further uniform
restriction. It has t edges and t tetrahedra: compactifying its
torus cusp to the ideal vertex gives Euler characteristic one,
so 1-#edges+2t-t=1. Choose the rows as
t-1 ACTUAL independent edge rows followed by the marked meridian,
as in the supplied gluing input. An integer alias changes the
imaginary equations to

    A theta+B gamma=Im c+2pi Bm.

Undoing the fixed quad rotations, its edge totals are therefore
2pi(1+k_e), with integer k_e on those t-1 rows. For strictly
positive tetrahedra every edge total is positive, so k_e>=0.
But the sum over ALL edge angles is exactly 2pi t, and hence
the omitted edge has total 2pi(1-sum k_e). Its positivity
forces sum k_e<=0. Consequently EVERY k_e is zero.

Thus any strictly positive alias cell has its ORIGINAL edge
angle equations. If m!=0, invertibility of B makes its remaining
meridian-angle shift a nonzero integer multiple of 2pi. Such
cells are distinct fixed-meridian-angle slices of the SAME full
Rivin angle polytope. Their closures omit the unique complete
maximizer. Strict concavity and compactness therefore bound their
volume maxima strictly below V_*. Only finitely many integer
meridian windings are feasible because that angle polytope is
compact, so the gap is uniform over all feasible nonzero
POSITIVE peripheral aliases.

This statement is not extended to all weak nonnegative alias
loci. A nonzero edge alias can survive only on a degenerate
wall, with at least one edge angle zero. Since all local angles
are nonnegative there, every tetrahedron incident to that edge
has a zero angle and zero volume. The remaining face source is
lower dimensional, but its TOTAL period or volume is not bounded
by the preceding argument. Its original quantum source terms
must still be retained. In particular a bound for the positive
interior modes does not prove a bound for every degenerate wall.

The proposed universal extension to all weak wrong-edge loci is now
**FALSE**, as proved by the
[certified positive-geometric counterexample](positive_geometric_alias_volume_counterexample.md).
Six legal positive 2-to-3 moves on the same 5_2 knot give a
nine-tetrahedron positive complete triangulation. A rational weak alias
angle assignment has volume 3.76403683049..., exceeding the complete
hyperbolic volume 2.82812208833.... Its complete marked meridian angle is
exactly zero, and its full marked defect is Bm for an explicitly retained
integer m, with det B=-2. Thus this is not an artifact of dropping the
peripheral equation or enlarging the integer alias lattice.

Here the strictly positive wrong-edge locus is EMPTY. The weak locus is
not the topological closure of a nonempty positive cell, so the preceding
positive-peripheral-alias theorem is unchanged. No coefficient of the
oversized weak locus in the original quantum source has been computed.
The counterexample therefore refutes universal FACE VOLUME domination;
it does not assert an oversized original quantum period. Source exclusion
or exact Ward/sewing cancellation remains necessary wherever such a
weak locus is encountered. Compact radial clipping alone does not give
the false comparison between different integer-shifted potentials.

An independent useful sufficient bound remains: if s_min is the minimum
number of DISTINCT tetrahedra incident to an edge, every wrong-edge weak
locus has volume at most (t-s_min)v_3. The
[star-bound note](degenerate_alias_faces_and_repair_obstructions.md)
proves this and supplies exact counterexamples to universal flat-only
repair and to an automatic favorable sign of complete edge multipliers.

## 7. Tests against the actual source and the critical-path consequence

The [original figure-eight counterchart](positive_quad_chart_and_actual_torus_signature.md)
has an indefinite angular Hessian on a valid transverse slice.
It does not satisfy (8). Choosing new radii in that original
chart cannot make this theorem apply. A source-preserving
change to the positive quad chart is still necessary.

The [selected five-crossing proof](five_two_selected_volume_proof.md)
also needed a bent outer source and bounded lower/vertical
pieces. That source theorem is not a consequence of (16).
It verified exactly the face and kernel terms that a
critical-point-only argument would miss.

The new general advance is the explicit algebraic Legendre
chain (5)--(7), its nonvanishing Jacobian and Schur-closed
positive Hessian, and the radial homotopy (13)--(15) with a
proved boundary gap. The target contour on every supplied
positive triangulation is no longer guessed. What remains
for a broad original-knot theorem is its exact quantum source
transport, with the alias face periods in Section 6 retained.
No broad volume conjecture is claimed proved by this lemma.

There is a simple exact check on the word "automatic" in the
boundary claim. In the scalar positive potential C=0,
kappa=2pi/3, the angle interval is

    0<theta<pi/3, gamma=2pi/3, beta=pi/3-theta.

Its positive critical point is theta_*=pi/6,
rho_*=-log(3)/2 and V_*=2v_3/3. But at the arbitrary initial
radius rho_0=0, the angle endpoint theta=pi/3 has

    F(0,pi/3)=Im Li_2(exp(pi i/3))=v_3>V_*.

The equalities follow from the ordinary Lobachevsky duplication
identity. Thus radial boundary prisms from an arbitrary starting
source radius need not be lower, even though the whole positive
volume problem is strictly concave. This is a test of the analytic
positive Lagrangian data, not a claim that this one-tetrahedron
data is an actual knot triangulation or a substituted quantum
invariant. It proves why (13) specifies rho_* and why the missing
original-source transport cannot be supplied by concavity alone.

The underlying angle-volume and Legendre viewpoints have the coverage
already recorded in [the Rivin/flow note](rivin_flow_and_quantum_source.md).
No novelty is claimed for Legendre duality or for the positive
symplectic Hessian. The explicit whole off-critical chain, its
boundary-prism inequality, algebraic phase graph and alias escape
are proved here from the displayed formulas, without adopting a
published quantum-cycle comparison.

[All-rank identity and scope audit](../experiments/audit_general_legendre_rivin_contour.py)
and [saved results](../experiments/general_legendre_rivin_contour_results.json).
