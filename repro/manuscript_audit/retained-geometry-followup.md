# Follow-up audit of the retained geometric cells

This is a bounded read of the geometric-volume identification and the
filled representation germ in the current manuscript. It concerns
Appendix F, Appendix I, their technical companions, and the uses of
these conclusions in the introduction, Chapters 7 and 12, Appendix M,
and the scope discussion. The paired snapshot records the exact source
hashes and an implication map. It supplements the earlier recursive
and directed geometry records; it does not replace them or certify the
whole manuscript.

No further necessary manuscript correction was found in this read.
The two previously identified explanations are now present: the
same-chain comparison between representation and metric volume, and
local uniqueness on the retained positive augmented triangulation.
Both have hypotheses that are essential to the conclusion below.

## 1. The original manifold and the positive metric

The topology checked here is the literal finite ordered circle tree
of Appendix F, lines 44–218. It has at least one physical quarter-turn
edge, a crossing circle at every product junction, and retained
endpoint orders, projection copies, disk framings and signed half
twists. The final one-component test is separate from the geometric
construction. The argument does not identify arbitrary tensor graphs,
graphs with cycles, or scalar turn identities with link exteriors.

I read the following upstream topological arguments, not just their
names:

* Appendix F's right and left insertion tables, the corresponding
  octahedral face labels, the terminal-root construction preserving
  the original child order, and the extension of the resulting labeled
  boundary-sphere homeomorphism over the two balls.
* The original closed projection/disk cut in
  `actual_conway_bowtie_projection_cut.md`, sections 2–4. Its physical
  segment pairing and oriented ribbon walks determine the white
  faces. Drilling the disjoint boundary-parallel auxiliary semicircles
  and opening their recorded half disks returns balls. This is a
  reversible cut of the specified diagram.
* The two-circle base in
  `actual_reflected_two_circle_octahedral_base.md`, sections 1–2:
  the quarter-turn shifts the puncture order, and the displayed
  shaded/white face table is the original disk regluing. Its later
  generalization warnings are not used as a general graph theorem.
* Appendix F's primitive concatenation, lines 183–218. An insertion
  subdivides a meridian passage without winding it again; the original
  disk longitude stays primitive. Internal frame changes telescope.
  The distinguished odd seam is used once, with its full puncture
  exchange and signed half-longitude correction.

The local angular calculations remain an explicit input: positive
tetrahedra, ordered three-point maps, complete edge-return identities,
and inverse complex seam ratios. I reread their use in F, lines
430–497, including the three odd return words. I did not rerun every
symbolic identity or the uniform numerical enclosure in the local
chart. The independent analytic path input is precisely

\[
 |\tau_v(c)|<10^{-2},\qquad
 \operatorname{Im}\tau_v(c)<0\quad(0<c\le1),
 \qquad
 \Psi_{\tau_v}+\frac{i n_v\tau_v}{2\pi}-ic=0.
\]

The geometric proof uses these path properties, not the particular
summed sufficient inequality that first supplied them. Thus the later
vertexwise and directed applications must supply the same path, as
their separate proofs state. This read does not reprove those analytic
estimates or infer them from finite checks.

## 2. Periods and smooth completion

The primitive formulas are

\[
 U_v=-2\pi\Psi_{\tau_v}-i\epsilon_v\tau_v,
 \qquad V_v=2i\tau_v,
 \qquad n_v=\epsilon_v-2p_v.
\]

They imply \(U_v+p_vV_v=-2\pi ic\). An exponentiated equation alone
would not suffice. F, lines 499–560, supplies the missing metric data:

1. The main puncture meridian is noncentral parabolic. Its commuting
   peripheral group acts by translations, giving complete main cusp
   links.
2. At each auxiliary end, \(\Re V_v=-2\Im\tau_v>0\), so its
   multiplier has nonunit modulus. The similarity torus avoids its
   second fixed point by the index argument. The logarithmic
   development has nonsingular derivative and induces a complete flat
   metric on that compact torus. Its periods form a real rank-two
   lattice.
3. Actual generator periods and the displayed \(U,V\) differ by
   multiples of \(2\pi i\). In a fixed frame the second fixed point
   escapes as the charge tends to zero, while the developed generator
   paths stay bounded. Their actual log increments tend to zero.
   This fixes the integers before a filling integer is multiplied
   into a peripheral period.
4. The original pair \((\mu_v+p_v\lambda_v,\lambda_v)\) has
   determinant one. The first period is \(-2\pi ic\), and the
   second has positive real part. The explicit cylindrical metric
   therefore adds a cone axis of angle \(2\pi c\); at \(c=1\) it
   adds the smooth solid torus with exactly the prescribed meridian.

