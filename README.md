# Murakami’s Dream

Kashaev invariants and the hyperbolic volumes of knot complements.

**[Read the illustrated guide](https://sashakolpakov.github.io/murakamis_dream/)** ·
[Manuscript and PDF](manuscript/README.md) ·
[Reproduction instructions](repro/README.md)

The volume conjecture predicts that the exponential growth of Kashaev’s
root-of-unity invariant recovers the volume of a hyperbolic knot complement.
This project studies that comparison by assembling knots from tangles.

The manuscript treats a specified family of Conway tangle constructions.
Start with elementary twist pieces, join them in order, turn intermediate
tangles, and apply the prescribed closure. For each allowed finite
construction, independently sufficiently large positive or negative twist
numbers give the volume limit. The construction and all twist numbers stay
fixed while the quantum level tends to infinity.

A [companion theorem](https://sashakolpakov.github.io/murakamis_dream/notes/actual_conway_net_twist_volume.html)
starts with any fixed ordered composition closed by the prescribed
cylindrical closure. An explicit tangle reduction groups its twist numbers
into disjoint sums. Unless the result is an elementary two-strand braid
closure, sufficiently large magnitudes of these sums give the volume
limit whenever the closed diagram is a knot. These are the *net twist
numbers*: large positive and negative twists in one group can cancel.
The reduction preserves the actual knot and its complement. The
[results chapter](https://sashakolpakov.github.io/murakamis_dream/guide/results.html)
explains the groups, the closure condition, and the exact quantifiers.
Another companion reconstructs the invariant from a quantum A-operator
and initial data, giving the same volume limit in recurrence form.

The [closure extension](https://sashakolpakov.github.io/murakamis_dream/notes/actual_conway_arbitrary_closure_volume.html)
also allows cap closures and exact cancellation of twist sums. Its
reduction can split the diagram into connected-sum factors. For a
hyperbolic input, if every surviving strict factor has sufficiently long
net twists, exactly one such factor remains and all other factors are
unknots. The original knot is therefore isotopic to a covered long-twist
knot. This extends the criterion for presentations, without adding an
estimate for short twists.

A further result controls the invariant while the meridian moves within
distance of order $1/N$ of completeness. It proves a uniform volume limit
and an explicit normalized profile for long-twist presentations satisfying
an additional condition on their multiplication junctions. The
[moving-meridian section](https://sashakolpakov.github.io/murakamis_dream/guide/results.html#the-volume-limit-while-the-meridian-varies)
states that condition and explains why this stronger conclusion currently
has a narrower scope than the complete-value theorem.

![Tangle reduction, the finite quantum evaluation, and the volume of the resulting knot complement](book/figures/research-map.png)

The general conjecture remains open. In particular, the theorem does not
classify all arborescent knots or cover arbitrary short twist numbers.

## Finding the material

The guide gives a continuous explanation of the results and their proofs.
The [research library](https://sashakolpakov.github.io/murakamis_dream/library.html)
organizes supporting arguments by question, and the
[figure gallery](https://sashakolpakov.github.io/murakamis_dream/figures.html)
explains the constructions with editable drawings. The Fourier, torsor,
weighted Cauchy, cube, and other approaches remain available there.

| Directory | Contents |
| --- | --- |
| `manuscript/` | TeX paper, bibliography, figures, and compiled PDF |
| `repro/` | Exact-certificate runner and explanation of what it checks |
| `book/` | Guide chapters, reading routes, and editable diagrams |
| `docs/` | Rendered illustrated guide |
| `notes/` | Detailed mathematical arguments and historical research notes |
| `experiments/` | Verification programs and recorded results |
| `tools/` | Paper, guide, and figure builders |

## Reading locally

```sh
python3 -m http.server 8000 --directory docs
```

Open `http://localhost:8000`. See the [guide maintenance instructions](book/README.md)
for rebuilding the pages, and [reproduction instructions](repro/README.md)
for the exact arithmetic checks.

The [research log](RESEARCH_LOG.md) preserves the earlier working history.
The publication manifest records the files and hashes included in each
release.
