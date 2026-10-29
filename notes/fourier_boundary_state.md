# Recovering the meridian state when the shape plane moves

Research note, 25 October 2026. This extends
`general_boundary_state_and_framing.md` to the other possible boundary
rank. We retain the original charged Andersen--Kashaev tensor and its
existing level convention, rather than replacing its tetrahedral function.
The new construction is inverse Fourier transformation of a specifically
leveled tensor. For ordinary fibers it is exactly the state already
constructed, including its Gaussian normalization.

Definitions used: Andersen--Kashaev,
[arXiv:1109.6295v2](https://arxiv.org/pdf/1109.6295v2), equations (4) and
(18), and the Fourier/Gaussian framework of Andersen--Kashaev,
[arXiv:1409.1208v1](https://arxiv.org/abs/1409.1208v1), Section 6.
All Fourier identities, phases, and analytic arguments needed below
are reconstructed here or in the preceding notes. We do not assume
an analytic theorem from either source.

## 1. The two ranks and a rational angle path

Let a globally branched ideal triangulation of a knot exterior in S^3
have a complete positive geometric structure. Use the independently
proved Fourier reduction and cochain identity:

    W=im S=im B^T, dim W=d=N-2k,
    G=-2Q+P_+, H=-G/2,
    L={(t,s):t in W, s-Gt in W^perp}=ker(A|-B).

Here the full A,B use N-1 independent edge rows and the unhalved
preferred-longitude row. The oriented meridian and longitude have
intersection 1, so

    A_m B_l^T-B_m A_l^T=-2.

Rank B_ed is either d-1 or d. The preceding ordinary-fiber theorem
treats d-1. We call d the moving-plane case, without assuming that
this is the same as any degeneration of the hyperbolic structure.

Choose a rational strict reference angle structure theta0, in units
of pi, with lifted angular meridian and longitude both zero. Existence
follows by rational density around the complete geometric angles.
Below physical angles are in radians. Write a for the first shape
angle and b'' for the angle of the literature double-prime shape:

    d0=pi*1-a0, W0=b0''-G d0.

The angular gluing equations are A_r a+B_r b''=nu_r. Their homogeneous
edge block has rank N-1. Adding both peripheral rows has rank N+1:
edge rows are symplectically orthogonal to both peripheral rows, while
their mutual pairing is -2. Therefore a rational angle variation
(a1,b1'') exists with

    A_ed a1+B_ed b1''=0,
    A_m a1+B_m b1''=0,
    A_l a1+B_l b1''=1.                                 (1.1)

Put d1=-a1, W1=b1''-G d1 and theta(lambda)=theta0+lambda*theta1.
For real lambda in a neighborhood of zero all physical angles remain
strictly positive, mu=0 and the angular longitude equals lambda.
The coefficients of theta1 are rational; lambda is measured in radians.

If rank B_ed=d-1, then d1 is in W, as proved in the ordinary-fiber note.
If rank B_ed=d, then d1 is outside W. Indeed otherwise
the projected edge identity gives B_ed W1=0, and B_l is in the row
space of B_ed. The longitude variation would then also be zero,
contrary to (1.1). Thus

    S_ext=[S,-d1] has rank d+1                          (1.2)

in the moving-plane case.

## 2. The exact level and inverse Fourier definition

Let T_b(lambda) denote the phase-free reduced integral with all
Jacobians, in the common-Phi convention:

    T_b(lambda)=c_X*(2pi sqrt(h))^(-d)
       integral_R^d exp[(i y^T H y+(W0+lambda W1)^T y)/(2pi h)]
                     product_j Phi_b(y_j/(2pi sqrt(h))) dz,
    y=i(d0+lambda d1)+S z,
    h=b^2/(1+b^2)^2.

For real small lambda the exact charged-kernel calculation gives

    Z_AK(theta(lambda);b)
       =exp(pi i N/12+i K0(theta(lambda))/h) T_b(lambda),

with the explicit K0 of the preceding boundary-state note. Define

    A_ref(lambda)=lambda W1.d0+(lambda^2/2)W1.d1,
    K(theta(lambda))=K0(theta(lambda))+A_ref(lambda)/(2pi),
    L_b(lambda)=exp[-i A_ref(lambda)/(2pi h)] T_b(lambda). (2.1)

Consequently L_b is exactly exp(-pi i N/12) times the existing AK
leveled tensor at level ell=-4K/pi. No scalar has been suppressed.
For real lambda this is an allowed real b-independent level.
Complex lambda below means analytic continuation of this precise
normalization from its real interval.

Define the meridian state by Fourier inversion:

    J_b(h,x)=1/(8pi^2 h) integral_R
                L_b(i tau) exp[-i tau x/(4pi h)] d tau. (2.2)

The factor 1/(8pi^2 h) follows from the Fourier frequency
tau/(4pi h). It is essential for comparison of states, although its
logarithm contributes no volume rate.

In the moving-plane case this is an ordinary absolutely convergent
integral. Substituting (2.1), set y=i d0+S z-tau d1 and

    I0_b(y)=exp[(i y^T H y+W0^T y)/(2pi h)]
                         product_j Phi_b(y_j/(2pi sqrt(h))).

Then the exact formula is

    J_b(h,x)=c_X/(8pi^2 h)*(2pi sqrt(h))^(-d)
       integral_R^(d+1) I0_b(y)
        exp{[i tau W1^T S z-i tau^2 W1.d1/2-i tau x/2]/(2pi h)}
                                                        dz d tau. (2.3)

Every extra quadratic coefficient is real. For real z,tau,x its
extra exponential has modulus one. On the horizontal plane Im y=d0,

    Re(i y^T H y+W0^T y)=b0'' . Re y.

Strict angles give 0<b0''_j<d0_j<pi. The exact Phi tails therefore
bound the modulus by C exp(-c sum_j |Re y_j|), for fixed b; derivatives
only add polynomial factors. By (1.2) this is an exponential bound
in |z|+|tau|. It proves absolute convergence, Schwartz regularity,
and holomorphy of (2.2) on a small horizontal x strip.

The same estimates on smaller real-lambda intervals give analytic
continuation of (2.1) to a vertical lambda strip. Explicitly, for
lambda=s+i tau, Im y=d0+s d1. The real terms from i tau W1.y
and -i A_ref cancel. The remaining modulus is exactly the charged
product for theta(s), and hence decreases exponentially in
|z|+|tau|, uniformly on smaller s intervals. Fourier inversion,
followed by a contour shift within that strip, proves exactly

    L_b(lambda)=integral_R J_b(h,x) exp(lambda x/(4pi h)) dx. (2.4)

Equivalently, this recovers the state from the normalized tensor.
Uniqueness is ordinary Fourier uniqueness. No imaginary-charge value
is postulated independently of its analytic continuation.

This also gives the local factorization for general angles, including
nonzero angular meridian mu. Let theta be near theta0, with angular
longitude lambda, and set

    d_bar=d0+lambda d1, W_bar=W0+lambda W1,
    Delta W=W_theta-W_bar,
    K(theta)=K0(theta)+[A_ref(lambda)+Delta W.d_bar]/(2pi). (2.5)

The fixed-longitude relation gives d_theta-d_bar in W and
Delta W in W^perp. Contour translation through the convex positive
angle segment changes T_b by precisely
exp[i Delta W.d_bar/(2pi h)]. Thus

    Z_AK(theta;b)=exp(pi i N/12+i K(theta)/h)
       integral_(R+i mu) J_b(h,x) exp(lambda*x/(4pi h)) dx. (2.6)

Locally the small mu contour lies in the holomorphic x strip above;
its translation changes no integral. Formula (2.5) is an explicit
real angle polynomial, and ell=-4K/pi is its existing AK level.
This supplies the general peripheral factorization near completeness,
rather than only the zero-meridian slice used to define the Fourier
transform. Continuation beyond these strips needs its own contour
control; no global continuation through singularities is asserted.

The factor two can also be checked directly for a variation at fixed
longitude: its symplectic pairing with theta1 gives

    Delta W.d1-W1.(d_theta-d_bar)=-mu/2.

The corresponding real tau term in the shifted z contour is -tau*mu/2;
the x contour Im x=mu supplies +tau*mu/2. They cancel exactly.
The audit verifies this identity on the entire balanced angle space,
with both peripheral variations free, before any specialization.

## 3. Agreement with the ordinary-fiber construction

Suppose rank B_ed=d-1 and retain p,beta from the preceding note.
Write d1=S eta1. The zero-meridian condition gives

    S^T W1=p/2, p^T eta1=-beta, W1.d1=-beta/2.

In (2.3) change z to z+tau eta1. The extra classical phase becomes

    i tau(p^T z-x)/2-i beta tau^2/4.

If beta is nonzero, its Fresnel integral gives precisely

    J_b(h,x)=1/(2pi sqrt(h)*sqrt(2i beta))
         integral exp[i(x-x')^2/(8pi beta h)] J_old(h,x') dx'.

The square root is the branch recorded in the ordinary-fiber note.
If beta=0, Fourier inversion gives delta(p^T z-x), recovering its
positive coarea fiber exactly. These operations may be justified by
a Gaussian cutoff and Schwartz Fourier inversion; no absolute
Fubini assertion is made for (2.3) in this noninjective case.

Also (2.1) reduces exactly to

    K=K_old-beta*lambda^2/(8pi).

Thus the inverse Fourier definition agrees with the previously
normalized meridian state in every ordinary-fiber chart. It is an
extension of the same construction, including its finite-b phase.

## 4. Independence of the auxiliary angle path

For vectors (a,c), where c denotes the double-prime angle, use
the symplectic form

    Omega((a,c),(a',c'))=a.c'-c.a'.

The kernel of the edge, meridian and longitude rows is the symplectic
dual of the edge-row space. It is isotropic with every solution of
the homogeneous edge equations. This follows directly by dimensions
and the peripheral pairing -2; it is not an additional NZ theorem.

Consequently, if delta d,delta W are angle variations with zero
meridian and longitude, then

    delta d in W, delta W in W^perp,
    delta W.d1=W1.delta d.                             (4.1)

Change theta1 by such a variation, keeping theta0 fixed. Contour
translation in W changes T_b(lambda) by exactly

    exp{i[lambda delta W.d0+lambda^2 delta W.d1]/(2pi h)}.

The change in A_ref is the same polynomial, by (4.1) and
delta W.delta d=0. Hence L_b and J_b are unchanged, not merely
equal in modulus. The argument first holds for small real lambda
where both paths have positive angles and then continues analytically.

Changing the reference theta0 to another strict rational reference
with mu=lambda=0 gives only

    J_new=exp[i (W_new-W0).d0/(2pi h)] J_old.             (4.2)

This is the previously recorded central phase. It is retained in
the level and leaves the boundary annihilator unchanged.

## 5. Exact classical equations and the extra saddle direction

The moving-plane action in (2.3) is

    F_ext(z,tau;x)=F0(y)+i tau W1^T S z
                               -i tau^2 W1.d1/2-i tau x/2,
    F0(y)=i y^T H y+W0^T y-i sum_j Li_2(-exp y_j),
    y=i d0+r, r=S z-tau d1.

Use the lifted shape deviations

    u=Log z_shape-i a0=-r,
    v=Log z_shape''-i b0'', D=v-G r.

Differentiation gives

    grad_z F_ext=i S^T(D+tau W1).

At a z-critical point rho=D+tau W1 is in W^perp. From (1.1) and
the projected cochain identities one obtains, with full lifted
holonomies H_r=A_r u+B_r v,

    H_ed=0, H_l=-tau.                                  (5.1)

For the remaining derivative,

    partial_tau F_ext
       =-i(b1'' . u-a1 . v)-i x/2.

The angle variation (a1,b1'') differs from
(B_m^T,-A_m^T)/2 by a symplectic dual edge vector, because its
longitude is one and its meridian is zero. Thus on H_ed=0,

    b1'' . u-a1 . v=-H_m/2,
    partial_tau F_ext=i(H_m-x)/2.                       (5.2)

All reference constants cancel in these formulas; the holonomies
are differences from their specified reference lifts. Hence the
full saddle equations are the edge equations with H_m=x, and the
boundary phase derivative is i H_l/2. The variable x really is
the meridian coordinate, without a zero-shear assumption.

At the complete shapes H_m=H_l=0. They lie in the lambda=0 plane
y=i d0+W by the preferred-longitude relation. Equations (5.1)--(5.2)
put their saddle at tau=0, including the new transverse direction.
Its phase value is the old F0 value, whose real part is -Vol(M).

## 6. Contour deformation and the volume theorem

Write d_geo-d0=S eta for the difference to the actual complete
geometric angles. Move the z contour through z+i s eta, 0<=s<=1,
keeping tau real. These are the convex strict angle structures with
zero meridian and longitude, so (4.1) applies at each s.

There is a potentially dangerous new linear tau term. It cancels
exactly: if delta W=W_s-W0 and delta d=S s eta, the real linear
change from F0 is tau*delta W.d1, while the cross term in (2.3)
contributes -tau*W1.delta d. Equation (4.1) makes their sum zero.
The modulus on every intermediate plane is therefore the charged
product for its positive angles. Its exponential tails are uniform
on the compact angle segment. The Phi poles stay outside
0<Im y_j<pi, and Cauchy side faces vanish. This justifies the
contour deformation for the complete d+1 dimensional integral.

On the geometric horizontal plane its real Hessian is

    -S_ext^T diag[Im(e^y/(1+e^y))] S_ext.

All diagonal entries are positive and S_ext has full column rank.
Thus this Hessian is negative definite. The added real quadratic
chirp affects only the imaginary part. The geometric critical
point is the unique maximum on this plane and has a nonzero
complex Gaussian coefficient. The previously proved uniform Phi
remainder and global linear tail estimates now give the ordinary
multivariate complex saddle asymptotic, in dimension d+1.

The prefactor in (2.3) is h^(-d/2-1), and the saddle factor is
h^((d+1)/2). The resulting polynomial scale is h^(-1/2), agreeing
with the ordinary-fiber normalization. In particular the state is
nonzero for all sufficiently small h and

    lim_(h->0+) -2pi h log|J_b(h,0)|=Vol(M).             (6.1)

Together with the ordinary-fiber theorem this proves (6.1) for
every globally branched complete positive geometric knot triangulation,
with its specified normalized tensor-derived meridian state. The
extra boundary-rank and zero-shear hypotheses have been removed.

## 7. Quantum operator and the limits of the result

Every Phi argument and Gaussian coefficient in (2.3) is rational,
apart from the recorded pi offsets and powers of h. The independent
finite-product, dimension-count and moment argument of
`general_annihilator_and_volume.md` therefore applies to this state.
It gives a nonzero annihilator and its primitive minimal generator
in the existing Andersen--Malusa b-shift algebra, after the stated
finite coefficient cover and descent. No Jones-polynomial input is
used, and no preservation of minimal degree under a fractional
Gaussian conjugation is assumed.

In its conventions

    Q=exp(-2pi b t), E f(t)=f(t-i b), t=x/(2pi sqrt(h)),
    EQ=qQE, q=exp(2pi i b^2).

Equations (5.1)--(5.2) give the classical branch

    Q=exp(-H_m), E=exp(H_l/2).

The previously proved uniform saddle substitution makes its
geometric peripheral factor divide the classical symbol of the
minimal annihilator. All generic peripheral coefficients must
still be retained. Equality to the entire A-polynomial, equality
to a Jones AJ operator, and an explicit coefficient list do not
follow from existence alone.

This is a theorem for the specified realizations. It does not
construct complete positive triangulations for all alternating
knots, treat flat tetrahedra, prove arbitrary global state
identifications, or establish an H-triangulation limit. Those
remain parts of the original objective. It also does not identify
the positive factorial sum with this complex state.

The exact matrix, polynomial, branch and Fourier-normalization
checks are in `experiments/audit_fourier_boundary.py`. They include
a six-tetrahedron 5_2 chart with rank B_ed=rank B=4, so that its
longitude really moves the shape plane. Its topology calibration
uses three explicitly recorded 2--3 moves; the local quantum move
identity is not inferred from this combinatorial calibration.

## 8. A certified moving-plane example

The fixture has ideal triangulation signature gLLPQcdefeffikdqhtk.
Its stacked face kernel has dimension k=1, its reduced dimension is
d=4, both B ranks are 4, c_X=1, and S_ext has rank 5. The rational
zero-meridian longitude variation can be chosen with d1=(1/2,0,0,0,0,0).
Thus this is an actual instance of (2.3), not just an abstract
symplectic matrix example.

In its native positive convention the six shapes are

    a, a, (a+2)/a^2, a-1,
    a^2/((a-1)(a+2)), -(a+1)^2/a,
    a^3+3a^2+2a+1=0.

Rouche's inequality on the rational disc centered at
(-337641021+562279512i)/10^9, of radius 10^(-8), has remainder-to-linear
ratio less than 0.044. Rational images and argument intervals put
every physical angle above 0.14 radians. All native edge and peripheral
products reduce exactly modulo this cubic; the argument intervals
fix the six edge branches at 2pi and both peripheral branches at zero.
The script separately verifies the literature shape equations after
the recorded vertex reorderings, without guessing a global conjugation.

Regina verifies each of the three legal 2--3 moves from the already
audited three-tetrahedron twist chart. Its initial combinatorial
isomorphism maps the independently marked twist meridian to minus
the source meridian, with zero longitude shear and zero additive
angle correction. The final preferred longitude also has a separate
integral dual-boundary certificate. These are topology and marking
checks; a complex quantum-state identity along this particular
sequence is not asserted without its level and move-phase audit.

The resulting hyperbolic volume is 2.82812208833078316276... . The
70-digit numerical diagnostic of the full five-direction saddle is
recorded separately from the rational geometry and matrix certificates.

## 9. A uniform boundary phase, independent of the angle path

For every balanced angle structure in the local factorization domain,
let d=pi*1-a, W=b''-Gd, with fixed zero-peripheral reference d0,W0.
If r is the number of tetrahedra, set

    L_tet(theta)=-pi*r/24+sum_j epsilon_j(c_j-b_j)/12,

where b_j denotes the middle physical angle. Then exactly

    K(theta)=L_tet(theta)
        +[d0.W-W0.d-d0.W0]/(4pi)-lambda*mu/(8pi).        (9.1)

The first two terms are affine in the angles; the only quadratic
peripheral term is universal. The auxiliary path theta1 has disappeared.

For the proof, the charged phase and W=2Qd-C reduce to
K0=L_tet-d.W/(4pi). Write

    d=d0+lambda*d1+delta d,
    W=W0+lambda*W1+delta W.

At fixed longitude, delta d lies in the allowed shape subspace,
delta W annihilates it, and the peripheral pairing gives

    delta W.delta d=0,
    delta W.d1-W1.delta d=-mu/2.

Expansion of (2.5) cancels lambda^2. Its remaining quadratic term is
lambda*(delta W.d1-W1.delta d)/(4pi), giving (9.1).
This is the boundary Heisenberg term hidden in the separate chart
normalizations. It connects the continuous level with the structural
period line of `heisenberg_period_torsor.md`. The identity retains
the full angle polynomials before any peripheral specialization.
