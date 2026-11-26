# A compact descent contour from the original primitive periods

Private written proof, 15 November 2026.

Suppose a fixed short partial filling has a positive solution in the
original circle-tree edge decomposition. Its primitive-period map has
a canonical inverse on a real slice. The entire real slice need not be
in its image. Nevertheless the original convex angle energy constructs
a bounded, star-shaped inverse domain around the solution, with a
constant strict action loss on its boundary. This is a theorem about
the actual classical source action and its peripheral marking. It does
not identify this contour with the original finite quantum cycle.

## 1. Fixed original data and the compact angle problem

Fix an original ordered circle tree, a nonempty selected set \(S\)
of size \(k\), and every edge incident to \(S\), counted once.
Write \(m\) for the number of included edges. Every selected vertex
has positive original degree. Fix the full complex angles at the outside
endpoints, the original real signed crossing powers \(n_v\), and the
primitive unit charges. In a physical integral filling,
\(n_v=\eta_v-2p_v\), with the original carrier \(\eta_v\).

Use the canonical positive edge branches of
[the global monotonicity theorem](research_positive_edge_global_monotonicity.md).
At an endpoint write
\[
 t_v=s_v+i h_v,\qquad r_{v,e}=k_{v,e}+i g_{v,e}.
 \tag{1}
\]
Before matching imaginary angles, use one \(h_{v,e}\) per incidence.
For an oriented edge \(e=(v,w)\), its two positive square factors
have coordinates
\[
 \begin{aligned}
 A_P&=s_v/4-g_{w,e}/2,& A_Q&=s_v/4+g_{w,e}/2,\\
 y_P&=g_{v,e}/2+s_w/4,& y_Q&=g_{v,e}/2-s_w/4.
 \end{aligned}
 \tag{2}
\]
Each coordinate lies in \((-\pi/4,\pi/4)\). Equivalently,
\[
 |s_v|+2|g_{w,e}|<\pi,\qquad
 |s_w|+2|g_{v,e}|<\pi.
 \tag{3}
\]
The outside \(s_b,h_b\) are prescribed. The selected constraints are
\[
       \sum_{e\ni v}g_{v,e}-\frac{n_v}{2}s_v=-\pi
                         \qquad(v\in S).
 \tag{4}
\]
Let \(\mathcal P\) be this open feasible polytope in the selected
\(s_v\) and all incidence \(g_{v,e}\), and let \(\overline{\mathcal P}\)
be its closure. Boundaries and interiors below are relative to its
affine constraint space. We assume that the original primitive
equations have a positive solution \(t^0\); in particular
\(\mathcal P\) is nonempty.

There is no zero-dimensional case under these hypotheses. The \(k\)
constraints (4) are independent, since each contains incidence
variables belonging to its own selected vertex. The affine space has
dimension \((k+2m)-k=2m>0\). Its projection to the selected \(s\)
coordinates is surjective: any infinitesimal change of \(s_v\) can
be offset in one incidence variable at that vertex. Strict feasibility
therefore gives the full local \(k\)-dimensional period problem.
The empty selected set is excluded throughout.

For one square let
\[
 \begin{aligned}
 x(A,y)&=\tfrac12\operatorname{arsinh}(\tan(2A)\cos(2y)),\\
 B(A,y)&=\tfrac12\operatorname{arsinh}(\tan(2y)\cos(2A)),\\
 dE_\square&=x\,dA+B\,dy,\qquad E_\square(0,0)=0.
 \end{aligned}
 \tag{5}
\]
These are real single-valued functions on the open square. The existing
variational theorem proves that \(E_\square\) is strictly convex,
extends continuously to its closed square, and has the edge identity
\[
 4\,dE_e=k_{v,e}\,ds_v+k_{w,e}\,ds_w
                   +h_{v,e}\,dg_{v,e}+h_{w,e}\,dg_{w,e},
 \qquad E_e=E_{\square,P}+E_{\square,Q}.
 \tag{6}
\]
Define the original energy, with the outside imaginary angles retained,
\[
 \mathcal E=4\sum_eE_e-
                   \sum_{b\notin S}h_b\sum_{e\ni b}g_{b,e}.
 \tag{7}
\]
It is continuous on the compact polytope, strictly convex in its
interior. Let \(z_0\) denote the angle assignment of \(t^0\).
The original variational theorem says that \(z_0\) is its unique
global minimum, including against boundary assignments.

