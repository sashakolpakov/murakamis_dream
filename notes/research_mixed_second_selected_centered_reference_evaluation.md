# Centered rational transport for the second-selection reference

Research evaluation proof and bounded diagnostic specification, 6 November
2026. The first direct interval diagnostic was inconclusive before any
scalar budget was evaluated: its first transferred shape enclosed zero.
This note changes only the arithmetic enclosure of the same reference
curve. It proves a sequential mean-value enclosure without clipping
derivative inputs. It does not prove a selected-source sign.

## 1. The same parameter, formulas and admissibility conditions

Retain the notation and original logarithmic lifts of the
[reference-curve theorem](research_mixed_second_selected_reference_curve.md).
Here the first flag is fixed at \(\alpha=1\), and both
\(\beta=0,1\) are considered. The shapes have meanings
\[
 W=e^{2\pi i\xi},\qquad
 (E,A,U,Z,V,B,C)=
 (e^{-2\pi ie},e^{-2\pi ia},e^{-2\pi iu},e^{-2\pi iz},
  e^{-2\pi iv},e^{-2\pi ib},e^{-2\pi ic}).
 \tag{1}
\]
All seven negative-sign shapes are functions of this one \(W\).
The two original transfers are
\((Z,V)=T_3(A,U)\) and \((B,C)=T_{2+\beta}(Z,V)\).
No variable is independently optimized or replaced by a source root.

The existing exact factored maps in the frozen
[own-four driver](../experiments/certify_mixed_next_four_endpoint_budget.py)
provide \(E,A,U,Z\): its keys `e,z,s,b` have precisely those
meanings. They come from the original endpoint and first ordinary
transfer. The reusable polynomial jets and rational mean-value enclosure
are in the frozen
[rational arithmetic provider](../experiments/certify_mixed_endpoint_log_budget.py).
Use those factorizations instead of evaluating the nested first-transfer
quotient on independently widened intermediate intervals.

Every mandatory filter is unchanged from reference equations (7)--(9)
and the failed diagnostic: endpoint rectangles, the proved attached
height for \(a\), ordinary reduced disks and rectangles, both possible
next-type envelopes, and the oriented internal and wire sums. In
particular there is no new \(\Im z\le-.02\) filter. Equality and
uncertain comparisons remain. A box is excluded only by strict
incompatibility with a necessary condition; both suffix alternatives
must fail before their union can be excluded.

## 2. Factored initial shapes and their full-box derivatives

