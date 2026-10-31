# Actual Rogers blocks and the full marked source at arbitrary bridge number

28 October 2026. This note connects the newly proved finite Rogers
transform to the original two-head fusion kernel and folds all the
actual plat turns through that kernel. The result is an exact recursion
for any admissible colored `2k`-plat, with one explicit marked output row,
all other outputs fixed corners, and no restriction on bridge number.
Every total integer degree is retained. This is a root-family identity
in the full meridian, not a moving-q extension or a volume theorem.

The [all-strand regular fusion theorem](actual_borel_regular_fusion_and_divided_cap_period.md),
[Euler word completion](actual_crossing_euler_completion_and_weight_source.md),
and [regular canonical fusion graph](fusion_canonical_chart_and_retained_source_wall.md)
already give much of the underlying matrix transport. The new assertions
here are the exact Rogers realization on every actual degree block, the
ordinary-turn corner formulas, the original marked-cap row and its
degree-restricted closed form, their simultaneous arbitrary-plat
recursion, and the exact final Ward-corner reduction. They do not turn a basis-change loop into a positive
tetrahedron or a source-preserving geometric 2↔3 theorem.

## 1. Every actual degree block is q-Pascal

Fix a primitive Nth root Q, `d=N-1`, and `F_a=(Q;Q)_a` for
`0<=a<N`. The original balanced heads have raising coefficients
`1-Q^(a+1)` and clock `x Q^-a`. For two heads the actual fusion is

    C_x(u,v; a,b) = x^(u-a) F_a F_v / [F_(a-u) F_b],
    0<=u<=a, v=a+b-u<N,                                  (1)

and zero otherwise. In particular it preserves the TOTAL INTEGER
degree, not only its value modulo N. Its diagonal entries are `F_a`,
so it is invertible over the whole Laurent field in x.

For total degree s put

    I_s = {max(0,s-d),...,min(d,s)}, 0<=s<=2d.

Using a for the first input and u for the first output, the block is

    C_(x,s)(u,a)
       = [x^u F_u F_(s-u)] {a choose u}_Q
                                      [x^-a/F_(s-a)].     (2)

The binomial is zero when u>a. Thus EVERY degree block is an exact
row/column gauge of the corresponding contiguous principal q-Pascal
block. The inverse Pascal block is explicit:

    P_s^-1(u,a)=(-1)^(a-u)Q^((a-u)(a-u-1)/2)
                                      {a choose u}_Q.    (3)

To prove (3), multiply the two triangular matrices and use
`{a choose v}{v choose u}={a choose u}{a-u choose v-u}`.
The remaining sum is `(1;Q)_(a-u)`, which is zero unless a=u.
The same proof applies to each I_s because the intermediate indices
between u and a all belong to that interval. No factorial of index N
is divided out.

In particular the ACTUAL inverse block, with row u and column a, is

    C_(x,s)^-1(u,a)
       =x^(u-a)(-1)^(a-u)Q^((a-u)(a-u-1)/2)
          F_(s-u)/[F_u F_(a-u) F_(s-a)]  for u<=a,

and zero otherwise. This follows by reversing the two diagonal
gauges in (2), and specifies every inverse kernel used below.

On the cap block s=d, let

    R(k,n)=Q^(n-k+1){n choose k}_Q, 0<=k,n<N.

This is the matrix in the arbitrary-x Rogers convolution proved in
[the finite whole-source transform](five_two_cyclotomic_transform_proof.md).
It is literally an actual fusion block with the following gauges:

    R(k,n) = L_k C_(x,d)(k,n) B_n,
    L_k=Q^(1-k)x^-k/[F_k F_(d-k)],
    B_n=Q^n x^n F_(d-n).                                 (4)

Thus that finite transform is available as a change of actual fusion
coordinates; it is not merely an unrelated operator on Newton
coefficients. Equation (4), however, realizes one degree block, not
an invariant subspace for an arbitrary plat word.

## 2. Actual ordinary turns become corners

Write `xvee=x^-1 Q^-1` for the actual dual color. All formulas below
use the original balanced turns from
[the bridge source calculation](quantum_bridge_cap_source.md), including
their factors N and 1/N and the original pivot.

