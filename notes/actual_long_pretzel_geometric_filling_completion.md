# Positive geometric deformation and smooth filling of the selected source

**Subsequent quantum scope extension.** The [improved full-color bound](actual_pretzel_all_width_extension.md)
lowers the required odd width to s>=9. The geometric argument below
already applies there and is unchanged. Its diagram-independent
generalization is [the general geometric theorem](general_source_regulator_hyperbolic_equality.md).

29 October 2026. The selected long-filling representation is realized
by a complete, positively oriented finite-volume hyperbolic metric
on the ACTUAL filled pretzel complement. The construction starts
with the explicit four-antiprism cellulation and uses finite face
and cell centers. It does not assume that an arbitrary ideal
topological triangulation has a positive geometric realization.

Together with the already proved full original-source asymptotic
and marked regulator comparison, this gives full hyperbolic-volume
equality for every fixed odd width \(s\geq25\), with all signed
twist parameters independently sufficiently large and fixed before
\(N\to\infty\). The proof below identifies the selected
representation geometrically; a representation-volume UPPER bound
or convergence of its volume alone would not prove this conclusion.

## 1. The precise geometric and source inputs

The [explicit augmented geometry](actual_augmented_pretzel_geometric_volume.md)
constructs the original half-twisted augmented link from two
convex ideal polyhedra \(\mathcal P_s\), each the double of an
ideal right-angled antiprism. Its labeled face pairings, edge
cycles and cusp tori are those of the original source, and the
complete volume is \(V_s\).

The [literal port and anchor theorem](actual_pretzel_port_lift_and_geometric_anchor.md)
supplies a family \(\rho_z\) of representations of that ACTUAL
augmented-link group, with its specified main and auxiliary
peripheral eigenflags. It proves:

* \(\rho_0\) is the positively oriented complete geometric
  holonomy, by every white and both shaded face maps;
* the main meridian stays noncentral parabolic;
* the auxiliary meridians and preferred disk longitudes are
  \(C_i,P_i\), with a common specified eigenflag and the
  retained SL sign;
* the selected source filling point approaches this complete
  point uniformly as \(\max_i|p_i|^{-1}\to0\), and kills exactly
  the primitive slopes \(\mu_i+p_i\lambda_i\) in PSL(2,C).

This family is a direct verified group/peripheral construction,
not an inference from a scalar eigenphase or an unspecified
character-variety component. The original cap order and the
orientation-preserving reverse traversal are retained.

The [primitive-period theorem](actual_long_pretzel_primitive_filling_angle.md)
fixes the continuous LOG SIMILARITY holonomies near completeness:

\[
 U_i=\operatorname{Log} M_i^2=-z_i,\qquad
 V_i=\operatorname{Log}\lambda_i^2\text{ centered at completeness}=-2\ell_i,
\]
\[
 U_i+p_iV_i=-2\pi i m_i,\qquad |m_i|=1.              \tag{1}
\]

The source's selected all-unit charge, not just its exponentiated
relation, is used in (1). The SL longitude sign is not counted as
an additional uncentered \(2\pi i p_i\).

## 2. A fixed positive triangulation of the ACTUAL complete cellulation

Choose a finite point \(O_P\) strictly inside each of the two
convex complete polyhedra. For every paired original face, choose
one finite point \(F\) in the relative interior of one face and
put the center of its partner at the point prescribed by that
face isometry. This is one choice per face ORBIT, not two
unrelated choices. Each original face is a convex ideal polygon.
Join its center to every ideal edge, and cone every resulting
triangle to \(O_P\).

The resulting finite tetrahedra have vertices

\[
 (O_P,F,v_j,v_{j+1}),                                \tag{2}
\]

with two finite and two ideal vertices. Every tetrahedron is
strictly positive with its cell's induced orientation: \(F\)
is interior to its face, \(v_jv_{j+1}\) is an edge, and \(O_P\)
is strictly on the inner side of that face plane. Convexity makes
these face fans and cones a decomposition of the original
polyhedron. The paired face fans match EXACTLY, including shaded
outer-label exchanges. There are \(24s\) tetrahedra in the two
polyhedra. Their only ideal vertices are the original cusp lifts.

