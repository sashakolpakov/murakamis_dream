# One bounded cover for the remaining next-four scalar comparisons

Research certificate specification, 6 November 2026. This note describes
one new full-domain attempt with ten inequalities per accepted leaf.
It does not assert that the attempt has run or that its partition is
complete. The three one-box diagnostics are implementation checks,
not substitutes for the cover.

## 1. The common reference domain and the ten tests

Use the actual first-four/next-four reference of a fixed mixed open word
of length at least three. The incoming selected height is
\(H=1/100\), and all other heights retain their original values.
The auxiliary root rectangle is
\[
 \mathcal U=[217/1000,117/500]+i[27/1000,9/200].
 \tag{1}
\]
The [reviewed own-four reference helper](../experiments/diagnose_mixed_four_four_half_row_budget.py)
uses the original rational maps, principal coordinate logarithms,
coordinate rectangles, reduced disks, coupled pair sums, and necessary
next-external-domain conditions in the
[evaluation specification](research_mixed_selected_four_four_half_row_evaluation.md).
Its additional scalar tests are exactly the necessary filters of the
completed next-four central certificate. In particular the outgoing
map and next-external relation have the own-four factorial power.
Every required actual reference is covered, including an attached
next external input at length three. This does not assert that each
retained auxiliary point is realized by a word.

All ten quantities are evaluated at the same auxiliary box. Four
upper bounds come from the
[half-row theorem](research_mixed_selected_four_four_half_row_majorant.md):
\[
 \mathcal H^{(4)}_{0,1},\quad \mathcal H^{(4)}_{0,0},\quad
 \mathcal H^{(4)}_{L,1},\quad \mathcal H^{(4)}_{L,0}.
 \tag{2}
\]
Two upper bounds come from the
[left-cap/main theorem](research_mixed_selected_four_four_left_main_majorant.md):
\[
                   \mathcal J^{(4)}_1,\quad\mathcal J^{(4)}_0.
 \tag{3}
\]
The last four quantities are the lower bounds for the exact trial
differences in the
[ordinary left-cut corner reduction](research_mixed_selected_four_left_row_corners.md):
\[
 D_{11/50,11/50},\quad D_{11/50,9/20},\quad
 D_{9/20,11/50},\quad D_{9/20,9/20}.
 \tag{4}
\]
With \(\delta=1/2000\), an accepted box must satisfy all six
upper tests strictly below \(-\delta\), and all four lower
tests strictly above zero. No extra gap is required in (4):
\(B_L\le B_0\) already transfers the established joint gaps.
Serialized directed endpoints are exact rationals; readable ball
strings are not used for acceptance.

## 2. Unchanged arithmetic and allocation

The wrapper invokes the three frozen inspection routines without
altering their arithmetic. Repeated calls to the same reference helper
are allowed; no independent reference or target is substituted. The
helper returns the auxiliary variable, all four rational shapes, and
coordinate enclosures intersected with their necessary rectangles.
These are pointwise containing enclosures. No parameter derivative
or integration along the clipped coordinate images is used.

Every primitive uses the
[centered original enclosure](research_mixed_centered_primitive_enclosure.md)
on a whole regular rectangle:
\[
 g(W)\subseteq g(w_0)+\Log(1-e^{-2\pi iW})(W-w_0),
 \qquad 0<\Re W<1.
 \tag{5}
\]
The actual private action retains the original auxiliary coordinate;
only the fixed left cut uses its explicit canonical root. The
ordinary phase is explicitly
\[
 Q_4(s;z,b)=g(s+z)+g(s+b)-3g(s)-g(z)-g(b)+2\pi izs.
 \tag{6}
\]
The outgoing halfweight remains in the marginal
\(p=g'(s_*+b_*)-3g'(b_*)/2\), the half-row gradient and
curvature \(41/10\). It cancels from the trial action only
after those derivative terms have been retained. In (3), the
additional index factorial contributes to
\(\mu_s=\pi(39/80+\Re\cot\pi s_*)\); the negative
index gain and incoming gain remain the reviewed rational clipped
bounds. The corner differences retain the original chirp and
coefficient \(-3g(s_*)\).

