# Two complete incoming periods at a 343 boundary

Private research deduction, 10 November 2026. For every fixed actual
positive three/four open word beginning \(343\), of length at least
five, both first retained coordinates can be integrated over their
entire periods. This includes both alternatives of the second
coordinate's type-four weight. On a fixed local interval of the
third coordinate, replacing the old two-coordinate unselected
plateau by this complete contraction changes the restricted
polynomial by an exponentially small term. Its original nonzero
leading coefficient is consequently unchanged.

This enlarges the original plateau in two complete coordinates,
using [the first-period patch](research_mixed_complete_first_period_boundary_patch.md)
as an input.
It is not a new local saddle theorem. The complete next-three
transfer is an established input; the additional assertion here is
the exact two-period patch, its comparison with the old plateau,
and its calibrated attachment to an arbitrary full middle.
The third coordinate's remote sectors remain outside this result.

## 1. Exact second contraction and the actual reference scope

Fix an actual complete open word of length \(m\ge5\), with
\[
 \epsilon_1=0,\qquad\epsilon_2=1,\qquad\epsilon_3=0,\qquad
 n_j=3+\epsilon_j,\qquad
 k_4=\sum_{j=1}^m\epsilon_j,\qquad h=m-1 .
\tag{1}
\]
All remaining types, original markings and reference coordinates
are unchanged. Write \(D=N-1\), \(r=e^{-2\pi i/N}\),
\(P_a=(r;r)_a\), and
\[
 W_{\epsilon,N}(X)=\{d_N(X)(1+X^{-N})\}^{\epsilon}.
\tag{2}
\]
Let \(f_{34,N}\) be the literal complete polynomial of the
first-period patch. Define
\[
\begin{split}
 F_{343,N}(w,Z)
 &=N\operatorname{CT}_Y
       [f_{34,N}(w,Y)d_N(Y)(1+Y^{-N})C_{0,N}(Y,Z)]\\
 &=N[Y^0](f_{34,N}d_NC_{0,N})
           +N[Y^N](f_{34,N}d_NC_{0,N})\\
 &=\sum_{a=0}^{D}\frac{f_{34,N}(w,r^a)}{P_a}
                                      C_{0,N}(r^a,Z).
\end{split}
\tag{3}
\]
The exact band argument in
[literal transfer](research_mixed_literal_transfer_norm_obstruction.md),
equations (3)--(5), proves all three equalities. In particular the
two Fourier coefficients are retained, not identified separately
by sampling. Equivalently,
\[
 F_{343,N}
 =N^2\operatorname{CT}_{X_1,X_2}
 [U_{0,N}(w,X_1)C_{1,N}(X_1,X_2)
          W_{1,N}(X_2)C_{0,N}(X_2,Z)] .
\tag{4}
\]
It has degree at most \(D\) in \(w,Z\). No final Gram factor
or ordinary right cap belongs to (3).

In the exact terminal-contracted chart, the whole original source is
\[
\begin{split}
 \mathcal Z_N
 ={}&\kappa_N^{m+k_4}N^{m+k_4-3}
   \operatorname{CT}_{X_3,\ldots,X_h}
       \left[
       F_{343,N}(w_L,X_3)
       \prod_{j=4}^{h}C_{\epsilon_j,N}(X_{j-1},X_j)\right.\\
 &\left.\hspace{24mm}\cdot
       \mathcal V_{\epsilon_m,N}(w_R,X_h)
       \prod_{j=3}^{h}W_{\epsilon_j,N}(X_j)
       \right].
\end{split}
\tag{5}
\]
Here \(W_{\epsilon_3,N}=1\). Thus the full old second weight
has been consumed inside (3); it is neither omitted nor left
outside a second time. Relative to the old terminal-contracted
scalar, two factors \(N\) have been absorbed in (4).
Before terminal contraction, the corresponding scalar is
\(\kappa_N^{m+k_4}N^{m+k_4-2}\), with the product through
\(j=m\) and the original factor
\(\mathcal H_N(w_R,X_m^{-1})\).

