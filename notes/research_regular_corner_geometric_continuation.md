# Marked geometric continuation through regular square corners

Private written geometry, 16 November 2026.

A supplied positive sequence approaching a regular one-square corner
determines a marked cone metric at the corner. For a proper selected
set, the original primitive-period Jacobian is nonsingular there.
The resulting local charge branch has actual marked cone metrics,
including on its admissible nonpositive-cell side, and its continued
original stationary action equals their volume.

Calibration holds on a full real charge neighborhood. Accumulation of
a sequence alone would not suffice: a sufficiently late strictly
positive point has an open positive neighborhood, with smoothly
identified actual original metrics. This supplies an open set for
the real-analytic identity theorem.

The theorem does not prove that arbitrary fixed short fillings have
the supplied positive approach, that every later degeneration is a
regular one-square corner, or that the geometric contribution
survives in the original finite quantum sum.

## 1. Original data and the supplied approach

Let \(G=(V,E)\) be a fixed connected original ordered circle tree
with at least one edge, and let
\(\varnothing\ne S\subsetneq V\) be its selected vertices.
Keep its original exterior \(Y\), main components, page orders,
face words, disk frames and half-twist carriers. At \(v\in S\)
fix the original primitive basis \((\mu_v,\lambda_v)\), integer
filling coefficient \(p_v\), and retained carrier \(\eta_v\). Put
\[
                 n_v=\eta_v-2p_v,\qquad
                 \alpha_v=\mu_v+p_v\lambda_v .
 \tag{1}
\]
Varying a charge changes neither a slope nor a carrier.

Write \(\mathbf t=(t_v)_{v\in S}\) and \(t_b=0\) for \(b\notin S\).
In the original angular coordinates, on \(e=\{v,w\}\) put
\[
 r_{v,e}=\operatorname{arsinh}
             \{\tan(t_v/2)\cos(t_w/2)\},\qquad
 \mathcal P_v(\mathbf t)=
              \sum_{e\ni v}r_{v,e}-\frac{i n_vt_v}{2},
 \tag{2}
\]
\[
 U_v=2\sum_{e\ni v}r_{v,e}-i\eta_vt_v,\qquad V_v=2it_v.
 \tag{3}
\]
The branches are the original positive ones and their continuation
to the specified regular corner. The charge equations are full
logarithmic identities:
\[
 \mathcal P_v(\mathbf t)=-\pi i\chi_v,\qquad
                     U_v+p_vV_v=-2\pi i\chi_v .
 \tag{4}
\]

Supply positive configurations \(\mathbf t^{(j)}\to\mathbf t^*\)
and charge vectors satisfying (4), with
\[
 \boldsymbol\chi^{(j)}\to\boldsymbol\chi^*,\qquad
 0<\chi_v^{(j)}\le1,\quad 0<\chi_v^*\le1,\qquad
 -\Im t_v^{(j)}>0,\quad H_v^*:=-\Im t_v^*>0 .
 \tag{5}
\]
They carry their actual original completed cone metrics \(g_j^+\),
with periods (3)--(4), cone angles \(2\pi\chi_v^{(j)}\), and
complete main and unselected cusps. One may instead supply a
positive one-parameter approach and take a sequence on it.

The limiting configuration must satisfy precisely the regular
one-square hypotheses of the marked-limit theorem: each edge is
positive or has one finite regular corner square with the other
square interior; there are no two-square corners, colliding ideal
vertices or face triples, or vanishing original face-map
denominators. The canonical angles remain finite. Condition (5)
then supplies the uniform positive upper and lower core-height
bounds required by that theorem.

Include every original edge in the primitive
\[
 \Psi(\mathbf t)=\sum_{e\in E}\psi_e(t_v,t_w),\qquad
 \psi_e(0,0)=4G_{\rm Cat}/\pi,\qquad
 d\psi_e=-\frac1\pi(r_{v,e}\,dt_v+r_{w,e}\,dt_w),
 \tag{6}
\]
where \(G_{\rm Cat}\) is Catalan's constant. Thus a complete
outside edge contributes its original volume \(8G_{\rm Cat}\).
The primitive, logarithmic lifts and absolute constant are retained
from the original positive branch, not chosen anew at the corner.
For real charges define
\[
 F_{\boldsymbol\chi}(\mathbf t)
 =\Psi(\mathbf t)+\frac{i}{4\pi}\sum_{v\in S}n_vt_v^2
                         -i\sum_{v\in S}\chi_vt_v .
 \tag{7}
\]

