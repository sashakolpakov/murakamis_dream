# A nonzero outward action gradient at every physical state face

28 October 2026. In the original one-component scalar source, adjacent
head factorials can be combined before estimating a boundary. Their
exponents are even, whereas every independent transfer has exponent
minus one. This elementary parity forces a nonzero radial logarithmic
coefficient at EVERY proper physical face. Each face admits an outward
direction lowering the complete marked action. Individual factors need
not go to their separate preferred sides.

The statement is uniform over the finitely many faces of any fixed
NONEMPTY braid word with one-component closure, at arbitrary width.
The empty one-strand unknot has constant density and is excluded.
It is not yet a deformation of the whole
original cycle or a sharp bound for its scalar. In particular, local
changes of integer cotangent charts have their own side currents.

## 1. The exact gathered factorial source

Use the original averaged cut before splitting the state, as justified
in [the scalar completion](actual_scalar_cardinal_source_completion.md).
Follow the one physical component once, listing its 2m crossing visits.
Visit i has transfer k_(j(i)) and increment eta_i k_(j(i)), eta_i=+/-1.
Each crossing appears twice, with opposite increments. Thus

    h_0=t, h_(i+1)=h_i+eta_i k_(j(i)), h_(2m)=t.       (1)

The variables (t,k_1,...,k_m) are independent integer coordinates.
Every arc form h_i has coefficient one on t. Its other coefficients
are 0,+1,-1. The physical source is exactly

    0<=t,k_j<=d, 0<=h_i(t,k)<=d, d=N-1.               (2)

The original signed coefficients at one visit contribute a factorial
exponent -eta_i at its input and +eta_i at its output. This is true
for both crossing signs after the EXACT conversion

    Fhat_-(s)=exp[i*pi*s-i*pi*s*(s+1)/N] Fhat_+(s).   (3)

Equation (3) follows from the common real Gamma product, not just
from equality at integer s. Its quadratic factor is retained. Therefore
the full scalar has gathered factorial part

    product_i Fhat_+(h_i)^(c_i) / product_j Fhat_+(k_j),
    c_i=eta_(i-1)-eta_i in {-2,0,2}.                 (4)

All cyclic indices in c_i refer to the physical component. Coincident
arc forms may be kept as separate occurrences; their exponents add.
Every original Cartan, pivotal and framing scalar and the chirps (3)
remain outside (4). The combined quadratic factor has unit modulus
on real indices, but is not discarded on complex contours.

## 2. Integral face coordinates and vertices

Scale (2) by d and call the resulting polytope P in R^(m+1).
It has strict interior: t=1/2 and all k_j sufficiently small and
positive put every h_i strictly between zero and one. Its defining
integer matrix is totally unimodular. Here is a direct proof.

In traversal order, each transfer column of the arc matrix is +1
or -1 on ONE contiguous interval between its two visits and zero
elsewhere. The t column is all ones. Negate negative columns.
For any square minor, selected arc rows retain this interval property.
Successive row differences turn each column into at most one +1 and
one -1. This row operation has determinant one. Such a square matrix
has determinant 0,+1,-1: expand a column with at most one nonzero;
if none exists, all column sums vanish and the determinant is zero.
Adjoining unit transfer rows preserves the assertion by expansion
along those rows. Upper inequalities only negate rows; duplicate
opposite rows give zero minors. This proves the claim for (2).

At a vertex, m+1 independent active rows consequently have determinant
+/-1. Their right sides are integers, so the vertex is integral.
Since t,k_j are all in [0,1], EVERY vertex lies in {0,1}^(m+1).
All its physical arc forms are also zero or one.

Any r independent active rows at a face have a nonzero r-by-r minor
of determinant +/-1. Adjoin the complementary original coordinate
rows to obtain an affine GL_(m+1)(Z) chart. Its r normal coordinates
are actual physical indices h, k, d-h or d-k. There is no fractional
lattice, root-grid multiplicity or unrecorded counting Jacobian.
At a nonsimple face the other active inequalities remain explicit.

