# The original operator period has a controlled closing region at two

30 October 2026. A whole right half-disk
at the spectral endpoint has vanishing exponential cost as its radius
tends to zero. The bound is uniform over EVERY physical degree and
every original matrix entry, including the Jordan blocks. Fixed genuine
generic-q and spectral derivatives of the resolvent have the same
vanishing-rate property. Combined with the separately proved canceled
Sears bound for the actual scalar polynomial, it controls the full
original integrand and its fixed generic normals throughout that region.

The same estimates extend to a fixed angular slit cone on both sides
of that half-disk, avoiding the spectral poles on the left real ray.
The statement is an upper estimate. It does not select a contributing
contour or give a nonzero saddle contribution. The scalar normal input
to the final assembly is proved in its linked companion theorem.

## 1. Uniform finite statement

Use the original physical matrix J_t, q=exp(pi i/N), d=N-1, N>=3,
and 0<=t<=d. Define

    f(r)=sqrt(r) log(2+1/r), r>0, and f(0)=0,
    H_N(r)=C N^3 exp[C N f(r)+C(log N)^2].          (1)

There is an absolute C such that for every 0<=r<=1/4,

    ||(zI-J_t(q))^-1||op<=H_N(r),
                  Re z>=2, |z-2|<=r.              (2)

The same holds for the actual high-degree blocks, by their exact
generic adapter. For fixed nonnegative integers j,k, with
R_t(h,z)=(zI-J_t(q exp(h)))^-1, one also has on this region

    ||partial_h^j partial_z^k R_t(0,z)||op
        <=C_(j,k) N^j max(1,H_N(r))^(j+k+1).       (3)

These are genuine generic derivatives of the original matrix, with
its distinct moving upper and lower entries. In particular

    lim_(r down 0) limsup_(N->infinity)
      N^-1 log sup_(t,z) ||partial_h^j partial_z^k R_t(0,z)||op
          <=0.                                   (4)

Here z ranges over the half-disk in (2). Replacing a zero norm by
max(1,norm) gives the equivalent nonnegative-rate formulation.

More generally fix 0<gamma_0<pi/2. All these statements hold, with
constants depending on gamma_0, throughout

    K_(r,gamma_0)={2} union
       {z=2+rho exp(i phi): 0<rho<=r,
                                 |phi|<=pi-gamma_0}.             (4a)

This includes parts of the disk to the LEFT of two, but excludes a
fixed angular neighborhood of the left real ray containing the poles.

## 2. Every prefix has a small positive determinant rate

Put theta=pi/N. The exact ground-state congruence in the
[endpoint theorem](actual_casimir_endpoint_resolvent_bound.md) gives,
for any leading prefix of size 1<=m<=t,

    |det(J_[m]-zI)|=|det(L_m+(z-lambda_0)V_m)|,
    lambda_0=2cos(theta), |(V_m)_(r,r)|=1.          (5)

L_m is the real Dirichlet path matrix with conductances

    a_r=4sin((t-r)theta)sin((r+1)theta), 0<=r<t,
    (L_m)_(r,r)=a_(r-1)+a_r, a_(-1)=0,
    (L_m)_(r,r+1)=-a_r.                           (6)

The final term a_(m-1) is retained as a Dirichlet boundary spring.
The principal minors are positive, so expansion in the diagonal
perturbation, term by term in absolute value, yields

    |det(L_m+(z-lambda_0)V_m)|
       <=det L_m det(I+s L_m^-1), s=|z-lambda_0|,
    det L_m=product_(r=0)^(m-1) a_r.              (7)

The following estimate holds uniformly in ALL t,m,N and 0<=s<=2:

    log det(I+s L_m^-1)
       <=C N f(s)+C(log N)^2.                     (8)

Here is a direct path proof, including the two small-conductance
endpoints. Let h_r=min(r+1,t-r). Since t<=N-1, both integers r+1
and t-r, and their distances from N, are at least h_r. The elementary
sine lower bound therefore gives

    a_r>=16 h_r^2/N^2.                            (9)

