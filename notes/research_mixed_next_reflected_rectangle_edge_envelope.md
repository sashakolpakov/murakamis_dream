# The original shortened edge on the reflected outgoing rectangle

Private finite-source theorem, 9 November 2026. The original shortened
second edge has a complete upper envelope on the three first-angle
families needed by the reflected right-hand inner contour. The outgoing
rectangle is independent; in particular its upper height need not be
smaller than half its real angle. The original two physical endpoint
groups, both midpoint caps, and both complete Fourier corrections are
retained.

This is written analysis only. No mathematical numerical evaluation,
saved-value arithmetic, or frozen-source edit is used.

## 1. Family, normalization, and precise conclusion

Put
\[
 \mathcal R^\uparrow=\{\beta+iK:0\le\beta\le4/3,\ 0\le K\le2/5\},
 \qquad h_0=1/10,\qquad a_1=\arccos(-3/5).
 \tag{1}
\]
For \(u\in\mathcal R^\uparrow\), use the following three compact
families for \(t=a-iH\):
\[
\begin{array}{ll}
 \mathcal H:&\pi/2\le a\le2\pi/3,\quad2/3\le H\le1,\\
 \mathcal V:&a=2\pi/3,\quad1/10\le H\le1,\\
 \mathcal L:&2\pi/3\le a\le a_1,\quad H=1/10.
\end{array}
 \tag{2}
\]
No assertion is made on the larger, unnecessary rectangle
\(\pi/2\le a\le2\pi/3,\ 1/10\le H\le1\).

Retain the original ordinary Newton polynomials and exact parity cutoff:
\[
 U_N=\lfloor N/2\rfloor-1,\qquad
 K_N^<(t,u)=\sum_{j=0}^{U_N}e_j(-2\cos t)e_j(-2\cos u).
 \tag{3}
\]
The phase \(\psi(t,u)\) below is the original closed edge primitive.
It is calibrated by the original mixed-height packet and continued
along the families (2); no logarithmic charge or additive constant
is reassigned.

**Theorem.** For every fixed \(\tau>0\), uniformly on (1)--(2), at both
parities and all sufficiently large \(N\),
\[
 |K_N^<(t,u)|\le C_\tau
 \exp N\left\{\max\!\left(\Re\psi(t,u),\frac{H+K}{2}\right)+\tau\right\}.
 \tag{4}
\]
This is a finite upper estimate for (3), not a Gaussian asymptotic.
It does not by itself extend the full inner trace or its one-remaining-
current representation to upper outgoing angles.

## 2. Original force and elementary rectangle guards

Use the original reciprocal-factorial interpolation and sidewise
upper exponent:
\[
\begin{split}
 B_N(y,z)&=\frac{N}{
 G_N(N(1/2-y+z/(2\pi))-1/2)
 G_N(N(1/2-y-z/(2\pi))-1/2)G_N(Ny)^2},\\
 T_N(y;t,u)&=B_N(y,t)B_N(y,u),\\
 \mathcal F(y)&=\mathfrak b(y,t)+\mathfrak b(y,u).
\end{split}
 \tag{5}
\]
Its horizontal derivative is \(\partial_x\mathcal F=\log|e^{F_y}|\),
with the unchanged force
\[
 e^{F_y}=
 \frac{(\cos2\pi y+\cos t)(\cos2\pi y+\cos u)}
 {(1-\cos2\pi y)^2},\qquad F=b(y,t)+b(y,u).
 \tag{6}
\]
The incoming zero cut starts at
\(1/2-a/(2\pi)+iH/(2\pi)\); the outgoing cut starts at
\(1/2-\beta/(2\pi)-iK/(2\pi)\). They run horizontally to the
right. For \(K=0,\beta>0\) the outgoing cut is on the real bottom.
For \(\beta=0\) its open interior part is empty.

Write
\[
 \cos u=P-iQ,\quad
 \mu=13/12,\quad \epsilon=\mu^2-1=25/144.
 \tag{7}
\]
The original elementary sine-series guards imply
\[
 P>7/30,\quad 0\le Q<5/12,\quad
 |\cos u|<\mu,\quad \cosh K<13/12,\quad \sinh K<5/12.
 \tag{8}
\]
Here \(\cos(4/3)>7/30\), and the latter hyperbolic inequalities
follow from their positive series with geometric tail bounds.
On the part \(K\le\beta/2\), one also has \(|\cos u|\le1\).
Indeed \(\sinh K\le\sinh(\beta/2)<\sin\beta\) for
\(0<\beta\le4/3\): use \(\sin\beta/\beta\ge19/27\) and
\(\sinh(\beta/2)/\beta\le19/30\).
At \(\beta=0\) this is the limiting equality.
On the complementary part \(K\ge\beta/2\),
\[
 \beta\le4/5,\qquad P\ge17/25>2/3,\qquad Q<1/3.
 \tag{9}
\]

