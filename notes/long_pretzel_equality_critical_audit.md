# Equality audit: positive geometric core and primitive tube completion

29 October 2026. The whole-source theorem already fixes a nonzero limit
equal to the regulator of an explicit filled representation. A sharp
representation-volume bound does NOT make that representation geometric.
This note isolates and proves the remaining local END-completion lemma.
It uses a positive geometric deformation of the compact core, not an
unfilled Casson--Rivin maximum and not convergence of volumes alone.

## 1. Exact inputs needed from the original source

For each fixed odd s>=25 the
[whole original source theorem](actual_long_pretzel_full_source_survival.md)
provides a nonzero asymptotic at every independently sufficiently long
fixed signed tuple p. Its constants may depend on s and that fixed tuple;
there is no assertion uniform in slopes growing with N. All auxiliary
colors, both root parities, the middle color, every normal jet, and the
original single marked source are retained there.

The [literal port theorem](actual_pretzel_port_lift_and_geometric_anchor.md)
constructs rho_z of the ACTUAL augmented-link group. It includes the
right-to-left cap order, rather than a permutation of arbitrary pretzel
boxes. At z=0 its complete main and auxiliary generators are the oriented
four-antiprism geometric holonomy. The
[preferred-peripheral certificate](actual_mixed_crossing_circle_preferred_longitude.md)
fixes M_i=H_i^(-1/2), lambda_i=-L_i^(-1), including the ordinary-circle
spin. The [regulator comparison](actual_pretzel_marked_regulator_and_filling_action.md)
then gives, at a selected filling point,

    source rate = Vol(rho_p).

For equality with the manifold volume one needs more than the facts that
rho_p kills the slope and Vol(rho_p) tends to the augmented volume. The
two additional geometric inputs used below are precise:

* A FIXED finite partially ideal geometric triangulation of the complete
  augmented manifold, every tetrahedron strictly positive. Finite face
  and cell centers are allowed. An arbitrary ideal topological
  triangulation is insufficient.
* Transporting its vertex orbits by rho_z and the selected cusp flags
  gives a nearby positive developing triangulation with local degree one
  at its finite faces, edges and vertices. Equivariance and the local
  degree statement concern the SAME original marked manifold.

The finite-center construction of this input is proved in
[the geometric-core and filling theorem](actual_long_pretzel_geometric_filling_completion.md),
sections2--4. It has been independently read in full: matched face-center
fans and finite cell centers give24s positive tetrahedra, exact
contractible edge transitions remove both screw and cone defects, and
the finite spherical links have degree one. The result below is
independent of whether an all-ideal positive subdivision is available.

## 2. A compact affine link becomes an honest translation torus

Consider one ideal end of such a positive developing triangulation.
Its oriented link is a compact torus T. Sending the selected peripheral
fixed flag to infinity identifies the link triangles with Euclidean
triangles and their transitions with orientation-preserving complex
similarities. Its developing map

    d: universal_cover(T) -> C

is a local homeomorphism, including at the link vertices. Local degree
one and the positive Euclidean angle sums are essential here.

Suppose the peripheral affine holonomies have a common finite fixed
point q. Assume d avoids q. On the simply connected cover choose

    f=Log(d-q).

The differential df is invariant under the deck group, because an affine
holonomy has d-q -> a_gamma(d-q). It is everywhere nonsingular. Thus

    |df|^2                                                   (1)

is a nonsingular Euclidean metric on the COMPACT torus T. It is complete.
The lifted f is a local isometry from its complete simply connected
Euclidean cover to C; it is a global isometry. To see this directly,
lift every straight segment starting at f(x). The corresponding unit
speed geodesic exists for the whole segment by completeness. This proves
surjectivity and path lifting; since C is simply connected, the local
isometry is a one-sheeted covering.

Consequently f gives a global coordinate on the link cover. Its deck
translations form a rank-two lattice

    Lambda={L_gamma : f(gamma x)=f(x)+L_gamma}.              (2)

The map pi_1(T)->Lambda is injective. Rank one or a nonzero deck element
with zero period would contradict the compact flat-torus quotient.
This argument controls the DEGREE of the logarithmic development, not
just its local derivative.

### Why q is avoided in the selected near-complete family

Choose the peripheral flag normalization continuously from the complete
geometric cusp. A fixed fundamental union of link triangles has bounded
developed image, uniformly near completeness. A meridian has affine form

    d -> a d+b, a ->1, b -> b_0!=0.

When a!=1 its common finite fixed point is q=b/(1-a), so q goes to
infinity. For sufficiently small deformation it misses that entire
finite fundamental image. Every other developed triangle is its affine
translate; the holonomy fixes q, so none of those triangles meets q
either. This proves the hypothesis globally on the link cover.

