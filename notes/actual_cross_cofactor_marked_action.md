# The full-V cofactor branch and the original marked peripheral action

The [whole-source local packet](general_full_spectral_numerator_geometric_packet.md) now assembles these results for the actual full numerator. The original global spectral filling period remains open.

31 October 2026. . The exact
central-cofactor formulas are in [actual cross cofactor factorization](actual_cross_cofactor_factorization.md).
This note identifies their indicated principal branch, including its
absolute normalization and the actual primitive logs. It does NOT prove
that a particular global quantum cycle selects it or that every complex
cofactor has a single-branch relative asymptotic.

Use spectral w=-sigma-2 (the cofactor note calls it u); the original
protected white faces are still named u,v and remain zero. At every
port put A=x+y>0 and P=xy. The principal diagonal and cleared tail root
are

 a(t)=4cos^2(pi t), s(t)=2sin(pi t),
 Lambda(t;w)=[s(t)^2 A+sqrt(s(t)^4 A^2
                          +4s(t)^2(a(t)+w)P)]/2.       (1)

For positive x,b,y select the root positive at w=0. Set

 w=-4sin^2(pi delta), sigma=-2cos(2pi delta),
 s=sin(pi delta), c=cos(pi delta),
 T_b=sqrt[bA+xy+b^2 s^2], D=A^2-4xy s^2,
 E_b=A+2b s^2+2s T_b.                                  (2)

All square roots/logs are the ones at delta=0. The finite physical
node is delta_a=(N-1-2a)/(2N), not an unrecorded unshifted row a/N.
The finite cofactors keep that half-index and all parity scalars.

## 1. Exact equality of the two normalized analytic actions

Define F_w by the stationary value

 F_w=mu Log b+integral_0^mu Log(a(t)+w)dt
                     +integral_mu^(1/2)Log Lambda(t;w)dt,     (3)

where mu is the continuation of the complete interior solution. It obeys

 b(a(mu)+w)=Lambda(mu;w),
 sin^2(pi mu)=c^2 b^2/[(b+x)(b+y)],
 mu=(1/pi)atan(b c/T_b).                                (4)

These identities follow by substitution into the quadratic for Lambda;
no asymptotic differentiation is involved. For small positive real delta,
mu<1/2-delta, so the first logarithm in (3) is positive along its path.
For positive x,y, Lambda(t)/t is nonzero and analytic at t=0. Separating
its log t singularity therefore defines a holomorphic germ of (3) near
delta=0, including b=0 by its limiting stationary value. Ordinary positive
b may vary down to zero on a fixed bounded interval after shrinking this
germ. Formula (3) is a stationary analytic value for complex parameters,
not a complex maximum operation.

For precision at b=0, write Lambda=t L with L(0) a unit and mu=b m
with m(0) a unit. In mu Log b minus integral_0^mu Log t, the only
potential logarithmic singularity is mu Log(b/mu); it is holomorphic.
Thus this is an analytic extension, not just a continuous rate limit.

Let Q_b(delta) be the original determinant-plus-beta-plus-HALF-forced-
product triangle action of the coupled complete source. Its proved
literal definition, putting nu=1/2-delta, is

 Q_b=I(2nu)-2I(nu)+integral_0^nu Log lambda_b(t)dt
       +(1/4)integral_nu^(1-nu)
                Log[x^2+y^2-2xy cos(2pi t)]dt,
 I(v)=integral_0^v Log(2sin(pi t))dt,
 lambda_b(t)=[A+2b cos^2(pi t)
       +2cos(pi t)sqrt(b^2cos^2(pi t)+bA+xy)]/[4cos^2(pi t)].

This is the actual beta, determinant and forced-product rate from
[actual positive face channel rate](actual_positive_face_channel_rate.md), not a chosen antiderivative.
Cancellation of their spectral derivatives gives its normalization
and differential

 Q_b(0)=F(x,b,y),
 partial_delta Q_b=-Log(E_b/sqrt D),
 partial_Log(b) Q_b=(1/pi)atan(b c/T_b).                 (5)

