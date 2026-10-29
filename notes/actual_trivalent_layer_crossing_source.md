# Every original crossing has a two-Newton, one-Rogers source layer

28 October 2026. The nine original scalar atoms admit a complete
partition into three disjoint trivalent sinks. Two sinks are the
PROVED Newton/Barnes template; the third is its actual all-U Rogers
polynomial. A positive Gaussian must first be combined with its
adjacent reciprocal factorial. A negative Gaussian stays ONCE and
is shared by its indicated Newton and Rogers variables.

This yields an exact one-internal-variable crossing kernel WITH its
original final nonnegative Hardy barrier, then a
simultaneous layer on any signed word and any bridge count. Each
Newton kernel can be replaced by its explicit two-full-Psi source
plus its retained central current. No positive-factorial edge,
Gaussian or original cap is used twice. The resulting current
branches are not classified as geometric degeneracies.

## 1. Fixed kernels and original normalization

Put Q=exp(2pi*i/N), d=N-1, F_a=(Q;Q)_a and

    p_a=(-1)^a Q^(a(a-1)/2)/F_a,
    U(t)=sum_(a=0)^d t^a/F_a,
    V(t)=sum_(a=0)^d p_a t^a,
    F(t)=sum_(a=0)^d F_a t^a.

These finite expressions are used to prove the source identity.
Their original full-Psi coefficient/relative-cycle realizations
may be reinserted exactly; they are not replaced by a new positive
invariant. Keep the original color x, not only its complete value.
Define

    B_N(u,v)=sum_(i+j<N) F_(i+j)/F_i *p_j u^i v^j,
    R_N(u,v)=sum_(i+j<N) F_(i+j)/(F_iF_j) u^i v^j.          (1)

B_N is the proved Newton polynomial. R_N is the actual truncated
Rogers--Szego generating kernel; it is not assumed to satisfy the
same beta theorem. All factorial normalization is already contained
in the coefficients in (1). No residual N^3 is to be inserted after
the three original factorials have been contracted this way.

Let the two input variables of one crossing be z_0,z_1 and its
outputs z_6,z_7. The four original internal head vertices after
Hardy-forest contraction are z_2,z_3,z_4,z_5. Write t=z_4.
The original external Cartan scalar kappa remains external. Write
Pi_+^(6) for the original nonnegative Hardy projection on the first
OUTPUT variable z_6. It is independent of N. This barrier is retained
in the physical crossing and in every separated branch below.

## 2. Literal nine-atom table, including the Gaussian placement

The original atom slots, in traversal order, are as follows. The
table displays the finite coefficient kernels; every F carries
its actual factorial support.

| Slot | Positive crossing | Negative crossing |
| --- | --- | --- |
| 0 | U(z_2/z_1) | same |
| 1 | V(x^(-1)z_2/z_0) | same |
| 2 | U(z_3/z_0) | same |
| 3 | F(t/z_2) | same |
| 4 | U(x^(-1)z_3/t) | V(g_- x^(-1)z_3/t) |
| 5 | U(g_+ z_5/t) | U(g_- z_5/t) |
| 6 | F(z_6/z_3) | same |
| 7 | U(x^(-1)z_5/z_6) | same |
| 8 | F(z_7/z_5) | same |

Here a Gaussian is still represented by its ORIGINAL moment

    g_s=-x^(-2s)exp(-s h/2)exp(sqrt(pi)(1+i s)xi),
    sqrt(N/(2pi))exp(-Nxi^2/2)d xi,
    h=2pi*i/N, s=+1 or -1.                                (2)

The original diagonal entries are

    d_a=(-1)^a x^(-2a)Q^(a(a-1)/2).

For R_+ the active Gaussian index is the slot-5 reciprocal
index h_5, hence its full exponent is g_+^(h_5). For R_-
the Gaussian precedes the central transfer; the index is
h_5+h_4, hence the two displayed g_- factors are the SAME
Gaussian variable. This is a literal gate-order calculation,
not two independently integrated Gaussians.

The four internal affine vertex equations are

    h_0+h_1+h_3=d,
    h_2+h_4+h_6=d,
    h_3+h_4+h_5=d,
    h_5+h_7+h_8=d.                                       (3)

The first, second and fourth are sinks. Their atomic stars
{0,1,3}, {2,4,6}, {5,7,8} are PAIRWISE DISJOINT and
partition ALL nine atoms. The third equation is at the
remaining source vertex t; its integration is retained.

The table follows either by coefficient conservation in
the strict original word or by weighted Hardy-forest residues.
At the Gaussian edge z_out=z_in/g_s, logarithmic residue
measure has no extra g_s Jacobian. This gives precisely the
two placements in the table. Its original caps are unchanged.

## 3. Positive crossing: absorb one COMPLETE Gaussian cell

