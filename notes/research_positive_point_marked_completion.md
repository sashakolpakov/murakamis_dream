# Completing a positive primitive solution with its original marking

A positive solution of the original circle-tree filling equations,
with negative imaginary boundary angles at the selected circles,
already determines the actual marked hyperbolic filling. A path of
solutions with fixed slopes is not needed for this conclusion.

The proof uses a different path for a specific purpose: it contracts
the positive tangent coordinates to the complete structure while
keeping each selected longitude loxodromic. That path identifies the
full logarithmic periods of the original peripheral curves. The
primitive filling equations are imposed only at its endpoint.
The local tube completion then gives the original smooth filling.

This extends the geometric argument in Section 6 of the
[circle-tree geometry manuscript](../papers/circle-tree-geometry/main.tex),
with its original cut cells, page order and primitive curves.
No manuscript is modified here.

## 1. Statement and conventions

Let \(Y\) be an original ordered circle-tree exterior with at least
one edge, as defined by the marked cut construction in that manuscript.
Retain every original half-twist carrier, disk frame, page order,
main component and auxiliary cusp. At an auxiliary vertex \(v\),
the primitive basis is \((\mu_v,\lambda_v)\), where \(\lambda_v\)
is the original disk longitude. Choose selected vertices \(S\),
original integer filling coefficients \(p_v\), and carriers
\(\eta_v\), and put
\[
                         n_v=\eta_v-2p_v.
 \tag{1}
\]
The outside angles are zero. For a selected vertex use a complex
angle \(t_v\) on the canonical branch \(|\Re t_v|<\pi\).
For an edge \(e=\{v,w\}\), put
\[
 a_v=\tan(t_v/2),\quad a_w=\tan(t_w/2),\qquad
 q_e^2=1+a_v^2+a_w^2.
 \tag{2}
\]
The positive branch is the one characterized by
\[
                  \Re q_e>
                  \sqrt{(\Re a_v)^2+(\Re a_w)^2}.
 \tag{3}
\]
This is exactly positivity of the eight original ordered tetrahedra,
as proved in
[the positive edge theorem](research_positive_edge_global_monotonicity.md).
Define the original returns by
\[
             r_{v,e}
              =\operatorname{arsinh}
                     \bigl(\tan(t_v/2)\cos(t_w/2)\bigr),
 \tag{4}
\]
on the same canonical positive branch.

**Theorem 1.** Suppose (3) holds at every original edge,
\(\Im t_v<0\) for \(v\in S\), and the full logarithmic equations
are
\[
                  \sum_{e\ni v}r_{v,e}
                         =\frac{i n_v}{2}t_v-\pi i
                  \qquad(v\in S).
 \tag{5}
\]
Then the original cells glue to a hyperbolic metric on \(Y\)
whose completion is the smooth Dehn filling along the original
primitive curves \(\mu_v+p_v\lambda_v\).
Every main cusp and every unselected auxiliary cusp is complete.
The filled core at \(v\) has length \(-2\Im t_v>0\).

Let \(\Psi=\sum_e\psi(t_v,t_w)\) include every original edge,
including complete edges outside the selected region. Then
\[
 \operatorname{Vol}Y(\mathbf p)
  =2\pi\Re\left\{
       \Psi+\frac{i}{4\pi}\sum_{v\in S}n_vt_v^2
                         -i\sum_{v\in S}t_v
           \right\}.
 \tag{6}
\]
This is a geometric statement. It does not assert that an original
quantum source has this exponential rate.

## 2. A positive path used to fix branches

We give the contraction explicitly. On one edge set
\[
 X=(\Re a_v)^2+(\Re a_w)^2,\quad
 Y_0=(\Im a_v)^2+(\Im a_w)^2,\quad
 Z=\Re a_v\Im a_v+\Re a_w\Im a_w,\quad
 D_0^2=XY_0-Z^2.
 \tag{7}
\]
Writing \(q=P+iQ\), the identity \(q^2=1+a_v^2+a_w^2\)
gives
\[
                    X-D_0^2=(P^2-X)(X+Q^2).
 \tag{8}
\]
For \(X>0\), positivity (3) is equivalent to \(D_0^2<X\),
with the square root chosen to have positive real part.
Conversely this strict inequality excludes a nonpositive real
value of \(q^2\): such a value would have \(Z=0\) and
\(Y_0\ge1+X\), contradicting \(D_0^2<X\).
When \(X=0\), positivity is exactly \(Y_0<1\).

