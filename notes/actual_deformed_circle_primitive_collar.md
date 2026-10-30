# The primitive collar of the actual deformed circle pattern

30 October 2026. Independently reviewed. The deformed marked
circle pattern supplies the flags that the limiting source quadratic
loses at a two-line triangle. This note calculates its ORIGINAL ordered
crossing-disk sidepairing, including the primitive meridian, half twist
and selected eigenflag. The result uses the specified sidepairing, not
the product of two shaded reflections. Global representation assembly
and the full regulator identification remain separate.

## 1. Keep the original order and corners

Use the actual labeled pattern of
[the marked reconstruction](actual_marked_deformed_circle_pattern.md).
At one matching edge its input triangle is (x,b,y), and its output
triangle is (x,c,y); the letters denote the curvatures of their actual
white circles. First calculate a finite-circle model with the specified
side signs. Section 5 verifies the signs and limits for the actual
marked pattern; positivity of the radii alone does NOT fix those signs.
Put

    delta=1/2-mu, s=sin(pi delta), c0=cos(pi delta),
    A=x+y, D=A^2-4xy s^2,
    T_b=sqrt[bA+xy+b^2s^2], B_b=A+2bs^2, E_b=B_b+2sT_b,

and similarly for the middle circle c. Roots are positive at complete
positive data and continued holomorphically near delta=0. Thus

    E_b(delta)E_b(-delta)=D,
    R0=E_b E_c/D.                                      (1)

These are precisely the continuant roots and channel ratio of the
[original coupled source](actual_whole_source_coupled_face_difference_system.md),
with input b and output c, including its original beta and forced
polynomial normalization.

Write r_f for reflection in white circle f in this paragraph only.
The actual prefix convention is explicitly proved in
[the original white-prefix dictionary](actual_right_angled_selected_framing_obstruction.md),
section 3:

    A_in=r_b r_x, B_in=r_y r_b, P=B_in A_in=r_y r_x,
    A_out=r_c r_x, B_out=r_y r_c.                       (2)

It is not the reversed product r_x r_y. The original corner labels are

    C1=x tangent b, C2=b tangent y,
    C0=x tangent c, C3=c tangent y.

The actual even disk glues the shaded b-side to the c-side by
C1->C0 and C2->C3, as in
[the labeled cut quotient](general_augmented_plat_matching_geometry.md),
section 4, equation(3). These corners, not an unlabeled metric rectangle,
fix the sidepairing used below.

## 2. Exact shaded-circle radii

For small real delta>0 put the outer centers at 0,L on the real axis,
with radii r_x=1/x,r_y=1/y and

    L^2=(r_x+r_y)^2-4r_xr_y s^2=D/(x^2y^2).

Their intersections are P_plus=u+iv and P_minus=u-iv, where

    u=(L^2+r_x^2-r_y^2)/(2L),
    v=2r_xr_y s c0/L=2s c0/sqrt(D).                    (3)

The input middle circle lies on the positive side of the outer center
line. Its center p_b+iq_b and radius r_b=1/b obey

    p_b=u+r_b(r_x-r_y)/L,
    q_b=2c0 T_b/(b sqrt(D))>0.

The output middle circle uses the negative side, with the same formula
for p_c and q_c=-2c0 T_c/(c sqrt(D)). These are the oriented model's
two shaded sides. The signed variant and its actual complete-word
calibration are retained in section 5.

The circle orthogonal to the three input white circles has center
u+i t_b and squared radius t_b^2-v^2. Orthogonality to the middle circle
gives exactly

    t_b=[r_x(r_x+r_b)-u p_b]/q_b
        =c0 B_b/[sqrt(D) T_b].                       (4)

The output shaded circle has t_c=-c0 B_c/[sqrt(D) T_c]. These formulas
follow by subtracting squared center-distance equations; in particular
they retain the actual side signs. The identity
B_b^2-4s^2 T_b^2=D verifies their normalizations.

Use the Möbius coordinate

    w=(z-P_plus)/(z-P_minus).

Both outer circles become straight lines through 0 and infinity.
On the shaded circle with center u+it, its equation gives

    |w|^2=(t-v)/(t+v).

