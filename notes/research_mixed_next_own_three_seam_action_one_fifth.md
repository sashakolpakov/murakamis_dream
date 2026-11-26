# Seam-branch action transport through one fifth

Private research deduction, 8 November 2026. This extends the frozen
[three-twentieths theorem](research_mixed_next_own_three_seam_action_three_twentieths.md)
to \(q=1/5\), unless the selected branch first reaches the paid real
half-index face. Two stronger real-part barriers give a uniform positive
derivative for the original joint action. A no-contact endpoint at
\(q=1/5\) remains unpaid. No finite upper-row contour or packet is asserted.

All calculations below are written inequalities. No numerical evaluation,
source replay, or edit of a frozen input is used.

## 1. Original domain and two barriers

Retain the actual ordinary own-three parameters, branches, phases and
weights of the [first-tenth theorem](research_mixed_next_own_three_seam_action_transport.md):
\[
Y=Re^{-2\pi iq},\quad 13/25<R<1,\quad
Z=\rho e^{-2\pi iu},\quad 11/50\le u\le9/20,
\qquad 0\le q\le1/5.
\tag{1}
\]
The actual outgoing height and the elementary exponential witness in
the three-twentieths theorem give
\[
\rho<43/28,\qquad \Re Z<43/140<5/16.
\tag{2}
\]
The branch starts at the original inward-seam root \(w_-\) and solves
\[
(w-Y)(w-Z)=Y(w-1)^2.
\tag{3}
\]
We follow it only while \(\Re w<0,\Im w<0\), stopping at its first
negative-real-axis contact if one occurs.

Write \(Y=a-ib\) and \(w=-x-iv\). Direct division of
\[
Z=\frac{(1-Y)w^2+Yw-Y}{w-Y}
\]
gives, for any real \(c\),
\[
\begin{split}
|w-Y|^2(\Re Z-c)
={}&bv^3+[a(2+x)-R^2-x-c]v^2\\
&+b[x^2+2x-1+2c]v\\
&+R^2(1+x+x^2-c)+ax(1-2c)
 -(1-a)x^3-cx^2.
\end{split}
\tag{4}
\]
We prove the uniform barriers
\[
\Re w<-3/4,\qquad
R\ge7/10\ \Longrightarrow\ \Re w<-1.
\tag{5}
\]

For their initial validity, the original seam map is
\[
Z=(1-R)w+R(2-R)-\frac{R(1-R)^2}{w-R}.
\]
Its last term has positive real part in the left half-plane. Thus
\(-3/4\le\Re w<0\) would imply
\[
\Re Z>\frac{11}{4}R-R^2-\frac34
\ge\frac{256}{625}>\frac5{16}.
\]
For \(R\ge7/10\), \(-1\le\Re w<0\) would similarly imply
\[
\Re Z>3R-R^2-1\ge\frac{61}{100}>\frac5{16}.
\]
The displayed lower bounds follow by concavity and endpoint comparison.
Both contradict (2).

For later crossings put \(\theta=2\pi q\in[0,2\pi/5]\).
Every angular expression \(A\cos\theta+B\sin\theta\) below has
\(A>0,B\ge0\), is positive and concave, and therefore is bounded below
by its endpoint values. At the right endpoint,
\[
\cos(2\pi/5)>3/10,\qquad \sin(2\pi/5)>19/20.
\tag{6}
\]
These follow from \(\cos(2\pi/5)=(\sqrt5-1)/4\) and
\(\sin^2(2\pi/5)=(5+\sqrt5)/8\), using respectively
\(\sqrt5>11/5\) and \(\sqrt5>111/50\).

