# Actual seams and a topological obstruction for positive Conway sources

29 October 2026. The positive Conway partition has an exact whole-source
limit, but its list of ideal-volume atoms is not automatically a
triangulation. Two structural facts sharpen that distinction. Every
final multiplication contains three forced flat atoms. More decisively,
an infinite subfamily of the actual compiled links has explicit annuli
between different boundary tori, and admits no complete finite-volume
hyperbolic metric. This is a topological disk certificate, rather than
an inference from a polynomial invariant.

The objects, turns and closure are those of the
[physical Conway compiler](actual_positive_complete_circle_conway_trees.md).
Write C=L_N, h=Rturn C and A=h^3. The
[whole-source variational theorem](actual_positive_conway_variational_limit.md)
is used without changing its original mark, its full circle operators,
or its repeated-root normal directions. No new volume equality for
arbitrary expression trees is claimed here.

## 1. A product closure is an exact seam with three flat atoms

Let f=sum f_i Bhat_i and g=sum g_j Bhat_j. At an actual product followed
by the original phi closure, the Newton multiplication rule forces

    k=d, i+j=d, mu_(i,d-i,d)=1, d=N-1.

Consequently the full repeated-root algebra gives

    phi(fg)=sum_(i=0)^d f_i g_(d-i).                 (1)

This is the genuine original Frobenius pairing, including all normal
directions. It is not a nodal or semisimple replacement. The unit
coefficient follows directly by cancelling the six sine factorials in
the exact multiplication formula.

The continuum constraints are z=1 and x+y=1. In the notation of the
variational theorem,

    p=z-x=y, q=z-y=x, r=x+y-z=0, w=1-x-y=0.

The three formal product tetrahedra are therefore

    (y,x,0), (y,x,0), (1,0,0).                      (2)

They have zero volume for EVERY feasible state. Thus the unreduced
list of formal tetrahedra can never be a strictly positive ideal
triangulation of a product-closed complement, even when that complement
is hyperbolic. These atoms must first be removed or interpreted as a
seam. Their flatness is not a failure of the quantum limit theorem.

There is a second exact closure rule:

    phi(Rturn f)=f_0=f(c_0),
    (fg)_0=f_0 g_0.                                (3)

Indeed only Bhat_0 is nonzero at c_0, and a product at coordinate zero
has i=j=k=0. Equations (1),(3), together with reversal r->d-r at a
turn, give a finite closure-reduction algorithm for EVERY expression
tree. They are exact source identities, rather than moves that delete
a physical circle. In particular they do not authorize replacing a
four-punctured Conway sphere by a geodesic pair of pants.

## 2. The main-strand pairing is computable before evaluation

Forget the auxiliary circles but retain the actual planar main arcs.
Use boundary order (bottom-left,bottom-right,top-left,top-right).
The circle box C has pairing

    I={(0,2),(1,3)},

while its genuine quarter-turn h has pairing

    U={(0,1),(2,3)}.

Neither deleting an auxiliary component nor this pairing calculation
changes the tangle being evaluated; this is only a record of its main
components. Main arcs have no mutual crossings. In a product, identify
the two top ports of the lower box with the bottom ports of the upper
box. Union of these pairings gives the new boundary pairing and counts
every internal main circle. A quarter-turn cyclically reorders the
four ports, interchanges I and U, and preserves internal circles.
Closing by phi adds the two corresponding top-to-bottom connections.

This is an exact combinatorial algorithm for the number and main
port membership of components of any compiled expression. It does
not determine its complement from a linking matrix: the actual
positions of the threaded disks still matter.

In particular h^s has U boundary pairing and s-1 internal main circles.
Its phi closure has s main components. The phi closure of Rturn(h^s)
has s+1 main components: rotation changes the last closure into the
top-and-bottom cap closure of h^s. In both cases there are s retained
auxiliary circles. Thus the latter actual link has 2s+1 components.

## 3. A literal disk model for the cap-closed run

Here is an explicit embedding of the cap closure of h^s, for EVERY
integer s>=1. It is also a local geometric model of the compiler,
not a manifold recognized from its quantum value.

Use coordinates (X,Y,Z) in R^3. Put y_i=4i, 1<=i<=s. In the i-th
box the upper and lower main U-arcs lie in Z=0. Their horizontal
segments are

    -1<=X<=1, Y=y_i+1 and Y=y_i-1,

with vertical connectors at X=+-1 to the corresponding ports at
Y=y_i+-2. Its auxiliary circle and its spanning crossing disk are

    C_i: X=0, (Y-y_i)^2+Z^2=2,
    D_i: X=0, (Y-y_i)^2+Z^2<=2.                    (4)

This is the actual threaded circle: its disk meets the two main arcs
once each. Before rotating the box, it is the ordinary loop around
two parallel through arcs. Reading its outgoing and returning strand
gives exactly the mixed braid [2,1,1,2] and its third-strand closure.
Rotating this embedded box in the projection plane gives h, with no
added crossing or framing twist. Rounded corners do not affect any
of the intersections below.

Stack these boxes by their recorded ports and close their top and
bottom pairs by planar caps outside the boxes. The resulting main
circles M_0,...,M_s are boundaries of disjoint planar rectangles:

    M_0: [-1,1] x [y_1-3,y_1-1],
    M_i: [-1,1] x [y_i+1,y_i+3], 1<=i<s,
    M_s: [-1,1] x [y_s+1,y_s+3],                  (5)

