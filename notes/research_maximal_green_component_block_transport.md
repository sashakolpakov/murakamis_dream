# Exact cap-tree and lower-block transport at a maximal Green child

31 October 2026. Internally reviewed analytical research theorem. This
preserves the original face targets and every finite LEFT/cap cutoff. It
gives an exact mixed-block reduction, not an absolute bound by Phi_D.
No numerical test or publication claim is used.

## 1. The actual maximal-child component

Use the reviewed classified common-weight datum. Choose a strict LEFT
Green port E with maximal child weight among all Green ports, and call
its child c. RIGHT is handled by the literal row reflection. Let S be
the connected component of actual residual cap edges containing c.

The response/network theorem proves that S is a tree, c has cap
indegree zero, every other vertex has cap indegree one, and every
other noncap port incident to S is CROSS. The chosen Green has no
input in S, since all its supported input weights are strictly
smaller than its child weight. Orient every cap from parent to its
overloaded child. These orientations are therefore precisely the
rooted-tree orientation away from c.

Let P_N((z_v)_(v in S),Y) be the product of ALL the other noncap
coupons incident to S, retaining their genuine CROSS projections.
They may share arbitrarily many face variables. At endpoint -2,
after fixed raw signs, its coefficients are nonnegative. The finite
identities below also hold for arbitrary spectra in these CROSS
coupons: positivity is not used in their derivation. The unchanged
outside source has no incidence to S.

Put N>=3, d=N-1, M=floor(N/2)-1. Each residual cap is held at its
actual stationary spectrum +2 and has exact polynomial

    F_v(z_v,z_parent)=sum_(j=0)^M (-1)^j U_j
                                  z_v^(d-j)z_parent^j,  v!=c,   (1)

in the original cap conventions, or their literal reflections.
Here

    U_j=csc^2(pi/(2N))
           product_(r=1)^j sin^2(pi r/N)/sin^2(pi(r+1/2)/N).

No regularized reference replaces this raw cap. Write the raw chosen
Green LEFT polynomial, removing only its fixed sign (-1)^d, as

    P_(E,LEFT)(c,Y;sigma)=sum_(s=0)^M c^(d-s)G_s(Y;sigma).      (2)

Its genuine strict-child support is s<=M at BOTH parities.

## 2. Original target extraction solves every cap index

Expand the CROSS product in its ORIGINAL component-face variables:

    P_N(z,Y)=sum_(k in Z_+^S) p_k(Y) product_v z_v^(k_v).

For v!=c let S_v be its descendant subtree, including v, and put

    K_v(k)=sum_(w in S_v) k_w,    |k|=sum_(w in S) k_w.

Extract the original demand z_v^d at EVERY vertex of S. At a nonroot
vertex the exponent equality is exactly

    (d-j_v)+sum_(w child of v) j_w+k_v=d.

At the root it is

    (d-s)+sum_(w child of c)j_w+k_c=d.

Starting from the leaves therefore gives, with no relaxed constraint,

    j_v=K_v(k),    s=|k|.                                      (3)

Because k_w>=0 and s<=M, EVERY cap restriction j_v<=M is automatic.
Conversely every k>=0 with |k|<=M gives exactly one set of all cap
indices satisfying the original face targets. Thus, up to the one
retained fixed Green/CROSS raw sign, the exact component contraction is

    B_N(Y;sigma)
      =sum_(|k|<=M) G_|k|(Y;sigma) p_k(Y)
                   product_(v!=c) [(-1)^K_v(k) U_K_v(k)].       (4)

All exterior face degrees remain explicit in G_s and p_k. This is not
a new source on a quotient graph: (3) is the solution of the original
unit demands, before any analytic estimate.

The same count explains the classical quotient. At a stationary flow,
each cap split is the total CROSS supply in its descendant subtree,
and the total CROSS supply in S is 1-q_(E,c)<1/2. In (3) the exact
integer version is s<=M, not a freely chosen residual demand.

