# A combinatorial geometric certificate for actual plats at every fixed width

The subsequent [planar decoration theorem](actual_balanced_terminal_fan_volume.md) constructs balanced diagrams from every simple triangulated sphere with a chosen dual matching. It includes the full general Morse source and independently long fillings. The theorem below retains its own original scope.

31 October 2026. Combinatorial sufficient class and arbitrary-width construction. The main class
is ALL actual flat plats with a simple white triangulated sphere. The
explicit words below prove nonvacuity at every supplied width; they do
not replace the general long-twist target by one family.

## 1. The existing simple-sphere construction applies to the actual source

Start with an original ordered 2k-strand flat plat, k>=2, whose boxes
cover all crossings, retaining the original cups, caps, marked top cap,
cyclic port order and crossing-disk matching. Build its actual plane
cubic matching graph and dual white triangular cellulation by the
literal construction in [the actual matching geometry](general_augmented_plat_matching_geometry.md),
sections1–2, or equivalently by the original middle-gap sweep.

Require that this white cellulation is a SIMPLE triangulated sphere:
its vertices and edge occurrences are the actual regions and incidences,
there are no loops or parallel edges, and every triangular cell has
three distinct vertices. This is a finite combinatorial test on the
supplied diagram, not an abstract graph chosen to imitate it. The
nondegenerate sphere has at least four white vertices. Each source
triangle still has exactly one designated matching edge.

The already proved construction in [the simple-block construction](actual_smoothed_source_capacity_blocks.md),
sections4–5, applies with this WHOLE sphere as its single simple block.
Its fixed-boundary Hall argument gives an interior angle maximizer;
Euclidean disk development is an embedding of degree1; the strict sector
argument excludes unintended contacts. The contact circles of the
shaded triangles then give all supporting halfspaces. Therefore it
constructs a convex three-dimensional ideal right-angled polyhedron
with exactly these LABELED white faces, shaded triangles, ideal contacts
and cyclic orders. Separating triangles are allowed by that proof.

Sections3–6 of [the actual matching geometry](general_augmented_plat_matching_geometry.md) identify
this labeled medial sphere with the TWO actual projection/crossing-disk
cut balls. They glue white faces across the copies and shaded triangles
by the original retained half-twist permutations. The original meridians,
primitive crossing-disk longitudes and source mark are retained. Their
right-angle edge cycles and cusp decorations prove completeness for
every fixed half-twist pattern. In particular the ACTUAL augmented
exterior Y_(D,epsilon) is hyperbolic, with volume2Vol(Q). Its positive
ideal triangulation supplies the general marked gluing certificate.

Thus the simple-white test is a SUFFICIENT combinatorial geometric
certificate for the exact class used by the right-angled source results.
It is not a claim that every hyperbolic or prime twist-reduced plat
satisfies this test. The older matching-geometry existence-gap paragraph
can now be sharpened for this class using the later simple-block proof.
No external alternating-link existence theorem is being imported.

## 2. Explicit literal words at all widths k>=3

Number adjacent strand slots from0 to2k-2. Put

    O_k=(1,3,...,2k-3), E_k=(0,2,...,2k-2),
    w_k=O_k E_k O_k, R=3k-2.                            (1)

These are the original bottom-to-top box slots; no isotopy or abstract
matching-to-plat adapter is needed. Denote the exterior by u, the k
bottom odd-gap regions by a_0,...,a_(k-1), the k top odd-gap regions
by b_0,...,b_(k-1), and the intermediate bounded even-gap regions by
e_1,...,e_(k-1). Set e_0=e_k=u for formulas only. All the other named
vertices are distinct.

The literal gap sweep gives exactly these ordered four-face incidences:

    first O:  (a_(j-1),u,e_j,a_j),       1<=j<=k-1;
    middle E: (e_j,a_j,b_j,e_(j+1)),      0<=j<=k-1;
    final O:  (b_(j-1),e_j,u,b_j),        1<=j<=k-1.      (2)

The two cells of a quartet (x,b,c,y) are (x,b,y) and (x,y,c).
The MAIN edges of its white sphere are exactly

    u-a_i, u-b_i                         (0<=i<=k-1),
    e_j-a_(j-1), e_j-a_j,
    e_j-b_(j-1), e_j-b_j                 (1<=j<=k-1),

and its MATCHING edges are exactly

    a_(j-1)-a_j, b_(j-1)-b_j             (1<=j<=k-1),
    u-e_1-e_2-...-e_(k-1)-u             (the k cycle edges). (3)

