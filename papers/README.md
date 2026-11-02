# Finite quantum invariants and hyperbolic volume

The manuscripts are organized by the mathematical results they establish
and the results they use. The dependency graph records those relations
before assigning paper boundaries. A finite spectral theorem should be
citable independently of an asymptotic theorem; a geometric filling
construction should state precisely the information needed to compare
its volume with a quantum action.

The 374-page reference account contains 93 pages of main text, 266 pages
of appendices, and 15 pages of front matter and references. The appendices
collect several subjects: finite quantum algebra, geometric constructions,
asymptotic estimates, sufficient conditions for different knot families,
and meridian and longitude results. Those subjects accumulated in one
file; the length does not show that one theorem requires 374 pages.
The account remains available while this division is prepared. The working
limit of 30 pages per paper is an editorial constraint, not the principle
for grouping results.

[Explore the dependency graph](../docs/papers/dependencies.html).
Each statement lists the results it uses, the reason for each use, and
the exact place where the statement or proof can be found. Arrows run
from prerequisites to their consumers. The overview groups related
results; the detailed view retains the individual statements.

The components are finer than the eventual papers. They are not a proposal
for one paper per box. Overlapping arguments belong in the same article:
the broader Conway source estimate has been incorporated into the existing
source paper, with its earlier local estimates retained as separate exports. For example, finite spectral algebra and exact
diagram evaluation now form one article, with the global contraction
and normalization calculations included. The graph keeps them as
separate components because the abstract norm theorem does not use
that contraction argument.

The current source-asymptotics proof defines its finite action directly
from the exact cofactor polynomial. The earlier fold interpolation
remains in the reference account and guide as an alternative construction;
the direct proof does not require both routes. This is one concrete way
the dependency analysis shortens the presentation without removing a
needed argument.

Three other distinctions determine the division. The classical filling
construction does not need a nonzero quantum asymptotic; their comparison
comes later, through the same marked critical equations. A nonzero
geometric contribution does not bound the rest of the invariant. Finally,
weak balance, protected triangular gluing, ordinary triangular insertion
and the three-braid comparison provide different sufficient estimates
for that remainder. Protected gluing does not require weak balance. The
ordinary-insertion estimate has a separate proof; the construction of a
common core for several inserted diagrams also uses protected gluing.

## The current drafts

The twenty current papers total 329 pages, with individual lengths from
11 to 28 pages. Each gives the proofs of its stated results and names
its numbered companion imports. Two earlier geometry editions, totaling
another 25 pages, are preserved below for existing citations. This is a
partial extraction of the reference manuscript; the remaining theorem
families are listed at the end of this guide.

**Finite spectral evaluation and uniform filling bounds.** 28 pages.
[TeX source](filling-bounds/main.tex) ·
[PDF](../docs/papers/filling-bounds.pdf)

This paper asks how a fixed twisting operation acts on a polynomial of
degree less than the root-of-unity level. It defines the functional at
simple and repeated spectral roots, proves its norm bound, and explains
why the canonical polynomial representative matters. It then proves the
exact coefficient formula for a marked planar diagram constructed from a
matched triangulated sphere. The proof includes the face variables, the
integer support, the shifted grids at even levels, the cups and caps,
and the single reduced cut. A finite Fourier and matrix calculation
compares the result with the reduced Kashaev invariant, including the
framing factor. These results supply the finite formulas used by later
papers. They do not estimate the large-level invariant or identify an
exponential rate with volume.

**Newton coefficients and positive sources for Conway tangles.** 18 pages.
[TeX source](newton-tangles/main.tex) ·
[PDF](../docs/papers/newton-tangles.pdf)

