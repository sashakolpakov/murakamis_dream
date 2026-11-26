# The full height change after a second type-three coordinate

Research deduction, 5 November 2026. For prefixes \((3,3)\) and
\((4,3)\), the first-pair collar budget also pays the following
edge's entire vertical **phase** change. No small attenuation or
Taylor reset is needed at this phase level. As in the complementary
[type-four marginal deduction](research_mixed_four_first_vertical_phase.md),
a finite upper bound for the next conditional source on the whole
vertical path remains a separate requirement.

## 1. Actual references and the whole conditional branch

Let an actual complete-color open word have length at least three
and begin with types \((3+\alpha,3)\), where
\(\alpha\in\{0,1\}\). Write its retained references as
\(r_1=a+ih,r_2=b+ic,r_3\), and let the third type be
\(3+\epsilon\). The second block is ordinary. The full-bidisk
image estimate in Proposition 1 of
[the universal image theorem](research_mixed_cyclic_critical_height_bounds.md)
therefore gives
\[
 .267<b<.433,\qquad -.065<c<.068.
 \tag{1}
\]
This is a restriction of the original ordinary block map, not a
periodic repetition of the open word. For the third reference, the
same estimate or the actual private-endpoint rectangle gives
\[
 \begin{cases}
 .267<\Re r_3<.438,\quad -.065<\Im r_3<.068,
       &\epsilon=0,\\
 .24<\Re r_3<.363,\quad -.102<\Im r_3<-.001,
       &\epsilon=1.
 \end{cases}
 \tag{2}
\]
The private case in (2) is needed when the length is three. The
[open-leg coverage](research_mixed_open_local_factor_coverage.md)
and [endpoint rectangles](research_mixed_open_word_endpoint_rectangles.md)
identify these as actual open-reference domains.

Keep \(r_3\) unchanged and unselected and set
\(z(k)=b+ik\), where \(k\) lies between \(c\) and zero.
All real coordinates in (1)--(2) are in the plateau. The inherited
cotangent comparisons in the
[four-three collar proof](research_mixed_four_three_cap_collar.md)
and [second-four collar proof](research_mixed_second_four_cap_collar.md)
give, on the entire path,
\[
 \begin{split}
 &\Re P>0,\quad |\Im P|<.37,
                &&P=\cot\pi z(k),\\
 &\Re Q>0,\quad
 \begin{cases}|\Im Q|<.37,&\epsilon=0,\\
                         0<\Im Q<.61,&\epsilon=1,
 \end{cases}
                &&Q=\cot\pi r_3.
 \end{split}
 \tag{3}
\]
These bounds use the explicit cotangent formula on the full
rectangles; they are not corner samples.

For \(\epsilon=0\), both outer cotangents lie in the original
half-square domain of the
[closed-root theorem](research_mixed_closed_cotangent_roots.md).
For \(\epsilon=1\), they lie in the one-sided cubic chamber
\(-1<\Im P<2/3\), \(0\le\Im Q<1\) proved in the
second-four collar note. Thus the original conditional root has
\[
                   S=u+iv,\qquad u>0,\quad -1<v<1
 \tag{4}
\]
throughout the path. Uniqueness identifies it with the actual
reference root, and the original zero logarithmic lift continues
along the path. This assertion concerns the phase branch only.

## 2. The first marginal and its exact integrated allowance

The next allocated phase is \(\phi_{0\epsilon}(z,r_3)\).
Its first argument is type three and hence has no Fourier halfweight.
The original marginal identity from
[the acute-gradient proof](research_mixed_acute_gradient_height_transfer.md)
is
\[
 \partial_1\phi_{0\epsilon}
       =\log_{\rm R}(S+P)-\log_{\rm R}(S-i).
 \tag{5}
\]
Write \(P=p+i\beta\). Both logarithms have positive-real-part
arguments. The imaginary numerator of their ratio is
\[
                    u(1+\beta)+p(1-v)>0.
 \tag{6}
\]
The difference of the two right-half-plane arguments belongs to
\((-\pi,\pi)\); (6) therefore proves
\[
 0<\theta(k):=\Im\partial_1\phi_{0\epsilon}(z(k),r_3)<\pi,
 \qquad \frac{d}{dk}\Re\phi_{0\epsilon}(z(k),r_3)=-\theta(k).
 \tag{7}
\]
No Hessian or convexity argument is needed to integrate (7).
With
\(D_\epsilon(k)=\Re\phi_{0\epsilon}(z(k),r_3)
 -\Re\phi_{0\epsilon}(r_2,r_3)\), it gives
\[
 D_\epsilon(k)\le A_c(k):=
 \begin{cases}
 0,&c\le0,\ c\le k\le0,\\
 \pi(c-k),&c\ge0,\ 0\le k\le c.
 \end{cases}
 \tag{8}
\]
In particular a negative second reference height makes the entire
next phase nonincreasing as it is attenuated to zero. A positive
height has the explicit allowance in (8).

## 3. The original pair calibration pays exactly this allowance

