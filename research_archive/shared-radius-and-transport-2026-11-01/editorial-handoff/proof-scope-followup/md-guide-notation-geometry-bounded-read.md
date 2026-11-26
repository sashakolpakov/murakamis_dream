# Bounded notation and geometry read

This read covers the current public `book/chapters/starting.md`, `notation.md`, and `geometry.md`, with targeted comparison to the finite-source manuscript chapter and the cited geometric-completion statements. It is an editorial/source-interface read, not a fresh verification of every linked proof. No public file was changed and no scientific computation was run.

## Corrections sent to the parent

1. `book/chapters/notation.md:415`: “positive main meridian eigenvalue” should read “eigenvalue of the positively oriented main meridian.” The eigenvalue is complex; positivity describes the chosen orientation, not its numerical value.
2. `book/chapters/geometry.md:187,229,255`: the unqualified statements that the action equals volume obscure the normalization fixed at the beginning of the chapter. The normalized quantum source action has real part equal to volume divided by \(2\pi\). The all-circle completion explicitly proves \(\operatorname{Vol}_c=2\pi\Re\mathcal C(c)\). State that factor, or explicitly introduce a separately rescaled geometric action.

The sine-product translation requested by the parent is already present at `notation.md:29`: the manuscript's \(s_r\) in `manuscript/sections/02-finite-source.tex:106` is the guide's \(S_r=\prod_{a=1}^r2\sin(\pi a/N)\), whereas the guide's \(s_r\) is a single sine factor. The different local uses of \(h\) are explicitly scoped and do not require a repository-wide rename.

## Scope retained

The read found no additional essential undefined symbol or incorrect figure caption in these three chapters. In particular, the geometric threshold is explicitly separated from the stronger quantum estimates; the all-CROSS geometric contribution is separated from control of the other source terms; and the angle-polytope and representation-volume discussions do not infer a contributing quantum cycle from a geometric critical point. The doubled-projection and local-cell volume factors are explicitly explained in the later local-action section.

One linked technical note has a stale historical scope sentence: `notes/actual_conway_pointed_quantum_a_volume.md:319` calls the directed all-orders expansion a separate requirement, whereas the guide now correctly links the completed `actual_all_circle_directed_all_orders.md`. This is a source-navigation consistency issue, not a missing proof in the guide's current statement. No linked source was edited during this read.

## Private research freeze

The protected marked-row scalar proof, its exact finite checker, and the independent absolute-array read remain frozen under the paths and hashes in `md-protected-left-sharp-spectral-manifest.json` and `md-protected-left-and-absolute-array-handoff.md`. The finite checker was run before this editorial task. Its conclusions do not include a signed-source exponential lower bound or a new volume theorem.
