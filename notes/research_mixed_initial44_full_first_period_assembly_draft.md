# Completing the first retained period of an initial four/four word

**SUPERSEDED UNFROZEN CONDITIONAL DRAFT — 10 November 2026.**
The pending input was subsequently proved. The final author version is
[the complete first-period theorem](research_mixed_initial44_full_first_period.md).
The conditional text below is retained only as the earlier working draft.

The complete pair estimate on the real interval \([7/10,7/8]\)
is still pending. No theorem below asserts that this input has
been proved. This draft checks the exact source and records the
assembly that would follow from that input and the adopted
near-endpoint and endpoint-collar estimates.

The first retained coordinate would then cover its entire period,
with both of its original Fourier alternatives. Every later
retained coordinate would still be unselected on its old plateau.
This is not the complete open-word source or a knot statement.

## 1. Literal source and the single pending input

Fix an actual positive three/four word \(n_j=3+\epsilon_j\), with
\[
 m\ge3,\qquad \epsilon_1=\epsilon_2=1,\qquad
 h=m-1,\qquad k_4=\sum_{j=1}^m\epsilon_j .
 \tag{1}
\]
Use its original retained reference \(r_j=a_j+ic_j\), ordinary
colors \(\mathbf w=(w_L,w_R)\), markings and logarithmic lifts.
Put
\[
 P=[11/50,9/20],\qquad
 \mathcal P'=\prod_{j=2}^{h}(P+ic_j),\qquad
 H_0=c_1,\quad H_1=1/100,\quad \kappa_0=1/2500000 .
 \tag{2}
\]
The first44 actual-reference conditions, including the length-three
attached reference, are exactly those in the
[connected-right theorem](research_mixed_initial44_connected_right_contour.md).
In particular \(a_1<.350\), \(c_1<0\), and the second coordinate
has its actual negative height throughout.

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
Here \(q_N=e^{-2\pi i/N}\) and \(P_j=(q_N;q_N)_j\);
all finite functions in (3) have their original definitions.
The terminal transform already contains every terminal row, its
whole diagonal weight, both of its Fourier alternatives and its
ordinary-color dependence. No second terminal selection is made.
The original scalar and increasing-angle measure are
\[
 S_N=\kappa_N^{m+k_4}N^{m+k_4-1},\qquad
 S_N\,dz_1\cdots dz_h
   =\kappa_N^{m+k_4}N^{k_4}\prod_{j=1}^{h}(N\,dz_j),
 \qquad |\kappa_N|=1 .
 \tag{4}
\]
These are equation (13) of
[terminal contraction](research_mixed_reversed_cap_assembly.md);
no extra residue power of \(N\) is inserted.

Retain the original allocated phases and their constants:
\[
\begin{split}
 \Phi(\mathbf z)&=L_1(z_1)+\sum_{j=2}^{h}
                \phi_j(z_{j-1},z_j)+\Pi(z_h),\\
 M&=\Re\Phi(\mathbf r),\qquad \nabla\Phi(\mathbf r)=0,\\
 \Lambda(x_2)&=\Re\{L_1(r_1)+\phi_2(r_1,r_2)\}
                   +\Re\partial_2\phi_2(r_1,r_2)(x_2-a_2).
\end{split}
 \tag{5}
\]

**Pending input \(\mathrm{I}_{44}\).** A positive number
\(\gamma_I\), fixed before \(N\), must be proved such that for
every \(\tau>0\), both parities, and \(\sigma=0,1\),
\[
\begin{split}
 &|U_{1,N}(w_L,X)C_{1,N}(X,Y)
                    d_N(X)X^{-N\sigma}|\,|d_N(Y)|^{1/2}\\
 &\hspace{16mm}\le C_\tau N^{A_\tau}
                e^{N\{\Lambda(x_2)-\gamma_I+\tau\}},\\
 &X=e^{-2\pi ix},\quad 7/10\le x\le7/8,\qquad
   Y=e^{-2\pi i(x_2+ic_2)},\quad x_2\in P .
\end{split}
 \tag{6}
\]
Its required scope is the same actual reference family, the whole
real incoming-color interval and sufficiently small fixed ordinary
color disks at a prescribed allowance. The full finite conditional
polynomial, not just its critical exponential, must occur in (6).
The two in-progress source estimates are not substituted for (6)
until their complete product and its original calibration have
been checked.

## 2. The available remainder of the real first path

Choose a fixed collar width \(\rho>0\) from
[the periodic endpoint theorem](research_mixed_four_four_periodic_right_endpoint_collar.md),
shrinking it if necessary so that \(\rho<1/8\).
That theorem pays the literal full pair on \([1-\rho,1]\),
at both Fourier choices, with gap \(1/4000\):
\[
 |U_1C_1d_N(X)X^{-N\sigma}|\,|d_N(Y)|^{1/2}
       \le CN^A e^{N\{\Lambda(x_2)-1/4000\}}.
 \tag{7}
\]
It includes \(x=1\) by exact finite periodicity and polynomial
continuation, not by continuing a factorial asymptotic to its
divisor.

