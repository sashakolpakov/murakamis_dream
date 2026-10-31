# Exact signed cap/CROSS contraction in a macroscopic high-demand range

31 October 2026. **Internally reviewed, unpublished analytical theorem**
for the exact two-port incidence in the
[original-demand convolution](research_two_port_main_cap_original_demand_convolution.md).
The original internal face demand, both remaining degrees, and both
genuine source cutoffs are retained. This proves a nontrivial range of
that note's proposed comparison. It is not a bound for its remaining
degrees, arbitrary spectra, or the whole invariant. The same exact degree window
is controlled at every level N>=3: the comparison factor is one at even
levels and 4N at odd levels, using the actual odd regularized reference
specified in section 7.

## 1. Statement with the original finite normalization

Let N=2m>=4, d=N-1, M=m-1 and theta=pi/N. Keep the original ports

    E=(A,0,C,Z), F=(0,A,0,C),

where A occurs only at these two ports. E is its genuine CROSS
polynomial at -2; F is its genuine RIGHT polynomial at +2. Extract
the actual A-degree d first. In the notation of the original reduction,

    S_(N,n)=sum_(j in J_n) (-1)^j U_j C_(j,n-j),
    D_(N,n)=sum_(j in J_n) V_j C_(j,n-j)>0,
    J_n=[max(0,n-M),min(M,n)] intersect Z,
    0<=n<=2M.                                      (1)

The raw B_N coefficient is (-1)^d S_(N,n), and the positive endpoint
coefficient B_N^0 is D_(N,n). No extra N factor occurs.

**Theorem.** For every even N>=4 and every original remaining degree

    ceil(3N/4-3/2)<=n<=N-2,

one has the exact inequality

    |S_(N,n)|<=U_M C_(M,n-M)
               =V_M C_(M,n-M)<=D_(N,n).            (2)

Thus the polynomial comparison holds in this entire range with
constant one, not just with a polynomial loss. In terms of the other
remaining degree k=d-n, the range is

    1<=k<=floor(N/4+1/2).

In particular it contains every macroscopic limit n/N->rho>3/4,
and includes the stated exact threshold at rho=3/4. The comparison
is at the fixed spectra of (1) and at even levels only.

## 2. A positive injection with every unused factor retained

Recall the literal source recurrence and coefficients

    s_r=2 sin(r theta), a_r=4 cos^2((r+1/2)theta),
    K_0=1, K_1=s_1^2(A+Z),
    K_r=s_r^2(A+Z)K_(r-1)
          +s_r s_(r-1)a_(r-1)AZ K_(r-2),
    C_(j,h)=[A^j Z^(d-h-j)]K_(d-h)
                          product_(r=d-h+1)^d a_r. (3)

All these coefficients are positive on the indices below. Let
h=n-j and r=d-h. For j in J_n with j<M, append the A-monomer
at the next row of K. Its contribution to the coefficient of
A^(j+1) Z^(d-n) is s_(r+1)^2 times the preceding coefficient;
every other contribution is nonnegative. The unused suffix loses
exactly the factor a_(r+1). Therefore

    C_(j+1,h-1)>=s_(r+1)^2/a_(r+1) C_(j,h)
                  =s_h^2/a_(h-1) C_(j,h).          (4)

The last equality uses r+1=N-h, hence s_(r+1)=s_h and
a_(r+1)=a_(h-1). The factor in (4) is not an approximation;
it is the exact weight of this subset of original paths, divided
by the single unused row removed from the suffix.

In the range of the theorem n>M, so J_n=[L,M] with L=n-M.
For j=L,...,M-1, both j and h remain within the actual cutoffs;
h>=n-M+1>=1. No full-sum or endpoint extension is being used.

## 3. Monotonicity of the actual alternating summands

The literal cap ratio is

    U_(j+1)/U_j
       =sin^2((j+1)theta)/sin^2((j+3/2)theta).

Put T_j=U_j C_(j,n-j)>0, a=(j+1)theta, b=h theta,
and epsilon=theta/2. Combining this ratio with (4) gives

    T_(j+1)/T_j
      >=[sin(a) sin(b)/(sin(a+epsilon)cos(b-epsilon))]^2. (5)