For a physical pair `(V(x),V(xvee))`,

    coev_L(x) = C_x |d,0>,
    ev_R(x) C_x = (1/N)<0,d|.                            (5)

For the opposite order `(V(xvee),V(x))`,

    coev_R(x) = C_(xvee) |d,0>,
    ev_L(x) C_(xvee) = (1/N)<0,d|.                       (6)

For the cups, (1) at `(a,b)=(d,0)` gives the coefficient
`N x^(u-d)`. This is exactly the original left cup. With the first
color xvee it is exactly the original right cup, because
`(xvee)^(u-d)=x^(d-u)Q^(d-u)`.

For completeness, a supported physical row
`ell(u,d-u)=kappa lambda^u` has

    (ell C_x)(a,d-a)
      =kappa N x^-a (Q lambda x;Q)_a/F_(d-a).            (7)

Indeed use

    F_u F_(d-u)=N(-1)^u Q^(u(u+1)/2)

in (1), and then the finite q-binomial theorem. The actual right cap
has `kappa=1/N`, `lambda=xvee`, so `Q lambda x=1`. All a>0
entries vanish and the a=0 entry is 1/N. This proves (5), and
the same argument proves (6). The vanished Pochhammer is the WHOLE
polynomial factor, rather than a numerical value selected after
specialization.

## 3. The original marked cap is an explicit nonconstant row

The actual reduced source is represented by the marked right cap

    ev_R^D(u,v)=x^v/N^2,                                 (8)

with no restriction on u+v. This is the original averaged source;
it is not an ordinary intertwining cap. Pulling (8) through (1) gives
the following exact row on the ENTIRE relative two-head space:

    m_x(a,b) := (ev_R^D C_x)(a,b)
       = x^b F_a/N^2
           sum_(h=0)^min(a,d-b) {b+h choose b}_Q.         (9)

To check (9), substitute v=a+b-u in (8). The x powers become
`x^(v+u-a)=x^b`. Set `h=a-u` in the remaining factorial quotient;
then `F_(b+h)/(F_h F_b)={b+h choose b}`. This calculation includes
every source wall and every total-degree block.

There is a useful further simplification in a whole plat. All k cups
start in total degree kd, every actual crossing preserves that integer
degree, and each of the k-1 ordinary output caps in (5)--(6) forces
degree d. Therefore the marked pair is automatically in degree d.
There (9) is the closed row

    mu_x(r) := m_x(r,d-r)
      = x^(d-r)(-1)^r Q^(-r(r+1)/2) F_r^2/N^2,
      0<=r<N.                                           (10)

For a direct proof of its inner sum, reflect the Gaussian:

    {d-r+h choose h}_Q
       =(-1)^h Q^(-rh+h(h-1)/2){r choose h}_Q.

Summing h=0,...,r gives
`(Q^-r;Q)_r=(-1)^r Q^(-r(r+1)/2)F_r`, yielding (10).
In particular every mu_x(r) is nonzero for x!=0, and

    mu_x(r+1)/mu_x(r)
       = -x^-1 Q^(-r-1)(1-Q^(r+1))^2.                  (11)

No normal direction in x, and hence no meridian derivative at fixed Q,
has been discarded. For example `x d/dx mu_x(r)=(d-r)mu_x(r)`.
At the canonical unit root `Q=exp(2pi i/N)`,

    mu_x(r)=x^(d-r)/N^2
                  product_(j=1)^r [2 sin(pi j/N)]^2.      (12)

Put `w_N(r)=|F_r|^2/N^2>0`. There is an explicit coherent gauge of
the WORD implementing the positive boundary row, rather than merely
an observation about its coefficients. Choose the same designated
pair at every horizontal slice and let

    G_boldx |a_1,b_1;...;a_k,b_k>
                   = x_*^(b_*) |a_1,b_1;...;a_k,b_k>.

Here x_* is that pair's current first color, updated after crossings.
For every letter replace (14) below by

    B_i^(epsilon,G)=G_boldx' B_i^epsilon G_boldx^-1.

