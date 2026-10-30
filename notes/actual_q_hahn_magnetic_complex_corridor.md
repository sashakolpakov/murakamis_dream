# The actual magnetic polynomial and its complex corridor

30 October 2026. This note concerns the original complete-circle column,
at fixed integer pair degree t and channel j. Its finite continuation in
the magnetic coordinate u is specified by its terminating factorial sum,
not chosen from an interpolation class. An exact coproduct recurrence
places every zero outside the physical magnetic strip. The original
Casimir difference equation then upgrades the real magnetic amplitude
theorem to a complex corridor in u/N.

The continuation keeps t and j REAL and discrete. It is not a joint
continuation in all magnetic/channel variables of an assembled plat.
In particular it does not choose the global source integration cycle.

## 1. A literal finite continuation, with all prefactors

Write d=N-1, q=exp(pi i/N), Q=q^2, x=q^d, and assume the actual
complete-circle inequalities

    d-j<=t<=d, 0<=j<=floor(d/2).

For a nonnegative integer a define the entire function

    beta(z,a)=product_(r=0)^(a-1) 2sin(pi(z-r)/N) / s_a,
    s_a=product_(r=1)^a 2sin(pi r/N).

The ORIGINAL continuation is the finite sum

    fhat_(N,t,j)(u)=exp(pi i u) q^[-(j+1)u]
       sum_(a=0)^j q^[(t+j-d)a]
                beta(j,a) beta(u,a) beta(t-u,j-a)/beta(t,j).           (1)

All exponential powers in (1) use their displayed logarithms. At an
integer 0<=u<=t, a term outside the original support vanishes because
one of its numerator sine factors is zero. Thus (1) is EXACTLY the
physical Casimir column, including its original scalar and phase.
Off that lattice those terms are retained; no fictitious support
truncation is made.

Put U=Q^u and T=Q^t. There is a polynomial G_t of degree at most j with

    fhat_(N,t,j)(u)=x^u U^(-j) G_t(U),  G_t(1)=1.         (2)

An explicit polynomial, with m=j-a and w=q^(t+j-d), is

    G_t(U)=i^(-j)s_j/beta(t,j)
       sum_(a=0)^j w^a q^[-mt-(a(a-1)+m(m-1))/2]
          product_(r=0)^(a-1)(U-Q^r)
          product_(r=0)^(m-1)(T-UQ^r) / (s_a^2 s_m^2).   (3)

Indeed each first product in the sine expression contributes
i^(-a)q^[-au-a(a-1)/2], and the second contributes
i^(-m)q^[-mt-mu-m(m-1)/2]. Their common u factor is q^(-ju).
This proves (2)--(3), including the degree, rather than inferring
an interpolation from its values.

## 2. The original coproduct proves the root factorization

Keep N and j fixed and let t range from d-j to d. The actual divided
coproduct F, normalized by the first component, gives

    G_(t+1)(U)=[Q^j(1-U)G_t(U/Q)
                        +(U-Q^(t+1))G_t(U)]/(1-Q^(t+1)).              (4)

To check its normalization directly, the unnormalized component at
degree t+1 is

    (1-Q^u) f_t(u-1)+q^(-d+2u)(1-Q^(t+1-u))f_t(u).

Its u=0 value is x^(-1)(1-Q^(t+1)). Dividing by this value and using
(2) gives (4). The term of degree j+1 cancels, so its right side is
again a polynomial of degree at most j. Equality on the t+2 original
physical nodes proves the polynomial identity as well.

At t=d-j the actual highest vector gives the exact base

    G_(d-j)(U)=(UQ;Q)_j/(Q;Q)_j.                        (5)

For example its u-th component is
(-1)^u q^[-(2j+1)u](Q^(u+1);Q)_j/(Q;Q)_j, directly from the
original highest-vector equation. There are d-j+1>=j+1 physical
nodes, so this determines the degree-j polynomial in (5).

Set h=d-t and n=j-h=t+j-d. Define

    B_h(z)=product_(r=0)^(h-1)(1+q^(h-1-2r)z).