The selected source family approaches the base uniformly as
max_i |p_i|^(-1) goes to zero. Therefore one small geometric neighborhood
works for independently unequal signed sufficiently long slopes. No
comparison between the different |p_i| is required.

There is no genericity exception a_i=1 at a selected finite filling.
Exact separate evenness gives V_i=tau_i(z)U_i holomorphically, with
tau_i near its nonreal complete cusp value. If U_i=0 then V_i=0,
contradicting U_i+p_iV_i=+/-2pi i. The selected logs are small, so
exp(U_i)=1 also forces U_i=0. Thus every selected auxiliary meridian
has a_i!=1 and the stated finite second fixed point exists.

## 3. The actual end contains a full punctured tube

Translate q to zero in upper half-space coordinates (z,y), y>0.
The link development now has z=exp(f). Every incident geometric
tetrahedron has its chosen ideal vertex at infinity. Its faces through
infinity are vertical planes. Above a bounded lower height its part
over its Euclidean link triangle is therefore a vertical product.
The opposite face cannot be vertical: otherwise all four vertices
would lie in one hyperbolic plane and the tetrahedron would have zero
volume. This works with finite as well as ideal remaining vertices.

There are finitely many such pieces in a fundamental link domain and
that domain avoids zero. It follows that for some finite A>0 the end
contains the full equivariant epigraph

    y>A|z|.                                                (3)

Indeed bound every lower cutoff y_0(z)/|z| on those finitely many compact
pieces; affine deck similarities multiply numerator and denominator
by the same positive number. Since f is globally one-to-one onto C,
the different pieces meet coherently across their side faces and do
not introduce an uncounted logarithmic covering.

Put r=y/|z|. Cylindrical coordinates about the vertical 0--infinity
axis are

    R=asinh(1/r), theta=Im f,
    X=Re f+(1/2)log(1+r^2).

The hyperbolic metric is exactly

    dR^2+cosh(R)^2 dX^2+sinh(R)^2 dtheta^2.                (4)

A link deck translation f->f+L_gamma acts by
(X,theta)->(X+Re L_gamma,theta+Im L_gamma). Equation (3) says that
the end contains the WHOLE region 0<R<R_0 of this tube, not merely
a narrow subset tending toward its axis.

## 4. Primitive logarithmic angle is the decisive completion condition

Let alpha be a primitive filled slope and choose beta so (alpha,beta)
is a basis of pi_1(T)=Z^2. Suppose its ACTUAL log-link period is

    L_alpha=+2pi i or -2pi i.                              (5)

Because Lambda has real rank two, Re L_beta!=0. The quotient of (4)
for 0<R<R_0 therefore has one angular period exactly 2pi and one
loxodromic screw generator. Adding R=0 is the ordinary smooth
hyperbolic solid torus, with core length |Re L_beta|. Its meridian
is exactly alpha. Either sign in (5) gives a smooth tube; it chooses
the orientation of its meridian parameter, not a mirror of the
positive compact core.

This proves smooth filling and discreteness directly from the local
metric. Killing alpha in PSL2 alone would NOT suffice. If instead
L_alpha=2pi i m with |m|>1, the same construction has cone angle
2pi|m| at its core. All punctured local geometry and the killed PSL
slope could still hold, but the completion would be branched rather
than smooth. If L_alpha=0, injectivity of the logarithmic period map
would already contradict a nonsingular compact link torus.

The [primitive-angle proof](actual_long_pretzel_primitive_filling_angle.md)
identifies the actual periods with the source logarithms, including
their integer windings. In the source conventions,

    U_i=Log(M_i^2)=-z_i,
    V_i=Log(lambda_i^2) centered at completeness=-2ell_i,
    U_i+p_i V_i=-2pi i m_i.

The surviving charges satisfy |m_i|=1, precisely (5). The complete
SL2 longitude sign is NOT used as an uncentered 2pi i contribution
to V_i. The proof of the period identification must remain separate
from merely checking exp(U_i+p_i V_i)=1.

At the unfilled main cusp all affine multipliers are one. Its positive
compact link is an ordinary complete Euclidean torus by the same
flat-metric argument, and its end contains a full horoball quotient.
Thus the completed filled metric has finite volume and exactly the
required complete main cusp.

## 5. What follows, without assuming a character-variety uniqueness theorem

Combining the positive-core input with sections2--4 yields a complete
oriented hyperbolic metric on the ACTUAL filled knot complement. Its
holonomy is rho_p. The developing map on its complete universal cover
is a local isometry to H3. Lifting geodesic segments exactly as above
makes it a covering of H3; since H3 is simply connected it is a global
isometry. Hence rho_p is discrete and faithful.

