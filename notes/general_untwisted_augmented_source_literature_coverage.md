# Coverage of the untwisted augmented-source volume theorem

Checked 30 October 2026 against the primary versions linked below. This
compares definitions and theorem statements with
[the untwisted source theorem](general_untwisted_augmented_source_volume.md).
It imports no external proof or proof technique and makes no priority claim.

The present statement fixes one connected augmented plat, its actual
labeled convex ideal right-angled cut polyhedron, and its complete link
exterior. It concerns the original single-mark root invariant, no retained
half twists, and the full integer sequence of levels. It does not concern
arbitrary filled knots, all retained half-twist sums, or an invariant chosen
only after fixing a geometric triangulation.

## 1. The invariant name is not a distinction

Murakami--Murakami, *The colored Jones polynomials and the simplicial volume
of a knot*, arXiv:math/9905075v2, 10 June 1999, Theorem 4.9, identifies their
Kashaev invariant with the normalized colored Jones evaluation for every
link and every integer N>=2. The introduction specifies N-dimensional colors,
a primitive N-th Jones root, and unknot value one. Thus an overlapping
colored-Jones theorem cannot be excluded merely by calling our source
"original Kashaev." [Primary version, pp.1 and15](https://arxiv.org/pdf/math/9905075v2).

Our parameter dictionary is q=exp(pi i/N), Jones t=q^2, and skein
A=exp(pi i/(2N)). The
[literal source identity, section4](general_matching_graph_full_normal_source.md)
divides exactly one ordinary physical trace factor
D_N=(-1)^(N-1)[N] before root specialization, equivalently retains its
specified first normal. It is not division by one quantum dimension for
every component. Mark, framing and dual-order phases must still be matched
in any concrete comparison; they cannot convert an exact zero into a nonzero
value when they are units.

## 2. Direct overlapping link results and the parity test

Van der Veen, *Proof of the volume conjecture for Whitehead chains*,
arXiv:math/0611181v2, 30 July 2007, Main Theorem, covers W_(a,b,c,d).
Its b=1 conclusion runs over all N; this includes the named Whitehead-link
and Borromean-ring examples. For b>=2 the statement is odd-only and the
even evaluations vanish. Definition1 makes b the number of Belt tangles.
The generic normalization on printed p.4 is
sum_n [2n+1]/[N] times the composed tangle eigenvalues, so the even zeros
are not explained by a different number of component reductions. The text
also records a Seifert piece when b>=2. [Primary version, pp.2--4](https://arxiv.org/pdf/math/0611181v2).

This possible contradiction was checked against the actual diagram, not
dismissed by terminology. In Figure1 a Belt is one circle around two straight
strands. The stated commuting composition permits two Belt copies to be
adjacent. Their circles cobound an annulus disjoint from those strands; the
literal cut graph has two parallel MAIN edges with an intervening white
bigon. A nondegenerate face of the required convex ideal polyhedron cannot
be that bigon. Independently, our exact face polynomial reproduces the even
zero: the intervening middle-face degree is at most a_1+a_2<=N-2, whereas
the marked coefficient requires N-1. This is a finite source compatibility
check, not an asymptotic argument. The complete labeled geometric certificate
is essential; connectedness or the word "augmented" alone is insufficient.

Van der Veen, *The volume conjecture for augmented knotted trivalent graphs*,
Algebraic & Geometric Topology9 (2009), 691--722, Definition2 and Theorem2,
uses a KTG move sequence and a sequence-dependent minimum number of
augmentation rings at every unzip. It states an odd-N SO(3) volume law and
zero even-N evaluations. The singly augmented outside consists of regular
ideal octahedra; additional rings introduce the stated Seifert pieces.
The normalization divides by an unlink according to SPLIT components,
not by every link component. This is substantial prior augmented-family
coverage, but the theorem's multiplicity and parity hypotheses must be
retained. [Published primary paper, pp.692,695--696](https://msp.org/agt/2009/9-2/agt-v9-n2-p02-s.pdf);
[arXiv:0805.0094v2, 5 February 2009](https://arxiv.org/abs/0805.0094v2).

## 3. Octahedral results and nearby quantum regimes

Ibarra--McQuire--Purcell, *Augmented links, shadow links, and the TV volume
conjecture: A geometric perspective*, New York J. Math.32 (2026), 1--34,
Definition2.8, restricts "octahedral" to the indicated regular-ideal-octahedron
decomposition. Theorem2.12 identifies these complements with fundamental
shadow-link complements. Theorem4.15 gives the untwisted Turaev--Viro volume
limit at exp(2pi i/r), odd r. Theorem4.16 also gives a colored-Jones limit
for equal colors m at t=exp(4pi i/(2m+1)), with m even; Remark4.17 presents
the extension to all m as an expectation. This is not the ordinary
N-dimensional/Jones-root exp(2pi i/N) specialization merely by renaming m.
The introduction explicitly attributes earlier Kashaev coverage of
octahedral augmented examples to van der Veen. [Published primary version,
pp.4,8,30--31](https://nyjm.albany.edu/j/2026/32-1p.pdf).
The earlier arXiv:2506.09296v1 has different theorem numbering; the numbers
here are those of the journal version.

Wong--Yang, *Relative Reshetikhin--Turaev invariants, hyperbolic cone metrics
and discrete Fourier transforms I*, arXiv:2008.05045v4, 11 December 2022,
Theorem6.3, states generalized colored-Jones asymptotics for twisted
octahedral fully augmented links at exp(4pi i/r), odd r, with colors giving
sufficiently small cone angles. Theorem6.1 includes the corresponding odd-r
Turaev--Viro statement, including twists. These are important overlapping
geometric families and quantum conclusions, not a theorem restricted to
the untwisted case. Their root/color and relative-RT conventions still
need to be retained when comparing the exact invariant above.
[Primary version, sections1.1 and6](https://arxiv.org/html/2008.05045v4).

## 4. General polyhedra and triangulations are separate coverage

Belletti, *An upper bound conjecture for the Yokota invariant*,
arXiv:2002.01904v2, 20 June 2024; published AGT25 (2025), 645--675,
Theorem4.9, proves its upper-bound conjecture for graphs obtained from the
tetrahedron by the two specified vertex/face moves. The trivalent Yokota
invariant is a unitary bracket absolute square, with odd root order and
its own admissible colors. The right-angled rectification and TV consequences
are relevant prior coverage, but do not identify the original single-mark
all-level link source. [Primary version, Definition2.7 and Theorem4.9](https://arxiv.org/html/2002.01904v2).

Ge's *Geometric ideal triangulations of hyperbolic 3-manifolds*,
arXiv:2609.27635v1, submitted 23 September 2026, is an existing primary
preprint. Theorem1.1 states geometric ideal triangulation existence for
every complete finite-volume cusped hyperbolic 3-manifold. This is a geometric
statement, not a Kashaev/colored-Jones asymptotic, an invariant-normalization
identity, or a theorem selecting an original quantum period. No inference
about the correctness of its proof is made in this coverage check.
[Primary statement](https://arxiv.org/html/2609.27635v1).

Jun Murakami's 13 October 2026 IPAM talk abstract explicitly describes
fully augmented right-angled polyhedra and their complexified filling
deformations. This is a closely related existing program, but that abstract
does not state the present full-level untwisted theorem.
[Primary event abstract](https://mathinstitutes.org/videos/25102).

The search also found Casandra Monroe's 2018 Princeton senior thesis,
*Knot Too Big: The Volume Conjecture for Augmented Links*. Its repository
abstract concerns fully augmented links. The repository's PDF endpoint
required authentication during this check, so its theorem statements were
NOT verified; its title alone supports neither inclusion nor exclusion.
[Primary repository record](https://theses-dissertations.princeton.edu/items/c0cd5846-e602-42cc-b935-b9e36c73fb7e).

## 5. Publication wording supported by this check

The result should acknowledge existing Whitehead-chain, augmented-KTG and
octahedral-link volume results. Its precise statement concerns the recorded
original source for any fixed untwisted augmented plat with the specified
complete labeled right-angled certificate, without assuming a regular
octahedral decomposition. The consulted primary statements do not by
themselves establish inclusion of that entire class with that exact all-level
normalization. This bounded check is not an exhaustive novelty conclusion.

For any claimed overlapping diagram, first match the literal topology,
augmentation multiplicities, quantum root and color dimension, one-cut
normalization, framing, and level subsequence. Existing covered cases remain
covered; a different presentation is not a new case. Conversely, a TV or
generalized-Jones theorem cannot silently be substituted for the ordinary
root specialization. The known parallel-belt even-zero family shows why
these checks are mathematical requirements rather than bibliographical
qualifications.

No external proof techniques were used. The theorem's own proof remains
the exact source/coefficient identity, its global coefficient asymptotic,
the uniform channel upper rate, and its absolute geometric normalization.

The comparison in Section 2 concerns the literal parallel-belt annulus/bigon and the even-level middle-face degree obstruction. It is not a verification of the external volume proofs.