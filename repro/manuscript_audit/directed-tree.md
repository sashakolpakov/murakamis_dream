# Bounded audit of the directed circle-tree theorem

This report concerns Appendix K, Sections 1–8, and its analytic and geometric dependencies in E, F and G. It includes the degree-or-twist corollary and the original-knot identification. It does not certify the manuscript as a whole, Appendix M, or the separate numerical star example in K.9. This reading began at commit `cfc8a9295dca45562634f6021415d0d80dc5f745`. The missing comparison described below has since been inserted into Appendix F and its standalone note. Finite experiments were not used as proofs of asymptotic estimates.

The read snapshots and the implication map are recorded in [directed-tree-snapshot.json](directed-tree-snapshot.json). The principal source hashes are K `3d1fd0968715801d9ecbb30b7d7232e16a004b0587005acb682c2aa50c0b3598`, G `9a169d6aeff06df5887952c18c22a0aef470bbcda9e18610d4f57f016e2dbdce`, and F `dde7ced3710b3479ff7021f5a867bf1fd52d163d953a293c3c43d08e33318122`.

## The omitted metric-volume comparison

F lines 585–591 identify the source regulator with the representation volume. Lines 607–610 then write the metric/cone volume without explicitly explaining why the same fundamental chain computes that metric volume. The required geometric hypotheses have already been proved in F, so this is an omitted justification rather than a new restriction on the theorem.

The inserted comparison, immediately after the representation-volume formula in Appendix F’s completion section, uses the same finite boundary triangulation and the explicit homotopy

\[
H_s(w,Y)=\bigl(sa(w),Y\exp((1-s)\eta(w)+s\log b(w))\bigr).
\]

The actual log-link coordinate supplies the equivariant real function η. On a fixed fundamental boundary section, the horizontal derivatives are bounded, the height and its derivatives have order Y, and the hyperbolic volume form makes the homotopy volume O(Y⁻²). At the smooth endpoint the axis-valued boundary assignment extends over the actual meridian disk; all added axis tetrahedra have zero volume. The main cusp remains the original complete horoball end.

This uses only the *chain-comparison* part of D lines 410–436 and the general source-regulator theorem, Section 6. It does **not** invoke D's small-framed-neighborhood completion theorem: F's high-degree zero-power cases can have U near −2πi and need F's separate actual-period construction. F has already supplied the needed positive cells (F.2), nonsingular links and nonunit auxiliary holonomy (F:478–513), actual primitive periods (F:515–540), and cone/smooth completion (F:542–560). Thus no unproved short-filling hypothesis is inserted.

No further change to the strength or hypotheses of K's theorem was found in the bounded review.

Three typesetting repairs were also made: replace `Section\textasciitilde{}\ref` by `Section~\ref` at K:38 and K:614, and `sections\textasciitilde{}\ref` by `sections~\ref` at K:943. These do not affect the proof.

## Exact source and normalization checked

1. **The diagram and limit are fixed.** K:4–27 assumes a finite ordered circle tree with at least one edge; every vertex carries its original crossing circle, every edge is a physical quarter-turn, and the main pairing must give one knot with no internally closed component. The integers and degrees do not vary with N. K.8's inserted even stacks preserve endpoint pairing, not knot type. No conclusion for cyclic scalar networks or arbitrary plat diagrams is being used.

2. **The full quotient is retained.** K:178–240 defines the fixed Newton polynomials, the correct typed polynomial relation, and the full top-coefficient trace, including repeated-root derivatives. The anti-diagonal metric is invariant under the constant change of relation because the one-division quotient of eᵢeⱼ has degree at most N−2. The physical turn then gives equal indices and the factor γₑH_N/W_k. The complete kernel includes all 0≤k<N, not a low-index replacement.

3. **Rooting does not change a physical word.** K:357–390 only reorders an already lowered finite tensor contraction. The functional acts in t, while all parent u dependence is in one kernel, so the outgoing polynomial has degree at most N−1 in −2cos u. The degree does not increase with subtree size. All physical edge scalars are assigned once; the original closing, mixed-reference and framing scalars and the single reduced-cut factor remain outside the final trace.

4. **Outgoing norm bounds include all normal data.** K:599–614 uses the complete polynomial norm, fixed-power crossing representative, Chebyshev reduction and full trace. I read the actual source-bound derivation (D9)–(D17), not just its named theorem: the factor-count cost is fixed for a fixed tree, negative powers are included, and the collision-safe bound holds on each disk |s|≤R<1. This argument does not estimate moving multiplication terms individually by positive complete tensors.