In the positive word C D U_+ C^(-1), the Gaussian D is
adjacent to the reciprocal second-head factorial in C.
Their exact combined diagonal coefficient is

    d_a/F_a=p_a x^(-2a).                                 (4)

Thus the COMPLETE Gaussian-plus-slot-5 cell is exactly

    V(x^(-2)z_5/t).

It has no remaining Gaussian variable or extra scalar.
One first contracts that whole Gaussian cell, then uses
the Newton identity. It is not a pointwise deletion of
g_+ in an arbitrarily separated full-Psi sector.

Contract the three disjoint sinks in (3). The guaranteed
first star {0,1,3} gives B_N(t/z_1,x^(-1)t/z_0). The
last star {5,7,8}, after (4), gives
B_N(x^(-1)z_7/z_6,x^(-2)z_7/t). The middle star is
R_N(z_6/z_0,x^(-1)z_6/t). Consequently the ENTIRE
raw positive crossing kernel is

    Ktilde_+=kappa CT_t [
       B_N(t/z_1,x^(-1)t/z_0)
       R_N(z_6/z_0,x^(-1)z_6/t)
       B_N(x^(-1)z_7/z_6,x^(-2)z_7/t)].                   (5)

On the ORIGINAL finite input heads, the PHYSICAL finite-head
crossing is K_+=Pi_+^(6) Ktilde_+.
All upper support and second-output lower support are already
enforced by the three factors; only negative first-output tails
remain in the raw expression.

In particular the all-U middle star was not renamed Newton.
The original Gaussian is accounted for by the exact identity
(4), including its color x^(-2a) and linear root phase.

## 4. Negative crossing: one shared Gaussian, not two

For the negative crossing, stars {0,1,3} and {2,4,6} have
the original U,V,F types and give Newton kernels directly.
The last star is all-U and gives the Rogers polynomial.
The exact raw negative kernel is

    Ktilde_-=kappa^(-1)sqrt(N/(2pi))integral_R exp(-Nxi^2/2)
       CT_t [
       B_N(t/z_1,x^(-1)t/z_0)
       B_N(z_6/z_0,g_-x^(-1)z_6/t)
       R_N(g_-z_7/t,x^(-1)z_7/z_6)] dxi.                 (6)

On those same finite input heads, K_-=Pi_+^(6) Ktilde_-.
For example the raw kernels,
on input (0,0), have a nonzero output (-1,1) from h_7=1,
with coefficient kappa^(+/-1)x^(-1). The final original
Hardy barrier removes it. Thus (5)--(6) are not asserted
entrywise finite-head operators without that barrier.

The two appearances of g_- are linked by the SINGLE Gaussian
measure (2). Keeping only one or integrating each independently
changes the original phase. No remaining Rogers sink is declared
a Newton move without a further proved transformation.

One finite coefficient proof checks (5)--(6) directly. On an
input (a,b), put h_1=j, h_2=a-j, h_5=b+j-h_4 and output
(c,e)=(h_2+h_4-h_7,h_5+h_7). The first Newton coefficient is

    F_(b+j)/F_b *p_j x^(-j).

The second chosen Newton and the Rogers factor supply exactly
the remaining original F and reciprocal F coefficients. Their
Gaussian powers are h_5 for the positive crossing before (4),
and h_5+h_4 for the negative crossing. Illegal original indices
have zero coefficient. This proves the entire matrix equality,
not merely a scalar cap evaluation.

## 5. Simultaneous exact layer on an arbitrary original word

For m signed crossings, select the TWO Newton stars specified
in (5) or (6) at each crossing. They are disjoint inside each
crossing and occur at distinct internal sink vertices in the
original ordered word. Spectator/Hardy contractions cannot
merge one of these sinks with a later crossing: it has only
its three atomic incidences and its affine charge -d.
Thus there are exactly 2m independent Newton contractions,
one remaining Rogers polynomial and one remaining internal
t variable per crossing. Every F edge is used exactly once.

Perform the positive Gaussian contraction (4) before expanding
any new beta sectors. Retain one Gaussian per negative crossing.
Glue the output and input head variables with the SAME original
Hardy/source identifications and pair with the SAME original cups,
ordinary caps, full marked cap, and external peripheral/framing
line. Equations (5)--(6) then give the original whole period.
This is valid for any bridge count and the whole original
nonzero color x family at the fixed physical root.

At each chosen Newton sink use its exact original-source identity

    B_N(u,v)=S_N(u,v)+D_N(u,v)I_N(u,v),
    D_N=1-u^N+v^N,
    S_N=(N/phi_N)u^N Psi_+(h-Logu)Psi_+(Log(v/u))
                                      exp[-Log(v/u)Logu/h]. (7)

This is the [proved beta source](actual_trivalent_quantum_beta_source.md)
with the [exact Fermat normalizer](exact_balanced_source_normalizer_fermat.md),
not bare replacement of a factorial coefficient by its symbol.
Multilinearity gives at most 2^(2m)=4^m source branches, with
all Rogers kernels, remaining Gaussians and original caps
retained. Expanding each D into its three monomials would
give at most 4^(2m) terms; keeping it grouped is preferable.
The number depends on the word, not N.

