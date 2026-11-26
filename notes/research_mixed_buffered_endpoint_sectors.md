# Endpoint losses with an arbitrary mixed interior

Research deduction, 5 November 2026. The proved first-collar and terminal
right-sector comparisons can be attached to a mixed interior without
setting that interior to its reference. The hypotheses retain a fixed
coherent buffer at each physical end and an unselected plateau corridor
between each buffer and the mixed core. Triple pinning pays its errors
from ordinary plateau curvature and the retained middle occupation.
This removes the specified family of configurations from the global
boundary comparison. It does not cover arbitrary boundary targets.

## 1. Physical buffers, corridors, and the actual reference

Use the actual complete-color open critical point and the definitions
\(I=[p-2,q+1]\), \(B_{L,N},B_{R,N},D_I,F_N\) from
[the finite-boundary reduction](research_mixed_open_finite_boundary_windows.md).
Choose safe fixed-width physical buffers, for example
\(p=16,q=m-15\), when the following corridors fit. All reference
windows used in the middle have the original eight-vertex safety halo.
No periodic reference replaces this open critical point.

A **coherent buffer neighborhood** means a sufficiently small real
neighborhood of its actual retained reference coordinates, at their
reference imaginary heights, with every selection absent. Each such
real coordinate lies in \(P=[.22,.45]\). The proved complete local
factor packets and original negative-Hessian estimates apply there.
The neighborhoods can be chosen uniformly on compact families of
fixed-width actual reference prefixes or suffixes. This is the
one-external-leg compact family from the boundary reduction; it is
not an independent assignment of refined cyclic endpoint heights.

At the left end use one of two states:

* **Neutral left:** positions \(1,\ldots,p-1\) lie in their
  coherent buffer neighborhood.
* **Active left:** the word starts \((3,3)\),
  \(0\le x_1\le\tau\rho\), and positions
  \(2,\ldots,p-1\) lie in a small real buffer neighborhood.
  The actual hybrid height of position two is retained; it is not
  set to zero. The fixed number \(\tau>0\) is chosen below.

At the right end use one of two states:

* **Neutral right:** positions \(q,\ldots,m\) lie in their
  coherent buffer neighborhood.
* **Active right:** \(x_m\in[1/2,1]\), either allowed terminal
  selection is retained, and positions \(q,\ldots,m-1\) lie
  in a coherent buffer neighborhood. In addition the actual direct
  neighbor \(r_{m-1}\) belongs to a specified compact subset
  \(K_\nu\Subset\operatorname{int}R_{3+\nu}\), where
  \[
  R_3=[.30,.39]+i[-.03,.02],\qquad
  R_4=[.27,.33]+i[-.057,-.001].                           \tag{1}
  \]
  The neighborhood is small enough that its actual direct target
  stays in the same rectangle at the unchanged reference height.

The active-right condition is a genuine additional restriction on
the actual open reference. The wider endpoint disks are not substituted
for (1). The right-angle motion does not attenuate its neighbor:
the terminal real cutoff remains one throughout this right sector.

Put \(d=352\), \(\ell=2d+7=711\). Choose disjoint blocks
\[
 [l,l+\ell-1],\qquad [r,r+\ell-1],\qquad
 l\ge p+1,\quad r+\ell-1\le q-2.                      \tag{2}
\]
Require every symbol from \(p\) through the end of the left block,
and from the beginning of the right block through \(q-1\), to be
unselected and in \(P\). These are the two plateau corridors.
All intervening safe symbols may be arbitrary original hybrid symbols,
including selected, early, seam, and right coordinates. In particular
the mixed core is not assumed close to its reference or unselected.

The fixed collar \(\rho\) satisfies all previously required source
and contour restrictions, including \(\rho\le.001\).
All sizes are chosen before the level tends to infinity.

## 2. The actual source rates at the two buffer cuts

