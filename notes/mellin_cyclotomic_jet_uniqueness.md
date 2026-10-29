# Cyclotomic Mellin functions are fixed by bounded quantum jets

Research proof, 27 October 2026. In the actual Fourier--Mellin
polarization, a bounded number of quantum jet levels fixes the whole
rational root function, not only a selected scalar multiple of it.
The normal-order bound is independent of N. The source, formal
starting lattice and cyclotomic pole lattice are all necessary inputs.

This extends the existing
[bounded-jet operator-period reconstruction](all_level_a_period.md)
from one coefficient to the whole rational Mellin fiber. The sparse
valuation and recurrence arguments are the same ones; no novelty is
claimed for them. The new scope is arbitrary competing root sections,
without a rank, semisimplicity, scalar-ratio or minimality hypothesis.

The result is uniqueness, not a construction of a regulator section
satisfying those exact data or an estimate of its residue. In particular
it does not prove the volume conjecture.

## 1. The actual operator, source and pole lattice

Use the specified actual Q-only color recurrence

    P=sum_(j=0)^d a_j(Q,Y)T^j, TY=QYT,
    sum_j a_j(Q,Q^r) C_(r+j)(Q)=0, r>=1,

with d>=1, a_0 a_d!=0, and Laurent-polynomial coefficients after
one fixed denominator clearing. Retain the actual colors, source
and conventions of
[the Fourier--Mellin construction](fourier_mellin_actual_source.md).
Let A be the Q-exponent span, D the Y-exponent span, and s the
number of collected monomials of a_d. Choose a fixed

    n_0>=d+A+1, B=D(s-1), k=B+1.

The actual formal series and its exact source are

    Z(Q,X)=sum_(r>=n_0) C_r(Q) X^r,
    P^M Z=mathcalB(Q,X),
    P^M=sum_(j,ell) a_(j,ell)(Q) Q^(-ell*j) X^(-j) S^ell,
    S f(X)=f(QX).

The Laurent polynomial mathcalB is fixed by the d actual colors
C_(n_0),...,C_(n_0+d-1). Its full quantum jets are retained,
rather than just its value at one root.

At Q_N=exp(2pi*i/N), the actual root section Z_N is rational.
Let

    p_<(N,X)=sum_(r=1)^(n_0-1) C_r(Q_N) X^r.

The exact color periodicity proved in
[the cyclotomic residue theorem](cyclotomic_mellin_residue.md)
gives the pole lattice

    (1-X^N)[Z_N(X)+p_<(N,X)]
           in X C[X], of degree at most N.               (1)

It also gives Z_N in X^(n_0)C[[X]] and

    K_N=Res_infinity Z_N(X)dX/X.

Condition (1) is more than having simple finite cyclotomic poles:
it fixes the allowed polynomial part at infinity as well.

## 2. Finite reconstruction theorem

For all sufficiently large N, let W_N be a rational function with

    W_N in X^(n_0)C[[X]],
    (1-X^N)[W_N+p_<] in X C[X], degree<=N.                (2)

Put Q=Q_N(1+epsilon), R_k=C[epsilon]/(epsilon^k). Suppose
there is a polynomial truncation

    Wtilde_N=sum_(r=n_0)^N w_r(epsilon)X^r,
    w_r in R_k,
    w_r(0)=[X^r]W_N,

whose source equation has the correct coefficients in the finite
window

    [X^m](P^M Wtilde_N-mathcalB)=0 in R_k,
                   n_0-d<=m<=N-d.                      (3)

Then exactly W_N=Z_N. In particular its residue is the original
Kashaev value K_N.

There are k=B+1 quantum levels in (3): orders zero through B.
The number of X coefficients grows with N, but the required
quantum normal order does not. No bounded X-degree is assumed
for higher actual quantum jets; only the indicated finite window
is used. Truncating the actual formal Z at X^N supplies one such
lift, since omitted higher coefficients cannot enter that window.

### Proof

Subtract that actual truncation and write its coefficients as
e_r(epsilon), with e_r=0 for r<n_0. Coefficient comparison in
the exact Fourier ordering gives

    sum_(j=0)^d a_j(Q,Q^m)e_(m+j)=0 in R_k.               (4)

Indeed the factor Q^(-ell*j) in the Fourier transform cancels
the j-part of the shift on the exponent m+j, leaving Q^(ell*m).
No square-root or index offset is suppressed here.

For r>=n_0 set

    h_(r-d)(Q)=a_d(Q,Q^(r-d)),
    mu_(r-d)=ord_(Q=Q_N) h_(r-d),
    M_r=sum_(t=n_0)^r mu_(t-d).

