# Independent source and contour audit of the directed-message criterion

The full proof in sections 1–9 of the directed-budget draft is valid at its stated fixed-tree scope. I found no fatal error or missing exponential budget affecting the claimed knot-volume limit or the fixed-disk microscopic profile. The numerical hypotheses are uniform in the tree's degrees and size; the amplitude constants, polynomial factors and sufficiently large quantum level may depend on the fixed tree, its powers, and the compact main-parameter disk. That distinction is essential and is respected by the proof.

The input read here is /private/tmp/md-variable-local-volume-directed-budget.md, SHA256 6e43e9c00ed4ac1899e0dae1ba60b57295801cdfccfa804e33a21df1a0e240fc. This includes the two final typography repairs after the earlier 052c8e version. No mathematical alteration was requested. This audit is a proof read and independent derivation, not an inference from the arithmetic script.

## 1. Actual source, types and arbitrary evaluation root

The theorem concerns the literal ordered all-circle tree with its original signed powers, physical turns, endpoint pattern, disk words and zero-framing normalization. It is not a theorem about arbitrary prescribed polynomials on an abstract tree.

The fixed-basis Frobenius metric is anti-diagonal. After lowering the original operation tensors, its contraction with an actual typed turn is diagonal, with the exact factor \(\gamma_e(s)H_N(s)/W_k(s)\). Thus the closed scalar is a finite sum over the original physical-edge indices. The same finite sum can be evaluated from any vertex. This changes no endpoint word or physical frame and invokes no tangle isotopy. In particular, it does not identify a physical inverse turn with a scalar reversal.

The message recursion retains the original vertex parameter \(\sigma_v=0,\pm s\), and the original closing, framing, opposite-order reference factors and one reduced cut remain outside the root trace. The scalar ledger consequently remains
\[
 A_N(s)=q_N^{[-w(D)-\sum_v n_v]s^2/2}.
\]
No extra root correction is introduced by finite Fubini.

Each outgoing message is a polynomial of degree at most \(N-1\) in \(-2\cos u\): all parent-variable dependence occurs in the single kernel factor \(e_k(-2\cos u)\). The size and depth of the subtree do not enlarge this degree. Its full quotient and repeated-root normal data remain present. Polynomial equivalence of the canonical norm, interval supremum and derivative norm is used only at degree bounded by a fixed multiple of \(N\), with constants allowed to depend on the fixed diagram.

## 2. The new rectangle kernel estimate

The key strengthening over the earlier tiny-disk argument is an estimate relative to the actual conditional phase \(\Re\psi(0,u)\), for the entire physical kernel. This estimate is proved, rather than inferred from the old disk asymptotic.

On the retained interval \(1/5\le k/N\le3/10\), all factors at real \(|a|\le1/8\) are positive. The largest relevant cosine argument is strictly below \(3\pi/5\), so
\[
 r_j>-1/3,\qquad r_j+\cos a>253/384.
\]
The complex denominator stays above \(3/5\) on the stated rectangle. The second logarithmic derivative is bounded by \(9\). Since the first derivative at a real point is real, the first-order contribution to the real logarithm along a vertical segment is zero. Integrating twice gives a quadratic \(b^2\) cost. The stated \(5Nb^2\) bound is conservative; it does not discard a linear imaginary shift of an absolute value.

The retained positive sum at \((0,a)\) has its actual maximum at
\[
 \tan^2(\pi x)=\frac{1}{1+\tan^2(a/2)}.
\]
This point stays in the interior of the retained interval, with a uniformly negative second derivative. Hence its polynomial-times-exponential upper bound uses \(\psi(0,a)\), not an unrelated global maximum. The difference between this real phase and \(\Re\psi(0,a+ib)\) costs at most a constant times \(b^2\).

For \(|t|\ge1/8\), the extra \(6b_0^2\) is absorbed by half the old angular loss. The displayed elementary bounds are sufficient:
\[
 6\,2^{-22}<\frac{1}{500}\sin^2(1/16),
 \qquad 2k_0<\frac1{500}.
\]
For \(|t|\le1/8\), both angular arguments lie strictly inside the old radius-\(1/4\) complex domain. The canonical wire contour and its nonzero amplitude apply there. The complementary indices, including the high ones and their normals, retain their fixed gap: the sum of the two linear ellipse costs, the possible conditional phase displacement, and \(2k_0\) is less than half that gap.

This proves the actual full-kernel estimate (15). No sign condition on an individual high Newton factor is used. The smaller rectangle asymptotic (24) is relative and holomorphic; it is not another absolute source error that must be compared with a filled action drop.

## 3. Phase closure and exact normalization

