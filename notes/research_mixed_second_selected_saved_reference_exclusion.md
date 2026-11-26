# Excluding the inherited box from saved reference bounds

Saved-data deduction, 6 November 2026. The shifted reference diagnostic
stopped inconclusively in its final derivative guard. Its already saved
retained-coordinate bounds nevertheless exclude both type alternatives
on the entire prescribed auxiliary box. This deduction uses only exact
rational comparisons of saved endpoints. No reference, polynomial,
primitive, source root or scalar budget is evaluated again.

## 1. A necessary sign before the final external coordinate

Use the original reference chart with first flag \(\alpha=1\),
second flag one, and third flag \(\beta\in\{0,1\}\). The
[reference theorem](research_mixed_second_selected_reference_curve.md)
and [exact canceled maps](research_mixed_second_selected_canceled_rational_transport.md)
identify the original outgoing retained coordinate by
\[
                       B_\beta(W)=e^{-2\pi i b_*}.
 \tag{1}
\]
Every actual ordinary reference has
\[
 \Re b_*\in(.267,.433)\quad(\beta=0),\qquad
 \Re b_*\in(.24,.36)\quad(\beta=1).
 \tag{2}
\]
Both intervals lie strictly between zero and one half. Therefore
\[
 \Im B_\beta(W)
       =-e^{2\pi\Im b_*}\sin(2\pi\Re b_*)<0.
 \tag{3}
\]
This necessary sign is independent of the next external type and of
the remaining word length. It holds whenever \(m\ge4\) in the
original second-selection setting.

The [saved shifted diagnostic](../repro/results/research-mixed-second-selected-shifted-reference-diagnostic.json)
contains completed full-rectangle enclosures for both `B0` and `B1`.
Their imaginary lower endpoints are strictly positive. These are the
stored directed rational endpoints of `full_value`, obtained from the
proved direct and mean-value enclosures. They bound all \(W\)'s in
the image of the same prescribed box
\[
 \xi\in[115337/512000,57677/256000]
       +i[8919/256000,279/8000],
 \qquad a_{18}=001111101111010111.
 \tag{4}
\]
The [saved-endpoint checker](../experiments/check_mixed_second_selected_saved_reference_exclusion.py)
checks these two exact strict inequalities and records their rational
values. Thus (3) and the saved bounds are incompatible for either
\(\beta\).

**Proposition 1.** The entire box (4) contains no actual reference
of the prescribed second-selection prefix, for either third type and
any admitted suffix.

The completed \(B_\beta\) maps already supply the contradiction.
No enclosure of the final external shape \(C_\beta\), nor any
admission through its typed filters, is needed to exclude a point
violating (3). At an actual reference every original denominator is
regular, so the exact canceled rational identities apply. This does
not assert that every point of the broader auxiliary chart is an
actual word reference.

This is a separate proof status derived from saved data. It does not
rewrite the original diagnostic's two `inconclusive` outcomes. No
scalar sign follows from this excluded box, and no replacement
diagnostic point is selected by this note.

## 2. The final derivative guard was unnecessarily conservative

The same saved record identifies the two stopping expressions as the
derivative denominator products of \(C_0\) and \(C_1\).
Their recorded radial modulus balls did not have positive lower
endpoints. However, the saved complex rectangles themselves already
exclude zero: the entire real interval of the first is negative,
and the entire imaginary interval of the second is negative.

For real intervals \(I=[l,r]\), put
\[
 d(I)=\max(0,l,-r).
 \quad\text{Then}\quad
 |x+iy|\ge\max\{d(I),d(J)\}
                   \quad(x\in I,\ y\in J).
 \tag{5}
\]
The checker evaluates the right side using exact saved rational
endpoints and verifies it is positive in both cases. In addition,
the two individually separated factors in each derivative denominator
give the positive pointwise lower bounds
\[
 \begin{split}
 |D_{33}^2D_{34}^2|
 &\ge\frac{31265543203252460797129721291185489}{18014398509481984},\\
 |D_{48}^2D_{49}^2|
 &\ge\frac{400032683734846533672225797599641489}{4294967296}.
 \end{split}
 \tag{6}
\]
These are products of the saved factor-modulus lower endpoints,
with the exact recorded multiplicities. They require no new
polynomial or interval evaluation.

The failed radial guard therefore detected neither an actual
denominator zero nor even a rectangle containing zero. It was a
conservative sufficient test that lost a separation visible in the
coordinate intervals. This did not turn an invalid result into a
valid one; it prevented the diagnostic from proceeding. A future
reviewed evaluator can use coordinate separation, or a factored
reciprocal bound, while preserving the original domain checks.
No frozen evaluator is modified here.
