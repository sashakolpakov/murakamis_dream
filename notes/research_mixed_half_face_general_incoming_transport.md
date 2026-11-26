# Algebraic incoming transport of the original half-face branches

Research deduction, 7 November 2026. The exact incoming multiplier
of the cap--conditional critical action has a rational factorization.
The original critical branches, including their logarithmic lifts,
continue along the real incoming arc \(1/2\le a\le7/10\).
Their regular phase arguments do not cross a wall.

This is a continuation of the original critical phases. It is not a
continuation of the complete finite-source asymptotics along that
whole arc. In particular an explicit point on the continued branch
lies outside the proved endpoint-coefficient rectangle. The incoming
derivative is strictly negative at that point and near the half face;
its sign on the interval between these neighborhoods remains unproved.
No numerical evaluation or certificate replay is used.

## 1. Original phases and their exponentiated equations

At complete ordinary color, retain exactly
\[
 \begin{split}
 F(e,u)&=-2J(1/2-u)-3J(u)-J(e-u)+i\pi eu,\\
 S(e)&=F(e,u_c(e)),\\
 \Psi(e,a)&=S(e)+J(e+a)-J(a)-i\pi ea,\\
 Q(t;a,y)&=g(a+t)+g(y+t)-3g(t)-g(a)-g(y)+2\pi iat .
 \end{split}                                                       \tag{1}
\]
All primitive constants and original logarithmic lifts are those of
[the whole cap](research_mixed_half_face_complete_cap_packet.md) and
[the whole conditional factor](research_mixed_half_face_complete_conditional_packet.md).
The corresponding local complete product and its phase
\(\mathcal P=\mathcal T+\Theta\) are proved in
[the joint-source theorem](research_mixed_half_face_joint_source_packet.md).
The algebra below is at ordinary color \(-2\); the letter \(\omega\)
is an auxiliary exponential, not an ordinary color.

Set
\[
 X=e^{-2\pi ia},\quad Y=e^{-2\pi iy},\quad
 \omega=e^{2\pi iu_c(e)},\quad p=e^{2\pi ie},\quad
                         v=e^{2\pi it}.                           \tag{2}
\]
On the original endpoint branch,
\[
 p=\frac{5\omega^2-2\omega+1}{(\omega+1)^2},\qquad
       e^{\Psi_e}=\frac{\omega(p-X)}{p-\omega}.                   \tag{3}
\]
Thus cap criticality gives
\[
 \begin{split}
 p&=\frac{\omega(1-X)}{1-\omega},\\
 f_X(\omega)&:=(6-X)\omega^3-(5+2X)\omega^2
                                      +(4-X)\omega-1=0 .
 \end{split}                                                       \tag{4}
\]
For the conditional equation, the original chirp contributes \(X^{-1}\):
\[
 e^{Q_t}
   =X^{-1}\frac{(1-X/v)(1-Y/v)}{(1-1/v)^3}
   =\frac{v(v-X)(v-Y)}{X(v-1)^3}.
                                                                    \tag{5}
\]
Consequently its critical polynomial is
\[
             (1-X)v^3+(2X-Y)v^2+X(Y-3)v+X=0.                    \tag{6}
\]
The factorizations are asserted on the original branches with
their divisors retained. They do not assign a logarithmic lift
to an arbitrary algebraic root.

Stationarity removes \(e_a,t_a\) from the incoming derivative.
The cap and conditional multipliers are respectively
\[
 \begin{split}
 e^{\mathcal T_a}
   &=\frac{1-X/p}{1-X}
     =\frac{\omega-X}{\omega(1-X)^2},\\
 e^{\Theta_a}
   &=\frac{1-X/v}{1-X}\,v
     =\frac{v-X}{1-X}.
 \end{split}                                                       \tag{7}
\]
In particular the exact combined multiplier is
\[
 \boxed{\quad
       e^{\mathcal P_a}
          =\frac{(\omega-X)(v-X)}
                         {\omega(1-X)^3}.
 \quad}                                                          \tag{8}
\]
Both chirps in (1) are included. On any continued original phase
sheet, taking moduli gives the exact test
\[
 \Re\mathcal P_a<0
 \quad\Longleftrightarrow\quad
 |(\omega-X)(v-X)|<|\omega|\,|1-X|^3.                              \tag{9}
\]