Remove only the synthetic closing terms from the definitions of the
boundary rates, and write
\[
\begin{split}
 G_{L,N}&=N^{-1}\log L_N-M_L
                     +\Re[P_{p,a}(z_{p-1}-r_{p-1})],\\
 G_{R,N}&=N^{-1}\log R_N-M_R
                     +\Re[P_{q,b}(z_q-r_q)].             \tag{3}
\end{split}
\]
The source products \(L_N,R_N\) remain literal, including their
cut halfweights. Thus \(B_{L,N}=G_{L,N}-A_p\) and
\(B_{R,N}=G_{R,N}-E_q\). No endpoint factor or remaining
complex tangent has been discarded.

At complete colors, a neutral buffer has
\[
                   G_{\partial,N}\le O(\log N/N).       \tag{4}
\]
Here and below constants may depend on the fixed word. To verify the
sign of its leading rate, retain the actual endpoint phase and subtract
its own tangent, and do the same for every ordinary allocated phase.
All linear terms cancel against the single cut tangent in (3).
On a horizontal buffer neighborhood the remaining quadratic forms
are nonpositive. This is the original one-ended negative Hessian
and its complex Schur complement, not positivity of a finite kernel.

For clarity, the left endpoint phase in this decomposition is
\(\mathcal T_{\epsilon_1}-\epsilon_1g/2\). At the right end
combine the final conditional kernel, \(H_N\), and the full last
diagonal weight before taking their Schur complement; allocate the
remaining external halfweight once. Before elimination the real
Hessian is the sum of the endpoint \(B\) form, the endpoint
\(W\) form, the adjacent \(V\) form, and the nonnegative own
terms of [the open Hessian proof](research_mixed_open_word_hessian.md).
Consequently the local statement (4) also controls the free coordinate
at the buffer cut. It does not rely on the false separate inequality
\(B_{\partial,N}\le0\), whose synthetic closing term is still absent
from (3).

For an active right buffer, use the entire-right estimate from
[the calibrated raw terminal theorem](research_mixed_terminal_raw_half_gap.md).
Its optimized endpoint action is \(P_\epsilon(a)\), with
\(a=z_{m-1}\). Together with the external allocated halfweight
the endpoint phase is
\(P_\epsilon(a)-\nu g(a)/2\). Its tangent cancels the preceding
ordinary derivative at the reference, and its negative Hessian is
positive on the same local source neighborhood. This gives
\[
 G_{R,N}\le-\frac1{400}-K(x_m)+O(\log N/N),
 \qquad K(e)=-\int_{1/2}^e\log\sin\pi t\,dt\ge0.       \tag{5}
\]
The neighboring height in this argument remains unchanged. Neither
the raw comparison nor this attachment asserts a sign after arbitrary
height attenuation or outside (1).

## 3. The first collar leaves a small, payable height change

The [three-three collar theorem](research_mixed_three_cap_collar_comparison.md)
bounds the exact first two factors by their actual affine plane,
with finite loss \(1/40\), when \(\Re z_2=\Re r_2\).
Its raw kernel ceiling is independent of the second real angle.
Thus a small change of that angle costs at most
\(L|\Re z_2-\Re r_2|\), where \(L\) bounds
\(|\Re P_{2,b}|\) on the actual compact reference family.
Choose the buffer neighborhood so this is at most \(1/400\).
The pair then retains finite loss \(9/400\).

The first seam preserves the neighboring height exactly at \(x_1=0\).
For the physical collar and the other buffer cutoffs equal to one,
\[
 \Im z_2=c_2(1-x_1/\rho),\qquad
 \Delta h_2=\Im z_2-\Im r_2=-c_2x_1/\rho,
 \qquad |c_2|<.093.                                    \tag{6}
\]
All other buffer heights remain their reference heights. The first
pair estimate already includes this full attenuation and its surviving
second tangent. The only extra phase to pay is the next incidence,
the actual conditional block \(\phi_3\).

