# The actual marked deformation of every retained Conway factor

29 October 2026. This constructs an actual framed representation of the
original closed link exterior for the mixed-circle critical source.
All face-pairing relations hold as PSL(2,C) identities, including the
white seams and the full four-step shaded-edge holonomies. The primitive
crossing-circle logarithms are

    U_i=-2pi i t_i,          V_i=-2 partial_i phi(t).

Thus the existing source filling saddle is the actual marked filling
equation. The conclusion concerns the broad robust LINK class. Even
full-twist fillings of these pure sources do not produce knots.

The proof uses the [actual closed bowtie cut](actual_conway_bowtie_projection_cut.md).
An open metric quadrilateral is an auxiliary chart, not an asserted
physical four-punctured boundary. No representation is inferred merely
from matching quadrilateral metrics.

## 1. The analytic branch to be represented

Fix a retained cylindrical factor C(A), A=h^3, or C(FG), where F,G
belong to the robust turn/product grammar. Delete its final forced-flat
product and retain the exact relation between the two final wire labels.
For its free wire coordinates y and independent auxiliary parameters t_i
write the original mixed-core action

    f(y,t)=sum_i g(x_i(y),t_i)+sum_products m(x,y,z),
    g(x,t)=J(2x)-2J(x)-J(x-t)-J(x+t),
    J(a)=integral_0^a Log(2sin(pi u))du.                    (1)

The logarithms are continued from the strict complete positive chamber.
The complete wire Hessian is negative definite. Hence there is one
holomorphic critical branch y_*(t) near zero, and

    phi(t)=f(y_*(t),t).                                   (2)

Uniqueness and the separate evenness of (1) imply that every wire label
and phi are separately even in all t_i. For small real t, all cell
angles used below remain strict. Stationarity still says that ordered
quadrilateral metrics match under the original stack corner maps.

## 2. The mixed leaf and its two actual flags

Put E=exp(2pi i x), H=exp(2pi i t). A mixed leaf is the ideal pyramid
with apex infinity and cyclic base

    C0=1, C1=E/H, C2=-1/H, C3=-E.                         (3)

The consecutive half-arc lengths of its unit-circle base are

    (x-t, 1/2-x, x+t, 1/2-x).

Triangulating the base gives volume pi g(x,t). Indeed the intermediate
diagonal angles cancel, and J(2x)-2J(x)=-2J(1/2-x).
Its ordered base cross ratio is

    kappa=sin(pi(x-t))sin(pi(x+t))/cos(pi x)^2
         =exp(-partial_x g).                             (4)

Normalize its ordered base to (0,infinity,1,R), where

    R=1/(1+kappa)=cos(pi x)^2/cos(pi t)^2
      =H(1+E)^2/[E(1+H)^2].                             (5)

In this chart the plus-t apex is

    zeta_+=(1+E)/(1+H).

The minus-t leaf has the SAME ordered base metric and its normalized
apex is zeta_-=H zeta_+. These are the two roots of

    zeta^2-(1+E)zeta+ER=0.                              (6)

For the second projection ball use the reflected MINUS-t cell, not
the reflection of the plus-t cell. Its apex is zeta_+/E. Its main
segment vertices remain the same real ordered base vertices.

In the actual bowtie cut the shaded map takes
(O,C1,C2) to (O,C0,C3). In the normalized chart its projective matrix is

    S=[[0,-ER],[1,-1-E]].                               (7)

It fixes both roots in (6). This follows by substitution, rather than
by naming an unmarked eigenvalue of the Newton boundary relation.

## 3. Four universal boundary transport matrices

For an ordered auxiliary port Q=(0,infinity,1,R) of wire label b, put
E=exp(2pi i b). The following matrices send a plus chart to its
reflected minus chart:

    W0=[[1,0],[0,E]],
    W1=[[1,E-1],[0,E]],
    W2=[[E-R,R(1-E)],[E-1,1-ER]],
    W3=[[R,0],[1-E,ER]].                               (8)

Wj fixes the two endpoints of port edge j,j+1. All equalities between
matrices below are projective. The FREE edges are 01 and 23; CAP edges
are 12 and 30.

For the mixed leaf, W0 and W2 are its ACTUAL white triangle maps:
they fix the relevant two main vertices and send zeta_+ to zeta_+/E.
For W2 the last assertion follows from (6). The matrices W1,W3 are
completion-plane maps: at a leaf they describe the white pieces
attached on the other side of its shaded CAP edges, not extra leaf
white faces.