The exact inverse-trace formula for L_t then gives

    Tr L_t^-1=sum_(r=0)^(t-1)(r+1)/a_r<=C N^3.     (10)

In particular its smallest eigenvalue is at least c N^-3.

Partition the rows of L_t into consecutive dyadic blocks from the
left and right endpoints towards the middle. There are O(log N)
blocks, with a bounded number of each dyadic length, apart from at
most two shorter remainder blocks. On a block of length ell, every
internal conductance is at least c ell^2/N^2 by (9). Remove the
springs between blocks and the final Dirichlet spring. The resulting
block-diagonal Neumann operator is smaller than L_t as a quadratic
form. A constant-conductance Neumann path of length ell has eigenvalues

    4 a sin^2(pi k/(2ell)), 0<=k<ell.

Consequently each such block contributes at most
1+C min(ell,N sqrt(lambda)) eigenvalues at most lambda.
Summing the dyadic lengths gives the counting estimate

    n_t(lambda)<=C log N
          +C N sqrt(lambda) log(2+1/lambda).       (11)

For clarity, with x=N sqrt(lambda), the sum of lengths below x is
O(x), while the larger blocks contribute O(x[1+log(N/x)]).
If x<1, their contribution is O(x log N), which is bounded by the
second term in (11). For large lambda the trivial bound n_t<=N
is stronger. Prefix interlacing gives n_m(lambda)<=n_t(lambda)
and the same lower eigenvalue bound as in (10).

For positive eigenvalues mu, integrate the identity
log(1+s/mu)=integral_mu^infinity s/[lambda(lambda+s)] d lambda.
The C log N term of (11), starting at cN^-3, costs O((log N)^2).
The other term has integral at most C N f(s): set lambda=s y and
use the integrability of y^-1/2(1+y)^-1 and the same function
times |log y|. This proves (8), with s=0 immediate.

No inverse bound for a long complex Casimir prefix was assumed.
Only the real positive path L_m enters this comparison.

## 3. Exact cancellation controls all original Green entries

For u<=v the original continuant identity expresses R_(u,v) as
the leading prefix determinant of size u, the trailing determinant
of size t-v, and the product of original upper entries between them,
divided by the full characteristic polynomial. At the root the
trailing prefix is the reflected conjugate of a leading prefix;
the magnitudes a_r in (6) obey a_(t-1-r)=a_r. Thus the conductance
products from the two bounds (7) and the middle Green product
telescope EXACTLY to

    product_(r=0)^(t-1) a_r=s_t^2,
    s_t=product_(r=1)^t 2sin(r theta).             (12)

The root matrix is symmetric, so the same estimate holds for u>v.
Its exact characteristic polynomial has real roots below two:

    chi_t(z)=product_(r=0)^t[z-2cos((2r+1)theta)].

For Re z>=2, each factor has magnitude at least its value at two.
The already proved exact product inequality is

    |chi_t(z)|>=chi_t(2)>=4s_t^2/N^2.             (13)

Equations (7),(8),(12),(13) therefore bound EVERY entry by

    (N^2/4) exp[2C N f(|z-lambda_0|)+2C(log N)^2]. (14)

Empty prefixes have determinant one and cause no exception.
For t=0 the scalar bound follows directly from
2-lambda_0>=4/N^2. Finally |z-lambda_0|<=r+delta with
delta=2-lambda_0 comparable to N^-2. The elementary inequality
f(a+b)<=f(a)+f(b) gives N f(r+delta)<=N f(r)+C log N.
The function f is increasing: its derivative has the sign of
log x-2+4/x for x=2+1/r>=2, whose minimum is log 4-1>0.
Multiplying the entrywise bound by the dimension at most N proves
(2). In particular the proof includes t=N-1 and long prefixes;
no compact restriction on physical degree is needed.

