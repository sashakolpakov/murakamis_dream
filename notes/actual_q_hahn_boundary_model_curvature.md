# Finite local curvature of the original boundary models

30 October 2026. The actual 220/222
determinants and the actual 202 positive polynomial have logarithmic
curvature bounded above and below by constant multiples of N, uniformly
through the fold. The other retained factors have nonlinear derivatives
of size O(s+1), where s is the channel deficit. These are finite local
source statements. No graph-rank, stationary-point, Gaussian reduction
or original-period assertion is made.

## 1. Actual clocks and the finite core factors

Put N>=3, d=N-1, theta=pi/N, q=exp(i theta), Q=q^2. Keep an ACTUAL
integer channel a with

    a0 N<=a<=floor(d/2),  a0>0,
    m=d-a, s=d-2a.

All estimates are for sufficiently large N, including either maximal
folded parity. Coefficients below range in fixed positive compact sets.
Use the exact physical half-index clocks

    U=q^-1 X, V=q^-1 Y, QUV=XY.                       (1)

The half-index is not dropped, and a is not replaced by a limiting
continuous color. The actual source determinant is

    H_a^1(U,V)=V^a K_a det[I-(qU/2)H_--(q^-1/(2V))H_+],
    K_a=[2a choose a]_Q.                              (2)

The a-by-a Hermitian positive matrices H_-,H_+ have diagonal

    d_n=1/[cos(n theta)cos((n+1)theta)], 0<=n<a,

and upper adjacent entries

    h_n^+/-=sqrt(b_n)[sin(n theta)+/-i cos(n theta)],
    b_n=sin^2(n theta)/[cos^2(n theta)
                      sin((2n-1)theta)sin((2n+1)theta)], 1<=n<a.

We take H_+ to have the plus upper entry and H_- the minus entry,
as in the [source determinant](actual_q_hahn_full_physical_complex_packet.md).
These are the original finite coefficients, including the fold endpoint.

For negative raw clocks X,Y set

    alpha=-X/2>0, beta=-1/(2Y)>0,
    M=I+alpha H_-+beta H_+.

The finite nonlinear core factors of the six models are:

* 220: det(I+alpha H_-), depending on the first raw log clock;
* 022: det(I+beta H_-), after the literal reversed reciprocity,
  depending on the second raw log clock with opposite sign;
* 222: det M, retaining BOTH actual finite clocks;
* 202: P_a(w)=sum_(k=0)^a beta_(a,k)^2 w^k, w=QUV=XY>0,
  beta_(a,k)=S_a/(S_k S_(a-k)), S_j=product_(r=1)^j 2sin(r theta);
* 200 and 002: no order-N nonlinear core is extracted here.

Every source scalar, affine phase, monomial and large-partner product
remains in the finite models of the
[correlated-band theorem](actual_correlated_boundary_band_ratio.md).
The word "core" separates a derivative calculation, not a change to
the source. Positivity below refers to real LOGARITHMIC RADII. A change
of normalized magnetic head nu changes its clock by exp(2pi i nu), so
pullback to those heads retains the factors 2pi i and the literal
incidence signs. No positivity in real magnetic-angle directions is
asserted.

## 2. An exact noncommutative determinant Hessian

Write Xmat=alpha H_-, Ymat=beta H_+, and

    A=M^-1/2 Xmat M^-1/2, B=M^-1/2 Ymat M^-1/2.

For real u,v let D differentiate alpha->alpha exp(tu),
beta->beta exp(tv). The finite matrix differentiation identity gives

    D^2 log det M
      =Tr[u^2 A+v^2 B-(uA+vB)^2]
      =u^2 Tr(Xmat M^-2)+v^2 Tr(Ymat M^-2)
                         +(u-v)^2 Tr(AB).              (3)

