# Strict representation-volume loss from an actual kernel

30 October 2026. This proves a geometric implication
once the source capacity has been identified with the indicated
representation volume. It does not identify smoothed blocks with JSJ
pieces or supply that representation by itself.

## 1. Statement and the exact radial construction

Let X=Gamma\H^3 be oriented, complete and finite-volume. Let
rho:Gamma->SL2(C), followed by its action on H^3. Its peripheral
matrix images commute. In this note ker(rho) means the kernel of
that PSL2 action, so a central sign is retained as acting trivially.
Use the
equivariant map f already constructed in the
[general-peripheral volume proof](general_peripheral_representation_volume_bound.md):
on each sufficiently deep axis cusp it is exactly

    f(w,y)=gamma(chi(w)+log y),

and on a parabolic cusp, after target normalization, it is

    f(w,y)=(A w,y).

Here chi is real-linear, A is real-linear, and neither is assumed
injective. Central peripheral images are included in the axis case
chi=0. The parabolic affine height constant could be retained and
does not affect the arguments. Extend f smoothly on the compact core.

The conclusion is:

    Vol(rho)=Vol(X)  =>  ker(rho) is trivial.         (1)

Orientation reversal gives the same statement for absolute equality.
Together with the non-strict bound derived below from the same maps,
a nontrivial kernel therefore gives |Vol(rho)|<Vol(X).

For a REAL parameter s>2 put

    Z_s=integral_H3 exp(-s d(x,y))dy,
    nu_x^s=Z_s^-1 integral_H3 exp(-s d(x,y)) mu_(f(y))dy,

where mu_z is the probability visual measure at z on the target ideal
sphere. Z_s is independent of x. These are rho-equivariant probability
measures. They have no atoms: each visual measure has none and Tonelli
applies. Their Busemann potentials are finite, strictly convex, and
proper, so their barycenters F_s(x) exist uniquely. Properness follows
directly from nonatomicity: choose uniformly small spherical caps of
mass<1/4, and compare Busemann growth along rays outside such a cap.
Strict convexity follows because the support is not contained in the
two endpoints of one geodesic. Thus F_s is rho-equivariant.

Write v_xi=grad B_xi at F_s(x), eta_y=grad_x d(x,y), and use the
joint probability measure in the definition of nu_x^s. Set

    H=E[v v^T],  B=I-H,  A=E[v eta^T].

The hyperbolic Busemann identity Hess B_xi=I-v_xi v_xi^T and
differentiation of the barycenter equation give EXACTLY

    B DF_s=s A.                                    (2)

Radial symmetry on the DOMAIN gives E[eta eta^T]=I/3, regardless
of f. Hence matrix Cauchy--Schwarz gives AA^T<=H/3 and

    |Jac F_s| <= s^3/(3sqrt3) sqrt(det H)/det(I-H)
              <= (s/2)^3.                          (3)

The last scalar inequality holds for nonnegative eigenvalues
lambda_1+lambda_2+lambda_3=1. Its maximum is attained only when
all lambdas=1/3. To check this without an external rigidity theorem,
differentiate log[det(I-H)/sqrt(det H)] under that constraint.
An interior critical point has at most two distinct eigenvalues;
on (t,t,1-2t) the ratio is 2(1-t)^2/sqrt(1-2t), minimized uniquely
at t=1/3. The boundary liminf is at least2, larger than
8/(3sqrt3); other boundary approaches have infinite ratio.

For s in (2,3], the first two x-derivatives of nu_x^s have uniformly
bounded total variation. Indeed derivatives of exp(-s d) cost bounded
powers of s and at second order at most coth d. The radial integral
of its 1/d singularity is finite. More explicitly,

    Z_s=8pi/[s(s^2-4)],  E_radial[coth d]=s/2,

so the second-derivative norm is at most 3s^2/2. This also justifies differentiating the radial integral and
gives the local C^2 estimates used below whenever B is uniformly
positive. No global Lipschitz bound for F_s is asserted.

## 2. Cusp control, retaining the potentially large axial shift

Fix s>2 throughout this section; its constants need not be uniform
as s decreases to2. Let x=(w,y) lie in a chosen deep lifted cusp
horoball H={y>Y}. Its kernel mass outside H is bounded by

    zeta(y)<=C_s y^(-(s-2)).                        (4)

This follows because the distance from x to the complement is
log(y/Y), while the radial tail is bounded by
C_s exp[-(s-2)log(y/Y)]. First physical-w derivatives of the entire
kernel have total variation at most s/y, since the physical vector
partial_w has hyperbolic norm1/y.

