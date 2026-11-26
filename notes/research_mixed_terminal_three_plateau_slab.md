# A whole plateau suffix with a local first-cap coordinate

Research theorem, 5 November 2026. For every fixed mixed word ending
in type three, the complete terminal transform permits a large
unselected contour sector to be controlled by the original critical
point. Only the first retained coordinate must stay in a fixed
neighborhood supplied by the complete first-cap theorem. Every later
retained real coordinate ranges independently over the full plateau.
All these coordinates have their actual unselected reference heights.
The result includes length two, where there are no ordinary conditional
factors. It uses no new roots, covers, or numerical checks.

## 1. The exact contracted source

Fix \(m\ge2\), \(n_j=3+\epsilon_j\), and \(\epsilon_m=0\).
Put \(h=m-1\), \(k_4=\sum_j\epsilon_j\),
\(X_j=e^{-2\pi iz_j}\), and \(P=[.22,.45]\).
The [exact terminal contraction](research_mixed_reversed_cap_assembly.md),
equation (13), has original scalar
\(\kappa_N^{m+k_4}N^{m+k_4-1}\) and integrand
\[
 \mathscr J_N(\mathbf z;w_L,w_R)=
 U_{\epsilon_1,N}(w_L,X_1)
 \prod_{j=2}^{h}C_{\epsilon_j,N}(X_{j-1},X_j)
 \mathcal V_{0,N}(w_R,X_h)
 \prod_{j=1}^{h}d_N(X_j)^{\epsilon_j}.
 \tag{1}
\]
Thus (1) chooses the unselected alternative for each retained
coordinate. The terminal coordinate and all its alternatives were
already summed exactly into \(\mathcal V_{0,N}\). When \(m=2\),
the product of conditional kernels is empty, and the two caps in
(1) use the same single retained coordinate.

Write the actual retained reference as \(r_j=a_j+ic_j\).
The first attached reference belongs to the compact image
\(K_{3+\epsilon_1}\) of
[the complete first-cap theorem](research_mixed_complete_first_cap_packet.md).
Every retained reference lies strictly inside the real plateau, and
every retained type-four height is negative. These are actual
open-word image bounds, including the attached endpoint legs;
no narrower cyclic height interval is used.

There is a uniform \(\rho_*>0\), for the two first-cap types and
their compact actual image families, such that the following sector
is admitted:
\[
 z_1=x_1+ic_1,\quad |x_1-a_1|\le\rho_*,\qquad
 z_j=x_j+ic_j,\quad x_j\in P\quad(2\le j\le h).
 \tag{2}
\]
Choose \(\rho_*\) so that the first interval is contained in \(P\).
All heights remain the reference heights. Since every real coordinate
is in the plateau, the original cutoff factors are one; (2) is the
literal unselected part of the hybrid contour.

## 2. The first cap supplies a quantitative supporting plane

Let \(\mathcal T_\alpha(z,w)\) be the original first-cap phase,
with \(\alpha=\epsilon_1\), and allocate one half of its outgoing
Fourier weight:
\[
 L_\alpha(z)=\mathcal T_\alpha(z,-2)-\frac\alpha2g(z).
 \tag{3}
\]
The other half belongs to the first conditional kernel if \(m\ge3\),
or to the terminal transform if \(m=2\).

**Lemma 1.** The neighborhood in (2) may be chosen so that
\[
 \Re L_\alpha(x+ic_1)
 \le\Re L_\alpha(r_1)+\Re L_\alpha'(r_1)(x-a_1)
                       -\frac{3\pi}{49}(x-a_1)^2.
 \tag{4}
\]
The complete finite cap with its outgoing halfweight has this upper
rate, with any prescribed positive tolerance and polynomial prefactor,
uniformly in a fixed ordinary-color neighborhood.

