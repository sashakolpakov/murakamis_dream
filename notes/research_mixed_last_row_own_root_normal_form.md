# The last-row comparison in the original own roots

Research reduction, 5 November 2026. The original index equation
eliminates the external exponential from the two bare boundary forces.
The Fourier halfweights contribute favorable factorial energies to
the last-row supporting-plane comparison. Consequently four explicit
target corners give a sufficient criterion, with the own denominator
power unchanged. No uniform sign of that criterion is asserted.

## 1. Exact elimination on the original branch

Use a fixed original conditional reference \((s_0,a_0,b_0)\)
from the [revived-endpoint lemma](research_mixed_horizontal_revived_endpoint.md).
Set
\[
 U=e^{-2\pi i s_0},\qquad V=e^{-2\pi i b_0},\qquad
 X=e^{-2\pi i a_0},\qquad d=2+\epsilon,\quad\epsilon\in\{0,1\}.
 \tag{1}
\]
The original zero-lift index equation implies
\[
 (1-UX)(1-UV)=X(1-U)^d,\qquad
 X=\frac{1-UV}{(1-U)^d+U(1-UV)}.
 \tag{2}
\]
This identity is used at an already specified original root. It is
not used to select a root or a logarithmic branch by exponentiation.
All denominators in (2) are nonzero on that original regular source
domain.

Let \(q_a,q_b\) be the bare real marginals in equation (6)
of the revived-endpoint lemma. The original logarithms give
\[
 e^{q_a}=\left|\frac{1-UX}{U(1-X)}\right|,
 \qquad e^{q_b}=\left|\frac{1-UV}{1-V}\right|.
 \tag{3}
\]
The factor \(U^{-1}\) in the first formula is the original
first-argument chirp. Substitution of (2) yields
\[
 \boxed{\quad
 e^{q_a}=
 \begin{cases}
 \displaystyle\left|\frac{1-U}{U^2(1-V)}\right|,&\epsilon=0,\\[2mm]
 \displaystyle\left|\frac{(1-U)^2}{U^2(2-U-V)}\right|,&\epsilon=1,
 \end{cases}
 \qquad
 e^{q_b}=\left|\frac{1-UV}{1-V}\right|.
 \quad}
 \tag{4}
\]
Indeed the unspecialized first ratio in (3) becomes
\((1-U)^{d-1}/[U\{(1-U)^{d-1}-1+UV\}]\).
For \(d=2,3\), the inner factor is respectively
\(U(V-1)\) and \(U(U+V-2)\). The minus signs disappear
only because (4) takes moduli. Nonvanishing of the resulting
denominators also follows from (3) and the original regular factors;
no unproved geometric sign is needed.

## 2. The matched gap and the halfweight energies

Write \(a_0=x_0+ih_a\), \(b_0=z_0+ih_b\), and define
\[
 \begin{split}
 \Phi^{\rm bare}&=Q_\epsilon(s_0;a_0,b_0)-g(a_0)-g(b_0),\\
 L&=2\pi(-h_a)_++2\pi(h_b)_+,\qquad
 \delta_1=\Re\Phi^{\rm bare}-L.
 \end{split}
 \tag{5}
\]
The original own flag \(\epsilon\) remains in
\(Q_\epsilon\) and in the index equation. For formal outer
allocation flags \(\tau_a,\tau_b\in\{0,1\}\), subtract
\(\tau_a g(a)/2+\tau_b g(b)/2\) from the critical phase,
and the same real terms from the last-row rate. They cancel from
the matched gap (5). The physical allocation is
\((\tau_a,\tau_b)=(\eta,\epsilon)\).

For a fixed height put \(G_h(x)=\Re g(x+ih)\), and let
\(\mathcal B_h(x,x_0)\) be its increment above its tangent,
as defined in the revived-endpoint lemma. On
\(I=[11/50,9/20]\) with the admitted fixed heights,
\(\mathcal B_h\ge0\). Write
\(d_a=x-x_0\), \(d_b=z-z_0\), and retain the zero-mode
coefficient \(\kappa_0=1/2500000\). The exact last-row deficit
from its original allocated affine-quadratic plane is
\[
 \begin{split}
 D_{\tau_a\tau_b}(x,z)
 ={}&-\delta_1-q_a d_a-q_b d_b
                      +\kappa_0(d_a^2+d_b^2)\\
 &-\frac{\tau_a}{2}\mathcal B_{h_a}(x,x_0)
  -\frac{\tau_b}{2}\mathcal B_{h_b}(z,z_0).
 \end{split}
 \tag{6}
\]
Thus removing the two halfweight energies gives an upper bound on
the deficit. It does not remove a finite-source factor. In particular
setting the auxiliary \(\tau_b\) to zero does not change a
type-four own denominator into a type-three denominator.

## 3. A four-corner sufficient condition

The first line of (6) is a convex function of each target real
coordinate separately. Its maximum on \(I^2\) occurs at a corner.
Consequently the four inequalities
\[
 \begin{split}
 \delta_1+q_a(\xi-x_0)+q_b(\zeta-z_0)
 -\kappa_0\{(\xi-x_0)^2+(\zeta-z_0)^2\}\ge\gamma,
 \quad(\xi,\zeta)\in\{11/50,9/20\}^2
 \end{split}
 \tag{7}
\]
imply \(D_{\eta\epsilon}\le-\gamma\) on the whole target
plateau. For two type-three outer coordinates the energies in (6)
are absent, so the four-corner test is exact. With a type-four
halfweight it is only sufficient; the explicit clipped cosine
optimization in the revived-endpoint lemma can be stronger.

Equations (2)--(7) retain the same two original own roots throughout.
The force ratios are rational in their exponentials before taking
moduli, but \(\delta_1\) still contains the original dilogarithmic
action and its absolute constant. The reduction does not turn (7)
into a purely polynomial sign test, enlarge the source domain, or
prove it uniformly over independently released root boxes. Actual
coupled reference constraints remain necessary for any uniform use.
