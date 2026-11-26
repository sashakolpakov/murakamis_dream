# Dimension independent covariance and stable fixed-degree extraction

Private written proof, 23 November 2026.

The existing positive Conway recursion has a stronger covariance
estimate when the full tensor normalization is used. Its covariance
lies between \(\varepsilon I\) and \(2\varepsilon I\) for every
\(0<\varepsilon\le1\), independently of the physical dimension and
tree size. Fixed-degree extraction can consequently use evaluation
points independent of \(N\), with uniformly conditioned full messages.
Chebyshev--Lobatto points also reduce its absolute extrapolation
amplification to less than four, independently of the number of leaves.

The original complex source, closing row and budget remain unchanged.
These are bounds for the auxiliary evaluation and extraction, not
relative-precision bounds for an exponentially small selected scalar.

## 1. The full normalized tensors

Use the complete literal expression tree in [C] and positive recursion
in [P]. At level \(N\ge2\), every boundary is the full \(N\)-dimensional
Newton space \(H_N\), with its fixed coefficient Hermitian metric.
Repeated-root value and derivative directions are both retained.
Write
\[
 \sigma=\frac1{16},\qquad
 b_v=16\max(1,\|T_v\|_{\mathrm{HS}}),\qquad
 B_N=\prod_vb_v\ge1 .
 \tag{1}
\]
The budgets include the actual root tensor. Let the normalized
leaf vectors be \(a_v\), unary maps \(A_v\), product maps \(M_v\),
and original closing row \(L\). The true normalized packets obey
\[
 a_v=A_va_c\ \text{or}\ M_v(a_l\otimes a_r),\qquad
 \|a_v\|\le\sigma,\quad\|A_v\|\le\sigma,\quad\|L\|\le\sigma,
 \qquad B_NLa_{\mathrm{top}}=K_N .
 \tag{2}
\]
Here \(K_N\) is the original reduced marked invariant, including
its recorded phases, powers of \(N\), and framing normalization.

The point needed below is stronger than a bound only on decomposable
bilinear inputs. Normalization (1) gives
\[
 \|M_v:H_N\otimes H_N\longrightarrow H_N\|_{\mathrm{op}}
       \le\|M_v\|_{\mathrm{HS}}\le\sigma .
 \tag{3}
\]
Indeed the Hilbert--Schmidt norm in [C] sums every coefficient of
the full tensor. Cauchy--Schwarz bounds its linearization on the
whole Hilbert tensor product by that same norm.

For real \(\varepsilon>0\), keep exactly the deterministic recursion
\[
 \begin{array}{ll}
 S_v=a_va_v^\dagger+\varepsilon I,&v\text{ a leaf},\\
 S_v=A_vS_cA_v^\dagger+\varepsilon I,&v\text{ unary},\\
 S_v=M_v(S_l\otimes S_r)M_v^\dagger+\varepsilon I,
                                           &v\text{ binary},
 \end{array}
 \qquad F_N(\varepsilon)=B_N^2LS_{\mathrm{top}}L^\dagger .
 \tag{4}
\]
There is no fresh error at the closing root. All adjoints use
the full original normalized maps, not separate absolute coefficients.
Only the leaf vectors are needed to evaluate (4); the true internal
packets enter the covariance proof, not its input data.

## 2. A covariance bound in operator order

Set \(V_v=S_v-a_va_v^\dagger\). Expanding (4), or using its
independent centered errors, gives exactly
\[
 \begin{array}{ll}
 V_v=\varepsilon I,&v\text{ a leaf},\\
 V_v=A_vV_cA_v^\dagger+\varepsilon I,&v\text{ unary},\\
 V_v=M_v(a_la_l^\dagger\otimes V_r+
             V_l\otimes a_ra_r^\dagger+V_l\otimes V_r)M_v^\dagger
             +\varepsilon I,&v\text{ binary}.
 \end{array}
 \tag{5}
\]
Every term is positive semidefinite. Thus the covariance and its
lower floor are genuine matrix statements, with all cross-channel
coherence retained.

