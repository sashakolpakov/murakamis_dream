# Adding the complete first Fourier alternative on the enlarged interval

Private written deduction, 10 November 2026. A complete estimate for the
first two factors at their selected height can be inserted into the
remaining word without a new loss at every subsequent vertex. The
original stationary equations cancel its outgoing linear term. This
note states that implication for either possible second type and applies
it to the completed four/three and four/four estimates.

The resulting integrals are specified portions of the Fourier
representation. Their complements and the contours joining them are
not identified with these portions.

## 1. The precise prefix hypothesis

Fix a positive word \(n_j=3+\epsilon_j\), \(1\le j\le m\), with
\(m\ge3\), \(\epsilon_j\in\{0,1\}\), and \(\epsilon_1=1\).
Set
\[
 h=m-1,\qquad k_4=\sum_{j=1}^m\epsilon_j,\qquad
 P=[11/50,9/20],\quad E=[1/10,11/50],\quad J=[1/10,9/20].
\tag{1}
\]
Retain the actual reference \(r_j=a_j+ic_j\), logarithmic lifts,
ordinary endpoint colors \(w_L,w_R\), and all finite kernels of the
[original first-selection theorem](research_mixed_first_selected_plateau.md).
Write \(\eta=\epsilon_2\) and put
\[
 H_0=7/625,\qquad H_1=1/100,\qquad
 z_1=x_1+iH_\eta,\quad z_j=x_j+ic_j\ (j\ge2),\quad
 X_j=e^{-2\pi iz_j}.
\tag{2}
\]
Only the first retained coordinate is selected in this section.

Let \(L_1,\phi_j,\Pi\) be the original allocated cap, ordinary,
and terminal phases. Their sum is the calibrated action
\[
 \Phi(\mathbf z)=L_1(z_1)+\sum_{j=2}^{h}\phi_j(z_{j-1},z_j)
                      +\Pi(z_h),\qquad
 M_{\rm open}=\Re\Phi(\mathbf r),\qquad \nabla\Phi(\mathbf r)=0.
\tag{3}
\]
Every retained type-four weight is allocated in two modulus halves
to its incident factors. Define
\[
 \begin{split}
 K_{\eta,N}(w;X,Y)&=U_{1,N}(w,X)C_{\eta,N}(X,Y)d_N(X)X^{-N},\\
 M_{12}&=\Re\{L_1(r_1)+\phi_2(r_1,r_2)\},\qquad
 p_R=\partial_2\phi_2(r_1,r_2).
 \end{split}
\tag{4}
\]
Here \(U_{1,N},C_{\eta,N}\) are complete finite kernels;
\(d_N\) is the original Fourier interpolation polynomial. The
monomial in (4) is part of the selected summand.

The hypothesis used below is the following complete-source inequality:
for some fixed \(d>0\), and every \(\tau>0\),
\[
 |K_{\eta,N}(w;X_1,X_2)|\,|d_N(X_2)|^{\eta/2}
 \le C_\tau N^{A_\tau}
 \exp N\{M_{12}+\Re p_R(x_2-a_2)-d+\tau\}
\tag{5}
\]
on \(E\times P\), with heights (2), both level parities, and a
fixed sufficiently small ordinary-color disk. Every cap term,
ordinary row and contour correction must be included in (5);
a main-integral estimate is insufficient.

For \(\eta=0\), the
[complete selected early-source theorem](research_mixed_selected_four_three_early_complete_source.md)
proves (5) with \(d=1/2000\). Its phase and outgoing derivative
are exactly (4), by equations (7)--(9) of the first-selection theorem.
The [selected plateau theorem](research_mixed_selected_four_three_full_product.md)
gives the same inequality on \(P^2\). Together they prove (5)
on \(J\times P\) with the same \(d\). The common face has no
effect on either pointwise estimates or integrals.

For \(\eta=1\), the
[complete selected early four/four theorem](research_mixed_selected_four_four_early_complete_source.md)
proves (5), including the outgoing modulus halfweight, with the same
\(d=1/2000\). The
[selected four/four plateau theorem](research_mixed_selected_four_four_full_product.md)
extends this inequality to \(J\times P\). Thus (5) is established
for both second types on that entire rectangle. The height in each
case is the corresponding value in (2); it is not varied in this
deduction.

## 2. The remaining unselected factors

