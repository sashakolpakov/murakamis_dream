# The central positive Newton envelope exceeds the outer-mode budget

Private exact source deduction, 8 November 2026. No mathematical
numerical evaluation, saved-value calculation, or frozen-source edit
is used.

The actual Fourier-degree weight of the outgoing polynomial removes
its growth on an outer contour of depth \(1/2\). It does not make the
positive Newton estimate for the remaining inner three-kernel
sufficient. Already the constant outer mode has the explicit
retained-row obstruction proved below. This is not a lower bound
for a signed kernel or trace.

## 1. The exact positive envelope being tested

Use the original notation and complete trace conventions from
[the thin-strip source theorem](research_mixed_next_three_outer_mode_thin_strip_obstruction.md),
including
\[
 D=N-1,\quad M=\lceil N/2\rceil,\quad
 \eta_N=(-1)^D,\quad
 W_N(z)=\frac{e^{-iNz}}{(1-\eta_Ne^{-iNz})^2},
\]
\[
 e_a(x)=S_a^{-2}\prod_{\nu<a}(c_\nu-x),\qquad
 K_N(x,y)=\sum_{a=0}^{D}e_a(x)e_a(y).
 \tag{1}
\]
The constant outer response is
\[
 \mathcal L_{N,0}
 =\phi_N^{(x)}
       [R(x)^3e_M(x)\mathcal K_{3,N}(-2,x)],
\]
\[
 \mathcal K_{3,N}(-2,x)
 =\phi_N^{(y)}[R(y)^3K_N(-2,y)K_N(x,y)].
 \tag{2}
\]
The outer radical consumes its original normal, while the inner
trace in (2) retains all original normals.

For complex angular variables \(z,t\), define the full positive
Newton envelope
\[
\begin{split}
 \mathcal B_N(z,t)
 ={}&\left(\sum_{a=0}^{D}
       |e_a(-2)e_a(-2\cos t)|\right)\\
 &\times\left(\sum_{b=0}^{D}
       |e_b(-2\cos z)e_b(-2\cos t)|\right).
\end{split}
 \tag{3}
\]
This is the positive estimate obtained by taking absolute values
inside each of the two original bare kernels of the inner trace.
In the nested lower-horizontal expression, it gives the majorant
\[
\begin{split}
 \mathcal E_N(z,t)
 ={}&
 \left|\sin z\,e_M(-2\cos z)W_N(z)
                         e^{3iNz^2/(4\pi)}\right|\\
 &\times\left|\sin t\,W_N(t)e^{3iNt^2/(4\pi)}\right|
                         \mathcal B_N(z,t).
\end{split}
 \tag{4}
\]
The scalar and measure factors of the two complete traces are
polynomial in \(N\) or have modulus one. Their original endpoint
currents remain separate; none is omitted or estimated here.

**Proposition.** Uniformly for
\[
 z=\frac{\pi}{3}-ih,\quad 0<h\le\frac12,\qquad
 t=\frac{\pi}{3}-iH,\quad 0<H\le\frac45,
 \tag{5}
\]
at both parities and all sufficiently large \(N\), one has
\[
             \mathcal E_N(z,t)
                    \ge \exp N\left(B_f+\frac1{700}\right),
 \qquad B_f=\frac{77}{50}+\frac{\pi}{50}.
 \tag{6}
\]
The heights in (5) may depend on \(N\) and tend to zero.
The Chebyshev coefficient weight is one for this constant mode,
so it makes no change to (6).

## 2. One original Newton row and its exact real exponents

Put
\[
 J(x)=\int_0^x\log|2\sin\pi s|\,ds,\qquad
 c=-2J(1/6)=2J(5/6),
\]
\[
 V_{\theta-ih}(y)=
     \int_0^y\log|2\cos(2\pi s)+2\cos(\theta-ih)|\,ds
                        -2J(y).
 \tag{7}
\]
These are the original real and complex Newton exponents in
[the complete physical-three Fourier bound](research_mixed_next_physical_three_kernel_fourier_bound.md),
Section 2. In particular \(V_{\theta-ih}(y)\ge V_\theta(y)\)
for \(h\ge0\) and \(0\le y\le1/2\).

The sine-doubling identity gives
\[
 J(1/3)=\frac23J(1/6)=-\frac c3.
 \tag{8}
\]
This is also the exact identity in
[real-period Newton, Section 5](research_three_crossing_real_period_newton_bound.md).
With \(L(x)=\int_0^x\log|2\cos\pi s|\,ds=J(x+1/2)\),
the shifted-cosine formula then gives
\[
 V_0(1/6)=2L(1/6)-2J(1/6)=\frac{5c}{3},
\]
\[
 V_{\pi/3}(1/6)=L(1/3)+L(0)-2J(1/6)=\frac{3c}{2}.
 \tag{9}
\]

