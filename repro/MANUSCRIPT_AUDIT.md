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

The [planar and insertion paper review](PLANAR_INSERTION_AUDIT.md)
records the later extraction of Appendices P--R, the corrected octahedral
boundary weights, and the precise scope of the written, interval and
Lean checks for those drafts. The reference manuscript stays frozen;
its appendix locators remain useful for the earlier review below.

## Separate accounts of the representation and longitude proofs

The classical arguments of Appendices I and J now have two companion
accounts: [Nonparabolic holonomy of trees of crossing circles](../papers/nonparabolic-tree-geometry/main.tex)
(22 pages) and [Preferred longitudes of Conway tree complements](../papers/preferred-longitudes/main.tex)
(29 pages). The first proves the original group reconstruction and the
positive filled meridian germ. The second proves the rational longitude
formula, its preferred framing and its extension across bare junctions.
The reference PDF and its mathematical sources remain unchanged.

The dependency graph assigns the representation and rigidity lemmas to
the first paper and the constant-field, regularity, cusp and sign
arguments to the second. It distinguishes the exact finite Fourier trace
from the later source estimate: only the finite trace is imported into
the bare-junction calculation. It likewise separates the tetrahedral
normal-flow identity from the later volume theorem. Neither classical
paper depends on a quantum asymptotic or an all-orders recurrence result.

The longitude extraction supplies an explicit interval-count induction
in the proof of angular elimination. If an interval convolution is
written as \(C=1_{[-r,r]}*H\), its adjacent difference is
\(C(k)-C(k+1)=H(k-r)-H(k+r+1)\). Choosing the largest radius
\(r\) and inducting on the remaining factors proves the strict
integer drop in the required tail. The resulting polynomial comparison
justifies the equality of exponential rates; a finite sample of
coefficients would not establish it. The proof also keeps the possible
half-label fold and uses the original positive triangulation for local
rigidity, rather than requiring the newly drilled subdivision to be
positive.

The registered finite suite now replays the local character, seam,
Hurwitz, cusp and framing identities from both papers. Its
[source record](results/paper-algebra/summary.json) pins the registered
TeX sources and checker inputs. The two PDF build records pin their
sources, page counts and stated companion imports. These computations
check algebra and typesetting; the topological reconstruction,
constant-field argument, local analytic inverse and surface-frame sign
remain written proofs. The existing Lean results cover specific algebraic
and analytic implications; they do not formally verify either new
geometric paper.

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
| Protected triangular sums | Appendix Q transports certificates covering every locally allowed noncentral string; N transfers the whole spectral bound | O applies to the new marked sphere | A fixed finite assembly of certified pieces, its own knot-component test and independently long fixed twists |
| Ordinary triangular insertion | Appendix R extends the block certificates to positive boundary weights and absorbs the joining error; N transfers the full bound | R gives the complete action; O supplies the final nonzero period and actual completed metric | All chosen core witnesses have sufficiently small boundary ratios; the final knot pairing and long fixed twists are required |
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

**Resolvent reproduction and face-grid support.** Appendix N now proves
that the constructed coefficient functional recovers a multiplier at
an annihilating element. For a split monic polynomial \(p\) of degree
\(m\ge1\) over a commutative ring and an element \(w\) with \(p(w)=0\),
synthetic division constructs
\(V_w(X)=(p(X)-p(w))/(X-w)\). The quotient here is a polynomial;
no inverse or distinct-root hypothesis is used. If \(\ell_p\) takes
the coefficient of \(X^{m-1}\) in the canonical remainder, then
\(\ell_p(fV_w)=f(w)\) for every polynomial \(f\), including those of
degree at least \(m\). Seven Lean declarations establish this from
the actual coefficient-list operations. The matrix application uses
the commutative algebra generated by one Casimir and the scalars.
Its annihilating polynomial and the original crossing values and
derivatives are required source inputs; matrices at different boxes
are not required to commute. The subsequent local Fourier proposition
in Appendix N now supplies the actual annihilator and the homogeneous
matrix adapter directly. It works with the original coproduct matrices,
retains endpoint zeros, and derives both the factor \(1/N\) and the
canonical integer displacement in the even-level phase. Its proof
uses a genuine similarity, not reconstruction from repeated
eigenvalues. The separate finite-field checker includes an erroneous
residue-phase convention that it detects at even levels.

