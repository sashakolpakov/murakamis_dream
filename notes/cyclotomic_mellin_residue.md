# The actual Fourier--Mellin period has a cyclotomic residue

Research note, 27 October 2026. The actual operator and finitely many
fixed-color values define a bounded-source Fourier--Mellin object.
At every root its selected section has a rational continuation with
only simple finite cyclotomic poles. Its residue at infinity is exactly
the original Kashaev invariant, with no jet-rank assumption.

The color-periodicity input is proved directly from integral Weyl
modules and the original root ribbon evaluation. It is not assumed
from a cyclotomic expansion or used as a Jones asymptotic theorem.
The geometric regulator norm of this residue remains unproved.

## 1. The specified operator period

Use the actual reduced fixed-color functions C_n(Q) of
[the color-pointing theorem](all_level_a_period.md), with Q=q^2,
and C_n(1)=1. The [Fourier--Mellin construction](fourier_mellin_actual_source.md)
gives, from a specified actual operator and a fixed starting color n_0,

    Z(Q,X)=sum_(n>=n_0) C_n(Q) X^n,
    P^M Z=B(Q,X),                               (1.1)

where P^M is the quantum-torus transform Y->S_X,T->X^(-1),
S_X f(X)=f(QX). The nonzero Laurent polynomial B uses only the d
fixed colors C_(n_0),...,C_(n_0+d-1). The formal lattice
Z in X^(n_0) ℚ(Q)[[X]] makes this source equation unique.

For N>=n_0 the selected period is already

    K_N=[X^N]Z(Q_N,X), Q_N=exp(2pi*i/N).         (1.2)

This note promotes its root fiber to a whole rational function and
identifies its exact residue. The generic section in (1.1) is still
defined formally; convergence at generic Q is not asserted.

## 2. Integral Weyl colors specialize through all dimensions

On D_m with basis u_0,...,u_m use

    H u_j=(m-2j)u_j, K u_j=q^(m-2j)u_j,
    E u_j=[m-j+1]_q u_(j-1), F u_j=[j+1]_q u_(j+1). (2.1)

These are the same integral colors used in the independently proved
[threading calculation](ado_threaded_shadow.md). At q=q_N=exp(pi*i/N),
E^N=F^N=0 on every D_m, including m>=N.

The generic universal R also specializes correctly on these colors.
Indeed a coefficient of E^k tensor F^k divided by [k]_q! on
u_a tensor u_b has its factorial part

    [k]_q! {m-a+k choose k}_q {b+k choose k}_q.  (2.2)

The Gaussian coefficients are Laurent polynomials. Thus every term
with k>=N vanishes at the root, while each k<N term is precisely
the original truncated root R. The inverse has the same property.
Cartan phases are nonzero and retained. This proves specialization
without dividing by [N] or evaluating a singular change of basis.

The generic zero-framed long-knot operator on D_(n-1) is
C_n(Q) times identity. Its regular specialization is therefore
the scalar C_n(Q_N) on the integral root module. The original
ordinary pivot K may be replaced by g=K^(1-N) here: on D_m they
differ by the scalar (-1)^m, as do their twists. A b-strand knot
of writhe w consequently has unchanged reduced scalar, since
(-1)^(m(b-1-w))=1. This retains the root ribbon conventions needed
to compare with the ADO color.

For clarity the long-knot operator is natural under an intertwiner
of its color. Follow the single component from its cut and multiply
the universal R legs, antipodes and pivot factors in their traversal
order. The result acts on each color; no independently colored
closed component remains. Every intertwiner commutes with these
actions. Equivalently, sliding its coupon along crossings and bends
uses exactly R-naturality and the evaluation/coevaluation identities.
Thus a nonzero color map between two scalar long-knot operators
forces equality of their scalars. The matrix specialization in
(2.2) makes this argument valid for root subquotients as well.

## 3. One-dimensional shifts preserve the reduced zero-framed knot

Let C_h be the one-dimensional root module with H=h,K=q^h,E=F=0,
where h=kN. On an integer-weight color V with weights m-2j its
double braiding is the scalar

    q^(hH)=(-1)^(km).                           (3.1)

Here is a direct statewise proof retaining its half-Cartan phase.
Tensoring V on the right by C_h changes E to (-1)^k E, leaves F
unchanged, adds h to H and multiplies K by (-1)^k. Put

    s_0=q^(h^2/2)(-1)^(km),
    g_h=q^((1-N)h) in {+1,-1}.

The exact full checked crossing, on a route with first input index a
and first output index c, changes by

    r'_sign/r_sign=s_0^sign (-1)^(k(c-a)).        (3.2)

Indeed the Cartan phase supplies q^(h^2/2)(-1)^(k(m-a-b)) and
the k_transfer-th nilpotent term supplies (-1)^(k k_transfer).
The actual index update makes a+b+k_transfer congruent to c-a
modulo two for both crossing signs. Inverse crossings give the
inverse constant s_0 and the same state sign.

