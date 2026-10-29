# Coherent circle control and the full original augmented pretzel period

29 October 2026. The analytic proof and its full two-branch recurrence
estimate have passed independent proof audits. The statement
below concerns the COMPLETE augmented pretzel source, with every
crossing-circle color equal to N and every retained half twist equal
to the original R^(-1). It is a link-source theorem at arbitrary fixed
odd box count s, not a theorem for its fixed Dehn fillings or for an
arbitrary alternating knot.

## 1. Statement, including the original phase and leading constant

Use the [literal complete-base polynomial](actual_pretzel_complete_base_casimir_polynomial.md)
z_N and the unchanged marked functional Phi_2. For each fixed odd
s>=3 put

    alpha=pi/s, eta=2 asinh(tan alpha), R=exp(eta),
    T=R+R^(-1)=4 sec(alpha)^2-2,
    u_*=atan(sec alpha), d=N-1,

    V_s=8s[Lambda(pi/4+alpha/2)+Lambda(pi/4-alpha/2)],

    C_s=(R-R^(-1)) exp(i s u_*/2)
          /[sqrt(s cos alpha) 2^s ((T+2)(T+6))^(s/4)].

Here Lambda(t)=-integral_0^t log|2 sin v|dv. The asserted full-source
asymptotic is

    A_(s,N)=Phi_2(z_N^s)
      =N^(3/2) exp(-i s pi(N-1)/4) C_s
             exp[N V_s/(2pi)] (1+o(1)).                    (1)

In particular C_s is nonzero. The formula treats both parities of N
with their actual original Cartan factors, and includes all repeated
Casimir nodes and normal derivatives through Phi_2. Any external
normalization must still be applied explicitly; no unexamined factor
is declared harmless. The
[explicit face-gluing and tetrahedron calculation](actual_augmented_pretzel_geometric_volume.md)
identifies V_s with the complete augmented link volume. This assertion
concerns the specified RAW marked source A_(s,N); an external chi_N
is not implicitly set to one or assigned a growth rate.

The [complete-point normalization proof](actual_complete_augmented_source_normalization.md)
now checks that the ORIGINAL reduced Kashaev link evaluation has
|<L_s>_N|=|A_(s,N)|. Its framing and component-dependent enhancement
characters have modulus one. Thus (1) proves the actual link statement

    lim_(N->infinity) (2pi/N)log|<L_s>_N|
                       =Vol(S^3 minus L_s)=V_s.           (1a)

The full one-cut modified ADO convention instead multiplies the
reduced value by i^(N+3)/N at completeness. That changes the leading
N-power from N^(3/2) to N^(1/2), and preserves (1a)'s exponential rate.

## 2. The coherent Newton coefficients and the permitted envelope

Write q=exp(pi i/N), Q=q^2, M=floor((N-1)/2), F_a=(Q;Q)_a,
s_a=|F_a|, and c_a=2cos((2a+1)pi/N). Set

    B_r(w)=product_(a=0)^(r-1)(c_a-w-w^(-1)),
    A_r=sum_(v=r)^M Q^(-vr)F_(2v)/(F_v^3 F_(v-r)),
    D_r=Q^(-r^2)F_(2r)/F_r^3, U_r=A_r/D_r.

The finite source identity is exactly

    z_N(w+w^(-1))
      =N^2 sum_(r=0)^M b_(N,r) B_r(w),
    b_(N,r)=kappa^(-1)(-1)^r q^(2r^2+r) A_r/F_r^3.
                                                               (2)

Consequently |b_(N,r)|=(s_(2r)/s_r^6)|U_r|. The
[coherent finite inner transformation](actual_pretzel_coherent_inner_gauss_elimination.md)
proves |U_r|<=2N for r>=ceil(N/4), and, uniformly on compact
subintervals of 0<u=pi r/N<pi/2 lying above pi/4,

    b_(N,r)=exp(-i pi d/4) (s_(2r)/s_r^6)
                sqrt(sin u) exp(iu/2) [1+O(1/N)].           (3)

The error is complex, uniform, and relative to the nonzero displayed
amplitude. This formula is the same for BOTH parities. It follows
from the exact half-shift phases before taking their asymptotics.

The [all-index backward estimate](actual_pretzel_all_index_backward_envelope.md)
retains the entire lower range and gives constants C,B independent
of r,N such that

    |U_r|<=C N^B exp[N E(pi r/N)],
    E(u)=(2/pi) integral_u^(pi/4) log(cot v)dv, 0<=u<pi/4,
    E(u)=0,                                      pi/4<=u<=pi/2.
                                                               (4)

This estimate expressly ALLOWS the second recurrence branch to grow.
No assertion that |U_r| is polynomial below N/4 is needed.

## 3. A uniform circle estimate for each original Newton factor