Indeed A+B=I-M^-1. Substitute this in Tr(A-A^2) and Tr(B-B^2)
and use cyclicity of trace. No commutativity of H_- and H_+ is assumed.
Each term on the last line is nonnegative: for example
Tr(AB)=Tr(A^1/2 B A^1/2)>=0. Since A,B are positive and A+B<I,
the first line also gives

    D^2 log det M<=a(u^2+v^2).                         (4)

For actual raw log-clock directions (u,v), equation (1) instead changes
alpha by exp(tu) and beta by exp(-tv). Thus the last square in (3)
is (u+v)^2, while the first two squares are unchanged. This sign is
part of the original second-clock normalization.

The one-variable beta=0 specialization of (3) is

    (alpha partial_alpha)^2 log det(I+alpha H_-)
               =Tr[alpha H_-(I+alpha H_-)^-2].         (5)

## 3. A finite bulk argument gives the lower bound through the fold

The actual Cholesky pivots are

    p_(n-1)=sin(n theta)/[cos(n theta)sin((2n-1)theta)],
    1<=n<=a.

Consequently, for h_n the upper entry of either H matrix,

    z*Hz=sum_(n=1)^(a-1) p_(n-1)
             |z_(n-1)+(h_n/p_(n-1))z_n|^2
                  +p_(a-1)|z_(a-1)|^2.               (6)

This is the original square decomposition; it follows by multiplying
its factors and the displayed finite trigonometric pivot identity.
Only ACTUAL rows appear. No virtual endpoint or singular extension
beyond the maximal folded matrix is used.

Select every other adjacent square whose two indices lie in a fixed
bulk interval, for example a0 N/4<=n<=a0 N/2. Their supports are
disjoint, and their number is at least cN. The pivots, h_n, row norms
and reciprocal row norms are bounded on this interval independently
of N and a. If w_j are the normalized column vectors of those squares,
they are orthonormal, and (6) gives

    Xmat>=c P,  P=sum_j w_j w_j*, rank P>=cN.          (7)

On the support of each w_j all entries of M are uniformly bounded,
since it is wholly inside that same bulk interval. Thus
<w_j,Mw_j><=C. For the spectral probability measure of M at w_j,
convexity of lambda->lambda^-2 gives

    <w_j,M^-2 w_j>>=<w_j,Mw_j>^-2>=C^-2.

Taking the trace of (7) against the positive M^-2 proves

    Tr(Xmat M^-2)>=cN.                                (8)

Apply the same argument separately to the squares of H_+ to prove
Tr(Ymat M^-2)>=cN. Their selected projections need not coincide.
The uniform lower and upper compact bounds on alpha,beta are used
here. Together with (3),(4), this proves

    cN(u^2+v^2)<=D^2 log det M<=CN(u^2+v^2).           (9)

The same proof with beta=0 and (5) proves cN<=log-radius curvature
of the 220 core<=CN. Exact reciprocity gives the 022 statement with
its recorded inverse clock. These estimates require a/N bounded
below, but no upper gap from the fold. Large final entries do not
affect the selected bounded bulk squares or their expectations.

## 4. Exact 202 curvature is a uniformly nondegenerate variance

For positive w define the probability weights

    pi_k=beta_(a,k)^2 w^k/P_a(w), 0<=k<=a.

Direct differentiation, with all finite coefficients retained, gives

    (w partial_w)^2 log P_a(w)=Var_pi(k).              (10)

Here is a uniform two-sided estimate without differentiating a limiting
Laplace formula. The EXACT consecutive weight ratio is

    R(k)=w[sin((a-k)theta)/sin((k+1)theta)]^2.

Extend its logarithm to real 0<=x<=a-1. It satisfies

    (log R)'(x)
      =-2theta sin((a+1)theta)
          /[sin((a-x)theta)sin((x+1)theta)].           (11)

