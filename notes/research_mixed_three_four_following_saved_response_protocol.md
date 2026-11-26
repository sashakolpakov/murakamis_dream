# Saved-only completion of the following boundary response

Protocol, 7 November 2026. The sole frozen full-circle attempt is
preserved as failed/inconclusive. Every one of its 1,024 cells completed
both prescribed root inclusions and the midpoint action evaluation, but
stopped when the direct inverse of a wide interval Hessian could not be
certified. The present separately reviewed computation uses those saved
certificates and values. It does not repeat any root proposal, inclusion,
Hessian, action, or dilogarithm evaluation.

No execution is authorized until the root and an independent peer have
reviewed this protocol and its standalone checker and a new frozen
manifest has been inspected. Only the root may perform the single new
saved-only completion. No old file, status, manifest, or result is changed.

## 1. Fixed saved inventory and the failed step

Input: `repro/results/research-mixed-three-four-following-boundary-cover-attempt01.json`,
SHA `e2a6f208dd59f9e2d8044619aa70532c7945972b8d499af3e00880f9e580449b`.
Its original manifest is
`repro/protocols/research-mixed-three-four-following-boundary-cover.json`,
SHA `d7e9e6a096e4ce5dc77858691a90b257f842a42910603f74f3d15a6e20a46405`.

Retain exactly the two full reduced circles and all 512 closed cells on
each, in the original order of
[the full-circle protocol](research_mixed_three_four_following_boundary_diagnostic_protocol.md).
There is no clipping, subdivision, discarded failure, replacement center,
changed radius or new proposal. The saved report contains exactly 24,576
proposals, 1,024 midpoint inclusions, 1,024 parameter inclusions, 1,024
action evaluations, and zero comparisons. Its original failed verdict
remains an input fact, not a successful cover assertion.

Before using any cell, check the complete saved inventory and absence of
hash invalidation, every original successful check, both inclusion row
inventories, and the recorded failure precisely at
`inverse_cell = cell_jac.inv()` with `ZeroDivisionError: matrix is singular`.
Check all required saved action, radius, beta, parameter, coordinate and
rational-inverse fields are present. Bind the original checker/protocol,
its manifest, all 44 bound input files, the primary author/replay records
and every inherited dependency transitively. The two actual source bounds
are still the complete initial-interval theorem and the sharp radial
complement theorem, with the same absolute pre-Gram action and constants.

## 2. Safe decoding of saved bounds

Use 256-bit ball arithmetic throughout. A saved real interval has a
`lower` and an `upper` display. These strings may themselves contain
printed `+/-` radii; those radii must be parsed and retained. Read each
string as an outward Arb ball, then take their interval union. Do not
read only the midpoint, use a binary64 conversion, or replace the interval
by its much coarser `ball` display. The union encloses the full original
saved interval, including any outward decimal-display rounding.

For one-sided upper bounds use the upper endpoint of this decoded union.
When maxima are needed, convert that endpoint to its exact dyadic rational
and compare these rational numbers. This is only outward decoding and
finite arithmetic on the saved bounds. It neither narrows a saved box nor
recomputes an original mathematical value.

Decode the whole-cell root boxes and the external-cell enclosure this
way. Read every entry of the saved rational inverse directly as its exact
rational real and imaginary components. Recheck, after outward decoding,
that every saved contraction row upper bound is strictly below one and
each saved image-radius upper bound is below its original prescribed
radius, for both inclusions. Retain any failure caused by display
widening. The original geometry checks remain required; the decoded
arguments used below must also stay in the same elementary logarithmic
strips and outgoing radius range. No radius or box is changed.

## 3. A response bound from the saved contraction

