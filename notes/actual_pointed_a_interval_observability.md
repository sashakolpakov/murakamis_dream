# Quantitative inward propagation for the actual pointed-A boundary response

28 October 2026. A uniformly off-characteristic color interval has a
controlled whole-line Green extension and an explicit finite-interval
observability estimate. Weighted energy entering from its retained
boundary packets decays exponentially inward. The constants remain
polynomial when the spectral gap shrinks slower than N^-1/2.

This upgrades [bulk Agmon coercivity](actual_pointed_a_bulk_agmon_energy.md)
to a resolvent and a maximum estimate for the actual fixed-band source
system. It accounts for nonnormality without diagonalizing transfers.
Both boundary packets remain in the general case. It is not a claim
that an arbitrary square finite compression has a tame inverse, or
that the required right-hand source packet is already bounded by volume.

## 1. Broad operator class and actual inputs

Let the block size r and shift radius d>=1 be fixed. On a lattice
interval J=[a,b] of length O(N), consider the ACTUAL weighted recurrence

    (L_N u)_j=sum_(i=-d)^d C_(i,N)(j) u_(j+i).         (1)

The forward-only case has zero coefficients for negative i. Assume
uniform boundedness of the coefficients, and that they are within
C/N of matrices A_(i,N)(j/N) having a uniform Lipschitz bound on J/N.
The functions A may depend on N. Suppose

    sigma_min(sum_i A_(i,N)(x) exp(i i theta))>=eta_N>0
                              for x in J/N, theta real. (2)

In exp(i i theta), the first i is sqrt(-1), the second the integer
shift index. The notation is solely the Fourier symbol of (1).
Require eta_N>=4C_0 N^-1/2, where C_0 depends on those uniform bounds
and on fixed r,d. Eventually strict inequality suffices.