### The angular slit-cone extension

The same numerator estimate applies at any complex z. Only the full
characteristic lower bound changes outside Re z>=2. Write

    x_h=2-2cos((2h+1)theta)>0,
    |chi_t(2+rho exp(i phi))/chi_t(2)|
       =product_(h=0)^t |1+rho exp(i phi)/x_h|.     (14a)

For |phi|<=pi-gamma_0 and every y>=0 one has
|1+y exp(i phi)|>=sin(gamma_0). Split the factors in (14a) at
x_h=2rho. To count them, put
v_h=min(h+1/2,N-h-1/2). The complete list 0<=h<N satisfies

    16 v_h^2/N^2<=x_h<=4pi^2 v_h^2/N^2.

There are O(N sqrt(rho)+1) factors with x_h<=2rho, so their total
logarithmic loss is at most C_(gamma_0)(N sqrt(rho)+1).
For the other factors, y=rho/x_h<1/2 and
log|1+y exp(i phi)|>=log(1-y)>=-2y. The two displayed comparisons,
followed by the convergent tail sum of v_h^-2, give

    sum_(x_h>2rho) rho/x_h<=C(N sqrt(rho)+1).

Bounding the entire list also bounds every degree sublist. Hence

    |chi_t(z)/chi_t(2)|
       >=exp[-C_(gamma_0)(N sqrt(rho)+1)]           (14b)

on (4a). The additional loss is absorbed in N f(r)+O(log N).
This proves (2),(3),(4) on the full cone (4a).

The cone has a useful literal overlap with the earlier strict-prefix
action domains. For any fixed strict pair of prefix angles beta_1,
beta_2<pi, choose gamma_0 smaller than both (pi-beta_i)/2. Points
z=2-rho exp(+/-i gamma_0) then lie in BOTH selected-prefix halfplanes.
Thus the estimate reaches potential joining points for those actual
integrand charts. No contour deformation or saddle contribution follows
from this overlap alone.

## 4. Actual generic normals remain controlled

For each fixed j>=1 the displayed original generic matrix satisfies

    ||partial_h^j J_t(q exp(h)) evaluated_(h=0)||op<=C_j N^j.

This follows directly from its fixed bandwidth and finite products
of monomials with exponents O(N). Differentiating the inverse identity
retains the exact moving matrix: partial_h R=R(partial_h J)R and
partial_z R=-R^2. Each mixed derivative is a finite sum of products
with at most j+k+1 resolvent factors and total h-derivative order j
on the intervening J factors. Bound them by (2) to obtain (3).
This argument includes every moving eigenvalue and Jordan-current
term, and differentiates no root-only reflection.

## 5. The root scalar integrand also has vanishing closing rate

The actual polynomial p_a(q,z), 0<=a<=floor(d/2), has only simple
roots strictly above two. Its normalization makes p_a(q,x)>0 for
real x<2. Therefore the factorization into its actual roots gives
the exact estimate

    |p_a(q,z)|<=p_a(q,2-r), |z-2|<=r.              (15)

This remains true on the part of the disk crossing the scalar's
LIMITING cut: the finite source is a polynomial there and (15)
does not select or continue a logarithm through its zeros.

For a/N->alpha in (0,1/2], the proved slit action gives
N^-1 log p_a(q,2-r)->Psi_alpha(2-r) at every fixed r>0.
Its explicit real formula has Psi_alpha(2-r)->0 as r decreases to
zero. Indeed its maximizing t_* satisfies

    sin^2(pi t_*)=A r/(r+4A), A=sin^2(pi alpha),

so t_*=O(sqrt(r)); the sine-log integrals in that formula tend to
zero, including their integrable endpoint logarithms. Thus (2),(15)
prove

    lim_(r down 0) limsup_(N->infinity) N^-1 log
       sup_(Re z>=2,|z-2|<=r)
          ||p_a(q,z)(zI-J_t(q))^-1||op <=0,         (16)

