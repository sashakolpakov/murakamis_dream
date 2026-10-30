# The original matching-edge block, its row measure, and its boundary cost

30 October 2026. This is an exact four-port rewrite of ONE matching
edge of the original complete-circle source, at every level parity.
It retains the physical cups, the categorical dual, the fixed gamma
factor, every new recoupling channel, and the whole-network first normal.
The original circle measure cancels the exponential row normalizer.
The remaining estimate separates a positive scalar from an explicitly
specified target tensor and complementary-network cost.

This is not a positive norm formula for the completed block or a
full-source volume bound. The retained half-twist phases, high-channel
Laurent terms, and surrounding contraction are not discarded.

## 1. The actual typed block and its natural bend

Use the conventions of the
[full matching-graph source](general_matching_graph_full_normal_source.md).
Put d=N-1, q=exp(pi i/N), zeta=q exp(t), and 0<=a<=floor(d/2).
The matching object has highest weight E=2a. The two physical objects
have highest weight d. Write W_a=W_dd^(2a), with its first highest
entry one, and use the ACTUAL physical cup and inverse cap

    pV(u,d-u)=N zeta^(-d^2) (-1)^u
                 zeta^[u(d-u-1)] F_u F_(d-u)/F_d,
    ellV=pV^-1, F_r=(zeta^2;zeta^2)_r.                    (1)

The ordinary channel cup p_E has first coefficient one. Keep

    gamma_a=q^(2-a^2)/N^2                              (2)

as a FIXED root constant. The regular generic lift of the original
root channel is exactly

    pi_a=gamma_a^-1 p_E^T W_a^T
                       (ellV^T tensor ellV^T) P,
    K_a=W_a pi_a,                                      (3)

where P reverses the two physical heads. No inverse of pi_a W_a
is used: that root composition is zero on every paired sector.
This is the allowed regular Hopf lift of the root map, not an assertion
that its entire moving-q germ equals the original circle's germ.

For an operator K on V_d tensor V_d define the cup bend by

    B(K)=K(pV tensor pV)P,
    B(K)_(a,b,c,e)=sum_(u,v) K_(a,b;u,v) pV(u,e)pV(v,c),
    B^-1(Psi)=Psi P(ellV tensor ellV).                  (4)

Thus the four outside ports are ordered a,b,c,e. This is the actual
reversal already present in (3), not a permutation chosen to improve
a recoupling coefficient. Every external object is V_d, independently
of the ribbon order elsewhere in the matching graph.

The exact generic identity is

    B(K_a)=gamma_a^-1 S_(2a),
    S_(2a)=W_a p_E W_a^T.                              (5)

Here is the sign and scale check. Canonical cups satisfy

    ell_A^T p_A=(-1)^A K_A^-1,
    p_A^T=(-1)^A p_A K_A.

Scaling p_A and inversely scaling ell_A leaves the first identity
unchanged. The two physical (-1)^d signs therefore cancel in (4).
Hopf covariance gives W_a K_E=(K_d tensor K_d)W_a, so the remaining
factor is p_E^T K_E^-1=p_E because E=2a is even. This proves (5)
with the physical scale in (1), before specialization.

## 2. The exact recoupling and the unchanged marked normal

The [generic all-port theorem](actual_general_four_port_single_racah_kernel.md)
now applies with A=B=C=D=d. Its actual target tensor includes the turn

    T_(2g)(u,v,w,z)=(-1)^d zeta^(d-2u)
        [(W_dd^(2g) tensor W_dd^(2g))p_(2g)](v,w,z,u).

Consequently

    K_a=gamma_a^-1 sum_(g=0)^d
                              L_(2g,2a) B^-1(T_(2g)).  (6)

All g=0,...,d are present. In particular the high targets 2g>=N
are genuine meromorphic generic tensors. They are not removed using
the root folded-channel range of the ORIGINAL matching edge.

Fix all other original matching labels. After (6) is inserted into
the actual network, denote its ordinary generic closure functional
on the four-port operator by C(t). It includes the original outside
ordering and bends. Keep the original exposed mark on a physical
edge. The proved whole-network identity first replaces that marked
scalar by the normal of its ORDINARY closure:

    Z_Delta(a,others)=nu_N^-1 [t^1] C(t)(K_a(t)),
    nu_N=2N(-1)^N/(q-q^-1).                            (7)

The functional C is holomorphic because its remaining original
coupons and physical cups/caps are regular. Equation (7) is not
obtained by moving a bare marked row through a local cap. It follows
from the ordinary whole-network trace D_N(t) times a regular open
scalar, exactly as in the full matching-graph theorem.

