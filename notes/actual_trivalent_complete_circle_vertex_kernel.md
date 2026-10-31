# Trivalent complete-circle vertices and the ordered pivotal sewing test

29 October 2026. The literal trivalent complete-circle vertex has an
explicit channel kernel with at most N coherent terms per entry.
It gives a source-exact partition for an ORDERED Morse circuit, including
genuinely four-vertex circuits and arbitrary fixed-width nested cup
insertions. Every physical pair degree, complete-circle normal weight,
signed twist and original marked cap is retained. An abstract graph's
plain incidence contraction is a different object unless its ordered
pivotal sewing has been certified; an exact cube diagnostic below
detects that error. No new volume equality is claimed.

The three vertex packets are different: black cup, ordinary white cap,
and the sole marked white cap. In particular this reduction does not
turn the original graph into the norm square of one vertex packet.
It gives the concrete finite kernel to which a coherent branching
estimate would have to apply.

## 1. Actual pair factor, on every physical degree

Put N>=2, d=N-1, q=exp(pi i/N), Q=q^2, x=q^d and
kappa=q^(d^2/2). Let R be the original full-Cartan checked crossing,
L=L_N its literal complete ordinary crossing circle, and P the
physical pair exchange, not an added crossing. Use the full physical
CD factor from [complete-circle positivity](actual_complete_circle_reflection_positive.md).
Its columns are indexed by alpha=(T,j), with

    0<=T<=2d, l=min(T,2d-T),
    0<=j<=d-j<=l.

Let v_alpha(a) be the canonical eigenvector in the original degree-T
block, normalized to one at its smallest physical first color. Extend
it by zero outside max(0,T-d)<=a<=min(d,T). The actual CD coefficient is

    h_alpha=2 s_l^2/[s_(l-j) s_(l+j-d)], j<d-j,
    h_alpha=s_l^2/s_(l-j)^2,             j=d-j,
    s_r=product_(t=1)^r |1-Q^t|.

The possible second line is the genuine odd-level Steinberg channel.
The v_alpha are the finite Jacobi continuants of the actual Casimir;
the high-degree block uses its specified physical translation. Define

    f_alpha(a)=sqrt(h_alpha) v_alpha(a),
    F_(a,b;alpha)=delta_(a+b,T) f_alpha(a),
    omega_alpha=kappa (-1)^j q^[j(j+1)].                 (1)

Every h_alpha is positive, and |omega_alpha|=1. The full physical,
all-input identities are

    F F^dagger=L P,
    R F=F diag(omega_alpha),
    R^e L=F diag(omega_alpha^e) F^dagger P, e in Z.      (2)

Thus the complete circle has acted with its actual FIRST normal at
each double Casimir node before its CD image is used. Equation (2)
does not semisimplify an incoming root state or a generic-q germ.
All zero-length and odd simple channels remain as in the physical map.

## 2. One physical trivalent junction

Number the six boundary ends cyclically, with consecutive pair ports
(12),(34),(56). Inside the disk join them by the PLANAR arcs

    S={(1,6),(2,3),(4,5)}.

The original cup tensor is J=p_16 p_23 p_45, where
p_(a,b)=N x^(-b) delta_(a+b,d). Its support and coefficient are

    (a,b,d-b,c,d-c,d-a),
    J=N^3 x^[a+b+c-3d].                                (3)

Let P_S swap both ends of all three arcs of S, and let P_S' swap
only (23),(45), leaving the designated marked arc (16) unchanged.
Let P_ports=P12 P34 P56. Define the THREE open channel tensors

    U=(F^dagger)^tensor3 P_ports J,
    V=(F^dagger)^tensor3 P_S J,
    V_m=(F^dagger)^tensor3 P_S' J.                       (4)

The first is the black cup packet. The second is the ordinary white
cap packet. The third is the marked white cap packet, after the
WHOLE graph has forced that marked arc's integer degree d. No local
unrestricted marked row is replaced on an arbitrary exterior.

Here are closed entries of (4), with no inverse Clebsch frame. For
alpha_i=(T_i,j_i), all three packets vanish unless

    T_1+T_2+T_3=3d.                                    (5)

When (5) holds, put

    b=T_1-a, c=T_1+T_2-d-a,
    I=[max(0,T_1-d,T_1+T_2-2d),
                         min(d,T_1,T_1+T_2-d)] intersect Z.