For every \(0<\varepsilon\le1\), induction proves
\[
 \boxed{\quad
 \varepsilon I\preceq V_v\preceq2\varepsilon I,\qquad
 \varepsilon I\preceq S_v
                    \preceq(\sigma^2+2\varepsilon)I .
 \quad}
 \tag{6}
\]
The leaf case is exact. The unary upper bound is
\((1+2\sigma^2)\varepsilon I\prec2\varepsilon I\).
At a binary vertex use (3) and the induction hypothesis in (5):
\[
 V_v\preceq
       \{\varepsilon+4\sigma^4\varepsilon
                              +4\sigma^2\varepsilon^2\}I
 \preceq\varepsilon(1+4\sigma^4+4\sigma^2)I
 \prec2\varepsilon I .
 \tag{7}
\]
This closes without multiplying a constant for the number of vertices.
The second assertion of (6) follows from \(\|a_v\|\le\sigma\).
In particular
\[
       \operatorname{cond}_2S_v(\varepsilon)
                       \le2+\sigma^2/\varepsilon .
 \tag{8}
\]
At \(\varepsilon=1\), this is \(2+\sigma^2\), independent of
both \(N\) and the tree. The trace need not be dimension independent:
the fresh floor has trace \(N\varepsilon\). Bounding the operator
covariance rather than its trace removes that unnecessary factor
from the original rank-one closing observation.

## 3. The calibrated additive error

At the unchanged closing,
\[
 \varepsilon B_N^2\|L\|^2
 \le F_N(\varepsilon)-|K_N|^2
          =B_N^2LV_{\mathrm{top}}L^\dagger
 \le2\varepsilon B_N^2\|L\|^2 .
 \tag{9}
\]
For \(0<\theta\le1\), the improved choice
\(\varepsilon=\theta/B_N^2\le1\) therefore gives
\[
                 0\le F_N(\theta/B_N^2)-|K_N|^2
                                      \le\theta/128 .
 \tag{10}
\]
The earlier trace proof used \(\theta/(NB_N^2)\) for this same
additive bound. The new choice removes \(N\), but can still be
exponentially small because the known budget \(B_N\) can be large.
The fixed-degree extraction below does not require that small choice.

If errors are added only at leaves, omit the internal
\(\varepsilon I\) in (5). The same induction gives
\(0\preceq V_v\preceq\varepsilon I\), because its binary upper
bound is
\(\sigma^2(2\sigma^2\varepsilon+\varepsilon^2)I
 \preceq\varepsilon I\).
The resulting closing error at \(\theta/B_N^2\) is at most
\(\theta/256\). Internal matrices in this leaf-only version
may be singular; the conditioning guarantee (8) uses fresh errors
at every proper vertex.

## 4. Fixed evaluation points with bounded extrapolation cost

Let \(l\ge1\) be the number of leaf occurrences.
The existing positive-coefficient induction in [P] gives
\[
 F_N(\varepsilon)=|K_N|^2+
                 \sum_{j=1}^{l}c_{N,j}\varepsilon^j,\qquad
 c_{N,j}\ge0 .
 \tag{11}
\]
This degree counts auxiliary errors, not physical colors.
The interpolation identities below are standard polynomial
identities; the new input is (6), which permits constant evaluation
points with conditioning independent of \(N\).

For example, equally spaced points \(j/(l+1)\), \(1\le j\le l+1\),
already give the existing forward-difference formula with weights
\((-1)^{j-1}\binom{l+1}{j}\).
Equation (8) improves their message condition bound to
\(2+\sigma^2(l+1)\). Their absolute weight sum is \(2^{l+1}-1\).

A better choice for absolute extraction is
\[
 \begin{gathered}
 a=(l+1)^{-2},\qquad x_j=\cos(j\pi/l),\\
 \varepsilon_j=(1+a)/2+(1-a)x_j/2,\quad 0\le j\le l,\qquad
 x_*=-\frac{1+a}{1-a},\\
 w_j=\prod_{k\ne j}\frac{x_*-x_k}{x_j-x_k}.
 \end{gathered}
 \tag{12}
\]
The nodes are distinct and lie in \([a,1]\); zero corresponds to
\(x_*\). Lagrange interpolation of the polynomial (11) proves
\[
 \boxed{\quad |K_N|^2=\sum_{j=0}^{l}w_jF_N(\varepsilon_j),\qquad
  \operatorname{cond}_2 S_v(\varepsilon_j)
                              \le2+\sigma^2(l+1)^2 .\quad}
 \tag{13}
\]
There is no \(N\)-dependent or budget-dependent evaluation point.
All matrices still have their full physical dimension \(N\).

