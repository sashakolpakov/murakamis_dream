# Own-three seam-branch action transport through the first tenth

Private research deduction, 8 November 2026. The actual inward-seam
own-three branch continues as a simple original critical point while
its exponential coordinate stays in the lower left quadrant. Through
the first tenth of the shared real interval, it can leave that quadrant
only through the negative real axis. Along this continuation the
original action, with the first factor and full shared Fourier
allocation retained, strictly increases toward the right.

A negative-real-axis exit is controlled by the already paid real
half-index profile. If the branch reaches \(q=1/10\) first, its action
there remains an unestimated endpoint of this transport theorem.
No finite upper-row packet, contour intersection, or complete
lower-left bound is asserted. No numerical evaluation is used.

## 1. Original branch and exact stopping convention

Keep the actual ordinary-next own-three domain of
[the inward-seam branch theorem](research_mixed_next_own_three_inward_seam_branches.md).
Fix
\[
13/25<R<1,\qquad
Z=\rho e^{-2\pi iu},\quad 13/20<\rho<8/5,\quad
11/50\le u\le9/20,
\]
and put
\[
Y(q)=Re^{-2\pi iq},\qquad y(q)=q+ih_y,\qquad
R=e^{2\pi h_y},\qquad 0\le q\le1/10 .
\tag{1}
\]
The actual heights remain in their original compact ranges.
In particular \(\Im Z<0\) and \(\Re Z<8/25\).

At \(q=0\), start with the branch \(w_-\) proved in that theorem:
\[
(w-Y)(w-Z)=Y(w-1)^2,\qquad
\Re w<0,\quad\Im w<0,\quad |w|>\max(1,|Z|).
\tag{2}
\]
Continue this branch in \(q\) while it is in the open lower left
quadrant. Let \(q_e\) be its first contact with the negative real
axis if that occurs at or before \(1/10\). Otherwise set
\(q_e=1/10\), retaining the distinction that no such contact has
occurred. The arguments below prove existence of this continuation
up to the stated stopping event. They do not assume it in defining
the event.

The original critical coordinate is
\[
t(q)=\frac{\log w(q)}{2\pi i},
\qquad \pi<\arg w(q)<3\pi/2
\]
before a contact, with the continuous value \(\arg w=\pi\)
at a negative-real-axis contact. Thus
\(1/2<\Re t<3/4\) before the contact.

## 2. A uniform lower radius on every possible quadrant branch

We prove the following barrier for the entire outgoing domain:
\[
\Re w\le0,\quad\Im w\le0,\quad |w|=13/20
\quad\Longrightarrow\quad
\left|\frac{w(w-Z)}{w^2-w+1-Z}\right|<\frac{13}{25}.
\tag{3}
\]
The quotient is the exact value of \(Y\) imposed by (2).

Write
\[
w=-x-iv,\quad x,v\ge0,\quad x^2+v^2=c:=169/400,
\qquad Z=\rho e^{-i\theta},\quad
11\pi/25\le\theta\le9\pi/10 .
\]
Set
\[
\begin{split}
C(x)&=\frac{1917}{20000}+\frac{569}{200}x+4x^2,\\
A(x)&=\frac{231}{200}+\frac{41}{8}x+4x^2,\\
B(x)&=v\left(\frac{41}{8}+4x\right).
\end{split}
\]
Direct expansion gives
\[
\begin{split}
&|w^2-w+1-Z|^2-\frac{25}{16}|w-Z|^2\\
&\hspace{8mm}
=C(x)+\rho\{-A(x)\cos\theta+B(x)\sin\theta\}
 -\frac9{16}\rho^2 .
\end{split}
\tag{4}
\]
For \(A,B\ge0\), the minimum of
\(-A\cos\theta+B\sin\theta\) on this angular interval
is at an endpoint: its only possible interior critical point
is a maximum. The elementary bounds
\[
\cos(11\pi/25)<1/5,\quad
\sin(11\pi/25)>49/50,\quad
\cos(9\pi/10)<-19/20,\quad
\sin(9\pi/10)>3/10
\]
therefore bound that expression from below by the smaller of
\(-A/5+49B/50\) and \(19A/20+3B/10\).
For example the sine witness at the first endpoint follows
from \(\cos(3\pi/50)>1-(33/175)^2/2>49/50\);
the other witnesses are the elementary pentagon and cosine
bounds already used in the profile sources.