5. **The microscopic normalization is the stated one.** The Gaussian crossing scalar is q raised to n(d²/4−σ²/2); the first charge coefficient is exactly one, and the paired edge insertion has leading value one. Together with the separately retained original scalar ledger, K obtains A_N(s)=q_N^{(-w(D)−Σn_v)s²/2} and one H_N(s). The N-dependent complex subtree scalar cancels only in the exact ratio M_v(u)/M_v(0). It is not replaced by its modulus or an assumed convergent amplitude.

## Conditional saddle and full-source remainder checked

The critical point proof is local to the current trace, while the recursion keeps each child's exact value at zero. That separation is what avoids accumulating the total augmented action loss at every vertex.

- **Actual finite edge saddle.** K.2 uses E.3–5 for the regular-index packet, its canonical factorial interpolation and cotangent endpoints. The complementary polynomial has a strict single-edge loss, including high-index normals; its ellipse bound absorbs the fixed complex-parent rectangle. Inside the retained interval, K:289–344 establishes the parent normalization Re ψ(0,u) from actual finite products, not merely 2G₀+O(|u|²). The conditional kernel estimate is therefore strong enough for the later local budget.

- **Closed phase class.** K:450–502 sums exactly d_v incidences. The even nonlinear error has E_t=tQ with |Q|≤a_v/20. Consequently t_ℓ=−iℓ/(D_v−Q), whose denominator has positive real part even for complex parent u and negative or zero n_v. This proves the lower-half-plane sign and the charge ordering. The Schur term in h_v'' is bounded using the same denominator; it does not assume child phases are real on the real axis.

- **The trace identity is valid before any long-twist asymptotic.** I read Section 2, equations (10)–(18), of `actual_main_meridian_direct_crossing_trace.md`. The translated finite grid, its vertical sides, upper/lower expansions and zero-mode endpoint currents are exact for every fixed integer n, including n=0. K uses this exact identity and proves its own saddle/tail estimates. It does not import that note's later theorem requiring large |n|.

- **Tail and connector budgets are conditional.** K:506–579 controls the actual normalized input by exp N[Re ψ(0,u)−A_vt²+B_vy²]. The omitted high charges are shifted by y_v and summed geometrically. Original endpoints and zero-mode currents retain their own loss. The finite retained charges are compared by saddle action and have an absolute error relative to Re ψ(0,u), not a false relative expansion at each much smaller charge. The condition β_v<η_v/2 puts every such error below the first conditional charge. The first coefficient is one at both level parities.

- **Finite-N logarithms do not add a new exponential loss.** Once a child has a nonzero uniform asymptotic on a slightly larger compact, its exact normalized logarithm differs from h_w by the amplitude logarithm divided by N and an O(N⁻²) term. Cauchy estimates control fixed derivatives. For a fixed finite tree these are ordinary amplitude corrections or an O(N⁻¹) saddle displacement. They are not repeated comparisons with the complete absolute source.

- **The real and strip bounds close.** The exact Laurent degree gives the subharmonic Poisson bound used in K:432–447. It applies to complex coefficients and zeros; it needs no positive message coefficients. The far angular region uses the chosen c_v budget, and the near region uses the local phase curvature. Only nonroot vertices require the outgoing normalization condition (9). At the final root no new message has to be propagated, so (8) is the correct remaining comparison.

These steps estimate the complete finite recursion. There is no separate unbounded global source remainder left after the conditional induction.

## The uniform degree-or-twist implication

K:672–775 proves the sufficient condition for all degrees, rather than sampling them. With c_v=k₀/2, the inequalities A_v≥k₀d_v/(2π²), B_v≤16d_v and C_v≤(d_v²+n_v²)/(8k₀d_v) hold also at the root. They yield a lower bound for every branch of y_v and then every branch of η_v. The two relevant comparisons depend on R_v²=d_v²+n_v². Either |n_v|≥2²⁷ or d_v≥2²⁸ exceeds both requirements. The outgoing β_v comparison is then proved separately by the twist or degree estimate.

