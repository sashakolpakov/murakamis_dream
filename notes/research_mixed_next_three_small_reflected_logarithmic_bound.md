# A centered logarithmic bound for the remaining small reflected indices

Research proof, 8 November 2026. A lower bound for the outgoing
geometric radius gives a comparison for the small reflected indices
that the shallower-strip argument leaves untreated. This is a
continuous rate inequality with explicit hypotheses. The upper bound
on the incoming radius still requires its separate geometric
certificate.

## 1. The rate and the precise hypotheses

Let
\[
Y=R e^{-2\pi iq},\qquad Z=\rho e^{-2\pi iu},\qquad
0<R\le\frac{41}{50},\quad \rho\ge\frac45,\quad
0\le q\le\frac{11}{50},\quad
\frac{11}{50}\le u\le\frac9{20}.
\tag{1}
\]
Define the real sine integral, with its constant fixed at zero, by
\[
J(t)=\int_0^t\log(2\sin\pi s)\,ds,\qquad 0\le t\le1.
\tag{2}
\]
The integrals at zero and one are improper integrals. The logarithmic
singularities are integrable. The original own-three row rate is
\[
\begin{split}
E(t;y,z)
={}&\int_0^t\log|1-Ye^{-2\pi is}|\,ds
+\int_0^t\log|1-Ze^{-2\pi is}|\,ds\\
&-2J(t)-t\log R .
\end{split}
\tag{3}
\]
Write \(v=1-t\), \(T=1/R\), and
\[
L_0=-\log R+\log_+\rho,\qquad
\log_+\rho=\max(0,\log\rho).
\tag{4}
\]
The integral over the full circle of the outgoing logarithm is
\(\log_+\rho\). Thus \(E(1;y,z)=L_0\).
The reflection identity, with both radial terms retained, is
\[
\begin{split}
\Phi(v)&=E(1-v;y,z)-L_0\\
&=2J(v)
-\int_{q-v}^{q}\log|T-e^{2\pi is}|\,ds
-\int_{u-v}^{u}\log|1-\rho e^{2\pi is}|\,ds .
\end{split}
\tag{5}
\]
This is the identity of
[the upper-end theorem, Section 2](research_mixed_next_own_three_upper_end_last_reduction.md);
it also follows directly by subtracting the last \(v\) of each
integral in (3).

**Proposition.** Under (1),
\[
E(1-v;y,z)\le L_0-\frac{v}{600},
\qquad 0\le v\le\frac15 .
\tag{6}
\]
The strict inequality holds when \(v>0\).
No assumption on the preceding quantum kernel enters this proposition.

## 2. A convex upper bound

Put \(a=11/50\) and \(r=41/50\). For \(0<r<1\), define
\[
G_r(x)=\int_0^x\log|1-r e^{2\pi is}|\,ds
=-\frac1{2\pi}\sum_{n=1}^{\infty}
                 \frac{r^n\sin(2\pi nx)}{n^2}.
\tag{7}
\]
The series follows by integrating the uniformly convergent
logarithmic series. In particular it has the same zero constant
as the integral.

For \(v\le1/5\), the incoming interval in (5) lies in
\([-1/5,11/50]\). The integrand is even and increases with distance
from zero there. Moving an interval of fixed length to have
midpoint zero minimizes its integral. The integrand also increases
with \(T\ge1\). Since \(T\ge50/41\), these facts imply
\[
\int_{q-v}^{q}\log|T-e^{2\pi is}|\,ds
\ge v\log(50/41)+2G_r(v/2).
\tag{8}
\]

For the outgoing interval, \(u-v\ge a-v>0\), and \(u\le9/20\).
The outgoing integrand increases on \([0,1/2]\). Moreover,
\[
|1-\rho e^{2\pi is}|^2
=(1-\rho)^2+4\rho\sin^2\pi s
\ge4\rho\sin^2\pi s .
\]
Move the interval to \([a-v,a]\) and use \(\rho\ge4/5\). This gives
\[
\int_{u-v}^{u}\log|1-\rho e^{2\pi is}|\,ds
\ge J(a)-J(a-v)+\frac v2\log(4/5).
\tag{9}
\]
Consequently \(\Phi(v)\le H(v)\), where
\[
H(v)=2J(v)+J(a-v)-J(a)-v\log(50/41)
                  -2G_r(v/2)-\frac v2\log(4/5).
\tag{10}
\]
In particular \(H(0)=0\).

