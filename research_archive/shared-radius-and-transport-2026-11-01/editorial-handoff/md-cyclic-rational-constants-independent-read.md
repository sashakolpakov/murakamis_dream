# Independent read of the rational cyclic constants

I read `md-cyclic-rational-constants.py` and its imported interval engine `verify_conway_two_leaf_block_alias_certificate.py`, then ran the script once to `md-cyclic-rational-constants-independent.json`. That output is byte-identical to the supplied JSON. The read concerns the fixed analytic inequalities, not the all-size incidence/trigonometric argument.

The interval arithmetic is enclosing. Endpoints have denominator 10^40; multiplication and division round each extreme outward, division rejects intervals containing zero, and all powers here have nonnegative integer exponent. The square-root bounds use the floor and ceiling of the appropriate integer square roots. Their rescaling gives lower/upper bounds for the square root of every input point.

The arctangent half-angle identity is applied to a positive enclosing interval until its upper endpoint is at most 1/2. Each iteration remains an enclosure even though dependencies are repeated. The 80-term alternating series then has absolute remainder at most the next term; multiplication by the recorded power of two restores the original angle. All uses of the result in Q explicitly check that the normalized angle lies strictly between 0 and 1/2.

The integral formula is

\[
 J(t)=t\log(2\pi t)-t-
 \sum_{n=1}^{20}\frac{\zeta(2n)t^{2n+1}}{n(2n+1)}+R(t),
 \qquad
 -\frac{2t^{43}}{21\cdot43(1-t^2)}\le R(t)\le0.
\]

It follows from the Euler sine product for 0<t<1/2. The tail estimate uses zeta(2n)<2 and n(2n+1)>=21*43 for n>=21, so its one-sided enclosure has the correct sign. Interval substitution preserves it. The imported zeta bounds are a positive finite sum through 64 plus its integral tail; zeta(2) uses the enclosed pi. The logarithm routine uses the positive atanh series with an upper geometric tail after scaling, and the Machin arctangent enclosure supplies pi.

Finally, `Q` uses precisely Lambda(pi*t)/pi=-J(t), twice, plus t log w. Its single-positive-coordinate branch is exactly one half-logarithm. Sorting the three rational weights uses the symmetry of Q; it does not assert a physical frame symmetry of the source.

All twelve lower comparisons and the distortion upper comparison are valid consequences of these enclosing intervals. The asserted positive boundary penalty is checked before its max branch is removed. The smallest displayed near net lower bound exceeds 0.08170, hence 7/100. No optimizer, floating value or sampled diagram size is used.

The only portability issue is the current absolute `ENGINE` path. Before publication it should resolve the repository engine relative to the script (or carry the same engine locally), and the imported engine should be included in the provenance hashes. This does not affect the current verification. No mathematical correction was found.
