# Actual ideal prism cells and geometric Newton associativity

29 October 2026. Every strictly positive Newton multiplication action
is the volume of an explicit convex IDEAL TRIANGULAR PRISM. Its three
ordered quadrilateral faces have cross ratios given by derivatives of
the actual source action. Thus internal source stationarity is exactly
the isometry condition for the prescribed quadrilateral face gluing.
Two stationary multiplication cells form an ideal cube; its alternative
diagonal cut gives the other parenthesization. The equality holds for
the full conjugate-antisymmetric pre-Bloch class, not just its regulator.

This supplies local geometric incidence and composition. It does not
by itself identify every closed Conway expression with a complete
hyperbolic link complement. Boundary degenerations, the global diagram
identification and complete ends still require their own arguments.

## 1. The actual source action

Use [the positive full-Newton multiplication](actual_positive_newton_multiplication.md),
whose uniform action is

    m(x,y,z)=L(x+y)+L(z)-L(x)-L(y)
                    -L(z-x)-L(z-y)-L(x+y-z),
    L(t)=integral_0^t log(2sin(pi u))du.

Work first in its STRICT domain

    p=z-x>0, q=z-y>0, r=x+y-z>0, w=1-x-y>0,
    p+q+2r+w=1,
    x=q+r, y=p+r, 1-z=r+w.                         (1)

For positive a+b+c=1 let V(a,b,c) be the actual volume of an ideal
tetrahedron with angles pi(a,b,c). The proved source identity is

    pi m=V(y,x,w)+V(p,q,1-p-q)+V(p+q,r,r+w).         (2)

The source remains its original multiplication table, including its
normal directions; no new state sum is being substituted here.

## 2. Explicit six vertices of a convex ideal prism

In the upper half-space model, use the ideal point infinity and four
points on the unit circle in the boundary plane:

    v0=1,
    v1=exp(2pi i p),
    v2=exp(2pi i(p+r)),
    v3=exp(2pi i(p+r+q)).                           (3)

The consecutive half-arc lengths are p,r,q,r+w. They are all positive
and sum to one. Let P be the intersection of the Euclidean lines
(v0,v1) and (v2,v3). The inequalities in (1) imply that P lies beyond
v1 on the ray from v0, and beyond v2 on the ray from v3. Indeed the
exterior triangle (P,v1,v2) has angles

    angle(v1)=pi y, angle(v2)=pi x, angle(P)=pi w.

Their sum is pi and all are positive. The elementary sine rule gives
the explicit formula

    P=v1+kappa_x(v1-v0)=v2+kappa_y(v2-v3),
    kappa_x=sin(pi x)sin(pi r)/(sin(pi w)sin(pi p)),
    kappa_y=sin(pi y)sin(pi r)/(sin(pi w)sin(pi q)). (4)

In particular |P|>1. Form the ideal quadrangular pyramid with apex
infinity and base (v0,v1,v2,v3), and attach the ideal tetrahedron
(infinity,P,v1,v2) along their common triangular face
(infinity,v1,v2), on opposite sides of that face.

The pyramid has dihedral angles p,r,q,r+w along its four base edges.
Its dihedral angle at an apex edge is one minus the sum of the two
adjacent half-arcs. Along the shared face the two apex-edge angles
therefore add to pi after the attachment, while the base-edge angle
adds to pi(r+w)<pi. The two coplanar face pairs merge. The resulting
six-vertex polyhedron is the ideal triangular prism with faces

    triangles: (P,v1,v2), (infinity,v0,v3),
    quadrilaterals:
       Fx=(infinity,v0,v1,P),
       Fy=(infinity,v3,v2,P),
       Fz=(v0,v1,v2,v3).                           (5)

Convexity is literal. The two merged vertical side planes are the
planes over (v0,v1) and (v2,v3). The third vertical side plane is over
(v3,v0). The remaining supporting hemispheres have boundary circles
(v0,v1,v2,v3) and (P,v1,v2). P is outside the first circle, and v0,v3
are outside the second circle on the side opposite its arc through P.
These five half-spaces contain both attached cells, and their
intersection has exactly the vertices and faces (5). Thus the union
is their convex intersection, not an immersed volume chain.

