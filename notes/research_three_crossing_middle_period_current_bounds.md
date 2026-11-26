# The new Newton-cut currents on the intermediate boundary interval

This note supplies the 39 additional current bounds needed when the
retained Newton cutoff changes from \(2/5\) to \(13/40\). It uses
the exact original cellwise contour identity. The existing 144-case
certificate and its source files are unchanged.

The new inequalities are proved first at \(u=3/5\), then extended
uniformly to \(3/5\le u\le\pi/3\). The original boundary variable
is \(w=-2\cos u\). These are bounds for the actual retained contour
currents, not estimates of unrelated real lattice tails.

## 1. The boundary correction and imaginary convexity

Use the phase \(\Xi(x,y,z;u)\) of
[the prepared boundary sum](research_three_crossing_prepared_boundary_sum.md).
Its only boundary dependence is the original Newton phase
\[
 \begin{split}
 b(y,u)={}&J(1/2+a)+J(1/2-a)\\
 &-J(1/2-y+a)-J(1/2-y-a)-2J(y),
 \qquad a=\frac{u}{2\pi}.
 \end{split}                                                   \tag{1}
\]
All branches are the original factorial-strip branches. Since
\(J(t)+J(1-t)=0\) on that strip, the exact correction is
\[
 \Delta b(y,u):=b(y,u)-b(y,0)
 =2J(1/2-y)-J(1/2-y+a)-J(1/2-y-a).                              \tag{2}
\]
At the new cutoff and throughout the required real interval,
\[
 \frac12-\Re y-\frac{u}{2\pi}
       \ge\frac12-\frac{13}{40}-\frac16=\frac1{120}>0.           \tag{3}
\]
Thus all shifted factorial arguments stay in their original open
strips, uniformly for the fixed contour heights. The original
\(y\le2/5\) cutoff likewise stays in those strips for
\(0\le u\le3/5\).

Write \(y=s+it\), with \(0<s<1/2\). Direct differentiation of
(1), with no change of logarithmic branch, gives
\[
 \partial_u\Re b(y,u)
 =\frac1{4\pi}\log
 \frac{\cosh(2\pi t)+\cos(2\pi s+u)}
      {\cosh(2\pi t)+\cos(2\pi s-u)}<0
             \qquad(0<u<\pi).                                 \tag{4}
\]
The strict inequality follows from
\(\sin(2\pi s)\sin u>0\); all denominator factors are nonzero
on the indicated strips. In particular every fixed-height phase
and current rate decreases as \(u\) increases.

The real horizontal Hessian has the same form as equation (10) of
[the global horizontal theorem](research_three_crossing_global_horizontal_and_wire_tails.md),
except that its positive \(y\)-diagonal term \(2\Re\tan\pi y\)
is replaced by
\[
 T(y,u)=\Re\{\tan(\pi y+u/2)+\tan(\pi y-u/2)\}
 =\frac{2\sin(2\pi s)
          [\cos(2\pi s)+\cos u\cosh(2\pi t)]}
        {|\cos(2\pi y)+\cos u|^2}>0.                            \tag{5}
\]
Indeed \(\cos u>0\) and the positive-strip condition gives
\(\cos(2\pi s)+\cos u>0\). Formula (5) applies on both ranges
\[
 \begin{cases}
 1/10\le s\le2/5,&0\le u\le3/5,\\
 1/10\le s\le13/40,&3/5\le u\le\pi/3.
 \end{cases}                                                    \tag{6}
\]
The global rank-one comparison used only the lower bound
\(4\Re\cot\pi y\) on that diagonal. Consequently the same
strict horizontal concavity holds on these ranges. Holomorphy then
gives simultaneous imaginary convexity. The closed-polytope and
small-thickening argument of the cited theorem still applies.

This proves that the intervening vertical heights in each current
can again be reduced to their endpoints and zero, with the exact
piecewise-linear Fourier penalty. No intermediate height is dropped.

## 2. The exact 39 new inequalities

Let \(h=(\Im x_*,\Im y_*,\Im z_*)\), so \(h_x<0<h_y,h_z\).
For \(\sigma\in\{-1,0,1\}^3\), put
\[
 f_{\sigma,u}(r)=\Re\Xi(r+i\sigma h;u),\qquad
 P_\sigma=2\pi\sum_{\sigma_j=-1}|h_j|.                           \tag{7}
\]
The retained real polytope now has
\[
 1/10\le r_x\le1/2,\quad
 1/10\le r_y\le13/40,\quad
                1/100\le r_z\le r_x-1/400.                     \tag{8}
\]
Only the following cases are new:

| Support | Height choices | Count |
|---|---|---:|
| \(r_y=13/40\) | \(\sigma_x,\sigma_z\ne0\), any \(\sigma_y\) | 12 |
| \(r_y=13/40,\ r_x-r_z=1/400\) | all three height choices in each coordinate | 27 |

