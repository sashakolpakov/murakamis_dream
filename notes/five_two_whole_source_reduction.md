# The actual whole source for the 7/3 five-crossing plat

Research note, 27 October 2026. This derives an exact finite source
formula for 5_2 from the same oriented mixed-color four-plat method
used for 4_1. All turns, the cut coupon, full Cartan scalar and
zero-framing correction are retained. Both the three-index
Gaussian/Pochhammer formula and its cyclotomic coefficient transform
are proved for the whole meridian family. At completeness the
transform gives an explicit two-index formula for the original state.

This is a diagnostic for arbitrary-bridge source transport, not a
restriction of the main volume target to the twist family. No broad
selected-period or hyperbolic-volume theorem is asserted here.

## 1. The marked plat and exact framing

Set q=exp(pi*i/N), Q=q^2, x=-M/q, Y=M^2=Qx^2, d=N-1 and
xvee=x^(-1)Q^(-1). Use

    beta=sigma_2^2 sigma_1^(-2) sigma_2.          (1.1)

Its action order is sigma_2, sigma_1^(-1), sigma_1^(-1), sigma_2,
sigma_2. With the same rational-tangle marking as in the
[figure-eight proof](figure_eight_whole_source_identity.md),

    T=[1 1;0 1], U=[1 0;1 1],
    T^2 U^2 T (0,1)^t=(7,3)^t.                 (1.2)

This is the two-bridge 7/3 plat, with continued fraction [2,2,1]
or [2,3], giving the five-crossing twist-knot diagram 5_2 in the
handedness fixed by (1.1). The actual three-braid word used in the
earlier prototype is retained as an independent finite evaluation
check in the audit; no Jones formula is used.

The top colors are [V(x),V(xvee),V(xvee),V(x)] and their orientations
are [+, -, -, +]. Every crossing has positive oriented writhe, so
the framing correction is the inverse fifth power of the actual
color twist. Put A=alpha, B=2d-alpha, so q^A=x, q^B=xvee. The full
mixed Cartan contribution is q^((3B^2-2AB)/2). Including the twist
q^(-(5/2)(A^2-2dA)) gives exactly

    q^(3dB)=xvee^(3d).                           (1.3)

Formula (1.3) is included in the contraction. Omitting either its
Cartan or framing part would change the whole meridian identity.

## 2. The same literal source has different bottom cap types

Use the exact balanced mixed R coefficients and turns from the
figure-eight proof. Cut the fourth top leg at index zero. Because
this cut is a left pivotal trace, its coupon is D_0=g E_00, and
Tr(g^(-1)D_0 C)=C_00. Thus it is the original reduced scalar cut.

The top source indices are

    (a,d-a,d,0), 0<=a<N,

and their coefficient, including the two cups and the coupon, is
N^2 x^(a-2d). The final colors are now [V(x),V(xvee),V(xvee),V(x)].
Thus the first bottom cap is ev_R(x), while the second is ev_L(x).
This differs from the figure-eight contraction and is essential.

If the surviving first output index is b and its dual partner is
d-b, then the two cap coefficients are

    x^(d-b)g_b/N=x^(-b)Q^(-b)/N,
    x^d/N,
    g_b=x^(-d)Q^(-b).                            (2.1)

All cap and cup factors are literal finite matrices. No ordinary
quantum dimension is divided out, and no separate modified trace
is assigned to each bridge.

## 3. Forced transfer elimination

Write the five transfers in action order as k_1,...,k_5. The first
positive crossing has second input index d, so k_1=0. After the
next two negative crossings write their transfers as k and ell.
The successive states are

    (a,d,d-a,0),
    (d-k,a+k,d-a,0),
    (a+k-ell,d-k+ell,d-a,0),

with

    a+k<N, 0<=ell<=k.                            (3.1)

The fourth positive crossing has transfer j<=a. The last bottom
cap forces the fifth transfer to be j-a, hence

    k_4=a, k_5=0.                               (3.2)

The final state is

    (a+k-ell,d-a-k+ell,d,0).

The first cap relation follows automatically. Thus the exact
surviving routes are (0,k,ell,a,0), with support (3.1). This
elimination uses only the actual unwrapped finite support.

Set j=k-ell, n=a+k and m=a+j=n-ell. The whole boundary factor
from the cups, cap types in (2.1), and the coupon is

    x^(-d-j) Q^(-a-j).

Multiplying by the five mixed crossing entries and (1.3), then
reflecting the two terminal Gaussian binomials, gives

    W_(a,k,ell)=(-1)^ell Y^(2d-2n+ell)
      Q^(a(k+1)+k^2+2k+2-ell*j-ell(ell+1)/2)
      {n choose k}_Q {k choose ell}_Q
      (Q/Y;Q)_k (YQ^(-n);Q)_ell
      (Q^(j+1)/Y;Q)_a.                          (3.3)

The reflection identities used here are

    {d choose a}_Q=(-1)^a Q^(-a(a+1)/2),
    {d-j choose ell}_Q
        =(-1)^ell Q^(-ell*j-ell(ell+1)/2)
                                      {j+ell choose ell}_Q.

They hold because Q has primitive order N and all upper indices
involved are less than N.

## 4. An exact whole-source Gaussian formula

Invert the ell factors of (YQ^(-n);Q)_ell in (3.3):

    (YQ^(-n);Q)_ell
       =(-Y)^ell Q^(-n*ell+ell(ell-1)/2)
                              (Q^(m+1)/Y;Q)_ell.

