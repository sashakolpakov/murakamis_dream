# Analytic gap estimates for Conway tangle sources

23 November 2026. Research proof; frozen papers and earlier notes remain
unchanged.

The two scalar comparisons used in the Conway source bound admit
analytic proofs with their original margins: \(1/100\) for each
two-leaf alias comparison and \(1/2500\) for a proper single attachment.
No finite comparison table is a proof input here. In the attachment
argument we use its actual proper parameter region. We do not assert
the stronger auxiliary comparison on the entire artificial slope square.
The result replaces the finite comparison checks needed by those two
lemmas. It supplies no new filled-source lower bound or volume identity.

## 1. Functions, domains and the assertions

Put
\[
 J(t)=\int_0^t\log(2\sin\pi u)\,du,\quad 0\le t\le1,
 \qquad J(1-t)=-J(t),\quad J(0)=J(1/2)=J(1)=0,
\]
\[
 g(x)=J(2x)-4J(x),\quad 0\le x\le1/2,\qquad
 \widetilde g(x)=g(\max(x,1/4)),\qquad k(x)=-2J(x/2).
 \tag{1}
\]
For completeness, substitution \(t\mapsto\pi/2-t\) and the
double-angle identity give
\(\int_0^{\pi/2}\log\sin t\,dt=-(\pi/2)\log2\).
This proves the stated zero values of \(J\); reflection then proves
\(J(1-t)=-J(t)\).
The domain of \(k\) is \([0,1]\). The original product action is
\[
 \begin{split}
 m(x,y,z)={}&J(x+y)+J(z)-J(x)-J(y)\\
 &-J(z-x)-J(z-y)-J(x+y-z),\\
 D={}&\{x,y\ge0:\max(x,y)\le z\le x+y\le1\}.
 \end{split}                                                    \tag{2}
\]
All maxima below include their indicated closed domains. The convention
for \(\operatorname{arccot}\) has values in \((0,\pi)\).

For \(1/2\le X\le1\), define
\[
 a=\operatorname{arccot}X/\pi,\quad
 b=\operatorname{arccot}(X-1/(2X))/\pi,\quad
 \lambda=2\log(2X^2),\quad
 P_2(\lambda)=2g(a)+m(a,a,b)-\lambda b .
 \tag{3}
\]
The two seed assertions are
\[
 \begin{split}
 P_2(\lambda)-\max_{D,\ y\le1/2}
       \{k(x)+\widetilde g(y)+m(x,y,z)-\lambda z\}&>1/100,\\
 P_2(\lambda)-\max_D
       \{k(x)+k(y)+m(x,y,z)-\lambda z\}&>1/100 .
 \end{split}                                                    \tag{4}
\]
Thus (4) includes the full closed slope interval
\([-\log4,\log4]\).

For the attachment, suppose
\[
 \frac12<X<1,\quad Y=\sqrt{1+B^2-X^2},\quad S=X+B>0,\quad
 Y_p=Y/S,\qquad 0<Y,Y_p<1 .
 \tag{5}
\]
Set \(a=\operatorname{arccot}X/\pi\),
\(b=\operatorname{arccot}B/\pi\),
\(c=\operatorname{arccot}(X-1/S)/\pi\), and
\[
 \begin{split}
 \mu=2\log(X/Y),\qquad \lambda=2\log(X/Y_p),\\
 P(\mu,\lambda)=\max_{D,\ x\le1/2}
       \{g(x)+m(x,y,z)+\mu y-\lambda z\},\\
 Q(\mu,\lambda)=\max_D
       \{k(x)+m(x,y,z)+\mu y-\lambda z\}.
 \end{split}                                                    \tag{6}
\]
We prove
\[
 P(\mu,\lambda)-Q(\mu,\lambda)>1/2500.                            \tag{7}
\]
Replacing \(g\) by \(\widetilde g\) in the pure maximum in (6)
does not change it. Its maximum is at \((a,b,c)\). These statements
and the identification of (3) as the pure seed maximum are proved below.

