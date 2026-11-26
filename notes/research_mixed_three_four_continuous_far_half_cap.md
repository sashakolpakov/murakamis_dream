# A continuous far-half cap bound and the closing seam connector

Research deduction, 7 November 2026. The first result bounds the whole
first cap on the real incoming half-circle, without using physical
termination away from a root. The second pays the complete ordinary
three/four source in a fixed two-sided complex neighborhood of its
closing seam. In particular it pays the final part of the specified
complementary contour. Neither result estimates the remaining middle
part of that contour. No numerical evaluation is used.

## 1. Exact source and uniform product bounds

Keep the original polynomials and scalar of
[the ordinary pair source](research_mixed_three_four_ordinary_pair_target.md):
\[
\begin{split}
 U_{0,N}(w,X)&=\sum_{j=0}^{N-1}
       \frac{H_N(w,r^{-j})p_j(X)}{P_j},\\
 V_{1,N}(w,X)&=\sum_{j=0}^{N-1}
       C_{1,N}(X,r^j)\frac{H_N(w,r^{-j})}{P_j},\\
 C_{1,N}(X,Y)&=\sum_{i=0}^{N-1}
       \frac{X^{-i}p_i(X)p_i(Y)}{P_i^3},\\
 Z_{34,N}&=\kappa_N^3N^2\int_0^1
       U_{0,N}(w_L,e^{-2\pi ia})V_{1,N}(w_R,e^{-2\pi ia})\,da .
\end{split}                                                     \tag{1}
\]
Here \(r=e^{-2\pi i/N}\), \(P_j=(r;r)_j\),
\(p_j(X)=(rX;r)_j\), and \(|\kappa_N|=1\). Every
\(H_N\) in (1) is its complete endpoint polynomial. None of
the sums in (1) is truncated by an off-grid support condition.

Let \(J\) denote the continuous one-periodic real primitive
with derivative \(\log(2|\sin\pi x|)\) and \(J(0)=0\).
For real \(x\) and \(0\le e\le1\), put
\[
 I_x(e)=J(x+e)-J(x).
                                                               \tag{2}
\]
The zero-safe finite-product upper bound gives, for every tolerance
\(\tau>0\),
\[
 |p_j(e^{-2\pi ix})|
 \le C_\tau N^{B_\tau}e^{N(I_x(j/N)+\tau)}.
                                                               \tag{3}
\]
It is uniform in both real variables, including a zero of the
product. The denominator has
\(\log|P_j|=NJ(j/N)+O(\log N)\) uniformly through both ends.
For (3), one may truncate the logarithmic factor from below,
apply uniform Riemann convergence to the truncated continuous
function, and then let the truncation error tend to zero. This
is exactly the upper-bound argument in
[the global transform-end theorem](research_mixed_three_four_global_transform_ends.md),
Lemma 1; it does not require a lower bound for a numerator.

The whole-index endpoint envelope from
[the endpoint polynomial theorem](research_mixed_endpoint_polynomial_collar.md),
equation (15), is
\[
 |\partial_w^k H_N(w,r^{-j})|
 \le C_{\tau,k}N^{B_{\tau,k}}
      e^{N\{J(e)+\lambda(e)+\tau\}},\qquad e=j/N,
 \quad \lambda(e)=\Re S(e).
                                                               \tag{4}
\]
It holds on a sufficiently small fixed ordinary-color disk about
\(-2\), for every fixed derivative order and both level parities.
The function \(J+\lambda\) is continuous on \([0,1]\), is
zero at both ends, and has its maximum at \(1/2\).

## 2. A real far-half comparison for every individual private row

**Lemma 1.** For \(1/2\le x\le1\),
\[
 I_x(e)\le
 \begin{cases}
   -J(1/2-e),&0\le e\le1/2,\\
   J(e),&1/2\le e\le1.
 \end{cases}                                                   \tag{5}
\]

*Proof.* For \(0<e<1\), away from the integrable zero,
\[
 \partial_x I_x(e)
       =\log\frac{|\sin\pi(x+e)|}{\sin\pi x}.
                                                               \tag{6}
\]
The squared numerator minus squared denominator is
\(\sin\pi e\,\sin\pi(2x+e)\). On \(x\in(1/2,1)\)
it is negative before \(x=1-e/2\) and positive after it.
Thus \(I_x(e)\) decreases and then increases: its sole interior
extremum is a minimum. Its maximum is at one of the two endpoints.
This reasoning extends across the zero by continuity of the integral.