No division by n_v is used in the directed proof or its geometric continuation. The definitions remain meaningful at n_v=0 because A_v>0 and |D_v|>0. A finite tree satisfying the mixed condition cannot have every power zero: its degree-one vertices must satisfy the long-twist alternative. Thus allowing a high-degree zero-power junction does not assert that an arbitrary unchanged zero-twist core is hyperbolic.

The explicit star arithmetic of K.9 was not rerun or independently rederived in this bounded review. It is an application of the same finite criterion, not an input to the universal degree-or-twist proof.

## Identification with the original filled volume

K:623–663 restores the exact subtree constants. Its stationary equations are the original joint equations

\[
\Psi_{\tau_v}+\frac{i n_v\tau_v}{2\pi}=i,
\qquad
\mathcal C(1)=\operatorname{stat}\left[
\Psi+\frac{i}{4\pi}\sum_vn_v\tau_v^2-i\sum_v\tau_v\right].
\]

Backward substitution gives every restored angle the bound 1/[(19/20)|D_v|]. By (8), |d_v−in_v|=2π|D_v|≥2π·2¹⁵>630. All restored angles therefore lie in G's simultaneous contraction polydisk. Uniqueness identifies this joint solution, not merely its action, with the geometric charge path at c=1.

I read G:264–382. The explicit edge derivative E(t,u)=2arsinh(tan(t/2)cos(u/2))−t has E=tH with a uniformly small holomorphic H. The maximum-norm contraction depends on d_v/|d_v−in_v|≤1, and not on the number of vertices. Its denominator has positive real part, proving Im τ_v(c)<0 for c>0 even when n_v=0. This gives the two facts needed by F: positive local octahedral shapes and nonunit auxiliary dilation. No geometric conclusion is inferred from a quantum lower bound.

I read F’s ordered-cut, local-chart and completion/calibration sections through line 629, together with the primitive-word portion of the original general-mask note. The literal insertion table retains the full oriented boundary ribbon graph, not just face counts. It constructs the two projection balls, preserves the individual crossing disks and their cyclic order, and leaves the odd crossing on one distinguished seam. The full complex seam maps cancel, including the actual odd copy exchange. The original primitive words give

\[
U_v=-2\pi\Psi_{\tau_v}-i\epsilon_v\tau_v,
\qquad V_v=2i\tau_v,
\qquad n_v=\epsilon_v-2p_v,
\]

hence U_v+p_vV_v=−2πic. This is the correct full logarithmic period: F's compact similarity-link argument excludes its second fixed point, and the complete limit forces the possible 2πi integer discrepancies to vanish. The period is established before multiplying a longitude by p_v and is never reset to a principal logarithm.

The primitive slope has cone angle 2πc, and its complementary primitive λ_v has positive core length Re V_v=−2Im τ_v. At c=1 the end is an ordinary smooth solid torus with meridian μ_v+p_vλ_v. The main parabolic meridian remains nonidentity in its local chart, so its torus has a complete Euclidean translation link. The completed metric is complete and finite volume on the original disk-filled diagram. The local crossing-disk surgery restores R^{ε_v−2p_v} in the original ball, so the one-component pairing hypothesis makes this the stated knot complement in S³.

Finally, the normalization is 2πRe C, not Re C. The source/regulator algebra is

\[
\frac{G}{2\pi i}-\mathcal C(c)
 =-\frac{i}{2\pi}\sum_vp_v\tau_v^2,
\qquad
\frac12\Re U_v\Im V_v=p_v\Im(\tau_v^2).
\]

The two corrections cancel exactly. The absolute constant is the same complete positive cell assembly, with two regular octahedra per tree edge. The added same-chain comparison supplies the explicit last metric-volume identification. The Schläfli check uses the same λ_v core and yields dVol_c/dc=2πΣIm τ_v. The main cusp stays unfilled throughout.

## Imports not freshly proved here

The audit traced the applicable statements and the main local derivations, but did not reprove the full quantum tangle compiler, all pointing/isotopy invariance, all original matrix threading calibrations, every Hermite interpolation inequality, or the ideal-chain Bloch differential from first principles. Those remain named written inputs with source hashes. The analyticity of the fixed factorial interpolation and ordinary uniform nondegenerate stationary phase are likewise used mathematical inputs, not formalized here.

The native reference check found all 258 `ref`/`eqref` targets examined in K/F/G present and unique. This is a reference-integrity check only. The finite rational and endpoint-pairing scripts in K.10 are supplementary checks of their stated finite claims; none replaces the uniform induction or the metric completion.
