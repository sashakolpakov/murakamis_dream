# The representation-volume bound with general peripheral holonomy

28 October 2026. The independently proved smearing argument for
[boundary-parabolic representations](regular_critical_values_and_representation_volume_bound.md)
also bounds representations whose peripheral images preserve a geodesic
axis. Its proof needs integrable pullback volume and integrable finite-
radius face errors, rather than a globally bounded derivative of the
developing map. Axis-valued cusp maps supply exactly those properties.

Consequently the marked regulator of EVERY actual SL2(C) representation
of a finite-volume hyperbolic knot group has absolute value at most the
manifold volume. This includes unit meridian and nonunit longitude.
It supplies a geometric bound for a genuine peripheral-curve primitive;
it does not identify a quantum-A component with that curve, or estimate
the actual sourced quantum Green function.

## 1. Peripheral classification and an equivariant cusp development

Let X=Gamma\H3 be an oriented complete finite-volume hyperbolic
3-manifold and rho:Gamma->SL2(C), followed by its PSL2 action. Each
peripheral image consists of commuting matrices. If one has distinct
eigenvalues, both common eigenlines are preserved by every commuting
matrix, so the image preserves their joining geodesic axis. Otherwise
the image is central or has a nontrivial unipotent, whose commuting
matrices preserve its unique eigenline and act parabolically there.
Thus each cusp is either of axis type or of the boundary-parabolic
type already treated. Central images may be treated as axis type with
zero translation. No discreteness or irreducibility is required.

For an axis-type cusp use domain coordinates (w,y), with w in C,
y>Y and peripheral translations w->w+lambda. Choose an oriented
target axis gamma(t), parametrized by hyperbolic distance. Its
peripheral action is

    rho(gamma_0) gamma(t)=gamma(t+chi(lambda_gamma0)),

where chi is the real translation character. The rotations about
the same axis act trivially ON the axis. Extend chi from the lattice
to a real-linear function of w and set

    f(w,y)=gamma(chi(w)+log y).                        (1)

This is exactly peripheral-equivariant. It is smooth on finite cusp
truncations and its image has dimension at most one. Hence

    f^*(vol_H3)=0 on the ENTIRE axis cusp.              (2)

It need not be globally Lipschitz: its horizontal derivative in the
hyperbolic domain metric can grow like y. Equation (2), not a false
global Lipschitz assertion, is what is used below.

On parabolic cusps retain the old affine conical map, which has a
uniform hyperbolic derivative bound and integrable pullback volume.
Extend over the compact truncated core equivariantly by geodesic
interpolation on a finite triangulation and a collar. Contractibility
of the target gives the extension. The resulting f is locally
Lipschitz, has a finite derivative bound on every fixed metric
neighborhood of the truncated core, and has absolutely integrable
pullback volume on X. Define

    Vol(rho)=integral_X f^*(vol_H3).                   (3)

## 2. Choice independence and the actual regulator normalization

Two axis-cusp maps for the same noncentral peripheral image can be
joined by an equivariant axis-valued homotopy. Its boundary-torus
homotopy has zero 3-volume because it lies in that axis. Reversing
the chosen axis endpoint is also such a homotopy. For a central
peripheral image the maps may be independent of w; a homotopy then
has zero horizontal derivatives and again zero boundary 3-volume.
Parabolic-cusp choices have the vanishing boundary estimate already
proved in the linked note. Stokes on a truncated core therefore
proves that (3) is independent of these choices.

Map (1) tends to a peripheral fixed ideal endpoint as y tends to
infinity. Truncate an ideal fundamental chain and compare its
developed straightening with f by the same face-compatible geodesic
homotopy on the compact pieces. Internal faces cancel. The comparison
with the IDEAL straightening is not generally axis-valued on a cusp:
the other developed vertices need not lie on that axis. Its boundary
term instead vanishes by the following explicit estimate.

Put the selected fixed endpoint at infinity and the preserved axis at
horizontal coordinate zero. An ideal straightening can be parametrized
conically near that vertex, along the vertical geodesic rays to infinity.
On a finite triangulation of a fundamental cusp cross-section its map
has form

    f_cone(w,y)=(a(w),y b(w)), b(w)>0.                 (4a)

Here a,b and their piecewise first derivatives are bounded on the
fundamental cross-section, and b is bounded below there. Extend these
functions using peripheral equivariance. If that peripheral acts by
(z,y)->(l_gamma z,|l_gamma|y), their transformation rules are

    a(w+lambda)=l_gamma a(w),
    b(w+lambda)=|l_gamma|b(w).

The conical parametrization is chosen on the common cusp cross-section
and its faces before extending over the finite tetrahedral interiors;
thus adjacent straight faces use the same tail parametrization. It is
an allowed proper straightening of the same developed ideal chain.
For a tetrahedron with vertex infinity, its faces incident to that
vertex are vertical, and its deep tail is foliated by these vertical
rays; this gives the claimed conical choice after subdivision.