No old central scalar inspection, finite quantum sum, proposed root,
moving target solve or diagnostic main program is called. The earlier
records supply frozen dependencies and implementation provenance only.
An unresolved pole, branch, primitive enclosure or sufficient sign
causes subdivision or an unresolved frontier, never a geometric
exclusion. A strict exclusion returned by any of the three identical
necessary-reference filters is sufficient to discard the box for all
ten tests.

## 3. Exact bounded traversal and retained frontier

The new driver is
[the combined scalar wrapper](../experiments/certify_mixed_selected_four_four_scalar_cover.py).
It sets 160-bit precision before constructing the primitive provider.
It starts from (1), permits at most 8,000 newly inspected boxes,
and has maximum depth 20. The split alternates real and imaginary
axes, real first, at their exact rational midpoints. Child zero is
the lower half and is visited first. There is no restart, continuation,
automatic precision escalation or second full-domain attempt in this
specification.

For each box, the wrapper calls all three scalar inspectors unless an
earlier necessary-reference exclusion has already decided the box.
An accepted leaf requires all ten exact endpoint checks, independently
of a callback's displayed status. The statuses `split` and
`inconclusive` both request subdivision. The first unresolved box at
depth 20 stops the entire traversal. A cell-budget stop retains every
unvisited box, rather than silently treating it as accepted. An
unexpected arithmetic error also stops with an unresolved frontier.

The active box stays on the pending stack until its result is
committed. Handled interruption signals request a stop after the
current atomic commit; they do not remove the active box. Each
committed operation replaces a pending box either by one terminal
leaf or by its two exact children. Thus accepted, excluded and
unresolved addresses remain an exact disjoint partition of (1).
The output checks that the address list is prefix-free and that
\[
   \sum_{\text{terminal or pending address }a}2^{-|a|}=1.
 \tag{7}
\]
It also reconstructs every recorded pending box from its address.
Depth failures retain their computed enclosures; untouched frontier
boxes are explicitly marked uninspected. The record reports exact
accepted, excluded and unresolved dyadic masses as well as counts.

The new output path must be absent. The record is installed atomically
without overwriting an existing record. Every reviewed proof, provider,
diagnostic record and transitive dependency is hash-bound before
inspection and checked again afterward. A dependency change prevents
a completed claim. The wrapper records its own bytes as well.

## 4. What a completed record would prove

**Proposition 1 (certificate soundness).** If the bounded attempt
returns a complete partition with all ten strict checks on every
accepted leaf, then (2)--(3) are uniformly below \(-1/2000\)
at every required actual reference, and (4) are positive there.

Every actual reference belongs to (1), survives every necessary
exclusion, and is contained in an accepted leaf. The proved outward
formulas then imply its six upper comparisons and four lower
comparisons. This proves the proposition. A partial record proves
only its recorded accepted subregions; an unsuccessful sufficient
test is not an actual-source counterexample.

For clarity, the resulting finite-source consequence would use no
new phase identity. The four corners give \(B_L\le B_0\).
The two bounds (3) pay \(A_L+B_0\), while (2) pay
\(A_0+B_R\) and \(A_L+B_R\), each with both complete
Fourier alternatives and gap \(1/2000\). The central,
cap-alias, right-cap-cut and last-row estimates are already proved.
Therefore the five-pair maximum in the
[next-four finite reduction](research_mixed_selected_four_four_finite_reduction.md)
would be strictly below \(-1/2000\).

In that event, its Theorem 1 would imply, for every positive total
tolerance \(\tau\),
\[
 |\partial_w^k\{U_{1,N}(w,X)C_{1,N}(X,Y)d_N(X)X^{-N}\}|
                  |d_N(Y)|^{1/2}
 \le C_{\tau,k}N^{D_{\tau,k}}
       e^{N\{M+\ell_b(v)-1/2000+\tau\}}.
 \tag{8}
\]
Here the ordinary color disk, fixed derivatives, original logarithmic
constants, both level parities, complete finite index ranges and
outgoing real affine term are exactly those of that reduction.
The outgoing halfweight is a modulus allocation, not a holomorphic
square root. This is a two-factor source consequence for words of
length at least three. It supplies no estimate for all remaining
open-word sectors, length two, arbitrary short fillings or global
noncancellation.

No completed record or assertion (8) is claimed by this specification.
