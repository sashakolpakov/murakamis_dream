# An explicit contraction for the geometric equations of a chain

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

Consider a chain in which every crossing power is three and both
outside vertices are complete. Its geometric equations can be solved
by repeatedly solving one vertex equation with its two neighbors
held fixed. We give a fixed rectangle preserved by this operation
and a contraction constant independent of the number of vertices.
This makes the geometric boundary-decay theorem quantitative.
It does not estimate a quantum sum or prove that a geometric
critical point contributes to that sum.

## 1. The one-vertex equation

Write an angle as \(t=a-iH\) and define
\[
 \Omega=\left\{a-iH:
       \frac{13}{10}\le a\le\frac{91}{50},\quad
       \frac{41}{50}\le H\le\frac{121}{100}\right\}.
 \tag{1}
\]
An outside complete vertex has angle zero. For two neighboring
angles \(u,w\), each either in \(\Omega\) or equal to zero, the
original logarithmic period equation is
\[
 \begin{split}
 G(t;u,w)&=3t+2i\{r(t,u)+r(t,w)\}-2\pi=0,\\
 r(t,u)&=\operatorname{asinh}
                  \bigl(\tan(t/2)\cos(u/2)\bigr).
 \end{split}
 \tag{2}
\]
These are the original equations of
[the positive path theorem](research_positive_path_fractional_charge_cube.md),
with unit charges. The branch of \(\operatorname{asinh}\) is the
one with positive real part on the right half-plane.

For \(t,u\in\Omega\), the tangent of \(t/2\) has positive real
part and negative imaginary part, while the cosine of \(u/2\)
has positive real and positive imaginary parts. Their product
has positive real part. The same is true for \(u=0\).
Thus all returns in (2) are holomorphic on a neighborhood of
the indicated rectangles. No logarithmic period is replaced
by its exponential.

Put \(v=\tan(t/2)\), \(c=\cos(u/2)\), and
\(s=(1+v^2c^2)^{1/2}\), with positive real part. Direct
differentiation gives
\[
 r_t=\frac{c(1+v^2)}{2s},\qquad
 r_u=-\frac{v\sin(u/2)}{2s},\qquad
 T_u=-\frac{2ir_u(t,u)}
                {3+2i\{r_t(t,u)+r_t(t,w)\}},
 \tag{3}
\]
where \(T\) denotes any local root of (2).

**Certified derivative lemma.** Throughout \(t,u\in\Omega\),
with \(w\in\Omega\) or \(w=0\),
\[
 \Re G_t>0,\qquad
 0<\Re T_u<\frac14,\qquad
 |\Im T_u|<\frac1{16}.
 \tag{4}
\]
For two selected endpoints the returns also satisfy
\[
               \Re r(t,u)>0,\qquad
                     -\frac35<\Im r(t,u)<0.
 \tag{5}
\]

The [outward calculation](../experiments/certify_homogeneous_three_geometric_box.py)
proves (4)--(5) on a finite covering of the entire domain.
For each rectangle of \(t\)-values, it divides the neighbor rectangle
into a \(32\) by \(32\) rational grid and encloses \(r_t(t,w)\)
over their union. It then substitutes that enclosing complex
rectangle into (3), checking every rectangle for \(u\), and also
checks the complete value \(w=0\). Over-enclosing the other return
is harmless: every actual denominator is included.
If any strict inequality is unresolved, the \(t\)-rectangle is
bisected. A successful record requires the queue to be empty.
Section 5 gives the exact-cover and scalar checks used with it.

To avoid repeated-variable overestimation, the calculation uses the
holomorphic mean-value formula from the center of each product
rectangle. The derivative enclosures are
\[
 \begin{split}
 r_{tt}&=\frac{cv(1+v^2)}{2s}
                  -\frac{c^3v(1+v^2)^2}{4s^3},\\
 r_{tu}&=-\frac{\sin(u/2)(1+v^2)}{4s^3},\qquad
 r_{uu}=-\frac{vc(1+v^2)}{4s^3}.
 \end{split}
\]
For example, the enclosure of \(r_t(t,u)\) is its center value
plus \(r_{tt}\Delta t+r_{tu}\Delta u\), with both derivatives
enclosed on the whole product rectangle. The straight segment
stays in that rectangle and the branch is holomorphic there.
This is an enclosure of every parameter value, not numerical
differentiation or interpolation between samples.

## 2. Continuation stays inside the rectangle

