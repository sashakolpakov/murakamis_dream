# Finite boundary comparisons for the complete open source

Research reduction, 5 November 2026. The full occupation inequality
and plateau forgetting reduce a possibly positive open-source upper
rate to two bounded-width boundary comparisons. The boundary functions
retain the literal endpoint polynomials and the exact middle completion
cost. A relative pinning estimate leaves no constant error at the
reference. The resulting finite boundary inequalities are not proved
here; neither a global open-source asymptotic nor an ordinary-color
strip theorem is asserted.

## 1. The original boundary functions

Fix a word and its actual complete-color open critical point. Use the
safe ordinary interval
\(I=[a,b]=[p-2,q+1]\) and all definitions from
[the open boundary comparison](research_mixed_open_boundary_comparison_reduction.md).
In particular, \(w_j\) is the original tangent-subtracted mixed
upper rate, \(A_p,E_q\) are its six closing terms, and
\[
 D_I(\mathbf q)=-\sum_j w_j(\widetilde{\mathbf q}),
 \qquad D_I\ge\kappa\sum_{j\in I}p_j,
 \qquad \kappa=\frac1{20000}.                         \tag{1}
\]
Here \(\widetilde{\mathbf q}\) retains the symbols in \(I\)
and is baseline elsewhere. The occupation \(p_j\) is exactly the
one in [the full-period occupation theorem](research_mixed_full_period_occupation.md):
it vanishes outside \(I\), and inside \(I\)
\[
 p_j=\min\{1,\sigma_j+400(\operatorname{clamp}_P x_j-\Re r_j)^2\},
 \qquad P=[.22,.45].                                   \tag{2}
\]
All reference windows touched below are required to be safe in the
sense of the cited boundary comparison. The fixed eight-vertex halo
there suffices. In particular \(.27<\Re r_j<.39\) on every
affected window.

The two complete boundary moduli are the literal products
\[
\begin{split}
 L_N(w_L)&=|U_{\epsilon_1,N}(w_L,X_1)|
       \prod_{j=2}^{p-1}|C_{\epsilon_j,N}|
       \prod_{j=1}^{p-2}|D_j|\ |D_{p-1}|^{1/2},\\
 R_N(w_R)&=|H_N(w_R,X_m^{-1})|
       \prod_{j=q+1}^{m}|C_{\epsilon_j,N}|
       |D_q|^{1/2}\prod_{j=q+1}^{m}|D_j|,\\
 D_j&=d_N(X_j)^{\epsilon_j}X_j^{-N\sigma_j}.
\end{split}                                                   \tag{3}
\]
Every selected Fourier alternative is kept. The source factors in
(3) are not replaced by their local saddle packets outside those
packets' domains. Define, with \(\log0=-\infty\),
\[
\begin{split}
 B_{L,N}&=N^{-1}\log L_N-M_L
    +\Re[P_{p,a}(z_{p-1}-r_{p-1})]-A_p,\\
 B_{R,N}&=N^{-1}\log R_N-M_R
    +\Re[P_{q,b}(z_q-r_q)]-E_q,\\
 F_N(\mathbf q;w_L,w_R)&=B_{L,N}+B_{R,N}-D_I(\mathbf q).
\end{split}                                                   \tag{4}
\]
The constants \(M_L,M_R\) are the complete-color reference
actions of the literal boundary products. Both surviving tangents
remain in (4). The first boundary function depends on only the first
three symbols of \(I\), in addition to its original physical
prefix; the second uses only its last three and its physical suffix.

For each fixed word and any prescribed total rate tolerance
\(\delta>0\), the established middle source bounds give
\[
 N^{-1}\log|\mathscr I_{\sigma,N}(\mathbf q;w_L,w_R)|
       -M_{\rm open}
 \le F_N(\mathbf q;w_L,w_R)+\delta+O_m(\log N/N).
                                                               \tag{5}
\]
This includes the original polynomial normalization and bounded
almost-everywhere graph Jacobian in the harmless prefactor. No
Fourier factor is divided out. The ordinary colors remain exclusively
in (3); the reference, tangents and occupation comparison in this
note are at complete colors. In particular (5) does not silently
replace \(M_{\rm open}\) by a moving-color critical action.

The argument below also applies to any uniform upper rates for the
literal products (3), in place of their exact normalized logarithms.
Such rates must include the whole private rows, ordinary-color
dependence and all originally retained Fourier factors.

## 2. A finite uniform upper budget

Fix a compact set of ordinary colors and keep the original physical
prefix and suffix widths bounded, as in the choice \(p=16\),
\(q=m-15\). There is a finite constant \(K\ge0\), independent
of the total word length and of \(N\ge2\), such that
\[
                         B_{L,N}+B_{R,N}\le K.           \tag{6}
\]
This is only an upper budget, not a desired boundary sign.

