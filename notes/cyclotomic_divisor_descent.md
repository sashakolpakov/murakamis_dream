# Uniform descent of a rank-one comparison by divisor flow

Research note, 27 October 2026. This proves cases of the proposed
cyclotomic rigidity mechanism without assuming bounded degree for the
levelwise Hilbert-90 gauges. The hypotheses are instead a fixed split
divisor presentation, or an unramified nonresonant algebraic divisor
presentation, of the generic rank-one comparison coefficient.
Cyclic transport detects its divisor charges; a finite flow solves
the comparison and gives an explicit bound on its support.

This is a theorem about comparison lines, not about the entire quantum
A-module of a knot. No claim is made that the missing actual/geometric
comparison line already has the presentation or norm compatibility
required here. The volume conjecture remains unproved.

## 1. The literature category is cyclotomic q-curvature

For coverage, the abstract of
[Di Vizio--Hardouin, 1205.1692](https://arxiv.org/abs/1205.1692)
describes a generic difference-Galois group through specializations
of q at roots of unity. Their
[parameterized version, 1205.1694](https://arxiv.org/abs/1205.1694)
also records the differential structure. These are closer to the
user's proposed cyclotomic rigidity question than a scalar norm
equation at one root. Neither theorem nor proof is used below.
Only this coverage and the original meaning of cyclic transport
are invoked; all implications needed for our restricted statement
are proved directly.

Use the actual parameters q_N=exp(pi*i/N), Q=q^2 and the even
meridian Y=M^2. Let sigma(Y)=QY, with q fixed. For a rank-one
coefficient a(q,Y), its cyclic transport at level N is

    C_N(Y)=product_(j=0)^(N-1) a(q_N,Q_N^j Y),
    Q_N=q_N^2.                                  (1.1)

For a comparison line, C_N=1 means that the two compared norm
characters agree, with the full meridian function retained. This
is a whole rational identity, not only its value at Y=1.

## 2. A fixed split-divisor class

Assume a has the fixed finite presentation

    a(q,Y)=c(q) Y^s
             product_(c,u) (1-c q^(2u)Y)^(n_(c,u)), (2.1)

where c(q) is a nonzero rational function of q, s and the n_(c,u)
are integers, u ranges through finitely many integers, and the
distinct labels c are nonzero complex constants. In particular c
is not an unknown function of q or Y. We distinguish the scalar
c(q) from the finitely many constant labels in the product.

The factors are whole functions on q,Y before root specialization.
This class includes finite products of linear factors in known
q-shift orbits, with arbitrary integer multiplicities and composite
root levels. It is not every rational function of q,Y. A general
zero algebraic over C(q) need not be c q^(2u).

**Divisor-descent theorem.** Suppose C_N(Y)=1 in C(Y) for every
sufficiently large N. Then s=0 and

    sum_u n_(c,u)=0 for every distinct label c,
    c(q)=q^(2k) for an integer k.                (2.2)

There is a rational function f(q,Y), independent of N, such that

    a(q,Y)=sigma(f)/f.                          (2.3)

It can be constructed explicitly. Put

    e_(c,u)=-sum_(v<=u) n_(c,v),
    f(q,Y)=Y^k product_(c,u)(1-c q^(2u)Y)^(e_(c,u)). (2.4)

The e have finite support because their total charges vanish. No
bound or coherence for separately chosen root-level gauges is
assumed. The original fixed divisor data give the bound afterward.

## 3. Proof of the divisor and constant statements

Set U=Y^N. The elementary finite product gives

    product_(j=0)^(N-1)(1-c Q_N^(u+j)Y)=1-c^N U,
    product_(j=0)^(N-1) Q_N^j Y=(-1)^(N-1)U.

Writing m_c=sum_u n_(c,u), the hypothesis is exactly

    c(q_N)^N (-1)^(s(N-1)) U^s
                         product_c(1-c^N U)^(m_c)=1. (3.1)

All factors after U^s are units at U=0. Hence s=0, and evaluating
at U=0 gives c(q_N)^N=1. It follows also that

    product_c(1-c^N U)^(m_c)=1.                  (3.2)

There are infinitely many N for which the finitely many c^N are
pairwise distinct. To see this, a collision requires that a ratio
c/c' be a root of unity of order dividing N. Let L be the least
common multiple of all these finitely many torsion orders, or one
if there are none. Every N coprime to L avoids all collisions.
Choose such a sufficiently large N. The distinct linear factors
in (3.2) force every m_c=0.

Here is a direct proof of the scalar assertion, including its
half-root convention. The identity |c(q_N)|=1 excludes a zero
or pole of c at q=1. Choose an analytic logarithm ell(q) near
one and set

    L_N=N ell(exp(pi*i/N)) in 2pi*i Z.

Expansion of the fixed analytic function, rather than separate
level functions, gives

    L_N=N ell(1)+pi*i ell'(1)+O(1/N).

Therefore L_(N+1)-L_N=ell(1)+O(1/N^2). These differences belong
to the discrete set 2pi*i Z, so ell(1) belongs to that set and
c(1)=1. Choose the logarithm with ell(1)=0. Now L_N converges
in the same discrete set and is eventually 2pi*i k for a fixed
integer k. Thus c(q_N)=q_N^(2k) for all sufficiently large N.
The rational function c(q)-q^(2k) has infinitely many zeros,
so c(q)=q^(2k) identically. This proves (2.2).

The assumption of all sufficiently large levels matters here;
an arbitrary subsequence need not fix the scalar character.

## 4. The remaining equation is a finite flow

For each c the vertices are u in Z and the edge u->u+1 carries
the flow e_(c,u). Equation (2.4) solves the divergence equation

    n_(c,u)=e_(c,u-1)-e_(c,u).                  (4.1)

The vanishing of total charge is exactly the condition for a
finite-support flow. Since sigma(1-cQ^uY)=1-cQ^(u+1)Y, equation
(4.1) proves the product part of (2.3), and
sigma(Y^k)/Y^k=Q^k gives its scalar part.

If the u support for label c is between u_min and u_max, at most
u_max-u_min flow factors are needed. Their total absolute exponent
is at most

    (u_max-u_min) sum_u |n_(c,u)|.               (4.2)

Together with |k| this bounds the Y degrees of the rational gauge
by the fixed input data. This is one way to supply the bounded
comparison space required by
[the whole-period reconstruction theorem](whole_period_cyclotomic_rigidity.md).
It is a divisor-flow condition, rather than a nilpotence assumption
on the entire braid image.

For a rank-one module T e=a e, the new frame e'=f^(-1)e satisfies
T e'=e'. The remaining ambiguity in f over C(q,Y) is multiplication
by C(q)^*: a rational sigma-invariant in Y has no finite nonzero
pole, since its q^2 orbit would be infinite; it is Laurent in Y,
and invariance then leaves only its constant term. A specified
regular generic anchor fixes this scalar. Root-level central
functions of Y^N have not been silently identified with generic
difference constants.

### An extension to moving algebraic zeros and poles

The fixed labels in (2.1) can be replaced by more general algebraic
functions under a finite nonresonance condition. This supplies a
second, broader sufficient condition for the comparison line.

Write a rational coefficient, over its algebraic splitting field, as

    a(q,Y)=r(q)Y^s
           product_(i=1)^d (1-alpha_i(q)Y)
             /product_(j=1)^e (1-beta_j(q)Y).     (4.3)

Assume every alpha_i,beta_j is holomorphic and nonzero near q=1.
They may coincide at q=1; the hypothesis is an unramified choice of
the individual branches, not distinctness of all limiting roots.
Let C be the set of their distinct values at q=1. Assume

    c!=c' in C => c^k!=c'^k for 1<=k<=max(d,e). (4.4)

Thus distinct limiting values have no root-of-unity ratio of these
bounded orders. This is a finite condition. It is automatic if all
branches have the same limiting value, or if all distinct limiting
values are positive real numbers.

**Unramified divisor-descent theorem.** Under (4.3)--(4.4), the
identity C_N(Y)=1 for every sufficiently large N implies s=0,
d=e, r(q)=q^(2k_0), and a pairing of the branches such that

    alpha_i(q)=q^(2k_i) beta_(pi(i))(q),
                                k_i in Z.       (4.5)

Consequently a=sigma(f)/f with f in C(q,Y)^*. Its Y-degree can
be bounded by |k_0|+sum_i |k_i|. In particular no prior bound
for root-level gauges is required. The integer shifts are read
from the fixed algebraic branches:

    k_i=(alpha_i'(1)/alpha_i(1)
                   -beta_(pi(i))'(1)/beta_(pi(i))(1))/2. (4.6)

Here the derivatives and the nonresonance condition are in the
quantum parameter q. Classical etaleness of shapes over the
meridian does not automatically imply these quantum hypotheses.

We first prove an elementary uniqueness lemma. If c_1,...,c_h
are distinct nonzero complex numbers and F_i(t) are meromorphic
germs at zero, then

    sum_i c_i^N F_i(1/N)=0 for all large N       (4.7)

forces every F_i=0. Indeed, among nonzero F_i choose those with
largest |c_i|=R, and among these the least Laurent order m.
Divide (4.7) by R^N N^(-m). It follows that
sum a_i omega_i^N tends to zero, where omega_i=c_i/R are distinct
points of the unit circle and at least one leading coefficient
a_i is nonzero. Multiplying by omega_j^(-N) and taking Cesaro
means gives a_j=0: each other geometric sum has mean zero and
the error tends to zero. This contradicts the choice of m.
It proves (4.7), including roots-of-unity ratios between the c_i.

To prove the theorem, the full norm identity first gives s=0,
r(q_N)^N=1 and equality of the multisets alpha_i(q_N)^N and
beta_j(q_N)^N. Hence d=e; the scalar proof in Section 3 gives
r(q)=q^(2k_0). Fix the logarithms of alpha_i(q)/alpha_i(1) and
beta_j(q)/beta_j(1) with value zero at q=1. For a branch with
limiting value c put

    A_i(t)=exp(Log(alpha_i(exp(pi*i*t))/c)/t),
    B_j(t)=exp(Log(beta_j(exp(pi*i*t))/c)/t).     (4.8)

These are holomorphic units at t=0 because their logarithm
numerators vanish there. The k-th power-sum equality is

    sum_(c in C) (c^k)^N
       [sum_(alpha_i(1)=c) A_i(1/N)^k
                   -sum_(beta_j(1)=c) B_j(1/N)^k]=0.

For 1<=k<=d, (4.4) makes the bases c^k distinct. Lemma (4.7)
therefore gives equality of the bracketed holomorphic functions,
separately for each c and k. Newton identities, padding each
multiset to d elements with zeros, give equal multisets of the
A_i and B_j as meromorphic germs. They are units, so the
numbers of branches at each c agree. A fixed pairing satisfies
A_i(t)=B_(pi(i))(t) identically.

The exponent of their quotient in (4.8) is a holomorphic
function whose exponential is one. It is a constant 2pi*i k_i.
Thus Log(alpha_i(q)/beta_(pi(i))(q))=2k_i Log q, proving (4.5)
as an identity of algebraic branches and giving (4.6).

For k_i>0 the corresponding rational gauge over the splitting
field is product_(u=0)^(k_i-1)(1-q^(2u) beta_(pi(i))(q)Y).
For k_i<0 use the inverse product over k_i<=u<0. Their product,
times Y^(k_0), gives the stated degree bound.

This gauge descends to C(q,Y). Its finite divisor flow is the
unique finite-support solution on each infinite q-shift orbit.
Uniqueness makes that divisor invariant under the Galois group
of the splitting field. The product part has value one at Y=0,
so its normalization is Galois invariant as well. Its coefficients
therefore lie in C(q); Y^(k_0) is already rational. This completes
the proof without a general q-curvature theorem.

## 5. Tests which prevent incorrect descent

If only even N are used, the scalar a=-1 has C_N=1 but has no
nonzero rational generic gauge for sigma(Y)=q^2Y. If
f(q^2Y)/f(Y)=-1, a finite divisor is shift-invariant and hence f
is a Laurent monomial; its ratio is q^(2k), a contradiction.

Likewise the rational coefficient

    a(q,Y)=(1-q^2 Y^2)/(1-Y^2)                  (5.1)

has C_N=1 at every odd N, but at even N its transport is

    C_N=((1+U)/(1-U))^2.                        (5.2)

Indeed the exponent 2 orbit has size N/gcd(2,N). Thus odd-level
agreement alone does not justify generic descent. Formula (5.2)
is also a concrete reason to retain the peripheral factors
1+U before evaluating U=1.

The half-step factor (1-qY)/(1-Y) has transport
(1+U)/(1-U) at every actual q_N: q_N^N=-1, whereas Q_N^N=1.
It is not in the class (2.1). Its two norm characters must be
retained, just as in the actual bridge-source calculation.

There is a stronger warning for the exact chosen half-root family.
The rational coefficient

    a_*(q,Y)=(1-Y)(1-qY)/[(1+Y)(1+qY)]          (5.3)

has C_N=1 for every N at q_N=exp(pi*i/N), with no parity exception.
Its numerator norm is (1-U)(1+U), while its denominator norm is

    (1-(-1)^N U)(1-(-1)^(N+1) U),

the same product. Nevertheless a_* is not sigma(f)/f for any
nonzero rational f(q,Y). Normalize a hypothetical f by its
q-1 valuation. At q=1 it then has a finite nonzero value in C(Y).
Since sigma(Y)=q^2Y tends to Y, sigma(f)/f specializes to one.
But a_*(1,Y)=((1-Y)/(1+Y))^2 is not one.

This does not contradict either descent theorem here. The roots
in (5.3) include q-shifts outside (2.1), and its limiting labels
1,-1 violate (4.4). Nor is it evidence against a correctly
parameterized general q-curvature theorem. The selected q_N
family contains only even orders of q. At q=-q_N with N odd,
which has odd order N, the same cyclic transport is
((1-U)/(1+U))^2 and detects the obstruction.

Thus all selected root values alone still do not determine a
generic comparison. One must supply the additional parameter
symmetry or cyclotomic places, a proved divisor condition, or
the bounded quantum-normal comparison required by the whole-
period reconstruction theorem. The even parameter Q=q^2 and
the retained half-root sign must be distinguished explicitly.
In particular finite-lift evenness is not an assumed symmetry
of an unknown minimal generic operator.

There is a constructive way to choose the smaller parameter for
the actual reduced state. The new argument in
[the even-meridian note](even_meridian_norm_descent.md#a-nonzero-actual-annihilator-can-nevertheless-be-chosen-over-qq2)
applies the finite-sum annihilator proof directly to its statewise
even closed lift, with base Q and central variable Q^N. It supplies
a specified nonzero actual operator over Q(Q,Y), with shift Y->QY.
This is an existence result, not the asserted q-sign stability of
the previous half-root minimal operator. The full ADO Tate/sign
line remains separate and unchanged. An unknown comparison still
must be placed over the correctly marked field and lattice.

The gauge (2.4) can have a zero or pole at the ideal meridian.
Its generic existence does not authorize deleting that divisor
or changing the marked normal functional. It must be transported
in the specified integral lattice. Once a comparison is a unit
of the correct marked line and is fixed algebraic across levels,
the existing central normalization theorem controls its norm.
This note does not infer that unit condition from (2.3).

## 6. What this contributes to the knot program

This supplies uniform Hilbert-90 descent theorems for the stated
classes of rank-one coefficients. They start from all-level cyclic
transport, derive a bounded global gauge, and give its explicit
divisor flow. The proof is independent of knot-by-knot examples and of
the published q-curvature proofs.

To use it for the desired comparison, one still has to construct
that comparison line from the actual pointed quantum A-object,
prove its split divisor presentation or an appropriate extension,
and match its cyclic norm characters with all peripheral factors.
Rivin's algebraic geometric place is available but does not alone
supply these quantum hypotheses. The regulator connection and
selected source must still be retained. No volume theorem follows
just from the vanishing of a rational norm-one comparison class.

[Exact audit](../experiments/audit_cyclotomic_divisor_descent.py).
[Results](../experiments/cyclotomic_divisor_descent_results.json).
