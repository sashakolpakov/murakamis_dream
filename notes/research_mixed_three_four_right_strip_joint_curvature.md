# Joint curvature beyond the ordinary three-four plateau

Research deduction, 7 November 2026. The full reduced terminal phase
remains horizontally concave when its incoming real coordinate
extends from \(9/20\) to \(1/2\). This holds on the original
private and transform rectangles, with all their allowed heights.
For the ordinary \((3,4)\) pair it bounds the terminal main
rectangle, multiplied by the complete first cap, strictly below
the geometric action on that added interval.

This is a source-sector estimate. The other terminal currents and
physical rows still require their own comparisons. No numerical
evaluation is used.

## 1. A triangle curvature bound on the full index rectangle

Put
\[
 V(z,w)=g(z+w)-g(z)-g(w),\qquad
 C(z)=\Re\cot(\pi z),\qquad g''(z)=\pi\cot(\pi z)-\pi i.
\]
Retain the actual terminal index ranges
\[
 t\in[.15,.5]+i[-.12,.12],\qquad
 e\in[.27,.49]+i[-.055,.04].
 \tag{1}
\]
All derivatives in this section vary real parts while holding
imaginary parts fixed. Direct differentiation gives
\[
 -\pi^{-1}\Re V''(t,e)
  =C(t)\,dt_R^2+C(e)\,de_R^2
                         -C(t+e)(dt_R+de_R)^2 .
 \tag{2}
\]

**Lemma 1.** The quadratic form (2) is positive semidefinite
on (1). If \(\Re(t+e)<1/2\), it is bounded below by
\((4/75)(dt_R^2+de_R^2)\).

*Proof.* If \(\Re(t+e)\ge1/2\), then
\(C(t+e)\le0\) and \(C(t),C(e)\ge0\); this proves
the first assertion in that region.

Otherwise \(.15\le t_R<.23\) and \(.27\le e_R<.35\).
The elementary formula
\[
 C(x+ih)=\frac{\sin(2\pi x)}
                     {\cosh(2\pi h)-\cos(2\pi x)}
 \tag{3}
\]
implies
\[
                C(t)>\frac45,\qquad C(e)>\frac{12}{25},
                     \qquad C(t+e)<\frac4{15}.
 \tag{4}
\]
Here are bounds proving these three comparisons uniformly.

On \(.15\le x\le.23\), expression (3) decreases as \(x\)
increases: its derivative has the sign of
\(\cosh(2\pi h)\cos(2\pi x)-1\), which is negative since
\(\cosh(.24\pi)<4/3\) and \(\cos(.3\pi)<3/4\).
It also decreases with \(|h|\). Therefore
\[
 C(t)\ge\frac{\sin(.46\pi)}
                   {\cosh(.24\pi)-\cos(.46\pi)}
      >\frac{99/100}{4/3-3/25}
      =\frac{297}{364}>\frac45 .
\]
The guards follow from
\(\sin(.46\pi)=\cos(.04\pi)>99/100\) and
\(\cos(.46\pi)=\sin(.04\pi)>3/25\).

On \(.27\le x\le.35\), the cosine in (3) is negative,
so the same monotonicity holds. Thus
\[
 C(e)\ge\frac{\sin(.7\pi)}
                   {\cosh(.11\pi)-\cos(.7\pi)}
       >\frac{4/5}{16/15+3/5}=\frac{12}{25}.
\]
Finally \(.42\le\Re(t+e)<.5\), so
\[
 C(t+e)\le\cot(.42\pi)=\tan(.08\pi)<\frac4{15}.
\]

These guards need no trigonometric evaluation. Use
\(157/50<\pi<22/7\) and the elementary Taylor bounds
\[
 \sin u\ge u-u^3/6,\qquad
 1-u^2/2\le\cos u\le1-u^2/2+u^4/24
                         \quad(0\le u\le1).
\]
They give the displayed sine and cosine bounds directly.
For the hyperbolic cosines use
\[
 \cosh u\le1+\frac{u^2}{2(1-u^2/12)}
                          \quad(0\le u<\sqrt{12}),
\]
with \(u=19/25>.24\pi\) and \(u=7/20>.11\pi\).
The resulting rational bounds are less than \(4/3\) and
\(16/15\), respectively. Also
\(\tan(.08\pi)\le (44/175)/(1-(44/175)^2/2)<4/15\).

Let \(B=\operatorname{diag}(4/5,12/25)\).
By Cauchy--Schwarz,
\[
 \frac4{15}(u+v)^2
 \le\frac4{15}\left(\frac54+\frac{25}{12}\right)
                         \left(\frac45u^2+\frac{12}{25}v^2\right)
 =\frac89 (u,v)B(u,v)^T.
\]
Equations (2)--(4) therefore leave at least
\(\frac19 B\succeq\frac4{75}I\), as claimed.
\(\square\)

## 2. Concavity of every regular terminal profile on the added interval

The complete reduced phase is
\[
 \Phi(a;t,e)=S(e)+V(a,t)+V(e,t)-g(t)
                    -\frac{\pi i}{2}(e-e^2)+2\pi iat .
 \tag{5}
\]
Here \(S(e)\) is the action of the whole original endpoint
coefficient. The
[endpoint Schur calculation](research_mixed_cap_outer_contour_reduction.md),
equation (8), gives \(-\Re S''(e)>0\) throughout (1).
It uses the original auxiliary critical branch.

