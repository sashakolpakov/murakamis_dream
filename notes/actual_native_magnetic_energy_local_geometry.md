# The native highest-weight energy has a geometric action

30 October 2026. The exponential native projector cost is already
geometric in a simple physical block. Its exact normalization also
shows why a general comparison cannot assign a positive volume to
every normalized magnetic summand or discard the phases at a maximum.

## 1. Exact highest-weight energy, both parities

Put q=exp(pi i/N), d=N-1, s_r=product_(h=1)^r 2sin(pi h/N), and choose
0<=j<=floor(d/2). In the physical degree t=j the original normalized
column is a highest vector. Its exact entries are

    f_u=C_j(q;j,u)=q^(ju) s_j/(s_u s_(j-u)), 0<=u<=j.       (1)

This follows directly from the original generic highest-vector ratio:
at the root its negative-index Pochhammer factors give
q^(u^2) [j choose u]_(q^2), and the Gaussian binomial has phase
q^[u(j-u)] and positive magnitude s_j/(s_u s_(j-u)). The generic
source is specialized only after this calculation.

The actual Christoffel--Darboux measure of this simple degree block is

    |sigma_(j,j)|=s_(2j)/s_j^2.                         (2)

For 2j<d, cancel the last factor in the original formula
s_(2j+1)/(s_j^2 |1-q^(4j+2)|). For the odd simple midpoint 2j=d,
the separately retained measure N/s_j^2 is the same expression,
since s_d=N. No zero denominator is evaluated in this cancellation.

Therefore its native rank-one projector norm is exactly

    E_(j,j)=sum_(u=0)^j W_N(j,u),
    W_N(j,u)=s_j^4/[s_(2j)s_u^2 s_(j-u)^2].           (3)

For j<d-j this is the degree-t=j block of the completed cluster
projector, not the singular individual projector on larger degrees.
For 2j=d it is the degree-t=j block of the isolated midpoint
projector. Formula (3) does not maximize over the other physical
degrees of either operator.

## 2. Its complete local variational profile

Let J(x)=integral_0^x log(2sin(pi y))dy. The endpoint-controlled
factorial estimate log s_r=N J(r/N)+O(log N), uniform for 0<=r<N,
gives, with xi=j/N and x=u/N,

    N^(-1)log W_N(j,u)=e(xi,x)+O(log N/N),
    e(xi,x)=4J(xi)-J(2xi)-2J(x)-2J(xi-x).            (4)

This is uniform on 0<=x<=xi<=1/2, with continuous endpoint values.
For fixed 0<xi<=1/2 the action is strictly concave in 0<x<xi:

    e_x=2 log[sin(pi(xi-x))/sin(pi x)],
    e_xx=-2pi sin(pi xi)/[sin(pi x)sin(pi(xi-x))]<0.  (5)

Its unique maximum is x=xi/2. The actual discrete support contains
a point within 1/N of this maximum, and has at most N points.
Bounding (3) between its largest summand and N times that summand
therefore proves, whenever j/N tends to xi in [0,1/2],

    lim N^(-1)log E_(j,j)=m(xi),
    m(xi)=4J(xi)-J(2xi)-4J(xi/2).                   (6)

This statement includes both level parities. Moreover

    m'(xi)=2 log[cos(pi xi/2)/cos(pi xi)]>0
                                      (0<xi<1/2),
    m(0)=0, m(1/2)=-4J(1/4)=v8/(2pi).              (7)

For even N=2h and j=h-1, the actual measure in (2) is
1/sin(pi/N); for odd N=2h+1,j=h it is one. This polynomial
difference does not change the common folded limit (7). Thus the
native exponential obstruction is not restricted to odd levels.

## 3. Four actual ideal tetrahedra at the folded color

Write Lambda(a)=-integral_0^a log|2sin b|db, so J(x)=-Lambda(pi x)/pi.
At xi=1/2, (4) becomes

    2pi e(1/2,x)
      =4[Lambda(pi x)+Lambda(pi(1/2-x))]
      =4 Vol T(pi x,pi(1/2-x),pi/2), 0<x<1/2.        (8)

The tetrahedra in (8) have positive angles summing to pi. They
also glue to an explicit convex ideal octahedron O_x. In the upper
half-space boundary take its six ideal vertices to be

    0, infinity, 1, -1, zeta, -zeta,
    zeta=exp(2pi i x).                               (9)

