# Boundary estimates for chains inside the half-period

Research deduction, 5 November 2026. The numerical source and phase
inputs cited below are already proved. This note adds no numerical
certificate. It extracts an
explicit six-edge boundary bound from their pointwise cyclic inequalities;
it does not infer a pointwise bound from an integrated asymptotic.

## 1. The original local weight and its cyclic inequality

Fix a periodic type word \(\epsilon_j\in\{0,1\}\) of period
\(m\ge1\), where 0 means type three and 1 means type four. Let
\(r_j\) be its original geometric outer critical coordinates, extended
periodically to all integer indices. Use the original allocated phase
\[
\begin{split}
 \phi_j(a,b)&=\phi_{\epsilon_{j-1},\epsilon_j}(a,b),\\
 \phi_{\eta\epsilon}(a,b)
 &=g(s+a)+g(s+b)-(2+\epsilon)g(s)+2\pi ias
       -(1+\eta/2)g(a)-(1+\epsilon/2)g(b),\\
 g(z)&=\frac{\operatorname{Li}_2(e^{-2\pi iz})-\pi^2/6}{2\pi i}.
                                                               \tag{1}
\end{split}
\]
Here \(s=s_\epsilon(a,b)\) is the original zero-logarithmic-lift
conditional critical point, on the source branch proved in the
[complete nonlow-half theorem](research_mixed_full_nonlow_half_region.md).
In particular, neither a different algebraic root nor an undetermined
additive action constant is permitted in (1).

Put \(A=[.1,.5]\). A symbol at position \(j\) is
\(q_j=(x_j,\sigma_j)\), where \(x_j\in A\) and
\(\sigma_j\in\{0,\epsilon_j\}\). Define
\[
 R(x)=\begin{cases}1,&.1\le x\le.45,\\
                   400(.5-x)^2,&.45\le x\le.5,
       \end{cases}\qquad
 L_b(x)=\min\{1,(x-.1)/(b-.1)\}.
\]
In row \(j\), take \(b_j=.22,c_j=\Im r_j\) if
\(\sigma_j=0\), and \(b_j=.12,c_j=H=.014\) otherwise.
The target is
\[
 z_j=x_j+i c_jR(x_j)
               \min\{L_{b_j}(x_{j-1}),L_{b_j}(x_j),
                                      L_{b_j}(x_{j+1})\}.     \tag{2}
\]
This is exactly the
[periodic hybrid contour](research_mixed_split_cutoff_hybrid_contour.md)
on \(A\). Its near-zero repair does not enter this domain. The cutoff
in a minimum is chosen by its row, not by the neighboring symbol.

Let the complex tangent to the original block be
\[
 \Gamma_j(a,b)=\phi_j(r_{j-1},r_j)
  +\phi_{j,a}(r_{j-1},r_j)(a-r_{j-1})
  +\phi_{j,b}(r_{j-1},r_j)(b-r_j),
 \qquad
 \chi(z)=\max\{\Re g(z),-2\pi\Im z\}.                       \tag{3}
\]
Define the real edge weight
\[
\begin{split}
 w_j(q_{j-2},q_{j-1},q_j,q_{j+1})
 ={}&\Re\{\phi_j(z_{j-1},z_j)-\Gamma_j(z_{j-1},z_j)\}\\
 &+\frac{\sigma_{j-1}}2\chi(z_{j-1})
   +\frac{\sigma_j}2\chi(z_j).                              \tag{4}
\end{split}
\]
Both alternatives of the actual selected Fourier bound remain in
\(\chi\). Formula (2) shows that (4) depends on exactly the indicated
four real coordinates and only the middle two selections. Including
all four selections in the symbol notation is harmless. Each weight
is continuous, though the minima and maxima need not be differentiable.

