# Uniform bounds for repeated three/four words

Research theorem, 7 November 2026. The full-period occupation estimate
can absorb the polynomial losses of the noncentral source estimates.
Near the geometric point, the sharp finite-source powers cancel the
Gaussian integration powers. Consequently a repeated word has an
upper bound with a constant per letter, independent of both the level
and the number of repetitions. This improves the exponential-rate
bound in [the spectral-radius theorem](research_mixed_word_spectral_radius.md).
It does not replace the marked boundary observation by a trace.

## 1. Statement and original normalization

Fix a nonempty word \(w=(3+\epsilon_1,\ldots,3+\epsilon_\ell)\),
where \(\epsilon_j\in\{0,1\}\), and put
\[
 k=\sum_j\epsilon_j,\qquad
 W_N=A_{3+\epsilon_1,N}\cdots A_{3+\epsilon_\ell,N},\qquad
 F_w=\mathcal F(z_w),\quad M_w=\Re F_w.
 \tag{1}
\]
All matrices, critical points and action constants are the original
ones in [the complete cyclic theorem](research_mixed_full_cyclic_period.md).
For an integer \(r\ge1\), the word \(w^r\) has length
\(n=r\ell\), contains \(rk\) four-type letters, and has the
repeated original reference with action \(rF_w\). The uniqueness
argument establishing this fact is in Section 1 of the spectral-radius
theorem. Only the reference repeats: the \(n\) integration variables
remain independent.

Use the original hybrid graph with collar width \(10^{-3}\).
For each original selection \(S\), let \(f_{S,N}\) be its
complete finite density and \(z_S(x)\) its graph. Define its total
absolute integral on this particular representation by
\[
 \mathfrak Z_N(w^r)=
 \sum_{S\subseteq E_4(w^r)}\int_{[0,1]^n}
 |f_{S,N}(z_S(x))\det(I+iD\mathcal H_S(x))|\,dx.
 \tag{2}
\]
The conditional sums inside \(f_{S,N}\) are taken before the
modulus in (2). Thus (2) is not the sum of the moduli of all original
individual factorial summands.

**Theorem 1.** There are constants \(C_*\ge1\) and \(N_*\),
independent of the word, its length and \(r\), such that
\[
 |\operatorname{tr}(W_N^r)|\le\mathfrak Z_N(w^r)
                   \le C_*^{r\ell} e^{NrM_w}
       \qquad(r\ge1,\ N\ge N_*).
 \tag{3}
\]
Both level parities are included. In particular,
\[
                         \rho(W_N)\le C_*^\ell e^{NM_w}.
 \tag{4}
\]
In particular (3) at \(r=1\) applies to words whose lengths and
letters vary with \(N\). It is an upper bound; no corresponding
uniform asymptotic or bound for a prescribed cap observation is asserted.

## 2. Local estimates with their exact powers of the level

Write \(a_j=\Re t_j^*\) for the outer reference coordinates;
they satisfy \(.27<a_j<.39\). For a target and selection put
\[
 p_j=\min\{1,\sigma_j+400(\operatorname{clamp}_{[.22,.45]}x_j-a_j)^2\},
                  \qquad \gamma=1/20000.
 \tag{5}
\]
Let \(\mathfrak a_{j,N}\) be the allocated nonnegative block
of equation (5) in the spectral-radius theorem, and let \(e_j\)
be its literal seam-priority, raw-right or coherent upper rate.
The exact product normalization and full occupation inequality are
\[
 |f_{S,N}|=N^{n+rk}\prod_j\mathfrak a_{j,N},\qquad
             \sum_je_j\le rM_w-\gamma\sum_jp_j.
 \tag{6}
\]
Every Fourier polynomial and selected monomial is allocated once.
No inverse of a zero finite factor is used.

Call a symbol good if \(\sigma_j=0\) and
\(x_j\in B=[.25,.40]\). A block is clean if all four symbols
in its dependency window \((j-2,j-1,j,j+1)\) are good.
Otherwise it is dirty. Let \(b\) and \(d\) be the numbers
of bad symbols and dirty blocks, respectively. Each bad symbol
can affect at most four block incidences, so
\[
                 d\le4b,\qquad p_j\ge p_*:=1/25
                       \quad\hbox{at every bad symbol}.
 \tag{7}
\]
For the second assertion, a selected symbol has \(p_j=1\).
An unselected symbol outside \(B\) has distance at least
\(.01\) from its reference after clamping. These incidence
bounds also hold for cycles of lengths one and two; repeated
indices do not create additional distinct dirty blocks.

