# The actual Fourier-ended source reduces to two finite boundary costs

Research deduction, 7 November 2026. The full-period occupation argument
does apply to the safe ordinary middle of an actual Fourier-ended
prefix. Its reference need not be cyclic. The new endpoint inclusion
supplies the missing reference geometry, while a separate exact
polynomial supplies the literal Fourier boundary source. These are
different statements: the inclusion does not pay that polynomial's
calibrated boundary cost.

This note gives the resulting source reduction. It introduces no
numerical test, new root search, whole-source sign, or Fourier-period
norm estimate.

## 1. The exact Fourier cap to place at the right cut

Let a positive three/four word have length \(m\ge2\), flags
\(\epsilon_1,\ldots,\epsilon_m\), and \(\epsilon_m=1\).
Put \(k=\sum_j\epsilon_j\), \(h=m-1\), and retain the
original conventions
\[
 r=e^{-2\pi i/N},\quad P_a=(r;r)_a,\quad
 W_{\alpha,N}(X)=\{d_N(X)(1+X^{-N})\}^{\alpha},
 \qquad Y=e^{2\pi iy}.
 \tag{1}
\]
The original Fourier basis from
[exact wire contraction](research_mixed_wire_exact_contraction.md),
equation (3), is
\[
 f_a(y)=\frac{e^{-\pi i(N-1)y}}N
 Y^a\prod_{j=a+1}^{N-1}(1-Yr^j).
 \tag{2}
\]
In particular it is an entire finite Fourier function, not a
conditional kernel with its argument replaced by \(y\).

Define the negative-band interpolation
\[
 J_N^{\rm F}(y,X)=\frac1N\sum_{a=0}^{N-1}P_af_a(y)
                   \sum_{j=0}^{N-1}(r^a/X)^j.
 \tag{3}
\]
It has band \([-N+1,0]\) and
\(J_N^{\rm F}(y,r^a)=P_af_a(y)\). For every polynomial
\(F\) of degree less than \(N\), the original transform satisfies
\[
 \mathcal E_\alpha F(y)
 =N\operatorname{CT}_X
          [F(X)W_{\alpha,N}(X)J_N^{\rm F}(y,X)].
 \tag{4}
\]
Indeed the physical-node value of the right side is
\(\sum_a F(r^a)J_N^{\rm F}(y,r^a)/P_a^\alpha\),
which is exactly the definition of \(\mathcal E_\alpha\).
The band calculation is the one in
[literal transfer](research_mixed_literal_transfer_norm_obstruction.md),
equations (3)--(7). If \(\alpha=1\), it retains both constant-term
sectors, zero and \(N\); their values are not identified separately.

Contract the last node before choosing a retained graph. The resulting
literal cap is
\[
 \begin{split}
 V_N^{\rm F}(y,X)
 &=N\operatorname{CT}_Z
       [C_{1,N}(X,Z)W_{1,N}(Z)J_N^{\rm F}(y,Z)]\\
 &=\sum_{a=0}^{N-1}C_{1,N}(X,r^a)f_a(y).
 \end{split}
 \tag{5}
\]
It again has band \([-N+1,0]\) in \(X\). Equations (4)--(5)
are signed identities, including all physical rows and the last
type-four sector. They assert no preferred off-grid asymptotic for
the interpolation (3).

By the [exact message intertwiner](research_mixed_conditional_fourier_message_bridge.md),
equations (6)--(9), the original observation is therefore
\[
 \begin{split}
 G_N(y,w)&=v_N(w)^TA_{3+\epsilon_1}\cdots A_4h_N(y)\\
 &=\kappa^{m+k}N^{m+k-1}
   \sum_{\sigma\le\epsilon}\oint
       U_{\epsilon_1,N}(w,X_1)
       \prod_{j=2}^{h}C_{\epsilon_j,N}(X_{j-1},X_j)
       V_N^{\rm F}(y,X_h)
       \prod_{j=1}^{h}d_N(X_j)^{\epsilon_j}X_j^{-N\sigma_j}
       \prod_{j=1}^{h}\frac{dX_j}{2\pi iX_j}.
 \end{split}
 \tag{6}
\]
Here the sum is only over \(1\le j\le h\). The last selection
has already been contracted in (5). The scalar follows from
\(m-1\) exact retained-node averages and the original
\(\kappa^{m+k}N^k\) Fourier normalization. All circles may have
arbitrary positive radii. Both parities and fixed ordinary/Fourier
derivatives remain literal identities.
Write \(\mathscr J^{\rm F}_{\sigma,N}\) for the displayed
integrand, without its differential factors or outside scalar.