Then the exact action-germ identity is

                         F_w=Q_b(delta).               (6)

Here is a complete constant check. The envelope rule in (3) gives
partial_Log(b) F_w=mu, so F_w-Q_b is independent of b. Also

 partial_delta mu=-b s/T_b,
 partial_Log(b) Log(E_b/sqrt D)=b s/T_b.                 (7)

The second identity follows directly from partial_b E_b=s E_b/T_b.
It remains to fix the b-independent term, not assume it zero.

At b=0, put lambda=2sqrt(xy)/A in(0,1]. With theta=pi t, differentiating
the integral in (3) gives

 partial_delta F_w|_(b=0)
 =-lambda^2 s c integral_0^(pi/2)
       dtheta/[W(theta)(sin theta+W(theta))],
 W(theta)=sqrt[(1-lambda^2)sin^2 theta+lambda^2 c^2].

Rationalize the denominator and put z=cos theta. The result is

 -s c integral_0^1 {1/sqrt(1-z^2)
       -1/sqrt(1-lambda^2 s^2-(1-lambda^2)z^2)}
                                      dz/(z^2-s^2).     (8)

The apparent pole at z=s is removable: the two square roots there
are both c. For an elementary evaluation, each integral of
1/[(z^2-s^2)sqrt(B-Cz^2)] has antiderivative

 [1/(2s c)] log |(c z/sqrt(B-Cz^2)-s)
                         /(c z/sqrt(B-Cz^2)+s)|,

because B-C s^2=c^2 in BOTH terms of (8). Subtract these antiderivatives
before evaluating: their logarithmic singularities at z=s cancel,
with no jump. They both vanish at z=0. At z=1 the first tends to zero
and the second is -artanh(lambda s)/(s c). Hence

 partial_delta F_w|_(b=0)=-artanh(lambda s)
      =-Log[(A+2s sqrt(xy))/sqrt(A^2-4xy s^2)].        (9)

This calculation uses small real delta>0, where every real branch is
specified; holomorphic continuation then gives the identity of germs.
It agrees EXACTLY with (5) at b=0. Equations (7),(9) give the full
partial_delta identity for every b>=0. Finally (3) at delta=0 is the
already calibrated complete triangle action: integral_0^(1/2)log a=0,
and the actual lower-block product contributes no exponential constant.
Thus F_w-Q_b vanishes at delta=0 and has zero delta derivative, proving
(6) with no additive face-dependent or spectral constant.

## 2. All allowed marked zeros, including the lost local strip flag

If exactly one of x,y vanishes, Lambda=s(t)^2 A is the EXACT monomer
root. Differentiating (3) gives

 partial_delta F_w=-2 artanh[(s/c)tan(pi mu)]
                 =-2 artanh(b s/T_b)
                 =-Log(E_b/A),                         (10)

since D=A^2. This proves the same normalization directly on the one-line
triangle, without dividing by xy. It also follows by a dominated limit
of (8); the integrable bounds C+2|log t| are uniform as xy decreases to0.
If b=0 and xy=0, (3) is exactly

                         F_w=(1/2)Log A,               (11)

independent of w, just as the original cofactor is the monomer product
A^n product_(j=1)^n s_j^2. For b=0 and xy>0, (9) is its nonconstant
spectral force. These include every allowed triangle of the original
marked dictionary. Both outer faces cannot be the two protected MAIN
faces on a matching edge; thus A>0 remains part of that dictionary.

At a two-line triangle (11) alone does NOT recover its selected flags.
For example at b=y=0 its actual strip height still obeys H=2c^2/x:
the finite x-circle is tangent to the marked b-line and intersects
the marked y-line in the recorded orientation. The existing
[actual marked deformed circle pattern](actual_marked_deformed_circle_pattern.md)
retains this common line geometry and its selected eigenlines. We use
THAT global boundary adapter, not the double root or constant action
to invent a flag.

