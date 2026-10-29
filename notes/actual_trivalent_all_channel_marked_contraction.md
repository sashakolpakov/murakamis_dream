# The original marked two-vertex contraction in every channel

29 October 2026. The complete magnetic contraction of one actual black
vertex with its ordinary white vertex and the ORIGINAL physical marked
arc has a positive formula at every supported folded triple. This is a
coherent contraction, not a replacement of white by a Hermitian adjoint.
The paired circle is retained as a nilpotent coupon. Its first normal
and the normal required by the physical mark are included separately.

Write N>=2, d=N-1, M=floor(d/2), q=exp(pi i/N), Q=q^2,
F_u=(Q;Q)_u, s_u=|F_u| and x=q^d. For 0<=a,b,c<=M put

    J=a+b+c, delta=J-d,
    r=b+c-a, r1=a+b-c, r2=a+c-b.

Let L_j be the FULL c_j sector of the actual complete circle L_N,
where c_j=q^(2j+1)+q^(-2j-1). On the original nested six-head source
p_16 p_23 p_45, insert L_a,L_b,L_c on the three consecutive physical
pairs. Close with the two original ordinary caps and the original
unrestricted marked row specified in the
[actual vertex definition](actual_trivalent_complete_circle_vertex_kernel.md).
Denote this raw scalar by Z_N(a,b,c). No extra component normalization
is inserted.

Put k_j=2 for a paired node 2j<d and k_j=1 for the odd simple node
2j=d. Then Z_N(a,b,c)=0 for J<d. For J>=d it is EXACTLY

    Z_N(a,b,c)
      =N s_delta s_r s_r1 s_r2
         *product_j h0_j/(s_(2a)s_(2b)s_(2c)) *|A_N(a,b,c)|^2
      =N^2 k_a k_b k_c s_r s_r1 s_r2/s_delta
                                            *R_N(a,b,c)^2 >0. (1)

Here A_N and R_N are the proved actual scalar and positive factorial
partition in the
[all-channel source theorem](actual_trivalent_all_channel_positive_scalar_and_regular_cubes.md),
and

    h0_j=k_j N s_(2j)/s_j^2.                         (2)

All factorial indices in (1) lie in 0,...,d. At N=2 there are no
supported triples. Formula (1) is a local two-vertex source evaluation;
it is not an arbitrary-graph norm or a hyperbolic-volume identification.

## 1. Genuine duality, including the reversed label order

Use the original ordinary image Q_j, its full Clebsch columns W_j and
its positive single-object metric from the
[all-degree CD normalization](actual_trivalent_full_cd_normalization_and_magnetic_growth.md):

    G_(j,u)=s_(2j)/(s_u s_(2j-u)),
    pi_j=G_j^(-1) W_j^dagger P,
    L_j=h0_j W_j pi_j.                              (3)

On a paired axis pi_j W_j=0. On the odd simple axis it is I. Nothing
below uses a paired retraction or substitutes a value-only projector
for L_j.

For Q_j choose the canonical ordinary cup with first entry one:

    p^(j)_(u,2j-u)=(-1)^u q^[u(2j-u-1)]
                                      F_u F_(2j-u)/F_(2j),
    ell^(j)=(p^(j))^(-1).                           (4)

Its defining E,F equations follow directly from the displayed ratio.
The physical maps remain p_(u,v)=N x^(-v)delta_(u+v,d) and
ell_(u,v)=x^u/N delta_(u+v,d). The right dual of W_j is

    D(W_j)=(p^(j))^T W_j^T(ell^T tensor ell^T)P,
    D(W_j)=gamma_j pi_j,
    gamma_j=q^[2d^2-2dj-j^2-2j]/N^2
           =q^(2-j^2)/N^2.                         (5)

These are bilinear pivotal duals. To fix the scalar, take row0 and
physical input (d-j,0). The original lowest endpoint is
W_(j,2j)(d,j)=q^[d^2-dj-j^2], and p^(j)_(2j,0)=q^(-2j), giving
the first exponent in (5). Its difference from 2-j^2 is a multiple
of 2N. Both maps are actual integer-H intertwiners. Their homogeneous
Hom space is one-dimensional: after duality its highest vector lies
in the degree d-j E-kernel, whose first-order recurrence has all
interior arrows nonzero. This proves the all-input equality.

Also D^2(W_j)=(K_V^(-1) tensor K_V^(-1))W_j K_j=W_j, directly by
the cup matrices and K covariance. Thus D(pi_j)=gamma_j^(-1)W_j,
even when pi_j W_j=0.

Define the ordered black column and ordinary white row by

    U_abc=(pi_a tensor pi_b tensor pi_c)J_source,
    Lambda_abc=ell^S(W_a tensor W_b tensor W_c).

Right duality REVERSES the three object labels. The actual nested
matching is invariant under the six-head reversal, so

    Lambda_abc=gamma_a gamma_b gamma_c D(U_cba).     (6)

