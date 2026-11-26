# Whole-boundary decay for the proved path and graph sources

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

The full wide-kernel estimate upgrades the recently proved local
outside packets to whole-period bounds and quadratic complex strips.
The argument retains the original finite source and all its normals.
It supplies boundary control for later composition; it does not by
itself solve an arbitrary adjacent short component.

## 1. The original source and the covered classes

Use the exact source, crossing powers, and marking conventions of
one of the following proved theorems:

* [The path theorem, Theorem 4](research_uniform_path_trace_assembly.md#7-the-source-theorem-at-powers-seven-and-eight):
  positive powers at least seven with the stipulated complete outside
  endpoint, or signed powers of absolute value at least eight.
* [The branching theorem](research_degree_controlled_network_source.md):
  a fixed loopless same-index graph, allowing repeated edges, with
  \(|n_v|\ge\max(8,4d_v)\) at each selected vertex.
* [The degree-power theorem](research_network_degree_power_source.md):
  a fixed same-index graph, allowing loops and repeated edges, with
  \(n_v^2+d_v^2\ge4096\) at each selected vertex.
* [The hybrid theorem, Theorem 3](research_network_degree_power_source.md#8-mixing-the-degree-and-power-regimes-at-adjacent-vertices):
  a fixed same-index graph, allowing loops and repeated edges, in
  which each selected vertex independently satisfies either
  \(|n_v|\ge\max(8,4d_v)\) or
  \(\sqrt{n_v^2+d_v^2}\ge512\).

The degrees are the actual incidence degrees, with loops counted
twice. Each bullet is a separately proved source class. Only the
last permits the displayed vertexwise combination. In particular
the homogeneous degree-power threshold \(64\) is not substituted
for the hybrid threshold \(512\).

Let \(I\) be the nonempty selected set and let \(B\subseteq V\setminus I\)
be any set of unselected vertices whose angles will be left free.
Other unselected angles stay zero. Delete isolated outside vertices
from \(B\), since the source is independent of their angles.
With \(z_b=-2\cos u_b\), define the literal polynomial
\[
 F_N(\mathbf u)=
 \left(\prod_{v\in I}\phi_N^{(z_v)}R(z_v)^{n_v}\right)
                 \prod_{\{v,w\}\in E}K_N(t_v,t_w),
 \quad t_b=u_b\ (b\in B),\quad
 t_b=0\ (b\notin I\cup B).
 \tag{1}
\]
Products precede the selected traces. A loop occurs once as
\(K_N(t_v,t_v)\). Unselected variables are not reduced in the
Casimir quotient. Their actual degrees obey
\[
             \deg_{z_b}F_N\le d_b(N-1).
 \tag{2}
\]
Let \(M\) be the proved selected stationary action with every outside
angle complete. Put
\[
       \gamma=\frac1{100},\qquad
       \mathcal U(\mathbf x)=
                 \sum_{b\in B}d_b(1-\cos x_b).
 \tag{3}
\]

**Theorem 1.** In each of the stated classes, for every fixed
multi-index \(\alpha\) of ordinary outside-color derivatives,
\[
 \left|\partial_{\mathbf z}^{\alpha}F_N(\mathbf x)\right|
 \le C_\alpha N^{A_\alpha}
              e^{N[M-\gamma\mathcal U(\mathbf x)]},
                   \qquad \mathbf x\in[-\pi,\pi]^B .
 \tag{4}
\]
There are \(c,B_0,h>0\) such that the same original functions satisfy
\[
 \left|\partial_{\mathbf z}^{\alpha}
             F_N(\mathbf x+i\mathbf y)\right|
 \le C'_\alpha N^{A'_\alpha}
       e^{N[M-c\mathcal U(\mathbf x)+B_0|\mathbf y|^2]},
       \qquad |x_b|\le\pi,\quad |y_b|\le h.
 \tag{5}
\]
The constants may depend on the fixed graph and powers, but not
on the level. Both statements hold at both level parities.
Near \(\mathbf u=0\), the nonzero holomorphic packet is exactly
the one proved by the corresponding source theorem.

## 2. A loss for every free outside incidence

Write
\[
 \mathcal W=\{t:|\Re t|\le\pi/2,\ |\Im t|\le3/10\},
       \qquad \delta=\frac{21}{200}.
 \tag{6}
\]
The [wide edge theorem](research_bare_kernel_thin_rectangle.md#6-the-full-rectangle-through-real-angle-pi-over-two)
and [wide phase Hessian](research_path_mixed_trace_currents.md#9-vertical-current-monotonicity-at-powers-of-at-least-seven)
give, including every fixed ordinary derivative,
\[
 |K_N(t,u)|\le CN^A e^{N\Re\psi(t,u)},\qquad
 -\Re\psi''(t,u)\succeq\frac1{20\pi}I,
                       \qquad t,u\in\mathcal W .
 \tag{7}
\]
All derivatives here and below act on the corresponding ordinary
colors, not on an angle divided by a possibly vanishing sine.

For fixed complex \(t\in\mathcal W\) and real \(|u|\le\pi/2\),
separate evenness gives \(\psi_u(t,0)=0\). Twice integrating
the \(uu\) entry of (7) yields
\[
 \Re\psi(t,u)\le\Re\psi(t,0)-\frac{u^2}{40\pi}
       \le\Re\psi(t,0)-\gamma(1-\cos u).
 \tag{8}
\]
Indeed \(1-\cos u\le u^2/2\) and \(\pi<5\).
For real \(\pi/2\le|u|\le\pi\), the
[centered incidence theorem](research_path_mixed_trace_currents.md#8-a-stronger-centered-loss-for-a-removed-incidence)
gives exponent \(\Re\psi(t,0)-\delta\).
Since \(2\gamma<\delta\), it implies the same outside loss.
Thus a retained selected angle anywhere on its actual horizontal
or vertical contour satisfies
\[
 |K_N(t,u)|\le CN^A
       e^{N[\Re\psi(t,0)-\gamma(1-\cos u)]},
              \quad t\in\mathcal W,\quad u\in[-\pi,\pi].
 \tag{9}
\]
Both branches of this proof already include all fixed ordinary
derivatives in either color.

Suppose the selected neighbor is instead an original removed
physical row, of real angle \(t\) with \(|t|\ge T_N\).
The strict reserve in the centered theorem permits the physical
midpoint cutoff \(T_N=\pi/2+O(N^{-1})\) below \(\pi/2\).
If \(|u|\le\pi/2\), use the symmetric centered estimate
\(\Re\psi(0,u)-\delta\), followed by (8) with \(t=0\).
If \(|u|\ge\pi/2\), use its two-removed-endpoint bound
\(M_\infty-2\delta\). Both give
\[
 |K_N(t,u)|\le CN^A
       e^{N[M_\infty-\delta-\gamma(1-\cos u)]}.
 \tag{10}
\]
Thus the entire internal removal cost \(\delta\) survives, in
addition to the outside loss.

For an edge with two unselected endpoints, both angles can be
free. If both have magnitude at most \(\pi/2\), integrate
the full real Hessian in (7) from \((0,0)\):
\(\psi(u,v)\le M_\infty-(u^2+v^2)/(40\pi)\).
If only one is large, use the centered estimate and (8) for
the other. If both are large, use the double-removed estimate.
In every case,
\[
 |K_N(u,v)|\le CN^A
       e^{N[M_\infty-\gamma\{(1-\cos u)+(1-\cos v)\}]}.
 \tag{11}
\]
This also applies on the diagonal of an outside loop; its two
losses correspond to its two actual incidences. The same arguments
apply to all ordinary derivatives. A loop's diagonal derivatives
are finite sums of those mixed derivatives.

## 3. The original traces retain these losses

Use exactly the complete-outside contours and removed-row subsets
in the underlying source theorem. No new stationary point at a
distant real outside color is assumed. For a retained boundary
edge use (9), and for a removed boundary edge use (10). Edges with
no selected endpoint use (11). Edges entirely inside the selected
set keep their original estimates.

After these replacements, the remaining exponent is precisely
the complete-outside exponent of the proved source calculation,
minus \(\gamma\mathcal U(\mathbf x)\). Every horizontal, mixed
vertical, higher-charge, and removed-row estimate therefore
retains that same loss. In particular each removed incidence
still has its full \(\delta\) cost before the original
partial-charge action budget is applied.

All coefficients and orientations of the finite Hermite identities
are unchanged. For negative powers their reflected vertical-side
signs are retained, and the zero-power case uses its already proved
mixed-current estimate. First normals differentiate a finite
incident product; (9)--(11) and the interior bounds retain every
such derivative at polynomial cost. Odd simple-node terms remain
among the original physical rows. The number of terms and the
orders of derivatives are fixed independently of \(N\).
This proves (4), including its ordinary outside derivatives.

## 4. Why the complex strip has quadratic height growth

Here polynomial continuation alone would give a linear height cost.
Use both (4) and the proved local packet, as in the
[two-boundary Laurent argument](research_uniform_path_trace_assembly.md#5-boundary-sources-and-kernels).
We give the multivariable version with the literal degrees (2).

For the undifferentiated source put \(D_b=d_b(N-1)\), and express
it as a Laurent polynomial in \(q_b=e^{iu_b}\). The function
\[
 \left(\prod_{b\in B}q_b^{D_b}\right)
 F_N(\mathbf q)\,
       \exp\left[-N\gamma\sum_{b\in B}d_bq_b\right]
 \tag{12}
\]
is holomorphic on the closed unit polydisk. Its distinguished
boundary norm is at most
\(CN^A\exp N(M-\gamma\sum_bd_b)\), by (4).
Apply the maximum principle one variable at a time.
Separate evenness permits either sign of each height, so evaluation
at \(|q_b|=e^{-|y_b|}\) gives the upper exponential rate
\[
 M-\gamma\sum_bd_b+
   \gamma\sum_bd_be^{-|y_b|}\cos x_b+
                  \sum_bd_b|y_b|.
 \tag{13}
\]
The same conclusion holds for every ordinary derivative, since it
is again a separately even polynomial of degree at most (2) and
has the real bound (4).

Outside any fixed neighborhood of \(\mathbf x=0\), the quantity
\(\mathcal U(\mathbf x)\) has a positive minimum. Choose \(h>0\)
so small that the linear height terms in (13), including the
change \(1-e^{-|y_b|}\), are absorbed into half that real loss.
This gives (5) on this part of the real torus.

On a fixed small polydisk about zero, use the proved source
expansion
\[
 F_N(\mathbf u)=\varepsilon_N N^\nu
       a(\mathbf u)e^{NW(\mathbf u)}(1+O(N^{-1})),
       \qquad a(\mathbf u)\ne0,\quad \Re W(0)=M.
 \tag{14}
\]
The phase, amplitude and normalized remainder are holomorphic.
Taking pointwise exponential rates in (4) gives
\(\Re W(\mathbf x)\le M-\gamma\mathcal U(\mathbf x)\).
The branch is separately even, so \(\nabla W(0)=0\) and
\[
                  -\Re W''(0)\succeq
                         \gamma\,\operatorname{diag}(d_b)>0.
 \tag{15}
\]
Holomorphic Taylor expansion on a smaller neighborhood and Young's
inequality for the mixed real-imaginary quadratic terms give
\(\Re W(\mathbf x+i\mathbf y)
 \le M-c\mathcal U(\mathbf x)+B_0|\mathbf y|^2\).
The bounded local amplitude proves (5) there. All fixed ordinary
derivatives have the same exponential upper bound with polynomial
cost: apply Cauchy's formula on ordinary-color circles of radius
\(O(N^{-2})\) inside the packet domain. The phase is holomorphic
in those colors, including the ramified complete angles, so the
change of exponent is \(O(N^{-1})\). No nonvanishing derivative
of the leading amplitude is assumed. This proves the theorem.

## 5. Consequence for marked corridor composition

For a connected path whose only unselected vertex is one free
endpoint, \(e=m\) and \(\nu=0\). For a selected run between two
unselected endpoints, \(e=m+1\) and \(\nu=-3/2\), whether both
ends are free or one is kept complete. Equations (4)--(5)
and the unchanged nonzero local packet give exactly the boundary
source and kernel hypotheses of the existing finite-library and
long-turn composition theorems. A fixed finite collection has
common constants after taking smaller neighborhoods and strips.
This now applies at the positive-seven and signed-eight thresholds,
with their original geometric and complete-end qualifications.

The [exact corridor threshold criterion](research_affine_reduction_fibers_and_core_obligation.md#10-which-short-corridors-can-be-made-long-and-what-conjugation-preserves)
can therefore be used at \(K=7\) for its positive complementary
presentation with complete retained ends. For example, binary
negative corridors with endpoint runs of twos of length at least
five and internal runs of length at least four have an admissible
marked two-boundary source. Their fixed end twists and proper
rotations remain those of the exact tangle identity. The
[canonical boundary-crossing theorem](research_boundary_crossing_packet_preservation.md)
retains their chirp factors and full ordinary normals; it is
applied after the whole-period estimate has been established,
not to an arbitrary unproved short source.

The graph assertions concern the literal source (1). At an outside
vertex of degree greater than one, they do not assert that canonical
reduction to degree less than \(N\) preserves the same global angular
loss. Path endpoints have degree one and are already canonical, which
is the scope of the immediate admissibility conclusion above. Knot
and volume conclusions still use the underlying marked circle-tree
realization and component tests. This boundary upgrade neither
changes original assignment fibers nor resolves every fixed adjacent
short word.

The minimal exact checker
[check_network_whole_boundary_decay.py](../experiments/check_network_whole_boundary_decay.py)
verifies the two scalar loss comparisons, incidence degree accounting
with loops, and the original powers of \(N\). Its
[saved record](../repro/results/research-network-whole-boundary-decay.json)
records the proof dependencies. It does not replace the contour,
source, or Laurent arguments above.