The input cup corners have b_*=0, so G_initial fixes them. Therefore
the final scalar can use weights w_N(r) and the entries of
`B_beta^G=G_final B_beta G_initial^-1` exactly. All intermediate
gauges cancel. On |x_j|=1 this is a unitary diagonal change at every
slice; for general nonzero x_j it remains an invertible Laurent
change retaining the whole meridian. The crossing kernels remain
complex, so positivity of this actual SOURCE row is not a
no-cancellation theorem for the whole contraction.

The empty one-bridge word has r=d as its sole input/output entry.
The full identity `(-1)^d Q^(d(d+1)/2)=1` gives mu_x(d)=1.
Hence (10) reproduces the original unknot normalization at both
parities without replacing the marked cap by an ordinary cap.

## 4. Strict actual crossing cores, including both signs and colors

Let `J_+|a>=|a+1>` and `J_-|a>=|a-1>`, with their actual top and
bottom arrows zero. Put `X_+=J_+ tensor J_-`; this preserves the
integer total degree and has `X_+^N=0`. Set

    u_N(t)=sum_(h=0)^d t^h/F_h,
    v_N(t)=sum_(h=0)^d (-1)^h Q^(h(h-1)/2)t^h/F_h,
    D_(x,y)|a,b>=(-1)^b Q^(b(b-1)/2)(xy)^-b |a,b>.

Then `u_N(X)v_N(X)=I` for every nilpotent X of order at most N.
The original checked crossings satisfy

    R_+^(x,y) = kappa_(x,y) C_y
                      D_(x,y) u_N(x^-1 X_+) C_x^-1,
    R_-^(x,y) = kappa_(y,x)^-1 C_y
                      v_N(y^-1 X_+) D_(x,y)^-1 C_x^-1.   (13)

Here every common Cartan scalar kappa is the original unrolled one,
or its prescribed external Hom-line factor; it is not reset to one.
The negative formula is the inverse of the positive formula with
input colors reversed. Formula (13) is STRICT for these noncyclic
head shifts. It differs from extending the coefficient algebra by
cyclic right multiplication, whose positive-degree-N completion is
only source-equivalent on the closed-braid algebra.

One proof of (13) is to multiply its triangular kernels and use the
finite q-binomial theorem. Equivalently, the already checked actual
right coefficient is

    kappa sum_(h+b<N)
       (-1)^b Q^(b(b-1)/2)x^-h(xy)^-b f^h e_b/F_h.

Its degree-preserving action on a relative input `(a,b)` has output
`(a+h,b-h)`, coefficient `x^-h/F_h` followed by the displayed
Gaussian at b-h. These are precisely `D u_N(x^-1 X_+)`.
The omitted cyclic paths raise physical integer degree by N; the
literal actual crossing contains exactly the degree-preserving
part. This proves (13) on every total-degree block, including
s>=N and both truncated endpoints. Taking the inverse proves the
negative formula with its stated operator order.

## 5. An exact recursion for every admissible 2k-plat

At a horizontal slice with colors `bold x=(x_1,...,x_(2k))`, define

    C_boldx = C_(x_1) tensor C_(x_3) tensor ... tensor C_(x_(2k-1)).

This is the actual pair-fusion frame. At a crossing i let boldx'
be the color order after swapping i and i+1, and set

    B_i^epsilon(boldx)
       = C_boldx'^-1 R_i^epsilon(boldx) C_boldx.          (14)

All entries of C and C^-1 are explicit in (1)--(3); all entries of
R are explicit in (13). Equation (14) is therefore a fixed finite
convolution rule, not an unspecified intertwiner.

For a crossing within one fused pair, (14) is exactly the triangular
Euler/Gaussian core in (13). A crossing between consecutive pairs
acts on ONLY four relative heads. If their current physical colors
are `(x,y,z,w)`, its rule is

    B_middle^epsilon
      = (C_x^-1 tensor C_y^-1)
           (I tensor R_epsilon^(y,z) tensor I)
                                      (C_x tensor C_z). (15)

Thus it consists of a fixed number of the actual Pascal, inverse
Pascal, Euler and Gaussian factors, independent of N and of k.
It retains the whole set of total-degree channels I_s. Other pairs
are unchanged. No source-dependent adjustment is introduced at an
interior crossing.

For any word beta update colors after EACH letter and iterate (14).
The frames at consecutive slices cancel exactly, giving

    B_beta=C_final^-1 R_beta C_initial.                  (16)