Then exactly

    U_(alpha1,alpha2,alpha3)
      =N^3 sum_(a in I) x^[a+b+c-3d]
          conjugate(f_alpha1(b) f_alpha2(c) f_alpha3(d-a)),

    V_(alpha1,alpha2,alpha3)
      =N^3 sum_(a in I) x^[-a-b-c]
          conjugate(f_alpha1(a) f_alpha2(d-b) f_alpha3(d-c)),

    Vm_(alpha1,alpha2,alpha3)
      =N^3 sum_(a in I) x^[-d+a-b-c]
          conjugate(f_alpha1(a) f_alpha2(d-b) f_alpha3(d-c)). (6)

Each entry has at most N terms. Equations (3) and a literal port
exchange prove all of (4)--(6). They retain the coherent relative
phase between every physical color before any positive norm.

For the known final-source middle-degree extraction T_i=d, the
underlying marked physical polynomial is particularly simple:

    F_J(z1,z2,z3)=N^3 x^(-d) sum_(a=0)^d x^(-a)
                      f_a(z1) f_a(z2) f_a#(z3),         (7)

where f_a now denotes the middle-degree continuant normalized by
f_0=1, not the sqrt(h)-normalized column in (1). This is precisely
the [marked multiport transform](actual_marked_multiport_chebyshev_source_packet.md)
of P_mid J. Its original marked corner gives

    x^d N^(-4) F_J(c0,c0,c0)=1,
    c0=q+q^-1.                                         (8)

Indeed f_a(c0)=x^a, so every term in (7)'s corner is one.
Formula (7) may be folded for that FINAL complete-circle observation.
It is not permission to discard the full-degree kernels (6) at an
internal graph seam.

## 3. The finite tensor partition and its necessary source qualification

Let G be any fixed trivalent bipartite port graph, with b black and
b white vertices, hence 3b edges. Its TYPED physical tensor circuit is
specified as follows. At each black vertex use the three
original cups (3), at each white vertex use the three ordinary caps
on the same cyclic matching, and along edge e put the actual box

    B_e=R^(e_e) L_N, e_e any fixed signed integer.

Use one original unrestricted marked cap in place of the arc (16)
at one white vertex w_*. A different arc is the corresponding cyclic
relabelling of (6). If an orientation changes, transport BOTH the
object and its turns by the specified genuine dual isometry; retain
its unitary pivot clocks. For this statement the pair-port ordering
and cup/cap orientations are those just displayed, so no such clock
is suppressed. All framing/peripheral normalization remains in the
original external line chi_N. Equation (10) is an identity for this
fully specified tensor circuit. When drawing it as a planar ribbon
tangle, the actual ordered edge charts and turns are part of that
specification. An abstract untyped graph alone does not authorize
replacing a necessary structural crossing by a plain tensor flip,
or identify its complement with a fully augmented hyperbolic link.

The incoming black cups have total integer degree 3bd. All boxes
preserve this degree. The 3b-1 ordinary cap arcs force their own
degrees d, so the SOLE marked arc has degree d. Only after this
whole-source argument its restricted row may be used. The exact
physical row identities are

    ell^S=N^(-6) J^dagger P_S,
    (ell ell m_d)^S=N^(-7) J^dagger P_S'.               (9)

Insert (2) ONCE on every graph edge. Contract its endpoint F factors
using (4). With the fixed cyclic order at each vertex, the resulting
whole original raw scalar is

    Z_G,N=N^(-6b-1) sum_(alpha:E(G)->CD labels)
       [product_(v black) U_(alpha around v)]
       [product_(w white,w!=w*) conjugate(V_(alpha around w))]
       conjugate(Vm_(alpha around w*))
       product_(e edge) omega_(alpha_e)^(e_e).           (10)

Equation (10) is an exact VECT tensor identity at both level parities
and composite N, with all ports open until the specified contraction.
IF its incidence ordering is the actual ordered Morse sewing described
in Section5, it is the original raw scalar and its normalized invariant
is chi_N Z_G,N. There is no additional normalization for a complete
auxiliary circle. No source identification is asserted just from a
planar rotation system. Nothing assumes that L_N is a projector or
that L_N^2 is nonzero.

Most importantly the incidence constraints in this partition are
the TRUE integer equations

    sum_(e incident to v) T_e=3d at EVERY vertex.        (11)

