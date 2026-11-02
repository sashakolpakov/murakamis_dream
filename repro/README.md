# Reproducing the calculations


The manuscript proves inequalities on continuous regions of state variables. Some of those inequalities are reduced, by concavity and supporting tangent planes, to a finite set of rational comparisons. This directory provides the scripts and reference records for those comparisons. The quantitative circle-tree theorem also has a group of symbolic, geometric and finite numerical checks, described below.

## Run the checks

The [manuscript audit](MANUSCRIPT_AUDIT.md) follows the implications from
the exact invariant to the volume identity, records the corrections
found in this review, and identifies the arguments still outside formal
verification. The [Lean project](../formal/README.md) checks finite
support, polynomial and tensor identities, and conditional implications
from whole-source estimates to a volume limit. Run it with
the pinned Lean toolchain installed:

```sh
python3 repro/check_proof_logic.py --output repro/results/proof-logic
```

This command does not replace the certificate checks below or formally
prove an analytic or geometric theorem in the manuscript.

The optional [Mathlib package](../formal-real/README.md) verifies the
elementary real and complex analysis used by the final implication:
actual norms and logarithms, a nonzero asymptotic contribution, and the
strict-gap argument for the ordinary volume limit. With its pinned
dependencies installed, run:

```sh
python3 repro/check_concrete_limits.py --output repro/results/concrete-limits
```

The exact state formula, its leading asymptotic, the whole-remainder
estimate and the geometric volume equality are explicit inputs. The
package also assembles distinct nonzero limits on finitely many residue
classes, including even and odd levels, when their action limits have
the same real part. Every rate uses the original level as denominator.
It also proves the finite weighted-graph energy and Laplacian identities,
including the constant kernel and strict positivity after fixing one
vertex. Identifying that matrix with the geometric Hessian remains a
written argument. The real-calculus module also derives the quadratic
action cost from actual second derivatives, the supporting-tangent
entropy gain, and the resulting two-branch strict sector estimate.
The triangle-potential module below now proves the local entropy derivative;
its substitution into the geometric application is stated separately.
The transport module starts with an actual positive table of corner
loads. If its supported incidence graph is connected, grounding one
vertex gives a strictly positive recession in every nonzero direction.
Compactness then supplies a uniform norm bound, compact sublevel sets
and an attained minimum. The geometric Hall inequalities constructing
that table remain written proofs. For fixed positive boundary values,
the application combines the boundary destinations into the grounded
vertex and retains their prescribed logarithms as row constants.
The strict-convexity module identifies the second derivative on an actual
segment with connected weighted graph energy. It derives strict
convexity, and hence uniqueness of that same potential's minimum. The
positive-table construction and geometric incidence remain written inputs;
the actual supported triangle derivatives are now supplied by the later
potential module. The reduced-Laplacian module identifies the actual free
matrix with that energy, constructs its inverse, and proves uniqueness
of every grounded linear solution. It does not prove a quantitative
inverse estimate or a nonlinear deformation theorem. The triangle-load module now differentiates the actual exponential,
square-root and arctangent expressions and identifies their shared-vertex
pairing with that edge energy. It includes one-zero triangles. The
triangle-potential module starts with the actual Lobachevsky integral and
supported supremum, proves attainment by those loads, and derives the
first and second derivatives. Its mixed assembly includes singleton rows
and retains shared variables and demands. The triangle-minimum module
then proves the actual potential's vertex lower bound and multivariate
continuity, aggregates a positive half-mass corner table, and converts
its row paths to positive conductance paths. These facts give a unique
global minimum after one coordinate is fixed. Repeated corner destinations
retain their separate coefficients; the prescribed demands need agree
with the table only at free vertices. Geometric Hall feasibility,
incidence, row connectivity and support-changing limits remain written
application inputs. Together the optional modules contain forty-eight definitions and
189 theorems, all 237 declarations included in the axiom audit; 24 negative
controls check invalid inputs.
The optional command is separate from the Std-only
check above; it requires
Mathlib and its substantially larger compiled library.

The separate [research papers](../papers/README.md) include bounded
checks of their finite algebra and rational constants. Run them together:

~~~sh
python3 repro/check_paper_algebra.py --output repro/results/paper-algebra
~~~

