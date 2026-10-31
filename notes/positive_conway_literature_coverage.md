# Coverage check for the retained-circle Conway theorem

Checked 29 October 2026. This is a comparison of definitions and
stated coverage, not an audit of external proofs and not an import of
their proof techniques. The current own results are the
[actual local source cells](actual_newton_ideal_prism_and_associativity.md)
and [whole retained cylindrical Conway theorem](actual_positive_conway_hyperbolic_volume.md).
The exact grammar is A=h^3, E ::= A | R E | E E, followed by the
specified cap-sum boundary reduction. It is not identified here with
all arborescent or all fully augmented links.

## 1. Augmented knotted trivalent graphs

Van der Veen's [2009 paper, Definition 2 and Theorem 2](https://arxiv.org/html/0805.0094v2)
starts from a KTG move sequence. Its main theorem requires sufficiently
many augmentation rings at each unzip, with the threshold depending
on the sequence. The stated quantum formula uses odd N; its even-N
values vanish. The geometric part is a regular-octahedral outside,
with additional Seifert pieces for multiple-ring unzips, and gives
volume (2t+2)v8 for t triangle moves.

This is substantial prior coverage of augmented examples. Applying
that theorem to a current diagram would require an explicit KTG move
sequence, the required augmentation multiplicities, and an exact
comparison of its invariant normalization with the original marked
source used here. None is implied merely by retaining crossing
circles. In particular an odd-level colored-Jones statement cannot
silently replace the current positive all-level source identity.

## 2. Fundamental shadow links and octahedral fully augmented links

