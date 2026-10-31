# The original braid period has an exact finite Euler/Gaussian Cauchy network

Subsequent exact simplification, 28 October: the
[Hardy support theorem](actual_hardy_cauchy_network.md) proves that, in
this COMPLETE ordered factorization, every internal upper-projector
branch is killed by an existing factorial barrier. The
[cyclic-function completion](actual_cyclic_hardy_dilog_network.md)
then replaces the finite Euler kernels by the anchored literature
cyclic functions without changing the original whole source. The
endpoint warnings below remain valid for the separate finite scalar
kernels and arbitrary inserted coupons; they are not an obstruction
to those proved complete-word replacements. The new representation
still requires its selected geometric-cycle theorem.

28 October 2026. The all-word Euler completion gives a strict
factorization of the original crossing into scalar Euler transfer
operators, factorial diagonals and a marked Gaussian diagonal.
The factorial kernels themselves are Euler polynomials. Consequently
the entire original period is an explicit Laurent-polynomial Cauchy
integral with a number of variables depending on the fixed braid,
not on N. Its original cap and peripheral line are retained.

This is useful for the proposed global contour route: it gives an
actual finite-polynomial integrand, not a different state integral
or an assumed sum over critical points. The finite-head projectors
have endpoint branches with their own exponential scale. The
construction does not prove that the geometric saddle is selected.

The existence of an exact finite-variable source period and coherent
composition was already proved in
[the compact coherent calculus](compact_coherent_source_period.md).
The additional content here is the explicit factorization of its
actual crossing kernels into scalar u_N/v_N, Gaussian and finite
projection atoms, with their precise arguments and original source.
This exposes the functions whose GLOBAL asymptotics a contour proof
must control; it is not a new abstract kernel-composition theorem.

## 1. Strict factorization after taking the zero-weight part

Use q=exp(pi*i/N), Q=q^2, x=-M/q and F_a=(Q;Q)_a. Let

    u_N(t)=sum_(a=0)^(N-1)t^a/F_a,
    v_N(t)=sum_(a=0)^(N-1)(-1)^aQ^(a(a-1)/2)t^a/F_a.

On one head let S^+ and S^- be the truncated unit raising and
lowering shifts. Define on two heads

    X_-=S_1^- S_2^+, X_+=S_1^+ S_2^-,
    U_-=u_N(x^-1 X_-), V_-=v_N(x^-1 X_-),
    U_+=u_N(x^-1 X_+), V_+=v_N(x^-1 X_+).

Both transfer arguments have Nth power zero, so V_- and V_+
are the exact inverses of U_- and U_+. Let F_i be the diagonal
whose entry on head i is F_a, and let

    D e_(a,k)=d_k e_(a,k),
    d_k=(-1)^k Q^(k(k-1)/2)x^(-2k).

Then the ACTUAL fusion and positive/negative crossings obey

    C=F_2 U_- F_1 F_2^-1,
    C^-1=F_2 F_1^-1 V_- F_2^-1,
    R_+=kappa C D U_+ C^-1,
    R_-=kappa^-1 C V_+ D^-1 C^-1.              (1)

Here kappa is the original common Cartan scalar, kept unchanged.
The formula for C follows entrywise: X_-^h sends (a,k) to
(a-h,k+h), giving exactly

    x^-h F_a F_(k+h)/[F_h F_k],

the proved actual fusion coefficient. For R_+, start from the
[source-equivalent completion](actual_crossing_euler_completion_and_weight_source.md),
whose right Euler uses S_1^+ times CYCLIC lowering on head two.
Its physical positive-N-weight part is precisely the part where
that cyclic shift wraps. Replacing it by S_2^- takes the degree-zero
part. Since C and D preserve integer degree, the resulting matrix
is the actual R, not only an equivalent scalar period. This gives
the third formula in (1); ordinary matrix inversion gives the fourth.

Thus each crossing is an ordered product of ten elementary factors.
All factors in (1) now preserve total unwrapped degree. This strict
factorization still has finite-head projections; those projections
are encoded explicitly below, not silently removed.

## 2. Scalar Laurent-polynomial kernels

Identify a head vector with a polynomial in z of degree<N. For
Laurent inputs define Pi_N to retain exponents 0,...,N-1 and put

    K_N(t)=sum_(a=0)^(N-1)t^a=(1-t^N)/(1-t).

The apparent pole is removable: K_N is a polynomial. For b heads
the exact projection formula is

    (Pi_N f)(z)=CT_w product_i K_N(z_i/w_i) f(w).

Consequently the transfer factors in (1) have the kernels

    K_(U_-,N)(z,w)=product_i K_N(z_i/w_i)
                                      u_N(x^-1 w_2/w_1),
    K_(U_+,N)(z,w)=product_i K_N(z_i/w_i)
                                      u_N(x^-1 w_1/w_2), (2)