Appendix O also gives the precise finite grid selector. With
\(d=N-1\), its \(R\) ordinary nonnegative face exponents must each
be congruent to \(d\) modulo \(N\). The numerator's total degree
is \(Rd\), so those minima force every ordinary exponent to equal
\(d\) and both protected exponents to vanish. The exterior protected
face is fixed, not averaged; no residue condition there is assumed.
The translated even-level character is consequently one. Six Lean
declarations prove this support implication and its converse selector,
but do not construct the physical grid or prove its character
orthogonality. The original winding, cup, cap and mark factors remain
the written source adapter.

The added complete-radius calculation in O differentiates the triangle
potential into a weighted graph Laplacian. Its positive edge weights
and connected ordinary graph leave only the common-scale kernel;
the fixed protected strip removes that scale. The optional
[weighted-graph module](../formal-real/WeightedGraph.lean) now proves
the finite quadratic-form step: it constructs the edge energy and
Laplacian, propagates equality along positive-weight paths, and proves
strict positivity after one vertex is fixed. The differentiation that
identifies the geometric Hessian, the conductance signs and the
connectivity of this particular graph remain written arguments.
The analytic reading also
checks the signed charge derivative, the order of the two contour
neighborhoods and the exact paired endpoint current. It uses the
whole shared complex-strip estimate, including real spectator spectra.
The odd simple spectral node contributes its value, whereas double
nodes contribute their values and first derivatives. O's wording now
makes this distinction explicit. The conclusion remains the nonzero
whole central period at both parities for sufficiently long fixed
signed powers; the full invariant requires its separate restricted
remainder theorem.

**The latest finite-algebra and interface reading.** Appendix N now
includes a proved product-reduction proposition: factors may be reduced
before multiplication, and both value and first derivative are retained
at a repeated root. The corresponding Lean module constructs the product
and proves its compatibility with reduction. A second module checks
Appendix M's coefficient recovery under \(u=hs\), including the exact
limitation of every finite-order truncation. The
[reading record](manuscript_audit/products-and-regrading.md) states their
scope and the further analytic and geometric inputs.

The same reading corrected two expressions. Appendix Q now uses
\(Q(0,e^{q_{11}},e^{q_{14}})\), distinguishing positive weights from
face labels. Appendix O now states holomorphic convergence
\(B_{e,N}\to B_{e,0}\), with \(B_{e,0}(0)=C_e>0\), instead of
asserting a constant limit away from the origin. Shrinking the fixed
chart gives the positive real part needed in the proof. Neither
correction changes the theorem's scope.

The statement-level map for N–R can be checked with
`python3 repro/check_manuscript_logic.py --output repro/results/manuscript-logic`.
It detects missing premise roles, lost hypotheses, level mismatches and
cycles, and rejects fourteen deliberately invalid substitutions. It retains
the open general remainder. This is a consistency check of a declared
proof map, not a verification of its mathematical assertions.

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

