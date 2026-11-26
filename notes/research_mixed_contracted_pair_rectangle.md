# The complete contracted three-four source on its original index rectangle

Research deduction, 7 November 2026. Contracting the shared Fourier
wire before taking a modulus gives a four-index phase which is
strictly accretive on the entire original index rectangle. This
proves a nonzero local current with the original action and scalar,
and separates the remaining global estimates from any far-wire
profile optimization. No numerical evaluation or global source
sign is asserted.

## 1. Exact finite source and its physical support

Use the original conventions
\[
 r=e^{-2\pi i/N},\quad Q_N=r^{-1},\quad P_j=(r;r)_j,
 \quad X=e^{2\pi ix},\quad Y=e^{2\pi iy},
 \quad c_x=N^{-1}e^{-\pi i(N-1)x}(1-X^N).
 \tag{1}
\]
The exact matrices \(B_3,\Gamma,B_4\) in
[wire contraction](research_mixed_wire_exact_contraction.md),
equations (5), (10)--(12), give
\[
\begin{split}
 \mathcal K_{34,N}(x,y)
 &=h(x)^TA_3A_4h(y)=f(x)^TB_3\Gamma B_4f(y)\\
 &=\kappa^3N c_xc_y
 \sum_{\substack{i,j,k,l\ge0\\ i+j<N,\ j+k<N,\ k+l<N}}
 \frac{X^iY^lQ_N^{jk}P_{i+j}P_{j+k}P_{k+l}}
 {P_j^2P_k^3P_l(X;r)_{i+1}(Y;r)_{l+1}}.
\end{split}
 \tag{2}
\]
There is no additional \(N\) factor: the shared-wire integral
has already produced \(\Gamma\). Both level parities, all
physical rows and all original normal factors remain in (2).
The three inequalities in its support are exact, not estimates.

Write \(s=i/N,t=j/N,p=k/N,q=l/N\). The closed physical
polytope is
\[
 \Omega=\{s,t,p,q\ge0:\ s+t\le1,\ t+p\le1,\ p+q\le1\}.
 \tag{3}
\]
In particular the shared triangular face \(t+p=1\) cannot
be replaced by two independent vertex triangles.

## 2. Original action and whole-rectangle accretivity

Let \(x_0=x_{34}\), \(K=e^{2\pi ix_0}\), and use the
original primitive \(g(z)=J(z)+i\pi(z-z^2)/2\). Put
\[
\begin{split}
 I_X(s)&=\frac{\operatorname{Li}_2(Xe^{-2\pi is})-
                         \operatorname{Li}_2(X)}{2\pi i},\\
 \ell_s(x)&=2\pi isx-I_X(s)-\pi ix,\\
 G(t,p)&=g(t+p)-2g(t)-2g(p)+2\pi itp,\\
 \mathcal F(s,t,p,q;x,y)
 &=g(s+t)+G(t,p)+g(p+q)-g(p)-g(q)
                             +\ell_s(x)+\ell_q(y).
\end{split}
 \tag{4}
\]
The original interpolation lifts in (4) are fixed by (2).
Take precisely the two old rectangles
\[
 \mathcal R_3=[1/4,9/20]+i[-3/100,3/200],\qquad
 \mathcal R_4=[1/5,21/50]+i[-11/200,3/200],
 \quad \mathcal R=\mathcal R_3^2\times\mathcal R_4^2.
 \tag{5}
\]
All factorial arguments lie in compact subintervals of the regular
strip: the three sum real parts are in \([.5,.9]\),
\([.45,.87]\), and \([.4,.84]\). The original estimate
\(|K|e^{.03\pi}<.7\) also keeps both external denominator
interpolants regular. These properties persist for \(x,y\)
in a fixed neighborhood of \(x_0\).

**Proposition 1.** There are a fixed endpoint neighborhood and
\(\mu>0\) on which
\[
                    -\Re\mathcal F''\succeq\mu I_4
                    \qquad\hbox{throughout }\mathcal R.
 \tag{6}
\]
The Hessian is in the four index variables. In particular the real
part is strictly concave in their real parts and separately convex
in their imaginary parts.

*Proof.* It suffices first to set \(x=y=x_0\). The negative
real Hessian of \(g(s+t)\) is positive semidefinite because
\(\Re(s+t)\ge1/2\). Define
\(V(z,w)=g(z+w)-g(z)-g(w)\). The
[complex triangle criterion](research_mixed_boundary_strip_bounds.md),
Section 1, makes \(-\Re V''\) positive definite whenever
the two legs have real parts in \((0,1/2)\) and
\(|\Im\cot\pi z|,|\Im\cot\pi w|<1\).

For \(t\in\mathcal R_3\), the last condition holds because
\(\Re t\ge1/4\). For either leg of \(\mathcal R_4\),
it follows from
\[
 \cos(2\pi\Re p)\le\cos(2\pi/5)<1/2
                         <e^{-11\pi/100}\le e^{-2\pi|\Im p|}.
 \tag{7}
\]
The middle strict inequality is elementary: \(11\pi/100<1/2\)
and \(e^{1/2}<2\), the latter following by comparison of its
power series with \(\sum_{n\ge0}2^{-n}=2\). Thus both
\(V(t,p)\) and \(V(p,q)\) have positive negative-real
Hessians. This also follows for the latter from the stronger
original [four-packet proof](research_power_four_source_packet.md),
Lemma 2, before its external diagonal terms are added.

