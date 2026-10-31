# Genuine numerator normals at positive-total framing boundaries

30 October 2026. A uniform spectral gap
for the SUM of the two original positive matrices controls the actual
generic numerator in both the202 and222 boundary regimes. The actual
total square root and every logarithmic head lift remain in the source
normalization. Near the fold, all fixed genuine quantum derivatives
have subexponential relative cost when the partner separation satisfies
s log N=o(N).

This is a numerator theorem. It does not assign a generic amplitude
to a root collision or prove a global source period. The separate
root222 determinant action and the root202 coefficient packet retain
their own normalizations and hypotheses.

## 1. An exact uniform gap, including the folded endpoint

Let theta=pi/N, N>=3, and 1<=a<=floor((N-1)/2). Use the actual
Hermitian H_-,H_+ from the
[source determinant](actual_q_hahn_full_physical_complex_packet.md),
with diagonal d_r=1/[cos(r theta)cos((r+1)theta)] and upper entries

    sqrt(B_n)[sin(n theta) +/- i cos(n theta)],
    B_n=sin^2(n theta)/[cos^2(n theta)
                      sin((2n-1)theta)sin((2n+1)theta)].

Then EXACTLY

    H_-+H_+ >= cos(theta) I >= I/2.                      (1)

Here is a direct weighted-path proof. Put J=(H_-+H_+)/2 and
w_r=sqrt(sin((2r+1)theta)), 0<=r<a. Alternating-sign conjugation
turns its real offdiagonal e_n=sqrt(B_n)sin(n theta) negative.
For an interior row r, subtracting its two weighted neighbors from
the diagonal gives

    d_r-e_r w_(r-1)/w_r-e_(r+1)w_(r+1)/w_r
       = [sin(r theta)cos(r theta)/(1+sin(r theta))
          +sin((r+1)theta)cos((r+1)theta)
                                      /(1+sin((r+1)theta))]
                                      /sin((2r+1)theta)
       >= cos(theta)/2.                                 (2)

For the equality, use sin((2r+1)theta)=sin(r theta)cos((r+1)theta)
+sin((r+1)theta)cos(r theta). For the inequality, bound both
denominators 1+sin by 2 and use
sin(r theta)cos(r theta)+sin((r+1)theta)cos((r+1)theta)
=sin((2r+1)theta)cos(theta).

The r=0 formula has its left term zero. At the final row r=a-1,
subtracting the finite positive quantity
sin^2(a theta)/[cos(a theta)sin((2a-1)theta)] from the ACTUAL
one-neighbor residual gives exactly the expression in (2). Thus
that actual residual is larger. This last comparison does not
introduce a virtual B_a or w_a: at the maximal odd fold those
separate quantities would be singular or zero. All weights and
coefficients actually used in the matrix are positive. For a=1
the same finite comparison applies with no actual neighbor.
Finally, for x_r=w_r y_r the quadratic form is the
sum of e_n w_(n-1)w_n |y_n-y_(n-1)|^2 and the weighted residual
diagonal terms. Thus (2) proves J>=cos(theta)I/2 and hence (1).
No limiting matrix or unproved eigenvalue asymptotic is used.

## 2. The actual total phase and the two boundary domains

Fix the actual logarithmic heads sigma,u and put, GENERICALLY,

    q=q0 exp(epsilon), Q=q^2, B=Q^-N,
    U=q^(2u), V=q^(2(sigma-u)), b=q^sigma,
    X=qU, Y=qV, T=XY=q^2UV,
    w=qb=q^(sigma+1), z=b/U.

In particular T=w^2 and z/w=1/X exactly. The square root w is
the original exponential, not a freely chosen branch. At the root,
the exact normalized source is

    H_n^1(U,V)=(qUV)^n K_n det M_n,
    M_n=X^-1 I-H_-/2-H_+/(2T),                         (3)

where K_n=[2n choose n]_Q for the small channel n and the matrices
are its n-row truncations. Indeed the original monic determinant is
R_n(z)=det[zI-(wH_-+w^-1H_+)/2]; divide its matrix by w and use
H_n=b^n K_n R_n. Thus the factor w^n, including its sign and every
integer logarithmic character, is retained in (qUV)^n.

