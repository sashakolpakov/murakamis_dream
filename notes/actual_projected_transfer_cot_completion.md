# Original output Fourier projection removes the colliding negative-transfer poles

28 October 2026. Keeping the original finite physical output projection
resolves the simultaneous endpoint collisions left by the scalar simple-seam
calculation. There is an exact matrix-valued total-transfer interpolant.
At EVERY newly crossed negative integer its projected operator has a zero,
including when its unprojected scalar coefficient has a pole. Consequently
the complete cotangent density is holomorphic across the whole negative
normal collar. Its operator norm and contour mass cost are exp(o(N)) on
any collar of width N^alpha, alpha<1, uniformly in ALL physical input basis states.

This is an actual full-source normal-boundary operation, not a favorable
scalar interpolation with its output tails deleted. The Fourier/sinc
factors are retained explicitly. It neither discards the original k=0
residue nor bounds an unrestricted bulk exterior by hyperbolic volume.

## 1. Literal physical Fourier projection and the interpolated crossing

Use the original balanced complete heads, N>=2, d=N-1,
Q=exp(2pi*i/N), x=-exp(-pi*i/N), with orthonormal basis |j>,0<=j<=d.
In L^2 of the unit circle use normalized measure dtheta/(2pi) and
the specified logarithmic lift 0<=theta<=2pi. The orthogonal projection
of exp(i nu theta) to the physical Fourier band is the ENTIRE vector

    v_N(nu)=sum_(j=0)^d s_j(nu)|j>,
    s_j(nu)=(exp(2pi*i*nu)-1)/(2pi*i*(nu-j)),             (1)

with its removable value one at nu=j. Thus v_N(j)=|j> inside the
physical band, and v_N(j)=0 at every other integer. At an invalid
integer its vector zero is at least simple. Orthogonality proves

    ||v_N(nu)||<=||exp(i nu theta)||_L2
                         <=exp(2pi |Im nu|).             (2)

No N-dependent conditioning or a nonpositive pivotal metric is used.

Let the scalar r_N(a,b;z), 0<=a,b<=d, be the EXACT factorial
interpolation of the original positive crossing:

    r_N(a,b;z)=kappa x^(-a-b+z)Q^(b(a-z))
               *Fhat(b+z)F_a/[Fhat(z)F_b Fhat(a-z)].     (3)

The normalizers, Gaussian, Cartan and completed factorial are those of
[the total-transfer theorem](actual_total_transfer_endpoint_packets.md).
Define the operator-valued continuation by its actual input columns,

    Rhat_N(z)|a,b>=r_N(a,b;z)
                           v_N(b+z) tensor v_N(a-z).    (4)

This is precisely the contraction of the two original output Fourier
projections with the scalar monomials of the physical crossing kernel.
It is not an arbitrary change of its output source. At an integer
0<=k<=d it equals the original kth transfer slice: valid outputs give
their literal basis vectors and forbidden transfers have their exact
factorial zeros. The opposite crossing uses its actual conjugate mirror.

Therefore the half-integer closed cotangent rectangle gives an OPERATOR
identity before applying any knot closure,

    R_plus=integral_Gamma pi cot(pi z) Rhat_N(z) dz/(2pi*i), (5)

where Gamma encloses precisely 0,...,d. The full original kappa is in
(3); all physical head projections and any external pivotal, framing,
peripheral or marked source are unchanged. Fubini on finite contours
applies (5) simultaneously to every crossing of a fixed signed word.

## 2. Exact cancellation at a simultaneous negative endpoint collision

Fix z=-s, with 1<=s<N. In this normal range Fhat has a simple pole
at each negative integer, and a simple zero at N,...,2N-2.
These orders follow directly from its convergent Gamma product or its
shift continuation. Put

    I_1=1 if b<s, otherwise 0,
    I_2=1 if a+s>=N, otherwise 0.

The scalar coefficient (3) has local order

    ord_(z=-s) r_N = 1-I_1-I_2.                         (6)

The first invalid output is b-s<0, and the second is a+s>d.
Formula (1) supplies a simple vector zero at EACH invalid output.
Thus the complete column in (4) has order at least

    (1-I_1-I_2)+I_1+I_2=1.                              (7)

In particular the double collision I_1=I_2=1 is not discarded: its
scalar pole is canceled by TWO actual physical projection zeros,
leaving another zero. This is exactly the source factor lost if one
studies the scalar factorial coefficient alone.

All scalar singularities in this collar lie at these integers.
Consequently Rhat is holomorphic on the negative collar and vanishes
at all its integers. Its complete density pi cot(pi z)Rhat_N(z) is
holomorphic there too. No derivative residue or logarithmic source
term has been omitted; the ENTIRE sinc vectors in (1) are retained
before taking the removable limits.

## 3. Uniform polynomial base bound at every physical input endpoint

Fix T>0 and let 0<=Re nu<=1, |Im nu|<=T. Uniformly in 0<=n<=d,

    |Fhat(n+nu)/F_n|<=C_T N^(C_T),
    |F_n/Fhat(n-nu)|<=C_T N^(C_T),
    |1/Fhat(nu)|<=C_T N.                               (8)

