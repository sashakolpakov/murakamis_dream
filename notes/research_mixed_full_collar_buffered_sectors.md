# Full first collars with coherent buffers and a mixed interior

Research deduction, 5 November 2026. The finite transport of the next
conditional source removes the small first-subcollar restriction from
the buffered comparison, for all four first-pair type choices. Both
physical second selections are allowed when the second type is four.
The other boundary targets remain in small coherent neighborhoods,
and the original two plateau corridors and arbitrary mixed core remain
present. This is a stronger restricted source comparison, not a global
open-word theorem.

## 1. The complete first-three-factor inputs

Use the actual complete-color reference \(r\) of a fixed open word,
with length large enough for the buffers and corridors in
[the buffered-sector theorem](research_mixed_buffered_endpoint_sectors.md).
Write its first three types as
\((3+\alpha,3+\beta,3+\epsilon)\). Define
\[
 \begin{split}
 \Phi_{123}&=\mathcal T_\alpha(r_1,-2)
           +\phi_{0\beta}(r_1,r_2)-\alpha g(r_1)
           +\phi_{\beta\epsilon}(r_2,r_3),\\
 M_{123}&=\Re\Phi_{123},\qquad
 Q_3=P_{3,b}=\partial_2\phi_{\beta\epsilon}(r_2,r_3).
 \end{split}
 \tag{1}
\]
The first weight is full; the second is split between the two
conditional phases; the third has only its first allocated half.
Original stationarity cancels the first two tangent coefficients.
The remaining plane is
\[
                       M_{123}+\Re[Q_3(z_3-r_3)].
 \tag{2}
\]

At the first collar, put \(X_j=e^{-2\pi iz_j}\), with
\(z_1=x_1\in[0,\rho]\). The literal product is
\[
 \begin{split}
 \mathcal B_{123,N}={}&
 |U_{\alpha,N}(w_L,X_1)C_{\beta,N}(X_1,X_2)
                         C_{\epsilon,N}(X_2,X_3)|\\
 &\cdot|d_N(X_1)^\alpha X_1^{-N\sigma_1}|
       |d_N(X_2)^\beta X_2^{-N\sigma_2}|
       |d_N(X_3)|^{\epsilon/2},
 \end{split}
 \tag{3}
\]
where \(\sigma_1\in\{0,\alpha\}\) and
\(\sigma_2\in\{0,\beta\}\). The third coordinate is unselected.
The two second halfweights in the proved local comparisons multiply
to exactly the second full weight in (3).

At \(\Re z_2=\Re r_2\), \(z_3=r_3\), retain every
physical second height. For \(\beta=0\) these lie between
\(c_2=\Im r_2\) and zero. For \(\beta=1\), they lie in
\([c_2,0]\) when unselected and \([0,.014]\) when selected.
The completed
[type-three source transport](research_mixed_three_first_source_transport.md)
and [type-four source transport](research_mixed_four_fixed_contour_transport.md)
give the following finite losses for (3) relative to \(M_{123}\):
\[
 \begin{array}{c|cccc}
 (3+\alpha,3+\beta)&(3,3)&(4,3)&(3,4)&(4,4)\\\hline
 \text{loss}&1/40&1/50&1/25&1/25.
 \end{array}
 \tag{4}
\]
Each assertion retains the full collar, both parities, the literal
ordinary-color polynomial, every finite row and every index current.
It is an upper bound relative to the original action, not a new
moving-target Gaussian packet.

The proofs supply continuous contour and full-row rate majorants
with strict room beyond the common loss \(1/50\), before their
arbitrary final source tolerance. For the second-three cases the
raw reserves exceed \(.03,.024\). For the second-four cases
the pair reserve \(1/20\), less the next-source allowance
\(13/2000\), leaves \(87/2000>1/25\). We use this
explicit room when perturbing the two real neighbors.

## 2. Stability of the literal upper bounds under small real changes

**Lemma 1.** There are fixed small real neighborhoods of
\(\Re r_2,\Re r_3\), and a sufficiently small fixed ordinary-color
disk, such that uniformly over those neighborhoods and the entire
first collar,
\[
 \frac1N\log\mathcal B_{123,N}
       \le M_{123}+\Re[Q_3(z_3-r_3)]-1/100+O(\log N/N).
 \tag{5}
\]
The third height remains \(\Im r_3\), and the second height
is its actual physical height for the chosen selection. No
\(x_1\le\tau\rho\) restriction is required.

*Proof.* Keep the exact reference contours used in the two finite
transport proofs. The closed height intervals, the collar, and the
finitely many selections are compact. All central factorial arguments
remain in fixed regular strips when the second and third real
coordinates change sufficiently little. The corresponding phase
functions, Gaussian-free upper symbols and horizontal/vertical alias
penalties are continuous uniformly on these fixed compact contours.
Thus their exponential upper rates change by an arbitrarily small
amount.

For the complementary real rows use their zero-safe product-integral
upper rates, not the logarithm of an individual finite value. These
integrals are jointly continuous in the row coordinate and the complex
parameters, including a numerator zero: locally the only singularity
is the integrable function \(\log|t-z|\). On a compact family its
integral has a uniform modulus of continuity. Taking a supremum over
the fixed compact row intervals preserves continuity. The standard
zero-safe finite-product upper estimates used in the original source
proofs are uniform on a slightly enlarged compact family. Consequently
this step retains the revived rows and physical zeros, without dividing
by a zero or differentiating its logarithm.

The same reasoning applies to each of the two genuine selected Fourier
upper branches. Their maximum is continuous, and the unchanged first
collar polynomial bound is already uniform. The first conditional
pair's row ceiling is independent of the second real angle. All factors
and allocations in (3) are therefore covered by a continuous majorant
of the same complete source. This is stronger information than the
value of the original finite sum at its reference; it is supplied by
the explicit fixed-contour and real-row proofs behind (4).