This paper supplies the additional finite calculus for composing turned
two-strand tangles. It proves the Newton product, physical quarter-turn,
closure and colored-circle formulas in the full Casimir quotient,
retaining the derivatives at repeated spectral roots and the retained
half-twist factors. It uses the finite paper's operator and reduced
Kashaev normalization. For the stated class of fixed Conway compositions,
it then proves the positive complete auxiliary-color source's variational
limit, strict interior maximum and stationary boundary bounds at both
level parities. The positive source is not the signed filled invariant.
The analytic estimates for that invariant remain separate. Other companions supply the moving-meridian formulas, the larger strict
variational problem and the complete geometric interpretation.

**Stationary profiles of strict Newton trees.** 14 pages.
[TeX source](strict-newton-profiles/main.tex) ·
[PDF](../docs/papers/strict-newton-profiles.pdf)

Which ordered tangle expressions admit an interior state of the positive
sum? This paper answers the question by computing the exact integer
supports, then their strict real intervals, under products and turns.
It proves that the independent summation coordinates form a primitive
integer lattice. A boundary argument excludes degenerate maxima;
strict concavity gives a unique interior maximum and its nondegenerate
Hessian. These conclusions also hold when an output is fixed.

The stationary value as a function of that output is its boundary
profile. The paper calculates these profiles, including their additive
constants, and proves the harmonic addition rule for their parameters.
It also proves that every stationary leaf index is at least one quarter
of the level. The elementary positive-sum limit and these variational
facts need neither a bound for the signed invariant nor a global
hyperbolic metric. Later papers use them for those separate purposes.

**Exact Newton calculus for tangles with a moving meridian.** 15 pages.
[TeX source](meridian-tangles/main.tex) ·
[PDF](../docs/papers/meridian-tangles.pdf)

The parameter of the main strand now varies while the quantum level stays
fixed. The paper starts with the physical representation matrices and
computes the partial trace before identifying its polynomial form. It
proves all six oriented quarter-turn formulas and keeps the derivatives
needed when spectral roots coincide, including at the additional
collisions away from the complete meridian. The closing scalar and
crossing phases are retained. The resulting tree formula sums every
index and gives the same contraction regardless of the order in which
vertices are eliminated. These are exact finite identities; they do not
show which part of the sum dominates as the level grows. The comparison
with Kashaev's original normalization imports the finite spectral paper
at levels at least three; the algebraic identities hold from level two.

**Spectral estimates for Conway tangle sources.** 28 pages.
[TeX source](conway-source-bounds/main.tex) ·
[PDF](../docs/papers/conway-source-bounds.pdf)

An auxiliary circle has an integer color between one and the quantum
level. The theorem bounds the whole source uniformly over all these
colors. It proves a strict exponential loss when any color stays a fixed
fraction below the level, and also bounds the entire difference between
the source and its central part. Theorem 1.1 treats any fixed strict
expression with at least three leaves; Corollary 9.1 proves the two-leaf
case separately. All retained half-twist signs and both level parities
are included.

The proof uses the value and first derivative at every repeated spectral
root. An exact Fourier formula controls a colored circle followed by a
turn, including its endpoint terms. Products between such turns are
bounded by positive sums with their shared indices retained. Two rational
supporting-plane inequalities and the absolute boundary profiles propagate
these bounds through the whole expression. The older signed recurrence
estimates remain available as local results; they are not premises of
this global argument. The conclusion is a bound before filling, with no
claim here about a nonzero filled invariant or its volume.

**Marked geometry of strict Conway compositions.** 21 pages.
[TeX source](strict-conway-geometry/main.tex) ·
[PDF](../docs/papers/strict-conway-geometry.pdf)

This paper extends the geometric construction to every fixed expression
passing the strict-state test. Four separate boundary-edge labels record
which shaded triangles have already been attached. Tracking them through
each product and turn proves convexity and identifies the assembled
polyhedron with the original projection cut. The complete metric is
therefore on the specified augmented link complement, with the original
meridians and primitive disk longitudes.