For completeness, the absolute amplification has an explicit bound.
Since \(x_j\) decrease and \(x_*<-1\), the numerator in \(w_j\)
has \(l\) negative factors and its denominator has \(j\). Thus
\(\operatorname{sign}w_j=(-1)^{l-j}\).
Using \(T_l(x_j)=(-1)^j\) in the same interpolation identity gives
\[
 \begin{split}
 \sum_{j=0}^{l}|w_j|
 &=(-1)^lT_l(x_*)=T_l((1+a)/(1-a))\\
 &=\cosh\!\left(2l\,\operatorname{atanh}\frac1{l+1}\right)
 \le\cosh2<4 .
 \end{split}
 \tag{14}
\]
Here \(\operatorname{atanh}t\le t/(1-t)\) for \(0<t<1\), as
follows by integrating \(1/(1-s^2)\le1/(1-s)^2\).
This also checks \(l=1\), where the two nodes are \(1\) and \(1/4\).

The weight sum in (14) is optimal for real nodes constrained to
\([a,1]\). Any linear reconstruction exact through degree \(l\)
can be tested on
\(T_l((2\varepsilon-1-a)/(1-a))\), whose modulus is at most one
on that interval. Its value at zero forces the weight sum to be
at least \(T_l((1+a)/(1-a))\), attained in (14).
No novelty is claimed for this classical interpolation fact.

## 5. What the improved conditioning does and does not control

If each evaluated scalar \(F_N(\varepsilon_j)\) has absolute error
at most \(\delta\), (13)--(14) give reconstruction error below
\(4\delta\). If instead the normalized observations
\(LS_{\mathrm{top}}L^\dagger\) have absolute errors at most
\(\delta\), the guaranteed error is below \(4B_N^2\delta\).
The original budget factor must remain in this statement.

The signed scalar sum may vanish or be exponentially smaller
than its positive summands. Uniformly conditioned messages and
bounded absolute extrapolation therefore do not imply fixed
relative precision, a nonzero constant Fourier mode, or a geometric
lower bound. They also do not make the full correlated phase Gram
uniformly positive in every auxiliary mode.

The quantitative improvement is (6), its calibration (10), and the
constant-point conditioning in (13), combined with the absolute
amplification (14). Fourier filtering, fixed-degree extraction and
elimination of the auxiliary minimization were already proved.
Every original cap, complex phase and Hermite direction is retained.
The full source value and its volume rate still require their own
estimate after arbitrary fixed short partial fillings.

## Complete sources and coverage

The two complete proof directs are [P],
[Positive Conway recursion](research_orthogonal_error_positive_conway_recursion.md)
(407 lines), SHA256
5506f489642f2ec118c4fef25cccc0485fecdc32ffccf09c700ac923c9da98dd;
and [C],
[Normalized complete compiler](research_convex_normalized_conway_source.md)
(329 lines), SHA256
6b89b4c6a67ef7a32cc41a5966c650f32de65d284ae7b70d94a71bddba21df3c.
Both were freshly read whole; the stronger use of their full
Hilbert--Schmidt normalization is written explicitly above.

Complete comparison sections in notes/research_finite_exceptions_progress.md
were read at ledger pin
cec7924dbd6e6d0eeb365ea7bd8d73d364ad1254cb77b2ae4cbebbeffa7c9d39:
“Keeping the error degrees separately,” “A finite Fourier projection
removes the auxiliary minimization,” and “Fixed degree removes the
small error parameter.” These are complete individual sections,
not a claim to have read the entire ledger as one proof source.
The older finite-difference nodes there were \(j/[(l+1)N]\);
their covariance trace estimate supplied conditioning of order \(N\).
Only written mathematics and source-text/hash operations were used.