all at Z=0. Their sides at X=+-1 are precisely the identity stack
wires or the external caps. Equations (4),(5) recover the literal
quarter-turned boxes and their cap closure.

The two intersections of C_i with the projection plane have
Y=y_i+-sqrt(2). The lower one lies in the rectangle for M_(i-1),
and the upper one in the rectangle for M_i. No other rectangle
contains either point. The disks D_i are mutually disjoint since
their center spacing is 4>2sqrt(2). Each D_i meets only M_(i-1)
and M_i, once each, at Y=y_i-1 and y_i+1 respectively.

In particular the planar disk bounded by M_s meets C_s ONCE and
is disjoint from every other component. Delete M_s. The disk D_s
now meets just M_(s-1), once, and no other component. Delete C_s;
the unused terminal cap on M_(s-1) can be shortened in this empty
end region. What remains is the same cap closure with s-1 boxes.

Induction proves a precise link description: starting with the
marked unknot M_0, insert a meridian C_1 of M_0, then a meridian
M_1 of C_1, and repeat. Equivalently the cap-closed h^s is an
iterated meridian-insertion link with path

    M_0 -- C_1 -- M_1 -- ... -- C_s -- M_s.        (6)

The disk witnesses, not just the abstract path or pairwise linking
numbers, are essential to this assertion.

## 4. These actual links are not finite-volume hyperbolic

Remove small neighborhoods of all link components. The disk bounded
by M_s, punctured by C_s, becomes a properly embedded annulus with
one boundary on T_(M_s) and the other on T_(C_s). Its core represents
the meridian of C_s, nonzero of infinite order in H_1 of the link
exterior. Hence the annulus is incompressible. Its two boundary
components lie on different boundary tori, so it is not boundary
parallel.

If the interior of this exterior had a complete finite-volume
hyperbolic metric, the annulus would freely homotope a nontrivial
peripheral element of one cusp to an element of a distinct cusp.
Both would be the same nontrivial parabolic after transporting the
basepoint along the annulus. A nontrivial parabolic fixes a unique
ideal point. Stabilizers of that ideal point determine one cusp,
so distinct cusp groups cannot have such an intersection. This is
a contradiction. Thus no complete finite-volume hyperbolic metric
exists on the literal exterior in (6).

This gives an infinite family WITHIN the robust Conway class:

    E_k=Rturn(A^k)=Rturn(h^(3k)), k>=1.            (7)

Each has 6k+1 components and the exhibited annulus. In particular,
no theorem identifying every positive Conway maximum with a
complete hyperbolic complement volume can hold without an additional
topological restriction or a JSJ-type reformulation.

There is also an independent check of the exact polynomial source.
The original complete meridian around one physical V_N acts by

    L_N(-2)=(-1)^d U_d(-1)=N.

Here -2=q^N+q^-N is the single-head Casimir. The disk/collar
insertions in (6) are zero framed, and the actual duality snakes
transport the self-dual main object without a curl. Keeping the
mark on M_0 and removing from the opposite end therefore supplies
one factor N per removed meridian. The starting marked unknot is 1.
Thus the actual raw source is N^(2s). This agrees with the entirely
independent full-normal Newton calculation

    phi(Rturn(h^s))=(h_0)^s=(N^2)^s.              (8)

In the variational polytope, the output of h^s is forced to zero.
Every one of its product inputs and every leaf is then zero. All
leaf and product volume atoms vanish. Its maximum is exactly zero,
at all levels and without estimating an oscillatory sum.

## 5. What a valid broader geometric comparison must retain

The following conclusions narrow the missing geometric gate.

* First reduce the exact closure seams (1)--(3). A positive ideal
  triangulation cannot include the three always-flat closure atoms.
* Exclude or explicitly split off a WITNESSED meridional end as in
  (4),(5). A mere valence test on the disk-incidence graph is not
  a substitute for its embedded disk.
* A Conway composition is a four-punctured-sphere gluing. Its metric
  has moduli. The geodesic-pants and matched-horocycle argument for
  the [actual belt-stack pieces](actual_balanced_octahedral_belt_stack_volume.md)
  does not apply to that sphere just because the scalar pairing
  (1) is exact. In that separate construction the actual disk cut
  and all face maps are proved before volume additivity is used.
* For a proposed positive-angle realization of the remaining atoms,
  retain the literal face identifications and the full edge and
  peripheral equations. Stationarity along the wire polytope alone
  does not establish the full fixed-periphery criticality in the
  [source-volume certificate](source_volume_casson_rivin_certificate.md).

The already proved whole-theta calibration phi(h^3) and its actual
four-octahedron geometry survive these restrictions. An all-tree
topology/angle-incidence theorem after the reductions above remains
open. This note proves an exact obstruction and a source-preserving
closure reduction; it does not replace that missing theorem by a
generic conditional volume assertion.

Audit: [exact seams, component pairings, disk intersections and original
marked closures](../experiments/audit_positive_conway_geometric_incidence.py).
The written disk induction proves the all-s topology; finite checks
do not infer it from a numerical invariant or manifold recognition.

The actual embedded disks, rather than the scalar or linking graph alone, are the topological evidence. No arbitrary-tree volume identification is included.