The complex face maps then give a marked deformation with complete main
cusps. Solving the primitive filling equations in one neighborhood permits
independently long twists of either sign. Smooth completion and a
comparison of the same oriented fundamental chain identify the absolute
filled volume. The local cell construction is included: supporting
planes, dihedral angles, tetrahedron volumes and the entire ordered
face maps are derived explicitly. The paper also computes the original
collar translations and their deformed multipliers. The two earlier
geometry papers are no longer prerequisites. The remaining companion
imports are the stationary-profile theorem and the general primitive
completion and volume differential. There is no quantum asymptotic
premise.

**Holomorphic source asymptotics and volume limits for strict Conway compositions.** 20 pages.
[TeX source](conway-asymptotics/main.tex) ·
[PDF](../docs/papers/conway-asymptotics.pdf)

This paper proves the nonzero asymptotic of the whole reduced invariant
for every fixed strict Conway expression with at least two leaves,
provided its actual strand pairing gives a knot and all signed twist
powers are independently sufficiently long. The expression and the
powers are fixed before the level tends to infinity.

The exact expansion of each full crossing power in ordinary colored
circles permits the analytic calculation to use the pure source.
Canonical factorial interpolation agrees exactly with its finite
coefficients, including at a quarter-index leaf. Summing over the original
wire lattice gives a nonzero local Gaussian term. A second finite Fourier
sum has a real local phase and a strict bound away from its maximum.
The source bounds control the original physical error before the
whole-period filling theorem is applied. Its nonzero amplitude supplies
the lower bound needed for a volume limit.

An explicit classical shear then identifies the quantum action with the
primitive filling action on the actual retained half-twist partner.
The calculation keeps its additive constant and the integer slope;
odd powers are not treated as half-integral surgery on another partner.
The signed local coefficient and completed-root source expansions remain
proved in the same article as separate reusable results. The strict
volume route does not require those signed expansions or the
quarter-index recurrence theorem.

**Ordered tangle reductions and long net twists.** 15 pages.
[TeX source](conway-reductions/main.tex) ·
[PDF](../docs/papers/conway-reductions.pdf)

Large written twists can cancel. This paper determines the signed sums
that survive an ordered tangle construction before applying a long-twist
theorem. It proves the actual collar isotopy that slides a twist box past
a tangle, retaining the resulting rotation. An unrooted tree records
which original labels fuse. The net blocks are independent of crossing
parities, although their order and the recorded rotations can depend on
those parities.

A vanishing net weight needs a separate treatment: the turned zero box
is a cup and a cap. Deleting it changes the closure, and a sphere through
two connecting strands can split a cap-closed product. The proof tracks
every component and shows that the resulting reduction terminates.
For sufficiently long surviving strict weights, an elementary
meridian-centralizer argument shows that a hyperbolic input has exactly
one strict terminal factor and only unknot factors beside it. The input
is isotopic to that strict knot, so the strict companion's volume limit
applies. The paper gives a criterion on terminal factors and a sufficient
condition on all nonzero subset sums. It supplies no numerical universal
twist threshold and makes no claim about all short-twist arborescent knots.

**Asymptotics of signed Newton coefficients near the quarter index.** 11 pages.
[TeX source](quarter-index-asymptotics/main.tex) ·
[PDF](../docs/papers/quarter-index-asymptotics.pdf)

At one quarter of the level, the two roots of the signed leaf recurrence
have equal modulus. The earlier high-index contraction no longer applies
across that point. This paper first reduces the actual matrix recurrence
on a fixed complex domain, then chooses a short propagation interval
whose relative action cannot amplify the exponentially small remainder.
Both initial components come from the original finite sum. The resulting
holomorphic interpolation retains the same nonzero amplitude and absolute
shear action. A local Gaussian consequence states its wire-window and
lattice hypotheses explicitly. These are local analytic results for use
in broader Conway arguments; they do not bound a whole complementary
source or prove a further knot-family volume theorem.

**Uniform spectral bounds for local Casimir sources.** 14 pages.
[TeX source](local-coefficients/main.tex) ·
[PDF](../docs/papers/local-coefficients.pdf)