The literal terminal-contracted integrand with only position one
selected is
\[
 \mathscr J^c_{\{1\},N}=
 U_{1,N}(w_L,X_1)\prod_{j=2}^{h}C_{\epsilon_j,N}(X_{j-1},X_j)
 \mathcal V_{\epsilon_m,N}(w_R,X_h)
 d_N(X_1)X_1^{-N}\prod_{j=2}^{h}d_N(X_j)^{\epsilon_j}.
\tag{6}
\]
The terminal factor \(\mathcal V\) already contains its full private
sum and its internal Fourier alternatives. The outside scalar is
\(\kappa_N^{m+k_4}N^{m+k_4-1}\), with \(|\kappa_N|=1\).
No additional selection inside that terminal factor is introduced.

**Theorem 1.** Under (5), extended to \(J\times P\) as above,
\[
 |\mathscr J^c_{\{1\},N}|
 \le C_{m,\tau}N^{A_{m,\tau}}
           \exp N\{M_{\rm open}-d+\tau\}
\tag{7}
\]
on \(J\times P^{h-1}\), at the heights (2). Both parities,
fixed small ordinary-color disks, and fixed derivatives in those
colors on smaller disks are included.

*Proof.* Assign the first complete weight and the outgoing halfweight
to (5). Each subsequent complete ordinary factor receives its original
two halves, and the terminal factor receives the last half. These
modulus identities remain valid at zeros. In particular, if \(\eta=1\),
the second half of \(|d_N(X_2)|\) comes from factor three, or directly
from the terminal factor when \(m=3\).

Apply the complete unselected supporting planes from the
[unselected plateau theorem](research_mixed_full_unselected_plateau.md)
to those remaining factors. Their target coordinates are all in their
original plateau and at their original heights. Their constants and
\(M_{12}\) add to \(M_{\rm open}\). The outgoing term in (5)
cancels because
\[
 p_R+\partial_1\phi_3(r_2,r_3)=0\quad(h\ge3),\qquad
 p_R+\Pi'(r_2)=0\quad(h=2).
\tag{8}
\]
Every later linear term cancels by (3). Drop the remaining nonpositive
quadratic losses. The positive first height has already been paid
inside (5); it causes no new height change at the next factor.
Choose the finitely many tolerances with sum less than \(\tau\).
This proves (7). Intersect the fixed color neighborhoods and apply
Cauchy's formula to the complete holomorphic product on smaller
disks to obtain the derivative assertion. No modulus halfweight
is differentiated. \(\square\)

## 3. The nonzero coefficient for the enlarged contribution

For either \(\eta=0\) or \(\eta=1\), let \(I_{0,N}^{+}\) be
the terminal-contracted unselected integral over
\(J\times P^{h-1}\), at its original reference heights, with its
original outside scalar and orientation. Let \(I_{1,N}^{+}\) be
the integral of (6) over that same real box, at heights (2), with
the same outside scalar and orientation. These are defined currents
of different Fourier summands; they are not equal-height integrals
or a contour deformation of one another.

The [unselected four/three assembly](research_mixed_initial43_early_boundary_assembly.md)
and [unselected four/four assembly](research_mixed_initial44_early_boundary_assembly.md),
in their respective cases, already prove
\[
 I_{0,N}^{+}(\mathbf w)=
 \kappa_N^{m+k_4}N^{-3/2}A_m(\mathbf w)
 e^{N\mathcal F_m(\mathbf w)}
                    \{1+O_{\rm hol}(N^{-1})\},\qquad A_m\ne0,
\tag{9}
\]
where \(\mathcal F_m(-2,-2)=\Phi(\mathbf r)\).
The action and coefficient are the original ones.

**Corollary 2.** The sum \(I_{0,N}^{+}+I_{1,N}^{+}\) has exactly
the asymptotic (9), with the same coefficient, phase, power of
\(N\), and fixed normalized ordinary-color derivatives.

*Proof.* The box has fixed finite volume and the outside scalar has
polynomial modulus. Equation (7), with \(d=1/2000\), gives
\[
 |I_{1,N}^{+}|\le CN^B e^{N(M_{\rm open}-d+\tau)}.
\tag{10}
\]
Choose \(\tau<d/8\). Shrink the common color disks so that
\(\Re\mathcal F_m>M_{\rm open}-d/8\) and the original nonzero
amplitude is bounded away from zero. Dividing (10) by the original
leading term in (9) then gives an exponentially small holomorphic
error, including its polynomial prefactor. Cauchy's formula gives
the same conclusion for every fixed normalized derivative on
smaller disks. Adding this error proves the assertion. \(\square\)

The sum in this corollary includes the two first-coordinate choices,
with all other retained coordinates unselected. It is not the complete
knot invariant or the entire open-word polynomial. The unestimated
parts of both Fourier summands remain outside its definition.

## 4. Propagation through the already controlled middle

