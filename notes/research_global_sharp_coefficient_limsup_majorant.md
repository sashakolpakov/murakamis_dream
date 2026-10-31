# A global closed-domain coefficient majorant from the original full tail

Analytical research theorem, 31 October 2026. Root and coherent
completed full internal analytical reviews; this is not external peer review. This extends the reviewed regular
LIMSUP estimate to all closed row and degree boundaries and the entire real
spectral interval. It remains only an upper bound. No nonzero coefficient
limit, phase cancellation, or quantum-cycle contribution is claimed.

## 1. Exact treatment of the final spectral cap

Retain the original full interval 0<=i<=j<=d=N-1 and r=j-i. Write
theta=pi/N, kappa=cos(pi delta), 0<=delta<=1/2, and

    lambda_N=cos(theta)+cos(2pi delta),
    eta_a=lambda_N/[cos(theta)-cos((2a-1)theta)].

The actual coefficient of x^k b^i c^(d-j)y^(r-k), 0<=k<=r, is

    a_N=(prod_(a<i)alpha_a(delta))(prod_(a>j)alpha_a(delta))
                                      [x^k y^(r-k)]K_(i,j),

up to the recorded common unit sign. Thus its total degree is d. In
particular CROSS is one full-interval K, not a difference of separately
estimated central cofactors. Put s_a=2sin(pi a/N). The exact recurrence is

    K_(i,i)=1, K_(i,i+1)=s_(i+1)^2(x+y),
    K_(i,a)=s_a^2(x+y)K_(i,a-1)
                  +s_a s_(a-1)alpha_(a-1)xy K_(i,a-2), a>=i+2.

Dividing by prod_(i<h<=a)s_h^2 gives second coefficient
alpha_(a-1)/(s_a s_(a-1))=eta_a-1: the exact identity is
alpha_(a-1)+s_a s_(a-1)=2lambda_N. The row range avoids s_0.

Every used denominator, i+2<=a<=j<=d, is positive. The exact normalized
tail Q=K_(i,j)/prod_(i<a<=j)s_a^2 has the two-letter word expansion:
the coefficient of each x^k y^(r-k) is a polynomial in lambda_N with
NONNEGATIVE coefficients. Thus, even on the last cap where lambda_N<0,

    |[x^k y^(r-k)]Q(lambda_N)|
                  <=[x^k y^(r-k)]Q(|lambda_N|).        (1)

This is the actual eta-word expansion, not an absolute-value substitution
in the original signed two-step recurrence. Define a real effective
spectral parameter by

    cos(2pi delta_eff)=|lambda_N|-cos(theta).

For N>=3 its right side lies in[-1,1], and its eta parameters are exactly
the positive ones in (1). If k_eff=cos(pi delta_eff), then

    k_eff^2=kappa^2                 if lambda_N>=0,
    k_eff^2=1-cos(theta)-kappa^2    if lambda_N<0.     (2)

The negative case implies kappa^2<(1-cos theta)/2. Hence uniformly

    |k_eff-kappa|<=sqrt(1-cos theta)=O(1/N).           (3)

The ORIGINAL unused alpha_r(delta) factors are NOT changed to delta_eff.
If any of them, or the retained A_rest factor, vanishes, the coefficient
is zero and automatically satisfies the upper bound.

## 2. Uniform fixed-tilt bounds on the full compact parameter set

For any fixed T<infinity, all l in[-T,T], every original row interval,
and all real delta in[0,1/2], the full-interval fixed-block proof gives

    N^(-1)log K_(i,j)(exp(l),1;delta_eff)
      <=int_(i/N)^(j/N) log Lambda_(delta_eff)(t;exp(l),1)dt+o(1), (4)

uniformly. Here are the inputs that remain valid at the cap. Divide K
by prod_(i<h<=a)s_h instead of its square. The exact signed transfer is

    T_a=[[s_a(x+y),alpha_(a-1)(delta_eff)xy],[1,0]], a>=i+2,

with initial values 1 and s_(i+1)(x+y). Its entries are uniformly bounded
on the whole row range and the fixed tilt interval. Its frozen limiting
matrix has spectral radius

    rho=(x+y)sin(pi t)
           +sqrt((x-y)^2 sin^2(pi t)+4xy k_eff^2),

