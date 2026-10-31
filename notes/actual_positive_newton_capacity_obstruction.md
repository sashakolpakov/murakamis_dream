# The positive Newton capacity can exceed the complete rate

30 October 2026. This concerns the proposed
absolute Newton majorant, not the original alternating low-color source.
The exact local kernel and one-port source interface below apply to the
proved flat-plat compiler. The obstruction family is an actual certified
matched graph with specified positive determinant polynomials; its full
original-source identification is CONDITIONAL on a compiler adapter
described in section3. All remaining half-twist signs are explicitly ZERO,
so these polynomial Newton coefficients are nonnegative and maximal-label
restriction is a lower bound. No signed-source conclusion is made.

## 0. The exact original Newton coefficient

Put q=exp(pi i/N), d=N-1, s_j=2sin(pi j/N), S_j=product_(k=1)^j s_k,
and B_r(z)=product_(k=0)^(r-1)(q^(2k+1)+q^(-2k-1)-z),
Bhat_r=B_r/S_r^2. For the original untwisted face operator T of
[the exact one-port correspondence](actual_small_circle_polynomial_face_insertion.md),
including its q^(dp) character, the finite identity is

    Bhat_r(-T)c^m = sum_(0<=i,j<=r; i+j<=m)
       [m r]_s [m+r-i-j r]_s [r i]_s [r j]_s
                        x^i y^j c^(m-i-j),          (0)

for 0<=m,r<N. Here [n r]_s=product_(k=1)^r s_(n-r+k)/s_k;
it is zero for n<r. Terms with second upper index>=N have the exact
numerator zero s_N. There is no vanishing denominator. Thus every
coefficient is nonnegative. Moreover T and Bhat_r(-T) commute with
multiplication by c^N; the higher block is preserved, not wrapped.
A proof is given in the appendix.

Let P_rem be the original product of the remaining positive circle
polynomials before merging b,c. The actual positive one-port coefficient
is Z_r=[L^(d F_sm)] [Bhat_r(-T)P_rem]_(c=b,u=v=0)>=0. Its source
scalar is N^(R-1) product_remaining(k_a beta_a^2), since every remaining
epsilon is0. The source theorem retains its ordinary caps, mark,
physical support and finite-grid measure. Input terms divisible by c^N
cannot reach the ordinary merged target d<N.
This one-port original-source identity assumes connected identity
smoothing and distinct unmarked middle faces, exactly as in its linked
source theorem. It does not extend the graph family through an absent
flat-plat adapter.

For 1<=h<=floor(N/2), the exact original Chebyshev--Newton identity is

    T_h=sum_(r=0)^(h-1) (-1)^(h-1+r) b_(h,r) Bhat_r(-T),
    b_(h,r)=S_r^2 S_(h+r)/[S_(2r+1)S_(h-r-1)]>0,
    b_(h,r)<=N/2.

The last uniform bound follows from the actual sine product: its
log-concavity in h puts the maximum at h=N/2; double-angle cancellation
gives 2 product_(k=1)^r s_(2k)/product_(k=0)^r s_(2k+1). Its successive
ratio changes once from <=1 to >=1, so the two endpoints suffice.
They are csc(pi/N) and either N/2 or csc(pi/N), all <=N/2. This is
also proved in [the pure-leaf calculation](actual_pure_conway_auxiliary_color_leaf.md).
The majorant studied here is the TRUE sum sum_r b_(h,r)Z_r, retaining
these magnitudes rather than replacing all of them by N/2.

## 1. The complete shared-face angle problem

Use one actual untwisted port with distinct unmarked middle faces b,c
and distinct unmarked outer faces x,y. Its two removed triangles are
(x,b,y),(x,c,y). Retain ALL other original triangle incidences and the
original marked faces u,v. Let R be the number of original circles.
For every remaining triangle t and incident face f introduce a_tf>=0,
with sum_f a_tf=1/2. Its center angle is theta_tf=2pi a_tf. Corners at
u,v are fixed zero. The exact fold local entropy is

    S_t(a_t)=V(2pi a_t)/(2pi),
    V(theta)=2 sum_j[Lambda(theta_j/2)+Lambda((pi-theta_j)/2)].

These are the source-normalized triangle entropies; no local constant
or exterior phase is reset. Put rho=r/N, mu=m/N, xi=i/N, eta=j/N for
the exact positive Newton coefficient (0).
Its limiting domain is

    0<=rho<=1/2, rho<=mu<=1,
    0<=xi,eta<=rho, xi+eta<=mu,
    mu+rho-xi-eta<=1.                               (1)

The true physical cap is rho<h/N; it approaches1/2 when h=floor(N/2).
The actual root-zero wall at the last boundary is interpreted by
approach from its nonzero side, not as replacing a vanished coefficient.
Let K(mu,rho,xi,eta) be

    J(mu)+J(mu+rho-xi-eta)-J(mu-rho)-J(mu-xi-eta)
      -J(xi)-J(rho-xi)-J(eta)-J(rho-eta),           (2)

