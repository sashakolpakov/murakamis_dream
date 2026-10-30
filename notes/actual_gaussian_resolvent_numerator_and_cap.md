# The original Gaussian resolvent has a positive numerator and a controlled closing cap

31 October 2026. Independently reviewed. The exact original numerator has
a positive path expansion and a Fejer all-color formula, while the Gaussian
resolvent has a subexponential closing cap at +2. No global contour selection,
source asymptotic or generic-q continuation of the Gaussian is asserted.

## 1. Inputs already proved in the repository

[actual matching edge continuant operator period](actual_matching_edge_continuant_operator_period.md) gives the actual
generic tridiagonal blocks, both continuants, all Jordan poles and the true
physical high-total adapter. [actual casimir off spectrum prefix action](actual_casimir_off_spectrum_prefix_action.md)
and [actual matching edge cross central green action](actual_matching_edge_cross_central_green_action.md) give selected
logarithmic actions only on strict physical prefix/row compacts. They do
not cover arbitrary complex magnetic heads, midpoint prefixes or a global
contracted exterior. The latter theorem is explicitly an integrand theorem.

[actual casimir endpoint resolvent bound](actual_casimir_endpoint_resolvent_bound.md) bounds EVERY original block by
CN^17 at +2 and on |sigma-2|<=cN^-18, including genuine resolvent normals.
The stronger [actual casimir closing region bound](actual_casimir_closing_region_bound.md) gives, for fixed
gamma>0, throughout the angular cone

    sigma=2+r exp(i phi), |phi|<=pi-gamma,
    ||(sigma-Omega)^-1|| <= CN^3 exp[CN f(r)+C log^2 N],
    f(r)=sqrt(r) log(2+1/r).

It includes every physical degree and all fixed genuine RESOLVENT jets.
Thus the +2 joining region was already controlled; it must not be reported
as an unresolved endpoint estimate.

The new exact all-integer Gaussian uses the full Hermite data:

    R^n=q^(n d^2/4) f_n(Omega),
    f_n(sigma)=exp[n N K(sigma)/(4pi i)],
    K(sigma)=arccosh(-sigma/2)^2,
    chi_N(sigma)=2T_N(sigma/2)+2,
    V_N(sigma)=chi_N(sigma)(sigma-Omega)^-1.

K is analytic on C minus [2,infinity), removable at -2. This equality is
at the original root; it does not identify an arbitrary off-root R germ.
The homogeneous source applies coefficient extraction to the ordered
product of these local functions, retaining all original targets and the
unit q^(n d^2/4). No additional N or marked scalar is introduced by this
functional calculus.

## 2. A direct Gaussian consequence for the entire closing cap

On either side of the K slit near +2,

    K(sigma)=-pi^2+O(sqrt(|sigma-2|)),
    |f_n(sigma)|<=exp[C |n| N sqrt(|sigma-2|)].

The estimate is uniform on either slit side, including its boundary
values. Therefore the old whole-cone resolvent bound gives

    ||f_n(sigma)(sigma-Omega)^-1||
      <=CN^3 exp[CN(f(r)+|n|sqrt(r))+C log^2 N].       (1)

For every FIXED integer n this has vanishing exponential rate as r->0.
It also holds with fixed genuine q derivatives on the resolvent ALONE,
using the old resolvent product rule. Those are not advertised as genuine
derivatives of R^n.

There is an actual joining path in the Gaussian slit. Run inward on the
two rays sigma=2-r exp(+/-i gamma), down to radius rho_N=min(cN^-18,r_N/2) when the outer radius is r_N,
and join
them by the short LEFT arc of that circle. The rays are covered by (1).
The left arc is in the old polynomial endpoint disk and lies to the RIGHT
of the largest spectral node, whose distance from 2 is comparable to N^-2.
It never crosses the K cut. On that arc |f_n|=exp[O(|n|N sqrt(rho_N))]
and the full resolvent is polynomial. The cap therefore has rate at most
C[f(r)+|n|sqrt(r)], and any r_N->0 yields exp[o(N)] for fixed n.
This establishes only the closing portion of a contour, with no estimate
for its surrounding source contraction.

## 3. Exact positivity of the FULL homogeneous resolvent numerator

Use distinct names B,C for the two middle face weights. In the proved
source polynomial representation, Omega=-T acts on z^j, 0<=j<N, by

    Omega z^j=c_j z^j-b_j(x+y)z^(j-1)-e_j xy z^(j-2),
    c_j=2cos((2j+1)pi/N),
    b_j=4sin^2(j pi/N),
    e_j=4sin(j pi/N)sin((j-1)pi/N).

Here b_0=e_0=e_1=0 and all allowed lowering weights are nonnegative.
These are the original endpoint factors, not cyclic replacements.

