# Fourier weights from a zero-free scalar-symbol homotopy

Private exact-source deduction, 9 November 2026. A zero-free homotopy
of the full shifted scalar symbol suffices for a uniformly bounded
inverse of the original low-frequency compression. Positivity of the
real part of the shifted symbol is not required. The proof includes
both finite-section boundaries and the reflection at zero frequency.

The original Hermite pairing, parity forcing and eleven boundary
output modes remain unchanged. No weight meeting the actual attachment
budget is supplied. No mathematical numerical evaluation, saved-value
arithmetic, or frozen-source edit is used. The original task attachment
was reread; this is an operator criterion within the short-source
problem, not a finite-exception theorem.

## 1. The original operator and the new hypothesis

Use the operators of the
[full-shift theorem](research_mixed_next_outer_full_shift_low_frequency_inverse.md):
\[
 (\mathcal P_N)_{n,k}=p_{n-k}(k/N),\qquad
 p(u,t)=\sum_{\ell=-11}^{11}p_\ell(t)e^{i\ell u}
       =(2-2\cos u)^3d(u,-e^{3iu+2\pi it}).                 \tag{1}
\]
The function \(d\) is exactly that source's equations (4)--(5).
The original half-step and outer crossing phase are included.
For real \(u,t\),
\[
 p(u,t)\in\mathbb R,\quad p_{-\ell}(t)=\overline{p_\ell(t)},
 \qquad p(-u,-t)=p(u,t).                                 \tag{2}
\]
For every fixed \(0<\alpha<1/2\),
\[
 \min_{u\in\mathbb R,\ |t|\le\alpha}p(u,t)>0.              \tag{3}
\]
The endpoint values are
\(p(0,t)=4096\cos^6(\pi t)\) and \(p(\pi,t)=256\).

Let \(\lambda:[0,\alpha]\to(0,\infty)\) be fixed and Lipschitz.
Suppose it is constant, equal to \(\eta>0\), on a fixed interval
\([0,\beta]\), \(0<\beta<\alpha\). Define
\[
 W(t)=\int_0^t\lambda(s)\,ds,\quad K_N=\lfloor\alpha N\rfloor,
 \qquad (E_Nv)_k=e^{NW(|k|/N)}v_k.                       \tag{4}
\]
Extend \(\lambda\) constantly past \(\alpha\) for the finitely
many further output modes. The new hypothesis is
\[
 \boxed{\quad
 p(u-is,t)\ne0\qquad
 (u\in\mathbb R,\ 0\le t\le\alpha,\ 0\le s\le\lambda(t)).
 \quad}                                                 \tag{5}
\]
The parameter set is compact modulo the period, so the modulus has
a positive uniform lower bound. This is a condition on the original
Laurent symbol. No assertion that a proposed large weight satisfies
it is implicit here; small constant weights do, by (3).

For each \(t\), the curve \(p(u-i\lambda(t),t)\) has winding zero
around zero: (5) gives a nonvanishing homotopy to the positive curve
\(p(u,t)\). Equation (2) gives the same assertion for the negative
frequency symbol \(p(u+i\lambda(|t|),t)\). Winding zero is thus
proved by the stipulated homotopy, not assumed from nonvanishing
at its final height alone.

## 2. Frozen full-line, half-line, and reflection inverses

We use an elementary scalar factorization. Let \(a(z)\) be a
Laurent polynomial, nonzero on \(|z|=1\), with winding zero.
Its full-line convolution is invertible by Fourier orthogonality,
with inverse norm at most \(\min_{|z|=1}|a(z)|^{-1}\).
Its Toeplitz compression to \(\ell^2(\mathbb N_0)\) is also
invertible, as follows.

Let \(r\) be its actual pole order at zero, taking \(r=0\) if
there is no pole. Winding zero implies that \(z^ra(z)\) has
exactly \(r\) roots inside the unit disk, counting multiplicities.
It has no root at zero in this convention: for \(r=0\) such a
root would already contradict winding zero. Factoring gives
\[
 a(z)=c\,a_-(z)a_+(z),\quad
 a_-(z)=\prod_{|\zeta_j|<1}(1-\zeta_j/z),\quad
 a_+(z)=\prod_{|\zeta_j|>1}(1-z/\zeta_j),                 \tag{6}
\]
where \(c\ne0\). Empty products are allowed. The factors and
their reciprocals have absolutely summable Laurent series of,
respectively, nonpositive and nonnegative degree. For the unilateral
forward shift \(S\), \((S^*)^rS^s=T(z^{s-r})\). Therefore
\[
 T(a)=c\,T(a_-)T(a_+),\qquad
 T(a)^{-1}=c^{-1}T(a_+^{-1})T(a_-^{-1}).                 \tag{7}
\]
All products converge in operator norm. The reverse half-line uses
\(a(z^{-1})\), which also has winding zero, and is invertible.
Neither claim uses positivity of a shifted symbol.