The finite threshold in (2) is exactly

    n-M+1>=N/4+1/2.

Consequently for every adjacent pair in J_n,

    pi/4+epsilon<=a,b<=pi/2-theta.

All denominators in (5) are positive. On the relevant intervals,

    sin(a)/sin(a+epsilon)
       and sin(b)/cos(b-epsilon)

are increasing functions of their arguments: their logarithmic
derivatives are cot(a)-cot(a+epsilon)>0 and
cot(b)+tan(b-epsilon)>0. Comparing the first ratio at a=pi/4
and the second at b=pi/4+epsilon gives

    [sin(pi/4)/sin(pi/4+epsilon)]
       [sin(pi/4+epsilon)/cos(pi/4)]=1.

Thus (5) is at least one, and

    T_L<=T_(L+1)<=...<=T_M.                         (6)

For a singleton J_n this assertion is vacuous and the next step
holds directly.

## 4. Alternation uses the original cutoff endpoint

For any nonnegative increasing finite sequence, its alternating sum
has absolute value at most the final entry. This follows by pairing
consecutive terms from the final end for nonnegativity and from the
opposite end for the upper bound. Applying it to (6) gives

    |sum_(j=L)^M (-1)^j T_j|<=T_M.                 (7)

The original cutoff is crucial: its final cap weight obeys

    U_M/V_M
       =product_(r=0)^M cot^2((r+1/2)theta)=1,      (8)

by pairing angles with their complements. In fact U_M=V_M=N:
the product over integer sine angles 1,...,m-1 has square
N/2^(N-1), while the product over half-integer angles
1/2,...,m-1/2 has square 2^(1-N); the prefactors in U_M and
V_M cancel their respective omitted first angles.

The term V_M C_(M,n-M) is present in the original positive sum
D_(N,n). Equations (7)--(8) prove (2), with all raw and endpoint
normalizations unchanged.

## 5. Exact scope and remaining issue

Equivalently, restrict the two degree-d polynomials B_N(C,Z) and
B_N^0(C,Z), after extracting A^d, to the C degrees in the theorem.
The coefficientwise modulus of the restricted B_N is bounded by
the same restriction of B_N^0. Every exterior face target and the
remaining C,Z degrees are retained. No exterior coupon has been
changed, and a signed exterior may only be bounded after its own
absolute coefficients are explicitly retained.

This argument uses cancellation in the original alternating sequence.
It does not pass through the [disproved bare cap-Cauchy norm or
absolute tensor coefficient mass](research_cap_moment_cauchy_norm_obstruction.md). It gives no estimate for lower
macroscopic n, and does not identify the projected coupons with
unprojected Casimir functions. The full uniform inequality in the
original reduction and the general strictly overloaded source bound
remain open. No numerical sampling is used in this proof.

## 6. At low remaining demand the two projections are redundant

There is a separate exact source simplification for 0<=n<=M. This
section gives an identity, not another estimate.

The FULL original cap at F, before RIGHT projection, has

    H_F(A,C;2)=sum_(j=0)^d (-1)^j U_j A^(d-j)C^j.   (9)

To verify the full range, set gamma_r=2-2cos((2r+1)theta)>0.
The protected output middle forces the actual stop to be d. For
the start i=d-j, the original raw sign and magnitude are

    (-1)^d (-1)^(d-j)=(-1)^j,
    product_(r=0)^(d-j-1) gamma_r
                         product_(r=d-j+1)^d s_r^2.

Reflection gives gamma_(d-r)=gamma_r and s_(N-r)=s_r. Thus the
magnitude equals product_(r=j+1)^d gamma_r times
product_(r=1)^j s_r^2. The exact full product
product_(r=0)^d gamma_r=4 identifies it with U_j, including both
j=0 and j=d. No upper-half state, derivative datum, or unused row
has been discarded.

Likewise the FULL original E coupon at -2, before CROSS projection,
is

    H_E(A,C,Z;-2)=(-1)^d sum_(h=0)^d sum_(a=0)^(d-h)
                    C_(a,h) A^a C^h Z^(d-h-a),     (10)

where the same literal coefficient formula (3) defines C_(a,h)
for all these h. The protected input middle forces start zero,
so (10) retains every possible actual stop and its unused suffix.

