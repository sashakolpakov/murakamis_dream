# A volume gap for parabolic representations of one fixed filled complement

This is a geometric lemma for one fixed complete finite-volume hyperbolic exterior. It does not assign a representation to a LEFT or RIGHT source sector. Its use for a filled quantum period requires that separate assignment, the absolute action normalization, and control of the original integration cycle.

The gap is uniform over representations of this one manifold. It is not uniform over diagram size, filling powers, or a sequence of different filled manifolds.

## 1. Statement and precise geometric inputs

Let \(X\) be an oriented complete finite-volume hyperbolic three-manifold with torus cusps, \(\Gamma=\pi_1(X)\), and \(\iota\) its marked complete projective holonomy. Consider representations
\[
 \rho:\Gamma\longrightarrow\mathrm{SL}_2(\mathbb C)
\]
whose peripheral projective images are parabolic or trivial. Central matrix signs are allowed. “Parabolic” means translation action at a common ideal fixed point; it excludes loxodromic peripheral groups.

Use the canonical signed representation volume of the original oriented fundamental class. Then its values on this representation space form a finite set. Moreover, there is \(\gamma_X>0\) such that every representation whose projective class is neither \(\iota\) nor its orientation reversal satisfies
\[
 |\operatorname{Vol}(\rho)|
       \le \operatorname{Vol}(X)-\gamma_X.
 \tag{1}
\]