### Axis cusp with nonzero chi

Conditioning the kernel on H gives a rotationally symmetric mixture
of visual measures whose centers lie on the SAME target axis.
At a target point with distance rho from the axis, every rotationally
symmetric probability measure has outward radial Busemann derivative
at least tanh(rho/2). This can be checked one azimuthal circle at a
time: its averaged potential is

    log[(cosh rho+sqrt(cosh^2 rho-b^2 sinh^2 rho))/2],
    0<=b<=1,

whose radial derivative is minimized at b=1 and equals tanh(rho/2).
The outside mass contributes a gradient of norm at most zeta. The
barycenter equation therefore implies

    dist(F_s(w,y),axis)<=C_s zeta(y).                (5)

This conclusion does NOT require control of its axial displacement.

Here is the needed axial estimate. Scale domain coordinates by
w'=w+y u, y'=y v. The conditional axis-center coordinate is

    chi(w)+log y + y chi(u)+log v,

and its density in (u,v) is proportional to

    exp[-s d((0,1),(u,v))] du dv/v^3, v>Y/y.         (6)

The distribution of the center coordinate divided by y converges
to that of chi(u). Its latter density is continuous, symmetric and
strictly positive near zero. These facts follow by integrating the
positive density in (6); tails are integrable because s>2.

For clarity, the visual average of the Busemann potential on an axis
at distance t from its visual center is

    h(t)=t coth t-1,
    h'(t)=coth t-t csch^2 t,
    h''(t)=2 csch^2 t(t coth t-1)>0.                (7)

Its derivative tends to the sign function. Thus the axial force
of the conditioned measure, evaluated at
chi(w)+log y+y a, converges to the strictly increasing median-force
function of chi(u), uniformly on a small fixed a-interval. Equation
(5) and the full barycenter equation imply that its axial force at
the actual F_s is O(zeta). Explicitly, compare at the nearest axis
point by radial parallel transport: the Busemann gradient has derivative
norm at most1, and the normalized axial unit vectors differ by O(rho).
Thus (5) changes that force component by only O(zeta).
Consequently the actual axial coordinate
lies in that central interval for all sufficiently large y.

There is a quantitative lower bound which is stronger than a formal
perturbation claim. Restrict v to [1,2], the coordinate of u orthogonal
to chi to a fixed compact interval, and chi(u) to the interval of
width2/y placing the axis center within distance1 of the actual axial
coordinate. On this compact part of (6) the density is bounded below.
It therefore has mass at least c_s/y. By (5), every such visual center
is within target distance2 of F_s. Its visual measure has density
bounded below by a fixed positive multiple of mu_(F_s). Since the
visual average of Hess Busemann at its own basepoint is (2/3)I,

    B(F_s(w,y)) >= (c_s/y) I.                       (8)

This bound survives arbitrary coupling of axial and transverse
derivatives: it is a lower bound on the WHOLE Hessian, not just one
diagonal entry. Combining (8), (2), and the raw physical-w kernel
derivative bound gives

    ||partial_(w_j) F_s|| <= C_s.                  (9)

One can also recover an axial displacement O(zeta y) relative to the
conditioned axial barycenter from (7), but it need not tend to zero
and is not used in (8)--(9). In particular this argument does not
compare an O(zeta) perturbation to an O(1/y) gap as if it were small.

In Fermi coordinates (rho,theta,t) about the target axis the invariant
primitive of hyperbolic volume is

    beta_ax=(1/2)sinh^2 rho dtheta wedge dt,
    ||beta_ax||=(1/2)tanh rho.                     (10)

It is invariant under every axial translation and rotation, and is
smooth across the axis. Equations(5),(9) imply

    integral_(fundamental cusp torus at y)|F_s^*beta_ax|
                                          <=C_s zeta(y)->0. (11)

### Central axis and parabolic cusps

When chi=0, after translating the target by log y, the conditioned
measure converges in total variation to the mixture of visual measures
at gamma(log v) with the full density(6). It has full support and a
strictly positive barycenter Hessian. The outside mass tends to zero,
so barycenters and Hessians converge in this normalization. Therefore
the physical-w derivatives are O_s(1/y). The flux(11) again vanishes.

For a parabolic cusp the same scaling changes f(w+y u,y v) to
(A u,v) after the target translation by A w and dilation by y.
The conditioned measure converges in total variation to the fixed
full-support mixture at (A u,v). Its barycenter is at a fixed positive
height and its Hessian is positive. The outside mass is o(1), so the
full barycenter stays near it in scaled coordinates. In particular
||partial_(w_j)F_s||=O_s(1/y). The invariant primitive

    beta_par=-(1/2)height^-2 dx_1 wedge dx_2,
    ||beta_par||=1/2