In the product of (9)--(10), extracting the original A^d forces a=j.
The remaining C-degree n then forces j+h=n. All exponents are
nonnegative. Hence if n<=M, necessarily j<=M and h<=M. These are
exactly the genuine RIGHT and CROSS restrictions already imposed in
(1). Consequently

    [A^d C^n Z^(d-n)] H_F(full;2) H_E(full;-2)
                            =(-1)^d S_(N,n),
    0<=n<=M.                                       (11)

This permits using a valid identity of the actual UNPROJECTED Casimir
coupons before taking this low-degree coefficient. It does not make
the projected coupons covariant operators and does not turn their
overlapping pair Casimirs into functions of one commuting operator.
Any further tensor identity must keep the original pair order and
cup/turn frames. Equation (11) alone supplies no polynomial bound in
the missing low- or intermediate-demand ranges.


## 7. Odd levels retain the same degree window

The reference is the actual spectral regularization at the fixed original
root, not the raw odd endpoint. The even statement in sections 1--5 and
the even low-demand identity in section 6 remain unchanged.

Let N=2m+1>=3, d=2m, M=m-1, theta=pi/N and keep the original quartets
E=(A,0,C,Z), F=(0,A,0,C), with A internal to these two ports. The raw E
coupon is V_N(-2), while the raw F coupon is V_N(2), restricted to RIGHT.
The positive reference at each port is the ACTUAL polynomial coupon

    F_N=V_N(-2)-N^(-2) V_N'(-2),

where the derivative is spectral at the fixed root. Use its CROSS part
at E and RIGHT part at F. These are the original odd supports: E has
C-middle degree h<=m, and F has A-middle degree d-j>=m+1, or j<=M.

The same literal continuant K_r and suffix coefficients C_(j,h) as in
the even theorem describe raw E, with a_m=0. The polynomial has no terms
h>m, since those paths miss the central row. The full cap formula U_j
is unchanged at every j=0,...,d. Consequently the original signed
coefficient after extracting A^d and then C^n Z^(d-n) is

    S_(N,n)=sum_(j in J_n) (-1)^j U_j C_(j,n-j),
    J_n=[max(0,n-m),min(M,n)] intersect Z, 0<=n<=N-2.

There is no extra raw sign here because d is even. Write V_j^o for the
positive F-reference cap coefficient. Its path lies entirely ABOVE the
central row when j<=M. Its raw endpoint coefficient therefore vanishes;
the spectral derivative removes its one unused zero factor. The exact
positive coefficient is

    V_j^o=N^(-2)
       product_(r=0,...,d-j-1; r!=m) a_r
       product_(r=d-j+1,...,d) s_r^2.                     (12)

The minus sign in F_N converts the negative spectral derivative to
the displayed positive product. Equivalently this follows from the
positive u-derivative in H_(V_N(-2-u)), with its coefficient N^(-2).

Let Cbar_(j,h) be the genuine CROSS coefficient of H_(F_N) at E. The
odd positive path expansion proves Cbar_(j,h)>=C_(j,h)>=0. Define the
actual positive comparator after the same demands by

    D^o_(N,n)=sum_(j in J_n) V_j^o Cbar_(j,n-j).

For every odd N>=3 and

    ceil(3N/4-3/2)<=n<=N-2,

we claim

    |S_(N,n)|<=4N D^o_(N,n).                            (13)

For a singleton J_n the argument below reduces to its endpoint term.
Otherwise n>=m and J_n=[L,M], L=n-m. The exact monomer injection is
unchanged: for j=L,...,M-1 and h=n-j,

    C_(j+1,h-1)>=s_h^2/a_(h-1) C_(j,h).

Its denominator is positive because h<=m and h-1<m; the unused row
removed from the suffix is N-h>m. Thus the central zero is never divided
out. With a=(j+1)theta, b=h theta, epsilon=theta/2 the original summands
T_j=U_j C_(j,n-j) satisfy

    T_(j+1)/T_j
       >=[sin(a)sin(b)/(sin(a+epsilon)cos(b-epsilon))]^2.

