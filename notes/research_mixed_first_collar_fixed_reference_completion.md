# A fixed-reference completion of the first collar ending in three

Research deduction, 5 November 2026. For prefixes beginning in
\((3,3)\) or \((4,3)\), the complete first collar can be followed by
independent unselected plateau coordinates. The upper bound retains
the explicit half-row and last-row excess of each ordinary conditional
factor. Its linear terms cancel exactly against the first-pair
tangent. Consequently, proving those two remaining row comparisons
removes the moving-root and small horizontal-neighborhood hypotheses
from this left buffer. No terminal conditional factor or unrestricted
open-word dominance is asserted.

## 1. Actual references and the two remaining row excesses

Fix an actual complete-color open reference
\(r_j=a_j+ic_j\), with types \(3+\epsilon_j\), and assume
\[
 m\ge4,\qquad 3\le h\le m-1,\qquad
 \epsilon_1=\alpha\in\{0,1\},\quad\epsilon_2=0.
 \tag{1}
\]
Thus every conditional block indexed \(3,\ldots,h\) is ordinary,
including when its external input is an attached endpoint leg.
Use the original allocated phase \(\phi_j\), its value \(M_j\),
and its two derivatives at the actual reference:
\[
 M_j=\Re\phi_j(r_{j-1},r_j),\qquad
 P_{j,a}=\partial_1\phi_j(r_{j-1},r_j),\quad
 P_{j,b}=\partial_2\phi_j(r_{j-1},r_j).
 \tag{2}
\]
The two halfweights of an internal coordinate are counted on its
two physical incidences. They are not removed by division.

Let \(P=[.22,.45]\), \(I_3=[.267,.433]\), and take
\[
 y_2\in I_3,\qquad y_3,\ldots,y_h\in P,\qquad d_j=y_j-a_j.
 \tag{3}
\]
Initially retain all reference heights. Put
\[
 \begin{split}
 \kappa_*&=1/2500000,\\
 B_j(y_{j-1},y_j)
 &=M_j+\Re P_{j,a}d_{j-1}+\Re P_{j,b}d_j
                       -\kappa_*(d_{j-1}^2+d_j^2),\\
 D_j&=\left[\max\{\mathcal R_j(1/2),\mathcal R_j(1)\}-B_j\right]_+ .
 \end{split}
 \tag{4}
\]
Here \(\mathcal R_j(u)\) is the full allocated real-row rate of
the [asymmetric contour theorem](research_mixed_horizontal_asymmetric_contour.md),
equation (13), evaluated at
\((y_{j-1}+ic_{j-1},y_j+ic_j)\), with the original chirp and
flags \((\epsilon_{j-1},\epsilon_j)\). In particular its two
factorial allocations are
\(-\epsilon_{j-1}\Re g/2\) and \(-\epsilon_j\Re g/2\).
The endpoint \(u=1\) is its continuous limiting row rate, not an
extra finite row or a deletion of revived rows.

The completed ordinary left-row comparisons for
[own three](research_mixed_three_left_cut_symmetry_completion.md)
and [own four](research_mixed_four_left_cut_support.md), the
[half-index contour](research_mixed_half_index_contour.md), the
[own-four cutoff extension](research_mixed_four_left_cut_extension.md),
and the [right-tail endpoint theorem](research_mixed_right_tail_endpoint_bound.md)
give the complete conditional upper rate
\[
                         V_j=B_j+D_j.
 \tag{5}
\]
For every prescribed tolerance, (5) bounds the literal finite kernel
with its two unselected halfweights, up to a polynomial prefactor
and that tolerance. The contour proof bounds its real tails and
each central current by the same rate. The actual outer heights
are within the admitted \(.108\) range, and the physical type-four
heights are negative. No right-tail conclusion on the larger
auxiliary height rectangle is used.

All functions in (4)--(5) are continuous on the stated compact
horizontal family, by the zero-safe product-integral bounds.
At this stage \(D_j\) is retained; its vanishing is not a premise
of the estimate proved below.

## 2. Type-three attenuation on the enlarged fixed contours

Only the physical second height can change in this prefix. Write
\[
 A(k)=y_2+ik,\qquad
 k\in[\min(c_2,0),\max(c_2,0)],\qquad -.065<c_2<.068 .
 \tag{6}
\]
All later coordinates are unselected. Since their real cutoffs,
including that of \(y_2\), equal one on (3), their heights remain
their reference heights. The first selection changes only its own
factor, not these cutoffs.

