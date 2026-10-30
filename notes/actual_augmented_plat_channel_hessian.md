# The endpoint channel Hessian is the inverse primitive cusp shape

30 October 2026. The actual normalized augmented-plat phase has a
nondegenerate channel block at every regular complete geometric point.
After eliminating its two local q-Hahn variables on their recorded
critical sheets, ALL channel/magnetic mixed second derivatives vanish
at the complete channel endpoint. The diagonal entries are exactly

    H_(xi_i,xi_i)=-4pi i/tau_i,                         (0)

where tau_i is the ACTUAL oriented primitive crossing-circle cusp
shape, longitude translation divided by meridian translation. Hence
each entry has strictly negative real part. This is a source theorem
for every original augmented plat admitting the stated regular complete
geometric chart, at any fixed width, with any retained half-twist pattern.

The proof identifies the cusp shape directly from the actual meridian
and longitude MATRICES. It does not infer that marking by matching a
Hessian. It also does not assert that the remaining magnetic Hessian is
nondegenerate after removing framing directions, or that a finite source
cycle contributes a nonzero Gaussian amplitude.

## 1. A local critical reduction must keep its integer characters

Use the fully normalized local phase Theta_epsilon and its rational
critical map from
[the actual character calculation](actual_augmented_plat_local_critical_character_map.md).
Write y for the magnetic variables (tau,u,v), xi for the folded channel,
and alpha,beta for the two internal q-Hahn variables. The high physical
degree chart uses its proved affine adapter; its phase remains the same
function of these LOW coordinates, not the same function with the
physical pair product substituted for T.

At a regular complete point J=exp(2pi i xi)=-1, both internal critical
quadratics have simple roots. The holomorphic implicit-function theorem
gives their chosen continuations alpha(y,xi), beta(y,xi) in a small
logarithmic neighborhood. The exponentiated equations alone give

    Theta_alpha=2pi i n_alpha,
    Theta_beta=2pi i n_beta,

with locally constant integers on these roots. Retain these characters
and put

    Theta_tilde=Theta-2pi i(n_alpha alpha+n_beta beta).

Then its two internal derivatives are EXACTLY zero. Define the
root-reduced phase Theta_bar(y,xi) by substituting these roots into
Theta_tilde. Envelope differentiation now gives

    exp(partial_xi Theta_bar)=R_epsilon
                             =R0(-J)^epsilon.          (1)

Reducing an unadjusted phase whose internal derivatives are nonzero
integer characters would add spurious alpha_xi and beta_xi terms.
No choice of these local characters is, by itself, a proof that the
corresponding Poisson sector contributes to the original finite sum.

## 2. Endpoint tangential derivatives vanish identically

The actual source identities hold on the ENTIRE endpoint root chart:

    R0|_(J=-1)=1,
    C=I+bH, H=P+I, H^2=0,
    (dR0/dJ)|_(J=-1)=2b.                              (2)

The derivative in (2) follows the implicit internal roots, holding the
magnetic variables fixed. In particular it is not a derivative taken
with their exponential coordinates Z,W incorrectly frozen. The scalar b
is recovered from the actual ordered input/output meridians by

    b=Tr([H,A_in] A_out)/32.

The endpoint regulator note's
[rational chart](actual_augmented_plat_endpoint_regulator.md), with
Z=(a-1)/(a+1), W=(b0-1)/(b0+1), gives explicitly

    b=(2Ta b0-Ta-Tb0+a+b0-2)
                      /[2(T+1)(a-1)(b0-1)].           (3)

Here b0 is a chart parameter, not the transport coefficient b. Formula
(3) holds in both physical degree charts. The audit differentiates the
original general-J rational expression for R0 using
Z_J=-P_J/P_Z and W_J=-P_J/P_W, and checks (2) exactly over Q(T,a,b0).

Because (-J)^epsilon=1 at J=-1, equation (1) implies

    partial_xi Theta_bar(y,1/2)=2pi i n_xi             (4)

for one LOCALLY CONSTANT integer n_xi on each connected marked endpoint
chart. It does not automatically imply that this derivative is zero.
Nevertheless differentiating (4) in ANY magnetic tangent direction gives

    partial_y partial_xi Theta_bar=0.                 (5)

This is an identity along the whole endpoint chart, not a numerical
vanishing at the geometric point alone. Finally dJ/dxi=-2pi i there,
so (1),(2) give

    partial_xi^2 Theta_bar
        =-2pi i(2b-epsilon)
        =-4pi i(b-epsilon/2).                         (6)

The high-degree adapter is independent of xi. Therefore (5),(6) remain
valid in the actual high physical coordinates.

## 3. The primitive cusp translations fix the factor and sign

The collar is the ORIGINAL threading word [2,1,1,2], followed by the
retained main half twist R^epsilon. The
[proved endpoint reconstruction](actual_augmented_plat_endpoint_regulator.md),
section 3, supplies its raw trace -2 auxiliary meridian

    C_aux,raw=-[I+(epsilon/2-b)H].                     (7)

Thus the actual trace +2 meridian is

    mu=I+(epsilon/2-b)H.

