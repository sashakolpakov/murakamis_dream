# Cyclotomic descent for rational sources and unipotent torsors

Research proof, 27 October 2026. This addresses the source extension,
rather than only its multiplicative norm line. The proof uses the
weighted sequence-uniqueness lemma proved in
[full rank-one descent](full_rank_one_cyclotomic_descent.md), and
finite flows on rational partial-fraction orbits. No published
q-curvature theorem is used as a premise.

The result is uniform in the number of source coordinates. It applies
to a specified rational unipotent comparison with whole cyclotomic
transport identities. Constructing that comparison for the actual
knot period, and verifying its source and peripheral lattice, remain
necessary. The volume conjecture is not proved by this conditional
descent theorem.

## 1. An additive descent theorem

Let k be the rational number field, let sigma(Y)=QY on k(Q,Y),
and take c in k(Q,Y). Suppose
that for every sufficiently large integer N,

    sum_(j=0)^(N-1) c(zeta_N,zeta_N^j Y)=0,
    zeta_N=exp(2pi*i/N),                          (1)

as an identity of whole rational functions of Y. Then

    c(Q,Y)=b(Q,QY)-b(Q,Y)                         (2)

for some b in k(Q,Y). Conversely (2) implies (1) at every level
where its rational specializations are defined.

There are no hypotheses on the ramification or limiting values of
the moving poles at Q=1. The ambiguity in b is precisely k(Q).
The theorem does not assert regularity of b at the ideal meridian.

The same proof works over a subfield k of C if (1) is given at every
primitive root for the chosen coefficient embedding. For rational
coefficients this follows from Galois conjugation. For a number
field, knowing the chosen principal root alone is not silently
treated as knowing all its coefficient conjugates.

## 2. Partial fractions and the charges seen by a root fiber

Over a finite algebraic splitting field of k(Q), write uniquely

    c(Q,Y)=sum_m c_m(Q)Y^m
          +sum_(mu,r>=1) a_(mu,r)(Q)/(1-mu(Q)Y)^r. (3)

The first sum is a finite Laurent polynomial; all mu are nonzero
algebraic functions, and the second sum is finite. The partial
fraction part is proper at infinity and has no pole at zero. All
identities below omit the finitely many root levels at which a
coefficient specialization fails or two distinct pole functions
coincide. A nonzero algebraic function has only finitely many such
specialization zeros on its finite algebraic cover.

At a primitive N-th root set U=Y^N and D_U=U partial_U. For r>=1,

    sum_j (1-mu zeta_N^j Y)^(-r)
      =N/(r-1)! product_(ell=1)^(r-1)(N D_U+ell)
                                         (1-mu^N U)^(-1). (4)

For r=1 this is the elementary geometric-series identity, first as
a power series and then as a rational identity. Applying the
operators (D_Y+ell) proves the general formula. Its pole at
U=mu^(-N) has exact order r with nonzero highest coefficient.

Terms with the same mu^N in (4) give exactly the same rational
function. Compare the highest remaining pole order in (1), then
descend in r. At every cluster C of equal values mu(zeta_N)^N,

    sum_(mu in C) a_(mu,r)(zeta_N)=0              (5)

for each r. Laurent polynomials have no finite nonzero poles and
do not affect this comparison. In particular, for each r,

    sum_mu a_(mu,r)(zeta_N) mu(zeta_N)^N=0.       (6)

For xi_N=exp(2pi*i*k/N), with fixed positive integer k, its actual
order is m=N/gcd(k,N). Apply (5) at order m and raise the common
m-th powers to the gcd(k,N)-th power. This proves

    sum_mu a_(mu,r)(xi_N) mu(xi_N)^N=0            (7)

for every sufficiently large N. It does not use a primitive
N-step formula at a nonprimitive scaled root.

## 3. Generic orbit charges from the weighted rigidity lemma

Choose the common convergent Puiseux forms near Q=1 provided by
the elementary finite-cover argument in the rank-one note. Put
t=Log Q/(2pi*i), and write

    mu(exp(2pi*i*t))=a_mu t^(nu_mu) exp(lambda_mu(t^(1/e))),
    A_mu(t)=exp(lambda_mu(t^(1/e))/t),             (8)

