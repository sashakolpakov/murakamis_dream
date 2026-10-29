# Independent audit of the printed GSWZ v2 definitions

Audit date: 25 October 2026. Scope: *The Habiro ring of a number field*,
arXiv:2412.04241v2, posted 27 August 2025; PDF title-page manuscript date
13 August 2025. The checked PDF has 73 pages and SHA-256
`308d1dd1c42bd979e5d5c31d9d95215a1808f604031b49c0ce2a1eb767273de9`.
This audit was separately requested by the user. It checks the proposed
examples against the printed definitions, rather than assuming either
the paper's theorems or the proposed criticisms.

Primary sources: [v2 PDF](https://arxiv.org/pdf/2412.04241v2) and
[v2 HTML](https://arxiv.org/html/2412.04241v2). Page numbers below are
the printed PDF page numbers. PDF pages 9, 29 and 35 were also inspected
visually; the relevant formulas agree with the HTML and extracted text.

**Result.** The two structural counterexamples are valid under the
printed definitions. Definition 1.4 is not closed under pointwise
addition, and the span in Definition 1.3 need not be finitely generated.
The Gaussian normalization and rank-one recurrence errors are also
present in the PDF. These findings do not directly disprove the
restricted arithmetic membership assertion in Theorem 5.

## 1. Printed conventions that matter

Definition 1.1, equation (13), p. 7, defines the actual Habiro ring
using the exact p-adic equality

    f_m(x+zeta_(pm)-zeta_m)=phi_p(f_(pm))(x).

The coefficient Frobenius fixes rational constants. At primes inverted
in R the completion is zero, so the paper explicitly treats those
gluing conditions as vacuous.

Definition 1.3, equations (20)--(22), p. 9, allows

    f_m in epsilon_m(xi)^(1/m)
             (R_p^[zeta_m]^*+x K_p[zeta_m][[x]]), (m,p)=1.

Only the constant coefficient has an integrality/unit condition.
The bracket placement really allows all higher coefficients in the
fraction field; it is not the bounded-denominator ring
R_p^[zeta_m][[x]][1/p]. The local module is the H_(R_p^)-span of
all sections satisfying the printed logarithmic Frobenius test.

Definition 1.4, equations (23)--(24), p. 10, indexes all m>=1.
It imposes membership in these local spans and, for every gamma>0,

    f(q^gamma)^gamma f(q^(-1)) in H_(R[1/gamma])|_gamma.

The restriction on the right tests only orders coprime to gamma.
This is not an implicit restriction to orders prime to Delta:
the paragraph immediately preceding Theorem 5, p. 14, explicitly
changes the earlier all-order definition to that narrower setting.

No quotient by independent root phases is printed in Definition 1.4.
For xi=0 the coefficient torsor has a trivial frame and the examples
below are actual rational scalar collections. A coherent change of
coefficient frame changes both compared sections by the same unit;
their relative sign and the addition obstruction are unchanged.
Quotienting the scalar collections by arbitrary componentwise phases
would also make their stated pointwise addition undefined, so would
be a different construction requiring a new definition.

## 2. The global zero-class set is not an additive group

Take K=Q, R=Z[1/6], Delta=6 and xi=0. Define constant series

    f_2=-1, f_m=1 for m!=2.

Every relevant prime p is odd. On orders m prime to p, q->q^p
preserves the order, so f(q^p)/f(q)^p=s/s^p=1 for s=+/-1.
The regulator term for xi=0 vanishes. Hence f is itself an
admitted invertible local section for every non-vacuous local test.

For equation (24), at an order m coprime to gamma, both substitutions
q->q^gamma and q->q^(-1) preserve that order. The tested constant is
f_m^(gamma+1). If m!=2 it equals one. If m=2, coprimality forces
gamma odd and it again equals one. Thus every global tested
collection is identically one, so f belongs to the printed H_(R,0).

Actual Habiro gluing with p=5,m=2 instead requires

    -1=1 in Z_5[zeta_10],

which is false, even after reduction modulo 5. Thus f does not belong
to H_R. This contradicts H_(R,0)=H_R in Theorem 2, p. 10.

Moreover 1 and f are both admitted. Their sum h=1+f has h_2=0
and h_10=2. Its local-span condition holds because a span is additive;
it is not being rejected merely because one constant term is zero.
The global gamma=1 test requires h(q)h(q^(-1)) to lie in H_R.
Its constants at orders 2 and 10 are 0 and 4, so p=5 gluing would
require 0=4. Therefore h fails Definition 1.4.

This proves directly that the global set is not closed under addition.
The argument uses neither Theorem 1 nor a nonzero K-theory class.

## 3. The local span is not finitely generated

Fix the same K,R,xi and p=5. Equation (14), p. 7, identifies the
local base ring with

    H=product_((m,5)=1) Z_5[zeta_m][[x]].

Only the integral projection H->Z_5[[x]] at m=1 is needed below;
no surjectivity or abstract product-decomposition theorem is used
in the finite-generation obstruction.

For every a>=1 define u^(a) by

    u_1^(a)(x)=(1+x)^(5^(-a)),
    u_m^(a)(x)=1 for m>1, (m,5)=1.

These are formal binomial series in Q_5[[x]] with constant coefficient
one, as allowed by equation (20). At the m=1 germ q=1+x, the exact
formal identity (q^5)^(5^(-a))=(q^(5^(-a)))^5 makes the quotient in
equation (21) equal one. Every other local component is one, and
the order is preserved under fifth powers. Hence all u^(a) are
admitted invertible sections, with linear coefficient 5^(-a) at m=1.

Let M be their full module as defined, i.e. the H-span of every
admitted invertible section. Every element of M has integral
constant coefficient at m=1: all defining sections do, and finite
H-linear combinations preserve it.

If g_1,...,g_r generated M, write

    g_(i,1)=A_i+B_i x+O(x^2), A_i in Z_5, B_i in Q_5.

Choose B>=0 so that every B_i lies in 5^(-B)Z_5. For h_i in H,
the coefficient of x in sum h_i g_i is a sum of terms
C_i B_i+D_i A_i, with C_i,D_i in Z_5. It therefore remains in
5^(-B)Z_5. It cannot produce 5^(-a) when a>B. This contradiction
proves that M is not finitely generated, and in particular not free
of rank one as asserted in Theorem 1, p. 9.

No analytic radius condition is imposed by the printed definition.
Requiring later continuation or integral slopes would be an added
hypothesis, not a property established by the defining test.

Lemma 3.4, equation (184), p. 39, separately requires the linear
coefficient to be integral. Corollary 3.5 retains that requirement,
and Lemma 3.6 equation (195), p. 41, explicitly includes it. The
counterexamples exploit exactly this missing condition in (20).
Adding it excludes these fractional-power examples, but a complete
repair still requires checking all subsequent uses. It does not
remove the constant-sign obstruction in Section 2.

## 4. The printed Gaussian normalization leaves a forbidden term

Equation (110), p. 28, defines formal Gaussian contraction on
R[[w,w^3/h,h]]. Equation (114), p. 29, gives the purported normalized
input. Already m=1,k=0 disproves that normalization.

From the defining Pochhammer product, independently,

    log(q*z*exp(w);q)_infty
       =-sum_(n>=1) z^n exp(nw)q^n/[n(1-q^n)], q=exp(h)
       =Li_2(z exp(w))/h+(1/2)Li_1(z exp(w))+O(h).

The quadratic term in the polar Taylor expansion is
Li_0(z)w^2/(2h). The printed exponential subtracts Li_0(z)w^2/h,
leaving -Li_0(z)w^2/(2h). This monomial is outside the stated domain:
nonnegative powers of w,w^3/h,h cannot have exponents (2,-1).

At w=0 its regular logarithm is -log(1-z), so the printed psi has
value (1-z)^(-1)+O(h), rather than 1+O(h).

This is not merely a choice of a scalar Gaussian phase. The n-th
power of the unwanted quadratic term has w^(2n)h^(-n); Gaussian
contraction contributes h^n, so infinitely many nonzero terms enter
the coefficient of h^0. In the formally allowed A=0 case of the
t-deformed construction, equation (119) gives Lambda=-Li_0(z).
The extra exponential then cancels the Gaussian kernel exactly.
This example concerns the formal construction before t=1; the
degenerate z=0 specialization for A=0 is not being offered as
admissible data for the arithmetic Theorem 5.

For general m the necessary polar subtractions are

    Li_2(z^m)/(m^2 h),
    Li_1(z^m)w/(m h),
    Li_0(z^m)w^2/(2h).

The regular constant logarithm of the product must also be subtracted,
where (114) adds it. These corrections follow by splitting the
Pochhammer product into its m residue classes and expanding each
factor. They identify the intended local normalization; they do not
verify the repaired global identification theorem.

## 5. Equation (165) has the stated sign error

Definition (32), p. 12, gives in rank one A=1,m=2,k=0

    H(t)=1+q^3 t^2/[(1-q)(1-q^2)]+O(t^4).

For sigma H(t)=H(qt), the coefficient of t^2 in
(1-sigma)(1-q^(-1)sigma)H is q^3. The printed right side of
equation (165), p. 35, gives -q^3. Thus the recurrence fails as
printed independently of the Gaussian issue.

For the general rank-one congruence series, let n=k+mj. Its
coefficients have successive ratio

    c_n/c_(n-m)=(-1)^(A*m)
       q^(A*m*n-A*m*(m-1)/2)/(q^(n-m+1);q)_m.

It follows that the corrected operator recurrence is

    product_(r=0)^(m-1)(1-q^(-r)sigma)H(t)
       =(-1)^(A*m) q^(A*m*(m+1)/2)
                                  t^m sigma^(A*m)H(t).

The q-exponent in the operator prefactor is unchanged; the sign is
(-1)^(A*m). The coefficient of sigma^(A*m) on the previous term is
q^(A*m*(k+m(j-1))); extracting coefficients must retain that factor.
The finite q-binomial expansion gives the product on the left.

## 6. Scope and implications for this project

Theorem 5 explicitly restricts to root orders prime to Delta. The
global collection in Section 2 becomes identically one there because
its exceptional order 2 disappears. It therefore does not disprove
Theorem 5's restricted arithmetic membership assertion. The local
error still occurs at the good prime 5 and order 1, but it is not
itself a counterexample to membership of the particular series
constructed in Theorem 5. That restricted statement needs a separate
audit with corrected definitions and formulas; it has not been
verified or disproved here.

The distinctions are:

| Printed claim | Independent finding |
| --- | --- |
| Definition 1.3 / Theorem 1 | The admitted span need not be finitely generated. |
| Definition 1.4 / Theorem 2 | The all-order zero-class set is not additive and differs from H_R. |
| Equation (114) | Wrong polar subtraction and constant normalization; input leaves the stated Gaussian domain. |
| Equation (165) | Wrong sign, with a direct coefficient correction. |
| Restricted Theorem 5 | Not directly refuted by these examples; not independently verified here. |

No result from this paper has been used as a premise of the project's
A-curve torsor proofs. In particular these findings do not by
themselves affect the independently derived finite cyclic norm
equation or its Hilbert-90 comparison. They do rule out importing
the printed unrestricted module theorems without repair.

The exact diagnostics in `experiments/audit_gswz_printed_definitions.py`
check the constant tests, fractional-power Frobenius identity,
Gaussian expansion, and recurrence coefficients. The all-order
arguments and the non-finite-generation proof are those above,
not extrapolations from finite computations.