**Pointwise cyclic input.** For every cyclic type word, every target in
\(A^m\), and every allowed selection, the established phase proofs give
\[
 \Re\sum_{j=1}^m\phi_j(z_{j-1},z_j)
       +\sum_{j=1}^m\sigma_j\chi(z_j)
       \le M,\qquad
 M=\Re\sum_{j=1}^m\phi_j(r_{j-1},r_j).                       \tag{5}
\]
On the unselected plateau this is critical-point concavity. On the
remainder of the left region it follows from the pointwise minimum
transport and early-block inequalities in the
[full left-region proof](research_mixed_full_left_region.md), including
the selected plateau bounds. For a coordinate above .45, Sections 2--3
of the complete nonlow-half proof remove its selection, clamp it to
.45, and compare to the pointwise left-face bound. Thus (5) is an input
from those phase proofs, not a consequence of their integral estimates.

Original stationarity gives the complex identity
\[
 \sum_j\{\Gamma_j(z_{j-1},z_j)-\phi_j(r_{j-1},r_j)\}
 =\sum_j\{\phi_{j,b}(r)+\phi_{j+1,a}(r)\}(z_j-r_j)=0.
                                                               \tag{6}
\]
It follows that the cyclic sum of (4) is exactly the left side of (5)
minus \(M\), and hence is nonpositive. Repeated incidences in (6)
are literal: for a one-cycle the two partial derivatives belong to
the one diagonal block, and for a two-cycle its two edges stay distinct.

The same assertion holds for any positive integer repetition of the
fixed type word, with the same repeated \(r\). Indeed, repeating its
full original critical coordinates solves every original zero-lift
equation of the longer cycle. The
[universal uniqueness theorem](research_mixed_cyclic_critical_localization.md),
Theorem 3, identifies that solution with the longer word's critical
point. Its conditional branches, tangents and action constants therefore
repeat as well. This argument includes primitive periods one and two;
it does not identify distinct target symbols merely because their types
or reference coordinates repeat.

## 2. Six explicit closing weights

Write the baseline symbol as
\(p_j=(\Re r_j,0)\). All baseline real coordinates are in
\([.22,.45]\), by the proved
[critical height and coordinate bounds](research_mixed_type_four_height_refinement.md).
Thus four baseline symbols give \(z_{j-1}=r_{j-1}\),
\(z_j=r_j\), and
\[
                    w_j(p_{j-2},p_{j-1},p_j,p_{j+1})=0.      \tag{7}
\]

A state at layer \(i\pmod m\) is an admissible triple
\(v=(u_{i-2},u_{i-1},u_i)\). Appending \(u_{i+1}\) shifts
the triple to layer \(i+1\) and has weight \(w_i\).
Define the exit and entry costs
\[
\begin{split}
 E_i(v)={}&w_i(u_{i-2},u_{i-1},u_i,p_{i+1})\\
          &+w_{i+1}(u_{i-1},u_i,p_{i+1},p_{i+2})\\
          &+w_{i+2}(u_i,p_{i+1},p_{i+2},p_{i+3}),             \tag{8}\\
 A_i(v)={}&w_{i-3}(p_{i-5},p_{i-4},p_{i-3},u_{i-2})\\
          &+w_{i-2}(p_{i-4},p_{i-3},u_{i-2},u_{i-1})\\
          &+w_{i-1}(p_{i-3},u_{i-2},u_{i-1},u_i).            \tag{9}
\end{split}
\]
These are explicit original-phase functions of one boundary triple,
its nearby periodic reference data, and its layer. In particular, they
retain the full complex tangent and the physical selected corrections.