For each such angular bound, (4) is concave in
\(0\le\rho\le8/5\), so it suffices to check \(\rho=0,8/5\).
At zero it is \(C(x)\ge1917/20000>0\).
At \(8/5\), the second angular bound gives
\[
C(x)+\frac{38}{25}A(x)+\frac{12}{25}B(x)-\frac{36}{25}
\ge\frac{8229}{20000}>0.
\]
For the first angular bound it gives
\[
F(x)=
-\frac{1371}{800}+\frac{241}{200}x+\frac{68}{25}x^2
+\frac{196}{125}\sqrt{169/400-x^2}
                 \left(\frac{41}{8}+4x\right).
\tag{5}
\]
This function is strictly concave on \(0<x<13/20\).
Indeed, if \(r_0=13/20\), then
\[
\frac{d^2}{dx^2}
\left[\sqrt{r_0^2-x^2}\left(\frac{41}{8}+4x\right)\right]
=-\frac{(41/8)r_0^2+12r_0^2x-8x^3}
        {(r_0^2-x^2)^{3/2}}
\le-\frac{205}{26}.
\]
Consequently \(F''\le-90/13<0\). Its two endpoint values are
\[
F(0)=\frac{70193}{20000},\qquad
F(13/20)=\frac{2187}{10000},
\]
both positive. This proves (4) is positive, and hence (3).
The denominators used here cannot vanish at a solution of (2):
otherwise \(w(w-Z)=0\), which at \(w\ne0\) would force
\(w=Z=1\), outside this quadrant.

Since the initial branch has modulus greater than one,
(3) prevents it from crossing the circle of radius \(13/20\)
while it remains in the closed lower left quadrant.

## 3. No other exit or algebraic collision before the stopping event

Write \(Y=a-ib\), with \(a>0,b\ge0\).
On (1), \(a>(4/5)R\). At a point \(w=-iv\), \(v>0\),
the exact formula
\[
Z=\frac{(1-Y)w^2+Yw-Y}{w-Y}
\]
gives
\[
\Re Z-\frac12=
\frac{\frac12R^2+(2a-R^2-\frac12)v^2+bv^3}
     {a^2+(v-b)^2}>0 .
\tag{6}
\]
For the last sign,
\[
2a-R^2-\frac12>
\frac85R-R^2-\frac12
\ge\frac{77}{1250}>0,
\qquad 13/25\le R\le1.
\]
The quadratic is concave; its other endpoint value is \(1/10\).
Equation (6) contradicts \(\Re Z<8/25\).
Thus the branch cannot leave through the negative imaginary axis.

A double root of the quadratic in (2) would satisfy
\[
Y=\frac{w^2}{2w-1}
=\frac w2+\frac14+\frac1{4(2w-1)}.
\tag{7}
\]
If \(\Re w\le0\), its right side has real part less than
\(1/4\). This contradicts
\(\Re Y>(4/5)(13/25)=52/125\).
Thus there is no collision in the closed left half-plane.
The leading coefficient \(1-Y\) stays nonzero; on the
actual compact height range it is uniformly separated from
zero. Roots therefore cannot escape to infinity along (1).

Together, (3), (6), and (7) prove existence and simplicity
up to \(q_e\), with
\[
|w(q)|>13/20,\qquad \Re w(q)<0,\qquad \Im w(q)<0
\quad (0\le q<q_e).
\tag{8}
\]
The only possible earlier boundary is the stated negative-real-axis
contact. No assertion is made that such a contact must occur
before \(1/10\).

## 4. Preservation of the original logarithmic branch

