# Completing the crossing-circle fillings and calibrating their volume

1 November 2026.

The octahedral cells of an ordered tree of crossing circles stay
positive while their angular longitude parameters vary in a fixed
small disk. This note proves that the parameter path selected by the
analytic filling equations completes those cells to the actual
filled link exterior. It follows the full logarithmic period of each
primitive filling curve, so the completed meridian makes exactly
one turn at the endpoint. It then identifies the absolute volume
with the continued critical action.

The [ordered decomposition](actual_all_circle_octahedral_decomposition.md)
supplies the original topology and primitive curves. The
[angular charts](actual_all_circle_angular_octahedra.md)
supply the positive cells and their exact face maps. The
[analytic criterion](actual_all_circle_curvature_filling_limit.md)
supplies the path under the explicit bound in (4).
Together these establish the geometric part of the
[quantitative volume theorem](actual_all_circle_quantitative_volume.md).
Only the original crossing circles are filled; the main knot cusp
remains complete and unfilled.

## 1. Exact topological and local inputs

Fix a finite circle-only Conway tree with at least two circle
vertices. Every edge is a physical quarter-turn and every vertex
is an original crossing circle. Keep its actual ribbon orders,
projection-copy labels, half twists and primitive disk curves.

The [ordered cut theorem](actual_all_circle_octahedral_decomposition.md)
supplies three marked facts.

- The original projection and disk-page cuts give two octahedra per
  edge, with the six vertices and face maps of the literal two-leaf
  [angular chart](actual_all_circle_angular_octahedra.md). Any transported
  corner permutations and projection-copy changes are retained.
- At each original circle, outgoing and incoming pages are joined
  in their actual cyclic order. The retained half twist occurs at
  its distinguished original seam. The face maps keep their full
  three-point labels.
- The disk longitude is the boundary loop with period \(V_v=2i\tau_v\).
  The original meridian concatenates the local meridional page paths,
  with the single half-longitude shear \(-\epsilon_vV_v/2\).
  These are the original primitive curves.

Physical \(T^{-1}\), \(T\), and retained planar half-turns are not
identified by source involutivity. Reversing a disk frame reverses
both its paths and its peripheral coordinate. All formulas below
use the fixed original disk basis.

The local positive eight-tetrahedron chart is valid on
\[
                         |\tau_v|,|\tau_w|\le10^{-2}.
\tag{1}
\]
Its incoming pants edge ratios are
\((-Q^{-1},-Q,-Q^{-1})\), and its outgoing ratios are their
inverses, where \(Q=e^{i\tau_v}\). Thus the marked seam cancels
the full complex shears, and its two interior-angle branches sum
to \(2\pi\). This includes both projection copies. At zero these
are the two regular octahedra in the actual two-leaf cut.

## 2. The analytic path and the actual peripheral formulas

Let \(F_0\) be the complete positive action, normalized so that
\(2\pi F_0\) is the volume of the original augmented exterior.
There are two regular octahedra per tree edge at completeness.
Let
\[
 \Psi(\boldsymbol\tau)=\sum_{\{v,w\}}\psi(\tau_v,\tau_w),
 \qquad \Psi(0)=F_0,
 \qquad
 \psi_{\tau_v}=-\frac1\pi\operatorname{arsinh}
          \bigl(\tan(\tau_v/2)\cos(\tau_w/2)\bigr).
\tag{2}
\]
The local action is separately even, with its complete branch and
constant. Fix the original signs \(\epsilon_v\in\{0,\pm1\}\),
integral fillings \(p_v\), and powers \(n_v=\epsilon_v-2p_v\).
The [analytic criterion](actual_all_circle_curvature_filling_limit.md)
supplies an analytic first-charge path
\(\boldsymbol\tau(c)\), \(0\le c\le1\), with
\[
 \Psi_{\tau_v}+\frac{i n_v\tau_v}{2\pi}-ic=0,\qquad
 \boldsymbol\tau(0)=0,\qquad
 |\tau_v(c)|<10^{-2},\qquad
 \Im\tau_v(c)<0\quad(c>0).
\tag{3}
\]
Write \(D_v\) for the circle-tree degree. The sufficient condition
and pointwise bound are
\[
 \sum_v\frac{D_v}{D_v^2+n_v^2}\le2^{-25},\qquad
 |\tau_v(c)|\le
 \frac{2\pi c}{(1-1/50)\sqrt{D_v^2+n_v^2}},
\tag{4}
\]
The common bound is less than \(0.00111\), inside (1). The geometric proof only uses the
explicit path properties (3).

