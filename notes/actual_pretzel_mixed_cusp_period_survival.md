# Survival of the full original mixed-color pretzel period near completeness

29 October 2026. Proof assembly independently reviewed for source
reconstruction, marked normalizations, analytic interpolation and
contour estimates. The discrete summation proof below uses the exact
finite cotangent contour, retaining every endpoint current. For every fixed
odd s>=5, a fixed open cusp-color corridor has a nonzero selected
asymptotic for the FULL original mixed-color augmented source. The
upper color band, lower inner indices, finite-grid residuals and
original Hermite marked functional are all estimated. This is a
mixed-source theorem; the subsequent coherent filling sum is not
replaced by one of its terms.

## 1. Statement and unchanged source

Let z_(N,h)=rotation(R^(-1)L_(N-h)) be the full physical polynomial
from the two-band source theorem, and put

    A_(s,N)(h_1,...,h_s)=Phi_2(product_i z_(N,h_i)).

All auxiliary colors are actual integers j_i=N-h_i. For each fixed
odd s>=5 there is delta_s>0 such that, uniformly for
0<=h_i<=delta_s N and chi_i=pi h_i/N,

    A_(s,N)(h)=N^(3/2) exp(-i s pi(N-1)/4)
                   A_s(chi) exp[N Phi_s(chi)](1+O(1/N)).     (1)

The functions Phi_s and A_s below are holomorphic on a fixed complex
neighborhood of chi=0, even separately in each chi_i, and A_s has no
zeros there. At the complete point,

    Phi_s(0)=V_s/(2pi), A_s(0)=C_s,

with the SAME V_s,C_s as the complete augmented-period theorem.
Evenness of the amplitude follows from the full low-core coefficients;
its definition by analytic continuation is fixed at the complete
point. The full physical polynomial contains a non-even alias band,
but that band is exponentially smaller in this corridor.

In particular (1) is actual uniform noncancellation on an OPEN
macroscopic corridor h_i<=delta_s N, not only fixed normal jets or
h_i=o(N). The choice s>=5 is used for the independently quantified
alias gap; no assertion for s=3 is inferred from that estimate.

## 2. The analytic high-index phase is attached to the finite source

Use the notation S(tau,chi), C(tau,chi) of the
[mixed inner source theorem](actual_pretzel_mixed_inner_source_wkb.md),
and define the analytic sine primitive

    J_sin(tau)=integral_0^tau Log(2sin(pi t))dt.

On a fixed high-index neighborhood tau>1/4 and small complex chi put

    B(tau,chi)=S(tau,chi)-S(tau,0)
       +2J_sin(tau)-J_sin(tau-chi/pi)-J_sin(tau+chi/pi),

    D(tau,chi)=[C(tau,chi)/C(tau,0)]
       sin(pi tau)/sqrt(sin(pi tau-chi)sin(pi tau+chi)).    (2)

All roots and logarithms continue from their positive real complete
values. These functions are even in chi, B(tau,0)=0, D(tau,0)=1,
and D is nonzero after shrinking the neighborhood.

These expressions follow from the actual coefficient, not a new
semiclassical normalization. Indeed

    q^(h^2)D_(h,r)/D_(0,r)
        =G_N(r)^2/[G_N(r-h)G_N(r+h)],

where G_N is the positive sine-factorial completion. Its bulk
asymptotic has exponential part 2J_sin(tau)-J_sin(tau-chi/pi)
-J_sin(tau+chi/pi) and prefactor
sin(pi tau)/sqrt(sin(pi tau-chi)sin(pi tau+chi)). Multiplying by
the SELECTED inner U_(h,r), including its exponentially accurate
analytic interpolant, gives (2).

For w=-exp(eta), define the analytic phase

    Psi(u,eta,chi)=(-Lambda(2u)+6Lambda(u))/pi
       +(1/(2pi))integral_0^(2u)Log(2cosh eta+2cos v)dv
       +B(u/pi,chi).                                      (3)

The analytic continuation of Lambda on this regular u-neighborhood
is fixed by its real values. At chi=0 this is the already calibrated
complete Newton phase. For real eta near eta_s=2asinh(tan(pi/s)),
its complete critical index is

    u_0(eta)=atan(cosh(eta/2)),
    Psi_uu(u_0,eta,0)<0.

The holomorphic implicit-function theorem therefore specifies a
unique critical u_*(eta,chi) near u_0, and

    j(eta,chi)=Psi(u_*(eta,chi),eta,chi).                    (4)

The local amplitude is explicitly

    a(eta,chi)=1/(4sqrt(pi))
       [sqrt(sin(2u_*))/sin(u_*)^(5/2)] exp(iu_*/2)
       D(u_*/pi,chi)/sqrt(-Psi_uu(u_*,eta,chi)).            (5)

All factors are nonzero near completeness. At chi=0 this reduces
to exp(iu_0/2)/[2((T+2)(T+6))^(1/4)], T=2cosh eta.

## 3. Discrete analytic Laplace lemma, including its actual error barrier