Expand the resolvent by ALL finite downward paths from j to i, using
steps one or two. A path with k steps visits k+1 distinct row indices.
Multiplication by chi_N removes precisely those k+1 factors, with their
multiplicities even when eigenvalues coincide. Its numerator is

    (-1)^k (positive step weight)
                product_(unvisited r)(sigma-c_r).

At sigma=-2-u, u>=0, the product has sign (-1)^(d-k). Consequently

    P_N(u;x,B,C,y):=(-1)^d H_(V_N(-2-u))(x,B,C,y)

is a polynomial with NONNEGATIVE coefficients in all FIVE variables
u,x,B,C,y. Its face degree remains d. The same original homogeneous
adapter is used, including C^(d-j) for the initial degree j. For every
complex sigma,

    |H_(V_N(sigma))|_coef <= P_N(|sigma+2|;x,B,C,y).    (2)

The inequality is termwise in face coefficients, since
|sigma-c_r|<=|sigma+2|+2+c_r. It controls the entire polynomial numerator,
including its independent semisimple data; no interpolation from only
the complete-channel values was used. Cauchy on a fixed spectral disk
also controls spectral derivatives by the same positive regularization
with an enlarged radius.

The spectral total-derivative identity supplied independently by cluster
is compatible with this statement. Its paired data involve BOTH V(c)
and V'(c); the latter cannot be recovered by differentiating a root-only
complete-channel simplification.

There is an exact Fejer normalization of the endpoint coupon. With
T=-Omega, define F_N(X)=(T_N(X)-1)/(X-1), using the polynomial quotient.
Then

    (-1)^d V_N(-2)=F_N(T/2)
      =N+2 sum_(j=1)^(N-1)(N-j) T_j(T/2)
      =L_N+2 sum_(h=1)^(N-1)L_h.                       (2a)

The first equality follows by dividing chi_N(sigma)-chi_N(-2) by
sigma+2 and using T_N(-X)=(-1)^N T_N(X). The other two follow from
the finite cosine telescope. This is a coherent identity in the actual
Casimir quotient, not positivity of the separate L_h coupons. It makes
the extra semisimple endpoint data completely explicit. No existing
Fejer-named note was found in the repository search.

More generally the divided Chebyshev identity gives EXACTLY

    (-1)^d V_N(-2cosh w)
      =L_N+2 sum_(h=1)^(N-1) cosh((N-h)w)L_h.           (2b)

For example, subtract 2T_N(t/2) from 2T_N(s/2), divide by s-t,
and expand in U_(h-1)(t/2); then set s=-2cosh w and t=Omega=-T.
This is a polynomial identity in s,t, so it includes coincident nodes
and all Hermite derivatives. The homogeneous coupon map and the whole
original marked contraction preserve it linearly.

For a set E of spectral ports, the contracted product of these signed
numerators is consequently the exact finite sum over 1<=h_e<=N of
the ORIGINAL external-color source, with weights 1 at h_e=N and
2cosh((N-h_e)w_e) at h_e<N. Every retained crossing on a complementary
port remains in its actual order. There is no free interpolation or
new mark. At a V-only selected port the coupon is literally L_h, with
no newly inserted half crossing. If an original R^epsilon is retained
separately at that same port, it multiplies BOTH sides of (2b) in its
original order. Thus the shared numerator-capacity problem is concretely an
exponential generating transform of ALL original colors. The existing
small-deficit corridor controls only h_e close to N; neither (2b) nor
path positivity supplies the missing phase-sensitive far-color bound.

## 4. Parity and an explicit limitation of a numerator norm argument

For odd N, -2 is a simple node and

    V_N(-2)=N^2 P_simple=N L_(N,simple).

For even N=2m, the exact scalar polynomial identity is

    -V_N(-2)=(2-Omega) U_(m-1)(Omega/2)^2.              (3)

Indeed chi_N(sigma)-4=(sigma^2-4)U_(m-1)(sigma/2)^2 and
V_N(-2)=(chi_N(Omega)-chi_N(-2))/(Omega+2), interpreted as its
polynomial quotient. Formula (3) retains semisimple contributions.

The unrestricted positive-weight norm in (2) does NOT always have the
complete folded rate. The B^d coefficient is a length-zero path, hence

    [B^d]P_N(u)=|chi_N(-2-u)|/(2+u+c_d).               (4)

At even N and u=0 this tends to one. Thus at x=y=C=1, B=exp(8),
liminf N^-1 log P_N(0)>=8. In contrast, positivity and degree a of
the original folded determinant give

    F(1,B,1)+F(1,1,1) <= (1/2)log B+2F(1,1,1)
                         <=4+pi<8.

