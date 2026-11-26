# Why the complete-edge ray does not extend unchanged to an internal pair

Research calculation, 4 November 2026. Frozen manuscripts are unchanged.

The [outer-index estimate](research_real_pair_geometry_and_tail_gap.md)
permits the traced pair sum to be restricted to
\(1/50<j/N<12/25\), with an exponentially smaller error.
This does not make a direct extension of the complete-edge tangent
ray valid. A zero of a shifted sine argument, and nearby exact
reciprocal-factorial zeros, can lie between the real wire interval
and that ray, even inside the retained interval. The
positive pair of powers \((7,3)\) supplies a verified example.

## 1. The proposed ray and the zero it must avoid

Let \(t=a-iH\) and \(u\) be the selected trace angles. Set
\[
 A=\cos^2(t/2),\qquad B=\cos^2(u/2),\qquad
 W=\sqrt{\frac{AB}{A+B-AB}},\qquad \gamma=\arg W.
 \tag{1}
\]
The square root is continued from the positive geometric solution.
The internal-edge critical equation in the coordinate
\(z=\tan(\pi x)\) factors as
\[
 \{A-(1-A)z^2\}\{B-(1-B)z^2\}-z^4
 =-(A+B-AB)(z^2-W^2)(z^2+1).
 \tag{2}
\]
It is therefore natural to consider the ray \(z=Wr\),
\(r>0\), through the selected saddle. For \(0<\gamma<\pi/2\),
its image in the wire plane is the graph
\[
 x=\xi+ih(\xi),\qquad
 h(\xi)=\frac{1}{2\pi}
      \operatorname{asinh}\{\tan\gamma\sin(2\pi\xi)\},
 \quad 0<\xi<1/2.
 \tag{3}
\]

One scaled sine argument of the limiting factorial phase vanishes at
\[
 x_0=\frac12-\frac{t}{2\pi}
     =\frac12-\frac{a}{2\pi}+i\frac{H}{2\pi}.
 \tag{4}
\]
In particular \(\tan(\pi x_0)=\cot(t/2)\). The finite factorial
argument at this point is \(-1/2\); it is regular, and is not
itself a zero of the exact interpolant. This distinction is
addressed below. The limiting sine zero is
strictly between the real interval and (3) precisely when
\[
 H<\operatorname{asinh}\{\tan\gamma\sin a\}.
 \tag{5}
\]
This is a criterion at the actual pair angles, rather than
at freely chosen points of an angular rectangle.

## 2. A positive period solution for which (5) holds