Since a0 N<=a<=floor(d/2), this is at most -c/N throughout its
interval. For w in a fixed positive compact the crossing of R through
one is a distance cN from both ends: for x<=cN the numerator sine
is bounded below while the denominator is at most Cc, and the reverse
holds for x>=a-cN. Choose c small using the two bounds on w.
Thus any modal integer k_* lies in [cN,a-cN]. On a fixed smaller
bulk neighborhood of k_*, (11) has absolute value at most C/N.
The adjacent modal logarithmic ratios are consequently O(1/N).

Multiplying the exact ratios away from k_* now yields, for every k,

    weight(k)/weight(k_*)<=C exp[-c(k-k_*)^2/N].       (12)

The bulk upper bound on the ratio drops also gives a fixed positive
lower bound for that ratio whenever |k-k_*|<=2sqrt(N), for large N.
It follows by summing (12) and those central terms that

    c sqrt(N) weight(k_*)<=P_a(w)<=C sqrt(N) weight(k_*).

The upper Gaussian bound gives E[(k-k_*)^2]<=CN, hence Var(k)<=CN.
Each of the two integer shells
k_*-2sqrt(N)<=k<=k_*-sqrt(N) and
k_*+sqrt(N)<=k<=k_*+2sqrt(N) has probability at least c>0.
For independent samples K,K', the identity
Var(K)=E[(K-K')^2]/2 therefore gives Var(K)>=cN.
This proves

    cN<=(w partial_w)^2 log P_a(w)<=CN.                (13)

In the actual two raw log-clock directions this is the quadratic
form Var(k)(u+v)^2, because w=QUV=XY EXACTLY. The affine phase
(-1)^a Q^[a(a-1)/2] contributes no curvature.

## 5. Fixed holomorphic logarithmic derivatives are O(N)

The preceding finite bounds have uniform complex neighborhoods.
For a positive reference M and complex z_1,z_2 near zero,

    M(z)=I+exp(z_1)Xmat+exp(z_2)Ymat.

Conjugating its increment by M^-1/2 gives
(exp(z_1)-1)A+(exp(z_2)-1)B, whose norm is less than one half on
a fixed polydisc, because A,B are positive with A+B<I. The matrix
logarithm series is therefore convergent and

    |Log(det M(z)/det M)|<=C a.

Cauchy's formula on a smaller fixed polydisc proves that every fixed
positive-order logarithmic derivative is O(N), including mixed
derivatives and both maximal-fold parities. The same proof covers
220 by setting Ymat=0. The normalization of the logarithm is relative
to its positive reference determinant; no absolute O(N) bound on
unrelated scalar logs is needed.

For 202 the proved original negative-root theorem factors
P_a(w)=C_a product_j(w+rho_j), rho_j>0. For w in a positive compact
and small complex z, every factor w exp(z)+rho_j stays a fixed
relative distance from zero. Its marked logarithmic ratio is O(1)
uniformly in rho_j; summing over a factors and using Cauchy gives
the same O(N) bound for every fixed positive-order derivative.

In particular, changing the logarithmic base clocks by O(N^-1) changes
each core Hessian by O(1), by the third-derivative bound and integration
along that short path. This controls the ACTUAL finite-r clock
correction to the real signed limiting clocks. It does not discard
the order-one transport term in the determinant or its source phase.

## 6. The retained noncore factors have O(s+1) nonlinear cost

Use the EXACT finite models from the correlated-band theorem on its
fixed complex clock polydisc. Let z_1,z_2 denote logarithmic clock
variations; marked heads are pulled back by their actual affine lifts.
All statements below concern fixed derivatives of total order at least
two. A function linear in these logarithms has zero such derivatives,
even when its value or first derivative is large.

The root cup identity is exactly

    p_(d-s)(x)=F_s exp(pi i x) q^[(s-1)x]
                    /product_(j=1)^s(1-Q^(x+j)).       (14)

Its character is retained. At finite auxiliary clocks every denominator
is uniformly separated from zero, so each logarithmic derivative of
order at least two costs O(s). At an escaping clock of size N^2 or
N^-2, first factor its full linear monomial if necessary; the remaining
derivatives cost O(s/N^2). Physical cups have s=0 and are EXACT linear
characters, as are their inverse caps. Literal dual reversals and their
Chevalley scalar are affine substitutions with their recorded signs.

For 202/222 the retained partner product
P_s(T)=product_(r=a)^(m-1)(T-Q^r) has fixed logarithmic derivatives
O(s): its positive total neighborhood is separated from the forced
arc. For 220/022 its total has size N^2 or N^-2; after retaining the
exact leading linear monomial its nonlinear derivatives cost O(s/N^2).
These statements hold uniformly in a sufficiently small near-fold
neighborhood s<=eta N, including both folded parities.

The 200 model retains
(-1)^m Q^{m(m+1)/2}(UV)^m product_(r<m)(1-Q^r/U)
times its zero-free Bessel factor. The monomial has zero nonlinear
derivatives. The product contributes O(m/N^2)=O(N^-1), and the
Bessel logarithm contributes O(1) on its fixed zero-free complex
compact. For 002, extract the exact constant product of -Q^r from
product_(r<m)(V-Q^r); its remaining product has the same O(N^-1)
cost, and its Bessel factor has O(1) cost. No Bessel factor or phase
is discarded. The 022 reciprocity prefactor is also exactly linear
in the logarithmic heads.

All other original white monomials, half-twist channel weights, fixed
root gamma/h0 factors and physical pivotal characters are affine in
the varying logarithmic heads, or independent of them. Their actual
values and first derivatives remain part of the source; this theorem
does not assert that they satisfy a stationary equation.
An exposed coherent binomial row, including its actual first-head
normalization, is not one of these local tensor factors. Its separate
nonlinear action and curvature are not removed by this decomposition.

Consequently, for one actual local boundary model, its logarithm
decomposes locally as an AFFINE retained source term, the applicable
core from section 1, and a remainder whose every fixed nonlinear
logarithmic derivative is O(s+1). For any fixed collection of these
local factors with the literal bounded affine head substitutions, the
correction is O(S+1), S=sum deficits. This is just a derivative bound
on a finite product; it asserts no rank of that affine substitution.

Finally the actual root numerator/model ratio has a holomorphic
O(N^-1) remainder on this same fixed normalized-head neighborhood.
The logarithm and all its fixed derivatives are O(N^-1) on a smaller
polydisc. Thus it adds only that error to the local curvature estimates.
Generic quantum normals are a separate calculation and are not obtained
by differentiating this ROOT identity.

These facts identify the finite local sources of order-N curvature and
bound their retained corrections. They do not prove a transverse rank,
stationarity of the complete geometric sample for the actual labels,
a nonzero Gaussian coefficient, or an original relative-cycle pairing.

Focused audit: [finite source curvature and corrections](../experiments/audit_actual_q_hahn_boundary_model_curvature.py),
with [saved results](../experiments/actual_q_hahn_boundary_model_curvature_results.json).
An exact noncommuting matrix identity, two finite trigonometric identities
and two original half-index identities check the algebraic interfaces.
The audit reconstructs 888 original Cholesky rows and checks 63 finite
matrix Hessians, 153 bulk Jensen vectors and 126 complex preconditioned
neighborhoods through both folded parities. It checks 80 original positive
weight families, 3580 exact sine ratios, 32 separated shell masses and
16 phase-normalized polynomial derivatives. At 85 digits it also compares
30 derivatives of the original finite H sum and 30 derivatives of its
literal leading-V coefficient with the determinant derivatives, with
maximum error below 1.4e-84. Finally it checks 72 determinant logarithmic
derivatives, 144 nonlinear corrections from all six models and 72
interior/escaping cup corrections. Sample lower bounds and rates are
diagnostics; the uniform assertions are proved above.

The O(S+1) statement concerns nonlinear derivatives; source values and first derivatives remain. It makes no rank or stationary-point assertion.

This is a finite local theorem. Rank and stationarity remain separate questions.