# Positive circle determinants and the central cofactor packet

This is a bounded reading of the finite positivity, pair-trace, and cofactor inputs used by Appendix O. The initial publication checkout was commit 2301771b66296cb7f2331938f1bfe0855719dd3d. The companion snapshot records exact source hashes and sections read. No publication source was changed for this private report.

These inputs have written proofs with the required fixed-diagram, both-parity scope. I found no correction to their mathematical statements. Coefficient positivity at a complete root is not being used as positivity at arbitrary complex spectra. The latter neighborhood is obtained from separate cofactor recurrences, nonzero initial projections, and analytic interpolation.

This conclusion is conditional on the specified white/cup formula and its Casimir/Hermite adapter being the original invariant source. Their full representation-theoretic derivation and the global Morse compiler are outside this reading. So are suppression of one-sided sectors, the later spectral filling contour, and absolute geometric volume calibration.

## 1. Exact source and parity

The formula read in actual_complete_circle_positive_face_polynomial.md, §§1–4, is at the fixed root
\[
 \theta=\pi/N,\quad q=e^{i\theta},\quad Q=q^2,\quad d=N-1,\quad
 0\le a\le\lfloor d/2\rfloor,\quad s=d-2a.
\]
Put
\[
 S_j=\prod_{r=1}^j2\sin(r\theta),\quad
 \beta_a=S_{2a}/S_a^2,\quad
 D_a(x,b,y)=\det(bI+xH_-/2+yH_+/2).
\]
The variables \(x,y\) are the outer faces and \(b,c\) the two middle faces of the same crossing. With the specified centered physical head logarithms, the whole circle coefficient is
\[
 h_{0,a}W_a\pi_a
 =k_a\beta_a^2
 \frac{D_a(x,b,y)D_a(x,c,y)\widetilde P_s(x,y)}{(bc)^{d/2}},
 \qquad \widetilde P_s=\prod_{j=a+1}^{d-a}(x-Q^jy),
 \tag{1}
\]
where \(k_a=1\) at the odd simple fold \(s=0\), and \(k_a=2\) otherwise. Its proof keeps the actual cup, \(\gamma_a=q^{2-a^2}/N^2\), and \(h_{0,a}=k_aN\beta_a\), without inverting an exceptional paired norm.

I checked the scalar reduction using \(F_j=(-i)^jq^{j(j+1)/2}S_j\), \(S_{d-j}=N/S_j\), and \(K_a=q^{a^2}\beta_a\). The remaining ratio is \(q^{-2N(-2N+a+3)}=1\). The physical half-index substitution gives
\[
 H_a(-q^{-1}x/b,-q^{-1}b/y)
 =(-q^{-1})^aK_a y^{-a}D_a(x,b,y).
\]
The outer sine product has scalar \(i^sq^{-sN/2}=1\), and \(d=2a+s\) cancels the remaining face powers. Additional \(N\)-lifts retain the character \((-1)^{d(n_R+n_S)}\). Its global cancellation is an input from the compiler, not a local convention.

At the maximal fold, the forced factor is \(1\) for odd \(N\) and \(x+y\) for even \(N\). The corresponding \(\beta_a\) is \(1\) and \(\csc(\pi/N)\), respectively. The finite fold interpolation retains these scalars in its exact anchor.

## 2. Actual matrix positivity and coefficient support

The matrices \(H_\pm\) have diagonal
\[
 d_n=[\cos(n\theta)\cos((n+1)\theta)]^{-1}
\]
and adjacent entries \(\sqrt{b_n}(\sin(n\theta)\pm i\cos(n\theta))\), where
\[
 b_n=\frac{\sin^2(n\theta)}
 {\cos^2(n\theta)\sin((2n-1)\theta)\sin((2n+1)\theta)}.
\]
They are diagonal-unitarily equivalent to the real Jacobi matrix with adjacent entries \(\sqrt{b_n}\).

The endpoint positivity check can be derived directly. The LDL pivots are
\[
 p_{n-1}=\frac{\sin(n\theta)}
 {\cos(n\theta)\sin((2n-1)\theta)}.
 \tag{2}
\]
The first is \(1/\cos\theta\). Also \(b_n/p_{n-1}=\sin(n\theta)/[\cos(n\theta)\sin((2n+1)\theta)]\). Subtracting this from \(d_n\) and using the sine addition identity gives \(p_n\). Every denominator is positive for the actual rows, since \(2a<N\); no virtual endpoint pivot is used. Consequently
\[
 2^{-a}\det H_\pm
 =\frac{\prod_{r=1}^a\sin(r\theta)}
 {\prod_{r=a+1}^{2a}\sin(r\theta)}
 =\beta_a^{-1}>0.
 \tag{3}
\]

