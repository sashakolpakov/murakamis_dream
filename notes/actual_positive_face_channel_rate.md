# A common positive face radius gives the global channel maximum

30 October 2026. This is a
finite determinant/rate theorem for the original positive face polynomials.
The exact marked coefficient interface is proved separately. No
external filling-color packet or filled-knot equality is claimed here.

## 1. The original finite factors and one common radius

Use the matrices and scalar normalization in
[the exact positive circle](actual_complete_circle_positive_face_polynomial.md).
Put d=N-1, a in {0,...,floor(d/2)}, s=d-2a, and mu=a/N. Write

    D_a(x,b,y)=det[bI+(x/2)H_-+(y/2)H_+],
    P_s(x,y)=product_(j=a+1)^(d-a)(x-Q^j y),
    B_(N,a)(x,b,c,y)=beta_a^2 D_a(x,b,y)D_a(x,c,y)P_s(x,y).

The fixed multiplicity k_a is between1 and2 and does not change a
normalized logarithmic rate. The retained half-twist omega_a^epsilon
has modulus1 for an integer channel; it must still be kept in a channel
SUM. Each circle uses the SAME face radius for every shared face.

Set the two original marked face variables u,v to zero, and put all
other face radii in a fixed positive compact set. The actual simple
white-face sphere has no matching edge between u,v, because their
edge is the original MAIN cut. Consequently x,y are not both zero.
Each triangle has at least one positive radius. If one outer radius
vanishes, at least one of b,c is positive: otherwise three distinct
faces would be u or v. These are exactly the nondegenerate patterns
used below. The result also holds when all four radii are positive.

## 2. Uniform logarithmic determinant rate, including both endpoints

Let

    c(t)=cos(pi t),
    E_b(t)=x+y+2b c(t)^2
                +2c(t)sqrt[b^2 c(t)^2+b(x+y)+xy],
    lambda_b(t)=E_b(t)/(4c(t)^2).

Then, uniformly over ALL integer a and the stated positive compact
sets with their fixed zero pattern,

    (1/N)log D_a(x,b,y)
        = integral_0^mu log lambda_b(t) dt + o(1).       (1)

All logarithms in (1) are real. Here is a direct finite-matrix proof.
Away from t=0,1/2, the actual diagonal and squared adjacent modulus
converge uniformly, with error O(N^-1), to

    A_b(t)=b+(x+y)/(2c(t)^2),
    B_b(t)=[(x+y)^2-4xy c(t)^2]/(16c(t)^4).

Thus lambda_b=(A_b+sqrt(A_b^2-4B_b))/2. No matrix of virtual
size beyond the maximal folded channel is introduced.

If b>0, every principal matrix is bounded below by bI. If x,y>0,
the exact [sum gap](actual_q_hahn_positive_total_boundary_normals.md)
H_-+H_+>=cos(pi/N)I gives the same uniform positive lower bound.
On an interior index interval the matrices also have a uniform upper
bound. Partition that interval into blocks of length ell tending to
infinity with ell/N tending to zero. Removing each connecting adjacent
entry is a rank-two perturbation. Both the original matrix and its
block diagonal pinching lie between the same positive lower bound and
a fixed upper bound. Eigenvalue interlacing, or integration of log det
along this positive interpolation, bounds the log-determinant change
by a constant times the number of removed edges.

Within a block, freezing the coefficients changes operator norm by
O(ell/N); the positive lower bound makes its log-determinant change
O(ell^2/N). After a diagonal unitary gauge the frozen block is the
real constant Jacobi matrix. Its eigenvalues are
A_b+2sqrt(B_b)cos(j*pi/(ell+1)). Their logarithmic Riemann sum is

    (1/pi)integral_0^pi log(A_b+2sqrt(B_b)cos theta)dtheta
      =log[(A_b+sqrt(A_b^2-4B_b))/2].

For the last identity, factor the expression as
lambda_b |1+sqrt(B_b)/lambda_b * exp(i theta)|^2; the second
logarithm has mean zero by its convergent Fourier expansion. The
positive spectral gap keeps the ratio below1 uniformly on this
interior interval. The total block error is O(N/ell+ell), hence o(N).
The same estimates allow a last shorter block, uniformly in a.

For completeness the endpoint truncations are uniform, not a fixed-a
argument. At either cut index a removed connecting edge has bounded
size depending only on the chosen endpoint cutoff epsilon, and its
rank-two cost is O_epsilon(1). A terminal block has a positive constant
lower spectral bound and the Hadamard upper bound from the ACTUAL
diagonal. Its log determinant is bounded in absolute value by

    C epsilon N(1+|log epsilon|)+O(log N)

at the fold, and C epsilon N+O(1) at zero. Indeed the diagonal is
at most C/[cos(n*pi/N)cos((n+1)*pi/N)]; summing its logarithm gives
the displayed integrable endpoint bound through both parities. The
limiting log lambda has the same integrable majorant. First let N
increase, then let epsilon decrease. This proves uniform (1).