For the original complete circle the outside scalar remains

    h0_a=k_a N s_(2a)/s_a^2,
    k_a=2 if 2a<d, k_a=1 if 2a=d,
    omega_a=q^(d^2/2)(-1)^a q^[a(a+1)],
    s_r=product_(v=1)^r 2sin(pi v/N).                   (8)

The coupon's signed half twist contributes omega_a^epsilon. Its
unit absolute value does not authorize removing its phase from
the sum over a.

## 3. The original measure cancels the row gauge

Write the genuine seven-factorial Racah sum as S_ag and put

    G_ag=(-1)^d S_ag/[N]_zeta,
    R_N(a,g)=G_ag(q)>0.                                (9)

The division is in each original summand. The
[matching-edge scalar theorem](actual_matching_edge_racah_positive_scalar.md)
proves analyticity, the positive formula

    R_N(a,g)=sum_(r=max(0,a-g))^(min(a,d-g))
        [s_(g+r)/(s_(g+r-a)s_r s_(a-r))]^2,             (10)

and fixed generic jet bounds polynomial times R_N(a,g). Its full
generic germ is tail-free: the original numerator never reaches [2N].

The actual source coefficient, with all boundary products as defined
in the all-port theorem, is

    L_(2g,2a)=rho_a G_ag h_g,
    rho_a=(-1)^d [N]_zeta chi_(2a) X_(2a)/S0,
    h_g=1/(b_(2g) J_(d-g) V_(d-g)).                    (11)

In particular h_g depends on g,N,t but NOT on a. Its b,J,V are the
actual first-entry and Casimir products, not a chosen orthogonality
measure. For completeness, with n=d-g and Q=zeta^2,

    S0=[2d+1]!/([d-a]!^2[a]!^2),
    V_n=zeta^n (Q^(-d-g-1);Q)_n /
                  [(Q;Q)_n^2 (Q^(-2d-1);Q)_n],
    J_n=zeta^[-n(d+1)] F_d^2/F_g^2,
    b_(2g)=(-1)^d zeta^(d-2g) h_dd^(2g)(d-g)
                    (-1)^(d-g) zeta^[-d^2+2d(d-g)-(d-g)(d-g+1)],
    h_dd^(2g)(r)=(-1)^r zeta^[r(d-2g-r-1)]
                             F_(g+r)F_(d-r)/(F_g F_d). (12)

The target product also has the exact symmetric-factorial form

    h_g=(-1)^d zeta^(g^2+d)
       [g]!^2[d-g]!^2[2g+1]![2d+1]! /
                       ([d]!^2[d+g+1]!^2).            (12a)

One can check (12a) directly by writing each negative Pochhammer
in (12) as a ratio of F-factorials; the residual zeta exponent is
g^2+d. If a_src(g)=chi_(2g)X_(2g)/S0 denotes the generic row
formula, continued through the entire target range, this gives

    a_src(g) h_g=[2g+1](Delta_g^2)^2,
    [N]^2 a_src(g) h_g=[2g+1]D_g^2.                   (12b)

Here Delta_g and D_g are the actual face factors of the scalar
theorem, with D_g(q)=1. Thus even the target normalization is a
specified boundary product. Equation (12b) is a generic bilinear
identity, not positivity of the completed root channel measure.

There is an especially useful exact simplification of the row:

    chi_(2a) X_(2a)=(-1)^d zeta^[2a(a-d)-d]
                                 F_d^2/(F_(d-a)^2 F_(2a)),
    rho_a=zeta^(-a^2-d)
          [d]!^2[a]!^2 / ([2a]! ([2d+1]!/[N])).         (13)

To check the exponent independently, converting the displayed F ratio
to symmetric factorials contributes 2da-3a^2; adding 2a(a-d)-d
gives -a^2-d. The powers of 1-Q cancel. At the root,

    [2d+1]!/[N]=(-1)^d[d]!^2,
    rho_a(0)=(-1)^d q^(-a^2-d) s_a^2/s_(2a),
    h0_a gamma_a^-1 rho_a(0)
                       =(-1)^d k_a N^3 q^(-d-2).       (14)

Thus the row's exponential factorial cost cancels against the
ORIGINAL circle measure. This is not an adjusted normalization.
Let u_a(t)=rho_a(t)/rho_a(0). All factors of (13), after its one
[N] cancellation, are root units. The same elementary harmonic
product bound used for (9) proves, for each fixed m,

    |[t^m]u_a(t)| <= C_m P_N^m,
    |[t^m]G_ag(t)| <= C_m P_N^m R_N(a,g),
    P_N=N^2(1+log N),                                 (15)

uniformly in every allowed a,g. This retains the actual generic
derivatives; root equality of partner values is not differentiated.

## 4. The full first-normal formula and the precise bound it gives

Set

    H_g(t)=t h_g(t) T_(2g)(t).                         (16)

