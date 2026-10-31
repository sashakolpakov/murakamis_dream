# Polynomial control through the target spectral endpoint two

30 October 2026. The actual exceptional
Casimir polynomial has a positive finite convolution at z=2. Its value
is between an explicit reciprocal polynomial and one. An exact generic
Sears representation then controls the whole polynomial, including its
genuine moving-q derivatives, on a shrinking joint neighborhood of
this endpoint. No contour deformation or saddle contribution is proved.

Use the original polynomial p_a(zeta,z) from the
[generic source identity](actual_matching_edge_geometric_target_polynomial.md),
with N>=3, d=N-1, q=exp(pi i/N), theta=pi/N and
`0<=a<=floor(d/2)`. Every occurrence of a moving-q derivative below
means zeta=q exp(epsilon), with the spectral variable z held fixed.

## 1. An exact positive endpoint convolution

Define

    b_n=product_(r=1)^n sin((r-1/2)theta)/sin(r theta), b_0=1.

Then the actual root polynomial satisfies

    p_a(q,2)=sum_(k=0)^a b_k^2 b_(a-k)^2.             (1)

In particular

    1/(4a+1)<=p_a(q,2)<=1.                          (2)

Here is a finite proof retaining the source normalization. At the root,
the polynomial's generic 4phi3 becomes, at z=2,

    4phi3(Q^-a,Q^(a+1),q,q; Q,Q,Q; Q,Q), Q=q^2.

Apply the proved finite Sears identity with length a, retained parameter
q, and d_S=e_S=Q. The result has numerator parameters
`(Q^-a,Q^-a,q,q)`, denominators `(Q,qQ^-a,qQ^-a)`, and prefactor

    (q,qQ^-a;Q)_a/(Q,Q^-a;Q)_a=b_a^2.

All denominators are units; the half-integer sine factors are never
zero. The kth transformed term is

    [(b_(a-k)/b_a)b_k]^2.

All q powers and signs cancel, giving exactly (1). This is an identity
of the actual source polynomial, not a lower estimate based on a
different factorial model.

Since `sin x/x` decreases and sin x increases on (0,pi/2),

    (r-1/2)/r <= sin((r-1/2)theta)/sin(r theta)<=1.

Thus `b_a>=product_(r=1)^a(r-1/2)/r`. The square of that last product
is at least `1/(4a+1)`: induction uses

    (2a+1)^2(4a+5)-(2a+2)^2(4a+1)=1.

Keeping k=0 in (1) proves the lower bound in (2). The upper bound
follows from the already proved simple roots `rho_h>2`, since

    p_a(q,2)=product_h (rho_h-2)/(rho_h-2cos theta)<=1.

## 2. An independent quantitative separation of the roots

The source Jacobi theorem gives

    J_a-2I=2 H D_a H+2sin^2(theta/2)D_a,

where D_a is its positive matrix and H its sine diagonal. The D_a
here is a MATRIX, not the scalar face factor. Its inverse has exact
entries, indexed 1<=k,l<=a,

    (D_a^-1)_(k,l)=(-1)^(k+l)
       sqrt[sin((2k-1)theta)sin((2l-1)theta)]
                         *sum_(m=max(k,l))^a cot(m theta).       (3)

For a direct proof, the elementary LDL^T pivots and lower entries are

    delta_m=sin(m theta)/[cos(m theta)sin((2m-1)theta)],
    L_(m,m-1)=sqrt[sin((2m-3)theta)/sin((2m-1)theta)].

Their inverse products telescope. Substituting them into
`L^-T diag(delta_m^-1)L^-1` proves (3). Summing its diagonal and using
`sum_(k=1)^m sin((2k-1)theta)=sin^2(m theta)/sin theta` gives

    Tr D_a^-1=sin(a theta)sin((a+1)theta)/(2sin^2 theta)
                                                   <=1/(2sin^2 theta).

Hence every source-polynomial root satisfies the uniform separation

    rho_h-2 >= 4sin^2(theta/2)sin^2 theta >= c N^-4.  (4)

The case a=0 has no roots. Equation (4) is useful by itself, but it
does not supply a moving-q estimate; that requires the actual generic
representation below.

## 3. A generic positive-at-the-root representation