One can compare its volume to any specified complete hyperbolic metric
on the same oriented manifold without importing an additional volume-
rigidity assertion. Apply the proved sharp representation-volume
inequality once with each complete structure as domain and the other
structure's holonomy as target. The finite fundamental chain has the
same oriented degree one in both cases. The two inequalities give

    Vol(rho_p)=Vol(the filled hyperbolic manifold).         (6)

Together with the already proved whole-source asymptotic and marked
regulator comparison, this is the required equality. The proof is
conditional ONLY on the explicit positive-core input and the actual
primitive-period certificate, both stated above; convergence of
Vol(rho_p) to the augmented volume is not used as an equality argument.

## 6. Casson--Rivin and Gromov: the exact scope of the extremal argument

Strict concavity of the ideal-tetrahedron volume on an affine POSITIVE
angle slice gives at most one interior critical point and makes that
point its global maximum. It does not by itself prove:

* that a supplied topological ideal triangulation has a positive
  geometric realization;
* that the SOURCE point lies in that same angle slice;
* that the correct filling slope and its integer log angle are used;
* that a locally geometric but incomplete end completes without a
  branching multiplicity.

In particular, the UNFILLED complete-cusp angle constraints have a
different maximum from a finite Dehn filling. For actual peripheral
logarithms u,v the regulator variation is

    dV=2 sum(Re v dIm u-Re u dIm v).

On a slice fixing only the rotational filling condition
Im(u+p v)=constant, this becomes

    dV=-2 sum(Re u+p Re v)dIm v.

The real filling condition Re(u+p v)=0 is therefore the relevant
stationarity condition. Replacing this modified slice by the original
complete-cusp slice would be incorrect. A positive all-ideal
triangulation and the full-rank marked gluing rows can make this a
strict-concavity proof of uniqueness; the finite-center completion
above does not need that additional representation.

Likewise the Gromov/representation-volume norm inequality proves only
|Vol(rho)|<=Vol(M). Equality needs an actual equality certificate.
Here that certificate is the complete local isometry constructed
from the positive core and the primitive tube, rather than proximity
of two volumes or a formal maximum principle.

## 7. A precise local-uniqueness lemma when positive ideal rows are supplied

There is also a short independent local-rigidity statement. Suppose an
ACTUAL positive all-ideal triangulation has t tetrahedra and c cusps,
and its t-c independent edge equations together with the c specified
meridian equations form a full-rank real isotropic row matrix (A B).
Thus its row space is Lagrangian, not just an arbitrary selection of
cleared polynomial equations. Write shape logs x_j=Log z_j and
y_j=Log(1-z_j^(-1)). At the positive complete point,

    dy_j=tau_j dx_j, tau_j=1/(z_j-1), Im tau_j<0.

The fixed-meridian gluing Jacobian A+B diag(tau_j) is invertible. If
a vector a were in its kernel, (a,diag(tau)a) would lie in the complex
Lagrangian kernel of (A B). Its symplectic pairing with its conjugate
would be zero; multiplied by i/2 that pairing is

    sum_j Im(tau_j)|a_j|^2,

which is strictly negative unless a=0. The holomorphic implicit-function
theorem therefore gives a UNIQUE local positive shape solution for
each set of small marked meridian logs.

Any sufficiently close framed representation whose equivariant ideal
vertices give that same positive triangulation satisfies those gluing
equations and is this shape germ, up to its already specified framing.
Thus no additional near-complete branch can be substituted while
keeping the SAME marked geometric gluing data. This lemma neither
asserts full rank for unverified rows nor obtains the source's
geometric realization from an arbitrary topological triangulation.
Even with this local uniqueness, the primitive-angle and end-completion
arguments in sections2--4 remain necessary to identify a smooth filled
manifold rather than a branched completion.

## 8. Final independent audit verdict

The primitive-angle proof and the positive-core construction have now
both passed independent analytical reads, and two independent readers
checked sections2--5 of this note. Thus the stated geometric inputs are
supplied, rather than left as formal hypotheses. The completed metric
and its degree-one fundamental chain identify the source regulator
with the actual hyperbolic volume for the precise long-pretzel class.

The separate [Casson--Rivin presentation](actual_long_pretzel_casson_rivin_equality.md)
also checks: its coisotropic first-variation formula applies to every
tangent of the marked ANGLE slice, because both the actual real log
vector and an arbitrary edge-angle tangent lie in E^perp. It does not
assume that every such tangent solves nonlinear gluing. The factor1/2
for squared peripheral coordinates is correct, and the source's real
filling equations kill the boundary derivative on the filled rotational
slice. Strict concavity then gives a unique maximum. The geometric
completion remains in that proof's dependency chain; the maximum alone
does not identify a smooth filled end.

The conclusion remains restricted to every fixed odd s>=25 and all
independently sufficiently long fixed signed p_i, with the ORIGINAL
source and normalization. It is not a conclusion for all hyperbolic
knots, short fillings, or slopes growing with the quantum level.
