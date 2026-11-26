# The middle right leg of three consecutive type-four vertices

Research geometric corollary, 4 November 2026.

**Corollary 1.** At the original critical point of every finite cyclic
three/four word, if positions \(j-1,j,j+1\) all have type four, then
\[
                       -.057<\Im t_j<-.053.                 \tag{1}
\]
Here \(t_j\) is the right leg of the middle vertex.

Use the five-window proof of
[the four-before-four theorem](research_mixed_four_before_four_height.md),
retaining only the words
\[
                     (a,1,1,1,c),\qquad a,c\in\{0,1\}.       \tag{2}
\]
There are four such words, four independent external type pairs and
sixteen products of external rectangle sides. The resulting 256
products are a subset of the earlier complete cover.

The checker reconstructs every saved dyadic cell in that subset and
evaluates the independently established sine/logarithm and cotangent
window self-map at higher precision. It requires the entire middle
right-leg enclosure to satisfy \(\Im t_2<-53/1000\).
Stored decimal extrema are not used for acceptance. Exact prefix and
dyadic-mass checks retain the full distinguished boundary.

Whole-product holomorphy was established before either cover. Two
harmonic maximum principles therefore extend the stronger upper bound
to the full typed external rectangles. Restricting an actual cyclic
solution to the five-window equations and using their uniqueness
identifies its middle right leg with this branch. Repeating a short
cyclic period preserves all original equations, so there is no minimum
cycle length. The lower bound in (1) is the already proved actual
type-four lower bound.

Only the geometric enclosure is asserted. In particular, it does not
supply a finite-source estimate or a contour comparison for target
heights coupled to these reference heights.

Reproduction:

    python3 experiments/check_mixed_three_consecutive_four_height.py --precision 320
