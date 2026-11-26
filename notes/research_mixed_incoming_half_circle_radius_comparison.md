# Incoming-angle comparison at any fixed circle radius

Research deduction, 7 November 2026. The real incoming-angle
comparison in
[the half-row reduction](research_mixed_right_pair_raw_reduction.md)
extends to every positive circle radius. It is an upper bound
for the original finite numerator factors, including their zeros.
It does not transfer cancellation from one angle to another.

## 1. The integrated numerator

For \(R>0\), define the one-periodic, integrable function
\[
 f_R(s)=\log|1-Re^{-2\pi is}|
       =\tfrac12\log\{(1-R)^2+4R\sin^2\pi s\}.
\]
At \(R=1\), its values at integers are understood as logarithmic
singularities. Put
\[
                    I_R(x,t)=\int_0^t f_R(x+s)\,ds,
                       \qquad 0\le t\le1.
 \tag{1}
\]
This is the absolute exponential rate of
\(p_i(X)=(rX;r)_i\), where
\(r=e^{-2\pi i/N}\), \(X=Re^{-2\pi ix}\), and \(t=i/N\).

**Proposition 1.** For \(1/2\le x\le1\) and
\(0\le t\le1/2\),
\[
                       I_R(x,t)\le I_R(1/2,t).
 \tag{2}
\]
For \(0<t\le1/2\), the inequality is strict when
\(1/2<x<1\). At \(x=1\) it is strict for \(0<t<1/2\);
at \(t=1/2\), the two endpoint values agree.

*Proof.* At every nonsingular point,
\[
 \partial_x I_R(x,t)=f_R(x+t)-f_R(x).
\]
Its sign is the sign of
\[
 \sin^2\pi(x+t)-\sin^2\pi x
                  =\sin\pi t\,\sin\pi(2x+t).
 \tag{3}
\]
For \(0<t\le1/2\), it is negative on
\((1/2,1-t/2)\) and positive on \((1-t/2,1)\).
The same monotonicity follows by integration at \(R=1\);
the logarithmic singularities are integrable. Hence the
maximum on the closed interval is at one of its endpoints.

Let \(D_R(t)=I_R(1/2,t)-I_R(1,t)\).
Its derivative is positive for \(0<t<1/4\) and negative
for \(1/4<t<1/2\), because it is
\(f_R(1/2+t)-f_R(t)\). Reflection and periodicity give
\(D_R(0)=D_R(1/2)=0\). Thus \(D_R(t)>0\) in between.
This compares the two endpoint values and proves all
the assertions. \(\square\)

The strict comparison is uniform away from the endpoints.
If \(0<R_-\le R\le R_+<\infty\),
\(0<\tau\le t\le1/2\), and
\(1/2+\delta\le x\le1-\delta\), with \(0<\delta<1/4\),
then
\[
                    I_R(x,t)\le I_R(1/2,t)-\gamma
 \tag{4}
\]
for some \(\gamma>0\) depending only on these compact
ranges. Indeed \(I_R\) is jointly continuous, including
at \(R=1\). To see continuity there, the logarithmic
singularity has a uniform integrable bound on a period;
dominated convergence in \(R\), followed by continuity
of translations in \(L^1\), suffices. Compactness and the
strict part of Proposition 1 then give (4).

## 2. The actual finite products, without division at a zero

**Lemma 2.** For \(R\in[R_-,R_+]\), all real \(x\),
\(0\le i<N\), and \(N\ge2\),
\[
 \log|p_i(Re^{-2\pi ix})|
             \le N I_R(x,i/N)+C\log(N+1),
 \tag{5}
\]
with a uniform constant. A zero product satisfies the
inequality with left side \(-\infty\).

*Proof.* Divide the interval \([x,x+i/N]\) into its
\(i\) cells of length \(1/N\), using right endpoint
samples. Exclude the bounded number of cells which
meet the distance-\(1/N\) neighborhood of an integer.
On every other cell,
\[
                        |f_R'(s)|\le\pi|\cot\pi s|.
\]
The sum of the sample-minus-integral errors is therefore
bounded above in absolute value by the integral of this
derivative bound away from those neighborhoods, which
is \(O(\log(N+1))\).