**Theorem 1.** On each complete face or edge in this list, at
\(u=3/5\),
\[
                \sup_r\{f_{\sigma,3/5}(r)-P_\sigma\}<3/2.       \tag{9}
\]
The same bound holds uniformly for \(3/5\le u\le\pi/3\).

*Proof.* On both listed supports, the complex value of \(y\) is
fixed at \(13/40+i\sigma_yh_y\). Hence (2) is constant in every
free real coordinate. The \(x,z\) derivatives of the phase are
unchanged; on the edge their sum gives the derivative along
\(r_z=r_x-1/400\). The actual \(y\) derivative is not needed
and is not replaced by its value at zero boundary angle.

The exact verifier
[verify_three_crossing_middle_period_faces.py](../experiments/verify_three_crossing_middle_period_faces.py)
checks that its cases are precisely the 12 plus 27 choices above,
without duplicates. At each rational point in the
[tangent-point fixture](../repro/fixtures/research-three-crossing-middle-period-face-points.json)
it evaluates the original phase and its unchanged \(x,z\)
derivatives, adds the real correction (2), and maximizes the resulting
affine tangent upper bound at the four face vertices or two edge
endpoints. Global concavity makes this a bound on the entire face or
edge; the tangent point need not be its maximizer.

All arithmetic is rational and outward, using the already audited
principal logarithm and dilogarithm routines. Every argument in (2)
has real part strictly between zero and one. Schwarz reflection of
the original \(J\) shows that the real corrections at \(+h_y\)
and \(-h_y\) agree. Therefore only the zero-height and positive-height
corrections need separate evaluation. Both are strictly negative.

The completed
[39-case certificate](../repro/results/research-three-crossing-middle-period-faces.json)
proves (9) in every case. Its maximum certified upper bound is below
\(1.466570\). It retains the previous 144-case result and every
direct code and height-certificate dependency by hash. No previous
certificate was overwritten or relaxed. Finally (4) gives the
pointwise extension from \(3/5\) to \(\pi/3\). \(\square\)

## 3. Why these cases cover the new currents

Use exactly the indicator \(\chi_N\) and finite differences
\(\Delta_V\chi_N\) in
[the cellwise contour theorem](research_three_crossing_retained_polytope_contour.md),
with only its upper \(y\) cutoff changed. The five old limiting
families
\[
 x=1/10,\quad y=1/10,\quad z=1/100,\quad
 x=1/2\ (\sigma_z\ne0),\quad
 x-z=1/400\ (\sigma_y\ne0)                                     \tag{10}
\]
are subsets of the previously certified faces. Their rates at the
new real angles are no larger than their rates at \(u=0\), by (4).
They retain all their previous strict bounds.

Consider a current on the new upper \(y\) face. If \(y\) is its
only vertical coordinate, its \(x,z\) heights are nonzero. It is
one of the 12 cases in Theorem 1. If an \(x\) or \(z\) coordinate
is also vertical, the exact support rules place it on an old \(x\)
or lower-\(z\) face, or on the diagonal cut. The old faces are
already covered by (10), with their required nonzero tangential
heights. In the remaining case both
\(y=13/40\) and \(x-z=1/400\) hold. This is one of the 27 new
edge cases.

The full 27-case edge is necessary: when \(y\) is vertical its
height may be zero. The old diagonal-face certificate explicitly
excludes that height. The new edge certificate includes it, together
with both staircase sheets of \(\Delta_x\Delta_z\chi_N\) and
all their further \(y\) differences. No triple or diagonal current
has been inferred to cancel.

By (5), the bounds at these height vertices control all intermediate
vertical heights after their exact kernel penalties are included.
The same compact-strip argument handles the actual \(O(N^{-1})\)
half-grid positions. The strict gaps persist on a small complex
neighborhood of the compact real boundary interval. Uniform
factorial bounds and polynomially many cell integrals then give
the original full mixed-current estimate, including fixed ordinary
boundary derivatives on a smaller neighborhood.

Consequently all mixed currents for (8), throughout
\(3/5\le u\le\pi/3\), have rate strictly below \(151/100\);
the newly introduced ones have the stronger bound (9). The seven
nonprincipal full horizontals also retain their old bound below
\(29/20\), by restriction and (4). For \(0\le u\le3/5\), the
original \(y\le2/5\) domain uses the same monotonicity and convexity
with its existing 144-case certificate. Negative real angles follow
from the exact evenness in \(u\).

These statements control the contour corrections for both cutoffs.
The principal horizontal, the removed real colors, and the outer
portion of the boundary period use their separate source bounds.
A whole-period source conclusion uses all those inputs together;
the 39 comparisons alone do not supply it.
