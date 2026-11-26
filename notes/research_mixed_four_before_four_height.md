# A type-four right leg followed by type four

Research geometric bound, 4 November 2026. The right leg at a vertex is
denoted by \(t_j\), and its type indicator by \(\epsilon_j\in\{0,1\}\).
The original critical point and all logarithmic lifts are those of the
[universal localization theorem](research_mixed_cyclic_critical_localization.md).

**Theorem 1.** In every finite cyclic word in types three and four,
if \(\epsilon_j=\epsilon_{j+1}=1\), then
\[
             -.057<\Im t_j<-.048.                         \tag{1}
\]
The bound concerns the first of the two consecutive type-four vertices.
It is a geometric enclosure, without a finite-source or contour estimate.

The previously proved actual right-leg rectangles are
\[
 R_3=[.30,.39]+i[-.03,.02],\qquad
 R_4=[.27,.33]+i[-.057,-.02].                              \tag{2}
\]
They are strict compact subsets of the external disks in the
[open-window existence theorem](research_mixed_cyclic_critical_height_bounds.md),
Lemma 2. That theorem supplies the unique original holomorphic root on
a neighborhood of every full product of typed external disks. This
existence statement precedes the boundary reduction below.

Take a five-vertex window with zero-based type word
\[
                    (a,b,1,1,c),\qquad a,b,c\in\{0,1\}.
                                                               \tag{3}
\]
Its middle right leg is the second output of the original ten-variable
window Newton primitive, namely coordinate 5 in the order
\((s_0,t_0,s_1,t_1,s_2,t_2,s_3,t_3,s_4,t_4)\).
For each of the eight words (3), allow both external types independently
and all sixteen products of rectangle sides. There are exactly
\(8\cdot4\cdot16=512\) two-real-parameter products.

On each product the checker verifies a rational dyadic cover using the
unchanged original-logarithm affine Newton primitive. Every accepted cell
has a positive weighted disk self-map in the original common chamber,
and its whole enclosed middle right leg satisfies
\[
                  \Im t_2<-6/125.                         \tag{4}
\]
The external edge parameters are reconstructed exactly from the binary
address. Consecutive bisections alternate between the two parameters.
Prefix freedom and total dyadic mass one verify the complete product.
Neither displayed decimal hulls nor a sampled extremum are acceptance
criteria. The complete cover has 4,745 accepted cells and 8,978 visits.
The independent mode rechecks every saved cell using the
separately established sine/logarithm and cotangent window primitive;
it does not import the author Newton formulas.

For a fixed word and external types, \(\Im t_2\) is harmonic in each
external complex parameter. Two maximum principles extend (4) from the
distinguished boundary to the full rectangle product. No actual-cycle
lower bound is used to clip an auxiliary open-window image.

At an actual cyclic critical point, its external legs belong to (2).
Restricting the cyclic solution to the window solves the identical
original equations. Global uniqueness identifies it with the window
root just enclosed. If the cyclic length is smaller than five, repeat
the period before extracting the window; repeated incidences retain
their original equations. The upper bound in (1) follows. Its lower
bound is the existing actual type-four height bound, applied only after
this identification.

This argument neither controls source contours with target heights
depending on these references nor asserts a global bound for the
original period.

Reproduction:

```sh
python3 experiments/certify_mixed_four_before_four_height.py --precision 256
python3 experiments/certify_mixed_four_before_four_height.py --precision 320 --independent --input repro/results/research-mixed-four-before-four-height.json
```
