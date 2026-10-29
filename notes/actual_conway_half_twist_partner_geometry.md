# Complete half-twist partners and a general knot-connectivity construction

29 October 2026. Every fixed half-twist pattern on the leaves of a
retained robust Conway factor has an actual complete hyperbolic
augmented-link complement, with the SAME volume as its pure partner.
This follows from explicit changed face pairings of the already proved
polyhedron, including their pointwise edge words and complete cusp links.
No unmarked half-twist invariance theorem is imported.

Moreover EVERY robust expression has a constructible half-twist pattern
whose main strands form ONE component, before or after any integral
full-twist fillings. Thus the grammar has genuine arbitrarily branching
knot candidates. The required odd-source mixed-color estimates and
marked DEFORMED geometry remain separate from the complete theorem here.

## 1. The actual local cut after one half twist

Use the original closed bowtie cut and its labels

    S0=(O,C1,C2), S1=(O,C3,C0).

Superscripts + and - distinguish the two projection balls. Without a
half twist the shaded gluing stays within each ball, fixing O and
matching C1 to C0, C2 to C3. The white faces pair the two balls by
their original projection labels.

To insert a literal half twist, cut at that leaf's original twice-
punctured crossing disk and rotate one side through +pi or -pi around
its normal. In coordinates on the disk this is (y,z)->(-y,-z), with
the projection line z=0 and the two punctures at y=+a,-a. It exchanges
the punctures AND the upper and lower half disks. Consequently the
new shaded pairings are

    S0+ -> S1-: O+->O-, C1+->C3-, C2+->C0-,
    S1+ -> S0-: O+->O-, C3+->C1-, C0+->C2-.          (1)

The reverse pairings are their inverses. The white maps are unchanged.
These are maps across copies; making the same puncture swap within one
copy would give the wrong boundary orientation.

This is a literal reversible local cut of the original odd leaf
T(R^epsilon L_N), epsilon=+1 or -1. Quarter-turning its one-crossing
main tangle gives the opposite pairing (0,2),(1,3), exactly as (1).
All original turns and identity strips outside this disk remain in
place. The closed bowtie proof therefore identifies the resulting
face quotient with the actual half-twist partner exterior.

The two signs have the same boundary half-rotation and hence the same
unmarked face pairing. Their collar paths differ by a full twist,
which changes the primitive crossing-circle meridian by one disk
longitude. Complete volume does not depend on this marking, but a
future filling equation must keep the chosen sign and collar path.

## 2. Exact odd edge holonomy

Keep the complete stationary polyhedron of the pure source. At this
leaf set E=exp(2pi i x), 0<x<1/2, and normalize its ordered port to

    Q=(0,infinity,1,R),  R=(1+E)^2/(4E),
    O+=(1+E)/2, O-=(1+E)/(2E).

The four actual white/completion maps are the matrices W0,...,W3 in
[the marked pure-deformation proof](actual_conway_marked_peripheral_deformation.md),
equation (8). At the COMPLETE point the cross-half map in the first
line of (1) is

    T=[[R,-R],[1,ER-1-E]].                           (2)

It sends infinity to R, 1 to 0 and O+ to O-. The second map is
T'=bar(T)^(-1), where bar(E)=E^-1 and bar(R)=R. Direct multiplication
gives all three pointwise odd edge words:

    W0^(-1) T' W2^(-1) T = identity,
    W2^(-1) T' W0^(-1) T = identity,
    W1^(-1) T' W3^(-1) T = identity.                 (3)

The first two are the two pairs of bowtie sides incident to O; the
third is the CAP-base pair. The reverse edge words are their inverses.
Each word visits four distinct copies of an edge. Each corner still
has dihedral angle pi/2, so its total is 2pi. Equation (3) additionally
rules out translation or dilation along that edge; the angle count
alone would not suffice.

Every edge belongs to one leaf bowtie. An arbitrary mixture of even
and odd leaves therefore uses the already checked pure edge word or
one of (3), independently at that leaf. All white/white auxiliary
seams remain the original pointwise identities. This proves every
edge relation for an arbitrary fixed pattern, not just one isolated
half-twist example.

## 3. Complete cusps and unchanged actual volume

Use the complete right-angled polyhedron's canonical horosphere
decoration: at each ideal vertex scale its rectangular link so that
both opposite shaded sides have length one. They have equal length
because they are opposite sides of a rectangle. The same decoration
is placed in the other copy. Every ideal shaded triangle then has
the same length-one horocycle at each of its three corners.

Both the original shaded maps and the changed cross-half maps (1)
preserve these horocycles, including their corner permutation. White
maps preserve the copied rectangular links. Hence the new cusp links
are finite Euclidean rectangle gluings without a dilation defect.
Their corner angles sum to 2pi by the four-edge cycles. The literal
link-exterior topology makes each connected link a torus. They give
complete flat cusp tori and complete horoball ends after a uniform
shrink. All finite points are smooth by (3).

Thus the quotient of the two original polyhedra is the complete
finite-volume hyperbolic metric on the ACTUAL half-twist partner.
Its oriented volume is exactly twice the unchanged polyhedron volume:

    Vol(S^3 minus L_E^epsilon)
       =2 Vol(P_E)=2pi phi_E(0).                    (4)

Combined with the independently proved whole complete odd-source
asymptotic in [the original Newton transport theorem](actual_odd_conway_newton_transport.md),
this identifies its full-sequence exponential rate with the actual
half-twist partner volume, for every fixed ±/0 pattern.

