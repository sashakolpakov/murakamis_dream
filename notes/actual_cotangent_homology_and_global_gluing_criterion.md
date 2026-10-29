# What all-face collars do not supply: source homology and a gluing criterion

28 October 2026. The physical-face collars and quantitative regular
gradient estimate are compatible local analytic ingredients. They do
not alone prove a low-action deformation of the ORIGINAL scalar.
There is an exact source-homology obstruction to applying that argument
as one ordinary contour homotopy of its undecomposed holomorphic
summand. The obstruction occurs for the SAME hyperbolic knot after
ordinary signed Markov stabilizations; it is not a hypothetical phase
counterexample.

Source-specific current cancellation, exact normalization pruning or a
pointed-operator reduction can evade it. Thus this does not rule out
all contour or boundary-to-interior methods. A sufficient quantitative
gluing criterion is given below; its source-compatibility premise is
not yet proved for the full cotangent atlas.

## 1. A precise individual-evaluation homology lemma

Let F_N be holomorphic on the swept region Omega_N in C^r. Let Gamma_0
be the original product residue contour around the finite integer box
in the independent ORIGINAL source coordinates. For every valid state
p in that box, the ordinary product Cauchy kernel gives

    F_N(p)=(2pi*i)^(-r) integral_(Gamma_0)
                          F_N(z) dz_1...dz_r/product_j(z_j-p_j). (1)

Suppose a closed deformed current Gamma_N, including all its retained
components and multiplicities, is homologous to Gamma_0 in

    Omega_N minus UNION_(j,n) {z_j=n},              (2)

where the removed set includes ALL coordinate integer divisors met
by the original source. In particular every form in (1) stays
holomorphic on the deformation complement. Equation (1) holds with
Gamma_N too, independently of whether it was originally obtained
using a cotangent kernel.

Define its individual Cauchy mass

    M_(p,N)=(2pi)^(-r) integral_(Gamma_N)
                      |dz_1 wedge ... wedge dz_r|/product_j|z_j-p_j|.

Then EXACTLY

    |F_N(p)| <= M_(p,N) sup_(Gamma_N)|F_N|.          (3)

Consequently, if log M_(p,N)=o(N), a deformation in this homology
class cannot place the undecomposed density below the exponential
rate of that original individual state. Subexponential geometric
mass plus subexponential inverse distance to these Cauchy kernels
is a sufficient hypothesis on M. An arbitrary deformation with
uncontrolled near-divisor mass is not covered.

This is a statement about ordinary homology preserving ALL individual
evaluation tests. It deliberately excludes source-specific crossings
of canceled divisors, dropping exact zero pairings only for the selected
source, current recombination, and distinct transports of meromorphic
phase sectors whose compensating poles must be paired. Such operations
can change these extra tests while preserving the original period.
They are possible escapes, not contradictions to (3).

## 2. An actual same-knot family with arbitrarily high individual states

Use the original complete physical head, with

    Q=exp(2pi*i/N), x=-exp(-pi*i/N), d=N-1,
    F_a=(Q;Q)_a, g_b=theta Q^(-b), theta=x^(1-N),
    kappa=exp(pi*i*(N-1)^2/(2N)).

For a positive crossing, a DIAGONAL original matrix element has
a=b+k and exact value

    r_+(a,b;k)=kappa x^(-2b)Q^(b^2)
                                    F_a^2/[F_k F_b^2]. (4)

The original negative crossing on the reversed pair has the conjugate
value, including conjugate kappa. For N divisible by four take

    A=3N/4, B=N/4, k=N/2.

The actual endpoint-uniform factorial estimate, or its elementary
interior Euler--Maclaurin proof, gives

    |r_+(A,B;k)|=|r_-(B,A;k)|
        =(2N)^(-1/2) exp[N v_8/(2pi)](1+O(1/N)).   (5)

