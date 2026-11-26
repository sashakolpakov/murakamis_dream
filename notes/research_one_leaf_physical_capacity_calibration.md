# A polynomial reference for one prescribed matrix-product leaf

24 November 2026. Research note. Written proof.
Earlier finals and public manuscripts remain unchanged.

A known leaf of the actual physical matrix-product compiler can be
matched to its parent's full input density with an explicit polynomial
change of reference. The other input and output have specified
row/column-energy densities. These give a full-matrix logarithmic
inequality on every finite metric window, without selecting a largest
singular mode or using the unknown closed invariant.

The construction is one-sided. It does not match the second input to
an arbitrary subtree, or prove a geometric lower bound.

## 1. The actual matrix-product compiler

Let
\[
 {\cal A}=\bigoplus_{\nu=1}^{s}\operatorname{Mat}_D(\mathbb C),
 \qquad
 \|A\|^2=\sum_\nu\operatorname{Tr}(A_\nu^*A_\nu),
 \qquad n=\dim{\cal A}=sD^2 .
 \tag{1}
\]
Vector norms on \({\cal A}\) use this unnormalized physical
Hilbert--Schmidt structure. Map norms labelled \({\rm op}\) are
induced operator norms; tensor coefficient norms are labelled
\({\rm HS}\). Componentwise multiplication is the
linearized tensor
\[
 \mu:{\cal A}\otimes_2{\cal A}\longrightarrow{\cal A},
                    \qquad \mu(A\otimes B)_\nu=A_\nu B_\nu .
 \tag{2}
\]
For the actual all-main-color source of [C, Section 5],
\(s=N\) and \(D=N^b\), where \(b\) is the fixed braid width.
Its leaves are the original signed physical crossings, or specified
nonzero blocked words. Its root takes the original partial pivotal
trace and marked entry, including framing and external factors.
The output and its positive norm remain
\[
 Y_N=(c_1,\ldots,c_N),\qquad
 \|Y_N\|^2=|K_N|^2+R_N,\qquad
 0\le R_N\le(N-1)(N/2)^{2b-2}.
 \tag{3}
\]
We do not replace this root by an identity trace.
The full matrix spaces retain all physical channels and Jordan data.

Fix a known nonzero leaf \(A=\alpha a\), where
\(\alpha=\|A\|>0\) and \(\|a\|=1\). The number \(\alpha\) is
computed from this prescribed leaf; it can be exponentially large.
It is not the closed source and will not be discarded.
Write \(L_a(B)=aB\). Matrix units in each color block give
\[
 C:=\mu\mu^*=D I_{\cal A},\qquad
 \operatorname{Tr}_1(\mu^*\mu)
       =\operatorname{Tr}_2(\mu^*\mu)=D I_{\cal A},\qquad
 X:=L_aL_a^*\preceq C,\qquad
 \operatorname{Tr}C=sD^3,\quad \operatorname{Tr}X=D .
 \tag{4}
\]
For example \(\mu^*E_{ij}= \sum_k E_{ik}\otimes E_{kj}\);
different color blocks do not interact. Also
\(\|L_a\|_{\rm op}=\max_\nu\|a_\nu\|_{\rm op}\le1\).

We first treat a leaf on the first input. For a leaf on the second
input, use \(R_a(B)=Ba\) instead of \(L_a\), apply the reference on
that second input, and exchange the logical input labels below.
The same matrix-unit proof applies. No matrix factors are commuted.

## 2. An input reference which fixes the entire original leaf

Put
\[
 P=|a\rangle\langle a|,\quad Q=I-P,\quad
 G_t=P+tQ,\qquad t\ge1,\qquad
 B_t=\mu(G_t^{-1}\otimes I).
 \tag{5}
\]
Thus \(G_t a=a\), \(G_t A=A\), and
\(\|G_t\|_{\rm op}\le t,\ \|G_t^{-1}\|_{\rm op}=1\), with equality in the first
bound when \(n>1\).
Use \(G_t\) on the selected leaf's output and its inverse on the
first input of its parent. In coefficient tensor notation the latter
is the inverse transpose on the dual leg. The complex bilinear
contraction is exactly unchanged.

This is a full bundled compiler-edge gauge. In general \(P\) mixes
colors and matrix coordinates. It is not a physical-head gauge or
an algebra automorphism. No output reference change is needed.
Every original source row, phase and incident inverse remains.