Here is a direct way to obtain such a budget from the exact source.
For \(P_j=(r;r)_j\), \(r=e^{-2\pi i/N}\),
\[
 |P_j|\le2^j,\qquad
 |P_j|\ge N\,2^{-(N-1-j)}\quad(0\le j<N),              \tag{7}
\]
because \(\prod_{k=1}^{N-1}|1-r^k|=N\). Thus every fixed
factorial quotient in the original finite kernels has an exponential
upper bound with a fixed constant. The degree-bounded Fourier
interpolations have at most polynomially many summands; evaluating
their bands on the compact hybrid annuli adds another fixed
exponential constant. More explicitly, the original Newton basis is
\(e_l(w)=\prod_{a<l}(c_a-w)/S_l^2\), where
\(|c_a|\le2\) and \(S_l=|P_l|\). On \(|w|\le W\),
\(|e_l(w)|\le(2+W)^l/S_l^2\). Together with (7), the
exact finite boundary formulas for \(U,H\)
therefore have the same kind of uniform bound, including all rows.
There are only boundedly many factors in (3). Finally the reference
actions, original slopes and six closing rates are bounded on their
fixed compact source domains. These observations give (6), and allow
any larger explicit rational budget to be used. No numerical value
of \(K\) or favorable boundary sign is asserted here.

Call a symbol in \(I\) **bad** when it is selected or its real
coordinate is outside \(P\). Each bad symbol has \(p_j=1\).
For \(\eta\ge0\), every configuration satisfying
\(F_N> -\eta\) consequently has at most
\[
                    B=\left\lfloor\frac{K+\eta}{\kappa}\right\rfloor
                                                               \tag{8}
\]
bad symbols. This counts physical symbols, not types or formal
incidences. The unselected real coordinates in \(P\) need not be
close to their reference values.

## 3. Pinning a good block with a relative error

Put \(q_0=99/101\). A good block of length \(2d+7\) has
vertices \(0,\ldots,2d+6\), all unselected and in \(P\).
Keep the halos \(0,2d+6\) and the Dirichlet endpoints
\(u=x_1,v=x_{2d+5}\) fixed. Optimize the \(2d+3\) coordinates
\(2,\ldots,2d+4\), then pin the central three coordinates
\(d+2,d+3,d+4\) to their reference values.

All variable coordinates stay in \(P\), where every cutoff is
one. Thus every row in the optimized corridor has its full original
reference height, and no exterior height changes. Even the two
exterior edges adjacent to the fixed Dirichlet endpoints stay
unchanged. The only varying part of \(D_I\) is exactly the
nearest-neighbor residual energy in
[plateau forgetting](research_mixed_plateau_boundary_forgetting.md).
That proof uses the local Hessian and reference stationarity, so
applies to these safe actual open windows without a periodic
completion.

Write \(a_u=\Re r_1\), \(a_v=\Re r_{2d+5}\).
If \((9/5)q_0^d<1/20\), the optimized, triple-pinned replacement
increases \(D_I\) by at most
\[
 a_d\{(u-a_u)^2+(v-a_v)^2\},
       \qquad a_d=1000q_0^{2d}.                          \tag{9}
\]
Indeed the unconstrained corridor minimum is no greater than its
original value, and the pinning loss is at most
\(20C^2q_0^{2d}\), with
\(C^2\le50[(u-a_u)^2+(v-a_v)^2]\).
The inactivity assertion is needed only on the three pinned
coordinates, not at all coordinates of the minimizer.

For an unselected endpoint in \(P\),
\[
 (u-a_u)^2\le\frac{81}{2500}p_u,
 \qquad
 a_d(u-a_u)^2\le c_d p_u,
 \qquad c_d=\frac{162}{5}q_0^{2d}.                       \tag{10}
\]
For displacements of square at most \(1/400\), this follows from
\(p_u=400(u-a_u)^2\); otherwise use \(|u-a_u|<.18\) and
\(p_u=1\). The same holds at \(v\). An explicit uniform choice is
\[
 d=352,\qquad
 (9/5)(99/101)^{352}<1/20,\qquad
 c_{352}<1/40000=\kappa/2.                               \tag{11}
\]
These are exact rational comparisons. The outer endpoint fee in (9)
is sharper than its occupation bound in (10), and vanishes exactly
at the reference.

## 4. Two bounded windows and the remaining middle loss

Set \(\ell=2d+7\), \(R=(B+1)\ell\). Suppose
\[
                              |I|\ge6+2R.               \tag{12}
\]
Protect the first and last three symbols of \(I\), which carry
the boundary functions in (4). Partition the next \(R\) symbols
from each end into \(B+1\) disjoint blocks of length \(\ell\).
By (8), each group contains a good block. The two groups are disjoint
by (12).