The main ends remain complete, the remaining region is compact, and
the completed metric is finite-volume on the original filled topology.
At the smooth endpoint, completeness makes its universal developing
map the hyperbolic-space covering, hence its holonomy is the geometric
holonomy. No global injectivity of the developing map was assumed
earlier. No descent to a smooth filled group is claimed for
nonintegral intermediate cone angles.

## 3. Absolute volume and the factor \(2\pi\)

F, lines 566–591 and 639–667, uses projective similarity logarithms,
not single eigenvalue logarithms:

\[
 G^0=2\pi i\bigl(\Psi-\sum_v\tau_v\Psi_{\tau_v}\bigr),
 \quad dG^0=\tfrac12\sum_vV_v\,dU_v^0,
 \quad G=G^0-\sum_v\epsilon_vV_v^2/8.
\]

The boundary-chain differential gives

\[
 \operatorname{Vol}(\rho)=\operatorname{Im}G
       -\tfrac12\sum_v\Re U_v\Im V_v.
\]

Its constant is the actual complete two-projection-ball metric:
\(\operatorname{Im}G(0)=2\pi F_0\). The derivation retains this
constant and the continued log branches. It does not determine the
volume by matching derivatives alone.

The inserted comparison at F, lines 593–637, uses the same oriented
cell chain and finite boundary triangulation. In a fixed auxiliary
frame its homotopy is

\[
 H_s(w,Y)=\bigl(sa(w),
 Y\exp((1-s)\eta(w)+s\log b(w))\bigr).
\]

The functions have the stated deck transformations, so the homotopy
is equivariant and face-compatible. Horizontal derivatives are bounded,
height is comparable to \(Y\), and height derivatives are \(O(Y)\).
The pulled-back hyperbolic volume form is therefore \(O(Y^{-2})\).
At \(c=1\) the zero real period on the primitive meridian permits
extension over its disk with added vertices on the common axis; the
added tetrahedra have zero volume. The main horoball comparison also
has vanishing boundary volume. For \(0<c<1\) the comparison is with
the cone metric off its axis, not a smooth filled-group representation.
These observations justify the inserted equality
\(\operatorname{Vol}(\rho)=\operatorname{Vol}_c\).

With \(\Phi=G/(2\pi i)\) and the stationary charge action
\(\mathcal C(c)\), the two algebraic terms are

\[
 \Phi-\mathcal C(c)=-\frac{i}{2\pi}\sum_vp_v\tau_v^2,
 \qquad
 \tfrac12\Re U_v\Im V_v=p_v\operatorname{Im}(\tau_v^2).
\]

They cancel in the volume formula, yielding
\(\operatorname{Vol}_c=2\pi\Re\mathcal C(c)\). The Schläfli
derivative is an additional consistency calculation, not a substitute
for this absolute calibration. The same-chain repair in Appendix D,
lines 410–436, has matching hypotheses for its original small
deformation construction; Chapters 4 and 7 retain their own completed
root class and independently long signed fillings.

## 4. Filled deformation uniqueness on the retained cells

The new proof is I, lines 1305–1406. It uses the positive triangulation
of the original augmented exterior at its filled representation point.
It does not assume a newly constructed positive ideal triangulation
of the filled knot complement.

The necessary hypotheses are:

* all \(t\) oriented tetrahedra are positive, their developed triples
  and quadruples are distinct, and the actual edge equations hold;
* the underlying fixed triangulation is the original augmented
  oriented manifold with \(\nu=R+1\) torus links;
* the main cusp retains its noncentral meridian, exact chosen
  eigencharacter, and source \(M^{-1}\) flag;
* every auxiliary longitude has distinct eigenvalues, and the slope
  word is projectively identity at the smooth endpoint;
* the peripheral rows are those of the original primitive main
  meridian and original integral slopes, with their continued logs.

I read the real row-rank proof in
`general_marked_multicusp_gluing_rigidity.md`, section 2, and the
componentwise normal-flow intersection proof in
`integral_half_longitude.md`, section 2. The latter is used only over
the reals; its later knot-specific integral half-class is unnecessary.
There are \(t-\nu\) independent isotropic edge rows. The peripheral
quotient is the sum of the \(\nu\) symplectic homology planes. One
nonzero primitive row on each different torus therefore completes a
full real Lagrangian system \((A\ B)\), with

\[
 \operatorname{rank}(A\ B)=t,
 \qquad AB^{\mathsf T}=BA^{\mathsf T}.
\]

In the stated quad order
\(T_j=z_j/(1-z_j)\), so \(\Im T_j>0\). The real kernel of
\((A\ B)\) is spanned by \((-B^{\mathsf T}y,A^{\mathsf T}y)\).
If \((A+B\operatorname{diag}T)x=0\), its complexification contains
both \(w=(x,Tx)\) and \(\bar w\), contradicting

\[
 \frac{i}{2}\Omega(w,\bar w)=\sum_j\Im T_j|x_j|^2>0
 \quad(x\ne0).
\]

