# The actual magnetic-energy profile and the full Steinberg cost

30 October 2026. An exact finite Fourier
identity reduces the native magnetic energy to its actual center
coefficient, within polynomial factors. The selected q-Hahn action
therefore gives its rate without taking the absolute values of a
coherent source sum. At the folded channel the degree profile is
strictly increasing. The FULL odd Steinberg projector and the even
maximal completed pair both have rate 5 v3/pi, larger than the
highest-weight block example v8/(2pi).

Here v3 is the volume of a regular ideal tetrahedron. The result is
an operator boundary cost. It does not assert a volume identity for
the original marked network or replace shared magnetic sums by
independent local maxima.

## 1. Exact Fourier reduction, including the unused nodes

Use q=exp(pi i/N), Q=q^2, d=N-1 and an actual complete channel

    0<=j<=floor(d/2), d-j<=t<=d.

Let fhat(u) be the literal terminating continuation of the original
normalized column C_j(t,u). The
[magnetic polynomial theorem](actual_q_hahn_magnetic_complex_corridor.md)
proves, with x=q^d, h=d-t and n=t+j-d,

    fhat(u)=x^u Q^(-ju) G_t(Q^u),
    G_t(q^t z)=c_t P_t(z),
    c_t=q^(jn)/(Q;Q)_j,
    P_t(z)=B_h(z) A_n(z)=sum_(k=0)^j p_k z^k.       (1)

Every p_k is strictly positive. This is the proved sine-coefficient
recurrence for A_n and the positive sine-binomial coefficients of
B_h, not positivity of the original oscillatory magnetic column.
Also G_t(Q^u)=0 for every unused physical node t<u<=d.

Since deg G_t=j<N, discrete Fourier orthogonality gives EXACTLY

    sum_(u=0)^t |C_j(t,u)|^2
      =sum_(u=0)^d |G_t(Q^u)|^2
      =N/s_j^2 sum_(k=0)^j p_k^2,                  (2)
    |fhat(t/2)|^2=(sum_k p_k)^2/s_j^2.

All prefactors in the first line of (1) have modulus one at real
u, including the possibly half-integral center. Thus no physical
parity or source phase is changed in (2). The vanished nodes are
essential: the whole Fourier sum is equal to the actual physical
column norm, rather than a norm on a larger invented support.

Cauchy's inequality and positivity now imply

    N/(j+1)|fhat(t/2)|^2 <= ||C_j(t,.)||_2^2
                              <=N|fhat(t/2)|^2.    (3)

This is both an upper and a lower estimate, uniform at ALL physical
degrees in the complete range. It leaves the actual cancellation
already present in the center coefficient untouched.

## 2. The explicit complete-channel energy profile

Let J(y)=integral_0^y log(2sin(pi z))dz for 0<=y<=1, and let
Phi_xi(tau,nu) be the ACTUAL selected action proved in the
[full physical packet](actual_q_hahn_full_physical_complex_packet.md).
For 0<xi<=1/2 and 1-xi<=tau<1 put

    e(tau,xi)=2 Re Phi_xi(tau,tau/2)
                 -J(tau-xi)-J(tau+xi-1)+2J(tau).    (4)

This formula is uniform near xi=1/2. It applies to both double
channels and the odd simple midpoint. More precisely, use the
actual ratios xi_N=j/N and tau_N=(t+1)/N, so that the complete
condition is exactly tau_N+xi_N>=1. On fixed real compacts with
1/2<tau_N<1 and xi_N bounded away from zero,

    log E_(t,j)=N e(tau_N,xi_N)+O(log N),           (5)

where E is the exact CD-normalized magnetic energy of the
[native projector theorem](actual_matching_edge_native_projector_energy.md).
The O(log N) is uniform, including the bottom complete degree.

Indeed (3) changes the logarithm of the norm from that of its
center by only O(log N). The original nonzero packet gives
log|fhat(t/2)|=N Re Phi_(j/N)(t/N,t/(2N))+O(log N).
Moving both scaled arguments by O(1/N) to the ratios in (5) costs
O(1) on these compacts. The exact double CD measure is

    |sigma_(t,j)|=N s_(t-j)s_(t+j-d)/(s_t^2 a_j^2),
    a_j=|1-Q^(2j+1)|.

Its log divided by N equals the three J terms subtracted in (4),
to error O(log N/N). Nonzero a_j is at least a constant/N, so
even the almost-folded double channels cost only O(log N).
At the simple midpoint its exact measure N s_(t-j)^2/s_t^2
has the SAME limiting profile. Uniform factorial endpoint estimates
include s_0=1. The shifted tau_N avoids assigning J a negative
argument at t=d-j.

