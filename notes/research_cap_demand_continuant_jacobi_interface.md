# Actual continuant recurrences and an explicit positive cap tensor metric

31 October 2026. **Internally reviewed, unpublished analytical continuation**
of the [original-demand convolution](research_two_port_main_cap_original_demand_convolution.md).
All statements below retain its even-level restriction and original
summation cutoff. The polynomial comparison (8) in that note remains
open. This note derives recurrences and a positive Jacobi metric; it does
not identify that metric with the separately derived cap-moment metric.

## 1. Normalization of the actual continuant

Use the notation of the source note: N=2m, d=N-1, M=m-1,
theta=pi/N, q=exp(i theta), Q=q^2,

    s_r=2 sin(r theta),
    a_r=2+2 cos((2r+1)theta),
    K_0=1, K_1=s_1^2(A+Z),
    K_r=s_r^2(A+Z)K_(r-1)
          +s_r s_(r-1) a_(r-1) AZ K_(r-2).

Write S_r=product_(a=1)^r s_a and L_r=K_r/S_r. Direct division gives

    L_r=s_r(A+Z)L_(r-1)+a_(r-1)AZ L_(r-2).       (1)

There is no small-eigenvalue inverse in (1). With the exact scalar
normalization

    L_r=i^r q^(-r(r+1)/2) R_r,

the recurrence is

    R_0=1,
    R_1=(1-Q)(A+Z),
    R_r=(1-Q^r)(A+Z) R_(r-1)
          -(1+q Q^(r-1))^2 AZ R_(r-2).           (2)

Indeed s_r=i q^(-r)(1-Q^r), and
a_(r-1)=q^(-(2r-1))(1+q^(2r-1))^2. These two identities prove every
factor and sign in (2), including r=2. All denominators (Q;Q)_r are
nonzero for r<=d. Dividing by this product recovers the positive
normalized source recurrence with dimer coefficient

    beta_r=a_(r-1)/(s_r s_(r-1))
           =cos^2((r-1/2)theta)
              /[sin(r theta) sin((r-1)theta)] > 0,
    2<=r<=d.                                     (3)

The strict positivity here uses EVEN N: the half-integer angle never
equals pi/2. No odd-level Jacobi assertion is made.

## 2. An actual positive Jacobi metric and its CD identity

Let p_0(z)=1, p_1(z)=z and

    p_r(z)=z p_(r-1)(z)-beta_r p_(r-2)(z).         (4)

For t>0, exact substitution in the source recurrence gives

    K_r(-t,1)=S_r^2 t^(r/2)
                 p_r((1-t)/sqrt(t)).              (5)

This is a polynomial identity after canceling the powers of sqrt(t),
so its endpoint values are obtained without a new limiting assumption.

Take the d-by-d real symmetric Jacobi matrix J with zero diagonal and
off-diagonal entries sqrt(beta_2),...,sqrt(beta_d). Its spectral measure
at the first coordinate is a positive probability measure nu_N. The
off-diagonal entries are nonzero, so its d eigenvalues are distinct and
each has positive first-coordinate mass. Recurrence (4), or direct
induction on the coordinate vectors p_r(J)e_1, gives

    integral p_r(z)p_s(z) dnu_N(z)
       =delta_(r,s) h_r,   0<=r,s<=d-1,
    h_0=1, h_r=product_(a=2)^(r+1) beta_a.         (6)

The indexing in (6) matters: p_r has norm beta_2 ... beta_(r+1),
not beta_2 ... beta_r. For example p_1=z has norm beta_2.
The polynomial p_d is the characteristic polynomial and vanishes on
the support; no positive norm for degree d is asserted.

For 0<=r<=d-2 the exact Christoffel-Darboux identity is

    sum_(a=0)^r p_a(z)p_a(w)/h_a
       =[p_(r+1)(z)p_r(w)-p_r(z)p_(r+1)(w)]
          /[h_r(z-w)].                            (7)

The same formula holds for r=d-1 with the right side divided by
h_(d-1); it is a polynomial identity, obtained by telescoping the
recurrences, with p_d retained as the endpoint polynomial. Diagonal
z=w is interpreted by differentiation. In particular the right side
at w=z is nonnegative on the real line.

This is an exact positive orthogonality statement for the actual
continuant after its negative-outer substitution. It does not follow
from a conjectured quantum-group unitarity or an imported q-Hahn
identification.

## 3. The coefficient recurrence keeps an undetermined endpoint

