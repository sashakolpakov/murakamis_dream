# A whole first-cap bound on the nonpositive-height far half

Research deduction, 7 November 2026. The continuous real far-half
bound for the complete type-three cap extends to every nonpositive
incoming height in a fixed compact range. The proof compares its
original finite rows through their zero-safe product integrals; it
does not assert monotonicity of the signed cap value. No numerical
evaluation is used.

## 1. Exact endpoint comparison at any radius

For \(R>0\), let
\[
 f_R(x)=\log|1-Re^{-2\pi ix}|,\qquad
 I_{x,R}(e)=\int_0^e f_R(x+s)\,ds,
             \quad 0\le e\le1.
                                                               \tag{1}
\]
The integrals are continuous through the logarithmic zeros when
\(R=1\). Fix \(e\in(0,1)\). Away from those zeros,
\[
 \partial_x I_{x,R}(e)
       =\log\frac{|1-Re^{-2\pi i(x+e)}|}
                       {|1-Re^{-2\pi ix}|}.
                                                               \tag{2}
\]
The squared numerator minus squared denominator is
\(4R\sin\pi e\sin\pi(2x+e)\). Thus on
\(1/2\le x\le1\), the integral first decreases and then
increases, with its minimum at \(x=1-e/2\). Its maximum is
at one of the two endpoints, independently of the radius.

To compare those endpoints, put
\[
 D_R(e)=I_{1/2,R}(e)-I_{0,R}(e).
                                                               \tag{3}
\]
Its derivative is the logarithm of
\(|1+Re^{-2\pi ie}|/|1-Re^{-2\pi ie}|\), whose sign is
the sign of \(\cos2\pi e\). Also \(D_R(0)=D_R(1/2)=0\):
the two half-period integrals agree by the reflection
\(x\mapsto1-x\) and periodicity. Consequently \(D_R(e)\ge0\)
on \([0,1/2]\). The identity
\(D_R(e+1/2)=-D_R(e)\) gives the reverse sign on the other
half. Hence
\[
 I_{x,R}(e)\le
 \begin{cases}
 I_{1/2,R}(e),&0\le e\le1/2,\\
 I_{0,R}(e),&1/2\le e\le1,
 \end{cases}
                  \qquad 1/2\le x\le1.
                                                               \tag{4}
\]
The proof applies at \(R=1\) by integration and continuity,
without division by a vanishing product.

## 2. Both selected endpoints increase with radius below one

Suppose \(0<R<1\), and use the Poisson kernel
\[
 \mathcal P_R(x)=\frac{1-R^2}{1-2R\cos2\pi x+R^2},
 \qquad R\partial_R f_R(x)=\frac{1-\mathcal P_R(x)}2.
                                                               \tag{5}
\]
The kernel increases on \([1/2,1]\), and its integral over
that half-period is \(1/2\). For \(0\le e\le1/2\),
the function
\[
 G_R(e)=e-\int_{1/2}^{1/2+e}\mathcal P_R(x)\,dx
                                                               \tag{6}
\]
is concave, with \(G_R(0)=G_R(1/2)=0\). It is therefore
nonnegative. Equations (5)--(6) imply
\[
                  R\partial_R I_{1/2,R}(e)=G_R(e)/2\ge0.
                                                               \tag{7}
\]
The mean of \(f_R\) over a whole period is zero, by the
convergent logarithm series, and each of its two half-period
integrals is zero by reflection. Thus, for \(e\ge1/2\),
\[
                   I_{0,R}(e)=I_{1/2,R}(e-1/2).
                                                               \tag{8}
\]
Its radius derivative has the same sign. Taking \(R\uparrow1\)
in (7)--(8), using continuity of the integrals, proves
\[
 I_{x,R}(e)\le
 \begin{cases}
  -J(1/2-e),&0\le e\le1/2,\\
  J(e),&1/2\le e\le1,
 \end{cases}
        \qquad 0<R\le1,\quad 1/2\le x\le1.
                                                               \tag{9}
\]
For \(R\ge1\), the exact factor identity gives
\[
                  I_{x,R}(e)=e\log R+I_{x,R^{-1}}(e).
                                                               \tag{10}
\]
The same two endpoint ceilings consequently hold after adding
\(e\log R\le\log R\).

## 3. The complete finite cap and its actual source scope

Keep
\[
 U_{0,N}(w,X)=\sum_{j=0}^{N-1}
                 \frac{H_N(w,r^{-j})p_j(X)}{P_j},
 \qquad X=e^{-2\pi i(x+ih)},\quad R=e^{2\pi h}.
                                                               \tag{11}
\]
Every \(H_N\) is its whole endpoint polynomial. The
[continuous far-half theorem](research_mixed_three_four_continuous_far_half_cap.md),
Section 1, combines the whole-index endpoint bound with the uniform
finite-product upper bound to give the rate
\(\lambda(e)+I_{x,R}(e)\) for its physical private row
\(e=j/N\). That argument remains uniform when \(R\) ranges
over any fixed compact positive interval. In particular all revived
off-grid numerator rows, both private ends and both level parities
are retained.

Using (9)--(10) in precisely that source estimate proves:

**Theorem 1.** Fix \(H>0\). For every tolerance \(\tau>0\),
there is a fixed ordinary-color disk about \(-2\) on which every
fixed ordinary derivative satisfies
\[
 |\partial_w^kU_{0,N}(w,e^{-2\pi i(x+ih)})|
 \le C_{\tau,k,H}N^{B_{\tau,k,H}}
       \exp N\left\{\frac{1549}{1500}+2\pi h_++\tau\right\},
 \quad \frac12\le x\le1,\quad |h|\le H.
                                                               \tag{12}
\]
Here \(h_+=\max(h,0)\). More sharply, \(1549/1500\)
can be replaced by the unchanged explicit upper envelope
\[
 \max\left\{\max_{0\le e\le1/2}
       [\lambda(e)-J(1/2-e)],\ \lambda(1/2)\right\}
                                                               \tag{13}
\]
from that theorem. No new value or calibrated comparison for (13)
is asserted.

The proof uses (9), the old scalar ceilings
\(\lambda(e)<433/500\), \(\max(-J)<1/6\), and
\(\max(\lambda+J)<101/125\), followed by the sum of all
private row bounds. Fixed ordinary derivatives use the same
whole-coefficient estimate, or Cauchy's formula on smaller color
disks. No cancellation inside any \(H_N\) is replaced by a
partial Newton sum.

Thus the first factor has no additional height cost on the entire
nonpositive-height part of the actual complementary contour.
This is an upper estimate for the whole factor, not a proof that
its signed value increases with radius. The terminal factor still
contains its original \(X^{-i}\) chirp; its upper rows and lower
rows require their own comparisons. In particular (12) alone does
not pay the initial connector or the middle complementary contour.
