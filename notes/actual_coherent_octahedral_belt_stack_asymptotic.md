# Coherent complete-belt stacks with arbitrary signs and outer twists

29 October 2026. The complete-circle boundary packet removes the
balance restriction from the original quantum source of the literal
octahedral belt stacks. No ordering, parity or residue subsequence is
selected. A fixed extra signed crossing power is retained exactly;
its literal geometric collar certificate is linked separately below.

## 1. The exact original source and its nodal crossing phase

Use the genuine full checked crossing R, the complete ordinary
auxiliary-circle operator L_N and the unscaled physical turn of
[the original stack construction](actual_balanced_octahedral_belt_stack_volume.md).
Write z=z_N, z^sharp for its literal reflected polynomial, and

    f_+=z^sharp R^(-1), f_-=Rz,
    n=p+q>0, e=q-p,
    Phi_(p,q,a;N)=phi(L_N R^a product_i f_(epsilon_i)),

where the fixed word epsilon has p plus and q minus pieces, and
a is any fixed signed integer. The whole pair commutant is the
FULL Hermite algebra, so the exact all-port identity is

    Phi_(p,q,a;N)=phi(L_N R^(e+a)(z^sharp)^p z^q)
       =N sum_(j=0)^(N-1) R(c_j)^(e+a)
                                  conjugate(z(c_j))^p z(c_j)^q. (1)

The second equality is the proved original complete-belt sewing
functional; the repeated Casimir normal source has not been replaced
before closure. Its derivative pairing gives precisely the displayed
N-weighted nodal sum. The all-port equality in the first line includes
the normal directions and is stronger than the final nodal formula.

Put d=N-1, q_root=exp(pi i/N), kappa=exp(pi i d^2/(2N)) and

    theta_j=(2j+1-N)pi/N, c_j=-2cos(theta_j).

The literal crossing has R(c_j)=kappa(-1)^j q_root^[j(j+1)].
Consequently, at EVERY node and both parities,

    R(c_j)=kappa^(1/2) exp[iN theta_j^2/(4pi)],
    kappa^(1/2) HERE MEANS exp[pi i d^2/(4N)].             (2)

There is no principal-square-root convention. The two exponent
formulas differ by -2pi i j, exactly. Since the two indices of a
double node give the same eigenvalue, (2) is compatible with all
multiplicities in (1). In particular |R(c_j)|=1.

## 2. The nonzero all-parity coherent Gaussian

The [source-exact boundary packet](actual_complete_circle_boundary_packet.md)
gives, uniformly for small real theta,

    z(-2cos theta)=exp(-i pi d/4) a(i theta)
                          exp[Nj(i theta)] [1+O(1/N)],
    j(i theta)=j_0-theta^2/(4pi)+O(theta^4),
    a(0)=2^(-9/4) exp(i pi/8), j_0=v8/pi.                 (3)

Both a(i theta) and j(i theta) are even analytic; j(i theta) is
real. Every fixed neighborhood of theta=0 has an exponential gap
on its complement for the literal polynomial. The twist in (2)
has unit modulus, so it preserves that entire-source gap.

Combining (1)--(3), the local exponent is EXACTLY, to quadratic order,

    nN j_0 - N[n-i(e+a)]theta^2/(4pi).

Its real quadratic part is positive because n>0, even for arbitrarily
large FIXED signed a. The nodal grid has step2pi/N and shift0 for
odd N, shift1/2 for even N. Its complex Gaussian sum is

    sum_j exp[-N(n-i(e+a))theta_j^2/(4pi)]
       =sqrt(N)/sqrt(n-i(e+a)) [1+O(exp(-cN))].

Here and below sqrt has positive real part. This follows directly
by Fourier transforming the Gaussian: all nonzero frequencies are
bounded by exp[-pi N Re(1/(n-i(e+a)))], at either lattice shift.
The two tails outside the fixed local window are exponentially
small as well. Taylor expansion of the even analytic amplitude and
quartic exponent has relative error O(1/N); dominated Gaussian
integration makes that estimate uniform on the actual lattice.

The resulting FULL original source is

    Phi_(p,q,a;N)
      =N^(3/2) 2^(-9n/4) kappa^(a/2)
         exp[-ie pi/8+ie pi/(4N)]
         /sqrt(n-i(e+a)) * exp[nN j_0] [1+O(1/N)].        (4)

The fixed constant in the error can depend on p,q,a. There is no
claim uniform in a growing with N. To check the phase explicitly,
the constant factors BEFORE simplification are

    kappa^((e+a)/2) exp[-ie pi d/4] exp[ie pi/8].

Since d^2/N-d=-d/N, these equal precisely those in (4).
This retains the original crossing scalar kappa, not only its
modulus. No source phase, normal or winding coefficient is dropped.

The leading factor in (4) is nonzero at EVERY sufficiently large
level, without a prime-level, parity or congruence restriction.
In particular

    lim_N (2pi/N) log|Phi_(p,q,a;N)|=2n v8.              (5)

For p=q=k and a=0, (4) reduces to the earlier retained-belt constant
N^(3/2)2^[-(9k+1)/2]/sqrt(k), providing a normalization check.
The excluded n=0 case has no positive localized packet and is not
covered by this theorem.

## 3. Actual links and the precise geometric scope

For a=0 the literal octahedral stack proof already constructs the
ACTUAL complement for every fixed sign word of length n>=1. Its
complete regular-cell metric has volume2n v8, without a balance
hypothesis. Its original source is exactly (1). The original reduced
single-cut Kashaev normalization differs only by the recorded unit
phases (and the stated single1/N in the modified convention), so
(5) proves the full original volume limit for EVERY such sign word.

Thus unbalanced stacks, including a single positive or negative
piece, are now included. This is an actual link-family extension,
not a new claim about arbitrary bridge graphs or independently
filled crossing circles. Its possible containment in previously
known Whitehead-chain families retains the earlier coverage caveat.

For a!=0, (1)--(5) retain the literal original outer R^a insertion
with all of its source scalars. The independently reviewed
[outer-collar puncture permutation/isometry certificate](actual_balanced_octahedral_belt_stack_volume.md#3a-any-fixed-integer-outer-crossing-power)
identifies its ACTUAL complement with the same complete regular-cell
gluing, of volume2n v8. Its component count is n+3 for even a and
n+2 for odd a. Thus the original volume equality holds for every
fixed sign word and every fixed integer outer twist a. The
topological assertion comes from that literal collar certificate,
not from the quantum rate.

Audit: [full original sign-word/outer-twist sources, high-precision nodal phase checks and coherent Gaussian calibrations](../experiments/audit_actual_coherent_octahedral_belt_stack_asymptotic.py).
Fresh replay PASS: seven full physical levels,210 all-sign word
operators and490 complete original outer-twist closures;860
100-digit all-parity nodal phase checks; six growing-N families of
complete coherent Gaussian calibrations. The phase identities themselves
are proved algebraically above; the phase checks and profiles supplement
the analytic proof and are not its noncancellation premise.

Independent analytical check: the global critical-path auditor
re-derived (2), the exact imbalance/Cartan phase in (4), and the
complex Gaussian at both lattice shifts. The pointwise source error
is controlled after summation by its absolute real Gaussian, with
fixed factor depending on n,e,a. Thus no parity cancellation or
unestimated residue current is being assumed away.
