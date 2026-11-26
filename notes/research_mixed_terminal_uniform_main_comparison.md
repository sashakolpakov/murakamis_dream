# Uniform terminal main comparisons on the complete type-four input disk

Research completion, 6 November 2026.

Both terminal types and both alternatives of the complete selected
weight now have a uniform main-phase gap greater than \(1/400\)
on the whole canonical type-four input disk. The selected height is
\(H=.01\), and both alternatives retain the full selected real
interval. This is a main-profile result; it does not control every
terminal contour profile or the complete terminal kernel.

## 1. The original phase and the uniform comparison

The preceding ordinary block has own flag one, and the incoming
flag is \(\beta=1\). For each terminal flag \(\epsilon=0,1\)
and parameter
\[
 \zeta\in D_4=
 \{|\zeta-(3/10-13i/250)|\le8/125\},
 \tag{1}
\]
use the original canonical reference
\((b_*,s_*,a_*,t_*,v_*)\), where \(b_*=\zeta\) and
\(v_*\) is \(\xi_*\) for terminal type three or \(e_*\)
for terminal type four. The
[complete reference theorem](research_mixed_terminal_all_input_affine_enclosures.md)
and its [posterior refinement](research_mixed_terminal_quadratic_residual_refinement.md)
enclose these same canonical branches on the closed disk, preserving
the original logarithmic equations and lifts.

Keep the original primitive and phases of the
[joint-main theorem](research_mixed_terminal_joint_main_budget.md):
\[
 \begin{split}
 Q_1(s;b,a)&=g(s+b)+g(s+a)-3g(s)-g(b)-g(a)+2\pi ibs,\\
 F_\epsilon&=Q_1+\Phi_\epsilon-g(a)-\tfrac12g(b),\\
 M_*(\zeta)&=F_\epsilon(b_*,s_*,a_*,t_*,v_*),\\
 p_*(\zeta)&=g'(\zeta+s_*)-\tfrac32g'(\zeta)+2\pi is_*.
 \end{split}
 \tag{2}
\]
Thus the incoming modulus halfweight, original private action and
full complex affine marginal are retained.

Set \(H=1/100\). The real targets range over
\[
 b_R,a_R\in P=[.22,.45],\quad s_R\in[.125,.5],\quad
 t_R\in[.15,.5],\quad v_R\in I_\epsilon,\qquad
 I_0=[.1,.4],\quad I_1=[.27,.49].
 \tag{3}
\]
The heights of \(b,s,t,v\) are their original reference heights,
and \(\Im a=H\). For \(\nu=1\) (factorial) and
\(\nu=0\) (forced), define the literal defect
\[
 D_{\epsilon,\nu}(\zeta;x)=
 \Re\{Q_1+\Phi_\epsilon-\nu g(a)-\tfrac12g(b)
                   -M_*(\zeta)-p_*(\zeta)(b-\zeta)\}
                         -2\pi\nu H.
 \tag{4}
\]

**Theorem 1.** For every \(\zeta\in D_4\), both terminal flags,
and both alternatives, uniformly over the full targets (3),
\[
                  \sup_xD_{\epsilon,\nu}(\zeta;x)<-1/400.
 \tag{5}
\]

The [symmetric pair-cost theorem](research_mixed_terminal_symmetric_pair_costs.md)
and the original index barriers justify optimizing on
\(s_R\in[.22,.5]\), \(t_R\in[.22,.4]\), while retaining
\(a_R\in P\) for both alternatives. These are reductions of the
original main maximum, not changes to the target statement (3).
The retained scalar costs have coefficients
\((2,\nu+1,(3+\epsilon)/2)\).

Three comparisons follow from the
[audited whole-disk height-integral test](research_mixed_terminal_four_input_integral_outcome.md).
The remaining terminal-four factorial comparison follows from the
[shared-force vertex lemma](research_mixed_terminal_shared_force_vertices.md).
It keeps the same mean imaginary cotangent in the ordinary and
selected forces, then uses convexity of the underlying scalar gains
to reduce their sum to sixteen force vertices. The sharper saved
posterior errors narrow the center and height-displacement intervals;
the original cotangent enclosures remain unchanged.

