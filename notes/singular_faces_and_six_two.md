# Fourier reduction of singular face matrices and the 6_2 state

Research note, 25 October 2026. The local operators are the published
charged Andersen--Kashaev kernels, with their Fourier and normalization
identities independently proved in `faddeev_pentagon_audit.md`. We evaluate
those kernels before extracting a boundary fiber. This does not replace
them with the positive factorial model, and does not require inversion
of the full face matrix.

The results are a general reduction and volume theorem under explicit
rank hypotheses, and complete finite geometric/peripheral certificates
for its application to 6_2. Uniform membership for all two-bridge knots,
global connecting paths, and the all-alternating conjecture remain open.
The subsequent [cohomology proof](automatic_face_regularity.md) shows that
both Fourier rank hypotheses hold for every globally branched ideal
triangulation of a knot exterior in S^3. Thus they are no longer additional
conditions in that setting.

## 1. A singular face matrix can give a regular reduced integral

Use N ordered tetrahedra, 2N paired faces, signs epsilon, and selectors
X_i. Put

    D=X_0-X_1+X_2, R=X_2-X_3, E=diag(epsilon).

The existing full charged kernel contraction is

    integral delta(Dx) product_j f_j(-(Rx)_j)
                 exp[-2pi i (X_0x)^T E R x] dx,            (1.1)

where f_j is the positive charged function or its conjugate. In the
previous proper calculation, t=E R x gave an invertible coordinate
system on ker D. That is sufficient but not necessary.

Assume rank D=N. Choose rational matrices G,F with DG=I and columns
of F a basis of ker D. Write x=G u+F z, and define

    T=E R F, U=X_0 F, k=dim ker T, rank T=N-k.

Choose K a basis of ker T and a complement Z, so [Z K] is invertible.
Writing z=Z a+K b gives t=P a, P=T Z. The phase is

    -2pi i a^T P^T U Z a -2pi i b^T C a,
    C=K^T U^T P.                                        (1.2)

**Additional rank hypothesis:** rank C=k. Choose CJ=I and V a basis
of ker C. With a=J c+V s, the b integral is delta(c), and the result is

    c_X integral_R^d exp(2pi i s^T Q_red s)
                      product_j f_j(epsilon_j(Ss)_j) ds,
    d=N-2k, S=P V,
    Q_red=-sym(S^T U Z V),
    c_X=|det[G F] det[Z K] det[J V]|.                    (1.3)

All displayed determinants are retained. In particular, a numerical
specialization is not used to discard a normalization factor.
In (1.3) we have reversed the remaining real coordinates s after the
delta integration. The dynamical variable is then t=-E R x=S s;
the quadratic is unchanged and the Lebesgue Jacobian is one. This
fixes the sign needed for the subsequent common-Phi convention.

**Distributional justification.** The delta(Dx) is an ordinary
independent linear delta measure. The remaining product of positive
charged functions, pulled back by the injective map P, is Schwartz in a;
the quadratic chirp preserves Schwartz space. Fourier integration in b
gives delta(Ca), whose pullback is defined because C is surjective.
Equivalently insert exp(-pi eta |b|^2): its b integral is
eta^(-k/2)exp(-pi|Ca|^2/eta), and the ordinary Gaussian approximate-identity
limit after a=Jc+Vs gives (1.3). The Schwartz bounds justify that limit.
Positive Gaussian regularizations in all face variables give the same
Fourier distribution by completing the kernel Gaussian and applying
the same argument. This is an evaluation of (1.1), not a divergent
integral treated as absolutely convergent.

The reduced integral itself is absolutely convergent. Its value is
independent of the chosen rational bases with exactly the determinants
in (1.3). For k=0 the calculation gives the earlier proper expression:
Q_ambient=Q_f and c_X/|det S|=1/|det script-A|.

## 2. Stokes still gives the edge identities

Let a_e,b_e,c_e denote local opposite-pair edge incidences and A_ed,B_ed
the literature edge matrices of `face_edge_stokes_identity.md`.
For an arbitrary assignment lambda to global edges, put on an ordered
triangle i<j<k

    phi(lambda)_ijk=lambda_jk-lambda_ik.

Then D phi=0 and E R phi=B_ed^T lambda. The same face cancellation as
in the previous note, now without an inverse face matrix, gives

    B_ed^T lambda in im S,
    S^T A_ed^T = S^T G_ambient B_ed^T,                   (2.1)
    G_ambient=-2 Q_ambient+P_+,
    P_+=(E+I)/2.

Here Q_ambient is any real symmetric extension of Q_red from im S.
For completeness, write phi=F z_lambda. The Stokes cancellation gives

    U^T B_ed^T lambda=T^T(lambda_01-lambda_02),
    U z_lambda=lambda_23-lambda_13.

