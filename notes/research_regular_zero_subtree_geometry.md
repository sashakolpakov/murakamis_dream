# Primitive geometry of a regular zero-power subtree

Research theorem, 2 November 2026. A regular minimizer of the
zero-power subtree potential gives the actual positive hyperbolic
geometry of the original meridian fillings. No small-angle bound
depending on the size of the subtree is needed. The proof uses
different cone angles at different vertices along the deformation.
It does not assume that all heights increase along a path with one
common prescribed cone angle.

This note supplies geometric input for a boundary-source theorem.
It does not replace the analytic proof that the complete quantum
sum has a nonzero leading contribution. Frozen manuscripts are
unchanged.

## 1. The original diagram and the regularity hypothesis

Let \(T\) be a fixed ordered circle tree, with its original tangle
stacks, quarter-turns, disk frames and peripheral curves. Let
\(S\) be a connected nonempty proper set of its original vertices.
Write \(E_S\) for all edges with at least one endpoint in \(S\),
counting internal edges once, and put \(m=|E_S|\).
Every selected original degree \(d_v\) is assumed at least three.

Fill every selected crossing circle to crossing power zero.
In the original conventions
\[
 n_v=\eta_v-2p_v,\qquad \eta_v\in\{-1,0,1\},
\]
this means \(\eta_v=p_v=n_v=0\). The filled slope is the
original primitive meridian \(\mu_v\); the disk longitude
\(\lambda_v^{\rm disk}\) is not rescaled. Every outside
angle is initially zero.

Use the potential from the
[convex minimization theorem](research_zero_power_subtree_convex_potential.md):
\[
 \mathcal L_S(\mathbf h)
   =\sum_{vw\in E_S}V(h_v,h_w)-\sum_{v\in S}h_v,
 \qquad h_w=0\quad(w\notin S).
 \tag{1}
\]
It has a unique finite minimizer \(\mathbf h^*\), all of whose
selected coordinates are positive. Set
\[
 r_v=\sinh(h_v^*/2).
\]
The hypothesis of this note is
\[
 r_vr_w<1\qquad(vw\subset S).
 \tag{2}
\]
An edge with (2) is called regular. Boundary edges are automatically
regular, since their outside height is zero.

