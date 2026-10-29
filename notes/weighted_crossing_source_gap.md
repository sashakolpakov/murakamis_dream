# Weighted complete-crossing norms and the actual Green-source gap

28 October 2026. The ORIGINAL complete crossing has a uniform compact
variational formula for its exponential norm in real boundary metrics.
At the flat metric its unique maximum is the regular octahedral point
and its rate is 2 Catalan/pi. The COMPLETE Green source, including its
carry, has a much smaller explicit metric exponent. This proves an
open weighted operator-norm gap for both signs.

This is a norm comparison. It does not assert noncancellation of the
original closed scalar period or replace the actual exterior source
by a norm-maximizing vector.

The [audit](../experiments/audit_weighted_crossing_source_gap.py)
and [results](../experiments/weighted_crossing_source_gap_results.json)
check literal weighted R/source norms, endpoint-uniform factorial
estimates and signed metric-rate diagnostics. The weighted optimizer
in that script is a diagnostic; the rigorous variational formula,
flat maximum and explicit gap chamber are proved below.

## 1. The actual coefficient and metric

Put q=exp(pi*i/N), Q=q^2, x=-q^(-1), F_k=(Q;Q)_k and d=N-1.
The exact positive Green reconstruction, with original unit scalar
kappa retained, has input (a,b), output (a+b-j,j), and coefficient

    kappa*x^(-b-j)Q^(jb)
           F_(a+b-j)F_a/[F_(a-j)F_bF_j],              (1)

when 0<=j<=a<N, 0<=b<N and a+b-j<N; otherwise it is zero.
Every displayed factor is nonzero on this range. This is the
ORIGINAL crossing coefficient, independently checked against its
gate word, not a positive surrogate.

Give input and output basis vectors real exponential metrics

    W_in|a,b>=exp(rho_a*a+rho_b*b)|a,b>,
    W_out|c,e>=exp(rho_c*c+rho_d*e)|c,e>,
    R_(+,rho)=W_out R_+ W_in^(-1).                    (2)

Set

    p=rho_c-rho_a, q_w=rho_c-rho_b,
    r=rho_d-rho_a.

The symbol q_w is a REAL weight, distinct from the root q. With
alpha=(a-j)/N, beta=b/N, gamma=j/N, the exact boundary-metric
exponent in (1) is N(p alpha+q_w beta+r gamma).

## 2. Uniform factorial and Laplace estimates

Define the continuous function

    J(s)=integral_0^s log(2 sin(pi t))dt, 0<=s<=1.

Uniformly for 0<=k<N,

    log|F_k|=N J(k/N)+O(log N).                       (3)

One direct proof writes log(2 sin(pi t))=log t+log(1-t)+b(t),
where b extends smoothly to [0,1]. Stirling bounds on the two finite
factorial sums give O(log N) uniformly, including k=0 and k=N-1;
the smooth remainder has bounded Riemann-sum error. Thus no fixed
distance from a factorial endpoint is needed.

Let

    D={alpha,beta,gamma>=0:
                           alpha+beta<=1, alpha+gamma<=1},
    f=J(alpha+beta)+J(alpha+gamma)-J(alpha)-J(beta)-J(gamma),
    M(p,q_w,r)=max_D [f+p alpha+q_w beta+r gamma].       (4)

Then for EVERY compact real metric set K,

    log||R_(+,rho)||_HS=N M(p,q_w,r)+O_K(log N).        (5)

The same formula holds for operator norm, with another O_K(log N).
Indeed the positive sum of squared matrix entries lies between its
largest summand and N^3 times that summand. Equation (3) approximates
each logarithm by the phase in (4) with O(log N) error. Conversely
shrink any point of D by 1-1/N and round its coordinates DOWN to
the 1/N grid. The resulting physical indices obey both upper bounds
N-1 and lie O(1/N) away. The uniform modulus of continuity of J is
O(eta(1+|log eta|)), so the maximal phase changes by O_K(log N/N).
This proves the uniform two-sided estimate (5). Finally
||R||_op<=||R||_HS<=N||R||_op, so their rates agree.

There is also an exact finite separable formula useful for computation.
Set

    A_N(k;s)=sum_(t=0)^(d-k) |F_(k+t)/F_t|^2 exp(2s t).

Then the ACTUAL weighted squared HS norm is exactly

    ||R_(+,rho)||_HS^2=sum_(k=0)^d |F_k|^(-2) exp(2p k)
                                      A_N(k;q_w)A_N(k;r). (5a)

This takes O(N^2) positive real operations without evaluating a
new invariant or assuming that the original scalar sum is positive.

For the negative crossing the exact balanced antiunitary identity is
R_-=P overline(R_+)P, including its original Cartan phase. Therefore
(5) applies with both input weights and both output weights swapped:

    p_-=rho_d-rho_b, q_-=rho_d-rho_a,
    r_-=rho_c-rho_b.                                 (6)

No factorial metric conversion is used. All estimates are uniform
on compact sets and hold for the literal two signs.

## 3. The unique flat maximum and its value

For fixed 0<alpha<1 put g_alpha(t)=J(alpha+t)-J(t).
On 0<t<1-alpha,

    g_alpha'=log[sin(pi(alpha+t))/sin(pi t)],
    g_alpha''=-pi sin(pi alpha)
                         /[sin(pi(alpha+t))sin(pi t)]<0.

Thus the unique maximizers in beta and gamma at zero weights are
both (1-alpha)/2. The mean of log(2 sin(pi t)) is zero and
J(1-s)=-J(s). The reduced maximum is consequently

    F(alpha)=-4J((1-alpha)/2)-J(alpha),
    F'(alpha)=log cot(pi alpha/2).                     (7)

