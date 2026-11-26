# Bounded geometry and source-interface audit of Appendices P and Q

1 November 2026. Repository: /private/tmp/murakamis_dream-publication. Base commit: 021e6482b99f8456b4a34912e9f97969fc546a69, including the current uncommitted O/Q corrections. The accompanying JSON records exact source hashes.

This is a read-only examination of specified written implications. It is not a certification of every manuscript proof, a formalization of topology or analysis, or an inference from finite numerical tests.

## 1. Findings and incorporated corrections

I read P and Q in full and checked their source, geometry and filling interfaces against the portions of N, O, L and the original technical notes listed in Section 7. Two precise corrections were reported and are now incorporated:

1. **Q, lines 506–510:** face identifiers 11 and 14 are not numerical weights. The corrected inequality
   \[
   Q(0,e^{q_{11}},e^{q_{14}})\ge q_{11}/2
   \]
   follows by selecting the simplex vertex supported at \(e^{q_{11}}\). The added explanation correctly distinguishes face labels from weights.
2. **O, lines 1309–1315:** the correct derivative limit is
   \[
   \partial_e A_N=-2\delta_e B_{e,N}(\boldsymbol\delta^2),
   \qquad B_{e,N}\longrightarrow B_{e,0},\qquad B_{e,0}(0)=C_e>0.
   \]
   At a nonzero argument the limit need not equal \(C_e\). Shrinking one fixed complex chart and then increasing the starting level gives \(\operatorname{Re}B_{e,N}>0\), which is the required input to the critical-point and nonunit-holonomy arguments.

Neither correction changes the theorem hypotheses. I found no additional defect in the checked algebra, target accounting, quantifiers or geometric interfaces. The unexamined proof layers remain explicit imports in Section 7.

## 2. The logical separation

| Input | Written implication | Output |
|---|---|---|
| Fixed simple oriented triangulated sphere, perfect dual matching, nonmatching mark, original orders | Inverse cut and simple-sphere packing | Original \(Y_D\subset S^3\), complete positive structure, \(\Phi_D=\operatorname{Vol}(Y_D)/(2\pi)\) |
| The same diagram and cup/cap transports | Exact Morse source identity | Shared coefficient extraction with original targets and scalar |
| Complete source and marked deformation | O's local estimates and whole-period argument | Nonzero entire central contribution for fixed independently long signed fillings |
| Selected critical point and primitive peripheral words | Representation, actual logarithmic periods and smooth completion | Metric on the specified filled knot complement |
| Same developed fundamental chain and complete anchor | Regulator and filling correction | \(2\pi\operatorname{Re}S_D=\operatorname{Vol}(S^3\setminus K_D)\) |
| P's weak balance, or Q's unabridged input certificates | Shared-weight comparison of every genuine noncentral string | Strict full-cube bound for the complementary polynomial |
| Full-cube bound and N's exact filling norm | Larger fixed twist threshold | Exponentially smaller filled remainder |
| Nonzero central term and smaller full remainder | Rate transfer | Full invariant volume limit |

The central contribution is not substituted for the full invariant. The initial simple-sphere geometry uses neither weak balance nor the desired full-source bound. P and Q do not use their volume conclusion to prove their source bounds.

## 3. Appendix P

### Fixed data and normalization

P, lines 15–81, fixes the sphere, protected adjacent vertices, local orders and a retained half-twist pattern whose actual strand pairing is a knot. Ordinary targets are \(d=N-1\); both protected targets are zero. The powers satisfy
\[
n_e=\epsilon_e-2p_e,\qquad \epsilon_e\in\{0,\pm1\}.
\]
The diagram, half twists and integers are fixed before \(N\to\infty\). The invariant is reduced and zero-framed, with unknot value one. There is no uniform estimate for a diagram growing with \(N\), and no bounded-ratio condition on independently large signed powers.

The triangle homogeneity is
\[
Q(tw_1,tw_2,tw_3)=Q(w_1,w_2,w_3)+\tfrac12\log t.
\]
Two triangles at a crossing have total logarithmic degree one, consistent with the ordinary target count. The geometric normalization is \(2\pi\Phi_D=\operatorname{Vol}(Y_D)\).

### Why the gap is strict