At \(x=1\), its value is \(J(e)\). At \(x=1/2\), its
value is \(-J(1/2-e)\) below the half point and \(J(e-1/2)\)
above it. Since \(J\le0\) on \([0,1/2]\) and
\(J\ge0\) on \([1/2,1]\), the first endpoint is larger
above the half point and the second is larger below it. This proves
(5), including the boundary values. \(\square\)

The scalar bounds in
[the coherent seam theorem](research_mixed_cap_seam_source_bounds.md),
equations (5)--(7), give
\[
 \lambda(e)<433/500\quad(0<e\le1/2),\qquad
 \lambda(e)+J(e)\le\lambda(1/2)<101/125\quad(1/2\le e<1).
                                                               \tag{7}
\]
Also \(\max_{[0,1]}(-J)=-J(1/6)<1/6\): strict concavity
of sine gives \(2\sin\pi s>6s\) for \(0<s<1/6\),
and integration gives \(J(1/6)>-1/6\).

**Theorem 2.** For every \(\tau>0\), all sufficiently small
fixed ordinary-color disks, and each fixed ordinary derivative order,
\[
 \sup_{1/2\le x\le1}
 |\partial_w^kU_{0,N}(w,e^{-2\pi ix})|
 \le C_{\tau,k}N^{B_{\tau,k}}
         \exp N\left(\frac{1549}{1500}+\tau\right).
                                                               \tag{8}
\]

*Proof.* Multiply (3) and (4) and divide only by the nonzero
\(P_j\). The resulting rate is \(\lambda(e)+I_x(e)\).
For \(e\le1/2\), (5)--(7) bound it by
\(433/500+1/6=1549/1500\). For \(e\ge1/2\), they bound
it by \(101/125\). The whole-index estimate (4) includes both
ends; no compact coefficient packet is extrapolated there.
Summing all \(N\) physical private rows costs only a polynomial
factor. Divide the prescribed tolerance between the finite estimates.
The derivative assertion follows directly from (4).
\(\square\)

More precisely, the same proof retains the upper ceiling
\[
 B_{\mathrm{cont}}=
 \max\left\{\max_{0\le e\le1/2}
       [\lambda(e)-J(1/2-e)],\ \lambda(1/2)\right\}.
                                                               \tag{9}
\]
No value or favorable comparison for (9) is asserted here.
Unlike the smaller \(41/40\) ceiling in
[the physical far-half theorem](research_mixed_three_four_physical_far_half.md),
(8) is valid at every real point of the arc. Its proof does not
extend the terminating physical identity to such points. The bound
does not by itself include a nonzero incoming height.

## 3. The whole closing seam has a fixed complex neighborhood

For \(z\) near zero, define
\[
 K(z,t)=\int_0^t\log|1-e^{-2\pi i(z+s)}|\,ds,
 \qquad
 \omega(\rho)=\sup_{\substack{|z|\le\rho\\0\le t\le1}}
                        |K(z,t)-J(t)| .
                                                               \tag{10}
\]
The logarithmic singularity is locally integrable uniformly in its
radial and angular displacement. Hence \(K\) is continuous on
the compact product and
\(\omega(\rho)\longrightarrow0\) as \(\rho\downarrow0\).
One explicit justification is to remove a small arc around the
possible zero. On its complement the logarithm converges uniformly;
on the removed arc the integral of its absolute value is uniformly
\(O(\epsilon|\log\epsilon|)\), after a harmless fixed constant
multiple of the arc width. The same argument applies to every
partial integral in (10).

The truncated-log proof of (3) is uniform also for \(|z|\le\rho\).
It therefore gives
\[
 \frac{|p_i(e^{-2\pi iz})|}{|P_i|}
 \le C_\tau N^{B_\tau}
                 e^{N\{\omega(\rho)+\tau\}},\qquad i<N.
                                                               \tag{11}
\]
Every numerator zero is retained in this upper bound.