The absolute bound and equality rigidity are inputs already proved in [the representation-volume gap note](https://sashakolpakov.github.io/murakamis_dream/notes/general_representation_volume_peripheral_gap.html). The construction and choice independence of canonical volume are in [the general peripheral proof](https://sashakolpakov.github.io/murakamis_dream/notes/general_peripheral_representation_volume_bound.html) and [the regular-critical-value proof](https://sashakolpakov.github.io/murakamis_dream/notes/regular_critical_values_and_representation_volume_bound.html), §§1–3. The proof below spells out the finite-value step, including singular peripheral strata, in the present geometric conventions. Componentwise volume constancy and finiteness are established facts, not new claims: [Garoufalidis–D. Thurston–Zickert, arXiv:1111.2828v2](https://arxiv.org/pdf/1111.2828v2), §1, pp. 2–3, states them and formulates the boundary-unipotent extension. Its Theorem 1.8 treats the projective quotient \(\mathrm{SL}_2/\{\pm I\}\), which accommodates our peripheral central signs. [Zickert, arXiv:0710.2049v2](https://arxiv.org/pdf/0710.2049v2), Definition 4.3, explicitly allows trivial ends; Theorem 6.10 and Definition 6.14 identify the decoration-independent regulator.

The convention is important. Our \(\operatorname{Vol}(\rho)\) is signed, equals the imaginary part of the Cheeger–Chern–Simons regulator, and equals the real part of the quantity called complex volume. The latter is \(\operatorname{Vol}+i\operatorname{CS}\). Thus the literature identity is \(\widehat c=i(\operatorname{Vol}+i\operatorname{CS})\); its real period ambiguity does not change volume. Projectively parabolic lifts need not be boundary-unipotent in \(\mathrm{SL}_2\): the preferred longitude may have trace \(-2\). The projective theorem, rather than only the version with peripheral diagonal entries \(+1\), is the appropriate comparison.

For the signed absolute bound and equality case, [Francaviglia, arXiv:math/0305275](https://arxiv.org/pdf/math/0305275), Theorems 5.1 and 7.2, gives precisely the finite-volume cusped setting. Proposition 4.18 records the sign change under reflection. We keep both complete orientation classes in (1). These citations record coverage; the finite-type, continuity, and path argument below remain explicit and do not replace a source-to-representation proof.

For a knot group, it suffices to impose trace squared four on its positive meridian. A noncentral parabolic has a parabolic centralizer, which contains its commuting longitude. If the meridian is projectively central, normal generation makes the whole projective representation trivial. This reduction is about the actual knot group.

## 2. Finite type and cusp flags along paths

A finite presentation makes the matrix representation space algebraic of finite type. At cusp \(i\), choose primitive generators \(\mu_i,\lambda_i\). Impose
\[
 (\operatorname{tr}\rho(\mu_i))^2=4,\qquad
 (\operatorname{tr}\rho(\lambda_i))^2=4.
 \tag{2}
\]
Because these two matrices commute, they are either simultaneously central or have a common parabolic fixed point. Thus these polynomial conditions describe exactly the desired peripheral locus.

As a real semialgebraic set, this locus has finitely many connected components, each joined by semialgebraic paths. A path can be partitioned into finitely many real-analytic arcs. Subdivide further where a peripheral generator changes between central and noncentral.

On an interval where one peripheral generator is noncentral, its eigenspace is the unique common peripheral flag. It is semialgebraic in the entries. A semialgebraic map into the compact projective line has one-sided endpoint limits. Where both generators are central, choose a constant flag. At a central transition the two one-sided flag limits may differ; §3 proves that they give the same volume.

Consequently each path has a finite subdivision on whose closed pieces the flags are continuous. Frames sending them to infinity can be chosen continuously in local unitary charts, and are bounded. A finite additional subdivision covers the needed frame charts. This does not diagonalize a parabolic matrix by dividing by an eigenvalue difference.

## 3. Continuity across reducible and trivial peripheral strata

Fix a closed path piece with those flags and bounded frames. On a fixed domain cusp use \((w,y)\in\mathbb C\times(Y,\infty)\) and its original translation lattice \(\Lambda_i\). In the chosen target frame each peripheral transformation is
\[
 z\longmapsto z+b_{i,\gamma}(t).
 \tag{3}
\]
These translations vary continuously and remain bounded. Let \(A_i(t)\) be the real-linear map taking the two domain lattice generators to their target translations. Its norm is bounded; rank one or zero is allowed. The explicit cusp map is
\[
 f_t(w,y)=g_i(t)^{-1}\bigl(A_i(t)w,y\bigr).
 \tag{4}
\]
It is exactly equivariant, with spatial Lipschitz constant at most \(\max(1,\|A_i(t)\|)\).

Extend across a fixed compact truncated core by a finite subdivision and equivariant geodesic interpolation, with a fixed joining collar. The finitely many matrix images needed for this interpolation and the boundary maps vary in compact sets. The construction therefore has one spatial Lipschitz bound over the closed parameter interval. It can be chosen continuous in the parameter, smooth on cell interiors, and with spatial differentials continuous almost everywhere. Hence
\[
 \left|f_t^*\operatorname{vol}_{\mathbb H^3}\right|
          \le C\,\operatorname{vol}_X.
 \tag{5}
\]
for one integrable majorant. Dominated convergence proves continuity of the canonical integral volume.

At a central peripheral endpoint, \(A_i=0\), so the cusp map is independent of \(w\). Changing the selected ideal flag there changes it by a homotopy with zero horizontal derivative, and hence zero boundary three-volume. Stokes on the truncated core proves independence of this choice. The one-sided limits from adjacent path pieces therefore agree. This proves continuity through singular peripheral types without asserting continuity of an individual ideal tetrahedron under an arbitrary simultaneous collision of its four vertices.

No irreducibility or nonzero peripheral translation was used.

## 4. Constancy on each regular path piece

The differential argument can be performed in a local finite-chain chart for every representation, not only near complete holonomy.

Triangulate a compact core and cone each boundary torus to its ideal cusp vertex. Take a barycentric subdivision. Every new tetrahedron contains at most one original prescribed cusp vertex. Its other barycentric vertices have trivial stabilizers and may be assigned generic auxiliary ideal flags, equivariantly. Their barycentric dimensions are distinct, so vertices in one tetrahedron are not forced into the same auxiliary orbit. Finitely many proper equality conditions can be avoided, giving four distinct developed flags in every tetrahedron. These choices persist on a small parameter interval.

This idealization computes the same canonical volume. First place the auxiliary vertices at finite developed points and straighten the original finite fundamental chain. Move the finitely many auxiliary positions to the chosen ideal flags. The face-compatible homotopies cancel on internal faces. The artificial vertex links are spheres and add no peripheral period. At the true cusps, the conical comparison and vanishing flux are those of §3. This is the finite-chain argument allowing auxiliary interior vertices in the regular-critical-value proof. It does not require an embedded or positive developed triangulation.

On the resulting local chart all cross-ratios avoid \(0,1,\infty\). Choose continuous logarithms
\[
 u_j=\operatorname{Log}z_j,\qquad
 v_j=\operatorname{Log}(1-z_j^{-1}).
 \tag{6}
\]
The edge shape products telescope by equivariance, so their logarithms are constant multiples of \(2\pi i\). The true peripheral similarities equal one, so their logarithms also are locally constant multiples of \(2\pi i\). The Bloch–Wigner differential is
\[
 d\sum_j\varepsilon_jD(z_j)
  =\sum_j\varepsilon_j
       \bigl(\operatorname{Re}u_j\,d\operatorname{Im}v_j
              -\operatorname{Re}v_j\,d\operatorname{Im}u_j\bigr).
 \tag{7}
\]
Here the signs are those of the oriented fundamental chain.

The local face and normal-curve cancellation reduces this pairing to the boundary pairing, exactly as in [the boundary regulator calculation](https://sashakolpakov.github.io/murakamis_dream/notes/boundary_regulator_period.html), §§2–3. Positivity is not used. Artificial sphere links have zero first homology and contribute no peripheral rows. On each true torus the remaining expression is
\[
 \frac12\bigl(\operatorname{Re}V_i\,d\operatorname{Im}U_i
              -\operatorname{Re}U_i\,d\operatorname{Im}V_i\bigr)=0.
 \tag{8}
\]
Indeed both peripheral similarities are identically one. Their continued logarithms are locally constant, with zero real parts; no branch is reset. This also follows directly by applying the edge-row cancellation to (7). The affine constants cause no term because they are purely imaginary and fixed.

Thus volume is locally constant on every regular arc, even at reducible representations. The construction uses neither smoothness of the representation variety nor nondegeneracy of a shape Hessian. Flat shapes other than \(0,1,\infty\) are permitted. Continuity from §3 joins these constants through the finitely many singular path endpoints.

It follows that volume is constant on each semialgebraic connected component. There are finitely many such components, proving the finite-value assertion.

## 5. The strict gap and a second proof

The universal volume bound gives \(|V|\le\operatorname{Vol}(X)\). Equality rigidity identifies the two maximal classes with the complete holonomy and its orientation reversal. Remove those values from the finite set. Its remaining largest absolute value is strictly smaller. The difference is \(\gamma_X\) in (1). The trivial representation has volume zero, so the remaining set is nonempty.

One can independently derive the gap from the already proved near-maximal convergence theorem. A hypothetical nongeometric boundary-parabolic sequence with absolute volumes tending to the maximum can, after fixing orientation and conjugating, converge to the complete holonomy. The marked peripheral logarithms are local coordinates there by [multicusp gluing rigidity](https://sashakolpakov.github.io/murakamis_dream/notes/general_marked_multicusp_gluing_rigidity.html), with its specified complete positive triangulation input. Fixing all meridian similarities to one leaves only the complete holonomy nearby. This contradicts the nongeometric condition. This alternative does not require a common compact normalization for all representations in advance.

For a simple-sphere long filling, \(X\) is the actual filled exterior supplied by [the Morse geometric contribution theorem](https://sashakolpakov.github.io/murakamis_dream/notes/actual_morse_geometric_contribution.html). Its original component test and primitive filling slopes remain fixed. Equation (1) concerns representations of \(\pi_1(X)\). A representation of the drilled exterior with only an exponentiated peripheral equation is not enough: a similarity-one slope at a parabolic auxiliary longitude need not be the identity element.

## 6. Consequence for the established regular full source

For the regular full charts already constructed, the source consequence needs no additional representation hypothesis. The relevant source theorem is [the full-critical-value theorem](https://sashakolpakov.github.io/murakamis_dream/notes/regular_critical_values_and_representation_volume_bound.html), §4. For the original marked braid scalar of a fixed filled hyperbolic knot, it proves that every regular full critical point, including its actual integer cut marks, supplies a boundary-parabolic representation \(\rho\) of the filled knot group and satisfies
\[
 \operatorname{Im}W_{\boldsymbol m}(Z)
      =\operatorname{Vol}(\rho),\qquad
 W_{\boldsymbol m}=W+2\pi i\sum_jm_j\operatorname{Log}A_j .
 \tag{9}
\]
The original exponential is \(\exp[NW_{\boldsymbol m}/(2\pi i)]\), so its real growth action is \(\operatorname{Im}W_{\boldsymbol m}/(2\pi)\). Combining that proved identification with (1) gives
\[
 \left|\operatorname{Im}W_{\boldsymbol m}(Z)\right|
     \le \operatorname{Vol}(X)-\gamma_X.
 \tag{10}
\]
whenever \(\rho\) is not geometric in either orientation. The gap is independent of the regular critical point and its integer marks, for this fixed knot.

Here is the dependency argument behind that implication; it matters for the word “full.”

1. The [wall-regulator note](https://sashakolpakov.github.io/murakamis_dream/notes/actual_wall_critical_regulator.html), §1, substitutes the nine physical scalar gates into the six output Gauss coordinates. They are exactly the positive and negative rational crossing maps in [marked braid holonomy](https://sashakolpakov.github.io/murakamis_dream/notes/marked_braid_holonomy.html), §§4–5. The latter's triangular factorizations, (5.1)–(5.3), transport the based meridians by the ordered Hurwitz relation. Their unchanged prefix products are what let adjacent maps compose in one based frame.
2. At each original cup or cap, stationarity includes its interval variable. The [coupled-cap source](https://sashakolpakov.github.io/murakamis_dream/notes/actual_coupled_caps_interval_source.html), §§4–5, gives \(z_2=-z_1\), \(B_2=B_1^{-1}\) at complete color and the based relation \(H_2H_1=I\). This is not the generally incorrect raw product \(G_2G_1\). Closing the original ordered diagram therefore imposes the full Wirtinger group relations of that knot.
3. A retained wall mark is an integer combination of logarithms of signed monomials in the original logarithmic head and Gaussian coordinates. Its derivatives shift logarithmic canonical equations by \(2\pi i\) times integer vectors. Exponentiation removes these shifts, leaving the same rational crossing and cap relations. The [exact cut-wall pushforward](https://sashakolpakov.github.io/murakamis_dream/notes/actual_full_psi_cut_wall_pushforward.html), §5, supplies those marks; the argument covers every such integer vector at any regular full critical point, without asserting that every vector occurs on the original cycle.
4. The action assertion is separate. Sections 2–3 of the wall-regulator note prove equality of the nine-atom and original five-atom Bloch–Wigner sums on the full regular rational crossing graph, fixing the constant on a real chart. With all Gaussian and cap variables retained, its identity is
   \[
   \operatorname{Im}W_{\boldsymbol m}
     -\sum_j\epsilon_jD(A_j)
      =(\operatorname{Re}Z)^t\operatorname{Im}\nabla W_{\boldsymbol m}.
   \]
   Full stationarity removes the right side. It would not vanish merely from stationarity on a constrained coefficient face.
5. The [crossing fundamental cycle](https://sashakolpakov.github.io/murakamis_dream/notes/crossing_fundamental_cycle.html), §§3–5, is the degree-one relative cycle of the original exterior, with the based Hurwitz transports and the preferred-longitude writhe shear. Its explicit five-term identities are representation-independent. Section 5 of the wall-regulator note applies them to nonfaithful representations, sending repeated developed vertices to zero in the normalized configuration complex. This gives (9) with the original oriented fundamental class. Noncentral complete meridians have unipotent projective centralizers; a central knot meridian gives the trivial projective representation by normal generation.

This is a statement about regular full critical charts of the original marked knot scalar, including their retained integer wall marks. It does not say that all integer-mark charts occur with nonzero cycle coefficient, that a separated coefficient sector has these group equations, or that wall terms are negligible. “Regular” excludes escaping positions, zero denominators, and singular or rank-deficient constrained strata; “full” retains all head, Gaussian, and cap variables.

This covers arbitrary presentations of that actual knot on those full critical charts. In particular it is not restricted to tree diagrams. The regular finite cap-endpoint strata covered in §5 of the same source theorem have critical value zero, so they also lie strictly below the positive geometric rate.

Neither conclusion identifies a constrained stationary point of a LEFT/RIGHT coefficient support with a full critical point. The regularity hypotheses retain every head and cap coordinate and all logarithmic shapes. Infinite positions, escaping critical sequences outside these charts, and singular endpoint contributions remain separate. A large face-envelope value is not a counterexample to (10).

## 7. A direct filled-period criterion, and what it does not supply

Let \(R_N\) be the original filled period minus the all-CROSS term. Suppose its exact relative-cycle decomposition retains every endpoint and connector current and satisfies the following conditions for this one fixed filling.

* Every regular critical chart represents \(\pi_1(X)\), has parabolic main peripheral image, and excludes the geometric and orientation-reversed geometric classes.
* Its fully normalized action satisfies \(2\pi\operatorname{Re}S=\operatorname{Vol}(\rho)\), with the original fundamental class and primitive filling correction.
* There are \(e^{o(N)}\) relevant pieces. Their measures and amplitudes are bounded by \(e^{o(N)}\), uniformly, and each deformed piece has phase real part at most its represented critical value plus \(o(1)\).
* The remaining tail and singular-stratum currents have a direct bound \(\exp[N(\operatorname{Vol}(X)/(2\pi)-\eta)+o(N)]\), for some \(\eta>0\).

Then (1) and the triangle inequality give
\[
 |R_N|\le
 \exp\left[N\left(\frac{\operatorname{Vol}(X)}{2\pi}
        -\min\left\{\frac{\gamma_X}{2\pi},\eta\right\}\right)+o(N)\right].
 \tag{11}
\]
This compares with the filled volume directly; it does not require an earlier supremum gap below the augmented action.

The conditions are not consequences of rigidity. A finite sector label is not a representation invariant. Different pieces may reach the same geometric representation, and an endpoint maximum need not solve the full group equations. The [half-charge calculation](md-filled-complement-half-charge-obstruction.md) retains an explicit factor that must be included before writing a one-sided sector's stationary filling equation.
