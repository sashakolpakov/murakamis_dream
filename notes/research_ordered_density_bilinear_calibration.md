# A full-matrix inequality for bilinear composition

22 November 2026. Research note; the public manuscripts remain frozen.

A surjective bilinear tensor admits explicit affine lower bounds in
the logarithms of arbitrary positive input and output metrics. The
density matrices in these bounds belong to a specified spectral family.
They are independent dual witnesses, rather than the actual marginals
of a tensor after a common choice of gauges.

The proof applies to the original anchored Conway multiplication,
including every Hermite channel. It supplies local inequalities for
the bounded-window certificate, but does not construct matching
geometric densities or evaluate their constants at the volume scale.

## 1. Ordered densities

All spaces are finite-dimensional complex Hilbert spaces. A density
matrix is positive semidefinite with trace one. Say that a density
\(\rho\) is ordered with a Hermitian matrix \(K\) if they have a common
orthonormal eigenbasis in which
\[
 K=\operatorname{diag}(k_i),\qquad
 \rho=\operatorname{diag}(w_i),\qquad
 (w_i-w_j)(k_i-k_j)\ge0\quad\hbox{for all }i,j.             \tag{1}
\]
Thus \([\rho,K]=0\) is required. Repeated eigenvalues cause no
ambiguity: diagonalize \(\rho\) within each eigenspace of \(K\).
Examples are the normalized identity, a normalized projection onto
the largest eigenvalues, and
\(\rho=e^{\alpha K}/\operatorname{tr}(e^{\alpha K})\) for
\(\alpha\ge0\). More generally, a nonnegative nondecreasing function
of \(K\), normalized to trace one, is allowed. An arbitrary density
need not satisfy (1). Within a tied eigenspace (1) need not make
\(\rho\) a scalar function of \(K\).

We write \(\operatorname{tr}\), \(\|\cdot\|_{\rm op}\), and
\(\|\cdot\|_{\rm HS}\) for trace, operator norm, and
Hilbert--Schmidt norm. All matrix logarithms below are those of
strictly positive matrices.

## 2. Logarithms and compression

Scalar integration in a spectral basis gives the norm-convergent
identity
\[
 \log B=\int_0^\infty
 \bigl\{(1+t)^{-1}I-(B+tI)^{-1}\bigr\}\,dt.                \tag{2}
\]
Inversion reverses positive-matrix order, as follows by conjugating
with a positive square root. Consequently (2) proves that
\(0<B\le C\) implies \(\log B\le\log C\).
No order-preservation assertion about exponentiation is needed.

Let \(V:\mathcal K\to\mathcal H\) be a coisometry:
\(VV^*=I_{\mathcal H}\). For \(B>0\), a Schur complement gives
\[
 V(B+tI)^{-1}V^*\ \ge\ (VBV^*+tI)^{-1}\quad(t\ge0).
                                                                    \tag{3}
\]
Indeed decompose \(\mathcal K=\operatorname{ran}V^*\oplus\ker V\).
The left side is the upper block of the inverse of \(B+tI\), namely
\((B_{11}+tI-B_{12}(B_{22}+tI)^{-1}B_{21})^{-1}\).
The subtracted Schur correction is positive, so this is at least
\((B_{11}+tI)^{-1}\). If \(\ker V=0\), equality holds directly.
Integrating (3) in (2), with the constant terms cancelled and
\(VV^*=I\), proves
\[
                 \log(VBV^*)\ge V(\log B)V^*.             \tag{4}
\]
The differences in these integrals converge in norm.

## 3. A positive factor and an ordered density

**Lemma 1.** Let \(D=e^K>0\), and let \(\rho\) satisfy (1).
For every \(B>0\),
\[
 \boxed{\quad
 \operatorname{tr}\{\rho\log(DBD)\}
 \ge \operatorname{tr}(\rho\log B)
                       +2\operatorname{tr}(\rho K).
 \quad}                                                       \tag{5}
\]

