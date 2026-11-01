# Marked fillings: construction and proof dependencies

Source snapshot: 2 November 2026.

This is a bounded mathematical read of `papers/marked-fillings/main.tex`, Sections 1–6 (lines 45–1022 in the pinned version), and of the corresponding import in `papers/three-braids/main.tex`. I read the actual construction and compared the relevant packing, original-cut and metric-completion arguments with the supporting notes listed in the adjacent snapshot. I did not run a build, finite checker, or formal proof during this read.

**Conclusion.** I found no remaining reference-manuscript premise in the construction of the original complete exterior, its marked holomorphic deformation, the independently signed critical point, or its smooth primitive filling. These parts supply the geometric construction needed by the three-braid paper. The equality with the absolute real action additionally uses Section 7; that section is under a separate review and is not included in this conclusion. This report does not certify the entire paper or the analytic source and filling companions.

The pinned marked-paper SHA256 is `a0d792eea4336ea0bbe7c9c274780539db2b57e80836525210ba16728661000e`. The pinned three-braid SHA256 is `9bad961bfcb9893bf0b6035a084d95436e0c146b3acda10850ba7d374a832c76`.

## 1. Hypotheses and the complete exterior

The actual input is a finite connected simple oriented white triangulated sphere, a perfect matching in its cubic dual, a nonmatching marked strand edge, the native ordered crossing-disk charts, and retained half twists. The original component pairing determines whether the filled object is a knot or a link. The theorem does not replace this input by an abstract representation or by an unlabeled circle pattern.

At `mf:packing` and the subsequent development argument (lines 213–305), the strict Hall inequalities are sufficient for the positive corner allocation used by the entropy maximum. For a nonempty interior vertex set, the punctured planar count gives at least (2|S|+1) incident triangles. For a destination set containing the pooled boundary, the complementary all-interior graph gives the second strict Hall inequality. The empty interior set is not used in the strict inequality. Boundary exclusion uses the actual singular entropy derivatives; strict concavity then gives the multipliers and the tangent-circle angle formula.

The development is more than a local flatness assertion. Vertex angle sums remove local holonomy; the fixed convex boundary triangle and degree-one argument give an embedded developed disk. The disk-sector argument excludes unwanted contacts and supplies the remote supporting inequalities, including the complementary shaded disk at the omitted outer face. Consequently the medial polyhedron is the required positive convex ideal polyhedron, rather than an assumed certificate.

The inverse cut in lines 314–377 retains all four native terminal labels. The original half-disks cancel the handles introduced by drilling the boundary-parallel semicircles, so the two projection pieces are balls. This argument does not assume a tree. The finite edge cycles have the correct angle and full holonomy: preserving their endpoint and normalized horospheres excludes an axial displacement. The cusp links and their primitive paths come from the original exterior. The positive ideal subdivision uses compatible white-face subdivisions and strict support.

The complete action at `mf:Phi` is compatible with the source normalization. With $\theta_i=2\pi a_i$, the geometric triangle expression equals

\[
 \sum_i a_i\log w_i+\frac1\pi\sum_i
 \left[\Lambda(\pi a_i)+\Lambda\left(\frac\pi2-\pi a_i\right)\right],
\]

which is the entropy normalization used by the source companion. There are \(2R\) triangle terms of degree \(1/2\) and \(R\) ordinary targets; common rescaling therefore cancels from the critical action. The geometric strip-width gauge and the source fixed-face gauge do not introduce an additive normalization.

## 2. The marked Jacobian and holomorphic pattern

The square system `mf:circle-system` and the rank statement `mf:pattern-rank` use the explicitly fixed translation and strip scale. The positive-conductance Laplacian in `mf:hessian` has only common-scale kernel because deleting the adjacent protected vertices leaves the ordinary graph connected. The link-rerouting proof supplies this connectedness for the stated simple sphere; it is not inferred from numerical Hessian values.

The two line-adjacent triangles eliminate the common scale in the fixed strip. With radii fixed, each finite tangent-center triangle has only an infinitesimal Euclidean motion, and each one-line triangle only a horizontal translation. Agreement across the connected developed disk propagates a single translation, removed by the fixed coordinate. Thus the real Jacobian has zero kernel, and its complexification is invertible at the complete real point.

One wording precision was identified and the author applied it before this snapshot: lines 466–468 now say that the infinitesimal deformation preserves the **cyclic order**, with angle sums remaining \(2\pi\). It does not assert that every individual angle is fixed. No mathematical change was needed.

The matched edge cannot have both outer vertices equal to the protected pair. Hence the needed local condition \(x+y>0\) holds for every actual matched pair, and each pair has a nonmonomial triangle. Degenerate triangles adjacent to the two marked lines are handled by the strip equation, not by division by a vanished radius. The selected flags continue holomorphically through the noncentral parabolic complete point using a nonzero off-diagonal entry.

## 3. Primitive peripheral words and global assembly

The maps `mf:P` and `mf:C` retain the full ordered puncture generators and the three prescribed points. The multiplier alone is not used as a substitute for the side-pairing. The formula for \(C\) has a regular nontrivial parabolic limit. The marked-line regularization and `mf:side-sign` fix the two side signs from the primitive cusp rectangle; zero terms cause no additional sign choice.

