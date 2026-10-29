# Long fillings of a general original quantum source

29 October 2026. The Fourier filling mechanism is independent of the
pretzel graph. This theorem isolates its actual analytic inputs and
proves that they propagate to every independently sufficiently long
fixed signed integral filling. The new general geometric theorem then
identifies the resulting rate with the actual filled hyperbolic volume.

This is a CONDITIONAL quantum transfer theorem. It does not assert its
source hypotheses for every diagram, or count them as proved merely
because the diagram has a positive geometric triangulation. Establishing
them for broader original sources is part of the active goal.

## 1. Exact source and hypotheses

Fix a diagram with b specified crossing-circle ports on original
complete target strands. Retain its entire marked closure, all Cartan
factors, and its literature normalization. Let A_N(h_1,...,h_b) be
its ORIGINAL mixed-circle scalar, with auxiliary colors j_i=N-h_i.
The [all-input circle basis](actual_crossing_circle_source_and_filling.md)
gives the exact finite identity

    K_N(p)=chi_N kappa^(-2 sum p_i)
       sum_(j_1,...,j_b=1)^N product_i beta_(j_i-1)^(-p_i)
                                        A_N(N-j_1,...,N-j_b). (1)

This substitutes each actual full twist R^(-2p_i), leaving the base
coupons and retained half twists in A_N. The beta coefficients retain
all confluent Casimir jets. Multilinearity of the original diagram
proves(1), even if adjacent physical operators do not commute. The
independent color-register functionals commute; no physical operator
is moved through another. Keep chi_N explicitly and require its known
normalization to be nonzero with log|chi_N|=o(N).
Here A_N is defined before precisely that recorded outer factor;
chi_N is not included a second time in the mixed scalar. It is not
chosen using the value of the completed unknown invariant.

Assume the following for this fixed source.

**Global source gap.** There is a fixed sufficiently small delta>0,
H=floor(delta N), a real F0 and gamma>0 such that

    max_(some h_i>H) |A_N(h)| <= poly(N) exp[N(F0-gamma)] (2)

over the ENTIRE physical color cube 0<=h_i<=N-1. The estimate includes
ordinary colors, every alias and every marked normal term.

**Exact analytic corridor packet.** There is a finite holomorphic
packet C_N(x), even in each coordinate, on a fixed complex neighborhood
of the box |Re x_i|<=2delta, |Im x_i|<=sigma0, with

    |A_N(h)-eta_N C_N(h/N)|
                    <=poly(N) exp[N(F0-gamma)]           (3)

for 0<=h_i<=H. Here eta_N is an explicit retained unit phase. On that
fixed complex neighborhood,

    C_N(x)=N^mu a(x) exp[N phi(x)](1+O(N^-1)),           (4)

uniformly, where a and phi are holomorphic and separately even,
a(0)!=0, phi(0)=F0, and

    phi''(0)=2pi i diag(tau_1,...,tau_b), Im tau_i>0.     (5)

A known imaginary constant in phi(0) may instead be retained explicitly
as exp[iN Im phi(0)] in eta_N. This only separates its specified unit
phase; it does not change the original state or an unknown growth rate.

The uniform complex statement is essential. A pointwise approximation
on the physical grid is not enough for the Fourier contour estimates.
One may shrink delta, with the global gap(2) required for the chosen
corridor. By(4)--(5), after shrinking the neighborhood,

    |C_N(x+iy)|<=poly(N) exp[N(F0-a0||x||^2+B0||y||^2)] (6)

with a0>0. All constants may depend on the fixed diagram, not on N.

These assumptions concern a specified original source and specified
interpolation, not a choice of solution of its recurrence.

## 2. The source action and theorem

Define the local analytic Fourier transform by

    grad phi(xi(z))+2pi i z=0,
    Psi(z)=phi(xi(z))+2pi i xi(z) dot z,
    B(z)=(2pi)^(b/2) a(xi(z))/sqrt(det[-phi''(xi(z))]).

The implicit-function theorem applies by(5). The Gaussian square root
is the one from the translated original real contour. Both Psi and B
are separately even; B(0)!=0 and

    Psi(z)=F0-i pi sum_i z_i^2/tau_i+O(||z||^4).        (7)

For integer nonzero charges m_i put

    T_m(z)=Psi(z)-2pi i sum_i(p_i z_i^2+m_i z_i).

For all independently sufficiently large fixed signed p_i, let z_*
be the unique nearby critical point of T_1. Then

    K_N(p)=chi_N eta_N kappa^(-sum p_i)
             N^mu D(p) exp[N T_1(z_*)](1+O_p(N^-1)),   (8)