I checked P, lines 85–264. The triangle log-weight Hessian is the stated positive semidefinite Laplacian, with off-diagonal entries
\[
-\frac{w_iw_j}{2\pi D_t(w_i+w_j)}.
\]
The complete action is stationary modulo common scaling. The common flattening \(q\mapsto(1-t)q\) costs at most \(t^2E/2\), while supported triangle entropy decreases as the log weights are multiplied by \(\beta\). Thus
\[
X_e-A_{e,s}\ge t h_{e,s}-(1-t)\epsilon_{e,s}.
\]
The relevant \(h_{e,s}\) is strictly positive: the matching outer edge cannot be the protected nonmatching edge of a simple sphere, so the overloaded-middle triangle has another ordinary supported corner. The proof does not assign positive entropy to a protected singleton triangle. Weak balance makes the defects zero, so a fixed small \(t>0\) gives a linear local loss against a quadratic complete-action cost.

P, lines 266–310, uses this single common weight vector on the same shared face torus for every genuine sector string. Every noncentral string has a surviving one-sided label. The finitely many strings are independent of \(N\); summing them preserves the exponential gap. Both parities and the full real spectral cube are retained.

### Filling transfer

P, lines 322–369, applies N's exact norm
\[
\left\|\bigotimes_e\mathcal L_N^{n_e}\right\|
\le\prod_e(1+|n_e|/2).
\]
For fixed powers this has zero exponential rate. O supplies a nonzero central term with
\[
\operatorname{Re}A_{\boldsymbol n}
=\Phi_D-O_D\!\left(\sum_e n_e^{-2}\right).
\]
The twist threshold is chosen after the fixed positive source gap, making the action decrease smaller than that gap. This order is present. The original framing phase has modulus one; the modified scalar \(i^{N+3}/N\) has zero exponential rate.

## 4. Appendix Q

### The operation and the original topology

Q, lines 132–182, removes oppositely oriented faces \((u,v,B)\) and \((u,B,v)\) from two fresh spheres. Their retained partners are \((u,a,B)\) and \((u,B,c)\), producing the ordered quartet \((u,a,c,B)\). Fresh interiors prevent additional identifications. Only the three boundary edges are identified; the embedded boundary cycles and opposite orientations give a simple oriented sphere. The induced matching is perfect and \(uv\) remains nonmatching:
\[
R_{\mathrm{new}}=R_1+R_2-1,\qquad
V_{\mathrm{new}}=R_{\mathrm{new}}+2,\qquad F_{\mathrm{new}}=2R_{\mathrm{new}}.
\]
The inverse-cut construction is applied to this new sphere with its retained local orders. It produces a link in \(S^3\) with the stated crossing disks, not an abstract tensor network assigned an unrelated manifold. A whole-input reflection transports its orders and signs; it is not an isolated matrix symmetry.

The new diagram must satisfy its own knot-component test. A knot-producing parity exists by choosing odd crossings on a spanning tree of the connected untwisted-component adjacency graph. The theorem does not say that arbitrary old knot parities remain knots, that knot type is preserved, or that filled volumes add.

### Target cancellation and the geometric action

For \(q_B=\log B\), \(Q_a=Q(0,a,B)\), \(Q_c=Q(0,c,B)\),
\[
C_1=\tfrac12q_B+Q_c,\quad C_2=Q_a+\tfrac12q_B,\quad
X_{\mathrm{new}}=C_1+C_2-q_B.
\]
The two old actions subtract the ordinary \(B\)-target twice and the new action subtracts it once. The local \(-q_B\) correction therefore cancels exactly the duplicated target:
\[
P_{\mathrm{new}}=P_1+P_2.
\]
The protected targets remain zero. Each whole action is invariant under common scaling of ordinary weights; normalize both minimizers to \(B=1\). This proves
\[
\Phi_{\mathrm{new}}=\Phi_1+\Phi_2.
\]
The simple-sphere calibration gives the volume of the **new augmented complement** divided by \(2\pi\). It makes no assertion about a sum of filled knot volumes.

### All strings and arbitrary fixed finite iteration

Q, lines 231–385, keeps the actual index partition at both parities and maps
\[
C\mapsto(C,C),\qquad L\mapsto(L,C),\qquad R\mapsto(C,R).
\]
The inequalities use \(Q_a,Q_c\ge q_B/2\), including the mixed branches. A new noncentral string induces at least one noncentral input string; no protected-overloaded input label is introduced.

The input requirement covers **every locally allowed noncentral string, even if its old global coefficient vanished**. This is necessary: old global support vanishing need not survive gluing. The proof retains this unabridged hypothesis.

