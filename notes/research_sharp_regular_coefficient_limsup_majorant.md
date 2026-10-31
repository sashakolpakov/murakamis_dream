# The original sharp interval functional is a uniform regular coefficient majorant

Unpublished workspace analytical theorem, 31 October 2026. Root and coherent
completed full internal analytical reviews. This is not external peer
review. This is an UPPER bound only.
It needs no every-level coefficient limit, nonzero prefactor, or selected
Fourier cycle. This historical theorem has the compact regular scope
stated below. Its boundary-uniform extension is now proved separately in
the [global closed-domain upper theorem](research_global_sharp_coefficient_limsup_majorant.md).
The proof and regular conclusions here retain their original scope;
that later extension does not assert a coefficient lower limit or boundary
maximizer regularity.

## 1. One exact coefficient, on the original full row range

Put d=N-1 and retain the original alpha_r=c_r-sigma and s_r=2sin(pi r/N).
For ANY 0<=i<=j<=d, r=j-i and 0<=k<=r, the coefficient of
x^k b^i c^(d-j)y^(r-k) in the full homogeneous numerator is, up to its
recorded common unit sign,

    a_N=(prod_(a<i) alpha_a)(prod_(a>j) alpha_a)
                          [x^k y^(r-k)] K_(i,j).       (1)

This is the exact original start/end expansion, not a decomposition
through separately signed central cofactors. In particular it covers
CROSS directly and includes the odd central visited/skipped paths in
the same K. Its total degree is exactly d. If j is in the lower half,
the second outside product includes the original A_rest factor;
equivalently retain A_rest separately and the unused lower suffix.
No division by A_rest or by a sampled alpha is made.

The normalized K has the positive eta-word expansion whenever
lambda_N=cos(pi/N)+cos(2pi delta)>=0. On any fixed real spectral
compact 0<=delta<=delta_max<1/2 this holds for all sufficiently large N.
The word proof applies on the ENTIRE range i+2<=a<=j<=d:
cos(pi/N)-cos((2a-1)pi/N)>0 there, and s_a,s_(a-1)>0.
Thus its coefficients are nonnegative even across the central row.

For every finite real tilt l, Cauchy's elementary coefficient bound is

    [x^k y^(r-k)]K <= exp(-k l) K_(i,j)(exp(l),1). (2)

All signs of the original outside products remain outside K. A zero
sampled factor makes a_N zero and automatically satisfies every upper
bound below. Both parities are treated by (1); there is no odd bare-
endpoint reference substituted for an actual coefficient.

## 2. Uniform weighted tails and outside products

Write mu=i/N, nu=j/N, xi=k/N. On positive compact tilt sets the existing
fixed-block transfer proof gives, uniformly in all interval endpoints,

    N^(-1)log K_(i,j)(exp(l),1)
      <=int_mu^nu log Lambda_delta(t;exp(l),1)dt+o(1). (3)

For clarity the same proof genuinely covers full intervals, not just
ones ending at1/2. After dividing K by prod s_a, its two-by-two transfer
has bounded entries on [0,1] and limiting spectral radius

    rho=A sin(pi t)+sqrt((x-y)^2 sin^2(pi t)+4xy cos^2(pi delta)).

On [eta,1-eta] this is uniformly positive. Cayley--Hamilton bounds each
fixed block by C(k+1)rho^k without an eigenbasis inverse; freezing a fixed
large block and then letting N grow proves its integral upper bound.
The endpoint intervals of length eta cost O(eta N), and their missing
logarithmic integral costs O(eta log(1/eta)N). Restore prod s_a and send
eta to0. This proves (3) with Lambda=2sin(pi t)rho. It also covers
an exact protected start i=0 or stop j=d when such a chart is retained.

The original outside products satisfy uniformly

    N^(-1)log |prod_(a<i)alpha_a prod_(a>j)alpha_a|
      <=int_0^mu log|alpha_delta(t)|dt
            +int_nu^1 log|alpha_delta(t)|dt+o(1).       (4)

