# What a Tauberian argument would need from the original positive Fourier energy

28 October 2026. The positive Fourier energy is the right actual object
for testing an Abelian/Tauberian approach. It permits elementary,
self-contained statements about its Laplace transform and its
exponential rate. Positivity alone identifies a limsup, however; it
does not force the volume limit or suppress exceptional low levels.

The results below give a precise additional cross-level condition that
WOULD turn a critical Laplace singularity into the full original
volume limit. No such cross-level condition or sharp singularity has
yet been derived from the actual A-source. This is a criterion and a
source-scope audit, not a proof of the conjecture.

## 1. The exact original energy and its existing bound

Use the original unitary color Fourier transform and original reduced
normalization from [the independently audited Plancherel identity](ordinary_color_plancherel_bound_audit.md).
For every fixed knot presentation,

    E_N=sum_k |chat_(N,k)|²=|K_N|²+R_N,
    1<=R_N<=N^B, N>=2,                            (1)

with a fixed constant/power allowed in the upper bound. Every pivot,
Cartan and framing factor is retained. The ordinary-color remainder
is the original remainder, not a positive replacement model. Thus

    log E_N=log(1+|K_N|²)+O(log N).                (2)

For any fixed lambda>0,

    log E_N/N ->lambda
      iff (2pi/N)log|K_N| ->pi*lambda.             (3)

In particular the desired energy exponent is lambda=Vol/pi.

The [direct ordinary-color coefficient bound](actual_regular_fast_color_elimination.md)
gives, for an ell-crossing b-braid,

    ||C_j||_1<=j^(ell+b-1)4^(ell*j).

Taking j=N and using (1) proves E_N<=exp(CN) for a fixed C. This
provides an actual nonempty convergence half-plane for the positive
Laplace series

    Z(s)=sum_(N>=2) E_N exp(-sN).                  (4)

It does not identify its sharp convergence boundary geometrically.

## 2. The abscissa gives exactly the exponential limsup

Put lambda*=limsup_N log(E_N)/N, finite and nonnegative. Then (4)
converges for real s>lambda* and diverges for s<lambda*.

Indeed, for s>lambda*, choose epsilon<(s-lambda*). Eventually
E_N<=exp((lambda*+epsilon)N), so comparison with a geometric series
proves convergence. For s<lambda*, infinitely many terms satisfy
E_N>=exp((s+epsilon)N), so the terms of (4) do not even tend to zero.
The convergence boundary itself can be convergent or divergent.

Consequently a source-derived proof that Z(s) is finite for every
s>Vol/pi would give the sharp original exponential UPPER bound.
Locating its abscissa at Vol/pi would identify the corresponding
limsup. Positivity makes these implications exact, but does not
compute the abscissa. Merely naming the abscissa is not an estimate.

## 3. A power singularity gives a genuine cumulative Tauberian conclusion

Here is a special case sufficient to explain the Karamata-type idea,
proved independently rather than assumed. Suppose, for lambda>0,
alpha>0 and C>0, an actual calculation establishes

    Z(lambda+t) ~ C t^(-alpha), t down to0.          (5)

Then

    A(x):=sum_(2<=N<=x) exp(-lambda N)E_N
             ~ C x^alpha/Gamma(alpha+1).          (6)

Proof. Write a_N=exp(-lambda N)E_N>=0 and define finite positive
measures on x>=0 by

    nu_t=(t^alpha/C) sum_N a_N exp(-tN) delta_(tN).

For each integer k>=0 their Laplace moments satisfy

    integral exp(-kx)dnu_t
       =(t^alpha/C)Z(lambda+(k+1)t)->(k+1)^(-alpha). (7)

Under y=exp(-x), these are ordinary polynomial moments on [0,1].
The candidate limit has x-density
exp(-x)x^(alpha-1)/Gamma(alpha); its moments are exactly (7), by
the defining Gamma integral. Polynomial moment convergence implies
convergence against every continuous function on [0,1]: Bernstein
polynomials approximate such a function uniformly, since uniform
continuity and the binomial variance bound force the approximation
error to zero. The measures' total masses tend to one, so the uniform
approximation error is uniform in t. This proves the claimed weak
convergence without a separate Tauberian theorem.

The bounded function y^-1 times the indicator y>=exp(-1) has just
one jump, at a point with zero limit mass. Approximate it from above
and below by continuous functions. Hence

    (t^alpha/C)A(1/t)
      ->integral_0^1 x^(alpha-1)/Gamma(alpha)dx
       =1/Gamma(alpha+1),

which proves (6).

An immediate useful consequence is that HIGH-ENERGY LEVELS OCCUR IN
EVERY FIXED MULTIPLICATIVE WINDOW: for each delta in(0,1),

    A(n)-A((1-delta)n)
      ~ C[1-(1-delta)^alpha] n^alpha/Gamma(alpha+1)>0.          (8)

Thus no fixed proportional interval can avoid all near-rate levels.
Also the UNTILTED cumulative energy S(n)=sum_(N<=n)E_N obeys

    log S(n)/n ->lambda.                          (9)

For the upper bound S(n)<=exp(lambda n)A(n). For the lower bound,
use (8) and exp(lambda(1-delta)n), then let delta decrease to zero.

