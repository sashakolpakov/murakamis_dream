# Full cyclotomic transport removes the limiting-root nonresonance condition

Independent extension, 27 October 2026. The coefficient field and the
quantum parameter matter. For a rational coefficient in the true
parameter Q, all-level principal-root transport identities propagate
to all primitive roots by Galois conjugacy. Repeated shorter orbits
then supply transport at scaled roots approaching Q=1. This removes
the limiting-root nonresonance assumption in the unramified rank-one
descent argument.

The proof below is elementary and independent of any general published
q-curvature theorem. It concerns a specified comparison line. It does
not construct that line for the actual selected knot period, identify
its marked source, or prove the volume conjecture.

## 1. The actual reduced state admits a Q-only annihilator

I checked the new construction in
[the even-meridian note](even_meridian_norm_descent.md) against the exact
crossing formulas and the
[finite-sum annihilator proof](finite_sum_annihilator.md). There is a
useful stronger identity for its integer-exponent step.

At a crossing write a_t for the first input index and c_t for the
first output. The x-power contributed by a positive crossing is
-(a_t+c_t), and by a negative crossing it is a_t+c_t. The remaining
pivot/framing contribution is (N-1)kappa_D, where
kappa_D=w-b+1 is even for a knot braid. Consequently

    E=(N-1)kappa_D
           +2 sum_negative a_t-2 sum_positive c_t
           +sum_all(c_t-a_t).                    (1.1)

The last sum is zero on each closed state, as the exact integer
position coboundary. Thus

    E/2=(N-1)kappa_D/2
                      +sum_negative a_t-sum_positive c_t. (1.2)

This is manifestly integral affine-linear on the closed-flow lattice.
No additional parity saturation or half-lattice assertion is needed.
Replacing x^E by (Y/Q)^(E/2) therefore leaves a proper Q-product sum
with integer-valued quadratic Q exponents and step-one Pochhammers.

The filtered dimension bound, boundary strata and finite-moment repair
of the existing proof apply with base Q, shift Y->QY and Z=Q^N.
Stripping the common central factor (Z-1)^h before specialization
gives a nonzero operator over the rational field in Q,Y. Factorials
have lengths below N, so their root specializations are regular.
This verifies the claimed existence result, conditional only on that
already supplied finite-sum proof. It does not prove q-sign symmetry
of a different minimal generator defined on half-roots. The full ADO
sign and modified-dimension line remain exactly those of the original
state.

## 2. Whole-root transport and the scaled-root lemma

Let sigma_Q(Y)=QY and let a(Q,Y) be a nonzero rational function. For
any complex Q where its coefficients are defined put

    C_n(Q,Y)=product_(j=0)^(n-1) a(Q,Q^jY).       (2.1)

Assume first a belongs to ℚ(Q,Y), and that for every sufficiently
large n,

    C_n(zeta_n,Y)=1 in C(Y),
    zeta_n=exp(2pi*i/n).                         (2.2)

The fixed coefficient denominators exclude only finitely many root
orders. Galois conjugation over ℚ takes (2.2) to

    C_n(zeta_n^r,Y)=1 whenever gcd(r,n)=1.       (2.3)

Fix a positive integer k, and set

    xi_N=exp(2pi*i*k/N), g=gcd(k,N), m=N/g.

Its order is m and it is a primitive m-th root. For all sufficiently
large N, m is above the finite exceptional range, so (2.3) gives
C_m(xi_N,Y)=1. The N-step orbit consists of g identical m-step
orbits, hence C_N(xi_N,Y)=C_m(xi_N,Y)^g=1.

One must not replace the nonprimitive orbit product by the primitive
formula 1-alpha^N Y^N. Instead use its actual order m. The identity
at that order gives equality of the multisets of m-th powers of
the numerator and denominator roots. Raising those multisets to
the g-th power gives equality of their N-th powers. This is the
only root-power implication used below.

The scaled-root lemma requires all sufficiently large orders, not
merely primes or one residue class. The half-root alias in
[the divisor note](cyclotomic_divisor_descent.md) is excluded by using
the true shift parameter Q and the full cyclotomic family.

More generally the argument applies over any subfield K of C provided
(2.3) is supplied for the fixed coefficient embedding. A sufficient
condition for a number field K is that (2.2) is known for every
coefficient conjugate of a in a finite normal closure of K. Indeed,
apply a cyclotomic automorphism to the appropriate inverse coefficient
conjugate. A statement at one chosen geometric embedding alone is not
silently promoted to this stronger Galois marking.

## 3. Unramified full-curvature descent

Assume a(Q,Y) belongs to ℚ(Q,Y) and has the full-order norm property
(2.2). Write over its splitting field

    a(Q,Y)=r(Q) Y^s
           product_(i=1)^d(1-alpha_i(Q)Y)
             /product_(j=1)^e(1-beta_j(Q)Y).     (3.1)

Assume all alpha_i and beta_j admit holomorphic nonzero branches
near Q=1. Coincident limiting roots and root-of-unity ratios between
different limiting roots are allowed. There is no nonresonance
assumption on those limiting values.

**Theorem.** One has s=0, d=e and r(Q)=Q^(k_0). The branches can be
paired so that

    alpha_i(Q)=Q^(k_i) beta_(pi(i))(Q),
                              k_i in Z.         (3.2)