Truncate log from below before the Riemann sum. The truncated function
is jointly continuous; the translated cosine-log factors have uniformly
integrable singularities. Their truncation errors tend uniformly to0.
This proves an UPPER sum estimate even at arbitrarily close sampled
zeros. A finite sum's value -infinity at an exact zero is harmless.
For a lower-half presentation the exact A_rest has |A_rest|<=poly(N),
including its zeros, and int_(1/2)^1 log|alpha_delta|=0. Thus (4) agrees
with the retained omitted-half normalization, rather than deleting it.

Combining (1)--(4), uniformly for l in a fixed compact interval, gives

    N^(-1)log|a_N| <= B_delta^full(mu,nu)
        +int_mu^nu log Lambda_delta(t;exp(l),1)dt-xi l+o(1), (5)

where B^full denotes the two displayed outside integrals. The o(1)
depends on the compact chart, not on the integer rows or spectral nodes.

## 3. Taking the actual finite Cauchy tilt

Consider any compact regular chart with nu-mu>=w_*>0,
xi/(nu-mu) in [epsilon,1-epsilon], and delta<=delta_max<1/2.
Rows may be required a fixed distance from the endpoints for ordinary
charts; fixed protected i=0 or j=d is also allowed. The continuum tilt
minimizing the right side of (5) is unique and ranges over a FIXED
compact real interval.

Indeed the logarithmic root has the strictly positive second l derivative
printed in the stationary reduction. Its first derivative lies in(0,1)
and tends to0 and1 as l tends to negative and positive infinity.
These limits are uniform on t in [eta,1-eta] and on the spectral compact.
The omitted endpoint intervals have arbitrarily small length and the
derivative is bounded by1 there. This proves uniform convergence of
the integrated first derivative to0 and nu-mu and bounds the minimizing
tilt. Strict positivity on an interior subinterval gives uniqueness.

We may therefore choose THAT finite tilt in (5), with the SAME uniform
error. Define

    H_delta(mu,nu,xi)=B_delta^full(mu,nu)
           +inf_l[int_mu^nu log Lambda_delta(t;exp(l),1)dt-xi l]. (6)

Then on every such compact regular chart, at BOTH parities,

    limsup_(N->infinity) sup_chart
       [N^(-1)log|a_N|-H_delta(mu,nu,xi)] <=0.       (7)

This is exactly the required uniform coefficient LIMSUP majorant.
There is no lower asymptotic and no exclusion of A_rest zeros.

If an outer face is protected, specialize the exact monomer first:
K=x^r prod_(i<a<=j)s_a^2 or its y version. Its coefficient has the
same upper formula with the corresponding closed outer-degree entropy,
by the ordinary sine-log Riemann bound. No finite tilt of a zero
outer weight is used. These fixed protected strata may be included;
uniform approach through arbitrary additional vanishing ordinary
loads is a separate assertion, not needed for (7).

## 4. LEFT and CROSS are precisely the reviewed sharp functionals

For a LEFT interval nu<1/2, the identity
int_(1/2)^1 log|alpha_delta|=0 makes (6) exactly h_delta in the
stationary reduction, including both unused lower intervals.
RIGHT is the actual reflected interval.

For CROSS put tau=1-nu. Both alpha and Lambda are symmetric under
t->1-t. Write B_a=int_0^a log|alpha_delta(t)|dt; then (6) is

    B_mu+B_tau+inf_l[Phi_(mu,1/2)(l)+Phi_(tau,1/2)(l)-xi l]. (8)

This equals the MAXIMUM of the two half-cofactor Legendre entropies
over the original outer split xi_1+xi_2=xi. One can prove this without
any joint row concavity: each half entropy is bounded above by its
weighted value at the common tilt, so their sum is at most (8).
At the minimizing common tilt set xi_a=Phi_a'(l); then both half
Legendre infima attain this tilt and equality follows. On regular
charts these are strict positive splits; limiting splits require
their separately stated boundary interpretation.