This paper proves the estimates needed before applying Cauchy's coefficient
formula to a collection of tangles. It defines the local polynomial by an
explicit banded matrix and partitions its paths into three degree regions.
Theorem 1.1 bounds all three regions over the entire real spectral interval
and for arbitrary phases of the face variables. The proof includes the
signed recurrence, both unused spectral products, the endpoint optimization,
both level parities and face variables fixed exactly at zero. It imports
the operator identification from the finite spectral paper. It does not
assume a geometric saddle or a volume identity.

**Oscillatory filling sums with independently long twists.** 11 pages.
[TeX source](oscillatory-fillings/main.tex) ·
[PDF](../docs/papers/oscillatory-fillings.pdf)

This paper addresses cancellation in the complete Fourier filling sum.
Theorem 1.1 assumes a nonzero holomorphic expansion near the complete point
and a strict bound for the shared source away from it. It then proves a
nonzero asymptotic for the entire sum, including every nonzero integer
Fourier charge and the original endpoints. The twist integers are fixed,
independently signed and sufficiently large; their ratios are unrestricted.
The proof estimates the infinite tail before localizing the remaining
finitely many integrals. An elementary polynomial example verifies both
hypotheses explicitly. For a knot source, construction of those hypotheses
and identification of the critical action with volume remain separate
theorems.

**Holomorphic asymptotics of central shared face coefficients.** 12 pages.
[TeX source](source-asymptotics/main.tex) ·
[PDF](../docs/papers/source-asymptotics.pdf)

Theorem 1.1 supplies the two source estimates used by the filling-sum
paper. Given positive stationary face weights, it proves a nonzero
holomorphic Gaussian expansion for the actual central coefficient and
a strict spectral bound away from its complete point. The proof treats
the entire shared face torus, including the regions outside the Gaussian
neighborhood. It retains both level parities, the original coefficient
targets and the odd skipped-row term. A tetrahedral example illustrates
why repeated face labels denote one variable and why the Gaussian measure
has no extra integer-lattice factor. Section 7 states the exact normalized
input to the oscillatory theorem. Bounding the other degree sectors of
the invariant remains the task of an application theorem.

**Circle patterns and primitive fillings of augmented links.** 18 pages.
[TeX source](marked-fillings/main.tex) ·
[PDF](../docs/papers/marked-fillings.pdf)

This is the classical geometric foundation. Starting from the marked
matched sphere, the paper constructs its complete augmented exterior
and one common deformed circle pattern. It calculates the peripheral
paths through each original crossing disk, including retained half
twists. The critical equations then specify a primitive filling slope.
The proof constructs the smooth complete metric and compares its volume
with the absolute critical action using the same fundamental chain.
Theorem 1.1 holds for independently sufficiently long signed fillings;
it does not assume a quantum asymptotic. Two drawings explain the single
disk pairing and the logarithmic torus periods. The final corollary
states the exact action comparison used by the quantum applications.

**Positive octahedra and primitive fillings for trees of crossing circles.** 15 pages.
[TeX source](circle-tree-geometry/main.tex) ·
[PDF](../docs/papers/circle-tree-geometry.pdf)

For an ordered tree with an original crossing circle at every vertex,
this paper builds the actual two-octahedron block for each edge and
retains its ordered disk pages, half twists and primitive curves. With
$d_v$ the vertex degree and $n_v$ the signed crossing power, the condition
$\sqrt{d_v^2+n_v^2}\ge630$ at every vertex gives a positive cone
path ending at a smooth complete filling, together with an absolute
action-volume identity and quantitative core-length and volume-loss
bounds. A more flexible criterion uses different radii at the vertices.
The theorem allows zero power at a sufficiently high-degree vertex. Its
only specialized companion import is the geometric foundation's local
peripheral-volume differential, not that paper's long-filling existence
theorem. It supplies geometry for subsequent asymptotic applications;
it does not select a nonzero contribution to a quantum invariant.