then gives a cusp-torus flux O_s(y^-2). This includes rank-deficient A.

The continuity used in these two normalized cases is elementary:
the fixed nonatomic limit assigns mass less than1/8 to all sufficiently
small spherical caps. Total-variation convergence makes their masses
less than1/4 uniformly. The Busemann potentials are then uniformly
proper by the same ray estimate as in section1, confining their
barycenters to a compact set. On that set the potentials and their
fixed derivatives converge; strict convexity gives the asserted
barycenter and Hessian convergence.

### Identification of the integral

The absolute Jacobian bound(3) makes F_s^*vol integrable. Compare it
to the original cusp-adapted f on a truncated core using an equivariant
homotopy. On each cusp the target volume form has the invariant
primitive just displayed. The boundary homotopy integral is exactly
the difference of the two primitive fluxes; paired fundamental sides
cancel by invariance. Both fluxes tend to zero by (11) and its
parabolic version, and by the explicit original f. Stokes therefore
proves, separately for EACH fixed s>2,

    integral_X F_s^*vol = Vol(rho).                 (12)

No limit in s was exchanged with a cusp estimate.
Combining(3) and(12) gives directly, for every s>2,

    |Vol(rho)| <= (s/2)^3 Vol(X).

Letting s decrease to2 proves the non-strict bound used here. Thus
this note does not depend on the old smearing proof of that inequality;
the linked peripheral note supplies the canonical regulator-volume
normalization and the original cusp-adapted map.

## 3. Equality forces an isometric limit and excludes a kernel

Assume Vol(rho)=Vol(X)>0 and take s_j decreasing to2. Equations(3),(12)
give the nonnegative deficit

    integral_X [(s_j/2)^3-Jac F_(s_j)]
                 =[(s_j/2)^3-1]Vol(X) ->0.         (13)

On any fixed compact ball there are points x_j tending along a
subsequence to x_0 with Jac F_(s_j)(x_j)->1. The strict maximum in
(3) forces H(x_j)->I/3. Moreover AA^T<=H/3 and (2) imply that all
singular values of DF_(s_j)(x_j) tend to1; their product has positive
sign. This uses no assumed convergence of rho or of the map values.

Postcompose each map by a target isometry sending F_(s_j)(x_j) to
one fixed point. Call the maps G_j. A kernel element of rho still
acts trivially on EVERY G_j, even though these normalizing isometries
can diverge. We only need this kernel-invariance, not convergence of
the conjugated representations.

There is one fixed source radius on which the G_j have uniform C^2
bounds. Indeed whenever B>=kappa I, equation(2) bounds DF by C/kappa;
differentiating H bounds its derivative by C(1+||DF||). Starting at
H near I/3, a fixed-radius bootstrap preserves B>=kappa. The uniform
first and second measure-derivative bounds after(3), together with
bounded target Busemann derivatives, then bound second derivatives
of G_j. Arzela compactness gives a C^1 limit on that ball.

On the ball the deficit tends to zero in L1 by(13), while C^1
compactness makes the Jacobians converge uniformly. The limiting
Jacobian is1 everywhere. The strict matrix inequality in(3) now
forces its derivative to be an orientation-preserving isometry at
every point. Thus the limit is a local hyperbolic isometry.

This convergence propagates across any fixed finite chain of
overlapping source balls. At a point in the known overlap, uniform
Jacobian convergence again forces H_j->I/3, so the same bootstrap
opens the next ball with the same radius and bounded target values.
Finite covers of paths, then a diagonal exhaustion, give a global
local-isometry limit G_infinity:H^3->H^3. Equivalently, its initially
fixed local isometry extends uniquely along paths; H^3 is simply
connected and complete, so it is a global isometry.

If gamma is in ker(rho), then G_j(gamma x)=G_j(x) exactly. Choose a
compact path from x to gamma x and pass to this same limit. The
global isometry would satisfy G_infinity(gamma x)=G_infinity(x),
forcing gamma=1. This proves(1). Reducible escape cannot evade the
argument: target normalization was explicit and kernel-invariance
survives it. Negative maximal volume is handled by a fixed target
orientation reversal before the construction.

## 4. The actual regular-smoothing corollary