## 2. The exact real-period image and its boundary completion

For \(\xi\in\mathbb R^k\), introduce only a linear tilt:
\[
 \mathcal E_\xi(z)=\mathcal E(z)-\sum_{v\in S}\xi_v s_v(z),
 \qquad z_\xi=\operatorname*{argmin}_{\overline{\mathcal P}}
                                                    \mathcal E_\xi.
 \tag{8}
\]
The minimizer is unique for every \(\xi\). Here the existing boundary
proof applies unchanged: a square on an open side has inward energy
derivative \(-\infty\), while an interior square or a corner has a
finite derivative along a line to a strictly feasible assignment.
Adding the linear term in (8) cannot remove that contradiction.
Thus every square factor of a boundary minimizer is either interior
or a corner. Uniqueness follows from strict convexity along a segment
between distinct minimizers; if the only differing factors join
adjacent corners, their midpoint would instead be an excluded
open-side minimizer. Existence follows from compactness.

The map \(\xi\mapsto z_\xi\) is continuous on all of
\(\mathbb R^k\). Indeed, for \(\xi_j\to\xi\), any convergent
subsequence of the compact minimizers minimizes \(\mathcal E_\xi\)
by passage to the minimum inequality. Uniqueness identifies its
limit with \(z_\xi\), proving continuity of the whole sequence.

Define the actual period map and its real image by
\[
 P_v(t)=\sum_{e\ni v}r_{v,e}(t)-\frac{i n_v}{2}t_v,
 \qquad J=\frac{\partial P}{\partial t},
 \qquad
 \Xi=\{\xi\in\mathbb R^k:z_\xi\in\mathcal P\}.
 \tag{9}
\]

**Proposition 1.** The set \(\Xi\) is open and contains zero.
It is exactly the set of \(\xi\) for which the original positive
domain, with its fixed outside angles, contains a solution of
\[
                              P(t)=\xi-\pi i\mathbf1.
 \tag{10}
\]
That solution \(t(\xi)\) is unique and real analytic. At any finite
boundary point \(\xi_*\in\partial\Xi\), the completed assignment
\(z_{\xi_*}\) has at least one corner factor and no open-side
factor. Every approach from \(\Xi\) converges to that same angle
assignment. The reconstructed complex angles can diverge at a corner;
their boundedness is not asserted.

**Proof.** Attach multipliers \(h_v\) to (4). Stationarity of (8)
in the incidence variables gives
\(h_{v,e}=h_v\) at selected vertices and
\(h_{b,e}=h_b\) at outside vertices. Stationarity in \(s_v\) gives
\[
                    \sum_{e\ni v}k_{v,e}+n_vh_v/2=\xi_v.
 \tag{11}
\]
Together with (4), these are exactly (10). Conversely a positive
solution gives an interior stationary point and hence the unique
global minimizer of (8).

The original edge monotonicity gives \(\operatorname{Re}J>0\),
with \(J\) complex symmetric. It is therefore invertible.
The implicit-function theorem gives openness and real analyticity;
global uniqueness also follows directly from strict monotonicity.
If a finite boundary point had an interior minimizer, this same
theorem would put a neighborhood in \(\Xi\). It must therefore
have a corner, by the preceding boundary exclusion. Continuity of
the unique closed minimizer proves the asserted limit. \(\square\)

