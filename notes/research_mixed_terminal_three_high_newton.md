# The upper Newton indices of the terminal type-three sum

Research deduction, 5 November 2026. The exact reduction of the terminal
type-three polynomial permits a uniform estimate for every Newton index
at least half the level. The proof uses the original finite products,
convexity of the sine integral, and a scalar concavity estimate. It
retains ordinary-color derivatives, including the derivatives of rows
whose complete-color values vanish at odd levels. The lower Newton
indices remain a separate coherent sum.

## 1. The finite sum to be estimated

Use the conventions of the
[terminal Newton reduction](research_mixed_terminal_three_newton_reduction.md):
\[
\begin{gathered}
r=e^{-2\pi i/N},\qquad q=e^{\pi i/N},\qquad
P_j=(r;r)_j,\quad p_j(X)=(rX;r)_j,\\
S_j=|P_j|=\prod_{h=1}^j2\sin(\pi h/N),\\
e_l(w)=\frac{\prod_{h=0}^{l-1}
       (2\cos((2h+1)\pi/N)-w)}{S_l^2},\\
C_{1,N}(X,Y)=\sum_{i=0}^{N-1}
          \frac{X^{-i}p_i(X)p_i(Y)}{P_i^3}.
\end{gathered}
\tag{1}
\]
The exact terminal polynomial is
\[
\mathcal V_{0,N}(w,X)
 =N\sum_{l=0}^{N-1}\frac{(-q)^{-l}e_l(w)}{P_l}C_{1,N}(X,r^l).
\tag{2}
\]
Let \(\mathcal V^{\mathrm{high}}_{0,N}\) denote the same sum restricted
to \(l\ge\lceil N/2\rceil\). For every such \(l\), the inner sum
has the exact support \(0\le i<N-l\). This follows from the factor
\(p_i(r^l)\), independently of \(w\) and \(X\).

Our first estimate holds for
\[
X=e^{-2\pi ia},\qquad
a=y+ih\in[.22,.45]+i[-.12,.12].
\tag{3}
\]
Taking the absolute value of every term after expanding (2) gives its
positive double-sum majorant. No such triangle estimate is asserted
for the omitted lower Newton indices.

## 2. A uniform Newton upper rate, including ordinary colors

Write
\[
J(x)=\int_0^x\log(2\sin\pi s)\,ds,\qquad 0\le x\le1,
\quad L(x)=-J(x),\quad 0\le x\le\tfrac12.
\tag{4}
\]
The continuous endpoint values are used. We have
\(J(1-x)=-J(x)\), \(J(1/2)=0\), and \(L\ge0\) on
\([0,1/2]\). On its interior, \(J''(x)=\pi\cot\pi x>0\).

The complete-color Newton rate is
\[
E(u)=\int_0^u\log(4\cos^2\pi s)\,ds-2J(u).
\tag{5}
\]
In particular, on the upper half,
\[
E(u)=2J(u-1/2)-2J(u),\qquad 1/2\le u\le1.
\tag{6}
\]
Indeed the integral of \(\log(4\cos^2\pi s)\) over \([0,1/2]\)
is zero, and its remaining integral becomes \(2J(u-1/2)\).

**Lemma 1.** For every \(\eta>0\), there is a fixed \(\rho>0\)
such that, uniformly in \(0\le l<N\) and \(|w+2|\le\rho\),
\[
|e_l(w)|\le C N^A\exp\{N(E(l/N)+\eta)\}.
\tag{7}
\]
Every fixed ordinary-color derivative obeys the same upper rate on a
smaller fixed disk. Both parities of \(N\) are included.

*Proof.* Each numerator factor has modulus at most
\(4\cos^2(\pi(h+1/2)/N)+\rho\). For fixed positive \(\rho\),
the logarithm of this expression is a smooth function of the midpoint
index on \([0,1]\). Its partial Riemann sums converge to its integral
uniformly in their endpoint. As \(\rho\downarrow0\), the difference
between this logarithm and \(\log(4\cos^2\pi s)\) is nonnegative
and tends to zero in \(L^1[0,1]\). For example, dominated convergence
applies for \(0<\rho\le1\), since the latter logarithm has only an
integrable logarithmic singularity at \(1/2\). Hence the same integral
comparison is uniform in all partial endpoints.