The child constants \(M_{w,N}(0)\) are divided out exactly. They may be complex and oscillatory, and are not replaced by upper estimates at the complete source. The first vertex supplies the nonzero value needed to start the induction; the same conditional argument then proves it at each successive vertex.

The evenness of the exact kernel and messages is exact. It gives \(E_t(0,u)=0\), and the second-derivative estimate gives
\[
 |E_t(t,u)/t|\le a_v/20.
\]
For retained charges, the fixed-point equation contracts in the radius-\(b_0\) disk because \(t_0+b_0/20<b_0\). Its solutions lie in the smaller disk of radius \(t_0/(19/20)\). The complex parent variable does not invalidate the sign of the saddle height. Writing the saddle as \(-i\ell/(D_v-e)\), with \(|e|\le a_v/20\), bounds its negative imaginary part by the stated \(380/441\) and \(420/361\) multiples of \(\ell a_v/|D_v|^2\).

Differentiating the stationary value gives the displayed Schur formula. The cross derivative has size at most \(a_0/50\), whereas the denominator is at least \((19/20)|D_v|\). Thus
\[
 \frac1{50}+\frac{20}{19\cdot2500}<\frac1{20}
\]
closes the same phase class for every fixed subtree. Charge ordering follows by integrating the negative saddle height. This proves both the first-charge drop bound and the separation of every other retained charge.

The exact normalized logarithms differ from the limiting phases by \(O(N^{-1})\), with fixed derivatives on a smaller compact. These terms belong to the analytic amplitude, or shift a nondegenerate saddle by \(O(N^{-1})\). They are not repeatedly charged as absolute complete-source errors. The nonzero first-charge amplitude contains the nonzero edge, child and Gaussian factors. The original crossing and carrier phases remain in the exact scalar normalization.

All Cauchy uses need nested compacts. The draft states this explicitly. Its strict numerical margins permit a slightly larger initial rectangle, followed by the required smaller rectangles, for the finitely many vertices of the fixed tree.

## 4. Derivation of the complex strip

The degree bound and the real envelope give the Poisson estimate (31). More explicitly, multiply the Laurent polynomial by the appropriate power of the disk coordinate and use the harmonic majorant of its boundary logarithmic bound. At radius \(e^{-|y|}\), the cosine term becomes \(e^{-|y|}\cos t\). Its change is bounded by \(c_v|y|\), while the degree costs at most \(N|y|\). This yields exactly the stated \((1+c_v)|y|\) term.

For \(|t|\ge r_0\), the choice of \(\delta_v\) absorbs this linear term into the available real loss. For \(|t|<r_0\), the local even phase and its Hessian bound give the quadratic estimate (32). Both points stay inside the analytic rectangle. Thus (30) is a consequence of the whole message, not an assumed weighted norm for its coefficients.

Multiplying the exact normalized inputs now gives (38), with
\[
 A_v=\frac2{\pi^2}\left(q_vk_0+\frac12\sum_w c_w\right),
 \qquad B_v=16q_v+|\mathrm{Ch}(v)|.
\]
The elementary inequality \(1-\cos t\ge2t^2/\pi^2\) is applied on the original real interval. No independent subtree volume appears in this bound.

## 5. Full tails, original endpoints and local connectors

I checked the four entries in \(\eta_v\) against separate operations on the actual finite translated-grid trace.

For charges beyond \(L_v=\lfloor t_0|D_v|\rfloor\), completing the square in the real angular variable gives the cost \(C_vy_v^2\). The second branch in the definition of \(y_v\) makes it at most \(t_0|D_v|y_v/4\). Thus the stated tail loss, one half of \(t_0|D_v|y_v\), leaves additional room. The exact coefficient growth of \(U_{\ell-1}(\cos2\pi\sigma)\) is fixed exponential growth in \(\ell\); the extra factor \(e^{-Ny_v}\) makes the tail summable for all sufficiently large \(N\).

At the original endpoints \(\pm\pi\), the third and fourth height constraints bound the linear chirp/finite-charge contribution and the quadratic strip contribution by \(A_v\pi^2/8\) each. The retained endpoint loss \(A_v\pi^2/2\) is therefore conservative. This includes the zero-mode current. It is not legitimate to drop these currents because the chirp is not periodic, and the proof does not do so.

The complement of the central real interval loses \(A_vr_0^2\). On the local vertical connectors, the displayed Young inequality leaves the negative term \(-a_vt^2/8\). If \(z\) is at most the saddle height, its remaining quadratic cost is at most
\[
 \frac{300}{361}\ell z<\frac78\ell z.
\]
Thus each connector has the claimed \(a_vr_0^2/8\) loss. Its points stay inside the rectangle: \(r_0=1/16<1/8\), and the largest retained saddle height is less than \((420/361)t_0<b_0\).

