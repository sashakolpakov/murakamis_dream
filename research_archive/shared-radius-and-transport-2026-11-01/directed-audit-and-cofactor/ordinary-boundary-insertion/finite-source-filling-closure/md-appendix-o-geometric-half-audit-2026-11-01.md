# Appendix O: bounded audit of the geometric contribution

This record concerns the public checkout at commit
164cb2c31ed788aa7375b18f2c3561cc445e6e2a. It reads Appendix O,
lines 631–1248, with targeted reading of the proofs listed in the
companion snapshot. It does not certify the preceding analytic half,
the exact finite source compiler, or the remainder estimate for the
full invariant. Those are separate dependencies.

The geometric argument checked here identifies the selected central
action with the volume of the original independently long-filled
link complement. Its knot conclusion additionally requires the
recorded terminal-pairing graph to have one component. It is not a
general full-source volume theorem.

## 1. Finding requiring a small repair

There is a mismatched Hessian reference, rather than a missing
geometric hypothesis.

Appendix O, lines 893–898, uses the complete logarithmic-curvature
Hessian. Its linked marked-pattern proof, lines 69–76, cites
actual_original_boundary_transverse_rank.md for this assertion.
That note proves the original magnetic/face-clock rank and a finite
q-Hahn reference Hessian. Its graph argument is applicable, but it
does not explicitly establish the complete triangle-curvature
Hessian used here.

The needed assertion has a short direct proof, given in Section 2
below. Inserting that calculation in O and replacing the marked-pattern
note's Hessian citation resolves the dependency without invoking
Appendix P's final theorem or any later volume result. The same
calculation is already displayed independently as equation
wb:hessian in P, before P's volume argument; it is also a possible
precise reference. A standalone proposed TeX insertion accompanies
this report.

I found no further correction in the assigned geometric implication
after tracing the actual local maps and the metric/fundamental-chain
comparison. This conclusion is bounded by the imported results and
proof segments explicitly identified below.

## 2. Direct complete Hessian and nondegenerate development

For an ordinary positive curvature \(w_i\), put \(q_i=\log w_i\).
In a complete triangle with at least two ordinary corners let
\[
 D_t^2=\sum_{\{i,j\}\subset I_t}w_iw_j,\qquad
 \theta_i=2\arctan(w_i/D_t).
\]
The omitted marked curvatures are zero. The source-normalized
triangle rate has gradient
\(\partial_{q_i}F_t=\theta_i/(2\pi)\). For distinct ordinary corners,
direct differentiation gives
\[
 \partial_{q_iq_j}F_t
 =-\frac{w_iw_j}{2\pi D_t(w_i+w_j)}
 =-\kappa_{ij}^{t}.
 \tag{H1}
\]
For three corners the simplification is
\(D_t^2+w_i^2=(w_i+w_j)(w_i+w_k)\). For two corners it is the
same identity with \(w_k=0\). Homogeneity gives zero row sums,
hence
\[
 h^{\mathsf T}\nabla^2 F_t h
   =\sum_{\{i,j\}\subset I_t}
       \kappa_{ij}^{t}(h_i-h_j)^2 .
 \tag{H2}
\]
A singleton triangle has rate \(\frac12q_i\) and zero Hessian.
Every ordinary edge of the triangulated sphere occurs in a triangle
with both endpoints ordinary, and its conductance in (H2) is
strictly positive.

Deleting adjacent vertices \(u,v\) from a simple triangulated sphere
leaves the ordinary graph connected. One direct proof reroutes a
path through the cyclic link of \(u\); it then reroutes any occurrence
of \(v\) through the link of \(v\) with \(u\) removed, which is
connected. These replacements introduce neither deleted vertex.
Thus the summed Hessian has precisely the constant kernel. A
linearized solution of the circle-distance equations has zero
angle-sum variation at every finite center, so its logarithmic
curvature variation, and therefore its logarithmic radius variation,
is constant.

At either triangle containing the marked edge \(uv\), a finite
circle is tangent to both fixed lines of separation one. Its radius
is \(1/2\); linearizing the two line equations forces its radius
variation to vanish. This removes the constant kernel.

For fixed radii, finite center triangles are nondegenerate and
infinitesimally rigid. A one-line triangle has fixed heights and
horizontal separation \(2\sqrt{r_fr_g}>0\); its only remaining
motion is a common horizontal translation. Removing the two
triangles at \(uv\) leaves a connected triangulated disk, containing
every finite vertex and a one-line triangle. Across a finite edge,
the two motions agree at two distinct centers. Across a line edge,
the two horizontal translations agree at the common finite center.
Propagation and the fixed horizontal normalization kill the last
motion. There are \(3R-1\) equations and variables, so the complete
Jacobian is invertible.