Join the axis map to (4a) by the EXPLICIT equivariant homotopy

    H_t(w,y)=(t a(w), y exp((1-t)chi(w)+t Log b(w))).

On a fundamental cross-section the horizontal coordinates and their
w,t derivatives are O(1), while its height is comparable to y and
its height derivatives are O(y). The hyperbolic volume form is
height^-3 dx_1 wedge dx_2 wedge dheight. Hence

    integral_(cusp torus at y times [0,1]) |H^*vol|
                                      <=C/y^2 ->0.   (4b)

This estimate is independent of any assertion of global Lipschitzness
or a zero comparison volume. On parabolic cusp tails use the old
vanishing horospherical estimate. Thus, with the SAME
marked fundamental-cycle convention,

    Vol(rho)=sum_Delta oriented Vol(straight_rho Delta)
            =sum_Delta D(z_Delta).                    (4)

Auxiliary ideal flags and degenerate tetrahedra are handled by the
finite-chain approximation used in the linked proof. This identifies
the absolute regulator normalization; it is not an arbitrarily
shifted primitive of a peripheral differential.

## 3. Finite-radius smearing without a global Lipschitz bound

Use the finite regular tetrahedron T_R and symmetric Lorentz
straightening/homotopy of the linked smearing proof. For each fixed
R its diameter is finite. That proof compares the developed
straight tetrahedron with integral_(g T_R) f^*vol by a sum of FOUR
oriented face-prism errors b_rho(g,face).

Their integrability is the only new issue. On an axis cusp, if a
domain face lies entirely in one lifted cusp horoball, both f on
that face and the straight interpolation of its three vertex images
lie on the SAME target axis. The complete face-prism homotopy is
axis-valued, so

    b_rho(g,face)=0 there.                            (5)

A cusp horoball is convex. For fixed R, every remaining domain face
which encounters an axis cusp and is not contained in it has its
frame basepoint in a FIXED metric neighborhood of the truncated core.
That neighborhood is compact modulo Gamma. On it f has some finite
Lipschitz bound L_R, so the finite-radius face-prism estimate of the
old proof bounds b there. On parabolic cusps the old global cusp
bound applies. Hence every fixed-R face error is absolutely
integrable on Gamma\Isom+(H3).

No bound uniform in R is asserted or needed. For EACH fixed R the
four ordered regular faces are congruent by orientation-preserving
isometries. Right Haar invariance makes their integrated error
values identical; their alternating sum is exactly zero. Fubini for
f^*vol is justified by its absolute integrability. With frame-fiber
Haar mass normalized to one, this gives

    Vol(T_R) Vol(rho)
       =integral_(Gamma\G) Vol(straight f(g T_R)) dg. (6)

Every target straight tetrahedron has absolute volume at most v3,
by the independently proved ideal-tetrahedron bound. The Haar mass
of the frame quotient is Vol(X). Therefore

    |Vol(rho)|<=v3 Vol(X)/Vol(T_R).

Let R tend to infinity, so Vol(T_R) tends to v3. This proves

    |Vol(rho)|<=Vol(X).                              (7)

There is no interchange of an unbounded family of face errors in this
last step: their cancellation was exact separately at every finite R.
Any joint projective shape limit of actual representation families has
the same bound, because each D extends continuously through 0,1,infinity.

## 4. Consequence and limitation for the actual A-curve route

On a genuinely identified peripheral representation curve, retain the
actual eigenvalues M and ell and the marked Bloch chain. Its already
proved boundary identity is

    delta beta=-2 M wedge ell.

The Bloch--Wigner differential gives, along |M|=1,

    dR=2 log|ell| dArg M
       =log|ell| dArg Y, Y=M^2.                      (8)

Thus R is an ABSOLUTELY normalized primitive of the logarithmic
longitude modulus on a specified representation branch, and (7)
bounds it by the knot volume, including along nonunit-longitude arcs.
For two points on that same branch,

    |integral log|ell| dArg Y|<=2Vol(X).              (9)

If the initial marked regulator is independently known to be zero,
the bound relative to it improves to Vol(X). A unitary meridian alone
does not make that initial regulator zero; the complete hyperbolic
representation is an immediate example.

This does NOT bound the integral of the pointwise largest root of an
arbitrary quantum-A symbol: that prescription may switch branches and
forgets their regulator constants. Nor does it identify the classical
symbol of an arbitrary all-level annihilator with a genuine peripheral
curve. The existing actual-state reciprocity theorem expressly makes
no such identification. Finally a quantum Green response requires its
original affine/normal source, finite-jet resonance and boundary
matching determinant. Bound (7) is a proved geometric input to that
problem, not a substitute for the missing sourced transfer estimate.