The [complete near-endpoint pair theorem](research_mixed_initial44_near_endpoint_complete_pair.md)
uses this same fixed \(\rho\) and gives on \([7/8,1-\rho]\)
\[
\begin{split}
 |U_1C_1d_N(X)X^{-N\sigma}|\,|d_N(Y)|^{1/2}
 \le C_\tau N^{A_\tau}\exp N\{&
 \Lambda(x_2)-\kappa_0(x_2-a_2)^2\\
 &-2\delta_R-1/400+\tau\},\\
 \delta_R&=\kappa_0(9/20-a_1)^2 .
\end{split}
 \tag{8}
\]
This estimate includes every conditional physical index before
any modulus is taken of the full conditional sum. No extra
conditional alias or unweighted contour is left to assemble.
Both (7) and (8) retain the complete cap, both original Fourier
upper alternatives, both parities and the outgoing halfweight.

Thus, **if** (6) holds, every real added segment
\([7/10,1]\) has the common pair gap
\[
                  \gamma_R=\min\{\gamma_I,1/400,1/4000\}>0 .
 \tag{9}
\]
All intervals and neighborhoods in this statement are fixed
before the level limit; no uniform bound as \(\rho\downarrow0\)
is needed.

Multiply these pair bounds by the remaining complete unselected
ordinary and terminal planes in equation (5) of
[the whole plateau theorem](research_mixed_full_unselected_plateau.md).
The first diagonal weight in (3) has been used in full.
The unused half of \(|d_N(X_2)|\) belongs to factor three
when \(h\ge3\), or directly to the terminal transform when \(h=2\).
Every later pair of halves restores the original integer diagonal
power. These identities hold at zeros and involve no division.
Original stationarity cancels the outgoing marginal in (5):
\[
 \partial_2\phi_2(r_1,r_2)+\partial_1\phi_3(r_2,r_3)=0
       \quad(h\ge3),\qquad
 \partial_2\phi_2(r_1,r_2)+\Pi'(r_2)=0\quad(h=2).
 \tag{10}
\]
All subsequent marginals cancel likewise. Consequently, conditional
on (6),
\[
\begin{split}
 |\mathscr J_{\sigma,N}|
 &\le C_{m,\tau}N^{A_{m,\tau}}
       e^{N\{M-\gamma_R-\mathcal Q_{\rm rem}(\mathbf x)+\tau\}},
      \qquad z_1\in[7/10,1],\quad \mathbf z'\in\mathcal P',\\
 \mathcal Q_{\rm rem}(\mathbf x)
 &=\kappa_0(x_2-a_2)^2
             +2\kappa_0\sum_{j=3}^{h}(x_j-a_j)^2 .
\end{split}
 \tag{11}
\]
For \(m=3\) the sum is empty; the terminal incidence supplies
exactly the remaining coordinate-two halfweight and quadratic.
The stronger quadratic in (8) can be dropped in this common bound.
Allocate one total tolerance among the fixed number of factors
and intersect their ordinary-color disks. Cauchy estimates apply
to the complete holomorphic source (3), never to a modulus
halfweight.

## 3. Additivity and preservation of the original coefficient

The adopted connected-right paths are
\[
 \mathcal G_\sigma:\quad
 0\longrightarrow1/10\longrightarrow1/10+iH_\sigma
 \longrightarrow1/2+iH_\sigma
 \longrightarrow1/2\longrightarrow7/10 .
 \tag{12}
\]
Append the real segment \([7/10,1]\), writing
\(\mathcal H_\sigma=\mathcal G_\sigma*[7/10,1]\).
The intermediate vertices \(7/8\) and \(1-\rho\) merely
partition that segment into its three source estimates.
Each of these paths starts at zero and ends at the real point one.
Set
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
 \tag{13}
