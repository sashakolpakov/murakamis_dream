# A fixed saved-only comparison for the incoming-height connector

Protocol, 7 November 2026. This proposes one separately reviewed
completion of the remaining right join, using only the already saved
whole-cell root boxes and action lower bounds. No root, Hessian,
response derivative, inclusion, action or dilogarithm is reevaluated.
No numerical trial is authorized before root and independent peer
static review, a frozen manifest, and the root's sole execution.

## 1. The complete source and the proposed comparison

Use the literal \(N\)-scaled vertical integral of
[the generalized connector theorem](research_mixed_transformed_vertical_connector.md),
with its complete \(U_{0,N}C_{1,N}\), all rows, both parities and
ordinary/outgoing derivatives. Its explicit whole-source ceiling is
\[
 \begin{split}
 V_d(R)&=B_0+\max\left\{d_0+f(d/2-\beta(R))+E(d),d+1/3\right\},\\
 B_0&=1549/1500,\quad d_0=7/40-3/512+73/125,\\
 f(u)&=u/4+\max\{u^2,(u-1/10)^2\}/20,\\
 E(d)&=\sqrt3\sinh^2(d/2)/(2\pi),\qquad
 \beta(R)=\tfrac12\log\frac2{1+R^2}.
 \end{split}                                                     \tag{1}
\]
The theorem applies for \(0\le d\le1/2\), \(0\le R\le1\), at
\(a=1/2+ih\), \(-d/(2\pi)\le h\le0\). Its \(B_0\) cap input
is the negative-radius/far-half estimate; it does not assume a whole
unit-disk cap bound at every angle.

For the actual half-chain input \(c\), retain the original first
attached leg \(a(c)\), last leg \(q(c)\), and absolute pre-Gram action
\(\mathscr P(c)\). These are the same original sheet as in the
[completed two-remainder theorem](research_mixed_three_four_following_remainder_gaps.md).
Define
\[
 d(c)=\max\{11/50,-2\pi\Im a(c)\},\qquad
 R(c)=e^{2\pi\Im q(c)}.
 \tag{2}
\]
The original fixed pair height obeys
\(-2\pi h_{\rm pair}<11/50\). Therefore, when \(\Im a(c)<0\) and
\(d(c)<1/2\), (1) bounds the full vertical join from
\(1/2+i\Im a(c)\) to \(1/2+ih_{\rm pair}\), in either orientation.
It retains the original fixed complementary path and the additional
join needed to reach it.

The only new comparison is
\[
              \Re\mathscr P(c)-V_{d(c)}(R(c))>0.
 \tag{3}
\]
No old remainder estimate is divided by a source value or transferred
to a different path without (1).

## 2. Why the full boundary circles suffice

Use the same full reduced disks \(P_3,P_4\) as the previous cover.
The original sheet is holomorphic near them. Suppose their boundaries
satisfy \(\Im a<0\) and \(-2\pi\Im a<1/2\). Harmonic maximum and
minimum principles extend both strict inequalities to the disks.
The outgoing last leg already lies in \(O_4\) on this full sheet.

The connector deficit
\[
                  D(c)=V_{d(c)}(R(c))-\Re\mathscr P(c)
 \tag{4}
\]
is subharmonic on a neighborhood of either disk satisfying these
strict guards. Here is the full elementary verification. The function
\(d(c)\) is the maximum of a constant and a harmonic function, so
is subharmonic. If \(h=\Im q(c)\), then
\[
 b(h)=\beta(e^{2\pi h}),\quad
 b''(h)=-8\pi^2e^{4\pi h}/(1+e^{4\pi h})^2<0.
 \tag{5}
\]
Thus \(-b(h(c))\) is subharmonic, and so is
\(u(c)=d(c)/2-b(h(c))\). On the admitted range,
\(-7/20\le u\le1/4\). Each quadratic branch defining \(f\) is
convex, and its derivative is respectively \(1/4+u/10\) or
\(1/4+(u-1/10)/10\), both at least \(41/200>0\).
Their maximum \(f\) is consequently convex and increasing there.
Therefore \(f(u(c))\) is subharmonic. Also \(E(d)\) is convex
and increasing for \(d\ge0\), so \(E(d(c))\) is subharmonic.
Both branches inside the maximum in (1) are now subharmonic, as is
their maximum. Subtracting the harmonic \(\Re\mathscr P\) proves
the assertion about (4). The usual composition theorem applies on
an open interval containing each compact actual range; the strict
guards and \(\beta<7/20\) supply this room.