Fix R>1 and write w=-R exp(i theta), rho=R^(-1),
g(t)=log|1-rho exp(it)|, eta=log R. The exact factorization gives

    log|B_r(w)|=r eta
       +sum_(a<r)[g(pi+theta+(2a+1)pi/N)
                   +g(pi+theta-(2a+1)pi/N)].              (5)

This is a midpoint sum on the symmetric arc [-2u,2u], u=pi r/N.
Its difference from N/(2pi) times the integral is O_R(1), uniformly
in r,N,theta. Indeed the total variation of g on one circle is
2log((R+1)/(R-1)); on each cell the midpoint error is at most half
the variation on that cell.

For any 0<=a<=pi, the function

    I_a(theta)=integral_(-a)^a g(theta+t)dt

has its maximum at theta=pi: its derivative is g(theta+a)-g(theta-a),
which is nonnegative on [0,pi], since
cos(theta+a)-cos(theta-a)=-2sin(theta)sin(a)<=0 and g decreases
as a function of cos. For 0<a<pi the maximum is unique modulo2pi.
It follows in particular that

    max_(|w|=R)|B_r(w)|
        <=((R+1)/(R-1))^2 B_r(-R).                       (6)

The right side is positive because every c_a>-2 and R+R^(-1)>2.
This is a bound for the ORIGINAL finite Newton factor; no positivity
of its monomial coefficients or unproved root-location assertion is
used.

## 4. The second-branch envelope stays below the geometric maximum

Uniform sine-factorial summation, including the endpoints, gives

    log s_k=-(N/pi)Lambda(pi k/N)+O(log N), 0<=k<N.

Equations (2),(4),(5) therefore bound each term by a fixed polynomial
in N times exp[N(H_R(u,theta)+E(u))], where

    H_R(u,theta)=(-Lambda(2u)+6Lambda(u))/pi+u eta/pi
         +(1/(2pi)) integral_(-2u)^(2u)g(pi+theta+t)dt.

At theta=0 put J_R(u)=H_R(u,0). Equivalently, with T=R+R^(-1),

    J_R(u)=(-Lambda(2u)+6Lambda(u))/pi
           +(1/(2pi)) integral_0^(2u)log(T+2cos v)dv.     (7)

It has the derivative

    J_R'(u)=(1/pi)log[(T+2cos(2u))cos(u)^2/(4sin(u)^4)].

In t=tan u its zero is

    4t^4-(T-2)t^2-(T+2)=0,
    tan(u_*)^2=(T+2)/4.

The other algebraic root is -1. Thus J_R has a unique strict global
maximum at u_* in (pi/4,pi/2). In the entire lower range,

    (J_R+E)'(u)
       =(1/pi)log[(T+2cos(2u))/(4sin(u)^2)]>0,
                                      0<u<pi/4.          (8)

Hence max_(u<=pi/4)(J_R+E)=J_R(pi/4)<J_R(u_*). This is the
essential quantitative comparison: the allowed growth from switching
recurrence branches never reaches the geometric maximum of the
OUTER original sum. The exact diagonal/interior equality in the old
two-variable presentation is handled coherently by (2), not ignored.

It follows that, with j(eta)=J_(exp eta)(u_*(eta)),

    limsup_N (1/N)log max_(|w|=R)|z_N(w+w^(-1))|<=j(eta).
                                                               (9)

There is also a stronger local bound needed for the full period.
For some c,epsilon,delta>0 and finite B,C depending only on R,

    |z_N(-R exp(i theta)-R^(-1)exp(-i theta))|
       <=C exp[Nj(eta)]
            [exp(-cN theta^2)+N^B exp(-delta N)],
                                  |theta|<=epsilon,       (10)

and the same expression with only C N^B exp[N(j-delta)] holds on
epsilon<=|theta|<=pi. To prove it, first use (8) and compactness to
remove the lower range and all u outside a small neighborhood of
u_*. At that maximum the real mixed derivative H_(u theta) vanishes,
while

    H_(uu)=J_R''(u_*)=-(T+6)^2/[pi(T+2)^(3/2)]<0,
    H_(theta theta)=-sin(2u_*)/[pi(T+2cos(2u_*))]<0.

Thus H<=j-c[(u-u_*)^2+theta^2] locally. On this compact u range,
(3) and the uniform sine-product expansion give a summand prefactor
O(N^(-5/2)); the outside factor N^2 and the discrete Gaussian sum
O(sqrt N) give O(1). This proves (10). Away from theta=0, the
strict arc inequality in section3 supplies the missing global gap;
u=0 and u=pi/2 are already below j by section4.

## 5. A nonzero central Gaussian from the actual finite sum

