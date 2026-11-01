# Bounded audit of the recursive geometric volume interface

This report concerns `manuscript/sections/04-geometry.tex`,
`07-marked-geometry.tex`, their full proof in
`D-marked-cell-calibration.tex`, and the new rate-transfer/dependency
section of `09-reproduction.tex` in the publication checkout. It records
the statements and dependencies actually examined. It is not a
certification of the whole manuscript or a new verification of the
finite inequality certificates.

The source hashes, a sixteen-node implication map, the exact algebra
checks and internal-reference resolution are in
`recursive-geometry-snapshot.json`. The accompanying script is
`check_recursive_geometry.py`.

## 1. Outcome and integrated correction

The bounded read found one missing explanation: before the final
filled-volume equation, Appendix D used the representation volume of
the augmented fundamental chain as the metric volume of the completed
filled manifold without explicitly recalling the boundary-chain
comparison. The comparison is proved in
`notes/general_source_regulator_hyperbolic_equality.md`, §6, and in the
two finite-chain sources cited there. It was not a missing geometric
completion hypothesis.

The manuscript now includes the explanation at D, lines 410–436. It
uses the same finite boundary triangulation, the explicit equivariant
homotopy

\[
H_s(w,Y)=\bigl(sa(w),
Y\exp((1-s)\eta(w)+s\log b(w))\bigr),
\qquad 0\le s\le1,
\]

and its \(O(Y^{-2})\) boundary volume. After replacing the old boundary
map by its axis-valued comparison, the same boundary assignment extends
through the solid torus with all new vertices on that axis. Every added
tetrahedron has zero volume. The unfilled main cusp retains the
parabolic convention. I read the integrated paragraph and found no
remaining mismatch with the cited construction.

No further necessary correction was found in the bounded geometric
interface or in the new rate-transfer section. The statements still
depend on the explicitly identified entropy, finite-source and
Fourier-period results; those are not replaced by this audit.

## 2. Exact class and quantifiers

The scope used by Chapters 04 and 07 is the grammar in Introduction,
Definition `def:grammar`:

\[
E::=hh\mid T(E)\mid E_1E_2\mid hE\mid Eh,
\qquad C(FG),\quad F,G\text{ both completed}.
\]

Every occurrence of \(h\) is an original elementary piece. Endpoint
orders, disk framings, the retained half-twist signs and the marked
main component are fixed. The half-twist pattern must give one main
knot with no internally closed main component. Section `sec:pairings`
provides a finite test and a choice-existence argument. Full twists
preserve that test.

The geometric construction first keeps all main components of the
augmented exterior. The knot conclusion uses the separate component
test. The final theorem fixes the expression and parity pattern, then
chooses every signed filling integer sufficiently large independently,
and only afterward takes the level to infinity. No ratio bound between
the filling integers enters the geometric neighborhood.

The older broad positive-Conway incidence note contains a flat annular
boundary case. It is not a counterexample to this statement: the
completed-root restriction and the strict stationary state are essential
here. In particular, neither an arbitrary positive tangle word nor an
arbitrary stationary sum of volume atoms is being identified with a
hyperbolic knot complement. The isolated closures and later quantitative
circle-tree or general strict-tree results have their own hypotheses;
they are not silently included in Chapters 04–07.

## 3. Complete metric: what was checked

The real stationary state is supplied by the preceding entropy and
response results. I checked how this input is used, rather than
reproving their full strictness induction. Strictness supplies positive
leaf and prism angles, actual maximal supported quadrilateral faces,
and nondegenerate local maps.

Chapter 04 gives explicit leaf and prism vertices. The local cell
volumes are \(\pi g(a)\) and \(\pi m(x,y,z)\). The derivative-to-face
identities are

