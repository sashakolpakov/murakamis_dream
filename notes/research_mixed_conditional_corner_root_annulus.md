# A strict annulus for the original conditional root at the inward seam

Private research proof, 8 November 2026. The original type-four
conditional root extends to the closed inward seam and satisfies
\(1/2<|v|<2\) on the full incoming corner rectangle. The lower
radius bound follows from an explicit exclusion of the upper
semicircle \(|v|=1/2\); it does not use a phase evaluation.

This is a root and phase-domain result. It does not estimate the
retained finite integral, prove a lower bound for its critical real
coordinate, or establish a Gaussian approximation.

## 1. Parameters, original branch, and the closed seam

Keep
\[
\begin{gathered}
a=x-i\eta,\qquad \frac12\le x\le\frac7{10},\qquad
0\le\eta\le\frac9{125},\\
y=q-i\xi,\qquad 0\le q\le\frac{11}{50},\qquad
\frac1{1000}\le\xi\le\frac{51}{500},\\
X=e^{-2\pi ia},\qquad Y=e^{-2\pi iy}.
\end{gathered}                                                    \tag{1}
\]
The elementary exponential bounds already used in
[the original lower-output reduction, Section 5](research_mixed_conditional_lower_output_middle_reduction.md)
give
\[
\Re X<0,\quad \Im X\ge0,\quad \frac58<|X|\le1,
\qquad \frac12<|Y|<1,\quad \Im Y\le0.
                                                               \tag{2}
\]
In particular \(|X|^2(3-2\Re X)>1\).

Use the original phase, including its chirp and primitive constant,
\[
Q(t;a,y)=g(a+t)+g(y+t)-3g(t)-g(a)-g(y)+2\pi iat,
\qquad g'(z)=\Log(1-e^{-2\pi iz}).                              \tag{3}
\]
Its exponential critical equation is
\[
v(v-X)(v-Y)=X(v-1)^3,
\qquad v=e^{2\pi it},                                         \tag{4}
\]
or
\[
(1-X)v^3+(2X-Y)v^2+X(Y-3)v+X=0.                              \tag{5}
\]
For \(q>0\), [the algebraic transport theorem](research_mixed_four_conditional_algebraic_transport_domain.md)
gives a unique simple upper-half-plane root, with
\[
0<\arg v<\arg X,\qquad
t=\frac{\Log v}{2\pi i},\qquad Q_t(t;a,y)=0.                  \tag{6}
\]
We first verify that this same branch extends through \(q=0\).

At \(X=-\rho\), \(Y=R\), where \(5/8\le\rho\le1\) and
\(1/2<R<1\), (5) becomes the real cubic
\[
(1+\rho)v^3-(2\rho+R)v^2+\rho(3-R)v-\rho.                    \tag{7}
\]
One quarter of the discriminant of its derivative is
\[
R^2+(7\rho+3\rho^2)R-5\rho^2-9\rho
<1-2\rho-2\rho^2<0.                                        \tag{8}
\]
The first expression increases with \(R\). Thus the cubic is
strictly increasing on the real axis and has one simple real root
and a simple conjugate pair. Its unique upper root persists under
a small displacement to \(\Im Y<0\), where it must equal the
unique upper root of (6).

For \(\Im X>0\), a real root of (5) would satisfy
\[
Y=v-\frac{X(v-1)^3}{v(v-X)},\qquad
\Im Y=-\frac{(v-1)^3\Im X}{|v-X|^2}.                         \tag{9}
\]
The values \(v=0,1,X\) are excluded by (4) and \(R<1\).
At real \(Y=R\), (9) therefore excludes every real root.
For each fixed \(X\) with \(\Im X>0\), approach this value of
\(Y\) from \(\Im Y<0\). No root reaches the real axis at the
endpoint, and none escapes to infinity: \(1-X\) stays away from
zero and the coefficients remain bounded. The already known upper
root count one therefore persists, counting multiplicity. Together
with (7)--(8), this proves simplicity and continuation on the
entire closed domain (1).