At \(x=3/4,c=5/16\), the numerator in (4) is
\[
N=bv^3+\left(\frac{11}{4}a-R^2-\frac{17}{16}\right)v^2
 +\frac{27}{16}bv+2R^2+\frac{45}{64}a-\frac{153}{256}.
\tag{7}
\]
At \(\theta=0\), the coefficient of \(v^2\) is a concave quadratic
with endpoint values \(971/10000,11/16\) on \([13/25,1]\).
The constant is increasing in \(R\), with left value
\(49403/160000>0\).
At the other endpoint, (6) gives the lower bound
\[
N\ge
Rv\left(\frac{19}{20}v^2-\frac74v+\frac{513}{320}\right)
 +2R^2+\frac{27}{128}R-\frac{153}{256}>0.
\tag{8}
\]
Indeed
\[
R^2-\frac{103}{40}R+\frac{17}{16}<0
\]
by convexity and endpoint values \(-61/10000,-41/80\).
This supplies the coefficient \(-7R/4\) in (8).
The quadratic in \(v\) has discriminant \(-4847/1600<0\).
The remaining constant increases with \(R\), with left value
\(8453/160000>0\). Angular concavity now proves \(N>0\)
throughout the interval, contradicting (2).

For the second barrier use \(x=1,c=5/16\). Then
\[
N=bv^3+\left(3a-R^2-\frac{21}{16}\right)v^2
 +\frac{21}{8}bv+\frac{43}{16}R^2+\frac{11}{8}a-\frac{21}{16}.
\tag{9}
\]
At \(\theta=0\), the coefficient of \(v^2\) has endpoint
values \(119/400,11/16\) on \([7/10,1]\); the increasing
constant has left value \(1547/1600>0\).
At the other endpoint,
\[
N\ge
Rv\left(\frac{19}{20}v^2-\frac74v+\frac{399}{160}\right)
 +\frac{43}{16}R^2+\frac{33}{80}R-\frac{21}{16}>0.
\tag{10}
\]
Here the convex coefficient difference
\[
R^2-\frac{53}{20}R+\frac{21}{16}
\]
has endpoint values \(-21/400,-27/80\). The quadratic in
\(v\) in (10) has discriminant \(-5131/800<0\), and the
increasing remaining constant has left value \(469/1600>0\).
Again (2) excludes the crossing. This proves (5).

## 2. Continuation of the original phase

The first barrier in (5) implies \(|w|>3/4>13/20\), so the
earlier radial guard is automatic. At a double root, the exact
elimination identity remains
\[
Y=\frac w2+\frac14+\frac1{4(2w-1)}.
\tag{11}
\]
If \(\Re w\le-3/4\), its right side has real part less than
\(-1/8\), whereas \(\Re Y>0\) in (1). Thus there is no collision.
There is no imaginary-axis exit by (5), and no escape to infinity
on the actual compact parameter set, since the leading coefficient
\(1-Y\) stays nonzero.

The outgoing principal-cut exclusion in the first-tenth theorem uses
only \(R>1/2,\rho^2<3\), and the lower-left quadrant. It still applies;
the own and incoming primitive divisors are excluded in that quadrant
as before. Hence every original logarithmic branch continues, with
\[
t(q)=\frac{\log w(q)}{2\pi i},\qquad
\pi<\arg w<3\pi/2,\qquad Q_{0,t}(t(q);y(q),z)=0.
\tag{12}
\]
The equality in (12) retains the original zero lift. It is not obtained
by replacing an argument by its principal value after continuation.
The branch therefore reaches either its first negative-real-axis
contact or \(q=1/5\). A contact is not assumed.

## 3. Joint action on the added interval

