# Exact three-port source sewing before and after the root normal

29 October 2026. An actual NC/Morse vertex substitution has a generic
three-port elimination, with an explicitly normalized theta denominator.
At a supported boundary it preserves the original FIXED first normal:
the new raw marked scalar is the product of the two old raw scalars
divided by the positive actual marked theta scalar. This is not root
multiplication of circle coupons. Unsupported boundaries retain their
explicit open-column/source jets before an actual six-head support
identity proves their complete-circle contribution zero.

The theorem is channelwise at arbitrary N, with all three correlated
boundary labels and original normal factors retained. It supplies a
survival transfer when the two actual input sources are known. It does
not prove a new all-N asymptotic for an unsolved primitive cube block,
identify arbitrary six-pants boundary maps, or complete the graph-volume
problem.

## 1. A literal NC vertex substitution, including the pointing

Let A,B be ordered NC/Morse graphs of the
[corrected exposed-source theorem](actual_nc_morse_graph_first_normal_source_reduction.md).
A has an interval black vertex u on edge slots (a,a+1,a+2), and an
EXPOSED white marked cap elsewhere. B has an outer white vertex w on
edge slots (0,k,E_B-1), so every other white block is in one of its
two gaps. Give B the exposed mark at w. Match the three boundary labels
in their displayed order; call them (a0,b0,c0).

Remove u and w and glue their three edge ends IN ORDER. Concretely
replace A's three-slot interval by B's whole edge row, map the three
old A contacts to a+(0,k,E_B-1), move subsequent A slots by E_B-3,
and map every B slot e to a+e. Keep the other vertices. Black A
blocks surround or avoid the replacement interval; the inserted black
blocks are noncrossing within it. The old white blocks are mapped
monotonically, and new white blocks lie strictly in the two previously
empty contact gaps. Thus both new partitions remain noncrossing.

The original p/ell matchings give a literal new Morse word. A's exposed
marked cap remains exposed; no inserted white block can surround its
contacts. All statements below use that point, not a bare mark moved
to a nested cap. The two merged edge exponents ADD. The new edge has
ONE coupon R^(e_A+e_B)L_j, not the product of the two old circle coupons.
No L_j^2 has been substituted or inverted at the root.

## 2. A genuine invariant output column, not a guessed scalar exterior

Fix generic zeta near q=exp(pi i/N), and the canonical ordinary Q_j
tensors, duals and actual edge constants of the first-normal theorem.
Assume first that every local ordinary triple is triangular. Remove
ONLY B's outer white row D(Theta_c0,b0,a0). Contract every other
ordinary vertex in B. The resulting column is

    Y_B(zeta) in Q_a0 tensor Q_b0 tensor Q_c0.       (1)

It is a genuine homogeneous invariant. For a direct proof, the
noncrossing black source is built by inserting interval invariant
triples, hence is globally invariant. Every white block other than
w can then be removed in its innermost interval order, by a genuine
ordinary invariant covector. All blocks are in w's two gaps. What
remains are its three ordered output ports, with no intervening cap,
braid, or free tensor permutation.

The ordinary invariant space has dimension ONE at generic zeta, and
its normalized Theta_a0,b0,c0 has corner (2a0,b0+c0-a0,0) equal to one.
Every local coefficient is regular at the root. Consequently

    Y_B=alpha_B Theta_a0,b0,c0,
    alpha_B=(Y_B)_(2a0,b0+c0-a0,0),                 (2)

with alpha_B a HOLomorphic finite function, computed by the open
magnetic contraction. This is an all-entry identity of that source
column and can be paired with an arbitrary exterior row. No invariant
or regularity assumption about A's exterior row is needed.

Let Xi_A,Xi_B,Xi_new be the complete ordinary networks. The fully
normalized ordinary theta is

    Xi_theta=D(Theta_c0,b0,a0)Theta_a0,b0,c0.

