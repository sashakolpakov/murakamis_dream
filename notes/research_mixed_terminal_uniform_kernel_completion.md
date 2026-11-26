# Complete selected terminal kernels on the canonical type-four input domain

Research completion, 6 November 2026.

The original selected ordinary-plus-terminal kernel now has a uniform
raw comparison gap \(1/2600\) on the canonical actual input domain
\(K_4\), for either terminal type three or four. Its complete finite
source has rate gap \(1/5200\) for all sufficiently large levels,
including both parities. The result includes every internal contour
current and physical complement of these two factors. It is local to
the specified outer plateau and unselected incoming leg.

## 1. Original reference and exact allocated product

Put
\[
 \begin{split}
 K_4&=\{|z-(3/10-13i/250)|\le3/50\}
                   \cap\{-27/250\le\Im z\le-1/1000\},\\
 P&=[11/50,9/20],\qquad H=1/100,\qquad X_z=e^{-2\pi iz}.
 \end{split}
\tag{1}
\]
The incoming flag and ordinary own flag are both one. The terminal
flag is \(\epsilon\in\{0,1\}\), denoting type \(3+\epsilon\).
For \(\zeta\in K_4\), let
\[
                  (b_*,s_*,a_*,t_*,v_*)
                   =(\zeta,s_*,a_*,t_*,v_*)
\tag{2}
\]
be the original canonical suffix, with \(v_*=\xi_*\) for terminal
type three and \(v_*=e_*\) for terminal type four. The
[all-input reference theorem](research_mixed_terminal_all_input_affine_enclosures.md)
and its [posterior refinement](research_mixed_terminal_quadratic_residual_refinement.md)
identify these same zero-lift branches. The primitive, private
stationary action and chirps below are original.

Use
\[
 \begin{split}
 Q_1(s;b,a)&=g(s+b)+g(s+a)-3g(s)-g(b)-g(a)+2\pi ibs,\\
 M_*(\zeta)&=Q_1(s_*;\zeta,a_*)+P_\epsilon(a_*)
                                -g(a_*)-\tfrac12g(\zeta),\\
 p_*(\zeta)&=g'(\zeta+s_*)-\tfrac32g'(\zeta)+2\pi is_*.
 \end{split}
\tag{3}
\]
Here \(P_\epsilon\) is the original stationary terminal action,
including its absolute constant. The index and terminal equations
are stationary, and
\[
 Q_{1,a}(s_*;\zeta,a_*)+P_\epsilon'(a_*)-g'(a_*)=0.
\tag{4}
\]
Thus the internal \(a\)-marginal cancels, while the full complex
incoming marginal \(p_*\) remains in every comparison.

The literal finite modulus is
\[
 \mathcal K_{N,\epsilon}(b,a;w)=
 \left|C_{1,N}(X_b,X_a)\,
       \mathcal V_{\epsilon,N}(w,X_a)\,
                   d_N(X_a)X_a^{-N}\right|\,|d_N(X_b)|^{1/2}.
\tag{5}
\]
The terminal factor \(\mathcal V_{\epsilon,N}\) is the original
reversed-cap source of
[the complete terminal envelope](research_mixed_terminal_concave_profile_envelope.md),
equation (1). It is not a cap with its two arguments transposed.
The complete selected diagonal and monomial appear once. The incoming
halfweight allocates a modulus; no holomorphic square root is inserted.

The outer target product is
\[
 b_R,a_R\in P,\qquad \Im b=\Im\zeta,\qquad \Im a=H.
\tag{6}
\]
Both real parts vary independently. In particular the target \(b_R\)
is not fixed to \(\Re\zeta\) or restricted by the reference disk
equation. The incoming leg is unselected.

The original type-three source theorem supplies its full ordinary
type-four input family. For terminal type four, the
[canonical source-domain theorem](research_mixed_terminal_canonical_source_domain.md)
proves the oriented and inverse-leg hypotheses throughout \(K_4\).
These results also supply the physical-tail and ordinary-color
source hypotheses and uniform neighborhoods on the compact family.
An arbitrary independent point of an image rectangle is not being
declared source-feasible. Auxiliary phase estimates on the larger
disk \(D_4\) do not enlarge the finite-source domain in this theorem.

## 2. Every terminal label and both complete-weight alternatives

The terminal envelope has 27 labels: 25 regular pairs from
\(\{0,L,R,-,+\}^2\), one physical entropy profile, and the
constant profile \(879/1000\). In a regular pair, the first coordinate
is the transform index and the second the private index. A main
coordinate uses its original reference height. Every real cut has
height zero. Each label retains its complete original active-index
domain and its stated alias penalties.

For a terminal profile \(T_{\epsilon,\sigma}\), define the
ordinary-main defect
\[
 \begin{split}
 D_{\epsilon,\nu,\sigma}
 ={}&\Re Q_1(s;b,a)+T_{\epsilon,\sigma}(a;y)
          -\tfrac12\Re g(b)-\nu\Re g(a)-2\pi\nu H\\
    &-\Re\{M_*(\zeta)+p_*(\zeta)(b-\zeta)\}.
 \end{split}
\tag{7}
\]
The factorial alternative is \(\nu=1\), and the forced alternative
is \(\nu=0\). Both retain all \(a_R\in P\), at the same height
\(H=.01\). They are the two additive rate alternatives for the
complete selected weight, not independently continued source
polynomials. Wherever a proof splits the weight into halves, it
uses the same choice of \(\nu\) in both halves.

