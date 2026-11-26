# Optimizing one real replacement does not appear to repair the right-star gap

This is a bounded floating diagnostic, not a proof. The standalone driver
uses only the archived repository phase helper and makes 32 pairs of
one-dimensional scalar optimizations. There is no cyclic-word search,
high-dimensional optimizer, interval cover, or temporary-file dependency.

The preserved actual example is the same alternating reference and physical
four-cycle used in the proved geometric-right-replacement obstruction.
Its middle type is three, its neighbors have type four and real angles
.1 and .5, and its right target is .5. Every target height is zero.
Replacing just that middle coordinate by any real value in [.1,.5] leaves
the other target heights unchanged: the left endpoint has zero left
cutoff and the right endpoint has zero right factor. Its own height also
stays zero because of the .1 neighbor. All selections are zero.

The floating maximum of the coherent pair is about 1.2300822022 at
t=.344134264; the complete raw-row maximum is about 1.2957014382.
Thus even this optimized single-coordinate comparison has a positive
diagnostic excess about .065619236. The original rational rows .28 and .23
are separately evaluated against a concavity tangent at the rational
center 43/125. Real low-coordinate monotonicity excludes a larger coherent
maximum below .1, while the proved real concavity justifies the tangent
formula if its values are later enclosed outward. This archive itself
does not perform that certification.

The other 31 cases only identify how type and endpoint orientation affect
this same local comparison. They are not actual new cyclic reference
theorems. The positive excess concerns an absolute-row envelope versus
a coherent replacement, not the signed finite kernel. Grouping additional
neighboring edges or using a common boundary potential remains a different
comparison.

Run from the repository root:

    python3 repro/diagnostics/2026-11-05-optimized-right-center/diagnose_optimized_right_center.py

The driver refuses to overwrite its result and records the exact source
helper and its hash. Frozen proof and certificate files are unchanged.
