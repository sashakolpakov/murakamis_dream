# Genuine scalar normals have vanishing exponential cost near the closing point

30 October 2026. The original Casimir
polynomial and every fixed genuine moving-q derivative have an absolute
upper bound of vanishing exponential rate on an ENTIRE small complex
disk about z=2. This is larger than the shrinking zero-free disk of the
[endpoint theorem](actual_matching_edge_polynomial_endpoint_control.md).
Zeros may occur in the present fixed disk; no relative lower bound or
canonical logarithm is asserted there.

Use N>=3, d=N-1, q=exp(pi i/N), zeta=q exp(epsilon), Q=zeta^2 and
`0<=a<=floor(d/2)`. All polynomials and face factors are the original
generic ones, before extracting any source normal.

## 1. All spectral denominators cancel in the finite Sears expression

In the exact generic endpoint formula put

    z=Z+Z^-1,
    A=zeta^-1 Z^-1 Q^-d,
    B=zeta^-1 Z Q^(-d-a).

The two spectral-dependent series denominators there are EXACTLY

    C=zeta Z Q^(d+1-a)=A^-1 Q^(1-a),
    zeta Z Q^(-d-a-1)=B.

For the kth term, finite product reversal gives

    (A;Q)_a/(C;Q)_k
       =(-1)^k A^k Q^[k(2a-k-1)/2](A;Q)_(a-k),
    (B;Q)_a/(B;Q)_k=(BQ^k;Q)_(a-k).

Consequently the exact source polynomial is the finite sum

    p_a(zeta,Z+Z^-1)=sum_(k=0)^a T_k(zeta,Z),

    T_k=(-1)^k A^k Q^[k(2a-k+1)/2]
       *(Q^-a;Q)_k^2 (zeta Z;Q)_k^2
       *(A;Q)_(a-k)(BQ^k;Q)_(a-k)
       /[(Q;Q)_k^2(Q^-d;Q)_a(Q^(-d-a-1);Q)_a].      (1)

The exponent of Q is an integer. Every denominator in (1) depends
ONLY on Q and is a root unit in this actual range. Thus (1) is valid
even when an uncanceled spectral denominator in the preceding Sears
presentation vanishes. Each T_k is a Laurent polynomial in Z of
degrees between -a and a, with regular generic-q coefficients.
The full sum is the already proved polynomial in z; this assertion
does not require any symmetry of an individual summand.

At zeta=q,Z=1 the exact endpoint convolution says

    T_k(q,1)=b_k^2 b_(a-k)^2>0,
    b_n=product_(r=1)^n sin((r-1/2)pi/N)/sin(r pi/N),
    sum_k T_k(q,1)=p_a(q,2),
    1/(4a+1)<=p_a(q,2)<=1.                         (2)

## 2. A uniform absolute bound on a fixed small disk

There are absolute constants c,C,r0>0 such that for 0<r<=r0,

    |p_a(q exp(epsilon),z)|
       <=p_a(q,2) exp[C N sqrt(r) log(2+1/r)+C log N],
    |epsilon|<=c N^-3, |z-2|<=r.                   (3)

In particular the upper exponential rate in (3) tends to zero as
r decreases to zero, uniformly in the original row and both parities.

Here is the estimate from the actual finite terms. Choose a solution
of Z+Z^-1=z with `|Z-1|<=C sqrt(r)`, and take r0 small enough that
|Z-1|<1/2. No holomorphic choice of this root over the disk is made.
The identity (1) is pointwise valid for either solution.

The denominators, Q-only numerator factors and q monomials in (1)
have relative logarithmic change `O(N^2(1+log N)|epsilon|)`.
Their factors have nonzero root exponent distances, and the harmonic
bound is the same one proved for the endpoint unit products. A factor
with Z dependence in its NUMERATOR instead satisfies

    |1-zeta^m Z^e|/|1-q^m|
        <=1+C N (|Z-1|+N|epsilon|)/dist(m,2NZ),

where e=+1 or -1 and |m|<=4N. At the base point these distances are
the nonzero odd distances 1,3,... in consecutive intervals. They
occur with uniformly bounded multiplicity. The separate factor Z^-k
costs at most exp(CN|Z-1|).

For v>=0 the elementary integral comparison gives

    sum_(j=1)^N log(1+Nv/j)
      <=N[log(1+v)+v log(1+1/v)]
      <=C N v log(2+1/v),                         (4)

with value zero at v=0. The first inequality uses the decreasing
integrand log(1+Nv/x) on (0,N]. Apply (4) with
`v=C(|Z-1|+N|epsilon|)`. The extra N|epsilon|<=cN^-2 costs at most
O(log N); the same is true of the Q-only changes. We obtain a bound
for EACH term, uniform in k,

    |T_k(q exp(epsilon),Z)|
      <=T_k(q,1)
         exp[C N sqrt(r) log(2+1/r)+C log N].        (5)

Summing (5) uses the exact positive endpoint weights in (2). There is
no replacement by a separately maximized summand, and no additional
number-of-terms cost is required. This proves (3), including points
where numerator factors vanish. Lower bounds away from z=2 are not
part of this argument.

## 3. Genuine q jets and fixed spectral derivatives

For each fixed nonnegative integer m, Cauchy on the SAME generic
epsilon disk proves

    sup_(|z-2|<=r) |partial_epsilon^m p_a(q exp(epsilon),z)|_(epsilon=0)
       <=C_m N^(3m) p_a(q,2)
             exp[C N sqrt(r) log(2+1/r)+C log N].   (6)

This differentiates (1), an identity of the original generic source.
It does not differentiate a root-only positive replacement.

For any additionally fixed spectral order s, applying Cauchy on a
disk of radius r inside |z-2|<=2r gives

    sup_(|z-2|<=r) |partial_epsilon^m partial_z^s p_a|_(epsilon=0)
       <=C_(m,s) r^-s N^(3m) p_a(q,2)
             exp[C N sqrt(r) log(2+1/r)+C log N],   (7)

after changing C and restricting r<=r0/2. For fixed r, the factor
r^-s has zero N-exponential rate. The tiny-endpoint theorem remains
available if a chosen r itself shrinks so quickly that (7) is not
the useful form of the bound.

The original face scalar D_a and its inverse remain uniformly bounded
on this epsilon disk by their canceled root-unit product estimate.
Thus (3),(6),(7) also apply to the actual normalized scalar
`D_a^-1 p_a`, with adjusted constants and the corresponding genuine
product derivatives.

## 4. The bound is for a closing region, not for a contributing cycle

The estimates allow the scalar factor and all fixed required normals
to be bounded throughout a small closing region, rather than just
at the point 2 or on a fixed compact of its limiting slit plane.
They make no claim that this region is zero-free: the scalar roots
are above 2 and can enter a fixed disk as N grows.

The actual resolvent still has its own nearby spectral poles. Any
bound on a closing part of the original contour must combine (6)
or (7) with its actual resolvent estimate and retain the permitted
contour and all residues. The present theorem by itself neither
selects that contour nor proves geometric saddle dominance or a
nonzero source contribution.

Focused audit: [canceled original Sears terms, removable spectral
denominators and genuine joint jets](../experiments/audit_actual_matching_edge_polynomial_closing_region_bound.py).

The closing-region bounds do not give a zero-free fixed disk or identify a contributing contour.