**Theorem.** Under (2), the selected meridian fillings have a
positive cone deformation from the original complete augmented
exterior. The unfilled auxiliary cusps and all main cusps remain
complete. If \(E_0\) consists of the edges with both endpoints
outside \(S\), the resulting complete partially filled exterior
\(Y'\) satisfies
\[
 \operatorname{Vol}(Y')
   =2|E_0|v_{\rm oct}
        +2\pi\mathcal L_S(\mathbf h^*).
 \tag{3}
\]
The primitive equations continue holomorphically when the outside
angles vary near zero. The selected stationary action \(G_S\)
has
\[
 G_S(0)=\mathcal L_S(\mathbf h^*),\qquad
 (G_S)_{u_ju_k}(0)
  =-\delta_{jk}\frac{\cosh(h_{v(j)}^*/2)}{2\pi}.
 \tag{4}
\]
Here the \(j\)-th boundary edge joins its outside vertex to
\(v(j)\in S\).

## 2. The geometric edge potential

For heights \(h,g\ge0\), let
\[
 r=\sinh(h/2),\quad s=\sinh(g/2),\qquad rs<1.
\]
The original edge phase is
\[
 \psi_t(t,u)=-\frac1\pi\operatorname{arsinh}
                         (\tan(t/2)\cos(u/2)),
 \qquad \psi(0,0)=v_{\rm oct}/\pi.
\]
At \(t=-ih,\ u=-ig\), its continued derivatives are
\[
 \psi_t(-ih,-ig)=\frac{i\alpha_h}{\pi},\qquad
 \alpha_h
  =\arcsin\frac{r\sqrt{1+s^2}}{\sqrt{1+r^2}}
  \in[0,\pi/2).
 \tag{5}
\]
The analogous formula holds at the other endpoint. The regularity
condition is exactly the strict inequality placing the inverse-sine
argument below one.

The convex theorem proves \(V_h=\alpha_h/\pi\). Differentiating
\(\psi(-ih,-ig)\) with respect to \(h\) gives the same
derivative, and both functions have value \(v_{\rm oct}/\pi\)
at \((0,0)\). The regular nonnegative region is connected by
radial segments to zero. Consequently
\[
                 \psi(-ih,-ig)=V(h,g)
 \tag{6}
\]
on its original continued branch. In particular the equality
includes its additive constant.

## 3. A path with its actual individual cone angles

For \(0\le a\le1\), take the straight height path
\[
 h_v(a)=a h_v^*,\qquad t_v(a)=-ia h_v^*.
 \tag{7}
\]
Every internal edge remains regular: each factor
\(\sinh(a h_v^*/2)\) is at most its final value.
Define the individual charges by
\[
 c_v(a)=\frac1\pi\sum_{e\ni v}\alpha_{v,e}(a\mathbf h^*).
 \tag{8}
\]
The stationary equations of (1) give \(c_v(1)=1\), while
\(c_v(0)=0\).

Each \(c_v\) increases strictly. Indeed the own-height derivative
of \(\alpha_{v,e}\) is positive, and its derivative in the
other height is nonnegative. These are \(\pi\) times the
corresponding entries of the regular-edge Hessian
\[
 \nabla^2V(h,g)
 =\frac1{2\pi\sqrt{1-r^2s^2}}
  \begin{pmatrix}
   \dfrac{\sqrt{1+s^2}}{\sqrt{1+r^2}}&rs\\
   rs&\dfrac{\sqrt{1+r^2}}{\sqrt{1+s^2}}
  \end{pmatrix}.
 \tag{9}
\]
Since \(h_v^*>0\), the own derivative already makes the
derivative of (8) strictly positive. Thus \(0<c_v(a)<1\)
for \(0<a<1\), and every cone angle \(2\pi c_v(a)\)
increases from zero to \(2\pi\). No monotonicity assertion
about the solution of a different uniform-charge system is used.

Writing \(\Psi_S=\sum_{e\in E_S}\psi\), equations (5) and
(8) give the full unexponentiated equations
\[
              (\Psi_S)_{t_v}(\mathbf t(a))=i c_v(a).
 \tag{10}
\]

## 4. Positive original tetrahedra throughout the path

We use the exact shape formulas established from the original
ordered cross ratios in
[the adjacent-filling geometry](research_adjacent_two_crossing_pair.md#3-the-original-geometric-equations).
For an edge with half-angles \(H=t/2,\ K=u/2\), put
\[
 R_t=\exp\operatorname{arsinh}(\tan H\cos K),\qquad
 R_u=\exp\operatorname{arsinh}(\tan K\cos H).
\]
The eight original oriented shapes are
\[
 (A,B,-1/A,-1/B),\qquad(C,D,-1/C,-1/D),
 \tag{11}
\]
where
\[
 A=iR_t e^{-iK},\quad B=i e^{iH}/R_u,\quad
 C=i e^{-iK}/R_t,\quad D=i e^{iH}R_u.
 \tag{12}
\]
At imaginary angles \(t=-ih,\ u=-ig\),
\[
 R_t=e^{-i\alpha_h},\qquad R_u=e^{-i\alpha_g}.
\]
The four shapes in (12) therefore have positive moduli and
arguments
\[
 \frac\pi2-\alpha_h,\quad
 \frac\pi2+\alpha_g,\quad
 \frac\pi2+\alpha_h,\quad
 \frac\pi2-\alpha_g,
 \tag{13}
\]
respectively. All lie strictly between zero and \(\pi\).
The map \(z\mapsto-1/z\) preserves the upper half-plane,
so all eight shapes in (11) are positive.

The original rational coordinates also remain nonsingular.
Write
\[
 y=-i\tanh(h/2),\quad z=-i\tanh(g/2),\qquad
 p=\sqrt{1+y^2+z^2}
   =\frac{\sqrt{1-r^2s^2}}{\sqrt{1+r^2}\sqrt{1+s^2}}>0.
\]
Their equator is \((0,\infty,1,R)\), with
\[
 R=\frac{1+z^2}{p^2+1}\in(0,1).
\]
The two pairs of apices are
\[
 \left(\frac{p+y}{p-i},\frac{z-i}{p-i}\right),\qquad
 \left(\frac{p+y}{p+i},\frac{z+i}{p+i}\right).
 \tag{14}
\]
Here \(p\pm i\), \(p\pm y\), \(p\pm z\), \(1+y^2\),
and \(1+z^2\) are nonzero. Thus the original face formulas
continue without a pole or a collapsed tetrahedron. These are
the actual cells and markings of the
[circle-tree geometry paper](../papers/circle-tree-geometry/main.tex),
not an unrelated realization of the same exponentiated equations.

## 5. Gluing, completeness and primitive periods

The ordered face maps of the original construction are rational
identities in these coordinates. Along (7) they stay defined and
match every pair of pages in its prescribed order. Positivity and
continuation from the complete point preserve the full angle
sum at each ordinary edge, not only its value modulo \(2\pi\).
The original tetrahedra hence give nonsingular metric neighborhoods
at finite points.

At any free vertex its angle is zero, and every selected-edge
derivative there is zero:
\[
                      \psi_u(-ih,0)=0.
\]
Its longitude period is also zero. The free auxiliary cusps
therefore remain complete. The original main-cusp corner products
remain parabolic under the same face maps. The positive
horospherical triangles assemble into nonsingular compact torus
links; their peripheral holonomies are translations, so these
cusps also remain complete.

The original meridian and disk-longitude words give
\[
 U_v=-2\pi(\Psi_S)_{t_v},\qquad V_v=2it_v.
 \tag{15}
\]
The carrier contribution vanishes because \(\eta_v=0\).
As in the original log-link construction, any difference between
these chosen logarithms and the actual periods belongs to
\(2\pi i\mathbb Z\). It vanishes at the complete end and
is constant through the positive path. Thus (15) gives the
full primitive periods:
\[
 U_v=-2\pi i c_v(a),\qquad V_v=2a h_v^*>0
                        \quad(a>0).
 \tag{16}
\]
The meridian is the curve being filled. Its cone angle is
\(2\pi c_v(a)\), and the core length is \(2a h_v^*\).
At \(a=1\) the angle is \(2\pi\), giving the smooth original
zero-power filling. In particular there has been no replacement
of a primitive meridian by a multiple or by a different slope.

## 6. The absolute volume constant

Define the real stationary action along this path by
\[
 \mathcal S(a)=
     \sum_{vw\in E_S}V(a h_v^*,a h_w^*)
                  -\sum_{v\in S}a h_v^*c_v(a).
 \tag{17}
\]
Using the derivative equations (8), the terms involving
\(c_v h_v^*\) cancel, leaving
\[
              \mathcal S'(a)
                  =-\sum_{v\in S}a h_v^*c'_v(a).
 \tag{18}
\]
Schläfli's formula for core lengths \(2a h_v^*\) and angles
\(2\pi c_v(a)\) gives exactly \(2\pi\) times (18).
At \(a=0\), the incident edges give \(2m\) regular ideal
octahedra and \(\mathcal S(0)=m v_{\rm oct}/\pi\).
Therefore their final volume is
\[
 2\pi\mathcal S(1)=2\pi\mathcal L_S(\mathbf h^*).
\]
The untouched edges each contribute two regular ideal octahedra,
proving (3). This argument fixes the absolute volume; it is not
only an equality of differentials.

## 7. Boundary deformation and subsequent long fillings

The Hessian of (1) at a regular minimizer is positive definite,
by the full edge forms (9) and the positive scalar forms on
boundary edges. By (6), the selected geometric Hessian is
its negative. Hence the equations
\[
                   (\Psi_S)_{t_v}=i\quad(v\in S)
\]
extend holomorphically for small outside angles \(\mathbf u\),
with the selected primitive charges fixed at one. Positivity
persists on a sufficiently small neighborhood of the final point.
The continued stationary action is
\[
 G_S(\mathbf u)=
   \operatorname{stat}_{\mathbf t}
      \left[\Psi_S(\mathbf t,\mathbf u)-i\sum_{v\in S}t_v\right].
 \tag{19}
\]
At zero the mixed derivatives between a selected angle and an
outside angle vanish by separate evenness. An outside vertex can
meet only one vertex of this connected subtree, since the original
graph is a tree. Thus its boundary Hessian is exactly (4).

Different selected components can share an outside vertex. Their
incident-edge sets are disjoint, their face maps agree at the
common zero angle, and their boundary actions add before the
remaining trace is taken. Their negative diagonal Hessian
contributions add as well. Once the complete boundary-source
theorem is supplied for each component, these are precisely the
geometric and Hessian inputs required by the
[complex-phase long-filling theorem](research_long_fillings_complex_boundary_phase.md)
and the assembly in
[Section 10 of the connected-cluster note](research_connected_short_filling_clusters.md#10-a-volume-theorem-after-further-long-fillings).
The further long-filling path uses the original remaining
peripheral curves and starts from the absolute volume (3).

## 8. A degree condition with no dependence on component size

For a nontrivial selected component, the convex theorem gives
\[
 r_v<\tan(\pi/d_v).
\]
Consequently a sufficient combinatorial condition for (2) is
\[
 d_v\ge3,\qquad
 \tan(\pi/d_v)\tan(\pi/d_w)\le1
                      \quad(vw\subset S).
 \tag{20}
\]
This includes every selected subtree all of whose original degrees
are at least four, regardless of its number of vertices. It also
allows degree-three vertices when all their selected neighbors
have degree at least six. A singleton of degree at least three
is regular without any internal-edge condition.

Condition (20) is sufficient, not necessary. The theorem applies
whenever the unit minimizer itself is regular, because the
straight-height path proves the needed geometric continuation.
If an internal edge reaches its endpoint, the present
triangulation need not stay positive and this proof does not
apply. Two adjacent trivalent zero vertices give that boundary
case. The existence of a different strict Conway description or
a different primitive Newton critical point does not automatically
identify its geometry with the same filled exterior; that
comparison requires the separate
[literal zero-deletion and boundary-potential proof](research_zero_subtree_conway_geometry.md).
That proof now supplies the identification for every selected
original degree at least three, including the folded cases.