The stated threshold is n-m+1>=N/4. Hence a>=pi/4 and
b>=pi/4+theta, which is stronger than b>=pi/4+epsilon.
All denominator angles stay in the positive sine/cosine range, since
j+1<=M and h<=m. The two increasing sine ratios, evaluated at
a=pi/4 and b=pi/4+epsilon, have product one. Therefore T_j is increasing
on the original J_n, and its alternating sum has modulus at most T_M.

The endpoint normalization is exact, not merely asymptotic. The standard
full sine products and reflection give

    product_(r=0)^(m-1) a_r=N,
    product_(r=1)^m s_r^2=N,
    s_m^2=4cos^2(theta/2).

The first identity follows because the two noncentral halves have equal
products and their total product is N^2. Formula (12) at j=M gives

    V_M^o=N^(-2) N [N/s_m^2]=1/[4cos^2(theta/2)].

For U_M, its numerator and denominator products are respectively

    product_(r=1)^(m-1) sin^2(r theta)
         =N/[2^(N-1) cos^2(theta/2)],
    product_(r=0)^(m-1) sin^2((r+1/2)theta)=2^(1-N).

Thus U_M=N/cos^2(theta/2)=4N V_M^o. Combining monotone alternation
with the original endpoint term yields

    |S_(N,n)|<=U_M C_(M,n-M)
       =4N V_M^o C_(M,n-M)
       <=4N D^o_(N,n),

which is (13). For N=3 only the singleton case occurs, and the same exact
products give U_0/V_0^o=12. No small-level exception is omitted.

The original even theorem and (13) consequently cover the SAME degree
range at all N>=3, with constant one at even levels and factor4N at odd
levels. The odd reference and its different CROSS cutoff remain explicit.
This is a signed two-port coefficient estimate at the stated spectra,
not a whole-source bound or a general volume-conjecture conclusion.

The source input is the [original odd regularized numerator](actual_fejer_odd_regularized_full_numerator.md),
sections 1--2: the literal derivative sign, noncentral product N^2,
genuine supports, and coefficientwise P0<=H_(F_N). The all-index cap
formula follows by the same unused-row reflection as in section 6;
its full gamma product is 4 at both parities. No new finite audit or
numerical asymptotic experiment is used.

## 8. Low demand still detects the actual Casimir Jordan data

This final section concerns an EVEN-level source obstruction to a
coupon-uniform semisimple adapter. It does not obstruct the particular
fixed-resolvent signed inequality or a non-intertwining positive realization.

Use even N=2m>=4, d=N-1, M=m-1 and the original two-port incidence
E=(A,0,C,Z), F=(0,A,0,C). For arbitrary polynomial Casimir coupons
f,g define the actual low-demand functional

    Lambda_n(f,g)=[A^d C^n Z^(d-n)]
        H_f(0,A,0,C) H_g(A,0,C,Z),  0<=n<=M.       (14)

The full homogeneous source fixes every raw normalization in (14).
It is legitimate to study unprojected coupons here. In the fixed pair
f=V(2), g=V(-2), the original RIGHT/CROSS projections are automatically
satisfied after these degrees are extracted, as section 6's separately reviewed
low-demand identity proves.

The following proposed stronger realization is impossible: a
semisimple realization of the ACTUAL E Casimir on a space, satisfying
its original annihilating polynomial chi_N, which computes (14)
uniformly for polynomial g by replacing g(Omega_E) with that same
polynomial of the semisimple operator. Boundary vectors/functionals
and the other coupon may be arbitrary. A finite-dimensional
self-adjoint restriction or quotient intertwining the actual Casimir
and preserving all these polynomial-coupon observables would be a
special case. No assumption about a particular choice of positive
inner product is needed for the obstruction.

### A literal nonzero nilpotent coupon

The actual annihilating polynomial at even levels is

    chi_N(z)=2T_N(z/2)+2=4T_m(z/2)^2.

The original complete-circle polynomial is

    L_N(z)=(-1)^d U_d(z/2)
           =(-1)^d 2T_m(z/2) U_(m-1)(z/2).        (15)

Here T and U are the ordinary Chebyshev polynomials with their
displayed arguments; U_d(z/2) is monic. Thus L_N vanishes at
every distinct root of chi_N. Also L_N^2 is a multiple of chi_N,
so its value on the actual pair Casimir is square-zero. It need
not be zero because the actual source retains confluent data.