\[
\varkappa(F_x)=e^{-m_x},\qquad
\varkappa(F_y)=e^{-m_y},\qquad
\varkappa(F_z)=e^{-m_z},\qquad
\varkappa(\text{leaf})=e^{-g'}.
\]

The ordered input maps invert this modulus, so stationarity is exactly
the required face-isometry relation. The order of all four vertices is
retained. Matching a single edge multiplier or merely the cell volumes
would not give this conclusion.

I read the following global steps in 04 and their supporting incidence
proofs in D and the cited Conway notes:

* Attach on opposite supported sides; the specified seam-angle sums
  imply local convexity. The finite-point shortest-path argument gives
  convexity of the finite union. Strict supported output faces exclude
  additional ideal intersections.
* The product consumes two disjoint pairs of exposed original
  endpoints, which never become exposed again. Turns only permute the
  four remaining endpoints. Final closure pairs endpoints from disjoint
  root boxes. Thus corner identifications do not grow into unrecorded
  chains or collapse the four corners of a leaf.
* The projection-sphere and half-crossing-disk cuts are cuts of the
  literal diagram in \(S^3\). Each auxiliary semicircle is
  boundary-parallel along its recorded half disk. Drilling and cutting
  returns each projection piece to a ball. The stack, turn and closing
  rules determine the same oriented colored boundary walks as the
  geometric construction. Their identification extends over the
  balls, so reversing the cuts recovers the original exterior with
  degree one.
* Pure and odd face-return words are identities of projective maps,
  including translation and dilation. The right-angled cusp rectangles
  admit the common shaded-side decoration. White and shaded pairings
  preserve it, so the actual compact cusp tori are complete.

The factor in the complete normalization is therefore

\[
\operatorname{Vol}(Y_E^\epsilon)=2\operatorname{Vol}(P_E)
=2\pi F_0.
\]

The first factor two is the two actual projection balls, not an
inference from an expected volume formula. The complete polyhedron
exists by the written construction; Rivin's variational work is cited
as context, not as an unverified existence premise here.

## 4. Selected source branch and marked representation

The local source germ is supplied by the finite recurrence/interpolation
and packet results. D does not choose it by matching a geometric Hessian.
It uses the selected local shear

\[
\chi=t-\frac{\epsilon v}{2\pi i},\qquad
f_\epsilon=g-\frac{\epsilon v^2}{4\pi i},\qquad
v=\partial_t g,
\]

with its constant fixed by the source normalization at the stated
endpoint. Its positive complete value is the already identified action.

D supplies the native white and shaded matrices, the full prism
compatibilities, the physical turn and closing maps, and all pure and
odd edge words. These relations apply to the original cut's group
presentation. A nearby framed representation of the same link group
therefore follows from full face/edge relations; it is not inferred from
matching boundary traces alone. The main-meridian maps have multiplier
one identically and are nonidentity at completeness. They remain
noncentral parabolic on a small neighborhood, and their commuting
partners remain parabolic.

I read the rational reduction for the nine prism identifications. The
private exact checker independently expands the three pure relations,
three odd relations, four physical-turn relations and four closing
relations at independent symbolic \(E,R\). It does not independently
expand all nine world-coordinate prism identities; that is an explicit
boundary of this computational check.

For the selected apex coordinates,

\[
\rho=\frac{Z}{1+E-Z}=e^{-2\pi it},\qquad
Q=\frac{E-Z}{Z-1}=e^{-v}.
\]

The actual disk longitude and meridian words give

\[
U=-2\pi i\chi,\qquad V=-2v=-2\partial_\chi\Phi_\epsilon.
\]

The two-rectangle cusp lattice and the typed signed threading fix the
primitive integral marking and which odd path belongs to which sign.
The half-longitude shear is a relation between those markings; it does
not assert that half a longitude is itself an integral peripheral loop.
The original physical power is \(\epsilon-2p\), not a reinterpreted
rational filling with a shifted meridian.

## 5. Regulator normalization and metric completion

The source primitive and regulator use similarity logs, twice the
corresponding eigenvalue logs:

\[
G=2\pi i\Phi_\epsilon,\qquad
dG=\frac12\sum V\,dU,\qquad
\operatorname{Vol}(\rho)
=\operatorname{Im}G-\frac12\sum\operatorname{Re}U\operatorname{Im}V.
\]

I checked the half-twist contribution to \(G\) is
\(-\epsilon V^2/8\), the peripheral differential has the stated factor
one half, and the absolute constant is fixed at the actual complete
metric. The written derivation retains the original oriented
fundamental chain. It uses its peripheral Bloch boundary
\(-2\mathcal M\wedge\mathcal L\); the relevant fundamental-chain
and regulator companion arguments were read. This audit does not
purport to formalize the general theory of representation volume.

The metric completion has more hypotheses than an exponentiated filling
equation. D supplies them explicitly:

1. The framed representation is close to the complete holonomy of the
   same manifold. A compact-core averaging construction and an
   equivariant affine cusp development give a positive local
   diffeomorphism on the core and entire ends.
2. At a filled cusp at least one multiplier differs from one. The
   common second fixed point \(q=b/(1-a)\) escapes every bounded
   developed generator path near completeness. The actual generator
   log increments tend to zero. Their possible \(2\pi i\) differences
   from the selected small logs therefore vanish before the large
   integer \(p\) is used.
3. The logarithmic development supplies a complete Euclidean metric on
   the compact torus. Its lifted development is the plane and its
   periods form a real rank-two lattice. The actual slope has period
   \(U+pV=-2\pi i\); the complementary primitive period \(V\) has
   nonzero real part. Thus there is a full punctured tube with a
   single angular turn, and adding its axis is a smooth solid torus.
4. The slope holonomy fixes both common fixed points and has multiplier
   one, so it is projectively the identity. This is where descent to
   the filled group is established; it is not asserted from multiplier
   one at a parabolic locus.
5. The main cusp is unfilled and has a complete translation link.
   The middle is compact. The resulting metric is complete and
   finite-volume on exactly the specified filled topology.

The step “some multiplier differs from one” does not itself assert
nonunit modulus. D only needs the former to define \(q\). The later
rank-two log lattice together with the pure imaginary primitive slope
forces \(\operatorname{Re}V\ne0\), which is the condition used for
the tube axis. This order is valid.

For the integrated filling-chain comparison, D has every premise of
the cited general lemma: an actual framed representation, a common
preserved axis at each filled cusp, the killed primitive slope and
solid-torus group descent, the same finite boundary triangulation as
the regulator, and the unchanged parabolic convention at each unfilled
cusp. The conical functions are bounded with bounded piecewise first
derivatives on a fundamental cross section, and their positive height
factor is bounded away from zero there. Hence the homotopy estimate
applies directly. No quantum asymptotic is used to calibrate volume.

## 6. Saddle, signs and independent long slopes

Writing \(r_\ell=1/p_\ell\), the geometric equations become
\(V_\ell+r_\ell U_\ell=-2\pi ir_\ell\). The packet gives at zero
the nondegenerate Jacobian
\(-4\pi i\operatorname{diag}(\tau_\ell)\), with
\(\operatorname{Im}\tau_\ell>0\). A fixed reciprocal-slope polydisk
therefore gives the selected small solution for independently long
positive or negative filling integers. Shrinking it once places all
these solutions in the fixed framed metric neighborhood.

The action is

\[
S_{\epsilon,\mathbf p}(\chi)=\Phi_\epsilon(\chi)
+\frac{\pi i}{2}\sum_\ell\frac{(\chi_\ell-1)^2}{p_\ell}.
\]

Its stationary equations give precisely the primitive equations above.
For one component, write \(\chi=a+ib\). At the stationary point,

\[
U=2\pi b-2\pi ia,\qquad
V=-\frac{2\pi b}{p}+\frac{2\pi i(a-1)}p.
\]

Consequently

\[
\frac12\operatorname{Re}U\operatorname{Im}V
=\frac{2\pi^2b(a-1)}p,
\qquad
2\pi\operatorname{Re}\frac{\pi i(\chi-1)^2}{2p}
=-\frac{2\pi^2b(a-1)}p.
\]

This is the exact boundary correction, including its sign and factor
two. Together with the completed metric and common-chain comparison it
gives

\[
2\pi\operatorname{Re}S_{\epsilon,\mathbf p}(\chi_*)
=\operatorname{Vol}(S^3\setminus K_{F,G,\epsilon}(\mathbf p)).
\]

The script checks this cancellation and the explicit change from the
upper-half-space metric to the tube metric. These algebraic checks
alone would not prove the existence of the original marked geometric
branch; the preceding construction is required.

## 7. Rate transfer and circularity

I read the new `09-reproduction.tex` proposition and its source maps.
For the exact decomposition
\(K_N=u_N(a_Ne^{N\mathcal A}+E_N)\), nonzero subexponential
\(u_N,a_N\), and a full remainder with rate strictly below
\(\operatorname{Re}\mathcal A\), its triangle-inequality proof gives
eventual nonvanishing and the claimed logarithmic limit. The geometric
identity is a separate final hypothesis. The proof neither assumes
that an isolated local saddle dominates nor treats a local Gaussian
as a bound on the whole period.

The recursive source, alias, local packet and full Fourier-charge
arguments are assigned to their corresponding chapters and appendices.
The geometry in 04/07/D does not depend on their final volume limit.
Conversely, the full invariant conclusion requires their nonzero
coefficient and entire-remainder estimates, not just the geometry.

The weak-balance dependency paragraph is also consistent with the
earlier bounded O/P audit: Appendix O uses Appendix L's complete
packing and exact finite Morse source, not L's full-invariant volume
conclusion. Appendix P supplies its separate complementary-source gap;
Appendix N transfers that gap through the finite filling functional.
Only then is the fixed long-filling threshold increased so the action
drop is smaller than the gap. This is an acyclic use of those results.

## 8. Limits of this audit

The record includes fifteen source hashes, twenty-one exact
matrix/normalization checks and a sixteen-node dependency graph. All
seventy-one reference occurrences in 04, 07, D and 09 resolve uniquely
in the actual manuscript input tree.

The following were treated as written proof inputs or were outside this
bounded review: the full entropy strictness induction, all finite
rational inequality certificates, the complete complex lattice
interpolation estimates, global alias bounds, and the entire
Fourier-charge domination proof. The nine world-coordinate prism
identities were read with their rational substitution instructions but
were not all independently expanded by the private checker. General
fundamental-chain and completeness arguments were read mathematically,
not machine-formalized. No public file was changed and no manuscript
or guide build was run by this audit.