This proof checks the full circle-position system, not only a radius
stationarity system. The holomorphic implicit-function theorem
therefore applies with independently complexified \(X,Y,r\);
conjugation of parameters is not introduced. On small real
parameters the original cyclic orders persist. The local
angle-force identity, obtained by differentiating the displayed
center angles and channel rate, identifies this one global pattern
with the face saddle. Holomorphic continuation supplies the complex
identity. Positivity of a complex circle configuration is neither
claimed nor needed to construct its representation.

For the complete starting packing I read the fixed-boundary
construction in actual_smoothed_source_capacity_blocks.md §§3–5
and actual_balanced_terminal_fan_volume.md §2. Strict Hall
feasibility and exclusion of a boundary entropy maximum are
distinct steps. The latter moves toward a strictly positive
allocation; each newly positive zero corner has a positive
order-\(\varepsilon\log(1/\varepsilon)\) contribution, including
the limiting contribution adjacent to an angle \(\pi\).
The developed center triangles have trivial vertex holonomy.
Their convex triangular boundary has winding number one, so
positive local degree gives global injectivity. The disk-sector
argument then proves disjointness and strict remote support,
including across separating triangles. No arbitrary immersion
or unproved packing realization is substituted for this argument.

## 3. Original manifold, full group words, and primitive marking

The inverse-cut construction is an embedding in \(S^3\):
disjoint matched-dual-edge neighborhoods are four-terminal disks;
outside arcs are their embedded nonmatching edges; each disk gets
its original crossing circle in a disjoint ball. Untwisted physical
pairs are \((0,1),(2,3)\); the shaded grouping is
\((1,2),(3,0)\). These are different pairings. The odd physical
pairing is \((0,2),(1,3)\). The component test uses the physical
pairs and the outside matching, not the cycles of the shaded graph.

I read the actual cut reversal in general_augmented_plat_matching_geometry.md
§§1–6 and research_matched_sphere_morse_source.md §§1–4. Opening the
same boundary-parallel half disks after drilling cancels the added
handles in disjoint collars. This leaves two balls with the prescribed
medial boundaries even when the matched graph has cycles. The
white and shaded maps reverse these cuts. Canonical length-one
shaded horocycles remove edge dilation; four right angles remove
edge rotation. Thus the complete polyhedral quotient has the
original link topology and complete torus ends.

The complete action constant is not inferred from a volume
derivative. I read the actual facet-coning calculation in
actual_original_boundary_stationary_character.md §6. Its local
entropy constant is fixed by \(F(w,0,0)=\frac12\log w\); white
and shaded facet pyramids partition the same convex polyhedron.
Consequently
\[
 \Phi_D=\frac{\operatorname{Vol}(Q_D)}{\pi}
       =\frac{\operatorname{Vol}(Y_D)}{2\pi}.
 \tag{T1}
\]
The two-copy factor and the source factor \(2\pi\) are both retained.

The shared reflection prefixes in O(12) cancel at every
\(F,G,F\) cup or cap:
\[
 (\mathcal R_F^+\mathcal R_G^-)
 (\mathcal R_G^+\mathcal R_F^-)=I .
 \tag{T2}
\]
This is the specific reason the group assembly survives a changing
Morse head count. It is not a flat-plat assumption.

The primitive collar proof was read in full. Its contact map has
eigenvalues \(R_0,1\), where \(R_0=E_bE_c/D\). A product of the
two shaded reflections would instead have ratio \(R_0^2\);
using that product would give the wrong primitive meridian.
The selected \(J\)-line and the three contact/fixed-point images
make the matrix limit regular at \(J=-1\), including the common
marked-line regularization. The nontrivial parabolic limit is
retained, rather than replaced by the identity.

I independently expanded the chronological threading word
\([2,1,1,2]\). With \(P=BA\) and
\(K=P^{-1}C_{\mathrm{aux}}P\), its outputs are
\[
 (K^{-1}AK,\ K^{-1}BK,\ K).
 \tag{T3}
\]
Closing the auxiliary strand gives \(K=C_{\mathrm{aux}}\), hence the
physical pure transport is conjugation by \(C_{\mathrm{aux}}^{-1}\).
The two underpasses give the disk longitude \(BA\), with no
auxiliary self-writhe correction. This is the based-word input in
actual_augmented_plat_local_critical_character_map.md §4, not
only a trace comparison.

