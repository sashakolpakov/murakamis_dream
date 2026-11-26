# The original Fourier-cap sheet through incoming real part one half

Research deduction, 7 November 2026. The whole uneliminated main sheet
has a calibrated horizontal upper bound when its incoming real target
extends from the plateau to \(1/2\), at its actual nonpositive height.
Only nonnegative curvature is needed on the added strip; the old
strict curvature on an initial part of each segment retains an
explicit quadratic reserve.

This proves a main-sheet estimate, without a moving-root calculation
or a new finite-source cover. Positive retained currents and the
complete compensated taper comparison are not inferred from it.

## 1. Exact phase and the added strip

Use the original correlated reference and phase of
[the bare inner contour](research_mixed_fourier_right_cap_bare_inner_contour.md):
\[
 \begin{split}
 F_\eta(s,a,q)
 &=V(s,a)+V(s,q)-g(s)-\frac{\eta}{2}g(a)
                        +2\pi ias+\ell_q(x_0),\\
 V(z,w)&=g(z+w)-g(z)-g(w),\qquad \eta\in\{0,1\},\\
 (s_*,a_*,q_*)&\text{ is the original critical reference},\\
 M_\eta&=\Re F_\eta(s_*,a_*,q_*),\qquad
 P_\eta=F_{\eta,a}(s_*,a_*,q_*),\\
 \mu&=1/1250000,\qquad \kappa=\mu/2.
 \end{split}
 \tag{1}
\]
The reference has \(F_{\eta,s}=F_{\eta,q}=0\).
Keep its heights fixed:
\[
 \begin{split}
 s&=u+ih_s,\quad 1/8\le u\le1/2,\quad -.102\le h_s\le-.001,\\
 a&=x+ic,\quad .22\le x\le1/2,\quad -.108\le c=\Im a_*\le0,\\
 q&=z+ih_q,\quad .22\le z\le.45,\quad -.102\le h_q\le-.001.
 \end{split}
 \tag{2}
\]
Thus this includes every incoming type-four reference, and the
nonpositive-height part of the incoming type-three family.
All logarithms, the cardinal constant and incoming halfweight
are the original ones.

For \(x\le.45\), Lemma 1 of the cited bare-contour proof gives
\[
                         -\Re F_\eta''\succ\mu I_3.
 \tag{3}
\]
For the added strip \(x\in[.45,.5]\), set
\[
 U=\Re\cot\pi s,\quad A=\Re\cot\pi a,\quad
 C_a=\Re\cot\pi(s+a).
 \tag{4}
\]
Since \(u,x\le.5\), one has \(U,A\ge0\). Also
\(.575\le u+x\le1\) and \(h_s+c<0\), so \(C_a\le0\)
from the exact real cotangent formula. The pair matrix is
\[
 -\pi^{-1}\Re V(s,a)''
   =\begin{pmatrix}U-C_a&-C_a\\-C_a&A-C_a\end{pmatrix}
   =\operatorname{diag}(U,A)
       -C_a\begin{pmatrix}1&1\\1&1\end{pmatrix}\succeq0.
 \tag{5}
\]
This conclusion requires no separate cotangent-cone bound.
At \(u=x=.5\), all three real cotangents can vanish.
No positive floor for (5) at that corner is asserted.

The remaining \((s,q)\) form \(V(s,q)-g(s)\) is positive.
For \(u\ge.15\), the old
[pair theorem](research_mixed_horizontal_zero_mode_support.md),
Section 2, and its
[half-index extension](research_mixed_half_index_contour.md)
give positivity of \(V(s,q)\), and \(-g(s)\) adds a nonnegative
real cost. For \(1/8\le u\le.15\), write
\[
 Q=\Re\cot\pi q,\qquad C_q=\Re\cot\pi(s+q).
 \]