Cauchy–Binet for the three positive summands expresses every coefficient of \(D_a\) as a sum of squared minors. Subtracting a sufficiently small multiple of \(I\) from each summand leaves them semidefinite and supplies a positive multiple of \((x+b+y)^a\). Thus every degree-\(a\) monomial has a positive coefficient. This is finite positivity, not an \(N\)-uniform lower bound for individual coefficients.

The forced factor has the exact expansion
\[
 \widetilde P_s(x,y)=\sum_{j=0}^s
       \frac{S_s}{S_jS_{s-j}}x^{s-j}y^j.
 \tag{4}
\]
Its Gaussian-binomial phase cancels because \(2a+1+s=N\), and \(s<N\) makes all sine coefficients positive. These facts establish positivity of the degree-\(d\) polynomial in (1), after separating its recorded Laurent character.

The exact finite white determinant is traced through actual_q_hahn_joint_accretive_determinant.md §§1–4, actual_q_hahn_full_physical_complex_packet.md §1, and actual_q_hahn_complementary_hard_edge.md §4. The chain is the specified Newton polynomial, its joint Casimir coefficient recurrence, the monic three-term recurrence, and the determinant with the same recurrence and initial values. I checked this recurrence/determinant conversion and normalization, not the full Hopf derivation of the Casimir equation.

## 3. Protected-middle curvature

The exact boundary polynomial is
\[
 D_a(x,0,y)=\beta_a^{-1}
 \sum_{k=0}^a\left(\frac{S_a}{S_kS_{a-k}}\right)^2x^{a-k}y^k.
 \tag{5}
\]
It follows from the boundary specialization of the finite white determinant, or its tridiagonal coefficient recurrence; (3) fixes the leading scalar.

For \(w=y/x>0\), logarithmic curvature is the variance of \(k\) under weights proportional to \((S_a/(S_kS_{a-k}))^2w^k\). Their exact ratio satisfies
\[
 R(k)=w\left[\frac{\sin((a-k)\theta)}{\sin((k+1)\theta)}\right]^2,
 \qquad
 (\log R)'(t)=
 -\frac{2\theta\sin((a+1)\theta)}
 {\sin((a-t)\theta)\sin((t+1)\theta)}.
 \tag{6}
\]
For \(a_0N\le a\le\lfloor d/2\rfloor\) and a fixed positive compact of \(w\), the mode stays \(cN\) from both endpoints. The derivative is at most \(-c/N\) everywhere and has absolute value at most \(C/N\) in a fixed bulk around the mode. Multiplying the ratios gives Gaussian upper tails and comparable weights on two separated intervals of length \(\sqrt N\). Their probabilities are bounded below after normalization, so \(cN\le\operatorname{Var}(k)\le CN\). This is the full written proof in actual_q_hahn_boundary_model_curvature.md §4. One-variable triangles remain monomials and supply no angular penalty.

## 4. Pair-trace identities and uniformity

Let \(X_j\ge0\), \(M=\sum_jX_j>0\), \(A_j=M^{-1/2}X_jM^{-1/2}\), and \(B=\sum_je^{i\vartheta_j}A_j\). Since \(\sum A_j=I\), \(B\) is a compression of a unitary. Direct cyclic trace expansion gives
\[
 \operatorname{Tr}(I-B^*B)=
 \sum_{i<j}|e^{i\vartheta_i}-e^{i\vartheta_j}|^2
                       \operatorname{Tr}(A_iA_j).
 \tag{7}
\]
The pair traces are nonnegative. Applying \(\log t\le t-1\) to squared singular values gives
\[
 |\det B|\le\exp\!\left[-\frac12\sum_{i<j}
 |e^{i\vartheta_i}-e^{i\vartheta_j}|^2\operatorname{Tr}(A_iA_j)\right].
 \tag{8}
\]
The singular case follows by continuity; no commutation of \(H_-\) and \(H_+\) is used.

For \(M=I+X+Y\), direct differentiation gives
\[
 D^2\log\det M=
 u^2\operatorname{Tr}(XM^{-2})+
 v^2\operatorname{Tr}(YM^{-2})+
 (u-v)^2\operatorname{Tr}(M^{-1}XM^{-1}Y).
 \tag{9}
\]
The actual second raw clock is inverted, changing the last square to \((u+v)^2\). The source note retains that sign.