Therefore
\[
                  a_v(\rho)=\rho a_v,\qquad 0\le\rho\le1
 \tag{9}
\]
preserves every positive edge simultaneously.
For \(X>0\) its criterion is
\(\rho^4D_0^2<\rho^2X\); for \(X=0\) it is
\(\rho^2Y_0<1\).
The angle branch is
\[
               t_v(\rho)=2\arctan(\rho a_v).
 \tag{10}
\]
The positive domain excludes the inverse-tangent cuts
\(a_v\in i[1,\infty)\cup-i[1,\infty)\).
For example, if \(\Re a_v=0\), \(|\Im a_v|\ge1\), and
\(\Re a_w\ne0\), then \(D_0^2\ge X\); if both real parts
are zero, then \(Y_0\ge1\). Thus (10) is the continuous
canonical branch throughout the contraction.

The sign of \(\Im\tan(t/2)\) is the sign of \(\Im t\) in
the canonical strip. Also the principal inverse tangent takes
the lower half-plane, with its excluded cut removed, to
negative imaginary part. It follows that
\[
             \Im t_v(\rho)<0\qquad
                         (v\in S,\ 0<\rho\le1).
 \tag{11}
\]
All outside angles stay zero. The path generally does not
satisfy (5), and is not being called a fixed-slope cone path.

## 3. The original gluing is regular on this whole path

The original face coordinates on an edge are rational functions
of \(a=a_v\), \(b=a_w\), and \(q=q_e\). In particular
\[
 E=\frac{q+i}{q-i},\quad
 R=\frac{1+b^2}{q^2+1},\quad
 R_1=1-R=\frac{1+a^2}{q^2+1},\quad
 Z_1=\frac{q+b}{q-i}.
 \tag{12}
\]
On the positive domain, \(\Re q>0\), so \(q,q\pm i\ne0\).
Moreover
\(\Re(q\pm a),\Re(q\pm b)>0\), hence these factors are
nonzero. The excluded inverse-tangent cuts give \(a\pm i\ne0\)
and \(b\pm i\ne0\).
Thus \(E,R,R_1\) are nonzero. The further apex denominators factor as
\[
 Z_1-R_1=\frac{(q+b)(b+i)}{q^2+1},\qquad
 Z_1-E R_1=\frac{(q+b)(b-i)}{(q-i)^2},
 \tag{13}
\]
and are nonzero, as are the expressions obtained by interchanging
the endpoints. Every face triple remains distinct because the
original tetrahedra are positive.

Consequently all original face maps are nonsingular on (9).
The original incoming and outgoing doubled disk triangles have
the complex edge ratios in equation \(\mathrm{ctg:pants}\) of
the manuscript. They depend only on the shared angle through
\(Q_v=e^{it_v}\), including the complex shears.
The ordered page gluing therefore remains the same full face
identification. The pure and odd edge-return matrix identities
in equations \(\mathrm{ctg:pure\text{-}returns}\) and
\(\mathrm{ctg:odd\text{-}returns}\) are rational identities in
these regular variables. They continue on the entire path.

In the fixed topological triangulation, every edge product is
therefore one. Its sum of positive dihedral angles is continuous,
is an integral multiple of \(2\pi\), and equals \(2\pi\) at
the complete endpoint. It remains \(2\pi\).
Thus the abstract glued tetrahedra give a nonsingular oriented
hyperbolic metric at every finite point of the original exterior.
This does not require that a deformed projection half-ball remain
convex or that its development be globally injective.

## 4. Complete main and outside cusps

The main meridians are the original corner words
\(W_{j-1}^{-1}W_j\), or their transported inverses.
Their multipliers at the corner flags are identically one.
They remain nonidentity on the full positive domain.
For example
\[
                    W_0^{-1}W_1:z\longmapsto z+(E-1),
 \qquad
                    E-1=\frac{2i}{q-i}\ne0.
 \tag{14}
\]
The other consecutive white maps cannot coincide projectively:
the \(W_1,W_2\) pair has respectively zero and nonzero lower-left
entries; the \(W_2,W_3\) pair has respectively nonzero and zero
upper-right entries, since \(R(E-1)\ne0\); and the \(W_3,W_0\)
pair again has nonzero and zero lower-left entries.
Thus all these marked main meridians are nontrivial parabolics.

