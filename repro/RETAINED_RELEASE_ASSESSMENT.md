# The retained results and their current proof sources

The current collection consists of 21 subject manuscripts, totaling
403 pages. The reference has 203 pages and covers overlapping material
and several different volume families. Separate papers repeat their
conventions and bibliography, so their aggregate length measures neither
compression nor proof strength.

All manuscripts are from this project. The Conway volume application
is 17 pages. Its five directly cited supporting papers, together with
the general marked-filling paper used by geometry, give a seven-paper
reading route of 149 pages. The reference is not an additional input
to that route.

The [paper guide](../papers/README.md) identifies each result and its
imports. The [collection record](results/paper-collection/summary.json)
checks all current sources against their PDFs, verifies the compiled
labels used by the dependency graph, and records the Conway route.
The graph checks references and logical organization; it does not
prove the mathematical assertions at its vertices.

The collection refresh removed eight superseded editions. Their six
still-needed finite check implementations were moved into the current
Newton, Casimir and circle-tree papers. Current checkers and illustrations
no longer depend on the removed folders. Historical tracked versions
remain in Git history, rather than in duplicate proof directories.

The analytic and geometric arguments retain their written proofs.
The [current Lean map](../formal/coverage.json) identifies the exact
finite, variational and complex-rate implications checked by the kernel.
The [manuscript audit](PROOF_PATH_CLEANUP_2026-11-25.md) explains those
interfaces and the whole-remainder assembly. It does not assert an
end-to-end Lean theorem about the knot invariant or a geometric manifold.

The [finite collection replay](results/paper-collection/finite/summary.json)
checks the exact identities, rational constants and certificate inputs
specified by each program. These finite checks do not replace contour
estimates, noncancellation or metric completion proofs.

The sufficient hypotheses of the restricted volume theorems are
unchanged. Natural density one concerns twist assignments to a fixed
construction. The extension across arbitrary short partial fillings,
and hence the proposed finite-exception theorem, remains open.