They follow from actual cup support, not a Q-clock residue. The same
edge label appears at its two endpoints. Hence (10) is a coherent
graph packet with coupled charge equations, rather than a product of
independently maximized circle capacities. The four-vertex example
and the correctly ordered cube in Section5 have independent original
Morse-source certificates. The cube's NAIVE cyclic charts do not pass
the same test; they must not be confused with its corrected source.

The positive edge weights and their affine-angle profile can be kept
visibly separate from each vertex. Divide U,V,Vm by
sqrt(h_alpha1 h_alpha2 h_alpha3), and call the resulting UNscaled
continuant kernels u,v,vm. The same equation (10) then has u,v,vm
at its vertices and the edge factor

    h_alpha omega_alpha^(e_e).                          (11a)

There is exactly ONE h_alpha per actual edge, since its two square
roots meet at the two endpoints. With

    A=l-j, B=l+j-d, C=d-l,
    A,B,C>=0, A+B+2C=d,

the reflection identity s_r s_(d-r)=N gives

    h_alpha=2 N^2/(s_A s_B s_C^2)                       (11b)

at a paired node, and half this prefactor at the odd simple node.
Thus the actual positive angle factor and every coherent vertex
sum are known explicitly. The graph constraint is still (11), with
T_e=l_e or 2d-l_e; no additional geometric edge equation has been
inferred from (11b). Dephasing the one-color sums in (6) is not part
of the identity.

## 4. Why this exact reduction is not yet a positive-volume theorem

The boundary packets in (4) cannot be identified by a local planar
reflection and unitary gauges. Already at the literal two-vertex,
three-edge graph, the independently exact N=3 original source gives

    Gram(U,Vm)=3^10 [[18,10],[10,119]].                 (12)

