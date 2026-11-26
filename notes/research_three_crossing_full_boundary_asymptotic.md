# The full adjacent three-crossing boundary asymptotic

Research assembly, 3 November 2026.

The original adjacent three-crossing source has a nonzero geometric
contribution on a fixed complex neighborhood of its complete boundary
value. The proof keeps the exact finite sum, its boundary derivatives,
and every contour term. All 144 boundary inequalities have been
certified with rational outward arithmetic.

This is a local boundary theorem. The separate
[whole-period estimate](research_three_crossing_whole_period_source.md)
controls the rest of the real boundary period and permits the
[long-closing deduction](research_three_crossing_long_closing_fiber.md).

## 1. The original source and the boundary-current estimate

At integer level \(N\ge2\), put
\[
 D=N-1,\quad q=e^{\pi i/N},\quad
 \kappa=e^{\pi iD^2/(2N)},\quad
 \omega_N=\exp i\pi\left(\frac14+\frac1{4N}-\frac N{12}\right).
 \tag{1}
\]
Let \(M\) and \(J\) be the original crossing and turn matrices,
and let \(\mathbf e(w)\) be the original Newton evaluation vector.
The positive adjacent source, with its original external variable
retained, is the ordinary polynomial
\[
 F_N(w)=\mathbf e(w)^TJM^3JM^3\mathbf e_0 .
 \tag{2}
\]
The negative source is obtained by coefficient conjugation. Neither
(2) nor its derivatives are replaced by a coefficient norm or a
specified Fourier observation.