For complex zeta near real eta>0 define

    Psi(u,zeta)=(-Lambda(2u)+6Lambda(u))/pi
           +(1/(2pi)) integral_0^(2u)
                   Log(2cosh zeta+2cos v)dv.             (11)

The logarithm is analytic in a fixed neighborhood, since its argument
is positive at real eta. In a compact neighborhood of u_*,

    s_(2r)/s_r^6
       =(2N)^(-5/2) sqrt(sin(2u))/sin(u)^3
           exp[N(-Lambda(2u)+6Lambda(u))/pi][1+O(1/N)],

and the midpoint expansion of B_r has leading prefactor one. These
follow respectively by factoring sin(pi k/N)/(pi k/N) before ordinary
Euler--Maclaurin, and by the smooth midpoint rule. Both are uniform
in the neighborhoods in use.

Insert (3) and set zeta=eta+i t/sqrt N,
u=u_*+x/sqrt N. Taylor's formula in the REAL index x gives

    N Psi=N j+i sqrt N Psi_eta t
          +(1/2)Psi_uu x^2+i Psi_(u eta)xt
          -(1/2)Psi_(eta eta)t^2+o(1).                   (12)

For bounded x,t this is uniform. The Gaussian bound (10), together
with its index-level proof, justifies summing (12) by dominated
Riemann sums and removing the remaining x tails. The resulting
Fourier transform of a real Gaussian has coefficient

    j''(eta)=Psi_(eta eta)-Psi_(u eta)^2/Psi_uu>0.

