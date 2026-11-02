# Volume limits from planar tangles

[Read the reference manuscript](build/main.pdf) ·
[Corrections to the reference](ERRATA.md) ·
[Current papers](../papers/README.md) ·
[Illustrated reading guide](../book/chapters/manuscript.md)

This is the frozen 374-page reference account. It contains 15 main
chapters (93 pages), eighteen appendices (266 pages), thirteen pages of
front matter and two pages of references. Several separate arguments
accumulated in one file, with repeated definitions and summaries followed
by full proofs. The page count is not the length of one proof of the
general volume conjecture.

The current subject drafts develop these arguments in smaller units and
include some broader results. There are 21 drafts, totaling 403 pages,
each between 11 and 29 pages. Their boundaries are provisional. The
[dependency graph](../docs/papers/dependencies.html) records which numbered
statements each argument uses, so a reader can follow one theorem without
reading the whole reference. Splitting has improved access; it has not
compressed the total collection. The reference's mathematical sources
and PDF stay frozen, and corrections are recorded in the errata.

## What the reference proves

The manuscript gives volume limits for specified constructions of knots.
It also contains partial results with narrower conclusions. The
[introduction](sections/01-introduction.tex) states the hypotheses. In
every volume theorem, the diagram and all twist powers are fixed before
the root-of-unity level tends to infinity. The strand connections must
give one knot, without an internally closed extra main component. The
volume is that of the original knot complement: only auxiliary crossing
circles are filled, and the main knot cusp remains complete.

One construction starts with a simple triangulated sphere whose triangles
are paired across selected edges. Terminal tangles are added until a
shared circle-packing inequality becomes strict. Independently
sufficiently long signed twists at every original and added crossing
circle then give the volume limit for the resulting knot. The decoration
can change the knot. For an unchanged matched sphere, a separate theorem
assumes an explicit weak balance condition on its complete packing;
that condition is not asserted for every diagram.

The ordered-tangle results have different hypotheses. The reference's
recursive construction admits independently long signed twists. For a
finite ordered tree with at least one edge and a crossing circle at each
vertex, let $d_v$ be the degree and $n_v$ the signed half-twist power.
The summed criterion is

$$
 \sum_v \frac{d_v}{d_v^2+n_v^2}\le 2^{-25}.
$$

A separate directed argument has the following sufficient condition at
every vertex:

$$
 d_v\ge 2^{28}\quad\text{or}\quad |n_v|\ge 2^{27}.
$$

The alternatives may differ from vertex to vertex. The degree alternative
allows fixed short or zero powers. The full directed condition assigns
separate bounds to the polynomials obtained from subtrees and is more
flexible than this consequence. The purely geometric threshold
$\sqrt{d_v^2+n_v^2}\ge630$ constructs a metric; it does not by itself prove
the quantum volume limit.

The meridian and longitude arguments give a conditional operator result.
If a specified fixed nonzero operator annihilates the whole reduced
meridian function at every sufficiently large level, the selected
geometric factor divides its first nonzero classical symbol. This
assumes the annihilator. It proves neither its existence nor equality
with the entire A-polynomial or recurrence ideal.

## Where the arguments are located

| Part of the reference | Mathematical role |
| --- | --- |
| Chapters 2–8 and Appendices A–D | Finite invariant, the first tangle construction, source bounds, oscillatory filling, marked geometry and rational certificates. |
| Chapters 9–11 and Appendices E–G, K | Summed and directed tree estimates, with their separate geometric thresholds and full finite-sum proofs. |
| Appendices H–J, M | Moving-meridian expansions, the geometric longitude, junction relations and the conditional classical-symbol conclusion. |
| The planar-decoration chapter and Appendix L | The packing decoration, its oriented source, full Fourier estimate and primitive filling. |
| Appendix N | A finite norm bound for inserting fixed twist powers. A volume application also requires a source estimate. |
| Appendix O | A nonzero geometric contribution for an unchanged matched sphere. Its general complementary signed contribution remains a separate problem. |
| Appendix P | A bound for that whole remainder under weak balance, including equality in the local inequalities and a quantified small-defect variant. |
| Appendix Q | Gluing certified pieces along protected triangles, retaining every locally allowed sector and the shared coefficient demands. |
| Appendix R | Insertion along an ordinary triangular face, with a fixed-boundary variational problem and sufficiently small positive boundary ratios. |

The current strict Conway proof is broader than the reference's original
completed-root construction. Its own variational, source and marked
geometry arguments are given in the [current papers](../papers/README.md).
The separate reduction paper treats net twists, zero sums and the
surviving closure before applying that theorem. Large written twist
numbers alone need not remain large after reduction.

## Proof dependencies and review

A full volume conclusion requires five pieces: the exact invariant
formula, a nonzero leading contribution, a bound for everything else,
the intended completed metric, and an absolute comparison of its volume
with the same action. A theorem about one geometric contribution cannot
supply the bound for the remainder. The restricted results have their
own estimates; they do not assume a general source theorem.

The [closing assessment](../repro/RETAINED_RELEASE_ASSESSMENT.md) records
the completed review of those retained implications. The
[proof-input map](../repro/PROOF_INPUTS.md) and
[detailed audit](../repro/MANUSCRIPT_AUDIT.md) locate the written inputs,
corrections and scope of each check. The named analytic and geometric
lemmas retain written proofs. The [Lean library](../formal/README.md)
and [Mathlib extension](../formal-real/README.md) prove finite algebra,
calculus and internal implications, with their application hypotheses
visible. They do not give an end-to-end formal proof for an actual knot.

The illustrated guide's [methods](../book/chapters/methods.md) and
[algebraic approaches](../book/chapters/algebraic.md) chapters preserve
exploratory ideas and unsuccessful comparisons. Those are separate from
the retained proof dependencies and from the frozen reference.

## Reproduce the reference and its checks

From the repository root, rebuild the archived sources with:

```sh
python3 tools/build_manuscript.py
```

This requires TeX Live or MacTeX with `latexmk` and the packages listed
in `main.tex`. It writes `manuscript/build/main.pdf`, figure previews and
a manifest of input and output hashes. Building the PDF checks
typesetting; it does not execute mathematical certificates or incorporate
the separate errata into the frozen text.

For the reference's rational supporting inequalities and their exact
domain coverage, run:

```sh
python3 repro/verify.py --output repro/results
```

For the current papers' full registered finite suite, run:

```sh
python3 repro/check_paper_algebra.py --output repro/results/paper-algebra
```

The [reproduction instructions](../repro/README.md) list dependencies,
individual check groups and the separate Lean commands. Finite checks
support the exact formulas and inequalities used; they do not prove
uniform analytic estimates by sampling levels.

To publish the illustrated guide locally:

```sh
python3 tools/build_book.py
python3 tools/check_book.py
```

Pandoc renders the formulas as MathML. The guide includes the reference
PDF and a rendered errata page. Former Sphinx addresses redirect to this
single maintained web exposition.
