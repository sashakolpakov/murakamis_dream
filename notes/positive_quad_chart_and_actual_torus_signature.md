# A positive classical torus chart exists; the actual flow chart need not have its signature

28 October 2026. For EVERY supplied positive complete ideal
triangulation with the marked full-rank Lagrangian gluing rows,
positive quad rotations produce an invertible B chart. Its
fixed-radii positive angle chamber has a strictly concave whole
classical action, a unique global maximum, and absolute gradient
degree one. The action at that maximum is exactly the hyperbolic
volume in the stated normalization.

This closes a classical chart restriction. It does not carry the
original quantum cycle into that chamber. An exact calculation in
the original figure-eight flow chart shows why that transport is
necessary: its geometric fixed-radii angular Hessian is indefinite,
even after the two framing variables are fixed.

## 1. Positive quad rotations always permit an invertible B

Use the marks and rank data of the
[doubled Rivin optimizer](doubled_phase_rivin_optimizer.md).
For t positive tetrahedra choose compatible principal logs

    x_j=Log z_j, y_j=Log(1-1/z_j), Im z_j>0,
    A x+B y=c,

where (A B) has rank t and AB^T=BA^T. The independent edges
and the marked meridian supply these t rows. The affine constant
c retains the original edge windings, peripheral eigenvalue
characters and logarithmic lift. At completeness Re c=0.

At the positive point put tau_j=1/(z_j-1). The usual positive
Lagrangian pairing gives

    det(A+B diag(tau_j))!=0.                         (1)

Indeed its kernel would give a tangent (a,tau a) in the
complexification of a real Lagrangian, while its symplectic
pairing with its conjugate is a nonzero multiple of
sum Im(tau_j)|a_j|^2, strictly signed unless a=0.

Expand (1) multilinearly in its columns. At least one term
choosing either A_j or B_j in each position has nonzero
determinant. For each chosen A_j rotate just that positive
quad type by

    z'_j=z''_j=1-1/z_j,
    x'_j=y_j, y'_j=-x_j-y_j+i*pi.                   (2)

All three positive shape orders stay in the upper half-plane.
Substitution in the original equation gives, in this column,

    A'_j=B_j-A_j, B'_j=-A_j,
    c'=c-i*pi*sum_(rotated j) A_j.                  (3)

Unrotated columns are unchanged. Thus the selected A/B
transversal is exactly the new B up to column signs. It is
invertible. The local transformation is symplectic, so
AB^T=BA^T persists and C=B^-1 A is real symmetric.

This uses positive tetrahedral rotations, rather than an
uninterpreted formal Fourier swap. It supplies a positive
classical chart for every triangulation under the stated inputs;
it does not assert an exact finite quantum transform for (2).

## 2. A whole positive chamber has the desired global maximum

Drop the primes after (3). On the product of upper half-planes
use the standard dilogarithm branch and the explicit potential

    W(x)=sum_j Li_2(exp x_j)
        +(1/2)x^T(I-C)x+(B^-1 c-i*pi*1)^T x.       (4)

For these positive shape logs,

    Log(1-z_j)=x_j+y_j-i*pi,
    grad_x W=-B^-1(Ax+By-c).                       (5)

Thus the positive complete shapes are a critical point of (4).
Let rho=Re x_* and restrict to the entire fixed-radii positive
angle cube

    x=rho+i theta, 0<theta_j<pi.

The quadratic in (4) is real, so its imaginary part is affine
in theta. Direct differentiation therefore gives

    Hess_theta Im W
       =-diag_j Im(z_j/(1-z_j))
       =-diag_j [exp(rho_j)sin theta_j
                    /|1-exp(rho_j+i theta_j)|^2].  (6)

It is strictly negative definite on the WHOLE cube, not just
at its complete point. The gradient vanishes at theta_*, by
(5). Strict concavity makes theta_* the unique global maximum
of Im W on this cube and on its closure. For a boundary point,
the segment from theta_* stays positive until its possible last
endpoint, its second derivative is strictly negative, and W has
the required continuous boundary value. This also proves strict
inequality at every other boundary point.

The same argument works on every affine angle slice containing
theta_*. The negative gradient is injective on the positive
cube. Its degree at zero on any compact neighborhood containing
theta_* and no boundary zero is +1; the gradient itself has
degree (-1)^t. This is a CLASSICAL angle-gradient degree, not
the intersection number of an unspecified quantum source cycle.