Thus the latent CROSS split functional used in the stationary audit
is a valid coefficient UPPER majorant. We never estimate a positive
cofactor and then subtract a signed central correction: the original
single K_(i,j) in (1) handles that correction before any bound.

The physical degrees divided by d, rather than N, satisfy the original
unit targets exactly. Their row/outer parameters differ by O(1/N).
On the compact regular charts H and its split versions are uniformly
continuous (including spectral delta=0 away from row/pole collisions),
so this changes (7) by o(1). The upper reflected start is
(d-j)/N rather than 1-j/N; its one-row difference is treated the same
way. No finite support endpoint or protected target is reset.

## 5. The literal shared coefficient

Fix the original diagram with finitely many ports. Restrict its degree
sum to any product of the compact regular charts above, imposing the
ONE original ordinary target d and the two protected targets0.
There are at most (d+1)^(4R) incidence arrays. Apply (7) to each local
coefficient, multiply, and use the triangle inequality on the actual
coefficient sum. It is bounded by

    exp{N[sup_(original feasible flows in the charts)
                        sum_e H_delta,e+o(1)]}.        (9)

The logarithm of the number of arrays is o(N) for fixed diagram.
The same bound with the limiting closed feasible flow set follows
by compactness and continuity; no lattice LOWER approximation is
needed. For CROSS use its equal split representation (8).

Each Cauchy tilt was allowed to depend on the LOCAL coefficient being
bounded. This is legitimate before the original shared extraction;
it is not replacing the original face constraints by independent
weighted source maxima. Common face weights arise later from the
linear-target stationary equations at an extremum of (9).

Hence an every-level remote coefficient limit is NOT a remaining
requirement for this upper-bound route on regular compacts. The
stationary reduction may be applied to maxima of the proven majorant
in (9). Its other restrictions remain: chart boundaries and phase
incompatibility, and comparison of cancellation loss with Phi rather
than only with a potentially larger positive envelope. No lower bound,
nonzero quantum amplitude, or original-cycle contribution is asserted.

## 6. Separate checked maximum exclusion at the spectral cap

For the full-row functional (6), the endpoint delta=1/2 has
Lambda=4sin^2(pi t) max(x,y), |alpha|=4sin^2(pi t), and total alpha
integral0. Thus H_cap=0 for every closed outer degree.

Fix a positive-length interval [mu,nu] strictly inside(0,1). Put
kappa=cos(pi delta)>0 and choose kappa<min_[mu,nu]sin(pi t).
On that interval

    Lambda_delta>=4sin^2(pi t)max(x,y),
    |alpha_delta|=4[sin^2(pi t)-kappa^2].

Therefore, uniformly over ALL tilts,

    log L_delta>=log max(x,y)
                      -log(1-kappa^2/sin^2(pi t)).

Take the same Legendre infimum; the integral of the second term is
strictly positive. Hence H_delta>H_cap=0 at fixed rows and outer
degree, preserving every shared face load. Such an interval cannot
maximize at the cap. The statement includes closed outer degrees
but NOT a protected fixed start mu=0 or stop nu=1. It is a separate
calculus exclusion for the majorant, not a boundary-uniform finite
coefficient theorem. The protected-cap case remains open here.


## Source dependencies and verification scope

The finite coefficient (1) is the path expansion of the
[original four-state source](research_original_one_sided_four_state_transfer.md).
The [positive eta-word](research_positive_eta_word_transfer.md) gives the
exact coefficient positivity; the [global CROSS proof](actual_global_cross_spectral_gap.md)
gives the fixed-block upper estimate and unused-product logarithmic bounds.
The [stationary reduction](research_regular_shared_spectral_stationary_reduction.md)
uses the resulting sharp functional without claiming local strong duality.

Both internal reviews checked the full-row source indexing, positivity,
uniform upper estimates, compact Cauchy tilts, protected specializations,
CROSS split identity, original target counting and separate cap exclusion.
The proof is analytical. No numerical audit or lower coefficient
asymptotic is claimed. Its uniform statement is restricted
to the specified compact regular charts and exact protected monomers.
