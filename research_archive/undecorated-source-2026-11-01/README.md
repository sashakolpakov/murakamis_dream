# The source estimate for diagrams without added tangles

The published result from this continuation is a finite bound for inserting
twist powers. It does not add a knot family to the volume theorems.
The remaining calculations are preserved here because they give a concrete
way to study the shared source and rule out several tempting shortcuts.

## Published finite estimate

The proof is in
[the synchronized note](../../notes/actual_uniform_filling_supremum_bound.md)
and Appendix N of the manuscript. For a polynomial of degree at most
\(N-1\), the original full filling functional satisfies
\[
 |\mathcal L_N^nH|\le(1+|n|/2)\|H\|_{[-2,2]}.
\]
If its values vanish at all spectral nodes, the factor improves to
\((N-1)/N\), independently of the twist power. Its derivatives at double
roots are retained. For several crossing regions the same bounds apply
after taking the original shared face coefficient. The full complementary
polynomial also has a product-grid cancellation, without splitting it
into separate path terms.

The proof derives the finite midpoint formula and the trigonometric
derivative bound directly. The reproduction script checks the finite
algebraic identities, including the original positive and negative crossing
matrices. The all-level inequality is a written proof, not an extrapolation
from those checks.

For fixed twists, this functional contributes no exponential cost.
The desired further estimate is a strict gap for the shared complementary
source below the complete augmented action. A separately established
nonzero crossing contribution and its geometric interpretation are also
needed. Bounding the full twist-independent source at the augmented
volume alone does not give the smaller volume after filling.

## The cyclic source and its signs

The private notes
[cyclic transfer](private/md-undecorated-bipyramid-exact-cyclic-transfer.md)
and [grade blocks](private/md-undecorated-bipyramid-signed-grade-blocks.md)
treat an even bipyramidal white sphere with opposite-offset matchings.
The actual marked source is a trace of matrices indexed by two pending
face degrees. The index sum is preserved at north rows and lowered by the
south-face degree at south rows. One marked row raises it by \(N-1\).
Thus a closed path has total lowering exactly \(N-1\); the common
south-face coefficient is retained.

The north blocks are polynomial functions of a bidiagonal Casimir followed
by reversal. The south blocks are coefficients of the full polynomial
matrix with a south-face variable. One full-grade conjugate pairing is a
positive Gram matrix. That identity does not cover arbitrary adjacent
rows: the actual cycle must contain positive total degree loss, and its
spectral variables are independent.

A separate two-row specialization has an exact alternating telescope.
Its signed coefficient is polynomially bounded on the whole real spectral
interval even where the sum of absolute summands grows exponentially.
The [derivation](private/md-undecorated-cancellation-two-row-telescope-audit.md)
and exact checks retain both endpoints. Its specified boundary degrees
cannot be dropped when sewing a full cycle.

## What the obstruction calculations establish

The [packing calculation](private/md-undecorated-geometry-all-marks-bipyramid-obstruction.md)
gives an arbitrary-size family for which every permitted choice of mark
fails the particular local complete-radius balance test. Its native
figure records the actual inversion and curvatures. This limits that
sufficient test; it is not a counterexample to a quantum volume limit.

The [fractional-flow calculation](private/md-undecorated-fractional-flow-network-and-lift-obstruction.md)
shows why an integral comparison-flow polytope does not force a concave
entropy maximum to occur at an integral point. Its local boundary-load
obstruction must not be reported as a counterexample for the full closed
diagram.

The [terminal-tangle calculation](private/md-undecorated-geometry-terminal-fan-cancellation-obstruction.md)
uses the twofold branched cover to show that the specified turned factors
with opposite long powers do not cancel as a tangle with fixed endpoints.
It distinguishes an endpoint pairing from a tangle isotopy. It makes no
claim that every possible external closure distinguishes the tangles.

The longer [half-charge reduction](private/md-undecorated-cancellation-half-charge-reduction.md)
retains the actual primitive peripheral logarithms. A half-integer Fourier
label alone does not identify a different filling representation.

## Next proof step

For the unchanged cyclic diagram, define
\[
 D_N=S_{N,\mathrm{full}}-S_{N,\mathrm{CROSS}}.
\]
The proposed sufficient estimate is
\[
 \sup_{\boldsymbol\sigma\in[-2,2]^m}|D_N(\boldsymbol\sigma)|
 \le \exp\!\left[
 N\left(\frac{\operatorname{Vol}(Y)}{2\pi}-\eta_m+o(1)\right)\right],
 \qquad \eta_m>0.
\]
Here \(Y\) is the original augmented exterior and the diagram is fixed
before \(N\). This inequality has not been proved. Before deducing a new
volume theorem, the nonzero crossing asymptotic and its metric
identification must also be checked for the literal diagram, with all
source and topological hypotheses preserved.

The public commit is
09cd63c5c5c1b1c8ce8805a7536e0f33e56a9d19.
The manifest records the saved files and their hashes. Earlier versions
are retained where a working file changed.