Extend the notation C_(j,h) from the source note temporarily to
0<=h<=d by its literal formula

    C_(j,h)=[A^j Z^(d-h-j)]K_(d-h)
                 product_(r=d-h+1)^d a_r.

It is zero outside 0<=j<=d-h. For 0<=n<=d define
f_n(j)=C_(j,n-j) for 0<=j<=n. Reflection of the original recurrence,
using a_(d-h)=a_h and s_(d-h)=s_(h+1), gives, for h=n-j,

    a_h f_n(j)
       =s_(h+1)^2 f_n(j-1)
         +s_(h+1)^2 f_(n+1)(j)
         +s_(h+1)s_(h+2) f_(n+1)(j-1),            (8)

for 0<=n<=d-1 and 0<=j<=n, with missing negative-index terms zero.
To check the last term, its source unused product contains both
a_(d-h) and a_(d-h-1); the latter cancels the actual dimer factor.
This leaves precisely the product of the two displayed s factors.

Equation (8) supplies n+1 relations for the n+2 coefficients of
f_(n+1). Its new top coefficient f_(n+1)(n+1)=C_(n+1,0) is not
determined by these equations. Formally extending the recurrence to
j=n+1 gives s_0=0 and only 0=0. This coefficient is fixed instead by
the original K_d. Omitting it would delete a genuine source boundary.

## 4. Why these identities do not yet settle the original sum

The original signed coefficient is

    (-1)^d sum_(j=max(0,n-M))^(min(M,n))
                   (-1)^j U_j C_(j,n-j).          (9)

The independently reviewed [positive cap moment construction](research_flat_cap_positive_moment_form.md) gives
U_j/U_0=E X_N^j for every 0<=j<=d, with X_N>0, non-atomic and
unbounded. Thus (9) is exactly (-1)^d U_0 E F_(N,n)(-X_N), with
F_(N,n)(t)=sum_(j in J_n) C_(j,n-j)t^j. Moments through
2M=d-1 supply a positive Gram form on this original cutoff space.

That cap-moment form and (6) are different constructions. No equality
of their measures, and no isometry between their polynomial spaces,
has been derived. In particular, CROSS restricts the tail degree
r=d-h to m<=r<=d, whereas RIGHT restricts the A-coefficient index
j<=M. The latter is not the Jacobi row index. Formula (7) does not
by itself turn the projected sum (9) into an orthogonal projection.

At n<=M, J_n is the full interval 0..n. At n>M, both endpoints
n-M and M must remain. A complete-polynomial summation identity at
the same n would need explicit correction terms at BOTH boundaries
before it could estimate (9).

The exact missing estimate remains a polynomial comparison of (9)
with sum_(j in J_n) V_j C_(j,n-j), uniformly in N and n. Positive
moments, positive Jacobi orthogonality, and the scalar recurrence
separately do not establish that comparison. The actual typed
unprojected two-port patch uses overlapping pair Casimirs on three
heads, rather than two functions of one Casimir; its RIGHT/CROSS
projections must also be retained in any future Racah identity.

No numerical growth test or general source bound is part of this continuation.

## 5. A finite operator identity and the exact cutoff commutator

This appendix uses the full coefficient slice only as an algebraic
auxiliary. Define, for 0<=n<=d,

    H_n(t)=sum_(j=0)^n (-1)^j C_(j,n-j)t^j,
    D=t partial_t,
    A_n(D)=a_(n-D),
    B_n(D)=s_(n+1-D)^2,
    E_n(D)=s_(n+1-D)s_(n+2-D).

All functions of D are finite diagonal operators on monomials. Thus
s_(n-D) on t^j means the real number 2 sin((n-j)theta), including
negative indices. Equation (8), with its sign (-1)^j, is equivalent to

    [A_n(D)+t B_(n-1)(D)] H_n
       =[B_n(D)-t E_(n-1)(D)] H_(n+1),
    0<=n<=d-1.                                    (10)

The operator order is literal: t B(D) first applies B(D), then
multiplies by t. This avoids an implicit D-versus-t commutation error.
The nominal highest coefficients on both sides vanish: B_(n-1)(n)=0,
B_n(n+1)=0, and E_(n-1)(n)=E_(n-1)(n+1)=0. Thus (10) retains, rather
than determines or deletes, the top coefficient discussed in section 3.

For 0<=l<=u, let Pi_[l,u] select polynomial degrees l through u. For any diagonal
G(D) and polynomial p(t)=sum p_j t^j, direct coefficient extraction
gives the exact commutator

    [Pi_[l,u], t G(D)]p
      =G(l-1)p_(l-1)t^l-G(u)p_u t^(u+1).          (11)

