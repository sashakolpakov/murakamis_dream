# The complete upper transform sector on a continuous far-half tube

Research deduction, 7 November 2026. All physical terminal transform
rows at or above the half index, multiplied by the whole first cap,
are exponentially smaller than the ordinary three/four reference on
the entire real far half-circle. The bound persists to a fixed thin
complex-height tube and retains every private endpoint coefficient.
It does not estimate the lower transform rows or the initial larger
height of the complementary contour. No numerical evaluation is used.

## 1. Keep the literal upper transform sector

Use the exact source and conventions of
[the ordinary pair](research_mixed_three_four_ordinary_pair_target.md).
For \(X=e^{-2\pi ia}\), define the positive majorant
\[
 \mathcal V_{\mathrm{hi},N}(w,X)
  =\sum_{i=\lceil N/2\rceil}^{N-1}
       \left|\frac{X^{-i}p_i(X)}{P_i^2}\right|
                         |U_{1,N}(w,r^i)|.
                                                               \tag{1}
\]
Each \(U_1(w,r^i)\) is its complete private and Newton source.
In particular (1) dominates the modulus of the corresponding signed
part of the original \(V_1\); it does not replace a coherent
terminal value by a single private row.

The source proof in
[the physical far-half theorem](research_mixed_three_four_physical_far_half.md),
equations (15)--(18), gives, uniformly for every physical
\(t=i/N\in[0,1)\),
\[
 |U_{1,N}(w,r^i)|
 \le C_\tau N^{B_\tau}
       e^{N\{b_1+L(t)-J(t)+\tau\}},
 \qquad b_1=433/500,\quad L(t)=-2J((1-t)/2).
                                                               \tag{2}
\]
For clarity, its exact physical source is
\[
 U_{1,N}(w,r^i)
  =\sum_{j=0}^{N-1-i}\frac{H_N(w,r^{-j})}{P_j}
                    \frac{P_{i+j}}{P_iP_j}.
                                                               \tag{3}
\]
The maximum of the quotient rate over \(0\le e\le1-t\)
is \(L(t)-J(t)\), attained at \(e=(1-t)/2\).
The remaining sum of complete coefficient moduli has ceiling
\(b_1\). Thus (2) includes both endpoint regimes and every zero
in the literal support. It uses only termination at the actual
physical transform index, which remains physical in (1).

## 2. An elementary scalar maximum on the upper half

**Lemma 1.** On \(1/2\le t\le1\),
\[
                    L(t)-2J(t)\le-2J(1/4)<73/250.
                                                               \tag{4}
\]

*Proof.* Put \(B(t)=L(t)-2J(t)\). In the open interval,
\[
 B'(t)=\log\frac{1}
                   {8\sin^2(\pi t/2)\cos(\pi t/2)}.
                                                               \tag{5}
\]
For \(\theta\in[\pi/4,\pi/2]\), the denominator
\(A(\theta)=8\sin^2\theta\cos\theta\) has derivative
\(8\sin\theta(2-3\sin^2\theta)\). It first increases
and then strictly decreases, starts at \(2\sqrt2>1\),
and ends at zero. It therefore crosses one exactly once on
its decreasing part. Equation (5) shows that \(B\) first
decreases and then increases. Its maximum is one of its endpoints.
Since
\(B(1/2)=-2J(1/4)>0\) and \(B(1)=0\), this proves
the first inequality. The second is the already accepted scalar
\(-4J(1/4)<73/125\), used in the cited physical far-half proof.
No new scalar evaluation is made. \(\square\)

## 3. Every real incoming point, including revived rows

