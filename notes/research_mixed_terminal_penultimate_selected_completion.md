# The penultimate-only terminal selection and its plateau assembly

Research completion, 6 November 2026. The prescribed saved-vertex
recombination proves the two-boundary ordinary-source criterion for
both terminal types. Its complete profile deficit is \(1/400\),
giving a finite-source gap \(1/800\). This treats a selected
penultimate retained type four with its final retained type-four
neighbor unselected. Together with the earlier terminal results it
completes all four final selection patterns for that suffix. The
statement remains a local source and restricted plateau theorem.

## 1. The original two-boundary product

Fix the actual reference of a positive mixed word of length
\(m\ge4\) whose final types are
\[
 (n_{m-3},n_{m-2},n_{m-1},n_m)
                  =(3+\gamma,4,4,3+\epsilon),
       \qquad \gamma,\epsilon\in\{0,1\}.
 \tag{1}
\]
Use the exact canonical reference and original lifts of the
[penultimate-only criterion](research_mixed_terminal_penultimate_selected_criterion.md).
Write its retained coordinates as \((c_*,b_*,a_*)\), with
ordinary indices \((r_*,s_*)\). The external coordinate belongs
to \(K_{3+\gamma}\); all the remaining coordinates are in
their original ordinary type-four domains. The
[reference-bank transfer](research_mixed_terminal_two_selected_reference_bank_transfer.md)
covers every such canonical reference, and hence every actual word
reference in (1). It is an identification of the original critical
equations, not a transposition of a localized finite source.

Put \(P=[.22,.45]\), \(H=.01\), and \(X_z=e^{-2\pi iz}\).
Only \(b\) is selected: its height is \(H\), whereas \(c,a\)
keep their original heights. Their three real targets vary
independently over \(P\). Set
\[
 \begin{split}
 Q(r;c,b)&=g(r+c)+g(r+b)-3g(r)-g(c)-g(b)+2\pi icr,\\
 F_{\rm pair}&=Q(r;c,b)+Q(s;b,a)-g(b)
                              -\tfrac\gamma2g(c)-\tfrac12g(a),\\
 M_*&=F_{\rm pair}(q_*),\\
 p_c&=g'(r_*+c_*)-(1+\gamma/2)g'(c_*)+2\pi ir_*,\\
 p_a&=g'(s_*+a_*)-\tfrac32g'(a_*),\\
 \Lambda(c,a)&=\Re\{M_*+p_c(c-c_*)+p_a(a-a_*)\}.
 \end{split}
 \tag{2}
\]
The two complex marginals in (2) are retained throughout. The
original derivatives in \(r,b,s\) vanish, including
\[
        g'(r_*+b_*)+g'(s_*+b_*)-3g'(b_*)+2\pi is_*=0.
 \tag{3}
\]
No stationary equation is imposed at an approximate enclosure center.

**Theorem 1.** For every \(\eta>0\), uniformly on the above
actual canonical families and independent targets,
\[
 \begin{split}
 &|C_{1,N}(X_c,X_b)C_{1,N}(X_b,X_a)
                           d_N(X_b)X_b^{-N}|
          |d_N(X_c)|^{\gamma/2}|d_N(X_a)|^{1/2}\\
 &\hspace{12mm}\le C_\eta N^{A_\eta}
                 e^{N\{\Lambda(c,a)-1/400+\eta\}}.
 \end{split}
 \tag{4}
\]
In particular the same product has upper bound
\(C N^A e^{N(\Lambda-1/800)}\). Both parities, all original
normal and complementary terms, and both alternatives for the
single complete selected Fourier weight are included.

### Saved evidence and the complete profile implication

The immutable [completed record](../repro/results/research-mixed-terminal-penultimate-selected-budgets.json)
has SHA-256
`83725f30893cbd7ad8f138f4db5cfbc934072f1c868600784be45c90505965d0`.
It binds the criterion, the
[fixed recombination protocol](research_mixed_terminal_penultimate_selected_evaluation.md),
and the [standalone checker](../experiments/check_mixed_terminal_penultimate_selected_budgets.py),
whose SHA-256 is
`ba62fa3cf6333226e5d49a85847b86b6db1be5bd55bc96f70a3d7f66843973f2`.
All 651 input bindings are unchanged. The prescribed two cases and
four branches use the same 96 vertices and 192 previously certified
\(r,b\) gain bounds. The checker evaluates 96 explicit rational
quadratics and one-step cubic corrections. It makes no analytic,
root, optimizer, new gain, or parameter-cell evaluation.

