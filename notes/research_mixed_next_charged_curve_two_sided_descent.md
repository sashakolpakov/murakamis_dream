# Horizontal descent on both angular halves

Private phase corollary, 9 November 2026. The horizontal descent
estimate extends to both angular halves and both signs of the
imaginary part. The improved argument bounds the derivative error
relative to its main term. It uses only the original cubic branch
and exact written inequalities.

## Statement

Let
\[
 \mathcal D=\{u:|\Re u|\le4/3,\ |\Im u|\le1/2\},\qquad
 f(u)=\operatorname{arsinh}\{c(u)\tan(u/2)\},
 \quad c(u)=\cos(t_*(u)/2).
 \tag{1}
\]
The [original cubic continuation](research_mixed_next_inner_three_cubic_continuation.md)
defines these branches on a neighborhood of \(\mathcal D\).
For the original phase
\[
                  \Psi_\delta(u)=S(u)+\frac{3iu^2}{4\pi}-i\delta u,
                  \qquad S'=-f/\pi,
 \tag{2}
\]
one has
\[
 \Re f'(u)>\frac1{50},\quad |f'(u)|<\frac32,\quad
 \Re\Psi_\delta''(u)<-\frac1{50\pi}
                      \qquad(u\in\mathcal D,\ 0\le\delta\le1/2).
 \tag{3}
\]
Write \(u_\delta=a_\delta-ih_\delta\) for the selected charged point
and \(\Gamma(\delta)=\Re\Psi_\delta(u_\delta)\). Then
\[
 \Re\Psi_\delta(a-ih_\delta)
       \le\Gamma(\delta)-\frac{(a-a_\delta)^2}{100\pi}
                         \qquad(-4/3\le a\le4/3).
 \tag{4}
\]
Thus the selected point is the unique real-part maximum on this
entire horizontal segment. Both endpoints have fixed uniform gaps:
\[
\begin{split}
 \Re\Psi_\delta(-4/3-ih_\delta)
       &\le\Gamma(\delta)-\frac4{225\pi},\\
 \Re\Psi_\delta(4/3-ih_\delta)
       &\le\Gamma(\delta)-\frac{d_{\mathrm R}^2}{100\pi},
 \qquad d_{\mathrm R}=(22/7-\pi)/3>0.
\end{split}
 \tag{5}
\]
These statements include \(\delta=0\), for which \(u_0=0\).

## Proof

Set \(v=2c\), \(\Delta=3v^2-4iv-3\), and
\[
 z=c\tan(u/2),\quad w=\sqrt{1+z^2},\quad
 L=\frac{c\sec^2(u/2)}{2w},\quad
 E=\frac{c'\tan(u/2)}{w}.
 \tag{6}
\]
The derivative is \(f'=L+E\), with \(w\) the principal square root.
The cubic guards hold on the larger original rectangle
\(|\Re u|\le\pi/2,\ |\Im u|\le1/2\), so all modulus estimates in
[the positive horizontal-descent proof, Section 2](research_mixed_next_charged_curve_horizontal_descent.md)
apply on \(\mathcal D\). Their derivations depend only on
\(|\Re u|\) and \(|\Im u|\). Specifically,
\[
\begin{gathered}
 |c|>3/4,\quad |c|<1,\quad 0<\arg c<3/7,\quad
 |\Delta|>19/4,\quad c'=-\frac{\sin(u/2)}{2\Delta},\\
 |\sin(u/2)|^2<9/20,\quad |\cos(u/2)|<16/15,\quad
 |z|^2<16/25,\quad |\arg w|<\pi/8,\quad
 |L|>225/832 .
\end{gathered}
 \tag{7}
\]
The slightly weaker cosine bound here follows from
\(|\cos(u/2)|^2<16/15\) and \(16/15>1\).
The square-root disk avoids the imaginary axis, so the derivative
branch in (6) agrees with the original inverse hyperbolic sine.

For either sign of the two coordinates,
\[
              |\arg\cos(u/2)|<3/14.
 \tag{8}
\]
Indeed its tangent in absolute value is
\(|\tan(\Re u/2)\tanh(\Im u/2)|<3/14\).
Consequently
\[
 -3/7-\pi/8<\arg L<6/7+\pi/8<5\pi/12.
 \tag{9}
\]
The lower bound is also greater than \(-5\pi/12\).
For the upper comparison it suffices that
\(6/7<7\pi/24\), which follows from \(\pi>3\).
Since
\[
 \cos(5\pi/12)=\frac{\sqrt6-\sqrt2}{4}>\frac14
\]
(equivalently \(3>2\sqrt2\)), this gives \(\Re L>|L|/4\).

The relevant error estimate is relative:
\[
 \frac EL
       =-\frac{\sin^2(u/2)\cos(u/2)}{c\Delta},\qquad
 \left|\frac EL\right|
       <\frac{(9/20)(16/15)}{(3/4)(19/4)}
        =\frac{64}{475}<\frac17 .
 \tag{10}
\]
Hence
\[
 \Re f'>|L|\left(\frac14-\frac17\right)
              >\frac{675}{23296}>\frac1{50}.
 \tag{11}
\]
The modulus bound from the same source is unchanged:
\[
 |f'|<\frac{135}{98}+\frac{25}{228}<\frac32.
 \tag{12}
\]
This proves (3). The full horizontal segment in (4) lies in
\(\mathcal D\), and its complex derivative vanishes at \(u_\delta\).
Twice integrating the real second-derivative estimate proves (4).
At the left endpoint the distance from \(a_\delta\ge0\) is at least
\(4/3\). At the right endpoint the charged-location estimate in
the cited horizontal-descent theorem gives distance greater than
\(d_{\mathrm R}\). These facts prove (5).

## Scope

The result supplies a quantitative horizontal contour for the
original phase over the whole frequency interval. A complete
quantum coefficient theorem also requires control of the finite
source on that contour and a deformation of the original finite
sampling formula with every connector and alias retained.
Neither requirement is proved by this phase corollary.
No numerical evaluation, certificate replay, or change to a frozen
source was made.

## Frozen source versions

- Original cubic continuation:
  8a8ef3f93a4ab44724d43f7bb9b15c5f8210d4649f79d1f0d4c0ec277801f41a.
- Selected charged curve:
  6828459338fff642bf52b425120ed806d39bd9847d8df5ea5db8a14f0859da0c.
- Positive horizontal descent and location bounds:
  c069665bd0780f72990ba55680a756d780c577c895ba4272e91af43e00c9ac7f.