This is a geometric triangulation of the actual complete manifold,
allowing finite vertices. No assertion about a positive all-ideal
subdivision is needed. Finite centers may, for example, be chosen
by normalized positive Lorentz sums of ideal vertex lifts in a
chosen face/cell and then transferred to a paired face by its
isometry. All choices are fixed before deformation.

## 3. Equivariant deformation gives a locally hyperbolic core

Work in the topological universal cover of this fixed triangulation.
Choose one representative of each FINITE vertex orbit and give it
its old finite point, or any continuous nearby point. For every
other lift define its position by \(\rho_z\)-equivariance.
Finite vertices have trivial deck stabilizer, so this assignment
is well defined. Assign each ideal vertex its specified peripheral
fixed flag, and propagate it equivariantly. This is well defined
because its entire peripheral subgroup fixes that flag.

The preferred flags vary continuously, indeed analytically on the
marked chart, at the complete point. For the auxiliary cusp the
given eigenvalue is \(M_i=H_i^{-1/2}\); its eigenspace is the
kernel of \(C_i-M_iI\), a rank-one matrix even at the complete
NONCENTRAL unipotent limit. Thus no singular diagonalizing frame
is used. The same statement holds for the noncentral main
parabolic meridian.

There are finitely many tetrahedra, faces and local stars modulo
the deck group. Only finitely many group words occur in their
vertex assignments. Their developed vertices are consequently
uniformly close to the old ones for \(z\) in one fixed sufficiently
small neighborhood. Every tetrahedron in (2) stays strictly
positive and nondegenerate. Straighten it to the convex geodesic
tetrahedron with its assigned vertices.

Shared faces match by EXACT hyperbolic isometries: their three
vertices are the same equivariant points, including every finite
face center. In a fundamental-domain description the transition
is precisely the corresponding \(\rho_z\) face word. Positivity
and closeness keep the two tetrahedra on opposite sides of a
common face. Thus there is no fold in a face interior.

Here are the remaining local checks; positivity alone would not
justify ignoring them.

**Edges.** Develop the finite cyclic star of a nonideal edge into
\(\mathbb H^3\). It returns to the SAME developed face and edge
point because its contractible edge-loop word is the identity in
the actual manifold group, hence also under \(\rho_z\). More
precisely the ENTIRE face-transition product telescopes to
\(\rho_z(1)=1\); this is stronger than merely returning one edge
endpoint or one normal ray. There is no residual translation or
dilation along the edge. In a normal disk, its
positive sectors therefore have total angle \(2\pi k\), with
integer \(k\). Their angles depend continuously on the finitely
many developed vertices. At completeness \(k=1\), so it remains
one in the chosen neighborhood. This includes finite--finite,
finite--ideal and ideal--ideal edges; dihedral angles are constant
along each geodesic edge. The full edge star is an ordinary
hyperbolic neighborhood, without a cone or screw defect.

**Finite vertices.** The finite topological vertex link is a
2-sphere. Its positive spherical triangles glue isometrically,
and the preceding edge check gives angle \(2\pi\) at every
link vertex. Its development is therefore a local isometry to
the unit sphere. Compactness and geodesic path lifting make it
a covering of that sphere. Since the sphere is simply connected,
it is one-sheeted. Hence the vertex star is an ordinary
hyperbolic ball; no hidden branched spherical link occurs.

It follows that every finite point of the ideal-vertex-deleted
manifold has a genuine oriented metric of curvature \(-1\).
Its holonomy is the original \(\rho_z\), by construction.
This proves the required local developing geometry directly,
without assuming a deformation or local-rigidity theorem.

## 4. The actual ideal stars have positive similarity links

Send a selected cusp flag to infinity by a Mobius frame chosen
continuously near its complete frame. In each incident tetrahedron,
the three faces through infinity are vertical planes. The
horizontal projections of the three remaining vertices form a
NONDEGENERATE Euclidean triangle, because the tetrahedron is
positive. They give its horospherical link triangle.

