# The source point is the Casson--Rivin maximum for the actual filling

**Current scope and direct geometric input.** The
[whole-color improvement](actual_pretzel_all_width_extension.md) lowers
the odd-width threshold to s>=9. The
[direct ideal-chart certificate](actual_pretzel_positive_ideal_angle_certificate.md)
constructs a compatible positive ideal subdivision of the ACTUAL
half-twisted cells and verifies the full edge/peripheral rank. Thus the
variational proof for this class no longer requires a general ideal
triangulation existence theorem. The
[general source certificate](source_volume_casson_rivin_certificate.md)
and [independent tangent audit](source_angle_stationarity_critical_audit.md)
isolate precisely why stationarity holds on the entire angle slice.

29 October 2026. This records the variational equality argument requested
by the user. The relevant volume is Vsrc_s(p), not the larger complete
augmented volume V_s. The angle constraints must be those of the actual
filled slopes. A maximum for the unfilled cusp problem would not prove
the desired equality.

The geometric completion inputs are the [positive-core construction](actual_long_pretzel_geometric_filling_completion.md),
the [primitive angle certificate](actual_long_pretzel_primitive_filling_angle.md)
and the [log-link/tube lemma](long_pretzel_equality_critical_audit.md).
Their proofs and independent reviews now accompany this note;
stationarity is not substituted for smooth end completion. The
[completion audit](long_pretzel_volume_equality_completion_audit.md)
records the full original-source equality and its exact scope.

## 1. The essential established quantum inputs

For each fixed odd s>=9 and independently sufficiently large fixed
signed integers p_i, the [whole original source theorem](actual_long_pretzel_full_source_survival.md)
with the subsequent [width improvement](actual_pretzel_all_width_extension.md) gives

    Kraw_N=N^(3/2) exp[-is*pi*(N-1)/4] kappa^(-sum p_i)
                   D_s(p) exp[N A_s(p)] (1+O_(s,p)(1/N)),
    D_s(p)!=0.

The original reduced Kashaev invariant has the same absolute value.
Thus its limit already exists and equals Vsrc_s(p)=2pi Re A_s(p).
The steps that matter for this conclusion are:

1. Exact source transformations retain the original marked derivative
   channels, all colors, peripheral factors and Cartan phases.
2. The inner sums are combined coherently before estimating them. The
   global alias/core gap controls every color outside the cusp corridor.
3. The corridor has an exact complex analytic packet, not merely a
   pointwise real-grid approximation. This permits the contour estimates.
4. The exact filling transform retains every endpoint current. Its zero
   charge vanishes and its minimal nonzero signed charges add. This
   establishes the nonzero coefficient for the entire source.
5. The [literal port lift](actual_pretzel_port_lift_and_geometric_anchor.md)
   and [marked regulator comparison](actual_pretzel_marked_regulator_and_filling_action.md)
   supply an actual representation rho_p of the filled knot group and
   the absolute identity Vsrc_s(p)=Vol(rho_p), with the complete oriented
   augmented holonomy as anchor.

Neither Cauchy alone nor existence of a classical stationary point
establishes steps2--4. They are already supplied by the linked analytic
proofs. The present task is the classical equality for this selected
representation.

## 2. Obtain a positive ideal angle point from the selected source

Let Y_s be the original complete augmented link complement. Choose a
fixed positive geometric ideal triangulation T of Y_s. The
[direct subdivision certificate](actual_pretzel_positive_ideal_angle_certificate.md),
sections 1--3, supplies it from the actual face-labeled polyhedra:
normalized light lifts are preserved by every white and shaded face
pairing, and a finite compatible affine subdivision gives nonflat ideal
tetrahedra. This uses no general triangulation existence theorem.
Here "positive" means every oriented tetrahedron has shape in the
upper half-plane; it is stronger than a topological ideal triangulation.
The direct finite-center completion proof does not depend on this
all-ideal existence input, but it supplies the customary Casson--Rivin
angle presentation used in this note.

Transport the finitely many developed ideal vertices of T using the
actual source representation rho_z and its selected peripheral flags.
At z=0 this is exactly the geometric developing configuration. A
peripheral flag tends continuously to its noncentral parabolic flag:
in a bounded matrix frame the eigenspace kernel has rank one at the
limit, so it admits a local continuous, indeed holomorphic, choice.
Every vertex orbit is well defined because its peripheral stabilizer
fixes the chosen flag.