The rate in (4) also has an elementary derivative. Set

    c=-cos(pi tau), C=cos(pi xi), s=sin(pi xi),
    k=sqrt(1+2c+C^2).

In the strict complete interior c>C>=0,

    partial_tau e
      =2 log{ [s sqrt(1+c)+sqrt((1-c)(1+2c+C^2))]
                                         /sqrt(2(c^2-C^2)) }>0.  (6)

For a direct derivation, the actual selected magnetic multiplier at
the real center is Y=(s+i k)^2/[2(1+c)]. It has modulus one and
argument in (0,pi). The original second finite-shift equation gives

    exp(Phi_tau)=(exp(pi i tau)-Y^-1)/(1+exp(pi i tau)).

Taking its modulus gives
[s tan(pi tau/2)+k]/sqrt(2(1+c)). The real derivative along the
center is Re Phi_tau because Re Phi_nu=0. Meanwhile the derivative
of the CD action is log[(c^2-C^2)/(1-c^2)]. Combining these two
identities proves (6). Its sign is exact: the square of the FIRST
numerator term minus the denominator squared is
(1-c)(1+2c+C^2)>0. It follows that the entire displayed numerator
is strictly larger than its denominator.

Thus the complete-channel rate is strictly increasing in physical
degree. For a nonfolded PAIR, the unpaired degrees j<=t<d-j are
not covered by this assertion; no full paired-operator maximum is
deduced from (6) alone.

## 3. A finite folded determinant controls ALL physical degrees

Now let N=2m+1 be odd and j=m. The full Steinberg projector is
simple. By the exact high-degree adapter, it suffices to consider
m<=t<=d=2m. Write

    c_t=-cos(pi(t+1)/N),
    R_m(z;c)=det(z I+c D_m+K_m),                   (7)

where D_m is the already proved real positive matrix and K_m is
real skew-symmetric. Here c_t ranges from sin(pi/(2N)) to 1.
The exact source scalar and CD measure give

    |fhat(t/2)|^2/|sigma_(t,m)|=R_m(1;c_t)^2/N.

Indeed beta(2m,m)=1, the sine denominator of the center column is
s_t/s_(t-m), and |sigma|=N s_(t-m)^2/s_t^2. Therefore (3) becomes

    R_m(1;c_t)^2/(m+1) <= E_(t,m) <= R_m(1;c_t)^2. (8)

The determinant is positive and strictly increasing for real c>=0.
To verify this directly, conjugate I+cD_m+K_m by D_m^-1/2. Its
symmetric part is D_m^-1+cI>0, so its inverse has positive definite
symmetric part. Consequently

    partial_c log R_m(1;c)
      =tr[(I+cD_m+K_m)^-1 D_m]>0.                  (9)

This proves finite bounds on the ENTIRE physical operator:

    R_m(1;1)^2/(m+1) <= ||Pi_St||op <= R_m(1;1)^2,
    ||Pi_St||op <= ||Pi_St||HS <= sqrt(N)||Pi_St||op. (10)

Every physical degree is retained. These bounds do not claim that
the exact finite maximum of E_(t,m) is always at t=d; they prove
that its exponential rate is determined there.

There is no unproved endpoint continuity hidden here. For c>=0 put
S=I+cD_m. The symmetric part of (S+K_m)^-1 is bounded above by
S^-1: conjugate by S^-1/2 and use
Re(I+A)^-1=(I-A^2)^-1<=I for real skew A. Integrating the trace
inequality yields

    0<=log R_m(1;c)-log R_m(1;0)
                                      <=log det(I+cD_m).          (11)

Hadamard and the explicit diagonal
(D_m)_(n,n)=1/[cos(n pi/N)cos((n+1)pi/N)] give

    log det(I+cD_m)
       <=sum_(r=1)^m log(1+C c N^2/r^2)
       <=C N sqrt(c).                              (12)

The last step bounds the decreasing sum by its integral on
(0,infinity). Thus the actual lowest c_t=O(1/N) and c=0 differ
by o(N) in log determinant. Near c=1 the simpler bound
partial_c log R_m<=m/c gives uniform continuity after division by
N. Together with the interior packet, (8),(11),(12) extend the
folded profile continuously to BOTH degree endpoints. At its lower
endpoint the native highest-column calculation gives

    e(1/2,1/2)=v8/(2pi).

