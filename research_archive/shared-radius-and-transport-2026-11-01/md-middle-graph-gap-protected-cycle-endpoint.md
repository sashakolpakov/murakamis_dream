# An endpoint gap when the marked pair meets every middle cycle

This note extends the positive endpoint argument to a finite class of the original matched-sphere Morse sources. It keeps the diagram and all coefficient targets. Its graph condition concerns the original reduced mark; it does not add tangles, change a filling power, or replace the diagram by a tree.

The conclusion is an endpoint entropy theorem and an absolute estimate on a small spectral polydisk. It is not a bound on the full real spectral cube or the original long-filling remainder.

## 1. The marked source and the graph condition

Let \(\mathcal T\) be a finite simple triangulated oriented sphere, with a perfect matching of its cubic dual. Each matched pair of triangles has the original ordered homogeneous coupon
\[
 H_p(x_e,b_e,c_e,y_e).
 \tag{1}
\]
Its shared white edge is \(x_ey_e\); the two middle faces are \(b_e,c_e\). The cyclic quadrilateral is \((x_e,b_e,y_e,c_e)\). Let \(R\) be the number of coupons. There are \(R+2\) white vertices. Mark a nonmatching white edge \(uv\). The original coefficient target is zero at \(u,v\) and \(d=N-1\) at every other face.

Use the actual inverse-cut diagram in \(S^3\), its prescribed terminal pairings and disk frames, as in [the Morse geometry theorem](/private/tmp/murakamis_dream-publication/notes/actual_morse_geometric_contribution.md), §§1–3. The source is the corresponding Morse contraction, not a tensor assigned only from an abstract incidence matrix. The complete untwisted augmented exterior is \(Y_D\), and
\[
 \Phi_D=\frac{\operatorname{Vol}(Y_D)}{2\pi}.
 \tag{2}
\]
The simple-sphere packing theorem supplies its labeled positive right-angled certificate. Retained half twists have the same complete polyhedron volume; the positive endpoint coupon below is nevertheless kept in its own stated source normalization. Any assertion about the filled knot retains the separate original component test.

The **middle graph** \(G\) has all white vertices and one edge \(b_ec_e\) for each coupon. Multiple edges remain distinct. A middle edge is drawn through its matched quadrilateral, crossing the original matching diagonal once. These arcs have disjoint interiors. It can equivalently be regarded as the collection of new diagonals after simultaneously flipping the matched white edges, with all labels and orders retained.

Assume
\[
                     G-\{u,v\}\ \text{is a forest}.
 \tag{3}
\]
Thus every cycle, including a two-edge multicycle, meets the original protected pair. The condition is a finite graph test. It is weaker than the flat-plat gap property that every middle cycle contains one particular exterior vertex.

For the original polynomial numerator
\[
 V_N(\sigma;\Omega)=
 \frac{\chi_N(\sigma)-\chi_N(\Omega)}{\sigma-\Omega},
 \qquad \chi_N(z)=2T_N(z/2)+2,
 \tag{4}
\]
use the positive reference coupon
\[
 F_N=
 \begin{cases}
 -V_N(-2;\Omega),&N\ \text{even},\\
 V_N(-2;\Omega)-N^{-2}\partial_\sigma V_N(-2;\Omega),
       &N\ \text{odd}.
 \end{cases}
 \tag{5}
\]
The quotient in (4) is polynomial; its repeated-node normal data are retained. Let \(Z_{F,N}\) be the original shared target coefficient of \(\prod_eH_{F_N}\).

**Endpoint theorem.** Under (3), the full incidence entropy has a unique maximum at the labeled complete all-CROSS flow \(q^{\mathrm{geom}}\), and
\[
 \lim_{N\to\infty}\frac1N\log Z_{F,N}=\Phi_D.
 \tag{6}
\]
There is a fixed \(\gamma_D>0\) such that the positive sum \(Z_{F,N}^{\mathrm{nc}}\) of all original assignments with at least one non-CROSS coupon satisfies
\[
 Z_{F,N}^{\mathrm{nc}}
       \le \exp\{N(\Phi_D-\gamma_D+o(1))\}.
 \tag{7}
\]
An empty complementary support means the sum is zero. Both parities are covered by their precise coupons in (5). The constants may depend on the entire fixed diagram and mark.