The face transitions fixing infinity are orientation-preserving
complex similarities \(\zeta\mapsto a\zeta+b\). Thus these
positive triangles form a similarity structure on the compact
topological cusp torus. At its vertices the same developed edge
star has winding one and angle \(2\pi\), so this is a local
Euclidean coordinate structure even at those vertices. There is
no cone or branch point in the affine link.

In the continuously chosen flag frame, all vertices of a fixed
finite fundamental union of link triangles remain finite and
uniformly bounded. The finite-center vertices stay finite; the
other ideal vertices remain distinct from the chosen flag.
Their projected triangles and any fixed meridian/longitude edge
paths consequently have uniformly bounded developed images and
Euclidean lengths. This verifies the geometric input used to
identify the small logarithmic periods in the primitive-period
theorem, including for independently unequal filling lengths.

The opposite face of an incident tetrahedron is not vertical:
otherwise it would also contain the ideal point at infinity and
all four vertices would be coplanar. It is a hemisphere, so over
each projected link triangle the tetrahedron contains a vertical
ray above a bounded lower height. These finitely many epigraphs
provide the ACTUAL end, not merely a formal link at infinity.

## 5. Primitive tube completion, with no hidden covering multiplicity

Apply the proved
[compact-log and tube-completion lemma](long_pretzel_equality_critical_audit.md),
sections2--4, to the similarity links just constructed. Its argument
is recalled to specify every needed input.

At an auxiliary end a meridian has affine form
\(d\mapsto a d+b\), with \(a\to1\) and complete
\(b\to W(1+ic)\ne0\). At the selected finite filling \(a\ne1\):
separate evenness gives \(V_i=\tau_i(z)U_i\), while (1) excludes
\(U_i=0\), and the logs are small. The common second fixed point
\(q=b/(1-a)\) therefore exists and escapes to infinity near
completeness. The bounded fundamental link triangles miss it;
equivariance then shows that the ENTIRE link development misses it.

On the simply connected link cover take
\(f=\operatorname{Log}(d-q)\). The form \(df\) is invariant under deck
translations and is everywhere nonzero. Hence \(|df|^2\) is a
nonsingular flat metric on the COMPACT link torus. It is complete.
Lifting straight Euclidean segments makes \(f\) a global
isometry of its universal cover onto \(\mathbb C\). Its periods
form an INJECTIVE rank-two lattice, rather than an unspecified
covering of a punctured plane.

After translating \(q\) to zero, \(d=e^f\). The actual epigraphs
in section4 contain \(y>A|d|\), for some finite \(A\), because
their lower heights divided by \(|d|\) are bounded on a finite
fundamental link domain. The deck similarities multiply both by
the same positive number. In cylindrical coordinates about the
axis \(0\)--\(\infty\), this is the WHOLE punctured tube

\[
 0<R<R_0,\qquad
 ds^2=dR^2+\cosh^2R\,dX^2+\sinh^2R\,d\theta^2.
 \tag{3}
\]

A logarithmic period \(L\) acts by
\((X,\theta)\mapsto(X+\Re L,\theta+\Im L)\).
The period of the primitive filled slope is exactly
\(\pm2\pi i\) by (1) and the primitive-period theorem, NOT
merely an exponentiated value one. Choose that primitive slope
and a complementary longitude as a torus basis. The latter has
nonzero real period because the lattice has real rank two.
Adding \(R=0\) to (3) is therefore a smooth hyperbolic solid
torus: its angular period is exactly \(2\pi\), and its core has
the nonzero loxodromic screw period. Its meridian is precisely
\(\mu_i+p_i\lambda_i\). There is no factor \(|m_i|>1\)
producing a branched core, no zero winding, and no extra framing
longitude.

At the unfilled main cusp both affine multipliers are one. Its
positive link is an ordinary flat translation torus; compactness
again makes its development the Euclidean plane. Its end contains
a full horoball quotient and is complete with finite volume.

## 6. A complete finite-volume metric on the original filled topology