## 4. The endpoint is an actual cubic Fourier sum

The upper endpoint can be evaluated without applying an interior
amplitude theorem on the boundary. At t=d,u=j=m the ORIGINAL
terminating sum is, up to its displayed unit phase,

    P_N(w_N)=sum_(a=0)^m beta(m,a)^3 w_N^a,
    w_N=q^m -> i,
    C_m(d,m)=exp(pi i m)q^[-(m+1)m] P_N(w_N).       (13)

The denominator beta(d,m) is exactly one. The
[negative-root theorem](actual_q_hahn_negative_root_source_polynomial.md)
applies to THIS physical polynomial and proves that every zero
is negative real. Its positive-real asymptotic is therefore
continued to i by the actual root-product normal-family argument.
For completeness, uniform factorial estimates give the real
Laplace phase

    E(alpha)=-3[J(alpha)+J(1/2-alpha)], 0<=alpha<=1/2.

For every w>0, E(alpha)+alpha log w has one strict interior maximum:
E'=3 log cot(pi alpha), E''<0. The selected saddle is explicitly

    alpha(w)=pi^-1 arctan(w^(1/3)).                 (14)

Use the positive cube root at w>0 and its continuation on the slit
plane C\(-infinity,0]. Its argument stays in (-pi/3,pi/3), so
arctan and the J terms continue holomorphically without reaching
their singularities. The root-product bound
|Log((w+rho)/(1+rho))|<=C_K, rho>0, on each slit-plane compact
and the positive-real Laplace limit identify the WHOLE actual
normalized logarithm with this continued saddle action. This
argument includes the moving arguments w_N and does not use a
triangle bound for (13).

At w=i,

    alpha=1/4+i log(3)/(4pi), z=exp(2pi i alpha)=i/sqrt(3).

Let eta=Im alpha. The real source rate is

    S=Re[E(alpha)+alpha log i]
      =-6 Re J(alpha)-(pi/2)eta
      =3 Im Li2(z)/pi+log(3)/4
      =3 D(z)/pi.                                  (15)

Here D(z)=Im Li2(z)+Arg(1-z)log|z| is the ideal tetrahedron volume.
To check every constant, the analytic primitive on the sine strip is

    J(a)=i pi(a-a^2)/2+i[Li2(exp(2pi i a))-pi^2/6]/(2pi).

At the displayed alpha it gives
Re J(alpha)=-pi eta/4-Im Li2(z)/(2pi). Also
Arg(1-z)=-pi/6 and log|z|=-log(3)/2. These prove (15).

The ideal shape z has angles pi/2,pi/6,pi/3. Thus
D(z)=Lambda(pi/6)+Lambda(pi/3), with Lambda(pi/2)=0.
The elementary duplication identity for the integral Lambda gives
Lambda(pi/6)=(3/2)Lambda(pi/3), and v3=3Lambda(pi/3).
Consequently D(z)=5v3/6, so the EXACT endpoint energy rate is

    2S=5v3/pi.                                     (16)

Since R_m(1;1)=sqrt(N)|C_m(d,m)|, equations (10),(13)--(16) prove

    lim_(odd N) N^-1 log ||Pi_St||op
      =lim_(odd N) N^-1 log ||Pi_St||HS=5v3/pi.       (17)

In the volume convention 2pi times a rate, this boundary cost is
10v3. It is strictly larger than the v8 cost in the highest-weight
block, which has the LOWEST physical degree t=j.

## 5. What is retained for the general source

The folded profile can be recorded without an implicit saddle:

    e(tau,1/2)=5v3/pi
       -integral_tau^1 2log{[sqrt(1+c)
                 +sqrt((1-c)(1+2c))]/(sqrt(2)c)} ds,
    c=-cos(pi s).                                   (18)

It is continuous on [1/2,1], strictly increasing in its interior,
and has the two endpoint values proved above. The fixed-jet native
theorem adds only polynomial factors to these energies.

Equations (2)--(5) retain an explicit magnetic degree and the exact
CD measure. The full operator norm takes a maximum over that ONE
degree. In an original diagram those degrees and magnetic variables
are shared by adjacent coupons, and the phases in (1),(13) remain
in their signed contractions. Nothing here authorizes multiplying
independently maximized local boundary costs, discarding those
phases, or identifying the energy optimum with a marked geometric
critical point. Those are distinct global requirements.

Audit: [actual Fourier energy and folded endpoint](../experiments/audit_actual_matching_edge_magnetic_energy_profile.py).