## 2. What the incidence restriction proves, and what it does not

For any selected set \(E_0\) of middle edges, let \(C\) run through its connected components containing an edge. Write \(e_C,v_C,p_C\) for its numbers of edges, vertices, and protected vertices. An ordinary target can receive at most one exponent strictly greater than \(d/2\); a protected target can receive none. A non-CROSS coupon has exactly one such middle exponent. Therefore the number of CROSS coupons in \(E_0\) is at least
\[
 \sum_C\max\{0,e_C-v_C+p_C\}
   =\sum_C\max\{0,\beta_C+p_C-1\},
 \qquad \beta_C=e_C-v_C+1.
 \tag{8}
\]
This is the optimal conclusion from the middle-edge assignment problem alone. If \(p_C>0\), choose a spanning forest with one protected root in each tree and orient its edges away from the roots. Its \(v_C-p_C\) edges have distinct ordinary heads. If \(p_C=0\) and \(C\) has a cycle, orient a spanning unicyclic subgraph cyclically and its attached trees outward, obtaining \(v_C\) distinct heads. If it is a tree, orient it from any root, obtaining \(e_C=v_C-1\) heads. These choices attain \(\min(e_C,v_C-p_C)\). No claim is made that every such edge assignment satisfies the remaining four-face source equations.

The stronger use of (3) is for **pure-middle** coupons, which have zero total outer load and total middle load one. For any component \(C\) of a feasible pure-middle subgraph,
\[
                    e_C\le v_C-p_C.
 \tag{9}
\]
If it contained a cycle, (3) would make that cycle contain a protected vertex, so \(p_C\ge1\) and \(e_C\ge v_C>v_C-p_C\), a contradiction. Thus it is a forest. A tree component cannot contain both protected vertices, since \(v_C-1>v_C-2\).

This is not an entropy estimate for arbitrary non-CROSS coupons. The subsequent proof uses the exact positive endpoint function and the geometry of the original complement.

## 3. Removing pure-middle maxima without changing the target

The uniform full-kernel and odd regularization theorems give one continuous function \(h\) on the closed local degree simplex, at both parities. Its CROSS branch is the maximum of the sum of two triangle entropies. Its one-sided branch is the original difference of two triangle entropies, with the same outer tilt. On the pure-middle segment it is zero.

Let \(Q_D\) be the compact nonnegative incidence-flow polytope: each coupon supplies one, each ordinary face demands one, and both protected faces demand zero. The original uniform coefficient theorem, positivity, and integral transportation rounding give
\[
 W_D=\lim_{N\to\infty}\frac1N\log Z_{F,N}
    =\max_{q\in Q_D}\sum_e h(q_e).
 \tag{10}
\]
All four local incidences remain separate, even when smoothing later identifies their global face labels. There are only polynomially many integral arrays for fixed \(D\). The rounding is in the coupon-to-face transportation graph and does not assume that the middle graph is a tree.

The all-CROSS comparison and original positive complete-source theorem give \(W_D\ge\Phi_D\). Choose a maximum and let \(J\) contain every pure-middle coupon, including the pure-middle CROSS seam. Replace precisely these coupons at the entropy level by the literal identity polynomial
\[
                     H_1(b,c)=\sum_{i=0}^d b^ic^{d-i}.
 \tag{11}
\]
The common maximizing flow is unchanged and has the same entropy. Conversely the mixed positive coefficient is bounded by the full positive source up to a fixed-diagram polynomial factor, using the exact diagonal comparison. Thus the mixed source has rate \(W_D\). This argument includes the limiting pure-middle seam through the full continuous entropy; it does not invent a finite CROSS monomial with zero outer degree.

