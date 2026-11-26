# A sharper geometric rate and the far-right closing connection

Private written deduction, 9 November 2026. The horizontal maximum
of the original closing phase gives a stronger lower bound for its
geometric rate. Together with the complete Newton-vector estimate,
this bounds a far-right connection of the original contour. The
intermediate connection from the end of the middle segment is
still to be estimated.

No mathematical numerical evaluation, saved-value arithmetic,
import, compilation, test or frozen-source edit is used.

## 1. The original geometric rate

Retain the original stationary inner action \(S(u)\), its constant,
and the closing phase
\[
 \Xi(u)=2S(u)+iu^2/\pi-iu,\qquad
 u_g=\beta_g-iK_g,\qquad M_g=\Re\Xi(u_g).
 \tag{1}
\]
The adopted height theorem gives
\(0<\beta_g<\pi/2\) and \(17/30<K_g<7/10\).
The horizontal comparison, on this actual height, says
\[
 \Re\Xi(a-iK_g)
 \le M_g-\frac{(a-\beta_g)^2}{8\pi},
                 \qquad 0\le a\le\pi/2.
 \tag{2}
\]
At \(u=\pi/2-iK_g\), the real parts of \(iu^2/\pi\) and
\(-iu\) are \(K_g\) and \(-K_g\), respectively. Consequently
\[
 \Re\Xi(\pi/2-iK_g)=2\Re S(\pi/2-iK_g).
 \tag{3}
\]
The original lower-rectangle action bound is
\(\Re S(u)>321/200\) for
\(0\le\Re u\le\pi/2,\ -7/10\le\Im u\le0\).
Using this bound at the point in (3), then (2), proves
\[
 \boxed{\quad
 M_g>
 \frac{321}{100}
 +\frac{(\pi/2-\beta_g)^2}{8\pi}
 >\frac{321}{100}.
 \quad}
 \tag{4}
\]
This comparison uses the original calibrated action. It neither
changes a phase constant nor substitutes a different geometric
point. The weaker bound \(307/100\) remains valid but is unnecessary
for the estimates below.

## 2. Complete finite functions and the path

Use the exact functions of the two-current closing identity:
\[
 \begin{split}
 Q_N(w,u)&=\mathbf e(-2\cos u)^T J_NM_N^3\mathbf e(w),\\
 F_N(u;\mathbf w)&=Q_N(w_L,u)Q_N(w_R,u),\\
 G_N(u;\mathbf w)&=\sin u\,F_N(u;\mathbf w)e^{iNu^2/\pi},\\
 W_N(u)&=\frac{e^{-iNu}}{(1-\eta_Ne^{-iNu})^2},
       \qquad \eta_N=(-1)^{N-1},\\
 C_{N,4}&=e^{\pi i(N-1)^2/N},\qquad |C_{N,4}|=1.
 \end{split}
 \tag{5}
\]
Here \(M_N\) is the complete crossing matrix, \(J_N\) is
coefficient reversal, and \(\mathbf e(w)\) is the vector of
all \(N\) Newton evaluations. Thus the two kernels defining
each \(Q_N\) are complete. The identity in (5) is in the original
Hermite algebra, with its double-root normal coordinates.

Retain the original midpoint endpoint and short height,
\[
 a_N=\pi-\frac{2\pi\lfloor N/400\rfloor}{N},\qquad
 a_N\ge\pi-\pi/200,\qquad 0<h_c\le1/1000.
 \tag{6}
\]
For all sufficiently large \(N\), \(a_N<\pi\). Define
\[
 a_R=19\pi/20,\qquad h_R=1/100,
\]
and orient the path by its successive vertices
\[
 \Gamma_{R,N}^{\mathrm{far}}:
 a_R-ih_R,\quad a_N-ih_R,\quad a_N-ih_c.
 \tag{7}
\]
Its entire real-angle range lies in \([a_R,\pi)\), and all
its depths lie in \([h_c,h_R]\).

**Theorem.** On fixed complex neighborhoods of the two real
incoming-color intervals, uniformly at both level parities,
\[
 \frac{N^2}{\pi}
 \int_{\Gamma_{R,N}^{\mathrm{far}}}
 |G_N(u;\mathbf w)W_N(u)|\,|du|
       \le C e^{N(M_g-1/20)}
 \tag{8}
\]
for all sufficiently large \(N\). Every fixed mixed ordinary
incoming derivative satisfies the same bound on smaller fixed
neighborhoods. In particular (8) bounds the original signed
current with scalar \(-N^2C_{N,4}/(\pi i)\).

## 3. Proof with every Newton index retained

First take \(w_L,w_R\in[-2,2]\). The complete column bound in
the far-boundary theorem gives
\[
 \|J_NM_N^3\mathbf e(w)\|_2
       \le CN^B e^{N\sigma_0},\qquad
 \sigma_0=2b_2+c<3/2.
 \tag{9}
\]
This uses \(\|M_N^2\|\), \(\|M_N\|\), and the full real
evaluation vector. It has no restriction on the outgoing angle.