Let \(t_*\) be the homogeneous angle:
\[
       \cos t_*=-\frac14+\frac{3\sqrt3}{4}i,\qquad
          0<\Re t_*<\pi,\quad \Im t_*<0.
 \tag{6}
\]
The [exact homogeneous calculation](research_homogeneous_three_action_calibration.md)
proves \(G(t_*;t_*,t_*)=0\) with the logarithms in (2).
The scalar enclosures used here are
\[
 \begin{array}{c|c|c}
 \text{neighbors}&\Re T&-\Im T\\ \hline
 t_*,t_*&(1.722,1.723)&(1.087,1.088)\\
 0,t_*&(1.539,1.540)&(.982,.983)\\
 0,0&(1.381,1.383)&(.882,.884).
 \end{array}
 \tag{7}
\]
For the last two rows, outward Rouché estimates isolate roots in
disks of radius \(10^{-9}\), with respective centers
\[
 \begin{split}
 1.539056826670160188-.982192219812633070i,\\
 1.381983397031137455-.883007686999445322i.
 \end{split}
 \tag{8}
\]
The displayed decimals in these certificates are exact rationals.
The checker bounds the actual residual and the second derivative
on each disk; it does not infer existence from a small numerical
residual alone.

**Lemma 1.** For each neighbor type, equation (2) has a continuous
root \(T(u,w)\) in the interior of \(\Omega\), holomorphic locally
in every noncomplete neighbor. This chosen root satisfies (4).

*Proof.* Keep any complete neighbors fixed and move each of the
other neighbors along the straight segment from \(t_*\) to its
desired value in \(\Omega\). Start with the appropriate row of
(7). As long as the root stays in \(\Omega\), (4) gives local
continuation and bounds its derivative.

Here is an explicit no-exit estimate. Write \(T_u=p+iq\) and
change one neighbor by \(\delta a-i\delta H\). The corresponding
changes of the real angle and height are
\[
       d(\Re T)=p\,\delta a+q\,\delta H,\qquad
       d(-\Im T)=p\,\delta H-q\,\delta a.
 \tag{9}
\]
During continuation, \(0<p<1/4\) and \(|q|<1/16\).
Relative to \(t_*\), the target neighbor changes satisfy
\[
 \begin{split}
 -.423\le\delta a\le .098,\qquad
 -.268\le\delta H\le .123,\\
 |\delta a|\le .423,\qquad |\delta H|\le .268.
 \end{split}
 \tag{10}
\]
Integrate (9) and use the signs of the changes in the terms
containing \(p\). With two noncomplete neighbors, the root remains in
\[
       1.477<\Re T<1.8055,\qquad
             .900125<-\Im T<1.202375.
 \tag{11}
\]
With one noncomplete neighbor it remains in
\[
       1.4165<\Re T<1.58125,\qquad
             .8885625<-\Im T<1.0401875.
 \tag{12}
\]
Both rectangles lie strictly inside (1). The zero-neighbor case
is already contained there by (7).

These estimates hold for every partial segment as well: reducing
the length of the segment replaces the change by a factor in
\([0,1]\), which cannot worsen the displayed one-sided bounds.
Thus no continued root can reach the boundary of \(\Omega\).
Compactness and \(\Re G_t>0\) extend it to the whole segment.
Continuous dependence of the continuation equation on the target
neighbors gives a continuous chosen root on the parameter rectangle.
The implicit-function theorem at each endpoint makes this chosen
root locally holomorphic, with derivative (3). This proves the
claim without assuming uniqueness of unrelated roots of (2)
outside this continuation. \(\square\)

## 3. The fixed point is the original positive geometry

For a chain of length \(m\), set \(t_0=t_{m+1}=0\), and define
\[
       (\mathcal T(t))_v=T(t_{v-1},t_{v+1}),
                         \qquad 1\le v\le m.
 \tag{13}
\]
For \(m=1\) the two neighbors are both complete. For complex
numbers use the real-coordinate norm
\[
       |z|_\square=\max\{|\Re z|,|\Im z|\},\qquad
       \|t\|_\square=\max_v |t_v|_\square .
 \tag{14}
\]

**Theorem 2.** The map \(\mathcal T\) sends \(\Omega^m\) into its
interior and has Lipschitz constant at most \(5/8\) in (14).
It has exactly one fixed point there. This fixed point is the
original positive geometric solution with the two complete ends.

*Proof.* Lemma 1 proves preservation of the rectangle. Multiplication
by a complex number \(p+iq\), in the real-coordinate norm, has
operator norm \(|p|+|q|\). Equation (4) bounds this norm by
\(5/16\) for each noncomplete neighbor. Integrating along the
segment between two pairs of neighbors therefore gives
\[
 |T(u,w)-T(u',w')|_\square
 \le\frac5{16}\bigl(
       |u-u'|_\square+|w-w'|_\square\bigr).
 \tag{15}
\]
There are at most two changing neighbors. Thus \(\mathcal T\)
contracts by at most \(5/8\), independently of \(m\).
The closed product rectangle is complete, so iteration converges
to a unique fixed point.

