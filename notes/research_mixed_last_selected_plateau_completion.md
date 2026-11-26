# Adding the last retained Fourier selection to an open-chain plateau

Research deduction, 6 November 2026. This note explains how the selected
terminal estimate is joined to the rest of the original open chain. It
extends the previously treated plateau region by allowing a selection at
its last retained coordinate. The integral outside the plateau, and the
other boundary selections, remain outside this result.

## 1. The sector being added

Fix a word of types
\[
 n_j=3+\epsilon_j,\qquad \epsilon_j\in\{0,1\},\qquad
 1\le j\le m,\qquad m\ge3,
\]
whose last three types satisfy
\[
             (n_{m-2},n_{m-1},n_m)=(4,4,3+\epsilon_m).
\tag{1}
\]
Put \(h=m-1\), \(k_4=\sum_j\epsilon_j\), and
\(P=[.22,.45]\). Let \(r_j=a_j+ic_j\), \(1\le j\le h\),
be the retained coordinates of the original open critical point.
The source, branches and reference are those of the
[unselected plateau theorem](research_mixed_full_unselected_plateau.md).

The set of interior positions used in the
[interior-selection theorem](research_mixed_interior_selected_plateau.md) is
\[
 I_m=\{j:6\le j\le m-5\},\qquad
 I_m^{(4)}=\{j\in I_m:\epsilon_j=1\}.
\tag{2}
\]
These sets may be empty. For every \(S\subseteq I_m^{(4)}\),
we add the sector with selected set \(S^+=S\cup\{h\}\).
Its integration variables have the fixed heights
\[
 z_j=x_j+i\widetilde c_j,\qquad x_j\in P,
 \qquad
 \widetilde c_j=
 \begin{cases}
  1/100,&j=h,\\
  7/500,&j\in S,\\
  c_j,&j\notin S^+.
 \end{cases}
\tag{3}
\]
In particular the incoming coordinate \(h-1\) of the terminal
pair is unselected. The two selected heights have different purposes:
\(7/500\) is the height in the existing interior theorem;
\(1/100\) is the height in the new terminal theorem.

With \(X_j=e^{-2\pi iz_j}\), the literal sector integrand is
\[
\begin{split}
 \mathscr J_{S^+,N}={}&
 U_{\epsilon_1,N}(w_L,X_1)
 \prod_{j=2}^{h}C_{\epsilon_j,N}(X_{j-1},X_j)
 \mathcal V_{\epsilon_m,N}(w_R,X_h)\\
 &\quad\cdot\prod_{j=1}^{h}
     d_N(X_j)^{\epsilon_j}X_j^{-N\mathbf1_{j\in S^+}}.
\end{split}
\tag{4}
\]
These are the original finite functions. The terminal factor already
contains its private finite sum and its own Fourier alternatives.
The selection at \(h\) in (4) belongs to the adjacent retained
coordinate, so it is inserted exactly once.

Define the additional contribution by integrating (4) over \(P^h\),
summing over \(S\subseteq I_m^{(4)}\), and multiplying by the
original scalar \(\kappa_N^{m+k_4}N^{m+k_4-1}\), where
\(|\kappa_N|=1\). Denote it by \(E_N^{\mathrm{last}}(w_L,w_R)\).
Let
\[
 Z_N^{\mathrm{int,last}}
   =Z_N^{\mathrm{int}}+E_N^{\mathrm{last}},
\tag{5}
\]
where \(Z_N^{\mathrm{int}}\) is the earlier plateau sum with only
interior selections. Formula (5) defines a sum of specified contour
sectors. It is not an assertion that these sectors exhaust the original
constant term. All regions and heights are fixed independently of the
ordinary colors.

## 2. The two-factor estimate uses exactly the missing incidences

The [complete terminal-kernel theorem](research_mixed_terminal_uniform_kernel_completion.md)
applies to the last ordinary factor and terminal transform in (4).
Its allocated modulus is
\[
 \left|C_{1,N}(X_{h-1},X_h)
       \mathcal V_{\epsilon_m,N}(w_R,X_h)
       d_N(X_h)X_h^{-N}\right|
       |d_N(X_{h-1})|^{1/2}.
\tag{6}
\]
Assumption (1) supplies the incoming type-four reference and the
ordinary type-four factor. The actual-reference theorem identifies
this suffix with the canonical \(K_4\) family, also when \(m=3\).
The real variables \(x_{h-1},x_h\) remain independent throughout
\(P^2\).

