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

The current source-asymptotics proof defines its finite action directly
from the exact cofactor polynomial. The earlier fold interpolation
remains in the reference account and guide as an alternative construction;
the direct proof does not require both routes. This is one concrete way
the dependency analysis shortens the presentation without removing a
needed argument.

Three other distinctions determine the division. The classical filling
construction does not need a nonzero quantum asymptotic; their comparison
comes later, through the same marked critical equations. A nonzero
geometric contribution does not bound the rest of the invariant. Finally,
weak balance, protected triangular gluing, ordinary triangular insertion
and the three-braid comparison provide different sufficient estimates
for that remainder. Protected gluing does not require weak balance, and
ordinary insertion does not require the protected-gluing theorem.

## The current drafts

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

**Uniform spectral bounds for local Casimir sources.**
[TeX source](local-coefficients/main.tex) ·
[PDF](../docs/papers/local-coefficients.pdf)

This paper proves the estimates needed before applying Cauchy's coefficient
formula to a collection of tangles. It defines the local polynomial by an
explicit banded matrix and partitions its paths into three degree regions.
Theorem 1.1 bounds all three regions over the entire real spectral interval
and for arbitrary phases of the face variables. The proof includes the
signed recurrence, both unused spectral products, the endpoint optimization,
both level parities and face variables fixed exactly at zero. It imports
the finite operator identification from the preceding paper. It does not
assume a geometric saddle or a volume identity.

**Oscillatory filling sums with independently long twists.**
[TeX source](oscillatory-fillings/main.tex) ·
[PDF](../docs/papers/oscillatory-fillings.pdf)

This paper addresses cancellation in the complete Fourier filling sum.
Theorem 1.1 assumes a nonzero holomorphic expansion near the complete point
and a strict bound for the shared source away from it. It then proves a
nonzero asymptotic for the entire sum, including every nonzero integer
Fourier charge and the original endpoints. The twist integers are fixed,
independently signed and sufficiently large; their ratios are unrestricted.
The proof estimates the infinite tail before localizing the remaining
finitely many integrals. An elementary polynomial example verifies both
hypotheses explicitly. For a knot source, construction of those hypotheses
and identification of the critical action with volume remain separate
theorems.

**Holomorphic asymptotics of central shared face coefficients.**
[TeX source](source-asymptotics/main.tex) ·
[PDF](../docs/papers/source-asymptotics.pdf)

Theorem 1.1 supplies the two source estimates used by the filling-sum
paper. Given positive stationary face weights, it proves a nonzero
holomorphic Gaussian expansion for the actual central coefficient and
a strict spectral bound away from its complete point. The proof treats
the entire shared face torus, including the regions outside the Gaussian
neighborhood. It retains both level parities, the original coefficient
targets and the odd skipped-row term. A tetrahedral example illustrates
why repeated face labels denote one variable and why the Gaussian measure
has no extra integer-lattice factor. Section 7 states the exact normalized
input to the oscillatory theorem. Bounding the other degree sectors of
the invariant remains the task of an application theorem.

**Circle patterns and primitive fillings of augmented links.**
[TeX source](marked-fillings/main.tex) ·
[PDF](../docs/papers/marked-fillings.pdf)

This is the classical geometric foundation. Starting from the marked
matched sphere, the paper constructs its complete augmented exterior
and one common deformed circle pattern. It calculates the peripheral
paths through each original crossing disk, including retained half
twists. The critical equations then specify a primitive filling slope.
The proof constructs the smooth complete metric and compares its volume
with the absolute critical action using the same fundamental chain.
Theorem 1.1 holds for independently sufficiently long signed fillings;
it does not assume a quantum asymptotic. Two drawings explain the single
disk pairing and the logarithmic torus periods. The final corollary
states the exact action comparison used by the quantum applications.

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
dependencies are substantial. The finite input and local upper bounds are
proved in the first two papers above. The filling-sum paper proves the
analytic implication once its local expansion and global gap are supplied.
The source-asymptotics paper constructs that expansion and gap. The
circle-pattern paper supplies the marked geometric volume comparison.
The application now cites numbered statements in these companion papers,
and checks their common normalization and hypotheses.

## What still needs its own paper

The division should follow results rather than cut the reference text
into equal lengths. The following groups have different mathematical
purposes:

| Subject | Result to explain and prove | Dependencies that must remain visible |
| --- | --- | --- |
| Sufficient conditions on planar compositions | Weak balance, decoration and joining operations control the full remainder | The source, analytic and geometric results above |
| Ordered tangle trees | Explicit degree and twist conditions give the volume limit | The recursive finite evaluation and its geometric construction |
| Geometric longitude and recurrences | All-order meridian expansions force the selected geometric factor to divide a classical symbol | The full expansion, its normalization and the geometric longitude |

These remaining subjects still need their own complete accounts. Each
candidate needs a precise theorem, complete proofs of its own claims,
defined notation, and an explicit list of imported theorems.

For a citation between papers, the exporting paper must state a numbered
theorem with its normalization, degree restrictions, level parity and
uniformity assumptions. The importing paper must name that theorem and
check those hypotheses. A reference to a folder of calculations is not
a substitute. The six drafts above separate one application and its
foundations. The other retained knot families and the longitude results
still require the remaining editorial and proof review. The dependency
graph keeps those obligations visible.

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

Replay the papers' finite identities and the three-braid rational constants
with one command, using Python and SymPy:

```sh
python3 repro/check_paper_algebra.py --output repro/results/paper-algebra
```

The runner saves a separate record and log for each check, and stops on
failure. The constant verifier uses outward rational bounds with explicit
series remainders. The argument for every even number of factors is
written in the paper; it is not inferred from computations for finitely
many braid lengths. The finite checks complement the written proofs of
the analytic estimates and geometric constructions.

The local-bound and filling-sum checks can also be run separately:

~~~sh
python3 papers/local-coefficients/check.py --output repro/results/local-coefficients.json
python3 papers/oscillatory-fillings/check.py --output repro/results/oscillatory-fillings.json
~~~

These require SymPy. They check finite polynomial identities and algebraic
normalizations, with their exact scope recorded in the output. They do not
replace the written uniform estimates, contour arguments or asymptotic
proofs.