The following completed estimates have identical reference, target,
height and normalization conventions:

| Profiles | Number of branches across both terminal types | Uniform raw gap |
|---|---:|---:|
| Main/main | 4 | \(1/400\) |
| Sixteen penalized alias endpoints per terminal type | 64 | \(1/20\) |
| Constant profile | 4 | \(1/100\) |
| Thirteen real-face families already paid by the global plane | 26 | \(>1/225\) |
| Type-four private-left face | 2 | \(51/20000\) |
| Type-three real right cut and entropy; type-four real left cut | 6 | \(>1/160\) |
| Type-four entropy, forced alternative | 1 | \(>5756/10^6\) |
| Type-four entropy, factorial alternative | 1 | \(>1/2600\) |

The table totals 108 branches, namely \(27\cdot2\) for each of the
two terminal types. The first three rows are the
[uniform main comparison](research_mixed_terminal_uniform_main_comparison.md),
[alias completion](research_mixed_terminal_uniform_alias_completion.md),
and [constant-profile theorem](research_mixed_terminal_uniform_constant_profile.md).
The old 26 real-face branches come from
[the exact global recombination](research_mixed_terminal_uniform_real_face_outcome.md).
The private-left estimate is its separate
[symmetric-cost transfer](research_mixed_terminal_private_left_symmetric_transfer.md);
its positive plane uppers are not used to prove that face.
The forced type-four entropy sign is in
[the source-cell outcome](research_mixed_terminal_source_cell_outcome.md).
The factorial type-four entropy sign is the
[terminal-side plane completion](research_mixed_terminal_terminal_side_plane_outcome.md).

The six new comparisons use the
[direct-cut theorem](research_mixed_terminal_real_transform_cut_budget.md)
and its [fixed protocol](research_mixed_terminal_real_transform_cut_protocol.md).
The literal real cuts \(t=.5\) and \(t=.15\) have height zero.
Their incoming dependence separates from the private variables, so
the original bare-source bound at \(a_*\) eliminates all private
targets. The same exact dependence applies to the entropy profile
at \(t=.5\). The corrected height value and selected force retain
the original chirp; the old \(t_*+a_*\) remainder cancels before
bounding. The remaining two scalar costs are integrated on the
full target intervals. No main-height index restriction is assigned
to a real cut, and no new private action is evaluated.

The completed six upper bounds are below these terminating rational
ceilings:

| Terminal type and profile | Factorial | Forced |
|---|---:|---:|
| Three, real right cut | \(-.068056\) | \(-.151542\) |
| Three, physical entropy | \(-.065250\) | \(-.148737\) |
| Four, real left cut | \(-.006497\) | \(-.056088\) |

All six are strictly below \(-1/160\). Their superseded positive
upper bounds remain in the historical records. Thus every branch
in (7) now satisfies
\[
                   \sup D_{\epsilon,\nu,\sigma}<-1/2600.
\tag{8}
\]
The least available reserve in the table is the independently paid
type-four factorial entropy branch. Neither positivity of a majorant
nor a pointwise maximum principle for an optimized budget is used.

## 3. Complete ordinary and terminal finite-source coverage

The [ordinary-label completion](research_mixed_terminal_ordinary_label_completion.md)
applies because
\[
 -.108\le\Im\zeta\le-.001,\qquad
 -.102<\Im s_*<-.001,\qquad b_R,a_R\in P,\qquad \Im a=.01.
\tag{9}
\]
Its six nonmain ordinary labels lie below the ordinary main maximum
with an additional gap at least \(1/500\). The terminal profile,
both weights, and the incoming affine term are independent of the
ordinary index, so adding them preserves each comparison. The
ordinary gap is added to (8), not subtracted from it. There is no
further minimum with \(1/500\).

The finite seven-label ordinary envelope is valid on (9), including
the endpoint height \(-.108\). It keeps the complete physical
rows, wrapped rows, half row, aliases, joins, and four affine
last-row carriers. Consequently the full
\(7\cdot27\cdot2=378\) comparisons for each terminal type have
the same raw gap in (8).

The terminal source reduction retains its original double summation
orientation. It deforms every unaliased index to its main height,
also when the other index is an alias. A vertical alias side is
split at zero height; on each sign half the alias penalty is
linear and the phase is convex in that height. Its endpoints are
an outer penalized alias label and a zero-height real-cut label.
All those endpoints now satisfy (8). Applying the same argument
successively in both indices controls every double alias side.
Main-to-real-cut joins are controlled by their main and real-cut
endpoints. The previously unproved zero-height endpoints are
therefore no longer an omitted part of the alias comparison.

