# Odd spectral regularization has the same full shared entropy

31 October 2026. All derivatives here
are SPECTRAL derivatives at the fixed original root. No genuine-q normal
is obtained by differentiating a root-only identity. The actual positive
coupon below includes the semisimple derivative data of the full V.

## 1. Exact odd normalization and one comparison block

Let N=2m+1>=3, d=2m, theta=pi/N. On the literal polynomial source block
z^j, 0<=j<=d, write A=2+Omega, with diagonal and lowering coefficients

    a_j=2+c_j=4cos^2((j+1/2)theta),
    s_j=2sin(j theta),
    A z^j=a_j z^j-s_j^2(x+y)z^(j-1)
                         -s_j s_(j-1)xy z^(j-2).

The sole zero diagonal is a_m=0. All other diagonals and all allowed
lowering weights are positive. The original endpoint zeros are retained.
Let

    P_N(u)=H_(V_N(-2-u)), P0=P_N(0), Q=P_N'(0),
    F_N=V_N(-2)-N^(-2) V_N'(-2),
    H_(F_N)=P0+N^(-2)Q.                              (1)

V_N is the [full original polynomial numerator](actual_gaussian_resolvent_numerator_and_cap.md)
chi_N(sigma)/(sigma-Omega),
chi_N=2T_N(sigma/2)+2. The second prime in (1) differentiates sigma;
the Q prime differentiates u. Thus the minus sign in F_N is literal.

The unused-row product expansion gives nonnegative coefficients of
P_N(u) in u,x,b,c,y. At odd N its full diagonal product is

    product_j(a_j+u)= -chi_N(-2-u)
                    =2cosh(N theta_u)-2,
    theta_u=arccosh(1+u/2).

Its first two Taylor coefficients give exactly

    product_(j!=m)a_j=N^2,
    sum_(j!=m) a_j^(-1)=(N^2-1)/12.                  (2)

Replace ONLY the zero central diagonal of A by a_m^*=N^(-2), keeping
all lowering coefficients and other diagonals unchanged. Call this
positive triangular block Atilde, and let Ktilde be the homogeneous
polynomial of Atilde^(-1). It is a comparison kernel, NOT asserted to
be a covariant physical coupon. Its full diagonal product equals1.

Split the coefficient Q according to whether its underlying path
visits m. Write Q_skip for the paths not visiting m. The unused-row
formula and (2) give EXACTLY

    Ktilde=P0+N^(-2)Q_skip,
    0<=Q-Q_skip<=((N^2-1)/12)P0.

The second inequality is coefficientwise: on each path visiting m,
the derivative adds the sum of reciprocal UNUSED noncentral diagonals.
Consequently the ACTUAL polynomial coupon has the finite comparison

    Ktilde <= H_(F_N) <= (13/12)Ktilde.              (3)

In particular both have every degree-d monomial, with positive
coefficient. One may also see this by the path consisting entirely
of one-steps. No spectral projector has been substituted for V'.

## 2. Exact half and cross pieces of Ktilde

As usual an input j and output i contribute b^i c^(d-j), with total
outer degree j-i. Partition its full monomial support into

    left: c>=m+1; right: b>=m+1; cross: b,c<=m.      (4)

For a left coefficient i<=j<=m-1 no path visits m. Define Q_ij by
the ACTUAL lower-block recurrence

    Q_ii=1,
    Q_ij=(s_j^2/a_j)(x+y)Q_(i,j-1)
                  +(s_j s_(j-1)/a_j)xyQ_(i,j-2),

with the missing second term zero. Then the coefficient at
x^k b^i c^(d-j)y^(j-i-k) is EXACTLY

    a_i^(-1)[x^k y^(j-i-k)]Q_ij.                    (5)

The right piece is its literal row-reflection b<->c; the steps and
diagonals have this exact symmetry.

Every cross path either visits m or skips it by the unique two-step
m+1->m-1. Replace that skipped step by the two one-steps through m.
Since xy <= (x+y)^2/2 coefficientwise, its weight is at most

    [1/(2N^2 s_m s_(m+1))] times the repaired path.  (6)

The repair is injective and its endpoints are unchanged. The paths
visiting m have EXACTLY the P0 weights because the new reciprocal
central diagonal is N^2. Therefore

    P0 <= Ktilde_cross
              <=[1+1/(2N^2 s_m s_(m+1))] P0.        (7)