**Theorem 1 (open-chain boundary bound).** Let a finite path start in
state \(v\) at layer \(a\), make \(n\ge0\) transitions, and
end in state \(v'\) at layer \(b=a+n\). Its literal weight sum is
\[
 W=\sum_{j=a}^{a+n-1}w_j(q_{j-2},q_{j-1},q_j,q_{j+1}).
\]
Then
\[
                         W\le-A_a(v)-E_b(v').               \tag{10}
\]
The right side uses only the first and last three symbols and their
reference windows. It has six edge terms, regardless of \(n\) or \(m\).

**Proof.** Choose the smallest integer \(k\ge3\) with
\(n+k+3\equiv0\pmod m\). Then \(3\le k\le m+2\).
After the path, append the \(k\) baseline symbols at positions
\(b+1,\ldots,b+k\), followed by copies of its initial three symbols.
The resulting closed walk has length \(T=n+k+3\), a positive multiple
of \(m\). The copied symbols occupy positions
\(a+T-2,a+T-1,a+T\), so their types and layers agree exactly with
the initial triple. No symbol in the prescribed path or its halo has
been changed.

The first three closing transitions have sum \(E_b(v')\). The
last three have sum \(A_a(v)\), by the period alignment. The remaining
\(k-3\) transitions, if any, are entirely baseline and have weight
zero by (7). Apply the cyclic inequality to the repeated word of
length \(T\). It gives \(W+E_b(v')+A_a(v)\le0\), proving
(10). Even when \(k=3\), the six closing transitions are distinct.
For \(m=1,2\), the longer closed walk keeps all its independent target
symbols; only its types and references have the shorter period. Thus
the same proof applies without replacing loops or parallel incidences
by fictitious extra edges. \(\square\)

The six terms cannot in general be replaced by the two endpoint blocks.
The first padded row may still be attenuated by the last prescribed
coordinate, and conversely at the entrance. The three-symbol state
retains exactly this height dependence.

## 3. Uniform boundedness and a normalized potential

There is a finite constant \(K_*\), independent of the period and the
type word, bounding \(|w_j|\) on every local configuration used above.
For clarity this assertion has an explicit compact-supremum definition:
in (1)--(4), take all four local type labels, all allowed selections,
all four real coordinates in \(A\), and independently take the two
reference coordinates in the closed typed rectangles
\[
 \overline R_3=[.30,.39]+i[-.03,.02],\qquad
 \overline R_4=[.27,.33]+i[-.057,-.02].                        \tag{11}
\]
Let \(K_*\) be the supremum of the absolute value of (4) on this
finite union of compact sets. The reference rectangles are in the
plateau source domain, while every target (2) lies in its typed polygon
\(\Omega_3\) or \(\Omega_4\) from the nonlow-half theorem.
The proved source branches are holomorphic on neighborhoods of the
complete products. Therefore the phases and their reference derivatives
are bounded there, and \(K_*<\infty\). No numerical value of this
constant is certified or asserted. The independent reference rectangles
are used only for this bound; cyclic inequality (5) always uses the
actual correlated geometric reference.

In particular, (10) gives \(W\le6K_*\). The explicit boundary
quantity in (10), rather than this coarse constant, is available when
a quantitative comparison with another source gap is required.

**Theorem 2 (continuous boundary potential).** For the fixed periodic
word and reference, there is a continuous real function \(\mathcal H\)
on its layered triple-state space such that every admissible transition
\(v\to v'\) satisfies
\[
 w(v\to v')\le\mathcal H(v')-\mathcal H(v),\qquad
 A_i(v)\le\mathcal H(v)\le-E_i(v).                          \tag{12}
\]
Every baseline state has value zero. Thus
\(|\mathcal H|\le3K_*\), uniformly in the word length, and every
open path obeys the telescoping bound
\(W\le\mathcal H(v')-\mathcal H(v)\).

**Proof.** Fix the baseline state at layer zero. Define
\(\mathcal H(v)\) as the supremum of the weights of all finite
paths from that state to \(v\). A zero-weight baseline path followed
by the three entry transitions reaches any \(v\), proving the lower
bound in (12). Conversely, append the three exit transitions to any
such path, then continue on the baseline to layer zero. The resulting
closed walk has nonpositive weight, so every incoming path has weight
at most \(-E_i(v)\). The supremum is therefore finite. Appending
one transition proves the first inequality in (12). For baseline
states both entry and exit costs vanish, so their values are zero.

For continuity, use the discrete topology for selections and the usual
topology for real symbols within each layer. Any incoming path may
be preceded by sufficiently many zero-weight baseline cycles to have
at least three transitions. Replacing its last three appended symbols
by a nearby terminal triple changes only its last three weights.
Uniform continuity of the finite local weight family gives a modulus
\(\omega\), tending to zero, and hence
\[
 |\mathcal H(v)-\mathcal H(\widetilde v)|
                  \le3\omega(d(v,\widetilde v))             \tag{13}
\]
for states at the same layer and in the same selection component.
Take suprema in both directions; attainment is unnecessary. The
compact local family in (11) supplies a common modulus independently
of the period. \(\square\)

This is a domination inequality, not an equality expressing the weight
as an exact coboundary. No positivity of a kernel, sum, or phase is used.

## 4. Meaning for the original finite source

Write \(X_j=e^{-2\pi iz_j}\). The literal allocated modulus is
\[
 \mathcal B_{j,N}=
 |C_{\epsilon_j,N}(X_{j-1},X_j)|
 |d_N(X_{j-1})X_{j-1}^{-N\sigma_{j-1}}|^{\epsilon_{j-1}/2}
 |d_N(X_j)X_j^{-N\sigma_j}|^{\epsilon_j/2}.                   \tag{14}
\]
Here \(C_{\epsilon,N}\) is the original complete conditional kernel,
with the normalization used in the cited source theorems. Formula (14)
is the same allocation that produces (4); its half-moduli introduce no
new square root branch in the source. The original integer-power product
recombines the two halves at every internal vertex. Endpoint halves
stay displayed for an open product.

The complete uniform source theorem on the typed \(\Omega\)-products,
with the true Fourier upper bound, implies for every tolerance
\(\delta>0\) and every fixed path length \(n\ge1\)
\[
 \prod_{j=a}^{a+n-1}\mathcal B_{j,N}
 \le C_{n,\delta}N^{B_n}
  \exp\!\left(N\left[
    \sum_{j=a}^{a+n-1}\Re\Gamma_j(z_{j-1},z_j)
     -A_a(v)-E_b(v')+\delta\right]\right).                  \tag{15}
\]
Indeed take tolerance less than \(\delta/n\) per block and apply
(10). Both Fourier alternatives, original rows, carriers in modulus,
and both level parities are retained. Zeros cause no difficulty because
the assertion is an upper bound; no division by a finite source is used.

The tangent sum in (15) also has an explicit boundary form. With
\(b=a+n\), internal stationarity cancels every internal linear term:
\[
\begin{split}
 \sum_{j=a}^{b-1}\Gamma_j(z_{j-1},z_j)
 ={}&\sum_{j=a}^{b-1}\phi_j(r_{j-1},r_j)\\
 &+\partial_1\phi_a(r_{a-1},r_a)(z_{a-1}-r_{a-1})\\
 &+\partial_2\phi_{b-1}(r_{b-2},r_{b-1})
                                      (z_{b-1}-r_{b-1}).     \tag{16}
\end{split}
\]
The two surviving targets are determined by the initial and final
triples, respectively. Thus (15) is the original critical bulk action
plus a completely explicit boundary expression. This cancellation
holds along the integer-indexed path even if its reference types and
coordinates have a shorter primitive period.

The phase boundary expression is independent of chain length. The
prefactors, powers and large-level threshold in (15) may depend on the
fixed length; no joint \(n,N\) uniformity is asserted. Nor does this
identify a complete ordinary-endpoint source, prove an open-chain
nonzero coefficient, or control real coordinates outside \(A\).
The potential in (12) does not cancel arbitrary new endpoint factors.
Any use in a larger contour estimate must pay its actual boundary
difference or the explicit six-term remainder in (10).

Reference padding was chosen because its internal weight is exactly
zero. Replacing it by real .5 padding is a different construction:
its bulk weights are generally nonzero, and the available negative
upper bounds on those weights do not give the lower bound on the
closing cost needed to improve (10). A better quantitatively evaluated
closing path is possible in principle, but is not claimed here.