All h_(r-d) are nonzero Laurent polynomials: r-d>A prevents
collisions of distinct Q^uY^v monomials after Y=Q^(r-d).
Each has at most s monomials, hence its nonzero-root vanishing
order is at most s-1 by the logarithmic-derivative Vandermonde
argument already proved in the operator-period note.

The points Q_N^(r-d), n_0<=r<=N, are distinct. For all large
N the Laurent polynomial a_d(Q_N,Y) is not identically zero;
it has at most D nonzero roots. Thus

    M_N<=D(s-1)=B.                                      (5)

These statements exclude only finitely many levels of the fixed
coefficient field. They do not assume regular propagation at
every color.

Induct in (4), with m=r-d. All earlier error coefficients
are divisible by epsilon^(k-M_(r-1)). The other operator
coefficients are regular in epsilon. Since h_(r-d) is a unit
times epsilon^mu_(r-d), it follows that

    e_r in epsilon^(k-M_r) R_k.                         (6)

This remains valid in the truncated ring: the annihilator of
epsilon^mu consists of epsilon^(k-mu) multiples, with at least
the divisibility claimed in (6). By (5), k-M_r>=1 through
r=N. Hence every root coefficient through X^N agrees.

Subtract the two pole conditions (1)--(2). The polynomial
(1-X^N)(W_N-Z_N) has degree<=N, and all its coefficients
through that degree are zero by (6) and the common starting
lattice. It vanishes identically. This proves the theorem.

## 3. A literal unknot example shows why root data are insufficient

The actual unknot has C_r(Q)=1. The following nonminimal
operator is nonetheless an actual all-level annihilator:

    P=(T-Q)[(1-QY)T-(1-Y)]
      =(1-Q^2Y)T^2+(1+Q)(QY-1)T+Q(1-Y).                (7)

The inner bracket applied to 1 is (1-Q)Y; the outer T-Q
kills it. Here D=1, s=2, so B=1 and k=2. Its exact Fourier
operator and source, for any fixed admissible n_0, are

    P^M=X^(-2)(1-X)(1-QX)(1-S),
    Z(Q,X)=X^(n_0)/(1-X),
    mathcalB=X^(n_0-2)[1-Q^(n_0)+(Q^(n_0)-Q)X].          (8)

At the root, for every constant lambda,

    W_N=Z_N+lambda X^N/(1-X^N)                          (9)

has the same affine source, starting lattice, prescribed prefix
and cyclotomic pole lattice. It has residue 1+lambda instead
of 1. This is an alternative root section of an ACTUAL unknot
operator, not a different knot invariant.

No nonzero lambda in (9) has the first normal lift (3).
One way to see this is (4) at m=N-2: its earlier errors are
zero, and h_(N-2)=1-Q^N has a simple zero, so the first
normal equation forces e_N(0)=0.

There is also a whole-function obstruction, not just the
coefficient argument. Write U=X^N, f(U)=lambda U/(1-U).
After canceling the nonzero rational prefactor in (8), a
first-order homogeneous lift would require

    (1-S_0)g_1=N U f'(U), S_0 g(X)=g(Q_N X).

The cyclic average of its left side is zero, whereas that
of its right side is N^2 U f'(U), nonzero if lambda!=0.
This argument is valid in C((X)) as well as in C(X).
Thus the required two jet levels are genuinely necessary
in this actual example. Root operator, affine source and
pole lattice by themselves do not determine the residue.

## 4. Relation to the selected-line and regulator questions

[The selected Mellin-line theorem](actual_mellin_normal_source_rigidity.md)
uses the observable source quotient to remove central scalar
multipliers at first normal order, without semisimplicity.
The present result also handles additions in the homogeneous
source-kernel, as illustrated by (9); it uses the larger fixed
jet budget and the exact cyclotomic pole lattice.

The theorem gives a finite exact target for a proposed whole
comparison. Such a candidate still must supply (2)--(3), with
the actual source and coefficients through the stated orders.
An algebraic classical optimizer or a local geometric Gaussian
does not yet supply that lift or its global pole behavior.
No hyperbolic-volume growth follows from uniqueness alone.

Verification: [script](../experiments/audit_mellin_cyclotomic_jet_uniqueness.py)
and [results](../experiments/mellin_cyclotomic_jet_uniqueness_results.json).
The [independent proof audit](mellin_cyclotomic_jet_uniqueness_independent_audit.md)
checks the finite Fourier window, truncated-ring valuation
induction, pole numerator reconstruction and sharp actual
unknot obstruction.
