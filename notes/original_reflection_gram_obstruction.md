# The original source has no automatic positive reflection form

27 October 2026. A universal reflection/Gram argument for the ORIGINAL
Kashaev source fails at every level: its identity value is zero while
an actual normalized unknot word has nonzero value. A two-channel
reflection square has source -2. The standard alternating three-strand
weaving transfer also cannot be made a positive Hermitian operator,
at any level N>=3, by a positive metric or a scalar phase.

These are obstructions to AUTOMATIC positivity of the original word
source or transfer. They do not rule out a separately proved positive
formula for a particular knot family, a word-dependent source
elimination, an explicitly projected positive channel, or the existing
positive squared norm of the original invariant. They do not disprove
the volume conjecture.

## 1. The original source is not a positive functional

Fix q=exp(pi*i/N), Q=q^2, N>=2, complete color
x=-q^-1=q^(N-1), and retain the original pivot

    K e_a=x Q^-a e_a, g=K^(1-N).

For b>=2 the original reduced one-cut source on actual braid
intertwiners is

    t_b(A)=Tr[(P_0 tensor g^(tensor(b-1)))A].      (1)

The all-ones first output row gives the same value on these
integer-weight-preserving words. The full source is its original
nonzero dimension factor d_N(1)=i^(N+3)/N, with the original
zero-framing line. No ordinary quantum dimension is divided out.

Since Q has exact order N,

    Tr(g)=x^(1-N)sum_(a=0)^(N-1)Q^-a=0,
    t_b(I)=0.                                    (2)

Let B_i be the original checked crossing with its own common
Cartan factor recorded, and theta its original twist factor.
Use the actual zero-framing normalized generator
Bhat_i=theta^-1 B_i. The ordinary positive Markov chain

    W_b=Bhat_(b-1)...Bhat_1

closes to the unknot and has

    t_b(W_b)=t_b(W_b^-1)=1.                       (3)

This can be checked directly without a knot-polynomial formula.
At each last-strand pivotal closure the actual positive crossing
has partial trace theta I; its inverse has theta^-1 I. For the
positive crossing evaluate on the first highest vector: the
closure forces both local indices zero, leaving g_0. For the
inverse evaluate on the first lowest vector: only its zero
transfer survives, leaving theta^-1. The root scalar-closure
identity makes those the whole partial traces. Repeating the
closures proves (3), with every original factor retained.

**No-go theorem.** There is no involution dagger on a unital
complex algebra containing these actual words, and no nonzero
scalar multiple of t_b, which makes it a positive linear
functional on all A^dagger A.

Indeed a positive functional obeys Cauchy--Schwarz. Its value
on the identity is zero by (2), so its value on every element
would be zero. Equation (3) contradicts this. Equivalently, if
the reflection Gram matrix on the channels I,W_b were Hermitian,
its upper-left entry would be zero and its off-diagonal entry
nonzero. Its determinant is negative.

For the usual anti-linear inverse-word reflection, W_b^dagger
=W_b^-1. The explicit formal braid combination A=I-W_b gives

    A^dagger A=2I-W_b-W_b^-1,
    t_b(A^dagger A)=-2.                           (4)

This is an actual source evaluation of a linear combination of
original braid words. It is not an invented negative test
functional. The full dimension/phase line multiplies both
positive and negative directions by the same fixed nonzero
scalar; no phase can turn their indefinite Gram form positive.

## 2. The original cups and caps have the same obstruction

The actual nonzero cup and cap obey

    cap cup=Tr(g)=0.

They therefore cannot be Hermitian adjoints in a positive-definite
reflection structure: that identity would be the squared norm
of the nonzero cup. This is the actual isotropic cup/cap channel
already exhibited in [the sewn-source construction](sewn_source_and_meridian_charge.md).
One marked cap changes its specified channel and gives the
normalized unknot value, but it does not convert ALL ordinary
cup/cap pairings in a multi-bridge plat into positive adjoint
pairings.

Thus drawing a braid or plat as two reflected halves is not by
itself a proof that its original scalar is a sum of absolute
squares. A valid restricted formula must prove how its actual
co-source becomes the required adjoint on the particular image
subspace, with the marked cap and all other turns retained.

## 3. Even the basic alternating weaving transfer is not positive

Let T_N=B_12 B_23^-1 on three original same-color strands. Its
two crossing scalars and zero-framing factors cancel, since
the word has writhe zero. It is the block repeated in the
alternating weaving words (sigma_1 sigma_2^-1)^m.