The same visited-central path split gives an exact factorization

    P0=N^2 D_m(x,b,y)D_m(x,c,y),                    (8)

with D_m monic of degree m in its middle variable. This is also the
actual odd simple-fold factorization (the sine beta_m equals1). It
can be proved without a value-only interpolation: split each original
path at m and reflect its upper part. If
D_m(x,b,y)=sum_i b^i G_i(x,y), then G_m=1 and, for i<m,

    G_i=[s_m^2(x+y)Q_(i,m-1)
                +s_m s_(m-1)xyQ_(i,m-2)]/a_i,      (9)

where a nonexistent Q term is zero. Equations (5)--(9) retain every
physical endpoint and every finite outer unit.

## 3. Uniform CLOSED coefficient entropy on the shifted odd mesh

The [closed half-block proof](actual_fejer_half_block_entropy.md)
applies to (5), with the following explicit
checks rather than an inference from a weighted limit. For j<=m-1,

    a_j=4sin^2((m-j)theta),
    s_j=2sin(j theta).

On any fixed interior interval j/N in [eta,1/2-eta], the recurrence
coefficients converge uniformly to the SAME positive monomer/dimer
coefficients, with Perron root

    L^2-(x+y)tan^2(pi t)L-xy tan^2(pi t)=0.

The corresponding normalized Jacobi recurrence has positive, uniformly
bounded interior coefficients and hence the same bounded negative-root
and Bernoulli local coefficient estimate. The boundary estimates also
remain unchanged in order: for j near0, s_j is comparable to j/N;
for r=m-j near0, a_j is comparable to (r/N)^2, with r>=1. Thus removing
eta N endpoint indices costs at most

    O(eta N log(1/eta)+log N)

in the monomer products and upper bounds. There is no zero coefficient
inside either lower half. The all-monomer x/y choices realize every
outer degree, including the extreme coefficients. These are precisely
the ingredients of the closed proof: finite-tilt compact-cover upper
bounds, trim/fill lower bounds at endpoints, the interior coefficient
estimate on the trimmed interval, and the collapsing-interval bound.
They prove uniformly for ALL 0<=i<=j<=m-1 and 0<=k<=j-i

    N^(-1)log([x^k y^(j-i-k)]Q_ij)
                     =E(i/N,j/N,k/N)+o(1).          (10)

The factor a_i^(-1) has logarithm O(log N), uniformly. Formula (9)
then gives the same uniform TRIANGLE coefficient entropy for D_m.
For i<m its first term supplies every permitted k by choosing x or y;
one of k or k-1 lies in [0,m-1-i]. All arguments in (10) differ by
O(1/N) from the desired endpoint E(i/N,1/2,k/N). The second term only
adds another argument with the same O(1/N) displacement. Their finite
positive weights have polynomial upper/lower bounds. Closed continuity
therefore proves the upper and lower limits uniformly. The corner i=m
is the exact coefficient1 and entropy zero.

Normalize all local exponents by d=2m. For D_m each triple divided by d
has sum1/2; changing i/N,k/N to i/d,k/d changes them by O(1/N).
Thus its absolute limit is the ALREADY normalized

    C(alpha)=E(alpha_b,1/2,alpha_x)=V(2pi alpha)/(2pi).

The positive convolution (8), with O(N) summands and integer split
endpoints, has the same uniform cross entropy max(C+C). Equations
(5) and (7), closed continuity at both seams and the constant comparison
(3) now prove, for every degree-d local exponent n,

    N^(-1)log [L^n]H_(F_N)=h(n/d)+o(1)              (11)

UNIFORMLY on the full closed simplex. This is the same h as the even
full Fejer theorem, not only its positive-radius weighted maximum.

## 4. Actual shared coefficient and full complex spectral disks

For a fixed original certified flat plat retain its original ordinary
targets d and protected targets0. The actual polynomial coupon F_N in
(1) is admissible in the original homogeneous compiler. By positivity,
(11), and unrestricted integral flow rounding, its whole shared source
satisfies

    N^(-1)log Z_(D,N;F_N at every port) -> W_D.       (12)