Put \(A=\cos^2(t/2)\), \(B=\cos^2(u/2)\), \(D_0=A+B-AB\),
and \(W=AB/D_0\). With
\[
 b=\Re B,\qquad B_2=|B|^2,\qquad e=25/576,
\]
the whole outgoing rectangle satisfies
\[
 \frac35<b\le\frac{25}{24},\qquad
 b^2\le B_2\le b+e<\frac{10}{9},\qquad
 |1-B|<\frac{17}{40},\qquad \Re(1/B)>\frac{24}{25}.
 \tag{10}
\]
The nontrivial upper bound is the exact identity
\[
 B_2-b=\frac{\sinh^2K-\sin^2\beta}{4}\le\frac{25}{576}.
 \tag{11}
\]
The reciprocal bound follows directly from
\[
 \Re(1/B)=\frac{2(1+\cos\beta\cosh K)}
 {(\cosh K+\cos\beta)^2};
\]
its derivative in \(\cos\beta\) is negative on the stated box,
so its minimum is at \(\cos\beta=1\).
All these guards are unchanged by the sign of \(K\).

## 3. Both cuts, with the adverse imaginary cross term retained

On the incoming upper cut set
\[
 C=\cosh H,\quad S=\sinh H,\quad d=\cos a,\quad
 q=-\cos(2\pi\Re y),\quad s_q=\sqrt{1-q^2}.
 \tag{12}
\]
Then \(\cos2\pi y=-Cq-iSs_q\) and the denominator modulus
in (6) is \((C+q)^2\). Unlike the lower outgoing family,
the second squared numerator has the adverse term
\(+2Ss_qQ\). This term is retained throughout.

First treat \(\mathcal H\cup\mathcal V\), where
\(d\in[-1/2,0]\), \(1\le C<8/5\), and \(q\in[d,1]\).
The original exact incoming calculation gives
\[
 O:=|\cos2\pi y+\cos t|^2
 \le
 \begin{cases}
 (q+1/2)^2(4C^2-1)/3,&q\le0,\\
 q^2+A_Cq+B_C,&q\ge0,
 \end{cases}
 \quad
 A_C=\frac{8C^2-5}{3},\quad B_C=\frac{4C^2-1}{12}.
 \tag{13}
\]
This comparison is obtained by increasing the first angle to
\(2\pi/3\); its derivative and the negative-\(q\) factorization
are those of the original cut proof.

For \(q=-v\le0\), triangle inequality gives
\[
 |\cos2\pi y+\cos u|
 \le\mu(|\cos2\pi y|+1)\le\sqrt2\,\mu(C+v).
 \tag{14}
\]
The second inequality follows by squaring
\((R+1)^2\le2(R^2+1)\), with \(R^2=C^2-1+v^2\).
The same perfect-square maximization as in the original cut proof,
\((1-5v)^2\ge0\), now gives
\[
 |e^{F_y}|^2\le\frac{27}{32}\mu^2
                =\frac{4563}{4608}<1.
 \tag{15}
\]

For \(q\ge0\), first suppose \(K\le\beta/2\).
Using \(|\cos u|\le1\), (8), and \(S<C\), the second
squared numerator is at most
\[
 q^2-\frac7{15}Cq+C^2+\frac56C.
 \tag{16}
\]
In the difference between \((C+q)^4\) and the product of
(16) with \(q^2+A_Cq+B_C\), the cubic coefficient is positive,
the quadratic coefficient is at least \(23C^2/6\), the linear
coefficient is at least \(-157C^2/75\), and the constant is
at least \(7C^2/18\). These follow from
\[
 4C-A_C\ge31/25,\qquad A_C<(8/3)C^2,\qquad B_C<C^2/3.
 \tag{17}
\]
For the linear coefficient also use \(A_C/C\le129/40<4\), since
\((8C-5/C)/3\) increases on \(1\le C\le8/5\);
then \(31/25-(5/6)\,4=-157/75\).
For the quadratic coefficient use
\((14/3)C^2-(5/6)C\ge(23/6)C^2\).
For the constant use
\((2/3)C^4-(5/18)C^3\ge(7/18)C^4\).
The remaining quadratic is strictly greater than \(C^2/10\),
because
\[
 \frac7{18}-\frac1{10}
 -\frac{(157/75)^2}{4(23/6)}
 =\frac{803}{258750}>0.
 \tag{18}
\]
Since \((C+q)^4\le16C^4\le(1024/25)C^2\), this proves
\[
                   |e^{F_y}|^2\le1-\frac5{2048}.
 \tag{19}
\]

