# Full rank-one cyclotomic descent, including ramified zeros and poles

Research proof for independent audit, 27 October 2026. This extends
[the unramified Q-parameter proof](q_parameter_curvature_extension.md).
The new ingredient is a weighted sequence-uniqueness lemma allowing
finite exponential--Puiseux amplitudes. It removes both ramification
and finite-nonzero limiting-root hypotheses from that rank-one result.

This remains a comparison-line theorem. The actual geometric
comparison line, its full cyclic transport identities and its
source/cut marking must still be supplied. The original volume
conjecture is not proved here.

## 1. Statement and the coefficient-field requirement

Let sigma_Q(Y)=QY and a(Q,Y) be a nonzero element of ℚ(Q,Y). Assume
that for every sufficiently large positive integer n,

    product_(j=0)^(n-1) a(zeta_n,zeta_n^jY)=1,
    zeta_n=exp(2pi*i/n),                         (1.1)

as a whole rational identity in Y. Then there exists

    f(Q,Y) in ℚ(Q,Y)^*,
    a(Q,Y)=f(Q,QY)/f(Q,Y).                      (1.2)

No unramifiedness, limiting-root separation, or levelwise degree
bound for Hilbert-90 gauges is assumed. The conclusion is generic
rational descent. It does not assert that f is a unit at the ideal
meridian or that it preserves an unspecified period pointing.

The same conclusion over a subfield K of C holds if (1.1) is known
at every primitive n-th root for the chosen coefficient embedding.
For ℚ-coefficients this whole-root condition follows by cyclotomic
Galois conjugation. For a number field a sufficient stronger marking
is to know (1.1) for all coefficient conjugates. A single geometric
embedding is not silently promoted to that condition.

## 2. Scaled roots supply all powers without a nonresonance assumption

For a fixed positive integer k set xi_N=exp(2pi*i*k/N). Its order
is m=N/gcd(k,N). Whole-root (1.1) gives the m-step transport identity
at xi_N for all sufficiently large N. Its N-step transport consists
of gcd(k,N) repetitions and is also one.

Factor a over an algebraic splitting field as

    a(Q,Y)=r(Q)Y^s
          product_(i=1)^d(1-alpha_i(Q)Y)
            /product_(j=1)^e(1-beta_j(Q)Y).      (2.1)

Every alpha_i,beta_j is a nonzero algebraic function of Q. Its
value may tend to zero or infinity at Q=1. For sufficiently large
root orders the values themselves are finite and nonzero.

The ordinary primitive-root product first gives s=0,
r(zeta_n)^n=1 and d=e. It also gives equality of the multisets
of n-th powers of the alpha and beta values. The fixed-rational
scalar discreteness argument yields

    r(Q)=Q^(k_0), k_0 in Z.                     (2.2)

Here is that argument in full. The identities |r(zeta_n)|=1
exclude a zero or pole of r at Q=1, so choose an analytic logarithm
ell of r near one. Then

    L_n=n ell(exp(2pi*i/n)) belongs to 2pi*i Z.

The expansion of this fixed analytic germ gives
L_n=n ell(1)+2pi*i ell'(1)+O(1/n), with a convergent expansion
in powers of 1/n after the linear term. Hence
L_(n+1)-L_n=ell(1)+O(1/n^2). These differences lie in the
discrete set 2pi*i Z, so ell(1) belongs to that set and r(1)=1.
Choose the logarithm with ell(1)=0. The sequence L_n now converges
in the same discrete set and is eventually 2pi*i k_0 for a fixed
integer k_0. Thus r(zeta_n)=zeta_n^(k_0) at infinitely many roots.
The rational function r(Q)-Q^(k_0) has infinitely many zeros and
is therefore identically zero. This proves (2.2).

At xi_N use its actual order m, not a primitive N-step product
formula. Equality of the m-th power multisets, raised to the
gcd(k,N)-th power, gives equality of their N-th power multisets.
In particular

    sum_i alpha_i(xi_N)^N=sum_j beta_j(xi_N)^N  (2.3)

for every fixed k and all sufficiently large N.

## 3. Convergent Puiseux forms from a finite cover