All cross-ratios of the finitely many tetrahedra therefore vary
continuously from strictly positive shapes. Shrink the parameter
neighborhood once so every shape remains positive and nondegenerate.
The actual representation identities telescope to the complex edge
gluing equations. The edge angular sums are continuously close to
2pi and are integral multiples of 2pi, hence are exactly 2pi. The
marked peripheral products are the actual eigenvalue multipliers.

The selected filling points approach z=0 uniformly as
max_i |p_i|^(-1) tends to zero. One threshold therefore puts ALL
independently signed sufficiently long tuples in this fixed positive
shape neighborhood. No comparability between different slopes is used.
Denote their positive angle points by theta_p.

## 3. The correct affine volume problem includes the filled slopes

For each tetrahedron write its positive angles as alpha,beta,gamma,
with alpha+beta+gamma=pi. Let

    V_T(theta)=sum_t [Lambda(alpha_t)+Lambda(beta_t)+Lambda(gamma_t)],
    Lambda'(a)=-log(2sin a).

The edge constraints are the usual linear equations with sum2pi at
each edge. Fix their original angle and peripheral log lifts, continued
from the complete triangulation. In projective geometric coordinates
the actual auxiliary logs are

    U_i=Log(M_i^2)=-z_i,
    V_i=Log(lambda_i^2), centered at completeness,=-2ell_i.

Their imaginary parts are affine real-linear functions of the
tetrahedral angles in this fixed marking. The old SL longitude sign
is retained in the quantum/regulator comparison; it is not an extra
geometric rotation here. By the primitive-angle certificate the
selected all-positive unit charge has

    U_i+p_i V_i=-2pi i.                                  (1)

Other minimal signed charges replace the right side by -2pi i m_i,
|m_i|=1, on their corresponding eigenflag marks. It suffices to use
the all-positive charge, whose nonzero contribution is already proved.

Define A_p to be the positive angle polytope satisfying the tetrahedral
and edge equations, the REAL linear filling-angle constraints

    Im U_i+p_i Im V_i=-2pi,  i=1,...,s,                 (2)

and Im U_0=0 on a chosen primitive meridian of the remaining main cusp.
The latter cusp is actually fully parabolic in rho_p, so U_0=V_0=0.
The source point theta_p belongs to the INTERIOR of this affine slice.

The full nonlinear holonomy equations are not being imposed as convex
constraints. Only their imaginary, angle-linear parts define A_p.
The real parts will give stationarity of volume.

## 4. The source equations imply stationarity on the entire angle slice

Set x_t=Log z_t and y_t=Log z_t'', z_t''=1-z_t^(-1), with
Im x_t=alpha_t and Im y_t=gamma_t. The sine rule gives

    Re x_t=log(sin beta_t/sin gamma_t),
    Re y_t=log(sin alpha_t/sin beta_t).

For EVERY infinitesimal angle variation, not merely a variation through
geometric solutions, direct differentiation gives

    dV_T(delta theta)=sum_t [Re x_t delta gamma_t
                                      -Re y_t delta alpha_t]. (3)

Let E be the real space of edge Hamiltonians in the standard shape
symplectic space Omega=sum dx_t wedge dy_t. Both the real logarithmic
shape vector of a gluing solution and any tangent satisfying the edge
angle equations lie in E^perp. The already established
[boundary pairing](bloch_lift_and_boundary_torsor.md), summed over the
boundary tori, reduces Omega there to

    Omega_red=-(1/2)sum_i dU_i wedge dV_i.

Distinct tori have zero intersection pairing; on each torus the
primitive peripheral rows have pairing -2. Thus at theta_p equation(3)
becomes the boundary formula for arbitrary angle tangents

    dV_T(delta theta)
      =(1/2)sum_i [Re V_i delta Im U_i
                                      -Re U_i delta Im V_i]. (4)

This is not obtained by restricting the derivative to the smaller
variety of full complex gluing solutions. The coisotropic pairing
justifies its use for every tangent of A_p.

For each filled cusp, the real part of(1) says

    Re U_i=-p_i Re V_i.

Its contribution to(4) is therefore

    (1/2)Re V_i [delta Im U_i+p_i delta Im V_i]=0

by(2). The main cusp contributes zero because U_0=V_0=0. Consequently

    dV_T(theta_p)|_(T_theta_p A_p)=0.                    (5)

This is the full constrained critical-point condition requested in
the Casson--Rivin argument. It uses the actual filled slopes and
their centered integer angles, rather than the unfilled cusp maximum.

## 5. Strict concavity makes this the unique global maximum

On one tetrahedron, in coordinates alpha,gamma with
beta=pi-alpha-gamma, the negative Hessian is

    [[cot alpha+cot beta, cot beta],
     [cot beta, cot gamma+cot beta]].                    (6)

