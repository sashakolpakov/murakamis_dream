# Torsion rigidity of the initial form and a finite generic-rank certificate

Research note, 26 October 2026. A rational root-level knot state forces
root-of-unity zeros of a fixed extremal coefficient polynomial. An
elementary cyclotomic argument reduces these zeros, outside an explicit
finite range, to finitely many binomial torsion curves contained in that
polynomial. A unique occupied curve gives generic rational rank one at
all sufficiently large levels. This extends the earlier pure-binomial
initial-form test to an initial form with an arbitrary non-toric remainder.

The argument is uniform and uses no knot census or asymptotic estimates.
It supplies a finite sufficient condition for the operator-only line in
[the ramified-fibre construction](ramified_weyl_fibre.md). It does not
prove that every knot operator satisfies that condition, retain a
geometric classical factor, or establish the regulator norm.

## 1. The initial rank bound, with the rational-coefficient scope fixed

Let L=sum_j a_j(q,Y)T^j be a specified actual polynomial annihilator,
T Y=q^2 Y T. In this note the cleared coefficients are in
Q[q^(+/-1),Y^(+/-1)]. Such an actual operator is supplied by the
[finite cut-state construction](finite_sum_annihilator.md), whose
linear equations and finite products have rational coefficients.
To pass from its M coordinate to Y=M^2, clear denominators and
separate the even and odd parts of P(M) and P(-M); both annihilate
the actual even state, and at least one is nonzero after the
possible left unit M is removed. The fixed normal gauge Y-1 also
has rational coefficients. These operations retain the specified
state and all meridian factors.
No claim is made that every minimal generator after extending
constants to C has rational coefficients.

Let r be the least Y exponent in its coefficient list, and set

    P(q,Z)=sum_j [Y^r]a_j(q,Y)*Z^j !=0.           (1.1)