The uniform sine-product estimate gives
\(\log S_l=NJ(l/N)+O(\log N)\), including \(l=0,N-1\).
For completeness, split \(\log(2\sin\pi s)\) at \(1/2\).
On each resulting monotone interval, upper and lower Riemann sums
differ only by endpoint terms. The values at \(1/N\) and \(1-1/N\)
and the integrals over the two omitted end cells have size
\(O(\log N)\) after multiplication by \(N\). This proves the
estimate uniformly in the partial endpoint \(l\).
Choose \(\rho\) and then \(N\) so that the two integral errors
use less than the prescribed \(\eta\). Division by \(S_l^2\)
proves (7); finitely many smaller levels are absorbed into \(C\).
Cauchy's formula on smaller color disks proves the derivative statement.
This argument does not divide by a Newton value and does not delete
any row that vanishes at the complete color. \(\square\)

## 3. Reducing the upper-half double sum to one real variable

Set \(u=l/N\), \(t=i/N\). The support of the upper-half sum is
\[
\tfrac12\le u<1,\qquad 0\le t<1-u.
\tag{8}
\]
Put
\[
I_a(t)=\int_0^t\log|1-e^{-2\pi i(a+s)}|\,ds.
\tag{9}
\]
The uniform zero-safe product upper estimate, the exact identity
\(p_i(r^l)=P_{i+l}/P_l\) on (8), and Lemma 1 give the double-row
upper rate, with any prescribed total positive tolerance,
\[
\begin{split}
R(u,t,a)={}&2J(u-1/2)+J(u+t)-4J(u)-3J(t)\\
          &+I_a(t)-2\pi ht.
\end{split}
\tag{10}
\]
There are no zero denominators: every factorial index is below \(N\).
All estimates are uniform up to the moving support wall. For the
nonphysical product in (9), replace its logarithm by
\(\tfrac12\log(|1-e^{-2\pi i(a+s)}|^2+\varepsilon^2)\).
For fixed \(\varepsilon>0\) this has uniformly convergent partial
Riemann sums on the target rectangle. Its integral decreases uniformly
to (9): away from the possible simple zeros the convergence is uniform,
and a neighborhood of length \(b\) around any zero has an integrated
logarithmic error tending uniformly to zero with \(b\). There are
only finitely many such neighborhoods in a period. Thus first choose
\(\varepsilon\), then the level, to obtain any prescribed upper-rate
tolerance. This is an upper estimate at zeros, with no relative
asymptotic or division by a zero. The factorial ratios in (10) use
the uniform estimate proved in Lemma 1. These are also the finite-source
estimates used for the
[terminal end tails](research_mixed_terminal_transform_tails.md).