where

    D(p)=2^b (2pi)^(b/2) B(z_*) product_i sinh(2pi i z_*,i)
                                      /sqrt(det[-T_1''(z_*)])

is NONZERO. Consequently

    lim_N (2pi/N)log|K_N(p)|=2pi Re T_1(z_*).           (9)

The slopes and diagram are fixed before N tends to infinity. There
is no slope-comparability, same-sign, prime-level or parity restriction.
The constants and threshold are source dependent.

## 3. Exact filling, including every endpoint and normal term

The full Hermite coefficients obey

    sum_j |beta_j^(-p)|<=2N(1+|p|).

Thus(2)--(3) cost only polynomial multiples of exp[N(F0-gamma)] in
the WHOLE finite sum(1). No non-even alias is folded into C_N.
For its exact even corridor define

    F_N(z)=sum_(|h_i|<=H) C_N(h/N) exp(2pi i h dot z).

The [full-normal Fourier identity](actual_filling_source_fourier_endpoint_gap.md),
sections4--5, is valid for ANY even packet. In each color its sampled
kernel is the derivative of

    exp(-2pi i p N z^2) sinh(2pi i z) F_N(z).

Its values vanish at z=+/-1/2 and its derivatives match at the two
endpoints. Therefore the exact charge representation retains only
m!=0. The complete b-port expression has integrand

    exp[-2pi i N sum_i(p_i z_i^2+m_i z_i)]
                        product_i[m_i sinh(2pi i z_i)] F_N(z),

with the unchanged parity phases and kappa factors. Its infinite
charge series converges with the paired endpoint currents retained.
This identity uses both original normal contributions; a value-only
Fourier kernel would not give the same zero-charge cancellation.

Hypothesis(6) is precisely the source-specific input of the exact
cotangent-contour Fourier estimate. Its proof applies coordinatewise
to C_N: noncentral frequencies, finite color endpoints and fixed
mixed derivatives all have an exponential source gap. The paired
high-charge current has a double zero at the endpoint. Its weighted
bound is a constant times

    poly(N,p) m/(m-|p|)^3 exp[N(F0-g)],

for m>2|p|+2delta+2, and is summable. The imaginary contour width
is fixed by the SOURCE, not divided by the largest slope.

In several coordinates use the exact telescoping difference of the
full color functionals and their finite-charge restrictions, as in
equation(14a) of that note. All spectator chirps stay on their REAL
finite grids or finite real integrals while one tail is removed.
Thus these bounds do not incur exp(N|p_j|) costs from another port.
This is why independently unequal slopes are permitted.

## 4. The central packet and all nonminimal charges

The central Fourier calculation in section6 of the same note uses
only(4)--(6), analytic implicit stationarity and a real Gaussian.
It gives, uniformly on a fixed small complex z-neighborhood,

    F_N(z)=N^(mu+b/2) B(z) exp[N Psi(z)](1+O(N^-1)).   (10)

No separate pointwise error is transformed as if it had an exponential
Fourier gap; the exact finite analytic C_N is used throughout.

The [local charge proof](actual_pretzel_long_filling_charge_selection.md)
also depends only on the stated analytic structure. Here is its
extension when the diagonal cusp parameters tau_i are different.
Put epsilon_i=1/p_i,t_i=m_i/p_i. The saddle equations become

    z_i=-t_i/2+epsilon_i Psi_i(z)/(4pi i).

They have a unique holomorphic solution in one fixed polydisk of
(t,epsilon), with z_i=-t_i/2 at epsilon=0. Completing the square
isolates a purely imaginary term on real t,epsilon:

    T_m(z_m)=(pi i/2)sum_i t_i^2/epsilon_i+Bhat(t^2,epsilon).

The remainder is analytic and even in every t_i. If
b_i=pi Im(tau_i)/|tau_i|^2>0, then

    partial_(t_i^2) Re Bhat(0,0)=-b_i/4.

Shrink one fixed polydisk so each derivative is <=-b_i/8. Integrating
these inequalities along the squared coordinates gives

    Re T_m(z_m)<=Re T_1(z_*)
                        -sum_i (b_i/8)(m_i^2-1)/p_i^2. (11)

Thus only |m_i|=1 can be leading among local nonzero charges.
Every component z_i is nonzero for m_i!=0: separate evenness writes
Psi_i=z_i Q_i(z_1^2,...,z_b^2), and the saddle equation solves
z_i=-t_i/[2(1-epsilon_i Q_i/(4pi i))]. The sinh factors in(8)
therefore do not vanish. The real part of the translated-contour
Hessian remains strictly negative, so its Gaussian determinant is
nonzero for signed as well as positive slopes.

