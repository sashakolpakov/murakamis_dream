# Regular simple cut-wall stationarity is full stationarity

28 October 2026. A regular simple wall of the ACTUAL global radius
homotopy has a free radial coordinate. Together with its remaining
head angles, Gaussian paths and interior cap paths, its tangent
vectors span the full complex tangent space. Therefore complex phase
stationarity on this wall is automatically full holomorphic
stationarity. On a regular all-pole branch this removes the extra
"full critical" hypothesis from the regular simple-wall value bound.

This does not identify the original geometric-thimble coefficient.
It does not cover simultaneous corners of the one-parameter homotopy,
dependent walls, endpoints, nonsmooth flow cells or escaping variables.
Nor does a maximum of only the real exponential rate imply the
complex stationarity used here.

The [audit](../experiments/audit_regular_cut_wall_total_reality.py)
and [results](../experiments/regular_cut_wall_total_reality_results.json)
verify the implicit radial identity and the exact complex Jacobians,
including arbitrary radial dependence of the head radii and the
distinction between a free multiwall chart and a one-parameter corner.

## 1. The actual simple-wall radial coordinate is free

Use the global head-radius homotopy (4) in
[the exact cut-wall pushforward](actual_full_psi_cut_wall_pushforward.md).
For a simple ray pole, write

    T_j=Log t_j=tau+i epsilon*pi, tau=log r,
    U=Log A_j=a.Z+b.E+i*pi*nu,
    Z=rho+i theta.                                  (1)

Here a is the primitive nonzero integer head-incidence row; E denotes
the Gaussian log variables. The original atomic ratio connects two
different retained head segments. All other moment and Gaussian
parameters are denoted y for the moment.

The radii are independent of HEAD ANGLES. On a smooth flow cell set

    rho_s=(1-s)lambda_0(tau,y)+s lambda_*(y).

The pole's real equation is

    F(s,tau,y)=a.rho_s+Re(b.E)-tau=0.                (2)

A REGULAR SIMPLE crossing means F_s is nonzero and 0<s<1; all other
pole factors are regular on this local stratum. The real implicit
function theorem solves s=s(tau,y). Thus tau is a genuinely free
local parameter, not a constrained boundary value. In particular

    a.rho_tau=1.                                   (3)

The imaginary pole equation is
a.theta+Im(b.E)+pi*nu=epsilon*pi. It leaves n-1 independent
head angles. The dependence of lambda_0 on tau and on the other
moment radii causes no difficulty: it enters the implicit function
and off-diagonal derivatives, while (3) remains exact.

## 2. The unreduced residue chain is maximal totally real

Complete a to complex linear head coordinates (U,Y), keeping E as
an additional independent coordinate. Let V be a real basis of
ker a. On the wall choose

    theta=theta_0(E)+V phi, phi in R^(n-1),
    U=tau+i epsilon*pi.                             (4)

Every other moment T_k follows its original circle or ray, with a
nonzero tangent derivative; each Gaussian E follows a regular complex
path, and each interior cap variable p=2*pi*i*s follows its regular
complex path. Order the complex coordinates as

    (U, T_other, E, p, Y)

and the real parameters as

    (tau, moment parameters, Gaussian parameters, cap parameters, phi).

Their complex Jacobian is block triangular. Its diagonal consists of
1, the nonzero moment/Gaussian/cap path derivatives, and i C V,
where C is the chosen complementary head-coordinate matrix. The
matrix C V is invertible. Thus the Jacobian is NONZERO. All head-radius
derivatives in tau or the other base variables occur only in lower
off-diagonal blocks. The residue chain is therefore maximal totally
real in its complex residue manifold.

For a holomorphic phase S on that manifold, dS vanishing on all real
tangent directions consequently implies dS=0 on the full complex
tangent space. This follows by multiplying its complex derivative
row by the invertible Jacobian. It requires stationarity of the
COMPLEX phase, not just a stationary real-part envelope.

This unreduced statement concerns the phase with independent other
moment variables and their Cauchy poles. It does NOT yet identify it
with the nine-atom W(A), or infer actual knot holonomy before those
other atomic variables are pushed forward.

## 3. The regular all-pole branch gives the actual nine-atom conclusion

Now restrict to a regular local branch on which the OTHER atomic
moments are pushed to their Cauchy poles, with no additional local
wall crossing. In a regular simple cut stratum these other pole
arguments are off their negative-ray cuts. Their circle Cauchy
reductions can retain the head variables; locally freeze the radius
labels at the circle radii while taking these normal residues. Their
normal degree is one, but no global thimble-degree claim is made.