Choose each summand's hybrid graph after (6). This is a homotopy of
its Laurent-polynomial top form in \((\mathbb C^\times)^h\),
not a projection of a graph depending on the eliminated last node.
This is precisely the construction of
[contracted finite boundary windows](research_mixed_contracted_finite_boundary_windows.md),
Section 1, with (5) in place of the ordinary terminal polynomial.

## 2. Which reference estimates actually transfer

Work first at \((y,w)=(x_0,-2)\) and use the original critical
point from [Fourier-boundary existence](research_mixed_fourier_boundary_critical_existence.md).
Write \(r_j=t_j^*\). Every vertex \(2,\ldots,m\) is an
ordinary two-leg block. The last one has right exterior leg
\[
 b_*=\beta_K(t_m^*)\in D_3,
 \qquad |b_*-(.35-.01i)|<.082,
 \qquad K=e^{2\pi ix_0}.
 \tag{7}
\]
The [original boundary update](research_mixed_fourier_boundary_update.md),
Lemma 2, proves with the fixed original logarithmic lifts that
\(G_t(t_m^*,b_*)=\ell_{t_m}'(x_0)\).

Consequently any ordinary window in \([2,m]\), with its actual
two exterior legs fixed, solves the same original equations as its
certified full-bidisk/window map. At the right endpoint use (7).
The common convex-domain uniqueness identifies the branches, not
merely their containing rectangles. In particular all conservative
interior ranges of
[open-word window inheritance](research_mixed_open_word_window_inheritance.md)
remain valid. No gain from moving those ranges one index right is
needed here.

The precise local uses are as follows.

| Input | Actual hypothesis used here |
|---|---|
| Coarse type-three/type-four images | The whole ordinary bidisk maps, not a repeated cycle |
| Refined type heights, conditioned three-type slopes, oriented 44/444 heights | The identical three- and five-vertex zero-lift window with its actual exterior legs |
| Closed-half, seam repair and upper-transition removal | Their prescribed independent typed height products and source domains |
| Minimum-level transport and final early/plateau/right allocation | The inherited conditioned windows; the conservative largest support has six vertices |
| First-cap profile planes | The oriented/inverse-feasible actual source domain, proved also for Fourier prefixes in the coherent main-sheet theorem |

An eight-vertex halo still suffices for every changed local rate and
its reference window. Thus the proof of
[open boundary comparison](research_mixed_open_boundary_comparison_reduction.md),
Lemma 1, applies verbatim to a compact perturbation whose halo is
inside \([6,m-5]\). That proof uses original local moves and
stationarity, not a periodic completion. Its strengthened
[full-period occupation inequality](research_mixed_full_period_occupation.md)
gives
\[
 -\sum_j w_j\ge\kappa_{\rm occ}\sum_{j\in I}p_j,
 \quad \kappa_{\rm occ}=1/20000,\quad
 p_j=\min\{1,\sigma_j+400(\operatorname{clamp}_{[.22,.45]}x_j
                                      -\Re r_j)^2\}.
 \tag{8}
\]
Here \(w_j\) is the original complete allocated source rate minus
its complex affine tangent. All right-incident raw rows, collar
priority and both selected Fourier alternatives are retained.

By contrast, the periodic closing proof for the
[retained boundary potential](research_mixed_full_alphabet_boundary_potential.md)
and the [repeated-trace theorem](research_mixed_uniform_repetition_bound.md)
uses a repeated original reference. Neither theorem can simply be
applied to the present reference as though it were periodic. Equation
(8) is the valid local replacement; it is already strong enough for
the finite-boundary reduction.

## 3. The Fourier boundary action and the two remaining costs

For an incoming type flag \(\eta\), define the calibrated local
Fourier-end action
\[
 \begin{split}
 Q_1(s;a,t)&=g(a+s)+g(s+t)-3g(s)-g(a)-g(t)+2\pi ias,\\
 \Pi^{\rm F}_\eta(a;y)
 &=\operatorname{crit}_{s,t}\{Q_1(s;a,t)+\ell_t(y)\}
                                      -\frac\eta2g(a).
 \end{split}
 \tag{9}
\]
This retains the incidence constant in the original \(\ell\),
including \(-\pi iy\). The critical value is on the original
branch, not chosen modulo an additive constant.

The branch in (9) exists for every fixed incoming \(a\) in its
typed disk. Indeed update the ordinary last vertex with exteriors
\((a,b)\), and update \(b\) by \(\beta_K(t)\).
The proved inclusions give a compact self-map. Its fixed point is
an original critical point by the zero-lift identity. For uniqueness,
\[
 Q_1(s;a,t)+\ell_t
       =V(a,s)+V(s,t)-g(s)+2\pi ias+\ell_t,
 \qquad V(v,z)=g(v+z)-g(v)-g(z).
 \tag{10}
\]
With \(a\) fixed, the pair estimates on \(Q^2\) in
[the open Hessian theorem](research_mixed_open_word_hessian.md),
and the positive last-incidence term in the boundary-update theorem,
give \(-\Re\partial^2_{s,t}(Q_1+\ell)\succ(\pi/8)I\).
Thus the branch is unique and simple. The same argument gives
one-ended suffix families with any fixed typed exterior leg, using
ordinary updates before the final update. Compactness and the implicit
function theorem give their parameter neighborhoods.

Let \(L\) be the original allocated first-cap action, and let
\(\phi_j\) be the allocated ordinary phases with their original
two halfweights. The actual action decomposes exactly as
\[
 \Phi=L(r_1)+\sum_{j=2}^{h}\phi_j(r_{j-1},r_j)
               +\Pi^{\rm F}_{\epsilon_h}(r_h;x_0),
 \qquad M=\Re\Phi.
 \tag{11}
\]
This follows either by expanding (9), or from the original full
factorial action in the
[Fourier-prefix local-current theorem](research_mixed_fourier_prefix_local_current.md).
In particular the added term \(-\eta g(a)/2\) in (9) supplies
exactly the missing incoming halfweight; no last diagonal factor is
added after (5).

Choose \(p=16,q=m-15\) when the safe middle is nonempty.
Let \(D_j=d_N(X_j)^{\epsilon_j}X_j^{-N\sigma_j}\).
The two literal boundary moduli are
\[
 \begin{split}
 L_N&=|U_{\epsilon_1,N}|\prod_{j=2}^{p-1}|C_{\epsilon_j,N}|
          \prod_{j=1}^{p-2}|D_j|\,|D_{p-1}|^{1/2},\\
 R_N^{\rm F}&=|V_N^{\rm F}|\prod_{j=q+1}^{h}|C_{\epsilon_j,N}|
          |D_q|^{1/2}\prod_{j=q+1}^{h}|D_j|.
 \end{split}
 \tag{12}
\]
Their product with the allocated middle moduli is the modulus of
the integrand in (6). These are nonnegative allocations, with no
division by zeros or holomorphic square roots.

Use the synthetic compact perturbation on \(I=[p-2,q+1]\),
its protected three-edge closing sums \(A_p,E_q\), and its total
loss \(D_I\), exactly as in the contracted-window theorem.
Let \(M_L\) and \(M_R^{\rm F}\) be the real parts of the two
end pieces of (11). Put \(P_{p,a}=\partial_1\phi_p(r)\),
\(P_{q,b}=\partial_2\phi_q(r)\), and
\[
 \begin{split}
 B_{L,N}&=N^{-1}\log L_N-M_L
       +\Re[P_{p,a}(z_{p-1}-r_{p-1})]-A_p,\\
 B_{R,N}^{\rm F}&=N^{-1}\log R_N^{\rm F}-M_R^{\rm F}
       +\Re[P_{q,b}(z_q-r_q)]-E_q.
 \end{split}
 \tag{13}
\]
As usual \(\log0=-\infty\). Original stationarity cancels
only the internal tangents. For every aggregate tolerance
\(\delta>0\), the existing complete middle-source bounds give
\[
 \frac1N\log|\mathscr J^{\rm F}_{\sigma,N}|-M
 \le B_{L,N}+B_{R,N}^{\rm F}-D_I
                         +\delta+O_m(\log N/N),
 \qquad D_I\ge\kappa_{\rm occ}\sum_{j\in I}p_j.
 \tag{14}
\]
This concerns full retained periods and the actual Fourier-ended
reference. It is not a bound over the outgoing Fourier period.
The latter parameter remains near \(x_0\).

## 4. Bounded width follows, but its boundary sign is still missing

On fixed compact hybrid annuli and an output neighborhood with
\(0<\rho_-\le|Y|\le\rho_+<1\), (2) gives, for example,
\[
 |f_a(y)|\le N^{-1}\rho_-^{-(N-1)/2}(1+\rho_+)^{N-1}.
 \tag{15}
\]
Together with \(|P_j|\le2^j\),
\(|P_j|\ge N2^{-(N-1-j)}\), and the exact \(N\)-term
formula (5), this proves a finite exponential upper budget for the
new right factor, uniform in \(N\). Fixed derivatives add only
polynomial factors. The two boundary widths are fixed; their calibrated
actions, slopes and closing rates are bounded on the fixed one-ended
reference families. Thus
\[
                    B_{L,N}+B_{R,N}^{\rm F}\le K_\partial
 \tag{16}
\]
for a finite \(K_\partial\) independent of total word length and
level. This is an upper budget, not a favorable sign.

Consequently the exact relative-pinning proof of
[finite boundary windows](research_mixed_open_finite_boundary_windows.md),
Sections 3--4, transfers unchanged. It uses
\(d=352\), \(\ell=711\),
\(a_d=1000(99/101)^{2d}<1/1296\), and
\[
 B=\left\lfloor\frac{K_\partial+\eta}{\kappa_{\rm occ}}\right\rfloor,
 \qquad R=(B+1)\ell.
 \tag{17}
\]
For a potentially violating configuration, pinning produces
\[
 \begin{split}
 B_{L,N}+B_{R,N}^{\rm F}-D_I
 \le{}&[B_{L,N}-D_L+a_d\delta_L^2]\\
     &+[B_{R,N}^{\rm F}-D_R+a_d\delta_R^2]
             -\frac{\kappa_{\rm occ}}2\sum_{j\in I_M}p_j.
 \end{split}
 \tag{18}
\]
Each bracket involves at most \(R+3\) safe symbols and the original
fixed physical boundary width. For sufficiently long words their
suprema \(\mathcal T_{L,N}\), \(\mathcal T_{R,N}^{\rm F}\)
give the same exact reduction
\[
 \sup(B_{L,N}+B_{R,N}^{\rm F}-D_I)
       \le\max\{-\eta,\mathcal T_{L,N}+\mathcal T_{R,N}^{\rm F}\}.
 \tag{19}
\]
The original length condition and protected pinning corridors remain
in force. Shorter words form finitely many whole-source problems.
Reference families remain coupled to their one external typed leg;
allowing the two suprema independently is only a sufficient relaxation.
This is a finite family of level-uniform source problems, not a
finite-level numerical criterion. No uniform-in-length Gaussian
asymptotic is inferred from the \(O_m\) term in (14).

The concrete remaining theorem is an upper-rate estimate for the two
brackets in (18), with a strict loss away from their actual unselected
reference germs. The right bracket now contains the explicit function
\(V_N^{\rm F}\), and the left one retains the actual first cap.
The existing first-cap planes control its original-height plateau
profiles, but do not remove arbitrary taper heights, neighboring
physical states or the relative fee. Likewise (7) supplies the right
reference family without estimating (5) on those states. Separately
requiring \(B_L\le0\) and \(B_R\le0\) would discard necessary
middle compensation; the quadratic obstruction in the open boundary
comparison note still applies.

Finally \(\beta_K\) is not an action or finite-source substitution.
Although \(G_t(t,\beta_K(t))=\ell_t'(x_0)\),
\[
 \frac d{dt}\{\ell_t(x_0)-G(t,\beta_K(t))\}
                   =-G_b(t,\beta_K(t))\beta_K'(t),
 \tag{20}
\]
which has no proved zero or favorable sign. The exact right boundary
cost in (13) therefore cannot be replaced by an ordinary cap cost
or an existing cyclic bound. Equation (19) completes the reduction
to the correct two source costs; it does not discharge them, prove
an arbitrary-message Fourier norm, or enlarge the established knot
class.
