# A coherent bridge has a pointed metric potential and a coercive source-fixed optimization

29 October 2026. The six-head bridge and the COMPLETE terminal packet
can be composed before an operator norm is taken. Eliminating the bridge
is exactly a POINTED diagonal potential on the terminal INPUT; the
terminal Green/Newton interference remains intact. Its best all-input
constant in the actual pair-degree bias family is a coercive log-convex
finite-dimensional optimization. Minimizers stay in a fixed compact
interval uniformly in N. They obey an exact physical charge-balance
equation, with no exponential cost at the original paired sources.

This gives a quantitative local metric step with arbitrary spectator
inputs. It does not bound the preceding biased word or prove that such
steps telescope across overlapping bridges. No sharp knot-volume bound
or new geometric-edge identification is asserted.

## 1. The SAME original maps and physical metric

Keep the original root N>=2,d=N-1,Q=q^2,x=q^d, F_a=(Q;Q)_a,
s_a=|F_a| and all kappa/source factors. Let

    W_2=(V^tensor4)_(degree2d), W_1=(V^tensor2)_(degree d).

Use the physical source-fixing coordinate gauge G_a=s_a/sqrt(N)
on each input/output head. It fixes original cups and ordinary caps
pointwise, since G_aG_(d-a)=1. The whole marked closure is kept by
the complete invariant-source theorem. Write L for the gauged
POSITIVE bridge map

    L=(ell_12 tensor I_34) R_23:W_2->W_1

from [the exact open bridge theorem](actual_terminal_bridge_operator_reduction.md).
For input |a,b,c,e> it forces

    k=d-a-c, u=b-k=d-e, a+c+k=d,
    0<=k<=d-u.                                          (1)

Its full coefficient includes the original phase; in this gauge its
magnitude is N/(s_a^2 s_c^2 s_k). All through-head feedback is the
actual strict shift and unitary clock, not a scalar substitution.

Let T:W_1->C^N be the original complete terminal packet. It has
[the closed all-input kernel](actual_terminal_packet_closed_kernel.md),
including its partial factorial Green register P_t. On W_1 the
physical product gauge is one. Thus that literal T matrix is unchanged.
The full six-head terminal bridge is K=TL, with every spectator port
retained. Its row sum is the original source row by the cap/Hopf
identity, not by a new boundary functional.

Define the genuine pair-degree bias on W_2 by

    A_delta|a,b,c,e>=exp[delta(a+b-d)]|a,b,c,e>,
    L_delta=L A_delta^(-1), delta real.                   (2)

It is obtained by the SAME coordinate factor exp(delta(j-d/2))
on heads1,2. It fixes every original paired cup/cap. Equation (1)
gives a+b-d=u-c, so its exact coefficient change is exp[delta(c-u)].
In particular the original initial vector w_0=p_12 tensor p_34 obeys
A_delta w_0=w_0. No knot value or unknown solution defines this bias.

## 2. Exact coherent composition reduces to a pointed potential

Rows of L_delta have disjoint spectator e=d-u. Consequently its
COMPLETE row Gram is exactly

    L_delta L_delta^*=diag(E_delta(u)),
    E_delta(u)=N^2 sum_(k=0)^(d-u) sum_(a+c=d-k)
                exp[2delta(c-u)]/(s_a^4 s_c^4 s_k^2).     (3)

All its original phases were retained before taking this Gram.
The complete composition therefore satisfies the operator identity

    (T L_delta)(T L_delta)^*
                    =T diag(E_delta(u)) T^*=:M_N(delta). (4)

It is not necessary to replace E_delta by its largest row. In
particular (4) keeps its THROUGH-COLOR dependence and all the
Green/Newton/R interference inside the terminal T.
Here u is a PHYSICAL degree-basis index of W_1, not a Casimir
node. The terminal Gram T^*T still mixes distinct Casimir nodes;
(4) does not return to the disproved nodewise Cauchy budget.

