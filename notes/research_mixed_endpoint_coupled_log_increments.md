# Correlated logarithmic increments at the first-four endpoint

Research deduction, 6 November 2026. This note rewrites the actual
reference data in the
[static endpoint budget](research_mixed_selected_endpoint_legendre_budget.md)
using three rational generators with a common numerator. It also
gives two-sided elementary bounds for the two logarithmic deficits
that cancel in its private-edge force. All quantities retain the
same original endpoint reference and the next-three compatibility.
The final endpoint-budget inequality is not proved here.

## 1. A smaller rational chart

Let \(U=e^{2\pi i u_*}\) be the original endpoint coordinate of
the [rational critical transport](research_mixed_rational_critical_transport.md),
with first type four and next type three. Its canonical sheet obeys
\[
 .217<\Re u_*<.234,\qquad .027<\Im u_*<.045.
 \tag{1}
\]
These are the established
[endpoint rectangles](research_mixed_open_word_endpoint_rectangles.md),
not a characterization of all admissible points of this rectangle.
Set
\[
 r=\frac{1+U}{1-U}=i\cot\pi u_*,\qquad
 K=r^2-2r+2,\qquad D=(r-2)(r^2-r+2).
 \tag{2}
\]
Write \(E=e^{-2\pi i e_*}\), \(Z=e^{-2\pi i z_*}\),
\(S=e^{-2\pi i s_*}\), as in the original transport. Its
endpoint equations simplify to
\[
 E=\frac{r^2}{K},\qquad
 1-EZ=-\frac4{K^2},\qquad
 Z=\frac{K^2+4}{r^2K},\qquad
 1-Z=\frac{2D}{r^2K}.
 \tag{3}
\]
For any displayed exponential or product define
\(q_X=-X/(1-X)\). Direct substitution in the original attached
equation \((1-EZ)(1-SZ)=S(1-Z)^3\) gives
\[
 \begin{split}
 q_{EZ}&=\frac{K^2+4}{4},\\
 q_Z&=-\frac{K^2+4}{2D},\\
 q_{SZ}&=\frac{r^4(K^2+4)}{2D^3},\\
 p:=q_S&=\frac{r^6K}{2D(D^2+r^4)}.
 \end{split}
 \tag{4}
\]
For example \(q_{SZ}=-Z(1-EZ)/(1-Z)^3\), proving its
formula without solving a new equation. The last follows from
\(q_S=-(1-EZ)/[(1-Z)((1-Z)^2-(1-EZ))]\).
All denominators are nonzero on the actual regular reference
chart. No zero of a cleared denominator is admitted.

Let \(\mathscr B=e^{-2\pi i b_*}\) and
\(\mathscr C=e^{-2\pi i c_*}\) be the two outputs of the
next-three transfer \(R_2(Z,S)\), and set
\(q_b=q_{\mathscr B}\), \(q_c=q_{\mathscr C}\).
Its two original critical equations give the low-degree identities
\[
 q_b=1-p+\frac{q_Zp}{1-p},\qquad
 q_c=\frac{(1-q_b)(p+q_b-1)}{q_b},\qquad
 q_{SZ}=p-\frac{p^2}{1-q_b}.
 \tag{5}
\]
These formulas retain the ordered roles: \(b_*\) is the outgoing
own type-three leg, whereas \(c_*\) is the next external leg.
At length three that external leg is attached. Its typed domain
still applies; it is not the private endpoint leg.

## 2. One shared radial increment