The signs cancel. The remaining products and binomials simplify by

    {n choose k}_Q {k choose ell}_Q
                   ={m+ell choose ell}_Q {m choose j}_Q,

    (Q/Y;Q)_k (Q^(j+1)/Y;Q)_a (Q^(m+1)/Y;Q)_ell
                   =(Q/Y;Q)_(m+ell)(Q^(j+1)/Y;Q)_ell.

Their monomial exponent becomes j(m+1)+m+ell+2. We obtain the
following proved identity for the actual reduced whole period:

    F_(5_2),N(Y)
      =sum_(m,ell>=0,m+ell<N) sum_(j=0)^m
          Y^(2(N-1-m)) Q^(j(m+1)+m+ell+2)
          {m+ell choose ell}_Q {m choose j}_Q
          (Q/Y;Q)_(m+ell)(Q^(j+1)/Y;Q)_ell.     (4.1)

Every factor is finite. This is a Laurent-polynomial identity
before setting Y=1 or Y^N=1. In particular the displayed
Y^(2(N-1-m)) is retained, including all of its meridian jets.
The exact original full ADO factor d_N(M), if desired, multiplies
both sides as its unchanged whole germ.

At N=2 the formula gives, exactly,

    F_(5_2),2(Y)=-2Y-3-2/Y,
    <5_2>_2=-7.

The sign is fixed by the above framing and source, rather than
chosen from the knot determinant.

## 5. Reciprocal Newton space and two proved boundary rows

Formula (4.1) has minimum Y exponent at least -d, term by term:
the minimum in a term is 2d-3m-2ell, and m+ell<=d. The already
proved actual Weyl symmetry F(Y)=F(Y^(-1)) therefore bounds the
maximum exponent by d as well. Consequently there are unique
coefficients C_n^(N), 0<=n<=d, in

    F_N(Y)=sum_(n=0)^d C_n^(N) T_n(Y),
    T_n(Y)=product_(r=1)^n(Y+Y^(-1)-Q^r-Q^(-r)). (5.1)

This is a statement about whole reciprocal Laurent polynomials,
not interpolation of a few root values. The T_n are monic Newton
polynomials of degree n in Y+Y^(-1), including at a root Q.

The actual anchor at Y=Q gives C_0^(N)=1. The coefficient of
Y^(-d) in (4.1) comes only from m=d,ell=0. Since
(-1)^d Q^(d(d+1)/2)=1, the top row is exactly

    C_d^(N)=Q sum_(j=0)^d {d choose j}_Q.         (5.2)

There is a useful source-basis simplification valid at every n:

    (1-Y)T_n(Y)=-Y^(n+1)(Q^(-n)/Y;Q)_(2n+1).   (5.3)

Thus the normal source has one contiguous Pochhammer rather than
two separated products. Equation (5.3) follows by inverting
(Y;Q)_(n+1) in (1-Y)T_n and joining its factors with (Q/Y;Q)_n.
It may be useful when transporting sources through arbitrary
bridge convolutions. It does not itself prove the remaining
coefficient transform.

## 6. The proved whole-source cyclotomic transform

For every primitive Nth root Q, every N>=2, and arbitrary nonzero Y,
the exact simplification is

    C_n(Q)=(-1)^n Q^(-n(n+3)/2)
                    sum_(j=0)^n Q^(-j(n+1)){n choose j}_Q,
    F_N(Y) =sum_(n=0)^(N-1) C_n(Q) T_n(Y).     (6.1)

Equivalently its inner summand is
Q^(-j(j+1)){n choose j}_(Q^(-1)). The
[direct finite proof](five_two_cyclotomic_transform_proof.md)
starts from (4.1), applies an elementary terminating three-factor
q-Chu transform and q-Vandermonde, and then uses a generic
Newton connection and a finite root Rogers-polynomial convolution.
Every parity sign and source factor is retained. The proof is
a Laurent-polynomial identity in Y; repeated ordinary-color nodes
are not used as interpolation data. Thus it includes all fixed-root
meridian jets and the normal complete-color source.

At Y=1, use

    T_n(1)=(-1)^n Q^(-n(n+1)/2)(Q;Q)_n^2.

Writing F_n=(Q;Q)_n, the original reduced Kashaev state is therefore

    <5_2>_N=sum_(0<=j<=n<N)
          Q^[-n(n+2)-j(n+1)] F_n^3/[F_j F_(n-j)]. (6.2)

This is the exact double sum used by the
[source-preserving inner quadrature](source_preserving_inner_quadrature.md).
Neither (6.1) nor (6.2) asserts saddle selection, a noncancellation
estimate, or a volume limit. The full modified-dimension function
remains its original separate factor when the full ADO period is used.

## 7. Independent checks

The [literal-path audit](../experiments/audit_five_two_whole_source.py)
starts with the original E/Cartan mixed crossing entries, the
two exact cups, the fourth-leg coupon, and the differently oriented
bottom caps. It sums all paths and checks the forced route pattern
and each surviving weight in (4.1). Twenty-seven whole contractions
at levels 2 through 10 and three meridians per level pass; eighteen
are also compared with the original six-crossing three-braid cut.
The audit checks (1.2)--(1.3), the normal-basis product identity,
the top Newton row, the proved cyclotomic values and (6.2).

The uniform proof of (4.1) is the source and transfer calculation
in Sections 1--4. The proof of (6.1) is the separate
[finite transform](five_two_cyclotomic_transform_proof.md), whose
[audit](../experiments/audit_five_two_finite_chu_bridge.py) also
compares whole-Y Laurent coefficients and checks the reusable
generic and root convolution identities. The finite checks
validate the formulas; they do not establish their all-level scope.

[Results](../experiments/five_two_whole_source_results.json).