with v_N replacing u_N for the inverses. These formulas are exact
on finite-head inputs: Pi_N of a monomial transfer is precisely
the corresponding product of truncated shifts. In a full kernel
composition every preceding output already lies in that head.

The diagonal factor on a head has kernel sum_a c_a(z/w)^a.
In particular its nontrivial scalar factors are

    F^-1: u_N(z/w),
    F:    N(z/w)^(N-1) v_N(Qw/z),
    D^s: Gamma_(s,N)(z/w), s=+1,-1,
    Gamma_(s,N)(t)=sum_(a=0)^(N-1)d_a^s t^a.    (3)

Every other spectator head contributes K_N(z_i/w_i).
The factorial identity in (3) follows from

    F_a=N Q^(-a-1)[t^(N-1-a)]v_N(t),
    sum_(a=0)^(N-1)F_a t^a=N t^(N-1)v_N(Q/t).

It retains its full factor N and monomial t^(N-1). All kernels
in (2)-(3) are finite Laurent polynomials. Their only coordinate
singularities are zero/infinity; the notation with 1-t in K_N
does not create an additional pole in the complete kernel.

## 3. The full original source and a fixed-dimensional integral

Let beta have b heads and m signed crossings, and expand (1)
in its original order. There are L=10m elementary factors A_l.
Let K_l(z^l,z^(l-1)) be their scalar kernels in (2)-(3), extended
by spectator K_N factors to b variables. Keep the original pivots
g_a=(xQ^-a)^(1-N). At the actual root their head kernel is

    G_N(t)=sum_a g_a t^a=x^(1-N)K_N(Q^-1 t).

For the original normalized-average first-cut source, its scalar
kernel is EXACTLY

    S_N(z^0,z^L)=(1/N)K_N(z_1^0)K_N((z_1^L)^-1)
                  product_(i=2)^b G_N(z_i^0/z_i^L). (4)

For the proved fixed-first-input/all-ones-output source at index
zero, simply replace its first factor by K_N((z_1^L)^-1).
These are the specified original source matrices, not a preferred
new contour or solution. The known root scalar-closure identity
equates their uninserted original periods.

If chi_(beta,N)(M) is the original external modified-dimension,
framing and common-Cartan line, then

    P_(beta,N)(M)=chi_(beta,N)(M)
       CT_(z^0,...,z^L) S_N(z^0,z^L)
                         product_(l=1)^L K_l(z^l,z^(l-1)). (5)

In (5), the factors kappa^sign from (1) are included once in chi,
if they were not already retained in the local kernels. They are
the original factors. One may leave (3)'s factors N inside their
kernels rather than collect them; no numerical multiplier is fixed
after specialization.

The proof is elementary coefficient contraction: each CT at an
internal head identifies its outgoing and incoming finite index.
The source kernel (4) performs exactly the original first-cut
pairing and all original pivotal closures. Thus (5) is the literal
actual tensor contraction written in scalar variables.

Equivalently every CT in (5) is an integral dz/(2pi*i*z) over ANY
nonzero circle. There are b(10m+1) variables, independent of N.
Since the full integrand is a finite Laurent polynomial, all these
radii can be varied freely without crossing a noncoordinate pole.
The equality holds for the whole root meridian family. It is not
an assertion about moving-q normal jets.

There are only m Gaussian kernels Gamma. Expanding those alone
gives a sum over m indices k_j in 0,...,N-1, with explicit weights
product_j d_(k_j)^(sign_j), whose remaining coefficient integral
contains only u_N,v_N, finite projection kernels and source
monomials. This is the requested fixed-number-of-indices
Euler/Gaussian realization of the original scalar.

## 4. The endpoint branches that a global deformation must retain

Formula (5) makes contour deformation possible, but does not remove
the finite-head endpoint actions. For fixed t with |t|!=1,

    (1/N)log|K_N(t)| -> max(0,log|t|),             (6)

uniformly on compact sets away from the unit circle. This follows
directly from (1-t^N)/(1-t). Thus discarding its numerator is an
exponentially wrong replacement in the |t|>1 chamber.

If the kernel network has nu projection factors, expand their
numerators simultaneously:

    product_e K_N(t_e)
      =sum_(epsilon in {0,1}^nu) (-1)^|epsilon|
                  product_e t_e^(N epsilon_e)/(1-t_e). (7)

There are at most 2^nu branches, where nu<=bL+b+1 is independent
of level. In each radius chamber avoiding t_e=1, (7) is an exact
identity on the SAME torus. Its branch actions retain the linear
terms 2pi*i sum epsilon_e Log(t_e)/h, h=2pi*i/N. Individual
branches have artificial poles that cancel in their marked sum;
deforming them across those poles separately requires the
corresponding residue correction.