The decomposition
\(G(t,p)=V(t,p)-g(t)-g(p)+2\pi itp\) adds positive
own-leg diagonal forms, since \(\Re\cot\pi t\) and
\(\Re\cot\pi p\) are positive. Its quadratic chirp has
zero real Hessian. Finally the external incidence contributes
\[
 -\Re\ell_{s,ss}(x_0)
   =\frac{-2\pi\Im(Ke^{-2\pi is})}{|1-Ke^{-2\pi is}|^2}>0.
 \tag{8}
\]
Indeed the original \(.18299<\Re x_0<.18301\) gives
\(-1/2<\Re x_0-\Re s<0\) throughout \(\mathcal R_3\).
The same argument applies to the external \(q\) incidence.
The positive pair forms cover \((t,p,q)\), and (8) covers
\(s\); all other displayed forms are nonnegative. Their sum is
strictly positive definite everywhere on the compact product.
Compactness and continuity give \(\mu>0\) and its endpoint
neighborhood. Holomorphy gives the imaginary-convexity assertion.
\(\square\)

## 3. The calibrated critical value and its local symbol

Let \(z_3,z_4\) be the original inverse legs at the alternating
reference. The critical point of (4) is
\[
             (s,t,p,q)=(z_3,z_3,z_4,z_4).
 \tag{9}
\]
The original index equations and shared-wire stationarity imply
this using the absolutely calibrated identity
\(G(t,p)=\operatorname{stat}_z[\ell_t(z)+\ell_p(z)]\)
from [the contracted phase](research_mixed_contracted_phase.md),
Section 5. Therefore its critical value is exactly
\[
 \mathcal F_* =\Phi_3(x_0,x_0)+\Phi_4(x_0,x_0),
 \qquad M=\Re\mathcal F_*.
 \tag{10}
\]
No carrier constant is reset. Proposition 1 gives uniqueness in
\(\mathcal R\), a nondegenerate local branch, and on the
horizontal product through (9)
\[
 \Re\mathcal F\le M-
       \frac\mu2\|(\Re s,\Re t,\Re p,\Re q)
                    -(\Re z_3,\Re z_3,\Re z_4,\Re z_4)\|^2.
 \tag{11}
\]

For precision about normalization, put
\(a(z)=\sqrt{2\sin\pi z}\,e^{-i\pi z/2}\), with its
original branch, and define the nonzero symbol
\[
 b(s,t,p,q;x,y)=
 \frac{e^{\pi i(x+y)}a(s+t)a(t+p)a(p+q)}
 {a(t)^2a(p)^3a(q)
  \sqrt{(1-X)(1-Xe^{-2\pi is})(1-Y)(1-Ye^{-2\pi iq})}}.
 \tag{12}
\]
The complete row interpolant in (2), including its outside scalar,
is \(\kappa^3N^{-5/2}b\,e^{N\mathcal F}(1+O(N^{-1}))\)
uniformly on the regular product. The factorial quotient supplies
\(N^{-3/2}\), and \(Nc_xc_y\) supplies \(N^{-1}\).
Thus its four-index zero-frequency local integral, with lattice
measure \(N^4\), has nonzero leading term
\[
 \kappa^3N^{-1/2}
 \frac{(2\pi)^2b_*}{\sqrt{\det(-\mathcal F''_*)}}
 e^{N\mathcal F_*}(1+O(N^{-1})).
 \tag{13}
\]
The determinant has its accretive branch. The phase, coefficient and
all fixed derivative expansions continue to a smaller endpoint
neighborhood. Formula (13) defines this current's own coefficient;
it does not identify selected local cycles merely from equality of
their complete finite sources.

## 4. What a whole-source proof still has to compare

Let \(C=[1/4,9/20]^2\times[1/5,21/50]^2\), and let
\(T=\Omega\setminus\operatorname{int}C\). On this full
closed physical complement, a uniform upper rate for the supported
physical rows, continuously extended to the faces of \(\Omega\), is
\[
\begin{split}
 E(s,t,p,q;X,Y)={}&-\tfrac12\log|XY|
 +J(s+t)+J(t+p)+J(p+q)-2J(t)-3J(p)-J(q)\\
 &+s\log|X|+q\log|Y|-\mathcal I_X(s)-\mathcal I_Y(q),\\
 \mathcal I_X(s)&=\int_0^s\log|1-Xe^{-2\pi iv}|\,dv.
\end{split}
 \tag{14}
\]
Uniform sine-factorial bounds with \(O(\log N)\) error prove
this upper bound up to all three triangular faces and all coordinate
ends. Rows exactly on a prohibited sum-\(N\) face are zero;
no two-sided logarithmic asymptotic for those rows is asserted.
The external denominator circles stay away from zero. No physical
support face or high row is discarded from the upper comparison.

Inside \(C\), apply the exact fourfold lattice contour identity
on (5), with each main height equal to its component in (9).
The physical central box lies strictly inside all three support
inequalities, so it introduces no diagonal staircase. All four
indices use the *same* phase (4). A sufficient remaining comparison
is a strict gap below \(M\) for (14) on \(T\) and for every
nonmain current of this tensor contour, including its full vertical
joins and both horizontal aliases. The joins may use the exact
debits in [vertical regrouping](research_exact_vertical_current_regrouping.md).
Separate imaginary convexity from (6) reduces any unpenalized
vertical-height maximum to its original endpoints; it does not
itself prove that endpoint maximum is below \(M\).

If these remaining comparisons have one common positive gap,
the exact finite source (2) equals (13) plus an exponentially
smaller remainder, uniformly on a smaller endpoint neighborhood.
At present those signs are not asserted. This formulation retains
the cancellation inside \(\Gamma\), so it does not require
separate absolute bounds for the two vertices at every shared-wire
angle. It also does not turn the local cap entrance theorem into a
whole-message estimate.