and both eigenvalue magnitudes are at most rho. On [eta,1-eta], rho has
a uniform positive lower bound. Cayley--Hamilton therefore bounds the
m-th power by C(m+1)rho^m with uniform C, INCLUDING the repeated-root
case x=y,k_eff=0; no eigenbasis inverse is used. For each fixed m, an
actual m-row block differs uniformly by o(1) from its frozen block.
Multiply these block bounds, then let N grow, m grow, and eta decrease
to zero in that order. The factor C(m+1) costs log(C(m+1))/m per row.
The bounded transfers on the two endpoint intervals cost O(eta N),
and their omitted logarithmic integrals cost O(eta log(1/eta)N).
Restoring prod s_a by its uniform sine-log upper sum gives (4), with
Lambda=2sin(pi t)rho. Uniformly in l and delta,

    c_T sin^2(pi t)<=Lambda_delta(t;exp(l),1)<=C_T,

so the missing endpoint integrals are uniformly small. The proof
includes the defective balanced root at the final spectral cap.

The integral in (4) is jointly continuous on the full compact set
of endpoints, delta and l in[-T,T]: on every interior t interval this
is ordinary continuity, and the displayed integrable lower bound
controls both endpoints uniformly. Equation (3) consequently allows
delta_eff to be replaced by delta in that integral at cost o(1),
uniformly in all these variables. Equivalently regard the integral
as a continuous function of kappa in[0,1], so no inverse-cosine
derivative near an endpoint is needed.

The original unused products satisfy the full uniform UPPER Riemann
estimate

    N^(-1)log |prod_(a<i)alpha_a(delta) prod_(a>j)alpha_a(delta)|
       <= B_delta(i/N,j/N)+o(1),
    B_delta(mu,nu)=int_0^mu log|alpha_delta(t)|dt
                              +int_nu^1 log|alpha_delta(t)|dt. (5)

The same truncation proof covers all real delta, including merging
cosine zeros and every sampled zero. The two cosine logarithms have
uniformly integrable singularities. Moving a mesh endpoint by one row
changes the corresponding integral by o(1) uniformly; a missing
sampled zero is never assigned a finite lower logarithm.

For the exact original coefficient a_N(k,i,d-j,r-k), equations(1)--(5)
and finite Cauchy extraction give, uniformly for l in[-T,T],

    N^(-1)log|a_N|
      <=B_delta(mu,nu)+Phi_delta(mu,nu,l)-xi l+o(1), (6)
    Phi_delta=int_mu^nu log Lambda_delta(t;exp(l),1)dt,
    mu=i/N, nu=j/N, xi=k/N.

No coefficient positivity is asserted on the negative lambda_N cap;
the exact domination (1) is what supplies (6) there. Both parities
and all original scalar modes/zeros are retained in the coefficient.

## 3. Uniform truncation of the outer Legendre infimum

Let w=nu-mu and 0<=xi<=w. Factor the limiting tail root as

    Lambda_delta(t;exp(l),1)=4sin^2(pi t) rho_eta(exp(l),1),
    rho_eta(x,y)=[x+y+sqrt((x-y)^2+4eta xy)]/2,
    eta=kappa^2/sin^2(pi t).

With a=exp(-|l|), the elementary square-root inequality gives

    1<=rho_eta(exp(l),1)/max(exp(l),1)
       =[1+a+sqrt((1-a)^2+4eta a)]/2
       <=1+sqrt(eta a).                            (7)

Thus log rho_eta=max(0,l)+r_delta(t,l), where

    0<=r_delta(t,l)
        <=log(1+exp(-|l|/2)/sin(pi t)).              (8)

Set

    R_T=int_0^1 log(1+exp(-T/2)/sin(pi t))dt.

It tends to0. An explicit bound, using sin(pi t)>=2min(t,1-t), is

    R_T <=(1+a_T)log(1+a_T)-a_T log a_T,
    a_T=exp(-T/2).                                 (9)

Subtract the l-independent sine integral from Phi-xi l. Its remaining
value is (w-xi)l+int r for l>=0 and -xi l+int r for l<=0. If l>T,
its value is at least(w-xi)T, while the value at T is at most
(w-xi)T+R_T. The same comparison holds at -T for l<-T. Therefore

    0<=inf_(|l|<=T)(Phi-xi l)-inf_(l in R)(Phi-xi l)<=R_T, (10)

