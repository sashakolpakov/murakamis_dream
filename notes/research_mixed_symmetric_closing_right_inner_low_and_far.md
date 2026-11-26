# The low and far inner contour on the right closing path

Private written deduction, 9 November 2026. The original shortened
inner trace is estimated with the outer crossing already included
in its rate budget. A sharper row-curvature estimate pays its low
horizontal segment. The far horizontal, final vertical, and discarded
far physical samples then satisfy the same budget. The central
contour through the inner critical point remains separate.

## 1. Finite functions and the available rate

Retain the original Newton polynomials \(e_j\), shortened kernel,
crossing scalar, and complete sampling multiplier:
\[
\begin{gathered}
 U=\lfloor N/2\rfloor-1,\qquad
 \mathcal K_N^<(w,x)=\sum_{j=0}^{U}e_j(w)e_j(x),\\
 K_N^<(t,u)=\mathcal K_N^<(-2\cos t,-2\cos u),\qquad
 \eta_N=(-1)^{N-1},\\
 C_{N,3}=e^{3\pi i(N-1)^2/(4N)},\qquad
 W_N(t)=\frac{e^{-iNt}}{(1-\eta_Ne^{-iNt})^2},\\
 g_N(t;w,u)=\sin t\,\mathcal K_N^<(w,-2\cos t)
                K_N^<(t,u)e^{3iNt^2/(4\pi)} .
\end{gathered}
\tag{1}
\]
The exact current on an oriented first-angle path \(\gamma\) is
\[
 I_N(w,u;\gamma)
       =-\frac{N^2C_{N,3}}{\pi i}
                        \int_\gamma g_N(t;w,u)W_N(t)\,dt .
\tag{2}
\]
Use the actual closing parameters \(K_g\) and \(M_g\), with
\(17/30<K_g<7/10\), \(M_g>321/100\), and set
\[
 u=\beta-iK,\qquad K=\frac{\pi K_g}{2\beta},
           \qquad\pi/2\le\beta\le2\pi/3,\qquad
 B(u)=\frac{M_g-(2\beta/\pi-1)K}{2}.
\tag{3}
\]
Thus adding half the outer exponential rate to an inner rate
means adding \((K_g-K)/2\).

Put \(a_0=2\pi/3\), \(a_1=5\pi/6\), \(h_0=1/10\).
Keep the original inner endpoint and fixed height
\[
 \Theta_N=\pi-\frac{2\pi\lfloor N/4000\rfloor}{N},
             \qquad 0<h_c\le1/2000,
\tag{4}
\]
as chosen in the original finite inner trace formula. For all
sufficiently large \(N\),
\(\pi-\pi/2000\le\Theta_N\le\pi-\pi/4000\).
Let \(\gamma_N\) have successive vertices
\[
 a_0-ih_0,\quad a_1-ih_0,\quad
                       \Theta_N-ih_0,\quad\Theta_N-ih_c .
\tag{5}
\]

**Theorem.** Uniformly on (3), for every real incoming color
\(w\in[-2,2]\), both parities, and all sufficiently large \(N\),
\[
 \frac{N^2}{\pi}\int_{\gamma_N}
                   |g_N(t;w,u)W_N(t)|\,|dt|
                      \le C e^{N(B(u)-1/400)} .
\tag{6}
\]
On a fixed complex neighborhood of \([-2,2]\) the same bound
holds with gap \(1/500\); every fixed ordinary incoming
derivative has that latter bound on a smaller neighborhood.

## 2. The row estimate and the first low endpoint

For \(z=a-ih\), define the entire shortened-row profile and its
maximum by
\[
\begin{aligned}
 V_z(y)&=\int_0^y\log|2\cos(2\pi x)+2\cos z|\,dx-2J(y),
                                  &&0\le y\le1/2,\\
 J(y)&=\int_0^y\log(2\sin\pi x)\,dx,\qquad
 m(a,h)=\max_{0\le y\le1/2}V_{a-ih}(y).
\end{aligned}
\tag{7}
\]
The [complete row-norm theorem](research_mixed_symmetric_closing_low_horizontal_norm.md)
proves, with every shortened index retained,
\[
 |K_N^<(t,u)|\le CN^A
           e^{N\{m(\Re t,-\Im t)+m(\beta,K)\}}.
\tag{8}
\]
It also proves that \(m(a,h)\) is nonincreasing in \(a\in[0,\pi]\),
and supplies
\[
 m(a_0,h_0)\le b_2-\frac{67}{72\pi}+\frac{19}{2800\pi},
       \qquad
 \Re\psi(a_0-ih_0,0)<\frac{47}{60},\qquad b_2<7/12 .
\tag{9}
\]
The first shortened kernel, uniformly over all real incoming
colors, satisfies
\[
 |\mathcal K_N^<(w,-2\cos t)|
       \le C_\tau e^{N(\Re\psi(t,0)+\tau)}
\tag{10}
\]
on the fixed compact first-angle paths here, for every
\(\tau>0\). This is the all-real incoming form of the original
slit-plane bound.