The runner requires SymPy, python-flint, NumPy and mpmath. It saves each program's
output and stops on a failed check. Its twenty groups cover polynomial
resolvents and path partitions, positive-matrix identities and parity
anchors, filling-sum normalization, symbolic peripheral coordinates,
rational three-braid constants, the complete forty-branch planar
certificate, its forty-five-branch extension at ordinary boundaries,
physical Newton matrices at eight levels, the exact terminal fan
recurrence, symbolic tree-block and peripheral identities, moving-meridian
physical matrices, complete Conway face maps and endpoint pairings,
the two complementary-color certificates, and the classical Conway
filling's symbolic peripheral and volume identities. The quarter-index
group compares the literal finite factorial source with its recurrence
and terminal walls, and checks two-channel transport identities. The
directed-tree group verifies its rational budgets, endpoint pairings and
finite quotient-versus-normal trace calculations. The strict-profile group
checks exact supports, turn-and-product identities and rational harmonic
responses. The strict-geometry group checks boundary labels, original
endpoint pairings and peripheral identities. The consolidated source
group also checks its full Fourier formula and derivative terms, including
examples whose values vanish at every spectral node while their normals
do not.
The two planar certificate groups use outward interval arithmetic with explicit
Fourier tails. Their reports keep the finite assertions separate from
the written all-length arguments.
The [planar and insertion review](PLANAR_INSERTION_AUDIT.md) records
which written arguments were examined and which results they import.
The [tangle and tree review](TANGLE_TREE_AUDIT.md) records the new papers'
proof boundaries and the transport module's formal coverage.
The subsequent [Conway geometry and meridian review](CONWAY_MERIDIAN_AUDIT.md)
records the two additional papers, their proof corrections, and the
formal derivation of strict convexity and uniqueness.
The [source and filling review](CONWAY_SOURCE_FILLING_AUDIT.md) records
the uniform complementary-color proof, classical deformation proof,
corrected Jacobian and formal reduced-Laplacian inverse.

The [strict Conway review](STRICT_CONWAY_AUDIT.md) records the larger
variational and geometric arguments, the consolidated whole-source proof,
the pure-source filling route and the formal minimum of the actual
triangle potential.

The programs use either a JSON output file or an output directory, as
registered in the single runner.
The planar, triangular-insertion, terminal-decoration, moving-meridian and
complementary-color programs accept an output directory
containing their summary and supporting records. The unified runner
handles both conventions. These commands do not establish uniform
large-level estimates, packing existence or metric completeness.

The statement-level dependency map for the retained volume families has a separate
standard-library command:

```sh
python3 repro/check_manuscript_logic.py --output repro/results/manuscript-logic
```

It checks the declared premise roles, retained assumptions, level scope,
references and absence of cycles. Fourteen deliberately invalid maps must
be rejected. The unrestricted matched-sphere route retains its open
remainder requirement. This is a check of the dependency record, not a
formal proof of the mathematical claims it records.

The exact verifiers require Python 3.10 or later and only its standard library. From the repository root, run:

```sh
python3 repro/verify.py --list
python3 repro/verify.py --plan
python3 repro/verify.py --output repro/results
```

The first command lists the checks. The second prints the execution plan without running them. The third executes the checks serially, writes fresh result records to `repro/results`, and compares them with the committed exact reference records. It does not overwrite those references. Without `--output`, the runner uses temporary results and removes them when it finishes.

Each verifier runs in Python's isolated mode. This prevents environment options from silently disabling the assertions on which the check depends. A successful run means that every required comparison and reference-record comparison passed; a failure should be investigated rather than accepted as a new reference result.

## What is being verified

A *leaf* is one basic two-strand twist piece in the manuscript's tangle construction. A *block* joins such pieces. The finite invariant has signed terms outside its selected central contribution; the proof calls those terms *aliases*. The certificates show that their upper bounds are strictly smaller than the relevant central value, throughout the specified parameter regions.

| Check | Mathematical role and finite work |
| --- | --- |
| Two-leaf block | Controls the two possible alias types in a two-piece block, using 16 slope intervals and 288 exact corner/vertex comparisons. |
| Single-leaf attachment | Controls an additional piece attached to a constructed box, using 55 dyadic rectangles and 880 exact comparisons over the full two-parameter slope square. |
| Single-leaf endpoint | Checks four exact vertex comparisons used with the monotone-response argument at the endpoint. |
| Elementary endpoints | Checks rational lower bounds used for the large-cotangent leaf estimate and the isolated three-piece closure. |

Here a *slope* is a derivative of an entropy function used in the source estimate. It is not a Dehn-filling slope. The interval engine bounds sine, logarithm, pi and the integrated log-sine function by rational series with explicit remainder estimates. It does not infer a continuum inequality from samples or call a numerical optimizer to certify a maximum.

The written proof explains why concavity and affine parameter dependence reduce the continuum statement to these finite comparisons. The [proof-input map](PROOF_INPUTS.md) identifies those arguments and the exact records used by the runner.

