# Murakami’s Dream

Kashaev invariants and the hyperbolic volumes of knot complements.

**[Read the illustrated guide](https://sashakolpakov.github.io/murakamis_dream/)** ·
[Manuscript and PDF](manuscript/README.md) ·
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

The broadest construction begins with a finite simple triangulation of
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
powers must also be sufficiently long. The
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

## Ordered tangle trees and explicit bounds

The paper also develops Conway’s algebraic, or arborescent, constructions
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

## The meridian and the A-polynomial

For the covered strict-tree constructions and the directed circle-tree
criterion, the original reduced invariant has a full expansion on the
required microscopic meridian charts. Its first correction is determined
by the preferred cusp shape. The highest-degree terms of that expansion
recover the preferred geometric longitude.

Consequently the selected geometric irreducible factor divides the first
nonzero classical symbol of every genuine fixed operator annihilating
the whole reduced invariant at all sufficiently large levels. This
retains the exact peripheral normalization; it does not identify every
A-polynomial factor, its multiplicity, or the full recurrence ideal.
The new decorated planar theorem concerns the complete meridian value;
a corresponding moving-meridian theorem for that larger class remains
separate work.

## Reading and reproducing the work

The [manuscript](manuscript/README.md) is the continuous proof account.
Chapter 1 separates full volume theorems from completed partial results:
a finite filling estimate and a theorem about one geometric contribution
do not assert the volume limit for an arbitrary original invariant.
New generalizations are included only when their arguments are complete.
The open remainder estimate for unchanged general diagrams is not a
premise of the restricted-family proofs.

The [illustrated guide](https://sashakolpakov.github.io/murakamis_dream/)
also explains the approaches that remain incomplete. Its
[methods chapter](https://sashakolpakov.github.io/murakamis_dream/guide/methods.html)
introduces the techniques, gives their literature references, and
distinguishes completed arguments from proposed extensions. The
[algebraic approaches chapter](https://sashakolpakov.github.io/murakamis_dream/guide/algebraic.html)
defines the earlier torsor and gluing proposals, works out the
factorial model's move test, and explains the remaining comparison
problems. The
[research library](https://sashakolpakov.github.io/murakamis_dream/library.html)
retains the Fourier, torsor, weighted Cauchy, cube, and other approaches,
including failed estimates and the reasons they failed. These historical
notes are not additional premises of the manuscript's theorems.

The illustrated guide is the maintained documentation. Former Sphinx
addresses redirect to it; there is no second exposition to keep in sync.

| Directory | Contents |
| --- | --- |
| `manuscript/` | TeX paper, bibliography, figures, and compiled PDF |
| `repro/` | Check runner and the precise scope of its checks |
| `book/` | Guide chapters and editable diagrams |
| `docs/` | Published illustrated guide |
| `notes/` | Detailed arguments and historical research notes |
| `experiments/` | Verification programs and recorded results |
| `tools/` | Paper, guide, and figure builders |