Multiplying by an initial shift or a Laurent monomial allows polynomial
notation; no meridian factor is discarded. At q_N=exp(pi*i/N), put
Q_N=q_N^2, U=Y^N. The preceding
[triangular-matrix proof](peripheral_normal_period.md#7-a-fixed-initial-form-bounds-the-rational-root-period-rank)
gives, whenever the initial form specializes nontrivially,

    dim_(C(U)) ker L_N
       <=#{0<=k<N:P(q_N,Q_N^k)=0}.               (1.2)

Indeed the matrix of Y^(-r)L on 1,Y,...,Y^(N-1) is integral at
U=0 and lower triangular modulo U, with these entries on its
diagonal. The principal minor on the nonzero diagonal indices is
nonzero. This proves (1.2), counting distinct roots, not multiplicity.

The original state has a nonzero rational solution at every regular
level, by its ordinary-color anchor. Thus the right side is at least
one at those levels. We now control it using the fixed polynomial P.

## 2. An elementary root-of-unity lemma

Suppose sum_(i=1)^h c_i eta_i=0 is a minimal vanishing relation,
c_i in Q^*, eta_i roots of unity. Minimal means no proper nonempty
subsum is zero. Then every ratio eta_i/eta_j has order dividing

    R_h=product_(primes p<=h) p.                  (2.1)

Here is an independent proof of the needed form of Mann's lemma.
Divide by eta_1 and let n be the least common multiple of the
orders of the remaining roots. If p^nu exactly divides n, write
the roots using a p^nu-th root rho and roots of order prime to p.

If nu>=2, the extension from the cyclotomic field of order n/p
to that of order n has degree p. Group the relation by the powers
rho^j, 0<=j<p. Linear independence makes each grouped coefficient
zero. Minimality forces all terms into one group. Their ratios
then have order dividing n/p, a contradiction. Thus n is squarefree.

If nu=1, the degree over the prime-to-p cyclotomic field is p-1.
The sole relation between 1,rho,...,rho^(p-1) has all coefficients
equal. If p>h, at least one group is empty, so all grouped
coefficients must be zero. Minimality again forces one group and
removes p from n, a contradiction. Hence each prime divisor of n
is at most h. This proves (2.1), including p=2. The cyclotomic
degrees used here are phi(n)/phi(n/p); no torsion-point theorem
is a proof premise.

## 3. A finite list of candidate curves, with an effective exception bound

Write the collected nonzero terms of P as

    P(q,Z)=sum_(i=1)^S c_i q^(a_i)Z^(b_i), c_i in Q^*.

A monomial has no torus zeros, so assume S>=2 and put R=R_S.
At a torsion zero (q,Z), partition the terms into minimal vanishing
subrelations. Any pair in one such relation satisfies

    (q^(a_i-a_j) Z^(b_i-b_j))^R=1.               (3.1)

Thus all torsion zeros lie on a finite, explicitly specified list
of binomial curves. For each support difference put

    g=gcd(|a_i-a_j|,|b_i-b_j|),
    (a,b)=((a_i-a_j)/g,(b_i-b_j)/g).

Its candidate curves are

    C_(a,b,eta):q^a Z^b=eta, eta^(Rg)=1.          (3.2)

The exponent vector is primitive. Each such curve is irreducible
over C. It is contained in P=0 exactly when its Laurent binomial
divides P. This is a finite algebraic factor test, not an inference
from a finite list of levels.

### Bounding the isolated exceptions

Choose integers c,d with ad-bc=1. The curve has the parametrization

    q=eta^d t^(-b), Z=eta^(-c)t^a,
    t=q^c Z^d.

If it is not contained in P=0, the substituted P is a nonzero
Laurent polynomial in t over Q(eta). Its exponent width is at most

    W_(a,b)=max_i(-b*a_i+a*b_i)-min_i(-b*a_i+a*b_i).

At an intersection, multiplying by a Laurent monomial gives a
nonzero polynomial of degree at most W_(a,b). Width zero gives
no intersection. If eta has order e, then

    [Q(q):Q] <= [Q(eta,t):Q] <= W_(a,b)*phi(e)
                                             <= W_(a,b)*phi(Rg). (3.3)

Define E(P) to be the maximum of W_(a,b)*phi(Rg) over support
pairs. Also let V(P) be the maximum Rg over the vertical pairs
b=0, or zero if there are none. Contained vertical curves have
q of order at most V(P).

Therefore, if

    phi(2N)>E(P), 2N>V(P),                       (3.4)

every zero P(q_N,Q_N^k)=0 belongs to a contained *nonvertical*
curve from (3.2). Conversely every grid point on a contained
curve is a zero. This proves the required classification beyond
an explicit finite range.

For a cruder bound stated using N alone, phi(n)^2>=n/2: in the
prime factorization, each factor p^(a-2)(p-1)^2 is at least one,
except the possible factor 1/2 from p=2,a=1. Hence phi(2N)>=sqrt(N),
and N>max(E(P)^2,V(P)/2) suffices for (3.4).

## 4. Exact periodic counting, retaining the half-root

Write a contained nonvertical curve as

    q^a Z^b=exp(2pi*i*h/t), gcd(h,t)=1,

using h=0,t=1 for the root one. On the specified grid its equation is

    a+2bk = 2N*h/t mod 2N.                       (4.1)

There are no roots unless t divides 2N. If it does, the count is

    gcd(|b|,N), if 2*gcd(|b|,N) divides 2N*h/t-a;
    0, otherwise.                               (4.2)

This follows by solving the elementary linear congruence in (4.1).
The count is periodic in N, for example with period 2|b|t. It keeps
the order-2N parameter q_N and the order-N parameter Q_N distinct.
For instance Z=q has no grid points at any N, while Z=-q has one
at odd N and none at even N. Dropping the half-root would lose
this distinction.

Distinct contained nonvertical curves have disjoint grid roots
outside another explicit finite range. If their primitive exponent
vectors have nonzero determinant Delta, their intersection gives
q^Delta=eta^(b') eta'^(-b), so ord(q) divides
|Delta|*lcm(ord(eta),ord(eta')). Parallel distinct curves are
disjoint. Thus, outside a fixed range, the number in (1.2) is
exactly the sum of (4.2) over the distinct contained curves.
It is a computable periodic function of N. Multiplicities of the
binomial factors do not enter this distinct-root count.

## 5. Consequences for actual operators

First, a fixed P attached to an actual rational root period at
infinitely many unbounded levels must contain a nonvertical
binomial torsion curve. Otherwise (3.4) would rule out all such
levels. An initial polynomial without such a factor cannot be
the initial form of the specified all-level rational knot state.

For an all-level state, the eventual periodic count in Section 4
must be nonzero on every residue class. This is a finite necessary
test for a proposed rational-coefficient quantum operator. It
does not require evaluating a growing root monodromy matrix.

Second, suppose the only occupied contained curve at all sufficiently
large N is Z=q^(2s), for a fixed integer s. Other contained curves
with no grid points are harmless; arbitrary non-toric factors are
allowed. Equations (1.2)--(4.2) give

    dim_(C(U)) ker L_N <=1.

The actual nonzero state gives the opposite inequality. Hence

    dim_(C(U)) ker L_N=1 for all sufficiently large N. (5.1)

More generally the same conclusion holds whenever the finite
periodic count is exactly one. This is a finite sufficient
generic-rank certificate, extending the pure-binomial test.

If a primitive minimal actual operator B over C(q,Y) is a right
factor of the certified L, then ker B_N is contained in ker L_N
at the cofinite set where the factorization specializes. It also
contains the actual state. Thus (5.1) proves generic rank one for
B_N as well; no rational-constant-field descent of B is needed.

This supplies the operator-only pointed saturated line of
[the ramified Weyl fibre](ramified_weyl_fibre.md) for every actual
operator meeting the finite certificate. It does not prove
injectivity on its special negative sector or a bound on the
complete period.

### A rigid comparison criterion once the common operator is constructed

Suppose a second period is explicitly represented by a regular vector
v'_N(U) in the same marked orbit lattice, satisfies B_N v'_N=0 and
the same Weyl equivariance, and has the same ordinary anchor
(v'_N(1))_1/(Q_N-1)=1. If (5.1) holds for B_N, linear algebra over
the local fraction field gives v'_N=h(U)v_N. The first ordinary
coordinate of v_N is a unit at U=1, so h is regular there and
h(1)=1. Weyl equivariance makes h(U)=h(U^(-1)). Hence its germ
is a unit in R_s with value one. On the descended special fibre

    (a'_0,b'_0)=(a_0,b_0).

The complete functional therefore gives exactly the same full ADO
value; no separate asymptotic comparison of those two vectors
is needed. This argument permits analytic germs as well as
algebraic ones, provided they extend in the specified lattice.

The requirements are substantive: the second realization must be
put in this same kernel and marked lattice with the same functional.
An abstract unpointed module isomorphism does not supply them, as
the ramified shear example shows. No geometric triangulation period
satisfying these conditions has been constructed here.

### The condition is algebraically broad, with the scope kept explicit

For fixed monomial support the candidate list (3.2) is finite.
Containing any designated curve is a finite set of linear
conditions on the coefficients, obtained by the substitution in
Section 3. Requiring that none of the other occupied curves be
contained removes a finite union of closed linear conditions.
Where nonempty, the single-occupied-curve condition is therefore
Zariski open relative to the family retaining the designated curve.

This is a class of actual *operator certificates*, not a proof
that all hyperbolic, adequate, or alternating knot operators lie
in it. Establishing such a diagram-independent containment and
the geometric regulator norm remains separate work.

## 6. An actual operator example with an isolated rank jump

For the unknot normal state v_N=Y-1, let

    B=(Y-1)T-(q^2Y-1), C=1-q+T, L=C*B.

These are actual all-level annihilators of that state. The initial
form of L is

    (1-Z)(1-q+Z).

The first factor is the persistent curve Z=1. The second is
non-toric and has the grid zero Z=q^2 at q=exp(pi*i/3), N=3.
At that level B maps Y to (1-Q)Y and C kills Y, so the kernel
of L has the two independent vectors 1,Y. At the other levels
C is invertible on the monomial root basis, and B has rank N-1
by (1.2) with initial form 1-Z. Indeed a grid zero of C
would require |q-1|=1, which on q=exp(pi*i/N), N>=2, forces N=3.
Thus the generic rational rank is two at N=3 and one otherwise.

This illustrates why non-toric initial factors can create isolated
exceptions but do not require a case-by-case large-level argument.
It is an operator example for a known state, not a hyperbolic
volume-conjecture counterexample or proof.

## 7. Coverage and verification

Root-of-unity relations have existing coverage in Mann,
[On linear relations between roots of unity](https://doi.org/10.1112/S0025579300005210),
Mathematika 12 (1965), 107--117. The general torsion-coset framework
also belongs to the established theory of algebraic tori. The
coverage check used the publication metadata and scope, not its
proof. Sections 2--4 provide the needed proof from elementary
cyclotomic degrees, Laurent substitution, and congruences. No
novelty is claimed for the general root-of-unity lemma or torsion
classification. The application is the uniform finite rank test
for the specified quantum operator and its marked period line.

[The independent audit](../experiments/audit_torsion_initial_rank.py)
uses polynomial division by Phi_(2N) over Q, rather than numerical
roots, for 490 level cases. Its examples include persistent,
sporadic, vertical, parity-dependent, and unoccupied cosets. The
matrix test constructs the actual unknot annihilator above at
29 levels and detects its isolated rank jump. Its
[results](../experiments/torsion_initial_rank_results.json) are
diagnostics of the uniform algebraic proof. They contain no
geometric period or volume estimate.