**Proof.** Put \(B_s=e^{sK}Be^{sK}\) and
\(R_{s,t}=(B_s+tI)^{-1}\). Differentiating (2),
\[
 \frac d{ds}\operatorname{tr}(\rho\log B_s)
 =\int_0^\infty
 \operatorname{tr}\{\rho R_{s,t}(KB_s+B_sK)R_{s,t}\}\,dt.  \tag{6}
\]
In the common eigenbasis in (1), use
\(B_sR_{s,t}=I-tR_{s,t}\) and
\[
 \int_0^\infty(R_{s,t}-tR_{s,t}^2)\,dt=I.
 \]
The latter follows by scalar integration on the spectrum of \(B_s\).
Subtracting \(2\operatorname{tr}(\rho K)\) from (6) gives
\[
 \begin{split}
 \frac d{ds}\operatorname{tr}(\rho\log B_s)
                  -2\operatorname{tr}(\rho K)
 &=2\int_0^\infty t\sum_{i,j}w_i(k_i-k_j)
                                  |(R_{s,t})_{ij}|^2\,dt\\
 &=\int_0^\infty t\sum_{i,j}(w_i-w_j)(k_i-k_j)
                                  |(R_{s,t})_{ij}|^2\,dt
 \ \ge0.                                                   \tag{7}
 \end{split}
\]
The second equality exchanges \(i,j\) in half the sum and uses
Hermitian symmetry. The differentiations are justified uniformly for
\(s\in[0,1]\): the positive matrices \(B_s\) have common positive
lower and finite upper spectral bounds. In the last integral only
off-diagonal terms matter. Near infinity they have
\((R_{s,t})_{ij}=O(t^{-2})\), whereas near zero the resolvent is
bounded. Thus the integrand is integrable.
Integrating (7) from zero to one proves (5). \(\square\)

For an invertible polar decomposition \(A=UD\), this also gives a
unary bound. Put
\(c=\|H_o^{1/2}AH_i^{-1/2}\|_{\rm op}^2\).
The inequality \(DU^*H_oUD\le cH_i\), logarithmic order, and (5)
give
\[
 \log\|H_o^{1/2}AH_i^{-1/2}\|_{\rm HS}
 \ge \operatorname{tr}(\rho\log D)
 +\tfrac12\operatorname{tr}(U\rho U^*\log H_o)
 -\tfrac12\operatorname{tr}(\rho\log H_i).                 \tag{8}
\]
Here \(\rho\) is ordered with \(\log D\). The rectangular result
below does not require inserting a separate unary gate.

## 4. The original surjective binary tensor

Let
\(A:\mathcal H_1\otimes\mathcal H_2\to\mathcal H_o\)
be surjective. Define
\[
 D=(AA^*)^{1/2}>0,\qquad V=D^{-1}A,\qquad VV^*=I.
                                                                    \tag{9}
\]
Choose a density \(\rho\) ordered with \(\log D\), and put
\[
 \omega=V^*\rho V,\qquad
 \rho_1=\operatorname{tr}_{\mathcal H_2}\omega,\qquad
 \rho_2=\operatorname{tr}_{\mathcal H_1}\omega,\qquad
 \beta=\operatorname{tr}(\rho\log D).                    \tag{10}
\]
Since \(VV^*=I\), \(\omega,\rho_1,\rho_2\) are densities.
The joint density \(\omega\) can be entangled; no product-density
replacement is made.

**Theorem 2.** For arbitrary positive \(H_o,H_1,H_2\),
\[
 \boxed{\quad
 \log\|H_o^{1/2}A(H_1^{-1/2}\otimes H_2^{-1/2})\|_{\rm HS}
 \ge \beta+\tfrac12\operatorname{tr}(\rho\log H_o)
       -\tfrac12\operatorname{tr}(\rho_1\log H_1)
       -\tfrac12\operatorname{tr}(\rho_2\log H_2).
 \quad}                                                       \tag{11}
\]

**Proof.** Write \(X_i=\log H_i\),
\(X=X_1\otimes I+I\otimes X_2\), and set
\[
 T=Ve^{-X}V^*>0,\qquad
 c=\|H_o^{1/2}DVe^{-X/2}\|_{\rm op}^2>0.
 \]
