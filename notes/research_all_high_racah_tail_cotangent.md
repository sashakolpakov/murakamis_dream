# Archived diagnostic: a coherent all-high Racah tail and a cotangent sum

**Current status, 29 October 2026:** the cotangent identity recorded here
is now proved by the own finite Fourier argument in
[the coherent-tail residue theorem](actual_coherent_racah_tail_fourier_residues.md).
That theorem also proves polynomial first-normal bounds whenever the
maximal face sum is repeated. General unique-maximal-face residuals
and higher generic normal jets remain open.

The text below is the preserved HISTORICAL DIAGNOSTIC, written before
that proof. Its question marks and statements that a finite proof was
missing describe that earlier checkpoint. The eleven-level numerical
record has not been relabeled as a proof.

29 October 2026, earlier checkpoint. RESEARCH LEAD ONLY at that stage.
The finite identity proposed below had been checked numerically at
eleven specified levels. No finite proof, certified error bound,
uniform normal estimate, or general partner-transport theorem was
asserted at that checkpoint.

## 1. The actual generic normal being observed

Fix an integer m>=1 and

    N=3m+1, D=N-1=3m, q=exp(pi i/N), Q=q^2,
    theta=pi/N, s_r=product_(u=1)^r 2sin(u theta).

Start with the supported folded sextuple (m,m,m,m,m,m), and change
ALL six spins to their partners D-m=2m. Use the SAME generic
symmetric quantum integers [u]=(zeta^u-zeta^-u)/(zeta-zeta^-1)
and seven-factorial sum S(zeta) as in the
[proved common-phase and retained-normal theorem](actual_supported_racah_common_phase_and_normal_metric.md).
For this all-high branch, every face sum is 6m and every opposite
sum is 8m. Its true summation range is therefore 6m<=z<=8m.

Remove the actual numerator zeros, before root evaluation:

    (-1)^D S(zeta)/[N]=C(zeta)+[2N]T(zeta).       (1)

Here C is the SINGLE term z=6m=2D, and T consists of the terms
z=6m+1,...,8m with BOTH [N] and [2N] omitted from the numerator.
All seven true denominator indices are <N. The functions C,T are
analytic at q, and the elementary factorial reflection gives

    C(q)=N^2/s_(2m)^3=s_m^3/N,
    T(q)=-2sin(theta)N^2 sum_(k=0)^(2m-1)
              (-1)^k s_k/[s_(k+1)^4 s_(2m-1-k)^3]. (2)

The tail is really present. In the coordinate t=log(zeta/q),

    dot[(-1)^D S/[N]](q)=dot C(q)+4N/(q-q^-1) T(q). (3)

Consequently T(q) cannot be deleted merely because [2N](q)=0.
The [all-partner value theorem](actual_racah_partner_reflection_identity.md)
does not identify the derivatives in (3).

## 2. The observed formula and its exact checked scope

The proposed finite identity is

    T(q)/C(q) ?= -3sin(theta) sum_(u=1)^m cot(u theta). (4)

The question mark is intentional. The portable diagnostic checks
EXACTLY the following previously probed values:

    m=1,2,3,4,6,8,12,16,24,32,48,
    N=4,7,10,13,19,25,37,49,73,97,145.

Thus it checks both parities and several composite levels, but not
every m<=48. Its working precision is 3N+60 decimal digits. At these
levels the two sides agree to far more than forty decimal digits.
This is numerical evidence, not an exact cyclotomic certificate.

Some rounded values of the coherent ratio are

    N=4:   -2.1213203435596,
    N=25:  -7.5419628808584,
    N=49:  -9.5541461519503,
    N=145: -12.801479315575.

Taking absolute values INSIDE the alternating sum in (2) loses the
cancellation. The diagnostic records this absolute-tail comparison
separately. The observed large overestimate supplies no no-go theorem
for the coherent sum and no proof of its growth rate.

If (4) is eventually proved, elementary cotangent estimates would
bound THIS T(q)/C(q) polynomially (in fact logarithmically). That
would still be a special all-high family, not a theorem for every
supported partner branch or for every normal order.

## 3. Higher-normal observations and a possible finite-proof route

The same existing probe records i dot T(q)/C(q) and
ddot T(q)/C(q), with no derivative of C in these ratios. These are
computed from the actual omitted-zero factorial terms, not by
differentiating (4). For a unit quantum integer the exact logarithmic
derivatives at q are

    dot log[u]=-i[u cot(u theta)-cot(theta)],
    ddot log[u]=u^2 csc^2(u theta)-csc^2(theta).   (5)

Sum (5) over the numerator indices except N,2N and subtract the
seven denominator sums. If the resulting real quantities for a
tail term are L1,L2, its first derivative is -i L1 times the term
and its second derivative is (L2-L1^2) times the term. The recorded
values grow moderately at the checked levels; no asymptotic bound
or all-order conclusion is inferred from that observation.

A possible own finite-proof route is a parameter-differentiated
cyclic terminating summation. The proved central cotangent identity
in [the spectral/normal transport note](actual_partner_normal_transport.md#5-an-exact-central-normal-check-by-a-finite-product-derivative)
comes from the OWN balanced Sears calculation followed by a finite
product derivative. It motivates looking for an analogous finite
transformation for (2). That analogy is a research direction, not
a missing step silently supplied by a named summation formula.

The current established scope remains the polynomial root spectral
estimate and the tail-free generic-normal criterion. General bounds
on live [2N] currents, their fixed jets, and coherent partner sewing
remain open.

Portable diagnostic: [script](../experiments/diagnose_all_high_racah_tail_cotangent.py)
and [recorded results](../experiments/all_high_racah_tail_cotangent_diagnostic_results.json).
Only mpmath is required. Status PASS_DIAGNOSTIC means the finite
numerical comparisons passed, not that (4) is proved.
