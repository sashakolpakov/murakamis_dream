# Twist-knot identification and exact peripheral certificates

Research note, 25 October 2026. This supplements the uniform geometric and
matrix proof in [twist_family_audit.md](twist_family_audit.md). The ordered
face data come from Ben Aribi–Guéritaud–Piguet-Nakazawa,
[arXiv:1903.09480v5](https://arxiv.org/pdf/1903.09480v5), Figures 7–14 and
17–23. We reconstruct the local topological operations below. We do not use
their identification of a preferred longitude, geometricity theorem, or
quantum asymptotic theorem as premises.

There are two different kinds of evidence here. The local constructions and
the formulas with arbitrary p give the arguments for the whole family. The
exact script and Regina recognition at the end are independent finite
diagnostics of the transcribed data. Finite recognition alone would not
establish an infinite-family knot identification.

## 1. Ordered triangulations and their marked extensions

Use p>=0, f_0=e_1, and the face tuples and signs from Section 1 of the
geometric note. In particular,

    T_j=(e_j,e_(j+1),f_j,f_(j-1)),
    U=(r,v,s,g),
    odd:  V=(g,s,f_p,u), W=(u,r,v,e_(p+1)),
    even: V=(s,g,f_p,u), W=(u,v,r,e_(p+1)).

Every face pairing maps the three vertices in increasing order. The ideal
triangulation is denoted X_p. Its compact marked extension Y_p is obtained
by adding

    Z=(m,m,s,s'),

changing V's face 1 from s to s' in the odd case, or U's face 2 from s to s'
in the even case. The marked knot edge is Z_23. Pairing the two m faces
uses the full vertex permutation (01); it fixes 2 and 3. These conventions
also cover p=0, without any chain tetrahedron.

### 1.1 Reconstruction from the twist diagram

Let K_n be the twist knot with a two-crossing clasp and an alternating
n-crossing twist region, with the mirror convention fixed by the oriented
diagram in Figures 7 and 17 of the source. Thus

    odd: n=2p+3,       even: n=2p+2.

In particular K_2 is 4_1, K_3 is 5_2, and K_4 is 6_1. The parameter n is
not the total crossing number of this reduced diagram: that number is n+2.

Here is a reconstruction of the diagram-to-face-data argument. It is useful
to distinguish actual local changes of a decomposition from any quantum
move identity; only topology is involved in this subsection.

1. Put vertices at the middle of the diagram arcs, with one additional
   vertex on the clasp arc, and draw a quadrilateral around each crossing.
   The two knot arcs at that crossing are opposite edges of an embedded
   crossing tetrahedron. Replace this block by an interval: the two knot
   edges become its ends, while its four lateral edges become the interval.
   The local quotient has the same regular neighborhood as the original
   block, with the four exterior sectors in the same cyclic order. One can
   see this by shrinking transverse disk sections inside a collar and
   expanding the adjacent collar by the same amount. Reversing the
   operation expands the interval back to the crossing block and restores
   the two knot arcs. Thus the resulting quotient and its marked curve
   describe the same pair (S^3,K_n). The crossing information is retained
   in the cyclic attachment of the exterior sectors.
2. After these disjoint local replacements, the regions above and below
   the projection are two balls. Their boundary face pairs are D,E,m,r,s.
   The arrow identifications are read by following one sector of each
   crossing: successive arrows in the long twist region alternate.
   Glue the two balls along the disk E. The result is one ball with paired
   faces D,m,r,s and one surviving marked knot edge. This is a disk gluing
   of two balls, rather than an assumption about a face-pairing quotient.
3. The repeated reduction in the twist region is a disk cut and regluing.
   Split a paired face F into a residual face and a triangle; isolate the
   adjacent ball with two triangular faces and one bigon; rotate this ball
   and reglue it along the triangular disk; then merge the residual face
   with the bigon. Each operation has its inverse, and the rotating ball
   misses the marked knot edge. This proves preservation of the pair.
   The effect on the boundary is to replace two successive twist edges by
   one long edge and move the triangle u upward by one level. These are
   exactly the labeled attachments in source Figure 10. Repeat p times.
4. In the odd case the residual pair of (p+2)-gons G is triangulated by a
   fan. The successive layers have boundary face tuples
   (e_j,e_(j+1),f_j,f_(j-1)). The clasp region has four tetrahedra; reading
   the faces opposite 0,1,2,3 gives

       U=(r,v,s,g), V=(g,s',f_p,u),
       W=(u,r,v,e_(p+1)), Z=(m,m,s,s').

   This reads the common triangular face at each layer, so it is unchanged
   when an additional level is added to the fan. For p=0 the fan is absent
   and the last two boundary faces have the common name f_0=e_1.
5. In the even case the same p disk reductions leave the opposite clasp
   attachment. Separate off the ball along the quadrilateral formed by
   the two adjacent G faces and change its diagonal. Both diagonals
   triangulate the same ball relative to its exterior boundary. The fan
   still has the preceding T_j tuples. Reading the residual clasp gives

       U=(r,v,s',g), V=(s,g,f_p,u),
       W=(u,v,r,e_(p+1)), Z=(m,m,s,s').

   This is the diagonal change visible in source Figure 21. For p=0 the
   intervening bigon is collapsed in its collar, so the same tuples with
   f_0=e_1 apply. No negative or zero number of layers is used.

All the face maps in this reading preserve the increasing order of their
three vertices. The signs in the geometric note follow by orienting the
ball and each tetrahedron. This gives a construction of Y_p as the marked
pair (S^3,K_n), rather than an inference from its homology or from a finite
list of recognized manifolds.

### 1.2 Why removing Z gives the knot complement

The quotient of Z by its m pairing is a ball. Its unpaired faces 2 and 3
are two disks meeting along their common equator 01: in each disk the two
radial sides have been identified. Their centers are 3 and 2 respectively.
The edge 23 is the unknotted proper arc joining these centers. Removing a
small neighborhood of that arc gives the product between the two punctured
disks. Absorbing this product into a collar identifies the punctured disks.

The equator vertices map 0->0, 1->1 and the centers map 3->2. Composing with
the two external face maps gives precisely the increasing vertex map
between the two s faces in X_p, in both parities. Thus drilling the marked
edge and deflating this product gives X_p, with no change to the remaining
tetrahedra. In particular X_p triangulates S^3 minus K_n.

The same local description explains the topology of the cusp. The vertex
link in Y_p is a sphere; deleting the two marked-edge germs and adjoining
the tube around the open edge makes a torus. The computation in Section 3
uses this description to identify the meridian without a linking-number
guess.

## 2. A separate uniform homology check

Orient each dual face edge from its first to its second occurrence in the
ordered tetrahedron list. A spanning tree in the dual graph is

    e_2,...,e_(p+1),r,s.

After contracting it, the generators are e_1,f_1,...,f_p,v,g,u. All edge
relations below are abelianized boundaries of the actual dual edge disks;
each is determined by crossing the consecutive faces incident to the edge.
For p>=1 put f_0=e_1. The relations, up to reversing individual disk
orientations, are

    f_j-f_(j-1)=0                         (1<=j<p),
    f_p-f_(p-1)-g+v=0,
    g-v-f_p=0,
    -v-g=0,
    sum_(j=1)^p f_j+u+2e_1=0.                              (2.1)

These formulas hold in both parities. The first two relations involving
f_p add to -f_(p-1)=0. Back substitution then gives

    e_1=f_1=...=f_(p-1)=0,
    v=-g, f_p=2g, u=-2g.

Every elimination has a unit integral pivot. There is no remaining relation
on g and no torsion; hence H_1(X_p;Z)=Z. For p=0 the three relations are

    -v-g=0, v-2e_1+u-g=0, v-g-e_1=0,

and give v=-g,e_1=-2g,u=-2g, again with no relation on g.

The single dual 1-chain g-s before tree contraction will be the meridian.
Thus its class is the displayed generator, not a multiple of it. Homology
by itself would not identify this class with the meridian of the knot;
that requires the next local argument.

The chain T_1,...,T_p by itself is also a useful diagnostic. For p>=1 it
is a layered solid torus with top faces 1 and 2. If A is its boundary
edge 01/23 and B is 02/13, their images in its H_1 are a and (p+1)a;
edge 03 has image (p+2)a. For p=1 the two face relations give B=2A
and 03=3A. Adding a layer leaves A unchanged, sends the new B to the
previous 03, and sends the new 03 to A plus that previous 03. This proves
the formulas inductively. Its meridian slope is (p+1)A-B and its three
unoriented meridional cuts are (1,p+1,p+2). This solid-torus description
does not assert that the fixed three-tetrahedron clasp piece is a
two-cusped link exterior.

## 3. The actual meridian, from the marked edge

A cusp normal walk is listed as (tetrahedron, vertex, exit face). The entry
face is determined by the preceding step. Define

    odd:  mu=((U,1,3),(V,2,1)),
    even: mu=((U,1,3),(V,2,0)).                             (3.1)

Thus U_1 enters through s and leaves through g; V_2 returns through s.
This is a simple two-arc curve. Its dual 1-chain is g-s.

To verify that it is a meridian, lift it to the spherical vertex link of
Y_p before drilling. Insert one arc in Z_1 at the s crossing. The resulting
closed three-arc walks are

    odd:  ((U,1,3),(V,2,1),(Z,1,2)),
    even: ((U,1,3),(V,2,0),(Z,1,3)).                       (3.2)

They separate the two germs of the marked edge Z_23. Here is a constant-size
certificate that can be checked directly from the face tuples. One side
contains the three whole link triangles

    odd:  U_3,W_3,Z_3,       even: U_3,W_3,Z_2,

and, in both parities, the following corner regions of the three cut
triangles:

    U_1: corner 0;
    V_2: the region containing corners 0 and 1;
    Z_1: corner 0.

There are thirteen local corners in this region: nine in whole triangles
and four in the cut pieces. Each non-cut edge is matched within the region;
its only boundary is (3.2). In the odd case it contains germ (Z,3;2) but
not (Z,2;3); in the even case it contains (Z,2;3) but not (Z,3;2). All
these triangles are in the fixed clasp block; no chain tetrahedron enters
the certificate. On the sphere, the simple curve (3.2) therefore bounds a
disk containing just one marked-edge germ. After the two germs are removed
and the tube is attached, it is precisely a meridian. Deflation gives (3.1).

This proves the meridian claim independently of the source cusp drawing.

## 4. A preferred longitude without a diagrammatic linking count

The following auxiliary simple normal walks beta stay in the fixed clasp
block. Each row is (tetrahedron, vertex, exit face), read cyclically:

| Step | Odd beta | Even beta |
| --- | --- | --- |
| 1 | (U,0,1) | (U,0,1) |
| 2 | (W,0,1) | (W,0,2) |
| 3 | (U,1,2) | (U,1,2) |
| 4 | (V,2,3) | (V,2,3) |
| 5 | (W,3,1) | (W,3,1) |
| 6 | (U,3,2) | (U,3,2) |
| 7 | (V,3,0) | (V,3,1) |
| 8 | (U,2,0) | (U,2,0) |
| 9 | (W,2,0) | (W,1,0) |
| 10 | (V,1,0) | (V,0,1) |

The cusp is oriented by the oriented complement. Direct normal-arc
intersection gives

    mu . beta = +1 (odd), -1 (even).                       (4.1)

For an entirely rational check, place the vertices of each cusp triangle at
(0,0),(1,0),(0,1) in increasing order. Put mu's endpoints one-third of the
way along each side and beta's endpoints two-thirds of the way along it.
The increasing face maps match these positions across triangles. Count
the transverse interior segment intersections with triangle orientation
-epsilon_t(-1)^v. This evaluates (4.1) using only the two triangles visited
by mu. It also avoids coincident-arc conventions.

Their dual face chains are

    odd:  [beta]=-r+v+2s-2g,
    even: [beta]=2s-2g.

Using (2.1), beta has homology class -3[mu] in the odd case and -2[mu]
in the even case. Define on the peripheral torus

    odd:  lambda=beta+3mu,
    even: lambda=beta+2mu.                                 (4.2)

There is a direct integral boundary certificate, with no division or
specialization. The dual disk at U_01 has oriented face word

    s u v^(-1) r u^(-1) g^(-1)

in the odd case. Its abelian boundary is s-v+r-g. Consequently the odd
lambda chain -r+v-s+g is minus this boundary. In the even case lambda's
dual chain is already zero. Thus both classes in (4.2) are null-homologous
in the complement. Equation (4.1) makes each lambda primitive. Since mu is
the actual meridian, these are preferred longitudes, with the orientation
specified by (4.1). This argument replaces a crossing-sign linking count.

## 5. Angular branches and the exact longitude rows

Let a,b,c be the local edge angles, in radians, assigned to opposite
edge pairs 01/23,02/13,03/12. For a normal arc at (t,v) entering face i
and leaving face j, let k be the unused vertex. Its signed corner-angle
contribution is

    epsilon_t (-1)^v sign((i,j,k) relative to the sorted other vertices)
        times the angle at edge vk.                       (5.1)

This follows by orienting the vertex link triangle and following its
oriented incoming and outgoing sides. It fixes the signs rather than
assigning an unsigned sum to a normal walk. Applying it gives

    h_mu = a_U-a_V                    (odd),
    h_mu = a_V-a_U                    (even),

    h_beta = -b_U-c_U-a_V-b_V+c_V+2a_W+c_W   (odd),
    h_beta = a_V-b_V+c_V+a_W-b_W-c_W         (even).

Put T_t=a_t+b_t+c_t and let

    omega_s=2a_U+b_V+c_V+a_W+b_W.

The target longitude formulas are

    h_lambda=2(a_U-a_V+c_V-b_W)        (odd),
    h_lambda=2(-a_U+a_V-b_V+a_W)       (even).               (5.2)

These follow from (4.2) with exact constraint certificates:

    odd:  (5.2)-(h_beta+3h_mu)=T_U+2T_V-T_W-omega_s,
    even: (5.2)-(h_beta+2h_mu)=-T_V+T_W.

On the balanced angle space T_t=pi and omega_s=2pi, both right sides are
exactly zero. In particular no unnoticed multiple of 2pi is needed to match
the source formula. This is stronger than equality modulo angular holonomy.

For the shape convention in the geometric note, a,b,c correspond to
z,z'',z' at positive tetrahedra and z,z',z'' at negative ones. Using
T_W=pi in the odd case and T_V=pi in the even case converts (5.2) to

    h_lambda=a_l Arg z+b_l Arg z''-2pi,

with chain entries zero and the U,V,W rows

    odd:  a_l=(2,-2,2),  b_l=(0,2,2),
    even: a_l=(-2,4,2),  b_l=(0,2,0).                      (5.3)

Thus the longitude rows and the branch constant nu_l=2pi used in the
geometric and Gaussian certificates are now independently identified.
The natural spectral boundary coordinate x=y_V-y_U has angular meridian
a_U-a_V in both parities. It reverses mu in the even case; its intersection
with the chosen preferred longitude is consequently +1 in both cases.

## 6. Consequence and the remaining scope

For every fixed p>=0 in both parities, the uniform topological
identification, the independently identified peripheral rows, and the
geometric certificates in the companion note apply to the same literature
integral. Therefore the state defined by FAMED equation (4.5), with the
explicit spectral rescaling and b-shift convention in
[general_annihilator_and_volume.md](general_annihilator_and_volume.md), has
a primitive minimal boundary annihilator and satisfies

    lim_(b->0+) -2pi hbar log|J_(X_p)(hbar,0)|
          = Vol(S^3 minus K_n),
    hbar=b^2/(1+b^2)^2.                                    (6.1)

Its classical symbol contains the geometric peripheral component in the
recorded eigenvalue-ratio/lift convention. The limiting state normalization
is fixed by the literature integral. This is a statement for these explicit
literature realizations. The identification of all triangulations or all
purported standard knot states requires the global quantum transformations
with their generic peripheral factors and contours. It does not follow
from the topological disk operations used in Section 1. No equality of the
entire classical symbol with the full A-polynomial is inferred here.

The all-alternating-knot extension also remains open in this program;
the positive geometric and matrix certificates have been supplied here
for the twist families. A Menasco decomposition alone does not supply those
certificates or an exact quantum move identity.

Run the exact cellular and normal-curve checks with

    python3 experiments/twist_topology_audit.py

and the optional independent 3-manifold recognition with

    .venv/bin/python experiments/twist_topology_audit.py --regina

The latter uses Regina 7.4.1 and SymPy 1.14. It recognizes Y_p as S^3,
checks X_p has one ideal torus cusp and H_1=Z, recognizes Z as a ball,
and checks the layered-solid-torus cuts for p=1,...,8. Both modes check
the eighteen cases p=0,...,8 in both parities against the uniform homology,
marked-germ, intersection, integral-boundary and zero-branch certificates.
The source figures specify the input drawings; the local reconstruction
and the all-p certificates, rather than these finite checks, justify the
family statement.