For physical half-index heads write X=exp(2pi i x), Y=exp(2pi i y),
sigma=N(x+y)-1. Then w=exp(pi i(x+y)) exactly. On the canonical
physical logarithms, when T is positive and both arguments lie
strictly between 0 and 2pi, their sum is 2pi and w is the NEGATIVE
square root of T. The same sign persists in that marked neighborhood.
If another actual integral lift changes this sign, (3) retains the
change; none of the estimates below replaces it by the canonical sign.

Let T at epsilon=0 range in a sufficiently small fixed complex
neighborhood of a compact subset of (0,infinity). Two domains are
allowed:

* 202: X/N^2 belongs to a fixed compact subset of C*.
* 222: X belongs to a fixed compact neighborhood of a negative real
  compact subset of C*.

Require the marked heads to satisfy |sigma|+|u|<=C N(1+log N).
These are conditions on the actual arguments, not on an arbitrarily
reset logarithm. In202, Y=T/X is small; in222 both raw finite
clocks are near negative reals. The
[actual prefix-sign theorem](actual_right_angled_resonant_prefix_signs.md)
supplies precisely these limiting signs where its dictionary applies.

For all sufficiently large N, on both domains the matrix in (3) satisfies

    Re(-M_n)>=cI,     ||M_n^-1||<=C,                   (4)

uniformly for all small n through the fold. Indeed Re(1/T)>=eta>0,
and (1) bounds H_-+eta H_+ below by a fixed positive multiple of I.
For202 the term 1/X is O(N^-2), so it cannot close that gap. For222,
Re(1/X)<0 adds a positive diagonal term. Thus the root numerator is
nonzero. This proof retains the additive identity term and does not
infer an inverse bound from positivity alone.

## 3. A genuine generic disk and its cofactor

The all-degree original generic recurrence, with B=Q^-N retained, is

    R_(n+1)=(z+alpha_n)R_n+beta_n R_(n-1).

Its coefficients and rational all-degree proof are in the
[actual paired-normal theorem](actual_q_hahn_near_fold_complex_partner_bound.md).
Here the generic scalar is
K_n(q)=(B^2Q^(n+1);Q)_n/(BQ;Q)_n, whose root value is the
Gaussian binomial in (3). Its generic derivatives are not those of
that root simplification. Set G_n=R_n/w^n. As exact generic identities,

    G_(n+1)=(X^-1+alpha_n/w)G_n+(beta_n/w^2)G_(n-1),
    H_n^B(U,V)=(qUV)^n K_n G_n.                         (5)

For n<=a the nonzero original spectral differences are bounded
below by cN^-2 on a small polynomial disk. Here b and w are bounded
above and away from zero; their derivatives have size O(N log N).
The quotient formulas for alpha_n,beta_n therefore give

    (alpha_n/w)'=O(N^5(1+log N)),
    (beta_n/w^2)'=O(N^7(1+log N)).                       (6)

The original b_n,d_n in those formulas are O(1), with derivatives
O(N(1+log N)); the preceding u_n and v_n have sizes O(N^2),O(N^4).
This gives (6) directly, with no generic specialization of a root
reflection. The derivative of X^-1 is no larger than O(N log N)
in either domain and is smaller in202.

For each edge of the actual root matrix M_a, freeze whichever of its
upper and lower entries has larger absolute value. Their SUM is

    -sqrt(B_n)sin(n theta)(1+T^-1).

Since sqrt(B_n)>=1/2 and |1+T^-1| is bounded below, the frozen
entry has absolute value at least c/N for every n=1,...,a-1.
The first bound follows directly from
sin((2n-1)theta)sin((2n+1)theta)<=sin^2(2n theta)
and the displayed formula for B_n.
Keep it in its original orientation and put the other generic entry
equal to -beta_n/(w^2 frozen_entry). The diagonal is X^-1+alpha_n/w.
At the root this is exactly M_a, with all edge phases intact. At
generic q its determinant and every leading principal minor are
exactly the recurrence in (5), since each adjacent product is the
original one. No constant choice of upper versus lower is required,
and no parameter-dependent similarity is silently dropped.