Choose a certified witness for a noncentral input and its complete minimizer for a central input. Scale each whole vector to \(B=1\). This gives one valid shared torus for the new string and gap at least \(\min(\gamma_1,\gamma_2)\). Distinct strings may use distinct tori, while all factors of any one string use the same torus.

Q, lines 390–427, repeats with one common protected mark and fresh interiors. The whole previously assembled witness is rescaled, not one already shared face. Any fixed finite number of positive input gaps has a positive minimum. No growing-assembly limit is asserted. N and O are reapplied to the resulting fixed diagram, with its own metric and primitive slopes.

### Seventeen-region application

I checked the logical certificate use and preserved incidences in Q, lines 458–546. Fifteen nonempty-right-subset branches and twenty-five remaining anchored branches cover all locally allowed noncentral strings. The restricted anchor-12 dual has mixed spectators only at \(2,4,7\), localizing a weak-balance failure to \(J=\{2,4,7,12\}\). The crossing-15 attachment leaves these candidates untouched and preserves their complete ratios up to common scale. The repeatable tetrahedral input has the stated \(\tfrac12,\tfrac14,\tfrac14\) loads.

This is the claimed separation between sufficient conditions for marked diagrams. It does not establish that the resulting unmarked knots lack another covered presentation. I did not rerun the interval certificates this turn; the numerical margins remain imports from the named exact public certificate/verifier pairs. The eight-attachment replay is a finite check, not the proof of arbitrary finite iteration.

## 5. Actual complement-volume identification

### Complete anchor independent of the source remainder

I read O, lines 658–811, with L, lines 48–144, and the original Morse inverse cut. The simple-sphere packing proof precedes fan insertion. It separates strict Hall feasibility from the entropy boundary-exclusion argument, then uses the strict interior maximizer and degree-one center development. It does not infer interiority from feasibility alone.

The center-triangle sectors give disjoint disks and remote supporting-circle inequalities, including separating triangles. Labeled halfspaces give the original convex right-angled ideal polyhedron. Its reflection double has the original white and shaded maps; complete torus links and four-right-angle edge cycles give the complete augmented metric and \(2\pi\Phi_D=\operatorname{Vol}(Y_D)\). The crossing-circle balls and inverse cut supply the topology in \(S^3\). Cycles in the matching graph are allowed; no tree substitute is used.

### Actual source coordinates and primitive words

O, lines 877–1094, constructs a marked holomorphic circle pattern near completeness, fixing scale and translation by the original protected strip. White reflections and prefix products give the actual group representation. The consecutive \(F,G,F\) factors cancel at cups/caps, so a flat plat sweep is not assumed.

For the original ordered pair \(P=BA\),
\[
U_e=-\operatorname{Log}R_{0,e}-\epsilon_e\operatorname{Log}(-J_e),
\qquad V_e=2\operatorname{Log}(-J_e)=-4\pi i\delta_e.
\]
The corner-map eigenratio is \(R_{0,e}\), not its square. The signed Hurwitz seam contributes once. The stated matrix has determinant one and eigenvalue \(e^{U_e/2}\).

With \(dA^\epsilon=\sum U_e\,d\delta_e\), the stationary action
\[
S=A^\epsilon-2\pi i\sum p_e\delta_e^2+2\pi i\sum\delta_e
\]
gives the original primitive equation \(U_e+p_eV_e=-2\pi i\). The reciprocal-slope implicit-function theorem starts at the complete pattern and gives a fixed neighborhood for independently large signed slopes, without a ratio restriction.

### Smooth completion, not just a multiplier equation

O, lines 1099–1204, applies the written small-framed-representation construction in the general regulator/hyperbolic-equality note. Its needed hypotheses are supplied: positive complete starting structure, nearby actual framed representation, complete main cusps, original primitive bases, and small individual-generator logarithms.

At the unit-charge critical point the corrected derivative identity implies
\[
\operatorname{Im}\delta_e>0,\qquad
\operatorname{Re}V_e=4\pi\operatorname{Im}\delta_e>0
\]
for either sign of \(n_e\). This is nonunit modulus. The second auxiliary fixed point escapes the complete cusp frame. Generator paths avoid it, and their logarithmic increments tend to zero and equal \(U_e,V_e\) before multiplication by the large integer.

