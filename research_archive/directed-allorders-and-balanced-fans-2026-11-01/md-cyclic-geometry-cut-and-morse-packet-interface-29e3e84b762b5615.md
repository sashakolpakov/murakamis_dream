# Cyclic cuts and the marked Morse interface for balanced decorations

Private proof record, 1 November 2026. This separates three graphs:
the graph of tangle operations, the cubic matching graph of the cut
polyhedron, and the graph obtained by collapsing physical cycles in the
finite magnetic source. Their cycles have different meanings.

## 1. A limitation of the tree's octahedral page construction

Let \(G\) be a finite connected simple graph with \(V\) vertices and
\(E\) edges. Try to repeat literally the all-circle tree construction:
one octahedral ball per edge in each projection copy, and
\(d_v-1\) shaded page-face identifications at every vertex \(v\).
Assume the identifications have the prescribed disjoint triangular
faces and connect all the balls. There are
\[
S=\sum_{v}(d_v-1)=2E-V
\tag{1}
\]
such identifications. After truncating the ideal vertices, these are
gluings along disjoint boundary disks.

Glue first along a spanning tree in the graph of balls. Each step joins
two balls along one disk and leaves a ball. There are \(E-1\) such
steps. Each remaining disk-pair identification is then a one-handle
attachment. Consequently each projection piece is a handlebody of
genus
\[
S-(E-1)=E-V+1=b_1(G).
\tag{2}
\]
In particular one operation-graph cycle produces a solid torus rather
than a ball. Nevertheless the number of unglued shaded faces is
\[
4E-2S=2V,
\tag{3}
\]
exactly the expected two per circle. Face counts alone do not detect
the obstruction.

The literal projection/crossing-disk cut of a planar augmented diagram
gives two balls: each drilled boundary-parallel semicircle is opened
again along its actual half disk. Thus the above unmodified page
recipe cannot be identified with that cut when \(b_1(G)>0\). Extra
cutting disks and their return maps would be needed. This does not
prove that no cyclic construction is a link exterior in \(S^3\), nor
identify the manifold obtained by an arbitrary uncorrected quotient.

The cubic matching graph \(\Delta\) is different. With \(R\) circle
ports it has \(2R\) vertices and \(3R\) edges, and hence already has
\(b_1(\Delta)=R+1\) even for a tangle-operation tree. Its cyclic
finite source is the one in `general_matching_graph_full_normal_source.md`.
Those cycles are not the operation-graph cycles in (2).

## 2. Literal non-tree diagrams and their complete geometry

A simple triangulated white sphere, together with the supplied matching
of its dual triangles and an actual flat or Morse box diagram, determines
the two projection/disk cut balls. The primitive same-copy and
cross-copy face maps are the labeled maps of
`general_augmented_plat_matching_geometry.md`. Its positive labeled
right-angled certificate gives the actual augmented metric, with
\(\operatorname{Vol}(Y)=2\operatorname{Vol}(Q)\).

There are already arbitrary-size explicit plat families: the
\(O_kE_kO_k\) simple-white family in
`general_simple_white_plat_class.md`, and the one-end-layer family in
`general_one_end_layer_long_filling_volume.md`. The latter already has
a complete full long-filling theorem. The goal here is not to relabel
that existing result as open. It is to extend the sufficient balance
condition to decorated certified cores without assuming their source
is an operation-tree kernel product.

The two-sided construction in
`md-cyclic-geometry-balanced-terminal-fans.md` inserts only literal
terminal tangles in fixed product collars. It preserves the original
marked edge and complete circle curvatures, adds interstice disks, and
keeps a simple triangulated white sphere. Every inserted disk and its
oriented puncture paths belong to the resulting diagram. A new circle
is not an auxiliary comparison variable later removed from the target
manifold.

## 3. The exact source hypothesis that must be supplied

For the refined Morse diagram, retain the same complete module,
physical turns, actual cups/caps, and one original reduced mark. The
needed source statement, for arbitrary full local coupons, is
\[
I_N=\left[\prod_{f\ne u,v}L_f^{d}\right]
 \left.\prod_{e=1}^{R}H_{f_e(\Omega)R^{\epsilon_e}}
       (L_{x_e},L_{b_e},L_{c_e},L_{y_e})\right|_{L_u=L_v=0},
\qquad d=N-1.
\tag{4}
\]
The two faces \(u,v\) meet along the original marked MAIN edge. This
is a full-matrix statement, including repeated-root data, not a value
identity restricted to complete circle coupons.