Since \(\mu(P\otimes I)=L_a(\langle a|\otimes I)\), (4) gives
\[
 Y_t:=B_tB_t^*=X+t^{-2}(C-X),\qquad
 Z_t:=\operatorname{Tr}Y_t
       =D\{1+t^{-2}(sD^2-1)\}.
 \tag{6}
\]
In particular \(Y_t\succ0\); no normal channel is removed.
Define densities on the output and on the two logical inputs by
\[
 \rho_t=\frac{Y_t}{Z_t},\qquad
 \omega_t=\frac{B_t^*B_t}{Z_t},\qquad
 \omega_{1,t}=\operatorname{Tr}_2\omega_t,\quad
 \omega_{2,t}=\operatorname{Tr}_1\omega_t .
 \tag{7}
\]
These are the actual normalized Hilbert--Schmidt marginals of
\(B_t\), in the logical-input convention. Their transposes belong
on the physical dual input half-edges, as in [O].
No independent ordered-density witness is being identified with
an actual tensor marginal.

## 3. Three exact marginal formulas

The canonical comparison states are
\[
 \rho_0=\frac{X}{D},\qquad
 \sigma_a=\frac{L_a^*L_a}{D},\qquad
 \eta_t=\frac{sD^2-1}{t^2+sD^2-1}.
 \tag{8}
\]
Both comparison states have trace one. Write
\(\epsilon=t^{-2}\) and \(Z=Z_t/D=1+(n-1)\epsilon\).
All three actual marginals have the same explicit form:
\[
 \boxed{\qquad
 \omega_{1,t}=\frac{P+\epsilon(I-P)}{Z},\quad
 \omega_{2,t}=\frac{\sigma_a+\epsilon(I-\sigma_a)}{Z},\quad
 \rho_t=\frac{\rho_0+\epsilon(I-\rho_0)}{Z}.
 \qquad}
 \tag{9}
\]
For the first identity, trace \(B_t^*B_t\) over the second
input and use (4), obtaining \(DG_t^{-2}\).
For the second, cyclicity in the traced first factor moves the
two copies of \(G_t^{-1}\) together. The \(P\) term is
\(\operatorname{Tr}_1((P\otimes I)\mu^*\mu)=L_a^*L_a\);
the identity term is \(DI\). This gives the middle formula.
The last formula is (6).
These partial-trace identities do not assume that \(G_t\)
commutes with \(\mu^*\mu\).

For \(n>1\), every density \(\tau\) obeys \(0\preceq\tau\preceq I\),
so the expression in (9) equals
\((1-\eta_t)\tau+\eta_t(I-\tau)/(n-1)\).
The two densities in this convex combination are normalized positive
states. Therefore, with
\(\|T\|_1=\operatorname{Tr}\sqrt{T^*T}\),
\[
 \boxed{\quad
 \|\omega_{1,t}-P\|_1=2\eta_t,\qquad
 \|\omega_{2,t}-\sigma_a\|_1\le2\eta_t,\qquad
 \|\rho_t-\rho_0\|_1\le2\eta_t .
 \quad}
 \tag{10}
\]
The first equality uses the orthogonal supports of \(P\) and \(I-P\).
For \(n=1\) all three states agree and \(\eta_t=0\).

## 4. A full-matrix logarithmic calibration

For arbitrary positive metrics \(H_o,H_1,H_2\) on \({\cal A}\), write
\(X_i=\log H_i\). Scalar spectral Jensen on the coefficient tensor
of \(B_t\) gives
\[
 \begin{split}
 \log\|H_o^{1/2}B_t(H_1^{-1/2}\otimes H_2^{-1/2})\|_{\rm HS}
 \ \ge\ &\frac12\log Z_t+\frac12\operatorname{Tr}(\rho_tX_o)\\
 &-\frac12\operatorname{Tr}(\omega_{1,t}X_1)
  -\frac12\operatorname{Tr}(\omega_{2,t}X_2).
 \end{split}
 \tag{11}
\]
For clarity, after vectorization the three signed logarithms act
on distinct tensor legs. Diagonalize them independently. The squared
norm divided by \(Z_t\) is a positive average of exponentials of
their summed eigenvalues. Jensen gives its mean exponent, which
is exactly the marginal expression in (11).
This is the identity-reference case of the tensor convexity proof
in [C]; it requires no ordering or mutual commutativity of the metrics.