Choose all slopes sufficiently long that their selected source
parameters lie in the fixed positive geometric neighborhood of
sections2--4. The source solution is holomorphic in all
\(\epsilon_i=1/p_i\) near zero, so a common threshold works
whenever every \(|p_i|\) exceeds it, with either sign and NO
comparability requirement. The source parameters are fixed before
the quantum-level limit is taken.

Complete every auxiliary end as in section5. The underlying
topological operation is exactly Dehn filling by its prescribed
primitive slope, and leaves the original complete main cusp.
This is the actual pretzel knot with boxes
\(R^{-(2p_i+1)}\), by the literal tangle and preferred-peripheral
certificates. All original cap, spin and marking data agree.

The resulting Riemannian metric is smooth of curvature \(-1\).
Its complement of the standard ends is compact; the added solid
tori are compact at bounded tube radius and the main horoball
quotient is a complete cusp. Thus the whole metric is complete.
Its volume is finite: there are finitely many finite-volume
partially ideal tetrahedra, standard finite-radius tubes, and
one finite-volume cusp. Its holonomy is exactly \(\rho_{\boldsymbol p}\).

The complete simply connected developing cover is \(\mathbb H^3\).
Indeed geodesic path lifting for a complete local isometry gives
a covering of \(\mathbb H^3\), which is simply connected. Hence
the developing map is a global isometry and the holonomy is
discrete and faithful. This conclusion has been PROVED from the
positive core and primitive tube; it was not inferred from killing
a peripheral word or from proximity of two volumes.

There is no need for a separate character-variety local-uniqueness
theorem. The actual source critical solution is already the unique
analytic selected solution in its marked small parameter chart.
For that fixed holonomy the completed structure is
\(\mathbb H^3/\rho_{\boldsymbol p}\), so changing auxiliary finite
centers cannot produce a different complete metric. No assertion
that all algebraic character components are this branch is used.

## 7. Hyperbolic-volume equality and the original invariant

The [marked regulator comparison](actual_pretzel_marked_regulator_and_filling_action.md)
and the finite compatible filling-chain argument prove

\[
 2\pi\Re\mathcal A_s(\boldsymbol p)
                    =\operatorname{Vol}(\rho_{\boldsymbol p}).
\]

Since the constructed complete metric has that holonomy and the
same oriented fundamental chain, its geometric volume is precisely
this value. If one starts with another complete finite-volume
hyperbolic metric on the same oriented filled topology, apply the
independently proved sharp representation-volume inequality in
BOTH directions, with the identity-marked holonomies. The two
inequalities force equal volumes. Thus no additional unproved
volume-rigidity assertion or imported Mostow theorem is needed to
identify this with the usual topological hyperbolic volume.

Finally the [whole original-source asymptotic](actual_long_pretzel_full_source_survival.md)
has a nonzero leading coefficient at BOTH level parities and all
composite levels, with the actual original normalization. Combining
it with the geometric completion gives

\[
 \boxed{\quad
 \lim_{N\to\infty}\frac{2\pi}{N}
       \log\left|\langle\operatorname{Pretzel}
                 (2p_1+1,\ldots,2p_s+1)\rangle_N\right|
 =\operatorname{Vol}\bigl(S^3\setminus
                 \operatorname{Pretzel}(2p_1+1,\ldots,2p_s+1)\bigr).
 \quad}                                                \tag{4}
\]

Here \(s\geq25\) is any fixed odd integer, and the independently
signed integer slopes are all sufficiently long and fixed before
\(N\to\infty\). The construction itself proves hyperbolicity
in this sufficiently long range. No statement for short slopes,
smaller widths, growing width, or arbitrary knots is inferred.

This completion is a geometric equality certificate. A
Casson--Rivin ideal-angle interpretation requires its own positive
ideal shape chart and modified filling constraints; it cannot be
obtained by maximizing the old unfilled cusp slice. The direct
positive finite-center metric and primitive end completion above
do not need that additional chart.

## 8. Scope of the completion argument

The edge transition is the full identity, including zero axial dilation. The proof uses degree-one spherical links, positive similarity-link triangles, bounded generator paths and actual epigraph ends; finite samples cannot replace these neighborhood and degree conditions.