In particular these kernels satisfy every colored braid relation
EXACTLY, with the original scalar lines retained: both words in
such a relation have the same boundary frames in (16). This is
stronger than claiming braid relations modulo the completion's
positive-degree error ideal. The actual noncyclic Euler cores and
all the degree blocks in (2) are what make the present statement
strict. Transporting an extra coupon means conjugating that coupon
by its slice frame as well; it does not mean leaving its old
relative matrix in place.

At every cup the initial state is `|d,0>`. At each ordinary cap
the final row is `(1/N)<0,d|`. Designate one final pair with first
color x_* for the original marked right cap; by choosing the
standard orientation of that marked pair, (8) applies. Let
`e_in=|d,0> tensor ... tensor |d,0>` and let `e_out(r)` put
`(r,d-r)` at the marked pair and `(0,d)` at all other pairs.
The original reduced scalar is exactly

    P_(beta,N) = chi_beta N^(-(k-1))
            sum_(r=0)^d mu_(x_*)(r)
                              <e_out(r)|B_beta|e_in>.    (17)

The factor chi_beta retains the original common Cartan and framing
lines if they were recorded externally rather than in R. Any
original peripheral modified-dimension germ multiplies both sides
unchanged. There are k cups, k-1 ordinary caps, and exactly ONE
marked cap, as in the original reduced closure. An ordinary cap
has not been placed at the marked pair.

The proof of (17) is (5)--(10) together with (16). It holds for
arbitrary bridge number, arbitrary signed word with admissible
output pairing, and the whole original meridian family. Reversing
an ordinary pair uses (6); no further scalar is generated. Its
full moments and meridian jets follow by differentiating the
same Laurent identities at fixed Q. Moving-q normal jets are
not asserted. Explicitly, the same truncated matrices obey
`C_(q x)(u,v;a,b)=q^(u-a) C_x(u,v;a,b)`. Thus meridian half-step
transport is an exact frame change on the fixed-root family; its
dual color changes by q^-1. None of the whole factors `1-x^N` or
`1+x^N` in the original cyclic boundary descriptions has been
inverted to obtain this recursion.

### The zero-current quotient is one corner, with no genericity hypothesis

For actual plat words without extra nonintertwining coupons, the
source can be reduced further. Contract the k-1 ordinary final caps
and leave the designated pair open. The resulting physical two-head
vector v is invariant under the actual coproduct, because the input
cups, crossings and the contracted ordinary caps are actual Hopf
intertwiners. In particular,

    F_total v=0,       K_total v=v.                      (18)

On the remaining ordered dual pair `(x,xvee)`, the literal actual
fusion identities are

    C_x^-1 F_total C_x=S_a,
    C_x^-1 K_total C_x|a,b>=Q^(-1-a-b)|a,b>,

where `S_a|a,b>=|a+1,b>` for a<d and is zero for a=d.
The first identity follows from the definition
`C_x|a,b>=F_total^a(|0> tensor |b>)`, including its top endpoint;
`F_total^N=0` is the actual root coproduct identity. Therefore

    ker S_a intersect ker(Q^(-1-a-b)-1)
                         = span{|d,0>}.                 (19)

Indeed the first kernel has a=d. The second equation then becomes
Q^-b=1, which forces b=0 in the actual head range. This uses neither
Schur's lemma nor irreducibility of the color module. It holds on
the whole meridian family, including reducibility divisors.

Consequently the amplitudes in (17) satisfy the exact Ward zeros

    <e_out(r)|B_beta|e_in>=0  for 0<=r<d.                (20)

There is no sum over hidden intermediate states in (20): the other
output pairs are already fixed to their ordinary cap corners. Since
mu_x(d)=1, the original scalar is the SINGLE original fused corner

    P_(beta,N)=chi_beta N^(-(k-1))
                         <e_out(d)|B_beta|e_in>.         (21)

The diagonal source gauge above also fixes e_out(d), because its
marked b coordinate is zero. Thus (21) is unaffected by that gauge.
The original marker is still necessary: an ordinary cap evaluates
the remaining invariant cup to zero, whereas the marker evaluates
it to one. Equations (19)--(21) describe the quotient by the actual
zero-current equations; they do not authorize replacing a marker
in a network containing nonintertwining current coupons. In that
more general network the full row (9), not (21), is required.

