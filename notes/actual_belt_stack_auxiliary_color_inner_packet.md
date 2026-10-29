# Actual auxiliary-color packets through the complete-circle quarter transition

29 October 2026. This extends the complete-circle boundary packet to
the ACTUAL inner auxiliary color j=N-h, rather than declaring its
pair-Casimir argument to be a peripheral parameter. It proves an
exact finite analytic inner packet on a fixed complex color disk,
with a nonzero joint spectral/color asymptotic, and a full physical
inner-color complement gap. Every original first Casimir normal and
Cartan phase remains present.

The final outer-circle color functional is a separate operation.
The estimates below supply its inner inputs; they do not by themselves
assert the hypotheses of the general long-filling theorem for the
whole stack or identify a deformed representation.

## 1. The actual mixed circle, including its nonzero second band

Use N,d,q,Q,kappa,M,F_r,s_r and the original continuants f_v from
[the exact mixed two-band source](actual_pretzel_cusp_color_two_band_bound.md).
For every physical 0<=h<=M, the FULL all-port identity is

    z_(N,h)=mathscrR(R^(-1)L_(N-h))=c_(N,h)+R P_(N,h),
    c_(N,h)=kappa^(-1) sum_(v=h)^M
                  N^2 s_(2v) f_v/[s_v^2 s_(v-h)s_(v+h)].       (1)

Here L_j is the literal ordinary mixed-color auxiliary trace and
mathscrR is the genuine unscaled physical turn. For j<=N/2 the
whole box is the pure alias (-1)^N R P_(N,j), including the even
middle color. Thus all physical colors are accounted for.

The reflected box is z_(N,h)^sharp. The sharp operation means
coefficient conjugation, including kappa and the fixed root. Its
complex-color continuation will be defined by Schwarz reflection
of the specified analytic packet, not by conjugating its parameter
inside an allegedly holomorphic expression.

For the physical low core, interchanging its two finite sums gives

    c_(N,h)(c)=N^2 sum_(r=0)^M b_(N,r)(h) B_r(c),
    b_(N,r)=kappa^(-1) q^(h^2)(-1)^r q^(2r^2+r)
                                                    A_(h,r)/F_r^3,
    A_(h,r)=sum_(v=max(h,r))^M
      Q^(-vr)F_(2v)/[F_v F_(v-h)F_(v+h)F_(v-r)],
    B_r(c)=product_(a<r)(c_a-c).                           (2)

These are exact root identities with their ORIGINAL marked phases.
No upper band, source normal or normalization is suppressed.

## 2. A source-selected complex-color channel THROUGH the quarter point

Put tau=r/N, chi=pi h/N, H=exp(2i chi), Y=exp(2pi i tau),
epsilon=1/N. On a fixed compact r-window about N/4, define A_(h,r)
for COMPLEX h=N chi/pi by replacing F_(v-h),F_(v+h) in its finite
sum v=r,...,M by the canonical marked Fhat_N. All these arguments
remain in regular nonzero factorial strips after choosing a fixed
small complex chi disk. The continuation is even in chi and equals
the physical coefficient whenever h is an integer below the window.

Normalize U_(h,r)=A_(h,r)/D_(h,r), where

    D_(h,r)=Q^(-r^2)F_(2r)/[F_r Fhat_N(r-h)Fhat_N(r+h)].

The [literal mixed Ward and high source](actual_pretzel_mixed_inner_source_wkb.md)
prove, for THIS finite factorial continuation,

    U_r=p_N(tau,chi) U_(r+1)+q_N(tau,chi) U_(r+2),        (3)
    p_N=-Q^(-2)Y^(-1)(2cos(2chi)Q^3Y^2+Q+1)
                                      /[(1-QY/H)(1-QYH)],
    q_N=-Q^(-4)Y^(-2)(1-Q^2Y)(1-Q^3Y^2)(1+Q^2Y)
       /[(1-QY/H)(1-QYH)(1-Q^2Y/H)(1-Q^2YH)].

The original source is U_M=1; its q_(M-1)=0 wall is exact at
both parities and remains independent of complex chi. In particular
the actual source, rather than an arbitrary solution of (3), is
holomorphic and nonzero at a strict high-index anchor.