### A finite unimodular simplex atlas of the physical polytope

Every physical facet has lattice width ONE on P. Its primitive
defining form takes only the values zero and one on the vertices,
by the preceding binary-vertex result. Every face inherits the same
property: a facet of a face is cut out by one of the original physical
inequalities, and its defining form takes both values on that face's
vertices. Their integer difference evaluates to one, so the restricted
form is primitive on the face lattice as well.

Fix an order on the finitely many vertices and form the pulling
triangulation. Inductively triangulate all opposite facets of a chosen
vertex, using the same order on every shared face, and cone their
simplexes to that vertex. This covers the polytope with disjoint
relative interiors and compatible intersections. The assertion is
elementary by following each ray from the chosen vertex to its first
opposite boundary face.

All resulting simplexes are unimodular. Dimension zero is the base.
At the inductive step the chosen vertex has primitive lattice height
one over the opposite facet. Appending its edge to a determinant-one
facet basis therefore gives determinant +/-1 in the face lattice.
Thus P has a finite unimodular triangulation depending only on the
fixed word. No imported triangulation theorem or N-dependent
refinement is needed for this statement.

For the ACTUAL source polytope dP, each cell is consequently

    u=d v_0+B n, n in d*Delta, B in GL_(m+1)(Z),

where Delta is the standard simplex and B is independent of N.
The cell d*Delta itself has N-dependent size; it is not asserted
to have lattice volume one. Its change of source coordinates has
counting Jacobian one. Shared cell faces must be assigned once by
a fixed half-open convention if their finite lattice sums are split.
This finite real simplex atlas supplies controlled integral charts.
It does not identify or glue their COMPLEX cotangent residue cycles.

## 3. The radial logarithmic coefficient never vanishes

Let F be a nonempty proper face of P. Let H(F) list its active head
occurrences h_i=0 or1, and J(F) its active transfers k_j=0 or1.
The row vector governing the radial logarithmic term is

    q_F=sum_(i in H(F)) c_i grad h_i
                           -sum_(j in J(F)) grad k_j. (5)

The SAME sign applies at the lower and upper endpoint. Indeed, for
I(s)=integral_0^s log|2sin(pi u)| du, either real endpoint a=0,1
satisfies

    I(a+delta v)-I(a)=delta v log delta+O_v(delta)    (6)

on a continuously marked side. At the upper endpoint this also
follows from I(1-s)=-I(s). Full-function branch changes add recorded
integer linear terms; along a real normal displacement they do not
change the real logarithmic coefficient.

If J(F) is nonempty, choose j in it. Every head contribution to the
k_j coefficient of (5) is even, while its own transfer contributes
-1 and other transfers contribute zero. That coefficient is ODD.
Hence q_F!=0, regardless of simultaneous head collisions.

If J(F) is empty, all transfers are positive and below one on the
relative interior of F. A head h_i=0 must be a strict local minimum
along the component: its preceding increment is negative and its
following increment is positive. Otherwise a neighboring head would
be negative. Thus c_i=-2. Similarly a head h_i=1 is a strict local
maximum, so c_i=+2. Writing a_f for the active INWARD inequalities
h_i>=0 or 1-h_i>=0, we obtain

    q_F=-2 sum_f grad a_f.                         (7)

This cannot vanish. At a real relative-interior point x of F, all
a_f(x)=0; at a strict interior point x_* all a_f(x_*)>0. If their
gradient sum vanished, their sum would be constant and these two
values would coincide, a contradiction. This completes the proof
for EVERY proper face.

## 4. An outward direction with strict action decrease

For every F there is a fixed integer vector v_F and an active inward
inequality a_g such that

    a_g'(v_F)<0, q_F(v_F)>0,
    a_f'(v_F)!=0 for every active a_f.              (8)

