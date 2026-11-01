# The actual marked line-circle pattern near the complete source

30 October 2026. This note reconstructs
a local analytic circle pattern on the ACTUAL labeled white-face sphere,
including its two marked line faces. Its radii agree with the stationary
limiting face action. It also retains the selected fixed-point germs of
the local product of physical meridians at the degenerate marked
triangles. The ordered auxiliary meridian and full regulator comparison
remain separate until their actual collar words are calculated.

Follow-up: the [primitive collar calculation](actual_deformed_circle_primitive_collar.md)
and [global geometric assembly](actual_complete_core_geometric_deformation.md)
now supply those steps. The full reflected-color filling estimate remains
outside these geometric theorems.

## 1. Actual incidence and a finite reconstruction system

Use the labeled convex ideal right-angled certificate and original main
mark of [the matching geometry](general_augmented_plat_matching_geometry.md).
The [white-normal construction](actual_right_angled_selected_framing_obstruction.md),
section 2, gives a SIMPLICIAL triangulated sphere C. Its vertices are the
R+2 actual white faces, and its 2R triangles are the shaded source
vertices. Each triangle has two main edges and one matching edge.
The two marked white faces u,v share the original MAIN edge. These
are incidence hypotheses already supplied by this certificate; no
arbitrary routed graph or combinatorial repair is introduced.

Make one common orientation-preserving normalization of the complete
circle picture. The outward marked disks are the halfplanes Y<=0 and
Y>=1. Their common ideal point is infinity. All other outward disks
are finite disjoint circles inside the strip, with positive radii.
Keep their original labels and choose one finite center's horizontal
coordinate as the last translation normalization.

For each finite face f use unknowns (X_f,Y_f,r_f). Let delta_i be one
small complex parameter for each actual matching edge. On a main edge
put I_e=1, and on matching edge i put I_e=cos(2pi delta_i). The equations
are, with the ACTUAL signed line side,

    (X_f-X_g)^2+(Y_f-Y_g)^2
                         =r_f^2+r_g^2+2I_e r_f r_g,       (1a)
    Y_f=r_f I_e                 on the lower marked line, (1b)
    1-Y_f=r_f I_e               on the upper marked line. (1c)

The marked line-line edge is automatic and has no equation. Fix the
chosen X-coordinate at its complete value. There are 3R-1 remaining
variables and 3R-1 equations, since C has 3R edges. These are holomorphic
polynomial/trigonometric equations; their real version is the usual
signed circle inversive-distance equation. Complexification uses
X,Y,r as independent holomorphic coordinates, not complex conjugation.

The Jacobian in these variables is invertible at delta=0. Consequently
(1) has a unique nearby holomorphic solution for all delta in one fixed
complex polydisc. It is real for real delta and even separately in each
delta_i. Radii remain nonzero. This assertion is local for each fixed
certified diagram, at arbitrary fixed bridge width.

## 2. Proof of the full Jacobian rank, including the line faces

Consider an infinitesimal kernel vector of (1) at delta=0. The original
center triangles have the following angle interpretations. A triangle
with three finite circles is its nondegenerate Euclidean center triangle.
For one marked line, the direction to its infinite center is the fixed
outward vertical direction, and the two finite angles are the limits
of the center-triangle angles. For two marked lines the two vertical
directions are opposite: the finite angle is \(\pi\) and the other two
angles are zero. The side signs in (1b,c) are essential here.

In the actual cyclic order around a finite face these direction angles
sum to \(2\pi\). Their first variation therefore vanishes. At complete
tangency the already proved source gradient is \(\theta/(2\pi)\). The
complete triangle Hessian can be computed directly. Let \(I_t\) be the
ordinary corners of a triangle, put \(w_i=1/r_i>0\), \(q_i=\log w_i\) and
\(D_t^2=\sum_{\{i,j\}\subset I_t}w_iw_j\), and let \(F_t\) be
its normalized triangle potential: maximize the calibrated triangle
entropy plus \(\sum_i\theta_iq_i\) over nonnegative angles of sum
\(\pi\), with protected angles zero, and divide the result by
\(2\pi\). The entropy is the function in Appendix L, equation
\(\mathcal V(\theta)=2\sum_i[\Lambda(\theta_i/2)+
\Lambda((\pi-\theta_i)/2)]\), where
\(\Lambda(s)=-\int_0^s\log|2\sin t|\,dt\).
For at least two ordinary corners and a real variation vector \(h\),
\[
 \partial_{q_iq_j}F_t
 =-\frac{w_iw_j}{2\pi D_t(w_i+w_j)}=-\kappa^t_{ij}
 \quad(i\ne j).
\]
Consequently,
\[
 h^{\mathsf T}\nabla^2F_t h
 =\sum_{\{i,j\}\subset I_t}\kappa^t_{ij}(h_i-h_j)^2.
\]
Indeed the gradient is \(\pi^{-1}\arctan(w_i/D_t)\), and for
three corners the derivative simplifies using
\(D_t^2+w_i^2=(w_i+w_j)(w_i+w_k)\). The two-corner formula is
the limit with \(w_k=0\). Logarithmic homogeneity gives zero row sums. A
singleton triangle has potential \(q_i/2\) and zero Hessian.
Deleting the two adjacent protected vertices leaves a connected
ordinary graph: reroute paths through the first vertex's cyclic link,
then through the second vertex's link with the first removed.
Every surviving edge has strictly positive conductance in this sum.
Consequently the full Hessian has exactly the constant kernel.
The zero angle-sum variations force all logarithmic curvatures, and
hence all logarithmic radii, to vary by one common scale. This is a
calculation at the complete pattern, independent of a parametrization
by off-critical representations.