## 3. The maximum's imaginary action is exactly the volume

Write x=rho+i theta and y=sigma+i gamma at a critical point.
The Bloch--Wigner identity on these positive branches is

    D(z_j)=Im Li_2(z_j)+rho_j(theta_j+gamma_j-pi).

Since d=B^-1 c=Cx+y at a critical point, direct expansion of
(4) gives the full boundary correction

    Im W_crit-sum_j D(z_j)
        =theta^T(C rho+sigma)
        =theta^T B^-1 Re c.                        (7)

At completeness Re c=0. Consequently

    max_(0<theta<pi) Im W(rho+i theta)
        =Im W(x_*)=Vol(X).                         (8)

For h=2pi*i/N the exponential exp(W/h) therefore has real
rate Vol(X)/(2pi) at that unique maximum. No numerical scalar
was fitted to obtain (8). The standard branch in (4) and the
affine marks in c were retained. An arbitrary additional
imaginary constant would change (8) and is not allowed in
this definition. Matching (4), including its constant, to an
actual quantum presentation remains separate work.

For the fixed positive chamber, strict concavity also supplies
a strict action gap outside every fixed neighborhood of the
complete point. It says nothing about other logarithmic
chambers, endpoint branches, or the original cycle's image.

## 4. The original figure-eight flow torus has a different signature

This is an actual phase calculation, not an arbitrary Airy
or formal-WKB example. Use the original balanced crossing
coefficients whose exact ratios and principal Hessians were
proved in [the actual stationary calculation](actual_geometric_normal_period.md).
The audit below imports its original closure embedding.

Take the figure-eight braid sigma_1 sigma_2^-1 sigma_1 sigma_2^-1
and its complete geometric parabolic representation

    t=(1-i sqrt(3))/2,
    mu_1=[[1,1],[0,1]], mu_2=[[1,0],[t,1]],
    mu_3=mu_1^-1 mu_2 mu_1 mu_2^-1 mu_1.

Use the regular original framing

    F=[[2,-1],[3,-3]]

and the same negative SL2 lift and sequential Gauss factorization
as that calculation. Its five free multiplicative phase variables
are the initial A_0 and the four crossing C_j. Fix log A_0 and
log C_1 as framing coordinates. This is a valid transverse slice:
their logarithmic Jacobian in the two original frame parameters
(r,s) at (2,3) has nonzero determinant

    15(-11sqrt(3)-i)/[4(155sqrt(3)+283i)].

Let H_normal be the original holomorphic phase Hessian in the
remaining log C_2,log C_3,log C_4 coordinates. Exact arithmetic
in Q(sqrt(-3)) gives

    -Im H_normal /sqrt(3)
      =[[-832683/405769,  1/52, -21/8],
        [         1/52,  -9/8,   3/8],
        [        -21/8,   3/8,  9/32]].           (9)

Its second and third diagonal entries have opposite signs.
Therefore the real exponent on the fixed-radii angular torus
has both an increasing and a decreasing quadratic direction
at this geometric point. Reversing the action convention
reverses both signs and cannot repair indefiniteness.

Thus free radii through this original geometric point do NOT
even give a local maximum in this valid original flow chart.
This does not rule out another framing or a source-preserving
canonical change of variables. It proves that positivity of a
different ideal triangulation cannot be silently transferred
to the original phase by changing radii alone.

## 5. What the classical result resolves and what is still missing

Equations (1)--(8) remove an invertible-B restriction and prove
the exact global positive-chamber convexity and calibration
needed on the classical target, for every supplied positive
complete ideal triangulation. The proof does not need equality
of the off-critical dilogarithm action with Rivin volume; its
angular Hessian and its critical value suffice.

Equation (9) shows that a source-preserving change from the
original quantum flow coordinates to that positive chart is
substantive. The original Cauchy cycle and every projection,
Gaussian, normal source, peripheral factor and matched residue
must pass through it. Neither the classical gradient degree nor
Rivin uniqueness computes that transport's global intersection
number. Controlling other chambers and endpoint pieces remains
necessary after the positive chamber is reached.

[The audit](../experiments/audit_positive_quad_chart_and_actual_torus_signature.py)
checks positive quad rotations and B selection, the calibration
identity, the exact actual figure-eight Hessian (9), and the
validity of its original framing slice. The all-triangulation
claims follow from the arguments above, not a finite list of
knot tests.
