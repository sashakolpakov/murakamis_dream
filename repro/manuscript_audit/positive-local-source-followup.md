# Positive local source inputs to the central filling period

This bounded reading checks the finite circle determinants, positive pair traces, and cleared-cofactor amplitudes used by Appendix O. It starts from commit 2301771b66296cb7f2331938f1bfe0855719dd3d. The [snapshot](positive-local-source-followup-snapshot.json) records the exact versions, sections read, private derivations, and finite diagnostics.

No mathematical correction was identified in these local inputs. This is not a new proof of the complete source compiler or the full invariant theorem. The [source-adapter reading](marked-source-adapter-followup.md) separately follows the stated local matrices through the original face grids, cup/cap characters and coefficient targets. The [finite source and filling record](finite-source-and-filling-followup.md) records the later functional, analytic and geometric interfaces.

## The actual positive polynomial

Let \(N\) be the root level, \(d=N-1\), \(\theta=\pi/N\), \(q=e^{i\theta}\), and \(Q=q^2\). The complete channel has \(0\le a\le\lfloor d/2\rfloor\), with deficit \(s=d-2a\). Put
\[
 S_j=\prod_{r=1}^j2\sin(r\theta),\qquad
 \beta_a=S_{2a}/S_a^2,\qquad
 D_a(x,b,y)=\det(bI+xH_-/2+yH_+/2).
\]
Here \(x,y\) are the outer face variables and \(b,c\) the two middle variables at one crossing circle. The [literal white/cup calculation](../../notes/actual_complete_circle_positive_face_polynomial.md), §§1–4, gives
\[
 h_{0,a}W_a\pi_a
 =k_a\beta_a^2
 \frac{D_a(x,b,y)D_a(x,c,y)\widetilde P_s(x,y)}{(bc)^{d/2}},
 \qquad
 \widetilde P_s=\prod_{j=a+1}^{d-a}(x-Q^jy).
\]
The multiplicity is \(k_a=1\) at the odd simple fold and \(2\) otherwise. The physical half-index, cup normalization, and any retained half-twist scalar remain in this identity. Additional head lifts have the character \((-1)^{d(n_R+n_S)}\); its global treatment belongs to the source adapter.

The matrices \(H_\pm\) are the specified finite Hermitian matrices, not limiting models. Denote their common diagonal by \(d_n\) and their squared adjacent magnitude by \(b_n\):
\[
 d_n=\frac1{\cos(n\theta)\cos((n+1)\theta)},\qquad
 b_n=\frac{\sin^2(n\theta)}
 {\cos^2(n\theta)\sin((2n-1)\theta)\sin((2n+1)\theta)}.
\]
The diagonal has \(0\le n<a\), and the adjacent entries have \(1\le n<a\). Their LDL pivots are
\[
 p_{n-1}=\frac{\sin(n\theta)}
 {\cos(n\theta)\sin((2n-1)\theta)}>0.
\]
The identity \(p_n=d_n-b_n/p_{n-1}\) follows directly from sine addition. It uses only actual rows with \(2a<N\), so it includes both maximal folds. In particular
\[
 \det(H_\pm)/2^a=\beta_a^{-1}.
\]
Cauchy–Binet then gives nonnegative coefficients of \(D_a\). Subtracting a small positive multiple of the identity from each positive summand shows that every homogeneous degree-\(a\) coefficient is strictly positive. This is finite positivity, not a uniform lower bound for each coefficient.

The forced factor is also exactly positive:
\[
 \widetilde P_s(x,y)=
 \sum_{j=0}^s\frac{S_s}{S_jS_{s-j}}x^{s-j}y^j.
\]
The phase cancellation uses \(2a+1+s=N\). At the maximal fold this factor is \(1\) for odd levels and \(x+y\) for even levels. The corresponding \(\beta_a\) is \(1\) or \(\csc(\pi/N)\); the interpolation keeps that finite anchor.

The determinant conversion was followed through the [joint finite recurrence](../../notes/actual_q_hahn_joint_accretive_determinant.md), §§1–4, the [second tridiagonal model](../../notes/actual_q_hahn_full_physical_complex_packet.md), §1, and the [exact clock conversion](../../notes/actual_q_hahn_complementary_hard_edge.md), §4. The full representation-theoretic derivation of the initial Casimir equation was not repeated.

## Pair traces and fixed complex neighborhoods

For positive semidefinite matrices \(X_j\) with \(M=\sum_jX_j>0\), set \(A_j=M^{-1/2}X_jM^{-1/2}\). Their sum is the identity. Thus \(B=\sum_je^{i\vartheta_j}A_j\) is a contraction, and direct trace expansion gives
\[
 \operatorname{Tr}(I-B^*B)=
 \sum_{i<j}|e^{i\vartheta_i}-e^{i\vartheta_j}|^2
                         \operatorname{Tr}(A_iA_j).
\]
Applying \(\log t\le t-1\) to squared singular values yields the global determinant penalty. No commutativity of \(H_-\) and \(H_+\) is assumed.

The [finite curvature proof](../../notes/actual_q_hahn_boundary_model_curvature.md), §§2–5, supplies order-\(N\) lower pair traces. For a positive middle variable, divide by \(b\) and write \(M=I+X+Y\), where \(X=xH_-/(2b)\) and \(Y=yH_+/(2b)\). Disjoint LDL squares in a fixed interior range give \(X\ge cP\), where \(P\) is a projection of rank at least \(cN\). Scalar Jensen applied to each selected vector gives \(\langle w,M^{-2}w\rangle\ge\langle w,Mw\rangle^{-2}\). Tracing proves the needed lower bound even when terminal entries grow at the fold.