where a_mu!=0, nu_mu is rational, and lambda_mu(0)=0. The
coefficients a_(mu,r)(exp(2pi*i*t)) are meromorphic Puiseux
germs after the same further finite ramification.

At xi_N, (7) becomes a sum of terms

    N^(-nu_mu N)(a_mu k^(nu_mu))^N
                 a_(mu,r)(exp(2pi*i*k/N)) A_mu(k/N)^k. (9)

The weighted exponential--Puiseux uniqueness lemma separates every
pair (nu_mu,a_mu). It applies to the partial-fraction weights as
well as to the exponentials; those weights need not be units.
For each such pair, and every positive integer k, it gives the
identity of punctured analytic germs

    sum_(mu in pair) a_(mu,r)(exp(2pi*i*t)) A_mu(t)^k=0. (10)

Here the argument was rescaled from kt to t after applying the
lemma. These are identities of functions, not only formal jets.

Group equal functions A_mu. If A_1,...,A_h are the distinct
nonzero functions in one pair and w_i is the sum of its weights,
then (10) for k=1,...,h has coefficient matrix (A_i^k). Its
determinant is a nonzero product of the A_i and their pairwise
differences in the field of meromorphic functions on the ramified
punctured disk. Hence w_i=0 for every i.

Within a fixed (nu,a), equality A_mu=A_eta is equivalent to

    mu(Q)/eta(Q)=Q^v for an integer v.            (11)

Indeed exp((lambda_mu-lambda_eta)/t)=1 forces the exponent to be
a constant in 2pi*i Z on the connected punctured cover. Conversely
(11) has this property. Thus the generic additive orbit charges
vanish:

    sum_(mu in each Q-shift orbit) a_(mu,r)(Q)=0  (12)

for every pole order r. The rational-function identities follow
from the analytic germ identities because these coefficients are
algebraic functions of Q.

## 4. A finite flow solves the transport equation

On one infinite orbit write mu_v=Q^v mu_0, and set a_v equal to
the coefficient in (3), or zero if that pole is absent. The a_v
have finite support and sum zero. Define

    e_v=-sum_(u<=v) a_u.

Then e_v has finite support, and

    b_orbit=sum_v e_v/(1-Q^v mu_0 Y)^r

satisfies sigma(b_orbit)-b_orbit=sum_v a_v/(1-Q^v mu_0 Y)^r.
The equality follows coefficientwise from e_(v-1)-e_v=a_v.
This flow is unique among finite-support flows on that orbit.

The total proper partial-fraction solution b_pole descends to
k(Q,Y). One way to see this is to apply any splitting-field
automorphism tau. The difference tau(b_pole)-b_pole is invariant
under Y->QY. A rational invariant has no finite nonzero poles,
since their Q-orbits would be infinite; its remaining Laurent
polynomial is therefore constant in Y. Both proper parts vanish
at infinity, so that constant is zero. Thus b_pole is Galois
invariant.

Subtract its coboundary from c. The remaining Laurent polynomial
still has zero cyclic sum at all sufficiently large roots. Its
nonzero powers sum to zero once N exceeds the largest absolute
value of their nonzero exponents,
so its constant coefficient obeys N c_0(zeta_N)=0 at infinitely
many Q-values. Consequently c_0=0. Finally

    b_Laurent=sum_(m!=0) c_m(Q)Y^m/(Q^m-1)

solves the Laurent part. This proves (2), its field of definition,
and the stated constant ambiguity. The construction does not
throw away the factors Q^m-1 or any Y-meridian factor in b.

## 5. Unipotent and Heisenberg descent

Let C(Q,Y) be a d-by-d upper unitriangular rational matrix. Use
the column transport equation

    sigma(v)=C v,
    C_[N]=sigma^(N-1)(C)...sigma(C) C.            (13)