\]
Path additivity, valid without (6), gives exactly
\[
 \mathcal H_N-\mathcal G_N
 =S_N\sum_{\sigma=0}^1
       \int_{[7/10,1]\times\mathcal P'}
                   \mathscr J_{\sigma,N}\,dz_1\cdots dz_h .
 \tag{14}
\]
The two first Fourier integrals remain separate even on their
common real segment.

The connected-right theorem already proves
\[
 |\mathcal G_N-\mathcal Z_N^P|
 \le C_{m,\tau}N^{A_{m,\tau}}e^{N(M-\gamma_G+\tau)},\qquad
 \gamma_G=\min\{\kappa_0(a_1-11/50)^2,\delta_R/2\}>0 ,
 \tag{15}
\]
where \(\mathcal Z_N^P\) is the original unselected plateau
integral. Under the pending input (6), integrate (11) in
(14) and retain the polynomial modulus of \(S_N\). Hence
\[
 |\mathcal H_N-\mathcal Z_N^P|
 \le C_{m,\tau}N^{A_{m,\tau}}e^{N(M-\gamma+\tau)},\qquad
 \gamma=\min\{\gamma_G,\gamma_R\}>0 .
 \tag{16}
\]

**Conditional conclusion.** If (6) is proved with its stated
source and color scope, then
\[
 \mathcal H_N(\mathbf w)=
 \kappa_N^{m+k_4}N^{-3/2}A_m(\mathbf w)
     e^{N\mathcal F_m(\mathbf w)}
                    \{1+O_{\rm hol}(N^{-1})\},\qquad A_m\ne0 .
 \tag{17}
\]
Here the action, leading coefficient, Gaussian branch, markings,
orientation and normalized ordinary-color jets are exactly those
of the original plateau theorem. Indeed choose the total allowance
in (16) below \(\gamma/8\) and then shrink the common disks so that
\(\Re\mathcal F_m>M-\gamma/8\) and \(A_m\) stays away from zero.
Division by the original nonzero leading term makes (16) an
exponentially small holomorphic relative error. Cauchy's formula
retains all fixed normalized jets on smaller disks. There is
no new saddle calculation or change to the power \(N^{-3/2}\).

## 4. Exact completion of the first retained period

The following identities require no estimate (6).
For fixed later coordinates and colors, (3) is a finite Laurent
polynomial in \(X_1=e^{-2\pi iz_1}\). It is therefore an entire
one-periodic function of \(z_1\). The original denominator
factorials \(P_j\) are nonzero constants; no interpolating
factorial is used in this assertion. Cauchy's theorem in the
\(z_1\)-plane shows, separately for each \(\sigma\),
\[
 \int_{\mathcal H_\sigma}\mathscr J_{\sigma,N}\,dz_1
       =\int_0^1\mathscr J_{\sigma,N}\,dx_1 .
 \tag{18}
\]
This is an equality of the whole exact functions, not a modulus
comparison with a different-height path.

The first-sector-zero integrand has \(X_1\)-band contained in
\([-N+1,2N-2]\): the cap and diagonal polynomial each have
degree at most \(N-1\), and the incoming band of \(C_1\)
is \([-N+1,0]\). The original torus root-average identity
therefore gives
\[
 \int_0^1\{\mathscr J_{0,N}+\mathscr J_{1,N}\}\,dx_1
   =\frac1N\sum_{j=0}^{N-1}
          \mathscr J_{0,N}(j/N,\mathbf z';\mathbf w).
 \tag{19}
\]
The only multiples of \(N\) in that band are \(0,N\);
the selected factor extracts the latter coefficient. The root
average in (19) uses \(\mathscr J_0\), not the sum of the two
sector values at the nodes. In particular there is no extra
factor two, even though \(X_1^{-N}=1\) at those nodes.
Also \(d_N(q_N^j)=P_j^{-1}\) there, exactly.

Combining (13), (18) and (19) gives the exact complete-first-source
representation
\[
 \mathcal H_N(\mathbf w)
  =\kappa_N^{m+k_4}N^{m+k_4-2}
      \int_{\mathcal P'}
       \sum_{j=0}^{N-1}
          \mathscr J_{0,N}(j/N,\mathbf z';\mathbf w)
                                      \,dz_2\cdots dz_h .
 \tag{20}
\]
The change from (4) is exactly the root-average factor \(1/N\).
At \(m=3\), the sole later retained coordinate is still present,
with its original terminal transform; (20) introduces no additional
conditional factor. The inherited increasing-angle measure makes
(18)--(20) consistent with the original positive residue measure.

Thus (17), if its single pending analytic input is supplied, would
hold for the original complete first retained period with all
later selections zero and all later targets on \(\mathcal P'\).
The terminal period was already complete before this step.
Later retained periods, their selected sectors and departures
from \(P\) remain excluded. No arbitrary short-filling stability,
ordinary closing or knot identification follows.

## Current source versions and draft status

| Available source | SHA-256 |
|---|---|
| research_mixed_initial44_connected_right_contour.md | cfda9bcc96bb0b0827df17f6bdcc0d7403841f5e6289cf54d80511e99925aa13 |
| research_mixed_initial44_near_endpoint_complete_pair.md | 4a481d134c93b8bb11bed2406253cec046f6e04a95339b1b48a8594469bc7712 |
| research_mixed_four_four_periodic_right_endpoint_collar.md | 91ed08bf7e2d04dabcd8e85bc3d3eac648bfdde9ae29a4d1bc7f6a137cbd39a4 |
| research_mixed_full_unselected_plateau.md | abd5dcddc9ed5057b6658bd8b7b60922540fd664c0c5c794135b19c1678c62a6 |
| research_mixed_reversed_cap_assembly.md | 79d44dfbcfe8c598783f27a49dea5bc716cc62e0a2c4762a238f3b2afffd244c |
| research_mixed_conditional_torus_composition.md | 8a25a25a95bf11767c4f305317a6fab9a9c17724ae0e24a36014b5fd8ec4f693 |

The available source implications above were read and their hashes
checked. Input (6) has no proved source binding in this draft.
This file is deliberately unfrozen and unadopted. Its conditional
asymptotic must not be recorded as an established first-period result.
No mathematical numerical evaluation, saved-value arithmetic, import,
test, compilation or frozen-source edit was used.