Equivalently one may use the elementary convex-union argument: the
two convex cells lie on opposite sides of the attaching support plane,
and all its finite seam angles are at most pi. The union is locally
convex. Between any two finite points, a length-minimizing path exists
by compactness of a bounded hyperbolic ball containing a minimizing
sequence; local convexity makes that path an ambient geodesic. Thus
the union is convex, without an assertion at a missing ideal vertex.

The complete edge-angle table is

| Edges | Dihedral angle divided by pi |
|---|---:|
| P-v1 and infinity-v0 | x |
| P-v2 and infinity-v3 | y |
| v1-v2 and v0-v3 | 1-z |
| P-infinity | w=1-x-y |
| v0-v1 | p=z-x |
| v2-v3 | q=z-y |

Each ideal vertex has three incident angles summing to pi. The three
longitudinal angles have sum pi(1-2r)<pi. This last strict inequality
is visible directly in the construction; no polyhedron existence
theorem is being invoked.

Conversely any convex ideal triangular prism with these ordered
ports has this explicit form after an isometry. Send its selected
quadrilateral port circle to the unit circle, and one of its two
remaining ideal vertices to infinity. The other two quadrilateral
faces then lie in vertical planes through the remaining vertex P;
their boundary lines are (v0,v1) and (v2,v3). Thus P is exactly
their intersection, and its position on the exterior side of the
base support hemisphere gives |P|>1. Orient the cyclic base order
so that the finite triangular wall is (P,v1,v2). Its positive
triangle angles make the four half-arcs (p,r,q,r+w) with w>0.
The same sine rule recovers (4), and the edge-angle table recovers
x=q+r, y=p+r, z=p+q+r. This verifies that the alternative prism
pieces used in section 6 are actual cells of this family.

Triangulating the quadrangular pyramid across (v0,v2) gives tetrahedral
angle triples (p,r,1-p-r) and (p+r,q,r+w). Their volume sum is

    Lambda(pi p)+Lambda(pi q)+Lambda(pi r)+Lambda(pi(r+w)),

because the complementary intermediate angles cancel. This is also
the sum of the last two volumes in (2). The attached tetrahedron has
volume V(y,x,w). Therefore this ACTUAL convex prism has volume pi m.

## 3. The ordered face metrics are the source derivatives

For cyclically ordered ideal points (a,b,c,d) on a circle or line set

    kappa(a,b,c,d)=(a-b)(c-d)/((a-d)(b-c))>0,       (6)

using the limit when one point is infinity. This positive real number
determines the ordered ideal quadrilateral up to hyperbolic isometry:
send three vertices to (infinity,0,1) and the fourth is determined
by (6). A one-step cyclic change of vertices, or reversal fixing the
first vertex, replaces kappa by its reciprocal.

For the orders in (5), direct substitution and the sine rule give

    kappa(Fx)=sin(pi x)sin(pi r)/(sin(pi w)sin(pi p)),
    kappa(Fy)=sin(pi y)sin(pi r)/(sin(pi w)sin(pi q)),
    kappa(Fz)=sin(pi p)sin(pi q)/(sin(pi z)sin(pi r)). (7)

Differentiating the actual source action, with all other boundary
variables fixed, proves the exact equations

    log kappa(Fx)=-partial_x m,
    log kappa(Fy)=-partial_y m,
    log kappa(Fz)=-partial_z m.                    (8)

There is no normalization constant: all factors of 2 in L' cancel.

The actual h-leaf action g(x)=-2L(x)-2L(1/2-x), 0<x<1/2,
likewise has a literal ideal pyramid. Its apex is infinity and its
base is the rectangle with vertices

    (1, exp(2pi i x), -1, -exp(2pi i x)).

