# The actual six-port source has a smaller regular generic-q module

29 October 2026. The complete root invariant space is larger than the
source space reachable by an ORIGINAL complete-color plat. There is a
canonical, proper, braid- and circle-stable module obtained by regular
generic-q specialization. This is an actual source restriction, not a
semisimple deletion of the original Casimir normal coefficients.

For six heads its rank is (N^3+N)/2, whereas the full root invariant
space has dimension (2N^3+N)/3. The difference (N^3-N)/6 consists of
extra root invariants which cannot be reached from the original cup by
any regular original tangle. The original marked co-source remains
literal, and compression to this module has NO additional boundary
norm cost. This gives the appropriate source-exact generic 6j input
for a genuine six-ended block. A sharp coherent packet estimate for
such blocks is not supplied by the rank theorem alone.

## 1. The whole root space and its exact octahedral lattice

Use q=exp(pi i/N), Q=q^2, d=N-1 and the ORIGINAL balanced V_N.
The [complete source theorem](actual_complete_source_multiplicity_module.md),
section5, identifies

    Inv_root(V_N^tensor6) = W_2=(V_N^tensor4)_(degree2d).

Its inverse is the specified coefficient of the last two physical
colors(0,d), multiplied by x^d/N, x=q^d. Thus there is no arbitrary
source projection or unidentified scalar in this identification.

Write the four physical labels as (a,b,c,e), with e=2d-a-b-c.
Then the remaining labels obey

    0<=a,b,c<=d,  d<=a+b+c<=2d.                          (1)

The continuous polytope is an octahedron. The integer coordinates

    u=d-b-c, v=d-a-c, w=d-a-b

identify its actual lattice with

    |u|+|v|+|w|<=d,  u+v+w == d (mod2).                  (2)

The inverse is a=(d+u-v-w)/2 and its cyclic variants. Conditions(1)
and(2) are equivalent by checking the eight octahedral facets.
Their lattice count is

    dim W_2=[z^(2d)](1+z+...+z^d)^4=(2N^3+N)/3.         (3)

This is a PHYSICAL source-support polytope. Its name does not identify
it with an ideal octahedron in a link complement or supply geometric
edge equations. A generic Borel tensor of dimension N^3 cannot simply
be substituted for this complete physical module.

## 2. The regular generic-q source lattice

Fix N while varying zeta near q. Let O be the convergent-power-series
DVR at zeta=q, t=zeta-q, and let K be its fraction field. Use the
ordinary highest-weight-d module in the analytic balanced basis

    F|a>=(1-zeta^(2a+2))|a+1>,
    Ecal|a>=zeta^(-N)(1-zeta^(2(N-a)))|a-1>,
    K|a>=zeta^d zeta^(-2a)|a>.                           (4)

The endpoint arrows are zero. At zeta=q these are exactly the
original root generators. The basis change from the ordinary highest
weight basis uses only factorials of indices<N, hence is regular and
invertible at q. The actual finite universal R and its inverse are
also regular: their summation orders are<N and their divided-factorial
denominators do not vanish. This retains the full Cartan phase.

Put M_O=V_d(zeta)^tensor6 over O and define

    Lambda=(Inv_K(M_O tensor K)) intersect M_O.           (5)

It is saturated: if t v belongs to Lambda for v in M_O, the generic
invariance equations imply that v belongs too. Hence M_O/Lambda is
torsion free, Lambda is free, and its specialization embeds into the
physical root tensor without a Tor kernel. Denote its image by

    S_N=Lambda/t Lambda subset Inv_root(V_N^tensor6).     (6)

This is a definition from the actual generic generators, independent
of the numerical knot invariant. Every actual generic braid, its
inverse, and every interval Casimir preserve the generic invariant
space and M_O, hence preserve Lambda and S_N. The same holds for
any polynomial circle coupon in an actual pair Casimir. No individual
Casimir value or generalized direction has been discarded.

## 3. Every original cup source lies in this module

The invariant generic cup can be normalized by its a=0 coefficient
p0=N x^(-d), x=zeta^d. On a+b=d its coefficients are

    p_a=p0 (-x)^a Q^[-a(a+1)/2] F_a F_(d-a)/F_d,
    Q=zeta^2, F_r=(Q;Q)_r.                              (7)

All denominators are units at q. Its successive ratio is

    p_(a+1)/p_a
       =-x Q^(-a-1)(1-Q^(a+1))/(1-Q^(d-a)).              (8)

Equation(8) is exactly the two-head coproduct-F invariant equation;
the E equation follows by the same substitution. At the root,
F_a F_(d-a)=N(-1)^a Q^[a(a+1)/2] and F_d=N, so (7) becomes

    p_a=N x^(a-d),

the literal original cup. Therefore p(zeta)^tensor3 belongs to Lambda,
and EVERY original braid/circle word applied to that cup specializes
into S_N. Arbitrary external rows may be contracted afterward. In
particular the original ordinary caps and full marked cap are kept.