Apply Section 3 to the chosen left and right good blocks. Denote the
endpoints of the left block by \(u_L,v_L\), in that order, and
of the right block by \(u_R,v_R\). The outer endpoints are
\(u_L,v_R\); the inner ones are \(v_L,u_R\). The boundary
functions (4) do not change. After the two triple pins, the new
configuration splits into left, middle and right compact
perturbations, with residual energies \(D_L,D_M,D_R\).
Exactly three baseline symbols separate their supports. Since an
original mixed weight depends on four consecutive symbols, no weight
sees two distinct supports, and
\[
                        D_I^{\rm pinned}=D_L+D_M+D_R.   \tag{13}
\]
The middle component remains safe. Its occupation inequality gives
\(D_M\ge\kappa\sum_{j\in M}p_j\). The two inner endpoints
are distinct physical symbols of this component and are not moved
by the optimization. Hence (9)--(11) imply
\[
\begin{split}
 F_N(\mathbf q)
 &\le [B_{L,N}-D_L+a_d(u_L-a_{u_L})^2]\\
 &\quad+[B_{R,N}-D_R+a_d(v_R-a_{v_R})^2]
                  -\frac\kappa2\sum_{j\in M}p_j.
\end{split}                                                   \tag{14}
\]
The pins can only create additional unselected plateau symbols.
No estimate on the occupation of their optimized neighbors is needed:
the middle inequality is applied to the resulting actual middle
component. Its two inner endpoint penalties are unchanged.

Define \(\mathcal T_{L,N}^{R,d}\) as the supremum of the first
bracket in (14) over its physical boundary prefix, the at most
\(R+3\) retained safe symbols, and the \(B+1\) possible left
block positions. After the corresponding pin the remaining symbols
are baseline. Require the chosen block's surviving symbols to be
unselected \(P\) symbols, and retain its distinguished outer
Dirichlet coordinate in the displayed quadratic fee. Define
\(\mathcal T_{R,N}^{R,d}\) by reflection. These are explicit
finite-variable boundary functions: they use the original products
(3), original tangents and local rates, together with the residual
sum of the one-sided compact perturbation. They are not bounds for
\(B_{L,N}\) or \(B_{R,N}\) separately.

**Theorem 1.** Under (6), (11) and (12),
\[
 \boxed{\quad
 \sup_{\mathbf q}F_N(\mathbf q;w_L,w_R)
 \le\max\{-\eta,
       \mathcal T_{L,N}^{R,d}(w_L)+\mathcal T_{R,N}^{R,d}(w_R)\}.
 \quad}                                                       \tag{15}
\]
For a potentially violating configuration the stronger pointwise
bound (14) retains half the middle occupation. Configurations with
\(F_N\le-\eta\) already satisfy (15). All other configurations
have the two good blocks just used. Taking the two finite suprema
proves the theorem.

In particular, choosing \(\eta=0\), nonpositivity of the sum of
these finite boundary functions is a sufficient exact rate criterion
for every longer word. There is no constant truncation error near
the reference. This does not assert that the criterion holds. One
can keep the two boundary maxima coupled through their admissible
reference data; allowing them independently is only a sufficient
relaxation.

For asymptotic use, an exact finite-level nonpositive sign is not
required: a uniform upper bound
\(\mathcal T_{L,N}^{R,d}+\mathcal T_{R,N}^{R,d}
\le C\log N/N+\delta_1\) propagates through (15) with those
same terms. The one middle tolerance in (5) is then added once.
The tolerances can be chosen as parts of one prescribed total budget.
Survival of the local Gaussian needs strict upper-rate gaps on its
complement, together with the local contour comparison; mere global
nonpositivity is insufficient.

Without paying the inner fees by occupation, the same construction
gives the simpler upper bound with two finite pinned boundary
functions and additive error
\(2(324/5)q_0^{2d}\). That estimate alone cannot decide a sign
arbitrarily close to the reference. Equation (14) removes precisely
that constant-error problem.

## 5. Finite families, ordinary colors, and the remaining obligation