Its coefficients are the positive sine binomials beta(h,a). Equations
(4)--(5) prove the factorization

    G_t(q^t z)=c_t B_h(z) A_n(z),
    c_t=q^(jn)/(Q;Q)_j,  A_0=1.                       (6)

Here A_n is a real polynomial of degree n with positive coefficients
and n simple negative roots. The following direct argument proves
these assertions at every step, not merely at sampled levels.

When h decreases to h-1, n increases to n+1. The residual update is

    A_(n+1)(z)=-Im[q^(-j-h)(1+q^h z)^2 A_n(qz)]/sin(h pi/N),          (7)

where (7) is stated for REAL z. Its holomorphic polynomial meaning is
the corresponding coefficientwise difference of conjugate polynomials.
Explicitly, if A_n=sum a_k z^k, then

    a'_k=[sin((j+h-k)theta)a_k
          +2sin((j-k+1)theta)a_(k-1)
          +sin((n-k+2)theta)a_(k-2)]/sin(h theta),
    theta=pi/N, a_k=0 outside 0<=k<=n.                  (8)

All coefficients of degrees 0 through n+1 are positive. The putative
degree n+2 coefficient is zero, since j=h+n. The scalar in (6)
changes by c_(t+1)=q^j c_t. To obtain (7), use

    B_h(q^(-1)z)=(1+q^(-h)z)B_(h-1)(z),
    B_h(qz)=(1+q^h z)B_(h-1)(z)

in (4); its residual numerator is

    q^(2j)(1+q^(-h)z)^2 A_n(q^(-1)z)
          -q^(-2h)(1+q^h z)^2 A_n(qz).

Now suppose A_n(z) has roots -rho_k, rho_k>0. At z=-r, r>0, the
continuous argument of the quantity inside Im in (7) is

    -(j+h)theta+2Arg(1-q^h r)+sum_k Arg(rho_k-qr).

It strictly decreases from -(j+h)theta, which lies in (-pi,0), to
-(n+2)pi as r tends to infinity. The limiting endpoint is not reached
at finite r. Each factor stays nonzero and each individual argument
strictly decreases. Therefore exactly n+1 multiples of pi are crossed,
with nonzero derivative. Equation (7) has n+1 distinct negative roots.
Since its degree is at most n+1, these are all its roots and the degree
is exactly n+1. This starts from A_0=1 and proves (6).

**Exact zero theorem.** G_t has its h forced zeros

    U=Q^(t+1),...,Q^d,

and its n residual zeros lie on U=-q^t rho with rho>0. The residual
zeros are simple; a residual zero can coincide with a forced zero,
which causes no problem below. In the scaled magnetic variable
upsilon=u/N, the latter zeros have

    Re upsilon=(1+t/N)/2 modulo 1.

Every zero therefore lies OUTSIDE

    S_tau={upsilon in C: 0<Re upsilon<tau}, tau=t/N.      (9)

The exact finite function (1) is nonzero on this entire strip, at
both parities and composite levels. This conclusion is special to
the original physical Fourier argument w=q^(t+j-d); it is not an
assertion of joint zero-freeness in independent w and upsilon.

## 3. The canonical magnetic logarithm and its selected limit

Let (tau,xi)=(t/N,j/N) remain in a compact strict real parameter set
with 0<xi<tau<1, xi<=1/2, tau+xi>=1 in the limiting complete chamber.
The actual integer parameters may have tau+xi=1-1/N; all constructions
use those actual parameters and are uniform for this O(1/N) boundary
displacement. Consider compact subsets inside S_tau, uniformly away
from both vertical boundaries.

Factorization (6) gives locally uniform bounds for

    N^(-1)Log[fhat(N upsilon)/fhat(N upsilon_0)]           (10)

and all its fixed derivatives. Here upsilon_0 is near tau/2 and
the logarithm is continued in the simply connected strip. For each
root, the logarithmic derivative is 2pi i U/(U-zeta). The possible
root locations in section 2 are uniformly separated from the image
of the chosen compact set; radial roots are compactified by their
radius in [0,infinity]. Integrating along compact paths bounds each
root's logarithmic ratio uniformly. There are j<=N/2 roots, and the
explicit exponential in (2) supplies only a bounded normalized term.