In a pure local block the small meridional increment is
\(-2\pi\psi_{\tau_v}\). The ordered cut theorem consequently gives
the original peripheral logarithms
\[
 U_v=-2\pi\Psi_{\tau_v}-i\epsilon_v\tau_v,
                      \qquad V_v=2i\tau_v.
\tag{5}
\]
Their exponentials are the actual holonomy multipliers. Section 4
proves that the chosen lifts are also the actual log-link periods.
The stationary equation gives
\[
                         U_v+p_vV_v=-2\pi ic.
\tag{6}
\]
The primitive basis is not reset when \(U_v\) approaches
\(-2\pi i\).

## 3. Positive metric on the cut-and-glued exterior

Realize every local block by its positive tetrahedra and perform
the original identifications in Section 1. Within a block the
rational face identities retain the full edge return map. At a
page seam the inverse ratios give both zero shear and angle
\(2\pi\), not only equality of multiplier moduli. Their branches
are continued from the complete cells.

At the distinguished odd seam use the original cross-copy maps,
rather than the pure inverse-ratio identification. In the local
leaf frame of the angular chart they are
\[
 A=\begin{pmatrix}R&-R\\1&ER-1-E\end{pmatrix},\qquad
 B=\begin{pmatrix}R/E-1-1/E&R\\-1&R\end{pmatrix}.
\tag{6a}
\]
They send respectively
\((Z,\infty,1)\) to \((Z/E,R,0)\) and
\((Z,R,0)\) to \((Z/E,\infty,1)\). Thus they specify all three
ideal vertices and the actual exchange of projection copies.
With the four original white maps \(W_j\), direct multiplication
gives the full projective edge returns
\[
 W_0^{-1}BW_2^{-1}A=I,\qquad
 W_2^{-1}BW_0^{-1}A=I,\qquad
 W_1^{-1}BW_3^{-1}A=I.
\tag{6b}
\]
These are identities under
\(Z^2-(1+E)Z+ER=0\), not modulus comparisons. The incoming and
outgoing marked pants structures depend only on their common
\(Q=e^{i\tau_v}\), by the local edge-ratio calculation. Transport
each to the same ordered three-vertex pants chart. Equations
(6a)–(6b) then give the same odd seam between any two incident
blocks, even when their far-end parameters differ. The allowed
puncture exchange is exactly the one in (6a), not an arbitrary
pants permutation. Every resulting edge has its complete angle
branch \(2\pi\), by positivity and continuation from zero.
The two physical signs retain their distinct primitive words and
the single correction in (5).

This gives a nonsingular local hyperbolic metric at every finite
point of the original exterior. Face pairings are isometries,
edge links have angle \(2\pi\) and identity return, and a finite
subdivision vertex has a nonsingular spherical metric on its
topological sphere link. Its complete local spherical development
is the ordinary sphere. No global injectivity of the developing
map is assumed.

The actual horospherical triangles form a nonsingular similarity
structure on each topological cusp torus. Main puncture holonomies
are the nontrivial parabolics of the local pants and remain so in
the fixed local charts. The actual primitive main meridian is
one of these local words. Its commutant is the translation group
at its flag. Hence each main torus has a complete Euclidean
translation link.

For \(c>0\), (3) and (5) give
\[
                         \Re V_v=-2\Im\tau_v>0.
\tag{7}
\]
The auxiliary peripheral group has a nonunit dilation and a second
common fixed point \(q_v\). Its nonsingular similarity development
misses \(q_v\). Indeed \((z-q_v)\partial_z\) is a globally invariant
vector field; each possible zero has index \(+1\), whereas the
total index on a torus is zero.

