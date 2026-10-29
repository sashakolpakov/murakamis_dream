# Polynomial-cost inversion of the actual two-head Ward current

28 October 2026. The actual two-head lowering current admits a uniformly
polynomial inverse on the orthogonal complement of its exact kernel,
at EVERY total integer degree. This is a statement in the original
Euclidean head metric, uniformly on compact meridian annuli. It does not use the potentially
exponentially conditioned fusion matrix to estimate an inverse.

In particular, a local current equation cannot introduce an extra
exponential loss merely through its inversion. Kernel and cokernel
charges remain explicit. Neither this fact nor nilpotence of the
current proves that the whole knot's selected geometric contribution
is nonzero.

## 1. The actual current and the bound

Fix N>=2, Q=exp(2pi i/N), d=N-1, and x!=0. In the balanced
physical basis the current is

    F |a,b> = (1-Q^(a+1)) |a+1,b>
                   + x^-1 Q^a (1-Q^(b+1)) |a,b+1>,       (1)

where arrows outside 0,...,d vanish. This is the actual coproduct
current F_1+K_1^-1 F_2 in the fusion conventions of
[the original kernel](fusion_canonical_chart_and_retained_source_wall.md).
Let H_s be the span of a+b=s, and F_s:H_s -> H_(s+1).

For every nonzero F_s, all its nonzero singular values obey

    sigma >= min(1,|x|^-1) 2 sin(pi/N)/N.                (2)

Consequently its Moore--Penrose inverse satisfies

    ||F_s^+|| <= max(1,|x|) N/[2 sin(pi/N)]
                                      <= max(1,|x|) N^2/4. (3)

Here the last inequality is sin(pi/N)>=2/N. F_(2d)=0 has
zero pseudoinverse; its kernel is retained, not inverted.
In particular this is uniform on every fixed compact meridian annulus.

## 2. Unitary reduction to a weighted path

The only nonzero entries of F_s are on two adjacent diagonals.
Their bipartite support graph is a path. Independent unitary phases
on its row and column vertices therefore make all entries real,
with opposite signs on the two diagonals: choose one vertex phase
and propagate along the path. There is no loop consistency condition,
and these changes of frame have norm and inverse norm exactly one.

For 0<=s<=N-2, F_s^* is unitarily equivalent to A_L with L=s+1.
For N-1<=s<=2N-3, F_s is unitarily equivalent to A_L with
L=2N-2-s. In both cases 1<=L<=N-1, and

    (A_L f)_i = a_i f_i-b_i f_(i+1), 0<=i<L,
    a_i=2sin(pi(L-i)/N), b_i=2sin(pi(i+1)/N)              (4)

when |x|=1. For general x, multiply a_i by |x|^-1 in the
lower-degree case, and b_i by |x|^-1 in the upper-degree case.

At |x|=1, for the lower degrees the coefficient on row a=i is
|1-Q^(s-i+1)|=a_i, and on row a=i+1 it is b_i.
For the upper degrees put a=s-d+i. The output degree starts
at a=s-d+1, so each row has the two coefficients

    |1-Q^(s-d+i+1)|=2sin(pi(L-i)/N),
    |1-Q^(d-i)|=2sin(pi(i+1)/N),

as claimed. In particular every coefficient in (4) is at least

    a_min=min(1,|x|^-1) 2sin(pi/N).                     (5)

The adjoint reduction in the lower degrees preserves nonzero
singular values; it is not a replacement of the original current
by another quantum operator.

## 3. A unimodal exact kernel supplies a spectral estimate

The row rank of A_L is L, and its kernel is spanned by the positive
vector eta defined by eta_0=1 and

    eta_(i+1)/eta_i=a_i/b_i.

Equivalently,

    eta_i= r^i |(Q;Q)_L/[(Q;Q)_i (Q;Q)_(L-i)]|,        (6)

where r=|x|^-1 for the lower-degree case and r=|x| for the
upper-degree case.

The ratios are nonincreasing in i. One direct verification extends
the ratio to real i and differentiates its logarithm:

    d/di log[sin(pi(L-i)/N)/sin(pi(i+1)/N)]
      = -(pi/N) sin(pi(L+1)/N)
           /[sin(pi(L-i)/N)sin(pi(i+1)/N)] <= 0.         (7)

Thus eta, and hence the probability weights

    p_i=eta_i^2 / sum_j eta_j^2,

are unimodal. They may have very different magnitudes; no lower
bound on every p_i is assumed. The constant ratio factor r does
not change (7). When L=N-1 the ratios are constant; the kernel is
uniform when |x|=1.

Set

    w_i=a_i^2 p_i=b_i^2 p_(i+1),
    P_i=sum_(j<=i) p_j.

Unimodality gives

    min(P_i,1-P_i) <= (L+1) max(p_i,p_(i+1)).            (8)

Indeed before a mode the prefix is at most (i+1)p_i; at or
after a mode the suffix is at most (L-i)p_(i+1). Together with
(5), this implies

    w_i >= [a_min^2/(L+1)] min(P_i,1-P_i).              (9)

For a complex-valued function g on the path, the exact variance
identity and Cauchy--Schwarz along each interval give

    Var_p(g)=sum_(i<j) p_i p_j |g_i-g_j|^2
       <= L sum_(r=0)^(L-1) P_r(1-P_r)|g_(r+1)-g_r|^2
       <= [L(L+1)/a_min^2]
                       sum_r w_r |g_(r+1)-g_r|^2.      (10)