The remaining cycle has head profile rho(tau,E) independent of the
free head angles, with a.rho+Re(b.E)=tau. Its coordinates are now
(U,E,p,Y) and its parameters (tau, Gaussian paths, cap paths,phi).
The same block-triangular proof gives a nonzero complex Jacobian.
Thus an INTERIOR stationary point of the actual wall action W_m
on this regular simple-wall chain automatically satisfies

    gradient W_m=0.                                (5)

Here W_m is the genuine nine-atom action with its integer norm charge,
Gaussian and original coupled cap phases. This is precisely the
case covered by
[the calibrated critical regulator](actual_wall_critical_regulator.md)
and [the sharp representation-volume bound](regular_critical_values_and_representation_volume_bound.md).
Consequently every such regular simple-wall interior stationary value
satisfies

    |Im W_m|<=Vol(M).                              (6)

No extra independent "full critical" assumption is required for
these regular simple interiors. Additional local pole crossings,
rank-deficient Cauchy reductions and endpoints are excluded from
this inference.

## 4. Several genuinely free independent walls

The linear-algebra statement extends if k wall rows form a real
rank-k matrix A and the stratum ACTUALLY has k free radial variables
tau=(tau_1,...,tau_k), with

    A.rho+ell(E)=tau,  A.theta+arg(E)=constant.

Choose n-k remaining angles in ker A. In coordinates consisting of
the k logarithmic wall monomials, the Gaussian/cap variables and a
complementary head basis, the Jacobian has diagonal blocks I_k,
the nonzero path derivatives and i I_(n-k). It is invertible, so
restricted complex stationarity is full stationarity there too.

Rank A=k ALONE does not establish these free radial parameters in
the actual common tube current. A simultaneous k-fold intersection
of our SINGLE-parameter radius homotopy imposes k real modulus
equations on k radii and the one homotopy parameter. In general this
leaves only one free radial combination and k-1 further relations.
It is a corner stratum, not the free multiwall chart just proved.
Dependent walls, tangential crossings F_s=0, intersections on a flow
cell edge, terminal homotopy faces, cap/ray endpoints and escapes
still need their own source-preserving resolution. Nothing here
deletes any of their original currents.

## 5. Transverse intersections: no extra exact corner residue, but a growth caveat

There is a useful exact-current refinement. Suppose k distinct atomic
pole divisors meet the homotopy TRANSVERSELY as 2k real equations,
at a finite smooth point. Use their complex normal values q_1,...,q_k
as real normal coordinates on that homotopy. On a compact patch the
form has a smooth numerator divided by q_1...q_k.

In a region where all |q_j| are comparable to epsilon, a rounded
simultaneous tube boundary has 2k-1 normal real tangent directions.
Its pulled-back form scales at most epsilon^(2k-1-k)=epsilon^(k-1).
For k>=2 its integral tends to zero at fixed N. On each simple wall,
the other transverse factors 1/q_j are locally L1 because their
normal directions have two real dimensions. Hence the exact total
current can be described by simple-wall residues with these L1
kernels; there is no additional independent transverse corner
residue. This argument requires actual real transversality of the
restricted pole equations, not just distinct divisors or a claimed
independence of the moment labels.

This DOES NOT remove transverse intersections from asymptotic growth.
Local L1 meromorphic singularities can carry an exponential rate
without a full holomorphic critical point. For real a>0 and c,

    I_N=integral_R^2 exp(N(c-x^2-y^2+i*a*x))/(x+i*y) dxdy
       =2*pi*i/(N*a) exp(N*c)(1-exp(-N*a^2/4)).       (7)

The pole is locally L1, and its real normal map (x,y)->x+i*y is
transverse. The only regular holomorphic critical value of
S(Z)=c-Z_1^2-Z_2^2+i*a*Z_1 is c-a^2/4. On the complex pole divisor
Z_1+i Z_2=0 its restriction is c+a Z_2, with NO critical point.
Nevertheless (7) has exponential rate c, arising at the real chain's
pole intersection. Thus L1 integrability and absence of an independent
exact corner term do not give a sharp exponential bound from the
regular critical values alone.

For a direct proof of (7), use polar coordinates. The angular integral
is 2*pi*i J_1(N*a*r), obtained by differentiating the angular
definition of J_0. Integration by parts reduces the radial integral
to the two-dimensional Gaussian Fourier identity and gives
integral_0^infinity exp(-N*r^2)J_1(N*a*r)dr
=(1-exp(-N*a^2/4))/(N*a). Everything is absolutely integrable, including
the pole. The audit checks the resulting identity independently.

This is a LOCAL ANALYTIC countermodel, not a claimed knot-source
counterexample. It shows precisely why a further source identity or
phase-specific bound is required before eliminating transverse
meromorphic intersections from the remaining growth analysis.