The same formulas show that \(V_d(R)\) is increasing in each of
\(d,R\) on the admitted range: \(f,E\) are increasing and \(\beta\)
decreases with \(R\). Thus a cell upper bound on \(d\) and \(R\)
is sufficient. If every boundary cell proves a positive lower margin
in (3), a finite positive minimum exists without computing its value.
The maximum principle for (4) proves that margin on both full disks,
and hence all four clipped following domains. This is a complete-source
connector upper bound. It does not by itself evaluate the remaining
central Gaussian or the next Fourier observation.

## 3. Fixed saved input and full cell inventory

Read only the completed saved-response result
`repro/results/research-mixed-three-four-following-saved-response-attempt01.json`,
SHA `5bc3e5ff76ab5371e76bddb8d8fc32512ef16d9571d1991fb0c5f57dd39867c3`,
and its original manifest
`repro/protocols/research-mixed-three-four-following-saved-response.json`,
SHA `84fe02e65cb17575f5016e8d70e67c261b93ea4a65d9992c99f9ccd9cfb92859`.
Retain all 512 cells of each complete circle, in the original order.
No root or parameter grid is changed, and no cell is dropped.

Verify the completed status, all 1,024 positive-cell identifiers,
2,048 positive comparisons, 46 passed checks per cell, zero forbidden
new-evaluation counters, and every bound input hash. The earlier failed
interval-inverse artifact remains unchanged and transitively bound.
The new manifest also binds (1), the actual-sheet/maximum-principle
sources and this protocol/checker. All old protocol, checker and
manifest bytes remain immutable.

Decode each saved real interval from the union of its `lower` and
`upper` displays, including their printed radii. Do not use the coarser
`ball` text or binary64 arithmetic. Use exact dyadic rational upper and
lower endpoints for maxima and recorded one-sided bounds, as in the
reviewed saved-response decoder.

## 4. The only permitted cell calculation

At 256-bit precision, use the saved `decoded_uniform_box` coordinates
in the fixed order \((e,a,u,t,q)\). Let \(a_-\), \(a_+\) be its
outward imaginary endpoints for \(a\), and let \(q_+\) be the outward
upper imaginary endpoint for \(q\). Define outward
\[
 \Delta_k=\max\{11/50,\operatorname{upper}(-2\pi a_-)\},
 \qquad R_k=\operatorname{upper}(e^{2\pi q_+}).
 \tag{6}
\]
The checker takes exact dyadic rational upper endpoints for the two
`upper` operations. Require \(a_+<0\), \(\Delta_k<1/2\), and
\(1/2<R_k<1\), retaining every failed guard. These checks prove the
boundary assumptions in Section 2; they are not guesses from the
typed containing rectangles.

Read the saved full-cell `real_initial` margin interval, which already
encloses \(\Re\mathscr P-7/4\) on the entire cell. Add \(7/4\) and
retain its outward lower endpoint \(P_{-,k}\). Do not reevaluate its
midpoint action, its response, or its transport debit. Evaluate (1)
once at \((\Delta_k,R_k)\), retaining both branches and both squares
in the maximum. Take an outward rational upper bound \(V_{+,k}\).
The saved-only certificate for this cell is the rational lower bound
\[
                         m_k=P_{-,k}-V_{+,k}.
 \tag{7}
\]
A cell is positive only if all guards passed and \(m_k>0\).
Otherwise its result is failed or inconclusive and remains recorded.
A nonpositive lower bound in (7) does not prove that the true action
comparison fails. No different height, radius, estimate or subdivision
is tried for that cell. Every remaining original cell is processed.

This performs only interval decoding, exact arithmetic, the elementary
exponential/logarithm/square-root/hyperbolic functions in (1),(6), and
the fixed comparison (7). It performs no new root proposals, inclusions,
Hessians, inverses, response derivatives, actions or dilogarithms.

## 5. Exclusive output and interpretation

Checker: `experiments/check_mixed_three_four_following_saved_connector.py`.
Manifest: `repro/protocols/research-mixed-three-four-following-saved-connector.json`.
Output: `repro/results/research-mixed-three-four-following-saved-connector-attempt01.json`.

Freeze all dependencies and actual root/peer static approvals before
execution. Save each original identifier, decoded heights/action interval,
all guards, both exact upper parameters, beta and u, both quadratic
squares, hyperbolic term, both ceiling branches, rational action lower,
rational ceiling upper and margin lower. Retain exceptions, the complete
and unprocessed inventories, and zero counters for all forbidden new
calculations. There is one exclusive output, no overwrite, retry,
refinement or automatic replay. Rehash every binding and manifest after
the run; changes invalidate it.

Only 1,024 positive cell results permit a full-disk connector conclusion.
Any needed theorem assembling this new join with the already proved
left/right paths must still preserve their exact source, orientations,
fixed-base holomorphic parameter scope and normalization. In particular
the next two-sector Fourier observation is not inferred by this check.
