# The actual degree cycle across the finite-head wall

30 October 2026. Independently reviewed and frozen. The specified generic
exceptional lift can be used on a larger original physical-grid residue
cycle by adding explicitly proved source-null local tori. This is a
statement about PERIODS, not multivariable removability of its poles.
Moving that enlarged cycle still meets genuine channel-row divisors.
Their pole coefficients, their cotangent finite parts, and their first
source-normal densities are calculated below with the actual lattice
step and original complement retained.

The theorem does not deform the whole cycle to the geometric saddle or
prove a nonzero global coefficient. It supplies the exact boundary
currents that such a deformation must retain.

## 1. The original meromorphic source at a chosen matching cut

Use the [specified generic lift](actual_matching_edge_generic_deficient_operator_lift.md),
with N>=3, d=N-1, L=2a, m=d-a, s=d-2a, and

    zeta=q0 exp(epsilon), q0=exp(pi i/N),
    P=pi i/Log zeta, lambda=2 Log zeta.

In the upper ordered physical sector u<=v<=t_target<=d put

    h=v-u, ell=t_target-v, sigma=d-h, r=a-h.

The actual generic continued coefficient, including its actual outside
contraction when desired, has the form

    F(epsilon,h,z)=p_L(epsilon,a-h) E(epsilon,h,z),          (1)

where

    p_L(epsilon,r)=exp(pi i r) zeta^[r(L-r-1)]
                Fhat_P(r) Fhat_P(L-r)/F_L(zeta).

Here E is NOT an assigned amplitude. It is exactly the two specified
large white numerators H_m, their original scalar and high adapter,
the actual physical inverse cups, the face factor if present, and
the unchanged complement and source mark. All are the factors in
the cited lift. Statements at a single channel divisor below are on
charts where these other factors are jointly holomorphic in the index
variables AND epsilon on a common germ. Additional source
divisors must be kept as additional residues, not discarded by (1).

The original scalar source has the product-cotangent realization in
[the exact factorial interpolation](exact_factorial_interpolation_and_complex_contours.md),
section 5, now with the moving-period factorial. Use the ACTUAL free
integral lattice coordinates x after its closure constraints. Its
initial cycle is the sum of small ordered product tori around the
allowed lattice states. The original finite sum, all outside phases,
and exposed mark are retained. No degree is assumed independent merely
because it has been named h.
For n_free lattice variables every period below uses the normalization
(2pi i)^(-n_free); each original product cotangent residue therefore equals
its literal summand.

The opposite ordered sector is left unchanged unless its own literal
adapter is applied. Enlarging only the sector above already preserves
the complete source when it is added to that unchanged remainder.

## 2. Forbidden physical grid tori are source-null at generic q

Consider a physical grid point with h>a, all four ports legal, and all
other source factors regular. Then 0<=sigma=d-h<m. The two large
numerators in (1) have magnetic rows

    i_1=sigma-u=d-v, i_2=ell,
    0<=i_1,i_2<=sigma.

Both H_m(Q^i,Q^(sigma-i)) vanish IDENTICALLY for generic zeta.
Indeed each kth Newton summand contains the factors

    product_(j<k)(Q^i-Q^j)
       *product_(j<m-k)(Q^(sigma-i)-Q^j).

Either k>i or m-k>sigma-i, because m>sigma. This proves the zero
before root specialization. All remaining denominator factors are
regular in the specified generic germ.

Let y=x-x0 be the primitive free lattice coordinates near this grid
point. If h is nonconstant on that lattice chart, its channel pole
has equation l(y)=h-h0, a nonzero integral linear form. Each numerator
is in the maximal ideal (y), so their product is in (y)^2. The channel
cup has at most a simple pole on l=0 in this range. Hence the local
source has the form

    F=A(epsilon,y)/l(y)+B(epsilon,y),
    A in (y)^2, B in (y)^2.                              (2)

Multiplication by a holomorphic original complement preserves this
property. It holds identically in epsilon, including every genuine
normal coefficient.

