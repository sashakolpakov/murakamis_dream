# Reusing a complete auxiliary cover for the second selection

Research deduction, 6 November 2026. This identifies a complete pending
reference partition for first flags \((1,1,\beta)\), uniformly over
all \(\beta\in\{0,1\}\), all suffixes and every word length \(m\ge4\).
It reuses only necessary-reference exclusions from a completed cover.
Its earlier scalar successes do not certify the new central budgets.
No reference map, primitive, root, or finite source is evaluated here.

## 1. The exact correspondence of reference variables

Use \((e,a,u,z,v,b,c)\) and the positive-sign endpoint parameter
\(W=e^{2\pi i\xi}\) from the
[second-selection reference curve](research_mixed_second_selected_reference_curve.md),
with \(\alpha=1\). The former
[first-four/next-four reference cover](research_mixed_first_four_next_four_central_gap.md),
Section 3, uses
\[
 (e_{\rm old},z_{\rm old},s_{\rm old},b_{\rm old},
                          c_{{\rm next},{\rm old}})
                 =(e,a,u,z,v).
 \tag{1}
\]
These are the same original reference, before any selected-height
target is introduced. In particular the old first ordinary
transfer is precisely the first of the two new transfers.
The old next-external coordinate is \(v=s_3^*\), not \(b=r_3\)
or \(c=s_4^*\).

Every present reference has
\[
 \xi\in R=[217/1000,117/500]+i[27/1000,9/200].
 \tag{2}
\]
The old ordinary block has own type four, one external leg \(a\)
of type four and the other external leg \(v\) of type \(3+\beta\).
Thus the old necessary restrictions all remain valid:

* The private and attached endpoint rectangles apply to \(e,a\);
  the proved coupled attached-height bound gives \(\Im a>-.078\).
* The two outputs \(u,z\) belong to \(O_4\); \(a,u,z\) belong
  to the reduced disk \(P_4\).
* The wire sum satisfies \(\Re(a+u)\in(.545,.77)\).
  The internal sum satisfies \(\Re(u+z)\in(.527,.77)\).
* The next external leg \(v\) belongs to \(K_3\cup K_4\), and
  its negative-sign exponential lies strictly below the real axis.

The stricter-looking internal floor \(.527\) in the old code is
valid here. The
[reduced-disk pair-sum theorem](research_mixed_reduced_disk_pair_sums.md)
gives the outward lower bounds \(.52743034\) for own four with
external types three/four, and \(.55863533\) for four/four.
Reflection interchanges the two external legs without changing
the internal sum. The new reference-curve note's \(.525\) was a
weaker convenient floor, not a limitation of the saved theorem.
The old typed envelope also includes attached next legs at length
three; the present \(m\ge4\) next leg \(v\) is ordinary and
satisfies the same necessary inclusion.

The old scalar-range exclusions are necessary-reference tests too.
For that old test only, put \(H_1=1/100\),
\(\lambda_1=e^{2\pi(H_1-\Im a)}\),
\(\ell_1=\log\lambda_1\), and
\[
 B_1=\log\left|
 \frac{1-\lambda_1 e^{-2\pi i(u+a)}}{1-e^{-2\pi i(u+a)}}\right|,
 \qquad d_1=\ell_1-B_1,\qquad
 q_1=\Re(a+u)-\tfrac12 .
 \tag{3}
\]
Then \(0<d_1<1\), \(.045<q_1<.21\), and
\(\Re\cot(\pi u)>2/5\), exactly as proved in the old
central-gap theorem. These statements concern functions of the
unchanged reference. They remain true when the new problem
selects position 2 and leaves position 1 unselected.
They are not new values of the position-2 increments.

## 2. A complete pending partition with no repeated source calculation

The completed record is
[adaptive attempt 02](../repro/results/research-mixed-next-four-adaptive-budget-attempt02.json),
SHA-256
6e3520360bf93d779c359f39f33e479cf422ef2fa7eadbfe23ce0b5383af7d27.
Its fixed original
[driver](../experiments/certify_mixed_next_four_adaptive_budget.py)
and [pending-only continuation](../experiments/resume_mixed_next_four_adaptive_budget.py)
distinguish an excluded leaf from a successful scalar test.
The saved partition contains
\[
 3291=2613+678\ \text{leaves},\qquad
 6581=2\cdot3291-1\ \text{visited nodes},
 \tag{4}
\]
with no unresolved leaves and maximal depth 19.
Its binary addresses are prefix-free and their exact dyadic
masses sum to one. All seven directly bound inputs still have
their saved hashes.

The excluded-leaf inventory is:

