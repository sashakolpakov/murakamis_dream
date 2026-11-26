# Critical-coordinate bounds conditioned on three consecutive types

Research proof, 4 November 2026. The full 256-bit outward cover and
independent written/code audit have passed. Completed source artifacts
are unchanged.

For an actual cyclic word, let three consecutive vertices have type
indicators \((\alpha,\beta,\gamma)\in\{0,1\}^3\), and write their
right legs as \((a,b,c)\). The original zero-lift critical point is
the one in the [universal localization theorem](research_mixed_cyclic_critical_localization.md).
The already established actual leg rectangles are
\[
 R_3=(.30,.39)+i(-.03,.02),\qquad
 R_4=(.27,.33)+i(-.057,-.02).
 \tag{1}
\]

**Theorem 1.** The following open intervals contain the indicated
coordinates of every original cyclic critical point. Every entry
in the table is divided by \(1000\).

| Types | \(\Re b\) | \(\Im b\) | \(\Im a\) |
|---|---|---|---|
| 000 | (322,349) | (−10,10) | (−17,10) |
| 001 | (358,379) | (−17,−2) | (−19,7) |
| 010 | (271,292) | (−49,−30) | (−25,1) |
| 011 | (302,318) | (−57,−43) | (−25,1) |
| 100 | (311,334) | (−17,2) | (−51,−31) |
| 101 | (346,363) | (−25,−11) | (−53,−34) |
| 110 | (268,288) | (−54,−36) | (−61,−42) |
| 111 | (299,313) | (−62,−49) | (−61,−42) |

These intervals may be intersected with (1) for an actual cyclic
leg. No such intersection is used to discard a point of the open
window image in the certificate.

The [open-window theorem](research_mixed_cyclic_critical_height_bounds.md),
Lemma 2, supplies a unique holomorphic original critical branch for
every finite window on a neighborhood of each full product of typed
external disks. In particular it applies to a window of three
vertices. The closed rectangles in (1) are strictly inside those
disks. Hence the real and imaginary parts of each window coordinate
attain their extrema on products of the two rectangle boundaries,
by two successive harmonic maximum principles. This reduction is
used only after the independent whole-product existence theorem.

There are eight ordered windows, four external type pairs, and
sixteen pairs of rectangle sides: exactly 512 two-real-parameter
products. The checker reconstructs the original logarithmic
six-variable equations, using the unchanged open-window affine
Newton primitive. Each accepted rational dyadic cell has an affine
parameter enclosure and a weighted disk remainder satisfying a
strict self-map. The zero-lift equations and the original common
chamber identify it with the global branch. The entire image is
tested against all three table intervals. Prefix freedom and exact
dyadic mass one check each whole boundary product. The full cover
passed all 512 products, with 4,778 accepted cells and 9,044 visits
at 256 bits. Stored decimal coordinate hulls are display summaries;
acceptance checks the original outward intervals, and the exact
binary addresses specify the complete reproducible cover.

At an actual cyclic point the two external legs belong to (1),
so the window restriction solves the same original equations.
Uniqueness identifies it with this open-window solution. For cycles
of length one or two, repeat the cyclic period before extracting
the three-vertex window. Repeated incidences preserve the literal
equations and the identification; distinct vertices are not an
assumption of this argument.

This is a geometric enclosure only. In particular, a source target
whose imaginary part depends on \(\Im a,\Im b,\Im c\) does not
automatically have a harmonic supporting-plane defect as a function
of these references. No source estimate or global contour bound is
inferred from the table.

Reproduction:

```sh
python experiments/certify_mixed_neighbor_conditioned_critical_boxes.py --precision 256
```