On the complementary part (9), the second numerator is at most
\[
 q^2-\frac43Cq+C^2+E_C,\qquad E_C=\frac{25}{144}+\frac23C.
 \tag{20}
\]
The cubic and quadratic coefficients of the denominator deficit
are positive. Write its constant and linear coefficients as
\[
 C_0=C^2(C^2-B_C)-E_CB_C,\qquad
 L_0=C^2(4C-A_C)+\frac43CB_C-E_CA_C.
 \tag{21}
\]
Then
\[
 C_0\ge\frac{167}{432}C^2,
\]
and direct expansion gives
\[
 C_0+L_0=
 -2C^4+\frac{22}{9}C^3+\frac{59}{48}C^2
                  +\frac{19}{18}C+\frac{175}{576}.
 \tag{22}
\]
On \(1\le C\le8/5\),
\[
 -2C^4+\frac{22}{9}C^3\ge-\frac{272}{225}C^2,
\]
so (22) exceeds
\[
 \frac{73}{3600}C^2+\frac{19}{18}C+\frac{175}{576}
                  >\frac{167}{432}C^2.
 \tag{23}
\]
For the last comparison one can use
\((19/18)C\ge(95/144)C^2\).
If \(L_0<0\), then \(L_0q\ge L_0\); otherwise it is nonnegative.
Thus the full deficit is at least \(167C^2/432\), and
\[
 |e^{F_y}|^2\le1-\frac{4175}{442368}<1.
 \tag{24}
\]
Equations (15),(19),(24) cover the entire reflected rectangle.

On \(\mathcal L\), put \(d_1=-\cos a\in[1/2,3/5]\).
The exact chord factorization gives
\[
 |\cos2\pi y+\cos t|\le\frac{51}{50}(q+d_1).
 \tag{25}
\]
Indeed the quotient of the two sine differences is at most
\(d_1/\sqrt{1-d_1^2}\le3/4\), and
\(\sqrt{C^2+9S^2/16}<51/50\) at \(H=1/10\).
Here \(S<101/1000\), so the adverse cross term satisfies
\[
                         2SQ<101/1200<1/10.
 \tag{26}
\]
For \(q\ge0\) the other numerator squared is at most
\((\mu^2+1/10)(C+q)^2\). For \(q=-v\le0\) it is at most
\((\mu^2+1/10)(C+v)^2\). To see the latter comparison,
first remove the adverse term and use
\[
 C^2-1+v^2+\mu^2+2Cv\mu\le\mu^2(C+v)^2.
 \tag{27}
\]
The case \(q\ge0\) follows by discarding the favorable real
cross term. The added \(1/10\) is absorbed since the respective
comparison factors \(C+v\) and \(C+q\) are at least one.
Consequently both cut portions obey
\[
 |e^{F_y}|\le\frac{102}{125}\sqrt{\mu^2+\frac1{10}}<1.
 \tag{28}
\]
For \(q\ge0\), use \((q+d_1)/(C+q)\le4/5\).
For \(q=-v\), use
\[
 \frac{(d_1-v)(C+v)}{(C-v)^2}
 \le\frac{(3/5-v)(1+v)}{(1-v)^2}\le\frac45;
 \tag{29}
\]
the last denominator difference is \((1-3v)^2/5\).
The first fraction decreases with \(C\).

The outgoing cut is lower. Its own real angle is less than
\(\pi/2\), so the original sign-independent own-leg inequality
and the triangle bound \(|\cos t|<8/5\) give, on all three families,
\[
                         |e^{F_y}|\le\frac{13\sqrt{79}}{150}<1.
 \tag{30}
\]
This includes the real outgoing cut and its starting zero at
\(K=0\). No upper-cut argument is used on the wrong side.