Every commuting peripheral transformation is a translation in
the same fixed-flag affine chart. The horospherical triangles
form a nonsingular similarity structure on the compact
topological cusp torus. With translation holonomy its Euclidean
metric descends and is complete, so the corresponding main end
is an ordinary complete cusp.

At an unselected auxiliary vertex, \(t_v=0\) and
\(r_{v,e}=0\) for every incident edge. Its two peripheral
multipliers are one. Its similarity holonomy is therefore
translational as well, and the same compact-link argument proves
completeness. A zero translation for an individual peripheral
generator cannot cause a degeneracy: the complete flat link
has an injective translation lattice.

## 5. The full logarithms at a selected end

The actual primitive words of the manuscript give affine
multipliers with continued logarithms
\[
 U_v=2\sum_{e\ni v}r_{v,e}-i\eta_vt_v
                   =-2\pi\Psi_{t_v}-i\eta_vt_v,\qquad
 V_v=2it_v.
 \tag{15}
\]
These are initially logarithms of multipliers. We now verify
that they are the full periods of the original primitive paths,
including their winding integers.

For \(0<\rho\le1\), equation (11) gives
\(\Re V_v=-2\Im t_v>0\).
Send the original selected ideal flag to infinity. The
longitude has a nonunit affine multiplier, so the abelian
peripheral holonomy has a second common fixed point \(q_v\)
in this affine chart.

Its similarity development misses \(q_v\).
Indeed the vector field \((z-q_v)\partial_z\) is invariant
under the peripheral affine holonomy. Its pullback by the
similarity development therefore descends to the compact
link torus. Every zero would have index \(+1\), because
the similarity development is locally orientation-preserving.
The sum of indices is the Euler characteristic zero.
Thus there are no zeros.

On the simply connected link cover one may consequently set
\[
                         f_v=\log(\operatorname{dev}_v-q_v).
 \tag{16}
\]
Its derivative is everywhere nonsingular. The metric
\(|df_v|^2\) descends to a smooth Euclidean metric on the
compact torus and is complete. Its lifted developing map
\(f_v\) covers the Euclidean plane; since that plane is
simply connected, it is a diffeomorphism.
The two generator periods therefore form an injective
real rank-two lattice.

Let \(P_{\mu_v},P_{\lambda_v}\) be these periods along the
original oriented primitive curves. Their exponentials are
the multipliers computed in (15), so
\[
          P_{\mu_v}-U_v,\quad P_{\lambda_v}-V_v
                                      \in2\pi i\mathbb Z.
 \tag{17}
\]
The integers are continuous along \(0<\rho\le1\).
The link is nonsingular, its selected flag and original
paths are retained, and the nonunit multiplier never disappears.

To fix the integers, use a continuous affine frame near
\(\rho=0\), and write the longitude as
\(z\mapsto a(\rho)z+b(\rho)\).
At completeness \(a(0)=1\) and \(b(0)\ne0\), because the
original primitive longitude is a nonzero translation on the
complete Euclidean torus. Its second fixed point is
\[
                           q_v=\frac{b}{1-a},
 \tag{18}
\]
which tends to infinity as \(\rho\downarrow0\).
The original generator paths pass through finitely many link
triangles. Their affine images and Euclidean lengths remain
bounded, say by \(B\) and \(L\), near completeness. Hence
\[
               |P_\gamma(\rho)|
                    \le\frac{L}{|q_v(\rho)|-B}
                    \longrightarrow0.
 \tag{19}
\]
Also \(U_v,V_v\to0\). Thus both integers in (17) vanish
near zero, and then along the entire path.
The endpoint values in (15) are exactly the original
full primitive periods. This argument used the positive
unfilled contraction, not the filling equation at intermediate
parameters.

## 6. The endpoint solid torus

At the endpoint, (1) and (5) give
\[
                           U_v+p_vV_v=-2\pi i.
 \tag{20}
\]
In the affine chart sending the two fixed points to zero
and infinity, write upper-half-space coordinates as \((z,y)\),
put \(r=y/|z|\), and use
\[
 \varrho=\operatorname{arsinh}(1/r),\qquad
 \theta=\Im f_v,\qquad
 X=\Re f_v+\tfrac12\log(1+r^2).
 \tag{21}
\]
Direct substitution into \(y^{-2}(|dz|^2+dy^2)\) gives
\[
        d\varrho^2+\cosh^2\varrho\,dX^2
                              +\sinh^2\varrho\,d\theta^2.
 \tag{22}
\]
The original ideal end contains all sufficiently high vertical
rays over its finitely many similarity triangles.
Those triangles miss the second fixed point, and their quotient
is compact. Thus the end contains a full punctured tube
\(0<\varrho<\varrho_0\) in (21).

