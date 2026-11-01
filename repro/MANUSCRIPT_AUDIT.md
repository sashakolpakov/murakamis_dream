# The manuscript's proof dependencies

The present review checks how the manuscript passes from its finite
invariant to its volume conclusions. It has found omitted
justifications and a missing degree hypothesis, and has replaced one
indirect geometric dependency by a direct proof. The changes are
described below. No counterexample to
a stated volume theorem was found in this review. This is not an
end-to-end formal verification of the manuscript.

The review began with commit `c5d9c851c672b941bdbbec51da50d8f1a5c2cf12`.
The detailed reading records refer to that snapshot unless they expressly
name a later one. The directed-tree and all-orders reviews began at
`cfc8a9295dca45562634f6021415d0d80dc5f745`. The current TeX includes the corrections. Source
hashes in the records distinguish the versions actually read.

## The five requirements of a volume proof

Fix the diagram, endpoint order, primitive peripheral curves, retained
half twists, and filling integers before letting the level increase.
Each full-invariant theorem needs the following five statements.

1. **The finite formula is the intended invariant.** Its marked tensor
   contraction, coefficient targets, crossing powers and scalar
   normalization must agree exactly with the original definition.
2. **The selected contribution is nonzero.** If it is written
   \(G_N=a_Ne^{N\mathcal A}\), one needs
   \(N^{-1}\log|a_N|\to0\). A formal critical point alone is insufficient.
3. **The whole remainder is smaller.** For
   \(E_N=Z_N-G_N\), prove an upper exponential rate strictly below
   \(\operatorname{Re}\mathcal A\), including all other colors, Fourier
   charges, endpoints and contour joins.
4. **The peripheral solution gives the specified manifold.** The
   selected logarithms must produce a smooth solid torus along the
   original primitive slope. The main knot cusp stays complete.
5. **The action is its absolute volume.** The regulator's oriented
   fundamental chain and the completed metric must have the same volume,
   with their boundary correction and normalization retained.

The new proposition “Transfer from a contribution to the invariant” in
the [reproduction chapter](../manuscript/sections/09-reproduction.tex)
states the final analytic implication and proves it with the reverse
triangle inequality. It treats the geometric equality as a separate
input. The decomposition and bounds must hold through all sufficiently
large integer levels if the conclusion is to include both parities.

## Where the hypotheses come from

| Result | Full remainder estimate | Nonzero contribution and actual volume | Restriction that remains part of the theorem |
| --- | --- | --- | --- |
| Recursive Conway construction | Chapter 5 and the certificates of Appendix C; Chapter 8 controls the remaining Fourier charges and contours | Chapters 6–8 and Appendix D | The stated completed-box grammar, knot component test, and independently long fixed signed twists |
| Quantitative, local and directed circle trees | Their own finite-sum or subtree estimates in Appendices E, G and K | The corresponding saddle analysis and marked geometric arguments in F and G | The summed, local or directed criterion of the particular theorem |
| Planar terminal decoration | Appendix L's common-weight estimates after the specified finite insertion | Appendix L with the general central-contribution argument in O | All original and added twist powers sufficiently long; the insertion can change the knot |
| Unchanged diagrams under weak balance | Appendix P's common perturbation of face weights and Appendix N's exact filling norm | Appendix O | The actual complete packing passes weak balance or P's quantified alternative |
| A general unchanged matched sphere | No general estimate is supplied | Appendix O gives the specified geometric contribution | The full-invariant volume conclusion is not asserted |

The rows have different hypotheses. In particular, the last row is not
a premise left open inside the restricted-family proofs. Conversely,
the result about one contribution in that row does not imply a theorem
for its full invariant.

There is a potential source of confusion in the references between
Appendices L and O. O imports L's initial complete packing construction
and exact finite Morse source. It does not import L's final
full-invariant volume conclusion. The dependency must be read at the
level of these statements, rather than treating an entire appendix as
one indivisible theorem.

## Corrections made during this review