## 2. The continuation theorem

**Theorem 1.** There is a connected real charge ball \(B\) about
\(\boldsymbol\chi^*\), and a holomorphic solution on a complex
neighborhood of \(B\), such that
\[
 \mathbf t(\boldsymbol\chi^*)=\mathbf t^*,\qquad
          \mathcal P(\mathbf t(\boldsymbol\chi))
                                  =-\pi i\boldsymbol\chi .
 \tag{8}
\]
It is unique in one fixed angular neighborhood of \(\mathbf t^*\).
Every sufficiently late supplied point lies on this same branch:
\[
                    \mathbf t^{(j)}
                          =\mathbf t(\boldsymbol\chi^{(j)}).
 \tag{9}
\]

For every charge in
\[
 B_{\rm adm}=\{\boldsymbol\chi\in B:
                              0<\chi_v\le1\text{ for every }v\},
 \tag{10}
\]
there is an actual complete finite-volume cone metric
\(g_{\boldsymbol\chi}\) on the original marked filling. Its
exterior holonomy is the original continued face-word representation.
At \(v\) its meridian is \(\alpha_v\), cone angle is \(2\pi\chi_v\),
core length is \(-2\Im t_v(\boldsymbol\chi)>0\), and full longitude
period is \(2it_v(\boldsymbol\chi)\). Every unfilled end is the
original labeled complete cusp.

The relative construction is real analytic in all charge
coordinates on compact sets, with exact canonical ends, and
\[
 \boxed{\quad
 \operatorname{Vol}(g_{\boldsymbol\chi})
       =2\pi\Re F_{\boldsymbol\chi}
                         (\mathbf t(\boldsymbol\chi)),
                \qquad\boldsymbol\chi\in B_{\rm adm}.
 \quad}
 \tag{11}
\]
This includes the corner and admissible nearby parameters where
some original tetrahedra have become negatively oriented. When
all charges are one, the metric is smooth hyperbolic on the
original filling. At nonintegral charges holonomy is asserted
on the unfilled exterior; descent to the filled group is not
asserted.

If every \(\chi_v^*\) is strictly less than one, a whole smaller
real ball is admissible. Otherwise (10) is the precise restriction:
a chosen path leaving it is outside the metric conclusion.

## 3. The charge branch and the actual representation

The corner-period theorem gives
\[
 J_S=D_{\mathbf t}\mathcal P
 =\sum_e\iota_e^T
   \frac1{2q_e}
   \begin{pmatrix}1+a_v^2&-a_va_w\\-a_va_w&1+a_w^2\end{pmatrix}
   \iota_e-\frac i2\operatorname{diag}n,\qquad
                         \Re J_S(\mathbf t^*)>0,
 \tag{12}
\]
where \(a_v=\tan(t_v/2)\), \(q_e^2=1+a_v^2+a_w^2\), and
\(\iota_e\) inserts zero variations at outside endpoints.
Connectedness and the proper selected set are essential: the
two nonzero coordinates of each corner kernel propagate a null
variation to an outside pin, where it vanishes. Signed powers
add only an imaginary diagonal.

The retained returns are holomorphic near the regular corner.
Taking limits in (4) gives its equation at
\(\boldsymbol\chi^*\). The holomorphic implicit-function theorem
for \(\mathcal P(\mathbf t)+\pi i\boldsymbol\chi=0\), using
(12), proves (8) and uniqueness in fixed neighborhoods.
Both members of (9) lie in those neighborhoods and solve the
same equation, proving (9). In particular branch coincidence
does not follow merely from a common limit. Differentiation gives
\[
                    D_{\boldsymbol\chi}\mathbf t=-\pi iJ_S^{-1}.
 \tag{13}
\]
Shrink the neighborhoods so that \(H_v=-\Im t_v>0\), every
original face denominator remains nonzero, and \(\Re J_S>0\).