Its four base angles alternate x and 1/2-x, its four apex-edge angles
are right angles, and its volume is pi g(x). Its ordered base metric
is

    kappa_leaf=tan(pi x)^2=exp(-g'(x)).             (9)

## 4. Source stationarity gives the actual corner-preserving gluing

Mark any child output quadrilateral by C0,C1,C2,C3 in its source
order. In a multiplication prism use the lower and upper input maps

    lower child: (C0,C1,C2,C3) -> (v0,v1,P,infinity),
    upper child: (C0,C1,C2,C3) -> (infinity,P,v2,v3). (10)

These are the literal identity-stack corner identifications: the
lower child's top left and right corners map to infinity and P,
which are respectively the upper child's bottom left and right
corners. Thus no unrecorded four-punctured-sphere mutation is inserted.

Relative to (5), the first map is a cyclic shift and the second a
reversal. Each replaces kappa by its reciprocal. At an internal
wire u, source stationarity says that the child output derivative
plus the parent input derivative is zero. Equations (8),(9) therefore
give

    kappa_child kappa_parent=1.                   (11)

By the complete metric invariant (6), (11) is EXACTLY the condition
that (10) is an ideal-quadrilateral isometry. This proves metric
matching of the whole face, rather than merely equality of a
formal edge product.

For the relevant angle bookkeeping, call output edges C0-C1 and
C2-C3 FREE, and the other pair CAP. A leaf output has FREE angles x
and CAP angles 1/2-x. A completed product output has FREE angles z
and CAP angles 1-z. The input maps (10) send CAP edges to the prism's
two edges with angle x or y, and FREE edges to its longitudinal
edges. Thus a leaf-to-prism seam produces right angles on the CAP
pair; a product-to-prism seam has angle pi on that pair and becomes
flat. The edge common to both inputs has total angle

    pi(w+x+y)=pi,

while the output's two longitudinal edges acquire angles

    pi(p+x)=pi z, pi(q+y)=pi z.                   (12)

These identities explain the local right/flat boundary pattern.
They do not alone prove the global closure or cusp completeness of
an arbitrary expression. A genuine turn rotates a product output
quadrilateral once, exchanges FREE and CAP, and replaces its label
x by 1-x. It also inverts kappa, exactly as the derivative of the
turned profile requires.

## 5. Equality of the full antisymmetric pre-Bloch class

Write A(z)=[z]-[bar z] in the rational pre-Bloch group. For an ideal
tetrahedron with positive angle triple (a,b,c), let its positive
shape be z=exp(pi i a)sin(pi b)/sin(pi c), and put
u_a=exp(2pi i a), and cyclically. Applying the defining five-term
relation to (z,bar z) gives

    A(z)=-[u_a^-1]+[u_c]-[u_b^-1].

Subtract its complex conjugate. One obtains the uniform identity

    A(z)=1/2 (A(u_a)+A(u_b)+A(u_c)).               (13)

No integral inversion identity or unproved regulator injectivity is
used. In particular A(exp(2pi i(1-a)))=-A(exp(2pi i a)) directly
from its definition.

Consequently the sum of A over a pyramid's two tetrahedra depends
only on the sum of A(exp(2pi i theta)) over its four half-arcs;
complementary diagonal terms cancel. The source ordering
(p,q,r,r+w) and the actual prism ordering (p,r,q,r+w) give exactly
the SAME class. Equation (13) therefore upgrades (2) to

    sum_(three source atoms) A(z_j)
           = sum_(an actual prism triangulation) A(z_j)          (14)

in the rational pre-Bloch group of any common field containing the
displayed phases and shapes. For algebraic source stationary points
this is a number field, as in the proved source-regulator theorem.
No assertion of zero boundary for this open cell is made.

More generally the antisymmetric class of a convex ideal polyhedron
is independent of its ideal triangulation, directly from five-term
relations. For equal boundary triangulations the difference of two
tetrahedral chains is a 3-cycle in the full abstract simplex on their
ideal vertices. Coning it to one vertex gives a 4-chain bounding it;
the boundary of each 4-simplex is precisely a five-term relation.
Different triangulations of a boundary polygon can first be corrected
by tetrahedral chains whose four vertices lie on that face's circle.
Their shapes are real, hence their A-symbols are zero. This proves
the assertion without assuming a general Pachner-connectivity theorem.

## 6. Actual ideal-cube geometry proves stationary associativity

Fix positive a,b,c,d with

    a+b<1, a+c<1, b+c<1,
    max(a,b,c)<d<min(1,a+b+c).                     (15)

For the left parenthesization put

    F_L(t)=m(a,b,t)+m(t,c,d),
    max(a,b,d-c)<t<min(a+b,d,1-c).                (16)

This interval is nonempty precisely under (15). Its derivative is

    F_L'(t)=log[sin(pi(t+c)) sin(pi(a+b-t)) sin(pi(d-t))
                    /(sin(pi(t-a)) sin(pi(t-b)) sin(pi(t+c-d)))].

It tends to positive infinity at the lower endpoint and negative
infinity at the upper endpoint. Strict concavity of the two actual
source actions gives a UNIQUE interior maximizer t*. Therefore the
two multiplication prisms glue by (10),(11).