On the simply connected link cover put
\[
                           f_v=\log(\operatorname{dev}_v-q_v).
\tag{8}
\]
Its real derivative is invertible. The metric \(|df_v|^2\)
descends to a nonsingular Euclidean metric on the compact torus,
and is complete. Geodesic path lifting makes \(f_v\) a covering
of the Euclidean plane; since the plane is simply connected,
it is a diffeomorphism. Its periods form an injective real
rank-two lattice.

## 4. The periods throughout the charge path

Let \(P_{\mu_v},P_{\lambda_v}\) be the actual periods of (8) on
the retained primitive paths. Their exponentials are the actual
peripheral multipliers, so
\[
               P_{\mu_v}-U_v,\quad P_{\lambda_v}-V_v
                                         \in2\pi i\mathbb Z.
\tag{9}
\]
These differences are continuous for \(0<c\le1\). The link
remains nonsingular, its development avoids the second fixed
point, and the paths and flags are retained. Choose a logarithm
at one basepoint and transport it continuously; rebasing adds a
constant and does not change a period.

The initial integers can be fixed directly from the complete charts.
Choose a peripheral frame depending continuously on the selected
flag and sending it to infinity. Write the longitude as
\(z\mapsto a(c)z+b(c)\), with \(a(c)=e^{V_v(c)}\).
At completeness \(a(0)=1\) and \(b(0)\ne0\), since the original
primitive longitude is a nonzero translation in the complete torus.
For \(c>0\), (7) makes \(a(c)\ne1\), and its second fixed point is
\(q_v(c)=b(c)/(1-a(c))\). Thus \(|q_v(c)|\to\infty\).

For this fixed finite tree, the developed fixed-generator paths
remain in one bounded region and have bounded Euclidean lengths
as \(c\downarrow0\). They use finitely many actual triangles and
transition maps, all continuous in the complete charts. If their
images lie in \(|z|\le B\) and their lengths are at most \(L\),
their actual logarithmic increments obey
\[
             |P_\gamma(c)|\le\frac{L}{|q_v(c)|-B}\longrightarrow0.
\tag{9a}
\]
Meanwhile (5) gives \(U_v,V_v\to0\). Each integer difference in
(9) is therefore zero for sufficiently small \(c\), and hence
on all of \((0,1]\). This fixes the winding without importing a
small-neighborhood completion theorem or resetting principal logs
at the endpoint.

Equivalently, each page increment in (5) is small in its local
two-leaf chart. Changes of a pants frame add logarithmic constants
at the ends of a page path; those constants telescope around the
circle. Its meridian accumulates the sum of the actual increments,
even when high degree makes that sum close to \(-2\pi i\).
The preceding continuity argument fixes the possible integer.

The actual slope period is thus \(-2\pi ic\). Its complementary
primitive curve is the original longitude: the determinant of
\((\mu_v+p_v\lambda_v,\lambda_v)\) in the original basis is one.
Its positive core translation length is
\[
                            \ell_v=\Re V_v=-2\Im\tau_v.
\tag{10}
\]

## 5. Cone completion and the smooth endpoint

The geometric end contains all sufficiently high vertical rays
over its similarity triangles. Send its fixed points to zero and
infinity, put \(r=y/|z|\), and use
\[
 R=\operatorname{arsinh}(1/r),\quad
 \theta=\Im f_v,\quad
 X=\Re f_v+\tfrac12\log(1+r^2).
\tag{11}
\]
The metric is exactly
\[
                  dR^2+\cosh^2R\,dX^2+\sinh^2R\,d\theta^2.
\tag{12}
\]
Compactness of the actual similarity link shows that the end
contains a whole punctured tube \(0<R<R_0\). Its primitive
meridian period is \(-2\pi ic\), and its independent longitude
has positive real part (10). Adding the axis produces a cone
solid torus of angle \(2\pi c\), with the specified topological
meridian. At \(c=1\) it is an ordinary smooth solid torus.

Main cusps remain complete horoball quotients, and the remaining
middle is compact. Thus the \(c=1\) metric is complete and has
finite volume on the original filled topology. The complete
universal local development covers simply connected hyperbolic
space, so the resulting representation is the geometric holonomy.
When the original component test gives one main component, the
metric is on that original knot complement. Its main cusp is
unfilled.