UNIFORMLY in every closed row interval, xi, and delta. It includes
w=0, xi=0,w, delta=1/2 and exact protected endpoints. There is no
uniform-minimizer assumption and no concavity in mu or nu.

## 4. Continuity and the global coefficient LIMSUP

Define on the FULL closed parameter domain

    H_delta(mu,nu,xi)=B_delta(mu,nu)
                     +inf_l[Phi_delta(mu,nu,l)-xi l].   (11)

B is continuous, by the same uniform integrability as (5). For each
finite T the truncated minimum is continuous: its integrand is jointly
continuous on a compact parameter set, and the difference of two minima
is bounded by the uniform difference of their functions. Equation(10)
then makes H a uniform limit of continuous functions. In particular H
is continuous and finite on the entire closed domain.

Given epsilon>0 choose T with R_T<epsilon, use (6) uniformly on that
fixed tilt interval, and minimize there. Equations(10)--(11) prove

    limsup_(N->infinity) sup_(all i,j,k,delta)
       [N^(-1)log|a_N|-H_delta(i/N,j/N,k/N)]<=0.       (12)

This is a GLOBAL uniform coefficient upper bound, including the final
spectral cap, all closed outer degrees, diagonal and terminal intervals,
both level parities, and sampled zeros. Zero coefficients have logarithm
minus infinity. No lower rate or every-level equality is inferred.

If normalized degrees are taken over d=N-1, they sum to1 exactly and
give mu=q_b,nu=1-q_c,xi=q_x. The N-normalized parameters in (12) differ
by O(1/N). Uniform continuity of H on its full compact domain absorbs
that difference uniformly. No finite protected target or seam support
is changed.

## 5. The original shared-source upper problem is now compact

For a fixed actual diagram D with R ports, use the original incidence
flow polytope: each port supplies1, each ordinary face demands1, and
the two original protected faces demand0. Assume it is nonempty, as it
is in the certified geometric class. If it is empty, every finite source
coefficient is identically zero and no finite maximum is needed. Define

    M_D=max_(q in this polytope, delta in[0,1/2]^R)
                     sum_e H_(delta_e)(q_b,1-q_c,q_x). (13)

The maximum exists by continuity. The number of original finite degree
arrays is polynomial in N at fixed R. Apply (12) to every local factor
and the triangle inequality to the ONE original marked coefficient.
For its actual raw full numerator S_N,

    sup_(delta in[0,1/2]^R)|S_N(delta)|
                              <=exp{N[M_D+o(1)]}.     (14)

All signs and omitted-half phases are still in S_N; (14) bounds their
absolute sum rather than asserting they align. Only the upper passage
from finite arrays to limiting flows is used. There is no lattice lower
approximation, equality of rates, or separate optimization of local
weighted norms in place of the shared target.

The former boundary-UNIFORM coefficient-majorant burden is removed by
(12), but the boundary-GEOMETRY and global phase questions remain.
In particular neither M_D<=Phi_D nor a contributing full period is
proved here. The [full-fiber boundary reduction](research_full_fiber_sharp_boundary_activation.md)
and [stationary classification](research_full_fiber_sharp_stationary_classification.md)
apply to this compact upper problem at their stated scopes. The global
phase comparison still needs its own quantitative estimate. This proof uses no numerical audit.


## Dependencies and internal verification scope

The [original four-state source](research_original_one_sided_four_state_transfer.md)
supplies the exact full-interval coefficient and unused-row factors. The
[positive eta-word identity](research_positive_eta_word_transfer.md) gives
the polynomial domination in section1. The
[global CROSS proof](actual_global_cross_spectral_gap.md) supplies the
antecedent fixed-block argument; section2 extends it explicitly through
the cap on the full row range. The
[full-fiber stationary classification](research_full_fiber_sharp_stationary_classification.md)
is a downstream consequence together with the separate boundary lemmas;
it is not a premise of the coefficient upper bound.

Both internal reviews checked the exact recurrence and row indices, the
absolute-lambda substitution and effective spectral parameter, the signed
normalized transfer and repeated-root block bound, uniform unused-product
upper sums, uniform clipping of all tilts, closed continuity, degree
normalization and the original shared-target upper bound. No numerical
audit, lower coefficient rate, signed-source positivity at the cap, phase
alignment, geometric bound on M_D or full-period conclusion is claimed.