For f_i=sqrt(p_i)g_i, orthogonality to ker A_L is exactly
sum_i p_i g_i=0, while

    ||f||^2=Var_p(g),
    ||A_L f||^2=sum_r w_r |g_(r+1)-g_r|^2.

Equation (10) proves the stronger estimate

    sigma_min(A_L)>=a_min/sqrt(L(L+1))>=a_min/N.         (11)

This proves (2)--(3) in every degree without an asymptotic limit.

## 4. The exact retained charges and use in transport

Let h_s=F_s^+. Orthogonal projections P_s onto ker F_s and
Q_(s+1) onto ker F_s^* satisfy the exact equations

    h_s F_s=I-P_s,       F_s h_s=I-Q_(s+1).             (12)

All projectors are explicit: pull the normalized rank-one vector
(6) through the unitary path gauges. For s<N-1 the kernel of
F_s is zero and its cokernel has rank one. For N-1<=s<2d
the kernel has rank one and its cokernel is zero. At s=2d
the whole one-dimensional source is kernel.

At the invariant dual-pair degree s=d, L=d and eta_i=|x|^i.
Putting back the actual phases gives the normalized invariant cup
with coefficients proportional to x^a. Thus the original cup
charge survives this contraction exactly; it is not a zero-current
term to be removed. The full K=1 constraint singles out this
degree's charge as in
[the original Ward corner reduction](actual_rogers_bridge_transport.md).

For a compatible physical equation F_s v=j, (12) produces the
unique minimum-norm solution v=h_s j, with

    ||v|| <= max(1,|x|)(N^2/4)||j||.                    (13)

For an incompatible j the exact retained obstruction is Q_(s+1)j.
Similarly a row annihilating ker F_s factors through F_s with
a coefficient row of norm at most max(1,|x|)(N^2/4) times its own norm.
Thus, for a fixed finite sequence of such compatible local solves,
the inversion cost alone is polynomial in N. The currents or
retained charges themselves can still be exponentially large.

This is complementary to the cyclic-character contraction used for
the sewn wall currents. Here the metric and operator are those of
the literal nilpotent physical heads, not a cyclic replacement.
It gives a genuine local flow estimate for the proposed torsor
transport. It does not assert that arbitrary interbridge kernels
obey each separate pair's Ward equation, nor that a simultaneous
many-head reduction has the same estimate. Those compatibilities
must be established before iterating (13) across a knot diagram.

## 5. A holomorphic contraction on the actual scaled meridian tube

The Moore--Penrose inverse used in (12) depends on a Hermitian
metric. Pointwise bounds on a fixed annulus do not by themselves
give a holomorphic torsor map there. On the meridian scale used by
the quantum jets, however, an algebraic contraction has the same
polynomial cost.

Fix |x_0|=1, write x=z x_0, and on H_s put

    D_s(z)|a,s-a>=z^a |a,s-a>.

The literal coefficients in (1) give

    F_s(z x_0)=z^-1 D_(s+1)(z) F_s(x_0) D_s(z)^-1.     (14)

Define the holomorphic matrix and projections

    h_s^hol(z)=z D_s(z) h_s(x_0) D_(s+1)(z)^-1,
    P_s^hol(z)=D_s(z) P_s(x_0) D_s(z)^-1,
    Q_(s+1)^hol(z)=D_(s+1)(z) Q_(s+1)(x_0) D_(s+1)(z)^-1.

Equations (12) hold EXACTLY with these matrices and F_s(z x_0).
All entries are Laurent polynomials in z with fixed coefficients.
When x_0 is algebraic, the coefficients are algebraic: the appropriate
full-rank Gram inverse computes h_s(x_0) over the field generated by
Q,x_0 and their complex conjugates.

For z=exp(u/N) and |Re u|<=C, every diagonal D and its inverse
has norm at most exp(C). Consequently

    ||h_s^hol(exp(u/N))|| <= exp(2C+C/N) N^2/4,          (15)
    ||P_s^hol||, ||Q_(s+1)^hol|| <= exp(2C).

Every fixed-order u derivative has the same polynomial bound with
an additional constant depending only on its order and C. To see
this directly, differentiation acts on h by a scalar 1/N and
left/right multiplication by diag(a/N), of norms at most one.
The rth derivative therefore costs at most (2+1/N)^r.

This is a genuine holomorphic, source-compatible local contraction
on the entire marked quantum meridian tube. It avoids inferring
analytic transport from a nonholomorphic inverse. On a fixed-width
annulus, (14) can instead have exponentially large diagonal norms;
no bound like (15) for that particular holomorphic contraction is
asserted there. Likewise a many-head compatibility problem cannot
be solved by applying (14) to pairs whose separate Ward equations
are not satisfied.

## 6. Verification

[The audit](../experiments/audit_actual_two_head_ward_contraction.py)
compares the singular spectra of the literal complex current and
the weighted-path reduction, checks the bound on every degree at
small levels, and tests the kernel, projector and compatible-solve
identities. Larger levels test the balanced and unbalanced path
regimes. These are diagnostics of the formulas; (4)--(11) are the
uniform proof.