## 3. A genuine positive-moment transport, with the total truncation first

The proved cap moment law gives independent positive variables X_v,
one per cap edge, with

    E X_v^j=U_j/U_0, 0<=j<=d.

Define the signed path dilation

    T_c=1,    T_w=product_(edges v on path c to w) (-X_v).

Then

    product_w T_w^(k_w)
          =product_(v!=c)(-X_v)^K_v(k).

Let P_(N,s)(z,Y) denote the part of P_N of TOTAL S-degree s.
Equation (4) is equivalent to the exact finite formula

    B_N(Y;sigma)
      =U_0^(|S|-1) E sum_(s=0)^M
                           G_s(Y;sigma) P_(N,s)(T,Y).          (5)

Equivalently, with one formal root variable z,

    B_N=U_0^(|S|-1) E [z^d]
          P_(E,LEFT)(z,Y;sigma)
          (Pi_(total S degree<=M) P_N)((zT_v)_v,Y).            (6)

The TOTAL-degree truncation in (6) is essential. For every monomial
retained by it, the exponent of each independent X_v is K_v(k)<=M,
so all absolute moments in (5)-(6) are finite. Coefficient extraction
and expectation may be interchanged on this finite truncated space.

One must NOT put the untruncated full P_N inside the expectation
before extracting the coefficient. Its degree in a descendant
subtree may exceed d; the cap law has no such general finite moment.
This is the same exact finite-moment restriction as in the reviewed
shared-star theorem, now applied to a real cap tree.

The formula retains nontrivial quantum information beyond the
classical component-sum quotient. Already the monomials z_c^s and
z_v^s for a leaf v have the SAME total component degree but receive
relative factors 1 and (-1)^(s distance(c,v))
product_(edges on path) U_s/U_0. Therefore replacing all component
faces by one equal variable is not the actual finite cap elimination.
This is a statement about the exact boundary polynomial operator,
not a counterexample to a source estimate on a particular diagram.

## 4. Exact Green lower-block factorization, both parities

The remaining single Green operation in (5) has a concrete finite
spectral reduction. Set theta=pi/N, m=floor(N/2), M=m-1, and

    a_r=2+2cos((2r+1)theta), s_r=2sin(r theta),
    u=-(sigma+2), alpha_r(u)=a_r+u,
    A_-(u)=product_(r=0)^M alpha_r(u).

Let R_j(x,b,y;u) be the ORIGINAL lower cleared cofactor:

    R_0=1,
    R_j=b^j product_(r<j)alpha_r
        +s_j^2(x+y)R_(j-1)
        +s_j s_(j-1)alpha_(j-1)xy R_(j-2),                   (7)

where absent negative indices and the last term at j=1 are zero.
It is homogeneous of FACE degree j. The original prefix/active/suffix
path expansion gives exactly

    G_j(Y;sigma)=R_j(x,b,y;u) product_(r=j+1)^d alpha_r(u).      (8)

No unused row or initial-state sum has been omitted. Reflection
alpha_(d-r)=alpha_r shows

    product_(r=j+1)^d alpha_r(u)
      =zeta_N(u) product_(r=j+1)^M alpha_r(u), j<=M,
    zeta_N(u)=A_-(u)              if N=2m,
              u A_-(u)          if N=2m+1.                    (9)

Define the actual lower-block numerator

    L_M(x,b,c,y;u)
      =sum_(j=0)^M c^(M-j)R_j(x,b,y;u)
                               product_(r=j+1)^M alpha_r(u).

It has FACE degree M and SPECTRAL degree at most M. The exact original
Green source is therefore

    P_(E,LEFT)(c,Y;sigma)
                  =zeta_N(u)c^(d-M)L_M(x,b,c,y;u).             (10)

The raw source has the fixed sign (-1)^d restored afterward.
The odd factor u is the UNUSED central row, not a cancelled zero.
This is the original level-N lower block, not a quantum source at
a different level.

