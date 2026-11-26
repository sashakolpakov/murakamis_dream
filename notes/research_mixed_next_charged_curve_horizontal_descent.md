# Uniform horizontal descent along the selected charged curve

Private written phase estimate, 9 November 2026. The selected cubic
phase has a uniformly negative real second derivative on the positive
rectangle containing its entire charged critical curve. This gives
quantitative horizontal descent, including estimates at both ends of
that rectangle and a lower bound on the action loss.

The proof concerns the original phase. It does not estimate the
remaining finite right-hand current or extend the full quantum packet.
No mathematical numerical evaluation or saved-value arithmetic is used.

## 1. Original phase and statement

Retain the notation and branches of the
[full charged-curve theorem](research_mixed_next_selected_charged_curve_full_interval.md).
In particular put
\[
 \mathcal R=\{a-ih:0\le a\le4/3,\ 0\le h\le1/2\},\qquad
 c(u)=\cos(t_*(u)/2),\qquad
 f(u)=\operatorname{arsinh}\{c(u)\tan(u/2)\}.
 \tag{1}
\]
The inverse hyperbolic sine is principal on this rectangle and agrees
with the original logarithmic lift. The action is
\[
 \Psi_\delta(u)=S(u)+\frac{3iu^2}{4\pi}-i\delta u,\qquad
 S'(u)=-\frac{f(u)}{\pi},\qquad 0\le\delta\le1/2 .
 \tag{2}
\]
Write its unique selected critical point as
\[
 u_\delta=a_\delta-ih_\delta,\qquad
 \Gamma(\delta)=\Re\Psi_\delta(u_\delta),\qquad M_3=\Re S(0).
 \tag{3}
\]
The cited theorem proves \(a_0=h_0=0\), and proves that
\(0<a_\delta<4/3\), \(0<h_\delta<1/2\) for positive \(\delta\).

**Theorem.** On the whole closed rectangle \(\mathcal R\),
\[
                  \Re f'(u)>\frac1{50},\qquad |f'(u)|<\frac32 .
 \tag{4}
\]
Consequently the original phase has
\[
                   \Re\Psi_\delta''(u)<-\frac1{50\pi}.
 \tag{5}
\]
For every \(0\le\delta\le1/2\) and \(0\le a\le4/3\),
\[
 \Re\Psi_\delta(a-ih_\delta)
       \le\Gamma(\delta)-\frac{(a-a_\delta)^2}{100\pi}.
 \tag{6}
\]
For positive \(\delta\) the following explicit bounds also hold:
\[
 \frac{\pi\delta}{6}<a_\delta
       <\frac{2\pi\delta}{3}+\frac27,\qquad
 \frac{a_\delta}{75}<h_\delta<\frac32a_\delta,\qquad
 h_\delta>\frac{\pi\delta}{450}.
 \tag{7}
\]
In particular, with
\[
                 d_{\mathrm R}=\frac{22/7-\pi}{3}>0,
 \tag{8}
\]
both ends of the horizontal interval satisfy
\[
\begin{split}
 \Re\Psi_\delta(-ih_\delta)
      &\le\Gamma(\delta)-\frac{\pi\delta^2}{3600},\\
 \Re\Psi_\delta(4/3-ih_\delta)
      &\le\Gamma(\delta)-\frac{d_{\mathrm R}^2}{100\pi}.
\end{split}
 \tag{9}
\]
The first inequality at \(\delta=0\) is equality. Finally,
\[
               M_3-\Gamma(\delta)\ge\frac{\pi\delta^2}{900}
                              \qquad(0\le\delta\le1/2).
 \tag{10}
\]
For positive \(\delta\), the action inequality is strict.

## 2. Bounds for the two terms of the derivative