The old exact transport lemma extends to the single index rectangle
\[
                    \mathcal K=[1/8,1/2]+i[-1/5,5/4].
 \tag{7}
\]
This contains both enlarged contour choices used for (5).
To verify the extension, set
\(P_A=\cot\pi A=p+i\beta\), \(C=\cot\pi w=u+iv\).
The established type-three path bounds give \(0<p<1\) and
\(\beta>-37/100\). For \(\Re w<1/2\) one has \(u>0\), and
the original normalized bare phase satisfies
\[
 \partial_Aq_\epsilon(w;A,B)
       =\log_{\rm R}(C+P_A)-\log_{\rm R}(C-i).
 \tag{8}
\]
The identity and its original logarithmic lift are those of
[the finite type-three transport proof](research_mixed_three_first_source_transport.md),
equation (7). All shifted real arguments remain strictly between
zero and one on (3), (6), (7); enlarging the fixed imaginary interval
crosses no regular-strip singularity.

The imaginary numerator of the ratio in (8) is
\[
                         u(1+\beta)+p(1-v).
 \tag{9}
\]
It is positive for \(v\le1\). If \(v>1\), the exact cotangent
formula and its monotonicity give
\[
 \frac{v-1}{u}
 \le\frac{\cos(\pi/4)-e^{-2\pi/5}}{\sin(\pi/4)}
 <\frac{47}{75}<\frac{63}{100}.
 \tag{10}
\]
For an elementary verification, put \(t=44/35\). The exponential
series with \(n!\ge2\,3^{n-2}\) for \(n\ge2\) yields
\[
 e^{2\pi/5}<e^t
 \le1+t+\frac{t^2}{2(1-t/3)}
 =\frac{7723}{2135}<\frac{15}{4}.
 \tag{11}
\]
Use also \(\sin(\pi/4)=\cos(\pi/4)<5/7\) in (10).
Thus (9) stays positive. At \(\Re w=1/2\), \(u=0\) and
\(v=-\tanh(\pi\Im w)<1\), so (9) is again positive.
The logarithm of \(C-i\) there is the continuous right-half-plane
boundary value with argument \(-\pi/2\). Consequently
\[
            0<\Im\partial_Aq_\epsilon(w;A(k),B)<\pi
                        \qquad(w\in\mathcal K).
 \tag{12}
\]
The bounds are strict on the compact parameter sets. Half-grid
rounding therefore uses only the already allocated arbitrarily
small tolerance.

Define
\[
 a_c(k)=
 \begin{cases}
 0,&c\le0,\quad c\le k\le0,\\
 \pi(c-k),&c\ge0,\quad0\le k\le c.
 \end{cases}
 \tag{13}
\]
Integrating (12) transports every fixed central current by at most
\(a_{c_2}(k)\). The index contour and its original reference height
remain fixed. Alias penalties do not depend on \(A\).
The exact finite Poisson derivatives in equations (14)--(15) of
the cited type-three proof transport every complementary real row
by the same factor \(e^{Na_{c_2}(k)}\), including wrapped factors,
fixed zeros and zeros appearing at \(k=0\).

The third halfweight is unchanged. Hence the finite upper rate for
edge three at the physical height is
\[
                 B_3+D_3+a_{c_2}(k),
 \tag{14}
\]
with one arbitrarily small tolerance. In particular (14) transports
the fixed-reference upper bound (5); it does not posit a moving
critical root or a packet at the transported parameters.

## 3. The complete prefix and exact tangent cancellation

Put \(X_j=e^{-2\pi iz_j}\), with
\(z_1=x_1\in[0,\rho]\), \(z_2=y_2+ik\), and
\(z_j=y_j+ic_j\) for \(3\le j\le h\).
For \(\sigma_1\in\{0,\alpha\}\), the literal allocated prefix is
\[
 \mathcal L_{h,N}=
 \left|U_{\alpha,N}(w_L,X_1)
                  \prod_{j=2}^h C_{\epsilon_j,N}(X_{j-1},X_j)\right|
 |d_N(X_1)^\alpha X_1^{-N\sigma_1}|
 \prod_{j=2}^{h-1}|d_N(X_j)|^{\epsilon_j}
 |d_N(X_h)|^{\epsilon_h/2}.
 \tag{15}
\]
It retains the full first weight, the full internal weights, and
exactly one cut halfweight. Define \(M_{12},p\) as in equation (2)
of the [first-pair tangent theorem](research_mixed_first_collar_horizontal_tangent.md),
and set \(M_h=M_{12}+\sum_{j=3}^hM_j\).
That theorem's uniform floor and concavity give
\[
 U_{\alpha0}(k)+a_{c_2}(k)
 <M_{12}+p\,d_2-\delta_\alpha,\qquad
 \delta_0=3/100,\quad\delta_1=3/125 .
 \tag{16}
\]
Here \(U_{\alpha0}\) is the full-row first-pair ceiling, including
its collar costs. Equation (16) holds throughout \(I_3\), not
only at \(a_2\).

