# Three retained convex costs for the terminal joint main phase

Research deduction, 6 November 2026. The coupled ordinary and terminal
main phase retains three scalar Bregman costs after all other real
targets remain free. These costs remove the positive affine-support
loss at the four saved canonical suffixes: elementary rational bounds
give a factorial main gap greater than \(1/800\), without another
primitive evaluation, reference solve or target optimizer. This is a
main-profile result at those four references, not a complete terminal
source comparison or a theorem on the entire reference domain.

The convex remainder and gradient-squared-over-curvature estimate are
standard; see Boyd and Vandenberghe,
[Convex Optimization, Section 9.1.2](https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf)
and the [corresponding strong-convexity slide](https://see.stanford.edu/materials/lsocoee364a/10UnconstrainedMin.pdf),
page 10-3. The new content here is the original-source residual
concavity, its legitimate target domain, and the exact scalar budget.
The proof below is self-contained rather than using that citation
as a proof dependency.

## 1. The original objective and justified target restriction

Use exactly \(D_\nu,T_\nu,A_s,A_t,A_{a,\nu}\), the original
action and incoming complex marginal from
[the joint-main theorem](research_mixed_terminal_joint_main_budget.md).
The preceding own flag is one, the incoming flag is
\(\beta\in\{0,1\}\), and the terminal flag is
\(\epsilon\in\{0,1\}\). The selected height is \(H=.01\).
The factorial alternative \(\nu=1\) keeps \(a_R\in P=[.22,.45]\);
the forced alternative \(\nu=0\) keeps \(a_R\in I_0=[.4,.45]\)
by the complete-weight dominance theorem. No weight is divided out.

Assume the original main heights satisfy
\[
 \begin{split}
 h_b&\in[-.078,.021],\qquad h_s\in[-.102,-.001],\\
 (h_t,h_v)&\in[-.072,.021]\times[.049,.077]
                                      &&(\epsilon=0),\\
 (h_t,h_v)&\in[-.108,-.020]\times[-.051,-.019]
                                      &&(\epsilon=1).
 \end{split}
 \tag{1}
\]
Here \(v=\xi\) for terminal type three and \(v=e\) for type four.
These are the original endpoint image ranges, not independent new
endpoint solutions. They include the four saved canonical references.

Both joint main maxima can be restricted to
\[
 \mathcal Q_\nu=P_b\times[.22,.5]_s\times I_\nu{}_a
                  \times[.18,.5]_t\times V_\epsilon{}_v,
 \quad I_1=P,\quad V_0=[.1,.4],\quad V_1=[.27,.49].
 \tag{2}
\]
All heights remain fixed as in the joint-main theorem. For \(s\),
map the incoming and selected arguments in Proposition 2 of
[the second-selection index barrier](research_mixed_second_selected_horizontal_concavity.md)
to \(b,a\). The derivative is exactly
\(Q_{1,s}=g'(s+b)+g'(s+a)-3g'(s)+2\pi ib\), including its
incoming chirp. The proof uses only the heights in (1), the two
outer real targets in \(P\), and the selected nonnegative height.
No terminal term depends on \(s\). For \(t\), use the
pointwise marginal inequalities in the
[type-three](research_mixed_terminal_three_selected_height_completion.md),
equation (15), and [type-four](research_mixed_terminal_four_selected_height_completion.md),
equations (7)--(8), selected-height proofs. Their whole private real
intervals and main heights are precisely those in (1)--(2).
They increase every \(t_R<.18\) to \(.18\). The other ordinary
factor and weights are independent of \(t\). These are legitimate
optimizer restrictions on the original main product; no alias or
real-cut current is being assigned a main-index barrier.

## 2. A terminal private-pair reserve

Write \(V(x,y)=g(x+y)-g(x)-g(y)\), and define
\[
 \begin{split}
 R_0(v)&=-2J(.5-v)-2J(v)-g(v)+i\pi v,\\
 R_1(v)&=S(v)-i\pi(v-v^2)/2.
 \end{split}
 \tag{3}
\]
The original terminal phases decompose exactly as
\[
 \Phi_\epsilon(a;t,v)=V(t,a)+V(t,v)-g(t)
                                  +R_\epsilon(v)+2\pi iat.
 \tag{4}
\]
All branches and complex constants are unchanged.

**Lemma 1.** On the main-height products (1)--(2), both
\(-\Re V(t,a)''\) and
\(-\Re\{V(t,v)+R_\epsilon(v)\}''\) are positive semidefinite.
Consequently the terminal Hessian retains the whole scalar cost
\(\Re g(t)\) in addition to these nonnegative matrices.

*Proof.* For an individual coordinate \(z=x+iy\),
\[
 |\Im\cot\pi z|<1
 \quad\Longleftrightarrow\quad
 \cos(2\pi x)<e^{-2\pi|y|}.
 \tag{5}
\]
For \(t_R\ge.18\), \(|h_t|\le.108\), the right side
exceeds \(1/2\), while the left side is at most
\(\cos(.36\pi)=\sin(.14\pi)<.44<1/2\).
The exponential bound follows from
\(.216\pi<17/25\) and the exact \(e^{17/25}<2\)
witness in [the original shape-sector lemma](research_mixed_reference_shape_half_plane.md).
The coordinate \(a_R\in P\), \(h_a=.01\), satisfies (5)
as well. The [cotangent-pair identity](research_mixed_pair_curvature_composition.md),
Proposition 1, therefore gives positivity of the first pair, including
\(t_R=.5\), where its individual real cotangent is zero.

For \(\epsilon=1\), \(v_R=e_R\in[.27,.49]\) has negative
doubled-angle cosine, so it also satisfies (5). The same pair result
applies to \(V(t,e)\). The original broad cap theorem, equation (9)
of [the cap plateau phase proof](research_mixed_first_cap_plateau_phase.md),
gives \(-\Re S''>\pi/43\) on the whole required cap rectangle.
The remaining imaginary quadratic in \(R_1\) has zero real Hessian.
This proves the assertion without importing the stronger private-cap
bound from its smaller \([.3,.4]\) real interval.

For \(\epsilon=0\), set
\(p=\Re\cot\pi t\), \(q=\Re\cot\pi v\),
\(r=\Re\tan\pi v\), and \(C=\Re\cot\pi(t+v)\).
The normalized negative real Hessian of the second expression is
\[
       \begin{pmatrix}p-C&-C\\-C&4q+2r-C\end{pmatrix}.
 \tag{6}
\]
Here \(p\ge0\), \(q,r>0\). If \(C\le0\), (6) is a
nonnegative diagonal plus a nonnegative rank-one matrix.
If \(C>0\), then \(t_R+v_R<.5\), so
\(t_R<.4\), \(v_R<.32\). We claim
\[
                         p>3C/2,\qquad q>C.
 \tag{7}
\]

For the first claim, \(\cosh(2\pi h_t)<9/8\). Put
\(z=\cot(\pi t_R)\) and \(k=\cot(\pi/10)\), so
\(0<z<8/5\), \(0<k<31/10\). Then
\[
 p>\frac{16z}{z^2+17},\qquad
 C\le\cot\pi(t_R+.1)=\frac{zk-1}{z+k}.
 \tag{8}
\]
The numerator of twice the difference after clearing positive
denominators is
\[
 P(z,k)=-3kz^3+35z^2-19kz+51.
 \tag{9}
\]
It decreases with \(k\). At \(k=31/10\), its derivative
in \(z\) has negative leading coefficient and discriminant
\(70^2-4(279/10)(589/10)<0\). Thus
\(P(z,k)>P(8/5,31/10)=5167/625>0\), proving the first claim.
For explicit trigonometric witnesses, use
\(x=1413/2500<.18\pi\) in
\(8(x-x^3/6)-5(1-x^2/2+x^4/24)>0\), and
\(x=157/500<\pi/10\) in
\(31(x-x^3/6)-10(1-x^2/2+x^4/24)>0\).
Their rational values are respectively
\(3639318425413/62500000000000\) and
\(3148696733/50000000000\).

For the second claim, \(\cosh(2\pi h_v)<9/8\). The function
\(\sin(2\pi x)/(9/8-\cos(2\pi x))\) has at most one
interior critical point, a maximum. Its endpoint values give
\(q>1\) on \([.1,.2]\), and \(q>1/2\) on \([.2,.32]\).
Indeed use \(\sin(.2\pi)>.58\), \(\cos(.2\pi)>.8\),
\(\sin(.4\pi)>.95\), \(\cos(.4\pi)>.3\),
\(\sin(.64\pi)>.9\), and \(\cos(.64\pi)>-.44\).
In the first interval \(C\le\cot(.28\pi)<1\).
In the second, \(C\le\cot(.38\pi)<\cot(3\pi/8)<1/2\).
These prove \(q>C\). The elementary endpoint constants follow
from the exact fifth-root trigonometric values and
\(\cos(.14\pi)>1-(.44)^2/2>.9\).

Both cosh estimates follow from
\[
 \cosh x\le1+\frac{x^2/2}{1-x^2/12},\qquad
 \frac98-\left(1+\frac{(121/250)^2/2}{1-(121/250)^2/12}\right)
                         =\frac{32591}{5882872}>0.
 \tag{10}
\]
Here \(2\pi|h_v|<121/250\), and \(2\pi|h_t|\) is smaller.
By (7), the diagonal entries in (6) exceed \(C/2\) and
\(3C\); its determinant therefore exceeds \(C^2/2\).
This finishes the type-three proof. \(\square\)

## 3. A simultaneous three-node Hessian inequality

The original ordinary decomposition is
\(Q_1=V(s,b)+V(s,a)-g(s)+2\pi ibs\).
On \(s_R\in[.22,.5]\), \(b_R,a_R\in P\), the
[ordinary pair estimate](research_mixed_selected_four_four_left_main_majorant.md),
Lemma 1, applies since all three height moduli are at most .102.
Each pair retains half the outer scalar cotangent curvature.
Add its two inequalities, Lemma 1 above, the selected factorial
term, and the unchanged incoming halfweight. In the order
\((b,s,a,t,v)\), this gives the joint matrix bound
\[
 -\Re D_\nu''\succeq
 \operatorname{diag}\left(
  \tfrac{1+\beta}{2}g_{h_b}''(b_R),\
  g_{h_s}''(s_R),\
  (\nu+\tfrac12)g_H''(a_R),\
  g_{h_t}''(t_R),\ 0\right),
 \qquad g_h(x)=\Re g(x+ih).
 \tag{11}
\]
All off-diagonal simultaneous motions remain accounted for; (11)
is not a statement only along coordinate lines.

For a coordinate with center \(x_*\) and fixed height \(h\), put
\(\phi_h(x;x_*)=g_h(x)-g_h(x_*)-g_h'(x_*)(x-x_*)\).
Integrating (11) along the full segment from the lifted reference,
and using its exact gradient \((0,A_s,A_{a,\nu},A_t,0)\), proves
\[
 \begin{split}
 \sup_{\mathcal Q_\nu}D_\nu\le T_\nu
 &+\sup_{x\in[.22,.5]}\{A_s(x-s_R^*)-\phi_{h_s}(x;s_R^*)\}\\
 &+\sup_{x\in I_\nu}\{A_{a,\nu}(x-A)
                         -(\nu+\tfrac12)\phi_H(x;A)\}\\
 &+\sup_{x\in[.18,.5]}\{A_t(x-t_R^*)-\phi_{h_t}(x;t_R^*)\}.
 \end{split}
 \tag{12}
\]
The boundary cost is nonnegative and its force is zero; the private
force is zero as well. They require no additional optimization cost.
The forced center may lie outside \(I_0\); the full connecting
segment remains inside the larger product with \(a_R\in P\).
Its signed supremum in (12) is retained, without a zero truncation.

## 4. Elementary factorial gains sufficient for the saved references

The following concrete additional hypotheses suffice:
\[
 \begin{gathered}
 .28<s_R^*<.314,\quad |h_s|<.061,\qquad
 .18<t_R^*<.35,\quad |h_t|<.066,\qquad .22<A<.314,\\
 0<A_s<.141,\quad -.255<A_t<0,\quad -.255<A_{a,1}<0,
                         \qquad T_1<-.0463.
 \end{gathered}
 \tag{13}
\]
These hypotheses supplement, and do not replace, the original
coupled reference and height conditions.

For the positive \(s\)-force, convexity restricts its scalar maximum
to \(s_R^*\le x\le.5\). On \([.28,.5]\), concavity of sine
and \(\sin(.44\pi)>49/50\) give
\(\sin(2\pi x)\ge(49/11)(.5-x)\).
Also \(\cosh(.122\pi)<27/25\). Therefore, for \(x<.5\),
\[
 g_{h_s}''(x)>
 \frac{1225\pi}{572}(.5-x)>\frac{32}{5}(.5-x).
 \tag{14}
\]
The non-strict bound extends to \(x=.5\) by continuity.
Set \(d=.5-s_R^*>93/500\), and write \(x=s_R^*+\delta\).
For \(0\le\delta\le d\), integration gives
\[
 \phi_{h_s}(s_R^*+\delta;s_R^*)
 \ge\frac{32}{5}\left(\frac{d\delta^2}{2}-\frac{\delta^3}{6}\right)
 \ge\frac{32d}{15}\delta^2.
 \tag{15}
\]
Enlarging the last quadratic maximization to the real half-line bounds
the first gain in (12) by
\[
                 \frac{15A_s^2}{128d}
                         <\frac{19881}{1587200}.
 \tag{16}
\]

For the negative \(t\)-force, only \(.18\le x\le t_R^*\)
can maximize its gain. The real cotangent decreases in \(x\) on
this interval: its derivative has the sign of
\(\cosh(2\pi h_t)\cos(2\pi x)-1<0\).
Use \(\cosh(.132\pi)<109/100\),
\(\sin(.7\pi)>161/200\), and \(\cos(.7\pi)>-59/100\)
at the larger endpoint .35. The latter two follow from
\(\sqrt5>111/50\) and the exact fifth-root trigonometric values.
Consequently
\[
 g_{h_t}''(x)>\frac{161\pi}{336}>\frac32,
 \qquad \text{third gain in (12)}\le\frac{A_t^2}{3}
                                      <\frac{867}{40000}.
 \tag{17}
\]

The negative factorial selected force restricts its scalar maximum
to \(.22\le x\le A<.314\). On that interval
\(\sin(2\pi x)>.9\), \(\cos(2\pi x)>-.4\), and
\(\cosh(.02\pi)<1.01\). Thus
\(g_H''>\pi(.9)/1.41>2\). Since its coefficient in (12) is
\(3/2\), the second gain satisfies
\[
                  \text{second gain in (12)}
                         \le\frac{A_{a,1}^2}{6}
                         <\frac{867}{80000}.
 \tag{18}
\]
For completeness, all hyperbolic estimates follow from (10).
At \(x=671/1750,363/875,11/175\), the respective rational
reserves below \(27/25,109/100,101/100\) are
\(5063368/907493975\), \(813393/301857700\), and
\(294779/36737900\). The lower sine bound in (14) follows
from \(\cos(3\pi/50)>1-(33/175)^2/2>49/50\).
For the selected cosine bound, the sine upper polynomial at
\(x=352/875>.128\pi\) is below \(2/5\) by
\(65219373927746/7693634033203125\); the sine lower bound
follows from the quadratic cosine bound at the same angle.
Only rational arithmetic and \(157/50<\pi<22/7\) are used.

**Theorem 2.** Under (1) and (13), the original factorial joint main
phase on its entire original target product satisfies
\[
 \sup D_1<-\frac{463}{10000}
          +\frac{19881}{1587200}
          +\frac{867}{40000}+\frac{867}{80000}
       =-\frac{50063}{39680000}<-\frac1{800}.
 \tag{19}
\]
The strict reserve beyond \(1/800\) is \(463/39680000\).
The proof is (12) and (16)--(18), together with the legitimate
restrictions (2). In particular no small global Hessian constant is
substituted for the much larger three directional costs.

## 5. Application and scope

All four cases of the frozen
[joint-main diagnostic](../repro/results/research-mixed-terminal-joint-main-budget-diagnostic.json),
SHA256 `2b6e9b17d1a16071c545c0ba9f9bb2502e1f18c5009fafc1212fd326d2a621f9`,
satisfy every strict inequality in (13) using their saved exact
coordinate and force endpoints. These are actual certified canonical
references from the previous reference certificate, not arbitrary
Cartesian points claimed to solve the stationary equations.
The primitive and logarithmic-force values are unchanged.
The [standalone saved-data checker](../experiments/check_mixed_terminal_joint_main_curvature_budget.py)
verifies the pinned original diagnostic and its analytic-input audit,
all height and coordinate/force guards in (1) and (13), the explicit
rational witnesses above, and the exact gain recombinations. It imports
no analytic evaluator and makes no new reference or primitive call.
Theorem 2 therefore closes the four previously unresolved factorial
main comparisons by saved-data arithmetic alone. Together with the
already proved forced main gaps greater than \(1/400\), both
main alternatives have a common gap greater than \(1/800\) at
each of the four canonical suffixes.

This does not claim finite-word realization of those suffixes,
uniformity over the external typed disks, or negativity of the other
26 terminal labels. The full original terminal source, its outer
contours and the arbitrary short-filling theorem remain separate.
The new reusable result is the simultaneous matrix allocation (11)
and its checkable three-gain criterion, not a replacement of the
entire finite source by its main phase.