No contour deformation of the r sum or assertion about an unknown
cycle is being made. The exact finite-sum asymptotic is, uniformly
for bounded real t,

    z_N(-exp(eta+i t/sqrt N)-exp(-eta-i t/sqrt N))
      =exp(-i pi d/4) a(eta) exp[Nj(eta)]
           exp[i sqrt N j'(eta)t-j''(eta)t^2/2](1+o(1)),

    a(eta)=exp(iu_*/2)/[2((T+2)(T+6))^(1/4)].          (13)

The displayed constant comes directly from the index Gaussian:
2^(-5/2)pi^(-1)sqrt(2pi/|Psi_uu|)
times sqrt(sin(2u_*))/sin(u_*)^(5/2). In particular it is nonzero.
At t=0, (13) also turns (9) into equality.

Elementary differentiation under the integral in (11) yields

    j'(eta)=alpha(eta)/pi,
    alpha(eta)=atan(sinh(eta/2)),
    j''(eta)=1/[2pi cosh(eta/2)]=cos(alpha)/(2pi).       (14)

For example j' follows by substituting tan(v/2) in its integral and
using tan(u_*)=cosh(eta/2). Also j(eta)-eta/2 tends to zero as
eta tends to infinity. Integrating (14), or differentiating the
Lobachevsky expression with this boundary value, gives

    j(eta)-alpha eta/pi
      =(4/pi)[Lambda(pi/4+alpha/2)+Lambda(pi/4-alpha/2)]. (15)

## 6. The original marked residue has a surviving leading term

The exact full source, including its normal coefficients, is

    A_(s,N)=(-1)^d N^2/(2pi i) integral_(|w|=R)
       z_N(w+w^(-1))^s
                 w^N(1-w^(-2))/(1+w^N)^2 dw.            (16)

This is the proved coefficient/partial-trace identity for Phi_2,
not a newly defined period. Choose eta=2asinh(tan(pi/s)), so that
s j'(eta)=1. Parametrize w=-R exp(i theta). Uniformly on this
circle, the rational factor is w^(-N)(1-w^(-2))[1+O(R^(-N))].
The error is exponentially smaller by (9),(10).

In the central window theta=t/sqrt N, the original factor (-1)^d
cancels the exact sign of w^(1-N). Equations (13),(14) cancel the
linear Fourier phase as well. The remaining Gaussian is
exp[-s j''(eta)t^2/2]. Bound (10) permits dominated convergence in
this final integral; its complement is exponentially negligible.
Consequently

    A_(s,N)=N^(3/2) exp(-i s pi d/4)
       [(R-R^(-1))a(eta)^s/sqrt(2pi s j''(eta))]
       exp[N(sj(eta)-eta)](1+o(1)).                      (17)

Equations (14),(15) are precisely the constant and exponent in (1).
The double-pole factor 1-w^(-2) is nonzero at -R and has been kept.
Equivalently, all higher positive windings in the exact source have
an extra R^(-(m-1)N) factor on this same circle; none was dropped
before estimating it. Together with the independently proved
finite-source and backward-envelope lemmas, this proves survival of
the specified original raw period with its stated normalization.

The bounds and local expansion used above are all at fixed s. No
uniform assertion as s grows with N, no fixed Dehn-filling theorem,
and no general-knot volume conjecture follows from (1).

## 7. Independent checks and the normalization boundary

Two independent analytical audits checked the midpoint maximum,
the lower-index envelope comparison, the all-parity coefficient
phase, the two real Gaussian integrations and the marked residue
constant. The explicit harmonic-error backward proof was separately
audited before use. The
[finite audit](../experiments/audit_actual_pretzel_coherent_circle_and_period_asymptotic.py)
checks the exact stationary polynomial/Hessian, literal Newton-circle
factors, and the predicted full complex leading constant against the
original value-plus-normal period at N=32,33,64,65,128,129 and
s=3,5,7,9. Those samples are calibration of the proof, not a
replacement for its estimates.

The original pretzel source theorem keeps a peripheral/framing line
chi_N outside A_(s,N). Formula (1) has NOT silently absorbed that line.
The [normalization proof](actual_complete_augmented_source_normalization.md)
retains the whole modified-dimension meridian germ before evaluating
it: |chi_red|=1 and |chi_full|=1/N at THIS complete point. It also
checks that the exact enhanced Kashaev comparison extends to this
multicomponent link, with component-dependent sign (-1)^(d(c-1)).
No polynomial-size assertion for an arbitrary moving peripheral
germ is inferred. The fixed filled-knot source also
contains the ENTIRE coherent auxiliary-color sum; taking only its
complete-color value is not a filling theorem.

## 8. The requested special inner product is an explicit Fourier norm

Write the SAME finite Laurent polynomial as

    z_N(w+w^(-1))^s=sum_(k=-sM)^(sM) a_k w^k.

For N>=3 use the positive inner product on its coefficient space

    <a,b>_R=sum_k conjugate(a_k)b_k R^(2(k-N)),
    Z_(s,N)=||a||_R^2
       =R^(-2N)/(2pi) integral_(-pi)^pi
            |z_N(-R exp(i theta)-R^(-1)exp(-i theta))|^(2s)dtheta.
                                                               (18)

The equality is finite Fourier--Plancherel. It retains all coherent
inner sums BEFORE squaring. The exact original source functional is

    b_N(a)=(-1)^d N^2 sum_(m>=1)(-1)^(m-1)m
                                  (a_(mN-1)-a_(mN+1)),        (19)

with coefficients outside the finite support equal to zero. Its
squared dual norm is bounded explicitly by

    ||b_N||_(R,dual)^2
       <=N^4(R^2+R^(-2)) sum_(m>=1) m^2 R^(-2(m-1)N)
       =N^4(R^2+R^(-2))(1+x)/(1-x)^3, x=R^(-2N).       (20)

There is no index overlap for N>=3. Omitting absent coefficients can
only decrease this bound. Cauchy--Schwarz therefore proves EXACTLY

    |A_(s,N)|^2<=N^4(R^2+R^(-2))(1+x)/(1-x)^3 Z_(s,N). (21)

This metric is specified by the polynomial source and the geometric
radius; it does not use the unknown contracted value A_(s,N).
Equations (10),(13) additionally prove, at the radius in section1,

    Z_(s,N)=[|a(eta)|^(2s)/sqrt(2s cos alpha)]
             N^(-1/2) exp[N V_s/pi](1+o(1)).            (22)

Thus for this complete augmented source the original question is
literally Cauchy in a specified inner product, AND its positive
energy has now been independently estimated at the sharp volume
rate. The additional Gaussian argument in section6 proves the lower
bound/survival that Cauchy by itself cannot supply. For an external
normalization chi_N, (21) retains |chi_N|^2 on its right.

There is also an exact way to separate the upper-bound question from
survival. Let D_(s,N) be the ACTUAL squared dual norm of (19) on the
finite coefficient space, and let v be its Riesz vector for (18).
Then

    |A_(s,N)|^2 = D_(s,N) Z_(s,N) cos(theta_N)^2,
    cos(theta_N)^2=|<v,a>_R|^2/(||v||_R^2 ||a||_R^2).    (23)

Here theta_N denotes the Hermitian angle, so cos(theta_N) is defined
as the nonnegative normalized absolute overlap. For each fixed s>=3,
both first-winding indices N-1,N+1 eventually lie in the coefficient
space. Consequently

    D_(s,N)=N^4(R^2+R^(-2))(1+O(R^(-2N))).

For fixed odd s>=3, equations (1) and (22) now give the quantitative
survival statement

    cos(theta_N)^2 ~ [(R-R^(-1))^2/(R^2+R^(-2))]
                         sqrt(2/(s cos alpha)) N^(-1/2). (24)

Thus Cauchy's upper estimate loses only a polynomial factor for this
particular original source. The nonzero-overlap asymptotic (24) uses
the independently proved original-period asymptotic (1); it is not
inferred from positivity or Plancherel. For a general filled source,
the geometric energy estimate and exclusion of exponentially small
overlap remain separate requirements.