The resulting strict rational comparisons are summarized by these
upward-rounded terminating rationals:

| Terminal flag \(\epsilon\) | Alternative \(\nu\) | Uniform upper is below |
|---:|---:|---:|
| 0 | 1 | \(-.003281\) |
| 0 | 0 | \(-.022498\) |
| 1 | 1 | \(-.003660\) |
| 1 | 0 | \(-.007431\) |

Every entry is strictly smaller than \(-1/400\), proving (5).
The two alternatives are bounded at the same height and are combined
additively before taking their rate maximum. No forced target is
discarded in this completion.

## 2. The isolated finite-main consequence on actual source references

Restrict now to an actual compact source reference family covered by
the inherited regular-contour symbol estimates, with its original
type-four input domain and all oriented-image and inverse-feasibility
requirements retained. The phase extension to \(D_4\) is not a
claim that those finite-source hypotheses hold at every auxiliary
parameter in the full disk.

Let \(\mathcal M_{N,\epsilon}(b,a;w)\) denote the contribution
of the ordinary main contour and both terminal main contours to the
literal allocated product
\[
 C_{1,N}(X_b,X_a)\,\mathcal V_{\epsilon,N}(w,X_a)\,
 d_N(X_a)X_a^{-N}\,|d_N(X_b)|^{1/2}.
 \tag{6}
\]
It includes the complete selected weight and original monomial.
It excludes the other terminal labels. The
[original finite-current envelope](research_mixed_terminal_concave_profile_envelope.md)
and its uniform main-contour estimates imply, for every sufficiently
small fixed \(\tau>0\),
\[
 |\mathcal M_{N,\epsilon}|
 \le C_\tau N^{A_\tau}
 \exp N\{\Re[M_*(\zeta)+p_*(\zeta)(b-\zeta)]-1/400+\tau\}.
 \tag{7}
\]
The constants are uniform on that actual compact source family and
the full retained targets, on the inherited sufficiently small
ordinary-color disk and for every fixed jet, through both level
parities. Choosing \(\tau<1/1600\) and absorbing the polynomial
factor gives an isolated finite-main rate gap \(1/800\) for all
sufficiently large \(N\). This assertion does not extend the
finite-source domain beyond its original hypotheses.

## 3. Evidence and remaining scope

The original integral record has SHA256
9831e8bdbc884cfc0b0c99dbc7f92245403988ae7dc4bbbba86b5606c5a1575e.
Its [saved audit](../repro/results/research-mixed-terminal-four-input-integral-budget-saved-audit.json),
SHA256 cda9eef92856387d0ec0dccca6311512bb980034a07832ab89a99a7bc733d6c3,
verifies the exact support, integral and scalar-gain recombinations.

The single [vertex result](../repro/results/research-mixed-terminal-shared-force-vertices.json)
has SHA256 feaf49d8666aea740a44d167bc898f5770c059c6331a6b6ff695aba65cf9603f.
It records sixteen vertices, 48 rational cubic gains and 48 independent
gain checks, with 521 unchanged input bindings. Its largest upper is
approximately \(-.003660925326445021\), at endpoint bits
\((1,0,0,1)\), and its exact rational endpoint is below \(-1/400\).
No analytic function, root, reference, source, target optimizer or
subdivision was evaluated in this final saved-data step.

The altered private-left face is not covered by (5). In particular,
the stronger terminal localization \(t_R\in[.22,.4]\) used here
has not been proved for that altered face, so its separate trial
offset and force-contraction statements do not automatically transfer
this new main budget. Other terminal profiles require their own
uniform comparisons as well. No complete terminal-kernel theorem,
whole-word asymptotic, finite-word realization of every canonical
parameter, or knot-volume theorem is claimed.
