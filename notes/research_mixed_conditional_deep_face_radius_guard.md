# The conditional critical point stays below the incoming zero

Research deduction, 7 November 2026. On the deepest face of the
required incoming rectangle, the selected conditional critical
point has smaller imaginary height than the incoming factorial
zero. This is proved from the original critical equation, without
evaluating its root. It supplies a domain condition for extending
the retained contour through the physical wall.

This phase statement does not by itself establish that extended
finite-source contour or its asymptotic.

## 1. Statement and the original branch

Fix
\[
\begin{gathered}
 \eta_0=\frac9{125},\qquad a=x-i\eta_0,\qquad
                         \frac12\le x\le\frac7{10},\\
 y=z+iH,\qquad \frac{11}{50}\le z\le\frac9{20},\qquad
                         0\le H\le\frac1{100},\\
 X=e^{-2\pi ia},\qquad Y=e^{-2\pi iy}.
\end{gathered}                                                     \tag{1}
\]
The original phase is
\[
 Q(t;a,y)=g(a+t)+g(y+t)-3g(t)-g(a)-g(y)+2\pi iat,
 \qquad g'(q)=\Log(1-e^{-2\pi iq}).
                                                               \tag{2}
\]
Let \(t_*=u_*+ih_*\) be the selected branch from the
[negative-height theorem](research_mixed_conditional_negative_height_branch.md).
It has the original zero lift \(Q_t(t_*;a,y)=0\), and
\[
 \frac1{16}<u_*<1-x,\qquad
 -\Re Q_{tt}(u+i\sigma;a,y)>0
          \quad\left(\frac1{16}\le u<1-x,\ \sigma\in\mathbb R\right).
                                                               \tag{3}
\]
Its upper exponential root \(V=e^{2\pi it_*}\) is simple
and continuous throughout (1).

**Theorem.** Uniformly on the compact set (1),
\[
                         h_*<\eta_0,
             \qquad\text{equivalently}\qquad |V|>|X|.
                                                               \tag{4}
\]
The difference \(\eta_0-h_*\) has a positive minimum.

The proof excludes equality everywhere, then fixes the side
using a known branch value. Write
\[
                    T=e^{2\pi\eta_0},\qquad R=e^{2\pi H}.
                                                               \tag{5}
\]
The original elementary bounds give
\[
                \frac32<T<\frac85,\qquad 1\le R<\frac{15}{14}.
                                                               \tag{6}
\]
For the lower bound on \(T\), use
\(\log(3/2)<5/12<54/125<18\pi/125\).
The logarithm inequality follows from
\(\log q<(q-q^{-1})/2\) for \(q>1\), whose difference has
derivative \((q-1)^2/(2q^2)>0\).
The upper bound on \(T\) is proved in the
[lower-current theorem](research_mixed_conditional_negative_height_lower_currents.md).
For \(R\), that theorem gives
\(R<175/164<15/14\).

## 2. Two real-part restrictions at a putative crossing

Assume for contradiction that \(h_*=\eta_0\). For an arbitrary
real trial \(u\) on this height line, the exact force, including
the incoming carrier, is
\[
 |e^{Q_t(u+i\eta_0;a,y)}|^2
 =\frac{4T^2\sin^2\pi(x+u)\,
          |1-RT e^{-2\pi i(z+u)}|^2}
        {|1-T e^{-2\pi iu}|^6}.
                                                               \tag{7}
\]
The equality of the incoming and own radii in (7) is specific
to this putative crossing. It is not asserted at arbitrary
index heights.

At \(u=1/4\), the incoming angle satisfies
\(3/4\le x+u\le19/20\), so its numerator square is at most
\(2T^2\). The own square is \(1+T^2\). Thus
\[
 |e^{Q_t(1/4+i\eta_0)}|^2
  <f(T):=\frac{2T^2(1+(15/14)T)^2}{(1+T^2)^3}.
                                                               \tag{8}
\]
For any fixed \(c>0\), the logarithmic derivative of
\(2T^2(1+cT)^2/(1+T^2)^3\) has the sign of
\[
                      1-2T^2+cT(2-T^2).
                                                               \tag{9}
\]
This is negative for \(T\ge3/2\). Consequently
\[
              f(T)<f(3/2)=\frac{95922}{107653}<1.
                                                               \tag{10}
\]
Horizontal concavity in (3) and the actual zero derivative
at \(u_*\) therefore imply
\[
                               u_*<\frac14.
                                                               \tag{11}
\]
The trial \(1/4\) is strictly before the wall \(1-x\ge3/10\).