Choose an index with nonzero coefficient of l, and order the local
torus radii so its term dominates the sum of the others. The torus
then avoids l=0. Expand 1/l by the corresponding convergent geometric
series. Every resulting Laurent monomial in F has TOTAL degree at
least one. Each factor pi cot(pi y_j) is y_j^-1 times a power series
whose nonconstant terms have positive even degree. Thus the coefficient
of product_j y_j^-1 is zero. The original local period is exactly

    (2pi i)^(-n_free) integral_(that ordered torus)
                         F product_j pi cot(pi x_j) dx_j=0.
                                                               (3)

This proof does not assert that F is holomorphic at the crossing of
the divisors. It computes the actual ordered residue. It applies to
every epsilon in the generic germ, so all required q normals of (3)
vanish as well.

Consequently one may add all such forbidden physical-grid tori to
the original supported cycle: their periods are zero term by term.
The resulting finite sum of periods still equals the WHOLE original
source, after the unchanged other sector and every original matching
state are included. This supplies a generic counterpart of the root
entire kernel's enlarged grid, without falsely identifying their
off-grid functions.

If h is constant on a free-lattice chamber and equals a forbidden
value, the original contribution is identically zero. Its meromorphic
lift may not be restricted to that polar chamber by substituting
0/0. Such a chamber is retained as zero; (2),(3) do not manufacture an
independent degree direction or a deformation out of it.

## 3. Exact pole and finite-part coefficients of the original cup

Write h0=a+k, 1<=k<=m, so r=-k. The moving-period recurrence gives

    R_k:=Res_(r=-k) Fhat_P(r)
       =-1/[lambda product_(j=1)^(k-1)(1-zeta^(-2j))].       (4)

To compute its finite part, let g0=partial_z Log Fhat_P(0). Then

    Fhat_P(-k+z)=R_k/z+R_k c_k+O(z),
    c_k=g0-lambda/2
             +lambda sum_(j=1)^(k-1)zeta^(-2j)/(1-zeta^(-2j)).
                                                               (5)

Equations (4),(5) follow by writing
Fhat_P(z)/product_(j=0)^(k-1)(1-zeta^(2(z-j))) and expanding its
single zero factor. No reflection with moving endpoint P-1 is
substituted for the fixed original L.

Put

    M_k=exp(-pi i k) zeta^[-k(L+k-1)],
    B_k=Fhat_P(L+k), B'_k=partial_z Fhat_P(L+k).