Suppose now that
\(\|X_o\|_{\rm op},\|X_1\|_{\rm op},\|X_2\|_{\rm op}\le R\).
Equation (10), applied before bounding any matrix entries, gives
\[
 \boxed{\begin{split}
 \log\|H_o^{1/2}B_t(H_1^{-1/2}\otimes H_2^{-1/2})\|_{\rm HS}
 \ \ge\ &\frac12\log Z_t+\frac12\operatorname{Tr}(\rho_0X_o)\\
 &-\frac12\operatorname{Tr}(PX_1)
  -\frac12\operatorname{Tr}(\sigma_aX_2)\\
 &-3R\eta_t .
 \end{split}}
 \tag{12}
\]
Each of the three marginal replacements costs at most \(R\eta_t\).
All comparison densities are specified from the actual local leaf.

The unchanged leaf itself has, again by scalar spectral Jensen,
\[
 \log\|H_1^{1/2}A\|
       \ge\log\alpha+\tfrac12\operatorname{Tr}(PX_1).
 \tag{13}
\]
Adding (12) and (13) cancels this incidence's metric term exactly.
The known leaf normalization contributes \(\log\alpha\), while
the parent contributes
\(\tfrac12\log Z_t=\tfrac12\log D-\tfrac12\log(1-\eta_t)\).
No possibly exponential physical leaf norm has been deleted.

## 5. Polynomial accuracy in the actual color dimensions

In the actual source put \(s=N,\ D=N^b\). For any fixed integer \(J\ge1\),
choose
\[
              t=\sqrt{s}\,D\,N^J .
 \tag{14}
\]
Then
\[
 \eta_t\le N^{-2J},\qquad
 2\eta_t=O(N^{-2J}),\qquad
 \log\|G_t\|_{\rm op}=(b+J+\tfrac12)\log N .
 \tag{15}
\]
Thus (12) has loss \(O(RN^{-2J})\), and \(O(N^{1-2J})\) on
any supplied window \(R=O(N)\). The theorem holds for every \(R\);
it does not identify the anchored Newton window in [O] with a window
on this larger matrix algebra. No new window theorem is asserted.
A polynomial reference changes spectral bounds for positive metrics
by only \(O(\log N)\) in their logarithmic radius, on the same compiler.

One may perform this construction simultaneously on any set of
prescribed-leaf edges with at most one selected input per parent.
Each affected parent is exactly its own \(B_t\); no product output
is gauged and the selected leaves remain fixed. For \(M\) selections,
the sum of actual defects on those incidences is at most
\(2M\eta_t\), and the reference costs
\(O(M\log N)\) for fixed \(b,J\).
The original output and root remain exact. Other edge defects
are not controlled by this statement.

## 6. Scope and closest coverage

The states \(\rho_0,\sigma_a\) are the complete left/right
multiplication energy states of the known leaf. They are not
an arbitrarily chosen largest mode or an unknown internal output.
The construction works for any specified nonzero crossing or
blocked word leaf; it makes no claim that every tangle contraction
is nonzero.

It is a one-sided calibration. In fact
\(\|\sigma_a\|_{\rm op}\le1/D\), so every unit vector \(h\) obeys
\[
 \|\sigma_a-|h\rangle\langle h|\|_1\ge2(1-1/D).
 \tag{16}
\]
Test the trace-zero difference against \(|h\rangle\langle h|\).
Thus a second actual pure leaf is not automatically matched.
Compatibility of these mixed states through the remaining tree
and the original closing is still a separate problem.
No Gaussian description of the whole all-color tuple, metric
undoing, geometric volume rate or finite-exception result is inferred.

[C] already proves qualitative leaf elimination with singular limiting
gauges and full tensor capacity. [O] already supplies full-matrix
calibration families and a different anchored Newton leaf shear.
[R] gives the actual positive main-color capacity with its original
source. The addition here is the explicit finite matrix-product
reference, exact defect, polynomial source-dimensional cost and
the local logarithmic inequality (12). No general novelty for
tensor Jensen or rank-one suppression is claimed.

| Label | Complete text | Lines | SHA-256 |
| --- | --- | ---: | --- |
| C | [Actual full-gauge tree capacity](research_scalar_tree_full_gauge_capacity.md) | 466 | 2997b732aa73e063c66e81d6487a1d9927509609d61842c1dbb43d9345df1d6d |
| O | [Ordered-density calibration](research_ordered_density_bilinear_calibration.md) | 320 | 928322373f35eee6692949953a91a592d9486b3507ffa439db5fbbc5729e516a |
| R | [Regularized actual source capacity](research_regularized_actual_source_capacity.md) | 377 | 0cea0d52182eb24b4610538f354dbe5158fa54aa6f9cf7f9fc280c72ab090ff8 |

All three complete matching texts were read. Only written mathematics,
text reads and metadata operations were used. No mathematical program,
numerical experiment, test, build, git operation or earlier-final edit
was performed.