For any semisimple operator X with chi_N(X)=0, one has L_N(X)=0.
Therefore a coupon-uniform realization of the type in the preceding definition would
force Lambda_n(1,L_N)=0. We now check the opposite statement in the
original source at every low remaining degree.

### Every original low degree detects this coupon

The identity at F specializes to

    H_1(0,A,0,C)=A^d.

Consequently (14) becomes exactly

    Lambda_n(1,L_N)=[C^n Z^(d-n)]H_(L_N)(0,0,C,Z). (16)

The [original complete-channel identity](actual_homogeneous_casimir_face_source.md) is

    H_(L_N)(x,b,c,y)
       =N sum_(a=0)^M k_a beta_a^2
          D_a(x,b,y)D_a(x,c,y) Ptilde_(d-2a)(x,y), (17)

where k_a beta_a^2>0. Each D_a is the actual positive-definite
determinant polynomial and every homogeneous degree-a coefficient
in its three variables is strictly positive. The retained polynomial
Ptilde_s has strictly positive coefficients; at a=M, s=1 and
Ptilde_1(x,y)=x+y. The [positive determinant theorem](actual_complete_circle_positive_face_polynomial.md) proves these exact finite source identities, not
coefficient-entropy assertions.

After the specialization in (16), the a=M summand in (17) contains

    N k_M beta_M^2 D_M(0,0,Z) D_M(0,C,Z) Z.

The first determinant is a strictly positive multiple of Z^M,
and the second has a strictly positive coefficient at every
C^n Z^(M-n), 0<=n<=M. Their product therefore contributes
positively to C^n Z^(d-n), since 2M+1=d. All other summands in
(17) are nonnegative. It follows that

    Lambda_n(1,L_N)>0 for EVERY 0<=n<=M.           (18)

As a normalization check, Lambda_0(1,L_N)=N^2. The highest-degree
term of L_N is (-1)^d z^d; producing the pure outer monomial Z^d
from the actual face operator requires all d lowering steps and
gives another (-1)^d times product_(r=1)^d s_r^2=N^2. Lower
powers cannot produce that outer degree. The two signs cancel.

Equations (15) and (18) contradict the proposed coupon-uniform
semisimple realization. In particular the low original coefficient
filtration has not annihilated the complete-circle nilpotent.
This is an all-even-level/all-low-degree source statement, not a
numerical example or an unconditioned coefficient obstruction.

### Scope of the obstruction

The actual signed target uses the particular pair V(2),V(-2).
The proof does not exclude an identity specialized to this pair,
a positive representation that does not intertwine arbitrary Casimir
polynomials, or a bound that retains explicit Jordan corrections.
It does exclude calling such a construction an actual semisimple
Casimir restriction while also claiming preservation of every
polynomial-coupon observable in (14).

No estimate for the signed coefficient, no hyperbolic-volume statement,
and no obstruction to the original volume conjecture is inferred.
The only inputs are the actual homogeneous source, its full complete
polynomial with confluent data, and the exact positive determinant
formula, all already independently reviewed.


## Inputs and internal review

The exact normalization and local incidence are those of the
[original two-port source reduction](research_two_port_main_cap_original_demand_convolution.md).
The full-interval source used in section 6 is the
[original four-state source identity](research_original_one_sided_four_state_transfer.md);
its [homogeneous physical adapter](actual_homogeneous_casimir_face_source.md)
keeps the original pair order and all matrix data.

Root and cluster independently read the complete high-demand proof
and original-source scope in sections 1--5, reporting PASS. Cluster additionally read the complete written low-demand coefficient
identity in section 6, including all-index raw signs and source factors,
and reported PASS. Root separately checked the same all-index cap and
source derivation. These are internal analytical
reviews, not external peer review. No numerical asymptotic experiment
or new finite audit is used as proof.

Root supplied and fully checked the odd extension in section 7. Coherent
and cluster independently read its complete written proof and checked
the original odd support, spectral-derivative sign, central-zero handling,
and all endpoint normalization products, each reporting PASS.

Root and cluster independently read the complete exact source obstruction
in section 8 and reported PASS, including its all-low-degree positivity
and its restriction to coupon-uniform semisimple adapters. No runtime
experiment is used for that algebraic statement.