Thus (8) gives an exact global description of the image slice by a
fixed compact convex problem. It does not assert that \(\Xi\) is
all of \(\mathbb R^k\), convex, or star shaped. Finite image
boundaries are possible corner degenerations of the original cells.

## 3. The calibrated action equals a constant minus the angle energy

Let \(M_\infty=\psi(0,0)\), with the original edge normalization,
and retain the primitive-charge action
\[
 F(t)=\sum_{e=vw}\psi(t_v,t_w)
                  +\frac{i}{4\pi}\sum_{v\in S}n_vt_v^2
                  -i\sum_{v\in S}t_v.
 \tag{12}
\]
The outside arguments are the fixed original boundary angles. As in
the original trace calculation,
\[
                  F_t=-\frac{P+\pi i\mathbf1}{\pi}.
 \tag{13}
\]

**Proposition 2.** At every point of \(\Xi\), with the canonical
positive logarithms,
\[
       \boxed{\quad
       \operatorname{Re}F(t(\xi))
                  =mM_\infty-\frac{\mathcal E(z_\xi)}\pi.
       \quad}
 \tag{14}
\]
The constant is the same on all components of \(\Xi\).

**Proof.** On one positive edge,
\(\psi_{t_v}=-r_{v,e}/\pi\). Hence
\[
 d(\pi\operatorname{Re}\psi)
              =\sum_{j=v,w}(-k_{j,e}\,ds_j+g_{j,e}\,dh_j).
\]
Combining this with (6) gives the exact identity
\[
        \pi\operatorname{Re}\psi+4E_e
                     -g_{v,e}h_v-g_{w,e}h_w=\pi M_\infty.
 \tag{15}
\]
Its differential vanishes. The positive edge domain is the connected
two-disk domain of the original coordinate theorem, and its complete
value fixes the displayed constant. Thus this is a global identity
on that positive domain, not a choice of a constant on an inverse
period component.

At an interior minimizer, all imaginary angles match. Sum (15) and
subtract the outside term in (7). Equation (4) gives
\[
 \mathcal E=\pi mM_\infty-\pi\operatorname{Re}\sum_e\psi
                  +\sum_{v\in S}h_v(n_vs_v/2-\pi).
\]
Since \(\operatorname{Re}(i n_vt_v^2/(4\pi))=-n_vs_vh_v/(2\pi)\)
and \(\operatorname{Re}(-it_v)=h_v\), this is exactly (14).
\(\square\)

In particular \(t^0\) is the unique global maximum of
\(\operatorname{Re}F\) on the entire inverse-period slice, not
only on its component containing \(t^0\).

For the differential form of the result, define the finite convex
conjugate
\[
 \mathcal C(\xi)=\max_{z\in\overline{\mathcal P}}
                                 \{\xi\cdot s(z)-\mathcal E(z)\}.
 \tag{16}
\]
Uniqueness and continuity of the maximizer imply
\(\mathcal C\in C^1(\mathbb R^k)\), with
\(\nabla\mathcal C=s(z_\xi)\). This follows directly by sandwiching
its difference quotient between the two maximizing linear forms.
On \(\Xi\) it is real analytic and
\[
 \nabla^2\mathcal C=\frac{\partial s}{\partial\xi}
      =\operatorname{Re}(J^{-1})>0,
 \qquad
 \operatorname{Re}(J^{-1})
      =J^{-*}(\operatorname{Re}J)J^{-1}.
 \tag{17}
\]
Here the real part is the Hermitian part, equal to the entrywise real
part for these symmetric matrices. Along a ray inside \(\Xi\),
\[
 \frac{d}{dr}\mathcal E(z_{r\omega})
     =r\,\omega^{\mathsf T}\operatorname{Re}(J^{-1})\omega>0
                                 \qquad(r>0,\ |\omega|=1),
 \tag{18}
\]
and the action derivative is minus this expression divided by \(\pi\).
Equivalently its exact loss is
\[
 \operatorname{Re}F(t^0)-\operatorname{Re}F(t(\xi))
       =\frac{\mathcal C(0)-\mathcal C(\xi)
                               +\xi\cdot\nabla\mathcal C(\xi)}\pi.
 \tag{19}
\]