Negative coefficients are zero. The original demand slice is
Pi_[max(0,n-M),min(M,n)] H_n. Its range changes with n; in particular
(10) cannot simply be asserted for these projected slices. Formula
(11), together with the difference between the adjacent projectors,
specifies the exact two boundary terms to retain. Empty ranges are
zero projectors and can be handled directly. This statement does not
replace an original projected sector by a full sum.

There is a compatible exact relation for the root's cap functional
L_N(p)=sum_j U_j p_j. Its moment proof gives

    L_N[t sin^2(theta(D+3/2))p]
       =L_N[sin^2(theta(D+1))p],  deg p<=d-1.       (12)

Put J(D)=sin^2(theta(D+1/2)) and T(D)=sin^2(theta(D+1)). Multiplying
(10) on the left by J(D), using J(D)t=t J(D+1), then (12), yields

    L_N[(J A_n+T B_(n-1))H_n]
       =L_N[(J B_n-T E_(n-1))H_(n+1)].            (13)

This is valid throughout 0<=n<=d-1 without requiring a divergent
moment: B_(n-1)H_n has degree at most n-1, and
E_(n-1)H_(n+1) has degree at most n-1. The other highest terms are
annihilated by B_n. For n=0 these products are zero. In particular no
extension of (12) to degree d has occurred.

The diagonal operators in (13) are Laurent polynomials in Q^D of
degree at most two. The resulting relation is not closed on L_N(H_n)
alone. It must not be read as a scalar recurrence for the original
cutoff sum. Any use on that sum first requires the projector terms
(11), as well as the adjacent-projector difference, before applying
the degree-restricted functional identity.

## 6. An explicit orthogonal basis for one beta factor, and the cap tensor metric

There is a further exact positive construction, distinct from the
source-continuant Jacobi matrix. Keep only one of the two independent
copies in the cap moment proof. It gives a positive random variable Y_N
with

    w_j=E Y_N^j=sqrt(U_j/U_0), 0<=j<=d,
    w_j/w_(j-1)=sin(j theta)/sin((j+1/2)theta).      (14)

The square root is positive. The single-copy convergence and moment
proof is the same beta-product proof with no squaring. Its distribution
is non-atomic and positive; moments through d are finite. Thus
ell_N(p)=E p(Y_N) is a positive definite polynomial inner product on
V_M, the space of degrees at most M, by ell_N(p conjugate(q)).

On V_M define the degree-preserving real operator

    T=t^(-1)[cos(2theta D)-1]
                        -cos(theta(2D+1/2)).       (15)

The first factor annihilates the constant, so (15) is a polynomial
operator, not division of a nonzero constant by t. Write
A_j=cos(2j theta)-1 and B_j=-cos((2j+1/2)theta). Then
T(t^j)=A_j t^(j-1)+B_j t^j.

This operator is symmetric for ell_N. On a pair of monomials t^i,t^j,
with s=i+j>=1, the difference of the two matrix elements is

    (A_i-A_j)w_(s-1)+(B_i-B_j)w_s
      =2sin((i-j)theta)
           [-sin(s theta)w_(s-1)+sin((s+1/2)theta)w_s]=0. (16)

For i=j=0 both first coefficients vanish and the assertion is
immediate. All used moments have degree at most 2M<=d. Real
coefficients then give the Hermitian statement for complex polynomials.

The triangular eigenvalues B_n, 0<=n<=M, are distinct: their angles
(2n+1/2)theta lie strictly between zero and pi. There is therefore a
unique eigenpolynomial P_n of degree n normalized by P_n(0)=1. Its
coefficients c_j satisfy the explicit finite recurrence

    c_0=1,
    c_(j+1)/c_j
       =- sin((n+j+1/2)theta) sin((n-j)theta)
                       /sin^2((j+1)theta),
    0<=j<n.                                       (17)

This follows directly by equating the t^j coefficient of T P_n=B_n P_n.
All factors in (17) are nonzero in the indicated range, so the
normalization and degree are valid. Symmetry and distinct eigenvalues
prove that P_0,...,P_M are mutually orthogonal for the positive
single-factor metric. Their norms are strictly positive and finite.
No external q-polynomial identity or representation-theoretic
unitarity is used in this derivation.