## 2. Concavity, strict maxima and elementary constants

Direct differentiation gives
\[
 g'=2\log\cot\pi x,\quad g''=-4\pi/\sin(2\pi x),\qquad
 k'=-\log(2\sin(\pi x/2)),\quad k''=-\frac\pi2\cot(\pi x/2).
 \tag{8}
\]
In their open domains both second derivatives are negative.
The plateau in \(\widetilde g\) joins \(g\) with derivative zero.
It is therefore concave and continuously differentiable on \((0,1/2)\).

For \(A+B+C=1\) put \(V(A,B,C)=-\pi[J(A)+J(B)+J(C)]\).
On the positive angle triangle its negative Hessian in \(A,B\) is
\[
 \pi^2\begin{pmatrix}
 \cot\pi A+\cot\pi C&\cot\pi C\\
 \cot\pi C&\cot\pi B+\cot\pi C
 \end{pmatrix}.
 \tag{9}
\]
The diagonal entries are positive and its determinant is \(\pi^4\):
use \(\cot\pi A\cot\pi B+\cot\pi B\cot\pi C+
\cot\pi C\cot\pi A=1\). Thus \(V\) is strictly concave inside.
For \(p=z-x,q=z-y,r=x+y-z,w=1-x-y\), direct substitution gives
\[
 \pi m=V(y,x,w)+V(p,q,2r+w)+V(p+q,r,r+w).                       \tag{10}
\]
Every triple has nonnegative entries summing to one on \(D\).
Continuity proves concavity on all of \(D\). At a strict gate
the first atom detects both input variations; with them zero,
the second detects the output variation. Hence the full gate
Hessian is negative definite at every strict point.

We record why constrained maxima used below are strict when required.
At a nonvertex flat atom, an inward segment has derivative \(+\infty\),
since \(-J(t)=-t\log t+O(t)\) at zero. At a vertex atom
the singular terms cancel to a finite derivative:
\[
 V(t\alpha,t\beta,1-t(\alpha+\beta))
 =\pi t[(\alpha+\beta)\log(\alpha+\beta)
       -\alpha\log\alpha-\beta\log\beta]+O(t^2).
 \tag{11}
\]
No atom contributes a negative infinite derivative toward a strict gate.
For a fixed output \(0<z<1\), every product face has a nonvertex
flat atom: \(w=0\) gives \((y,x,0)\), \(r=0\) gives
\((z,0,1-z)\), \(p=0<q\) or \(q=0<p\) gives one zero in
the second atom, and \(p=q=0\) gives \((0,z,1-z)\) in the third.
An input endpoint either belongs to these faces or gives
\((0,z,1-z)\) in the first atom. Each is nonvertex for interior \(z\).
The extra leaf terms \(k,\widetilde g\) have no negative infinite
inward derivative; at \(y=1/2\), \(\widetilde g\) has positive
infinite derivative in the inward direction. Consequently the AC
and AA fixed-output maxima are strict and unique: their slices
contain a strict point \(x=y\in(z/2,\min(z,1/2))\).
Their profiles
are continuously differentiable by uniqueness and the envelope
formula, including across the continuously differentiable plateau seam.
Continuity at endpoint outputs follows by compactness and interpolation
with any strict state. The same argument gives unique strict
one-variable core responses whenever the fixed \(x,z\) slice contains
a strict gate.