Put \(H=7/625\), \(c=\Im z_*\), and
\[
 \lambda=e^{2\pi(H-c)},\quad \ell=\log\lambda,
 \quad\delta=\lambda-1,\qquad
                  (1+\delta)|Z|=e^{2\pi H}.
 \tag{6}
\]
For \(j=e,s,z\), let \(q_e=q_{EZ}\), \(q_s=q_{SZ}\),
\(q_z=q_Z\) and define
\[
 R_j=|1+\delta q_j|^2
       =1+2\delta\Re q_j+\delta^2|q_j|^2.
 \tag{7}
\]
The increments of the static budget are exactly
\(A=\tfrac12\log R_e\), \(B=\tfrac12\log R_s\),
\(C=\tfrac12\log R_z\). Consequently their coupled forces are
\[
 \begin{split}
 d&=\frac12\log\frac{(1+\delta)^2}{R_s},\\
 h&=\frac14\log\frac{R_z^6}{R_s(1+\delta)^2},\\
 A-h&=\frac14\log\frac{R_e^2R_s(1+\delta)^2}{R_z^6}.
 \end{split}
 \tag{8}
\]
Every entry uses the same \(r\) and \(\delta\). In particular
the imaginary part of \(q_s\) contributes positively to \(R_s\)
and can reduce \(d\); replacing \(R_s\) by a bound involving
only \(\Re q_s\) can discard that compensation.

For reference, a proposed barrier \(\Re q_s\ge a\), with
\(0\le a\le1\), would imply
\[
 d\le\ell-\log\{1+a(e^\ell-1)\}.
 \tag{9}
\]
Its right side increases with \(\ell\). The particular barrier
\(\Re q_s\ge1/3\) is equivalent to
\(2|SZ|^2-\Re(SZ)\ge1\), or
\(|SZ-1/4|\ge3/4\). None of these barriers is asserted for
the actual family here. Upper-half-plane signs for the own legs
alone are not a proof of them.

## 3. Two positive deficits retain the important cancellation

Write \(h_e=\Im e_*\), \(x=\Re z_*\),
\(t=\Re(e_*+z_*)\). The actual bounds give
\(-.07<c<-.02\), \(-.051<h_e<-.019\),
\(.246<x<.350\), and \(.579<t<.713\). Define
\[
 \begin{array}{lll}
 a_z=-2\pi c,&b_z=2\pi H,&Q_z=\cos(2\pi x),\\
 a_e=-2\pi(h_e+c),&b_e=-2\pi(h_e+H),&Q_e=\cos(2\pi t).
 \end{array}
 \tag{10}
\]
Both pairs satisfy \(0<b_j<a_j\). The exact sine modulus
formula gives positive deficits
\[
 \gamma_j=\frac12\log
       \frac{\cosh a_j-Q_j}{\cosh b_j-Q_j},\qquad
 A=\ell/2-\gamma_e,\quad C=\ell/2-\gamma_z.
 \tag{11}
\]
Thus, with the same \(d\) as in (8),
\[
 \begin{split}
 h&=(\ell+d)/2-3\gamma_z,\\
 A-h&=3\gamma_z-\gamma_e-d/2,\\
 m:=A-\frac{163}{298}h
   &=\frac{135\ell-163d}{596}
                     +\frac{489}{298}\gamma_z-\gamma_e.
 \end{split}
 \tag{12}
\]
The last variable is the center of the improved free-flow bound in
[the centered scalar-cost note](research_mixed_centered_endpoint_scalar_costs.md).
Equations (11)–(12) keep its cancellation before taking bounds.