## 4. The upper saddle on exactly the required parameter paths

On \(\mathcal H\cup\mathcal V\), the original elementary guards are
\[
 \Re A>1/10,\quad |A|<4/5,\quad |1-A|<21/20.
 \tag{31}
\]
Together with (10), they imply
\[
 \Re D_0>443/800,\qquad \Re(1/W)>93/800.
 \tag{32}
\]
On \(\mathcal L\), instead
\(\Re A>1/6,\ |A|<1/3,\ |1-A|<83/100\), so
\[
 \Re D_0>2589/4000,\qquad \Re(1/W)>73/50.
 \tag{33}
\]

The imaginary sign needs a separate check because \(\Im B\le0\).
The whole rectangle gives the sufficient bound
\[
 0\le\Im(1/B)
 =\frac{2\sin\beta\sinh K}{(\cosh K+\cos\beta)^2}
 <\frac{750}{1369}<\frac35.
 \tag{34}
\]
On \(\mathcal H\), put \(S=\sinh H\). Then
\(2/3<S<5/4\), and
\[
 \frac{S}{1+S^2}\ge\frac6{13},\qquad
 -\Im(1/A)=
 \frac{2\sin a\,S}{(\cosh H+\cos a)^2}>\frac{10}{13}.
 \tag{35}
\]
The first bound follows from the single maximum of \(S/(1+S^2)\);
its other endpoint value is \(20/41>6/13\).
For \(\mathcal V\), the reciprocal imaginary modulus is
\[
 \frac{\sqrt3\sinh H}{(\cosh H-1/2)^2}.
 \tag{36}
\]
Its derivative has the sign of \(2-C^2-C/2\); hence its minimum
on \([1/10,1]\) is at an endpoint. At \(H=1/10\), use
\(C<2011/2000<101/100\), \(S>1/10\), and \(\sqrt3>5/3\)
to obtain a lower bound \(5000/7803>3/5\).
At \(H=1\), use \(S>1,\ C<8/5\) to get a still larger
lower bound \(500/363>3/5\).
On \(\mathcal L\), the same expression with \(2\sin a>8/5\)
is greater than \(1600/2601>3/5\).
Therefore, on all the stated paths,
\[
                         \Im(1/W)<0.
 \tag{37}
\]
It follows that \(W\) stays in a compact subset of the upper
right quadrant, and
\[
 y_*=\pi^{-1}\arctan\sqrt W
 \tag{38}
\]
stays a fixed distance inside the upper half-strip.

Here is an original-sheet calibration that does not enlarge (2).
At \(a=\pi/2,H=2/3\), the bare-kernel conjugate of the original
mixed-height packet is eligible for every \(u\) in (1). Its lower
outgoing partner is \(\bar u\in\mathcal U_+\), whose original
cubic height exceeds \(2/3\); the imaginary cubic equation and
the original \(b>1/2\) argument prove this uniformly. The bare
Newton kernel and the edge primitive have real coefficients and
the original real complete constant. Conjugation here calibrates
only this edge, not the crossing or the full inner trace.

First vary \(H\) in \([2/3,1]\) at \(a=\pi/2\), then increase \(a\)
to \(2\pi/3\); next vary \(H\) at \(a=2\pi/3\), then follow
\(\mathcal L\). These paths stay in (2). The exact critical identity
\[
 e^{F_y}-1=
 -\frac{(z_y^2+1)(D_0z_y^2-AB)}{z_y^4},\qquad z_y=\tan\pi y,
 \tag{39}
\]
has only the root (38) at finite height in the open strip.
At that root the force is one; the strict cut bounds prevent
any cut or zero crossing. The continuous original logarithmic
derivative starts at zero and belongs to \(2\pi i\mathbb Z\).
Thus throughout (2),
\[
 F_y(y_*)=0,\qquad F(y_*)=\psi(t,u),\qquad
 -F_{yy}(y_*)=\frac{2\pi D_0(1+W)^2}{W^{3/2}}\ne0.
 \tag{40}
\]
No continuation down the unneeded low-height face at \(a=\pi/2\)
has been used.

## 5. The real boundary has one maximum

