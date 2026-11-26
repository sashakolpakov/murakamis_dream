# The main-color Fourier energy retains a coherent cap projection

20 November 2026. Research note; public manuscripts remain frozen.

The main-color Plancherel norm has an exact realization by positive
projectors on the original physical braid. Its cap projector is still
coherent: the input and output indices of each traced head are paired
in a maximally entangled vector. This note gives the actual identity,
characterizes its allowed lower-bound test vectors, and computes what
happens when a local output window is inserted. It proves no geometric
lower bound or additional volume-conjecture case.

## 1. The original main-color orbit

Fix a zero-framed knot presented as the closure of a braid on \(b\)
strands. Its closure has one component. At level \(N\ge2\), put
\[
 q=e^{\pi i/N},\quad Q=q^2,\quad
 \alpha_j=j-1,\quad x_j=q^{j-1},\quad M_j=-q^j,
 \qquad 1\le j\le N.
\]
At every \(j\), use the original \(N\)-dimensional unrolled color
\(V_{\alpha_j}\), including its reducible specializations. On its
fixed basis \(e_a\), \(0\le a<N\),
\[
 K_je_a=x_jQ^{-a}e_a.
\]
Let \(W_j\) be the original checked braid operator on
\(V_{\alpha_j}^{\otimes b}\), including all common Cartan factors
and its scalar zero-framing correction. Cut the first strand. The
original reduced source is the \((0,0)\) entry of its partial pivotal
trace:
\[
 c_j=\left[\operatorname{Tr}_{\rm env}
        \{W_j(I\otimes g_j)\}\right]_{00},\qquad
 g_j=(K_j^{1-N})^{\otimes(b-1)}.                         \tag{1}
\]
This is the reduced tangle scalar with unknot value one, as specified
in [the ADO source note](kashaev_ado_pointing.md), Section 1. It does
not include the modified-dimension factor, whose ordinary-color
specializations can have poles. The selected cut entry retains the
reduced marked normalization; the pivotal trace closes only the other
strands. In particular
\[
 c_N=K_N,\qquad c_j=C_j(q)\quad(1\le j<N).                \tag{2}
\]

Here (2) is an actual source comparison, not a renaming of labels.
For \(j<N\), the span of \(e_j,\ldots,e_{N-1}\) is invariant under
\(E,F,K,H\). Both finite signed crossings and the pivot preserve it
on each strand. Its quotient is the ordinary \(j\)-dimensional
highest-weight color. In a partial trace of a one-component braid,
a path contributing to the quotient cut cannot enter that invariant
subspace and later leave it. Every contributing strand path therefore
stays in the quotient. The pivotal and framing convention difference
is \((-1)^{(j-1)(b-1-w)}=1\), since the writhe \(w\) of a braid
with cyclic closure permutation satisfies \(w\equiv b-1\pmod2\).
This proves the ordinary-color assertion in (2); the complete-color
assertion is the retained original Kashaev normalization.

The [ordinary-color Plancherel proof](ordinary_color_plancherel_bound_audit.md)
also proves
\[
 E_N:=\sum_{j=1}^N|c_j|^2=|K_N|^2+R_N,\qquad
 0\le R_N\le (N-1)(N/2)^{2b-2}.                         \tag{3}
\]
Briefly, in its positive path realization the ordinary color projector
is orthogonal and has trace
\([j]=\sin(\pi j/N)/\sin(\pi/N)\); the cabled braid is unitary.
The unreduced colored trace is therefore bounded by \([j]^b\).
Dividing by its nonzero dimension \([j]\) gives
\(|C_j|\le[j]^{b-1}\le(N/2)^{b-1}\). The argument applies to the
whole range \(j<N\). At \(j=N\), the dimension is zero and that
positive quotient erases the complete sector; we do not use it there.

## 2. A common physical cap projector

Write the traced environment as \(\mathbb C^D\), where
\(D=N^{b-1}\), with multi-indices \(I=(i_2,\ldots,i_b)\).
Its pivot has the exact form
\[
 (g_j)_I=\gamma_j(g_*)_I,\qquad
 \gamma_j=x_j^{(1-N)(b-1)},\qquad
 (g_*)_I=Q^{-\sum_{s=2}^b i_s}.                          \tag{4}
\]
Indeed \(Q^{(N-1)a}=Q^{-a}\). Both \(\gamma_j\) and every
entry of \(g_*\) have modulus one. Move only the recorded scalar
phase into \(\widetilde W_j=\gamma_jW_j\); no source factor is
dropped.

For an operator \(A\), fix the vectorization convention
\[
 \operatorname{vec}A
 =\sum_{a,a',I,J}A_{(a,I),(a',J)}
       e_a\otimes e_{a'}\otimes e_I\otimes e_J.          \tag{5}
\]
The two first factors are the open output and input; the final
factors are the environment output and input. All carry their usual
positive coordinate inner products, so
\(\|\operatorname{vec}A\|=\|A\|_{\rm HS}\), the Hilbert--Schmidt
norm. Define unit vectors
\[
 h=\frac1{\sqrt D}\sum_I\overline{(g_*)_I}\,e_I\otimes e_I,
 \qquad r=e_0\otimes e_0\otimes h.                       \tag{6}
\]
The vector \(h\) is a product of the specified pivotal cap-pair
vectors over the \(b-1\) traced heads. Its Schmidt rank across the
whole environment output/input split is \(D\).

Add one main-color register \(\mathbb C^N\), with basis \(|j\rangle\),
and set
\[
 \mathsf w=\sum_{j=1}^N|j\rangle\otimes
                          \operatorname{vec}\widetilde W_j,
 \qquad \Pi=I_{\rm color}\otimes|r\rangle\langle r|.      \tag{7}
\]
This is a direct sum of different actual main-color braid operators,
not a braid with independently chosen colors on its different strands.

