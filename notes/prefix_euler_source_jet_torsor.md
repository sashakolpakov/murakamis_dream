# A bounded unipotent torsor transports the whole Euler word, currents and source jets

27 October 2026. The original fixed-width braid network and its full
Euler completion admit an explicit pointed gauge on every fixed
quantum-normal jet order. This gauge lies in a unipotent group whose
nilpotence length is bounded by braid index plus jet depth, independently
of N. Transporting the coupons AND the co-source preserves every
original network period. This includes local Ward defects that bare
Euler completion does not preserve.

This theorem concerns the actual quantum word/source comparison.
It does not construct the marked geometric A-period, select a
hyperbolic cycle, or estimate the size of the resulting period.
The group dimension and its matrix coefficients may grow with N.

## 1. Actual local completion and the relevant restricted algebra

Fix N>=2 and a b-strand braid, b>=2. On the original physical
heads let the integer degree be sum_i a_i, with 0<=a_i<N.
It ranges from zero to b(N-1). Let F_b be the algebra of matrices
whose nonzero integer-degree shifts are nonnegative multiples
of N, and n_b its positive-degree ideal. Then

    n_b^b=0.                                           (1)

Indeed a product of b such positive shifts would raise degree
by at least bN>b(N-1). Its zero-degree projection pi_0 is an
algebra homomorphism on F_b.

The [actual crossing-completion theorem](actual_crossing_euler_completion_and_weight_source.md)
constructs local full Euler matrices R_i^E, including their
original common scalar line, such that at the original root

    R_i^E-R_i belongs to n_b,
    (R_i^E)^-1-R_i^-1 belongs to n_b.                 (2)

Every completed signed word has the original FULL pivotal
first-cut matrix. This follows from degree, not an arbitrary
quotient of the entire Borel commutant: partial closure would
need first-output minus first-input at least N, impossible in
the original N-head. All original meridian, dimension and
framing factors remain assigned as before.

An arbitrary negative-degree coupon can detect n_b. Thus n_b
is not a null ideal in the entire endomorphism algebra, and
(2) does not license keeping local E/F coupons unchanged.
The transport below supplies the missing corrections explicitly.

## 2. Quantum-normal jets and a uniform finite correction depth

Choose the marked original root and its normal coordinate

    delta=1-Q^N.

The local coefficient ring contains the original meridian
parameters and is regular in delta where F_r=(Q;Q)_r, 0<r<N,
are units. All other original poles and source lattices remain
specified; they are not discarded by working in the generic
meridian coefficient field. Treat the common scalar/Hom lines
in their original compatible frames.

Continue the displayed finite Euler matrices by their explicit
finite kernels at generic Q. They still have shifts zero and
N, but their zero-degree part differs from the actual compressed
crossing off root. The [independent normal audit](positive_carry_completion_independent_audit.md)
proves that this difference is divisible by delta locally.
For example at N=2 the extra zero-degree term is proportional
to Q+1. Its first q-normal source is nonzero.

On jets modulo delta^(J+1), set

    j=(delta F_b)+n_b.

Then

    j^(b+J)=0, R_i^E-R_i belongs to j.                 (3)

Every product of b+J generators either contains b positive
degree shifts or J+1 factors delta. Both possibilities vanish.
This proves (3) without assuming that the continued compressed
matrices form a Hopf representation away from the root.

Both R_i and R_i^E are invertible on the local chart, including
their literal negative crossings, and have the same image
modulo j. Thus their relative units belong to 1+j.

If the bare co-source is to stay unchanged off root, one can
instead use the explicitly repaired operators

    R_i^sharp=R_i+pi_(>0)R_i^E
             =R_i^E+[R_i-pi_0 R_i^E].                 (4)

Their correction is the retained degree-zero normal coupon
delta Z_i. They preserve the original bare cut matrix as whole
meromorphic q/meridian families by (1). They are Euler matrices
plus this known normal correction, rather than uncorrected
Euler matrices. Equations (3) and (4) give two compatible ways
to retain the normal data; neither deletes that coupon.

## 3. Prefix gauges solve the word transport exactly

Write the signed actual prefix in action order as

    W_j=R_j ... R_1,
    W_j^E=R_j^E ... R_1^E,
    W_0=W_0^E=I.

Define the explicit relative prefix unit

    G_j=W_j^E W_j^-1, G_0=I.                         (5)

By (3), G_j belongs to 1+j and

    R_j^E=G_j R_j G_(j-1)^-1.                        (6)

This follows by multiplying the two adjacent prefix formulas;
it includes negative letters as literal inverses. There is no
unknown knot scalar in (5). The original source fixes the
initial frame G_0=I. If another initial unit is specified, the
same recurrence determines every G_j; the set of comparisons
is a pointed torsor under the initial group 1+j.

Put L=b+J. Every inverse and logarithm in this comparison is
an honest finite expression, for example

    G_j^-1=sum_(r=0)^(L-1)(I-G_j)^r,
    log G_j=sum_(r=1)^(L-1)(-1)^(r+1)(G_j-I)^r/r.    (7)

The group 1+j has nilpotence class at most L-1, by its
successive ideal-power filtration. This is bounded for fixed
braid index and jet depth. It is the COMPLETION-ERROR group,
not a claim that the whole actual braid transport group is
nilpotent or that its semisimple part has disappeared.