Use the original first-pair phase
\[
 \Phi_{\alpha3}
  =\mathcal T_\alpha(r_1,-2)+\phi_{00}(r_1,r_2)-\alpha g(r_1),
 \quad M_{\alpha3}=\Re\Phi_{\alpha3},
 \quad P_2=\partial_2\phi_{00}(r_1,r_2).
 \tag{9}
\]
The full first Fourier weight is retained when \(\alpha=1\).
The original first critical equation cancels the first tangent.
The second critical equation gives
\(P_2+\partial_1\phi_{0\epsilon}(r_2,r_3)=0\).
Consequently, for \(\Delta z=z(k)-r_2\),
\[
 \begin{split}
 &[\mathcal C_\alpha(k)-M_{\alpha3}-\Re(P_2\Delta z)]\\
 &\quad+[D_\epsilon(k)
       -\Re\{\partial_1\phi_{0\epsilon}(r_2,r_3)\Delta z\}]\\
 &=\mathcal C_\alpha(k)-M_{\alpha3}+D_\epsilon(k).
 \end{split}
 \tag{10}
\]
Thus (8) pays the next-edge remainder after the supporting planes
are combined; the surviving second tangent is not discarded.
At an unchanged third target the remaining third tangent is zero.
Its coefficient remains present if a later comparison moves that target.

Here the full-row first-pair upper rate, before its one arbitrary
finite-source and ordinary-color tolerance, is
\[
 \begin{split}
 \mathcal C_\alpha(k)&=b_\alpha+M_0(2\pi k_+)
                             +2\Delta_\rho+\alpha\omega(\rho),\\
 b_0&=101/125,\qquad b_1=433/500.
 \end{split}
 \tag{11}
\]
The definitions of \(M_0\), \(\Delta_\rho\), and the actual
first-polynomial allowance \(\omega\) are those in the two
collar proofs. They bound all rows, both level parities and the
literal first Fourier polynomial. The first selected monomial,
when allowed, has unit modulus on the real collar.

For the three-three prefix one may retain its original broader
height bounds \(-.093<c<.073\), \(h_+<.021\).
For the four-three prefix use \(-.065<c<.068\).
Convexity of \(M_0\), together with the already certified
\(M_0(0)<.326\) and \(M_0(.146\pi)<.526\), gives
\[
 M_0(2\pi k_+)+\tfrac\pi2(-c)_++A_c(k)
       <\begin{cases}.326+.073\pi,&\alpha=0,\\
                      .326+.068\pi,&\alpha=1.
         \end{cases}
 \tag{12}
\]
For \(c\le0\), this is the endpoint value \(M_0(0)\)
plus the indicated reference-height debit. For \(c\ge0\),
maximize the convex function
\(M_0(2\pi k)+\pi(c-k)\) at \(k=0,c\).
These are exactly the budgets used in the proved pair comparisons.

Their actual reference floors are
\(M_{03}>1+11/25-(\pi/2)\{h_++(-c)_+\}\) and
\(M_{13}>1+11/25-(\pi/2)(-c)_+\).
Therefore the same certified scalar reserves imply
\[
 \mathcal C_\alpha(k)+\Re\phi_{0\epsilon}(z(k),r_3)
 <M_{\alpha3}+\Re\phi_{0\epsilon}(r_2,r_3)
     -\begin{cases}3/100,&\alpha=0,\\6/250,&\alpha=1.
       \end{cases}
 \tag{13}
\]
For \(\alpha=0\), take the original \(\rho\le.001\).
For \(\alpha=1\), also require
\(2\Delta_\rho+\omega(\rho)<1/100\): the inherited
pre-collar reserve is greater than \(17/500\), leaving
more than \(6/250\). The numerical comparisons here are already
proved in the two collar certificates; no new scalar or root
calculation is used.

Equation (13) is the complete first-cap plus first-two-edge
**phase comparison** at the unchanged third reference. It applies
to the full physical height interval. In particular it does not
require \(x_1\le\tau\rho\). At the exact seam the neighboring
height is preserved, while at the collar face it is zero; no
seam-reset assertion is used.

## 4. The single remaining finite-source requirement

Put \(Y=e^{-2\pi iz(k)}\), \(Z=e^{-2\pi ir_3}\).
To turn (13) into a finite-source comparison, it suffices to prove
the following upper bound on (1)--(2), uniformly in the whole height
path and for either \(\epsilon\):
\[
 |C_{\epsilon,N}(Y,Z)|\,|d_N(Z)|^{\epsilon/2}
 \le C_\eta N^A
      \exp N\{\Re\phi_{0\epsilon}(z(k),r_3)+\eta\}.
 \tag{14}
\]
The second coordinate is type three, so it has no selected branch
or diagonal factor. The third coordinate is unselected, and (14)
contains exactly its allocated halfweight; its other half remains
in the subsequent source. No finite factor is divided out.

**Conditional consequence.** If (14) holds, the literal product
\[
 |U_{\alpha,N}(w,X)C_{0,N}(X,Y)d_N(X)^\alpha X^{-N\sigma_1}|
       |C_{\epsilon,N}(Y,Z)|\,|d_N(Z)|^{\epsilon/2}
 \tag{15}
\]
has finite loss \(1/40\) for prefix \((3,3)\), and
\(1/50\) for prefix \((4,3)\), relative to the reference
sum on the right of (13). Here \(X=e^{-2\pi ix}\),
\(0\le x\le\rho\), and \(\sigma_1\in\{0,\alpha\}\).
Spend one total tolerance smaller than \(1/200\) or \(1/250\),
respectively, after combining all source factors. Both parities
and every fixed ordinary derivative follow on smaller color disks
from the original first-cap bounds. No additional reset error is needed.

The original local packets give a genuine ambient neighborhood of
the reference. They do not by themselves give (14) on the whole
vertical interval. The wider analytic root chamber established
above does not enlarge any finite-source theorem. Together with
the type-four marginal deduction, this identifies one common
remaining kind of estimate for all four first-pair type choices:
an upper bound for the complete next conditional source on its
actual vertical path, retaining all rows, aliases and any allocated
selected branches. This note proves the phase budget, not that
source estimate or a global open-boundary inequality.