For an excluded cell, its sample is bounded above by
\(\log(1+R_+)\), unless it is \(-\infty\), when the desired
upper estimate is immediate. Its integral is bounded
below using
\[
 f_R(s)\ge \log(2\sqrt{R_-})+\log|\sin\pi s|.
\]
The integral of the last logarithm over a cell within
\(O(N^{-1})\) of an integer, multiplied by \(N\), is
bounded below by \(-C\log(N+1)\). There are only a
bounded number of such cells. Adding all the estimates
proves (5). No lower bound at a sampled zero is used.
\(\square\)

Combining (2) and (5), for \(i\le N/2\),
\[
 |p_i(Re^{-2\pi ix})|
 \le (N+1)^C\exp\{N I_R(1/2,i/N)\},
                  \qquad 1/2\le x\le1.
 \tag{6}
\]
For indices \(\tau N\le i\le N/2\) and angles as in
(4), the right side has the extra factor \(e^{-N\gamma}\).
The statement is uniform at both level parities. It
compares rates, not finite products at two angles:
the reference finite product at \(x=1/2\) can itself
vanish.

## 3. Use for an original physical row sum

Let \(c_{i,N}\) be any prescribed coefficients independent
of \(x\), and let \(\sigma\) be a fixed integer. For
\[
 B_N(X)=\sum_{i=0}^{\lfloor N/2\rfloor}
                         c_{i,N}X^{-\sigma i}p_i(X),
\]
equation (6) gives
\[
 |B_N(Re^{-2\pi ix})|
 \le (N+1)^C
       \sum_{i=0}^{\lfloor N/2\rfloor}
       |c_{i,N}|
       \exp\{N I_R(1/2,i/N)-\sigma i\log R\}.
 \tag{7}
\]
If the coefficient indices are restricted as in (4),
the same extra strict exponential factor applies.
Keeping the complete coherent inner coefficient inside
\(c_{i,N}\) is permitted; taking its absolute value then
occurs only at the explicitly displayed outer summation.

For example, the lower transform rows of the actual
terminal-four polynomial have
\[
 c_{i,N}=\frac{U_{1,N}(w,r^i)}{P_i^2},\qquad \sigma=1,
 \quad
 V_{1,N}(w,X)=\sum_{i<N}c_{i,N}X^{-i}p_i(X),
 \quad P_i=(r;r)_i .
 \tag{8}
\]
Thus (7) bounds its lower-index part on the right
semicircle at any bounded fixed incoming height.
It includes every term of that part and retains the
whole inner cap.

The upper physical rows in the
[type-three](research_mixed_terminal_three_right_triangle.md)
and [type-four](research_mixed_terminal_four_right_triangle.md)
entropy reductions also admit arbitrary real incoming
angle \(x\). In those proofs the only bound involving
that angle is
\[
 \partial_t\{I_R(x,t)-t\log R\}
          \le\log(1+R^{-1}).
\]
For \(|\log R|\le .24\pi\), it is bounded by the same
\(\log(63/20)<\log4\). Their entropy maximizers and
their derivative estimates do not involve \(x\).
Consequently the upper-row transport to \(t=1/2\)
continues to hold on the entire incoming circle, as
a zero-safe positive row bound. No claim about a
continued holomorphic phase at a product divisor is
required for this extension.

Neither (7) nor this upper-row extension supplies the
needed geometric comparison at the incoming half face.
In particular they cannot replace the right side of
(7) by the modulus of the coherent value \(B_N(-R)\).
That replacement would discard cancellation. To use
these bounds for the ordinary \((3,4)\) remainder, the
resulting half-face majorant must still be compared
with its actual coupled action. The already proved
coherent supporting plane at that angle is a different
bound and does not imply this comparison.