Here is the precise local summation argument used in (4),(5).
Choose a fixed real index window [a,b] about u_0, strictly within
(pi/4,pi/2). Choose its physical endpoints on the grid pi r/N;
their O(1/N) motion does not change any of the fixed gaps below.
The source theorem supplies an analytic interpolation of its inner
packet on a FIXED complex window, with relative grid residual
O(exp(-cN)), uniform in small complex chi. Retain that residual.

The original Newton factor has an analytic interpolation there too.
With

    alpha_+=(N+1)/2-iN eta/(2pi),
    alpha_-=(N+1)/2+iN eta/(2pi),

take

    Bhat_N(r,eta)=q^(-r^2)
       Fhat_N(alpha_++r-1)Fhat_N(alpha_-+r-1)
          /[Fhat_N(alpha_+-1)Fhat_N(alpha_--1)].           (6)

At every integer r this is EXACTLY product_(k<r)
(2cos((2k+1)pi/N)+2cosh eta). All four factorial arguments remain
in regular compact substrips. Their marked bulk expansions give
the integral term in (3), with leading prefactor ONE: the half-step
in alpha_± cancels the two endpoint square-root factors. This
continues uniformly to complex u=pi r/N and eta in fixed smaller
neighborhoods; no extrapolation from real integer values is used.

The remaining original factorial factors use the same Fhat/G_N
completion. Thus the interpolated high-window summand is holomorphic
and equals its explicit nonzero amplitude times exp(N Psi), with a
uniform analytic relative O(1/N) error. On the physical grid it
agrees with the original summand up to the RETAINED exponentially
small inner residual.

Use the following EXACT finite cotangent formula, which avoids any
conditional sum of Poisson endpoint terms. For the integers k<=r<=l
in this window, place its vertical sides at the HALF-grid points
a_N=(k-1/2)pi/N and b_N=(l+1/2)pi/N. Let f_N(u) denote the analytic
interpolated r-summand, with all the prefactors just specified, and
let Gamma be the positively oriented rectangle with these vertical
sides and fixed imaginary heights +/-d. Then

    sum_(r=k)^l f_N(pi r/N)
        =N/(2pi i) integral_Gamma f_N(u)cot(Nu)du.       (3a)

This is the interpolated-grid sum; its retained difference from the
ORIGINAL source grid is bounded separately below. The residue of
cot(Nu) at each enclosed physical point is 1/N, so (3a) has no
endpoint half weights or new lattice multiplicity.

Choose d>0 inside the fixed holomorphic tube. The complete real
phase has a fixed gap at both window endpoints. By continuity, the
full vertical sides stay below Re j by a fixed amount, uniformly
after making d and then the eta,chi neighborhoods sufficiently small.
On those sides cot(N(a_N+it))=-i tanh(Nt), and similarly at b_N,
so its modulus is at most one. Their ENTIRE integrals are therefore
poly(N)exp[N(Re j-gamma)] for some gamma>0. They are retained
currents, not terms assigned value zero.

On the upper and lower horizontal sides, respectively,

    cot(Nu)=-i+O(exp(-2Nd)),
    cot(Nu)=+i+O(exp(-2Nd)).

At the complete real parameters, holomorphic Taylor expansion gives
sup Re Psi(x+/-id)<=j_0+C d^2 for real x in the window: its first
normal derivative is imaginary there. The eta and chi perturbations
change this bound and Re j continuously by O(|eta-eta_s|+|chi|^2).
Choose d first with C d^2<d/4, and then the fixed parameter
neighborhood with this perturbation less than d/4. The horizontal
cotangent remainders consequently have a uniform fixed exponential
gap. This bounds ALL nonzero Fourier modes together, without an
unsupported absolute summation of individual 1/m endpoint terms.
Shrink that neighborhood also so that |Im u_*|<d/2 and Re u_*
stays a fixed positive distance from both vertical sides.

With the counterclockwise orientation, the two constant cotangent
parts give N/(2pi) times the sum of the lower and upper left-to-right
ordinary integrals. Deform EACH ordinary integral inside the analytic
rectangle to the horizontal segment through u_*(eta,chi). The
connecting vertical segments at a_N,b_N have the already proved
endpoint gap. Away from a small central neighborhood, the shifted
segment has the same strict gap by the complete profile and small
parameter continuity. In the center,

    Re Psi<=Re j-c_1|u-u_*|^2.

Thus both ordinary integrals give the SAME saddle integral, with
total coefficient N/pi. Uniform analytic Gaussian expansion gives
exactly (5), with relative O(1/N). No unknown original-cycle
intersection number is assigned.

The total grid-residual contribution is at most
poly(N)exp[N(j_0+C|eta-eta_s|+C|chi|^2-c)], by the source theorem,
where j_0 is the complete action at eta_s. Choose the
fixed eta neighborhood and chi disk so small that this remains
exponentially below Re j.
This is WHY relative O(1/N) accuracy on the real grid alone would
not suffice, and why the exponential interpolation is used here.

## 4. The lower indices and the rest of the circle are genuinely smaller

The full physical real-color bound in the mixed source theorem gives

    |q^(h^2)A_(h,r)/D_(0,r)|
        <=poly(N)exp[N(E(pi r/N)+C chi^2)],               (7)