Here W_D is EXACTLY the same finite-dimensional full h maximum as at
even levels. The separate [even endpoint volume theorem](general_fejer_endpoint_source_volume.md) therefore
identifies W_D=Vol(Y_D)/(2pi). No odd identity-deletion or geometric
reconstruction has been inferred by differentiating an even statement.

For u>=0 define C_N(0)=1 and

    C_N(u)=product_(j!=m)(1+u/a_j)
      =[sinh(N theta_u/2)/(N sinh(theta_u/2))]^2
      <=exp((N-1)theta_u).                          (13)

The product of UNUSED noncentral ratios on any path is at most C_N(u).
Visiting-central paths start from P0; skipping paths have their one
central factor u. Consequently the exact positive path comparison is

    P_N(u)<=C_N(u)[P0+u Q_skip]
           <=C_N(u)max(1,N^2u) H_(F_N).             (14)

For arbitrary complex sigma the source-proved factorwise majorant is
|H_(V_N(sigma))|_coef<=P_N(|sigma+2|). Multiplying (14) at all original
ports and taking the UNCHANGED shared marked coefficient bounds the
absolute full numerator contraction by

    Z_(D,N;F_N) product_e
       {exp((N-1)theta_(u_e)) max(1,N^2u_e)},
    u_e=|sigma_e+2|.                                (15)

In particular it has upper rate at most W_D+sum_e arccosh(1+u_e/2)
on fixed bounded spectral disks, and upper rate at most W_D uniformly
on ANY shrinking polydisks |sigma_e+2|<=r_N->0. This includes all actual
semisimple numerator data. Cauchy estimates may be applied to spectral
derivatives with their stated disk-radius cost; they are not genuine-q
normal estimates. No Gaussian contour selection, complement estimate,
or nonzero filling-cycle contribution is concluded here.

## 5. Exact whole-source spectral jets, both parities

Let S_N(sigma_1,...,sigma_R) be the ENTIRE shared contraction of the
original V_N numerators, with the original homogeneous face targets
and protected zero specialization. Use F_N from (1) at odd levels and
F_N=-V_N(-2)=P_N at even levels. For each variable choose the actual
Cauchy radius r=N^(-2). The elementary inequality cosh t>=1+t^2/2
gives

    arccosh(1+1/(2N^2))<=1/N,
    max(1,N^2r)=1.

At odd levels (14)--(15) therefore bound |S_N| on the whole polydisk
by e^R Z_(D,N;F_N). At even levels the exact unused-factor comparison
instead has factor

    product_j(1+r/a_j)=cosh^2(N theta_r/2)<=exp(N theta_r)<=e,

at every port, and gives the SAME bound. Cauchy's formula yields for
every multiindex alpha the finite all-parity estimate

    |partial_sigma^alpha S_N(-2,...,-2)|
       <= e^R alpha! N^(2|alpha|) Z_(D,N;F_N).       (16)

There is no unspecified exponential constant in (16): its right side
is the actual positive shared source whose rate is W_D. This includes
the full spectral semisimple derivatives at the parabolic endpoint.
It does not identify these spectral jets with genuine-q normal jets,
and it does not select any Gaussian or filling cycle.

## Validation and scope

The [focused audit](../experiments/audit_actual_fejer_odd_regularized_full_numerator.py)
and its [results](../experiments/actual_fejer_odd_regularized_full_numerator_results.json)
independently construct V and its SPECTRAL derivative on the original
coproduct matrices. They compare 3,672 physical-grid entries, including
1,200 wrong-unwrapped-total zeros, and six whole original marked F_N
sources. Four literal simple-fold factorizations retain the root scalar.
The 75-digit positive checks cover 2,510 derivative paths, 1,035 full-
support coefficient comparisons, 783 central-cross repairs and 3,105
spectral-radius coefficient bounds. The maximum identity error is below
3.90e-73. These are exact-source/formula checks, not numerical proofs
of the uniform entropy limit or of the volume theorem.

Root the full analytical proof through section4
and supplied/checked the exact whole spectral-jet corollary. Geometry
the full proof, including every closed-coefficient
and seam argument, then the complete audit code and freshly
replayed it with redirected output. Geometry also separately checked
section5's all-parity Cauchy constant. Public promotion changes only
links, formatting and file-relative audit paths; its author replay
reproduced the same counts and errors. No genuine-q normal, Gaussian
contour selection or nonzero filling-cycle claim is part of this result.