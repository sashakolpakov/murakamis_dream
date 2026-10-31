# Exact binomial conversion with algebraic clock coefficients

28 October 2026. This supplements the [analytic conversion
counterexample](analytic_two_channel_conversion_counterexample.md).
The failure of a bound by the maximum complete marked-branch action
already occurs with polynomial coefficients over Q(i), on a compact
interval with no zero or coincident eigenvalues. This is a recurrence
example, NOT a knot operator; the clock x below is not the meridian M.

Fix delta=1/16. Take integers H=16r, n=H-2r=14r, and

    x_j=(r+j)/H, j=0,...,n-1,
    T_j=[ x_j       1/n;
          0       i(1-x_j) ],
    P_n=T_(n-1)...T_0.

The source is e_2 and the observable is e_1*. Thus the selected scalar
is (P_n)_12. The eigenvalues x and i(1-x) are nonzero and distinct on
[delta,1-delta], with gap |x-i(1-x)|>=1/sqrt(2). Eigenframes and their
derivatives are uniformly bounded. The principal family is diagonal;
the exact family differs from it only by the entry 1/n.

## 1. Exact finite identity

Expanding according to the unique off-diagonal step gives

    (P_n)_12=(1/n) C_(H,r) i^(-r)
                      sum_(m=r)^(H-r-1) binom(H,m)i^m,
    C_(H,r)=H^(-(n-1))(H-r-1)!(H-r)!/H! .          (1)

Indeed the term with conversion at step k has, apart from (1/n)i^k,
the positive weight

    H^(-(n-1)) (H-r-1)!(H-r)! /
                              ((r+k)!(H-r-k)!).    (2)

This proves (1) without an asymptotic argument. The same scalar is
the solution of the exact second-order recurrence

    u_(j+2)=[x_(j+1)+i(1-x_j)]u_(j+1)
                         -i x_j(1-x_j)u_j,
    u_0=0, u_1=1/n.                               (3)

Its coefficients are polynomial in x_j and 1/H over Q(i), and its
leading shift coefficient is one. The principal characteristic roots
are again x and i(1-x). Thus this is also a scalar companion example.

## 2. Growth follows from the binomial theorem and elementary tails

Write h(delta)=-delta log(delta)-(1-delta)log(1-delta). The full sum
is (1+i)^H, with modulus exp[H log(2)/2]. The omitted tails satisfy

    |omitted tails|<=(2r+1)exp[H h(delta)].          (4)

For completeness, binom(H,m)<=exp[H h(m/H)] follows because the
m-th term of the binomial probability sum with p=m/H is at most one.
Entropy increases on [0,1/2] and is symmetric, giving (4) for both
tails, including the single endpoint m=H-r. Since

    Delta=log(2)/2-h(1/16)>0,

the middle sum equals (1+i)^H times 1+O(H exp(-H Delta)). There is
no unresolved oscillatory cancellation in this conclusion.

Applying the elementary factorial asymptotic
log(m!)=m log(m)-m+O(log(m)) to (1) gives

    lim_(r->infinity) (1/n)log|(P_n)_12|=Gamma,
    Gamma=-1+[2(1-delta)log(1-delta)+log(2)/2]/(1-2delta).
                                                               (5)

Each continuously marked eigenvalue has the SAME complete action

    I=(1/(1-2delta)) integral_delta^(1-delta) log(x) dx
     =-1+[(1-delta)log(1-delta)-delta log(delta)]/(1-2delta).
                                                               (6)

Their discrepancy is strictly positive:

    Gamma-I=[log(2)/2-h(delta)]/(1-2delta)>0.        (7)

The diagonal entries of P_n have rate I, so its full norm also has
rate Gamma. Both numbers happen to be negative with this normalization;
multiplying every matrix by the fixed rational scalar 4 makes both
positive and preserves the discrepancy. No positivity of the rate is
needed to refute the proposed upper bound.

The diagonal principal product has rate I. Thus the polynomial 1/n
perturbation changes the leading exponential rate, despite the
uniformly separated spectrum. Algebraicity in a clock variable alone
does not remove this phenomenon. The additional structure of an actual
quantum knot operator, its meridian dependence, and its selected source
remain separate, essential questions.

[Audit](../experiments/audit_algebraic_clock_conversion.py): exact
Gaussian-integer triangular products, identity (1), the independently
iterated scalar companion, and asymptotic tail/rate checks.

The algebraic clock is not identified with an actual quantum meridian.