## 4. Arbitrary coupons and the original co-source have exact transports

For a coupon X_j acting at level j use

    X_j^E=G_j X_j G_j^-1.                            (8)

There is no degree restriction on X_j. Composing (6) and (8)
telescopes every internal gauge. If A is the resulting actual
network, the Euler network with these transported coupons is

    A^E=G_m A G_0^-1.                               (9)

Write the original full source as Phi(A)=Tr(D A); for example
D includes the original first-input/output row and every
pivotal closure. Its transported co-source is

    D^E=G_0 D G_m^-1.                               (10)

Ordinary matrix trace cyclicity now proves the exact pointed
network identity

    Tr(D^E A^E)=Tr(D A)                              (11)

in the assigned coefficient/source lattice, at every jet order
under consideration. The same formula applies entry by entry
to the co-source family extracting the entire first-cut matrix.
An externally retained peripheral/dimension/framing line multiplies
both sides identically. No factor such as 1+M^(2N) is replaced
by its complete numerical value during this transport.

At the root with no non-weight-preserving insertions, (2) lets
one keep the original bare source: its extra terms are invisible
by degree. At positive normal depth or with arbitrary coupons,
(10) is essential. The numerical witnesses show that omitting
it can change the period. The co-source in (10) is explicit but
generally nonlocal and word-dependent. No factorized local-cap
or diagram-independent matrix formula is asserted for it.

Although j is not an ideal on the FULL coupon algebra, this
does not obstruct finite coupon transport. If B_j=log G_j,
then B_j^L=0 as a matrix and

    (ad B_j)^(2L-1)(X)=0 for EVERY matrix X.

In the binomial expansion, each term contains B_j^L on at
least one side. Thus (8) can equivalently be computed with
at most 2L-2 nested commutators. This is the uniform finite
correction to local current coupons, including ones that
could detect the positive carry before transport.

## 5. Ward defects, meridian maps and normal source lattices

The original finite matrices specify the actual current/Ward
rows and, away from a genuine Hopf fiber, their actual defects.
Transport those generator matrices too:

    rho_j^E=G_j rho_j G_j^-1.

Their local defect obeys the exact naturality identity

    rho_j^E R_j^E-R_j^E rho_(j-1)^E
      =G_j[rho_j R_j-R_j rho_(j-1)]G_(j-1)^-1.       (12)

This transports the actual defect, rather than asserting that
it vanishes off root. Every specified Hopf-adjoint/current
expression follows by the same multiplication/inverse naturality
with its original endpoint terms and ordered coproduct retained.
It does not make the old fixed Hopf action the action in the
new Euler frame at every prefix.

With the stipulated pointed initial frame G_0=I, a two-fiber
meridian map K(M',M)=W(M')W(M)^-1 becomes

    K^E(M',M)=G_m(M') K(M',M) G_m(M)^-1.             (13)

For the logarithmic meridian connection this is

    A_M^E=(D_M G_m)G_m^-1+G_m A_M G_m^-1,
    A_M=(D_M W)W^-1.                               (14)

These are physical finite-matrix statements and do not assume
that a longitude insertion is Borel-linear in one color fiber.
The assigned external meridian scalar adapter remains on its
original line. Equations (11)-(14) preserve the actual source
identities, hence every required fixed normal jet and meridian
transport at this stage of the comparison.

The source lattice matters if external rational factors have a
normal pole. Either take jets in their originally assigned line
lattice, or retain enough extra normal orders before multiplying
by a pole of order p. A desired numerical depth J can then
require depth J+p upstream, with bound b+J+p in (3). This
does not permit specializing a zero-over-zero peripheral factor
before its whole product has been formed.

The proof uses invertible fixed-width braid prefixes. Cups,
caps or stabilization maps are not asserted to be invertible
prefix gauges. Their original closure is retained as D, and
root invariant equality for any braid presentation follows
from (2), not from inventing an off-root braided category.

## 6. What this removes on the critical path

There is now a concrete exact whole-word map from the original
quantum state and its current/jet sources to the Euler-completed
presentation. The algebraic comparison equations are solved in
bounded nilpotent depth; this does not rest on Hilbert 90 being
assumed to control a growing matrix frame. The bare root period
already agrees at arbitrary braid index, and the normal/current
source corrections are explicit in (7)-(14).

The bound concerns nilpotent DEPTH. It is not a bound for matrix
dimension, coefficient degree or operator norm as N grows.
It therefore does not prove subexponential source normalization,
a nonzero selected hyperbolic image, or the sharp logarithmic
growth. The remaining comparison must carry this specified
Euler word and co-source to the marked geometric A-period.
The general original volume conjecture remains unproved.

[The exact jet audit](../experiments/audit_prefix_euler_source_jet_gauge.py)
and [saved output](../experiments/prefix_euler_source_jet_gauge_results.json)
use the actual generic-Q N=2 crossings, their literal inverses,
the full original pivotal source and inserted negative-degree
coupons. Twenty-four cases cover braid indices two through four,
two colors and depths J=0,1,2. They verify 66 prefix comparisons,
174 transported coupon/source-jet identities and the stated
nilpotence. The tests detect 122 bare coupon failures and eight
bare quantum-normal source failures, all repaired by the proved
transport. The all-N, all-width theorem rests on (1)-(14).