Retain a first main profile at its original negative height, clipped
as in the [joint-profile theorem](research_mixed_next_lower_left_joint_main_profiles.md)
to \(1/6\le\Re s\le5/12\), or either original real first cut
\(s=1/8,1/2\). Put \(S=e^{2\pi is}\), and retain the complete
shared Fourier allocation:
\[
\mathcal A_s(q)=
\Re\{Q_1(s;a,y(q))+Q_0(t(q);y(q),z)-g(y(q))\}.
\]
The original phases, including the next chirp, give exactly
\[
e^{\mathcal A_s'(q)}
=\frac{|1-Y/S|\,|w-Y|}{|1-Y|^3}.
\tag{13}
\]
For \(3/20\le q\le1/5\), define
\[
D=1+R^2-\frac35R,\qquad
U=1+\frac{R^2}{4}+\frac25R.
\tag{14}
\]
Then
\[
|1-Y|^2<D,\qquad |1-Y/S|^2>U.
\tag{15}
\]
The first inequality follows from \(\cos(2\pi q)>3/10\).
For the clipped first main,
\[
q+\Re s\in[19/60,37/60],\qquad
\cos(2\pi(q+\Re s))<-2/5.
\]
At the left endpoint use
\(\sin(2\pi/15)>\sin(5/12)>2/5\), the last inequality following
from the cubic sine lower bound; at the right endpoint the cosine
is less than \(-1/2\). The intermediate cosine is no larger.
The original first height gives \(e^{2\pi\Im s}>1/2\), proving
the second inequality in (15).
For the real low cut the shifted cosine is less than
\(-\sin(\pi/20)<-3/20\), so its squared modulus exceeds
\(1+R^2+3R/10>U\). The sine witness follows from
\(\pi/20>5/32\) and \(\sin(5/32)>3/20\).
For the real half cut, its squared modulus exceeds
\(1+R^2+3R/5>U\).

If \(13/25<R\le7/10\), the first barrier gives
\[
|w-Y|>\frac34+\frac3{10}R>\frac89D,\qquad
U>\frac{13}{10}D.
\tag{16}
\]
The last difference is the concave quadratic
\[
-\frac3{10}-\frac{21}{20}R^2+\frac{59}{50}R,
\]
whose endpoint values are \(371/12500,23/2000\).
The middle difference in (16) is
\[
-\frac89R^2+\frac56R-\frac5{36},
\]
with endpoint values \(1217/22500,2/225\).
Thus (13) squared is greater than
\[
\frac{13}{10}\left(\frac89\right)^2=\frac{416}{405}.
\tag{17}
\]
If \(7/10\le R<1\), the second barrier gives
\[
|w-Y|>1+\frac3{10}R>\frac{13}{14}D,\qquad
U>\frac{33}{28}D.
\tag{18}
\]
The exact differences are
\[
U-\frac{33}{28}D=\frac{(1-R)(26R-5)}{28},\qquad
1+\frac3{10}R-\frac{13}{14}D
=\frac{(1-R)(13R+1)}{14}.
\]
The squared multiplier consequently exceeds
\[
\frac{33}{28}\left(\frac{13}{14}\right)^2
=\frac{5577}{5488}.
\tag{19}
\]
Both (17) and (19) exceed \(126/125\). Combining this with
the frozen first-tenth and three-twentieths bounds proves
\[
\boxed{\quad
\mathcal A_s'(q)>\frac12\log(126/125)>0
\quad}
\tag{20}
\]
through the entire continued interval, for every stated first profile.
No coherent first sum has been replaced by a positive sum here.

## 4. Paid stopping event and remaining obligation

At a negative-real-axis contact \(q_e\le1/5\), the original lift has
\(\Re t=1/2\). Along that half-index line,
\[
\Re Q_{0,tt}(1/2+i\sigma;y,z)
=\pi\{\Re\cot\pi(1/2+i\sigma+y)
      +\Re\cot\pi(1/2+i\sigma+z)\}<0.
\tag{21}
\]
Both shifted real parts lie between \(1/2\) and \(1\); at \(q=0\)
the first term may vanish, while the second is still strictly negative.
Thus the real action is strictly convex in \(\sigma\). Its critical
height has no larger action than the real half-index profile.
The joint-profile theorem pays that profile with the same first
main or real-cut profile, the same cap support, and the same complete
shared Fourier weight. Equation (20) then pays all earlier actions
on this branch as well.

If no such contact occurs, (20) only transports the action to the
still unpaid value at \(q=1/5\). This note supplies no bound for that
value and no assertion that contact must occur. The complete reflected
upper finite sum still needs its own source-valid contour, all retained
rows, endpoint pieces, aliases and joins. In particular this phase
theorem is not a complete next own-three estimate or a new family result.