Its matrix divided by \(\pi\) is
\[
 \begin{pmatrix}2U-C_q&-C_q\\-C_q&Q-C_q\end{pmatrix}.
 \tag{6}
\]
The original \(\lambda=1\) estimates in the
[own-four left-cut proof](research_mixed_four_left_cut_extension.md),
as explicitly retained in the bare-contour proof, give
\[
 U>21/20,\quad Q-C_q>9/70,\quad
 C_q+\frac{C_q^2}{Q-C_q}<187/120.
 \tag{7}
\]
For \(C_q\le0\) the last expression is nonpositive;
otherwise it is exactly the old Schur estimate.
The Schur complement of (6) is therefore greater than
\[
                       2(21/20)-187/120=13/24>0.
 \tag{8}
\]
Finally \(-\eta g(a)/2\) has nonnegative negative-real Hessian,
the chirp has purely imaginary Hessian, and
\(-\Re\ell''_q(x_0)>1/10\) on (2), as already proved.
Adding these forms establishes
\[
                 -\Re F_\eta''\succeq0
                    \quad\hbox{throughout the added strip.}
 \tag{9}
\]
The primitive \(g(s+a)\) at \(\Re(s+a)=1\) is its original
lower-half-plane continuation. Its imaginary part is at most
\(-.001\); hence this is a regular point, not an omitted factorial
zero or a new logarithmic lift.

## 2. A positive quadratic reserve from the initial segment

Write \(a_R=\Re a_*\), \(s_R=\Re s_*\), \(q_R=\Re q_*\).
The original typed images give
\[
 a_R\le.433\quad(\eta=0),\qquad a_R\le.36\quad(\eta=1).
 \tag{10}
\]
Consider the straight horizontal segment from the reference
to a target in (2). If \(x>.45\), it remains in the old
strict-curvature domain at least until parameter
\[
 \lambda_0=\frac{.45-a_R}{x-a_R}
       \ge\lambda_\eta,\qquad
 \lambda_0^{\rm min}:=\frac{17}{67},\quad
 \lambda_1^{\rm min}:=\frac9{14},\quad
 \lambda_\eta:=\lambda_\eta^{\rm min}.
 \tag{11}
\]
The index and outgoing coordinates stay in their old rectangles
on the entire segment. Integrating (3) up to \(\lambda_\eta\)
and (9) thereafter gives
\[
 \begin{split}
 \Re F_\eta(u+ih_s,x+ic,z+ih_q)
 \le{}&M_\eta+\Re P_\eta(x-a_R)\\
 &-\kappa\chi_\eta
       \{(u-s_R)^2+(x-a_R)^2+(z-q_R)^2\},
 \end{split}
 \tag{12}
\]
where the explicit constants are
\[
 \chi_0=2(17/67)-(17/67)^2=\frac{1989}{4489},\qquad
 \chi_1=2(9/14)-(9/14)^2=\frac{171}{196}.
 \tag{13}
\]
Indeed the Taylor weight is \(1-t\), so
\(\mu\int_0^{\lambda_\eta}(1-t)\,dt=\kappa\chi_\eta\).
When \(x\le.45\), the old coefficient \(\kappa\) applies and
implies (12) as well.

Thus (12) is an original calibrated sheet inequality on the
whole incoming half interval. It retains the private-index and
outgoing losses, rather than only an optimized value.
No critical point at the new incoming target has been selected.

## 3. Raising the incoming height on the right taper

For \(x\in[.45,.5]\), the phase inequality (22) of
[incoming height transport](research_mixed_fourier_incoming_height_transport.md)
applies at the actual negative index height \(h_s\).
For every \(c\le h\le0\), it combines with (12) to give
\[
 \begin{split}
 \Re F_\eta(u+ih_s,x+ih,z+ih_q)
 \le{}&M_\eta+\Re P_\eta(x-a_R)
       -\frac{\pi}{10}(h-c)\\
 &-\kappa\chi_\eta
       \{(u-s_R)^2+(x-a_R)^2+(z-q_R)^2\}.
 \end{split}
 \tag{14}
\]
This includes the full quadratic taper
\(h=400(.5-x)^2c\). It is a bound on the original main phase;
all source arguments in it remain on the same lower-half-plane
branches.

Relative to the complete complex tangent
\(\Re\{\Pi_\eta^{\rm F}(a_*;x_0)+P_\eta(x+ih-a_*)\}\),
the additional displayed height term is
\[
                    \{\Im P_\eta-\pi/10\}(h-c).
 \tag{15}
\]
It is retained, not discarded as favorable. A full compensated
right-boundary estimate must combine it with the adjacent ordinary
allocation and its other quadratic costs. The main-sheet inequality
also supplies no positive-retained-current bound or complete
low-source estimate at these new targets. Those are separate
obligations; the new horizontal and height estimates do not
change their contour inventory.