If C_[N] specializes to I at Q=zeta_N for every sufficiently large
N, then there is a rational upper unitriangular G such that

    C=sigma(G) G^(-1).                          (14)

To prove this, filter strictly upper triangular matrices by their
distance above the diagonal. In the first surviving diagonal of
C-I, multiplication adds the entries, so (13) says exactly that
their cyclic sums vanish. Solve each by the additive theorem and
gauge by a unitriangular matrix carrying those solutions. This
kills that diagonal. The cyclic curvature remains identity,
because it transforms by conjugation with the specialized G.
Repeat through the finite d-1 diagonals. The process terminates
and gives (14). Only finitely many bad root levels are introduced
by each fixed rational gauge.

For the Heisenberg matrix

    C=[1 u w; 0 1 v; 0 0 1],
    G=[1 p r; 0 1 q; 0 0 1],

the equations are explicitly

    sigma(p)-p=u,
    sigma(q)-q=v,
    sigma(r)-r=w+u q.                           (15)

The first two are additive. With these solved, set

    G0=[1 p 0;0 1 q;0 0 1].

Then sigma(G0)^(-1) C G0 has only central entry w+u q.
Its cyclic curvature is identity, so the additive theorem solves
the last equation. This retains the central cross term; solving
only the two abelian equations would miss the regulator coordinate.

Two solutions of (14) differ on the right by a constant
upper unitriangular matrix over k(Q). A regular specified anchor
can fix that ambiguity. A generic gauge alone need not preserve
the integral cut lattice or the complete meridian specialization.

The combination with multiplicative descent also proves the same
existence assertion for every invertible upper triangular rational
C, with G upper triangular. Each diagonal entry has cyclic norm
one, so the rank-one theorem supplies its rational diagonal gauge.
Apply that diagonal gauge first; the remaining matrix is upper
unitriangular and the finite induction above applies. This covers
a rationally split full flag without assuming unipotence in advance.

In particular an affine source over such a flagged homogeneous
module is handled by the augmented triangular matrix

    C_aff=[C c; 0 1].

If its full cyclic curvature is identity, the theorem solves its
source together with the homogeneous transport. A rational gauge
can be chosen with bottom row (0,...,0,1), so its top-right column
is precisely an affine particular solution. This is stronger than
solving the homogeneous norm while leaving the source arbitrary.

## 6. What this supplies to the proposed A-torsor argument

This gives the requested group-theoretic termination in a precise
setting: finite unipotence makes all transport equations solvable
after their whole cyclotomic curvature has vanished. It includes
the Heisenberg group underlying the marked regulator torsor, and
is independent of crossing number, bridge number, or knot family.

It does not infer that a general quantum A-module is unipotent.
If the relevant comparison is a rank-one homogeneous line with
a source, first trivialize the line by the full multiplicative
theorem, then apply the additive theorem to its transformed source.
More generally the triangular result handles every rationally split
full flag and its affine source. A flag appearing only on a formal
normal completion has not thereby supplied that rational flag.

Rivin's positive maximizer supplies a marked algebraic geometric
branch. The theorem here would descend an already constructed
rational quantum/geometric comparison from its full cyclotomic
transport identities, without choosing unrelated levelwise gauges.
The actual comparison, its whole transport identities, its source
and cut anchor, and the selected regulator norm still have to be
proved. Algebraicity of the critical shape does not supply those
identities by itself.

The [regulator applicability audit](regulator_curvature_obstruction.md)
makes the word comparison essential. A regular rational family with
identity absolute curvature has a rationally trivial differential
limit, even if its initial rational gauge is singular at Q=1. The
marked regulator's logarithmic residues exclude such absolute
triviality. Nor does equality of two noncentral matrix curvatures
make their whole Hom curvature identity. The relative comparison
object and its specified flat subobject must be constructed first.

[Exact audit](../experiments/audit_additive_unipotent_cyclotomic_descent.py).
[Audit results](../experiments/additive_unipotent_cyclotomic_descent_results.json).
[Independent proof audit](additive_cyclotomic_descent_independent_audit.md).