Put t=Log Q/(2pi*i), with the logarithm near Q=1. There is a
positive integer e_0 such that, after t=s^(e_0), all branches
in (2.1) are single-valued meromorphic functions of s near zero.
Here is a direct justification of the needed analytic form.

Choose a punctured t-disk avoiding other discriminant zeros and
coefficient poles of the finite root polynomials. Local analytic
roots give a finite covering there. Its monodromy is a permutation
of finitely many roots. Taking e_0 divisible by the cycle lengths
kills this monodromy, so the pulled-back roots are single-valued
holomorphic functions on a punctured s-disk. Cauchy's elementary
root bound, after division by the leading polynomial coefficient,
bounds every root by a fixed power of |t|^(-1). Multiplying by a
sufficient power of s then gives a bounded holomorphic function,
which extends across zero. Hence each root is meromorphic there.

Since no root is identically zero, it has a convergent form

    alpha_i(exp(2pi*i*t))
       =a_i t^(nu_i) exp(lambda_i(t^(1/e_0))),   (3.1)

where a_i!=0, nu_i is rational and lambda_i is holomorphic with
lambda_i(0)=0. Choose the branch t^(1/e_0)>0 on the positive
t-axis, which contains all scaled roots used below. The beta
branches have corresponding data b_j,mu_j,eta_j.

Define

    A_i(t)=exp(lambda_i(t^(1/e_0))/t),
    B_j(t)=exp(eta_j(t^(1/e_0))/t).               (3.2)

These need not extend meromorphically across t=0. Each is of the
specific form

    exp(P(s^(-1))) g(s), s=t^(1/e_0),           (3.3)

where P is a polynomial with no constant term and degree below
e_0, and g is a holomorphic unit. Indeed separate the terms of
lambda(s)/s^(e_0) with negative s exponents; the remainder is
holomorphic. Multiplication by any algebraic/Puiseux weight changes
g to a meromorphic function after a common further ramification.
The next lemma permits these weights explicitly.

## 4. Weighted exponential--Puiseux sequence uniqueness

Fix e>=1. Consider finitely many triples (nu,a,P), with
nu rational, a!=0 complex and P a polynomial of degree below e
with P(0)=0. Let g_(nu,a,P)(s) be meromorphic germs at zero.
Merge identical triples by adding their g coefficients. If

    sum_(nu,a,P) N^(-nu N) a^N
        exp(P(N^(1/e))) g_(nu,a,P)(N^(-1/e))=0  (4.1)

for every sufficiently large integer N, then every merged g is
identically zero.

**Oscillatory estimate.** If

    phi(x)=theta x+sum_(r=1)^(e-1)b_r x^(r/e),
    theta,b_r real,

and either theta is nonzero modulo 2pi or some b_r is nonzero,
then the Cesaro mean of exp(i phi(N)) is zero.

If theta is nonzero modulo 2pi, partial sums of exp(i theta N)
are bounded. Summation by parts bounds the sum through M by
O(1+M^rho), where rho<1 is the highest fractional exponent;
the total variation of exp(i sum b_r x^(r/e)) has that bound.
If all b_r vanish the sum is bounded directly.

