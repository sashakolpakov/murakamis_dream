# A positive lens chart with its linear constraints retained

28 October 2026. Every supplied positive complete marked ideal
triangulation admits a geometric reference chart in which ALL shape
arguments lie in the closed lens |z|<=1, |1-z|<=1. No invertibility
of the gluing block B is required. Its kernel is retained as exact
linear constraints, rather than removed by changing some shapes to
exterior arguments.

On this constrained chart the complete fixed-radii reference chain
has a unique volume maximum, a nonzero Gaussian coefficient, and a
strict boundary gap. Every geometric atom lies inside the already
proved coefficient-one finite-Euler region. This removes a classical
polarization obstruction; it does not identify the ORIGINAL quantum
cycle with this reference chain or select its logarithmic sheet.

The [exact/Arb audit](../experiments/audit_constrained_lens_geometric_chart.py)
and [results](../experiments/constrained_lens_geometric_chart_results.json)
verify the supplied 8_1 geometry with its peripheral markings kept
distinct, and six synthetic Lagrangian systems with every rank B=0,...,5.
The synthetic systems check the linear construction; they are not
asserted knot triangulations or a quantum source theorem.

## 1. Lens choices do not require an invertible B

For a positive shape z, the Euclidean triangle with vertices 0,1,z
has sides 1, |z|, |1-z|. Normalize one of its longest sides to one,
preserving orientation. The three cyclic normalizations have shapes

    z, 1/(1-z), 1-1/z.

At least one has both modulus and complementary modulus at most one.
Choose it independently in each tetrahedron. All chosen shapes remain
strictly in the upper half-plane. Their geometric arguments consequently
belong to D_+ in the
[full Euler-atom theorem](full_euler_atom_dilog_and_endpoint_regions.md),
including the cases of equal side lengths. On a compact family of
nondegenerate positive shapes, the coefficient-one estimate is uniform
after taking a finite collection of these lens charts.

Use the resulting real rational marked gluing data

    A x+B y=c,
    x_j=Log z_j, y_j=Log(1-1/z_j),
    rank(A B)=t, AB^t=BA^t, c=i*c_R, c_R real.       (1)

The rotated affine signs and full peripheral mark are retained in c.
Let rank B=r and k=t-r. Choose a real full-rank k-by-t matrix E
whose rows span the left kernel of B. Put

    D=EA, d=Ec.

Then rank D=k and the necessary projection equations are

    D x=d.                                         (2)

Indeed a row combination annihilating both A and B is zero by (1).
Moreover

    ker B=image(D^t),                               (3)

since BD^t=BA^t E^t=AB^t E^t=0 and both spaces have dimension k.

Choose any purely imaginary solution (x_0,y_0) of (1). Such a choice
exists by its full real row rank. Let L be a real t-by-r matrix with
columns a basis of ker D. Solve

    B Y=-A L                                        (4)

for a real t-by-r matrix Y. The solution exists because EAL=DL=0.
Set C=L^tY and l=L^t y_0. Then C is real symmetric and l is purely
imaginary. Symmetry follows because the tangent vectors (L v,Y v)
lie in the Lagrangian kernel of (A B). It is independent of the
choice of Y, by (3) and L^t D^t=0.

The ENTIRE affine gluing relation now reads

    x=x_0+L xi,
    y=y_0+Y xi+D^t lambda,                         (5)

with unconstrained lambda. No inverse of B appears. There is no
assertion that the coordinates xi, or the Fourier implementation of
(2), already have the original quantum source.

## 2. A nondegenerate constrained potential with the original volume mark

On the positive branches define

    F(x)=sum_j [Li_2(exp x_j)+x_j^2/2-i*pi*x_j],
    W_L(xi)=F(x_0+L xi)+xi^t C xi/2+l^t xi.        (6)

The additive constant in (6) is zero, hence real; no imaginary
constant is chosen to fit a volume. Since F_x=-y_shape, its derivative is

    grad W_L=-L^t y_shape+C xi+l.                   (7)

By (3), equation (7)=0 is equivalent to y_shape having the form in
(5). Together with (2), these are exactly ALL the original equations
(1), including their marked affine constants.

On the positive chart, where each z_j=exp(x_j) lies in the upper
half-plane,

    Im Hess W_L
       =L^t diag_j[Im(z_j)/|1-z_j|^2] L >0.        (8)

Thus the reduced Hessian is invertible, for every rank of B. If r=0
the statement is the zero-dimensional one with determinant one.
No degeneracy is introduced by retaining (2).

Let xi_*=rho_xi+i theta_xi be the complete solution, and write
x_*=rho+i theta and y_*=sigma+i gamma. Because x_0 is purely imaginary,
rho=L rho_xi. The Bloch identity gives

    Im F(x_*)=sum_j D(z_j)-rho^t gamma.

The quadratic/linear terms in (6) have imaginary part
rho_xi^t(C theta_xi+Im l). The imaginary part of (7)=0 makes this
rho^t gamma. Therefore, with its stated marks,

    Im W_L(xi_*)=sum_j D(z_j)=Vol(M).               (9)

This argument uses the complete marked gluing solution and retains
the constraints; it does not replace an unsaturated gluing scheme by
all of its cleared boundary points.