There is a second useful exact parameterization. Put
\[
                         k=\frac{1-\omega}{1+\omega}.
\]
Equations (3)--(4) give
\[
 \begin{gathered}
 p=1-2k+2k^2,\qquad
 X=4k^2+3-\frac2{1-k},\\
 p-X=\frac{2k^3}{1-k},\qquad
 1-X=\frac{2kp}{1-k},\qquad
                   \boxed{\ e^{\mathcal T_a}=(k/p)^2\ } .
 \end{gathered}                                                     \tag{10}
\]
For example, writing \(B=k/p\) and \(q=1-X\), elimination gives
\[
 B^2(B-1)q^2+(2B^2-3B-1)q+2B=0.                                \tag{11}
\]
Indeed
\(2Bk^2-(2B+1)k+B=0\) and \(2k^2=Bq(1-k)\);
hence
\(k(B^2q+2B+1)=B(Bq+1)\), and substitution gives (11).
On the unit arc below, all the displayed original divisors
are nonzero. The intermediate denominator \(B^2q+2B+1\)
cannot vanish there either: its vanishing with
\(B(Bq+1)=0\) would force \(B=-1,q=1,X=0\).
Equation (11) alone does not choose the actual root \(B\).

## 2. The cap branch on the left upper unit arc

In this section
\[
 a\in[1/2,7/10],\qquad X=e^{-2\pi ia},\qquad
 \mathcal Y=\{11/50\le\Re y\le9/20,\quad0\le\Im y\le1/100\}.
                                                                    \tag{12}
\]
For \(a>1/2\), \(X\) is in the upper half-plane with negative
real part. At \(a=1/2\), choose precisely the cap root
\(\omega_+\) from the whole half-cap theorem.

The discriminant of (4) is
\[
                  64(X^3-17X^2+19X-7).                          \tag{13}
\]
On the nonreal arc, writing \(c=\Re X<0\), its cubic factor
has imaginary part
\[
                    2\Im X\,(2c^2-17c+9)>0.
\]
At \(X=-1\) the discriminant is \(-2816\). Thus no cap
root coalesces on this arc; \(6-X\ne0\) also prevents a root
from escaping to infinity. The selected root has a unique
analytic continuation along the arc.

A real root \(\omega\) would make \(X\) real in the rational
formula
\[
 X=\frac{6\omega^3-5\omega^2+4\omega-1}
                              {\omega(\omega+1)^2}.
                                                                    \tag{14}
\]
Neither \(\omega=0\) nor \(\omega=-1\) is a root of (4).
Therefore the selected \(\omega\) remains in the upper
half-plane for \(a>1/2\).

Its value \(p\) in (3) remains in the upper half-plane as well.
To verify this without assuming it, suppose \(p\) is real.
For \(p\ge1/2\), the endpoint quadratic
\[
              (p-5)\omega^2+2(p+1)\omega+(p-1)=0
                                                                    \tag{15}
\]
has real roots, including its linear degeneracy at \(p=5\).
This contradicts \(\Im\omega>0\).
For \(p<1/2\), its nonreal conjugate roots satisfy
\[
 |\omega|^2=\frac{1-p}{5-p},\qquad
                  \Re\omega=\frac{p+1}{5-p}.
\]
Criticality gives \(X=1+p-p/\omega\), whence
\[
                         |X|^2=1-\frac{4p^3}{1-p}.               \tag{16}
\]
On \(|X|=1\) this forces \(p=0\), which would give \(X=1\).
This is not on (12). There is therefore no real \(p\), and
continuity from the known half-face value proves \(\Im p>0\).

