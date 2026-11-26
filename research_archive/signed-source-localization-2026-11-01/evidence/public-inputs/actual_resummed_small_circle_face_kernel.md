# Exact resummed small-circle face kernels and a local norm obstruction

30 October 2026. All assertions concern the
literal root kernel of the [homogeneous original-source theorem](actual_homogeneous_casimir_face_source.md).
The formulas retain the Chebyshev cancellations before absolute values. They
neither identify a shared-face capacity with representation volume nor bound
the complete source. No generic-q normal or filling asymptotic is asserted.

Put d=N−1, q=exp(pi i/N), s_j=2sin(pi j/N), S_j=prod_(v=1)^j s_v,
and c_j=q^(2j+1)+q^(−2j−1). The actual face operator is

    T b^j=−c_j b^j+s_j^2(x+y)b^(j−1)+s_j s_(j−1)xy b^(j−2).

Physical missing endpoint arrows are literal zeros. Let U_n be the monic
Chebyshev polynomial U_0=1,U_1=T,U_(n+1)=T U_n−U_(n−1). Then

    H_h=U_(h−1)(T) sum_(j=0)^d b^j c^(d−j).

No absolute value of a Newton expansion is taken below.

## 1. Closed finite rational generating function for every coefficient

Fix input j, outer powers a,beta, and put r=a+beta, i=j−r>=0.
Let S range over nonoverlapping dimers of the interval {i+1,...,j}.
A dimer with upper endpoint k is {k−1,k}; no two share an endpoint.
Write ell=|S| and omit terms unless ell<=min(a,beta). Put

    w_S=prod_(v=i+1)^j s_v^2 / prod_({k−1,k} in S)(s_k s_(k−1)),
    V_S={i,...,j} minus {k−1 : {k−1,k} in S},
    D_v(u)=1+c_v u+u^2.

If A_h(j;a,beta) is the coefficient of
x^a y^beta b^(j−a−beta)c^(d−j) in H_h, then EXACTLY

    sum_(h>=1) A_h(j;a,beta) u^(h−1)
    =sum_S binom(r−2ell,a−ell) w_S u^(r−ell)
                                         /prod_(v in V_S)D_v(u).       (1)

This is an equality of formal power series, so coincident diagonal roots
cause no problem. Proof: sum U_n(T)u^n=(I−uT+u^2)^−1. A downward
resolvent path from j to i has monomers (single lowering) or dimers
(double lowering). Its visited diagonal entries are precisely V_S;
there are r−ell transitions. The monomers have r−2ell color choices,
with a−ell of them x. This gives every factor in (1). In particular
all endpoint restrictions and repeated-node Hermite data are retained.

Equivalently, the denominator coefficient is the complete homogeneous
symmetric polynomial in the 2|V_S| numbers
{−q^(2v+1),−q^(−2v−1):v in V_S}. Formula (1) is therefore a closed
finite coefficient formula after Chebyshev/Newton resummation.
It is not asserted to make a sharp asymptotic estimate automatic.

## 2. Full one-outer-face formula

On y=0, ell=0 only. For r<=h−1 and n=h−1−r,

    A_h(j;r,0)=(S_j/S_(j−r))^2 (−1)^n
      sum_(v=0)^n [r+v choose v]_s [r+n−v choose n−v]_s
                       q^[(2j−r+1)(2v−n)].                         (2)

Here [a choose b]_s=S_a/(S_b S_(a−b)), and h<=N implies every
factorial upper index in (2) is <N. If r>h−1, this coefficient is zero.
Proof: factor the denominator in (1) as the two consecutive products
prod_(k=j−r)^j(1+q^(2k+1)u)(1+q^(−2k−1)u), and use the finite
q-binomial generating identity for each reciprocal product. Conversion
from Q-binomial to sine-binomial retains exactly the displayed phase.
Thus the cancellation is an explicit finite Fourier sum, not a sum of
absolute Newton weights. At 2j−r+1=N all phases equal (−1)^n and
cancel its prefactor, giving a positive sum. This special coherence does
not imply positivity of all coefficients or of an arbitrary global source.

## 3. A unique physical path defeats crossing-normalized bounds

For r=h−1, (2) has n=0, hence

    A_h(j;h−1,0)=(S_j/S_(j−h+1))^2.                  (3)