The horizontal saddle has negative real quadratic part and its physical sine factor is nonzero. The latter is small for very long fixed powers, but is a nonzero fixed number; no uniform lower bound in an \(N\)-dependent twist family is asserted.

The retained nonminimal integrals are saddle terms plus an absolute conditional error. The proof correctly does not require a relative approximation at those possibly much smaller actions. The strict inequality \(\beta_v<\eta_v/2\) puts every absolute error below the first charge. Its exact coefficient is one at both level parities. The finite translated endpoints displaced by \(O(N^{-1})\) are harmless because \(y_v\le\delta_v^{\mathrm{in}}/2\), leaving a strip margin; their bounded costs are absorbed in polynomial or fixed factors.

The removability argument is applied to the whole physical trace minus its first-charge expression. Formal vertex parameters can first be taken on collision-free circles, followed by the maximum principle. This retains the normal channel \(\sigma_v=0\) and does not declare individual divided currents removable.

## 6. Outgoing envelopes, root exception and geometry

To regenerate the global outgoing bound, the proof uses the actual fixed-power crossing polynomial, polynomial norm equivalence, Chebyshev folding in the correct quotient, and the full top-coefficient functional. This is a different estimate from the false pointwise comparison for a high-index hub. It retains all repeated-root derivatives.

Division by the nonzero scalar at zero costs at most \(\beta_v\). For \(|u|\ge r_0\), condition (9) absorbs that cost into the difference between \(k_0\) and the chosen outgoing budget. The local phase handles smaller \(u\). Hence the outgoing real and strip bounds close.

At the final root there is no outgoing variable and no need to regenerate a polynomial envelope. The omission of (9) there is legitimate. All conditional estimates still apply because the root has at least one incident edge and \(A_v,B_v>0\).

Restoring the exact constants produces the original joint first-charge stationary equations and their original critical value. It does not sum independent local hyperbolic volumes. The cutoff assumption gives
\[
 \sqrt{d_v^2+n_v^2}=2\pi|D_v|\ge2\pi\,2^{15}>630.
\]
Therefore the established vertexwise geometric completion identifies the selected branch with the original filled knot complement. Its uniqueness on the common small-angular domain identifies the recursively eliminated saddle with that geometric path.

There is one \(N^{-3/2}\) edge factor and one \(N^{3/2}\) trace factor at each respective edge and vertex. Since the graph is a tree, the net power is the original \(N^{3/2}\), with nonzero amplitude. The first coefficient and paired edge insertion have leading value one. The exact scalar and the single reduced-cut factor are retained, so the asserted microscopic ratio and logarithmic volume follow with no extra normalization.

## 7. Independent check of the degree-uniform \(2^{27}\) corollary

Set every nonroot budget to \(k_0/2\). The cosine lower bound gives
\[
 \chi\ge 2^{-9}\frac{3071}{3072},\qquad \delta>2^{-30}.
\]
Writing \(\mathcal R_v=\sqrt{d_v^2+n_v^2}\), the bounds (49) hold at roots and nonroots alike. In particular
\[
 C_v\le16d_v+\frac{n_v^2}{8k_0d_v}
       \le\frac{\mathcal R_v^2}{8k_0d_v}.
\]
This supplies the four lower bounds for the contour height. The second is smaller than the third and fourth; the other entries in \(\eta_v\) exceed the second entry in (51). The resulting two necessary comparisons are satisfied if
\[
 \mathcal R_v^2>\frac{64\pi}{t_0\delta},
 \qquad
 \mathcal R_v^2>\frac{32\pi^2}{t_0^2k_0}.
\]
Their right sides are respectively less than \(2^{52}\) and \(2^{53}\). Thus \(|n_v|\ge2^{27}\) supplies strict margins for every degree, as well as the charge cutoff.

For regeneration, use the sharper maximum of \(d/(d^2+n^2)\), rather than the coarse \(\beta<4d/\mathcal R^2\):
\[
 \beta_v\le\frac{210\pi}{361|n_v|}
 \le\frac{330}{361}2^{-26}
 <\frac{3071}{3072}2^{-26}
 \le\frac{k_0}{2}\chi.
\]
The middle rational inequality is strict. This is a proof over all positive degrees, not degree sampling. The constant is independent of the fixed parameter disk \(R<1\); the starting quantum level is not asserted to be uniform in that disk or the diagram.

## 8. The star and its original knot pairing

