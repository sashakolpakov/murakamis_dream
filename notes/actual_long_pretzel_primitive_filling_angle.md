# The selected long-pretzel filling has primitive angle 2pi

29 October 2026. The actual unit-charge equation gives a primitive
2pi geometric meridian, not merely scalar PSL holonomy. The
uncentered SL longitude log would give the WRONG angle. This note
fixes the small geometric logs from the actual cusp development,
proves their exact oriented core-length formula for independently
signed slopes, and identifies the normal rotation without a hidden
integer. The positive compact-core deformation and the resulting
global tube completion are supplied by their separate geometric
lemmas; scalar holonomy alone would not supply them.

## 1. Center the projective geometric logs before forming the slope

The literal mixed-circle certificate fixes

    M_i=exp(u_i)=H_i^(-1/2), u_i=-z_i/2,
    lambda_i=-L_i^(-1), v_i=Log lambda_i=pi i-ell_i,
    z_i=Log H_i, ell_i=Log L_i,

with all z_i,ell_i zero at the complete geometric point. The
preferred longitude has SL eigenvalue -1 there. Its PROJECTIVE
multiplier is nevertheless one. In a coordinate whose infinity
is the selected peripheral eigenflag, the actual affine holonomy
multipliers are M_i^2 and lambda_i^2. Their continuously small logs
are therefore

\[
 U_i=2u_i=-z_i,\qquad
 V_i=2(v_i-\pi i)=-2\ell_i.                            \tag{1}
\]

Both vanish at completeness. This centering is fixed ONCE by the
complete affine translation cusp, independently of the slope.
It is not an opportunistic logarithm reset at the filling point.
The positive original diagonal marking is

    mu_i=W_i(1+i c), lambda_i=2ic W_i,
    c=cos(pi/s), W_i>0,

in its complete Euclidean cusp coordinate. Thus

    (dV_i/dU_i)(0)=2tau_s=2ic/(1+ic), Im(2tau_s)>0.     (2)

The basis is primitive: it is the actual meridian and boundary of
the crossing disk, not half or twice that boundary. The retained
R^(-1) is already in this mu_+ marking; no additional meridian shear
is allowed.

For the ACTUAL source equation of charge m_i,

    z_i+2p_i ell_i=2pi i m_i,

equation (1) gives EXACTLY

\[
 \boxed{U_i+p_iV_i=-2\pi i m_i.}                       \tag{3}
\]

In contrast u_i+p_i v_i=pi i(p_i-m_i) is an UNCENTERED SL
eigenlog. Its p_i*pi i term is the old longitude spin, not
geometric winding about a new core. Doubling that expression and
calling it a cone angle would be incorrect. Likewise using undoubled
eigenlogs would incorrectly give pi instead of 2pi.

## 2. A uniform exact core-length and orientation identity

Separate evenness of the original analytic source action implies

    ell_i=z_i a_i(z_1^2,...,z_s^2), a_i(0)=tau_s.

Hence the ratio

    t_i(z)=V_i/U_i=2a_i(z_1^2,...,z_s^2)

is holomorphic through z_i=0. On a fixed sufficiently small
complex source neighborhood, Im t_i>=b>0. This remains true for
the simultaneous selected fillings, regardless of the signs or
relative magnitudes of their large p_i.

Combining V_i=t_iU_i with (3), for REAL nonzero p_i, gives the
exact formulas

\[
 U_i=\frac{-2\pi i m_i}{1+p_it_i},\qquad
 V_i=\frac{-2\pi i m_i t_i}{1+p_it_i},\qquad
 \boxed{\operatorname{Re}V_i
       =\frac{2\pi m_i\operatorname{Im}t_i}
                                  {|1+p_it_i|^2}.}     \tag{4}
\]

The denominator cannot vanish because Im t_i>0. Thus each nonzero
charge gives U_i,V_i nonzero and a genuine LOXODROMIC core generator:
Re V_i has the sign of m_i. In particular it cannot be a nontrivial
elliptic with an accidentally killed eigenvalue. At the selected
unit charges the positive core length is

    length_i=|Re V_i|=2pi Im t_i/|1+p_i t_i|^2>0.

There is no comparison between different slope sizes in this proof.
The oriented logarithmic lattice is also fixed:

\[
 \operatorname{Im}(\overline U_iV_i)
     =|U_i|^2\operatorname{Im}t_i
     =2\pi m_i\operatorname{Re}V_i>0.                  \tag{5}
\]

Thus the two period directions are linearly independent over R,
with the SAME orientation as the positive complete cusp. Reversing
the unit charge jointly reverses U_i,V_i and the core orientation;
it does not mirror the hyperbolic structure or change the slope.

## 3. The small source logs ARE the geometric angular lifts

Here is the precise local lemma needed to exclude a hidden extra
2pi winding. Its input is the genuine positive similarity cusp-link
deformation supplied by the positive-core construction, not an
abstract representation with prescribed eigenvalues.

Choose the moving peripheral eigenflag as infinity by a frame
continuous at the complete cusp. Let the developed similarity
cross-section have holonomy

    mu: w -> exp(U)w+A,
    lambda: w -> exp(V)w+B.

On the complete limit A->W(1+ic), B->2icW, both nonzero.
Develop the two primitive generator paths using a fixed finite
cusp triangulation and a fixed basepoint. Their images and their
Euclidean lengths stay uniformly bounded near completeness: each
comes from finitely many continuously varying positive triangles.
Call a common image bound R and length bound L. These are bounds
in the continuous cusp frame, not a singular diagonalizing frame.

For U!=0 sufficiently small, the common finite affine fixed point is

    k=A/(1-exp(U)).