The developed torus has a complete flat logarithmic metric and rank-two period lattice. The primitive slope has actual period \(-2\pi i\), not merely exponential one. The complementary primitive period has nonzero real part. The tube therefore closes smoothly with angle \(2\pi\), along exactly \(\mu_e+p_e\lambda_e\). The main cusps stay complete. This is a complete finite-volume metric on the original filled knot exterior; no cone-to-smooth or multiplier-to-group shortcut is used.

### Absolute action on the same fundamental chain

I checked the signs and factors:
\[
d(2\pi iA^\epsilon)=-\tfrac12\sum U_e\,dV_e,\qquad
2\pi\operatorname{Re}A^\epsilon
=\operatorname{Vol}(\rho)-\tfrac12\sum\operatorname{Im}U_e\operatorname{Re}V_e.
\]
At a primitive critical point,
\[
\operatorname{Re}(-2\pi i p_e\delta_e^2+2\pi i\delta_e)
=\frac{\operatorname{Im}U_e\operatorname{Re}V_e}{4\pi},
\]
which cancels the boundary term, with the complete constant fixed.

The metric comparison uses the same finite boundary triangulation and developed relative chain. The cusp map is homotoped to an axis-valued boundary map with vanishing limiting homotopy volume. Extending that assignment across the filled solid torus adds collinear straight tetrahedra of zero volume. Thus representation volume equals the constructed metric volume in the same fundamental class. An unrelated triangulation or volume-rigidity slogan is not being substituted.

P/Q do not require the separate result that a filled knot's meridian is a local character-variety coordinate. They do not use the all-orders geometric-characteristic or annihilator-factor theorem.

## 6. Declared dependency checker

I read the JSON map and Python checker and executed it with output confined to /private/tmp. It checked seventeen declared steps and rejected seven supplied invalid substitutions.

The map separates six final roles: exact invariant, nonzero contribution, full remainder, specified metric, absolute volume, and rate transfer. It propagates assumptions and level restrictions, detects graph cycles, and prevents a written conclusion from depending on an open node. The general unchanged-sphere remainder and full-volume claim remain open.

This is a manually supplied graph. It does not discover hidden dependencies, prove node statements, or derive truth from anchors/hashes. The metric node bundles the framed deformation and primitive-log construction reviewed above. The long-twist assumption now explicitly says **absolute values** exceed the threshold, and the tensor norm node points to its tensor-product formula. These agree with the manuscript's signed-magnitude quantifier and the precise N interface. My private checker execution preceded those two reference/prose refinements; the parent reports a successful execution of the revised map.

## 7. Read scope and remaining imports

| Source | Portion examined |
|---|---|
| P-weak-balance.tex | Full theorem/proof: flattening, positivity, full source, filling transfer |
| Q-protected-triangular-sums.tex | Full theorem/proof: all bridge cases, topology, iteration, seventeen-region logical application |
| N-uniform-filling-bound.tex | Finite source/domain/normalization, norm statement and tensor use, rate interface |
| O-morse-geometric-contribution.tex | Analytic assumptions/whole-period statement and graph applicability; full original geometry, matrices, filling, regulator/metric interface; charge summary |
| L-balanced-terminal-fans.tex | Initial simple-sphere existence before fans; local whole-spectrum rate statements |
| research_matched_sphere_morse_source.md | Inverse cut, actual endpoint connections, knot parity, degree/clock/even-coset normalization |
| actual_global_left_weighted_spectral_envelope.md | Original finite sector/unused factors, uniform envelope and endpoint meaning |
| general_source_regulator_hyperbolic_equality.md | Hypotheses, compact core, primitive tube completion, same-chain comparison |
| general_peripheral_representation_volume_bound.md; actual_pretzel_marked_regulator_and_filling_action.md | Identification of the further boundary-chain/regulator dependencies, not a new full proof audit |
| manuscript_logic.json; check_manuscript_logic.py | Semantic N–Q interface comparison and private execution of structural checks |

I did not reprove N's entire Chebyshev/Hermite calculation, every global cofactor estimate, O's complete contour/all-charge tail argument, or the bottom-level Bloch-boundary/fundamental-chain identities this turn. These remain written mathematical imports, not newly verified Lean theorems. Nor did I rerun the seventeen-region exact interval certificates.

The new thin-face research was frozen separately at /private/tmp/md-thin-face-source-certificate-extension.md, retaining its independent-review obligations. It is not an input to this audit or the published P/Q conclusions.
