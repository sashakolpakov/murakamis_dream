# Appendix O: import interface for a protected triangular sum

This is a bounded, read-only check of the geometric central-contribution theorem used in the private protected triangular-sum closure. It checks the hypotheses and normalization of the imported arguments; it does not replace their complete analytic or geometric proofs. No compiler, numerical experiment, manuscript build, or scientific verifier was run. No public file was changed.

The inspected public revision is `552425cd54a02c84a46813ed48565c1e30b70e74`. Exact file hashes and the read scope are recorded in the companion JSON manifest. The new outside-weak-balance application in the closure note's section 7 is **not** covered by this report.

## 1. Verdict and the extra data required

I found no new hypothesis mismatch in applying Appendix O to the new sphere constructed in sections 1–6 of the protected triangular-sum note. Simplicity, orientation, a dual perfect matching, and the final knot parity are not the entire *recorded input*: one must also retain the literal inverse-cut realization in the oriented three-sphere, all cyclic crossing orders, signed disk collars, a nonmatching marked edge, and the original primitive disk basis. These are explicitly part of the closure construction and Appendix O's hypotheses.

A positive geometric certificate, full-rank marked deformation, and nonzero selected period are necessary parts of the proof. They are not additional unproved assumptions for this simple-sphere class: Appendix O supplies or imports their construction with the requisite scope. In particular, the positive certificate is obtained **before any terminal decoration**. No complete-radius balance, middle forest, Conway-tree presentation, or flat-plat reduction is required for Appendix O's central contribution.

The resulting claim is nonvanishing for **every sufficiently large level of both parities**, with the diagram and signed powers fixed. It is not a claim of nonvanishing at every finite level. The long-power threshold and the subsequent level threshold may depend on the entire assembled diagram and its recorded choices.

The full invariant remains a separate step. Appendix O proves the central period and its actual filled volume, not a full-source complementary bound. The closure note supplies such a bound by its unabridged shared-radius certificate and the actual weighted Hermite functional. This separation is maintained in the inspected text.

## 2. Recorded topology, positivity, and rank

The following locations are in `manuscript/sections/O-morse-geometric-contribution.tex`.

* **Lines 658–699, `mcg:sec-1`:** the permitted data are a finite oriented simple triangulated sphere with at least four vertices, a dual perfect matching, a recorded order of each four-vertex quadrilateral, and a marked nonmatching edge. Either an actual augmented diagram with this cut or the literal inverse-cut construction is required. The retained signed half twists and primitive disk curves are fixed. Knot parity is tested on the new diagram, not inherited by assertion from two old knots.
* **Lines 740–811, `mcg:sec-2`:** the inverse-cut construction uses disjoint four-terminal disks and their perpendicular crossing-circle collars in the three-sphere. Opening the original half disks cancels the handles introduced by drilling the boundary-parallel semicircles, leaving the two projection balls. It is not the incorrect operation of gluing edge-octahedron balls cyclically without extra cuts. The actual even and odd corner maps, rectangle links, and complete horoball ends identify the original augmented exterior.
* **Lines 693–699 and 801–811:** the positive right-angled certificate comes from `actual_balanced_terminal_fan_volume.md`, section 2. That section begins with the simple sphere itself; the fan construction starts later. Its proof permits separating triangles. Thus importing its initial packing theorem does not covertly add terminal decorations or assume radius balance.
* **Lines 181–217 and 875–947, `mca:sec-2`, `mcg:sec-4`:** the ordinary graph obtained by deleting the two adjacent protected vertices is connected. The literal face-difference rows are primitive and have rank (R-1) after fixing a common scale. A matching outer pair cannot consist of both protected vertices because their unique edge is the nonmatching mark. Each crossing therefore has (x+y>0) and at least one nonmonomial source triangle. These are the hypotheses needed by the local cofactor and spectral-curvature formulas.

The marked circle reconstruction has a separate finite rank argument, not a consequence inferred from the scalar action alone. In `mcg:sec-4`, the angle equations first force a common radius scaling, the fixed two-line triangles kill that scaling, and adjacency of the remaining disk of center triangles leaves only the removed horizontal translation. This matches `actual_marked_deformed_circle_pattern.md`, sections 1–3. The selected flags, including the collision at a two-line triangle, are retained.

For the protected triangular sum, the two removed triangles have opposite orientations; only their three boundary vertices are identified, and the interiors are disjoint. The output is again a simple sphere. The former partners give the new quartet ((u,a,c,B)), with four distinct vertices; the marked edge (uv) remains nonmatching. These facts suffice to restart the above construction for the **new** diagram. No assertion that an old geometric representation extends across the sum is needed. Nor is an additive formula for the *filled* volumes used.

## 3. Exact finite source, source degree, and normal data

