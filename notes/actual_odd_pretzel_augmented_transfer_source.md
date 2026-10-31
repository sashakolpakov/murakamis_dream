# The original odd pretzel and its complete mixed-circle transfer source

29 October 2026. The literal original turns and disjoint twist boxes
give an exact cyclic transfer formula for EVERY odd number of odd
pretzel boxes. It keeps one unwrapped integer charge, the entire marked
row and all original crossing-circle normal channels. It is not a
replacement by a Jones polynomial, a TV state, or an AK integral.

The formula is a concrete source for the arbitrary-region augmented
pretzel survival question. Its complete-color base does not become
entrywise positive by a diagonal phase gauge, even after retaining the
half twists. A positive reflected network or an original relative-cycle
calculation still needs proof.

## 1. Diagram, signs and literal original source

Use \(N\geq2,d=N-1,q=e^{\pi i/N},Q=q^2,x=q^d\). Label \(2s\)
vertical heads from left to right. Box \(i\) acts on heads
\((2i-1,2i)\). At BOTH ends the planar matching is

\[
 (1,2s),(2,3),(4,5),\ldots,(2s-2,2s-1).                \tag{1}
\]

The outer bottom turn is the original \(p_{a_1,b_s}\); the other
bottom turns are \(p_{b_i,a_{i+1}}\). At the top the inner turns are
\(\ell_{d_i,c_{i+1}}\), and the outer turn is the sole original
marked row \(m_{c_1,d_s}\). All port orders here are part of the
definition, including that of the nested outer turn. The original
formulas are

\[
 p_{uv}=N x^{-v}\mathbf1_{u+v=d},\quad
 \ell_{uv}=x^u/N\,\mathbf1_{u+v=d},\quad
 m_{uv}=x^v/N^2.                                     \tag{2}
\]

In particular \(m\) has NO degree indicator before the contraction.
For degree-preserving physical boxes \(B_i\), define the RAW marked
source \(\mathcal A_{s,N}(B_1,\ldots,B_s)\) by this tensor diagram.
Its original peripheral/framing line \(\chi_N\) remains outside it.

For odd box integers \(n_i\), the usual odd pretzel diagram is (1)
with \(B_i=R^{-n_i}\), with this explicit crossing convention.
Choosing \(R^{n_i}\) instead gives the global mirror. This fixes the
sign by the one-crossing boxes: rotating their original cup/cap
diagrams and applying the two snake identities concatenates them
into the literal central \(s\)-crossing four-plat, with no curl.
Thus the all-\(n_i=1\) raw source agrees with the original four-plat
\(\sigma_2^s\). This is an equality of the specified tangle sources,
not an identification inferred from a colored polynomial.

There is one component when \(s\) is odd. Indeed each odd box has
the swap permutation of its two endpoints. Following the two planar
matchings advances the box index by two modulo \(s\). For odd \(s\)
this visits every box; for even \(s\) there are two components. This
proof is independent of the odd twist magnitudes and signs. We use
only odd \(s\geq3\), so the sole marked source is an admissible
original one-component cut. Reduction, hyperbolicity and long filling
are further topological hypotheses, not consequences of this source
formula.

## 2. Exact unwrapped-charge transfer theorem

For \(-d\leq h\leq d\) put