**The regulator and the filled metric.** Appendix D previously moved
directly from the completed metric to its volume identity. It now
compares the same finite boundary triangulation with an equivariant map
into each peripheral axis. The displayed homotopy has boundary volume
\(O(Y^{-2})\) at height \(Y\). Extending that boundary assignment through
the solid torus adds only axis-valued tetrahedra, whose volumes vanish.
The argument uses the primitive metric completion already proved in D
and explicitly cites the existing filling-chain comparison.

The same omitted comparison was found in Appendix F. Its proof now uses
the original positive tetrahedra, the actual logarithmic link periods,
and the same finite boundary triangulation to equate representation
volume with metric volume. For an intermediate cone angle it compares
the metric off its axis; smooth solid-torus completion is asserted only
at the endpoint. This argument applies to F's vertexwise construction,
including its permitted high-degree, small-power cases. It does not
silently impose D's different small-global-log hypothesis.

**The geometric meridian germ.** Appendix I previously invoked a
local-rigidity result whose existence input was a positive triangulation
of the filled manifold. The replacement proof uses the already
constructed positive augmented triangulation at its incomplete filling
endpoint. The main meridian and original primitive filling slopes give
an invertible shape Jacobian by the real symplectic row identities and
positivity. The shape/representation inverse is explicit, and the
distinct auxiliary longitude eigenvalues turn the slope multiplier
conditions into the projective filled-group relations. This gives the
required one-dimensional decorated germ modulo conjugation. The
determinant-one longitude sign is still fixed by the separate Seifert
frame calculation. This replacement removes that triangulation-existence
dependency for the retained-positive family, without making a claim
about its other uses in the research library.

**The complex strip in the Fourier estimate.** Appendix B previously
explained persistence of the real Fourier gap by a bound on the physical
Fourier support. Such a statement needs care because the real gap uses
cancellation. The revised proof inserts the complex parameter directly
into the same cotangent contour. On every side of the contour the extra
factor is at most
\(\exp(2\pi(\delta N+1/2)|v|)\). Choosing a fixed small strip preserves
the existing gap. Spectator Fourier variables stay real throughout
this step. The local contour argument also now fixes its outer box
before the smaller charge-ratio neighborhood and the reciprocal-slope
bound. Connector errors have an absolute exponential bound; they need
only lie below the first-charge action. Relative corrections to that
first saddle remain in its amplitude, rather than being mislabeled as
an exponentially smaller remainder.

**The degree hypothesis for the tensor norm.** The standalone joint-grid
bound in [the finite filling note](../notes/actual_uniform_filling_supremum_bound.md)
now explicitly requires degree at most \(N-1\) in each spectral variable.
Appendix N already included that hypothesis. Grid vanishing alone would
not give the stated derivative bound for polynomials of arbitrary degree.

**Formal coefficients and the recurrence.** Appendix M's regrading
argument now gives the coefficient recovery formula explicitly. For a
formal series \(B(h,u)=\sum B_{a,b}h^au^b\), substitution \(u=hs\)
recovers \(B_{a,b}\) as \([h^{a+b}s^b]B(h,hs)\). Applied to the
denominator-cleared operator identity, this explains why the microscopic
expansion determines a whole formal longitude germ. It does not extend
a bounded-\(s\) analytic estimate to \(s\) growing with the level.

## What has been checked formally

The [Lean project](../formal/README.md) checks finite degree partitions at both parities,
polynomial divided differences, the algebra retaining the double-root
derivative, the finite tensor subtraction, and scalar comparisons of
entropy gains, quadratic costs and filling-action losses. It now also
constructs division by a split monic polynomial, proves the remainder's
degree bound, and identifies its top coefficient with an iterated divided
difference. These are coefficientwise identities over a commutative ring;
the list of nodes may contain repetitions. The constructed remainder and
functional are now also proved linear, unchanged by arbitrary zero
padding, and unchanged on adding an actual monic multiple. The
[runner](check_proof_logic.py) builds the library and then separately
inspects every theorem's axioms. The
[recorded result](results/proof-logic/summary.json) includes the source
hashes and logical dependencies.