The function \(H\) is strictly convex on \((0,1/5]\).
To see this, set \(T_0=50/41\) and \(\theta=\pi v\). Differentiation
of (10) gives
\[
H''(v)=2\pi\cot\theta+\pi\cot(\pi(a-v))
-\frac{\pi T_0\sin\theta}{T_0^2+1-2T_0\cos\theta}.
\tag{11}
\]
Since \(T_0^2+1-2T_0\cos\theta\ge2T_0(1-\cos\theta)\),
the last fraction is at most \((\pi/2)\cot(\theta/2)\).
Also
\[
2\cot\theta-\frac12\cot(\theta/2)
=\frac{3\cos\theta-1}{2\sin\theta}>0
\]
for \(0<\theta\le\pi/5\), and \(\cot(\pi(a-v))>0\).
This proves the assertion. The continuous extension at zero is convex
as well.

## 3. A strict endpoint estimate by rational inequalities

We prove
\[
H(1/5)<-\frac1{3000}.
\tag{12}
\]
All bounds below are exact written inequalities; no numerical
evaluation of the series or of a saved geometric root is used.

First, the Catalan-series estimate in
[the earlier sine-integral calculation, equations (18)--(20)](research_mixed_next_own_three_deep_radius_complete_central.md)
gives
\[
-J(1/4)>\frac{29}{200}.
\tag{13}
\]
This particular scalar inequality has no hypothesis on a geometric
radius. For completeness its witness is
\[
\sum_{k=0}^{\infty}\frac{(-1)^k}{(2k+1)^2}
>1-\frac19+\frac1{25}-\frac1{49}+\frac1{81}-\frac1{121}
>\frac{319}{350},
\]
together with \(-J(1/4)\) equal to this sum divided by \(2\pi\)
and \(\pi<22/7\).

The elementary radical formulas and \(20/9<\sqrt5<9/4\) give
\[
\frac7{12}<\sin(\pi/5)<\frac{59}{100},
\qquad
\frac{19}{20}<\sin(2\pi/5)<\frac{24}{25}.
\tag{14}
\]
For the lower bounds, squaring reduces the first to
\(\sqrt5<41/18\), and the second to \(\sqrt5>111/50\).
For the upper bounds it suffices respectively that
\(\sqrt5>2769/1250\) and \(\sqrt5<1483/625\).
All four follow from the stated rational bounds for \(\sqrt5\).