Let Y_N' be an independent copy. The cap moment variable can be taken
as X_N=Y_N Y_N'. For F of degree at most M define the monomial-diagonal
embedding

    I F(t,u)=F(tu) in V_M tensor V_M.

Then its exact tensor norm is

    ||I F||_(ell tensor ell)^2
       =sum_(i,j) F_i conjugate(F_j) w_(i+j)^2
       =U_0^(-1) ||F||_cap^2.                     (18)

Equivalently the cap Gram matrix divided by U_0 is the entrywise square
of the single-factor Gram matrix. Its original signed functional is

    L_N(F(-t))=U_0 < I(F(-t)), 1 tensor 1 >.        (19)

Thus the explicit orthogonal product basis P_a(t)P_b(u) is a genuine
positive tensor metric for the original cutoff polynomial. Both J_n
boundaries remain in F=F_(N,n); no unrestricted degree is introduced.

The monomial-diagonal subspace is NOT automatically invariant under
T acting on either factor. Indeed for 1<=j<=M, A_j is nonzero and

    (T tensor I)(t^j u^j)
       =A_j t^(j-1)u^j+B_j t^j u^j

has a nonzero off-diagonal monomial. The positive tensor metric alone
therefore supplies no source continuant identity, projected Racah
operator, or endpoint norm comparison. Deriving such an identity with
the actual coefficient projections is still required for the original
uniform polynomial convolution bound.

## 7. Exact norms of the single-factor eigenpolynomials

The explicit coefficients also give their norms without an imported
orthogonality formula. In this section write

    sigma_r=sin(r theta), tau_r=sin((r+1/2)theta),
    kappa_n=[t^n]P_n(t).

Multiplying (17) gives

    kappa_n=(-1)^n product_(r=n)^(2n-1) tau_r
                         /product_(r=1)^n sigma_r,
    [t^(n-1)]P_n/kappa_n
       =-sigma_n^2/(sigma_1 tau_(2n-1))=:r_n,
    r_0=0.                                        (20)

The coefficient formula (17) is also meaningful for n=M+1=m. This
one additional polynomial is an eigenpolynomial whose eigenvalue is
distinct from all those at 0,...,M: its angle is (N+1/2)theta, and no
angle (2j+1/2)theta for j<=M has the same cosine. Applying (16) to
its pairings with degrees<=M uses only moments through 2M+1=d.
It is therefore orthogonal to V_M in this cross-moment sense. Its
squared norm is NOT used or asserted finite; it diverges.
Indeed the single-copy Y_N contains an independent inverse
Beta(N-1/2,1/2) factor, so E Y_N^N is infinite; the nonzero leading
term of the degree-N/2 polynomial forces its squared integral to diverge.

Orthogonality gives the multiplication recurrence, including n=M,

    t P_n=Acal_n P_(n+1)+Bcal_n P_n+Ccal_n P_(n-1),
    Acal_n=-sigma_(n+1)tau_n/[tau_(2n)tau_(2n+1)],
    Bcal_n=r_n-r_(n+1),
    Ccal_n=-sigma_n tau_(n-1)/[tau_(2n-1)tau_(2n)]. (21)

For n=0 the last term is zero. To prove the absence of lower terms,
pair tP_n with P_j, j<=n-2, move multiplication to tP_j, and use its
degree<n; the P_(n+1) cross pairings also vanish. The leading and
next coefficients give Acal_n=kappa_n/kappa_(n+1) and Bcal_n as
displayed. Finally P_j(0)=1 implies Ccal_n=-Acal_n-Bcal_n.
The last formula in (21) follows from the following exact sine
addition identity, which records the only simplification required:

    sigma_(n+1)^2 tau_(2n-1)tau_(2n)
       -sigma_n^2 tau_(2n)tau_(2n+1)
      =sigma_1 [sigma_(n+1)tau_n tau_(2n-1)
                         +sigma_n tau_(n-1)tau_(2n+1)]. (22)

It follows by substituting sin(a+b) and sin(a-b), or by writing
each sine as its two exponentials and canceling. All denominators
in (20)--(21) that are used are nonzero at the stated even levels.

Write g_n=ell_N(P_n^2)>0 for 0<=n<=M; these are not the source-Jacobi
norms h_r in (6). Pair (21) with P_(n-1),
then move t to the other factor. This yields

    g_n/g_(n-1)=Ccal_n/Acal_(n-1)
                =tau_(2n-2)/tau_(2n).

Since g_0=1, telescoping proves the exact closed formula

    g_n=sin(theta/2)/sin((2n+1/2)theta),
    0<=n<=M.                                      (23)