The last elementary bound uses
F(1,1,1)=3[Lambda(pi/6)+Lambda(pi/3)]/pi<=pi/2, obtained by
the absolute Fourier bound |Lambda(theta)|<=pi^2/12. This is a
strictly positive quartet, not a zero-face pathology.

At odd N, the coefficient (4) vanishes exactly at u=0. But for any fixed
k>0 and u_N=N^-k its exponential rate is zero: writing
eta_N=arccosh(1+u_N/2), its numerator is
4sinh^2(N eta_N/2), while eta_N~sqrt(u_N). Therefore the same lower
rate 8 reappears under polynomially small regularization. The relevant
limits do not commute. No coefficientwise domination by bare P_N(0)
is asserted.

This is only a LOCAL arbitrary-positive-radius norm limitation. It is
not a counterexample to the original shared marked coefficient, nor to
a rate statement on a specially certified packing radius. The large
diagonal term has a source-specific face degree and can be constrained
by the remaining original graph. The phase-blind Hermite obstruction
in [actual direct long power source](actual_direct_long_power_source.md) is a separate, graph-wide result.

## 5. The Gaussian does not automatically damp a whole enclosing contour

On the spectral cover put sigma=-2cosh w, w=s+it, s>0, |t|<pi. Then

    K=squared w,
    |f_n|=exp[n N s t/(2pi)],
    chi_N(-2cosh w)=2[(-1)^N cosh(Nw)+1].

On a fixed compact with s>0,

    N^-1 log |f_n/chi_N| -> n s t/(2pi)-s.            (5)

Thus one side is damped and the other grows. On the growing side, a
fixed spectral ellipse with |t|>2pi/|n| gives positive scalar quotient
rate, increasing with |n|. The exact matrix numerator can change that
rate, but the mere largeness of a fixed twist cannot justify a global
decrease. A complete ellipse also meets the K cut near +2; deleting that
point and using the proved cap does not change this bulk sign issue.

In the half-plane Re w>0 the exact denominator has the convergent expansion

    epsilon=(-1)^N,
    1/chi_N=epsilon exp(-Nw)/(1+epsilon exp(-Nw))^2
            =sum_(m>=1) (-1)^(m-1) epsilon^m m exp(-mNw). (6)

The individual Gaussian-charge phase is n w^2/(4pi i)-m w, before adding
the actual V numerator phase and all face coefficient actions. Its
stationary point without that numerator is w=2pi i m/n. There is no
justification for discarding every m except the smallest. This agrees
with the independently derived nonzero midpoint charges in the exact
full-Hermite Fourier formula.

## 6. A precise remaining input

A sufficient next theorem would control the ORIGINAL marked, shared-face
resolvent numerator after sewing, uniformly on a specified spectral
cycle and on the needed complex face torus. It must include the full
V (or V and V'), not just positive complete samples, and prove:

1. a local analytic relative packet at the selected near-parabolic
   stationary point, including its original coefficient contour;
2. a strict global real-action bound for the complement of that packet
   on a homologous product cycle, preserving every spectral pole and
   the endpoint/Fourier currents;
3. control of every surviving nonzero charge in (6), or its equivalent
   unsplit resolvent period, with the actual neighboring Casimirs kept
   in their original order.

The torsor theorem solves the classical local transport and normalizes
the Gaussian Hamiltonian. The existing Green estimates supply selected
integrand phases on strict physical charts, and (1) completes the +2
cap for this root Gaussian. Neither supplies the missing global
source-specific amplitude, cycle comparison or complementary gap.
The exact positive path theorem (2) is a concrete input,
but (4) explains why replacing its shared coefficient by an unrestricted
local norm would not complete the argument.

## Validation and reviewed scope

The [focused original-source audit](../experiments/audit_actual_gaussian_resolvent_numerator_and_cap.py)
and its [results](../experiments/actual_gaussian_resolvent_numerator_and_cap_results.json)
record 77 symbolic identities, 3,100 independently built original
coproduct/physical-grid entries (including 1,000 wrong-unwrapped-total
zeros), and 4,039 nonnegative path/complex majorant checks. They do not
numerically establish any asymptotic or contour claim.

Primary full analytical and audit-code review: PASS. Independent full
analytical/code review and fresh redirected replay: PASS. The reviews
checked the existing all-block endpoint estimates, Gaussian joining cap,
full multiplicities in the path expansion, Fejer and parity identities,
strictly positive-quartet rate comparison, source target normalization
and charge signs. The joining radius was clarified to remain inside
both the endpoint disk and an arbitrarily shrinking outer cap. The
remaining bulk/shared-source requirements in Section 6 are not proved.