The actual disk-framed preferred longitude is P=BA, with no meridian
power inserted. Since P=-I+H, its centered trace +2 representative is

    lambda_centered=-P=I-H.                           (8)

Changing a matrix by its central minus sign changes no projective
translation. Conjugate their common parabolic fixed point to infinity.
The nonzero nilpotent H then has form [[0,h],[0,0]], h!=0. Equations
(7),(8) say that the actual translations are

    translation(mu)=(epsilon/2-b)h,
    translation(lambda)=-h.

Both primitive paths retain their original collar orientations. Therefore

    tau_geom=translation(lambda)/translation(mu)
             =1/(b-epsilon/2).                       (9)

This proves the inverse cusp relation DIRECTLY at the complete point;
no nearby deformation theorem or guessed cusp potential is used. With
the positive orientation I(mu,lambda)=1, Im tau_geom>0. Substituting
(9) into (6) proves (0), including

    Re(-4pi i/tau_geom)
                   =-4pi Im(tau_geom)/|tau_geom|^2<0.  (10)

As a sign check, an actual rectangular crossing-circle cusp with
c=cot(pi x)>0 has, in the SOURCE half-twist convention,

    tau_epsilon=2ic/(1-epsilon ic),
    b=1/(2ic),
    H_xixi=-2pi/c+2pi i epsilon.                       (11)

Source epsilon=-1 is the geometric '+' collar of the matching-graph
geometry note; the two notations should not be silently interchanged.
The parameter x in (11) is a geometric rectangle parameter and is not
being identified with a general Newton source coordinate.

## 4. The full original plat retains this diagonal block

Sum the root-reduced phases of all original circle coupons, together
with the original cup, cap, marking and exterior phases. Eliminate only
the affine physical-wire degree equations, using coordinates independent
of the channel variables. Denote the resulting local phase by

    F(y,xi_1,...,xi_r).

The remaining y coordinates are the original magnetic degrees of freedom;
no assertion about their Hessian or framing quotient is made. Cups/caps
and the degree constraints introduce no additional channel dependence.
At the full endpoint xi_i=1/2, equations (5),(6) give exactly

    F_(xi,y)=0,
    F_(xi_i,xi_j)=-delta_ij 4pi i/tau_i                (12)

at a regular complete geometric point. Off-diagonal channel terms vanish
because each local reduced coupon contains only its own channel. The
mixed block remains zero under the actual affine degree restriction.
In particular the channel block is invertible with negative definite
REAL PART in these actual channel coordinates, independently of any
magnetic degeneracies.

For clarity this statement concerns the marked phase. The integers in
(4) remain locally constant, and the original normal equation becomes
stationary only in the corresponding specified Poisson sector. Equation
(12) does not choose that sector's coefficient in the finite source.

## 5. A local channel elimination, with the color normalization retained

There is a limited but useful implicit-function consequence. Subtract
the recorded constants 2pi i n_i xi_i from F, and add the actual positive
cosine-branch color coupling

    -2pi i sum_i (xi_i-1/2) chi_i.                    (13)

At chi=0 every point y of a sufficiently small endpoint chart has the
channel stationary solution xi_i=1/2. By (12) and continuity, the
holomorphic implicit-function theorem solves all CHANNEL equations
uniquely for xi=xi(y,chi), near the geometric point. This eliminates
only those variables. It does not solve the remaining y equations.

At the complete geometric point,

    partial xi_i/partial chi_j=-delta_ij tau_i/2.      (14)

The resulting channel-eliminated phase f(y,chi) obeys

    f_(chi_i,chi_j)=delta_ij pi i tau_i,
    f_(chi,y)=0,                                     (15)

at chi=0. Replacing the cosine sign changes both first derivatives and
leaves (15) unchanged. For the displayed positive cosine branch the physical similarity logs are
U_i=-2pi i chi_i and V_i=4pi i(xi_i-1/2), so (14) also gives
V_i/U_i=tau_i to first order, with the original inverse-meridian sign.

The transfer convention writing f''=2pi i tau_packet therefore has

    tau_packet=tau_geom/2,

as already required in the explicitly solved Conway sources. There is
no additional factor of two in (0) or (15).

What this removes is a genuine local obstruction: the folded channel
normal is nondegenerate, its sign is controlled, its mixed second-order
coupling to the magnetic coordinates vanishes, and its peripheral
coefficient is correctly normalized. What remains includes the magnetic
critical scheme and its genuine gauge directions, a selected complex
magnetic branch, the physical support/Poisson cycle, boundary and alias
estimates, and a nonzero amplitude. The physical channel endpoint is
still an endpoint of the finite folded summation domain; this theorem
does not turn it into an interior finite-state saddle.

Audit: [exact cusp and channel calculation](../experiments/audit_actual_augmented_plat_channel_hessian.py),
[results](../experiments/actual_augmented_plat_channel_hessian_results.json).

Independent character/current review: full analytical read and fresh
audit PASS. The review checked the retained internal integer characters,
implicit root derivatives, actual primitive cusp orientation and signed
shear, both physical adapters, the channel-independent affine degree
restriction and the channel-only implicit-function theorem. Six cusp
cases and three rectangle/color-Hessian checks passed. No magnetic
quotient rigidity, physical cycle or global source estimate is inferred.