Keep zeta generic and put Q=zeta^2, z=Z+Z^-1. The original polynomial
is the finite series with numerator parameters
`(Q^-a,Q^(a+1),zeta/Z,zeta Z)` and denominator parameters
`(Q,Q^-d,Q^(d+2))`. Apply the same own Sears identity, now retaining
zeta Z and choosing d_S=Q, e_S=Q^-d. It gives the exact GENERIC identity

    p_a(zeta,Z+Z^-1)=P_a(zeta,Z)
       *4phi3(Q^-a,Q^-a,zeta Z,zeta Z;
              Q,zeta Z Q^(d+1-a),zeta Z Q^(-d-a-1);Q,Q),

    P_a=(zeta^-1 Z^-1 Q^-d,zeta^-1 Z Q^(-d-a);Q)_a
                         /(Q^-d,Q^(-d-a-1);Q)_a.     (5)

At zeta=q,Z=1, the terms INCLUDING P_a are the positive summands
of (1). The identity is generic before taking any normal. In particular
its derivatives are not obtained by differentiating the root convolution.

There are absolute constants c,C>0 such that, uniformly in every
allowed a,N,

    |p_a(q exp(epsilon),z)/p_a(q,2)-1|<=1/2
       if |epsilon|<=c N^-3 and |z-2|<=c N^-4.       (6)

Here is an explicit estimate. Each nonzero factor in each summand of
(5) is `1-zeta^m Z^e`, with |m|<=4N and e in {-1,0,1}, or the
unit monomial Q^k. At the base point its distance from zero is at least
a constant times its distance in exponent from 2NZ divided by N.
The half-integer factors in the Q notation correspond to ODD integer
powers of zeta; they stay separated from every even multiple 2N.
All other factors in the finite range also avoid those multiples.

Summing logarithmic changes along each consecutive product gives

    |change log(summand)|
       <=C[N^2(1+log N)|epsilon|+N(1+log N)|Z-1|].  (7)

This includes the prefactor, not merely the residual series. The
bound uses a harmonic sum of reciprocal nonzero exponent distances;
the product multiplicities are uniformly bounded. Taking
`|epsilon|<=c N^-3`, `|Z-1|<=c N^-2` and decreasing c makes every
summand a relative perturbation of its positive root value by, say,
one quarter. Their sum obeys the same relative bound, without paying
the number of terms or allowing cancellation of large terms.

For every `|z-2|<=c' N^-4`, one solution of Z+Z^-1=z satisfies
`|Z-1|<=c N^-2`, since `(Z-1)^2/Z=z-2`. Apply the preceding pointwise
estimate to it. The polynomial is already holomorphic in z; a global
choice of this square root is neither needed nor made. This proves
(6), after adjusting the absolute constants.

## 4. All fixed genuine jets have polynomial endpoint cost

Multivariable Cauchy applied to (6) proves, for every fixed r,s>=0,

    |partial_epsilon^r partial_z^s p_a(q exp(epsilon),z)
                                           evaluated_(0,2)|
          <= C_(r,s) N^(3r+4s) p_a(q,2).             (8)

The same bound holds on a fixed smaller joint disk with an adjusted
constant. By (2), the function and its inverse therefore have only
polynomial cost there, and a holomorphic logarithm exists on that
product disk. The actual scalar face factor D_a is a product of root
units after its displayed [N] zero is canceled, and D_a(q)=1. The same
harmonic product estimate bounds D_a and its inverse on the WHOLE
epsilon disk in (6), which is contained in their earlier uniform unit
disk of radius c/[N^2(1+log N)]. Thus the statement also applies on
the same joint disk to the original normalized scalar `D_a^-1 p_a`.

These bounds cover the polynomial through the endpoint z=2 while the
Casimir poles approach it. They retain both level parities and every
original generic coefficient. The resolvent factor in the exact operator
period, its own poles and normals, and the actual contour contribution
still require their respective estimates. Neither (6) nor (8) moves a
contour or proves dominance of its geometric saddle.

Audit: [original endpoint convolution, generic Sears germ and joint disk](../experiments/audit_actual_matching_edge_polynomial_endpoint_control.py).
It passes 426 exact generic Sears comparisons, 210 joint root four-jet
identities, 1,679 actual endpoint/convolution/lower-bound comparisons,
eight inverse-trace and root-gap matrices, and 104 genuine generic
joint-disk samples at 100 digits. The uniform bounds follow from the
displayed finite formulas and harmonic estimates, not from those samples.


The endpoint estimates do not deform contours or establish source-saddle dominance.