One useful geometric description of (8) is that Wj followed by complex
conjugation is reflection in a plane through the corresponding port
edge. Its angle with the port plane is pi b on FREE edges and
pi(1-b) on CAP edges, with the side fixed by the ordered chart.
These are virtual planes for the mixed leaf; its actual white planes
need not be their fixed planes. Equation (8), rather than an assumption
of planarity of the deformed white polygons, is the transport data.

### The product identities

Use the literal prism coordinates and child maps from
[the local-cell proof](actual_newton_ideal_prism_and_associativity.md):

    lower Q=(v0,v1,P,infinity),
    upper Q=(infinity,P,v2,v3),
    output Q=(v0,v1,v2,v3).                             (9)

The white prism triangles are T_top=(P,v1,v2) and
T_bottom=(infinity,v0,v3). Call their actual maps to their reflected
copies B_top,B_bottom. Transport each set of matrices (8) to the
common prism coordinate. Then direct substitution gives ALL the
needed identities:

    W_lower,1=W_upper,1=W_output,1=B_top,
    W_lower,3=W_upper,3=W_output,3=B_bottom,
    W_lower,2=W_upper,0,
    W_output,0=W_lower,0,
    W_output,2=W_upper,2.                              (10)

Here the three E parameters are exp(2pi i x), exp(2pi i y),
exp(2pi i z), and each R is the actual ordered-port value.
These identities can also be checked by the plane description:
the CAP/input angles complement each other; the common two-input
FREE seam has angle w+x+y=1; the two output FREE angles are p+x=z
and q+y=z. The maps are equal on entire planes, including their
translations, since their ordered edge endpoints and reflection
planes agree. No mere equality of absolute cross ratios is used.

For a wholly algebraic check of (10), put
A=exp(2pi i p), B=exp(2pi i r), C=exp(2pi i q). The prism coordinates are

    v0=1, v1=A, v2=AB, v3=ABC,
    P=1+A-A[AB(1+C)-1-A]/[A^2 B^2 C-A],                 (11)

and the three E parameters are BC, AB, ABC. Conjugation replaces
A,B,C by their reciprocals. If T sends an ordered port to
(0,infinity,1,R), its world-coordinate matrix is
bar(T)^(-1) Wj T. Inserting (11) gives (10) by cancellation of rational
functions. The accompanying audit checks these identities symbolically
with independent indeterminates A,B,C.

### Turns and final cylindrical closure

A turn replaces E by E^-1, R by 1-R. The coordinate change is
T(z)=(R-1)/(z-1), and exact substitution in (8) gives

    T W_(j+1)(E,R)=W_j(E^-1,1-R) T.                    (12)

For the final ordered gluing j->3-j the two wire labels add to one
and their kappas are equal. The normalized coordinate change is
C(z)=(z-R)/(z-1), and

    C W_j(E^-1,R)=W_(2-j)(E,R) C.                     (13)

Thus every original turn and the actual cylindrical closing map retain
the complete transport matrices, not only their port metrics.

## 4. All original white face maps exist

Build both halves using the prescribed metric quad maps. For real t,
the plus and minus source wire values are equal. Every prism is
therefore the same before reflection, and all corresponding main
vertices have the same normalized port coordinates. Only auxiliary
apices select the opposite roots (6).

Induct on the actual expression. At a leaf its two white triangle maps
are W0,W2. At a product the CAP pieces already white in a nonleaf
child match the attached prism maps by (10). If the child is a leaf,
its CAP face is shaded and the prism supplies precisely its completion
map W1 or W3. The two-input FREE seam matches by the middle identity
in (10). The remaining boundary pieces have exactly the output maps
in (8). Equations (12),(13) perform every turn and final closure.

Consequently any two triangular pieces belonging to the SAME original
white face have EXACTLY the same Mobius map. This statement continues
through all the white/white seams, including those whose deformed
pieces are no longer coplanar. Their two-step edge holonomy is the
identity. The original closed bowtie ribbon graph fixes which pieces
belong to each white face; no open-port topology is being assumed.

## 5. Shaded edge relations and actual representations

Write bar(S) for (7) with E replaced by E^-1; R is unchanged. Direct
matrix multiplication gives

    W0 S=bar(S) W0,
    W2 S=bar(S) W2,
    W3 S=bar(S) W1.                                    (14)

The first two equations are the two pairs of bowtie sides incident
to O. The last equation is its CAP-base pair. They are precisely the
four-step edge words: shaded in the first half, white to the second,
inverse shaded there, and inverse white back. Every such word is
POINTWISE the identity in PSL(2,C), including any possible dilation
or translation along its ideal edge.

