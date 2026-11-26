# The actual crossing sum and the complete Bloch fundamental class

Research note, 26 October 2026. This closes a classical comparison
left open in [the marked braid note](marked_braid_holonomy.md).
The setting is an oriented hyperbolic knot complement, its complete
geometric representation, and the actual reduced ADO crossing
conventions already fixed. At the complete color the crossing
Bloch sum is the oriented idealized fundamental class. In particular
its Bloch--Wigner regulator is the hyperbolic volume.

The comparison is in the rational oriented pre-Bloch group. It
does not identify an integral flattening, a full complex quantum
period, or the component selected by the actual finite contraction.
The original volume conjecture remains unproved.

## 1. Statement and conventions

Use the balanced factorial basis of the preceding note. For
q=exp(pi*i/N), Q=q^2, x=q^alpha and M=-qx, its positive
crossing has input A=Q^a,B=Q^b, shift C=Q^k, and symbol

    beta_+=[B]+[C]+[x^2/A]-[BC]-[x^2C/A].           (1.1)

The inverse crossing has the independently checked symbol

    beta_-=[A]+[C]+[x^2/B]-[AC]-[x^2C/B].           (1.2)

At the classical complete color M=1, x=-1. The actual
critical correspondence supplies meridians mu_j=-H_j of trace
2, and their Hurwitz crossing relation. Fix the geometric
representation with the orientation of the knot exterior.
Let beta_D be the sum of (1.1)--(1.2) over the diagram at this
critical representation, with its regular frame.

Then

    beta_D=beta_[M,partial M] in P(C) tensor Q,
    D(beta_D)=Vol(M).                              (1.3)

Here the right side is the marked idealized fundamental class,
not an unspecified lift of the peripheral wedge. If T is the
positive complete triangulation supplied by the audited existence
theorem, the same statement is

    beta_D=sum_(Delta in T)[z_Delta].               (1.4)

It is useful to separate this from the remaining quantum claim:
(1.3) identifies the classical Bloch period attached to the actual
coefficients. It does not prove the growth rate of their sum.

We use normalized oriented configurations: a tuple with repeated
developed points is zero, and reversing a tetrahedron reverses
its symbol rationally. Cross-ratios are

    r(v0,v1,v2,v3)
       =det(v3,v1)det(v2,v0)/(det(v3,v0)det(v2,v1)),
    r(infinity,0,1,z)=z.                           (1.5)

The boundary of five points is the five-term relation. If some
points coincide, its remaining alternating terms cancel in pairs.
Thus normalized degenerate configurations cause no additional
Bloch generator. This matters for diagrams with redundant arcs.

## 2. Region vectors come directly from the actual holonomy chart

Consider a positive crossing. Write a for the over-meridian,
b for the incoming under-meridian, and c=a^(-1)ba for the
outgoing under-meridian. The same letters in a tetrahedron
denote their unique fixed flags. Choose unipotent SL(2) lifts.
Choose a generic region vector s and an auxiliary vector p.
Put

    s_0=s, s_M=a s, s_P=c s, s_R=b a s=a c s,
    p_1=a p, w_i=det(p,s_i).                       (2.1)

Region vectors propagate across an oriented arc by its meridian
or inverse. The equality ba=ac is exactly the consistency
condition at a crossing. Hence the data propagate over the
projection sphere; all dual-face relations are these crossing
relations. The initial region vector is arbitrary. These are
the same region words obtained by multiplying the actual
Hurwitz meridians, not an additional representation.

To verify the coordinates, let P_j=mu_j...mu_1 in a braid
slice, and set w_j=(P_j)_11 in the frame p=(0,1),s=(1,0).
The previous Gauss reconstruction gives

    K_j=-(w_j/w_(j-1)), A_j=x/K_j.

The minus sign is from H_j=-mu_j. At x=-1, near one crossing,

    A=w_0/w_M, B=w_M/w_R,
    C=w_0 w_R/(w_M w_P).                           (2.2)

The last relation follows equally from
C=K_2/K'_1. Therefore the actual expression (1.1) becomes

    [w_M/w_R]+[w_0w_R/(w_Mw_P)]+[w_M/w_0]
                      -[w_0/w_P]-[w_R/w_P].       (2.3)