| Saved reason | Count | Present coordinate or condition |
|---|---:|---|
| old \(b\) range | 1313 | \(z\in O_4\) |
| old \(s\) range | 811 | \(u\in O_4\) |
| old \(z\) range | 315 | attached \(a\) rectangle |
| next external typed domains | 112 | \(v\in K_3\cup K_4\) |
| old \(b\) reduced disk | 28 | \(z\in P_4\) |
| old \(e\) range | 26 | private endpoint rectangle |
| old \(s\) reduced disk | 7 | \(u\in P_4\) |
| actual ordinary curvature | 1 | \(\Re\cot(\pi u)>2/5\) |

Each exclusion is a strict contradiction of a necessary reference
condition. Uncertain intervals, nonfinite estimates, and boundary
equalities were not discarded. Every one of the other 678 leaves
has status accepted and reason “both credits”; those old rate
successes are not exclusions.

**Proposition 1 (coverage transfer).** The union of the 678 old
accepted closed boxes contains every actual auxiliary reference
in (2) for \((1,1,\beta)\), \(m\ge4\). Their exact total
dyadic area fraction is
\[
                         \frac{2587}{65536}.
 \tag{5}
\]
The 2613 excluded boxes can be preserved without reevaluation in
a new second-selection computation.

*Proof.* The old terminal partition covers all of \(R\).
By Section 1 every actual new reference satisfies every necessary
condition used for an old exclusion. Therefore no actual reference
belongs to an excluded box. It must belong to an old accepted
box. The prefix-free addresses and (5) are checked using exact
fractions only. \(\square\)

This proposition imports coverage, not a single new scalar sign.
For each \(\beta\), all 678 boxes initially have the status
pending for the new problem, even though their old status was
accepted. The two beta cases may subsequently have different
necessary-filter outcomes.

## 3. Staged reference exclusion before expensive continuation

The [exact-shift evaluator](research_mixed_second_selected_shifted_reference_evaluation.md)
provides whole-rectangle values and derivatives of the canceled
rational maps. A new provider can evaluate \(E,A,U,Z,V\), then
\(B_\beta\), and apply each necessary filter immediately.
In particular it need not evaluate \(C_\beta\) before testing
whether \(B_\beta\) lies strictly above the real axis.
The [saved excluded reference box](research_mixed_second_selected_saved_reference_exclusion.md)
shows why this ordering is useful. All original diagnostic records
and their reported statuses remain unchanged.

Here is a safe algebraic exclusion even before a quotient is formed.
For a canceled rational map \(F(W)=N(W)/D(W)\), every actual
reference has \(D(W)\ne0\), and
\[
 \Im F(W)=
    \frac{\Im\{N(W)\overline{D(W)}\}}{|D(W)|^2}.
 \tag{6}
\]
If the whole-box lower bound for the numerator in (6) is
strictly positive, the box cannot contain an actual reference
whose required shape is in the lower half-plane.
For this exclusion alone no logarithm is needed. Conversely,
failure to separate its sign is inconclusive.
The proof uses the value of the same \(W\); rectangular interval
products only enlarge the containing range.

For retained evaluations, every original uncanceled division and
logarithmic lift must still be checked as in the reference theorem.
A complex rectangle excludes zero whenever either of its real
or imaginary intervals excludes zero. This Cartesian test may
be used in addition to a positive modulus lower bound; the latter
can be unnecessarily coarse. It changes no reference domain.
Coordinate intersections with necessary ranges are permitted only
after obtaining full-parameter shape and derivative enclosures.

The immediate proposed reference-only pass preserves the 2613
old excluded leaves and calls the staged provider at most once
for each of the 678 remaining boxes and each beta: at most 1356
reference cases, with no subdivision or replacement box.
It distinguishes necessarily excluded, reference-retained, and
inconclusive cases. A reference-retained case certifies neither
word realization nor any central sign. All inconclusive cases
remain in the complete partition.

A later bounded continuation could process only those pending
roots and their descendants, keeping a separate exact frontier
for each beta. A scalar-success status would require the new
branch-budget inequalities, not the old acceptance. The inherited
dyadic partition supplies coverage without random diagnostic
retries. No new reference pass or scalar-budget computation is
performed here.

## 4. What the external-coordinate chart does and does not supply

The reference-curve theorem also proves a unique holomorphic
canonical prefix over either next-external input disk, with
unramified projection \(W\mapsto C_\beta(W)\) on the admitted
chart. This is a useful alternative parameterization.
It does not itself give quantitative inverse enclosures on a
partition of \(K_3\cup K_4\). A new inverse-chart computation
would need such enclosures, retaining its original lifts and
all source conditions. The saved auxiliary partition in
Proposition 1 already supplies complete parameter coverage and
does not require that additional inverse construction.