These proofs quantify over the parameters in their statements. They do
not prove that a given knot diagram supplies those parameters with the
required properties. The divided-difference identity, for example, is
an algebraic identity for a polynomial; connecting it to the literal
crossing matrix is a further theorem. Similarly, the scalar strict-gain
lemma assumes the entropy and Hessian bounds supplied by Appendix P.

## Scope of the mathematical review

The detailed records are organized by the implication being checked:

| Reading record | Scope |
| --- | --- |
| [Finite filling functional](manuscript_audit/finite-filling.md) | Repeated roots, signed crossing jets, scalar and tensor norms, and the original face targets |
| [Signed source and local approximation](manuscript_audit/source-packet.md) | Chapters 5–6, the global recurrence bound, certificate dependencies, and the nonzero local amplitude |
| [Filling analysis](manuscript_audit/filling-analysis.md) | Chapter 8, the complete Fourier period, charge comparison, contour joins, and noncancellation |
| [Recursive geometry](manuscript_audit/recursive-geometry.md) | Chapters 4 and 7, Appendix D, primitive filling, and the added fundamental-chain comparison |
| [Geometry used by weak balance](manuscript_audit/weak-balance-geometry.md) | The precise geometric inputs and implications from O to P |
| [Meaning of the formal declarations](manuscript_audit/formal-semantics.md) | Whether the Lean statements express the finite mathematical steps claimed for them |
| [Reduction at repeated roots](manuscript_audit/monic-remainder.md) | Constructive coefficientwise division, its top-coefficient functional, and the double-root remainder; the actual spectral data remain separate |
| [Directed circle trees](manuscript_audit/directed-tree.md) | K's main criterion, the complete conditional remainder, the degree-or-twist implication, and the F/G metric-volume interface |
| [All orders and recurrence factors](manuscript_audit/directed-all-orders.md) | Exact interpolation identities, the degree filtration, formal regrading and gauge, and the independent finite-sum existence proof |
| [The geometric branch and longitude](manuscript_audit/directed-geometry.md) | I/M's marked reconstruction, preferred longitude and cusp conventions; the new local rigidity proof on the retained augmented triangulation |

The detailed records cover the finite functional in Appendix N, the
geometric interface from O to P, the recursive source estimates in
Chapters 5–6, the marked geometry in Chapters 4 and 7 with Appendix D,
and the filling analysis in Chapter 8 with its contour estimates.
They identify the imported lemmas rather than treating their names or
finite checks as proofs.

The review has not reverified every certificate or every result in the
333-page starting manuscript. K's main proof and M's all-orders implication
now have separate reading records, with their imported results named.
This does not constitute a new complete review of H–J, K's separate
star example, every quantitative extension, or the original quantum
tangle compiler. The numerical checks of finitely many levels do not
establish uniform analytic claims. Those claims retain their written
proofs and hypotheses.

The two geometry records have portable symbolic checks, requiring SymPy:

```sh
python3 -I repro/manuscript_audit/check_recursive_geometry.py --output repro/results/recursive-geometry-current.json
python3 -I repro/manuscript_audit/check_weak_balance_geometry.py --output repro/results/weak-balance-geometry-current.json
```

These check the displayed algebra, source hashes, reference resolution,
and the recorded finite dependency graphs. Acyclicity of a graph does not
prove the claims at its vertices. The fundamental-chain arguments and
metric completeness remain written proofs even when their local formulas
pass the symbolic checks.

The general monic-remainder calculation is a step toward the finite
Hermite functional. Its application still needs the Chebyshev root data,
the original crossing jets, and the scalar norm. In particular, a list
of roots supplied to the algebraic theorem is not a proof that the
actual spectral polynomial has those roots with those multiplicities.
The diagram adapter then needs to be proved for the literal marked
tensors. Real and complex analysis, and the construction of the completed
hyperbolic metric, are further stages; the present Lean files do not
encompass them.
