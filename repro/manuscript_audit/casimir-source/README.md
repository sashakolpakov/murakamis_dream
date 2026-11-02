# Local bounds and central-source proof audit

[Report](report.md) records a complete reading of the two original papers at commit acd7e7d5bff5641537f0b6dc71684711ac68dda0. The [source pins and locators](sources.json) refer to that historical snapshot, retained under [snapshot](snapshot/). These are the sources the review actually examined, not the current
paper layout. The two papers have since been combined as
[Spectral bounds and asymptotics of Casimir sources](../../../papers/casimir-source-asymptotics/README.md).
The [consolidation record](../../MANUSCRIPT_AUDIT.md#local-spectral-bounds-shared-asymptotics-and-finite-meridian-jets)
explains which conclusions and proofs were retained.

The mathematical audit found no defect under the printed hypotheses. The report distinguishes the stationary-radius assumption, imported finite and oscillatory results, central-source conclusion, and remaining noncentral/geometric work.

This is a historical proof-review record. The later
[whole-sum reading](../whole-charge/report.md) and
[closing assessment](../../RETAINED_RELEASE_ASSESSMENT.md) cover subsequent
steps in the retained arguments. They do not change the assumptions or
scope recorded here.

The bounded calculations can be repeated from this directory:

    python3 snapshot/papers/local-coefficients/check.py --output local-exact-check.json
    python3 snapshot/papers/source-asymptotics/check.py --output source-exact-check.json
    python3 counterchecks.py

The first two scripts require SymPy; the third also requires mpmath and SciPy. Exact finite examples check identities only at the listed levels. The quadrature and convergence diagnostics are not proofs of uniformity, zero exclusion, complement gaps, or a volume theorem.