where J(t)=integral_0^t log(2sin(pi z))dz. This is the sum of four
ideal-tetrahedron volumes/pi, with normalized angle triples

    (rho,mu-rho,1-mu),
    (rho,mu-xi-eta,1-mu-rho+xi+eta),
    (xi,rho-xi,1-rho), (eta,rho-eta,1-rho).

The FULL shared-face constraints are

    sum_(t incident f) a_tf =1                 for f outside{x,y,b,c,u,v},
    sum_t a_tx=1-xi,       sum_t a_ty=1-eta,
    sum_t a_tb=1-mu+xi+eta,
    sum_t a_tc=mu.                                  (3)

They follow directly from the exact finite monomial:
c^m -> x^i y^j c^(m-i-j), followed by c=b and target exponent d.
The input b exponent is d-m+i+j. Thus these are not factorwise
maxima or independently chosen local degrees. Their sum is R-1,
exactly the total remaining triangle degree. Define

    C_Newt=max_(1),(3) [sum_remaining S_t+K].        (4)

The polytope is compact and the objective continuous and concave.
It is the natural shared capacity for the positive one-port Newton
coefficient with every other channel at maximal fold. The ordinary
source polynomial and its normalized Newton kernel are nonnegative.
The source measure N^(R-1), k factors and odd maximal-fold beta=1
are subexponential; no exponential normalization is omitted.

## 2. Euler--Lagrange equations and the lost phase

At a strict constrained maximum let l_f>0 be the shared face multipliers.
Use the Lagrangian sum S_t+K+sum_f log(l_f)(sum_t a_tf-demand_f).
The triangle equations are exactly the original source circle-angle
equations, tan(theta_tf/2) proportional to l_f. Write s(t)=sin(pi t).
The remaining interior equations are

    s(mu)s(mu+rho-xi-eta) /
       [s(mu-rho)s(mu-xi-eta)] = l_c/l_b,

    s(mu-xi-eta)s(rho-xi) /
       [s(mu+rho-xi-eta)s(xi)] = l_b/l_x,

    s(mu-xi-eta)s(rho-eta) /
       [s(mu+rho-xi-eta)s(eta)] = l_b/l_y,

    s(mu+rho-xi-eta)s(mu-rho) /
       [s(rho-xi)s(rho-eta)] =1.                    (5)

At an active rho boundary the last equality is replaced by its KKT
inequality. These equations do not retain the original factor
(-1)^(h-1+r) in the low-color Newton sum. In the actual complex
stationarity equation that factor contributes the linear character
pi i rho (with its fixed lattice mark); its exponential rho equation
would have the opposite sign. Dropping it is therefore a change of
critical scheme, not a harmless choice of a logarithm.

## 3. A certified two-sided Apollonian matched-graph family

Start from the actual octahedral-white source used in the frozen
smoothing-fixed-radius note: white faces0,1,2,3 form the equator,
4,5 are the two poles, matching edges are01,12,34,35, and marked
MAIN23 is unchanged. In the marked chart, faces2,3 are the parallel
lines y=0,2; circles0,1 have curvatures2 and centers(0,1/2),(0,3/2),
and circles4,5 have curvature1 and centers(-sqrt2,1),(sqrt2,1).

Make n literal Apollonian insertions into triangle(0,1,4), and n
into triangle(0,1,5), each successive insertion inside the triangle
adjacent to the retained matched edge01. On each side the new matching
edge is the previous-middle/new-middle edge, exactly as in the frozen
one-sided construction. Both constructions have disjoint interiors.
The old matching01 remains; marked MAIN23 is untouched. The explicit
small disks have curvatures

    B_n=4n^2+4sqrt2 n+1

and centers (+/- (2n+sqrt2)/B_n,1). The already proved tangent-disk
and supporting-halfspace induction applies separately on the two
sides. Thus this is an actual connected certified augmented matched graph,
not an arbitrary angle graph. Identity smoothing at01 merges its
two opposite final middle faces b_n,c_n; its two chains keep the
smoothed projection connected and the marked faces distinct.

There is an essential presentation qualification. The embedded dual
and chosen matching give a literal general Morse augmented diagram,
with its original cyclic ports. The currently proved marked coefficient
compiler, however, assumes a fixed FLAT PLAT with k bottom cups, k top
caps and its specified gap sweep. No adapter has yet been proved that
carries the successive local subdivisions into that compiler while
preserving this positive coefficient formula. Nor is a common bridge
width over all n asserted. Choosing a fixed depth gives a finite graph,
but a general link-to-plat isotopy by itself is not the missing adapter.
Consequently the unconditional obstruction below concerns its specified
positive determinant polynomial and capacity. Its conclusion for the
original flat-plat quantum source requires that actual adapter; the
exact one-port kernel formula alone does not supply it.

