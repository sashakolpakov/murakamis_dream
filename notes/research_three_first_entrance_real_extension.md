# A larger real interval and a sharper bound for the next boundary sum

Research proof, 4 November 2026. The manuscripts are unchanged.

The preceding attachment theorem gives the original finite function
\(v(w)^TA_N^3h(y)\) on a complex disk. Here we extend its asymptotic
to a longer real interval through the center of that disk. We also
improve its bound on the entire real period. These two improvements
are useful for further attachments: the local formula controls the
contribution near the critical point, while the full-period bound
controls everything that might otherwise cancel it.

## 1. The finite function and the statement

Keep the matrices, carriers and phase from
[the preceding attachment theorem](research_three_first_entrance_source.md).
In particular,
\[
 A_N=JM^3,\qquad \widetilde A_N=A_N-E_{\lfloor N/40\rfloor},
 \qquad x_h=\frac16+\frac{i\log2}{2\pi},\qquad R=\frac1{200}.
 \tag{1}
\]
The function before restoring the deleted corner is
\[
 F_{2,N}(y,w)=v(w)^TA_N^2\widetilde A_Nh(y)
  =N\int_{x_h-1/2}^{x_h+1/2}F_{1,N}(x,w)K_N(x,y)\,dx,
 \tag{2}
\]
where \(F_{1,N}=v(w)^TA_N^2h(x)\),
\(K_N(x,y)=h(x)^T\widetilde A_Nh(y)\), and \(w=-2\)
is the complete ordinary outside color. Set
\[
 \mathcal U=\{|y-x_h|\le R\}
       \cup\{x_h+u:u\in\mathbb R,\ |u|\le9/1000\}.
 \tag{3}
\]

**Theorem 1.** On a neighborhood of
\(\mathcal U\times\{-2\}\),
\[
 F_{2,N}(y,w)=C_{N,3}\kappa^2N^{-1}\mathcal A_2(y,w)
                  e^{NS_2(y,w)}(1+O(N^{-1})),
 \qquad \mathcal A_2(y,w)\ne0.
 \tag{4}
\]
The same formula holds for the original undeleted function
\(v(w)^TA_N^3h(y)\). The error is uniform and holomorphic;
both level parities and each fixed ordinary outside-color derivative
are included, on a smaller neighborhood for the derivative estimates.