For the retained half twist let \(H=P^{-1}-I\).
Equal traces of \(A,B\) imply \(HB=AH\), and \(H\) commutes with
\(P\), so it gives \((A,B)\mapsto(A^{-1}BA,A)\).
On the selected line its eigenvalue is \(J^{-1}-1\), and
\[
 \det H=2-J-J^{-1}=(J^{-1}-1)^2(-J).
 \tag{T4}
\]
This verifies for both signs of \(\epsilon\) that O(16) has
selected eigenvalue \(m\) and determinant
\(m^2R_0(-J)^\epsilon=1\). It also checks the regular inverse
for \(\epsilon=-1\).

The actual head/box/cup/cap relations therefore define a framed
representation of the original augmented group. This conclusion
does not need the additional character-germ uniqueness paragraph
in the older global-assembly note. In particular no theorem
asserting a positive triangulation of an arbitrary filled knot
is used by this part of O.

## 4. Absolute regulator and filling-action calculation

The boundary formula O(19) needs the original oriented ideal
fundamental chain, its peripheral flags, and its primitive torus
rows. I read the written ingredients, rather than treating a named
regulator as an absolute volume:

* pointed_tetrahedron_gluing.md §§3–4 proves real edge-row rank
  and isotropy by tetrahedron/face cancellation;
* integral_half_longitude.md §2 proves the componentwise
  normal-curve intersection formula;
* general_marked_multicusp_gluing_rigidity.md §§1–3 assembles
  the \(2c\)-dimensional peripheral quotient and the actual
  shape/representation correspondence;
* bloch_lift_and_boundary_torsor.md §§1–3 derives the
  peripheral wedge and Bloch–Wigner differential;
* general_peripheral_representation_volume_bound.md §§1–2
  compares that same ideal chain with axis/parabolic cusp maps.

The knot-only integral half-longitude assertion is not required.
Over the real or rational shape space, edge rank is \(t-c\);
the primitive meridian/longitude pair on each torus has the
recorded pairing \(-2\), and different tori have zero pairing.
Thus the boundary identity is
\(-\frac12\sum m_i\wedge l_i\) for squared multipliers.
It yields precisely O(19). The oriented complete cut fixes the
absolute integration constant.

I independently checked the cancellation in O(24). Write
\(\delta=a+ib\). Since \(V=-4\pi i\delta\) and
\(U=-pV-2\pi i\), both sides of O(24) equal
\[
 4\pi pab-2\pi b.
 \tag{A1}
\]
Also \(d(2\pi i A_\epsilon)=-\frac12U\,dV\) gives
\[
 d(2\pi\operatorname{Re}A_\epsilon)
   =-\frac12\{\operatorname{Re}U\,d\operatorname{Im}V
              +\operatorname{Im}U\,d\operatorname{Re}V\},
 \tag{A2}
\]
which is exactly the differential of
\(\operatorname{Vol}(\rho)-\frac12\operatorname{Im}U\operatorname{Re}V\).
Together with (T1), this gives an absolute equality on the selected
small branch. It does not require an unknown period to be set to zero.

The sole source input to this geometric comparison is the specified
limiting local rate and its calibrated critical value. The analytic
claim that the original central period has that critical value with
nonzero amplitude remains an independent input from O's analytic
half. No equality for a noncentral sector is inferred.

## 5. Actual log periods and smooth metric completion

I read general_source_regulator_hyperbolic_equality.md §§1–6 in
full. The necessary hypothesis is closeness of the actual framed
representation to the complete one, not closeness of its traces.
O supplies this through its global matrices and holomorphic
selected flags.

The compact-core Lorentz average is equivariant and \(C^1\)-close
to the original development. The cusp affine average is a positive
local diffeomorphism on a compact fundamental parallelogram and
therefore everywhere by equivariance. Its vertical extension has
positive triangular differential on the entire end. The compact
collar interpolation is a local diffeomorphism after shrinking one
fixed neighborhood.

The sign assertion in O lines 1133–1138 is sufficient. More directly,
in the limiting chart write
\(\partial_e A_0=-2\delta_e B_{e,0}(\boldsymbol\delta^2)\)
with \(\operatorname{Re}B_{e,0}>0\). At unit charge,
\[
 \delta_e=-\frac{1/n_e}
       {1+iB_{e,0}/(\pi n_e)},\qquad
 \operatorname{Im}\delta_e
   =\frac{\operatorname{Re}B_{e,0}}
      {\pi n_e^2|1+iB_{e,0}/(\pi n_e)|^2}>0 .
 \tag{M1}
\]
This holds for either sign of \(n_e\). Hence
\(\operatorname{Re}V_e>0\): the auxiliary longitude multiplier
has nonunit modulus.

In its selected affine frame the second fixed point
\(q=b_\lambda/(1-a_\lambda)\) escapes to infinity, since the
original longitude translation \(b_\lambda(0)\) is nonzero.
The whole developed fundamental parallelogram, not only its
boundary, misses \(q\) for sufficiently small deformation.
Equivariance propagates this to the entire link cover.
The map \(\log(d_\rho-q)\) has nonsingular real differential.
Its invariant flat metric descends to a compact torus and is
complete. The developing local isometry is therefore the plane;
its periods are an injective rank-two lattice.

