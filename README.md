# Murakami’s Dream

Kashaev invariants and the hyperbolic volumes of knot complements.

**[Read the illustrated guide](https://sashakolpakov.github.io/murakamis_dream/)** ·
[Research papers](papers/README.md) ·
[Dependency graph](https://sashakolpakov.github.io/murakamis_dream/papers/dependencies.html) ·
[Reference manuscript](manuscript/README.md) ·
[Reproduction instructions](repro/README.md)

For a fixed hyperbolic knot $K$, the volume conjecture predicts

$$
 \lim_{N\to\infty}\frac{2\pi}{N}\log|K_N(K)|
       =\operatorname{Vol}(S^3\setminus K).
$$

Here $K_N(K)$ is the reduced Kashaev invariant at level $N$, with
unknot value one. This repository develops proofs for specified
families built from planar tangle diagrams. The diagram and every
twist number are fixed while $N$ tends to infinity.

For a first reading, start with
[the diagram, its finite evaluation, and the meaning of the limit](https://sashakolpakov.github.io/murakamis_dream/guide/starting.html).
The guide defines its terms before using the source-polynomial and
geometric constructions. The
[results chapter](https://sashakolpakov.github.io/murakamis_dream/guide/results.html)
states the precise hypotheses for each family.
Its [literature comparison](https://sashakolpakov.github.io/murakamis_dream/guide/results.html#comparing-the-result-with-other-volume-statements)
also distinguishes the Kashaev limit from Turaev–Viro volume statements,
and records restrictions such as odd levels or a specified link family.

## Planar constructions with arbitrarily many tangles

One general construction begins with a finite simple triangulation of
the sphere and a pairing of its triangles across selected edges. Every
triangle belongs to exactly one pair. The paired triangles specify
crossing-circle tangles and the connections between their strands.
The construction places the resulting augmented link in the three-sphere;
it does not require the tangle operations to form a tree.

There is an explicit finite decoration of this diagram for which the
volume conjecture holds after all twist regions receive sufficiently
long signed twists. At each original crossing circle, insert an even
number of additional terminal tangles on each side. The numbers are
chosen from the circle packing constructed in the proof. Give the new
pieces odd crossing parity, and choose the original parities so that
following the strands gives one knot. Every original and added twist
number may then be chosen independently, with either sign, beyond one
threshold for the decorated diagram.

The resulting knot is hyperbolic and its reduced Kashaev invariant has
the knot-complement volume limit through all integer levels. The added
tangles preserve the chosen endpoint pairing, but generally change the
knot. The theorem concerns this decorated knot; the original core’s
powers must also be sufficiently long. The companion paper
[Balanced circle packings from terminal tangle decorations](docs/papers/terminal-decorations.pdf)
proves the literal insertion, the packing recurrence and strict balance
at every old and new region. It imports the finite evaluation, analytic
and geometric results stated in the foundation papers. The
[statement and construction](https://sashakolpakov.github.io/murakamis_dream/guide/results.html#decorating-a-planar-diagram)
explain the quantifiers and the geometric condition that the decoration
establishes.

![A local insertion subdivides one triangle and preserves the original matching edge.](book/figures/balanced-terminal-fans.png)

The proof controls the entire finite invariant, including the terms
outside the geometric contribution. A strict inequality at each crossing
circle, evaluated in one shared circle packing, makes those remaining
terms exponentially smaller. The geometric contribution is nonzero.
Its peripheral equations complete the auxiliary cusps by smooth solid
tori while leaving the main knot cusp complete, so the limiting action
is the volume of the actual knot complement.

## When the original diagram already satisfies the packing condition

A further theorem requires no added tangles. If the complete circle
packing satisfies the explicit **weak balance inequalities**, independently
sufficiently long signed twists at the existing crossing circles give
the full volume limit, provided the original strand connections form one
knot with no extra closed main component. Equalities in the packing
condition are allowed.
The proof perturbs the radii used in the coefficient estimate: a linear
entropy gain dominates the quadratic increase of the stationary action.

This is a condition on the unchanged diagram, not a claim about every
circle packing. [The statement and proof explanation](https://sashakolpakov.github.io/murakamis_dream/guide/results.html#an-unchanged-diagram-satisfying-weak-balance)
define all its quantities. Appendix P gives the proof and a quantified
extension allowing small failures of the local inequalities.

## Joining certified diagrams

A [triangular-sum theorem](https://sashakolpakov.github.io/murakamis_dream/guide/results.html#joining-diagrams-with-a-shared-weight-certificate)
preserves the full source estimate when certified matched spheres are
joined along specified triangles. Any fixed finite number of certified
pieces is allowed. An explicit sequence has $17+r$ crossing regions
after $r$ attachments and retains a failure of weak balance at its mark.
Its strict source certificates nevertheless give the volume limit after
independently sufficiently long fixed fillings. Appendix Q defines the
operation, its input certificates and its knot-component requirement.

Appendix R permits an insertion away from the protected edge. Its
attaching triangle has three positive circle curvatures; two must be
sufficiently small relative to the third at every coefficient witness
used by the core. An explicit even chain makes these ratios as small
as required. Consequently any fixed finite collection of certified
pieces can be attached to a suitable core, followed by independently
long fixed signed twists. The
[construction and proof](https://sashakolpakov.github.io/murakamis_dream/guide/results.html#inserting-a-piece-at-an-ordinary-triangular-face)
explain the boundary condition and the exact coefficient demands.

## Ordered tangle trees and explicit bounds

The reference account also develops Conway’s algebraic, or arborescent, constructions
by stacking and turning rational tangles. A reduction combines twist
boxes that can be brought together. Sufficiently large surviving *net*
twists give the volume limit; large individual counts alone need not
suffice when opposite signs cancel.

For an ordered tree with a crossing-circle tangle at every vertex and
at least one edge, a separate theorem gives an explicit sufficient
condition. If the signed crossing power at every vertex has magnitude
at least $2^{27}$, the volume equality holds, independently of the tree’s
size and depth. More generally, each vertex may satisfy either this
twist bound or the degree bound $2^{28}$. The latter allows any fixed power,
including zero. The original strand connections must form one knot,
with no extra component closed inside a tangle.

The [results chapter](https://sashakolpakov.github.io/murakamis_dream/guide/results.html)
also gives a summed criterion that can produce smaller bounds for a
particular tree, and explains the exact net-twist and closure reductions.
These explicit tree bounds and the planar decoration theorem have
different hypotheses; neither is a classification of all hyperbolic knots.

Two new companions extract separate inputs to the tree proofs.
[Newton coefficients and positive sources for Conway tangles](docs/papers/newton-tangles.pdf)
proves the exact turn, product, closure and circle formulas, including
repeated-root derivatives, and the variational limit of the positive
complete auxiliary-color source. Signed fillings still require their
own remainder and noncancellation estimates.
[Positive octahedra and primitive fillings for trees of crossing circles](docs/papers/circle-tree-geometry.pdf)
constructs the actual filled hyperbolic metric whenever
$\sqrt{d_v^2+n_v^2}\ge630$ at every vertex. This geometric criterion permits
zero powers at high degree; it does not by itself prove a quantum limit.
Its peripheral-volume input is a local differential from the geometric
foundation, so no independently long-twist assumption is imposed on
these zero-power cases.

[Volume asymptotics for trees of crossing circles](docs/papers/circle-tree-volume.pdf)
proves two distinct sufficient conditions in one 27-page account. The
summed condition is $\sum_v d_v/(d_v^2+n_v^2)\le2^{-25}$; the directed
condition uses local estimates along the tree. The proofs share their
finite kernel and Fourier trace, then establish their own remainder and
noncancellation estimates. Both give a uniform microscopic meridian
profile. The explicit first correction is retained under the summed
condition alone. Each proof verifies the geometric threshold above.

For every fixed strict Conway expression with at least two original
crossing circles,
[Holomorphic source asymptotics and volume limits for strict Conway compositions](docs/papers/conway-asymptotics.pdf)
proves the nonzero leading term of the entire filled invariant and its
volume limit, provided the actual closure is a knot and all signed powers
are independently sufficiently long. It imports the strict optimizer,
whole complementary-source bound and marked geometry by numbered theorem,
then proves the pure-source expansion and absolute action comparison.
Its separate signed local results and the quarter-index paper are not
premises of this volume theorem.

## The meridian and the A-polynomial

The 20-page
[moving-meridian source paper](docs/papers/moving-meridian-sources.pdf)
controls the actual finite source when the main meridian is
$M=q_N^s$, with $s$ in the stated fixed microscopic parameter sets.
It treats arbitrary strict product junctions, retains their shared
indices and proves a nonzero joint filling contribution for independently
long fixed signed powers. This supplies the error bounds needed to
expand the whole invariant, rather than only its selected local term.

The 13-page
[meridian-expansion paper](docs/papers/meridian-expansions.pdf)
then proves every inverse-level order for these strict sources and,
separately, for circle trees satisfying the summed or directed criterion.
The estimates hold on the translated parameter sets needed by a fixed
recurrence. The degree of each logarithmic coefficient identifies its
highest-degree term with the stationary action. A separate classical
argument identifies the resulting germ with the preferred longitude;
in particular, the first correction is determined by the preferred cusp
shape. The analytic expansion itself does not assume that geometric
identification.

Theorem 1.2 and Corollary 8.1 give a conditional consequence: start with a
specified fixed nonzero operator annihilating the **whole reduced
meridian function at every sufficiently large integer level**. Its first
nonzero classical symbol contains the selected geometric irreducible
factor. The proof retains the meridian divisor and sign in the exact
reduced/full normalization. It does not construct such an operator,
identify every A-polynomial factor or its multiplicity, or establish the
full AJ conjecture. For strict sources, the geometric corollary takes
the larger of the analytic and classical filling thresholds.
The new decorated planar theorem concerns the complete meridian value;
a corresponding moving-meridian theorem for that larger class remains
separate work.

## Reading and reproducing the work

Choose a theorem in the
[dependency graph](https://sashakolpakov.github.io/murakamis_dream/papers/dependencies.html)
and open **The recorded proof route**. This lists the statements it uses
in prerequisite order, with each shared result appearing once. Follow
that route through the [papers organized by subject](papers/README.md);
there is no need to read the whole collection before approaching one
application. The graph records declared theorem uses. Its cycle and
source-location checks do not verify the proofs themselves.

The collection currently contains **21 drafts, totaling 403 pages**, each
between 11 and 29 pages. These are provisional mathematical groupings,
not a decision to publish 21 separate papers. Shared finite algebra,
coefficient estimates, asymptotic analysis and hyperbolic geometry should
each have a clear home. An application cites the numbered statements it
needs and checks their hypotheses.

The [frozen reference manuscript](manuscript/README.md) has 374 pages:
93 pages of main text, 266 pages in eighteen appendices, 13 pages of front
matter, and two pages of references. Several mathematical projects
accumulated in that account, with repeated setup and summaries followed
by full proofs. Its length is not the length of one proof of the general
volume conjecture. Splitting the material has made individual arguments
easier to follow, but has not reduced the total page count. Current
papers also contain expanded proofs and broader results. The Newton,
circle-tree and Casimir consolidations have removed ten pages of overlap;
we have not measured how much more can be removed. The
[manuscript guide](https://sashakolpakov.github.io/murakamis_dream/guide/manuscript.html)
explains the current division and the [errata](manuscript/ERRATA.md)
record corrections to the frozen account.

The [closing assessment](repro/RETAINED_RELEASE_ASSESSMENT.md) records the
completed review of the retained restricted results. For each volume
conclusion, the proof needs an exact invariant formula, a nonzero leading
term, a bound for the whole remainder, the intended hyperbolic metric,
and an absolute comparison between its volume and the same action.
The open remainder estimate for general unchanged diagrams is not an
input to the retained restricted-family arguments. Further families,
stronger estimates and the general conjecture remain separate research.

There are three different kinds of checks:

- The [finite reproduction suite](papers/README.md#building-and-reproducing-the-papers)
  runs 22 groups covering exact formulas, rational and interval
  inequalities, normalization factors and endpoint pairings. It does
  not infer an asymptotic theorem from sampled levels.
- The [Lean library](formal/README.md) proves finite algebra and theorem
  assembly. The [Mathlib extension](formal-real/README.md) also proves
  concrete calculus, norm and logarithmic-limit results, formal series
  identities and the nonzero classical-symbol implication under its
  stated recurrence assumptions. The
  [coverage record](repro/PAPER_FORMAL_COVERAGE.md) identifies the written
  analytic, geometric and topological inputs. No actual knot-family
  theorem is claimed as an end-to-end Lean proof.
- The [guide checks](book/README.md#rebuilding-the-guide) verify rendered
  formulas, navigation and illustration assets. Paper builds check
  typesetting, references and page limits.

The [illustrated guide](https://sashakolpakov.github.io/murakamis_dream/)
is the maintained web exposition. Its
[methods](https://sashakolpakov.github.io/murakamis_dream/guide/methods.html)
and [algebraic approaches](https://sashakolpakov.github.io/murakamis_dream/guide/algebraic.html)
chapters retain the Fourier, torsor, weighted Cauchy, cube and other
approaches, including unsuccessful comparisons and the reasons they
failed. Definitions, literature references and limitations accompany
those discussions. The
[research library](https://sashakolpakov.github.io/murakamis_dream/library.html)
keeps the detailed notes available. Historical approaches are not extra
premises of a current theorem. Former Sphinx addresses redirect to the
guide; there is no second exposition to maintain.

| Directory | Contents |
| --- | --- |
| `papers/` | Current subject drafts, earlier editions, and the dependency inventory |
| `manuscript/` | Frozen reference manuscript, illustrations, bibliography and errata |
| `repro/` | Reproduction commands, recorded results and scoped proof reviews |
| `formal/` | Lean proofs of finite algebra and internal implications |
| `formal-real/` | Mathlib proofs of calculus, limits and formal-series implications |
| `book/` | Illustrated-guide sources and editable diagrams |
| `docs/` | Published guide, dependency graph and PDFs |
| `notes/` | Detailed arguments and historical research notes |
| `experiments/` | Verification programs and recorded calculations |
| `tools/` | Paper, guide, graph and figure builders |
