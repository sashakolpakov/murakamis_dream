# Finite quantum invariants and hyperbolic volume

The manuscripts are organized by the mathematical results they establish
and the results they use. The dependency graph records those relations
before assigning paper boundaries. A finite spectral theorem should be
citable independently of an asymptotic theorem; a geometric filling
construction should state precisely the information needed to compare
its volume with a quantum action.

The 374-page reference account contains 93 pages of main text, 266 pages
of appendices, and 15 pages of front matter and references. The appendices
collect several subjects: finite quantum algebra, geometric constructions,
asymptotic estimates, sufficient conditions for different knot families,
and meridian and longitude results. Those subjects accumulated in one
file; the length does not show that one theorem requires 374 pages.
The account remains available while this division is prepared. The working
limit of 30 pages per paper is an editorial constraint, not the principle
for grouping results.

[Explore the dependency graph](../docs/papers/dependencies.html).
Each statement lists the results it uses, the reason for each use, and
the exact place where the statement or proof can be found. Arrows run
from prerequisites to their consumers. The overview groups related
results; the detailed view retains the individual statements.

The components are finer than the eventual papers. They are not a proposal
for one paper per box. For example, finite spectral algebra and exact
diagram evaluation now form one article, with the global contraction
and normalization calculations included. The graph keeps them as
separate components because the abstract norm theorem does not use
that contraction argument.

Three other distinctions determine the division. The classical filling
construction does not need a nonzero quantum asymptotic; their comparison
comes later, through the same marked critical equations. A nonzero
geometric contribution does not bound the rest of the invariant. Finally,
weak balance, protected triangular gluing, ordinary triangular insertion
and the three-braid comparison provide different sufficient estimates
for that remainder. Protected gluing does not require weak balance, and
ordinary insertion does not require the protected-gluing theorem.

## The first two drafts

**Finite spectral evaluation and uniform filling bounds.**
[TeX source](filling-bounds/main.tex) ·
[PDF](../docs/papers/filling-bounds.pdf)

This paper asks how a fixed twisting operation acts on a polynomial of
degree less than the root-of-unity level. It defines the functional at
simple and repeated spectral roots, proves its norm bound, and explains
why the canonical polynomial representative matters. It then proves the
exact coefficient formula for a marked planar diagram constructed from a
matched triangulated sphere. The proof includes the face variables, the
integer support, the shifted grids at even levels, the cups and caps,
and the single reduced cut. A finite Fourier and matrix calculation
compares the result with the reduced Kashaev invariant, including the
framing factor. These results supply the finite formulas used by later
papers. They do not estimate the large-level invariant or identify an
exponential rate with volume.

**Volume limits for long alternating-generator three-braids.**
[TeX source](three-braids/main.tex) ·
[PDF](../docs/papers/three-braids.pdf)

This application concerns the ordinary closure of

\[
 \sigma_2^{n_0}\sigma_1^{n_1}\cdots
 \sigma_2^{n_{m-2}}\sigma_1^{n_{m-1}},\qquad
 m\ge6\text{ even}.
\]

For each fixed number of factors, the signed powers are independently
sufficiently large in magnitude, and their permutation must give a knot.
The generators alternate; the crossing signs need not alternate.
The braid axis is not a component. The paper develops the diagram,
its circle packing and the estimates that control the entire remainder.
It imports three explicitly stated results: the exact source identity,
the uniform local coefficient estimates, and the nonzero geometric
filling contribution with its absolute volume calibration. Those
dependencies are substantial. The finite input is proved in the first
paper above. The analytic and geometric inputs still have their complete
accounts in the reference manuscript and its cited technical notes.

## What still needs its own paper

The division should follow results rather than cut the reference text
into equal lengths. The following groups have different mathematical
purposes:

| Subject | Result to explain and prove | Dependencies that must remain visible |
| --- | --- | --- |
| Uniform local asymptotics | Bounds over the full allowed coefficient range, and a nonzero complex local approximation | Exact local formulas; estimates at the endpoints as well as in the interior |
| The geometric filling contribution | A nonzero contribution survives the filling sum and has the volume rate of the same knot complement | Local asymptotics, primitive filling curves and an absolute volume comparison |
| Sufficient conditions on planar compositions | Weak balance, decoration and joining operations control the full remainder | The source, analytic and geometric results above |
| Ordered tangle trees | Explicit degree and twist conditions give the volume limit | The recursive finite evaluation and its geometric construction |
| Geometric longitude and recurrences | All-order meridian expansions force the selected geometric factor to divide a classical symbol | The full expansion, its normalization and the geometric longitude |

This is a proposed division, not a claim that five more finished papers
already exist. The geometric filling contribution may need separate
analytic and geometric papers. Its short reference chapter cites proofs
elsewhere; copying it would not make a self-contained paper. Each
candidate needs a precise theorem, complete proofs of its own claims,
defined notation, and an explicit list of imported theorems.

For a citation between papers, the exporting paper must state a numbered
theorem with its normalization, degree restrictions, level parity and
uniformity assumptions. The importing paper must name that theorem and
check those hypotheses. A reference to a folder of calculations is not
a substitute. At present the two drafts above are written; several of
their shared foundations still have their complete accounts in the
reference manuscript and technical notes. The dependency graph makes
that remaining editorial work visible.

The illustrated guide retains the broader approaches and unsuccessful
comparisons. The reference manuscript remains available for the existing
full account. Exploratory research is separate from this editing work.

## Building and reproducing the papers

With TeX Live or MacTeX, `latexmk`, Python and PyMuPDF installed, run from
the repository root:

```sh
python3 tools/build_papers.py
```

Use a directory name to build just one paper, for example
`python3 tools/build_papers.py filling-bounds`.
The command checks the page limit, unresolved references and overfull
boxes, then copies the PDFs and their source-hash records to `docs/papers/`.
Add `--no-publish` to keep the outputs in each paper's `build/` directory.
These are typesetting checks, not mathematical verification.

Rebuild the dependency graph with:

```sh
python3 tools/build_dependency_graph.py
```

Its source is `papers/dependencies.json`. The command verifies the named
source locations, checks both statement and component graphs for cycles,
and refuses a recorded completed result that imports an open result.
It generates the interactive graph, vector overview and source-hash
record in `docs/papers/`. These checks validate the declared dependency
record, not the proofs at its nodes.

The rational constants in the three-braid argument have a separate command:

```sh
python3 repro/check_cyclic_source_constants.py --output repro/results/cyclic-source-constants.json
```

It uses outward rational bounds with explicit series remainders. The
argument for every even number of factors is written in the paper; it is
not inferred from computations for finitely many braid lengths.
