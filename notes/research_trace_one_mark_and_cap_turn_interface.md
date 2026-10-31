# Trace-one top marks and the exact protected cap-turn interface

31 October 2026. These exact finite identities delimit two proposed cap simplifications. They neither rewire the diagram nor establish an absolute shared-source or volume bound.

## 1. Any trace-one matrix at the same original top cap

Fix the original complete-colored polynomial-Casimir source and one top
cap, with all full crossings and original turn conventions retained.
Write d=N-1, q=exp(pi i/N), Q=q^2 and x0=q^d. In the balanced basis the
ordinary cap and the original unrestricted marked cap are

    ell_(i,j)=x0^j g_i/N delta_(i+j,d),
    m_(i,j)=x0^j/N^2.

For ANY matrix e, insert D_e=g^(-1)e on the same primal cap input. The
literal contraction, before a support restriction, gives

    m^e_(i,j)=x0^j/N * e_(d-j,i).                       (1)

Every polynomial Casimir coupon and the actual R/R^-1 preserves the
unwrapped total of its two physical heads. The original bottom cups and
other top caps therefore force i+j=d at the exposed top pair. On this
actual whole-source support,

    m^e_(i,j)=N e_(i,i) m_(i,j).                        (2)

Off-diagonal entries do not contribute. In particular e=E_aa gives

    m^a_(i,j)=x0^j/N delta_(i,a)delta_(j,d-a),
    m^a p=1, p_(i,j)=N x0^(-j)delta_(i+j,d).            (3)

The [scalar-open-cap proof](research_arbitrary_casimir_top_mark_transport.md)
shows that the remaining vector is a scalar times this original cup.
Thus its evaluation by (1) is that scalar times Tr(e). Every e with
Tr(e)=1 gives exactly the same full marked scalar, including e=E_aa.
No positivity, idempotence or generic-q normalization is required for e.
This is a statement for the full original source, not transport of e
through a projected local sector.

## 2. Exact face-grid meaning: fixing a clock does not change the targets

The original centered head formula at this top cap is

    q^(d i)=q^(d^2/2)(L_u/L_v)^(d/2).

Its lifted clock equality, equivalently the explicit physical head
assignment, is

    L_v/L_u=q^(d-2i)=x0 Q^(-i).                       (4)

Therefore (3) fixes L_v/L_u=t_a=x0 Q^(-a). At odd N this is an ordinary
Q-grid point; at even N it is on the original odd gap-parity coset.
No half-power lift or head offset is changed.

Let P=prod_e H_(f_e) be the original homogeneous numerator, of total
degree dR. Fix L_u=1. The original marked source is the normalized
N^(R+1)-point average of

    P(1,L_v,L_ordinary)/prod_ordinary L_f^d.

Equation (2) multiplies by N and restricts the one v-grid coordinate to
t_a. Thus the E_aa-marked source is EXACTLY

    N^(-R) sum_(original ordinary grid)
             P(1,t_a,L_ordinary)/prod_ordinary L_f^d. (5)

All exponents of P are nonnegative. Each ordinary grid average requires
an exponent congruent to d modulo N, whose least nonnegative value is d.
There are R ordinary faces and total degree dR. Consequently EVERY
ordinary exponent equals d and both u,v exponents equal zero. The
remaining even-grid phases are one, because each exponent equals its
target. It follows that (5) is

    [prod_ordinary L_f^d] P |_(L_u=L_v=0),             (6)

independently of a or the nonzero value t_a. More generally (2) gives
Tr(e) times (6). All N factors have been accounted for: the factor N in
(2) cancels the removed v average, and no extra mark scalar remains.

In particular the alternate E_00 mark does NOT replace the protected-zero
coefficient by a positive ordinary-radius coefficient or eliminate its
cap corners. A physical marked head index a fixes a face clock; it is
not the polynomial row-degree index j of a cap coefficient. Identifying
these indices would require another actual source transform.

## 3. The cap comparison polynomial is an actual crossing corner modulus

Now specialize the ordered local quartet to x=b=0. Put theta=pi/N.
At sigma=+2 the literal full numerator has

    H_V(0,0,c,y)=sum_(j=0)^d (-1)^j A_j c^(d-j)y^j,
    A_j=csc^2(theta/2)
           prod_(r=1)^j sin^2(r theta)/sin^2((r+1/2)theta). (7)

This follows from the exact full-interval expansion and the shifted
sine product prod_(r=0)^d 4sin^2((r+1/2)theta)=4. It includes both
parities and the omitted half. The ratios A_j/A_(j-1) are less than
one up to the unique middle crossing of sin(j theta)=sin((j+1/2)theta),
then greater than one. Hence the maximum occurs at an endpoint.
A_0=csc^2(theta/2)<=N^2 by the elementary sine chord bound, and the
ordinary sine product gives A_d=N^2. Thus 0<A_j<=N^2 for every j.
Any original LEFT window is a subpolynomial of this coefficient modulus.