All numerical constants needed here have short analytic bounds.
The series for \(\log((1+t)/(1-t))\), at \(t=1/3\), gives
\[
 \frac23<\log2<
 \frac23+\frac23\frac{1/27}{1-1/9}
 =\frac{25}{36}<\frac7{10}.
 \tag{12}
\]
The upper bound replaces every denominator in the tail by \(3\).
Alternating arctangent series and
\(\arctan(1/2)+\arctan(1/3)=\pi/4\) give
\[
 \arctan(1/2)>\frac{11}{24},\qquad
 \pi>4\left(\frac{11}{24}+\frac{26}{81}\right)
       =\frac{505}{162}>\frac{31}{10}.
 \tag{13}
\]
Polynomial division and integration give the independent upper bound
\[
 0<\int_0^1\frac{t^4(1-t)^4}{1+t^2}\,dt=\frac{22}{7}-\pi .
 \tag{14}
\]
Write \(\operatorname{Ti}(u)=\int_0^u\arctan(t)\,dt/t\).
Integration of its alternating series yields
\[
 \operatorname{Ti}(1/2)>\frac{35}{72},\qquad
 \operatorname{Ti}(2/3)>
 \frac23-\frac{(2/3)^3}{9}+\frac{(2/3)^5}{25}
             -\frac{(2/3)^7}{49}
 =\frac{1708762}{2679075}.
 \tag{15}
\]
Finally, \(k\) has its maximum at \(x=1/3\). Strict concavity of
sine on \([0,\pi/6]\) gives \(\sin\pi u>3u\) for
\(0<u<1/6\). Therefore
\[
 J(1/6)>\int_0^{1/6}\log(6u)\,du=-1/6,\qquad \max k<1/3 .
 \tag{16}
\]

## 3. Stationary points and the attachment response

At a strict gate let \(U=\cot\pi x,V=\cot\pi y,Z=\cot\pi z\)
and \(D_0=1-UV+Z(U+V)\). Sine addition gives
\[
 e^{m_x}=\frac{(U+V)(U-Z)}{D_0},\quad
 e^{m_y}=\frac{(U+V)(V-Z)}{D_0},\quad
 e^{-m_z}=\frac{(U-Z)(V-Z)}{D_0}.                               \tag{17}
\]
Here \(U+V,U-Z,V-Z,D_0\) are positive. For (3),
\(D_0=X^2\), \(m_x=m_y=-2\log X\), and \(m_z=\lambda\).
Thus concavity proves that (3) is the pure two-leaf maximum.
The same supporting plane applies to \(\widetilde g\), since \(a\ge1/4\).

For the attachment point in (5), take \(U=X,V=B,Z=X-1/S\).
Then
\[
 U+V=S,\quad U-Z=1/S,\quad V-Z=Y^2/S,\quad D_0=X^2 .
 \tag{18}
\]
These inequalities give a strict gate, and (17) gives
\(m_x=-2\log X,m_y=-\mu,m_z=\lambda\).
Concavity proves the assertion about the pure maximum in (6),
also with \(\widetilde g\). Notice also
\[
 |B|<X,\quad B>\frac1{2X}-X,\quad
 Y_p^2=1+(X-1/S)^2-X^2 .
 \tag{19}
\]
The first two follow separately from \(Y<1\) and \(Y_p<1\).

We need an explicit inner maximum, including its feasible branch.
For any \(p,r>0\), put \(\mu=-2\log p,\lambda=-2\log r\) and
\[
 F_{\mu,\lambda}(x)=\max_{y,z:(x,y,z)\in D}
                         \{m(x,y,z)+\mu y-\lambda z\}.
 \tag{20}
\]
For \(0<x<1\), let
\[
 A=p^2+r^2+p^2r^2,\quad U=\cot\pi x,\quad
 D_1=\sqrt{A+(A+1)U^2},\quad
 T=\frac{p^2(U+D_1)}A,\quad
 V=T-U,\quad Z=U-\frac{r^2}{p^2}T .
 \tag{21}
\]
These formulas give its unique strict maximizer
\(y=\operatorname{arccot}V/\pi,z=\operatorname{arccot}Z/\pi\).
Here is a direct check of feasibility, rather than a choice of a
squared stationary branch. We have \(D_1>|U|\), so \(T>0\)
and \(U-Z>0\). Put \(\Gamma=(1+r^2/p^2)T-2U=V-Z\).
For \(U\le0\), it is positive immediately. For \(U>0\), write
\(s=p^2+r^2,t=p^2r^2\); then
\[
 s^2D_1^2-(s+2t)^2U^2
       =A[s^2+(p^2-r^2)^2U^2]>0 ,
 \tag{22}
\]
which proves \(\Gamma>0\). The quadratic for \(T\) gives
\[
 AT^2-2p^2UT-p^4(1+U^2)=0,\qquad D_0=T\Gamma/p^2>0 .
 \tag{23}
\]
Thus \(x+y<1,z>x,z>y\); the sine-addition expression for \(D_0\)
then gives \(x+y-z>0\). All gate inequalities are strict.
Equations (17),(23) give \(e^{m_y}=p^2,e^{-m_z}=r^2\).
Strict concavity proves global maximality and uniqueness.
The profile is smooth for \(0<x<1\), concave, and continuous
at the endpoints by compactness and interpolation.