The nondegenerate Gauss chart constructed in the preceding note
keeps these five arguments away from 0 and 1. The auxiliary
vectors can additionally avoid the finitely many coincidences
used in the calculations below.

## 3. An explicit three-five-term certificate

Write T(v0,v1,v2,v3) for the oriented tetrahedron symbol in
(1.5). The fixed flag of a is also denoted a, and similarly
for b,c. Unipotence and determinant preservation give

    T(a,p,s_0,s_M)=[w_M/w_0],
    T(b,p,s_M,s_R)=[w_R/w_M],
    T(a,p,s_P,s_R)=[w_R/w_P],
    T(c,p,s_0,s_P)=[w_P/w_0],
    T(s_M,s_R,p_1,p)=[w_0w_R/(w_Mw_P)].             (3.1)

For the middle identity, use
det(p_1,s_M)=det(p,s_0) and
det(p_1,s_R)=det(p,s_P). For the other four, the relevant
unipotent meridian fixes its cusp vector with eigenvalue one.
These are determinant identities, including their signs.

The five-term sum (2.3) consequently equals

    T(a,p,s_0,s_M)-T(b,p,s_M,s_R)
      -T(a,p,s_P,s_R)+T(c,p,s_0,s_P)
      +T(s_M,s_R,p_1,p).                           (3.2)

It equals the four-tetrahedron shadow expression

    Gamma=-T(p,a,c,s_0)+T(p,a,c,s_P)
               +T(p,a,b,s_M)-T(p,a,b,s_R).         (3.3)

Here is a finite certificate, rather than an appeal to a
shadow-volume theorem. Apply a to the whole tetrahedra
containing c,s_0,s_P; this replaces them by b,s_M,s_R and
changes their auxiliary p to p_1. Cross-ratios are invariant.
After those replacements, the difference of (3.2) and (3.3) is

    J=T(a,p,s_0,s_M)+T(a,p,p_1,s_M)
           -T(a,p,s_P,s_R)-T(a,p,p_1,s_R),          (3.4)

modulo the following explicit five-vertex boundaries:

    -partial(b,p,p_1,s_M,s_R)
      +partial(a,b,p,p_1,s_M)
      -partial(a,b,p,p_1,s_R).                     (3.5)

Expansion of the alternating boundaries verifies (3.5) as a
formal oriented-chain identity. Finally J=0. To see this,
send a to infinity. Its meridian acts as z->z+t, t!=0.
For z=r(a,p,s,a s), one has

    r(a,p,a p,a s)=z/(z-1).

The two symbols cancel by [z/(z-1)]=-[z]. Apply this to
s=s_0 and s=s_P in (3.4). This proves (3.3) in the rational
pre-Bloch group, without a regulator limit.

For a negative crossing, use the same block read backwards
with reversed orientation. The actual inverse formula agrees:
substituting (A,B,C)->(B/C,AC,1/C) in beta_+ gives -beta_-.
Thus the certificate applies to both actual crossings.

## 4. The four tetrahedra form the diagram crossing block

The local vertex order is (p,over,under,region), with four
tetrahedra and coefficients

| Tetrahedron | Developed vertices | Orientation |
| --- | --- | --- |
| 0 | (p,a,c,s_0) | -1 |
| 1 | (p,a,c,s_P) | +1 |
| 2 | (p,a,b,s_M) | +1 |
| 3 | (p,a,b,s_R) | -1 |

Faces are numbered by the omitted local vertex. The internal
face pairings are

    (0,0)<->(2,0), (1,0)<->(3,0),
    (0,3)<->(1,3), (2,3)<->(3,3),                  (4.1)

with identity vertex maps on their faces. The first two have
developing transport a, because (a,c,s_0)->(a,b,s_M)
and (a,c,s_P)->(a,b,s_R). The other two have transport one.

The underlying block is a ball. Its tetrahedra attach in the
order 0,1,2,3 along 0,1,1,2 previous faces; the last two faces
are adjacent. Its six vertices are

    over, under, P_01, P_23, S_02, S_13.

