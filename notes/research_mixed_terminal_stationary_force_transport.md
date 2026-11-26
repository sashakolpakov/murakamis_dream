# A correlated stationary-force enclosure from saved terminal data

Research deduction and fixed saved-only protocol, 6 November 2026.
The selected factorial force can be transported from the certified center
without separately enclosing three height integrals. The original shared-leg
equation cancels their lower endpoints. The resulting real differential
retains the single complex input parameter and can be bounded using 32
vertices of already saved cotangent rectangles. This note evaluates nothing
and does not assert that the resulting bound improves or closes a budget.

## 1. Eliminate the lower-height logarithms

Use the original stationary reference \((s,a,t)\), with \(a=A+ic\),
selected height \(H=1/100\), and the factorial force \(A_{a,1}\) in
[the joint-main theorem](research_mixed_terminal_joint_main_budget.md).
The original zero-lift shared-leg equation is
\[
 g'(s+a)+g'(t+a)-3g'(a)+2\pi it=0.
 \tag{1}
\]
Consequently, at an actual canonical reference,
\[
 A_{a,1}=\widehat A(s,a,t):=
 \Re\{g'(s+A+iH)+g'(t+A+iH)-3g'(A+iH)+2\pi it\}.
 \tag{2}
\]
The right side is an explicitly defined real differentiable function on
every regular containing tube, including its nonstationary points.
Equality to the original force is asserted only on the canonical family.
It has no explicit dependence on \(c\). No branch is changed or logarithm
replaced by an equation modulo a period.

Put \(z_s=s+A+iH,\ z_t=t+A+iH,\ z_a=A+iH\),
\(\kappa_j=\cot(\pi z_j)=C_j+iI_j\), and
\(k_j=g''(z_j)=\pi(\kappa_j-i)\). Direct differentiation gives
\[
 d\widehat A=\Re\{G_s\,ds+G_t\,dt+G_a\,da\},\qquad
 G_s=k_s,\quad G_t=k_t+2\pi i,\quad
 G_a=\Re(k_s+k_t-3k_a)\in\mathbb R.
 \tag{3}
\]
The last equality uses \(dA=\Re da\). The term \(2\pi i\) in
\(G_t\) is the original terminal chirp. Thus the imaginary displacement
of \(a\) has zero direct contribution to this force differential.

## 2. Transport the common parameter before taking moduli

Consider only the type-four input and terminal type-four family:
\(\beta=\epsilon=1\), \(b_0=.30-.052i\), \(|\delta|\le r=8/125\).
The completed affine certificate gives the unchanged exact vectors
\(q^0,u\), in the order \((e,\xi,t,a,s)\). The
[quadratic residual refinement](research_mixed_terminal_quadratic_residual_refinement.md)
gives smaller certified errors \(\eta_i\), so
\[
 q_*(b)=q^0+u\delta+\zeta,\qquad |\zeta_i|\le\eta_i,\qquad
 0\le\eta_i\le\eta_i^{\rm old},\qquad \delta=b-b_0.
 \tag{4}
\]
Here \(\eta^{\rm old}\) is exactly the posterior vector used in the
[original integral protocol](research_mixed_terminal_four_input_integral_budget.md).
Its last height slab contains \(\theta=1\), and its three cotangent
rectangles therefore enclose every \(z_j\) throughout the larger
affine/error tube. Those original rectangles are retained; no derivative
bound is recomputed on a smaller tube.

Along the affine path \(q^0+\tau u\delta\), \(0\le\tau\le1\),
the common coefficient in (3), divided by \(\pi\), is
\[
 \begin{split}
 P={}&C_s(u_s+u_a)+iI_su_s+C_t(u_t+u_a)+iI_tu_t\\
    &-3C_au_a+i(u_t-u_s).
 \end{split}
 \tag{5}
\]
All coefficients are combined before taking a modulus. Since \(P\)
is affine in the five real variables \(C_s,I_s,C_t,I_t,C_a\),
its modulus is convex in each separately. Its maximum over their
saved rectangle occurs at one of its 32 vertices. Define
\[
 P^+=\max_{\text{32 vertices}}|P|,\quad
 S^+=\max|\kappa_s-i|,\quad T^+=\max|\kappa_t+i|,\quad
 A^+=\max|C_s+C_t-3C_a|.
 \tag{6}
\]
The last three maxima also occur at rectangle vertices. They require
only rational squared moduli and outward integer square roots.

Let \(q_c=q_*(b_0)\) be the original certified center reference.
Its saved root box bounds \(|s_c-s^0|\le e_s\),
\(|t_c-t^0|\le e_t\), and
\(|\Re a_c-\Re a^0|\le e_a\). If the saved original factorial
force at \(q_c\) lies in \([F_-,F_+]\), then the whole disk satisfies
\[
 A_{a,1}(b)\in[F_--B,F_++B],\qquad
 B=\pi_{\rm upper}
 \{rP^++(\eta_s+e_s)S^++(\eta_t+e_t)T^++
                                  (\eta_a+e_a)A^+\}.
 \tag{7}
\]
To prove this, integrate (3) first along the affine parameter path
and then along the error segment to \(q_*(b)\). Integrating from
\(q^0\) to \(q_c\) supplies the separate anchor correction.
All paths remain in the same larger affine/error tube: the new errors
are smaller than the old ones, and the center root box is checked
inside the old central error polydisk. Equation (2) is used at the two
actual canonical references; no intervening point is assumed stationary.

The bound (7) may be intersected with the already certified integral
force interval. Both contain the same true force. An empty intersection
is a failed consistency check, not an exclusion of an input parameter.

## 3. One prescribed saved-data calculation

The new checker is
[check_mixed_terminal_stationary_force_transport.py](../experiments/check_mixed_terminal_stationary_force_transport.py).
It uses only case \((1,1)\), the original height \(H=.01\), and
the old final slab \([15/16,1]\). Its sources are the original
center reference and force diagnostic with their completed audits,
the integral record and its exact audit, the old affine/posterior
chain, and the completed quadratic residual refinement.
All source associations and input hashes are checked before and after.

The errors in (4) are taken from the
[quadratic residual record](../repro/results/research-mixed-terminal-quadratic-residual-refinement.json),
SHA256 2834576c2a443c9ffd24032277b5f253d9a85eac17d3f754905812e822a9a331.
The cotangents remain those of the integral record
9831e8bdbc884cfc0b0c99dbc7f92245403988ae7dc4bbbba86b5606c5a1575e,
bound by audit
cda9eef92856387d0ec0dccca6311512bb980034a07832ab89a99a7bc733d6c3.
The exact center and affine response must agree throughout this chain.

The checker retains every vertex, the three error-coefficient bounds,
the explicit center-box correction, (7), and the intersection with the
old force enclosure. It then recomputes only the selected factorial
gain with coefficient \(98/5\), using the same safe moving-center
three-piece rule as the integral protocol. The old selected-center
interval, \(W\), ordinary-index gain and terminal-index gain remain
unchanged. Thus the new valid budget is
\[
 B_{\rm new}=T_1^+ +G_s^++G_t^++
       G_{a,1}^+(\text{intersected force interval}).
 \tag{8}
\]
Both the old and new upper bounds are recorded; their minimum is a
valid bound. No improvement or sign is presumed.

This is one fixed rational computation, with no new analytic values,
cotangent boxes, root solves, optimizers, input subdivisions, alternate
families or retries. The proposed fresh output is
repro/results/research-mixed-terminal-stationary-force-transport.json.
It supplies an independent constraint for the terminal-four factorial
alternative, not a new finite-source theorem or a claim about the other
terminal profiles. That alternative has since been resolved by the
[shared-force vertex comparison](research_mixed_terminal_uniform_main_comparison.md).
The present checker remains unrun; no additional calculation is needed
to establish the already completed main comparison. The other profiles'
source hypotheses and the cofinite objective remain separate.