The [closed cut](actual_conway_bowtie_projection_cut.md) supplies two
actual topological balls and the labeled white/shaded gluings. Choose
one of the face transitions to join their frames. The remaining face
transitions generate the fundamental group; its edge relations are
exactly the two-step white seams and four-step bowtie words just proved.
Equivalently subdivide the balls and their faces and use the standard
dual two-skeleton presentation, whose two-cells are these edge words.
Thus these matrices define an ACTUAL representation of the original
link group. This argument does not need the deformed half-ball image
to remain an embedded convex polyhedron.

At t=0 the construction is the proved complete geometric holonomy.
The finitely many face matrices and cusp flags vary analytically and
stay in a bounded framed neighborhood of it. Extend to complex t by
holomorphic continuation: the second half means the Schwarz-reflected
minus branch, with conjugated coordinate coefficients, rather than
antiholomorphic dependence on t. Every identity above is holomorphic
and holds for small real independent t, hence on a complex polydisk.

## 6. All main cusps remain parabolic

At a main corner Cj the two original white sectors give its small
meridian: cross one white face and return through the other. In its
local port frame the resulting map is W_(j-1)^(-1) Wj, or its inverse
according to the orientation. Both factors fix Cj. Their derivatives
there are equal: at C0,C2 they are E^-1, and at C1,C3 they are E,
using the finite local coordinate at infinity. Thus the multiplier
of this actual meridian is one, IDENTICALLY in the deformation.

The meridian is nonidentity at the complete point and remains so after
shrinking the neighborhood. It is therefore parabolic. The actual
longitude commutes with it, so it too is a translation in the common
flag frame and has multiplier one. This proves parabolicity of the
entire main peripheral groups, not only a trace equation at one flag.

## 7. Primitive auxiliary holonomies and their source derivatives

Use the same primitive paths as at completeness in the closed-cut note.
The crossing-circle meridian is the inverse shaded map. In the original
leaf coordinate (3) it sends C3 to C2, C0 to C1 and fixes infinity:

    mu(z)=H^-1 z+(E-1)/H.

Hence its small centered similarity log is exactly

    U=-Log H=-2pi i t.                                (15)

The disk-framed longitude crosses the bottom white face and returns
through the top. In the normalized chart it is W2^-1 W0, fixing
zeta_+. Its multiplier in the flag-at-infinity coordinate is

    exp(V)=[(zeta_+-E)/(zeta_+-1)]^2
          =[(1-EH)/(E-H)]^2
          =[sin(pi(x+t))/sin(pi(x-t))]^2.             (16)

One can check the first equality directly: a Mobius map fixing a
finite flag has flag-at-infinity multiplier reciprocal to its
ordinary derivative there. Use (6) when differentiating W2^-1 W0.
Continue the logarithm from V=0, obtaining

    V=2Log[sin(pi(x+t))/sin(pi(x-t))]
      =-2 partial_t g(x,t).                           (17)

The paths are the primitive meridian and disk-framed longitude already
calibrated by the two-rectangle complete cusp; no doubled longitude or
unrecorded change of slope is inserted. Their continuations cannot
change integral marking in a small connected neighborhood.

Internal criticality and the envelope rule now give for every circle

    U_i=-2pi i t_i,       V_i=-2 partial_i phi(t).      (18)

An unfilled auxiliary color has t_i=0. Separate evenness makes V_i=0
there as well, so it remains a complete parabolic cusp. In particular

    dV_i/dU_i at zero =2i cot(pi x_(i,*)),

in agreement with the primitive complete lattice, while the packet
parameter in phi_ii=2pi i tau_packet,i is half this ratio.

## 8. Algebraic marked peripheral equations

This construction also supplies finite algebraic equations for the
ACTUAL peripheral branch. Exponentiate every internal stationarity
equation, retaining all port variables and excluding the strict
denominators. The product cross ratios are rational functions of their
angle phases, and (4) is rational in E,H. Include

    M_i=H_i^-1,
    L_i=[(1-E_i H_i)/(E_i-H_i)]^2.                     (19)

Here M_i=exp(U_i), L_i=exp(V_i) are the centered PROJECTIVE similarity
multipliers. An SL(2) eigenvalue convention takes their square roots
on the local marked branch, retaining its original central signs.
No SL(2) spin is silently identified with one in (19).