For k>=3 every listed edge has distinct endpoints and occurs only once
in (3) and the MAIN list. In particular the matching cycle has length
at least3. The triangles in (2) are distinct and every listed edge
occurs in precisely two of them. These are the actual embedded sphere
cells from the gap sweep, with

    vertices=3k, edges=9k-6, triangles=6k-4,
    vertices-edges+triangles=2.

For example the MAIN edge e_j-a_(j-1) appears in the first-O output
triangle and the preceding middle-E input triangle; the other three
e_j MAIN incidences pair in the same way. The end u-a_0,u-a_(k-1)
incidences close against the first and last middle-E cells, and the
interior u-a_i incidences pair between consecutive first-O cells;
the b incidences are reflected. The matching edges each pair the two
triangles of their own original box. This checks the full labeled
sphere, not just its Euler count. The protected mark can be the original
first top cap: its two adjacent white faces are u,b_0, joined by MAIN.
Consequently every w_k, k>=3, meets the simple-white certificate.

## 3. Width two and the knot parity

For k=2 take the original slot word (1,0,1), with R=3. Its actual
quartets are

    (1,0,3,2), (0,1,4,3), (4,3,0,2).

The six triangles form the triangular bipyramid on vertices0,...,4,
with equatorial triangle(0,2,3) and apices1,4. Thus its white sphere
is simple and nondegenerate. The superficially similar word
(1,0,2,1) must NOT be used for this argument: its two middle boxes
produce parallel matching edges between the same white pair.

For k>=3 put epsilon=+1 or -1 on EVERY box of the FIRST O layer, and
zero on the other boxes. For k=2 use one nonzero epsilon on the first
slot1 box and zero on the other two. Signs do not affect permutation.
Starting with k disjoint cap components, the successive first-layer
transpositions on slots1,3,...,2k-3 join component j to the already
joined components0,...,j-1. At that step their two strands are in
DIFFERENT components; cutting and cross-rejoining them merges those
two cycles. Induction therefore gives ONE main component. Equivalently,
the exact permutation is the product of the disjoint transpositions
(1 2)(3 4)...(2k-3 2k-2), and the lower standard pairing together with the upper pairing transported
by this permutation form a single alternating cycle.

All full twists have trivial strand permutation. Thus for each such
fixed parity pattern EVERY fixed integer vector p gives a knot with
box exponents epsilon_i-2p_i. The [geometric long-filling theorem](general_augmented_plat_long_filling_quantifiers.md) gives
a threshold T_geom(D,epsilon) for independently long signed p_i, with
no comparability requirement. Each resulting knot has a k-bridge
PRESENTATION, hence minimal bridge number at most k. This class construction alone does not prove b(K)=k. The later
[Fox certificate](actual_fox_coloring_exact_plat_bridge.md) does prove it
when every box exponent is divisible by3, independently of the quantum
asymptotic problem.

## 4. Exact coverage and threshold dependence

The main geometric assertion applies to EVERY actual simple-white
flat plat, not just (1). Its width and number/order of boxes may be
arbitrary but are fixed before the quantum limit. Each fixed retained
half-twist pattern and original primitive marking is part of D.
The geometric threshold can depend on that full D, including cusp
moduli, the positive-shape and framed-completion neighborhoods, and
the common inverse-slope IFT polydisk. It is not asserted to depend
only on k. A maximum over the finitely many cusp subsets gives one
threshold for partial fillings as well, with unfilled inverse slopes0.

The endpoint/complete-source results apply with their separately stated
source and parity scopes. The later [balance theorem](general_complete_radius_balance_filling_volume.md)
proves the full fixed long-filling limit under its additional geometric
condition. The [one-end layer family](general_one_end_layer_long_filling_volume.md)
establishes that condition for its actual words at every k>=2. This class
construction alone does not prove balance or the quantum limit for all
its diagrams. The direct fixed-root route needs no separate genuine-q
normals; the older mixed-color route has its own hypotheses. Neither
result identifies all essential hyperbolic plats with this class or
certifies an arbitrary abstract matched graph as an original source.

## 5. Focused verification

The [literal-source audit](../experiments/audit_general_simple_white_plat_class.py)
and [recorded output](../experiments/general_simple_white_plat_class_results.json)
check the original gap-sweep incidences, distinct triangle and edge
occurrences, sphere counts and one-component parity at widths 2 through
30. At width 30 the source has 88 ports and 90 white vertices. These
finite checks support the source dictionary; the symbolic formulas and
construction above prove the arbitrary-width statement. They do not prove
minimal bridge number or the phase-sensitive quantum filling limit.
