# The original Newton and complete-core local actions on the reciprocal branch

30 October 2026. Independently reviewed and frozen. Original untwisted port;
x,b,c,y>0, with the literal input b/output c convention. The theorem
is an equality on the selected HOLOMORPHIC GERM near alpha=0 and any
fixed positive face base. The real formulas below use 0<alpha<1/2 to
describe the reciprocal algebraic branch; they do not assert a global
continuation of the marked core or its source period over that range. This compares classical
generating functions on one explicitly continued sheet. It neither
moves a finite source cycle nor identifies its amplitude or contribution.

Use the [exact Newton action and its localized critical equations](actual_alternating_newton_peripheral_branch.md). Put A0=x+y,
L=A0+b+c, D=xy-bc and kappa=4cos(pi alpha)^2. For 0<alpha<1/2,
let z be the smaller positive root of

    (L^2+kappa D)z^2-(2LA0+kappa xy)z+A0^2=0.

The existing proof gives 0<z<A0/L<1. Set

    theta=acos(cos(pi alpha)sqrt(z)), r=theta/pi,
    rho=1-r, W=exp(-2i theta),
    k=(A0-Lz)/(2cos theta)>0,
    sinh(pi beta)=sin(pi alpha)sqrt(z/(1-z)), delta=i beta.

The two useful algebraic identities are

    k^2=xy(1-z)+bc z,
    A0-Lz=2k cos theta.                                      (1)

The actual selected primitive collar obeys R0=exp(2pi i alpha),
with meridian M=exp(-pi i alpha). The reflected Newton root W is
chosen, not the first-half root exp(2i theta).

## 1. The exact marked Newton lifts

Write phi_b=Arg(k+b exp(i theta)), phi_c similarly, and set

    xi=Arg(k-x exp(-i theta))/pi,
    eta=Arg(k-y exp(-i theta))/pi,
    mu=1-phi_c/pi.                                          (2)

All arguments in (2) are the indicated real arguments between0 andpi.
The exact reverse reconstruction has

    t=-k exp(-i theta),
    A=exp(2pi i xi)=(k-x exp(-i theta))/(k-x exp(i theta)),
    B=exp(2pi i eta)=(k-y exp(-i theta))/(k-y exp(i theta)),
    Z=exp(2pi i mu)=(k+c exp(-i theta))/(k+c exp(i theta)).    (3)

This is precisely the earlier t=W(Lz-A0)/(W+1), followed by its
original A,B,Z reconstruction. Moreover its t equation gives

    AB/Z=(k+b exp(-i theta))/(k+b exp(i theta)).

Now 0<phi_b,phi_c<theta and 0<pi xi,pi eta<pi-theta.
Consequently xi+eta+(phi_b+phi_c)/pi is an integer strictly between
0 and2, hence exactly1. Thus

    mu-xi-eta=phi_b/pi, 1-mu=phi_c/pi.                       (4)

This proves that ALL four Newton face loads are positive and add to1.
It also proves the strict four-binomial K-polytope inequalities:

    rho<mu<1, 0<xi,eta<rho, xi+eta<mu,
    mu+rho-xi-eta=rho+phi_b/pi<1.

Only the low-color Newton termination is violated: rho>1/2>alpha.
The principal log mu=-phi_c/pi is NOT the original marked lift (2);
already its face monomial would change by Log(c/b), before any
additional entropy-sheet changes.

## 2. Full face momenta equal the core angles

Let Q_b(delta) be the actual one-triangle determinant-plus-beta rate
plus HALF of the forced-factor rate, normalized by Q_b(0)=F(x,b,y).
Then Q_b'=-Log(E_b/sqrt(Dg)), where

    Dg=A0^2-4xy sin(pi delta)^2,
    T_b^2=b A0+xy+b^2 sin(pi delta)^2,
    E_b=A0+2b sin(pi delta)^2+2sin(pi delta)T_b.