The [right row-curvature lemma](research_mixed_symmetric_closing_right_row_curvature.md)
gives
\[
 m_{hh}(\beta,h)<\frac4{3\pi}
           \quad(0\le h\le K(\beta)).
\]
Since \(m_h(\beta,0)=0\), the original real-angle comparison
therefore yields
\[
 m(\beta,K)\le b_2-\frac{1-\cos\beta}{2\pi}
                              +\frac{2K^2}{3\pi}.
\tag{11}
\]
The exact first crossing and sampling factor have rate
\(3ah_0/(2\pi)-h_0\). At \(a=a_0\) that rate is zero.
Consequently the upper rate of the integrand, with half the
outer rate attached and before the tolerance in (10), is at most
\[
 \Re\psi(a_0-ih_0,0)+m(a_0,h_0)+b_2
 -\frac{1-\cos\beta}{2\pi}
 +\frac{2K(\beta)^2}{3\pi}+\frac{K_g-K(\beta)}2 .
\tag{12}
\]

The last three terms have their maximum at \(\beta=\pi/2\).
Indeed their derivative, multiplied by \(2\pi\beta\), is
\[
 -\beta\sin\beta-\frac83K^2+\pi K
 \le-\frac\pi2+\frac{3\pi^2}{32}<0.
\tag{13}
\]
For the first inequality, \(\beta\sin\beta\) is concave on
\([\pi/2,2\pi/3]\) and both endpoint values are at least
\(\pi/2\). Also
\(\pi K-8K^2/3\le3\pi^2/32\) by completing the square.
The final strict inequality uses \(3\pi<16\).

Substituting (9) into (12), and using \(K_g<7/10\), bounds
the attached rate by
\[
 \frac{39}{20}-\frac{27647}{25200\pi}
 <\frac{321}{200}-\frac{2261}{554400}.
\tag{14}
\]
The first fraction follows from
\[
 \frac{67}{72}+\frac12-\frac{19}{2800}-\frac{49}{150}
                                      =\frac{27647}{25200}.
\]
The strict inequality in (14) uses \(\pi<22/7\).
Its reserve exceeds \(1/300\), since \(678300>554400\).

## 3. The whole low segment

For \(a_0\le a\le a_1\), the rate before attaching the outer
factor is
\[
 R(a,u)=\Re\psi(a-ih_0,0)+m(a,h_0)+m(\beta,K)
                              +\frac{3ah_0}{2\pi}-h_0 .
\tag{15}
\]
This decreases as \(a\) increases. The row maximum is
nonincreasing. For the first-edge derivative, put
\(q=\cosh h_0<101/100\). Then
\[
 \Re\tan((a-ih_0)/2)=\frac{\sin a}{q+\cos a}>1
                                      \quad(a_0\le a\le a_1).
\tag{16}
\]
To verify the inequality throughout the interval, its derivative
has the sign of \(1+q\cos a>0\). At its left endpoint its
value exceeds \((5/6)/(51/100)=250/153>1\), using
\(\sqrt3/2>5/6\). The positive-real-part property of the principal
return gives
\(\Re\operatorname{arsinh}(\tan((a-ih_0)/2))>\operatorname{arsinh}1>1/2\).
For the latter comparison, the positive series gives
\(\sinh(1/2)\le12/23<1\).
Thus
\[
 \partial_a\Re\psi(a-ih_0,0)<-\frac1{2\pi},
                  \qquad \frac{3h_0}{2\pi}=\frac3{20\pi}.
\tag{17}
\]
Equations (15)--(17) prove the claimed decrease, including
one-sided limits if needed for the row maximum.

The complete sampling denominator is uniformly bounded below
on the line at height \(h_0\). Use \(\tau=1/10000\) in (10)
and absorb all polynomial factors, including \(N^2/\pi\),
using another \(1/10000\). The reserve in (14) then still
exceeds \(1/400\). This proves (6) on the first segment of (5).

## 4. The far horizontal and the endpoint vertical

The original slit-plane theorem, using its full real outside
period and the exact degree \(U<N/2\), gives on the remaining
two segments, for each fixed \(\tau>0\),
\[
 |\mathcal K_N^<(w,-2\cos(a-ih))K_N^<(a-ih,u)|
 \le C_\tau N^A e^{N\{2\Re\psi(a-ih,0)+K/2+2\tau\}}.
\tag{18}
\]
It applies uniformly to every real incoming color and every
real outgoing angle. The spectral first-angle image is a
fixed compact subset of the slit plane because
\(a\le\pi-\pi/4000\) and \(h_c\le h\le1/10\).