There are exactly two triangles containing the edge uv. In either,
the finite circle is tangent to BOTH normalized lines, so r=1/2.
Linearizing its two equations gives dr=0. Hence the common radius
scale variation is zero: all dr_f=0.

With the radii fixed, an all-finite triangle has fixed three side lengths,
so its center velocities are one infinitesimal Euclidean motion. A
one-line triangle has dY_f=dY_g=0. At the complete point its horizontal
separation has absolute value 2sqrt(r_f r_g)>0. Its fixed finite edge
length therefore gives dX_f=dX_g: its two centers have one common
horizontal translation, with zero rotation and vertical translation.

Delete the two triangles incident to uv. Their union is a topological
disk with four-edge boundary; the remaining triangles form a triangulated
disk with connected adjacency graph. This last statement follows by
joining two triangle interior points by a path in the disk interior and
perturbing that path to avoid vertices and cross edges transversely.
Every finite vertex occurs in this remaining disk: its sphere link has
at least three triangles, whereas only two triangles were deleted.
There is a remaining one-line triangle, since the link of u has at
least three triangles and only its two uv triangles were removed.

Two remaining triangles sharing a finite-finite edge have the same
infinitesimal Euclidean motion, because they agree at two distinct
centers. If their common edge contains a marked line, both are one-line
triangles; agreement at their common finite center identifies their
horizontal translations. Starting at a remaining one-line triangle and
using the connected adjacency graph therefore leaves one horizontal
translation for ALL finite centers. The fixed X-coordinate removes it.
The Jacobian kernel is zero. Since the finite system is square, the
holomorphic implicit-function theorem proves the assertion in section 1.
No Bessel packet, finite-color stationarity, or new source-cycle
hypothesis is used in this reconstruction.

## 3. The full local face force is the deformed center angle

Here all variables are curvatures, so l_f=1/r_f. For one ordered source
triangle (x,b,y), put mu=1/2-delta and

    s=sin(pi delta), c=cos(pi delta), A=x+y,
    D=A^2-4xy s^2,
    T_b=sqrt[bA+xy+b^2s^2], E_b=A+2bs^2+2sT_b.

Select every root by the positive complete value and continue analytically.
Let Q_b be ONE determinant rate, ONE beta rate and HALF the forced-product
rate from the [actual channel action](actual_positive_face_channel_rate.md):

    Q_b=I(2mu)-2I(mu)+integral_0^mu log lambda_b(t)dt
                                                    +(1/2)J_mu(x,y). (2)

Thus Q_b+Q_c is exactly the full original circle rate, with its sine
normalization retained. Direct differentiation cancels the sine factors:

    partial_delta Q_b=-Log(E_b/sqrt D), Q_b(0)=F(x,b,y). (3)

For positive curvatures its center triangle has two main tangent side
lengths r_x+r_b,r_b+r_y and matching side length

    L_xy=sqrt[(r_x+r_y)^2-4r_xr_y sin^2(pi delta)].

The middle angle and the outer x-angle obey

    theta_b=2atan[b c/T_b],
    cos theta_x=[x(y-x)+b(y+x cos(2pi delta))]/[(x+b)sqrt D],
    sin theta_x=2x c T_b/[(x+b)sqrt D].                 (4)

Exchange x,y for the third angle. These formulas also specify the
selected complex angle germs. Differentiating (4) gives exactly

    partial_delta(theta_j/(2pi))
                    =-partial_log l_j Log(E_b/sqrt D). (5)

For the middle angle both sides are -b s/T_b. For the outer angle,
differentiate its cosine and sine: their squared sum is one and
(cos theta_x)(partial sin theta_x)-(sin theta_x)(partial cos theta_x)
gives (5) after substitution. This is an elementary rational identity
in x,b,y,s and the displayed roots. The complete source already fixes
the integration constant, so integrating (5) proves

    partial_log l_j Q_b=theta_j/(2pi).                 (6)

One marked zero curvature is obtained by the corresponding line limit.
With two zero curvatures the single finite angle is pi and (6) is the
single-variable homogeneous rate (1/2)log l. The geometry of that
triangle's strip is retained by (1), not by assigning extra information
to this degenerate angle formula.