For a facet the verification is explicit. A transfer k_j=0 facet
has q_F=-grad k_j. A k_j=1 constraint cannot be a facet: its
crossing forces physical head endpoints as independent equalities.
A head endpoint facet has q_F a negative positive-integer multiple
of its inward normal, by the local-minimum/maximum argument above.
Choose v outward, then perturb within its open halfspace if needed.

For codimension at least two, active inward normals span a space of
dimension at least two. Since q_F!=0, at least one normal a_g' is
not a positive multiple of q_F. There is then a real vector v with
a_g'(v)<0 and q_F(v)>0: these two strict halfspaces are incompatible
only for positive proportional normals. Avoid the finitely many
other normal hyperplanes, choose v rational, and clear denominators.
This gives (8) with integer v_F. All its constants depend only on
the fixed word and face, not on N or the tangential source values.

The direction need not make EVERY active inequality negative.
It remains outside the physical polytope because a_g<0. This is
why it also handles the all-zero corner, where shifting every
transfer outward negatively was uphill. At that corner one can
instead increase all transfers and decrease t sufficiently: all
heads move outside while q_F(v_F)>0. The COMPLETE product descends.

## 5. Uniform local phase estimate

Write the original scalar density as exp(N S) times its retained
amplitude, with the gathered factorials (4), and include any fixed
integer character sector from the actual cardinal/norm packets.
Let y_F be a point of the COMPLEXIFIED affine face: its active
indices equal 0 or1 exactly. Assume its inactive factors are regular
on the chosen marked tube. If G is the nonsingular part, suppose

    |grad G|<=C_0+C_1 epsilon log N.                (9)

The original shrinking-strip hypotheses supply (9); it is not a
bound on an unknown knot scalar. Choose delta=N^(-alpha), with
alpha>C_1 epsilon/q_F(v_F), allowing fixed norm-comparison constants.
The finitely many endpoint expansions (6) give

    Re S(y_F+delta v_F)-Re S_face(y_F)
       =delta log delta q_F(v_F)
                       +O_word(delta(1+epsilon log N))
       <=-c_F delta log N                           (10)

for all sufficiently large N. Choose alpha<1 and epsilon small.
The estimate is uniform on the regular tangential tube. Any fixed
integer mark has exactly constant modulus under this real displacement.
The active full-function resets change only those marks, so (10)
holds for all retained outgoing marked sectors. A pole in a separated
cardinal coefficient is not crossed independently of its full packet.