The intermediate cone description makes no discreteness claim
for \(0<c<1\). It records the positive metric and its actual
link completion; smoothness is asserted at \(c=1\).

## 6. Absolute action and the primitive normalization

The calibration can be derived on this explicit geometric block
family. It does not require choosing an unmarked character
component by comparison of its derivatives at one point.

Put \(U_v^0=-2\pi\Psi_{\tau_v}\) and
\[
 G^0=2\pi i\left(\Psi-\sum_v\tau_v\Psi_{\tau_v}\right).
\tag{13}
\]
Direct differentiation gives
\[
                         dG^0=\tfrac12\sum_vV_v\,dU_v^0.
\tag{14}
\]
The actual half twist changes \(U_v^0\) to
\(U_v=U_v^0-\epsilon_vV_v/2\). Its marked primitive is therefore
\[
 G=G^0-\sum_v\frac{\epsilon_vV_v^2}{8}
 =2\pi i\left(\Psi-\sum_v\tau_v\Psi_{\tau_v}\right)
                          +\sum_v\frac{\epsilon_v\tau_v^2}{2}.
\tag{15}
\]
This is exactly the source Legendre transform with its complete
constant. In particular \(\Im G(0)=2\pi F_0\).

The original boundary fundamental-chain differential, applied to
these actual positive blocks and their marked paths, gives
\[
             \operatorname{Vol}(\rho)
                  =\Im G-\tfrac12\sum_v\Re U_v\Im V_v.
\tag{16}
\]
The constant is fixed at the complete assembly. Every local shape
stays in a simply connected positive neighborhood of \(i\), and
Section 4 retains the actual period lifts. No volume period is
reset. The positive tetrahedral volume sum also shows directly
that the volume tends to \(2\pi F_0\) as \(c\downarrow0\).

Define the stationary charge action
\[
 \mathcal C(c)=\operatorname*{stat}_{\boldsymbol\tau}
 \left[\Psi+\frac{i}{4\pi}\sum_vn_v\tau_v^2
                                  -ic\sum_v\tau_v\right].
\tag{17}
\]
At its critical point, set \(\Phi=G/(2\pi i)\). Substitution of
(3) gives the exact cancellation
\[
 \Phi-\mathcal C(c)=-\frac{i}{2\pi}\sum_vp_v\tau_v^2,
 \qquad
 \tfrac12\Re U_v\Im V_v=p_v\Im(\tau_v^2).
\tag{18}
\]
Consequently
\[
                           \operatorname{Vol}_c
                                     =2\pi\Re\mathcal C(c).
\tag{19}
\]
The primitive normalization has an independent differential check:
\[
             \frac{d}{dc}\,2\pi\Re\mathcal C(c)
                                  =2\pi\sum_v\Im\tau_v.
\tag{20}
\]
The core is represented by the complementary primitive curve
\(\lambda_v\), its length is (10),
and its cone angle is \(2\pi c\). The finite-cell Schläfli
differential \(-\tfrac12\sum_v\ell_v\,d(2\pi c)\) gives (20).
This checks the factor and sign; (19) already follows from the
marked regulator and the complete anchor, without cone rigidity.

At \(c=1\), (19) identifies the actual analytic first-charge rate
with the original smooth filled volume. The ordered topological
theorem and the analytic criterion supply the topology and path
(3) used in this proof. The finite-source dominance and its exact
normalization are proved in the
[analytic theorem](actual_all_circle_curvature_filling_limit.md).

## 7. Scope of the completion

The metric argument permits large global meridian logs while every
edge block remains uniformly close to its regular geometry. It
does not require a globally small framed-representation norm.

The conclusion applies to the ordered all-circle trees of Section 1
under (4), or more generally whenever their actual analytic path
satisfies (3). It does not assert that every bounded crossing power
gives a hyperbolic filling. The degree-weighted bound permits some
small powers because the resulting local angular changes remain
small while the primitive meridian is assembled from many sectors.

The [preferred-cusp continuation](actual_all_circle_preferred_cusp.md)
also follows the actual main longitude through this family.
Its marking is established by the original face words and surgery
homology. The complete geometric and analytic conclusions are
collected in the
[quantitative volume theorem](actual_all_circle_quantitative_volume.md).