By §2 the identity subgraph is a forest with at most one protected vertex per component. Contract each component to an ordinary face if it contains no protected vertex, and otherwise to a protected face. For a rooted identity edge, let \(L\) be the total remaining load in its child subtree. Its two identity loads are exactly
\[
                \sigma_{\mathrm{child}}=1-L,
                \qquad \sigma_{\mathrm{parent}}=L.
 \tag{12}
\]
They lie in \([0,1]\); the remaining load of a whole ordinary tree is one and that of a protected tree is zero. Subtree balance proves uniqueness. At level \(N\), replace one by \(d\) in (12); the integer identity coefficient is one. Hence contraction identifies the face variables and preserves the one ordinary \(d\)-target or protected zero target exactly, without a counting multiplicity.

This is also the literal connected identity smoothing. In the flipped white sphere a regular neighborhood of each embedded middle tree is a disk. Collapsing it merges precisely its incident white faces, retaining their induced cyclic orders. Equivalently delete the corresponding physical untwisted crossing disks one at a time from a leaf of the tree. The two ordered strand pairs then coincide. A tree contraction creates neither an extra component of the cut sphere nor an annular identification. This is the only part of the existing forest argument that used the special flat-plat gap graph; (3) now supplies its needed hypothesis.

The remaining cellulation is loopless. If a loop enclosed \(k\) ordinary vertices on its mark-free side, the actual dual parity count would give \(k-1\) whole retained coupons and one inside half of a matching bridge. Their target \(k\) would force that bridge middle load to be one and all its other loads zero. It would be another pure-middle coupon, contrary to the definition of \(J\). Likewise a retained matching edge cannot join the two protected merged faces: it would have zero outer load. The original nonmatching edge \(uv\) survives with distinct endpoints, since no identity tree contains both.

These arguments depend on the embedded sphere and the literal perfect matching, not a constant number of Morse heads.

## 4. Hybrid regularity and the original representation

After the identity contractions the white object is a loopless triangular sphere, possibly with parallel edges. At the inherited maximum tag terminal seams CROSS, retain each CROSS coupon's two half-supply triangle nodes, and retain every strict one-sided coupon as one full-supply node. Its entropy remains the difference of the two original triangle values; it is not split into independent positive pieces.

The [hybrid tight-cut theorem](/private/tmp/murakamis_dream-publication/notes/actual_fejer_hybrid_tight_cut_reduction.md) is stated exactly for this loopless sphere. Its proof is independent of flat-plat gaps. For a proper nonempty ordinary-vertex set \(S\), the induced graph on its complement has at most \(2|V\setminus S|-4\) original triangular faces. Equality forces connectedness and genuine digon holes. Merging a one-sided pair never lowers Hall capacity; hybrid equality merges neighboring holes only across whole one-sided coupons. The remaining cuts are strand/strand digons, or matching/matching digons with both crossing coupons CROSS.

Cut along those actual disks. Each piece keeps two adjacent protected boundary labels. The feasible hybrid polytope and its entropy split as a Cartesian product: no strict one-sided coupon is cut. On each piece the reserve-\(\varepsilon\) Hall argument supplies a common witness positive on every non-forced ordinary incidence. Mixing toward it stays within the strict one-sided intervals and the CROSS triangle simplexes. The proved corner expansions produce nonnegative \(\varepsilon\log(1/\varepsilon)\) terms, and a positive one at any free ordinary zero. Maximality excludes such zeros. Finite row-space multipliers now give positive finite ordinary curvatures and the two recorded zero curvatures.

The resulting signed center triangles develop in one cooriented strip on each piece. Around each finite white vertex the signed angle sum is zero or \(2\pi\), so the full Euclidean star holonomy is the identity. Removing one positive marked triangle gives a disk; its dual cycles are generated by these stars. The propagated two marked lines therefore close the omitted triangle. This proves one white reflection for every label occurrence on that piece, including a piece marked at a matching cut.