Let \(\mathcal W\) be the rectangular complex ball enclosing
\(e^{2\pi i\xi}\) on the prescribed auxiliary box, and let
\(W_0\) be its exact rectangular midpoint. The rectangle is convex.
For a factored rational map \(F=N/D\), evaluate the polynomial
products and derivatives on all of \(\mathcal W\). First certify
\(0\notin D(\mathcal W)\). Then
\[
 F'(\mathcal W)\subseteq
 \frac{N'(\mathcal W)D(\mathcal W)
             -N(\mathcal W)D'(\mathcal W)}{D(\mathcal W)^2},
 \qquad
 F(\mathcal W)\subseteq F(W_0)+F'(\mathcal W)(\mathcal W-W_0).
 \tag{2}
\]
The second formula follows by integrating the first along each segment
from \(W_0\) to \(W\). It is valid on the entire containing
rectangle, including points that later fail a reference filter.
The frozen `rational_enclosure` implements the right side of (2).
Its `product_jet` supplies the derivative enclosure separately.

Apply (2) to each of \(E,A,U,Z\). Keep three objects for each
shape: its value at the common \(W_0\), its containing value box
on \(\mathcal W\), and its derivative box on \(\mathcal W\).
No coordinate or geometric intersection is applied to these objects.

## 3. Sequential quotient-rule enclosures of the remaining shapes

Suppose \(P,Q\), their common-midpoint values, and their derivatives
with respect to \(W\) are already enclosed on the full rectangle.
For the first coordinate of a transfer, set
\[
 \begin{split}
 n&=1-PQ,& n'&=-P'Q-PQ',\\
 h&=(1-Q)^p,&h'&=-p(1-Q)^{p-1}Q',\\
 f&=n-Ph,&f'&=n'-P'h-Ph',\\
 d&=Qn,&d'&=Q'n+Qn'.
 \end{split}
 \tag{3}
\]
The outgoing retained shape is \(R=f/d\). Before estimating its
derivative, certify that the full boxes for \(Q,n\) exclude zero;
then the full box used as \(d\) must also exclude zero. The
quotient-rule enclosure is
\[
 R'\subseteq\frac{f'd-fd'}{d^2},\qquad
 R(\mathcal W)\subseteq R(W_0)+R'(\mathcal W)(\mathcal W-W_0).
 \tag{4}
\]
Every expression on the right uses only predecessor enclosures and
the certified denominator. In particular it does not use the unknown
new box for \(R\) to prove its own derivative bound.

For the second coordinate of a transfer, suppose \(Q,R\) and
their derivatives have already been enclosed. Put
\[
 \begin{split}
 k&=1-QR,&k'&=-Q'R-QR',\\
 d&=Rk+(1-R)^p,&d'&=R'k+Rk'-p(1-R)^{p-1}R'.
 \end{split}
 \tag{5}
\]
After checking the full denominator box excludes zero, the next
external shape \(T=k/d\) satisfies
\[
 T'\subseteq\frac{k'd-kd'}{d^2},\qquad
 T(\mathcal W)\subseteq T(W_0)+T'(\mathcal W)(\mathcal W-W_0).
 \tag{6}
\]
Equations (3)--(6) are the ordinary quotient-rule versions of reference
equation (20). They avoid the factors \(R\) or \(T\) on the
right of the logarithmic derivative form, and therefore expose a
noncircular order of enclosure.

The actual order is
\[
 \begin{array}{c|c|c}
 \text{new shape}&\text{already enclosed inputs}&\text{formula}\\ \hline
 V&Q=U,\ R=Z,\ p=3&(5)\text{--}(6)\\
 B&P=Z,\ Q=V,\ p=2+\beta&(3)\text{--}(4)\\
 C&Q=V,\ R=B,\ p=2+\beta&(5)\text{--}(6).
 \end{array}
 \tag{7}
\]
The midpoint value at each stage uses the predecessor midpoint values
at the same \(W_0\). The derivative uses the predecessor full-box
values and derivatives. Intermediate recentering tightens a proved
image; it is not an intersection with an admissibility filter.

**Proposition 1.** If the denominator checks in (2)--(7) pass, the
three objects at every stage contain the indicated original rational
function, its value at \(W_0\), and its derivative on all of
\(\mathcal W\).

The proof is induction in (7). Formula (2) establishes the base case.
The full denominator separation at a new stage proves holomorphy on
the rectangle before the derivative and image are enclosed. The chain
and quotient rules prove the derivative bounds, and the segment
integral proves the centered image. This proves the induction without
assuming any yet unproved separation for that new image.

The remaining original regularity conditions are checked before any
reference is admitted, including the shape zeros and
\(1-EW,1-E,1-EA,1-UA,1-A\), and all
\(1-PQ,1-QR,1-RT,1-Q,1-R\) from each transfer. The original
endpoint final denominator is nonzero also by its exact identity
\((1-EA)/U\); the factored first retained denominator is nonzero
by the checked \(U\) and \(1-AU\). No denominator separation is
inferred from clipped coordinate bounds. Failure of any arithmetic
separation is inconclusive, never an exclusion.

## 4. Original branches and the bounded diagnostic

Decode the seven negative-sign shapes by \(i\Log X/(2\pi)\)
only when their containing balls are strictly in the lower half-plane.
A shape wholly in the upper half-plane is strictly incompatible with
the necessary real-coordinate ranges; a box meeting the separating
axis is inconclusive. Apply the same necessary filters as before.
Only after derivative transport is complete may coordinate rectangles
be intersected for pointwise output. The original reference theorem's
zero-lift lemma applies to every admitted point, and identifies these
rational values with the original critical equations. No new branch
choice or logarithmic lift is introduced.

The new diagnostic uses exactly the previously prescribed box
\[
 \xi\in[115337/512000,57677/256000]
       +i[8919/256000,279/8000],
 \qquad a_{18}=001111101111010111.
 \tag{8}
\]
Its deterministic selection and reconstruction use only the saved
[complete central record](../repro/results/research-mixed-next-four-adaptive-budget-attempt02.json).
Run at 160 bits, once for each \(\beta=0,1\), with \(\alpha=1\).
There is no replacement box, subdivision, precision retry, or type-three
first endpoint. The box is not asserted to represent a finite word.

The record must preserve every factored and sequential stage's midpoint,
full image, derivative and denominator separation bounds, including
partial data if a later stage is inconclusive. It also saves the
untruncated decoded coordinates, necessary pointwise intersections,
admitted suffix alternatives, all exclusion or inconclusive reasons,
exact call counts and frozen input hashes. Hashes are checked before
repository imports and after evaluation. Old inspect and main functions,
the failed diagnostic's direct reference function, source primitives and
scalar conjugate evaluators are forbidden in this run.

This diagnostic evaluates reference transport only. Even two retained
families would establish no central budget or selected-source sign.
The failed direct diagnostic and its driver remain frozen; a scalar-flow
evaluation with the new provider would require a separate reviewed plan.