The two original triangles at01 now have the SAME curvatures

    (l_x,l_b,l_y)=(2,B_n,2),
    (l_x,l_c,l_y)=(2,B_n,2).

Put

    a_n=(2/pi)atan(1/sqrt(B_n+1)).

Their normalized angles (theta_x,theta_b,theta_y)/pi are
(a_n,1-2a_n,a_n), and a_n->0. KEEP EVERY remaining original packing
angle exactly as it was. Its demands in (3) are met by

    rho=1/4, mu=1/2+a_n, xi=eta=a_n.                (6)

For sufficiently large fixed n these lie strictly in (1), and the
four kernel tetrahedron triples are

    (1/4,1/4+a_n,1/2-a_n),
    (1/4,1/2-a_n,1/4+a_n),
    (a_n,1/4-a_n,3/4), (a_n,1/4-a_n,3/4).

Let F0=Vol(Y_n)/(2pi) be the geometric complete capacity of this
certified matched graph. Its identification with the original flat-plat
complete rate requires the stated compiler adapter. The value of
the FULL shared objective at this feasible state exceeds F0 by

    E(a_n)=K(1/2+a_n,1/4,a_n,a_n)
                   -V(pi a_n,pi(1-2a_n),pi a_n)/pi. (7)

The subtraction is the TWO deleted source triangle entropies, each
V/(2pi), not one. By continuity of the actual Lobachevsky functions,

    E(a_n) -> 2 Catalan/pi = v_oct/(2pi)>0.          (8)

Indeed the last two kernel tetrahedra flatten, the first two tend
to the right ideal tetrahedron with angles(pi/4,pi/4,pi/2), of volume
Catalan, while the old two source triangle entropies tend to0.
Hence for every sufficiently large FIXED n,

    C_Newt >= F0+E(a_n)>F0.                        (9)

This refutes the proposed universal strict comparison even AFTER
allowing all shared radii/angles to readjust: (6) is already a feasible
full angle state. It does not refute the original volume conjecture.

## 4. A lower bound for the specified positive coefficient

The following lower-bound step uses only the supplied positive
determinant saddle estimates. At odd N, M=d/2, each normalized
remaining white polynomial D_M has degree M and nonnegative coefficients.
For a fixed strict source-angle triple, its prescribed coefficient
with exponents M theta_j/pi+O(1) has exponential rate V(theta)/(2pi).
This follows from the SAME PSD contraction proof as the frozen
face-coefficient saddle, applied to that single two/three-variable
pencil and its prescribed interior logarithmic-gradient target:
pair traces give the global torus gap, the Hessian is cN on its
homogeneity quotient, and the finite saddle moves o(1). One-variable
forced faces are literal monomials. Fixed zero marked corners are
deleted before this argument; all other corners in this fixed
certified packing are strictly positive.

There are compatible integer exponents with all these triple
fractions and all original ordinary face targets. Scale the remaining
packing flows by d rather than N: every row then has the integer
sum M=d/2, and all face columns outside x,y,b,c already have target d.
Round within the bipartite row/face incidence network, allowing the
four displayed face columns to vary by O(1). Impose the integer floor
and ceiling of each given entry as lower and upper bounds. The row
equations and fixed face-column equations form a totally unimodular
network matrix. Its bounded feasible polytope has an integral vertex,
preserving every fixed integer margin and changing each entry by at
most1. Marked zeros stay zero. Strict positive entries stay positive
for large N.

The resulting actual remaining input monomial has c exponent
m=d(1/2+a_n)+O(1)<N, and its deficits determine i=d a_n+O(1),
j=d a_n+O(1), with the merged b target exactly d. Choose r=N/4+O(1)
integer. Every finite kernel sine product is then in its strict
nonzero domain. The exact Newton coefficient formula and the
uniform sine-product estimates show that this ONE product of
positive coefficients contributes rate F0+E(a_n). Thus for the
specified positive Newton polynomial coefficient at maximal remaining labels,

    liminf_(N odd) N^-1 log Z_(r_N) >= F0+E(a_n).   (10)

The specified original-compiler scalar, if its adapter is established,
is polynomial and does not change this inequality.
For h_N=floor(N/2), r_N=N/4+O(1), the exact coefficient b_(h_N,r_N)
has exponential rate zero directly from the exact finite sine products:

    lim N^-1 log b_(h_N,r_N)
      =2J(1/4)+J(3/4)-J(1/2)-J(1/4)=0,

using J(3/4)=-J(1/4), J(1/2)=0 and the uniform O(log N) factorial
errors. No off-grid color interpolation is needed for this step.
Consequently the TRUE absolute Newton expansion

    sum_(r<h_N) b_(h_N,r) Z_r