There are eight exterior triangles and twelve exterior edges,
the octahedral graph. Its sole internal edge joins over to
under and has valence four. To see the developed octahedron,
transport tetrahedra 2,3 by a^(-1). Its vertices are then

    a,c,p,a^(-1)p,s_0,s_P.                         (4.2)

Thus the occurrence of different b/c and region flags is
ordinary face transport in this same crossing ball.

For an explicit orientation check, use over=(0,0,1),
under=(0,0,-1), P_01=(1,0,0), P_23=(-1,0,0),
S_02=(0,1,0), S_13=(0,-1,0). The determinants in the
four displayed vertex orders are -2,2,2,-2. These are exactly
the signs in the table. The over-strand runs north to south
and the under-strand west to east, giving a positive crossing
in the oriented projection chart. Reverse the block for a
negative crossing.

Its four strand-end slots consist of two triangles each:

| Positive-crossing end | Left region face | Right region face |
| --- | --- | --- |
| over input | (0,2) | (2,2) |
| over output | (1,2) | (3,2) |
| under input b | (2,1) | (3,1) |
| under output c | (0,1) | (1,1) |

Join each output to the next input along the diagram strand,
preserving p, the arc vertex, the region vertex, and left/right
side. For a negative crossing interchange the inputs and outputs
and reverse all four orientations. This specifies every face
pairing, including braid closure, without a knot-by-knot choice.

### Why this is the complement, with degree one

Here is the cellular reconstruction. Cut the projection sphere
into crossing disks and the intervening arc/region strips. Use
one pole in each of the two complementary projection balls.
The dual decomposition relative to the over- and underpass bands
has one crossing ball with an over-to-under diagonal and four
alternating pole/region corners. Subdivide it about that diagonal:
its four pieces and their internal faces are exactly (4.1).
At an arc strip the two exposed triangles on each side are
identified to those on the next crossing, preserving the three
vertex types. These are exactly the slots in the table.
The remaining pieces are the two pole stars and the regular
neighborhood of the knot. Consequently truncating the knot
vertex gives the exterior; the two pole stars are balls.
Taking the barycentric subdivision before this dual subdivision
gives a common subdivision with the original projection-ball
decomposition. Thus these identifications do not attach an
additional handle or a covering of a crossing neighborhood.

There is also a direct peripheral degree check. Truncate the
over and under vertices of the four oriented tetrahedra. With
outward boundary orientation their link triangles are

    over: - (p,c,s_0)+(p,c,s_P)
                         +(p,b,s_M)-(p,b,s_R),
    under: (p,a,s_0)-(p,a,s_P)
                         -(p,a,s_M)+(p,a,s_R).     (4.3)

At the over vertex, transport the first two triangles by a.
The two copies of p differ by p->a p, a *single* meridian
translation. At an underpass the chart changes by a^(-1),
the actual Wirtinger transport c=a^(-1)ba. Along each oriented
strand the left and right region edges in (4.3) join to the
next end in the slot table. Following all ends around a knot
therefore gives one meridional circle times one traversal of
the knot. Its longitudinal transition is the blackboard
longitude. Replacing that by the preferred longitude subtracts
the writhe times the meridian, a determinant-one shear of the
peripheral basis. Hence the cusp cycle has degree one, not an
unspecified multiple of the peripheral torus.

For a hyperbolic knot exterior H_3(M)=H_2(M)=0, so the boundary
map H_3(M,partial M)->H_2(partial M) is an isomorphism. The
degree-one check, with the orientation already fixed, identifies
this chain with [M,partial M].

## 5. Face cancellation also checks the flat bundle and marking

The boundary of (3.3), after the a-transport on the faces
without p, is

    B(s_0,c)-B(s_M,b)-B(s_0,a)+B(s_P,a),
    B(s,g)=(p,g,s)-(p,g,g s).                      (5.1)

The face calculation uses no volume formula. Each B is the two
region-side faces at one strand end. The slot table makes them
cancel with the neighboring end, so the global cycle is closed
in the ideal configuration complex. Local monodromy about the
over-arc is a, and underpass transport is c=a^(-1)ba; thus the
developed flat bundle is the specified representation rho.

The two extra vertex orbits are free vertices, while the knot
vertex has the peripheral stabilizer. One can formalize the
comparison in the augmented configuration complex on

    Gamma/P disjoint-union Gamma.p disjoint-union Gamma.s.