The branches live on specified logarithmic/relative source
charts. They need not be separately single-valued scalar
periods or independently absolutely integrable on an
uncontinued original torus. Start on a common regular marked
chart, use (7), and continue with its exact beta currents.
Equivalently use common finite Gaussian cutoffs and matched
pole indentations BEFORE summing the branches. Their sum is
the original finite polynomial integrand, so its limiting
period is fixed by the original absolute convergence theorem.
No independent finite part is chosen for one branch alone.
The joint deck/source gluing is part of the retained source
extension; deleting current sectors would destroy it.

Thus this is an exact finite-branch whole-source NORMAL FORM.
It is not a proof of termwise global growth estimates or
of dominance of the all-S branch.

There is an optional whole-source reduction of the last Hardy
barrier, but it has a different scope. The COMPLETE raw B/R
kernel has only nonnegative incoming index demands, so it
annihilates any negative input head. Its only unphysical output
is a negative first head. The next crossing touching that head
annihilates it; if no crossing touches it again, the original
finite final source annihilates it. Therefore the raw complete
crossings give the same whole-word source after summing their
complete finite kernels. This no-healing argument must NOT be
applied separately to the meromorphic S/I branches. The displayed
branch normal form retains Pi_+^(6), unless that full-word
source reduction has first been performed before splitting.

## 6. What the actual central monomials do

For the guaranteed first star the literal central function is

    A=u^N-v^N=t^N[z_1^(-N)-x^(-N)z_0^(-N)].                (8)

It is a free scalar boundary function, not identically zero
or one. At the other positive star it is

    A_F=x^(-N)z_7^N/z_6^N-x^(-2N)z_7^N/t^N,

and at the negative central star it is

    A_C=z_6^N/z_0^N-g_-^N x^(-N)z_6^N/t^N.                (9)

The original peripheral x^N and the Gaussian norm g_-^N
remain. They cannot be evaluated at an ideal point before
normal source operations. A separately chosen cyclic
boundary-character extension with z_1^N=x^N z_0^N would
make (8) zero, but that is not a specialization theorem for
the original finite-head scalar source.

There IS an exact finite-input support statement. The original
inverse fusion kernel after the first contraction is

    U(z_3/z_0)B_N(t/z_1,x^(-1)t/z_0).                     (10)

Its monomial indexed by i,j,r has incoming exponents
(r+j,i) and outgoing (r,i+j), with i+j<N. Multiplication
by u^N demands incoming second index i+N; multiplication
by v^N demands incoming first index r+j+N. Both are outside
the original head. Therefore each inserted WHOLE-kernel
tail in (10) is zero on every original finite-head input.
This holds before closing a knot, for every original color.

It is a degree-tail annihilation, not a scalar value A=0
assigned inside (7). The separated full-Psi and Barnes kernels
are not finite nonnegative head polynomials. They do not
inherit this support assertion termwise. The exact constraint
after splitting is instead the equal-sum statement

    exterior[A S_N]+exterior[A D_N I_N]=0,                (11)

whenever the indicated original finite-head exterior is used.
It is invalid to set A=0 in a generic inverse norm or to
conclude from (11) that each current vanishes. Inputs outside
the original head already detect the nonzero degree shifts.

Likewise the current monomials do not force a degenerate
Hurwitz representation. On any regular logarithmic current
branch they add to its action respectively

    0,
    2pi*i(Logt-Logz_1),
    2pi*i(Logt-Logz_0-Logx).                              (12)

Their logarithmic momenta change by integer 2pi*i shifts,
while their EXPONENTIATED canonical relation is unchanged.
Thus they are lifted charge/degree corrections to whatever
regular current graph is present, not automatic identity
or rank-deficient classical maps. The known full-Psi deck
mixing can put the same growing S class into I, so a
current-only quotient cannot be imposed without transporting
this source extension.

## 7. Audit and remaining obligation

Run

    python3 experiments/audit_actual_trivalent_layer_crossing_source.py

The [audit](../experiments/audit_actual_trivalent_layer_crossing_source.py)
checks the exact inverse-fusion kernel, both original signed/color
crossings, two arbitrary Gaussian dilation values before moment
contraction, the positive complete-cell identity, whole original
pivotal word sources, the disjoint graph partition and the full-B
degree-tail assertion. All original normalization factors are read
from the independent original crossing evaluator.

To reach a global volume theorem one still needs to control the
remaining Rogers fibers and the combined marked source branches,
and show a nonzero geometric exterior coefficient or a suitable
global norm gap. Positivity of a single local bipyramid does not
give that gap, as the explicit original-source nongrowth chamber
already demonstrates. The normal form above states exactly the
actual network and currents to which such a proof must apply.