This restriction concerns original deformable source inputs. It is
not an all-input identification of the larger root invariant space
with a generic-q invariant space. A root-only Hopf coupon with no
regular generic lift need not preserve S_N; no such coupon is inserted
into the original argument here.

## 4. Exact rank: ordinary triangular channels, not a root semisimplification

Over K the tensor of two highest-weight-d modules is the direct sum
of the highest-weight-2a modules W_a, a=0,...,d, each once. This follows
directly from their distinct generic pair Casimirs, their explicitly
constructed highest vectors and the dimension identity
sum_a(2a+1)=N^2, as in the actual Casimir proof.

Three such channels have a one-dimensional invariant precisely when

    0<=a,b,c<=d,  |a-b|<=c<=a+b.                         (9)

Indeed the same two-factor highest-vector calculation decomposes
W_a tensor W_b into the weights 2a+2b-2r, r=0,...,2min(a,b).
It contains W_c exactly under(9), once; the unique pairing with W_c
then gives the invariant. This uses generic distinctness, not a root
semisimplicity assertion.

Count the triples: of the N^3 triples, those with a>b+c number

    sum_(a=1)^d a(a+1)/2=d(d+1)(d+2)/6.

The analogous three violations are disjoint. Consequently

    rank Lambda=dim S_N=(N^3+N)/2,
    dim Inv_root-dim S_N=(N^3-N)/6.                     (10)

The latter is a PROPER subspace already at N=2. Thus it would be
wrong either to identify the whole root Inv space with a generic
6j channel space, or to infer that generic source specialization
loses the actual original word. The saturated lattice distinguishes
these two statements.

## 5. A fully specified finite recoupling kernel before specialization

No published TV/shadow state sum is needed to construct the generic
six-port kernel. Here is a direct finite tensor construction with all
coordinates specified. For the complete pair and its channel W_a put
k=d-a. Its highest vector h_a=sum_(r=0)^k b_r |r,k-r> has b0=1 and

    b_(r+1)/b_r
       =-x^(-1)Q^(k-1-r)
                   (1-Q^(a+1+r))/(1-Q^(d-r)).           (11)

These are units near q; their derivation is the actual coproduct-E
equation in(4). Let iota_a:W_a->V_d tensor V_d send its divided-F
basis vector of index r to F_pair^r h_a/(Q;Q)_r.

For arbitrary ordinary channels W_a,W_b, their highest vector for
the W_c component has index k=a+b-c and coefficients beta_r,
beta0=1. In its own balanced bases define

    e_a(j)=zeta^(-2a-1)(1-Q^(2a+1-j)),
    K_a(j)=zeta^(2a)Q^(-j).

Then

    beta_(r+1)/beta_r
           =-e_b(k-r)/[e_a(r+1)K_b(k-1-r)].             (12)

Divided-F descendants define iota_(a,b)^c. Compose it with the
nonzero ordinary cup of W_c, then with iota_a tensor iota_b tensor
iota_c. This gives one explicitly normalized rational six-head
invariant B_abc for every triple(9). Formula(7), with the appropriate
highest weight and a fixed p0=1, specifies the internal cup too.
Thus all B_abc are finite products/sums of actual Gaussian factorial
coefficients and fixed Cartan phases.

Let B_T be the resulting column matrix for a chosen paired tree T.
It has full generic column rank(10). Choose any nonzero maximal minor
to form an explicit rational left inverse L_T. A specified genuine
SIX-ENDED tangle, after bending its incoming legs by the original
duality, gives a physical invariant tensor Psi_G. Its exact channel
coordinates are L_T Psi_G, and

    Psi_G=B_T(L_T Psi_G).

The physical contraction defining Psi_G, including any internal
crossings/circles, is retained; this does not assert that a generic
trivalent B_abc is already a particular geometric shadow block.
For an actual BRAID ENDOmorphism R_G on six physical heads, its
complete channel transport matrix is exactly

    K_(T',T)(G)=L_(T') R_G B_T.                          (13)

Changing trees or multiplying tangles gives the same actual physical
map, because all columns represent the SAME invariant vectors. This
is the source-relevant finite 6j construction. No equality of an
unpointed cyclic Borel 6j with the original marked source is assumed.

At the root, denominators with index>=N can vanish. One MUST compute
(13) on the saturated lattice(5), equivalently take its complete Smith
regularization before specialization. Taking values of the generic
channel matrix alone would omit precisely the confluent information
at risk. The original R's first Casimir derivatives, and any additional
source-frame normal coefficients required by that lattice, remain.
No uniform bound on the norm or necessary jet order of this generic
frame is asserted here; an unspecified minor inverse is not a tame
metric. The physical saturated source space itself is nevertheless
completely defined and source exact by(5)--(10).

## 6. Polynomial-cost compression and a concrete further Ward constraint