It increases to alpha=1/2 and decreases afterward; its endpoint
values are zero. Hence the unique maximum on the ENTIRE domain is

    (alpha,beta,gamma)=(1/2,1/4,1/4),
    M(0,0,0)=-4J(1/4)=2G/pi,                         (8)

where G=sum_(n>=0)(-1)^n/(2n+1)^2 is Catalan's constant. To obtain
the last equality independently, expand log|1-r exp(2*pi*i*t)| for
r<1, integrate its absolutely convergent Fourier series, and let
r tend to one in L^1. This gives J(1/4)=-G/(2*pi).

Equivalently 2G/pi=v_8/(2*pi), where v_8=4G is the volume of the
regular ideal octahedron. Only the explicit Catalan value is needed
for the norm theorem. In particular

    log||R_+||=log||R_-||=N*(2G/pi)+O(log N).           (9)

The maximizing Hessian is
-pi[[2,1,1],[1,2,0],[1,0,2]], negative definite. Thus the maximum
and M vary smoothly for sufficiently small weights. No global
concavity for arbitrary weights is assumed.

## 4. A one-dimensional computation for arbitrary real weights

For every 0<alpha<1, strict concavity gives the exact inner optima

    beta_*(alpha;q_w)
       =Arg(exp(-q_w)-exp(-pi*i*alpha))/pi,
    gamma_*(alpha;r)
       =Arg(exp(-r)-exp(-pi*i*alpha))/pi.               (10)

Both lie strictly between zero and 1-alpha. Thus M is the maximum
over the SINGLE interval alpha in [0,1] of (4) evaluated at (10).
Its endpoint values are max(0,q_w)+max(0,r) at alpha=0 and p at
alpha=1. This is an explicit computable variational problem, including
weighted maxima that reach the boundary. Uniqueness is not asserted
for arbitrary weights.

## 5. Sharp complete Green-source exponent with its carry retained

Use the actual COMPLETE Green source L=G_out+G_in+G_top from
[the sharp endpoint theorem](actual_crossing_shared_face_fourier_source.md#9-exact-flat-metric-norm-of-the-complete-green-source).
This is the weighted crossing source of that theorem, NOT the
unweighted exponentially large fusion-ground channel H_m. Its exact
complete coefficients are unit phases on the following supports:

* G_out maps (a,b) to(a+b,0), a>=1 and a+b<N.
* G_in maps (a,0) to(a-e,e), 1<=e<=a<N.
* G_top is one rank-one block on pair degree N, with input(a,N-a)
  and output(N-e,e), 1<=a,e<N, and unit-modulus input/output factors.

Put L_rho=W_out L W_in^(-1). For either operator or HS norm,

    log||L_rho||=N delta(rho)+O_K(log N),
    delta(rho)=max(0,max(rho_c,rho_d)-min(rho_a,rho_b)). (11)

Here is the full endpoint proof. The rank-one carry has norm equal
to the product of its weighted vector norms. Its output components
have magnitudes exp[rho_c(N-e)+rho_d e], and its input covector
components exp[-rho_a a-rho_b(N-a)]. The allowed grids approach both
ends within 1/N, so its logarithmic norm is
N(max rho_out-min rho_in)+O_K(log N), uniformly even at tied weights.

The ground-output triangular support gives rate max(0,p,q_w).
The ground-input triangular support gives rate max(0,p,r). The
degree-one ground entry supplies the lower rate zero even if every
metric difference is negative. Both triangular rates are at most
delta. Different total-degree blocks isolate the top carry, and
different second-output supports isolate the two lower-degree ground
terms, so cancellation cannot remove the maximal component. Projection
onto those supports bounds each component by the whole operator;
the reverse bound is their triangle sum. This proves (11), including
the carry and BOTH ground sources. The same assertion for HS follows
also by their disjoint matrix-entry supports. Negative crossing sources
are transported by the same flip-conjugation; delta is unchanged by
the swaps, proving (11) for both signs.

The norms of the COMPLETE Green source are only polynomial at the
flat metric. The carry fixes the sharp positive exponent when output
radii dominate input radii. It has not been omitted as a negligible
degree-N correction.

## 6. An explicit open radius chamber for the relative source norm gap

Evaluate (4) at its unweighted maximizing point. This gives

    M_+(rho)>=2G/pi+L_+(rho),
    L_+=(3rho_c+rho_d-3rho_a-rho_b)/4,
    M_-(rho)>=2G/pi+L_-(rho),
    L_-=(rho_c+3rho_d-rho_a-3rho_b)/4.                 (12)

Consequently the following strict, explicit piecewise-linear chamber
contains the flat metric:

    delta(rho)<2G/pi+min(L_+(rho),L_-(rho)).             (13)

On every compact subset with a margin eta>0, equations (5), (6),
and (11) prove for BOTH crossing signs

    ||L_(sigma,rho)||/||R_(sigma,rho)||
                                      <=N^C exp(-N eta). (14)

One convenient radius cube is |rho_i|<=epsilon, with

    0<epsilon<G/(2*pi).

Then delta<=2epsilon and L_+,L_->=-2epsilon. Hence (14) holds
uniformly with any eta<2G/pi-4epsilon. The fixed explicit choice
epsilon=1/10 even permits eta=4/25 without relying on a decimal
evaluation: the alternating series gives G>8/9, and pi<22/7 implies
2G/pi-2/5>82/495>4/25. A common additive shift of all four
rho_i leaves every comparison unchanged, so this can also be viewed
as a chamber of radius RATIOS rather than a fixed overall scale.

These are relative operator/HS norm gaps for the actual sourced
crossing equation. Contracting through the rest of a knot can select
a subspace far below the norm-maximizing octahedral profile. No scalar
volume limit or source-angle lower bound follows from (14) alone.