## 4. A bounded star-shaped domain with a strict boundary gap

The compact angle problem supplies a positive number
\[
 \Delta=\min_{z\in\partial\mathcal P}\mathcal E(z)
                                      -\mathcal E(z_0)>0.
 \tag{20}
\]
Strict positivity follows from continuity and the unique interior
minimum. This is a boundary-energy quantity in the specified original
polytope; no computable lower bound is assumed.

**Theorem 3.** For every \(0<\delta<\Delta\), the set
\[
 \Omega_\delta=
       \{\xi\in\mathbb R^k:
                \mathcal E(z_\xi)<\mathcal E(z_0)+\delta\}
 \tag{21}
\]
is a bounded open strictly star-shaped domain with smooth boundary.
Its closure lies in \(\Xi\). Every ray has a unique boundary radius
\(\rho_\delta(\omega)>0\), depending smoothly on its direction.
Its inverse image
\[
                         \Gamma_\delta=t(\Omega_\delta)
 \tag{22}
\]
is an embedded real \(k\)-dimensional contour with compact closure
in the original positive domain. It has its unique action maximum
at \(t^0\), and
\[
 \operatorname{Re}F\big|_{\partial\Gamma_\delta}
              =\operatorname{Re}F(t^0)-\delta/\pi.
 \tag{23}
\]

**Proof.** The closed angle sublevel
\(K_\delta=\{z:\mathcal E(z)\le\mathcal E(z_0)+\delta\}\)
is compact and contained in \(\mathcal P\). Thus every minimizer
occurring in (21), or at equality, is interior and reconstructs a
regular matched positive point.

The inverse-period parameters of those minimizers are bounded. To
see this without assuming properness of the whole period map, choose
one incidence at each selected vertex and reconstruct its imaginary
angle using (5) and the original square formulas. These are smooth
on the compact set \(K_\delta\). At every interior minimizer all
incidences give the same angle. Formula (11) then expresses its
\(\xi\) as bounded smooth functions of that compact angle data.
Consequently the set defined by the weak inequality in (21) is
bounded and closed, hence compact and contained in \(\Xi\).

There is also global monotonicity along each parameter ray, including
after a possible exit from \(\Xi\). For \(0\le r_1<r_2\), the two
minimum inequalities from (8) imply
\[
 \omega\cdot(s_2-s_1)\ge0,\qquad
 r_1\omega\cdot(s_2-s_1)
       \le\mathcal E(z_{r_2\omega})-\mathcal E(z_{r_1\omega})
       \le r_2\omega\cdot(s_2-s_1).
 \tag{24}
\]
Thus the energy cannot decrease along the ray. Before the level in
(21) is reached, the minimizer is interior and (18) makes it strictly
increasing for \(r>0\). The ray must reach that level at a finite
radius: otherwise its parameters would lie in the bounded weak
sublevel just proved. Continuity and strict increase give exactly
one first radius. There is no later equality interval: the first
level point lies in the open set \(\Xi\), so (18) gives an immediate
strict increase there, followed by the nondecrease in (24).

At that radius the radial derivative in (18) is positive. The implicit
function theorem therefore makes \(\rho_\delta\) smooth; for
\(k=1\) this means the two positive endpoint radii. This proves all
assertions about \(\Omega_\delta\). Injectivity and nonsingularity
of the period map prove the embedding in (22). Compactness of its
closure follows from the same reconstruction on \(K_\delta\).
Finally (14) gives (23) and the unique maximum. \(\square\)

