# Balanced anchors and the actual alternating-knot source

28 October 2026. In the exact charged source of an alternating
one-component diagram, vanishing of every individual anchor defect
forces all overcrossing clocks to be equal. This is a topological
incidence statement, not a knot census.

For the original figure-eight state the resulting diagonal clock
sectors are ALL annihilated, at every level. More strongly, every
nonzero clock sector has an anchor defect of size at least (N-1)/2.
Thus individual sublinear-defect star estimates, or a positive
balanced-anchor chamber alone, cannot cover this actual source.
Further clustering/fusion may transport these defects; no statement
that such a global method is impossible is made.

## 1. Alternation determines the defect equations

Use the exact [charged source](actual_global_charged_bridge_flow.md)
and [source closure contraction](actual_general_flow_fusion.md).
Put d=N-1. In a strictly alternating diagram, each maximal overbridge
is a single crossing. After contracting the original closure-adapter
forest, its anchors are the physical oriented segments between
successive OVER encounters. Each such segment contains exactly ONE
UNDER encounter.

Let crossing i be its first over encounter and j its next over
encounter. If its under encounter has clock h_l, the three
contributions to the anchor's incident linear-factor count are

    h_i             from the first over-output block,
    d-h_j           from the final over-input block,
    (d-h_l)+h_l=d   from the spectator under encounter.

A self-loop is counted twice, since it contributes a factor of that
anchor at both ends. Phase rescalings from the retained pivots do
not change these counts. Hence the EXACT incidence and defect are

    S_(i->j)=2d+h_i-h_j,
    delta_(i->j)=S_(i->j)-2d=h_i-h_j.              (1)

The successor relation on over encounters is one cycle for a
one-component knot. Therefore

    all delta=0  iff  all crossing clocks h_i=H.    (2)

For a link the same conclusion is componentwise. Formula (1) is
valid independently of crossing signs. It uses physical over/under
roles and survives the exact signed source gluing, rather than
identifying successive braid positions with successive physical
strand encounters.

## 2. The actual figure-eight cut forces its first clock to zero

Take the original signed word [1,-2,1,-2], with clocks
(h_0,h_1,h_2,h_3). We retain the original averaged pivotal scalar.
The initial use of INTEGER degree conservation to write it as

    (1/N)Tr[(I tensor g tensor g)W]                (3)

is made before decomposing into clock sectors, as in the charged
source theorem. No Schur lemma or marked-row substitution is
applied to an individual h-sector afterward.

For the support calculation choose fixed cyclic Fourier grids on
head i with root x^(i-1), x=-exp(-pi*i/N). At a positive adjacent
crossing these roots differ by x. The outgoing first propagated
root is Q^(-1) times its fixed root; the other outgoing root is
unchanged. Thus if (a,b;c,e) are its fixed-grid input/output colors,
the actual overclock at the first +sigma_1 crossing is

    h_0=[b-c-1],                                  (4)

where brackets mean the representative in 0,...,d. The same-grid
crossing is the exact finite Fourier transform of the original R,
even where its old raw four-Psi presentation was singular. The
closed polynomial port formulas extend there; their normalizer
is a nonzero monomial.

These clock dictionaries are unchanged by the propagated prefixes.
If a positive under-input root has offset Q^v from its fixed
position root, its under-output root has offset Q^(v-1), since
it is x times the input root. The difference of the two label
offsets therefore still gives b-c-1. For a negative understrand
the offsets are Q^v and Q^(v+1), giving e-a-1. Thus resetting
the grid labels does not silently replace the actual clock variables.

Here is its elementary support dictionary. Put

    u=[b-a-1], v=[a-c], t=[c-e], z=[e-b].

The two positive Pochhammers are nonzero exactly when

    u+v+t+z=d,
    h_0=u+v.                                      (5)

For example the first Pochhammer says u<=h_0 and then v=h_0-u;
the second says z<=d-h_0 and then t=d-h_0-z. The negative table
gives the same support equation, with its overclock u+z instead.
Equivalently supported crossing colors have cyclic lifts

    b<=e_lift<=c_lift<=a_lift=b+[a-b].              (6)

For clarity, the cut-support argument is recalled here. For fixed
sentinels L,R define

    V(x)=[L-x_1]+sum_i[x_i-x_(i+1)]+[x_b-R].

The cyclic interval (6) makes V nonincreasing at every supported
crossing: the two outside triangle inequalities have defects
which are nonnegative multiples of N, and their middle intervals
sum to [a-b]. The trace source (3) has input
(A_1,[A_2+1],...) and output (A_1,A_2,...), because the actual
pivot is a nonzero scalar times the cyclic shift. Choose L=A_1
and R=[A_b+1]. The endpoint difference of V is zero if A_2=A_1
and -N otherwise. Thus A_2=A_1 and V is constant along every
supported source path.

Translate colors by -A_1; this changes none of the support tests.
The first head begins and ends at zero. The left triangle equality
at position1 gives [0-c]=[0-a]+v. Its nonnegative increments must
sum to zero, so v=0 at every position1 crossing and that head
stays zero. Before the FIRST such crossing the second head stays
one: its distance [0-x_2] is nondecreasing and begins at its maximum
d. Thus at that first crossing a=0,b=1, so u=v=0.