Their two wall-edge seams with angles (1-t*)+t* become flat. The
four triangular walls merge into two quadrilateral walls. The union
is an ACTUAL convex ideal cube with four input/output port faces.
Its wall-edge angles, in order around either wall, are

    pi(a,b,c,1-d),

and its four edges between consecutive port faces have angles

    pi(1-a-b), pi(1-b-c), pi(d-c), pi(d-a).        (17)

They are all positive and less than pi by (15). The seam's remaining
edge angles are respectively (t*-a)+(d-t*)=d-a and
(t*-b)+(1-t*-c)=1-b-c. Thus the two convex cells have no reentrant
seam, and their union is the convex ideal hexahedron with these faces.

There is an explicit common reflection, which supplies the other
diagonal cut without invoking a rigidity theorem. For the single
prism in section 2 define the reflection in the hemisphere centered
at P with squared radius |P|^2-1:

    R(z)=P+(|P|^2-1)/(bar z-bar P).               (18)

It exchanges infinity with P. The elementary power-of-a-point
identity for the unit circle shows that it exchanges v0 with v1
and v3 with v2. Its reflecting plane is perpendicular to all three
quadrilateral port planes: it is perpendicular to the two vertical
planes through P and orthogonal to the unit hemisphere. It exchanges
the prism's two triangular walls.

The corner maps (10) intertwine the corresponding vertex exchanges.
Hence the two reflecting planes agree after gluing, and the ideal
cube has a common reflection plane. Its section by that plane is a
convex hyperbolic quadrilateral; its four vertices lie on the four
edges between port faces. Each such edge is perpendicular to the
reflection plane, and its two ideal endpoints are exchanged.

The OTHER diagonal of this quadrilateral determines a hyperbolic
plane perpendicular to the reflection plane. It contains both full
perpendicular port edges at its endpoints. Consequently it cuts the
cube in an IDEAL QUADRILATERAL with those four ideal endpoints.
The two pieces are convex ideal triangular prisms. Their external
ports are (b,c) and (a,d), exactly the right parenthesization. If u*
denotes the new internal source label, the angle table in section 2
gives their actions m(b,c,u*) and m(a,u*,d). Their common face is
already isometric, so (8) gives right-side stationarity. The same
endpoint and strict-concavity argument makes u* its unique maximizer.

Both parenthesizations thus decompose ONE actual ideal cube. They
have equal volume and equal full antisymmetric pre-Bloch class by
section 5. This is a source-local geometric associativity theorem;
it is stronger than deducing equality of exponential rates from
the finite algebra's associativity.

There is also an exact algebraic check of the critical point. Put
X=exp(2pi i a), Y=exp(2pi i b), Z=exp(2pi i c), W=exp(2pi i d),
T=exp(2pi i t*). The sine equation in (16) is the polynomial identity

    (ZT-1)(XY-T)(W-T)=(T-X)(T-Y)(ZT-W).

Its cubic and constant terms cancel, and its nonzero root is

    T=(XYZW-XYZ+XY-XW-YW+W)
                          /(XYZ-XZ-YZ+ZW-W+1).                 (19)

The denominator is nonzero under (15): otherwise the polynomial
would have no nonzero root or would vanish identically, contradicting
existence and strictness of the real stationary point. The root
for u* follows by cyclically permuting (X,Y,Z). The selected angle
interval, not the rational formula alone, fixes the geometric branch.

The proof above concerns positive local cells and their stationary
composition. Flat source faces, boundary maxima and full closed-link
incidence must still be handled before turning these local results
into a general hyperbolic-volume theorem.

Audit: [explicit cells, symbolic classes and actual stationary cubes](../experiments/audit_actual_newton_ideal_prism_and_associativity.py)
and [recorded results](../experiments/actual_newton_ideal_prism_and_associativity_results.json).
It checks 163 prisms with exact rational circle coordinates and exact
reflection maps, the symbolic five-term phase conversion and critical
polynomial, and 20 actual stationary ideal cubes at high precision.
The cube checks construct the face-gluing Mobius map, verify all six
supporting face planes and convexity, check the common reflection,
and test coplanarity of the four endpoints of the alternative cut.
The uniform proof is the geometric and algebraic argument above;
the finite checks do not infer arbitrary link geometry.

The explicit converse normalization in section 2 identifies the alternative pieces with this source prism family; no general polyhedron rigidity theorem is assumed there.