To glue the pieces, map each child's ordered tangent pair to its parent's pair by one Möbius map. Across a split original CROSS coupon the outer parabolic product is common. Its centralizer uniquely carries the whole ordered pair of raw meridians and all three contact flags from one triangle to the other. Strict one-sided coupons retain their explicit unsplit Green collar map. The [hybrid representation proof](/private/tmp/murakamis_dream-publication/notes/actual_fejer_hybrid_piece_representation.md), §§2–5, supplies these maps and the zero-volume restoring caps.

Here the actual Morse words must be retained. On a sweep the white transitions are the original products \(R_F^+R_G^-\). At a cup or cap the region sequence \(F,G,F\) inserts
\[
                  R_F^+R_G^-R_G^+R_F^-=I.
 \tag{13}
\]
Thus the same based prefix survives a change of head count. At every physical coupon the whole-pair conjugacies are those of its four-crossing threading collar, in its recorded input/output order. These are the local identities proved in [the Morse geometry theorem](/private/tmp/murakamis_dream-publication/notes/actual_morse_geometric_contribution.md), §5, together with the signed Green formulas. Neither step requires a flat sweep.

The original projection and crossing-disk cut consists of two balls. The digon disks are proper disks in these same balls. Their extra chain pieces collapse at a common contact horosphere with zero limiting volume. One global reflection supplies the second ball. Signed cyclic polygon coning therefore computes the original relative fundamental class, with degree one:
\[
                   \operatorname{Vol}(\rho)=2\pi W_D.
 \tag{14}
\]
This is the full sewn chain calculation, not invariance of an open crossing regulator after resetting its reference flag.

Restoring every deleted original auxiliary meridian as identity gives a representation of \(\pi_1(Y_D)\), with the same relative volume. Its retained outer product may be axial, parabolic, or central; the corresponding zero-volume cap is used, rather than imposing a new tangency. The representation-volume inequality gives \(W_D\le\Phi_D\), proving equality in (10).

If \(J\ne\varnothing\), this representation kills an essential original auxiliary meridian. The strict killed-meridian volume gap makes (14) strictly smaller than \(\operatorname{Vol}(Y_D)\), a contradiction. Hence a maximum has no pure-middle coupon. This last argument is now justified by the forest reduction; it was not assumed before (3).

## 5. Equality determines the labeled configuration

With no identity deletion, the white sphere is the original simple sphere. Its induced-graph equality case has no proper digon tight set. The previous regularity argument consequently develops one signed circle family on the original labels. Equation (14) and equality rigidity identify its representation with the marked complete holonomy, by an orientation-preserving conjugacy.

The actual based peripheral words determine the contacts:

* At a strand contact, the based main meridian is noncentral parabolic and fixes precisely that contact.
* At a matching contact, the ordered product \(P=BA\) is the noncentral parabolic preferred auxiliary longitude, and its unique fixed point is that contact.

These are the words from the original cut and its Morse prefixes. They are not freely selected conjugacy classes. Under the conjugacy to complete holonomy, every labeled contact therefore goes to its corresponding complete contact.

Every original white face in the positive simple-sphere certificate has at least three distinct contacts. Their ideal points determine its generalized circle uniquely. Normalize both marked contacts to infinity. The conjugacy then is affine, and carries the ordered pair of marked lines to the ordered complete pair. Ordinary source circles bound disks on the prescribed inward side of these lines. Thus it preserves the disk choice as well as the circles.

The resulting center triangles have the complete cyclic signs. A strict one-sided coupon would contain a negatively signed triangle whose middle is ordinary and overloaded. Such a triangle has either three finite circles or one cooriented line and two finite circles. The two-line case would overload a protected middle and is impossible. In either permissible case the sign is fixed by the recovered labeled configuration, contradicting the negative sign. Hence every maximizing coupon is CROSS and every triangle angle is its complete angle. This also excludes terminal seams: each complete middle angle is strictly less than \(\pi\), because its matching outer edge cannot be the marked strand edge.

