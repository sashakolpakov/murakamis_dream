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

For an ordered tree with at least one edge and an integer
two-strand braid at every junction, the [directed subtree theorem](https://sashakolpakov.github.io/murakamis_dream/notes/actual_all_circle_directed_volume.html)
gives an explicit bound independent of the number of pieces:
\[
                         |n_v|\ge2^{27}
\]
at every vertex suffices. Here \(n_v\) is the signed number of
half-twists. The original endpoint pairing must form one knot,
with no component already closed inside an intermediate tangle.
The theorem proves hyperbolicity and the volume limit through
both even and odd quantum levels. Every tree and all its powers
are fixed before the level tends to infinity.

More generally, if \(d_v\) counts incident tree edges, each vertex
may independently satisfy either
\[
                  |n_v|\ge2^{27}\quad\text{or}\quad d_v\ge2^{28}.
\]
Thus sufficiently large degree permits any fixed signed power,
including zero. One can retain an arbitrary fixed core with a knot
pairing and attach an even number \(B\ge2^{28}\) of terminal
pieces at each core vertex, in the specified order, each with
an odd power of magnitude at least \(2^{27}+1\). This preserves
the endpoint pairing and gives a knot covered by the theorem;
the added pieces generally change the knot itself.

The [summed criterion](https://sashakolpakov.github.io/murakamis_dream/notes/actual_all_circle_quantitative_volume.html)
remains a useful alternative:
\[
                  \sum_v\frac{d_v}{d_v^2+n_v^2}\le2^{-25}.
\]
For a tree with \(E\) edges, every \(|n_v|\ge8192\sqrt E\)
suffices for that test. Either proof identifies the rate with the
volume of the actual knot complement, using its original marked
fillings. These constants are sufficient bounds, not sharp thresholds.
The earlier local criterion is retained as an included theorem.

The [closure extension](https://sashakolpakov.github.io/murakamis_dream/notes/actual_conway_arbitrary_closure_volume.html)
also allows cap closures and exact cancellation of twist sums. Its
reduction can split the diagram into connected-sum factors. For a
hyperbolic input, if every surviving strict factor has sufficiently long
net twists, exactly one such factor remains and all other factors are
unknots. The original knot is therefore isotopic to a covered long-twist
knot. This extends the criterion for presentations, without adding an
estimate for short twists.

The [moving-meridian theorem](https://sashakolpakov.github.io/murakamis_dream/notes/actual_main_meridian_filled_volume.html)
also controls the invariant within distance of order $1/N$ of completeness
for every fixed strict Conway tree with independently sufficiently long
signed twists. Product junctions may have arbitrary valence and adjacency.
The theorem gives a uniform volume limit, a nonzero normalized profile,
and a first correction determined by the preferred cusp shape. The
[results chapter](https://sashakolpakov.github.io/murakamis_dream/guide/results.html#the-volume-limit-while-the-meridian-varies)
explains the finite-sum comparison and its hypotheses.

These intrinsic conclusions also pass through the net-twist and closure
reductions when their stated hypotheses on twist length and the knot hold. The
ambient isotopy preserves the whole zero-framed meridian family and the
preferred peripheral curves. The comparison uses the volume and cusp of
the original knot, even when its reduced presentation has a different
auxiliary augmented link. The meridian disk stops before the first
ordinary-color resonances; continuation through them remains a separate
problem.

![Tangle reduction, the finite quantum evaluation, and the volume of the resulting knot complement](book/figures/research-map.png)

The [full microscopic expansion](https://sashakolpakov.github.io/murakamis_dream/notes/actual_main_meridian_filtered_characteristic.html)
also selects a classical curve in any genuine annihilating operator.
The [strict-tree geometric longitude theorem](https://sashakolpakov.github.io/murakamis_dream/notes/actual_strict_tree_geometric_characteristic.html)
identifies this curve with the preferred meridian--longitude deformation
for every covered strict long-filling construction, including junctions
without crossing circles. The earlier summed circle-tree theorem
and the local theorem with
bound \(2^{-120}\) also supply the required full expansion and
geometric identification. Consequently the selected
geometric irreducible factor divides the first nonzero classical
symbol of every genuine
all-level annihilator of the reduced invariant. Marked ambient isotopy
also carries this conclusion to the covered net-twist and closure inputs.
The result does not identify all factors, their multiplicities, or the
entire recurrence ideal.

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