Here are explicit two-sided bounds requiring only elementary
functions of those same reference values. For \(0<b<a\),
\(Q<1\), put \(\Delta=\cosh a-\cosh b\) and
\(v=\Delta/(\cosh a+\cosh b-2Q)\). Then
\[
 \gamma=\operatorname{arctanh}v,\quad 0<v<1,
 \qquad
 v\le\gamma\le v+\frac{v^3}{3(1-v^2)}.
 \tag{13}
\]
The bounds follow term by term from the positive arctanh series.
For these two actual deficits the same parameter is rational in
the correlated exponential data:
\[
 v_j=\frac{\delta(1-\lambda|P_j|^2)}
 {\lambda|1-P_j|^2+|1-\lambda P_j|^2},
              \qquad P_e=EZ,\quad P_z=Z.
 \tag{13a}
\]
Indeed \(\gamma_j=\tfrac12\log(\lambda/R_j)\) and
\(\lambda-R_j=\delta(1-\lambda|P_j|^2)/|1-P_j|^2\).
The numerator is positive: \(\lambda|Z|^2=e^{2\pi(H+c)}<1\),
and \(|E|<1\). Thus (13) can be used with (13a) without
independently bounding a height or an angle. Likewise
\(d=\operatorname{arctanh}((\lambda^2-R_s)/(\lambda^2+R_s))\);
its argument lies in \((0,1)\) by the proved \(0<B<\ell\).
For \(a<1\), the hyperbolic numerator itself has the bounds
\[
 \frac{a^2-b^2}{2}+\frac{a^4-b^4}{24}
 \le\Delta\le
 \frac{a^2-b^2}{2}
       +\frac{a^4-b^4}{24(1-a^2/20)}.
 \tag{14}
\]
Indeed successive terms \((a^{2j}-b^{2j})/(2j)!\), for
\(j\ge2\), have ratio at most
\(a^2/[2j(2j+1)]\le a^2/20\). This follows from
\((1-r^{j+1})/(1-r^j)\le(j+1)/j\), \(0\le r<1\).
Both actual pairs in (10) have \(a<1\). Equations (13)–(14)
therefore supply rational-series bounds without independent
maximization of \(A,B,C\).

A coarse but useful integrated lower bound is
\[
 \gamma\ge\frac{a^2-b^2}{4(\cosh a-Q)}.
 \tag{15}
\]
It follows by integrating
\(\sinh t/(\cosh t-Q)\ge t/(\cosh a-Q)\).
One may retain the actual denominator in (15). For uniform simpler
denominators, the established ranges give
\(\cosh a_z-Q_z<17/10\) and
\(\cosh a_e-Q_e<11/5\). For example
\(\cosh(.14\pi)<11/10\),
\(-\cos(.7\pi)<3/5\),
\(\cosh(.242\pi)<131/100\), and
\(-\cos(1.158\pi)<89/100\) suffice.
For the two hyperbolic bounds, use respectively \(a<11/25\)
and \(a<761/1000\) in
\(\cosh a\le1+a^2/2+a^4/[24(1-a^2/30)]\).
The first trigonometric bound is \(\sin(\pi/5)<3/5\).
For the last, \(.158\pi>.49\) and
\(\cos(.49)<1-.49^2/2+.49^4/24<.89\).
These are rational Taylor witnesses using
\(157/50<\pi<22/7\). Therefore
\[
 \begin{split}
 \gamma_z&>\frac{5\pi}{17}\ell(-c-H),\\
 \gamma_e&>\frac{5\pi}{22}\ell(-2h_e-c-H).
 \end{split}
 \tag{16}
\]
In particular
\(h<\ell\{1/2-(15\pi/17)(-c-H)\}+d/2\).
This bound keeps the reset height \(c\) coupled to the force,
instead of replacing \(h\) by an independent global endpoint.

## 4. The feasibility constraints still belong to the test

An arbitrary point of (1) need not be an actual source reference.
The canonical endpoint branch, the original zero logarithmic lifts,
and the next-three outputs in (5) remain required. In particular
\(s_*,b_*\) belong to the actual ordinary type-three image and
\(c_*\) to its ordinary-or-attached typed domain. The proved
[wire-sum theorem](research_mixed_reduced_disk_pair_sums.md)
also gives \(.545<\Re(s_*+z_*)<.77\) and
\(.6<\Re(s_*+b_*)<.77\), with stronger case-specific lower
bounds in its table. These inclusions follow from the existing
full product maps; no boundary-only pruning or new root choice is
being made.

The formulas above turn a proposed force bound into an explicit
inequality on one correlated rational parameter, its shared radial
increment (6), and the actual necessary output constraints. They
do not prove the old elementary majorant is below \(\pi^2/128\),
nor the corresponding improved free-flow majorant. In particular,
the next-output conditions must not be dropped merely because
the endpoint parameter rectangle is small.