The four unit-circle vertices form a Euclidean rectangle. Their
unit-hemisphere plane separates the other two vertices. The upper
half is the ideal quadrangular pyramid with apex infinity; reflection
in that hemisphere gives the lower half with apex zero. Split the
base along the diameter from 1 to -1. The two upper tetrahedra have
the Euclidean triangle (1,zeta,-1), or (1,-zeta,-1), as a horospherical
triangle at infinity. Each has angles pi x,pi(1/2-x),pi/2, up to
permutation. Reflection gives two more tetrahedra of the same volume.

These four tetrahedra fill the convex hull in (9). One can check
the supporting planes directly: the vertical halfspace over each
rectangle edge contains the origin, because the rectangle contains
its center. It therefore contains ALL six vertices. Reflecting that
halfspace in the unit hemisphere fixes the four rectangle vertices
and exchanges zero and infinity, so the four lower face halfspaces
contain all six vertices as well. Their eight triangular faces form
the octahedral boundary. Along a shared rectangle edge, the two interior dihedral
angles sum to either 2pi x or pi-2pi x, both strictly less than pi.
The remaining pyramid edges have angle pi/2. Thus the joined boundary
is locally convex; equivalently its eight triangular face planes
support all six vertices. There is no hidden negative-volume piece.

It follows that 2pi e(1/2,x)=Vol(O_x). At x=1/4 its eight faces
form the regular ideal octahedron and its volume is v8. Equation (5)
gives this as the unique maximum in this family. This is a geometric
interpretation of ONE native degree-block energy, not a claim that
this octahedron is already a cell in the supplied link complement.

## 4. The compulsory face subtraction away from the fold

The same interpretation is signed for other colors. The elementary
duplication identity

    Lambda(2a)=2Lambda(a)-2Lambda(pi/2-a)

converts (4), for 0<x<xi<1/2, to

    2pi e(xi,x)
       =4 Vol T(pi x,pi(xi-x),pi(1-xi))
                         -4Lambda(pi(1/2-xi)).       (10)

The second term is forced by the original measure (2). It is positive
before its subtraction, since Lambda is positive on (0,pi/2).
At x=0 the tetrahedron flattens and

    e(xi,0)=-(2/pi)Lambda(pi(1/2-xi))<0.             (11)

Consequently no representation of EVERY CD-normalized magnetic
summand's action as a sum of nonnegative ideal-cell volumes can be
correct without additional boundary terms or cancellations. This
does not prevent the completed energy from having a positive
geometric maximum: (6),(7) prove that its maximum is strictly positive.
It identifies a necessary normalization in any such argument.

## 5. What a shared-variable action must retain

For general physical degree and channel, the exact local energy is
sum_u |C_j(t,u)|^2/|sigma_(t,j)|. On strict compacts where the selected
ordinary packet applies, its summand has the action

    2 Re Phi_xi(tau,nu)-kappa(tau,xi),               (12)

where kappa is the leading logarithm of the ACTUAL measure. Here tau,
nu and xi are real admissible scaled physical indices; the complex
packet supplies their selected action, not a different complex-degree
operator norm. In the
two chambers supplied by its factorial formulas,

    kappa=J(tau-xi)+J(tau+xi)-2J(tau), tau+xi<1,
    kappa=J(tau-xi)+J(tau+xi-1)-2J(tau), tau+xi>1.   (13)

The odd self-paired endpoint has the corresponding limit
2J(tau-1/2)-2J(tau). Polynomial factors in the finite measures do
not contribute to (13). Formula (12) describes a normalized summand;
the sum over u and the sum over physical degree are still to be taken.

If a positive comparison energy is constructed by sewing these actual
columns, its candidate action is the SUM of (12), together with the
remaining original boundary weights, restricted to the SAME magnetic
wire variables and exact affine degree constraints used in that
sewing. Taking separate maxima in tau or nu before sewing changes
that variational problem. Neither the existence of such a useful
global comparison nor its equality with the manifold's angle-volume
problem is proved here.

The selected geometric framing generally gives COMPLEX magnetic
coordinates. The localization theorem puts them in the selected
physical tube, but does not put them on the real grid defining this
positive energy. An identification with a real angle polytope, or a
justified deformation of the original sum, is therefore an additional
step; the local complex packet alone supplies neither.