All roots and logarithms are the source-selected ones at completeness.
The [proved source circle-pattern identity](actual_marked_deformed_circle_pattern.md),
section3, gives
partial_(log l_j)Q_b=theta_j^(b)/(2pi), the three actual center angles.
At delta=i beta the angles remain real and positive on the selected
near-complete germ. Directly from (1), with C=cos theta,S=sin theta,

    cosh(pi beta)=S/sqrt(1-z),
    T_b=(k+b C)/sqrt(1-z), T_c=(k+c C)/sqrt(1-z).           (5)

Therefore the middle-angle formula tan(theta_b/2)=b cosh(pi beta)/T_b
is tan(phi_b). Since both angles lie in(0,pi), theta_b=2phi_b,
and similarly theta_c=2phi_c. This proves the two middle derivatives.

Here is an explicit algebraic proof for the outer derivatives too.
Put H=1-z and

    R0x=xH(y-x)+2i x S k,
    R1x=H A0+2x(z-C^2)+2i x S C,
    R_b=R0x+b R1x, R_c=R0x+c R1x.

The actual deformed center-triangle sine/cosine formulas say

    exp(i theta_x^(b))=R_b/[(x+b)H sqrt(Dg)].

The identity

    R_b R_c (k-x C-i x S)
    =(x+b)(x+c)H^2 Dg (k-x C+i x S)                     (6)

follows by substitution of

    b+c=[A0 H-2kC]/z, bc=[k^2-xyH]/z, S^2=1-C^2.

In particular exp(i(theta_x^(b)+theta_x^(c)))=exp(2pi i xi).
Both angle sums lie strictly between0 and2pi, so they agree as marked
angles, not merely modulo2pi. Exchange x,y for the other outer face.
Thus the full homogeneous face gradients are exactly

    (xi,mu-xi-eta,1-mu,eta)
    =partial_(log x,log b,log c,log y)[Q_b(delta)+Q_c(delta)]. (7)

Equation (6) was independently expanded symbolically; its residual
is identically zero after the three displayed substitutions. The
angle branches extend to a sufficiently small complex neighborhood.
Regularity of the reconstructed critical point comes from the earlier
localized four-branch reconstruction and its simple quadratic roots,
not from the outer-angle identity alone.

## 3. The actual sine continuation and stationarity

Let J(t)=int_0^t Log(2sin(pi u))du, initially real for0<t<1.
Continue rho BELOW the two real divisors rho=alpha and rho=1/2.
On the final real reciprocal branch this specifies

    J(t)=-J(-t)+pi i t,                -1<t<0,
    J(t)= J(t-1)+pi i(t-1),             1<t<2.             (8)

Both negative sine factors have Log=log(abs(sine))+pi i. The opposite
approach sides in their arguments are essential: alpha-rho passes
above0, while2rho passes below1. A continuation exists without any
extra K divisor: the K-polytope is convex. Join an initial strict
physical point with rho<alpha to (2) inside this polytope, and detour
its parameter below the two specified rho crossings. All K arguments
stay near(0,1); rho and alpha+rho also stay in(0,1).

Use the FULL homogeneous action, not just its critical-variable part:

    Psi_New=K+B_alpha+pi i(alpha+rho)+Log c
             +mu Log(b/c)+xi Log(x/b)+eta Log(y/b),      (9)

with the literal K,B_alpha of the Newton theorem. On the selected
real branch K has only positive sine arguments. By (8) the imaginary
part of B_alpha is pi(1-alpha-rho). Thus the full action has constant
imaginary part pi, and all four critical-variable derivatives have
zero imaginary part. Their exponentiated equations are the exact
uncleared Newton equations, so their real derivatives are exactly0.
There is no concealed integer stationarity subtraction.

The envelope external derivative retains the pi i alpha character:

    partial_alpha Psi_New,crit
    =Log[-sin(pi(alpha+rho))/sin(pi(alpha-rho))]
    =log[sin(theta-pi alpha)/sin(theta+pi alpha)]
    =-2pi beta=2pi i delta.                              (10)

For the last step, tanh(pi beta)=tan(pi alpha)cot theta, by (5).
Omitting pi i alpha would give the wrong external derivative.

## 4. Complete-core action and the additive constant