The finite nonlocal charges are treated by the same source estimate:
outside |z_i|<=t0/4 the real source has a fixed Fourier gap; inside,
|m_i+2p_i z_i|>=|p_i|t0/2 for a charge with |m_i/p_i|>=t0. A fixed
imaginary shift in that coordinate decreases its filling phase,
including the endpoint connectors. The gap is independent of the
largest other slope. Local connector bounds use
|Im z_i|<=C|p_i|^-1 |m_i/p_i|, which follows from the same separately
even factorization. These are the arguments of sections4--5 of the
[corridor proof](actual_pretzel_cusp_corridor_filling_survival.md);
they do not use a common value of tau_i or a cyclic diagram.

The 2^b minimal signed charges have identical complex action. Under
(m_i,z_i)->(-m_i,-z_i), m_i sinh(2pi i z_i) is unchanged; the
exact parity characters are unchanged as well. They ADD. Gaussian
integration of(10) supplies N^(-b/2), giving(8). Finally
Re T_1(z_*) tends uniformly to F0 as max_i|1/p_i| tends to zero,
so the threshold can absorb the fixed global/error gaps(2)--(3).
This proves the full-source, not only corridor, theorem.

## 5. When the rate is the ACTUAL hyperbolic volume

Add the following independent geometric certificates for the SAME
source. The base diagram is a fixed complete finite-volume cusped
hyperbolic manifold Y. The analytic critical packet has an actual
bounded framed representation family rho_x near the oriented complete
holonomy, with the remaining components parabolic. Its original
peripheral marking and absolute source action satisfy

    G=2pi i phi(x)+recorded real constant,
    z_i=2pi i x_i, ell_i=partial_(z_i)G=phi_i(x),
    U_i=-z_i, V_i=-2ell_i,

with the literal spin kept when converting to these centered
projective logs. Require the actual regulator comparison and the
absolute anchor ImG(0)=Vol(Y), rather than merely a matching Hessian.

The Fourier and filling stationarity equations then give EXACTLY

    ell_i=-2pi i z_*,i,
    U_i+p_i V_i=-2pi i,
    2pi Re T_1(z_*)=Vol(rho_p).

The [general geometric completion theorem](general_source_regulator_hyperbolic_equality.md)
applies to this actual nearby framed representation. It gives a
complete smooth hyperbolic metric on the correctly marked filled
topology and hence

    lim_N (2pi/N)log|K_N(p)|=Vol(Y(p)).                 (12)

That theorem handles arbitrary bases and primitive slopes. The quantum
transfer proved HERE concerns the integral full-twist kernel(1);
arbitrary rational quantum surgery kernels would need their own exact
source and endpoint proof. No rational-filling quantum statement is
silently added by the more general geometric theorem.

## 6. Current proved applications and active generalization task

The established long-pretzel family supplies every hypothesis by explicit
source and port proofs. The improved width estimate is being audited
separately. For a general augmented diagram, identity(1) is already
available, but the complete complex packet(3)--(5), its global gap(2),
and its actual marked representation anchor must still be established.
The theorem propagates those base certificates to all long fillings;
it does not manufacture them from the A-polynomial or geometry alone.

The active goal of the most general original-invariant equality remains
open beyond the source classes where those hypotheses are proved.

The [signed octahedral belt-stack assembly](actual_long_filled_octahedral_belt_stack_volume.md)
now supplies all these hypotheses for another class, at every fixed
nonempty stack width and fixed outer crossing power. Its literal inner
color continuation, squared outer Fourier kernel, global source gaps,
typed peripheral lift and complete face anchor give full equality for
independently long signed integral fillings of ANY subset of auxiliary
circles. Unfilled colors remain at h=0; they are not assigned p=0.
This application does not turn the present conditional theorem into
an unconditional statement for arbitrary graph sources.

## 7. Independent proof audit

An independent read checked the exact N powers, the Cartan kernel
factor, the all-unit parity cancellation, and the unequal-cusp charge
estimate. It also checked the coordinate conversion
dG=ell dz=(1/2)VdU and 2pi i T=G+sum p_i ell_i^2 up to its recorded
REAL constant. The general theorem retains its base-source hypotheses;
the audit does not establish them for a new diagram. The improved
pretzel source proof currently verifies them for fixed odd s>=9.

The [robust Conway filling theorem](actual_conway_long_filling_source_limit.md) now supplies every quantum hypothesis and the [actual marked peripheral branch](actual_conway_marked_peripheral_deformation.md) for all retained cylindrical robust factors. Arbitrary finite branching and turns are allowed; any subset of auxiliary circles may be filled along independently sufficiently long fixed signed integral slopes. Its complete mixed-color gap and uniform complex packet are proved separately. These pure full-twist fillings remain links with at least 2S+1 main components for S seeds, so this application is not a new knot-family claim.