There is a further exact local warning about stationarity. Equation
(1) has the marked highest-weight action

    Phi_high(xi,x)=J(xi)-J(x)-J(xi-x)+pi i xi x.

At the energy maximum x=xi/2,

    partial_x Phi_high=pi i xi,
    exp(partial_x Phi_high)=exp(pi i xi).            (14)

At the folded value this multiplier is i, although the real energy
derivative vanishes. Real-energy stationarity constrains the modulus
of a transport multiplier; it does not by itself impose its marked
phase or a full complex gluing equation. In a real link network those
phases may cancel through the actual shared incidence and boundary
characters, but that requires a separate proof. This example does not
assert that an open column ought to have trivial boundary momentum.

Thus the missing global bridge is precise: construct the actual sewn
energy with its signed face terms and shared variables, and prove
that its stationarity, INCLUDING the retained phase and peripheral
conditions, gives the degree-one geometric gluing. The local octahedral
volume and the correctly normalized summands alone do not establish
that bridge or a nonzero original quantum period.

## 6. The larger full folded cost is twice an ideal cube volume

The separate [full magnetic-energy theorem](actual_matching_edge_magnetic_energy_profile.md)
now computes the full folded operator rate as 5v3/pi, with effective
volume 10v3, for the odd simple projector and the actual even completed
pair. This maximizes over physical degree and is strictly larger than
the highest-weight block cost in (8). Here is an explicit local
polyhedron with that larger two-copy volume.

In Minkowski coordinates with form (-+++), let

    V_epsilon=(sqrt(3),epsilon_1,epsilon_2,epsilon_3),
    epsilon_i in {+1,-1}.

These null vectors project to the eight Klein vertices of the cube
[-1/sqrt(3),1/sqrt(3)]^3. The four vertices with product epsilon_i=+1
form a regular ideal tetrahedron: every distinct pair has the same
Lorentz product, and the signed coordinate symmetries permute its
vertices. Its face opposite V_epsilon has normal

    n_epsilon=(1,-sqrt(3)epsilon_1,
                    -sqrt(3)epsilon_2,-sqrt(3)epsilon_3),
    <n_epsilon,n_epsilon>=8,
    <V_epsilon,n_epsilon>=-4sqrt(3).

Reflection in that face sends the opposite vertex to

    V_epsilon-2<V_epsilon,n_epsilon>n_epsilon/8
                                  =2V_(-epsilon).                (15)

Thus the four adjacent corner tetrahedra are also regular ideal
tetrahedra, congruent to the central one. They fill the cube without
overlap. Indeed the central tetrahedron has the four Klein inequalities
epsilon dot x>=-1/sqrt(3), for sign triples of product +1. Inside the
cube, two such inequalities cannot fail simultaneously: adding them
would violate one coordinate bound of the cube. The part failing one
inequality is precisely the tetrahedron with its opposite cube corner
and the three neighboring central vertices. This gives the usual
central tetrahedron and four corner tetrahedra as an actual geometric
partition.

Each original cube edge lies in one regular tetrahedron and has
dihedral angle pi/3. Along each triangulated square-face diagonal,
three tetrahedral angles add to pi. This is the regular ideal
six-square-faced cube, with its stated angle data.

Consequently this regular ideal cube has volume 5v3, and TWO copies
have volume 10v3. This is an exact geometric interpretation of the
local full folded COST. It supplies no face pairing, cusp marking,
degree-one chain, or volume upper inequality for the original link
complement. Attaching the local cube to a source diagram remains a
separate shared-incidence problem.

Focused audit: [original highest vectors, CD measures and ideal shapes](../experiments/audit_actual_native_magnetic_energy_local_geometry.py).
It verifies 817 original finite highest-vector entries with their phases,
167 bilinear measures, 23 even/odd folded measure formulas, and all four
actual tetrahedron cross ratios. The global sewing and phase-matching
problem is not a conclusion of these checks.
The cube addition also checks all four Lorentz reflections (15) exactly.

The theorem concerns a degree block. It does not identify cells in the actual source complement, a real-grid geometric saddle, or a global volume equality.

The cube volume is a local boundary-cost interpretation. It is not identified with the right-angled matching polyhedron; the topology of those constructions remains distinct.