These are identities of finite Laurent polynomials. Perform the
first two constant terms on independent circles before choosing
a contour in the remaining variables. This does not identify the
new chart with a restricted piece of an old height graph depending
on the first two real coordinates.

Set
\[
 y_*=t_2^*,\qquad z_*=t_3^*,\qquad b_*=s_4^*
\tag{6}
\]
at the actual reference. The
[correlated-height theorem](research_mixed_cap_343_correlated_height_bounds.md),
Section 1, identifies the first three vertices with the original
cap-initialized \(343\) half-chain at \(b_*\).
Since \(m\ge5\), vertex four is ordinary and
\(b_*\in O_{n_4}\subset P_{n_4}\).
Section 3 gives the additional actual-word refinement used by the
complete transfer theorem. Every fixed positive three/four
continuation after the first three letters is permitted.

The [complete transfer bidisk theorem](research_mixed_next_transfer_complex_neighborhood.md)
therefore applies to exactly (3), near \((-2,z_*)\).
Its scope is every such actual word; it does not assert the same
source estimate at all independent points of a containing
pre-Gram parameter disk. Length four, a terminal third vertex,
and initial \(344\) are not supplied by that theorem.

## 2. An exponential comparison with the complete old plateau

Let \(P=[11/50,9/20]\), \(c_j=\Im t_j^*\), and
\(X_j=e^{-2\pi i(x_j+ic_j)}\). Define the exact two-coordinate
unselected plateau message
\[
\begin{split}
 I_{PP,N}(w,z)
 =N^2\int_{P^2}
 U_{0,N}(w,X_1)C_{1,N}(X_1,X_2)d_N(X_2)
                           C_{0,N}(X_2,e^{-2\pi iz})\,dx_1dx_2 .
\end{split}
\tag{7}
\]
This is the word \(343\) instance of equation (8) of
[retained-prefix plateau](research_mixed_retained_prefix_unselected_plateau.md).
All its heights and endpoints stay fixed as \(w,z\) vary.

Write \(P_3(w,z)=\mathcal P_0^+(w,z)\) for the original action of
[the exact next local source](research_mixed_three_four_next_local_source.md).
The subscript here denotes a prefix of length three, not a
new crossing action. Its exact calibration at the actual reference is
\[
 P_3(-2,z_*)=H_{343}(b_*)-G(z_*,b_*)-g(z_*).
\tag{8}
\]
In particular the last own-three correction \(-g(z_*)\) remains.

**Lemma 1.** There is a fixed complex bidisk about \((-2,z_*)\)
and a number \(\delta>0\) such that
\[
 \left|e^{-NP_3(w,z)}
   \{F_{343,N}(w,e^{-2\pi iz})-I_{PP,N}(w,z)\}\right|
        \le C N^A e^{-\delta N}.
\tag{9}
\]
All fixed normalized mixed derivatives satisfy an exponential
bound on smaller bidisks.

*Proof.* Choose the same fixed local segment
\(J_*=[y_*-\varepsilon,y_*+\varepsilon]\) as in the next-source
theorem, shrinking it inside \(P+ic_2\) if necessary. Its exact
local integral is
\[
 I_{\mathrm{loc},N}
   =N\int_{J_*} f_{34,N}(w,e^{-2\pi iy})d_N(e^{-2\pi iy})
                C_{0,N}(e^{-2\pi iy},e^{-2\pi iz})\,dy .
\tag{10}
\]
Equations (8)--(9) in the proof of the complete transfer bidisk
theorem retain the exact identity
\[
 F_{343,N}-I_{\mathrm{loc},N}=E_N^-+R_N^+ .
\tag{11}
\]
The [left remainder](research_mixed_next_left_remainder_complex_extension.md)
and [incoming-color right remainder](research_mixed_next_incoming_color_outer_upper_bound.md),
Corollary 2, bound the two terms on a fixed bidisk with positive
normalized exponential gaps. The algebraic local Gaussian error
is not included in either term. A smaller fixed segment in (10)
is allowed: the removed ends lie inside the proved local packet
with a fixed horizontal phase gap and are absorbed into \(E_N^-\);
equation (11) then denotes that exact adjusted remainder.