The original face words give actual representations throughout
this germ. Indeed each relation in a finite presentation, written
with the regular face matrices, is a holomorphic matrix identity.
It holds on the open set of strictly positive original
configurations, where the same face maps give an exterior metric,
and therefore on the connected local chart. The retained
peripheral identities continue in the same way, including
(3)--(4) and their actual flags. This is the original face
cocycle construction, not a representation inferred from periods.

At selected ends \(H_v>0\) keeps the longitude loxodromic.
Its ordered fixed pair continues from the original one.
Commutation and the retained common flag keep both peripheral
images in that pair. At an unselected auxiliary vertex \(t_b=0\)
makes its continued return identically zero, so its two
peripheral multipliers remain one. The main corner words also
retain their original parabolic flags and unit multipliers.
These identities do not require positivity beyond the wall.

The limiting metric constructed next has nontrivial parabolic
generators and independent real translation periods at every
unfilled cusp. These are open conditions after normalizing the
continued flags. Thus the local original representations have
all the peripheral properties required by the relative cone
theorem wherever (10) holds.

## 4. The marked base and the relative metric family

The marked-limit theorem applied to the supplied sequence gives,
after a subsequence, an actual complete marked cone metric \(g_*\)
on the original filled topology. It has the limiting periods and
canonical complete cusp models. It also gives compact-core
diffeomorphisms and stabilized original markings under which the
normalized developments of \(g_j^+\) converge smoothly to that
of \(g_*\) on compact subsets of the exterior universal cover.
Every selected axis is omitted, including smooth unit-charge axes.
The canonical end identifications converge in that same marking.

The holonomy of \(g_*\) is the literal original limiting face-word
representation. Section 3 supplies nearby actual representations
of this marked exterior with the requisite full peripheral data.
The relative cone deformation theorem therefore constructs
\(g_{\boldsymbol\chi}\), using the real parameter
\(\boldsymbol\chi-\boldsymbol\chi^*\). Its formulas are real
analytic in all coordinates. Its Proposition 3 gives an analytic
total-volume germ on a real neighborhood of the corner, including
the analytic extension of the formula when (10) has a boundary.

Agreement of volumes and actions only on the supplied sequence
would not justify a multivariable identity. The following
positive-family statement supplies an open set of agreement.

## 5. Smooth dependence of the actual positive gluing

**Lemma 2.** Near a strictly positive point on (8), the original
positive cone metrics admit actual identifications of compact
cores preserving the original marking and canonical ends.
In these identifications their metrics and normalized developing
charts depend smoothly in space and real analytically on nearby
real charge vectors.

**Proof.** Positivity is open. The original face maps and full
projective edge returns remain the same analytic identities.
Around every internal edge the positive dihedral angles sum
to an integral multiple of \(2\pi\), and their shears vanish.
Continuity from the given point fixes this angle sum to \(2\pi\).
The original quotient is consequently an actual nonsingular
hyperbolic exterior metric. Its complete cusps and selected
tube completions use (3)--(4). The positive completion argument
uses the positive cone charge and full primitive period, so
applies here without requiring that the charge equal one.
More explicitly its logarithmic link has ordered periods
\(-2\pi i\chi_v\) and \(2H_v+2i\Re t_v\), of real covolume
\(4\pi\chi_vH_v>0\). Its canonical punctured tube completes
by adding an axis of angle \(2\pi\chi_v\). The winding of
these periods is fixed by the same positive tangent contraction
as in that source; the contraction need not satisfy filling
equations. This local positive argument requires \(\chi_v>0\),
while the final theorem retains the restriction (10).
On a smaller neighborhood common truncation radii and cusp
depths can be chosen.

Here is the chart dependence. Cover the reference compact core
by finitely many smaller developed balls contained in tetrahedron
interiors, two-tetrahedron face stars, or finite edge stars.
There are no finite ideal vertices in this compact part.
For an interior ball, regular moving vertices give a continuously
normalized frame and the smaller ball stays inside the cell.
Across a face, develop the two positive sides using the actual
face isometry; again the smaller ball stays covered. At an edge,
the consecutive positive wedges still tile a full angle \(2\pi\)
about the moving geodesic. Their other faces stay away from the
chosen smaller ball. It remains a full ball in the actual edge
star. The frames and face maps vary real analytically.

