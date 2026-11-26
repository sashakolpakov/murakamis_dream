# A saved own-four margin for the Fourier right-cap last row

Fixed saved-data protocol, 7 November 2026. This extracts a stronger
margin from the completed ordinary last-row replay. It evaluates no
analytic function, source bound, root or gain. The numerical premise
below remains conditional until the prescribed checker has passed.

## 1. The exact old deficit and the quantitative consequence

Use the original own-four branch on each of
\(K_3\times K_3,K_3\times K_4,K_4\times K_4\), both orientations,
and the four revived carriers. The domains, charts, primitive and
allocations are exactly those of the
[height-chart design](research_mixed_typed_last_row_height_charts.md).
In the notation where \(Q_1\) already contains \(-g(a)-g(q)\), put
\[
 F=Q_1-\frac{\eta}{2}g(a)-\frac12g(q),\qquad
 B_F=\Re F_*+\Re F_a\,\delta x+\Re F_q\,\delta z
            -\kappa(\delta x^2+\delta z^2),\qquad
 \kappa=\frac1{2500000}.
 \tag{1}
\]
The complete real last-row rate is the maximum of
\[
 R_{vw}(x,z)=-2\pi v h_a+2\pi w h_q
      -\frac{\eta}{2}\Re g(x+ih_a)-\frac12\Re g(z+ih_q),
 \qquad v,w\in\{0,1\}.
 \tag{2}
\]
The target square remains \(P^2=[11/50,9/20]^2\).

The [completed replay](../repro/results/research-mixed-typed-last-row-support-replay.json)
contains 72 chart summaries. Its fixed ordering puts the 36 own-four
charts at indices \(36,\ldots,71\). The pinned writer's
replay_all routine takes the maximum of the recomputed upper bound
over every saved leaf, after checking every original carrier and target
envelope in both orientations. The resulting maximum_upper field is
therefore an upper enclosure for the entire chart deficit
\(R_{vw}-B_F\). It is not a sampled trial value. The new checker inherits
this reviewed analytic meaning; it does not repeat that replay.

**Fixed premise.** Each of these 36 saved summary upper endpoints is
strictly less than \(-1/50\).

If the premise holds, the exact closed charts cover the full ordinary
boundary of all three own-four products. The local input/root swap
covers the omitted homotyped boundary slot, since both orientations
were included. The quantitative reference-boundary principle,
[typed envelopes (10)](research_mixed_typed_last_row_envelopes.md),
then gives
\[
 \max_{K\times P^2,v,w}(R_{vw}-B_F)
 \le\max\left\{-\frac1{1000},-\frac1{50}\right\}
 =-\frac1{1000}.
 \tag{3}
\]
The first constant is the original matched entropy gap. In particular,
the boundary reserve \(1/50\) is not asserted throughout the interior.
The principle uses the original locally open retained-coordinate map
and its strict horizontal Hessian; it does not differentiate the
maximum over carriers or targets.

## 2. Transfer to the actual bare Fourier last row

For the actual last-four Fourier reference with incoming type
\(3+\eta\), the
[correlated annulus completion](research_mixed_fourier_right_cap_annulus_completion.md)
places its auxiliary outgoing exterior leg in \(K_3\). Thus (3)
applies to the original coupled reference for either incoming type.
The original logarithmic lifts identify the branches.