Consider its invariant physical total-index-one subspace with
basis |100>,|010>,|001>. Literal crossing coefficients give

    T_N|_1=[[1-Q,0,1],
             [-q,0,0],
             [0,-q^-1,1-Q^-1]].                  (5)

For example the local index-one crossing block is
[[1-Q,-q],[-q,0]] in the ordered pair |10>,|01>.
The two coefficients are rho/x=1-Q and x^-1=-q at
x=-q^-1. Multiplying the two adjacent blocks gives (5).
This is a computation in the original head, without a proposed
positive replacement crossing.

Its exact characteristic polynomial is

    (lambda-1)
      [lambda^2-(1-Q-Q^-1)lambda+1].             (6)

At N=3 it is (lambda-1)^3 but the matrix in (5) is not
identity. Thus it is nontrivially unipotent and cannot be
self-adjoint in any positive-definite Hermitian metric.

At every N>=4 the two other roots are exp(+/-i theta_N),
where

    cos(theta_N)=[1-2cos(2pi/N)]/2,
    pi/3<=theta_N<2pi/3.

They are nonreal. Every positive-metric self-adjoint operator
has real spectrum. Consequently T_N cannot be a positive
Gram operator C^dagger C after any similarity. Multiplying it
by a scalar phase cannot help: its eigenvalue 1 forces that
phase to be positive real, leaving the nonreal pair unchanged.

Nor does a fixed power remove the obstruction. For any fixed
m>=1, the positive eigenvalue condition for T_N^m would require
m theta_N to be an integer multiple of 2pi. The angle theta_N
is strictly increasing to 2pi/3, so this cannot hold for all
sufficiently large N. Indeed each admissible multiple can occur
at most once. A fixed alternating weave block therefore cannot
be converted into a positive transfer at all levels by taking
a fixed number of repetitions.

This statement concerns the transfer as an operator. A positive
scalar identity for a particular closure could still result from
source cancellation and a nontrivial finite-sum identity, as
the [actual figure-eight proof](figure_eight_whole_source_identity.md)
demonstrates. Operator positivity is stronger than that scalar
conclusion.

## 4. What remains possible for a positive high-weight channel

The unit-circle eigenpair in (6) does not exclude a separately
constructed positive spectral channel elsewhere in the tensor
module. Such a route would require at least:

1. An explicit source-compatible projection or relative source
   reduction on the actual word, rather than deleting the
   nonpositive channels from the invariant by definition.
2. A proved positive representation of the retained scalar
   with its original marked cap, phases and peripheral line.
3. A bound showing that omitted channels cannot cancel the
   desired leading contribution, plus a nonzero coupling to
   the calibrated geometric critical class.

The existing positive trace for ordinary colors does not
automatically give these facts on the Kashaev projective
color. Its quantum dimension is precisely zero, while the
modified source detects its nonsemisimple data. Nor does
Rivin uniqueness establish positivity of this quantum source.
No new positive high-weight channel satisfying these conditions
has been constructed here.

There IS already a valid positive formulation for all knots:
the [original cyclic norm](regularized_kashaev_period.md#6-a-positive-trace-norm-gives-another-exact-formulation)
satisfies H_N=|K_N|^2/N+O(poly(N)), and the
[pointed A-Gram theorem](pointed_a_gram_period.md) expresses its
equivalent pointed norm by positive polynomial coefficients.
Those constructions retain the actual source and target. They
are not an ordinary reflection-positive word trace, and their
geometric exponential estimate and source overlap remain open.
The present obstruction does not invalidate them.

## 5. Exact checks and scope

[The audit](../experiments/audit_original_reflection_gram_obstruction.py)
and [saved results](../experiments/original_reflection_gram_obstruction_results.json)
check 17 literal original-source cases, braid indices two
through four, including the normalized positive unknot chain,
its actual inverse and (4). Seven exact root tests check the
literal invariant block (5). Its characteristic polynomial
is also checked symbolically. The complex positivity conclusion
comes from the all-level proof, not from an inference about
finite-field signs.

This rules out the automatic Gram/reflection route and its
basic alternating-transfer version. It neither rules out a
separately proved positive family nor supplies a hyperbolic
volume lower bound. A genuine selected geometric-cycle or
source-compatible positive-channel theorem is still needed.