The definition of \(c\) gives
\(H_o^{1/2}DTD H_o^{1/2}\le cI\).
Conjugating and inverting gives
\[
                            DH_oD\le cT^{-1}.            \tag{12}
\]
Use logarithmic order in (12), then trace against \(\rho\).
Lemma 1 on the left, and (4) applied to \(e^{-X}\) on the right,
give
\[
 \operatorname{tr}(\rho\log H_o)+2\beta
 \le \log c-\operatorname{tr}(\rho\log T)
 \le \log c+\operatorname{tr}(\rho VXV^*).                \tag{13}
\]
The last trace equals
\(\operatorname{tr}(\rho_1X_1)+\operatorname{tr}(\rho_2X_2)\).
Since \(\log\|\cdot\|_{\rm HS}\ge\tfrac12\log c\),
rearrangement proves (11). \(\square\)

The metric matrices need not commute. Only the fixed calibration
density is restricted by (1).
For bilinear tree contractions, the output half-edge density is
\(\rho\), and the dual input half-edge densities are
\(\rho_1^{\mathsf T},\rho_2^{\mathsf T}\).
The parent tensor uses \(H_i^{-\mathsf T/2}\) on its dual index;
\(\operatorname{tr}(\rho_i^{\mathsf T}X_i^{\mathsf T})
=\operatorname{tr}(\rho_iX_i)\).

## 5. The full anchored Conway product

For each integer \(N\ge2\), use the complete Newton coefficient space
\[
 H_N=\mathbb C[z]/(2T_N(z/2)+2)
 \]
where \(T_N\) is the Chebyshev polynomial of the first kind. Use the
actual normalized Newton basis \(b_i\), with coefficient vectors
\(e_i=b_i\), and its Euclidean Hermitian norm.
It retains all value and first-normal channels at repeated Casimir
roots. Its actual multiplication \(M\) has unit \(b_0\), hence is
surjective. The anchored compiler uses
\[
 \widehat H_N=\mathbb C e_\star\oplus H_N,\qquad
 \widehat M((a,u),(b,v))=(ab,M(u,v)).                      \tag{14}
\]
This is surjective because
\(\widehat M((a,u),(1,b_0))=(a,u)\).
Thus (9)--(11) apply to the literal tensor without changing a
crossing leaf, a quarter-turn, or the original marked closing row.
All original framing and peripheral scalars remain prescribed.

Its covariance satisfies
\[
 \widehat M\widehat M^*=\operatorname{diag}(1,MM^*)\ge I.
                                                                    \tag{15}
\]
Indeed \(M(e_i\otimes e_0)=e_i=M(e_0\otimes e_i)\) in the
orthonormal Newton basis. These input columns are distinct except
at \(i=0\); their contribution gives
\(MM^*\ge2I-e_0e_0^*\ge I\).
Consequently every allowed \(\beta\) in (10) is nonnegative here.

The densities in (10) are independent dual data. They need not be the
actual reduced densities of any one gauged tensor. For example the
whitened map \(V\), after Hilbert--Schmidt normalization, has actual
output density \(I/\dim\widehat H_N\); this does not require choosing
that density in (10). No physical channel has been projected away.

There is also an explicit source-dependent change of reference that
requires no unknown internal packet. At a literal crossing leaf put
\(a_\pm=(1,R^{\pm1})\) and use the anchored shear
\[
 S_\pm(a,u)=(a,u-aR^{\pm1}),\qquad
 S_\pm a_\pm=e_\star,\qquad
 \|S_\pm\|_{\rm op},\ \|S_\pm^{-1}\|_{\rm op}\le1+\sqrt N.
                                                               \tag{16}
\]
The bound follows from the shear formula and the exact Newton norm
\(\|R^{\pm1}\|=\sqrt N\). Apply \(S_\pm^{-1}\) on the adjacent
parent input to preserve the complete contraction. Each affected local
logarithmic Hilbert--Schmidt norm changes by at most \(O(\log N)\);
the new parent map remains surjective, so Theorem 2 applies to it.
This is a known complex nonunitary reference change, rather than a
unitary rephasing. The bound \(D\ge I\) in (15) concerns the original
untransformed product, and is not asserted after this change.
The shear neither constructs globally matched densities nor proves
an upper volume rate.

