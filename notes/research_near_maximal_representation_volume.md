# A uniform volume gap away from geometric holonomy

Research note, 3 November 2026.

The signed action-volume identity bounds every identified regular
critical representation by the hyperbolic volume. Here that bound is
made uniform away from the complete holonomy. In particular, a sequence
of representations escaping every neighborhood of that holonomy cannot
have volumes approaching the maximum.

This is an established rigidity phenomenon. Francaviglia and Savini
state the sequence theorem, in greater generality, in
[*Volume rigidity at ideal points of the character variety of hyperbolic
3-manifolds*](https://arxiv.org/abs/1706.07347), published in 2020.
That reference supplies coverage and attribution. The proof below
extends the natural-map argument already written in this repository;
it does not assume the cited proof. There is no novelty claim for the
general rigidity theorem.

## 1. The representations and the precise conclusion

Let \(M=\Gamma\backslash\mathbb H^3\) be an oriented complete
finite-volume hyperbolic three-manifold. Write
\(\iota:\Gamma\longrightarrow\mathrm{PSL}_2(\mathbb C)\) for its
oriented holonomy and \(V=\operatorname{Vol}(M)>0\).
Consider representations whose image on each cusp fixes an ideal
point and is either parabolic or preserves a geodesic axis with its
endpoints individually fixed. Trivial peripheral images are allowed.
These are precisely the peripheral types needed below; no peripheral
group interchanging the two endpoints is silently treated as axial.
The marked critical representations in Section 4 have complete main
cusps and therefore satisfy this requirement.

Use the representation volume defined by the cusp-adapted equivariant
maps in
[the peripheral-volume proof](general_peripheral_representation_volume_bound.md).
Its normalization is the signed volume of the same oriented
fundamental chain.

**Theorem 1.** Suppose \(\rho_j\) are representations of the indicated
type and
\[
                  \operatorname{Vol}(\rho_j)\longrightarrow V.
 \tag{1}
\]
There are a subsequence and orientation-preserving target isometries
\(h_j\) such that
\[
                     h_j\rho_j(\gamma)h_j^{-1}
                            \longrightarrow\iota(\gamma)
                   \qquad(\gamma\in\Gamma).
 \tag{2}
\]
Convergence on a fixed finite generating set is sufficient in (2).

The subsequence formulation is enough for the uniform gap we will use.
It makes no initial compactness assumption on the representations,
their chosen conjugations, or their peripheral translation lengths.

**Corollary 2.** Let \(\mathcal U\) be a conjugacy-invariant open
neighborhood of \(\iota\) in the representation space. There is a
\(\delta=\delta(M,\mathcal U)>0\) such that every representation of
the indicated type outside \(\mathcal U\) satisfies
\[
                  \operatorname{Vol}(\rho)\le V-\delta .
 \tag{3}
\]
For a neighborhood of both oriented holonomies, the corresponding
statement holds with \(|\operatorname{Vol}(\rho)|\).

Indeed, failure of (3) would give a sequence outside \(\mathcal U\)
satisfying (1). A conjugacy-invariant neighborhood contains all
sufficiently late terms of its normalized convergent subsequence,
which is a contradiction. For the absolute statement, pass to a
subsequence with one sign and, if necessary, compose with a fixed
orientation-reversing target isometry.

## 2. Which estimates are uniform when the representation varies

For each \(\rho_j\), choose its cusp-adapted equivariant map \(f_j\).
For \(s>2\), the
[natural-map construction](general_representation_volume_kernel_strictness.md),
Sections 1--2, takes the barycenter of
\[
 \nu_{j,x}^{\,s}
   =Z_s^{-1}\int_{\mathbb H^3}
          e^{-s d(x,y)}\mu_{f_j(y)}\,dy,
 \qquad
 Z_s=\int_{\mathbb H^3}e^{-s d(x,y)}\,dy .
 \tag{4}
\]
Here \(\mu_z\) is the probability visual measure at \(z\).
The resulting map \(F_{j,s}\) is \(\rho_j\)-equivariant.
The measures have no atoms and have full support, so their Busemann
potentials have a unique barycenter.

Retain the tensors from that proof,
\[
 H=\mathbb E[vv^T],\qquad A=\mathbb E[v\eta^T],\qquad B=I-H.
\]
The vectors \(v\) and \(\eta\) are unit target Busemann gradients and
unit radial domain gradients, respectively. The established identities
and inequalities are
\[
 B\,dF_{j,s}=sA,\qquad
 AA^T\le H/3,\qquad
 \operatorname{Jac}F_{j,s}\le
       |\operatorname{Jac}F_{j,s}|\le(s/2)^3,
 \qquad
 \int_M\operatorname{Jac}F_{j,s}=\operatorname{Vol}(\rho_j).
 \tag{5}
\]
The matrix inequality giving the Jacobian maximum is strict unless
\(H=I/3\). Near that maximum it also forces every singular value of
\(dF_{j,s}\) to be near \(s/2\). Along \(s_j\downarrow2\), these
singular values therefore tend to one.

Three facts about uniformity are essential.

First, for \(2<s\le3\), the first two derivatives in \(x\) of (4)
are bounded in total variation by constants independent of \(f_j\).
Differentiation acts on the radial kernel, while each
\(\mu_{f_j(y)}\) has mass one. The only apparent second derivative
singularity is \(\coth d(x,y)\); its radial expectation is \(s/2\).
These are the bounds explicitly established after equation (3) of
the natural-map proof.

Second, on a ball where \(B\ge\kappa I\), implicit differentiation
of the barycenter equation therefore bounds \(dF_{j,s}\) and its
first covariant derivative by constants depending only on \(\kappa\)
and the indicated interval of \(s\). Target Busemann derivatives
have universal bounds. Also
\(\|\nabla H\|\le C(1+\|dF_{j,s}\|)\). Starting with \(H\) near
\(I/3\), these bounds give a source radius independent of \(j\) on
which \(B\) stays uniformly positive. Target normalization fixes a
map value and gives ordinary local \(C^2\) bounds on this ball.

Third, the last equality in (5) is proved separately for each fixed
\((j,s)\). Its cusp-flux constants may depend on both. No uniform
cusp estimate is required here: we use the equality only after it
has been proved, and never exchange a limit in \(j\) or \(s\) with
a cusp truncation.

## 3. The isometric limit and the convergence of the representations

Choose \(s_j\downarrow2\), with \(s_j\le3\), and put \(F_j=F_{j,s_j}\).
Equations (1) and (5) give
\[
 \int_M\left[(s_j/2)^3-\operatorname{Jac}F_j\right]
      =(s_j/2)^3V-\operatorname{Vol}(\rho_j)\longrightarrow0 .
 \tag{6}
\]
The integrand is nonnegative and \(\Gamma\)-invariant.
Its integral on every fixed compact subset of the universal cover
also tends to zero. To see this, cover that compact set by finitely
many balls on which the covering map is injective and apply (6)
to their projections.

In a fixed relatively compact source ball, choose points \(x_j\)
where the integrand in (6) tends to zero. Pass to a subsequence so
that \(x_j\to x_0\) in the interior of a slightly larger fixed ball.
Then \(\operatorname{Jac}F_j(x_j)\to1\).
The strict matrix maximum in (5) implies \(H_j(x_j)\to I/3\).
Choose orientation-preserving target isometries \(a_j\) sending
\(F_j(x_j)\) to a fixed target point, and set \(G_j=a_jF_j\).
The uniform local bounds of Section 2 apply on a fixed neighborhood
of \(x_0\). A subsequence converges there in \(C^1\).

The limiting Jacobian is identically one. Indeed the Jacobians
converge uniformly there, and (6) says that their nonnegative
deficits have integrals tending to zero. At each point, equality
in the limiting matrix bound forces \(H=I/3\) and makes the
derivative an orientation-preserving isometry. Thus the limit is
a local hyperbolic isometry.

This convergence extends along any fixed finite chain of overlapping
source balls. At a point in an existing overlap, convergence of the
Jacobian to one again makes \(H_j\) approach \(I/3\). The same
uniform-radius argument opens the next ball. Values there stay
bounded because one overlap value is already bounded and the
derivative is bounded. A diagonal extraction over a compact
exhaustion of \(\mathbb H^3\) gives
\[
                         G_j\longrightarrow g
                              \quad\hbox{in }C^1_{\rm loc}.
 \tag{7}
\]
The limit is a local hyperbolic isometry everywhere. It agrees on
its first ball with the unique global orientation-preserving
hyperbolic isometry having the same value and derivative at one
point. Uniqueness of isometries on overlapping balls makes it agree
with that isometry along every path. We continue to denote this
global isometry by \(g\).

It remains to recover the representations, rather than just their
maps. Define \(\sigma_j=a_j\rho_j a_j^{-1}\). Equivariance gives
\[
                  \sigma_j(\gamma)G_j(x)=G_j(\gamma x).
 \tag{8}
\]
For a fixed \(\gamma\), (7) shows that both sides specify bounded
images of a fixed basepoint, up to a displacement tending to zero.
The stabilizer of a point of \(\mathbb H^3\) is compact, so the
isometries \(\sigma_j(\gamma)\) lie in a relatively compact set.
Every subsequential limit \(\sigma_\infty(\gamma)\) satisfies
\[
                 \sigma_\infty(\gamma)g(x)=g(\gamma x)
                                    \quad(x\in\mathbb H^3)
\]
by (7)--(8). Hence that limit is uniquely
\(g\,\iota(\gamma)\,g^{-1}\). This proves convergence for every
generator, and therefore for every fixed group element.
Taking \(h_j=g^{-1}a_j\) proves Theorem 1.

## 4. Consequence for the original regular critical actions

Fix one original integer filling whose knot complement \(M\) is
hyperbolic. Section 9 of the
[signed action-volume calculation](research_positive_edge_volume_identity.md)
constructs a representation \(\rho_\xi\) from every regular
continued critical configuration \(\xi\) satisfying its full
primitive filling conditions and nonunit selected longitude
conditions. It proves the absolute normalization
\[
                 2\pi\Re\mathcal S(\xi)
                              =\operatorname{Vol}(\rho_\xi).
 \tag{9}
\]
The remaining main cusps are complete. Corollary 2 therefore gives
the uniform bound
\[
 \rho_\xi\notin\mathcal U
 \quad\Longrightarrow\quad
 \Re\mathcal S(\xi)
          \le\frac{\operatorname{Vol}(M)-\delta}{2\pi}.
 \tag{10}
\]
There is no requirement here that the compared critical set be
finite, bounded in shape coordinates, or zero dimensional.
The bound also survives limits of such real action values. It does
not automatically identify every singular limiting shape assignment
with a representation.

This removes one possible source of loss of a strict comparison:
regular critical representations cannot escape while their actions
approach the maximal geometric action. It leaves three questions
untouched. Distinct decorations or logarithmic lifts can give the
same geometric representation; (10) does not separate them. An
arbitrary interpolation or contour endpoint has not thereby become
a regular critical representation. Finally the coefficient of the
geometric contribution in the original quantum period is not
determined by its critical value.

Thus (10) is a stronger geometric input to the connected-short-source
problem. It is not a proof of its noncancellation or of the
finite-exception theorem.

## 5. A gap for every other boundary-parabolic representation

A supplied positive complete ideal triangulation lets us remove the
unspecified neighborhood from (10), for boundary-parabolic
representations. Here boundary-parabolic means that each peripheral
group is conjugate into the group of parabolic translations, with
the identity included.

**Corollary 3.** Suppose \(M\) is supplied with an actual positive
complete ideal triangulation, with its primitive cusp curves.
There is a \(\delta_M>0\) such that every boundary-parabolic
representation not conjugate to the oriented complete holonomy obeys
\[
                     \operatorname{Vol}(\rho)\le V-\delta_M.
 \tag{11}
\]
For representations conjugate to neither orientation of complete
holonomy, there is an analogous bound
\(|\operatorname{Vol}(\rho)|\le V-\delta_M'\).

**Proof.** At each complete cusp choose one primitive meridian.
Its holonomy is noncentral parabolic. The same is true for a
sufficiently nearby boundary-parabolic representation: it cannot
be the identity near that fixed nonidentity matrix. Its unique
fixed ideal point varies continuously. For example, choose local
matrix lifts with repeated eigenvalue one; their rank-one
nilpotent parts have continuously varying kernels.
Since the entire peripheral image commutes with this meridian,
that kernel is its common fixed flag.

These flags develop every vertex of the given triangulation
equivariantly. All tetrahedral vertex differences and face
determinants are nonzero at completeness, and remain so nearby.
Their cross ratios therefore lie in the positive gluing chart.
The converse development and normalization by three ideal
vertices are the rational inverse constructions proved in
[the marked multicusp rigidity theorem](general_marked_multicusp_gluing_rigidity.md),
Sections 2--3.

In that chart the logarithms of the selected meridian multipliers
are local coordinates. Boundary-parabolic representations fix all
of them to zero on the centered branches. The invertible marked
Jacobian therefore gives the single complete solution, modulo
conjugation. Thus an open neighborhood \(\mathcal V\) of \(\iota\)
contains no other boundary-parabolic conjugacy class. Its conjugacy
saturation \(\mathcal U\) is open and has the same property.
Corollary 2 applied to \(\mathcal U\) proves (11).
Apply the same argument to the opposite orientation for the
absolute bound. \(\square\)

The hypothesis is a geometric certificate, not an assertion that an
arbitrary ideal triangulation is positive. The
[geometric-triangulation audit](ge_geometric_triangulation_audit.md)
explains how the audited affine-subdivision argument supplies such
a certificate under its stated Epstein--Penner input. No new
quantum identity is inferred from choosing that triangulation.

For the original critical configurations in Section 4, (11) gives a
strict uniform comparison with every other boundary-parabolic
holonomy, whenever this geometric certificate is supplied. All
decorations and logarithmic lifts of the complete holonomy remain
in one exceptional class. The inequality does not say which of
them the original quantum period contains, or how their
contributions combine.

## 6. A uniform competitor gap on the real boundary

The same argument gives a neighborhood statement for the original
critical actions without varying an integer filling coefficient.
It is important here to keep the free angles real.

**Corollary 4.** Fix one original integer partial filling
\(M=Y(\mathbf p)\) which is hyperbolic, and supply a positive
complete ideal triangulation of \(M\) with its original primitive
cusp curves. Suppose the original source has a regular marked
geometric critical germ \(\xi_{\rm geo}(\mathbf u)\), based at the
oriented complete holonomy of \(M\). Its free circle periods are
\(V_b=2iu_b\); choose that primitive curve as the coordinate on
each free cusp. All other remaining cusps have their prescribed
primitive coordinate equal to zero. These choices must account
for every cusp of \(M\). Let \(\mathcal S_{\rm geo}(\mathbf u)\)
be the original, absolutely normalized action of that germ.

Compare it with regular continued original critical configurations
\(\xi\) having the following same data:

* the fixed integer powers \(n_v=\eta_v-2p_v\), with integer
  filling charges and the full original face and logarithmic marking;
* the same free periods \(e^{V_b}=e^{2iu_b}\), and complete
  prescribed primitive periods on the other remaining cusps;
* nonunit selected longitude multipliers, as in (47) of the
  [signed action-volume proof](research_positive_edge_volume_identity.md),
  so that its original representation descends to this fixed \(M\).

There are \(r>0\) and \(\epsilon>0\), depending on this fixed
filling and chart, such that, for real
\(\mathbf u\in(-r,r)^b\),
\[
 \rho_\xi\not\sim\rho_{\rm geo}(\mathbf u)
 \quad\Longrightarrow\quad
 \Re\mathcal S(\xi)
       \le\Re\mathcal S_{\rm geo}(\mathbf u)-\epsilon.
 \tag{12}
\]
Here \(\sim\) denotes conjugacy of the underlying representations.
All decorations and logarithmic lifts of
\(\rho_{\rm geo}(\mathbf u)\) are grouped into the exceptional
class. The comparison set need not be finite or bounded in shape
coordinates.

*Proof.* First choose a sufficiently small representation
neighborhood \(\mathcal V\) of the complete holonomy. At each
cusp fix a primitive group element whose complete image is a
nonidentity parabolic. A nearby image remains nonidentity. Every
fixed flag of these nearby matrices lies near the complete
parabolic flag, after shrinking \(\mathcal V\). Indeed a contrary
sequence of flags would have a convergent subsequence in
\(\mathbb{CP}^1\); its limit would be a different fixed point of
the nonidentity parabolic. This is impossible. This argument
includes both flags when the nearby element is semisimple.

Consequently every retained peripheral decoration of a
representation in \(\mathcal V\) develops the supplied ideal
triangulation in its positive chart. The original chosen primitive
curve on each cusp is a valid local coordinate by Section 2 of
the marked multicusp rigidity theorem: the argument there allows
any one primitive curve per cusp, not just a fixed meridian.
Take the centered logarithms of their multipliers. For small
\(\mathbf u\), the specified logarithms are exactly \(2iu_b\)
and zero. Local uniqueness of that marked gluing solution shows
that a representation in \(\mathcal V\) with these data is
conjugate to \(\rho_{\rm geo}(\mathbf u)\). Wild source shape
coordinates or additional logarithmic windings do not change
this conclusion about the underlying representation.

Let \(\mathcal U\) be the conjugacy saturation of a smaller such
neighborhood. Corollary 2 supplies a fixed \(\delta>0\) for
representations outside \(\mathcal U\). The peripheral groups
in the comparison satisfy its hypotheses. Their original
meridian and longitude commute and have a retained common flag.
If one is semisimple, this makes them fix both endpoints
individually; otherwise the group is parabolic or trivial.

The signed edge identity (42) in the action-volume proof holds
with nonzero free angles as well. Summing it and eliminating the
selected periods by their critical equations gives the signed
version of its equation (24):
\[
 \operatorname{Vol}(\rho_\xi)
   =2\pi\Re\mathcal S(\xi)
       -2\sum_b\Im u_b
                    \sum_{e\ni b}\Im r_{b,e}.
 \tag{13}
\]
Every original edge and carrier is retained. The chain and axis
filling argument in Section 9 of that proof is unchanged: the
filled slopes are still the same integers, and the unfilled
peripheral types are those already allowed by the representation
volume construction. A retained free carrier contributes only
a purely imaginary quadratic to the action on this real boundary.
For real \(\mathbf u\), the last term in (13) is zero, without
requiring a bound on the other peripheral logarithms. Thus any
competing representation outside the geometric class obeys
\[
                 2\pi\Re\mathcal S(\xi)\le V-\delta.
 \tag{14}
\]
Finally \(2\pi\Re\mathcal S_{\rm geo}(0)=V\). Continuity of
the given geometric germ allows us to choose \(r\) so that
\(2\pi\Re\mathcal S_{\rm geo}(\mathbf u)>V-\delta/2\).
Equations (14) and this inequality prove (12) with
\(\epsilon=\delta/(4\pi)\). \(\square\)

This corollary compares actual regular critical values on a whole
real boundary neighborhood. It does not identify the geometric
coefficient in the finite quantum period. In particular the exact
[primitive cap minor](research_quantum_cap_primitive_source.md)
retains a boundary-selected Green problem; the volume gap does
not decide which of its modes occurs. Nor does (12) follow for
complex free angles by the same argument: the last term in (13)
then need not be small uniformly over other logarithmic lifts.
Finally none of these conclusions applies this fixed-manifold
rigidity theorem to a homotopy through nonintegral filling slopes.