## A cap estimate uniform over its real spectrum

The research notes give a strict bound for one signed contribution in the
recorded 54-region diagram. The selected cap parameter may vary throughout
\([-2,2]\); all other spectral parameters remain \(-2\), and the exterior
factorization used in the proof requires odd levels. Run its certificates
with one command:

```sh
python3 repro/check_cap_response.py --output repro/results/cap-response
```

This checks the original triangulated sphere and marking, localizes the
positive exterior stationary point, bounds its first two responses, and
compares two explicit pressure values with a complete feasible-flow
entropy. The three numerical comparisons use outward rational intervals,
not an optimizer. The response report is recomputed before it is passed to
the tilted-pressure verifier. The same command checks the finite
alternating-section inequalities on rational examples.

With SymPy installed, append `--algebra` to check the original spectral
products and their matrix divided differences in exact cyclotomic fields.
These finite checks complement the [uniform cap proof](../notes/research_cap_uniform_spectral_gap.md)
and its [stationary-point argument](../notes/research_cap_common_axis_bound.md).
They do not replace the all-level analytic estimates or the geometric
volume theorem. Neither the even-level exterior nor the full filled-knot
remainder is covered by this certificate.

## Uniform bounds for inserting twists

The local matrix-to-polynomial adapter has its own short check:

~~~sh
python3 repro/check_local_face_fourier.py
~~~

It constructs the physical Casimir from its coproduct and the face
operator separately, then compares them in exact finite fields at
levels 2 through 12. It also checks the homogeneous kernel for a
polynomial of degree larger than the level and detects the incorrect
even-level replacement of an integer displacement by its residue.
The script uses only the Python standard library. These are finite
checks of signs and normalization; Appendix N proves the identity
for every complex root level.

With SymPy and NumPy installed, run:

~~~sh
python3 repro/run_research_checks.py filling-supremum
~~~

The program checks the finite derivative interpolation formula in
cyclotomic fields, the repeated and simple Chebyshev residues, and the
reconstruction of positive and negative powers of the original crossing
matrices. It also checks the lower-block numerator derivatives against
the corresponding spectral projectors. The [proof](../notes/actual_uniform_filling_supremum_bound.md)
establishes the norm bounds for every level. The finite checks do not
estimate a volume limit.

## Balanced terminal decorations

~~~sh
python3 repro/run_research_checks.py balanced-terminal-fans
~~~

This standard-library group checks exact polynomial recurrences, rational
balance constants, oriented stellar subdivisions, the matching and face
parity, and the actual endpoint pairing of even terminal stacks. Results
are saved in the [result file](../experiments/actual_balanced_terminal_fans_results.json)
and runner logs. The all-real choice of fan counts, the uniform source
estimates, and hyperbolic completion are analytic proofs in the
[theorem](../notes/actual_balanced_terminal_fan_volume.md); the checks do
not replace those proofs or extrapolate from sampled quantum invariants.

## The quantitative circle-tree theorem

Run its three programs with one command:

```sh
python3 repro/run_research_checks.py curvature-fillings
```

This group requires Python, SymPy and mpmath. It checks four edge-action
identities and 990 finite complex Gaussian samples; 46 rational
octahedral identities and seven bounds; and 128 ordered trees with
448 local attachments and 28 additional algebraic identities. The
programs retain both half-twist signs and the original peripheral
curves. Results record the exact source hashes.

