# Polynomially conditioned signed Green transport with the original source

28 October 2026. The physical crossing Green equation has a useful
whole-word consequence: its complete clock-family transport and inverse
have polynomial norms for every fixed signed diagram and every bridge
count. The original contraction is transported as a functional, rather
than replaced by a positive contraction or a geometric quotient.

This is an ambient source-transport theorem. It does NOT give a lower
bound for the restriction of that functional to geometric data. In fact
the complete ground data already contain the original positive crossing
entries by an isometric reindexing. That fact sharply limits what can be
deduced from the norm theorem alone.

## 1. The actual signed clock families

Fix N>=2, Q=exp(2*pi*i/N), q=exp(pi*i/N), x=-q^(-1), and
F_a=(Q;Q)_a. Use the SAME balanced finite heads V=C^N as in the
[literal crossing source](actual_trivalent_layer_crossing_source.md).
Keep the original unit-modulus Cartan scalar kappa external. Give
End(V tensor V) its flat Hilbert--Schmidt norm, and put

    E_N = direct_sum_(m in Z/N) End(V tensor V),
    ||X||^2 = sum_m ||X_m||_HS^2.

The [physical Green theorem](actual_rogers_sink_opposite_beta_source.md#8-the-actual-shared-head-source-combines-the-currents-into-a-ground-channel)
constructs ACTUAL internal-clock insertions K_m^+, and their full
retained ground sources H_m^+, with

    K_m^+ - A_+ K_(m+1)^+ = H_m^+,
    (A_+ X)_(c,d;a,b) = x^(-1) X_(c,d-1;a-1,b).       (1)

An out-of-range index on the right means zero. In particular A_+
retains both physical barriers. It is a partial coordinate shift
times a unit scalar, so ||A_+||<=1 and A_+^N=0.

The [signed transport proof](signed_green_antiunitary_transport.md)
shows that at this COMPLETE color the balanced negative crossing is obtained by
flip and complex conjugation:

    R_- = P overline(R_+) P.                          (2)

This includes kappa, since its conjugate is its inverse. For clarity,
the proof starts from the original unbalanced crossing conjugation
relation with its Cartan diagonal D. The balanced basis change has
g_j/overline(g_j)=(-1)^j q^(j(j+1)). Its residual diagonal on a pair
(a,b) is q^((a+b)(a+b+2)), depending ONLY on total integer degree.
It therefore commutes with both the crossing and the flip, and cancels
from the conjugation relation. No exponentially sized factorial gauge
is used as an isometry.

Consequently K_m^-=P overline(K_m^+)P and
H_m^-=P overline(H_m^+)P are actual negative-crossing clock families,
and their equation is (1) with

    (A_- X)_(c,d;a,b) = x X_(c-1,d;a,b-1).             (3)

The label m names the conjugated original insertion; it does not
reassign its physical clock orientation. Again ||A_-||<=1 and
A_-^N=0 in the SAME flat metric. These assertions concern the complete
color; a fixed nonunit color cannot be included by silently treating
|x| as one.

## 2. A bounded inverse on the entire clock space

Define T_s on E_N by (T_s X)_m=A_s X_(m+1), s=+,-.
The clock shift is a cyclic isometry and commutes with A_s. Hence

    T_s^N=0,  ||T_s||<=1,
    G_s=(1-T_s)^(-1)=sum_(j=0)^(N-1) T_s^j,
    ||G_s||<=N,  ||G_s^(-1)||<=2.                     (4)

Thus the full actual family satisfies K^s=G_s H^s. This is an
isomorphism on ALL of E_N, not only on vectors meeting a guessed
geometric support condition. It preserves the currents already
combined into the explicit H_m; none is set to zero.

Nilpotence here has index N. What makes (4) useful is the contraction
bound on EACH power, not nilpotence by itself. A nilpotent matrix with
exponentially large entries would not give (4).

For a fixed word with r signed crossings put

    E_W = tensor_(v=1)^r E_N,
    G_W = tensor_(v=1)^r G_(s_v),
    k_W = tensor_v K^(s_v),  h_W = tensor_v H^(s_v).

The tensor Hilbert norm gives the general, all-bridge theorem

    k_W=G_W h_W,
    ||G_W||<=N^r,  ||G_W^(-1)||<=2^r.                 (5)

In particular this change of the COMPLETE data has zero exponential
conditioning cost as N tends to infinity for any fixed word. Neither
the word nor its bridge count is allowed to grow with N in this claim.

## 3. Carry the specified original co-source

Let L_W be the EXACT original linear tensor contraction: evaluate
each external clock label at zero, connect the original head indices
in their original order, and apply the specified cups, caps, pivotal
weights and external normalization line. In a braid presentation the
same statement uses its original selected cut and pivotal closure.
No new trace or averaging is substituted for that selected functional.
The original scalar is therefore

    K_N(W)=L_W(k_W)=(L_W composed with G_W)(h_W).       (6)

Define L_W^G=L_W composed with G_W. Equations (4)--(5) imply, for
the dual norm on the FULL ambient tensor space,

    2^(-r)||L_W|| <= ||L_W^G|| <= N^r||L_W||.          (7)

The lower inequality follows from L_W=L_W^G composed with G_W^(-1),
so it requires no positivity assertion. The fixed original complete
source has polynomial coefficients and polynomially many tensor
entries: balanced pivotal entries have unit modulus, and the original
cup/marked-cap normalizations are fixed powers of N times unit color
phases. Thus its norm is polynomially bounded for a fixed diagram.
The exact external factors are retained in L_W on BOTH sides of (7).

For any vector h and nonzero L_W, the elementary Hilbert-space identity
dist(v,ker L)=|L(v)|/||L|| now gives

    2^(-r) dist(h,ker L_W^G)
       <= dist(G_W h,ker L_W)
       <= N^r dist(h,ker L_W^G).                     (8)

This quantifies preservation of the actual cancellation problem. It
does not replace distance by ||h||. A tensor can be large and belong
to the exact kernel. Nor does (7) give a lower bound for L_W^G
RESTRICTED to a geometric submodule or to the actual ground-support
subspace; that restriction can vanish.

## 4. The complete ground data have an exact visible-support metric

The positive sources are, for alpha+beta<N,

    H_m^+|alpha,beta> =
       Q^(m beta) x^(-beta) {alpha+beta choose alpha}_Q
          (Q^(m+1);Q)_alpha |alpha+beta,0>.            (9)

Choose 0<=m<N. The coefficient vanishes if alpha+m>=N, because the
displayed Pochhammer then contains 1-Q^N. Every remaining entry maps,
under the mth Green term, to the original crossing entry with

    input  (alpha+m,beta),
    output (alpha+beta,m),

and changes only by the unit scalar x^(-m). Distinct entries in (9)
give distinct crossing entries, and every nonzero original crossing
entry is obtained this way. Therefore, exactly,

    sum_m ||H_m^+||_HS^2 = ||R_+/kappa||_HS^2.        (10)

Flip-conjugation gives the identical negative statement. In particular

    (sum_m ||K_m^s||_HS^2)^(1/2) <= N ||R_s||_HS.     (11)

Here |kappa|=1. Equation (11) controls ALL these internal clock
responses despite the factorial frames in their definition. For a
fixed signed word, (5) and (10) give the analogous tensor bound

    ||k_W|| <= N^r product_v ||R_(s_v)||_HS.

This does not bound the clock-inserted SCALAR by the uninserted knot
scalar: contraction can cancel, and (8) is the exact distinction.

The endpoint channel is not of lower exponential order. Already H_0
has the norm computed in the local source note,

    ||H_0||^2=max_(t<N)|F_t|^2 sum_(b=0)^t |F_b|^(-2),

with a strictly positive exponential rate. The ground presentation
therefore transports the original bulk difficulty; it does not prove
that all nonground or current contributions are negligible.

## 5. What remains on the critical path

We now have an exact polynomially conditioned signed transport with
the ORIGINAL functional, without dropping peripheral or endpoint/current terms.
This answers a specified transport-norm question for this presentation.
It does not identify a geometric quotient, prove that L_W^G is nonzero
on the marked Bloch-regulator sector, or bound the total remainder by
a smaller exponential. Those are still necessary for the requested
volume limit. In particular (5) is not completion of the general
source-coefficient gate: that gate concerns a geometric projection,
whereas (5) concerns the complete ambient data.

The [audit](../experiments/audit_whole_word_ground_green_transport.py)
and [results](../experiments/whole_word_ground_green_transport_results.json)
verify signed finite transport, nilpotence,
the visible-support isometry, and the unchanged original contraction
on a nonfactorable ambient test as well as actual crossing tensors.
The all-N statements follow from the index and operator proofs above.

## 6. A global bound with several actual gluing-source insertions

The [complete crossing normal source](actual_crossing_shared_face_fourier_source.md)
is a different operator from the unweighted H_m in (9). At complete
color it obeys the sharp flat bound ||L||=N-1 for N>=3 and sqrt(2)
for N=2. Flip-conjugation defines the opposite signed insertion in
the same metric. Since its rank is at most N^2, its Hilbert--Schmidt
norm is O(N^2); every original scalar factor is still attached.

The [uniform weighted crossing estimate](weighted_crossing_source_gap.md)
proves at zero weights

    log ||R_+||_HS = log ||R_-||_HS
                  = N v_8/(2*pi)+O(log N),

where v_8=4 Catalan is the regular ideal octahedron volume. This
constant is an exact local norm rate, not the volume of the knot.

For a fixed original word with r crossings, replace any s distinct
crossing slots by these actual L operators (or their signed versions),
and retain its SAME original source. The polynomial source norm and
tensor norm inequality give unconditionally

    |L_W(tensor with s such insertions)|
       <= N^C exp[N (r-s)v_8/(2*pi)].                 (12)

Here C depends on the fixed diagram, not on N. This is valid for every
bridge count and every placement of the specified insertions. It does
not assert they form a nilpotent ideal: in particular their degree-N
carry contains a nonzero idempotent.

Consequently these terms are exponentially smaller than a POSITIVE
target of rate V/(2*pi) whenever (r-s)v_8<V. This is a precise sufficient
condition, not a claim that the current decomposition of the original
invariant already has that many insertions. A single local source
replacement generally leaves a bound much larger than Vol(K).
Equation (12) controls some whole-source terms, but neither bounds the
remaining invariant sharply nor proves its geometric lower bound.