Then (2) gives exact generic identities

    Xi_B=alpha_B Xi_theta,
    Xi_new=alpha_B Xi_A,
    Xi_theta Xi_new=Xi_A Xi_B.                     (3)

The scalar alpha_B is not defined by contracting the unknown final
invariant: it is the explicit open corner in (2). In particular its
regularity is proved BEFORE division by Xi_theta. If the boundary
triple is nontriangular, the actual invariant column (1) is zero and
the new source is identically zero. Nontriangular interior vertices
are likewise zero; they are not omitted as a semisimple convention.

## 3. The denominator has an exact root order and source normalization

Write a,b,c for the boundary labels in this section and set

    J=a+b+c, r=b+c-a, r1=a+b-c, r2=a+c-b,
    F_l=(zeta^2;zeta^2)_l.

The independently proved finite Vandermonde evaluation is

    Xi_theta=(-1)^r1 zeta^[2c-r1(r-1)]
       F_(2b)F_r2 F_(J+1)
             /[(1-zeta^2)F_r F_(2a)F_r1 F_(2c)].    (4)

All denominator factorials have index <N. Thus

    ord_q Xi_theta=1 if J>=d, and 0 if J<d, d=N-1.  (5)

The numerator contains at most one factor 1-zeta^(2N), since J+1<2N.
Formula (4) applies to odd simple and even/odd paired axes without
separating away their original source factors.

Let F_A,F_B,F_new be the ordinary GENERIC physical closures in the
chosen regular Hopf lift, and use C,S as in the first-normal theorem.
The new constants are exactly

    C_new=C_A C_B/C_theta,
    C_theta=product_(boundary j)h0_j gamma_j,
    S_new=product_(vertices of A except u)s_v
                              *product_(vertices of B except w)s_v. (6)

Boundary edge twists are added, so their omega factors occur in C_new
with the correct sum. Both removed source factors are the actual
s_abc and s_cba. In particular the cross-multiplied identity is

    F_theta F_new=F_A F_B,
    F_theta=C_theta s_abc s_cba Xi_theta.           (7)

This keeps ALL phases, G factors, h0 first normals and fixed gamma
units. Each remains present exactly once on a new edge. The source
identity is generic and does not divide by nilpotent root operators.

For J>=d the actual s_abc(0),s_cba(0) are nonzero, Xi_theta has a
simple zero, and

    F_theta'(0)=nu_N Z_theta!=0,
    nu_N=2N(-1)^N/(q-q^(-1)),
    Z_theta=N^2 k_a k_b k_c
                         s_r s_r1 s_r2/s_(J-d) *R_N(a,b,c)^2>0. (8)

Here R_N is the already proved positive finite source partition,
not an assumed quantum 6j. Equation (8) is a fully explicit boundary
weight. It may be exponential and must not be called a polynomial
normalization cost.

## 4. Exact fixed-normal gluing and order addition

Each exposed physical closure is F_G=D_N z_G, where
D_N=(-1)^d[N]_zeta has its simple zero at q and z_G is the actual
regular open scalar. For a SUPPORTED boundary (J>=d), equation(7)
therefore gives a holomorphic identity

    z_new=z_A z_B/z_theta,

because z_theta(q)=Z_theta>0. In particular the original raw marked
scalars, with no transported or repeated mark, obey

    Z_new=Z_A Z_B/Z_theta.                          (9)

This formula holds even if one of the pieces has a zero raw scalar
or a retained unsaturated marked-white current. Those pieces are
the complete exposed original sources, not just a selected leading
saddle. All such terms are included in their z_G.

For nonzero generic ordinary spin networks, (3) gives

    v(Xi_new)=v(Xi_A)+v(Xi_B)-v(Xi_theta),           (10)

where v is the exact order at q. The regular alpha_B proves this
without assigning a first-nonzero convention to the original source.
For supported seams and nonzero physical closure germs one similarly
has v(F_new)=v(F_A)+v(F_B)-1. Thus two genuine simple physical zeros
give a simple zero after sewing. If a piece has higher order, its
fixed first-normal value vanishes and (9) retains that zero.