**Degree and twist estimates for circle-tree invariants.** 15 pages.
[TeX source](circle-tree-asymptotics/main.tex) ·
[PDF](../docs/papers/circle-tree-asymptotics.pdf)

For the literal ordered circle tree, this paper proves the full invariant's
volume limit when the sum of $d_v/(d_v^2+n_v^2)$ is at most $2^{-25}$.
It permits zero crossing power at a sufficiently high-degree vertex.
The proof retains the first derivatives at repeated spectral roots when
bounding discarded Newton indices. A complex edge-sum calculation gives
the local action and amplitude. A joint Fourier argument controls all
charges and endpoint terms, keeping other variables on real integrals
or their physical grids while estimating each infinite tail. The first
charge has a nonzero coefficient at both parities. The positive-octahedra
companion identifies its action with the original knot-complement volume.
A second theorem gives the first centered microscopic meridian correction,
including its physical framing. Local and directed degree criteria, and
the all-orders longitude statements, are separate results.

**Local degree and twist bounds for circle-tree volume limits.** 15 pages.
[TeX source](directed-tree-asymptotics/main.tex) ·
[PDF](../docs/papers/directed-tree-asymptotics.pdf)

The finite tree contraction is evaluated one vertex at a time. Each
subtree polynomial is divided by its exact value at zero before the next
trace, so earlier complex contributions remain in the calculation.
A conditional kernel estimate and a fresh real-domain bound let the
induction continue without a loss proportional to tree depth. All Fourier
charges, repeated-root derivatives and endpoint terms are retained.
The explicit directed criterion implies the volume limit and a centered
microscopic meridian profile. One consequence requires, at every vertex,
either degree at least \(2^{28}\) or absolute signed crossing power at
least \(2^{27}\); the alternatives may differ between vertices.
The older uniform local condition follows as a corollary, making its
separate tiny-disk induction unnecessary here. The summed criterion has
its own proof and a sharper meridian correction; neither theorem is
substituted for the other.

**Shared face estimates and triangular gluing for planar link diagrams.** 15 pages.
[TeX source](planar-certificates/main.tex) ·
[PDF](../docs/papers/planar-certificates.pdf)

The first criterion bounds every noncentral sector using one weight for
all occurrences of each face. At the complete packing, non-strict balance
suffices: convexity gives a linear local gain under a common change of
weights, while stationarity bounds the total action cost quadratically.
The second theorem joins two marked triangular faces and transports a
certificate for every locally allowed sector string. It counts the shared
boundary target once. A fully specified seventeen-region example and
rational certificates show that this gluing theorem applies beyond weak
balance. The full volume conclusion imports the five numbered foundation
results; the source estimates and their transport are proved here.

**Balanced circle packings from terminal tangle decorations.** 13 pages.
[TeX source](terminal-decorations/main.tex) ·
[PDF](../docs/papers/terminal-decorations.pdf)

Starting from a simple marked matched sphere, the paper gives an explicit
finite number of terminal insertions on both sides of each original
crossing circle. It proves their literal endpoint connections, constructs
the packing extension while fixing all old circles, and solves the
curvature recurrence. The resulting inequalities establish strict balance
at every original and added region. Even stacks of odd terminal tangles
preserve a chosen knot pairing, while generally changing the knot type.
The strict-balance criterion in the planar paper then gives the full
reduced Kashaev volume limit after independently sufficiently long fixed
signed powers at all regions. The exact source, central asymptotic and
primitive volume inputs are named foundation results; the insertion and
all-length balance arguments are proved here.

**Triangular insertion and volume limits for augmented diagrams.** 17 pages.
[TeX source](triangular-insertion/main.tex) ·
[PDF](../docs/papers/triangular-insertion.pdf)