Equations (6),(8),(9) are stronger than a bare limsup. They still
do not prove log E_N/N->lambda for every individual N.

## 4. An operative cross-level condition completing the implication

The following one-sided source-transport condition suffices. Suppose
there are fixed delta0>0, L>=0 and A0>=0 such that, for every large n,

    E_(n-r)<=n^A0 exp(Lr) E_n,
                   0<=r<=delta0*n.               (10)

It prevents an exponentially deep drop from preceding nearby levels;
it does not assert positivity of the original unsquared period. An
exact source-preserving map between the relevant positive Fourier
spaces, with norm at most n^(A0/2)exp(Lr/2), would prove (10).

Then the cumulative exponential law (9) implies

    log E_n/n ->lambda.                           (11)

To prove it, fix 0<delta<delta0. Since lambda>0, (9) gives

    S(n)-S((1-delta)n)=exp(lambda n+o(n)).

By (10) this difference is at most
n^(A0+1)exp(L delta n)E_n. Hence
liminf log E_n/n>=lambda-Ldelta. Let delta decrease to zero;
the upper bound E_n<=S(n) proves (11). Combining (3),(5),(10)
therefore proves the original volume limit with V=pi*lambda.

An O(1) bound on each negative neighboring log-increment implies
(10). In contrast, a polynomial comparison at ONE neighboring step,
E_(n-1)<=n^A E_n, accumulates to exp(O(r log n)); it does not imply
(10). Such a weak comparison allows narrow exponentially deep dips.
It cannot be substituted into this proof without further control.

The power singularity (5) is itself a substantial averaged asymptotic.
It is stronger information than the convergence abscissa. Neither
(5) nor (10) is being inferred from positivity or from an algebraic
classical characteristic.

## 5. What the current actual source does and does not supply

The available exact A-equation transports COLOR j at a fixed q:

    sum_i a_i(q,-q^j) C_(j+i)(q)=0.

The energy E_N changes the color range, the Hilbert-space dimension,
AND the parameter q_N when N changes. The fixed-q recurrence does
not provide an operator from the level n-r Fourier space to the level
n Fourier space. The quantum-group coproduct is also at fixed q.
Connected-sum multiplication changes the KNOT at a fixed level; it
is not a submultiplicative relation in the LEVEL N. The verified
cross-level polynomial rigidity of the color family identifies that
family, but gives no norm estimate of the form (10).

There is a concrete actual-source reason not to replace this missing
level map by uniform continuity of a fixed-color polynomial in q. For
4_1, its exact Newton formula gives C_N(q_(N+1))=1 for EVERY N:
at that root the evaluation node Q^N+Q^-N equals the first node
Q+Q^-1, so all positive Newton indices vanish. The same fixed color
at q_N is K_N. Thus a q-displacement of order N^-2 can cross the
entire high-color boundary response. This does not disprove (10)
for the COMPLETE level energies E_N,E_(N+1); it shows why fixed-q
pointing and low-color derivative estimates do not supply it.

Likewise each exact pointed Gram ratio is positive at its own level.
It has not been rewritten as the moments of one fixed positive
transfer operator across levels, nor as a positive renewal equation
with a specified spectral edge. Either construction, with the
original source and nonzero edge weight verified, could supply
Tauberian input. The existing level-dependent Gram identity does not.

There is even a small exact original hyperbolic-source warning against
assuming cross-level moment/log-convex structure for raw E_N. For 4_1,
the independently proved whole-source formula gives

    K_2=5, K_3=13, K_4=27,
    R_2=1, R_3=2, R_4=3,
    E_2=26, E_3=171, E_4=732.

Thus

    E_2 E_4-E_3²=-10209<0.                         (12)

So positivity within each Fourier space does not imply positivity of
the cross-level Hankel matrix, or a raw positive moment representation
of E_(n+2). This does not exclude an eventual inequality, a known
polynomial normalization, or a different source-derived transfer.
It simply prevents assuming that structure from Plancherel alone.

## 6. A minimal counterexample to positivity-only inference

For any lambda>0, let E_N=exp(lambda N) at even N and E_N=1 at odd N.
This is NOT a knot counterexample. Its purpose is to check the exact
logical strength of the proposed Tauberian inference. It satisfies

    Z(lambda+t)~1/(2t),
    A(x)~x/2,
    log S(n)/n->lambda,

but log E_N/N alternates between lambda and0. It violates (10).
Thus even the pure-pole singularity and positivity leave an
individual-level survival condition to establish.

The useful next target is consequently a SOURCE-DERIVED positive
Laplace/renewal description or a cross-level comparison such as (10).
Neither is currently available. A Tauberian argument can use those
inputs efficiently; it cannot create them or resolve the geometric
branch coupling by itself.

Reproduce the exact source warning and the positive-sequence checks:

```sh
python3 experiments/audit_actual_fourier_energy_tauberian.py
```

Coverage only: this is the classical positive-measure Tauberian setting;
see [Michael Taylor, Karamata's Tauberian Theorem](https://mtaylor.web.unc.edu/wp-content/uploads/sites/16915/2020/07/karamata.pdf).
Section 3 supplies its own moment proof for the precise power-law case
used here; no quoted theorem supplies the missing knot-source inputs.