Indeed I(3/4)=-I(1/4)=Catalan/(2pi), I(1/2)=0 and
v_8=4 Catalan. The factorial square-root prefactors give precisely
(2N)^(-1/2). Both actual half-root and full Cartan phases are retained
in (4); they have modulus one.

Start from ANY fixed one-component braid diagram of ANY hyperbolic
knot K. Its closed state with every head A and every original transfer
zero is valid. Every original crossing then has modulus one, at either
sign, and all original pivots also have modulus one.

Append signed Markov stabilizations, starting with a positive one and
then alternating signs. The new last head values are B,A,B,A,...,
and every appended transfer is k=N/2. Each new crossing is diagonal:
(A,B) is unchanged by the positive crossing and (B,A) is unchanged by
the negative crossing. Thus this is an EXACT valid closed original
state at every stage, with no mod-N routing or reset. With s such
stabilizations, its absolute value is

    (2N)^(-s/2) exp[s N v_8/(2pi)](1+O_s(1/N)),    (6)

up to the retained label-independent external line, which has no
exponential modulus at the original complete normalization. The
single original averaged-cut factor 1/N also changes only a power
of N. No additional average is attached to each new head.

### Independent check of the whole original Markov normalization

The exact original partial trace of the new head is

    Tr_new[(I tensor g)R_+]=kappa theta I,
    Tr_new[(I tensor g)R_-]=kappa^(-1)theta^(-1)I.   (7)

Here is a direct proof without assuming an external invariance
theorem. For the positive case its a-th cut diagonal, divided by
kappa theta, is

    F_a^2 sum_(b=0)^a Q^(b^2)/(F_(a-b)F_b^2)=1.    (8)

The rational identity follows by decomposing a partition with largest
part at most a by its Durfee square of side b: the square contributes
Q^(b^2), the part to its right is a b by (a-b) rectangle, with generating
polynomial {a choose b}_Q, and the part below has largest part at most
b, contributing 1/F_b. This is a bijection, so
1/F_a=sum_b Q^(b^2){a choose b}_Q/F_b as a formal power series and
hence as a rational identity. All root denominators satisfy b<=a<N.
There is no first-partial-trace off-diagonal by exact degree support.

For the negative trace put A'=d-a and replace b by d-r. Exact factorial
reflection at Q^(-1) and the SAME identity (8) give, before its final
Cartan simplification, the scalar

    kappa^(-1)theta x^(2a)
                            Q^[-a^2+1+A'(A'+1)].

Since x^2=Q^(-1), A'+a=N-1 and theta^2 Q=1, this is exactly the
second value in (7), with no parity exception. Both are unit scalars.

The original zero-framing line cancels precisely these actual
Markov factors. Partial tracing the new head in a whole word uses
its original pivot and NO factor 1/N; the sole original average in
(2) of the cardinal source stays unchanged. Thus every stabilized
diagram has the SAME original knot invariant and the same volume,
while (6)'s individual-state rate is arbitrarily large as the fixed
number s increases. This independently checks every new pivot and
normalization relevant to the example.

## 3. Consequence for the proposed global dynamics

For the cardinal completion, F_N is holomorphic on the stated joint
box and equals the exact original summand at every valid integer
state. Therefore (1)--(6) apply to that ACTUAL source. Choosing s
with s v_8>Vol(K) rules out an undecomposed low-|F_N| cycle with
subexponential Cauchy mass in the homology class (2), at the desired
knot-volume level. All proper physical faces of that diagram still
have the proved outward action coefficient, and its genuine regular
critical values still have the representation-volume bound.

This pinpoints a compatibility which those local results alone do
not establish. One must use the selected source, not silently prove
an equally strong estimate for every individual-state evaluation.
The already proved exact Markov pruning DOES evade this example;
it contracts a complete source cell before absolute estimation.
It is part of the remedy, rather than a contradiction to the theorem.
Additional source-specific relations can likewise evade the extra
evaluation tests. The example does not prove that a pruned diagram
still has the same obstruction, nor that all sector/current contour
methods fail.