This paper permits insertion at an ordinary triangular face, where all
three boundary weights are positive. Its geometric theorem minimizes the
disk action with those weights fixed and proves that the result is the
removed triangle's potential plus a constant. It proves existence,
uniqueness and the joint limit when two boundary weights vanish. The
coefficient estimate then distinguishes a wholly central inserted piece
from every other sector string, keeping each old face target once.
Explicit circle chains supply small boundary ratios for any fixed finite
list of certified inputs. The proof includes the exact recurrence and
all-length inequalities; interval arithmetic checks the finitely many
constants and certificate inequalities used in the example.

**Volume limits for long alternating-generator three-braids.** 14 pages.
[TeX source](three-braids/main.tex) ·
[PDF](../docs/papers/three-braids.pdf)

This application concerns the ordinary closure of

\[
 \sigma_2^{n_0}\sigma_1^{n_1}\cdots
 \sigma_2^{n_{m-2}}\sigma_1^{n_{m-1}},\qquad
 m\ge6\text{ even}.
\]

For each fixed number of factors, the signed powers are independently
sufficiently large in magnitude, and their permutation must give a knot.
The generators alternate; the crossing signs need not alternate.
The braid axis is not a component. The paper develops the diagram,
its circle packing and the estimates that control the entire remainder.
It imports three explicitly stated results: the exact source identity,
the uniform local coefficient estimates, and the nonzero geometric
filling contribution with its absolute volume calibration. Those
dependencies are substantial. The finite input and local upper bounds are
proved in the finite spectral and local Casimir coefficient papers. The filling-sum paper proves the
analytic implication once its local expansion and global gap are supplied.
The source-asymptotics paper constructs that expansion and gap. The
circle-pattern paper supplies the marked geometric volume comparison.
The application now cites numbered statements in these companion papers,
and checks their common normalization and hypotheses.

## Earlier geometry editions

The following two papers treat the narrower completed-root construction.
They remain available for existing citations. The 21-page **Marked
geometry of strict Conway compositions** now contains the local proofs
and the broader complete and filled constructions, so these editions are
not part of its required reading.

**Pyramids, prisms, and complete geometry of Conway closures.** 13 pages.
[TeX source](conway-geometry/main.tex) ·
[PDF](../docs/papers/conway-geometry.pdf)

The positive-source maximum in the Newton paper determines ideal
hyperbolic cells. This paper proves that the stationary equations match
their entire ordered quadrilateral faces, and that successive attachments
stay convex. It then identifies the assembled boundary with the original
projection cut, checks the face maps and edge returns, and constructs
compatible horospheres at every cusp. The metric is therefore on the
specified augmented link complement. Its volume is twice the sum of the
cell volumes, or \(2\pi\) times the source action. The original meridian
and disk longitude form a primitive basis, also for the retained
half-twist partners. The theorem uses the completed-root grammar of the
Newton paper. A corollary identifies the positive complete source's rate
with this volume; neither result asserts a signed filling asymptotic.

**Marked deformations and long fillings of Conway closures.** 12 pages.
[TeX source](conway-fillings/main.tex) ·
[PDF](../docs/papers/conway-fillings.pdf)

Starting with the complete Conway metric, this paper defines a classical
cell potential and continues the full face maps and group relations.
The original meridian and disk longitude give the primitive logarithmic
filling equations. One neighborhood works for independently long signed
slopes, without restrictions on their ratios. The metric completion
keeps the main cusps complete and adds smooth solid tori along the
original auxiliary slopes. The complete volume fixes the action's
constant, and a comparison of the same fundamental chain gives the
absolute filled volume. Its proof does not use a quantum asymptotic.
The [reference errata](../manuscript/ERRATA.md) explain the corrected
factor in the filling Jacobian.

## What still needs its own paper

The division should follow results rather than cut the reference text
into equal lengths. The following groups have different mathematical
purposes:

| Subject | Result to explain and prove | Dependencies that must remain visible |
| --- | --- | --- |
| Geometric longitude and recurrences | All-order meridian expansions force the selected geometric factor to divide a classical symbol | The moving-meridian source, full expansion, normalization and preferred geometric longitude |