Every H_g is holomorphic. Indeed h_g has a simple pole exactly
when 2g<d, while the target cup can have a simple pole only when
2g>=N. These ranges are disjoint. The Clebsch factors in T have
the regular canceled physical coproduct expressions. This is the
simple-pole result of the matching-edge scalar theorem, now with
the actual typed source interface included.

Combining (6)--(16) gives the exact original weighted sector

    h0_a omega_a^epsilon Z_Delta(a,others)
      =(-1)^d k_a N^3 q^(-d-2) omega_a^epsilon/nu_N
         *sum_(g=0)^d [t^2]
              {u_a(t) G_ag(t) C(t)(B^-1(t)H_g(t))}.    (17)

Only Taylor orders zero, one and two of each regular factor in (17)
are needed. The regular full source requires a first normal; the
second-order budget in (17) is exactly the cost of its singular
recoupling coordinates. No termwise root evaluation replaces it.

Here is one explicit bound, in the standard physical basis. Use the
Hilbert--Schmidt norm for four-port matrices and its dual for C, and
define the N-dependent quantities

    J_C=max_(0<=m<=2) ||[t^m]C(t)||,
    J_g=max_(0<=m<=2) ||[t^m]H_g(t)||_HS.              (18)

They are finite, fully specified ORIGINAL tensor and complement
costs. They are not postulated to be subexponential. At the root each
nonzero entry of pV has magnitude N, since s_u s_(d-u)=N. Therefore

    ||B^-1(0)||_(HS->HS)=N^-2,
    ||[t^m]B^-1(t)||_(HS->HS)<=C_m N^-2 P_N^m
                                      (0<=m<=2).       (19)

The second bound follows directly from the nonzero cup entries in
(1) and their harmonic logarithmic derivative bounds. Thus the
physical cup scale contributes no exponential cost. Expanding (17),
using (15),(18),(19), and noting |nu_N|=N/sin(pi/N), gives

    |h0_a omega_a^epsilon Z_Delta(a,others)|
       <= C k_a sin(pi/N) P_N^2 J_C
                            sum_(g=0)^d R_N(a,g) J_g.  (20)

The constant is universal for these fixed jet orders. Weighted
Cauchy also gives

    sum_g R_N(a,g)J_g
       <= (sum_g R_N(a,g))^(1/2)
                              (sum_g R_N(a,g)J_g^2)^(1/2). (21)

Equations (20),(21) are source-exact upper estimates with every
boundary cost displayed. They do not define a positive root inner
product on the original paired-nilpotent channels. Summing them over
a and the other original labels retains all their original scalar
weights and yields an upper bound, not a lower bound or a nonvanishing
statement. Retaining the phases in (17) is necessary for an equality.

## 5. What this resolves and the remaining costs

The prescribed-pair geometric localization can put both exceptional
facets at the ends of this ONE matching edge. Its four outside
objects are then all V_d, so (5)--(20) apply at arbitrary plat width.
A main-edge pair does not have this automatic all-physical port type.

The exceptional scalar is positive, tail-free, and polynomially
stable at all fixed generic jet orders. The original row measure and
physical bend introduce no exponential loss. The remaining local
cost J_g consists exactly of the target normalization h_g and the
regularized target tensor, through order two. The complement cost
J_C consists of its actual contraction and derivatives, also through
order two. No theorem here controls those costs sharply by the
geometric action. In particular the remaining vertices are not
automatically in the central selected-kernel domain merely because
their weaker support defects have been localized elsewhere.

A full-source volume argument still requires such a coherent bound
and a nonzero selected contribution with its physical cycle. The
explicit row cancellation and finite Laurent budget remove two
particular normalization obstacles; they do not supply that cycle.

Audit: [actual typed bend, original measure, and full recoupling](../experiments/audit_actual_matching_edge_marked_four_port_block.py).
The focused audit passed 30 generic physical matrix families and all
154 target coefficients, comparing 32,114 original operator entries;
19 actual root bend first-jet families, comparing 64,882 jet entries;
239 canceled row germs with 956 retained coefficients; and 54 target
normalizers against their original boundary products. Odd pivotal-sign
regressions and paired-nilpotent sectors are included. These finite
checks supplement the generic tensor and harmonic-product proofs.

Two independent analytical reviews passed the typed bend, original
cup signs and gamma, both product normalizers, exact circle-measure
cancellation, whole-network normal extraction and Taylor-two budget,
and the norm factors in (19),(20). One reviewer also independently
replayed the full focused audit and reproduced all reported counts.
The reviews retain the stated complete-circle scope and the explicit,
uncontrolled native target and complement costs. No positive completed
Hermite metric or full-source asymptotic is inferred.
