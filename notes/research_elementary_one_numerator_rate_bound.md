# An elementary bound for the complete one-numerator rate

Private written proof, 11 November 2026. This note supplies a direct
analytic proof of the scalar estimate \(M_1(0)<7/15\) used in the
conditional-kernel bounds. It needs no numerical maximization or
saved numerical value. The strict estimate below is slightly stronger.

## 1. Statement and normalization

For \(0\le t\le1\), let
\[
 J(t)=\int_0^t\log(2\sin\pi u)\,du,\qquad
 L(t)=-2J((1-t)/2),\qquad F(t)=L(t)-2J(t).
 \tag{1}
\]
The endpoint integrals are improper integrals with their continuous
values. Define
\[
                         M_1(0)=\max_{0\le t\le1}F(t).
 \tag{2}
\]

**Proposition.** With the normalization (1),
\[
                         M_1(0)<\frac7{15}-\frac1{1000}.
 \tag{3}
\]

The proof uses only elementary calculus, the bounds
\(25/8<\pi<22/7\), and a finite alternating-series estimate.
In particular it does not assume a decimal approximation to
Catalan's constant.

## 2. Bounds on the sine integral

The elementary integral of the logarithm of sine gives
\[
 J(0)=J(1/2)=J(1)=0,\qquad J(1-t)=-J(t).
 \tag{4}
\]
For completeness, if \(I=\int_0^{\pi/2}\log(\sin x)\,dx\),
substitution \(x\mapsto\pi/2-x\) and the double-angle identity give
\(2I=I-(\pi/2)\log2\). Thus
\(I=-(\pi/2)\log2\), proving the middle equality in (4);
reflection then proves the other assertions.

On \([0,1/2]\), \(J\le0\), and its minimum is at \(1/6\),
because \(J'(t)=\log(2\sin\pi t)\). Strict concavity of sine
gives \(2\sin\pi t>6t\) for \(0<t<1/6\). Hence
\[
 -J(1/6)<-\int_0^{1/6}\log(6t)\,dt=\frac16,\qquad
                    0\le L(t)<\frac13.
 \tag{5}
\]
In particular \(F(t)\le L(t)<1/3\) for \(1/2\le t\le1\).

Let
\[
                    G=\sum_{k=0}^{\infty}\frac{(-1)^k}{(2k+1)^2}.
\]
Then
\[
                            -2J(1/4)=\frac G\pi.
 \tag{6}
\]
One can obtain (6) without any numerical evaluation. Expand
\(\log|1-r e^{2\pi iu}|=-\sum_{n\ge1}r^n\cos(2\pi nu)/n\)
for \(0<r<1\) and integrate on \([0,1/4]\).
The integrated series is absolutely convergent even at \(r=1\).
The logarithmic integrals converge to \(J(1/4)\): away from zero
the convergence is uniform; near zero, for \(r\ge1/2\),
\[
 |1-r e^{2\pi iu}|^2=(1-r)^2+4r\sin^2\pi u
                      \ge2\sin^2\pi u,
\]
which provides an integrable logarithmic majorant together with
the upper bound two. This proves (6).

Seven terms of the alternating series give
\[
 \begin{split}
 G&<
 1-\frac19+\frac1{25}-\frac1{49}+\frac1{81}
                 -\frac1{121}+\frac1{169}\\
 &=\frac{209}{225}-\frac{32}{3969}-\frac{48}{20449}\\
 &<\frac{209}{225}-\frac1{125}-\frac1{450}
   =\frac{689}{750}<\frac{23}{25}.
 \end{split}
 \tag{7}
\]
Here \(32\cdot125>3969\) and \(48\cdot450>20449\) justify the
two subtractions. Consequently
\[
                         -2J(1/4)<\frac{184}{625}.
 \tag{8}
\]

## 3. The maximum below one half

For \(0<t<1/2\), direct differentiation gives
\[
 \begin{split}
 F'(t)&=\log(2\cos(\pi t/2))-2\log(2\sin\pi t),\\
 F''(t)&=-\frac\pi2\tan(\pi t/2)-2\pi\cot(\pi t)<0.
 \end{split}
 \tag{9}
\]
At \(t=1/4\),
\[
                     F'(1/4)=\log\cos(\pi/8)\in(-1/12,0).
 \tag{10}
\]
To see the lower bound, \(\cos(\pi/8)>12/13\), since
\(\cos^2(\pi/8)=(2+\sqrt2)/4\) and
\(2\cdot169^2>238^2\). Also
\(\log(13/12)<1/12\).

Equation (9) implies that \(F\) decreases on \([1/4,1/2]\).
For \(0<t\le1/4\), it also gives \(F''(t)<-6\), because
\(\cot(\pi t)\ge1\) and \(\pi>3\).
The tangent-line inequality for the concave function
\(F(t)+3(t-1/4)^2\) therefore yields
\[
 F(t)\le F(1/4)+F'(1/4)(t-1/4)-3(t-1/4)^2
       < F(1/4)+\frac1{1728}.
 \tag{11}
\]
The bound extends to \(t=0\) by continuity. Together with
monotonicity on \([1/4,1/2]\), it applies throughout
\([0,1/2]\).

It remains to estimate \(F(1/4)\). The inequality
\(\log\cos x\le-x^2/2\), obtained by integrating
\(\tan x\ge x\), gives
\[
 \begin{split}
 L(1/4)
 &=2\int_0^{1/8}\log(2\cos\pi v)\,dv\\
 &\le\frac{\log2}{4}-\frac{\pi^2}{1536}
   <\frac7{40}-\frac3{512}.
 \end{split}
 \tag{12}
\]
Here \(\log2<7/10\): the first four terms of the positive
exponential series at \(7/10\) already exceed two.
Equations (8), (11), and (12) imply
\[
 \max_{0\le t\le1/2}F(t)
 <
 \frac7{40}+\frac{184}{625}-\frac3{512}+\frac1{1728}
 =
 \frac7{15}+\frac{41}{15000}-\frac3{512}+\frac1{1728}.
 \tag{13}
\]
The remaining comparison is rational:
\[
 \frac3{512}>\frac1{200},\qquad
 \frac1{1728}<\frac1{1500},\qquad
 \frac{41}{15000}<\frac1{300}.
\]
Thus the last expression in (13) is strictly smaller than
\[
 \frac7{15}+\frac1{300}-\frac1{200}+\frac1{1500}
                       =\frac7{15}-\frac1{1000}.
 \tag{14}
\]
The bound \(F<1/3\) on the other half, from (5), is smaller
still. This proves (3).

## 4. Use and limits

The proposition proves the scalar inequality appearing as
\(M_1(0)<7/15\) in
[the low-index kernel estimate](research_mixed_next_low_index_kernel_margin.md),
Lemma 1. The definitions of \(J,L,M_1(0)\) agree literally.
That note's finite-product bound supplies the separate implication
from this scalar maximum to a bound for every original finite row.

No cancellation or lower bound for a quantum invariant follows from
(3). This is an absolute upper rate for a positive majorant.
It may be used to estimate omitted rows in a contour proof only
with the other factors and their allocations retained.

There are no imported mathematical lemmas from project notes in
the proof above. The author has read the complete argument.
Independent full proof review is required before adoption.
No mathematical numerical evaluation, test, import, compilation,
or saved-value arithmetic was used.