The original primitive curve \(\mu_v+p_v\lambda_v\) has
zero real period and angular period exactly \(-2\pi\).
Its complementary curve is the original \(\lambda_v\),
since the change of primitive basis has determinant one.
Its positive real period is
\[
                          \ell_v=\Re V_v=-2\Im t_v>0.
 \tag{23}
\]
Adding the axis \(\varrho=0\) therefore gives a smooth solid
torus with the prescribed primitive meridian, not a multiple
cover or an unspecified slope. Its core length is \(\ell_v\).

After performing this completion at every selected end, the
remaining cusp ends are complete and the middle is compact.
The resulting smooth metric is complete and has finite volume
on the original marked filling \(Y(\mathbf p)\).
Its universal local development covers simply connected
hyperbolic space and is an isometry.
This proves the geometric assertion of Theorem 1.

Finally the original tetrahedron interiors partition the metric
away from their faces and the completed cores, all of which have
measure zero. Their volume sum is therefore the actual hyperbolic
volume. The
[pointwise volume identity](research_positive_edge_volume_identity.md)
gives (6), including its absolute additive constant.

## 7. The explicit negative-corridor class

**Corollary 2.** In an original circle tree, select a connected
path with at least one outside end, with original selected degrees
one or two. Fix negative crossing powers \(n_v=-b_v\), with
\[
                            b_v\ge3\qquad(v\in S),
 \tag{24}
\]
and retain the original carrier parity and integral slopes.
Then the selected filling, with all other auxiliary cusps left
complete, has its original marked hyperbolic structure.
Its volume is given by (6).

**Proof.** The
[negative-corridor variational theorem](research_negative_corridor_variational_bounds.md),
Theorem 15, gives an interior positive solution of (5) at unit charges.
It also proves \(\Im t_v<0\).
Theorem 1 applies. \(\square\)

The threshold in (24) is independent of the number of selected
vertices. The last two corner cases in the variational proof use
an exact rational interval certificate; its full domain and
reproducible bounds are given there. The original slopes and carrier
conventions are unchanged. This is a geometric conclusion and does
not supply a quantum asymptotic.

If the phase includes only edges incident to the selected path,
add \(8G=2v_{\rm oct}\) for each omitted complete original edge
to the right side of (6).
Several nonadjacent selected paths may be treated simultaneously:
their incident edge sets are disjoint, even when they share an
outside vertex. At that vertex the angle is zero, so all original
interface maps and complete periods match in their recorded order.

The full logarithmic period Jacobian at an interior solution is
nonsingular: the real part of the return Jacobian is positive
definite, whereas the crossing contribution is purely imaginary
on the diagonal. Hence the implicit function theorem also gives
the marked boundary deformation germ near this complete outside
point, with all selected primitive periods fixed at (20).
Positivity and the core length signs persist locally.
No new meridian or longitude is chosen in this continuation.

The theorem does not resolve arbitrary coefficients two and three
in a negative corridor. The
[exact rational normal form](research_definite_rational_corridor_normal_form.md)
still retains those coefficients, boundary shifts and rotations.
Nor does the geometric theorem establish saddle survival in the
original finite quantum source. Those remain separate problems,
and no cofinite assignment statement follows from this corollary.

## 8. Reproducing the original-coordinate checks

The separate
[checker](../experiments/check_positive_corridor_completion.py)
solves sixteen original primitive systems in the explicit corridor
class. It checks the logarithmic filling residuals, the core signs,
the full rational face denominators and positive tetrahedron shapes
along the tangent-radial contraction. It also compares the direct
tetrahedron volumes with the calibrated stationary action.

    .venv/bin/python experiments/check_positive_corridor_completion.py \
      --precision 110 --output /tmp/positive-corridor-completion-replay.json

The [saved replay](../repro/results/research-positive-corridor-completion-root.json)
records 900 positive edge checks along those contractions, at
110 decimal digits. Its script SHA256 is
1041957cc7a3ee5fb21133db3d92e6a1d789ec8266d8b4d005aafb11814e2b64.
These are finite checks of the formulas and conventions.
The marked topological completion and the uniform theorem
are supplied by the written proof above.