Let \(A=-\Re\phi_3''\) and \(B=-\Im\phi_3''\) on a compact
convex source neighborhood of its actual reference. The ordinary local
source and Hessian theorems give \(A>0\) there; after shrinking the
neighborhood there is a finite uniform constant \(C\) such that
\[
                      A+B A^{-1}B\preceq C I.            \tag{7}
\]
This constant is compact-defined, not numerically evaluated. Completing
the square gives, for real \(u,v\),
\[
 \Re[(u+iv)^T\phi_3''(u+iv)]
       \le v^T(A+B A^{-1}B)v.
\]
The Taylor formula along the actual segment therefore proves
\[
 \Re\{\phi_3(z_2,z_3)-\Gamma_3(z_2,z_3)\}
                                  \le\frac C2|\Delta h_2|^2.
                                                               \tag{8}
\]
Every later buffer residual is nonpositive by horizontal concavity.
Choose a fixed \(\tau>0\), small enough to remain in these genuine
source neighborhoods, with
\[
                         \frac C2(.093\tau)^2\le1/400.
                                                               \tag{9}
\]
Summing the exact tangents after the first pair now gives
\[
                         G_{L,N}\le-1/50+O(\log N/N).    \tag{10}
\]
In detail, the leading remainder after that pair is exactly
\(\sum_{j=3}^{p-1}\Re(\phi_j-\Gamma_j)\); the derivative
\(P_{2,b}\) cancels \(P_{3,a}\), and the last derivative cancels
the cut tangent in (3). This is why the first-pair loss cannot simply
be asserted for the whole original collar without (8)--(9).

The compact source neighborhoods and the constants in this section
may be chosen uniformly over the fixed-width reference families.
Their existence uses only the completed local packets and strict
Hessian bounds. No cyclic height bound is imposed on the actual first
or second open leg, and no numerical value of \(C\) is asserted.

## 4. The arbitrary safe middle remains present

Apply the two good-block replacements from the finite-boundary
reduction to (2). The central triple of each block is pinned to its
reference; the intervening mixed component is retained. Denote its
occupation by \(\sum_M p_j\). Exactly as in that proof,
\[
\begin{split}
 F_N\le{}&B_{L,N}-D_L+a_d(u_L-a_{u_L})^2\\
         &+B_{R,N}-D_R+a_d(v_R-a_{v_R})^2
                         -\frac\kappa2\sum_Mp_j,\\
 &a_d=1000(99/101)^{704}<1/1296,
                    \qquad\kappa=1/20000.               \tag{11}
\end{split}
\]
The inner endpoint fees are paid by the middle occupation, not by
assuming its coordinates vanish. The two outer endpoint coordinates
are unchanged by the replacement.

The remaining synthetic terms telescope exactly. If \(h_L\) is
the first left pinned coordinate and \(h_R\) the last right one,
\[
\begin{split}
 B_{L,N}-D_L&=G_{L,N}+\sum_{j=p}^{h_L}w_j,\\
 B_{R,N}-D_R&=G_{R,N}+\sum_{j=h_R+1}^{q}w_j.             \tag{12}
\end{split}
\]
The edge index convention is that edge \(j\) joins \(j-1,j\).
All weights remaining in these sums are ordinary unselected plateau
weights at their original reference heights. Their reference windows
are safe, including the edges across the physical buffer cuts.
The [extracted plateau curvature](research_mixed_extracted_plateau_curvature.md)
therefore gives the literal local bound
\[
 w_j\le-\frac1{10}
 \{(x_{j-1}-\Re r_{j-1})^2+(x_j-\Re r_j)^2\}.          \tag{13}
\]
One edge adjacent to \(u_L\) in the left sum pays its outer fee
in (11), since \(a_d<1/10\). One edge adjacent to \(v_R\) in
the right sum pays its fee. These edges are distinct and belong to
different pinned components; neither was used in the middle occupation
charge. Every other corridor contribution is nonpositive.

Write \(\ell_L=1/50\) for an active left buffer and zero otherwise,
and \(\ell_R=1/400\) for an active right buffer and zero otherwise.
Combining (4)--(5), (10)--(13) proves
\[
 F_N\le-\ell_L-\ell_R
       -\mathbf1_{\rm right\ active}K(x_m)
       -\frac\kappa2\sum_Mp_j+O_m(\log N/N).             \tag{14}
\]
The occupation here is that of the actual resulting mixed middle,
as in the original pinning theorem. This suffices for an upper bound
on the original configuration; no comparison of its occupation with
the pre-optimization occupation is needed.

## 5. A whole-source consequence with explicit restrictions

