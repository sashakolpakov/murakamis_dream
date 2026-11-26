# Seam-branch action transport through three twentieths

Private research deduction, 8 November 2026. The original own-three
seam branch and joint action transport continue through \(q=3/20\),
unless the branch first reaches the already paid half-index boundary.
A new vertical barrier keeps the exponential critical coordinate
strictly to the left of \(-1/6\). It supplies a positive joint action
derivative even beyond the first tenth.

This is a companion to the frozen
[first-tenth theorem](research_mixed_next_own_three_seam_action_transport.md).
The stopping endpoint at \(3/20\) remains unpaid if no half-index
contact has occurred. A finite upper-row contour and packet remain
separate. No numerical evaluation or frozen-source edit is used.

## 1. Actual domain and strengthened branch guard

Keep every actual parameter, original phase, allocation, and branch
of the first-tenth theorem. In particular
\[
Y(q)=Re^{-2\pi iq},\quad 13/25<R<1,\qquad
Z=\rho e^{-2\pi iu},\quad u\in[11/50,9/20],
\]
and now allow \(0\le q\le3/20\).
The actual ordinary own-three outgoing height gives the sharper
bound
\[
\rho<\frac{43}{28},\qquad \Re Z<\frac{43}{140}.
\tag{1}
\]
Indeed \(2\pi h_z<17\pi/125<3/7\) when \(h_z>0\), and
the positive exponential-series bound gives
\[
e^{3/7}<
1+\frac37+\frac{(3/7)^2}{2(1-1/7)}
=\frac{43}{28}.
\]
When \(h_z\le0\) the claim is immediate.
Also \(\cos(2\pi u)<1/5\), as in the seam theorem.
The existing \(13/20\) radius barrier only needed
\(\rho<8/5\), so it remains valid unchanged.

Let \(w=w(q)\) solve the original equation
\[
(w-Y)(w-Z)=Y(w-1)^2,
\tag{2}
\]
starting at the seam branch \(w_-\).
As long as this branch is in the lower left quadrant, its radius
is greater than \(13/20\). We claim the stronger real-part guard
\[
\boxed{\qquad \Re w<-1/6 .\qquad}
\tag{3}
\]

First, (3) holds initially. At \(q=0\) the seam rational map is
\[
Z=(1-R)w+R(2-R)-\frac{R(1-R)^2}{w-R}.
\]
If \(-1/6\le\Re w\le0\), its real part would satisfy
\[
\Re Z>-\frac{1-R}{6}+R(2-R)>\frac23,
\]
contrary to (1).

To exclude a later crossing of (3), write \(Y=a-ib\) and
suppose \(w=-1/6-iv\), \(v\ge0\). The radius barrier gives
\[
v^2>\frac{169}{400}-\frac1{36}=\frac{1421}{3600},
\qquad v>\frac{37}{60}.
\tag{4}
\]
The exact quotient
\[
Z=\frac{(1-Y)w^2+Yw-Y}{w-Y}
\]
has
\[
\begin{split}
\Re Z-\frac{23}{72}
={}&\frac{
v^2\{(13/6)a-R^2-35/72+bv\}
+(7/8)R^2+(168a-35)/2592}
 {|w-Y|^2}.
\end{split}
\tag{5}
\]
All numerator terms in (5) are positive. Put
\(\theta=2\pi q\in[0,3\pi/10]\). The function
\((13/6)\cos\theta+(37/60)\sin\theta\) is concave on
this interval. At zero it is \(13/6\); at the other endpoint,
using \(\cos(3\pi/10)>7/12\) and
\(\sin(3\pi/10)>4/5\), it exceeds
\[
\frac{91}{72}+\frac{37}{75}
=\frac{3163}{1800}>\frac74 .
\]
Thus (4) implies
\[
\frac{13}{6}a+bv-R^2-\frac{35}{72}
>\frac74R-R^2-\frac{35}{72}>0.
\tag{6}
\]
The last concave quadratic has endpoint values
\(6907/45000\) and \(19/72\) on \([13/25,1]\).
Also \(a>7R/12>91/300\), so \(168a-35>0\).
Equation (5) consequently gives
\(\Re Z>23/72>43/140\), contradicting (1). This proves
the barrier (3).

