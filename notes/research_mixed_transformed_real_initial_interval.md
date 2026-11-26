# The complete transformed source on the real initial interval

Research deduction, 7 November 2026. This bounds the entire conditional
sum after the final boundary has been fixed at a complex value. It
includes every row revived by that change. The estimate is uniform
on the closed outgoing unit disk and on the whole real ordinary-color
interval. No numerical evaluation is used.

## 1. The exact source

Use the notation and inverse-boundary normalization of
[the transformed complement](research_mixed_three_four_transformed_complement.md):
\[
\begin{split}
 r&=e^{-2\pi i/N},\qquad P_j=(r;r)_j,\qquad p_j(X)=(rX;r)_j,\\
 U_{0,N}(w,X)&=\sum_{j=0}^{N-1}H_N(w,r^{-j})p_j(X)/P_j,\\
 C_{1,N}(X,Y)&=\sum_{j=0}^{N-1}
                X^{-j}p_j(X)p_j(Y)/P_j^3,\\
 \mathfrak f_{[0,1/10],N}(w,Y)
   &=N\int_0^{1/10}
        U_{0,N}(w,e^{-2\pi ix})C_{1,N}(e^{-2\pi ix},Y)\,dx .
\end{split}                                                     \tag{1}
\]
The integral has the original incoming orientation. It is the specified
part of the retained-leg prefix, before the final Gram contraction.
There is no final halfweight or Fourier selection in (1).
Every coherent coefficient \(H_N\) remains whole.

**Theorem 1.** For every fixed pair of nonnegative derivative orders
\(k,\ell\), there are constants \(C_{k,\ell},B_{k,\ell}\) such that,
at all sufficiently large integer levels of either parity,
\[
\sup_{\substack{0\le x\le1/10\\w\in[-2,2],\ |Y|\le1}}
\left|\partial_w^k\partial_Y^\ell
  [U_{0,N}(w,e^{-2\pi ix})C_{1,N}(e^{-2\pi ix},Y)]\right|
\le C_{k,\ell}N^{B_{k,\ell}}e^{7N/4}.                    \tag{2}
\]
The same estimate holds on a sufficiently small fixed complex disk
about the complete color \(w=-2\), on a smaller disk for derivatives.
It also bounds (1), with a larger polynomial prefactor.

No physical termination in the incoming or outgoing variable is used.
In particular (2) includes the seam \(x=0\), both finite-index
endpoints, and every zero of a numerator polynomial.

## 2. A small-angle quotient bound for all physical indices