On an overlap choose one route inside the common local face stars.
The transition is the corresponding finite product of original
isometries and varies real analytically. Other routes give the
same local transition by the full return identities in these
contractible stars; no assertion is made about routes around a
nontrivial global loop. These are charts
of the actual quotient, not charts in a formal gluing complex.
Add the canonical tube and cusp charts on compact boundary
collars; their periods and fixed-point frames vary real
analytically as well.

The local candidate maps from the reference charts to the nearby
charts have discrepancies tending to zero with every derivative.
Glue them by the normalized Lorentz average of Section 4 of the
marked-limit proof, with a fixed smooth partition. Use weight
one for the canonical end candidates near boundary tori and for
the normalized base chart near the basepoint. The candidate
images at a point lie in one common buffered target chart.
Lorentz invariance makes the average independent of that chart.
It is a smooth local diffeomorphism, real analytic in parameters
in local coordinates, and preserves boundary levels and sides.

The compact-core map is a global diffeomorphism. It is proper
and locally invertible also in boundary half-charts, hence a
finite covering: the fiber is finite, and its finitely many
inverse neighborhoods together with properness give an evenly
covered target neighborhood. Its image is open and closed.
The target is connected and has boundary, since \(S\) is proper.
Every boundary torus is mapped by its prescribed diffeomorphism,
so a boundary point has exactly one preimage and the degree is
one. Extend by the exact model end identifications.

The marking remains the original one. Candidate maps follow
the same labeled cell and face-star routes. A small change of
parameter homotopes each chosen original generator through these
same stars; the Lorentz average stays in their buffered
neighborhoods and changes none of those homotopies. The exact
end maps preserve the peripheral bases, and the base chart fixes
the holonomy normalization. Continuing the convergent chart
transitions along fixed lifted paths proves the corresponding
development convergence on each compact subset of the exterior
cover. This proves the lemma. \(\square\)

At the flattened corner these conclusions could not be inferred
from the old cell maps. There the marked-limit theorem was needed
first. Lemma 2 is used only at a strictly positive sequence member.

## 6. Open-set calibration

The positive-edge volume identity allows arbitrary real charges.
Writing \(t_v=s_v+ih_v\), it gives
\[
 V_e=2\pi\Re\psi_e
              -2\sum_{v\in e}\Im t_v\,\Im r_{v,e},\qquad
 \sum_{e\ni v}\Im r_{v,e}=n_vs_v/2-\pi\chi_v .
 \tag{14}
\]
Thus the selected correction is exactly
\[
 -n_vs_vh_v+2\pi\chi_vh_v
       =2\pi\Re\{in_vt_v^2/(4\pi)-i\chi_vt_v\}.
 \tag{15}
\]
Outside angles vanish. Sum (14) over every original edge to get
\[
       \operatorname{Vol}(g_{\boldsymbol\chi}^+)
              =2\pi\Re F_{\boldsymbol\chi}
                                   (\mathbf t(\boldsymbol\chi)).
 \tag{16}
\]
The positive tetrahedron interiors partition the actual metric
away from faces and completed axes of volume zero. This is a
metric-volume identity with the absolute constant retained.
Neither (14) nor (15) requires integral or unit charges.

Choose a sufficiently late \(\boldsymbol\chi^{(j)}\in B\).
By (9) its actual representation agrees with that of
\(g_{\boldsymbol\chi^{(j)}}\). The marked-limit identifications
put \(g_j^+\) close to \(g_*\) in the finite lifted atlas of
the relative comparison lemma. The constructed metric is also
close there. The canonical ends have identical full periods.
That lemma gives an actual marked isometry between the metrics.

Lemma 2 strengthens this to an open neighborhood \(O_j\) of
the positive charge vector. Shrink it inside \(B\) and inside
the positive locus. Compose its smoothly varying original
markings with the fixed marked-limit identification at \(j\).
Both metric families stay close to \(g_*\) in the same lifted
atlas throughout this neighborhood, with the same actual
representations and compatible canonical ends. The relative
comparison lemma applies at every admissible parameter of
\(O_j\), giving (16) for the constructed metrics.

