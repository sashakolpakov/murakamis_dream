# Independent proof of additive full-cyclotomic descent

Research audit and proof, 27 October 2026. The additive analogue of
the full rank-one theorem is valid with the weighted
exponential--Puiseux uniqueness lemma. The pole-order induction needs
the whole orbit function, not just its highest principal coefficient.
The proof below makes that cancellation explicit.

This concerns additive comparison torsors with trivial homogeneous
action. It does not by itself solve a residual twisted by a nontrivial
geometric companion matrix, or construct the selected knot comparison.
The volume conjecture remains unproved.

## 1. Statement and full-root propagation

Let c(Q,Y) belong to ℚ(Q,Y), sigma(Y)=QY. Suppose that for every
sufficiently large N,

    sum_(j=0)^(N-1)c(zeta_N,zeta_N^jY)=0        (1.1)

as a rational identity in Y. Then there is b in ℚ(Q,Y) such that

    c(Q,Y)=b(Q,QY)-b(Q,Y).                     (1.2)

For coefficients in a field K contained in C the same conclusion
over K(Q,Y) holds if the hypothesis is supplied at every primitive
root for the fixed coefficient embedding. The rational coefficient
case obtains these conjugate identities by Galois action. An
appropriate sufficient condition over a number field is the full
coefficient-conjugate marking of the multiplicative theorem.

For fixed k, xi_N=exp(2pi*i*k/N) has order m=N/gcd(k,N). Its
true m-step sum is zero for all sufficiently large N; the N-step
sum repeats it gcd(k,N) times. Thus these scaled roots are available
without a coprimality restriction on k,N.

## 2. Exact pole-cluster cancellation

Over a finite algebraic splitting field write the unique partial
fraction expansion

    c(Q,Y)=sum_l c_l(Q)Y^l
            +sum_(mu,r) a_(mu,r)(Q)/(1-mu(Q)Y)^r, (2.1)

with finitely many Laurent monomials, distinct nonzero algebraic
mu, and positive pole orders r. The Laurent coefficients belong
to the original rational field. Choose the common algebraic
coefficient field large enough for all partial fractions.

At a primitive m-th root, the universal orbit function is

    Psi_(m,r)(u)=sum_(j=0)^(m-1)(1-zeta_m^j z)^(-r),
    u=z^m,
    Psi_(m,r)(u)=m sum_(l>=0)
                       binom(ml+r-1,r-1)u^l.   (2.2)

This follows from expansion at z=0 and root orthogonality. The
binomial is a polynomial in l of degree r-1. Hence Psi is rational
and has an order-r pole at u=1 with highest coefficient

    Psi_(m,r)(u)=m^r/(1-u)^r
                         +lower pole orders.  (2.3)

For example this coefficient follows inductively from
Psi_(m,r+1)=Psi_(m,r)+(m*u/r) partial_u Psi_(m,r). Equivalently use
the leading coefficient m^(r-1)/(r-1)! of the binomial polynomial
in (2.2) and the order-r pole of sum l^(r-1)u^l.

Fix a root specialization outside the finite bad set and a cluster
of poles for which mu(Q)^m has the same value lambda. Let R be
the largest pole order still present. At U=Y^m=1/lambda, the
order-R coefficient of the averaged rational function is

    m^R sum_(mu^m=lambda) a_(mu,R)(Q).

It must vanish. Crucially, the entire contribution of that order
is the same universal function Psi_(m,R)(lambda U) multiplied
by this sum. It therefore vanishes identically, including all its
lower pole orders. One may now descend to R-1. Induction proves

    sum_(mu^m=lambda) a_(mu,r)(Q)=0
                         for every r,lambda.  (2.4)

This avoids mixing an order-R lower principal part with a genuine
order-(R-1) coefficient. Moving poles and their partial-fraction
weights are algebraic, so accidental collisions or poles of the
weights exclude only finitely many sufficiently near Q=1 roots,
unless the algebraic branches are identical and were already
combined.

For large m all nonconstant Laurent monomials average to zero.
The pole terms tend to zero at infinity. Comparing the remaining
constant there gives m c_0(Q)=0. Infinitely many root values
therefore give c_0(Q)=0 identically.

## 3. Weighted scaled moments detect the generic Q-orbits