Write \(a=\Re A\), \(A_2=|A|^2\), and use \(b,B_2\) from (10).
Here \(a\) is a temporary real-part variable, not the first angle.
For \(v=\sin^2\pi x\), the real force is
\[
 q_Aq_B=\frac{|A-v||B-v|}{v^2},\qquad
 \partial_v\log q_A=\frac{av-A_2}{v|A-v|^2}.
 \tag{41}
\]
It starts at infinity and ends below one, since
\(|1-A||1-B|<1\).

On \(\mathcal H\), one has \(A_2/a>5/8\). Indeed, with
\(C=\cosh H>11/9\) and \(d=\cos(\Re t)\in[-1/2,0]\),
\[
 (C+d)^2-\frac54(1+Cd)
 =\left(d+\frac{3C}{8}\right)^2+\frac{55C^2}{64}-\frac54
 >\frac{175}{5184}.
 \tag{42}
\]
If the \(A\)-derivative in (41) is nonnegative, then \(v>5/8\),
\(q_A^2<1\), and
\[
 q_B^2\le1+\frac{b(1-2v)+e}{v^2}<1,
 \tag{43}
\]
because \(b\ge3/5\) and \(e<3/20\).
If the \(B\)-derivative is nonnegative, then \(v\ge B_2/b\ge b\)
and \(q_B^2\le1-b/v\le2/5\). The exact convex endpoint calculation
of the original high-angle guard gives \(q_A^2\le181/100\) for
\(1/2\le v\le1\), so the force squared is at most \(181/250<1\).
Thus every force-one crossing is strictly downward.