The prewall ray exclusion of the algebraic theorem also remains
strict. On \(v=sX\), \(s>1\), its first numerator in equation
(12) is positive, so \(\Im Y>0\) if \(\Im X>0\). For
\(0<s<1\), its second numerator implies \(\Re Y>1\).
For negative real \(X\), that ray is outside the upper half-plane.
Consequently (6) still gives
\[
                         0<\Re t<1-x.                       \tag{10}
\]
At the seam the logarithm in \(g'(y)\) is regular because
\(|Y|<1\); its value is the limit from the original strip.
The other arguments in (3) remain strictly inside their regular
real strips. Continuity therefore preserves the original zero
lift in (6), rather than just its exponential equation.

## 2. Exclusion of the full upper semicircle

We prove a slightly more general algebraic statement. Suppose
\[
\Re X<0,\quad |X|\ge\frac58,\qquad
Y=a_0-ib_0,\quad b_0\ge0,\quad \frac12<R:=|Y|\le1.          \tag{11}
\]
No upper-half-plane solution of (4) has modulus \(1/2\).
The proof of this exclusion does not require a sign for \(\Im X\).

Suppose instead that
\[
v=r+it_0,\qquad t_0>0,\qquad r^2+t_0^2=\frac14.
\]
Solving (4) for \(X\) gives
\[
X=\frac{v(v-Y)}{L-Y},\qquad
L=v^2-2v+3-\frac1v.                                         \tag{12}
\]
On this semicircle write
\[
\ell:=\Re L=2r^2-6r+\frac{11}{4},\qquad
m:=\Im L=2(r+1)t_0>0.                                      \tag{13}
\]
In particular \(L-Y\ne0\).

### The part \(r\le2/5\)

Direct expansion gives
\[
\begin{split}
\Delta&:=|L-Y|^2-\frac{16}{25}|v-Y|^2\\
&=|L|^2-\frac4{25}+\frac9{25}R^2
 -2\left(\ell-\frac{16r}{25}\right)a_0
 +2\left(m-\frac{16t_0}{25}\right)b_0.                      \tag{14}
\end{split}
\]
Here
\[
m-\frac{16t_0}{25}
 =\left(2r+\frac{34}{25}\right)t_0>0,
\qquad
C(r):=\ell-\frac{16r}{25}
 =2r^2-\frac{166r}{25}+\frac{11}{4}
 \ge\frac{207}{500}.                                       \tag{15}
\]
The last polynomial is decreasing for \(-1/2<r\le2/5\).
Since \(a_0\le R\) and \(b_0\ge0\), the right side of
(14) is bounded below by
\[
|L|^2-\frac4{25}+\frac9{25}R^2-2C(r)R.
\]
Its derivative in \(R\le1\) is at most
\(18/25-414/500=-27/250<0\). Its minimum therefore occurs
at \(R=1\). Hence
\[
\begin{split}
\Delta&\ge |L-1|^2-\frac{16}{25}|v-1|^2\\
&=-32r^3+40r^2-\frac{443r}{25}+\frac{261}{80}=:P(r).
\end{split}                                                   \tag{16}
\]
The derivative \(-96r^2+80r-443/25\) is strictly negative:
its discriminant is \(-10112/25<0\). Thus
\[
                 P(r)\ge P(2/5)=\frac{1053}{2000}>0.
                                                               \tag{17}
\]
Equations (12) and (14) now imply
\(|X|<(1/2)/(4/5)=5/8\), contradicting (11).

### The part \(r\ge2/5\)

A second direct expansion of (12) is
\[
\begin{split}
|L-Y|^2\Re X={}&rR^2+
 \left(6r^2-\frac{13r}{4}-\frac14\right)a_0
 +t_0\left(10r-\frac{11}{4}\right)b_0\\
&-16r^3+6r^2+\frac52r-\frac{11}{16}.                         \tag{18}
\end{split}
\]
For \(2/5\le r\le1/2\), the coefficient of \(a_0\) is
negative and that of \(b_0\) is positive. It follows that
\[
\begin{split}
|L-Y|^2\Re X\ge f(r,R):={}&rR^2+
 \left(6r^2-\frac{13r}{4}-\frac14\right)R\\
&-16r^3+6r^2+\frac52r-\frac{11}{16}.                         \tag{19}
\end{split}
\]
For fixed \(R\le1\),
\(f_{rr}=12R-96r+12<0\), so its minimum is at one of the
two endpoints. There
\[
\begin{split}
f(1/2,R)&=\frac12\left(R-\frac14\right)
                      \left(R-\frac12\right)>0,\\
f(2/5,R)&=\frac25R^2-\frac{59}{100}R+\frac{497}{2000}>0.
\end{split}                                                   \tag{20}
\]
The discriminant of the latter quadratic is \(-99/2000<0\).
Thus (18) implies \(\Re X>0\), the other contradiction to
(11). This completes the semicircle exclusion.

## 3. The actual root lies outside the semicircle

At \(X=-\rho,Y=R\), let \(r_0\) denote the real root of
(7). The values at zero and one are \(-\rho\) and
\((1+\rho)(1-R)\), so \(0<r_0<1\). Vieta's product identity
for the conjugate pair gives
\[
|v_{\rm upper}|^2=\frac{\rho}{(1+\rho)r_0}
 >\frac{\rho}{1+\rho}\ge\frac5{13}>\frac14.                 \tag{21}
\]
Every point of (1) connects to such a seam anchor by first
reducing \(q\) to zero and then reducing \(x\) to \(1/2\),
with both radii fixed. The simple selected upper root continues
along this connected domain. Section 2 prevents it from crossing
\(|v|=1/2\), so it satisfies \(|v|>1/2\) everywhere.

The upper estimate \(|v|<2\) uses only \(|X|,|Y|\le1\),
\(x\ge1/2\), and the original zero lift. Indeed, if
\(|v|\ge2\), each of the three original logarithms
\[
\Log(1-X/v),\qquad \Log(1-Y/v),\qquad \Log(1-1/v)
\]
has argument of modulus at most \(\pi/6\). The last has
multiplicity three in \(Q_t\). Hence
\[
                 \Im Q_t\ge2\pi x-5\pi/6\ge\pi/6>0,
                                                               \tag{22}
\]
a contradiction. This part of the old root proof does not use
the former lower bound \(\Re y\ge11/50\).

We have therefore proved, on the full closed domain (1),
\[
\boxed{\qquad \frac12<|v|<2,
 \qquad |\Im t|<\frac{\log2}{2\pi},
 \qquad 0<\Re t<1-x.\qquad}                                  \tag{23}
\]
All strict separations are uniform on this compact domain.
The simple root and its original local phase extend to fixed
small complex neighborhoods. This assertion concerns the phase;
it makes no estimate for a finite polynomial in those neighborhoods.

In particular the old lower-index guard \(\Re t>2/25\) has
not been imported: its old proof used \(\Re y\ge11/50\).
To deform the middle integral in
[the current corner reduction](research_mixed_next_lower_left_corner_middle_reduction.md),
one must still justify a suitable real-coordinate guard, the
main-line curvature, and both unweighted connections with the
actual canonical amplitude. The present annulus supplies a
strict private-height domain for that remaining analysis only.