Let mu_s,mu_f be the roots of the principal companion, continued
from mu_s=-Y^(-1), mu_f=Y^(-1)cot(pi tau)^2 at chi=0.
They are distinct and nonzero near tau=1/4 on a fixed complex
neighborhood and small chi disk. Their relative multiplier in
HIGH-to-LOW transport at chi=0 is -cot(pi tau)^2.

Apply the supplied-eigenframe analytic diagonalizer from
[the boundary-packet proof](actual_complete_circle_boundary_packet.md#2-the-exact-direction-of-transport-and-a-source-barrier),
now holomorphically in chi. First fix its neighborhood and positive
exponential remainder barrier sigma. Then choose a small fixed
delta, anchor u_b=pi/4+2delta+O(1/N), and target
|u-pi/4|<=delta/4. At chi=0 the relative fast action from anchor
to ANY target is at most -gamma_0<0, while its entire intermediate
action width is O(delta^2)<sigma/4. Continuity on the fixed complex
chi disk preserves a strictly negative target action and width<sigma/2.
Shrink chi AFTER delta; merely distinct roots do not imply this.

The established high-index continued fraction supplies the exact
anchor vector. Relative to its nonzero selected scalar, its slow
coefficient is1+O(1/N), its fast coefficient O(1/N), uniformly for
complex chi. Multiplying the exponentially diagonalized recurrence
in its diagonal interaction frame bounds EVERY conversion error by
exp[-N(sigma-width)]. The initially present fast source component
is exponentially damped on the target. No source component or
compensating current is deleted. This proves selection through the
modulus crossing, uniformly on that fixed complex parameter disk.

Optimal analytic Euler--Maclaurin of the slow diagonal product,
anchored to the SAME exact high source coefficient, now gives a
holomorphic zero-free Uhat_N(tau,chi) on a tube containing the
whole anchor-to-target interval. On the target physical r-grid,

    U_(h,r)=Uhat_N(r/N,chi)[1+O(exp(-gamma N))].           (4)

All statements are uniform in complex chi. The first transport
coefficients are exactly the old rational expressions

    S(tau,chi)=integral_tau^(1/2) Log mu_s(t,chi)dt,
    C(tau,chi)=sqrt(mu_s(tau,chi))
                    exp[integral_tau^(1/2)nu/mu_s dt],
    nu=[p_1+q_1/mu_s-q_0(partial_tau mu_s)/mu_s^2]
                                         /[1+q_0/mu_s^2].    (5)

The roots are continued from the original high interval to the
target; the denominator is1-mu_f/mu_s and does NOT vanish at the
quarter point. The normal-form diagonal and its first correction
are holomorphic. Their explicit first-order scalar transport gives

    Uhat_N=C(tau,chi) exp[N S(tau,chi)] [1+O(1/N)].        (6)

The constant is fixed by the old high source on the overlapping
anchor tube, not by an unknown closed circle value. Formula (5)
agrees there with the proved selected transport; the same analytic
nonresonant transport equation continues it uniquely across the
quarter point. This separates the algebraic leading error in (6)
from the exponential original-grid error in (4).

## 3. Exact finite analytic inner packet and its joint asymptotic

Choose a fixed index window I_N about the quarter point whose
closure lies STRICTLY INSIDE the controlled target neighborhood
in section2; for example use |u-pi/4|<=delta/8. Its endpoints
may move by O(1/N) to the physical grid. It is nonempty for all
sufficiently large N. Take the finite polynomial

    Z_N^win(c,chi)=N^2 sum_(r in I_N)
        kappa^(-1) q^(h^2)(-1)^r q^(2r^2+r)
                                            Ahat_(h,r) B_r(c)/F_r^3, (7)

where Ahat is the EXACT finite factorial completion in section2.
It is even holomorphic in chi on a fixed complex disk, with all
Casimir derivatives literal. The reflected packet is
Z_N^(win,sharp)(c,chi)=conjugate(Z_N^win(conjugate(c),conjugate(chi))).
Both are holomorphic, with their separate typed source phases.

Let J_sin(tau)=integral_0^tau Log(2sin(pi t))dt and define

    B(tau,chi)=S(tau,chi)-S(tau,0)+2J_sin(tau)
                 -J_sin(tau-chi/pi)-J_sin(tau+chi/pi),
    D(tau,chi)=[C(tau,chi)/C(tau,0)] sin(pi tau)
                 /sqrt(sin(pi tau-chi)sin(pi tau+chi)).        (8)

The marked factorial reflection shows these are precisely the
exponential correction and amplitude ratio of q^(h^2)D_(h,r)/D_(0,r).
In particular B(tau,0)=0,D(tau,0)=1, and D is nonzero. Put

    Psi(u,eta,chi)=[-Lambda(2u)+6Lambda(u)]/pi
       +(1/(2pi))integral_0^(2u)Log(2cosh eta+2cos v)dv
       +B(u/pi,chi).                                         (9)

The whole phase is even in eta and chi. At (eta,chi)=(0,0),
its selected index is u=pi/4 and Psi_uu=-8/pi. The implicit
function theorem gives a unique holomorphic u_*(eta,chi) nearby.
Let j(eta,chi)=Psi(u_*,eta,chi), and

    a(eta,chi)=[sqrt(sin(2u_*))/sin(u_*)^(5/2)]
       exp(iu_*/2)D(u_*/pi,chi)
                         /[4sqrt(pi)sqrt(-Psi_uu(u_*,eta,chi))]. (10)

These are the SAME source-calibrated functions as the old mixed
high-index theorem on its overlap eta>0; now both parameters range
on fixed complex disks about zero. The exact finite packet satisfies

    Z_N^win(-2cosh eta,chi)
       =exp(-i pi d/4) a(eta,chi) exp[Nj(eta,chi)]
                                                    [1+O(1/N)], (11)

uniformly on smaller fixed complex disks. Its amplitude is nonzero.

Proof: (4) supplies an exponentially accurate ORIGINAL-grid
interpolant. Canonical factorials and the half-shift Newton factor
are regular on this window and have the same optimal EM residual
bound. The exact half-grid cotangent rectangle retains every vertical
endpoint and horizontal nonzero-mode current. Its complete real
phase has a fixed endpoint gap; the top/bottom cotangent errors
have exp(-2Nd) while the phase increases O(d^2). Choose contour
height first, then shrink the fixed eta,chi disks. All residuals
are below the selected saddle by a fixed exponential rate. The
two constant cotangent pieces give the same saddle integral with
density N/pi. Analytic Gaussian expansion gives (10)--(11),
including both original parity phases. This is the earlier exact
cotangent proof with the newly justified source across the quarter
point, not continuation of a merely pointwise leading formula.

The rational principal quadratic gives, by differentiating in chi^2,

    j(eta,chi)=j(eta,0)
                     -(1+exp(2iu_*(eta,0)))chi^2/(2pi i)+O(chi^4).

Consequently at the complete spectral point,

    j(eta,chi)=j_0+eta^2/(4pi)
                          +(-1+i)chi^2/(2pi)+O((|eta|+|chi|)^4), (12)

with j_0=v8/pi. Reflection reverses the imaginary color coefficient,
with its own explicit opposite complete-source phase. The real
physical-color curvature is strictly negative. All fixed Casimir
normals follow from the uniform holomorphic c-disk in (11);
this does not assert moving-q normal derivatives of an unspecified
off-root turn family.

These estimates apply to the EXACT packet, not only its leading
expression. Writing theta=s+it, chi=x+iy, and using eta=i theta,
one may shrink the fixed disks so that

    |Z_N^win(-2cos theta,chi)|
      <=poly(N) exp N[j_0-a(s^2+x^2)+C(t^2+y^2)]         (12a)

for some a,C>0. The same holds for the typed reflected packet.
The cross terms from the imaginary quadratic coefficient are
absorbed by a fixed completion of squares; the quartic remainder
is absorbed after shrinking. The uniform relative error in (11)
changes only the prefactor.

There is also a fixed angular gap away from theta=0. On the whole
physical r-window the exact coefficient bound is

    |b_(N,r)(chi)|<=poly(N) [s_(2r)/s_r^6]
                                                   exp(CN|chi|^2).

It follows from (4)--(8) and their even analytic action perturbation.
The old Newton arc-convolution has a strict angular gap uniformly
on this compact r-window about pi/4. Therefore, on the remainder
of the physical theta circle outside any fixed small central arc,
the packet is bounded by poly(N)exp[N(j_0-g+C|chi|^2)]. The gap
persists on a small fixed complex theta strip and chi disk. Cauchy
on radius1/N then controls every fixed derivative with only an
additional polynomial factor. These are bounds for the explicit
finite polynomial (7), suitable before the outer-color transform.

## 4. Actual-source replacement on a full fixed cusp corridor

Use the faithful original Hermite norm

    ||f||_H=max_double(|f(c)|+N^(-2)|f'(c)|),

also including the odd simple value. It is submultiplicative;
||R||_H,||R^(-1)||_H<=9/8, and |phi(f)|<=3N^3||f||_H.
For some fixed delta_0,gamma>0, uniformly for the ACTUAL integers
0<=h<=delta_0 N,

    ||z_(N,h)-Z_N^win(.,pi h/N)||_H
                                <=poly(N)exp[N(j_0-gamma)].  (13)

The proof includes two different retained source errors. First,
the removed r-indices have the original all-index envelope
J_1(u)+E(u)+C chi^2. Its unique maximum at chi=0 is pi/4,
so the complement of I_N has a fixed gap. To obtain a uniform
segment bound without a root singularity, enclose[-2,2] by a fixed
small Bernstein ellipse: its uniform log-integral profile approaches
the unit-radius profile, hence preserves that gap. The factorial
and mixed-Ward bounds are polynomial times this exponential. A
degree<=M complex Markov bound preserves it for the first normals.

Second, the entire original upper band obeys
||RP_(N,h)||_H<=56^h. Shrink delta_0 until delta_0 log56<j_0-gamma.
The finite errors in (13) are not zero; they are bounded before
any exterior closure. This is why the actual even packet can
replace the non-even full mixed source only with its explicit residual.

For any fixed number n of stack pieces and fixed crossing power m,
telescoping products in this faithful norm proves the same type of
exponential replacement bound for the entire original stack, after
an additional fixed shrink of delta_0. It is uniform for every
physical outer color because

    max_(1<=j<=N)||L_j||_H=poly(N),
    ||R^m||_H<= (9/8)^|m|.                              (14)

Indeed |U_(j-1)(c/2)|<=j on[-2,2] and Markov costs at most
N^2/2 per derivative. No positive quotient of the radical or
source-operator commutation beyond the actual full pair algebra
is used.

## 5. A width-free gap for the ENTIRE physical inner-color complement

For every fixed delta>0 with a nonempty physical complement there
is gamma_delta>0 such that

    limsup_N N^(-1)log max_(0<=h<N)||z_(N,h)||_H<=j_0,
    limsup_N N^(-1)log max_(delta N<=h<N)||z_(N,h)||_H
                                                   <=j_0-gamma_delta. (15)

Here h=N-j labels EVERY actual auxiliary color, not just the low
half. For j<=N/2, the entire box is a pure alias, bounded by the
proved uniform rate B_alias=(1/2)log(4+sqrt15)<j_0. For j>N/2,
keep both the low core and that alias. The uniform core upper
rate j_0 follows from the global mixed-source spectral envelope.

Its STRICT complement gap can be made uniform as the enclosing
ellipse shrinks to the unit circle. Specifically choose ONCE
1/4<beta<1/2 and a closed contracting interval
I subset(pi beta,pi/2). Every actual source propagating from the
original terminal wall to r<=beta N crosses I. The exact spectral
ellipse gives a uniform strict factor there for ALL
delta N<=h<=M, including the repeated-root endpoint color. Frozen
finite blocks turn it into a fixed exponential contraction, without
choosing a root or assuming an eigenbasis. This factor is independent
of the spectral radius R of the outer Newton estimate.

For r>beta N, the complete profile J_R+E has a fixed gap from
j_0 uniformly for R sufficiently close to1, since its maximizer
converges to pi/4. Choose that R so small that j(log R)-j_0
is less than one quarter of the fixed contraction/gap budget.
The maximum principle on the segment and complex Markov give
the stated Hermite gap. Thus a vanishing gap in the limit R->1
has NOT been assumed away. The old uniform subexponential frozen-
block cost is absorbed by half the fixed gap. This proves (15),
including every color endpoint and its first normal.

It follows immediately that for every fixed stack width n>=1,
any fixed signed R power, and ANY physical outer color, the full
original mixed scalar has a fixed exponential gap below n j_0
whenever at least one INNER deficit is at least delta N. The
source cost in (14) is polynomial and one factor in (15) loses a
fixed rate; the other fixed n-1 factors cost at most j_0+o(1).
No minimum-width restriction is required: unlike the pretzel
marked-period problem, the stack reference height is n j_0 with
no outer Legendre loss. The separate complement in the OUTER
auxiliary color remains the task of its exact Fourier-Hermite
source transform.

## 6. The complete local input for the original outer-color source

Fix n>=1 and m in Z. For physical inner deficits in the corridor,
let

    F_phys(theta)=R(-2cos theta)^m
                    product_i z_(N,h_i)^(typed i)(-2cos theta),

where each type is z or its literal sharp. Its definition here
means the original full-Hermite polynomial. On a fixed small
central complex theta window take the EXACT finite analytic function

    F_win(theta,chi)=kappa^(m/2) exp[iNm theta^2/(4pi)]
                    product_i Z_N^(win,typed i)(-2cos theta,chi_i), (16)

with kappa^(m/2)=exp[i pi m d^2/(4N)], without a principal-root
reset. This is separately even in theta and every chi_i.

The replacement of R by its displayed Gaussian retains BOTH
the value and first normal at every physical node in this window.
Indeed, for theta_j=(2j-d)pi/N, the exact nodal phase is
R(c_j)=kappa^(1/2)exp[iNtheta_j^2/(4pi)]. At every double node,
the full original source derivative is

    R'(c_j)/R(c_j)=-(d-2j)/[2(q^(2j+1)-q^(-2j-1))],
    partial_theta log R(c_j)=iNtheta_j/(2pi).              (17)

The second identity follows using
q^(2j+1)-q^(-2j-1)=-2i sin theta_j and dc/dtheta=2sin theta.
At the odd simple node only its value is prescribed, as required.
Thus (16) is not an arbitrary spectral extension of the physical
crossing; it matches exactly the jets used in the original closure.

Equations (12a),(13) and submultiplicativity now give, after a fixed
shrink of the inner corridor, a gamma>0 with the following actual
source estimates, uniformly on its physical grid:

* On the central nodes, F_phys-F_win and their first theta
  derivatives are bounded by poly(N)exp[N(nj_0-gamma)].
* Outside any fixed smaller central theta window, F_phys and
  its first theta derivative obey the same exponential-gap bound.

For the second assertion use the uniform angular gap of the finite
packet on the compact r-window, the H-residual(13), and the fact
that the original R^m has unit nodal values and at most a polynomial
first-normal cost. Derivatives of the fixed n-factor product cost
only another polynomial. Thus the ORIGINAL physical spectral
complement, not just the interpolant, is estimated.

On smaller fixed complex theta/color disks, the exact function
(16) has a nonzero analytic asymptotic with phase

    n j_0 -[n-im]theta^2/(4pi)
            +sum_i[-1+i sigma_i]chi_i^2/(2pi)+O_4,
    sigma_i=+1 for z, -1 for z^sharp.                      (18)

The unit kappa and complete source phases remain in its specified
external factor. In particular, for theta=s+it and chi=x+iy,

    |F_win(s+it,x+iy)|
      <=poly(N)exp N[nj_0-a(s^2+||x||^2)
                                      +C(t^2+||y||^2)]   (19)

for some a,C>0 depending on n,m. The real quadratic coefficients
at t=y=0 are n/(4pi) and1/(2pi); imaginary cross terms are
absorbed by completing squares. Shrinking the fixed disks absorbs
the quartic remainder. All fixed derivatives have polynomial
additional cost on still smaller disks. These give the exact
local holomorphic input, original-grid residual and spectral
complement required BEFORE the outer-color Fourier-Hermite
transform; no contour endpoint or alias is set to zero here.

Audit: [actual mixed-circle operators, canonical complex quarter source and original crossing normals](../experiments/audit_actual_belt_stack_auxiliary_color_inner_packet.py).
Fresh replay PASS: seven full physical mixed-circle finite-field
families and seven entire low-color alias families; two canonical
complex-Fhat source families across the quarter point; nine
high-precision literal crossing/first-normal families; and six
all-parity selected complex-source calibrations at N=32,33,64,65,128,129.
The last checks compare the ACTUAL terminating finite U sum with its
endpoint-normalized C exp(NS), not just a formal root. These finite
calibrations supplement the analytic proof of its uniform domains,
exponential interpolation residuals and source gaps.

Independent analytical review by the global critical-path auditor
passed the parameterized source/barrier argument, uniform R->1
strict inner-color gap, and the full-node local/spectral-complement
interface in section6. The physical outer-color transform and
geometric holonomy remain separate as stated.
