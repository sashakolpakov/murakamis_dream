# The outer-cap action at the end of the auxiliary-real curve

Research deduction, 8 November 2026. The explicit curve on which the
endpoint auxiliary saddle is real is not, by itself, a descending
outer-cap contour. At an exact actual incoming parameter, its terminal
portion lies strictly above the outer critical action. A horizontal
segment through that same critical point is descending and lies in an
available endpoint-source neighborhood after a sufficiently small
shrink. Connecting the earlier curve to this segment remains a
separate contour problem.

This is an exact local statement about the original action. It does
not assert a lower bound for a signed finite sum, failure of the
endpoint asymptotic, or nonexistence of another outer contour. No
numerical evaluation is used.

## 1. Original phases and the actual incoming point

Keep the phases and their original logarithmic lifts from
[the general incoming transport](research_mixed_half_face_general_incoming_transport.md),
Section 1:
\[
 \begin{split}
 F(e,u)&=-2J(1/2-u)-3J(u)-J(e-u)+i\pi eu,\\
 S(e)&=F(e,u_c(e)),\\
 \Psi(e,a)&=S(e)+J(e+a)-J(a)-i\pi ea,
 \qquad J'(q)=\Log(2\sin\pi q).
 \end{split}                                                     \tag{1}
\]
The endpoint curve in
[the auxiliary-real source theorem](research_mixed_endpoint_auxiliary_real_curve.md),
Section 1, is
\[
 \begin{gathered}
 t_-= (\sqrt3-1)/2,\qquad t_0=1/\sqrt2,\qquad t_-\le t\le t_0,\\
 p(t)=1-2t^2+2it,\qquad
 e(t)=\frac{\Log p(t)}{2\pi i},\\
 u_c(e(t))=\frac{\arctan t}{\pi},\qquad
 \omega(t)=e^{2\pi iu_c(e(t))}=\frac{1+it}{1-it}.
 \end{gathered}                                                   \tag{2}
\]
The logarithm has argument in \([\pi/4,\pi/2]\). At the right
endpoint,
\[
 \begin{gathered}
 e_0=e(t_0)=\frac14-\frac{i\log2}{4\pi},\qquad
 p_0=i\sqrt2,\qquad
 \omega_0=\frac{1+2\sqrt2\,i}{3},\\
 X_0=-\frac13+\frac{2\sqrt2}{3}i,\qquad
 a_0=1-\frac{\Arg X_0}{2\pi}.
 \end{gathered}                                                   \tag{3}
\]
Here \(1/2<a_0<7/10\). Indeed \(X_0\) is on the upper unit
semicircle, and
\(\cos(3\pi/5)=(1-\sqrt5)/4>-1/3\), using \(\sqrt5<7/3\).
Section 4, equations (28)--(30), of the general incoming transport
identifies (3) with the selected original cap critical point.
In particular its original lift satisfies
\[
                \Psi_e(e_0,a_0)=0,\qquad
                M_{\rm cap}(a_0)=\Re\Psi(e_0,a_0).              \tag{4}
\]
This identification is stronger than merely solving an
exponentiated critical equation.

The complete original endpoint coefficient has a nonzero
\(N^{-3/2}\) asymptotic on a fixed open neighborhood of \(e_0\),
with both parities and fixed ordinary-color/index derivatives:
see [the later-point source theorem](research_mixed_endpoint_later_incoming_point.md),
Section 4. The auxiliary-real source theorem extends that endpoint
statement along all of (2). Neither statement alone compares the
outer action along the curve with (4).

## 2. Exact outer Hessian