Consequently the INPUT and OUTPUT shaded circles become concentric
circles of radii rho_b,rho_c with

    rho_b^2=(B_b-2sT_b)/(B_b+2sT_b)=D/E_b^2,
    rho_c^2=(B_c+2sT_c)/(B_c-2sT_c)=E_c^2/D,
    rho_c/rho_b=E_b E_c/D=R0.                          (5)

The square roots in (5) are positive in this real configuration.
Equation(5) is an algebraic identity with the stated selected branches;
it continues holomorphically on the small complex parameter germ.

## 3. The primitive sidepairing and its selected flag

The two transformed middle circles are tangent to the same two outer
lines and lie in the SAME selected wedge. To check the latter rather
than assume it, as delta tends to zero the coordinate w tends to1 at
every original point away from the outer tangency. Both entire middle
circles are separated from that tangency, and their transformed circles
are therefore small circles near1 in the same wedge. This persists
for sufficiently small positive delta.

In one such wedge, a circle tangent to both boundary lines has center
on its fixed angle bisector. Its center distance and radius are fixed
positive multiples of the radius of its concentric orthogonal circle.
Hence the POSITIVE dilation

    C_w(w)=R0 w                                        (6)

maps the entire input middle circle to the output middle circle, and
the shaded b-circle to the shaded c-circle. It preserves EACH outer
circle and sends their respective contact points C1->C0 and C2->C3.
This is exactly the original even shaded sidepairing. The alternative
negative dilation moves the middle circle to the opposite wedge and
does not give this corner pairing. The reverse disk path gives C^-1.

This argument also distinguishes the primitive map from a doubled one.
Reflection in |w|=rho is w->rho^2/conjugate(w). Thus the composition of
the TWO shaded reflections has multiplier R0^2, not R0. The original
disk pairing (6) is a single sidepairing within its projection copy;
it must not be replaced by that doubled reflection word.

For the order (2), the actual determinant-one outer product is

    P=1/(r_x r_y) [[r_y^2-L^2, L r_x^2],
                         [-L,             r_x^2]].     (7)

It has trace -2cos(2pi delta). At P_minus its eigenvalue is

    J=-exp(-2pi i delta),

whereas at P_plus it is J^-1. Indeed the lower row evaluated on
(P_minus,1)^T gives
[-L P_minus+r_x^2]/(r_xr_y)=-cos(2pi delta)+i sin(2pi delta).
The coordinate w sends the J-line to infinity. Therefore (6) has
eigenratio R0 ON THE ORIGINAL J-LINE, as required by the source.
Reversing the product in (2) would exchange this ratio with its inverse.

In the original coordinate the projective map (6) is exactly

    C=I+(R0-1)/(J-J^-1) (P-J^-1 I).                  (8)

It has eigenvalues R0 and1 and determinant R0. Because it preserves
the two outer circles and maps b to c, the original ordered meridians
satisfy

    C A_in C^-1=A_out, C B_in C^-1=B_out.             (9)

Thus (8) is the geometric sidepairing with the SAME full ordered
character map as the original source; trace matching alone was not
used to identify it. All formulas first hold for small positive real
delta and positive circle data, then as holomorphic identities.

At completeness put

    Cscalar=pi(T_b(0)+T_c(0))/(x+y).

Then R0=1+2Cscalar delta+O(delta^2) and
J-J^-1=4pi i delta+O(delta^3). The apparent quotient in (8) is
removable, and its limit is

    C=I+(Cscalar/(2pi i)) (P+I).                     (10)

This is the nontrivial parabolic collar already fixed by the actual
complete rectangle. It is not inferred to be identity from R0=1.

## 4. Primitive meridian and the retained half twist

The actual crossing-disk threading word is [2,1,1,2]. Its original
Hurwitz calculation in
[the local critical-character map](actual_augmented_plat_local_critical_character_map.md),
section 4, gives pure physical transport by C_aux^-1, with disk
longitude P=BA and no auxiliary meridian detour. Equation(9), with
its checked original corner order, therefore identifies C with that
pure transport in the untwisted case. Normalize its SL2 lift by
sqrt(R0), selected to equal1 at completeness. On the J-line the
primitive auxiliary meridian eigenvalue is then M_aux=R0^-1/2.