The protected-middle relative packet proved separately in
[actual cross cofactor protected packet](actual_cross_cofactor_protected_packet.md) has finite-N product
prod_j[s_j lambda_(j,+)] and a nonzero bounded amplitude. Its logarithmic
limit is exactly (3) at b=0, since s(t)lambda_+(t)=Lambda(t;w). Thus
(6),(9) identify an analytically PRESENT branch for those actual cleared
cofactors, including the exact monomer case. For a summed ordinary
middle b>0 and for the original shared coefficient, the corresponding
relative packet is a separate requirement.

## 3. The original physical conic and all momenta

By (4), the physical input momentum p=exp(-2pi i mu) satisfies exactly

\[
\sigma=2+\frac{(p-1)^2}{p}\frac{(b+x)(b+y)}{b^2}=-2-w. \tag{12}
\]

This is the original crossing Casimir, with the physical inverse of
the coefficient momentum as fixed in [actual crossing torus meridian transport](actual_crossing_torus_meridian_transport.md).
It is not a new trace convention. The reciprocal output momentum is
selected by the CROSS action Q_b+Q_c.

More precisely retain the full physical adapter H/(bc)^(d/2). For its
principal phase Theta=Q_b+Q_c-(Log b+Log c)/2, the original head change
of variables gives ALL derivatives

 p_in=exp(-i theta_b), p_out=exp(+i theta_c),
 g_out/g_in=exp[i(theta_y,in+theta_y,out)].            (13)

The three angles in each triangle are those of the deformed center
triangle. Identity (6), together with the already proved full face
gradients of Q, supplies the outer derivative in (13), not only (12).
The regular ordered-character calculation in
[actual whole source coupled face difference system](actual_whole_source_coupled_face_difference_system.md), §4, therefore
applies without changing a physical half power: the ENTIRE ordered
product P=BA is preserved and the same primitive centralizer transports
both punctures. Its selected spectral line is

                  J=-exp(-2pi i delta), lambda=-J.     (14)

At the protected zeros use the common marked line pattern and its
literal reflection products; no singular old Gauss denominator is
canceled there.

The actual original input b/output c collar has, on that J-line,

 R0=E_b E_c/D,
 C=I+(R0-1)/(J-J^(-1)) (P-J^(-1)I).                  (15)

The quotient is the already proved removable divided difference on the
selected marked germ. Its delta=0 limit is the nontrivial parabolic
collar, not I. The corner order and three contacts are those proved in
[actual deformed circle primitive collar](actual_deformed_circle_primitive_collar.md); in particular C is a
primitive shaded pairing, not the square of two shaded reflections.
These equations identify the regular original crossing/A-torsor branch.
They do not identify every branch of the full cofactor characteristic or
claim a scalar eliminated A-polynomial.

## 4. Global marked geometry and the correct polarization

For a fixed original certified D, form the stationary face action

 A_epsilon(delta)=crit_(ordinary faces)
    {sum_i [Q_bi(delta_i)+Q_ci(delta_i)]
         -sum_(ordinary f)Log l_f +pi i sum_i epsilon_i delta_i^2}.
                                                               (16)

The two original marked faces remain zero. The existing face Hessian,
marked circle reconstruction and source IFT give its selected local
analytic branch and one common circle family. By (6) it is exactly the
candidate full-V CROSS branch with the retained half-twist character.
This is an equality of principal action germs, conditional on that
branch when discussing a relative asymptotic of the full numerator.

The existing actual group assembly supplies its representation with
primitive logs

 U_i=-Log R0_i-epsilon_i Log(-J_i),
 V_i=2Log(-J_i)=-4pi i delta_i,
 partial_delta_i A_epsilon=U_i.                       (17)

The derivative uses face stationarity; it does not differentiate an
unproved asymptotic. At zero its diagonal Jacobian is

 partial_delta_j U_i=-2(C_i-pi i epsilon_i)delta_ij,
 C_i=pi[T_bi(0)+T_ci(0)]/(x_i+y_i)>0.                 (18)