The [proof-input map](PROOF_INPUTS.md#the-quantitative-circle-tree-theorem)
locates the uniform estimates, arbitrary-tree induction and geometric
completion. The finite tree examples check the attachment code against
the original strand compiler; the induction proves the general case.
The numerical Gaussian samples check formulas, while the written
bounds control the whole complex domain.

## Reproducing the local tree argument

This group requires Python and mpmath. Run it using one command:

~~~sh
python3 repro/run_research_checks.py local-tree-fillings
~~~

The first two programs check 21 analytic and eight geometric
constant comparisons by exact rational arithmetic. The third
compares the polynomial subtree recursion with a separate
spectral or first-derivative trace calculation in 48 finite cases,
using 180 choices of root at 80-digit precision. The examples
include both level parities, zero and signed powers, moving
parameters, and constant channels with repeated spectral roots.
All $N$ edge indices are retained; removing the high indices
changes every tested value.

These checks verify the constants and finite identities used by
the argument. The written proof supplies the induction for all
finite trees, the contour bounds, noncancellation, and the metric
completion. The scripts do not test the asymptotic conclusion
by extrapolating finite levels.

## Checking the geometric longitude formulas

With Python and SymPy installed, run the four exact-algebra programs
through one command:

~~~sh
python3 repro/run_research_checks.py geometric-characteristic
~~~

The programs check the nonparabolic face maps and peripheral words,
the four-puncture character matrices, the two eigenline choices in a
half twist, and the differential and discriminant identities used by
the rigidity argument. They compare rational functions symbolically,
rather than sampling hyperbolic knots. The written proof establishes
the ordered gluing, boundary pairing, constant field and regularity
over every nonzero main meridian value. Those global arguments are
not replaced by the script results.

## What a passing run does not replace

The suite verifies the finite arithmetic in the source bounds. It does not mechanically verify the whole manuscript. In particular, the invariant normalization, the ordered tangle identities, the geometric gluing, the complex interpolation estimates and the filling-period argument require their written proofs. A passing result should not be reported as a computer proof of the volume conjecture for arbitrary knots.

## Build the paper and documentation

The [manuscript source guide](../manuscript/README.md) gives the paper and figure build commands. Documentation builds are separate from the proof checks and do not launch this suite.

The paper and figure builds require TeX Live or MacTeX with `latexmk`, `pdflatex`, TikZ and `standalone`, plus Ghostscript (`gs`) for PNG previews. The guide requires Pandoc. Its builder uses Python's standard library and produces native MathML, with no separate documentation framework.

Then, from the repository root:

```sh
python3 tools/build_manuscript.py
python3 tools/build_book.py
python3 tools/check_book.py
```

The certificate runner itself still requires only Python's standard library. Keeping rendering and verification separate makes a failed build distinguishable from a failed mathematical certificate.

## A limit of the shared-weight envelope method

```sh
python3 repro/run_research_checks.py singleton-envelope
```

This standard-library group checks the fifty-four-region example in the
[fixed-sector obstruction](../notes/actual_singleton_sector_envelope_obstruction.md).
One program replays the oriented sphere moves and verifies the rational
face loads and entropy bounds. The other checks the sphere links,
matching, marked edge, and knot-producing strand parity. The written
argument also proves that the selected sector has nonzero shared
coefficient support at all sufficiently large even levels.

The conclusion is that one proposed upper-bound method cannot prove a
strict volume gap for this fixed source. It is not a lower bound for
the quantum invariant and is not a counterexample to the volume conjecture.

For the extension to the actual absolute sum of shared-array terms, run:

```sh
python3 repro/run_research_checks.py source-cancellation
```

This includes the preceding rational and topology certificates, then
checks the protected endpoint formula, the odd central cofactor product,
and exact integer load rounding at both parities. The new check uses only
the standard library. Its result is saved in
`repro/results/absolute-source-obstruction.json`. The
[proof](../notes/research_absolute_source_cancellation_obstruction.md)
supplies the all-level entropy lower bound and explains why no choice of
positive diagonal Cauchy weights removes the excess. Cancellation in the
signed shared sum remains a different quantity.

## Protected triangular sums

With `python-flint` installed, run:

```sh
python3 repro/check_protected_sums.py --output repro/results/protected-sums
```

This replays both rational interval certificates for the seventeen-region
input and checks eight exact tetrahedral attachments. Each resulting
complex has connected cyclic vertex links, is a connected closed surface
of Euler characteristic two, has the specified triangle matching, and
retains the protected nonmatching edge and every ordinary target. The
regions at which weak balance must fail remain unchanged. Use
`--attachments` to change the finite number checked. Appendix Q proves
the general closure theorem and its volume implication; these finite
checks do not certify its analytic or geometric inputs.

## Ordinary triangular insertion

The explicit construction in Appendix R has a separate finite runner:

```sh
python3 repro/check_triangular_boundary_certificate.py --output repro/results/triangular-boundary
```

It requires `python-flint` and NumPy. The command checks the original
seventeen-region source and its rational corner loads, the forty old
branches and five new overload bounds, and the restricted dual inequality
that retains a failure of weak balance. It also constructs the oriented
cores and their insertions at lengths 2, 4, 8 and 16, checking the exact
matching and coefficient targets. The reference calculation is stored
in `repro/triangular-boundary-insertion/`; a fresh run writes separately
to `repro/results/triangular-boundary/`.

The rate certificate is evaluated at the boundary ratios for length
`2**20`. It does not construct that many regions: the proof gives their
curvatures and uniform inequalities explicitly. Monotonicity then extends
the same witnesses to every larger even length. The all-length topology,
conditional disk minimum, nonzero asymptotic, knot-component condition
and identification with the completed metric remain written proofs.
See the [audit of this argument](manuscript_audit/triangular-boundary.md)
for the scope of the Lean and finite checks.
