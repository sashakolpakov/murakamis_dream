# One-box evaluation of the four next-four left-row corners

Research specification, 6 November 2026. This records the proposed
single diagnostic for the four sufficient lower bounds in the
[corner-reduction theorem](research_mixed_selected_four_left_row_corners.md).
It establishes no corner sign and authorizes no parameter cover.

Use the actual first-four/next-four reference conventions, \(H=.01\),
and the own-four rational maps and necessary filters of the
[frozen next-four half-row diagnostic](../experiments/diagnose_mixed_four_four_half_row_budget.py).
Its pure reference function and centered original primitive are reused
unchanged. Its half-row scalar inspection routine is not called.
In particular the outgoing map and next-external denominator have
the own-four powers, all original restrictions on the same auxiliary
parameter remain, and coordinate intersections preserve every actual
reference in the input box.

For \(a_0=1/8\), \(s_*=x_*+ih_s\), and
\(\epsilon,\eta\in\{11/50,9/20\}\), evaluate exactly
\[
 \begin{split}
 K_*&=-3\Re g(s_*)+3\Re g(a_0)-2\pi H(x_*-a_0),\\
 I_\epsilon&=\Re\{g(s_*+\epsilon+iH)-g(a_0+\epsilon+iH)\}
                                      -2\pi\epsilon h_s,\\
 O_\eta&=\Re\{g(s_*+\eta+ih_b)-g(a_0+\eta+ih_b)\},\\
 D_{\epsilon,\eta}&=K_*+I_\epsilon+O_\eta.
 \end{split}
 \tag{1}
\]
The minimum of the four values is a lower bound for the pointwise
\(B_0-B_L\) comparison, by the separate concavity theorem.
Their signs must be tested with lower endpoints.
The unchanged outgoing halfweight cancels between the two profiles;
the own-four factorial and both parts of the original incoming chirp
remain explicitly in (1).

Every argument rectangle must lie strictly in \(0<\Re w<1\).
The [reviewed centered enclosure](research_mixed_centered_primitive_enclosure.md)
then encloses the original primitive by
\[
 g(W)\subseteq g(w_0)+\Log(1-e^{-2\pi iW})(W-w_0),
 \tag{2}
\]
with the original dilogarithm point value at the exact dyadic center.
All constants are formed after setting 160-bit precision. A nonfinite
enclosure is inconclusive, never a sign certificate or a new reference
exclusion.

The single box is the same inherited depth-18 box fixed in
[the next-four half-row evaluation specification](research_mixed_selected_four_four_half_row_evaluation.md):
\[
 \begin{gathered}
 \texttt{001111101111010111},\\
 \Re u\in[115337/512000,57677/256000],\qquad
 \Im u\in[8919/256000,279/8000].
 \end{gathered}
 \tag{3}
\]
It is selected from the completed central record solely by saved
metadata: maximal accepted depth, then lexicographically first.
The diagnostic verifies that selection and reconstructs the box
exactly from the original root. It does not reevaluate a central
or half-row scalar bound.

The new evaluator returns the unchanged necessary-reference
exclusions, or all four corner enclosures. Its accepted status
requires every exact rational lower endpoint to be strictly positive.
The record additionally reports nonnegativity and comparison with
the optional candidate \(1/2000\), which is not needed to deduce
\(B_L\le B_0\). It saves \(K_*\), both \(I_\epsilon\), both
\(O_\eta\), reference data and every directed rational endpoint.

Only one diagnostic call on (3) is proposed. There are no additional
boxes, subdivisions, root proposals, quantum-source evaluations,
automatic retries or precision changes. The record binds the corner
proof, this specification, the frozen next-four helper and its
original branch/map providers, the centered-primitive proof, the
completed central record and its dependencies, and the new diagnostic
code before and after evaluation. A fresh output path is required.

This necessary-superset box need not contain a realized word.
A successful one-box diagnostic would not establish the uniform
four-corner sign. A failed corner lower test would not refute
domination by the full main contour.
