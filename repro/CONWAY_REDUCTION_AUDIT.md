# Ordered reductions, consolidated geometry and load equations

This record concerns the current companion papers and their declared
proof dependencies. The 374-page reference manuscript and its mathematical
sources remain frozen. The preceding [strict Conway review](STRICT_CONWAY_AUDIT.md)
records the earlier, 17-page geometry edition; the present geometric
account has 21 pages and includes the local proofs it formerly imported.

## The geometric reading route

The previous route used three papers totaling 42 pages: the 13-page
completed geometry, the 12-page completed-root filling construction,
and the 17-page strict extension. The current
[Marked geometry of strict Conway compositions](../papers/strict-conway-geometry/main.tex)
proves the needed local calculations within its 21 pages. The two older
editions remain available for citations, but no longer supply premises
of this proof.

The additions construct the leaf pyramid and multiplication prism from
their vertices and supporting planes. Positive tetrahedron subdivisions
fix their volume constants. Ordered cross ratios match the entire gluing
faces, including shear. Explicit world-coordinate matrices give all
prism transitions, the actual white triangle maps, and pure and odd edge
returns. Conjugating the original peripheral words gives the complete
collar translations; determinants and fixed-point eigenvalues give the
deformed similarity multipliers. The main Theorems 1.2 and 1.3 and the
classical potential equations (6.1)–(6.5) retain their numbering.

These local proofs do not replace the global steps. The four-edge
attachment argument still proves convexity and the original cut topology.
The cusp area proves that the traced basis is primitive. The stationary
profiles come from their separate variational paper. The classical
ideal-tetrahedron formula fixes the local normalization; the general
primitive completion, peripheral volume differential and same-chain
comparison remain explicit imports from the marked-filling paper.
There is no quantum asymptotic premise in this geometric construction.

The expanded exact checker starts with the two original chord equations,
solves for the prism vertex, and compares the independently normalized
face maps with the twelve entries of the displayed table. It also checks
the actual triangle maps, complete collar conjugations, edge scalars and
primitive multipliers. These computations supplement the written support,
convexity, topology and completion arguments; they do not establish them
by evaluating examples.

## The topological reduction and its volume consequence

[Ordered tangle reductions and long net twists](../papers/conway-reductions/main.tex)
is a 15-page account. Its topological input is an actual ordered tangle
expression, with a specified cylindrical or cap closure. Every original
leaf has a distinct label and an integer signed crossing count. All
internal closed components are retained.

The first part proves the proper rotations and the collar isotopy for
sliding an integral twist past a tangle. The rotated tangle is retained.
The fixed closing reflection gives closed turn transfer; moving the cut
around the solid torus gives closed cyclicity. These moves lead to a
terminating normalization. Contracting the zero-turn edges of its
unrooted syntax tree determines the disjoint net label blocks before
crossing parities are chosen. Parities determine subsequent rotations
and orders, not those blocks.

The second part evaluates zero sums. A turned zero box is a cup and a
cap, so deleting it changes the closure. A specified two-punctured sphere
splits a cap-closed product along the components containing its cap arcs.
The one-box endings are handled before deletion. The resulting reduction
terminates, keeps a tree of componentwise sums, and has finitely many
structural outputs for a fixed original expression. Its choices depend
only on the original parities and subset-sum zero pattern.

Under the longness hypothesis, a nontrivial terminal knot is either a
long strict knot or a nontrivial two-strand torus knot. Each has an element
outside the meridian subgroup commuting with the meridian. Two such
factors give a nonabelian meridian centralizer in the connected-sum group.
A complete hyperbolic knot cannot have that centralizer: its meridian is
parabolic, and commuting Möbius maps are translations. The torus case is
proved using its central element and the quotient free product. This
selects exactly one strict factor for a hyperbolic input; the remaining
unknot factors are removed by actual ambient isotopies.

The only asymptotic application is the strict companion's Theorem 1.1.
Its primitive slope threshold is converted to a crossing-weight threshold
and maximized over finitely many output templates and knot-producing
parities. The maximum explicitly includes zero when no such parity
exists. The actual filled knot, its meridian and preferred longitude are
transported by isotopy. The original invariant comparison is used at
levels at least three, with one reduced cut and the same zero-framing
normalization. Pullback of the strict knot's metric gives the same volume.
No connected-sum formula for a quantum invariant is assumed.

