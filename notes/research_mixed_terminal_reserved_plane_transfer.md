# Joining terminal terms that retain a strict reserve

Research deduction, 6 November 2026. The existing horizontal terminal
plane is too large to prove the joint main comparison by itself. It
can nevertheless control terminal terms that lie substantially below
that plane. The neighboring ordinary factor retains enough curvature
to bound the excess of the joined plane. This note gives a sufficient
criterion using the original reference and the same selected height
for both Fourier alternatives. It makes no new analytic evaluation.

## 1. The plane and the original allocation

Use the original ordinary phase
\[
 Q_1(s;b,a)=g(s+b)+g(s+a)-3g(s)-g(b)-g(a)+2\pi ibs
 \tag{1}
\]
and terminal action \(P_\epsilon\), with incoming flag
\(\beta\in\{0,1\}\) and terminal flag \(\epsilon\in\{0,1\}\).
Let \((b_*,s_*,a_*,t_*,v_*)\) be an original stationary reference,
\(a_*=A+ic\), and put
\[
 \Pi=P_\epsilon-g/2,\qquad p_T=\Pi'(a_*),\qquad
 B_T(y)=\Re\Pi(a_*)+\Re p_T(y-A)-\kappa(y-A)^2,
 \quad\kappa=1/2500000.
 \tag{2}
\]
The original full action \(M_*\) and incoming marginal \(p_*\)
are those in the [joint-main comparison](research_mixed_terminal_joint_main_budget.md).
In particular
\[
 Q_{1,a}(s_*;b_*,a_*)+p_T-\tfrac12g'(a_*)=0.
 \tag{3}
\]
The hypotheses include the source scope of the existing selected
terminal theorems, explained for canonical suffixes in
[the horizontal-envelope diagnostic, Section 2](research_mixed_terminal_horizontal_envelope_diagnostic.md).
For type four this includes the original oriented input condition.

Keep the original \(b,s\) heights, set \(H=1/100\), and let
\(b_R,a_R\in P=[.22,.45]\), \(s_R\in[.125,.5]\).
For \(\nu=0,1\), the joined plane has exact defect
\[
 E_\nu=B_T(a_R)+\Re Q_1(s;b,a)
 -\frac\beta2\Re g(b)-\frac\nu2\Re g(a)-\pi\nu H
 -\Re\{M_*+p_*(b-b_*)\},\qquad a=a_R+iH.
 \tag{4}
\]
Both alternatives in this note keep all of \(P\).
The selected modulus is split into two equal halves. Each half has
upper rate \(\max\{-\Re g(a)/2-\pi H,0\}\). Splitting the
modulus does not assert a holomorphic square root or change the source.
The common maximizing alternative suffices for the product; all
actual Fourier summands remain present.

Suppose a terminal profile \(T(a;\mathbf x)\), with its original
penalties, satisfies
\[
 T(a;\mathbf x)+\max\{-\Re g(a)/2-\pi H,0\}
                       \le B_T(a_R)-\rho .
 \tag{5}
\]
Then its full joint defect, with either complete selected-weight
alternative, is at most \(E_\nu-\rho\). Indeed the terminal half
of that alternative is no larger than the maximum in (5), and the
remaining ordinary half is exactly the term in (4). Thus a positive
upper bound for \(E_\nu\) is useful whenever it is smaller than
\(\rho\). This implication does not compare the plane to the
selected-height terminal main maximum.

## 2. Centered value, forces and two convex costs

Write \(\Delta=H-c\), \(\bar a=A+iH\), and
\[
 \mathcal B(z)=g(z+i\Delta)-g(z)-i\Delta g'(z),\qquad
 L_z=g'(z+i\Delta)-g'(z).
 \tag{6}
\]
At the lifted reference \((b_*,s_*,\bar a)\), (3) gives the
following exact values and horizontal forces:
\[
\begin{split}
 J_1&=\Delta\Im p_T+
       \Re\{\mathcal B(s_*+a_*)-\tfrac32\mathcal B(a_*)\}-\pi H,\\
 J_0&=J_1+\tfrac12\Re g(\bar a)+\pi H,\\
 G_s&=\Re L_{s_*+a_*},\\
 G_{a,1}&=\Re\{L_{s_*+a_*}-\tfrac32L_{a_*}\},\qquad
 G_{a,0}=G_{a,1}+\tfrac12\Re g'(\bar a).
\end{split}
 \tag{7}
\]
The force in \(b_R\) is zero. Its full original marginal was
subtracted in (4). The quadratic term in (2) has zero value and
first derivative at this trial.