There is a stronger correlated restriction when \(x\ge13/20\).
Set
\[
                      b=\frac9{10}-x\in[1/5,1/4].
                                                               \tag{12}
\]
At this trial \(x+b=9/10\). Since
\(\sin(\pi/10)<1/3\), the incoming square in (7) is
less than \(4T^2/9\). Also
\(\cos(2\pi b)\le\cos(2\pi/5)<1/3\), so the own square
\(D=|1-T e^{-2\pi ib}|^2\) obeys
\[
 \frac DT>T+T^{-1}-\frac23>\frac32.
                                                               \tag{13}
\]
Here \(T+T^{-1}\) increases for \(T>1\), and (6) was used.
The two trigonometric bounds follow from the exact value
\((\sqrt5-1)/4<1/3\).
For the outgoing modulus,
\[
 |1-RT e^{-2\pi i(z+b)}|
       \le1+RT<T\left(\frac23+\frac{15}{14}\right)
                              =\frac{73T}{42}<\frac{7T}{4}.
                                                               \tag{14}
\]
Substitution into (7) gives
\[
 |e^{Q_t(b+i\eta_0)}|^2
       <\frac{(4/9)T^2(49/16)T^2}{(27/8)T^3}
        =\frac{98T}{243}<\frac{784}{1215}<1.
                                                               \tag{15}
\]
Again (3) puts the actual critical point to the left:
\[
                   u_*<\frac9{10}-x\qquad(x\ge13/20).
                                                               \tag{16}
\]
Both trials and the full segments used for concavity stay
inside the original primitive strip.

## 3. The imaginary critical equation cannot vanish there

For \(s\in(0,1)\) and \(h>0\), define the real functions
\[
 B_h(s)=\arctan\{\cot(\pi s)\tanh(\pi h)\},\qquad
 D_h(s)=\frac{\sinh(2\pi h)}
                   {\cosh(2\pi h)-\cos(2\pi s)}.
                                                               \tag{17}
\]
The arctangent is in \((-\pi/2,\pi/2)\).
Direct differentiation gives
\[
                             B_h'(s)=-\pi D_h(s).
                                                               \tag{18}
\]
On \(1/4<s<3/4\) one has \(0<D_h(s)<1\).
On \(1/5\le s\le1/4\),
\[
 D_{\eta_0}(s)\ge\tanh(2\pi\eta_0)
       =\frac{T^2-1}{T^2+1}>\frac5{13}>\frac13.
                                                               \tag{19}
\]

On the crossing line, the incoming factorial argument
\(a+u+i\eta_0=x+u\) is real and in \((1/2,1)\).
Using the original arguments of all three logarithms gives
the exact identity
\[
\begin{split}
 I(u;x,z,H)
  &:=\Im Q_t(u+i\eta_0;a,y)\\
  &=\pi(x-z+u-1/2)
       +B_{\eta_0+H}(z+u)-3B_{\eta_0}(u).
\end{split}                                                       \tag{20}
\]
For example the incoming argument is
\(\pi/2-\pi(x+u)\); the outgoing and own arguments are
\(\pi/2-\pi(z+u)+B_{\eta_0+H}(z+u)\) and
\(\pi/2-\pi u+B_{\eta_0}(u)\).
Together with the carrier \(2\pi x\) these give (20)
without an integer logarithmic shift.

On \(1/16\le u\le1/4\) and the outgoing range (1),
\(1/4<z+u<3/4\). Equations (18)--(19) show
\[
 \partial_u I
     =\pi\{1-D_{\eta_0+H}(z+u)+3D_{\eta_0}(u)\}>0,\qquad
 \partial_z I=-\pi\{1+D_{\eta_0+H}(z+u)\}<0.
                                                               \tag{21}
\]
After decreasing \(z\) to \(11/50\), the argument
\(z+u\) is below \(1/2\). Its cotangent is positive, so
increasing \(H\) to \(1/100\) increases the remaining
outgoing \(B\) term.