On a clean block the hybrid heights are exactly the original
reference heights. The complete conditional expansions on the
independent central products, used in Section 3 of
[the central integral theorem](research_mixed_central_outer_integral.md),
give the sharp powers of \(N\) with bounded coefficients.
Specifically, \(C_{\epsilon_j,N}\) contributes
\(N^{-(1+\epsilon_j)/2}\), and its two allocated Fourier
halfweights contribute \(N^{-(\epsilon_{j-1}+\epsilon_j)/4}\).
The actual Fourier polynomial has its reciprocal-factorial
asymptotic on this whole region: equation (15) of that theorem
gives the strict relative margin greater than \(3/100\).
Consequently, for all sufficiently large \(N\),
\[
 \mathfrak a_{j,N}\le C_0N^{-\delta_j}e^{Ne_j},\qquad
 \delta_j=\frac12+\frac14\epsilon_{j-1}
                         +\frac34\epsilon_j,
                         \quad\hbox{on clean blocks}.
 \tag{8}
\]
This uses individual compact block expansions, not a uniformity
claim about a full-word asymptotic error. Theorem 2 of
[independent central rectangles](research_mixed_central_conditional_rectangles.md)
is uniform on four fixed closed typed products, containing every
actual reference height and every target in \(B\). Thus its
constants and thresholds are independent of the word. Notice that
\[
                  \delta_j\le3/2,\qquad
                       \sum_j\delta_j=n/2+rk.
 \tag{9}
\]

On every dirty block use the already proved uniform finite-source
bound, before summing over the word. For every fixed \(\tau>0\),
Section 2 of the spectral-radius theorem gives
\[
             \mathfrak a_{j,N}\le
                       C_\tau N^{b_\tau}e^{N(e_j+\tau)}.
 \tag{10}
\]
This includes the zero seam, right-half rows and both Fourier
alternatives. Here the constants and threshold can be chosen
independently of the word as well. To justify this stronger
uniformity, all coherent target products belong to the fixed closed
typed domains covered by the
[left source packets](research_mixed_early_selected_source_cap.md),
[right-taper products](research_mixed_unselected_right_taper_products.md),
and [left/right interface packets](research_mixed_left_right_interface_source.md).
Deep-low nonseam targets are real and belong to the one compact
square \([10^{-3},1/2]^2\), covered by the
[half-endpoint packet](research_mixed_half_endpoint_conditional_packet.md).
Seam-incident edges instead use the zero-uniform
[height-resolved bounds](research_mixed_height_resolved_seam_sources.md),
including their prescribed seam priority. The remaining raw-right
edges use the zero-safe row and Fourier estimates in
[right-half reduction](research_mixed_right_half_source_reduction.md),
equations (2), (7)--(8). These closed domains cover all allowed
typed heights and cutoff values; they are not word-dependent germs.
The families are finite, so take the maximum of their individual
constants and thresholds, with a fixed tolerance per allocated edge.
No compact-away-from-zero packet is extended through a seam zero.
Combining (8)--(10), and setting
\(C=\max(C_0,C_\tau,1)\), \(B_\tau=b_\tau+3/2\), yields
\[
 \prod_j\mathfrak a_{j,N}
 \le C^nN^{-n/2-rk}N^{B_\tau d}
                       \exp N\left\{\sum_je_j+\tau d\right\}.
 \tag{11}
\]

## 3. Paying for dirty blocks and integrating the remaining loss

Choose once and for all
\[
                     \tau=\gamma p_*/16.
\]
Increase the level threshold, independently of \(r\), until
\(B_\tau\log N/N\le\gamma p_*/16\). Equations (7) imply
\[
 \frac{B_\tau d\log N}{N}+\tau d
   \le\frac{\gamma p_*}{2}b
   \le\frac\gamma2\sum_jp_j.
 \tag{12}
\]
Thus the polynomial and tolerance losses are charged only to
the dirty blocks that require them. From (6) and (11),
\[
 |f_{S,N}(z_S(x))|
 \le C^nN^{n/2}e^{NrM_w}
                 \exp\left\{-\frac{\gamma N}{2}\sum_jp_j\right\}.
 \tag{13}
\]
There is no fixed loss per clean block in the exponential.

It remains to integrate (13), including the selection sum. Put
\(c=\gamma/2\). Because \(.27<a<.39\), the unselected
penalty satisfies on the whole interval
\[
 p(x,0)=\min\{1,400(x-a)^2\}.
 \tag{14}
\]
Indeed outside \([.22,.45]\) both this expression and the
clamped expression equal one. A selected penalty is identically
one. Therefore, uniformly in the reference coordinate,
\[
 \begin{split}
 \int_0^1e^{-cNp(x,0)}\,dx
       &\le\frac{\sqrt\pi}{20\sqrt{cN}}+e^{-cN},\\
 \sum_{\sigma\in\{0,\epsilon\}}
                  \int_0^1e^{-cNp(x,\sigma)}\,dx
       &\le G N^{-1/2},
 \end{split}
 \tag{15}
\]
where the set \(\{0,\epsilon\}\) has one element if
\(\epsilon=0\). For example one may take
\(G=\sqrt\pi/(20\sqrt c)+\sqrt{2/(ce)}\), using
\(\sup_{t>0}\sqrt t\,e^{-ct}=1/\sqrt{2ce}\).

