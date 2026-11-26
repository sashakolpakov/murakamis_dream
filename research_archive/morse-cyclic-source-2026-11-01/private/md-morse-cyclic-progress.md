# The geometric term on general planar diagrams, and the remaining signed estimate

The geometric part of the long-filling argument now applies to the original diagram associated with a simple triangulated sphere and a chosen perfect matching of its dual. No terminal tangles need to be added for this part of the proof. The result concerns a specified summand of the exact finite evaluation. It does not yet identify that summand with the whole knot invariant.

Fix the sphere, matching, cyclic orders, strand mark, and crossing-disk framings. Choose the retained half twists and require the resulting strand pairing to form a knot. If the signed crossing powers are independently sufficiently long and then held fixed, the contribution obtained by choosing the central crossing part of every local polynomial satisfies

\[
 \lim_{N\to\infty}\frac{2\pi}{N}
       \log|I_{N,\mathrm C}|=
       \operatorname{Vol}(S^3\setminus K).
\]

Here the central crossing part is denoted CROSS in the earlier formulas. It is a linear decomposition of the original finite source, with its original face-degree constraints. It has not been defined as a separate topological invariant. The limiting volume is the volume of the complement obtained by filling the original auxiliary crossing circles; the knot cusp remains unfilled.

## Why the extension works

The exact coefficient formula already holds when cups and caps occur between crossing regions. The new analytic argument checks that the hypotheses for a nonzero geometric contribution also hold in this setting. Deleting the two protected adjacent vertices from a simple triangulated sphere leaves a connected ordinary-face graph. This gives a nondegenerate face Hessian after removing common scale, and primitive phase differences exclude additional angular maxima. Every matching factor contains a nonmonomial triangle, which gives a strict spectral loss away from the complete point.

The whole Fourier sum is then controlled, not merely its first local critical point. The proof retains the currents on the sides of the shifted contours, treats the large Fourier indices on the entire original intervals, and compares the remaining critical values before taking the limit. Two different fixed cubes are required: an outer cube for the local critical points and a smaller inner cube for the bounded indices outside that local regime. This distinction is explicit in the final proof. The original repeated-root derivatives, odd-level endpoint, and framing scalar remain present.

The geometric argument constructs one marked deformed circle pattern on the entire sphere. Ordered reflection products give the original main meridians and the primitive auxiliary peripheral words, also through cups and caps. The source action and marked regulator have the same differential after the stated boundary correction. Their constants agree at the complete augmented structure. At the first-charge critical point the filling equation cancels that boundary correction. A separate metric completion argument proves that the representation is the smooth hyperbolic filling of the specified topology. Thus the right side above is an actual hyperbolic knot-complement volume, rather than the value of an unidentified representation.

The two complete arguments are in `md-morse-cross-analytic-packet-and-whole-period.md` and `md-morse-cross-source-geometry-and-filling.md`. Their hypotheses allow a fixed sphere of arbitrary size, separating triangles, either sign of each long power, and arbitrarily unequal fixed powers. They do not allow the diagram or powers to grow with the quantum level.

## What still prevents the full volume theorem

Write the original shared spectral polynomial as

\[
 S_N=S_{N,\mathrm C}+D_N.
\]

For an undecorated diagram outside the existing comparison criteria, the remaining problem is to control the signed polynomial \(D_N\). One sufficient statement is

\[
 \sup_{\boldsymbol\sigma\in[-2,2]^r}|D_N(\boldsymbol\sigma)|
 \le \exp\{N(\Phi_D-\eta)+o(N)\},
 \qquad \eta>0,
 \qquad \Phi_D=\frac{\operatorname{Vol}(Y_D)}{2\pi}.
\]

The polynomial does not depend on the twist powers. The published finite filling bound transfers this strict gap to every fixed tuple of twists without an exponential cost. The geometric filled rate approaches \(\Phi_D\) as all powers become long. A strict gap would therefore make the complementary term smaller than the nonzero geometric contribution and prove the full invariant limit. A bound at the augmented rate with no gap would not establish the smaller filled rate.

This is still a substantial multivariable cancellation estimate. It is not an omitted normalization, a numerical check, or a choice of terminology. The existing decorated planar and covered Conway theorems already have the required comparison and do not depend on solving this new undecorated problem.

## Two exact results about the remaining sum

At the spectral endpoint \(+2\), each monomial coefficient of the original local resolvent face polynomial has absolute value at most \(2N^3\). The proof uses a positive quadratic energy for its signed three-term recurrence and an exact bound for the unused-row product. The same argument gives \(2N^4\) uniformly on the shrinking interval \([2\cos(\pi/N),2]\). Consequently the full shared sum, its central crossing part, and their difference are polynomially bounded on the corresponding shrinking cube, for every fixed diagram. This is an all-level statement; it does not give the supremum estimate on the fixed cube above.

The actual adjacent north and south boxes of an opposite-offset bipyramid also satisfy an exact finite Green identity. It retains the exterior face demands, the common south-face degree, four interior bands, and both endpoint currents. The interior contribution does not automatically vanish when the other boxes are attached. At level three, the six-box source with ordered spectral tuple \((2,0,2,2,2,2)\) gives the nonzero interior contribution \(-2051892\) by exact integer coefficient extraction. This rules out a proposed cancellation identity, not the desired exponential estimate.

The associated face-operator factorization and root difference rule explain why the missing terms matter: moving a difference operator through a shared product shifts the other factors as well. Those shifted terms must be estimated or combined using their actual identities. Dropping them does not preserve the original finite evaluation.

Finite evaluations through level 32 have also been retained as diagnostics. They use the full signed coefficients and common face targets, with separate precision comparisons and exact low-level checks. They are not proofs of a uniform gap or a volume limit.

An odd-level support identity makes the complementary polynomial vanish when only the protected position departs from the spectral value \(-2\). It does not extend to an arbitrary position. At \(N=3\) in the six-box example, changing position three alone gives exactly \(2\cdot9^5(\sigma-1)(\sigma+2)\). Its first derivative at \(-2\) is nonzero. Thus a single repeated-root derivative can survive in the original closed source. The exact two-monomial calculation and its reproduction script are preserved alongside the support proof.

## What changed relative to the previous state

The previous handoff left two separate obligations for the unchanged bipyramid: applicability of the nonzero geometric filling theorem, and a strict estimate for the complementary sum. The applicability and actual-volume argument are now written for the general matched simple sphere. The strict complementary estimate remains open. No additional full-invariant knot family is claimed in this continuation.