Retain the height and coordinate hypotheses of
[the three-cost theorem](research_mixed_terminal_joint_main_curvature_budget.md),
equations (1) and (13), wherever they concern \(b,s,a\).
The original index barrier restricts every maximum of (4) to
\(s_R\ge.22\); the terminal plane and weights do not depend on
\(s\). The ordinary pair lemma, with
\(g_h(x)=\Re g(x+ih)\), gives in coordinates \((b_R,s_R,a_R)\)
\[
 -E_\nu''\succeq
 \operatorname{diag}\left(
 \tfrac{1+\beta}{2}g_{h_b}''(b_R),\quad
 g_{h_s}''(s_R),\quad
 \tfrac{1+\nu}{2}g_H''(a_R)\right).
 \tag{8}
\]
The extra \(2\kappa\) in the last diagonal is discarded.
This is a simultaneous matrix inequality, retaining all cross terms
of the original ordinary phase.

Assume in addition
\[
 G_s>0,\qquad G_{a,1}<0,\qquad G_{a,0}>0,\qquad
 d=\tfrac12-\Re s_*>0.
 \tag{9}
\]
Integrating (8) from the lifted reference and applying the scalar
estimates already proved in the three-cost theorem gives
\[
\begin{split}
 \sup E_1&\le J_1+\frac{15G_s^2}{128d}+\frac{G_{a,1}^2}{4},\\
 \sup E_0&\le J_0+\frac{15G_s^2}{128d}+G_{a,0}(.45-A).
\end{split}
 \tag{10}
\]
For the first line, the negative selected force restricts its scalar
maximum to \(.22\le a_R\le A<.314\). There \(g_H''>2\),
and its coefficient in (8) is one. The scalar gain is therefore at
most \(G_{a,1}^2/4\). For the second line discard the nonnegative
selected convex remainder and keep its full-interval affine support.
The boundary cost is nonnegative and has zero force. The selected
center is inside \(P\), so no signed support has been replaced by
a zero truncation.

## 3. A rational criterion that pays the known reserves

The following additional guards suffice:
\[
\begin{gathered}
 .28<\Re s_*<.314,\quad |h_s|<.061,\quad
 .28<A<.314,\quad 0<G_s<.141,\\
 J_1<19/500,\quad -127/1000<G_{a,1}<0,\qquad
 J_0<3/500,\quad 0<G_{a,0}<33/200.
\end{gathered}
 \tag{11}
\]
Together with the standing reference and height conditions these
give
\[
\begin{split}
 \sup E_1&<\frac{19}{500}+\frac{19881}{1587200}
                         +\frac{16129}{4000000}<\frac{11}{200},\\
 \sup E_0&<\frac3{500}+\frac{19881}{1587200}
                         +\frac{561}{20000}<\frac{11}{200}.
\end{split}
 \tag{12}
\]
All quantities in (7) are in the existing four-reference diagnostic
and the earlier saved terminal-marginal record. No terminal action
value, new primitive evaluation or new critical-point solve is needed
to check (11). Application to those four references still requires
an exact check of the saved endpoints and their source associations.

The selected-height terminal proofs give the following raw reserves
in the precise sense of (5):

* Every regular penalized alias endpoint has \(\rho>59/1000\).
  The twelve original families include a freely real other index at
  height zero, that index at its original main height, and double
  aliases. They therefore include all sixteen labels of the
  25-label regular compiler having at least one alias coordinate,
  including restrictions at the other coordinate's real cut.
  See [type three, Section 4](research_mixed_terminal_three_selected_height_completion.md)
  and [type four, Section 2](research_mixed_terminal_four_selected_height_completion.md).
* The constant profile \(879/1000\) has \(\rho>63/1000\).
  This follows from the bare plane lower bound \(.99\), the
  halfweight-change upper bound \(.048\), and horizontal convexity
  of \(\Re g\), as proved in
  [the terminal end-index estimate, Section 2](research_mixed_terminal_three_selected_height_completion.md).
  Its argument applies to both terminal types.

Consequently, whenever (11) holds, every such alias label has full
joint deficit greater than \(1/250\), and the constant profile
has deficit greater than \(1/125\), on the entire original real
target product at \(H=.01\). These bounds hold for each complete
selected alternative. Arbitrarily small asymptotic tolerances and
polynomial factors can be absorbed, for example leaving gaps
\(1/500\) and \(1/250\), respectively, for the represented finite
contributions on a sufficiently small fixed ordinary-color disk.

This conclusion concerns the penalized endpoint profiles. A vertical
alias side also has an endpoint at height zero, controlled by one of
the regular real-cut profiles. Those profiles have not been bounded
by (12). Thus this theorem does not yet suppress the entire alias
integral. After these comparisons and the main comparison, eight
regular real-cut profiles and the physical-triangle entropy profile
still require joint estimates, as does uniformity in the incoming
parameter. No complete terminal-source or knot asymptotic follows
from the criterion alone.