These inverses are uniformly bounded over the compact family in
(5). There is no need to label roots continuously. Toeplitz operators
depend continuously in norm on their finitely many coefficients;
the Neumann argument around each invertible member and a finite
cover give the uniform bound. This also permits drops of the extreme
Laurent degrees. Let \(c_*>0\) be a common lower singular-value
bound for these full-line and both half-line models.

The zero-frequency reflection needs another model. Let \(P^0\)
be convolution with \(p_\ell(0)\), and set
\[
 (B^0)_{n,k}=e^{\eta(|n|-|k|)}p_{n-k}(0).                \tag{8}
\]
This is a bounded band matrix on \(\ell^2(\mathbb Z)\).
Reality in (2) reflects zero-freeness from
\(-\eta\le\Im u\le0\) to the upper strip. Compactness supplies
a fixed further margin: \(1/p(u,0)\) is holomorphic near a
closed strip \(|\Im u|\le\eta+\epsilon\), \(\epsilon>0\).
Its Fourier coefficients \(h_j\) satisfy
\[
                         |h_j|\le C e^{-(\eta+\epsilon)|j|}.       \tag{9}
\]
Consequently
\[
 (G^0)_{n,k}=e^{\eta(|n|-|k|)}h_{n-k}                    \tag{10}
\]
has bounded row and column sums. In either product of (8),(10)
the exponential factors cancel at the intermediate index.
The remaining finite convolution is the identity. Thus (10)
is an exact bounded two-sided inverse of (8). Decrease \(c_*\)
to include this model. No separate small-\(\eta\) real-part test
is required at the reflection.

## 3. A uniform finite-section lower bound

Put \(I_N=\{-K_N,\ldots,K_N\}\) and
\[
 B_N=E_N\Pi_N\mathcal P_N\Pi_NE_N^{-1}.                  \tag{11}
\]
Every nonzero entry has \(|n-k|\le11\), and all entries are
uniformly bounded: the weight ratio is at most
\(e^{11\max\lambda}\).

Take \(L=\lfloor\sqrt N\rfloor\), extend vectors by zero outside
\(I_N\), and use
\[
 \chi_j(k)=L^{-1/2}{\bf1}_{j\le k<j+L},\qquad
 \sum_j\chi_j(k)^2=1.                                   \tag{12}
\]
The finite output space is retained in the commutator bound
\[
 \sum_j\|[B_N,\chi_j]v\|_2^2\le C L^{-1}\|v\|_2^2.       \tag{13}
\]
Indeed each commutator entry is
\((B_N)_{n,k}(\chi_j(k)-\chi_j(n))\); there are at most
23 terms per row, and
\(\sum_j|\chi_j(k)-\chi_j(n)|^2=2|n-k|/L\) on the band.
Cauchy--Schwarz and the uniform entry bound prove (13).

For \(v^{(j)}=\chi_jv\), enlarge its index support by eleven
to include every possible output. There are three frozen comparisons.

* If this enlarged support reaches a hard boundary of \(I_N\),
  use the corresponding half-line, anchored at that boundary,
  with the coefficients frozen at \(t=\alpha\) or \(-\alpha\).
  It has exactly the same retained outputs on this input.
  The opposite hard boundary is out of range for large \(N\).
  Relevant frequencies differ from the endpoint by \(O(L/N)\),
  including the floor error in \(K_N\).
* If the enlarged support meets zero, use (8) on the full line.
  Here all indices are \(O(L)\), so the weight is exactly
  \(e^{\eta|k|}\) for large \(N\). Freeze \(p_\ell(k/N)\)
  at zero.
* Otherwise the enlarged support is interior and has one sign.
  Choose a supported index \(k_j\). On a nonzero diagonal,
  \[
  N\{W(|n|/N)-W(|k|/N)\}
   =(n-k)\operatorname{sgn}(k_j)\lambda(|k_j|/N)+O(L/N).
  \]
  Freezing coefficients at \(k_j/N\) gives the appropriate
  shifted full-line convolution from Section 2. All of its
  outputs on this input remain in \(I_N\).