In particular a same-order adjoint cannot be inferred when labels
are unequal. Let Theta_abc be the genuine ordinary invariant normalized
by Theta_abc(2a,r,0)=1. The complete source theorem gives

    U_abc=s_abc Theta_abc,
    s_abc=N^3 A_N(a,b,c)/G_(b,r),
    s_cba=N^3 A_N(c,b,a)/G_(b,r1),
    G_(b,r1)=G_(b,r).                               (7)

All source phases in (7) are kept.

## 2. An own finite ordered theta evaluation

Temporarily use a generic parameter zeta, Q=zeta^2. Let the same
ordinary modules have highest weights 2a,2b,2c, and use the cups (4)
with q replaced by zeta. The canonical invariants are regular finite
Clebsch recursions, with denominators of index at most 2a,2b,2c.

The third-color-zero slice of Theta_abc is, for 0<=k<=r1,

    A_k=Theta_abc(2a-k,r+k,0)
       =(-1)^k zeta^[k(2a+1-k)]
                           F_(r+k)F_(2a-k)/(F_r F_(2a)). (8)

This follows by solving its first-order lowest F equation backward
from its stated corner. For the reversed tensor, the first color
2c is held fixed. Its E equation has just two terms, giving

    B_k=Theta_cba(2c,r1-k,k)
       =zeta^[2k(a-b)] A_k.                         (9)

There is no boundary term: the first E input would be color 2c+1.

Let T be the partial magnetic pairing of Theta_abc and D(Theta_cba)
over the first two objects. The invariant E equations imply K_c T
is scalar, as cleared equalities between adjacent diagonal entries.
At third color zero its scalar is zeta^(2c)T_00. Substituting (8),(9)
and the exact cups yields

    zeta^(2c)T_00
       =(-1)^r1 zeta^[4c-r1(r-1)] F_(2b)F_r2/(F_r F_(2a))
                                             *[J+1 choose r1]_Q. (10)

For completeness, the sole finite summation in (10) is

    sum_(k=0)^r1 Q^[k(r2+1)]
             [r+k choose k]_Q[2a-k choose r2]_Q
       =[J+1 choose r1]_Q.                          (11)

It is the coefficient of u^r1 in

    1/[(uQ^(r2+1);Q)_(r+1)(u;Q)_(r2+1)]
       =1/(u;Q)_(2c+2).

The reciprocal finite-product coefficient formula follows by
induction on its length; no theta or 6j evaluation is a premise.
Taking the pivotal trace of (10), and canceling its factor
1-Q^(2c+1) BEFORE specializing, proves the finite identity

    Xi_abc:=D(Theta_cba)Theta_abc
      =(-1)^r1 zeta^[2c-r1(r-1)]
          F_(2b)F_r2 F_(J+1)
                 /[(1-Q)F_r F_(2a)F_r1 F_(2c)].     (12)

This keeps both the ordered normalization and its root zero.

## 3. Retain the physical marked normal by a regular trace quotient

A regular generic lift of the physical W_j is explicit. Put t=d-j.
Its highest coefficients and actual divided descendants are

    h_u(zeta)=(-1)^u zeta^(-du)
      Q^[u(t-1)-u(u-1)/2](Q^(j+1);Q)_u F_(d-u)/F_d,
    W_(j,v)(zeta)=F_pair^v h(zeta)/F_v, 0<=v<=2j.   (13)

Its highest recurrence and the directly inductive E,F commutator give
its E,F,K covariance at every interior descendant. The final vector
F_pair^(2j+1)h is killed by E_pair by the same commutator. Its degree
is d+j+1>d, where E_pair is a rectangular bidiagonal matrix of full
column rank: starting at its boundary row eliminates each input in
turn, using only nonzero physical interior E arrows. Hence that
final vector is zero. This proves the last F endpoint as well, without
a generic decomposition theorem. All denominators in (13) have index <=d<N and are
units near the chosen root. At that root factorial reflection gives
exactly the original W_j. For the physical cup choose its generic
canonical formula with highest weight d and scale N zeta^(-d^2);
its root values are exactly the original p and ell.

Keep the ROOT gamma_j and h0_j fixed, and define

    pi_j(zeta)=gamma_j^(-1)D(W_j(zeta)).

Thus h0_j W_j(zeta)pi_j(zeta) is a regular Hopf coupon specializing
to the full actual circle sector (3), including its nilpotent value.
This is a regular lift for a FIXED-ROOT identity. It does not identify
the original moving-q germ with a projector or a new scalar germ.

By the original dual index contraction (6), the ordinary closed
generic physical source without the h0 factors is

    F(zeta)=gamma_a gamma_b gamma_c
                     s_abc(zeta)s_cba(zeta) Xi_abc(zeta). (14)

The source coefficients s(zeta) are holomorphic and their root values
are (7). Cut the ORIGINAL physical marked arc. The resulting map is
a regular scalar t(zeta)I on the generic physical highest-weight-d
module. Indeed its K eigenvalues are distinct and its interior F
arrows are nonzero, so commuting with K,F forces a scalar. Direct
cup/cap multiplication gives

    ell p^T=(-1)^d K_V,
    F(zeta)=(-1)^d[N]_zeta t(zeta).                 (15)

