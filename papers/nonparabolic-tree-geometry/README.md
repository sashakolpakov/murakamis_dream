# Nonparabolic holonomy of trees of crossing circles

This classical paper constructs the actual marked representation of an
ordered tree of crossing circles with a variable main meridian. It proves
the complete face and character maps, ordered page sewing, the physical
Hurwitz collar, and the locally unramified primitive filled germ.
There is no quantum asymptotic or global preferred-longitude theorem here.

## Statements and proof locations

- **Theorem 1.1, ng:representation**: the original augmented group,
  selected main \(M^{-1}\) flag and primitive auxiliary logarithms
  \(U_v=\sum\log\rho_{v,e}-\epsilon_v\log Q_v\), \(V_v=2\log Q_v\).
  Sections 2–4 construct the full maps and actual gluing.
- **Theorem 3.1, ng:character**: the explicit four-puncture chart,
  rational two-generator intertwinings and its native marked conjugacy.
  Equations (3.15), (3.23) and (3.31) give the transport identities,
  local commutator and native conjugacies.
- **Proposition 6.1, ng:positive-germ**: any original positive
  retained ideal triangulation with torus ends has a local decorated
  germ coordinated by one primitive similarity log at each torus.
  The ends may be incomplete. The proof includes the real row rank,
  positive polarization and shape/representation inverse, also for
  local Artin algebras with exact peripheral characters.
- **Theorem 1.2, ng:filled-germ**: at an actual positive smooth
  filled endpoint with distinct auxiliary longitude eigenvalues,
  the continued primitive slope equations are exactly the filled-group
  relations. With one unfilled main cusp, \(\log M\) is a local coordinate.
- **Corollary 7.1, ng:branch-identification**: a separately constructed
  branch with the same original representation, flags and logarithmic
  slopes is this same marked geometric germ.

The tree criterion is the published geometric condition
\(\sqrt{d_v^2+n_v^2}\ge630\), or its heterogeneous refinement.
It does not require a lower bound on each twist alone. The actual
main strand pairing must have one component for the knot statement.
At a parabolic auxiliary longitude, an exponentiated slope equation
alone does not kill the word. Intermediate cone charges are not
asserted to factor through the smooth filled group.

## Exact companion inputs

- **Positive octahedra and primitive fillings for trees of crossing
  circles**: Proposition 2.1 for the original inverse cut and ordered
  pages; Lemma 3.1 for the positive eight-tetrahedron chart; Theorems
  1.1 and 7.1 for the actual primitive smooth filling anchor.
  Section 5 of this paper matches all local coordinates and maps along
  that angular path, not just at the complete point.
- **Marked geometry of strict Conway compositions**: Section 5,
  equations (5.1)–(5.2), only for the physically signed original
  half-twist meridian. Its global strict theorem is not an input.
- **Circle patterns and primitive fillings of augmented links**:
  Section 7.1, equations (7.1)–(7.2), for actual normal-path rows and
  their intersection pairing. The real edge-rank and positive-Jacobian
  argument are written here. No quantum source theorem or preferred
  longitude is imported.

The general germ proposition is applied on the **original positive
augmented triangulation**. It does not require positivity of an added
flat subdivision or a positive triangulation of the filled manifold.

## Build and bounded exact checks

From this folder:

    latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build main.tex

From the repository root with SymPy installed:

    python -I papers/nonparabolic-tree-geometry/check.py --output /tmp/nonparabolic-tree.json

The checker reuses the three explicitly pinned exact matrix scripts
audit_all_circle_nonparabolic_edge.py,
audit_all_circle_four_punctured_adapter.py, and
audit_all_circle_hurwitz_line_transport.py. It adds independent angular
chart, edge-row and polarization identities and negative controls.
All subprocess outputs are private temporary records. A stale requested
summary is removed before checking, optimized Python is rejected, and
the success record is written only if all pinned inputs are unchanged.

These are rational identities, not sampling evidence for topology,
positive development, metric completion or analytic uniformity.