Write the local action and its incoming derivative as
\(M_*(r_{h-1})\) and \(p_*(r_{h-1})\). For every sufficiently
small fixed \(\eta>0\), (6) has upper rate
\[
 \Re\{M_*(r_{h-1})+p_*(r_{h-1})(z_{h-1}-r_{h-1})\}
                         -\delta_T+\eta,
 \qquad \delta_T=1/2600.
\tag{7}
\]
There is a polynomial prefactor, and the estimate holds on a fixed
small complex disk of ordinary right colors. The terminal
[real-color extension](research_mixed_terminal_profile_real_color_lift.md)
gives the same upper rate for every \(w_R\in[-2,2]\). It does
not require an angular loss for every terminal profile.

Here is the exact matching of (7) with the adjoining factors. Let
\(\phi_j\) be the allocated ordinary phases, and let \(L,\Pi\)
be the allocated endpoint phases in the unselected plateau theorem.
At the original reference,
\[
\begin{split}
 M_*(r_{h-1})
   &=\phi_h(r_{h-1},r_h)+\Pi(r_h),\\
 p_*(r_{h-1})
   &=\partial_1\phi_h(r_{h-1},r_h),\\
 \partial_2\phi_h(r_{h-1},r_h)+\Pi'(r_h)&=0.
\end{split}
\tag{8}
\]
The last equation is the original retained-coordinate critical
equation at \(h\). Thus (7) replaces exactly the sum of the two
old complex affine tangents, with an additional strict loss. It
retains the incoming affine term in full.

Every interior selection \(k\in S\) is incident to ordinary
factors \(k,k+1\). Their indices are at most \(m-4=h-3\),
so none is the factor \(h\) already used in (6). The
interior-selection theorem bounds each such factor with its original
allocated tangent and loss \(1/200\). It covers both endpoints
selected as well as just one selected endpoint. Every remaining
ordinary factor has both coordinates unselected and uses its
completed unselected tangent bound. The first cap is also unselected.

At coordinate \(h\), (6) consumes the full selected weight.
At coordinate \(h-1\), (6) consumes one half of its unselected
weight. The adjoining ordinary factor supplies the other half; if
\(m=3\), the first cap supplies it instead. Every other retained
weight is split between its two original incidences as before.
No weight or ordinary factor is counted twice.

## 3. Exponential suppression and the nonzero leading coefficient

Put
\[
 \Phi(\mathbf z)=L(z_1)+
      \sum_{j=2}^{h}\phi_j(z_{j-1},z_j)+\Pi(z_h),
 \qquad M=\Re\Phi(\mathbf r).
\tag{9}
\]
The original critical equations give \(\nabla\Phi(\mathbf r)=0\).
Consequently the sum of all the allocated complex affine tangents
is exactly \(\Phi(\mathbf r)\), including at the changed heights
(3). This is why it is necessary to retain the incoming term in (7).

**Theorem 1.** Under (1), there are constants and polynomial
prefactors, depending on the fixed word, such that
\[
 |E_N^{\mathrm{last}}(w_L,w_R)|
       \le C N^A e^{N(M-1/5200)}
\tag{10}
\]
on fixed sufficiently small complex neighborhoods of \((-2,-2)\).
The same bound holds for all real \((w_L,w_R)\in[-2,2]^2\).
It holds through both level parities. Every fixed ordinary-color
derivative has (10) on smaller complex neighborhoods, with its own
constant and polynomial prefactor.

*Proof.* Multiply the complete finite-factor bounds in Section 2.
There are finitely many factors for a fixed word. Choose the sum of
their rate tolerances smaller than \(\delta_T/2\). Equations
(8)--(9) cancel every affine displacement. The terminal pair gives
loss \(\delta_T\); the additional interior losses and all
nonpositive unselected quadratic terms may be discarded. The result
is (10) for each integrand, with a common polynomial prefactor.
The volume of \(P^h\), the finite number of selected sets, and the
original scalar only change that prefactor.