It remains to identify its geometry. For an edge with both
endpoints selected, write \(r_{vu}=k_{vu}+ig_{vu}\).
Equations (1) and (5) imply
\[
       a_v+2|g_{uv}|<\frac{91}{50}+\frac65
                       =\frac{151}{50}<\pi,
 \tag{16}
\]
and the same inequality with the endpoints reversed. These are
exactly the two open-square conditions in the positive variational
domain. For an edge to a complete endpoint, the return based at
that endpoint is zero; the other return has imaginary part
strictly between \(-\pi/2\) and \(\pi/2\). Both required
inequalities hold there too. The real returns are positive.
Consequently the fixed point solves the original full logarithmic
equations inside their positive domain. Uniqueness of the positive
variational solution identifies it with the original marked
geometry. \(\square\)

Starting every selected vertex at \(t_*\) gives an explicit
approximation. The first change has norm less than \(7/20\)
by (7). Hence after \(k\) iterations,
\[
       \|t^{(k)}-t^{\rm geom}\|_\square
          \le\frac{14}{15}\left(\frac58\right)^k .
 \tag{17}
\]
This is an error estimate for the whole path, not an extrapolation
from computations on a few path lengths.

## 4. An explicit decay rate from the two ends

Put
\[
       q_{\rm geom}=\frac{8-\sqrt{39}}5,\qquad
                0<q_{\rm geom}<\frac9{25}.
 \tag{18}
\]
The two roots of \(q+q^{-1}=16/5\) are positive; (18) is the
smaller one.

**Corollary 3.** At every selected vertex of every such chain,
\[
       |t_v-t_*|_\square
        \le\frac12\left(q_{\rm geom}^{\,v-1}
                         +q_{\rm geom}^{\,m-v}\right)
        \le q_{\rm geom}^{\,\min(v,m+1-v)-1}.
 \tag{19}
\]

*Proof.* The rectangle (1) and enclosure (7) give
\(|t_v-t_*|_\square<1/2\) at either end. At every interior
vertex, (15) and \(T(t_*,t_*)=t_*\) give
\[
       e_v\le\frac5{16}(e_{v-1}+e_{v+1}),\qquad
                         e_v=|t_v-t_*|_\square.
 \tag{20}
\]
The first expression on the right of (19) satisfies equality
in this recurrence and is at least \(1/2\) at both ends.
If the difference between \(e_v\) and that expression had a
positive maximum, it would occur in the interior; (20) would
bound that maximum by \(5/8\) of itself, a contradiction.
For \(m=1\) the endpoint bound suffices. The last inequality
in (19) is immediate. \(\square\)

The local holomorphic formula for the edge Fourier coordinate,
given in
[the interior localization proof](research_three_path_interior_localization.md),
then gives explicit convergence after a neighborhood and its
derivative bound are fixed. The theorem does not assert that
the corresponding complementary Fourier integrals are small.
That remains a separate requirement in the full source problem.

## 5. Reproduction and scope

The derivative calculation is run with

    python3 experiments/certify_homogeneous_three_geometric_box.py --mesh 32 --max-boxes 50000

Its [record](../repro/results/research-homogeneous-three-geometric-box.json)
contains every accepted rational rectangle and the strict margins.
Then run

    python3 experiments/check_homogeneous_three_geometric_contraction.py

The [second record](../repro/results/research-homogeneous-three-geometric-contraction.json)
checks that these rectangles cover (1) exactly once, using an exact
rational sweep. It also checks the derivative program's hash,
the endpoint Rouché disks, the rational image bounds (11)--(12),
and the constants in the positivity and contraction arguments.
The continuation, contraction, and geometric identification are
the written arguments above. Neither calculation tests a volume
limit or a nonzero quantum coefficient.

The separate
[replayer](../experiments/replay_homogeneous_three_geometric_box.py)
imports no author code. It reconstructs every neighbor rectangle,
recomputes the analytic enclosures at higher precision, and checks
the parameter cover with a horizontal rational sweep. Run

    python3 experiments/replay_homogeneous_three_geometric_box.py --precision 160

The [completed replay](../repro/results/research-homogeneous-three-geometric-box-review.json)
checks all \(1797\) accepted parameter rectangles and all \(32^2\)
neighbor rectangles for each, without further subdivision. Its
cover consists of \(32\) horizontal slabs, each covered exactly
once. This verifies the derivative input; the role of that input
in the geometric theorem remains the explicit argument in Sections
2--4.