*Proof.* Before eliminating its private coordinates \((e,u)\),
the real Hessian of (3) is that of
\[
 B(e,u)+W(e,z)-\alpha J(e)-\frac\alpha2J(z),\qquad
 W(e,z)=J(e+z)-J(z).
 \tag{5}
\]
The omitted terms are \(i\pi\) times polynomials with real
coefficients of degree at most two. On the rectangles \(E,U,Q\)
of [the open-word Hessian theorem](research_mixed_open_word_hessian.md),
equations (9)--(10) give
\[
 -\Re B''\succ(6\pi/49)I_{e,u},\qquad
 -\Re W''\succeq(\pi/8)I_z.
 \tag{6}
\]
The additional own terms in (5) have nonnegative negative-real
Hessian. Since \(\pi/8>6\pi/49\), the full three-variable
negative Hessian has real part greater than \((6\pi/49)I\).

The complete first-cap theorem supplies the holomorphic original
critical graph \((e(z),u(z))\) near its compact outgoing images.
At those images its coordinates lie strictly inside \(E\times U\)
and the outgoing coordinate lies strictly inside \(Q\). Compactness
gives a fixed neighborhood in which the graph stays in those rectangles.
The accretive Schur lemma in
[terminal supporting planes](research_terminal_supporting_plane.md),
Section 1, yields \(-\Re L_\alpha''>6\pi/49\) there.
Double integration on the horizontal segment proves (4).

The whole original cap packet is uniform there, including every
private finite row and the ordinary-color germ. At \(\alpha=1\),
the actual negative outgoing height gives the unselected Fourier
halfweight rate \(-\Re g/2\); multiplication realizes (3).
Its source and color errors fit in one prescribed rate tolerance.
No finite Fourier factor is divided out. \(\square\)

## 3. Cancellation on the independent plateau suffix

Put \(\kappa_*=1/2500000\) and \(d_j=x_j-a_j\).
For each ordinary factor \(2\le j\le h\), use its original
allocated phase \(\phi_j\) and the complete independent-plateau
supporting plane from
[three-row source assembly](research_mixed_three_row_source_assembly.md),
equations (4)--(6). Its two endpoint losses are
\(-\kappa_*(d_{j-1}^2+d_j^2)\).
For the terminal transform use
[whole terminal completion](research_mixed_terminal_three_full_completion.md),
equation (9), with \(\Pi=\mathcal P_0-\epsilon_hg/2\);
its loss is \(-\kappa_*d_h^2\).

The allocations are exact:
\[
 L_{\epsilon_1}(r_1)+\sum_{j=2}^{h}\phi_j(r_{j-1},r_j)
                         +\Pi(r_h)=\Phi_{\rm open}(\mathbf r),
 \tag{7}
\]
and every retained marginal of this sum is zero at \(\mathbf r\).
These are the original critical equations after holomorphic
elimination, with the additive calibration of the complete cap,
ordinary factors, and terminal transform. Every retained weight has
two allocated halves. For \(h=1\), (7) simply means
\(L_{\epsilon_1}(r_1)+\Pi(r_1)\), with the same stationarity.

**Theorem 2.** On the whole sector (2), for every \(\tau>0\)
and all sufficiently large integer levels of either parity,
\[
\begin{split}
 N^{-1}\log|\mathscr J_N|
 \le{}&M_{\rm open}+\tau
  -\left(\frac{3\pi}{49}+\kappa_*\right)d_1^2
  -2\kappa_*\sum_{j=2}^{h}d_j^2+O_m(\log N/N)\\
 \le{}&M_{\rm open}+\tau-2\kappa_*\sum_{j=1}^{h}d_j^2
                                  +O_m(\log N/N),
 \quad M_{\rm open}=\Re\Phi_{\rm open}(\mathbf r).
\end{split}
 \tag{8}
\]
The estimate holds on fixed ordinary-color disks at both ends and
for all fixed ordinary-color derivatives on smaller disks, with
the corresponding polynomial prefactors.