This is a COMPLETE statement. The mixed pure-cell construction with
opposite apex flags cannot be reused unchanged in (1): the odd
cross-half equations and the correct meridian marking must be solved
for the odd source's own deformed action.

## 4. The two primitive half-twist markings

The complete crossing-circle cusp can also be computed directly.
In its original local upper-half-space coordinate,

    (C0,C1,C2,C3)=(1,E,-1,-E), O=infinity.

The lower and upper white maps to the reflected copy are

    B0(z)=-z/E+(E+1)/E,
    B2(z)=-z/E-(E+1)/E.

The two cross-half shaded maps in (1) are

    T0(z)=-z/E+(E-1)/E,
    T1(z)=-z/E-(E-1)/E.                             (5)

The disk-framed longitude still crosses the bottom white face and
returns through the top, giving

    lambda=B2^(-1)B0=-2(E+1).

The two signed meridian collar paths give translations

    mu_+=-2,       mu_-=2E,       mu_+-mu_-=lambda. (6)

For example the elementary shaded/white paths B0^(-1)T0 and
B0^(-1)T1 translate by 2 and 2E; reversing the first gives mu_+.
Which collar is called + is the geometric positive-diagonal convention.
Identifying it with the chosen quantum R or R^-1 requires retaining
that braid convention; it is not inferred from the unmarked metric.

Put c=cot(pi x)>0. Relative to the pure meridian mu_0=E-1,

    mu_+=mu_0+lambda/2,    mu_-=mu_0-lambda/2,
    tau_+=lambda/mu_+=2ic/(1+ic)=1+E,
    tau_-=lambda/mu_-=2ic/(1-ic)=-1-E^-1.             (7)

These relations compare Euclidean translation vectors; lambda/2
alone need not be a loop of either cusp lattice. Each pair
(mu_+,lambda) or (mu_-,lambda) has area 4 sin(2pi x), exactly the
total area of the two original rectangles, so each is a primitive
peripheral basis. This checks the complete marking rather than merely
the isometry type of an unmarked cusp.

## 5. Literal main connectivity

Ignore auxiliary circles only for counting the main components.
For the four ports (bottom-left,bottom-right,top-right,top-left) write

    I=(0,3)(1,2), U=(0,1)(2,3), X=(0,2)(1,3).

A pure leaf has pairing U. An odd leaf has pairing X by (1).
A turn swaps I and U and fixes X. The literal stack table is

| lower / upper | I | U | X |
|---|---|---|---|
| I | I | U | X |
| U | U | U plus one internal circle | U |
| X | X | U | I |

This is obtained just by following the original two identity wires.
The ONLY operation creating a new internal main circle is U times U.
Once an internal component exists later operations cannot remove it.
The cylindrical closure of I has two components; those of U and X
have exactly one.

At a robust seed h^3 choose either:

* all three leaves odd: its pairing is X, with no internal circle;
* exactly one leaf pure and the other two odd: its pairing is U,
  with no internal circle.

Thus the seed can realize the set C={U,X} without loops. A turn
permutes the three pairing types. To see that arbitrary branching
never destroys the needed choices, put

    A={I,U}, B={I,X}, C={U,X}, D={I,U,X}.

When the forbidden loop-creating choice U times U is excluded, the
products of the three two-element sets are

| lower / upper | A | B | C |
|---|---|---|---|
| A | A | D | C |
| B | D | B | D |
| C | C | D | A |

In particular at least two feasible pairing types survive every
product. The statement remains true if a child already offers D.
Induction proves that EVERY robust expression offers at least two
types with no internal main circles. At least one is U or X. Choose
that root type and backtrack the finite choices in the table: its
cylindrical closure has one main component.

This is a linear-time constructive parity prescription for arbitrary
fixed branching and turn depth. One may choose either sign on every
odd leaf; only parity affects connectivity. Subsequent full twists
have even endpoint permutation and preserve it. Therefore after
filling ALL auxiliary circles by any integral full-twist parameters,
the resulting diagram is a KNOT in S^3. With some auxiliary circles
retained it has one main component and those auxiliary components.

The complete augmented partner is hyperbolic by sections 1--3. The
odd mixed source estimates and the correctly marked deformed branch
are separate inputs. They are now supplied in the
[long-filled knot and link assembly](actual_odd_conway_long_filling_volume.md)
for C(FG) with robust children. That mixed-color filling theorem
continues to exclude C(A), although the complete theorem here covers it.

Audit: [exact odd edge words, cusp paths and constructive knot patterns](../experiments/audit_actual_conway_half_twist_partner_geometry.py)
and [results](../experiments/actual_conway_half_twist_partner_geometry_results.json).
PASS for all three generic odd edge words, both primitive diagonal
markings and their two-rectangle areas, all nine products of pairing
sets, 69 literal expression witnesses and 483 signed full-twist checks.

Independent internal review: the local-cell/source agent read the full
actual half-disk cut, all three pointwise edge words, the complete
rectangle decoration and primitive collar markings, and reported PASS.
Its independent fresh audit replay also passed.

Primary-agent review and fresh symbolic/topological audit: PASS. The closed half-disk cut, cross-copy orientation, complete cusp decoration, primitive marking areas, matching-set induction and preservation under full twists were checked. Complete geometry alone is not used to claim a filled quantum theorem.