Let \(I_{P,N}(w,y)\) be the exact first plateau in equation (7) of
the first-period patch. By ordinary integration of finite sources,
\[
\begin{split}
 I_{PP,N}-I_{\mathrm{loc},N}
 ={}&N\int_{(P+ic_2)\setminus J_*}
                 I_{P,N}(w,y)d_N(Y)C_{0,N}(Y,Z)\,dy\\
 &+N\int_{J_*}
       \{I_{P,N}(w,y)-f_{34,N}(w,Y)\}
                        d_N(Y)C_{0,N}(Y,Z)\,dy ,
 \qquad Y=e^{-2\pi iy}.
\end{split}
\tag{12}
\]
The first term is the exact double plateau integral over a set
where \(|x_2-\Re y_*|\ge\varepsilon\). Equations (21)--(22) of
retained-prefix plateau bound its complete integrand by its
original action minus a fixed positive quadratic loss. Their
fixed complex-neighborhood extension applies to \(w,z\), before
integration.

For the second term, equation (8) of the first-period patch
bounds \(I_{P,N}-f_{34,N}\) with a fixed exponential loss relative
to \(\mathcal P_{34}(w,y)\) on a neighborhood of \(J_*\).
The original complete conditional packet and the actual Fourier
weight in the next local-source theorem give, on this same
neighborhood, their original phases
\(\psi_0(y,z)\) and \(-g(y)\).
At the complete base their sum with \(\mathcal P_{34}\) is
\[
 \varphi_0(y;-2,z_*)
       =\mathcal P_{34}(-2,y)-g(y)+\psi_0(y,z_*).
\]
It is strictly horizontally concave on \(J_*\), has critical
point \(y_*\), and has value \(P_3(-2,z_*)\) there, by that
theorem's Schur lemma. Thus the second term retains the
first-period gap. Fixed sufficiently small \(w,z\) neighborhoods
use only an arbitrarily small fraction of it.

Combine (11)--(12). There are finitely many positive gaps;
polynomial factors can be absorbed by decreasing their minimum.
This proves (9). Fixed-radius Cauchy estimates for its normalized
holomorphic expression prove the derivative assertion.
No conclusion here is drawn merely from two matching
\(O(N^{-1})\) leading asymptotics. \(\square\)

## 3. A calibrated supporting plane at the new first coordinate

There is no Fourier halfweight at \(z=t_3\), since its own type
is three. The appropriate left boundary phase is exactly
\[
                         L_{343}(z)=P_3(-2,z).
\tag{13}
\]
Here is a direct verification of its curvature and marginal.
Before eliminating the first six variables the phase is
\[
\begin{split}
 \mathcal F={}&E(s_1,u)+V_0(s_1,t_1)+G(t_1,s_2)
       +V_1(s_2,t_2)+G(t_2,s_3)+V_0(s_3,z)-g(z).
\end{split}
\tag{14}
\]
Its stationary value is (13), with (8)'s constant. In the
notation of the original
[open Hessian proof](research_mixed_open_word_hessian.md), its
negative-real Hessian is that of
\[
\begin{split}
 B(s_1,u)+W(s_1,t_1)
  +V(t_1,s_2)+V(s_2,t_2)+V(t_2,s_3)+V(s_3,z)
                                  -J(s_2)-J(t_2).
\end{split}
\tag{15}
\]
The difference between (14) and (15) is an imaginary polynomial
with real coefficients; its complex Hessian has zero Hermitian
real part. All individual terms and constants in (14) are the
original primitives.