**Theorem 1.** Assume the two physical buffers, two plateau corridors,
and safe mixed core described above, and assume at least one end is
active. For any fixed \(\delta>0\), sufficiently small fixed ordinary
color disks give the original complete integrand estimate
\[
 \frac1N\log|\mathscr I_{\sigma,N}|-M_{\rm open}
 \le-\ell_L-\ell_R
       -\mathbf1_{\rm right\ active}K(x_m)
       -\frac\kappa2\sum_Mp_j
       +\delta+O_m(\log N/N).                            \tag{15}
\]
The physical selections in the mixed core and either terminal selection
in the active right sector are retained. The other buffer and corridor
positions are unselected as required by the hypotheses. The same upper
rate holds for each fixed ordinary derivative on smaller color disks.

To obtain (15), add the one middle source tolerance in the original
finite-boundary inequality. A neutral endpoint's holomorphic local
color phase may change by an arbitrarily small fixed amount after its
color disk is reduced; include that amount in this same \(\delta\).
Active endpoint comparisons already retain their literal ordinary
polynomials on fixed color disks. No moving-color action is silently
substituted for \(M_{\rm open}\).

For example, choose \(\delta<(\ell_L+\ell_R)/2\).
Polynomial normalization, the bounded almost-everywhere hybrid Jacobian,
and integration over this region then leave a strict exponential gap
of any fixed size less than \((\ell_L+\ell_R)/2\), at both parities.
Thus this is suppression of a family of regions of the complete source,
not only a comparison of two isolated endpoint factors.

The conclusion does not dispose of configurations with a noncoherent
physical buffer, a selected corridor symbol, an intervening bad symbol
before a required plateau block, a first collar outside the small
subcollar in (9), or a terminal direct neighbor outside (1). Occupation
limits how many bad symbols a near-optimal configuration can have, but
does not move them out of these boundary buffers. Those cases remain
part of the finite boundary inequalities. Neither global boundary
dominance nor survival of the complete local Gaussian is asserted.

## 6. A four-three active left buffer

**Corollary 2.** Theorem 1 also holds if the active-left prefix is
\((4,3)\), with either first selection retained, and its loss is
replaced by
\[
                         \ell_L=3/200.                   \tag{16}
\]
All other buffer, corridor, reference, and safe-middle hypotheses are
unchanged. Choose \(\rho\) small enough for the
[four-three collar theorem](research_mixed_four_three_cap_collar.md)
as well as the earlier restrictions. A further fixed choice of
\(\tau>0\) in (9) is allowed. The \((3,3)\) active-left loss
remains \(1/50\); the neutral-left and active-right losses are
unchanged.

*Proof.* The four-three theorem bounds the literal first pair,
including its full first \(d_N\) weight and either selected monomial,
by the actual affine plane with finite loss \(1/50\). The first
target is real, so the selected monomial has unit modulus. Its second
target is type three, with \(|c_2|<.068<.093\), and its raw kernel
ceiling is again independent of the second real angle. The real
neighborhood chosen in Section 3 therefore spends at most \(1/400\).
The same completion estimate (8)--(9) spends at most another
\(1/400\) on the next incidence. The first pair already contains
its actual attenuation and surviving tangent. Their cancellation
with the later buffer is unchanged, so
\(G_{L,N}\le-3/200+O(\log N/N)\).

The corridor pinning, occupation payment, and two separate outer-fee
payments use none of the first vertex's type. Equations (14)--(15)
follow with (16), including the same single total source/color
tolerance and every fixed ordinary derivative. The arbitrary mixed
middle is still retained. \(\square\)

## 7. An active left buffer whose second type is four

**Corollary 3.** Theorem 1 also holds for an active-left prefix
\((3,4)\) or \((4,4)\), provided its second selection is absent,
\(\sigma_2=0\). Either allowed first selection is retained. Its
active-left loss is
\[
                         \ell_L=9/200.                   \tag{17}
\]
All other buffer, corridor, reference and safe-middle hypotheses
remain unchanged, as do the earlier left and right losses. Choose
\(\rho\) small enough for the
[second-four collar theorem](research_mixed_second_four_cap_collar.md)
and all prior restrictions. A further fixed reduction of \(\tau\)
and of the real buffer neighborhood is allowed.