The exact graph bound is \(|\det(I+iD\mathcal H_S)|\le60^n\).
The right side of (13) factors in the real coordinates and
selection labels, even though the original integrand need not.
Sum and integrate it using (15). The \(N^{-n/2}\) from these
integrals cancels the remaining \(N^{n/2}\) in (13), giving
\[
                       \mathfrak Z_N(w^r)
                    \le(60CG)^n e^{NrM_w}.
 \tag{16}
\]
This proves (3) with \(C_*=60CG\). No extra factor
\(2^{rk}\) is needed: the selections were already summed in
(15). The fixed-level identity
\(\rho(W_N)=\limsup_{r\to\infty}|\operatorname{tr}(W_N^r)|^{1/r}\)
then proves (4). Its proof by poles of the trace generating
function is given in Section 3 of the spectral-radius theorem.

## 4. Uniform suppression outside the central region

Let \(I_{B,N}(w^r)\) be the literal original integral with no
selected coordinates and all \(n=r\ell\) real coordinates
in \(B=[.25,.40]\). Its graph heights are the reference heights
and its Jacobian is one. There are universal constants
\(C_1,N_1\), independent of word and repetition, such that
\[
 \left|\operatorname{tr}(W_N^r)-I_{B,N}(w^r)\right|
       \le C_1^{r\ell}\exp\left\{N\left(rM_w-
                                      \frac1{2000000}\right)\right\}
              \quad(N\ge N_1).
 \tag{17}
\]
Indeed the complementary integrals have at least one bad symbol,
so \(\sum p_j\ge p_*\). In (13), split the remaining
penalty as
\[
 e^{-\gamma N\sum p_j/2}
 \le e^{-\gamma Np_*/4}e^{-\gamma N\sum p_j/4}.
\]
Integrate the last factor over the full cube and all selections
using (15) with \(c=\gamma/4\). This leaves only a universal
constant per letter, and \(\gamma p_*/4=1/2000000\).
There is no union-bound factor counting the possible bad positions.
The argument bounds the sum of absolute complementary integrals,
so it applies to their signed sum with its original orientations.

Equation (17) is a uniform comparison with a central integral.
It does not make the fixed-dimensional stationary-phase expansion
of that integral uniform when the word length grows with \(N\).

## 5. A normalized determinant on a fixed disk

Set
\[
 T_N=\kappa_N^{-(\ell+k)}e^{-NF_w}W_N,
              \qquad D_N(z)=\det(I-zT_N),\quad C_w=C_*^\ell.
 \tag{18}
\]
For every fixed integer \(r\ge1\), the complete cyclic theorem
for \(w^r\) gives
\[
 \operatorname{tr}(T_N^r)\longrightarrow A_{w^r},\qquad
 A_{w^r}=\frac{(2\pi)^{r\ell}a(z_{w^r})}
                         {\sqrt{\det[-\mathcal F_{w^r}''(z_{w^r})]}}.
 \tag{19}
\]
The determinant root and symbol are the original Gaussian ones.
The new bound gives \(|\operatorname{tr}(T_N^r)|\le C_w^r\)
simultaneously in \(r\) and all sufficiently large \(N\).
Thus on \(|z|<C_w^{-1}\),
\[
 D_N(z)\longrightarrow
 D_w(z):=\exp\left\{-\sum_{r=1}^{\infty}
                              \frac{A_{w^r}}r z^r\right\}
 \tag{20}
\]
locally uniformly, with every fixed derivative. To prove this,
use \(\rho(T_N)\le C_w\) and expand the finite-dimensional
logarithmic determinant with its value zero at \(z=0\):
\[
 \log D_N(z)=-\sum_{r\ge1}
                         \operatorname{tr}(T_N^r)z^r/r.
\]
The geometric majorant makes the tails uniform on every smaller
disk. Apply (19) to the finitely many remaining terms, then
exponentiate. Cauchy's formula gives convergence of derivatives.
Equivalently the unmarked resolvent traces converge there:
\[
 \operatorname{tr}\bigl(T_N(I-zT_N)^{-1}\bigr)
                 \longrightarrow\sum_{r\ge1}A_{w^r}z^{r-1}.
 \tag{21}
\]

This disk is zero-free for the limiting determinant. Equations
(20)--(21) do not assert convergence on a contour enclosing an
eigenvalue, convergence of spectral projections, or a nonzero
residue after inserting the actual rank-one cap. Those would
require estimates beyond the unmarked traces proved here.
The result supplies a level-uniform upper bound for the complete
conditional representation and a corresponding fixed-domain
generating function; it does not prove the finite-exception theorem.