On \(u\in U,s_1\in E\), with all remaining variables in \(Q\),
the same source gives
\[
             -\Re\mathcal F''\succ\mu I_7,\qquad
                                  \mu=6\pi/49 .
\tag{16}
\]
Indeed \(B\) covers its two variables, \(W\) supplies the first
attached leg, the four pair forms cover all subsequent legs,
and the two extra own-four terms have nonnegative negative-real
Hessian. The original reference is strictly inside this product.
The complex Schur complement in the six eliminated variables
therefore satisfies
\[
                         -\Re L_{343}''(z)>\mu
\tag{17}
\]
on a fixed smaller neighborhood of \(z_*\).
For clarity, if \(H=-\mathcal F''\) and
\(\xi=(-H_{vv}^{-1}H_{vz},1)^T\), then
\(H\xi=(0,S)^T\) and
\(\Re S=\xi^*(\Re H)\xi\ge\mu\|\xi\|^2\).
No Schur complement of entrywise real parts is substituted.

Choose a nondegenerate closed interval
\[
 J_3=[\Re z_*-\rho_3,\Re z_*+\rho_3]\Subset P
\tag{18}
\]
inside this neighborhood at height \(c_3\). Then
\[
 \Re L_{343}(x+ic_3)
 \le\Re L_{343}(z_*)+\Re L_{343}'(z_*)(x-\Re z_*)
                              -\frac{\mu}{2}(x-\Re z_*)^2 .
\tag{19}
\]
The exact remaining marginal is
\[
 L_{343}'(z_*)=g'(s_3^*+z_*)-g'(z_*),\qquad
 L_{343}'(z_*)+\partial_1\phi_4(z_*,t_4^*)=0 .
\tag{20}
\]
This follows directly from (14) and the original stationarity
at \(t_3\). In particular there is no own-four halfweight left
at the new boundary and no missing \(-g'(z_*)\).

The complete transfer packet and continuity in the incoming
ordinary color now prove, for any \(\eta>0\), on a sufficiently
small fixed \(w\)-disk,
\[
\begin{split}
 |F_{343,N}(w,e^{-2\pi i(x+ic_3)})|
 \le C_\eta N^{A_\eta}
 \exp N\{&\Re L_{343}(z_*)
        +\Re L_{343}'(z_*)(x-\Re z_*)\\
        &-\tfrac{\mu}{2}(x-\Re z_*)^2+\eta\},
                    \qquad x\in J_3 .
\end{split}
\tag{21}
\]
This is a complete finite-source bound on the local first
remaining interval, not a statement about all of its real period.

## 4. A larger restricted polynomial with the same coefficient

Let \(\mathcal Z_N^P\) be the original full unselected plateau
polynomial, and define
\[
 R_N(\mathbf z;w_R)=
     \prod_{j=4}^{h}C_{\epsilon_j,N}(X_{j-1},X_j)
       \mathcal V_{\epsilon_m,N}(w_R,X_h)
       \prod_{j=3}^{h}d_N(X_j)^{\epsilon_j},
 \qquad z_j=x_j+ic_j .
\tag{22}
\]
Set
\[
\begin{split}
 \mathcal Z_N^{P,343}
 =\mathcal Z_N^P
   +\kappa_N^{m+k_4}N^{m+k_4-3}
     \int_{J_3\times P^{h-3}}
        \{F_{343,N}(w_L,X_3)-I_{PP,N}(w_L,z_3)\}
                         R_N(\mathbf z;w_R)\,d\mathbf x .
\end{split}
\tag{23}
\]
This is an exact restricted polynomial in the original ordinary
colors. On \(x_3\in J_3\), its first two integrations are the
complete constant term (4), including the selected second
alternative. On the complement of \(J_3\), the old unselected
plateau remains. The old first two plateau integrals are
\(I_{PP,N}/N^2\), explaining exactly the scalar in (23).
Every domain and contour is fixed independently of the ordinary
colors.

**Theorem 3.** On sufficiently small fixed ordinary-color disks,
\[
 \mathcal Z_N^{P,343}(w_L,w_R)
 =\kappa_N^{m+k_4}N^{-3/2}
     A_m(w_L,w_R)e^{N\mathcal W_m(w_L,w_R)}
                          (1+O_{\rm hol}(N^{-1})),
\tag{24}
\]
where \(A_m\ne0,\mathcal W_m\), and all Gaussian branches are
exactly those of the original
[full unselected plateau](research_mixed_full_unselected_plateau.md).
Every fixed normalized mixed ordinary derivative has the
corresponding estimate.

*Proof.* Lemma 1 gives a fixed normalized exponential loss for
the difference in (23). Apply (19) to its prefix action, and
the original complete unselected supporting planes to every
remaining conditional factor and terminal transform.
Their complex linear terms cancel by (20) and the other
original stationary equations. Their constants sum to the
original complete value \(M_{\rm open}\); (8) retains exactly
the last own-three correction needed for that equality.
All quadratic losses can be discarded. With one aggregate
source tolerance smaller than a fixed fraction of Lemma 1's
gap, the added integral has rate strictly less than
\(M_{\rm open}\).

Shrink the ordinary disks so that the real part of
\(\mathcal W_m\) differs from its complete value by less than
another fixed fraction of this gap. The added term is then
exponentially small relative to the original nonzero plateau
packet. This proves (24), with the same coefficient, rather
than a newly chosen symbol. The exact finite contractions
preserve degree at most \(D\) in each free ordinary color.
All normalized expressions are holomorphic on fixed
neighborhoods; Cauchy's formula gives the fixed derivative
claims on smaller disks. Both original parity normalizations
are unchanged. \(\square\)

## 5. Compatible propagation through an arbitrary full middle

At safe cuts beyond the first three vertices, retain the protected
unselected \(P\)-triples of
[clean-closing completion](research_mixed_clean_closing_edges_completion.md),
and let \(F=[p+1,q-2]\) have its whole original alphabet.
Take \(x_3\in J_3\) at height \(c_3\), and
\(x_4,\ldots,x_{p-1}\) independently unselected in \(P\)
at their actual heights. The new literal left modulus is
\[
 L_N^{343}
 =|F_{343,N}(w_L,X_3)|
       \prod_{j=4}^{p-1}|C_{\epsilon_j,N}|
       \prod_{j=3}^{p-2}|d_N(X_j)|^{\epsilon_j}
                       |d_N(X_{p-1})|^{\epsilon_{p-1}/2}.
\tag{25}
\]
Its calibrated rate satisfies
\[
 G_{L,N}^{343}
 \le-\frac{\mu}{2}(x_3-\Re z_*)^2
     -\kappa_*\sum_{j=4}^{p-1}(x_j-\Re t_j^*)^2
                   +\eta+O_m(\log N/N),
 \qquad \kappa_*=1/2500000 .
\tag{26}
\]
This is (21) plus the complete ordinary planes, with the
joining tangent canceled by (20).

For any compatible right state in
[completed boundary-state propagation](research_mixed_completed_boundary_state_propagation.md),
its exact clean-closing cancellation gives
\[
 |\mathscr J_{\sigma,N}^{343}|
 \le C_{\eta,m}N^{A_{\eta,m}}
 e^{N\{M_{\rm open}+\eta-\Delta_R-K_R
                          -\kappa\sum_{i\in F}p_i\}},
                 \qquad\kappa=1/20000 .
\tag{27}
\]
The terminal-contracted and uncontracted charts retain their
separate scalars from Section 1 and the original right-source
domains. All synthetic closing edges and middle charges lie
beyond the changed prefix and are unchanged.

In the contracted chart, active selected-suffix sectors or
selected/nonplateau free sectors have the same gap \(1/40000\)
after tolerances and polynomial factors. Their disjoint regions
may be added to (23) without changing (24). The neutral plateau
part already present in (23) is not added twice. No union of
different terminal charts is asserted.

## 6. The exact next gate

This theorem removes both original early coordinates, not just
their local critical variables. It adds the entire second
type-four selected sector and the whole first and second periods
on a nonempty third-coordinate interval.

The first remaining coordinate is now \(X_3\), of own type
three. Its exact next operation, if another coordinate is
contracted, is
\[
 F_{343(3+\beta),N}(w,Z)
   =N\operatorname{CT}_X
       [F_{343,N}(w,X)C_{\beta,N}(X,Z)]
   =\sum_{a<N}F_{343,N}(w,r^a)C_{\beta,N}(r^a,Z).
\tag{28}
\]
There is no old-four weight in (28). The proved packet near
\(X=e^{-2\pi iz_*}\) does not bound its entire \(N\)-node
observation or all of its complex contour. A new calibrated
complement estimate for (28), retaining its actual following
reference, is still required.

For an initial \(344\), the exact formula (3) instead uses
\(C_{1,N}\). The next local-source theorem supplies its nonzero
local integral but does not pay the two full outer coefficients.
Nothing here changes that missing global comparison. Length-four
\(343\) prefixes are also outside the complete transfer theorem's
actual-word refinement.

The completed ordinary two-boundary \(343\) kernel is a different
observation: it closes the third vertex with an ordinary terminal
factor. It is not substituted for (3) or (28), and no inverse
ordinary-boundary transform is assumed to preserve a local
packet. The actual reference and the original remaining
boundary conditions are retained throughout.

The construction removes an additional whole coordinate relative
to the first-period mechanism, but remains a restricted
original-source theorem. It proves no
whole arbitrary mixed word, arbitrary short-filling stability,
knot identity or finite-exception result.

## Frozen direct source bindings

| Source | SHA-256 |
|---|---|
| research_mixed_complete_first_period_boundary_patch.md | 2469feb7027078f160c78a268599793530b68ae7b79e4aae12a0855a423e613d |
| research_mixed_next_transfer_complex_neighborhood.md | 3baac5dfce1f55588166e519b5408f6d374a37ef6c3ca3b3b80731e73118f6fe |
| research_mixed_three_four_next_local_source.md | f75fe4196fed3561381bef59bf446f00ba428101dab62d61990c91e0bdf9c696 |
| research_mixed_next_left_remainder_complex_extension.md | fbdc20aba05f2895e1fada626ff6ea8f26b7c8e6300a76fd6c51bb16b9c6f092 |
| research_mixed_next_incoming_color_outer_upper_bound.md | 5bf182877bb6905b67d68f3aafb57ec5f015b57467a9b1fb7fbff2cff2108c49 |
| research_mixed_cap_343_correlated_height_bounds.md | 47dc786c39ec848d2aa6add06eb231727786ddce9fd848b2053cd81afa491e2e |
| research_mixed_retained_prefix_unselected_plateau.md | 4f8be2ee4fd0aceda28ad4d96bb4b57d864765438183563c34db070823d6d72b |
| research_mixed_open_word_hessian.md | 21556711a3ac410ce7d3e4dda0d3a6395cd7ee2a69993d82f5f8325c6e7dad23 |
| research_mixed_full_unselected_plateau.md | abd5dcddc9ed5057b6658bd8b7b60922540fd664c0c5c794135b19c1678c62a6 |
| research_mixed_clean_closing_edges_completion.md | cc5b75d521fe648ab5aa0974e162de02b14fb814fc628635a1126349df5dfca9 |
| research_mixed_completed_boundary_state_propagation.md | cc7b2fc0db168d00e2b75b54ec3ff51496f178e819e4e5c8d5c6b53af563cb48 |
| research_mixed_literal_transfer_norm_obstruction.md | e9ce5a518439ed23b94c70eb548470ecbf9abfa5bd7c880f6828ed594a3fe0a3 |

The original source proofs and domains were read directly.
No mathematical numerical evaluation, saved-value arithmetic,
import, compilation, test or frozen-source edit was used.

