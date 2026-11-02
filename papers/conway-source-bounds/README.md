# Complementary color bounds for Conway tangle sources

The paper proves two bounds for a fixed Conway construction whose cylindrical closure joins two completed boxes:

- the sum of every sector containing at least one complementary color term has a strict exponential gap below the positive complete-color action;
- the whole physical source has a strict gap when one auxiliary color differs from complete color by at least a fixed positive fraction of the level.

The bounds include all sufficiently large integer levels, all physical auxiliary colors and all retained half-twist signs. The exact finite Newton algebra and the strict complete stationary point are numbered imports from *Newton coefficients and positive sources for Conway tangles*. This paper proves the signed recurrence estimate, the two certified composition inequalities and the whole-tree propagation. It asserts no filled-invariant or volume asymptotic.

Build locally:

    cd papers/conway-source-bounds
    latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build main.tex

From the repository root, replay the two rational supporting-plane certificates:

    python3 papers/conway-source-bounds/check.py --output /tmp/conway-source-check

Python's standard library is sufficient. The output directory contains detailed two-leaf and attachment interval records, their subprocess logs and summary.json. The summary is removed before verification and written only after both certificates and the elementary rational leaf margin have been checked, with unchanged source/data hashes. These finite computations verify the stated continuum comparisons through the written concavity and enclosure proofs; they do not substitute level samples for the recurrence or tree arguments.