The general Morse compiler in `research_matched_sphere_morse_source.md`
proves (4) from the literal adapter
\(N^{-1}H_e/(b_ec_e)^{d/2}\), the physical cup/cap formulas, and
the winding identity \(M_f-T_f=2\) on bounded faces and \(-2\)
on the exterior face. The local insertion changes middle-incidence
counts by
\[
\Delta M_b=-1,\qquad
\Delta M_x=\Delta M_y=1,\qquad M_w=1.
\tag{5}
\]
The corresponding turn changes must be read in the same inherited
frames; they are
\[
\Delta T_b=-1,\qquad
\Delta T_x=\Delta T_y=1,\qquad T_w=-1.
\tag{6}
\]
Then old demands are unchanged and the new ordinary face has demand
\(d\). An independent local tensor derivation of this step is being
kept separately; the downstream claims in this note use the literal
full identity (4), not an abstract equality of entropy functions.

The conserved integral head lattice is the cycle lattice of the
connected spherical diagram. Dual-path integration identifies it
primitively with face potentials modulo their common constant.
The even-level half-index coset is obtained by integrating the cochain
which is one on MAIN edges and zero on matching edges. Each triangle
contains two MAIN edges, so the cochain is closed; the sphere makes it
exact. Nonnegative homogeneous numerator degree \(dR\) leaves only
the target in (4). These facts use the embedding and full source
support, not a flat height ordering.

Applying the original full-Hermite functional separately to each
\(R^{n_e}\), with \(n_e=\epsilon_e-2p_e\), gives
\[
\begin{aligned}
I_{N,\mathbf n}={}&q^{d^2\sum_e n_e/4}(-i)^R
\sum_{\boldsymbol\ell\in(\mathbb Z\setminus\{0\})^R}
 \left(\prod_e\ell_e\right)(-1)^{(N+1)\sum_e\ell_e}\\
&\times\int_{[-1/2,1/2]^R}
 \left(\prod_e\sin(2\pi\delta_e)\right)
 S_N(-2\cos(2\pi\boldsymbol\delta))
 e^{N\sum_e(\pi i n_e\delta_e^2+2\pi i\ell_e\delta_e)}
 \,d\boldsymbol\delta.
\end{aligned}
\tag{7}
\]
Here \(S_N\) is (4) with the original spectral numerator at every
port. All half twists and framing/component scalars remain in their
original convention. Formula (7) is multilinearity in the local
matrices; it makes no claim that matrices at different ports commute.

## 4. The complete action and the local relative packet need no sweep

Assume (4) has been supplied for the literal refined diagram. The
following verifies the hypotheses of the existing packet proof, rather
than merely changing the word "plat" in its opening.

At the actual marked complete packing, put
\[
\Phi=\sum_e[F(x_e,b_e,y_e)+F(x_e,c_e,y_e)]
       -\sum_{f\ne u,v}\log L_f.
\tag{8}
\]
Every finite circle has total center angle \(2\pi\). Hence it is a
stationary point of (8). Its positive finite-face Hessian is
nondegenerate after fixing the common scale: the local positive
triangle Hessians identify adjacent finite-face variations, and the
simple sphere remains connected after deleting \(u,v\). The resulting
one-dimensional kernel before scale fixing is exactly common scaling.
This is the proof used in `actual_original_boundary_transverse_rank.md`;
Morse cups/caps do not add a face variable or a Hessian equation.

The absolute constant comes from the actual polyhedron, not a local
choice. For a shaded center triangle with angles \(\theta_j\),
\[
2\pi F-\sum_j\theta_j\log L_j
=2\sum_j\left[\Lambda(\theta_j/2)
                  +\Lambda((\pi-\theta_j)/2)\right].
\tag{9}
\]
The constant is fixed by \(F(x,0,0)=\tfrac12\log x\). Cone the
marked ideal vertex to the nonincident faces of the certified convex
polyhedron. The white and shaded facet contributions are exactly the
two Lobachevsky terms in (9); internal diagonals cancel. Summing the
actual facets and their \(2\pi\) angle sums proves
\[
2\pi\Phi=2\operatorname{Vol}(Q)=\operatorname{Vol}(Y).
\tag{10}
\]
The proof is the facet-coning argument in Section 6 of
`actual_original_boundary_stationary_character.md`, which explicitly
requires only the connected certificate and marked MAIN edge.