Use the exact prepared sum, phase \(\Xi(x,y,z;u)\), and density
\(a_3(x,y,z)\) from
[the finite prepared-source theorem](research_three_crossing_prepared_boundary_sum.md):
\[
\begin{split}
 \Xi={}&\mathcal J(x+y)-\mathcal J(x)-\mathcal J(x-z)
               -3\mathcal J(z)-2\mathcal J(y)+b(y,u)\\
 &+\frac{i\pi}{2}\big[(x-y)^2-x+y+2xz+2z^2\big],\\
 a_3={}&
 \frac{e^{i\pi(x-y)/2}\sqrt{\sin\pi(x+y)}}
 {16\sin^2(\pi y)\sqrt{\sin\pi x}\,
           (\sin\pi z)^{3/2}\sqrt{\sin\pi(x-z)}} .
\end{split}                                                       \tag{3}
\]
Here \(w=-2\cos u\), \(\mathcal J'(t)=\operatorname{Log}(2\sin\pi t)\),
and \(b\) is the canonical Newton phase, with
\(b(y,0)=\mathcal J(2y)-4\mathcal J(y)\).
All factorial and square-root branches are the original ones.

The retained indicator has limiting cuts
\[
 \frac1{10}\le x\le\frac12,\qquad
 \frac1{10}\le y\le\frac25,\qquad
                    \frac1{100}\le z\le x-\frac1{400}.           \tag{4}
\]
Its exact integer rounding and all finite differences are those in
[the retained-polytope contour theorem](research_three_crossing_retained_polytope_contour.md).
Let \(\epsilon=(-1,+1,+1)\), and let
\(H_x=-\Im x_*,H_y=\Im y_*,H_z=\Im z_*\) be the selected positive
height magnitudes.

The boundary-current theorem gives the following estimate.
Every actual nonempty vertical
subset \(V\) in the exact contour theorem has, on the limiting
support of \(\Delta_V\chi_N\), rate
\[
 \Re\Xi(v+ih;0)
 -2\pi\sum_{\substack{r\notin V\\h_r=-\epsilon_rH_r}}H_r
 -2\pi\sum_{r\in V}(-\epsilon_rh_r)_+
                    <\frac{151}{100}.                           \tag{5}
\]
It suffices to verify the stated six boundary families at their
144 allowed height vertices \(h_r\in\{-H_r,0,H_r\}\), using
the exact support restrictions of the contour theorem.
Convexity in the imaginary variables then gives the intervening
heights. The exact finite cuts differ by \(O(N^{-1})\), so strict
limiting bounds extend to them for all sufficiently large \(N\).

The checker is
[verify_three_crossing_current_faces.py](../experiments/verify_three_crossing_current_faces.py).
Its rational tangent points are inputs to global concave upper
bounds, not assumed numerical maxima. The
[saved rational certificate](../repro/results/research-three-crossing-current-faces.json)
contains exactly the 144 required cases, with no duplicates, and
verifies every inequality with explicit analytic remainders.
Its largest upper bound is less than \(1.499\).
Theorem 4 of
[the horizontal and boundary-current estimates](research_three_crossing_global_horizontal_and_wire_tails.md)
proves that these cases cover every term of the exact contour identity.
Thus (5) is a proved input.

## 2. The boundary theorem

Let \((x(u),y(u),z(u))\) denote the unique holomorphic continuation
of the selected stationary point, and put
\[
 W(u)=\Xi(x(u),y(u),z(u);u),\qquad
 C(u)=\frac{(2\pi)^{3/2}a_3(x(u),y(u),z(u))}
 {\sqrt{\det[-\Xi''_{x,y,z}(x(u),y(u),z(u);u)]}} .
 \tag{6}
\]
The square root is the Gaussian branch defined by integration over
the positively oriented real three-dimensional tangent plane.
Equivalently it is the holomorphic Gaussian square root on the
cone of complex symmetric matrices with positive real part.

**Theorem 1.** There is a fixed complex
neighborhood of \(u=0\) on which \(W,C\) are holomorphic and even,
\(C\) is nowhere zero, and
\[
 \boxed{\displaystyle
 F_N(-2\cos u)=\kappa^2\omega_N\,C(u)e^{NW(u)}
                         \bigl(1+O(N^{-1})\bigr).}               \tag{7}
\]
The error is uniform on a smaller fixed closed neighborhood and
the limit runs through all integer levels, without a parity
restriction.

Every term in (7) descends holomorphically to a fixed disk in the
ordinary variable \(w\) centered at \(-2\). On smaller fixed disks,
all fixed derivatives of the normalized relative error are
\(O(N^{-1})\). In particular (7) retains the original first normal
at the complete boundary, including odd levels.

For the negative source the same theorem holds with
\[
 W_-(u)=\overline{W(\overline u)},\qquad
 C_-(u)=\overline{C(\overline u)},\qquad
 \kappa^2\omega_N\ \hbox{replaced by }\
                         \overline{\kappa^2\omega_N}.            \tag{8}
\]
No new external crossing or carrier is inserted in these formulas.

## 3. Whole-source reduction and the nonprincipal currents

The exact original three-crossing preparation is
\[
 M^3\mathbf e_0=\kappa^3A_Nh+\delta_N,\qquad
 h_j=q^{j(j+2)}S_j^2,\qquad
 A_N=N^{-1/2}\omega_N(1+O(N^{-1})),
 \tag{9}
\]
with its specified exact \(A_N\). The
[global preparation-error theorem](research_three_crossing_global_preparation_error.md)
carries \(\delta_N\) through the entire remaining operator in (2).
Uniformly on \(|w+2|\le10^{-6}\), its rate is strictly less than
\(3/2\), with all fixed derivatives on a smaller disk.
That proof is an original-matrix operator estimate; it does not
assume any contour contribution.

Section 6 of the same note removes the outer real-color ranges
outside \(x\in[1/10,1/2]\), \(y\in[1/10,2/5]\) at rate at most
\(4507/3000+o(1)\).
The [wire-tail theorem](research_three_crossing_global_horizontal_and_wire_tails.md)
then removes \(z\le1/100\) and \(x-z\le1/400\) at rates at most
\(663/500\) and \(18229/12000\), respectively.
These bounds retain the entire ordinary boundary disk and every
original parity. Thus the source is reduced to (4), with an
exponentially controlled error before any complex deformation.

The cellwise contour identity is exact for this retained finite
sum. Its principal horizontal coefficient is exactly \(+1\):
each of its three one-cell orientation factors is
\(\epsilon_rs_r=1\) when \(s_r=\epsilon_r\).
The seven other full horizontal integrals are bounded separately
in Section 3 of the wire-tail note, each at rate below \(29/20\).
They are not included in the 144 mixed-current tests.

By (5), every remaining term of the exact identity has rate
below \(151/100\). The kernels and the complete finite-difference
supports are exactly those used in (5). The numbers of cells,
faces, and finite differences grow only polynomially, and the
canonical factorial estimates are uniform on their fixed bulk
sets. Therefore their sum obeys the same strict exponential gap.
There is no undeclared slanted face, dropped Fourier copy, or
untraced normal current.

The selected-action certificate gives
\[
                         \Re W(0)>\frac{153}{100}.              \tag{10}
\]
Among the explicit error rates just listed the largest is
\(18229/12000<153/100\). The cut perturbations, small boundary
perturbations, and polynomial factors can consequently be absorbed
in a fixed positive gap. This remains valid uniformly on a
sufficiently small complex boundary neighborhood.

## 4. The principal integral and its normalization

On the selected horizontal plane the real part of (3) is globally
strictly concave on (4), by the global horizontal theorem.
The selected stationary point is interior and is its unique
maximum. A fixed neighborhood of it therefore has a positive
action gap over the compact complement, including the limiting
faces. The union of actual retained cells differs only by
\(O(N^{-1})\) in its real boundary. It still contains the same
fixed stationary neighborhood, and its complementary region has
the same strict gap for all sufficiently large \(N\).

In that neighborhood the original summand, including its scalar,
has the uniform holomorphic expansion
\[
            A_N\kappa^2N^{-1}a_3(x,y,z)
                     e^{N\Xi(x,y,z;u)}(1+O(N^{-1})).             \tag{11}
\]
The three lattice-residue factors contribute \(N^3\).
The principal kernels equal one up to a uniform exponential
error because all three selected heights are separated from zero.
The real Gaussian integral contributes
\[
              (2\pi/N)^{3/2}/\sqrt{\det(-\Xi'')}.
\]
Thus its total power is
\[
               A_N N^{-1}N^3N^{-3/2}
                    =A_NN^{1/2}=\omega_N(1+O(N^{-1})).          \tag{12}
\]
Equations (11)--(12) give exactly (6)--(7), with no leftover
power of \(N\).

At \(u=0\), \(-\Re\Xi''\) is positive definite. The local Gaussian
square root and all density factors are therefore nonzero.
Their analytic continuations remain nonzero on a smaller fixed
disk. The implicit function theorem supplies the stationary
continuation. For complex \(u\), one may deform just the small
stationary neighborhood to its nearby critical point; the
interpolation is holomorphic there and the kernels remain away
from their poles. The boundary of that local deformation stays
in a strict-gap region. The complementary integrals and every
current retain their gaps by uniform continuity. Analytic
stationary phase therefore gives the uniform relative
\(O(N^{-1})\) error in (7).

The Newton interpolation is holomorphic and even in \(u\);
all other explicit factors are independent of \(u\).
Uniqueness of the nearby stationary point makes \(W,C\) even
as well. Every contour term consequently descends through
\[
                     w+2=2-2\cos u=u^2+O(u^4),
\]
which is an invertible local analytic coordinate in \(u^2\).
This proves ordinary-\(w\) holomorphy without division by
\(\sin u\). On a disk where \(C\ne0\), the normalized relative
error is holomorphic and \(O(N^{-1})\). Cauchy's formula on
smaller fixed disks gives all its stated derivative estimates.
The argument is uniform over all integer \(N\); coefficient
conjugation proves (8).

## 5. Marked geometric meaning and scope

The selected action in (6), after eliminating its \(z\) variable,
is exactly the calibrated remaining-row action. The
[absolute action-volume theorem](research_three_crossing_action_volume_calibration.md)
proves its equality with the original angular action up to a
constant in \(i\mathbb R\). Thus
\[
 2\pi\Re W(0)=\operatorname{Vol}(M_{3,3})
            =\operatorname{Vol}(M_{-3,-3}),\qquad
 U_0=-2\pi W'(u),\quad V=2iu .                                  \tag{13}
\]
These are the original two filled circles and original free
boundary, with both primitive slopes retained. The actual source
phase \(W\), not an arbitrarily rephased geometric primitive, is
used in (7). An outside carrier would be a later operation.

The theorem concerns the local original free-boundary polynomial
and every fixed normal derivative. It does not by itself state
a full-period Gaussian strip, a theorem for arbitrary adjacent
words, a long-closing-power theorem, or a finite-exception
classification. The separate whole-period estimate supplies the
upper gap used in the long-closing deduction. The local coefficient
and all local ordinary boundary derivatives are the contribution
of this note. Arbitrary connected short regions and the full
cofinite-template objective remain outside these results.
