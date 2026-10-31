# What the original compact trace does not localize

28 October 2026. Independent lower-bound audit. The exact compact
coherent source is a genuine normalized matrix trace. That fact does
not make the original crossing a pullback along a map of the compact
source, and it does not make its total-normalized selected functional
a rational trace on the geometric critical field. The two failures
below concern the specified original operators and source, rather than
arbitrary replacement periods.

They exclude an exact finite-graph Lefschetz shortcut. They do not
exclude a semiclassical Fourier-integral or derived-correspondence
construction with its own source transport theorem.

## 1. Every original crossing level has a full-rank coherent endpoint

Use the balanced factorial basis of the
[compact source](compact_coherent_source_period.md),

    d=N-1, Q=exp(2 pi i/N), x=-exp(-pi i/N),
    F_k=(Q;Q)_k, F_0=1.

Let B be the original checked positive crossing, with its common
nonzero Cartan scalar retained externally. In these actual balanced
coordinates its coefficient for

    |a,b> -> |b+k,a-k>

is

    (-1)^k x^(-a-b-k)
    Q^[ab+(a-b)k-k(k+1)/2]
    {b+k choose k}_Q (Q x^2 Q^(-a);Q)_k.          (1)

This is the original coefficient followed by its literal two head
factorial changes, as independently specified by `MixedEntries.direct`
in the [whole-source audit](../experiments/audit_figure_eight_whole_source.py).
No cup or co-source is replaced here.

Because Q x^2=1 and Q^(-d)=Q, (1) gives

    B |d,0> = sum_(k=0)^d c_k |k,d-k>,
    c_k=(-1)^k x^(-d-k)
          Q^[d k-k(k+1)/2] F_k.                  (2)

Every c_k is nonzero. Thus the two-head coefficient matrix is
anti-diagonal with nonzero determinant: its Schmidt rank is exactly N.
There is an equally useful transpose statement:

    B^t |d,0> = sum_(k=0)^d t_k |k,d-k>,
    t_k=x^(-d-k) Q^(-k) F_d/F_(d-k).             (3)

For (3), apply (1) to input (k,d-k) and transfer k, and use

    (Q^(-k);Q)_k=(-1)^k Q^[-k(k+1)/2] F_k.

All t_k are again nonzero. These formulas are valid at every N>=2;
neither a numerical asymptotic nor a particular knot is involved.
The independent original E/Cartan evaluator also checks both formulas
exactly over the existing prime-field realizations for N=2,...,13.

## 2. No exact single-graph pullback, even on a dense rational chart

The coherent evaluation embedding for one head is the degree-d
Veronese curve

    P^1 -> P(H^0(P^1,O(d))^*).

For two heads its image lies in the rank-one locus for the tensor
product of the two head spaces. The endpoint |d,0> is such an
evaluation tensor; the binomial normalizations do not alter that
endpoint or tensor rank.

A weighted composition operator on sections along a rational map
f:(P^1)^2 -->> (P^1)^2 has the following necessary property wherever
it is defined:

    T^t ev_p = h(p) ev_(f(p)).                    (4)

It therefore maps coherent evaluation tensors to rank-one tensors on
a dense open set. Every two-by-two minor expressing rank at most one
is a polynomial in the evaluation coordinates. If it vanishes on that
dense open set it vanishes everywhere. If T is invertible its image
never vanishes, so indeterminacy at a special endpoint cannot evade
this test. Equation (3) contradicts (4).

Consequently the actual B is not a weighted pullback on this compact
source, even along a rational map defined only generically. Constant
changes of frame on individual heads preserve tensor rank, so separate
head frame changes do not repair the obstruction.

More generally, suppose T is a sum of r weighted graph pullbacks on
a common dense open set. Then T^t ev_p is a sum of r rank-one tensors,
so it has matrix rank at most r there. The rank-at-most-r locus is
closed, hence that bound holds at the endpoint as well. Equation (3)
forces

                          r >= N.                 (5)

Thus an exact graph-pullback expansion of bounded branch number cannot
be the sought fixed finite geometric Lefschetz model. A genuine
quantized canonical correspondence is a different object: it need not
act by pointwise composition on holomorphic sections. None of (2)--(5)
rules out such an object or its eventual stationary localization.

## 3. The original selected leading source need not descend as a field trace

There is a second, independent obstruction to applying
[irreducible critical trace nonvanishing](irreducible_critical_source_and_whole_norm.md)
without constructing its actual comparison map.

Use the exact original positive figure-eight state, with its literal
monomial insertions:

    mu_N(f)=sum_(n=0)^(N-1) |(Q;Q)_n|^2 f(Q^n),
    mu_N(1)=K_(4_1,N)>0.                          (6)

This is the same source as in the
[actual quotient obstruction](actual_source_quotient_and_critical_relation.md).
Its continuous rate is

    H(s)=2 integral_0^s log(2 sin(pi t)) dt.

The logarithmic endpoint singularities are integrable. Comparing the
monotone endpoint pieces and ordinary interior Riemann sums gives

    log |(Q;Q)_n|^2=N H(n/N)+O(log N)

uniformly in n. The unique global maximum of H on [0,1] is s=5/6.
Indeed H'=2 log(2 sin pi s) has zeros 1/6 and 5/6, with the former
a minimum; H(0)=H(1)=0 and H(5/6)>0. Thus for any fixed neighborhood
U of 5/6 the normalized mass outside U is exponentially small.
For every fixed Laurent polynomial f, positivity and continuity give

    mu_N(f)/mu_N(1) -> f(z_*),
    z_*=exp(-pi i/3).                            (7)

In particular the actual leading normalized first moment is z_*.
On the critical algebra

    K=Q[Z]/(Z^2-Z+1)

this selected limiting functional is one complex embedding. It is
not a Q-valued field trace: its value on Z is nonrational. After
extension to C the algebra splits as C x C and the functional in
(7) has weights (1,0), up to the order of its two embeddings. Its
moment matrix has rank one. This is compatible with the exact
finite source and with every nonzero weight in (6).

The trace-duality theorem itself remains correct. Its hypothesis is
an F-valued functional on an irreducible finite extension over F.
The total-normalized selected functional in (7) does not have that
rational descent. Taking F=C instead splits the critical algebra and
removes irreducibility. Finite normalized matrix trace faithfulness
does not supply the missing descent.

This does NOT disprove rational descent of a separately
action-normalized, multi-sector critical module. Division by the
dominant total period automatically suppresses any lower-action
sector, even if that sector has a nonzero rationally descended
coefficient before this division. Thus (7) excludes identifying this
particular limiting functional with a rational field trace; it does
not show that the conjugate sector's own coefficient vanishes or
that a suitable per-sector construction is impossible.

Equation (7) is a diagnostic of the already specified original source,
not a definition of a new source by dividing an unknown invariant.
In particular it is not an adapter proposed for a general knot.

## 4. Consequence for the lower-bound strategy

The exact compact trace supplies the original cycle and a faithful
finite matrix pairing. It supplies neither the graph hypothesis of
ordinary holomorphic Lefschetz localization nor rational descent of
the total-normalized leading functional. Both shortcuts have concrete
failures above. The separately action-normalized microlocal comparison
is not decided by these tests.

An action-normalized microlocal correspondence could still solve the
problem, but it must construct the geometric summand and prove that
the original source has nonzero image there. Rewriting its conclusion
as a positive rank in a critical field does not bypass that step.
No new broad-class exponential lower bound is proved by this audit.
