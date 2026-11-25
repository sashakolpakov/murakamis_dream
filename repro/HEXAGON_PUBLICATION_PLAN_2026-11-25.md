# The Conway series for Hexagon

The proposed deposit is a series of seven papers, led by **Holomorphic
source asymptotics and volume limits for strict Conway compositions**.
Its theorem fixes an ordered strict tangle construction and a half-twist
pattern producing one knot. All signed auxiliary filling integers are
independently sufficiently long and remain fixed as the level grows
through all integers. The result concerns the complete knot-complement
volume. Density one refers to twist assignments for the fixed recipe;
the finite-exception extension is still open.

The lead paper is 19 pages. Its five direct companion references and one
further geometric prerequisite contain the supporting proofs. Together
they have 160 pages. The 205-page reference overlaps this material and
includes other families; it is not an eighth prerequisite or the intended
first deposit.

## The papers to deposit together

The order below respects their mathematical dependencies. A background
citation discussing a later application does not create a proof dependency.

| Paper | Pages | Role |
| --- | ---: | --- |
| [Finite spectral evaluation and uniform filling bounds](../papers/filling-bounds/README.md) | 28 | The finite invariant, repeated-root crossing data, diagram contraction and normalization. |
| [Newton calculus and stationary profiles](../papers/newton-calculus/README.md) | 28 | Exact tangle algebra, strict support, stationary maximum and boundary profiles. Uses finite spectral evaluation. |
| [Spectral estimates for Conway tangle sources](../papers/conway-source-bounds/README.md) | 30 | Bounds on the full colored evaluation, omitted coefficients and macroscopic color deficits. Uses the two algebra papers. |
| [Circle patterns and primitive fillings](../papers/marked-fillings/README.md) | 20 | General near-complete metric completion and the absolute volume comparison. |
| [Marked geometry of strict Conway compositions](../papers/strict-conway-geometry/README.md) | 23 | The specified augmented exterior and its primitive long fillings. Uses Newton profiles and the general geometric completion. |
| [Oscillatory filling sums](../papers/oscillatory-fillings/README.md) | 12 | A nonzero asymptotic for the whole filling sum under explicit source hypotheses. Uses the finite Hermite functional. |
| [Holomorphic source asymptotics and volume limits](../papers/conway-asymptotics/README.md) | 19 | Verifies those hypotheses for the strict Conway construction and compares the surviving action with its geometric volume. |

The [series file](../papers/conway-series.json) fixes the exact collection,
its dependency order and the Git edition used by its bibliographies.
These are papers from one project, not independent external confirmations
of each other's conclusions.

## What was checked before packaging

The [exposition audit](CONWAY_SERIES_AUDIT_2026-11-25.md) records the
substantive changes. Every paper was read and revised for definitions,
notation, proof transitions and the scope of imported statements.
Corrections include the exposed-leaf/zero-color notation collision and
wording that confused a derivative datum with its logarithmic derivative.
The revision removes a duplicated variational induction, explains the
Fourier normalization and coherent error array, and adds geometric
illustrations and worked examples. Theorem and equation numbering is
preserved across the seven papers.

The finite checks exercise the algebra and certificates specified in
their programs. The [verification record](results/manuscript-and-lean/verification-summary.json)
separates those checks, typesetting and kernel compilation from written
analytic and geometric proofs. The current
[Lean coverage map](../formal/coverage.json) states exactly which finite
identities and theorem-assembly implications are formalized. It does not
claim a fully formal proof about the knot invariant or its manifold.

## Source packages and submission

The offline packaging tool builds each TeX source archive by an explicit
allowlist of files actually read by TeX, including required figures. It
then compiles the extracted archive in a temporary directory outside the
repository. Its report records the archive contents, source hashes,
page counts and metadata drafts. This checks that a deposit can be read
and built independently of the working directory; it does not certify
mathematical correctness.

The configured author, ORCID, license and provenance declarations are
retained. Credentials and local parameter files are excluded from every
archive. Code and Lean formalizations remain in the repository and are
linked separately: [Hexagon's deposit instructions](https://hexagonmath.org/about)
accept TeX sources and external formalization links. Hexagon provides
moderation, [not peer review](https://hexagonmath.org/who).

No remote draft or submission has been made. Preparing and validating
this collection is separate from depositing its permanent public versions.