More precisely, the coefficient \(19\) is used only after the
saved strict guard \(|\Im s_*|<.061\) passes. The original
unopposed negative \(s\)-force is bounded by the exact convex
conjugate and its rational upper from Lemma 3 of the criterion.
Each saved two-selected vertex has its old linear shared debit
removed and that rational upper inserted. The signed forced trial
and selected-coordinate gain retain their common endpoint variable.
The convex vertex argument concerns exact conjugates, not the
rounded upper values. The four resulting main bounds are all
strictly below \(-1/400\); the record therefore reports the
complete profile upper \(-1/400\), raw gap \(1/400\), and
finite gap \(1/800\).

*Proof of Theorem 1.* Apply the complete-source criterion, Theorem 1,
with these four main bounds. Its source reduction includes all
\(7\cdot7\cdot2=98\) ordinary-profile/weight choices, or 32
after maximizing the four affine last-row carriers in each factor.
The six left nonmain labels are pointwise dominated on the full
actual \(K_3\cup K_4\) input domain. The right left-cut and
half-row labels are dominated in their correct selected-incoming,
unselected-outgoing orientation. The remaining right last-row
envelope is paid jointly by the original two-factor comparison
with deficit \(1/400\). The double-last choices are included by
first replacing the left carrier, then using that joint bound.
These are complete finite-source reductions, including physical
tails, revived rows, aliases and vertical joins.

For the main/main case the original lower-index barriers, symmetric
pair allocation and stationarity (3) give the same simultaneous
costs \(2g_{h_r},(\mu+1)g_H,2g_{h_s}\). The factorial branch
uses full \(P\). The forced branch restriction is the original
complete-weight comparison; its clipped gain stays signed when
the reference center is outside \([.4,.45]\). The certified
vertex bounds apply to precisely this source and these targets.
Thus every original profile has defect at most \(-1/400\).
One aggregate tolerance gives (4), and choosing it smaller than
\(1/800\) gives the stated finite bound. \(\square\)

## 2. Joining the unselected terminal factor and the preceding source

Put \(h=m-1\), and use the original allocated action
\[
 \Phi=L(z_1)+\sum_{j=2}^h\phi_j(z_{j-1},z_j)+\Pi(z_h),
                 \qquad M=\Re\Phi(\mathbf z_*),
 \tag{5}
\]
from the [unselected plateau theorem](research_mixed_full_unselected_plateau.md).
The identification in Theorem 1 is
\((c,b,a)=(z_{h-2},z_{h-1},z_h)\). In this notation
\[
 \begin{split}
 M_*&=\phi_{h-1}(z_{h-2,*},z_{h-1,*})
                              +\phi_h(z_{h-1,*},z_{h,*}),\\
 p_c&=\partial_1\phi_{h-1},\qquad p_a=\partial_2\phi_h,\\
 \partial_2\phi_{h-1}+\partial_1\phi_h&=0,
                   \qquad p_a+\Pi'(z_{h,*})=0.
 \end{split}
 \tag{6}
\]
Adjoin the original unselected terminal source with its allocated
halfweight at \(a\). Its supporting plane cancels \(p_a\)
exactly. The other halfweight at \(a\) is in (4), so the
original integer weight is restored. Similarly the preceding
ordinary factor cancels \(p_c\) and supplies the other half at
\(c\). When \(m=4\), the preceding factor is the original
first cap instead; its derivative and halfweight do the same job.
When \(\gamma=0\), both incoming halves are absent.
The selected weight at \(b\) was already complete in (4).

All statements retain the full complex marginals before taking
real parts. There is no residual boundary force, no duplicate
halfweight, and no use of the two-selected theorem with a selection
formally removed. On the whole real ordinary-color square, use
the [first-cap real-color estimate](research_mixed_endpoint_real_color_decay.md),
equation (14), and the
[terminal real-color estimate](research_mixed_terminal_real_color_decay.md).
The two-factor product itself is independent of the ordinary colors.
Small fixed complex color neighborhoods and fixed color jets on
smaller neighborhoods follow from the original endpoint bounds
and Cauchy applied to the holomorphic integer-weighted product.

## 3. The additional plateau sectors and unchanged leading packet