*Proof.* Multiply Lemma 1, every complete ordinary source plane,
and the full terminal plane. Equation (7) adds the constant terms
and cancels all linear terms. For \(h\ge2\), the first coordinate
has its cap loss plus one ordinary endpoint loss, every intermediate
coordinate has two ordinary losses, and the last has one ordinary
and one terminal loss. For \(h=1\), the cap and terminal losses
give the displayed first coefficient. This proves (8).
All factors are literal complete sources. For each fixed word,
choose their rate tolerances to sum to \(\tau\), rather than
paying a fixed constant at each edge. Word length affects the
threshold, neighborhoods and polynomial prefactor. Ordinary-color
derivatives are treated by Cauchy before multiplication. \(\square\)

For any fixed \(\eta>0\), the subset of (2) with
\(\sum_jd_j^2\ge\eta^2\) therefore has strict loss
\(\kappa_*\eta^2\), after choosing the total tolerance smaller
than \(\kappa_*\eta^2\) and absorbing polynomial factors for
large \(N\). No moving conditional root at these independent
targets is assumed, and no fixed rate error is multiplied by the
number of coordinates.

## 4. The local packet survives integration over this entire sector

All exact factors in (1) have nonzero original local packets near
\(\mathbf r\). Their phase is (7), the holomorphic Schur reduction
of the original open action. Its negative Hessian has positive real
part by the open-word Hessian theorem. Hence a small horizontal box
around \(\mathbf r\) has a nonzero Gaussian contribution with the
original branch and action.

For the newly completed terminal factor, the needed incoming-variable
neighborhood follows from its actual full-source proof, not just a
value at \(a_*=r_h\). Its central double interpolant is jointly
holomorphic in the incoming variable and ordinary color. Its selected
critical pair is simple. All other currents and real sectors have
strict bare gaps, with regular contour symbols or zero-safe continuous
upper rates. Those gaps persist on a fixed small joint neighborhood
of this reference. Deforming the local central contour to the
continued critical point therefore gives its holomorphic local packet
there. This is only a local continuation; no target critical root on
the whole independent plateau is required for (8).

The complement of that box in (2) has the strict bound following
(8). Integration of (1) over the **entire** sector (2) therefore
has the same local asymptotic, including its original normalization
and relative \(O(N^{-1})\) error. This does not assume a packet
on the whole plateau: complete-source upper planes control its
complement there.

The normalized leading power remains \(N^{-3/2}\). The first cap
contributes \(N^{-1-\epsilon_1/2}\), the ordinary factors
contribute \(N^{-(m-2+k_4-\epsilon_1)/2}\), the full terminal
transform contributes \(N^{-1}\), and the retained Fourier weights
contribute \(N^{-k_4/2}\). Including the scalar and the remaining
\((m-1)\)-dimensional Gaussian gives
\[
 (m+k_4-1)-(1+\epsilon_1/2)
 -\frac{m-2+k_4-\epsilon_1}{2}-1-\frac{k_4}{2}
 -\frac{m-1}{2}=-\frac32.
 \tag{9}
\]
All local symbols and Gaussian determinants are nonzero. At fixed
ordinary derivative orders \(a,b\), the leading power becomes
\(N^{a+b-3/2}\), with the original nonzero factors
\((-\tan\pi u_L/(4\pi))^a\) and
\((-\tan\pi u_R/(4\pi))^b\). Small ordinary-color perturbations
use the local critical germ and a local contour deformation; the
strict complementary gap survives on a fixed pair of disks.

This is a complete contour-sector asymptotic for every fixed length
\(m\ge2\) ending in three. It is not yet the full ordinary closure:
the first retained real coordinate outside its admitted cap
neighborhood, retained selected alternatives, and nonplateau
coordinates remain outside (2). The separately proved first-collar
sector is suppressed, but the intervening first-coordinate region
and those other sectors cannot be discarded by (8). The original
large-word boundary reduction still needs its mixed boundary
comparisons; middle occupation alone does not replace them.
