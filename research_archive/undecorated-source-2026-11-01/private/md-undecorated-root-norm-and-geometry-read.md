# Root check of the finite filling estimate and the geometric obstruction

The authoritative public baseline is bb6d98a0e523dc0ee622398c4d10d439ff9af57b. This record does not assert a new volume class.

## Finite functional

Starting from the exact midpoint identity in actual_spectral_total_derivative_source.md, write P(phi)=H(2 cos phi). Its trigonometric degree is d=N-1. The original filling chirp has unit modulus on the real interval and derivative bounded by |n|N/2, with the scalar q^(n d^2/4) retained.

The Riesz interpolation formula at the 2d odd half-grid points has coefficients (-1)^(r+1)/(4d sin^2((2r-1)pi/(4d))). A finite geometric sum verifies it on every mode from -d to d, including the opposite-sign alias at the two end modes. The sum of absolute coefficients is d, by differentiating the sine product. This proves the complex trigonometric Bernstein inequality without requiring real coefficients.

The three terms in the differentiated midpoint formula cost 1/N, d/N and |n|/2 in the original interval supremum norm. Their total is 1+|n|/2. If H vanishes at every original spectral node, the value terms vanish exactly, leaving at most d/N times the same norm. No spectral derivative of the chirp is left in this case.

For several variables, the original common-face coefficient is extracted first. The resulting polynomial has degree at most d in each spectral variable. Iterating the local linear functionals preserves that degree condition and the remaining node-vanishing conditions, so the product bounds apply to the same shared polynomial, without independently chosen local radii.

For the unsplit full-minus-CROSS remainder, vanishing on the whole node product grid kills the term using the value part of the functional in every coordinate. The derivative part costs d/N and the value part costs 1/N+|n|/2. This gives the product-difference upper bound in the focused proof. It is a polynomial upper bound in the absolute twist magnitudes, not an assertion that the invariant itself is polynomial in those magnitudes.

The paired-node residue coefficients were checked directly from the Chebyshev ODE: chi''(c)/2=N^2/(4-c^2), and chi'''(c)/(3chi''(c))=c/(4-c^2). For odd N the simple node -2 has derivative chi'(-2)=N^2. Thus the derivative/value decomposition has the exact stated normalization.

The earlier Fourier-Hermite Gram note already proves a level-uniform filling dual norm for a different positive packet energy. The new direct numerator-supremum estimate and the exact normal-order removal should be distinguished from that existing result.

## Geometry

For the bipyramid packing, the north/south contact inversions give the rim curvatures 4a(a-1)sin^2(j theta) and 4a(a+1)sin^2(j theta). The equatorial contact has |p|^2=a^2-1 and gives both apex curvatures 2, with neighboring rim curvatures 8cos^2(theta). This supplies the normalized quartets with two protected entries and positive ratio r=4cos^2(pi/m), for every legal edge mark and either matching offset.

The source normalization Q(1,r,0)=2 Ti_2(sqrt(r))/pi has derivative with respect to log r equal to arctan(sqrt(r))/pi and value zero at r=0. The inversion identity for Ti_2 gives the asserted balance difference. For r>=3, Ti_2(r^(-1/2))<1/sqrt(3), pi>3, sqrt(3)>5/3 and log 3>1 prove the strict upper bound -1/10.

The shared unconditioned envelope is coercive after fixing the common scale: its complete cost is bounded below by its recession function, whose zero directions force equality along every supported ordinary triangle. Connectivity of the ordinary graph leaves only the common scale. Therefore a failed complete balance condition forces the optimized unconditioned envelope strictly above the complete value. This does not apply to genuine conditioned sectors.

The m=6 figure was visually inspected. Its radii, line labels, transformed apex positions and selected curvature quartet agree with the algebra. The inverse-plane view identifies the actual matching contact; no metric claim is inferred from a schematic graph.

## Remaining proof requirement

No sharp universal bound for the original shared numerator or its non-CROSS remainder has been proved. A local node-value reduction is not an ordinary Hopf-intertwiner replacement. The one-sided polynomial projection does not commute with the full Casimir. An odd sign cycle gives inconsistency but not a sufficient quantitative volume gap. Removing a half-charge phase without changing the ordered physical boundary tuple is not permitted.

These results simplify and delimit the next analytic task. They do not change the published planar decoration theorem into an undecorated volume theorem.