If theta is zero modulo 2pi, let rho in (0,1) be the highest
nonzero fractional exponent. Eventually
|phi'(x)| is comparable to x^(rho-1), and
|phi''(x)|=O(x^(rho-2)). The sum--integral error is O(M^rho),
by integrating the derivative's absolute value over unit intervals.
Integration by parts with 1/(i phi') bounds the integral by
O(M^(1-rho)); its derivative term is bounded by
the integral of |phi''|/|phi'|^2=O(x^(-rho)). Both bounds are
o(M), proving the estimate.

**Proof of (4.1).** If a merged coefficient is nonzero, choose
successively among the finitely many such terms:

1. the smallest nu;
2. the largest modulus R=|a| at that nu;
3. the lexicographically largest vector of real coefficients of P,
   ordered from the highest power down;
4. the smallest Laurent order m of g among those remaining terms.

Normalize by the common positive scale

    N^(-nu N) R^N exp(Re P(N^(1/e))) N^(-m/e).

Every term outside these selected scales tends to zero: the successive
comparisons are on the N log N, N, fractional-power and log N scales.
The normalized equality becomes

    sum_l c_l exp(i phi_l(N))+o(1)=0,           (4.2)

with at least one nonzero leading Laurent coefficient c_l. The
residual phases are distinct modulo constants: equal phases would
have the same complex a and the same complex P, and would already
have been merged. Their pairwise differences therefore satisfy
the oscillatory estimate above. Multiply (4.2) by exp(-i phi_j(N))
and take Cesaro means. Every cross term has mean zero, and the
error tends to zero, so c_j=0. This contradicts the selection of m.
It proves the lemma.

In particular, distinct pairs (nu,a) remain distinguishable when
their amplitudes are finite sums of (3.3). This weighted conclusion
is stronger than the earlier meromorphic-amplitude lemma and is
the form usable for rational partial-fraction source coefficients.

## 5. Branch pairing from all scaled power sums

At xi_N, equation (3.1) gives exactly

    alpha_i(xi_N)^N
      =N^(-nu_i N)(a_i k^(nu_i))^N A_i(k/N)^k. (5.1)

For fixed k the amplitudes in this formula are finite sums of
(3.3), with the same common ramification. Apply the lemma to
(2.3). Distinct (nu,a) remain distinct after replacing a by
a k^nu. Thus for every pair (nu,a),

    sum_(alpha_i in (nu,a)) A_i(kt)^k
                   =sum_(beta_j in (nu,a)) B_j(kt)^k.

Rescale the argument and take k=1,...,d. For each (nu,a) this
gives equality of the first d power sums of its A and B functions.
Newton identities, padding by zeros to length d, identify their
multisets over the common field of meromorphic functions on the
ramified punctured disk. Their entries are nonzero exponentials,
so the group cardinalities agree. A fixed permutation pairs
A_i=B_(pi(i)) as function germs.

The paired branches have the same nu and a. Their quotient is
therefore exp(lambda_i-eta_(pi(i))). The equality of A and B says
that (lambda_i-eta_(pi(i)))/t has exponential one. It is holomorphic
on a connected ramified punctured disk, even if initially it could
have a pole at zero. A holomorphic function with values in the
discrete set 2pi*i Z is constant. Hence

    lambda_i-eta_(pi(i))=2pi*i k_i t,
    alpha_i(Q)=Q^(k_i) beta_(pi(i))(Q), k_i in Z. (5.2)

This proves the required integral Q-shift pairing without any
assumption on ramification or limiting values.

## 6. Finite divisor flow and rational descent

For k_i>0 use the finite gauge
product_(u=0)^(k_i-1)(1-Q^u beta_(pi(i))(Q)Y).
For k_i<0 use the inverse product over k_i<=u<0. Their product,
times Y^(k_0), gives (1.2) over a finite splitting field. Its
numerator and denominator Y-degrees are each at most

    |k_0|+sum_i |k_i|.                          (6.1)

The finite divisor flow is unique on each infinite Q-shift orbit.
Consequently it is invariant under the Galois group of the splitting
field over ℚ(Q). The product part has value one at Y=0, fixing
its remaining scalar. It therefore descends to ℚ(Q,Y). This
also proves descent over K under the stated whole-root hypothesis.

The remaining generic scalar ambiguity is a function of Q alone;
a specified regular anchor can fix it. The theorem does not
discard a zero or pole of the gauge at the ideal meridian or
replace the required source/cut lattice by a generic isomorphism.

## 7. Scope for the actual A-period program

The actual reduced knot state has a rational Q-operator. This
places its rational coefficient constructions in the correct
cyclotomic field. However, the theorem applies to a specified
rank-one comparison coefficient with the full transport identity
(1.1). The current root-state data do not automatically construct
that comparison or prove its norm characters agree with a
geometric regulator realization. Those remain substantive inputs.

The proof concerns fixed rational comparison data. It neither
trivializes the whole quantum A-module nor asserts algebraicity
of the selected Mellin period, which is transcendental for the
adequate class. Algebraic comparison maps and transcendental
marked periods remain compatible.

[Ramified and weighted audit](../experiments/audit_full_rank_one_cyclotomic_descent.py).
[Results](../experiments/full_rank_one_cyclotomic_descent_results.json).