Fix a cell and any actual external point \(c\) in it. Let \(H\) denote
the original five-variable Hessian at its certified critical point, and
let \(Y\) be the cell's exact saved rational midpoint inverse. The saved
parameter-inclusion proof bounds the row norms of
\[
 E=I-YH,
 \qquad \sum_j|E_{ij}|\le k_i,\qquad
 k=\max_i k_i<1.
 \tag{1}
\]
Here every \(k_i\) is the safely decoded outward upper bound of the
corresponding saved `derivative_row`, not a recomputed Hessian quantity.
Let the last coordinate be \(z\), and put
\[
 m=\max_j|Y_{jz}|,\quad
 \gamma=\frac{2\pi i}{1-e^{-2\pi iz}e^{-2\pi ic}}.
 \tag{2}
\]
All entries of \(Y\) are fixed exact rationals; \(m\) is bounded
outward using only them. Differentiating the original equations gives
\(Hv'=-\gamma e_z\). Multiplication by \(Y\), without an interval
matrix inverse, gives
\[
 v'=-\gamma Ye_z+Ev',\qquad
 \|v'\|_\infty\le\frac{|\gamma|m}{1-k}.
 \tag{3}
\]
Consequently the last derivative has the uniform complex-disk enclosure
\[
 \boxed{\quad
 z'(c)=-\gamma Y_{zz}+\varepsilon(c),\qquad
 |\varepsilon(c)|\le
 r_{\rm resp}:=\frac{|\gamma|k_zm}{1-k}.
 \quad}                                                        \tag{4}
\]
The denominator in (2) is checked away from zero on the saved uniform
boxes. Formula (4) follows from the already certified contraction and
does not assume that direct interval Gaussian elimination succeeds.
No new root or Hessian values are used.

## 4. The same two margins, with signed response transport

Let \(t,z\) denote the fourth and fifth saved uniform coordinate boxes.
On their original branches compute only the elementary quantities
\[
 \begin{split}
 p_z&=g'(t+z)-g'(z)
       =\Log(2\sin\pi(t+z))-\Log(2\sin\pi z)-i\pi t,\\
 R&=e^{2\pi\Im z},\quad
 \beta=\tfrac12\log\frac2{1+R^2},\\
 B_h&=(-6/25+\beta/10)\frac{-2\pi R^2}{1+R^2}.
 \end{split}                                                     \tag{5}
\]
For the original circle center \(c_\nu\), its angular derivative is
exactly \(c'(\theta)=i(c(\theta)-c_\nu)\), so the saved external-cell
box gives its enclosure without evaluating a new angular grid.
Use the saved enclosure of \(\omega=\pi/512\) for the halfwidth.

For \(A_0=p_z\) and \(A_+=p_z+iB_h\), the exact real margin derivatives
are \(\Re[A_j z'(c)c'(\theta)]\). Retain the signed central response
in (4). A valid derivative enclosure is
\[
 \Re[-A_j\gamma Y_{zz}c'(\theta)]
 +[-|A_j|\,|c'(\theta)|\,r_{\rm resp},
     |A_j|\,|c'(\theta)|\,r_{\rm resp}].
 \tag{6}
\]
This uses a complex-disk error directly and introduces no artificial
Cartesian-square \(\sqrt2\) loss. All interval dependencies may be
forgotten outward; none is assumed independent in an equality.

The midpoint bare action and outgoing beta/radius are **read from the
saved report**, including their full lower/upper enclosures. Form only
\[
 m_{0,k}=\Re P_k-7/4,\qquad
 m_{+,k}=\Re P_k-\left(17539/9600-23/64000
                          -6\beta_k/25+\beta_k^2/20\right).
 \tag{7}
\]
No primitive, action, or new midpoint radius is evaluated. Enlarge each
midpoint margin interval by \([-\omega L_j,\omega L_j]\), where
\(L_j\) bounds the absolute value of (6). Record the full resulting
cell interval and its strict positive, strict negative or inconclusive
verdict. Decode failures and nonpositive results are retained; all
remaining original cells are still attempted once.

If every cell has both positive margins, the exact original-sheet
harmonic/subharmonic argument of the full-circle protocol proves the
two margins on both full reduced disks and therefore all four clipped
following domains. Only the two named complete prefix remainders are
paid. No full prefix packet, remaining plateau/taper estimate, next-word
nonzero observation, attachment-sector deletion or knot-family theorem
is inferred. The earlier direct-inverse attempt remains failed.

## 5. One separate output and no hidden replay

Checker: `experiments/check_mixed_three_four_following_saved_response.py`.
Manifest: `repro/protocols/research-mixed-three-four-following-saved-response.json`.
Output: `repro/results/research-mixed-three-four-following-saved-response-attempt01.json`.

The standalone checker imports no old checker and defines no original
gradient, Hessian, Newton iteration, matrix inverse, action or
dilogarithm function. Its permitted work is saved-data/provenance
validation, safe interval decoding, exact rational arithmetic, elementary
scalar/complex functions in (2) and (5), and the fixed calculations
(1)--(7). No preliminary numerical trial of these operations is allowed
before review and the root's sole execution.

Save every original identifier, decoded bounds actually used, all five
saved contraction upper bounds, \(k,m,Y_{zz}\), \(\gamma\), the response
center/radius, both derivative enclosures, both midpoint margins and full
cell margins, every check/exception, complete and unprocessed inventories,
and input hashes. Rehash all bindings and the new manifest at the end;
changes invalidate the new report. Keep explicit zero counters for new
roots, inclusions, Hessians, inverses, actions and dilogarithms. Open the
new fixed output exclusively. No failed or inconclusive cell may trigger
a retry, refinement or different response estimate in this protocol.