There is also a direct extension of
[selected-prefix propagation](research_mixed_first_selected_full_middle_propagation.md),
Theorem 1. Keep either of its exact source charts, safe cuts \(p,q\),
eight-vertex safety condition, and protected triples
\[
 T_L=\{p-2,p-1,p\},\qquad T_R=\{q-1,q,q+1\},\qquad
 F=[p+1,q-2].
\tag{11}
\]
The complete prefix (4) must lie before those protected triples.
Keep its second and later targets through the left cut unselected
in \(P\), at their reference heights. Its first real coordinate
may now range over \(J\), at height \(H_\eta\), whenever (5)
has been established.

Let \(G_{L,N}\) be the calibrated logarithmic rate of the literal
left cut product, including its single cut halfweight, as defined
in equations (6)--(7) of that propagation theorem. Multiplying
(5) by the subsequent ordinary supporting planes up to the cut
and using their stationary equations gives
\[
                 G_{L,N}\le-d+\tau_L+O_m(\log N/N).
\tag{12}
\]
This is the proof of (7) stopped before the middle; the last
outgoing derivative cancels with the original incoming cut derivative.
There is no extra selected factor at the cut.

Choose any proved right boundary state for the same chart and retain
all of its type, height, selection and neighborhood conditions.
Write its original calibrated estimate as
\(G_{R,N}\le-\Delta_R-K_R+\tau_R+O_m(\log N/N)\).
The exact cut inequality (10) of
[completed boundary propagation](research_mixed_completed_boundary_state_propagation.md)
then gives
\[
 |\mathscr J_{\sigma,N}|\le CN^A
 \exp N\left\{M_{\rm open}-d-\Delta_R-K_R
              -\frac1{20000}\sum_{i\in F}p_i+\tau\right\},
\tag{13}
\]
where
\[
 p_i=\min\{1,\sigma_i+
                 400(\operatorname{clamp}_P x_i-a_i)^2\}.
\]
Here \(\operatorname{clamp}_P x\) is the nearest point of \(P\)
to \(x\). Every free middle symbol retains the original alphabet,
height rule and selection priority. The first two selections are
\(\sigma_1=1,\sigma_2=0\).

The contracted and uncontracted source charts and their different
outside scalars remain those of the cited exact cut theorem; they
are not combined. The proof consists of substituting (12) and the
chosen right estimate into that theorem's algebraic cut identity.
Its clean closing losses, occupation terms and protected heights
are unchanged. One total tolerance proves (13), with both parities
and the original color neighborhoods and derivatives.

For either second type, (13) has \(d=1/2000\) on the whole
interval \(J\). It replaces the former unquantified small
left overlap by an interval with endpoint \(1/10\). It does not
estimate the height-changing joins to that interval, permit an
unproved right boundary state, or remove the safe-cut conditions.

## Direct source versions

| Source | SHA-256 |
|---|---|
| research_mixed_selected_four_three_early_complete_source.md | c0f4532b7f8d04c3bc4d84f16435029625c469adf1282914f80bf019bd22ebd6 |
| research_mixed_selected_four_three_full_product.md | 410c91677327cbea7f856e705b958ae011f93f29321f2c0c2ed7fc7100432c18 |
| research_mixed_selected_four_four_early_complete_source.md | 760ab93cc36ccba00eea97c518eb3697f55638b90c43c90d5ce1a9cd029ddc05 |
| research_mixed_selected_four_four_full_product.md | 4fadefa2aa2ab731da1c1557aeec77113e2bbd5d491c7fd104011b24766a248d |
| research_mixed_first_selected_plateau.md | 51f5d9ed2a68c21756aa09e18a180562d00a488630dbcb132948fb7f9c375d75 |
| research_mixed_first_selected_full_middle_propagation.md | eabc5a3d769a9fd88ebcf49ad81cb9bf57b5776c17a0caef23ab0337bc302be3 |
| research_mixed_initial43_early_boundary_assembly.md | 8174ad95137353bdcb0acec24497d8fa0087ece417e0f2ddd72ceaf2a26f72fd |
| research_mixed_initial44_early_boundary_assembly.md | 8ed393fd2e465d5399c8ffddc46c2d603ef4c5cb6d154ee561e676aa8bfd2c90 |
| research_mixed_full_unselected_plateau.md | abd5dcddc9ed5057b6658bd8b7b60922540fd664c0c5c794135b19c1678c62a6 |
| research_mixed_completed_boundary_state_propagation.md | cc7b2fc0db168d00e2b75b54ec3ff51496f178e819e4e5c8d5c6b53af563cb48 |

This deduction uses written source implications only. No new mathematical
numerical evaluation, saved-value computation, test or compilation is used.
The manuscripts and the source notes are unchanged.