At the root this is exactly the original pivot K^(1-N), since
K^N=(-1)^d I. The original unrestricted marked row has m p=1, hence
the marked closure is t(q). The mark has stayed on the physical
V_N component; no paired-image projection is used to move it.

For J>=d, J+1=N+delta<2N. The numerator F_(J+1) in (12) has EXACTLY
one root zero, and all displayed denominator factorials are units.
Since

    F_(J+1)/(1-Q^N) -> N F_delta,

equations (12),(15) give the finite, nonzero normal quotient

    eta_abc=lim_(zeta->q) Xi_abc/[(-1)^d[N]_zeta]
      =(-1)^(r1-d)q^[2c+d-r1(r-1)]
          N F_delta F_(2b)F_r2/[F_r F_(2a)F_r1 F_(2c)]. (16)

This quotient retains the physical marked normal. Because Xi has a
simple zero, derivatives of the holomorphic source coefficients in
(14) make no contribution to the limit. The full paired-circle CD
normal was already included in h0 and is not substituted for this
different normal operation.

## 4. Full phases and the positive answer

Combining (7),(14)--(16), the marked scalar including all three
circle sectors is

    Z_N=product_j h0_j
       *q^[6-a^2-b^2-c^2] A_N(a,b,c)A_N(c,b,a)
                                      *eta_abc/G_(b,r)^2. (17)

The two actual corner magnitudes are equal. Their ordered source
phases satisfy

    phase(A_abc A_cba)
       =q^[2a^2+2c^2-2ac-2J-6].

Substitute F_u=(-i)^u q^[u(u+1)/2]s_u in (16). The net F-index
difference is -d. Combining it with (17) leaves the phase

    (-1)^(r1-d) i^d q^[N(N-2J-1)/2]=q^(-2Nc)=1.

Its remaining magnitude is

    N s_delta s_(2b)s_r2/[s_r s_(2a)s_r1 s_(2c)].

Use G_(b,r)=s_(2b)/(s_r s_r1). This proves the first equality in
(1). The independently proved scalar formula
|A_N|=s_a s_b s_c R_N/(N s_delta) and (2) give its second equality.
No phase, paired multiplicity or factor of N has been dropped.

As normalization checks, the odd simple triple a=b=c=(N-1)/2 gives
Z=N^3|A|^2. For even N=2m>=4 and a=b=c=m-1, it gives
Z=8N^3|A|^2/cos(pi/N), exactly the separately proved
[even central normal contraction](actual_even_central_black_white_marked_contraction.md).

There is also an explicit marked co-source identity. With the original
unscaled W-coordinate packet Vm and the independently normalized
Theta_abc used above, contracting all magnetic indices gives

    sum_magnetic Theta_abc overline(Vm_abc)
      =N^5 s_delta s_r2/[s_(2a)s_(2c)] overline(A_N(a,b,c)). (18)

Indeed the literal vertex normalization is
Z=(product h0_j/N^7)sum U_raw overline(Vm)/product G, while
U_bal=N^3 A Theta/G_(b,r). Substitution of (1) proves (18).
This is a specified linear functional of the entire magnetic tensor,
not equality of the marked co-source and an adjoint on other inputs.

For literal signed edge twists R^(e_i)L_(j_i), multiply (1) by
product_i omega_(j_i)^(e_i), where

    omega_j=kappa(-1)^j q^[j(j+1)], kappa=q^(d^2/2).

This follows on the full root block since its nilpotent circle kills
the additional normal term of R. It is not a stripped-Cartan phase.
The coherent sum over different triples can then have cancellations.
For three UNTWiSTED full complete circles the source is the sum of
the positive terms (1); that statement concerns this specified
two-vertex wiring only. Any external original line factor stays
outside the raw scalar.

## 5. What this theorem does and does not estimate

The extra growth of the black magnetic tensor is contracted BEFORE
an estimate. Its compensation here is supplied by the genuine white
duality and the physical marked normal, not by bounding white in a
Euclidean norm. Formula (1) supplies an exact positive partition for
this local marked two-vertex source. It does not make the marked
white tensor an adjoint on arbitrary exteriors, prove a tensor-product
metric compatible with general recoupling, or identify its factorial
action with the volume of a graph complement.

The [focused exact audit](../experiments/audit_actual_trivalent_all_channel_marked_contraction.py)
checks all folded triples at ten physical levels N=2,...,11, every
original Clebsch dual, reversed-label ordinary white and unrestricted
marked contraction. A separate generic audit checks (10),(12) on
all 65 admissible spin triples <=4 and all covariances of eleven regular
physical lifts. Direct ungrouped original physical sources include
both parities, unequal labels, genuine full-normal circle summands
and signed Cartan crossings, in eighteen closures. These tests supplement the finite
Vandermonde, duality and regular-trace proof above.

An independent analytical reader rederived the ordered magnetic
recursions, Vandermonde, generic endpoint, all-label normal quotient
and exact remaining phase, and reported PASS. A separate fresh replay
of the audit also passed. These are internal proof reviews, not
external peer review.