Suppose a nonempty set of untwisted crossing-circle components of the
original connected certified augmented exterior X is deleted by the
literal identity smoothing, and the resulting connected diagram has
its OWN positive labeled right-angled certificate. Retain every
remaining half twist and the original peripheral labels. Let Y be
that actual complete smoothed exterior. Its core source capacity is
Vol(Y)/(2pi), by the independently proved face-coefficient and coning
normalization. No abstract existence theorem supplies this certificate.
For example, when the entire literal smoothed white cellulation is
one simple triangulated sphere with at least four vertices, the
[capacity-block construction](actual_smoothed_source_capacity_blocks.md),
section4, supplies exactly this labeled certificate by its proved
Hall, disk-development, and supporting-halfspace argument.

The topological operation is meridional Dehn filling of precisely the
deleted crossing-circle components: their original crossing disks
fix the slope, and the untwisted physical strands keep their original
pairing. Compose the induced quotient pi_1(X)->pi_1(Y) with the actual
complete holonomy of Y. This representation rho has nontrivial kernel:
each deleted meridian was an essential nontrivial parabolic in the
original certified complete exterior, and becomes trivial after filling.

Its absolute representation volume is EXACTLY Vol(Y), with the same
orientation. To check the normalization, first replace the axis cusp
map gamma(chi(w)+log y) on each filled cusp by gamma(chi(w)), using
an axis-valued homotopy and a collar. Its boundary homotopy has zero
3-volume, so the representation volume is unchanged. Unlike the old
log y map, the new map extends continuously over the filled solid
torus by its longitude core map. The extension has rank at most one
and contributes zero volume. It does not require that the image core
curve be embedded or even nontrivial.

A filled core image may instead be parabolic. Because the killed
meridian is in its kernel, its real-linear translation map A has rank
at most one. Replace the cusp map (A w,y) by (A w,1). The vertical
homotopy lies in the vertical plane over that one translation line,
so its rank is at most two and its 3-volume is zero. The new map
extends over the filled solid torus by the rank-one longitude map
along that horocycle. A central image is included by taking A=0.
Thus the same zero-volume filling-cap argument covers every possible
commuting peripheral image of the actual quotient.

On the remaining cusps keep the actual complete parabolic markings
and their conical maps. The extended map from the filled topological
exterior to Y induces the identity on its fundamental group and agrees
with the actual peripheral homotopy classes. Since the universal
cover of Y is contractible, it is properly homotopic to the actual
identification with Y, using the conical maps on the remaining ends.
It therefore has degree one. Integration of the target volume form,
or Stokes on truncated cores followed by the already proved vanishing
horospherical boundary terms, gives Vol(rho)=Vol(Y).

Applying(1) and the bound just proved now yields the STRICT comparison

    Phi_sm=Vol(Y)/(2pi)<Vol(X)/(2pi)=Phi_old.        (14)

This needs neither a balanced split nor the original packing variables
to remain fixed. At the attained smoothed packing the gap is positive.
Replacing its marked zero variables by sufficiently small fixed
positive ones preserves a strict gap, with their target exponents
still zero. For a single port, the
[actual polynomial small-circle insertion](actual_small_circle_polynomial_face_insertion.md)
therefore gives the corresponding full-source small-h upper gap with
cost C^(h-1). For a connected untwisted subset covered by the
[simultaneous polynomial correspondence](actual_simultaneous_small_circle_face_correspondence.md),
the cost is product C_i^(h_i-1), including protected outgoing faces
and dependency cycles. These are applications of that exact source
theorem; disconnected smoothings and signed small ports remain outside
this corollary.

## 5. Scope still needed for degenerate smoothing

To apply this geometric strictness result to the actual smoothed
capacity one must construct a representation of the original
complete source group whose volume is the sum of the proved capacity
blocks, and show that the actual essential deleted crossing meridian
lies in its kernel. For a connected certified hyperbolic smoothed
exterior this is the literal filling quotient and its marked volume
normalization. For a degenerate block decomposition it still requires
the actual gluing/peripheral argument. No quantum source product or
unproved JSJ identification is substituted here.

## 6. Literature coverage and validation

Maximal representation-volume rigidity is established territory. The
abstract of [Francaviglia, *Hyperbolic volume of representations of fundamental groups of cusped 3-manifolds*](https://arxiv.org/abs/math/0305275)
states a stronger discrete-and-faithful conclusion at maximal volume.
That reference is coverage and attribution only. The construction,
matrix bound, cusp-flux control, and kernel-exclusion argument above
are supplied here rather than importing that theorem's proof. No
novelty claim is made for natural-map volume rigidity.

The smoothing corollary requires its exact certificate, marking and untwisted polynomial-insertion hypotheses. It does not construct a representation from a degenerate block sum or bound signed small ports.