There is a rational gauge f in ℚ(Q,Y)^* with

    a(Q,Y)=f(Q,QY)/f(Q,Y).                      (3.3)

Its numerator and denominator Y-degrees can each be bounded by
|k_0|+sum_i |k_i|. In particular the degree bound is deduced from
fixed branch data, rather than imposed on levelwise Hilbert-90
gauges. The shifts are

    k_i=alpha_i'(1)/alpha_i(1)
                         -beta_(pi(i))'(1)/beta_(pi(i))(1). (3.4)

If a has coefficients in K and the whole-root hypothesis (2.3)
holds, the same proof gives f in K(Q,Y).

### Preliminary scalar and exponential-sequence facts

At a primitive root the product formula gives

    r(zeta_N)^N (-1)^(s(N-1)) U^s
       product_i(1-alpha_i(zeta_N)^N U)
          /product_j(1-beta_j(zeta_N)^N U)=1,
    U=Y^N.

Its U-valuation gives s=0, its value at U=0 gives
r(zeta_N)^N=1, and its factorization gives d=e and the equality
of the indicated root multisets. The scalar discreteness argument
of the divisor note, now with Q_N=exp(2pi*i/N), gives r(Q)=Q^(k_0):
choose a logarithm ell at Q=1, use
N ell(exp(2pi*i/N)) in 2pi*i Z, first take consecutive differences
to get r(1)=1, then take the limit to make these integers constant.
The rational identity follows from infinitely many root values.

We also use the following directly proved uniqueness fact. For
distinct nonzero constants c_1,...,c_h and meromorphic germs F_i(t),

    sum_i c_i^N F_i(1/N)=0 for all large N       (3.5)

implies every F_i=0. Among nonzero germs choose the largest modulus
R of the c_i, then the smallest Laurent order of those germs.
After division by R^N and that common power of 1/N, the identity
is a finite sum sum a_i omega_i^N tending to zero, with distinct
unit complex omega_i and at least one nonzero a_i. Multiplying by
omega_j^(-N) and taking Cesaro means gives a_j=0, a contradiction.
The lower-modulus terms vanish exponentially and the remaining
errors tend to zero, so the averaging is justified. Root-of-unity
ratios between distinct c_i cause no problem in this lemma.

### Separation at scaled roots, without separating c^k

Let C be the finite set of distinct limiting branch values at Q=1.
Use logarithms vanishing at Q=1 and define the holomorphic units

    A_i(t)=exp(Log(alpha_i(exp(2pi*i*t))/alpha_i(1))/t),
    B_j(t)=exp(Log(beta_j(exp(2pi*i*t))/beta_j(1))/t). (3.6)

Fix an integer k between 1 and d. The scaled-root lemma implies
equality of the N-th root-power multisets at xi_N=exp(2pi*i*k/N).
Their first power sums therefore give

    sum_(c in C) c^N
       [sum_(alpha_i(1)=c) A_i(k/N)^k
                    -sum_(beta_j(1)=c) B_j(k/N)^k]=0. (3.7)

The bases here are the distinct c, not c^k. Apply (3.5) to the
holomorphic bracketed functions of 1/N, then rescale their argument
by k. It follows that for each c and every k=1,...,d,

    sum_(alpha_i(1)=c) A_i(t)^k
                      =sum_(beta_j(1)=c) B_j(t)^k. (3.8)

Newton identities, with zeros padding each multiset to length d,
give equality of these multisets over the field of meromorphic
germs. Their entries are units, so the cardinalities at each c
agree. A fixed permutation pairs A_i identically with B_(pi(i)).

The quotient of the logarithms in (3.6) has exponential one and
is holomorphic. It is therefore a constant 2pi*i k_i. This gives
Log(alpha_i/beta_(pi(i)))=k_i Log Q, proving (3.2) and (3.4).

### Rational descent and the degree bound

For a pair with k_i>0 use the gauge

    product_(u=0)^(k_i-1)(1-Q^u beta_(pi(i))(Q)Y).

For k_i<0 use the inverse product over k_i<=u<0. The product of
all these gauges, times Y^(k_0), proves (3.3) over the splitting
field and gives the stated degree bound.

The finite divisor flow solving div(a)=sigma(div f)-div f is
unique on each infinite Q-shift orbit. Because a is rational over
ℚ(Q), its flow divisor is invariant under the Galois group of a
finite splitting field. The product part is normalized to one at
Y=0, so its multiplicative scalar is invariant as well. Thus the
gauge descends to ℚ(Q,Y). The same argument works over K(Q).
This completes the proof.

## 4. What the theorem does not remove

The unramified branch hypothesis remains. It concerns zeros and
poles as functions of the quantum parameter Q, not merely classical
shape etaleness over M. No claim is made here that every rational
comparison has that property, or that the actual unknown comparison
line has been constructed.

Nor does (3.3) itself preserve the ideal-meridian lattice. The gauge
can carry a zero or pole on that divisor. The source, cut functional,
and full ADO sign line must be transported in their specified lattices.
A rational generic comparison fixes neither an arbitrary root-central
scalar nor the nonzero coefficient of the selected regulator period.
Those require the original pointing. This theorem is a new sufficient
descent tool for that comparison problem, not the volume theorem.

[Exact audit](../experiments/audit_q_parameter_curvature.py).
[Results](../experiments/q_parameter_curvature_results.json).