The complete-vector theorem supplies
\[
 \|\mathbf e(-2\cos(a-ih))\|_2
       \le CN^B e^{N(m_0(a)+h)},\qquad
 m_0(a)\le\frac{\pi-a}{\pi},
 \tag{10}
\]
for \(0\le a\le\pi\), \(0\le h\le7/10\).
Its proof treats all indices \(0\le j<N\); it does not stop
at the first zero of a Newton product or discard the upper
half of the index range. On (7), \(m_0(a)\le1/20\).
Equations (5), (9), (10), and the finite-dimensional
Cauchy--Schwarz inequality therefore give
\[
 |F_N(a-ih;\mathbf w)|
       \le CN^B
            e^{N(2\sigma_0+1/10+2h)}.
 \tag{11}
\]
The two remaining exponential factors are exact:
\[
 |e^{iN(a-ih)^2/\pi}|=e^{2Nah/\pi},\qquad
 |W_N(a-ih)|
       \le \frac{e^{-Nh}}{(1-e^{-Nh})^2}
       \le C e^{-Nh}.
 \tag{12}
\]
The last constant is uniform because \(h\ge h_c>0\). It
retains the whole rational denominator, including every Fourier
charge. At the midpoint column its denominator is in fact
\((1+e^{-Nh})^2\), but this stronger fact is not needed.

Combining (11)--(12), the full rate on either segment of (7)
is at most
\[
 2\sigma_0+\frac1{10}
           +\left(1+\frac{2a}{\pi}\right)h
 <3+\frac1{10}+\frac3{100}
 =\frac{313}{100}.
 \tag{13}
\]
The sine, uniformly bounded path length, and original prefactor
\(N^2/\pi\) contribute only polynomial factors.

For completeness the incoming neighborhood is obtained from
an estimate on the whole real interval, not from one value.
For fixed \(u\), each \(Q_N(w,u)\) has ordinary degree at most
\(D=N-1\) in \(w\). Expand \(F_N\) separately in the two
Chebyshev bases on \([-2,2]\). Its coefficients are bounded
by four times its uniform real-bidisk norm; there are at most
\((D+1)^2\) terms. The filled ellipses of parameter
\(\rho=e^{1/1000}\) therefore add at most
\(2D/1000\le N/500\) to the exponential bound.
Their interiors contain fixed complex neighborhoods of
the real intervals.

Spend a further \(1/1000\) in the rate to absorb all polynomial
factors, including the finite Chebyshev sums and the integral
prefactor. The total is then at most \(3133/1000\), whereas
\[
 \frac{321}{100}-\frac1{20}=\frac{3160}{1000}
                         >\frac{3133}{1000}.
 \tag{14}
\]
Equations (4), (13), (14) prove (8). Cauchy's formula on
smaller ellipses gives the fixed ordinary incoming derivatives;
it may be applied pointwise in \(u\) before integration.
This proves the theorem.

## 4. The connection still requiring an estimate

The exact remaining right current starts at \(\pi/2-iK_g\)
and ends at \(a_N-ih_c\). The full integrand in (5) is
holomorphic in the lower half-plane: its polynomial and
trigonometric factors are entire, and the sampling denominator
has zeros only on the real line. Thus this current may be
deformed to any lower-half-plane path joining
\[
                    \pi/2-iK_g
                    \quad\hbox{to}\quad
                    19\pi/20-i/100,
 \tag{15}
\]
followed by (7).

The final part is now bounded by (8). No estimate of the
intermediate path in (15) is asserted. In the exact closing
identity it remains as one literal integral of the complete
finite functions. Shrinking the incoming neighborhood so that
\(|\Re\Theta(\mathbf w)-M_g|<1/200\) expresses the far-right
error with a fixed positive gap relative to
\(\Re\Theta(\mathbf w)\) as well.

The nonzero middle contribution and the paid left connection
do not rule out cancellation with the remaining integral.
Neither the closed-knot volume identity for this calculation
nor stability under arbitrary short partial fillings follows
from this far-right bound.

## Source bindings

- Original phase and lower-rectangle action floor:
  [larger closing strip](research_mixed_symmetric_closing_strip_phase_and_tail.md),
  fa1224123389462fd7e29199f1045d0892c167225b4dd6f79ea5bd967a583795.
- Actual-height horizontal maximum:
  [horizontal concavity](research_mixed_symmetric_closing_horizontal_concavity.md),
  f7890776761cf7d59e015617b9daf89a240d0b57b1bd51c86ee1e03000782a0b.
- Complete Newton vector, including the upper index range:
  [left-far vector estimate](research_mixed_symmetric_closing_left_far_connection.md),
  d02646e7422138c265de9ed1e16749590a8cb2f808b9cf15f30e584627aa6184.
- Complete crossing-column bound and original midpoint endpoints:
  [far-boundary source](research_mixed_symmetric_closing_far_boundary_payment.md),
  dc1942698fe442e9995c6bf1ee44ae67f7432c54f2f2d2086e108d83f132fd6b.
- Exact original right current and normalization:
  [two-current identity](research_mixed_symmetric_closing_two_remaining_currents.md),
  15c28d0004bfcdebd26e55dfe48419aa54d14c563c95e33e1d32ef5b1ac6cad8.