**Theorem 1.** For every prescribed \(\tau>0\), a sufficiently
small fixed ordinary-color disk and the previous fixed collar give
\[
 \begin{split}
 \frac1N\log\mathcal L_{h,N}
 \le{}&M_h+\Re P_{h,b}d_h-\delta_\alpha+\sum_{j=3}^hD_j+\tau\\
 &-\kappa_*\left(d_2^2+2\sum_{j=3}^{h-1}d_j^2+d_h^2\right)
       +O_h(\log N/N).
 \end{split}
 \tag{17}
\]
This holds for both parities, every target in (3), every height
in (6), and either allowed first selection. If the cut is pinned
to its reference, \(d_h=0\).

*Proof.* Use (16) for the first pair and the height allowance in
(14), then (5) on every remaining ordinary edge. Original
stationarity gives
\[
 p+\Re P_{3,a}=0,\qquad
 P_{j,b}+P_{j+1,a}=0\quad(3\le j<h).
 \tag{18}
\]
Only the displayed cut tangent survives. Each internal displacement
occurs twice in the sum of the quadratic terms; the two end
displacements occur once. This proves (17). For the fixed word,
choose the individual source tolerances to sum to \(\tau\), including
the ordinary-color tolerance of the literal cap. There is no
per-edge fixed rate loss that grows with \(h\). Polynomial
prefactors may depend on this fixed prefix. \(\square\)

**Corollary 2.** If \(D_j=0\) on the target domain for every
\(3\le j\le h\), then at a pinned cut (17), with
\(\tau<1/250\), has a common finite exponential loss \(1/50\)
for both prefixes, in addition to its displayed quadratic loss.
Thus the two ordinary real-row comparisons suffice for this full
independent horizontal prefix; no moving-root source hypothesis
remains.

## 4. Boundary attachment and complex neighborhoods

Take \(h=p-1\) in the original buffered notation. The cut tangent
in (17) cancels the term \(\Re P_{p,a}d_{p-1}\) in \(G_{L,N}\).
The exact prefix (15) is the literal \(L_N\) used there.
Consequently its active-left estimate strengthens to
\[
 G_{L,N}\le-\delta_\alpha+\sum_{j=3}^{p-1}D_j+\tau
       -\kappa_*\left(d_2^2+2\sum_{j=3}^{p-2}d_j^2+d_{p-1}^2\right)
       +O_p(\log N/N).
 \tag{19}
\]
It permits the full first collar, \(y_2\in I_3\), and arbitrary
unselected \(P\) targets at positions \(3,\ldots,p-1\), instead
of their small coherent buffer neighborhoods.

Keep the two safe plateau corridors, triple pins, right buffer and
arbitrary mixed core of the
[buffered-sector theorem](research_mixed_buffered_endpoint_sectors.md).
Its telescoping identity (12) is unchanged. Its distinct safe
corridor edges still pay the outer pinning fees using their
\(1/10\) curvature; the smaller constant \(\kappa_*\) in (19)
is not used to pay those fees. The right comparison and retained
middle occupation are unchanged. In particular, when the excesses
in (19) vanish, this replaces only the active-left buffer condition
by the larger domain just stated, with common left loss \(1/50\).
Without their vanishing, their sum remains an explicit additive
rate in that same whole-integrand inequality.

The [complex extension theorem](research_mixed_horizontal_complex_extension.md)
also applies to these upper bounds. For an individual conditional
factor it applies to the polynomial
\(C_j^2d_N(X_{j-1})^{\epsilon_{j-1}}d_N(X_j)^{\epsilon_j}\);
for (15), square the full prefix to make the cut halfweight an
integer weight. The exponent bands are \(O_h(N)\), and the real
rates in (17) are continuous. Regard \(k\) as an independent
compact label in (6): the proof bounded the full rectangle in
\(x_1,y_2,\ldots,y_h\) at every such fixed height, before imposing
the physical hybrid relation. Thus the extension supplies a fixed
complex neighborhood, with any prescribed extra tolerance.
Its derivative conclusion is for these holomorphic products,
without division by a possibly zero Fourier factor. Fixed ordinary
color derivatives use the already uniform cap color disk and
Cauchy's estimate on a smaller disk.

This is an upper-source completion. It neither supplies a relative
Gaussian packet at moving targets nor removes the excesses in (4).
It does not cover a terminal block \(j=m\), a second type-four
height path on the enlarged contours, selected later coordinates,
or later nonplateau height changes. The unrestricted finite-boundary
comparison and the complete open-source theorem remain separate.
