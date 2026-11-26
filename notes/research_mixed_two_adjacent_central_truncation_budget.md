# A central truncation whose error is below the outer critical rate

Research deduction, 7 November 2026. The complete physical inner
asymptotic has a relative error of order \(N^{-1}\). That error
cannot be carried through the oscillatory outer sum without
additional estimates. Here we instead discard a specified part of
the original finite sum and bound its absolute size below the
final complex critical rate.

The estimate applies to total indices \(2/3\le m/N\le4/5\), with
the two external parameters equal to \(x_0\). Every complementary
total index remains in the original sum. No numerical evaluation
is used.

## 1. Original quantities

Use the exact rows from
[the physical total-index theorem](research_mixed_two_adjacent_physical_total_index_packet.md):
\[
 T_{N,m,j}
 =\frac{r^{-j(m-j)}P_m p_j(X)p_{m-j}(X)}
              {P_j^2P_{m-j}^2},\qquad
 r=e^{-2\pi i/N},\quad X=e^{-2\pi ix_0}.
 \tag{1}
\]
Here \(0\le j\le m<N\), \(P_j=(r;r)_j\),
\(p_j(X)=(rX;r)_j\), and
\[
 x_0=\xi+i\upsilon,\qquad
 .18299<\xi<.18301,\qquad .07871<\upsilon<.07873.
 \tag{2}
\]
The full pair has the outside factor \(e^{2\pi i(N-1)x_0}\).
Its original inner and reduced phases are
\[
\begin{split}
 F_c(a)={}&g(c)+g(a+x_0)+g(c-a+x_0)
                 -2g(a)-2g(c-a)-2g(x_0)+2\pi ia(c-a),\\
 \phi(c)={}&F_c(c/2).
\end{split}
 \tag{3}
\]
The primitive and all its constants are those of the original
factorial. Let \(c_*=2a_*\), where \(a_*\) is the critical point
of the adjacent pair. Put
\[
 M=\Re\phi(c_*)-2\pi\upsilon,\qquad H_*=\Im c_*.
 \tag{4}
\]

## 2. The loss from the real maximum to the complex critical point

**Lemma 1.** The real function \(\Re\phi(c)\), \(0\le c\le1\),
has a unique maximum at a point \(c_0\in(2/3,4/5)\). Moreover,
\[
  \max_{0\le c\le1}\Re\phi(c)-\Re\phi(c_*)<\frac7{100}.
 \tag{5}
\]