This proves uniqueness of \(q^{\mathrm{geom}}\). On the compact closed set
\[
 \mathcal B_D=\{q\in Q_D:
      q_{e,b}\ge\tfrac12\ \text{or}\ q_{e,c}\ge\tfrac12
      \text{ for some }e\},
 \tag{15}
\]
continuity gives
\[
 \max_{\mathcal B_D}\sum_e h(q_e)=\Phi_D-\gamma_D
                  <\Phi_D.
 \tag{16}
\]
if the set is nonempty. Every finite non-CROSS assignment at either parity, normalized by \(d\), lies in this set. Uniform local coefficient asymptotics and positivity now prove (7).

## 6. What transfers to nearby spectra

Let \(\Delta_N(\boldsymbol\sigma)\) be the full original shared numerator minus its all-CROSS part, with no change of mark or target. The support-preserving path comparisons in [the spectral-polydisk theorem](/private/tmp/murakamis_dream-publication/notes/actual_fejer_spectral_polydisk_complement.md) use only the local polynomial (4). They are therefore valid here before shared extraction.

Put \(\theta(r)=\operatorname{arcosh}(1+r/2)\). For fixed bounded \(r_e\ge0\),
\[
 \sup_{|\sigma_e+2|\le r_e}|\Delta_N(\boldsymbol\sigma)|
 \le
 \exp\left\{
 N\left(\Phi_D-\gamma_D+\sum_e\theta(r_e)+o(1)\right)
 \right\}.
 \tag{17}
\]
At odd levels the extra \(\prod_e\max(1,N^2r_e)\) is polynomial and is included in \(o(N)\). In particular a sufficiently small fixed polydisk has a strict endpoint-scale loss. At radii \(r_e=N^{-2}\), Cauchy gives the exact comparison
\[
 |\partial_{\boldsymbol\sigma}^{\alpha}\Delta_N(-2,\ldots,-2)|
 \le e^R\alpha!N^{2|\alpha|}Z_{F,N}^{\mathrm{nc}}.
 \tag{18}
\]
These are fixed-root spectral derivatives. No genuine-\(q\) derivative is inferred.

The full filling contour still sees the remaining spectra and every original pole and connector current. Equations (17)–(18) do not move that contour into this polydisk. They prove no full remainder estimate for the original filled invariant.

## 7. An unchanged cyclic family

Take the oriented even bipyramid, \(m\ge6\),
\[
 (N,v_j,v_{j+1}),\qquad(S,v_{j+1},v_j),
 \qquad j\in\mathbb Z/m.
 \tag{19}
\]
Match \(Nv_j\) for odd \(j\), and \(Sv_j\) for even \(j\). The original ordered source factors are
\[
 \begin{cases}
 H_p(N,v_{j-1},v_{j+1},v_j),&j\ \text{odd},\\
 H_p(S,v_{j+1},v_{j-1},v_j),&j\ \text{even}.
 \end{cases}
 \tag{20}
\]
The reversed middle order on the south side is retained.

Choose the original equatorial strand mark \(v_0v_1\). Then the middle graph consists of the cycle on the even rim vertices and the disjoint cycle on the odd rim vertices, together with isolated \(N,S\). Deleting \(v_0,v_1\) breaks both cycles, proving (3). Thus (6)–(18) hold for every even \(m\), without a terminal insertion or a changed twist.

This literal marked source is not covered merely by the flat-plat gap lemma: its two vertex-disjoint middle cycles cannot both contain one exterior vertex. This is a distinction between source presentations, not a claim that the underlying knots are outside every previously proved knot class. The original matched-sphere terminal-pairing construction supplies knot-producing parity patterns; any filled-knot statement must retain the selected pattern's component test.