The physical prefix and suffix have fixed initial width. Their new
windows have at most \(R+3\) safe symbols, with a fixed extra halo
for all reference inputs. There are consequently finitely many type
words and cut positions. Their actual reference prefixes belong to
the one-external-leg families proved in Section 2 of the boundary
comparison note: fix the external nonprivate leg in its
[common smaller typed disk](research_mixed_open_local_factor_coverage.md#1-exact-factors-and-the-common-smaller-disks), solve the
endpoint and ordinary critical equations on the inherited product
chart, and restrict its unique branch. Enough untouched reference
vertices are kept between the last affected rate and that external
leg to supply the eight-vertex halo. No independent choice of all
reference coordinates, and no periodic reference substitution, is
made. Words failing (12) have a bounded total length and remain
finitely many complete source problems.

Thus (15) reduces arbitrary lengths to a finite family of
bounded-width **source estimates uniform in the level**. It is not
a claim that checking finitely many numerical levels suffices. The
bound may be large: neither a small numerical value of \(K\) nor
a practical exhaustive cover of these families is supplied.

The ordinary colors are still literal parameters of \(U,H\) in
each finite boundary function. A uniform estimate on a complex color
neighborhood would therefore permit ordinary derivatives by Cauchy's
formula, without dividing by a possibly zero boundary factor.
Such an estimate remains to be proved. Likewise, comparing with the
moving-color critical value requires retaining that value in the
boundary normalization; (15), as written, uses the complete-color
reference action.

## 6. The retained fee does not destroy the local maximum

There is a local check on the new finite comparison, at complete
ordinary colors and with every selection absent. Keep its reference
cut triple fixed, and let \(t\) denote all retained free leg
coordinates in one boundary window. The original source packets give
its leading phase \(\Phi_{\partial}(t)\). The tangents in (4)
and the closing terms in \(D_L\), or \(D_R\), cancel exactly:
\[
 \text{leading rate of }B_{\partial,N}-D_{\partial}
       =\Re\{\Phi_{\partial}(t)-\Phi_{\partial}(t^*)\}.
                                                               \tag{16}
\]
For example, let \(h\) be the first pinned coordinate at the left
cut. In this local unselected plateau germ, the only continuing
nonzero coherent edges end at \(h\), and
\[
\begin{split}
 D_L&=-A_p-\sum_{j=p}^{h}w_j,\\
 \sum_{j=p}^{h}\Re\Gamma_j
   &=\sum_{j=p}^{h}\Re\phi_j(r_{j-1},r_j)
         +\Re[P_{p,a}(z_{p-1}-r_{p-1})],\\
 B_{L,N}-D_L
   &=N^{-1}\log L_N-M_L
       +\sum_{j=p}^{h}
           \Re\{\phi_j(z_{j-1},z_j)-\phi_j(r_{j-1},r_j)\}.
\end{split}                                                   \tag{16a}
\]
The inner endpoint tangent is zero because \(z_h=r_h\);
all other internal tangent coefficients cancel by the original
critical equations. The right-end calculation is its reflected
version. The endpoint phase in
\(U\), or \(H\), remains part of \(\Phi_{\partial}\).
The ordinary-color normalization has not been differentiated or
changed. This is the actual fixed-cut source phase, not the earlier
separately closed boundary relaxation.

The proof of the
[open Hessian bound](research_mixed_open_word_hessian.md) applies to
this one-ended action with its other leg fixed. The endpoint supplies
its original \(B\) form, the other free variables retain the
ordinary pair forms, and at the fixed end the corresponding pair
contributes its active principal submatrix. Its negative real Hessian
is bounded below by \(6\pi/49\). Holomorphic elimination of the
private and conditional variables preserves this lower bound by the
same complex Schur argument as in
[the local Gaussian theorem](research_mixed_open_local_gaussian.md).
Restrict to a source neighborhood in which the continued variables
stay in the original rectangles. For the real retained displacement
\(\xi=t-t^*\), with the actual reference heights fixed, this gives
\[
 \Re\{\Phi_{\partial}(t)-\Phi_{\partial}(t^*)\}
                  \le-\frac{3\pi}{49}\|\xi\|_2^2.
                                                               \tag{17}
\]
The remaining outer fee is \(a_{352}\xi_o^2\), for one of
these same coordinates. From (11), \(a_{352}<1/1296\), and
\(9/49-1/1296>1/6\). Hence the complete leading boundary
function, including its fee, satisfies locally
\[
 \Re\{\Phi_{\partial}(t)-\Phi_{\partial}(t^*)\}
           +a_{352}\xi_o^2\le-\frac16\|\xi\|_2^2.
                                                               \tag{18}
\]
Thus the fee vanishes at the reference and is absorbed by the local
coherent maximum. Equations (16)--(18) are statements about the
leading phase. The exact finite logarithms also have their original
\(O(\log N/N)\) prefactors; no exact finite-level sign is inferred
by omitting those factors. Selected configurations and configurations
outside this source neighborhood remain the global finite boundary
comparison problem.

The reduction preserves all original source factors, Fourier
selections and surviving tangents. It supplies a finite comparison
target with a one-sided variational error and a version with no
constant error. It does not prove the sign of that target, whole
ordinary-boundary strip control, or survival of the local Gaussian
term in the complete open-chain sum.