**Proposition 1.** The rank-\(N\) positive orthogonal projector in
(7) satisfies
\[
 \sqrt D\,\Pi\mathsf w
      =\sum_{j=1}^Nc_j|j\rangle\otimes r,
 \qquad E_N=D\|\Pi\mathsf w\|^2.                        \tag{8}
\]

**Proof.** Equations (1), (4)--(6) give
\[
 \langle r,\operatorname{vec}\widetilde W_j\rangle
 =D^{-1/2}\sum_I(g_*)_I(\widetilde W_j)_{(0,I),(0,I)}
 =D^{-1/2}c_j.
\]
Project onto \(r\) in each orthogonal color block and sum their
squared norms. This proves both identities. \(\square\)

The unitary Fourier matrix \(\mathcal F_{kj}=N^{-1/2}Q^{-kj}\),
\(0\le k<N\),
acts only on the main-color register and commutes with \(\Pi\).
Applying it to (8) gives exactly the main-color Plancherel norm.
It does not remove the cap projector. Opening it instead gives the
upper bound \(E_N\le D\sum_j\|W_j\|_{\rm HS}^2\).
The single-color vectorized closure identity underlying (8) is already
proved in [the weighted plat-energy note](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/actual_weighted_fourier_plat_energy.md),
Section 4; (4) supplies the common projector for the whole actual orbit.

## 3. Which lower-bound tests preserve this source?

Every vector in \(\operatorname{ran}\Pi\) is uniquely
\(\psi=\sum_j a_j|j\rangle\otimes r\). Cauchy gives
\[
 E_N\ge\frac{|\sum_j\overline a_jc_j|^2}{\sum_j|a_j|^2}
 \quad(a\ne0).                                         \tag{9}
\]
For an arbitrary trial vector \(v\), the valid test is \(\Pi v\):
\[
 E_N\ge D\frac{|\langle\Pi v,\mathsf w\rangle|^2}
                         {\|\Pi v\|^2}
 \quad(\Pi v\ne0).                                     \tag{10}
\]
Replacing \(\Pi v\) by \(v\) in the numerator has no justification.
Moreover, when \(\sum_j|a_j|^2=1\), (3) gives the exact separation
\[
 \left|\sum_j\overline a_jc_j-\overline a_NK_N\right|
 \le\sqrt{1-|a_N|^2}\,\sqrt{R_N}.                       \tag{11}
\]
Thus a test avoiding the complete main color has only polynomial
size. A successful exponential lower bound from (9) is possible, but
it must retain and estimate the original complete-color contribution.

## 4. Exact effect of localizing an environment output

Let \(A\) be any operator on the environment output factor alone;
extend it by identities on the other factors and call the extension
\(\widehat A\). Maximal entanglement in (6) gives
\[
 \boxed{\qquad
 \Pi\widehat A\Pi=\frac{\operatorname{Tr}A}{D}\Pi.
 \qquad}                                                \tag{12}
\]
To verify this, expand
\(\langle h,(A\otimes I)h\rangle\). The input inner product sets
the two indices equal, the pivot phases cancel, and the result is
\(D^{-1}\sum_IA_{II}\). The remaining factors in (7) are unchanged.
In particular a rank-\(s\) orthogonal output-window projector gives
exactly \((s/D)\Pi\). Sandwiching such a window between the actual
source projectors therefore rescales the same unknown source norm;
it does not extract an independently localized contribution.

There is a second useful support restriction. If \(0\le Q_0\le\Pi\),
then \(\operatorname{ran}Q_0\subseteq\operatorname{ran}\Pi\).
For \(z\in\ker\Pi\), positivity gives
\(0\le\langle z,Q_0z\rangle\le0\), hence
\(Q_0^{1/2}z=0\); taking orthogonal complements proves the claim.
When \(D>1\), this range contains no nonzero vector whose environment
output/input part is a single product vector: every nonzero color
block has the full-Schmidt-rank environment vector \(h\).
Consequently an independently product-localized positive projector
cannot be placed below \(\Pi\) in operator order.

These statements hold for all input tensors. They do not prove that a
source-compatible entangled geometric test is impossible, or that
such a test has small overlap with the actual \(\mathsf w\). They
specify what must be constructed before positivity can give the desired
lower bound without changing the original source.

Finally, this is the orbit of the knot's main meridian: it changes
every main-strand crossing representation and its pivot. Auxiliary
crossing-circle colors instead change selected inserted circle coupons
while the main representation stays fixed. Their Fourier or Hermite
norms cannot be substituted for (8). Likewise a complete-main-color
Conway Gram does not become an all-main-meridian compiler from (8).
All ordinary and complete physical blocks in (7) must remain as stated.

## Complete direct-source pins

All three direct texts were read completely. No mathematical program,
test, build, or public-document edit was used.

* [Original main-color source](kashaev_ado_pointing.md):
  `005ad157ebbf068b71eb80e2ceddc1aa9fccc460a54266756306e5cb54cf4c78`.
* [Ordinary-color comparison and Plancherel remainder](ordinary_color_plancherel_bound_audit.md):
  `1c8b95921af8da7063d92af35cfcc15756b276fb9c85639fb2ffc3def1f922f0`.
* [Original vectorized pivotal closure](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/actual_weighted_fourier_plat_energy.md):
  `69757cb8ab3b857b690d9da8d3d7a46e4a42df4f0ab47a6bb85816aa9efc38b2`.