For real \(x\in[1/2,1]\), the numerator rate is
\(I_x(t)=J(x+t)-J(x)\), with the periodic continuous primitive.
Lemma 1 of
[the continuous far-half cap theorem](research_mixed_three_four_continuous_far_half_cap.md)
proves
\[
                         I_x(t)\le J(t)\qquad(t\ge1/2).
                                                               \tag{6}
\]
It applies to every real \(x\), not only sampled roots.
The incoming chirp \(X^{-i}\) has modulus one at these points.
Combining (2), (6), and the uniform factorial/product upper bounds
gives the upper rate
\[
 b_1+L(t)-J(t)+I_x(t)-2J(t)
        \le b_1+L(t)-2J(t)
        <\frac{433}{500}+\frac{73}{250}
                                                               \tag{7}
\]
for every row in (1). In particular, rows which vanish at some
physical incoming roots but revive between those roots are still
present in this bound.

The same continuous-cap theorem bounds the whole first factor by
\(1549/1500\). Therefore
\[
 |U_{0,N}(w_L,e^{-2\pi ix})|
        \mathcal V_{\mathrm{hi},N}(w_R,e^{-2\pi ix})
 \le C_\tau N^{B_\tau}
       e^{N\{1643/750+\tau\}},\qquad 1/2\le x\le1,
                                                               \tag{8}
\]
where
\[
 \frac{1549}{1500}+\frac{433}{500}+\frac{73}{250}
          =\frac{1643}{750},\qquad
 \frac{22269}{10000}-\frac{1643}{750}
          =\frac{1087}{30000}>\frac1{30}.
                                                               \tag{9}
\]
The actual ordinary reference satisfies \(M>22269/10000\)
with its original action normalization, by the two-vertex collar
theorem. Thus (8) has a strict calibrated reserve before any source
tolerance is allocated.

## 4. Uniform continuation to a thin height tube

For real \(x\) and small real \(h\), write
\[
 I_{x+ih}(t)=\int_0^t
                  \log|1-e^{-2\pi i(x+ih+s)}|\,ds.
                                                               \tag{10}
\]
This is continuous jointly in \((x,h,t)\), including moving
logarithmic zeros. Consequently
\[
 \omega_1(\rho)=
 \sup_{\substack{1/2\le x\le1,\ |h|\le\rho\\0\le t\le1}}
            |I_{x+ih}(t)-I_x(t)|\longrightarrow0
                      \quad(\rho\downarrow0).
                                                               \tag{11}
\]
The zero-safe truncated-log Riemann proof is uniform on this
compact product, just as in the preceding continuous-cap theorem.
In the complete first cap it adds at most \(\omega_1(\rho)\)
to every private row. In (1) it adds at most
\(\omega_1(\rho)+2\pi\rho\), the second term retaining
the original \(X^{-i}\) chirp. All private factors in (2)
remain at their original physical transform values.

Choose a fixed \(\rho>0\) and then the total finite-source/color
tolerance so that
\[
                 2\omega_1(\rho)+2\pi\rho+\tau<1/120.
                                                               \tag{12}
\]
Equations (8)--(12) prove:

**Theorem 2.** On sufficiently small fixed ordinary-color disks,
\[
 |U_{0,N}(w_L,e^{-2\pi i(x+ih)})|
       \mathcal V_{\mathrm{hi},N}(w_R,e^{-2\pi i(x+ih)})
 \le C N^B e^{N(M-1/40)}
       \quad(1/2\le x\le1,\ |h|\le\rho).
                                                               \tag{13}
\]
Every fixed pair of ordinary derivatives has the same positive-row
estimate on smaller disks, with its own polynomial prefactor.
Both parity cases are included, with the original half row assigned
by the ceiling in (1).

For the derivative statement, apply the uniform coefficient bounds
to the complete \(U_1(w,r^i)\) on a slightly larger color disk,
and use Cauchy's formula row by row. The first factor is likewise
whole. No derivative of an incomplete Newton sub-sum is required.

After restoring the original \(\kappa_N^3N^2\), (13) pays
this complete transform sector on any fixed bounded-length incoming
contour in the tube. The lower transform sector \(i<N/2\) is
not estimated here. Nor is the connector from \(1/2+ic\)
to the thin tube, unless it is supplied with a separate valid bound.
Thus this is a full-source sector estimate on an actual continuous
contour, not a whole complementary-contour or knot-family theorem.