All derivatives below are derivatives of (1). Put
\[
 C=\cot\pi(e_0-u_c(e_0)),\qquad
 A=2\tan\pi u_c(e_0)+3\cot\pi u_c(e_0).
\]
The exact ratios in (3) give
\[
 \frac{\omega_0}{p_0-\omega_0}=1-i\sqrt2,\qquad
 C=i\left(1+\frac{2\omega_0}{p_0-\omega_0}\right)
      =2\sqrt2+3i,\qquad A=4\sqrt2.                            \tag{5}
\]
Since
\[
 F_{ee}=-\pi C,\qquad F_{eu}=\pi(C+i),\qquad
 F_{uu}=-\pi(A+C),
\]
the Schur derivative of the original endpoint action is
\[
 \frac{S''(e_0)}{\pi}
   =-C+\frac{(C+i)^2}{A+C}
   =-2\sqrt2-\frac i3.                                        \tag{6}
\]
For example, \((C+i)^2=-8+16\sqrt2\,i\), and division by
\(A+C=6\sqrt2+3i\) gives \(8i/3\). The outer numerator contributes
\[
 \cot\pi(a_0+e_0)
    =i\left(1+\frac{2X_0}{p_0-X_0}\right)
    =-2\sqrt2+3i.
 \tag{7}
\]
Consequently the full outer Hessian, retaining the endpoint action
and the outer chirp in (1), is
\[
             \boxed{\ \Psi_{ee}(e_0,a_0)
                       =-4\pi\sqrt2+\frac{8\pi i}{3}\ }.       \tag{8}
\]
These are algebraic calculations of derivatives on a regular
original phase chart; no new action value is evaluated.

## 3. The curve approaches through an ascending direction

Direct differentiation of (2) gives
\[
                e'(t_0)=\frac{1-i/\sqrt2}{\pi}.                \tag{9}
\]
The first derivative of \(\Psi(e(t),a_0)\) vanishes by (4).
Its second real derivative is
\[
 \left.\frac{d^2}{dt^2}\Re\Psi(e(t),a_0)\right|_{t=t_0}
   =\Re\{\Psi_{ee}(e_0,a_0)e'(t_0)^2\}
   =\frac{2\sqrt2}{3\pi}>0.                                  \tag{10}
\]
Thus the actual curve satisfies
\[
 \Re\Psi(e(t),a_0)
    =M_{\rm cap}(a_0)+\frac{\sqrt2}{3\pi}(t-t_0)^2
                         +O(|t-t_0|^3).
 \tag{11}
\]
In particular its points with \(t<t_0\) sufficiently close to
\(t_0\) have action strictly greater than \(M_{\rm cap}(a_0)\).
The unmodified terminal portion of (2) therefore cannot be included
in a main path whose pointwise outer action is everywhere at most
\(M_{\rm cap}(a_0)\). This obstruction occurs at the actual
incoming parameter (3), not at an unrealized point of a containing
parameter box.

For a local geometric description, write a displacement approaching
the saddle from the left as \(\Delta e=-s+ims\), with \(s>0\).
Equation (8) gives
\[
 \Re\{\Psi_{ee}(e_0,a_0)(\Delta e)^2\}
  =-4\pi\sqrt2\,s^2
        \left(1-m^2-\frac{4m}{3\sqrt2}\right).
 \tag{12}
\]
The strictly descending quadratic directions with \(m\ge0\)
therefore satisfy
\[
            0\le m<\frac{\sqrt{11}-\sqrt2}{3}.                 \tag{13}
\]
The curve's terminal direction has \(m=1/\sqrt2\), outside
this interval, consistently with (10).

## 4. What the endpoint source does supply locally

The horizontal direction has
\[
 \Re\Psi(e_0+s,a_0)
     =M_{\rm cap}(a_0)-2\pi\sqrt2\,s^2+O(|s|^3),
                       \qquad s\in\mathbb R.                 \tag{14}
\]
Choose a sufficiently small fixed \(\rho>0\) so that this segment
lies in the proved endpoint-source neighborhood and the original
outer factorial chart. Such a choice is possible: \(e_0\),
\(e_0-u_c(e_0)\), and \(a_0+e_0\) are all regular, and the
endpoint source is holomorphic on an open neighborhood.
After decreasing \(\rho\) if necessary,
\[
 \Re\Psi(e_0+s,a_0)
       \le M_{\rm cap}(a_0)-\pi\sqrt2\,s^2,
                          \qquad |s|\le\rho.                 \tag{15}
\]
This is an admissible local descending segment for the actual
endpoint factor, with its original nonzero symbol and fixed
derivatives. It is not yet a whole outer-cap contour or a
complete outer-cap asymptotic.

The preceding source theorems give no specified width for their
neighborhoods. Moreover, a terminal curve point in (11) already
lies above the target action, so a path staying below that action
cannot start at such a point. A complete construction must leave
the curve before this terminal ascending portion and enter a
descending corridor such as (13), retaining all connecting pieces.
The required earlier action comparison and source control along
that corridor are not supplied by (15). The new endpoint curve
theorem and the local horizontal segment therefore remain useful
source inputs, while the outer left/main connection remains open.
