# A calibrated terminal half-point gap on admitted neighbor rectangles

Research deduction, 5 November 2026. This note keeps the last conditional
kernel, ordinary endpoint coefficient and terminal Fourier weight together.
The accompanying outward record proves the finite arithmetic statement
below; its saved replay records independent verification. The scope is a
restricted boundary region, not the complete open-word contour.

## 1. The exact action comparison

Write \(\epsilon\in\{0,1\}\) for the last vertex type minus three,
and \(\nu\in\{0,1\}\) for the type of its external attached leg
\(a\). Use the original primitives
\[
 g(z)=\frac{\operatorname{Li}_2(e^{-2\pi iz})-\pi^2/6}{2\pi i},
 \qquad J(z)=g(z)-\frac{i\pi}{2}z(1-z),
 \qquad J'(z)=\operatorname{Log}(2\sin\pi z).
 \tag{1}
\]
The logarithms have their original zero lifts. Define
\[
\begin{split}
 Q_\epsilon(s;a,e)&=g(s+a)+g(s+e)-(2+\epsilon)g(s)+2\pi ias,\\
 F(e,u)&=-2J(1/2-u)-3J(u)-J(e-u)+i\pi eu,\\
 \mathcal X_\epsilon(a,e,t,u)
 &=Q_\epsilon(t;a,e)-g(a)-(1+\epsilon)g(e)+J(e)+F(e,u).
\end{split}
\tag{2}
\]
The exact terminal source is
\[
 C_{\epsilon,N}(e^{-2\pi ia},e^{-2\pi ie})
 H_N(w_R,e^{2\pi ie})\,
 d_N(e^{-2\pi ie})^\epsilon e^{2\pi iN\sigma e},
 \qquad \sigma\in\{0,\epsilon\}.
\tag{3}
\]
At the complete color and the original unaliased endpoint, its phase
is exactly (2). Indeed the three contributions are
\(Q_\epsilon-g(a)-g(e)\), \(J(e)+F(e,u_c(e))\), and
\(-\epsilon g(e)\). The last contribution must not be omitted.
Any allocated half-weight of the unchanged external leg is common to
the two sides and cancels.

Let \((e(a),t(a),u(a))\) be the original holomorphic map from
[open critical localization](research_mixed_open_word_critical_localization.md).
Direct differentiation of (2) gives its three original equations:
\[
\begin{split}
 \mathcal X_e&=-J'(e-u)+J'(e+t)-\epsilon J'(e)
        +i\pi[u-t+\epsilon(e-1/2)],\\
 \mathcal X_t&=J'(t+a)+J'(t+e)-(2+\epsilon)J'(t)
        +i\pi[a-e+\epsilon(t-1/2)],\\
 \mathcal X_u&=2\operatorname{Log}\cos\pi u
       +\operatorname{Log}\sin\pi(e-u)
       -3\operatorname{Log}\sin\pi u+i\pi e.
\end{split}
\tag{4}
\]
They all vanish at the map. Thus this is the original stationary
endpoint action, rather than a tangent-subtracted surrogate.

At the terminal half point set
\[
 e_h=1/2,\qquad u_h=1/4+i\log(3)/(4\pi),\qquad
 s_h(a)=s_*(a,1/2).
\tag{5}
\]
The exact endpoint equation gives \(F_u(e_h,u_h)=0\). The original
conditional root \(s_h\) is holomorphic on the independent source
rectangles in the
[right-square theorem](research_mixed_unselected_right_taper_products.md),
Theorem 1. Consider the holomorphic difference
\[
 D_\epsilon(a)=
 \mathcal X_\epsilon(a,e(a),t(a),u(a))
 -\mathcal X_\epsilon(a,1/2,s_h(a),u_h).
\tag{6}
\]
Its real part is harmonic. Criticality removes every unknown-map
response from its derivative:
\[
 D_\epsilon'(a)=g'(t(a)+a)+2\pi it(a)
              -g'(s_h(a)+a)-2\pi is_h(a).
\tag{7}
\]
In particular no derivative of the endpoint map is estimated numerically.

## 2. A finite boundary check in one complex variable

Use the closed rectangles
\[
 R_3=[.30,.39]+i[-.03,.02],\qquad
 R_4=[.27,.33]+i[-.057,-.001].
\tag{8}
\]
Every corner is strictly inside its original input disk
\(D_3=D(.35-.01i,.09)\) or
\(D_4=D(.30-.052i,.064)\). Both rectangles also lie in the
proved independent conditional source domain. Thus both terms of
(6) are holomorphic on a neighborhood of each rectangle.

**Theorem 1.** For both own types and both external types,
\[
                 \Re D_\epsilon(a)>1/100
                    \qquad(a\in R_{3+\nu}).
\tag{9}
\]

The check of (9) uses only the four sides of each rectangle. It reads
the four complete old endpoint trees, retaining precisely their leaves
whose closed rectangles meet those sides. Their side-incidence counts,
in own/external order \((0,0),(0,1),(1,0),(1,1)\), are
\[
 (11,10,33,17),\quad(26,15,30,16),\quad
 (10,10,20,17),\quad(15,13,16,16).
\tag{10}
\]
Corner incidences may share an old leaf. There are 275 incidences and
258 distinct retained leaves in total, with 67, 82, 53 and 56 leaves in
the four families. The checker exhausts all 10,978 old nodes and validates the 233
strict disk exclusions. The inclusion of (8) in the old input disks
ensures that no side point is in an excluded node.