If b is a ker T direction, the first equality implies
K^T U^T B_ed^T lambda=0, so B_ed^T lambda is in im S.
Differentiating the quadratic (1.2) along this direction gives
-2 S^T Q_ambient B_ed^T lambda=S^T(a(lambda)-b(lambda)).
Adding P_+ gives (2.1). Changes of lift by ker T vanish in this
calculation precisely because S satisfies the Fourier constraints.

## 3. A complete-geometry volume theorem for the full tensor

Assume the two rank hypotheses of Section 1 and a complete positive
geometric ideal structure. Choose its actual physical angles as the
charges. Use b>0 for the quantum parameter, Q_b=b+b^(-1), h=Q_b^(-2).
Write a,c for physical angle vectors in radians and put

    d_angle=pi 1-a, C_angle=E c,
    H=Q_ambient-P_+/2,
    W=2 Q_ambient d_angle-C_angle.

Applying the exact inversion identity to the reduced tensor and setting
y=i d_angle+S z gives the dynamical integrand

    exp[(i y^T H y+W^T y)/(2pi h)]
                       product_j Phi_b(y_j/(2pi sqrt(h))). (3.1)

The Jacobian is (Q_b/(2pi))^d, multiplied by c_X. All omitted factors
in this display are the explicit unit phases of Section 6 below.

**Lemma (decoration).** If z_j are the positive literature shape
parameters, set u=log|z| and w=log|z''|. There is a real global edge
vector lambda with

    u=-B_ed^T lambda/2, w=A_ed^T lambda/2.                (3.2)

Choose consistently scaled horospheres on the complete cusp(s), and
let lambda_e be the signed length of the segment on e between them.
The formula is the cross-ratio modulus identity. For the negative
ordering with vertices (infinity,0,1,z), take unit horosphere factors:
the nonzero finite edge contributions are
lambda_13=2log|z| and lambda_23=2log|1-z|. Thus
u=(b_e-c_e)lambda/2 and w=(a_e-b_e)lambda/2. Changing the ordering
gives exactly (3.2) with the columnwise epsilon convention. Horosphere
changes add vertex terms and cancel in both formulas.

By (2.1), Re y_*=-u lies in im S, where

    y_*=-Log z+i pi 1,
    Im y_*=d_angle.

It is therefore on the actual integration plane. The real part of
the ambient classical gradient at this point is zero: in a positive
tetrahedron it is d_angle-c-Arg z''=0, and in a negative tetrahedron
it is c-Arg z''=0. Its imaginary part on im S is zero by (3.2) and
(2.1). Hence y_* is a full critical point on the reduced plane.

For the classical phase

    F_0(y)=i y^T H y+W^T y-i sum_j Li_2(-exp y_j),

the Bloch--Wigner identity gives Re F_0(y_*)=-sum_j D(z_j)=-Vol(M).
Its real Hessian on real directions in im S is

    -S^T diag[Im(e^y/(1+e^y))] S,

which is negative definite because 0<Im y_j<pi. Thus the critical
point is unique on its horizontal plane, has a nonzero Gaussian
coefficient, and has the global linear tail bound proved by the ray
argument in `literature_state_volume.md`. The independently derived
uniform Phi remainder and the exact h versus b^2 correction apply
to the same N factors. The implicit-function and contour arguments
therefore apply in dimension d. They prove

    lim_(h->0+) -2pi h log|Z_AK(X,complete angles;b)|=Vol(M). (3.3)

The normalized full tensor is nonzero for sufficiently small h. This
theorem does not assume B invertible, a FAMED longitude identity, or a
formal absence of cancellations. It is a theorem for the specified
kernel contraction under the displayed rank/geometric hypotheses;
it does not assert global triangulation invariance.

## 4. The explicit singular chart for 6_2

Use the folded word RRLR, hence Conway [3,1,2]=11/3, and the ordered
faces returned by `certify_six_two.py`. The signs are

    (+,+,-,-,-,+).

The 12 by 12 stacked face matrix has rank 11. Nevertheless
rank D=6, k=1, rank C=1, d=4 and c_X=1. A determinant-one change of
the reduced coordinates gives the especially simple affine shape plane

    y=(u,v,i pi-u-v,i pi-u-v,w,z),
    z_coord=(u,v,w,z).

Thus the singularity imposes actual linear relations; it does not
prevent an integral representation of the same charged tensor.

The normal cusp cycles computed from the face pairings give H_1(M)=Z,
alpha of linking number 1, beta of linking number 6, intersection
alpha.beta=1, and

    [beta-6alpha]=boundary_2*(-2,-3,-7,3,0,3)^T.