The frozen reference manuscript's first theorem uses its completed-root
grammar. The companion accounts now cover the larger strict syntax through
its own variational, source and marked-geometry arguments. A further
topological reduction can change the written expression before this
theorem is applied. The tangle-reduction paper supplies that step: large
written twists may cancel to a small net twist, and a vanishing net twist may change
the closure or produce additional components. The proof of those
isotopies is distinct from the strict asymptotic theorem.

These remaining subjects still need their own complete accounts. Each
candidate needs a precise theorem, complete proofs of its own claims,
defined notation, and an explicit list of imported theorems.

For a citation between papers, the exporting paper must state a numbered
theorem with its normalization, degree restrictions, level parity and
uniformity assumptions. The importing paper must name that theorem and
check those hypotheses. A reference to a folder of calculations is not
a substitute. The current drafts include the strict Conway volume theorem,
the summed and directed circle-tree criteria, and the local quarter-index
expansion, together with their finite and geometric foundations. The
all-orders meridian and longitude results still require their own
extraction and proof review.
The dependency graph keeps those obligations visible.

The illustrated guide retains the broader approaches and unsuccessful
comparisons. The reference manuscript remains available for the existing
full account. Exploratory research is separate from this editing work.

## Building and reproducing the papers

With TeX Live or MacTeX, `latexmk`, Python and PyMuPDF installed, run from
the repository root:

```sh
python3 tools/build_papers.py
```

Use a directory name to build just one paper, for example
`python3 tools/build_papers.py filling-bounds`.
The command checks the page limit, unresolved references and overfull
boxes, then copies the PDFs and their source-hash records to `docs/papers/`.
Add `--no-publish` to keep the outputs in each paper's `build/` directory.
These are typesetting checks, not mathematical verification.

Rebuild the dependency graph with:

```sh
python3 tools/build_dependency_graph.py
```

Its source is `papers/dependencies.json`. The command verifies the named
source locations, checks statement, component and article graphs for cycles,
and refuses a recorded completed result that imports an open result. Each
article import has a path through named theorem uses; the builder checks
that path and its declared ownership. Acyclic statements can become
circular when grouped into papers, so this is a separate check.
It generates the interactive graph, vector overview and source-hash
record in `docs/papers/`. These checks validate the declared dependency
record, not the proofs at its nodes or the completeness of the inventory.
The article-cycle and witness controls run with
`python3 -I tools/test_dependency_graph.py`.

Replay the papers' finite identities and rational certificate constants
with one command:

```sh
python3 repro/check_paper_algebra.py --output repro/results/paper-algebra
```

The runner requires SymPy, python-flint and NumPy. It saves a separate
record and log for each registered check group, and stops on failure. The
planar certificate groups retain their supporting interval records in
separate subdirectories. The new Newton group compares physical matrix
turns, traces, circle coefficients and crossing normals with the stated
formulas over exact finite fields. The terminal group checks symbolic
curvature identities, oriented insertions and literal pairing graphs;
its finite count examples supplement the written construction for every
length. The circle-tree group checks rational seam and peripheral
identities and the displayed numerical bounds. The constant verifier
uses outward rational bounds with explicit series remainders. The argument
for every even number of braid factors is written in the three-braid paper; it is not inferred from computations for finitely
many braid lengths. The finite checks complement the written proofs of
the analytic estimates and geometric constructions.

The local-bound and filling-sum checks can also be run separately:

~~~sh
python3 papers/local-coefficients/check.py --output repro/results/local-coefficients.json
python3 papers/oscillatory-fillings/check.py --output repro/results/oscillatory-fillings.json
~~~

These require SymPy. They check finite polynomial identities and algebraic
normalizations, with their exact scope recorded in the output. They do not
replace the written uniform estimates, contour arguments or asymptotic
proofs.