One can prove (3) without any generating function: only the leading
T^(h−1) in U_(h−1) can produce x^(h−1); with y-degree zero every
step is the single-x lowering. There is one physical path and no
remaining alternating cancellation.

The exact absolute coefficient of the normalized crossing kernel on
x^k b^i y^l c^t, i+k+l+t=d, is

    A_N(i,k,l,t)=N/(S_i S_k S_l S_t).

Using S_j S_(d−j)=N, (3) gives the EXACT normalized coefficient

    g_h(j;h−1,0)=S_j S_(h−1)/S_(j−h+1).              (4)

Choose N=4m,h=2m,j=3m−1. Then i=t=m,k=2m−1,l=0 and

    A_h=N^2/S_m^4,
    g_h=N sqrt(N/2)/S_m^2.                           (5)

Indeed S_(2m−1)=sqrt(N/2). With Lambda(t)=−int_0^t log(2sin u)du,

    lim (1/N)log g_h=2Lambda(pi/4)/pi>0.              (6)

This rigorously rules out any polynomial bound on all crossing-normalized
coefficients, even when h<=N/2. Direct normalized-recursion experiments
suggest larger interior growth, but are unnecessary for this conclusion.

The obstruction also holds for the WHOLE WEIGHTED COEFFICIENT NORM.
Take x=1, b=c=1/sqrt(2), y=0. The single monomial (5) has weighted
exponential rate

    4Lambda(pi/4)/pi−(log 2)/4.

The positive crossing magnitude polynomial

    A_N(x,b,c,y)=sum_(i+k+l+t=d) N b^i x^k y^l c^t/(S_i S_k S_l S_t)

has rate, at these weights,

    2Lambda(pi/4)/pi−(log 2)/4.

To verify this sharp comparison, y=0 restricts to l=0. Its strictly
concave ideal-triangle entropy has the unique maximizer
(i/N,k/N,t/N)=(1/4,1/2,1/4), since the three weights are proportional
to the sines of these angles. Uniform sine-product estimates and a
finite Laplace sum give the asserted rate. Hence

    liminf (1/N)log(||H_(N/2)||/A_N)>=2Lambda(pi/4)/pi>0. (7)

Continuity of the crossing entropy on nonzero nonnegative quartets
preserves a strictly positive lower bound in (7) for all sufficiently
small FIXED positive y. The chosen edge monomial is independent of y.
Thus the failure is not restricted to zero face radii.

This rules out a proposed universal local bound by polynomial times the
crossing magnitude. It does NOT rule out a sharper complete-source
bound after shared-face coefficient extraction and radius optimization.
No particular certified plat is required or claimed for the norm test.

## 4. A precise edge-sector rate throughout the color range

If h/N->chi in (0,1), j/N->mu in (chi,1), the coefficient (3) has rate

    2[J(mu)−J(mu−chi)], J(t)=int_0^t log(2sin pi u)du.

At positive x,b,c its weighted monomial rate is this plus
chi log x+(mu−chi)log b+(1−mu)log c. It is strictly concave in mu;
the unique maximum satisfies

    sqrt(b) sin(pi mu)=sqrt(c) sin(pi(mu−chi)).        (8)

Equations (1),(2),(8) provide actual resummed coefficient data for
further shared-face analysis. They do not yet control the other outer
coefficients, signed crossing composition, or global filling periods.

## 5. Verification and source interface

[The focused audit](../experiments/audit_actual_resummed_small_circle_face_kernel.py)
compares the finite resolvent and boundary Fourier formulas with the public
homogeneous Chebyshev helper, including both level parities and all colors
1<=h<=N. These are exact recurrence/formula comparisons, not a new independent
original-matrix audit. The separate
[homogeneous-source audit](../experiments/audit_actual_homogeneous_casimir_face_source.py)
provides the original Casimir/crossing matrices, wrong-unwrapped-total zeros,
cup/cap/mark, and full finite-grid interface. The additional large-level edge
rates in the present audit are diagnostics; equations (5)--(7) prove their
exponential limit independently. The saved
[results](../experiments/actual_resummed_small_circle_face_kernel_results.json)
record these separate scopes.

The resolvent kernel has the stated local-norm and fixed-root scope. It does not give a global source estimate.