At xi_N, use (2.4) at its true order m, then raise mu^m to the
gcd(k,N)-th power. For every fixed r this gives

    sum_mu a_(mu,r)(xi_N) mu(xi_N)^N=0.          (3.1)

Choose the common ramification and Puiseux forms of
[the full multiplicative proof](full_rank_one_cyclotomic_descent.md):

    mu(exp(2pi*i*t))=a t^nu exp(lambda_mu(t^(1/e))),
    A_mu(t)=exp(lambda_mu(t^(1/e))/t).

The algebraic weights a_(mu,r)(exp(2pi*i*t)) are meromorphic
in t^(1/e). They are precisely allowed by the weighted uniqueness
lemma. At each fixed scaled root k that lemma separates the
groups (nu,a), giving, after rescaling the argument,

    sum_(mu in (nu,a)) a_(mu,r)(Q(t)) A_mu(t)^k=0. (3.2)

The weights are not raised to the k-th power. Within one group,
partition the mu by identical functions A_mu. Let the distinct
nonzero functions be A_1,...,A_h and let W_l(t) be the sum of
their weights. For k=1,...,h, equation (3.2) is

    sum_l W_l(t) A_l(t)^k=0.

This matrix is a Vandermonde matrix times a diagonal matrix of
the nonzero A_l, and is invertible over the common function field
on the ramified punctured disk. Hence every W_l=0 identically.

For branches with the same (nu,a), equality A_mu=A_eta is
equivalent to

    mu(Q)/eta(Q)=Q^j for an integer j.          (3.3)

One direction is immediate. For the other, their logarithmic
difference divided by t has exponential one and therefore is a
constant 2pi*i j, exactly as in the multiplicative proof. Thus
the identical-A classes are the generic Q-shift orbits of the
pole parameters. We have proved zero total weight in each such
orbit, separately for every pole order r.

## 4. A finite additive flow constructs the rational primitive

On an orbit mu=Q^u eta write the order-r weights as a_u(Q).
Their total is zero. Define the finite cumulative flow

    e_u=-sum_(v<=u) a_v,
    b_(eta,r)=sum_u e_u/(1-Q^u eta Y)^r.        (4.1)

Then sigma b_(eta,r)-b_(eta,r) is the required pole contribution,
because the coefficient at index u is e_(u-1)-e_u=a_u. For a
nonzero Laurent exponent l, use the primitive

    c_l(Q)Y^l/(Q^l-1).                         (4.2)

The constant Laurent coefficient has already been shown to vanish.
The sum of (4.1)--(4.2) solves (1.2) over the splitting field.

The pole flow is the unique finite-support flow on its infinite
Q-orbit. Since c is rational over ℚ(Q), Galois permutations preserve
the resulting whole pole part. The Laurent part is already rational.
Choosing the free constant in that Laurent part to be zero therefore
gives b in ℚ(Q,Y). The same descent works over K(Q). Any two rational
solutions differ by a rational sigma-invariant, hence by a function
of Q alone.

This is generic rational descent. Pole divisors of b at the ideal
meridian remain part of its lattice. A source-compatible marked cut
or normal residue cannot be inferred from (1.2) alone.

## 5. The finite nilpotent extension consequence

Combining the full multiplicative and additive results gives a
direct finite induction for upper-triangular comparison transport.
Suppose an upper-triangular rational matrix B(Q,Y) has identity
cyclic monodromy at every sufficiently large primitive root. Its
diagonal coefficients have norm one, so the multiplicative theorem
trivializes them by rational diagonal gauges. The matrix is now
unipotent and its root monodromy remains identity.

The first superdiagonal of its monodromy is the cyclic sum of that
superdiagonal of B. The additive theorem removes it by a rational
unipotent gauge. After this removal the second superdiagonal has
the same property; continue by distance above the diagonal.
Only finitely many steps occur, at most the nilpotence class.
This proves rational triviality for the stated upper-triangular
comparison object.

It does not assert nilpotence of the original braid image, nor
triangularity or identity curvature for the unknown actual/geometric
comparison. Those inputs must be established. A twisted source
residual (sigma-C)b=Delta is not automatically the untwisted problem
(1.2).

[Exact independent audit](../experiments/audit_additive_cyclotomic_descent.py).
[Results](../experiments/additive_cyclotomic_descent_results.json).