The coefficient and weight errors in every case have norm
\(O(L/N)\), because the bandwidth is fixed and \(\lambda\)
is Lipschitz. Therefore
\[
 \|B_Nv^{(j)}\|_2\ge(c_*-CL/N)\|v^{(j)}\|_2.             \tag{14}
\]
By (12)--(13) and the triangle inequality in the Hilbert sum
over windows,
\[
 \begin{split}
 (c_*-CL/N)\|v\|_2
 &\le\left(\sum_j\|B_N\chi_jv\|_2^2\right)^{1/2}\\
 &\le\left(\sum_j\|\chi_jB_Nv\|_2^2\right)^{1/2}
                   +CL^{-1/2}\|v\|_2\\
 &=\|B_Nv\|_2+CL^{-1/2}\|v\|_2.
 \end{split}                                             \tag{15}
\]
It follows that, for all sufficiently large \(N\),
\[
 \boxed{\quad \|B_Nv\|_2\ge(c_*/2)\|v\|_2,\qquad
                   \|B_N^{-1}\|\le2/c_* .\quad}          \tag{16}
\]
The matrix is finite and square, so the lower bound proves
invertibility. No infinite-dimensional surjectivity is inferred
from a lower bound alone.

By (2), the leading operator, projection, and weight preserve
the even Fourier subspace. The inverse also preserves it by
uniqueness. Thus (16) supplies the original cosine restriction,
with the zero mode and both finite boundaries included.

## 4. Exact finite perturbation and the original observation

Let \(\mathcal R_N=\mathcal C_N-\mathcal P_N\). The adopted
ordinary-divisibility and same-strip estimates give, in the
orthonormal cosine basis, for every fixed \(\rho>0\),
\[
 |(R_N)_{n,k}|\le C_\rho N^{-1}e^{\rho(k-n)},\qquad
 (R_N)_{n,k}=0\quad(n>k+11).                             \tag{17}
\]
This concerns the whole removable operator, not separated poles
of its finite coefficients. Put \(\lambda_-=\min\lambda>0\)
and choose \(\rho=\lambda_-/2\). On downward entries the weight
adds at most \(e^{-\lambda_-(k-n)}\); there are only eleven
upward diagonals. Both row and column sums of the weighted
remainder are \(O(N^{-1})\). The finite Neumann argument and
(16) prove
\[
 \boxed{\quad
 \|(\Pi_N\mathcal C_N|_{\mathrm{even},\,\deg\le K_N})^{-1}
          \|_{W\to W}\le C .\quad}                       \tag{18}
\]
This is not an accretivity assertion. The same estimates bound
the full output through degree \(K_N+11\).

Retain the complete attached outgoing profile
\[
 |F_{k,N}^+(Z)|\le CN^Ae^{NE_Z(k/N)},\quad
 E_Z(t)=\mathcal E(1/2+t,Z),\quad 0\le k\le U,             \tag{19}
\]
and define the unique compressed solution and exact residual
\[
 g_N=(\Pi_N\mathcal C_N|_{\mathrm{even},\,\deg\le K_N})^{-1}
                       \Pi_NF_N^+,\qquad
 r_N=F_N^+-\mathcal C_Ng_N.                              \tag{20}
\]
Then \(\Pi_Nr_N=0\). Its only generated boundary modes are
\(K_N<k\le K_N+11\); above them the coefficients equal the
input coefficients. Put
\[
 A_W(\alpha,Z)=\max_{0\le t\le\alpha}(E_Z(t)+W(t)),\qquad
 G_W(\alpha,Z)=A_W(\alpha,Z)-W(\alpha).                   \tag{21}
\]
Exactly as in the
[variable-weight source](research_mixed_next_outer_variable_frequency_weight.md),
(18), the full-output bound, and monotonicity of \(E_Z\) give
\[
                         \|r_N\|_{\mathbb R}\le CN^Ae^{NG_W}.     \tag{22}
\]
The eleven boundary coefficients are estimated from the actual
solved system, not replaced by coefficients of its input.

Use also a second sufficiently small constant admissible weight.
The compressed system has a unique solution, so its existing
small-weight estimate bounds that same \(g_N\) by
\(CN^Ae^{NE_Z(0)}\) in the smaller norm. With
\(h_N=Q_{3,N}^{\rm rev}g_N\), the full Hermite identity remains
\[
 \mathcal L_N(F_N^+)=\mathfrak f_N\ell_N(h_N)+\mathcal L_N(r_N),
 \qquad
 \mathfrak f_N=\begin{cases}4\kappa_N^3/N^2,&N\text{ even},\\
                           0,&N\text{ odd}.
             \end{cases}                                \tag{23}
\]
Every first normal, central zero, odd simple node and original
observation scalar is retained. The complete physical inner bound
then yields, for every fixed \(\tau>0\),
\[
 |\mathcal L_N(F_N^+)|\le C_\tau N^{A_\tau}
 \{e^{NE_Z(0)}+e^{N(\mathfrak M_3+G_W+\tau)}\}.             \tag{24}
\]
The first term vanishes at odd levels. A sufficient strict
comparison is still
\[
 E_{Z_*}(0)<\Lambda,\qquad
                   \mathfrak M_3+G_W(\alpha,Z_*)<\Lambda.         \tag{25}
\]
In particular \(t=0\) imposes
\(W(\alpha)>\mathfrak M_3+E_{Z_*}(0)-\Lambda\).
No weight satisfying the budget is supplied by (18).