The actual positive main Hurwitz move is
(A,B)->(A^-1 B A,A). It is simultaneous conjugation by P^-1-I,
whose eigenratio on the J-line is -J^-1. Retaining the source half
twist epsilon in {0,+1,-1} thus gives the SAME original convention
as the source equation:

    M_aux^-2=R0(-J)^epsilon.                          (11)

No unrecorded half-longitude loop is inserted. The square root defining
M_aux is selected by the original complete meridian lift; reversing
the selected eigenflag or the collar path reverses the indicated
logarithms, rather than changing this convention silently.

On the logarithmic branches centered at completeness,

    U_aux=2Log M_aux=-Log R0-epsilon Log(-J),
    V_long=2Log(-J)=-4pi i delta.                    (12)

In particular dV_long/dU_aux at zero is
2pi i/(Cscalar-pi i epsilon), the independently proved primitive
rectangle modulus. This is a consequence of the ordered calculation;
it is not used as a substitute for it.

## 5. Common marked-line limit

The [marked pattern theorem](actual_marked_deformed_circle_pattern.md)
has already constructed the TWO marked lines, the common strip width,
and their selected matching eigenline germs. They provide the geometric
data absent from a collapsed 200 source root. We use those data here;
no finite Bessel logarithmic derivative is interpreted as a classical
eigenflag.

There is one explicit regularization for the whole finite pattern.
In its normalized strip 0<Im z<1 take real t->0 and

    g_t(z)=z/[1-t z+i t/2].                           (13)

Its pole 1/t+i/2 lies between the two marked halfplanes and outside
every finite white disk for sufficiently small t. Every transformed
outward disk is therefore bounded, with positive radius. In particular
both marked curvatures are positive and O(t^2); every other curvature
has its original positive limit. The same g_t transforms ALL circles,
original contact labels, sidepairings and selected flags, and g_t->Id.
It is not a collection of independent local conjugations.

An important signed correction is necessary here: making all disks
bounded does NOT imply that the input and output middle centers lie on
opposite sides of their outer center line. If their actual side signs
are sigma_b=sign(q_b) and sigma_c=sign(q_c), the same calculation gives

    rho_f=(sqrt(D)/E_f)^sigma_f,
    R_signed=(E_b/sqrt(D))^sigma_b
                         (E_c/sqrt(D))^(-sigma_c).      (13a)

For example both centers can lie on the negative side after a common
Möbius transformation. Equation(13a), not an unsigned application of
(5), is used at every finite regularization parameter.

Here is the actual planar and word calibration. At completeness all
transformed disks are bounded and disjoint. Each straight tangency edge
between their centers lies in its two disks, so these edges give the
original planar rotation system. The bounded center triangles have its
consistent orientation; only the outer triangle has the opposite
orientation. The pole in (13) is in a far-end gap of the original strip.
Every one-line/two-finite gap has bounded horizontal extent, while the
two unbounded gaps are precisely the triangles containing BOTH marked
line faces u,v. Thus the exceptional outer triangle is a uv triangle.
Its matching edge is not uv, since uv is MAIN, so its limiting source
type is 200 or002 and its T_f tends to zero. On that triangle
E_f/sqrt(D) tends to1, whichever side sign occurs.

The global choice of the remaining orientation is fixed by the ORIGINAL
complete collar word, rather than by a desired sign for (1). The direct
primitive translation calculation in
[the channel-Hessian note](actual_augmented_plat_channel_hessian.md),
section 3, together with the actual rectangle in
[the external reflection note](actual_external_circle_reflection_and_cusp.md),
section 4, gives

    C_complete=I-i(P+I)/(2c_geom),
    c_geom=(x+y)/(T_b(0)+T_c(0))>0.                  (13b)

ALL curvatures and T terms in (13b) refer to the ORIGINAL MARKED-STRIP
LIMIT after t->0, not to arbitrary finite g_t curvatures. At finite t
one must keep (13a), including its possible flipped sign. First take
the signed complete-collar coefficient back to the marked strip, and
only then compare it with (13b).