The only remaining allowed case is b=0 and exactly one of x,y positive.
Here D_a is a scalar multiple of det H_+ or det H_-, and the ACTUAL
Cholesky pivots are

    p_(n-1)=sin(n*pi/N)/[cos(n*pi/N)sin((2n-1)*pi/N)].

Their exact product proves (1) directly by the same endpoint-truncated
Riemann sums; its bulk ratio is x/(4cos(pi t)^2) or its y counterpart.
This avoids using a positive spectral gap in this single-summand case.
The empty determinant at a=0 is included.

## 3. The circle rate increases strictly to the fold

Define

    I(v)=integral_0^v log(2sin(pi t))dt,
    J_mu(x,y)=integral_mu^(1-mu) log|x-exp(2pi i t)y|dt.

The exact sine products, with their integrable endpoint logarithms,
give uniformly in a

    (1/N)log beta_a = I(2mu)-2I(mu)+o(1),
    (1/N)log P_s(x,y) = J_mu(x,y)+o(1).                (2)

When x=y the second integrand has endpoint logarithmic singularities;
the elementary sine-product comparison gives the same uniform o(1).
If one outer radius is zero, the assertion is immediate from the
single monomial. The positive coefficient identity fixes P_s>0.

Combine (1),(2) to obtain the continuous uniform circle rate

    F_mu=2I(2mu)-4I(mu)
       +integral_0^mu [log lambda_b(t)+log lambda_c(t)]dt
       +J_mu(x,y).                                    (3)

For 0<mu<1/2, put

    D_xy(mu)=(x-y)^2+4xy sin(pi mu)^2.

Direct differentiation, retaining the scalar beta and forced product,
gives the cancellation

    partial_mu F_mu = log[E_b(mu)E_c(mu)/D_xy(mu)] >0. (4)

Indeed the scalar derivative is4log(2cos(pi mu)), while the two
determinant denominators multiply to16cos(pi mu)^4. The derivative
of J is minus log D_xy. If xy>0, then E_b,E_c>=x+y and
D_xy<(x+y)^2. If exactly one outer radius vanishes, at least one of
b,c is positive, making at least one E strictly larger than x+y.
Thus strictness holds in every actual pattern. Formula (3) is
continuous at both endpoints even when the derivative at zero diverges.

There is therefore a strict diagram-dependent gap on every region
mu<=1/2-epsilon. For a fixed graph, multiplying the original factors
at their shared radii and summing any polynomial number of channel
choices preserves that exponential gap whenever at least one channel
stays epsilon away from the fold. This upper estimate is at one common
radius; it does not sum incompatible independent local optimizers.

Near the fold (4) also gives the explicit classical quadratic gap.
Write A=x+y>0 and

    T_b=sqrt[bA+xy], T_c=sqrt[cA+xy].

At mu=1/2-delta,

    partial_mu F_mu = 2pi delta(T_b+T_c)/A+O(delta^2),
    F_(1/2)-F_(1/2-delta)
           = pi(T_b+T_c)delta^2/A+O(delta^3).          (5)

The coefficient is strictly positive in the actual patterns. This is
a statement about the limiting action. Uniform finite relative
asymptotics on delta of order N^-1/2, and cancellation of the retained
half-twist phases in the whole channel sum, require a further proof;
the o(1) in (1)--(3) is NOT used as such a relative estimate.

## 4. Scope of the whole-source upper bound

The [exact marked coefficient theorem](actual_original_marked_face_coefficient.md)
makes every coefficient nonnegative before the explicit half-twist scalar. Evaluating its
polynomial at the SAME positive radius bounds the selected coefficient
by that value divided by its prescribed radius monomial. Equations
(1)--(4) then control the entire finite channel sum from above, with
all original scalar factors and only polynomial counting cost.

The absolute endpoint value is computed separately from the actual
facet coning and marked source normalization. A positive central
coefficient with that value supplies a lower bound for an UNTWISTED
channel sum, as assembled in the
[complete untwisted theorem](general_untwisted_augmented_source_volume.md).
Signed half twists require a noncancellation theorem.
External crossing-circle colors needed for long Dehn fillings are
not the internal a labels in this note and are not estimated here.

Focused audit: [original finite channel factors](../experiments/audit_actual_positive_face_channel_rate.py), with [saved results](../experiments/actual_positive_face_channel_rate_results.json). It checks six symbolic identities, 704 all-label circles, 1408 original determinants, 528 independent Newton comparisons, 176 exact LDL products and 576 adjacent-channel ratios, including 64 maximal folds of each parity. The 72 rate samples are diagnostics only.

No finite-window signed Gaussian or external-color theorem follows from the channel-rate estimate.