## 6. The even maximal pair has the same full rate

Let N=2h>=4, j=h-1, l=h. Use the ACTUAL completed Q_j,M_j of the
native-energy theorem, rather than treating the two root channels
as separate simple projectors. The complete degrees are h<=t<=d.
Their exact normalization is

    |fhat(t/2)|^2/|sigma_(t,j)|
       =(8/N) sin(pi(t-j)/N) R_j(1;c_t)^2.           (19)

For verification, a_j=2sin(pi/N), a_j s_(2j)=N and s_j^2=N/2.
Substituting these identities into the center column and the DOUBLE
CD measure leaves (19), because
s_(t-j)/s_(t+j-d)=2sin(pi(t-j)/N). This retains the paired source
normal and its measure.

By (3),(9),

    8 R_j(1;1)^2/(j+1) <= max_(h<=t<=d) E_(t,j)
                                      <=8 R_j(1;1)^2.             (20)

The lower bound uses t=d, where the sine in (19) is exactly one;
the upper bound uses that sine<=1 and c_t<=1. There is just ONE
incomplete low degree, t=j, with its reflected high copy. Its
normalized highest column has |f_u|=beta(j,u) and
|sigma|=1/sin(pi/N), so its energy has the smaller rate v8/(2pi).

At t=d the center d/2 is half-integral. Use the original physical
sample u=j, only half a step away. The endpoint polynomial is

    P_N(w_N)=sum_(a=0)^j beta(j,a)^2 beta(j+1,j-a) w_N^a,
    w_N=q^j -> i.                                  (21)

Again beta(d,j)=1 and the external source factor has modulus one.
Its coefficients differ from the cubic coefficients by the EXACT
positive ratio

    beta(j+1,j-a)/beta(j,a)=1/sin(pi(a+1)/N),

which is between one and O(N). Thus its uniform real Laplace
profile is the same E(alpha) as in section 4. Its actual negative
roots then select the same complex action at i; this does not
deduce the complex rate by comparing positive coefficients alone.

The center/sample comparison is also exact up to a controlled unit.
At t=d the positive polynomial P_t in (1) has all roots negative
real. Each factor with root -rho satisfies

    cos(pi/(2N)) <= |exp(-pi i/N)+rho|/(1+rho) <=1.

Multiplying its j factors, with the physical prefactors of (1), gives

    cos(pi/(2N))^j <= |C_j(d,j)|/|fhat(d/2)| <=1.    (22)

The center determinant scalar in (19) is polynomial in N, so
(21),(22) prove N^-1 log R_j(1;1)^2 ->5v3/pi at even levels too.

Finally, M_j has exact rank-one norm E_(t,j) on the complete blocks
and is zero on the incomplete block. The native-energy theorem
also places ||Q_j|| between constant times the complete energy and
a polynomial times the full energy, retaining the incomplete block.
Equations (20)--(22) therefore prove

    lim_(even N) N^-1 log ||M_j||op
      =lim_(even N) N^-1 log ||Q_j||op=5v3/pi,        (23)

with the same limits for Hilbert--Schmidt norms. Every fixed
generic-q jet of these operators has upper exponential rate at
most 5v3/pi by the already proved native bounds. No equality is
asserted for a derivative that might vanish or cancel.

This proves a common FULL folded boundary cost at both parities,
using the simple odd projector and the actual even Hermite pair
in their respective source roles.

Primary-agent analytical review: PASS, including the exact physical
Parseval reduction, source-shift/CD derivative and its strict sign,
finite determinant bounds, skew-inverse comparison and endpoint
control, actual cubic endpoint and its selected dilogarithm constant,
and the even measure, half-step comparison and completed Q/M norms.
The review retains the one-operator boundary-cost scope and does not
infer a whole-network positive pairing, gluing identity or volume limit.

Independent full analytical and targeted even-parity review: PASS.
The reviewer independently derived the exact Fourier support and
normalization, degree profile, determinant endpoint bounds, cubic
source phase and selected 5v3/pi constant, even paired measure and
half-step comparison, and full Q/M norm implications. A fresh
100-digit replay passed 1,848 original physical values, 336 unused
nodes, 189 Parseval/center identities, 35 odd determinant brackets,
seven odd cubic endpoints, 27 even center normalizations, six even
endpoint/half-step comparisons and four source-gradient checks.
The displayed sequences reach levels 256/257; the written proof,
not those sequences, supplies the limits and uniform estimates.