Let \(H(q)=g(q)/2+\ell_q(x_0)\). The bare phase is
\(\mathscr F=F+H(q)\). Its outgoing derivative vanishes at the
actual reference, so \(F_q=-H'(q_*)\); its incoming derivative is
unchanged. The exact rate identity, also for the true last row, is
\[
 \mathcal T_\eta(1;x,z)-B_{\rm F}
 =\max_{v,w}\{R_{vw}(x,z)-B_F\}
 +\Re\{H(q)-H(q_*)-H'(q_*)\delta z\}.
 \tag{4}
\]
Here \(q=z+ih_q\) and
\[
 \mathcal T_\eta(1;x,z)
 =2\pi(-h_a)_+-\frac{\eta}{2}\Re g(x+ih_a)+\Re\ell_q(x_0),
 \tag{5}
\]
because the actual outgoing height \(h_q<0\).
Equation (4) concerns the literal complete row rates, not division
by a finite outgoing weight.

The [allocation-curvature theorem](research_mixed_fourier_allocation_curvature.md),
Lemma 2, bounds the last term in (4) strictly by \(33/70000\),
uniformly on \(P\). Consequently a successful check proves
\[
 \boxed{\quad
 \mathcal T_\eta(1;x,z)
 < B_{\rm F}-\frac{37}{70000}
 < B_{\rm F}-\frac1{2000}.
 \quad}
 \tag{6}
\]
Together with that theorem's two cut gaps \(1/35000\), this pays all
three real rows of the
[bare inner-contour theorem](research_mixed_fourier_right_cap_bare_inner_contour.md).
It keeps the old \(\kappa\), both original marginals before Fourier
stationarity, and every original finite allocation. The same bounds
hold against the weaker plane with coefficient \(\kappa/2\).

This is an inner-index source conclusion on the stated plateau.
The outgoing \(q\)-sum's physical complement, aliases and joins
remain separate. No whole right-cap asymptotic or open-source
noncancellation follows from this extraction alone.

## 3. Fixed standard-library check

The unrun checker is
[check_mixed_fourier_right_cap_last_row_saved_margin.py](../experiments/check_mixed_fourier_right_cap_last_row_saved_margin.py).
Its sole output is the fresh path
repro/results/research-mixed-fourier-right-cap-last-row-saved-margin.json.
It must be invoked with its exact reviewed SHA-256; output creation is
exclusive. It uses only Python's standard library.

The immutable source inputs are:

| Input | SHA-256 |
|---|---|
| Original author attempt 04 | be75ec2a2628d4ae6e594a31ee62ca254788528024d1c27680d63ad86b9f0e46 |
| Completed 320-bit replay | 99d0d67616cfd0272d5ff9139c5e6a70a16fe6da7ef8421e9cd580baa3f0c06e |
| Original replay writer | fa35e484760e8de06ef310b99c99946400559bbfcb7cc566d6aacea03c1ac715 |
| Original certificate proof | 0387a95df2b25fe4d1a32281dad5ab4503b8ada4ad0289eafce125954ed69c1f |

The procedure is fixed as follows.

1. Verify all direct hashes and all 37 dependencies named identically
   by the two original records. Bind them before and after the check.
   Require the original author/replay success, schema, flags,
   precision, target, curvature and zero-proposal/refinement metadata.
2. Reconstruct all 72 chart specifications independently from the
   original typed ordering. Compare every replay domain, including
   all saved trees, witnesses and targets, with its canonical author
   hash. Reconstruct the 71 nonimported dyadic trees with their
   original cyclic split axes and traversal order; verify complete
   unit volume, empty frontier, depths, leaf counts and envelope
   inventory. Chart 18 remains the unchanged imported own-three
   domain, with its original author/replay bindings.
3. Associate all 72 summary indices/specifications/counts with those
   domains and verify the original aggregate inventories. Only for
   the fixed own-four indices \(36,\ldots,71\), parse the saved
   maximum_upper enclosure as exact decimal fractions. A printed
   interval \([m\mathbin{+/-}r]\) is bounded above by the exact
   fraction \(m+r\); no Arb or floating conversion is used.
4. Visit all 36 comparisons \(m+r<-1/50\), retaining every original
   summary string, rational endpoint and pass/fail flag. There is no
   adaptive fallback, changed threshold, source replay or new gain.
   Verify the exact deductions (3) and (6), and the two inherited cut
   margins, only if all fixed checks and input bindings pass.
5. Save complete scope and failure status. A failed comparison or
   malformed association does not certify a gap. Partial evidence
   survives a calculation error or interruption; all conclusion flags
   and gap fields are cleared in that case.

The summary maxima remain inherited analytic enclosures. The fresh
work is exact parsing, tree/provenance association, the 36 rational
threshold comparisons, and the stated rational margin deductions.
The checker does not claim independent validation of the original
root, slope, optimizer or primitive calculations.