For the other two families it is convenient to use the cubic
\[
 D(v)=v^4-|A-v|^2|B-v|^2.
 \tag{44}
\]
Its derivative is an upward quadratic with discriminant \(4\Delta\),
where
\[
 \Delta=(A_2+B_2+4ab)^2-12(a+b)(aB_2+bA_2).
 \tag{45}
\]
We prove \(\Delta<0\), which gives \(D'>0\) and hence exactly
one downward force crossing.

On \(\mathcal V\),
\[
 1/10<a\le1/4,\qquad A_2=4a^2-3a+9/16.
 \tag{46}
\]
Convexity in \(B_2\) reduces to \(B_2=b^2\) and \(B_2=b+e\).
At the first endpoint,
\[
 \Delta=A_2^2-4aA_2b+b^2\{(b-2a)^2-10A_2\}.
 \tag{47}
\]
The bracket is at most \(-191/576\): increase \(b\) to \(25/24\)
and then \(a\) to \(1/4\). Since \(A_2\le121/400\) and \(b\ge3/5\),
\[
                         \Delta\le-4459/160000<0.
 \tag{48}
\]
At \(B_2=b+e\), write
\[
\begin{split}
 \Delta&=\Delta_0(b)+e(2A_2+2b-4ab-12a^2)+e^2,\\
 \Delta_0(b)&=A_2^2+b\{(2-4a)A_2-12a^2\}
                         +b^2(-32a^2+32a-23/4).
\end{split}
 \tag{49}
\]
The \(b\)-derivative of \(\Delta_0\) at \(b=1\) is at most
\(-3/16\), and at \(b=3/5\) at most \(-31/80\).
For clarity, the two polynomials are respectively
\[
 -16a^3-56a^2+223a/4-83/8,\qquad
 -16a^3-152a^2/5+603a/20-231/40.
 \tag{50}
\]
Both increase on (46), and their values at \(a=1/4\) give
the stated bounds. Also \(-32a^2+32a-23/4\le1/4\).
After adding the \(e\)-term, the derivative at \(b=25/24\)
is therefore at most
\[
             -3/16+1/48+5/72=-7/72<0,
 \tag{51}
\]
and at \(b=3/5\) it is at most \(-31/80+5/72<0\).
It is affine in \(b\), so (49) decreases throughout the interval.
At \(b=3/5\), \(\Delta_0\) increases with \(a\): its derivative
is at least
\[
 (-1331-4350+5760)/1000=79/1000>0.
 \tag{52}
\]
These three terms bound the derivatives of \(A_2^2\), the
linear \(b\)-term, and the quadratic \(b\)-term in (49).
Consequently \(\Delta_0(3/5)\le-2039/6400\).
The extra term is less than \(1/10\), since \(e<1/20\) and
\(2A_2+6/5\le361/200\). Thus \(\Delta<0\) here as well.

On \(\mathcal L\),
\[
 \frac{3967}{20000}<a\le\frac14,\qquad A_2<1.
 \tag{53}
\]
The lower bound uses \(\cosh(1/10)<2011/2000\) and
\(-\cos(\Re t)\le3/5\). The derivative of (45) in \(A_2\) is
\[
 2A_2+2B_2-4ab-12b^2
             <2+20/9-108/25<0.
 \tag{54}
\]
It suffices to replace \(A_2\) by \(a^2\), then use convexity
in \(B_2\). At \(B_2=b^2\) the result is \(b^4F(a/b)\), where
\[
 F(r)=r^4-4r^3-6r^2-4r+1.
 \tag{55}
\]
Here \(19/100<r\le5/12\), and
\[
 F(r)\le1-4r-6r^2-\frac72r^3
                         <-\frac{1213}{2000000}.
 \tag{56}
\]
At \(B_2=b+e\), the result is
\[
 a^4-(10+4a)a^2b+(1-2a)^2b^2
                  +e\{2b(1-2a)-10a^2\}+e^2.
 \tag{57}
\]
It is convex in \(b\). At \(b=25/24\), the identity
\[
                 b+e=(25/24)^2=b^2
 \tag{58}
\]
reduces it to the already negative case. At \(b=3/5\), the
first three terms in (57) are at most \(-47097/500000\).
Indeed discard \(a^4-(12/5)a^3\le0\) and use \(a>39/200\)
in \(9/25-(36/25)a-(114/25)a^2\).
The remaining terms are less than \(1/16\), since
\(e<1/20\). Their sum is strictly negative.
This finishes the proof of \(\Delta<0\).

All three real profiles consequently increase to one maximum
and then decrease. Exact numerator zeros have zero force and
do not create further crossings; their logarithmic derivatives
are used only through integrable one-sided limits.

## 6. Side profiles and the upper main path

The original sidewise envelope is continuous and subharmonic.
Across each of its cuts the outward derivative jump is \(+2\pi\);
the starting-zero flux is \(O(\varepsilon|\log\varepsilon|)\).
The strict cut bounds exclude local minima at cuts or their
starting points. Off cuts the function is nonconstant harmonic.
Section 5 excludes minima on the real bottom.

For either sign of an angular height, the original left-side
derivative is
\[
 \pi\ \pm\{\vartheta_r(s+v)+\vartheta_r(s-v)\},\qquad
 \vartheta_r(w)=\arctan(\tan(\pi r)\tanh(\pi w)).
 \tag{59}
\]
Here \(r=\Re z/(2\pi)<3/8\); hence its derivative is at least
\(\pi/4\). The left rate starts at zero and increases strictly.

We give the right-side check for mixed signs explicitly.
At \(x=1/2\), put \(C_v=\cosh(2\pi v)\ge1\).
Using \(P>7/30\), \(|\cos u|<13/12\), and \(|\cos t|<8/5\),
the squared full boundary force is at most
\[
 \frac{(C_v+8/5)^2(C_v^2-7C_v/15+169/144)}{(C_v+1)^4}<1.
 \tag{60}
\]
The denominator deficit has successive coefficients
\[
 \frac{19}{15},\quad \frac{59}{15}-\frac{25}{144},\quad
 \frac{748}{375}-\frac59,\quad-\frac{451}{225}
 \tag{61}
\]
in degrees three through zero. They exceed \(1,3,1,-3\),
respectively, so the deficit exceeds
\(C_v^3+3C_v^2+C_v-3\ge2\).
This is a product bound; no false individual-leg bound is required.

Apply the exact matched-vector right-side calculation of the
mixed-height source with the upper and lower angular legs in their
actual positions. On the central right-side height interval, the
derivative is the difference of the arguments of the two vectors
\(P_z-C_v+i|\Im\cos z|\). Its sign is that of an affine function
of \(C_v\). An upper-side local maximum would require aligned
vectors \(\lambda e^{i\theta},\mu e^{i\theta}\), \(\lambda>\mu>0\),
for the upper and lower angular legs, respectively. The exact identity is
\[
 \Im(1/W)=
 \frac{2\sin\theta(\lambda-\mu)((1+C_v)^2-\lambda\mu)}
 {|1+\cos(\bar u)|^2\,|1+\cos t|^2}.
 \tag{62}
\]
The denominator is positive. Equation (60) says
\(\lambda\mu<(1+C_v)^2\), so (62) contradicts (37).
Thus the upper right-side profile has no local maximum.
Outside the central height interval its derivative has the fixed
outward sign; each cut jump is positive. Coincident vectors are
impossible because the incoming real cosine is nonpositive and
the outgoing one is positive.

The zero-height and zero-angle cases are also retained.
If \(K=0,\beta>0\), the outgoing contribution is \(\pi\)
above the real axis and the whole side increases. If \(\beta=0\),
the outgoing contribution is zero below \(K/(2\pi)\) and \(\pi\)
above it. The incoming contribution decreases before its own cut
and increases after it; the full side decreases to the smaller
cut height and then increases. These are limits of the same
original one-leg formula, not arguments assigned at a zero.
Every right-side strict sublevel is therefore connected or empty.
The real right endpoint is
\[
                    \mathcal F(1/2)=(H+K)/2,
 \qquad \mathcal F(0)=0.
 \tag{63}
\]

At large upper height the original primitive gives
\(\mathcal F(x+iv)=2\pi v+O(1)\), uniformly on the compact
families. There is exactly one finite simple upper critical point,
namely (38). The original rectangle/component/Jordan argument now
applies at its level \(m=\Re\psi\): every strict-sublevel component
reaches a vertical side, and the two descending germs of the saddle
cannot lie in the same component. Otherwise a simple crosscut
would surround an ascending germ, contradicting the subharmonic
maximum principle. The two germs reach the two different sides.

Move along those sides to the real endpoints. The left rate
does not exceed \(m\); the right rate does not exceed
\(\max(m,(H+K)/2)\). Thus, after an arbitrarily small fixed
tolerance, there is an upper path between fixed interior real cuts
\(\alpha,\gamma\) with rate at most that maximum.
Compact finite path covers give uniform bounded lengths and heights.
The cuts and their \(O(N^{-1})\) midpoint perturbations are connected
inside the same endpoint collars.

## 7. Full aliases, caps, physical endpoints, and proof of (4)

For both signs of the wire height the original sidewise formulas give
\[
\begin{split}
 \mathcal F(\pm iv)-2\pi v&\le
                   \frac{aH+\beta K}{2\pi},\\
 \mathcal F(1/2\pm iv)-2\pi v&\le\frac{H+K}{2}.
\end{split}
 \tag{64}
\]
Here \(a\) again denotes the first angle.
Since \(a\le a_1<3\pi/4\), \(\beta<\pi/2\), and \(H\ge1/10\),
the first bound has a reserve at least
\[
                  H/8+K/4\ge1/80
 \tag{65}
\]
below the endpoint rate. Use the original \(J_+\) and \(J_-\)
series at fixed wire height two. Their polynomial parts are
bounded by the first expression in (64), and the complete two-leg
remainder is less than \(1/600\), with both reflection terms retained.
This is the same height-two estimate used in the original vertical
and low-horizontal envelopes; all angular absolute heights here
are at most one and all real arguments stay a fixed distance
from the outer factorial endpoints.

Choose small fixed endpoint columns and a fixed \(h_c>0\).
Uniform continuity of the original zero-safe rate pays their
unweighted collars and their penalized columns at the endpoint
rate plus any prescribed tolerance. The two aliases can use
\[
 \alpha_N\pm ih_c\longrightarrow\alpha_N\pm2i
 \longrightarrow\gamma_N\pm2i
 \longrightarrow\gamma_N\pm ih_c,
 \tag{66}
\]
where
\(\alpha_N=(\lfloor N\alpha\rfloor+1/2)/N\) and
\(\gamma_N=(\lceil N\gamma\rceil-1/2)/N\).

For completeness the unchanged exact joined identity is
\[
\begin{split}
 K_N^<(t,u)={}&
 N\int_{\Gamma_+}\frac{T_N}{1-\zeta}\,dy+
 N\int_{\Gamma_-}\frac{T_N}{\zeta-1}\,dy+C_N+E_N^{\rm phys},
 \qquad \zeta=e^{2\pi iNy},\\
 C_N={}&N\int_{\gamma_N-ih_c}^{\gamma_N+ih_c}
               \frac{T_N}{\zeta-1}\,dy
       -N\int_{\alpha_N-ih_c}^{\alpha_N+ih_c}
               \frac{T_N}{\zeta-1}\,dy,\\
 E_N^{\rm phys}={}&
 \sum_{j=0}^{\lfloor N\alpha\rfloor}T_N(j/N)
 +\sum_{j=\lceil N\gamma\rceil}^{U_N}T_N(j/N).
\end{split}
 \tag{67}
\]
Both \(\Gamma_\pm\) are oriented left to right.
The reciprocal reflection identity makes \(T_N\) holomorphic
through its original numerator cuts. Split
\((1-\zeta)^{-1}=1+\zeta/(1-\zeta)\) and move only the entire
unweighted term to the upper path of Section 6. The two added
endpoint integrals have the exact orientations
\[
 N\int_{\alpha_N+ih_c}^{\alpha_N}T_N\,dy+
 N\int_{\gamma_N}^{\gamma_N+ih_c}T_N\,dy.
 \tag{68}
\]
The complete alias multipliers on (66) are bounded by
\(2e^{-2\pi N|\Im y|}\). On the midpoint caps
\(\zeta=-e^{-2\pi N\Im y}\), so the reciprocal denominator
has modulus at most one. No real residue is crossed or omitted.

The original uniform factorial theorem bounds \(T_N\) by a
polynomial times \(e^{N\mathcal F}\) on these fixed paths,
through all numerator zeros. At physical endpoints the own
factorial displacement has
\[
 N\big|J(x+1/(2N))-J(x)\big|=O(\log N),\qquad0\le x\le1/2.
 \tag{69}
\]
Thus the same zero-safe exponent, with a polynomial prefactor,
controls every row of \(E_N^{\rm phys}\), including \(j=0\),
the exact odd last row, and all exact numerator zeros.
All shifted real arguments stay in a fixed compact subinterval
of \((-1,1)\), because \(a_1<3\pi/4\) and \(\beta<\pi/2\).
Both reciprocal reflection terms and the original residue factor
\(N\) in (67) are unchanged.

Apply the rate bounds of Sections 6--7 in (67)--(69), choose their
fixed tolerances below \(\tau/2\), and absorb the fixed polynomial
factors in the remaining tolerance. This proves (4) at both parities.

## 8. What this theorem does not replace

The theorem supplies the original second-edge upper estimate along
the reflected right-hand path. It has not changed the definition of
the full inner trace. In particular, the adopted one-current inner
assembly was proved for lower outgoing angles; it is not imported
here for upper outgoing angles merely by conjugating a bare edge.
The crossing has its original fixed sign.

To bound the full reflected \(Q_N\), the original first-edge
trace tail, partial central Gaussian, negative inner interval,
left connector, far samples, and all endpoint verticals must be
retained and reassembled with eligible upper-outgoing bounds.
An upper ceiling for that full source could suffice without a
relative packet, but it is not a consequence claimed by (4).
No estimate of the signed outer observation is inferred.

## Frozen source bindings

- Original mixed-height source, side formulas, and exact caps:
  fb885dd5c25d49f2b0cdf03eb8d2ce05d303bb90fcc8523cb800832b940c4b07.
- Original enlarged cut factorization and real profile:
  8c44e62b5015b61aa7b5a19e9706e539a6b1544be5657edb2bbc78a6ab99adfc.
- Original complete upper-envelope construction:
  c7ea7e57bfcb41d7fcbc65202e281181576c76710dc5c5a00d6e436200cbb699.
- Independent rectangle modulus and reciprocal guards:
  7f3c6a64aab48f54e60dcf4c0c192f348f0d8e64c0f3547fd5783c9ef3b11ca5.
- Original low incoming-cut factor:
  2f0287cf9655c04d2b9ca0a1545707619b57f23e899c3b76430c73b143929141.
- Original joined contour:
  1588e16cedaa06fd3f9e1d403cd642032ed5929e3e7741014994af5c51058b9d.
- Original component/Jordan proof:
  b655d894a75f0744b5935f781996a386d9e78f1fe4a00ab503978842f2aa2542.
- Original deep alias primitives:
  79a0e9fb0c9b8d22819cc0acbf4495664f2c6608ca6430bbde9a2c2c0732503c.
- Original uniform zero-safe factorial source:
  4dcda2109db1db4581aa0bf7c3bafa5351e43ccd449f3337151240306ae55c11.
- Original cubic family used only to calibrate the bare edge:
  8a8ef3f93a4ab44724d43f7bb9b15c5f8210d4649f79d1f0d4c0ec277801f41a.
