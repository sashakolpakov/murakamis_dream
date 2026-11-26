# Removing the inner tails throughout the remaining physical totals

Research deduction, 7 November 2026. The original adjacent-pair
sum can be reduced, with an exponentially smaller absolute error,
to total indices \(m/N>1/2\) and centered inner indices
\(|j-m/2|\le N/5\). The fixed centered cutoff is important:
all its factorial arguments remain in regular strips during
subsequent changes of the imaginary total parameter.

This is an estimate for the original physical rows. It does
not by itself evaluate their remaining outer sum. No numerical
evaluation is used.

## 1. Quantities and the previously established outer budget

Use the original \(T_{N,m,j}\), \(F_c(a)\), \(\phi(c)\),
\(x_0=\xi+i\upsilon\), and full critical rate
\[
 M=\Re\phi(c_*)-2\pi\upsilon
 \tag{1}
\]
from [the central truncation budget](research_mixed_two_adjacent_central_truncation_budget.md).
That note proves
\[
 \max_{0\le c\le1}\Re\phi(c)-\Re\phi(c_*)<7/100,
 \tag{2}
\]
and bounds the sum of the absolute values of all original
terms with \(m/N\le1/2\), including the outside factor,
by \(C N^b e^{N(M-3/1000)}\).

The elementary parameter bounds used here are
\[
 \xi>91/500,\quad \xi<19/100,\quad
 \sin(2\pi\xi)>91/100,\quad
 2/5<\cos(2\pi\xi)<41/100,\quad 2\pi\upsilon<1/2.
 \tag{3}
\]
They follow from the original output bounds retained in the
cited note and its critical-point sources. In particular
\[
 C_h:=\cosh(2\pi\upsilon)<8/7,
 \tag{4}
\]
using \(\cosh t\le(1-t^2/2)^{-1}\) for \(t^2<2\).

## 2. A uniform inner curvature bound

**Lemma 1.** Let \(1/2\le c\le1\) be real and
\(|a-c/2|\le1/5\). The second derivative in the inner
variable satisfies
\[
                     \Re F_c''(a)<-\frac{29\pi}{25}.
 \tag{5}
\]
At \(c=1\) this is the continuous value of the derivative
in \(a\); the term \(g(c)\) is independent of \(a\).

*Proof.* Set \(s=c-a\), so \(1/20\le a,s\le7/10\).
All four moving factorial arguments remain in regular strips.
The exact real derivative is
\[
 \Re F_c''(a)
 =\pi\Re\{\cot\pi(a+x_0)+\cot\pi(s+x_0)\}
                -2\pi(\cot\pi a+\cot\pi s).
 \tag{6}
\]