Use the original principal logarithmic equations
\[
 \begin{split}
 7t+2i\{\operatorname{asinh}\tan(t/2)
       +\operatorname{asinh}(\tan(t/2)\cos(u/2))\}&=2\pi,\\
 3u+2i\{\operatorname{asinh}\tan(u/2)
       +\operatorname{asinh}(\tan(u/2)\cos(t/2))\}&=2\pi.
 \end{split}
 \tag{6}
\]
The [interval checker](../experiments/check_pair_truncated_ray_obstruction.py)
encloses a solution of (6), verifies the positive return branches,
and proves uniqueness in its enclosing box. On every original
edge \((v,w)=(t,0),(t,u),(u,0)\), it additionally certifies
\[
 \Re q_{vw}>
 \sqrt{\{\Re\tan(v/2)\}^2+\{\Re\tan(w/2)\}^2},
 \qquad q_{vw}=\sqrt{1+\tan^2(v/2)+\tan^2(w/2)}.
 \tag{7}
\]
This is the exact [positive-edge criterion](research_positive_edge_global_monotonicity.md),
not merely positivity of the real parts of two returns.
The four distinct original shape expressions on each edge
also have certified positive imaginary parts. Finally the
identities \(\cosh r_{vw}=q_{vw}\cos(w/2)\), with positive
real part on the right, verify the return square-root signs.
Thus the solution lies in the positive domain of the
[pair variational theorem](research_radical_path_sector_gap.md#6-a-uniform-estimate-for-every-positive-pair-of-powers-at-least-three).
That theorem identifies this solution with the selected positive
pair. The certificate gives
\[
 \frac1{50}<\Re x_0<\frac{12}{25},\qquad
 0<\Im x_0<h(\Re x_0)-\frac3{1000}.
 \tag{8}
\]
For orientation, \(\Re x_0\) is approximately \(0.362689\).
The strict assertions in (8) use outward interval arithmetic,
not those rounded values.

The checker first obtains a candidate with numerical root finding.
It then applies a fixed inverse of the central Jacobian to (6).
On a complex rectangular box of radius \(2^{-100}\) in each
real coordinate, the resulting fixed-point map sends the box
strictly into itself and has derivative norm less than \(1/2\).
This proves existence and uniqueness there. The branch checks and
(8) are evaluated on the whole box. The
[saved certificate](../repro/results/research-pair-truncated-ray-obstruction.json)
records the box, image, derivative bound, and geometric inequalities.

The contraction is measured in the maximum complex-coordinate norm.
The rectangular box is convex, and the interval Jacobian encloses
the integral derivative along every segment in it. Hence the
recorded affine interval image contains the full fixed-point map.
Moreover \(\|I-BJ\|<1\) forces \(BJ\), and therefore the fixed
preconditioner \(B\), to be invertible. A fixed point consequently
solves (6), rather than merely its preconditioned equations.

## 3. Exact finite zeros and the scope of the obstruction

The canonical factorial representative is
\[
 B_N(x,t)=\frac{N}
 {G_N(N(1/2-x+t/(2\pi))-1/2)
  G_N(N(1/2-x-t/(2\pi))-1/2)G_N(Nx)^2}.
 \tag{9}
\]
Its [exact factorial recurrence](exact_factorial_interpolation_and_complex_contours.md)
shows that \(G_N\) has a simple pole at \(-1\), since
\(G_N(0)=1\) and
\(G_N(z+1)=2\sin(\pi(z+1)/N)G_N(z)\).
Consequently
\[
 x_N=x_0+\frac1{2N}
 \tag{10}
\]
is an exact simple zero of the second reciprocal factorial in
(9). The other argument in (9) is \(Nt/\pi-1\), and the repeated
argument is \(Nx_N\). Their real parts lie in the nonzero strip
\(-1<\Re z<N\). They are therefore finite and nonzero and cannot
cancel this zero.

The other endpoint factor \(B_N(x_N,u)\) is regular too.
The certificate gives \(H_u>H_t>0\). Thus both of its shifted
factorial arguments have nonzero imaginary part. The canonical
factorial has zeros and poles only on the real axis, as follows
from its gamma product and integer-shift continuation. Its
repeated argument \(Nx_N\) is again in the regular strip.
In particular the zero is not canceled in the product of the
two original factorial representatives.

The checker also proves \(0<\tan\gamma<1/2\) and
\(\Re x_0<12/25-1/200\). From (3),
\[
 |h'(\xi)|
 =\left|\frac{\tan\gamma\cos(2\pi\xi)}
 {\sqrt{1+\tan^2\gamma\sin^2(2\pi\xi)}}\right|<\frac12.
 \tag{11}
\]
For every \(N\ge100\), (8) therefore implies
\[
 \frac1{50}<\Re x_N<\frac{12}{25},\qquad
 h(\Re x_N)-\Im x_N>
          \frac3{1000}-\frac1{4N}\ge\frac1{2000}.
 \tag{12}
\]
This finite-zero assertion retains the half-integer factorial
shift; it does not identify \(x_0\) itself as a finite zero.

The finite Newton polynomials are entire. A zero between two
contours is not a pole and does not itself prohibit a deformation
of the exact polynomial. It does invalidate a proof that uses
one zero-free logarithmic phase throughout the swept region,
as in the complete-edge ray argument. Such a proof would need
a detour and its estimates, or an explicit treatment of the
changed factorial branches. The outer-index cutoff alone does
not supply either.

This observation does not refute the desired pair asymptotic.
It rules out transferring the complete-edge deformation unchanged.
The [regular-support cell formula](research_pair_regular_support_cells.md)
retains the corresponding changes of support as explicit currents;
their grouped estimate remains a possible route.

Run the certificate with

```sh
python3 experiments/check_pair_truncated_ray_obstruction.py
```
