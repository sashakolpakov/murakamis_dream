# The conditional critical point on the displaced incoming rectangle

Research deduction, 7 November 2026. The original conditional
critical point continues throughout the negative-height rectangle
needed for a displaced incoming contour. It remains simple, stays
on the original logarithmic sheet, and has uniform bounds on its
exponential coordinate. This extends the real incoming continuation;
it does not continue the complete finite-source asymptotic.

No numerical evaluation is used. All primitive constants and the
incoming carrier are those of the original conditional sum.

## 1. The original equation

Retain
\[
\begin{split}
 Q(t;a,y)&=g(a+t)+g(y+t)-3g(t)-g(a)-g(y)+2\pi iat,\\
 X&=e^{-2\pi ia},\qquad Y=e^{-2\pi iy},\qquad v=e^{2\pi it}.
\end{split}
\tag{1}
\]
Here \(g'(z)=\Log(1-e^{-2\pi iz})\) on the original strip
\(0<\Re z<1\). The parameter set in this note is
\[
\begin{split}
 \mathcal A_-&=\{1/2\le\Re a\le7/10,\ -9/125\le\Im a\le0\},\\
 \mathcal Y&=\{11/50\le\Re y\le9/20,\ 0\le\Im y\le1/100\}.
\end{split}
\tag{2}
\]
The original exponential equation is
\[
 \exp Q_t=\frac{v(v-X)(v-Y)}{X(v-1)^3}=1,
\tag{3}
\]
or, equivalently,
\[
 (1-X)v^3+(2X-Y)v^2+X(Y-3)v+X=0.
\tag{4}
\]
The factor \(X^{-1}\) in (3) comes from the incoming
carrier in the finite sum and is retained.

The real incoming continuation in
[the original branch theorem](research_mixed_half_face_general_incoming_transport.md),
Section 3, supplies exactly one simple upper-half-plane root
at \(X=-1\), for every \(y\in\mathcal Y\). At that root the
original logarithmic equation is \(Q_t=0\).

For (2) one has
\[
 \Re X<0,\quad \Im X\ge0,\quad
       \frac13<|X|^2\le1,\qquad
 \Im Y<0,\quad \Re Y<1,\quad 1\le|Y|<\frac87.
\tag{5}
\]
The outgoing inequalities are those proved in the cited branch
theorem. For the new lower radius bound, put \(R=|X|^2\).
Then
\[
 R\ge e^{-36\pi/125}>e^{-1}>\frac13.
\tag{6}
\]
Indeed \(36\pi/125<1\), using \(\pi<22/7\), and
\(e<3\) follows directly from its factorial series.

## 2. Exactly one upper root throughout the rectangle

**Lemma 1.** Equation (4) has exactly one root in the upper
half-plane, counting multiplicity, for every pair in (2).
That root is simple and depends holomorphically on the parameters
on a neighborhood of this compact set.

*Proof.* Neither zero nor \(1\) nor \(X\) is a root,
as follows by substitution into the undivided equation
\[
                 v(v-X)(v-Y)=X(v-1)^3.
\tag{7}
\]
For a putative real root, solve (7) for \(Y\):
\[
       Y=v-\frac{X(v-1)^3}{v(v-X)}.
\tag{8}
\]
If \(\Im X>0\), this gives
\[
       \Im Y=-\frac{(v-1)^3\Im X}{|v-X|^2}.
\tag{9}
\]
For \(v<1\), (9) is positive, contrary to (5).
For \(v>1\),
\[
 \Re\frac{X}{v-X}
       =\frac{v\Re X-|X|^2}{|v-X|^2}<0,
\tag{10}
\]
so (8) gives \(\Re Y>v>1\), again impossible.
When \(X\) is negative real, (8) is real for real \(v\),
also contradicting \(\Im Y<0\).

Thus no root crosses the real axis. The leading coefficient
\(1-X\) is bounded away from zero on (2), so no root escapes
to infinity along a parameter path in this compact rectangle.
For fixed \(y\), first move from \(a=1/2\) vertically to the
desired height and then horizontally to the desired real part.
The upper root count therefore remains the count one at the
initial point. A multiple upper root would count at least twice,
so this root is simple. The analytic implicit-function theorem,
uniqueness of the upper root, and compactness give the stated
holomorphic continuation. \(\square\)

## 3. The incoming numerator wall is not crossed

The upper root alone does not establish the original phase
domain. We must also show that its logarithm satisfies
\(\Re(a+t)<1\).

**Lemma 2.** Choose \(\Log v\) with argument in \((0,\pi)\).
Then the continued root in Lemma 1 obeys
\[
           t=\frac{\Log v}{2\pi i},\qquad
                   0<\Re t<1-\Re a.
\tag{11}
\]

*Proof.* Write \(c=\Re X<0\) and \(R=|X|^2\).
A point on the forbidden ray has \(v=sX\), \(s>0\).
The case \(s=1\) has already been excluded.
Substitution into (8) gives exactly
\[
\begin{split}
 \Im Y
  &=\Im X\,
     \frac{s^3(1-2c)+2s^2-R^{-1}}{s(s-1)},\\
 \Re Y-1
  &=\frac{s^3(R+c-2c^2)+(2c-1)s^2-2s+c/R}{s(s-1)}.
\end{split}
\tag{12}
\]
If \(s>1\) and \(\Im X>0\), the numerator in the first
line is greater than \(3-R^{-1}>0\). It would give
\(\Im Y>0\). If \(0<s<1\), the numerator in the second
line is bounded above by
\[
                     s^3-s^2-2s<0,
\tag{13}
\]
because \(R\le1\) and \(c<0\). Its denominator is negative,
so it would give \(\Re Y>1\). Both conclusions contradict (5).
If \(X\) is negative real, its positive ray is the negative
real axis and cannot contain the upper root.

At \(\Re a=1/2\) the argument of \(X\) is \(\pi\), strictly
larger than the argument of the upper root. Continuity and the
ray exclusion preserve
\(\arg v<\arg X=2\pi(1-\Re a)\), proving (11).
\(\square\)

In particular \(t,a+t,y+t,a,y\) all have real parts in
their original strips; for the outgoing numerator,
\(\Re(y+t)<19/20\). All primitive logarithms therefore
continue without a divisor. Equation (3) says that \(Q_t\)
is an integral multiple of \(2\pi i\); continuity from its
original value zero shows that
\[
                             Q_t=0
\tag{14}
\]
on the entire parameter rectangle. This proves continuation
of the original phase, not merely of an algebraic root of (4).

## 4. Explicit radius bounds on the same sheet

**Lemma 3.** The selected root satisfies
\[
                         \frac25<|v|<2.
\tag{15}
\]

*Upper bound.* If \(|v|\ge2\), the original logarithmic
derivative can be written
\[
 Q_t=\Log(1-X/v)+\Log(1-Y/v)-3\Log(1-1/v)+2\pi ia.
\tag{16}
\]
All logarithms here have their principal values, by the strip
conditions just proved. For \(|z|\le r<1\),
\(|\Arg(1-z)|\le\arcsin r\). The three radii in (16)
are bounded by \(1/2,4/7,1/2\). Hence
\[
 \Im Q_t
 \ge 2\pi\Re a-4\arcsin(1/2)-\arcsin(4/7)
 >\pi-\frac{2\pi}{3}-\frac\pi5>0.
\tag{17}
\]
The elementary bound \(\arcsin(4/7)<\pi/5\) is proved
in the [real incoming decrease theorem](research_mixed_half_face_global_phase_decrease.md),
Lemma 1. This contradicts (14).

*Lower bound.* Suppose \(v=\rho e^{i\phi}\),
\(0<\rho\le2/5\). On the same original strips, factor
the three logarithms in (16) to obtain
\[
 Q_t=\Log v+\Log Y-i\pi
      +\Log(1-v/X)+\Log(1-v/Y)-3\Log(1-v).
\tag{18}
\]
Here \(\arg Y=-2\pi\Re y\in[-9\pi/10,-11\pi/25]\)
and \(0<\phi<\arg X\). The factorizations have no hidden
integer lift: one may decrease \(\rho\) to zero at fixed
angles, keeping all the arguments in their same strips.
The leading argument contributions are respectively
\(\arg X-\phi-\pi\), \(\arg Y-\phi+\pi\), and
\(\pi-\phi\); also \(2\pi ia=-\Log X+2\pi i\).
Their sum is precisely the constant \(-i\pi\) in (18).

The core argument
\[
 B_\rho(\phi)=
     \phi+3\Arg(1-\rho e^{-i\phi})
\tag{19}
\]
increases to \(\pi\) on \(0\le\phi\le\pi\), since
\[
 B_\rho'(\phi)=
 \frac{1+\rho\cos\phi-2\rho^2}
      {1-2\rho\cos\phi+\rho^2}>0
                  \qquad(0<\rho\le2/5).
\tag{20}
\]
Moreover \(|v/X|<2\sqrt3/5<1/\sqrt2\) and
\(|v/Y|\le2/5<1/2\).
Consequently the two remaining argument contributions in
(18) have sum at most
\[
 \arcsin(2\sqrt3/5)+\arcsin(2/5)
                  <\frac\pi4+\frac\pi6=\frac{5\pi}{12}.
\tag{21}
\]
The first radius comparison is \(12/25<1/2\);
the second is immediate.
Taking imaginary parts in (18) now gives
\[
              \Im Q_t<
                  -\frac{11\pi}{25}+\frac{5\pi}{12}<0,
\tag{22}
\]
again contradicting (14). This proves (15).
\(\square\)

## 5. The critical point stays above the original lower index cut

**Lemma 4.** Throughout (2),
\[
                              \Re t>\frac1{16}.
\tag{23}
\]

*Proof.* Suppose \(0<u=\Re t\le1/16\), and put
\[
 R_t=e^{2\pi\Im t}=|v|^{-1}\in(1/2,5/2),\qquad
 T=e^{-2\pi\Im a}\ge1,\qquad R_y=e^{2\pi\Im y}\ge1.
\]
The exact force, including the incoming carrier, is
\[
 |\exp Q_t|^2=
 \frac{|T-R_t e^{-2\pi i(\Re a+u)}|^2
       |1-R_yR_t e^{-2\pi i(\Re y+u)}|^2}
      {|1-R_t e^{-2\pi iu}|^6}.
\tag{24}
\]
On the assumed range,
\[
\begin{split}
 &\cos(2\pi u)>9/10,\\
 &\cos(2\pi(\Re a+u))<1/10,\\
 &\cos(2\pi(\Re y+u))<1/5.
\end{split}
\tag{25}
\]
For the first inequality use \(2\pi u\le\pi/8<2/5\)
and \(\cos s\ge1-s^2/2\).
For the second, \(\Re a+u\in[1/2,61/80]\), whose
maximum cosine is \(\sin(\pi/40)<1/10\).
For the third, \(\Re y+u\in[11/50,41/80]\);
its maximum cosine is \(\sin(3\pi/50)<1/5\).

The first numerator square increases as a function of \(T\ge1\),
since \(T-R_t\cos(2\pi(\Re a+u))>1-(5/2)/10>0\).
The second increases as a function of \(R_y\ge1\), since
\(R_yR_t-\cos(2\pi(\Re y+u))>1/2-1/5>0\).
Writing
\[
                         D=1+R_t^2-\frac95R_t>0,
\]
(25) therefore bounds the numerator squares below by
\(D+8R_t/5\) and \(D+7R_t/5\), respectively, and bounds
the denominator before cubing above by \(D\).
On \(1/2\le R_t\le5/2\), convexity gives
\[
 D\le\frac{11}{4},\qquad
 \frac{D}{R_t}=R_t+R_t^{-1}-\frac95\le\frac{11}{10}.
\tag{26}
\]
The endpoint comparisons suffice for both convex functions.
It follows that
\[
 |\exp Q_t|^2
 \ge\frac{(1+8R_t/(5D))(1+7R_t/(5D))}{D}
 \ge\frac{(1+16/11)(1+14/11)}{11/4}
 =\frac{2700}{1331}>1.
\tag{27}
\]
This contradicts (3). \(\square\)

The critical point consequently lies above the original lower
cut \(1/16\) by a uniform positive margin. Compactness and
Lemma 2 also give a uniform margin below its incoming wall.
One may choose a fixed positive upper-cut collar small enough
to retain the critical point throughout (2).

There is a corresponding horizontal curvature statement.
Write \(C(z)=\Re\cot(\pi z)\). The all-height inequality
in Lemma 2 of
[the complete real-arc conditional theorem](research_mixed_real_arc_complete_conditional_packet.md)
gives \(3C(t)-C(t+y)>0\) whenever
\(3/50\le\Re t<1/2\), for the same outgoing rectangle.
It is independent of the incoming height. On the present
critical chart \(\Re(a+t)>1/2\), so \(C(a+t)<0\).
Therefore
\[
 -\Re Q_{tt}
 =\pi\{3C(t)-C(t+y)-C(a+t)\}>0.
\tag{28}
\]
This holds on the entire regular horizontal index interval
from \(1/16\) to a fixed collar below \(1-\Re a\), at every
bounded index height. In particular the selected saddle has
a strictly decaying horizontal Gaussian direction.

## 6. Consequence for the proposed contour and remaining work

The actual incoming height in the selected first-three source
satisfies \(-9/125<\Im a_*<0\). Thus the entire proposed
horizontal displacement from \(1/2+i\Im a_*\) to
\(7/10+i\Im a_*\) lies in (2), as does the far vertical
segment up to \(7/10\). On both pieces the same conditional
critical point and its original logarithmic phase are available.
There is no branch collision or incoming numerator wall on
this critical branch.

The strict inequalities and compactness give uniform positive
strip margins and a fixed complex neighborhood for this phase.
Lemma 3 also bounds its imaginary critical coordinate.
These conclusions can be used when choosing an internal
conditional contour.

The literal conditional sum still includes every original
index, including indices beyond the selected critical chart.
No estimate for those rows, the finite residue remainders,
or the intervening cap has been inferred here. A simple
critical point does not by itself prove that it contributes
to that finite sum. The complete displaced-contour estimate
and the finite-exception filling theorem remain open.