For the lower bound, disjoint adjacent LDL squares wholly inside a fixed bulk interval give \(X\ge cP\), with \(P\) a projection of rank at least \(cN\). Its normalized vectors satisfy \(\langle w_j,Mw_j\rangle\le C\). Scalar Jensen for their spectral measures gives \(\langle w_j,M^{-2}w_j\rangle\ge C^{-2}\). Tracing the positive inequality proves \(\operatorname{Tr}(XM^{-2})\ge cN\), and separately the same for \(Y\). This is a trace argument, not a false operator-monotonicity assertion about inverse squares. It remains valid when terminal matrix entries grow at the fold.

These are the middle–outer pair traces for a positive middle; (5)–(6) give the outer–outer trace when the middle is protected. Thus every nonmonomial triangle has an order-\(N\) angular penalty on the entire phase torus.

Fixed small complex relative coefficient changes have
\[
 M(\zeta)=M^{1/2}(I+E(\zeta))M^{1/2},\qquad \|E(\zeta)\|<1/2.
 \tag{10}
\]
This follows from \(\sum A_j=I\), also with protected zeros fixed. The relative matrix logarithm is single valued, of size \(O(a)\), and all fixed derivatives are \(O(N)\) on smaller fixed neighborhoods. No neighborhood shrinking with \(N\) is hidden here.

## 5. The original positive coefficient

The graph inputs are a fixed simple triangulated white sphere and a marked unmatched edge \(uv\), with only \(u,v\) set to zero. The induced ordinary graph is connected: reroute paths along the first deleted vertex's link cycle, then along the second's link with the first vertex removed. Simplicity prevents a matching edge from having both protected endpoints. Thus \(x+y>0\) at every crossing, and at least one of its two triangles is nonmonomial.

These are exactly the graph facts used in actual_positive_face_coefficient_saddle.md §§2–4 and actual_morse_cross_filling_period.md §§2–4. Formula (8) along a fixed spanning tree gives a penalty off the common phase. Individual phase differences have integer coefficient \(1\), so after fixing one ordinary face there is no extra phase alias.

The target is \(d\) at each ordinary face, and total numerator degree is \(dR\), so the common angular integral is exactly \(1\). The geometric angle-force input makes the supplied packing critical for the limiting pressure. The finite Hessian is between \(c_DNI\) and \(C_DNI\); uniform holomorphic derivative bounds give a nearby actual finite critical radius. The original Cauchy torus, global angular penalty, and Gaussian calculation give a positive coefficient with a nonzero determinant prefactor.

This reading does not redo the geometric angle-force or absolute coned-facet volume proof. It also does not infer an off-node central packet from coefficient positivity alone.

## 6. Actual cofactor amplitudes

The cleared cofactor is the determinant of the original upper two-diagonal matrix with its last row replaced. Hence it extends polynomially across every vanished diagonal. Its exact path expansion is
\[
 R_j=b^j\prod_{r<j}\alpha_r+p_jR_{j-1}+q_jR_{j-2},
 \quad p_j=s_j^2(x+y),\quad q_j=s_js_{j-1}\alpha_{j-1}xy.
 \tag{11}
\]
Here \(\alpha_r=4\cos^2((r+\tfrac12)\pi/N)+u\). The independent symbolic check verifies the row-replacement recurrence with formal diagonal and superdiagonal entries.

At a physical node, the zero diagonal removes later starts and gives
\[
 R_j(b,-a_a)=K_{a,j}(-a_a)R_a(b,-a_a),\qquad
 R_a(b,-a_a)=S_{2a}D_a(x,b,y).
 \tag{12}
\]
The second equality uses the original complete-node identity and comparison of the monic \(b^a,c^a\) coefficients. Its scalar is fixed by
\(\prod_{r<a}(a_r-a_a)=\prod_{r<a}4\sin((a+r+1)\theta)\sin((a-r)\theta)=S_{2a}\).
Cancellation is in a polynomial domain, not division by a possibly zero numerical factor.

For \(b>0\), the actual start sum has a unique interior saddle. Nested-domain Riccati iteration around its dominant transfer root has a contraction factor below one. Its initial projection is an analytic truncated sum with limit \(1/(1+k_0(t))>0\). The smaller root may vanish, but is never inverted. Prefix logarithms are used only below the interior start, where the diagonal is nonzero. Optimally truncated Euler–Maclaurin sums retain finite anchors and have exponential errors. Starts outside the saddle interval retain their exponential penalty under sufficiently small fixed complex perturbations. The finite cotangent-grid contour retains, and bounds, its vertical sides. These are the written steps in actual_cross_cofactor_interior_packet.md §§2–5.