The phase is
\[
Q_0(t;y,z)=g(t+y)+g(t+z)-2g(t)-g(y)-g(z)+2\pi iyt,
\]
with the original \(g'(v)=\operatorname{Log}(1-e^{-2\pi iv})\).
At the seam it has the zero lift proved in the branch theorem.

On the continuation (8), neither \(1/w\) nor \(Y/w\)
can cross the dilogarithm cut \([1,\infty)\):
the former has negative real part, and positive proportionality
of \(Y\) and \(w\) is impossible because their real parts have
opposite signs. The remaining possible cut is
\[
Z/w\in[1,\infty),\qquad w=\lambda Z,\quad0<\lambda\le1.
\]
It too is excluded on (1),(8).
Here \(\Re Z<0\) would be necessary. Solving (2) for \(Y\)
gives
\[
Y=\frac{\lambda(\lambda-1)Z^2}
        {1-(\lambda+1)Z+\lambda^2Z^2}.
\tag{9}
\]
For \(0<\lambda<1\), factor the denominator as
\((1-\alpha Z)(1-\beta Z)\), where
\(\alpha,\beta>0\), \(\alpha+\beta=\lambda+1\),
\(\alpha\beta=\lambda^2\).
Since \(\Re Z\le0\),
\[
|(1-\alpha Z)(1-\beta Z)|
\ge\sqrt{(1+\alpha^2\rho^2)(1+\beta^2\rho^2)}
\ge1+\lambda^2\rho^2 .
\]
It follows that
\[
|Y|\le
\frac{\lambda(1-\lambda)\rho^2}{1+\lambda^2\rho^2}
<\frac12,
\tag{10}
\]
because \(2\lambda-3\lambda^2\le1/3\) and
\(\rho^2<64/25<3\). This contradicts \(R>13/25\).
The case \(\lambda=1\) would give \(Y=0\), unless \(Z=1\);
both are excluded.

Thus all original principal logarithms continue without a cut
crossing. Their exponentiated critical equation is (2), and their
integer lift remains the initial zero lift:
\[
Q_{0,t}(t(q);y(q),z)=0 .
\tag{11}
\]
This is a phase continuation statement, not an extension of a
canonical finite-row packet or a permission to discard reciprocal
product divisors in a later contour construction.

## 5. Positive joint action transport

Keep the first incoming coordinate \(a=x+ih_a\), \(x\in P\),
and its original first main height \(h_s<0\). For a fixed
first main index
\[
s=v+ih_s,\qquad 1/6\le v\le5/12,
\]
or a first real cut \(s=1/8,1/2\), put
\[
\mathcal A_s(q)=
\Re\{Q_1(s;a,y(q))+Q_0(t(q);y(q),z)-g(y(q))\}.
\tag{12}
\]
The full shared allocation is exactly \(-g(y)\); the next
own flag is zero, so there is no outgoing halfweight.
The complete cap plane \(B_U(x)\) is independent of \(q\)
and can be added without changing the following derivatives.

The original chirps and (11) give the exact multiplier
\[
\exp\mathcal A_s'(q)=
\frac{|1-Y/S|\,|w-Y|}{|1-Y|^3},
\qquad S=e^{2\pi is}.
\tag{13}
\]
The first factor has modulus greater than \(6/7\) on the
clipped first main. Indeed \(q+v\in[1/6,31/60]\), and
radial minimization over \(|Y/S|\le1\) gives at least
\(\sin(\pi/3)=\sqrt3/2>6/7\) when the cosine is positive;
when it is nonpositive the modulus is at least one.
The same \(6/7\) lower bound holds at the real half cut.
At the real low cut, the corresponding bound is \(7/10\),
from \(q+1/8\in[1/8,9/40]\) and \(\sin(\pi/4)>7/10\).

The angle between a lower-left \(w\) and \(Y\), whose argument
lies in \([-\pi/5,0]\), is at least \(3\pi/10\).
If that angle is at most \(\pi/2\), radial minimization and
\(\sin(3\pi/10)>4/5\) give
\[
|w-Y|>|w|(4/5)>\frac{13}{25}.
\]
If the angle is larger, the stronger bound \(|w-Y|\ge|w|\)
applies. Also
\[
|1-Y|^2<9/20,
\tag{14}
\]
by \(\cos(2\pi q)>4/5\) and convexity in \(1/2\le R\le1\).

The rational comparisons
\[
\left(\frac67\frac{13}{25}\right)^2
>2\left(\frac9{20}\right)^3,\qquad
\left(\frac7{10}\frac{13}{25}\right)^2
>\frac{36}{25}\left(\frac9{20}\right)^3
\]
therefore prove
\[
\begin{cases}
\mathcal A_s'(q)>\frac12\log2,
 &s\text{ on the clipped first main or real half cut},\\
\mathcal A_{1/8}'(q)>\log(6/5),
 &s=1/8 .
\end{cases}
\tag{15}
\]
In particular every one of these original profiles satisfies
\[
\mathcal A_s(q)\le
\mathcal A_s(q_e)-\log(6/5)(q_e-q),\qquad 0\le q\le q_e .
\tag{16}
\]
The first-index upward and downward clippings in
[the joint-profile theorem, Sections 3 and 6.1](research_mixed_next_lower_left_joint_main_profiles.md)
are independent of the next factor. They extend (16), as an
upper comparison with a clipped first profile, to the original
first main range. No derivative of a maximizing or clipped index
is used.

## 6. What the stopping event does and does not pay

Suppose that \(q_e\) is a negative-real-axis contact.
Then \(\Re t(q_e)=1/2\). For fixed \(q_e\le1/10\) and
any real height \(\sigma\),
\[
\Re Q_{0,tt}(1/2+i\sigma;y(q_e),z)
=\pi\{\Re\cot\pi(1/2+i\sigma+y(q_e))
       +\Re\cot\pi(1/2+i\sigma+z)\}<0 .
\tag{17}
\]
The own cotangent has zero real part. The first shifted
term is nonpositive, and the second is strictly negative
since \(u\in[.22,.45]\).
Thus the real phase on this vertical line is strictly convex
in \(\sigma\). At the critical point its vertical derivative
vanishes by (11), so
\[
\Re Q_0(t(q_e);y(q_e),z)
\le\Re Q_0(1/2;y(q_e),z).
\tag{18}
\]
The vertical path is in the regular original strips:
the shifted real parts are \(1/2+q_e<1\) and
\(1/2+u<1\). The original branches in Section 4 agree with
those strips; no logarithmic period is added in (18).

The paired real-half profile in
[the joint-profile theorem](research_mixed_next_lower_left_joint_main_profiles.md)
is already below the unchanged following plane. Hence in this
exit case (16)--(18) give, with the complete cap plane attached,
\[
B_U(x)+\mathcal A_s(q)
<\Lambda_{123}(z)-10^{-10}
 -\log(6/5)(q_e-q)
\]
for every stated first profile, with the clippings as specified.

If the branch reaches \(q_e=1/10\) without that contact,
(16) remains a proved action transport but its endpoint action
is not bounded here. No claim is made that all actual branches
must exit before \(1/10\), or that this phase estimate controls
the full physical upper sum. A complete source argument still
needs its exact integration cycle, terminal cancellations,
all aliases and joining currents, together with the remaining
action comparison beyond this stopping rule.