The original coherent coefficient sums obey
\[
 \sum_{j<N}|H_N(w,r^{-j})|\le C N^B e^{N(b_0+\tau)},\qquad
 \sum_{j<N}\frac{|H_N(w,r^{-j})|}{|P_j|}
                    \le C N^B e^{N(b_1+\tau)},
 \quad b_0=101/125,\ b_1=433/500.
                                                               \tag{12}
\]
These are the seam theorem with its exact normalization. The
all-period numerator bound and the scalar already used in
[the two-vertex collar proof](research_mixed_two_vertex_first_collar.md),
equations (3)--(7), are
\[
 |p_i(Y)|\le C N^B e^{NL(i/N)}\quad(|Y|=1),\qquad
 L(t)=-2J((1-t)/2),\qquad
 M_1(0)=\max_{[0,1]}[L(t)-2J(t)]<7/15.
                                                               \tag{13}
\]
For \(X=e^{-2\pi iz}\), the original chirp in (1) satisfies
\(|X^{-i}|\le e^{2\pi N\rho}\). Apply (11) to the incoming
numerator of \(C_1\), (13) to its other numerator, and (12)
only after retaining each complete endpoint coefficient. This gives
\[
 \begin{split}
 |U_{0,N}(w_L,X)|&\le C N^B
          e^{N\{b_0+\omega(\rho)+\tau/2\}},\\
 |V_{1,N}(w_R,X)|&\le C N^B
          e^{N\{b_1+M_1(0)+\omega(\rho)+2\pi\rho+\tau/2\}}.
 \end{split}                                                   \tag{14}
\]
Here \(\tau\) denotes a prescribed total allowance, after
dividing it between the finitely many source estimates.

The source ceiling at \(z=0\) is less than \(3211/1500\).
The unchanged original reference satisfies
\[
 M>9/4-147\pi/20000>22269/10000,
 \qquad 22269/10000-3211/1500>7/100.
                                                               \tag{15}
\]
Choose a fixed \(\rho>0\) so that
\(2\omega(\rho)+2\pi\rho<1/100\), and then choose the
total source/color tolerance below \(1/100\).

**Theorem 3.** On sufficiently small fixed ordinary-color disks,
\[
 |\partial_{w_L}^{k}\partial_{w_R}^{\ell}
       [U_{0,N}(w_L,e^{-2\pi ia})V_{1,N}(w_R,e^{-2\pi ia})]|
 \le C_{k,\ell}N^{B_{k,\ell}}e^{N(M-1/20)}
                    \qquad (|a-1|\le\rho).
                                                               \tag{16}
\]
The same conclusion holds near every integer incoming coordinate.
The disks and radius are fixed before the level tends to infinity.
The result includes every finite row, both level parities and all
fixed ordinary mixed derivatives. On a smaller incoming disk it
also holds for each fixed incoming derivative, by Cauchy's formula.

The undifferentiated bound is (14)--(15). Holomorphy on smaller
fixed color disks gives the ordinary derivatives; exact period one
gives the stated incoming center. There are no branch restrictions
on the finite Laurent polynomials away from \(X=0\), and the
small exponential-coordinate neighborhood stays away from it.

## 4. An actual paid part of the complementary contour

The complementary path in
[the first-half assembly](research_mixed_three_four_first_half_assembly.md)
is \(a_+(x)=x+2ic(1-x)\), \(1/2\le x\le1\), where
\(-.072<c<.021\). It satisfies
\[
 |a_+(x)-1|\le(1+2|c|)(1-x)<\frac{143}{125}(1-x).
                                                               \tag{17}
\]
Consequently, after taking
\(\epsilon\le125\rho/143\), its complete final segment
\(1-\epsilon\le x\le1\) satisfies (16). Its contribution,
including the original \(\kappa_N^3N^2\), has rate at most
\(M-1/20\) with a polynomial prefactor. Any fixed bounded-length
replacement connector contained in the same disk has the same bound.

This is a continuous-contour estimate, not an identification of a
partial root sum with an arc. The remaining path from \(1/2+ic\)
to this disk is still unestimated. In particular (8) and (16) do not
supply a whole ordinary pair packet, an outside-color loss, or a new
knot-family conclusion.