The star has fixed odd center degree \(30{,}000{,}001\), central power \(2\), and fixed odd leaf powers \(2^{60}+1\). This is a very large fixed diagram, not a sequence whose size grows with \(N\).

I checked its pairing against the original literal stack convention \(F_2\sim G_1\), \(F_3\sim G_0\), and cylindrical closure \(03,12\). A braid has pairing \(I\) or \(X\); a quarter-turn sends \(I\) to \(H\) and preserves \(X\). Rooting the actual expression at a terminal circle leaves an even number of other odd leaf pairings at the center. Their product is \(I\), and the central even braid leaves it \(I\). Its actual turn is \(H\). Stacking the remaining root braid with \(H\) gives \(H\) without creating an internal circle; closing it by \(I\) gives a single component. Before that final stack all factors are through-strand braids. The algebraic evaluation from the center is merely a different contraction order.

The rational bounds in (56)–(59) have the correct inequality directions. For the center, \(D_-\) and \(A_-\) are lower bounds and \(D_+,C_+\) are upper bounds. The proposed height \(\delta_-/2\) is below every actual height constraint, and each of the four proposed lower bounds for \(\eta_o\) is valid. The most restrictive ratio of the upper bound for \(2\beta_o\) to the lower bound for \(\eta_o\) is less than \(9/10\), by rational cross-multiplication.

For a leaf, the proposed height \(t_0k_0/(2n)\) is below every constraint. The four lower action bounds exceed \(2^{-49}\), whereas the upper bound for \(\beta_v\) is below \(2^{-117}\). The regeneration and cutoff conditions follow with large margins.

The center fails every possible outgoing patch because \(\beta_o>k_0\chi\), but it needs no such patch when chosen as the final root. The displayed lower bound for the summed old criterion and the failure of the old local maximum criterion are also correct. No conclusion about an arbitrary short-twist island with several boundary variables is drawn.

## 9. Evidence and limitations

The exact-arithmetic script was read directly. Its 25 rational comparisons are legitimate enclosures of the displayed constants and the star data. Its output is arithmetic corroboration only; it does not verify a quantum sum, an analytic continuation, or hyperbolic completeness. No additional scientific computation was required for this proof read.

The inspected arithmetic script has SHA256 e600e4224be636a0c189379f4b8770ce353f4b93c3f2ff65a4a3e89bb909e052. Its result file has SHA256 9aed223ff3413a4045762388b1ae9115f937cd90a06cc9efaab435cb10c54258.

The original finite-source and normalization dependencies were read against the current notes, including the local-message theorem, uniform Newton bounds, typed compiler and turn comparison, direct-crossing trace, ordered octahedral cut, exact scalar and vertexwise geometry. A separate JSON manifest beside this audit records their hashes.

No fatal issue or required mathematical correction was found. The result remains restricted to literal ordered all-circle knot diagrams satisfying the stated test. Ordinary resonances are outside the fixed disks \(R<1\). The argument does not assert a uniform starting level for varying diagrams, a general short-twist island substitution principle, or a first correction of order \(N^{-2}\) from the leading \(O(N^{-1})\) profile alone. The earlier root-exempt \(2^{46}\) criterion remains a separate valid, more restrictive theorem.

## 10. Subsequent degree alternative and explicit core extension

After the preceding full read, the author added an explicit backward-restoration paragraph in section 7 and equations (53a)–(53c). I read these additions separately. They do not alter the conditional proof.

Backward substitution is legitimate: the root angle lies in the small contraction disk, and substituting it into each child's parent variable keeps that variable inside its analytic rectangle. Repeating this along the finite tree puts every restored angle in the common simultaneous uniqueness polydisk. This supplies the explicit identification with the geometric branch already used above.

The alternative \(d_v\ge2^{28}\) gives \(\mathcal R_v^2\ge2^{56}\), which is stronger than both tail requirements. Its outgoing estimate is
\[
 \beta_v\le\frac{420\pi}{361d_v}
 \le\frac{330}{361}2^{-26}
 <\frac{k_0}{2}\chi.
\]
The last bound is identical to the checked twist alternative. Consequently the choice between the degree and twist alternatives may be made independently at every vertex. No sum over the number of high-degree vertices is introduced.

The explicit extension of an original ordered core is topologically scoped correctly. An even stack of turned odd braid pairings has through pairing \(I\) in the actual insertion frame and has no internal closed component. It may therefore replace the empty joining slot without changing the original global component count. It need not preserve the original knot type, and the text explicitly says so. The inserted leaves are new actual crossing-circle pieces, not analytic dummy variables. Every old vertex gains the required degree and every new leaf has the required odd long power. The quantum and geometric conclusions concern the resulting knot.
