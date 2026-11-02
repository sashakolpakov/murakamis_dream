# Local bounds and central-source proof audit

[Report](report.md) records a complete reading of the two original papers at commit acd7e7d5bff5641537f0b6dc71684711ac68dda0. The [source pins and locators](sources.json) refer to that historical snapshot, retained under [snapshot](snapshot/). The subsequent paper consolidation has its own proof-diff review.

The mathematical audit found no defect under the printed hypotheses. The report distinguishes the stationary-radius assumption, imported finite and oscillatory results, central-source conclusion, and remaining noncentral/geometric work.

The bounded calculations can be repeated from this directory:

    python3 snapshot/papers/local-coefficients/check.py --output local-exact-check.json
    python3 snapshot/papers/source-asymptotics/check.py --output source-exact-check.json
    python3 counterchecks.py

The first two scripts require SymPy; the third also requires mpmath and SciPy. Exact finite examples check identities only at the listed levels. The quadrature and convergence diagnostics are not proofs of uniformity, zero exclusion, complement gaps, or a volume theorem.