Appendix O lines 814–872 (`mcg:sec-3`, equations `mcg:eq-5`–`mcg:eq-7`) identify the exact original source and raw Fourier/Hermite period. The underlying source is `research_matched_sphere_morse_source.md`, sections 4–6, not an abstract matching-graph partition function substituted for the invariant.

The finite reasoning needed for this use is explicit there:

1. The typed local adapter imposes the physical, unwrapped head support before the face grids are introduced. Cups, caps, reversals and the mark use their actual matrices.
2. The mark is initially unrestricted. Whole-network conservation forces the complementary heads before replacing the mark/cap ratio. The cup/cap and coupon scalar is (N^{-R-1}), and the primitive face grid has (N^{R+1}) entries.
3. The winding equation (M_f-T_f=2) on bounded faces and (-2) on the exterior determines the original face targets. At even levels, the main-edge parity cochain integrates on the sphere. The remaining coset character is one on the surviving alias.
4. The face numerator is homogeneous of total degree (dR), (d=N-1). Its nonnegative face exponents and the (R) ordinary targets (d) exclude every other grid alias. Both protected exponents are zero.
5. The local cleared resolvent has degree at most (d) in its spectral variable. Multiplying different boxes and extracting their shared face coefficient preserves degree at most (d) in **each** spectral variable; central/left/right projection does not raise it. This is the degree hypothesis needed by the whole-period tail estimate and finite filling norm.
6. The actual (R^{n_e}) is inserted by its complete fixed-root Hermite functional, including repeated-node derivatives and the odd simple-node term. Multilinearity permits separate local functionals without commuting different boxes. The old flat ordering is not used.

The raw Fourier normalization includes (q^{d^2\sum n_e/4}(-i)^R), the original nonzero integer charges, their product and parity character, and all sine factors. There is no extra (N^R), spectral square-root Jacobian, quantum dimension or independently assigned mark factor. The separately recorded framing/component character has modulus one. If the full one-cut modified convention is used instead, its (i^{N+3}/N) factor must remain; its logarithmic cost is zero after division by (N).

This is the weighted physical functional, not merely the untwisted top-coefficient functional of a monic quotient. In particular, a scalar normalization of an untwisted coefficient map would not justify arbitrary signed crossing powers: their multiplier and its derivatives remain part of the exact formula.

## 4. Analytic central contribution: no flat-plat or full-source shortcut

`mca:sec-1` first states the analytic theorem with a positive labeled certificate. The geometry part discharges that hypothesis for this class. The chain is as follows.

* **Local packet, O lines 219–250:** `actual_cross_cofactor_interpolant_rigidity.md`, sections 1–4, treats every actual protected-zero pattern on a fixed positive compact, with both parity grids. It compares the actual central cofactor with its complete-fold interpolation by relative exponential accuracy. Its even and odd factorization retains the central-skipping term and the normal data; it does not differentiate a value-only interpolation.
* **Shared coefficient, O lines 252–325:** the angular cofactor bound is sewn on the same shared face radii. The connected ordinary graph supplies a separated triangle off the common phase. The exact primitive quotient torus has dimension (R-1) and measure ((2\pi)^{-(R-1)}d\theta). The positive Hessian gives the actual finite face saddle and a nonzero Gaussian coefficient. This obtains H1 directly for the central projection.
* **Global spectral complement, O lines 328–375:** `actual_global_cross_spectral_gap.md`, sections 1–2, uses the original start decomposition, signed tail transfer, repeated-root Cayley–Hamilton bound and uniform prefix estimates. Its assumptions are (x+y>0), protected zeros fixed, and other weights in a positive compact, with terminal indices (N/2+O(1)). The sole monomial exception is harmless because each crossing has another nonmonomial triangle. Combined with the shared angular gap, this supplies H2 on the full real spectral cube and a thin fixed strip.
* **Nonzero packet and every charge, O lines 378–522:** the original real cube is translated to the joint finite saddle, with side currents below it. Separate evenness gives the exact derivative comparison of charge-critical values. Infinite charges are bounded on whole intervals with real spectators and the retained second-derivative endpoint currents. Only after this operation is a finite charge set split into local and bad charges. The argument allows independently unbalanced fixed signed powers.

The old `general_localized_unit_charge_filling_period.md` states its full-numerator result for certified flat plats and imports a full packet. It cannot alone be cited as the present theorem. Appendix O does not do so: it reconstructs H1/H2 for its own central polynomial and spells out the whole-period argument in `mca:sec-4`–`mca:sec-7`. In particular O line 325 explicitly excludes reliance on the old full-numerator restoration. No middle-forest positive endpoint theorem enters this chain.