The physical complement is also retained in full. The constant
profile controls the coherent outer end rows and positive Newton
exterior majorants. The original left-strip and private-tail
transports end at the real cuts already present in (8). The strip
at the upper transform cut, including the even-level half row,
uses the real \(t=.5\) anchor with its original \(O(N^{-1})\)
rate tolerance. The entropy profiles control the entire physical
right triangle, including its support walls and zeros. The
type-four source contains the entire private ordinary polynomial;
off-grid terms revived by contour motion are not discarded.
These are the exhaustive physical partitions of the original
terminal-envelope theorem, not a replacement source.

## 4. Uniform complete local finite-kernel theorem

**Theorem.** For each sufficiently small fixed \(\eta>0\), there
are an ordinary-color neighborhood of the complete color \(w=-2\)
and constants \(C_\eta,A_\eta,N_\eta\), uniform in
\(\zeta\in K_4\), such that
\[
 \mathcal K_{N,\epsilon}(b,a;w)
 \le C_\eta N^{A_\eta}
       \exp N\{\Re[M_*(\zeta)+p_*(\zeta)(b-\zeta)]
                                      -1/2600+\eta\}
\tag{10}
\]
for both terminal types, all targets (6), and all integers
\(N\ge N_\eta\) of either parity. Each prescribed fixed
ordinary-color jet of the original integer-weighted holomorphic
source obeys the same rate on a smaller neighborhood, with its
polynomial prefactor and tolerance, after the incoming modulus
allocation.

*Proof.* Use the complete selected-weight bound with one choice of
\(\nu\) fixed throughout each alternative. By Sections 2--3, all
378 finite profiles for that terminal type have gap greater than
\(1/2600\). Apply the complete original ordinary and terminal
finite-source envelopes, retaining all currents and physical
majorants, and sum their finite profile bounds with one total
positive tolerance \(\eta\). Uniform ordinary-color neighborhoods
come from the original regular interpolants, zero-safe finite
products, and compact source-domain coverage. Cauchy estimates
apply to the original integer-weighted holomorphic source; the
modulus halfweight is not differentiated as a holomorphic
function. This proves (10). \(\square\)

Choose \(\eta<1/10400\) and absorb the polynomial prefactor using
a further reserve smaller than \(1/10400\). For all sufficiently
large \(N\), (10) then retains the explicit finite rate gap
\[
                              1/5200 .
\tag{11}
\]

Every actual positive mixed open word of length \(m\ge3\) with
final types \((n_{m-2},n_{m-1},n_m)=(4,4,3+\epsilon)\), and
unselected incoming leg \(b\), satisfies these local reference
hypotheses. At \(m=3\) the incoming reference is attached to the
first endpoint; for \(m>3\) it is ordinary. The original uniqueness
theorem identifies its suffix with (2). The proof does not require
arbitrary canonical parameters to be realized by finite words.

This theorem controls a complete local finite source on (6).
It does not cover incoming type three, a selected incoming leg,
or a length-two word whose preceding factor is an endpoint.
It does not estimate outer real tails, variable-height outer
contours, their reset faces, or nonplateau joins. The incoming
affine marginal in (10) still has to cancel against the adjoining
original source, with its complementary halfweight. This upper
bound alone proves no nonzero global amplitude, whole-word
asymptotic, outside-color decay, arbitrary short-filling theorem,
or cofinite knot-volume result.

## 5. Immutable completed evidence

The new direct-cut record is
[research-mixed-terminal-real-transform-cut-budget.json.gz](../repro/results/research-mixed-terminal-real-transform-cut-budget.json.gz),
SHA256 6f526c7a5b9c5f0f3b23a23a79ada4c5670966b7518959600e0a02b1caeea8cb.
The prescribed two-case run completed at 256 bits with 32 new
height-slab cotangent enclosures, two center cotangents, four
sines and two logarithms. It retained all 192 force vertices,
384 scalar gains with their independent exact checks, and six
source comparisons. All 528 input bindings were unchanged.
There were no roots, private actions, source replays, new parameter
cells, subdivisions or retries.

The [direct-cut saved-data audit](../repro/results/research-mixed-terminal-real-transform-cut-saved-audit.json),
SHA256 29d1edc0a516e44ceac16f3c9fe9868bfee0e8c3268134819f05bbd21067306e,
checks the saved exact arithmetic and source associations without
analytical evaluation. It retains the prior upper bounds, recombines
all six new comparisons, and verifies that all 36 real and entropy
branches have the common gap \(1/2600\), with no remaining branch.
All 563 input bindings were unchanged.

The limiting factorial entropy sign is bound by
[the terminal-side saved audit](../repro/results/research-mixed-terminal-terminal-side-planes-saved-audit.json),
SHA256 4f387cabec8dcc511aa28a43ebc6887e63eaffbf48eef104ca8612b68f80ac29.
Its complete upper is less than \(-.0003956<-1/2600\).
The other real and entropy comparisons are recorded in
[the global recombination](../repro/results/research-mixed-terminal-uniform-real-face-comparison.json),
[the source-cell recombination](../repro/results/research-mixed-terminal-source-cell-comparison.json),
and [the private-left transfer](../repro/results/research-mixed-terminal-private-left-symmetric-transfer.json).
The original failed or inconclusive upper bounds in those
historical calculations are preserved.