Suppose now \(p,r\ge1\) and
\[
 p^2<2r,\quad r^2<2p,\quad R=\sqrt{1+p^2+r^2},\quad
 X=\frac{R-1}{pr}.
 \tag{24}
\]
The corresponding pure parameters are
\(B=p/r-X,\ C=X-r/p,\ Y=pX,\ Y_p=rX\).
Indeed \(pX<1,rX<1\) are exactly the two inequalities in (24).
The identity \(1+B^2-X^2=p^2X^2\) and \(X+B=p/r>0\)
give the proper identities in (5). Since \(p\ge1\), \(pX<1\)
gives \(X<1\); the two inequalities in (19) give \(X>1/2\).
At the pure input \(U=X\), (21) gives \(T=p/r\), and
\[
 \begin{split}
 T_{UU}&=p^2(A+1)/D_1^3>0,\\
 1-T_U&=\frac{(1+p^2)r(r-pX)}{A-prX}>0,\\
 1-\frac{r^2}{p^2}T_U
       &=\frac{(1+r^2)p(p-rX)}{A-prX}>0 .
 \end{split}                                                   \tag{25}
\]
The denominator equals \(prD_1\) at that point and is positive.
Since \(T_U\) increases with \(U\), the last two strict inequalities
continue to every \(U\le X\). Hence as \(x>a\), the optimized
input \(y(x)\) decreases and the optimized output \(z(x)\) increases.

For \(a\ge1/4\), \(X=\cot\pi a\le1\), and
\[
 k'(a)-g'(a)=-\log[2X^2\sin(\operatorname{arccot}X/2)]>0 .
 \tag{26}
\]
For example \(2X\sin(\operatorname{arccot}X/2)<1\), as follows
by squaring and using
\(1+X^2+X\sqrt{1+X^2}>2X^2\); multiplying by \(X\le1\)
proves (26). The concave alias profile \(k+F_{\mu,\lambda}\)
therefore has its unique global maximum at some \(x_*>a\).
It may be an endpoint: (25) still gives, by continuity,
\(y_*<b,z_*>c\). Consequently the continuous gap
\(\Delta=P-Q\) has envelope derivatives
\[
 \Delta_\mu=b-y_*>0,\qquad \Delta_\lambda=z_*-c>0 .
 \tag{27}
\]
There is no assumption that the full alias maximum is interior.
Uniqueness gives the envelope formula even at an endpoint: compare
the value at the old maximizer with the new maximum and pass to
the limit using compactness. The same argument gives continuity
of these derivatives.