The nonzero formula is `mcg:eq-32` (O lines 1291–1307). Its determinants use the continued positive face branch and the accretive spectral branch. Formula `mcg:eq-33` has positive imaginary saddle coordinates for either sign of the fixed powers, so the sine factors are nonzero. The contour coefficient is one, proved by the translation rather than assigned. The unit charge signs agree because reflection reverses both the sine integral and its charge weight; the original parity sign cancels by `mcg:eq-36`. Thus the relative asymptotic supplies a lower bound, not only a candidate action or an upper rate.

## 5. Primitive filling and actual volume

O lines 950–1028 use the same global white-reflection pattern to form every slice head. Products telescope, and the inserted cup/cap pair is an exact inverse pair. Each local disk transport conjugates the two **actual** generators. The primitive collar is the specified contact map, not the doubled reflection product. Formula `mcg:eq-16` supplies the whole determinant-one auxiliary meridian, including negative retained half twists. This is stronger than agreement of peripheral eigenvalues.

The source convention and the disk surgery convention are exactly
[
 n_e=\epsilon_e-2p_e,\qquad
 V_e=-4\pi i\delta_e,\qquad
 U_e+p_eV_e=-2\pi i.
]
The half twist is included once, through the shear in (A_\epsilon) and the actual collar. A chosen new parity pattern must be recorded before choosing its long powers; changing parities during the argument would change the knot.

The completion import `general_source_regulator_hyperbolic_equality.md`, sections 1–5, requires an actual framed representation near the complete one, parabolic unfilled peripherals, and exact **primitive logarithmic** filling equations. O verifies these at lines 1097–1203. In particular the unit saddle has \(\operatorname{Re}V_e>0\), hence a nonunit longitude modulus. The common second fixed point escapes to infinity as all powers grow, so actual developed link periods equal the small (U,V) logs *before* multiplication by (p_e). The log-link torus has rank two. The primitive period (-2\pi i) consequently completes to a smooth solid torus, rather than merely giving an exponentiated identity at a parabolic cusp.

Finally O equations `mcg:eq-18`–`mcg:eq-25` retain the regulator boundary term and the absolute complete anchor (2\pi\Phi_D=\operatorname{Vol}(Y_D)). The explicit Gaussian and linear terms cancel that boundary term at the first charge. The same original fundamental class and filling-chain comparison then give the metric volume of the **new filled exterior**. This is not deduced from hyperbolicity alone or from a matching Hessian.

## 6. The remaining full-invariant interface and a formalization skeleton

O lines 1235–1246 (`mcg:eq-29`) expressly leave the full complementary source estimate separate. For the closure application let \(\mathcal D_N=S_{N,\mathrm{full}}-S_{N,\mathrm C}\). The unabridged certificate proves
[
 \|\mathcal D_N\|_{[-2,2]^R}
 \le \exp\{N(\Phi_D-\gamma)+o(N)\}.
]
The multidegree property above permits the **actual weighted** norm theorem `actual_uniform_filling_supremum_bound.md`, sections 2–5, to give
[
 |(\bigotimes_e\mathcal L_N^{n_e})\mathcal D_N|
 \le \prod_e(1+|n_e|/2)\,\|\mathcal D_N\|.
]
Both parities and all normal terms are already in this finite identity. The stronger joint-grid-vanishing improvement is optional. For fixed powers the displayed constant has zero exponential rate. As the powers become independently long, the selected action approaches \(\Phi_D\); take them long enough that \(\operatorname{Re}S_{\boldsymbol1}>\Phi_D-\gamma/2\). The nonzero relative central asymptotic then dominates the remainder. No global nonzero old-sector omission is allowed in transporting the closure certificate; the closure note explicitly requires the stronger unabridged input.

A useful proof-assistant dependency boundary is therefore:

1. Oriented simple sphere + matching + marked edge + recorded inverse cut -> original diagram and primitive disk data.
2. Finite typed coupon/mark/cup/cap identities + primitive face lattice -> exact source and degree/normalization ledger.
3. Positive complete geometry + local analytic cofactor theorems + ordinary graph rank -> H1 and H2 for the central projection.
4. Exact whole Fourier period + H1/H2 + charge comparison/current estimates -> nonzero central asymptotic at both parities.
5. Actual marked representation + primitive log equations + completion and regulator -> its action equals actual filled volume.
6. Unabridged finite sector certificate + local phase-uniform envelopes -> strict full complementary supremum gap.
7. Multidegree + weighted finite Hermite norm + positive rate margin -> full-invariant equality.

Steps 2 and 7 have finite algebraic substatements suited to formalization. The local analytic estimates, compact geometric completion, and regulator identity are independent analytic/geometric inputs; finite experiments or split-monic Lean algebra do not certify them. This report found no unclosed *import-interface* obligation for steps 1–5 on the protected triangular sum. It is not an exhaustive reproof of all supporting notes, a certification of the whole manuscript, or a review of the new section 7 example.