This is positive throughout the original finite Hilbert degree.
The product basis in section 6 therefore has explicit norm
g_a g_b. In fact 1/N<=sin(theta/2)<=g_n<=1, so these product norms
lie between N^(-2) and 1. This is a polynomial normalization of the
displayed orthogonal basis, NOT a condition-number bound for its
change of basis from the original monomials.
The original cap norm remains the restriction to the
monomial-diagonal embedding, and that subspace still fails the
invariance test following (19). Formula (23) does not identify the
source continuant or prove its required endpoint comparison.


## 8. The actual slices are not a scalar orthogonal family

This exact finite obstruction rules out one possible identification;
it does not rule out the tensor construction or the original convolution
bound. Normalize the auxiliary signed slices of section 5 by

    Hhat_n(t)=H_n(t)/C_(0,n).

At N=12, M=5, so n=0,1,2,3 all have their original genuine range
J_n=0,...,n. Direct exact arithmetic from the source recurrence and
every unused suffix factor gives

    Hhat_0=1,
    Hhat_1=1-2t,
    Hhat_2=1-(2+sqrt(3)+sqrt(2)+sqrt(6)/2)t
                +(7+sqrt(2)+sqrt(3)+sqrt(6))t^2/2,
    Hhat_3=1-(8+5sqrt(2))t
              +(15+10sqrt(2)+3sqrt(3)+2sqrt(6))t^2
              -(14+8sqrt(2))t^3.                   (24)

All coefficients belong to Q(sqrt(2),sqrt(3)). Write
Hhat_2=1+a t+b t^2 and Hhat_3=1+c t+e t^2+f t^3. Comparing powers
of t in

    t Hhat_2=A_3 Hhat_3+A_2 Hhat_2+A_1 Hhat_1+A_0 Hhat_0

gives A_3=b/f, A_2=(a-A_3 e)/b,
A_1=(1-A_3 c-A_2 a)/(-2), and A_0=-A_3-A_2-A_1. Hence

    A_0=(5341-5789sqrt(2)+1110sqrt(3)+665sqrt(6))/13906 !=0. (25)

The nonzero assertion is exact because 1,sqrt(2),sqrt(3),sqrt(6)
are linearly independent over Q. Its sign and decimal approximation
are unnecessary.

Were these four actual slices an orthogonal family for a nonzero
positive scalar measure with finite squared norms, symmetry of
multiplication would give

    <t Hhat_2,Hhat_0>=<Hhat_2,t Hhat_0>=0,

because t Hhat_0 lies in span(Hhat_0,Hhat_1). But (25) makes the left
side A_0 ||Hhat_0||^2 nonzero. Rescaling the individual slices does
not remove this obstruction. They therefore cannot simply be one
positive scalar orthogonal-polynomial family. No tensor or block
identification is refuted, and no source-growth conclusion follows.

The [focused exact verifier](../experiments/research_audit_cap_demand_scalar_orthogonality.py)
rebuilds the original K_r and all unused tails, checks the ten
coefficients in (24), and verifies the full triangular expansion and
(25) in the exact field. Its [recorded result](../experiments/research_cap_demand_scalar_orthogonality_results.json)
contains only exact field arithmetic. It concerns this
finite scalar-identification obstruction only; it is not an audit of
the analytical metric theorems or an asymptotic numerical experiment.


## Internal review and exact remaining question

Root and geometry independently read the complete analytical/source
proof, including the operator appendix, single-factor eigenbasis,
finite cross-moment treatment and exact norms, and reported PASS.
Cluster independently reviewed sections 1--4 in full, also PASS.
Root and geometry additionally read the complete section 8 proof and
verifier and each completed a fresh exact redirected replay, PASS.
The portable verifier changes only its sibling default-output filename;
its verification-function AST is identical to the reviewed private code.
The portable replay reproduces both independent results exactly.
These are internal reviews, not external peer review. No numerical
asymptotic diagnostic is used as proof.

The two positive metrics must remain distinct: the source continuant
has the Jacobi measure of section 2, while the original cap has the
[positive moment and finite quadrature form](research_flat_cap_positive_moment_form.md)
and the tensor realization in sections 6--7. The still-open statement
is the uniform polynomial comparison in the
[original-demand convolution](research_two_port_main_cap_original_demand_convolution.md),
with both endpoints of J_n and every unused source factor retained.
No source-volume or full-invariant bound is obtained here.