Define the [original untwisted local core generating function](actual_complete_core_complex_packet.md) by

    S_core(alpha;x,b,c,y)=Q_b(delta)+Q_c(delta)+2pi i alpha delta,
    Log R0(delta)=2pi i alpha, delta(0)=0.                 (11)

Its delta stationarity is exact, so its external derivative is
2pi i delta and its four face derivatives are (7). Consequently
Psi_New,crit-S_core is constant on the selected connected germ.
It is important that (9) contains Log c: without it one face derivative
would differ by1 and the action difference would not be constant.

Calibrate at x=b=c=y=1 and alpha=0. Then

    rho=2/3, mu=5/6, xi=eta=1/3,
    K=-4J(1/6)-4J(1/3),
    B_0=-5J(1/3)+pi i/3.

The elementary reflection J(1-t)=-J(t) and duplication
J(2t)=2J(t)+2J(t+1/2) imply2J(1/6)=3J(1/3).
Also F(1,1,1)=-3[J(1/6)+J(1/3)]. Therefore

    Psi_New,crit = S_core + pi i.                       (12)

This equality is exact on the specified holomorphic germ; it is not
only equality of trace squares or exponentiated derivatives. Other
continuation windings need their corresponding explicit characters.
Both sides have been compared in the SAME homogeneous face
normalization. The [literal source adapter](actual_homogeneous_casimir_face_source.md),
equation(7a), multiplies either local homogeneous kernel by
N^-1(bc)^(-d/2) on the same original lifted face variables. Thus the
corresponding physical-box actions both subtract
(Log b+Log c)/2, and (12) is unchanged. The original global cup,
cap, target and mark characters are likewise common and retained;
none is reset to obtain the equality.

At leading semiclassical level the additive constant is the actual
phase exp(pi i N)=(-1)^N. The literal finite Newton sign is
(-1)^(h-1+r)=exp[pi i N(alpha+rho)]*(-1); its additional order-one
minus sign remains in the finite amplitude, as do all factorial +/-1
shifts. This result does not compare those amplitudes.

The branch is outside the low terminating Newton support. Nothing
here deforms the original finite cycle to it, excludes other branches
or endpoint currents, or proves its contribution coefficient nonzero.
It provides a source-normalized local classical generating-function
interface only; global face identification still uses the original
shared variables and their exact target/mark characters.

## 5. Physical support and verification

The calibration at alpha=0 is an analytic germ limit, not an evaluation
of L_0, which is exactly zero. Nor does the same exterior action prove
a complete exponential rate for fixed low color. For h=1, alpha=1/N
tends to zero, but the actual L_1 is the identity and its finite Newton
sum contains ONLY r=0. The selected critical index has rho>1/2 and
is absent from that terminating sum. Its local homogeneous identity
kernel has the already proved rate log max(b,c), not an automatically
selected complete-circle rate. These facts are consistent with (12):
the theorem compares phase functions, not finite amplitudes, cycles
or their contribution coefficients.

The [focused audit](../experiments/audit_actual_newton_complete_local_action.py)
checks the exact polynomial identities, the explicitly marked loads,
raw critical derivatives on the prescribed sine sheets, the unsquared
collar, and the full action including its imaginary constant. Its
[results](../experiments/actual_newton_complete_local_action_results.json)
are classical identity checks, not numerical evidence for a finite
source cycle deformation or a selected asymptotic contribution.

Root full analytical and public audit-code review: PASS. Two independent
full analytical reviews also checked the canonical lifts, strict K
polytope, outer-angle identity, sine continuation, peripheral momentum
and additive constant. The author and independent redirected 70-digit
audits reproduce two symbolic identities, 24 full critical actions,
120 raw stationarity/external derivatives, 96 marked face derivatives
and 24 unsquared collar checks, with maximum error below 1.74e-69.
A separate root implementation of the triangle normalization and
imaginary-delta collar integral checked eight additional equal,
asymmetric and large-ratio cases at 65 digits, with error below
6.72e-66. These reviews certify the stated local holomorphic action
identity; they do not certify a finite-cycle contribution or an
amplitude comparison.