*Proof.* The second-four theorem bounds the literal first pair by
its actual supporting plane with finite loss \(1/20\). That pair
contains the full first Fourier weight and **one half** of the
second weight. The other half remains in the next allocated phase
\(\phi_3\); neither is discarded or charged twice. Its all-row
source ceiling is independent of the second real angle, so the
same small real-neighborhood choice as in Section 3 spends at most
\(1/400\) against the surviving second tangent.

Because \(\sigma_2=0\), the actual second height is
\(c_2(1-x_1/\rho)\), with \(|c_2|<.102\) by the ordinary
and private type-four union in the second-four theorem. Thus
\(|\Delta h_2|\le.102\tau\) on the active subcollar. The
same actual local source neighborhood and completion argument
(7)--(8), now for the phase carrying the second weight's remaining
half, give a finite constant \(C\). Choose the new fixed \(\tau\)
so that
\[
                         \frac C2(.102\tau)^2\le1/400.  \tag{18}
\]
This keeps the changed arguments in that genuine local packet and
pays the only changed exterior height incidence. A selected second
coordinate is excluded here: its height need not approach the
unselected reference height as \(x_1\to0\), so (18) would not
follow from the collar width.

The first-pair tangent cancels the derivative of \(\phi_3\)
with these exact halfweight allocations. All later buffer residuals
are the same horizontal residuals as before. Consequently
\[
 G_{L,N}\le-\left(\frac1{20}-\frac1{400}-\frac1{400}\right)
                    +O(\log N/N)
           =-\frac9{200}+O(\log N/N).                    \tag{19}
\]
The independent corridor pinning, middle occupation and two outer-fee
payments in Section 4 are unchanged. They yield (15) with (17),
the same single total source/color tolerance, and every fixed
ordinary derivative on smaller color disks. \(\square\)

## 8. The terminal reference need not lie in the old rectangles

**Corollary 4.** In Theorem 1 and its two active-left extensions,
the active-right reference restriction \(r_{m-1}\in K_\nu\)
from Section 1 may be removed. Keep the remaining right-buffer
coordinates unselected and in a sufficiently small coherent
neighbourhood of their actual reference, and replace the active-right
loss by
\[
                           \ell_R=1/5000.                 \tag{20}
\]
All plateau-corridor and safe-middle hypotheses are unchanged.
The earlier stronger right loss still applies under its original
rectangle hypothesis.

*Proof.* The
[remaining-family theorem](research_mixed_terminal_remaining_disk_gaps.md)
gives a finite terminal loss of \(1/1000+K(x_m)\) for the
three ending types \((4,3),(3,4),(4,4)\), on a neighbourhood
of each entire smaller external disk. The
[coupled three-three theorem](research_mixed_terminal_coupled_disk_gap.md)
gives a loss of \(1/5000+K(x_m)\) near every actual reference
ending \((3,3)\) at length at least three. Every word admitting
the two buffers and corridors here has at least that length.
Thus (20) is a common terminal loss for every ending type under
the present hypotheses.

The two three-three blocks use their critical compatibility only
at the reference. Their terminal bound already holds in a small
ambient neighbourhood, so the neighbouring integration target is
free to vary there at its unchanged reference height. In all
families, shrink the right coherent buffer neighbourhood to keep
that target inside the proved terminal-source neighbourhood.

Combine the optimized endpoint action with the adjacent allocated
halfweight and the remaining local phases exactly as in Section 2.
The one-ended negative Hessian and its Schur complement still give
a nonpositive remainder after the cut tangent is removed. Therefore
the revised version of (5) is
\[
 G_{R,N}\le-1/5000-K(x_m)+O(\log N/N).                    \tag{21}
\]
No other term in the corridor telescoping or either pinning-fee
payment changes. Equations (14)--(15) follow with (20), including
the same one total ordinary-colour and source tolerance. This
proves the corollary. \(\square\)

This removes a restriction on the geometric reference. It does
not remove the small-neighbourhood requirement on the other
right-buffer targets or allow arbitrary attenuation of their heights.