Small complex offsets of size delta'=N^(-beta), beta>alpha, change
the active-factor height by O(delta'|log delta'|), and the regular
height by O(delta'(1+epsilon log N)). They therefore do not remove
the far-edge decrease in (10). The shift of the quantum upper
endpoint d/N from1 costs O(log N/N), also smaller than the stated
drop. This is a local inner-to-outer normal estimate, not a monotone
flow assertion at every intermediate point of every small corner.

There are finitely many physical faces for a fixed word. Thus the
vectors, charts and admissible exponents can be chosen uniformly
over this entire finite list. At every vertex Re S_face=0: all
factorial arguments are 0 or1 and all retained polynomial phases
are pure imaginary on the real vertex. This agrees with the
independent subexponential all-transfer-endpoint operator bound.

## 6. Exact source scope and what remains

The cardinal-completed scalar is holomorphic in any prescribed fixed
O(N) box and has the exact original values at every valid integer
state, zero at every invalid one. Therefore its COMPLETE finite
residue sum can be represented in any affine unimodular chart from
Section 2. This is equality of residue functionals on holomorphic
scalars, with orientation retained. It is not a pointwise identity
between the different products of cotangents.

Consequently (8)--(10) identify a descending normal for every physical
face without assuming independent output positions or individual-atom
zero sides. They do not by themselves glue those charts into one
global deformed cycle. Partial chart changes retain diagonal cotangent
walls and side currents; a sweep through valid physical integers
retains their original residues. Nonphysical integer poles of separated
window modes must still cancel in their complete packet.

The remaining global claim must control this entire assembled source,
the cumulative transport mass and any escaping tangential charts.
Neither geometric survival nor a sharp whole-source volume upper
bound follows merely from nonvanishing q_F or from the existence
of the local vectors (8). These are constructive boundary action
estimates for the proposed boundary-to-interior transport, with
the exact source gluing still required.

## 7. A uniform quantum bound for the complete active cluster

The preceding real radial estimate has an exact finite-N counterpart.
It concerns the WHOLE cardinal-completed active factorial packet,
not separate polar Gamma or cardinal modes. All constants below may
depend on the fixed face, word, chosen integer direction and bounded
normal-height set, but not on N or the bulk amplitude.

### 7.1 A primitive outward direction with a literal source coordinate

One can strengthen (8) to choose

    grad a_g(v_F)=-1, q=q_F(v_F)>0,
    grad a_f(v_F)!=0 for every active a_f.         (11)

Every physical row a_g is primitive. If q_F is a negative multiple
of grad a_g, any integer solution of grad a_g(v)=-1 has positive
q_F(v); perturb it within the integer kernel to avoid the finitely
many other normal hyperplanes. Otherwise q_F is nonzero on its
integer kernel. Start with
one integer solution v_0 and add Lw, where w lies in that kernel,
q_F(w)>0, and avoids all active normal kernels except those forced
by proportionality to a_g. Such w exists by an open rational
halfspace argument; choose L sufficiently large and avoid the
finitely many exceptional values. This proves (11). The vector v_F
is automatically primitive, since its pairing with an integer row
is -1.

Use a_g as the FIRST affine integer source coordinate and complete
the others by an integer basis dual to v_F and ker a_g. The resulting
chart has determinant +/-1. With its tangent coordinates fixed,
the outward normal path is

    u=u_F+z v_F, a_g(u)=-z EXACTLY.                (12)

This selected zero offset is important. Other active factorial
arguments may have bounded complex offsets nu_f in a small face
tube, but the selected a_g has zero offset for every value of those
tangent coordinates. Every positive integer z in (12) is therefore
an INVALID physical state through this selected head or transfer.
The complete cardinal factor for that physical form vanishes there,
even when the remaining tangent coordinates are complex. This is
stronger than an assertion just on integer tangent slices.

Re-present the COMPLETE residue source in this affine integer chart
before taking the normal homotopy. Its first factor is
pi*cot(pi*a_g) da_g=pi*cot(pi*z) dz with induced orientation. Moving
the original outward edge from Re z=1/2 to Re z=M+1/2 crosses only
these zero-residue nonphysical integers. Both finite-height horizontal
connectors remain. This source statement uses the full holomorphic
completion, not a pointwise substitution of one cotangent product
for another. No valid-state cotangent residue is swept away.

### 7.2 All upper normalizers and window reflections are exact

Write an active argument at its lower endpoint as s, and one at its
upper endpoint as d+s. Its exponent c is one of the actual head
exponents -2,0,2 or a transfer exponent -1. The exact identities are

    Fhat(d+s)/N=exp[i*pi*s*(s+d)/N]/Fhat(-s),
    w_N^+(d+s)=w_N^-(-s),
    w_N^-(d+s)=w_N^+(-s).                        (13)

The first identity retains the complete reflected chirp and the
factor N=F_d. The other two follow from
S_N(d-s)=-S_N(s) in the literal cardinal sum. Thus the complete
active packet, including its windows, becomes

    N^(C_upper) exp(P_upper(z))
       product_i [Fhat(s_i)^(r_i)
                    w_N^+(s_i)^(p_i^+) w_N^-(s_i)^(p_i^-)],
    s_i=nu_i+beta_i z, beta_i integer nonzero,
    C_upper=sum_(active upper occurrences) c,
    sum_i r_i beta_i=q_F(v_F)=q>0.               (14)

Here lower occurrences have r_i=c and their original slope;
upper occurrences have r_i=-c and the reflected slope. P_upper is
the explicit sum of the chirps in (13). The powers are those of the
original scalar cardinal completion, with orientations exchanged
under (13). They are never reset to one. Total window powers are
strictly larger than every positive Gamma pole order; in particular
p_i^++p_i^->max(r_i,0). An active physical window with r_i=0 is kept
as well. It may be precisely the selected window in (12).

The integer power N^(C_upper) is the ACTUAL upper-endpoint factor,
not a tame normalization chosen by the proof. It may be negative.
It will remain explicit in the bound below. On bounded normal
imaginary height the chirp exp(P_upper) has at most exp(O(M+1))
modulus for Re z of size M.

### 7.3 Uniform regularized Gamma estimate through all collisions

Put h=2*pi*i/N and use the fixed branch Log(-h)=log(2*pi/N)-pi*i/2.
The actual Barnes product gives EXACTLY

    Fhat(s)=(-h)^s Gamma(s+1) A_N(s),
    A_N(s)=exp[i*pi*s*(s+1)/(2N)]
       product_(k>=1) Gamma(Nk+s+1)
                    /[Gamma(Nk-s)(Nk)^(2s+1)].    (15)

For |s|<=delta_0*N with any fixed sufficiently small delta_0, A_N
is holomorphic and zero-free, including at the negative integers.
The common Gamma divisor in (15) has been canceled BEFORE evaluating
there. Uniformly in this disk,

    |A_N(s)|+|A_N(s)^(-1)|
                   <=2 exp[C(|s|+1)^2/N].        (16)

For completeness, apply the elementary uniform Stirling expansion
to t+s+1 and t-s, t=Nk. Its 1/t term cancels exactly:

    LogGamma(t+s+1)-LogGamma(t-s)-(2s+1)log t
                     =O((|s|+1)^3/t^2).

Both arguments have positive real part, uniformly away from zero.
The error sums absolutely over k. Its total is
O((|s|+1)^3/N^2), bounded by C(|s|+1)^2/N on the disk. The explicit
quadratic chirp in (15) has the same latter bound. This proves (16)
without a periodic ambiguity or a choice of a replacement factorial.

Let Re z=M+theta with theta in a fixed bounded interval, |Im z|<=T,
and let all nu_i range over a fixed bounded complex set. For M
sufficiently large the sign of Re s_i is the sign of beta_i.
For negative Re s_i use the exact reflection

    Gamma(s_i+1)=-pi/[sin(pi*s_i) Gamma(-s_i)].

The COMPLETE window is

    w_N^+/- (s)=exp(+/-pi*i*s) sin(pi*s) S_N(s)/pi.

On Re s<=-1/2, |S_N(s)|<=C log(N+1). The retained window powers
cancel every negative-integer Gamma pole in the same product, and
leave only nonnegative powers of sin(pi*s). These are uniformly
bounded on the stated fixed-height strip. For positive Re s_i,
the original Gamma is regular and the whole-plane cardinal bound
is polynomial in N on that strip. Stirling for the remaining Gamma
or reciprocal Gamma factors now gives, for the complete product,

    log |active packet/N^(C_upper)|
       <=-q M log[N/(M+1)]
                    +C M+C M^2/N+C log N.         (17)

Offsets nu_i contribute only O(log N), since they are bounded;
all constants beta_i are fixed. For bounded M the same assertion,
with enlarged C, follows from (15) after the already-canceled
Gamma poles. Thus (17) is uniform through dependent and coincident
active collisions. No estimate is made on individual polar modes.

### 7.4 Coupling to the actual bulk and the quantitative collar

Let G_N(u_F) contain all INACTIVE factorials and the full original
Cartan, conversion, pivot, kappa and external chi_N/N factors.
Do not divide by a completed face amplitude, which may vanish.
The explicitly retained N^(C_upper) stays outside G_N.
Assume the inactive marked tube gives the normal allowance

    |G_N(u_F+zv_F)|
       <=exp(CM) N^(C_1*epsilon*M+C_2) |G_N(u_F)|. (18)

This is the quantitative form of (9). On a regular marked bulk
branch with uniform factorial-symbol control, inactive clocks and
their complements bounded above and below by N^(+/-epsilon), and
a displacement smaller than their singularity distance give the
stated O(1+epsilon log N) leading logarithmic derivative. In a
continued chart the EXACT allowance (18) additionally retains and
controls its central norm factors and full symbol; it does not
follow merely from bounds on B and 1-B if an outside-band integer
factorial divisor is approached. Finite bulk-window modes keep
their actual integer-marked exponential in G_N; the HEAD/active
windows remain whole as in (14). Their bounded-height polynomial
factors are already included in (17).

Combining the exact active bound and (18) gives the following bound
for each retained bulk-window mode, with the active packet WHOLE:

    |Atilde_N(u_F+zv_F)|
       <=|N^(C_upper) G_N(u_F)| N^C
          exp[CM+CM^2/N]
          N^(C_1*epsilon*M) [(M+1)/N]^(qM).      (19)

For a general nonreal tangent chamber the COMPLETE scalar is the
fixed finite sum of these modes. Its bound uses the SUM of the
absolute reference amplitudes on the right of (19), not the absolute
value of their potentially canceling sum. On a fixed-height joint
contour the inactive windows themselves cost only a polynomial;
there the unwindowed original bulk G_N suffices directly.

Choose M=floor(N^(1-alpha)), with

    max(epsilon,C_1*epsilon/q)<alpha<1.

Then the far normal edge has the strict bound

    |Atilde_N|<=|N^(C_upper)G_N(u_F)|
       exp[-(q*alpha-C_1*epsilon+o(1))M log N].   (20)

Throughout that collar the additional normal cost is exp(o(N));
finite-height connector lengths and cotangent bounds add only
polynomial factors. Estimate (20) compares to the retained bulk
source itself, not to an assumed volume bound for it. Arbitrarily
fixed bounded normal jets obey the same kind of bound on slightly
smaller contours by Cauchy's formula after pole cancellation.

One may allow offset size L=o(M), at the additional cost
exp[O((L+1)log N)]: the same regularized Gamma calculation and
bounded-height estimate use |Im s|=O(L+1). In particular the small
thickenings in Section 5 with beta>alpha do not remove (20).
This extension concerns a single common radial normal and its
specified small offsets, not arbitrary nested scales.

The actual conclusion is a uniform active-cluster OUTWARD quantum
collar for every physical face, whenever the inactive bulk allowance
is available. The original residues and all upper normalizers are
retained, and the selected outside cotangent integers have exactly
zero residue. It does not glue different face collars, prove a
global mass bound, or classify every nested tangential escape.

Section 7 supplies the finite-N whole-packet estimate; no scalar noncancellation or full volume theorem is inferred.

[Independent face audit](../experiments/audit_actual_physical_face_outward_action.py):
790 proper physical faces of seven original signed words, 4877 exact
maximal minors, primitive outward vectors and 28 radial phase checks.
The all-word conclusions use the proofs above, not this finite census.

The supplementary complex checks in
[the two-neighbor audit](../experiments/audit_actual_regular_head_face_cot_filling.py)
also pass nine normalized Gamma-factor checks, eighteen exact upper
window reflections, and three mixed-direction pole cancellations.
The latter use a cluster with q=2*(-1)+(-1)*(-3)=1, so an individual
factor goes toward a pole while the COMPLETE product has the stated
descending logarithmic coefficient. These are checks of exact local
identities, not substitutes for the uniform proof or global source
gluing.