## 5. A concrete algebraic width and the optimal criterion

The symbol specifies the maximal homotopy width without an arbitrary
weight ansatz. Put \(z=e^{iu}\), \(v=e^{2\pi it}\), and
\[
 Q=2-z-z^{-1},\quad P=2+z+z^{-1},\quad
 L=8+P(z^3v+z^{-3}v^{-1}),\quad
 M=8+P(z^2v+z^{-2}v^{-1}).
\]
Direct substitution in the original definition of \(d\) gives
\[
 p(z,t)=(L^2-Q^2)M-(8+z+z^{-1})LQ^2+10Q^3.              \tag{26}
\]
Its highest and lowest Laurent coefficients are exactly
\(v^3z^{11}\) and \(v^{-3}z^{-11}\). Thus \(z^{11}p(z,t)\)
is a degree-22 polynomial with nonzero leading and constant
coefficients for every real \(t\). Define
\[
 r(t)=\min_{\zeta:\ p(\zeta,t)=0}|\log|\zeta||,
                         \qquad |t|<1/2.               \tag{27}
\]
There are always 22 roots with multiplicity. On any compact
frequency interval their moduli are uniformly bounded above
and away from zero, by the polynomial coefficient bounds
applied both forwards and reciprocally. Root multisets depend
continuously on the coefficients; for example this follows by
isolating the finitely many roots in disjoint small disks and
using the argument principle on their boundaries. Consequently
\(r\) is continuous. Equation (3) proves \(r(t)>0\).

Reality in (2) gives reciprocal-conjugate pairing of roots.
Thus the nearest inner and outer distances from the unit circle
agree. Since \(p(u-is,t)\) evaluates (26) at
\(z=e^se^{iu}\), condition (5) is precisely
\[
                         \lambda(t)<r(t),\qquad0\le t\le\alpha.
                                                               \tag{28}
\]
The strict inequality is needed because (5) includes its top height.

On every compact \([0,\alpha]\), positive Lipschitz lower
approximations to \(r\), constant near zero, approximate it uniformly
from below. To see this, first approximate the positive continuous
function uniformly by a piecewise linear function, subtract a fixed
small error, and flatten it on a sufficiently small initial interval.
Uniform continuity permits that flattening with arbitrarily small
additional error. Choosing the errors below a fixed fraction of
\(\min r\) retains positivity and a strict lower margin.

For a fixed \(Z\), (21) gives the exact saving
\[
 E_Z(0)-G_W(\alpha,Z)
 =\min_{0\le t\le\alpha}
       \left[E_Z(0)-E_Z(t)+\int_t^\alpha\lambda(s)\,ds\right].
\]
The uniform approximation just proved, and the Lipschitz dependence
of a minimum on the uniform norm of its argument, show that its
supremum over the weights admitted by (5) is exactly
\[
 \boxed{\quad
 \mathcal J_Z(\alpha)=
 \min_{0\le t\le\alpha}
       \left[E_Z(0)-E_Z(t)+\int_t^\alpha r(s)\,ds\right].
 \quad}                                                   \tag{29}
\]
The supremum over the allowed compressions is
\(\sup_{0<\alpha<1/2}\mathcal J_Z(\alpha)\).
Equation (29) is an algebraic-root integral criterion with the
original action profile. No value or sufficient sign is asserted.

At \(\alpha=1/2\) the unshifted central symbol vanishes, so
neither (5) nor the inverse theorem licenses that endpoint.
The new result relaxes shifted real-part positivity to a zero-free
homotopy and proves its finite-source application. It does not
suppress the retained residual without (25), or prove the required
stability under arbitrary short partial fillings.

## Frozen sources

- Full-shift inverse, exact coefficients and same-strip remainder:
  7b11e96c482d3c435e3fac0d9a488d0025aae31e2ec9d806949858031381b84c.
- Original all-character symbol:
  c88ba98093fc147f5acfcf1790aa5b6f0f26edda6d741d2efc7c55315942e55e.
- Variable-weight degree estimate and action attachment:
  09caa456c9f27ca22a91521a64c24ded42b4bad7546b591696daaaa82212bfcf.
- Shifted-symbol framework and original forcing:
  858546c9a2762175c32c1ef7b6dd62385051335a613665c9ff1848e0af711ff1.
- Ordinary divisibility and exact degree increase:
  c5cb10096ed4c6aafefdc957958ddaf392ad17c81cab5e7e99dbbe026fc1aed3.
- Complete attached outgoing coefficient profile:
  e39abb76185b6969901b6ee4c95a4f947bdda5f74d8ff57062ed4b6591a0c029.

