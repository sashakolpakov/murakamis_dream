# Two complete canonical terminal families on the type-four input disk

Research note, 6 November 2026. The fixed correlated certificate gives
uniform enclosures of both canonical terminal families on the complete
type-four input disk. This is a reference-coordinate theorem. A uniform
finite terminal-source estimate still requires its own phase and source
comparisons.

## 1. The recorded complete families

Use the original five variables \(q=(e,\xi,t,a,s)\) and the unscaled
gradient \(f(q;b)\) of
[the correlated primitive certificate](research_mixed_terminal_correlated_affine_family_certificate.md).
The input type is \(\beta=1\), while the terminal type is
\(\epsilon=0\) or \(1\). Put
\[
 b_0=\frac3{10}-\frac{13}{250}i,\qquad
 D_4=\left\{b:|b-b_0|\le\frac8{125}\right\},\qquad
 \rho=\left(\frac1{500},\frac1{1000},\frac1{200},
                    \frac1{200},\frac1{100}\right).
 \tag{1}
\]
For each \(\epsilon\), let \(q^0_\epsilon,u_\epsilon\) be the
**exact rational pairs** in the fields `center` and `response_exact`
of the corresponding case \((1,\epsilon)\) of the
[completed record](../repro/results/research-mixed-terminal-correlated-affine-family.json).
These are case indices 2 and 3. They are the unchanged saved center
and response proposal of the preceding affine attempt, not new
solutions or newly fitted responses.

**Theorem 1.** The original canonical holomorphic branch on \(D_4\)
satisfies, for both terminal types,
\[
 \left|q_{*,i}(b)-q^0_{\epsilon,i}
                  -u_{\epsilon,i}(b-b_0)\right|<\rho_i
       \quad(b\in D_4, 1\le i\le5).
 \tag{2}
\]
The enclosure includes the disk boundary. Shared dependence on the
single complex parameter \(b-b_0\) is retained in (2); replacing it
by five independent input parameters is unnecessary.

The source record has SHA256
`51b702aa6ea44aa5891bc1146a7d5c0d22686cd814f9bbe5d9c4c63b9a16f9e1`.
It retains all sixteen prescribed tests, including failures. Both
\(D_4\) cases pass at multipliers 1 and 2. We use multiplier 1 in (1).
The two multiplier-one weighted contraction bounds are respectively
less than \(435/1000\) and \(436/1000\), and each of the five inclusion
margins is strictly positive. All four \(D_3\) tests per terminal type
remain inconclusive; a contraction bound below one by itself does
not replace the missing inclusion inequalities.

For (2), apply Theorem 1 of the correlated certificate to the eleven
original shared log arguments. The recorded strips are strictly
regular on the full correlated tubes, and the saved certified center
root lies in each central error polydisk. The new fixed points
therefore coincide with the canonical branches first by local
implicit uniqueness, then throughout the connected disk by analytic
continuation. Full-tube containment in the old common coordinate
rectangle is not a premise. The original log strips, central-root
containment, and all strict inequalities are premises and remain
checked separately.

The fixed run used 44 center logarithms, 44 center cotangents, 44
affine curvature sine bounds, and 176 full-tube curvature sine
bounds. It made no new inverse or response proposal, root solve,
action evaluation, finite-source evaluation, subdivision, precision
retry, or radius change. The 36 recorded input bindings are unchanged.

## 2. A sharper componentwise error bound from the same witnesses

Here is a general consequence after a candidate has been certified.
Let \(R\ge0\) and \(E\ge0\) be its residual vector and entrywise
Jacobian-error majorant, with
\[
 R+E\rho<\rho,\qquad
 \eta=\max_i\frac{(E\rho)_i}{\rho_i}<1.
 \tag{3}
\]
The already established root lies in this same tube. Writing
\(w_i=|q_{*,i}(b)-q^0_i-u_i(b-b_0)|\), the exact preconditioned
fixed-point identity and integration along the segment inside the
tube give
\[
 w\le R+Ew.
 \tag{4}
\]
The weighted contraction bound implies that
\[
 (I-E)^{-1}=\sum_{n\ge0}E^n\ge0,\qquad
 w\le z:=(I-E)^{-1}R<\rho.
 \tag{5}
\]
For the last strict inequality, multiply
\((I-E)\rho-R>0\) by the nonnegative inverse, whose diagonal is at
least one. All statements are componentwise. This is a refinement
of a previously certified root enclosure, not a new evaluation of
the gradient or a new choice of error-radius candidates.

The vector \(z\) can be computed by exact rational Gaussian
elimination and checked by the identity
\[
                 (I-E)z=R,\qquad 0\le z<\rho.
 \tag{6}
\]
The saved-data checker below performs this calculation for the two
certified multiplier-one families. In particular (2) may replace
its right side by the corresponding posterior radius vector in
the checker output, with a non-strict inequality. An independent
Cartesian consequence is
\[
 \begin{split}
 |\Re q_{*,i}(b)-\Re q_i^0|&\le r|u_i|+z_i,\\
 |\Im q_{*,i}(b)-\Im q_i^0|&\le r|u_i|+z_i,
 \qquad r=8/125.
 \end{split}
 \tag{7}
\]
The affine form with the shared parameter remains the stronger
information.

For an uncertified \(D_3\) candidate, the algebraic vector
\((I-E)^{-1}R\) is still well defined when its saved weighted
contraction bound is below one. The checker retains these eight
vectors only as radius diagnostics. It does **not** infer (4), a
canonical-root enclosure, or a new successful candidate there:
the required prior tube inclusion has not been established.

## 3. Exact saved-data verification and serialized intervals

The standalone checker is
[check_mixed_terminal_correlated_affine_family_record.py](../experiments/check_mixed_terminal_correlated_affine_family_record.py).
Its output is the fresh file
`repro/results/research-mixed-terminal-correlated-affine-family-saved-audit.json`.
It imports only the standard library. It binds the complete record,
its frozen driver and proof, the preceding affine record, the original
canonical center record and audit, and every inherited input before
and after checking. Exact case, center, inverse, response, radius,
primitive-argument, and central-root-box associations are retained.

The checker first reproduces all original rational summands of the
residual and error-matrix bounds, all sixteen contraction and
inclusion tests, and their exact recorded success statuses. The
analytic center log/cotangent values and positive sine intervals
are source-bound inputs; no analytic function is evaluated again.

It then performs a conservative independent rational reconstruction.
The original chirp uses the certified interval for \(\pi\) saved in
the canonical center record. The five gradients, point Jacobian,
preconditioned center/linear defects, and center error matrix are
recombined with exact interval arithmetic, taking the outward hull
with their separately saved enclosures. No containment relation
between independently serialized operands is assumed. Modulus bounds
are rebuilt from the resulting Cartesian intervals with exact integer
square roots, and curvature bounds use

\(\pi_{\rm upper}^2/(\sin_{\rm lower})^2\), enlarged to include the
saved bound. Final residual and matrix entries are rounded upward
to dyadic rationals of denominator \(2^{240}\).

These reconstructed \(R,E\) can only increase the original
majorants. The checker requires all sixteen success/failure outcomes
to remain unchanged, and in particular rechecks (3) for both
multiplier-one \(D_4\) families. It records the maximum enlargement.
Only those reconstructed majorants are used for the posterior
systems (6). Exact rational solutions are retained without truncation;
decimal displays are informational only.

No uniform phase gap, nonzero scalar coefficient, finite-word
realization of every input, or volume-conjecture theorem follows
from this coordinate certificate alone. Source comparisons may
still require the smaller actual geometric input region, even
though the canonical family is enclosed on the full disk.