Its determinant is1. Its first diagonal entry equals
sin(gamma)/(sin(alpha)sin(beta))>0. It is positive definite on the
entire positive angle simplex. Summing proves strict concavity of
V_T on every affine angle slice, including A_p.

For any other point of the closure of A_p, the straight segment from
theta_p stays positive until its possible final endpoint. Along it
the first derivative starts at zero by(5), and the second derivative
is strictly negative unless the point is unchanged. Continuity of
Lambda at the boundary then gives

    V_T(theta)<V_T(theta_p),  theta!=theta_p.             (7)

Thus the source point is the UNIQUE global maximizer of the full
filled-slope angle polytope, including its boundary. No gradient-flow
convergence assumption or numerical maximum is required.

## 6. Smooth completion identifies the maximum with hyperbolic volume

The value of the positive developed fundamental triangulation is

    V_T(theta_p)=D(beta(rho_p))=Vsrc_s(p).                (8)

Here the absolute marked regulator comparison fixes the constant;
one is not defining an unknown source action to be volume.

For completeness, the geometric content behind the generalized
Casson--Rivin conclusion is proved directly by the companion notes.
The positive finite-center deformation supplies a local hyperbolic
metric on the same compact core. Its auxiliary cusp links are positive
Euclidean similarity tori. After placing their chosen flags at infinity,
the second common affine fixed point q escapes to infinity near the
complete structure. The finite link development avoids q. Therefore
Log(dev-q) gives a nonsingular translation structure on a COMPACT torus.
Its flat metric is complete, so its universal developing map is the
whole complex plane, with its actual rank-two period lattice.

The end contains a full punctured hyperbolic tube. The
[primitive-angle certificate](actual_long_pretzel_primitive_filling_angle.md)
proves that its actual meridian period is exactly -2pi i, not that
integer merely modulo2pi. Hence the tube completes to a smooth solid
torus with the specified primitive slope. The main cusp stays complete.
The [tube lemma](long_pretzel_equality_critical_audit.md) proves both
the degree-one statement and the finite-volume completion.

The resulting complete oriented metric g_p is on the ACTUAL filled
knot complement. Its holonomy is rho_p. This supplies the geometric
equality certificate that strict concavity or scalar PSL holonomy alone
would not provide.

The user's Gromov-norm observation gives a short final comparison.
Apply the independently proved [sharp representation-volume inequality](regular_critical_values_and_representation_volume_bound.md)
with the specified hyperbolic metric g_hyp as domain and g_p holonomy
as target. Then reverse their roles using the same oriented topological
marking. Fundamental chains have degree one in both directions, so

    Vol(g_p)<=Vol(g_hyp),  Vol(g_hyp)<=Vol(g_p).

No separate unproved equality case of the norm inequality is invoked.
These two inequalities prove

    Vsrc_s(p)=max_(theta in A_p) V_T(theta)
                         =Vol(g_p)=Vol(S^3 minus K).     (9)

## 7. Quantum conclusion and quantifiers

Combining(9) with the whole-source asymptotic and the independently
audited positive-core, primitive-period and tube certificates proves
the requested original-invariant equality:

    lim_(N->infinity) (2pi/N)log|<K>_N|=Vol(S^3 minus K).

With the later whole-color improvement, the class is each fixed odd
width s>=9, all independently
sufficiently large fixed signed p_i, the original boxes R^(-(2p_i+1)),
and the standing hyperbolicity assumption. The common threshold may
increase to place the selected source points inside the fixed geometric
neighborhood. There is no upper bound on width across the class, no
comparability or common-sign condition on the slopes, and no restriction
to prime levels or one parity. This note does not assert the quantum
limit for all hyperbolic knots or for slopes growing with N.

## 8. Literature coverage, not a proof premise

The [Futer--Gueritaud survey](https://arxiv.org/abs/1004.0440)
describes Casson--Rivin's critical-volume characterization of hyperbolic
structures. That classical variational framework is established
territory; this note does not claim to invent it. The contribution
needed for this project is verifying its hypotheses for the point
selected by the ENTIRE original quantum source, with the actual filled
slopes and marked logarithms. Equations(3)--(7) and the companion
geometric completion arguments are proved here rather than imported
from the survey. The geometric ideal-triangulation input used for this
angle presentation is the previously audited argument of
[Ge, version1](https://arxiv.org/abs/2609.27635v1); the independent
finite-center completion route avoids making that input necessary
for the final volume equality itself.
