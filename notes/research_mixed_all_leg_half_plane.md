# The sine lens and inverse-leg strip for every positive path power

Research lemma, 5 November 2026. On the original positive charge family
with all powers at least three and original incidence degree at most
two, every active vertex lies in both cosine and sine unit disks.
Consequently every inverse leg lies strictly in the lower half-plane.
The proof uses the full real and imaginary period equations. It does
not establish the adjacent-sum chamber or an action-to-volume identity.

## 1. Original geometric inputs

Use the finite path and charge cube of
[the positive path theorem](research_positive_path_fractional_charge_cube.md).
At an active vertex of power \(n\ge3\), write
\[
 \tau=a-iH,\qquad 0<a<\pi,\quad 0<H<23/20,
 \qquad r_j=k_j+ig_j,
 \qquad \chi\in(0,1].                                  \tag{1}
\]
There are at most two original incidences. Their returns are on the
original branches, with \(k_j>0\) and
\(-\pi/2<g_j<\pi/2\), and satisfy
\[
 \sum_j k_j=\frac{nH}{2},\qquad
 \sum_j g_j=\frac{na}{2}-\pi\chi,
 \qquad
 \sinh r_j=\tan(\tau/2)\cos(\tau_j/2).                 \tag{2}
\]
Complete neighbors have angle zero. The
[wire-order theorem](research_positive_path_real_wire_order.md)
proves \(|\cos(\tau_j/2)|\le1\), strictly below one at
active neighbors. The
[cosine phase maximum principle, Theorem 5](research_geometric_phase_maximum_principle.md#7-a-sharper-bound-for-the-maximum-cosine-phase)
proves
\[
 \beta_j:=\arg\cos(\tau_j/2)\ge0,\qquad
 \tan\beta_j<\frac1{\sqrt2},\qquad
 C:=\cosh H<\frac74.                                   \tag{3}
\]
These are already proved statements about the actual coupled family.

**Theorem 1.** Every active vertex in this family satisfies
\[
 \left|\sin\frac{\tau}{2}\right|<1,
 \qquad
 A=\cos^2(\tau/2):\quad |A|<1,\quad |1-A|<1.            \tag{4}
\]
For \(n\ge4\), this is
[the preceding sine-lens lemma](research_mixed_four_leg_half_plane.md#1-an-additional-lens-inequality-from-the-actual-periods).
It remains to prove (4) at \(n=3\).

## 2. A type-three lens failure confines both real returns

Suppose that \(n=3\) and the sine inequality fails. Put
\(c=\cos a\). The failure and the own-vertex phase bound give
\[
 c\le C-2,\qquad
 \tan^2\beta
 =\frac{(C-1)(1-c)}{(C+1)(1+c)}<\frac12,
 \qquad
 c>\frac{C-3}{3C-1}.                                   \tag{5}
\]
Their compatibility implies
\((C-1)(3C-5)>0\). Since \(C>1\),
\[
 C>\frac53,\qquad H>\log3,\qquad
 c>-\frac13,\qquad c< -\frac14,\qquad
 a>\frac\pi2+\arcsin\frac14.                           \tag{6}
\]
Here \((C-3)/(3C-1)\) is strictly increasing, and its value
at \(C=5/3\) is \(-1/3\). The other cosine bound uses
\(C<7/4\). In particular
\[
 |\tan(\tau/2)|^2=\frac{C-c}{C+c}<\frac32,              \tag{7}
\]
because \(c>-1/3>-C/5\).

Equation (2), the neighbor modulus bound, and
\(|\sinh(k+ig)|^2=\sinh^2k+\sin^2g\) imply
\[
 0<k_j<\operatorname{arsinh}\sqrt{3/2}<K:=\frac{21}{20}.
                                                               \tag{8}
\]
The last comparison is elementary: \(\sinh K>K+K^3/6\), and
\((K+K^3/6)^2-3/2=11492769/256000000>0\).
On the other hand the exact real period gives
\[
 S:=\sum_jk_j=\frac{3H}{2}>\frac{3\log3}{2}
                  >S_0:=\frac{13}{8}>K.                 \tag{9}
\]
For the logarithm bound, the first three positive terms of
\(\log3=2\operatorname{atanh}(1/2)\) sum to
\(263/240>13/12\). There must therefore be exactly two
actual incidences: a single return cannot satisfy (8)--(9).

## 3. Their negative arguments contradict the imaginary period

Set \(R=\sinh H/\sin a\). The lens failure gives
\[
 R^2\ge\frac{C+1}{3-C}>2.                               \tag{10}
\]
The argument of the product defining \(\sinh r_j\) is
\(-\arctan R+\beta_j<0\). By (3), its negative tangent is
strictly greater than
\[
 \frac{R-1/\sqrt2}{1+R/\sqrt2}
 >\frac1{2\sqrt2}>d:=\frac7{20}.                        \tag{11}
\]
On the original branch, \(-\pi/2<g_j<0\), and
\(\tan(-g_j)=\tanh k_j\tan(-\arg\sinh r_j)\).
Consequently
\[
 -g_j>f(k_j),\qquad f(k)=\arctan(d\tanh k).              \tag{12}
\]
This function is strictly increasing and concave for \(k>0\),
as is seen directly from
\[
 f''(k)=\frac{-2d(1+d^2)\tanh k\,\operatorname{sech}^2k}
                   {(1+d^2\tanh^2k)^2}<0.              \tag{13}
\]
For a fixed sum \(S\in(S_0,2K)\), the concave function
\(f(k)+f(S-k)\) on \([S-K,K]\) is bounded below by its
equal endpoint values. Using its monotonicity in the remaining
argument gives
\[
 \sum_j(-g_j)>f(K)+f(S-K)
                  >f(21/20)+f(23/40).                   \tag{14}
\]
No equal-return assumption is used.

The positive exponential series through degree four gives
\[
 \sum_{j=0}^4\frac{(21/10)^j}{j!}-7=\frac{52707}{80000}>0,
 \qquad
 \sum_{j=0}^4\frac{(23/20)^j}{j!}-3
                         =\frac{528401}{3840000}>0.      \tag{15}
\]
Thus \(\tanh(21/20)>3/4\) and \(\tanh(23/40)>1/2\).
Using \(\arctan x>x-x^3/3\) for \(x>0\),
\[
\begin{split}
 f(21/20)+f(23/40)
 &>\arctan(21/80)+\arctan(7/40)\\
 &>\frac{23}{56}+\frac{40793}{2150400}
 >\frac{23}{56}.                                       \tag{16}
\end{split}
\]
But the exact imaginary period and (6) give the opposite bound:
\[
 \sum_j(-g_j)=\pi\chi-\frac{3a}{2}
 <\frac\pi4-\frac32\arcsin\frac14
 <\frac{22}{28}-\frac38=\frac{23}{56}.                  \tag{17}
\]
Here \(\chi\le1\), \(\arcsin(1/4)>1/4\), and
\(\pi<22/7\). This contradiction proves Theorem 1.

## 4. Consequence for all inverse legs, and remaining scope

On an original edge write
\[
 q^2=A^{-1}+B^{-1}-1,\qquad
 U=\frac{-i}{2A(q+i)-i},\qquad
 s=\frac{i}{2\pi}\Log U,                               \tag{18}
\]
where \(A=\cos^2(\tau/2)\), \(B\) is the neighboring
cosine square, and \(q\) is the original root continued from
completeness.

**Corollary 2.** At every incidence of every selected vertex of power
\(n\ge3\), including a vertex of zero charge,
\[
                        \Im U<0,\qquad 0<\Re s<1/2.     \tag{19}
\]
The logarithm in (18) is continuous from its complete value and
is not reset during continuation.

Indeed the real-crossing proof of
[the inverse-leg half-plane theorem](research_mixed_four_leg_half_plane.md#2-excluding-every-real-crossing-of-an-inverse-leg)
uses only the own lens inequality \(|1-A|<1\) and the neighboring
condition \(\Im B\ge0\). Theorem 1 now supplies that lens at
type three as well. Along simultaneous charge scaling, the inverse
has no zeros or poles, starts at \(-1/5-2i/5\), and cannot cross
the real axis. At zero own charge, \(A=1\), \(q^2=B^{-1}\),
\(\Re q>0\), so (19) follows directly from the denominator
\(2q+i\).

This establishes the individual inverse-leg strip for every power.
It does not establish \(\Re(s+t)>1/2\) at vertex or shared pairs,
the endpoint wire-before-leg inequalities, or the full original
zero logarithmic lifts. The conditional lift tests in Section 3 of
the preceding note remain conditional on their additional ranges.
No finite-source estimate or action-to-volume identity follows
solely from (19). All estimates above are analytic or exact rational
comparisons; no root search or parameter cover is used.