Define the exact constant

    C_N(delta)=lambda_max(M_N(delta))>0.                  (5)

It is the SMALLEST all-input constant in the typed inequality

    ||T L w||^2 <=C_N(delta)||A_delta w||^2,
                                                  EVERY w in W_2. (6)

This follows from T L=(T L_delta)A_delta and the largest singular
value. It remains true with an arbitrary Hilbert spectator tensor,
including matrix-valued exterior columns; no spectator coefficients
have been commuted. Optimality is an actual singular-value statement
on the COMPLETE module, not an independently estimated path sum.

Equivalently the conditional bridge cost is exact: if v is a specified
output of L_delta, its minimum input norm squared is
sum_u |v_u|^2/E_delta(u), since L_delta has full row rank. Thus (4)
is the actual pointed input metric for the terminal packet.

For clarity, the known ordered factorization of T is

    T=N^(-1) D_out U^(2) D_in P(J) Rev (kappa^(-1)R).

Substituting it in (4) leaves the middle operator
R diag(E_delta) R^* between Rev and the two Green factors.
It does NOT allow P(J), Rev, R and E_delta to be reordered.
The terminal singularity P_1=0 at N=6 causes no difficulty: T
need not be invertible anywhere in (4)--(6).

For the unchanged scalar source, the exact terminal row factorization
also yields

    |chi_N sum_n (T L w)_n|^2
       <=|chi_N|^2 N C_N(delta)||A_delta w||^2.           (7)

The N is the known number of coherent packets. The full positive
completion by exp(-N^2)I from the terminal Gram theorem still has
polynomial dual cost; no boundary source is normalized by a period.

The full positive completion can be kept throughout. Put
H_epsilon=(TL)^*(TL)+epsilon I on the COMPLETE W_2, and
consider its exact norm after the same input bias. Its optimal
constant C_(N,epsilon)(delta) satisfies

    C_N(delta)<=C_(N,epsilon)(delta)
        <=C_N(delta)+epsilon exp(2|delta|d).              (7a)

This follows by conjugating H_epsilon with A_delta^-1 and using
the exact input charge range[-d,d]. For epsilon=exp(-N^2),
the difference is superexponentially small on every bounded bias
set. No channel in ker(TL) is removed. Log convexity and the
coercive bounds below apply to this completed norm too: apply
the same column exponential-sum proof to the fixed stacked matrix
(TL,sqrt(epsilon)I)A_delta^-1. The tiny regularizer is therefore
compatible with the complete positive inner product, not an
assumed inverse of T or L.

## 3. The local metric optimization is genuinely coercive

Let t_u=T e_u be a COMPLETE terminal input column. Equations (3)--(4)
give the positive matrix exponential sum

    M_N(delta)=sum_(u,k,a+c=d-k)
       N^2 exp[2delta(c-u)]/(s_a^4 s_c^4 s_k^2)
                                                   t_u t_u^*. (8)

For any fixed unit output vector z with T^*z!=0,
z^*M_N(delta)z is a positive sum of exponentials in delta.
Its logarithm is convex by the elementary log-sum-exp Hessian.
Vectors in the common nullspace give zero and are ignored in
the Ritz supremum. Since log C_N is that supremum,

    delta -> log C_N(delta) is convex.                    (9)

There are ACTUAL opposite extreme charges, not just a formal convex
hull assumption. The bridge states (a,c,k,u)=(0,d,0,0) and
(d,0,0,d) each have squared coefficient N^-2 before the bias.
The closed terminal entries give

    |T_(0,0)|=1/N, |T_(0,d)|=1.

Their rank-one positive contributions imply, for ALL real delta,

    C_N(delta)>=N^-4 exp(2delta*d),
    C_N(delta)>=N^-2 exp(-2delta*d).                     (10)

Thus log C_N tends to infinity at BOTH ends and attains a finite
global minimum. Neither uniqueness nor positivity of every terminal
eigenvalue is required.