Ibarra, McQuire and Purcell's
[2026 paper, Definition 2.8 and Theorems 2.12 and 4.15](https://nyjm.albany.edu/j/2026/32-1v.pdf)
restricts the relevant class to octahedral fully augmented links.
It identifies their complements with fundamental-shadow-link
complements and states a Turaev–Viro volume theorem without half
twists, along odd levels. The displayed volume is 2(c-1)v8 for c
crossing circles. The paper explicitly distinguishes this invariant
and root from the colored-Jones/Kashaev setting.

Our cell construction uses general ideal prisms and pyramids and
does not assume a regular-octahedral decomposition. The words
“fully augmented” therefore do not establish coverage by that
theorem. Conversely, this observation alone is not a proof that
our entire class is new or strictly larger: an exact inclusion or
noninclusion requires a diagram or geometric certificate. No such
general class equivalence is asserted in this coverage check.

## 3. Whitehead chains

Van der Veen's [Whitehead-chain paper](https://arxiv.org/abs/math/0611181)
states a volume-conjecture result for a particular infinite link
family containing the Whitehead link and Borromean rings. It does
not state a theorem for arbitrary branching and turn depth in the
current expression grammar. Overlapping examples should retain their
earlier attribution; no claim of disjoint classes is made here.

## 4. The geometric program also has direct antecedents

The primary abstract of Jun Murakami's
[13 October 2026 IPAM talk](https://mathinstitutes.org/videos/25102)
describes a route from doubled right-angled fully augmented polyhedra
to deformed filled complements and spatial-graph invariants. This is
an explicitly related program. The abstract presents an approach;
it does not state the current all-level theorem for this exact
source grammar. Its proofs have not been audited here.

Thus the broad idea of relating augmented-link quantum expressions
to geometric polyhedra should not be advertised as new. The concrete
claims to assess in this repository are narrower and checkable:
the original full Newton coefficient, its positive all-level limit,
the exact prism face metric as an action derivative, its actual
ordered stack map, and the complete geometric realization of the
specified retained cylindrical factors.

## 5. What this check does and does not establish

The consulted primary statements do not by themselves subsume the
present exact grammar, normalization and all-level conclusion. This
is a limited coverage finding, not an exhaustive priority claim.
It supplies no reason to trust or reject any external proof. The
own local and global arguments must stand on their explicit source,
topological, geometric and completeness calculations.

A future comparison should record, for each proposed inclusion, the
actual diagram transformation and the complete invariant dictionary:
color dimension versus highest weight, root convention, component
normalization, marking and framing, and level subsequence. Those
data are mathematical hypotheses, not optional bibliographical
details. Until they are supplied, the safe statement is the explicit
retained-circle theorem, not a claim to settle arbitrary augmented
links, arbitrary hyperbolic knots, or all formulations of the volume
conjecture.

## 6. Coverage check for the signed long-filling extension

The stated coverage of Ce Shen's
[September 2026 preprint, version 3](https://arxiv.org/abs/2609.11839v3)
is long integral fillings of marked fundamental-shadow-link exteriors
for SO(3) Turaev--Viro invariants along odd levels, with a corresponding
Witten--Reshetikhin--Turaev asymptotic. This is directly related prior
coverage. Its statement alone does not give the full-level original
Kashaev invariant for the present signed Conway knot diagrams. No proof
from that preprint is used here, and its correctness was not audited
in this coverage check.

The Ibarra--McQuire--Purcell paper cited above likewise explicitly
distinguishes its Turaev--Viro conclusion and its octahedral class.
The current signed-coupon construction retains the general prism and
pyramid geometry, the selected original period, actual primitive
odd-link meridians, and both level parities. An identification of an
overlapping subfamily still needs the explicit diagram and invariant
dictionary. No exhaustive novelty claim or equality of the present
grammar with all arborescent links follows from this limited check.


## 7. Ordered compositions with long net twists

Checked 31 October 2026. The [net-twist theorem](actual_conway_net_twist_volume.md) uses actual tangle isotopies to reduce an arbitrary fixed ordered cylindrical product closure to a strict template or an elementary two-strand braid closure. Its bound concerns the final disjoint sums of twist integers. The analytic input is the earlier strict-tree theorem in this repository. The comparison below concerns the main statements of primary papers; their proofs are not used or assessed here.

| Primary statement | Coverage relevant to this comparison |
| --- | --- |
| [Jun Murakami, double-twist knots, Theorem 1](https://arxiv.org/html/2501.00225v3#Thmthm1) | The stated volume-conjecture theorem covers hyperbolic double-twist knots without a long-twist condition. This is direct prior coverage of an arborescent subfamily; the present theorem makes no priority claim for those knots. |
| [Chen–Zhu, twist-knot asymptotics, Theorem 1.2 and Corollary 1.4](https://arxiv.org/pdf/2307.13670v1#page=3) | The ordinary-root result concerns twist knots with parameter at least six. It does not state an arbitrary ordered-tree theorem. |
| [Van der Veen, Whitehead chains, Main Theorem](https://arxiv.org/pdf/math/0611181v2#page=2) | The one-belt statement runs through all levels. With two or more belts the even-level invariant vanishes and the expansion uses odd levels. These are specified link constructions; passing to knots by filling every auxiliary circle requires an additional argument. |
| [Van der Veen, augmented knotted trivalent graphs, Theorem 2](https://arxiv.org/pdf/0805.0094v2#page=5) | For a fixed graph-move sequence, sufficiently many augmentation rings give the stated odd-level theorem. The rings remain present, and the displayed even-level invariant is zero. This does not by itself establish the present all-level filled-knot conclusion. |

Two more recent statements concern different objects. [Ge's Theorem 1.1](https://arxiv.org/pdf/2609.27635v1#page=1) asserts existence of finite geometric ideal triangulations for complete finite-volume cusped hyperbolic manifolds. It is not a theorem about a quantum invariant. [Liu–Ming–Sun–Wu–Yang's Theorem 1.6](https://arxiv.org/html/2608.16560v1#S1.Thmtheorem6) states a volume asymptotic for their modular-double Turaev–Viro state integral on a geometric ideal triangulation. Identifying that integral with the finite-dimensional reduced Kashaev invariant would be a separate theorem; the triangulation assertion does not supply such an identification.

Similarly, [Ge–Meng–Wang–Yang, Theorems 1.1–1.2](https://arxiv.org/html/2410.20489v1#S1.Thmthm1), concerns Reshetikhin–Turaev and Turaev–Viro asymptotics of closed manifolds obtained by surgery on sufficiently twisted twist knots. There the knot cusp is filled. The net-twist theorem leaves that cusp unfilled and evaluates the reduced knot invariant through all integer levels.

This search did not locate a main statement with the precise ordered-composition, net-weight and all-level hypotheses used here. That limited finding is not an assertion of novelty or exhaustive coverage. Overlap should be settled by matching actual diagrams, normalizations and level conventions.