The first identity is the literal threading/longitude translation
calculation there, independent of its subsequent Hessian conclusion.
The signed model (13a) has limiting coefficient
-i[sigma_b T_b(0)-sigma_c T_c(0)]/[2(x+y)]. Comparing with (13b)
forces sigma_b=+1 whenever the MARKED limiting T_b(0)>0 and
sigma_c=-1 whenever the marked limiting T_c(0)>0. A zero limiting
T term has no sign constraint and contributes nothing. Reversing
the copy or collar path reverses both the ordered word and this
calibration; it is not an independent local choice.

The signs remain constant for small real delta. Indeed the squared
height of every finite center triangle is the strictly positive
4cos^2(pi delta) T_f^2/[f^2 D], so no nondegenerate center triangle
can reverse along this deformation. The exceptional uv triangle has
T_f=0 in the actual line limit for every delta. Thus (13a) converges
to EXACTLY R0 in (1) for small real delta. The regular three-point
map below then supplies its holomorphic extension; no separate uniform
square-root assertion at the disappearing T term is required.

Conjugating the SIGNED finite-circle sidepairing back by g_t and letting
t->0 therefore gives (8),(9) for the actual line pattern. The limit is
regular: the
three original labeled points C1,C2 and the selected matching fixed
point are distinct at completeness, as are their images C0,C3 and
that fixed point. Their unique Möbius map is holomorphic on a common
neighborhood. A point equal to infinity is handled in homogeneous
coordinates. It is precisely the sidepairing already determined in
section 3. This also proves existence of the common-conjugated limit,
rather than selecting a root of a boundary polynomial after the fact.

No matching edge has both outer faces equal to the two marked faces:
their common edge is MAIN and the white sphere is simplicial. Thus
A=x+y remains positive at every matching edge, even at a two-line
triangle. The functions D,E_b,E_c and R0 therefore have the stated
nonzero holomorphic limits near delta=0. For a 200 triangle T_b=0,
take E_b=A exactly. Its missing flag has already been supplied by the
marked line geometry and the common-conjugated map. The actual upper
and lower line eigenflag adapters are those of the marked pattern
theorem, with no independent reflection of a source head.

The resulting identities extend to small complex delta by holomorphy
in the constructed pattern. The geometric configuration, not the
collapsed scalar root alone, is what justifies that extension.

## 6. Scope

This proves the actual local primitive collar, its ordered meridian
transport, selected flags, half-twist and logarithmic normalization
on the marked deformed pattern. The matching ratio is exactly the
source ratio E_b E_c/D, including the marked zero-face limits.

Global representation relations, comparison with the chosen marked
geometric deformation, and integration of the full regulator still
require the separate assembly. Ordinary-color subsets and the full
filled-source gap also remain outside this local theorem.

Focused [collar audit](../experiments/audit_actual_deformed_circle_primitive_collar.py),
with [saved results](../experiments/actual_deformed_circle_primitive_collar_results.json):
author PASS. It checks 11 exact radius/selected-flag identities,
60 ordered-product and eigenflag identities, 24 literal contact
pairings, 12 primitive-versus-double-reflection factors, 36 actual
threading/half-twist words and their primitive eigenvalues, 18 marked
200 maps/flags, and 24 common circle regularizations at 80 digits.
Twelve regularizations genuinely flip the center triangle: the signed
formula passes while the unsigned finite formula fails. These checks
retain the marked-line correction rather than hiding it in a limiting
sample.

Independent root full analytical review, audit-code review and fresh
80-digit replay: PASS. The final proof explicitly takes the signed
regularization back to the original marked-strip limit before applying
the complete-word sign calibration; it does not apply the unsigned
formula to a flipped finite compactification.

Independent geometry full analytical review and fresh redirected
80-digit replay: PASS. This includes the original ordered P/J flag,
literal corner pairing, primitive-versus-double-reflection distinction,
threading/Hurwitz word, signed regularization and regular three-point
line limit. All stated audit counts were reproduced. These reviews
establish the local collar theorem with its marking; global assembly
and the source qualifications in section 6 are unchanged.