\[
 I_h=\{\max(0,h),\ldots,\min(d,d+h)\},\quad
 D_h=\operatorname{diag}_{a\in I_h}x^{2a},
\]
\[
 M_i^{(h)}[a,a']
 =x^{-2a+h}
   (B_i)_{(a-h,\,d-a'+h);\,(a,\,d-a')},
                  \qquad a,a'\in I_h.                \tag{3}
\]

These are finite physical matrix entries; no cyclic index is allowed.
Then

\[
 \boxed{\displaystyle
 \mathcal A_{s,N}(B_1,\ldots,B_s)
 =\frac{x^{(s-1)d}}N
   \sum_{h=-d}^d\operatorname{Tr}
         \bigl(D_hM_1^{(h)}\cdots M_s^{(h)}\bigr).}     \tag{4}
\]

The statement holds for arbitrary degree-preserving boxes on their
specified physical pairs, not merely for one eigenchannel or for
root-sampled continuations. In particular it includes every actual
signed power of \(R\), every literal mixed-color circle, and their
products.

Proof. Write the inputs of box \(i\) as \((a_i,b_i)\), its outputs
as \((c_i,d_i)\). The bottom source forces
\(b_i=d-a_{i+1}\), cyclically, where the exceptional outer source
has the ordered coefficient \(p_{a_1,b_s}\). The inner caps force
\(d_i=d-c_{i+1}\), \(i<s\). The total input degree is \(sd\);
each \(B_i\) preserves its actual integer degree. Therefore the
remaining outer pair has \(c_1+d_s=d\), including when evaluated
against the FULL marked row (2). Only now may that forced equality
be used to write \(d_s=d-c_1\).

Each box conservation equation is now

\[
 a_i-a_{i+1}=c_i-c_{i+1}.
\]

Thus \(h=a_i-c_i\) is a common UNWRAPPED integer, and each
\(a_i\) lies exactly in \(I_h\). No mod-\(N\) aliases have been
introduced or discarded. The total turn coefficient before using
this conservation law is

\[
 \frac1N x^{(s-1)d+2a_1-\sum_i a_i-\sum_i c_i}
 =\frac{x^{(s-1)d}}N x^{2a_1}
                          \prod_i x^{-2a_i+h}.       \tag{5}
\]

The \(N^{-1}\) in (5) is exactly \(N^s/N^{s+1}\) from the cups,
ordinary caps and single marked cap. Summing the resulting cyclic
product gives (4). This proves the literal source normalization;
there is no new trace average of size \(N^{s}\) or \(2N\).

## 3. Simultaneous original full-twist filling

For \(n_i=2p_i+1\), keep the half twist \(R^{-1}\) and use the
already proved ALL-INPUT circle kernel on \(R^{-2p_i}\):

\[
 R^{-n_i}=\kappa^{-2p_i}\sum_{j=1}^N
          \beta_{N,-2p_i,j}\,R^{-1}L_j,
 \qquad\sum_j|\beta_{N,-2p_i,j}|\leq2N(1+|p_i|).       \tag{6}
\]

Every \(L_j\) is the ordinary \(j\)-dimensional mixed auxiliary
circle with its original pivot, not an extra complete component
identified by a quotient lemma. Define

\[
 \mathcal A_{s,N}(j_1,\ldots,j_s)
       =\mathcal A_{s,N}(R^{-1}L_{j_1},\ldots,R^{-1}L_{j_s}).
\]

Equations (4) and (6) give the exact original pretzel scalar

\[
 K_N=\chi_N\prod_i\kappa^{-2p_i}
       \sum_{j_1,\ldots,j_s}\left(\prod_i\beta_{N,-2p_i,j_i}\right)
                                 \mathcal A_{s,N}(j_1,\ldots,j_s). \tag{7}
\]

The \(\chi_N\) here is the original filled pretzel's line. It is
not replaced by a guessed normalization or framing of the augmented
diagram. For each fixed \(s\) the coefficient mass is at most
\(\prod_i2N(1+|p_i|)\). The formula treats arbitrary odd \(s\),
so it is not restricted to bounded braid width or one variable slope.
Its large-\(N\) constants may depend on the fixed diagram \(s\).

## 4. Exact complete-base channel formula and a positivity test

At complete circle colors every box is the SAME
\(B_*=R^{-1}L_N\). Hence (4) becomes a sum of weighted powers
\(\operatorname{Tr}(D_h(M_*^{(h)})^s)\). The
[positive reflected-circle theorem](actual_complete_circle_reflection_positive.md)
gives a complete all-degree expansion of \(B_*P\). In a low total
degree block \(T\), its coefficients are

\[
 B_*P=\sum_jh_{T,j}(\kappa\nu_j)^{-1}v_{T,j}v_{T,j}^*,
\quad h_{T,j}>0,                                     \tag{8}
\]

including the odd simple node and every even-level normal channel.
Thus the transfer (3) retains the HALF-TWIST phase
\((\kappa\nu_j)^{-1}\); it is not the plain PSD matrix \(L_NP\).
Its two physical ports can belong to different total degrees
\(T=d+a-a'\). A partial transpose or reshuffling of the PSD matrix
is not assumed positive.

For an exact illustration, at \(N=3,h=0\) the literal transfer is

\[
 M_*^{(0)}=
 \begin{pmatrix}
  \tfrac92+\tfrac{3\sqrt3}2i&-\tfrac32-\tfrac{3\sqrt3}2i&0\\
  3&\tfrac{21}2+\tfrac{9\sqrt3}2i&-\tfrac32+\tfrac{3\sqrt3}2i\\
  0&-\tfrac32-\tfrac{3\sqrt3}2i&9
 \end{pmatrix}.                                      \tag{9}
\]

Its diagonal entries do not have a common phase. No scalar and
diagonal similarity can therefore make this matrix entrywise
nonnegative or Hermitian positive. This is a failure of that specific
Perron/diagonal-gauge shortcut, not an obstruction to a coherent
reflected-source formula or geometric survival.

The complete raw base scalar at \(N=3,s=3\), including ALL charges
in (4), is exactly

\[
 \mathcal A_{3,3}(3,3,3)=-189+81\sqrt3\,i.             \tag{10}
\]

Its nonzero value is an exact source check. It is not an all-level
nonvanishing theorem, an asymptotic volume calculation, or a proof
that its geometric coefficient is nonzero. Establishing an original
positive reflected base or a selected relative cycle in an open
cusp-color corridor remains the geometric step.

[Audit](../experiments/audit_actual_odd_pretzel_augmented_transfer_source.py)
compares (4) with direct physical tensor contraction, all single
crossing pretzels with the original central four-plat, mixed-circle
ports and the simultaneous filling, and reconstructs (9)--(10)
over the exact quadratic field.