Let \(v=1-u\). Then \(t\le v\le1/2\), and the first three
terms involving \(u\) in (10) equal
\[
-2L(1/2-v)+L(v-t)-4L(v).
\tag{11}
\]
Convexity of \(J\) on \([0,1/2]\) gives
\[
L(v-t)-L(v)=J(v)-J(v-t)
 \le J(1/2)-J(1/2-t)=L(1/2-t).
\tag{12}
\]
This follows by integrating the increasing function \(J'\) over two
intervals of equal length; endpoints follow by continuity. Since
\(L(v),L(1/2-v)\ge0\), (11) is at most \(L(1/2-t)\).

For the remaining product and chirp,
\[
\begin{split}
I_a(t)-2\pi ht
 &=\int_0^t\log|e^{-2\pi h}-e^{-2\pi i(y+s)}|\,ds\\
 &\le t\log(1+e^{.24\pi})=:ct.
\end{split}
\tag{13}
\]
Thus every row in (8) satisfies
\[
R(u,t,a)\le B(t):=L(1/2-t)+3L(t)+ct,
\qquad 0\le t\le1/2.
\tag{14}
\]
This comparison preserves the factor \(P_l^{-1}\) in (2) and all
three factors \(P_i^{-1}\) in the conditional kernel.

## 4. An exact scalar ceiling

**Lemma 2.** On \([0,1/2]\),
\[
\max B(t)<\frac{95458861}{108769600}<\frac{439}{500}=.878.
\tag{15}
\]

*Proof.* Direct differentiation in the interior gives
\[
B'(t)=\log(2\cos\pi t)-3\log(2\sin\pi t)+c,\qquad
-B''(t)=\pi(\tan\pi t+3\cot\pi t)\ge2\pi\sqrt3.
\tag{16}
\]
The quadratic supporting bound at \(t=1/4\) therefore gives
\[
\max B\le\frac{2G}{\pi}+\frac c4
                 +\frac{(c-\log2)^2}{4\pi\sqrt3},
\qquad
G=\sum_{j=0}^{\infty}\frac{(-1)^j}{(2j+1)^2}.
\tag{17}
\]
Here \(L(1/4)=G/(2\pi)\). One direct verification writes
\(G=\int_0^1(-\log x)/(1+x^2)\,dx
=-\int_0^{\pi/4}\log\tan s\,ds\).
The sum of the integrals of \(\log(2\sin s)\) and
\(\log(2\cos s)\) over this interval is zero by the double-angle
identity and \(J(1/2)=0\). Their difference gives the stated value
of \(L(1/4)\).

All constants in (17) have the following rational bounds:
\[
G<229/250,\quad c<57/50,\quad \log2>693/1000,\quad
\pi>157/50,\quad \sqrt3>433/250.
\tag{18}
\]
For \(G\), the alternating upper partial sum through \(j=100\)
is less than \(229/250\). For \(\log2\), the first four positive
terms of \(2\sum_{j\ge0}(1/3)^{2j+1}/(2j+1)\) suffice.
For \(c\), put \(x=(6/25)(22/7)=132/175\). The exact inequality
\[
1+\sum_{j=0}^{20}\frac{x^j}{j!}
       +\frac{x^{21}}{21!(1-x/22)}
 <\sum_{j=0}^{20}\frac{(57/50)^j}{j!}
\tag{19}
\]
proves \(1+e^{.24\pi}<e^{57/50}\).
The square of \(433/250\) is less than three.
Since \(c>\log2\), substituting (18) into (17) is legitimate.
The resulting rational upper bound is exactly the first fraction
in (15). \(\square\)

The accompanying
[rational checker](../experiments/check_mixed_terminal_three_high_newton_constants.py)
verifies these finite scalar inequalities. It performs no root search,
source evaluation, or parameter subdivision.

## 5. The finite bound and its geometric normalization

**Theorem 3.** On the target rectangle (3), there is a fixed ordinary
color disk about \(-2\) on which the positive double-sum majorant of
\(\mathcal V^{\mathrm{high}}_{0,N}\) is at most
\[
CN^A e^{879N/1000}.
\tag{20}
\]
Every fixed ordinary-color derivative of the polynomial has the same
bound on a smaller disk, for both parities of the level.

*Proof.* Use (10)--(15), with less than \(1/1000\) total rate
tolerance in the finite product and ordinary-color estimates.
There are at most \(N^2\) rows and the prefactor in (2) is \(N\).
They change only the polynomial prefactor. Cauchy's formula proves the
derivative assertion. \(\square\)

For its comparison with the geometric source, let \(a_*=A+ic_*\)
be an actual external reference of a terminal type-three block in an
open word of length at least two. Let \(\nu\in\{0,1\}\) be the
external type minus three, put \(d=y-A\), \(\kappa=1/2500000\),
and write \(\mathcal P_0\) for the optimized terminal action called
\(P_0(a)\) in the end-tail theorem. Its neighboring allocation is
\[
\Pi_{0,\nu}=\mathcal P_0-\nu g/2.
\tag{21}
\]
The end-tail theorem proves
\[
\Re\mathcal P_0(a_*)+\Re\mathcal P_0'(a_*)d-\kappa d^2>89/100,
\quad y\in[.22,.45].
\tag{22}
\]
When \(\nu=1\), the actual height \(c_*<0\), and its proof also
shows that the Fourier halfweight has rate \(-\Re g(y+ic_*)/2\).
Convexity of this real primitive places its negative below the
negative tangent at \(a_*\).

**Corollary 4.** On a sufficiently small fixed ordinary-color disk,
for every fixed derivative order \(j\),
\[
\begin{split}
&|\partial_w^j\mathcal V^{\mathrm{high}}_{0,N}
       (w,e^{-2\pi i(y+ic_*)})|\,
       |d_N(e^{-2\pi i(y+ic_*)})|^{\nu/2}\\
&\quad\le C_jN^{A_j}\exp N\left\{
 \Re\Pi_{0,\nu}(a_*)+\Re\Pi_{0,\nu}'(a_*)d
           -\kappa d^2-\frac1{100}\right\}.
\end{split}
\tag{23}
\]
Indeed (22) minus (20) leaves more than \(11/1000\).
The same halfweight comparison as in the end-tail theorem proves (23).
The bound remains true if the high-Newton sum is further restricted
to any subset of its inner indices, because (20) bounds its positive
double-sum majorant.

Combining this with the end-tail decomposition leaves, for type three,
only the exact finite region
\[
0\le l<\lceil N/2\rceil,\qquad
\delta<i/N<1-\delta,\qquad i+l<N
\tag{24}
\]
uncontrolled by these discarded-region bounds. To avoid double counting,
first remove the full terminal end tails and then remove the upper
Newton half only from the remaining middle-index sum. The latter
restriction is permitted by the positive majorant just proved.
The sum on (24) is kept coherent. Its nonzero full contribution, the
type-four analogue, and the ordinary knot-closure theorem remain open.