This verifies the sign and full-rank assumptions, rather than assuming
that positivity alone makes an arbitrary square Jacobian invertible.
Dependent affine edge constants are compatible because this very
endpoint satisfies them. Incomplete auxiliary ends introduce no new
condition in this argument.

The normalized ordered-triple construction and the original dual
two-skeleton give the shape-to-representation map. Conversely,
equivariant peripheral flags develop the original ideal vertices and
recover every cross-ratio. Unit denominators make these inverse also
over local Artin algebras. The object is the decorated representation
germ modulo simultaneous conjugation; it is not the unmarked trace
variety. In particular the exact main eigencharacter is required at
the noncentral parabolic point.

For the filling relations, distinct auxiliary eigenvalues split the
rank-two module. Choose the slope lift with residue identity. Its
projective commutator scalar satisfies \(c_0^2=1\) and \(c_0\equiv1\),
so \(c_0=1\) because \(c_0+1\) is a unit. The slope is then diagonal
in the longitude basis; ratio one makes it scalar. This works over
the same Artin rings and does not change a separately retained
determinant-one lift sign. Consequently imposing the continued slope
logs is exactly imposing the filled-group relations locally.

Fixing those \(R\) slope coordinates leaves one smooth decorated
germ, with \(u=\log M\) as coordinate: the ordered main similarity
log on the source flag is \(-2u\). The full source reconstruction,
its nondegenerate implicit branch and its already identified complete
filled basepoint place it in this same germ. Uniqueness therefore
identifies the source branch with the geometric meridian germ.

This removes the previous filled-positive-triangulation existence
import for this retained-positive augmented family. It does not assert
that every other use of geometric rigidity in the repository has been
removed or audited. In particular Appendix J explicitly allows flat
added zero-circle cells; its argument must use the original strict
geometry and its own marked comparison, not positivity of those added
cells. That broader proof was not re-audited in full here.

## 5. Peripheral words and the use in Appendix M

I reread I's complete ordered boundary tuple table, lines 1046–1115,
and its opposite-eigenflag qualification and mapping-cylinder gluing,
lines 1117–1185. The two puncture conjugacies and the boundary product
are retained. The proof does not infer the group representation from
three trace equalities or transport incompatible displayed flags
without their eigenvalue choices.

The squared longitude proof remains a separate algebraic chain:
boundary isotropy, the source constant field, regular reconstruction
over every nonzero main value, the monomial calculation, and the
preferred surgery correction. The determinant-one sign is fixed at
the actual filled point by the written Seifert-frame argument. This
turn did not repeat every matrix identity or every all-parameter
regularity calculation in I, sections 6–10; the earlier bounded
geometric-characteristic audit records those checks. The retained-cell
replacement supplies the local geometric branch premise, not an
independent proof of that whole algebraic chain.

M, lines 293–360, uses the geometry in the correct order. Its directed
certificate supplies \(2\pi|D_v|>630\), and backwards restoration
puts the conditional stationary points in the common angular
uniqueness region. Thus it uses the same completed charge path.
It then uses the exact source stationary equations and I's full
reconstruction to obtain the filled meridian germ. The preferred
eigenvalue is stated on the \(M\) line, inverse to the source
\(M^{-1}\) line. Its cusp correction retains the factor
\(\pi i\tau_Ks^2/(2N)\). No finite test is being substituted for
the all-order estimates, which were outside this follow-up read.

## 6. Scope and remaining proof inputs

The checked introduction and scope passages retain these distinctions:

* The completed-root recursive construction has its own fixed diagram
  and knot test, followed by independently long signed fillings.
* Circle trees have separate summed, local, or directed analytic
  hypotheses. The vertexwise positive metric criterion alone supplies
  no quantum volume limit.
* Terminal decorations can change the knot. The decorated theorem is
  not a theorem for every unchanged core.
* Weak balance is a sufficient full-source condition for its stated
  unchanged diagrams. It is not asserted for every packing.
* For an arbitrary unchanged simple matched sphere, Appendix O only
  identifies a nonzero geometric contribution. A full invariant limit
  still needs a bound on the complementary signed contribution.
* The selected-factor statement assumes an existing nonzero fixed
  all-level annihilator and the specified all-order source hypotheses.
  It is not recurrence existence or equality with an entire ideal.

The standard holomorphic implicit-function theorem, completeness and
covering arguments, elementary three-manifold cut topology, and the
representation-volume boundary differential remain mathematical proof
inputs, not Lean-checked results. The latter's chain conventions were
checked here against F and the prior D record; its entire underlying
Bloch/regulator theory was not redeveloped. The local rational chart,
the strict entropy/source theorem, and the analytic noncancellation
estimates remain their named written inputs. No source estimate has
been obtained from volume rigidity or geometric uniqueness, so the
dependency order examined here is not circular.