The conclusion concerns sufficiently long surviving sums, not large
written summands which may cancel. The topology works with arbitrary
weights, but the paper does not decide the geometry of a short strict
factor. It does not supply a numerical threshold uniform over growing
expressions, a prime-decomposition algorithm, a new quantum asymptotic,
or a meridian/longitude expansion. The introduction places the tangle
calculus beside Conway, Kauffman–Lambropoulou, Bonahon–Siebenmann and Volz;
those references are background coverage, not substitutes for the collar,
closure and group arguments written here.

The standard-library checker independently compares spatial matrices,
endpoint pairings with closed-component counts, and an incidence-tree
partition with the ordered fusion algorithm. Its 1,344 bounded expression
assignments retain zero sums. Endpoint pairings do not determine a tangle
isotopy, and the checker makes no such claim. The decreasing live-block
argument proves termination for arbitrary fixed size.

## What the formal proof now adds

[TriangleBalance.lean](../formal-real/TriangleBalance.lean) uses the actual
supported entropy supremum from the earlier modules. Its regular rows
have the proved arctangent maximizing loads; singleton rows have load
one half at the active corner. The derivative in a shared vertex
coordinate is the aggregate load minus the prescribed demand.

A supporting inequality follows by reusing a maximizing load vector as
a feasible competitor. Thus a grounded point is a global minimum if and
only if all free-vertex loads balance. The positive supported corner table
and connected row incidence give a unique grounded solution. No gradient
identity or minimizing point is supplied as an assumption.

The root equation is separate. Each triangle has total load one half,
even when its corners have repeated destinations. Once the free equations
hold, the root residual is half the number of triangles minus total
demand. It vanishes exactly under that compatibility condition. Four
compiled examples retain the half-mass convention, repeated destinations,
an arbitrary grounded root demand and the failure of uniqueness without
connected support.

The optional package now has 51 definitions and 208 theorems. Every one
of those 259 declarations is included in the axiom inventory, with only
Lean's standard foundational axioms allowed. The nine dependency pins
are unchanged; 26 deliberately invalid metadata/axiom cases are rejected.
The nine earlier mathematical modules are unchanged. Geometric Hall
feasibility, actual incidence and connectivity, developing maps,
support-changing limits, saddle estimates and metric-volume comparison
remain written application inputs.

## Dependency records and reproduction

The detailed graph separates ordered normalization, zero-cap decomposition
and terminal-factor selection from their two volume corollaries. New
local geometry nodes refer to the proofs in the consolidated article;
the earlier editions retain their historical proof nodes. The graph has
140 statements, 316 direct uses, 15 subject groups and 22 articles,
including the two earlier editions. Its 56 article imports have explicit
paths through named statements. The statement, subject and article graphs
are acyclic. These checks validate the declared inventory; they do not
prove that every mathematical dependency has been discovered.

The separate six-premise volume map now includes the strict Conway route.
It distinguishes the two-leaf source bound from the three-or-more-leaf
bound, the pure local expansion from the shared global Fourier bound,
and the unfilled source error from the full filled remainder. It checks
61 declared steps and rejects 19 invalid substitutions. The graph and
map are structural records, not Lean proofs of their mathematical nodes.

The reproducible commands are:

```sh
python3 repro/check_paper_algebra.py --output repro/results/paper-algebra
python3 repro/check_manuscript_logic.py --output repro/results/manuscript-logic
python3 repro/check_concrete_limits.py --output repro/results/concrete-limits
python3 tools/test_dependency_graph.py
python3 tools/build_dependency_graph.py
python3 tools/build_papers.py
```

The first command runs 21 finite-check groups. Their records pin the
inputs and distinguish finite identities from analytic and geometric
proofs. The formal command requires the pinned Mathlib environment.
The final command checks typesetting, page limits and references, not
mathematical validity. The [source snapshot](conway-reduction-audit-snapshot.json)
records the files used for this publication.

The current reading collection has twenty papers totaling 329 pages;
the two earlier geometry editions add 25 archived pages. This total is
not a suggested linear reading order. The all-orders meridian and
longitude accounts still need extraction and proof review. The remainder
estimate for unchanged general diagrams remains open.