**Proposition 2.** Fix any incoming height \(c\) in the
actual type-three range \((-.072,.021)\), and any index
heights in (1). The real part of (5) is jointly concave
in \(a_R,t_R,e_R\) on
\[
 [9/20,1/2]\times[.15,.5]\times[.27,.49].
 \tag{6}
\]
It has the continuous limiting real phase at \(a+t=1\)
if that corner is reached.

*Proof.* On (6), \(.6\le\Re(a+t)\le1\).
Except at the indicated numerator corner, the negative
real Hessian of \(V(a,t)\) is positive semidefinite:
the form is as in (2), with \(C(a),C(t)\ge0\) and
\(C(a+t)\le0\). Lemma 1 gives the same assertion for
\(V(e,t)\). The remaining terms supply
\(-\Re S''(e)\,de_R^2+\pi C(t)\,dt_R^2\), which is
nonnegative. The two imaginary quadratic polynomials
have zero real Hessian in the real coordinates.
Adding these forms proves concavity in the interior.
The primitive is continuous at the numerator corner;
the concavity inequality extends there by limits.
\(\square\)

This proposition also applies when some coordinates are fixed
at real cuts or alias heights. Their sampling penalties are
constant in the real variables. It provides curvature, not
the calibrated comparison for every such profile.

## 3. The main rectangle with the complete first cap

Use the actual ordinary-pair reference
\[
 a_*=A+ic,\quad t_*=T+ih_t,\quad e_*=E+ih_e,
\]
where the
[endpoint rectangles](research_mixed_open_word_endpoint_rectangles.md)
give \(A<.391\). Let
\[
 p=\Re P_1'(a_*),\quad M=\Re\{T_0(a_*)+P_1(a_*)\},
 \quad b=9/20,\quad \kappa_*=\frac1{2500000}.
\]
The original shared critical equation is
\(T_0'(a_*)+P_1'(a_*)=0\).
Define
\[
 f(x)=\max_{\substack{.15\le u\le.5\\ .27\le v\le.49}}
       \Re\Phi(x+ic;u+ih_t,v+ih_e).
 \tag{7}
\]
On \(A\le x\le b\), the
[original reduced-current Hessian](research_mixed_terminal_four_reduced_currents.md)
has negative real part at least \((\pi/100)I\).
The maximum at \(x=A\) is the actual internal stationary
point, so
\[
 f(A)=\Re P_1(a_*),\qquad f'_+(A)=p,\qquad
 f(b)\le\Re P_1(a_*)+p(b-A)-\frac{\pi}{200}(b-A)^2.
 \tag{8}
\]
The last inequality also follows by applying the full quadratic
tangent bound before taking the maximum over \(u,v\).

Proposition 2 joins this concavity to the old interval.
Maximizing a jointly concave function over the same convex
compact index rectangle preserves concavity in \(x\).
Thus every right derivative after \(A\) is at most \(p\),
and
\[
 f(x)\le \Re P_1(a_*)+p(x-A)-\frac{\pi}{200}(b-A)^2,
                         \qquad b\le x\le1/2 .
 \tag{9}
\]

The [complete first-cap extension](research_mixed_cap_upper_target_completion.md)
bounds the whole \(U_{0,N}\) on this interval by the rate
\[
 B_U(x)=\Re T_0(a_*)-p(x-A)-\kappa_*(x-A)^2 .
\]
It follows that
\[
 B_U(x)+f(x)
 \le M-\frac{\pi}{200}(b-A)^2-\kappa_*(x-A)^2
                         <M-\frac1{20000}.
 \tag{10}
\]
For the last comparison, \(b-A>59/1000\) and \(\pi>3\)
give \(3\cdot59^2>10000\) after clearing denominators.

The literal terminal main component is the two-index horizontal
integral of the original reduced interpolant, at heights
\(h_t,h_e\), with all original normalizations retained.
Its uniform compact symbol and the zero-safe numerator shift
at \(a+t=1\) give a polynomial prefactor times \(e^{Nf(x)}\).
The finite-product justification at that corner is the same
one-sided estimate written in Section 5 of
[the private-left extension](research_mixed_three_four_private_left_right_extension.md);
it divides by no vanishing numerator. Inward half-grid cuts
change the upper rate by at most \(O(\log N/N)\).

Consequently this entire horizontal main component, multiplied
by the complete first cap, is bounded by
\[
                 C N^B e^{N(M-1/40000)}
                         \qquad(9/20\le x\le1/2).
 \tag{11}
\]
The bound holds on sufficiently small fixed ordinary-color
neighborhoods, with every fixed ordinary-color derivative,
at both level parities. One total small exponential tolerance
in (10) pays those perturbations and the polynomial factors.

Equation (11) does not include the terminal aliases, vertical
joins or physical complement. Those are distinct pieces of
the exact finite source. Nor does it change the incoming height
or bound the rest of the circle. It supplies one previously
missing regular-sector estimate with the actual geometric
action and the whole first cap retained.