In particular, `K_N(z/w) dw/w=[1-(z/w)^N]dw/(w-z)` is regular
at the proposed reproducing face `w=z`. For any other factor
regular there, the two split residues are `+f(z)` and `-f(z)`.
Thus a reduction keeping only the first reproducing residue loses
the accompanying tail chain. This is visible to the original
source even in degree zero: with the literal transfer arguments
`X_-=S_1^- S_2^+`, `X_+=S_1^+ S_2^-`,
`X_-X_+=(I-E_top) tensor (I-E_bottom)`. The averaged original
two-head pivotal cut evaluates this as `-(N-1)g_0/N`, whereas
ordinary multiplication of the reciprocal Laurent arguments gives
`I`, whose pivotal cut is zero. These walls are not in the proved
positive-N-weight source-null ideal. Quantitative interior
conditions under which the tails really are exponentially small
are given in [the analytic bulk projection theorem](analytic_bulk_projection_and_euler_endpoint.md).

This counts ONLY the projection-numerator choices. It does not
count or control every semiclassical branch of u_N,v_N or the
Gaussian polynomials Gamma. Their own finite truncations and
Stokes transitions also have to be analyzed. In particular the
proved small-disk Euler expansions cannot be continued uniformly
to arbitrary geometric radii merely because the finite polynomials
are entire in their arguments.

These endpoint choices are not new knot states or independently
normalizable periods. They are components of one prescribed
source. Around a closed chain made only of projection ratios,
the product of their moduli is one, so they cannot ALL lie in
the decaying |t_e|<1 chamber. Other diagonal factors in an actual
network can change that feasibility problem; no universal
infeasibility assertion for every connected knot is made here.

Likewise the monomials in (3) and the marked Gaussian factors must
remain in the global phase. Strict concavity of a bulk volume
functional alone does not bound the full upper envelope (6)-(7)
or prove cancellation cannot occur between its branches.

The concrete next problem is therefore well defined: choose a
torus through the complete geometric point, prove uniform actual
atom asymptotics there INCLUDING the marked endpoint branches,
and establish the global real-part gap and nonzero derived source.
The present note supplies that exact integrand and its finite
branch bookkeeping, not those three analytic/geometric assertions.

## 5. The single general comparison still to prove

For clarity, a sufficient general comparison proposition for THIS
literal network is the following. It is an OPEN target, not a
consequence claimed here.

For the proposed broad class of positive geometric ideal
triangulations, construct a source-preserving reduction of (5)
and a contour deformation of its original marked cycle to a
relative Rivin-angle chain such that:

1. Every auxiliary integration, cap, projection-numerator branch
   and peripheral normal row is carried by an exact identity or
   by a contour deformation with its matched residue terms.
2. The resulting chain projects to the positive angle domain
   with oriented local degree plus or minus one at its complete
   Rivin optimizer. The full derived source coefficient at that
   point is nonzero, with its normalization bounded above and
   below by powers of N.
3. The actual finite atoms have a UNIFORM comparison on that
   chain to the calibrated marked action. Its unique maximal
   real exponent is Vol(X)/(2pi) at the complete point; all
   other stationary or escaping boundary pieces have a strict
   exponential gap or a proved smaller contribution.

After redundant source variables are eliminated, a nondegenerate
Gaussian contraction (or the corresponding sourced clean-critical
calculus), with its local remainder controlled RELATIVE to the
full nonzero leading source coefficient, and the global gap
would then give

    log|P_(beta,N)|=N Vol(X)/(2pi)+o(N),

with the original polynomial peripheral factors still attached.
The leading source coefficient may vary with N; the stated upper
and lower polynomial bounds do not assert a fixed power or a
convergent prefactor. A formula N^alpha(c+o(1)) would require an
additional coherent density expansion. The logarithmic statement
already proves the original volume limit. It is not enough
to match one local saddle of one atom or show that the positive
angle optimizer exists.

The currently unproved assertion is the whole marked chain/source
comparison above, particularly its degree-one/nonzero-source
property and uniform control of all atom endpoint sectors. Rivin
strict concavity controls the optimizer ON an already supplied
angle chain; it does not determine the homology or intersection
degree of the original cycle (4). Formula (5) now makes that
cycle and every required function explicit for the comparison.

## 6. Exact checks

[The audit](../experiments/audit_actual_euler_gaussian_cauchy_network.py)
and [saved output](../experiments/actual_euler_gaussian_cauchy_network_results.json)
check (1) against the original positive and negative crossing,
the actual fusion matrix, transfer projection kernels, factorial
reflection kernels and full original word/source contractions.
These are exact finite-field convention checks; (1)-(7) are
direct all-level identities. No lower bound for the hyperbolic
volume exponent is claimed.