Set \(v=2c\) and
\[
                   \Delta=3v^2-4iv-3.
\]
The original cubic continuation gives throughout \(\mathcal R\)
\[
 \Re v>\frac32,\quad \frac13<\Im v<\frac23,\quad |c|<1,
 \quad \Re c>\frac34,\quad 0<\arg c<\frac37 .
 \tag{11}
\]
Writing \(v=x+ib\), one obtains directly
\[
 \Re\Delta
      =3x^2-3(b-2/3)^2-\frac53>\frac{19}{4}.
 \tag{12}
\]
Differentiating the original cubic
\(v^3-2iv^2-3v+2i-2\cos(u/2)=0\) therefore gives
\[
                    c'(u)=-\frac{\sin(u/2)}{2\Delta}.
 \tag{13}
\]

The charged-curve proof supplies the strict rational bounds
\[
 \cos(4/3)>\frac7{30},\qquad
 \cosh(1/2)<\frac{17}{15},\qquad
 |\tan(u/2)|^2<\frac23,\qquad
 |c(u)\tan(u/2)|^2<\frac{16}{25}.
 \tag{14}
\]
They imply
\[
\begin{split}
 |\sin(u/2)|^2
    &=\frac{\cosh h-\cos a}{2}<\frac9{20}<\frac9{16},\\
 |\tan(u/2)|&<\frac56,\qquad |c'(u)|<\frac3{38},\\
 \frac{15}{16}
       &<|\sec^2(u/2)|<\frac{81}{49}.
\end{split}
 \tag{15}
\]
For the last line, use
\[
 |\cos(u/2)|^2
       =\frac{\cos a+\cosh h}{2}<\frac{16}{15},
 \qquad
 |\cos(u/2)|^2\ge\cos^2(2/3)>(7/9)^2.
\]

Write \(z=c(u)\tan(u/2)\) and take the principal square root
\[
                         w=\sqrt{1+z^2}.
\]
The disk bound in (14) gives
\[
                  \frac35<|w|<\frac{13}{10},
                  \qquad |\arg w|<\frac{\pi}{8}.
 \tag{16}
\]
Indeed \(|1+z^2|>1-16/25=9/25\), whereas
\(|1+z^2|<41/25<(13/10)^2\). The disk with center \(1\)
and radius \(16/25\) has arguments bounded in modulus by
\(\arcsin(16/25)<\pi/4\), since \(512<625\).
Taking its principal square root proves the argument assertion.