**Degree and operator order.** The all-orders chapter and Appendix M
now denote the fixed annihilator order by \(r_P\), keeping it distinct
from the spectral degree \(d=N-1\). The required translates are
\(s,s+1,\ldots,s+r_P\), a fixed finite collection. Appendix M also
states that its Hermite, supremum and Chebyshev norm comparison is for
the canonical representative of degree less than \(N\). Products of
higher degree must first be reduced by the exact folding identity.
Otherwise a nonzero multiple of the spectral polynomial would have
zero Hermite data, and the asserted comparison would fail.

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
next module proves uniqueness under a coefficientwise degree bound,
idempotence, and invariance under reordering the roots, including
repeated roots. Its final theorem gives sufficient hypotheses for a
candidate additive functional to equal the constructed one. Those
hypotheses are part of that characterization. The resolvent module
now provides a direct reproduction proof under the actual annihilator
hypothesis, rather than assuming quotient compatibility or
diagonalizability. Appendix N states both results in ordinary
polynomial notation. The
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
| [Uniqueness and root order](manuscript_audit/monic-uniqueness.md) | Canonical remainders, arbitrary zero padding, repeated-root permutations, and the precise hypotheses of the functional characterization |
| [Directed circle trees](manuscript_audit/directed-tree.md) | K's main criterion, the complete conditional remainder, the degree-or-twist implication, and the F/G metric-volume interface |
| [All orders and recurrence factors](manuscript_audit/directed-all-orders.md) | Exact interpolation identities, the degree filtration, formal regrading and gauge, and the independent finite-sum existence proof |
| [Directed asymptotics and coefficient functionals](manuscript_audit/directed-monic-logic-followup.md) | Fixed operator order and canonical-degree norm comparison; semantic reading of the three split-monic modules and the distinction between the unit functional, source trace and crossing multiplier |
| [The geometric branch and longitude](manuscript_audit/directed-geometry.md) | I/M's marked reconstruction, preferred longitude and cusp conventions; the new local rigidity proof on the retained augmented triangulation |
| [Source coverage and parity](manuscript_audit/source-coverage-followup.md) | The recursive complementary-color proof and the statement-level dependency order of N, O, L and P; separate all-level results from odd-level cap research |
| [Protected triangular sums](manuscript_audit/protected-sum.md) | Three sector comparisons, duplicate target cancellation, the N/O import interface, exact input certificates, and the bounded scope of the new Lean declarations |
| [Retained geometric cells](manuscript_audit/retained-geometry-followup.md) | Primitive logarithmic periods, absolute volume calibration, and the precise rank, positivity and decoration assumptions in the filled-germ argument |
| [Products, formal coefficients and volume interfaces](manuscript_audit/products-and-regrading.md) | Actual canonical multiplication and repeated-root derivatives; regrading injectivity and finite-jet scope; O's complex cofactor inputs and the separate full remainders in P and Q |
| [Finite source and whole filling period](manuscript_audit/finite-source-and-filling-followup.md) | The local functional, source estimates, both-parity central period, independently long signed charges, and the separate geometric completion |
| [Original invariant and normalization](manuscript_audit/original-invariant-normalization-followup.md) | Defining Kashaev crossing weights, their finite Fourier comparison, complete-color turns and the full modified-dimension scalar |
| [Local Casimir and face polynomial](manuscript_audit/local-casimir-source-followup.md) | Actual annihilating relation, crossing values and normals, and the direct Fourier adapter with its endpoint and phase conditions |
| [Positive local source inputs](manuscript_audit/positive-local-source-followup.md) | The pair-trace and cofactor identities entering the central analytic estimates, with their uniformity assumptions |
| [Marked source and face coefficient](manuscript_audit/marked-source-adapter-followup.md) | Primitive face grids, original cup and cap factors, parity cosets, total-degree selection, and the limitations of the finite formal support proof |
| [Central coefficient companion](manuscript_audit/source-asymptotics-companion.md) | The exact cofactor phase, fixed complex neighborhoods, entire face torus, primitive Gaussian measure, shared spectral gap and all-parity normalization; includes the necessary positive outer-sum hypothesis |
| [Geometric companion's regulator](manuscript_audit/marked-fillings-regulator.md) | The explicit cusp-side logarithms, the distinction between coefficient-row and tangent pairings, absolute integration constant, and comparison on the same filled fundamental chain |
| [Geometric companion's construction](manuscript_audit/marked-fillings-construction.md) | Positive packing, the original augmented exterior, marked deformation, primitive peripheral words, signed classical saddle and smooth completion; fixed-basis logarithmic periods are checked before multiplication by the filling integers |

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

The monic-remainder and resolvent calculations construct the finite
coefficient functional and prove its algebraic reproduction property.
Their source application uses the actual Casimir annihilator,
Chebyshev root data, original crossing jets and scalar norm. Appendix N
now supplies the annihilator and local adapter by the explicit Fourier
calculation. A list
of roots supplied to the algebraic theorem is not itself a proof that
the spectral polynomial has those roots with those multiplicities.
The diagram adapter also needs the literal marked tensors and their
normalization. The new support module proves the exponent consequence
of its degree and residue premises, not that the physical diagram
supplies those premises. Real and complex analysis, and the construction
of the completed hyperbolic metric, remain further written stages.

The protected-sum follow-up also corrected a quantifier in the guide:
the seventeen-region example defeats one required anchored bound for
every choice of shared weights; it does not defeat every anchored bound.
Its forty-branch certificate is unabridged in the precise sense needed
for composition. Appendix Q now states its scaling law explicitly as
logarithmic homogeneity, and gives the assembled diagram's full hypotheses
before asserting its volume conclusion.


## Ordinary triangular boundaries

[The Appendix R audit](manuscript_audit/triangular-boundary.md) follows
conditional disk minimization, boundary development, the zero-boundary
limit, and the extension of finite source witnesses. The decisive
comparison splits according to the entire inserted block. This removes
extra middle-weight inequalities that are unnecessary once the block's
strict certificate absorbs the joining error. The original boundary
coefficient demands are retained throughout.

The finite reproduction checks the explicit seventeen-region extension
and the original restricted dual, with oriented small constructions as
incidence checks. Nine new Lean declarations verify the scalar
comparisons and their exact target correction. The full project now
contains 241 compiled declarations with inspected axiom dependencies.
The additional source-assembly and limit declarations are described below.
The dependency map has 49 statement-level nodes and fourteen invalid-map
controls. These counts describe the checks, not the fraction of the
manuscript formally verified. Its analytic and geometric arguments
remain written proofs.

## From the whole remainder to the volume limit

The formal project now proves the final implication as an epsilon-limit
statement. `SourceAssembly` constructs the sum over the entire retained
sector list, preserves its multiplicities under an additive filling
functional, and bounds it using the local estimates and the filling
norm. The admissible degree class is explicit. No bound for arbitrary
higher-degree polynomials is inferred.

`LevelLimits` retains the level subsequence in every eventual estimate.
It combines the two parity conclusions and constructs common thresholds
for finitely many estimates and independently long fixed signed powers.
`VolumeTransfer` derives actual modulus domination from a strict rate
gap, then uses the triangle and reverse triangle inequalities to prove
eventual nonvanishing and equality of rates. It restores the scalar
normalization and transfers the geometric action to the volume attached
to the same diagram and filling tuple.

These are conditional mathematical proofs, not a dependency graph whose
vertices are named after desired conclusions. Their analytic inputs are
explicit: a nonzero central asymptotic, the upper rate of the full
remainder, and elementary laws for modulus and a scaled logarithm.
The optional [Mathlib package](../formal-real/README.md) now constructs
those laws for the actual complex norm and `Real.log(x)/N`. It proves
that the epsilon definition is ordinary convergence through all
sufficiently large integer levels. It also derives the leading rate of
`N^k a_N exp(N S_N)` from a fixed real exponent, a coefficient converging
to a nonzero value, and a convergent complex action. Its final theorem
proves eventual nonvanishing and the ordinary `2π/N` logarithmic limit.
These elementary analytic steps are formalized. The exact source
identity, the diagram-specific asymptotics, the whole-remainder estimate
and the geometric volume comparison remain written arguments.
The original packet theorem assumes one coefficient limit. The added
residue-class theorem permits a different nonzero amplitude limit and
a different complex action limit on each class, provided all action
limits have the same real part. Its parity corollary proves the
even/odd assembly directly, retaining the original denominator
\(N\), including when \(N=2n+1\).

The optional package also constructs the real energy
\(E(f)=\sum_e w_e(f(s_e)-f(t_e))^2\) and its incidence-matrix
Laplacian. Nonnegative weights and actual finite paths through the
positive support imply that the zero-energy functions are constant.
Fixing one vertex then gives strict positivity for every nonzero
variation. This is the linear-algebra implication used after the
written geometric Hessian calculation, not a formal proof of that
calculation or of circle-pattern existence. The real-calculus module additionally derives the quadratic cost from
actual second derivatives and the local entropy gain from a supporting
tangent. Its two-branch estimate constructs the balance defect before
applying the strict sector comparison. The geometric formulas supplying
those derivatives and entropies remain written inputs. The package
contains ten definitions and fifty theorems, with all sixty declarations
included in its axiom audit. Its replay checks nine pinned Git
dependencies and twelve negative controls. These counts are separate
from the 241 declarations in the Std-only project.

The dependency map now also records the recursive construction, the
summed, local and directed tree criteria, and terminal decoration.
Its checks reject substitution of a different family's source or period
even when the two statements have the same level scope. This is a
consistency check on the map, separate from the Lean implications and
from the mathematical proofs of its premises.

## The completed-root theorem and the strict-tree extension

The reference manuscript's first theorem retains its completed-root
grammar. The research notes extend the source argument to general strict
ordered trees by adding an exact junction normal form, absolute boundary
profiles, positive closing comparisons and spectral loss propagation.
They also need the quarter-index leaf expansion and the geometry with
individual face masks. These are additional written arguments, not
consequences of the narrower manuscript theorem alone.

The dependency graph now records those inputs separately and distinguishes
the completed-root source bound, filling theorem and metric from their
strict-tree extensions. The geometric longitude argument in Appendix J
uses the marked strict-tree geometry; it does not require the full quantum
volume limit or its global alias estimate. The broader source notes still
need their own companion paper and detailed review. Acyclicity and valid
source locations do not establish those mathematical arguments.

## Where this research phase ends

The companion-paper review found two issues that a list of successful
finite calculations would not resolve. The local cofactor logarithm
needs \(x+y>0\); with both outer variables zero its zeros approach
the complete spectral point. The actual matched-sphere construction
excludes that case, and the local proposition now states the hypothesis.
The geometric paper also needed an explicit dictionary between its
normal-flow vectors and the actual cusp logarithms. It now develops
the positively ordered tetrahedron \((0,\infty,1,z)\), lists all four
cusp-side tables, derives similarity holonomy by telescoping triangle
scales, and distinguishes the row pairing from the induced tangent
form. Its symbolic checker now tests the side-coordinate formulas as
well as the bilinear identity. The written topological and analytic
arguments remain necessary.

The scope is now frozen at the stated restricted families, including
ordinary triangular insertion. A broader knot class, a smaller explicit
constant, or another proposed method is not a requirement for finishing
this phase. The unrestricted matched-sphere volume conjecture remains
open in this account.

The stopping criterion is a reviewable proof, not the number of lemmas or
successful computations. For each retained volume theorem, the record
must locate the exact invariant identity, the nonzero leading term, the
whole remainder estimate, the primitive metric completion, and the
absolute volume comparison. Their hypotheses and level scope must agree,
and the final rate transfer must use those statements without an open
premise. A genuine missing argument must be repaired or the conclusion
narrowed; it cannot be replaced by a numerical test or a consistency check
of the dependency graph.

The finite certificates must be reproducible from committed inputs, with
explicit rounding or truncation bounds and checks of the original source
and coefficient targets. The manuscript and guide must state the same
quantifiers and limitations, define their notation and render their
formulas and diagrams correctly. The review record must also say which
imported proofs were read and which parts remain outside formal
verification. It must not turn a bounded review into a claim of complete
machine verification.

Once these conditions are met for the release's stated claims, further
research stops for this phase. Formalizing all of analysis and geometry,
optimizing the chain length, enlarging the knot class, and pursuing the
archived cap, transport and torsor proposals are separate projects.
Finding a defect in the retained proof reopens only the affected
argument and its dependent conclusions.