The published exact normalized crossing coefficient on b^i x^k y^l c^t,
i+k+l+t=d, is

    (-1)^(k+l+1) q^[kl-(i+1)(t+1)] N/(S_i S_k S_l S_t),
    S_a=prod_(r=1)^a 2sin(pi r/N).

Set i=k=0,l=j,t=d-j and use S_j S_(d-j)=N. This gives

    H_(r_N)(0,0,c,y)=sum_(j=0)^d (-q)^j c^(d-j)y^j,
    H_(r_N^-1)(0,0,c,y)=sum_(j=0)^d (-q^-1)^j c^(d-j)y^j. (8)

The inverse formula includes the confluent data, not just conjugate
nodal eigenvalues. The actual face operator T has real monomial
coefficients at this root: each displayed q/Q combination is invariant
under q -> q^(-1). The [frozen signed-kernel theorem](actual_signed_small_circle_face_kernel.md),
section 1 and (6a), expresses r_N=sum_r(-q)^r Bhat_r and its ACTUAL Hermite inverse as
sum_r(-q^(-1))^r Bhat_r, where Bhat_r has real spectral nodes and real
sine-product normalization. Hence the inverse face kernel is coefficientwise
complex conjugate in this real polynomial basis, including every repeated
node derivative. This justifies using q^(-1) in (8).

The ACTUAL crossing R^epsilon has the additional original scalar
lambda0^epsilon, lambda0=q^(d^2/2), of unit modulus. Therefore

    |H_V(0,0,c,y)|_coeff <= N^2 H1(c,y),
    H1(c,y)=sum_(j=0)^d c^(d-j)y^j
           =|H_(R^epsilon)(0,0,c,y)|_coeff, epsilon=+/-1. (9)

Here coefficient modulus is taken before evaluating positive c,y. The
last equality retains the unit scalar's modulus; it does not delete its
phase in a signed contraction. Crucially, the identity coupon on the
original quartet instead has

    H_(identity)(0,0,c,y)=c^d,

because its two middle variables are b,c. Thus (9) is not the standard
identity-insertion polynomial on the original middle pair.

## 4. The exact boundary contraction, and what it does not identify

Let P(c,y;Z) be any complementary polynomial in these two ordinary
faces and all remaining variables Z. Then, with coefficient operators
in Z retained unchanged,

    [c^d y^d] H1(c,y) P(c,y;Z)=[t^d] P(t,t;Z).        (10)

For epsilon=+/-1 let zeta=-q^epsilon. Equation (8) gives instead the
SIGNED actual half-crossing corner identity

    [c^d y^d] H_(R^epsilon)(0,0,c,y) P(c,y;Z)
         =lambda0^epsilon [t^d]P(zeta t,t;Z).         (11)

So the actual turn carries a nontrivial shared-face phase, not the
positive merge in (10). On the only relevant c-degree truncation, define D_A by
D_A(c^j y^h)=A_j c^j y^h for 0<=j<=d. The raw cap identity is

    [c^d y^d] H_V(0,0,c,y)P(c,y;Z)
                         =[t^d](D_A P)(-t,t;Z).      (12)

The coefficient bound gives a positive merged-polynomial upper bound
via N^2[t^d]|P|(t,t;Z). It does not turn (12) into (11), nor show that
the signed complementary contraction has the same bound or rate as a
geometrically smoothed source.

The merged pair c,y is an OUTPUT MAIN edge. Its two incident white
triangles belong to two different original matching coupons. Removing
the two triangles of the cap coupon is therefore not the same
combinatorial operation as contracting that MAIN edge. A physical
rewiring would have to retain the neighbor coupon, its boundary typing,
and the phase/degree operator in (11)--(12). No such two-port turn or
volume comparison is proved here.

## 5. Dependencies

The exact inputs are the [homogeneous source](actual_homogeneous_casimir_face_source.md),
sections 1–4 and (10); the [signed kernel](actual_signed_small_circle_face_kernel.md),
section 1 and (6a); the [original marked cap](quantum_bridge_cap_source.md),
(2.1)–(2.4); and the [top-mark transport theorem](research_arbitrary_casimir_top_mark_transport.md).
The [finite-collar obstruction](research_double_protected_cap_finite_collar_obstruction.md)
remains unchanged.

The existing
[mark audit](../experiments/research_audit_arbitrary_casimir_top_mark_transport.py)
already verifies the scalar-cup identity entrywise and hence all E_aa
evaluations in its fixtures. No new finite replay, physical rewiring,
absolute shared-source estimate or volume assertion is claimed here.