# An elementary maximum theorem on the horizontal contour

Research note, 2 November 2026.

The exact double sum for two adjacent powers equal to two has a
distinguished complex critical point. The purpose of this note is
to prove that, on the horizontal contour through this point, the
real part of the phase has a unique global maximum there. The proof
uses explicit first derivatives to locate the maximum and a
uniform Hessian estimate on the resulting rectangle.

This is one part of a contour argument. It does not estimate the
faces joining the original summation region to the horizontal
contour, nor does it estimate nonzero Fourier modes of the lattice
sum. Consequently it does not, by itself, prove the asymptotic
formula for the entire original source.

## 1. The phase and its branch

Use the phase and branches of
[the exact adjacent-pair calculation](research_adjacent_two_crossing_pair.md).
At zero remaining boundary angle, the phase is
\[
 W(x,y)=J(x+y)-3J(x)-6J(y)+J(2y)
       +i\pi(x^2-xy+y^2/2+x+y/2),
 \tag{1}
\]
where \(J'(z)=\log(2\sin\pi z)\) continues from the interval
\(0<z<1\). In the upper half-plane this branch is
\[
 J(z)=\frac{i\pi}{2}z(1-z)
   +\frac{\pi^2/6-\operatorname{Li}_2(e^{2\pi iz})}{2\pi i}.
 \tag{2}
\]
The series defining the dilogarithm is absolutely convergent here.
Equation (2) follows by differentiating and taking the limit at
zero, so it fixes the additive constant as well as the derivative.

Set
\[
 h_x=\frac{3\log2}{4\pi},\qquad h_y=\frac{\log7}{4\pi},\qquad
 x=\xi+ih_x,\quad y=\eta+ih_y,\qquad
 f(\xi,\eta)=\operatorname{Re}W(x,y).
 \tag{3}
\]
For later use, write
\[
 a=\frac1{\sqrt8},\quad b=\frac1{\sqrt7},\quad
 X=a e^{2\pi i\xi},\quad Y=b e^{2\pi i\eta},
 \qquad
 c_x=-3\log2+\frac{\log7}{2},\quad
 c_y=\frac{3\log2-\log7}{2}.
 \tag{4}
\]
Here \(c_x<0<c_y\).

**Theorem.** On the closed triangle
\[
 \mathcal P=\{(\xi,\eta):\xi\ge0,\ 0\le\eta\le1/2,\
                                      \xi+\eta\le1\},
 \tag{5}
\]
the function \(f\) has a unique maximum at
\[
 \xi_*=\frac{\arg(5+i\sqrt7)}{2\pi},\qquad \eta_*=\frac14.
 \tag{6}
\]
Every point outside the rectangle
\[
 \mathcal R=[3/50,1/10]\times[23/100,27/100]
 \tag{7}
\]
either has \(f<1/2\), or can be joined to a point of \(\mathcal R\)
by coordinate segments on which \(f\) strictly increases. On
\(\mathcal R\),
\[
 -D^2 f\succeq \frac{17\pi}{20}I.
 \tag{8}
\]
In particular, the same maximum theorem holds on the compact
polygon obtained by imposing
\(\xi\ge\epsilon,\ \epsilon\le\eta\le1/2-\epsilon,\
\xi+\eta\le1-\epsilon\), for \(0<\epsilon<1/100\).

## 2. Excluding the half with \(\xi\ge1/2\)

Substitution of (2) into (1) gives the exact identity
\[
 f(\xi,\eta)=\frac{\log7}{4}+c_x\xi+c_y\eta
  +\frac1{2\pi}\operatorname{Im}
       \left(3\operatorname{Li}_2(X)+6\operatorname{Li}_2(Y)
          -\operatorname{Li}_2(Y^2)-\operatorname{Li}_2(XY)\right).
 \tag{9}
\]
On \(1/2\le\xi\le1,\ 0\le\eta\le1/2\), the linear part is at most
\[
 \frac{\log7}{4}+\frac{c_x+c_y}{2}
     =\frac14\log(7/8)<0.
 \tag{10}
\]
Moreover, \(\operatorname{Im}\operatorname{Li}_2(X)\le0\).
For a proof of this sign, fix the argument \(\alpha\in[\pi,2\pi]\)
and differentiate \(\operatorname{Im}\operatorname{Li}_2(r e^{i\alpha})\)
in \(r\). The result is
\(-\arg(1-r e^{i\alpha})/r\le0\), and the value at \(r=0\) is zero.

For \(0\le r<1\), the absolutely convergent series gives
\[
 |\operatorname{Li}_2(z)|
 \le r+\frac{r^2}{4(1-r)}
 \quad (|z|\le r).
 \tag{11}
\]
The right side increases with \(r\). Since
\[
 |Y|<2/5,\qquad |Y^2|=1/7,\qquad |XY|<1/7,
\]
we obtain from (9)--(11)
\[
 f<\frac{6(7/15)+2(25/168)}{2\pi}
   =\frac{1301}{840\pi}
   <\frac{1301}{2604}<\frac12.
 \tag{12}
\]
Only \(\pi>31/10\) was used in the last step.
The exact selected value \(M=f(\xi_*,1/4)\) satisfies
\(M>3/4\), by the rational dilogarithm estimate in
[the tail calculation, Section 4](research_adjacent_two_crossing_global_tails.md).
Thus no point of this half can maximize \(f\).

## 3. The first derivatives confine the maximum

Differentiating (9), or using (1), gives
\[
 \begin{aligned}
 f_\xi&=c_x+\log|1-XY|-3\log|1-X|,\\
 f_\eta&=c_y+\log|1-XY|+
                         2\log|1+Y|-4\log|1-Y|.
 \end{aligned}
 \tag{13}
\]
These identities contain the complete real derivatives; no
argument or logarithmic winding is being discarded.

We use the following elementary bounds:
\[
 \begin{gathered}
 \frac18<\sin(\pi/25)<\frac{126}{1000},\qquad
 \cos(3\pi/25)>\frac{929}{1000},\qquad
 \frac45<\cos(\pi/5)<\frac{810}{1000},\\
 \frac{707}{1000}<\frac1{\sqrt2}<\frac{708}{1000},
 \qquad ab<\frac{134}{1000},\qquad
 \frac{1069}{1000}<\sqrt{\frac87}<\frac{1070}{1000},
 \qquad b>\frac{377}{1000}.
 \end{gathered}
 \tag{14}
\]
The square-root bounds follow by squaring positive rational
numbers. For the trigonometric bounds, use
\(157/50<\pi<22/7\), the alternating sine and cosine series,
and the exact value \(\cos(\pi/5)=(1+\sqrt5)/4\).
The estimates are deliberately wider than their exact values.

First fix \(0\le\xi\le1/2\). Write
\(\beta=2\pi\eta\). Exponentiating the second equation of (13)
gives
\[
 e^{f_\eta}=\sqrt{\frac87}\,|1-XY|\,
   \frac{8/7+2b\cos\beta}{(8/7-2b\cos\beta)^2}.
 \tag{15}
\]
The last ratio increases strictly with \(\cos\beta\), since both
its numerator and the reciprocal of its denominator do so.
For \(0\le\eta\le23/100\),
\(\cos\beta\ge\sin(\pi/25)>1/8\). The elementary bounds
\[
 |1-XY|>866/1000,\quad
 8/7+2b\cos\beta>1237/1000,\quad
 8/7-2b\cos\beta<1049/1000
\]
therefore imply
\[
 e^{f_\eta}>
 \frac{1069\cdot866\cdot1237}{1000\cdot1049^2}
 =\frac{572578849}{550200500}>1.
 \tag{16}
\]
For \(27/100\le\eta\le1/2\), the same calculation with
\(\cos\beta\le-1/8\) gives
\[
 e^{f_\eta}<
 \frac{1070\cdot1134\cdot1049}{1000\cdot1237^2}
 =\frac{63641781}{76508450}<1.
 \tag{17}
\]
Thus moving \(\eta\) toward \([23/100,27/100]\) strictly
increases \(f\), unless \(\eta\) is already in that interval.

Now suppose \(23/100\le\eta\le27/100\). If
\(0\le\xi\le3/50\), then
\[
 \cos(2\pi(\xi+\eta))\le\sin(\pi/25),\qquad
 \cos(2\pi\xi)\ge\cos(3\pi/25).
 \tag{18}
\]
Since \(e^{2c_x}=7/64\), the first equation of (13) and
(14) imply
\[
 e^{2f_\xi}>
 \frac{7}{64}\,
 \frac{1+1/56-(268/1000)(126/1000)}
      {[9/8-(707/1000)(929/1000)]^3}
 =\frac{107634750000000000}{102632729679481373}>1.
 \tag{19}
\]
For \(1/10\le\xi\le1/2\), no restriction on \(\eta\) is
needed: \(|1-XY|<1134/1000\) and
\(\cos(2\pi\xi)\le\cos(\pi/5)\) give
\[
 e^{2f_\xi}<
 \frac{7}{64}\,
 \frac{(1134/1000)^2}
      {[9/8-(708/1000)(810/1000)]^3}
 =\frac{6029296875}{7191281536}<1.
 \tag{20}
\]
Consequently a maximum in the square
\([0,1/2]\times[0,1/2]\) must lie in \(\mathcal R\).
More explicitly, first move the second coordinate toward its
specified interval, then move the first coordinate toward its
specified interval. Equations (16)--(20) show that each
nontrivial segment increases \(f\). These movements stay in
\(\mathcal P\). They also stay in the smaller polygon in the
theorem: decreasing a coordinate preserves the diagonal
constraint, while each required increase finishes with
\(\xi+\eta\le77/100\).

## 4. Strict concavity in the small rectangle

For \(x=\xi+ih_x,\ y=\eta+ih_y\), put
\[
 A=\operatorname{Re}\cot(\pi x),\quad
 B=\operatorname{Re}\cot(\pi y),\quad
 D=\operatorname{Re}\tan(\pi y),\quad
 C=\operatorname{Re}\cot(\pi(x+y)).
 \tag{21}
\]
The imaginary quadratic polynomial in (1) has zero real
Hessian on a horizontal contour. Using
\(2\cot(2z)=\cot z-\tan z\), one finds
\[
 D^2f=\pi\left[
 C\begin{pmatrix}1&1\\1&1\end{pmatrix}
 -\begin{pmatrix}3A&0\\0&4B+2D\end{pmatrix}\right].
 \tag{22}
\]
The real trigonometric formulas are
\[
 \begin{aligned}
 A&=\frac{\sin(2\pi\xi)}
           {9\sqrt2/8-\cos(2\pi\xi)},\\
 B&=\frac{\sin(2\pi\eta)}
           {4/\sqrt7-\cos(2\pi\eta)},\qquad
 D=\frac{\sin(2\pi\eta)}
           {4/\sqrt7+\cos(2\pi\eta)},\\
 C&=\frac{\sin(2\pi(\xi+\eta))}
           {57/(4\sqrt{14})-\cos(2\pi(\xi+\eta))}.
 \end{aligned}
 \tag{23}
\]
On \(\mathcal R\), the following coarse bounds suffice:
\[
 A>\frac9{20},\qquad B,D>\frac{99}{173},\qquad C<\frac14.
 \tag{24}
\]
Here are the details. For \(A\), the numerator is greater than
\(\sin(3\pi/25)>9/25\), while the denominator is less than
\(8/5-4/5=4/5\). For \(B,D\), the numerator is greater than
\(\cos(\pi/25)>99/100\), and both denominators are less than
\(8/5+13/100=173/100\). Finally,
\(\xi+\eta\in[29/100,37/100]\), so
\[
 \cos(2\pi(\xi+\eta))
 \le-\sin(2\pi/25)<-1/5,\qquad
 \frac{57}{4\sqrt{14}}>\frac{19}{5}.
 \]
The denominator in \(C\) is therefore greater than four and
its numerator is at most one. All these sine and cosine
estimates follow from the same alternating-series bounds used
in (14).

For every real vector \(v=(v_1,v_2)\),
\((v_1+v_2)^2\le2(v_1^2+v_2^2)\). Equations (22)--(24)
consequently give
\[
 \begin{aligned}
 -v^T D^2f\,v
 &>\pi\left[
       \left(\frac{27}{20}-\frac12\right)v_1^2+
       \left(\frac{594}{173}-\frac12\right)v_2^2\right]\\
 &\ge\frac{17\pi}{20}(v_1^2+v_2^2).
 \end{aligned}
 \tag{25}
\]
This proves (8).

The exact critical point (6), whose unexponentiated derivatives
vanish by the adjacent-pair calculation, lies inside
\(\mathcal R\). For example,
\[
 \frac{3\pi}{25}
 <\frac{5\sqrt7}{32}
 <\arctan(\sqrt7/5)
 <\frac{\sqrt7}{5}<\frac{\pi}{5}.
 \]
The middle lower bound follows by integrating
\((1+t^2)^{-1}\ge(1+7/25)^{-1}\) from zero to \(\sqrt7/5\).
Strict concavity proves that this point is the unique maximum
in \(\mathcal R\). Sections 2 and 3 exclude every point outside
the rectangle, completing the proof.

## 5. What this adds to the contour problem

The argument is entirely algebraic and elementary after the
canonical dilogarithm expansion. Its useful feature is that
global concavity is unnecessary. The one-variable logarithmic
terms confine a possible maximum, and the coupling through
\(XY\) is weak enough for the remaining Hessian estimate.

On any fixed compact subset of \(\mathcal P\) excluding a
neighborhood of \((\xi_*,1/4)\), continuity and uniqueness give
a positive gap below \(M\). Near the maximum, (25) gives an
explicit quadratic loss. These facts justify the horizontal
part of a local stationary-phase argument.

For comparison, an [independent interval proof](research_adjacent_two_crossing_horizontal_maximum.md)
establishes the same maximum and an explicit exterior gap of
\(1/10000\). Its rational calculation is implemented in
[the verification script](../experiments/verify_adjacent_two_crossing_horizontal_maximum.py);
its saved output is
[here](../repro/results/research-adjacent-two-crossing-horizontal-maximum.json).
The proof above does not depend on that computation.

The missing steps remain specific: the interpolation of the
finite factorial sum must be deformed to this contour with
controlled connecting faces, and its other lattice modes must
be bounded below the selected exponential rate. Neither the
finite coefficient identity nor the maximum theorem replaces
those steps.
