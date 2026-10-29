# The actual period from an all-level A-operator and finite pointing

Research note, 25 October 2026. Starting from any specified nonzero
all-level annihilator of the actual reduced ADO state, the Kashaev
value is recovered from that operator and finitely many fixed small
colors, without a rank-one or regular-orbit assumption. Singular
steps require a uniformly bounded quantum-parameter jet. Those
initial jets are bounded because the colors are fixed. This gives
an exact operator period; its volume growth remains unproved.

The definitions and independently checked normalization are those of
[the ADO note](kashaev_ado_pointing.md). In particular

    F_N(-q_N^j)=C_j(q_N), 1<=j<=N,
    F_N(1)=<K>_N, q_N=exp(pi*i/N),                   (0.1)

where C_j(q) is the fixed finite-dimensional reduced period, with
unknot normalization one. It is Laurent polynomial in the recorded
quantum parameter, analytic at q=1, and C_j(1)=1. Only finitely many
fixed colors will be input. No large-color Jones estimate or
unverified holonomicity theorem is used.

## 1. Cross-level rigidity gives the generic trace recurrence

Fix a specified nonzero all-level reduced ADO annihilator

    P=sum_(i=0)^d a_i(q,M)T^i, TM=qMT, d>=1,         (1.1)

with rational coefficients, annihilating F_N for all but finitely
many N. Clear denominators once so that a_i are Laurent polynomials.
This changes no state or peripheral normalization. A possible
order-zero annihilator of this nonzero state is necessarily zero.

For any fixed positive integer j form the Laurent polynomial

    H_j(q)=sum_(i=0)^d a_i(q,-q^j) C_(j+i)(q).        (1.2)

At every sufficiently large N with N>=j+d, (0.1) and the actual
ADO equation give H_j(q_N)=0. Infinitely many distinct q_N occur.
A nonzero Laurent polynomial has only finitely many nonzero roots,
so

    sum_(i=0)^d a_i(q,-q^j) C_(j+i)(q)=0             (1.3)

identically in q, for every j>=1. This is an elementary Zariski
rigidity argument. It requires neither an equality of annihilator
ideals nor an identification of the root central curve with A_K.