Thus these are actual local coordinates on the same marked geometric
germ as the complete Fourier core. This is a LONGITUDE-polarized
primitive. Put G_lon=2pi i A_epsilon. Then

 dG_lon=-(1/2)sum_i U_i dV_i.                         (19)

The core instead has chi_i=-U_i/(2pi i) and
S_core(chi)=A_epsilon(delta)+2pi i sum_i chi_i delta_i.
Consequently

 G_mer=2pi i S_core=G_lon+(1/2)sum_i U_i V_i,
 dG_mer=(1/2)sum_i V_i dU_i.                          (20)

The complete source fixes 2pi Re A_epsilon(0)=Vol(Y_D). Applying the
proved core regulator identity through this exact Legendre relation
therefore gives the ABSOLUTELY normalized longitude action

 2pi Re A_epsilon(delta)
        =Vol(rho_delta)-(1/2)sum_i Im U_i Re V_i.      (21)

No local open-word re-framing invariance is used. Equation (21) retains
the complex boundary term; for real delta its V are purely imaginary
and that term vanishes. All known spectral-independent framing and
finite parity scalars remain outside the normalized principal action.

## 5. Original Gaussian charges and primitive filling logs

For an actual fixed crossing exponent n_i=epsilon_i-2p_i, the full
Hermite Gaussian contributes pi i n_i delta_i^2 and a surviving Fourier
charge ell_i contributes 2pi i ell_i delta_i, with their original
constant scalar signs retained. Its principal phase is therefore

 A_epsilon(delta)-2pi i sum_i p_i delta_i^2
                         +2pi i sum_i ell_i delta_i.

Stationarity gives EXACTLY

                     U_i+p_i V_i=-2pi i ell_i.        (22)

For the original unit charge ell_i=1 this is the already calibrated
primitive smooth filling equation. Reciprocal delta/J branches reverse
the corresponding logs and charges; kappa or the trace alone cannot
choose them. The charge0 contribution is identically zero in the
original spectral total-derivative formula and must not be resurrected
as a complete-point saddle. Higher charges remain actual terms of that
formula; (22) alone neither selects them nor supplies a smooth filled
metric at nonunit charge.

There is also an exact critical-value check. If S_fill denotes the
displayed phase, then

 2pi i S_fill=G_lon-sum_i p_i V_i^2/4-pi i sum_i ell_i V_i. (23)

For real integers p_i,ell_i, equation (22) makes the imaginary part
of the last two terms cancel the correction in (21) exactly. Thus

                 2pi Re S_fill=Vol(rho_delta)           (24)

at such a critical point. For unit charges on the already established
sufficiently long smooth-filling germ, this is the volume of that
actual filling. For other charges it asserts representation volume
only; no smooth completion or period contribution is inferred.

At fixed independently long twists the relevant delta_* is O(1/p),
fixed before N grows. The preceding identities locate its candidate
marked geometric branch and its regulator. They do not prove a
relative full-V packet there, its global coefficient-cycle intersection,
a nonzero charge sum, or a complementary Gaussian-contour bound.

## Focused verification

The reproducible helper
`../experiments/audit_actual_cross_cofactor_marked_action.py` accepts `--output`.
Its saved author result is
`../experiments/actual_cross_cofactor_marked_action_results.json`, evaluated at
75 digits. It checks the b=0 antiderivative symbolically, 24 independent
integrations of the literal beta/determinant/forced source against (3),
17 derivatives of that integral, and 12 actual Gauss configurations with
both ordered products and both primitive collar legs. It also checks
the polarization and full Gaussian boundary cancellation. Maximum
action error is 2.77e-76; the finite-difference force error is 8.62e-41;
the matrix error is 1.97e-73. These checks supplement the analytic proof;
they do not prove a relative packet or a contributing quantum cycle.

The action and geometry identities do not select a contributing original period.

[Focused audit](../experiments/audit_actual_cross_cofactor_marked_action.py) · [Recorded output](../experiments/actual_cross_cofactor_marked_action_results.json). These finite checks supplement the written proof and retain the scope recorded in their output.