For a protected middle variable, the exact boundary formula is
\[
 D_a(x,0,y)=\beta_a^{-1}
 \sum_{k=0}^a\left(\frac{S_a}{S_kS_{a-k}}\right)^2x^{a-k}y^k.
\]
Its logarithmic curvature is a variance. The exact adjacent-weight ratio puts the mode a positive fraction of \(N\) from both ends and gives upper Gaussian tails and two separated intervals of positive probability. Hence that variance also lies between \(cN\) and \(CN\). A triangle with only one positive variable is a monomial and imposes no angular condition.

Small complex relative changes precondition the determinant to \(I+E\), with \(\|E\|<1/2\) on a neighborhood independent of \(N\). The relative matrix logarithm is therefore holomorphic, and its fixed derivatives are \(O(N)\) on smaller neighborhoods. Protected zero variables remain exactly zero.

## The actual cofactor is needed off the nodes

The [interior-start proof](../../notes/actual_cross_cofactor_interior_packet.md), §§1–5, starts from the original upper two-diagonal matrix on rows \(0,\ldots,j\). Its diagonal is \(a_r+u\), where \(a_r=4\cos^2((r+\tfrac12)\pi/N)\) and the spectral parameter is \(\sigma=-2-u\). Define \(R_j(b,u)\) by replacing its last row with \((1,b,\ldots,b^j)\) and taking the determinant. This row-replaced cofactor and its recurrence are polynomial even when a diagonal vanishes. At the physical complete node the exact adapter is
\[
 R_a(b,-a_a)=S_{2a}D_a(x,b,y),\qquad
 \prod_{r<a}(a_r-a_a)=S_{2a}.
\]
This does not identify an arbitrary off-node cofactor with a moving-dimensional determinant.

For positive \(b\), the original sum over starting rows has a strict interior saddle. If \(\lambda_+\) and \(\lambda_-\) are the dominant and smaller characteristic roots of its limiting transfer recurrence at the starting row, put \(k_0=-\lambda_-/\lambda_+\). The dominant root is a unit, and its initial projection tends to \(1/(1+k_0)>0\). Nested analytic contractions and finite endpoint anchors give a relative packet on a fixed complex neighborhood. The proof retains all other starts and the vertical sides of the finite-grid contour.

For \(b=0\), the [protected-middle proof](../../notes/actual_cross_cofactor_protected_packet.md) instead keeps the initial negative transfer branch. The ratio \(r=\lambda_-/\lambda_+\) starts at \(-1\), while \(1-r\) remains separated from zero. A near-identity conjugation and product estimate suppress that branch without discarding it. The surviving coefficient is a holomorphic unit. If an outer face also vanishes, the exact monomer product applies.

The exact even and odd central formulas have unit multiplying factors near completeness. With \(A=x+y\), \(P=xy\), \(S=\sqrt{A^2+uP}\), and \(\Lambda_*=2(A+S)\), their limits are
\[
 4A+8uP/\Lambda_*=4S,\qquad
 1+4uP/\Lambda_*^2=2S/(A+S).
\]
The odd term proportional to \(u\), including its derivative, is retained.

Write \(\mathcal B_N\) for the finite-level analytic fold interpolant of the complete-circle polynomial, and \(P_{\mathrm C}\) for the original central-cut cofactor numerator with its sign \((-1)^d\) included. The [fold interpolation](../../notes/actual_positive_face_exponential_fold_interpolation.md), §§1–6, keeps the exact finite anchor. The [cofactor rigidity proof](../../notes/actual_cross_cofactor_interpolant_rigidity.md), §§2–4, combines its exponentially accurate node values with the independently established off-node growth. Finite Cauchy–Lagrange interpolation on both parity grids then gives
\[
 P_{\mathrm C}=N^2\mathcal B_N(1+O(e^{-\kappa N}))
\]
on a fixed smaller complex neighborhood, with fixed derivatives. Nonvanishing is established before this interpolation. The \(N^2\) node adapter is a separate source identity; no extra derivative or paired multiplicity is imposed at the odd simple node.

## What reaches Appendix O

For a fixed simple white sphere marked at an unmatched edge, removing its two protected endpoints leaves a connected ordinary graph. No matching edge has both protected endpoints. Every crossing therefore has \(x+y>0\) and at least one nonmonomial triangle. The pair-trace penalties along a spanning tree eliminate every phase except common rotation; the phase differences have primitive integer coefficient \(1\).

The [positive coefficient proof](../../notes/actual_positive_face_coefficient_saddle.md), §§2–4, uses the original targets and total degree to remove that common rotation with integral exactly \(1\). Given the supplied geometric angle-force identity, its finite critical radius and nonzero Gaussian amplitude follow from the Hessian and complex derivative bounds. The [global angular cofactor proof](../../notes/actual_cross_cofactor_global_angular_gap.md), §§1–4, retains positive node tails and handles omitted terminal nodes before extending to the real spectral interval and a thin strip.

These are the local inputs to [H1 in the Morse central-period theorem](../../notes/actual_morse_cross_filling_period.md), §§2–4. H2 additionally uses the [strict real-spectral rate comparison](../../notes/actual_global_cross_spectral_gap.md), §§1–2, read in the earlier O analytic follow-up. Positivity alone does not prove H2.

All diagrams and positive compacts are fixed. Constants and neighborhoods may depend on them. The reading does not establish growing-diagram uniformity, the full Morse compiler, the complete Casimir/Hermite derivation, geometric existence or absolute volume calibration, the later filling contour, or suppression of one-sided sectors. Finite identity checks supplement the written arguments; they do not establish uniform estimates. In particular, a nonzero central period is not by itself the full-invariant volume theorem.