The inclusion of the ADO recursion ideal in a suitably normalized
colored-Jones recursion ideal is already stated in
[Brown--Dimofte--Garoufalidis--Geer, 2005.08176](https://arxiv.org/abs/2005.08176).
Its proof is not a premise: (1.2)--(1.3) follow directly from the
quotient-color identity already independently proved here. Reduced
meridian convention M=-q^j includes the needed sign and shift;
it must not be replaced silently by a different paper's x-variable.

## 2. A fixed initial window avoids identically singular steps

Write the support of the leading coefficient as

    a_d(q,M)=sum_(a,b) c_(a,b) q^a M^b.

Let A be its q-exponent span, D its M-exponent span, and s its
number of monomials after collecting terms. Choose

    j_0=A+1.                                        (2.1)

For j>=j_0 the substituted Laurent polynomial a_d(q,-q^j) is
nonzero identically. In fact its exponents are a+bj. A collision
between distinct b's would imply
|j|=|a-a'|/|b-b'|<=A, and terms with the same b do not collide.

Thus (1.3) propagates the fixed initial vector

    c_0(q)=(C_(j_0)(q),...,C_(j_0+d-1)(q))^t        (2.2)

as rational functions in q to every later color. Let B_j(q) be
the companion matrix, now evaluated at M=-q^j with q variable.
For N>=j_0+d put

    r_N(q)=e_d^t B_(N-d)(q)...B_(j_0)(q).

Then the exact period formula is

    <K>_N=[r_N(q)c_0(q)]_(q=q_N).                   (2.3)

The right side is the value of the whole regular germ. Its product
equals the Laurent polynomial C_N(q) identically, so all apparent
poles cancel before evaluation. The operator and the fixed initial
periods specify this value uniquely. There is no free levelwise
central multiplier and no choice of a favorable root solution.

The use of small colors here is finite pointing of the A-module.
Equation (2.3) does not substitute a large-color Jones asymptotic
for the requested A-operator analysis.

## 3. A uniform bound on the required q-jets

For all sufficiently large N, a_d(q_N,M) is a nonzero Laurent
polynomial of M-span at most D. The points -q_N^j appearing in
the product are distinct. Therefore at most D steps satisfy
a_d(q_N,-q_N^j)=0.

Each such step has q-multiplicity at most s-1. To see this, any
nonzero Laurent polynomial with t<=s monomials has the form

    h(q)=sum_(r=1)^t c_r q^e_r, e_r distinct.

If h and its first t-1 logarithmic derivatives vanished at a
nonzero q_0, then

    sum_r e_r^k c_r q_0^e_r=0, k=0,...,t-1.

The Vandermonde determinant in the distinct integers e_r is nonzero
in characteristic zero. All c_r would be zero, a contradiction.
Ordinary and logarithmic vanishing multiplicities coincide at q_0!=0.

Consequently the total pole budget of the companion product obeys

    B_N=sum_(j=j_0)^(N-d) ord_(q=q_N) a_d(q,-q^j)
        <=D(s-1).                                  (3.1)

This counts tangencies of the moving curve M=-q^j as well as
ordinary root-orbit zeros. The simpler meridian bound D from
[the preceding note](bounded_meridian_jets.md) cannot just be
reused for q-jets, because M moves with q.

Use t=q/q_N-1 and expand

    r_N(q_N(1+t))=sum_(k=-B_N)^infinity R_(N,k)t^k,
    J_k(N)=[t^k]c_0(q_N(1+t)).

The whole-germ formula becomes

    <K>_N=sum_(k=0)^B_N R_(N,-k) J_k(N).             (3.2)

For every fixed k<=D(s-1), J_k(N) is bounded as N tends to
infinity: its entries are q_N^k C_j^(k)(q_N)/k! for a fixed finite
set of colors, and these functions are analytic near q=1.
Thus initial pointing introduces no unknown exponential level
normalization. Every growing part of (3.2) is in the specified
operator's long companion product and its bounded-order germ.

As in the meridian calculation, regular numerator matrices and
the full denominator product compute (3.2) using a fixed truncation.
No division by a zero coefficient at q_N is performed.

## 4. Why levelwise Hilbert 90 alone would miss this coherence

There are fixed operators with extra root-level solutions that
cannot be the coherent knot family. For example take

    Q=(1+q^2 M^2)T^2-(1+q^2)T+q^2(1-M^2)
      =(T-q^2)[(1+M^2)T-(1-M^2)].                  (4.1)

For even N put

    f_N(M)=product_(r=N/2)^(N-1)(1-q_N^(2r) M^2).

Telescoping gives
(1+M^2)f_N(q_N M)=(1-M^2)f_N(M), so Q annihilates
both 1 and f_N. Moreover

    f_N(-q_N^j)=0 for 1<=j<=N/2,
    |f_N(1)|=sqrt(2N).                              (4.2)

For the modulus, pair the conjugate factors in
product_(r=1)^(N-1)(1-exp(2pi*i*r/N))=N and retain the middle
factor 2. This gives the stated square root exactly.

Hence h_N=1+a^N f_N, a>1, has value one at every fixed small
color for all sufficiently large even N, yet its target has
logarithmic rate log(a). Take h_N=1 at odd levels. The same fixed
Q annihilates the whole manufactured root family.

This family cannot satisfy (0.1) with fixed Laurent polynomials
C_j at every permitted level. For fixed j its values are one at
infinitely many levels, so polynomial rigidity forces C_j=1
identically. But at a single even level, j=N/2+1 has a nonzero
f_N value and contradicts that identity. Equivalently the generic
recurrence with initial C_1=C_2=1 forces C_j=1 for all j, since
1+q^(2j+2) is never identically zero.

Thus the cross-level condition used in Sections 1--3 is essential.
The example is not a counterexample to any knot invariant or to
the volume conjecture. It distinguishes an arbitrary norm-torsor
section at each root from the actual coherent pointed period.

## 5. Peripheral factors and the exact scope of the theorem

If the specified literature operator is in full ADO normalization,
first transport it by the fixed rational gauge already checked in
[the pointing note](kashaev_ado_pointing.md). Retain the actual
whole factor d_N in comparing states. Its exact evaluation is
N_N(1)=eta_N <K>_N/N; its reference residue and target jet are
those in [the preceding note](bounded_meridian_jets.md#5-the-full-ado-normalization-keeps-its-residue-and-first-jet).
No generic factor such as 1+M^N is being replaced by one.

The theorem has these inputs: a specified actual nonzero all-level
annihilator, and the independently established fixed-color identities.
It has no root rank, semisimplicity, primeness, regular-orbit, or
alternatingness assumption. It removes the extra rank/regularity
conditions of the earlier exact cofactor and value-propagation formulas.

The subsequent [finite cut-state proof](finite_sum_annihilator.md)
now independently supplies a nonzero actual all-level meridian
annihilator for every knot, so this theorem's existence input is
available. It does not prove the classical-symbol identification
with the geometric A-curve. Most importantly it does not estimate
the logarithmic growth of the actual matrix-period expression (3.2).
Comparison with the marked regulator period remains the volume theorem.
Bounded jet order and bounded initial jets alone do not rule out
cancellation in a long matrix product or prove its geometric norm.

The [exact diagnostics](../experiments/audit_all_level_a_period.py)
test moving-q germs against known polynomial solutions, including
singular steps of higher multiplicity and even/composite levels.
They also check the coherence obstruction (4.1)--(4.2) algebraically.
The [results](../experiments/all_level_a_period_results.json) are
diagnostics, not evidence that an unaudited knot operator has the
required symbol or volume growth. No novelty claim is made for the
standard recurrence or sparse-polynomial arguments.

The subsequent [affine source construction](affine_quantum_a_period.md)
retains a specified inhomogeneous source as an extension class,
with a cyclic resolvent when its homogeneous block is nonresonant.
The [adequacy argument](adequacy_and_algebraic_periods.md) proves
that fixed algebraic meridian sections cannot reproduce the
actual adequate color periods. It supplies nonsplitting tests
for this extension, without inferring the missing volume norm.

The [cyclotomic Mellin uniqueness theorem](mellin_cyclotomic_jet_uniqueness.md)
extends the same bounded-jet argument to the whole rational
root generating function. The actual source window through
orders zero to D(s-1), together with the exact cyclotomic
numerator lattice, determines every competing section and its
Kashaev residue. This does not impose a rank or semisimplicity
condition, and does not estimate that residue's growth.