The CUP coefficients in the r coordinate are

    A_k=R_k M_k B_k/F_L,
    Bcup_k=R_k M_k/F_L
       *{[c_k+pi i+(Log zeta)(L+2k-1)]B_k-B'_k}.          (6)

Thus p_L(r)=A_k/(r+k)+Bcup_k+O(r+k). Formula (6) keeps B_k
and B'_k separately; it does not divide by the complementary
factorial when that factorial has a root zero.

In h coordinates the FULL actual lift (1) has

    F=A_h/(h-h0)+B_h+O(h-h0),
    A_h=-A_k E(h0),
    B_h=Bcup_k E(h0)-A_k partial_h E(h0).                  (7)

These are explicit original-source densities, including derivatives
of the actual complement. Replacing E by one, or by a selected
local eigenvalue, changes the boundary term.

## 4. Primitive lattice step and the exact contour correction

Fix the other primitive coordinates and write a varying degree as
h=A0 x+B0, with A0 a nonzero integer. The original one-form is

    pi cot(pi x) dx
      =(pi/A0) cot(pi(h-B0)/A0) dh.                       (8)

If x0=(h0-B0)/A0 is an integer, its Laurent residue in h is ONE
and its constant term is zero. The crossed residue of the original
weighted lift is therefore B_h, not A_h. If x0 is not an integer,
the cotangent is regular and the crossed residue is

    (pi/A0) cot(pi x0) A_h.                               (9)

More generally a retained analytic weight with expansion
w=c_(-1)/(h-h0)+c0+... gives c_(-1)B_h+c0 A_h.
This records the Jacobian, possible nonprimitive step, and the
coalescence of the lattice and channel poles.

For two oriented contours bounding a finite annular chain on this
chart, Cauchy's theorem gives the EXACT difference of their source
periods as the sum of (7)--(9), with the actual crossing orientations,
plus the residues of EVERY other crossed source divisor. On a family
of charts the same identity is integrated against all retained
remaining source cycles. Coincident additional divisors require their
actual iterated or multivariate residues; they are not covered by a
single-wall formula. The local ordered tori in section 2 specify the
initial lattice intersections, rather than silently changing their
residue convention.

This is a concrete correction to a proposed degree transport. It
does not assert that any chosen geometric contour is homologous to
the original one, or that a noncompact cap has negligible integral.

## 5. The late-wall first normal is the actual root density

For k>=s+1, n=L+k lies in [N,2N-1]. The complementary finite
factorial has exactly one root zero. From the ORIGINAL integer
product,

    partial_epsilon F_n|0=-2N^2 F_(n-N)(q0).

The root functional equation with a full N-step gives

    partial_z Fhat_N(n)=-2pi i F_(n-N)(q0).

Consequently (6) yields

    A_k(0)=0,
    partial_epsilon A_k|0=P'(0) Bcup_k(0),
    P'(0)=-N^2/(pi i).                                  (10)

On these walls the root cup is regular. If the actual other factors
in (1) are holomorphic, (10) proves the full source identity

    Res_(r=-k) partial_epsilon F|0=P'(0) F(0,-k),
    Res_(h=a+k) partial_epsilon F|0=-P'(0) F(0,a+k).       (11)

This includes the actual outside coefficient, rather than only the
scalar cup. It is a POLE coefficient. At a resonant cotangent wall
the complete boundary period still uses the finite part in (7),(8).

For the early walls 1<=k<=s, sigma=m-k belongs to [a,m-1]. Each
actual large numerator has the root factor
P_s(T)=product_(j=a)^(m-1)(T-Q^j), with T=Q^sigma.
At this fixed channel wall each is O(epsilon). Their product is
O(epsilon^2), whereas the cup pole coefficient is a root unit.
Thus the full lift has ZERO first-normal pole residue there.
This does not say its cotangent finite part vanishes at an arbitrary
off-grid point. At original physical grid points the stronger
generic source-null theorem (3) applies.

Finally the ORIGINAL exposed trace normal is
nu_N=2N(-1)^N/(q0-q0^-1). Hence

    P'(0)/nu_N=(-1)^(N+1) N sin(pi/N)/pi.                 (12)

Its modulus is bounded away from zero and tends to one, at both
parities. Thus an isolated late-wall source-normal residue has an
explicit order-one coefficient times its actual root density
(and the opposite sign in h). This coefficient is not the global
geometric intersection number, the complete cotangent finite part,
or a proof that the surrounding coherent contraction is nonzero.

Focused verification: [actual numerator and boundary audit](../experiments/audit_actual_matching_edge_degree_cycle_boundary.py)
and [saved results](../experiments/actual_matching_edge_degree_cycle_boundary_results.json).
The audit checks the literal large-numerator generic zeros, both wall
ranges, primitive cotangent weights, ordered diagonal-wall residues,
the original moving-period cup Laurent coefficients, and the actual
exposed-normal normalization. Numerical checks of local densities do
not substitute for the ordered-cycle proof in section 2.

Primary-agent full analytical review: PASS. The reader checked the
actual large-numerator support, maximal-ideal total-degree residue
argument, common generic germ, primitive lattice step, cup finite-part
and complement-derivative signs, both wall ranges, and the original
source-normal scalar. Additional divisors, constant-degree chambers,
noncompact caps, and the global geometric intersection remain outside
the conclusion.

Independent source-agent full analytical review and fresh redirected
audit: PASS. The reader independently checked the generic Newton zeros,
the ordered multivariable residue argument, the actual primitive
cotangent weights, cup Laurent coefficients and complement derivative,
both first-normal wall ranges, and the original exposed-trace scalar.
The replay reproduced 2588 generic numerator-zero jets, 95 early and
70 late factor checks, 12 primitive cotangent residues, 18 ordered
ideal checks, 8 moving-Gamma Laurent coefficients, 334 late root/normal
checks, and 13 exposed-normal scalars. No removability, omitted-divisor,
or global contributing-cycle assertion was used in this review.