On each retained whole parameter cell the original three-variable
endpoint disk is revalidated. The same old rational center and inverse
validate a radius-\(10^{-10}\) disk at its parameter midpoint.
For \(s_h\), the quadratic or cubic cotangent equation supplies only a
proposal. An original-log Newton disk verifies the entire cell and a
radius-\(10^{-10}\) midpoint disk. Its strict test is
\[
 |YQ_s(c;a,1/2)|+ho
       \sup_{|s-c|\le\rho}|1-YQ_{ss}(s;a,1/2)|<\rho.
\tag{11}
\]
The derivative supremum is enclosed on a square containing the disk;
the same contraction proves existence, uniqueness and holomorphic
dependence. Original sine-strip and cotangent-cone tests
\(\Re\cot(\pi s)>0\), \(|\Im\cot(\pi s)|<1\) identify the root with the
proved conditional branch. Saved replay supplies every rational
half-root center and radius and cannot propose or refine either tree.

At the midpoint the two values in (6) are enclosed directly. If the
cell's real and imaginary half-widths are \(h_x,h_y\), (7) yields
the outward lower bound
\[
 \Re D(a_0)-h_x\sup|\Re D'|-h_y\sup|\Im D'|>1/100.
\tag{12}
\]
This proves every boundary value. The harmonic minimum principle proves
(9) throughout (8). No new endpoint roots or parameter subdivisions are
used.

## 3. What the strict comparison controls

At \(e=1/2\) the actual Fourier polynomial has upper exponential
rate zero, and both terminal selected monomials in (3) have unit
modulus. The conditional kernel there has the complete right-square
packet; the endpoint coefficient has the complete half-point packet.
At the original endpoint graph the
[terminal conditional packet](research_mixed_terminal_conditional_packet.md),
the endpoint coefficient packet and the actual inverse-factorial
Fourier packet give the nonzero unaliased source. These are all original
finite functions, with every row and parity retained.

Consequently, uniformly for (8), the modulus of (3) at the half point,
for either \(\sigma\), is at most
\[
 \operatorname{poly}(N)\exp\left\{
 N\left[\Re\mathcal X_\epsilon(a,e(a),t(a),u(a))-1/100\right]
 \right\}.
\tag{13}
\]
This upper bound never divides by \(d_N(-1)\), which may vanish.
Relative to the nonzero unaliased source at the original endpoint,
any fixed smaller exponential gap, for example \(1/200\), follows
for all sufficiently large levels.

For a fixed open word of length \(m\ge2\) whose last external
critical leg belongs to the interior of (8), keep the remaining
coordinates in a sufficiently small unaliased real neighborhood of
their critical values, at their critical heights. Optimize the last
endpoint variables holomorphically. The original
[open Hessian](research_mixed_open_word_hessian.md) and its complex
Schur complement give
\[
 \Re\widehat\Phi_m(x)\le M_m-
       \frac{3\pi}{49}\|x-x_*\|_2^2.
\tag{14}
\]
The same conditional elimination and the exact phase identity from
[the local Gaussian theorem](research_mixed_open_local_gaussian.md)
identify the half-point phase with
\(\widehat\Phi_m(x)-D_\epsilon(a(x))\). Thus (9) retains the
remaining interior loss rather than discarding the boundary tangents:
\[
 \Re\Phi_{m,\mathrm{half}}(x)
 \le M_m-1/100-\frac{3\pi}{49}\|x-x_*\|_2^2.
\tag{15}
\]
All other outgoing variables remain unselected in this corollary.
By the genuine ambient source neighborhoods and compactness, a smaller
strict gap persists on a sufficiently small real terminal collar of
\(1/2\), and for sufficiently small ordinary-color perturbations and
their fixed derivatives. A single strict-gap tolerance covers the
polynomial prefactors. No leading coefficient of every derivative is
asserted nonzero.

The restrictions matter. The known open references can have neighboring
heights below \(-.057\); they are not covered by (8). Nor does (15)
control arbitrary motions of the remaining coordinates, the separate
terminal collar near angle one, or other selected outgoing variables.
In particular the whole-right angular reduction ends at a raw row
majorant at \(1/2\); that majorant can exceed the coherent conditional
phase used here. This theorem does not replace the raw half-point rate
by its coherent value or prove a loss on the entire right half.
Length one has no adjacent conditional kernel and is not a case of this
theorem. This supplies a calibrated local boundary loss, not a whole
open-source noncancellation or a new short-filling theorem.

## 4. Reproduction

    python3 experiments/check_mixed_terminal_half_endpoint_gap.py --precision 256
    python3 experiments/check_mixed_terminal_half_endpoint_gap.py --precision 320 --input repro/results/research-mixed-terminal-half-endpoint-gap.json --output repro/results/research-mixed-terminal-half-endpoint-gap-replay.json

The separate
[archived proposal diagnostic](../repro/diagnostics/2026-11-05-terminal-half-endpoint-gap/README.md)
is not an input to either outward check.