First suppose \(c<1-2\xi\). The shifted cotangent pair
has real part less than \(6/5\). To prove this, if both
shifted real arguments are less than \(1/2\), each is
greater than
\[
       c+2\xi-1/2\ge2\xi>1/3.
\]
Each real cotangent part is therefore less than
\(\cot(\pi/3)=1/\sqrt3\), and their sum is less than
\(2/\sqrt3<6/5\).
If one shifted real argument is at least \(1/2\), its
real cotangent part is nonpositive. The other argument
is greater than \(1/20+\xi>9/40\), and its real part
is at most the corresponding real cotangent. Thus the
pair is less than \(\cot(9\pi/40)<6/5\) in this case too.
For the last inequality,
\[
 \tan(9\pi/40)>
 \frac7{10}+\frac{(7/10)^3}{3}
                +\frac{2(7/10)^5}{15}>\frac56.
 \tag{7}
\]
Here \(9\pi/40>7/10\), and the displayed lower polynomial
follows by twice integrating \(\tan' t=1+\tan^2t\),
starting from \(\tan t>t\).

The ordinary cotangent pair obeys
\[
 2(\cot\pi a+\cot\pi s)
       \ge4\cot(\pi c/2)>4\tan(\pi\xi)>\frac52.
 \tag{8}
\]
Indeed \(\pi\xi>91/160\), and
\[
 \tan(\pi\xi)>
 \frac{91}{160}+\frac13\left(\frac{91}{160}\right)^3
 =\frac{7742371}{12288000}>\frac58.
 \tag{9}
\]
Equations (6)--(9) give
\(\Re F_c''<-13\pi/10<-29\pi/25\).

Now suppose \(c\ge1-2\xi\). Write
\[
 t_0=c/2+\xi,\quad k=\cos(2\pi t_0),\quad
 z=\cos(2\pi(a-c/2)).
\]
Then
\[
 -1\le k<-2/5,\qquad z\ge\cos(2\pi/5)>3/10.
 \tag{10}
\]
The sum of the two shifted real cotangents in (6) is
\[
 2\sin(2\pi t_0)\,
 \frac{C_hz-k}{C_h^2-2C_hkz+k^2+z^2-1}.
 \tag{11}
\]
Its denominator is the product of two positive cotangent
denominators. The derivative of the fraction in (11)
with respect to \(z\) has numerator
\[
 C_h(C_h^2-1-k^2-z^2)+2kz
 <\frac{22}{343}-\frac6{25}<0.
 \tag{12}
\]
For this estimate use (4), (10), and
\(C_h^2-1-k^2-z^2<15/49-1/4=11/196\).
Since \(\sin(2\pi t_0)\le0\), (11) is at most its
value at \(z=1\):
\[
 \Re\{\cot\pi(a+x_0)+\cot\pi(s+x_0)\}
       \le2\Re\cot\pi(c/2+x_0).
 \tag{13}
\]
At \(c=1-2\xi\), both sides of (13) are zero.
The ordinary cotangent sum is at least
\(2\cot(\pi c/2)\). Define
\[
 G(c)=4\cot(\pi c/2)-2\Re\cot\pi(c/2+x_0).
\]
On \(1/2\le c\le1\),
\[
 G'(c)=-2\pi\csc^2(\pi c/2)
                    +\pi\Re\csc^2\pi(c/2+x_0)<0.
 \tag{14}
\]
In fact \(\csc^2(\pi c/2)\ge1\), while
\(1/4<\Re(c/2+x_0)<3/4\) gives
\(|\csc^2\pi(c/2+x_0)|<2\). Consequently
\[
 G(c)\ge G(1)=2\Re\tan(\pi x_0)
 =\frac{2\sin(2\pi\xi)}{\cos(2\pi\xi)+C_h}
 >\frac{1274}{1087}>\frac{29}{25}.
 \tag{15}
\]
Combining (6), (13)--(15) proves (5).
\(\square\)

Exact symmetry gives \(F_c'(c/2)=0\). Integrating (5)
twice yields, at either \(a=c/2\pm1/5\),
\[
 \Re F_c(a)<\Re\phi(c)-\frac{29\pi}{1250}
                            <\Re\phi(c)-\frac9{125}.
 \tag{16}
\]
The second strict inequality already follows from
\(\pi>25/8\).

## 3. The complete discarded physical sum

**Theorem 2.** There are constants \(C,b\), independent of \(N\),
such that
\[
 \left|e^{2\pi i(N-1)x_0}\right|
 \sum_{\substack{N/2<m<N\\|j-m/2|>N/5\\0\le j\le m}}
        |T_{N,m,j}|
       \le C N^b e^{N(M-1/500)}.
 \tag{17}
\]

*Proof.* The exact finite unimodality from
[the physical inner theorem](research_mixed_two_adjacent_physical_total_index_packet.md)
controls every discarded row by the first one on its side
of the central cutoff. Its inner argument is within \(1/N\)
of one of the two boundary arguments in (16).
The moving inner arguments stay in fixed regular strips.
The possibly near-endpoint fixed factor \(P_m\) is controlled
by the uniform physical estimate
\(\log|P_m|=NJ(m/N)+O(\log N)\). Thus (16) gives
\[
 |T_{N,m,j}|
 \le C N^b e^{N\{\Re\phi(m/N)-9/125\}}
 \tag{18}
\]
for every discarded row and all sufficiently large \(N\),
uniformly even as \(m/N\to1\).
The strict margin in (16) absorbs the finite displacement
of the cutoff. No expansion at an original endpoint row
is required.

There are at most \(N^2\) rows. By (2),
\[
 \Re\phi(m/N)-2\pi\upsilon-\frac9{125}
 <M+\frac7{100}-\frac9{125}=M-\frac1{500}.
 \tag{19}
\]
The exact outside factor changes only the fixed prefactor
after the \(-2\pi\upsilon\) part has been included.
This proves (17). \(\square\)

Let \(\sigma(m)=0\) for even \(m\), and \(1/2\) for odd \(m\).
For the fixed central finite source
\[
 \mathcal H_{\sigma,N}(c,x_0)
  =\sum_{\substack{d\in\mathbb Z+\sigma\\|d|\le N/5}}
                 T_N(c/2+d/N;c,x_0,x_0),
 \tag{20}
\]
the original pair therefore satisfies
\[
 \boxed{\quad
 V_{22,N}(x_0,x_0)=e^{2\pi i(N-1)x_0}
     \sum_{N/2<m<N}\mathcal H_{\sigma(m),N}(m/N,x_0)
       +O\!\left(N^b e^{N(M-1/500)}\right).
 \quad}
 \tag{21}
\]
Theorem 2 pays the discarded inner rows, while Theorem 4
of the earlier budget pays all totals \(m/N\le1/2\).
Both are absolute bounds on original terms. Equation (21)
thus precedes, and does not assume, cancellation in the
remaining outer sum.

If a final interval of total indices near \(1\) is removed
using the original diagonal-strip bound, its absolute error
must also be retained. The remaining finite outer sum,
its two parity lattices, and its contour estimates still
require their own proof.