There is no double root before a negative-real-axis contact.
The exact double-root formula in the first-tenth theorem,
\[
Y=\frac w2+\frac14+\frac1{4(2w-1)},
\]
has real part less than \(1/4\) when \(\Re w\le0\).
Here \(\Re Y>91/300>1/4\).
There is no escape through the imaginary axis because of (3),
and no root can escape to infinity on the actual compact
parameter set, since \(1-Y\) is uniformly nonzero.

The outgoing principal-cut exclusion of the first-tenth theorem
uses only \(R>1/2\), \(\rho^2<3\), and the lower-left quadrant.
It therefore applies without a change. All original logarithmic
branches continue, and the zero lift
\[
Q_{0,t}(t(q);y(q),z)=0,\qquad
t(q)=\frac{\log w(q)}{2\pi i},\quad
\pi<\arg w<3\pi/2,
\tag{7}
\]
persists to the first negative-real-axis contact or to \(q=3/20\).
No such contact is assumed to occur.

## 2. A distance bound supplied by the new guard

For \(Y=a-ib\), \(a,b>0\), and
\[
w=-x-iv,\quad x>1/6,\quad v\ge0,\quad |w|>13/20,
\]
elementary distance minimization gives
\[
|w-Y|^2\ge
(a+1/6)^2+
\left(\sqrt{1421}/60-b\right)_+^2 .
\tag{8}
\]
To see this, first fix \(x\). If the radial constraint is inactive,
the minimum over \(v\ge0\) is at \(v=b\). Otherwise the minimum
lies on \(x^2+v^2=(13/20)^2\). On that circle the squared
distance is
\((13/20)^2+R^2+2ax-2b\sqrt{(13/20)^2-x^2}\), which
increases with \(x\). Thus its minimum in the allowed half-plane
is at \(x=1/6\), proving (8).

Since \(\sqrt{1421}/60>5/8\), the weaker bound
\[
|w-Y|^2\ge(a+1/6)^2+(5/8-b)_+^2
\tag{9}
\]
suffices. At fixed \(R\), the right side decreases as
\(\theta=\arg(\overline Y)\) increases through
\([0,3\pi/10]\). This follows directly by differentiation,
separately before and after \(R\sin\theta=5/8\).
The bounds \(\cos(3\pi/10)>7/12\) and
\(\sin(3\pi/10)<5/6\) then imply
\[
|w-Y|^2>
L(R):=\left(\frac{7R}{12}+\frac16\right)^2+
\left(\frac58-\frac{5R}{6}\right)_+^2.
\tag{10}
\]

## 3. Joint positive transport on the two added intervals

Retain the original first main or real-cut profiles and define
\(\mathcal A_s(q)\) exactly as in the first-tenth theorem:
\[
\mathcal A_s(q)=
\Re\{Q_1(s;a,y(q))+Q_0(t(q);y(q),z)-g(y(q))\}.
\]
The first main can be clipped to
\(1/6\le\Re s\le5/12\), at its original negative height;
the original real cuts are \(s=1/8,1/2\).
The exact shared multiplier remains
\[
\exp\mathcal A_s'(q)
=\frac{|1-Y/S|\,|w-Y|}{|1-Y|^3},
\qquad S=e^{2\pi is}.
\tag{11}
\]
In particular the original next chirp is still included.

For \(1/10\le q\le1/8\), every stated first profile has
\(|1-Y/S|>1\). On the first main and half cut the shifted
cosine is nonpositive. At the real low cut it is less than
\(\sin(\pi/20)<1/6\), and \(R>13/25>1/3\) gives the same
strict modulus bound. Also \(\cos(2\pi q)>7/10\), whence
\[
|1-Y|^2<3/5,\qquad
|w-Y|>\Re Y+\frac16>
\frac7{10}\frac{13}{25}+\frac16=\frac{199}{375}.
\tag{12}
\]
Thus the squared multiplier in (11) is greater than
\(39601/30375>126/125\).