Consequently l=beta-6alpha is the primitive preferred longitude up to
sign. This is an integral cellular certificate. Its angle rows are
recorded in the script; the affine offset and its zero branch are
checked independently.
The optional combinatorial isomorphism to the marked canonical 6_2
triangulation calibrates alpha to the standard meridian and l to the
standard longitude, with zero affine correction. Its cusp matrix from
the imported arbitrary basis is [[6,-1],[1,0]].

A positive rational reference angle structure, in units of pi, is

    (5,1,1 | 5,1,1 | 4,2,1 | 4,1,2 | 5,1,1 | 1,5,1)/7.

Its longitude is zero. On the entire balanced affine angle space,
the imaginary affine plane above is fixed; the angle-dependent linear
term varies only with the longitude. Its coefficient is

    (lambda/2) p, p=(-1,-1,-1,1)^T,
    x=p^T z_coord=-u-v-w+z, gamma=0.

The imaginary part of x is exactly the angular holonomy of alpha.
All these claims are rational matrix identities on the complete affine
angle space, rather than identities checked only at one structure.

## 5. An exact complete-geometry certificate for 6_2

In the native all-positive shape convention the layer shapes are
(a,a,b,b,c,c), with

    P(c)=c^5-3c^4+5c^3-5c^2+4c-1=0,
    a=c^3-2c^2+2c-1,
    b=2c^4-5c^3+8c^2-7c+6.

The root is isolated by the rational Rouché disc

    |c-(1186078+874646 i)/10^6|<10^(-5).

The Taylor remainder bound divided by the lower bound for the linear
term is less than 0.086 (the exact test is less than 1/10). Thus there
is exactly one root in the disc. Rational image enclosures put every
shape in the upper half-plane. The eight native multiplicative
edge/peripheral equations reduce to zero modulo P. Rational atan2
and Machin bounds fix their logarithmic branches. All dihedral angles
are greater than 1/4 radian.

The source Gaussian uses the opposite global orientation from this
native shape convention. Choose the quad in each newly ordered
tetrahedron first, then uniformly replace its positive shape q by
1/conj(q). In terms of the lower root t=conj(c), the positive
**literature** shape parameters for our six ordered tetrahedra are

    (1/a(t),1/a(t),1/b(t),1/b(t),1-t,1/t).                (5.1)

This distinction preserves angles and Bloch--Wigner volume but changes
logarithmic moduli. Inverting tetrahedra individually according only
to their signs would give the wrong saddle.

The script independently reduces all six literature Neumann--Zagier
edge equations and the two normal peripheral equations using (5.1)
modulo P(t). It also fixes the affine-plane branch
y_0+y_1+y_2=i pi and y_2=y_3. These give a complete positive ideal
structure without relying on a numerical solver. Its volume is

    V=2[D(a)+D(b)+D(c)]
       =4.4008325161230461014... .

## 6. The selected boundary state and its exact tensor normalization

Define the following state by disintegrating the Fourier-reduced
existing tensor along x=-u-v-w+z. With z=x+u+v+w, put

    J_6_2(h,x)=(2pi sqrt(h))^(-4) integral I_b(u,v,w,z) du dv dw,
    I_b=exp[(i z_coord^T H_red z_coord+pi v_lin^T z_coord)/(2pi h)]
          product_(j=1)^6 Phi_b(y_j/(2pi sqrt(h))),
    v_lin=(-2,-2,-1,1)^T,

    H_red = [ -3/2 -3/2 -3/2  1/2 ]
            [ -3/2 -3/2 -3/2  1/2 ]
            [ -3/2 -3/2   -2    1 ]
            [  1/2  1/2    1 -1/2 ].                   (6.1)

The contour is the horizontal fiber through the complete saddle at
x=0, continued for small x. The positive coarea Jacobian is one
when eliminating z, since its coefficient in x is one.

Equivalently the exponent after substitution is

    [i(-(u+v)^2-(u+v)w-w^2/2+xw-x^2/2)
                                +pi(x-u-v)]/(2pi h),

and the Phi arguments have numerators

    u, v, i pi-u-v, i pi-u-v, w, x+u+v+w.

This is not the printed FAMED formula evaluated with det script-A=0.
It is a fiber of the original charged-operator contraction, providing
the type of factorization used in the existing AK formulation.

Here is its exact phase convention. For balanced physical angles let
Q_ambient be the rational extension in the certificate and set

    d_angle=pi 1-a, C_angle=E c,
    W=2 Q_ambient d_angle-C_angle,
    Theta=C_angle^T d_angle-d_angle^T Q_ambient d_angle,
    k(a,c)=a c/(4pi)+(a-c)/12-pi/24,
    beta0=(0,0,1,1,0,0)^T,
    kappa=-beta0^T H beta0+(W^T beta0)/pi,
    K=sum_j epsilon_j k(a_j,c_j)-pi N_+/12
                               +Theta/(2pi)+pi kappa/2.