Write \(k_0=(4\pi/21)(2\sqrt3-3i)\),
\(M_2=\Re S_2(x_h,-2)\), and
\[
 \frac{S_2'(x_h+z,-2)}{k_0}=-\sqrt{21}z+h_2(z).
\]
Then
\[
 |h_2(0)|<.0057,\qquad \sup_{x_h+z\in\mathcal U}|h_2'(z)|<.18.
 \tag{5}
\]
The full real period satisfies the stronger bound
\[
 |F_{2,N}(x_h+t,-2)|\le CN^b
 \exp N\left\{M_2+|k_0|(.0057)v(t)-\frac{29}{20}v(t)^2\right\},
 \qquad
 v(t)=\min\{\operatorname{dist}(t,\mathbb Z),.03\}.
 \tag{6}
\]
Every fixed ordinary outside-color derivative at \(w=-2\) obeys
the same exponential bound (6), with its own polynomial prefactor.
The undeleted function satisfies these bounds as well. This theorem does not
assert that (4)--(6) are preserved by another attachment; that is
a separate induction problem.

## 2. The actual center and real critical branch

Put \(D=5+\sqrt{21}\), \(M_1=\Re S_1(x_h,-2)\), and let
\(z_c(y)\) be the critical input in (2). The existing
[three-variable critical-point certificate](research_three_entrance_critical_branches.md)
encloses \(z_c(x_h)\) without replacing the original source phase.
For \(d=z_c(x_h)-x_h\), the uniform Hessian defect on the disk gives
\[
 \Re\{S_2(x_h)-S_1(x_h)-2c\}
 \ge \frac12\Re(k_0D d^2)-\frac3{10}|k_0||d|^2>-.000066.
 \tag{7}
\]
Indeed, for \(T(z)=S_1(x_h+z)+\Phi(x_h+z,x_h)\),
\(T'(d)=0\) and
\[
 T(d)-T(0)=-d^2\int_0^1 sT''(sd)\,ds,
 \qquad |T''/k_0+D|<.6.
\]
This proves (7) directly from the certified center and the written
Hessian bound. No numerical dilogarithm subtraction is needed.
The exact outgoing derivative is \(\Phi_y(z_c(x_h),x_h)\).
Evaluating this algebraic-logarithmic expression on the same enclosure
gives
\[
 |\Re S_2'(x_h)|<.00215,\qquad |S_2'(x_h)/k_0|<.0057.
 \tag{8}
\]

The [real-output critical-branch proof](research_three_first_entrance_real_critical.md)
continues this same point over \(|u|\le.009\), keeping the critical
input strictly inside \(|z-x_h|<R\). It proves
\[
 9.3<-\Re S_2''(x_h+u)<9.8,\qquad |h_2'(u)|<.18.
 \tag{9}
\]
On the complex disk the derivative bound was already established.
Equations (7)--(9) give a lower bound for the real output phase:
\[
 \Re S_2(x_h+u)\ge M_1+2c-B_{\rm real},\qquad
 B_{\rm real}=.000066+.00215(.009)+4.9(.009)^2=.00048225.
 \tag{10}
\]

## 3. The central contour and its neighboring real intervals

Only the real extension in (3) needs proof. For such an output, move
the central input segment from \(x_h-R\) to \(x_h+R\) onto the
two straight segments through \(z_c(y)\), with the original endpoints
fixed. The critical input and both segments lie in the true input
disk. The incoming finite-source asymptotic is valid there.
The kernel asymptotic on these segments follows from
[the input-rectangle theorem](research_three_vertex_input_rectangle.md)
and the exact symmetry \(K_N(x,y)=K_N(y,x)\). This is a symmetry
of the retained finite matrix, whose original corner deletion is
symmetric, as recorded in
[the closure proof](research_three_small_source_closure.md).
It is not an inference from a symmetric limiting phase.

The Hessian defect along either segment is bounded by
\[
 |(S_1''+\Phi_{xx})/k_0+D|
       <\frac12+18(.005+.009)=.752.
 \tag{11}
\]
Here the kernel estimate is the existing cubic-phase estimate,
used by symmetry on \(|x-x_h|\le.005,|y-x_h|\le.009\).
For \(d_\pm=\pm R-(z_c(y)-x_h)\), the real critical certificate
proves
\[
 \Re(k_0D d_\pm^2)-.752|k_0||d_\pm|^2>5\cdot10^{-7}.
 \tag{12}
\]
Integrating the Hessian twice therefore bounds each real endpoint
below the critical value by more than \(2.5\cdot10^{-7}\).
It also gives strict decrease along both contour segments.
Their real displacements have opposite signs, so they belong to
opposite Gaussian convergence sectors. The resulting coefficient is
the full nonzero coefficient in (4), with the square-root branch
continued from the disk theorem.

For \(R\le|t|\le.01\), the wider
[actual kernel theorem](research_three_vertex_real_input_union.md)
and the incoming real principal term both apply. Set
\(T(t,u)=S_1(x_h+t)+\Phi(x_h+t,x_h+u)\).
The real endpoint derivatives point outwards:
\[
 \Re T_t(-R,u)>0,\qquad \Re T_t(R,u)<0.
 \tag{13}
\]
For an explicit bound, the incoming real curvature exceeds \(9.3\),
its central real slope is at most \(P_1=.0113\), and the kernel
gradient is its linear part plus an error of modulus at most
\(9|k_0|(R+.009)^2\). Both inequalities in (13) follow from
\[
 9.3R-P_1+5(\Re k_0)R-2(\Re k_0)(.009)
                  -9|k_0|(R+.009)^2>0.
 \tag{14}
\]
The factor \(\Re k_0\) in the mixed linear term is justified
because both displacements are real.
An outward rectangular cover of the exact selected kernel Hessian
gives \(-\Re\Phi_{xx}>9.4\) for real input displacement at most
\(.02\) and real output displacement at most \(.009\).
Consequently \(-\Re T_{tt}>18.7\) on the annuli.
Together with (12)--(14), this proves a strict gap for their entire
principal contributions.

## 4. The rest of the original period

The incoming real expansion retains its absolute error separately:
\[
 |F_{1,N}(x_h+t,-2)|\le CN^b
 \left[e^{N(M_1+.0113|t|-4.65t^2)}+e^{1.9107N}\right],
 \qquad |t|\le.02,
 \tag{15}
\]
and \(M_1>1.9113\). For \(|t|\ge.02\), measured on the
real period, its global bound has rate at most \(1.91115\).
These are estimates for the original finite incoming function.

Use the joint kernel bound with input cap \(.04\) and real output.
It has rate at most \(2c-(3/2)\min\{|t|,.04\}^2\).
The difference between each remaining upper rate and the output
phase in (10) is bounded by the following strict comparisons:
\[
 \begin{array}{c|c}
 \text{contribution}&\text{lower bound for its gap}\\ \hline
 \text{principal term, } .01\le|t|\le.02
   &6.15(.01)^2-.0113(.01)-B_{\rm real}>.000019\\
 \text{absolute error in (15)}
   &.0006-B_{\rm real}>.000117\\
 \text{remaining period, } |t|\ge.02
   &.00015+1.5(.02)^2-B_{\rm real}>.000267.
 \end{array}
 \tag{16}
\]
The quadratic loss in the first row increases with \(|t|\) on
the specified interval. The second row applies wherever (15) is
used, including the near annuli; it does not assume that the incoming
principal term dominates its absolute error everywhere.

The central stationary-phase integral and these strict complementary
gaps prove (4) on the real interval. The original carriers, measure
and powers of \(N\) are the same as in the disk theorem. Restoring
the deleted corner has rate below \(2.38\), while (10) is greater
than \(2.55\), so the original undeleted function has the same
asymptotic. Strict inequalities on compact domains give an open
parameter neighborhood and the asserted holomorphic derivative bounds.

## 5. A bound on the whole real period

Use the incoming full-period bound with linear coefficient
\(P_1=.0113\) and quadratic coefficient \(29/20\), and the
two-wire kernel bound with both distance caps equal to \(.03\).
Completing the input square, and now using the sharper center
comparison (7), gives
\[
 |F_{2,N}(x_h+t,-2)|\le CN^b
 e^{N[M_2+B_2-(3/2)v(t)^2]},\qquad
 B_2=.000066+\frac{(.0113)^2}{4(29/20+3/2)}<.000077.
 \tag{17}
\]
The incoming distance cap is \(.01\). Replacing the kernel's
input distance by that smaller cap only weakens this upper bound;
the output cap remains \(.03\).

For \(|t|\le R\), the disk asymptotic and its real curvature
give
\(\Re S_2(x_h+t)\le M_2+|k_0|(.0057)|t|-4t^2\).
This implies (6) there. For \(v(t)\ge R\), the inequality
needed to deduce (6) from (17) is
\[
 B_2\le |k_0|(.0057)v(t)+\frac1{20}v(t)^2.
 \tag{18}
\]
Its right-hand side is increasing and already exceeds \(B_2\)
at \(v=R\). Thus (6) holds on the entire period, and the
negligible corner error preserves it for the undeleted source.
The positive slack in (17) has been accounted for by (18).

For the derivative assertion, differentiate the exact finite integral
before estimating it. The kernel is independent of the ordinary
outside color. Corollary 4 and Proposition 3 of the incoming real-output
theorem explicitly retain every fixed derivative with the same
exponential rate. Hence the square completion giving (17) applies to
each derivative. On the small interval, differentiate the already
holomorphic packet (4); fixed derivatives of its phase and normalized
remainder cost only powers of \(N\) at the complete color. The same
comparison (18) finishes the full-period bound. This is a statement
about fixed derivatives at the complete color, not an assertion that
(6) holds throughout a fixed outside-color neighborhood.

## 6. Reproduction and scope

The scalar comparisons, the sharper center estimates and the exact
\(320\times144\) real-parameter cover of the kernel curvature are
checked by
`experiments/check_three_first_entrance_real_budgets.py`.
The incoming real expansion, the kernel's finite contour, and the
critical-input sectors each have separate proofs and interval covers
cited above. The new bounds do not by themselves establish a closed
class under arbitrary further attachments. In particular they do not
assert the volume conjecture for all short chains or finitely many
exceptional assignments for a general template.