The phase at the noninteger center is fixed exactly, not guessed:
B_h(1)A_n(1)>0 in (6), and hence a specified argument is

    Arg fhat(t/2)=pi[d(t-j)+j^2]/(2N).                 (11)

This uses (Q;Q)_j=(-i)^j q^[j(j+1)/2]s_j with its original product
phase. The leading imaginary action at the center is therefore
pi(tau-xi+xi^2)/2. A nearest integer to t/2, together with the
bounded logarithmic derivative in (10), supplies its real leading
value from the actual real-magnetic theorem.

Write the previously selected physical action, for REAL upsilon, as

    Phi_(tau,xi)(upsilon)=psi_(tau,xi,upsilon)(w_star)
                               +pi i upsilon(1-xi),
    w_star=exp[pi i(tau+xi-1)].                         (12)

At the center its internal saddle is alpha=xi/2+i eta. The paired
J terms make Ecal(alpha) real, so Im Phi(tau/2) is exactly
pi(tau-xi+xi^2)/2, agreeing with (11) to leading order. The same
pairing gives Ecal'' real negative and A(alpha)B(alpha)>0. Therefore
the continued Acal amplitude is positive real there. The remaining
order-one phase exp[pi i(alpha-tau/2)] is
-pi(tau-xi)/2, exactly the difference between (11) and N Im Phi.
This checks both the additive logarithmic mark and its finite phase.

The actual real-magnetic amplitude theorem supplies its values on
all physical samples. Normal-family limits of (10) must have the
same real part there. More precisely, adjacent physical sample
ratios and bounded second derivatives give

    exp(g'(upsilon))=exp(Phi'(upsilon))

on the real interval. Thus g'-Phi' is a constant 2pi i integer.
This sampling alias must be removed; dense samples alone do not
remove it.

At the center, positivity of all coefficients of B_h A_n gives

    0<=Im[N^(-1)partial_upsilon Log fhat(N upsilon)]<=pi

in the limit, with real part zero. The selected derivative in (12)
lies STRICTLY between 0 and pi on that imaginary axis. Indeed the
internal saddle there is alpha=xi/2+i eta, eta>=0. Its exact phase
equation is

    4Arg sin(pi(xi/2+i eta))
     +2Arg sin(pi((tau-xi)/2+i eta))=pi(tau+xi-1).

Consequently

    Phi'(tau/2)=pi i(1-xi)
                   +2i Arg sin(pi((tau-xi)/2+i eta))

has imaginary part in [pi(1-xi),pi tau], a compact subinterval of
(0,pi). The integer alias is zero. Equation (11) fixes the remaining
additive constant. Compactness and the identity theorem now prove
convergence of the WHOLE actual sequence, including derivatives:

    N^(-1)Log fhat(N upsilon) -> Phi_(tau,xi)(upsilon).    (13)

The right side is the holomorphic continuation selected by the
actual polynomial. The same subsequence argument gives uniformity
for compact real parameter families. It does not interpolate t or j.

## 4. The exact magnetic difference equation and its simple branch

Let f(upsilon)=fhat(N upsilon), h_N=1/N, U=exp(2pi i upsilon),
T=exp(2pi i tau), and Jc=exp(2pi i xi). The original symmetric
physical Casimir gives the exact finite difference equation

    A_+(upsilon,h_N) f(upsilon+h_N)
     +A_-(upsilon,h_N) f(upsilon-h_N)
     +(D_(h_N)(upsilon)-c_(h_N))f(upsilon)=0,            (14)

where q=exp(pi i h_N), Q=q^2 and

    A_+=(U-T)(1-QU)/T,
    A_-=(U-QT)(1-U)/(QT),
    D_h=(U/T)[2(q^(-1)+qT)-(q+q^(-1))U],
    c_h=q Jc+q^(-1)Jc^(-1).

