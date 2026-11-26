# The complete first retained period of an initial four/four word

Private written consequence, 10 November 2026. The complete right-real
pair bound closes the first retained period of every fixed actual
positive three/four word beginning with four and four, of length at
least three. Both original first Fourier alternatives are included.
The resulting restricted source has exactly the original plateau's
nonzero coefficient, action and normalization.

Every later retained coordinate remains unselected on its original
plateau. The terminal coordinate was already summed exactly. This
does not complete the other retained periods or identify a knot
invariant.

## 1. Exact source, reference and paths

Fix an actual word \(n_j=3+\epsilon_j\), with
\[
 m\ge3,\qquad \epsilon_1=\epsilon_2=1,\qquad
 h=m-1,\qquad k_4=\sum_{j=1}^m\epsilon_j .
 \tag{1}
\]
Retain its original reference \(r_j=a_j+ic_j\), marking, logarithmic
lifts and ordinary colors \(\mathbf w=(w_L,w_R)\). Put
\[
\begin{aligned}
 P&=[11/50,9/20],&
 \mathcal P'&=\prod_{j=2}^{h}(P+ic_j),&
 H_0&=c_1,\quad H_1=1/100,\\
 \kappa_0&=1/2500000,&
 \delta_R&=\kappa_0(9/20-a_1)^2,&
 d_R&=\delta_R/2,\\
 \gamma_{44}&=\kappa_0(a_1-11/50)^2,&
 \gamma_*&=\min\{\gamma_{44},d_R\}>0 .
\end{aligned}
 \tag{2}
\]
The actual-reference family is exactly that of the
[connected-right theorem](research_mixed_initial44_connected_right_contour.md).
In particular \(11/50<a_1<.350\), \(c_1<0\), and the second
coordinate has its actual negative height throughout. The same
attached-input conditions include \(m=3\); no cyclic reference or
independently enlarged input family is used.

After the original exact terminal contraction, the two first-sector
integrands are
\[
\begin{split}
 \mathscr J_{\sigma,N}(\mathbf z;\mathbf w)
 ={}&U_{1,N}(w_L,X_1)
       \prod_{j=2}^{h}C_{\epsilon_j,N}(X_{j-1},X_j)
       \mathcal V_{\epsilon_m,N}(w_R,X_h)\\
 &{}\cdot d_N(X_1)X_1^{-N\sigma}
                   \prod_{j=2}^{h}d_N(X_j)^{\epsilon_j},
 \qquad X_j=e^{-2\pi iz_j},\quad \sigma=0,1 .
\end{split}
 \tag{3}
\]
Here \(q_N=e^{-2\pi i/N}\), \(P_j=(q_N;q_N)_j\), and all
finite functions have their original definitions. We write \(U\)
for the full ordinary-color polynomial \(\mathcal U\) of the exact
torus source. Every later retained selection is zero. The terminal
transform already contains every terminal row, its whole diagonal
weight, its Fourier alternatives and its ordinary-color dependence.
It is not selected a second time.

Equation (13) of
[terminal contraction](research_mixed_reversed_cap_assembly.md)
gives the outside scalar and inherited increasing-angle measure
\[
 S_N=\kappa_N^{m+k_4}N^{m+k_4-1},\qquad
 S_N\,dz_1\cdots dz_h
   =\kappa_N^{m+k_4}N^{k_4}\prod_{j=1}^{h}(N\,dz_j),
 \qquad |\kappa_N|=1 .
 \tag{4}
\]
The clockwise exponential parametrization cancels the sign in
\(dX_j/(2\pi iX_j)=-dz_j\), as in the plateau theorem. A vertical
piece uses its oriented \(dz_1=i\,dy\). No extra sign, residue
power of \(N\), or \(2\pi\) is supplied.