The local full CROSS/cofactor interpolation is unchanged: at every
port it gives the same \(N^2\mathcal B_{e,N}\) with exponential
relative error on a fixed complex chart of its positive nonzero
curvatures, with protected zeros fixed. The number of ports is fixed.
The Cauchy phase is therefore literally
\[
\Psi_N(z,\boldsymbol\delta)=
 \frac1N\sum_e\log\mathcal B_{e,N}(\delta_e;L(z))
 -\frac dN\sum_{f\ne u,v}\log L_f(z).
\tag{11}
\]
The finite phase includes every beta, midpoint, forced-product and
parity scalar. Uniform holomorphic convergence and the preceding
Hessian yield its selected saddle and determinant on one fixed
spectral polydisk.

Off the local common-phase neighborhood, an ordinary-face path has
two neighboring phases separated by a fixed amount. The actual
triangle cofactor containing that edge has the proved angular gap;
all other factors have their endpoint majorants. The simple sphere
connectivity and fixed graph size make this a global Cauchy-torus
gap. No flat gap forest appears. Local deformation of that exact
torus then gives the same nonzero relative packet, with Cauchy
dimension \(R-1\) and its original measure, as
`general_full_spectral_numerator_geometric_packet.md`, Sections 2--3.
This conclusion uses only the CROSS part and does not require a
previous theorem about the full remainder.

## 5. Global spectral and one-sided errors

The proof of `actual_global_cross_spectral_gap.md` is local weighted
cofactor analysis followed by the same shared Cauchy period. Each port
has \(x+y>0\) and at least one nonmonomial triangle, because the only
two zeros are adjacent along a MAIN edge, not its matching edge.
Thus a spectral coordinate bounded away from zero supplies a strict
loss. The global angular complement from Section 4 controls the
remaining face phases. This supplies the theorem's full real-cube
bound and thin complex strip, including endpoint and collision cases.

Now impose the true complete-radius balance at every port. The
original LEFT and RIGHT weighted envelopes are respectively
\[
\max\{\log c,F(x,b,y)+\tfrac12\log c\},\qquad
\max\{\log b,F(x,c,y)+\tfrac12\log b\}.
\tag{12}
\]
A zero overloaded middle kills that finite sector exactly. Otherwise
strict balance and \(F(x,t,y)>\tfrac12\log t\) make (12)
strictly smaller than the complete port action. Use the one shared
complete face torus in (4): each sector containing a one-sided port
is then bounded by \(e^{N(\Phi-\gamma)}\), with one fixed
\(\gamma>0\). There are finitely many sectors. The polynomial
spectral degree permits a fixed thin-strip extension, just as in
`general_complete_radius_balance_filling_volume.md`, Section 2.
No port has separately optimized radii.

Every source input of the entire all-CROSS theorem is now supplied:
the exact period (7), the nonzero local packet, the shared spectral
gap, and the actual source's primitive action. Its proof uses only
these inputs. Its whole-domain three integrations by parts keep the
second-derivative endpoint currents and control the infinite charge
tail. The finite remaining charges use the same original saddle
continuation. The one-sided remainder has an exponential bound below
\(\Phi\), while the filled first-charge rate tends to \(\Phi\)
as all fixed twists become independently long. Thus the same
independent-long quantifier is available, with a threshold depending
on this decorated diagram. No relative-growth restriction on the
twists is introduced.

## 6. Primitive geometry on the refined Morse diagram

The geometric verification also uses the actual Morse presentation,
not a hidden flat-plat replacement. From the stationary radii, solve
the marked line-circle equations with matching inversive distances
\(\cos(2\pi\delta_e)\). Their Jacobian is invertible by the same
finite-face Hessian and elementary triangle motion argument. This
gives one common nearby pattern with the original two marked lines.