At the center the real phase curvature in \(\xi\) coordinates is
\(-\operatorname{Re}(J(t^0)^{-1})/\pi\), which is negative definite.
On each compact annulus of this contour the action has a positive
gap. If the original core signs satisfy \(\operatorname{Im}t_v^0<0\),
then sufficiently small \(\delta\) makes the entire closed contour
lie in the lower poly-half-plane: compact angle sublevels shrink to
their unique minimizer as \(\delta\downarrow0\).

All these finite-contour assertions persist for sufficiently small
complex changes of the prescribed outside angles. On a compact
closed contour, the holomorphic inverse-function theorem applies
uniformly to (10); the continued contour and critical point retain,
for example, half of the strict boundary gap in (23). The statement
uses the same continued primitive logarithms, not newly selected
endpoint branches.

## 5. What this does not prove about the original finite source

Finite boundary points of the full image \(\Xi\) are accounted for
by its unique corner minimizers. If \(|\xi|\to\infty\), a sequence
of interior minimizers cannot remain in a compact subset of
\(\mathcal P\), by (11). Neither fact asserts that the full inverse
slice is a proper integration cycle with integrable ends. Indeed
\(\mathcal E\) is bounded on the closed polytope, so (14) by itself
does not make the action tend to \(-\infty\) along an infinite end.

Theorem 3 avoids this issue by constructing a finite compact collar.
For the original finite source, one must still match its boundary to
the actual trace endpoints, control the connecting faces and vertical
currents, and justify the complete edge-kernel asymptotics on the
deformation. Its being a descent contour for the calibrated classical
phase does not supply those facts or its relative homology coefficient.
The original lattice modes and peripheral scalar factors are unchanged.

This limitation is substantive even inside positive edge charts.
The [actual full-wire obstruction](research_all_three_edgewise_contour_obstruction.md)
proves that on positive all-three path fillings the full individual
wire kernel can have a strictly larger rate than its geometric packet.
Its dominant endpoint products can then vanish after the original
adjacent Hermite traces. Thus neither an edgewise smaller remainder
nor a competing rate for the whole contraction follows from the
positive classical contour; the full source must be treated coherently.

The [local coefficient theorem](research_primitive_filling_local_gaussian_unit.md)
supplies a nonzero primitive Gaussian coefficient when its regular
chart conditions hold. Together, the two results give a local block
and a compact classical contour with a strict boundary action gap.
They still do not identify the entire selected scalar with that block,
exclude cancellation from the remaining source, or cover a short
hyperbolic filling outside the original positive decomposition.

## Pinned direct sources

* `notes/research_positive_edge_global_monotonicity.md`, SHA256
  `da5129c7110190035eedb8249d4004dd06b5a7555e78d948234d8de50fa17500`:
  the full positive two-disk coordinates, canonical branches, exact
  meridian increments, global strict monotonicity and accretive
  primitive-period Jacobian for arbitrary real signed powers.
* `notes/research_positive_filling_convex_variation.md`, SHA256
  `2777b2bcb149d64a79757ba64ccb16be5438cf37ce820ad50c5f532afd8fc6c0`:
  the square energy, exact differential (6), original angle constraints
  and boundary term, compact continuous extension, exclusion of open
  sides and uniqueness of the closed minimizer. The present proof
  adds real-period tilts, the global calibrated action identity and
  compact inverse-period contours.
* `notes/research_primitive_filling_local_gaussian_unit.md`, SHA256
  `daff63f379f9a037fc69f67503b69eef6a749e305592f10a10644dc155779b92`:
  the original primitive-charge action and its exact finite trace
  normalization, and the separate local Gaussian-unit statement.
* `notes/research_all_three_edgewise_contour_obstruction.md`, SHA256
  `39008a1b4a95ec5b21caeea7a4abaa7972795050b82a1415ce8aef7dcdd495b0`:
  the actual positive-chart full-wire obstruction and exact adjacent
  endpoint cancellation used solely to delimit the source conclusion.

Only written proofs and source-text reads enter this note. No
mathematical code, numerical calculation, test or compilation was run,
and no frozen manuscript or other note was edited.