In particular \(2\sin(\pi/5)>7/6\). Since
\(\log x>2(x-1)/(x+1)\) for \(x>1\),
\[
J(1/4)-J(1/5)
\ge\frac1{20}\log(2\sin(\pi/5))
>\frac1{130}.
\]
Combining this with (13),
\[
J(1/5)<-\frac{29}{200}-\frac1{130}.
\tag{15}
\]
Also \(J(11/50)>J(1/5)\), since \(J'\) is positive on this interval.

At the other short endpoint, \(\sin\pi s\le\pi s\) gives
\[
J(1/50)\le\frac1{50}\{\log(\pi/25)-1\}<-\frac3{50}.
\tag{16}
\]
Here \(\pi/25<e^{-2}\): indeed \(e<11/4\), whence
\(e^2<121/16<175/22\), and \(\pi<22/7\).
One elementary witness for the bound on \(e\) is to sum through
degree three, obtaining \(8/3\), and bound the remaining exponential
series by \(5/96\). The resulting \(87/32\) is less than \(11/4\).

To bound the radial term, set
\[
\mathcal S=\sum_{n\ge1}\frac{r^n\sin(n\pi/5)}{n^2},
\qquad r=41/50.
\]
The first four terms are bounded above, in order, by
\[
\frac{121}{250},\quad \frac{81}{500},\quad
\frac3{50},\quad \frac{17}{1000},
\tag{17}
\]
using (14). Terms five and ten vanish. Terms six through nine
are negative. Retain the following lower bounds for the absolute
values of terms six, seven and eight:
\[
\frac3{625},\qquad \frac{23}{5000},\qquad \frac7{2500}.
\tag{18}
\]
For these bounds use \(r^3>11/20\), hence \(r^6>3/10\);
then \(r^7>6/25\) and \(r^8>19/100\). With (14), the respective
lower bounds before simplification are
\(7/1440\), \(57/12250\), and \(361/128000\), each greater than
its entry in (18). Drop term nine.

Finally,
\[
\sum_{n\ge11}\frac{r^n}{n^2}
\le\frac{r^{11}}{121(1-r)}<\frac2{363}<\frac3{500}.
\tag{19}
\]
For the strict middle bound, \(r^3<14/25\) and \(r^2<17/25\)
give \(r^{11}<46648/390625<3/25\).
Adding (17), the positive tail allowance in (19), and the
negative allowances in (18), yields
\[
\mathcal S<\frac{448}{625}.
\]
Since \(\pi>25/8\), equation (7) implies
\[
-2G_r(1/10)=\frac{\mathcal S}{\pi}<\frac{3584}{15625}.
\tag{20}
\]

The remaining logarithms satisfy
\[
\log(50/41)>\frac{18}{91},\qquad
\log(5/4)<\frac9{40}.
\tag{21}
\]
The first is the lower logarithmic bound already used.
The second follows from
\(\log x<(x^2-1)/(2x)\) for \(x>1\), obtained by the trapezoid
upper bound for the integral of the convex function \(1/t\).

Substitute (15)--(21) into (10). In this substitution,
\(2J(1/5)-J(11/50)<J(1/5)\) is essential. The result is
\[
\begin{split}
H(1/5)
&<\frac{3584}{15625}-\frac{73}{400}-\frac{43}{910}\\
&=-\frac{8571}{22750000}<-\frac1{3000}.
\end{split}
\tag{22}
\]
This proves (12). Convexity now puts \(H(v)\) below the chord
joining \(0\) to \(H(1/5)\):
\[
H(v)\le5vH(1/5)<-\frac v{600}\quad(0<v\le1/5).
\]
Together with (5)--(10), this proves (6).

## 4. Application to actual open words and its present limit

For an actual complete word in the original powers three and four,
beginning \(343\), of length \(m\ge5\), the third vertex is an
interior ordinary three. The first row of
[the open-word inheritance theorem](research_mixed_open_word_window_inheritance.md)
applies at \(j=3\) and gives
\[
-\frac3{100}<\Im z_*<\frac1{50}.
\]
Therefore its actual outgoing radius satisfies
\[
\rho=e^{2\pi\Im z_*}>e^{-3\pi/50}>\frac45.
\tag{23}
\]
For the final inequality,
\(3\pi/50<33/175<2/9<\log(5/4)\).
The prescribed real target coordinate can range over the whole
interval in (1), while its height remains this actual height.

The other geometric requirement \(R\le41/50\) is the first test of
[the saved-height protocol](research_mixed_cap_343_saved_height_protocol.md).
It has not been established by this analytic proof.
The argument does not apply the interior height theorem to a
length-four word, nor to a terminal \(343\) word.

Once its actual hypotheses hold, (6) bounds the small reflected
indices by their last rate before any preceding factor is attached.
The [shallower-strip reduction](research_mixed_next_own_three_shallow_upper_strip_reduction.md)
handles the complementary intermediate indices, and
[the correlated last-row transport](research_mixed_next_three_correlated_last_row_transport.md)
supplies the requisite preceding-factor comparison under its two
geometric hypotheses. Their finite-source assembly is a separate
implication. In particular this proposition by itself proves no
noncancellation statement for the complete signed quantum invariant.