This proves pointwise, for EVERY cut color in the averaged source,

    nonzero fixed-clock source sector implies h_0=0. (7)

This is the same support argument independently proved in
[the original cyclic-cut theorem](original_source_cyclic_variation_peeling.md),
with its mapping (4)--(5) to the present clocks made explicit.
It does not require intertwinement of separately split sectors.
The center-independent homogeneous source theorem transports
this support calculation back to its original regular frames.

## 3. A second support inequality in the actual reduced polynomial

There is also a direct regular-Fermat test of the full reduced
four-anchor polynomial. Up to a nonzero scalar, rescale its two
anchors B,D by x^(-1), and call the four new variables A,B,C,D.
Choose all four new variables to be Nth roots of one. This is
permitted by the exact finite-flat source theorem, not a change of
invariant or a pointwise replacement of the old raw kernel.

The eight actual blocks have the following lengths and root starts:

| tail -> head | length | start exponent p in (tail-Q^p head;Q)_L |
| --- | --- | --- |
| B -> C | d-h_0 | 0 |
| C -> A | h_0 | 1 |
| D -> A | d-h_1 | h_1+1 |
| A -> B | h_1 | -h_1+h_2+1 |
| C -> B | d-h_2 | h_0+h_2+2 |
| B -> D | h_2 | -h_2-h_3-1 |
| A -> D | d-h_3 | -h_1 |
| D -> C | h_3 | 0 |

This table includes all original closure pivot substitutions. It
is a direct application of the actual graph metadata and full-block
source contractions. No new graph or exterior coupon is introduced.

Let a,b,c,e be the root-grid color indices of A,B,C,D. If a grid
summand is nonzero, the D->A block forces

    r=[e-a] in [0,h_1].

The A->D block forces [a-e+h_1] in [d-h_3,d]. Since r<=h_1,
the left representative is the ordinary integer h_1-r. Hence

    h_1-r>=d-h_3,
    h_1+h_3>=d.                                    (8)

The endpoint cases with an empty block give the same (possibly
vacuous) inequalities. If (8) fails, EVERY point on this regular
Fermat grid has polynomial value zero. Its exact source coefficient
is therefore zero. Thus (8) is necessary for a nonzero h-sector,
not merely an absolute-envelope or stationary-point condition.

There is an independent pathwise check of (8), in the same cyclic
coordinates as Section2. With first cut color zero, the source-cut
support forces the four intermediate states to have the form

    initial (0,1,B+1),
    after first  (0,D,B+1),
    after second (0,E,F),
    after third  (0,0,F),
    final        (0,0,B),

all colors interpreted cyclically. The fourth negative crossing
has current clock h_3=[B-1]. If B=0 it is d, proving (8).
If B>0, its cyclic interval forces 1<=F<=B. At the second
negative crossing h_1=u_2+z_2 with

    u_2=[B-D]>=0,
    z_2=[F-B-1]=N+F-B-1>=N-B.

Thus h_1+h_3>=(N-B)+(B-1)=d. This argument uses only actual
supported paths before summation. The grid offsets just checked
show that h_1,h_3 here are the present propagated overclocks,
not renamed old-corner variables.

## 4. Balanced diagonal sectors vanish, and defects must be macroscopic

For this alternating one-component diagram, (2) makes every
balanced clock sector (H,H,H,H). But (7) would force H=0, while
(8) would require 2H>=d. As d>=1, these are incompatible. Therefore

    lambda(P_(H,H,H,H))=0,
       EVERY N>=2 and EVERY H in 0,...,d.           (9)

There is no asymptotic qualifier: the WHOLE fixed-H coefficient
vanishes exactly in the actual original source.

More generally, any nonzero sector has h_0=0 and
max_i h_i>=d/2 by (8). Its cyclic clock range is therefore at
least d/2. Along the physical four-overencounter cycle, total
variation is at least twice the range. In fact the actual physical
successor is (3,0,1,2), so the four defects are exactly

    (-h_3,h_1,h_2-h_1,h_3-h_2).

Using (8) gives the stronger explicit bound

    sum_anchors |delta_i|>=d,
    max_anchors |delta_i|>=max(h_1,h_3)>=(N-1)/2.    (10)

Thus no sequence of nonzero figure-eight clock sectors can have
all individual anchor defects o(N) in this representation.
The positive balanced-anchor maximum principle and the retained
sublinear local defect jets are consequently insufficient by
themselves for its actual volume contribution.

This does not rule out cluster reductions: full-kernel fusion can
add opposite defects, and exact phase-aware fusions can change the
remaining source variables. Equation (10) must be respected before
such a further operation; it does not prove that a macroscopic
defect core can never be reduced or analyzed geometrically.

## 5. Reproducible audit

    python3 experiments/audit_actual_alternating_balanced_source.py

The audit verifies the sign-independent physical successor and
incidence formula on actual alternating signed words after all
original closures, the local cyclic-support dictionary directly
against both original R matrices, the general reduced figure-eight
block table, and exact zero of every diagonal sector at multiple
levels. It separately checks the regular-grid support implications
without replacing them by coefficient-modulus estimates.