It is an identity for the entire continuation (1). One direct check
uses (2): after removing its exponential, the residual is a polynomial
in U of degree at most j+1, since its top degree j+2 cancels. Its
constant coefficient is zero. It also vanishes at the t+1 original
physical nodes U=1,Q,...,Q^t, by the actual Casimir eigenvector
equation, including both boundary rows. Since t>=j, these zeros plus
U=0 force the polynomial to vanish identically. No generic contiguous
identity or missing endpoint equation is presumed.

Put

    A=(U-T)(1-U)/T, D=2U(1+T-U)/T,
    H(upsilon,a)=A(e^a+e^(-a))+D-(Jc+Jc^(-1)).          (15)

The branch selected in (13) satisfies H(upsilon,Phi')=0. It is
simple throughout the strip in the limiting complete chamber. Its
characteristic discriminant is exactly

    (Jc+Jc^(-1)-2)
       [Jc+Jc^(-1)+2-4U(1+T-U)/T].                    (16)

The second factor's zeros, after U=exp(pi i tau)X, obey

    X^2-2cos(pi tau)X+cos^2(pi xi)=0.

Because tau>=1-xi and xi<=1/2, its finite nonzero roots are negative
real. They lie on the same excluded magnetic line as the residual
roots in section 2. A zero root at xi=1/2 is not a finite U. Also
A has no zero inside S_tau and Jc!=1. Hence H_a!=0 there. On compact
subsets it remains bounded away from zero, also for the actual
O(1/N) displacement below tau+xi=1.

## 5. Actual complex amplitude from the magnetic finite shifts

This section proves a fixed complex corridor theorem around any
compact real magnetic interval inside (0,tau). The preceding root
and discriminant estimates also permit compact paths farther inside
the strip, with the continued functions specified in sections 3--4.

Write G_N=N^(-1)Log f and a_N=G_N'. The exact zero theorem and (13)
give bounded holomorphic derivatives and a_N->Phi' on larger compact
sets. Taylor expansion of the ACTUAL shifted ratios in (14) yields

    f(upsilon+/-h_N)/f(upsilon)
      =exp(+/-a_N)[1+(h_N/2)a_N'+O(h_N^2)].             (17)

Expand the displayed finite coefficients as A_+=A+h_N A_1^++O(h_N^2),
A_-=A+h_N A_1^-+O(h_N^2), and similarly for D and c. Explicitly,

    A_1^+=-2pi i U(U-T)/T,
    A_1^-=-2pi i U(1-U)/T,
    D_1=2pi i U(T-1)/T,
    c_1=pi i(Jc-Jc^(-1)),
    H_1(upsilon,a)=A_1^+e^a+A_1^-e^(-a)+D_1-c_1.

Equations (14) and (17) imply

    0=H(upsilon,a_N)
       +h_N[H_1(upsilon,a_N)+(a_N'/2)H_aa(upsilon,a_N)]
       +O(h_N^2).

Uniform simplicity first gives a_N-Phi'=O(h_N). Cauchy's estimate
on a larger compact set improves its derivative to the same order.
Substitution a second time proves the ACTUAL correction

    a_N=Phi'+h_N b+O(h_N^2),
    b=-[H_1(upsilon,Phi')+(Phi''/2)H_aa(upsilon,Phi')]
                                           /H_a(upsilon,Phi').       (18)

Let Btilde solve the scalar holomorphic equation Btilde'/Btilde=b,
with its nonzero value at the real center fixed by the previous
[actual amplitude theorem](actual_q_hahn_uniform_complex_amplitude.md).
Then Btilde is holomorphic and never zero on the corridor. The
center may be noninteger: use the nearest physical sample to fix
the constant to relative error O(1/N), since both Btilde and the
previous explicit amplitude are smooth and nonzero there.
Integrating (18) from that physical sample proves

    fhat_(N,t,j)(N upsilon)
        =N^(-1/2) Btilde_(tau,xi)(upsilon)
                exp[N Phi_(tau,xi)(upsilon)](1+O(N^(-1))).            (19)

The error is uniform on the complex corridor, with each fixed
derivative on smaller compact subsets. Thus the transport solution
in (18) is justified by the original polynomial and a known actual
constant; it is not a formal ansatz substituted for it.

The amplitude in (19) is the continuation of the earlier explicit one:

    Btilde_(tau,xi)(upsilon)
      =Acal_(tau,xi,upsilon)(w_star)
             exp[pi i(alpha_(tau,xi,upsilon)(w_star)-upsilon)].         (20)

To see this without assuming an unproved transport identity, compare
(19) with the previous actual theorem at physical real samples.
Taking sequences of parameters and samples tending to any strict
real point proves equality of the two nonzero amplitudes there.
Their holomorphic continuations are therefore identical. The local
coefficient functions are analytic across tau+xi=1, so the identity
also covers the actual O(1/N) boundary displacement. This analytic
identity between coefficient functions is NOT a claimed finite
interpolation of t or j.

The phases and the order-one factor in (20) retain both original
integer offsets. No root-normal derivative has been taken. The
theorem supplies an actual complex magnetic packet at fixed real
t,j; global magnetic/channel summation, complex pair-degree or
channel continuation, and the original global cycle remain separate.

## 6. A canonical joint rational continuation, without a joint estimate

There is also a source-defined joint continuation in u and v=t-u.
Set U=Q^u, V=Q^v and retain the phase x^u=exp(pi i d u/N). For
fixed N and j define the finite polynomial

    H_j(U,V)=sum_(a=0)^j [j choose a]_Q^2 q^[a(a-d)] V^a
        product_(r=0)^(a-1)(U-Q^r)
        product_(r=0)^(j-a-1)(V-Q^r),
    D_j(T)=product_(r=0)^(j-1)(T-Q^r).                  (21)

The original terminating formula, extended with its own finite sine
products, is exactly

    fhat_j(u,v)=x^u H_j(U,V)/D_j(UV).                  (22)

The denominator and the marked exponential are retained. This is a
specified finite rational function, not a choice of factorial
interpolation. In (21) the binomial is the GAUSSIAN binomial. If one
uses the positive sine binomial instead, the same coefficient is

    beta(j,a)^2 q^[a(2j-a-d)] V^a.                     (23)

Indeed [j choose a]_Q=q^[a(j-a)] beta(j,a). Confusing these two
binomials changes the original phase, already at j=2.

For a direct derivation, substitute the two finite sine products
used in (3), and use

    beta(t,j)=i^(-j)q^[-jt-j(j-1)/2] D_j(Q^t)/s_j.

Removing this denominator leaves the phase q^[a t+a(j-a)] before
the original w^a is included. Since w=q^(t+j-d), and Q^(at)U^(-a)=V^a,
the remaining phase is exactly q^[a(2j-a-d)]. This proves (22).
Restricting UV=T to an actual integer degree recovers

    G_t(U)=U^j H_j(U,T/U)/D_j(T).                      (24)

No joint zero-location theorem for H_j(U,V), or joint complex
asymptotic in pair degree and magnetic coordinate, is asserted here.
The preceding strip theorem uses the essential restriction that
UV=Q^t with t real and integer. Formula (22) specifies a possible
next object without supplying the missing estimates for it.

Audit: [exact magnetic polynomial and complex corridor](../experiments/audit_actual_q_hahn_magnetic_complex_corridor.py).

Independent analytical review: a second reader checked the literal
terminating continuation, coproduct normalization and negative-root
factorization, the strip zero exclusion, canonical center phase and
sampling-alias removal, the endpoint-inclusive Casimir equation and
its discriminant, and the actual finite-shift amplitude bootstrap.
The real-center normalization and both original integer offsets were
independently recalculated. The joint rational appendix, including the
Gaussian-versus-sine binomial phase, also passed. The primary reader's
fresh audit replay was retained rather than duplicated. The theorem
still fixes real discrete pair degree and channel; it supplies neither
a joint complex estimate nor a selected whole-source cycle.

Root review: full analytical read and fresh audit PASS. The review checked
the original terminating function, exact coproduct normalization, residual
root induction, canonical center phase, removal of the sampling alias,
Casimir polynomial identity, simple branch and two-order derivative
bootstrap. The replay included 186 independent joint sine-product checks
and 32 complex magnetic amplitude regressions. The joint rational formula
is exact; joint complex asymptotics and the global source remain open.