Let \(\mathcal G_\sigma\) and \(\mathcal H_\sigma\) be the ordered
paths
\[
\begin{split}
 \mathcal G_\sigma:\quad
 0&\longrightarrow1/10\longrightarrow1/10+iH_\sigma
 \longrightarrow1/2+iH_\sigma
 \longrightarrow1/2\longrightarrow7/10,\\
 \mathcal H_\sigma&=\mathcal G_\sigma*[7/10,1].
\end{split}
 \tag{5}
\]
The point \(9/20+iH_\sigma\) on the horizontal piece retains
the partition between the established left and right estimates.
The intermediate real points \(7/8\) and \(1-\rho\), for a fixed
endpoint collar width, partition the final real segment only for
its estimates. Both \(\mathcal H_\sigma\) start at zero and end
at the real point one.

Define
\[
\begin{split}
 \mathcal G_N(\mathbf w)
 &=S_N\sum_{\sigma=0}^1
       \int_{\mathcal G_\sigma\times\mathcal P'}
                 \mathscr J_{\sigma,N}\,dz_1\cdots dz_h,\\
 \mathcal H_N(\mathbf w)
 &=S_N\sum_{\sigma=0}^1
       \int_{\mathcal H_\sigma\times\mathcal P'}
                 \mathscr J_{\sigma,N}\,dz_1\cdots dz_h .
\end{split}
 \tag{6}
\]
Let \(\mathcal Z_N^P\) be the original unselected integral on
\(\prod_{j=1}^h(P+ic_j)\), with scalar (4).

Use the original allocated phases and their constants:
\[
\begin{split}
 \Phi(\mathbf z)&=L_1(z_1)+\sum_{j=2}^{h}
                 \phi_j(z_{j-1},z_j)+\Pi(z_h),\\
 M&=\Re\Phi(\mathbf r),\qquad \nabla\Phi(\mathbf r)=0,\\
 \Lambda(x_2)&=\Re\{L_1(r_1)+\phi_2(r_1,r_2)\}
       +\Re\partial_2\phi_2(r_1,r_2)(x_2-a_2).
\end{split}
 \tag{7}
\]

## 2. Complete-first-period theorem

**Theorem.** For each fixed actual word (1), both level parities,
and every \(\tau>0\), there are sufficiently small fixed ordinary
color disks about \((-2,-2)\) and polynomial prefactors such that
\[
 |\mathcal H_N(\mathbf w)-\mathcal Z_N^P(\mathbf w)|
 \le C_{m,\tau}N^{A_{m,\tau}}e^{N(M-\gamma_*+\tau)} .
 \tag{8}
\]
On sufficiently small fixed disks the exact complete-first-period
source has the asymptotic
\[
 \mathcal H_N(\mathbf w)=
 \kappa_N^{m+k_4}N^{-3/2}A_m(\mathbf w)
       e^{N\mathcal F_m(\mathbf w)}
                    \{1+O_{\mathrm{hol}}(N^{-1})\},
 \qquad A_m(\mathbf w)\ne0 .
 \tag{9}
\]
The action, coefficient, Gaussian branch, marking, orientation and
fixed normalized ordinary-color jets are exactly those of the
original plateau theorem. In particular
\(\mathcal F_m(-2,-2)=\Phi(\mathbf r)\).

The phrase “complete first period” is literal: at every allowed
finite level \(N\ge2\), \(\mathcal H_N\) also equals
\[
\begin{split}
 \mathcal H_N(\mathbf w)
 &=S_N\int_{[0,1]\times\mathcal P'}
          \{\mathscr J_{0,N}+\mathscr J_{1,N}\}
                                    \,dx_1\,dz_2\cdots dz_h\\
 &=\kappa_N^{m+k_4}N^{m+k_4-2}
      \int_{\mathcal P'}
       \sum_{j=0}^{N-1}\mathscr J_{0,N}
                      (j/N,\mathbf z';\mathbf w)\,dz_2\cdots dz_h .
\end{split}
 \tag{10}
\]
The later restrictions and selections in (3) are unchanged in both
representations. Constants, thresholds and color disks may depend on
the fixed word. There is no asserted uniformity in word length.

## 3. Payment of the added real segment

Corollary 2 of
[the complete right-real pair theorem](research_mixed_initial44_complete_right_real_arc.md)
gives exactly
\[
\begin{split}
 &|U_{1,N}(w_L,X)C_{1,N}(X,Y)d_N(X)X^{-N\sigma}|
                               |d_N(Y)|^{1/2}\\
 &\hspace{20mm}\le CN^A e^{N\{\Lambda(x_2)-d_R\}},
 \qquad X=e^{-2\pi ix},\quad 7/10\le x\le1,\\
 &\hspace{40mm}
 Y=e^{-2\pi i(x_2+ic_2)},\quad x_2\in P,\quad \sigma=0,1 .
\end{split}
 \tag{11}
\]
This is the full finite pair, not just its critical exponential.
It retains both parities, every cap and conditional row, the exact
Fourier polynomial and its selected monomial. The common bound
includes all real incoming colors and sufficiently small fixed
ordinary-color disks and derivatives. Its closed endpoint \(x=1\)
is proved from the exact periodic source; no factorial asymptotic
is continued through a divisor. Its proof uses one fixed collar
width and a finite cover of \([7/10,1]\), so the constants in (11)
are uniform on this closed interval.

Multiply (11) by the complete unselected ordinary and terminal
supporting planes in equation (5) of
[the whole plateau theorem](research_mixed_full_unselected_plateau.md).
The first diagonal weight in (3) is already used in full.
The other half of \(|d_N(X_2)|\) belongs to factor three when
\(h\ge3\), or directly to the terminal transform when \(h=2\).
The subsequent halves restore their original integer diagonal
powers. These are modulus identities also at zeros; no factor
is divided out and no holomorphic halfpower is introduced.

Original stationarity cancels the first remaining marginal:
\[
 \partial_2\phi_2(r_1,r_2)+\partial_1\phi_3(r_2,r_3)=0
       \quad(h\ge3),\qquad
 \partial_2\phi_2(r_1,r_2)+\Pi'(r_2)=0\quad(h=2).
 \tag{12}
\]
All later marginals cancel likewise, and the constants sum to \(M\).
Coordinate two has one remaining quadratic incidence; every later
coordinate has two. Hence, for any prescribed total allowance,
\[
\begin{split}
 |\mathscr J_{\sigma,N}|
 &\le C_{m,\tau}N^{A_{m,\tau}}
       e^{N\{M-d_R-\mathcal Q_{\mathrm{rem}}(\mathbf x)+\tau\}},
       \qquad z_1\in[7/10,1],\quad\mathbf z'\in\mathcal P',\\
 \mathcal Q_{\mathrm{rem}}(\mathbf x)
 &=\kappa_0(x_2-a_2)^2+
                    2\kappa_0\sum_{j=3}^{h}(x_j-a_j)^2 .
\end{split}
 \tag{13}
\]
For \(m=3\) the sum is empty. Its terminal incidence supplies
exactly the other coordinate-two halfweight and quadratic;
there is no extra ordinary kernel.

Distribute the tolerance among the fixed number of remaining
factors and intersect their color disks with those for (11).
Cauchy estimates on smaller disks apply to the entire holomorphic
source (3), never to an allocated modulus halfweight. This also
gives fixed ordinary-color derivative bounds in (13).

## 4. Exact additivity and the nonzero coefficient

Path additivity gives, at every level,
\[
 \mathcal H_N-\mathcal G_N
 =S_N\sum_{\sigma=0}^1
       \int_{[7/10,1]\times\mathcal P'}
                  \mathscr J_{\sigma,N}\,dz_1\cdots dz_h .
 \tag{14}
\]
The two first Fourier integrals remain separate even on this
common real segment. All lengths and later volumes are fixed.
Equation (13) and the polynomial modulus of (4) give
\[
 |\mathcal H_N-\mathcal G_N|
 \le C_{m,\tau}N^{A_{m,\tau}}e^{N(M-d_R+\tau)} .
 \tag{15}
\]
The connected-right theorem, equation (15a), already proves
\[
 |\mathcal G_N-\mathcal Z_N^P|
 \le C_{m,\tau}N^{A_{m,\tau}}e^{N(M-\gamma_*+\tau)} .
 \tag{16}
\]
The triangle inequality, with one total allowance, proves (8).
This is an additive estimate on the exact source; it does not
replace a current by an unestimated different-height current.

The whole plateau theorem gives (9) for \(\mathcal Z_N^P\),
with its original nonzero coefficient and holomorphic color germ.
Choose the allowance in (8) below \(\gamma_*/8\), then shrink
the common disks so that
\(\Re\mathcal F_m>M-\gamma_*/8\) and \(A_m\) stays away from
zero. Dividing (8) by that original leading term gives an
exponentially small holomorphic relative error, with the polynomial
factor absorbed for sufficiently large \(N\). Adding this error
proves (9); Cauchy's formula gives all fixed normalized jets on
smaller disks. There is no new saddle calculation or change to
the leading power \(N^{-3/2}\).

## 5. The entire first period and its finite root average

For fixed later coordinates and colors, (3) is a finite Laurent
polynomial in \(X_1=e^{-2\pi iz_1}\). It is therefore entire and
one-periodic as a function of \(z_1\). Every \(P_j\) in its
denominators is a nonzero constant. No factorial interpolant is
used here. Cauchy's theorem in the \(z_1\)-plane gives, separately
for each \(\sigma\),
\[
 \int_{\mathcal H_\sigma}\mathscr J_{\sigma,N}\,dz_1
       =\int_0^1\mathscr J_{\sigma,N}\,dx_1 .
 \tag{17}
\]
This is an equality of the exact functions, not an inference from
a phase estimate. It proves the first equality in (10).

The original Fourier bands in equations (2), (6) and (21) of
[exact torus composition](research_mixed_conditional_torus_composition.md)
show that the \(X_1\)-band of \(\mathscr J_{0,N}\) is contained in
\([-N+1,2N-2]\): the cap and \(d_N\) each have degree at most
\(N-1\), and the incoming band of \(C_1\) is \([-N+1,0]\).
Thus the only possible multiples of \(N\) are \(0,N\), and
\[
 \int_0^1\{\mathscr J_{0,N}+\mathscr J_{1,N}\}\,dx_1
   =\frac1N\sum_{j=0}^{N-1}
                  \mathscr J_{0,N}(j/N,\mathbf z';\mathbf w).
 \tag{18}
\]
The selected factor extracts the coefficient at \(N\). The root
average uses \(\mathscr J_0\), not the sum of the two sector values
at the nodes. In particular there is no extra factor two, even
though \(X_1^{-N}=1\) at those nodes. The identity
\(d_N(q_N^j)=P_j^{-1}\) is exact.

Substitute (18) into (6). Its factor \(1/N\) changes (4) to
exactly \(\kappa_N^{m+k_4}N^{m+k_4-2}\), proving the second
equality in (10). At \(m=3\), the single later retained coordinate
and its original terminal transform remain present. Every finite
identity is polynomial in the ordinary colors, so the same
normalizations hold for their derivatives and both level parities.
This completes the proof of the theorem.

The theorem removes the first retained-coordinate period restriction,
including its selected alternative, while preserving the original
action-volume calibration of the restricted source. Every later
retained coordinate is still in \(\mathcal P'\) with selection zero.
Departures of those coordinates, their other Fourier sectors,
general short partial fillings, and ordinary closing retain their
separate obligations. No whole-word volume or knot identification
is inferred.

## Direct source versions

| Direct source | SHA-256 |
|---|---|
| research_mixed_initial44_connected_right_contour.md | cfda9bcc96bb0b0827df17f6bdcc0d7403841f5e6289cf54d80511e99925aa13 |
| research_mixed_initial44_complete_right_real_arc.md | 5ce18a7e361bdb2dc38d67cc9805da0b04361d45c26a06a5c25446599ba814a0 |
| research_mixed_full_unselected_plateau.md | abd5dcddc9ed5057b6658bd8b7b60922540fd664c0c5c794135b19c1678c62a6 |
| research_mixed_reversed_cap_assembly.md | 79d44dfbcfe8c598783f27a49dea5bc716cc62e0a2c4762a238f3b2afffd244c |
| research_mixed_conditional_torus_composition.md | 8a25a25a95bf11767c4f305317a6fab9a9c17724ae0e24a36014b5fd8ec4f693 |

The complete written proof and directly used source implications
were read, and the source hashes checked. No mathematical numerical
evaluation, saved-value arithmetic, import, test, compilation or
frozen-source edit was used. Independent full proof and direct-source
review is required before adoption.