Keep the actual index \(a_N=\lfloor N/6\rfloor\) in each
sum in (3). All numerator factors of these terms stay away
from zero on the parameter set (5): at the real face their
cosine sums are at least \(1\), and adding imaginary height
cannot decrease their modulus. The ordinary midpoint product
estimate and the original sine-factorial estimate consequently
give a two-sided logarithmic estimate for these particular
terms, uniform at both parities and through zero height.
Rounding \(a_N/N\) to \(1/6\) changes it by \(O(\log N)\).
Thus
\[
\begin{split}
 \mathcal B_N(z,t)
 \ge C^{-1}N^{-A}
 \exp N\left\{
       \frac{5c}{3}
       +2V_{\pi/3-iH}(1/6)
       +V_{\pi/3-ih}(1/6)\right\}.
\end{split}
 \tag{10}
\]
This is a lower bound for the positive envelope because it keeps
one genuine summand in each positive sum. It does not replace
either coherent bare kernel by that summand.

## 3. The height costs and a rational strict comparison

The exact second-height derivative in the cited Fourier bound,
equation (17), simplifies here to
\[
 \frac{d^2}{dH^2}V_{\pi/3-iH}(1/6)
      =\frac{\sqrt3}{4\pi(2\cosh H-1)}.
 \tag{11}
\]
Indeed
\[
 \Re\frac1{\tfrac12+\cos(\pi/3-iH)}
                        =\frac1{2\cosh H-1}.
 \tag{12}
\]
This identity follows by writing the real and imaginary parts
of the denominator and using \(\sinh^2H=\cosh^2H-1\).
At \(H=0\) the first-height derivative is zero.

For \(0\le H\le4/5\), the positive cosh series gives
\[
 \cosh H
 \le 1+\frac{H^2/2}{1-H^2/12}
 \le 1+\frac{24}{71}=\frac{95}{71}<\frac75.
 \tag{13}
\]
The series bound uses the upper ratio \(H^2/12\) after the
quadratic term. Since \(\sqrt3>5/3\) and \(\pi<22/7\),
equations (11)--(13) imply
\[
 V_{\pi/3-iH}(1/6)
       \ge \frac{3c}{2}+\frac{175}{4752}H^2.
 \tag{14}
\]
For the other height it suffices to retain the weaker
\(V_{\pi/3-ih}(1/6)\ge3c/2\). Hence (10) gives the rate
\[
                       \frac{37c}{6}
                                  +\frac{175}{2376}H^2.
 \tag{15}
\]

The original radical cancellation is exact at both parities:
\[
 e_M(-2\cos z)W_N(z)=
 \begin{cases}
 \displaystyle\frac{e^{-iNz/2}}
                       {2N(1+e^{-iNz})},&N\ \text{even},\\[2mm]
 \displaystyle-\frac{\sin(z/2)e^{-iNz/2}}
  {2iN\cos^2(\pi/(2N))(1-e^{-iNz})},&N\ \text{odd}.
 \end{cases}
 \tag{16}
\]
At the real coordinate \(\pi/3\), the sine factors in
(4),(16) have moduli bounded below by positive constants.
The denominators \(1\pm e^{-iNz}\) have modulus at most
two. The outer factor in (4) therefore has a polynomial
lower bound: the radical loss \(e^{-Nh/2}\) cancels
the crossing modulus \(e^{Nh/2}\) exactly.

For the inner factor, \(|W_N(t)|\ge e^{-NH}/4\), while
its crossing modulus is \(e^{NH/2}\). It contributes only
the loss \(e^{-NH/2}\), up to a fixed factor.
Combining with (15) proves
\[
 \mathcal E_N(z,t)\ge C^{-1}N^{-A}
       \exp N\left\{\frac{37c}{6}-\frac H2
                                   +\frac{175}{2376}H^2\right\}.
 \tag{17}
\]
The expression in braces decreases as \(H\) ranges from
zero to \(4/5\).

There is an elementary rational lower bound for \(c\).
Since \(2\sin\pi s<2\pi s\) on \(0<s\le1/6\),
\[
 -J(1/6)>
       \frac16\{1-\log(\pi/3)\}
       >\frac16\left(1-\frac1{21}\right)
       =\frac{10}{63}.
 \tag{18}
\]
Here \(\pi/3<22/21\) and
\(\log(22/21)<1/21\). Thus \(c>20/63\), and the rate
in (17) is uniformly greater than
\[
 \frac{370}{189}-\frac25+\frac{14}{297}
       =\frac{16682}{10395}.
 \tag{19}
\]
Finally
\[
 B_f<\frac{561}{350},\qquad
 \frac{16682}{10395}-\frac{561}{350}
       =\frac{1421}{727650}>\frac1{600}.
 \tag{20}
\]
Absorbing the fixed polynomial cost in the difference
between \(1/600\) and \(1/700\) proves (6).

## 4. Exact scope of the obstruction

The test lies at a central positive real angle, away from
the angular endpoint currents. A full outer lower contour
crosses the real coordinate \(\pi/3\); a full inner lower
contour does so as well. Therefore a construction using
the positive Newton envelope (3) at that crossing, with
the stated height bounds, cannot obtain the rate \(B_f\).
Keeping the inner contour only to depth \(1/2\) is a
special case of this obstruction.

This does not preclude a different decomposition that
estimates the corresponding omitted real region coherently,
a deeper inner contour, or a coherent estimate for
\(\mathcal K_{3,N}\) on the displayed central region.
It makes no assertion about the sign or exponential rate
of \(\mathcal L_{N,0}\). In particular it does not disprove
the coefficient-weighted mode bound or suppression of
the actual polynomial insertion \(H_N\).