## 5. A positive nodal tail, with the child character retained

The m lower nodes u_a=-a_a, 0<=a<=M, are distinct. At u=u_a,
all terms of L_M with j<a vanish because their retained suffix
contains alpha_a=0. For j>=a, the exact cofactor identity is

    R_j(u_a)=K_(a,j)(u_a) R_a(u_a).

Here K_(a,a)=1, and K is the original interval continuant. The
reviewed coefficientwise nodal theorem proves

    R_a(x,b,y;u_a)>=0,
    K_(a,j)(x,y;u_a)>=0, j<=M.                                (11)

For clarity, positivity of K is nontrivial: normalized by product
s_r^2 it obeys q_r=(x+y)q_(r-1)-gamma_r xy q_(r-2), with
0<=gamma_r<=1. Induction on q_r-xq_(r-1) proves positivity and
q_r<=(x+y)^r. No termwise positivity of the signed dimer weights
has been assumed.

For r>a one has a_a-a_r>0. Put

    T_(a,M)(x,c,y)
      =sum_(j=a)^M c^(M-j) K_(a,j)(x,y;u_a)
                          product_(r=j+1)^M (a_a-a_r).        (12)

This is a nonnegative-coefficient polynomial of FACE degree M-a.
The entire nodal source factors EXACTLY as

    L_M(x,b,c,y;u_a)
                    =R_a(x,b,y;u_a) T_(a,M)(x,-c,y).           (13)

The sign on c in (13) is exactly the sign of the unused lower suffix:
there are M-j negative alpha_r factors. It cannot be deleted.
The first factor is the actual complete-node input cofactor
R_a=S_(2a)D_a(x,b,y), where S_k=product_(r=1)^k s_r and D_a is
the original complete-circle determinant. This exact normalization
is the source adapter in [original complete-node cofactor adapter](actual_cross_cofactor_global_angular_gap.md)
section 1, equations (3)-(4). The second factor is
the explicit positive tail (12); no covariance or different-level
quantum interpretation of it is asserted.

At the two extremes,

    B_M=product_(r=1)^M s_r^2,
    T_(M,M)=1,
    T_(0,M)=B_M s_(M+1)
         sum_(j=0)^M h_j(x,y)c^(M-j)/s_(j+1),
    h_j(x,y)=sum_(r=0)^j x^r y^(j-r).                         (14)

Indeed at a=0 the normalized interval continuant is h_j, and
a_0-a_r=s_(r+1)s_r makes the suffix product telescope. These formulas
are exact finite source identities, not estimates.

## 6. Polynomial-cost interpolation reduces the remaining spectral variable

Let ell_a(u) be the cardinal polynomials on the LOWER m nodes u_a.
Since deg_u L_M<=M, (13) gives the exact identity

    L_M(u)=sum_(a=0)^M ell_a(u)
                         R_a(x,b,y;u_a) T_(a,M)(x,-c,y).       (15)

At even levels the nodes are the shifted Chebyshev roots, with
Lebesgue norm O(log N) on [-4,0]. At odd levels use the full physical
Radau family including the central u=0 node. For any scalar polynomial
p of degree <=M, interpolate u p(u), of degree <=m, on that full grid.
Its value at zero is zero. The full-grid O(log N) bound and division
by the ONE known endpoint factor cost at most a fixed polynomial in N:
for instance |p(u)|<=sup|(u p(u))'| and the elementary degree-m
derivative bound C m^3 sup|u p(u)| give

    sup_[-4,0]|p|
       <=C N^3 log(N+1) max_(0<=a<=M)|p(u_a)|.                (16)

This proof works for complex scalar values. It does not infer an
angular nodal theorem at an unavailable index. A polynomial cost is
all that is claimed.