The derivative has exactly two terms:
\[
 f'(u)=L(u)+E(u),\qquad
 L(u)=\frac{c(u)\sec^2(u/2)}{2w},\qquad
 E(u)=\frac{c'(u)\tan(u/2)}{w}.
 \tag{17}
\]
Equations (15)--(16) give
\[
                         |E(u)|<\frac{25}{228}.
 \tag{18}
\]
There is also useful control of the argument of \(L\). The number
\(\cos((a-ih)/2)\) is in the first quadrant, with
\[
 0\le\arg\cos(u/2)
       =\arctan\{\tan(a/2)\tanh(h/2)\}<\frac3{14}.
 \tag{19}
\]
Here \(\tan(2/3)<6/7\), by \(\sin(2/3)<2/3\) and
\(\cos(2/3)>7/9\), while \(\tanh(1/4)<1/4\).
Thus \(-3/7<\arg\sec^2(u/2)\le0\).
Together with (11),(16), this implies
\[
                |\arg L(u)|<\frac37+\frac{\pi}{8}<\frac{\pi}{3}.
 \tag{20}
\]
The last comparison follows already from \(\pi>3\).
Its modulus satisfies
\[
             |L(u)|>\frac{(3/4)(15/16)}{2(13/10)}
                           =\frac{225}{832}.
 \tag{21}
\]
Consequently
\[
 \Re f'(u)>\frac{225}{1664}-\frac{25}{228}
              =\frac{2425}{94848}>\frac1{50}.
 \tag{22}
\]
For the upper modulus use the opposite bounds in (15)--(16)
and \(|c|<1\):
\[
 |f'(u)|<\frac{135}{98}+\frac{25}{228}<\frac32.
 \tag{23}
\]
For example, \(3/2-135/98=6/49>25/228\), since
\(1368>1225\). This proves (4). All estimates apply to the
closed rectangle and to its original analytic branches.

## 3. Horizontal descent and location estimates

Equation (2) gives
\[
                   \Psi_\delta''(u)
                         =-\frac{f'(u)}{\pi}+\frac{3i}{2\pi}.
 \tag{24}
\]
Its real part satisfies (5). On the horizontal line through
\(u_\delta\), the real derivative vanishes at \(a=a_\delta\)
because the full complex derivative vanishes there. Integrating
(5) twice along this real segment proves (6).

To prove (7), fix positive \(\delta\) and abbreviate
\(a=a_\delta\), \(h=h_\delta\). The original critical equation is
\[
                    f(a-ih)=\frac{3h}{2}
                                      +i(3a/2-\pi\delta).
 \tag{25}
\]
The charged-curve proof gives, on the left boundary,
\[
                        0<\Re f(-ih)<h/2.
 \tag{26}
\]
The lower inequality follows directly from the right-half-plane
argument of the original inverse hyperbolic sine. Integrating
(4) horizontally from \(-ih\) to \(a-ih\) now gives
\[
              \frac{a}{50}<\frac{3h}{2}<\frac h2+\frac{3a}{2}.
 \tag{27}
\]
These are the two bounds \(a/75<h<3a/2\).

Since \(f(0)=0\), integration of (4) on the radial segment in
\(\mathcal R\) gives \(|f(u)|<3|u|/2\) for nonzero \(u\).
From (25),
\[
 \pi\delta\le\frac32|u_\delta|+|f(u_\delta)|
                <3|u_\delta|<6a .
 \tag{28}
\]
The last inequality uses \(h<3a/2\), hence
\(|u_\delta|<(\sqrt{13}/2)a<2a\). This proves the lower
bound on \(a\) and then \(h>\pi\delta/450\).

The upper bound uses the already proved \(\Im f(u)<3/7\)
on \(\mathcal R\). Equation (25) gives
\[
                         a<\frac{2\pi\delta}{3}+\frac27.
 \tag{29}
\]
Because \(\delta\le1/2\), the distance from \(a\) to \(4/3\)
is greater than \(d_{\mathrm R}\) in (8). Equations (6)--(7)
give both endpoint bounds (9). They remain valid at \(\delta=0\)
by the original values \(a_0=h_0=0\).

Finally the calibrated action identity in the charged-curve theorem is
\[
                  M_3-\Gamma(\delta)=\int_0^\delta h_s\,ds.
 \tag{30}
\]
Integrating the lower bound in (7) proves (10).

## 4. What this does and does not supply to the finite sum

For every compact frequency interval bounded away from \(\delta=0\),
the selected point stays away from both ends of the horizontal
segment, and (6) gives a uniform Gaussian maximum there. At
\(\delta=0\) the selected point is the left endpoint of this positive
segment; the original full sampling argument uses both angular
halves and treats that endpoint separately.

The proof supplies a horizontal descent contour for the phase on the
positive rectangle. To use it for the original finite cosine
observation throughout the frequency interval, one still needs the
full finite source on an eligible neighborhood of this contour, the
connection to the original sampling contour, and estimates for its
other sides and aliases. In particular the right-hand current in the
inner-source assembly has not been bounded here. The phase action
loss in (10) cannot replace a finite-source estimate.

## Frozen source versions

- Full selected charged curve and its original logarithmic lift:
  6828459338fff642bf52b425120ed806d39bd9847d8df5ea5db8a14f0859da0c.
- Original cubic continuation and strict branch guards:
  8a8ef3f93a4ab44724d43f7bb9b15c5f8210d4649f79d1f0d4c0ec277801f41a.