For later identification, the selected root is the unique root
of (4) with both \(\Im\omega>0\) and \(\Im p>0\).
At \(X=-1\), the other nonreal root has \(p\) in the lower
half-plane. The real root \(\alpha\) has \(p>1/2\).
When \(X\) moves into the upper arc,
\[
 \omega_X(\alpha)=\frac{\alpha(\alpha+1)^2}{f_{-1}'(\alpha)}>0,
 \qquad
 \frac{dp}{d\omega}(\alpha)=
                 \frac{4(3\alpha-1)}{(\alpha+1)^3}<0.
\]
Thus that root initially has \(\Im\omega>0,\Im p<0\).
No root can cross the real \(\omega\)-axis on the nonreal
arc; (16) prevents a nonreal root's \(p\) from crossing
the real axis. The asserted characterization follows.

Two further wall exclusions are necessary for the original
primitives, not just for the algebraic root.

First, \(p\) cannot lie on the positive ray through \(X\).
If \(p=sX\), \(s>0\), (4) gives
\(\omega=sX/[1+(s-1)X]\). Substitution in (15) yields
\[
 s(2s-1)^2X^3-(2s+1)X^2+(s+2)X-1=0.
                                                                    \tag{17}
\]
After division by \(X\), its imaginary part is
\(2s\Im X\{c(2s-1)^2-1\}\), which is strictly negative.
Thus (17) is impossible. At the half face \(\arg p<\arg X\);
this inequality persists along the arc. With the logarithms
whose arguments are in \((0,\pi)\), it gives
\[
                             0<\Re e<1-a.                       \tag{18}
\]

Second, \(p/\omega\) cannot be positive real.
If \(p=s\omega\), \(s>0\), criticality gives
\(\omega=(X+s-1)/s\). Substituting this in (15) gives
\[
 \begin{split}
 X^3+(5s-8)X^2+(8s^2-18s+13)X
                         +4s^3-12s^2+13s-6=0.
 \end{split}                                                       \tag{19}
\]
The imaginary part after division by \(X\) forces
\[
                         c=1+2s(s-1)(s-2)>0.                   \tag{20}
\]
For \(0<s\le1\) or \(s\ge2\) the last inequality is immediate.
For \(1<s<2\), put \(z=s-1\in(0,1)\); then
\(z^3-z\ge-2/(3\sqrt3)\), so the right side is at least
\(1-4/(3\sqrt3)>0\).
Equation (20) contradicts \(c<0\). Since at the half face
\(\arg p>\arg\omega\), this inequality persists. Thus
\[
                     0<\Re u_c<\Re e<1/2.                       \tag{21}
\]

The endpoint quadratic has exactly one upper-half-plane root
for every upper-half-plane \(p\), as proved with the original
branch in the half-face cap theorem. Consequently this
continued \(\omega\) is still that original endpoint branch.
Equations (18)--(21) place all arguments
\(u_c,1/2-u_c,e-u_c,e+a,a\) in their original regular strips.
None crosses a primitive divisor. The exponentiated stationary
equations therefore retain their original zero logarithmic
lifts by continuous continuation from \(a=1/2\).
This proves continuation of the actual critical phase
\(\mathcal T(a,-2)\), with its original absolute constant.

## 3. The conditional branch and its no-wall guards

For \(y\in\mathcal Y\),
\[
          \Im Y<0,\qquad \Re Y<1,\qquad |Y|<8/7.                 \tag{22}
\]
The last bound is in the complete conditional theorem.
For the middle one, if \(\Re Y>0\), then
\(\Re Y\le e^{\pi/50}\cos(11\pi/25)
 <(8/7)\sin(3\pi/50)<1\).
At \(X=-1\), the original conditional theorem proves exactly
one upper-half-plane root \(v\), counting multiplicity.

For fixed \(Y\) satisfying (22), this root count cannot
change as \(X\) moves on the nonreal arc.
Indeed \(v=0,1,X\) are excluded by (6) and \(Y\ne1\).
Solving (5) for \(Y\) gives
\[
                  Y=v-\frac{X(v-1)^3}{v(v-X)}.                 \tag{23}
\]
For real \(v\ne0,1\),
\[
             \Im Y=-\frac{(v-1)^3\Im X}{|v-X|^2}.               \tag{24}
\]
If \(v<1\), this has the wrong sign. If \(v>1\), then
\[
          \Re\frac{X}{v-X}
                       =\frac{v\Re X-1}{|v-X|^2}<0,
\]
so (23) gives \(\Re Y>v>1\), again impossible.
No root can escape to infinity because \(1-X\ne0\).
There remains exactly one upper root, with multiplicity one.
It defines the continued simple branch \(v(a,y)\).

The additional incoming wall also cannot be crossed.
If \(v=sX\), \(s>0\), formula (23) gives
\[
 \begin{split}
 \Im Y&=\Im X\,
       \frac{s^3(1-2c)+2s^2-1}{s(s-1)},\\
 \Re Y-1&=
       \frac{s^3(1+c-2c^2)+(2c-1)s^2-2s+c}{s(s-1)} .
 \end{split}                                                       \tag{25}
\]
Here \(s=1\) is already excluded.
For \(s>1\) the first line is positive.
For \(0<s<1\), the second numerator is bounded above by
\(s^3-s^2-2s<0\), so its quotient is positive.
Both cases contradict (22).
Since at \(X=-1\) one has \(\arg v<\arg X\), it follows that
\[
                      0<\Re t<1-a.                             \tag{26}
\]
Thus \(t,a+t,y+t,a,y\) all remain in their original regular
factorial/primitive strips; in particular \(\Re(y+t)<.95\).
The logarithmic lift of \(Q_t\) stays zero by continuation.
The actual phase \(\Theta(a,y)\), with its original constant,
therefore continues throughout (12).

There is also a useful uniform root bound.
On \(|v|=3\), the leading term of (6) has modulus greater than
\[
                  (8/5)3^3=216/5,
\]
because \(|1-X|=2\sin(\pi a)>8/5\) on (12).
The sum of the other terms is less than
\[
                  (22/7)3^2+(29/7)3+1=292/7<216/5.
\]
Rouché's theorem therefore puts every root of (6) in
\[
                                  |v|<3.                        \tag{27}
\]
Compactness and the absence of the listed divisors give fixed
positive strip margins and bounded heights for the selected
roots over (12). The simple roots and their original phases
extend holomorphically to a fixed complex neighborhood of this
compact parameter set. This assertion is about the critical
equations and phases, not about complete finite-source dominance.

## 4. An exact later point and the source-domain limitation

Consider the exact values
\[
 \begin{gathered}
 k_0=-i/\sqrt2,\qquad
 \omega_0=\frac{1+2\sqrt2\,i}{3},\qquad
 p_0=i\sqrt2,\\
 X_0=-\frac13+\frac{2\sqrt2}{3}i,\qquad
                    a_0=1-\frac{\arg X_0}{2\pi}.
 \end{gathered}                                                     \tag{28}
\]
They satisfy (10), and \(1/2<a_0<7/10\).
For the upper bound on \(a_0\), use
\(\cos(3\pi/5)=(1-\sqrt5)/4>-1/3\).
The root has both \(\Im\omega_0>0\) and \(\Im p_0>0\);
the uniqueness characterization in Section 2 identifies it
with the continued original cap branch.

Its cap multiplier is exactly \(1/4\). Equations (7) and (27)
therefore give, uniformly for all selected \(y\),
\[
 |e^{\mathcal P_a(a_0,-2,y)}|
       <\frac1{|1-X_0|}
        =\sqrt{\frac38}<\frac58,\qquad
              \Re\mathcal P_a(a_0,-2,y)<-\frac6{13}.             \tag{29}
\]
Here \(|v-X_0|<4\), and
\(\log(8/5)>2[(8/5)-1]/[(8/5)+1]=6/13\).
Strictness and compactness give a fixed neighborhood of \(a_0\)
on which the continued phase has negative real incoming
derivative. This is a genuine second region of phase decrease,
separated from the already proved half-face neighborhood.

The point (28) also gives an exact warning about finite-source
scope:
\[
                 e(a_0)=\frac14-\frac{i\log2}{4\pi}.             \tag{30}
\]
Its real part is below \(.27\). Its depth also exceeds \(.055\):
\[
 \log2>
 2\left(\frac13+\frac1{81}+\frac1{1215}\right)
 =\frac{842}{1215}>\frac{121}{175}>\frac{11\pi}{50}.
                                                                    \tag{31}
\]
The middle cross-product difference is \(335>0\).
Thus the root has left the proved endpoint rectangle in both
coordinates. Its auxiliary point has zero height, since
\(|\omega_0|=1\). Algebraic regularity does not license retaining
the old rectangle's finite tails and aliases at this point.

Near \(a=1/2\), (8) reduces exactly to the multiplier in
[the incoming finite-source theorem](research_mixed_half_face_incoming_transport.md).
That theorem already proves the local whole-product decrease
and short-integral expansion, with ordinary-color continuation.
No duplicate whole-source conclusion is inferred here.
At \(a_0\), (29) concerns the continued original critical phase
only; a complete source expansion there still needs all its
actual rows and currents paid.

The remaining two questions are distinct. Inequality (9) has
not been proved on every point between the two negative-
derivative neighborhoods. Even if it were, the complete
finite-source expansions would still need continuation across
the changing endpoint and conditional source domains.
Neither question is settled by the cubics, by the square
identity (10), or by the absence of a critical divisor.