By (6) this generic matrix differs from its root by
O(N^8(1+log N)|epsilon|) in operator norm. Choose

    |epsilon|<=rho_N=cN^-10.                            (7)

Equations (4),(6) give uniformly bounded inverse and two-sided
determinant ratio. Indeed the logarithm of the determinant ratio
costs at most O(N^9(1+log N)rho_N), which is bounded and tends to
zero. The last diagonal inverse entry is the actual cofactor, so

    |G_(a-1)/G_a|<=C.                                  (8)

The exact source scalar K_a has logarithmic derivative O(N^3),
and (qUV)^a has logarithmic derivative O(N^2(1+log N)). Their
two-sided ratios are bounded on (7). Thus the small H_a itself
has bounded two-sided relative variation on this disk.

## 4. The actual large partner and every fixed normal

Let m=d-a, s=m-a, with 0<=s<=eta N and eta sufficiently small.
The literal root identity is H_m^1=P_s(UV)H_a^1, where
P_s(UV)=product_(r=a)^(m-1)(UV-Q^r). Since UV=q0^-2T is near a
positive real compact and these r lie near N/2, every added factor
is bounded above and away from zero. In particular H_m^1 is nonzero.

On the boundary of (7), the original folded spectral differences
are at least c rho_N; all others are at least cN^-2. The original
generic recurrence coefficients alpha_n/w and beta_n/w^2 are
therefore at most C rho_N^-1 and C rho_N^-2. Starting from (8),
propagating the s rows costs at most (CN^20)^s.

The exact generic K_m/K_a ratio has 2s numerator factors and 2s
denominator factors. Those denominator indices stay near N/2,
so the ratio costs only C^s. The factor (qUV)^s also costs C^s
relative to the retained root P_s(UV). Thus on the circle, and
then throughout its disk,

    |H_m^B(U(q),V(q))/H_m^1(U(q0),V(q0))|
                        <=C(CN^20)^s.                  (9)

The passage inside uses the original finite H_m sum: all its
generic factorial denominators have indices below N and are units
on this disk. Singular monic R_m factors were never assigned a
holomorphic root value. Cauchy's formula now gives, for each fixed k,

    |partial_epsilon^k H_m^B|_0
       <=C_k N^(10k)(CN^20)^s |H_m^1(U(q0),V(q0))|.     (10)

For s=0 this follows directly from the small determinant argument.
For bounded s the cost is polynomial, covering both maximal folded
parities. For s log N=o(N) it is subexponential. This does not cover
a fixed nonzero scaled partner separation and does not give a
nonzero leading normal amplitude. The source factor (qUV)^n, the
integer characters and every marked head are retained before taking
the derivative.

The result applies to the individual actual202/222 numerator factors.
Any surrounding white monomials, cups, pivots, marks and finite support
cycles must still use their literal source identities and their own
estimates. Neither the positive gap nor finite-jet control selects
the original global relative period.

Focused audit: [positive-total source and retained-normal checks](../experiments/audit_actual_q_hahn_positive_total_boundary_normals.py),
with [saved results](../experiments/actual_q_hahn_positive_total_boundary_normals_results.json).
The 120-digit run checks both exact trigonometric identities, 389 actual
weighted rows including 24 finite last-row comparisons, 24 folded matrix
gaps, 12 original root phase/determinant identities, 48 original generic
determinants and 48 cofactors, 48 actual large-partner generic-circle
values and 24 first/second normals. Four cases have one root edge
EXACTLY zero and retain the opposite edge. Twelve tests keep identical
root clocks but change sigma to sigma+N; their genuine first normals
differ, verifying why marked lifts cannot be reset. Maximum source
error was below 3.3e-119. These finite checks supplement the proof;
they do not establish its uniform estimates by numerical sampling.

The result remains the stated individual-numerator, shrinking-channel normal bound; no leading normal amplitude, whole-network contraction estimate or global relative-cycle coefficient is inferred.