Equation (21) removes the final source-row cancellation problem at
the exact finite level. It does not say that the remaining corner
coefficient has positive summands, or that its geometric critical
coefficient cannot vanish in an asymptotic decomposition.

## 6. Why the cap-block Rogers rule alone cannot unwind every bridge

The degree-d block in (4) is NOT stable under crossings between
pairs. For every N>=2, take the actual cup-supported physical
input `(0,d,0,d)`. The zero-raising route of the positive middle
crossing takes its middle pair `(d,0)` to `(0,d)` with a nonzero
original coefficient. The resulting four-head state is

    (0,0,d,d),

whose pair degrees are 0 and 2d, rather than d and d. This is an
all-N literal coefficient statement; it uses no semiclassical
model. Later crossings can return these channels to degree d.
Discarding them does not define an exact iterative actual-plat
transform. Equations (14)--(17) supply the necessary larger rule.

This explains the distinction from the auxiliary Newton operators
in [the whole-source Newton note](whole_source_newton_transport.md):
one actual cap block realizes their Rogers matrix, but arbitrary
actual bridge transport requires the full physical channel system.

## 7. The source meets a fusion boundary, not the regular fusion torus

The [already proved regular fusion graph](fusion_canonical_chart_and_retained_source_wall.md)
has relative clocks A,J, physical clocks U,V, and momenta satisfying

    AJ=UV,  H=A/U,
    p_U=(1-A)p_A,
    p_V=(1-V)p_J/(1-J),
    H=1-(1-A)(1-J)/(x p_J/p_A).                          (22)

It is the actual Borel multiplication chart: in particular physical
total lowering has symbol `f_total=1/p_A`. The physical ordinary
bridge source has `f_total=0`, because its two Borel holonomies
multiply to I. Therefore it is outside this chart with finite
nonzero p_A. A regular interior symplectic map alone cannot move
the bridge source into a chosen positive geometric chart.

The same issue is visible directly in the original marked row,
without assigning a symbol to a finite nilpotent matrix. Fix total
degree d, a=r, and multiply the physical-u summand of (1) by (8).
Apart from a factor independent of u, this summand is
`F_(d-u)/F_(r-u)`. Its consecutive ratio is exactly

    [1-Q^(r-u)]/[1-Q^(d-u)].                            (23)

On an interior principal chart its limit is `(U-A)/(U-1)`.
The stationary equation setting this ratio to one forces A=1,
which is a divisor excluded from (22). Thus the exact nonzero
row (10) is a boundary/resonant transport calculation. It is not
an interior critical point of the regular fusion kernel with
the original marker inserted.

This is a specific constraint on the route to a positive quad
or Rivin chart. The source-boundary contribution must be included
in an actual compactified/relative chart transform; merely
composing the interior canonical graphs would lose it. The exact
row (9)--(10), its endpoint recurrence (11), and its exact Ward
corner (19)--(21) give that transform a specified source to carry.
They do not prove that its selected geometric coefficient is
nonzero after the full word contraction.

## 8. Verification and precise remaining comparison

The [independent original-matrix audit](../experiments/audit_actual_rogers_bridge_transport.py)
and [saved output](../experiments/actual_rogers_bridge_transport_results.json)
pass fourteen root/color families at N=2,...,8, all total-degree
Pascal blocks, the Rogers gauges, all four turn corners, the full
marked row, the degree-d simplification, and six mixed signed
crossings per family. Six whole pointed plats with two and three
bridges compare literal original contractions with (17), verify
all the zero-current channels (20), and verify the single corner
(21). Seven
all-parity leakage witnesses verify Section 6. These checks fix
conventions; the finite identities above prove the all-N formulas.

What is now explicit is the actual arbitrary-bridge kernel system
AND its marked source. A further source-preserving local transform
must turn these all-channel kernels into positive quad/2↔3 kernels
while carrying (9), its boundary (23), the Ward corner (19), and all central factors.
Neither a Pascal basis change nor the ordinary matrix pentagon
by itself performs that comparison. No broad hyperbolic growth or
geometric-cycle selection claim follows from (17) alone.