## 3. A full constrained angular box with a strict gap

Keep rho_xi fixed at its complete value. Then the allowed shape
angles lie in the affine plane D theta=Im d. Define the reference
polytope

    P={theta in [0,2*pi]^t : D theta=Im d}.         (10)

It has relative dimension r and the geometric angle point in its
relative interior. Use theta=Im x_0+L theta_xi to parametrize it.
This is a SPECIFIED lifted polytope. It is not automatically a
fundamental domain of the corresponding torus: other integer
logarithmic sheets and their source factors must not be identified
with (10) without proof.

Put r_j=|z_*j| and ell_j=log|1-z_*j|. Both r_j<=1 and ell_j<=0
by the lens choice. On the affine plane (10), direct expansion of
(6) and the REAL part of (7) give

    Im W_L=sum_j f_j(theta_j)+constant,
    f_j(theta)=Im Li_2(r_j exp(i theta))+ell_j theta. (11)

To verify the possibly important linear term, its coefficient in
theta_xi is L^t rho+C rho_xi. The real part of (7) says
C rho_xi=L^t sigma, and sigma_j=ell_j-rho_j. Thus that coefficient
is exactly L^t ell. Equality (11) follows up to one fixed constant,
already calibrated by (9).

Each f_j has its unique global maximum on [0,2*pi] at theta_*j.
On (0,pi),

    f_j'=ell_j-log|1-r_j exp(i theta)|,
    f_j''=-r_j sin(theta)/|1-r_j exp(i theta)|^2<0.

The derivative changes sign at theta_*j. On (pi,2*pi) the function
is convex, so its maximum is at an endpoint. The endpoint values
at 0 and 2*pi are 0 and 2*pi*ell_j<=0; at pi the value is
pi*ell_j<=0. Meanwhile f_j(theta_*j)>0. These statements also hold
when r_j=1 by continuous boundary values. Consequently

    max_P Im W_L=Vol(M),
    max_(relative boundary P) Im W_L
                <=Vol(M)-min_j f_j(theta_*j)<Vol(M). (12)

If r=0 the boundary is empty. In positive dimension every relative
boundary point has at least one active coordinate face; the others
cannot exceed their own maxima. This proves (12) on the WHOLE marked
box intersection, not only the positive angle polytope.

For example, let a be a FIXED continuous density on the compact
polytope, smooth near xi_* and nonzero there. The reference integral

    I_N=integral_P a(theta_xi)
               exp[N W_L(rho_xi+i theta_xi)/(2*pi*i)] dtheta_xi

has a nonzero Gaussian leading coefficient, a power N^(-r/2), and
exponential rate Vol(M)/(2*pi). Its real quadratic part is negative
definite by (8); the unique interior maximum separates the complement
of a small critical neighborhood, and (12) also gives its strict
boundary gap. A specified classical amplitude with a nonzero leading
density gives the same conclusion under its uniform bounds.

This assertion is not about arbitrary N-dependent regular densities,
which can themselves carry an exponential action. For finite
full-Psi amplitudes one must use their actual uniform symbols and
retain any endpoint indentations or completions; the statement does
not discard them. Near xi_* the original finite Euler atoms have
coefficient one by their D_+ theorem.

## 4. Consequence and remaining source issue

The earlier 8_1 example shows that all-subunit shapes may force B
singular. It does NOT force an exterior geometric atom if one retains
the linear constraints (2). In that same exact five-tetrahedron
geometry the unique lens rotation is (1,1,1,1,0). Using the ORIGINAL
meridian row and independent edge rows (0,1,2,3,5), B has rank THREE:
there are two constraints and a nondegenerate three-variable phase.
The constraint matrix from the exact elimination is

    D=[[0,0,1,1,-2], [0,0,1,0,-1]], d=0.

Using the explicitly different LONGITUDE marking (0,1,2,3,6) gives
rank B=FOUR, one constraint, and a nondegenerate four-variable phase.
Both complete geometric points have all supplied edge and peripheral
equations satisfied. The two reduced charts do not silently identify
their peripheral source or polarization. Including both peripheral
rows together would instead give rank(A B)=6 and a non-Lagrangian
system, outside hypothesis (1); its B-rank four is not a substitute
for checking that hypothesis.

The audit imports the existing exact field/gluing certificate and
checks rank, the entire affine parameterization, symmetry and
independence of C, the marked critical equations, volume calibration,
positive Hessian minors, a nonzero complex Gaussian determinant, and
certified positive coordinate/boundary gaps. Its synthetic rank-zero
case also checks the empty-boundary convention. Optional --topology
replays the existing combinatorial identification with 8_1.

This is a general construction for supplied positive triangulations,
not a new knot-by-knot strategy. It avoids one reason for leaving the
coefficient-one atom domain. The remaining requirement is still to
transport the ORIGINAL source, lattice and logarithmic marks to this
constrained chart and compute its geometric relative coefficient.
Neither classical linear elimination nor a formal Fourier delta is
being asserted to perform that quantum/source comparison.

Run

    python3 experiments/audit_constrained_lens_geometric_chart.py

or add --topology in the previously specified SnapPy environment.