Transport S_N to W_2 by the original coefficient isomorphism. Let P_S
be its orthogonal projector in the specified physical orthonormal W_2
basis. The complete original source theorem has

    w0=p tensor p, lambda=ell tensor ell,
    original scalar=chi_N lambda B_word w0,
    ||w0||=N^3, ||lambda||=N^(-1).                      (14)

Here the FULL marked cap was reduced only after the whole invariant
tensor identity. Since w0 and every original state lie in S_N, insert
P_S on both sides of every reduced generator without changing(14).
Its norm is one, and the restricted boundary row has no larger norm.
Thus the original boundary norm product is at most N^2, with no new
exponential cost. This is an actual source-specific compression before
choosing a geometric metric. It does not yet bound the word's energy.

There is also a concrete normal Ward operator. In the generic physical
tensor define the ordinary divided power

    E^[N]=E_tot^N/[N]_zeta!,

with the fixed nonzero conversion between E and Ecal retained. This
has a regular matrix on tensors of highest-weight-d modules: in the
divided coproduct formula all individual indices are<N, and terms
with a local index>=N vanish identically. Every generic invariant is
killed by it. Hence S_N is killed by its specialized normal operator.

Under the W_2 extraction, this implies specifically

    E_(first4)^[N] w=0,   w in S_N.                      (15)

To check(15), project the global divided-power equation to last colors
(0,d). Last color d forces zero lowering there. In H_2(w), fifth input
c>0 contributes E_4^c w and requires c lowering in that head; the
remaining ordinary E_4^(N-c) then yields E_4^N=0 at the root. All such
denominators are units. Only c=0 leaves E_4^[N]w, multiplied by the
known nonzero extraction factor. Its target degree is N-2, of dimension

    [z^(N-2)](1+z+...+z^d)^4=binom(N+1,3),

exactly the dimension difference in(10). The separate
[divided-current kernel theorem](actual_six_port_divided_power_source_kernel.md)
now proves this surjectivity, rather than inferring it from the count:
in its literal first-normal normalization J_E J_F=-2N^2 I on that
target. Consequently the saturated source is EXACTLY ker J_E, and
its algebraic projection is I+J_F J_E/(2N^2). The proof retains both
E/F constraints and all original Cartan signs. The projection is
oblique; no polynomial operator-norm estimate follows from its
displayed denominator. The
[all-width normal-current calculation](actual_all_width_divided_source_projection.md)
extends the same kernel identification to every even plat width.

The normal Ward is a genuine all-source constraint at level N, not
an ordinary fixed-degree observable or an independently imposed angle
edge charge. It is compatible with retaining the original normal
source instead of quotienting it to zero.
Derivatives of the WHOLE source in q still satisfy differentiated
inhomogeneous Ward equations; this root-value restriction does not
make those equations homogeneous.

## 7. The precise analytic six-port task still needed

The reduction above exposes a concrete local problem. For a SPECIFIED
prime six-ended block with its literal physical tensor Psi_G, the
coordinates L_T Psi_G and transport(13) must be specialized on the
lattice(5). To use that block in the general long-filling theorem
one needs a uniform complex saddle/packet estimate for this COHERENT
finite Clebsch contraction, on a bounded geometric color corridor,
and a bound on its complementary root channels. No particular prime
block is identified solely from the coordinate count. The ordinary triangle
domain(9), physical support(2), and divided-power constraint(15) must
all be retained; they are not three independently summable scalar
circle registers.

The naive alternative of replacing such a vertex by commutative
Frobenius multiplication is specifically invalid: the exact circle
algebra has L_N^2=0 at even levels, so a tree built only from that
connector and scalar multiplication already collapses. The
[circle-source extension](general_augmented_graph_source_extension.md)
retains that warning. Conversely the generic-q 6j frame alone has no
proved sharp large-N norm and its polar factors cannot be declared
subexponential. A uniform coherent estimate of(13), together with its
normal Ward source, is the next analytic input; a TV state sum is not
substituted for the original scalar.

This is a structural extension beyond the two-port turn algebra:
it supplies a proper, exactly source-stable six-port module, an explicit
finite actual Clebsch construction and a new normal Ward constraint.
It does not declare a new broad geometric source packet proved, and
does not change the active general equality objective into a formal
recoupling identity.

## 8. Focused verification

[The new audit](../experiments/audit_actual_six_port_deformable_source.py)
passes three COMPLETE generic six-port Clebsch frames at N=2,3,4,
including every triangular channel, literal E/F/H invariance and full
column rank. Four original root families at N=2,...,5 check the exact
octahedral parity lattice, the regular generic cup's literal root
specialization, all five induced physical braid generators, and a
mixed signed word against the full six-head marked scalar. Their
source cyclic ranks are respectively5,15,34,65, agreeing with(10).
The rank theorem for S_N is the analytical saturation/count argument;
no uniform claim that the cup is cyclic in S_N is inferred from these
finite checks. No numerical asymptotic or tame six-port-frame estimate
is asserted.