Choose the two real neighborhoods so that the total rate-majorant
variation is at most \(1/400\). Also choose the third neighborhood
so that
\[
                         |\Re[Q_3(z_3-r_3)]|\le1/400.
 \tag{6}
\]
The original reference derivatives are bounded on the compact actual
reference family. Finally choose the one aggregate local finite-source
and ordinary-color tolerance to be less than \(1/400\). The common
reserve in (4), with the strict room just noted, leaves at least
\[
                \frac1{50}-\frac3{400}
                         =\frac1{80}>\frac1{100}.
 \tag{7}
\]
Equations (6)--(7) give (5), with the original third tangent retained.
The neighborhoods are fixed before \(N\) tends to infinity;
continuity of the individual finite functions is not used to choose
an \(N\)-dependent radius. The constants and neighborhoods may be chosen uniformly on compact
families of the actual fixed-width reference prefixes. No independent
cyclic endpoint-height assignment is used. \(\square\)

Only real coordinates are varied in this lemma. It does not infer
holomorphic derivatives transverse to a real height path from that
path's bound. The ordinary color occurs in the first cap; its fixed
derivative bounds were already proved on a complex color disk, so
they persist on smaller such disks in (5).

## 3. There is no further height reset in the remaining buffer

Replace only the active-left condition of the buffered-sector theorem
by the following one. Allow any first two types, take the full
\(x_1\in[0,\rho]\), allow both \(\sigma_1,\sigma_2\)
as in (3), and keep the second and third real coordinates in the
neighborhoods of Lemma 1. Positions \(3,\ldots,p-1\) are
unselected and in a small coherent buffer neighborhood at their
reference heights. The second coordinate retains its physical height.
All these real coordinates remain in the plateau.

Changing the second selection changes only its own height. Every
cutoff from its real coordinate into position three is one for
both row cutoff choices, as are the other buffer cutoffs. Hence
position three and every later buffer height stay at their reference
values. The potentially large second-height change has already been
included in the whole product (3). No residual edge with that changed
height remains after its two incident conditional factors are grouped.

Let \(G_{L,N}\) be the literal left rate with the synthetic
closing terms removed, as in (3) of the buffered-sector theorem.
Adding the later allocated phases to (5) gives the exact tangent
cancellation
\[
 \begin{split}
 G_{L,N}\le -1/100
       +\sum_{j=4}^{p-1}\Re\{\phi_j(z_{j-1},z_j)
                                      -\Gamma_j(z_{j-1},z_j)\}
       +O(\log N/N).
 \end{split}
 \tag{8}
\]
Indeed \(Q_3\) cancels the first derivative of \(\phi_4\)
at the reference; the subsequent shared derivatives cancel in order,
and the last one cancels the original cut tangent. The third Fourier
halfweight in (3) and its other half in \(\phi_4\) are each
used once. The initial two reference tangents already canceled in
(1)--(2).

Every residual in (8) is a horizontal unselected local residual,
with both arguments at their reference heights. The existing local
source packets and negative real Hessian make them nonpositive on
the chosen small coherent neighborhoods. Thus
\[
                         G_{L,N}\le-1/100+O(\log N/N).
 \tag{9}
\]
The smallness requirement now concerns the neighboring real targets,
not the first collar's fractional depth.

## 4. Attachment to the unchanged corridors and arbitrary core

**Theorem 2.** Keep the two plateau corridors, two triple pins,
safe actual open reference, and arbitrary mixed core of
[the buffered-sector theorem](research_mixed_buffered_endpoint_sectors.md).
Use the enlarged active-left condition of Section 3. At an active
right end use that theorem's Corollary 4, with its small coherent
buffer and common loss \(1/5000\) near every actual reference.
A neutral end keeps its original coherent hypothesis. Assume at
least one end is active. Then, with
\[
 \ell_L=\frac1{100}\mathbf1_{\rm left\ active},\qquad
 \ell_R=\frac1{5000}\mathbf1_{\rm right\ active},
 \tag{10}
\]
the literal whole-integrand bound is
\[
 \frac1N\log|\mathscr I_{\sigma,N}|-M_{\rm open}
 \le-\ell_L-\ell_R
       -\mathbf1_{\rm right\ active}K(x_m)
       -\frac\kappa2\sum_Mp_j
       +\delta+O_m(\log N/N),\qquad \kappa=1/20000.
 \tag{11}
\]
Here \(\delta>0\) is arbitrarily small after the remaining
middle-source and neutral-color tolerances are chosen. The local
tolerance spent in Lemma 1 is already included in \(\ell_L\)
and is not spent again. Both parities and every fixed ordinary
color derivative hold on smaller color disks.

*Proof.* Substitute (9) for the old active-left bound. The synthetic
closing terms still telescope exactly into the two plateau corridors.
Their distinct clean edges pay the same two outer pinning fees, while
the unchanged middle occupation pays the inner fees. No boundary
source factor is part of that middle payment. The arbitrary mixed
core and its completion loss therefore remain exactly as in the
original theorem. Its right-side proof is unchanged. Summing these
inequalities gives (11). \(\square\)

Taking \(\delta<(\ell_L+\ell_R)/2\) gives strict suppression
after polynomial normalization and integration over this restricted
region. This removes the small-subcollar and second-selection
exclusions from the active left family. It does not allow arbitrary
second or third real coordinates, noncoherent physical buffers, or
missing plateau corridors. Those remain genuine boundary-comparison
obligations; no full open-source asymptotic is asserted.