If \(x\le13/20\), (11), (21), and \(\partial_x I=\pi\)
therefore give
\[
 I(u_*;x,z,H)
       \le I(1/4;13/20,11/50,1/100).
                                                               \tag{22}
\]
If \(x\ge13/20\), first apply (16), (21), and the same
outgoing comparisons. It remains to maximize
\[
 I(b;9/10-b,11/50,1/100),\qquad 1/5\le b\le1/4.
                                                               \tag{23}
\]
Its linear term is constant. Its derivative with respect
to \(b\) is
\[
       \pi\{3D_{\eta_0}(b)-D_{\eta_0+1/100}(11/50+b)\}>0
                                                               \tag{24}
\]
by (19) and \(D_{\eta_0+1/100}(11/50+b)<1\).
Thus (22) holds in this case as well.

The right side of (22) is strictly negative. Here are
explicit elementary witnesses. First,
\[
 \cot(47\pi/100)=\tan(3\pi/100)<\frac1{10},\qquad
 \tanh(41\pi/500)<\frac{13}{50}.
                                                               \tag{25}
\]
For the first inequality use \(3\pi/100<2/21\) and
\(\tan s\le s/(1-s^2/2)\), giving
\(\tan(3\pi/100)<42/439<1/10\).
The second follows from \(\tanh s<s\) and \(\pi<22/7\).
Also
\[
 \tanh(\pi\eta_0)>
 \tanh(3/14)\ge\frac3{14}-\frac{(3/14)^3}{3}
                 =\frac{579}{2744}>\frac{21}{100}.
                                                               \tag{26}
\]
Here \(\pi\eta_0>27/125>3/14\).
The inequality \(\tanh s\ge s-s^3/3\) follows by
differentiation from \(\tanh s\le s\).
Finally
\[
 \arctan(21/100)>
       \frac{21}{100}-\frac{(21/100)^3}{3}>\frac15.
                                                               \tag{27}
\]
The last cubic term is smaller than \(1/192<1/100\).
Equations (25)--(27), together with \(\arctan q<q\)
for \(q>0\), yield
\[
\begin{split}
 I(1/4;13/20,11/50,1/100)
  &=\frac{9\pi}{50}
       +B_{41/500}(47/100)-3B_{\eta_0}(1/4)\\
  &<\frac{99}{175}+\frac{13}{500}-\frac35
    =-\frac{29}{3500}<0.
\end{split}                                                       \tag{28}
\]
This contradicts the original critical equation
\(\Im Q_t(t_*;a,y)=0\). Therefore equality \(h_*=\eta_0\)
is impossible anywhere in (1).

## 4. Fixing the side and the precise consequence

The parameter set (1) is connected. The selected critical
root is continuous and no equality in (4) occurs, so
the sign of \(h_*-\eta_0\) is constant there.
At \(x=1/2,z=2/5,H=0\), Section 4 of the
[wall-gap completion theorem](research_mixed_conditional_wall_gap_completion.md)
proves \(h_*<0\) by an exact unit-root exclusion.
This is the same selected branch at the full depth
\(\eta_0\). It fixes the negative sign throughout (1),
proving (4). Compactness gives a positive minimum for
\(\eta_0-h_*\).

Thus the incoming numerator argument on the horizontal
critical line has uniformly negative imaginary part:
\[
                    \Im(a+t)=h_*-\eta_0<0.
                                                               \tag{29}
\]
In particular the established
[lower-half-plane factorial expansion](research_lower_half_factorial_continuation.md)
applies to that numerator even when its real part passes
through one. This application uses a proved uniform
asymptotic on a lower-half-plane compact set, not merely
holomorphy of a finite interpolation.

For \(h_*\le0\), complete conditional asymptotics are
already supplied by the wall-gap completion theorem.
For \(0<h_*<\eta_0\), (29) permits a different retained
contour through the half-index cut. Its main-line bounds,
both Fourier remainders and every connecting segment
must still be assembled for the exact finite source.
The guard does not assert that assembly, an outer-cap
estimate, or a new knot-volume theorem.
