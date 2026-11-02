# Spectral estimates for Conway tangle sources

The paper proves whole-source and complementary-color bounds for every fixed strict Conway presentation with at least three elementary boxes. A separate corollary treats every strict two-leaf closure, with all retained signs and the original coefficient-square normalization. Strictness is the explicit interval-type test in Section 1. It includes the earlier completed/completed closure grammar, elementary closing leaves and the isolated three-leaf closure.

The main conclusions are uniform over all physical auxiliary colors, retained signs 0,+1,-1 and all sufficiently large integer levels:

- the full source has upper rate equal to the positive complete-action maximum;
- a macroscopic deficit in any original color gives a strict rate loss;
- the entire full-minus-core difference has a strict rate loss.

These are estimates before filling. No nonzero filled asymptotic or volume identity is asserted.

The paper retains the local signed recurrence estimates as Proposition 3.1 and the scalar supporting-plane inequalities as Lemmas 4.1 and 5.1. The new global proof uses the scalar inequalities, the exact Fourier functional, complete-node Hermite conditioning and the pure variational/profile results. It does not require the local signed recurrence or a quantum core packet. The complete-node conditioning and high first-normal estimates are proved directly here; there is no circle-tree-asymptotics import.

The older completed-root propagation is subsumed by the arbitrary-array component comparison in Section 8 and the strict-source induction in Section 9. The physical complementary-color identity is used only after the full physical-color bound has been proved. It is distinct from the low/high Newton-band comparison.

Build locally:

    cd papers/conway-source-bounds
    latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build main.tex

From the repository root, replay the exact comparisons and bounded finite algebra:

    python3 papers/conway-source-bounds/check.py --output /tmp/conway-source-check

Python's standard library is sufficient. The two rational certificate records verify 288 endpoint/vertex inequalities on 16 slope intervals and 880 inequalities on 55 covering rectangles, together with the elementary attachment margin. `fourier.json` checks exact polynomial/Laurent identities, phases, endpoint repair, value-invisible classes and negative controls at levels 2 through 18. These finite checks do not prove the uniform recurrence, strip or component estimates by sampling.

The wrapper removes a stale success summary before verification, rejects `-O`, runs isolated child processes and writes its summary only after the sources and data retain their initial hashes. The published physical operator identification remains an explicit finite-algebra import; the pure strict-profile theorem is a separate companion import.