At `mf:hurwitz` the positive crossing is \((A,B)\mapsto(A^{-1}BA,A)\). The equal-trace identity with \(P=BA\) gives the conjugator \(H=P^{-1}-I\), and Cayley–Hamilton gives

\[
 H^2=(\operatorname{tr}P-2)P^{-1}.
\]

The threading word `[2,1,1,2]` gives inverse auxiliary transport and the disk longitude \(P\). Killing \(\mu+p\lambda\) sets the auxiliary word to \(P^{-p}\); the resulting transport \(P^p\) is the \(-2p\) twist. This checks the physical convention \(n=\epsilon-2p\), including negative powers, without changing outside paths.

The meridian in `mf:meridian-matrix` has determinant one and selected eigenvalue \(m\), using exactly \(m^2R_0(-J)^\epsilon=1\). The small longitude logarithm is centered projectively; the paper correctly avoids claiming that every centered local representative belongs to one global \(SL_2\) lift.

The prefix products in lines 775–805 telescope with the actual mutually inverse white maps. A cup or cap inserts a cancelling \((F,G,F)\) pair. The crossing map intertwines both puncture generators. These are the original Wirtinger and disk van Kampen relations, so arbitrary diagram cycles are retained. Main meridians stay noncentral parabolic; their commuting longitudes stay translations, with the original complete cusp marking.

## 4. Independent signed critical point

The separate evenness of the pure action gives the factorization used in `mf:channel-hessian`. At the complete point the coefficients have positive real part. The implicit-function parameter is the full vector \(t_e=1/n_e\), with derivative \(2\pi i I\); no bound on ratios of filling powers is imposed.

In particular, the displayed solution

\[
 \delta_e=-\frac{t_e}{1+i t_eB_e/\pi}
\]

has

\[
 \operatorname{Im}\delta_e=
 \frac{t_e^2\operatorname{Re}B_e}
 {\pi|1+i t_eB_e/\pi|^2}>0.
\]

This sign remains valid when \(B_e\) is complex. The exact action differential then gives the original primitive equation \(U_e+p_eV_e=-2\pi i\). It is not merely an exponentiated equation. The threshold is chosen in the independent small-parameter polydisk before a fixed signed filling tuple is selected.

## 5. Smooth completion and the order of logarithmic choices

Proposition `mf:completion-prop` states its geometric inputs explicitly: a framed representation near the complete one, the fixed primitive cusp bases, complete unfilled multipliers, and the primitive logarithmic filling equation. The preceding construction supplies these inputs for the selected critical point; the proposition does not assume that the deformed representation is already discrete.

The Lorentz average `mf:core-dev` constructs a positive local developing map on the compact core. The affine-equivariant link map and the whole tail `mf:link-dev`, `mf:tail-dev` extend it to each cusp. Their compact overlap can be interpolated while retaining a positive Jacobian. These steps do not infer a complete metric from a regulator alone.

For a filled cusp, at least one multiplier differs from one. The common finite fixed point \(q=b/(1-a)\) tends to infinity, whereas the developed fixed fundamental parallelogram and its fixed generator paths remain bounded. The logarithm of \(d-q\) therefore exists on the simply connected link cover. Its differential gives a nonsingular flat metric on the compact link torus, hence a complete Euclidean developing map and a rank-two period lattice.

The crucial order appears explicitly at `mf:actual-periods`: the actual periods along the **two fixed primitive generators** tend to zero, with estimate of the form \(L/(|q|-R)\). Their exponentials equal the peripheral multipliers, so smallness identifies them with the chosen small \(U,V\), removing the possible \(2\pi i\mathbb Z\) ambiguity. Only afterwards is the second period multiplied by the potentially large slope \(p\).

The resulting end contains a full punctured tube. Formula `mf:tube-metric` is the smooth cylindrical hyperbolic metric. The primitive period \(\pm2\pi i\) makes one angular turn, while a complementary period has nonzero real part. This fills the intended solid torus smoothly with the original meridian. Translation cusps remain complete. Completeness of the resulting finite-volume metric supplies the discrete faithful geometric realization.

## 6. Downstream import and remaining review boundary

The three-braid foundation `found:period` (beginning at line 679 in the pinned file) retains the original marked simple sphere, positive complete cut, connected ordinary graph, nonmonomial matched triangles, actual targets, and integer lattice. Its geometric construction is now supplied by this companion, not by an unresolved manuscript statement. Its source packet and whole oscillatory period are separately imported from the source-asymptotics and oscillatory-fillings companions.

The local limiting actions match because their complete values agree by the triangle normalization above and their spectral derivatives are the same continued \(-\Log(E_b/\sqrt D)\). The primitive logarithms in the three-braid display match `mf:peripheral`, including the signed half-twist contribution exactly once. No flat-plat, tree, weak-balance, or full positive-endpoint source hypothesis is silently needed for this geometric import.

To conclude the **absolute action-volume equality**, the three-braid paper still uses the marked paper's Section 7 regulator, absolute calibration and comparison with the same filled fundamental chain. That is a written component of the new companion, not an asserted open premise; its correctness is the scope of the other independent read. This report establishes no new full-source remainder estimate and does not identify a central contribution with the full invariant.

Standard tools used here include finite Hall/flow feasibility, strict concavity and the implicit-function theorem, elementary covering/development facts for complete flat and hyperbolic metrics, and the explicitly written local matrix identities. I found no additional specialized theorem from the old reference manuscript required in Sections 1–6.