Here is a direct estimate, including the input endpoints. On the fixed
nu rectangle, its defining product gives Fhat(nu) bounded by C_T
N^(-Re nu), and its reciprocal by C_T N^(Re nu). For the first ratio
use the exact product

    Fhat(n+nu)/F_n=Fhat(nu)
             product_(j=1)^n (1-Q^(j+nu))/(1-Q^j).

Each ratio is at most 1+C_T/min(j,N-j); the sum of their logarithms
is O_T(log N). For the second ratio when n>=1, start at Fhat(1-nu)
and use factors j=2,...,n. Its ratios are bounded by
1+C_T/min(j-1,N-j), and |F_1/Fhat(1-nu)| is polynomially bounded.
For n=0 use 1/Fhat(-nu)=(1-Q^(1-nu))/Fhat(1-nu), which is regular
and satisfies the same bound. Thus (8) does not hide a large F_n
or its inverse at the physical endpoints.

Since the Cartan multiplier in (3) is bounded on this fixed-height
rectangle at physical a,b, (8) gives |r_N(a,b;nu)|<=C_T N^(C_T),
uniformly for ALL a,b. Together with (2), this is the required bounded
normal base for the actual projected operator.

## 4. A subexponential-cost compensated collar for the entire word

The same exact ratio used for the sourced Ward equation gives

    r_N(z+1)/r_N(z)
       =c(1-Q^(b+z+1))(1-Q^(a-z))/(1-Q^(z+1)),
    c=xQ^(-b).                                         (9)

Take the rectangle -s-1/2<=Re z<=-1/2, |Im z|<=T, with s<N/2.
On either half-integer vertical side or either nonzero-height
horizontal side, write z=nu-M, 0<=Re nu<=1. Inverting (9) M times
costs at most (C_T N^2)^M: each denominator 1-Q^(integer+nu) has
magnitude at least c_T/N there, while the numerator is bounded.
The distance from an integer is bounded below by min(1/2,T).
The base estimate (8) and (2) therefore give on this ENTIRE boundary

    ||pi cot(pi z)Rhat_N(z)||
                        <=N^(C_T)(C_T N^2)^(s+1).         (10)

The matrix operator norm costs only another factor N from its N^2
input columns. The cotangent is bounded on these edges. Its apparent
interior poles have already been removed in Section 2. The maximum
principle applied to every scalar matrix coefficient <u,Rhat v>,
or to this holomorphic complete density, extends (10) through the
interior with the same bound.

The added contour has length O_T(s+1). Moving the original left edge
from -1/2 to -s-1/2 and retaining BOTH finite-height connecting pieces
changes (5) by zero: all enclosed new poles are removable. Thus this
is an exact source-preserving collar move with quantitative operator
cost

    exp[O_T((s+1)log N)].                               (11)

For s<=N^alpha with any fixed alpha<1 this is exp(o(N)). The number
of crossings and physical heads of a fixed diagram does not grow
with N, so finitely many such original operator collar operations
have the same subexponential additional cost. Every original cup,
cap, pivot, phase and external line remains as prescribed.

For an artificial positive split k=R the adjacent contours have
opposite interface currents; moving them together retains the same
integer residues with opposite signs. Equations (5)--(11) address
the ACTUAL outer normal source as well, including the simultaneous
collisions which a scalar split had left uncontrolled.

## 5. Scope of the advance

This removes an artificial negative-transfer exit of normal width
N^alpha at the full finite physical source, with explicit tame cost.
The original integer residues 0,...,d remain enclosed. In particular
it does not contradict the full-rate low Markov packet: no original
residue has been declared zero or individually lower-rate.

The physical input labels in (4) are the original finite basis labels.
The bound is uniform over all of them, so it is an operator/source
statement rather than a selected fixed-clock phase claim. If those
input indices are themselves replaced by independent complex contour
variables, one must retain the corresponding input projections and
their joint sources; (7) is not an assertion for an arbitrary scalar
continuation with those physical projections removed.

Nothing here assigns a sharp geometric bound to an unrestricted
bulk exterior, a real radial cutoff face, or a transfer collar of
macroscopic width whose cost in (11) is no longer subexponential.
It does not identify every stationary branch of a split sinc density
with a knot representation: the entire physical projection must stay.
The theorem is a quantitative full-source normal-boundary filling,
not the global sublevel transport or volume conjecture.

[Audit](../experiments/audit_actual_projected_transfer_cot_completion.py): original physical integer transfer slices, all simultaneous negative endpoint pole cancellations, fixed-height projected density limits, and finite-source tests including both physical input endpoints. The literal positive test includes the original common Cartan factor kappa=q^((N-1)^2/2), with its inverse in the negative crossing. The same audit now checks the [upper extension](actual_projected_transfer_upper_collar.md), its exact N-shift and fractional base identity, all physical upper collision orders and the two-sided expanded cotangent residue sum.