For each white face let \(\mathcal R_f^\pm\) be its two
holomorphic reflection matrices, with
\(\mathcal R_f^-\mathcal R_f^+=I\). At an actual Morse slice
with regions \(F_0,\ldots,F_k\), set
\[
H_j=\mathcal R_{F_j}^+\mathcal R_{F_{j-1}}^-,\qquad
H_j\cdots H_1=\mathcal R_{F_j}^+\mathcal R_{F_0}^-.
\tag{13}
\]
Shared wire ends have the same regions and therefore the same based
head. At cups/caps the first and last regions agree, giving the full
inverse-pair relation. The prescribed shaded collar sends both
ordered input puncture generators to their output generators, while
preserving their product \(P=BA\). The source-selected eigenvalue is
\(J=-e^{-2\pi i\delta}\), and the primitive collar ratio is
\[
R_0=E_bE_c/D,\qquad
U=-\log R_0-\epsilon\log(-J),\qquad
V=2\log(-J)=-4\pi i\delta.
\tag{14}
\]
The matrix collar is the regular full divided difference
\[
C=I+\frac{R_0-1}{J-J^{-1}}(P-J^{-1}I).
\tag{15}
\]
Its value at the parabolic complete point is retained, not replaced
by the scalar eigenratio one. The auxiliary meridian follows
\(C^{-1}\), and the original signed half twist is the full Hurwitz
word with \(P^{-1}-I\). The ordered contacts, not just traces,
fix these choices. The common marked-line limit supplies every zero
face case. These are the local identities in
`actual_deformed_circle_primitive_collar.md`.

Equations (13)--(15) verify all shared wires, cups/caps, drilled
threading and half-twist relations in the actual Morse van Kampen
presentation, exactly as in
`actual_complete_core_geometric_deformation.md`, Section 2. Matching
graph cycles introduce no extra free conjugating frame because the
reflections were chosen on one global pattern. At zero this is the
complete representation of the refined link, from its own cut
certificate. Marked positive-gluing rigidity identifies the nearby
family as that same geometric germ.

For the ordinary-face stationary action
\[
A_\epsilon(\boldsymbol\delta)=
 \operatorname{crit}_{\text{finite faces}}
 \left\{\sum_e(Q_{b_e}+Q_{c_e})-
 \sum_{f\ne u,v}\log L_f+\pi i\sum_e\epsilon_e\delta_e^2\right\},
\tag{16}
\]
the primitive identities give \(\partial_eA_\epsilon=U_e\).
The complete anchor is (10). The same marked regulator calculation
therefore gives
\[
2\pi\operatorname{Re}A_\epsilon
=\operatorname{Vol}(\rho)
-\tfrac12\sum_e\operatorname{Im}U_e\operatorname{Re}V_e.
\tag{17}
\]
At the first-charge critical point of (7),
\[
U_e+p_eV_e=-2\pi i.
\tag{18}
\]
For independently sufficiently long fixed fillings this is the
primitive smooth-filling branch of the actual refined exterior.
The boundary term in (17) cancels the original Gaussian/linear
filling terms exactly. Hence the exponential rate is the volume of
that actual filled complement. There is no comparison-diagram
substitution and no inference from a formal critical value alone.

## 7. Precise resulting interface statement

Once the literal local full-source identity (4) for the insertion is
in place, the preceding arguments supply the packet, global spectral
gap, primitive geometric action and whole-period hypotheses directly
for the refined Morse diagram. They do not require moving every cup
and cap outside the boxes. Combining this interface with the balanced
fan construction gives a full independently-long fixed-filling volume
theorem for the decorated certified cores, with their prescribed knot
parity and original reduced normalization. This is the fixed-root
complete-main-color invariant. No deformation of the main meridian,
shifted microscopic chart, or annihilator-factor conclusion is supplied
by this argument.

This statement does not remove the source's cyclic magnetic labels,
prove a kernel product on an abstract cyclic graph, establish a
uniform threshold over cores, or prove the volume conjecture for an
undecorated core. It also leaves unaddressed cores without the supplied
simple-white positive geometric certificate. The finite source
interface and its geometric target are the substantive hypotheses;
an abstract entropy refinement alone would not provide them.