It is acyclic by coning a finite cycle from a fresh vertex.
In positive chain degrees its Gamma-action is free, using
peripheral malnormality. Its degree-three coinvariant homology
therefore realizes the relative group homology of (Gamma,P);
the two extra trivial stabilizers add no H_2 term. The cusp
link in (4.3) is exactly its connecting map to H_2(P).
This also explains why the extra projection poles do not
change the relative fundamental class.

Map a developed tetrahedron to its cross-ratio symbol. The
five-point boundary is the five-term relation, so the map
depends only on this relative fundamental class. Two developed
presentations of that same class have equal rational pre-Bloch
images. Apply it to the diagram cycle and to the positive
geometric triangulation T. Equations (3.2)--(3.5) then prove
(1.3)--(1.4). Signed or degenerate tetrahedra in the diagram
cause no problem; T supplies the positive representative.

## 6. The generic peripheral correction is retained

The cancellation of J in (3.4) used unipotence. Its generic
form is explicit, so this argument does not erase meridian
information before the complete specialization.

Keep M generic. In the actual Gauss chart the region expression
for beta_+ is

    [M w_M/w_R]+[w_0w_R/(w_Mw_P)]+[M w_M/w_0]
                         -[M w_0/w_P]-[M w_R/w_P]. (6.1)

For its four outer tetrahedra choose the M-eigenflag of the
over-meridian and the M^(-1)-eigenflags of the under-meridians.
The two eigenflag choices are intentionally distinguished.
Determinant preservation gives exactly the factors in (6.1).
The same three five-term boundaries leave

    J=F_(M^2)(z_0)-F_(M^2)(z_P),
    F_kappa(z)=[z]+[z/(z-kappa)],
    z_0=M w_M/w_0, z_P=M w_R/w_P.                  (6.2)

To verify it, put the over-eigenflag at infinity. Its projective
action is z->kappa*z+t, kappa=M^2. If
z=r(a,p,s,a s), direct subtraction gives

    r(a,p,a p,a s)=z/(z-kappa).

For kappa=1 the two oriented symbols cancel. Away from it they
give an explicit correction to the class, and the two eigenflags
need not agree on neighboring strand roles. The cut's selected
flag in the previous note was the M^(-1)-flag; that distinction
must be transported in a family-level comparison. Equation
(1.3) is a complete-color statement, not a generic-meridian
identity obtained by silently identifying the two flags.

The quantum factor d_N(M), its wall/central-defect ratio, and
all meridian germs remain exactly as in the preceding notes.
Vanishing of the classical correction at M=1 is not permission
to discard its meridian jets or a quantum specialization factor.

## 7. Scope, coverage, and checks

The classical shadow-volume construction has existing coverage
in [Inoue--Kabaya](https://arxiv.org/abs/1012.2923), and diagrammatic
potential/volume comparisons in
[Cho](https://doi.org/10.1017/S144678871600001X). These were checked
for coverage after deriving the certificate and face table.
Their proofs are not premises here. The contribution to this
project is an explicit comparison in the actual ADO source and
meridian conventions, not a novelty claim for shadow volumes.

The [audit](../experiments/audit_crossing_fundamental_cycle.py) and
[results](../experiments/crossing_fundamental_cycle_results.json)
check the three five-term boundaries as a formal chain identity,
the five determinant identities and parabolic cancellation,
the generic affine correction, the octahedral shelling and
orientation, and the global face pairing. With --regina it
checks eleven diagrams, including both stabilizations, a
cancelling pair, multiple components, and mixed signs. Every
constructed triangulation is exactly isomorphic to the
independently constructed, *unsimplified* Regina link complement.
This is stronger validation than a match of homology or volume;
the general identification is the cellular argument above.
A complex calibration compares both local crossing orientations
and the global two-tetrahedron regulator in three frames.

The complete classical Bloch--Wigner comparison is now supplied.
Integral flattenings, the full complex period, source-preserving
quantum transport, survival of the geometric branch after
elimination, and its contribution to the actual selected quantum
period remain separate. In particular, (1.3) does not imply

    (2pi/N)log|<K>_N| -> Vol(M).

That original conjecture remains the active target.