The inequalities in (24) imply \(1\le p,r<2\).
Increase the smaller of \(p,r\) until they agree, then increase both
to \(2\). For instance, if \(p\ge r\), increasing \(r\) to \(p\)
preserves \(p^2<2r\), while \(r^2\le p^2<2p\).
The balanced path is proper until its limiting endpoint.
Moreover
\[
 X_p=\frac{pX-r}{p^2R}<0,\qquad
 X_r=\frac{rX-p}{r^2R}<0 .
 \tag{28}
\]
Each increase decreases \(\mu\) or \(\lambda\), so (27) decreases
the gap. Continuity of the maxima on their compact domains proves
\[
 \Delta(p,r)\ge\Delta(2,2).                                    \tag{29}
\]
In particular a starting condition \(X\le2/3\) is preserved.
For the actual proper attachment with \(X\le2/3\), (19) gives
\(Y,Y_p>X\), so \(p=Y/X,r=Y_p/X>1\), and (24) applies.

## 4. An analytic corner bound

At \(p=r=2\), let \(\ell=\log2\) and
\[
 F(x)=\max_{y,z:(x,y,z)\in D}
       \{m(x,y,z)-\log4\,y+\log4\,z\},
 \qquad a_0=\arctan(2)/\pi .
 \tag{30}
\]
The involution \((x,y,z)\mapsto(x,1-z,1-y)\) preserves \(D\),
\(m\), and the displayed linear term, by \(J(1-t)=-J(t)\).
Uniqueness of the inner maximum therefore gives \(z=1-y\).
Writing \(U=\cot\pi x,D_2=\sqrt{24+25U^2}\), its stationary
equation and profile derivative are
\[
 B=\cot\pi y=\frac{D_2-5U}{6},\qquad
 F'(x)=f(U)=\log\frac{2(D_2+U)}{D_2-5U}.
 \tag{31}
\]
These also follow by setting \(p=r=2\) in (21).
Thus \(F'(a_0)=\log4,F'(1/2)=\ell\).
Direct differentiation gives
\[
 h(U)=(1+U^2)f_U=U+\frac{6+5U^2}{D_2},\qquad
 h'(U)=1+\frac{90U+125U^3}{D_2^3}>0\quad(U\ge0).
 \tag{32}
\]
Hence \(F'''(x)=\pi^2(1+U^2)h'(U)>0\) on
\([a_0,1/2]\). The derivative \(F'\) is convex there, so its
integral lies below its endpoint trapezoid:
\[
 F(1/2)-F(a_0)\le(1/2-a_0)\frac32\ell .
 \tag{33}
\]
The global concave tangent of \(F\) at \(1/2\) gives
\[
 Q(-\log4,-\log4)
 \le F(1/2)-\ell/2+\max_{0\le x\le1}\{k(x)+\ell x\}
 =F(1/2)+\ell/2 .
 \tag{34}
\]
The last maximum is \(\ell\): its derivative is
\(-\log\sin(\pi x/2)\ge0\), and \(k(1)=0\).
The pure maximum is \(g(a_0)+F(a_0)\), since
\(g'(a_0)+F'(a_0)=-\log4+\log4=0\) and both terms are concave.

For use here and below, integration of \(g'\), with \(g(1/2)=0\),
gives, for \(u=\cot\pi a\),
\[
 g(a)=\frac2\pi[\operatorname{Ti}(u)-\arctan(u)\log u],
 \quad
 g(a)+(1-a)g'(a)=\frac2\pi\operatorname{Ti}(u)+\log u .
 \tag{35}
\]
Indeed substitute \(a=1/2-\arctan(u)/\pi\) and integrate by parts.
Since \(a_0=1/2-\arctan(1/2)/\pi\), (33)--(35) give
\[
 \begin{split}
 \Delta(2,2)&\ge
 g(a_0)-(5/4-3a_0/2)\ell\\
 &=\frac{4\operatorname{Ti}(1/2)
          -(\pi-\arctan(1/2))\ell}{2\pi}\\
 &>\frac{329}{5040}\frac7{44}
   =\frac{2303}{221760}>\frac1{100}.
 \end{split}                                                   \tag{36}
\]
For the numerator use (12)--(15):
\(35/18-(22/7-11/24)(7/10)=329/5040\).
Equations (29),(36) prove the attachment assertion for \(X\le2/3\).

## 5. The analytic large-\(X\) attachment bound

For \(1/4\le a<1/2\) define the whole-interval deficit
\[
 I(a)=\min_{0\le u\le1}\{g(a)+g'(a)(u-a)-k(u)\}.
 \tag{37}
\]
Put \(a_*=\arctan\sqrt2/\pi\). For \(a\ge a_*\),
\(g'(a)\le-\log2=k'(1)\), so the minimum is at \(u=1\),
and \(I(a)=g(a)+(1-a)g'(a)\). For \(1/4\le a\le a_*\)
the minimizer is
\[
 u(a)=\frac2\pi\arcsin\frac{\tan^2(\pi a)}2 .
 \tag{38}
\]
It exceeds \(a\). To see this, put \(t=\pi a\): the needed
inequality is \(\tan^2t>2\sin(t/2)\). It holds at \(\pi/4\);
its derivative \(2\tan t\sec^2t-\cos(t/2)\) is positive thereafter.
The envelope derivative is therefore
\(I'(a)=g''(a)(u(a)-a)<0\).
On the other branch it is \((1-a)g''(a)<0\).
Thus \(I\) decreases throughout the relevant interval.

For \(X\ge2/3\), \(a=\operatorname{arccot}X/\pi\) lies between
\(1/4\) and \(\operatorname{arccot}(2/3)/\pi>a_*\).
Using (35), (15), and \(\pi<22/7\), we obtain
\[
 I(a)\ge \frac2\pi\operatorname{Ti}(2/3)-\log(3/2)
 >\frac7{11}\frac{1708762}{2679075}-\frac{177391}{437500}
 =\frac{57269}{136687500}>\frac1{2500}.                           \tag{39}
\]
The logarithm bound here is elementary:
\[
 \log(3/2)\le
 2\left(\frac15+\frac1{3\cdot5^3}+\frac1{5\cdot5^5}\right)
 +\frac2{7\cdot5^7(1-1/25)}
 =\frac{177391}{437500}.
 \tag{40}
\]
It is the positive logarithmic series at \(1/5\), with all
remaining denominators replaced by \(7\).
Add the tangent plane of \(m\) at the strict pure point to
\(k(x)\le g(a)+g'(a)(x-a)-I(a)\).
The \(x,y,z\) coefficients cancel by (18).
This proves \(Q\le P-I(a)\), and hence (7) for the remaining
parameters. The attachment proof is complete on (5).

## 6. Seed gaps increase with the output slope

For \(0<b<1\), define the fixed-output profiles
\[
 H_{AC}(b)=\max_{D,\ z=b,\ y\le1/2}\{k(x)+\widetilde g(y)+m\},
 \qquad
 H_{AA}(b)=\max_{D,\ z=b}\{k(x)+k(y)+m\}.
 \tag{41}
\]
Their strictness, uniqueness, continuous derivatives and endpoint
continuity were proved using the atoms in Section 2.
In the AC fixed-output problem, fix \(x=a\) first. Its unique
maximizing core input is \(y=a\), by the pure stationary equations
and concavity. The derivative of the resulting optimized \(x\)
profile there is \(k'(a)+m_x=k'(a)-g'(a)>0\), by (26).
Concavity therefore puts its maximizing alias input strictly above \(a\).
For AA, symmetry and uniqueness give equal maximizing inputs.
The derivative along their diagonal at \(a\) is
\(2(k'(a)-g'(a))>0\), so their common value also exceeds \(a\).

Here is the full AC response calculation, including the plateau.
Fix \(Z=\cot\pi b\), optimize the core input \(y\), and put
\(U=\cot\pi x,V=\cot\pi y\).
On the \(g\) branch, \(g'(y)+m_y=0\) and (17) give
\[
 D_0=V^2,\qquad U=\frac1{V-Z}-V,\qquad
 m_z=\log\frac{V^2}{1+Z^2-V^2}.
 \tag{42}
\]
For example the stationary equation factors by \(1+V^2\);
it is equivalent to \((U+V)(V-Z)=1\).
Here \(dU/dV=-1/(V-Z)^2-1<0\), while \(m_z\)
strictly increases with \(V>0\) on its feasible branch.
On the plateau, \(m_y=0\). With \(w=V-Z>0\), it gives
\[
 D_0=(1+V^2)/2,\quad
 U=\frac{1+Z^2-w^2}{2w},\quad
 \frac{dU}{dV}=-\frac{1+Z^2}{2w^2}-\frac12<0,\quad
 m_z=\log\frac{1+V^2}{1+2Z^2-V^2}.
 \tag{43}
\]
The last slope again strictly increases with \(V\).
Indeed \(2U(V-Z)=1+2VZ-V^2\) derives the middle formula
directly. At a feasible seam \(V=1\), both (42),(43)
give \(U=Z/(1-Z)\) and the same output slope.
Uniqueness and these derivatives continue the response from the
pure input to the alias optimum. Increasing \(x\) decreases \(U\),
increases \(V\), and strictly increases \(m_z\).
Consequently \(H_{AC}'(b)>\lambda\).

For AA the maximizing inputs are equal. At fixed \(Z\),
\[
 m_z=\log(2UZ-U^2+1)-2\log(U-Z),\qquad
 \frac{\partial m_z}{\partial U}
 =-\frac{2(1+Z^2)}{(2UZ-U^2+1)(U-Z)}<0 .
 \tag{44}
\]
Its maximizing input exceeds \(a\), so \(H_{AA}'(b)>\lambda\)
as well. These arguments require only strict fixed-output maxima;
they make no interior assumption about later conjugate maxima.

Let \(A_J(\lambda)=\max_{0\le z\le1}\{H_J(z)-\lambda z\}\)
for \(J=AC,AA\). Concavity and the strict derivative inequality
at the pure output \(b(\lambda)\) imply that every maximizing
output of \(A_J\) is greater than \(b(\lambda)\), including when
that maximum occurs at \(1\). The conjugates are Lipschitz.
At almost every slope their derivatives are \(-z_J(\lambda)\),
where \(z_J\) is a maximizing output; this follows by comparing
maximizers at nearby slopes and using compactness.
Since \(P_2'(\lambda)=-b(\lambda)\), their gaps obey
\[
 \frac{d}{d\lambda}(P_2-A_J)
       =z_J(\lambda)-b(\lambda)>0
       \quad\hbox{almost everywhere}.
 \tag{45}
\]
Lipschitz continuity and integration prove that both gaps are
nondecreasing on the entire closed slope interval.
It remains to bound them at \(\lambda=-\log4\).

## 7. The two seed endpoints

At that endpoint \(a=a_0=\arctan2/\pi\), and the pure output is
\(1-a_0\). The tangent of \(\widetilde g\) at \(a_0\) has
slope \(-\log4\). Thus the AC conjugate is at most
\[
 g(a_0)+a_0\log4+Q(-\log4,-\log4),
 \tag{46}
\]
whereas \(P_2=g(a_0)+a_0\log4+P(-\log4,-\log4)\).
The AC endpoint gap is therefore greater than \(1/100\) by (36).

For AA, symmetry and concavity allow its two inputs to be equal:
averaging them cannot decrease either the two \(k\) terms or \(m\).
Write
\[
 F_2(s)=\max_z\{m(s,s,z)+\log4\,z\},\qquad 0\le s\le1/2.
 \tag{47}
\]
For \(0<s<1/2\), set \(U=\cot\pi s>0,D_3=\sqrt{1+5U^2}\).
The unique feasible critical branch and its derivatives are
\[
 Z=\cot\pi z=5U-2D_3,\qquad
 F_2'(s)=2\log\frac{4U}{D_3-2U},\qquad
 F_2''(s)=-2\pi\left(\frac1U+\frac2{D_3}\right).
 \tag{48}
\]
Indeed \(m_z=-\log4\) is the quadratic
\(Z^2-10UZ+5U^2-4=0\); only its displayed root has \(Z<U\).
It has \(U-Z>0,D_0=(U-Z)^2/4>0\), proving every strict
gate inequality. Differentiating the inner logarithm gives
\(1/[UD_3(D_3-2U)]\), which proves (48).
The pure value is \(P_2=2g(a_0)+F_2(a_0)\).

The concave AA profile \(2k+F_2\) has positive derivative at
\(a_0\), by (26), so its global maximum has \(s>a_0\).
On that interval \(U\le1/2\), and (48) gives \(F_2''\le-4\pi\).
Since \(F_2'(a_0)=4\log2\), continuity at \(s=1/2\) yields
\[
 F_2(s)\le F_2(a_0)+4\ell(s-a_0)-2\pi(s-a_0)^2
       \le F_2(a_0)+2\ell^2/\pi .
 \tag{49}
\]
Using (16), the AA endpoint gap is strictly greater than
\(2g(a_0)-2/3-2\ell^2/\pi\).
The elementary bounds in Section 2 give
\[
 g(a_0)>\frac7{11}
       \left(\frac{35}{72}+\frac{11}{24}\frac23\right)
       =\frac{133}{264},\qquad
 \frac{2\ell^2}{\pi}<\frac{49}{155}.
 \tag{50}
\]
Consequently
\[
 P_2(-\log4)-A_{AA}(-\log4)>
 \frac{133}{132}-\frac23-\frac{49}{155}
 =\frac{169}{6820}>\frac1{100}.
 \tag{51}
\]
Equations (45),(46),(51) prove both seed assertions (4).

## 8. Source scope and complete coverage texts

Equations (4),(7) have exactly the margins used by the original
two-leaf and single-attachment lemmas. They apply to the same full
product domain and retain the core plateau. The attachment argument
uses both proper inequalities \(Y<1,Y_p<1\); it does not prove the
separate auxiliary square-gap statement for nonproper slope pairs.
The two required lemmas therefore no longer depend on finite
supporting-plane tables. Their scalar propagation through the
original shared indices can use these estimates unchanged.

All arguments above are scalar upper-comparison arguments. They do
not construct a nonzero geometric packet after arbitrary short
filling, rebase the global remainder at a filled-parent action,
identify an original cycle coefficient, or prove a new volume case.
The original finite algebra, normal channels, source caps and filling
normalizations are supplied by their existing source theorems.
No alteration of those objects is involved in this analytic proof.

The following complete matching texts were read. The scalar proof is
written in full above; the texts identify its source application and
the previous coverage.

| Text | Lines | SHA-256 |
|---|---:|---|
| [Frozen source definitions and theorem](../papers/conway-source-bounds/main.tex) | 316 | 7776205358839357f2484cd37aaeaf3e8655e27ecec56410fbc5c2cf2d21bf22 |
| [Frozen comparison statements](../papers/conway-source-bounds/composition.tex) | 181 | 15de1c92f7c46a439382e6887d9bc78f58f17d4f9fc434cb26620e11e095359d |
| [Earlier two-leaf response argument](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/actual_conway_two_leaf_monotone_alias_response.md) | 311 | 9b66411b0cd6e11fd2bce73e8664d3a1140f0e18f8ea7114661675d2ff39ebfe |
| [Earlier analytic leaf threshold](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/actual_conway_algebraic_leaf_alias_certificate.md) | 335 | b52230acf4fd745b23990df7adcadd2c5f1c2abb191b8b8620cae9dd5a793596 |

The addition is an analytic proof of the original uniform comparisons,
including the proper attachment reduction and the two corner bounds.
No general novelty is claimed for concavity, envelope differentiation
or elementary integral inequalities. Only written mathematics and
text/hash operations were used; no mathematical program, test, build,
git operation, frozen-paper edit or earlier-final edit was performed.