The set
\[
                   O_j\cap\{0<\chi_v<1\text{ for every }v\}
 \tag{17}
\]
is nonempty and real open. Indeed \(O_j\) is open about a
positive vector with entries at most one, and entries equal to
one can all be decreased slightly inside \(O_j\).
This handles unit-charge members without assuming an admissible
two-sided neighborhood of such a member.

Both sides of (11) have real-analytic germs on the connected ball
\(B\). For volume use Proposition 3 of the relative cone theorem,
including its analytic extension across admissibility boundaries.
For the action use (6)--(8): regular shapes avoid \(0,1,\infty\)
and the original holomorphic primitive and logarithms are
continued on the chosen germ. Their difference vanishes on
(17), and hence on \(B\) by the real-analytic identity theorem.
Explicitly its power series vanishes locally on (17), and
overlapping analytic balls continue that zero along any path
in \(B\). Restriction to (10) proves (11) for actual metrics.

The open positive family is essential to this argument.
An accumulating sequence alone would not determine an analytic
function of several charge variables.

## 7. One-parameter specialization and scope

Let \(\boldsymbol\chi(\tau)\) be real analytic through
\(\boldsymbol\chi(0)=\boldsymbol\chi^*\), and suppose a supplied
positive approach \(\mathbf t^+(\tau)\), \(\tau<0\), tends to
\(\mathbf t^*\) and satisfies the same original equations.
The fixed-neighborhood uniqueness in Section 3 forces
\[
                 \mathbf t^+(\tau)
                        =\mathbf t(\boldsymbol\chi(\tau))
 \tag{18}
\]
for all sufficiently small negative \(\tau\). It is therefore
the same analytic branch, not just a branch with the same limit.
If the approach was merely continuous, (18) itself gives its
analyticity near the corner. Theorem 1 continues its actual
marked cone metric and volume wherever its charges remain in (10).

The metric beyond the wall uses a regular atlas and does not
assert that the original ideal cells remain positive. No
arbitrary short filling is proved to reach this branch, and
later two-square, zero-height, vertex-collision or face-chart
singularities remain outside the theorem.

No finite quantum cycle, closing functional or coefficient is
changed or estimated. Geometric and volume continuation do not
establish the volume conjecture for these fillings.

## Direct sources and author readback

- [Marked corner limit](research_regular_corner_marked_metric_limit.md):
  full theorem and Sections 2--6, actual metric, original marking
  and compact-cover development convergence. SHA256
  f37150aac382997ef3c96e23f2370517dc669184446577f7b452a2304571f1c0.
- [Corner primitive periods](research_regular_corner_period_assembly.md):
  full proof, especially Theorem 2 and Section 4, anchored
  accretivity, original branch and carrier normalization. SHA256
  7d551e90d04b7c45232074109581bf2a807569259f98ad81e00855bec7f51ce5.
- [Relative cone deformation](research_relative_cone_holonomy_deformation.md):
  full proof, Theorem 1, Lemma 2 and Proposition 3, actual metrics,
  marked comparison and analytic total volume. SHA256
  cf1ae892d02731cd8bbf35966ad4fd5a948fd9b3b21ace534fe1656a51be2ee3.
- [Original positive volume](research_positive_edge_volume_identity.md):
  full proof; (21)--(27) allow arbitrary real charges; Section 9
  records the regular original face cocycle. SHA256
  669722d49e292bf64d839901b350226b9d878c1b240d148193b09a927ef7b88e.
- [Original positive completion](research_positive_point_marked_completion.md):
  full proof, Sections 3--6, actual positive gluing, primitive
  words, complete cusps and tube coordinates. SHA256
  28de22f081e24629ea6d26ad05213301a9bcf5d17d3ae7d00cc9c675a8218887.

Only written mathematics and source-text/hash inspection are used.
No mathematical program, numerical computation, test or compilation
is used. Frozen notes and public documents are unchanged.
The author reread the entire final proof. All five complete direct
source reads were retained or renewed in this proof sequence,
their used implications were reread, and their hashes checked.
Independent full peer and root review are required before adoption.