Any original external lines remain explicit. If K_G=chi_G Z_G, then
the corresponding relation has the extra factor
chi_new chi_theta/(chi_A chi_B); it cannot be suppressed without
the actual framing/normalization certificate.

## 5. All boundary channels, including the unsaturated current

The ordinary column (2) and identity (3) hold at EVERY triangular
folded boundary label. For J<d, Xi_theta(q) is a unit. The two
removed source factors s_abc(q),s_cba(q) are zero; it is not valid to
divide root marked scalars by Z_theta=0. Instead the exact formula is

    Z_new=C_new/nu_N *d/dt|0
          {S_new(t) Xi_A(t) alpha_B(t)}.             (11)

All local source factors in S_new are defined by actual finite
Clebsch/cup contractions and their explicit first jets. Thus (11)
retains the local unsaturated source normals, including a local
marked-white current inherited from A. It does not infer them from
the zero closed values of the removed boundary vertices.
Using alpha_B=Xi_B/Xi_theta here is harmless because this particular
ordinary denominator is a root unit.

For full circles, the shared boundary triple must be summed ONCE,
and its three labels remain correlated. If Z_A(a,b,c),Z_B(a,b,c)
denote the complete coherent interior sums with those labels fixed,
the whole new scalar is exactly

    sum_(a+b+c>=d) Z_A(a,b,c) Z_B(a,b,c)/Z_theta(a,b,c). (12)

There is no omitted unsaturated correction in this COMPLETE-circle
operation. The [exposed six-port pruning theorem](actual_exposed_six_port_complete_circle_pruning.md)
proves it before the exterior or mark acts: remove B's three boundary
coupons and every ordinary cap other than its omitted outer vertex.
The remaining physical six-head column is a regular generic invariant,
so its root lies in the actual saturated S_N. The three boundary
coupons commute with those disjoint cap removals and can be applied
last. Their full complete-circle product annihilates S_N when J<d.
This proves that the exact expression(11) vanishes as a WHOLE source;
it does not set its local source derivatives to zero. Nontriangles
are zero as well. The positive denominator in (12) does not make its
numerator a square: the two actual packets need not be conjugates.
A physical mirror/reflection identity would still be needed before
asserting a positive graph norm.

## 6. An explicit primitive cube corner, with three finite sum variables

For the genuine ordered cube use black blocks

    (0,1,2),(3,4,11),(5,9,10),(6,7,8)

and ordinary white blocks (1,8,9),(2,3,7),(4,5,6), leaving outer
white (0,10,11) OPEN. Put j_0=a,j_10=b,j_11=c, fix boundary magnetic
colors r_0=2a,r_10=b+c-a,r_11=0, and write J_v for the sum of edge
labels at the indicated vertex. Define

    B0=j_1+j_2-a,
    B1=j_3+j_4+c,
    B2=j_5+j_9+a-c.

For free magnetic integers u,v,w set

    r_1=u, r_2=B0-u,
    r_3=v, r_4=B1-v,
    r_5=w, r_9=B2-w,
    r_8=J_(1,8,9)-B2-u+w,
    r_7=J_(2,3,7)-B0+u-v,
    r_6=J_(4,5,6)-B1+v-w.                          (13)

The remaining black magnetic equation holds identically by boundary
weight conservation. Therefore alpha_cube is exactly the triple sum
over (13) of the FOUR canonical black Theta entries and the THREE
genuine white dual Theta entries. Require 0<=r_e<=2j_e on EVERY
edge; otherwise the term is zero. Each individual entry is the
explicit finite ordinary coefficient(6),(7) of the first-normal
theorem, including its phase. There is no extra closed physical
source or unknown inverse frame in this formula.

