# Spectral estimates for Conway tangle sources

[Read the PDF](../../docs/papers/conway-source-bounds.pdf) · [TeX source](main.tex) · [Dependency graph](https://sashakolpakov.github.io/murakamis_dream/papers/dependencies.html)

Before full twists are inserted, a Conway tangle construction gives a finite polynomial expression. Colored circles provide its inputs, stacking multiplies them, a quarter turn acts by a linear involution, and a linear functional closes the expression. The paper bounds the resulting scalar uniformly in every circle color from 1 to the level N and in all retained half twists.

For each fixed strict construction, it proves three statements:

- The exponential upper rate is at most the maximum action of the positive sum with every circle colored N.
- If any circle color is at least δN below N, for a fixed δ > 0, the exponential rate is strictly smaller.
- The difference between the full expression and its explicitly defined core has a strictly smaller rate.

Strictness means that the normalized Newton indices admit labels satisfying the strict multiplication inequalities and the turn and closing relations. Section 1 gives these inequalities, an equivalent interval test, and a three-leaf example. The main theorem applies to all such constructions with at least three boxes. A separate corollary treats the strict two-leaf closure. All sufficiently large integer levels are included.

These are bounds before filling. The [asymptotic paper](../conway-asymptotics/README.md) uses them to exclude terms outside its leading contribution; it separately proves that contribution is nonzero and interprets its action geometrically.

The proof alternates two estimates. A circle factor gives an exact Fourier formula, in which the derivative data at repeated spectral roots cancel a potentially troublesome frequency. Between circle factors, a positive comparison keeps every shared multiplication index. Two supporting-plane inequalities propagate strict losses through that comparison. The supporting inequalities have rational interval certificates; the analytic and inductive arguments are written in full. The individual leaf recurrence in Section 3 is a separate result and is not needed for the main theorem.

Build from the repository root:

    .venv/bin/python tools/build_papers.py conway-source-bounds --no-publish

Replay the rational comparisons and finite-algebra examples:

    python3 papers/conway-source-bounds/check.py --output /tmp/conway-source-check

The check uses Python's standard library. It verifies the complete covers and rational margins for 288 inequalities on 16 slope intervals and 880 inequalities on 55 rectangles. It also checks polynomial and Fourier formulas at levels 2 through 18, including examples invisible to spectral values alone. The output identifies the sources and data used. The finite examples supplement the written all-level proofs.