Let \(J\) be the continuous one-periodic primitive with
\(J'(u)=\log(2|\sin\pi u|)\), \(J(0)=0\), and put
\[
 L(x)=-2J((1-x)/2),\qquad A(x)=L(x)-J(x).
                                                               \tag{3}
\]
The uniform zero-safe product estimate in
[the continuous far-half cap proof](research_mixed_three_four_continuous_far_half_cap.md),
equations (2)--(3), and the uniform sine-factorial estimate give
\[
\frac{|p_j(e^{-2\pi ix})|}{|P_j|}
\le C_\tau N^{B_\tau}
 \exp N\{J(x+t)-J(x)-J(t)+\tau\},\qquad t=j/N.            \tag{4}
\]
The numerator needs only an upper estimate. Truncating its logarithm
from below before taking Riemann sums proves (4) uniformly through
its zeros. No lower estimate for that numerator is asserted.

For \(0<x\le1/10\), the derivative in \(t\) of the rate in (4)
is
\[
 \log\frac{|\sin\pi(x+t)|}{\sin\pi t}.
                                                               \tag{5}
\]
On \(0<t<1-x\) it changes sign from positive to negative at
\(t=(1-x)/2\). The maximum there is \(A(x)\).
For \(1-x\le t\le1\), periodicity gives
\[
 J(x+t)-J(x)-J(t)\le-J(x)\le A(x),
                                                               \tag{6}
\]
because \(x+t-1\in[0,x]\), \(J\le0\) on \([0,1/2]\),
and \(J(t)\ge0\) on this final interval. The assertion at \(x=0\)
follows either by continuity or from \(p_j(1)=P_j\).
Consequently
\[
 \max_{j<N}\frac{|p_j(e^{-2\pi ix})|}{|P_j|}
 \le C_\tau N^{B_\tau}e^{N(A(x)+\tau)}
                    \quad(0\le x\le1/10).               \tag{7}
\]

The function \(A\) is increasing on this interval, since
\[
 A'(x)=-\log(2\sin(\pi x/2))>0.
                                                               \tag{8}
\]
Moreover \(L(1/10)\le(1/10)\log2<7/100\).
Concavity of sine on \([0,1/6]\) gives \(2\sin\pi u>6u\)
for \(0<u\le1/10\). Hence
\[
 -J(1/10)<\frac1{10}\{1+\log(5/3)\}<\frac4{25}.
                                                               \tag{9}
\]
The last inequality follows from
\(e^{3/5}>1+3/5+(3/5)^2/2>5/3\).
Thus
\[
                         A(x)<23/100.                  \tag{10}
\]

## 3. Retain both complete finite sums

The whole coherent coefficient norm, including its all-real-color
extension in
[the terminal real-color theorem](research_mixed_terminal_real_color_decay.md),
Lemma 2, is
\[
 \sum_{j<N}|H_N(w,r^{-j})|
 \le C_\tau N^{B_\tau}e^{N(101/125+\tau)}.
                                                               \tag{11}
\]
The same bound on small complete-color disks is the original
[seam source theorem](research_mixed_cap_seam_source_bounds.md).
Equations (7) and (11) therefore give
\[
 |U_{0,N}(w,e^{-2\pi ix})|
 \le C_\tau N^{B_\tau}
            e^{N(101/125+A(x)+\tau)}.                   \tag{12}
\]
This uses a positive sum of moduli of coherent coefficients, without
replacing any one coefficient by its individual Newton terms.

The centered-arc numerator estimate and the polynomial maximum
principle give
\[
 \sup_{|Y|\le1}|p_j(Y)|
       \le C N^B e^{NL(j/N)}.
                                                               \tag{13}
\]
The scalar \(M_1(0)<7/15\), explicitly recorded in
[the two-vertex first-collar proof](research_mixed_two_vertex_first_collar.md),
equations (3)--(4), is
\[
 M_1(0)=\max_{0\le t\le1}\{L(t)-2J(t)\}<7/15.
                                                               \tag{14}
\]
Using the uniform denominator estimate at every index gives
\[
 \sup_{|Y|\le1}\sum_{j<N}\frac{|p_j(Y)|}{|P_j|^2}
       \le C_\tau N^{B_\tau}e^{N(7/15+\tau)}.            \tag{15}
\]
Since the incoming chirp has modulus one on the real interval,
the exact sum (1), followed by (7) and (15), yields
\[
 |C_{1,N}(e^{-2\pi ix},Y)|
 \le C_\tau N^{B_\tau}e^{N(A(x)+7/15+\tau)}.
                                                               \tag{16}
\]
In particular the two numerator factors are never assumed to have
simultaneous terminating support.

Combining (10), (12), and (16) proves the sharper limiting ceiling
\[
 \frac{101}{125}+\frac{46}{100}+\frac7{15}
       =\frac{1301}{750}<\frac74.                       \tag{17}
\]
Allocate the finite product tolerances below the strict difference
in (17). This proves the value assertion in (2).

For fixed ordinary derivatives apply Markov's inequality to each
polynomial \(H_N(w,r^{-j})\), of degree at most \(N-1\), before
the positive sum in (11). For outgoing derivatives each \(p_j\)
has degree at most \(N-1\). The polynomial growth estimate
\[
 \sup_{|Y|\le1+1/N}|p_j(Y)|
   \le(1+1/N)^{N-1}\sup_{|Y|\le1}|p_j(Y)|
   \le e\sup_{|Y|\le1}|p_j(Y)|
                                                               \tag{18}
\]
and Cauchy's formula on a radius \(1/N\) disk cost only fixed
powers of \(N\). Both arguments precede summation and therefore
retain zeros and the true finite-index endpoints. The small ordinary
complex-disk assertion instead uses the disk version of (11) and
Cauchy's formula there. This completes the proof of Theorem 1.

## 4. Comparison to the actual retained-leg action

The [calibrated transformed complement](research_mixed_three_four_transformed_complement_calibration.md)
uses the single frozen original six-variable enclosure to prove
\[
 |e^{-2\pi iz_*}|<5/6,\qquad
 \Re\mathcal P_{34}(-2,z_*)>181/100.
                                                               \tag{19}
\]
Here \(\mathcal P_{34}\) is the original prefix action before
the final Gram contraction, not the complete two-boundary action.
The explicit removed endpoint action is retained in that calibration.

**Corollary 2.** On a sufficiently small fixed neighborhood of
\((-2,z_*)\), the full normalized initial contribution (1) satisfies,
for every fixed \(k,\ell\),
\[
 \left|\partial_w^k\partial_z^\ell
  \left[e^{-N\mathcal P_{34}(w,z)}
   \mathfrak f_{[0,1/10],N}(w,e^{-2\pi iz})\right]\right|
       \le C_{k,\ell}e^{-N/20}.                         \tag{20}
\]

Indeed \(181/100-7/4=3/50>1/20\). Shrink the neighborhood
so that its outgoing variable stays in the unit disk and the action
retains a strict margin above \(7/4+1/20\).
The holomorphic value estimate and Cauchy's formula on a smaller
fixed neighborhood absorb all polynomial factors and give (20).

This pays one entire continuous segment of the original contour.
It neither identifies a partial sampled sum with that segment nor
estimates the incoming taper \([.1,.22]\). The remaining first-path
pieces and any later halfweights or Fourier sectors are still separate
parts of the exact retained-boundary assembly.