For a spoke mark \(Nv_0\), the even rim cycle meets \(v_0\), but the odd rim cycle is unprotected. Condition (3) fails there. The theorem does not replace the spoke-mark coefficient by the equatorial one: its proof uses the explicitly chosen original equatorial targets from the start.

### Transporting the full source back to another original mark

The all-mark theorem is an exact statement for arbitrary full polynomial coupons, including the complete numerator and its spectral derivatives. Its proof uses the spherical generic pivotal lift, keeps every original coupon disk and its frame fixed, and then specializes the regular finite matrices at the root. Section 4 of [the matched-sphere Morse construction](/private/tmp/murakamis_dream-publication/notes/research_matched_sphere_morse_source.md) supplies it for these diagrams, without assuming an earlier flat plat.

Consequently, for any two original strand marks \(a,b\),
\[
 S_N^{(a)}(\boldsymbol\sigma)=S_N^{(b)}(\boldsymbol\sigma),
 \qquad Z_{F,N}^{(a)}=Z_{F,N}^{(b)}.
 \tag{22}
\]
There is no additional mark-dependent scalar. All original peripheral and exterior framing factors remain the same. Equation (22) does not assert equality of the two all-CROSS projections or their complementary sums.

If mark \(a\) satisfies (3), the proven conclusion for every other original mark \(b\) is
\[
 S_N^{(b)}(\boldsymbol\sigma)
   =S_{N,\mathrm C}^{(a)}(\boldsymbol\sigma)
     +O\!\left(e^{N(\Phi_D-\gamma_D/2)}\right)
 \tag{23}
\]
on a sufficiently small fixed polydisk. The all-CROSS complex packet for mark \(a\), supplied by [the Morse analytic theorem](/private/tmp/murakamis_dream-publication/notes/actual_morse_cross_filling_period.md), therefore gives a local geometric packet for the full source, with the exact normalization in (22). This conclusion may be transferred to a spoke mark of the bipyramid. It does not identify that spoke mark's own CROSS or non-CROSS pieces.

Thus the source class for a full endpoint rate or local full packet can be stated intrinsically as diagrams admitting at least one original strand edge whose endpoints meet all middle cycles. The remainder estimate (7) is asserted for the qualifying marked decomposition. No topological operation changes the original knot in this use of (22).

## 8. The remaining unprotected-cycle issue

A feasible pure-middle subgraph on a general marked sphere may have an unprotected unicyclic component. Summing its loads shows that all targets on that component are exhausted by its identity edges; every other incidence there is zero.

Contract a spanning tree of such a component. The one remaining identity edge is a loop, and its exact contribution is
\[
                       H_1(L,L)=N L^d.
 \tag{21}
\]
Extracting its ordinary target therefore sets the remaining total \(L\)-degree to zero and produces a factor \(N\). This is a valid polynomial reduction, but not the earlier ordinary-face tree contraction: the merged face has become a new zero target.

The final embedded loop separates the flipped white sphere. To extend the proof beyond (3), one must identify its two actual cut pieces, their inherited marks and group maps, and show that their entropy and degree-one chains glue with exactly the new zero target. These are additional geometric obligations. A polynomial factor \(N\) alone does not settle them. In particular the existing forest proof cannot silently be applied to an unprotected identity cycle.

Finally, Hall alone is not a quantitative spectral estimate. Formula (8) is optimal as an incidence assignment statement and gives no weight to a surviving excursion. Even an exact forest expansion can have individual source channels above the geometric rate, as proved for the original figure-eight expansion in [the forced-source entropy obstruction](/private/tmp/murakamis_dream-publication/notes/actual_forced_source_tree_entropy.md). That is a different exact expansion, not a counterexample to (6); it excludes a general inference from a forest label to a sharp absolute term bound. The new theorem instead uses positive endpoint entropy, the original group representation, and its fixed labeled geometric equality case.
