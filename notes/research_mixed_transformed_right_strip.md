# The transformed three/four source on the right incoming interval

Research deduction, 7 November 2026. This note estimates the complete
conditional polynomial after fixing the outgoing coordinate near the
last private leg of the original ordinary three/four pair. It covers
the incoming interval from \(9/20\) to \(1/2\), at the original
critical height. The original terminal comparisons can be used here
because their required estimates are pointwise before the private
coordinate is summed. Its physical triangular support is not used.

## 1. Statement and exact interpolation

Use the notation, reference and action in
[the transformed upper-row theorem](research_mixed_transformed_upper_rows.md).
In particular
\[
 a_*=A+ic,\quad z_*=E+iv,\quad -7/200<c<0,\qquad
 C_{1,N}(X,Y)=\sum_{j=0}^{N-1}
              \frac{X^{-j}p_j(X)p_j(Y)}{P_j^3},
 \quad X=e^{-2\pi ia},\quad Y=e^{-2\pi iz}.              \tag{1}
\]
Write \(P_* =\mathcal P_{34}(z_*)\). Its phase is before a
final Gram contraction. It extends holomorphically to
\(\mathcal P_{34}(w,z)\) near \((-2,z_*)\).

**Theorem 1.** On a sufficiently small fixed neighborhood of
\((-2,z_*)\), every fixed pair of derivative orders satisfies
\[
 \left|\partial_w^k\partial_z^\ell
 \left[e^{-N\mathcal P_{34}(w,z)}
       U_{0,N}(w,e^{-2\pi i(x+ic)})
       C_{1,N}(e^{-2\pi i(x+ic)},e^{-2\pi iz})\right]\right|
 \le C_{k,\ell}e^{-N/500000},
 \qquad 9/20\le x\le1/2,                               \tag{2}
\]
for all sufficiently large integer levels, of either parity.

Here is the exact one-index interpolation used in the proof. If
\(\mathfrak P_N\) is the original canonical factorial, put
\[
 R_N(a,t,z)=e^{2\pi iNat}
 \frac{\mathfrak P_N(a+t)\mathfrak P_N(z+t)}
      {\mathfrak P_N(a)\mathfrak P_N(t)^3
       \mathfrak P_N(z)}.                               \tag{3}
\]
Its factorial difference equation gives
\[
 R_N(a,j/N,z)=X^{-j}p_j(X)p_j(Y)/P_j^3.                 \tag{4}
\]
On the regular central rectangle (3) has phase \(Q(t;a,z)\)
from equation (3) of the upper-row theorem, with its original
branches. Equivalently it is exactly the retained terminal
interpolant divided pointwise by
\[
 D_N(z)=\Delta_N(z)^{-1}\mathcal C_N(z,-2).
\]
The complete endpoint theorem makes \(D_N\) nonzero on a fixed
neighborhood of \(z_*\) for all sufficiently large \(N\).
This equality is an identity of interpolants; no bound on an
integrated terminal polynomial is divided by \(D_N\).

## 2. Pointwise comparisons inherited from the ordinary source

The exact terminal phase satisfies
\[
 \Phi(a;t,z)=E_{\rm end}(z)+Q(t;a,z),\qquad
 M=\Re P_*+\Re E_{\rm end}(z_*).                       \tag{5}
\]
Its original private main segment contains the fixed value
\(z_*\). Every comparison below is pointwise on that segment;
therefore subtracting the constant \(\Re E_{\rm end}(z_*)\)
preserves its gap.

Let \(b=9/20\), let \(h_t\) be the original critical transform
height, and use the complete cap rate
\[
 B_U(x)=\Re T_0(a_*)-p(x-A)-\kappa_*(x-A)^2,
 \quad p=\Re P_1'(a_*),\quad\kappa_*=1/2500000.          \tag{6}
\]
The following are the needed comparisons from the written ordinary
source proofs.

| Transform part, with \(z=z_*\) fixed | Bound after multiplying by the complete cap and removing \(E_{\rm end}(z_*)\) |
|---|---|
| \(.15\le\Re t\le.5\), height \(h_t\) | At most \(\Re P_*-1/20000\), by [joint curvature](research_mixed_three_four_right_strip_joint_curvature.md), equations (9)--(10) |
| \(t=.5\) real | At most \(\Re P_*-1/20000\), by [right-face transport](research_mixed_three_four_private_left_right_extension.md), Proposition 4 |
| \(.15\le\Re t\le.5\), heights \(\pm.12\), with their original sampling penalties | At most \(\Re P_*-1/25\), by Theorem 6 of the same right-extension note |

The first row is valid for every point of the whole original private
main segment because it is proved before its maximum is taken.
The second and third rows likewise retain that pointwise private
coordinate. There is no need to import a statement about ordinary
two-leg references at an unrelated private reference.