including r<h. The complete-circle proof showed that the positive
Newton envelope J_R(u)+E(u) has a unique maximum at u_0>pi/4,
with a strict gap on u<=pi/4 and on every complement of a fixed
neighborhood of u_0. Its angular envelope also has a strict gap
away from the negative axis. Both gaps persist for fixed sufficiently
small REAL chi by (7) and continuity. The high-index WKB provides
the same bound on the remaining compact index intervals.

Consequently the box's original low core satisfies, uniformly on
a fixed complex neighborhood of the negative point of the circle,
for the physical REAL chi on its specified integer-color grid,

    c_(N,h)(-exp eta-exp(-eta))
       =exp(-i pi(N-1)/4)a(eta,chi)
                              exp[Nj(eta,chi)](1+O(1/N)), (8)

up to an exponentially smaller retained remainder. On the original
circle outside that neighborhood, the entire low core has a fixed
exponential gap relative to the complete maximum, persisting for
small chi. These assertions use the actual real-grid lower packets;
no off-grid extension of the region r<h is needed.
The leading functions a,j are holomorphic in chi; this statement
does not identify an unexamined off-grid continuation of those
lower physical packets with that holomorphic leading expression.
In (8) eta varies in a fixed complex neighborhood, while chi is a
PHYSICAL REAL color pi h/N. The leading functions and high-index
interpolants are holomorphic in chi; no analytic continuation of the
full low-index physical packet is asserted here.

## 5. The original marked period, followed by the alias estimate

For the product of low cores the exact marked residue is

    (-1)^(N-1) N^2/(2pi i) integral_(|w|=R_s)
      product_i c_(N,h_i)(w+w^(-1))
                w^N(1-w^(-2))/(1+w^N)^2 dw.              (9)

Let eta_*(chi) be the unique nearby solution

    sum_i partial_eta j(eta_*,chi_i)=1.

It exists since the complete derivative of the left side is
s cos(pi/s)/(2pi)>0. Define

    Phi_s(chi)=sum_i j(eta_*,chi_i)-eta_*,

    A_s(chi)=2sinh(eta_*) product_i a(eta_*,chi_i)
          /sqrt(2pi sum_i partial_eta^2 j(eta_*,chi_i)).  (10)

The branch of the square root is fixed at the complete real point.
The same finite complex-contour argument as in section3, now in
eta=log(-w), moves the central arc to eta_*. No pole of (9) is
crossed: Re eta remains strictly positive. The global circle gaps
in section4 control its complement. The real Gaussian integral
along the local vertical direction gives (1) for the low-core
product, with the ORIGINAL sign and N^(3/2) normalization exactly
as in the complete-period proof.

Finally the [uniform original alias source gap](actual_pretzel_mixed_alias_source_gap.md)
proves for odd s>=5, and a sufficiently small fixed corridor,

    |Phi_2(product_i z_(N,h_i)-product_i c_(N,h_i))|
        <=poly(N)exp[N(Phi_s(0)-gamma_s)], gamma_s>0.      (11)

Shrink delta_s until Re Phi_s(chi)>Phi_s(0)-gamma_s/2.
Then (11) is exponentially smaller than the just computed nonzero
core period. This proves (1) for the FULL original source, keeping
every normal derivative and every nonempty alias subset.

## 6. Quantitative curvature and what filling still requires

The leading action is even in each chi_i. Its quadratic term can
be calculated directly from the actual mixed recurrence, without
assuming a topological longitude convention. Normalize by D_(0,r),
put u=pi r/N, Y=exp(2iu), c=cot(u)^2, and write its classical
backward eigenvalues as Y^(-1)v. Then

    v^2-[(c-1)cos(chi)^2-2i sqrt(c)sin(chi)^2]v-c=0.

The selected high-index root is v=-1 at chi=0. Differentiation in
chi^2 gives delta Log(Y^(-1)v)=Y chi^2+O(chi^4).
The actual endpoint factor has zero leading action. Therefore

    j(eta,chi)=j(eta,0)
        -(1+Y_*(eta))chi^2/(2pi i)+O(chi^4).

Envelope differentiation at the outer critical point gives

    Phi_s(chi)=V_s/(2pi)
       -(1+Y_s)/(2pi i) sum_i chi_i^2+O(||chi||^4),
    Y_s=exp(2iu_s), u_s=atan(sec(pi/s)).                  (12)

In particular on the real physical corridor,

    Re Phi_s(chi)=V_s/(2pi)
       -sin(2u_s)/(2pi) sum_i chi_i^2+O(||chi||^4).       (13)

This proves strict quadratic decay away from complete color within
that corridor, as well as a nonzero analytic leading amplitude.

The next operation is still the ENTIRE original filling-color sum.
Its exact Weyl fold and normal-weighted Gaussian kernel must be
combined with (1), and intermediate colors outside this corridor
must be bounded. No independent full-twist factor may be discarded.
The identification of the filled critical action with the marked
geometric volume must also respect the actual meridian/longitude
orientation. A complete augmented-source or mixed-cusp theorem is
not a fixed filled-knot volume theorem.