## 4. A sufficient quantitative gluing criterion and its power count

The following criterion isolates what a valid boundary-to-interior
construction would have to add. It is local-current data rather than
an assumption that the unknown whole period already has a low-action
representative.

Suppose the finite physical-face atlas is supplied with SOURCE-specific
chain homotopies on the complete marked sector/current complex, with
all these properties:

* Their boundary formulas include all overlap curtains, valid
  cotangent residue currents, and paired artificial pole currents.
  The formulas glue on overlaps and preserve the selected original
  period. They need not preserve the additional tests (1).
* A common marked height H is used. A face operation, including its
  outgoing current pieces, lowers H by at least
  g_N=c N^(-alpha)log N, up to a smaller overshoot
  O(N^(-beta)log N), beta>alpha. No unmatched side current is left
  at arbitrary height. Already low-height terminal pieces are allowed.
* After the leading height is accounted for, each operation has a
  bounded number of pieces and log mass cost at most
  C log^C N+C N^(1-beta)log^C N. The exact collar Gamma bounds can
  provide this type of local estimate; their leading negative action
  must not be counted again as a positive amplitude loss.
* Regular gradient segments preserve the same source class and have
  cumulative log mass at most N^(B epsilon)log^C N, with B epsilon<1.
  All ends either enter another covered patch or the target sublevel.

If the initial relevant height range is O(log^C N), these properties
give the desired exp(o(N)) total transport cost. In fact the number
of face operations is at most

    J_N=O(N^alpha log^C N),

because each spends at least a fixed fraction of g_N in height. Their
combined log mass is consequently bounded by

    O(N^alpha log^C N+N^(1+alpha-beta)log^C N)=o(N), (9)

provided alpha<1 and beta>alpha. Fixed branching adds only O(J_N).
The regular-flow cost is also o(N). A transported chain ending in
H<=Vol(K)/(2pi)+eta then gives the upper bound by triangle inequality;
letting eta decrease gives the sharp limsup. This proves the criterion.

The not-yet-verified part for the actual global cotangent atlas is
precisely the first two source-compatible gluing properties, including
valid interior residue currents and overlap heights. Finite face count,
endpoint action drop and a regular flow bound do not imply them.
In particular source-universal chart identities alone preserve the
individual tests behind (3); state-specific normalization/Ward or
pointed-A information must enter where that barrier is exceeded.

## 5. Independent audit of the source-specific A-boundary alternative

I independently read
[the actual A-boundary Schur theorem](actual_a_boundary_schur_transport.md)
and reran its audit: **PASS**. The initial weighted identity-row
source gives g_I=0 exactly when those colors are retained in B.
Completing the square gives H=-P_II^(-1)P_IB and the positive Schur
operator S with ker P=E ker S. Consistency gives
beta=g_B^* S^+ g_B, not an independently chosen border normalization.

I checked the positive bordered Gram and the selected coefficient
formula [lambda^nu z]D/[lambda^nu]Q, including the retained kernel:
g_B and the selected observable vanish on it, so the kernel factors
off as lambda^nu and the z derivative is the exact squared selected
boundary response. The banded Neumann-series inverse decay and the
rigid two-endpoint recurrence example also check, including
lambda_min(S)~3*4^(-n)/4. No source or weight correction was needed.

The fresh audit passed four actual pointed-source eliminations, the
exact one-dimensional retained-kernel fixture and four rational rigid
boundary recurrences. This construction can escape (3): it estimates
the ACTUAL selected source response, not every holomorphic state
evaluation. Its remaining boundary energy estimate is not supplied
by uniqueness or the good interior gap.

[Independent original-source normalization audit](../experiments/audit_actual_cotangent_homology_stabilization.py)
checks (4)--(8), both crossing signs and every new pivotal trace.