The exact inversion and charged Fourier identities now give

    Z_AK(X,angles;b)=i exp(i K/h)
        integral_(R+i mu) J_6_2(h,x)exp(lambda x/(4pi h)) dx. (6.2)

At the rational reference angles kappa=27/35. Thus removing the
constant from the displayed compact integrand has the recorded
multiplier exp(27pi i/(70h)); it is included in K in (6.2).
Choosing the existing AK level ell=-4K/pi removes precisely that phase.
The root i is exp(pi i N/12) for N=6. No peripheral variable has been
specialized in (6.2).

The strip, tail, and Fourier--Laplace uniqueness arguments of the
previous phase note apply to this reduced integral. The map from
balanced angles to (mu,lambda) has rank two. Thus the fixed normalization
in (6.2) recovers this selected fiber uniquely from that normalized
tensor function. General identification with fibers from arbitrary
triangulations still requires compatible connecting paths.

## 7. Volume and the quantum A-operator for this state

There is also a direct critical-equation check, independent of the
general decoration lemma in Section 3. Let g=(1/i)grad F_0 in the four
coordinates of (6.1), and use the exact edge/normal-curve matrices from
the certificate. They give all edge equations as linear combinations
of g with zero logarithmic offset. Their coefficient matrix has rank
three. Adding the preferred-longitude row gives rank four. Therefore
the complete shapes (5.1) force g=0. The meridian relation is

    H_alpha=x+b_alpha^T g,
    H_l=b_l^T g, b_alpha^T p=0, b_l^T p=2.               (7.1)

In particular x=0 at completeness. The restricted Hessian on its
three-dimensional fiber has negative definite real part. The same
uniform Phi remainder, complex saddle, and tail proof as before gives

    lim_(h->0+) -2pi h log|J_6_2(h,0)|=Vol(S^3\6_2).     (7.2)

For clarity, the critical value is not inferred from the exponentiated
equations alone. In the affine coordinates y=i pi beta0+S z_coord,
the exact Bloch--Wigner identity is

    Re F_0 = Re z_coord . Re grad F_0 + sum_j D(-exp y_j).

At the certified critical point this is -sum_j D(z_j). Strict concavity
and the nonzero Gaussian coefficient control cancellation. The state
is nonzero for all sufficiently small h.

All Phi arguments and Gaussian coefficients in (6.1) are rational
linear/quadratic data. The independently proved finite-product,
dimension-count, and exponential-moment argument therefore gives a
nonzero minimal boundary annihilator in the Andersen--Malusà convention:

    t_0=x/(2pi sqrt(h)), q=exp(2pi i b^2),
    Q=exp(-2pi b t_0), E:t_0 -> t_0-i b, E Q=q Q E.

At a constrained saddle grad F_0=i xi p/2, equations (7.1) yield

    H_alpha=x, H_l=xi,
    Q=exp(-H_alpha), E=exp(H_l/2).

Thus Q^(-1) and E^2 are the PSL(2) meridian and longitude eigenvalue
ratios. Conversion to conventional SL(2) A-polynomial variables must
also record the lift signs, including the possible negative longitude
lift at completeness.

The geometric peripheral factor thus divides its nonzero classical
symbol by the uniform saddle argument already proved. A full explicit
minimal-operator coefficient list and equality to the Jones AJ operator
are not being asserted. Generic factors are retained before any Q=1
specialization.

## 8. Reproducibility and remaining uniform work

Run the exact core with

    python3 experiments/reduce_singular_faces.py
    python3 experiments/certify_six_two.py

and the separate standard-marking calibration with

    .venv/bin/python experiments/certify_six_two.py --topology

The finite word scan

    python3 experiments/reduce_singular_faces.py --scan-length 7

checks 81 one-component folded R/L words. They all pass the two rank
hypotheses, fixed-support angle test, rank-one longitude variation test,
and rank B_ed=d-1. The rank hypotheses now have the uniform cohomological
proof in the subsequent note. The additional finite angle tests remain
evidence for the general boundary construction, rather than a proof of it.
The scan also includes singular charts: the alternating word
RLRLRLRL reduces from fourteen tetrahedral factors to ten integration
variables. The exact algorithm and analytic theorem now handle the
singularity which prevented the previous proper-chart approach.

`check_singular_state_volume.py` additionally checks the correctly
oriented classical saddle and evaluates the finite-b three-dimensional
integral numerically. The recorded maximum classical gradient is below
7e-16. At b=0.24 and b=0.16, changing the quadrature order from 36 to
56 changes the normalized complex amplitude by approximately 5.7e-4
and 1.4e-4 respectively. These are coarse numerical diagnostics;
the proof and all root/branch decisions use the exact certificates.