also has lower rate at least F0+E(a_n). This is not an artifact of
replacing b by its upper bound N/2.

To obtain a volume-rate upper bound for the alternating polynomial,
one would therefore need exponential cancellation in the retained signs
(-1)^(h_N-1+r), possibly together with remaining source sums. No such
upper bound or cancellation theorem has been proved here. The
positive-polynomial majorant cannot supply a capacity comparison on
all certified matched graphs. Without the presentation adapter this
is not a claimed flat-plat source counterexample.

Finally, (9) prevents an interpretation of the maximizing positive
capacity as Vol(rho)/(2pi) for a representation of the SAME original
group with the actual source normalization. Such an interpretation
would contradict the independently proved universal representation-
volume bound. The missing Newton phase in (5) identifies a concrete
reason that the positive critical scheme is not the original one.

## Appendix: proof of the finite positive Newton identity

One may first work at generic q, writing s_j=(q^j-q^-j)/i and
c_j=q^(2j+1)+q^(-2j-1). The original operator acts by

    T c^m=-c_m c^m+s_m^2(x+y)c^(m-1)
                           +s_m s_(m-1)xy c^(m-2). (A1)

The literal coefficients at the bottom two rows are zero, so there
are no negative powers. Define

    D(c^m)=s_m c^(m-1),
    R_j(c^k)=s_(k+2j+2)c^(k+1)
             +s_(k+j+1)(x+y)c^k+s_k xy c^(k-1).

Direct computation gives

    R_0 D=T+c_0,
    D R_j=R_(j+1)D+s_1 s_(2j+2)I,
    sum_(j=0)^(r-1) s_1 s_(2j+2)=c_0-c_r.

It follows inductively that

    B_r(-T)=R_0 R_1...R_(r-1)D^r.                   (A4)

This already proves the exact zero for r>m. For r<=m, the coefficient
of x^i y^j c^(m-i-j) asserted by (0), after multiplication by S_r^2,
is

    C_r(m;i,j)=
     S_m S_(m+r-i-j) S_r^2 /
     [S_(m-r)S_(m-i-j)S_i S_(r-i)S_j S_(r-j)].       (A5)

The recurrence B_(r+1)(-T)=(T+c_r)B_r(-T), using (A1), proves (A5).
For completeness, set k=m-i-j. After dividing on the generic open
set and clearing the factors, the only identity needed is

 s_(k-r)s_(r+1-i)s_(r+1-j)
 +s_(k+1)[s_i s_(r+1-j)+s_j s_(r+1-i)]
 +s_(k+r+2)s_i s_j
       =s_(k+i+j-r)s_(r+1)^2.                     (A6)

This follows by substituting s_a=(q^a-q^-a)/i. The zero-index boundary
terms of the recurrence are recovered after clearing denominators,
or directly from (A4). Thus the generic polynomial identity holds.
Specialize it through the finite products in (0): all denominators
S_r,S_i,S_j,S_(r-i),S_(r-j) are nonzero for r<N. If m+r-i-j<N,
all surviving sine factors are positive; otherwise its interval
of r consecutive numerator factors contains s_N, since
m-i-j<N. This proves the claimed root positivity.

At the top endpoint r=d, only m=d and i+j=d survive, and every
binomial [d choose i]_s equals1. Hence a useful exact endpoint is

    Bhat_d(-T)c^d=sum_(i=0)^d x^i y^(d-i),
    Bhat_d(-T)c^m=0 for m<d.                       (A7)

## Validation and remaining source interface

The [focused audit](../experiments/audit_actual_positive_newton_capacity_obstruction.py)
and [saved results](../experiments/actual_positive_newton_capacity_obstruction_results.json)
check the exact local identity against the original coproduct Casimir:
2,436 monomial paths, including812 high totals and756 preserved whole-N
blocks, 55,562 low-color matrix entries and15,316 complete-color entries.
Two cleared symbolic identities and1,286 exact numerator-zero cases
check the finite formula; finite-field arithmetic verifies equality,
while nonnegativity is supplied by the sine-product proof.

Four explicit two-sided matched graphs check76 matching incidences,
1,416 white and2,376 shaded support inequalities,228 right angles and
62 shared-face equations. Six integral-flow roundings check132 integer
row margins,60 fixed face columns and all strict Newton domains. Eighteen
literal determinant coefficients include three-, two- and one-variable
cases. The finite coefficient/entropy profiles are diagnostics; the
limit and positive gap follow from the written analytic arguments.
The audit does not label the graph family as a flat-plat source fixture.

The two-sided supporting-halfspace, matching, mark and load calculations do not supply the missing flat-plat compiler adapter.

The classical capacity identity is geometric. Its use for the source remains conditional on the stated source interface.