In particular ||U-Vm||^2=117*3^10>0 in the actual positive-circle
image. This is the full original-cup certificate in
[the coherent reflection audit](actual_pretzel_circle_coherent_reflection.md#3a-the-untwisted-source-mismatch-survives-the-positive-circle-quotient),
not an arbitrary choice of eigenvector phases. Simultaneous changes
of CD factor preserve (12). Thus a pointwise positive replacement of
(10) by the norm of one unspecified vertex would change the source.

There is a direct wiring reason before the quotient: the port reversal
P_ports takes the noncrossing matching S to

    {(2,5),(1,4),(3,6)},

which is crossing in the six-ended disk. P_S instead preserves S.
A cyclic or reflected relabelling of a disk preserves whether a
matching is crossing. Hence these two local wirings are not equal
as planar tangles. This does not rule out a larger coherent reflected
construction with actual extra crossings and their full kernels.

Nor can the ordinary white cap be silently used to avoid the marked
distinction. Closing any honest all-ordinary original complete-color
ribbon tangle is zero:
cut one complete-color component to obtain an actual Hopf endomorphism
of the simple original V_N, hence a scalar, and its ordinary pivotal
closure has sum_a K_a^(1-N)=0. This proof is at the fixed root; all
internal E/F arrows are nonzero. The original invariant instead uses
the sole modified marked cap in (9). Positivity of a closed ordinary
trace therefore cannot supply its missing normal source. This is a
necessary typing test, not a sufficient source certificate. The next
section uses it to reject an otherwise tempting graph contraction.

## 5. Actual ordered Morse sewing, and an exact failed cube shortcut

A reusable sufficient rule is to KEEP A HORIZONTAL MORSE CUT and its
ordered list of physical strands. At a black vertex insert J into a
specified GAP of that list; this is an actual planar six-head cup
insertion. At a white vertex remove six CONSECUTIVE strands using the
specified cap tensor. Each edge box acts on its two consecutive physical
strands while they run from its black to its white vertex. Bare wires
preserve their actual order. A necessary permutation is performed by
its genuine braid, not by relabelling the tensor indices for free.
This recipe gives a finite original cup/box/cap word, and induction on
its Morse events proves its source preservation. It allows arbitrarily
many fixed nested trivalent insertions and does not assume a small
bridge width or a value-only root source.

For a first genuinely four-vertex example, the black vertex orders and
white vertex orders of its six pair-edges are respectively

    black: (0,1,2), (3,4,5),
    white: (0,1,3), (4,5,2).                            (13)

Start with the first six-head J. Insert the second J in the gap after
its first four strands. On the resulting twelve-head cut the exact
bottom cup matching is

    (1,12),(2,3),(4,11),(5,10),(6,7),(8,9).              (14)

It is NONCROSSING and is obtained by that actual nested insertion.
The six two-head boxes occupy the consecutive pair-slots in the order
(0,1,3,4,5,2). Close the first six and last six strands by the two
white caps in (13), keeping the sole unrestricted mark at the first
white arc(1,6). This is a literal original twelve-head Morse diagram.
Its physical cap/box/cup contraction is therefore EXACTLY (10) for
(13). All ordinary closures vanish, as required. In the cyclotomic
image q^6=1, q of order6, p=1009, the genuinely marked untwisted
N=3 scalar is 242. This finite-field nonzero image proves that the
corresponding exact complex source is not zero; it is not a numerical
asymptotic. No topology or volume of its complement is inferred.

By contrast take the planar cube with vertices 0,...,7 and edges

    01,12,23,30,45,56,67,74,04,15,26,37.

Use the usual nested-square drawing, black vertices{0,2,5,7}, put
the SAME counterclockwise cup/cap chart at every vertex, and connect
like-numbered pair legs by a bare incidence delta. With every edge L_N,
the ALL-ORDINARY contraction has the exact N=3 cyclotomic image

    174 (mod1009), q of order6.                         (15)

Here no sqrt(h) or absolute value enters the test: it uses only the
literal polynomial L_N, original p, ordinary ell and finite contractions
in Z[q,1/3]. Reduction modulo a prime not dividing3 is a ring map, so
(15) proves exact complex NONZERO. It contradicts the required ordinary
qdim-zero test for an honest original closed link. Consequently these
naive cube charts are not that ribbon link's source, despite planarity
of the untyped cube and correctness of every isolated box.

### A source certificate that corrects the cube and gives an unbounded class

Here is an algebraic criterion which supplies the actual Morse orders,
rather than guessing local cyclic charts. Take two partitions B,W of
the ordered set{0,...,3b-1} into triples. Each partition must be
NONCROSSING: no two of its blocks contain a<c and b<d respectively
with a<b<c<d. For each sorted triple(a,b,c) use the actual matching

    (2a+1,2c+2),(2a+2,2b+1),(2b+2,2c+1)               (15a)

on the 6b physical heads. Use B for the bottom cups, W for the top
caps, and put box e on consecutive pair(2e+1,2e+2). Mark exactly one
of the top arcs, retaining its unrestricted original row.

Every matching in (15a) is noncrossing. For two different triple blocks,
their intervals are either disjoint or a block is contained wholly in
a gap of the other; otherwise their four alternating endpoints violate
the stated partition condition. The three arcs of an individual triple
are noncrossing, and a block contained in a gap is nested in one of
these arcs. This proves the assertion by induction. Conversely the
actual cup insertion order can be read without any topology theorem:
remove an innermost adjacent matched pair repeatedly and then reverse
these removals. Each reverse step is the original p inserted in the
specified gap. Top caps are the corresponding removals. Thus (15a)
is a finite literal original Morse diagram, not a vector-space
permutation pretending to be a braid. Its root source also has a
regular generic Hopf lift: use the actual regular generic cups and
the corresponding polynomial in the generic pair Casimir for each
root circle. This proves saturated-source inclusion at the ROOT.
It does not identify that chosen lift with the entire actual ADO
q-normal germ or permit differentiating a value-only CD replacement.

Its graph has one black vertex for each B triple, one white vertex
for each W triple, and one edge for each number e. Its source is
EXACTLY (10) in those sorted triple orders. The partition condition
is independent of N, allows arbitrary b, and is checked by finitely
many alternating-endpoint tests. Multiple edges or disconnected
components are allowed; connectedness can be required separately.
No claim that all planar graphs admit this particular certificate
is needed. This is an actual branching source class, not a geometric
or survival hypothesis about an unknown invariant.

Pointing qualification: to identify its bare m insertion with the
original exposed one-cut invariant, choose the marked outer cap at
a top-level white block, not inside another top cap. Equation(10)
is still a tensor identity for a bare m at an inner block, but that
different insertion is not automatically a transported pivotal cut.
The [first-normal source theorem, section4a](actual_nc_morse_graph_first_normal_source_reduction.md)
records an exact cube counterexample and the corrected exposure
condition. No local invariant property of the unrestricted m permits
moving it through enclosing caps without their pivotal transport.

In particular the following certificate has the CUBE as its connected
simple incidence graph:

    B=(0,1,2),(3,4,11),(5,9,10),(6,7,8),
    W=(0,10,11),(1,8,9),(2,3,7),(4,5,6).                (15b)

The incidence matrix, in the displayed vertex orders, is

    1 1 1 0
    1 0 1 1
    1 1 0 1
    0 1 1 1.

Thus it is K_(4,4) with a perfect matching removed, the usual cube.
The source is a literal TWENTY-FOUR-head cap/box/cup diagram. Each
cap has the opposite boundary orientation to a cup: its ribbon
rotation is the REVERSE of its displayed left-to-right Morse order.
Writing each half-edge as(vertex,edge), the six ribbon face cycles are

    (0,0) (4,11) (1,3) (6,2),
    (0,1) (5,9)  (2,10)(4,0),
    (0,2) (6,7)  (3,8) (5,1),
    (1,4) (7,6)  (3,7) (6,3),
    (1,11)(4,10) (2,5) (7,4),
    (2,9) (5,8)  (3,6) (7,5).

There are six quadrilateral faces and 8-12+6=2. This verifies the
planar ribbon embedding and the cup-versus-cap rotation directly;
it does not assign a hyperbolic decomposition to the link complement.
Keeping the SAME cyclic orientation at both kinds of vertex would
instead give four hexagonal faces and Euler characteristic0.

An independent primitive-pair audit expands all bottom arcs as actual
N U cups, all top arcs as actual U^(-1)/N caps, the sole marked arc as
its UNRESTRICTED m, and every edge as the original full four-index
R^e L_N. It does not use a six-head vertex or fitted eigenvector frame.
It agrees with (10) for nine signed 24-head families, and its ordinary
closures vanish. At N=3 the corrected untwisted marked cube has image
730 mod1009, with ordinary image ZERO. At N=4 its marked image is228
mod1009, so this genuine branching source is not forced to vanish at
every even level. These are exact finite source checks, not a proof
of a limiting nonzero saddle or a claim of hyperbolicity.

For a nonprogressive planar embedding, the correction is to put back
the ACTUAL bends at its Morse events. In the original physical basis

    U_(a,b)=x^(-b) delta_(a+b,d),
    cup=N U, cap=U^(-1)/N.

Their left/right discrepancies are the retained original pivots
U^(-1)U^T=g, U^T U^(-1)=g^(-1), not an arbitrary scalar. For example
the bend of one leg of a full four-port matrix B is exactly

    (D_2 B)_(ab;cd)
      =sum_(u,v) U_(b,u) B_(a,v;c,u) (U^(-1))_(v,d)
      =(I tensor U) B^(transpose_2) (I tensor U^(-1)).  (16)

Both factors N cancel in (16). Repeating these physical bends and
keeping every required pivot gives the correct ordered matrix; a
needed structural crossing still uses its full R. This is the
reusable correction rule, not an assertion that the untyped cube is
corrected by one chosen global gauge. In particular (16) is a partial
transpose, not a positive Hilbert congruence. A positive CD factor on
one bipartition must NOT be carried through it by simply changing
the names of its node indices. The actual H at N=2 has a one-leg
bend with spectrum(4,4,4,-4), as independently proved in
[the original reflection audit](actual_reflection_marked_boundary_metric.md#3-reflection-of-original-crossings-and-a-genuine-bend-caveat).

Thus the exact positive kernels (6) can already be used at every
ordered progressive junction, including (13) and (15b). To use a more general
embedded graph one must first perform its explicit ordered bend/crossing
calculation. The corrected cube(15b) has that explicit original Morse
source. Its naive charts have not been rescued by an invented positive
vertex or by an unproved change of tensor order.

## 6. The exact dipole transfer, and why two-belt tree insertion fails at even N

There is a useful local operation on the noncrossing source certificates.
Replace an element e of the ordered edge set by four consecutive elements
e0<e1<e2<e3. In B replace the old e by e0 and add(e1,e2,e3).
In W replace the old e by e3 and add(e0,e1,e2). The new partitions
are noncrossing: each new triple occupies a previously empty contiguous
gap next to the replaced element, while old alternating-endpoint tests
are unchanged. The operation inserts one genuine trivalent cup vertex
and one genuine trivalent cap vertex, with two parallel interior edges.
It preserves all exteriors by the actual ordered Morse construction.

Its full physical transmission is explicit, rather than a scalar
Frobenius multiplication. Put B_i=R^(e_i)L_N on the two INTERIOR
edges, and write ell^S=ell_16 ell_23 ell_45. The open paired-input,
paired-output matrix is

    K=(ell^S tensor I^tensor2)
       (I^tensor2 tensor B_1 tensor B_2 tensor I^tensor2)
       (I^tensor2 tensor J).                            (17)

This is an eight-head cap/box/cup composition, open on all four
exterior physical ends. Every displayed factor is a genuine Hopf
map. Therefore K commutes with the full pair E,F,K action, and the
[all-level physical commutant theorem](actual_pair_casimir_commutant_and_rotated_trace.md#2-exact-commutant-theorem-with-all-jordan-derivatives-retained)
gives K in C[Omega], WITH every projective normal retained.

Let w_alpha be the unscaled physical CD eigenvector from(1). In terms
of the explicit unscaled vertices following(11a), the coherent
EXTERIOR-CIRCLE-OBSERVED transmission kernel is

    w_beta^dagger P K w_alpha
      =N^(-6) sum_(gamma,delta) h_gamma h_delta
            omega_gamma^(e_1) omega_delta^(e_2)
            u_(gamma,delta,beta) conjugate(v_(alpha,gamma,delta)). (18)

This follows by inserting(2) twice in(17), keeping both CD-observed
exterior ports open. Its known coefficients determine the physical
B_3 K B_0 AFTER the exterior complete circles, not the unobserved
K with arbitrary exteriors. Equation(17), rather than(18), retains
K's full all-input matrix and its normals. In fact the paired-node
socle has zero P-self-pairing, so (18) is zero at every even N for
every polynomial K, including nonzero K. It is not a faithful
Hermite frame from which those discarded-by-the-actual-circles jets
can be reconstructed. No contraction to the unknown closed invariant
is used in either formula.
It vanishes unless T_alpha=T_beta, by the TRUE vertex equations(5).
No absolute value or independent maximum of the two interior vertices
has been taken. If the marked cap is in that interior block, v must
instead be replaced by its full marked kernel and K is no longer
being asserted to be an unmarked Hopf transmission.

There is an exact obstruction to using repeated such insertions as an
all-N volume-limit extension. The TWO exterior edges of the inserted
dipole still carry complete circles. Their physical effective map is

    B_3 K B_0=R^(e_3)L_N K R^(e_0)L_N
             =R^(e_3) K R^(e_0) L_N^2.                 (19)

The commutant theorem, not a claimed unitary recoupling, justifies the
commutations. The full complete-circle identity is

    L_N^2=0, N even;
    L_N^2=N^2 E_St, N odd,                             (20)

where E_St is the genuine full simple Steinberg-channel projector.
Paired-node derivative data are INCLUDED in(20): L_N has zero value
and nonzero first derivative there, so its square is zero on the
actual size-two Jordan blocks. Consequently (19) is identically ZERO
as a four-port physical operator at every even N, for every signed
interior and exterior twist and every allowed exterior/co-source.
When the mark lies outside the inserted block this statement applies
directly to the original marked invariant. No zero division, changed
framing, or exponential bound is involved.

The same proof applies to any unmarked four-port Hopf tangle between
two retained complete belts. Thus a source-certified two-belt neck
can kill the even subsequence; local positivity cannot fix it.
The four-vertex example(13) contains such a dipole, explaining its
even-level zeros. In contrast the corrected cube(15b) is simple and
three-edge-connected, has no such two-edge neck, and has the nonzero
even N=4 source certificate above. Its genuine six-port coherent
vertex problem cannot be replaced by(19) or by a scalar tree product.

This leaves a precise new analytic target: the full marked cube packet
(6),(10),(15b), or another source-certified neck-free noncrossing
partition pair, with its ACTUAL jointly constrained saddle. No sharp
positive upper, global noncancellation theorem or Casson--Rivin
identification has yet been proved for it.

Audit: [full-degree CD vertices, literal graph sources and integer charge constraints](../experiments/audit_actual_trivalent_complete_circle_vertex_kernel.py).
Fresh exact cyclotomic-image replay passed seven full-degree CD/vertex
levels, 33 ordered marked source families, six independent twelve-head
and nine primitive twenty-four-head Morse contractions, and 21 all-input
dipole transfers. It also verifies the rejected naive cube's nonzero
ordinary closure. These are finite source/normal audits; no asymptotic
or geometric conclusion is inferred from their numerical range.

Formula (18) retains its observed-only qualification. The vertex-kernel statement does not assert a graph volume or global coherent survival estimate.