Here M_i,L_i are the PSL(2,C) similarity multipliers, equivalently
the squared SL(2,C) peripheral eigenvalues. An SL lift and its spin
would need to be retained before changing to unsquared variables.

All equations are over Q after choosing the finitely many phase
variables clearing the rational wire coefficients. Select the branch
through the complete positive solution and retain its actual marking.
The nondegenerate internal Hessian gives the analytic branch already
used above. Thus (19) is a marked gluing presentation of an actual
peripheral representation branch. Elimination may introduce extra
components or factors; no irreducibility or equality with an entire
classical A-polynomial is asserted merely by eliminating variables.

More precisely, near the selected complete point the exponentiated
stationarity Jacobian in the internal wire phases is nonsingular:
on its continued logarithmic sheet it is the invertible wire Hessian
times invertible phase-coordinate factors. Hence this algebraic
solution branch is locally etale over the auxiliary H coordinates.
Its marked peripheral image is the analytic graph L=L(M) given by
(19). Equation (20) below implies sum_i dU_i wedge dV_i=0, so this
actual H-dimensional peripheral germ is Lagrangian. The source action
is its calibrated local primitive, not a period attached to an
unidentified algebraic curve.

## 9. Absolute regulator and actual long-filled volumes

Put G=2pi i phi, with any explicitly recorded real action constant
retained. Equation (18) gives the full differential

    dG=(1/2)sum_i V_i dU_i.                           (20)

At zero the actual oriented fundamental-chain volume is
Im G(0)=2pi phi(0)=Vol(S^3 minus L_E), by the complete cell theorem and
the closed bowtie cut. This anchors the SAME oriented representation
family, not a possibly unrelated Bloch cycle of equal regulator.

For completeness, the marked fundamental-chain differential is

    dVol(rho)=(1/2)sum_i[Re V_i dIm U_i-Re U_i dIm V_i].

It follows by differentiating each ideal tetrahedron's Bloch--Wigner
volume; internal face/edge terms cancel, and a primitive meridian and
longitude on a boundary torus have the signed intersection pairing.
With eigenlogs U/2,V/2 the boundary pairing is -2, giving precisely
the factor 1/2 displayed here. Distinct tori have zero cross pairing.
This is the diagram-independent marked-chain calculation proved in
[the general regulator theorem](general_source_regulator_hyperbolic_equality.md),
section 6. Applying (20) and the complete anchor yields the ABSOLUTE
identity on the connected small branch

    Vol(rho_t)=Im G(t)-(1/2)sum_i Re U_i Im V_i.        (21)

Now choose any subset of auxiliary circles and sufficiently long fixed
signed integral full twists p_i. The actual original-source filling
saddle is

    phi_i(t)+(pi i/p_i)(t_i-1)=0.

By (18) this is exactly U_i+p_i V_i=-2pi i, in the primitive disk
marking. Unfilled main and auxiliary cusps stay parabolic. The actual
nearby framed representation therefore satisfies every hypothesis of
the general geometric completion theorem. It gives a smooth complete
hyperbolic metric on the correctly marked filled link exterior.

Using Re U_i=-p_i Re V_i at the saddle in (21) gives

    Vol(L_E(p))=2pi Re[phi(t)+(pi i/2)
                                  sum_i(t_i-1)^2/p_i].        (22)

The already proved [whole original-source transfer](actual_conway_long_filling_source_limit.md)
has exactly the right side of (22) as its full-sequence exponential
rate. Hence it is the ACTUAL filled hyperbolic volume for every fixed
retained robust factor and all independently sufficiently long signed
integral fillings of any chosen subset. Its original normalization,
normal terms, level parities and nonzero prefactor are those of that
source theorem; geometry does not replace them with another state.

This is a general branching LINK theorem. The
[component obstruction](actual_conway_full_filling_component_obstruction.md)
still gives at least 2S+1 main components for S robust seeds after all
even full-twist fillings. A knot extension needs different connectivity
and its separately checked quantum source, such as retained odd twists.

Audit: [exact peripheral and transport matrices](../experiments/audit_actual_conway_marked_peripheral_deformation.py)
and [results](../experiments/actual_conway_marked_peripheral_deformation_results.json).
The finite audit checks all nine generic prism identities over Q(A,B,C), all four
turn identities, all four cylindrical closure identities, the three
pointwise shaded-edge identities, and every main/auxiliary peripheral
matrix check. No sampled phase values are used in this audit.

In the original leaf coordinate, the two white slopes compose to the complete longitude translation -2(E+1), with multiplier (16).