For \(b=0\), that start saddle is inapplicable. The separate protected packet keeps the initial negative transfer branch. At the lower endpoint its ratio is \(-1\), but \(1-r\) stays separated from zero. Near-identity diagonalization leaves \(O(N^{-2})\) error per step; the negative product is exponentially small by a positive terminal proportion. The initial positive coefficient is exactly \(1/g_0\), giving the holomorphic unit
\[
 \frac{\lambda_{n,+}}{g_0}
 \prod_{j=1}^n\frac{\lambda_{j-1,+}-\lambda_{j,-}}{g_j}.
 \tag{13}
\]
If one outer face also vanishes, the exact monomer product applies instead. The all-zero triangle is excluded by the stated graph hypotheses.

For the whole crossing let \(A=x+y\), \(P=xy\), \(S=\sqrt{A^2+uP}\), \(\Lambda_*=2(A+S)\). The actual terminal ratios converge uniformly to \(\Lambda_*\). The exact even and odd central factors tend respectively to
\[
 4A+\frac{8uP}{\Lambda_*}=4S,\qquad
 1+\frac{4uP}{\Lambda_*^2}=\frac{2S}{A+S}.
 \tag{14}
\]
They are units near \(u=0\), also at a protected outer face. Thus the central-cut sum cannot cancel its local amplitude. The odd term proportional to \(u\), including its derivative, is retained.

## 7. The specific H1/H2 dependency

The complete-fold interpolation keeps the exact finite anchor \(B_{N,M}\). Nested analytic contractions construct approximate pivots with exponential residuals; comparison with actual pivots gives exponential accuracy on the physical channel grid. This is read in actual_positive_face_exponential_fold_interpolation.md §§1–6.

The actual cofactor packets and this interpolation have uniform normalized holomorphic logarithms. Their dense physical node values force agreement of the limiting logarithms. Thus their ratio has subexponential outer-circle growth. The finite Cauchy–Lagrange formula on the \(j/N\) or \((j+\tfrac12)/N\) grid and its reflection then gives
\[
 P_{\mathrm C}=N^2\mathcal B_N(1+O(e^{-\kappa N}))
 \tag{15}
\]
on a smaller fixed complex face and spectral neighborhood. The denominator was proved nonzero before interpolation. Cauchy estimates give fixed derivatives. This is actual_cross_cofactor_interpolant_rigidity.md §§2–4, not a differentiation of value-only node data.

The \(N^2\) is the specified cofactor/complete-node adapter. The odd simple node contributes a value in the Hermite functional, not an extra derivative or paired multiplicity. Its complete derivation belongs to the separate Casimir/Hermite audit.

The angular complement also uses the exact post-node tail
\(q_r=(x+y)q_{r-1}-\gamma_rxyq_{r-2}\), \(0\le\gamma_r\le1\).
Induction on \(q_r-xq_{r-1}\) proves its coefficientwise positivity and monomer upper bound. Near nodes use (8); far nodes have a strict path penalty. Exact cosine-grid interpolation extends to the real spectral interval. For finitely omitted terminal nodes the proof first multiplies by their factors, then proves division costs only a polynomial. A polynomial exterior estimate supplies the thin complex strip.

This supplies the local unit, positivity, and angular inputs to actual_morse_cross_filling_period.md lines 109–162. Its fixed complex neighborhoods and constants depend on the fixed diagram and compact; there is no growing-diagram claim. H1 follows on the prescribed face torus once the declared angle-force input is supplied.

For H2, the strict real-spectral comparison additionally uses actual_global_cross_spectral_gap.md §§1–2. Its full block-transfer and prefix-integrability argument was read in the previous O analytic audit and has not been repeated here. Pair traces alone do not imply H2. Neither the later spectral filling period nor the noncentral remainder has been re-audited here.

## 8. Finite checks and exclusions

The companion script checks formal row-replacement identities and independently compares finite Newton polynomials, matrices, LDL normalization, (5), the nodal scalar, forced factors, and pair traces at both parities. It replays the original literal white/dual-cup scalar test by loading only its named function bodies. Results are recorded separately. These are finite algebra diagnostics, not proofs of uniform analytic estimates.

Still outside this report are the complete quantum representation/Casimir/Hermite derivation; the exact global Morse compiler and its carriers, grid measure, cup/cap characters and targets; positive packing existence and absolute action-volume calibration; the later whole spectral filling period and primitive metric completion; full-source restoration; moving-\(q\) and external-color/all-orders claims.

The older local notes' historical statements that the filling period remained open do not alter the local results checked here. Their current use is the explicitly central-only theorem in actual_morse_cross_filling_period.md. Its H1/H2 do not prove the full invariant theorem for every simple sphere without a separate remainder argument.