For
\[
 I_m^{(4)}=\{j:6\le j\le m-5,\ \epsilon_j=1\},\qquad
 S\subseteq I_m^{(4)},
 \tag{7}
\]
define the new selected set \(S^- =S\cup\{h-1\}\), with
\(h\) unselected. The penultimate height is \(.01\), the
selected interior heights are \(7/500\), and every other height
is its original one. Integrate the literal source
\[
 \begin{split}
 \mathscr J_{S^-,N}={}&U_{\epsilon_1,N}(w_L,X_1)
       \prod_{j=2}^h C_{\epsilon_j,N}(X_{j-1},X_j)
                      \mathcal V_{\epsilon_m,N}(w_R,X_h)\\
 &\quad\cdot\prod_{j=1}^h
                d_N(X_j)^{\epsilon_j}X_j^{-N\mathbf1_{j\in S^-}}
 \end{split}
 \tag{8}
\]
over \(P^h\), sum over \(S\), and restore the original scalar
\(\kappa_N^{m+k_4}N^{m+k_4-1}\), where
\(\epsilon_j=n_j-3\), \(k_4=\sum_j\epsilon_j\), and
\(|\kappa_N|=1\). Call the result
\(E_N^{\rm pen}\). No source normalization or coefficient is
changed.

The interior incidences \(E(S)=\bigcup_{j\in S}\{j,j+1\}\)
have indices at most \(m-4\). They are disjoint from the two
ordinary factors \(m-2,m-1\) used in (4). Apply the
[interior-selection theorem](research_mixed_interior_selected_plateau.md)
there, including adjacent interior selections, and the unselected
tangents elsewhere. Equation (6) and all other original stationarity
equations cancel the affine displacements. After one aggregate
tolerance, finite summation and integration give
\[
           |E_N^{\rm pen}(w_L,w_R)|
                  \le C N^A e^{N(M-1/800)}.
 \tag{9}
\]
This holds on the full real color square, on sufficiently small
fixed complex color neighborhoods, for both parities, and for fixed
ordinary-color jets on smaller neighborhoods.

Let \(Z_N^{\rm int,last\,two}\) be exactly the polynomial in
the [two-selected completion](research_mixed_terminal_two_selected_kernel_completion.md),
equation (13). Define
\[
             Z_N^{\rm int,end\,four}
                       =Z_N^{\rm int,last\,two}+E_N^{\rm pen}.
 \tag{10}
\]
The earlier polynomial contains the final selection patterns
\(\varnothing,\{h\},\{h-1,h\}\); the new pattern
\(\{h-1\}\) is disjoint from all of them. Thus (10) is an
explicit restricted sum of original sectors, with no double counting.
Its ordinary-color degrees remain at most \(N-1\), and (9)
is exponentially smaller than the existing packet after shrinking
the complex neighborhood if necessary. Consequently
\[
 Z_N^{\rm int,end\,four}
    =\kappa_N^{m+k_4}N^{-3/2}A(w_L,w_R)
        e^{N\mathcal W(w_L,w_R)}(1+O(N^{-1})),
                       \qquad A(-2,-2)\ne0,
 \tag{11}
\]
with the same action, amplitude, branches and original scalar.
The new sectors cannot cancel its leading coefficient.

The old real outside-color gap and (9) retain a gap at least
the minimum of the old gap and \(1/800\). In particular the
conservative common terminal-sector gap \(1/5200\) from the
older restricted sum remains valid. The degree bound, local packet
and real gap satisfy the
[open-source stability lemma](research_mixed_open_source_stability_reduction.md),
which gives the corresponding thin angular-strip estimate for
the same restricted polynomial.

For \(m\ge6\), the
[disjoint endpoint-window lemma](research_mixed_disjoint_endpoint_plateau_assembly.md)
also permits all already completed first-two selections together
with these four final patterns and the safe interior selections.
This uses separate complete left/right real-color inputs and the
original shared unselected-coordinate cancellation; overlapping
short windows are not covered by that joining rule.

The ending \((4,4)\) restriction on the two ordinary factors is
essential here. A selected type four followed by an unselected
own-three factor, other boundary selected positions, overlapping
short windows, and the full nonplateau complement remain distinct
obligations. Equations (10)--(11) concern a restricted plateau
polynomial, not the whole original open source or invariant.
No new knot-family or finite-exceptions theorem follows from this
local completion alone.