These are independently checkable coefficient hypotheses. For the
actual pointed jet matrix, after its proved jet scaling and color
weight exp(N phi_N(x)), its symbol is

    A_B(x,exp(-phi_N'(x))exp(i theta)).

The hypotheses above follow from the actual finite monomial formula
whenever phi_N' and phi_N'' are uniformly bounded and this radius
has gap eta_N. No unknown period is used. All original jet components
and source rows remain. A shrinking radius tilt with a fixed smooth
profile is allowed; an unbounded derivative of that profile is not.

## 2. A controlled whole-line extension and inverse

Extend each coefficient sequence constantly beyond the two ends of
J. Equivalently clamp the symbol path at its endpoint values; the
actual coefficients keep their O(1/N) error there. This defines an
auxiliary operator L_ext on ell2(Z,C^r), agreeing with the actual
recurrence on J. The extension is part of the PROOF; it replaces
neither the original outside word nor its source.

The sqrt(N)-window Plancherel argument gives

    ||L_ext v|| >=(eta_N-C_0 N^-1/2)||v||
                                    >=eta_N||v||/2. (3)

The same proof applies to L_ext^dagger. Its coefficients are shifted
adjoints of those in (1), hence have the same slow variation, and its
frozen symbol is the adjoint of (2), with the same singular-value gap.
Thus its kernel is zero too. The range of L_ext is closed by (3) and
dense by the zero adjoint kernel. Therefore it is onto and

    G_N=L_ext^-1 exists, ||G_N||<=2/eta_N.             (4)

This is a two-sided, source-independent resolvent theorem, with no
assumption of normal matrices or distinct eigenvalues. The constants
do not grow with interval length. The proof uses full output rows;
it does not discard the leakage rows at an interval endpoint.

## 3. Exponential Green decay, proved by bounded conjugations

Put K_1=sum_i |i|sup_j||C_(i,N)(j)|| and K_1^+=max(1,K_1).
Choose

    mu_N=min(1/d, eta_N/(8K_1^+)).                    (5)

For a fixed source color k, multiply by the BOUNDED weights

    W_R(j)=exp(mu_N min(|j-k|,R)).

Their neighboring ratios differ from one by at most
exp(mu_N|i|)-1<=2mu_N|i|. Consequently

    ||W_R L_ext W_R^-1-L_ext||<=2mu_N K_1<=eta_N/4.

Neumann inversion using (4) bounds the conjugated inverse by 4/eta_N,
uniformly in R. Applying it to a block point source at k and then
letting R increase proves the explicit kernel bound

    ||(G_N)_(j,k)||<= (4/eta_N)exp(-mu_N|j-k|).        (6)

No unbounded conjugation or imported decay theorem is used. Block
sources and multiplicities are included in the operator norm.

## 4. Exact finite-interval boundary observability

Suppose u is the original response on J and satisfies (1)=f on all
rows whose stencil is inside J. Let J_in=[a+d,b-d]; retaining this
slightly smaller row set works for both shift orientations. Zero
extend u from J and call it u_J. Then exactly

    L_ext u_J=1_(J_in)f+B_left u_left+B_right u_right. (7)

The two u-side packets contain the first and last 2d physical color
blocks of J. The two B operators are simply the corresponding
boundary rows of L_ext; they are explicit, have fixed support and
uniformly bounded norm. Their row supports lie within distance d of
the respective endpoint. If J is shorter than 4d the analogous
finite-dimensional estimate uses all its blocks as boundary data.

Uniqueness of (4) gives an EXACT representation by applying G_N to
(7). In particular

    ||u_J||_2 <=C eta_N^-1
                   (||f_(J_in)||_2+||u_left||_2+||u_right||_2). (8)

More precisely, for any j in J, (6) gives

    ||u_j|| <=C eta_N^-1 [
       sum_(k in J_in) exp(-mu_N|j-k|)||f_k||
       +exp(-mu_N dist(j,left))||u_left||_2
       +exp(-mu_N dist(j,right))||u_right||_2 ].       (9)

The fixed-width ambiguity in dist is absorbed into C. Summing the
geometric series proves the uniform maximum/observability estimate

    sup_J||u_j|| <=C eta_N^-1(1+mu_N^-1)
                         (sup_(J_in)||f_j||+||u_left||+||u_right||). (10)

Thus a regular homogeneous bulk transmits only the retained boundary
packets, with exponential distance suppression. On a compact bulk
interval of the actual pointed jet system, its initial identity rows
lie outside J, so f is zero in (9); this is NOT a replacement by an
arbitrary homogeneous solution. Those initial rows remain original
boundary data. More general actual affine sources may lie inside a
regular interval; their full row and column weighting remains in f.
An initial identity row is not silently assigned the bulk symbol (2).

For eta_N=N^-gamma with 0<=gamma<1/2, the inverse and maximum
constants are polynomial and the decay length is O(N^gamma). Thus
the loss is exp(o(N)), even for a shrinking off-characteristic tilt.
This also applies to the full normal-jet blocks, not only their
constant-color projection. The latter can be selected afterwards.

## 5. Which boundary data are genuinely necessary

The general estimate needs BOTH sides. Spectral gap alone does not
make a recurrence stable in the forward direction. The elementary
scalar recurrence u_(j+1)=2u_j has a fixed unit-circle gap, yet left
data u_0=1 grow to 2^j. Its reciprocal recurrence demonstrates the
opposite direction. These examples concern the broad operator class,
not a proposed replacement knot state.

Nor does (4) prove a tame inverse for any chosen square compression.
For example I-2T has min_(|L|=1)|1-2L|=1, but the n-by-n upper
bidiagonal compression has inverse sum_(k=0)^(n-1)2^k T^k, of norm
at least 2^(n-1). It has dropped an output leakage row and imposed
the wrong boundary condition. The full-output estimate and (7)
retain precisely the boundary data which prevent that inference.

There is a genuine one-sided improvement under an EXTRA checkable
stability condition. Suppose the monic actual companion equals T(j/N)
up to O(1/N), with T uniformly bounded and Lipschitz, and has uniformly
rho(T(x))<=1-delta on the interval. Then its positive Lyapunov metric
sum_(k>=0)(T^dagger)^k T^k/(1-delta/2)^(2k) is uniformly bounded
and Lipschitz. Its neighboring metric changes are 1+O(1/N), so
for large N the actual transfer contracts by 1-c_delta. Variation
of constants gives a uniform one-sided bound from the full LEFT
initial packet and its actual sources. If the inverse companions
have that property, the analogous theorem uses the RIGHT packet.
Mixed stable/unstable spectra do not satisfy either premise.

For an actual geometric radius between spectral branches, mixed
spectra are the usual case. The missing incoming packet is then
genuine source data, not an error that the local gap controls.
The pointed initial rows, cyclic root matching and normal resonance
must determine it with a quantified bound. This is exactly the
boundary-response problem retained by the positive Schur reduction.

For the ACTUAL bounded-jet problem the initial fixed-color packet is
known polynomially, including all its retained jets. The far packet
is different: the ordinary-color theorem bounds only CONSTANT values
C_j(q_N), j<N, not their q-normal jets. Those jets, and the complete
coordinate itself, may carry exponential size. Replacing the full
right-hand packet in (8)--(10) by the ordinary-color bound would
therefore drop source data. Bounding it by an unknown multiple of
the target period would not close the estimate either. An actual
cyclic/Weyl or source-Schur certificate is needed there.

## 6. Consequence for a sharp volume estimate

The theorem gives controlled inward propagation on every certified
regular interval. It accounts for repeated roots away from the
chosen circle, nonnormal jet blocks and shrinking gaps. A regulator
primitive is a legitimate weight there only on a genuinely identified
peripheral branch. It must also retain its SOURCE anchor: normalizing
the small-color source changes the recovery factor to R(x)-R(0),
which may be as large as twice the knot volume.

It follows that a sharp Vol upper bound needs a quantified connection
of the actual endpoint/turning packets, with that source anchoring.
Equations (7)--(10) remove uncontrolled regular-interval amplification
from this question; they do not supply those remaining boundary
values or assume them equal to the desired invariant.

[Audit](../experiments/audit_actual_pointed_a_interval_observability.py):
actual full-source figure-eight intervals with full leakage rows,
explicit nonnormal Green kernels and the finite-compression caution.
The all-operator proof is (2)--(10); the finite checks do not assert
a new sharp knot class.