Commutativity makes it the fixed point for lambda too. Since A has
a nonzero limit, |k| tends to infinity as U tends to zero, uniformly
in all the other small parameters. In particular |k|>2R. Along
either generator path the analytic logarithmic coordinate

    T=Log(dev-k)

can be continued in the ball of radius R, which misses k. Its
variation satisfies the elementary bound

\[
 |\Delta T|\le L/(|k|-R)\longrightarrow0.              \tag{6}
\]

The endpoint affine holonomy gives exp(Delta T)=exp(U) or exp(V).
Therefore Delta T-U or Delta T-V is an integer multiple of 2pi i.
Both quantities tend to zero. For all sufficiently small parameters
the ONLY possible integer is zero:

\[
 \boxed{\Delta_\mu T=U,\qquad\Delta_\lambda T=V.}      \tag{7}
\]

This is pointwise quantitative; no connectedness of a punctured
parameter domain or arbitrary lift choice is used. It rules out
an added integer for EACH primitive generator before multiplying
one by the large p. Because the finite source/port frame and the
cusp triangles vary on one fixed neighborhood, the argument is
uniform for independently signed large slopes. If only a PSL
character were given without this geometric cusp-link development,
the conclusion (7) would not follow from eigenvalues alone.

The log-link/tube theorem uses precisely these periods. Its compact
translation torus has no extra wrapping index because the primitive
generators have periods U,V generating its full rank-two lattice.
One must not infer a period lattice solely from the multiplier
equations without the small-increment argument (6).

## 4. Primitive slope, actual angle, and the absence of branching

The filled primitive curve is sigma=mu+p lambda: its first
coefficient is one, so it is primitive in the ACTUAL torus basis.
Take lambda as the complementary core curve. This is an integral
basis change of determinant one. From (3),(7), its exact developed
displacements in T are

    Delta_sigma T=-2pi i m,
    Delta_lambda T=V, Re V!=0.                         (8)

For the angle normalization use H3 around the vertical axis above k.
In upper-half-space coordinates set

    horizontal=k+exp(t)tanh(r)exp(i theta),
    height=exp(t)sech(r).

Direct differentiation gives

    ds^2=dr^2+sinh(r)^2 dtheta^2+cosh(r)^2 dt^2.

At fixed r, T=t+Log tanh(r)+i theta, so its periods ARE the
axial/rotational displacements (Re T,Im T). Equation (8) has zero
axial translation and angular displacement -2pi m. A small normal
circle therefore has circumference

    2pi |m| sinh(r)=2pi |m| r+O(r^3).                  (9)

For |m|=1 the axis has the ordinary smooth 2pi neighborhood. For
|m|=2 it is a 4pi branched neighborhood, although both cases have
scalar PSL meridional holonomy. This is the rigorous discriminant
that the scalar group relation alone cannot supply. In particular
the selected |m|=1 channels give a smooth primitive filling.

For m=1 the displayed meridian angle is -2pi; reversing the
orientation of the SAME primitive filling curve gives +2pi. This
is the usual orientation-reversing boundary attachment of a solid
torus, not a reversal of ambient volume. Formula (5) keeps the
positive cusp lattice orientation for either choice of signed slope.
More explicitly, for either unit sign choose

    meridian_tube=-m sigma, core_tube=m lambda.

Their angular period and axial length are respectively +2pi and
|Re V|. Relative to the original oriented (sigma,lambda) basis the
change has determinant -m^2=-1, exactly the boundary-orientation
reversal required to glue an ORIENTED solid torus. This works for
both signs of p without changing the orientation of H3.
The exact holomorphic reversed-cap isometry jointly inverts both
peripheral generators; it interchanges m=+1 and -1 and preserves
(9). No mu_+ -> mu_- framing shear occurs.

The ORIGINAL coherent source has no zero charge, and all 2^s unit
signed charges were proved to add. Thus it is exactly the quantum
selected channels, rather than an imposed primitive filling, that
meet the smooth-angle condition.

## 5. Scope and the direct geometric lemmas used for completion

The result proves the actual peripheral lift, loxodromic core
orientation and primitive smooth-angle calibration, using the
positive geometric cusp-link deformation near the established
complete anchor. It does NOT infer a hyperbolic metric from a bare
PSL representation. The independent
[finite-center positive-core proof](actual_long_pretzel_geometric_filling_completion.md)
now supplies the face-compatible local metric and these cusp links.
The [log-link/tube completion proof](long_pretzel_equality_critical_audit.md)
identifies the ENTIRE end with a standard punctured tube before
adding its smooth core. Both constructions have passed this note's
independent analytical review; no imported Dehn filling theorem is
being assumed correct without proof.

The final completion review checks the finite face-orbit centers and
cell cones, exact identity of each contractible edge-star holonomy
(including zero axis dilation), winding-one continuity, finite-vertex
spherical covering degree one, ideal similarity links and actual
vertical epigraphs. It also checks the signed surgery convention:
straightening mu+p lambda uses phi'=phi-p theta and inserts -p full
turns, so the original retained R^(-1) becomes R^(-(2p+1)). Thus the
completed oriented manifold is the actual source's filled knot.

Combined with the independently proved complete log-link and
whole-source/regulator theorems, this is a FULL equality certificate
on the unchanged class: each fixed odd s>=25 and independently
sufficiently large FIXED signed p_i, with the full N sequence,
both parities and composite levels. No slope comparability or
all-ideal triangulation assumption is needed for this completion.
It makes no assertion for small widths, short slopes, N-dependent
slopes/width, or arbitrary hyperbolic knots.

[Audit](../experiments/audit_actual_long_pretzel_primitive_filling_angle.py)
checks the exact spin/angle distinctions, signed independent core
length and orientation identities, the small affine logarithmic
increments, and the Fermi metric/circumference normalization.