The integer position coboundary gives sum(c-a)=0 on every closed
state. Thus all state-dependent signs in (3.2) cancel. The crossing
constants contribute s_0^w, the closed pivots contribute g_h^(b-1),
and the twist ratio is (s_0 g_h)^w. Their total is

    g_h^(b-1-w)=1.                              (3.3)

This proves that the reduced zero-framed knot scalar is unchanged
by tensoring with C_(kN). No auxiliary closed component or its
quantum dimension has been inserted. In particular the full Cartan
half-phase cancels with its specified twist before any root value
is suppressed.

## 4. Exact root periodicity, including multiples of N

Write n=kN+r, 0<=r<N. If r>0, the span of
u_r,...,u_(n-1) is a submodule of D_(n-1): its first E coefficient
is [n-r]=[kN]=0. The quotient on u_0,...,u_(r-1) is exactly

    D_(r-1) tensor C_(kN).                      (4.1)

The E coefficients are (-1)^k[r-j], the F coefficients are [j+1],
and the H and K shifts agree with the displayed tensor product.
Naturality and Section 3 therefore give C_n(Q_N)=C_r(Q_N).

If r=0, the first N basis vectors instead form a submodule:
F u_(N-1)=[N]u_N=0. This submodule is

    D_(N-1) tensor C_((k-1)N).                  (4.2)

The N-dimensional D_(N-1) is the actual Kashaev color after a unit
rescaling by [j]_q!, j<N. Hence C_n(Q_N)=C_N(Q_N)=K_N.
All maps use nonzero subquotients; no quantum dimension is divided
out at a multiple of N.

We have proved, for every knot and every N>=2,

    C_(n+N)(Q_N)=C_n(Q_N), n>=1,
    C_(kN)(Q_N)=K_N, k>=1.                     (4.3)

Combining this with the original finite-color identity for 1<=r<N
gives the uniform meridian form

    C_n(Q_N)=F_N(Q_N^n), n>=1.                 (4.4)

The fixed-color functions are Laurent polynomials in Q with rational
coefficients. Galois conjugation therefore gives the corresponding
identities at every primitive Q-root. This does not alter the full
ADO parity/Tate line; (4.3) concerns the reduced scalar.

For coverage, periodic root values are part of the existing
cyclotomic-color framework: see
[Le, Section 4.8](https://letu.math.gatech.edu/Papers/Lectures_Luminy_2014_new.pdf)
and [Murakami, 1606.00125](https://arxiv.org/abs/1606.00125) for explicit
low-order periodic patterns. No cyclotomic integrality or periodicity
proof from those sources is a premise above.

## 5. The rational fiber and its residue

Define the canonical start-one series Z_1(Q,X)=sum_(n>=1)C_n(Q)X^n.
Equation (4.3) gives its root rational continuation exactly:

    Z_1(Q_N,X)
      =[sum_(r=1)^(N-1) C_r(Q_N) X^r+K_N X^N]/(1-X^N). (5.1)

Equality holds first as formal series at X=0 and hence as its
specified rational function. For any fixed n_0>=1,

    Z(Q_N,X)=Z_1(Q_N,X)-sum_(r=1)^(n_0-1) C_r(Q_N)X^r. (5.2)

Thus it has at most simple poles at the N-th roots of unity. The
subtracted polynomial has no constant term. Since Z_1 tends to
-K_N at infinity, the residue convention Res_infinity(dX/X)=-1
gives the exact operator-period identity

    K_N=Res_(X=infinity) Z(Q_N,X) dX/X
       =-sum_(gamma^N=1) Res_(X=gamma) Z(Q_N,X) dX/X. (5.3)

It is also the normalized sum of values of the numerator in (5.1):
each finite residue is -P_N(gamma)/N and root orthogonality kills
all r=1,...,N-1 terms. The identity includes the case K_N=0.

This gives a genuine whole rational root fiber of the specified
bounded-source A-object. If its Fourier operator is defined at
Q_N, it satisfies P^M_N Z=B_N as a rational identity, because the
formal source identity specializes coefficientwise and rational
functions with the same formal expansion agree. No new solution
is selected after specialization. Uniqueness is the generic
source/lattice statement of Section 1, not an assumed invertibility
of the singular root operator.

The full original ADO value at the ideal meridian remains
eta_N K_N/N, eta_N=i^(N+3). The residue formula is for the reduced
scalar K_N; it does not remove this marked normalization line.

## 6. The volume target in this polarization

For the very same source-defined solution, the desired theorem is

    lim_(N->infinity) (2pi/N)
        log|Res_infinity Z(Q_N,X)dX/X|=Vol(S^3 minus K). (6.1)

Equation (5.3) proves that this is exactly the original conjecture.
It does not prove (6.1). The Fourier symbol is the transform of the
actual chosen operator's symbol; its geometric component and the
selected residue's regulator norm still require proof. A root pole
or a rational continuation alone gives no exponential lower bound.

[Exact independent module/state audit](../experiments/audit_cyclotomic_mellin_residue.py).
[Results](../experiments/cyclotomic_mellin_residue_results.json).
