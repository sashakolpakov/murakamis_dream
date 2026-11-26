# Review of the local tree-message argument

1 November 2026. This record concerns the private draft
md-all-circle-local-message-filling-criterion.md and the published
finite-source inputs at d8ff75be41f307c34867046445c530a6251ec5cf.
It is a reading record, not a replacement for those proofs.

## What was checked

The exact crossing trace in actual_main_meridian_direct_crossing_trace,
equations (10)--(17), applies to any even polynomial input after replacing
its displayed product of Newton factors by that input. Its derivation
uses Lagrange interpolation and residues, not positivity of the input.
The chirp is even. Thus the sine-weighted integrand remains odd when
the child messages are complex and even. The reflected Fourier terms
still have coefficient one at charge one. The moving endpoints and
zero mode remain endpoint currents.

The full kernel keeps all Newton indices. The complete spectral-jet
norm and its polynomial equivalence with the real polynomial sup norm
in actual_main_meridian_source_bounds, Section 1.1, justify the bound
on the complementary kernel. Each incidence has rate at most g(k/N)
for low indices and zero for high indices. Summing both incidences
gives the fixed single-edge gap from the published curvature proof.
The polynomial degree in the parent angle is at most N-1 because only
the outgoing edge kernel contains that angle.

The conditional kernel bound is stronger than the unconditional
two-angle bound. Near zero, the uniform complex edge-sum expansion
from the published curvature proof, Section 5, gives the phase
psi(t,u), including its actual additive constant. Its second derivative
differs from -1/(2pi) by at most 1/(100pi). Separate evenness removes
a linear term. Outside the small real interval the raw Newton product
bound absorbs both changes of normalization, each at most r^2.
The complementary kernel has a much larger fixed gap even after its
linear complex polynomial growth is included.

The complex child phases need not be real on real angles. The
inequality |h''+a0|<=a0/20 nevertheless gives
Re h(t+iy)<=-19a0 t^2/40+21a0 y^2/40 by bounding the remainder
in h(z)=-a0 z^2/2+remainder. No absent reality assumption is used.
Likewise, the saddle formula t=-i ell/(D-Q), with |Q|<=a/20,
gives the sign of its imaginary part because Re(D-Q)>0.
The charge derivative is exactly Re(-it)=Im t.

The Hessian of the outgoing critical value is the Schur complement
in equation (24) of the draft. The edge cross derivative is small
and the denominator has modulus at least 19|D|/20. This closes the
same curvature class independently of the number of children and
the depth.

On a smaller local disk, a uniform holomorphic relative O(1/N)
expansion gives a zero-free quotient for sufficiently large N and
an analytic logarithm. Its logarithm divided by N has O(1/N^2)
remainder after the leading amplitude. Cauchy's estimate supplies
the needed fixed derivatives. The saddle contours stay strictly
inside that smaller child disk; the parent disk does not shrink
with depth. Constants and starting N may depend on the fixed tree.

The Poisson strip argument uses the exact degree bound and a
subharmonic maximum principle. It gives linear imaginary growth
globally. The local quadratic bound and the far real decay are
then patched, so no unjustified global quadratic estimate for
individual high Newton polynomials is needed.

After the exact child values at zero are factored out, the absolute
tail and connector estimates are compared with the action drop
of the current vertex. The finite-charge saddles need only have
an additive error below the first-charge action; a relative expansion
at every higher-charge action is not required. The first-charge
amplitude is a product of nonzero edge amplitudes, child amplitudes,
a sine of a nonzero small saddle, and a nonzero Gaussian determinant.

The physical final trace still needs its original crossing and
framing scalars. These cancel in each normalized boundary-message
ratio; they cannot be omitted from the unnormalized invariant.
The reduced cut factor also occurs exactly once.

## Clarification requested

The proof of the global real outgoing envelope should be expressed
using the canonical polynomial norms and the quotient estimates
(D9)--(D11) of actual_main_meridian_source_bounds. For real parent u,
the kernel has a real t-sup bound with the desired parent decay.
Each normalized child has polynomial real sup norm. The crossing
power has polynomial canonical norm. Their product has degree a
fixed multiple of N, and the complete trace estimate is polynomial.
This proves the stated envelope directly, including repeated-root
normals, without a separate informal argument at colliding grid nodes.

The normalized amplitude may be independent of N at leading order,
while the omitted angular-independent physical scalar need not be.
The statement should make that convention explicit.

## Constants and geometry

The companion script md-audit-local-message-constants.py checks 21
strict numerical margins by exact rational arithmetic. Bounds used
are 3<pi<22/7, pi^2<10 and alpha>1/250. These checks cover constants
only, not the analytical induction or the knot invariant.

The geometric completion note explicitly states that it uses only
its path properties (3), not its previous summed sufficient
condition (4). The vertexwise contraction gives those path properties
on the same actual positive octahedral chart. The primitive periods
U+pV=-2pi i c, their initial logarithmic lifts, and the unchanged
original face identifications therefore give smooth primitive filling
at c=1. The complete volume anchor and the calibrated Schlaefli
identity identify 2pi Re C(1) with the original complement volume.

## Status of this reading

No mathematical obstruction has been found in the reviewed steps.
The source-norm clarification and the independent complete reading
remain to be incorporated before promotion to a public theorem.