*Proof.* The
[outer-phase theorem](research_mixed_two_adjacent_total_phase.md)
proves that \(\Re\phi'\) is positive on
\((0,1-2\xi]\), and strictly decreasing on
\([1-2\xi,1)\). Write \(S=|X|\), so
\(163/100<S<33/20\). Its exact multiplier is
\[
 e^{\phi'(c)}
  =\frac{(1+U)(1-XU)}{U(1-U)},\qquad U=e^{-\pi ic}.
 \tag{6}
\]
At \(c=2/3\), the square of its modulus is
\(|1-XU|^2/3>1\): indeed
\(\cos(2\pi(\xi+1/3))<0\) and \(1+S^2>3\).
At \(c=4/5\), its modulus is at most
\[
 \cot(2\pi/5)(1+S)<\frac13\frac{53}{20}<1,
 \tag{7}
\]
because \(\cot^2(2\pi/5)=1/(5+2\sqrt5)<1/9\).
The asserted unique maximum follows. The phase is continuous
at the real endpoints.

We first improve the upper bound on the height of \(c_*\).
The critical-corridor proof gives
\[
 \cot(\pi a_*)=u-iv,\qquad u>1/3,\quad 0<v<1/4.
\]
Solving for \(e^{2\pi ia_*}\) gives
\[
 \Im a_*=\frac1{4\pi}
       \log\frac{u^2+(1+v)^2}{u^2+(1-v)^2}
       <\frac1{4\pi}\log\frac{241}{97}
       <\frac{11}{48\pi}.
 \tag{8}
\]
For the first inequality the ratio decreases with \(u>0\)
and increases with \(v<\sqrt{1+u^2}\). For the second,
\[
 e^{11/12}>
 1+\frac{11}{12}+\frac{(11/12)^2}{2}
       +\frac{(11/12)^3}{6}+\frac{(11/12)^4}{24}
 =\frac{1241473}{497664}>\frac{241}{97}.
 \tag{9}
\]
Consequently \(0<H_*<11/(24\pi)\).

Throughout \(2/3\le c\le4/5\), \(0\le H\le H_*\), the
outer second derivative satisfies
\[
 \Re\phi''(c+iH)
 =\pi\Re\left\{-\csc\pi(c+iH)
       +\tfrac12\cot\pi((c+iH)/2+x_0)\right\}
 <-\frac9{10}\pi.
 \tag{10}
\]
Here the cotangent term is negative since its real argument
lies between \(1/2\) and \(1\). To check the cosecant bound, put
\(s=\sin\pi c\), \(C=\cosh\pi H\). Then
\[
 \Re\csc\pi(c+iH)=\frac{sC}{s^2+C^2-1}.
 \tag{11}
\]
We have
\(\sin(\pi/5)\le s\le\sqrt3/2\) and \(1\le C<9/8\).
The last bound follows from
\[
 \cosh(11/24)
 \le\frac1{1-(11/24)^2/2}
 =\frac{1152}{1031}<\frac98.
\]
On this rectangle, \(s^2>C^2-1\):
\(\sin^2(\pi/5)=(5-\sqrt5)/8>11/32>17/64\).
Expression (11) decreases with \(s\), and also with \(C\).
It is therefore at least
\[
 \frac{36\sqrt3}{65}>\frac9{10}.
 \tag{12}
\]
This proves (10).

At real \(c_0\), the original logarithms give
\[
 \Im\phi'(c_0)
 =\pi(c_0-\tfrac12)
       +\arg(1-Xe^{-\pi ic_0})
 <\pi(c_0/2-\xi)<\frac{2171}{10000}\pi.
 \tag{13}
\]
For the argument estimate, set \(t=c_0/2+\xi\in(1/2,1)\).
As the radius \(S\) increases from \(1\), the argument of
\(1-Se^{-2\pi it}\) decreases from \(\pi(1/2-t)\).
Its derivative in \(S\) is
\(\sin(2\pi t)/|1-Se^{-2\pi it}|^2<0\).

The real part of the phase on the segment \([0,1]+iH_*\)
is maximized at \(c_*\), by the outer-phase theorem. The
Cauchy--Riemann equations and (10)--(13) yield
\[
\begin{split}
 \Re\phi(c_0)-\Re\phi(c_*)
 &\le \Re\phi(c_0)-\Re\phi(c_0+iH_*)\\
 &=\int_0^{H_*}\Im\phi'(c_0+it)\,dt\\
 &<\frac{2171\pi}{10000}H_*-\frac{9\pi}{20}H_*^2.
\end{split}
 \tag{14}
\]
The last quadratic is increasing on
\([0,11/(24\pi)]\). At the right endpoint it equals
\[
 \frac{23881}{240000}-\frac{1089}{11520\pi}
 <\frac{23881}{240000}-\frac3{100}
 =\frac{16681}{240000}<\frac7{100}.
 \tag{15}
\]
The strict middle inequality uses \(\pi<22/7\).
This proves (5). \(\square\)

## 3. A stronger loss before discarding the inner tails

**Lemma 2.** For real \(2/3\le c\le4/5\), at either
\(a=c/2\pm1/5\),
\[
 \Re F_c(a)<\Re\phi(c)-\frac{16\pi}{625}
                         <\Re\phi(c)-\frac2{25}.
 \tag{16}
\]

*Proof.* Write \(s=c-a\) and suppose \(|a-c/2|\le1/5\).
Both \(a,s\) lie in \([2/15,3/5]\). The real second
derivative of (3) is
\[
 \Re F_c''(a)=\pi\Re\{\cot\pi(a+x_0)+\cot\pi(s+x_0)\}
                  -2\pi(\cot\pi a+\cot\pi s).
 \tag{17}
\]
The first pair has negative real part throughout this interval.
Indeed, with \(A=\pi(a+\xi)\), \(B=\pi(s+\xi)\) and
\(C=\cosh(2\pi\upsilon)\), the numerator of the sum of
their real parts, over positive denominators, is
\[
 2\sin(A+B)\{C\cos(A-B)-\cos(A+B)\}<0.
 \tag{18}
\]
Here \(1<c+2\xi<3/2\),
\(|a-s|\le2/5\), and hence the sine is negative,
the cosine of \(A+B\) is negative, and
\(\cos(A-B)>0\).

Also
\[
 \cot\pi a+\cot\pi s
 =\frac{\sin\pi c}{\sin\pi a\sin\pi s}
 \ge2\cot(\pi c/2)
 \ge2\cot(2\pi/5)>\frac{16}{25}.
 \tag{19}
\]
For the last inequality,
\(\cot^2(2\pi/5)=1/(5+2\sqrt5)>2/19>64/625\).
Thus \(\Re F_c''<-32\pi/25\).
Since \(F_c'(c/2)=0\) by exact symmetry, integration
over an interval of length \(1/5\) gives the first
inequality in (16). The second uses \(\pi>25/8\).
\(\square\)

## 4. An absolute error bound for the original discarded rows

**Theorem 3.** Let
\[
 \mathcal E_N=e^{2\pi i(N-1)x_0}
 \sum_{\substack{0\le m<N\\2/3\le m/N\le4/5}}
 \ \sum_{\substack{0\le j\le m\\|j-m/2|>N/5}}
                              T_{N,m,j}.
 \tag{20}
\]
There are constants \(C,b\), independent of \(N\), such that
\[
 |\mathcal E_N|\le C N^b e^{N(M-1/100)}.
 \tag{21}
\]
The same bound holds for the sum of the absolute values
of the discarded terms, including the outside factor.

*Proof.* The original physical row moduli increase toward
\(m/2\) and decrease afterward, as proved by the exact
consecutive-term ratios in the physical total-index theorem.
The first discarded row on either side lies within
\(1/N\) of \(a=c/2\pm1/5\).
These boundary arguments are in a fixed regular factorial
chart. Its row estimate, (16), and uniform continuity
therefore give
\[
 |T_{N,m,j}|
 \le C N^{-3/2}
       e^{N\{\Re\phi(m/N)-2/25\}}
 \tag{22}
\]
for every discarded row and all sufficiently large \(N\).
The strict margin between \(16\pi/625\) and \(2/25\)
absorbs the half-grid displacement and the uniform row error.
Unimodality extends this bound to the original endpoint rows;
no factorial expansion at those endpoints is required.

There are at most \(N^2\) discarded rows. The modulus of
the outside factor is \(e^{-2\pi(N-1)\upsilon}\).
By (5),
\[
 \Re\phi(m/N)-2\pi\upsilon-\frac2{25}
 <M+\frac7{100}-\frac8{100}
 =M-\frac1{100}.
 \tag{23}
\]
This proves (21). Finitely many smaller levels can be
absorbed in \(C\). Both parities are included. \(\square\)

The central sums can now be treated separately for even
and odd \(m\), with the centered lattice
\(\mathbb Z\) or \(\mathbb Z+1/2\), respectively.
At physical total indices they reproduce all retained
original rows exactly. An analytic interpolation of those
central sums need not reproduce the discarded rows away
from physical indices: their original total contribution
has already been bounded in (21).

## 5. The first half of the original total indices is smaller

The same cancellation budget also gives a direct estimate for
the original outer indices \(m/N\le1/2\).

**Theorem 4.** For constants \(C,b\) independent of \(N\),
\[
 \left|e^{2\pi i(N-1)x_0}\right|
 \sum_{0\le m\le N/2}\ \sum_{j=0}^m |T_{N,m,j}|
       \le C N^b e^{N(M-3/1000)}.
 \tag{24}
\]

*Proof.* We first prove
\[
 \Re\phi(c_0)-\Re\phi(1/2)>\frac{73}{1000}.
 \tag{25}
\]
For \(1/2\le c\le7/10\), the angle
\(\pi c+2\pi\xi\) lies between
\(\pi/2+2\pi\xi\) and \(3\pi/2-2\pi\xi\). Consequently
\[
 |1-Xe^{-\pi ic}|^2
 \ge1+S^2+2S\sin(2\pi\xi)
 >\frac{13247}{2000}.
 \tag{26}
\]
For \(1/2\le c\le2/3\), (6) therefore gives
\[
 \Re\phi'(c)>\tfrac12\log(11/5)>\frac{201}{512}.
 \tag{27}
\]
Here \(\cot(\pi c/2)\ge1/\sqrt3\), and
\[
 \log(11/5)=2\operatorname{atanh}(3/8)
 >2\left(\frac38+\frac{(3/8)^3}{3}\right)
 =\frac{201}{256}.
\]
For \(2/3\le c\le7/10\), use
\(\cot(\pi c/2)\ge\tan(3\pi/20)>1/2\). The last strict
inequality follows from
\[
 \tan(3\pi/20)>
 \frac{15}{32}+\frac13\left(\frac{15}{32}\right)^3
 =\frac{49455}{98304}>\frac12,
\]
using \(\pi>25/8\) and
\(\tan t>t+t^3/3\) for \(0<t<\pi/2\).
Together with (26) this gives
\[
 \Re\phi'(c)>\tfrac12\log(33/20)>\frac{13}{53}.
 \tag{28}
\]
For the logarithm bound use
\(\log z>2(z-1)/(z+1)\), \(z>1\).
In particular \(c_0>7/10\). Integrating (27)--(28) yields
\[
 \Re\phi(c_0)-\Re\phi(1/2)
 >\frac{67}{1024}+\frac{13}{1590}
 >\frac{73}{1000}.
 \tag{29}
\]

The real phase increases up to \(c_0\). Thus (5) and (29)
imply, for \(0\le c\le1/2\),
\[
 \Re\phi(c)-2\pi\upsilon<M-\frac3{1000}.
 \tag{30}
\]
This comparison applies to the complete physical row sums.
Indeed, the exact unimodality bounds every row by a central
row. The uniform physical factorial estimate
\(\log|P_j|=NJ(j/N)+O(\log N)\), including \(j=0\),
and the uniform estimate for \(p_j(X)\) give
\[
 \max_{0\le j\le m}|T_{N,m,j}|
          \le C N^b e^{N\Re\phi(m/N)}
                     \qquad(0\le m<N).
 \tag{31}
\]
These are the endpoint-safe estimates of
[the physical side-strip proof](research_mixed_two_adjacent_physical_end_strips.md).
Replacing the nearest central lattice point by \(m/(2N)\)
costs \(O(\log N)\) in the exponent, also as \(m/N\to0\);
this follows from the logarithmic endpoint singularity of
\(J'\). No regular expansion is asserted at \(m=0\).
Summing at most \(N^2\) rows in (31), and restoring the
outside factor, proves (24). \(\square\)

The remaining original total indices above \(1/2\) still
require their exact outer summation. In particular the interval
\((1/2,2/3)\) has not been discarded by the central truncation,
and an asymptotic for the central rows on \([2/3,4/5]\)
does not estimate that interval.
