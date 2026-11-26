# Independent read of the cap Dirichlet restoration argument

Scope: a read of `md-cap-dirichlet-restoration-response-region.md`, sections
1--7, against the original cap coordinates, triangle pressure, and the
finite stable-polynomial formulas. This is a proof-level read, not a
reconstruction of the actual matched sphere or a new filling theorem.
No code was run for this review, and no public source was edited.

The restoration normalization is correct. For the literal coupon
\((C,0,A,0)\), the omitted triangles contribute
\(\tfrac12\log C+Q(C,A,0)\). Grounding \(C=1\) and retaining the original
\(A\) target gives exactly \(\inf_z[F(z)+q(z)-z]\). In particular the
singleton triangle is not replaced by a second two-supported triangle.
The identities \(q'=\pi^{-1}\arctan(e^{z/2})\) and
\(q(z)-z/2=q(-z)\) have the correct factors.

Strict exterior feasibility and connected support justify the positive
minimizer for each finite tilt. Differentiating its stationary equations
gives a harmonic voltage with boundary values zero and one. The maximum
principle therefore bounds every interior log-weight derivative between
zero and one. Both \(ab/(a+b)\) and
\(\sqrt{ab+ac+bc}\) are coordinatewise monotone and homogeneous of
degree one. Their individual scale ratios lie in \([1,e^s]\), giving
the claimed conductance ratio in \([e^{-s},e^s]\). Minimization over
the same grounded voltage space preserves both sides. No statement that
the tilted weights themselves are a new complete packing is used.

The integration in equations (11), (13), and (21) is correct. Under
\(0<\nu\le1/2\) and \(\nu+\kappa\ge1/2\), the complete minimizer lies
at positive tilt; the action lower bound is consequently sufficient at
the actual minimum. The strict comparison
\(\kappa<\mathscr L(\nu,\kappa)\) uses the original odd stable
response bound \(\kappa\le\nu(1-\nu)\). On the half-load interval,
the endpoint integral is
\(a+(k-a)\log(1-a/k)\), including its continuous limit at \(a=k\).
Compactness yields a uniform margin; a point where \(k=1/4\) has
logarithmic rate minus infinity and causes no loss of upper
semicontinuity.

The weak-balance implication in section 5 is valid within the stated
interior-cap range. Its endpoint comparison at \(e^{z_*}=5/2\) has the
correct direction. The elementary root inequality is obtained from a
concave quadratic in the original root parameter, and its positive-tilt
average converges to the same exterior response. The conclusion should
continue to say explicitly “within \(0<\nu\le1/2\).” The proof does
not cover \(\nu>1/2\). Exchanging \(A,C\) is not an automatic repair,
because the omitted singleton triangle distinguishes these two faces.

The exact tilted squared-factor formula in section 6 retains the factor
\(P_N(e^z,1)\); all three endpoint squares are correct. It is distinct
from the weighted half-load expression of section 4. Taking an infimum
over fixed real tilts is legitimate after proving the corresponding
upper bound at each fixed tilt. The abstract example in section 7
correctly disproves a conclusion based only on arbitrary stable binary
polynomials and the formal restoration expression; it is not presented
as a matched-sphere counterexample.

One literal TeX correction is needed in equation (21): `k,qquad` should
be `k,\qquad`. No other mathematical correction was found in this
bounded read. The source consequence remains the original odd singleton
at the stated fixed spectra unless a separate finite spectral theorem
is supplied.