## 4. Identification with the stationary source radii

The real solution of (1) for small real delta preserves all original
cyclic center-direction orders. Its main tangencies and prescribed
matching intersections give exactly the angles (4), including the
one-line and two-line conventions in section 2. Thus their sums at
every finite circle are 2pi. Holomorphic continuation preserves these
identities on the fixed complex polydisc.

By (6), its curvatures solve the actual limiting face-stationary equations
of the complete Fourier-core action, with the two marked faces zero.
After fixing the source's one positive curvature scale, the complete
face Hessian is invertible. Its holomorphic implicit-function theorem
therefore identifies these normalized curvatures with the UNIQUE
nearby source stationary radii, for every small delta. This is a full
face-momentum identification, not only agreement of the cusp Hessian.

The line-side equations also prove the missing strip consistency
explicitly. At either triangle containing uv, one finite circle is
tangent to one marked line and has matching inversive cosine cos psi
with the other, where psi=2pi delta_i. For strip height H,

    H=r_f(1+cos psi), l_f=2cos^2(pi delta_i)/H.         (7)

The same H occurs on the adjacent uv triangle. It was fixed in (1),
not chosen independently for two source factors. At complete delta0
this is the usual r_f=H/2. Formula (7) survives even though that
triangle's source characteristic quadratic has a repeated root.

## 5. Selected fixed-point germs at a marked triangle

The actual ordered product of two white reflections at matching edge i
has trace -2cos(2pi delta_i) in the recorded negative-parabolic lift.
At delta_i=0 it is a nontrivial parabolic, supplied by the original
certificate. Choosing the eigenvalues

    lambda_+=-exp(-2pi i delta_i),
    lambda_-=-exp( 2pi i delta_i)                      (8)

therefore gives two holomorphic fixed-line germs. This is elementary:
a nonzero off-diagonal entry of the complete parabolic remains a unit,
so the eigenline can be solved explicitly in that affine chart using
lambda_+ or lambda_-. Their collision at delta0 is retained.
The internal source node is exactly -2cos(2pi delta), so (8) records
its two actual eigenvalue branches; it is not a free square root of
the collapsed scalar characteristic.

For clarity an actual two-line calculation resolves the 200 case.
Take the finite circle centered at X+i r, tangent to the lower line,
and the upper matching line at height H=r(1+cos psi). The matching
product P=r_upper r_circle, with the original outward reflection signs,
has trace -2cos psi. Its fixed points are

    p_+=X+r sin psi+iH, p_-=X-r sin psi+iH.            (9)

The recorded lift may be written

    P=(i/r) [[bar c+2iH, r^2-c bar c-2iH c],
                         [1, -c]], c=X+ir.

Here bar c means X-ir; after complexification it is this holomorphic
expression. At p_+ its eigenvalue is -exp(-i psi), at p_- it is
-exp(i psi). If the matching line is instead the LOWER line and the
circle is tangent to the upper one, the selected lambda_+ line is the
point X-r sin psi on that lower line. Reversing the ordered product
exchanges its eigenvalues. These are literal orientation adapters,
not independently reset choices of a local frame.

Equations (7)--(9) retain the actual selected line germs that the
limiting 200 quadratic alone loses. They do not identify a finite-N
Bessel logarithmic derivative with a single classical characteristic.

## 6. What is still required for the complete geometric action

The reconstructed ordered main meridians are parabolic because every
main incidence in (1) remains tangent. Their matching products have
(8). This establishes the local marked circle data and the source
face equations on the actual labeled sphere.

To identify the entire continued core critical action with the marked
geometric deformation, one must still calculate the ACTUAL auxiliary
collar transporter between the two middle circles, including its
half-twist and primitive marking. Its eigenvalue logarithm must equal
the source channel derivative -Log(E_b E_c/D), with the recorded sign
and any integral logarithmic character. One must then check the actual
group relations and peripheral word, and use the already fixed complete
regulator value. Neither existence of circle positions nor the Hessian
match alone replaces this ordered peripheral calculation. No general
mixed-color packet, ordinary-color subset bound, or filled-volume claim
is made here.

Focused audit: [marked reconstruction and selected flags](../experiments/audit_actual_marked_deformed_circle_pattern.py),
with [saved results](../experiments/actual_marked_deformed_circle_pattern_results.json).
It checks 15 exact symbolic gradient and ordered line-eigenvalue identities;
the full 5- and 11-dimensional Jacobians of the original octahedral and
cuboctahedral checkerboard fixtures; 24 real/complex deformed patterns;
144 actual triangle/source-angle checks; 48 shared-strip checks; and
144 selected matching eigenlines. The numerical residuals are below
1.1e-13. These finite fixtures audit the general Jacobian argument; they
do not replace it or prove an auxiliary primitive-collar formula.

The auxiliary primitive-collar identification is separate from the marked circle-pattern theorem.