For \(1/8\le q\le3/20\), put
\[
D(R)=1+R^2-\frac76R,\qquad
U(R)=1+\frac{R^2}{4}+\frac R4 .
\]
Then
\[
|1-Y|^2<D(R),\qquad |1-Y/S|^2>U(R)
\tag{13}
\]
for every stated first profile.
For a clipped first main, the shifted cosine is at most
\(-1/4\), because
\(q+\Re s\in[7/24,17/30]\). For the real low cut it is
nonpositive, giving \(1+R^2>U(R)\); the real half cut
gives the stronger \(1+R^2+2R\cos(2\pi q)>U(R)\).
The elementary endpoint witnesses for the main are
\(\sin(\pi/12)>1/4\) and
\(\cos(17\pi/15)<-1/2\).

On \(13/25\le R\le1\),
\[
U(R)>\frac74D(R).
\tag{14}
\]
Indeed the difference
\(-3/4-3R^2/2+55R/24\) is concave and has endpoint
values \(541/15000,1/24\).
We next prove
\[
L(R)>\frac47D(R)^2.
\tag{15}
\]
If \(13/25\le R\le3/4\), the expression (10) is
\[
L(R)=\frac{149}{144}R^2-\frac{61}{72}R+\frac{241}{576}.
\]
The difference \(L-(4/7)D^2\) is increasing on this interval.
Until \(R=7/12\), \(D'\le0\) and \(L'>0\).
After that point,
\[
L'\ge\frac{311}{864}>\frac{11}{42},
\qquad
\frac87DD'\le\frac87\frac{11}{16}\frac13=\frac{11}{42}.
\]
At \(R=13/25\),
\[
L=\frac{92749}{360000}>\frac9{35},\qquad
D=\frac{2489}{3750}<\frac23 .
\]
The first cross-product difference is \(6215>0\), and hence
\[
L-\frac47D^2>\frac9{35}-\frac{16}{63}=\frac1{315}
\quad (13/25\le R\le3/4).
\tag{16}
\]
For \(3/4\le R\le1\), (10) is the square of
\(7R/12+1/6\). The concave difference
\[
\frac{7R}{12}+\frac16-\frac45D(R)
=-\frac45R^2+\frac{91}{60}R-\frac{19}{30}
\]
has endpoint values \(13/240,1/12\). Therefore
\[
L>\frac{16}{25}D^2>\frac47D^2
\tag{17}
\]
on this remaining interval.

Equations (10), (13)--(17) quantify the multiplier gap.
For \(R\le3/4\), use \(D\le5/6\) to obtain
\[
\exp(2\mathcal A_s')>
1+\frac1{180D^2}\ge\frac{126}{125}.
\]
For \(R\ge3/4\), the stronger lower bound is \(28/25\).
Together with (12) and the first-tenth theorem, this proves
\[
\boxed{\qquad
\mathcal A_s'(q)>\frac12\log\frac{126}{125}
\qquad}
\tag{18}
\]
throughout the continued branch up to \(q=3/20\), for every
stated first main or real-cut profile.

## 4. Exact stopping conclusion and retained obligations

Let \(q_e\le3/20\) be the first negative-real-axis contact, if
one occurs, and otherwise put \(q_e=3/20\). The branch exists
to this stopping event by Section 1, with its original zero lift.
The proved transport is
\[
\mathcal A_s(q)\le
\mathcal A_s(q_e)
-\frac12\log(126/125)(q_e-q),
\qquad 0\le q\le q_e .
\tag{19}
\]
The first-index clippings are used only as upper comparisons;
no derivative of a clipped or maximizing index is taken.

At an actual negative-real-axis contact, \(\Re t=1/2\).
The strict vertical convexity argument in Section 6 of the
first-tenth theorem still applies: both shifted real parts
\(1/2+q_e\) and \(1/2+u\) lie in \((0,1)\).
The critical action is at most the original real-half action.
After the complete cap plane is attached, the paired profile
theorem therefore pays that endpoint and all earlier actions
in (19), with the original strict deficit.

If there is no such contact by \(3/20\), the action there is
unpaid. This result neither forces that contact nor estimates
the finite upper conditional block. Its exact reversed source,
terminal zeros, principal divisors, integration-cycle selection,
aliases and joins must all remain in any subsequent finite
argument. No full lower-left remainder or new knot-family
conclusion follows from (19) alone.