For the left transform side use the moving boundary
\[
                       s(x)=3/5-x\in[.1,.15].           \tag{7}
\]
Lemmas 1--3 of
[the moving-boundary proof](research_mixed_three_four_moving_transform_cut.md)
are pointwise for every \(z\) in the old private rectangle. They
give the following three statements, with \(z=z_*\).

* On \(.1\le\Re t\le.15\), \(|\Im t|\le.12\),
  \(\partial_{\Re t}\Re Q>1/60\).
* The real part of \(Q\) is convex in \(\Im t\) on that
  added rectangle.
* The coupled real-side function
  \(B_U(x)+\Re Q(s(x);x+ic,z_*)\) decreases at rate
  greater than \(1/20\). At \(x=b\) it is the old real
  transform face \(t=.15\), whose raw gap is \(1/20000\).

The endpoint action is independent of \(t,x\), so removing it
does not change any of these derivatives. In particular
\[
 B_U(x)+\Re Q(s(x);x+ic,z_*)
                         \le\Re P_*-1/20000.          \tag{8}
\]
The added horizontal main and alias portions transport by the first
bullet to their already controlled values at \(\Re t=.15\).
At either real side, convexity in the transform height bounds
ordinary joins by their two endpoints. For each sign of height,
subtracting the linear sampling penalty preserves that convexity.
Thus it also bounds all the vertical alias portions. On the old
rectangle, the requisite convexity follows from the joint-curvature
proof; at the new left side it is the second bullet above. The
main, both joins and all sampling corrections have consequently
retained a raw gap of at least \(1/20000\).

## 3. The exact physical partition

Let
\[
 L_N(x)=\lceil Ns(x)\rceil,\qquad H_N=\lceil N/2\rceil.
\]
Partition the original rows into
\[
 0\le j<L_N(x),\qquad L_N(x)\le j<H_N,
 \qquad H_N\le j<N.                                    \tag{9}
\]
For the middle set apply the original one-index residue formula to
(3). Its vertical boundaries are the half-grid lines
\((L_N(x)-1/2)/N\) and \((H_N-1/2)/N\). Its horizontal
boundaries stay at heights \(-.12,.12\). The constant mode has
coefficient \(+N\); move it to height \(h_t\), retaining its
two joins. Keep both horizontal aliases and both sign halves of
each vertical alias. All these pieces were bounded in Section 2.
The reciprocal factorials and the other numerator arguments remain
regular. The numerator \(\mathfrak P_N(a+t)\) can reach real part
one; it has strictly negative height on the main line, and on the
other source currents it uses the same zero-safe continuation as
the moving-boundary proof, including a possible numerator zero.
The half-grid discrepancies change rates by at most
\(O(\log N/N)\). A jump in \(L_N(x)\) transfers one complete
row between the first two sets in (9); we do not differentiate that
integer-valued boundary.

For the first set, the physical row rate is \(E_1(t;a,z_*)\)
of equation (5) in the upper-row theorem. Lemma 2 of
[the right physical-complement proof](research_mixed_three_four_right_strip_physical_complement.md)
is a derivative calculation on the entire private rectangle. It
gives
\[
 \partial_t E_1(t;x+ic,z_*)>\log(3/2),
                      \qquad 0<t\le.15.                \tag{10}
\]
Thus every lower physical row is bounded by the moving real face
(8). This includes \(j=0\) by continuity of the integrated rate.
Uniform finite product estimates, including the factorial endpoints,
are those proved in the upper-row note. No separate coherent
terminal estimate is needed at the true lower end.

The third set is exactly the complete high-row sum bounded by
Theorem 2 of the upper-row note. It includes every restored row,
regardless of the support it had before the outgoing variable was
fixed at \(z_*\). The even half row is assigned to this set only.
There is no private physical summation remaining in any of (9).

## 4. Uniformity and derivatives

At \((w,z)=(-2,z_*)\), Sections 2--3 give a strict gap for every
piece of the exact finite sum. The complete cap bounds may be used
before each integration. Fixed path lengths, the coefficient
\(+N\), the number of rows and all regular symbols cost only
polynomial factors. The reciprocal factorials and non-wall arguments
remain regular on fixed neighborhoods of the retained paths; the
numerator \(\mathfrak P_N(a+t)\) retains its uniform zero-safe
bound at the wall. The literal numerator
product bounds for the physical tails are uniform on a small
negative-height neighborhood of \(z_*\).

These facts, the existing ordinary-color continuation of the cap,
and continuity of \(\mathcal P_{34}(w,z)\) allow one fixed
neighborhood and one total tolerance. Shrink them to preserve a
gap larger than \(1/500000\), taking into account the already
weakened high-row bound. Cauchy's formula on smaller neighborhoods
proves (2) for every fixed derivative order. This proves Theorem 1.

The factor \(N\) and integration over this fixed incoming interval
in the transformed prefix preserve an exponential gap. The result
settles this whole right interval. The left taper and the central
stationary contribution are separate estimates; uniformity under
further short attachments is not asserted here.