This is a usable all-N primitive open-column scalar. The full column
is alpha_cube Theta_boundary by (2), so the triple sum is not just
one arbitrarily chosen bad entry. At spin one its exact evaluation
is g^3(D^3-9D^2+29D-32), recovering the independently proved generic
flow model. A positive high-fold evaluation or a large-N nonzero
estimate for the general triple sum remains open; absolute values
of its summands would discard precisely the coherence to be proved.

## 7. An exact order-two counterexample to a graph-only criterion

At N=5, d=4 and M=2, take two actual ordered cubes. In A give its
interval black edges (0,1,2) labels (1,1,1); every other edge has label2.
In B give its outer white edges (0,10,11) labels (1,1,1); every other
edge has label2. Perform the typed substitution. The new graph has
fourteen vertices and twenty-one edges and is three-edge-connected
by the vertex-sum proof. Its marked cap remains exposed. Every
remaining vertex triple has sum FIVE or SIX, hence is fully supported
and has the strictly positive local source scalar. The separating
three-edge triple itself has sum3<d.

The new ordinary network nevertheless has order EXACTLY TWO.
Here is a compact exact certificate for the only additional zero
needed. Evaluate B's triple sum(13) in Q(q), with

    Phi_10(q)=q^4-q^3+q^2-q+1=0.

There are fifty nonzero terms. Group them by u=r_1=0,1,2,3.
Their reduced coefficients in the basis (1,q,q^2,q^3) are

    u=0: (  58, -58,   0,  -92),
    u=1: (-386, 236, -92,  476),
    u=2: ( 476,-234, 150, -528),
    u=3: (-148,  56, -58,  144).

Each column sums to zero. This is an exact reduction of the explicit
finite canonical Clebsch sum, using only polynomial arithmetic and
inversion of units modulo Phi_10. It proves alpha_B(q)=0 over the
complex numbers, not just in one finite field.

Its first derivative is nonzero. The exact rational first-jet
formulas reduce modulo the prime 1021 at q->432, a primitive tenth
root, to

    alpha_B'(q)->909,
    Xi_A'(q)->775.

Every denominator is a unit in this reduction. A zero algebraic
derivative would reduce to zero, so these nonzero images certify
nonzero derivatives. Xi_A(q)=0 independently: A's exposed outer
triple is (1,2,2), whose regular outer-column factor contains the
simple Xi_theta zero. Thus v(Xi_A)=1 and v(alpha_B)=1. Equation(3)
gives v(Xi_new)=2; its second Taylor coefficient has nonzero image
775*909=1006 modulo1021.

All NEW vertex source factors are nonzero by their supported sums.
Therefore the new physical ordinary closure also has order two,
and the original fixed-first-normal marked sector is ZERO. Its
higher normal is nonzero. This is not a zero of the full channel
sum or a counterexample to a volume statement. It proves that
connectivity, absence of a two-edge neck, and positive supported
VERTEX scalars do not by themselves ensure simple source order.
The separating source constraint matters. It agrees with the
all-N six-port pruning theorem rather than deleting its higher jet.

The [focused audit](../experiments/audit_actual_nc_three_port_source_sewing.py)
checks open-column invariance and all entries, exact local theta
normalization, NC/pivotal pointing, ordinary and full marked sewing,
the cube triple-sum corner, the physical divided-current pruning,
and the exact cyclotomic certificate above. No graph-volume or
unconditional all-N cube survival claim is made.

Independent internal reviews: root read the source sewing, exposed
pointing and pruning arguments. The global audit agent independently
read sections1--7 and the separate pruning proof, checked the C/S
cancellations and fixed-normal quotient, and freshly replayed the
audit: PASS nineteen sewings, five physical six-head Ward/divided-
current pruning families, the nested-cut countercurrent and the
exact QQ(q) order-two certificate. No correction was required to
these corrected exposed statements. These are internal checks,
not external peer review or an all-N primitive-core estimate.