For the two fixed primitive generator paths the bound
\(L/(|q|-R)\) makes their actual logarithmic increments small.
Their differences from the prescribed small \(U,V\) are integer
multiples of \(2\pi i\), so those integers vanish. This comparison
is made before multiplying by the arbitrarily large \(p_e\).
It justifies the common neighborhood for independently unbalanced
signed fillings.

The explicit end contains the full tube epigraph, not just an
immersed torus. The period \(U+pV=-2\pi i\) is a primitive full
rotation with zero axial translation; a complementary period has
nonzero real part by rank two. Adding the axis is a smooth solid
torus with that exact meridian. The slope holonomy fixes both axis
endpoints and has multiplier one, so it is the identity.
Thus the representation descends to the filled group. This is
the step that excludes a nontrivial parabolic slope with unit
multiplier.

The remaining main cusps have two independent translations close
to the original ones; their ends are complete horoball quotients.
The compact part, finitely many completed tubes and ordinary
cusps give a complete finite-volume metric. A complete universal
developing local isometry covers \(\mathbb H^3\). No assertion
that an arbitrary exponentiated filling solution is geometric
has entered this argument.

## 6. The same-chain comparison with metric volume

O lines 1180–1188 explicitly retain the same boundary triangulation.
The imported proof has the quantitative homotopy needed here.
At the selected ideal endpoint, a conical cusp map has the form
\[
 f_{\mathrm{cone}}(w,Y)=(a(w),Yb(w)),\qquad b(w)>0.
\]
The axis map is \((0,Y e^{\chi(w)})\). On the common boundary
triangulation use
\[
 H_s(w,Y)=
 \bigl(s a(w),Y\exp((1-s)\chi(w)+s\log b(w))\bigr).
 \tag{C1}
\]
The functions and piecewise first derivatives on one fundamental
cross-section are bounded and \(b\) is bounded below. Horizontal
derivatives are \(O(1)\), the height and its derivatives are
\(O(Y)\), and the hyperbolic volume denominator is \(O(Y^3)\).
Hence the absolute boundary-homotopy volume is \(O(Y^{-2})\).
The affine transformation rules make (C1) equivariant.

The actual deformed end used for the metric is itself of this
conical form: set \(Y=e^t\), \(a=d_\rho-q\), and \(b=e^\chi\).
Thus the comparison applies to that end, as well as to a
face-compatible ideal-chain parametrization. Internal face
homotopies cancel with the same orientation.

After the boundary map has been moved to the axis, the primitive
slope is killed. Its vertex assignments factor through the solid
torus group and extend to the same boundary's filling
triangulation on the axis. Every added straight tetrahedron has
zero volume. The cutoff comparison tends to zero, so the
augmented regulator equals the filled representation's integral
volume on the same oriented fundamental class. The latter is
the constructed positive metric's volume. This is an absolute
chain comparison, not an inference from a volume derivative or
from putting unrelated new vertices on the axis.

## 7. Exact boundary of this audit

The hypotheses still needed are:

1. A fixed finite oriented simple triangulated sphere with at least
   four vertices, its actual dual perfect matching and cyclic
   quadrilateral orders, and a marked nonmatching edge.
2. The original disk-framed primitive bases and retained half-twist
   signs. The knot assertion needs the unchanged component test.
3. The written complete packing/support construction, its absolute
   source normalization, and the local channel/angle identities.
4. Fixed independently sufficiently long signed powers, so the
   first-charge point lies in the one complete framed neighborhood.
5. For the central asymptotic itself, the exact compiler and
   analytic packet/noncancellation theorem in the other half of O.
6. For a full invariant statement, an additional whole-source
   remainder estimate; O does not supply it for every sphere.

I read the topology, circle-rank, primitive-collar, peripheral
boundary-form, local metric, and same-chain proofs identified above.
I did not rerun symbolic or numerical scripts, verify every source
determinant asymptotic, or re-audit the contour/Hermite estimates.
The normal-curve and edge-row arguments were read at their written
finite algebraic proof level; they are not Lean-certified by this
record. Standard finite-dimensional implicit-function, degree,
covering, and differential/Stokes facts are used as stated.

There is no identified circular use of a full source-volume theorem:
the complete polyhedral anchor precedes the source asymptotic;
the group representation precedes the regulator comparison; and
the metric completion precedes replacing representation volume by
the filled complement's volume. The older global assembly's
additional geometric-germ uniqueness assertion is not needed
for these implications.