uniformly over every physical degree t. The actual face factor is
one at the root. The same conclusion holds with any fixed generic
or spectral derivative placed on the RESOLVENT factor alone, by (3).

Consequently a closing arc of bounded length contained in this
half-disk has the upper rate (16). This is a genuine estimate on
the entire closing region, rather than an inference from a tiny
endpoint disk. This root-factor argument does not itself estimate
generic derivatives of the scalar polynomial on that whole region;
Section 6 uses the separate scalar theorem for them. Neither argument
estimates the rest of an enclosing
contour, its deformation or intersection numbers, or the coherent
surrounding state. A contributing geometric saddle and noncancellation
remain separate requirements.

All conclusions in this section also hold on the slit cone (4a),
with its fixed gamma_0-dependent constants. The scalar estimate (15)
already holds on the whole disk, and (14b) supplies the only extra
resolvent cost.

## 6. Assembly for the full original integrand and its generic normals

The independently proved
[canceled-Sears closing theorem](actual_matching_edge_polynomial_closing_region_bound.md)
supplies the scalar factor on the WHOLE complex disk, including its
genuine generic-q normals and the actual face scalar. Combine it with
(2),(3),(4a). For

    I_(N,a,t)(h,z)=D_a(q exp(h))^-1
                   p_a(q exp(h),z)(zI-J_t(q exp(h)))^-1,

every fixed j,k>=0 satisfies

    sup_(z in K_(r,gamma_0))
        ||partial_h^j partial_z^k I_(N,a,t)(0,z)||op
       <=C_(j,k,gamma_0) r^-k N^(4j+3k+3)
          exp[C_(j,k,gamma_0) N f(r)
                         +C_(j,k,gamma_0)(log N)^2].             (17)

This holds uniformly in ALL 0<=a<=floor((N-1)/2), ALL 0<=t<=N-1,
both level parities and 0<r<=r0, for a sufficiently small fixed r0.
The angular exclusion gamma_0 remains fixed and positive. No limit
a/N->alpha is required in (17).

Here are the finite costs in the pure Leibniz argument. Put i of the
j generic derivatives and l of the k spectral derivatives on the
scalar factor. Its companion bound costs at most
N^(3i) r^-l exp[C N f(r)+C log N], since p_a(q,2)<=1.
The remaining resolvent derivatives cost, by (3),

    C N^(j-i) H_N(r)^(j-i+k-l+1).

The resulting power of N is
4j-i+3k-3l+3<=4j+3k+3, and r^-l<=r^-k. Summing the finitely many
Leibniz terms proves (17). The inverse face scalar and all its q jets
are already part of the scalar companion theorem; none is discarded.

In particular, let r_N decrease to zero at ANY rate and let an arc
Gamma_N lie in K_(r_N,gamma_0), with length at most a fixed power of N.
Hold that arc fixed while taking generic-q derivatives. For every
fixed j, the integral over Gamma_N of partial_h^j I(0,z) has norm
at most exp[o(N)]. This uses k=0 in (17), so there is no r_N^-k loss.
It includes the actual finite source normals needed by the exceptional
operator period, not just its root value.

This cap estimate does not prove a deformation of the remainder of
the original contour, its saddle intersection number or a nonzero
geometric contribution. In particular it leaves the surrounding
complement and its coherent contraction explicit: multiplying this
block by an uncontrolled environment is not a completed volume bound.

Audit: [dyadic path comparison, all-prefix determinants and original Green entries](../experiments/audit_actual_casimir_closing_region_bound.py).

The finite spectral-count samples are diagnostics. The uniform estimates come from the proof. Section 6 uses the two bounds and the displayed Leibniz count, retaining the actual face factor, conservative power of N, arbitrary shrinking radii when k=0, fixed angular exclusion and the stated surrounding-environment limitation.