For real colors, use the terminal real-color extension in (7).
The [first-cap real-color estimate](research_mixed_endpoint_real_color_decay.md)
bounds the other endpoint by its unchanged complete-color tangent,
even after its favorable angular loss is discarded. All intervening
factors are independent of ordinary colors. The same multiplication
therefore proves (10) on the whole real color square. On complex
color disks, use the local terminal and cap bounds with the same
total tolerance. Cauchy's formula proves the fixed-derivative
statement on smaller disks. No modulus halfweight is differentiated.
\(\square\)

All factors containing an ordinary color are polynomials of degree
at most \(N-1\) in that color. Integrating over the fixed regions
preserves this fact. Both \(E_N^{\mathrm{last}}\) and
\(Z_N^{\mathrm{int,last}}\) are therefore entire polynomials of
separate ordinary degrees at most \(N-1\).

Let \(\mathcal W(w_L,w_R)\) and \(A(w_L,w_R)\) be the
original action and nonzero amplitude of the unselected plateau.
Shrinking the color disks so that
\(\Re\mathcal W>M-1/10400\), (10) is exponentially smaller
than its leading term. The previously proved expansion of
\(Z_N^{\mathrm{int}}\) consequently gives
\[
 Z_N^{\mathrm{int,last}}(w_L,w_R)
  =\kappa_N^{m+k_4}N^{-3/2}A(w_L,w_R)
       e^{N\mathcal W(w_L,w_R)}(1+O(N^{-1})),
 \qquad A(-2,-2)\ne0.
\tag{11}
\]
The amplitude, logarithmic branches and normalization in (11) have
not changed. The extra sectors cannot cancel this leading term.

## 4. The boundary estimate survives the enlarged sector

Set
\(Q_N^{\mathrm{int,last}}(\boldsymbol\theta)
 =Z_N^{\mathrm{int,last}}(-2\cos\theta_L,-2\cos\theta_R)\).
The [central-region boundary theorem](research_mixed_central_region_boundary_colors.md)
already supplies, for every sufficiently small fixed \(\rho>0\),
a gap \(\delta_\rho>0\) for \(Z_N^{\mathrm{int}}\) whenever
\(\max_j|\theta_j|\ge\rho\) on \([-\pi,\pi]^2\).
Equation (10) and the triangle inequality therefore give
\[
 |Q_N^{\mathrm{int,last}}(\boldsymbol\theta)|
 \le C N^A\exp\{N(M-\min(\delta_\rho,1/5200))\}
 \quad\text{if }\max_j|\theta_j|\ge\rho.
\tag{12}
\]
This argument uses a uniform strict gap for the new sectors; it
does not manufacture a boundary-angle loss from their positivity.

The polynomial degree bound, the unchanged local expansion (11),
and (12) satisfy Lemma 1 of the
[open-source stability reduction](research_mixed_open_source_stability_reduction.md).
Thus there are \(c,B,t>0\) and a polynomial prefactor such that
\[
 |Q_N^{\mathrm{int,last}}(\mathbf x+i\mathbf y)|
 \le C N^A\exp N\left\{
 M-c\sum_{j=L,R}(1-\cos x_j)+B\|\mathbf y\|_2^2\right\},
 \qquad |y_j|\le t.
\tag{13}
\]
The strictly negative real angular Hessian is the same one already
proved from the original endpoint marginals. No new Hessian or
almost-invariant-vector assumption is needed for (13).

## 5. What remains for a whole-source statement

This deduction includes the last retained selection together with
arbitrarily many allowed interior selections. It leaves the other
boundary selections, the integrals outside \(P^h\), and their
joining regions untreated. It also requires the suffix (1), so it
does not cover an incoming type-three reference or two selected
coordinates entering the terminal window. Estimates (11)--(13)
belong to the explicitly defined polynomial (5).

To replace that polynomial by the entire original open source still
requires a bound for its full complement near the complete colors
and over the real outside-color period. Even a whole-source theorem
for these positive mixed words would need the marked geometric
boundary deformation and an extension to arbitrary fixed short
fillings before the per-template finite-exception deduction applies.