The original prefactor in (9) has a uniform REAL-spectral bound.
With sigma=2cos phi, the exact Chebyshev products give

    |zeta_N(u)|<=2                         (N even),
    |zeta_N(u)|=|4cos(phi/2)cos(N phi/2)|<=4 (N odd).           (17)

The limiting endpoint values are polynomial continuations; no zero is
divided. In particular the odd unused central factor is included.

For the ISOLATED component S={c}, put

    Q_(a,N)(Y)=R_a(x,b,y;u_a)
                    [c^M] T_(a,M)(x,-c,y) P_N(c,Y).

The original isolated Green-star coefficient is exactly

    B_N(Y;sigma)=zeta_N(u)
                          sum_(a=0)^M ell_a(u) Q_(a,N)(Y),    (18)

and (16)-(17) yield, for all real sigma in [-2,2],

    |B_N(Y;sigma)|<=poly(N) max_a |Q_(a,N)(Y)|.                (19)

The unchanged outside face coefficient can be taken after this identity;
it is linear and all original targets remain. One may also apply the
scalar cosine-Bernstein bound to B_N as a degree-d polynomial in sigma
to extend (19) to a fold strip with the explicit factor
exp(2pi d |Im delta|).

For a nontrivial cap component, replace the s-th root coefficient of
P_N in (18) by the exact averaged coefficient from (5). Equivalently,
apply (18) to the finite polynomial
sum_(s=0)^M E P_(N,s)(T,Y)c^s and retain the outside factor
U_0^(|S|-1). This is legitimate finite linear algebra by the moment
cutoff check in section 3.

## 7. What is resolved, and the exact remaining signed pairing

Equations (3)-(6) are a finite quantum counterpart of the actual cap
quotient, retaining every descendant demand and its character.
Equations (10)-(19) reduce the continuous Green spectrum at polynomial
cost to explicit finite child-character pairings against the actual
CROSS spectator product. No arbitrary matrix, new face target or
coefficientwise comparison of an alternating sum has been introduced.

The lower block has distinct nodes, but this does NOT discard the
original Casimir Jordan data. The original LEFT numerator vanishes
at physical nodes because of zeta_N. Its quotient values L_M(u_a)
retain precisely the information lost by that vanishing factor.
They are not substituted for full-numerator values at those nodes.

What remains is a bound on the signed quantities Q_(a,N), or their
exact cap-tree moment averages, relative to an endpoint/volume
quantity on the SAME original fiber. The factors in (13) have
nonnegative coefficients before c is changed to -c, but taking their
absolute coefficients would remove the cancellation being sought.
Their positive capacity need not equal the original Phi_D.
The a=M term has no tail and lies at the retained half boundary;
the smaller a terms retain the genuine signed tail.

Thus (19) is a concrete finite spectral reduction, NOT an absolute
Phi_D estimate, an instability theorem, or a proof of the prescribed
long-twist volume statement. No globally feasible maximum or
counterexample is manufactured by these identities.

## Exact input provenance and review

Inputs: [actual response network and maximal-child component](research_sharp_source_response_forest_main_network.md) section 5
for the maximal-child component; [original cap positive moment form](research_flat_cap_positive_moment_form.md)
sections 1-3 for the all-level finite moments; the [original homogeneous face source](actual_homogeneous_casimir_face_source.md) and [actual cleared cofactors and nodal interpolation](actual_cross_cofactor_factorization.md) sections 1-2
for (7)-(10), and section 8 equations (22)-(26) for nodal positivity
and interpolation. Original cap/cutoff conventions agree with
[original cap and cutoff conventions](research_cap_cross_all_demand_subexponential_contraction.md).

Internal review: root full analytical/source read, PASS; independent
geometry full analytical/source read of sections 1–7, PASS. The reviews
cover the original subtree demands, finite moment cutoff, both-parity
source factors, nodal child character and polynomial interpolation.
No numerical scan, asymptotic lower claim or external peer-review claim
is involved.