Moreover all minimizers are uniformly bounded as N varies. The
uniform sine-factorial estimate bounds s_a and s_a^-1 by
N^C exp(CN), with constants independent of a. The explicit closed
T entry consists of a bounded number of such ratios, a sum of at
most N terms, and |P_t|<=(4^(t+1)-1)/3. Therefore

    ||T||<=N^C exp(C_T N).

The independently proved pointed bridge profile gives
max_u E_0(u)<=N^C exp(Nv_8/pi). Hence

    log C_N(0)<=C_0N+C_1log N.                           (11)

At a minimizer delta_N, C_N(delta_N)<=C_N(0). Combining (10)
with (11), and d=N-1>=N/2, proves

    |delta_N|<=C_2                                      (12)

with an explicit finite constant obtainable from those factorial
bounds, independent of N. Thus the optimal local typed metric
does not require a bias growing with N or an unknown solution.
Its exponential coordinate conditioning is the controlled physical
degree weight in (2); original paired boundary norms remain fixed.

## 4. Its optimality equation is an exact physical charge balance

If the largest eigenvalue in (5) is simple at a minimizing delta,
let z be its unit eigenvector. Differentiating the finite matrix
sum (8) gives EXACTLY

    sum_(u,k,a+c=d-k) (c-u)
       N^2 exp[2delta(c-u)]/(s_a^4 s_c^4 s_k^2)
                                               |z^*t_u|^2=0. (13)

For a multiple largest eigenvalue, the same equation holds with
|z^*t_u|^2 replaced by Tr(rho t_ut_u^*), for a positive trace-one
rho supported on that largest eigenspace. To see this, the left
and right derivatives of the largest eigenvalue are the minimum
and maximum quadratic forms of M_N' on the top eigenspace.
At a minimum they enclose zero; a convex mixture gives rho.

All weights in (13) are nonnegative and sum to C_N(delta) after
dropping (c-u). Thus the maximizing output-energy ensemble has
zero mean ACTUAL pair-degree charge, a+b-d=u-c. The true bridge
angle sum a+c+k=d and cutoff k<=d-u are retained simultaneously.
This is a concrete local metric-duality constraint, not an assertion
of a complete hyperbolic gluing equation or a peripheral parameter.
It concerns the all-input norm optimizer, not automatically the
selected original-source distribution.

The exact negative-bridge analogue uses the dual physical gauge
G^-1, complementary angles and the corresponding E_-(u) profile.
The same matrix-potential construction applies. Changing between
the two physical gauges retains the actual G^2 interface; it is
not a free contraction in this optimization.

## 5. Why it does not yet telescope through an arbitrary prefix

For an original preceding braid B and its original source w_0,
(6) is the genuine pointed bound

    ||T L B w_0||^2
        <=C_N(delta)||A_delta B w_0||^2,
    A_delta B w_0=(A_delta B A_delta^(-1))w_0.            (14)

The conjugated prefix and all its original coefficients remain.
A_delta commutes with generators contained in input pair12 or34,
but not with the overlapping bridge R_23. Its matrix entries gain
the exact pair-degree difference of their physical input/output.
Thus one cannot optimize (5) and then keep the untransformed
preceding word. This is the retained interface to be controlled in
a sequence of bridge eliminations.

The new result is an exact, coercive ALL-input step relative to the
fixed terminal Gram, preserving all spectator operators and known
sources. It improves on a free octahedral maximum by retaining the
pointed potential and a physical degree-balance condition. It does
not prove a global telescoping potential, a knot-volume upper bound,
or geometric survival. No additional presentation counterexample
is needed or claimed by this local optimization theorem.

[Audit](../experiments/audit_actual_coherent_terminal_bridge_metric.py):
eleven levels N=2,...,12. The code constructs L directly from the
original R and cap, T from its independently verified closed kernel,
and tests (4) on all open columns, arbitrary two-column spectator
states, exact paired-source invariance, both coercive bounds,
log convexity and the minimizing charge equation. Finite numerical
optimization supplements the all-level convex/coercivity proof.