## 6. Use on a fixed tree

For the exact anchored source \(Y_N=(1,K_N)\), the three complete
sources below give regularized minimizing metrics satisfying
\[
 \|\log H_e^*\|_{\rm op}\le R_N=O(N),\qquad
 \|Y_N\|\le\prod_v\|T_{v,N}\|_{H^*}\le2\|Y_N\|.           \tag{17}
\]
One can take \(R_N=L_N(I)/\varepsilon+\log Z(I)\), where
\(L_N=\sum_v\log\|T_{v,N}\|_H\),
\(Z=1+\sum_e\operatorname{tr}(H_e+H_e^{-1})\), and
\(\varepsilon=1/(512m^2)\) for a fixed tree with \(m\ge2\)
vertices.
For completeness, regularized stationarity gives total actual marginal
mismatch \(S\le2\varepsilon\). The capacity comparison is
\(\|Y_N\|/\prod_v\|T_v\|_{H^*}
\ge1-4m\sqrt S-5mS>1/2\) at this value of \(\varepsilon\).
Also \(L_N(H^*)\ge\log\|Y_N\|\ge0\); comparison of
\(L_N+\varepsilon\log Z\) at \(H^*\) and \(I\) gives
\(\log Z(H^*)\le R_N\). Each eigenvalue of \(H_e^*\) and its
reciprocal is at most \(Z(H^*)\), proving the other part of (17).

Use (11) at products and valid literal leaf, turn, and closing lower
bounds on this window. Let \(\delta_{e,N}\) be the trace-norm
mismatch between the child density and the transposed parent density.
Summing at \(H^*\) and bounding each residual trace gives
\[
 \log\|Y_N\|\ge
 \sum_v\beta_{v,N}-\frac{R_N}{2}\sum_e\delta_{e,N}-\log2.   \tag{18}
\]
Thus total density error \(o(1)\) costs \(o(N)\) in this logarithmic
certificate on a fixed tree. This is not a complex-source error bound.

Theorem 2 supplies an explicit valid family at the original product.
It does not prove that this restricted family contains geometric
data matching the actual leaves and closing with small error, or that
its constants sum to the hyperbolic-volume rate. Source-adapted
preconditioning may be needed. A separate full-metric upper trial is
also required. No exact entropy dual or new volume theorem is asserted.

## Sources and coverage

The matrix inequalities are proved above. These three entire sources
supply the physical compiler and the tree comparison in Section 6.

| Source | SHA-256 |
|---|---|
| [Full gauge capacity](research_scalar_tree_full_gauge_capacity.md) | 2997b732aa73e063c66e81d6487a1d9927509609d61842c1dbb43d9345df1d6d |
| [Regularized capacity](research_regularized_actual_source_capacity.md) | 0cea0d52182eb24b4610538f354dbe5158fa54aa6f9cf7f9fc280c72ab090ff8 |
| [Anchored physical compiler](research_anchored_conway_positive_variational_period.md) | e83c35d16c79faa13ac6556db78b9b57da2a2371d3fc04c4673ecd74e1d336f7 |

The co-ordering trace inequality underlying (7) is a standard
monotone-pair inequality: see Yanagi--Furuichi--Kuriyama,
[Lemma II.1](https://arxiv.org/pdf/quant-ph/0501152v2), and
Furuichi--Kuriyama--Yanagi,
[Lemma 1.5](https://arxiv.org/pdf/1001.1384), which credits Bourin
and Fujii. The compression inequality (4) is the logarithmic case of
operator Jensen; see Hansen--Pedersen,
[Theorem 2.1](https://arxiv.org/pdf/math/0204049).
These definitions and statements were checked for coverage. They are
not proof premises here, and no novelty claim about those inequalities
is made.

No mathematical program, numerical test, build, or manuscript edit was
used for this proof.