The existing far first-edge estimate is
\[
 2\Re\psi(a-ih,0)<\frac{13}{12}+h
                \qquad(5\pi/6\le a<\pi,\ 0\le h\le1/10).
\tag{19}
\]
Multiplication by the original crossing and full sampling
factor bounds the rate by
\[
 \frac{13}{12}+\frac K2+\frac3{20}+2\tau .
\]
After half the outer rate is attached, this is
\[
 \frac{13}{12}+\frac{K_g}{2}+\frac3{20}+2\tau
                         <\frac{19}{12}+2\tau .
\tag{20}
\]
The gap between \(321/200\) and \(19/12\) is \(13/600\),
larger than the low-segment reserve required in (6).
The denominator estimate uses the fixed \(h_c>0\); on the
endpoint column the exact midpoint denominator is even
\((1+e^{-Nh})^2\). Taking \(\tau=1/10000\) and absorbing
the polynomial factors proves (6) on both remaining segments.

The integrand is a polynomial of degree at most \(U<N/2\) in
the incoming color \(w\). Apply a filled Bernstein ellipse of
parameter \(\exp(1/4000)\) to the pointwise all-real bound,
before integrating. The degree costs at most \(N/8000\).
Absorb its coefficient count using another \(1/8000\).
The resulting gap exceeds \(1/500\), since
\(1/400-1/4000>1/500\). Cauchy's formula on smaller
neighborhoods proves the derivative assertion.

## 5. The far physical terms in the original trace identity

The exact sampling formula from the
[original inner remainder theorem](research_mixed_symmetric_closing_fixed_low_remainder.md),
Section 2, remains applicable on (3). Its far-sample estimate
used the outgoing angle only through
\[
 |e_j(-2\cos u)|\le CN^A e^{N(b_2+K/2)}
                                      \qquad(0\le j\le U),
\tag{21}
\]
which follows from the real-period norm and polynomial degree
and holds for every real part of \(u\). The same estimate
holds for the first real incoming color in its original
finite range.

Consequently its discarded far physical samples, their first
normal derivatives, and the two short midpoint verticals
have attached rate at most
\[
 2b_2+\frac K2+\frac3{2000}+\frac{K_g-K}{2}
             <\frac{91}{60}+\frac3{2000}.
\tag{22}
\]
The Markov and Bernstein-ellipse arguments in that sampling
proof retain every double-root normal and the odd simple
node. Its algebraic identity and prefactor are unchanged.
Since
\[
 \frac{321}{200}
     -\left(\frac{91}{60}+\frac3{2000}\right)-\frac1{20}
                      =\frac{221}{6000}>0 ,
\]
these terms have gap \(1/20\) below \(B(u)\) after polynomial
costs. The same statement, with a smaller fixed gap if
necessary, holds near the real incoming interval.

Thus a full two-short-edge trace may be represented by its
original lower-half-plane integral with these far errors
already controlled; (6) controls that integral after its
first angle reaches \(2\pi/3-i/10\). The positive central path,
its right-face vertical down to this point, and any high-depth
endpoint contribution are not estimated by this note.

## Source bindings

- Complete diagonal row profile, all indices, and first-endpoint bounds:
  [row-norm theorem](research_mixed_symmetric_closing_low_horizontal_norm.md),
  0393c562e44904a7976d3cf809af931d24e818e084235e4d9f5d452e6c3176da.
- Curvature on the right hyperbola:
  [right row-curvature lemma](research_mixed_symmetric_closing_right_row_curvature.md),
  735cc89d293ff7e6a959cc8da632d16d27c12b285e3cfbeddf3ecb11b1986814.
- First-short and all-real incoming bounds, with the entire outside period:
  [slit-plane theorem](research_mixed_next_first_short_edge_slit_plane_bound.md),
  efe1c1c89bb01f5a0aca9468917595926648780bca265f73000ede095f432e7b.
- Original exact trace formula, far physical terms and far first-edge estimate:
  [inner remainder theorem](research_mixed_symmetric_closing_fixed_low_remainder.md),
  03accd56435b7c00be36b89a5e2ffcee70ae84027ad918a6b3b1dca204825ab0.
- Original geometric floor:
  [far-right connection theorem](research_mixed_symmetric_closing_right_far_connection.md),
  dd3322925c80e58eaf22af936e5653945532f1b6de6b4044c047d92348211835.
